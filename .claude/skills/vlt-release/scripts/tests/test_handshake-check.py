#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml", "pytest"]
# ///
"""Tests for handshake-check.py. Run: uv run scripts/tests/test_handshake.py"""

import importlib.util
import sys
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "handshake_check", Path(__file__).resolve().parent.parent / "handshake-check.py"
)
hc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hc)


def make_convention(root: Path, name: str, version, consumers):
    d = root / "skills/vlt-setup/assets/governance/_meta/conventions"
    d.mkdir(parents=True, exist_ok=True)
    consumers_yaml = "[" + ", ".join(consumers) + "]"
    (d / f"{name}.md").write_text(
        f"---\ntitle: {name}\nversion: {version}\nconsumers: {consumers_yaml}\n---\nbody\n",
        encoding="utf-8",
    )


def make_skill(root: Path, name: str, depends_on):
    d = root / "skills" / name
    d.mkdir(parents=True, exist_ok=True)
    deps_yaml = "[" + ", ".join(f'"{x}"' for x in depends_on) + "]"
    (d / "SKILL.md").write_text(
        f"---\nname: {name}\ndepends_on: {deps_yaml}\n---\nbody\n", encoding="utf-8"
    )


def test_consistent_passes(tmp_path):
    make_convention(tmp_path, "frontmatter", 3, ["vlt-ingest", "vlt-mint"])
    make_skill(tmp_path, "vlt-ingest", ["frontmatter@3"])
    make_skill(tmp_path, "vlt-mint", ["frontmatter@3"])
    assert hc.check(tmp_path) == []


def test_stale_ack_fails_both_directions(tmp_path):
    # Convention bumped to 3, consumer still pins @2 — the exact bite the gate exists for.
    make_convention(tmp_path, "frontmatter", 3, ["vlt-ingest"])
    make_skill(tmp_path, "vlt-ingest", ["frontmatter@2"])
    failures = hc.check(tmp_path)
    assert any("stale ack" in f and "forward" in f for f in failures)
    assert any("stale ack" in f and "reverse" in f for f in failures)


def test_consumer_missing_the_pin(tmp_path):
    # Convention lists vlt-lint, but vlt-lint's depends_on omits it.
    make_convention(tmp_path, "extraction", 2, ["vlt-lint"])
    make_skill(tmp_path, "vlt-lint", [])
    failures = hc.check(tmp_path)
    assert any("does not pin 'extraction'" in f for f in failures)


def test_depends_on_convention_not_listing_skill(tmp_path):
    # Skill pins the convention, but the convention's consumers omit the skill.
    make_convention(tmp_path, "spec", 1, ["vlt-mint"])
    make_skill(tmp_path, "vlt-mint", ["spec@1"])
    make_skill(tmp_path, "vlt-dispatch", ["spec@1"])
    failures = hc.check(tmp_path)
    assert any("vlt-dispatch" in f and "does not include" in f for f in failures)


def test_depends_on_unknown_convention(tmp_path):
    make_convention(tmp_path, "spec", 1, ["vlt-mint"])
    make_skill(tmp_path, "vlt-mint", ["spec@1", "ghost@1"])
    failures = hc.check(tmp_path)
    assert any("no such convention exists" in f for f in failures)


def test_malformed_depends_on_entry(tmp_path):
    make_convention(tmp_path, "spec", 1, ["vlt-mint"])
    make_skill(tmp_path, "vlt-mint", ["spec@1", "no-at-sign"])
    failures = hc.check(tmp_path)
    assert any("malformed depends_on entry" in f for f in failures)


def test_consumer_listed_but_skill_absent(tmp_path):
    make_convention(tmp_path, "spec", 1, ["vlt-mint", "vlt-gone"])
    make_skill(tmp_path, "vlt-mint", ["spec@1"])
    failures = hc.check(tmp_path)
    assert any("vlt-gone" in f and "was not found" in f for f in failures)


def test_real_repo_head_is_consistent(tmp_path):
    # Ground against the actual repo: HEAD must be bipartite-consistent.
    repo = Path(__file__).resolve().parents[5]
    if not (repo / hc.CONVENTIONS_GLOB.split("*")[0]).exists():
        pytest.skip("not running inside the module repo")
    assert hc.check(repo) == []


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
