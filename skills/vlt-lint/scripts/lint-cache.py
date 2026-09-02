#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Read, write and evict from the vlt-lint findings-cache sidecar (`_agent/lint-cache.json`).

Cycle 14 build-2 (A14-8). The cache shipped in Cycle 12 and never once worked:
the reader (`vlt-lint-full.js`, the `cachedScans.filter((c) => c && c.slug &&
c.key && c.scan)` line) required `{slug, key, scan}` records, while the write
step was PROSE telling the SKILL to persist a differently-shaped value — one
contract stated twice, with no enforcement point where the two meet. This
script is that enforcement point on the write side: the SKILL no longer
hand-emits a serialization, it runs an executable.

Three callers, all in `references/full-scale.md`:
  - step 2 (`read`)    — hand the returned `records` to the workflow as `cachedScans`.
  - step 2 / 5 (`evict`) — remove one named page's record (Cycle 15 build-2, A15-4): on
    request before the step-2 read (`full lint, re-scan <slug>`), or for a finding the
    operator refuses as false AFTER the step-5 write (a whole-file write before the
    evict would write the record straight back).
  - step 5 (`write`)   — persist the workflow's returned `cache_records` verbatim.

What this script deliberately does NOT do: re-validate the record schema. The
reader-side filter in `vlt-lint-full.js` is the SINGLE HOME of what makes a
record usable, and the workflow's returned `cache_rejected` is its instrument.
A write-side copy of that predicate would be a second statement of one
contract — the exact defect this build exists to remove. The workflow
constructs every record it returns, so records reaching this writer are
well-formed by construction.

File shape:

    {"fingerprint": "<cache_fingerprint>", "components": {...}, "written": "YYYY-MM-DD", "records": [...]}

The top-level `fingerprint` and `components` are INFORMATIONAL ONLY and are
never a source of a reuse decision. The per-record `key` is the sole authority.
`components` (the workflow's returned `cache_components`: `scan_model` + the
three scanner-read `convention_digests`, by name) exists so the SKILL can name
which term moved on a cold run — nothing more. The pre-repair sidecar's fatal
shape was a top-level fingerprint with no per-page digest, and this file must
not read as a return to it.

Exit codes: `read` exits 0 for ok, missing AND unparseable alike — a cold run
is not an error (full-scale.md step 2's standing mandate). Non-zero is reserved
for a genuine failure to write. `evict` exits non-zero when it evicted nothing
(a slug matching no record; a missing or unparseable sidecar is `evicted 0 of
0`) — an eviction that removed no record is the one outcome the operator must
not mistake for success.
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
        "components": data.get("components"),
        "written": data.get("written"),
    })
    return 0


def _load_records(spec):
    raw = sys.stdin.read() if spec == "-" else open(spec, "r", encoding="utf-8").read()
    records = json.loads(raw)
    if not isinstance(records, list):
        raise ValueError("--records must be a JSON array of the workflow's returned cache_records")
    return records


def _load_components(spec):
    if not spec:
        return None
    raw = sys.stdin.read() if spec == "-" else open(spec, "r", encoding="utf-8").read()
    components = json.loads(raw)
    if not isinstance(components, dict):
        raise ValueError("--components must be a JSON object (the workflow's returned cache_components)")
    return components


def _atomic_write(agent, sidecar, payload):
    """The ONE writer: `write` and `evict` both land the sidecar through here.

    Atomic: temp file in the SAME directory, then os.replace — an interrupted sweep never
    leaves a half-written sidecar that the next run reads as unparseable.
    """
    os.makedirs(agent, exist_ok=True)
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


def cmd_write(args):
    agent, sidecar, legacy = _paths(args.vault_root)
    try:
        records = _load_records(args.records)
    except Exception as exc:
        sys.stderr.write("lint-cache: could not read --records: %s\n" % exc)
        return 2
    try:
        components = _load_components(args.components)
    except Exception as exc:
        sys.stderr.write("lint-cache: could not read --components: %s\n" % exc)
        return 2
    payload = {
        "fingerprint": args.fingerprint,
        "written": args.today or datetime.date.today().isoformat(),
        "records": records,
    }
    if components is not None:
        payload["components"] = components
    try:
        _atomic_write(agent, sidecar, payload)
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


