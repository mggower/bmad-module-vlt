import shutil
import subprocess
import sys

import pytest

from conftest import REPO, write

INDEX_SRC = REPO / "kits" / "core" / "files" / ".claude" / "skills" / "vlt-playbook" / "index.py"
FOLDER = "resources/playbooks"


def playbook(need="Do the thing", state="live", domain="vault", extra=""):
    return (f"---\ntype: resource\ntitle: Playbook — x\nneed: \"{need}\"\nstate: {state}\n"
            f"domain: {domain}\n{extra}---\n# X\n\n## Procedure\n\n1. Do it.\n")


def companion(parent="a.md"):
    return f"---\ntype: resource\ncompanion_of: {parent}\n---\n# Reference\n"


@pytest.fixture
def pv(tmp_path):
    v = tmp_path / "vault"
    dest = v / ".claude" / "skills" / "vlt-playbook" / "index.py"
    dest.parent.mkdir(parents=True)
    shutil.copy(INDEX_SRC, dest)
    write(v / FOLDER / "README.md", "---\ntype: resource\ndomains: [vault, wiki]\n---\n# Playbooks\n")
    write(v / FOLDER / "a.md", playbook(need="Do the A thing"))
    return v


def run(v, *args):
    return subprocess.run([sys.executable, str(v / ".claude/skills/vlt-playbook/index.py"), *args],
                          capture_output=True, text=True, cwd="/")


def test_table_lists_need_and_path(pv):
    r = run(pv)
    assert r.returncode == 0, r.stderr
    row = [l for l in r.stdout.splitlines() if "Do the A thing" in l]
    assert len(row) == 1
    assert "`resources/playbooks/a.md`" in row[0]
    assert "README" not in r.stdout


def test_dormant_is_marked(pv):
    write(pv / FOLDER / "b.md", playbook(need="Sleepy", state="dormant"))
    row = [l for l in run(pv).stdout.splitlines() if "Sleepy" in l][0]
    assert "dormant" in row


def test_companion_is_appended_not_listed(pv):
    write(pv / FOLDER / "a-reference.md", companion())
    out = run(pv).stdout
    row = [l for l in out.splitlines() if "Do the A thing" in l][0]
    assert "then `a-reference.md`" in row
    assert len([l for l in out.splitlines() if "a-reference.md" in l]) == 1


def test_check_passes_on_clean_folder(pv):
    write(pv / FOLDER / "b.md", playbook(need="B", domain="wiki"))
    write(pv / FOLDER / "a-reference.md", companion())
    r = run(pv, "--check")
    assert r.returncode == 0, r.stdout
    assert r.stdout.strip().splitlines()[-1] == "2 playbooks, 1 companions, 0 problems"


def test_check_fails_on_missing_need(pv):
    write(pv / FOLDER / "b.md", "---\ntype: resource\nstate: live\ndomain: vault\n---\n# B\n")
    r = run(pv, "--check")
    assert r.returncode == 1
    assert "b.md" in r.stdout and "need" in r.stdout


def test_check_fails_on_bad_state(pv):
    write(pv / FOLDER / "b.md", playbook(state="asleep"))
    r = run(pv, "--check")
    assert r.returncode == 1
    assert "b.md: state:" in r.stdout


def test_check_fails_on_unknown_domain(pv):
    write(pv / FOLDER / "b.md", playbook(domain="football"))
    r = run(pv, "--check")
    assert r.returncode == 1
    assert "b.md: domain:" in r.stdout


def test_check_fails_on_missing_tool_path(pv):
    write(pv / FOLDER / "b.md", playbook(extra="tools: [_agent/tools/nope/run.py]\n"))
    r = run(pv, "--check")
    assert r.returncode == 1
    assert "_agent/tools/nope/run.py" in r.stdout and "does not exist" in r.stdout


def test_existing_tool_path_passes(pv):
    write(pv / "_agent/tools/yes/run.py", "")
    write(pv / FOLDER / "b.md", playbook(extra="tools: [_agent/tools/yes/run.py]\n"))
    assert run(pv, "--check").returncode == 0


def test_tools_as_a_yaml_block_list(pv):
    write(pv / FOLDER / "b.md", playbook(extra="tools:\n  - _agent/tools/nope/run.py\n"))
    r = run(pv, "--check")
    assert r.returncode == 1
    assert "_agent/tools/nope/run.py" in r.stdout


def test_check_fails_on_tool_outside_agent_tools(pv):
    write(pv / "scripts/x.py", "")
    write(pv / FOLDER / "b.md", playbook(extra="tools: [scripts/x.py]\n"))
    r = run(pv, "--check")
    assert r.returncode == 1
    assert "scripts/x.py" in r.stdout and "_agent/tools/" in r.stdout


def test_check_fails_on_orphan_companion(pv):
    write(pv / FOLDER / "z-reference.md", companion(parent="z.md"))
    r = run(pv, "--check")
    assert r.returncode == 1
    assert "z-reference.md" in r.stdout and "z.md" in r.stdout


def test_file_without_frontmatter_does_not_crash_table(pv):
    write(pv / FOLDER / "b.md", "# Just a heading\n")
    write(pv / FOLDER / "c.md", "---\nneed: [unclosed\n")
    r = run(pv)
    assert r.returncode == 0, r.stderr
    assert "Do the A thing" in r.stdout
    c = run(pv, "--check")
    assert c.returncode == 1
    assert "b.md" in c.stdout
    assert "Traceback" not in c.stderr


def test_domains_read_from_readme(pv):
    write(pv / FOLDER / "b.md", playbook(domain="cooking"))
    assert run(pv, "--check").returncode == 1
    write(pv / FOLDER / "README.md", "---\ntype: resource\ndomains: [vault, wiki, cooking]\n---\n# Playbooks\n")
    assert run(pv, "--check").returncode == 0


def test_readme_without_domains_fails_check_once(pv):
    write(pv / FOLDER / "README.md", "# Playbooks\n")
    r = run(pv, "--check")
    assert r.returncode == 1
    assert len([l for l in r.stdout.splitlines() if "README.md" in l]) == 1
    assert run(pv).returncode == 0


def test_missing_folder_is_a_clear_failure(tmp_path):
    v = tmp_path / "vault"
    dest = v / ".claude" / "skills" / "vlt-playbook" / "index.py"
    dest.parent.mkdir(parents=True)
    shutil.copy(INDEX_SRC, dest)
    r = run(v, "--check")
    assert r.returncode == 1
    assert "resources/playbooks" in r.stdout
    assert "Traceback" not in r.stderr
