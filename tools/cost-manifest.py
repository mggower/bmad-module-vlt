#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Cost manifest for the vlt module (build B5-1) — the module's sizing instrument.

Read-only in both modes; writes nothing but stdout. Output is a markdown report
with stable section order and stable within-section sort (size desc, ties by
path), so two runs diff cleanly. No thresholds, no baselines, no judgments —
this instrument measures and reports; enforcement vocabulary is B5-9's.

Honest limit (pre-ideation ruling 3): the tool sizes the DECLARED read surface
in bytes on disk and estimates tokens from two crude estimators; it does not
observe what a live session actually read (that would be A5-13 disposition (b),
unbuilt).

Modes:
  module mode (default, or --module) — sizes the declared read surface from
      module source at rest: per-partner fixed boot, governance stock, skill
      surface, workflow assets, named aggregates.
  vault mode (--vault /path/to/vault) — sizes an installed vault's
      field-variable surfaces: structure-map-resolved beat-2 reads, installed
      governance, {log} derivations, session context.

Usage: uv run tools/cost-manifest.py [--module | --vault /path/to/vault] [--root PATH]
Exit: 0 = report produced; 2 = error (e.g. vault has no _bmad/config.yaml).
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# SHARED MEASUREMENT SUBSTRATE (arc-5 pre-ideation ruling 1)
#
# The one derive-only reader over existing vault records. B5-9's enforcement-
# kit vitals EXTEND these functions; they never lay a second substrate. Homed
# in tools/ for now — the module-owned-code-home question (A5-19 Q1) re-opens
# at B5-9's brief and is deliberately not answered here.
# ---------------------------------------------------------------------------

# Tolerant {log} header parser, per the contract's canonical entry grammar
# (vault-operating-contract.md "The {log} — chronological record"):
#   ## [YYYY-MM-DD HH:MM] <type> (<partner>) | <summary> [→ <artifacts>]
# Tolerances (A5-19's residual probe: strict parsing drops ~5% of real
# headers): case-insensitive type; paren optional (omittable for partner-less
# generic operations per the contract). The trailing "|" stays required so a
# non-header "## " line cannot match.
LOG_HEADER_RE = re.compile(
    r"^##\s*\[([^\]]+)\]\s*([A-Za-z][A-Za-z0-9_-]*)\s*(?:\(\s*([^)]*?)\s*\))?\s*\|",
    re.IGNORECASE,
)
# Fallback shape seen in real logs: the bracket swallowed type and partner —
# `## [2026-07-18 track (chess-coach)] | …`. The type must start with a letter,
# so a well-formed `[YYYY-MM-DD HH:MM]` bracket can never match this one.
LOG_HEADER_FALLBACK_RE = re.compile(
    r"^##\s*\[([^\]\s]+(?:\s+[^\]\s]+)*?)\s+([A-Za-z][A-Za-z0-9_-]*)\s*(?:\(\s*([^)]*?)\s*\))?\s*\]\s*\|",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def parse_log_entries(text):
    """Parse {log} text -> list of entries, file order (the log is append-only).

    Each entry: {"date": "YYYY-MM-DD" or None, "type": lowercased str,
    "partner": lowercased str or None, "start": char offset of the header}.
    Derive-only: no thresholds, no judgments.
    """
    entries = []
    offset = 0
    for line in text.splitlines(keepends=True):
        m = LOG_HEADER_RE.match(line) or LOG_HEADER_FALLBACK_RE.match(line)
        if m:
            date_m = DATE_RE.search(m.group(1))
            partner = m.group(3)
            entries.append(
                {
                    "date": date_m.group(0) if date_m else None,
                    "type": m.group(2).lower(),
                    "partner": partner.strip().lower() if partner and partner.strip() else None,
                    "start": offset,
                }
            )
        offset += len(line)
    return entries


def parse_block_map(lines, section_path):
    """Extract a flat `key: value` block map nested under section_path.

    A deliberately narrow YAML-subset reader (stdlib-only) for the two
    installer-materialized shapes this tool needs: `vlt.vault_structure` in a
    vault's _bmad/config.yaml and `vault_structure.default` in module.yaml.
    Walks indentation; skips blanks/comments; strips quotes. Returns {} if the
    section is absent.
    """
    depth = 0
    section_indent = -1
    result = {}
    in_target = False
    for raw in lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip())
        stripped = raw.strip()
        if in_target:
            if indent <= section_indent:
                break
            m = re.match(r"^([A-Za-z_][\w-]*):\s*(\S.*)$", stripped)
            if m:
                result[m.group(1)] = m.group(2).strip().strip("'\"")
            continue
        if indent <= section_indent:
            # left the section we were descending through
            depth = 0 if indent == 0 else depth
            section_indent = -1 if indent == 0 else section_indent
        want = section_path[depth]
        if stripped == f"{want}:" or stripped.startswith(f"{want}:"):
            if depth == len(section_path) - 1:
                in_target = True
                section_indent = indent
            else:
                depth += 1
                section_indent = indent
    return result


