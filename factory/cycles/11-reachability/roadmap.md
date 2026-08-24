---
title: 'Cycle 11 — reachability'
status: 'open — captured 2026-08-24, awaiting ideation (scaffold + owner rulings + roundtable)'
module_code: 'vlt'
created: '2026-08-24'
updated: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-22-150000-spec-candidate-relay-leg-fires-on-ordinary-round-trips.md'
  - 'factory/inbox/2026-08-23-110913-amendment-trigger-should-not-be-a-personal-handle.md'
  - 'factory/inbox/2026-08-23-111410-council-consult-partial-lens-shortfall-is-silent.md'
  - 'factory/inbox/2026-08-23-180100-rule-shelved-as-trailing-clause-is-unreachable-by-subject.md'
  - 'factory/inbox/2026-08-23-180200-migrations-amend-the-base-but-walk-no-vault-local-overlay.md'
  - 'factory/inbox/2026-08-23-190200-undeclared-para-type-is-invisible-to-both-nets.md'
  - 'factory/inbox/2026-08-23-210653-instrument-rule-for-byte-exact-comparisons.md'
  - 'factory/inbox/2026-08-24-085505-vlt-upgrade-names-a-real-install-on-shipped-surface.md'
  - 'factory/inbox/2026-08-24-142822-extraction-retirement-reads-as-general-closure-of-resources.md'
  - 'factory/inbox/2026-08-24-142828-resources-outside-wiki-write-posture-unruled.md'
  - 'factory/inbox/2026-08-24-102813-full-lint-cost-scales-with-corpus-not-with-change.md'
predecessor: 'factory/cycles/10-signal-integrity/roadmap.md (Cycle 10 — CLOSED 2026-08-23, builds B10-1..B10-12 shipped v0.13.0 + v0.14.0)'
intent: >
  Capture the gap between the module's declared surface and its effective one: rules that
  exist but cannot be found by subject, checks whose populations are quietly incomplete,
  metrics the shipped vocabulary cannot express, triggers that fire on the wrong signal,
  panels that read full while lenses dropped, instruments named but not actually run, and
  names sitting on surfaces that must be recipient-agnostic. Every filing here is a case
  where the machinery behaved as written and the written thing still failed to reach.
---

# Cycle 11 — reachability

## The through-line

Cycle 10 fixed checks that *lied* (a full sweep that never executed, a wrapper that said
"identical"). This cycle's signal is one step subtler: things that are **declared but not
effective**. A standing rule exists — as a trailing clause under someone else's `ref:`,
where no read path can reach it (A11-4). A check exists — but its trigger counts traffic
instead of revision (A11-1), or its two nets each correctly decline the same file and sum
to zero coverage (A11-6), or its predicate omits three whole populations (A10-18). A
metric is wanted — and the shipped kinds cannot express it (A10-19). A panel returns —
reading as complete while three of seven lenses silently dropped (A11-3). An overlay
survives byte-intact — while a migration silently moves the territory its rules name
(A11-5). A record says "verified with sha hashing" — while a wrapper actually ran
(A11-7). And two names sit on surfaces whose contract is to name nobody: a personal
GitHub handle as a shipped trigger (A11-2), a real install's name in shipped provenance
(A11-8). The decision-log holds (A10-12/A10-13) and the wiki-index rule-vs-example
contradiction (A10-10) are the same family: a route or a legal value that ought to exist
and doesn't, so correct behavior has nowhere legal to land.

The cycle's question, per filing: **what would make the declared thing effectively
reachable — by the reader, the check, the trigger, or the record — and who detects it
when it isn't?**

*Extended by the second 2026-08-24 capture run (A11-9..A11-11):* three more filings land
squarely in the same class. A write to `resources/<not-wiki>/` falls **between** the hard
rule's grant and its prohibition — neither clause reaches it, so a careful partner cannot
answer a legality question from the bundle at all (A11-10). A retirement sentence whose
scope is technically correct **does not carry that scope to a careful reader** — the
prose reached the partner, the rule's boundary didn't, and a legal relocation died on it
(A11-9). And the full-lint sweep pays whole-file price for rule *slices* because **the
addressable unit of a convention is the file and nothing smaller** — the rule a scanner
needs is declared but unreachable at the granularity that needs it, and the resulting
cost curve is on a path to convert expense into refusal (A11-11). A11-9/A11-10 are, with
A11-5, the third and second symptoms of one root: the 0.14.0 wiki relocation turned
`resources/` into a mixed zone and no rule, prose, or overlay walk was revisited as a set.

