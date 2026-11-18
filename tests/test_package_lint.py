import json
import shutil
import subprocess
import sys

import pytest

from conftest import REPO, write

LINT = REPO / "tools" / "package-lint.py"
SURFACE = (".claude-plugin", "skills", "kits", "scripts")


@pytest.fixture
def tree(tmp_path):
    """A copy of the shipped surface that a test can damage."""
    root = tmp_path / "repo"
    for name in SURFACE:
        shutil.copytree(REPO / name, root / name, ignore=shutil.ignore_patterns("__pycache__", ".DS_Store"))
    return root


def lint(root, version="1.0.0"):
    return subprocess.run([sys.executable, str(LINT), "--root", str(root), "--expect-version", version],
                          capture_output=True, text=True)


def assert_fails(result, check):
    assert result.returncode == 1, result.stdout + result.stderr
    assert f"[{check}]" in result.stdout
    assert result.stdout.strip().splitlines()[-1].startswith("FAIL:")


def test_real_tree_passes():
    r = subprocess.run([sys.executable, str(LINT), "--expect-version", "1.0.0"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert r.stdout.strip().splitlines()[-1] == "PASS: 8 checks"


def test_copy_passes(tree):
    assert lint(tree).returncode == 0


def test_cruft_fails(tree):
    write(tree / "kits/core/files/_agent/tools/checks/.decision-log.md", "x")
    assert_fails(lint(tree), "cruft")


def test_pycache_fails(tree):
    write(tree / "scripts/__pycache__/kits.cpython-312.pyc", "x")
    assert_fails(lint(tree), "cruft")


def test_wrong_expected_version_fails(tree):
    assert_fails(lint(tree, "1.0.1"), "version")


def test_kit_version_out_of_step_fails(tree):
    p = tree / "kits/wiki/kit.yaml"
    p.write_text(p.read_text().replace("1.0.0", "0.9.0"))
    r = lint(tree)
    assert_fails(r, "version")
    assert "wiki" in r.stdout


def test_skill_missing_from_manifest_fails(tree):
    write(tree / "skills/vlt-extra/SKILL.md", "---\nname: vlt-extra\n---\n")
    assert_fails(lint(tree), "skills")


def test_manifest_skill_without_directory_fails(tree):
    p = tree / ".claude-plugin/marketplace.json"
    data = json.loads(p.read_text())
    data["plugins"][0]["skills"].append("./skills/vlt-ghost")
    p.write_text(json.dumps(data))
    assert_fails(lint(tree), "skills")


def test_path_in_two_kits_fails(tree):
    write(tree / "kits/wiki/files/_meta/vault.md", "dup\n")
    assert_fails(lint(tree), "kits")


def test_rules_over_budget_fails(tree):
    p = tree / "kits/core/files/_meta/vault.md"
    p.write_text(p.read_text() + "\nmore\n" * 60)
    r = lint(tree)
    assert_fails(r, "budget")
    assert "vault.md" in r.stdout


def test_named_skill_over_budget_fails(tree):
    p = tree / "kits/wiki/files/.claude/skills/vlt-ingest/SKILL.md"
    p.write_text(p.read_text() + "\nextra rule\n" * 10)
    assert_fails(lint(tree), "budget")


def test_named_skill_pointing_nowhere_fails(tree):
    p = tree / "kits/research/files/.claude/skills/vlt-research/SKILL.md"
    p.write_text(p.read_text().replace("playbooks/research.md", "playbooks/gone.md"))
    assert_fails(lint(tree), "pointers")


def test_machine_path_fails(tree):
    p = tree / "kits/core/files/_agent/tools/README.md"
    p.write_text(p.read_text() + "\nSee /Users/someone/vault.\n")
    assert_fails(lint(tree), "scrub")


def test_persona_word_fails(tree):
    p = tree / "kits/wiki/files/_meta/wiki.md"
    p.write_text(p.read_text() + "\nAsk the Partner.\n")
    assert_fails(lint(tree), "scrub")


def test_kits_that_fail_their_own_checks_fail(tree):
    (tree / "kits/core/files/_agent/tools/checks/README.md").unlink()
    r = lint(tree)
    assert_fails(r, "seed")
    assert "tool-readmes" in r.stdout


def test_all_checks_reported_together(tree):
    write(tree / "scripts/__pycache__/x.pyc", "x")
    p = tree / "kits/wiki/kit.yaml"
    p.write_text(p.read_text().replace("1.0.0", "0.9.0"))
    r = lint(tree)
    assert "[cruft]" in r.stdout and "[version]" in r.stdout
    assert r.stdout.strip().splitlines()[-1] == "FAIL: 2 of 8"
