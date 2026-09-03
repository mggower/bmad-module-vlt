#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Walk the `para_*` population from disk and emit per-file FACTS, never verdicts — the
population instrument every per-file slot of the lint report is checked against.
Cycle 15 build-5 (A15-7 / A15-8; E1 as made buildable at the roundtable, A16 (3); D2 (iv));
build-7 added the write-posture facts and `--writer-line` (A15-13; A8; D2 (iv) extended).

Why this exists: the report's five `para_*` slots are mandated PER-FILE (`references/report.md`,
`[<para-file: ...>` lists) and were rendered by hand from a population the SKILL walked in
prose — so one string could stand in for 27 files and nothing could tell. The persist gate
(`lint-report-check.py`) needs a population that did NOT transit the agent: it imports `walk`
from this file and walks the directories itself. The count the report carries as `para_scan:`
comes from the same walk (`--line`), so the denominator is produced by an instrument
independent of the value's producer (the operating contract's instrument rule).

THE POPULATION (P) — the executable form of `references/checks.md`'s population statement
("The `para_*` population, and the closing nets"): every `*.md` file under each `--dir`
(the SKILL resolves `{projects}`, `{areas}`, `{resources}` from the `vault_structure` map),
recursively, with every `--exclude` subtree carved out BY NAME (`{wiki}` — its pages are the
wiki page population, never `para_*` candidates; `references/full-scale.md` step 1). A file
with no frontmatter block is a member (`has_frontmatter: false`) — it is in the population and
is what the field's "no-frontmatter files" rollups were about.

THE PREDICATE (M) — `references/checks.md` Attestation findings, `para_missing_attestation`,
implemented here ONCE: `type` present, `author` in {agent, hybrid}, not attested, and not of
the operational-record class — the carve-out's both halves as stated there: basename in
{charter.md, record.md, register.md} OR `type` in {charter, record, register}. "Attested" is
the pair `{conventions}/write-verification.md` Attestation defines — `verified_by` AND
`verified_at` both present and non-empty.

FACTS, NEVER VERDICTS: per file `has_frontmatter`, `type`, `author`, `status`, `created`,
`attested`, `basename` — raw scalars (or null when the key is absent) — plus two write-posture
facts (build-7): `writers` — the file's own `writers:` list where it carries one (a charter's;
flow `[a, b]` or block `- a` form, read by the sibling line reader, never a YAML library), else
null — and `declaring_ancestor` — the walk-relative path of the nearest `charter.md` at or above
the file (up to the `--dir` it was found under) whose `writers:` list is non-empty, else null
(`references/checks.md`, `para_writer_unauthorized`: the nearest declaring ancestor binds every
sub-container; a charter that declares is its own). `counts.D` is how many members have one.
Which `type:` values are recognized, which `status:` enum applies, whether an `author:` is
legal, and whether a writer is ADMITTED by that list — none of that is decided here (their
single homes are `{conventions}/extraction.md`, the overlays, and `checks.md`'s join, which the
SKILL judges); the walker says who declares over which files, never who passes.

Frontmatter is read the way `lint-page-facts.py` reads it — the leading `---` block, line-
parsed, no YAML library (this script must run under bare `python3`; `lint-report-check.py`'s
`.json` route depends on it) — by importing that script's `frontmatter_lines` and unquoters
by sibling path, never a copy.

Input   --dir <path>       (repeat) a population directory; --exclude <path> (repeat) a
                           subtree to carve out; --root <path> the project root the emitted
                           paths are relative to (default: cwd).
Output  --out <path|->     one JSON object: {instrument, population: [relpath, ...],
                           files: {relpath: {facts}}, missing_attestation: [relpath, ...],
                           counts: {P, M, D}}  (default stdout)
        --line             print ONLY the `para_scan:` value — the exact string the SKILL
                           pastes at Step 5 and the gate re-derives and compares at Step 6.
        --writer-line      print ONLY the `para_writer_scan:` value — `<P> judged; <D> under a
                           declaring ancestor; <P−D> passed on open posture (instrument: …)` —
                           pasted and compared the same way (`report.md`, Write-posture reporting).

