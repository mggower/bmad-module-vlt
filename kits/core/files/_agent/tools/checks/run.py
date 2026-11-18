#!/usr/bin/env python3
"""Run every check this vault has.

    python3 _agent/tools/checks/run.py

In order: the playbook index's own --check; that every tool folder has a README; then
every _agent/tools/<name>/check.py. A check.py is any script that exits non-zero when
something is wrong and prints what. All checks run even after one fails.
Exit 1 if any failed. Stdlib only; finds the vault from its own location.
"""
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
TOOLS = VAULT / "_agent" / "tools"
INDEX = VAULT / ".claude" / "skills" / "vlt-playbook" / "index.py"


def script(path, *args):
    if not path.is_file():
        return False, f"{path.relative_to(VAULT).as_posix()} does not exist"
    proc = subprocess.run([sys.executable, str(path), *args], cwd=VAULT, capture_output=True, text=True)
    return proc.returncode == 0, (proc.stdout + proc.stderr).strip()


def tool_readmes():
    missing = [d for d in sorted(TOOLS.iterdir()) if d.is_dir() and not (d / "README.md").is_file()]
    return not missing, "\n".join(f"{d.relative_to(VAULT).as_posix()}/ has no README.md" for d in missing)


def checks():
    yield "playbooks", lambda: script(INDEX, "--check")
    yield "tool-readmes", tool_readmes
    for path in sorted(TOOLS.glob("*/check.py")):
        yield path.parent.name, lambda path=path: script(path)


def main():
    total = failed = 0
    for name, run in checks():
        ok, output = run()
        total += 1
        failed += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {name}")
        if not ok and output:
            print("\n".join(f"     {line}" for line in output.splitlines()))
    print(f"{total} checks, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
