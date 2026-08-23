---
title: 'Build #B10-12 — the lint-full execution repair (the full-mode wiki sweep runs again, and can no longer lie when it does not)'
status: |
  BUILT 2026-08-23 — one commit on arc10-v0.14.0. Five files: vlt-lint-full.js (F1/F3/F4/F5/F6),
  package-lint.py (F2 _e6 + imports + docstring), test-package-lint.py (F2 case 23 + CASE_FLOOR 22→23),
  vlt-lint/references/full-scale.md (F7 refusal clause), vlt-lint/SKILL.md (F7 Step-6 pointer).
  No convention rule changed → no depends_on/version bump, no consumer re-ack (confirmed: header at
  :11 byte-intact, package-lint E5 green). No module version bump (release is a later step).

  Verification (exercised, not just grepped — the B10-2 lesson):
  - PAGE_SCAN serialized JSON.stringify length 4,100 → 3,223 (target ≤3,700; also under the 3,757
    field-proven floor). Measured by node JSON.stringify over the eval'd literal.
  - node --check vlt-lint-full.js: OK.
  - Fixture smoke run (scratchpad, stubbed agent/parallel/budget) over the real reduce/return path:
    (a) full 10/10 → findings report, no caps, no false missing; (b) partial 7/10 (2 null agent-fail
    + 1 available:false) → cap "partial sweep: scanned 7/10 pages — 2 agent-rejected [page-8, page-9],
    1 page-unreadable [page-7]; the rest were NOT checked" + orphans/near-dup suppression cap, and
    page-0 → page-9 (a REAL but unscanned page) produced NO false missing_target (leg-3 pageSlugSet
    proof); (c) 3/10 (< ceil(10/2)=5) → status:'failed', no fix_now buckets, reason + agent_failed:7 + next.
  - uv run tools/package-lint.py → A/B/C/E PASS, D SKIPPED. E6 passes over all three workflow assets.
  - uv run tools/test-package-lint.py → 23/23 green incl. new case 23 (padded BIG_SCAN → E fails,
    "schema-size budget" + "BIG_SCAN" in output).
  - Grep cross-file: scans-derived slugSet has NO remaining consumer (removed); pageSlugSet feeds
    :224 missing-targets / :274 index-prompt / :344 callout gate; header + four pins byte-intact;
    per write-verification@3 present at :121 and :173.

  Deviations (deliberate, numbered):
  1. F1 trim overshot to 3,223 (well under 3,700) — deliberate headroom (the budget is a margin
     device); no field's presence or the required[] array changed, only descriptions shrank/moved.
  2. F1/DA5 — the `created` field's SKILL-side rationale ("gates unattested_write as informational
     for pre-convention files") was TRIMMED from the schema description, not migrated to the prompt:
     it is a checks.md (SKILL) semantic, not a scanner instruction; the scanner still returns the
     created date verbatim (the prompt already asks for it). No scanner behavior lost.
  3. F1/R4 — the sources_vs_prose `:121` write-verification@3 marker was CONSERVED IN PLACE (the
     trimmed description retains "apply the prompt Gap B rule, per write-verification@3"), not
     retired: the prompt at :173 already carries the full Gap B semantics AND the marker, so :121 is
     a redundant-but-preserved marker copy. Nothing migrated or retired (F8 audit below).
  4. F7 — the full-scale.md refusal was inserted as a NEW numbered step 3 (renumbering the old apply
     step to 4) rather than folded into an existing step, so the version-skew defence reads as its
     own gate; SKILL.md Step 6 points at it (single-home preserved).
  5. package-lint E6 extractor tokenizer skips // and /* */ comments (added after a first run
     mis-parsed KIND_PANEL, whose // comments carry apostrophes) — discovery is by type:'object'
     with properties, so KIND_PANEL (not a schema) is correctly ignored.

  F8 — R4 fan-out currency audit (the ask/schema edits re-run it):
  | ask/site | convention enforced | in convRead? | marker present | verdict |
  |---|---|---|---|---|
  | pageScanPrompt :173 (unchanged text) | frontmatter@13, write-verification@3, wiki-supersession@2 | yes (all 4 read) | per frontmatter@13 rule 4 ×2, per write-verification@3, per wiki-supersession@2 | intact |
  | PAGE_SCAN.sources_vs_prose :121 (trimmed) | write-verification@3 | yes | per write-verification@3 (retained) | conserved |
  | PAGE_SCAN other fields (trimmed) | none (verbatim extraction, no rule enforcement) | n/a | n/a | no marker owed |
  | index-pass prompt :335 (pageSlugSet swap) | wiki-index@2 | yes | judged against convRead('wiki-index') | intact (enumeration source only, not a convention ask) |
  | cluster prompt :371 (unchanged) | wiki-supersession@2 | yes | per wiki-supersession@2 ×2 | intact |
  Result: no convention added/removed, every ask enforces only conventions in convRead, every
  restated instruction keeps its inline marker → no depends_on bump, no re-ack. Header @:11 byte-intact.

  Field-contingent tail (check 6, the B10-2(5) re-discharge) rides the v0.14.0 vlt-core upgrade —
  not a ship-time event.
