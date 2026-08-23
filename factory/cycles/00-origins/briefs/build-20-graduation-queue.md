---
title: 'Build #20 — the research-note graduation queue, first cut (opens frontmatter@4; kills the module-caused topic: scalar the whole cluster tripped on)'
status: 'BUILT 2026-07-17 — F1–F5 landed + unit-verified at rest on branch arc3-v0.7.0. Handshake bipartite=5, all consumers (vlt-ingest/extract/research/lint/mint) pin frontmatter@4 (opened @4); topic: scalar→list fix verbatim-matches vlt-ingest:84 (scalar gone); revisit_after references review_after single-home (no restate of resolved-date/absence-evergreen); adoption facet + two documented-optional wiki slots ride the one @4 bump; linkage_ripe/revisit_due checks + report keys added, {research} topic: scope widened; vlt-lint-full.js UNCHANGED (research pass is the SKILL inline jurisdiction). package-lint A/B/C PASS @0.6.0 (not a release build). Deviations: (a) built directly — brief named bmad-workflow-builder but the build ships no workflow (same as build-19); (b) F1 uses the verbatim vlt-ingest:84 placeholders (<broad domain>/<narrower facet>) per the binding "match verbatim" instruction + verification, not the F1 code block''s illustrative <general>/<specific>; (c) F5 took the no-workflow-edit path (the inbound-count optimization declined as optional — keeps node --check N/A); (d) adoption facet keyed adoption_first_instance: (brief gave semantics, no key name); (e) revisit_after placed after sources in schema + write template, mirroring review_after''s last-position.'
module_code: 'vlt'
created: '2026-07-17'
derives_from:
  - 'inbox/2026-07-11-114226-research-note-graduation-queue.md (A3-7 design half: candidacy key, linkage finding, ingest probe, dispatch line — surviving shape only)'
  - 'inbox/2026-07-11-153000-graduation-queue-field-calibration.md (A3-8 vlt-core calibration: union projection ~79%→~21% FP, topic: raggedness is module-caused, K not observed)'
  - 'inbox/2026-07-12-114837-graduation-queue-sayari-calibration.md (A3-9 vlt-sayari calibration: union 69%→23% on the opposite vault profile; scan-surface + lint-cadence binds)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings A3-7..A3-17 (2026-07-17): build-20 = graduation queue first cut, surviving shape only (union projection, revisit_after, linkage_ripe, defer cluster_ripe, trivial backfill); research-zone-first; rides the severable vlt-research:65 fix (fix-then-measure); scopes the missing vlt-lint-full.js research read path honestly; OPENS frontmatter@4 — one coordinated bump, one 5-consumer walk (exit-gated at vlt-mint:141), inherits the parked batch + the adoption/first-instance facet.'
risk: 'moderate — bumps a convention version (frontmatter@3→@4) so it triggers the full 5-consumer walk (vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint); the graduation checks themselves are additive/read-only (lint surfaces, never mutates). The severable vlt-research:65 fix is low-risk and correct on its own terms.'
---

# Build #20 — the research-note graduation queue, first cut

## Intent

Research notes accumulate in `{research}` with no lifecycle statement: nothing marks a note
as *ripe to graduate* into the wiki, and — the defect grounding found underneath the whole
cluster — the module's own write template tells every research note to write `topic:` as a
**scalar**, contradicting the schema that says it must be a list, which is what manufactured
the `topic:` raggedness the field calibrations reported as *data blocking clustering*. This
build lands the **first cut** of a graduation queue: a candidacy freshness key
(`revisit_after`), a **union-projection** linkage finding in `vlt-lint` (`linkage_ripe`),
the severable `vlt-research:65` scalar→list fix, and the trivial-by-construction backfill —
while **opening `frontmatter@4`** (the coordinated version bump this batch was ruled to own)
and doing the single 5-consumer walk.

