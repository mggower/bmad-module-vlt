---
id: 'ST-5'
slug: 'specimens-have-no-owner'
title: 'Field specimens have no owner, so verification instruments are built at the point of least evidence — from the shape of the fix rather than the shape of the failure'
status: 'standing'
opened: '2026-08-26'
opened_by: 'owner problem-solving session (bmad-cis-problem-solving), handed off from the Cycle 12 acceptance-discharge session'
session: '_output/problem-solution-2026-08-26.md (gitignored — provenance only, never load-bearing; this study carries the diagnosis in full)'
causes:
  - 'No lifecycle stage owns field-specimen preservation; specimens attrit from observation to brief (20 → 2 → 2 → 0 for Cycle 12 build-1), so instruments are constructed where evidence is thinnest.'
  - 'An instrument authored from the fix''s shape cannot observe what the fix''s author did not anticipate; an instrument authored from the population''s shape can, and does.'
  - 'One tag resolves a check''s blocking power from its grading modality, welding "gradeable only in the field" to "cannot block."'
  - 'Closeout cannot distinguish a field check that never fired from one that fired and failed, so it applies Arc 3''s remedy to Cycle 12''s opposite disease.'
  - 'Ship-day capture boundary + one-release-whole-cycle compose to guarantee every acceptance failure is exported to the next cycle.'
  - 'The factory built a durable register for diagnoses, which are re-derivable, and none for observations, which are not.'
cited_by:
  - 'factory/cycles/14-no-enforcement-point/roadmap.md §A14-1 (capture 2026-08-26 — Cycle 13 check (2)''s instrument was the recorded returns, and those returns were all bare-form: the subset the guard handles. The substitution that made the check pass is visibly why it passed — cause 2, with a clean specimen)'
superseded_by: ''
---

# Specimens have no owner

## What provoked this

On 2026-08-26 `acceptance-discharge` graded Cycle 12 build-1 acceptance check (5) **FAILED** —
the second consecutive field run reporting the same defect — and the closeout gate stayed
**green**, because the check was tagged `[field-contingent]` and only `[ship-verifiable]` checks
gate. The skill's own routing recommended `cycle-closeout`. The cycle stood formally ready to
close with its lead build's central promise unmet. Only an owner override converted that into a
v0.16.1 patch; nothing in the process proposed repair.

The owner declined a point fix and asked for the **oscillation** to be studied: acceptance was
once *"so strict it was impossible to unblock the next build"* (Arc 3, eighteen days unclosable,
nine of thirteen tails field-shaped, four needing a vault the factory machine cannot read), and
the repair made it *"so loose that items get passed from cycle to cycle because they remain
open."*

## The evidence

Grounded at `c2d66af` / v0.16.0. Cycle 12: 4 builds, **27 acceptance checks — 16
`[ship-verifiable]` (all gate), 11 `[field-contingent]` (none gate)**. Outcome: 16/16
ship-verifiable PASS; of the 11 field-contingent, 4 DISCHARGED, 6 STILL-OPEN, **1 FAILED**. All
four build bullets remain bare `- [ ]`.

### The specimen trace — the direct evidence for the primary cause

| Stage | Specimens held | What the stage is obliged to do |
|---|---|---|
| Field run 2026-08-24 | **20/20** — 18 `malformed_frontmatter`, 2 `unmarked_supersessions` | — |
| Filing `2026-08-24-173002` | **2/20** — names `acotar-world-building`, `katsuo-dashi`; the other 18 are the phrase *"18 entries"* | `factory/inbox/README.md` shape; no specimen-manifest duty |
| Capture A12-2 (`12-proxy-claims/roadmap.md:246-300`) | **2/20** — faithfully propagates what it was handed | CLAUDE.md: ground *"against current module source"* — **code, never corpora** |
| Brief build-1 | **0/20** — instrument is a synthetic fixture, *"a page built to break it"* | `build-brief/references/brief-anatomy.md:212-219` — must **name** an instrument; holds two names and a count to name it from |
| Acceptance 2026-08-26 | **6/6** — every failing page named | evidence rubric: *"Read only what the item names. Don't go spelunking"* — **forbidden to characterize**; sole output is a filing routed to the next cycle |

