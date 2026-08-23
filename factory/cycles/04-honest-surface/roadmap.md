---
title: 'Inbox Evolution Roadmap — Arc 4: the honest-surface arc (what the vault can see about itself)'
status: 'CLOSED 2026-07-29 — the honest-surface arc, shipped as v0.8.0 2026-07-26 (builds A4-1+A4-2+A4-3+A4-4+A4-5 @ 557347f, tagged v0.8.0 on origin/main, package-lint PASS line in the release commit). Acceptance: four discharge runs (2026-07-26 → 2026-07-29) rode the vlt-core 0.7.0→0.8.0 upgrade, the 2026-07-26 18:05 full lint (linkage_ripe 10 of 103, FP hand-verified ≈0% against the naive ~79% baseline), the vault''s first two consults (which surfaced a six-week-old arithmetic error no document carried), two vlt-research writes, the vlt-sayari 0.6.0→0.8.0 upgrade, the 2026-07-27 ingest, and the 2026-07-29 16,215-word heavy ingest — every trigger-bearing gating tail on the ledger fired, the inherited build-20 clause discharged, and five of six ledger items are fully checked with dated evidence. **A4-4 closes UNCHECKED on its clause (5), graded FAILED** — entity-collision coverage is silently pair-incomplete (the check found the Seahawks instance and missed its explicitly-paired Rams twin) — **owner-carried as inherited debt to Arc 5** (the build-20 form): filed as inbox/2026-07-29-120002-entity-collision-coverage-pair-incomplete.md and captured as A4-21; the ledger''s [x] count may not be read as a measure of what the arc proved — the unchecked box is the record of a real failure. Still open elsewhere: the sayari lint-render halves on A4-1 (6) / A4-3 (7) / A4-4 (8) released as ONE standing watch (field-contingent, trigger: first vlt-sayari full lint — none may be read as passed); A4-5 clause (4)''s standing watch (a non-answer consult return is still unexercised — when consults only ever return answer, inspect, don''t assume); the A4-6..A4-23 Arc-5 seed batch captured in this roadmap (grounded @ 9f05579) awaiting owner-steered ideation; and the re-listed Arc-3 carry-forwards, which travel to Arc 5 — the authoritative list is **Carried forward past Arc 4** below, which the next inbox-capture re-lists (anything left off is silently dropped). Filing archival at close, per the per-filing criterion: five filings moved to inbox/archive/ (A4-1/A4-2/A4-3/A4-5''s filings fully discharged; A3-18''s chess-coach filing closed by its no-build ideation ruling — vault-local, its evidence debt closed with it); A4-4''s auto-caption filing HELD ACTIVE as the carrier of the inherited debt. This arc is archived — do not append.'
module_code: 'vlt'
created: '2026-07-25'
updated: '2026-07-29 (CLOSED — arc-closeout: gate passed on the discharged ledger + tag v0.8.0; A4-4 (5) owner-carried as inherited debt (A4-21, fix rides Arc 5); carry-forwards recorded in **Carried forward past Arc 4**; roadmap + five briefs archived to skills/reports/archive/; five filings archived, one held; memory synced. Prior: DISCHARGE RUN 4 — A4-4 (4) discharged on the 16,215-word heavy ingest. Prior: CAPTURE — 18 filings folded in as A4-6..A4-23, the Arc-5 seed batch)'
arc_title_status: 'PROPOSED — the arc name above is the clerk''s, derived from the cross-filing thread; owner may rename before the first brief lands.'
derives_from:
  - 'inbox/2026-07-18-115913-chess-coach-persona-line-seeds-fabricated-time.md'
  - 'inbox/2026-07-25-144500-revisit-after-has-no-adoption-path.md'
  - 'inbox/2026-07-25-160239-contradictions-have-no-drain.md'
  - 'inbox/2026-07-25-160949-auto-caption-name-substitution.md'
  - 'inbox/2026-07-25-132141-partner-consult-synchronous-channel.md'
  - 'inbox/2026-07-25-162416-linkage-ripe-cannot-see-graduation.md'
  # ── capture 2026-07-29 (A4-6..A4-23, the Arc-5 seed batch) ──
  - 'inbox/2026-07-25-171500-brief-restatement-drift.md'
  - 'inbox/2026-07-25-183003-upgrade-preserve-set-misses-vault-grown-op-skills.md'
  - 'inbox/2026-07-25-193000-report-slot-with-no-check.md'
  - 'inbox/2026-07-26-124223-lint-has-no-memory-of-adjudicated-divergence.md'
  - 'inbox/2026-07-26-141500-group-e-did-not-retire-the-handwritten-handshake-grep.md'
  - 'inbox/2026-07-26-142000-spec-convention-surfaces-candidates-nobody-accepts.md'
  - 'inbox/2026-07-26-142500-boundary-classifier-five-verdicts-and-an-unmeasurable-metric.md'
  - 'inbox/2026-07-26-184704-lint-full-asks-llms-for-exact-facts.md'
  - 'inbox/2026-07-26-184705-spec-candidate-revision-signal-is-template-boilerplate.md'
  - 'inbox/2026-07-29-082930-activation-contract-read-is-the-boot-whale.md'
  - 'inbox/2026-07-29-082931-handoffs-and-consults-repay-the-full-boot.md'
  - 'inbox/2026-07-29-082932-beat-2-orient-scales-with-vault-age.md'
  - 'inbox/2026-07-29-082933-no-instrument-measures-session-token-cost.md'
  - 'inbox/2026-07-29-082934-whale-files-carry-restated-weight.md'
  - 'inbox/2026-07-29-120001-adoption-stamp-unreachable-beyond-mint.md'
  - 'inbox/2026-07-29-120002-entity-collision-coverage-pair-incomplete.md'
  - 'inbox/2026-07-29-120003-sayari-upgrade-omitted-convention-adoption-line.md'
  - 'inbox/2026-07-29-120004-lint-report-block-is-never-persisted.md'
predecessor: 'skills/reports/archive/inbox-evolution-arc3-roadmap.md (Arc 3 — the enforcement arc; CLOSED 2026-07-26, shipped v0.6.0 + v0.7.0, build-17 unbuilt and folded into Arc 5. Archived at closeout as anticipated; every pointer below survived the move — only this path changed.)'
---

# Arc 4 — the honest-surface arc

## The through-line (why these filings are one story)

Arc 3 built the bells: enforcement stages, attestation, freshness keys, a graduation queue, a
packaging lint. Arc 4 is what the field found when those bells started ringing — **the module
can report on itself, but it cannot yet tell a true report from a comfortable one.**

