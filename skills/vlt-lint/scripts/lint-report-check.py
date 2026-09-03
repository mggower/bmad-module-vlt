#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""The persist gate: read a rendered lint report back under a strict parser and check it against
the shape `references/report.md` states — before any file lands under `{lint_reports}`.
Cycle 15 build-5 (A15-7 the parse requirement, A15-8 the shape requirement; E1 as ruled and as
made buildable at the roundtable, A16 (1)-(5); D2 (iv)). `ST-7`'s output-side instance.

THIS SCRIPT WRITES NOTHING. Cycle 14 build-4 §3 ruled that the report persist gets no
serializer — the block is the agent's, content-verbatim — and that ruling is honoured, not
superseded: this is the READER that ruling said the enforcement point would be. It reads one
file, prints one JSON verdict on stdout, and exits 0 (`status: ok`), 1 (`status: failed`, with
`reason`) or 2 (`status: schema_unreadable`). `vlt-lint` Step 6 runs it over a scratch copy and
`mv`s the validated bytes into place on `ok` — the ritual's single home is `SKILL.md` Step 6.

THE SHAPE SOURCE IS THE FENCE, NEVER A SECOND LIST (A16 (1)). The mandated key set, each key's
type, the per-file marking and the full-mode-only marking are DERIVED by parsing the ```yaml
fence in `references/report.md` under the line grammar that file states directly above it —
structure by indentation, type by the value's first non-space character (`[` list, `{` map,
else scalar), per-file by the `[<para-file:` opener, mode conditionality by the `# full mode
only` comment marker, comments otherwise ignored. No key list, type table or per-file roster
lives here. The one number this script hard-codes is SCHEMA_FLOOR — a floor on the top-level
key count that catches a truncated fence, not a key list (the `CASE_FLOOR` precedent).

WHAT `check` VERIFIES (A16 (2), (3)) — presence + type, NEVER closure:
  - parse:       `yaml.safe_load` over the whole file as ONE document (`.yaml`), or
                 `json.loads` (`.json`); a multi-document stream or a non-mapping top level is
                 a parse failure. `yaml` is imported LAZILY, only for a `.yaml` report — the
                 `.json` home validates under bare `python3` with nothing installed.
  - presence:    every key the grammar yields is present and not null (`key:` with nothing
                 after it is a bare key, not a rendered slot). A `# full mode only` key may be
                 absent under `--mode scoped`.
  - type:        list <- a sequence; map <- a mapping; scalar <- str/int/float/bool (or a
                 date the YAML parser produced from an unquoted date). Inline-map children are
                 not parsed and not validated.
  - extra keys:  reported (`extra_keys`), never failed on.
  - membership:  every entry of a `[<para-file:` slot opens with a path token — the text before
                 the first `: ` or ` — `, whichever comes first — that names ONE member of the
                 population `lint-para-facts.py` walks (imported by sibling path and run HERE
                 over `--dir`/`--exclude`; no population is accepted from the caller), and no
                 file is named twice. A rollup ("27 PARA files carry ..."), a "same N files as
                 ... above", or a prose sentence where `[]` belongs all fail here.
  - count:       full mode, `para_missing_attestation` only — the rendered entry count equals
                 the walk's M (the walker's mechanical predicate). The other four per-file
                 slots are membership-only; their count instruments are declared blocked at
                 the brief (each rule's single home is prose or moves this release).
  - para_scan:   the report's `para_scan:` scalar equals, by string equality, the line the
                 walker prints for the same directories — a read-back with no regex over prose.

REASON VOCABULARY (fixed; one clause per defect, joined `; `):
  `parse: <parser message>` | `key missing: <path>` | `wrong type: <path> (got X, expected Y)`
  | `not a member: <slot> <- <entry head>` | `duplicate: <slot> <- <path>`
  | `count: <slot> rendered N, walk finds M` | `para_scan: rendered line does not match the walk`

`--kind failed` checks a `...-lint-failed.yaml` record instead: parse, plus presence of
`status`, `reason`, `next` and `unvalidated_report` — so the failure artifact can never be a
second unreadable file.

`schema` prints the parsed fence as JSON (the at-rest oracle `build-5-expected-schema.json` is
compared against it; a build that edits the fence re-derives the oracle).

Usage
  lint-report-check.py check --report <path> --mode full|scoped --dir <p> [--dir ...]
                             [--exclude <p> ...] [--root <project-root>] [--schema <report.md>]
                             [--kind report|failed] [--format yaml|json]
  lint-report-check.py schema [--schema <report.md>]
"""

import argparse
import datetime
import importlib.util
import json
import os
import re
import sys

sys.dont_write_bytecode = True  # sibling imports must leave no __pycache__ in the shipped tree

SCHEMA_FLOOR = 18  # top-level keys the fence carried at Cycle 15 build-5's commit — a floor, not a list
DEFAULT_SCHEMA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "report.md")
KEY_LINE = re.compile(r"^(\s*)([a-z_]+):(.*)$")
FENCE_OPEN = re.compile(r"^```yaml\s*$")
FENCE_CLOSE = re.compile(r"^```\s*$")
PER_FILE_OPENER = "[<para-file:"
FULL_MODE_MARKER = "full mode only"
COUNT_SLOTS = {"para_missing_attestation": "missing_attestation"}  # slot -> walker list (disposition 3)
SCAN_KEY = "para_scan"
SCALAR_TYPES = (str, int, float, bool, datetime.date, datetime.datetime)


class SchemaUnreadable(Exception):
    pass


# ---------------------------------------------------------------- the fence, under its grammar

def split_comment(value):
    """(value, comment) — a `#` outside a `<...>` placeholder opens the comment."""
    depth = 0
    for i, ch in enumerate(value):
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth = max(0, depth - 1)
        elif ch == "#" and depth == 0:
            return value[:i].strip(), value[i + 1:].strip()
    return value.strip(), ""


def fence_lines(text):
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if FENCE_OPEN.match(l)), None)
    if start is None:
        raise SchemaUnreadable("no ```yaml fence found")
    end = next((i for i in range(start + 1, len(lines)) if FENCE_CLOSE.match(lines[i])), None)
    if end is None:
        raise SchemaUnreadable("the ```yaml fence never closes")
    return lines[start + 1:end]


def parse_fence(text):
    """The fence -> {path: {type, per_file, full_mode_only}} in fence order, plus the top-level count."""
    raw = fence_lines(text)
    rows = []  # (indent, key, value, comment, lineno)
    for n, line in enumerate(raw, 1):
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = KEY_LINE.match(line)
        if not m:
            raise SchemaUnreadable("fence line %d matches no grammar rule: %r" % (n, line))
        value, comment = split_comment(m.group(3))
        rows.append((len(m.group(1)), m.group(2), value, comment, n))

    keys = {}
    stack = []  # (indent, path) of open maps
    inline_parent = None  # (indent) of an inline-map / list / scalar line: deeper lines are illegal
    for idx, (indent, key, value, comment, n) in enumerate(rows):
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if inline_parent is not None and indent > inline_parent:
            raise SchemaUnreadable("fence line %d is nested under a non-map key" % n)
        inline_parent = None
        path = ".".join([p for _, p in stack] + [key])
        next_indent = rows[idx + 1][0] if idx + 1 < len(rows) else None
        if value == "":
            if next_indent is None or next_indent <= indent:
                raise SchemaUnreadable("fence line %d: empty value with no deeper line (%s)" % (n, key))
            kind, per_file = "map", False
            stack.append((indent, key))
        else:
            first = value[0]
            kind = "list" if first == "[" else "map" if first == "{" else "scalar"
            per_file = kind == "list" and value.startswith(PER_FILE_OPENER)
            inline_parent = indent
        keys[path] = {
            "type": kind,
            "per_file": per_file,
            "full_mode_only": comment.startswith(FULL_MODE_MARKER),
        }
    top = sum(1 for p in keys if "." not in p)
    if top < SCHEMA_FLOOR:
        raise SchemaUnreadable("fence carries %d top-level keys, below the floor of %d" % (top, SCHEMA_FLOOR))
    return {"top_level": top, "keys": keys}


def load_schema(path):
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return parse_fence(fh.read())
    except OSError as exc:
        raise SchemaUnreadable("cannot read %s: %s" % (path, exc))


# ---------------------------------------------------------------- the report, strictly

def load_report(path, fmt):
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if fmt == "json":
        data = json.loads(text)
    else:
        import yaml  # lazy: the .json home never needs it
        data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ValueError("top level is not a mapping")
    return data


def type_name(value):
    if value is None:
        return "null"
    if isinstance(value, list):
        return "list"
    if isinstance(value, dict):
        return "map"
    if isinstance(value, SCALAR_TYPES):
        return "scalar"
    return type(value).__name__


def lookup(data, path):
    """(present, value) for a dotted path; present is False when any parent is missing/not a map."""
    cur = data
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return False, None
        cur = cur[part]
    return True, cur


def entry_head(entry):
    text = entry if isinstance(entry, str) else json.dumps(entry, ensure_ascii=False)
    cut = len(text)
    for sep in (": ", " — "):
        i = text.find(sep)
        if i != -1 and i < cut:
            cut = i
    return text[:cut].strip().strip("`").strip()


def short(text, n=80):
    return text if len(text) <= n else text[: n - 1] + "…"


def check_report(data, schema, mode, walk_result):
    reasons = []
    extra = []
    keys = schema["keys"]

    # presence + type, parents first — a missing/wrong-typed parent is reported once
    skipped_parents = set()
    for path, meta in keys.items():
        parent = path.rsplit(".", 1)[0] if "." in path else None
        if parent in skipped_parents:
            skipped_parents.add(path)
            continue
        present, value = lookup(data, path)
        if not present or value is None:
            if meta["full_mode_only"] and mode == "scoped":
                skipped_parents.add(path)
                continue
            reasons.append("key missing: %s" % path)
            skipped_parents.add(path)
            continue
        got = type_name(value)
        if got != meta["type"]:
            reasons.append("wrong type: %s (got %s, expected %s)" % (path, got, meta["type"]))
            skipped_parents.add(path)

    # extra keys at every parsed depth
    parsed_maps = [""] + [p for p, m in keys.items() if m["type"] == "map" and any(k.startswith(p + ".") for k in keys)]
    for prefix in parsed_maps:
        present, node = (True, data) if prefix == "" else lookup(data, prefix)
        if not present or not isinstance(node, dict):
            continue
        for k in node:
            full = k if prefix == "" else prefix + "." + k
            if full not in keys:
                extra.append(full)

    # per-file slots: membership, duplicates, count
    population = set(walk_result["population"])
    for path, meta in keys.items():
        if not meta["per_file"]:
            continue
        present, entries = lookup(data, path)
        if not present or not isinstance(entries, list):
            continue
        slot = path.rsplit(".", 1)[-1]
        seen = set()
        for entry in entries:
            head = entry_head(entry)
            if head not in population:
                reasons.append("not a member: %s ← %s" % (slot, short(head)))
                continue
            if head in seen:
                reasons.append("duplicate: %s ← %s" % (slot, head))
            seen.add(head)
        if mode == "full" and slot in COUNT_SLOTS:
            expected = len(walk_result[COUNT_SLOTS[slot]])
            if len(entries) != expected:
                reasons.append("count: %s rendered %d, walk finds %d" % (slot, len(entries), expected))

    # the population line, by string equality
    scan_paths = [p for p in keys if p.rsplit(".", 1)[-1] == SCAN_KEY]
    for path in scan_paths:
        present, value = lookup(data, path)
        if present and isinstance(value, str) and value != walk_result["line"]:
            reasons.append("para_scan: rendered line does not match the walk")

    return reasons, extra


def check_failed_record(data):
    reasons = []
    for key in ("status", "reason", "next", "unvalidated_report"):
        if key not in data or data[key] is None:
            reasons.append("key missing: %s" % key)
    return reasons


# ---------------------------------------------------------------- the walker, by sibling path

def load_walker():
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("lint_para_facts", os.path.join(here, "lint-para-facts.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------- entry points

def emit(obj, code):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False) + "\n")
    return code


def cmd_schema(args):
    try:
        schema = load_schema(args.schema)
    except SchemaUnreadable as exc:
        return emit({"status": "schema_unreadable", "reason": str(exc)}, 2)
    sys.stdout.write(json.dumps(schema, ensure_ascii=False, indent=1) + "\n")
    return 0


def cmd_check(args):
    fmt = args.format or ("json" if args.report.lower().endswith(".json") else "yaml")
    try:
        data = load_report(args.report, fmt)
    except Exception as exc:
        msg = " ".join(str(exc).split())
        return emit({"status": "failed", "reason": "parse: %s" % msg, "kind": args.kind}, 1)

    if args.kind == "failed":
        reasons = check_failed_record(data)
        if reasons:
            return emit({"status": "failed", "reason": "; ".join(reasons), "kind": "failed"}, 1)
        return emit({"status": "ok", "kind": "failed"}, 0)

    if not args.mode:
        sys.stderr.write("lint-report-check: --mode full|scoped is required for --kind report\n")
        return 2
    if not args.dir:
        sys.stderr.write("lint-report-check: at least one --dir is required for --kind report\n")
        return 2
    try:
        schema = load_schema(args.schema)
    except SchemaUnreadable as exc:
        return emit({"status": "schema_unreadable", "reason": str(exc)}, 2)

    walker = load_walker()
    try:
        walk = walker.walk(args.dir, args.exclude, args.root)
    except FileNotFoundError as exc:
        sys.stderr.write("lint-report-check: --dir is not a directory: %s\n" % exc)
        return 2
    walk["line"] = walker.scan_line(walk)

    reasons, extra = check_report(data, schema, args.mode, walk)
    verdict = {
        "status": "failed" if reasons else "ok",
        "kind": "report",
        "mode": args.mode,
        "schema_keys": len(schema["keys"]),
        "extra_keys": extra,
        "walk": walk["counts"],
    }
    if reasons:
        verdict["reason"] = "; ".join(reasons)
        return emit(verdict, 1)
    return emit(verdict, 0)


def main(argv):
    ap = argparse.ArgumentParser(description="the vlt-lint persist gate — reads a report back against report.md's fence; writes nothing")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sc = sub.add_parser("schema", help="print the parsed fence")
    sc.add_argument("--schema", default=DEFAULT_SCHEMA)
    ck = sub.add_parser("check", help="validate one rendered report (or failed-run record)")
    ck.add_argument("--report", required=True)
    ck.add_argument("--mode", choices=("full", "scoped"))
    ck.add_argument("--dir", action="append", default=[])
    ck.add_argument("--exclude", action="append", default=[])
    ck.add_argument("--root", default=".")
    ck.add_argument("--schema", default=DEFAULT_SCHEMA)
    ck.add_argument("--kind", choices=("report", "failed"), default="report")
    ck.add_argument("--format", choices=("yaml", "json"), help="override the extension-derived format")
    args = ap.parse_args(argv)
    return cmd_schema(args) if args.cmd == "schema" else cmd_check(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
