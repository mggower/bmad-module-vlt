#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# ///
"""Compute, verify, and shrink-check the skill-asset manifest (build B7-2;
source-hash semantics build B10-1).

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

Hashing rule (B10-1): the manifest records STOCK content. Every
source-provenanced path — a file the module source tree carries at the same
relative path, including every EXTRA_DIRS entry (mapped by basename) — is
hashed FROM THE SOURCE TREE, so a local edit present at write time is
reported as divergence, never absorbed as the new baseline. A live file
under a shipped skill dir with no source counterpart is hashed live (the
only live-hash case on the normal path). When --source-skills-dir resolves
to the live skills dir itself (the fresh-install fallback), the write
proceeds with `"source_mode": "live"` and a top-level `"warning"` that the
net is live-hashed for that write — loud, never the default silence.

Sanction record ({overlays}/.skill-manifest.sanctioned, `<sha256>\\t<path>`
lines, paths relative to --root like the manifest): the vault-owned record
of sanctioned migration edits, appended by the sanctioning acts in
vlt-upgrade Step 3 (loop-profile lift, write-through). Both modes read it
(--sanctioned, default derived from --overlays-dir; absent file = empty
set, never an error) and partition divergence: live sha == baseline sha ->
clean; live sha == sanctioned sha -> `sanctioned` (excluded from
`diverged`, denominated); else -> `diverged`. A record entry whose live sha
now equals the stock sha is reported `sanction_stale` — informational,
never auto-pruned (the record is the vault's). The sanctioned sha pins the
sanctioned content: a further unsanctioned edit on top shows `diverged`.

Modes (JSON result to stdout in both):
  --write   compute the manifest and write it. Refuses with the named error
            `version-skew` (exit 2) when the source tree's module.yaml
            `module_version:` differs from the installed record's, and
            `version-record-missing` (exit 2) when either record is
            unreadable — a skewed source would make every entry cry wolf.
            Otherwise THE WRITE ALWAYS PROCEEDS: write-time divergence is
            reported (`diverged` / `sanctioned` / `sanction_stale`), never
            refused. When one already exists at the target path, report
            previous_entries / added / removed first — the shrink check:
            `removed` is informational, never blocking (a de-shipped file
            legitimately leaves the net), but always printed, so a silent
            narrowing is structurally impossible.
  --verify  recompute SHAs for every manifest entry against the live files;
            report diverged (unsanctioned SHA mismatch), sanctioned,
            sanction_stale, and missing paths. Exit 0 either way —
            divergence is a finding for the caller to surface, not a
            script failure.

Exit codes: 0=success (findings included), 1=usage error, 2=operational error
(manifest missing/unreadable in --verify, unreadable trees, version-skew,
version-record-missing, duplicate EXTRA_DIRS basename in source).
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
    """Return {path-relative-to-root: (sha256, provenance)} for the net.

    provenance is "source" (sha hashed from the module source tree — the
    entry can diverge live) or "live" (no source counterpart; hashed from
    the live file, today's behavior preserved for de-facto extras). The
    scope is the structural walk documented in the module docstring —
    shipped skill dirs (provenance from source_skills_dir) plus installed
    module-owned extras (basenames from the shipped assets trees).
    """
    entries = {}

    shipped = {
        p.name for p in source_skills_dir.glob("vlt-*") if p.is_dir()
    }
    for name in sorted(shipped):
        live_dir = live_skills_dir / name
        if not live_dir.is_dir():
            continue
        source_dir = source_skills_dir / name
        source_rels = set()
        # Source-provenanced paths: hashed from the SOURCE tree, recorded at
        # the live-relative path. A source file whose live counterpart is
        # missing is still recorded — --verify then reports it `missing`.
        for f in sorted(source_dir.rglob("*")):
            if f.is_file() and not is_cruft(f.relative_to(source_dir)):
                rel = f.relative_to(source_dir)
                source_rels.add(rel)
                entries[str((live_dir / rel).relative_to(root))] = (sha256_file(f), "source")
        # Live-only files (no source counterpart at the same relpath) keep
        # today's behavior: hashed from live, recorded.
        for f in sorted(live_dir.rglob("*")):
            if f.is_file() and not is_cruft(f.relative_to(live_dir)):
                rel = f.relative_to(live_dir)
                if rel not in source_rels:
                    entries[str(f.relative_to(root))] = (sha256_file(f), "live")

    for sub in EXTRA_DIRS:
        shipped_tree = source_skills_dir / "vlt-setup" / "assets" / sub
        if not shipped_tree.is_dir():
            continue
        # basename -> source path; a duplicate basename would make the pick
        # arbitrary and silent — refuse operationally instead.
        source_by_name = {}
        for p in sorted(shipped_tree.rglob("*")):
            if p.is_file():
                if p.name in source_by_name:
                    print(
                        f"Error: duplicate basename {p.name!r} in shipped "
                        f"{shipped_tree} ({source_by_name[p.name]} vs {p}) — "
                        "cannot map installed extras unambiguously",
                        file=sys.stderr,
                    )
                    sys.exit(2)
                source_by_name[p.name] = p
        installed = root / ".claude" / sub
        if not installed.is_dir():
            continue
        for f in sorted(installed.iterdir()):
            if f.is_file() and f.name in source_by_name and not is_cruft(f):
                entries[str(f.relative_to(root))] = (
                    sha256_file(source_by_name[f.name]),
                    "source",
                )

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


def read_sanctioned(path: Path) -> dict:
    """Read the vault's sanction record; absent file => empty set."""
    if not path.is_file():
        return {}
    sanctioned = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        sha, _, rel = line.partition("\t")
        if not rel:
            raise ValueError(f"malformed sanction line (no tab): {line!r}")
        sanctioned[rel] = sha
    return sanctioned


def read_module_version(module_yaml: Path) -> str:
    """Stdlib line-parse of module.yaml's `module_version:` value."""
    for line in module_yaml.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("module_version:"):
            return stripped.split(":", 1)[1].strip().strip("'\"")
    raise ValueError(f"no module_version: line in {module_yaml}")


def write_manifest(path: Path, entries: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [f"{sha}\t{rel}" for rel, (sha, _prov) in sorted(entries.items())]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def partition_divergence(root: Path, baseline: dict, sanctioned: dict):
    """Partition live-vs-baseline mismatches against the sanction record.

    baseline is {path: stock-sha}. Returns (diverged, sanctioned_paths,
    sanction_stale) — paths whose live file exists, sorted. Clean or
    missing paths appear in none of the three (missing is the caller's).
    """
    diverged, sanctioned_paths, stale = [], [], []
    for rel, sha in sorted(baseline.items()):
        live_file = root / rel
        if not live_file.is_file():
            continue
        live_sha = sha256_file(live_file)
        if live_sha == sha:
            if rel in sanctioned:
                stale.append(rel)
        elif sanctioned.get(rel) == live_sha:
            sanctioned_paths.append(rel)
        else:
            diverged.append(rel)
    return diverged, sanctioned_paths, stale


def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute (--write) or verify (--verify) the skill-asset "
        "manifest. Scope is derived structurally from the shipped trees — "
        "never a hand-kept list; source-provenanced paths are hashed from "
        "the SOURCE tree (stock, never the live edit); --write reports "
        "added/removed vs any prior manifest (the shrink check) plus "
        "write-time diverged/sanctioned."
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
        help="Module SOURCE skills dir — shipped-ness provenance and the "
        "hash source for source-provenanced paths (required for --write; a "
        "locally-minted vlt-* dir is never manifested)",
    )
    parser.add_argument(
        "--manifest",
        help="Manifest path (default: {overlays-dir}/.baseline/.skill-manifest)",
    )
    parser.add_argument(
        "--overlays-dir",
        help="Resolved {overlays} dir, used to derive the default manifest "
        "and sanction-record paths",
    )
    parser.add_argument(
        "--sanctioned",
        help="Sanction record path (default: "
        "{overlays-dir}/.skill-manifest.sanctioned; absent file = empty set)",
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

    if args.sanctioned:
        sanctioned_path = Path(args.sanctioned).resolve()
    elif args.overlays_dir:
        sanctioned_path = (Path(args.overlays_dir) / ".skill-manifest.sanctioned").resolve()
    else:
        sanctioned_path = None
    try:
        sanctioned = read_sanctioned(sanctioned_path) if sanctioned_path else {}
    except Exception as e:
        print(f"Error: sanction record unreadable: {e}", file=sys.stderr)
        sys.exit(2)

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

        source_mode = "live" if source == live else "source"

        if source_mode == "source":
            # Version-skew refusal: a skewed source would source-hash a
            # manifest against files the vault does not have — every entry
            # instantly diverged/missing, a net that cries wolf.
            src_record = source / "vlt-setup" / "assets" / "module.yaml"
            live_record = live / "vlt-setup" / "assets" / "module.yaml"
            try:
                src_version = read_module_version(src_record)
                live_version = read_module_version(live_record)
            except Exception as e:
                print(
                    f"Error: version-record-missing — cannot read a "
                    f"module_version record: {e}",
                    file=sys.stderr,
                )
                sys.exit(2)
            if src_version != live_version:
                print(
                    f"Error: version-skew — source module_version "
                    f"{src_version!r} != installed module_version "
                    f"{live_version!r}. Apply the source to the install "
                    "first, or pass the source that matches the installed "
                    "version.",
                    file=sys.stderr,
                )
                sys.exit(2)

        entries = compute_manifest(root, live, source)

        previous = None
        if manifest_path.is_file():
            try:
                previous = read_manifest(manifest_path)
            except Exception as e:
                print(f"Error: existing manifest unreadable: {e}", file=sys.stderr)
                sys.exit(2)

        # Write-time divergence: only source-provenanced entries can
        # diverge (live-provenanced ones equal their own hash by
        # construction). Report, never refuse — the write always proceeds.
        source_baseline = {
            rel: sha for rel, (sha, prov) in entries.items() if prov == "source"
        }
        diverged, sanctioned_paths, stale = partition_divergence(
            root, source_baseline, sanctioned
        )

        result = {
            "status": "success",
            "mode": "write",
            "source_mode": source_mode,
            "manifest_path": str(manifest_path.resolve()),
            "entries": len(entries),
            "diverged": diverged,
            "sanctioned": sanctioned_paths,
            "sanction_stale": stale,
        }
        if sanctioned_paths:
            result["sanctioned_summary"] = (
                f"{len(sanctioned_paths)} sanctioned divergences: "
                + ", ".join(sanctioned_paths)
            )
        if source_mode == "live":
            result["warning"] = (
                "source_mode: live — the live skills dir served as the "
                "source, so the net is live-hashed for this write (blind to "
                "any pre-existing local edit)."
            )
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

        missing = [
            rel for rel in sorted(recorded) if not (root / rel).is_file()
        ]
        diverged, sanctioned_paths, stale = partition_divergence(
            root, recorded, sanctioned
        )

        result = {
            "status": "success",
            "mode": "verify",
            "manifest_path": str(manifest_path.resolve()),
            "entries": len(recorded),
            "diverged": diverged,
            "sanctioned": sanctioned_paths,
            "sanction_stale": stale,
            "missing": missing,
        }
        if sanctioned_paths:
            result["sanctioned_summary"] = (
                f"{len(sanctioned_paths)} sanctioned divergences: "
                + ", ".join(sanctioned_paths)
            )
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
