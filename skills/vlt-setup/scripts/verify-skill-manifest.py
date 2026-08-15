#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Compute, verify, and shrink-check the skill-asset manifest (build B7-2).

The manifest ({overlays}/.baseline/.skill-manifest, one `<sha256>\\t<path>`
line per file, paths relative to --root) is the module-owned divergence net
over everything the module ships into a vault. Its scope is DERIVED
STRUCTURALLY — a walk of the shipped trees, never a hand-kept list:

- every file under each **shipped** `vlt-*` skill dir in the live skills dir
  (whole trees: SKILL.md, assets/, references/, scripts/, and anything a
  future build adds). Shipped-ness is provenance-based, from the module
  source: exactly the `vlt-*` dirs present under --source-skills-dir. A
  locally-minted `vlt-agent-*`/`vlt-*` dir is NEVER manifested — it is the
  vault's, and the manifest is the module-owned net only.
- installed module-owned extras: files under {root}/.claude/workflows/ and
  {root}/.claude/hooks/ whose basenames exist under the shipped
  vlt-setup/assets/workflows/ and assets/hooks/ trees. The walk of the
  shipped tree defines the set — a vault's own hooks are untouched, unlisted.
- exclusions: the upgrade's cruft set (.decision-log.md, __pycache__/,
  *.pyc, .DS_Store) — dev artifacts never enter the net.

Modes (JSON result to stdout in both):
  --write   compute the manifest and write it. When one already exists at the
            target path, report previous_entries / added / removed first —
            the shrink check: `removed` is informational, never blocking (a
            de-shipped file legitimately leaves the net), but always printed,
            so a silent narrowing is structurally impossible.
  --verify  recompute SHAs for every manifest entry against the live files;
            report diverged (SHA mismatch) and missing paths. Exit 0 either
            way — divergence is a finding for the caller to surface, not a
            script failure.

Exit codes: 0=success (findings included), 1=usage error, 2=operational error
(manifest missing/unreadable in --verify, unreadable trees).
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

# The upgrade's cruft set — byte-for-byte the names vlt-upgrade Step 2
# excludes from the apply copy. Dev artifacts must not enter the net even
# if present on disk.
CRUFT_NAMES = {".decision-log.md", ".DS_Store"}
CRUFT_DIR_NAMES = {"__pycache__"}
CRUFT_SUFFIXES = {".pyc"}

# Installed module-owned extras: {root}/.claude/<dir> files whose basenames
# the shipped vlt-setup/assets/<dir> tree carries.
EXTRA_DIRS = ("workflows", "hooks")


def is_cruft(path: Path) -> bool:
    if path.name in CRUFT_NAMES or path.suffix in CRUFT_SUFFIXES:
        return True
    return any(part in CRUFT_DIR_NAMES for part in path.parts)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_manifest(root: Path, live_skills_dir: Path, source_skills_dir: Path) -> dict:
    """Return {path-relative-to-root: sha256} for the module-owned net.

    The scope is the structural walk documented in the module docstring —
    shipped skill dirs (provenance from source_skills_dir) plus installed
    module-owned extras (basenames from the shipped assets trees).
    """
    entries = {}

    shipped = {
        p.name for p in source_skills_dir.glob("vlt-*") if p.is_dir()
    }
    for name in sorted(shipped):
        skill_dir = live_skills_dir / name
        if not skill_dir.is_dir():
            continue
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file() and not is_cruft(f.relative_to(skill_dir)):
                entries[str(f.relative_to(root))] = sha256_file(f)

    for sub in EXTRA_DIRS:
        shipped_tree = source_skills_dir / "vlt-setup" / "assets" / sub
        if not shipped_tree.is_dir():
            continue
        basenames = {p.name for p in shipped_tree.rglob("*") if p.is_file()}
        installed = root / ".claude" / sub
        if not installed.is_dir():
            continue
        for f in sorted(installed.iterdir()):
            if f.is_file() and f.name in basenames and not is_cruft(f):
                entries[str(f.relative_to(root))] = sha256_file(f)

    return entries