## Carried in from Cycle 10 (re-listed from the authoritative closeout hand-off)

Per `factory/cycles/10-signal-integrity/roadmap.md`, *Carried forward past Arc 10*:

1. **B10-2(5)/B10-12(6) — BOUND inherited debt (GATES this cycle's closeout).**
   Ship-verifiable-re-check-tagged (owner-ruled at A10-18; the A4-4(5)/B8-2(4)
   mechanism). Discharging event: an executing full sweep whose missing-target flags
   survive verification (or a measured zero) after the A10-18 build lands the
   predicate's three missing populations (`sources/`, `{index}`, non-`.md` linkables) at
   `skills/vlt-lint/references/full-scale.md:7`. Criteria as amended by DA9.
2. **B10-4(4) — BLOCKED (unreachable) carry, explicitly not a watch** (owner-ruled at
   A10-19). Unblocks when this cycle rules A10-19. Parts 2 and 3 ride the same carry.
3. **Released standing watches:** B10-7(4), B10-8(4), B10-8(5), B10-9(3) remainder —
   as recorded in the Cycle 10 closeout; not re-decided here.
4. **DECLINE+WATCH pair, unchanged:** confidentiality-as-container-attribute (Maya's
   dissent preserved) and propagation-debt.
5. **Held captures awaiting this cycle's ideation** (grounded in Cycle 10's roadmap —
   grounding not repeated here; ids keep their capture cycle):
   - **A10-10** — #4 wiki-index row-format rule contradicts its own worked example.
   - **A10-12 + A10-13** — #6 + #7 decision-log pair (writer roster admits no discovery
     site; `kind:` has no value for a scoped deviation) — Cycle 10 sketched them as one
     build.
   - **A10-15 C3** — voice-rule single-homing.
   - **A10-18** — crossLayerSlugs missing populations (the carry-1 build; the gate
     above discharges on it).
   - **A10-19** — `local_metrics:` expressiveness (the carry-2 unlock; content
     predicate / fourth kind / canonical entry is the ruling owed).
6. **Inherited registers, re-carried not re-decided:** C6-c, B5-3..B5-9, the pre-Arc-5
   and Arc-7 registers, Arc 9's item-6 standing watches (authoritative in the Arc 9
   archive's Closeout record).

## Capture — 11 filings (8 + 3 across two 2026-08-24 runs, grounded against module source 2026-08-24)

### A11-1. Spec-candidate relay leg fires on ordinary round trips (2026-08-22) — 2026-08-22-150000-spec-candidate-relay-leg-fires-on-ordinary-round-trips.md

**CONFIRMED / GAP CONFIRMED.** The leg lives at `skills/vlt-lint/references/checks.md:48`
(the filing cited `:47` — moved by one line): a handoff doc with "**≥2 `relay:` entries in
`_agent/dispatch.md` and its `{archive}`-mirrored sibling pointing at the same path**"
flags `spec_candidate`. The filing's structural point holds exactly: a single ask→answer
round trip produces two relay entries, so the trigger counts *traffic*, not *revision* —
the false-fire rate scales with ordinary usage (field-measured 6 of 8 fires on the
2026-08-22 vlt-core scoped lint were single round trips).

- **Retained postures the retune must honor, all live at `:48`:** records-never-reports
  derivation, no stored counter, decline exclusion, relay-entries-only (consult blocks
  never increment), drained-history counts, the repeat partition, never-auto-promote.
- **Consumer sites restating the signal's example vocabulary** — a retune sweeps these or
  strands them: `skills/vlt-lint/references/report.md:59` ("signal 2 relay entries") and
  `skills/vlt-lint/references/fix-and-file.md:50` ("e.g. 2 relay entries").
- **Candidate directions (carried verbatim, unresolved):** count relay entries past the
  first delivery (amendments), or require the second entry to be a `deliver`-kind
  revisiting the same artifact; or keep the count but require co-occurrence with the
  dated-revision-record signal (the both-signals case the field wearer trusted).
- **Acceptance linkage:** rides B10-3(3)'s open tail — run 1 (2026-08-22) recorded
  conformant; whichever build takes this re-states the leg and the next two-run
  observation window sizes the false-fire collapse.

### A11-2. Amendment trigger is a personal handle (2026-08-23) — 2026-08-23-110913-amendment-trigger-should-not-be-a-personal-handle.md

