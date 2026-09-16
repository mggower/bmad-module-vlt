#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Cycle 16 build-1 — the convention-side fixture for acceptance check (1) Stub read (brief F2; Q2, D5
one-off). Reads the SHIPPED `wiki-index.md` BY PATH — never a copy — so a shipped-heading change fails
the harness (the instrument-beat property: a fixture that is a copy of the convention is not the
instrument).

Two readers over §The Stubs section, each returning the heading text a reader takes from the prose:

  Reader A — fence-NAIVE section scan (the read that broke, A16-1): from the line `## The Stubs
            section` to the next line matching `^## ` — whatever it is, fenced or not — take the first
            inline code span whose text begins `## ` and return the text after `## `. Under v0.18.0
            bytes the scan terminates on the fenced `## Stubs (linked, not yet written)` line and finds
            no span → none. Under F1's bytes the span in the prose sentence is found first.
  Reader B — fence-AWARE: strip fenced blocks over the whole file first (the fence semantics of
            lint-page-facts.py's strip_code; inline spans KEPT), then the same section scan. Under
            v0.18.0 → none (no prose statement exists); under F1 → the heading.

Cases: the shipped base; the base merged with `build-1-wiki-index.overlay.md` (base bytes, newline,
overlay bytes — full-scale.md step 2's merge order) where the overlay appends one bullet to §The Stubs
section; and, end to end, the returned heading applied to the Cycle 15 index pair under the collection
rule at checks.md Missing targets (locate the `## ` heading whose text equals it; collect every
backtick-wrapped slug in that section's list items up to the next `## `): `build-3-index-stubs.md` →
located: yes, 3 slugs; `build-3-index-bare-stubs.md` → located: no, 0 slugs.

Failability: `--convention <path>` runs the same table over another copy — the builder runs it over
`git show v0.18.0:skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md` and records the
FAIL count in the BUILT record (expected: both readers FAIL on the heading in both cases, and the
long-form index case FAILS by consequence; the bare index case passes coincidentally — none ⇒ no).

Run: uv run factory/cycles/16-closed-loops/fixtures/build-1-stub-heading-harness.py [--convention <path>]
Exit 0 when every expectation holds, 1 otherwise. No dependency.
"""

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
SHIPPED = os.path.join(REPO, "skills", "vlt-setup", "assets", "governance", "_meta", "conventions", "wiki-index.md")
OVERLAY = os.path.join(HERE, "build-1-wiki-index.overlay.md")
C15 = os.path.join(REPO, "factory", "cycles", "15-nothing-reads-it-back", "fixtures")
INDEX_LONG = os.path.join(C15, "build-3-index-stubs.md")
INDEX_BARE = os.path.join(C15, "build-3-index-bare-stubs.md")

SECTION = "## The Stubs section"
EXPECTED_HEADING = "Stubs (linked, not yet written)"  # the human reading of the convention's rule — the oracle
FENCE_OPEN = re.compile(r"^\s*(`{3,}|~{3,})")
FENCE_CLOSE = re.compile(r"^\s*(`{3,}|~{3,})\s*$")
SPAN = re.compile(r"`([^`]+)`")
SLUG = re.compile(r"`([^`]+)`")


def read(path):
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8")


def strip_fences(text):
    """Fenced blocks removed (lint-page-facts.py's fence rule); inline spans kept — the reader needs them."""
    out, fence = [], None
    for line in text.split("\n"):
        if fence is None:
            m = FENCE_OPEN.match(line)
            if m:
                fence = (m.group(1)[0], len(m.group(1)))
                continue
            out.append(line)
        else:
            m = FENCE_CLOSE.match(line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1]:
                fence = None
    return "\n".join(out)


def section_scan(text):
    """From the section heading line to the next `## ` line: the first inline span beginning `## `."""
    lines = text.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.rstrip() == SECTION)
    except StopIteration:
        return None
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        for span in SPAN.findall(line):
            if span.startswith("## "):
                return span[3:]
    return None


def reader_a(text):
    return section_scan(text)


def reader_b(text):
    return section_scan(strip_fences(text))


def locate(index_text, heading):
    """checks.md Missing targets' collection rule: (located, slugs)."""
    if heading is None:
        return False, []
    lines = index_text.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.rstrip() == "## " + heading)
    except StopIteration:
        return False, []
    slugs = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        if line.lstrip().startswith("- "):
            slugs.extend(SLUG.findall(line))
    return True, slugs


def main(argv):
    ap = argparse.ArgumentParser(description="the convention-side stub-heading fixture")
    ap.add_argument("--convention", default=SHIPPED, help="the wiki-index.md to read (default: the shipped file, by path)")
    args = ap.parse_args(argv)

    base = read(args.convention)
    merged = base + "\n" + read(OVERLAY)
    long_index, bare_index = read(INDEX_LONG), read(INDEX_BARE)
    rows = []

    def expect(label, got, want):
        rows.append((label, got == want, got, want))

    print("convention: %s" % os.path.relpath(args.convention, REPO) if args.convention.startswith(REPO) else "convention: %s" % args.convention)
    a, b = reader_a(base), reader_b(base)
    expect("reader A (fence-naive) over the base → the heading", a, EXPECTED_HEADING)
    expect("reader B (fence-aware) over the base → the heading", b, EXPECTED_HEADING)
    expect("reader A over base + overlay (append-only bullet) → the heading", reader_a(merged), EXPECTED_HEADING)
    expect("reader B over base + overlay → the heading", reader_b(merged), EXPECTED_HEADING)
    expect("readers A and B agree on the base", a, b)
    heading = a if a == b else None
    expect("index side: build-3-index-stubs.md → located: yes, 3 slugs", locate(long_index, heading), (True, ["birria", "jesse-minter", "nfl-draft-safety-archetypes"]))
    expect("index side: build-3-index-bare-stubs.md → located: no, 0 slugs", locate(bare_index, heading), (False, []))
    expect("the fenced example still carries its copy (the heading is stated twice on purpose — disposition 3)", base.count("## " + EXPECTED_HEADING), 2)

    failed = 0
    for label, ok, got, want in rows:
        failed += not ok
        print("%s  %s%s" % ("PASS" if ok else "FAIL", label, "" if ok else " — got %r, expected %r" % (got, want)))
    print("\nbuild-1 stub-heading harness: %d rows, %d failed" % (len(rows), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
