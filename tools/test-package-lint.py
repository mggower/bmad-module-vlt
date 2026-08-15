#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""Negative-test harness for tools/package-lint.py (build-14; baseline repaired
and made load-bearing by B7-1).

Builds a minimal synthetic fixture tree with the shipped-surface shape, seeds
one defect per case, and asserts the lint fails in the right group. Runs the
lint exactly as release time does (`uv run tools/package-lint.py`), so the
PEP 723 + pyyaml path is exercised too. (pyyaml is a dependency here only for
the one in-process E4 case, which imports package-lint.py directly.)

Standing rule R2 (Arc 7): every gate check must have a case that can make it
fail. Each case declares `covers=` — the package-lint check callables it can
turn red — and the aggregate COVERAGE map is imported by package-lint's E4,
which fails any inventoried check with no covering case. CASE_FLOOR is the
count shrink net: deleting a case without a deliberate floor edit fails loudly.

Usage: uv run tools/test-package-lint.py
Exit: 0 = all cases green; non-zero otherwise.
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# The fixture-build imports merge-help-csv.py; don't seed __pycache__ into the
# clean fixture (group A would trip on the harness's own bytecode).
sys.dont_write_bytecode = True

REPO = Path(__file__).resolve().parent.parent
LINT = REPO / "tools/package-lint.py"

CSV_ROWS = [
    'Vault,vlt-setup,"Setup Vault",SU,"Install or update, durably.",configure,"{-H: headless}",anytime,,,true,{project-root},"config files installed"',
    'Vault,vlt-mint,"Mint the Cast",MN,"Grow the roster.",mint,"{kind: operation | partner}",anytime,,,false,{project-root},"a new vlt-* skill"',
]

# B7-1, structural doctrine (first application): the fixture's structure map is
# written ONCE here and rendered into both of its homes (module.yaml
# vault_structure.default and the contract's pipe table) — never transcribed by
# hand. Must include tripwires + lint_reports: C8(d) hard-requires both rows.
FIXTURE_STRUCTURE = {
    "wiki": "_agent/wiki/",
    "log": "_agent/log.md",
    "tripwires": "_agent/tripwires.yaml",
    "lint_reports": "_agent/lint-reports/",
}