The stage holding complete specimens has no authority to use them. The stage obliged to build the
instrument has none left to build it from. **The briefer's synthetic fixture was a reasonable act
given what survived** — which is why this is a mechanism defect and not a lapse.

### The instrument comparison — same cycle, same briefer, opposite outcomes

- **Build-3 check (3)**, a seven-grep retirement battery, **found a sixth undeclared site the
  brief's own retirement table had missed** (`extraction.md:26`, `vlt-track/SKILL.md:21`). It is
  authored from the **population** — every site in the repo.
- **Build-1 check (2)**, an at-rest reader probe, **passed while the field failed**. It is
  authored from the **fix** — the two slots build-1 closed — and so could not, even in principle,
  observe leakage into a third.

So `16/16 ship-verifiable PASS` measured the fix against itself. A coverage claim from a
self-shaped instrument is the vacuous-discharge failure wearing the tag meant to prevent it.

### The composition that exports every failure

Three individually-correct rules compose into a guarantee:

- field acceptance evidence requires a **release**;
- **ship day, not closeout day, is the capture boundary** (`inbox-capture/SKILL.md:70-82`), and the
  mid-cycle addendum reaches **unbuilt builds only** (`:84-95`);
- Cycle 12 ruling **D3 — "ONE RELEASE, WHOLE CYCLE"** (`12-proxy-claims/roadmap.md:1914`) leaves
  no build unbuilt.

Therefore **at the exact moment a cycle first becomes gradeable in the field, it is already closed
to capturing its own result.** Under D3 not even the addendum offers a partial escape. Every field
acceptance failure is next-cycle work *by construction*.

### Corroborating signals

- **Capture predicted this failure in writing and the cheap branch shipped.** A12-2 closed:
  *"the cheap read is prompt-only; the durable read is that an agent will keep re-deriving the
  wrong answer from a convention that does not state the boundary."* Prompt-only shipped (F2/F3
  schema descriptions, F7 a §Scope clause). Cycle 13's A13-1 Finding 3 now restates it harder:
  **prompt-only, enforced nowhere** — `vlt-lint-full.js:159`/`:168` state prohibitions the reduce
  at `:609` never enforces. Nothing tracked that a prediction was outstanding.
- **Magnitude fell 20 → 6; shape held.** The signature of a loop that improves fixes and never
  instruments.
- **Event-bounds proxy for elapsed opportunity.** Six Cycle 12 tails bounded *"no later than Cycle
  13's `inbox-capture`"* nearly fired with one day of runway when Cycle 13 opened early for the
  patch; papered with an owner carve-out. Cycle 12 is named *proxy claims*.
- **The hand-applied brakes are the diagnosis.** Bound debt; Arc 7 amendment A3's *"tag it
  ship-verifiable so it gates"*; build-3 (9)'s *"routes to an owner ruling, not a fourth
  re-carry"*. Each worked — A4-4(5) retired after four arcs, B10-2(5)/B10-12(6) after three,
  B8-2(4) on its bound. Each is a bespoke brake on one named tail.

## The causal chain

1. Cycle 12 stood ready to close green over a failed central promise — because build-1 (5) was
   `[field-contingent]`, and such checks do not gate (`closeout-checklist.md:24-28`).
2. It was field-contingent because grading it needed a real corpus, unavailable factory-side at
   brief time.
3. No corpus was available because the specimen set attrited **20 → 2** before the filing was
   written and stayed there through capture.
4. It attrited because **no stage owns specimen preservation** — the filing shape has no manifest
   duty, capture grounds only against module source, the brief has no corpus-acquisition duty, and
   acceptance is forbidden to characterize beyond what a check names.
5. **ROOT — the factory models field evidence as a transient input to diagnosis rather than as a
   durable asset of verification.** Every artifact in the loop carries a *claim*: a filing a defect
   claim, a capture a grounded claim, a brief a scope claim, a study a cause claim. **None carries
   an observation.**