It closes A3-7's surviving design shape and the two field calibrations (A3-8 vlt-core, A3-9
vlt-sayari) that validated the union projection on two vaults of opposite profile
(FP ~79%→~21% and ~69%→~23%). **All rejected alternatives in the parent filings are settled
— do not re-litigate**: naive frontmatter-only projection (rejected for the union),
`cluster_ripe`/K-threshold (deferred, not this cut), verbatim-copy of `review_after`
semantics (forbidden by `frontmatter.md:115`'s single-definition rule — use a pointer), and
the `ingest:`/`cluster_ripe` candidacy keys (dropped from the first cut).

This is **not a release build** (build-20 of the 19–23 group). The module `version:` bump
and tag ride the arc's release build; this build bumps only the **frontmatter convention**
version (`3→4`) and walks its consumers.

## Brief-time dispositions

Each resolves a question the roadmap left to build-20's brief (`roadmap §Ideation rulings
A3-7..A3-17 → "Questions deliberately left to brief time → build-20"`), or a HOW the RULED
coordinated bump left open. Cited, not re-litigated.

1. **Q1 (K cluster-threshold default) — MOOT, no K this cut.** The surviving-shape ruling
   defers `cluster_ripe`; with no clustering finding built, there is no K to default. The
   date-ordering and per-source signals A3-8 proposed as `cluster_ripe` replacements are
   **not built either** — they need the research read path F5 defers. Recorded so a later
   build re-opens K only alongside `cluster_ripe`.

2. **Q3 (ingest-time probe scope: any-shared-`topic:` vs most-specific) — DEFER the probe to
   the named second cut.** The surviving-shape list contains no ingest-time probe; it is a
   detection surface that needs both the post-fix `topic:` data (fix-then-measure, Q2 ruled)
   and a research read path the workflow lacks (F5). The first cut is **lint-cadence
   detection only** (`linkage_ripe`/`revisit_due`), not ingest-time probing. So Q3's
   axis-choice does not arise this build.

3. **Q4 (aging-queue escalation: lint promotion vs enforcement-kit tripwire) — EXTEND the
   existing precedent: tripwire, not lint.** `vlt-lint/SKILL.md:62` already rules for the
   review queue that "escalation of an aging queue is a tripwire concern, not lint's." The
   graduation queue is the same shape. `vlt-lint` **surfaces** candidates
   (`flag_for_human`, never nag, never auto-promote — the `review_due`/merge-candidate
   pattern); escalation of the aging graduation queue is a **tripwire concern deferred to
   build-17's enforcement kit**. Extending a stated position, not inventing one.

4. **Q5 (`review_after` wiki vs `revisit_after` research near-homophones) — name the research
   candidacy key `revisit_after:`, and DROP `revisit_when:`.** One research-candidacy
   freshness key, named `revisit_after:` (parallel to the wiki key `review_after:`, its
   semantics referenced by pointer per `frontmatter.md:115`, never redefined). A3-7's
   separately-parked `revisit_when:` is a redundant near-homophone twin — shipping both is
   exactly the self-confusing surface this arc's thesis flags; it is dropped, not parked.

5. **The RULED coordinated `@4` bump — HOW the parked batch lands.** The owner ruled build-20
   opens `frontmatter@4` inheriting the parked batch "one coordinated bump, one consumer
   walk" (roadmap `:1658`). Honored: **one** version bump, **one** 5-consumer walk. What
   lands as live schema with a consumer this build: `revisit_after:` (consumed by F4's
   `linkage_ripe`/`revisit_due`) and the **adoption/first-instance facet** on the enforcement
   declaration (re-homed here from build-17 per `:1631`, ruled GENERAL at `:1685`). The
   remaining parked keys — `source_type:`, `review_note:` (091006 OQ5, parked *against usage
   evidence*) — land as **documented-optional schema slots** (absence = default, no rule, no
   check): they ride the single `@4` bump so the walk never churns twice, but impose **zero
   obligation** until usage evidence arrives (which honors both `:1658` and 091006 OQ5, and
   keeps the arc's "defined-but-unenforced" line — an inert optional slot is not an
   unenforced *rule*). `revisit_when:` is dropped (disposition 4); `ingest:`/`cluster_ripe`
   candidacy keys are out of the surviving shape.

## F1 — `vlt-research/SKILL.md`: the `topic:` scalar fix (severable, fix-then-measure)

**Current state.** The research-note write template (`skills/vlt-research/SKILL.md:57-70`)
emits, at **`:65`**:
```yaml
topic: <subject area>
```
a **scalar**, contradicting `frontmatter.md:131` ("Research notes use the same `topic:` list
form as wiki pages, general → specific, lowercase") and its sibling
`vlt-ingest/SKILL.md:84` (`topic:` written as a YAML list). Per roadmap A3-7, 55 of 92
vlt-core research notes carry the scalar form the module told them to write.

**The exact change.** Replace the scalar with the list form, matching the ingest sibling's
shape and comment:
```yaml
topic:                             # YAML list, general → specific, lowercase
  - <general>
  - <specific>
```
Mirror `vlt-ingest/SKILL.md:84` exactly (same comment wording) so the two write templates
agree verbatim.

**Why.** Correct on its own terms independent of the queue (roadmap `:1641`,
"ships regardless of the queue's fate"). It is the substrate the calibrations' `topic:`
raggedness rests on; fixing it is the **fix** half of the ruled *fix-then-measure* (Q2) — the
raggedness is re-measured on post-fix data before any `topic:`-based clustering is ever ruled
(that measurement is an acceptance item, not this build's work).

**In scope beyond the letter:** this file also gets its `depends_on` re-pinned to
`frontmatter@4` — see F3 (it is a listed consumer).

## F2 — `frontmatter.md`: open `frontmatter@4` (the coordinated bump)

**Current state.** `version: 3` (`:11`); `consumers: [vlt-ingest, vlt-extract, vlt-research,
vlt-lint, vlt-mint]` (`:12`); research-note schema at `## Research notes ({research})`
(`:119`, key statement `:131`); `review_after` single-definition rule at `:115`; the
enforcement declaration block (build-16 lineage) carries a violation facet but no adoption
facet.

**The exact change** (one coordinated bump — disposition 5):

- **Bump `version: 3` → `version: 4`** (`:11`). A schema-field addition is a rule change per
  the mint Step-4 bump rule (`vlt-mint:139`).
- **Add `revisit_after:` to the research-note schema** (`:119-131` block): an **optional**
  research-note key naming the date the note's graduation candidacy should be rechecked — a
  **resolved date, never a duration; absence = not-a-candidate (evergreen-off)**. Its date
  semantics **reference `review_after`'s single definition at `:115` by pointer** — "the
  wiki-page key's semantics, applied to a research note's candidacy" — **never restate them**
  (`:115` forbids redefinition verbatim; A3-7 grounding flagged the verbatim-copy mechanism
  as wrong). Note the schema already states research notes carry no `last_updated` (`:131`) —
  `revisit_after` is the self-announcing freshness signal, exactly as `review_after` is for
  wiki pages.
- **Add the adoption/first-instance facet to the enforcement declaration** (re-homed from
  build-17 per roadmap `:1631`; ruled GENERAL as a schema facet at `:1685`): the declaration
  grows a facet recording a boundary's **first live instance / adoption state**, one
  class-wide answer usable by specs and loop profiles alike. Schema + semantics only —
  "whatever checks consume it live where checks live" (`:1688`); this build defines the
  facet, not its checks.
- **Add `source_type:` and `review_note:` as documented-optional wiki-page slots** (091006
  OQ5 parked batch) — optional, absence = default, **no rule and no lint check this build**
  (disposition 5). They ride the single `@4` bump only so the consumer walk is not churned a
  second time when usage evidence later activates them.

**Why.** The batch was ruled to open `@4` as one coordinated bump (`:1658`) per the build-16
"one coordinated bump, NOT split" precedent. `revisit_after` is the queue's candidacy
substrate; the adoption facet is its re-homed schema owner.

**Out of scope here:** `revisit_when:` (dropped, disposition 4); `ingest:`/`cluster_ripe`
keys (not surviving shape); any `.base` file (`:117` — module ships none; the graduation
views are documented-reference only, per the standing 091006 OQ1 owner ruling); `module.yaml`
`vault_structure` (untouched — candidacy is a frontmatter key, not a new zone; `{research}`
already exists at `module.yaml:47`).

## F3 — the `frontmatter@4` consumer walk (5 consumers; exit-gated)

**Current state.** All five listed consumers pin `frontmatter@3` today:
- `vlt-ingest/SKILL.md` `depends_on: [..., "frontmatter@3", ...]`
- `vlt-extract/SKILL.md` `depends_on: ["extraction@2", "wiki-supersession@1", "frontmatter@3", "write-verification@1"]`
- `vlt-research/SKILL.md` `depends_on: ["frontmatter@3", "write-verification@1"]`
- `vlt-lint/SKILL.md` `depends_on: [..., "frontmatter@3", ...]`
- `vlt-mint/SKILL.md` `depends_on: ["spec@1", "frontmatter@3"]`

**The exact change.** Per `vlt-mint:140-141` (the Step-4 walk + exit gate): for **each**
consumer, reconcile its text against the new keys and **bump its `depends_on` ack
`frontmatter@3` → `frontmatter@4`**. Expected reconciliation outcomes:
- **`vlt-research`** — edited (F1's template `topic:` fix + it is where `revisit_after` is
  *written* if the writing partner sets a candidacy date; add the optional key to its write
  template with the "absence = not-a-candidate" note). Ack bumped.
- **`vlt-lint`** — edited (F4 adds the graduation findings + widens the `topic:` scope). Ack
  bumped (covers `vlt-lint-full.js` per the workflow-asset rule at `vlt-lint:74`).
- **`vlt-ingest`, `vlt-extract`, `vlt-mint`** — **no edit needed** (they neither write nor
  read `revisit_after`/the adoption facet/the optional slots); **bump the ack anyway** —
  recording that a human verified the consumer against `@4` is the point of the ack
  (`vlt-mint:140`).

**Exit gate (`vlt-mint:141`):** the bump cannot close while any of the five still pins
`frontmatter@3`. Grounding-enumeration note: the capture (A3-7) named only `vlt-extract` and
`vlt-mint` for re-pin; **all five** must move.

**Why.** The version-handshake standing rule (CLAUDE.md): a convention rule change bumps
`version:` and re-acks every consumer in the same build, bipartite-consistent.

## F4 — `vlt-lint/SKILL.md`: widen `topic:` scope + the graduation findings

**Current state.**
- `:60` — the frontmatter/Bases-field drift check (`topic:` present and a YAML list) is
  scoped "**for every wiki page**".
- `:89` — the `topic:` string→list auto-fix sits under the same wiki-only heading.
- `:59` — a `[[wikilink]]` resolving to a cross-layer (`{research}`) note is already a
  legitimate edge (the union projection's body-linkage component is machinery already
  shipped, per A3-8).
- `:62` — `review_due` is surfaced, never nagged; aging-queue escalation ruled a tripwire
  concern (the Q4 precedent).
- No graduation-candidacy finding exists.

**The exact change.**
- **Widen the `topic:`-is-a-list check (`:60`) and its string→list auto-fix (`:89`) to
  `{research}`.** The healing machinery exists; only its scope clause needs "for every wiki
  page **and every `{research}` note**" (the auto-fix is safe there identically). This is
  what mostly dissolves the calibrations' `topic:` raggedness at the source (A3-7/A3-8).
- **Add `linkage_ripe`** (governance/candidacy check, both modes): a `{research}` note is
  graduation-**ripe** when the **union projection** flags it — frontmatter `topic:` overlap
  **∪** body `[[wikilink]]` inbound from ≥1 wiki page **∪** shared-`sources:` overlap with a
  wiki page. Surface as `flag_for_human` (candidate + why), **never auto-promote** (matches
  the merge-candidate/`review_due` pattern; routing to a partner is not lint's job). The
  union — not naive frontmatter-only — is mandatory: A3-8/A3-9 measured naive at ~79%/~69%
  false-positive vs union ~21%/~23% on two opposite-profile vaults.
- **Add `revisit_due`** (candidacy freshness): a `{research}` note whose `revisit_after:` is
  past → `flag_for_human` (note + date). Same posture as `review_due` (`:62`) — surface,
  never nag, never auto-resolve.
- **Report keys:** add `linkage_ripe` and `revisit_due` slots to the structured report
  (siblings of `review_due` at `:135`); use a **term distinct from `orphans`** for the
  linkage finding — `fix_now.orphans` (`:117`) already means *wiki pages with no inbound
  links*, the opposite semantic (A3-7 vocabulary-collision note).
- **Aging-queue escalation (Q4/disposition 3):** state, mirroring `:62`, that graduation-queue
  escalation is a tripwire concern (build-17), not lint's — lint surfaces, the enforcement
  kit escalates.

**Why.** Closes A3-7's `linkage_ripe` + `revisit_after` in the surviving shape, using the
union the field evidence validated, and heals the module-caused `topic:` raggedness at lint
cadence.

**Out of scope:** `cluster_ripe`/K (deferred); ingest-time probe (disposition 2); any nagging
or auto-promotion (the read-only ledger/`review_due` posture holds).

## F5 — `vlt-lint-full.js`: scope the missing research read path honestly

**Current state** (`skills/vlt-setup/assets/workflows/vlt-lint-full.js`). The fan-out
workflow **sweeps `{wiki}` only**: `PAGE_SCAN` (`:64-82`) reads wiki pages; `{research}`
notes enter **only** as `crossLayerSlugs` — normalized basenames, never content (`:48`,
`:150`) — so a wiki→research `[[link]]` isn't false-flagged as missing. Orphans are computed
over wiki scans (`:146`). The SKILL already owns the checks outside the workflow's wiki page
set (`para_missing_attestation`, governance checks, the doctrine meta-check — `vlt-lint:43`).

**The exact change — honest scoping, no research zone this cut.** Do **not** give the
workflow a research read path. The graduation-candidacy pass (`linkage_ripe`/`revisit_due`,
and the widened `{research}` `topic:` check) is a **research read** the workflow doesn't do;
it lives in the **`vlt-lint` SKILL's own jurisdiction pass** — exactly where
`para_missing_attestation` and the governance checks already live (`vlt-lint:43`). Two honest
consequences to state in the SKILL and in this brief:
- The SKILL's research pass runs **inline** (per-note reads of `revisit_after` + `sources:` +
  frontmatter `topic:`), not fanned out. For the first cut and typical research-zone sizes
  this is fine; if it ever needs scale, "give the workflow a `{research}` zone" is the
  **named second-cut** work (recorded, not silently deferred).
- The workflow **may** surface the wiki→research inbound counts it can already derive from
  the reduced link graph (it knows every wiki page's `outbound_links` and the `crossLayer`
  set) as an input to the SKILL's union — but reading research-note **content**
  (frontmatter/sources) stays the SKILL's job. Optional optimization; not required for the
  first cut.

**Why.** The ruling requires scoping "the missing `vlt-lint-full.js` research read path
**honestly**" (`:1616`). Honest = the workflow stays wiki-only, the SKILL owns the research
pass, and the wider workflow research zone is named as second-cut work — never a capped sweep
presented as exhaustive (`vlt-lint:154`).

## Registration

**None.** A convention edit (F2) and lint/skill edits (F1, F4, F5) register nothing in the
help registry (`vlt-mint:141`: "A convention edit registers nothing in the help registry").
No new skill, no new workflow, no `module-help.csv` row. The **frontmatter convention**
version moves `3→4`, which triggers the 5-consumer walk (F3) — that walk *is* the
registration surface for this build, and its exit gate is `vlt-mint:141`.

## Out of scope (dispositioned)

- **`cluster_ripe` / K cluster-threshold** — deferred (surviving-shape ruling; disposition 1).
  Re-opens only with a future clustering build, on post-fix `topic:` data.
- **Ingest-time candidacy probe (A3-7 change; A3-8 per-source sharpening)** — deferred to the
  named second cut (disposition 2); needs the research read path F5 defers.
- **Widening the scan surface to handoffs/threads/project-status (A3-9)** — the named second
  cut; first cut is **research-zone-first** by explicit ruling (`:1662`), a recorded
  decision, not a default.
- **`revisit_when:` key** — dropped as a `revisit_after` near-homophone (disposition 4).
- **`source_type:` / `review_note:` checks** — the keys land as documented-optional slots
  (disposition 5) but get **no check** until usage evidence (091006 OQ5).
- **Shipping an Obsidian `.base`** — module ships none (`frontmatter.md:117`; 091006 OQ1
  standing ruling); graduation views are documented-reference only.
- **`module.yaml` `vault_structure`** — untouched; `{research}` zone already exists (`:47`).
- **Enforcement-kit tripwire for the aging graduation queue** — build-17 (disposition 3).

## Verification (unit, at rest — lifecycle step 5)

- **Handshake bipartite re-check (required — `version:` moved 3→4).** Grep every
  `frontmatter.md` consumer's `depends_on`; confirm all five pin `frontmatter@4` and none
  still pins `@3`; confirm `frontmatter.md:12` `consumers:` ↔ the acking skills are
  bipartite-consistent. Run the `vlt-lint` convention-coherence check's logic by hand over
  the five: zero stale/unacked/dangling for frontmatter.
- **Enforcement-doctrine self-check.** `frontmatter.md` still carries valid enforcement
  frontmatter after the adoption-facet addition (no `deferral_invalid`/`declared_untripwired`
  regression); the new optional keys carry no rule that needs a bell.
- **`topic:` agreement grep.** `vlt-research/SKILL.md` `topic:` template now matches
  `vlt-ingest/SKILL.md:84` verbatim (comment included); no scalar `topic: <subject area>`
  remains in the research template.
- **`review_after` single-home grep.** `revisit_after`'s definition **references**
  `review_after` (`frontmatter.md:115`) and does **not** restate its date semantics —
  confirm no second copy of the resolved-date/absence-evergreen rule.
- **Lint scope grep.** The `topic:`-is-list check and string→list auto-fix now name
  `{research}` alongside `{wiki}`; `linkage_ripe`/`revisit_due` report keys present and
  distinct from `orphans`; the workflow (`vlt-lint-full.js`) is **unchanged in sweep scope**
  (still `{wiki}` only) and the SKILL states the research pass is its own inline jurisdiction.
- **Workflow parse.** `node --check skills/vlt-setup/assets/workflows/vlt-lint-full.js` (only
  if F5 takes the optional inbound-count optimization; if the workflow is untouched, note "no
  workflow edit — parse N/A").
- **Packaging lint (mid-arc).** `uv run tools/package-lint.py` → A/B/C PASS (D
  `--expect-version` is the release gate, not this build).
- **Scrub.** No personal/vault-local content or live-vault artifact paths in any changed
  shipped file; worked examples (if any added) use placeholder paths (CLAUDE.md publishing
  rule).

*(No Release section — build-20 is not the arc's release build. The module `version:` bump
and tag ride the release build; this build bumps only the frontmatter **convention** version.)*

## Acceptance (live — appended to the roadmap ledger)

Rides the next ordinary vlt-core / vlt-sayari upgrade:

1. **`topic:` fix took.** A fresh `vlt-research` note on the upgraded vault writes `topic:` as
   a YAML list; no new research note carries the scalar form.
2. **Handshake holds at `@4`.** All five consumers pin `frontmatter@4`; a live `vlt-lint`
   run reports zero convention-coherence findings for frontmatter (no stale/unacked/dangling).
3. **Union projection is honest on live data.** `vlt-lint` surfaces `linkage_ripe`
   candidates on the research zone via the union (frontmatter ∪ body wikilinks ∪ shared
   sources); the false-positive rate tracks the calibrations (union ≪ naive: A3-8 ~21% vs
   ~79%, A3-9 ~23% vs ~69%) — measure on both vaults; a naive-level FP storm is a failure.
4. **`revisit_after` behaves.** A research note with a past `revisit_after` is surfaced
   (`revisit_due`), never auto-resolved or nagged; **absence = zero findings** — legacy
   research notes (92 on vlt-core, 13 on vlt-sayari) generate no noise (trivial backfill by
   construction).
5. **Fix-then-measure closes (Q2).** Post-fix `topic:` raggedness is re-measured on vlt-core
   research notes; the result feeds any future `cluster_ripe`/K decision (this build makes no
   `topic:`-clustering ruling).
6. **Honest scoping verified in the field.** `vlt-lint-full.js` still sweeps `{wiki}` only;
   the SKILL's research-candidacy pass covers `{research}`; no capped sweep is presented as
   exhaustive, and the wider-surface second cut remains named, not silently dropped.
</content>
</invoke>
