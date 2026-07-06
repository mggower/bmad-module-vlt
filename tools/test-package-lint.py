#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Negative-test harness for tools/package-lint.py (build-14).

Builds a minimal synthetic fixture tree with the shipped-surface shape, seeds
one defect per case, and asserts the lint fails in the right group. Runs the
lint exactly as release time does (`uv run tools/package-lint.py`), so the
PEP 723 + pyyaml path is exercised too.

Usage: uv run tools/test-package-lint.py
Exit: 0 = all cases green; non-zero otherwise.
"""

import json
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


def build_fixture(root: Path) -> None:
    """Minimal synthetic tree with the same shape as the shipped surface."""
    scripts = root / "skills/vlt-setup/scripts"
    assets = root / "skills/vlt-setup/assets"
    (assets / "governance/_meta").mkdir(parents=True)
    scripts.mkdir(parents=True)
    (root / "skills/vlt-mint").mkdir(parents=True)
    (root / ".claude-plugin").mkdir()

    # HEADER's single source: the real merge script, copied into the fixture.
    shutil.copy(REPO / "skills/vlt-setup/scripts/merge-help-csv.py", scripts)

    import importlib.util
    spec = importlib.util.spec_from_file_location("mhc", scripts / "merge-help-csv.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    header_line = ",".join(mod.HEADER)
    (assets / "module-help.csv").write_text(
        "\n".join([header_line] + CSV_ROWS) + "\n", encoding="utf-8"
    )

    (assets / "governance/_meta/vault-operating-contract.md").write_text(
        "# contract\n", encoding="utf-8"
    )
    (assets / "module.yaml").write_text(
        'code: vlt\nname: "Vault"\nmodule_version: 9.9.9\n', encoding="utf-8"
    )
    (root / "skills/vlt-mint/SKILL.md").write_text("# vlt-mint\n", encoding="utf-8")
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


CASES = []


def case(name):
    def register(fn):
        CASES.append((name, fn))
        return fn
    return register


@case("1. clean tree -> exit 0, all groups PASS")
def case_clean(root):
    r = run_lint(root)
    assert r.returncode == 0, r.stdout + r.stderr
    for g in "ABC":
        assert f"PASS group {g}" in r.stdout, r.stdout
    assert "SKIPPED group D" in r.stdout, r.stdout


@case("2. stray .decision-log.md under skills/vlt-mint/ -> A fails")
def case_cruft(root):
    (root / "skills/vlt-mint/.decision-log.md").write_text("cruft\n")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group A" in r.stdout, r.stdout


@case("3. legacy after,before header -> B fails")
def case_legacy_header(root):
    edit(root / "skills/vlt-setup/assets/module-help.csv",
         "preceded-by,followed-by", "after,before")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group B" in r.stdout, r.stdout


@case("4. unquoted description containing a comma -> B fails")
def case_unquoted_comma(root):
    edit(root / "skills/vlt-setup/assets/module-help.csv",
         '"Install or update, durably."', "Install or update, durably.")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group B" in r.stdout, r.stdout


@case("5. malformed row (wrong column count) -> B fails")
def case_malformed_row(root):
    csv_path = root / "skills/vlt-setup/assets/module-help.csv"
    csv_path.write_text(
        csv_path.read_text(encoding="utf-8") + "Vault,vlt-broken,short,row\n",
        encoding="utf-8",
    )
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group B" in r.stdout, r.stdout


@case("6. version mismatch module.yaml vs marketplace.json -> C fails")
def case_version_mismatch(root):
    edit(root / "skills/vlt-setup/assets/module.yaml",
         "module_version: 9.9.9", "module_version: 8.8.8")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout


@case("7. --expect-version mismatch on a clean tree -> D fails")
def case_expect_version(root):
    r = run_lint(root, "--expect-version", "1.2.3")
    assert r.returncode != 0 and "FAIL group D" in r.stdout, r.stdout
    for g in "ABC":
        assert f"PASS group {g}" in r.stdout, r.stdout


@case("8. skills[] entry removed from marketplace.json -> C fails")
def case_c5_unlisted_dir(root):
    mkt_path = root / ".claude-plugin/marketplace.json"
    mkt = json.loads(mkt_path.read_text(encoding="utf-8"))
    mkt["plugins"][0]["skills"].remove("./skills/vlt-mint")
    mkt_path.write_text(json.dumps(mkt, indent=2), encoding="utf-8")
    r = run_lint(root)
    assert r.returncode != 0 and "FAIL group C" in r.stdout, r.stdout


def main():
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
