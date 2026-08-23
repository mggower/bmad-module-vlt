#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""Version-handshake bipartite consistency check (vlt-release stage 2).

The factory-side handshake, mechanized. A convention in the governance bundle
carries `version:`/`consumers:`; each consumer skill carries a flat
`depends_on: ["name@version"]`. A release must never ship a stale ack, so this
asserts the two sides agree in BOTH directions:

  forward  — every convention's listed consumer pins that convention at its
             current version in its own depends_on
  reverse  — every depends_on entry names a real convention, pins its current
             version (not a stale one), and that convention lists the skill

The vault-operating-contract is deliberately NOT handshaked (single-home +
pointers instead); it lives at governance/_meta/ top level, so scanning only
conventions/*.md naturally excludes it.

Usage: uv run scripts/handshake-check.py [--root PATH]
Exit: 0 = bipartite-consistent; 1 = any mismatch (with a per-mismatch report).
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

CONVENTIONS_GLOB = "skills/vlt-setup/assets/governance/_meta/conventions/*.md"
CONSUMERS_GLOB = "skills/vlt-*/SKILL.md"
WORKFLOWS_DIR = "skills/vlt-setup/assets/workflows"
DEP_RE = re.compile(r"^(?P<name>[^@]+)@(?P<version>.+)$")
DEPENDS_ON_LINE_RE = re.compile(r"^\s*//\s*depends_on:\s*(\[.*\])\s*$")


def is_asset_node(consumer: str) -> bool:
    """Mirror of package-lint's _is_asset_node (B7-6): a consumers: entry ending
    .js is a workflow-asset node resolving against skills/vlt-setup/assets/workflows/,
    acked by the file's single `// depends_on: [...]` header, not a SKILL.md."""
    return str(consumer).endswith(".js")


def load_asset_consumers(root: Path) -> dict:
    """{workflow_filename: [(dep_name, dep_version_str_or_None, raw), ...]}.
    A file with zero or multiple depends_on headers maps to None (malformed —
    absence must be loud, matching package-lint E5)."""
    assets = {}
    wf_dir = root / WORKFLOWS_DIR
    for wf in sorted(wf_dir.glob("*.js")) if wf_dir.is_dir() else []:
        matches = [
            m for line in wf.read_text(encoding="utf-8").splitlines()
            for m in [DEPENDS_ON_LINE_RE.match(line)] if m
        ]
        if len(matches) != 1:
            assets[wf.name] = None
            continue
        try:
            raw_pins = json.loads(matches[0].group(1))
            assert isinstance(raw_pins, list) and all(isinstance(p, str) for p in raw_pins)
        except Exception:
            assets[wf.name] = None
            continue
        deps = []
        for raw in raw_pins:
            m = DEP_RE.match(raw)
            deps.append((m.group("name"), m.group("version"), raw) if m else (None, None, raw))
        assets[wf.name] = deps
    return assets