Five mechanisms, one shape. A count whose only attainable value is "fine" (`revisit_after:` at
0-of-96; `contradictions_handled:` that only grows; `spec.md`'s original `deferral_metric` scar),
and its mirror, a projection whose hits are all noise (`linkage_ripe` at 41/0, and ~97/98 once
its accidental damper was removed). Underneath both: a check that infers state from the residue
of the very process it is checking, and a schema that offers keys nobody is ever asked to fill.
One layer down again, the same axis at the partner surface — a partner speaking in another
partner's voice, or a transcript substituting a plausible real name that reads as clean data.

Arc 3 shipped `adoption_first_instance:` as the answer to "declared but never exercised." It is
itself declared and never exercised — zero of seven conventions carry it, including `spec.md`,
the example its own definition names. **The arc's remedy became the arc's fourth instance.** That
is Arc 4's opening position.

**Extension (capture 2026-07-29, A4-6..A4-23 — the Arc-5 seed batch).** The 18 filings folded in
below arrived after this arc's builds shipped, and they bend the story a quarter-turn. Arc 4 made
the surfaces honest; the new batch reports what honest surfaces cost and what they still can't do.
Three threads: **(1) the checks behind the checks** — a report key no check fills (A4-8), a lint
that asks LLM scanners for exactly-computable facts (A4-13), a revision signal that detects the
module's own template vocabulary (A4-14), a classifier whose bell has never rung (A4-12), a
`spec_candidate` beat whose terminal state is the backlog (A4-11) — the same silent-zero anatomy
Arc 4 fixed, one layer down. **(2) writes with no surface** — an adoption stamp only mints may
write (A4-20), a lint report nothing persists (A4-23), an upgrade-report line nothing verifies
(A4-22), a decision the lint can't remember (A4-9), a vault-grown op skill no preserve bullet
catches (A4-7). **(3) the price of the machinery** — the five-filing boot-cost anatomy
(A4-15..A4-19), which asks, for the first time with numbers, whether the governance the arcs have
been stacking is paid for at every activation. The factory itself appears twice (A4-6, A4-10):
the loop's own briefs and templates drift the same way vault surfaces do.

## Inherited from Arc 3

**Acceptance debt (one), per the 2026-07-25 arc-boundary ruling (option (b)).** Arc 3 closes
carrying build-20's **FAILED** `linkage_ripe` FP-rate clause; it is inherited here rather than
re-opening Arc 3 for a sixth build. `arc-closeout` records it as such.

- **The FAILED grade stands.** The check returned 41 hits / 0 real on the vlt-core
  `[2026-07-25 15:05]` full lint.
- **Its wording does not.** The original clause — *FP rate tracks the calibrations (~21–23%)* —
  is unsatisfiable: it compares an FP rate to a set-reduction ratio. **Restated target for A4-1:**
  *the projection's false-positive rate, hand-verified on a mature research zone, is near the
  calibration's ≈0% and must not exceed the naive signal's ~79%* — an FP rate against an FP rate.
- **Its stated root cause does not.** Not "missing graduation state" but a **polarity inversion**
  (see the spike digests below).
- **Its severity was understated.** The 41 was an undercount; the same lint run destroyed the
  cause. Re-measured: **97 of 98, ≥93% FP**, latent in the vault today.

Full ledger text, the graded verdict, and both correction notes: Arc-3 roadmap, *Deferred
acceptance ledger (Arc 3)*, build-20 entry.

**Not inherited — and now resolved (Arc 3 CLOSED 2026-07-26).** Arc 3's remaining first-exercise
tails did not transfer here. At closeout they were disposed by an owner-ruled batch: three filed as
findings (build-15's spec adoption, build-16's boundary metric, build-23's process-adoption FAILURE),
five released as standing watches, one staged (build-18 F1), one dated (091006, 2026-08-17), and
build-17 + 091003 M0 folded into **Arc 5**. The authoritative list of what outlives Arc 3 is its
*Carried forward past Arc 3* section — the next `inbox-capture` re-lists from there, **not** from
this roadmap. Arc 4 inherits exactly one thing: build-20's clause above.

> **Note for Arc 4's own acceptance run.** Arc 3's closeout diagnosed a defect in the *ledger form*,
> not in Arc 3: acceptance checks conflate **ship-verifiable** (bounded) with **field-contingent**
> (needs an event of a specific kind — unbounded) under one checkbox, and gating closeout on both
> means closeout has no bound. Nine of Arc 3's thirteen tails stuck that way, four of them on a vault
> the factory machine cannot read. **This ledger has the same shape.** Before `acceptance-discharge`
> runs here, tag each check ship-verifiable or field-contingent, and name which vault can produce the
> event for the field-contingent ones. Full statement: Arc-3 roadmap, *The durable fix this arc
> earned*.

## The batch (A3-18..A3-23)

Captured in the **Arc-3 roadmap**, *Capture — six filings (grounded against module source
2026-07-25, v0.7.0 @ `dbcf018`)*. **Capture ids are kept as filed** — they are stable references
used by the rulings, the ledger and the spikes; they are not renumbered into an A4-* series.
The full grounded text (verified `file:line` citations, corrections, honest limits, per-filing
cross-references) lives there and is **not restated here**. Summaries below are for navigation.

| Id | Filing | Verdict at capture | Build |
|---|---|---|---|
| A3-18 | chess-coach persona line seeds fabricated time | ⛔ provenance correction — vault-local mint prose, not module source | **none** (vlt-core only) |
| A3-19 | `revisit_after:` has no adoption path | GAP confirmed; two writers disagree, and the adoption facet is itself unexercised | **A4-2** |
| A3-20 | contradictions have no drain | GAP confirmed; Step 4 is a routing gap, not an eligibility gap (cheaper than filed) | **A4-3** |
| A3-21 | auto-caption sources substitute plausible real names | GAP confirmed; no proper-noun guard anywhere in ingest | **A4-4** |
| A3-22 | a synchronous partner→partner consult channel | GAP confirmed; the batch's only *candidate*, not a defect | **A4-5** |
| A3-23 | `linkage_ripe` cannot see graduation | GAP confirmed; a **graded acceptance failure**, root cause re-established by spike | **A4-1** |

## Governing rulings (digest — binding text lives in the Arc-3 session record)

The binding record is the Arc-3 roadmap's **`## Ideation rulings — A3-18..A3-23 (owner-steered,
2026-07-25)`** section. **If this digest and that section disagree, that section wins.** Briefs
cite it, never re-litigate it. (It travels to `skills/reports/archive/` at Arc-3 closeout —
read-only there, per the standing rule against appending to closed roadmaps.)

- **Arc boundary → (b).** Build-20's failed clause carries here; Arc 3 does not re-open.
- **A3-18 → no build.** Vault-local fix; no module residue. Its evidence debt closes with it.
- **A3-19 → fix the key in BOTH writers AND wire the adoption facet.** `revisit_after:` plus a
  two-outcome question in `vlt-research/SKILL.md:71` **and** `vlt-ingest/SKILL.md:77-91` (which
  omits the key entirely and is the majority write path); `adoption_first_instance:` gets its
  first real consumer. *(Owner-delegated to clerk's recommendation; reversible.)*
- **Silent zeros → ONE general honest-reporting rule, stated once**, written by A4-2 and cited by
  the rest: *a count whose only attainable value is "fine" must state what it cannot see.* No
  site briefs a bespoke report-line fix.
- **Verification-by-residue → a boundary clause on derive-first**, not a new standalone invariant:
  *derive-first does not license deriving a state from the residue of the very process that
  produces it.* *(Owner-delegated to clerk's recommendation; reversible.)*
- **A3-22 → the consult mechanism never ships without its governance pairing** (a handshaked
  `{conventions}/consult.md` with `version:`/`consumers:` + a `vlt-lint` check for artifacts
  claiming out-of-authority domain with no consult record). A brief may sequence
  convention-then-mechanism; it may not ship the mode with the pairing merely "planned."
- **A3-22's two zero-machinery prose items ship independently and sooner** — the contract
  prohibition (*a partner never speaks in another partner's voice; it consults, or it cites*) and
  read-and-cite as documented default. They ride the **earliest-shipping build = A4-1**. *(Open
  to re-pinning to A4-2 for thematic coherence; nothing depends on it.)*
- **Evidence debts → six not-blocking, two attached.** Attached: the A4-1 baseline capture (see
  the spike caveat below) and the **B1 upgrade-preserve-path check** on any `dispatch.md` shape
  change (A4-5) — a standing-rule hit, named in the brief, not discovered at implementation.
- **Derive-vs-store (A4-1) → deferred at ideation, then RESOLVED toward DERIVE by SPIKE-2.**

## Spikes (both CLOSED 2026-07-25 — full records in the Arc-3 rulings section)

**SPIKE-1 — the A3-8 calibration re-read. Hypothesis REFUTED; a larger defect found.**

- The audit sampled **all 90 notes** with 76 already absorbed *in sample* — nothing was excluded.
  The "fourth instance of discharging against a non-adopting population" finding is **RETRACTED**;
  that class stays at three.
- **`~21–23%` was never an FP rate**: 21% = vlt-core's union residual as a share of the *naive
  flagged set* (13/62); 23% = vlt-sayari's union *flag rate over population* (3/13). The union's
  measured FP rate was ≈**0%**.
- **Root cause = polarity inversion.** Both calibrations used the union as an **absorption test**
  (citation ∪ body wikilinks ∪ shared-source ⇒ already absorbed ⇒ **exclude**; ripe meant *no*
  linkage). `vlt-lint/SKILL.md:83` fires the same signals inverted. Two further drifts: `topic:`
  overlap replaced the **frontmatter-citation** leg, and the name came from A3-7's different
  `linkage_ripe` ("a newer note cites/links this orphan").
- **It entered at brief time** — `build-20-graduation-queue.md:211-216` — not in the field and not
  at capture, and shipped verbatim into `vlt-lint:83`.

**SPIKE-2 — does the absorption test reproduce? YES, and it tracks the drain.**

- Calibration polarity on today's zone: **8 of 98** (14% of the naive set, matching the audit's
  21%/13-of-90 order). Of the audit's five hand-verified gaps, the **four since graduated** are
  now correctly **excluded**; the **one never drained** still surfaces. The shipped check surfaces
  all of them.
- Shipped polarity re-run: **97 of 98 (99%), 90 already absorbed (≥93% FP)** — recall intact,
  precision ~8%.
- **The 41 was an undercount and the same run destroyed the cause:** exactly 41 notes carried a
  list-form `topic:` at candidacy time; the same sweep auto-fixed **55 scalar → list**
  (`sessions/2026-07-25-150500-lint.md:52`, build-20's own F1 fix). All 98 are list-form now.
- **Derive-vs-store → DERIVE.** No graduation-state key, no `frontmatter@5`, no consumer walk.
  **Derive-first holds unbent.**
- **Baseline caveat (material for A4-1's precondition):** the original 41-hit list is
  **permanently unrecoverable** — its substrate was destroyed by the auto-fix in the same run.
  The closest recoverable baseline is preserved at
  `skills/reports/spike2-projection-baseline-2026-07-25.md` (both polarities, full enumeration).
- **Honest limits:** the candidacy pass is prose-specified and agent-run, not code — the re-run
  *models* it (the exact 41↔41 correspondence is corroboration, not proof); the 8-note ripe set is
  mechanical, without the audit's 9-agent hand-verification (3 of 8 map to audit-identified
  items); **vlt-core only** — vlt-sayari unreadable from this machine.

## Builds

**Numbers follow ship order**, per the Arc-3 convention (build-14 opened that arc, build-23 closed
it). Corrected 2026-07-25 on owner challenge: the first assignment numbered by *filing* order
because ship order was deferred to the spikes. Per the build-17 precedent, a number records
intended order **at assignment** — a build that later slips is not renumbered.

Ship order **`A4-1 → A4-2 → A4-3 → A4-4 → A4-5`** (set 2026-07-25; A4-1 leads on smallest-size +
highest-latent-severity, reversing the "probably last" expectation).

### A4-1 — `linkage_ripe` polarity (A3-23) · **BUILT 2026-07-25** (`4ca619e`, unreleased)

Restore the calibration's polarity and the dropped frontmatter-citation leg; re-state the
acceptance target as an FP-rate-against-FP-rate. Carries the inherited Arc-3 clause, the two
A3-22 prose items, and the preserved baseline. **Brief-time:** derive-vs-store is answered
(derive) — the brief states the call explicitly and may not arrive at it by default; prose
Sources entries and the `orphans` naming tension both need a disposition.

**BUILT 2026-07-25.** All three brief-time questions closed: derive-vs-store → **DERIVE**, stated
explicitly (no graduation-state key, no `frontmatter@5`, no consumer walk — derive-first unbent);
prose `## Sources` entries → **in scope**, shipped as half of the cited leg; the `orphans` naming
tension → **key kept**, prose carries the correction (the name is marked historical). Two owner
calls at build time: **no release** (version held to arc end), and `sources_vs_prose_mismatches`
**filed** as `inbox/2026-07-25-193000-report-slot-with-no-check.md` rather than fixed off-brief.
Two hand-offs to A4-2 are live — see A4-2 below.

### A4-2 — the adoption unit (A3-19) · **BUILT 2026-07-25** (`skills/reports/build-A4-2-adoption-unit.md`, unreleased)

`revisit_after:` in both research-note writers with a two-outcome question; the first real
consumer for `adoption_first_instance:`; **writes the general honest-reporting rule.**
**Brief-time:** where the consuming check lives — bounded by `frontmatter.md:242` (the facet's
absence is *not* a lint finding, so the consumer lives outside lint or the brief revisits `:242`
explicitly and says so); where the honest-reporting rule itself lives.

**Inherited from A4-1 (2026-07-25) — two obligations, do not drop:** (1) the
**verification-by-residue boundary clause** now lives at `vlt-lint`'s candidacy-pass header
(stated, not legislated, because no derive-first doctrine file exists and both candidate homes cost
more than the clause). A4-2 chooses a governance home for the general honest-reporting rule anyway;
both rules are *how a check may establish truth*, so A4-2 either **relocates that clause into that
home or points at it** — it must not create a second home. (2) The new filing
`inbox/2026-07-25-193000-report-slot-with-no-check.md` (`sources_vs_prose_mismatches` — a declared
report key no check fills) is an instance of the silent-zero class: its honesty half is A4-2's
general rule, its missing-check half is a separate wiki-side question for capture to rule.

### A4-3 — the contradiction drain (A3-20) · **BUILT 2026-07-25** (`091b3fb`, unreleased)

Routing, not eligibility: `vlt-lint:105`'s catch-all already admits the class; missing are a
second item template and two pointers from `:69`/`:101`, plus a disposition for the report's
`handled`/`unhandled` split. **Brief-time:** `open`/`deferred` vs drain vs callout-disposition vs
bounding; whether `:69` is bounded at all (this sweep flagged 25, documented 0). The filing's
four-bucket triage is **not** a proposed taxonomy.

### A4-4 — source fidelity (A3-21) · **BUILT 2026-07-26** (`fb04902`, unreleased)

Entity substitution at ingest — prevent / catch / codify / reframe. **Briefed apart from A4-3**
despite sharing `vlt-lint`: one symptom (the Jonah/Alaric pair), two independent causes.
**Brief-time:** whether an entity pass is affordable at ingest scale. The substitution table's
right-hand column may not be cited as verified fact.

**BUILT 2026-07-26.** ODQ #7 closed: **all four shapes ship**, with *codify* load-bearing. The
affordability sub-question ruled — **an entity pass over the source is not affordable; a collision
check over what you are about to write is nearly free** (bound the check by what the write asserts,
not by what the source contains; the prep sub-agent already reads the body, so a located
proper-noun inventory with mention counts is a by-product, not a second pass). The rule is
single-homed at `vault-operating-contract.md` § *Grounding sufficiency — what a claim may rest on*
— **not** a fifth declared-and-unexercised convention file and **not** `wiki-supersession.md` (the
rule governs new claims as much as amendments, and that home would have cost a `2 → 3` bump with a
second four-consumer re-ack one build after the first). **Zero `version:` movement, zero consumer
walk.** Nine F-sites over four files; `vlt-lint-full.js` moved in lockstep with the SKILL on the
new `entity_collisions` key (A4-3's two-producer lesson applied). No new backlog `kind`, no new
frontmatter key (derive-first: the check fires on the collision and names the suspected cause
rather than gating on provenance the vault does not record). Report slot conforms to A4-2's general
honest-reporting rule as its **fourth conformer** and its most exact one — the check's structural
blind spot *is* the filing's own honest limit. `package-lint` A/B/C/E PASS, D skipped (not the
release build). Three deviations recorded in the brief's `status:` — F2 paragraph placement, an
`entity_scan` mention inside a workflow comment, and F5's added back-pointer to the research note's
Open Questions (nothing otherwise returned the writer to the note when a name is declined).
**Nothing outstanding hands forward to A4-5.**

### A4-5 — the consult channel (A3-22) · most gated

A fourth `dispatch` mode **plus** its convention + lint pairing, which do not separate.
**Preconditions:** the B1 upgrade-preserve-path check; the four-site registration surface
(`vlt-dispatch/SKILL.md:4`, `:56`, `:120`, `module-help.csv:11` — free-text fields stay quoted).
**Brief-time:** payload shape, the convention's preconditions, and the five named risks
(confabulated authority, `thread.md` rot, boundary erosion, human-out-of-the-loop, durability).
Deferred by the filing and not reopened: `dialogue`, `convene`, `summon`.

## Deferred acceptance ledger (Arc 4)

Per convention, acceptance rides the next ordinary vlt-core upgrade; per-build checks are appended
at brief time.

- [x] **INHERITED FROM ARC 3 — build-20 `linkage_ripe` FP-rate (graded FAILED 2026-07-25).**
  Discharges only on A4-1's fix, measured against the **restated** target: FP rate hand-verified
  on a mature research zone, near ≈0% and never exceeding the naive ~79%. The measurement must
  be **hand-verified**, not self-reported by the same pass under test — the original clause failed
  partly because a set-reduction ratio was read as an FP rate. Baseline for comparison:
  `skills/reports/spike2-projection-baseline-2026-07-25.md`.
  - *STILL-OPEN 2026-07-26 (discharge run 1).* The 0.8.0 upgrade landed (vlt-core
    `_agent/upgrade-ledger.md`, `[2026-07-26 12:50] vlt 0.7.0 → 0.8.0 (own)`), but this clause's
    evidence is a **measurement**, not an install: no `vlt-lint` has run since (latest lint sitting
    `_agent/sessions/2026-07-25-150500-lint.md`, pre-upgrade). **Discharging event:** one full
    `vlt-lint` on vlt-core, then the surfaced `linkage_ripe` set hand-verified against the 07-25
    baseline. **Trigger:** owner runs the lint.
  - **DISCHARGED 2026-07-27 (discharge run 2).** The full lint ran 2026-07-26 18:05 (128 pages, 8
    clusters, `coverage_caps: []`); its report block carries `linkage_ripe: 10 of 103` and
    `research_zone: "103 notes scanned; 1 carries revisit_after:"`. **FP rate hand-verified
    factory-side, independently of the pass under test** (the clause's own requirement): each of the
    10 surfaced notes was checked against all three absorption legs across the live wiki **and**
    `_archive/` — named in frontmatter `sources:` (0 hits), inbound body `[[wikilink]]` (0 hits), and
    shared `sources:` entry (sampled 4 of 10 on their actual source URLs — `youtube-transcript-api`,
    `perfect-chess-opening-repertoire-black`, the two World-Cup standings URLs — 0 hits). **0 false
    positives of 10 → FP rate ≈0%**, against the naive baseline of ~79%
    (`skills/reports/spike2-projection-baseline-2026-07-25.md`) and against the 07-25 run's own
    41-hit set that resolved **entirely** to already-graduated notes. The measurement is not
    self-reported: the lint asserted the set, the audit re-derived it from disk.
- [x] **A4-1 (linkage-polarity, briefed 2026-07-25):** on the next ordinary vlt-core upgrade +
  full lint — (1) the inherited build-20 clause above discharges here, measured as stated there
  (hand-verified FP rate, near ≈0%, never exceeding the naive ~79%); (2) **surfacing rate
  collapses** — `linkage_ripe` surfaces on the order of **~8 of ~98** notes (≈8% of the research
  zone / ~14% of the naive orphan set), not ~97; a rate near population is the failure signature;
  (3) **the projection tracks the drain** — notes graduated since the 07-11 audit are not
  surfaced, the never-drained one still is (same disk, opposite behavior from the 07-25 run);
  (4) **never-auto-promote survives** — every candidate surfaced for a human, none promoted by
  lint (this clause discharged on the 07-25 run and must not regress under the new polarity);
  (5) **the two A3-22 prose items reach the field** — after upgrade the installed contract carries
  the partner-voice prohibition and read-and-cite as documented default, with any local overlay
  untouched; (6) **second-vault check, non-blocking** — if vlt-sayari becomes readable, confirm a
  same-order surfacing rate (the calibration's 3/13); SPIKE-2's measurement is vlt-core only.
  Brief: `skills/reports/build-A4-1-linkage-polarity.md`.
  - *Split, annotated 2026-07-26 (discharge run 1).* **Upgrade-side DISCHARGED:** (5) the installed
    `_meta/vault-operating-contract.md` carries both A3-22 prose items in `## Sessions, sittings, and
    hand-offs` — *Authority boundary at the seam — a partner never speaks in another partner's voice*
    and *Read-and-cite is the documented default* — with no overlay to disturb (`_agent/conventions/`
    holds `.baseline/` only; ledger records overlays none, base divergence none).
    **STILL-OPEN:** (1)(2)(3)(4) all wait on the first post-upgrade full `vlt-lint` — none has run
    (latest lint sitting 2026-07-25 15:05, pre-upgrade); **trigger:** owner runs the lint, then
    hand-verifies the surfaced set. (6) **non-blocking** — vlt-sayari *is* readable at
    `~/Vaults/vlt-sayari` but is still on **0.6.0** (its upgrade ledger's last entry
    is `[2026-07-09 12:13] vlt 0.4.0 → 0.6.0`; no `consult.md` in its `_meta/conventions/`);
    **trigger:** owner upgrades vlt-sayari to 0.8.0.
  - **DISCHARGED 2026-07-27 (discharge run 2) — every blocking clause; (6) is field-contingent and
    does not gate closeout.** Evidence: the 2026-07-26 18:05 full-lint report block.
    (1) discharges as recorded on the inherited item above — FP ≈0%, hand-verified factory-side.
    (2) **the surfacing rate collapsed**: `linkage_ripe` surfaced **10 of 103** notes (**≈9.7%**),
    inside the calibrated 8–14% band and against the briefed prediction of ~8 of ~98 — not the ~97
    that a near-population rate (the stated failure signature) would have produced. (3) **the
    projection tracks the drain** — same disk, opposite behavior from 07-25: that run surfaced 41
    notes that all resolved to *already-graduated* ones; this run surfaces 10 of which **none** is
    absorbed by any live or archived page. The set is disjoint from the graduated population, which
    is exactly the clause's test. (4) **never-auto-promote survives the polarity change** —
    `linkage_ripe` sits under `flag_for_human`, and `fix_now` contains no promotion of any kind (its
    only entries are one summary trim and three supersession/self-link/status repairs). (5)
    discharged run 1. **(6) remains open, non-blocking** — vlt-sayari still on 0.6.0; **trigger:**
    owner upgrades it to 0.8.0.
  - *Run 3, 2026-07-29:* (6) armed — vlt-sayari upgraded 0.6.0 → 0.8.0 (`[2026-07-27 10:19]` in its
    `_agent/upgrade-ledger.md`, @ 557347f) and readable at `~/Vaults/vlt-sayari`, but
    no post-upgrade `vlt-lint` has run there (no session since 07-27 carries lint report keys), so the
    surfacing-rate comparison stays open, still non-blocking. **Trigger:** first sayari full lint.
- [x] **A4-2 (adoption-unit, briefed 2026-07-25):** on the next ordinary vlt-core upgrade + the
  sittings that follow — (1) **both write paths ask** — the installed `vlt-research` and
  `vlt-ingest` both carry `revisit_after:` in their research-note templates plus the two-outcome
  ask, and the next note written by **each** path shows the partner either setting a date or
  naming the decline in-flow (the ingest path is the one that matters — it is the majority path
  and the one that could not see the slot); (2) **adoption moves off zero** — within the first
  sittings after upgrade at least one newly written research note carries `revisit_after:`,
  breaking the 0-of-96 (days-to-first-check: the first research or ingest write; a run of new
  notes with no date **and** no spoken decline is the failure signature — the ask is being
  skipped, not answered); (3) **the candidacy pass reports honestly** — the next full `vlt-lint`
  run carries the `research_zone:` denominator above `linkage_ripe`/`revisit_due` (M notes
  scanned, N carrying the key) and no bare zero appears on either slot (A3-19 shape 3 discharged
  by conformance to the general rule, not by a bespoke fix); (4) **the adoption facet has a live
  consumer** — the post-flight report emits `convention_adoption:` three-valued per convention,
  `spec.md` + `wiki-consolidation.md` reporting *declared, no first instance yet* and the five
  `checked` conventions *axis not declared*, with the same line appended to the upgrade ledger so
  the state is comparable at the next upgrade; (5) **the stamp is reachable** — if a first live
  instance occurs in the window (first spec minted under `spec.md`, first consolidation under
  `wiki-consolidation.md`), `vlt-mint` stamps `adoption_first_instance:` with a dated reference,
  the mint decision log records it, and the following upgrade reports that convention *adopted*
  — **non-blocking if no instance occurs**, but the absence must show as *declared, no first
  instance yet*, never as silence; (6) **single home holds in the field** — the installed
  operating contract carries the honest-reporting rule **and** the derive-first boundary clause,
  the installed `vlt-lint` carries a pointer with no restated wording, and any vault-local
  overlay is untouched (`overlays_intact`); (7) **second-vault check, non-blocking** — if
  vlt-sayari becomes readable, confirm both writers carry the key there and its adoption line
  reports the same three-valued shape (A3-19's honest limit is one vault + four post-fix notes;
  the fix does not wait on it). Brief: `skills/reports/build-A4-2-adoption-unit.md`.
  - *Split, annotated 2026-07-26 (discharge run 1).* **Upgrade-side DISCHARGED:** (1, install half)
    both write paths carry the slot **and** the ask — `.claude/skills/vlt-research/SKILL.md:71` +
    `:75` and `.claude/skills/vlt-ingest/SKILL.md:94` + `:98` (*Decide `revisit_after:` before you
    write — two outcomes, both legitimate*). (3, denominator half) installed
    `vlt-lint/SKILL.md:175` carries `research_zone: <M notes scanned; N carry revisit_after:>` above
    the candidacy slots. (4) the adoption facet has a live consumer — the upgrade's post-flight
    emitted `convention_adoption:` three-valued and the same line is in the ledger entry: `consult` /
    `spec` / `wiki-consolidation` *declared, no first instance yet*; `extraction`, `frontmatter`,
    `wiki-index`, `wiki-supersession`, `write-verification` *axis not declared* — the briefed shape,
    with `consult` a third declarant contributed by A4-5. (6) single home holds — the contract's
    `## Honest reporting — what a check may claim` carries the rule **and** the derive-first boundary
    clause, installed `vlt-lint`'s candidacy pass points at it verbatim-free (*"stated once in the
    operating contract … read it there, not from memory"*), overlays intact.
    **STILL-OPEN:** (1, field half) + (2) adoption off zero — **0 of 102** notes in
    `_agent/research/` carry `revisit_after:`, and every note on disk predates the upgrade (newest
    `2026-07-26-121947-…`, 12:19 < 12:50); **trigger:** the next `vlt-research` write **and** the
    next `vlt-ingest` write (each path must show it). (3, run half) **trigger:** owner runs the full
    lint. (5) **non-blocking** — no spec mint or consolidation post-upgrade. (7) **non-blocking** —
    vlt-sayari still on 0.6.0.
  - *Split, re-annotated 2026-07-27 (discharge run 2).* **Newly DISCHARGED:** (2) **adoption moved
    off zero** — `_agent/research/2026-07-26-165816-huberman-layne-norton-eating-for-health-fat-loss.md:17`
    carries `revisit_after: 2027-01-26`, written in-flow during the 17:09 ingest sitting. The failure
    signature (a run of new notes with no date **and** no spoken decline) did not fire. (1, **ingest
    half**) the majority path — the one that could not see the slot — now demonstrably sets the date.
    (3) **the candidacy pass reports honestly** — the 18:05 report block carries
    `research_zone: "103 notes scanned; 1 carries revisit_after: (2027-01-26, not due)"` above both
    candidacy slots, and `revisit_due: []` renders **beside its denominator**, not as a bare zero.
    A3-19 shape 3 discharged by conformance to the general rule, as briefed.
    **STILL-OPEN:** (1, **research half**) — `vlt-research` has not written since the upgrade (latest
    research sitting `_agent/sessions/2026-07-26-122309-research.md`, 12:23 < 12:50); the clause names
    *each* path, and only the ingest path has exercised. **Trigger:** the next `vlt-research` write.
    (5) **non-blocking**, but see the observation below — it now has a **second instance**.
    (7) **non-blocking** — vlt-sayari still on 0.6.0.
  - *Observation, routed to `inbox/` rather than graded (2026-07-26).* The upgrade's own report
    flagged `spec.md` reading `adoption_first_instance: null` while `_agent/specs/` already holds
    **two** live specs (`2026-06-13-health-coach-to-chef-nutrition-spec.md`,
    `2026-06-21-creative-to-chef-meal-plan-format.md`, both from the proto-spec retrofit). Clause 5
    stays *reachable* — the stamp fires at the next mint — but the axis will read *declared, no first
    instance yet* indefinitely for a convention with instances on disk. Module signal, not an A4-2
    failure — **drafted as a filing, pending owner confirm** (`…-adoption-stamp-unreachable-for-pre-existing-instances.md`);
    routes into the next `inbox-capture` once filed.
  - *Observation strengthened 2026-07-27 (discharge run 2) — the drafted filing now has a **second,
    sharper instance**, and it is not a retrofit artifact.* `consult@1` had its **first live
    exercise** on 2026-07-26 (two consults, `_agent/dispatch.md` 19:21) and
    `_meta/conventions/consult.md` still reads `adoption_first_instance: null`. The vault's own
    operator recorded why it stays that way (`_agent/sessions/2026-07-26-180500-lint.md`, Watches):
    *"Editing it is a shipped-base change that would trip `convention_base_divergence` — so it wants
    an overlay or an upstream fix, not a quiet edit."* This is materially worse than the `spec.md`
    instance the run-1 draft captured: there the instances predated the axis, here the axis shipped
    **first** and the very build that declared it produced the instance the same week — and the
    stamp still cannot fire, because the only surface that writes it is `vlt-mint`'s ceremony and a
    consult is not a mint. The A4-2 (5) clause's promise that *"the stamp is reachable"* holds for
    mint-borne conventions only. **The drafted filing should be widened to cover both instances
    before it is filed** — it is a reachability gap in the adoption axis, not a retrofit gap.
  - **DISCHARGED 2026-07-29 (discharge run 3) — every blocking clause.** (1, research half) the
    research path exercised: two `vlt-research` writes on 2026-07-27, both notes carrying the key —
    `_agent/research/2026-07-27-100227-agent-harness-architecture-pi-case-study.md:54` and
    `…-112419-homemade-training-treats-for-penny.md:36`, each `revisit_after: 2026-10-27`, with the
    session note recording the in-flow decision (*"set deliberately: fast-moving domain, three
    months"* — `_agent/sessions/2026-07-27-100227-research.md:48`). Both write paths have now asked
    and answered. (7) second-vault check, split: **writers half discharged** — sayari's installed
    `vlt-research/SKILL.md:71`+`:75` and `vlt-ingest/SKILL.md:94`+`:98` carry the key and the
    two-outcome ask; **adoption-line half FAILED** — sayari's 0.8.0 upgrade-ledger entry carries
    **no** convention-adoption line (`grep -i adoption` → 0 hits across its whole ledger) against
    the installed `vlt-upgrade:112` never-omit rule; owner-confirmed and filed as
    `inbox/2026-07-29-120003-sayari-upgrade-omitted-convention-adoption-line.md`. (5) stays
    non-blocking; the widened adoption-stamp draft owner-confirmed and filed as
    `inbox/2026-07-29-120001-adoption-stamp-unreachable-beyond-mint.md`. Ticked with both
    non-blocking residues routed as filings — nothing left here waits on a trigger.
- [x] **A4-3 (contradiction-drain, briefed 2026-07-26):** on the next ordinary vlt-core upgrade +
  the first full lint that follows — (1) **both pointers reach the field** — the installed
  `vlt-lint` routes contradictions at Step 4 and points at the callout convention, and the
  do-not-auto-apply line names the drain symmetrically with merges (the one-sentence asymmetry the
  filing found is gone from the installed text); (2) **the drain actually runs** — at least one
  contradiction dispositioned `adjudicable` is filed to `{backlog}` as `maintenance` or
  `knowledge-gap`, mentioned in-flow, naming what would close it, and appears in `backlog_filed:`
  (failure signature: entries in `contradictions_deferred` with an empty `backlog_filed` — the
  disposition landed, the drain did not); (3) **the split is real and derived, not inferred** — the
  report emits `contradictions_open` / `contradictions_deferred` / `contradictions_undispositioned`
  and **no** `contradictions_handled`, and three spot-checked entries each trace to a
  `**Disposition:**` line written on the page; **the bulk of the prior 63 `handled` must land
  `undispositioned`** on the first sweep (they predate the convention — that is the honest answer),
  and a first sweep that classifies all 63 into `open`/`adjudicable` **is** the failure signature;
  (4) **the bound is stated, so the skip is visible** — `contradiction_scan:` carries pages
  compared, documented count, undispositioned count, and the count this run **declined** to
  document, with no bare zero on any contradiction slot (A3-20 shape 4 discharged by conformance to
  the general honest-reporting rule, not by a bespoke fix); (5) **report and backlog stop
  disagreeing** — at least one documented contradiction whose vault backlog already carries an open
  item now reads `deferred` rather than health (the Schottenheimer-class property; **non-blocking**
  if that pair has since resolved — the property under test is report↔backlog agreement, not the
  pair); (6) **handshake + durability in the field** — installed
  `_meta/conventions/wiki-supersession.md` at `version: 2` with its four consumers, all four
  installed skills pinning `@2`, `convention_drift:` empty, any vault-local
  `wiki-supersession.overlay.md` untouched and no new `convention_base_divergence` (B1 posture);
  (7) **second-vault check, non-blocking** — if vlt-sayari becomes readable, confirm the three slots
  and the denominator render there too; a vault with **no** contradictions must still emit
  `contradiction_scan:` with its denominator rather than a silent empty report (A3-20's honest limit
  is one vault / one sweep and the mechanism is size-sensitive; the fix does not wait on it).
  Brief: `skills/reports/build-A4-3-contradiction-drain.md`.
  - *Split, annotated 2026-07-26 (discharge run 1).* **Upgrade-side DISCHARGED:** (1) installed
    `vlt-lint/SKILL.md:69` routes contradictions to the callout convention with its
    `open`/`adjudicable` vocabulary and names the `{backlog}` drain **symmetrically with merge
    candidates** (*"filed to `{backlog}` in Step 4 — that is its drain, exactly as a merge
    candidate's is"*) — the filing's one-sentence asymmetry is gone. (3, shape half) + (4, shape
    half) the report block emits `contradiction_scan:` (`:184`) and
    `contradictions_open`/`_deferred`/`_undispositioned` (`:186-188`), and **no**
    `contradictions_handled` survives anywhere installed (grep over `.claude/` + `_meta/` → zero
    hits), with **both producers** agreeing (`vlt-lint-full.js:276-278`). (6) handshake + durability
    in the field — `_meta/conventions/wiki-supersession.md` at `version: 2`,
    `consumers: [vlt-ingest, vlt-lint, vlt-extract, vlt-track]`, and all four installed skills
    pinning `wiki-supersession@2`; overlays none, no `convention_base_divergence` (ledger: all 8
    bases == baseline at close).
    **STILL-OPEN:** (2) the drain actually running, (3, sweep half) the bulk of the prior 63
    `handled` landing `undispositioned`, (4, run half) the stated bound, (5) report↔backlog
    agreement — all four wait on the first post-upgrade full `vlt-lint`. **Zero** callouts currently
    carry a `Disposition:` line (grep over `wiki/` + `_agent/research/`), which is the expected
    pre-sweep state and makes the 63→`undispositioned` prediction the sharp thing to watch.
    **Trigger:** owner runs the lint. (7) **non-blocking** — vlt-sayari still on 0.6.0.
  - *Split, re-annotated 2026-07-27 (discharge run 2).* **Newly DISCHARGED:** (2) **the drain
    actually ran** — `contradictions_deferred` carries two entries, **each ending `| backlog filed`**,
    and `backlog_filed: 5` agrees; both were mentioned in-flow and each names what would close it
    (*"closes when the cross-link is qualified or a pan material is named"*; *"closes when both state
    one sourced window"*). The failure signature — entries in `contradictions_deferred` with an empty
    `backlog_filed` — did not fire. (3, **derivation half**) the split is derived, not inferred: all
    four on-page `> **Disposition:** adjudicable` lines exist on disk
    (`carne-asada.md:75`, `cooking-with-carbon-steel.md:68`, `calf-strain.md:195`,
    `acute-soft-tissue-injury-management.md:111`) — both pages of each pair, and each report entry
    traces to one. (4) **the bound is stated** — `contradiction_scan: "128 pages compared in 8
    clusters; 16 surfaced, 2 documented (4 callouts, both pages each), 14 surfaced-but-declined this
    run"` carries pages, documented count and **the count this run declined**, with no bare zero on
    any contradiction slot. (5) **report and backlog stopped disagreeing** — both deferred entries
    are documented contradictions carrying open backlog items and now read `deferred`, never health;
    the `contradictions_handled` bucket that would have called them healthy no longer exists in
    either producer.
    **(3, sweep half) — PREDICTION REFUTED AT THE PREMISE, PENDING OWNER RULING.** The clause
    predicted *"the bulk of the prior 63 `handled` must land `undispositioned`"* and named a sweep
    that classified all 63 into `open`/`adjudicable` as the failure signature. **Neither happened:**
    `contradictions_undispositioned: 8`, `contradictions_open: []`, two deferred. The audit's
    reconstruction of where the other ~55 went: a callout census of the live wiki returns
    **56 `[!superseded]`, 19 `[!stale]`, 4 `[!contradiction]`** — so the Arc-3-era count of
    *"63 already documented"* was overwhelmingly **supersessions counted as contradictions**, not
    contradictions awaiting disposition. The prior bucket was not merely terminal, it was
    **cross-class** — which is a *stronger* confirmation of the defect A4-3 was built to fix than the
    prediction it was written against, and the new report is correct to count only genuine
    contradiction callouts (4 dispositioned + 8 pre-existing undispositioned = 12). **The clause's
    letter fails; its premise is what was wrong.** Owner ruling wanted on whether to discharge it as
    *restated* (recommended — the honest sweep is the one that separates the classes) or to hold it.
    (7) **non-blocking** — vlt-sayari still on 0.6.0.
  - **DISCHARGED 2026-07-29 (discharge run 3) — (3, sweep half) owner-ruled discharged as
    restated:** the clause's letter fails but its premise was wrong — the callout census (56
    `[!superseded]` / 19 `[!stale]` / 4 `[!contradiction]`) shows the Arc-3 "63 handled" was
    overwhelmingly supersessions miscounted as contradictions, and the class-separating sweep is the
    honest outcome A4-3 exists to produce. Supporting evidence since run 2: the 2026-07-27 ingest
    ran the disposition machinery organically in-flow (`_agent/sessions/2026-07-27-114604-ingest.md:20`
    — liver/vitamin-A → `adjudicable` with a backlog knowledge-gap filed naming what closes it;
    garlic → `open`, documentation as the resolution — a second live exercise of the drain). (7)
    stays non-blocking: sayari is on 0.8.0 with the three slots installed
    (`vlt-lint/SKILL.md:184-188`) but no post-upgrade lint has rendered them; **trigger:** first
    sayari full lint.
- [ ] **A4-4 (source-fidelity, briefed 2026-07-26):** on the next ordinary vlt-core upgrade + the
  sittings and first full lint that follow — (1) **the rule reaches the field** — the installed
  `_meta/vault-operating-contract.md` carries *Grounding sufficiency — what a claim may rest on*
  with the single-mention rule, the suspect-the-source clause and the fidelity-vs-contradiction
  distinguisher, any vault-local overlay untouched (`overlays_intact`, B1 posture) and no new
  `convention_base_divergence`; (2) **ingest looks before it writes** — the next ingest of a
  machine-transcribed source shows the collision check as a visible beat, either "no collision"
  stated or a collision named in-flow (failure signature: a transcript ingest that canonicalizes
  new person-names with no fidelity beat visible in the run); (3) **a declined name is recoverable,
  not lost** — where a name is declined, all three residues exist: the claim recorded without the
  name, the flagged string in the research note's Open Questions (as rendered, with its location),
  and a backlog item whose `why` names *suspected substitution in a machine-transcribed source* and
  whose `closes when` names the verifying act (**non-blocking if no collision occurs in the
  window**; a run that declines a name and files nothing is a failure); (4) **the split still
  protects the context** — the next heavy (>~15k word) ingest returns a located proper-noun
  inventory with mention counts and **no** corrections or "likely intended" candidates, with the raw
  body still out of the interpreting context (invariant 3 intact); (5) **lint catches what ingest
  missed, in its own slot** — the next full `vlt-lint` emits `entity_collisions:` and
  `entity_scan:`, and if the Jonah/Alaric pair is still on disk it surfaces **as an entity collision
  and not in `contradictions:`** (failure signature: the same pair in both slots, or a collision
  still filed as a contradiction — the check surfaces the question; neither the brief nor this
  ledger takes a position on which name is correct); (6) **the report is honest about what it cannot
  see** — `entity_scan:` carries the population compared (pages, and clusters in full mode) **and**
  names the by-construction blind spot (a substitution that entered once and was never
  contradicted), with no bare zero on either fidelity slot (A3-21 shape 3 discharged by conformance
  to the general honest-reporting rule, not by a bespoke fix); (7) **both producers agree in the
  field** — a full-mode sweep large enough for the `vlt-lint-full` fan-out (>~30 pages) emits the
  same two keys as an inline sweep, with the cluster cap surfaced in `coverage_caps` when it
  truncates (failure signature: keys present inline, absent or denominator-less in full mode —
  A4-3's two-producer lesson regressing); (8) **second-vault check, non-blocking** — if vlt-sayari
  becomes readable, confirm the contract section installed there and that its lint emits both slots,
  a vault with **no** collisions still emitting `entity_scan:` with its denominator rather than a
  silent empty report (A3-21's honest limit is one vault / one programme / one domain; the fix does
  not wait on it, and no check may treat an absence of collisions elsewhere as evidence about the
  rate). Brief: `skills/reports/build-A4-4-source-fidelity.md`.
  - *Split, annotated 2026-07-26 (discharge run 1).* **Upgrade-side DISCHARGED:** (1) the installed
    `_meta/vault-operating-contract.md` carries `## Grounding sufficiency — what a claim may rest on`
    with the single-mention rule, *suspect the source, not the record*, the
    substitution-vs-mangling distinction, the decline-the-name/keep-the-claim write rule, the
    fidelity-vs-contradiction distinguisher and the stated honest limit; overlays intact, no new
    `convention_base_divergence`. (5, slot half) + (6, slot half) `vlt-lint/SKILL.md:189-190` emit
    `entity_scan:` (blind spot named inline) and `entity_collisions:`, with the one-finding-one-slot
    precedence stated at `:69` and the blind spot restated in the check body at `:74`. (7, install
    half) both producers carry it — `vlt-lint-full.js:109` (required), `:115` (schema), `:236`
    (prompt, with precedence), `:282` (reduce).
    **STILL-OPEN:** (2) the ingest collision beat, (3) the three residues on a declined name
    (*non-blocking*), (4) the heavy-ingest located inventory — all wait on the **next ingest
    sitting**; none has occurred since the upgrade (latest `_agent/sessions/2026-07-26-115754-ingest.md`,
    11:57 < 12:50). **Trigger:** the owner's next ingest, ideally of a machine-transcribed source.
    (5, run half) + (6, run half) wait on the first full lint; (7, field half) additionally needs a
    >~30-page full-mode sweep. (8) **non-blocking** — vlt-sayari still on 0.6.0.
  - *Split, re-annotated 2026-07-27 (discharge run 2).* **Newly DISCHARGED:** (2) **ingest looked
    before it wrote** — the 17:09 sitting ingested a machine-transcribed source (YouTube
    auto-captions, no speaker labels) and the fidelity beat is visible in-flow
    (`_agent/sessions/2026-07-26-170920-ingest.md:53`, *"Three study-author names declined"*), with the
    note itself opening on an explicit attribution caveat. (3) **a declined name is recoverable, not
    lost** — all three residues exist for each of the three declined names: the claims are kept
    without attribution; the flagged strings sit in the note's Open Questions **as rendered, with
    their locations** (`…-165816-…md:101-105`, each with a mention count and a transcript line
    number); and `_agent/backlog.md:30` carries a `knowledge-gap` item whose `why` names
    *Grounding sufficiency* and a single-mention proper noun in an auto-captioned source, and whose
    **Closes when** names the verifying act (*"any written source names them — the episode's show
    notes, a citation, or the description of the original full-length episode"*). It also records the
    near-miss that makes the rule load-bearing — `[[tdee-estimation]]`'s existing *"Hall et al. 2013"*,
    a compatible record and exactly the partial match that invites completing a surname from recall.
    (6) **the report is honest about what it cannot see** — `entity_scan: "128 pages compared in 8
    clusters; single-mention sub[stitutions invisible] by construction, and a cluster-bounded sweep
    did not compare every pair"` carries the population **and names two blind spots**, one more than
    the clause required. (7) **both producers agree in the field** — the sweep was full-mode at 128
    pages (well past the ~30-page fan-out threshold), emitted both keys with denominators, and
    reported `coverage_caps: []`; the regression the clause feared (keys present inline, absent or
    denominator-less in full mode) did not occur.
    **(5) — FAILED on its named subject, pending owner confirm on the filing.** The slot fired and
    found **three real collisions** (Tariq Woolen; Anthony Campanile; Miyabi's cultivar count,
    correctly read as a probable supersession wearing a collision's clothes). But the clause names
    **the Jonah/Alaric pair** as its test case, that pair **is** still on disk
    (`_agent/wiki/los-angeles-rams.md:77`, a `[!stale]` *"Which Jackson?"* callout against
    `[[nfl-2026-offense-rankings]]`), and it **did not surface in `entity_collisions`**. The stated
    failure signature did not fire — it is not in both slots, and it is not filed as a contradiction
    (it is a `[!stale]` name-verification callout, already tracked in `{backlog}`) — so the check did
    not mis-classify it. It simply could not see it, for the reason the report itself states: the
    sweep is **cluster-bounded and did not compare every pair**. The sharp detail: the page's own
    callout says the Rams instance *"Tracked in `{backlog}` alongside the Seahawks-coordinator
    instance — one lookup settles both,"* and the check **found the Seahawks instance and missed its
    twin**. A known, already-documented, explicitly-paired collision is the cheapest regression test
    the check could have, and cluster bounding lost it. **Drafted as a filing, pending owner
    confirm** — the gap is that entity-collision coverage is silently pair-incomplete, and unlike
    the single-mention blind spot (which is by construction) this one is a *sweep-shape* limit that
    a cluster-aware second pass over already-flagged name callouts would close.
    **STILL-OPEN:** (4) **the heavy-ingest split** — the clause arms only above ~15k words and the
    window's ingest was **6,307 words** (`sources/transcripts/2026-06-25-essentials-…md`), so the
    located-inventory-without-corrections behavior was never exercised. Not a miss; the trigger never
    fired. **Trigger:** the next >~15k-word ingest. (8) **non-blocking** — vlt-sayari still on 0.6.0.
  - *Run 3, 2026-07-29.* (5) **FAILED confirmed by owner** — filed as
    `inbox/2026-07-29-120002-entity-collision-coverage-pair-incomplete.md`; routes into the next
    `inbox-capture`. (4) still open: the only ingest since run 2 (2026-07-27 11:46) was a
    partner-relayed research note, not a transcript ingest — no >~15k-word source in the window;
    **trigger unchanged** (the next >~15k-word ingest). (8) second-vault check, split: **install
    half discharged** — sayari's contract carries `## Grounding sufficiency`
    (`_meta/vault-operating-contract.md:262`) and its `vlt-lint/SKILL.md:189-190` emit
    `entity_scan:`/`entity_collisions:`; **run half open** — no post-upgrade lint has rendered them
    there; **trigger:** first sayari full lint (still non-blocking).
  - *Run 4, 2026-07-29 (heavy-ingest trigger fired).* (4) **DISCHARGED — the split protected the
    context at scale.** The 13:25 vlt-core sitting ingested "NFC South Preview & Predictions"
    (Mina Kimes Show) at **16,215 words / 215 turns**
    (`sources/transcripts/2026-07-29-nfc-south-preview-predictions-mina-kimes-show.md`, `wc -w`
    16,249) — the first ingest above the ~15k arm since the clause was written. All three
    behaviors held: the prep agent deposited the cleaned body and **interpretation ran on fresh
    context per the capability** (`_agent/sessions/2026-07-29-132500-ingest.md:17-18` — invariant
    3 intact, the raw body never entered the interpreting context); the research note returns a
    **located proper-noun inventory** of ~10 declined names *as rendered, with transcript line
    locations and single/multi-mention counts*
    (`_agent/research/2026-07-29-125602-nfc-south-preview-kimes-greg.md:115-125` — e.g. the Bucs
    HC rendered only "Todd B's/Todd Bulls/Todd Bowls/Todd BS" at L51–L365, never cleanly,
    role-only in every fold); and the inventory offers **no corrections and no "likely intended"
    candidates** — each name closes on "a roster or written source," the note states
    *"substitution suspected for none (these are mangle-class, not substitution-class), but
    spellings are not trusted,"* and the only canonicalizations (Mayfield, Staley, Chase Young,
    Vea) were multi-mention-consistent **and** collision-checked per the rule's own carve-out
    (`:58-60`). (5) unchanged — FAILED, filed, and its signal now **captured as A4-21** in the
    Arc-5 seed batch; the fix rides Arc 5. (8) run half unchanged — **trigger:** first sayari
    full lint (non-gating). **The box stays unchecked solely on (5)'s FAILED clause.** Every
    trigger-bearing gating tail on this ledger has now fired.
- [x] **A4-5 (consult-channel, briefed 2026-07-26):** on the next ordinary vlt-core upgrade
  (0.7.0 → **0.8.0**, the arc's release) + the sittings and first full lint that follow — (1) **the
  whole surface reaches the field** — installed `_meta/conventions/consult.md` at `version: 1`,
  `enforcement_stage: checked`, `adoption_first_instance: null`, plus
  `.claude/workflows/vlt-consult.js`, a `vlt-dispatch` offering **four** modes and a help registry
  whose `DP` row says four; any later `consult.overlay.md` untouched and no new
  `convention_base_divergence` (B1 posture) — *failure signature: the convention is in the repo but
  not in `_meta/conventions/`, i.e. the `vlt-setup:144` enumeration was missed*; (2) **a real
  consult runs end to end and the caller keeps the wheel** — the sitting yields **one** session note
  (the caller's), the consulted partner writes none, and the raw answer appears **attributed, in its
  own block**, before the caller's use of it (failure signature: two session notes for one sitting —
  the consult was treated as a hand-off — or an answer arriving already digested into the caller's
  voice); (3) **the record shows consult traffic and the board does not** — `_agent/dispatch.md`
  gains a `consult: <from> → <to>` block whose pointer is written **checked (`- [x]`)**, the same
  run's `ledger` does not list it as open, and the `{log}` line is tagged with the **caller** while
  naming the consulted partner in its summary (failure signature: a consult sitting open in a
  partner's slice forever); (4) **the refusals are real, not decorative** — at least one consult
  returns something other than `answer` and the caller routes it correctly (`needs-work` exits
  through `relay`, never the consulted partner doing the work); **non-blocking if every consult in
  the window legitimately answers**, but consults that *only ever* return `answer` are the
  confabulated-authority signature and must be inspected, not assumed healthy; (5) **the bound holds
  on memory** — the consulted partner's `thread.md` gains an entry **only** where the consult changed
  its stance (failure signature: one `thread.md` line per consult — the rot the bound exists to
  prevent); (6) **the check is live and exercised by construction** — the first full `vlt-lint`
  emits `authority_scan:` and `consult_missing:`, and a `{specs}` artifact binding a partner other
  than its owner either shows a consult record or surfaces as `consult_missing`; **non-blocking if
  no such spec exists in the window**, but the absence must render as `authority_scan:` with its
  denominator, **never as silence**; (7) **the report is honest about what it cannot see** —
  `authority_scan:` names the blind spot beside the count (out-of-authority claims outside `{specs}`
  are invisible by construction), no bare zero on either slot — A3-22 discharged by conformance to
  A4-2's general honest-reporting rule as its **fifth conformer**, not by bespoke wording;
  (8) **nothing else moved** — `convention_drift:` empty (only `consult@1` is new; no existing
  convention re-acked), `spec.md` still `version: 1` with its four consumers, and `spec_candidate`
  does not fire on a spec whose only extra dispatch traffic is consults; (9) **second-vault check,
  non-blocking** — if vlt-sayari becomes readable, confirm the four modes and both report slots
  installed there (A3-22's evidence is one vault, taken as filed and never verified factory-side;
  nothing here may assert what vlt-sayari's state was); (10) **the release itself** — installed
  `module.yaml` reports `0.8.0`, the marketplace manifest agrees, and tag `v0.8.0` exists on `main`
  with the `package-lint` PASS line in its release commit.
  Brief: `skills/reports/build-A4-5-consult-channel.md`.
  - *Split, annotated 2026-07-26 (discharge run 1).* **Upgrade-side DISCHARGED:** (1) the whole
    surface reached the field — `_meta/conventions/consult.md` at `version: 1`,
    `enforcement_stage: checked`, `adoption_first_instance: null`,
    `consumers: [vlt-dispatch, vlt-lint]`; `.claude/workflows/vlt-consult.js` present; installed
    `vlt-dispatch` offering **four** modes (`:11`, `:54`, description line) and
    `_bmad/module-help.csv:16`'s `DP` row naming all four. **The `vlt-setup:144` failure signature
    did not fire** — the ledger records `consult.md` + `vlt-consult.js` seeded and the skill-asset
    manifest regenerated 43 → 46 entries; no overlay, no new `convention_base_divergence`.
    (6, slot half) + (7, slot half) `vlt-lint/SKILL.md:87-89` carries the consult-precondition check
    with its blind spot stated in the check's own text; `:191-192` emit `authority_scan:` and
    `consult_missing:`. (8) nothing else moved — `spec.md` still `version: 1` with its four
    consumers, `consult@1` the only new pin (`vlt-lint` `depends_on`), and the `spec_candidate` check
    explicitly excludes `consult:` blocks from the relay count (*"a `consult:` block grounding in the
    same path … must never increment this count"*). (10) the release itself — installed `module.yaml`
    reports `0.8.0`, `.claude-plugin/marketplace.json:16` agrees, tag `v0.8.0` on `main` @ `557347f`,
    release commit carrying `package-lint: A/B/C/E PASS, D PASS — vlt 0.8.0 (… exit 0)`.
    **STILL-OPEN:** (2) a real consult end to end, (3) the already-checked `consult:` block —
    `_agent/dispatch.md` currently holds **zero** consult blocks, (4) a non-`answer` return
    (*non-blocking*), (5) the `thread.md` bound — all four wait on the **first consult**.
    **Trigger:** the owner's next sitting in which a partner needs another partner's domain
    mid-turn. (6, run half) + (7, run half) wait on the first full lint. (9) **non-blocking** —
    vlt-sayari still on 0.6.0.
  - *Split, re-annotated 2026-07-27 (discharge run 2) — the channel had its first live exercise and
    it earned its cost on day one.* **Newly DISCHARGED:** (2) **a real consult ran end to end and
    the caller kept the wheel** — two consults (librarian → chef, `_agent/dispatch.md` 19:21), the
    sitting yielded **one** session note (the caller's, `2026-07-26-180500-lint.md`), the Chef wrote
    none, and the raw answer appears attributed in its own block (`_agent/partners/chef/thread.md:29`,
    quoted verbatim in the caller's note before the caller uses it). Neither failure signature fired —
    no second session note, no answer arriving pre-digested into the Librarian's voice. The
    mechanism's value is measurable rather than asserted: the consult surfaced that the nutrition
    spec's macro centers sum to **2,265 kcal against a stated ~2,150**, an error that shipped in v1,
    **survived a v2 revision, and was absorbed silently for six weeks** — a fact present in no
    document, derivable only by a partner who cooks to the spec adding up its own rows. That is the
    clearest possible answer to whether the channel beats read-and-cite. (3) **the record shows
    consult traffic and the board does not** — both `consult:` blocks are written **checked
    (`- [x]`)**, neither appears as an open ledger item, and both `{log}` lines are tagged with the
    **caller** (`dispatch (librarian)`) while naming the Chef in the summary. The failure signature —
    a consult sitting open in a partner's slice forever — did not fire. (6) **the check is live and
    exercised by construction** — `consult_missing:` named both `{specs}` artifacts binding a partner
    other than their owner, and those findings are what *caused* the two consults; `authority_scan:
    "2 specs compared; 2 bind a partner other than th[eir owner]"` renders the denominator. A
    convention that shipped `checked` on day one was enforced by its own check within the day.
    (7) **the report is honest about what it cannot see** — `authority_scan:` names the blind spot
    beside the count (*"out-of-authority claim made anywhere other than {specs} has no authority axis
    to derive from and is invisible here"*), no bare zero on either slot; A3-22 discharged as the
    fifth conformer to A4-2's general rule, as briefed. (4) **non-blocking, and inspected rather than
    assumed** — both consults returned `answer`, which the clause flags as the confabulated-authority
    signature when it is the *only* outcome. It was inspected: both answers carry independently
    verifiable content (the arithmetic was re-checked before routing; the format verdict came with
    three specific asks and a named cost), and both produced `relay` traffic to the owning partners
    rather than the consulted partner doing the work. A non-`answer` return is still unexercised.
    **(5) — PENDING OWNER RULING.** The bound reads: the consulted partner's `thread.md` gains an
    entry **only** where the consult changed its stance, with *"one `thread.md` line per consult"*
    named as the failure signature. Two consults produced **two** Chef entries. The first
    (`chef/thread.md:29`) is unambiguously legitimate — it records findings the Chef states he *"had
    not previously named."* The second (`:39`) is headed **"my position, now stated"** and records a
    view he had held since Week 2 — an entry that *states* rather than *changes* a stance, and 2
    consults → 2 entries is the failure signature's exact arithmetic. Reading it either way is
    defensible and the call is the owner's, not the auditor's: an unstated position becoming stated
    may be a genuine change in what the thread knows, or it may be precisely the rot the bound exists
    to prevent. (9) **non-blocking** — vlt-sayari still on 0.6.0.
  - **DISCHARGED 2026-07-29 (discharge run 3) — (5) owner-ruled legitimate:** an unstated position
    becoming stated is a genuine change in what the thread knows; the bound holds. (9) discharged —
    sayari (now on 0.8.0) has the installed surface confirmed: four modes
    (`vlt-dispatch/SKILL.md:14-18`; help CSV `DP` row naming `daily | relay | consult | ledger`) and
    both report slots (`vlt-lint/SKILL.md:191-192`, `authority_scan:` + `consult_missing:`). Every
    blocking clause discharged. Standing watch, not a gate: a non-`answer` consult return is still
    unexercised — when consults only ever return `answer`, inspect, don't assume (per clause 4).

## Open items not owned by any build

- **The brief-time drift class (unfiled as of 2026-07-25).** The `linkage_ripe` inversion entered
  at `build-20-graduation-queue.md:211-216`: a brief restated a field calibration with its
  polarity flipped, a leg substituted, and a borrowed name, and `vlt-lint:83`'s parenthetical
  shows the resulting tension was noticed at build time and resolved in prose **in the wrong
  direction**. No current check compares a brief's restatement against the filing it cites —
  briefs are verified against their own claims. **Recommended: file to `inbox/` so it enters the
  loop as a filing rather than living only inside a spike record.** *(Owner to decide.)*
- **Arc naming.** The title above is the clerk's proposal (see `arc_title_status:`).

## Status & next step

> **⛔ This arc is archived — do not append.** Closed 2026-07-29 by `arc-closeout`. The
> authoritative final state is the frontmatter `status:` and the **Carried forward past Arc 4**
> section at the end of this document; the next `inbox-capture` re-lists from there.

Stood up 2026-07-25 with ideation complete, both spikes closed, and ship order set.

**A4-1 BRIEFED 2026-07-25** — `skills/reports/build-A4-1-linkage-polarity.md`; its acceptance
checks are in the ledger above. Grounding at brief time found **0 corrections** (every A3-23
capture site still holds) and 4 additions (`vlt-lint:43`, `:141`, `frontmatter.md:138`, and the
operating contract's `## Sessions, sittings, and hand-offs` as the home for the two A3-22 prose
items). Brief-time calls recorded there: derive-vs-store → **DERIVE** (closes the deferred
cross-filing ruling without an exception); the derive-first boundary clause is **stated in
`vlt-lint`**, with its governance home deferred to A4-2 alongside the honest-reporting rule
(owner-ruled); `linkage_ripe` **keeps its key**, the prose carries the polarity correction
(owner-ruled); prose `## Sources` entries join the citation leg; the `topic:`-overlap leg is
dropped. The 41-hit baseline precondition is **discharged** by the SPIKE-2 artifact.

**A4-2 BRIEFED 2026-07-25** — `skills/reports/build-A4-2-adoption-unit.md`; its acceptance checks
are in the ledger above. Grounding at brief time found **1 correction** and 4 additions
(`vlt-lint:43`, `vlt-lint:151-152`, the operating contract's lack of any reporting section, and
`spec.md:13` / `wiki-consolidation.md:13` as the facet's two instance sites).

> **Superseding note (grounding correction, 2026-07-25).** The A3-19 capture cites
> `vlt-lint/SKILL.md:84` as the `revisit_due` report line. **A4-1 moved it to `:94`** — the build
> inserted the derive-first boundary clause and rewrote the `linkage_ripe` bullet above it,
> shifting everything below by ten lines. The bullet's **text is byte-unchanged** (A4-1's own
> verification 8 confirmed it as A4-2's site): this is a line shift, not a scope change. Note
> `:84` now points at the **boundary clause**, so the capture's number resolves to a different
> obligation — cite `:94` for `revisit_due`, `:84` for the clause. The capture entry stands as
> written; this note supersedes its line number.

Brief-time calls recorded in the A4-2 brief: the general honest-reporting rule's home →
**`vault-operating-contract.md`**, a new `## Honest reporting — what a check may claim` section
(closes the silent-zero ruling's deferred governance question; a new `{conventions}/reporting.md`
was rejected as a fifth declared-and-unexercised surface, `frontmatter.md` as schema-only and
handshake-expensive); the derive-first boundary clause → **RELOCATED** into that section with
`vlt-lint:84` reduced to a pointer, discharging A4-1's handoff obligation 1 without a second
home; the `adoption_first_instance:` consumer → **outside lint** (`vlt-upgrade` post-flight
report + upgrade ledger consumes, `vlt-mint`'s ceremony stamps, `spec.md` +
`wiki-consolidation.md` carry explicit `null` instances), so **`frontmatter.md:242` is honored,
not revisited**; the two-outcome question → **a required ask in both write beats** with absence
keeping its `:138` meaning (the `revisit_after: none` variant was rejected — it buys countability
at the price of a rule change plus a five-consumer re-ack, and the F4 denominator gets the same
visibility free). **No convention `version:` moves in A4-2** — F5 is a prose clarification, F6
stamps an optional self-describing facet; no consumer walk. A4-1's second handoff obligation (the
`sources_vs_prose_mismatches` filing) is dispositioned: its honesty half closes under the general
rule, its missing-check half stays with capture.

**A4-2 BUILT 2026-07-25** — F1–F8 landed across nine shipped files; verification 1–6 + 8–11 pass
(package-lint A/B/C/E PASS, no `version:`/`consumers:` line moved, both rules single-homed), check 7
PARTIAL on the `vlt-lint` fence for a **pre-existing** strict-YAML break at
`sources_vs_prose_mismatches:` (byte-unchanged here; the slot disposition 5 leaves to capture). Both
A4-1 handoff obligations discharged: the derive-first boundary clause **relocated** into the
contract's new *Honest reporting* section with `vlt-lint:84` reduced to a pointer, and the
`sources_vs_prose_mismatches` filing dispositioned (honesty half closed by the rule, missing-check
half stays with capture). Deliberate asymmetry recorded: the five `checked`-stage conventions are
**not** stamped — no witnessed first instance exists to cite, and the report's third value covers
them honestly. Unreleased (version held to arc end).

**A4-3 BRIEFED + BUILT 2026-07-26** — `skills/reports/build-A4-3-contradiction-drain.md`; its
acceptance checks are in the ledger above. Grounding at brief time found **1 correction** (one shared
cause, five sites) and **4 additions**.

All eight F-sites landed; full build record + verification in the brief's `status:`. `wiki-supersession`
`1 → 2` with all four consumers re-acked in-build (`vlt-track` ack-only — reconciliation found nothing
to change, a verified conformance). `contradictions_handled:` **retired**, replaced by the derived
three-value split (`open` / `deferred` / `undispositioned`) across **both** producers — `vlt-lint`
Step 5 and the `vlt-lint-full.js` reduce. The arc's third silent-zero instance closed **by conformance**
to A4-2's general honest-reporting rule (`contradiction_scan:` denominator + declined count), no bespoke
wording. Three deliberate deviations, all recorded in the brief `status:` — two tightenings toward the
brief's own verification checks (schema descriptions describe the read, not the vocabulary; the SKILL
states it composes `contradiction_scan:`), one observation left unchanged (F1's reading-list line makes
`vault-operating-contract.md` appear twice). No backfill, no migration, no new `kind`, no schema key.
Package-lint A/B/C/E PASS (D skipped — not the release build). Unreleased (version held to arc end).

> **Superseding note (grounding correction, 2026-07-26).** The A3-20 capture cites `vlt-lint/SKILL.md`
> `:101` (do-not-auto-apply), `:105` (Step 4 catch-all), `:108` (item template), `:111` (routing
> sentence), `:150` (`contradictions_handled`) and `:175` (the Tips line). **A4-1 and A4-2 shifted all
> six by +10** — they are now `:111`, `:115`, `:118`, `:121`, `:161` and `:186`, with **text
> byte-unchanged**. This is a line shift, not a scope change, but the old numbers now resolve to
> different obligations (`:101` is Step 3's opening, `:105` is *Broken wikilinks*), so cite the new
> ones. **`:69` (the tier-2 Contradictions check) is unmoved** and holds exactly as captured. The
> capture entry stands as written; this note supersedes its line numbers.

Grounding additions recorded in the A4-3 brief: (1) **`skills/vlt-setup/assets/workflows/vlt-lint-full.js`
produces the contradiction report slots** (`:105-114` schema, `:230-232` prompt, `:270-272` reduce) —
the capture named only the SKILL, so a report-key change lands in two files or a full-mode sweep
silently emits a retired key (no extra ack — `vlt-lint:74` says a consumer's ack covers its workflow
assets); (2) **no shipped file specifies how a contradiction is documented at all** —
`wiki-supersession.md` carries contradiction only as the `contradicted` *reason value* on the
supersession callout (`:40`), so the capture's "write-side only" reading holds but there is less
there than "covers conflicting claims" suggests; (3) `vlt-ingest/SKILL.md:134` names the
`**Contradictions / Open Questions**` page section and `:136` writes contradictions — a consumer to
reconcile, not just re-ack; (4) `vlt-extract/SKILL.md:47` reads "a Contradictions section" — the
third skill referencing a shape that exists nowhere.

Brief-time calls recorded there: ODQ #5 → **shapes 1 + 2 + 3, with 3 as the mechanism** (the callout
carries a recorded `Disposition: open | adjudicable`; the report split and the backlog drain are its
consequences); the split's truth lives **on the page, derived, never counted** (derive-first unbent,
and the boundary clause applied — today's report infers *managed* from the residue of documenting);
ODQ #6 → `vlt-lint:69` is **bounded as a stated outcome, not a numeric top-N** (a top-N needs a
severity ordering, and the only one in evidence is the four-bucket triage the ruling forbids adopting
as a taxonomy); `contradictions_handled:` is **retired**, replaced by a three-valued split whose third
value is `undispositioned` (A4-2's `convention_adoption:` precedent); **no backfill** of existing
callouts; **no new backlog `kind`** (`maintenance` | `knowledge-gap` already map onto the filing's own
routing split); and the "contradictions are features" tip is **kept and qualified**, per the filing's
explicit request.

**The build carries one convention rule change, named up front:** the contradiction callout must be
specified somewhere for the first time, so it is written once into `{conventions}/wiki-supersession.md`
— **`version: 1 → 2` with all four consumers re-acking in the same build** (`vlt-ingest`, `vlt-lint`,
`vlt-extract`, `vlt-track`). Stating it in `vlt-lint` alone was rejected: `vlt-ingest` writes
contradictions too, so lint-local mechanics would be restated at the write site within one build.

**A4-4 BRIEFED 2026-07-26** — `skills/reports/build-A4-4-source-fidelity.md`; its acceptance checks
are in the ledger above. Grounding at brief time found **1 correction** (one shift class, three line
numbers) and **4 additions**.

> **Superseding note (grounding correction, 2026-07-26).** The A3-21 capture cites
> `vlt-ingest/SKILL.md` `:114` (`trust: raw`, wiki-page frontmatter), `:99` (Step 6's near-duplicate
> check) and `:153` (Step 9's attestation). **A4-2 shifted all three by +3** — it inserted
> `revisit_after:` into the research-note template (`:90`) and the two-outcome paragraph (`:94`),
> both above these sites — so they are now **`:117`, `:102` and `:156`**, with **text
> byte-unchanged**. A line shift, not a scope change, but the old numbers resolve to different lines
> now; cite the new ones. **`:48-63` (the heavy-source prep/interpret split) and `:83` (`trust:
> raw`, research-note frontmatter) are unmoved** and hold exactly as captured. The capture entry
> stands as written; this note supersedes its line numbers.

Grounding additions recorded in the A4-4 brief: (1) **`vlt-lint-full.js` is the second producer of
the lint report** — the capture named only the SKILL, and A4-3 learned one build ago that a
report-key change landing in one producer means a full-mode sweep silently omits the key; the
bounded cross-page cluster pass (`:106-116` schema, `:228-239` agent, `:272-276` reduce) is also the
right host for the catch half, since it already reads the pages and is already capped
(`clusterCap`, `:53`); (2) the operating contract's `## Honest reporting` (`:250-256`) **postdates
the capture** (A4-2, 2026-07-25) and is both the rule the new report slot conforms to and the
structural sibling the new section sits beside; (3) **`vlt-ingest/SKILL.md:136` now specifies the
write-side contradiction path** (A4-3 rewrote it to require the disposition callout) — a hazard the
capture could not have seen, since ingest can now document a name collision as a contradiction, the
wrong remedy applied with fresh machinery; (4) `vault-operating-contract.md:238` carries the backlog
kind vocabulary, the routing target that makes a new `kind` unnecessary.

Brief-time calls recorded there: ODQ #7 → **all four shapes ship**, with shape 2 (codify) as the
load-bearing one the other three point at; the **affordability sub-question ruled** — an entity pass
over the *source* is not affordable and is not needed, a collision check over the entities about to
be *canonicalized* is nearly free (small cardinality, comparison target already read at Step 6
`:100`/`:102`, and at heavy scale the prep sub-agent already reads the body so a located
proper-noun inventory is a by-product, not a second pass); the rule's home →
**`vault-operating-contract.md`, a new `## Grounding sufficiency — what a claim may rest on`
section** sibling to *Honest reporting* (a new `{conventions}/source-fidelity.md` rejected as a
fifth declared-and-unexercised surface per A4-2's precedent; `wiki-supersession.md` rejected
**substantively** — the rule governs new claims as much as amendments, and the observed case was a
brand-new page with no record to supersede — as well as on a `2 → 3` bump with a second
four-consumer re-ack); the rule is **scoped to machine-transcribed sources**, not all `trust: raw`
material, per the arc's standing ruling against pre-generalizing from thin evidence; the catch half
gets **its own report slot with a stated precedence rule** (one finding, one slot — not an overload
of A4-3's contradiction slots, whose remedy differs); **no new backlog `kind`** — the mis-filed
item's defect is its `why` line, not its kind (a roster lookup *would* close it, so `knowledge-gap`
was correct); and prevention **declines the name and keeps the claim** rather than blocking the
write or guessing a correction. **No convention `version:` moves in A4-4** — the contract is
deliberately not handshaked, and `vlt-lint:74` covers the workflow asset under the existing ack. The
evidence debt is binding on the writing: no F-site and no acceptance check asserts which of
Jonah/Alaric is correct.

**A4-4 BUILT 2026-07-26** (`fb04902`) — see its section above for the build record.

**A4-5 BRIEFED 2026-07-26** — `skills/reports/build-A4-5-consult-channel.md`; its acceptance checks
are in the ledger above. Grounding at brief time found **0 corrections** — `vlt-dispatch/SKILL.md`,
`vlt-review-council/SKILL.md` and `module-help.csv` are all byte-unchanged since build-15
(`3795d86`), so every A3-22 capture citation (`vlt-dispatch:11`, `:13-15`, `:17`, `:21`, `:225`,
`:4`, `:56`, `:120`, `module-help.csv:11`, and the corrected council lines `:10`/`:35`/`:41`) holds
exactly. **6 additions:** (1) `vlt-setup/SKILL.md:144` **enumerates the seven shipped convention
files by name** — a new `consult.md` must be hand-registered there or it ships in the repo and never
reaches a vault (a completeness-list-drifts hit); (2) `vlt-setup/SKILL.md:155-156` likewise
enumerates the two shipped workflows in prose, so the new engine asset registers there too; (3)
`vlt-dispatch:73`'s `daily` watermark reader ("relay blocks carry no watermark and are ignored
here") must learn to ignore consult blocks — the B1-critical guard; (4) `vlt-lint:86`'s
`spec_candidate` check counts relay entries in the dispatch record and would otherwise miscount a
consult block pointing at the same path; (5) the arity surface is **six** sites, not four —
`vlt-dispatch:11` and `:17` say *three modes* alongside the four ideation named; (6) A4-1's
contract prose at `:226`/`:228` already names the consult act and its trigger rule, so this build
supplies the mechanism sentence A4-1 deferred by name (`build-A4-1-linkage-polarity.md:415-418`),
not a new rule.

Brief-time calls recorded there: the engine is a **workflow asset** (`vlt-consult.js`), not prose in
the SKILL — the module's own doctrine at `vlt-review-council/SKILL.md:51`, and the only way the typed
return union is *enforced* and depth-1 is *structural*; the payload is **fat and carries the caller's
boundary** (`from`/`to`/`question`/`groundIn` live absolute paths/`why`, the council `subject` idiom);
the convention's precondition is **bounded to `{specs}`** — the only artifact class carrying a
machine-readable authority axis (`owner:`/`consumers:` partner slugs), with the resulting blind spot
stated **in the rule itself** per A4-4's precedent; the consult record is **derived from the dispatch
block, never stored** (no frontmatter key, no counter — derive-first unbent for the fifth build
running, and the boundary clause satisfied because the block is an event, not the residue of one);
**`spec.md` does not bump** — it gains a version-free Reading-list pointer, rejecting a `1 → 2` bump
plus a four-consumer re-ack one build after A4-3 paid that price; **a consult is not a hand-off** —
it crosses no sitting boundary, so the caller keeps the wheel and owns the single session note (one
clause at the contract's sitting home, `:213`); the `{log}` line keeps **one** partner tag, the
caller — the filing's dual-tag proposal **rejected** as a change to the contract's canonical format
that would break its own published grep patterns, with attribution living in the attributed block and
the consult record instead; and the filing's four remaining risk mitigations adopted unchanged
(praised `insufficient-context`, raw attributed answer before use, `thread.md` written only on a
changed stance, read-only-except-own-memory with `needs-work` exiting through `relay`).

**The build carries one new handshaked convention, named up front:** `{conventions}/consult.md` at
`version: 1` with `consumers: [vlt-dispatch, vlt-lint]`, both acking `consult@1` in the same build.
**No existing convention `version:` moves** and nothing re-acks. It ships at
`enforcement_stage: checked` with **no deferral block** — its check lands in the same build, which is
the whole point of ODQ #8's pairing and the arc's answer to the shipped-but-unexercised scar. The
named tension is recorded in the brief: A4-2 and A4-4 each *rejected* a new convention file as a
fifth declared-and-unexercised surface; this one is exempt precisely because it is not declared-only,
and a deferral block appearing in it at build time is the signal the pairing has come apart.

**The B1 precondition is discharged in the brief** (F3, four readings): `_agent/dispatch.md` is
agent-zone and is never written by the install path (`vlt-setup` never touches it), so durability is
by **location** and no merge script changes; an un-upgraded reader degrades to *invisible*, never
*wrong*, because the pre-checked pointer escapes both `ledger` greps and the watermark scan; there is
nothing to backfill; and `vlt-upgrade:74`'s re-point rule concerns **open** pointers only, so
`vlt-upgrade` needs no edit.

**A4-5 is the RELEASE BUILD** — it carries the dual version bump `0.7.0 → 0.8.0`
(`.claude-plugin/marketplace.json` + `module.yaml:4`), the `uv run tools/package-lint.py
--expect-version 0.8.0` gate (tag only on exit 0, PASS line in the commit message), and the
ff-merge → tag `v0.8.0` → push for all five Arc-4 builds, which are built and unreleased.

---

## Capture — 18 filings (grounded against module source 2026-07-29, v0.8.0 @ `9f05579`)

**This is the Arc-5 seed batch.** Owner confirmed scope 2026-07-29: all 18 un-captured filings
(the three Arc-3 closeout findings, four A4-era off-brief filings, two full-lint fallout filings,
the five-filing boot-cost cluster, and the four discharge-run-3 filings). Grounded in five
parallel passes. Capture-run judgment calls, recorded here per the no-separate-decision-log rule:

- **Numbering** — entries take **A4-6..A4-23**, continuing past the A4-1..A4-5 build ids so the
  two series can never collide (the arc's builds reference A3-* capture ids; nothing references
  an A4-6+ id yet). Ordered by filing timestamp.
- **Why this roadmap** — Arc 4 is the open roadmap; this batch lands here exactly as A3-18..23
  landed in Arc 3's, and its ideation belongs to **Arc 5**. Nothing here re-opens Arc 4's builds.
- **Standing line-drift correction applied batch-wide:** three filings cite the honest-reporting
  rule at `vault-operating-contract.md:252`; the section heading is at **`:254`** (rule text
  `:256`) in current source — A4-4/A4-5 added contract text below it. Captures below carry the
  corrected line.
- **One inter-filing dedupe:** A4-14's addendum re-raises the `adoption_first_instance` stamp gap;
  that claim is captured once, at **A4-20**, which owns it.
- **One filing self-citation corrected:** A4-14 declares its companion at an `inbox/archive/`
  path; the companion (`…-142000`, A4-11) is **active**, captured this same run.

**Cross-filing threads** (what makes 18 filings one story — expanded from the through-line):

- **The proxy-check family** (A4-11, A4-12, A4-13, A4-14, A4-8): checks whose stated signal and
  actual signal diverge, with no report slot where the divergence could appear. All five sit
  adjacent to the honest-reporting rule (`vault-operating-contract.md:254`); whether capture
  treats them as one cross-cutting finding or separate bugs is carried below as A4-14's own
  verbatim question — **deliberately not resolved here**.
- **The write-surface pair** (A4-20, A4-23): a key with no reachable writer off the mint road,
  and a report with no persistence home at all. A4-23 is load-bearing for the loop itself — two
  discharge runs verified report-shape clauses only by owner hand-paste.
- **The reporter dependency** (A4-22 → A4-20): the upgrade report's adoption line is the adoption
  axis's only reporter; if it can silently drop, the axis loses its reporter as well as (per
  A4-20) most of its writer.
- **The boot-cost anatomy** (A4-15..A4-19): one cost model, deliberately factored — A4-18 is the
  measurement keystone (its own preference: run the instrument **before** the others are
  briefed), A4-15 the fixed cost, A4-17 the variable cost, A4-16 the repetition operator over
  both, A4-19 the orthogonal per-invocation axis. A cross-cutting **pre-hoc vs post-hoc
  governance** ruling (A4-15's verbatim question) would settle several at once.
- **The factory thread** (A4-6, A4-10, and A4-8's tail question): the loop's own artifacts drift
  the way vault surfaces do. A4-10's "named slot" idea and A4-11's "named next owner" idea are
  the same design at two altitudes — plausibly one ideation ruling.
- **The upgrade-machinery pair** (A4-7, A4-9): disjoint defects, both extending existing
  `vlt-upgrade` beats, both "the module's own voice gives false reassurance."

### A4-6. Brief restatement drift (2026-07-25) — 2026-07-25-171500-brief-restatement-drift.md

**Verdict: shipped half SUPERSEDED (A4-1 fixed it in full); factory half GAP CONFIRMED.**

- The historical defect is real and verbatim: build-20's brief inverted the field calibration's
  polarity, substituted a leg, and relabelled the numbers
  (`skills/reports/archive/build-20-graduation-queue.md:210-216`), while the capture had it right
  (`archive/inbox-evolution-arc3-roadmap.md:654-656`).
- **SUPERSEDED:** the shipped instance is gone — `skills/vlt-lint/SKILL.md:96-101` now carries
  the corrected polarity ("any absorption signal means **already absorbed ⇒ exclude**"), the
  restored prose-`## Sources` leg, the real measurements, and a failure signature (A4-1,
  `4ca619e`, shipped v0.8.0).
- **GAP CONFIRMED (factory):** no loop step re-derives a brief's restatement of a filing against
  the filing. `.claude/skills/build-brief/references/grounding-at-brief-time.md:16-30` re-grounds
  module-source sites only; `brief-anatomy.md:22` cites filings by path, never by `file:line`
  into them; CLAUDE.md step 5's unit-verify checks brief↔shipped agreement — downstream-consistent
  with a misread. None of the filing's four candidate shapes exists.
- Residual scope: entirely factory-side — first a **classification ruling** (module build vs
  factory process record), then, if buildable, the four candidate shapes against `build-brief`.

> **Open design question (verbatim):** The remedy probably lands in **factory** artifacts — the
> `build-brief` skill, `CLAUDE.md`'s lifecycle steps 4–5, possibly the brief template — none of
> which ship to vaults. If so this filing produces **no module build**, like A3-18, and belongs in
> the factory's own process record rather than an arc's build plan. Alternatively the `091002`
> precedent applies (the packaging lint was factory-side and *did* get a build, with `tools/`
> tracked as public documentation of the release contract), in which case it is ordinary arc work.
> **Capture should rule which, before anyone scopes it.** *(Carried to ideation unresolved.)*

### A4-7. Upgrade preserve set misses vault-grown op skills (2026-07-25) — 2026-07-25-183003-upgrade-preserve-set-misses-vault-grown-op-skills.md

**Verdict: GAP CONFIRMED in full; intact at HEAD; every filed site re-derived.**

- `vlt-mint/SKILL.md:168` promises unqualified durability for any local mint; B1 honors it
  provenance-based (`merge-help-csv.py:199-201,219` — no name test); but `vlt-upgrade`'s Step-1
  snapshot is name-scoped to `vlt-agent-*` (`SKILL.md:34`) and **no bullet catches a vault-grown
  `vlt-{op}/` dir** (`:35-40` — overlays, divergence, manifest-scoped assets, mint history,
  agent-zone capabilities, governance). B2 restores only snapshotted partner dirs (`:66`).
  `vlt-mint` mints op skills as a first-class kind into `{module-skills}/vlt-{op}/` (`:131,170`)
  — the two skills disagree about what a vault can grow.
- Ledger/report fields read partner-only: `:97-98`, `:124`.
- **Grounding addition beyond the filing:** the Step-2 own-the-apply prohibition is *also*
  name-scoped — `vlt-upgrade/SKILL.md:48` "never delete an unshipped `vlt-agent-*` dir" — a third
  site the widening must touch.
- Residual scope: all of it. Sites: `vlt-upgrade/SKILL.md:34` (widen to provenance test), `:48`,
  `:66`, `:97-98`/`:124`, and `vlt-mint/SKILL.md:168` (true only once the widening ships).
  Durability-posture standing rule applies (re-check B1 preserve path in the same build).

> **Open design question (verbatim):** **Second, smaller:** the ledger schema field
> `mints_preserved:` and the report line "Mints preserved" both read partner-only. If the widened
> set should be visible in the ledger, either broaden that field's description or add a sibling —
> maintainer's call, and I'd default to broadening rather than adding a field.

### A4-8. Report slot with no check (2026-07-25) — 2026-07-25-193000-report-slot-with-no-check.md

**Verdict: GAP CONFIRMED, still true at HEAD.** (This filing shaped three Arc-4 builds without
ever entering a `derives_from:` — the un-referenced state Arc 3's closeout named.)

- `sources_vs_prose_mismatches` is a declared `fix_now` report key at `vlt-lint/SKILL.md:162`
  (post-A4 numbering) that **no check in Step 2 (`:51-105`) ever fills** — the full check
  inventory was walked; nothing compares a wiki page's frontmatter `sources:` against its prose
  `## Sources`. A4-4 did not touch it (its entity work is a different axis).
- A4-1 made the dual-surface read mandatory for the *candidacy* leg (`:97`, `:43`) — so
  disposition (b)'s "the read is no longer additional cost" argument holds — but that read fills
  `linkage_ripe`, never this slot. A4-2's honest-reporting rule shipped (`contract:254`) and the
  slot still isn't marked unimplemented: the current state is the filing's feared **"(c) plus
  silence"** — the key renders as checked-and-clean.
- Note: this slot is also the known pre-existing strict-YAML fence break A4-2/A4-5 recorded in
  their PARTIAL checks — the slot's disposition settles that too.
- Residual scope: the (a)/(b)/(c) ruling; if (b), tier membership is
  `{conventions}/write-verification.md`'s call.

> **Open design questions (verbatim):** **(a) Delete the slot.** Cheapest and honest: a declared
> finding with no producer is a promise the SKILL does not keep. Cost: loses the intent record.
> **(b) Define the check.** A tier-1 (one-file-checkable) wiki-page check: frontmatter `sources:`
> vs prose `## Sources`, flag divergence. Note A4-1 already made the wiki-side prose-`## Sources`
> read mandatory for the candidacy pass, so the read is no longer additional cost in full mode.
> Membership test lives in `{conventions}/write-verification.md` — tier-1 vs tier-2 is that
> file's call, not this filing's. **(c) Keep + mark.** Leave the slot, let A4-2's general rule
> mark it unimplemented. Weakest — the slot keeps claiming a check that does not exist.
> Whether that is a pattern worth a check of its own — a lint on the module's own report
> contract, i.e. every declared report key traces to a check that fills it — is a
> **factory-tooling** question (`tools/package-lint.py` territory, plausibly a Group E
> extension), not module source.

### A4-9. Lint has no memory of adjudicated divergence (2026-07-26) — 2026-07-26-124223-lint-has-no-memory-of-adjudicated-divergence.md

**Verdict: GAP CONFIRMED in full; no A4 build touched the seam; every line cite holds (minor
contract drift: relay-when-done now `:236`, honest-reporting `:254`).**

- `vlt-lint` neither reads nor writes the decision log (grep-zero at HEAD; nearest reference is
  `:176`'s "never writes the stamp"). The other two governance-touching ops are wired in:
  `vlt-mint/SKILL.md:68-84` owns the entry schema, `vlt-upgrade/SKILL.md:85` write-through +
  `:77` reconcile. The long-lived governance findings (`convention_base_divergence` et al.,
  `vlt-lint:81-84`, "Never auto-fix — a human decides overlay-vs-upstream" verbatim) re-flag
  adjudicated states forever; the entry schema has no machine key (`ref:`) to make rulings
  addressable (`vlt-mint:75-79`).
- Residual scope: all of it, as filed — `vlt-mint:72-80` (add `ref:`), `vlt-lint:81-84`
  (read-before-flag, three-state reporting per `contract:254`), a lint write-through clause, the
  `vlt-upgrade:77` reconcile extension, plus the §6 homing decision, which sets build size and
  intersects the `vlt-mint:84` three-homes supersession debt (Q21, re-listed below).

> **Open design question (verbatim):** The decision-log entry schema is single-homed in
> **`vlt-mint`'s SKILL.md — a skill, not a convention** — so it carries **no handshake axis**.
> Adding `vlt-lint` as a consumer makes it a contract between three ops.
> **(a) Leave it in `vlt-mint`; lint points at it.** Cheap, no handshake, matches the
> relay-when-done precedent (named at every site, mechanics in one home). Risk: three consumers
> depending on an unversioned format. **(b) Promote to `{conventions}/decision-log.md`** with
> `version:`/`consumers:`, re-acking consumers per build-4. Correct by handshake doctrine,
> **and** it gives a home to the carry-forward debt already tracked at `vlt-mint:84`.
> **Owner's stated instinct (2026-07-26): (b), promote from the start** — noting that
> discharging the `vlt-mint:84` debt makes (b) cheaper than it first appears. **Not yet a
> ruling**; deliberately left open for arc ideation. This choice determines the build's size.

### A4-10. Group E did not retire the handwritten handshake grep (2026-07-26) — 2026-07-26-141500-group-e-did-not-retire-the-handwritten-handshake-grep.md

**Verdict: items 1–2 FIXED as the filing's own banner claims (do not re-brief); item 3 GAP
CONFIRMED. Wholly factory-side (`.claude/skills/build-brief/`); no shipped surface.**

- Group E works as designed (`tools/package-lint.py:351-382` — derives conventions from the
  governance glob and acks from every `depends_on:`); A4-3 and A4-5 nonetheless wrote handwritten
  greps as checks of record with Group E demoted to "the net" (`build-A4-3…md:469,494`;
  `build-A4-5…md:615,618`) — the inversion is exactly as filed.
- The fix that landed: `.claude/skills/build-brief/references/brief-anatomy.md:95-107` now names
  Group E the check of record, says "do not compose your own," and cites this filing; `:108`
  corrects the mid-arc run to A/B/C/E.
- **Item 3 sharpened at grounding:** §7 (`brief-anatomy.md:89-112`) remains prose obligations,
  not named slots — but of the "other standing rituals" the open question names, only **Scrub**
  (`:111-112`) is actually a §7 ritual today; workflow parse-on-intake and fence well-formedness
  live in CLAUDE.md standing rules and individual briefs. The question's premise needs that
  narrowing at ideation.

> **Open design question (verbatim):** Should the verification template carry a **named slot**
> for the handshake check rather than leaving builders to compose one? The drift here was a
> builder filling an *unnamed obligation* with the cheapest available tool, and items 1–2 fix
> the naming without addressing the shape. Related open question: whether the same
> unnamed-obligation risk exists for the other standing rituals in §7 (scrub, workflow
> parse-on-intake, fence well-formedness), none of which names a tool either.

### A4-11. Spec convention surfaces candidates nobody accepts (2026-07-26) — 2026-07-26-142000-spec-convention-surfaces-candidates-nobody-accepts.md

**Verdict: GAP CONFIRMED — and the dead end is by explicit design, not omission. One line
correction (retrofit is `vlt-upgrade/SKILL.md:79`, not `:75`); one sharpening that partially
answers direction 2.**

- Advocacy exists at both cadences (`vlt-upgrade:79` retrofit; `vlt-lint:86` `spec_candidate`),
  but a candidate's terminal state is the backlog: `vlt-lint:86` mandates "**Never
  auto-promote**… routing back to the owning partner is not lint's job," and no surface names a
  next owner or promotion step. The nearest machinery (`vlt-mint:176`) only stamps on **mint**
  ceremonies, and no ceremony authors a spec — the deadlock as filed (lock needs a spec;
  authoring has no ceremony) holds.
- `spec.md:14-15`'s `deferral_metric` ("spec version bumps shipping without their relay entries",
  threshold 1) is unreachable at zero adoption — a metric whose only attainable value is "fine",
  nonconforming to `contract:256`. **Repair is a convention rule change**: `spec.md` `version: 1`
  (`:11`), `consumers: [vlt-mint, vlt-dispatch, vlt-upgrade, vlt-lint]` (`:12`) — bump +
  four-consumer re-ack, Group E the check of record (per A4-10).
- Sharpening: `adoption_first_instance: null` (`spec.md:17`) **is** surfaced at upgrade cadence —
  `vlt-upgrade:105` report + `:131` ledger. What nothing reads is its **age**. The gap is
  longevity-as-signal, not visibility. (Reachability of the stamp itself is A4-20's.)
- `spec.md:13` is one of only two conventions still `declared` (with `wiki-consolidation.md:13`);
  `spec.md:81` records the two deferred lint checks and pre-agreed escalation.

> **Open design questions (verbatim — "Candidate directions, not a design"):** **1. An
> acceptance beat.** A `spec_candidate` in the backlog should have a named next owner and a
> promotion step, the way A4-3 gave adjudicable contradictions a route to Step 4 and a `Filed:`
> back-write that ends in the finding being gone. Today the candidate's terminal state is "still
> in the backlog." **2. `adoption_first_instance:` on `spec.md`.** A4-2 wired the facet end to
> end and `spec.md` carries it as an explicit `null`. That null is now 18 days old and nothing
> reads it as a signal — worth checking whether the standing ledger surfaces a long-lived null,
> which is exactly the adoption axis build-20's facet was created for. **3. Repair the
> `deferral_metric`.** A metric whose only attainable value at zero adoption is "fine" is the
> exact class A4-2's honest-reporting rule now governs. `spec.md` predates that rule and does
> not conform to it.

### A4-12. Boundary classifier: five verdicts and an unmeasurable metric (2026-07-26) — 2026-07-26-142500-boundary-classifier-five-verdicts-and-an-unmeasurable-metric.md

**Verdict: shape 1 SUPERSEDED (the ship-verifiable/field-contingent tagging landed at `9f05579`,
post-filing); shapes 2–3 GAP CONFIRMED. Verdict evidence is vault-local, correctly labeled.**

- Gate live and reachable on every kind: `vlt-mint/SKILL.md:42` (classifier + `non-boundary:`
  exemption), `:59` (gated kinds), `:94` (kind → council map), replicated in all three mint
  templates. The counter-incentive is real at source: `vlt-mint:150` — a true rule change has no
  overlay form and "should be **filed upstream**," structurally cheaper than a boundary mint for
  an owner-owned vault.
- **Shape 1 superseded:** `9f05579` shipped the general fix (`build-brief` tags every acceptance
  check `[ship-verifiable]`/`[field-contingent]` with a named event-vault;
  `arc-closeout` gates on ship-verifiable only). Nothing remains to split.
- **Shape 3 (report the never-rung streak) GAP CONFIRMED with a scoping nuance:** no surface
  aggregates classifier verdicts (decision log records per-mint lines; nothing counts them) —
  but `contract:256` governs *count surfaces*, and the classifier is a per-event gate; extending
  the rule to event-gates is a **design ruling, not a present nonconformance**.
- **Shape 2 (discriminating probe) GAP CONFIRMED as absence** — no fixture or known-boundary
  probe exists; primarily a field/owner action.
- The `review_after: 2026-08-17` dated clock is live at `spec.md:16` (the Arc-3 dated watch,
  re-listed below).

> **Open design questions (verbatim, shapes 2–3; shape 1 omitted as superseded):** **2. A
> discriminating probe.** The cheapest way to distinguish correct-decline from biased-to-silence
> is a `convention edit` mint against a rule the vault genuinely wants, or a deliberate fixture
> case with a known-boundary subject. Neither exists today. **3. Consider reporting the streak.**
> Five consecutive `non-boundary` verdicts is a signal no surface currently surfaces. Under
> A4-2's honest-reporting rule a bell that has never rung arguably owes the reader that fact.

### A4-13. `vlt-lint-full` asks LLM scanners for exact mechanical facts (2026-07-26) — 2026-07-26-184704-lint-full-asks-llms-for-exact-facts.md

**Verdict: the seam CONFIRMED; both defect instances GAP CONFIRMED; the near-duplicate item is a
separable third defect; plus one gap the filing measured but didn't name.** (Provenance note: the
filing cites the vault-local workflow copy; module source
`skills/vlt-setup/assets/workflows/vlt-lint-full.js` is line-identical at every cited site.)

- **The seam:** scanners are asked for exactly-computable facts (`vlt-lint-full.js:78` links
  "normalized to slugs", `:83` char-counted summaries, prompt `:122-124`), and the reduce
  compares them exactly (`:145-155`).
- **Instance 1 (links):** `crossLayerSlugs` are basenames (`vlt-lint/SKILL.md:41`); the reduce
  does raw set-membership with no stripping of path prefix/`.md`/`#anchor`/`|alias`
  (`:153-155`); no normalization exists anywhere. Build-3 shipped only the exclusion set
  (archive `build-3-lint-full-hardening.md:18,42-43`) — symptom, not cause. Prior rate 82%
  re-derives from the archived 2026-06-06 filing (§5 tail, `:139-140`).
- **Instance 2 (summary length):** the deterministic remedy was recommended in the archived
  filing's §5 and deliberately left unshipped. **Load-bearing constraint for any re-cut:** the
  workflow has **no filesystem access** (`archive/build-3…md:20`) — deterministic checks must be
  fed by, or run in, the SKILL. `category_no_match` is the same class (`:81`, `:102`,
  `:199-200`).
- The whole file-local check list is LLM-asserted (PAGE_SCAN `:64-93`); partial exception:
  `review_due`'s *comparison* is deterministic (`:270-271`), the date still scanner-transcribed.
- **Separable third defect (capture separates it, as the filing asks):** near-duplicates 4/4
  false — `:168`'s two-segment stem means every `nfl-2026-*` page shares a stem, auto-firing the
  `sameStem` signal (`:187-191`). Build-3 C2 heuristic defect, not the LLM seam.
- **Unnamed fourth gap (grounding addition):** the surviving-10 `missing_targets` were all
  index-registered stubs — the reduce has no stub set to exclude against (`wiki-index.md:83-90`
  defines `## Stubs` with backtick identifiers), so a `[[link]]` to a registered stub always
  fires. Whether the SKILL passes stub slugs as a third exclusion channel is unowned.
- Report shape can't distinguish complete from accurate coverage (`:249-251`, `:290` — coverage
  axes only); adjacent to `contract:254`.

No open design questions posed — both "Suggested shape" blocks are marked "(owner steers)" and
the candidate direction is "explicitly **not a design**"; carried as such to Arc-5 ideation.

### A4-14. `spec_candidate`'s revision signal is template boilerplate (+ `consult_missing` addendum) (2026-07-26) — 2026-07-26-184705-spec-candidate-revision-signal-is-template-boilerplate.md

**Verdict: heading-leg defect GAP CONFIRMED with a sharper root than filed; the honest-limit item
the filing left unchecked is CONFIRMED (defect lives in two places); addendum GAP CONFIRMED
(day-one gap in a one-day-old check, not a regression).**

- The rule as shipped (`vlt-lint/SKILL.md:86`): "revised in place (carries a 'What changed'
  section) **or** ≥2 `relay:` entries" — the heading is the only operationalization of revision.
  **Sharper root:** the module itself teaches the heading — `spec.md:63` makes "What changed"
  the *required* revision mechanism and `:81` names its absence a schema violation — so the
  check scores the module's own template vocabulary as history. Zero-revision false positives
  are structural.
- **Two sites, one defect:** the proto-spec retrofit uses the same signal
  (`vlt-upgrade/SKILL.md:79`), and `vlt-lint:86` cross-cites it as "the same signals" — any fix
  lands in both.
- The relay leg is sound and correctly guarded (`:86` — consult blocks never increment).
- **Addendum:** `consult.md:41` states a temporal precondition ("requires a consult record…
  **before** it is filed"); `consult.md:57` + `vlt-lint:87` check pair-presence only; no date
  comparison or `consult_retroactive` state exists. The derivation is sound on current schemas
  (dated consult header `vlt-dispatch:271`; spec `created` at `spec.md:50`). Context: the check
  shipped checked-on-day-one in A4-5 — the filing's lint run was likely its first exercise.
- The `adoption_first_instance` secondary is **deduped to A4-20**. Git-availability caveat on
  direction 2 is correct — nothing in the governance bundle requires git (though the retrofit
  already assumes `git mv`, `vlt-upgrade:74,79`).

> **Open design questions (verbatim):** "Whether capture treats that as one cross-cutting
> finding about **proxy checks that cannot state what they actually measure** — adjacent to the
> honest-reporting rule — or as two unrelated bugs, is the owner's call; I'm flagging the
> resemblance, not asserting a shared root cause in the code." · "If capture prefers amendments
> as separate filings, say so and I'll split it." *(Capture accepted the amendment in place; the
> procedural ruling on amended filings generally is left to the owner.)* · (Direction 2 caveat:)
> "it assumes the vault is git-managed, which the conventions do not currently require — worth
> checking before making it load-bearing."

### A4-15. Activation contract read is the boot whale (2026-07-29) — 2026-07-29-082930-activation-contract-read-is-the-boot-whale.md

**Verdict: CONFIRMED throughout; token estimate band adjusted; one two-home coherence constraint
added at grounding.**

- All three partners open every activation with a full contract read — identical opener at
  `vlt-agent-researcher/SKILL.md:22`, `vlt-agent-librarian/SKILL.md:22`,
  `vlt-agent-creative/SKILL.md:22`; the contract concurs (`contract:16` — "reinforcement, not
  the sole guarantee").
- Measured: contract **38,271 chars / 5,636 words** — ~9.6K tokens by chars/4, ~7.3K by
  words×1.3; a fairer band is **~7.5–9.5K**, whale claim stands. Partner SKILLs 10,069–11,497
  chars — the contract adds **~3.3–3.8×** the SKILL's own weight before Beat 2.
- Conventions are already lazy (point-of-use: researcher `:56`, librarian `:53`, creative `:54`;
  `vlt-lint:17` JIT) — the contract is the one eagerly-read governance surface.
- **Two-home constraint (grounding addition):** the ritual is also single-homed at
  `contract:161` ("Activation ritual — two beats") — any disposition must move the three SKILL
  openers **and** the contract's own ritual section in step. Ceremony-not-sanctum is a standing
  ruling (2026-06-03), honored by all three dispositions.

> **Open design question (verbatim):** The ideation session surfaced a deeper trade the owner
> may want to rule on once, arc-level: how much governance must be loaded *pre-hoc* versus
> enforced *post-hoc* by `vlt-lint`/review-council (optimistic execution, cheap correction).
> That is a governance-guarantee trade, not an optimization, so it is deliberately **not** a
> disposition here — but (a)/(b) sit on its spectrum and a ruling would settle several filings
> at once.

### A4-16. Hand-offs and consults repay the full boot (2026-07-29) — 2026-07-29-082931-handoffs-and-consults-repay-the-full-boot.md

**Verdict: both claims CONFIRMED (the consult half as the filed "plausibly" — a prompt-ambiguity
gap, not a mandated read); one citation correction.**

- The same-conversation skip covers Beat 2 only (`researcher/SKILL.md:31`, identical in both
  others); the contract read at `:22` sits textually outside it, and the contract's hand-off
  section (`:211-215`) grants no exemption either. Researcher→librarian is the canonical
  main-path hand-off (`researcher:46`; a hand-off ends a sitting, `contract:213`).
- The consult prompt (`vlt-consult.js:125` "Read your SKILL… and BECOME that partner") says
  nothing about skipping the ritual; the SKILL has hand-off and headless carve-outs but **no
  consult carve-out**. Nuance: `contract:213` already exempts the consult's *exit* (no session
  note, no sitting boundary) — only the *entry* is ungoverned. Dispatch frames consult as cheap
  (`vlt-dispatch:18` "traffic, not a queue item"; `:205` depth-1 hard).
- **Citation correction:** `vlt-dispatch:207` makes the dispatch §consult section the mechanics
  home ("This section owns the mechanics"), not the engine; a consult-lite boot edit lands in
  the engine prompt (`vlt-consult.js:123-143`), but the pointer chain is contract → dispatch
  §consult → engine.
- `consult@1` governs when-earned, not the summoned boot — a boot exemption there is plausibly
  prose-clarification (no bump), but that call is ideation's.

> **Open design question (verbatim):** Note the consult convention (`consult@1`) governs *when*
> a consult is earned, not the summoned boot — a prose clarification there may suffice without a
> version bump, but that is capture's call under the handshake rules. *(Capture's read: the
> change is additive prose defining the summoned partner's read surface — likely no bump — but
> the ruling is deferred to ideation with the build that would make it.)*

### A4-17. Beat 2 orient scales with vault age (2026-07-29) — 2026-07-29-082932-beat-2-orient-scales-with-vault-age.md

**Verdict: CONFIRMED with two sharpenings — the gap is narrower than filed for `thread.md`,
wider than filed for `{log}`; and the unbounded read list has TWO homes.**

- Beat 2's read list is unbounded in both homes: partner SKILLs `:25` (all three) **and**
  `contract:167` — `{index}` unqualified, "recent `{log}`" with no N, `{backlog}`, `thread.md`,
  open dispatch slice, capabilities. Any bounds fix keeps two homes in step (the filing notes
  only one).
- `{log}` and `{index}` grow with module output (`contract:36,116`; every sitting appends,
  `:213,215`) and **no rollover/archival rule exists anywhere** — the `{archive}` mechanics
  (`:63`) cover retired notes, not the log. For `{log}` the gap is total.
- `thread.md`: "prunable" (`researcher:18`) — but the contract **does** state the how
  (`:190` — supposed to fade, attention steward, `## Set aside`, never silently deleted; `:215`
  puts set-aside in every close). What's missing is a **bound/trigger**, not a mechanism.
- The filing's own ship-verifiable (mechanism) vs field-contingent (magnitude) split is
  correctly drawn; the work vault is the named evidence source, A4-18 the instrument.

Open design questions: none beyond the four dispositions (a) bounds / (b) orient digest /
(c) measure-first sequencing behind A4-18 / (d) pruning discipline — carried as filed.

### A4-18. No instrument measures session token cost (2026-07-29) — 2026-07-29-082933-no-instrument-measures-session-token-cost.md

**Verdict: GAP CONFIRMED by exhaustive absence check; baseline figures re-measured with two
corrections. The batch's measurement keystone.**

- No sizing instrument anywhere: `tools/` is package-lint only; `vlt-lint` has no cost surface
  (its "cost" mentions are model tiering `:42` and coverage caps `:200,203`); the session-note
  schema records nothing about reads; `vlt-track` nothing.
- Re-measured at HEAD: contract 38,271 ✓; partner SKILLs ~10–11.5K ✓; lint 41,202 ✓; dispatch
  38,285 ✓; **"all skills ~267K"** = exactly 267,254, but SKILL.md files only (tracked `skills/`
  content is far larger — the label needs the qualifier); **"conventions 86K"** conflates
  populations — conventions dir alone is **73,387** (8 files); 86,335 only with the 5 persona
  files (`_meta/` minus contract); frontmatter.md is **22,977 chars** (22.4 KiB — a units slip).
- The bell principle is standing doctrine; token cost has no bell in any tier. The sequencing
  claim is confirmed: A4-17 defers its bounds to "measure first," and A4-15/A4-19's savings are
  unquantifiable without this.
- Dispositions: (a) a `tools/` script (release-choreography adjacent); (b) has frontmatter@N
  handshake implications, flagged in the filing; (c) conflicts with A4-19's lint-weight concern
  by the filing's own admission; (d) one-shot measurement.

> **Open design question (verbatim):** Preference, weakly held: **(d)** — and whichever lands
> should run once against the work vault before the other filings in this batch are briefed, so
> their dispositions are chosen against numbers.

### A4-19. Whale files carry restated weight (2026-07-29) — 2026-07-29-082934-whale-files-carry-restated-weight.md

**Verdict: CONFIRMED with figure corrections; the single-home discipline is holding — this is a
weight problem, not a drift problem.**

- Sizes re-measured: lint 41,202 + dispatch 38,285 + contract 38,271 = **117,758 (~118K)** — and
  the filed "~116K of ~267K" mixes populations (the contract is an asset, not in the 267K
  SKILL.md denominator). Honest phrasing: three files totalling ~118K against a 267K SKILL.md
  surface.
- Lint references **7 of 8** conventions (all but `wiki-consolidation.md`, grep-zero); the seven
  sum to **65,506 chars (~65.5K, not ~70K)**. Dispatch carries four modes' mechanics in one file
  (`:69` daily, `:148` relay, `:203` consult, `:297` ledger). frontmatter.md is the conventions
  whale at **22,977** — 2× the next (extraction.md 11,310).
- Single-home holding: lint JIT-reads conventions before fixes (`:17`); dispatch delegates the
  trigger rule to the contract (`:211`) and points at `consult.md` (`:207` — same correction as
  A4-16: dispatch's section is the mechanics home; the engine holds only the spawn prompt).
- Disposition notes: (a) per-mode progressive disclosure is the structurally largest change
  (SKILL-router + reference files — new cross-file agreement to keep lintable;
  **check `package-lint.py`'s packaging expectations before briefing**); (c) folds into A4-15's
  digest disposition; (d) sequences behind A4-18.

> **Open design question (verbatim):** Preference, weakly held: **(b) soon** (safe, composable),
> **(a) briefed against (d)'s numbers** — cut lines chosen from measured per-mode loads, not
> guessed.

### A4-20. Adoption stamp unreachable beyond mint (2026-07-29) — 2026-07-29-120001-adoption-stamp-unreachable-beyond-mint.md

**Verdict: GAP CONFIRMED — a reachability gap in module source, with an internal inconsistency
named at grounding. Owns the claim A4-14's addendum deduped here.**

- `vlt-mint/SKILL.md:176` is the exclusive writer ("Nothing else may write this key; `vlt-lint`
  never does"); grep confirms no other writer exists. Both non-mint roads are real **in module
  source**, not just field accidents: the module's own proto-spec retrofit creates spec
  instances with "zero body changes" and no stamp beat (`vlt-upgrade:79`), and the consult path
  (`vlt-consult.js`, `consult.md`) has none either.
- The reporter is honest and three-valued (`vlt-upgrade:105,112,131` — never omitted, never a
  gate). A4-2's acceptance clause 5 defined reachability exclusively in mint vocabulary
  (`build-A4-2…md:624`) — it never contemplated a non-mint first instance.
- **Internal inconsistency:** `frontmatter.md:242` says the reference is recorded "the moment
  that instance appears" — impossible off the mint path under the writer topology.
- **Structural lock-out confirmed:** a vault cannot self-stamp without tripping
  `convention_base_divergence` (`vlt-lint:81`) and the `.baseline` compare — so a second writer
  must also rule **where the stamp write is allowed to land**.
- Fix sites: `vlt-mint:176` (sole-writer rule), `frontmatter.md:242`, plus whichever surface
  gets a second authorized stamp beat — or an explicit mint-borne-only scope statement.

> **Open design question (verbatim):** Wants either a second authorized writer (an owner-ruled
> stamp beat somewhere on the consult/spec paths), or an explicit statement that the axis
> measures mint-borne adoption only.

### A4-21. Entity-collision coverage pair-incomplete (2026-07-29) — 2026-07-29-120002-entity-collision-coverage-pair-incomplete.md

**Verdict: GAP CONFIRMED — and the mechanism is sharper than filed: greedy cluster consumption,
not absent linkage. This is A4-4's still-FAILED acceptance clause 5; its fix rides this
capture.**

- `vlt-lint-full.js:204-219`: clusters are built greedily from link adjacency —
  `clustered.add(s.slug)` consumes each page into the *first* matching cluster, and
  `entity_collisions` is only asked within a cluster (`:106-117`, prompt `:229+`). Consequences:
  unlinked pairs are never compared, **and even directly-linked pages can be split** — vlt-core's
  `los-angeles-rams.md:72` links the missed counterpart directly, so the pair was almost
  certainly lost to greedy consumption. **The fix is a cluster-aware second pass, not a looser
  linkage test.**
- The report is honest about the limit (`vlt-lint:207` verbatim disclosure; `:74` single-mention
  blind spot; `:189` denominator).
- No pass reads already-flagged name callouts to seed pairs (`:68` surfaces `[!stale]`
  generically; nothing feeds the entity pass). Minor vault-citation correction: the "Which
  Jackson?" callout starts at `los-angeles-rams.md:76`, not `:77`.
- Fix sites: `vlt-lint-full.js` cluster formation and/or a callout-seeded pair pass, plus
  `vlt-lint:207`'s `entity_scan:` composition rule if the compared population changes. No
  handshake implications apparent.

No open design questions filed; the proposed shape (a cluster-aware second pass over
already-flagged name callouts) is carried as a proposal, not a ruling.

### A4-22. Sayari upgrade omitted convention-adoption line (2026-07-29) — 2026-07-29-120003-sayari-upgrade-omitted-convention-adoption-line.md

**Verdict: GAP CONFIRMED as reliability — with a PROVENANCE CORRECTION that relocates the fix:
the template already carries the line; what's missing is the completeness check.**

- The never-omit rule is module source, verbatim as filed (`vlt-upgrade:112`; report key
  `:105`). Sayari's ledger omission is field-attested (work-machine vault; corroborated by this
  roadmap's run-3 record and owner confirmation).
- **Correction:** the filing wants the ledger template to name the line as required — **it
  already does**: `vlt-upgrade:131` lists `- Convention adoption: <list>` exactly as
  Mints/Overlays/Migrations are listed. The genuine gap is one step along: **the Verify section
  (`:146`) checks that a dated block exists, never that it carries its required fields** — a
  skipped line survives the skill's own close-out.
- Sharpened fix sites: `vlt-upgrade` Verify (`:146`) field-completeness check, and/or
  required-vs-optional markers in the `:123-132` template (several lines say "or none"; the
  adoption line doesn't say "required"). Open sub-question: whether the post-flight *report*
  (`:92-108`) needs the same completeness net.
- Cross-dependency: this line is the adoption axis's only reporter (see A4-20).

> **Open design question (verbatim):** Wants whatever makes the post-flight report's required
> lines hard to drop (a checklist the ledger entry template carries, or the ledger-entry format
> in `vlt-upgrade` Step 5 naming the line as a required field). *(Grounding note: the second
> option already exists; the live fork is Verify-side check vs template-side required markers.)*

### A4-23. Lint report block is never persisted (2026-07-29) — 2026-07-29-120004-lint-report-block-is-never-persisted.md

**Verdict: GAP CONFIRMED; one PROVENANCE CORRECTION on which keys are Arc-4-new. Load-bearing
for the loop itself — the factory is the first consumer.**

- Step 5 produces "a parseable report (stable keys, so a dashboard can consume it)"
  (`vlt-lint:149`, block `:147-201`) with **no write destination anywhere**; Step 6 appends only
  the one-line `{log}` entry (`:211-219`, no session note per contract session-ownership). The
  only durable residue of a lint run is the `{log}` line plus landed fixes/backlog items.
- The `{log}` lint-entry shape (`:216`) is **byte-identical at v0.7.0** — no Arc-4 slot fits it.
  Irony worth keeping: `contract:116` says of `{log}` "a future dashboard parses it" — the
  dashboard framing exists in two places and the richer surface evaporates.
- **Correction:** `linkage_ripe`/`revisit_due` are build-20 (Arc 3, v0.7.0), not Arc-4-shipped;
  the Arc-4-new keys are `research_zone` (`:175`), `contradiction_scan` + three splits
  (`:184-188`), `entity_scan`/`entity_collisions` (`:189-190`),
  `authority_scan`/`consult_missing` (`:191-192`). The point stands: none of them, old or new,
  reaches a durable surface.
- Two discharge runs verified report-shape clauses only via owner hand-paste (this roadmap's
  run-2/run-3 records) — eleven sub-clauses are unverifiable without persistence.
- **Design-relevant grounding:** `contract:57` permits ad-hoc `_agent/` artifacts without a
  structure-map change; the derive-first clause is at `contract:260` and the filing's
  report-is-an-observation framing is consistent with it but **not yet a ruled position**;
  wrinkle — `vlt-lint` is forbidden to write session notes (`:219`), so the session-note home
  would be the *summoning partner's* obligation, a cross-surface rule.
- Residual scope: persistence home; whether scoped-mode runs persist too; retention/series
  semantics (the trend questions imply keeping run N−1).

> **Open design question (verbatim):** Wants a persistence home for the report block (a dated
> artifact under the agent zone, or the session note carrying the block verbatim as a fenced
> trailer) — chosen with the derive-first rule in mind: persisting a *report* is recording an
> observation, not storing derivable state.

## Carried forward past Arc 3 — re-listed (2026-07-29, per the archived hand-off contract)

The archived Arc-3 roadmap's *Carried forward past Arc 3* section says the next `inbox-capture`
re-lists it — "anything left off is silently dropped." Re-listed here in full; the archive holds
the binding text. **None of these is discharged by this capture**; they travel to Arc 5's
standing surface unless an ideation ruling disposes them sooner.

- **Standing watches (released, not verified — none may be read as passed):** build-19
  empty-`_agent/specs/` lint negative case (needs a fresh-install vault); build-18 F3
  post-upgrade write op honoring an overlaid rule (sayari-relay only); build-21 A3-14
  overlay-subsumption on `extraction.overlay.md:13` (sayari-relay only, no clock); build-22 F1
  full four-lens `KIND_PANEL` on a roster-changing mint; build-22 F2 partner/heavy-cap mint
  registering only in the live CSV; build-23 F4-in-the-field (someone citing `vlt-lint:74`'s
  pin-not-conformance limit correctly).
- **Named actions with a trigger:** build-18 F1 `skill_asset_divergence` detect — STAGED for a
  pre-upgrade deliberate vault-local asset edit (**note: the vlt-core 0.7.0→0.8.0 upgrade ran
  2026-07-26; whether the staged edit was made is not recorded here — if it wasn't, the stage
  re-arms for the next upgrade**); 091006/build-16 first review-cycle evidence — **DATED WATCH
  2026-08-17** (`spec.md:16`), fires without owner action.
- **Tracked design debts:** Q21 governance-wide supersession convergence (intersects A4-9's
  option (b) — see that entry); Q27 standing loop-profile detector + roster-level declaration;
  Q24 sanctioned mint-upstreaming path; build-23's vault-side conformance spot-check (extend
  `vlt-lint:74` to re-read consumer bodies).
- **Standing metric:** 091002 zero packaging filings for releases ≥0.6.0 — **HOLDING** (now four
  releases through 0.8.0; this batch's 18 filings include zero packaging filings — re-probed at
  this capture, still holding).
- **Owner action filed elsewhere:** file the BMB template drift (`after,before`) upstream to
  BMAD-METHOD.
- **Transferred to Arc 5 (not captured this run — Arc 5's capture owns them):** build-17, the
  enforcement kit (evidence-blocked, never built) with its filing
  `inbox/2026-07-06-091003-enforcement-kit-derive-first.md`, and 091003 M0 (counter-accuracy
  audit + tripwire-hit data, unpayable until counters exist). When Arc 5's roadmap stands up,
  these enter its capture alongside the A4-6..A4-23 batch above.

## Status & next step — after capture (2026-07-29)

> **⛔ This arc is archived — do not append.** Closed 2026-07-29 by `arc-closeout`; the two-track
> "next move" below is historical — track 1 completed (heavy-ingest trigger fired, discharge run 4,
> closeout run), track 2 (Arc-5 ideation over the seed batch) is what remains, recorded in
> **Carried forward past Arc 4** below.

Arc 4's own position is unchanged by this capture: acceptance discharged except A4-4's two tails
(heavy-ingest split; the FAILED entity-pair clause, whose fix now rides **A4-21**), plus the
non-gating sayari lint-render halves. The 18-filing batch above is grounded and waiting; it is
**Arc 5's** raw material, together with the two Arc-3 transfers (build-17 + 091003 M0).

**Next lifecycle move:** two tracks, not one —
1. **Arc 4:** exercise the heavy-ingest trigger, re-run `acceptance-discharge`; once A4-4
   resolves or is owner-carried, run `arc-closeout` (its Stage 5 owns this arc's deferred filing
   archival, per the standing 2026-07-27 ruling).
2. **The batch:** owner-steered **ideation** over A4-6..A4-23 (+ the build-17 transfer) —
   grouping, order, scope rulings — which stands up Arc 5. The batch carries its own sequencing
   signal: A4-18's instrument wants to run against the work vault **before** the boot-cost
   filings are briefed, and A4-13/A4-14's shared proxy-check framing question wants a single
   owner ruling up front.

## Carried forward past Arc 4 (recorded at close, 2026-07-29)

This is the authoritative hand-off point: the next `inbox-capture` re-lists from here —
anything left off is silently dropped. None of these is discharged by the close.

- **Inherited debt → Arc 5 (the build-20 form):** A4-4 clause (5), graded **FAILED** 2026-07-27
  and owner-confirmed 2026-07-29 — entity-collision coverage is silently pair-incomplete: the
  cluster-bounded sweep found the Seahawks instance and missed its explicitly-paired Rams twin
  (`los-angeles-rams.md:77`), a known, already-documented collision the page itself says "one
  lookup settles both." Filed as
  `inbox/2026-07-29-120002-entity-collision-coverage-pair-incomplete.md` and **captured as A4-21**
  in the seed batch below; the fix rides Arc 5. Its filing
  (`inbox/2026-07-25-160949-auto-caption-name-substitution.md`) is **held in the active inbox**
  as the debt's carrier — carried from the Arc-4 ledger, STILL OPEN at arc close, carries forward
  past Arc 4. A4-4's box stays unchecked on this clause alone; the `[x]` count may not be read as
  a measure of what the arc proved.
- **Standing watch (released, not verified — none may be read as passed): the sayari lint-render
  halves.** A4-1 (6) (same-order `linkage_ripe` surfacing rate), A4-3 (7) (the three contradiction
  slots + `contradiction_scan:` denominator rendering, an empty vault still emitting the
  denominator), A4-4 (8, run half) (`entity_scan:`/`entity_collisions:` rendering). Install halves
  are all verified on sayari at 0.8.0; **trigger:** the first vlt-sayari full `vlt-lint`.
  Field-contingent, non-gating per the ship-verifiable rule — released at close, not ticked.
- **Standing watch: the consult channel's refusal path.** A4-5 clause (4) — a non-`answer` consult
  return is still unexercised (both live consults answered, both inspected). When consults only
  ever return `answer`, that is the confabulated-authority signature: inspect, don't assume.
- **The Arc-5 seed batch:** A4-6..A4-23, captured in this roadmap (grounded against v0.8.0 @
  `9f05579`), awaiting owner-steered ideation — grouping, order, scope rulings — which stands up
  Arc 5. Sequencing signals recorded above: A4-18's instrument runs against the work vault before
  the boot-cost filings are briefed; A4-13/A4-14's shared proxy-check framing wants one owner
  ruling up front. All 18 filings remain in the active inbox (captured ≠ built ≠ accepted).
- **Re-listed Arc-3 carry-forwards** (binding text in the archived Arc-3 roadmap; re-listed in
  full in *Carried forward past Arc 3 — re-listed (2026-07-29)* above): six standing watches
  (build-19 empty-`{specs}` negative case; build-18 F3; build-21 A3-14; build-22 F1; build-22 F2;
  build-23 F4-in-the-field); the **staged** build-18 F1 `skill_asset_divergence` detect (whether
  the staged edit rode the 0.7.0→0.8.0 upgrade is not recorded — if not, it re-arms for the next
  upgrade); the **dated watch 2026-08-17** (091006 first review-cycle evidence, `spec.md:16`,
  fires without owner action); design debts **Q21 / Q27 / Q24** + build-23's vault-side
  conformance spot-check; the **standing 091002 packaging metric** (zero packaging filings for
  releases ≥0.6.0 — HOLDING through 0.8.0); the **owner action** to file the BMB template drift
  (`after,before`) upstream to BMAD-METHOD; and the **Arc-5 transfers** build-17 (the enforcement
  kit, with `inbox/2026-07-06-091003-enforcement-kit-derive-first.md`) + 091003 M0.
- **Arc naming:** the arc closes under the clerk's proposed title (*the honest-surface arc*) —
  `arc_title_status:` was never re-ruled; no obligation carries, noted for the record.

### Filing archival at close (Stage 5 record — which filings moved under which criterion)

Moved to `inbox/archive/` under the per-filing criterion (every clause traceable to the filing
discharged with dated evidence; remaining build tails attributable to a different filing):

- `2026-07-25-162416-linkage-ripe-cannot-see-graduation.md` (A3-23 → A4-1; fully discharged run 2;
  the sayari half is the released watch above, a second-vault comparison, not a clause of this
  filing's defect)
- `2026-07-25-144500-revisit-after-has-no-adoption-path.md` (A3-19 → A4-2; fully discharged run 3)
- `2026-07-25-160239-contradictions-have-no-drain.md` (A3-20 → A4-3; fully discharged run 3)
- `2026-07-25-132141-partner-consult-synchronous-channel.md` (A3-22 → A4-5; fully discharged run 3)
- `2026-07-18-115913-chess-coach-persona-line-seeds-fabricated-time.md` (A3-18 → **no build**,
  owner-ruled 2026-07-25: vault-local mint prose, not module source; "its evidence debt closes
  with it" — closed by ruling, not by acceptance; archived so the active inbox stays honest)

Held in the active inbox: `2026-07-25-160949-auto-caption-name-substitution.md` (A3-21 → A4-4;
its own clause (5) is the inherited debt above) and all 18 seed-batch filings plus the four
run-2/run-3 findings (`…-120001` … `…-120004`), which are captured but unbuilt.
