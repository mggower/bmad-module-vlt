---
title: 'vlt-core 0.12.0 → 0.13.0 upgrade — Step-4 report (verbatim hand-save)'
date: '2026-08-21'
posture: 'A1 interim evidence posture (roundtable 2026-08-21, owner-ruled) — the owner
  hand-saved this report verbatim at upgrade time; the last transcript-regime run.
  B10-6 retires this posture; its E2 census names this file as a migration input.'
provenance: 'Pasted verbatim by the owner into the factory session 2026-08-21, saved
  same turn. Report body below is unedited.'
---

**vlt 0.12.0 → 0.13.0 upgraded** (own-the-apply, from your local module tree @ `a3ec505`). Committed as `033f9d9`; the pre-existing football-analyst source relocation was committed first as `7b93da8`.

```yaml
upgrade:
  from_version: 0.12.0
  to_version: 0.13.0
  apply_path: own
  mints_preserved: [vlt-agent-career-strategist, vlt-agent-chef, vlt-agent-chess-coach,
                    vlt-agent-dog-trainer, vlt-agent-football-analyst, vlt-agent-health-coach, vlt-sweep]
  bodies_restored: []                     # nothing was deleted
  overlays_intact: [frontmatter.overlay.md]   # reshaped by ruling; no consumers: line, so no retirement annotation
  local_conventions_intact: []            # none exist
  baselines_refreshed: [consult, decision-log, extraction, frontmatter, spec,
                        wiki-consolidation, wiki-index, wiki-supersession, write-verification]
  base_divergence: []                     # all 4 live-vs-baseline diffs were declared vault-writable fields, carried forward
  vault_writable_collisions: []
  skill_asset_divergence: []              # 67 entries, diverged/missing/added/removed all empty, source_mode: source
  migrations_run: [decision-log-write ×3, decision-log-reconcile]
  governance_divergence: []               # contract diff was 100% upstream text; personas byte-identical
  convention_adoption:
    - spec — adopted 2026-06-13
    - decision-log — adopted 2026-07-30
    - consult — declared, no first instance yet (created 2026-07-26 — 26 days)
    - wiki-consolidation — declared, no first instance yet (created 2026-06-01 — 81 days)
    - extraction, frontmatter, wiki-index, wiki-supersession, write-verification — axis not declared
  capabilities_intact: [23 light capabilities across 9 partners; families/ empty]
  family_invariant_drift: []
```

**Three rulings you approved, all written through to `_agent/mint/decision-log.md`** (32 → 35 entries), not the ledger alone:
1. `frontmatter.overlay.md` reshaped to frontmatter@11 per-section enforcement addressing — six keys moved verbatim under `## A`, no value changed.
2. `_agent/reflexes.md` (the new vault rung) seeded and given its first pointer line for the pre-existing overlay.
3. `_agent/tripwires.yaml` header refreshed for the `local_metrics:` schema — all 4 wires and thresholds verified data-identical by parse-and-compare.

**Two things worth your attention:**
- **Decision-log classifiability tail** — 12 entries can't be mechanically classified (7 pre-schema, 5 with `kind:` but no `ref:`). Append-only forbids backfill, so this is permanent; all 12 are named in the ledger Notes rather than swept.
- **Standing tripwires still ring** — `relay-overdue` (26 days) and `drain-due` (47 days). Vault hygiene, not upgrade artifacts: a `vlt-decay` drain and a partner summon are due.

One caution recorded: the shell `diff` wrapper reported `_meta/conventions/decision-log.md` "identical" against a genuinely differing file. Every comparison in this run was redone with md5/difflib.