def resolve_structure_map(vault_root, module_root):
    """Resolve a vault's structure map: vault config first, canonical default
    (module.yaml vault_structure.default — the SSoT) for any missing key.

    Returns (map, fallback_keys). Raises FileNotFoundError if the vault has no
    _bmad/config.yaml at all (not a vlt install — a hard error, never a silent
    all-defaults guess).
    """
    config = vault_root / "_bmad" / "config.yaml"
    if not config.is_file():
        raise FileNotFoundError(
            f"no _bmad/config.yaml under {vault_root} — not an installed vault"
        )
    vault_map = parse_block_map(
        config.read_text(encoding="utf-8", errors="replace").splitlines(),
        ["vlt", "vault_structure"],
    )
    default_map = parse_block_map(
        (module_root / "skills/vlt-setup/assets/module.yaml")
        .read_text(encoding="utf-8", errors="replace")
        .splitlines(),
        ["vault_structure", "default"],
    )
    resolved, fallbacks = {}, []
    for key in sorted(set(default_map) | set(vault_map)):
        if key in vault_map:
            resolved[key] = vault_map[key]
        else:
            resolved[key] = default_map[key]
            fallbacks.append(key)
    return resolved, fallbacks


# ---------------------------------------------------------------------------
# Sizing + report rendering
# ---------------------------------------------------------------------------


def measure_text(text):
    """(bytes, words, band_lo, band_hi) for a decoded text."""
    n_bytes = len(text.encode("utf-8"))
    words = len(text.split())
    return n_bytes, words, round(words * 1.3), round(n_bytes / 4)


def measure_file(path):
    if not path.is_file():
        return None
    return measure_text(path.read_text(encoding="utf-8", errors="replace"))


def sum_rows(rows):
    """Sum (bytes, words) across rows and derive the band from the sums."""
    n_bytes = sum(r[1] for r in rows)
    words = sum(r[2] for r in rows)
    return n_bytes, words, round(words * 1.3), round(n_bytes / 4)


def fmt_band(lo, hi):
    return f"~{lo:,}–{hi:,}"


def table(rows, total_label=None):
    """Render rows of (label, bytes, words, lo, hi) as a markdown table."""
    out = [
        "| surface | bytes | words | est. tokens |",
        "| --- | ---: | ---: | ---: |",
    ]
    for label, n_bytes, words, lo, hi in rows:
        out.append(f"| {label} | {n_bytes:,} | {words:,} | {fmt_band(lo, hi)} |")
    if total_label is not None and rows:
        t = sum_rows(rows)
        out.append(f"| **{total_label}** | **{t[0]:,}** | **{t[1]:,}** | **{fmt_band(t[2], t[3])}** |")
    return "\n".join(out)


def sized_rows(paths, root, absent_note=" (absent)"):
    """(label, ...) rows for files, sorted size desc, ties by path. Absent files
    render as zero-size rows tagged absent — visible, never silently dropped."""
    rows = []
    for p in paths:
        label = str(p.relative_to(root)) if root else str(p)
        m = measure_file(p)
        if m is None:
            rows.append((label + absent_note, 0, 0, 0, 0))
        else:
            rows.append((label, *m))
    return sorted(rows, key=lambda r: (-r[1], r[0]))


