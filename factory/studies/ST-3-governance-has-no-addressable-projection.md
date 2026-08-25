---
id: 'ST-3'
slug: 'governance-has-no-addressable-projection'
title: 'Governance has no machine-addressable projection, and full-mode lint has no memory — so cost is priced against corpus size instead of against change'
status: 'standing'
opened: '2026-08-24'
opened_by: 'owner problem-solving session'
session: '_output/problem-solution-2026-08-24.md (untracked — provenance only)'
causes:
  - '(a) Governance has no machine-addressable projection — the only unit of a convention is the whole file, so any consumer that needs a slice must pay for the whole thing, per consumer, per run.'
  - '(b) Full mode has no memory — every run starts from zero because coverage and recomputation were never separated, so cost is priced against corpus size instead of against change.'
cited_by:
  - 'factory/cycles/11-reachability/filings/2026-08-24-102813-full-lint-cost-scales-with-corpus-not-with-change.md (the filing this session produced)'
  - 'factory/cycles/11-reachability/roadmap.md §A11-11 (captured CONFIRMED; direction 0 shipped in build-8, directions 1–4 deferred to Cycle 12)'
  - 'factory/studies/ST-2-location-as-proxy-for-trust.md §RC2 (this study derived the same cause from the cost side, one day earlier)'
superseded_by: ''
---

# ST-3 — Governance has no addressable projection

**Back-filled 2026-08-25** (platform P-14), and back-filled **as a correction**: this session
was excluded from the register at its build on the reasoning that it had *reached its fix*. It
had not. Its cause is live, deferred to Cycle 12, and independently re-derived one day later in
a different subsystem — which makes it both a study by every clause of the definition and the
sharpest evidence the register has produced. See §Convergence with ST-2, and the register
README's *What does not earn an entry*, whose guard exists because of this miss.

## The presenting complaint

Full-mode lint costs roughly **4.1 M input tokens across ~209 agents per run** — the session's
own flagged estimate, never measured. The wiki it audits had tripled from 65 to 147 pages, and
the `lint-debt` tripwire pushes toward full runs without the cost curve ever having been
re-checked against that growth.

## Root cause

**Five Whys, condensed:** full lint is expensive because ~70% of the dominant phase is
convention text duplicated 147× and the cluster phase re-reads the whole corpus a second time
on a costlier model → convention text is duplicated per agent because each fan-out agent is a
fresh context with no shared state, and the design **correctly refuses to restate convention
rules in prompts**, so it makes each agent read the real files — correct for fidelity,
catastrophic for cost → correctness forces whole-file reads because the conventions have **no
addressable sub-unit for "what a page scanner needs to know"** (`frontmatter.md` is 38.7 KB of
field schema, migration notes and worked examples; a scanner needs perhaps 15% of it, and there
is no legal way to take that 15% without either restating it — breaking single-home — or
reading all of it) → and every page is re-judged every run because *"full"* is defined as **full
recomputation** rather than **full coverage**, with no memory of a page's findings across runs,
despite a report already being persisted per run.

> **(a) Governance has no machine-addressable projection.** The only unit of a convention is
> the whole file, so any consumer that needs a slice must pay for the whole thing, per
> consumer, per run.
>
> **(b) Full mode has no memory.** Every run starts from zero because coverage and
> recomputation were never separated, so cost is priced against corpus size instead of against
> change.

**Cause (a) is why this is a study and not a filing.** It is not a fact about lint. Any
fan-out consumer that needs a rule slice faces the same choice — pay whole-file price or break
single-home — so the cause binds every future skill of that shape, and the module's own
single-home discipline is what forecloses the cheap way out. A11-11's direction 4
(scanner-card projection) is the proposed fix, and Cycle 12's ideation will be ruling on it.

## Contributing factors

- **Exact-facts-from-LLMs residue.** ~9 of 16 `PAGE_SCAN` fields are pure deterministic
  extraction. B5-3 already moved *comparison* into JS ("the scanner reads, JS does the
  arithmetic") — but *reading* is still done by a model, which is why the scanner must load
  `frontmatter@13`'s full 38.7 KB at all. The open filing
  `2026-07-26-184704-lint-full-asks-llms-for-exact-facts.md` is the same seam seen from the
  correctness side rather than the cost side.
- **`wiki-index.md` sits in the page-scanner read set and is unused by it** — ~8.2 KB × 147 ≈
  1.2 MB of pure waste per run. The index judgment happens in the dedicated index pass, which
  reads it correctly.
- **Prompt layout defeats cross-agent prefix caching.** `pageScanPrompt` opens with the
  *variable* part and follows with the invariant instruction block — inverting the one ordering
  that would let 147 near-identical prompts share a cached prefix.
- **The cluster prompt already receives `key_claims`** from the scan phase, then instructs the
  agent to re-read every page live anyway. The cheap triage signal is in hand and is not used
  as a gate.
- **Ratcheted caution.** Every honesty repair (A10-16, A10-17, B10-12, DA7) correctly added
  coverage guards; **none of them ever removed work**, so the pipeline has monotonically
  accreted cost.

## Convergence with ST-2 — three derivations of one cause

The contributing factor above, and this session's Key Insight 4, state:

> *Honesty ratchets have a cost side, and nobody was watching it. Cycles 9–10 correctly added
> coverage guards and never removed work. Monotonic accretion of correctness is still monotonic
> accretion. **A guard's cost should be reviewed on the same cadence as its correctness.***

That is `ST-2`'s **RC2** — *the loop can process defects but not obsolescence* — derived **one
day earlier**, in a different subsystem, by a different route, from the cost side rather than
the governance side. It is also platform **P-15**'s baseline claim (*eleven cycles retired zero
rules while adding many*) observed as a token bill instead of as a rule count.

So one cause has now been derived **three times independently**: here (2026-08-24, cost side),
in `ST-2` (2026-08-25, governance side), and as P-15's measured baseline. Two of those three
derivations happened **because the first had nowhere citable to sit** — and the third, P-14's
own back-fill, then excluded this session from the register on a test that said it was spent.

**The register's failure mode was reproduced inside the register's own build.** That is not an
embarrassment to bury in a deviation note; it is the strongest evidence P-14 has that the
problem it names is real, and it is why the README's exclusion criterion now tests the *cause*
rather than the *fix*, with an explicit guard that a live diagnosis is never excluded.

## Disposition

Filed as `2026-08-24-102813-full-lint-cost-scales-with-corpus-not-with-change.md`; captured as
Cycle 11's **A11-11** and graded **CONFIRMED** — every mechanism claim verified against
`skills/vlt-setup/assets/workflows/vlt-lint-full.js` (byte sizes exact at 58,531 per agent; the
cache-hostile prompt ordering, the unused index read, and the bought-and-discarded `key_claims`
triage all confirmed at their sites).

**Only direction 0 — the instrumentation — shipped**, in Cycle 11's build-8. **Directions 1–4
are deferred to Cycle 12**, on the recorded rationale that all four would otherwise be priced
against a number nobody had measured, and that direction 2 was sequencing-blocked behind
build-1 regardless. Two anti-directions ride the deferral unchanged and are part of this
study's standing content: **no sampling**, and **no `coverage_caps` entry is ever removed to
make a run look cleaner.**

Cause (a) and cause (b) are both **unrepaired** as of v0.15.0.