module_code: 'vlt'
created: '2026-08-23'
derives_from:
  - 'inbox/2026-08-22-130455-lint-full-nonexecutable-and-vacuous-clean-report.md (A10-16 Defect 1 PAGE_SCAN non-executable + Defect 2 vacuous-clean silent-shortfall, incl. the folded withdrawn …-130456 content)'
  - 'inbox/2026-08-22-130456-lint-missing-target-false-positives-existing-pages.md (A10-17 missing_targets false-positive class — WITHDRAWN by author, folded into …-130455; mechanism reattributed to the :208 scans-derived slugSet)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Grouping&order build-B10-12 bullet + §Roundtable review — addendum (2026-08-22) DA4..DA8/DA11; D1 RULED option (C) — v0.14.0 = B10-6..B10-12 one cut (owner, in-session 2026-08-22); DA4 spike SETTLED (spike-b10-12-classifier-ceiling-2026-08-22.md)'
risk: 'moderate — a workflow/script + package-lint + consumer-SKILL change, no convention rule change, so NO frontmatter/convention version bump and NO consumer re-ack; risk sits in the live re-discharge, not the source. New package-lint check owes an E4/R2 fixture in the same build.'
---

# Build #B10-12 — the lint-full execution repair

## Intent

The `vlt-lint-full` fan-out sweep has been **non-executable in the field since the v0.13.0
upgrade** and — worse — rendered its own total failure as a **clean, empty, healthy-looking
report**. B10-2's tri-state descriptions pushed `PAGE_SCAN`'s serialized output schema from
3,757 to 4,100 chars, over the harness classifier's ~4,096-char ceiling, so 145/146 page
agents were rejected pre-read; the lone survivor (`INDEX_SCAN`, order-of-magnitude smaller)
carried on, and the workflow's `.filter(Boolean)` silently dropped every dead agent, leaving
`files_checked: 0`, empty buckets, and `coverage_caps: []`. The one page that did scan then
emitted six `missing_targets` false positives — every wikilink from the surviving page, because
the valid-target set is built from *surviving scans*, not the pages on disk. Three defects, one
root: a partial/total fan-out failure is invisible to the reduce, and it corrupts the surviving
scanner's own findings.

This build makes the sweep **executable again as a deliberate source change**, makes any
shortfall **loud at the reduce boundary**, and derives the valid-target space from **filesystem
truth** so a dead agent can no longer fabricate a missing-target. It is **release-blocking**:
D1 was ruled option (C) — v0.14.0 = B10-6..B10-12 in one cut, so the first (and only) 0.14 cut
contains this repair (owner, in-session 2026-08-22). The re-discharge of the FAILED B10-2(5) —
an executing, loud-degrading full sweep passing the original criteria — is this build's field
acceptance event.

**All rejected alternatives in the parent filings and the roundtable delta are settled — do not
re-litigate.** In particular: trim-only-as-terminus (rejected — the budget is the standing
device), the branch-surgery release composition D1(D) (no voice endorsed it), and re-deriving
the classifier ceiling from harness internals (the spike's binary-read section is quarantined
FLAGGED PROVENANCE — do not cite it or repeat its method; this brief rests only on the spike's
behavioral run table and the field-proven sizes).

## Brief-time dispositions

1. **Leg 1 — trim AND budget, not either/or (DA4; spike SETTLED).** ✅ **OWNER-RULED
2026-08-23 — CONFIRMED, budget value included: ≤ 3,700 serialized chars per fan-out
schema**, enforced non-enumeratively over every shipped workflow asset. The owner set this
number knowing it will gate future builds (~10% headroom under the field-proven 3,757, 396
under the measured 4,096 hard ceiling), and accepts the brief's own caveat that the budget
is a margin device, not the guarantee — leg 2's loud degrade plus the re-discharge event
are the terminating guarantee. The DA4 spike settled the
   fixed-vs-moved question empirically: the ceiling is a **fixed serialized-output-schema size
   limit**, measured **4,096 alive / 4,097 dead** in auto mode; `PAGE_SCAN` serializes to
   **4,100** (dead by 4); the field-proven 0.12.0 size was **3,757** (ran for months); the gate
   measures `JSON.stringify(schema).length`, **not** the source-literal char count. Because the
   limit is fixed, the trim gets `PAGE_SCAN` compliant *now* and the standing package-lint
   **schema-size budget** stops the next silent creep — B10-2 crossed by 180 serialized chars
   with nobody noticing. **Budget = serialized (JSON.stringify) length ≤ 3,700 per fan-out
   schema** (≈10% headroom under the 3,757 field-proven floor and 396 under the 4,096 gate),
   enforced in `package-lint` over **every** agent-schema in every shipped workflow asset
   (non-enumerative — the check iterates the schemas it finds). Measured serialized sizes at
   HEAD (grounding, `node` JSON.stringify): `PAGE_SCAN` 4,100 (**over — must drop under 3,700**),
   `INDEX_SCAN` 823, `CLUSTER_FINDINGS` 1,630, `PAIR_FINDINGS` 376, `vlt-review-council`
   VERDICT 776 / SYNTHESIS 1,035, `vlt-consult` CONSULT_RETURN 1,703 (all others already
   compliant). The budget is a **margin device, not the guarantee** — the classifier constant is
   undocumented harness-internal and the LLM classifier above it can reject for contextual
   reasons at any size. Leg 2's loud degrade plus the re-discharge event are the terminating
   guarantee.

