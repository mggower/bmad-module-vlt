#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Derive the per-page BYTE FACTS the vlt-lint fan-out's link graph, summary-length and bare-path
clauses run on: every `[[ ]]` inner text on each page (raw), each page's parsed `summary:` length in
characters, and each page's count of frontmatter `sources:` entries in the bare-path form — plus, as
a second entry point, the wiki-wide BARE-PATH CENSUS the full-mode report renders. Cycle 15 build-4
(A15-1 / A15-3 / A15-4 fidelity half / A15-5; D-C, D-A); Cycle 16 build-1 (A16-2, Q3 (a), A9).

Why this exists: the fan-out's reduce (`vlt-lint-full.js`) has no filesystem access and used to
build its inbound map and its missing-target list from whatever link list the page SCANNERS
returned — a link the scanner dropped did not exist (three consecutive false orphans),
a stripped `#` turned a same-page anchor into a missing page, a substituted proper noun reached
`missing_targets` and the findings cache made it permanent, and the scanner's own summary-length
verdict counted the raw YAML line. The link set and the length now come from the side of the
boundary that can read bytes: the SKILL runs THIS script and passes its two maps across as
`pageLinks` / `summaryLengths` (the `crossLayerSlugs` / `pageHashes` precedent); the scanner is
no longer asked for links at all.

FACTS, NEVER VERDICTS. This script emits raw inner texts, an integer length and an integer count.
The normal form (`normalizeTarget`, B5-3) and the 160-character verdict stay in the workflow, where
they already live — a verdict here would put the limit in a second home. The bare-path count is a
FORM the bytes carry; its legality under frontmatter.md rule 4 is indexed on WRITE DATE, which no
byte carries — which is why the count is a census and never a per-page verdict (Cycle 16 Q3 (a)).

Two entry points, mutually exclusive:

Input   --pages <path|->   a JSON array `[{slug, path}]` — the same list the SKILL builds at
                           `references/full-scale.md` step 1. The maps are keyed by the
                           SKILL-SUPPLIED slug, never one this script derives (the cacheRecords
                           principle: keying on anything else lets a derivation drift from the
                           population).
Output  --out <path>       (default stdout) one JSON object:
          {"pageLinks": {slug: [inner, ...]}, "summaryLengths": {slug: int},
           "bareSources": {slug: int}, "sourcesUnparsed": [slug, ...],
           "unreadable": [slug, ...], "pages": N}
        At scale the SKILL writes it to the scratch directory and the wrapper-writing step
        (full-scale.md step 3) embeds the three maps — the payload never transits the caller.

Input   --census <wiki-dir> [--census-exclude <path> ...]   walk every `*.md` under the directory
                           recursively (sorted; excluded files/subtrees pruned; an unreadable file
                           is counted in M and carries no entries — the lint-para-facts.py walk
                           idiom). The SKILL passes `{index}` as the exclusion.
Output  --out <path>       one JSON object {"bareSources": {page: int}, "sourcesUnparsed": [page, ...],
                           "counts": {"N": entries, "P": pages carrying >= 1, "M": pages walked}},
                           keyed by the wiki-relative path with `.md` stripped; with --census-line,
                           ONLY the report line below, for `bare_path_sources:` (report.md).
        Two callers, one function: the SKILL's full-scale.md step 1 run (the --pages map for the
        reduce, the --census-line for Step 5) and the persist gate's recount (lint-report-check.py
        imports `census`/`census_line` by sibling path and compares the rendered line by string
        equality). The line: `N entries across P of M pages — sources: scalars unquoted and ending
        .md (instrument: scripts/lint-page-facts.py --census)`.

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

