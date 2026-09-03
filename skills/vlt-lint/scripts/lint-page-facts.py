#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Derive the two per-page BYTE FACTS the vlt-lint fan-out's link graph and summary-length
clauses run on: every `[[ ]]` inner text on each page (raw) and each page's parsed `summary:`
length in characters. Cycle 15 build-4 (A15-1 / A15-3 / A15-4 fidelity half / A15-5; D-C, D-A).

Why this exists: the fan-out's reduce (`vlt-lint-full.js`) has no filesystem access and used to
build its inbound map and its missing-target list from whatever link list the page SCANNERS
returned — a link the scanner dropped did not exist (three consecutive false orphans),
a stripped `#` turned a same-page anchor into a missing page, a substituted proper noun reached
`missing_targets` and the findings cache made it permanent, and the scanner's own summary-length
verdict counted the raw YAML line. The link set and the length now come from the side of the
boundary that can read bytes: the SKILL runs THIS script and passes its two maps across as
`pageLinks` / `summaryLengths` (the `crossLayerSlugs` / `pageHashes` precedent); the scanner is
no longer asked for links at all.

FACTS, NEVER VERDICTS. This script emits raw inner texts and an integer length. The normal form
(`normalizeTarget`, B5-3) and the 160-character verdict stay in the workflow, where they already
live — a verdict here would put the limit in a second home.

Input   --pages <path|->   a JSON array `[{slug, path}]` — the same list the SKILL builds at
                           `references/full-scale.md` step 1. The two maps are keyed by the
                           SKILL-SUPPLIED slug, never one this script derives (the cacheRecords
                           principle: keying on anything else lets a derivation drift from the
                           population).
Output  --out <path>       (default stdout) one JSON object:
          {"pageLinks": {slug: [inner, ...]}, "summaryLengths": {slug: int},
           "unreadable": [slug, ...], "pages": N}
        At scale the SKILL writes it to the scratch directory and the wrapper-writing step
        (full-scale.md step 3) embeds the two maps — the payload never transits the caller.

pageLinks — the executable form of `references/checks.md` Missing targets' POPULATION statement:
only `[[ ]]`-delimited text is an outbound link; a `[[wikilink]]` inside an inline code span or a
fenced code block is not one ({conventions}/frontmatter.md rule 5); bare text, a filename or a
path that is not `[[ ]]`-delimited is not one. Concretely: the file's bytes read as UTF-8; fenced
blocks (a line opening with ``` or ~~~, to the matching closer — same fence character, at least
as long; an unclosed fence runs to end of file) removed; inline spans (a run of N backticks to
the next run of exactly N on the same line) removed; then every match of `\\[\\[([^\\[\\]]+?)\\]\\]`
yields its inner text RAW — `|alias`, `#anchor`, path prefix all intact; an embed's leading `!`
is outside the brackets and is not part of the text. FRONTMATTER IS SCANNED LIKE BODY TEXT — a
wiki page's quoted `"[[path]]"` `sources:` entry is a link (rule 4: a wiki page's `sources:` is a
link graph). Duplicates are kept as they occur; the reduce sets them.

summaryLengths — the parsed scalar's length in CHARACTERS (code points), never bytes
(frontmatter.md: counting characters, not bytes — em-dashes count as one). The frontmatter block
is the leading `---` line to the next `---` / `...` line; the first `summary:` line's value is
unquoted per its form — double-quoted (`\\"`, `\\\\` unescaped), single-quoted (`''` -> `'`), plain
(a trailing ` #comment` stripped); a block-scalar indicator (`>` / `|`, a form rule 2 forbids)
collects its indented continuation lines joined by one space — a documented approximation. The
length is Python `len()` of that string. No frontmatter, no `summary:` key, or an empty value
-> 0, which the reduce renders as `summary missing`.

No dependency (`requires-python` only, the lint-cache.py precedent): the module's release gate
and every vault must run it with nothing installed. A PyYAML parse would be the honest "parsed
scalar" but is not available at that cost, and the three quoted/plain forms above are the whole
of what the convention permits.

unreadable — a page whose bytes cannot be read or decoded is listed by slug and absent from both
maps; the workflow renders the gap as a denominated coverage cap.

