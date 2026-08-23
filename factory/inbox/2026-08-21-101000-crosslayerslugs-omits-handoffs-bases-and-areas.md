# The fan-out's `crossLayerSlugs` omits `_agent/handoffs/`, `_agent/bases/` and `areas/` — valid cross-layer links report as missing targets

_Filed 2026-08-21 from the factory on the owner's go-ahead, classification: **defect**
(module-feedback candidate). **Provenance:** lint-surfaced on vlt-core (the 2026-08-16 full
`vlt-lint` run, Arc 8 era — the owner's vault-side report, third of three strength-ordered
candidates); content recovered from Arc 7's Closeout record item 8
(`skills/reports/archive/inbox-evolution-arc7-roadmap.md:1852-1856` — the substance was never
lost, only the pointer to it); filed 2026-08-21 on the owner's go-ahead discharging ruling
4c's pre-tag bound (Arc 9 roadmap, roundtable A8, discharge route 1)._

## The claim, as recorded in Arc 7's closeout (item 8, verbatim substance)

> the fan-out's `crossLayerSlugs` omitting `_agent/handoffs/`, `_agent/bases/` and `areas/`

`crossLayerSlugs` is the allowlist of valid non-wiki `[[link]]` targets the `vlt-lint` SKILL
globs and passes into the fan-out so a legitimate cross-layer link is not reported as a
missing target. On the 2026-08-16 run the assembled set did not include notes under
`_agent/handoffs/`, `_agent/bases/` (a vlt-core vault-grown location), or `areas/` (a PARA
layer) — so wiki pages linking into those layers false-positived as `missing_targets`.

## Grounding against current module source (HEAD 86efd48, v0.11.0)

**The defect still stands.** The workflow itself is agnostic — it takes whatever the caller
passes (`skills/vlt-setup/assets/workflows/vlt-lint-full.js:35` arg doc, `:78` intake, `:211`
set construction) and its comment even warns "Without crossLayer, valid cross-layer links
false-positive en masse. (#3 §4)". The assembly instruction is the gap:
`skills/vlt-lint/references/full-scale.md:7` tells the SKILL to glob `{research}` "(and any
agent-zone note location the wiki conventionally `[[links]]` into)" —

- `_agent/handoffs/` is covered only by that vague parenthetical, never enumerated; whether
  an operator's glob reaches it is left to interpretation per run.
- `_agent/bases/` is a **vault-grown** location with no module counterpart — exactly the
  class the parenthetical gestures at, and exactly the class a non-enumerating instruction
  silently misses (`vault_structure` explicitly supports vault-local keys, so such locations
  are in-contract, not anomalies).
- `areas/` is a **PARA layer**, neither research nor agent-zone — no clause of the
  instruction covers it at all. A wiki page linking to an `areas/` artifact false-positives
  by construction.

Note the design tension for capture: CLAUDE.md's "lists that claim completeness drift" rule
argues against a hard enumeration; but the current subset-plus-vague-parenthetical produced
three omitted layers in the field. A point-at-the-map fix (e.g. derive the glob set from the
resolved `vault_structure` keys that hold linkable notes, rather than naming directories)
would satisfy both.