2. **Leg 1 — trim discipline (DA5).** The blanket "descriptions near-duplicate the prompt"
   claim is **false field-by-field**: `available` (:108), `created` (:110), `frontmatter_issue`
   (:120), `thin` (:126), and the `key_claims` cap (:127) carry semantics that exist **only** in
   the schema descriptions. The trim is preceded by a **per-field duplication audit**; a
   description that merely restates the prompt is trimmed to the field name/type/enum; a
   description carrying **load-bearing schema-only semantics migrates into the `pageScanPrompt`
   text, never dropped**. `available`'s semantics are **load-bearing for leg 2** (it is the
   page-unreadable signal the reason-partition reads) — its meaning is preserved wherever it
   ends up. **R4 markers are conserved**: the `per write-verification@3` marker inside the
   `sources_vs_prose` description at **:121** moves with its semantics (the prompt at :173
   already carries `per write-verification@3`) or its migration/retirement is recorded in the R4
   audit table (F8).

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

3. **Leg 2 — near-total shortfall error threshold (DA6, brief-time question).** ✅
**OWNER-RULED 2026-08-23 — CONFIRMED at the majority floor as briefed**
(`scans.length === 0` or `scans.length < Math.ceil(pages.length / 2)` → error object, never
a findings report). The owner-adjustable value is ruled and set; both sides stay
fixture-exercised (~40% → error, ~80% → cap). A sweep that
   did not scan a **majority** of the listed pages returns an **error object, never a findings
   report**: the guard is `scans.length === 0` (the hard sub-case) **or**
   `scans.length < Math.ceil(pages.length / 2)`. Rationale: below majority coverage the
   cross-page reduce is dominated by absent pages and any "clean" bucket is far more likely
   shortfall than health — the exact field failure (0.7% coverage rendered clean). Between the
   majority floor and 100%, the **loud coverage cap + reason-partition + surviving failed slugs**
   is the honest signal, and leg 3's filesystem-truth denominators keep `missing_targets` / index
   / callout valid across the shortfall. This threshold is **owner-adjustable**; the ship-verifiable
   fixtures exercise both sides of it (a ~40%-coverage run → error, an ~80%-coverage run → cap).

4. **Leg 2 — the SKILL version-skew defence (DA6).** A **fixed** workflow can no longer emit a
   `files_checked: 0` findings report (it errors first, disposition 3). So a report arriving at
   the SKILL with `files_checked: 0` — or the error shape — means a **stale vault-local workflow
   copy**: `vlt-lint` refuses to persist it or advance/reset `lint-debt`, worded as the
   **version-skew defence**, as a **directed surface** (states the cause + the operator's next
   move: re-run after the workflow upgrade lands). The refusal floor is `files_checked: 0` (the
   hard case) plus the same majority floor.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

5. **Leg 2 — the error path leaves evidence (DA6).** The error path **persists a dated
   failed-run record** distinct from a findings report, so a refused sweep is not the silent
   no-evidence gap of 2026-08-22. It lands as `{lint_reports}/YYYY-MM-DD-HHMM-lint-failed.yaml`
   — same dir, **rides the existing dir-level Decay-contracts exemption** (contract :323), so
   **no new Decay-contracts row and no contract edit** (adding a row/list would be the
   second-home risk the contract's own :329 warns against — the dir row already exempts
   everything under it). Its shape names `status: failed`, the reason, `files_listed`,
   `files_checked`, the reason-partition counts + failed slugs, and a directed `next:` line. It
   **does not** reset the `lint-debt` counter (Step 6's reset is derived from the log line, which
   is not written on a failed run). Retry/re-scan of failed pages is **out of scope** (DA6) — the
   cap/error is the signal to re-run; a retry mechanism is its own filing.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

