#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""Pre-tag packaging lint for the vlt module repo (build-14).

The release boundary's bell: every tag is cut only after this exits 0. Checks
the WORKING TREE ON DISK, never the git index — vlt-upgrade's own-the-apply is
a filesystem copy, so a git-scoped check silently misses on-disk cruft.

Groups:
  A — on-disk cruft (.decision-log.md, __pycache__/, *.pyc, .DS_Store) within
      the shipped surface (skills/vlt-*/**, .claude-plugin/**) + repo root depth 1
  B — module-help.csv canon: header equals merge-help-csv.py's HEADER (imported,
      never duplicated), every row parses to exactly len(HEADER) fields, and the
      free-text fields (display-name, description, args, outputs) are
      double-quoted in the raw line whenever non-empty (always-quote rule)
  C — resolvability + version agreement: module.yaml parses, module_version
      equals marketplace.json plugins[0].version, governance bundle home exists
      non-empty, and marketplace skills[] maps one-to-one onto skills/vlt-* dirs
  D — tag intent: with --expect-version X.Y.Z, both version strings equal it;
      without the flag, reported SKIPPED (not PASS)

Usage: uv run tools/package-lint.py [--expect-version X.Y.Z] [--root PATH]
Exit: 0 = all groups PASS (or D SKIPPED); non-zero on any FAIL.
"""

import argparse
import csv
import importlib.util
import json
import sys
from io import StringIO
from pathlib import Path

import yaml

# The HEADER import execs merge-help-csv.py; without this the lint would write
# the very __pycache__ cruft group A polices.
sys.dont_write_bytecode = True

CRUFT_NAMES = {".DS_Store", ".decision-log.md"}
CRUFT_DIR_NAMES = {"__pycache__"}
CRUFT_SUFFIXES = {".pyc"}

# Free-text columns of module-help.csv that must be quoted when non-empty
# (CLAUDE.md always-quote rule). Indexes resolved against the imported HEADER.
FREE_TEXT_FIELDS = ["display-name", "description", "args", "outputs"]


def is_cruft(path: Path) -> bool:
    if path.is_dir():
        return path.name in CRUFT_DIR_NAMES
    return path.name in CRUFT_NAMES or path.suffix in CRUFT_SUFFIXES


def check_group_a(root: Path) -> list:
    """On-disk cruft within the shipped surface + repo root depth 1."""
    hits = []
    scopes = list(root.glob("skills/vlt-*")) + [root / ".claude-plugin"]
    for scope in scopes:
        if not scope.exists():
            continue
        for p in scope.rglob("*"):
            if is_cruft(p):
                hits.append(p.relative_to(root))
    for p in root.iterdir():  # repo root, depth 1 (./.DS_Store has shipped before)
        if is_cruft(p):
            hits.append(p.relative_to(root))
    return [f"cruft on disk: {h}" for h in sorted(set(hits))]


def load_canonical_header(root: Path) -> list:
    """Import HEADER from merge-help-csv.py — the single source; never a copy."""
    script = root / "skills/vlt-setup/scripts/merge-help-csv.py"
    spec = importlib.util.spec_from_file_location("merge_help_csv", script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return list(mod.HEADER)


def field_quote_flags(line: str) -> list:
    """For one raw CSV line, return whether each field is double-quoted."""
    flags = []
    i, n = 0, len(line)
    while i <= n:
        quoted = i < n and line[i] == '"'
        flags.append(quoted)
        if quoted:
            i += 1
            while i < n:
                if line[i] == '"':
                    if i + 1 < n and line[i + 1] == '"':  # escaped quote
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            i += 1  # past the comma (or end)
        else:
            nxt = line.find(",", i)
            if nxt == -1:
                break
            i = nxt + 1
    return flags


def check_group_b(root: Path) -> list:
    """module-help.csv: canonical header, 13-field rows, always-quote free text."""
    failures = []
    csv_path = root / "skills/vlt-setup/assets/module-help.csv"
    if not csv_path.exists():
        return [f"missing: {csv_path.relative_to(root)}"]
    try:
        header = load_canonical_header(root)
    except Exception as e:
        return [f"cannot import HEADER from merge-help-csv.py: {e}"]

    raw_lines = csv_path.read_text(encoding="utf-8").splitlines()
    rows = list(csv.reader(StringIO("\n".join(raw_lines))))
    if not rows:
        return ["module-help.csv is empty"]
    if rows[0] != header:
        failures.append(
            f"header is not canonical (expected {len(header)} cols "
            f"preceded-by/followed-by; got {rows[0][:13]})"
        )
        return failures  # positional checks below are meaningless off-canon

    free_text_idx = [header.index(f) for f in FREE_TEXT_FIELDS]
    for line_no, row in enumerate(rows[1:], start=2):
        if not row:
            continue
        if len(row) != len(header):
            failures.append(
                f"line {line_no}: {len(row)} fields, expected {len(header)} "
                f"(skill {row[1] if len(row) > 1 else '?'})"
            )
            continue
        flags = field_quote_flags(raw_lines[line_no - 1])
        for idx in free_text_idx:
            if row[idx] and (idx >= len(flags) or not flags[idx]):
                failures.append(
                    f"line {line_no}: free-text field '{header[idx]}' is "
                    f"non-empty but unquoted in the raw line (always-quote rule)"
                )
    return failures


def check_group_c(root: Path) -> tuple:
    """Resolvability + version agreement. Returns (failures, versions_or_None)."""
    failures = []
    yaml_path = root / "skills/vlt-setup/assets/module.yaml"
    mkt_path = root / ".claude-plugin/marketplace.json"
    module_version = plugin_version = None

    try:
        module = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        module_version = module.get("module_version")
        if module_version is None:
            failures.append("module.yaml: module_version missing")
    except Exception as e:
        failures.append(f"module.yaml does not parse as YAML: {e}")

    listed_skills = None
    try:
        mkt = json.loads(mkt_path.read_text(encoding="utf-8"))
        plugins = mkt.get("plugins", [])
        if len(plugins) != 1:
            failures.append(f"marketplace.json: expected exactly 1 plugin, got {len(plugins)}")
        else:
            plugin_version = plugins[0].get("version")
            listed_skills = plugins[0].get("skills", [])
    except Exception as e:
        failures.append(f"marketplace.json does not parse: {e}")

    if module_version is not None and plugin_version is not None:
        if str(module_version) != str(plugin_version):
            failures.append(
                f"version mismatch: module.yaml module_version={module_version} "
                f"!= marketplace.json plugins[0].version={plugin_version}"
            )

    gov = root / "skills/vlt-setup/assets/governance/_meta"
    if not gov.is_dir() or not any(gov.iterdir()):
        failures.append("governance bundle home missing or empty: skills/vlt-setup/assets/governance/_meta/")

    # C5: skills[] <-> skills/vlt-* dirs, both directions
    if listed_skills is not None:
        listed = {Path(s).name for s in listed_skills}
        on_disk = {p.name for p in root.glob("skills/vlt-*") if p.is_dir()}
        for missing_dir in sorted(listed - on_disk):
            failures.append(f"marketplace.json lists '{missing_dir}' but skills/{missing_dir}/ does not exist (breaks install)")
        for unlisted in sorted(on_disk - listed):
            failures.append(f"skills/{unlisted}/ exists but is not in marketplace.json skills[] (silently doesn't ship)")

    return failures, (module_version, plugin_version)


def check_group_d(expect: str, versions) -> list:
    module_version, plugin_version = versions
    failures = []
    if str(module_version) != expect:
        failures.append(f"module.yaml module_version={module_version} != --expect-version {expect}")
    if str(plugin_version) != expect:
        failures.append(f"marketplace.json version={plugin_version} != --expect-version {expect}")
    return failures


def main():
    parser = argparse.ArgumentParser(description="Pre-tag packaging lint (working tree on disk).")
    parser.add_argument("--expect-version", help="Tag about to be cut; group D asserts both version strings equal it")
    parser.add_argument("--root", default=None, help="Repo root to lint (default: this script's repo)")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    results = {}
    results["A"] = ("on-disk cruft", check_group_a(root))
    results["B"] = ("module-help.csv canon", check_group_b(root))
    c_failures, versions = check_group_c(root)
    results["C"] = ("resolvability + version agreement", c_failures)
    if args.expect_version:
        results["D"] = (f"tag intent ({args.expect_version})", check_group_d(args.expect_version, versions))
    else:
        results["D"] = ("tag intent", None)  # SKIPPED

    failed = []
    for group, (label, failures) in results.items():
        if failures is None:
            print(f"SKIPPED group {group} — {label} (no --expect-version)")
        elif failures:
            print(f"FAIL group {group} — {label}:")
            for f in failures:
                print(f"  - {f}")
            failed.append(group)
        else:
            print(f"PASS group {group} — {label}")

    version = versions[1] or versions[0] or "?"
    if failed:
        print(f"package-lint: FAIL ({', '.join(failed)}) — vlt {version}")
        sys.exit(1)
    d_note = "D PASS" if args.expect_version else "D SKIPPED"
    print(f"package-lint: A/B/C PASS, {d_note} — vlt {version}")


if __name__ == "__main__":
    main()