def read_manifest(path: Path) -> dict:
    """Parse `<sha256>\\t<path>` lines into {path: sha256}."""
    entries = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        sha, _, rel = line.partition("\t")
        if not rel:
            raise ValueError(f"malformed manifest line (no tab): {line!r}")
        entries[rel] = sha
    return entries


def write_manifest(path: Path, entries: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"{sha}\t{rel}" for rel, sha in sorted(entries.items())]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute (--write) or verify (--verify) the skill-asset "
        "manifest. Scope is derived structurally from the shipped trees — "
        "never a hand-kept list; --write reports added/removed vs any prior "
        "manifest (the shrink check)."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Compute and write the manifest")
    mode.add_argument("--verify", action="store_true", help="Verify live files against the manifest")
    parser.add_argument(
        "--root", required=True,
        help="Install/project root; manifest paths are recorded relative to it",
    )
    parser.add_argument(
        "--live-skills-dir",
        help="Live installed skills dir (default: {root}/.claude/skills)",
    )
    parser.add_argument(
        "--source-skills-dir",
        help="Module SOURCE skills dir — shipped-ness provenance (required for "
        "--write; a locally-minted vlt-* dir is never manifested)",
    )
    parser.add_argument(
        "--manifest",
        help="Manifest path (default: {overlays-dir}/.baseline/.skill-manifest)",
    )
    parser.add_argument(
        "--overlays-dir",
        help="Resolved {overlays} dir, used to derive the default manifest path",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    root = Path(args.root).resolve()

    if args.manifest:
        manifest_path = Path(args.manifest).resolve()
    elif args.overlays_dir:
        manifest_path = (Path(args.overlays_dir) / ".baseline" / ".skill-manifest").resolve()
    else:
        print("Error: pass --manifest or --overlays-dir", file=sys.stderr)
        sys.exit(1)

    if args.write:
        if not args.source_skills_dir:
            print("Error: --write requires --source-skills-dir (shipped-ness provenance)", file=sys.stderr)
            sys.exit(1)
        live = (
            Path(args.live_skills_dir).resolve()
            if args.live_skills_dir
            else root / ".claude" / "skills"
        )
        source = Path(args.source_skills_dir).resolve()
        if not source.is_dir():
            print(f"Error: source skills dir not found: {source}", file=sys.stderr)
            sys.exit(2)

        entries = compute_manifest(root, live, source)

        previous = None
        if manifest_path.is_file():
            try:
                previous = read_manifest(manifest_path)
            except Exception as e:
                print(f"Error: existing manifest unreadable: {e}", file=sys.stderr)
                sys.exit(2)

        result = {
            "status": "success",
            "mode": "write",
            "manifest_path": str(manifest_path.resolve()),
            "entries": len(entries),
        }
        if previous is not None:
            result["previous_entries"] = len(previous)
            result["added"] = sorted(set(entries) - set(previous))
            result["removed"] = sorted(set(previous) - set(entries))

        write_manifest(manifest_path, entries)
        print(json.dumps(result, indent=2))

    else:  # --verify
        if not manifest_path.is_file():
            print(f"Error: manifest not found: {manifest_path}", file=sys.stderr)
            sys.exit(2)
        try:
            recorded = read_manifest(manifest_path)
        except Exception as e:
            print(f"Error: manifest unreadable: {e}", file=sys.stderr)
            sys.exit(2)

        diverged, missing = [], []
        for rel, sha in sorted(recorded.items()):
            live_file = root / rel
            if not live_file.is_file():
                missing.append(rel)
            elif sha256_file(live_file) != sha:
                diverged.append(rel)

        result = {
            "status": "success",
            "mode": "verify",
            "manifest_path": str(manifest_path.resolve()),
            "entries": len(recorded),
            "diverged": diverged,
            "missing": missing,
        }
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
