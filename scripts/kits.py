#!/usr/bin/env python3
"""Seed vlt kits into a vault, and pull kit changes file by file.

    kits.py seed   --vault DIR            copy every kit file the vault does not have
    kits.py status --vault DIR [--json]   one line per file: <state> <kit> <path>
    kits.py diff   --vault DIR PATH       vault copy against the kit's current copy
    kits.py take   --vault DIR PATH...    write the kit's copy, record it
    kits.py leave  --vault DIR PATH...    record the kit's copy as seen, write nothing

A kit is kits/<kit>/kit.yaml plus kits/<kit>/files/<vault-relative path>: the tree is the
manifest. The vault owns every seeded file. Nothing here overwrites or deletes a vault
file unless `take` is asked to, and `take` refuses over uncommitted vault edits.

The lock, _agent/kits.lock, records per file the hash of the shipped copy the vault last
saw. With the kit's current hash and the vault's own, that gives each file a state:

    unchanged        the vault matches the kit
    shipped-changed  the kit moved, the vault did not
    vault-changed    the vault moved, the kit did not
    both-changed     both moved, differently
    vault-removed    the vault deleted it (never re-created unasked)
    new              the kit added it since the lock
    retired          the kit dropped it (the vault's copy is left alone)

Stdlib only. Exit: 0 ok, 1 a refused or unknown path, 2 no usable lock or a broken kit.
"""
import argparse
import difflib
import hashlib
import json
import subprocess
import sys
from pathlib import Path

LOCK_REL = "_agent/kits.lock"
SKIP_NAMES = {".DS_Store"}
SKIP_DIRS = {"__pycache__"}
NO_LOCK = "no usable {lock}: {why}. To seed this vault, run vlt-setup."