**The proof this is root and not a deep symptom:** the factory already learned this lesson and
applied it to half the domain. `factory/studies/README.md` opens with it — *"a diagnosis with
nowhere tracked to live does not survive… distilled into whatever artifact was due that day…
Cycles later the same cause is re-derived from scratch, and the loop pays twice."* Substitute
**specimen** for **diagnosis** and the paragraph is this finding verbatim. The missed asymmetry:
**a diagnosis is re-derivable from the code; a specimen is not.** The factory built durable
machinery for the recoverable half and none for the unrecoverable half.

## System dynamics

**R1 (reinforcing).** specimens evaporate → instrument synthesized from the fix's shape → passes
vacuously → defect escapes to the field → new filing carrying a count → specimens evaporate again.
Each turn yields a new *filing*, never a stronger *instrument*. Build-1 was turn 2; Cycle 13's
patch is turn 3.

**B1 (balancing — the trap).** The owner's manual brakes reliably work, which is precisely why
pressure never accumulates on the mechanism. This is *shifting the burden to the intervenor*: the
owner's capacity becomes the system's load-bearing member. **A system whose manual overrides work
well is a system that will not repair itself.**

## The boundary of the problem

It occurs **exactly** where an instrument is authored from the fix's shape, and not where it is
authored from the population's shape. `[field-contingent]` is a *symptom* of that: a check goes to
the field precisely when nobody could construct a population-shaped instrument at rest.

**Not the problem: the loop's honesty.** `acceptance-discharge` graded FAILED and refused to
soften it — *"Not re-carried as STILL-OPEN — the discharging event occurred and the check did not
pass."* Capture called the fork. The brief named its instrument as the rules require. **Every actor
behaved correctly and the failure happened anyway.** No repair resting on anyone trying harder can
work.

## Rejected alternatives

- **A specimen register (`factory/specimens/`, `SP-N`), parallel to this one.** Rejected on this
  register's own words: *"a second set of adoption gates across five skills would be the accretion
  the register's own first two entries were written about."* The root is **no owner**, not **no
  register**; a manifest section inside the existing filing shape, cited by path, assigns the owner
  at zero accretion.
- **Letting acceptance open repair builds directly, bypassing capture.** Rejected: capture's
  module-source grounding is the loop's strongest link — it corrected this very filing's diagnosis
  twice (A13-1 Findings 3 and 4). Bypassing it trades the good half to save the broken half.
- **Making field-contingent checks gate.** Rejected as the pendulum's third swing — it is Arc 3
  rediscovered. The narrowing (*fired-and-failed* vs *never fired*) achieves the goal without the
  regression.
- **Snapshotting the real corpus as a fixture.** Rejected as illegal under P-9 (*no personal or
  vault-local information anywhere tracked*) — 146 pages of vault content. A **manifest** (slugs
  plus the minimal triggering fragment) is a different object and clears the line: slugs have been
  in a tracked public filing since 2026-08-24.
- **Running real-corpus sweeps at build time as gating checks.** Rejected on three costs: it puts a
  **stochastic** instrument on the release gate (A13-1 Findings 4 and 5 prove the scanners
  paraphrase `verbatim` fields and invent schema requirements); it gives the release a **hardware
  dependency** (build-1 (4)/(5): *"vault: `{field-vault}` only"*); and it grades against a **moving
  corpus**. A frozen specimen-derived fixture obtains the benefit without any of them.

## What this session got wrong

- **It opened on the wrong cause.** Step 1 framed the root as the tag — *one bit answering three
  questions*. That is real, but it is the **second** cause. The owner's challenge (*"why is finding
  the evidence at build time and not during acceptance or capture?"*) relocated it upstream to
  specimen custody, where the trace turned an argument into direct evidence. The session nearly
  became the fourth repair to move the visible dial.
- **It first proposed a criterion at the wrong stage.** The original success criterion #3 read *"a
  cheap check cannot be tagged out of the gate"* — locating the duty at build time, the point of
  **least** evidence. Pricing it exposed compute, flakiness and portability costs that all
  evaporate once the duty moves to observation time.
- **It initially accepted a plausible constraint untested.** *"Field evidence can't be carried
  factory-side"* was assumed until the tracked 2026-08-24 filing was read and found to contain
  specimen slugs already.
- **Least-confident claim, stated so a later reader can test it:** that a specimen manifest is cheap
  to author in the field. Filings are written mid-session by a human; a 20-slug manifest is real
  friction. If filings keep arriving with counts, the manifest must be **machine-emitted** from the
  persisted lint report — which already carries the slugs — rather than hand-written.