def dir_file_rows(directory, root, pattern="*"):
    """Rows for a directory's top-level files (sorted glob for determinism)."""
    if not directory.is_dir():
        return []
    return sized_rows(sorted(p for p in directory.glob(pattern) if p.is_file()), root)


HONESTY_HEADER = """\
> **What this measures:** the *declared* read surface — file sizes in bytes on
> disk (`wc -c` equivalent) and whitespace-split word counts. **Est. tokens**
> is a band, never one number: `[words × 1.3 … bytes / 4]` — the two
> estimators the arc's captures used, which disagree by ~25% on prose. This
> instrument does **not** observe what a live session actually read (that
> would be a session self-report, deliberately unbuilt — A5-13 disposition
> (b)). It measures and reports; it never nags — thresholds and tripping are
> the enforcement kit's (B5-9)."""


# ---------------------------------------------------------------------------
# Module mode
# ---------------------------------------------------------------------------

# Eager/contingent grouping — encodes, as data, the activation ritual's two
# documented prose homes: every partner opens with a full contract read
# (partner SKILL.md "Become yourself — the two-beat ritual") and the contract's
# "Activation ritual — two beats" section; governance conventions are lazy
# point-of-use reads (partner SKILL "Ending a sitting" reads frontmatter.md at
# need; vlt-lint reads conventions per check). This constant is a soft third
# home of that grouping (brief B5-1, Out of scope 6) — if the prose homes move,
# update it here.
CONTRACT_REL = "skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md"
GOVERNANCE_REL = "skills/vlt-setup/assets/governance/_meta"
WORKFLOWS_REL = "skills/vlt-setup/assets/workflows"


def module_mode(root):
    out = ["# vlt cost manifest — module mode", ""]
    out.append(HONESTY_HEADER)
    out.append("")
    out.append(
        "Module source at rest, measured from the repo root. "
        "Vault-side field-variable surfaces (index/log/orient reads) are the "
        "other half — run `--vault /path/to/vault` for those."
    )

    contract = root / CONTRACT_REL

    # Per-partner fixed boot: SKILL.md + full contract read, per activation.
    out.append("\n## Per-partner fixed boot (eager — paid at every activation)\n")
    out.append(
        "Every partner activation opens with its SKILL.md plus a full "
        "operating-contract read (the two-beat ritual's opener).\n"
    )
    partner_skills = sorted(root.glob("skills/vlt-agent-*/SKILL.md"))
    contract_m = measure_file(contract)
    boot_rows = []
    for skill in partner_skills:
        skill_m = measure_file(skill)
        partner = skill.parent.name
        combined_bytes = skill_m[0] + contract_m[0]
        combined_words = skill_m[1] + contract_m[1]
        boot_rows.append(
            (
                f"{partner} (SKILL.md {skill_m[0]:,} + contract {contract_m[0]:,})",
                combined_bytes,
                combined_words,
                round(combined_words * 1.3),
                round(combined_bytes / 4),
            )
        )
    out.append(table(sorted(boot_rows, key=lambda r: (-r[1], r[0]))))

    # Governance stock: lazy point-of-use reads, contract broken out.
    out.append("\n## Governance stock (lazy — point-of-use reads)\n")
    gov = root / GOVERNANCE_REL
    gov_files = sorted(p for p in gov.rglob("*") if p.is_file())
    conv_rows = sized_rows([p for p in gov_files if p.parent.name == "conventions"], root)
    other_rows = sized_rows(
        [p for p in gov_files if p.parent.name != "conventions" and p != contract], root
    )
    out.append("Conventions (`_meta/conventions/`):\n")
    out.append(table(conv_rows, total_label="conventions total"))
    out.append("\nContract (broken out — it is the eager read above):\n")
    out.append(table(sized_rows([contract], root)))
    if other_rows:
        out.append("\nOther `_meta/` files:\n")
        out.append(table(other_rows, total_label="other _meta total"))
    all_gov = sized_rows(gov_files, root)
    t = sum_rows(all_gov)
    out.append(f"\nGovernance bundle total: **{t[0]:,}** bytes, {t[1]:,} words, {fmt_band(t[2], t[3])} est. tokens.")

    # Skill surface — SKILL.md files only (the capture's correction).
    out.append("\n## Skill surface (SKILL.md files only — not whole skill dirs)\n")
    skill_rows = sized_rows(sorted(root.glob("skills/*/SKILL.md")), root)
    out.append(table(skill_rows, total_label="all SKILL.md total"))

    # Workflow assets.
    out.append("\n## Workflow assets\n")
    wf_rows = dir_file_rows(root / WORKFLOWS_REL, root, "*.js")
    out.append(table(wf_rows, total_label="workflows total"))

    # Named aggregates — the whales the captures track, one diffable block.
    out.append("\n## Named aggregates (the tracked whales — one diff line each)\n")
    agg_rows = []
    for name, m in [
        ("contract", contract_m),
        ("lint SKILL", measure_file(root / "skills/vlt-lint/SKILL.md")),
        ("dispatch SKILL", measure_file(root / "skills/vlt-dispatch/SKILL.md")),
        ("conventions total", sum_rows(conv_rows) if conv_rows else None),
        ("frontmatter.md", measure_file(gov / "conventions/frontmatter.md")),
        ("all-SKILL.md total", sum_rows(skill_rows) if skill_rows else None),
    ]:
        agg_rows.append((name, *m) if m else (name + " (absent)", 0, 0, 0, 0))
    out.append(table(agg_rows))
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Vault mode
# ---------------------------------------------------------------------------