6. **Leg 3 — inbound-derived slots under shortfall (DA7, per-slot brief-time pick): SUPPRESS
   with a cap.** `orphans` (:212) and `near_duplicates` (:228-266) are computed from the inbound
   link map, which is only as complete as what scanned — under any shortfall a page whose only
   inbound link came from an unscanned page falsely reads as an orphan (the A10-17 class in a
   different slot). Under partial shortfall these two slots are **emitted empty and a coverage
   cap names the suppression** ("orphans / near-duplicates not computed — inbound-derived and
   coverage was incomplete"). `missing_targets`, index drift, and the callout gate switch to
   filesystem truth (F5) and stay valid. Owner-adjustable per-slot (annotate-against-cap is the
   alternative DA7 names).

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

7. **DA11 — the sibling fan-out (`vlt-review-council.js:148-152`): DECLINE the lens-shortfall
   cap, on record; file-forward.** The council fan-out already carries a zero-guard (:154 →
   degraded verdict) and a materially **different degrade contract** — a review panel's
   moderator synthesizes only the fielded positions and the run is not coverage-denominated the
   way a wiki sweep is. Its schemas (VERDICT 776, SYNTHESIS 1,035) sit far under the classifier
   ceiling, so the execution defect does not reach it. The one real parity gap — no
   *partial*-lens-shortfall signal (3 of 7 lenses silently dropped reads as a full panel) — is a
   genuine but **lower-severity honesty gap that deserves its own filing, not a rider on a
   release-blocking lint repair**. DA11's own framing is "a ruling on record, not a scope
   expansion by default"; the default posture is not to expand. **File-forward:** a new
   `inbox/` candidate for a minimal council/consult partial-shortfall cap, Arc 11.
   **FILED 2026-08-23 under the owner's batch disposition:**
   `inbox/2026-08-23-111410-council-consult-partial-lens-shortfall-is-silent.md`. Note the
   schema-size budget (disposition 1 / F2) **does** cover the council and consult schemas — the
   check is workflow-agnostic — so a future council schema crossing the ceiling is caught
   regardless of this decline.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

8. **R1 (interim posture): not applicable in the forward sense — but the standing interim field
   posture (DA3) is retired by this build's cut.** This build ships no rule/check ahead of its
   mechanism; every leg lands with its enforcement. The pre-existing interim posture — full-mode
   lint on 0.13.x is untrusted, no full-mode sweep run, unexplained-shortfall reports voided
   (roadmap DA3) — is **retired by this build's shipped cut** (v0.14.0), as DA3 states.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

## F-sites

All sites re-grounded against `skills/vlt-setup/assets/workflows/vlt-lint-full.js` at HEAD
(`arc10-v0.14.0` @ `7a4b1a8`); B10-11 re-stamped the header and added the attestation census, so
capture-time line numbers are confirmed or corrected below.

### F1 — `PAGE_SCAN` schema trim (leg 1) — `vlt-lint-full.js:102-133`

- **Current state (HOLDS):** `PAGE_SCAN` at `:102-133`; serialized `JSON.stringify` length =
  **4,100** (over the 4,096 gate → every page agent rejected in auto mode). The `:121`
  `sources_vs_prose` description carries the R4 marker `conformant per write-verification@3`.
- **Change:** run the **per-field duplication audit** (disposition 2), then trim descriptions so
  `JSON.stringify(PAGE_SCAN).length ≤ 3,700`. Trim descriptions that merely restate the
  `pageScanPrompt` (:172-174) to name/type/enum; **migrate load-bearing schema-only semantics
  into the prompt** — candidate fields per DA5: `available` (:108, its "dropped from the reduce"
  semantics are load-bearing for leg 2 — preserve), `created` (:110, the pre-adoption
  informationality gate), `frontmatter_issue` (:120), `thin` (:126), `key_claims` cap (:127).
  Keep the `required` array and every field's presence; only descriptions shrink or move.
- **R4 marker conservation:** the `:121` `per write-verification@3` marker moves with its
  semantics or its retirement is logged in the F8 audit; the prompt already restates
  `per write-verification@3` / `per frontmatter@13 rule 4` / `per wiki-supersession@2` at :173,
  so migrated semantics land beside an existing marker.
- **Why:** A10-16 Defect 1 — restore executability as a deliberate source change (never a
  runtime reshape). Verify the post-trim serialized size at rest.

### F2 — package-lint standing schema-size budget (leg 1) — `tools/package-lint.py` + `tools/test-package-lint.py`

- **Current state:** `check_group_e` (`:890-925`) aggregates `_e1`.. `_e5`; E5
  (`_e5_asset_nodes`, `:758`) already reads every `skills/vlt-setup/assets/workflows/*.js` for
  its `// depends_on:` header. No schema-size check exists. E4 (`_e4_harness_coverage`, `:847`)
  fails any inventoried check (name matching `^(check_|_e\d+_)`) that has no covering case in
  `tools/test-package-lint.py`.
- **Change:** add `_e6_schema_size_budget(root)` and aggregate it in `check_group_e`'s return
  (`:919-925`). It extracts **every** agent output-schema object literal in every workflow
  asset (`const *_SCAN = {…}` / `VERDICT` / `SYNTHESIS` / `PAIR_FINDINGS` / `CONSULT_RETURN` —
  discovered structurally by `type: 'object'`, never a hand-kept list) and FAILs any whose
  **serialized `JSON.stringify` length > 3,700**, naming the file, schema, and measured size.
  **The measure must reproduce the runtime's own `JSON.stringify(schema).length`** — the
  recommended faithful implementation is a `node` subprocess that requires/evals each literal
  and serializes it (the factory already needs `node` — the workflows are JS and F7's smoke run
  runs one); a pure-Python balanced-brace extractor is acceptable only if it reproduces the
  serialized measure exactly. Do **not** count source-literal chars (the 4,266/4,284 figures are
  the source literal; the gate sees the 4,100 serialized form).
- **E4/R2 obligation (same build):** add a covering case to `tools/test-package-lint.py`
  (`covers=("_e6_schema_size_budget", "check_group_e")`) that **can fail** — a fabricated schema
  padded over 3,700 → FAIL, a compliant one → pass — and **bump `CASE_FLOOR` 22 → 23**. Without
  this, E4 fails the release gate.
- **Why:** the budget is the standing margin device (disposition 1) so the next tri-state-style
  growth cannot silently re-cross the ceiling.

### F3 — reduce-boundary loud degrade + reason-partition (leg 2) — `vlt-lint-full.js:176-197`

- **Current state (HOLDS):** `scans` / `coverageCaps` init `:176-177`; the overlay loud-degrade
  posture to mirror at `:180-184`; the budget guard (the *only* current shortfall cap) at
  `:186-192`; the fan-out at `:194`; the **silent drop** at `:195`
  `scans.push(...part.filter(Boolean).filter((s) => s.available !== false))` (`parallel()`
  resolves a classifier-killed agent to `null` — confirmed by the spike, no catchable error).
- **Change:** replace the silent double-filter with **counted, reason-partitioned** accounting.
  `parallel()` preserves position, so `chunk[k]` names the page for `part[k]`: a `null` result
  is an **agent-failed** slug; a `part[k].available === false` result is a **page-unreadable**
  slug. Accumulate `agentFailedSlugs` and `pageUnreadableSlugs` across chunks; still push only
  live, readable scans into `scans`. After the fan-out loop, when `scans.length < pages.length`
  for any reason **other than** the budget guard already having capped, push a coverage cap
  naming the **count + reason partition + the failed slugs**, mirroring the `:180-184` overlay
  posture and the budget-guard message shape at `:188`. (E.g. `"partial sweep: scanned
  N/M pages — K agent-rejected [slug,…], J page-unreadable [slug,…]; the rest were NOT checked"`.)
- **Census honesty (:382-387):** `attestation_census.pages_total` stays `scans.length` (DA7 — the
  three-bucket partition invariant holds over what scanned); the shortfall honesty rides the new
  cap + `files_listed`, not a census rewrite. `files_checked: scans.length` (`:393`) and
  `files_listed: pages.length` (`:394`) are unchanged.
- **Why:** A10-16 Defect 2 — a dead agent must add a loud cap, never vanish.

### F4 — near-total shortfall → error, not a report (leg 2) — new guard after the fan-out (~`:198`)

- **Current state:** the only error return today is the args-guard at `:98-100`
  (`return { error: '…' }`). The reduce (`:199+`) runs unconditionally on whatever `scans` holds.
- **Change:** after the fan-out loop and before the reduce, add the disposition-3 guard:
  `if (scans.length === 0 || scans.length < Math.ceil(pages.length / 2)) return { status:
  'failed', mode: 'full', reason: '…near-total fan-out shortfall…', files_listed: pages.length,
  files_checked: scans.length, agent_failed: agentFailedSlugs, page_unreadable:
  pageUnreadableSlugs, next: '…re-run after confirming the workflow copy is current…' }` — a
  shape **distinct** from the findings report (carries `status: 'failed'`, no `fix_now`/
  `flag_for_human` buckets), mirroring the `:98-100` error convention.
- **Why:** below majority coverage a findings report cannot be honest (disposition 3); the field
  event (145/146 dead) must have produced this error, not a clean report.

### F5 — filesystem-truth valid-target space (leg 3, root cause) — `vlt-lint-full.js:208, :219-220, :269-271, :336-344`

- **Current state (with one grounding correction):**
  - `:208` `const slugSet = new Set(scans.map(nslug))` — the **scans-derived** existence set,
    the A10-17 root cause (a dead agent deletes its page from valid-target space).
  - `:219-220` `missing_targets` tests `!slugSet.has(l) && !crossLayer.has(l) && !stubs.has(l)`.
  - `:269-271` the index-pass prompt enumerates `${[...slugSet].join(', ')}` at **:270** —
    **DA7 grounding correction confirmed at HEAD**: `:270` is the **index-pass** slug
    enumeration; the cluster pass (`:279-291`) iterates `scans`/`nslug(s)` directly and never
    touches `slugSet`.
  - `:336-344` the callout-seed gate at **:340** `if (!target || !slugSet.has(target) ||
    target === nslug(s)) continue`. **Grounding correction:** the roadmap DA7 note says `:341`;
    at HEAD the gate is at **:340** (trivial off-by-one; substance unchanged — a roadmap
    superseding note is appended, F-audit below).
- **Change:** introduce `const pageSlugSet = new Set(pages.map((p) => normalizeTarget(p.slug)))`
  — the **filesystem-truth** page set (every page that exists on disk, whether or not its agent
  scan survived) — and point the three **switch-to-filesystem-truth** consumers at it:
  `:220` missing-targets, `:270` index-prompt enumeration, `:340` callout gate. The
  scans-derived `slugSet` at `:208` then has **no remaining consumer** (orphans/near-dup/cluster
  use `inbound`/`nslug`/`outbound_links`, not `slugSet`) → **remove it as dead code** (confirm by
  grep during the build). Per DA7's stay-scans-denominated partition, `files_checked` (:393),
  the census (:383), and the inbound-derived slots (F6) remain scans-denominated.
- **Why:** A10-17 at its root — a wikilink to a real page that merely failed to scan is no
  longer a fabricated missing-target; post-fix a flagged existing page is a genuine relocation
  finding, never a shortfall artifact (this is the DA9 disambiguation rule the re-discharge
  reads against).

### F6 — inbound-derived slots suppressed under shortfall (leg 3, DA7) — `vlt-lint-full.js:212, :228-266, :438-440`

- **Current state (HOLDS):** `orphans` `:212` (from `inbound`); `near_duplicates` computed
  `:228-266`, emitted at `:438-440` under `opportunities`.
- **Change:** when `scans.length < pages.length` (any partial shortfall), **suppress** both:
  emit `orphans: []` and `near_duplicates: []` and push a coverage cap naming the suppression
  (disposition 6). Guard the computation or the emission — either is fine; the invariant is that
  neither slot carries inbound-derived findings computed over an incomplete graph.
- **Why:** a false orphan under shortfall is the A10-17 class in another slot; suppress-with-cap
  is the honest posture (disposition 6).

### F7 — `vlt-lint` SKILL: refusal + failed-run record (leg 2 consumer defence) — `skills/vlt-lint/references/full-scale.md:8-9` + `skills/vlt-lint/SKILL.md:72`

- **Current state (HOLDS):** `full-scale.md` step 2/3 invokes the workflow and instructs
  honoring `coverage_caps`; nothing handles an **error shape** or `files_checked: 0`. `SKILL.md`
  Step 6 (`:72`) persists the Step-5 report verbatim to
  `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` and the log line is "by derivation the `lint-debt`
  counter reset."
- **Change:**
  - `full-scale.md` gains a clause: if the workflow returns `status: 'failed'` (F4) **or** a
    findings report with `files_checked: 0`, **do not** apply fixes, **do not** persist a
    findings report, and **do not** write the Step-6 log line (so `lint-debt` does not reset).
    Instead write a **failed-run record** `{lint_reports}/YYYY-MM-DD-HHMM-lint-failed.yaml`
    (disposition 5 shape) and surface a **directed refusal** — cause (near-total shortfall /
    likely stale vault-local workflow copy — the **version-skew defence**, disposition 4) + the
    operator's next move.
  - `SKILL.md` Step 6 gains the one-line guard pointer (single-home the mechanics in
    `full-scale.md`; Step 6 points at it): a failed full-mode run persists the failed-run record
    and writes **no** counter-resetting log line.
- **Single-home / contract:** the failed-run record rides the existing `{lint_reports}`
  dir-level Decay exemption (contract `:323`) — **no contract edit, no new Decay row, no
  rule-card re-derive** (disposition 5). Legacy `.yaml`/`.md` lint reports stay legal.
- **Why:** DA6 — the error path leaves evidence and the consumer refuses a shortfall report; the
  B10-2(5) no-evidence gap does not recur.

### F8 — R4 fan-out currency audit (leg-wide) — `vlt-lint-full.js:11-21` header + `full-scale.md:8`

- **Current state (HOLDS):** the `// depends_on: ["frontmatter@13", "wiki-supersession@2",
  "wiki-index@2", "write-verification@3"]` header at `:11`; the R4 note at `:16-21`; `convRead`
  reads exactly these four conventions.
- **Change:** none to the read-list or pins — **no convention is added or removed, no rule text
  changes**, so **no `depends_on` bump and no consumer re-ack**. But legs 1 and 3 edit **asks**
  (the `PAGE_SCAN` schema shape and the index-pass prompt), which per R4 (`:16-21`) **re-runs
  the fan-out audit**: verify every ask in the file still enforces only conventions in `convRead`
  and every restated convention instruction still carries its inline `per <convention>@N` marker
  (the `:121` and `:173` markers — F1). **Record the audit table in the BUILT `status:`** (R4's
  run is evidenced there, per the B10-2 precedent).
- **Why:** R4 standing rule — any ask/schema edit re-runs the audit; markers conserved.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row, no `marketplace.json` entry.
No convention **rule** changed, so no `version:` bump and no consumer walk. **"No bump owed" is
not "no cost"** — this build touches:
- **package-lint E4 / R2** — F2 adds `_e6_schema_size_budget`, which owes a covering, failable
  case in `tools/test-package-lint.py` **in the same build** + `CASE_FLOOR` 22→23, or the
  release gate blocks.
- **package-lint E5** — the workflow header at `:11` is unchanged, so E5 stays green; the F1/F5
  edits do not touch the `// depends_on:` line (verify it survives the edits intact).
- **package-lint C6** — **not touched**: no edit to `vault-operating-contract.md` (F7's
  failed-run record rides the existing `{lint_reports}` exemption), so **no rule-card
  re-derive**.

## Out of scope (dispositioned)

- **`vlt-review-council.js:148-152` partial-lens-shortfall cap (DA11)** — **declined for this
  build, on record** (disposition 7); file-forward as an Arc 11 `inbox/` candidate. The
  schema-size budget (F2) still covers council + consult schemas.
- **Retry / re-scan of failed pages (DA6)** — deliberately out of scope; the cap/error is the
  re-run signal; a retry mechanism is its own filing.
- **A `{research}`-zone fan-out** — already named second-cut work in `full-scale.md:9`;
  untouched.
- **The follow-up "did a prior release ship a vacuous full-lint report" audit** — **DISCHARGED
  at capture** (roadmap DA10): the 2026-08-14/-16 exposure-window reports verified genuine; no
  audit obligation carries into this build.
- **The classifier-limit "platform constraints" dependency-record row (Carson OOS #2)** —
  B10-8's `module.yaml` dependency record has no harness-schema-limit row class; noted, not
  built here (Arc 11 candidate).
- **Harness-internal re-derivation of the 4,096 constant** — forbidden; the quarantined spike
  section is not cited and its method is not repeated.

## Verification (unit, at rest — lifecycle step 5)

- **Executable smoke run (mandatory — the B10-2 lesson).** B10-2's checks (1)-(4) were
  discharged "at rest" while the workflow was in fact non-executable — greps passed over a file
  the harness rejected. So at-rest verification here **must actually exercise the workflow**, not
  only grep it: `node --check vlt-lint-full.js`, **plus** a real fixture run of the reduce/return
  path against a temp fixture page set with a stubbed `agent`/`parallel` (or a headless run)
  covering: (a) a full/complete run → findings report, correct buckets; (b) an injected partial
  failure (some `null`, some `available:false`) → the reason-partitioned cap with counts +
  slugs, `missing_targets` computed against `pageSlugSet` (no false missing for a
  surviving-but-unscanned real page), `orphans`/`near_duplicates` suppressed with their cap;
  (c) a below-majority run → the `status:'failed'` error shape, no findings buckets.
- **Serialized schema-size assertion.** After the F1 trim, confirm
  `JSON.stringify(PAGE_SCAN).length ≤ 3,700` (grounding target: 4,100 → under 3,700); run the new
  package-lint `_e6` check and confirm it passes over all workflow schemas and **fails** on a
  padded fixture schema.
- **Grep for cross-file agreement:** `slugSet` has no remaining consumer after F5 (removed);
  `pageSlugSet` feeds `:220`/`:270`/`:340`; the `:11` header and its four pins are byte-intact;
  the `per write-verification@3` marker is present wherever the `sources_vs_prose` semantics
  landed.
- **Handshake bipartite re-check — `package-lint` Group E** (the check of record; not a
  hand-written grep). No `version:`/`consumers:`/structure-map change, so E1/E2/E3/E5 stay green;
  E4 must go green **only after** the F2 fixture + `CASE_FLOOR` bump land. Run the mid-arc
  `package-lint.py` **A/B/C/E** pass (D/`--expect-version` is the release gate).
- **Fixture extension (R2):** F2's `_e6` check + its covering case + `CASE_FLOOR` bump — same
  build (named under Registration).
- **Legal response (R3):** F3 adds the reason-partitioned shortfall cap and F4 the failed-run
  error class; their legal responses home at their single sites — the cap in the workflow's
  reduce (surfaced by `full-scale.md`'s honor-coverage_caps clause) and the failed-run refusal
  in `full-scale.md`/`SKILL.md` Step 6 (F7). Stated in the same build.
- **Enumeration widening (R4):** the fan-out currency audit (F8) is R4's run for the ask/schema
  edits — recorded in the BUILT status; **no convention added** so no ack widening. The
  failed-run record is a new `{lint_reports}` artifact but rides the dir-level exemption (not a
  live-read enumeration) — declared, not silently omitted.
- **Scrub:** no personal / vault-local content in any changed shipped file (worked
  examples/paths stay placeholder).

## Acceptance (live — appended to the roadmap ledger)

**Ship-verifiable (gate — DA8):**

1. **`[ship-verifiable]`** — **partial-failure fixture**: an injected partial agent failure
   (some `null`, some `available:false`) makes the workflow emit a coverage cap naming
   **count + reason-partition + the failed slugs**, the findings report shape is intact, and
   `missing_targets` computed against the filesystem-truth `pageSlugSet` carries **no** false
   missing for a surviving-but-unscanned real page; `orphans`/`near_duplicates` suppressed with
   their cap. Discharged by the F7-verification fixture smoke run at rest.
2. **`[ship-verifiable]`** — **near-total-shortfall fixture**: a below-majority run
   (`scans.length < ceil(pages.length/2)`, and the `scans.length === 0` sub-case) returns the
   `status:'failed'` error shape, **never** a findings report. Discharged at rest by fixture.
3. **`[ship-verifiable]`** — **SKILL refusal**: a `files_checked: 0` (stale-workflow) report is
   refused by `vlt-lint` — not persisted as findings, `lint-debt` not reset, a dated
   `…-lint-failed.yaml` record written, a directed version-skew refusal surfaced. Discharged by
   the workflow error-path fixture (executable half) + a grep that `full-scale.md`/`SKILL.md`
   carry the guard (prose half) — the two halves named explicitly per the B10-2 lesson (no
   at-rest claim of executability for the prose surface).
4. **`[ship-verifiable]`** — **schema-size budget**: package-lint's `_e6` asserts every shipped
   workflow fan-out schema serializes ≤ 3,700; `PAGE_SCAN` post-trim is under 3,700; the check
   has a **failable** covering case in `tools/test-package-lint.py` (E4/R2) with `CASE_FLOOR`
   bumped. Discharged at the release gate.
5. **`[ship-verifiable]`** — **executability proof**: `node --check` + a real fixture run of
   `vlt-lint-full.js` execute end-to-end (the B10-2 non-executability class cannot recur
   undetected). Discharged at rest by the smoke run.

**Field-contingent (DA8 — the narrowed event):**

6. **`[field-contingent]`** — **the B10-2(5) re-discharge**: an **executing full-mode sweep**
   (`files_checked ≈ files_listed`), **degrading loudly if it degrades at all**, passing
   B10-2(5)'s original criteria **as amended by DA9** — `sources_vs_prose_mismatches` has no
   no-prose-only false page; `missing_targets` has no valid `_agent/handoffs/`/`areas/`/
   `projects/` (post-B10-11 zone map) link **and no target that exists on disk as a wiki page**
   (the fabricated-by-partial-sweep class, now falsifiable via leg 3); no new false-positive
   class. **Event:** the owner's first full-mode (>30 pages) `vlt-lint` sweep on **vlt-core**
   after the **v0.14.0 upgrade** (performer: the owner; vault: vlt-core; evidence: the persisted
   `{lint_reports}` `.yaml`). This one run carries **three ledger consequences** (DA9): it
   discharges B10-2(5), is B10-12's field-acceptance event, and sizes-or-collapses the residual
   `normalizeTarget` seam — record the single run against both the B10-2 and B10-12 ledger
   entries. **E6's attestation-census checks are re-verified at rest on the post-B10-12 file**
   (DA7) as part of check 1's fixture, not a separate field event.

## Next lifecycle move

A **fresh builder session** implements this brief via `bmad-workflow-builder`. Exit obligations:
rewrite this `status:` to a BUILT record with numbered deviations **and the F8 R4 audit table**;
delete any `.decision-log.md`; **one commit** for the build on `arc10-v0.14.0`. Then — B10-12
being the last build before the cut (D1 option C) — the owner runs the v0.14.0 release
choreography (`vlt-release`) and the vlt-core upgrade discharges the ledger tail.
