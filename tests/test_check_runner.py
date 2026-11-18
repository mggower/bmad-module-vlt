import shutil
import subprocess
import sys

import pytest

from conftest import REPO, write

CORE = REPO / "kits" / "core" / "files"
RUNNER = "_agent/tools/checks/run.py"


@pytest.fixture
def cv(tmp_path):
    """A vault holding the core kit's files only."""
    v = tmp_path / "vault"
    shutil.copytree(CORE, v)
    return v


def run(v):
    return subprocess.run([sys.executable, str(v / RUNNER)], capture_output=True, text=True, cwd="/")


def test_clean_vault_passes(cv):
    r = run(cv)
    assert r.returncode == 0, r.stdout + r.stderr
    assert r.stdout.strip().splitlines()[-1].endswith("0 failed")


def test_tool_folder_without_readme_fails(cv):
    write(cv / "_agent/tools/foo/run.py", "")
    r = run(cv)
    assert r.returncode == 1
    assert "_agent/tools/foo" in r.stdout
    assert r.stdout.strip().splitlines()[-1].endswith("1 failed")


def test_failing_check_py_fails_the_run(cv):
    write(cv / "_agent/tools/bar/README.md", "# bar\n")
    write(cv / "_agent/tools/bar/check.py", "import sys\nprint('bar is broken')\nsys.exit(3)\n")
    r = run(cv)
    assert r.returncode == 1
    assert "FAIL bar" in r.stdout
    assert "bar is broken" in r.stdout


def test_passing_check_py_is_counted(cv):
    write(cv / "_agent/tools/bar/README.md", "# bar\n")
    write(cv / "_agent/tools/bar/check.py", "print('fine')\n")
    r = run(cv)
    assert r.returncode == 0
    assert "ok   bar" in r.stdout
    assert r.stdout.strip().splitlines()[-1] == "3 checks, 0 failed"


def test_all_checks_run_after_a_failure(cv):
    for name, code in (("aaa", 1), ("zzz", 0)):
        write(cv / f"_agent/tools/{name}/README.md", f"# {name}\n")
        write(cv / f"_agent/tools/{name}/check.py", f"import sys\nsys.exit({code})\n")
    r = run(cv)
    assert r.returncode == 1
    assert "FAIL aaa" in r.stdout and "ok   zzz" in r.stdout


def test_broken_playbook_fails_the_run(cv):
    write(cv / "resources/playbooks/bad.md", "# no frontmatter\n")
    r = run(cv)
    assert r.returncode == 1
    assert "FAIL playbooks" in r.stdout and "bad.md" in r.stdout


def test_missing_playbook_index_is_reported(cv):
    shutil.rmtree(cv / ".claude/skills/vlt-playbook")
    write(cv / "_agent/tools/bar/README.md", "# bar\n")
    write(cv / "_agent/tools/bar/check.py", "")
    r = run(cv)
    assert r.returncode == 1
    assert "FAIL playbooks" in r.stdout and "index.py" in r.stdout
    assert "ok   bar" in r.stdout
    assert "Traceback" not in r.stderr
