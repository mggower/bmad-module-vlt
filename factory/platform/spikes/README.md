# The spike register

**Single home for spike mechanics** (platform P-2, 2026-08-24). Every other site — the
lifecycle map, `ideation-scaffold`, `build-brief`, `cycle-closeout`, `inbox-capture` —
carries a pointer here and never restates the ladder, the ids, or the frontmatter shape.

A **spike** is the lifecycle's answer to an external unknown: CLAUDE.md's step 3 rule is
that such an unknown gets *a spike before the brief is written — read the actual external
source rather than reasoning from its docs or from memory*. This register is what gives
that rule durable ids and lifecycle teeth: **visible at adoption, blocking at brief.**

*Why blocking at brief and not at adoption* (the ruling that survived the 2026-08-21
brainstorm): blocking **adoption** front-loads spikes at their dumbest moment — the
question is not yet sharp. Ideation shapes the scope first, and spike questions sharpen
*after* the rulings. Arc 9's S3 proved it: the question only became answerable once
B9-6's dependency on the A10-6 fix was ruled.

## Files and ids

One file per spike: `factory/platform/spikes/S-N-<slug>.md`.

- **`S-N` is a register-global id**, not per-cycle. It is allocated once, never reused,
  and never renumbered — a consumed spike's id stays live because briefs cite it.
- The next id is one past the highest `S-N-*.md` in this directory. Nothing else assigns
  ids.
- Cycles used to number spikes locally (`S1`/`S2`/`S3` in Arc 9, `SPIKE-1`/`SPIKE-2` in
  Arc 3). Where a back-fit carries such a name, it is recorded as `legacy_id:` — the
  global `S-N` is the id every gate resolves.

## Frontmatter (the parse target every gate reads)

```yaml
---
id: 'S-N'
slug: '<kebab-slug>'
status: 'proposed'          # proposed | running | harvested | consumed
question: '<the external unknown, one line — what a real source must answer>'
opened: 'YYYY-MM-DD'
opened_by: '<capture | ideation | roundtable> — Cycle NN (<the id that demanded it>)'
timebox: '<how much reading this is worth before it reports back, even unresolved>'
verdict: ''                 # proceed | reshape | kill — empty until harvested
sources: []                 # what was ACTUALLY read (paths, versions, URLs) — not what was planned
findings: ''                # path to the harvest artifact, or inline if short
consumed_by: []             # the briefs/builds that cited it — appended, never replaced
legacy_id: ''               # optional: the per-cycle name this spike carried before the register
---
```

Below the frontmatter: the question in full, and — once run — the findings, or a pointer
to the harvest artifact if the harvest is long. **Harvest artifacts live in the cycle
directory that produced them** (`factory/cycles/NN-<slug>/spike-*.md`); archival is
location, so a closed cycle's harvest never moves. The register entry is the durable
pointer; it is not a copy.

## The ladder

| status | means | who moves it |
|---|---|---|
| `proposed` | the question is written; no source has been read | opened by capture (grounding hit an external unknown), by ideation, or by a roundtable amendment |
| `running` | someone is reading the actual source, inside the timebox | whoever runs it |
| `harvested` | the source was read; `sources:`, `findings:` and `verdict:` are filled | whoever ran it |
| `consumed` | a brief or build cited the finding; `consumed_by:` names it | `build-brief`, on the run that consumes it |

`harvested` is the state the gates accept. `consumed` is terminal and is a record, not a
further gate — a spike may be consumed by more than one build.

**A timebox that runs out does not mean `kill`.** It means the spike reports what it
learned and sets `verdict: reshape` — the unknown gets re-cut into a question the
timebox can answer. `kill` is for a question that turned out not to need answering.

## The gates (each named site points here, never restates)

- **`ideation-scaffold`** lays a **Spikes** slot in the rulings skeleton. Each build
  bullet the owner rules carries a `spike:` field — `none`, or the `S-N` it depends on.
  The skeleton also lists any spike this register already holds `proposed`/`running`
  against the open cycle, so an inherited spike is visible at adoption rather than
  rediscovered at brief time.
- **`build-brief`** blocks unless build N's `spike:` field reads `none` or names an
  `S-N` whose register file is `harvested` or `consumed`. Blocking here is the point: a
  brief written over an open spike reasons from docs and memory, which is the exact
  failure the rule exists to prevent.
- **`cycle-closeout`** runs the **orphan-spike check**: no spike opened against the
  closing cycle may still read `proposed` or `running`. Each is either harvested, or
  ruled `kill` by the owner, or explicitly carried forward to the next cycle (which
  re-stamps `opened_by`). A cycle does not close over a question nobody answered and
  nobody killed.
- **`inbox-capture`** may open a `proposed` stub when grounding hits an external unknown
  — the question is sharpest at the moment grounding fails to answer it. A stub is a
  question with an id, never a ruling; ideation decides whether it binds a build.
- **`.claude/skills/vlt-lifecycle.md`** carries the observable rows, so `lifecycle-status`
  reports an open spike as a lifecycle position with a named next move.

## What is *not* in the register

Closed cycles' spike history beyond the two back-fits below is **deliberately not
migrated** (P-2 out-of-scope). Known and unmigrated: the B10-12 harness-classifier-ceiling
spike, `factory/cycles/10-signal-integrity/spike-b10-12-classifier-ceiling-2026-08-22.md`
(SETTLED 2026-08-22; carries an owner-reviewed provenance quarantine note). It is named
here so the register's silence about it is a recorded choice rather than an oversight.

## Register

| id | slug | status | verdict | opened | cycle |
|---|---|---|---|---|---|
| `S-1` | para-container-harvest | consumed | proceed | 2026-08-21 | Cycle 9 → consumed in Cycle 10 |
| `S-2` | projection-baseline | consumed | proceed | 2026-07-25 | Cycle 3 |
| `S-3` | github-notification-semantics | **proposed** | — | 2026-08-24 | Cycle 11 (A11-2) |

*(This table is a convenience index over the files, which are authoritative. It lists
every register file — a completeness claim it can keep only because the directory is its
population; re-derive it from `ls` when in doubt.)*