**CONFIRMED, with one grounding correction: three instances, not two.** The literal
"@mention @mggower" trigger sentence ships identically in **all three** issue templates —
`.github/ISSUE_TEMPLATE/field-pattern.yml:17`, `field-candidate.yml:17`, **and
`field-defect.yml:17`** (the filing named only the first two). Not a defect — B10-7
disposition 7 ruled it keep-literal for v0.14.0 with this filing as the named follow-up;
the candidate replaces the *trigger mechanism* (repo-level watch/subscription or a
repo-owned mention target) so no personal name sits in public shipped text.

- **Bounded exposure confirmed:** `.github/` is tracked and public but outside the
  own-the-apply copy surface (CLAUDE.md, Git & publishing) — the handle never lands
  inside an installed vault.
- **Preserved constraints (carried):** the trigger must remain real, not prose (a
  replacement ships only if the notification demonstrably fires — that is the acceptance
  evidence); admission stays owner-gated via `amended`; decide the `rail_contract` bump
  question at brief time (label set is additive without a bump, but the amendment
  instruction's *meaning* changes).
- **Open questions (carried verbatim):** (1) does a repository watch actually notify on
  comments to issues the maintainer has not participated in? — **an external unknown:
  per lifecycle step 3 this gets a spike before the brief** (verify against GitHub's
  current notification semantics, not memory; register it per P-2's spike register when
  that lands). (2) Is there a filer-grantable "please look" label, or is the permission
  model owner-only? (3) Does the same person-name residue exist elsewhere on shipped
  surface? (Partially answered by A11-8's grep: the only shipped-surface *install* name
  is the `vlt-core` instance; a person-name sweep is still worth the one grep at brief
  time.)
- **Cross-filing:** with A11-8, the "no names on recipient-facing surfaces" pair.

### A11-3. Council partial lens-shortfall is silent (2026-08-23) — 2026-08-23-111410-council-consult-partial-lens-shortfall-is-silent.md

**CONFIRMED for the council; the consult parity check is discharged at grounding — no
build needed there.** The double silent filter is exactly as filed at
`skills/vlt-setup/assets/workflows/vlt-review-council.js:148-152`
(`.filter(Boolean).filter((p) => p.available !== false)`); the zero case is loudly
guarded at `:154` (degraded verdict + `log()`); the partial case carries no denominator,
no named missing lenses, nothing in the synthesis output — 4 of 7 reads as a full panel.

- **Grounding resolution on the consult sibling:** `vlt-consult.js` has **no fan-out at
  all** — one agent per consult (`:155`), and both degrade paths are loud, attributed
  returns (`!result` → `degraded: true, returnType: 'needs-human'` with a nothing-was-
  invented note; `available === false` → the degraded note at `:168-180`). The
  silent-partial shape structurally cannot occur there. The filing's requested audit is
  answered NO at capture; the build scope is the council only.
- **Preserved severity reasoning (carried from DA11/B10-12 disp. 7):** the council's
  degrade contract genuinely differs from a coverage-denominated sweep; the execution
  defect does not reach it (VERDICT 776 / SYNTHESIS 1,035 serialized, far under the
  4,096 ceiling); the standing ≤3,700 schema-size budget already covers these schemas.
  Residual gap: honesty-under-partial-shortfall only.
- **The candidate (carried):** a minimal shortfall signal on the council return — lenses
  selected vs fielded, the missing lenses named (died vs `available: false` where
  distinguishable), surfaced in the moderator's synthesis output, **no error threshold**
  (a partial panel may be legitimate; the ask is that it says so).
- **Open questions (carried verbatim):** does the moderator prompt need to know (so
  synthesis language hedges), or is a return-level field enough? Is `available: false`
  worth partitioning from a dead agent? Does anything downstream consume the council
  return positionally such that a new key disturbs it?

### A11-4. A rule shelved as a trailing clause is unreachable by subject (2026-08-23) — 2026-08-23-180100-rule-shelved-as-trailing-clause-is-unreachable-by-subject.md

**GAP CONFIRMED.** The decision-log convention
(`skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md`) requires `ref:`
naming **the** governed object on every new entry (`:40`, `:47` — "findable by subject")
and every read side keys on it: `vlt-lint`'s read-before-flag matches governance findings
by `ref:` against live entries (`:85`, `:95`), and the upgrade-time reconcile resolves by
governed object. But **nothing constrains an entry's prose to its `ref:` subject** — no
"one entry, one governed subject" discipline exists, and no lint class flags an entry
whose body states a rule about a surface absent from its `ref:`. The filing's structural
claim verifies: the better the ref-keyed read discipline gets, the more invisible an
off-subject trailing clause becomes — every reader that matters resolves by subject.

- **Precedent for the cheap fix's posture:** the verdict-provenance rule v2 is
  write-side, enforced by the ceremonies that write gated entries (`:99`) — a
  subject-coherence rule ("a rule about another subject gets its own entry or its own
  home") rides the same write-time posture and matches declare-at-birth.
- **Candidate directions (carried verbatim):** the write-time discipline rule (cheaper,
  recitable), or a lint heuristic over entries whose body names a governed surface
  absent from their `ref:` (dearer, semantic).
- **Note for ideation:** a convention **rule change** to `decision-log.md` bumps
  `version:` and re-acks consumers in the same build (the version-handshake).
- **Cross-filing:** with A10-12/A10-13 (no discovery route into the log; no legal
  `kind:` value) this is a natural decision-log grouping — three reachability gaps on
  the same convention.

### A11-5. Migrations amend the base but walk no vault-local overlay (2026-08-23) — 2026-08-23-180200-migrations-amend-the-base-but-walk-no-vault-local-overlay.md

**GAP CONFIRMED.** The durability posture protects overlay *bytes* everywhere: Step 1
snapshots overlays as "durable — must never be lost" (`skills/vlt-upgrade/SKILL.md:35`),
own-the-apply never overwrites an `{overlays}/*.overlay.md` (`:49`), Step 3 confirms
overlays intact (`:69`). But the standing **relocation-migration discipline** (`:75` —
"applies to every migration below that moves a file") carries exactly two clauses:
(a) never touch parallel-worktree copies / stub the old path, (b) re-point open dispatch
pointers. **No clause visits overlays whose rules are stated in terms of a moved path** —
a migration that changes what a path resolves to has no obligation to grep `{overlays}/`,
which is precisely how the 0.14.0 wiki relocation carried `{wiki}` out of vlt-core's
`frontmatter.overlay.md` §A scope with no ruling and no report.

- **Natural site, matching the filing's cheapest direction:** a clause (c) on the
  standing discipline at `:75` — any migration changing path resolution greps
  `{overlays}/` for the affected path/key and surfaces hits as a human-gated review
  bullet (**report, never auto-edit** — overlays are vault-owned; the same
  never-write-into-the-agent-zone posture as `:49`).
- **Candidate directions (carried verbatim):** the authoring rule above; or a lint class
  (overlay section naming a path whose resolution changed since `last_updated` — needs a
  resolution history, harder to state honestly); plus the drafting recommendation
  (predicate-over-territory phrasing at overlay-mint time — shrinks exposure, doesn't
  close the walk gap).

### A11-6. An undeclared PARA `type:` is invisible to both nets (2026-08-23) — 2026-08-23-190200-undeclared-para-type-is-invisible-to-both-nets.md

**GAP CONFIRMED, with one sharpening.** Both declines verify as individually correct:
`para_status_unknown` (`skills/vlt-lint/references/checks.md:17`) keys on the per-type
`status:` enums — `type: note` is no PARA artifact type, so no enum exists to be outside
of; `para_missing_attestation` (`:16`) keys on `author: agent|hybrid` — **not
`human|agent|hybrid` as filed** (bare human files are out of jurisdiction by
`write-verification.md`'s scope rule; the correction changes nothing material, since
`author: creative` is off-vocabulary either way). A file carrying *almost* the vocabulary
lands in neither world, and only executor judgment surfaced the live instance.

- **The declare-at-birth escape already exists for *declared* vocabulary** — `:17`'s
  legal response routes vault-grown vocabulary into `{overlays}/extraction.overlay.md`.
  The gap is specifically **undeclared** vocabulary landing silent; a closing net
  (`para_type_unknown` / `para_author_unknown`) is the R3 pattern: a legal response
  stated, loud rather than silent.
- **Candidate directions (carried verbatim):** the closing net; or widen the vocabulary
  deliberately — rule whether partner names are legal `author:` values (the nets could
  map them to `agent`) and whether non-artifact types are legal residents of container
  folders.
- **Cross-filing:** with A11-3 and A10-18 — coverage shortfalls rendered as clean
  results, the cycle's core class.

### A11-7. An instrument rule for byte-exact comparisons (2026-08-23, issue #8) — 2026-08-23-210653-instrument-rule-for-byte-exact-comparisons.md

**GAP CONFIRMED — an absence, as the filing's provenance guess predicted and the owner's
2026-08-23 triage comment already verified; re-confirmed at capture.** No shipped
convention's declared scope covers instrument selection. Of the three sites whose verdict
*is* a byte comparison: `vlt-upgrade`'s base-vs-baseline divergence
(`skills/vlt-upgrade/SKILL.md:37`) and `vlt-lint`'s `convention_base_divergence`
(`skills/vlt-lint/references/checks.md:42`) name **no instrument**; the skill-asset
manifest walk (`SKILL.md:38`) **does** specify its instrument (`verify-skill-manifest.py`,
in-process hashing) — so only the rule's second half (confirm the instrument *actually
ran* unwrapped — "a record of the instrument named is not a record of the instrument
run") applies there. Natural home confirmed: the operating contract's *Honest reporting*
(`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:341`), which
already carries the general form this instantiates. The operating contract is
deliberately NOT handshaked — single-home + pointers from the two consumer sites.

- **Both halves retained:** (1) an act whose verdict is a byte-exact comparison uses an
  **unwrapped** instrument (property named, not a tool — a future wrapper inherits the
  rule); (2) it confirms the instrument actually ran unwrapped and names it in the
  record.
- **Second field instance (issue #8 comment 2026-08-23T21:55:12Z, carried in the filing
  verbatim):** a wrapped `find -newermt` scoping query returned all 147 wiki pages where
  `os.stat` put the true count at 0/0/2/4 — same wrapper class, different verb, and
  **outside the byte-exact trigger as drafted**. Open design question for ideation, not
  resolved here: should the trigger be "any instrument whose output a verdict rests on"
  rather than "byte-exact verdicts"?
- **Acceptance shape (from the payload):** reproduces only in a vault whose shell
  installs a command-rewriting hook; other vaults can verify only that the rule reads
  sensibly — tag accordingly at brief time.

### A11-8. `vlt-upgrade` names a real install on shipped surface (2026-08-24) — 2026-08-24-085505-vlt-upgrade-names-a-real-install-on-shipped-surface.md

**CONFIRMED — exactly one shipped-surface instance, as filed.** The capture-time
verification grep the filing requested (`grep -rn 'vlt-core' skills/ .claude-plugin/`)
returns precisely one hit: `skills/vlt-upgrade/SKILL.md:89` — Step 3 item 7's "First two
instances of this rule" note, instance (a): *"the `vlt-core` firewall ruling that should
have superseded the decision log"*. Shipped into every vault by the own-the-apply copy;
owner-ruled a defect 2026-08-24 (a shipped skill must be recipient-agnostic).

- **Fix direction confirmed viable:** genericize the one line (e.g. "a field vault's
  firewall ruling…") — the instance's teaching content (ruling recorded in the ledger
  alone; superseding log entry written when next reconciled) is vault-agnostic already;
  only the name does no work. **No `version:` bump:** the site is `vlt-upgrade` SKILL
  prose, not a handshaked convention, and the rule itself doesn't change.
- **Scope guard (carried):** this filing covers only the shipped-surface instance; the
  ~179 factory-record files naming vlt-core stay under the publish-as-is posture
  (names no path — the vlt-sayari precedent).
- **Cross-filing:** with A11-2, the "no names on recipient-facing surfaces" pair — but
  note the surfaces differ (own-the-apply copy vs repo-side `.github/`), so they need
  not share a build.

### A11-9. extraction.md's retirement sentence reads as a general closure of `resources/` (2026-08-24, issue #10) — 2026-08-24-142822-extraction-retirement-reads-as-general-closure-of-resources.md

**CONFIRMED — editorial defect, exactly as filed.** The sentence is verbatim at
`skills/vlt-setup/assets/governance/_meta/conventions/extraction.md:81`: it retires
`resources/` "as an extraction target", then in the same breath states where reference
material "goes now" — without ever scoping the retirement to extraction artifacts, so
the general-closure misread is genuinely available. Field trace verified plausible
against the sibling gap (A11-10): no shipped rule governed the blocked `type: research`
write either way, so citing `:81` as a hard blocker was a misread the prose invited.

- **Fix is prose-only, and the filing's own scoping note verifies:** `extraction.md`
  carries `version: 5`, `consumers: [vlt-extract, vlt-lint, vlt-track]` (`:11-12`); per
  the standing handshake rule a prose clarification that changes no rule bumps nothing
  and re-acks nobody. The fix scopes the retirement explicitly to extraction artifacts
  and, for "what else may live at that root", **points at** the A11-10 ruling rather
  than answering — the two must not fork the answer.
- **Acceptance shape (from the payload):** a read test — a partner reading the amended
  sentence cold can answer "may a non-extraction artifact live at the `resources/`
  root?" is *not answered here*; only that the sentence stops implying one.
  Ship-verifiable as a read check.
- **Cross-filing:** third symptom of the 0.14.0 wiki-relocation root, with A11-5
  (migration walked no overlay) and A11-10 (the contract's own gap). Sequencing: this
  edit naturally lands **with or after** A11-10's ruling, since its best form cites it.

### A11-10. `resources/` outside `{wiki}` is neither granted nor prohibited — ruling wanted (2026-08-24, issue #11) — 2026-08-24-142828-resources-outside-wiki-write-posture-unruled.md

**GAP CONFIRMED — the composition holds exactly as filed.** All three cited sites verify
at the module source
(`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`): `:66` defines
Layer 3 PARA as `{projects}`/`{areas}` only; `:68`'s hard rule allowlists `_agent/`,
`_meta/`, `{wiki}` + the two named PARA surfaces and prohibits "nothing else **in
PARA**"; `:41`'s structure-table row defines `resources/` as its own zone with no stated
write posture. `resources/<not-wiki>/` genuinely sits in neither clause — the gap is
real, not a misreading, and the root-cause read (0.14.0 made `resources/` a mixed zone;
the write rule was never revisited) matches the shipped history.

- **This is an owner design ruling, not an edit** — the filing deliberately proposes no
  answer. **Open design question carried verbatim for ideation:** is `resources/`
  outside `{wiki}` partner-writable, and if so under what discipline — attestation?
  extraction-only? a named surface, the way the two PARA surfaces are named? or
  explicitly closed? Any of the four is a usable answer; the silence is not. A ruling of
  "explicitly closed" satisfies the filing fully.
- **Field posture noted:** the filing vault parked its shelf in the agent zone as a
  reversible interim, addressed through a structure-map key — so acting on the ruling
  costs one config value vault-side. No urgency distortion; the motivation ("put the
  human-facing artifact where humans browse" is every partner's next inference) argues
  the edge recurs across vaults.
- **Acceptance shape (from the payload):** the contract states a posture explicitly
  enough that a partner answers without escalating — whichever way the ruling goes.
- **Cross-filing:** the design-ruling side of the A11-5/A11-9/A11-10 relocation trio —
  the only one of the three needing an owner ruling rather than an edit; A11-9's prose
  fix wants to cite its outcome.

### A11-11. Full lint's cost scales with corpus, not with change (2026-08-24) — 2026-08-24-102813-full-lint-cost-scales-with-corpus-not-with-change.md

**CONFIRMED — every mechanism claim verifies against the shipped workflow; the token
totals remain the filing's own flagged estimate.** Verified at
`skills/vlt-setup/assets/workflows/vlt-lint-full.js`: the per-page scanner read set is
the four conventions including `wiki-index` (`convRead` calls in `pageScanPrompt`,
`:172-174`) while the page ask itself judges frontmatter/supersession/Gap B and returns
no index judgment — the ~8 KB × N index read does no work there, as filed. Byte sizes
exact: 38,672 + 8,195 + 6,114 + 5,550 = 58,531 per agent. `pageScanPrompt` leads with
the variable `${p.path}`/`${p.slug}` before the invariant block (`:172-174`) — the
cache-hostile ordering, as filed. `clusterCap = max(12, ⌈N/4⌉)` (`:90` → 37 at 147
pages), `pairCap` 24 (`:93`), `budgetFloor` 40k (`:87`), models haiku/sonnet
(`:94-96`) — the filing's table shape is right. The cluster prompt receives the
already-extracted `key_claims` **and still instructs "For each, read its LIVE path"**
(`:369-370`) — the bought-and-discarded triage signal, confirmed. The
availability-failure dynamic verifies end-to-end: the majority-coverage floor errors
with `status: 'failed'` (`:233-235`), and `full-scale.md` step 3 then refuses to persist
and **does not write the Step-6 log line, so `lint-debt` does not reset** — on a large
enough corpus under a budget, expense becomes refusal exactly as filed.

- **Candidate directions 0–4 carried verbatim, unresolved** (instrument first; workflow-
  only waste removal; change-keyed findings cache with facts-not-verdicts + honest
  `scanned N / cached M of T` coverage line; scanner-card projection — the reachability
  root fix, governance-surface exposure, likely ruled last; pairing with the
  adjudicated-divergence memory filing). The anti-direction is also carried: **no
  sampling** — Cycle 10's honesty is not spent back, and **no `coverage_caps` entry is
  ever removed to make a run look cleaner**.
- **Sequencing ruling owed at ideation (carried):** direction 2 touches the same
  full-mode coverage predicate as **A10-18** (single-homed at
  `skills/vlt-lint/references/full-scale.md:7`), which carries the B10-2(5)/B10-12(6)
  bound debt gating this cycle's closeout — an owner sequencing ruling comes before
  direction 2 is briefed. Direction 1 has no entanglement.
- **Cross-filing:** direction 3 is the cycle theme's purest instance (a declared rule
  unreachable at the granularity that needs it); adjacency with the held
  `2026-07-26-184704-lint-full-asks-llms-for-exact-facts.md` (correctness side of the
  same seam — B5-3 moved the arithmetic to JS; moving the *reading* out is what retires
  the 38.7 KB read) and `2026-07-26-124223-lint-has-no-memory-of-adjudicated-divergence.md`
  (shares direction 2's sidecar-state mechanism; separate build, ideate together).

## Capture narrative — 2026-08-24 run (the judgment calls, on the record)

- **GitHub intake:** 5 admitted open issues (#1, #4, #6, #7, #8) all already
  materialized (origin-token idempotence hits) and correctly labeled `captured` —
  nothing materialized, no label drift. Amendment leg: no `captured`+`amended` issues.
- **Cycle opening:** `factory/CYCLE` read `none`; Cycle 10 CLOSED 2026-08-23 → this run
  opened Cycle 11 (number = one past `10-signal-integrity`), slug `reachability` from
  the batch's through-line. This capture run is also **platform P-8's self-acceptance
  path event** (the capture opening at `factory/cycles/11-<slug>/`) — the paired
  `lifecycle-status` run discharges P-8's done-when; P-10's discharge is the owner-gated
  `issue-triage` sync projecting this roadmap onto the tracker.
- **Scope:** all 8 un-captured filings captured (owner-confirmed in-session, no
  deferrals); the 6 Cycle-10 holds re-listed with pointers, not re-ground.
- **Grounding corrections this run:** A11-2 (three templates carry the handle, not
  two); A11-3 (consult parity check answered NO at grounding — no fan-out exists;
  council-only build); A11-6 (attestation net keys `agent|hybrid`, not
  `human|agent|hybrid`); A11-1 (leg lives at `checks.md:48`, not `:47`; two consumer
  sites restate the example signal).
- **Spike flag for ideation:** A11-2's Q1 (GitHub watch/notification semantics) is an
  external unknown → spike before brief (lifecycle step 3; register per P-2 when its
  register lands).

## Capture narrative — 2026-08-24 second run (A11-9..A11-11)

- **GitHub intake:** issues #10 and #11 (owner-admitted `vault-accepted` in the same
  session's `issue-triage` run) materialized to
  `factory/inbox/2026-08-24-142822-…` / `…-142828-…` and labeled `captured`; #1/#4/#6/#7/#8
  remained idempotence hits, correctly labeled. Amendment leg: empty.
- **Scope:** all three un-captured filings captured (owner-confirmed in-session — the two
  rail materializations + the owner-filed full-lint cost pattern filing); the held inbox
  population untouched.
- **Cycle posture:** Cycle 11 open, pre-ideation (no rulings, no roundtable stamp) — plain
  capture, no addendum machinery; A11 numbering continues at A11-9.
- **Grounding corrections this run:** none — all three filings' claims verified as cited
  (triage had already grounded the rail pair; capture re-derived the sites independently).
  One note held on the record: A11-11's ~4.1 M-token total is the filing's own flagged
  estimate (its Direction 0 makes instrumenting it the first move); the mechanisms behind
  it all verified.
- **Owner rulings owed at ideation, flagged:** the A11-10 write-posture design ruling
  (four usable shapes named); the A11-11 direction-2 vs A10-18 sequencing ruling.
