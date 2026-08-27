#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Read and write the vlt-lint findings-cache sidecar (`_agent/lint-cache.json`).

Cycle 14 build-2 (A14-8). The cache shipped in Cycle 12 and never once worked:
the reader (`vlt-lint-full.js`, the `cachedScans.filter((c) => c && c.slug &&
c.key && c.scan)` line) required `{slug, key, scan}` records, while the write
step was PROSE telling the SKILL to persist a differently-shaped value — one
contract stated twice, with no enforcement point where the two meet. This
script is that enforcement point on the write side: the SKILL no longer
hand-emits a serialization, it runs an executable.

Two callers, both in `references/full-scale.md`:
  - step 2 (`read`)  — hand the returned `records` to the workflow as `cachedScans`.
  - step 5 (`write`) — persist the workflow's returned `cache_records` verbatim.

What this script deliberately does NOT do: re-validate the record schema. The
reader-side filter in `vlt-lint-full.js` is the SINGLE HOME of what makes a
record usable, and the workflow's returned `cache_rejected` is its instrument.
A write-side copy of that predicate would be a second statement of one
contract — the exact defect this build exists to remove. The workflow
constructs every record it returns, so records reaching this writer are
well-formed by construction.

File shape:

    {"fingerprint": "<cache_fingerprint>", "written": "YYYY-MM-DD", "records": [...]}

The top-level `fingerprint` is INFORMATIONAL ONLY and is never a source of a
reuse decision. The per-record `key` is the sole authority. The pre-repair
sidecar's fatal shape was a top-level fingerprint with no per-page digest, and
this file must not read as a return to it.

Exit codes: `read` exits 0 for ok, missing AND unparseable alike — a cold run
is not an error (full-scale.md step 2's standing mandate). Non-zero is reserved
for a genuine failure to write.
"""

import argparse
import datetime
import json
import os
import sys
import tempfile

SIDECAR = "lint-cache.json"
LEGACY = "lint-cache.yaml"
AGENT_DIR = "_agent"


def _paths(vault_root):
    agent = os.path.join(os.path.abspath(vault_root), AGENT_DIR)
    return agent, os.path.join(agent, SIDECAR), os.path.join(agent, LEGACY)


def _emit(obj):
    sys.stdout.write(json.dumps(obj) + "\n")


def cmd_read(args):
    _agent, sidecar, _legacy = _paths(args.vault_root)
    if not os.path.isfile(sidecar):
        _emit({"status": "missing", "reason": "no sidecar at _agent/%s (first full sweep, or it was deleted — a cold run, never an error)" % SIDECAR, "records": [], "count": 0})
        return 0
    try:
        with open(sidecar, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as exc:
        _emit({"status": "unparseable", "reason": "sidecar at _agent/%s did not parse as JSON (%s) — a cold run, never an error" % (SIDECAR, type(exc).__name__), "records": [], "count": 0})
        return 0
    if not isinstance(data, dict) or not isinstance(data.get("records"), list):
        _emit({"status": "unparseable", "reason": "sidecar at _agent/%s parsed but carries no records: list — a cold run, never an error" % SIDECAR, "records": [], "count": 0})
        return 0
    records = data["records"]
    _emit({
        "status": "ok",
        "reason": "read %d record(s) from _agent/%s" % (len(records), SIDECAR),
        "records": records,
        "count": len(records),
        "fingerprint": data.get("fingerprint"),
        "written": data.get("written"),
    })
    return 0


def _load_records(spec):
    raw = sys.stdin.read() if spec == "-" else open(spec, "r", encoding="utf-8").read()
    records = json.loads(raw)
    if not isinstance(records, list):
        raise ValueError("--records must be a JSON array of the workflow's returned cache_records")
    return records


def cmd_write(args):
    agent, sidecar, legacy = _paths(args.vault_root)
    try:
        records = _load_records(args.records)
    except Exception as exc:
        sys.stderr.write("lint-cache: could not read --records: %s\n" % exc)
        return 2
    payload = {
        "fingerprint": args.fingerprint,
        "written": args.today or datetime.date.today().isoformat(),
        "records": records,
    }
    try:
        os.makedirs(agent, exist_ok=True)
        # Atomic: temp file in the SAME directory, then os.replace — an interrupted sweep
        # never leaves a half-written sidecar that the next run reads as unparseable.
        fd, tmp = tempfile.mkstemp(dir=agent, prefix=".lint-cache.", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, sort_keys=True)
                fh.write("\n")
            os.replace(tmp, sidecar)
        except Exception:
            if os.path.exists(tmp):
                os.unlink(tmp)
            raise
    except Exception as exc:
        sys.stderr.write("lint-cache: could not write _agent/%s: %s\n" % (SIDECAR, exc))
        return 2
    # The legacy .yaml sidecar cannot express the reader's key even in principle (it stored
    # one top-level fingerprint and no per-page digest), so it is not converted — it is
    # removed, rather than left as an unowned file at a path the contract's Decay table no
    # longer covers.
    legacy_removed = False
    if os.path.isfile(legacy):
        try:
            os.unlink(legacy)
            legacy_removed = True
        except Exception:
            legacy_removed = False
    _emit({"written": len(records), "path": sidecar, "legacy_removed": legacy_removed})
    return 0


def main(argv):
    ap = argparse.ArgumentParser(description="read/write the vlt-lint findings-cache sidecar")
    sub = ap.add_subparsers(dest="mode", required=True)

    r = sub.add_parser("read", help="print the sidecar's records as JSON (exit 0 even when missing/unparseable)")
    r.add_argument("--vault-root", required=True, help="absolute path to the vault root")

    w = sub.add_parser("write", help="rewrite the sidecar whole from the workflow's returned cache_records")
    w.add_argument("--vault-root", required=True, help="absolute path to the vault root")
    w.add_argument("--fingerprint", default="", help="the workflow's returned cache_fingerprint (informational only)")
    w.add_argument("--records", required=True, help="path to a JSON array of cache_records, or - for stdin")
    w.add_argument("--today", default="", help="'YYYY-MM-DD' for the written: stamp (defaults to today)")

    args = ap.parse_args(argv)
    return cmd_read(args) if args.mode == "read" else cmd_write(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