def vault_mode(vault_root, module_root):
    smap, fallbacks = resolve_structure_map(vault_root, module_root)

    def vp(key):
        return vault_root / smap[key].rstrip("/")

    out = ["# vlt cost manifest — vault mode", ""]
    out.append(HONESTY_HEADER)
    out.append("")
    out.append(
        "An installed vault's field-variable surfaces — the half module mode "
        "cannot see. Paths resolve through the vault's own structure map."
    )

    out.append("\n## Structure map resolution\n")
    out.append(f"Read from `_bmad/config.yaml` key `vlt.vault_structure` ({len(smap)} keys).")
    if fallbacks:
        out.append(
            "\nKeys **missing from the vault's map**, resolved from the canonical "
            "default (`module.yaml vault_structure.default`, the SSoT) — named, "
            "never silently defaulted:\n"
        )
        for key in fallbacks:
            out.append(f"- `{key}` → `{smap[key]}` (fallback)")
    else:
        out.append("No fallbacks — the vault's map carries every canonical key.")

    # Beat-2 variable surfaces — the orient reads (contract "Activation ritual",
    # Beat 2), priced per A5-12.
    out.append("\n## Beat-2 variable surfaces (the orient reads)\n")
    log_path = vp("log")
    log_text = (
        log_path.read_text(encoding="utf-8", errors="replace") if log_path.is_file() else ""
    )
    entries = parse_log_entries(log_text)
    rows = sized_rows([vp("index"), vp("backlog")], vault_root)
    if log_path.is_file():
        rows.append((f"{smap['log']} (full)", *measure_text(log_text)))
        start = entries[-5]["start"] if len(entries) >= 5 else (entries[0]["start"] if entries else len(log_text))
        rows.append(
            (
                f"{smap['log']} (last-5-entries slice — the contract's recency read)",
                *measure_text(log_text[start:]),
            )
        )
    else:
        rows.append((f"{smap['log']} (absent)", 0, 0, 0, 0))
    dispatch = vault_root / "_agent/dispatch.md"  # fixed home per the contract
    dm = measure_file(dispatch)
    if dm:
        rows.append(
            (
                "_agent/dispatch.md (full — a partner reads only its open slice, "
                "but the slice is semantic; file size is the honest measurable)",
                *dm,
            )
        )
    else:
        rows.append(("_agent/dispatch.md (absent)", 0, 0, 0, 0))
    out.append(table(sorted(rows, key=lambda r: (-r[1], r[0]))))

    # Per-partner memory: identity + thread + capabilities.
    out.append("\n### Per-partner memory (identity.md + thread.md + capabilities/)\n")
    partners_dir = vp("partners")
    partner_rows = []
    if partners_dir.is_dir():
        for pdir in sorted(p for p in partners_dir.iterdir() if p.is_dir()):
            files = [pdir / "identity.md", pdir / "thread.md"]
            caps = pdir / "capabilities"
            cap_files = sorted(p for p in caps.rglob("*") if p.is_file()) if caps.is_dir() else []
            measured = [measure_file(f) for f in files]
            parts = [m for m in measured if m] + [measure_file(f) for f in cap_files]
            parts = [m for m in parts if m]
            n_bytes = sum(m[0] for m in parts)
            words = sum(m[1] for m in parts)
            cap_note = f", capabilities/ ×{len(cap_files)}" if cap_files else ""
            partner_rows.append(
                (
                    f"{pdir.name} (identity+thread{cap_note})",
                    n_bytes,
                    words,
                    round(words * 1.3),
                    round(n_bytes / 4),
                )
            )
    out.append(table(sorted(partner_rows, key=lambda r: (-r[1], r[0])), total_label="partner memory total"))

    # Installed governance.
    out.append("\n## Installed governance\n")
    out.append("Conventions (`{conventions}`):\n")
    out.append(table(dir_file_rows(vp("conventions"), vault_root), total_label="conventions total"))
    out.append("\nOverlays (`{overlays}` — top-level files only; `.baseline/` stock copies are upgrade machinery, not a read surface):\n")
    overlay_rows = dir_file_rows(vp("overlays"), vault_root)
    out.append(table(overlay_rows, total_label="overlays total") if overlay_rows else "*(no overlay files)*")
    out.append("\nWorkflows (`.claude/workflows/*.js`):\n")
    wf_rows = dir_file_rows(vault_root / ".claude/workflows", vault_root, "*.js")
    out.append(table(wf_rows, total_label="workflows total") if wf_rows else "*(no workflow files)*")

    # {log} derivations — the substrate seed. Derive-only display.
    out.append("\n## `{log}` derivations (derive-only — no thresholds, no judgments)\n")
    out.append(f"- Total entries: **{len(entries)}**")
    by_type = {}
    by_partner = {}
    for e in entries:
        by_type[e["type"]] = by_type.get(e["type"], 0) + 1
        key = e["partner"] or "(none — partner-less generic op)"
        by_partner[key] = by_partner.get(key, 0) + 1
    # `ingest` printed explicitly even at zero — the "several ingestions since
    # the last lint" reflex finally has a counter behind it.
    out.append(f"- By type: ingest: **{by_type.get('ingest', 0)}**"
               + "".join(f", {t}: {n}" for t, n in sorted(by_type.items()) if t != "ingest"))
    out.append("- By partner: " + (", ".join(f"{p}: {n}" for p, n in sorted(by_partner.items())) or "(none)"))
    dates = [e["date"] for e in entries if e["date"]]
    if dates:
        out.append(f"- First entry: {dates[0]} — last entry: {dates[-1]}")
    else:
        out.append("- First/last entry dates: (no dated headers parsed)")

    # Context: sessions are not a boot read.
    out.append("\n## Context — `{sessions}` (not a boot read)\n")
    sessions = vp("sessions")
    if sessions.is_dir():
        sfiles = sorted(p for p in sessions.rglob("*") if p.is_file())
        total = sum(p.stat().st_size for p in sfiles)
        out.append(f"- {len(sfiles)} files, {total:,} bytes total")
    else:
        out.append("- (absent)")
    out.append("")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "vlt cost manifest — sizes what a partner session reads. Module mode "
            "(default) sizes the declared read surface from module source; vault "
            "mode (--vault /path/to/vault) sizes an installed vault's "
            "field-variable surfaces. Read-only; markdown report to stdout; "
            "stable ordering so two runs diff cleanly."
        )
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--module", action="store_true", help="module mode (the default)")
    mode.add_argument("--vault", metavar="PATH", help="vault mode: an installed vault's root, e.g. /path/to/vault")
    parser.add_argument("--root", default=None, help="module repo root (default: this script's repo)")
    args = parser.parse_args()

    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent

    try:
        if args.vault:
            print(vault_mode(Path(args.vault).resolve(), root))
        else:
            print(module_mode(root))
    except FileNotFoundError as e:
        print(f"cost-manifest: error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