def cmd_evict(args):
    """Remove every record whose `slug` EXACTLY equals a given --slug (A15-4, roundtable A13).

    Records are keyed on the SKILL-supplied slug (the workflow's cache_records comment), so
    there is no normalization here: a slug that does not match is a loud miss (exit 1),
    never a silent near-match. The rest of the sidecar — fingerprint, components, written,
    the other records — is preserved and rewritten through the same atomic writer `write`
    uses. Evicting nothing is the failure this subcommand exists to make loud.
    """
    agent, sidecar, _legacy = _paths(args.vault_root)
    wanted = list(dict.fromkeys(args.slug))
    if not os.path.isfile(sidecar):
        _emit({"evicted": 0, "of": 0, "missing": wanted, "reason": "no sidecar at _agent/%s — nothing to evict" % SIDECAR})
        sys.stderr.write("evicted 0 of 0\n")
        return 1
    try:
        with open(sidecar, "r", encoding="utf-8") as fh:
            data = json.load(fh)
        if not isinstance(data, dict) or not isinstance(data.get("records"), list):
            raise ValueError("no records: list")
    except Exception as exc:
        _emit({"evicted": 0, "of": 0, "missing": wanted, "reason": "sidecar at _agent/%s is unparseable (%s) — nothing to evict; the next full run is cold" % (SIDECAR, type(exc).__name__)})
        sys.stderr.write("evicted 0 of 0\n")
        return 1
    records = data["records"]
    total = len(records)
    present = {r.get("slug") for r in records if isinstance(r, dict)}
    kept = [r for r in records if not (isinstance(r, dict) and r.get("slug") in wanted)]
    evicted = total - len(kept)
    missing = [slug for slug in wanted if slug not in present]
    if evicted:
        data["records"] = kept
        try:
            _atomic_write(agent, sidecar, data)
        except Exception as exc:
            sys.stderr.write("lint-cache: could not write _agent/%s: %s\n" % (SIDECAR, exc))
            return 2
    _emit({"evicted": evicted, "of": total, "missing": missing, "path": sidecar})
    sys.stderr.write("evicted %d of %d\n" % (evicted, total))
    return 0 if evicted else 1


def main(argv):
    ap = argparse.ArgumentParser(description="read/write/evict the vlt-lint findings-cache sidecar")
    sub = ap.add_subparsers(dest="mode", required=True)

    r = sub.add_parser("read", help="print the sidecar's records as JSON (exit 0 even when missing/unparseable)")
    r.add_argument("--vault-root", required=True, help="absolute path to the vault root")

    w = sub.add_parser("write", help="rewrite the sidecar whole from the workflow's returned cache_records")
    w.add_argument("--vault-root", required=True, help="absolute path to the vault root")
    w.add_argument("--fingerprint", default="", help="the workflow's returned cache_fingerprint (informational only)")
    w.add_argument("--records", required=True, help="path to a JSON array of cache_records, or - for stdin")
    w.add_argument("--today", default="", help="'YYYY-MM-DD' for the written: stamp (defaults to today)")
    w.add_argument("--components", default="", help="path to the workflow's returned cache_components JSON object, or - for stdin (informational only; lets a cold run name which term moved)")

    e = sub.add_parser("evict", help="remove the named page(s)' records so the next full sweep re-derives exactly those pages (exit 1 when nothing was evicted)")
    e.add_argument("--vault-root", required=True, help="absolute path to the vault root")
    e.add_argument("--slug", action="append", required=True, help="exact page slug to evict (repeatable)")

    args = ap.parse_args(argv)
    return {"read": cmd_read, "write": cmd_write, "evict": cmd_evict}[args.mode](args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
