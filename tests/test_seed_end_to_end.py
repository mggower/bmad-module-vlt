import hashlib
import json
import re
import shutil
import subprocess
import sys

import pytest

from conftest import REPO, git, run_kits

KITS = REPO / "kits"
FIXTURE = REPO / "tests" / "fixtures" / "vault-0.19"
NAMED = ("vlt-research", "vlt-ingest", "vlt-query", "vlt-feedback")


def checks(vault):
    return subprocess.run([sys.executable, str(vault / "_agent/tools/checks/run.py")],
                          capture_output=True, text=True, cwd="/")


@pytest.fixture
def fresh(vault):
    r = run_kits(vault, KITS, "seed")
    assert r.returncode == 0, r.stderr
    return vault


@pytest.fixture
def old(tmp_path):
    v = tmp_path / "old"
    shutil.copytree(FIXTURE, v)
    git(v, "init", "-q")
    git(v, "add", "-A")
    git(v, "commit", "-q", "-m", "0.19")
    return v


def hashes(root):
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob("*") if p.is_file() and ".git/" not in p.as_posix()}


def test_fresh_vault_passes_every_check(fresh):
    r = checks(fresh)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "ok   wiki" in r.stdout


def test_every_seeded_skill_points_at_an_existing_playbook(fresh):
    for name in NAMED:
        text = (fresh / ".claude/skills" / name / "SKILL.md").read_text()
        named = re.findall(r"`(resources/playbooks/[a-z-]+\.md)`", text)
        assert len(named) == 1, name
        assert (fresh / named[0]).is_file(), named[0]


def test_every_playbook_companion_path_exists(fresh):
    for path in (fresh / "resources/playbooks").glob("*.md"):
        m = re.search(r"^companion: (.+)$", path.read_text(), re.M)
        if m:
            assert (fresh / m.group(1).strip()).is_file(), f"{path.name} -> {m.group(1)}"


def test_no_file_ships_in_two_kits():
    from kits import kit_files
    assert len(kit_files(KITS)) > 20      # raises Stop on a duplicate


def test_lock_lists_all_four_kits(fresh):
    lock = json.loads((fresh / "_agent/kits.lock").read_text())
    assert sorted(lock["kits"]) == ["core", "research", "task-board", "wiki"]
    assert all(k["version"] == "1.0.0" for k in lock["kits"].values())


def test_seed_into_0_19_vault_changes_no_existing_file(old):
    before = hashes(old)
    r = run_kits(old, KITS, "seed")
    assert r.returncode == 0, r.stderr
    after = hashes(old)
    assert {k: after[k] for k in before} == before
    out = r.stdout.splitlines()
    assert "kept-yours CLAUDE.md" in out
    assert "kept-yours .claude/skills/vlt-ingest/SKILL.md" in out
    assert "seeded _meta/vault.md" in out


def test_checks_run_in_a_seeded_0_19_vault(old):
    run_kits(old, KITS, "seed")
    r = checks(old)
    assert "Traceback" not in r.stdout + r.stderr
    assert r.stdout.strip().splitlines()[-1].startswith("3 checks")
    # the 0.19 wiki page carries its attestation keys, so the stand-in vault is clean
    assert r.returncode == 0, r.stdout


def test_status_is_all_unchanged_after_a_fresh_seed(fresh):
    r = run_kits(fresh, KITS, "status")
    assert r.returncode == 0
    assert {line.split()[0] for line in r.stdout.splitlines()} == {"unchanged"}


# --- final-review fixes

def test_docs_tell_a_0_x_vault_how_to_reach_the_plugin_setup():
    for name in ("README.md", "COMING-FROM-0.x.md"):
        text = (REPO / name).read_text()
        assert "/vlt:vlt-setup" in text, name
    assert "/vlt:vlt-setup" in (REPO / "skills/vlt-setup/SKILL.md").read_text()


def test_review_default_tells_the_writer_to_set_the_key(fresh):
    schema = (fresh / "_meta/frontmatter.md").read_text()
    assert "sets `review: requested` on each document it writes there" in schema
    assert "review: requested" in (fresh / "_agent/templates/zone-readme.md").read_text().split("## Writing here")[1]


def test_pull_skill_says_to_restore_a_missing_lock():
    assert "git checkout -- _agent/kits.lock" in (REPO / "skills/vlt-pull/SKILL.md").read_text()
