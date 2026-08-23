# The lint report block is never persisted — stable keys with no series, and acceptance can't read them either

_Filed 2026-07-29 from **acceptance discharge runs 2 + 3** (Arc 4). Drafted at run 2 after the
owner named the gap directly; owner confirmed filing at run 3. Evidence is vlt-core, read-only._

## The claim

`vlt-lint` Step 5 emits a *"parseable report (stable keys, so a dashboard can consume it)"* —
and **nothing keeps it**. The report exists only in-session; the `{log}` line's fixed shape
predates Arc 4 and structurally cannot carry the seven slots the arc shipped
(`research_zone`/`linkage_ripe`, `contradiction_scan` + the three-value split,
`entity_scan`/`entity_collisions`, `authority_scan`/`consult_missing`).

## Grounding

- `skills/vlt-lint/SKILL.md` Step 5 — the report block spec (stable keys, dashboard framing).
- The `{log}` line format (operating contract, canonical log shape) — one fixed-shape line per
  sitting; no slot for report keys.
- Measured cost, twice: **discharge runs 2 and 3 could verify report-shape acceptance clauses
  only because the owner hand-pasted the 2026-07-26 18:05 report block into the session** —
  eleven sub-clauses across A4-1..A4-5 had no on-disk evidence to read. The session note
  (`_agent/sessions/2026-07-26-180500-lint.md`) carries prose and watches, not the block.

## Why it matters

Two costs, one deeper than the other. The shallow one: any factory-side audit (acceptance
discharge, a future capture grounding) depends on a human courier for machine-shaped data. The
deep one: **stable keys with no series** — the keys were designed to be comparable across runs,
and no trend question (is adoption climbing? did `coverage_caps` start truncating? is the
undispositioned count draining?) can be asked at all, because run N−1's block no longer exists
anywhere. Wants a persistence home for the report block (a dated artifact under the agent zone,
or the session note carrying the block verbatim as a fenced trailer) — chosen with the derive-first
rule in mind: persisting a *report* is recording an observation, not storing derivable state.