bareSources — THE BARE-PATH FORM, STATED ONCE (Cycle 16 build-1 disposition 6). A `sources:` ENTRY
is an item of the frontmatter `sources:` key's YAML sequence — block form (`- <value>` lines
following the key) or flow form (`[a, b]` on the key line). An entry is in BARE-PATH FORM iff its
value, after a trailing ` #comment` is stripped, does not begin with `"` or `'`, does not begin
with `[[`, and ends with `.md`. Everything else — quoted wikilinks, URLs, quoted paths, entries
without `.md` — is not counted. Only the `sources:` key counts: `grounding:`,
`personalization_sources:`, `artifacts:` and any prose `## Sources` section are never read. The
frame is the same frontmatter block `frontmatter_lines` delimits. A page whose `sources:` is NOT a
parseable list — the key absent, a scalar value, a block-scalar indicator, an empty key, no closing
frontmatter delimiter — has NO entry in the map and is listed under `sourcesUnparsed` instead: the
census counts only what it could parse, so a complaint about such a page can never be refused as
"the census has it" (the reduce's disposition 3 keys on a present integer). `sources: []` -> 0.

unreadable — a page whose bytes cannot be read or decoded is listed by slug and absent from every
map; the workflow renders the gap as a denominated coverage cap.

Exit 0 whenever the input parsed; non-zero only for an unreadable `--pages` input or a missing
`--census` directory (2) or an unwritable `--out` (3). No `--self-test`: the factory harness is the test, a vault runs none.
"""

import argparse
import json
import os
import re
import sys

WIKILINK = re.compile(r"\[\[([^\[\]]+?)\]\]")
FENCE_OPEN = re.compile(r"^\s*(`{3,}|~{3,})")
FENCE_CLOSE = re.compile(r"^\s*(`{3,}|~{3,})\s*$")
# A maximal run of N backticks, then the shortest span to the next maximal run of exactly N.
INLINE_SPAN = re.compile(r"(?<!`)(`+)(?!`)(.+?)(?<!`)\1(?!`)")
SUMMARY_KEY = re.compile(r"^summary:(.*)$")
SOURCES_KEY = re.compile(r"^sources:(.*)$")
INSTRUMENT = "scripts/lint-page-facts.py --census"


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


def strip_plain_comment(raw):
    """A plain scalar's trailing ` #comment` is not part of the value (the summary_value rule)."""
    return re.sub(r"\s+#.*$", "", raw).strip()


def is_bare_path(value):
    """The bare-path form, per the docstring: unquoted, not a wikilink, ending `.md`."""
    v = strip_plain_comment(value)
    if not v or v[0] in ('"', "'") or v.startswith("[["):
        return False
    return v.endswith(".md")


def split_flow(inner):
    """Split a flow sequence's inner text on top-level commas (quotes and [[ ]] respected)."""
    items, buf, quote, depth = [], [], None, 0
    for ch in inner:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ('"', "'"):
            quote = ch
        elif ch == "[":
            depth += 1
        elif ch == "]":
            depth = max(0, depth - 1)
        elif ch == "," and depth == 0:
            items.append("".join(buf).strip())
            buf = []
            continue
        buf.append(ch)
    tail = "".join(buf).strip()
    if tail or items:
        items.append(tail)
    return [i for i in items if i != ""]


def bare_sources(text):
    """(count, unparsed) over the frontmatter `sources:` list — the ONE function both callers use.
    count is the number of entries in bare-path form; (None, True) when `sources:` is not a
    parseable list (absent, scalar, block-scalar indicator, empty key, no frontmatter block)."""
    fm = frontmatter_lines(text)
    if not fm:
        return None, True
    for idx, line in enumerate(fm):
        m = SOURCES_KEY.match(line)
        if not m:
            continue
        raw = m.group(1).strip()
        if raw.startswith("["):
            body = strip_plain_comment(raw)
            if not body.endswith("]"):
                return None, True  # a flow sequence that never closes on its line
            return sum(1 for item in split_flow(body[1:-1]) if is_bare_path(item)), False
        if raw == "" or raw.startswith("#"):
            count, items = 0, 0
            for cont in fm[idx + 1:]:
                if cont.strip() == "":
                    continue
                if not cont[:1].isspace():
                    break
                s = cont.strip()
                if s == "-":
                    items += 1  # an empty item
                elif s.startswith("- "):
                    items += 1
                    count += 1 if is_bare_path(s[2:]) else 0
                else:
                    return None, True  # an indented non-item line: not a plain sequence
            return (count, False) if items else (None, True)  # `sources:` alone is YAML null
        return None, True  # a scalar or a block-scalar indicator: not a list
    return None, True  # no sources: key


def _under(path, excludes):
    for ex in excludes:
        if path == ex or path.startswith(ex + os.sep):
            return True
    return False


def census(wiki_dir, excludes=()):
    """The wiki-wide bare-path census: walk `*.md` under wiki_dir recursively (sorted, excluded
    paths pruned, unreadable files counted in M with no entries) and count with bare_sources().
    Raises FileNotFoundError for a missing directory (a mistyped dir must never read as zero)."""
    top = os.path.realpath(wiki_dir)
    if not os.path.isdir(top):
        raise FileNotFoundError(top)
    ex = [os.path.realpath(e) for e in excludes]
    bare, unparsed, walked = {}, [], 0
    for cur, subdirs, names in os.walk(top):
        subdirs[:] = sorted(s for s in subdirs if not _under(os.path.join(cur, s), ex))
        for name in sorted(names):
            if not name.endswith(".md"):
                continue
            full = os.path.join(cur, name)
            if _under(full, ex):
                continue
            walked += 1
            key = os.path.relpath(full, top).replace(os.sep, "/")[:-3]
            try:
                with open(full, "rb") as fh:
                    text = fh.read().decode("utf-8")
            except Exception:
                continue  # unreadable: in M, no entries, no map entry
            count, un = bare_sources(text)
            if un:
                unparsed.append(key)
            else:
                bare[key] = count
    n = sum(bare.values())
    p = sum(1 for v in bare.values() if v > 0)
    return {"bareSources": bare, "sourcesUnparsed": unparsed, "counts": {"N": n, "P": p, "M": walked}}


def census_line(result):
    """The `bare_path_sources:` value — `references/report.md`'s placeholder, filled."""
    c = result["counts"]
    return "%d entries across %d of %d pages — sources: scalars unquoted and ending .md (instrument: %s)" % (
        c["N"], c["P"], c["M"], INSTRUMENT)


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


def write_out(payload, out):
    try:
        if out == "-":
            sys.stdout.write(payload)
        else:
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(payload)
    except Exception as exc:
        sys.stderr.write("lint-page-facts: cannot write --out %s: %s\n" % (out, exc))
        return 3
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description="derive each page's raw [[ ]] set, parsed summary: length and bare-path sources: count from its bytes; or the wiki-wide bare-path census")
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--pages", help="path to a JSON array of {slug, path}, or - for stdin")
    mode.add_argument("--census", metavar="WIKI_DIR", help="walk *.md under this directory and count bare-path sources: entries")
    ap.add_argument("--census-exclude", action="append", default=[], metavar="PATH", help="a file or subtree the census walk skips (repeatable; the SKILL passes {index})")
    ap.add_argument("--census-line", action="store_true", help="with --census: print only the report's bare_path_sources: line")
    ap.add_argument("--out", default="-", help="where to write the result (default: stdout)")
    args = ap.parse_args(argv)

    if args.census:
        try:
            result = census(args.census, args.census_exclude)
        except FileNotFoundError as exc:
            sys.stderr.write("lint-page-facts: --census is not a directory: %s\n" % exc)
            return 2
        payload = census_line(result) + "\n" if args.census_line else json.dumps(result, ensure_ascii=False, indent=1) + "\n"
        return write_out(payload, args.out)

    try:
        pages = load_pages(args.pages)
    except SystemExit as exc:
        sys.stderr.write(str(exc) + "\n")
        return 2

    links, lengths, bare, unparsed, unreadable = {}, {}, {}, [], []
    for slug, path in pages:
        try:
            with open(path, "rb") as fh:
                text = fh.read().decode("utf-8")
        except Exception:
            unreadable.append(slug)
            continue
        links[slug] = page_links(text)
        lengths[slug] = summary_length(text)
        count, un = bare_sources(text)
        if un:
            unparsed.append(slug)
        else:
            bare[slug] = count

    result = {"pageLinks": links, "summaryLengths": lengths, "bareSources": bare, "sourcesUnparsed": unparsed,
              "unreadable": unreadable, "pages": len(pages)}
    payload = json.dumps(result, ensure_ascii=False, indent=1) + "\n"
    return write_out(payload, args.out)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
