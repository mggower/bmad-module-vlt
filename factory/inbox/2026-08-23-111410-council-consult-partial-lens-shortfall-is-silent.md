# The council/consult fan-out has no partial-shortfall signal — 3 of 7 lenses can drop and it reads as a full panel

_Filed 2026-08-23 as the named file-forward from B10-12 disposition 7 (DA11), which **declined**
folding a lens-shortfall cap into the lint-execution repair and ruled the gap "a genuine but
lower-severity honesty gap that deserves its own filing, not a rider on a release-blocking lint
repair." Owner-confirmed under the 2026-08-23 batch disposition. Arc 11 candidate._

## Problem statement + evidence

`skills/vlt-setup/assets/workflows/vlt-review-council.js:148-152` fans out one agent per lens and
filters the results twice:

```js
const positions = (
  await parallel(lenses.map((lens) => () => agent(lensPrompt(lens), { label: `lens:${lens}`, phase: 'Lenses', schema: VERDICT })))
)
  .filter(Boolean)
  .filter((p) => p.available !== false)
```

`parallel()` resolves a failed or dead agent to `null`, and an agent that returns
`available: false` is dropped too. Both filters are silent.

**The zero case is guarded.** `:154` catches `positions.length === 0` and returns an explicit
degraded verdict with a `log()` line — so a totally-failed panel is loud.

**The partial case is not.** If 3 of 7 lenses drop, `positions` carries 4 entries and the
moderator synthesizes them as though the full panel fielded a position. Nothing in the return
names the shortfall: no denominator, no cap, no list of the lenses that never answered. The
verdict reads exactly like a complete review.

This is the **same class** as the full-mode lint defect B10-12 repaired (A10-16/A10-17): a
coverage shortfall rendered as a clean, complete-looking result. It is lower severity for the
reasons DA11 and B10-12 disposition 7 recorded, and those reasons should be preserved in any
capture:

- the council's degrade contract genuinely differs from a wiki sweep's — a moderator
  synthesizes only the fielded positions, and the run is not coverage-denominated the way a
  page sweep is;
- the **execution** defect does not reach it: the council's schemas measure `VERDICT` 776 and
  `SYNTHESIS` 1,035 serialized chars, far under the 4,096 classifier ceiling the DA4 spike
  measured — so lenses are not being killed by the schema-size failure that killed `PAGE_SCAN`
  at 4,100;
- B10-12's standing **schema-size budget** (≤ 3,700 serialized, owner-set 2026-08-23) is
  workflow-agnostic and **does** cover the council and consult schemas, so a future council
  schema crossing the ceiling is caught regardless of this filing.

So the residual gap is honesty-under-partial-shortfall only, not execution.

## The candidate

A minimal partial-shortfall signal on the council return, mirroring leg 2's shape without
importing its machinery:

- carry a denominator — lenses selected vs lenses fielded;
- name the lenses that did not field a position (and, where distinguishable, whether they died
  or returned `available: false` — the reason-partition idea from DA6);
- surface it in the moderator's synthesis output rather than only in a `log()` line, so a reader
  of the verdict sees it;
- **no error threshold is proposed.** Unlike a wiki sweep, a partial panel may still be a
  legitimate review — the ask is that it says so, not that it refuses.

`vlt-consult`'s fan-out should be audited for the same shape in the same build
(`CONSULT_RETURN` 1,703 serialized) — DA11 named the council instance; the consult sibling is
the obvious parity check.

## Open questions for capture

1. Does the moderator prompt need to know about the shortfall (so synthesis language can hedge),
   or is a return-level field enough for the reader?
2. Is `available: false` semantically different enough from a dead agent to be worth partitioning
   in the output, or is one "did not field" count honest enough?
3. Does anything downstream consume the council return positionally in a way a new key would
   disturb?

## Provenance

- Roundtable delta 2026-08-22, **DA11** — "a ruling on record, not a scope expansion by default."
- B10-12 brief, disposition 7 (DECLINE + file-forward): `skills/reports/build-B10-12-lint-full-execution-repair.md`.
- Owner batch disposition 2026-08-23 confirming the decline and this filing.
