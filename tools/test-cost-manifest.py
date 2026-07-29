#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Test harness for tools/cost-manifest.py (build B5-1).

Builds a minimal synthetic vault fixture in a temp dir (placeholder content
only — this repo is public), exercises vault mode against it with exact-size
assertions, runs the module-mode self-check against the real repo (ground
truth computed by this harness's own walk — never hardcoded figures, which
would fossilize HEAD's numbers), and asserts both modes are deterministic.

Usage: uv run tools/test-cost-manifest.py
Exit: 0 = all cases green; non-zero otherwise.
"""

import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TOOL = REPO / "tools/cost-manifest.py"

# Fixture {log}: known headers, including the tolerant-parser edge cases —
# mixed case, paren-less generic op, bracket-swallowed type+partner, and a
# non-header "## " line that must NOT match.
FIXTURE_LOG = """\
# Log

## [2026-01-01 09:00] ingest (librarian) | filed a source → [[wiki/topic]]
## [2026-01-02 10:00] INGEST (Librarian) | mixed-case header, same partner
## [2026-01-03 11:00] lint | paren-less generic-op header
## [2026-01-04 track (coach)] | bracket-swallowed type and partner
## [see also] this line is not an entry header and must not match
## Not an entry either
## [2026-01-05 12:00] session (researcher) | fifth real entry
## [2026-01-06 13:00] query (researcher) | sixth real entry
"""

FIXTURE_CONFIG = """\
document_output_language: English
vlt:
  name: Vault
  description: A placeholder description that folds
    across two lines like the installer writes it.
  version: 0.0.0
  vault_structure:
    wiki: _agent/wiki/
    index: _agent/wiki/index.md
    research: _agent/research/
    log: _agent/log.md
    backlog: _agent/backlog.md
    partners: _agent/partners/
    conventions: _meta/conventions/
    overlays: _agent/conventions/
"""
# Deliberately missing from the fixture map (must fall back to the canonical
# default and be NAMED in the report): sessions, specs, capabilities,
# personas, contract, upgrade_ledger, archive.
EXPECTED_FALLBACKS = {"archive", "capabilities", "contract", "personas",
                      "sessions", "specs", "upgrade_ledger"}


def build_fixture(root: Path) -> dict:
    """Synthetic vault; returns expected byte sizes keyed by logical surface."""
    (root / "_bmad").mkdir(parents=True)
    (root / "_bmad/config.yaml").write_text(FIXTURE_CONFIG, encoding="utf-8")
    (root / "_agent/wiki").mkdir(parents=True)
    (root / "_agent/partners/alpha/capabilities").mkdir(parents=True)
    (root / "_agent/partners/beta").mkdir(parents=True)
    (root / "_agent/conventions").mkdir(parents=True)
    (root / "_agent/sessions").mkdir(parents=True)
    (root / "_meta/conventions").mkdir(parents=True)
    (root / ".claude/workflows").mkdir(parents=True)

    files = {
        "log": ("_agent/log.md", FIXTURE_LOG),
        "index": ("_agent/wiki/index.md", "# Index\n- [[topic]]\n"),
        "backlog": ("_agent/backlog.md", "## Open\n- an item\n## Done\n"),
        "dispatch": ("_agent/dispatch.md", "## alpha\n- [ ] a handed-off item\n"),
        "alpha_identity": ("_agent/partners/alpha/identity.md", "name: Alpha\n## Bond\n## Self\n"),
        "alpha_thread": ("_agent/partners/alpha/thread.md", "## Thread\nopen inquiry\n"),
        "alpha_cap": ("_agent/partners/alpha/capabilities/cap-one.md", "# A capability\nsteps\n"),
        "beta_identity": ("_agent/partners/beta/identity.md", "name: Beta\n## Bond\n## Self\n"),
        "beta_thread": ("_agent/partners/beta/thread.md", "## Thread\nquiet\n"),
        "convention": ("_meta/conventions/frontmatter.md", "# Frontmatter\nfields\n"),
        "overlay": ("_agent/conventions/local-rule.md", "# Local addition\n"),
        "workflow": (".claude/workflows/vlt-thing.js", "const args = JSON.parse(input);\n"),
        "session": ("_agent/sessions/2026-01-01-090000-ingest.md", "session note body\n"),
    }
    sizes = {}
    for key, (rel, content) in files.items():
        p = root / rel
        p.write_text(content, encoding="utf-8")
        sizes[key] = len(content.encode("utf-8"))
    return sizes


def run(*args) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["uv", "run", str(TOOL), *args], capture_output=True, text=True
    )


CASES = []


def case(name):
    def register(fn):
        CASES.append((name, fn))
        return fn
    return register


@case("1. vault mode: exact sizes, entry counts, tolerant-parser edges")
def case_vault_fixture(root, sizes, out):
    # Exact sizes surface in the report (comma-formatted).
    for key, label in [("index", "index.md"), ("backlog", "backlog.md")]:
        assert f"| {sizes[key]:,} |" in out, f"{label} size {sizes[key]} not in report"
    assert f"(full) | {len(FIXTURE_LOG.encode()):,} |" in out.replace("_agent/log.md ", ""), \
        f"log full size {len(FIXTURE_LOG.encode())} not in report"
    # 6 real entries: the two "## " non-headers must not count; the
    # mixed-case, paren-less, and bracket-swallowed ones must.
    assert "Total entries: **6**" in out, out
    # Counts by type: two ingests (case-folded together), one each else.
    assert "ingest: **2**" in out, out
    for frag in ["lint: 1", "query: 1", "session: 1", "track: 1"]:
        assert frag in out, f"missing type count {frag!r}\n{out}"
    # Counts by partner: librarian case-folded to 2; the paren-less op is partner-less.
    assert "librarian: 2" in out and "coach: 1" in out and "researcher: 2" in out, out
    assert "(none — partner-less generic op): 1" in out, out
    assert "First entry: 2026-01-01 — last entry: 2026-01-06" in out, out
    # Last-5 slice: from the 5th-from-last entry header ("## [2026-01-02 ...")
    # to EOF — includes the non-header lines between entries.
    slice_start = FIXTURE_LOG.index("## [2026-01-02")
    expected_slice = len(FIXTURE_LOG[slice_start:].encode("utf-8"))
    assert f"slice — the contract's recency read) | {expected_slice:,} |" in out, out


@case("2. vault mode: missing structure-map keys fall back, each NAMED")
def case_fallbacks(root, sizes, out):
    named = set(re.findall(r"^- `([\w-]+)` → `.*` \(fallback\)$", out, re.M))
    assert named == EXPECTED_FALLBACKS, f"fallbacks named {named} != expected {EXPECTED_FALLBACKS}"
    # Keys present in the vault map must not be reported as fallbacks.
    assert "`log` →" not in out and "`wiki` →" not in out, out


@case("3. vault mode: partner memory covers both partners, capabilities counted")
def case_partners(root, sizes, out):
    alpha_total = sizes["alpha_identity"] + sizes["alpha_thread"] + sizes["alpha_cap"]
    beta_total = sizes["beta_identity"] + sizes["beta_thread"]
    assert f"| alpha (identity+thread, capabilities/ ×1) | {alpha_total:,} |" in out, out
    assert f"| beta (identity+thread) | {beta_total:,} |" in out, out


@case("4. vault mode: installed governance + workflows + sessions context")
def case_governance(root, sizes, out):
    assert f"| {sizes['convention']:,} |" in out, out
    assert f"| {sizes['overlay']:,} |" in out, out
    assert f"| {sizes['workflow']:,} |" in out, out
    assert f"- 1 files, {sizes['session']:,} bytes total" in out, out


@case("5. vault with no _bmad/config.yaml -> clear error, exit nonzero")
def case_missing_config(root, sizes, out):
    with tempfile.TemporaryDirectory() as tmp:
        r = run("--vault", tmp)
        assert r.returncode != 0, "expected nonzero exit"
        assert "no _bmad/config.yaml" in r.stderr, r.stderr


@case("6. module-mode self-check: named aggregates equal a fresh walk")
def case_module_self_check(root, sizes, out):
    r = run("--module")
    assert r.returncode == 0, r.stderr
    report = r.stdout
    gov = REPO / "skills/vlt-setup/assets/governance/_meta"
    truth = {
        "contract": (gov / "vault-operating-contract.md").stat().st_size,
        "lint SKILL": (REPO / "skills/vlt-lint/SKILL.md").stat().st_size,
        "dispatch SKILL": (REPO / "skills/vlt-dispatch/SKILL.md").stat().st_size,
        "conventions total": sum(p.stat().st_size for p in gov.glob("conventions/*.md")),
        "frontmatter.md": (gov / "conventions/frontmatter.md").stat().st_size,
        "all-SKILL.md total": sum(p.stat().st_size for p in REPO.glob("skills/*/SKILL.md")),
    }
    agg = report[report.index("## Named aggregates"):]
    for name, expected in truth.items():
        m = re.search(rf"^\| \*?\*?{re.escape(name)}\*?\*? \| \*?\*?([\d,]+)", agg, re.M)
        assert m, f"aggregate {name!r} missing from report"
        got = int(m.group(1).replace(",", ""))
        assert got == expected, f"{name}: report says {got}, walk says {expected}"


@case("7. determinism: two consecutive runs byte-identical, each mode")
def case_determinism(root, sizes, out):
    for args in (["--module"], ["--vault", str(root)]):
        a, b = run(*args), run(*args)
        assert a.returncode == b.returncode == 0, a.stderr + b.stderr
        assert a.stdout == b.stdout, f"non-deterministic output for {args}"


def main():
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        sizes = build_fixture(root)
        r = run("--vault", str(root))
        assert r.returncode == 0, f"vault mode failed on fixture:\n{r.stdout}{r.stderr}"
        out = r.stdout
        for name, fn in CASES:
            try:
                fn(root, sizes, out)
                print(f"PASS  {name}")
            except AssertionError as e:
                failures += 1
                print(f"FAIL  {name}\n      {e}")
    total = len(CASES)
    print(f"test-cost-manifest: {total - failures}/{total} cases green")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
