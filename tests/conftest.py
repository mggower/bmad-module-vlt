import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
KITS_PY = REPO / "scripts" / "kits.py"
sys.path.insert(0, str(REPO / "scripts"))


def git(cwd, *args):
    return subprocess.run(
        ["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", *args],
        cwd=cwd, capture_output=True, text=True, check=True,
    )


def run_kits(vault, kits_dir, *args):
    """Run scripts/kits.py as the skills do. Returns the CompletedProcess."""
    return subprocess.run(
        [sys.executable, str(KITS_PY), args[0], "--vault", str(vault),
         "--kits-dir", str(kits_dir), *args[1:]],
        capture_output=True, text=True,
    )


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def kits_dir(tmp_path):
    d = tmp_path / "kits"
    write(d / "core" / "kit.yaml", "name: core\nversion: 1.0.0\ndescription: test kit\n")
    write(d / "core" / "files" / "_meta" / "vault.md", "# rules v1\n")
    write(d / "core" / "files" / "resources" / "playbooks" / "README.md", "# playbooks\n")
    return d


@pytest.fixture
def vault(tmp_path):
    v = tmp_path / "vault"
    v.mkdir()
    git(v, "init", "-q")
    git(v, "commit", "-q", "--allow-empty", "-m", "init")
    return v


def commit_all(vault, msg="c"):
    git(vault, "add", "-A")
    git(vault, "commit", "-q", "-m", msg)