Exit 0 whenever the input parsed; non-zero only for an unreadable `--pages` input (2) or an
unwritable `--out` (3). No `--self-test`: the factory harness is the test, a vault runs none.
"""

import argparse
import json
import re
import sys

WIKILINK = re.compile(r"\[\[([^\[\]]+?)\]\]")
FENCE_OPEN = re.compile(r"^\s*(`{3,}|~{3,})")
FENCE_CLOSE = re.compile(r"^\s*(`{3,}|~{3,})\s*$")
# A maximal run of N backticks, then the shortest span to the next maximal run of exactly N.
INLINE_SPAN = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
SUMMARY_KEY = re.compile(r"^summary:(.*)$")


def strip_code(text):
    """Remove fenced blocks and inline code spans; everything else is returned line-for-line."""
    out = []
    fence = None  # (char, length) of the open fence
    for line in text.split("\n"):
        if fence is None:
            m = FENCE_OPEN.match(line)
            if m:
                fence = (m.group(1)[0], len(m.group(1)))
                continue
            out.append(INLINE_SPAN.sub("", line))
        else:
            m = FENCE_CLOSE.match(line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= fence[1]:
                fence = None
            # inside a fence: dropped
    return "\n".join(out)


def page_links(text):
    return WIKILINK.findall(strip_code(text))


def frontmatter_lines(text):
    """The lines between the leading `---` and the next `---`/`...` line, or [] when absent."""
    if text.startswith("\ufeff"):
        text = text[1:]
    lines = text.split("\n")
    if not lines or lines[0].rstrip("\r") != "---":
        return []
    body = []
    for line in lines[1:]:
        if line.rstrip("\r") in ("---", "..."):
            return body
        body.append(line.rstrip("\r"))
    return []  # no closing delimiter: not a frontmatter block


def unquote_double(raw):
    out = []
    i = 1
    while i < len(raw):
        c = raw[i]
        if c == '"':
            break
        if c == "\\" and i + 1 < len(raw):
            out.append(raw[i + 1])
            i += 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def unquote_single(raw):
    out = []
    i = 1
    while i < len(raw):
        c = raw[i]
        if c == "'":
            if i + 1 < len(raw) and raw[i + 1] == "'":
                out.append("'")
                i += 2
                continue
            break
        out.append(c)
        i += 1
    return "".join(out)


def summary_value(fm_lines):
    """The first top-level `summary:` line's scalar, unquoted per its form ('' when absent)."""
    for idx, line in enumerate(fm_lines):
        m = SUMMARY_KEY.match(line)
        if not m:
            continue
        raw = m.group(1).strip()
        if raw.startswith('"'):
            return unquote_double(raw)
        if raw.startswith("'"):
            return unquote_single(raw)
        if raw[:1] in (">", "|"):
            parts = []
            for cont in fm_lines[idx + 1:]:
                if cont.strip() == "":
                    continue
                if not cont[:1].isspace():
                    break
                parts.append(cont.strip())
            return " ".join(parts)
        # plain scalar: a trailing ` #comment` is not part of the value
        return re.sub(r"\s+#.*$", "", raw).strip()
    return ""


def summary_length(text):
    return len(summary_value(frontmatter_lines(text)))


def load_pages(spec):
    try:
        if spec == "-":
            data = json.load(sys.stdin)
        else:
            with open(spec, "r", encoding="utf-8") as fh:
                data = json.load(fh)
    except Exception as exc:  # unreadable or unparseable input
        raise SystemExit("lint-page-facts: cannot read --pages %s: %s" % (spec, exc))
    if not isinstance(data, list):
        raise SystemExit("lint-page-facts: --pages must be a JSON array of {slug, path}")
    pages = []
    for entry in data:
        if not isinstance(entry, dict) or not isinstance(entry.get("slug"), str) or not isinstance(entry.get("path"), str):
            raise SystemExit("lint-page-facts: every --pages entry must be an object with string slug and path")
        pages.append((entry["slug"], entry["path"]))
    return pages


def main(argv):
    ap = argparse.ArgumentParser(description="derive each page's raw [[ ]] set and parsed summary: length from its bytes")
    ap.add_argument("--pages", required=True, help="path to a JSON array of {slug, path}, or - for stdin")
    ap.add_argument("--out", default="-", help="where to write the JSON result (default: stdout)")
    args = ap.parse_args(argv)

    try:
        pages = load_pages(args.pages)
    except SystemExit as exc:
        sys.stderr.write(str(exc) + "\n")
        return 2

    links, lengths, unreadable = {}, {}, []
    for slug, path in pages:
        try:
            with open(path, "rb") as fh:
                text = fh.read().decode("utf-8")
        except Exception:
            unreadable.append(slug)
            continue
        links[slug] = page_links(text)
        lengths[slug] = summary_length(text)

    result = {"pageLinks": links, "summaryLengths": lengths, "unreadable": unreadable, "pages": len(pages)}
    payload = json.dumps(result, ensure_ascii=False, indent=1) + "\n"
    try:
        if args.out == "-":
            sys.stdout.write(payload)
        else:
            with open(args.out, "w", encoding="utf-8") as fh:
                fh.write(payload)
    except Exception as exc:
        sys.stderr.write("lint-page-facts: cannot write --out %s: %s\n" % (args.out, exc))
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