def frontmatter(path: Path) -> dict:
    """Parse the YAML frontmatter block (between the first two --- fences)."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    return yaml.safe_load(parts[1]) or {}


def load_conventions(root: Path) -> dict:
    """{convention_name: (version_str, [consumer_skill, ...])}. Name = filename stem."""
    conventions = {}
    for path in sorted(root.glob(CONVENTIONS_GLOB)):
        fm = frontmatter(path)
        conventions[path.stem] = (str(fm.get("version")), list(fm.get("consumers") or []))
    return conventions


def load_consumers(root: Path) -> dict:
    """{skill_name: [(dep_name, dep_version_str_or_None, raw), ...]}. Skill = dir name."""
    consumers = {}
    for path in sorted(root.glob(CONSUMERS_GLOB)):
        skill = path.parent.name
        deps = []
        for raw in frontmatter(path).get("depends_on") or []:
            m = DEP_RE.match(str(raw))
            deps.append((m.group("name"), m.group("version"), str(raw)) if m else (None, None, str(raw)))
        consumers[skill] = deps
    return consumers


def check(root: Path) -> list:
    conventions = load_conventions(root)
    consumers = load_consumers(root)
    assets = load_asset_consumers(root)
    failures = []

    # Forward: every convention's consumer pins it at the current version.
    for name, (version, listed) in conventions.items():
        for skill in listed:
            if is_asset_node(skill):
                deps = assets.get(skill)
                if deps is None:
                    failures.append(
                        f"forward: convention '{name}' lists asset consumer '{skill}', but "
                        f"{WORKFLOWS_DIR}/{skill} is missing or lacks exactly one parseable "
                        f"`// depends_on: [...]` header"
                    )
                    continue
                pinned = {n: v for n, v, _ in deps if n is not None}
                if name not in pinned:
                    failures.append(
                        f"forward: convention '{name}' lists asset '{skill}' as a consumer, "
                        f"but its depends_on header does not pin '{name}'"
                    )
                elif pinned[name] != version:
                    failures.append(
                        f"forward: asset '{skill}' pins {name}@{pinned[name]} but the "
                        f"convention is at version {version} (stale ack)"
                    )
                continue
            if skill not in consumers:
                failures.append(
                    f"forward: convention '{name}' lists consumer '{skill}', but "
                    f"skills/{skill}/SKILL.md was not found"
                )
                continue
            pinned = {n: v for n, v, _ in consumers[skill] if n is not None}
            if name not in pinned:
                failures.append(
                    f"forward: convention '{name}' lists '{skill}' as a consumer, "
                    f"but {skill}'s depends_on does not pin '{name}'"
                )
            elif pinned[name] != version:
                failures.append(
                    f"forward: '{skill}' pins {name}@{pinned[name]} but the convention "
                    f"is at version {version} (stale ack)"
                )

    # Reverse: every depends_on entry names a real convention at its current
    # version, and that convention lists the skill back.
    for skill, deps in consumers.items():
        for name, version, raw in deps:
            if name is None:
                failures.append(f"reverse: '{skill}' has malformed depends_on entry '{raw}' (expected name@version)")
                continue
            if name not in conventions:
                failures.append(f"reverse: '{skill}' depends on '{name}@{version}', but no such convention exists")
                continue
            conv_version, listed = conventions[name]
            if version != conv_version:
                failures.append(
                    f"reverse: '{skill}' pins {name}@{version} but the convention "
                    f"is at version {conv_version} (stale ack)"
                )
            if skill not in listed:
                failures.append(
                    f"reverse: '{skill}' depends on '{name}', but '{name}'s "
                    f"consumers list does not include '{skill}'"
                )

    # Reverse (asset leg): every workflow header parses, and every pin names a
    # real convention at its current version whose consumers list the asset.
    for asset, deps in assets.items():
        if deps is None:
            failures.append(
                f"reverse: {WORKFLOWS_DIR}/{asset} lacks exactly one parseable "
                f"`// depends_on: [...]` header — absence must be loud"
            )
            continue
        for name, version, raw in deps:
            if name is None:
                failures.append(f"reverse: asset '{asset}' has malformed depends_on entry '{raw}'")
                continue
            if name not in conventions:
                failures.append(f"reverse: asset '{asset}' depends on '{name}@{version}', but no such convention exists")
                continue
            conv_version, listed = conventions[name]
            if version != conv_version:
                failures.append(
                    f"reverse: asset '{asset}' pins {name}@{version} but the convention "
                    f"is at version {conv_version} (stale ack)"
                )
            if asset not in listed:
                failures.append(
                    f"reverse: asset '{asset}' depends on '{name}', but '{name}'s "
                    f"consumers list does not include '{asset}'"
                )

    return failures


def main():
    parser = argparse.ArgumentParser(description="Version-handshake bipartite consistency check.")
    parser.add_argument("--root", default=None, help="Repo root to check (default: current directory)")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd()

    conventions = load_conventions(root)
    consumers = load_consumers(root)
    assets = load_asset_consumers(root)
    pin_count = sum(1 for deps in consumers.values() for n, _, _ in deps if n is not None)
    pin_count += sum(1 for deps in assets.values() if deps for n, _, _ in deps if n is not None)

    failures = check(root)
    if failures:
        print(f"FAIL handshake — {len(failures)} mismatch(es):")
        for f in failures:
            print(f"  - {f}")
        print("handshake: FAIL — a release must never ship a stale ack")
        sys.exit(1)

    print(f"handshake: {len(conventions)} conventions, {pin_count} consumer pins — bipartite-consistent")


if __name__ == "__main__":
    main()
