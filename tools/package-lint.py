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
  E — self-description integrity (build-23): the dev-side twin of vlt-lint's
      Convention coherence check — derives truth from the authoritative surface
      rather than confirming a string it expects. E1 handshake-bipartite
      (convention consumers: <-> consumer depends_on: pins, both directions),
      E2 structure-map SSoT (contract's hand-transcribed table <-> module.yaml
      vault_structure.default, its declared source of truth), E3 stray-pin
      (a name@version pin token in a SKILL.md body, outside depends_on: — a
      de-facto convention-consumption tell). Retires the self-confirming
      handshake grep every arc-3 build wrote by hand.

Usage: uv run tools/package-lint.py [--expect-version X.Y.Z] [--root PATH]
Exit: 0 = all groups PASS (or D SKIPPED); non-zero on any FAIL.
"""

import argparse
import csv
import importlib.util
import json
import re
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


def _read_frontmatter(path: Path) -> dict:
    """Parse the YAML frontmatter block (between the first two --- fences)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    lines = text.split("\n")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}
    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _e1_handshake(conventions: dict, acks: dict, skill_dirs: set) -> list:
    """E1: convention consumers: <-> consumer depends_on: pins, both directions.

    Derives the answer from BOTH sides of the handshake and compares — retiring
    the self-confirming `grep "<name>@"` every arc-3 build wrote by hand (which
    searched for the ack string it had just written). Vocabulary matches
    vlt-lint:131 so the dev-side and vault-side homes read alike.
    """
    failures = []
    for conv, (version, consumers) in conventions.items():
        for consumer in consumers:
            if consumer not in skill_dirs:
                failures.append(f"stale/dangling — {conv}@{version} lists {consumer} which is not installed")
                continue
            pinned = acks.get(consumer, {}).get(conv)
            if pinned is None:
                failures.append(
                    f"unacknowledged — {consumer} is a listed consumer of {conv}@{version} but does not ack it"
                )
            elif pinned != version:
                failures.append(f"stale — {consumer} acks {conv}@{pinned} but convention is @{version}")
    return failures


def _e2_structure_map(root: Path) -> list:
    """E2: the contract's hand-transcribed structure-map table vs its declared SSoT.

    module.yaml vault_structure.default is the SINGLE SOURCE OF TRUTH (module.yaml
    comment); the contract table's own note says "don't hand-transcribe it". A3-10:
    the table drifted anyway. Derive both sides and diff — the "authoritative
    source, not the declaration" pattern, enforcing the map's own promise.
    """
    failures = []
    yaml_path = root / "skills/vlt-setup/assets/module.yaml"
    try:
        module = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        ssot = dict(module["vault_structure"]["default"])
    except Exception as e:
        return [f"structure map: cannot read module.yaml vault_structure.default: {e}"]

    contract = root / "skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md"
    try:
        lines = contract.read_text(encoding="utf-8").splitlines()
    except Exception as e:
        return [f"structure map: cannot read vault-operating-contract.md: {e}"]

    # Anchor on the heading, then read the pipe table until the next `## ` section.
    # A data row is `| `key` | `path` | description |`; its first cell is a backticked
    # logical name (header/separator rows are not, so they are skipped naturally).
    heading = "## Path resolution — the structure map"
    table = {}
    in_section = False
    for line in lines:
        if line.strip() == heading:
            in_section = True
            continue
        if in_section:
            if line.startswith("## "):
                break
            s = line.strip()
            if not s.startswith("|"):
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) < 2:
                continue
            first = cells[0]
            if first.startswith("`") and first.endswith("`"):
                table[first.strip("`")] = cells[1].strip("`")

    for key in sorted(set(ssot) | set(table)):
        if key not in table:
            failures.append(f"structure map: {key} in module.yaml but not contract")
        elif key not in ssot:
            failures.append(f"structure map: {key} in contract but not module.yaml")
        elif str(ssot[key]) != table[key]:
            failures.append(
                f"structure map: {key} path {table[key]} (contract) != {ssot[key]} (module.yaml)"
            )
    return failures


def _e3_stray_pin(root: Path, conv_names: set) -> list:
    """E3: a name@version pin token in a SKILL.md body (outside depends_on:).

    The pin token is the strongest machine-detectable signal of convention
    consumption — you write it only to pin. It legitimately lives only in a
    skill's depends_on:; anywhere else it is a near-certain de-facto-consumption
    tell with near-zero false positives. Anchored on the known convention names
    (not a bare \\w+@\\d+) so an email address or unrelated foo@2 cannot trip it.
    """
    failures = []
    if not conv_names:
        return failures
    pattern = re.compile(r"\b(" + "|".join(re.escape(n) for n in sorted(conv_names)) + r")@(\d+)\b")
    for p in sorted(root.glob("skills/vlt-*/SKILL.md")):
        rel = p.relative_to(root)
        for lineno, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
            if line.lstrip().startswith("depends_on:"):
                continue
            m = pattern.search(line)
            if m:
                failures.append(
                    f"stray pin: {rel}:{lineno} recites the pin {m.group(1)}@{m.group(2)} outside "
                    f"depends_on: — a de-facto consumption signal; add it to depends_on: and the "
                    f"convention's consumers:, or rewrite the reference as a version-free pointer "
                    f"(pointer-vs-ack: roadmap :1682)"
                )
    return failures


def check_group_e(root: Path) -> list:
    """Self-description integrity: E1 handshake-bipartite, E2 structure-map SSoT, E3 stray-pin.

    Aggregates three failure lists. Each check derives truth from the authoritative
    surface and compares, rather than confirming a declaration about it — the fix
    the whole arc pointed at.
    """
    conv_dir = root / "skills/vlt-setup/assets/governance/_meta/conventions"
    conventions = {}  # name -> (version_str, [consumers])
    for f in sorted(conv_dir.glob("*.md")):
        fm = _read_frontmatter(f)
        version, consumers = fm.get("version"), fm.get("consumers")
        # A file lacking either is vlt-lint:75's convention_meta_missing jurisdiction
        # (vault time); Group E's remit is the handshake, not enforcement frontmatter.
        if version is None or consumers is None:
            continue
        conventions[f.stem] = (str(version), list(consumers))

    skill_dirs = {p.name for p in root.glob("skills/vlt-*") if p.is_dir()}
    acks = {}  # skill_name -> {conv_name: version_str}
    for p in sorted(root.glob("skills/vlt-*/SKILL.md")):
        pins = {}
        for entry in _read_frontmatter(p).get("depends_on") or []:
            name, sep, ver = str(entry).partition("@")
            if sep:
                pins[name] = ver
        acks[p.parent.name] = pins

    return (
        _e1_handshake(conventions, acks, skill_dirs)
        + _e2_structure_map(root)
        + _e3_stray_pin(root, set(conventions))
    )


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
    results["E"] = ("self-description integrity", check_group_e(root))

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
    print(f"package-lint: A/B/C/E PASS, {d_note} — vlt {version}")


if __name__ == "__main__":
    main()
