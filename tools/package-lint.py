#!/usr/bin/env python3
"""Pre-tag packaging lint for the vlt plugin. Tag only on exit 0.

    python3 tools/package-lint.py --expect-version X.Y.Z [--root DIR]

Checks the working tree on disk, not the git index: the plugin is installed as a file
copy, so cruft on disk ships. Eight checks, all run every time:

  cruft     no .decision-log.md, __pycache__, *.pyc or .DS_Store in the shipped surface
  version   marketplace.json and every kit.yaml carry --expect-version
  skills    the manifest's skills list is exactly the directories under skills/
  kits      no vault path ships in two kits
  budget    the rules files and the named pointer skills stay within their line budgets
  pointers  every named skill in a kit names a playbook some kit ships
  scrub     no machine path and no persona word in kits/
  seed      all kits seeded into an empty vault pass that vault's own checks

Stdlib only. Prints one line per failure, then `PASS: 8 checks` or `FAIL: M of 8`.
"""
import argparse
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SURFACE = ("skills", "kits", "scripts", ".claude-plugin")
CRUFT_NAMES = {".decision-log.md", ".DS_Store"}
BUDGETS = {"_meta/vault.md": 120, "_meta/wiki.md": 120, "_meta/frontmatter.md": 150}
POINTER_BUDGET = 15
ENTRY_SKILL = "vlt-playbook"     # the index skill; it is not a pointer at one playbook
BANNED = (re.compile(r"/Users/"), re.compile(r"/home/"), re.compile(r"partner", re.I))
PLAYBOOK = re.compile(r"`(resources/playbooks/[A-Za-z0-9._-]+\.md)`")


def load_engine(root):
    sys.dont_write_bytecode = True   # the lint must not create the cruft it checks for
    spec = importlib.util.spec_from_file_location("kits_engine", root / "scripts" / "kits.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rel(root, path):
    return path.relative_to(root).as_posix()


def check_cruft(root, _args):
    out = []
    for name in SURFACE:
        for path in sorted((root / name).rglob("*")) if (root / name).exists() else []:
            if path.name in CRUFT_NAMES or path.name == "__pycache__" or path.suffix == ".pyc":
                out.append(f"{rel(root, path)} is build cruft")
    return out


def check_version(root, args):
    out = []
    manifest = json.loads((root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    version = manifest["plugins"][0].get("version")
    if version != args.expect_version:
        out.append(f"marketplace.json version is {version}, expected {args.expect_version}")
    engine = load_engine(root)
    for kit in engine.kit_dirs(root / "kits"):
        kit_version = engine.kit_meta(kit)["version"]
        if kit_version != args.expect_version:
            out.append(f"kits/{kit.name}/kit.yaml version is {kit_version}, expected {args.expect_version}")
    return out


def check_skills(root, _args):
    manifest = json.loads((root / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    listed = {s.removeprefix("./").rstrip("/") for s in manifest["plugins"][0].get("skills", [])}
    on_disk = {f"skills/{d.name}" for d in (root / "skills").iterdir() if d.is_dir()}
    out = [f"{s} is on disk but not in the manifest's skills list" for s in sorted(on_disk - listed)]
    out += [f"{s} is in the manifest's skills list but not on disk" for s in sorted(listed - on_disk)]
    out += [f"{s} has no SKILL.md" for s in sorted(on_disk) if not (root / s / "SKILL.md").is_file()]
    return out


def check_kits(root, _args):
    engine = load_engine(root)
    try:
        files = engine.kit_files(root / "kits")
    except engine.Stop as stop:
        return [str(stop)]
    return [] if files else ["kits/ ships no files"]


def kit_file_paths(root):
    """vault path -> source file, tolerating a duplicate (check_kits reports that)."""
    out = {}
    for files in sorted((root / "kits").glob("*/files")):
        for src in sorted(files.rglob("*")):
            if src.is_file():
                out.setdefault(src.relative_to(files).as_posix(), src)
    return out


def lines_in(path):
    return len(path.read_text(encoding="utf-8").splitlines())


def check_budget(root, _args):
    out = []
    files = kit_file_paths(root)
    for vault_path, budget in BUDGETS.items():
        if vault_path not in files:
            out.append(f"{vault_path} is not shipped by any kit")
        elif lines_in(files[vault_path]) > budget:
            out.append(f"{vault_path} is {lines_in(files[vault_path])} lines, budget {budget}")
    for vault_path, src in files.items():
        parts = vault_path.split("/")
        if parts[:2] == [".claude", "skills"] and parts[-1] == "SKILL.md" and parts[2] != ENTRY_SKILL:
            if lines_in(src) > POINTER_BUDGET:
                out.append(f"{vault_path} is {lines_in(src)} lines, budget {POINTER_BUDGET} "
                           "(a named skill points at its playbook and restates nothing)")
    return out


def check_pointers(root, _args):
    out = []
    files = kit_file_paths(root)
    for vault_path, src in files.items():
        parts = vault_path.split("/")
        if parts[:2] != [".claude", "skills"] or parts[-1] != "SKILL.md" or parts[2] == ENTRY_SKILL:
            continue
        named = PLAYBOOK.findall(src.read_text(encoding="utf-8"))
        if not named:
            out.append(f"{vault_path} names no playbook")
        out += [f"{vault_path} names {p}, which no kit ships" for p in named if p not in files]
    return out


def check_scrub(root, _args):
    out = []
    for src in sorted((root / "kits").rglob("*")):
        if not src.is_file():
            continue
        text = src.read_text(encoding="utf-8", errors="replace")
        for number, line in enumerate(text.splitlines(), 1):
            for pattern in BANNED:
                if pattern.search(line):
                    out.append(f"{rel(root, src)}:{number} contains {pattern.pattern!r}")
    return out


def check_seed(root, _args):
    with tempfile.TemporaryDirectory() as tmp:
        vault = Path(tmp) / "vault"
        vault.mkdir()
        seed = subprocess.run([sys.executable, str(root / "scripts" / "kits.py"), "seed", "--vault", str(vault),
                               "--kits-dir", str(root / "kits")], capture_output=True, text=True)
        if seed.returncode != 0:
            return [f"seeding an empty vault failed: {seed.stderr.strip()}"]
        runner = vault / "_agent" / "tools" / "checks" / "run.py"
        if not runner.is_file():
            return ["the seeded vault has no _agent/tools/checks/run.py"]
        run = subprocess.run([sys.executable, str(runner)], capture_output=True, text=True)
        if run.returncode != 0:
            return ["a freshly seeded vault fails its own checks:"] + [f"  {l}" for l in run.stdout.splitlines()]
    return []


CHECKS = (("cruft", check_cruft), ("version", check_version), ("skills", check_skills), ("kits", check_kits),
          ("budget", check_budget), ("pointers", check_pointers), ("scrub", check_scrub), ("seed", check_seed))


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--expect-version", required=True)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    root = Path(args.root).resolve()
    failed = 0
    for name, check in CHECKS:
        try:
            problems = check(root, args)
        except Exception as exc:  # a check that cannot run is a failure, never a pass
            problems = [f"could not run: {type(exc).__name__}: {exc}"]
        failed += bool(problems)
        for problem in problems:
            print(f"[{name}] {problem}")
    print(f"PASS: {len(CHECKS)} checks" if not failed else f"FAIL: {failed} of {len(CHECKS)}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
