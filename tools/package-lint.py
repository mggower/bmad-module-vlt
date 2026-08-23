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
      non-empty, and marketplace skills[] maps one-to-one onto skills/vlt-* dirs;
      plus C6 (build B5-7) derived-artifact freshness: vault-rule-card.md exists,
      its frontmatter derived_from: sha256 equals the shipped contract's actual
      SHA-256 (a contract edit without re-deriving the card fails), and the card
      is within its 8,000-byte budget (a digest that balloons re-creates the
      whale under a new name); plus C7 (build B5-8) router integrity: every
      skills/vlt-*/references/*.md is named by its skill's SKILL.md or a
      sibling reference (no orphan reference), every `references/<name>.md`
      token in a router or reference resolves to a real file (no dangling
      route), and the two re-cut routers stay within their byte budgets; plus
      C8 (build B5-9) enforcement-kit agreement: the tripwires seed parses as
      YAML with every wire carrying all required fields, every wire's metric
      id exists in vlt-vitals.py's canonical METRICS table (parsed from the
      asset, never re-declared), vlt-vitals.py compiles, and module.yaml's
      default map carries the tripwires + lint_reports rows; plus C9 (build
      B7-2, the enumeration-vs-structure doctrine) durability nets:
      merge-config.py's merge_config() preserves a defined variable absent
      from the answers and reports removals (in-process probe against the
      real script), and verify-skill-manifest.py's computed scope contains
      this check's own independent walk of the shipped skill dirs (never
      confirming the script's claim about itself)
  D — tag intent: with --expect-version X.Y.Z, both version strings equal it and
      CHANGELOG.md carries exactly one dated `## vX.Y.Z — YYYY-MM-DD` entry
      (build B6-1; existence + heading only, never a grade on the entry's prose);
      without the flag, reported SKIPPED (not PASS)
  E — self-description integrity (build-23): the dev-side twin of vlt-lint's
      Convention coherence check — derives truth from the authoritative surface
      rather than confirming a string it expects. E1 handshake-bipartite
      (convention consumers: <-> consumer depends_on: pins, both directions),
      E2 structure-map SSoT (contract's hand-transcribed table <-> module.yaml
      vault_structure.default, its declared source of truth), E3 stray-pin
      (a name@version pin token in a SKILL.md or references/*.md body, outside
      depends_on: — a de-facto convention-consumption tell; widened to
      reference files by B5-8, since mechanics moved there exit a
      SKILL.md-only scan). Retires the self-confirming handshake grep every
      arc-3 build wrote by hand. E4 harness-coverage (build B7-1, standing
      rule R2): every gate check callable (introspected, never listed) has a
      tools/test-package-lint.py case declaring it can make that check fail —
      a gate check with no fixture case is itself a lint failure. E5
      asset-node handshake (build B7-6): every shipped workflow file
      (skills/vlt-setup/assets/workflows/*.js) carries exactly one
      machine-parseable `// depends_on: [...]` header line of flat
      "name@version" pins (or []), and asset consumers — a convention
      consumers: entry ending .js — are bipartite-checked both directions
      in E1's vocabulary; E1 skips .js entries (E5 owns them, one shared
      predicate). E6 schema-size budget (build B10-12): every fan-out output
      schema in every workflow asset (discovered structurally by
      type: 'object', never a hand-kept list) serializes to
      JSON.stringify(schema).length <= 3700 — the standing margin device that
      stops a tri-state-style description from silently re-crossing the
      harness classifier's ~4096-char output-schema ceiling (the v0.13.0
      non-executable-full-lint failure). Measured by a node subprocess so the
      figure reproduces the runtime's own JSON.stringify, never a
      source-literal char count.

Usage: uv run tools/package-lint.py [--expect-version X.Y.Z] [--root PATH]
Exit: 0 = all groups PASS (or D SKIPPED); non-zero on any FAIL.
"""

import argparse
import csv
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
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

    failures.extend(check_rule_card(root))
    failures.extend(check_router_integrity(root))
    failures.extend(check_enforcement_kit(root))
    failures.extend(check_durability_nets(root))

    return failures, (module_version, plugin_version)


RULE_CARD_BUDGET = 8000  # bytes — B5-7 disposition 2's acceptance bound
ROUTER_BUDGETS = {  # bytes — B5-8 disposition 8's acceptance bounds
    "vlt-dispatch": 14000,
    "vlt-lint": 12000,
}
REF_TOKEN_RE = re.compile(r"references/([A-Za-z0-9_-]+\.md)")


def check_router_integrity(root: Path) -> list:
    """C7 (build B5-8): router<->reference agreement for re-cut skills.

    The re-cut moved skill mechanics into skills/vlt-*/references/*.md read at
    the moment that uses them — creating a new cross-file agreement with no
    net. This check is the net, both directions: an orphan reference (on disk,
    named by no router or sibling reference) and a dangling route (a
    `references/<name>.md` token naming a file that does not exist) each FAIL.
    Also enforces the re-cut routers' byte budgets (ROUTER_BUDGETS), the
    RULE_CARD_BUDGET idiom one artifact class over.
    """
    failures = []
    for skill_dir in sorted(p for p in root.glob("skills/vlt-*") if p.is_dir()):
        router = skill_dir / "SKILL.md"
        refs_dir = skill_dir / "references"
        ref_files = sorted(refs_dir.glob("*.md")) if refs_dir.is_dir() else []
        scan_files = ([router] if router.is_file() else []) + ref_files
        texts = {p: p.read_text(encoding="utf-8") for p in scan_files}
        existing = {r.name for r in ref_files}
        for ref in ref_files:
            token = f"references/{ref.name}"
            if not any(token in texts[p] for p in scan_files if p != ref):
                failures.append(
                    f"orphan reference: {ref.relative_to(root)} is named by neither "
                    f"its SKILL.md nor a sibling reference — nothing routes to it"
                )
        for p in scan_files:
            for lineno, line in enumerate(texts[p].splitlines(), start=1):
                for m in REF_TOKEN_RE.finditer(line):
                    if m.group(1) not in existing:
                        failures.append(
                            f"dangling route: {p.relative_to(root)}:{lineno} names "
                            f"references/{m.group(1)} which does not exist"
                        )
        budget = ROUTER_BUDGETS.get(skill_dir.name)
        if budget is not None and router.is_file():
            size = router.stat().st_size
            if size > budget:
                failures.append(
                    f"router over budget: {router.relative_to(root)} is {size:,} bytes "
                    f"> {budget:,} (the re-cut's eager surface must stay thin — move "
                    f"mechanics to references/)"
                )
    return failures


def check_rule_card(root: Path) -> list:
    """C6 (build B5-7): derived-artifact freshness for the shipped rule-card.

    The card is factory-authored and MARKED derived (frontmatter derived_from:
    carries the shipped contract's SHA-256). This check keeps the marker honest
    by machine, not by memory: a factory edit to the contract without
    re-deriving the card fails here — the drift this artifact class invites.
    """
    failures = []
    card = root / "skills/vlt-setup/assets/governance/_meta/vault-rule-card.md"
    contract = root / "skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md"
    if not card.is_file():
        return ["rule-card missing: skills/vlt-setup/assets/governance/_meta/vault-rule-card.md (the ceremony's eager read — partners point at it)"]

    size = card.stat().st_size
    if size > RULE_CARD_BUDGET:
        failures.append(
            f"rule-card over budget: {size:,} bytes > {RULE_CARD_BUDGET:,} "
            f"(a digest that balloons re-creates the whale — re-distill it)"
        )

    declared = str(_read_frontmatter(card).get("derived_from") or "")
    m = re.search(r"sha256:([0-9a-f]{64})", declared)
    if not m:
        failures.append("rule-card: frontmatter derived_from: carries no sha256:<64-hex> marker")
    elif not contract.is_file():
        failures.append("rule-card: shipped contract missing — cannot verify derived_from:")
    else:
        actual = hashlib.sha256(contract.read_bytes()).hexdigest()
        if m.group(1) != actual:
            failures.append(
                f"rule-card stale: derived_from sha256 {m.group(1)[:12]}… != shipped contract "
                f"{actual[:12]}… — the contract changed without re-deriving the card"
            )
    return failures


def check_enforcement_kit(root: Path) -> list:
    """C8 (build B5-9): enforcement-kit packaging agreement.

    The kit's promises get a deterministic factory net (the C6/C7 precedent):
    (a) the tripwires seed parses as YAML and every wire carries all required
    fields; (b) every wire's metric id exists in vlt-vitals.py's canonical
    METRICS table — parsed by importing the asset, never re-declared here;
    (c) vlt-vitals.py compiles; (d) module.yaml's default map carries the
    tripwires and lint_reports rows the kit resolves through.
    """
    import py_compile
    import tempfile

    failures = []
    vitals = root / "skills/vlt-setup/assets/hooks/vlt-vitals.py"
    seed = root / "skills/vlt-setup/assets/tripwires.yaml"

    # (c) the reader compiles — checked first; (b) depends on importing it.
    # The .pyc goes to a throwaway temp path, never beside the source — a
    # default cfile would write the very __pycache__ cruft group A polices.
    if not vitals.is_file():
        return ["enforcement kit: vitals reader missing: skills/vlt-setup/assets/hooks/vlt-vitals.py"]
    with tempfile.TemporaryDirectory() as tmp:
        try:
            py_compile.compile(str(vitals), cfile=str(Path(tmp) / "vlt-vitals.pyc"), doraise=True)
        except py_compile.PyCompileError as e:
            return [f"enforcement kit: vlt-vitals.py does not compile: {e.msg.splitlines()[-1] if e.msg else e}"]

    metrics = None
    required_fields = None
    try:
        spec = importlib.util.spec_from_file_location("vlt_vitals_lint", vitals)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        metrics = set(mod.METRICS)
        required_fields = list(mod.WIRE_REQUIRED_FIELDS)  # imported, never re-declared
        if not metrics:
            failures.append("enforcement kit: vlt-vitals.py METRICS table is empty")
    except Exception as e:
        failures.append(f"enforcement kit: cannot read METRICS/WIRE_REQUIRED_FIELDS from vlt-vitals.py: {e}")

    # (a) seed parses; every wire complete. (b) metric ids canonical.
    if not seed.is_file():
        failures.append("enforcement kit: tripwires seed missing: skills/vlt-setup/assets/tripwires.yaml")
    else:
        try:
            data = yaml.safe_load(seed.read_text(encoding="utf-8"))
            wires = (data or {}).get("wires")
            if not isinstance(wires, list) or not wires:
                failures.append("enforcement kit: tripwires.yaml carries no wires: list")
            else:
                for w in wires:
                    wid = (w or {}).get("id", "(no id)")
                    missing = [f for f in (required_fields or []) if not (w or {}).get(f)]
                    if missing:
                        failures.append(
                            f"enforcement kit: seed wire '{wid}' missing required field(s): {', '.join(missing)}"
                        )
                    if metrics is not None and (w or {}).get("metric") not in metrics:
                        failures.append(
                            f"enforcement kit: seed wire '{wid}' names metric "
                            f"'{(w or {}).get('metric')}' — not in vlt-vitals.py's canonical table"
                        )
        except Exception as e:
            failures.append(f"enforcement kit: tripwires.yaml does not parse as YAML: {e}")

    # (d) the structure map carries the kit's two logical paths.
    try:
        module = yaml.safe_load((root / "skills/vlt-setup/assets/module.yaml").read_text(encoding="utf-8"))
        default_map = module["vault_structure"]["default"]
        for key in ("tripwires", "lint_reports"):
            if key not in default_map:
                failures.append(f"enforcement kit: module.yaml vault_structure.default lacks the '{key}' row")
    except Exception as e:
        failures.append(f"enforcement kit: cannot read module.yaml default map: {e}")

    return failures


def _import_script(path: Path, name: str):
    """Import a shipped script by path (the load_canonical_header idiom —
    single source, never a copy)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_durability_nets(root: Path) -> list:
    """C9 (build B7-2): the durability nets are proven, structurally.

    Two mechanisms whose whole job is to protect vault state once defined
    their protected surface by enumeration and silently destroyed what the
    enumeration missed (A7-2/A7-3). This check is their standing proof:

    Probe 1 — merge-config preservation: call the real merge_config()
    in-process with a synthetic triple (an existing config carrying a
    defined variable's map with a vault-local sub-key plus one zombie key;
    answers omitting the variable). FAIL unless the variable survives
    byte-identical and the merge report names the zombie in `removed` and
    the variable in `preserved` — A7-2's reproduction table as a gate.
    Probe 1b (build B10-10): a module default key absent from the existing
    map must be ADDED by the key-level merge — existing keys byte-identical
    plus the new key, named in `structure_keys_added` — the C6-b fix's gate.

    Probe 2 — manifest structural scope: compare the script's computed
    manifest for this repo's own skills tree (source == live) against this
    check's OWN independent walk of the shipped vlt-* dirs (marketplace
    skills[] ∩ disk, cruft excluded). The truth side is the check's walk,
    never the script's claim about itself (the build-23/E-group posture) —
    a regression back to an enumeration goes red on the first references/
    or scripts/ file it drops.
    """
    failures = []
    scripts_dir = root / "skills/vlt-setup/scripts"

    # Probe 1 — merge-config preservation
    variable_map = {"wiki": "_agent/wiki/", "local_zone": "_agent/local-zone/"}
    existing = {
        "vlt": {
            "name": "Vault",
            "vault_structure": dict(variable_map),
            "zombie_key": "stale",
        }
    }
    module_yaml = {
        "code": "vlt",
        "name": "Vault",
        "module_version": "9.9.9",
        "vault_structure": {
            "prompt": "override paths?",
            "default": {"wiki": "_agent/wiki/"},
        },
    }
    answers = {"module": {}}
    try:
        mc = _import_script(scripts_dir / "merge-config.py", "merge_config_lint")
        result = mc.merge_config(existing, module_yaml, answers)
        config, report = result  # must be (config, merge_report)
        section = config["vlt"]
        if section.get("vault_structure") != variable_map:
            failures.append(
                "durability net (merge-config): a defined variable absent from "
                "the answers did not survive intact — got "
                f"{section.get('vault_structure')!r}, expected {variable_map!r} "
                "(preserve-unless-answered is broken)"
            )
        if "vault_structure" not in report.get("preserved", []):
            failures.append(
                "durability net (merge-config): merge report does not name the "
                "preserved variable in 'preserved' — removals/preservation "
                "would go unreported"
            )
        if "zombie_key" not in report.get("removed", []):
            failures.append(
                "durability net (merge-config): merge report does not name the "
                "dropped zombie key in 'removed' — a removal went silent"
            )
        # Probe 1b — structure-key injection (build B10-10, the C6-b fix):
        # a key newly added to module.yaml's default must reach a preserved
        # map, with every existing key (vault-grown local_zone included)
        # byte-identical and the report naming the addition.
        module_yaml_new_key = {
            "code": "vlt",
            "name": "Vault",
            "module_version": "9.9.9",
            "vault_structure": {
                "prompt": "override paths?",
                "default": {"wiki": "_agent/wiki/", "projects": "projects/"},
            },
        }
        config2, report2 = mc.merge_config(existing, module_yaml_new_key, answers)
        merged_map = config2["vlt"].get("vault_structure")
        expected_map = dict(variable_map)
        expected_map["projects"] = "projects/"
        if merged_map != expected_map:
            failures.append(
                "durability net (merge-config): a newly shipped default key "
                "never reaches an existing vault's map, or an existing key "
                f"was clobbered — got {merged_map!r}, expected {expected_map!r} "
                "(the C6-b key-level merge is broken)"
            )
        if report2.get("structure_keys_added") != ["projects"]:
            failures.append(
                "durability net (merge-config): merge report does not name the "
                "injected key in 'structure_keys_added' — got "
                f"{report2.get('structure_keys_added')!r} (a key addition went "
                "unreported)"
            )
    except Exception as e:
        failures.append(
            f"durability net (merge-config): merge_config() probe failed — {e} "
            "(the preserve-unless-answered contract, incl. the (config, report) "
            "return, is broken)"
        )

    # Probe 2 — manifest structural scope
    try:
        vsm = _import_script(
            scripts_dir / "verify-skill-manifest.py", "verify_skill_manifest_lint"
        )
        computed = set(
            vsm.compute_manifest(root, root / "skills", root / "skills")
        )
    except Exception as e:
        return failures + [
            f"durability net (manifest): cannot compute the manifest via "
            f"verify-skill-manifest.py — {e}"
        ]

    # The check's OWN walk — marketplace skills[] ∩ disk, cruft excluded.
    walk = set()
    try:
        mkt = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        listed = {Path(s).name for s in mkt["plugins"][0].get("skills", [])}
    except Exception as e:
        return failures + [f"durability net (manifest): cannot read marketplace skills[]: {e}"]
    for name in sorted(listed):
        skill_dir = root / "skills" / name
        if not skill_dir.is_dir():
            continue
        for f in skill_dir.rglob("*"):
            if f.is_file() and not any(
                part in CRUFT_DIR_NAMES for part in f.relative_to(root).parts
            ) and f.name not in CRUFT_NAMES and f.suffix not in CRUFT_SUFFIXES:
                walk.add(str(f.relative_to(root)))
    if not walk:
        failures.append(
            "durability net (manifest): the independent walk found no shipped "
            "files — the probe is vacuous (A7-1) and cannot prove the net"
        )
    for missing in sorted(walk - computed):
        failures.append(
            f"durability net (manifest): shipped file {missing} is absent from "
            "the script's computed manifest — the scope has narrowed back "
            "toward an enumeration"
        )
    return failures


def check_group_d(expect: str, versions, root: Path) -> list:
    module_version, plugin_version = versions
    failures = []
    if str(module_version) != expect:
        failures.append(f"module.yaml module_version={module_version} != --expect-version {expect}")
    if str(plugin_version) != expect:
        failures.append(f"marketplace.json version={plugin_version} != --expect-version {expect}")

    # D3 (build B6-1): the tag's changelog entry. Existence + exactly one correctly-dated
    # heading — never a judgement on the entry's prose. Disk-only like every other group:
    # no git, so this deliberately does NOT check that every tag has an entry.
    changelog = root / "CHANGELOG.md"
    if not changelog.is_file():
        failures.append(f"CHANGELOG.md missing — no entry for --expect-version {expect}")
    else:
        pattern = rf"^## v{re.escape(expect)} — \d{{4}}-\d{{2}}-\d{{2}}$"
        n = len(re.findall(pattern, changelog.read_text(encoding="utf-8"), re.M))
        if n == 0:
            failures.append(f"CHANGELOG.md has no '## v{expect} — YYYY-MM-DD' entry")
        elif n > 1:
            failures.append(f"CHANGELOG.md has {n} entries for v{expect} — expected exactly one")
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


def _is_asset_node(consumer: str) -> bool:
    """Shared predicate (E1/E5): a convention consumers: entry ending .js is a
    workflow-asset node — it resolves against skills/vlt-setup/assets/workflows/
    and E5 owns its leg of the bipartite comparison; E1 skips it."""
    return str(consumer).endswith(".js")


def _e1_handshake(conventions: dict, acks: dict, skill_dirs: set) -> list:
    """E1: convention consumers: <-> consumer depends_on: pins, both directions.

    Derives the answer from BOTH sides of the handshake and compares — retiring
    the self-confirming `grep "<name>@"` every arc-3 build wrote by hand (which
    searched for the ack string it had just written). Vocabulary matches
    vlt-lint:131 so the dev-side and vault-side homes read alike. Skips
    consumers: entries ending .js — workflow-asset nodes, whose leg E5 owns
    (the shared predicate _is_asset_node, stated in both docstrings).
    """
    failures = []
    for conv, (version, consumers) in conventions.items():
        for consumer in consumers:
            if _is_asset_node(consumer):
                continue  # E5 owns the asset leg
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
    """E3: a name@version pin token in a SKILL.md or references/*.md body
    (outside depends_on:).

    The pin token is the strongest machine-detectable signal of convention
    consumption — you write it only to pin. It legitimately lives only in a
    skill's depends_on:; anywhere else it is a near-certain de-facto-consumption
    tell with near-zero false positives. Anchored on the known convention names
    (not a bare \\w+@\\d+) so an email address or unrelated foo@2 cannot trip it.
    Scope (B5-8): SKILL.md plus skills/vlt-*/references/*.md — the re-cut moved
    mechanics into reference files, which would otherwise exit this coverage;
    deliberately NOT a blanket **/*.md (vlt-setup/assets/** is installable
    payload with its own vault-side jurisdiction).
    """
    failures = []
    if not conv_names:
        return failures
    pattern = re.compile(r"\b(" + "|".join(re.escape(n) for n in sorted(conv_names)) + r")@(\d+)\b")
    targets = sorted(root.glob("skills/vlt-*/SKILL.md")) + sorted(root.glob("skills/vlt-*/references/*.md"))
    for p in targets:
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


WORKFLOWS_DIR = "skills/vlt-setup/assets/workflows"
_DEPENDS_ON_LINE_RE = re.compile(r"^\s*//\s*depends_on:\s*(\[.*\])\s*$")
_ASSET_PIN_RE = re.compile(r"^[A-Za-z0-9_-]+@\d+$")


def _e5_asset_nodes(root: Path, conventions: dict) -> list:
    """E5 (build B7-6): workflow assets are first-class handshake nodes.

    Structural on both sides, never an enumeration. (a) Presence: every
    skills/vlt-setup/assets/workflows/*.js MUST carry exactly one
    `// depends_on: [...]` header line parsing as flat "name@version" pins
    (or []) — a missing or unparseable line FAILs; absence must be loud,
    the named-node state is the deliverable. (b) Bipartite, both directions,
    E1's vocabulary: every convention consumers: entry ending .js (the
    shared predicate _is_asset_node — E1 skips these, E5 owns them) must
    resolve to an existing workflow file whose header acks that convention
    at the current version (dangling / unacknowledged / stale); every
    non-empty pin in a workflow header must appear in that convention's
    consumers: (an asset consuming unlisted is the reverse drift).
    """
    failures = []
    wf_dir = root / WORKFLOWS_DIR
    asset_pins = {}  # filename -> {conv_name: version_str}
    for wf in sorted(wf_dir.glob("*.js")) if wf_dir.is_dir() else []:
        rel = wf.relative_to(root)
        matches = [
            m for line in wf.read_text(encoding="utf-8").splitlines()
            for m in [_DEPENDS_ON_LINE_RE.match(line)] if m
        ]
        if len(matches) != 1:
            failures.append(
                f"asset node: {rel} carries {len(matches)} `// depends_on: [...]` header "
                f"lines — every shipped workflow must carry exactly one ([] if it reads "
                f"no conventions); absence must be loud"
            )
            continue
        try:
            raw = json.loads(matches[0].group(1))
            assert isinstance(raw, list) and all(
                isinstance(p, str) and _ASSET_PIN_RE.match(p) for p in raw
            )
        except Exception:
            failures.append(
                f"asset node: {rel} depends_on header does not parse as flat "
                f'["name@version"] pins: {matches[0].group(1)}'
            )
            continue
        pins = {}
        for p in raw:
            name, _, ver = p.partition("@")
            pins[name] = ver
        asset_pins[wf.name] = pins

    for conv, (version, consumers) in sorted(conventions.items()):
        for consumer in consumers:
            if not _is_asset_node(consumer):
                continue  # skill consumers are E1's leg
            if consumer not in asset_pins:
                failures.append(
                    f"stale/dangling — {conv}@{version} lists asset {consumer} but "
                    f"{WORKFLOWS_DIR}/{consumer} does not exist (or its header failed to parse)"
                )
                continue
            pinned = asset_pins[consumer].get(conv)
            if pinned is None:
                failures.append(
                    f"unacknowledged — asset {consumer} is a listed consumer of "
                    f"{conv}@{version} but its depends_on header does not ack it"
                )
            elif pinned != version:
                failures.append(f"stale — asset {consumer} acks {conv}@{pinned} but convention is @{version}")

    for fname, pins in sorted(asset_pins.items()):
        for conv, ver in sorted(pins.items()):
            if conv not in conventions:
                failures.append(
                    f"asset node: {fname} acks unknown convention {conv}@{ver} "
                    f"(no such convention in the shipped bundle)"
                )
            elif fname not in conventions[conv][1]:
                failures.append(
                    f"asset node: {fname} acks {conv}@{ver} but {conv}'s consumers: does "
                    f"not list it — an asset consuming unlisted is the reverse drift"
                )
    return failures


# E4 (build B7-1, standing rule R2): the gate-check inventory is structural —
# every module-level callable whose name matches this pattern IS a gate check,
# so a new check enters the inventory the moment it is defined, with no
# registry to forget.
_E4_CHECK_NAME_RE = re.compile(r"^(check_|_e\d+_)")


def _e4_harness_coverage(inventory=None, coverage=None) -> list:
    """E4 (build B7-1, standing rule R2): harness coverage — the gate proves
    its own checks can fail.

    A rule observed passing only on the artifact it was authored from is not
    yet tested (A7-1). Derives the check inventory by introspecting this
    module's own callables (^check_ / ^_e\\d+_ — never a hand-kept list) and
    reads the harness's COVERAGE map (imported from
    tools/test-package-lint.py, the load_canonical_header idiom — single
    source, never a copy). Any inventoried check with no covering case FAILs;
    a missing/unimportable harness FAILs loudly, never skips. Binds the gate's
    OWN repo, invariant of --root: fixture trees have no tools/, and every
    fixture subprocess run therefore also exercises E4 against the real repo.
    The inventory/coverage parameters exist so the harness's own E4 case can
    exercise the failure path in-process with a fabricated hole.
    """
    if inventory is None:
        inventory = sorted(
            name for name, obj in globals().items()
            if callable(obj) and _E4_CHECK_NAME_RE.match(name)
        )
    if coverage is None:
        harness = Path(__file__).resolve().parent / "test-package-lint.py"
        if not harness.is_file():
            return [
                "harness coverage: tools/test-package-lint.py is missing — the gate's "
                "checks cannot be proven able to fail (R2; absence must be loud)"
            ]
        try:
            spec = importlib.util.spec_from_file_location("test_package_lint", harness)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            coverage = dict(mod.COVERAGE)
        except Exception as e:
            return [f"harness coverage: cannot import tools/test-package-lint.py: {e} (R2; absence must be loud)"]
    return [
        f"harness coverage: {name} has no fixture case that can fail it "
        f"(R2 — extend tools/test-package-lint.py in the same build)"
        for name in inventory
        if not coverage.get(name)
    ]


SCHEMA_SIZE_BUDGET = 3700  # serialized JSON.stringify(schema).length ceiling per fan-out schema

# The measure MUST reproduce the runtime's own JSON.stringify(schema).length — a
# source-literal char count is the wrong number (the 4,266 source literal serializes
# to 4,100). A node subprocess evals every top-level `const NAME = {…}` object literal
# in a workflow asset and, for those that are output schemas (type:'object' with
# properties — discovered structurally, never a hand-kept list), prints its serialized
# length. A literal that textually looks like a schema but fails to eval is reported as
# an error (absence must be loud), never silently skipped.
_E6_NODE_EXTRACTOR = r"""
const fs = require('fs');
const src = fs.readFileSync(process.argv[1], 'utf8');
const out = [];
const re = /(?:^|\n)\s*const\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*\{/g;
let m;
while ((m = re.exec(src))) {
  const name = m[1];
  let start = src.indexOf('{', m.index);
  let depth = 0, j = start, inStr = null, inLine = false, inBlock = false;
  for (; j < src.length; j++) {
    const c = src[j], c2 = src[j + 1];
    if (inStr) { if (c === '\\') { j++; continue; } if (c === inStr) inStr = null; continue; }
    if (inLine) { if (c === '\n') inLine = false; continue; }
    if (inBlock) { if (c === '*' && c2 === '/') { j++; inBlock = false; } continue; }
    if (c === '/' && c2 === '/') { inLine = true; j++; continue; }
    if (c === '/' && c2 === '*') { inBlock = true; j++; continue; }
    if (c === '"' || c === "'" || c === '`') { inStr = c; continue; }
    if (c === '{') depth++;
    else if (c === '}') { depth--; if (depth === 0) { j++; break; } }
  }
  const lit = src.slice(start, j);
  let obj;
  try { obj = eval('(' + lit + ')'); }
  catch (e) { if (/type:\s*['"]object['"]/.test(lit)) out.push({ name, error: String(e) }); continue; }
  if (obj && obj.type === 'object' && obj.properties) out.push({ name, len: JSON.stringify(obj).length });
}
process.stdout.write(JSON.stringify(out));
"""


def _e6_schema_size_budget(root: Path) -> list:
    """E6 (build B10-12): standing schema-size budget — every fan-out output
    schema in every workflow asset serializes to JSON.stringify length within
    SCHEMA_SIZE_BUDGET. The margin device that stops a description from silently
    re-crossing the harness classifier's output-schema ceiling (the v0.13.0
    non-executable-full-lint failure). Workflow-agnostic: the same check covers
    the vlt-review-council and vlt-consult schemas, so a future council/consult
    schema crossing the ceiling is caught regardless of any per-build decline.
    """
    failures = []
    wf_dir = root / WORKFLOWS_DIR
    if not wf_dir.is_dir():
        return failures
    node = shutil.which("node")
    if not node:
        return [
            "schema-size budget: node is not on PATH — the serialized "
            "JSON.stringify(schema).length cannot be measured faithfully (R2; absence must be loud)"
        ]
    for wf in sorted(wf_dir.glob("*.js")):
        rel = wf.relative_to(root)
        try:
            proc = subprocess.run(
                [node, "-e", _E6_NODE_EXTRACTOR, str(wf)],
                capture_output=True, text=True, timeout=30,
            )
        except Exception as e:
            failures.append(f"schema-size budget: could not run node over {rel}: {e}")
            continue
        if proc.returncode != 0:
            failures.append(
                f"schema-size budget: node failed extracting schemas from {rel}: "
                f"{(proc.stderr or proc.stdout).strip()[:300]}"
            )
            continue
        try:
            schemas = json.loads(proc.stdout or "[]")
        except Exception as e:
            failures.append(f"schema-size budget: unparseable extractor output for {rel}: {e}")
            continue
        for s in schemas:
            if "error" in s:
                failures.append(
                    f"schema-size budget: {rel} schema {s['name']} looks like an output schema "
                    f"but could not be evaluated to measure it: {s['error']}"
                )
            elif s.get("len", 0) > SCHEMA_SIZE_BUDGET:
                failures.append(
                    f"schema-size budget: {rel} schema {s['name']} serializes to {s['len']} chars "
                    f"(> {SCHEMA_SIZE_BUDGET}) — trim descriptions or migrate schema-only semantics "
                    f"into the prompt (the harness rejects an over-ceiling output schema pre-read)"
                )
    return failures


def check_group_e(root: Path) -> list:
    """Self-description integrity: E1 handshake-bipartite, E2 structure-map SSoT,
    E3 stray-pin, E4 harness-coverage (B7-1/R2), E5 asset-node handshake (B7-6),
    E6 schema-size budget (B10-12).

    Aggregates the failure lists. Each check derives truth from the authoritative
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
        + _e4_harness_coverage()
        + _e5_asset_nodes(root, conventions)
        + _e6_schema_size_budget(root)
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
        results["D"] = (f"tag intent ({args.expect_version})", check_group_d(args.expect_version, versions, root))
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