## What the session recommended

**"Custody, provenance, then gating"** — a composite of nine components in three tiers, ordered.
The bundle is the unit: **C1** without **C6** preserves specimens nobody is obliged to use, and
**C8** without **C1** gates checks that were never able to be good. Reversing the tier order
rediscovers the strict era, because it would tighten gating on checks that still could not be
made good.

**Tier A — specimen custody. Fixes the root: no owner for observations. Adds no artifact class.**

- **C1** — a filing reporting a countable defect class carries the **full specimen set** (slug
  plus the minimal triggering fragment), never a bare count. A section in the existing
  `factory/inbox/README.md` shape.
- **C2** — `acceptance-discharge`'s FAILED and BLOCKED grades **must emit a complete manifest**
  with the filing they already mandate. Codifies what the 2026-08-26 filing did unprompted, at
  the moment of maximum evidence.
- **C3** — `inbox-capture` grounds on a **second axis**: where a filing carries a count,
  dereference the named report and recover the set. Today's duty is *"ground against current
  module source"* — code, never corpora.
- **C4** — the manifest **materializes as a tracked fixture** in the cycle directory: frozen,
  deterministic, portable, public-safe.
- **C5** — **specimen retention is published per build** as a number (build-1's was 20 → 0).
  Pure measurement; no new gate.

**Tier B — instrument integrity. Fixes: instruments authored from the fix's shape.**

- **C6** — every acceptance check **declares its instrument's provenance** —
  `population-shaped` / `specimen-derived` / `synthetic` — and **synthetic is the option that
  must be justified**, inverting today's path of least resistance.
- **C7** — every instrument carries **negative controls in both directions**: a case that fails
  if the fix is absent, and a case that fails if the fix over-reaches. Precedent that worked:
  build-3 (4)'s *"the inheriting sub-container MUST fail"*. Build-1's fixture carried none.

**Tier C — gating honesty. Fixes: one bit, three jobs. By narrowing a population, never by
adding a precedence statement (Arc 9 D5).**

- **C8** — closeout's non-gating clause narrows to *field-contingent **and not yet fired***. A
  check that **fired and returned a negative verdict** routes to an owner **ruling** — not an
  automatic block, because agent-judged instruments are stochastic and an automatic block would
  put a flaky instrument on the release gate.
- **C9** — an **unfired** field-contingent check decays to an owner ruling on a bound expressed
  as a **date or run-count**, never an event. Generalizes build-3 (9)'s bespoke hatch and extends
  the pass-through tripwire from *unreachability* to *elapsed opportunity*.

**Held, not recommended: the in-cycle repair lane.** A shipped cycle staying open to capture for
repairs of *its own* acceptance failures only, shipping as a patch — narrowing the ship-day
boundary rather than removing it. It is the only component touching release policy, the only one
interacting with ruling D3, and the only one that would have let Cycle 12 close its own loop.
**Recorded as a live option this study does not recommend either way** — it is an owner call about
release cadence, not a conclusion the diagnosis compels.

**One hard constraint came out of reverse-brainstorming** (*"how would we guarantee this keeps
happening?"*, which returned eight tactics — **all eight current, deliberate rules**): **the
bundle must add no new artifact class, register, or adoption gate.** The manifest lives inside the
filing and is cited by path. A specimen register was generated and rejected on this constraint;
see Rejected alternatives.

## Lessons that generalize

1. **A good instrument is authored from the population; a bad one from the fix.** Build-3's grep
   battery found a site its author had missed; build-1's fixture could not see a slot its author
   had not thought of. Same cycle, same briefer — the difference is provenance, not diligence.
2. **A diagnosis is re-derivable; an observation is not.** Durable machinery for the recoverable
   half and none for the unrecoverable half is exactly backwards.
3. **Every actor can behave correctly and the failure still happen.** Capture predicted it in
   writing, the brief named its instrument as required, acceptance graded FAILED and refused to
   soften it. That is what a mechanism defect looks like from inside, and it is why no repair here
   asks anyone to try harder.
4. **A system whose manual overrides work well will not repair itself.** The brakes were the
   diagnosis, not the treatment.
5. **Two opposite diseases under one rule dissolve by narrowing the population, not by
   re-balancing the dial.** *Never fired* and *fired and failed* needed separating, not weighting.
6. **Don't open on the visible dial.** Three prior repairs moved gating power; this session nearly
   became the fourth. The dial everyone argues about is usually downstream of the thing nobody has
   named.
7. **Magnitude falling while shape holds** (20 → 6) is the signature of a loop that improves fixes
   and never instruments.

## The sharpest acceptance test

Two retrospective tests, both run in-session, and the second matters more than the first.

**Would the bundle have caught build-1?** C1 carries 20 specimens → C3 propagates 20 → C6 forces
the instrument to declare `specimen-derived` and build from pages whose *only* defect is a missing
attestation pair → C7 requires a case that fails if the fix over-reaches, so the probe observes
routing into **any** slot rather than the two closed ones → leakage is visible **at rest, before
release**. Caught. Had it still shipped, C8 routes the FAILED verdict to a ruling with no override
needed. **Caught twice.**

**Would the bundle have re-broken Arc 3?** Arc 3's thirteen tails: nine field-shaped, four needing
a vault the factory machine cannot read. **None fired.** C8 touches only checks that fired and
returned a negative verdict; C9 routes unfired checks to a ruling, never to a block. Arc 3 closes
exactly as it does today. **Structurally cannot reproduce it** — a property of narrowing an
existing population, not a judgment call. *This is the test any future proposal in this territory
must pass, and the one three prior repairs lacked.*

**Forward test, and the only thing that should be reported as success:** a specimen-derived
instrument discharging against real specimens (proves the primary cause), and a fired-and-failed
check reaching an owner ruling **without** an override (proves the secondary). Retention reaching
100% proves neither — it is scaffolding.

**Falsifier, stated so a later reader can kill this diagnosis:** if retention reaches 100% across
two cycles and repeat-defect turns remain above 1, **the primary cause is incomplete** and the true
cause is instrument *authorship* rather than instrument *material* — the indicated escalation is
adversarial instrument authorship (the instrument built by a party that did not author the fix,
from the manifest alone), generated in this session and held in reserve for exactly this.

## What became of it

**Nothing is built.** At writing, the v0.16.1 patch proceeds on the owner's override, Cycle 13's
ideation is live, and none of C1–C9 is opened as work. This section is the honest state, not a
plan.

**Routing.** Every component touches factory skills, `factory/inbox/README.md`, and closeout
mechanics — none of which `vlt-upgrade` delivers to vaults. Per CLAUDE.md they belong to the
**platform ledger** (`factory/platform/roadmap.md`), not a cycle build, so they do not compete
with the patch in flight. Scope, numbering and the WIP limit are the owner's ruling under that
ledger's channel contract. **This study makes none of them — a study gates nothing.**

**C6 was reached independently, by hand, before this study existed — and that is confirming
evidence, not a coincidence.** Cycle 13's ideation ruled its open question 4 on 2026-08-26:
*"THE INSTRUMENT IS THE REAL CORPUS AND IT GATES — the six pages that failed 2026-08-25, tagged
ship-verifiable; a fixture built only over the changed surfaces does NOT satisfy it."* Its
build-1 brief's check (2) names all six specimen slugs and gates closeout, and the build's ratio
is **three ship-verifiable to one field-contingent**, against Cycle 12 build-1's three-to-three.

That is C6 and C7's substance, obtained correctly, under the pressure of a live failure — and
obtained as **a per-build owner ruling, not a mechanism change**. It is therefore the ninth
hand-applied brake in the series this study documents, and a live instance of loop **B1**: the
factory reaches the right answer one tail at a time, which is precisely what keeps pressure off
the default. The next build with no failure behind it inherits nothing. **A later reader should
treat this as the strongest available evidence for the diagnosis, and as the reason C1–C5 (custody
without a prior failure to motivate it) matter more than C6, not less.**

**Read alongside `ST-4`.** Its named cause — *every lifecycle artifact is written to be re-read
later and none to be read now* — is this finding on the cognition axis; this study is the same
shape on the evidence axis. Neither supersedes the other.