def build_fixture(root: Path) -> None:
    """Minimal synthetic tree with the same shape as the shipped surface.

    A clean fixture passes every group (B7-1): the four A7-1 seeds (structure
    map, rule-card, vitals reader, tripwires) plus the R2 seeds a coverable
    C7/E1/E3 need (a routed reference, one convention, its consumer's ack).
    """
    scripts = root / "skills/vlt-setup/scripts"
    assets = root / "skills/vlt-setup/assets"
    (assets / "governance/_meta/conventions").mkdir(parents=True)
    (assets / "hooks").mkdir(parents=True)
    scripts.mkdir(parents=True)
    (root / "skills/vlt-mint/references").mkdir(parents=True)
    (root / ".claude-plugin").mkdir()

    # HEADER's single source: the real merge script, copied into the fixture.
    shutil.copy(REPO / "skills/vlt-setup/scripts/merge-help-csv.py", scripts)

    # C9 (build B7-2): the real durability-net scripts — real, never stubs, so
    # the clean-tree baselines exercise the true code paths (the merge-help-csv
    # precedent). Cases 19/20 swap in destructive stubs to prove C9 can fail.
    shutil.copy(REPO / "skills/vlt-setup/scripts/merge-config.py", scripts)
    shutil.copy(REPO / "skills/vlt-setup/scripts/verify-skill-manifest.py", scripts)

    import importlib.util
    spec = importlib.util.spec_from_file_location("mhc", scripts / "merge-help-csv.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    header_line = ",".join(mod.HEADER)
    (assets / "module-help.csv").write_text(
        "\n".join([header_line] + CSV_ROWS) + "\n", encoding="utf-8"
    )

    # Contract with the structure-map table rendered from FIXTURE_STRUCTURE
    # (E2 anchors on the exact heading; rows are backtick-celled).
    table_rows = "\n".join(
        f"| `{key}` | `{path}` | fixture zone |" for key, path in FIXTURE_STRUCTURE.items()
    )
    contract_path = assets / "governance/_meta/vault-operating-contract.md"
    contract_path.write_text(
        "# contract\n\n"
        "## Path resolution — the structure map\n\n"
        "| logical | path | note |\n"
        "| --- | --- | --- |\n"
        f"{table_rows}\n",
        encoding="utf-8",
    )

    # Rule-card (C6): derived_from sha256 computed over the FINAL contract
    # bytes at fixture-build time — never a hard-coded digest.
    digest = hashlib.sha256(contract_path.read_bytes()).hexdigest()
    (assets / "governance/_meta/vault-rule-card.md").write_text(
        "---\n"
        f"derived_from: 'vault-operating-contract.md sha256:{digest} (derived fixture)'\n"
        "---\n\n# fixture rule-card\n",
        encoding="utf-8",
    )

    # module.yaml with vault_structure.default rendered from FIXTURE_STRUCTURE.
    structure_yaml = "\n".join(f"    {key}: {path}" for key, path in FIXTURE_STRUCTURE.items())
    (assets / "module.yaml").write_text(
        'code: vlt\nname: "Vault"\nmodule_version: 9.9.9\n'
        f"vault_structure:\n  default:\n{structure_yaml}\n",
        encoding="utf-8",
    )

    # Vitals reader (C8 a–c): minimal but real — compiles, non-empty METRICS,
    # WIRE_REQUIRED_FIELDS as the real seven-field list (imported by the lint).
    (assets / "hooks/vlt-vitals.py").write_text(
        'METRICS = {"ingests_since_lint": "fixture metric"}\n'
        'WIRE_REQUIRED_FIELDS = ["id", "metric", "threshold", "owner", "moment", '
        '"surface_text", "review_after"]\n',
        encoding="utf-8",
    )

    # Tripwires seed (C8 a–b): one wire, all seven required fields, metric
    # naming the fixture METRICS id.
    (assets / "tripwires.yaml").write_text(
        "wires:\n"
        "  - id: fixture-wire\n"
        "    metric: ingests_since_lint\n"
        '    threshold: ">= 10"\n'
        "    owner: fixture\n"
        "    moment: fixture moment\n"
        '    surface_text: "fixture surface"\n'
        "    review_after: 2099-01-01\n",
        encoding="utf-8",
    )

    # One convention + ack (E1/E3): bipartite-consistent clean.
    (assets / "governance/_meta/conventions/testconv.md").write_text(
        "---\nversion: 1\nconsumers: [vlt-mint]\n---\n\n# testconv\n",
        encoding="utf-8",
    )

    # vlt-mint: acks the convention; routes to its one reference (C7 clean).
    (root / "skills/vlt-mint/SKILL.md").write_text(
        '---\ndepends_on: ["testconv@1"]\n---\n\n# vlt-mint\n\n'
        "Mechanics live in references/how.md.\n",
        encoding="utf-8",
    )
    (root / "skills/vlt-mint/references/how.md").write_text(
        "# how\n\nFixture mechanics.\n", encoding="utf-8"
    )

    # Group D's third artifact (build B6-1): a valid entry for the fixture's version.
    (root / "CHANGELOG.md").write_text(
        "# Changelog\n\n## v9.9.9 — 2026-01-01\n\n**Arc 9** — the fixture arc.\n",
        encoding="utf-8",
    )
    (root / ".claude-plugin/marketplace.json").write_text(
        json.dumps(
            {
                "name": "vlt",
                "plugins": [
                    {
                        "name": "vlt",
                        "version": "9.9.9",
                        "skills": ["./skills/vlt-setup", "./skills/vlt-mint"],
                    }
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def run_lint(root: Path, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["uv", "run", str(LINT), "--root", str(root), *extra],
        capture_output=True,
        text=True,
    )


def edit(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    assert old in text, f"fixture edit target not found in {path}: {old!r}"
    path.write_text(text.replace(old, new), encoding="utf-8")


def rederive_card(root: Path) -> None:
    """Rewrite the fixture rule-card's sha256 from the contract's current bytes
    (for cases that edit the contract but are NOT testing C6)."""
    contract = root / "skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md"
    card = root / "skills/vlt-setup/assets/governance/_meta/vault-rule-card.md"
    digest = hashlib.sha256(contract.read_bytes()).hexdigest()
    card.write_text(
        re.sub(r"sha256:[0-9a-f]{64}", f"sha256:{digest}", card.read_text(encoding="utf-8")),
        encoding="utf-8",
    )


CASES = []
COVERAGE = {}  # package-lint check name -> [case names]; E4's data source (R2)

# R2 shrink net: a net that must carry a list carries a shrink check. Bump the
# floor in the same edit that adds cases (ratchet); main() fails loudly when
# the registered count drops below it. Per-check shrink is E4's jurisdiction.
CASE_FLOOR = 20


def case(name, *, covers):
    """Register a case. `covers` (required) names the package-lint check
    callables this case can make fail — empty only for the whole-run baselines
    (cases 1 and 9), whose job is the clean-tree exit-0 assertion (B7-1 pick,
    recorded: baselines carry covers=() rather than claiming every check)."""
    def register(fn):
        CASES.append((name, fn))
        for check in covers:
            COVERAGE.setdefault(check, []).append(name)
        return fn
    return register


@case("1. clean tree -> exit 0, PASS A/B/C/E, SKIPPED D", covers=())
def case_clean(root):
    r = run_lint(root)
    assert r.returncode == 0, r.stdout + r.stderr
    for g in "ABCE":
        assert f"PASS group {g}" in r.stdout, r.stdout
    assert "SKIPPED group D" in r.stdout, r.stdout


@case("2. stray .decision-log.md under skills/vlt-mint/ -> A fails",
      covers=("check_group_a",))
def case_cruft(root):
    (root / "skills/vlt-mint/.decision-log.md").write_text("cruft\n")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group A" in r.stdout, r.stdout


@case("3. legacy after,before header -> B fails", covers=("check_group_b",))
def case_legacy_header(root):
    edit(root / "skills/vlt-setup/assets/module-help.csv",
         "preceded-by,followed-by", "after,before")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group B" in r.stdout, r.stdout


@case("4. unquoted description containing a comma -> B fails",
      covers=("check_group_b",))
def case_unquoted_comma(root):
    edit(root / "skills/vlt-setup/assets/module-help.csv",
         '"Install or update, durably."', "Install or update, durably.")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group B" in r.stdout, r.stdout


@case("5. malformed row (wrong column count) -> B fails", covers=("check_group_b",))
def case_malformed_row(root):
    csv_path = root / "skills/vlt-setup/assets/module-help.csv"
    csv_path.write_text(
        csv_path.read_text(encoding="utf-8") + "Vault,vlt-broken,short,row\n",
        encoding="utf-8",
    )
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group B" in r.stdout, r.stdout


@case("6. version mismatch module.yaml vs marketplace.json -> C fails",
      covers=("check_group_c",))
def case_version_mismatch(root):
    edit(root / "skills/vlt-setup/assets/module.yaml",
         "module_version: 9.9.9", "module_version: 8.8.8")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout


@case("7. --expect-version mismatch on a clean tree -> D fails, A/B/C/E pass",
      covers=("check_group_d",))
def case_expect_version(root):
    r = run_lint(root, "--expect-version", "1.2.3")
    assert r.returncode != 0 and "FAIL group D" in r.stdout, r.stdout
    for g in "ABCE":
        assert f"PASS group {g}" in r.stdout, r.stdout


@case("8. skills[] entry removed from marketplace.json -> C fails",
      covers=("check_group_c",))
def case_c5_unlisted_dir(root):
    mkt_path = root / ".claude-plugin/marketplace.json"
    mkt = json.loads(mkt_path.read_text(encoding="utf-8"))
    mkt["plugins"][0]["skills"].remove("./skills/vlt-mint")
    mkt_path.write_text(json.dumps(mkt, indent=2), encoding="utf-8")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout


@case("9. --expect-version matching a clean tree -> exit 0, D passes",
      covers=())
def case_d_positive(root):
    # Load-bearing D-active baseline (A7-1/B7-1): the fixture now satisfies
    # every group, so whole-run exit 0 is asserted deliberately — a new gate
    # check with no fixture seed turns this case red loudly.
    r = run_lint(root, "--expect-version", "9.9.9")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "PASS group D" in r.stdout, r.stdout


@case("10. CHANGELOG.md entry for a different version -> D fails naming CHANGELOG.md",
      covers=("check_group_d",))
def case_d_wrong_entry(root):
    edit(root / "CHANGELOG.md", "## v9.9.9 — ", "## v9.9.8 — ")
    r = run_lint(root, "--expect-version", "9.9.9")
    assert r.returncode != 0 and "FAIL group D" in r.stdout, r.stdout
    assert "CHANGELOG.md" in r.stdout, r.stdout


@case("11. duplicated CHANGELOG.md entry for the expected version -> D fails",
      covers=("check_group_d",))
def case_d_duplicate_entry(root):
    path = root / "CHANGELOG.md"
    path.write_text(
        path.read_text(encoding="utf-8") + "\n## v9.9.9 — 2026-01-02\n\nsecond block\n",
        encoding="utf-8",
    )
    r = run_lint(root, "--expect-version", "9.9.9")
    assert r.returncode != 0 and "FAIL group D" in r.stdout, r.stdout


@case("12. contract edited without re-deriving the rule-card -> C fails, stale",
      covers=("check_rule_card",))
def case_c6_stale_card(root):
    contract = root / "skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md"
    contract.write_text(contract.read_text(encoding="utf-8") + "\ncorrupted\n",
                        encoding="utf-8")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout
    assert "rule-card stale" in r.stdout, r.stdout


@case("13. router names a reference that does not exist -> C fails, dangling route",
      covers=("check_router_integrity",))
def case_c7_dangling_route(root):
    # (The orphaned how.md this edit also creates is a legitimate co-failure;
    # the assertion targets the dangling-route string.)
    edit(root / "skills/vlt-mint/SKILL.md",
         "references/how.md", "references/missing.md")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout
    assert "dangling route" in r.stdout, r.stdout


@case("14. seed wire names an unknown metric id -> C fails, enforcement kit",
      covers=("check_enforcement_kit",))
def case_c8_unknown_metric(root):
    edit(root / "skills/vlt-setup/assets/tripwires.yaml",
         "metric: ingests_since_lint", "metric: bogus_metric")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout
    assert "not in vlt-vitals.py's canonical table" in r.stdout, r.stdout


@case("15. consumer's depends_on ack removed -> E fails, unacknowledged",
      covers=("_e1_handshake", "check_group_e"))
def case_e1_unacked(root):
    edit(root / "skills/vlt-mint/SKILL.md",
         'depends_on: ["testconv@1"]', "depends_on: []")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group E" in r.stdout, r.stdout
    assert "unacknowledged" in r.stdout, r.stdout


@case("16. contract table path cell drifts from module.yaml -> E fails, structure map",
      covers=("_e2_structure_map",))
def case_e2_table_drift(root):
    # Builder's pick (recorded): re-derive the card digest after the edit so
    # C6 stays green and the failure isolates to E2.
    edit(root / "skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md",
         "| `wiki` | `_agent/wiki/` |", "| `wiki` | `_agent/wiki2/` |")
    rederive_card(root)
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group E" in r.stdout, r.stdout
    assert "structure map:" in r.stdout, r.stdout


@case("17. reference body recites a pin outside depends_on -> E fails, stray pin",
      covers=("_e3_stray_pin",))
def case_e3_stray_pin(root):
    path = root / "skills/vlt-mint/references/how.md"
    path.write_text(
        path.read_text(encoding="utf-8") + "\nPer testconv@1, do the fixture thing.\n",
        encoding="utf-8",
    )
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group E" in r.stdout, r.stdout
    assert "stray pin" in r.stdout, r.stdout


@case("18. E4 in-process: fabricated inventory with an uncovered check -> failure string",
      covers=("_e4_harness_coverage",))
def case_e4_self(root):
    # E4 covers itself (B7-1 disposition 4): not by self-exclusion but by an
    # in-process call against a fabricated inventory/coverage pair with a
    # known hole — cheap, deterministic, and it can fail.
    import importlib.util
    spec = importlib.util.spec_from_file_location("package_lint_e4", LINT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    failures = mod._e4_harness_coverage(
        inventory=["check_fixture_probe"], coverage={}
    )
    assert any(
        "check_fixture_probe" in f and "no fixture case" in f for f in failures
    ), failures


@case("19. merge-config swapped for a rebuild-from-answers stub -> C fails, preservation",
      covers=("check_durability_nets",))
def case_c9_destructive_merge(root):
    # The pre-B7-2 behavior, reproduced deterministically: delete the module
    # section, rebuild from answers alone, return config only (no report).
    (root / "skills/vlt-setup/scripts/merge-config.py").write_text(
        "def merge_config(existing_config, module_yaml, answers, verbose=False):\n"
        "    config = dict(existing_config)\n"
        "    code = module_yaml['code']\n"
        "    config.pop(code, None)\n"
        "    section = {'name': module_yaml.get('name')}\n"
        "    section.update(answers.get('module', {}))\n"
        "    config[code] = section\n"
        "    return config\n",
        encoding="utf-8",
    )
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout
    assert "durability net (merge-config)" in r.stdout, r.stdout


@case("20. manifest script swapped for a references/-dropping enumeration stub -> C fails naming the path",
      covers=("check_durability_nets",))
def case_c9_manifest_enumeration(root):
    # The A7-3 regression shape: a walk that filters references/ back out.
    (root / "skills/vlt-setup/scripts/verify-skill-manifest.py").write_text(
        "import hashlib\n"
        "def compute_manifest(root, live_skills_dir, source_skills_dir):\n"
        "    entries = {}\n"
        "    for d in source_skills_dir.glob('vlt-*'):\n"
        "        for f in (live_skills_dir / d.name).rglob('*'):\n"
        "            if f.is_file() and 'references' not in f.parts:\n"
        "                entries[str(f.relative_to(root))] = "
        "hashlib.sha256(f.read_bytes()).hexdigest()\n"
        "    return entries\n",
        encoding="utf-8",
    )
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout
    assert "references/how.md" in r.stdout, r.stdout


def main():
    if len(CASES) < CASE_FLOOR:
        print(
            f"test-package-lint: FAIL — {len(CASES)} registered cases < "
            f"CASE_FLOOR {CASE_FLOOR} (R2 shrink check: a case was removed "
            f"without a deliberate floor edit)"
        )
        sys.exit(1)
    failures = 0
    for name, fn in CASES:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_fixture(root)
            try:
                fn(root)
                print(f"PASS  {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL  {name}\n      {e}")
    total = len(CASES)
    print(f"test-package-lint: {total - failures}/{total} cases green")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