class Stop(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def kit_meta(kit_dir):
    """kit.yaml is flat `key: value` lines; nothing else is supported."""
    out = {}
    meta = kit_dir / "kit.yaml"
    if not meta.is_file():
        raise Stop(2, f"{kit_dir.name}: no kit.yaml")
    for line in meta.read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip().strip("\"'")
    if not out.get("version"):
        raise Stop(2, f"{kit_dir.name}: kit.yaml has no version")
    return out


def kit_dirs(kits_dir):
    return sorted(d for d in Path(kits_dir).iterdir() if d.is_dir() and (d / "files").is_dir())


def kit_files(kits_dir):
    """vault-relative posix path -> (kit name, source file). A path in two kits is an error."""
    out = {}
    for kit in kit_dirs(kits_dir):
        root = kit / "files"
        for src in sorted(root.rglob("*")):
            if not src.is_file() or src.name in SKIP_NAMES or SKIP_DIRS & set(src.parts):
                continue
            rel = src.relative_to(root).as_posix()
            if rel in out:
                raise Stop(2, f"{rel} ships in two kits: {out[rel][0]} and {kit.name}")
            out[rel] = (kit.name, src)
    return out


def read_lock(vault):
    """The parsed lock. Raises Stop(2) when it is missing or unreadable."""
    path = Path(vault) / LOCK_REL
    if not path.is_file():
        raise Stop(2, NO_LOCK.format(lock=LOCK_REL, why="the file is missing"))
    try:
        lock = json.loads(path.read_text(encoding="utf-8"))
        if lock["schema"] != 1 or not isinstance(lock["kits"], dict):
            raise ValueError("unknown shape")
        for kit in lock["kits"].values():
            if not isinstance(kit["files"], dict):
                raise ValueError("unknown shape")
    except (ValueError, KeyError, TypeError) as exc:
        raise Stop(2, NO_LOCK.format(lock=LOCK_REL, why=f"it cannot be read ({exc}); "
                                     "repair or remove it first"))
    return lock


def write_lock(vault, lock):
    path = Path(vault) / LOCK_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(lock, indent=2, sort_keys=True) + "\n"
    if not path.is_file() or path.read_text(encoding="utf-8") != text:
        path.write_text(text, encoding="utf-8")


def locked(lock):
    """vault path -> (kit name, lock hash), across every kit in the lock."""
    return {rel: (kit, h) for kit, body in lock["kits"].items() for rel, h in body["files"].items()}


def state(lock_hash, kit_hash, vault_hash):
    if vault_hash == kit_hash:
        return "unchanged"
    if kit_hash is None:
        return "retired"
    if vault_hash is None:
        return "new" if lock_hash is None else "vault-removed"
    if lock_hash is not None and vault_hash == lock_hash:
        return "shipped-changed"
    if kit_hash == lock_hash:
        return "vault-changed"
    return "both-changed"


def record(lock, kit, rel, kit_hash):
    lock["kits"].setdefault(kit, {"version": "", "files": {}})["files"][rel] = kit_hash


def survey(vault, kits_dir, lock):
    """Rows of (state, kit, path), and the lock refreshed where the vault already matches."""
    files = kit_files(kits_dir)
    seen = locked(lock)
    rows = []
    for rel in sorted(set(files) | set(seen)):
        kit, src = files.get(rel, (seen.get(rel, (None,))[0], None))
        kit_hash = sha(src) if src else None
        target = Path(vault) / rel
        vault_hash = sha(target) if target.is_file() else None
        lock_hash = seen.get(rel, (None, None))[1]
        st = state(lock_hash, kit_hash, vault_hash)
        if st == "unchanged" and kit_hash is not None and lock_hash != kit_hash:
            record(lock, kit, rel, kit_hash)
        rows.append((st, kit, rel))
    stamp_versions(kits_dir, lock, rows)
    return rows


def stamp_versions(kits_dir, lock, rows):
    """A kit's lock version moves to the shipped one once no file of it awaits a decision."""
    waiting = {kit for st, kit, _ in rows if st in ("shipped-changed", "both-changed", "new")}
    for kit_dir in kit_dirs(kits_dir):
        body = lock["kits"].get(kit_dir.name)
        if body is not None and (kit_dir.name not in waiting or not body.get("version")):
            body["version"] = kit_meta(kit_dir)["version"]


def cmd_seed(vault, kits_dir, _args):
    files = kit_files(kits_dir)
    lock_path = Path(vault) / LOCK_REL
    lock = read_lock(vault) if lock_path.exists() else {"schema": 1, "kits": {}}
    seen = locked(lock)
    for kit_dir in kit_dirs(kits_dir):
        lock["kits"].setdefault(kit_dir.name, {"version": kit_meta(kit_dir)["version"], "files": {}})
    for rel in sorted(files):
        kit, src = files[rel]
        target = Path(vault) / rel
        if not target.exists():
            if rel in seen:
                print(f"vault-removed {rel}")
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(src.read_bytes())
            record(lock, kit, rel, sha(src))
            print(f"seeded {rel}")
            continue
        same = target.is_file() and sha(target) == sha(src)
        if rel not in seen:
            record(lock, kit, rel, sha(src))
        print(f"{'same' if same else 'kept-yours'} {rel}")
    write_lock(vault, lock)
    return 0


def cmd_status(vault, kits_dir, args):
    lock = read_lock(vault)
    rows = survey(vault, kits_dir, lock)
    write_lock(vault, lock)
    if args.json:
        print(json.dumps([{"state": s, "kit": k, "path": p} for s, k, p in rows], indent=2))
    else:
        for st, kit, rel in rows:
            print(f"{st} {kit} {rel}")
    return 0


def cmd_diff(vault, kits_dir, args):
    files = kit_files(kits_dir)
    rel = args.paths[0]
    if rel not in files:
        raise Stop(1, f"{rel}: no kit ships this path")
    target = Path(vault) / rel
    mine = target.read_text(encoding="utf-8").splitlines(keepends=True) if target.is_file() else []
    theirs = files[rel][1].read_text(encoding="utf-8").splitlines(keepends=True)
    sys.stdout.writelines(difflib.unified_diff(mine, theirs, f"vault/{rel}", f"kit/{rel}"))
    return 0


def uncommitted(vault, rel):
    """True when git cannot give this path back as it stands now."""
    proc = subprocess.run(["git", "status", "--porcelain", "--", rel],
                          cwd=vault, capture_output=True, text=True)
    return proc.returncode != 0 or bool(proc.stdout.strip())


def cmd_take(vault, kits_dir, args):
    lock = read_lock(vault)
    files = kit_files(kits_dir)
    code = 0
    for rel in args.paths:
        if rel not in files:
            print(f"{rel}: no kit ships this path", file=sys.stderr)
            code = 1
            continue
        kit, src = files[rel]
        target = Path(vault) / rel
        if target.exists() and sha(target) != sha(src) and uncommitted(vault, rel):
            print(f"{rel}: refused, the vault's copy has uncommitted changes (or the vault is "
                  "not a git repository). Commit it first so it can be recovered.", file=sys.stderr)
            code = 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(src.read_bytes())
        record(lock, kit, rel, sha(src))
        print(f"took {rel}")
    survey(vault, kits_dir, lock)
    write_lock(vault, lock)
    return code


def cmd_leave(vault, kits_dir, args):
    lock = read_lock(vault)
    files = kit_files(kits_dir)
    seen = locked(lock)
    code = 0
    for rel in args.paths:
        if rel in files:
            kit, src = files[rel]
            record(lock, kit, rel, sha(src))
            print(f"left {rel}")
        elif rel in seen:
            del lock["kits"][seen[rel][0]]["files"][rel]
            print(f"dropped {rel} from the lock (retired; the vault's copy is untouched)")
        else:
            print(f"{rel}: no kit ships this path", file=sys.stderr)
            code = 1
    survey(vault, kits_dir, lock)
    write_lock(vault, lock)
    return code


COMMANDS = {"seed": cmd_seed, "status": cmd_status, "diff": cmd_diff, "take": cmd_take, "leave": cmd_leave}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=sorted(COMMANDS))
    parser.add_argument("--vault", required=True)
    parser.add_argument("--kits-dir", default=str(Path(__file__).resolve().parents[1] / "kits"))
    parser.add_argument("--json", action="store_true")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args(argv)
    if args.command in ("diff", "take", "leave") and not args.paths:
        parser.error(f"{args.command} needs at least one path")
    vault = Path(args.vault)
    if not vault.is_dir():
        print(f"{vault}: not a directory", file=sys.stderr)
        return 2
    try:
        return COMMANDS[args.command](vault, Path(args.kits_dir), args)
    except Stop as stop:
        print(str(stop), file=sys.stderr)
        return stop.code


if __name__ == "__main__":
    sys.exit(main())