Exit 0 when the walk ran; 2 for a missing/unreadable `--dir`; 3 for an unwritable `--out`.
No `--self-test`: the factory harness is the test, a vault runs none.
"""

import argparse
import importlib.util
import json
import os
import posixpath
import re
import sys

sys.dont_write_bytecode = True  # sibling imports must leave no __pycache__ in the shipped tree

INSTRUMENT = "scripts/lint-para-facts.py"
OPERATIONAL_BASENAMES = {"charter.md", "record.md", "register.md"}
OPERATIONAL_TYPES = {"charter", "record", "register"}
SELF_AUTHORS = {"agent", "hybrid"}
FACT_KEYS = ("type", "author", "status", "created", "verified_by", "verified_at")
KEY_LINE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(.*)$")
LIST_ITEM = re.compile(r"^\s*-\s*(.*)$")
WRITERS_KEY = "writers"
CHARTER = "charter.md"


def _page_facts():
    """`lint-page-facts.py` by sibling path — the frontmatter reader's single home."""
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("lint_page_facts", os.path.join(here, "lint-page-facts.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_pf = _page_facts()
frontmatter_lines = _pf.frontmatter_lines
unquote_double = _pf.unquote_double
unquote_single = _pf.unquote_single


def scalar(raw):
    """A top-level frontmatter value, unquoted per its form; '' when empty."""
    raw = raw.strip()
    if raw.startswith('"'):
        return unquote_double(raw)
    if raw.startswith("'"):
        return unquote_single(raw)
    return re.sub(r"\s+#.*$", "", raw).strip()


def list_value(raw, following):
    """A top-level YAML list read by line (`frontmatter.md` YAML rules 3/4): flow `[a, b]` on the
    key's own line, or block `- a` lines directly beneath an empty value. Never a YAML library."""
    raw = raw.strip()
    if raw.startswith("["):
        inner = raw[1:raw.rindex("]")] if "]" in raw else raw[1:]
        return [scalar(x) for x in inner.split(",") if scalar(x)]
    if raw and not raw.startswith("#"):
        return [scalar(raw)]  # a bare scalar where a list belongs — one entry, read as written
    items = []
    for line in following:
        m = LIST_ITEM.match(line)
        if not m or not line.strip():
            break
        if scalar(m.group(1)):
            items.append(scalar(m.group(1)))
    return items


def file_facts(text, basename):
    fm = frontmatter_lines(text)
    values = {}
    writers = None
    for i, line in enumerate(fm):
        if line[:1].isspace():
            continue  # nested keys are not top-level facts
        m = KEY_LINE.match(line)
        if not m:
            continue
        if m.group(1) in FACT_KEYS and m.group(1) not in values:
            values[m.group(1)] = scalar(m.group(2))
        elif m.group(1) == WRITERS_KEY and writers is None:
            writers = list_value(m.group(2), fm[i + 1:])
    attested = bool(values.get("verified_by")) and bool(values.get("verified_at"))
    return {
        "has_frontmatter": bool(fm),
        "type": values.get("type") or None,
        "author": values.get("author") or None,
        "status": values.get("status") or None,
        "created": values.get("created") or None,
        "attested": attested,
        "basename": basename,
        "writers": writers,
        "declaring_ancestor": None,  # filled by walk(), which knows the tree
    }


def missing_attestation(facts):
    """The `para_missing_attestation` predicate (`checks.md` Attestation findings)."""
    if not facts["type"] or facts["author"] not in SELF_AUTHORS or facts["attested"]:
        return False
    if facts["basename"] in OPERATIONAL_BASENAMES or facts["type"] in OPERATIONAL_TYPES:
        return False
    return True


def _under(path, roots):
    return any(path == r or path.startswith(r + os.sep) for r in roots)


def _join(*parts):
    return posixpath.normpath(posixpath.join(*parts))


def declaring_ancestor(rel, top, files):
    """The walk-relative path of the nearest `charter.md` at or above `rel` (stopping at `top`,
    the `--dir` the file was found under) whose `writers:` list is non-empty; None where no
    directory on that path declares (`checks.md`, `para_writer_unauthorized`: `open`)."""
    cur = posixpath.dirname(rel) or "."
    while True:
        charter = _join(cur, CHARTER)
        facts = files.get(charter)
        if facts and facts["writers"]:
            return charter
        if cur == top or cur in (".", "", "/"):
            return None
        cur = posixpath.dirname(cur) or "."


def walk(dirs, excludes, root):
    """P, per-file facts and M for the given directories. Raises FileNotFoundError for a
    missing --dir (a mistyped directory must never read as an empty population)."""
    root = os.path.realpath(root)
    ex = [os.path.realpath(e) for e in excludes]
    files = {}
    tops = {}
    for d in dirs:
        d = os.path.realpath(d)
        if not os.path.isdir(d):
            raise FileNotFoundError(d)
        top = os.path.relpath(d, root).replace(os.sep, "/")
        for cur, subdirs, names in os.walk(d):
            subdirs[:] = sorted(s for s in subdirs if not _under(os.path.join(cur, s), ex))
            if _under(cur, ex):
                continue
            for name in sorted(names):
                if not name.endswith(".md"):
                    continue
                full = os.path.join(cur, name)
                rel = os.path.relpath(full, root).replace(os.sep, "/")
                if rel in files:
                    continue
                try:
                    with open(full, "rb") as fh:
                        text = fh.read().decode("utf-8")
                except Exception:
                    text = ""  # unreadable: a member with no readable frontmatter
                files[rel] = file_facts(text, name)
                tops[rel] = top
    population = sorted(files)
    for p in population:
        files[p]["declaring_ancestor"] = declaring_ancestor(p, tops[p], files)
    missing = [p for p in population if missing_attestation(files[p])]
    declared = [p for p in population if files[p]["declaring_ancestor"]]
    return {
        "instrument": INSTRUMENT,
        "population": population,
        "files": {p: files[p] for p in population},
        "missing_attestation": missing,
        "counts": {"P": len(population), "M": len(missing), "D": len(declared)},
    }


def scan_line(result):
    """The `para_scan:` value — `references/report.md`'s placeholder, filled."""
    return (
        "%d files walked under {projects}/{areas}/{resources}, {wiki} subtree carved out "
        "(instrument: %s); %d carry author agent|hybrid with no attestation outside the "
        "operational-record class" % (result["counts"]["P"], INSTRUMENT, result["counts"]["M"])
    )


def writer_line(result):
    """The `para_writer_scan:` value — `references/report.md`'s placeholder, filled. N is the
    walk's P (every member is judged; one resolving no identity is left to the honesty nets),
    D the members under a declaring ancestor, O = N − D the open-posture passes (D5.5)."""
    p, d = result["counts"]["P"], result["counts"]["D"]
    return "%d judged; %d under a declaring ancestor; %d passed on open posture (instrument: %s)" % (p, d, p - d, INSTRUMENT)


def main(argv):
    ap = argparse.ArgumentParser(description="walk the para_* population and emit per-file facts")
    ap.add_argument("--dir", action="append", required=True, help="a population directory (repeat)")
    ap.add_argument("--exclude", action="append", default=[], help="a subtree to carve out (repeat)")
    ap.add_argument("--root", default=".", help="project root the emitted paths are relative to")
    ap.add_argument("--out", default="-", help="where to write the JSON result (default: stdout)")
    ap.add_argument("--line", action="store_true", help="print only the para_scan: value")
    ap.add_argument("--writer-line", action="store_true", help="print only the para_writer_scan: value")
    args = ap.parse_args(argv)

    try:
        result = walk(args.dir, args.exclude, args.root)
    except FileNotFoundError as exc:
        sys.stderr.write("lint-para-facts: --dir is not a directory: %s\n" % exc)
        return 2

    if args.line:
        payload = scan_line(result) + "\n"
    elif args.writer_line:
        payload = writer_line(result) + "\n"
    else:
        payload = json.dumps(result, ensure_ascii=False, indent=1) + "\n"
    try:
        if args.out == "-":
            sys.stdout.write(payload)
        else:
            with open(args.out, "w", encoding="utf-8") as fh:
                fh.write(payload)
    except Exception as exc:
        sys.stderr.write("lint-para-facts: cannot write --out %s: %s\n" % (args.out, exc))
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
