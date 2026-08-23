---
title: 'Inbox Evolution Roadmap — Arc 10: the signal-integrity arc'
status: 'CLOSED 2026-08-23 — the signal-integrity arc. Shipped: v0.13.0 2026-08-21 @ a3ec505 (builds B10-1..B10-5) and v0.14.0 2026-08-23 @ 283fe5d, annotated tag 55b739d (builds B10-6..B10-12, the single option-C cut). Acceptance: discharged 2026-08-21..23 over the vlt-core 0.13.0 and 0.14.0 upgrades plus same-day field events, on the persisted-report instrument''s first live use (the A1 hand-save posture retired) — 6 of 12 ledger items ticked on dated evidence (the count is not a measure of what the arc proved); B10-2(5)/B10-12(6) FAILED narrowly and carry as BOUND inherited debt to Arc 11 (ship-verifiable re-check — GATES); B10-4(4) BLOCKED (unreachable), carried, not a watch. Both review halves complete — every clerk disposition and DA1..DA11 owner-ruled, incl. the B10-4 direction-2 count-shape premise correction. Still open elsewhere: the released watches B10-7(4)/B10-8(4)/B10-8(5)/B10-9(3)-remainder, the confidentiality + propagation-debt DECLINE+WATCHes, the Arc 11 held captures A10-10/A10-12+13/A10-15-C3/A10-18/A10-19, the seven un-captured filings (Arc 11''s capture seed), and the inherited registers — authoritative list in the Closeout record at the end of this file. This arc is archived — do not append.'
module_code: 'vlt'
created: '2026-08-21'
updated: '2026-08-23'
derives_from:
  - 'inbox/2026-08-21-100000-spec-candidate-relay-count-six-repeat-false-positives.md'
  - 'inbox/2026-08-21-100500-lint-scanner-prompts-skip-rule4-coexistence-and-callout-vs-bullet.md'
  - 'inbox/2026-08-21-101000-crosslayerslugs-omits-handoffs-bases-and-areas.md'
  - 'inbox/2026-08-21-124500-upgrade-reports-need-a-durable-vault-home.md'
  - 'inbox/2026-08-21-124800-report-yaml-in-markdown-legibility.md'
  - 'inbox/2026-08-21-144352-skill-asset-manifest-hashed-from-live-files-divergence-net-blind.md'
  - 'inbox/2026-08-21-144554-lint-fan-out-gap-b-asked-unconditionally-misfires-without-write-verification.md'
  - 'inbox/2026-08-21-150500-captured-issues-accept-comments-the-intake-never-reads.md'
  - 'inbox/2026-08-21-150800-vault-capabilities-install-tools-with-no-dependency-record.md'
  - 'inbox/2026-08-20-093000-para-write-path-single-door-wrong-shape.md'
  # mid-arc capture addendum 2026-08-22 (A10-10..A10-15):
  - 'inbox/2026-08-21-150212-wiki-index-row-format-rule-contradicts-worked-example.md'
  - 'inbox/2026-08-21-150213-high-value-gaps-declared-field-has-no-producer.md'
  - 'inbox/2026-08-21-150214-decision-log-writer-roster-admits-no-discovery-site.md'
  - 'inbox/2026-08-21-150215-decision-log-kind-has-no-value-for-scoped-deviation.md'
  - 'inbox/2026-08-21-164445-step4-report-omits-manifest-write-divergence-line.md'
  - 'inbox/2026-08-21-181500-rail-triage-arc-surface-candidates.md'
  # mid-arc capture addendum #2, 2026-08-22 (A10-16..A10-17):
  - 'inbox/2026-08-22-130455-lint-full-nonexecutable-and-vacuous-clean-report.md'
  - 'inbox/2026-08-22-130456-lint-missing-target-false-positives-existing-pages.md'
  # (^ WITHDRAWN by its author 2026-08-22, file deleted — retraction + content folded
  #  into …-130455; A10-17's capture entry stands as the record, scope rides B10-12 leg 3)
  # mid-arc capture addendum #3, 2026-08-23 (A10-18..A10-19 — the two negative grades of
  # the 0.14.0 acceptance run; BOTH owner-ruled HOLD FOR ARC 11, no build minted):
  - 'inbox/2026-08-23-160500-crosslayerslugs-blind-to-sources-index-and-non-md-linkables.md'
  - 'inbox/2026-08-23-190100-local-metrics-kinds-cannot-express-a-content-filtered-count.md'
  # (^ captured together with the issue #1 amendment consumed by the same run's intake leg:
  #  inbox/2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md, amendment
  #  section only — the filing itself was captured in Arc 9 and is not re-captured here)
  # NOT captured by that run (owner-scoped to the ledger-blocking pair) and still un-captured
  # on disk, owned by the next capture run: …-2026-08-22-150000-spec-candidate-relay-leg…,
  # …-2026-08-23-110913-amendment-trigger…, …-2026-08-23-111410-council-consult-partial-lens…,
  # …-2026-08-23-180100-rule-shelved-as-trailing-clause…,
  # …-2026-08-23-180200-migrations-amend-the-base…,
  # …-2026-08-23-190200-undeclared-para-type…, and the newly materialized
  # …-2026-08-23-210653-instrument-rule-for-byte-exact-comparisons.md (issue #8).
  # (A9-1 — inherited whole from Arc 9, owner ruling 2026-08-21; its grounded capture
  # lives in the Arc 9 archive and is pointed at, never restated, below)
predecessor: 'skills/reports/archive/inbox-evolution-arc9-roadmap.md (Arc 9 — CLOSED 2026-08-21, builds B9-1..B9-5 shipped v0.12.0 @ 336d90b; B9-6/B9-7 folded here unbuilt)'
intent: >
  Arc 10 opens on a dual inheritance and one new story. The inheritance: the PARA
  write-path filing (A9-1) that was Arc 9's original headline, ruled out because its brief
  cannot be written from module source alone, plus the two release-forward builds (B9-6,
  B9-7) that v0.13.0 was cut without. The new story, told nine times by nine filings all
  dated the same day: the module's instruments — lint's fan-out, the spec-candidate
  signal, the skill-asset divergence net, the upgrade report, the feedback intake, the
  dependency expectations of capabilities — emit signal that is wrong, lost, or unheard.
  Arc 9 drew the boundaries; Arc 10 is about whether the machinery watching those
  boundaries can be believed.
---

## Inherited from Arc 9 (owner rulings 2026-08-20/21 — re-listed, not re-decided)

Authoritative source: the Arc 9 archive's Closeout record, *Carried forward past Arc 9*
(`skills/reports/archive/inbox-evolution-arc9-roadmap.md:2620-2660`). This section
re-lists what Arc 10 must act on; the archive holds the reasoning.

1. **A9-1 — the PARA write-path filing** (`inbox/2026-08-20-093000-…`) — inherited
   **whole**: its grounded capture, Q6/Q7 (the PARA container questions, archive `:1398`,
   `:1403`), E5/E6 (deferred with it, `:1986`, `:1991`), and spike **S1** (the two-vault
   container harvest, `:1907`) all live in the Arc 9 archive. Its thesis — Layer 3's
   boundary drawn by *location* where it should be drawn by *authorship* — is this arc's
   deepest inherited question. S1 must run before any brief.
2. **B9-6 — durable metric home + overlay bell + Finding 4** (A9-3 + A9-2; archive
   `:976`) — ruled, unbriefed, unbuilt; spike **S3** (the `vlt-upgrade` Step-3/Step-3.6
   ordering trap, `:1928`) closes before its brief. Target was v0.13.0.
3. **B9-7 — the fleet-wide rung** (A9-5; archive `:995`) — ruled, briefed-then-re-scoped,
   unbuilt; spike **S2** (boot-cost of a new always-loaded read, re-scoped, `:1918`)
   closes before its brief. Target was v0.13.0.
4. **The narrow-vs-general ruling Arc 10 ideation owes** (closeout item 1): the operating
   contract has no overlay mechanism — the durable-host doctrine's three hosts do not
   cover the file that states the doctrine. Compounds with A10-6 below (the
   divergence-net defect): a vault whose only legal move is a hand-edit is exactly the
   vault the blind manifest then betrays.
5. **D7** (does `grounding:` inherit the personalized-extraction firewall checks,
   archive `:1896`) and the **four brief-time questions** (Round 1, per the archive's
   successor line) — ideation-table items, carried.
6. **Standing watches** (not this arc's to build, listed for visibility): E2 scrub-gate
   efficacy, the B9-4(3)(a/b) lint-cycle and vitals-Confirm first exercises, the B9-5
   Stage-5 terminal half, the rail degrade path, the lane-check fixture-grammar note, the
   Disposition-4 PARA factory-side posture, and the inherited C6-c / B5-3..B5-9 /
   pre-Arc-5 / Arc-7 registers — all per the closeout record.

## The through-line

Every one of the nine newly captured filings is about **signal integrity** — the gap
between what the module's machinery reports and what is true:

- **False positives drowning real findings** (A10-1, A10-2, A10-3, A10-7): four lint
  signals fire on conformant state. Three share one root shape — *the enforcing agent was
  never handed, or never had encoded, the rule it enforces* (Gap B's governing convention
  absent from the scanner's read list; the coexistence posture and callout-vs-bullet
  distinction left to a cheap scan model's faithful convention read; the cross-layer
  allowlist assembled from a vague parenthetical). The fourth (A10-1) is suppression that
  exists but goes unused in practice. A10-7's filer names the general check: audit every
  fan-out ask against the convention set its scanner receives.
- **An instrument that disables itself** (A10-6): the divergence net's `--write` hashes
  the live tree, so the one state it exists to catch — a local edit — is the state that
  silently becomes its new baseline.
- **Evidence that evaporates** (A10-4, A10-5): the upgrade's full post-flight report — now
  acceptance evidence by Arc 9's own rules — persists nowhere, while lint's equivalent
  persists verbatim; and the persisted shape (YAML fenced in markdown) is itself
  questioned. The pair is one ruling: *whether* reports persist and *in what shape*.
- **A deaf ear** (A10-8): the rail's first live exercise found its first structural hole —
  a captured issue invites comments the factory will never read.
- **An unstated expectation** (A10-9): capabilities install machine-level tools with no
  record; the vault ports, the toolchain doesn't. The durable-host doctrine, applied to
  dependencies.

The inherited A9-1/B9-6/B9-7 half is not signal-integrity work — it is Arc 9's boundary
work finishing its release. The two halves meet at A10-6 + the narrow-vs-general ruling
(inherited item 4): both are about what happens when the module gives a vault no legal
place to put something and then mis-measures the workaround.

## Capture — 9 filings (grounded against module source 2026-08-21, v0.12.0 @ 336d90b)

Run notes: the GitHub intake ran first (`mggower/bmad-module-vlt`, per
`module.yaml:69` `feedback_repo.default`). Three admitted open issues (#1, #2, #3) — all
three already materialized on disk with matching `origin:` keys and all already labeled
`captured`; nothing new materialized, no label drift, no stale-shape holds (all stamp
`rail_contract: 1`, current). The Arc 9 closeout's carry item 9 says "8 uncaptured
filings" but enumerates nine filenames; the enumeration (and project memory) is taken as
authoritative — the count was the typo. Owner confirmed all-nine scope in-session. The
three ruling-4c recoveries below were filed with grounding against v0.11.0 @ 86efd48;
this run re-derived their cited sites against v0.12.0 — all survived Arc 9 unchanged.

### A10-1. The naive `spec_candidate` relay count re-fires the same six false positives (2026-08-21) — …-100000-spec-candidate-relay-count-six-repeat-false-positives.md

**GAP CONFIRMED, in the filing's own narrowed form.** The check is at
`skills/vlt-lint/references/checks.md:47` (*Spec candidates*): relay-entries-only counting,
drained-archive inclusion, no stored counter, and the designed suppression — "A candidate
with a **recorded decline** in `{backlog}` or its `{archive}`-mirrored sibling … is
excluded from the finding, with the count of honored declines stated beside it" — are all
present in current source, verified verbatim. The residual defect is exactly as the filing
narrows it: the *only* suppression is a per-candidate decline record, and three
consecutive field runs (the last with the decline mechanism live since v0.9.0) produced
six repeats and zero declines. The field evidence indicts the ritual, not the mechanism's
absence: either the decline path is too heavy for batch-noise or no run routes to it.

Fix directions the filing offers for the ideation table (not resolved here): a
batch-decline affordance at report time; or a repeat-aware report line (new candidates
loud, unchanged repeats quiet). Cross-filing: same signal-vs-noise second-order cost A10-7
names — a reviewer who learns a class is noise stops reading it.

### A10-2. `vlt-lint-full.js` scanner prompts don't encode rule 4's coexistence posture or the callout-vs-bullet distinction (2026-08-21) — …-100500-lint-scanner-prompts-skip-rule4-coexistence-and-callout-vs-bullet.md

**GAP CONFIRMED (the filing's own "partially addressed" grading re-verified).** The prompt
is `pageScanPrompt` at `skills/vlt-setup/assets/workflows/vlt-lint-full.js:166-183`, the
convention read list built by `convRead` at `:161`. Confirmed present: the B7-6 rule-4
normalization instruction for Gap B ("strip surrounding quotes and `[[ ]]`, strip a
trailing `.md`, compare on the vault-relative path"), and the merged-on-read overlay
handling. Confirmed absent: (a) the **coexistence posture** — `frontmatter.md` rule 4
(version 9, `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:36`
region) states "existing bare-path entries stay legal and there is **no backfill sweep**",
but the prompt never restates it; whether a legal mixed state gets flagged rides on the
scan model's faithful read of the convention. (b) The **callout-vs-bullet distinction** —
the prompt asks for `unmarked_supersession` and `name_callout_targets` but nowhere states
that a bullet- or heading-form marker is not a callout (in either direction). Both are the
seam class B5-3 closed for slug normalization: model judgment where an explicit
instruction should sit.

Cross-filing: same file and same seam class as A10-7; A10-7's proposed general check
("does any fan-out ask enforce a rule its scanner wasn't given?") subsumes this filing's
residual — strong candidate to build as one lint-full prompt/read-list repair.

### A10-3. The fan-out's `crossLayerSlugs` omits `_agent/handoffs/`, `_agent/bases/`, `areas/` (2026-08-21) — …-101000-crosslayerslugs-omits-handoffs-bases-and-areas.md

**GAP CONFIRMED.** The workflow is agnostic and correctly warns for itself
(`vlt-lint-full.js:35` arg doc, `:78` intake, `:211` set construction; the comment at
`:208-210`: "Without crossLayer, valid cross-layer links false-positive en masse"). The
gap is the assembly instruction: `skills/vlt-lint/references/full-scale.md:7` (step 1)
tells the SKILL to glob `{research}` "(and any agent-zone note location the wiki
conventionally `[[links]]` into)" — `_agent/handoffs/` covered only by that parenthetical,
`_agent/bases/` (vault-grown, in-contract per `vault_structure`'s vault-local keys)
silently missed by any non-enumerating instruction, `areas/` (a PARA layer, neither
research nor agent-zone) covered by no clause at all.

Design tension the filing names, carried verbatim for ideation: CLAUDE.md's
"lists that claim completeness drift" rule argues against hard enumeration; the field
shows the vague parenthetical missed three layers. The filing's point-at-the-map
direction — derive the glob set from resolved `vault_structure` keys holding linkable
notes — satisfies both. Note the A9-1 adjacency: if Arc 10's PARA work reshapes Layer 3,
the linkable-layer set changes again — an enumeration would be stale on arrival.

### A10-4. The upgrade's full post-flight report is never persisted (2026-08-21) — …-124500-upgrade-reports-need-a-durable-vault-home.md

**GAP CONFIRMED.** The asymmetry is real: `vlt-lint/SKILL.md:72` persists the Step-5
report block **verbatim** to `{lint_reports}/YYYY-MM-DD-HHMM-lint.md` (path at
`module.yaml:61`), with its Decay-contracts exemption; `vlt-upgrade` persists only the
digest ledger block (`vlt-upgrade/SKILL.md:121`, `{upgrade_ledger}` at `module.yaml:58`,
append-only summary) — no persist instruction for the Step-4 report exists anywhere in
`vlt-upgrade/SKILL.md` (grep: zero relevant hits), and no `upgrade_reports`-style path
exists in `module.yaml`. The filing's three whys stand grounded: the Step-4 report is
acceptance evidence (Arc 9's B9-2 field-contingent check discharged by hand-carried chat
transcript in the 2026-08-21 run), the lost-ephemeral-report class already cost ruling 4c
a three-arc slip, and the report carries owner rulings.

Design notes carried for ideation (not resolved): the symmetric shape (verbatim dated
file under a config path, **retention row declared in the same build** per Arc 8's
retention-at-birth rule); the census question — which verbs report-and-discard vs
report-and-persist (lint persists, upgrade digests; groom? decay? setup?); durable-host
doctrine already satisfied by `_agent/` siblings; whether the persisted report doubles as
the factory's acceptance instrument. **Companion: A10-5 — one format ruling for both.**

### A10-5. Reports are YAML fenced inside markdown — plain `.yaml` instead? (2026-08-21) — …-124800-report-yaml-in-markdown-legibility.md

**CONFIRMED as filed (a question, not a defect — carried to ideation unresolved).** The
current shape verified: `vlt-lint/references/report.md:3` ("The fenced report block is
strict YAML as a whole — keep it parsing whole") inside a `.md` wrapper that carries
essentially nothing else; the upgrade Step-4 report is the same shape in-session. The
filing's trade table is carried verbatim to the ideation table: `.yaml` for direct
parseability vs `.md` for the vault machinery's walkers — sharpened by the fact that
reports are deliberately *exempt* artifacts (never wake-read), so invisibility to the
walkers may be exactly right or may strand future tooling. Middle shapes to price:
minimal-frontmatter+one-fence contract; `.yaml` sidecar + `.md` pointer; `.yaml` under
report dirs as a declared lint-walker exclusion. A build owes the consumer census
(`vlt-lint/SKILL.md:72`, `report.md`, path docs; the lint-debt counter derives from the
session log, not reports — stated at `SKILL.md:72` "by derivation, the `lint-debt`
counter reset" — but verify at brief time). **Must land under the same ruling as A10-4.**

### A10-6. Write the skill-asset manifest from stock content — hashing live files disables the divergence net (2026-08-21) — …-144352-…-divergence-net-blind.md · origin: mggower/bmad-module-vlt#2

**CONFIRMED — defect, rail-materialized (issue #2, `captured`).** Every claim re-derived:
`skills/vlt-setup/scripts/verify-skill-manifest.py:72-102` `compute_manifest` — both loops
hash the live tree (`:85` `skill_dir = live_skills_dir / name`, `:90`/`:102`
`sha256_file(f)` on live/installed files) while `source_skills_dir` supplies names only
(`:82`, `:93`). Both contradicting prose claims verified verbatim:
`skills/vlt-setup/SKILL.md:153` ("Compute it from the *installed* shipped files (which
equal stock at install time)" — true once, false thereafter) and
`skills/vlt-upgrade/SKILL.md:49` ("The skill manifest itself is refreshed to the new
shipped versions by the Step-6 provision hand-off" — it is refreshed to live versions).
The no-upgrade reproduction (hand-edit → re-run `vlt-setup` → manifest absorbs the edit)
is sound: `vlt-setup` provisions governance/workflows/hooks, never re-copies skill files.
Field-hit in the 2026-08-21 vlt-core upgrade (Arc 9 acceptance record confirms the vitals
divergence had to be re-established by hand).

The filer's fix guess grounds as the right single site: on `--write`, hash source-tree
content for source-provenanced paths, live only where no counterpart exists — making both
prose claims true rather than needing rewording. The filer's open question carried for
ideation: should `--write` refuse or report (`absorbed: [...]`) when live differs from
source at manifest time. Cross-filing: compounds with the inherited narrow-vs-general
ruling and B9-6 (issue #1) — independent fixes, same victim population. Acceptance is
synthetic-reproducible (ship-verifiable candidate): edit one manifested file, `vlt-setup`,
`--verify` → still `diverged`.

### A10-7. Supply `write-verification.md` to the lint fan-out scanner — Gap B asked unconditionally (2026-08-21) — …-144554-…-misfires-without-write-verification.md · origin: mggower/bmad-module-vlt#3

**CONFIRMED — defect, rail-materialized (issue #3, `captured`).** Re-derived: the
scanner's convention read list (`vlt-lint-full.js:167`) is `frontmatter`,
`wiki-supersession`, `wiki-index` — `write-verification` is not in it; the Gap B ask in
`pageScanPrompt` ("whether the frontmatter `sources:` and the prose Sources section
diverge") carries no no-prose-section carve-out; the governing conditional lives at
`skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md:38` ("a page
with no prose section is conformant"). Field evidence: 22 of 25 findings in the class
false (88%) on a 56-page wiki. Both filer fix sites ground: (1) add `write-verification`
to `convRead` — root cause, general; (2) make the tri-state explicit in the ask/schema
(the `PAGE_SCAN` schema at `:97-128` currently folds "no prose section" into the boolean).
The filer's general check — audit every fan-out ask against the convention set its
scanner receives — is the load-bearing capture: it subsumes A10-2's residual and is the
natural shape for one combined lint-full repair build with A10-2 (and plausibly A10-3).

### A10-8. Captured issues accept comments the intake never reads (2026-08-21) — …-150500-captured-issues-accept-comments-the-intake-never-reads.md

**GAP CONFIRMED.** The field contract's state flow
(`skills/vlt-feedback/references/field-contract.md:54-69`: `vault-filed → vault-accepted →
captured`, or `→ declined`) has no amendment verb — zero occurrences of amend/comment in
the contract. The factory intake queries admitted-**open** issues and excludes any issue
whose `origin:` token already exists under `inbox/` (correct idempotence, A15(d)) — so a
captured issue is a write-only surface for its filer across the whole open window (which
lasts until archive, potentially arcs). Proven live: the substantive 2026-08-21 comment
on issue #1 reached the factory only because the owner mentioned it in-session.

Design material carried verbatim for ideation: the re-triage label (owner-applied
`amended` or re-applied `vault-accepted`; one extra query leg; append to the existing
filing, never re-materialize), vs the comment-scan with watermark; the contract-text
obligation either way (state-flow table gains the amendment verb; the issue templates
tell filers whether comments reach the factory — today's silence is an honesty gap in
the contract's own terms); A15's cost discipline applies to amendments (an unadmitted
comment costs the factory nothing). Note: the intake mechanics half of any fix is
factory-side (`.claude/skills/inbox-capture/references/github-intake.md`, gitignored);
the contract/template half is shipped surface — a build touches both sides of that seam.

### A10-9. Vault capabilities install machine-level tools with no dependency record (2026-08-21) — …-150800-vault-capabilities-install-tools-with-no-dependency-record.md

**GAP CONFIRMED (pattern candidate, as filed).** Verified: `vlt-feedback/SKILL.md:90`'s
named `gh-missing` error (with `:107`'s degrade choreography) is the one shipped instance
of a dependency being checked-and-reported, done per-skill ad hoc; `module.yaml` declares
no dependency of any kind (zero hits); no manifest of vault-grown tool dependencies
exists anywhere in the module or the mint/capability ceremonies. The two-layer split the
filing draws is the capture's keel: **module-level** dependencies (what shipped skills
assume — `gh`, `uv`; arguably `module.yaml`'s to declare) vs **vault-grown** dependencies
(what local capabilities added — agent-zone, durable, vault-writable; the durable-host
doctrine's population). Design directions carried: declare-at-birth (retention-at-birth
applied to tooling, plus a one-time retroactive census) and check-at-arrival
(`vlt-setup`/`vlt-upgrade` report-not-gate, the named-error discipline generalized).
Related: the rail-degrade standing watch (inherited item 6) and A9-4's multi-machine
theme — vaults provably move across machines faster than their toolchains.

## Ideation rulings — A10-1..A10-9 + inherited A9-1/B9-6/B9-7 (owner-steered, 2026-08-21)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Skeleton
laid 2026-08-21 by `ideation-scaffold`; **session COMPLETE — filled 2026-08-21 over six
owner-steered rounds (Round 0 spikes-first through Round 6 synthesis). Every slot is
ruled.** One ruling was resolved on a clerk recommendation at the owner's request (D2)
and one on the clerk's risk read against the owner's stated conditional (Q6, fallback on
record); both are marked in place. `build-brief` gates on this section being filled —
it is.

Seeded from the Arc 10 capture (2026-08-21) and the Arc 9 closeout's carry-forwards.
Question numbering is the clerk's, for reference in session only; it implies no ordering
or priority.

**Session ruling, Round 0 (owner, 2026-08-21): spikes first, ideation deferred.** The
owner ruled that S1/S2/S3 run **now**, before any further rulings, because their results
inform the shape of the roadmap (S3 decides whether B9-6 carries a defect fix; S2 prices
B9-7; S1 shapes the entire A9-1 half). Ideation resumes when the three SPIKE CLOSED
records below are dated. Provisional pencil marks from the aborted Round 1 (Q1 leaning
"everything stays", Q4 leaning "interleaved"; D7 unanswered) were **re-put and ruled in
Round 1 after all three spikes closed** — see the slots below.

**What each round settled (running list).**

- **Round 0 (2026-08-21)** — spikes first; ideation deferred until S1/S2/S3 closed. All
  three closed the same day.
- **Round 1 (2026-08-21, post-spikes)** — the arc's shape: **everything stays** (Q1);
  **interleaved, A10-6 early** with B9-6 briefed only after the A10-6 build per S3 (Q4);
  the K9 template fix is a **drive-by** (D7).
- **Round 2 (2026-08-21)** — the cross-cutting pair: the contract gets a **narrow
  per-host overlay** (Q2, consistent with Arc 9's no-single-mechanism ruling); reports
  follow a **general persist rule with a verb census** (Q3a) and live as **plain `.yaml`
  under a declared lint-walker exclusion** (Q3b).
- **Round 3 (2026-08-21)** — the lint-signal and manifest decide-onces: **one combined
  lint-full repair** (D1: A10-2 + A10-7 + A10-3, A10-1 separate); `crossLayerSlugs`
  **derives from the map with a one-line interim PARA supplement** whose deletion binds
  to the A9-1 widening build (D2); A10-1 gets the **repeat-aware report line** (D3);
  A10-6's `--write` **reports `absorbed:`, never refuses** (D4).
- **Round 4 (2026-08-21)** — the rail, the record, the firewall: amendments reach the
  factory by **owner-applied re-triage label** (D5); the dependency record ships **both
  halves** — declare-at-birth + check-at-arrival, report-not-gate (D6); `grounding:`
  **inherits the firewall family in the same build that ships the field** (Q7).
- **Round 5 (2026-08-21)** — the PARA tail: workspace posture **confirmed moot** (Q5);
  the resources-retirement/wiki-move series ships **whole this arc, internally sequenced
  model-first** with the move as the capstone build (Q6, owner's conditional resolved on
  the clerk's risk read; fallback on record); the attestation census **ships with the
  move** (E6).
- **Round 6 (2026-08-21)** — the synthesis: the derived build list stands **as laid,
  B10-1..B10-11 in table order**; **v0.13.0 cuts after B10-5** (builds 1–5), later cuts
  called as builds land; the **K9 drive-by rides B10-1**.

### Grouping & order

**RULED (Round 6, 2026-08-21): eleven builds, as laid, in this order.** Standing rule
(Arc 9): every build bullet carries a `binds:` roster, kept current as rounds add
rulings.

- **build-B10-1 — A10-6, the manifest fix.** Source-hash the manifest for
  source-provenanced paths (live only where no counterpart exists), making both prose
  claims (`vlt-setup/SKILL.md:153`, `vlt-upgrade/SKILL.md:49`) true; `--write` reports
  divergence, never refuses; the brief resolves S3's sanctioned-lift tension within that
  posture. **Carries the K9 drive-by** (`vlt-mint/assets/capability-template.md:23`).
  Ship-verifiable (synthetic reproduction: edit → `vlt-setup` → `--verify` still
  `diverged`). Unblocks B10-4. *(roundtable 2026-08-21: A5 — the brief also closes the
  two escape paths: on `--write` with source == live (the `vlt-setup/SKILL.md:163`
  fallback) refuse the silent path or report loudly that the manifest is live-hashed, and
  refuse with a named error (the `gh-missing` discipline) when the source tree's
  `module_version` ≠ the installed version record; acceptance gains live-as-source and
  version-skew fixtures. A6 — the `absorbed:` list routes into the upgrade post-flight
  report/Confirm summary and the manifest write is named an E2 census entry, born under
  Q3's ruled shape or the brief records why not. A14 — carries a second drive-by: the
  one-sentence interim honesty note in both issue forms (comments on captured issues
  reach the factory only via owner admission), replaced by B10-7's full template text.)*
  **`binds:` Q4, D4, D7, S3 + Q3a *(roundtable A6)*.**
- **build-B10-2 — the lint-full signal repair (A10-2 + A10-7 + A10-3).** `convRead`
  gains `write-verification`; the Gap-B ask/schema goes tri-state; the
  coexistence-posture and callout-vs-bullet instructions are made explicit;
  `crossLayerSlugs` derives from resolved `vault_structure` keys **plus the interim PARA
  supplement line** (retired by B10-10); plus A10-7's general audit — every fan-out ask
  checked against the convention set its scanner receives.
  *(roundtable 2026-08-21: A7 — the interim supplement line names `_agent/handoffs/`
  alongside the PARA layers (no `vault_structure` key is minted this arc — C6-b's
  merge-config strip makes key-minting unsafe until that debt clears) and carries its own
  retirement clause in the shipped text; **[owner-ruled 2026-08-23 — the reading of this
  parenthetical: CONDITIONAL, not arc-wide.** "No key *before* the C6-b fix"; a build
  that clears the fix may mint in the same act. B10-10 is that build (F2 clears with a
  red-then-green fixture, case 22 / `CASE_FLOOR` 22; F1 then mints five keys) and both
  interim clauses were deleted per their own retirement text. The clerk's read is
  confirmed; the strict arc-wide reading is rejected on the record.**]; the qualifying-key predicate — which resolved
  keys hold walker-visible linkable notes — is single-homed in `full-scale.md`, and
  B10-6's exclusion and B10-10's inclusion each edit that home. A8 — the `convRead` edit
  ships its handshake in the same build: `write-verification.md` `consumers:` gains
  `vlt-lint-full.js` and the workflow's E5-parsed `depends_on:` ack gains
  `write-verification@3`; every restated convention instruction carries an inline source
  marker (`per frontmatter@9 rule 4` style). Ships R4 — see the review record.)*
  **`binds:` D1, D2, R4 *(roundtable A7/A8)*.**
- **build-B10-3 — A10-1, the repeat-aware report line.** New candidates loud; unchanged
  repeats one quiet line with repeat count. Decline path untouched.
  **`binds:` D3.**
- **build-B10-4 — B9-6 carried (durable metric home + overlay bell + Finding 4).**
  Briefed **only after B10-1 lands** (the S3 dependency). Arc 9's rulings travel whole:
  its roster lives at the archive's build entry (`:979`) — direction 1/2 choice on top
  of the direction-3 floor (A21) is the standing brief-time question.
  *(roundtable 2026-08-21: A2 — carries the inherited A22 second bump
  (`frontmatter@9 → @10`) with the full nine-consumer + workflow-ack walk as explicit
  in-cut scope; its consumer-walk item for `vlt-lint-full.js` re-derives every marked
  restatement, not just the ack string. A6 — the durable metric home is born under Q3's
  ruled persist shape (dated `.yaml`, retention row same build) or the brief records why
  it sits outside E2's census population.)*
  **`binds:` Q4, S3, Q3a, Q3b *(roundtable A6)* + the Arc 9 roster at archive `:976-984`.**
- **build-B10-5 — B9-7 carried (the fleet-wide rung).** S2 cleared it on cost (~1%
  boot at birth, ~6% at cap-full worst case); A17's negative branch not triggered.
  Arc 9's roster at archive `:995-1008` travels whole.
  *(roundtable 2026-08-21: A9 — the rung's writer population and pointer-shape falsifier
  are worded non-enumeratively (any overlay class the contract recognizes), with B10-9 in
  view; the brief carries one fixture check: a contract-overlay pointer line parses under
  the falsifier as shipped.)*
  **`binds:` S2 + the Arc 9 roster at archive `:997`.**
  **→ Release: v0.13.0 cuts after B10-5** (builds 1–5; the inherited target plus the
  early signal fixes). Later cuts are called as builds land — with two pre-called
  commitments *(roundtable 2026-08-21, owner-ruled)*: **B10-11 ships as its own cut,
  alone** (isolating the relocation's acceptance run; B10-10-without-B10-11 — vestigial
  `resources/` standing — is a legal interim field state), and the **declared fold order**
  if the arc shortens: B10-7/B10-8/B10-9 defer before B10-10/B10-11, so a fold is an owner
  choice made now, not sequencing gravity later. *(roundtable A1, owner-ruled)* **Interim
  evidence posture for the v0.13.0 discharge:** the owner hand-saves the upgrade's Step-4
  report verbatim to a dated file at upgrade time (the last transcript-regime run, a
  deliberate specimen); B10-6 retires this posture and its E2 census names the hand-saved
  file as a migration input. **[owner-ruled 2026-08-23 — A1 RETIRED at the B10-6-bearing
  release: factory discharge reads the persisted `_agent/upgrade-reports/*.yaml` as the
  evidence of record, never a hand-carried transcript; a factory-unreadable vault
  hand-carries the persisted file itself. B10-6 disposition 1 confirmed.]**
  *(roundtable delta 2026-08-22 DA1, roster-converged — ✅ **owner-ruled 2026-08-23, batch**)*
  **Superseding note:** any v0.14.0 cut is **blocked on B10-12** being briefed and built
  (owner ruling, second capture addendum 2026-08-22); the cut **composition** — whether
  and how the two pre-called commitments survive — is **OPEN dispute D1** in the
  roundtable delta record (`## Roundtable review — addendum (2026-08-22)`); the room
  could not rule it without touching a standing owner ruling.
  *(roundtable delta 2026-08-22 DA2, roster-converged — ✅ **owner-ruled 2026-08-23, batch**)* The
  declared fold order is **discharged unexercised**: all fold candidates were built
  sequentially at `7a4b1a8`, so its trigger ("if the arc shortens") closed and the fold
  is mechanically unexecutable under prefix-tag releases; B10-12 appends after B10-11,
  order unaffected. Any future deferral would be a new ruling over a history rewrite,
  not this one.
- **build-B10-6 — the report contract (A10-4 + A10-5).** The verb census first (E2),
  the consumer walk (E1), then the general persist rule (dated verbatim files under
  config paths, retention rows same build) and the `.yaml` cut with the declared
  lint-walker exclusion. Brief-time: the acceptance-instrument question (presented, not
  adopted, Round 2).
  **`binds:` Q3a, Q3b, E1, E2.**
- **build-B10-7 — A10-8, the rail amendment channel.** The `amended` re-triage label,
  one intake query leg, append-never-re-materialize; state-flow table gains the
  amendment verb; issue templates state the comment truth. Both sides of the
  factory/shipped seam. *(roundtable 2026-08-21: A13 — the contract-text scope explicitly
  includes the new `amended` label row and the "Seven labels" count fix. A14 — the issue
  templates state the filer's affirmative move: comment **and @mention the owner**
  (GitHub's notification is the trigger; the label stays the owner's admission);
  supersedes the interim honesty note that rode B10-1.)*
  **`binds:` D5.**
- **build-B10-8 — A10-9, the dependency record.** Both halves: `module.yaml` declares
  module-level deps; the mint/capability ceremony records vault-grown deps at birth;
  one retroactive census; `vlt-setup`/`vlt-upgrade` check-at-arrival, report-not-gate.
  **`binds:` D6.**
- **build-B10-9 — the contract overlay (Q2's narrow build).** Contract-overlay read at
  contract-read time; a rung pointer line (B10-5's shape); R1 fires (rule-card
  re-derive, 8,000-byte budget re-check). *(roundtable 2026-08-21: A15 — the brief rules
  the derived rule card's posture under overlays: either the card carries a standing
  one-line overlay pointer so card-readers inherit the read, or card-reading ceremonies
  are declared exempt with the reason on record — the card is overwritten to shipped
  content on every install (`vlt-setup/SKILL.md:148`), so silence leaves a vault's
  contract overlay unenforced at mint time.)*
  **`binds:` Q2, R1, B10-5's shipped rung wording *(roundtable A9)*.**
- **build-B10-10 — the PARA container model + parameterization (A9-1 head).** The
  harvested model (charter + running record + register, 2–3 files; container status
  enum; per-type artifact status enumerated, closing `extraction.md:94`); PARA keys
  into `vault_structure` — **and the same act deletes B10-2's interim supplement**
  (D2's bound cleanup); the authorship re-draw (C1, five recitation sites);
  `grounding:` ships with its inherited firewall checks (Q7); the three inherited
  brief-time questions attach here.
  *(roundtable 2026-08-21: A2 — the `grounding:`/status-enum widening is a handshake rule
  change: the frontmatter bump-and-walk fires with **whichever of B10-10/B10-11 ships
  first** (owner-ruled; one coalesced bump if same release), and the per-type status enums
  touch `extraction@3` — that bump named at brief time if the enums land there.)*
  **`binds:` Q5, Q6, Q7, D2 (supplement retirement), E5, S1 (the harvest is the brief's
  evidence base) + the A2 handshake obligations.**
- **build-B10-11 — the wiki-move capstone.** `resources/` retirement + wiki move as one
  operation at true cost: two `vault_structure` entries, a `frontmatter` bump **from the
  version current at brief time** with the full **nine-consumer + workflow-ack** walk
  (version-handshake, re-ack same build) *(roundtable 2026-08-21 A2: the ruled "@8 → @9"
  was stale — source is already at @9 and B10-4's in-cut A22 bump takes it to @10, so the
  expected bump here is @10 → @11; the grounding:/type-retirement bump fires with
  whichever of B10-10/B10-11 ships first, owner-ruled)*, the relocation-migration
  discipline (stub, worktree rule, re-point open dispatch pointers), and E6's
  attestation census in the same build. **Deferrable on the recorded fallback without
  re-litigating direction** (Q6). *(roundtable 2026-08-21, owner-ruled: ships as its own
  cut, alone — see the release line.)*
  **`binds:` Q6, E6 + the version-handshake and relocation standing rules.**
  *(Superseding note, B10-11 brief 2026-08-22: the "@10 → @11" arithmetic above is stale
  a second time — B10-5 took @11 and B10-10 took @12, so the capstone's grounded bump is
  **frontmatter@12 → @13**, plus **extraction@4 → @5** determined at brief time; A2's
  governing "from the version current at brief time" clause is what binds. Q6's fallback
  was assessed at brief time: **verdict BRIEF — not fired**; see the brief's risk
  section.)*
- **build-B10-12 — the lint-full execution repair (A10-16 + A10-17), mid-arc escalation
  (owner ruling 2026-08-22 — second capture addendum).** **RELEASE-BLOCKING: briefed and
  built before any v0.14.0 cut.** Three legs, all on the post-B10-11 workflow file
  (`frontmatter@13` ack + `:173` markers, attestation census in the reduce): (1)
  `PAGE_SCAN` under the harness classifier limit as a deliberate source change — the
  fixed-vs-moved-limit question settles first and decides one-time trim vs. a standing
  schema budget (package-lint-enforceable); the lean-schema direction (residual
  semantics into the prompt, descriptions `:106-131` near-duplicate the prompt
  `:172-174`) is the field-validated cheap candidate; (2) loud degrade at the reduce
  boundary — agent shortfall becomes a coverage cap naming count + reason (mirroring the
  overlay posture at `:180-184`), `scans.length === 0` returns an error never a findings
  report, `vlt-lint` SKILL refuses to persist or advance `lint-debt` on
  `files_checked: 0`, and the scans-denominated `attestation_census` (`:383`) is covered
  by the same honesty; (3) the shortfall-corrupted graph — valid-target space
  (`slugSet`, `:208`) derives from the input `pages` list (filesystem truth), not
  surviving scans, retiring A10-17's false-positive class at its root. Any ask/schema
  edit re-runs the R4 fan-out audit. Re-discharge of the FAILED B10-2(5) — an executing,
  loud-degrading full sweep passing the original criteria — is this build's field
  acceptance event.
  **`binds:` the release-blocker posture (owner, 2026-08-22 — no v0.14.0 cut before
  B10-12), A10-16 + A10-17 (second capture addendum), B10-2(5)'s re-discharge criteria,
  R4 (fan-out audit re-run on any ask/schema change), and the pending roundtable-delta
  confirmation (joint moved — see the second addendum's joint test; `build-brief` gates
  on its resolution).**
  *(roundtable delta 2026-08-22, roster-converged — ✅ **owner-ruled 2026-08-23, batch** — DA4..DA8 +
  DA11 amend this entry:)*
  - **DA4 (leg 1 — the spike):** the fixed-vs-moved-limit question is a **pre-brief
    spike obligation** (lifecycle step 3): settle it empirically against the installed
    harness (bisect between `INDEX_SCAN`'s surviving size and 4,266 chars; read the
    harness classifier source where reachable) and record the measured value —
    **trim-vs-budget is then an owner ruling on that number, before the brief**. If the
    question cannot be settled from factory-obtainable evidence, the standing-budget
    branch is the default, pinned to an empirically-passing size with headroom (3,920
    executed pre-B10-2 — a known-good floor). The budget is a **margin device, not the
    guarantee** — the terminating guarantee against a moved limit is leg 2's loud
    degrade plus the re-discharge event.
  - **DA5 (leg 1 — trim discipline):** the near-duplication claim is false
    field-by-field: `available` (`:108`), `created` (`:110`), `frontmatter_issue`,
    `thin`, and the `key_claims` cap exist **only** in the schema descriptions
    (`available`'s semantics are load-bearing for leg 2). The trim is preceded by a
    per-field duplication audit; schema-only semantics migrate into the prompt, never
    dropped; **R4 markers are conserved** — the `per write-verification@3` marker at
    `:121` moves with its semantics or its retirement is recorded in the R4 audit — and
    the touched acks re-walked.
  - **DA6 (leg 2 — respecified):** the degrade cap is denominated over the **input
    list** (any non-budget `scans.length < pages.length`), reason-partitioned
    (agent-failed vs page-unreadable `available: false`), with the failed pages' slugs
    surviving to the operator; **total or near-total shortfall returns an error, never
    a findings report** (the threshold a brief-time question); the SKILL defence is
    re-predicated on the shortfall signal (floor set at brief time; `files_checked: 0`
    the hard case) and worded as the **version-skew defence** — a fixed workflow can no
    longer emit `files_checked: 0`, so the clause guards against a stale vault-local
    workflow copy; the refusal is a **directed surface** (states cause + the operator's
    next move); the error path **persists a dated failed-run record** distinct from a
    findings report, so a refused sweep leaves evidence (the 2026-08-22 no-evidence gap
    does not recur); retry/re-scan of failed pages is deliberately **out of scope** —
    the cap is the signal to re-run; a retry mechanism is its own filing.
  - **DA7 (leg 3 — non-enumerative + census):** grounding correction: the `:270` site
    is the **index-pass** slug enumeration (the cluster pass at `:277-291` iterates
    `scans` directly, never `slugSet`). Leg 3's principle is non-enumerative: **every
    consumer denominated over surviving scans is audited at brief time** (starting
    partition — switch to filesystem truth: `:220` missing-targets, `:270` index
    prompt, `:341` callout gate; stay scans-denominated: `:393` `files_checked`, `:383`
    census, `:209-212` orphans/inbound, near-dup link sets). Inbound-derived findings
    (orphans, near-duplicates) are unfixable from filesystem truth — under any
    shortfall they are suppressed or emitted annotated against the cap, per-slot pick
    at brief time. The census keeps `pages_total: scans.length` (the three-bucket
    partition invariant holds); shortfall honesty rides the cap + `files_listed`; and
    **E6's census checks are re-verified at rest on the post-B10-12 file**.
  - **DA8 (acceptance tagging):** B10-12 pre-binds **ship-verifiable** fixture checks
    that gate: injected partial agent failure → the cap named with count/reason/slugs
    and the report shape; zero scans → error-not-report; a `files_checked: 0` fixture
    against the SKILL refusal; an at-rest schema-size assertion against the settled
    limit (package-lint-enforced under the budget branch). The **field-contingent**
    event is narrowed to: an executing full sweep (`files_checked ≈ files_listed`) —
    degrading loudly if it degrades at all — passing B10-2(5)'s original criteria.
  - **DA11 (the sibling fan-out):** the brief records a disposition of the one other
    `parallel().filter(Boolean)` fan-out, `vlt-review-council.js:148-152` (zero-guard
    present, no partial-shortfall signal): fold a minimal lens-shortfall cap in, or
    decline with the reason on record — a ruling on record, not a scope expansion by
    default.

### Pre-ideation rulings the capture demanded

**Q1 — Arc scope. RULED (Round 1, 2026-08-21): everything stays.** Arc 10 = all of
A10-1..A10-9 **plus** the inherited A9-1 + B9-6 + B9-7. Ruled with S3's coupling in view
(B9-6 depends mechanically on the A10-6 build), which the owner weighed as strengthening
one arc over a split.

**Q2 — The narrow-vs-general ruling. RULED (Round 2, 2026-08-21): NARROW — a
contract overlay.** Per-host plumbing for the one uncovered file: a contract-overlay
mechanism read at contract-read time, a rung pointer line (B9-7's shape accommodates it
naturally), and R1 applies (any contract touch re-derives `vault-rule-card.md` against
the 8,000-byte budget). Consistent with — not a reversal of — Arc 9 Round 1's "no single
durable-host mechanism; the plumbing is per host." Skill assets remain overlay-less;
their durability story stays A10-6's detect-preserve-reapply. No general mechanism is
built this arc.

**Q3 — The A10-4/A10-5 joint format ruling. RULED (Round 2, 2026-08-21), both
halves.** *(a) Whether:* **general rule + census** — report-emitting verbs persist their
report **verbatim to a dated file under a config path**, symmetric with lint's existing
persist; the build runs the verb census (lint persists, upgrade digests; groom? decay?
setup?) and applies the rule everywhere it hits. Retention row declared in the same
build (Arc 8's retention-at-birth). *(b) Shape:* **plain `.yaml` under the report dirs,
with a declared lint-walker exclusion** — directly parseable, invisible to vault
machinery by design (reports are deliberately walker-exempt artifacts). The
acceptance-instrument variant (factory discharge reads the persisted file rather than a
hand-carried transcript) was presented and **not adopted** — available to a brief as a
brief-time question, not ruled here. Consumer-census evidence debt E1 attaches to
whichever build takes this (existing consumers of the current `.md` shape must be
walked: `vlt-lint/SKILL.md:72`, `report.md`, path docs). *(roundtable 2026-08-21 A12:
the lint-walker exclusion is declared by extending the existing operating-contract
Decay-contracts + zone-map rows — new report paths get rows in the same tables, per
retention-at-birth — never a new list (the second-home risk); and B10-6's brief states
the legacy-`.md` coexistence posture: existing files stay legal, no backfill sweep.)*

**Q4 — Sequencing of the inherited v0.13.0 half. RULED (Round 1, 2026-08-21):
interleaved, A10-6 early.** The spike-gating half is discharged (S1/S2/S3 all closed
2026-08-21, before ideation — Round 0). Sequencing: **A10-6 builds early; B9-6 is
briefed only after the A10-6 build lands** (the S3 dependency); B9-7 slots wherever
grouping puts it (S2 cleared it on cost); the A9-1 work is paced by its own size against
the harvest. Release cuts (incl. where v0.13.0 falls) are decided at grouping, not here.

**Q5 — Q6 inherited with A9-1** (Arc 9 archive `:1398`). **RULED (Round 5,
2026-08-21): the moot disposition is CONFIRMED.** Bounded/unbounded is the axis; no
workspace default-vs-opt-in question remains. Consistent with the S1 harvest (neither
field vault has a workspace concept; both built project containers on the
bounded/unbounded line).

**Q6 — Q7 inherited with A9-1** (archive `:1403`). **RULED (Round 5, 2026-08-21):
CONFIRMED at true cost — the whole series ships this arc, internally sequenced
model-first.** The owner's stated desire: ship it all together, with model-first as the
fallback if risk is high. Resolved on the clerk's risk read (risk is moderate and
concentrated in the live-vault relocation, not the design): the series lands **in this
arc as sequenced builds** — the container model + PARA parameterization first, then the
**move as the capstone build** carrying the `frontmatter` bump (from the version current
at brief time — the "@8 → @9" text was stale; see A2), the **nine**-consumer +
workflow-ack walk (version-handshake, re-ack same build), the relocation-migration
discipline (stub, worktree rule, re-point open dispatch pointers), and E6's census. A
slip strands only the capstone, never the model. **Fallback on record (owner,
Round 5):** if the capstone proves high-risk at brief time, it defers without
re-litigating the direction — the direction is ruled. *(roundtable 2026-08-21 A10,
owner-ruled: a fired fallback converts B10-11 + E6 into **bound** inherited debt — dated,
ship-verifiable re-check, gates the receiving arc; and a deferred capstone brief may not
cite S1 without a delta-check re-harvest first.)*

**Q7 — D7 inherited with A9-1** (archive `:1896`). **RULED (Round 4, 2026-08-21):
INHERIT, same build.** `grounding:` joins the `method_not_in_sources` /
`method_in_personalization` check family rather than inventing one, and the inherited
checks **ship in the same build that ships the field** — the
enforcement-ships-with-widening rule applied, honoring A9-1's own hard constraint (its
residual scope item 6). E5 (the `grounding:` laundering watch) is answered by this
ruling's mechanism — disposition recorded under Evidence-debt dispositions.

### Cross-filing decide-once rulings

**D1 — One lint-full repair or several? RULED (Round 3, 2026-08-21): ONE combined
build** — A10-2 + A10-7 + A10-3 land together as the lint-full signal repair: the
`convRead` read-list fix (+ `write-verification`), the tri-state Gap-B schema, the
coexistence-posture and callout-vs-bullet instructions, the `crossLayerSlugs` assembly
fix (shape per D2), and A10-7's general fan-out audit (every ask checked against the
convention set its scanner receives). **A10-1 stays a separate build** (different
instrument — `checks.md:47`, not the fan-out).

**D2 — Enumeration vs point-at-the-map for `crossLayerSlugs`. RULED (Round 3,
2026-08-21, on the clerk's recommendation): DERIVE + interim PARA line.** The glob set
derives from resolved `vault_structure` keys holding linkable notes (correct-by-
construction for `_agent/handoffs/`, `_agent/bases/`, and any vault-grown key), **plus
one explicit interim supplement line naming the PARA layers** — necessary because the
PARA folders are not designed parameters today (A9-1 grounding). The supplement carries
its own retirement: **the A9-1 build that puts PARA keys into `vault_structure` deletes
it in the same act** (enforcement-ships-with-widening; this is a bound cleanup in that
build's scope, and its brief must carry it — `binds:` at grouping). *(roundtable
2026-08-21 A7: the "correct-by-construction" claim is narrowed — `vault_structure` has no
`handoffs` key, so the supplement line names `_agent/handoffs/` alongside the PARA layers;
the shipped line carries its own retirement clause in-file (the B9-4 precedent:
slip-exposed interim postures live in shipped text); and if B10-10 folds past Arc 10, the
supplement retirement travels as **bound** inherited debt with a ship-verifiable re-check
— the B8-2(4) mechanism.)*

**D3 — A10-1's fix direction. RULED (Round 3, 2026-08-21): the repeat-aware report
line.** New candidates loud; unchanged repeats collapse to one quiet line with their
repeat count. No human act required — chosen against the field evidence (decline
mechanism live since v0.9.0; three runs, six repeats, zero declines). The per-candidate
decline path stays as-is; no batch-decline affordance is built. *(roundtable 2026-08-21
A3: repeat detection derives from vault record state — relay/backlog/archive — **never
from prior persisted reports**, keeping reports walker-exempt (Q3b's own premise) and
B10-3 out of E1's census by construction; the exact derivation is the brief's, and if
records prove insufficient the brief returns to the owner rather than silently reading
reports.)*

**D4 — A10-6's `--write` posture. RULED (Round 3, 2026-08-21): REPORT, never refuse.**
The write proceeds and the output lists every live-vs-source divergence
(`absorbed: [...]`-style) — loud, never blocking. Ruled on S3's finding that sanctioned
migration edits exist (the loop-profile lift's pointer line in a shipped partner's
SKILL.md), so a refusal would block legal states. The core fix stands as grounded: hash
source-tree content for source-provenanced paths, live only where no counterpart
exists. S3's flagged tension (a sanctioned lift edit becomes standing reported
divergence) is the A10-6 brief's to resolve within this posture. *(roundtable 2026-08-21
A4: the posture is widened one sentence — a sanctioned migration edit records itself in
the same act that makes it (zero-ritual, D6's declare-at-birth pattern; A10-1's field
evidence is the bound — per-item rituals go unused), so `absorbed:`/`diverged` report only
unsanctioned divergence, with sanctioned entries excluded-and-denominated ("N sanctioned
divergences: <paths>"); the brief may instead choose elimination — stock converging to
the pointer shape — if reachable.)*

**D5 — A10-8's amendment channel. RULED (Round 4, 2026-08-21): the re-triage label.**
An owner-applied `amended` label admits a comment *(roundtable 2026-08-21 A13: the
"re-applied `vault-accepted`" alternative is struck — that label's defined-once meaning is
the materialization trigger, and a re-application is invisible to the existing query
shape)*;
intake gains one extra query leg; the amendment **appends to the existing filing, never
re-materializes**. Keeps A15's cost discipline (an unadmitted comment costs the factory
nothing) and the owner's curatorial gate. The contract-text obligation ships with it:
the state-flow table gains the amendment verb, and the issue templates tell filers
plainly that comments reach the factory only via the label. The build touches both
sides of the factory/shipped seam (intake mechanics gitignored; contract/templates
shipped). No comment-scan is built; the watch on amendments-going-unnoticed was not
separately adopted.

**D6 — A10-9's shape. RULED (Round 4, 2026-08-21): BOTH halves.** Declare-at-birth —
`module.yaml` declares module-level dependencies (`gh`, `uv`); the mint/capability
ceremony records vault-grown tool dependencies at their birth moment; one retroactive
census covers what's already born — **plus** check-at-arrival: `vlt-setup`/`vlt-upgrade`
probe the declared set and **report, never gate**, generalizing `vlt-feedback`'s
`gh-missing` named-error + degrade pattern. The halves are complementary by
construction: the declaration is the record the check reads. Stands alone as a build
(not folded into A10-6); grouping assigns it.

**D7 — The K9 drive-by. RULED (Round 1, 2026-08-21): drive-by.** The one-line
`skills/vlt-mint/assets/capability-template.md:23` fix rides the first convenient build
rather than waiting on the A9-1 work — which build carries it is assigned at grouping.
Ruled with the S1 harvest in view: the enum-in-comment defect class was found live at
its template origin in the field (`vlt-sayari`'s session-digest template).

### Spike obligations

*Each carries SPIKE OPEN until a dated SPIKE CLOSED record replaces it in this section.*

**S1 — The PARA container harvest (A9-1, K13). SPIKE CLOSED 2026-08-21** (clerk;
read-only over both vaults, no contract text drafted — K13's bound honored). Full
harvest: `skills/reports/spike-s1-para-container-harvest-2026-08-21.md`. Headline
findings: **the A9-1 thesis is field-proven in both directions** — `app-vault` broke the
location rule to get an honest in-PARA container (`projects/<slug>/index.md`,
`author: hybrid`, container-level `status:`), while `vlt-sayari` *obeyed* the rule and
its container **fled to a shadow tree in the agent zone**
(`_agent/projects/<name>/{charter.md, status.md}`, 10 charters, nested sub-containers;
PARA files cite it via `personalization_sources:`). Convergent model both vaults built
independently: charter (stable frame) + dated running record (+ decision/question
register with decider·pick) as **2–3 files, not one index**; numbered evidence ledgers;
bidirectional project↔project dependency tables; portfolio nesting ("umbrella",
2–3 levels). Defects quantified: 142/210 sayari files no frontmatter, 25 distinct
`status:` values (≥8 vocabularies, changelogs stuffed into the field), ~12/210 ever
terminal (K7/K8 at scale), `resources/` vestigial in both vaults (K3/K6),
`verified_by:` on 1/210 vs a hand-rolled `trust:` lifecycle on 37, K9's enum-in-comment
found at its template origin, and a **confidentiality-as-container-attribute** boundary
the module has no field for. New model candidates the filing didn't name: the
decider·pick register (with verification + assignment queues), the standing-feed
evidence ledger, propagation-debt tracking. Q6 note: neither vault has a `workspace`
concept; Q7 note: the wiki-into-resources move matches the field (resources/ already
vestigial). **A9-1 is clear to ideate/brief against the harvest.**

**S2 — Boot-cost of the fleet-wide rung (A9-5/B9-7). SPIKE CLOSED 2026-08-21** (clerk,
factory-side; measured against `skills/reports/cost-baseline-2026-07-29.md` + live
`vlt-core` reflexes files). *Shape priced* (per Q8's ruling: a vault-scoped
`reflexes.md` sibling, agent zone, pointer lines only, hard-capped, cap/falsifier/posture
in its own frontmatter — the contract's rule-layer shape). *Field data:* vlt-core's nine
per-partner `reflexes.md` run 411 B–5.1 KB (frontmatter alone ≈ 0.4 KB, ~9 lines incl.
`cap: 30`; researcher at 31 lines = 5.1 KB). *Rung cost bands* (both baseline estimators,
against the ~48.3–49.8 KB / ~9.4K–12.4K-token per-activation eager boot):
**birth** (vault has zero overlays today — vlt-core's live state) ≈ 0.4–0.5 KB, ~100–150
est. tokens, **+~1%** of eager boot; **plausible steady state** (~10 pointer lines ≈
1.2–1.3 KB) ≈ ~300–420 tokens, **+~2.5%**; **cap-full worst case** (30 pointer lines ≈
2.9 KB) ≈ ~700–950 tokens, **+~6%**. Paid at *every* partner activation (fleet-wide,
always-loaded), but bounded by the cap and noise against Beat-2 variable reads
(`_agent/log.md` alone is 151 KB). *Verdict for the brief:* cost does **not** trigger
A17's pre-ruled negative branch — the rung is affordable at cap; B9-7 is clear to brief
on cost grounds.

**S3 — `vlt-upgrade` Step-3 / Step-3.6 ordering trap (A9-3/B9-6). SPIKE CLOSED
2026-08-21** (clerk, factory-side; real read of `skills/vlt-upgrade/SKILL.md`,
`skills/vlt-setup/SKILL.md:153`, `skills/vlt-setup/scripts/verify-skill-manifest.py`).
**Both claims CONFIRMED — and the trap is a special case of A10-6.**
*(a) The ordering trap is real and in-skill reachable.* The order holds: Step 2 refreshes
shipped files; Step 3's reconcile runs; Step 3 item 6 ("Step 3.6") hands off to
`vlt-setup`, whose provision runs `verify-skill-manifest.py --write`
(`vlt-setup/SKILL.md:156`) — and `compute_manifest` hashes the **live** tree
(script `:85`, `:90`, `:102`). Any edit to a manifested file landing between the Step-2
refresh and the item-6 write is recorded as stock. Two sanctioned in-skill writers can do
exactly that: the **loop-profile relocation** (Step 3 item 5) lifts a profile out of an
installed partner's SKILL.md leaving a pointer line — for a *shipped* partner that edits
a manifested file mid-upgrade; and **write-through** (Step 3 item 7) can edit "a skill's
stated rule." Both human-gated, both then silently blessed.
*(b) The B7-2 manifest analysis holds.* `.claude/hooks/` is in the net (script
`EXTRA_DIRS = ("workflows", "hooks")`, basenames from the shipped assets trees), and the
structural walk covers whole shipped skill trees incl. `references/`/`scripts/`
(`vlt-setup/SKILL.md:153` states it as a worked consequence — note for the C6-d carry:
that debt looks already discharged by B7-2's walk; not this spike's to disposition). The
filing's "detection is not preservation" and one-time-tail claims stand — with the A10-6
caveat that detection itself lasts only until the next `--write` absorbs the edit.
*Consequences for ideation/brief:* (1) the fix is **A10-6's fix** — hash source-tree
content for source-provenanced paths; that makes step order irrelevant, so B9-6's brief
should **depend on the A10-6 build, not fix ordering separately**. (2) A tension the
A10-6 build must rule on: the loop-profile lift's pointer line becomes *permanent
reported divergence* under source-hashing — a sanctioned migration edit needs a home in
the manifest posture (the migration targets "installed `vlt-agent-*` partners," which
includes shipped ones).

**No new spikes ruled** (Round 6 close): none flagged by capture, none demanded by the rulings — the slot closes empty.

### Evidence-debt dispositions

*(each debt attached to a build, or ruled not-blocking, per build)*

**E1 — A10-5's consumer census. ATTACHED (Round 2, via Q3)** to whichever build takes
the report contract: the consumer set of the current `.md` report shape, **re-derived
against live source at B10-6 brief time** (starting from `vlt-lint/SKILL.md:72`,
`report.md`, path docs, and explicitly including any reader added by B10-1..B10-5 — the
hand-saved v0.13.0 Step-4 report file included), must be walked before the `.yaml` cut,
including verifying the `lint-debt` counter truly derives from the session log, not
reports. *(roundtable 2026-08-21 A6: reworded from a fixed enumeration — the
lists-that-claim-completeness class.)*

**E2 — A10-4's verb census. ATTACHED (Round 2, via Q3)** to the same build: which verbs
report-and-discard vs report-and-persist (lint persists, upgrade digests; groom? decay?
setup?) — the census is the build's first act, and the general persist rule applies
everywhere it hits.

**E5 — the `grounding:` laundering watch. DISPOSITIONED (Round 4, via Q7):** answered by
the inherit-the-family ruling — `grounding:` ships with the firewall check family in the
same build as the field; the laundering channel is closed by construction, not watched.

**E6 — the attestation-census pattern (K16). RULED (Round 5, 2026-08-21): ships with
the move.** The census/staleness posture is designed and shipped **in the same build as
the wiki move** (Q6's capstone) — enforcement-ships-with-widening, attached as a binding
evidence debt on that build.

### Questions deliberately left to brief time

**Confirmed at Round 6** — per-build, as ruled:

- **B10-4:** which of the A9-3 directions (1/2) lands on top of the direction-3 floor
  (Arc 9 A21; S3 informs the choice).
- **B10-6:** the acceptance-instrument question (does factory discharge read the
  persisted report file) — presented Round 2, not adopted, open to the brief.
- **B10-10:** the three questions inherited with A9-1 (Arc 9 Round 1) — whether
  `areas/`-as-ideation-home (K3) survives contact with the S1 harvest (harvest note:
  app-vault has zero areas, vlt-sayari has 8 — "areas unused" is not universal);
  the exact per-type PARA `status:` enumerations (the *that* is ruled into B10-10's
  scope; the *values* are the brief's, against the harvest's 25-value evidence);
  the project-to-project relation shape (K11 — the harvest found four hand-rolled
  relation kinds: membership, dependency, supersession, containment).
  *(roundtable 2026-08-21 A11: plus the S1 harvest's unadopted candidates as explicit
  adopt/decline/watch calls, none silently dropped — the
  confidentiality-as-container-attribute boundary (owner-ruled brief-time; **Maya's
  dissent on record**: without the field the shadow tree cannot repatriate, and
  `grounding:` in the same build raises leak pressure on exactly the confidential
  containers), the `trust:`-vs-`verified_by:` fork (37 hand-rolled vs 1 stamped in 210
  files), the decider·pick register, the standing-feed evidence ledger, and
  propagation-debt tracking — and one added question: where does a vault-grown
  type/template declare its per-type status vocabulary (D6's declare-at-birth is the
  copyable shape).)*
- **B10-11:** exact `type:` value migration for retired `resource` pages, and the
  census/staleness posture's concrete check shapes (E6).
- ~~the K9 template fix~~ — **D7 ruled it a drive-by (Round 1); rides B10-1.**

## Roundtable review — Arc 10 batch B10-1..B10-11 (2026-08-21)

**Convened** over the filled Ideation rulings above (`roadmap-roundtable`). Roster: Mary
(analyst), Winston (architect), Amelia (dev), John (PM), Paige (tech writer), Sally (UX),
Carson (brainstorming), Dr. Quinn (problem-solving), Maya (design thinking), Victor
(innovation strategy) — Caravaggio and Sophia excused by the owner; ~50 raw findings
merged to 15 joints. Owner's pre-seeded joint (the v0.13.0 mid-arc cut) answered: forward
dependencies compose safely; every fault found runs the other way — cut builds
pre-deciding or newly consuming surfaces ruled post-cut, and cut-time evidence outliving
its window. Session file:
`_output/party-mode/2026-08-21-arc10-roadmap-roundtable-session.md`.

**Amendments applied (all landed in-session, dated markers in place):**

- **A1** — interim evidence posture for the v0.13.0 discharge (owner hand-saves the
  Step-4 report; B10-6 retires it) → release line + ledger preamble. *(7 voices)*
- **A2** — frontmatter arithmetic repaired: relative bump wording (source already at @9;
  B10-4 carries the in-cut A22 @9→@10; capstone expected @10→@11); "seven-plus" → nine +
  workflow-ack; **owner-ruled:** the grounding:/type-retirement bump fires with whichever
  of B10-10/B10-11 ships first → Q6, B10-4, B10-10, B10-11. *(8 voices)*
- **A3** — D3's repeat detection derives from vault records, never prior reports → D3.
- **A4** — D4 widened: sanctioned edits record themselves at sanction time (zero-ritual);
  `absorbed:`/`diverged` report only unsanctioned divergence → D4.
- **A5** — B10-1 closes the live-as-source and version-skew escape paths; two new
  acceptance fixtures → B10-1.
- **A6** — Q3 bindings for the cut's new persisted surfaces (B10-1 `absorbed:` list,
  B10-4 metric home); E1 reworded from enumeration to brief-time derivation → B10-1,
  B10-4, E1.
- **A7** — D2 narrowed honestly: supplement names `_agent/handoffs/` + PARA layers
  (no `vault_structure` key under C6-b); retirement clause in shipped text; fold
  contingency = bound inherited debt (B8-2(4) mechanism); qualifying-key predicate
  single-homed → D2, B10-2.
- **A8** — B10-2 ships the write-verification handshake same build (consumers: + E5 ack)
  and version-markers on restated prompt instructions; B10-4/B10-11 walks re-derive
  marked restatements → B10-2, B10-4.
- **A9** — B10-5's rung writer population worded non-enumeratively with a contract-overlay
  fixture check; B10-5 joins B10-9's binds → B10-5, B10-9.
- **A10** — Q6 fallback bounded: a fired fallback converts B10-11 + E6 to bound inherited
  debt (ship-verifiable re-check, gates the receiving arc); deferred capstone requires an
  S1 delta re-harvest; **owner-ruled cadence:** B10-11 ships as its own cut
  (B10-10-without-B10-11 a legal interim state) + declared fold order B10-7/8/9 before
  B10-10/11 → Q6, release line.
- **A11** — B10-10's brief-time questions gain the S1 unadopted candidates as recorded
  adopt/decline/watch calls + the vault-grown status-vocabulary question → brief-time
  questions.
- **A12** — Q3b's walker exclusion declared by extending the existing Decay-contracts +
  zone-map rows, never a new list; legacy-`.md` coexistence posture stated → Q3.
- **A13** — D5's "(or re-applied `vault-accepted`)" struck; contract scope includes the
  `amended` label row + "Seven labels" count fix → D5, B10-7.
- **A14** — filer honesty note rides B10-1 as a drive-by; B10-7 templates state the
  affirmative move (comment + @mention) → B10-1, B10-7.
- **A15** — B10-9 rules the rule card's posture under overlays (pointer line or recorded
  exemption) → B10-9.

**Rule declared:**

- **R4** *(the fan-out currency rule; continues the R1–R3 series)* — **any ask that
  enforces a convention's rule adds that convention to `convRead` and to the workflow's
  ack in the same edit; any edit to an ask or the read list re-runs the fan-out audit;
  restated instructions carry `per <convention>@N` markers that consumer walks re-derive.**
  Named home: the `vlt-lint-full.js` ack header block + one line in
  `vlt-lint/references/full-scale.md`. The home's edit is itself B10-2, so this dated
  declaration is the interim carrier: until B10-2 lands, R4 binds briefs via this record;
  B10-2's audit is R4's retroactive first run, not the fix itself.

**Owner rulings (4, live):** bump home = whichever-ships-first (T2); cadence = both
commitments (T10); confidentiality = brief-time adopt/decline (T11) — **dissent on
record (Maya):** without the field in B10-10's scope the shadow tree cannot repatriate
and `grounding:` raises leak pressure on the confidential containers; evidence gap =
interim hand-save line (T1; John's pull-forward declined as the larger change).

**No OPEN disputes.** Out-of-scope material for `inbox/` filing (Carson): (1)
detect-preserve-reapply lacks an instrument for its third verb — divergence evidence
never becomes a checkable re-apply worklist; (2) the field contract never states when a
captured issue's comment window ends (close-at-archive shuts issues silently).

**Keepsake:** `_output/party-mode/2026-08-21-arc10-roadmap-roundtable.html`.

## Capture addendum — 2026-08-22 (mid-arc)

*Six filings grounded against v0.13.0 @ `a3ec505` + working tree, folded under the
mid-arc posture (platform P-4): unbuilt builds only, per-filing addendum rulings made by
the owner in-session (this run, 2026-08-22 — four AskUserQuestion rulings, all landing on
the clerk's recommended routes). Intake context: this run was the github-intake's second
live pass — issues #4–#7 (all `rail_contract: 1`, current; all `vault-accepted`) were
materialized into the four `2026-08-21-1502xx-*` filings below and labeled `captured`;
#1–#3 were already on disk and consistent. Through-line note: the batch extends the arc's
signal-integrity story rather than bending it — four of six are the instruments' own
report/record contracts failing honesty (A10-10..A10-11, A10-14), and the other two are
closed enumerations in the governance record with no value for a legitimate real case
(A10-12..A10-13) plus the rail's own triage residue (A10-15). No joint moved anywhere in
the batch — no roundtable delta convenes.*

### A10-10. Reconcile wiki-index.md's row-format rule with its worked example (2026-08-21) — …-150212-wiki-index-row-format-rule-contradicts-worked-example.md · origin: mggower/bmad-module-vlt#4

**CONFIRMED — defect, rail-materialized (issue #4, `captured`).** The contradiction is
verbatim in shipped source:
`skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md:64` — "Each page is
one list item: its wikilink, optionally a terse **structural tag**. **No description, no
source count, no date.**" — against the worked example at `:68`, whose hub row carries
`— how grind, time, and pressure shape a cup, split by speed`, a description by the
prose's own definition (the structural-tag bullet at `:74` defines the only permitted
suffix as a one-or-two-word axis label, and `hub` already occupies that slot in the same
row). Grounding sharpened two things past the filing: **(1)** the convention is at
`version: 2` with **three** consumers — `consumers: [vlt-ingest, vlt-lint,
vlt-lint-full.js]` (`wiki-index.md:12`; B10-2 registered the workflow) — so either
resolution's `version:` bump walks three, not the filing's two. **(2)** Enforcement is
not absent: `vlt-lint/references/checks.md:35` (index drift, both modes) states the index
"carries no descriptions, source counts, or dates" — lint's own text sides with the
**prose**, while the example teaches the opposite, so the ambiguity is live inside a
shipped check, not merely between writer and validator. The filing's two resolutions
(example-is-right: bound a permitted short description; prose-is-right: rewrite the
example + stated migration + lint flag) carry to Arc 11 ideation unresolved.

- **Ruled into:** hold for Arc 11 (owner, 2026-08-22) — no unbuilt B10 build squarely
  owns the wiki-index convention; B10-11 ride-along and a B10-6 stretch were both
  declined. Captured-unrouted; routes at Arc 11 ideation.
- **Joint test:** joint moved: none (nothing enters the ruled batch).

### A10-11. Produce `high_value_gaps` in the full-mode fan-out, or make "unmeasured" expressible (2026-08-21) — …-150213-high-value-gaps-declared-field-has-no-producer.md · origin: mggower/bmad-module-vlt#5

**CONFIRMED — defect, rail-materialized (issue #5, `captured`); not superseded by
B10-2.** Re-derived against the post-B10-2 tree: the identifier `high_value_gaps` has
exactly one tree-wide occurrence, its declaration
(`skills/vlt-lint/references/report.md:61`, annotated `# full mode`); the full-mode
fan-out — now at `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — has no
gap-candidate field in the PAGE_SCAN schema (`:106-137`), does not ask for one in the
scan prompt (`:173-174`), and computes none in the reduce/assemble step (`:368` ff).
B10-2 rebuilt exactly this workflow's signal paths (Gap B tri-state, convention reads)
and left this slot untouched — it was outside B10-2's ruled scope (A10-2/3/7), so the
filing survives the rebuild intact. The declared field remains structurally unfillable in
the only mode that requires it; a full sweep can only misread as "no gaps" or "measured,
none found" when the truth is "never measured". The filing's three resolutions (implement
/ retire / make-unmeasured-expressible) carry to brief time; option 3 aligns with the
module's never-omit posture and generalizes (the same misread class as A10-14's absent
line, one layer down).

- **Ruled into:** build B10-6 (unbuilt) (owner, 2026-08-22) — the report-contract build's
  census and format ruling extend to the lint report schema's unfillable field; the brief
  rules produce/retire/unmeasured-marker.
- **Joint test:** joint moved: none — scope-internal to the report contract; no
  cross-build dependency, ordering, or interim posture changes.

### A10-12. Give a shipped write op a route to the decision log — the writer roster admits no discovery site (2026-08-21) — …-150214-decision-log-writer-roster-admits-no-discovery-site.md · origin: mggower/bmad-module-vlt#6

**GAP CONFIRMED — candidate, as filed (rail-materialized, issue #6, `captured`).**
Verified whole: the Writers roster
(`governance/_meta/conventions/decision-log.md:76-80`) names exactly three ops
(`vlt-mint` ceremonies, `vlt-upgrade` write-through, `vlt-lint` write-through), matching
`consumers: [vlt-mint, vlt-upgrade, vlt-lint]` (`:12`); grep of `skills/vlt-ingest/` for
any decision-log reference returns nothing; no shipped text states what a non-writer op
does with a deviation it surfaces. One staleness note: the convention has moved to
`version: 2` since the filing's 0.12.0 snapshot (verdict-provenance, v2) — the gap is
unchanged by it. The filing's own framing stands: nothing shipped is self-contradictory;
the silence is the gap. Its two resolutions (widen the roster + bump-and-walk / state the
hand-off with a named route) plus its noted third shape (B9-4-style checked registration
for write authority) carry to Arc 11 ideation unresolved. Pairs with A10-13 — same file,
same closed-enumeration shape, one `version:` bump if built together.

- **Ruled into:** hold for Arc 11 (owner, 2026-08-22), paired with A10-13 as a natural
  single build — no unbuilt B10 build touches `decision-log.md` (the B10-8
  mint-ceremony adjacency was declined as a weak fit).
- **Joint test:** joint moved: none (nothing enters the ruled batch).

### A10-13. Add a `kind:` value for a scoped deviation — forcing it to `convention-edit` mis-scopes the reconcile pass (2026-08-21) — …-150215-decision-log-kind-has-no-value-for-scoped-deviation.md · origin: mggower/bmad-module-vlt#7

**GAP CONFIRMED — candidate, as filed (rail-materialized, issue #7, `captured`);
mis-scope mechanism verified end-to-end.** The enum
(`governance/_meta/conventions/decision-log.md:39`) is six values, all presupposing the
governed object changed; `kind:`'s machine-key role is stated at `:46`; the
`convention:` delta line is defined "convention-edit ONLY — the version delta" (`:43`),
so the observed workaround (a deviation logged as `convention-edit` with `convention: …
unchanged`) uses a required field against its definition, exactly as filed. The
downstream half checks out too: `vlt-upgrade/SKILL.md:78`'s decision-log reconcile scans
gated `convention-edit`/`upgrade-ruling` entries for a missing accounted-for superseding
entry — a mis-classed deviation enters that scan and surfaces as perpetually
unreconciled, since no superseding entry can ever exist for a convention that never
changed. The filing's two resolutions (add a `deviation`/`ruling` value with a stated
reconcile relationship / declare `convention-edit` covers it and define the `unchanged`
idiom) carry to Arc 11 ideation; either way the reconcile pass's scoping rule should name
its matched classes. Same-build pair with A10-12.

- **Ruled into:** hold for Arc 11 (owner, 2026-08-22), paired with A10-12 (one
  `decision-log.md` edit, one `version:` bump, one three-consumer walk).
- **Joint test:** joint moved: none (nothing enters the ruled batch).

### A10-14. The 0.13.0 Step-4 report omitted the mandatory `manifest_write_divergence:` line (2026-08-21) — …-164445-step4-report-omits-manifest-write-divergence-line.md

**CONFIRMED — defect, acceptance-surfaced (B10-1 check (5) FAILED, this arc's own
discharge run).** The source contract is intact: `vlt-upgrade/SKILL.md:106` carries the
`manifest_write_divergence:` schema line with "never omitted when empty"; the first live
report under it (the A1 hand-saved
`skills/reports/2026-08-21-vlt-core-upgrade-0.13.0-step4-report.md`) jumps
`skill_asset_divergence: []` → `migrations_run:` with the string absent — an
**emitter-honesty defect**, not a source omission. The filing's not-broken boundary
holds: the ledger digest records the source-hashed write (`source_mode: source`, 67
entries, all divergence slots empty), and the Notes-line (`SKILL.md:138`) is
when-non-empty, conforming. The candidate direction (make mandatory lines structurally
unskippable — schema-derived emission, or package-lint/fixture assertion on a rendered
report) carries to the B10-6 brief. Re-discharge evidence stays as the filing states: a
future upgrade's Step-4 report carrying the line, empty or not.

- **Ruled into:** build B10-6 (unbuilt) (owner, 2026-08-22, confirming the discharge
  annotation's "natural home" at the ledger's B10-1 entry) — B10-6 gains the
  unskippable-mandatory-lines clause alongside its persist/format rulings.
- **Joint test:** joint moved: none — scope-internal to the report contract.

### A10-15. Rail-triage residue on shipped surface — three candidates from P-1's boundary cuts (2026-08-21) — …-181500-rail-triage-arc-surface-candidates.md

**ALL THREE CONFIRMED — candidate batch, owner-filed (factory-observed, no issue).**
**C1 (verdict-label widening):** the field contract's label table
(`skills/vlt-feedback/references/field-contract.md:54-69`) admits accept/decline as the
only triage outcomes — needs-info, duplicate, and a decline-reason taxonomy exist only in
P-1's comment prose, invisible to `gh` queries. **C2 (issue-form 1:1):** the forms
(`.github/ISSUE_TEMPLATE/field-defect.yml`, `field-pattern-candidate.yml`) carry the
eight payload fields but the shared pattern/candidate form cannot branch labels (noted in
the contract's own table) and no field asks for `file:line` grounding. Both are
surface-identical to unbuilt **B10-7's already-ruled scope** — the `amended` label row +
"Seven labels" count fix (roundtable A13) and the issue-template comment-truth statement
(A14) touch exactly this table and these templates; one `rail_contract` evolution-rule
check (label additions additive) covers the whole set. **C3 (voice-rule single-homing):**
the duplication is real — `vlt-feedback/SKILL.md:77-79` (the approval gate) and the
factory's `issue-triage/SKILL.md:19-20` ("The agent never writes to the public tracker
unapproved") — but the second home is a **factory** skill, so single-homing in the
operating contract is half-shipped/half-factory work, weaker-fit for a shipped build's
scope.

- **Ruled into:** C1+C2 → build B10-7 (unbuilt) (owner, 2026-08-22) — B10-7's contract
  amendment additionally widens the triage verdict vocabulary and evolves the forms
  toward triage-ready filings, under its existing evolution-rule check. C3 → hold for
  Arc 11.
- **Joint test:** joint moved: none — C1+C2 are scope-internal widening of B10-7's own
  contract-text and template surfaces; no cross-build dependency or ordering changes.

## Capture addendum — 2026-08-22 (mid-arc, second exercise)

*Two filings grounded against branch `arc10-v0.14.0` @ HEAD `7a4b1a8` (B10-6..B10-11 all
built), folded under the mid-arc posture (platform P-4, second exercise — the A10-10..A10-15
addendum above is the shape precedent). Both filings descend from one event: the failed
B10-2(5) discharge attempt, the first full-mode lint on vlt-core post-0.13.0 (evidence:
the relayed vault handoff `<vault>/_agent/acceptance/2026-08-22-vlt-0.13-lint-full-defect.md`,
vault read-only throughout). The filings were written against v0.13.0 @ `a3ec505` with
factory grounding at `aba700c`; this capture re-grounds at `7a4b1a8`, where B10-10/B10-11
have since touched the same workflow (`// depends_on:` ack now `frontmatter@13`, both
`:173` inline markers re-stamped, the attestation census added to the reduce) — any fix
lands on the post-B10-11 file. GitHub intake ran first: all seven open `vault-accepted`
issues already carry `captured` and are consistent on disk; the `amended` query returned
empty — nothing materialized, nothing held. **Owner ruling this session (2026-08-22,
per-filing addendum ruling, verbatim intent: "the full lint failure is a release blocker.
two new filings were added which need to escalate a mid-arc fix"):** both filings
**ESCALATED** into a new unbuilt build **B10-12**, **release-blocking** — briefed and
built before any v0.14.0 release cut. Unlike the first addendum, this batch is not
scope-internal: see the joint test at the end of this addendum.*

### A10-16. `vlt-lint-full` is non-executable at 0.13.0, and the total failure renders as a clean vault (2026-08-22) — …-130455-lint-full-nonexecutable-and-vacuous-clean-report.md

**CONFIRMED ×2 at HEAD — defect pair, acceptance-surfaced (B10-2 check (5) FAILED, this
arc's own discharge run); the second defect is the release blocker.** **Defect 1
(non-executable):** the `PAGE_SCAN` schema literal
(`skills/vlt-setup/assets/workflows/vlt-lint-full.js:102-133`) is **byte-identical across
`a3ec505` → `aba700c` → `7a4b1a8`** — exactly **4,266 chars**, as the filing grounded
(4,100 JSON-serialized); B10-10 and B10-11 left every scanner schema and prompt byte
untouched (their briefs' R4 no-change claims verified here by byte-identity), so the
harness-classifier rejection (145/146 agents dead pre-read; the lone survivor the
order-of-magnitude-smaller `INDEX_SCAN`) carries to HEAD unchanged. Site corrections at
HEAD: `pageScanPrompt` is now `:172-174` (the filing's `:166-169` was the pre-B10-10
position); the near-duplication observation holds — the schema descriptions (`:106-131`)
restate the prompt's semantics. The filing's open question carries verbatim: fixed limit
B10-2 crossed vs. moved harness-side limit — the answer decides one-time trim vs. a
standing schema budget the workflow respects as it grows (package-lint-enforceable), and
the fix must land as a deliberate source change, never a runtime reshape. **Defect 2
(vacuous clean report):** all three mechanism sites confirmed at HEAD — `:195`
`scans.push(...part.filter(Boolean).filter((s) => s.available !== false))` verbatim (line
number unmoved; `parallel()` resolves a failed agent to `null`, silently dropped; zero
scans and zero problems are the same downstream state); the budget guard (`:187-192`) is
still the **only** guard that pushes a coverage cap for scan shortfall — agent failure has
no equivalent (the overlay loud-degrade posture to mirror sits at `:180-184`);
`files_checked: scans.length` moved `:380` → **`:393`** (B10-11's attestation-census
block shifted it), and nothing asserts on it. **New at HEAD, sharpening the filing:**
B10-11's `attestation_census` denominates over `scans` too (`:383`
`pages_total: scans.length`) — under total shortfall the census renders `pages_total: 0`,
a fourth face of the same silent-shortfall defect any fix must cover. Candidate
directions carry as filed, endorsed on grounding: (1) shortfall → coverage cap naming
count + reason at the reduce boundary; (2) `scans.length === 0` → error, never a
findings report; (3) consumer-side defence — `vlt-lint` SKILL refuses to persist or
advance `lint-debt` on `files_checked: 0`. The suggested follow-up audit also carries
(no prior release signed off on a vacuously-empty full-lint report — 2026-08-14/-16 look
genuine, exposure window 0.12→0.13).

- **Ruled into:** build B10-12 (new, unbuilt) (owner, 2026-08-22) — the mid-arc fix
  build, **release-blocking**; both defects in one build (the filing's own framing:
  filed together because the second makes the first dangerous rather than inconvenient).
- **Joint test:** **joint moved** — see the addendum joint test below.
- *(roundtable delta 2026-08-22 DA10, roster-converged — ✅ **owner-ruled 2026-08-23, batch**)* The
  suggested follow-up audit is **DISCHARGED at capture**: A10-17's era grounding is its
  evidence — both exposure-window reports (2026-08-14-1336, 2026-08-16-1118) verified
  genuine with real content and no existing-wiki-page class; no audit obligation
  carries into B10-12.

### A10-17. Full-lint `missing_targets` flags existing wiki pages (2026-08-22) — …-130456-lint-missing-target-false-positives-existing-pages.md

> **Superseding note (2026-08-22, post-capture):** the source filing was WITHDRAWN by its
> author the same day (file deleted from `inbox/`) — the author's retraction reached the
> same conclusion this capture's grounding did (the six flags were fabricated by the
> `:208` scans-derived existence set, not a `normalizeTarget`/`crossLayerSlugs` seam) and
> its content was folded into `…-130455`, which now carries the `:208` mechanism as its
> grounded Defect-2 third mechanism. This capture entry stands as the record; the scope
> travels in B10-12's leg 3 unchanged. No filing archives at closeout under A10-17 — its
> acceptance evidence rides `…-130455`'s.

**CONFIRMED — the false-positive class is real; the mechanism is REATTRIBUTED by
grounding, and the filing's era question is RESOLVED at capture.** All six flagged
targets verified on disk as vlt-core wiki pages (`_agent/wiki/{drake-maye,
new-england-patriots, nfl-2026-offense-rankings, nfl-2026-player-outlook,
nfl-player-trajectory-eval, run-pass-option}.md`). The filing's suspected seam
(`normalizeTarget`/`crossLayerSlugs`) is not the likely mechanism: `slugSet` is built
from **surviving scans**, not the input page list (`vlt-lint-full.js:208`
`const slugSet = new Set(scans.map(nslug))`), and a target flags as missing when absent
from slugSet ∪ crossLayer ∪ stubs (`:220`). In the degraded run slugSet held exactly one
member (`a-j-brown`), so every wikilink from the surviving page to any other wiki page
necessarily flagged — and `crossLayerSlugs` (691 entries, passed externally) cannot
rescue them, because wiki pages are by design not in the cross-layer set. The six false
positives are thus a **consequence of A10-16's silent shortfall** — a further face of the
same defect: a dead agent silently deletes its page from valid-target space, corrupting
even the surviving scanner's findings (the same scans-derived denominator also feeds the
cluster-pass slug enumeration at `:270` and the name-callout adjudication gate at
`:340`). **Era RESOLVED** by the filing's own suggested cheap step: the genuine pre-0.13
reports show no existing-wiki-page class — 2026-08-14
(`{lint_reports}/2026-08-14-1336-lint.md:8`) adjudicated `missing_targets: []` with all
20 targets resolving on disk; 2026-08-16 (`…-1118-lint.md:9`) had 7 fan-out flags, all
the since-fixed A10-3 zone-omission class (bases/areas/handoffs — none of them existing
wiki pages). The seam does not predate 0.13; the class folds into the same fix family as
A10-16, not its own build. Residual, honest: one page of evidence from a degraded run —
a residual `normalizeTarget` seam cannot be excluded until an executing full sweep;
B10-2(5)'s re-discharge sizes or collapses the class, exactly as the filing states.

- **Ruled into:** build B10-12 (new, unbuilt) (owner, 2026-08-22) — same build; the
  grounded mechanism (valid-target space derived from surviving scans, `:208`) is
  B10-12's third leg alongside A10-16's two defects.
- **Joint test:** rides A10-16's — below.

### Addendum joint test + release posture (owner ruling, 2026-08-22)

Unlike the first addendum's "no joint moved anywhere in the batch", **this batch moves a
joint**: B10-12 is a **new build entering the ruled batch**, and the owner's
release-blocker ruling changes the release ordering and interim posture — v0.14.0
(pre-called as B10-6..B10-10, with B10-11 its own cut) is now **blocked on B10-12**
being briefed and built first. That is exactly the class of joint
(`roadmap-roundtable`'s frame: cross-build ordering, interim posture) the P-4 rule says
convenes a roundtable **delta** before the affected build's brief. **The roundtable-delta
question is flagged for owner confirmation, not waived:** either the delta convenes over
B10-12 before its brief, or the owner records an explicit waiver here — `build-brief`
gates on this record either way. (Capture's read, for the owner's decision material: the
delta's surface is narrow — one new build, one workflow file, a re-ordered release gate —
but the release-blocking posture is precisely the kind of joint the room exists to
pressure-test.)

*(roundtable delta 2026-08-22 DA3, roster-converged — **✅ OWNER-RULED 2026-08-23:
posture CONFIRMED; the flagged owner action is discharged by CHANNEL RULING — the
known-issue notice lands in the **v0.14.0 release notes / CHANGELOG entry**, not a pinned
tracker issue. The owner ruled the exposure window too short to warrant a standalone
public warning (v0.14.0 carries the repair and is release-ready), and the CHANGELOG is
the durable record. **Release-time obligation:** `vlt-release` Stage 3 authors the
CHANGELOG `## v0.14.0` entry — the notice text must be included there, and the entry is
where DA3 is finally retired.**)* **Interim
field posture until the B10-12-bearing cut is installed:** full-mode lint on 0.13.x is
**untrusted** — the owner runs no full-mode sweep on a 0.13.x install (standard/scoped
mode is unaffected), and any existing full-mode report is read against its
`files_checked:` line before belief (a shortfall unexplained by a coverage cap voids
it — never persisted, never advancing `lint-debt`). Flagged owner action: a known-issue
notice for the field beyond vlt-core (the fresh public-GitHub install exists) — tracker
rail issue or changelog/README, the owner picks the channel. B10-12's shipped cut
retires this posture.

**Next lifecycle move:** owner confirmation on the roundtable-delta question above, then
`brief build B10-12` (`build-brief`) — before any v0.14.0 release choreography.
*(Delta convened 2026-08-22 — see the record below; OPEN dispute D1 blocks the brief.)*

## Roundtable review — addendum (2026-08-22)

**Convened** as a scoped DELTA over the second capture addendum only (A10-16 + A10-17 →
B10-12; the moved joint) — not a re-review of the batch. **The owner was not present:**
converged amendments are applied and marked *roster-converged, owner review pending*;
the one genuine split — which touches standing owner rulings — is recorded OPEN below,
never substituted. Roster: Mary (analyst), Winston (architect), Amelia (dev), John (PM),
Paige (tech writer), Sally (UX), Carson (brainstorming), Dr. Quinn (problem solving),
Maya (design thinking), Victor (innovation strategy) — Caravaggio and Sophia remain
excused per the owner's 2026-08-21 roster ruling (carried, not re-decided). ~49 raw
findings merged to 12 joints. Grounded against branch `arc10-v0.14.0` @ `7a4b1a8`;
capture claims re-verified against `vlt-lint-full.js` (one misattribution found and
corrected — DA7). Session file:
`_output/party-mode/2026-08-22-arc10-roadmap-roundtable-delta-session.md`.

**Amendments applied (all landed in-session, dated markers in place; every one owner
review pending):**

- **DA1** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — release-line superseding note: v0.14.0 blocked on B10-12; cut composition
  is OPEN D1 → release line. *(7 voices proved the joint)*
- **DA2** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — the declared fold order recorded **discharged unexercised** (all candidates
  built at `7a4b1a8`; mechanically unexecutable under prefix tags) → release line.
  *(Mary conceded her fold-contingency finding to this — no trigger remains)*
- **DA3** — ✅ **OWNER-RULED 2026-08-23** (posture confirmed; notice channel ruled =
  v0.14.0 release notes / CHANGELOG entry, no pinned issue; carried as a release-time
  obligation on `vlt-release` Stage 3) — interim field posture: full-mode lint untrusted on 0.13.x (standard mode
  unaffected); unexplained-shortfall reports void; flagged owner action — a known-issue
  notice for the wider field, channel owner-picked; retired by B10-12's cut → addendum
  release-posture section. *(A1's precedent, 3 voices)*
- **DA4** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — leg 1's fixed-vs-moved-limit question is a **pre-brief spike obligation**
  (bisect 3,920..4,266 / read harness source); trim-vs-budget an owner ruling on the
  measured number; cannot-settle default = standing budget with headroom; budget is a
  margin device, the guarantee is leg 2 + re-discharge → B10-12 entry. *(6 voices)*
- **DA5** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — trim discipline: per-field duplication audit (five schema-only fields
  falsify the blanket near-duplicate claim; `available` load-bearing for leg 2); R4
  markers conserved (`:121`) → B10-12 entry.
- **DA6** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — leg 2 respecified: cap denominated over the input list, reason-partitioned,
  failed slugs survive; near-total shortfall → error (threshold to brief); SKILL
  refusal re-predicated on the shortfall signal and worded as version-skew defence,
  refusal a directed surface; error path persists a dated failed-run record; retry
  deliberately out of scope → B10-12 entry. *(the refusal-defends-an-abolished-state
  and would-not-have-refused-the-motivating-event findings, 5 voices)*
- **DA7** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — leg 3 non-enumerative: every scans-denominated consumer audited at brief
  time (grounding correction: `:270` is the index pass, not the cluster pass);
  inbound-derived orphans/near-dups suppressed-or-annotated under shortfall; census
  keeps `pages_total: scans.length`; E6 census checks re-verified post-B10-12 →
  B10-12 entry + the capture's `:270` claim corrected in place.
- **DA8** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — acceptance tagging split: ship-verifiable fixture checks gate (partial-
  failure cap, zero-scans error, refusal fixture, schema-size assertion); field event
  narrowed to an executing sweep "degrading loudly if it degrades at all" → B10-12
  entry. *(the A4-4(5)/B8-2(4) lesson, 5 voices)*
- **DA9** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — B10-2(5) ledger bookkeeping: routing-resolved line; the one field event's
  three ledger consequences cross-referenced; criteria read against the post-B10-11
  zone map; pass additionally requires no on-disk wiki page in `missing_targets`;
  relocation-state disambiguation rule → B10-2 ledger entry.
- **DA10** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — A10-16's follow-up audit recorded DISCHARGED at capture (A10-17's era
  grounding is the evidence) → A10-16 entry.
- **DA11** — ✅ **OWNER-RULED 2026-08-23 — CONFIRMED (batch disposition)** — brief-time recorded disposition of the one sibling fan-out
  (`vlt-review-council.js:148-152`): fold a minimal lens-shortfall cap or decline with
  reason → B10-12 entry.

**No rule (R#) declared** — every cure landed as an amendment with an existing home.

**OPEN dispute (1) — GATES the brief:**

- **D1 — the cut composition.** The three standing commitments are jointly
  unsatisfiable as written (7 voices, independently): linear history + ff-tag releases
  mean the first cut containing B10-12 contains B10-11, so "B10-11 ships as its own
  cut, alone" (owner, 2026-08-21 T10), "no v0.14.0 cut before B10-12" (owner,
  2026-08-22), and "the fix lands on the post-B10-11 file" (capture grounding) cannot
  all hold — and "built before the cut" read literally permits a cut that ships the
  broken lint-full again, against the owner's verbatim intent. The room cannot cure
  this without touching an owner ruling. **Options for the owner** (decision material
  in the session file): **(A)** v0.14.0 = B10-6..B10-10, v0.15.0 = B10-11 alone,
  v0.16.0 = B10-12 — both rulings literal; cost: the relocation's acceptance runs
  while full-lint is dead and lies about exactly the moved-link class (an acceptance
  run nobody can read — Victor), and the broken instrument persists two more cycles;
  **(B)** v0.14.0 = B10-6..B10-10, v0.15.0 = B10-11 + B10-12 — "alone" amended to
  "B10-11 + its blocking repair"; the repaired instrument ships with the relocation it
  observes; **(C)** v0.14.0 = B10-6..B10-12 one cut — fastest field cure; both
  pre-called commitments superseded, with the isolation purpose preserved procedurally
  (B10-11's acceptance checks run as their own discharge pass — Winston); **(D)**
  branch surgery: author B10-12 against the pre-B10-11 file and rebase beneath B10-11 —
  preserves both rulings literally at the cost of forking the fix, contradicting the
  capture's grounding, and rewriting the branch (presented for completeness; no voice
  endorsed it). **Recorded positions:** Maya holds that only a composition where the
  first shipped cut CONTAINS B10-12 honors the owner's verbatim intent (favors B/C);
  Victor's instrument argument favors B over A; the blocker's delay is pure cost (the
  field is already exposed) so the chain should run immediately — decision material,
  not a room ruling. ~~**`build-brief` is BLOCKED on the owner ruling D1.**~~
  **RULED (owner, in-session, 2026-08-22): option (C) — one cut, v0.14.0 =
  B10-6..B10-12.** Both pre-called commitments superseded by this ruling; the isolation
  purpose is preserved procedurally per Winston's shape — B10-11's acceptance checks run
  as their own discharge pass over the one upgrade, and the wiki-relocation migration
  remains separately human-gated at upgrade time. The blocker is satisfied: the first
  (and only) 0.14 cut contains the lint-full repair. DA1's release line resolves
  accordingly: v0.14.0 releases after B10-12 lands, twelve builds + the repair, one
  vlt-core upgrade discharges the whole ledger tail. `build-brief` for B10-12 is
  UNBLOCKED.

**Mid-session evidence update (external, noted):** while the delta sat, the B10-2(5)
ledger entry gained the vault's same-day follow-up — the regression era PROVEN (ceiling
in the 3,920..4,266 window) and the `…-130456` filing withdrawn by its author, folded
into `…-130455`. DA9's wording was written against the updated text; DA4's spike now
starts from a narrowed bracket, and the fixed-limit hypothesis has direct support (the
3,920 schema executed on the same harness era) — the spike still runs, to locate the
value and its stability for the budget number.

**Out-of-scope material for `inbox/` filing (Carson):** (1) no factory-side execution
tier exists for agent-spawning workflows — B10-2's checks (1)-(4) discharged at rest
while the workflow was non-executable; propose a fixture-vault smoke run / harness-limit
canary in the release choreography, tagged ship-verifiable. (2) the harness classifier
limit is an undocumented platform dependency — B10-8's dependency record has no
"platform constraints" row-class for harness schema/prompt limits.

**Keepsake:** `_output/party-mode/2026-08-22-arc10-roadmap-roundtable-delta.html`.

**Next lifecycle move:** the owner rules D1 (and reviews DA1..DA11, each marked owner
review pending) — that closes this record; then `brief build B10-12` (`build-brief`).

## Deferred acceptance ledger

*(empty — populated per build at brief time; checks tagged ship-verifiable vs
field-contingent per build-brief §9. Roundtable A1, owner-ruled: the v0.13.0 discharge
runs under the stated interim evidence posture — the owner hand-saves the Step-4 report
verbatim to a dated file at upgrade time; B10-6 retires the posture.)*

- [x] **build-B10-1 (manifest-source-hash, briefed 2026-08-21):** brief
  `skills/reports/build-B10-1-manifest-source-hash.md`. Five checks. **(1)
  `[ship-verifiable]`** — the divergence net catches the edit it exists to catch: the
  synthetic reproduction discharged at rest with a red-then-green record in the BUILT
  status (hand-edit a manifested file → `--write` → `--verify` still reports `diverged`;
  the pre-fix clean report is the red). **(2) `[ship-verifiable]`** — the live-as-source
  escape path is loud (A5): a write with source == live carries `source_mode: "live"` +
  a warning in its JSON, with the Confirm/Step-4 routing text shipped; discharged at
  rest by the fixture run + greps. **(3) `[ship-verifiable]`** — the version-skew escape
  path refuses (A5): a write against a source whose `module_version` ≠ the installed
  record exits 2 with the named error `version-skew` (the `gh-missing` discipline);
  discharged at rest by the fixture run. **(4) `[ship-verifiable]`** — both prose claims
  true, both drive-bys landed, the contract row priced: `vlt-setup/SKILL.md` no longer
  claims installed-files compute; `vlt-upgrade/SKILL.md:49` is literally true with the
  trap-closed clause; `capability-template.md:23`'s enum lives in prose, not the copied
  comment; both issue forms carry the identical interim honesty sentence; the contract
  `:311` row names `{overlays}/.skill-manifest.sanctioned` and package-lint **C6 passes**
  against the re-stamped rule card. **(5) `[field-contingent]`** — the first live upgrade
  under the fixed net reports honestly; discharging event named: **the owner's vlt-core
  upgrade to v0.13.0** (performer: the owner; vault: vlt-core; evidence reaches the
  factory via the A1 hand-saved Step-4 report). Pass = the `manifest_write_divergence`
  line appears in the Step-4 report (never omitted), any Step-3 sanctioned migration edit
  shows sanctioned-and-denominated (not silently blessed), and known local edits remain
  `diverged` on the post-upgrade `--verify` instead of being absorbed; fail = a clean
  report over a live tree that differs from v0.13.0 stock at any unsanctioned manifested
  path.

  **Acceptance 2026-08-21 (discharge run over the vlt-core 0.13.0 upgrade, A1
  hand-save):** (1)-(4) ship-verifiable, discharged at rest per the BUILT status.
  **(5) FAILED** — the hand-saved Step-4 report
  (`skills/reports/2026-08-21-vlt-core-upgrade-0.13.0-step4-report.md`, verbatim per its
  provenance header) **omits the mandatory `manifest_write_divergence:` line**: its YAML
  jumps `skill_asset_divergence: []` → `migrations_run:`, and the string appears nowhere
  in vlt-core — violating `vlt-upgrade/SKILL.md:106`'s never-omitted-when-empty contract.
  The mechanism itself ran and was honest: the upgrade-ledger digest records the
  Step-3.6 source-hashed write (`source_mode: source`, 67 entries, diverged/sanctioned/
  sanction_stale all empty) and the check's fail condition (a clean report over a
  differing tree) did not occur — the defect is the report-shape clause alone. Inbox
  filing FILED on owner confirmation 2026-08-21:
  `inbox/2026-08-21-164445-step4-report-omits-manifest-write-divergence-line.md` —
  routes into the next `inbox-capture` run (B10-6 the natural home).

  **Acceptance 2026-08-23 (discharge run over the vlt-core 0.14.0 upgrade) — (5)
  re-check DISCHARGED, item complete.** The persisted Step-4 report
  (`_agent/upgrade-reports/2026-08-23-1217-upgrade.yaml`, B10-6's instrument) carries
  `manifest_write_divergence: []` (line 13 — present-when-empty, the exact clause that
  failed on 0.13.0), mirrored in the ledger Notes (`upgrade-ledger.md:312`). No
  sanctioned migration edit occurred this run (Step-3 sanction path unexercised —
  vacuous, stated). The known-local-edits clause discharges vacuously: no live local
  edit exists any more (the researcher "standing sweeps" bullet is gone from vlt-core's
  live file — the vlt-sweep registration migrated to durable `local_consumers:` on
  `frontmatter.md`/`write-verification.md`), and pre-flight `--verify` reported 67/67
  entries clean, diverged/sanctioned/sanction_stale/missing all empty
  (`upgrade-ledger.md:308`). The fail condition (a clean report over a differing tree)
  did not occur.

- [ ] **build-B10-2 (lint-full-signal-repair, briefed 2026-08-21):** brief
  `skills/reports/build-B10-2-lint-full-signal-repair.md`. Five checks. **(1)
  `[ship-verifiable]`** — the A8 handshake is bipartite-consistent:
  `write-verification.md` (still @3, membership not a rule change) `consumers:` lists
  `vlt-lint-full.js` and the workflow's `// depends_on:` header acks
  `write-verification@3`; discharged by **package-lint Group E PASS** at rest. **(2)
  `[ship-verifiable]`** — the Gap-B tri-state landed whole: the
  `sources_vs_prose_mismatch` boolean is gone, the required
  `sources_vs_prose` enum (`match`/`diverge`/`no_prose_section`) is in `PAGE_SCAN`, the
  prompt instructs the three states with the no-prose-conformant conditional, and the
  reducer populates `sources_vs_prose_mismatches` only from `diverge` (slot name
  unchanged, `report.md:20` stable); discharged at rest by greps + `node --check`. **(3)
  `[ship-verifiable]`** — the three explicit instructions are present with current inline
  markers: coexistence posture (`per frontmatter@9 rule 4`), callout-vs-bullet in both
  directions on the page scanner **and** the cluster ask (`per wiki-supersession@2`), the
  Gap-B conditional (`per write-verification@3`) — every marker version matching the
  convention's `version:` on disk; discharged at rest. **(4) `[ship-verifiable]`** — the
  derivation shipped with its interim honest: `full-scale.md` step 1 derives
  `crossLayerSlugs` from resolved `vault_structure` keys with the qualifying-key
  predicate single-homed there; the interim supplement line names `projects/`, `areas/`,
  `resources/`, `_agent/handoffs/` and carries its own in-file retirement clause (D2/A7);
  `checks.md:12` points at the derived set rather than enumerating; R4's rule text stands
  in the workflow ack header with its one-line pointer in `full-scale.md` (the interim
  carrier in this review record retires); the F8 fan-out audit table (R4's retroactive
  first run) is recorded in the BUILT status; discharged at rest. **(5)
  `[field-contingent]`** — the repaired signal is quiet where the field was loud;
  discharging event named: **the owner's first full-mode `vlt-lint` sweep (>30 pages,
  the fan-out path) on vlt-core after the v0.13.0 upgrade** (performer: the owner;
  vault: vlt-core; evidence via the persisted `{lint_reports}` file — lint already
  persists verbatim). Pass = `sources_vs_prose_mismatches` contains no page whose only
  "defect" is having no prose Sources section (the 22-of-25 false class collapses),
  `missing_targets` contains no valid link into `_agent/handoffs/`/`areas/`/`projects/`/
  `resources/` or a vault-grown key's directory, and no new false-positive class from
  the added instructions (a legal mixed `sources:` state unflagged; a bullet-form
  supersession note still correctly surfaces as unmarked). Fail = any class persists or
  returns under a new name.

  **Acceptance 2026-08-21:** (1)-(4) discharged at rest per the BUILT status. (5)
  STILL-OPEN — no post-upgrade lint run exists (`{lint_reports}` latest is
  2026-08-16-1118, pre-upgrade). Discharging event: the owner's first full-mode
  (>30 pages) `vlt-lint` sweep on vlt-core; evidence: the persisted `{lint_reports}`
  file.

  **Acceptance update 2026-08-22 — (5) FAILED.** The discharging event was attempted
  (vlt-core, 145 wiki pages, installed 0.13.0 bundle) and the sweep is
  **non-executable**: 145/146 agents rejected pre-read (`PAGE_SCAN` 4,266 chars vs the
  harness classifier limit — a B10-2 regression, 3,920 → 4,266 via the tri-state
  descriptions), and the workflow then rendered the total failure as a **clean empty
  report** (`files_checked: 0`, all buckets empty, `coverage_caps: []` — the
  `.filter(Boolean)` silent drop at `:195`; only the budget guard caps coverage).
  Worse, the one page that did scan showed the missing-targets false-positive class
  live (6 flags, all existing pages). Evidence: relayed vault handoff
  `<vault>/_agent/acceptance/2026-08-22-vlt-0.13-lint-full-defect.md`, factory-grounded
  against source 2026-08-22 (all mechanism claims confirmed verbatim). No report
  persisted, no vault write. Filing FILED on owner confirmation 2026-08-22:
  `inbox/2026-08-22-130455-lint-full-nonexecutable-and-vacuous-clean-report.md` —
  route at the next capture (no unbuilt B10 build owns `vlt-lint-full.js`; routing is
  an owner ruling, and bears on the v0.14.0 release gate). **Evidence sharpened by the
  vault's same-day follow-up:** the regression era is PROVEN (the 2026-08-16 full lint
  ran the fan-out on 0.12.0/3,920 chars; non-executable after the 08-21 upgrade — the
  ceiling sits in the 3,920..4,266 window), and the "missing-target seam" third
  finding was RETRACTED by its author — the six flags were fabricated by the partial
  sweep itself (`:208` builds the existence set from scanned pages only), which makes
  Defect 2 worse and the companion filing `…-130456` was withdrawn, its content folded
  into `…-130455`. Re-discharge = an executing,
  loud-degrading full sweep passing the original criteria.
  *(roundtable delta 2026-08-22 DA9, roster-converged — ✅ **owner-ruled 2026-08-23, batch**)* **Routing
  resolved 2026-08-22:** the filing (`…-130455`, carrying the withdrawn `…-130456`'s
  folded content) ESCALATED into **B10-12**, release-blocking — see the second capture
  addendum. The re-discharge event carries **three ledger consequences in one run** —
  it discharges this check, is B10-12's field-acceptance event, and sizes or collapses
  the residual `normalizeTarget` seam — record the one run against both entries. The
  original criteria are read against the **post-B10-11 zone map** (the `resources/`
  clause superseded by its stub/wiki-move equivalents), and the pass **additionally
  requires `missing_targets` to contain no target that exists on disk as a wiki page**
  (the fabricated-by-partial-sweep class, made falsifiable). The evidence records the
  wiki-relocation state the sweep ran under; leg 3's filesystem-truth `slugSet` is the
  disambiguation rule — post-fix, a flagged existing page is a genuine relocation
  finding, never a shortfall artifact. Wording per DA8: an executing full sweep
  (`files_checked ≈ files_listed`), degrading loudly if it degrades at all, passing the
  original criteria as amended here.

  **Re-discharge attempted 2026-08-23 — (5) FAILED, narrowly (one leg of three).** The
  discharging event ran: the first post-0.14.0 full-mode sweep
  (`{lint_reports}/2026-08-23-1504-lint.yaml`) **executed** (`files_checked: 145` of
  `files_listed: 146` — the one shortfall named loudly in `coverage_caps` with its
  reason, the StructuredOutput retry cap on sourdough-starter) and **degraded loudly
  everywhere it degraded** (orphans/near_duplicates rendered `unmeasured`, never zero;
  no vacuous clean report — the B10-2/A10-16/A10-17 failure classes are dead). Two of
  three criteria PASS: `sources_vs_prose_mismatches` contains no no-prose-only false
  page (every entry a genuine divergence; one cosmetic case labeled cosmetic), and
  `missing_targets` contains no valid link into `_agent/handoffs/`/`areas/`/`projects/`
  or a vault-grown key's directory. **The missing-target leg FAILS:** the report
  declares its own check broken this run — the workflow returned 12 missing targets,
  all 12 verified false positives (`coverage_caps`, cause: the `crossLayerSlugs`
  derivation): 3× `[[index]]` (`resources/wiki/index.md` exists on disk — violating
  the DA9 no-target-that-exists-as-a-wiki-page clause), 8× `sources/` deposits
  (`sources/` is not a `vault_structure` key, so the qualifying-key predicate cannot
  reach it), 1× `_agent/bases/wiki.base` (outside the `*.md` glob). The `[[index]]`
  and `.base` causes **persist from the pre-B10-2 class** (identical flags in the
  2026-08-16 pre-move report, its `missing_targets` note) — "any class persists or
  returns under a new name" = fail. The DA9 seam duty is done: the residual seam is
  **sized, not collapsed** — 12 hits, three named causes. Inbox filing FILED on owner
  confirmation 2026-08-23:
  `inbox/2026-08-23-160500-crosslayerslugs-blind-to-sources-index-and-non-md-linkables.md`
  — routes into the next `inbox-capture`. Re-discharge = a full sweep whose
  missing-target flags survive verification (or a measured zero) after the predicate
  gains those three populations.

- [x] **build-B10-3 (repeat-aware-spec-candidate, briefed 2026-08-21):** brief
  `skills/reports/build-B10-3-repeat-aware-spec-candidate.md`. Three checks. **(1)
  `[ship-verifiable]`** — the partition shipped whole and agrees across its three homes:
  `checks.md:47` carries the open-backlog-item partition with the extended
  records-never-reports derivation sentence (A3's rule verbatim in force) and every
  retained posture (no stored counter, never-auto-promote, decline exclusion,
  relay-entries-only, empty-handoffs closer); `report.md` carries the annotated loud
  `spec_candidate:` slot (name/position stable) + the new `spec_candidate_standing:`
  denominated line with the empty-handoffs no-line rule; `fix-and-file.md`'s Guard
  carries the mandatory signal-clause refresh. Discharged at rest by the brief's
  verification greps + six-case desk-check + package-lint A/B/C/E PASS, recorded in the
  BUILT status. **(2) `[ship-verifiable]`** — A3 compliance by construction: no shipped
  text directs a read of `{lint_reports}` or any prior report for repeat detection; no
  Decay-contracts / zone-map row changes (no new persisted surface — B10-3 stays out of
  E1's census); discharged at rest by grep. **(3) `[field-contingent]`** — the
  six-repeat field class collapses; discharging event named: **the owner's next two
  `vlt-lint` runs on vlt-core after the v0.13.0 upgrade** (performer: the owner; vault:
  vlt-core; the governance check reads all of `_agent/handoffs/` in both modes, so
  scoped runs qualify; evidence via the persisted `{lint_reports}` files — a factory
  read of those files is acceptance evidence, not repeat detection). Pass = any
  standing candidate with an open filed item and unchanged signal appears only on
  `spec_candidate_standing:` with count and paths, never loud; a candidate lacking a
  filed item reports loud once, its Step-4 filing lands, and the second run shows it
  collapsed (the two-run record-establishing shape — expected if vlt-core's six were
  never filed); any genuinely new candidate still reports loud. Fail = an unchanged
  filed candidate re-fires loud on the second run, or the standing line is
  absent/undenominated over a non-empty handoffs dir.

  **Acceptance 2026-08-21:** (1)-(2) discharged at rest per the BUILT status. (3)
  STILL-OPEN — zero post-upgrade lint runs. Discharging event: the owner's next two
  `vlt-lint` runs on vlt-core (scoped qualifies); expected shape is the two-run
  record-establishing collapse — the standing pair reports loud once and files, then
  shows on `spec_candidate_standing:` in run two (vlt-core's six were never filed).

  **Note 2026-08-22:** the failed full-mode attempt (see B10-2's FAILED update) does
  **not** count toward this pair — it aborted with no persisted report, and this
  check's evidence is the persisted `{lint_reports}` files. Unaffected path: **scoped
  runs qualify** and don't ride the broken fan-out workflow — two scoped `vlt-lint`
  runs can discharge (3) while the full-mode repair is pending.

  **Run 1 of 2 recorded 2026-08-22 — CONFORMANT.** The scoped lint (vault commit
  `f39946a`, persisted report `{lint_reports}/2026-08-22-1500-lint.md`): the genuinely
  new candidate (`penny-treat-rotation`, both signals) reported **loud once** with full
  annotation (`new; owner dog-trainer; 0 prior declines honored`) and its backlog
  filing landed; the unchanged filed candidate (`walkthrough-contract`) appeared
  **only** on the denominated `spec_candidate_standing:` line, never loud — exactly
  the check's shape. (The standing count is 1, not the historical pair: the nutrition
  spec was long since promoted to `{specs}` and is out of the handoffs population —
  consistent, not a miss.) Run 2 discharges on the next scoped-or-full run: pass =
  `penny-treat-rotation` collapsed to the standing line. Side signal from this run's
  `coverage_caps` — the ≥2-relay leg fires on ordinary round trips (6 of 8) — filed as
  `inbox/2026-08-22-150000-spec-candidate-relay-leg-fires-on-ordinary-round-trips.md`.

  **Run 2 of 2 recorded 2026-08-23 — (3) DISCHARGED, item complete.** The first
  post-0.14.0 full lint (`{lint_reports}/2026-08-23-1504-lint.yaml`): `spec_candidate:
  []` (no new candidate loud) and `penny-treat-rotation` collapsed onto the denominated
  `spec_candidate_standing:` line ("2 standing candidate(s) — previously filed, open
  backlog item, signal unchanged", penny-treat-rotation + walkthrough-contract, "0
  prior declines honored") — exactly the two-run record-establishing shape the check
  named. No unchanged filed candidate re-fired loud; the standing line is present and
  denominated over a non-empty handoffs dir. Side signal, surfaced to the owner (not
  gating): the workflow's raw spec-candidate derivation returned 10 and was corrected
  to 2 by in-run verification (drain annotations counted as second relays;
  `[!superseded]` callouts quoting wiki content read as revision records) — see the
  report's `coverage_caps` and the discharge report's candidate-filing list.

- [ ] **build-B10-4 (metric-home-overlay-bell, briefed 2026-08-21):** brief
  `skills/reports/build-B10-4-metric-home-overlay-bell.md` (B9-6 carried; direction 2
  clerk-resolved on top of the shipped direction-3 floor, autonomous run 2026-08-21,
  ~~owner review pending~~ **✅ OWNER-REVIEWED 2026-08-23, first-half review: all seven
  CONFIRMED — direction 2 live-ruled with the count-shape premise correction on record;
  see the brief's stamp**). Four checks. **(1) `[ship-verifiable]`** — the `frontmatter@10`
  handshake is bipartite-consistent across all nine legs: `frontmatter.md` at
  `version: 10` (roster unchanged), all eight skill pins + the `vlt-lint-full.js`
  `// depends_on:` header ack `frontmatter@10`, and both `vlt-lint-full.js:173`
  `per frontmatter@9` markers re-derived (rule 4 untouched, verified still-true) and
  re-stamped `@10` — no `@9` pin or marker anywhere in the shipped surface; discharged
  at rest by **package-lint Group E (E1+E5) PASS**, recorded in the BUILT status.
  **(2) `[ship-verifiable]`** — the durable metric home works end-to-end at rest with a
  red-then-green record: pre-build, a `local_metrics:`-declared metric's wire errors
  `unknown metric id` (the red); post-build the fixture derives it, evaluates the wire
  (tripped + ok), renders the denominated local block; genuinely unknown ids and
  malformed/shadowing declarations stay loud per-entry; `--strip` silent on green,
  loud on error; **C8 PASS unchanged** (seed ships zero local metrics). **(3)
  `[ship-verifiable]`** — the overlay bell and Finding 4 shipped whole and agree
  across their homes: `frontmatter.md` carries *Per-section addressing (overlays)* +
  the widened `enforcement_counter:` vocabulary under the one bump; `checks.md:37`
  walks `{overlays}` with the five classes + the new `overlay_rule_undeclared` (R3
  legal response in place); `report.md` carries the widened annotations + the new slot
  with the five existing slots name/position-stable; `vlt-mint/SKILL.md:140` directs
  per-section (not file-level) placement and `:99` the widened vocabulary;
  `vlt-setup/SKILL.md:186` states `local_metrics:` seed-merge durability; discharged
  at rest by the brief's cross-file greps + six-case desk-check. **(4)
  `[field-contingent]`** — the first vault-grown metric survives an upgrade and the
  bell rings on a real overlay; discharging event named: **the owner declares
  vlt-core's tripwire metric (the derive function issue #1 lost) as a `local_metrics:`
  entry with its wire after the v0.13.0 upgrade, then runs `vlt-lint` and the
  subsequent upgrade** (performer: the owner; vault: vlt-core; evidence via the
  persisted `{lint_reports}` file and the A1 hand-saved Step-4 report / upgrade
  ledger). Pass = the declared metric derives and its wire evaluates with no
  unknown-id error, the next upgrade's seed-merge + vitals overwrite leave declaration
  and wire intact (no re-establish-by-hand), and the meta-check walks vlt-core's
  overlays reporting any rule-shaped section's declaration state. Fail = hand
  re-establishment needed post-upgrade, an unknown-id error on a declared metric, or
  an overlay-hosted rule still invisible to the meta-check.

  **Acceptance 2026-08-21:** (1)-(3) discharged at rest per the BUILT status. (4)
  STILL-OPEN — vlt-core's `_agent/tripwires.yaml` carries the 0.13.0 header docs for
  the schema but **no `local_metrics:` section is declared yet** (grep
  `^local_metrics:` = 0 matches; the seed ships none by design). Discharging event,
  owner-triggered in three parts: declare the tripwire metric (the derive function
  issue #1 lost) under `local_metrics:` with its wire, run `vlt-lint`, then the
  subsequent (v0.14.x) upgrade proves seed-merge durability.

  **Acceptance 2026-08-23 — (4) STILL-OPEN, unchanged (first discharge run on this
  tail).** vlt-core's `_agent/tripwires.yaml` still declares no `local_metrics:`
  section (grep: comment/header mentions only; the 0.14.0 upgrade carried the header
  docs and all four wires byte-for-byte, `upgrade-ledger.md:312`), and the lint's
  `counter_unknown_metric: []` / `overlay_rule_undeclared: []` ran over a zero-metric
  population. Discharging event unchanged, owner-triggered in three parts: declare
  the metric + wire → `vlt-lint` → the subsequent (v0.15.x) upgrade proves
  seed-merge durability.

  **Acceptance update 2026-08-23 (evening) — (4) re-graded BLOCKED (unreachable).**
  The declaration was attempted for real (session vlt-core-d4) and **refused honestly**:
  the named metric is now identified — `pages_with_review_after` (count of wiki pages
  whose frontmatter carries `review_after:`, the denominator for `expired_pages`),
  recovered from vault git history (`1e01b01:_agent/vitals.sh`, corroborated by the M0
  audit artifact) — and it is **inexpressible under the shipped `local_metrics:`
  schema**: factory source `vlt-vitals.py:251` bounds kinds to
  `{file_count, bytes, days_since_newest}` with pure glob/path locators and **no
  content predicate**; declaring it as `file_count` over `{wiki}/**/*.md` would count
  all pages and label them key-carriers — a fabricated metric, owner-ruled stop.
  No shipped surface can produce the discharging event for a content-filtered derive,
  which is the very shape issue #1 describes — per the rubric this is BLOCKED, not
  STILL-OPEN; waiting cannot discharge it. Inbox filing FILED on owner confirmation
  2026-08-23:
  `inbox/2026-08-23-190100-local-metrics-kinds-cannot-express-a-content-filtered-count.md`
  (the module owes a content predicate, a fourth kind, or a canonical `METRICS`
  entry); routes into the next `inbox-capture`. The corrective story was also posted
  to issue #1 as its `amended` seed (label applied 2026-08-23 — the B10-7(3)
  discharging comment). **Premise corrections on the record:** the loss was a **silent
  supersession, not an upgrade clobber** — vlt-core never hand-edited `vlt-vitals.py`
  (4 commits, all upgrades; three ledger entries confirm no local edit overwritten);
  `_agent/vitals.sh`'s six derives were superseded at 0.9.0, five carried into
  canonical `METRICS`, `pages_with_review_after` dropped with **no divergence report
  naming it** (a contributing pattern, carried in the filing). Part 2's
  `counter_unknown_metric: []` this run is a stated-vacuous zero
  (`2026-08-23-1739-lint.yaml:91` says so explicitly — the honest-reporting posture
  working). Part 3 (seed-merge durability) is moot until declarable.

- [x] **build-B10-5 (fleet-rung, briefed 2026-08-21):** brief
  `skills/reports/build-B10-5-fleet-rung.md` (B9-7 carried; eight brief-time dispositions
  clerk-resolved, autonomous run 2026-08-21, ~~owner review pending~~ **✅ OWNER-REVIEWED
  2026-08-23, first-half review: all eight CONFIRMED, the "chiefly" pair live-ruled as
  field-proven** — chiefly: literal
  `_agent/reflexes.md` with no structure-map key, and the rung schema as a
  `frontmatter` rule change → @10→@11 nine-leg walk). **The v0.13.0 release build.** Six
  checks. **(1) `[ship-verifiable]`** — the `frontmatter@11` handshake is
  bipartite-consistent across all nine legs, both `vlt-lint-full.js:173` markers
  re-derived (rule 4 untouched) and re-stamped `@11`, zero `frontmatter@10` in the
  shipped surface, R4 fan-out audit re-run recorded (no `convRead` change); discharged at
  rest by **package-lint Group E (E1+E5) PASS**. **(2) `[ship-verifiable]`** — the rung
  shipped whole and agrees across its homes: all five contract touches (Beat-1 read, the
  rung passage as single home, the ladder row, the non-enumerative same-act overlay
  clause, the decay row per the contract's `:314` rule), rule card re-derived + sha
  re-stamped ≤ 8,000 bytes (**C6 PASS**), the `scope: vault` frontmatter stanza under the
  @11 bump, the setup seed + report line, the upgrade provisioning line, the mint
  same-act step, four Beat-1 recitations, the groom-pass scope sentence — all
  pointer-not-restatement; discharged at rest by greps + the seed dry-run. **(3)
  `[ship-verifiable]`** — the roundtable-A9 fixture: a **contract-overlay** pointer line
  parses under the shipped population + falsifier wording with no wording edit, a
  convention-overlay pointer likewise, and a copy-shaped line fires the falsifier (the
  red case); three verdicts recorded in the BUILT status. **(4) `[ship-verifiable]`** —
  the release gate: both version strings `0.13.0`,
  `package-lint --expect-version 0.13.0` exit 0 with its PASS line in the release commit,
  ff-merge + tag + push per `vlt-release`. **(5) `[field-contingent]`** — the rung
  arrives without harm; discharging event named: **the owner's vlt-core upgrade to
  v0.13.0** (performer: the owner; vault: vlt-core; evidence via the A1 hand-saved
  Step-4 report + a factory read of vlt-core). Pass = `_agent/reflexes.md` seeded
  frontmatter-only (`scope: vault`, cap/falsifier/posture, ≈0.4–0.5 KB — S2's birth
  band), nothing clobbered, activations proceed with the no-op read; fail = missing/
  overwritten file, a seed carrying rule content, or an activation error on the empty
  rung. **(6) `[field-contingent]`** — the writers write; discharging event named: **the
  first `vlt-mint` overlay mint/amend act in vlt-core after the upgrade** (performer:
  the owner in vlt-core — standing overlays make an amend a natural near-term event;
  evidence: the rung file + the mint decision-log entry, read directly from vlt-core).
  Pass = the pointer line lands in the same act, pointer-shaped, with no outside-an-act
  backfill (the at-write posture holds); fail = an overlay act closing with no rung
  line, or a rung line restating rule content (the falsifier's copy case — itself the
  filing the declined lint check waits on).

  **Acceptance 2026-08-21:** (1)-(4) discharged at rest per the BUILT status. (5)
  split — **upgrade-side DISCHARGED 2026-08-21**: `_agent/reflexes.md` seeded (689 B;
  frontmatter `scope: vault`, `cap: 30`, falsifier, `review_after: 2026-11-17`; body =
  the shipped italic hint matching `vlt-setup/SKILL.md:286` byte-for-byte, plus one
  pointer line for the pre-existing frontmatter overlay written by owner-ruled upgrade
  migration 2 — pointer-shaped, no rule content, legal under the writer clause and the
  file's own hand-adding-is-legal note; nothing clobbered). STILL-OPEN: the no-op
  activation read (trigger: the owner's next vlt-core partner session — routine use).
  (6) STILL-OPEN — the migration pointer write was an upgrade-ruling, **not** a mint
  act, so the writers-write clause is unexercised. Discharging event: the first
  `vlt-mint` overlay mint/amend in vlt-core (the standing frontmatter overlay makes an
  amend the natural near-term trigger); evidence: the rung file + the mint
  decision-log entry, read directly from vlt-core.

  **Acceptance 2026-08-23 — (5) tail and (6) both STILL-OPEN, unchanged.** (5)'s no-op
  activation read: no post-upgrade partner session exists yet (latest
  `_agent/sessions/` entry 2026-08-23-103039 predates the 11:56 upgrade); trigger
  unchanged — the owner's next vlt-core partner session, which now also exercises
  B10-11's read-the-index-at-its-new-home tail (one session feeds both). (6): the rung
  file is byte-unchanged since the 2026-08-21 seed (689 B, `last_updated: 2026-08-21`,
  one migration-written pointer line, no mint act since — the 0.14.0 upgrade ran no
  overlay mint). Trigger unchanged: the first `vlt-mint` overlay mint/amend in
  vlt-core. First-run tails, no pass-through: no event of the discharging kind has
  occurred.

  **Acceptance update 2026-08-23 (evening) — (5) tail and (6) both DISCHARGED, item
  complete.** (6): the first `vlt-mint` overlay amend ran in vlt-core (session
  vlt-core-d4, carry-back verified against the vault read-only) — commit `10d935e`
  amends `frontmatter.overlay.md` (new §D, append-only) **and writes the rung pointer
  line + decision-log entry in the same commit** (`_agent/reflexes.md` +
  `decision-log.md:1049` in the act's own diff — the at-write posture holds, no
  outside-an-act backfill); the second overlay act (`92a0e5d`, the contract overlay)
  shows the same same-act shape. Both rung lines are pointer-shaped — subject + read
  trigger, no rule content (the falsifier's copy case did not occur). (5) tail: a
  routine post-upgrade partner session ran (football-analyst, 16:15–17:09, session
  note `_agent/sessions/2026-08-23-161500-misc.md` + thread/correction/relay commits)
  and proceeded with no activation error against the two-line rung — behavioral pass;
  the fail modes (activation error, rung-read failure) did not occur.

- [x] **build-B10-6 (report-contract, briefed 2026-08-22):** brief
  `skills/reports/build-B10-6-report-contract.md` (A10-4 + A10-5 under Q3, + the
  addendum-ruled A10-11 and A10-14; brief-time: the acceptance-instrument question
  **ADOPTED** — factory discharge reads the persisted report file, never a hand-carried
  transcript; **✅ OWNER-RULED 2026-08-23: adoption CONFIRMED**, transport caveat
  included — an unreadable vault hand-carries the persisted file itself, never a
  transcript; the A1 posture retires at this build's release). Six
  checks. **(1) `[ship-verifiable]`** — the E2 census + E1 consumer walk on the record
  whole: census table (structured emitters = lint Step-5 + upgrade Step-4; prose verbs
  report-and-discard with durable records named; the A1 hand-saved 0.13.0 file named as
  the one pre-rule specimen / migration input, unconverted), the E1 walk's nine entries
  re-verified incl. the `lint-debt` counter deriving from the `{log}` entry
  (`vlt-lint/SKILL.md:72`), no consumer of the `.md` wrapper found; discharged at rest.
  **(2) `[ship-verifiable]`** — the persist rule + `.yaml` cut coherent across every
  home: `vlt-lint/SKILL.md:72` persists `-lint.yaml` with the legacy-`.md` coexistence
  clause; `vlt-upgrade` Step 4 persists the schema-derived block verbatim to a dated
  `_agent/upgrade-reports/*.yaml` (lazily created literal path — no `vault_structure`
  key this arc per A7, the zone-map row carries the interim no-key clause with its own
  retirement) and the ledger schema gains the required `Report:` line; contract gains
  both rows + the persist-at-birth rule sentence (extending existing tables, never a
  new list — A12); `full-scale.md:7`'s report-dir exclusion names the new dir;
  `vlt-setup` creates/reports both dirs; rule card re-derived + sha re-stamped (**C6
  PASS**); **package-lint A/B/C/E PASS**; discharged at rest by the brief's greps.
  **(3) `[ship-verifiable]`** — mandatory lines structurally unskippable (A10-14):
  schema-derived emission + persist-then-parse-and-verify shipped in Step 4 with the
  fix-and-re-persist response inline; red-then-green desk-check recorded (the hand-saved
  0.13.0 block FAILS the verify on its absent `manifest_write_divergence:` key; a
  schema-complete block passes); discharged at rest. **(4) `[ship-verifiable]`** —
  `high_value_gaps` honesty (A10-11): `report.md:61` renders the literal `unmeasured`
  (never `[]`, never omitted), the identifier still has no producer site tree-wide, and
  `vlt-lint-full.js` is byte-untouched (R4-fanout not triggered); discharged at rest.
  **(5) `[field-contingent]`** — the first upgrade under the contract persists honestly
  and the A1 posture retires; discharging event named: **the owner's next vlt-core
  upgrade (the release carrying B10-6, expected v0.14.x)** (performer: the owner;
  vault: vlt-core — factory-readable). Pass = a dated `_agent/upgrade-reports/*.yaml`
  exists, parses whole, carries the full schema key set incl.
  `manifest_write_divergence:` (empty or not — A10-14's re-discharge evidence), the
  ledger entry's `Report:` line names it, and the factory discharge reads that file as
  the evidence of record with no hand-carried transcript. Fail = a missing/unparseable
  file, any absent mandatory key, or a discharge needing a transcript. **(6)
  `[field-contingent]`** — the lint cut is live and legacy-coexistent; discharging
  event named: **the owner's first vlt-core `vlt-lint` run after that upgrade**
  (performer: the owner; vault: vlt-core; evidence: `{lint_reports}` read directly —
  same event class as the open B10-2 (5) / B10-3 (3) tails, one run can feed all
  three). Pass = the new report lands as `YYYY-MM-DD-HHMM-lint.yaml` (plain YAML,
  parses whole), every pre-existing `.md` report untouched, and a full-mode report
  renders `high_value_gaps: unmeasured`. Fail = a fenced-`.md` persist, a legacy file
  converted/edited/pruned, or the slot rendering `[]`.

  **Acceptance 2026-08-23 — (5)+(6) DISCHARGED, item complete.** (5): the persisted
  report `_agent/upgrade-reports/2026-08-23-1217-upgrade.yaml` exists, parses whole
  (PyYAML, 18 schema keys), carries the full mandatory set incl.
  `manifest_write_divergence: []` and `machine_tools_missing: []`, and the ledger
  entry's `Report:` line names it (`upgrade-ledger.md:313`); this discharge run read
  that file as the evidence of record — no hand-carried transcript. **The A1 hand-save
  posture is retired in practice as well as by ruling.** (6): the first post-upgrade
  lint persisted as `{lint_reports}/2026-08-23-1504-lint.yaml` — plain YAML, parses
  whole; all four pre-existing `.md` reports untouched (mtimes at their original
  dates, 08-03/08-14/08-16/08-22); the full-mode report renders the literal
  `high_value_gaps: unmeasured` (line 130), never `[]`.

- [ ] **build-B10-7 (rail-amendment-channel, briefed 2026-08-22):** brief
  `skills/reports/build-B10-7-rail-amendment-channel.md` (A10-8 under D5/A13/A14 + the
  addendum-ruled A10-15 C1+C2; eight brief-time dispositions clerk-resolved, autonomous
  run 2026-08-22 — **✅ ALL OWNER-RULED 2026-08-23** (disp. 1/2 live-ruled; disp. 7 the
  @mention, live-ruled keep-literal with a follow-up filed; the rest batch-confirmed) —
  chiefly: the widened set is `amended` +
  `needs-info` + five `declined:<reason>` labels, the "Seven labels" count is removed not
  incremented, label additions are ruled additive under `rail_contract: 1`, and the A14
  @mention is the literal `@mggower`). Four checks. **(1) `[ship-verifiable]`** — the
  rail's text agrees with itself across all seven derive-surfaces: the contract carries
  the `amended`/`needs-info`/`declined:<reason>` rows, the amendment verb in the state
  flow, the label-additions-additive evolution clause, and no label count; the three
  per-kind forms parse with true labels, contract-ordered ids, the sharpened
  `provenance_guess`, and the A14 affirmative-move sentence with the B10-1 interim note
  gone; `config.yml` provisions the full roster non-enumeratively; the factory intake
  carries the consume-on-read amendment leg; issue-triage is A13-clean with labeled
  verdict ops; the lifecycle map routes the amendment observable. Discharged at rest by
  the brief's greps + six-case desk-check, recorded in the BUILT status. **(2)
  `[ship-verifiable]`** — the tracker matches the contract at release: the owner runs the
  idempotent bootstrap block before the release tag and `gh label list` shows all
  fourteen labels; after the release push the issue chooser offers the three per-kind
  forms (shared form gone) rendering the affirmative-move note (performer: the owner;
  bounded by the release that ships this build). **(3) `[field-contingent]`** — the
  first live amendment cycle closes the deaf ear; discharging event named: **the owner
  applies `amended` to a captured open issue carrying an un-folded comment, then runs
  the next `inbox-capture`** (performer: the owner + the factory clerk; venue: the
  public tracker + this repo — no vault read needed; open issues #1–#7 make a
  qualifying comment a natural near-term event, and the owner can legally seed one).
  Pass = the comment appends to the origin filing as a dated amendment section
  verbatim, the `amended` label is removed in the same run, the issue stays `captured`
  with no re-materialization, and the appended section joins that run's un-captured
  set. Fail = a re-materialized duplicate, an append never grounded, a label left
  standing, or a comment reaching the factory with no label. **(4)
  `[field-contingent]`** — the widened verdict vocabulary is used and queryable;
  discharging event named: **the next `issue-triage` batch containing at least one
  non-accept verdict** (performer: the owner at the batch gate; venue: the public
  tracker). Pass = a decline lands as `declined` + exactly one `declined:<reason>`
  label with the prose reason still in the closing comment (queryable via
  `gh issue list --label "declined:<reason>"`), and/or a hold-with-question lands
  `needs-info` with `vault-filed` retained. Fail = a decline reason existing only in
  prose again, a `declined:` label with no terminal `declined`, or `needs-info`
  displacing `vault-filed`.

  **Acceptance 2026-08-23 — split: (2) DISCHARGED; (3)+(4) STILL-OPEN.** (2): the
  tracker matches the contract — `gh label list` shows all 14 field-contract labels
  live (incl. `amended`, `needs-info`, the five `declined:<reason>` rows), and the
  post-push chooser offers exactly the three per-kind forms
  (`field-defect.yml`/`field-pattern.yml`/`field-candidate.yml` + `config.yml` on the
  default branch; shared form gone). (3): no issue has ever carried `amended`
  (`gh issue list --label amended --state all` = empty); trigger unchanged — the owner
  applies `amended` to a captured open issue with an un-folded comment (issues #1–#7
  qualify; owner may legally seed one), then runs the next `inbox-capture`. (4): all
  seven issues sit at `vault-accepted`+`captured`; no non-accept verdict has been
  batched yet; trigger — the next `issue-triage` batch containing a decline or
  needs-info. First-run tails, no pass-through.

  **Acceptance update 2026-08-23 (night) — (3) DISCHARGED; only (4) remains.** The
  first live amendment cycle ran whole and in the exact pass shape: the owner seeded a
  substantive comment on captured issue #1 (2026-08-23T21:55:08Z, the B10-4 corrective
  story) and applied `amended`; the same-day `inbox-capture` run (capture addendum #3)
  consumed it — appended **verbatim** to the origin filing
  (`inbox/2026-08-19-155515-…:82`, under the contract's dated amendment header, the
  already-relayed 08-21 comment correctly not duplicated), the `amended` label
  **removed in the same run** (tracker verified: #1 now
  `vault-filed,vault-accepted,captured` only), the issue left `captured` and open,
  **no re-materialized duplicate**, and the appended section joined that run's
  grounded set (folded into A10-19 as the same event's vault-side telling). Every
  fail mode absent. (4) unchanged STILL-OPEN — the 2026-08-23 triage batch (#8)
  contained only an accept; trigger remains the first batch with a genuine
  non-accept verdict (never manufactured).

- [ ] **build-B10-8 (dependency-record, briefed 2026-08-22):** brief
  `skills/reports/build-B10-8-dependency-record.md` (A10-9 under D6, both halves; seven
  brief-time dispositions clerk-resolved, autonomous run 2026-08-22, owner review
  pending — chiefly: the module-level declared set is `gh`/`uv`/`python3`/`git`
  (D6's pair + two grounding additions), the declaration is a merge-config-inert plain
  list read directly from `module.yaml`, the vault-grown record's single home is
  capability frontmatter `requires:` with explicit `[]` as the censused-none marker —
  no central manifest — and the census is a human-gated Step-3.5 offer). Five checks.
  **(1) `[ship-verifiable]`** — the declaration layer is on disk and inert where it
  must be: `module.yaml` carries the four-row `machine_tools:` block with the same-act
  writer clause; the fixture `merge-config.py` run proves the key never reaches
  `config.yaml` and the variable set is unchanged; the four-way agreement greps
  (`requires:` = template + mint + setup probe; `machine_tools_missing` = upgrade
  schema + Notes; `dependency-census` = bullet + enum) + package-lint A/B/C/E + Group E
  pass; discharged at rest, recorded in the BUILT status. **(2) `[ship-verifiable]`** —
  the arrival record reaches the persisted report: on the owner's next ordinary
  vlt-core upgrade, the Step-4 report renders `machine_tools_missing:` (empty form `[]`
  legal, absence a failure — never-omit), the persisted `_agent/upgrade-reports/*.yaml`
  verifies with the widened key set, and the Confirm Dependencies bullet carries the
  probe result (performer: the owner; vault: vlt-core). **(3) `[ship-verifiable]`** —
  the census offer fires where its population exists: the same vlt-core upgrade
  surfaces the dependency-census offer over vlt-core's vault-grown capabilities, writes
  `requires:`/`requires: []` only on per-capability owner confirmations, records
  `dependency-census` in `migrations_run` when any is censused, and a re-run offers
  only still-keyless capabilities (performer: the owner; vault: vlt-core). **(4)
  `[field-contingent]`** — declare-at-birth exercised by a real birth; discharging
  event named: **the next capability mint or self-grow in vlt-core after this release**
  (performer: the owner with a partner at the wheel; vault: vlt-core,
  factory-readable). Pass = the newborn capability carries `requires:` (or explicit
  `[]`) from its first commit; fail = a post-release birth with the key absent. **(5)
  `[field-contingent]`** — check-at-arrival catches a genuinely stranded toolchain;
  discharging event named: **the next `vlt-setup`/`vlt-upgrade` run on the work
  machine's vault** (performer: the owner; vault: the work-machine install — **a vault
  the factory cannot read**; evidence is the owner's report of the probe lines or a
  hand-saved Confirm/Step-4 excerpt). Pass = every genuinely missing declared tool
  surfaces as a named `tool-missing:` line with its degrade note and the run completes
  (report, never gate); an all-present machine discharges only the gating claim — the
  detection claim's could-have-failed form is a deliberate probe with one tool absent
  (e.g. `gh` off PATH).

  **Acceptance 2026-08-23 — split: (2)+(3) DISCHARGED; (4)+(5) STILL-OPEN.** (2): the
  persisted Step-4 report renders `machine_tools_missing: []` (present-when-empty) and
  verifies with the widened key set; the ledger Notes carry the probe result — module
  layer `gh`/`uv`/`python3`/`git` all present, vault-grown layer every censused tool
  present incl. the whisper large-v3-turbo model (`upgrade-ledger.md:312`). (3): the
  census offer fired over vlt-core's 20 vault-grown capabilities and the owner
  approved all 20 — 5 real tool lists (career-helper-toolkit, answer-key,
  walkthrough-renderer, sleeper-sync, ingest-youtube) + 15 `requires: []`
  censused-none markers, written into partner capability frontmatter
  (`_agent/partners/*/capabilities/*.md` grep confirms), with `dependency-census` in
  `migrations_run` (`upgrade-ledger.md:309`). (4): no capability birth since the
  release; trigger — the next mint/self-grow in vlt-core. (5): the work-machine
  vault has not run a 0.14.0 setup/upgrade; trigger — the owner's next run there,
  evidence hand-carried as the persisted file per the B10-6 transport caveat.
  First-run tails, no pass-through.

- [ ] **build-B10-9 (contract-overlay, briefed 2026-08-22):** brief
  `skills/reports/build-B10-9-contract-overlay.md` (Q2's narrow build; seven brief-time
  dispositions clerk-resolved, autonomous run 2026-08-22 — **✅ ALL OWNER-RULED 2026-08-23**
  (A15 live-ruled; the rest batch-confirmed) — chiefly:
  **A15 ruled POINTER, not exemption — ✅ OWNER-RULED 2026-08-23: POINTER CONFIRMED, no
  card-reading ceremony exempt, no new exemption minted** — the rule card carries a standing one-line
  conditional overlay pointer born of the R1 re-derive, no card-reading ceremony is
  declared exempt (the consult lite-boot stays exempt by its prior ruling); overlay name =
  resolved `{contract}` basename + `.overlay.md`; read rule single-homed in the contract's
  Durability section, zero per-skill restatements; no new lint finding class — existing
  overlay classes widen in population; mint route = the widened `convention edit` kind).
  Three checks. **(1) `[ship-verifiable]`** — the contract overlay shipped whole and
  agrees across its six homes: the contract clause (merged-on-read rule, the `:112`
  birth-time obligation discharged for the contract itself, the `{overlays}` zone-map row
  widened), the re-derived rule card carrying the A15 standing pointer with
  `derived_from:` re-stamped ≤ 8,000 bytes (**C6 PASS**), the `vlt-mint` route
  (council-gated, no-handshake, same-act rung line), the `checks.md:42` orphan/base
  resolution widening, the `vlt-upgrade:70` subsumption base clause, the `full-scale.md`
  declared `overlayNames` exclusion — all pointer-not-restatement, `vlt-lint-full.js`
  byte-untouched, **package-lint A/B/C/E PASS with Group E unchanged** (no bump, no walk);
  discharged at rest by the brief's greps + recorded verdicts. **(2) `[ship-verifiable]`**
  — the A9 seam holds with zero rung edits: the B10-5 fixture case (b) re-run against
  post-build text shows a contract-overlay pointer line VALID under the shipped rung
  population + falsifier, and the orphan desk-check shows the red-then-green pair (an
  unknown-name overlay still fires `overlay_orphan`; the contract overlay does not);
  discharged at rest. **(3) `[field-contingent]`** — the first live contract overlay is
  born, enforced, and survives; discharging event named: **the owner mints a vault-local
  contract-level addition in vlt-core via the widened `convention edit` route, then runs
  the subsequent upgrade** (performer: the owner with a partner at the wheel; vault:
  vlt-core — factory-readable; nothing schedules this event and the owner can legally seed
  it — a standing local operating rule is a natural candidate). Pass = the overlay lands
  at `_agent/conventions/vault-operating-contract.overlay.md` append-only with per-section
  declarations on rule-shaped sections, the rung pointer line + decision-log entry land in
  the same act, the next `vlt-lint` governance pass flags no `overlay_orphan` for it, and
  the next upgrade leaves it byte-intact while running the subsumption offer against the
  refreshed contract base. Fail = an orphan flag on a legal overlay, a mint closing
  without the rung line, a clobbered overlay on upgrade, or a contract-level addition
  hand-edited into the live contract because the route was unfindable.

  **Acceptance 2026-08-23 — (3) STILL-OPEN, unchanged (first discharge run on this
  tail).** No contract overlay exists in vlt-core — `_agent/conventions/` holds only
  `frontmatter.overlay.md`, and the 0.14.0 ledger states it directly: "No contract
  overlay exists yet (B10-9's `{overlays}` contract host is available but
  unexercised)" (`upgrade-ledger.md:306`). Trigger unchanged: the owner mints a
  vault-local contract-level addition via the widened `convention edit` route, then
  the subsequent upgrade proves survival. First-run tail, no pass-through.

  **Acceptance update 2026-08-23 (evening) — (3) split: birth-side DISCHARGED;
  STILL-OPEN: the lint no-orphan pass + upgrade survival.** The first live contract
  overlay was born via the widened `convention edit` route (session vlt-core-d4,
  council-gated, carry-back verified against the vault read-only): commit `92a0e5d`
  creates `_agent/conventions/vault-operating-contract.overlay.md` (§A the instrument
  rule — byte-fidelity comparisons use unwrapped instruments; no
  `version:`/`consumers:`/handshake keys, per-section declaration, append-only) **with
  the rung pointer line + decision-log entry in the same commit** (`reflexes.md` +
  `decision-log.md:1077` in the act's diff). Notably not seeded theater: the rule was
  already practiced three upgrades running (ledger `:272`/`:282`/`:307` cite "the
  standing instrument note"), and the mint surfaced that the note DID exist — as a
  trailing clause of the [2026-08-18] decision-log entry ref-keyed to an unrelated
  overlay, structurally unreachable by subject; the act closed it with a clause-scoped
  supersession (`decision-log.md:989`) rather than leaving two live homes.
  STILL-OPEN sub-clauses with triggers: the next `vlt-lint` governance pass flags no
  `overlay_orphan` for it (trigger: the owner's next lint run — scoped qualifies), and
  the next (v0.15.x) upgrade leaves it byte-intact while running the subsumption offer
  (trigger: the owner's next upgrade).

  **Acceptance update 2026-08-23 (evening, second) — the lint half DISCHARGED; only
  the v0.15.x survival half remains.** The first lint since the overlay's birth
  (`{lint_reports}/2026-08-23-1739-lint.yaml`): `overlay_issues: []`, and the report's
  `overlay_walk` records both overlays resolving a base —
  `vault-operating-contract.overlay.md → {contract}` **via the contract-basename
  rule** — with **no `overlay_orphan`**, heading-duplication computed against the
  resolved contract base (0 shared headings), and no handshake keys. The change-12
  read-path risk is **partially retired**: the lint-side reader demonstrably resolves
  the overlay; the partner point-of-use read (a contract-read applying the overlay
  mid-act) remains undemonstrated and stays the named residual on the survival half. **Named risk riding this check (the vault
  council's unresolved change 12):** the contract's read-the-base-then-apply-overlay
  clause is unverified at point-of-use — first live instance anywhere; if the read
  path doesn't resolve, the rule sits in a file nobody opens while the
  ledger-archaeology habit that carried it has been retired. A factory-side
  acceptance probe of the read path is the recommended discharge instrument.
  Companion field signal: issue #8 (vault-filed, field:candidate) proposes the rule's
  generic home in the shipped contract's *Honest reporting* section — triage pending.

- [x] **build-B10-10 (para-container-model, briefed 2026-08-22):** brief
  `skills/reports/build-B10-10-para-container-model.md` (A9-1 head under
  Q5/Q6/Q7/D2/E5/S1 + A2; sixteen brief-time dispositions clerk-resolved, autonomous run
  2026-08-22 — **✅ ALL SIXTEEN OWNER-RULED INDIVIDUALLY 2026-08-23** — chiefly: the A2 bump grounded as
  **frontmatter@11→@12** (B10-5 already took @11; B10-10 ships before B10-11 so the
  bump fires here, nine-leg walk) and **extraction@3→@4** (the enums land in
  `extraction.md`, three-leg walk) — **✅ OWNER-RULED 2026-08-23: both bumps CONFIRMED**,
  incl. the underlying call that the per-type `status:` enums are a schema rule change
  (bump + re-ack), not a prose clarification; the merge-config `vault_structure` fix is in scope as
  the ruled minting's mechanism — A7's "no key this arc" parenthetical is read as
  no-key-before-the-C6-b-fix, per the two shipped interim clauses (`full-scale.md:7`,
  contract `:48`) that both name that fix as their retirement trigger, and B10-10 is the
  build that carries it — **✅ OWNER-RULED 2026-08-23: conditional read CONFIRMED**, the
  arc-wide reading rejected on the record (see the dated note on A7 above); **the minted
  set of five is likewise OWNER-CONFIRMED 2026-08-23** (the widening past the two ruled
  PARA keys accepted — `handoffs` prevents re-manufacturing the A10-3 drop when the
  supplement is deleted, `upgrade_reports` discharges its own shipped `:48` clause,
  `resources` stands on B10-11's re-semanticization); five keys mint (`projects`/`areas`/`resources`/`handoffs`/
  `upgrade_reports`); the C1 re-draw is the two-named-write-surfaces rule (extraction +
  attributed container-maintenance appends — **✅ OWNER-RULED 2026-08-23: CONFIRMED
  as-shipped**, the narrow-to-extraction-only fallback recorded moot); the A11 calls: decider·pick
  + evidence-ledger idiom + declare-at-birth vocabulary ADOPTED, confidentiality
  DECLINED/WATCH with Maya's dissent standing — **✅ OWNER-RULED 2026-08-23: decline +
  watch CONFIRMED as-is, not converted to a bound debt; dissent preserved unchanged** —,
  trust-fork + propagation-debt DECLINED).
  Five checks. **(1) `[ship-verifiable]`** — both handshakes bipartite-consistent under
  one build: `frontmatter@12` across all nine legs (eight pins + the workflow ack) with
  both `vlt-lint-full.js:173` markers re-derived and re-stamped, `extraction@4` across
  all three legs, zero stale tokens; discharged at rest by **package-lint Group E
  (E1+E5) PASS** recorded in the BUILT status. **(2) `[ship-verifiable]`** — the
  parameterization is real end-to-end with a red-then-green record: `module.yaml` + the
  contract table carry the five keys (**E2 PASS**), the merge fixture proves key
  injection into a preserved map with overridden and vault-grown keys byte-intact and
  `structure_keys_added` reported (pre-fix red recorded), the R2 covering case +
  `CASE_FLOOR` bump landed, and both shipped interim clauses are gone — the
  `full-scale.md:7` supplement (D2 discharged; the derivation qualifies the new keys)
  and the contract `:48` upgrade-reports no-key clause — with `vlt-setup`/`vlt-upgrade`
  speaking `{upgrade_reports}`. **(3) `[ship-verifiable]`** — the model and re-draw
  shipped whole and agree across their homes: the five recitation sites carry the
  two-surface authorship rule (impossibility-form greps clean), `extraction.md:94`'s
  placeholder is a real per-type enum set with the coexistence + declare-at-birth
  clauses, the container section + `grounding:` definitions agree between
  `extraction.md` and `frontmatter.md`, `checks.md` carries the carve-out, the recast
  net rationale, the widened firewall (`method_in_grounding`), and
  `para_status_unknown` with legal responses (R3), `report.md` gains the slots
  additively, the rule card is re-derived ≤ 8,000 bytes (**C6 PASS**), six-case
  desk-check verdicts recorded; **package-lint A/B/C/E PASS**. **(4)
  `[field-contingent]`** — the container the field kept building arrives, honestly;
  discharging event named: **the first container birth in vlt-core after the owner's
  upgrade to the release carrying this build** (performer: the owner, or a partner at
  the wheel with the owner ratifying the charter; vault: vlt-core — factory-readable;
  vlt-core's live project work makes a birth a natural near-term event and the owner can
  legally seed one). Pass = a `{projects}/<slug>/` container with a ratified charter
  (`type: charter`, enum `status:`, honest `author:`), an attributed `record.md`
  maintained in place by the working partner (no shadow-tree flight to `_agent/`), and
  the next `vlt-lint` PARA pass reporting no
  `para_missing_attestation`/`para_status_unknown` against it. Fail = a new agent-zone
  shadow container for shareable work, a charter carrying a non-enum status, or the net
  firing on the model's own conformant files. *(Standing watches riding this check, not
  gating it: the confidentiality decline — Maya's dissent — and propagation-debt; a
  field signal on either files to `inbox/`.)* **(5) `[field-contingent]`** — the minted
  keys survive a live merge and feed the derivation; discharging event named: **the
  owner's next vlt-core upgrade (the release carrying this build, expected v0.14.x)
  followed by the owner's next `vlt-lint` full-mode run** (performer: the owner; vault:
  vlt-core; evidence: the vault's `config.yaml` + the persisted
  `{lint_reports}`/`{upgrade_reports}` files — all factory-readable; same lint event
  class as the open B10-2(5)/B10-3(3)/B10-6(6) tails — one run can feed them all).
  Pass = `config.yaml`'s `vlt:` `vault_structure` carries the five new keys with every
  pre-existing override and vault-grown key byte-intact (the merge report naming
  `structure_keys_added`), and the lint run's `missing_targets` contains no valid link
  into `projects/`/`areas/`/`resources/`/`_agent/handoffs/` (the derived set now covers
  them with the supplement gone). Fail = a dropped or clobbered map key, a
  supplement-era false-positive class returning, or the keys present in `module.yaml`
  but absent from the vault's merged config.

  **Acceptance 2026-08-23 — split: (5) DISCHARGED; (4) STILL-OPEN.** (5): vlt-core's
  merged `_bmad/config.yaml` `vault_structure` carries all five minted keys
  (`projects`/`areas`/`resources`/`handoffs`/`upgrade_reports`) plus the new
  `wiki`/`index` defaults, with the vault-grown `dog_training_root:` byte-intact and
  `module_keys_removed: []` / `module_keys_defaulted: []` (ledger records the gains
  explicitly, `upgrade-ledger.md:312`); the full lint's `missing_targets` contains no
  valid link into `projects/`/`areas/`/`resources/`/`_agent/handoffs/` — the
  supplement-era false-positive class did **not** return (the 12 false flags this run
  are a different, pre-existing class — `[[index]]`/`sources/`/`.base`, graded at
  B10-2(5) and filed there; not this check's population). (4): no container birth yet —
  zero `type: charter` files under `projects/` (`projects/`+`areas/` were created by
  this upgrade as new homes); the PARA net ran honestly over pre-model files (26
  `para_missing_attestation` in jurisdiction with the 32-file scope exemption stated,
  2 post-adoption `para_status_unknown` loud with both legal responses offered) and
  fired on no conformant file (vacuously — none exists yet). Trigger unchanged: the
  first container birth in vlt-core (owner may legally seed one). First-run tail, no
  pass-through.

  **Acceptance update 2026-08-23 (evening) — (4) DISCHARGED, item complete.** The
  vault's first container birth landed (session vlt-core-d4, commit `534e82f`, owner
  ratifying): `projects/fantasy-2026/charter.md` — `type: charter`, `author: hybrid`
  (partner-drafted, human-ratified — honest), `status: open` **inside the
  project-container enum** (`open|paused|closed`), `grounding:` with 7 entries all
  resolving on disk; an attributed `record.md` opened in place beside it (no
  shadow-tree flight). The evidence lint (`2026-08-23-1739-lint.yaml`, commit
  `f9049da`, `fixes_applied: []` by owner instruction): the **container carve-out
  fired correctly on its first real instance** — charter + record exempt from the
  attestation pair per the container schema, while the two `type: project` artifact
  files beside them still flag `para_missing_attestation` (the right discrimination);
  `para_status_unknown` resolved for both artifacts (owner ruled map-to-enum:
  `active` → `in-progress`, no vocabulary grown, ruling in `rulings_recorded:`).
  The net fired on none of the model's own conformant files. Fail modes absent.
  Side signal, FILED on owner confirmation 2026-08-23:
  `inbox/2026-08-23-190200-undeclared-para-type-is-invisible-to-both-nets.md` — a PARA
  file with an undeclared `type:` (`draft-night-dashboard-intent.md`, `type: note`,
  `author: creative`) is invisible by construction; both nets correctly decline,
  summing to no coverage.

- [x] **build-B10-11 (wiki-move-capstone, briefed 2026-08-22):** brief
  `skills/reports/build-B10-11-wiki-move-capstone.md` (A9-1 residual item 7 under Q6/E6 +
  A2/A10; **Q6 risk verdict made at brief time: BRIEF — the fallback does not fire** (the
  design risk retired by B10-10, the field relocation bounded by the map's decline-path
  override, the standing relocation discipline, and the practiced walk; S1 cited legally
  under the verdict) — **✅ OWNER-RULED 2026-08-23: verdict CONFIRMED on grounds (1)–(3);
  ground (4) ("the cut is isolated by A10") is SUPERSEDED by the D1 option-C ruling —
  B10-11 ships in the one v0.14.0 cut and its acceptance run is entangled, ruled
  acceptable because the same cut carries B10-12's repair to the instrument that reads a
  relocation**; clerk-resolved dispositions, autonomous run 2026-08-22, owner
  review pending — chiefly: new home `wiki: resources/wiki/` + `index:
  resources/wiki/index.md` (bounded subtree; `resources` key kept, re-semanticized),
  `type: resource` retires by grandfathering (no backfill; reference material routes to
  the browsable wiki or `areas/`), the migration is a human-gated offer whose decline
  path writes the two pinning overrides, and E6's census = the denominated
  `attestation_census:` full-mode line computed in the workflow reduce with zero prompt
  changes). ~~**Ships as its own cut, alone** (roundtable A10).~~ **SUPERSEDED by the D1
  ruling (owner, option C — one cut): B10-11 ships inside v0.14.0 with B10-6..B10-10 and
  B10-12.** Six checks. **(1)
  `[ship-verifiable]`** — both handshakes bipartite-consistent under one build:
  `frontmatter@13` across all nine legs (both `vlt-lint-full.js:173` markers re-derived,
  rule 4 untouched, re-stamped) and `extraction@5` across all three, zero stale tokens;
  discharged at rest by **package-lint Group E (E1+E5) PASS**. **(2)
  `[ship-verifiable]`** — the move coherent across every home: the two new defaults in
  all three structure-map homes (**E2 PASS**), rule card re-derived ≤ 8,000 bytes (**C6
  PASS**), the two-folder Layer-3 enumeration + two-named-surfaces sentence agreeing at
  every recitation site, `_agent/wiki` surviving only in the migration bullet's
  firing/decline text, no shipped text offering `resources/` as an extraction target;
  **package-lint A/B/C/E PASS**; discharged at rest by the brief's greps. **(3)
  `[ship-verifiable]`** — E6 shipped whole same-build: `checks.md:16` census + R3
  response, `report.md` `attestation_census:` slot (existing slots stable), workflow
  reduce computing it with `PAGE_SCAN` and every prompt byte-untouched (R4 fan-out audit
  re-run recorded), four-page desk-check rendering the denominated line; discharged at
  rest. **(4) `[ship-verifiable]`** — the release gate, own cut: dual bump,
  `--expect-version` exit 0 with the PASS line in the release commit, ff-merge + tag +
  push per `vlt-release`. **(5) `[field-contingent]`** — the relocation offer runs
  honestly; discharging event named: **the owner's vlt-core upgrade to the release
  carrying this build** (performer: the owner; vault: vlt-core — factory-readable;
  evidence: the persisted `_agent/upgrade-reports/*.yaml` Step-4 report + a factory
  read). Pass, accept = wiki whole at `resources/wiki/` (page count preserved), one-line
  stub at `_agent/wiki/index.md`, open dispatch pointers re-pointed, `migrations_run`
  carries `wiki-relocation`, next activation reads the `{index}` at its new home; pass,
  decline = both overrides in `config.yaml` with every skill resolving the old home.
  Fail = a half-moved wiki, a clobbered worktree copy, an orphaned open pointer, or a
  declined offer leaving default resolution at an empty `resources/wiki/`. **(6)
  `[field-contingent]`** — the census reads the browsable wiki honestly at scale;
  discharging event named: **the owner's first full-mode (>30 pages) `vlt-lint` run on
  vlt-core after the relocation** (performer: the owner; vault: vlt-core; evidence: the
  persisted `{lint_reports}` `.yaml` — same event class as the open
  B10-2(5)/B10-3(3)/B10-6(6)/B10-10(5) tails, one run can feed them all). Pass = a
  denominated `attestation_census:` whose `pages_total` matches the moved wiki, no new
  path-shaped `missing_targets` class, no wiki page double-reported as a cross-layer
  target, human edits appearing in the census counts rather than a new loud class; fail
  = a missing/undenominated census line, a mass `attestation_stale` loud class, or a
  move-born missing-target class.

  **Acceptance 2026-08-23 — split: (6) DISCHARGED; (5) relocation-side DISCHARGED,
  activation-read tail STILL-OPEN.** (5), accept path taken: the owner accepted the
  offer — 147 pages moved whole `_agent/wiki/` → `resources/wiki/` via main-tree-only
  `git mv`; the one-line stub stands at `_agent/wiki/index.md` (255 B, "Wiki has
  moved"); no open dispatch pointer carried an old-path doc reference (the one
  `dispatch.md` mention is body prose, resolvable through the stub);
  `migrations_run: [wiki-relocation, …]`; `vault_structure.wiki`/`index` updated to
  the new defaults; `{archive}` mirror untouched (`upgrade-ledger.md:309`). STILL-OPEN
  sub-clause: "next activation reads the `{index}` at its new home" — no post-upgrade
  partner session yet; trigger: the owner's next vlt-core session (the same event as
  B10-5(5)'s activation tail — one session feeds both). (6): the full lint renders a
  denominated `attestation_census: {pages_total: 145, fresh: 100, stale: 2,
  unattested_pre_adoption: 43}` (partition sums; pages_total matches the scanned
  moved wiki), human edits appear in the counts not a loud class, `attestation_stale`
  is 2 entries (no mass class), and the missing-target false flags are **not
  move-born** — the identical `[[index]]`/`.base` flags appear in the pre-move
  2026-08-16 report (its `missing_targets` note), so the class predates the
  relocation and is graded at B10-2(5), not here.

  **Acceptance update 2026-08-23 (evening) — (5) activation tail DISCHARGED, item
  complete.** The first post-upgrade partner session ran (football-analyst,
  16:15–17:09, session note `2026-08-23-161500-misc.md`) and activated without error
  under the new resolution ({index} → `resources/wiki/index.md`; the old home a
  redirect stub). Behavioral pass — the Beat-1 read leaves no per-session trace, but
  the discharging event occurred and no fail mode fired (no activation error, no
  resolution at the empty old home). Same event as B10-5(5)'s tail, recorded on both.

- [ ] **build-B10-12 (lint-full-execution-repair, briefed 2026-08-23):** brief
  `skills/reports/build-B10-12-lint-full-execution-repair.md` (A10-16 + A10-17; DA4..DA8/DA11;
  D1 RULED option C). Six checks. **(1) `[ship-verifiable]`** — partial-failure fixture: an
  injected partial agent failure (some `null`, some `available:false`) makes the workflow emit
  a coverage cap naming **count + reason-partition + failed slugs**, the findings report shape
  intact, `missing_targets` computed against the filesystem-truth `pageSlugSet` carries **no**
  false missing for a surviving-but-unscanned real page, and `orphans`/`near_duplicates` are
  suppressed with their cap; discharged at rest by the fixture smoke run. **(2)
  `[ship-verifiable]`** — near-total-shortfall fixture: a below-majority run
  (`scans.length < ceil(pages.length/2)`, and the `scans.length === 0` sub-case) returns the
  `status:'failed'` error shape, never a findings report; discharged at rest by fixture. **(3)
  `[ship-verifiable]`** — SKILL refusal: a `files_checked: 0` (stale-workflow) report is refused
  by `vlt-lint` — not persisted as findings, `lint-debt` not reset, a dated `…-lint-failed.yaml`
  record written, a directed version-skew refusal surfaced; discharged by the workflow
  error-path fixture (executable half) + a grep that `full-scale.md`/`SKILL.md` carry the guard
  (prose half) — the two halves named per the B10-2 non-executability lesson. **(4)
  `[ship-verifiable]`** — schema-size budget: package-lint `_e6` asserts every shipped workflow
  fan-out schema serializes ≤ 3,700, `PAGE_SCAN` post-trim is under 3,700, and the check has a
  **failable** covering case in `tools/test-package-lint.py` (E4/R2) with `CASE_FLOOR` bumped
  22→23; discharged at the release gate. **(5) `[ship-verifiable]`** — executability proof:
  `node --check` + a real fixture run of `vlt-lint-full.js` execute end-to-end (the B10-2
  non-executability class cannot recur undetected); discharged at rest by the smoke run.
  **(6) `[field-contingent]`** — the B10-2(5) re-discharge: an **executing full-mode sweep**
  (`files_checked ≈ files_listed`), degrading loudly if it degrades at all, passing B10-2(5)'s
  original criteria **as amended by DA9** — no no-prose-only false `sources_vs_prose` page; no
  valid `_agent/handoffs/`/`areas/`/`projects/` (post-B10-11 zone map) `missing_targets` **and
  no target that exists on disk as a wiki page**; no new false-positive class. Discharging
  event: **the owner's first full-mode (>30 pages) `vlt-lint` sweep on vlt-core after the
  v0.14.0 upgrade** (performer: the owner; vault: vlt-core; evidence: the persisted
  `{lint_reports}` `.yaml`). This one run carries **three ledger consequences** (DA9) — it
  discharges this check, is B10-12's field-acceptance event, and sizes-or-collapses the residual
  `normalizeTarget` seam; record the single run against **both** the B10-2(5) and B10-12(6)
  entries. E6's attestation-census checks are re-verified at rest on the post-B10-12 file (DA7)
  under check (1), not a separate field event.

  **Grounding at brief time (2026-08-23):** all capture/DA sites re-verified against
  `vlt-lint-full.js` @ `7a4b1a8` — HOLDS except one off-by-one: the callout-seed gate DA7 cites
  as `:341` is at **`:340`** at HEAD (`if (!target || !slugSet.has(target) …`); substance
  unchanged, F5 rewires it to `pageSlugSet`. DA7's `:270`-is-the-index-pass correction is
  confirmed at HEAD.

  **Field acceptance 2026-08-23 — (6) FAILED, narrowly; the repair itself is
  field-proven.** The DA9 single run (the first post-0.14.0 full sweep,
  `{lint_reports}/2026-08-23-1504-lint.yaml`) is recorded against both this entry and
  B10-2(5) — full verdict text at B10-2(5). What B10-12 shipped **worked in the
  field**: the sweep executed end-to-end (145/146, vs 1/146 on 0.13.0), the one agent
  shortfall degraded loudly (`coverage_caps` names the page and reason), inbound-derived
  checks were suppressed as `unmeasured` rather than fabricated, no vacuous clean
  report, and the persisted `.yaml` parses whole — checks (1)-(5)'s at-rest claims held
  live. The FAIL is the amended criteria's missing-target leg: 12/12 workflow-returned
  missing targets are false positives from the `crossLayerSlugs` derivation (3×
  `[[index]]`, 8× `sources/`, 1× `.base` — the first and last persisting from the
  pre-B10-2 class). The DA9 third duty is discharged: the residual seam is **sized**
  (12 hits, three causes), not collapsed. One inbox filing covers it (drafted this
  run, see B10-2(5)); routes into the next `inbox-capture`.

## Owner review of clerk dispositions — 2026-08-23

Every clerk-resolved call in the arc's **second half** (B10-6..B10-12, built autonomously on
`arc10-v0.14.0`) plus the roundtable delta's **DA1..DA11** was put to the owner before release.
**Outcome: every disposition CONFIRMED. Nothing rejected, no rework, no shipped code edited.**
Two follow-up filings were opened and one release-time obligation was created (below).

**Method.** The owner ruled the load-bearing calls **one at a time in-chat**, each presented with
its grounded facts, `file:line` sites, downstream cost and the clerk's recommendation (the
repo's standing "full context in chat" posture). Partway through, the owner **filtered the
remainder**: four calls were pulled out for live rulings and the rest confirmed as one dated
**batch disposition** — an owner-chosen procedure, precedent Arc 3's closeout batch. Each ruling
was written into its brief (and, where the disposition lives there, the roadmap) in the same
turn. Rulings are reversible at arc close.

**Ruled individually (35):** B10-10 all sixteen · B10-11's Q6 verdict + all eight · B10-6 all
eight · B10-7's disp. 1–2.

**Live rulings after the filter (4):** L1 B10-9's A15 (POINTER) · L2 B10-7's disp. 7 (the literal
@mention) · L3 B10-12's two owner-adjustable numbers · L4 DA3's flagged owner action.

**Batch-confirmed (36):** B10-7 disp. 3,4,5,6,8 · B10-8 all seven + R1 · B10-9 disp. 2–7 + R1 ·
B10-12 disp. 2,4,5,6,7,8 · DA1, DA2, DA4–DA11. Each carries a dated batch marker at its own site.

### Rulings that changed the record, not just confirmed it

- **B10-10 disp. 3 / roundtable A7 — the reading is CONDITIONAL, not arc-wide.** "No
  `vault_structure` key is minted this arc" means *no key before the C6-b merge-config fix*; the
  build that clears the fix may mint in the same act. The arc-wide reading is **rejected on the
  record**, stamped at A7's own entry. B10-10 stands whole (five keys, both interim clauses
  deleted).
- **B10-10 disp. 10 — the authorship re-draw CONFIRMED.** Layer 3's boundary is
  authorship-honesty with **two named partner write-surfaces** (extraction + container
  maintenance). The narrow-to-extraction-only fallback is recorded **moot**. The owner accepted
  the widening explicitly as bounded (append-only, `record.md`/`register.md` only, per-entry
  attribution, charters human-gated).
- **B10-6 disp. 1 — the A1 hand-save posture RETIRES** at this cut. Factory discharge reads the
  persisted `_agent/upgrade-reports/*.yaml`; a factory-unreadable vault hand-carries **the
  persisted file itself**, never a transcript. Stamped at A1's own entry.
- **B10-11 Q6 — verdict BRIEF confirmed on grounds (1)–(3); ground (4) SUPERSEDED.** "The cut is
  isolated by A10" is falsified by the owner's D1 option-C ruling. Entanglement ruled acceptable
  because the same cut carries B10-12's repair to the instrument that reads a relocation.
  Accepted cost on record: harder attribution if the v0.14.0 acceptance run goes sideways. The
  stale "ships as its own cut, alone" commitment is struck at the B10-11 ledger bullet.
- **B10-11 disp. 8 — the shipped sweep came out cleaner than declared** (context (b) has no
  surviving instance); the brief's three-context declaration is reconciled against the tree.
  B10-11's **three numbered deviations accepted** as briefed-rule-reaching-unenumerated-sites.
- **B10-12 disp. 1 & 3 — two standing numbers SET by the owner**, not merely confirmed: the
  package-lint fan-out **schema-size budget ≤ 3,700 serialized chars**, and the **majority**
  coverage floor (`scans.length < ceil(pages.length/2)` → error, never a findings report).
- **B10-7 disp. 7 — KEEP LITERAL, with the residue named.** The `@mggower` trigger stays for
  v0.14.0 (a non-literal mention notifies nobody and would strand the channel); the personal
  handle in the public surface and the single-person failure mode are accepted on record, bounded
  by `.github/` never being part of the own-the-apply copy surface.

### Obligations created

1. **DA3 — release-time.** The known-issue notice (full-mode lint untrusted on 0.13.x) lands in
   the **v0.14.0 release notes / CHANGELOG entry**; no pinned tracker issue (exposure window too
   short, repair release-ready). `vlt-release` Stage 3 authors that entry — **the notice text
   must be included there, and DA3 retires with it.**
2. **Filing (L2).** `inbox/2026-08-23-110913-amendment-trigger-should-not-be-a-personal-handle.md`
   — move the amendment trigger to the repo's watch/subscription. Arc 11 candidate.
3. **Filing (DA11 / B10-12 disp. 7).**
   `inbox/2026-08-23-111410-council-consult-partial-lens-shortfall-is-silent.md` — the declined
   lens-shortfall cap, filed forward as ruled. Arc 11 candidate.

### Standing watches unchanged by this review

Confidentiality-as-container-attribute stays **DECLINE + WATCH** (explicitly *not* converted to a
bound debt) with **Maya's dissent preserved unchanged**; propagation-debt stays DECLINE + WATCH.
E5's laundering watch is **retired, not released** — closed by construction by `grounding:`'s
firewall inheritance.

### Out of scope of this review

B10-1..B10-5 shipped in v0.13.0 and their briefs still carry
"autonomous run 2026-08-21, owner review pending" markers (B10-4 and B10-5 ledger bullets
included). This session reviewed the **second half only**; those remain open for review at arc
close.

## Owner review of clerk dispositions — first half (2026-08-23)

**RESOLVED — the review debt above is cleared.** All **36 first-half dispositions**
(B10-1: 7 · B10-2: 7 · B10-3: 7 · B10-4: 7 · B10-5: 8) put to the owner and
**CONFIRMED**, with the advantage the second-half review lacked: every build was
field-exercised first, so each call was reviewed against live evidence. **Four
live-ruled:** L1 B10-4 disp. 1 — direction 2 CONFIRMED **with a premise correction on
record** (the "lost derive was a count-shape" justification is false in the field — it
is a content-filtered count, inexpressible under the kinds, the B10-4(4) BLOCKED cause;
the bound's stated escape route worked: A10-19 filed); L2 B10-2 disp. 2(+3) — the
qualifying-key predicate CONFIRMED as-shipped-with-known-costs (the A10-18 seam is its
priced residue, fix at `full-scale.md:7` in Arc 11 per the clerk's own
named-editable-classes design); L3 B10-2 disp. 1 — the required tri-state enum
CONFIRMED (its cost, the schema-size regression, named; B10-12 its repair; the
tri-state field-proven 2026-08-23); L4 B10-5 disp. 1+2 — the "chiefly" pair CONFIRMED
as field-proven. **The remaining 32 confirmed as one dated batch** (second-half
precedent) — all field-clean or unexercised with no contrary signal. Each brief carries
its dated stamp at the head of its dispositions section. **No first-half review debt
remains — arc-closeout's precondition is met.**

## Capture addendum — 2026-08-23 (mid-arc, third exercise)

*Two filings grounded against the shipped release **v0.14.0 @ `283fe5d`** (tag `55b739d`),
folded under the mid-arc posture (platform P-4; the 2026-08-22 addenda are the shape
precedents). Both descend from the 2026-08-23 acceptance-discharge run over the vlt-core
0.14.0 upgrade — they are the two **negative** grades that run produced, and each filing is
its grade's rubric-mandated routing: A10-18 is B10-2(5)/B10-12(6)'s **FAILED (narrowly)**
missing-target leg, A10-19 is B10-4(4)'s **BLOCKED (unreachable)** re-grade. **Run scope
(owner-ruled in-session):** this run covered **the ledger-blocking pair only** — the other
five un-captured filings on disk (…-110913, …-111410, …-180100, …-180200, …-190200) and the
newly materialized …-210653 were explicitly held for a later run and remain un-captured;
they are **not** silently deferred, they are on disk with no roadmap entry, and the next
capture run owns them.*

*__Owner ruling on this batch (2026-08-23, both filings):__ **HOLD FOR ARC 11** — ground now,
mint no build. The B10-12 escalation precedent explicitly does **not** apply: v0.14.0 has
shipped and every Arc 10 build is done, so nothing is release-blocked and the mid-arc
escalation lever has no work to do. Neither filing widens an unbuilt build's scope, because
Arc 10 has no unbuilt builds left. **No `joint moved` on either** — an Arc-11 routing moves
no Arc-10 joint, so no roundtable delta is convened.*

*__GitHub intake (ran first, per Discovery).__ Query returned eight open `vault-accepted`
issues. **#8 materialized** → `inbox/2026-08-23-210653-instrument-rule-for-byte-exact-comparisons.md`
(`rail_contract: 1`, matches the current contract — no stale-shape hold; `captured` applied,
issue left open). Its two pre-materialization comments (the 2026-08-23T21:33:18Z triage
grounding and the 2026-08-23T21:55:12Z **second field instance** — the wrapped `find
-newermt` scoping bite, which argues the rule's trigger should be "any instrument a verdict
rests on", not "byte-exact verdicts") were appended to the filing verbatim as a thread
record so the second instance is not lost at capture; neither is an `amended` consumption
(#8 never carried the label). #2–#7 already carry `captured` and are consistent on disk —
skipped by the `origin:` idempotency key, no drift. **Amendment leg:** #1 (`captured` +
`amended`) consumed — its 2026-08-23T21:55:08Z comment appended verbatim as a dated
amendment section to `inbox/2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md`
(its 2026-08-21 comment was already on the filing, hand-relayed, and was not duplicated),
`amended` removed in the same run, issue left `captured` and open, filing not
re-materialized. That amendment tells A10-19's story from the vault side and is captured
with it below rather than as a separate entry. This is the rail's **first machine-run
amendment cycle** — B10-7(3)'s acceptance evidence.*

### A10-18. The missing-target check cannot be trusted until `crossLayerSlugs` reaches `sources/`, `{index}`, and non-`.md` linkables (2026-08-23) — …-160500-crosslayerslugs-blind-to-sources-index-and-non-md-linkables.md

**GAP CONFIRMED ×3 at the shipped v0.14.0 — all three causes verified against source, and
the filing's site attribution is corrected: none of the three lives in `vlt-lint-full.js`.**
The filing names "the `crossLayerSlugs` derivation (`vlt-lint-full.js`, the qualifying-key
predicate)". The workflow does **not** derive `crossLayerSlugs` — it only *consumes* the
array (`skills/vlt-setup/assets/workflows/vlt-lint-full.js:84` normalizes the passed
array; `:281` builds the `crossLayer` Set for the missing test). The derivation, and the
qualifying-key predicate itself, are **single-homed in the SKILL reference**:
`skills/vlt-lint/references/full-scale.md:7`, which says so in its own parenthetical
("*This predicate is single-homed here — other sites point at it, never restate it*").
**Any fix is a `full-scale.md:7` edit, not a workflow edit** — which also means it costs no
`.js` change, no `// depends_on:` re-ack, and no version bump.

- **Cause 1 — `{index}` is in neither population (3 hits).** `full-scale.md:7` builds the
  page list by globbing `{wiki}` for `*.md` **"(excluding `{index}`)"**, and the
  qualifying-key predicate excludes the wiki's own key (`wiki`) from the cross-layer set.
  `index` *is* a `vault_structure` key (`skills/vlt-setup/assets/module.yaml`,
  `vault_structure.default`: `index: resources/wiki/index.md`) but it resolves to a **file,
  not a directory**, so the predicate's "resolved value names a *directory*" test excludes
  it a second time, independently. `[[index]]` is therefore missing by construction, from
  two directions.
- **Cause 2 — `sources/` has no structure-map key at all (8 hits).** Confirmed against the
  canonical map: `vault_structure.default` carries 23 keys and **`sources` is not among
  them**. The predicate operates over *resolved map keys*, so it cannot admit a zone the map
  never names — this is not a predicate bug but a map gap, and it is the one cause of the
  three that B10-2 could not have caught (it is a real vault zone that never existed as a
  key). Note the near-miss that makes this easy to misread: `resources: resources/` **is** a
  qualifying key, and `sources/` is a *sibling* of `resources/`, not a child — the
  resemblance is orthographic only.
- **Cause 3 — the linkable set is `*.md`-only (1 hit).** `full-scale.md:7`: "Glob each
  qualifying key's directory for **`*.md`** basenames". `[[_agent/bases/wiki.base]]` is a
  legal link to a file the glob cannot see. Note the interaction with B10-11: that build
  removed report dirs and cold storage from the qualifying set, but never touched the
  extension filter, so the `.base` class survived every Arc-10 lint repair untouched.

**The filing's "persisting class" claim holds, and is the exact wording B10-2(5) fails on.**
B10-2 replaced a hardcoded root list with derivation from resolved `vault_structure` keys —
which is why `handoffs`/`areas` are confirmed gone this run — but causes 1 and 3 are
orthogonal to *where the roots come from*, so the fix could not have reached them. B10-2(5)'s
fail wording ("any class persists or returns under a new name") fires correctly.

**Residual scope after grounding:** smaller than the filing implies. All three causes are
edits to one sentence-group at `full-scale.md:7`; the workflow, the reduce, and the report
contract are untouched. What is *not* small is cause 2's design question, below.

> **Open design questions — carried verbatim, unresolved (ideation's, not capture's):**
> whether `sources/` should become a `vault_structure` key (the B10-10 minting route exists
> now), whether `{index}` joins the cross-layer set or the page population, and whether the
> linkable set widens past `*.md` (`.base` today; the general class is "non-markdown files
> the vault legally links").
>
> *Capture adds one framing note, not an answer:* the three questions are **not** one
> question. 1 and 3 are predicate-shape questions answerable from module source alone; 2 is
> a **structure-map** question whose answer changes the shipped canonical map for every
> vault, and it is the only one of the three that could reasonably be ruled the vault's
> business rather than the module's.

- **Ruled into:** **no build — HOLD FOR ARC 11** (owner, 2026-08-23). Explicitly *not* an
  in-arc escalation: unlike A10-16/A10-17, nothing is release-blocked (v0.14.0 shipped) and
  there is no unbuilt Arc-10 build whose scope this could widen.
- **Ledger consequence (recorded here so closeout cannot lose it):** at `arc-closeout` the
  **B10-2(5) / B10-12(6) FAILED** missing-target item carries forward as **bound inherited
  debt to Arc 11**, gated on the Arc 11 build that lands this fix, and its re-check is
  tagged **ship-verifiable so it gates** — the A4-4(5) lesson applied preemptively, the same
  way B8-2(4) was bound into Arc 9. Re-discharge = a full sweep whose missing-target flags
  survive verification (or a measured zero) after the predicate gains all three populations.
- **Joint test:** `joint moved: none` — an Arc-11 routing moves no Arc-10 joint; no
  roundtable delta.

### A10-19. `local_metrics:` cannot express a content-filtered count — the exact derive class issue #1 lost has no vault-local home (2026-08-23) — …-190100-local-metrics-kinds-cannot-express-a-content-filtered-count.md

*Captured together with the **issue #1 amendment** consumed by this run's intake leg (the
vault-side telling of the same event). Filing = factory-side grounding of the BLOCKED grade;
amendment = the field's own correction of issue #1's framing. They agree on every fact.*

**CONFIRMED at the shipped v0.14.0 — every cited site re-derived, and the filing's core
claim is exactly right.** `LOCAL_METRIC_KINDS = {"file_count", "bytes", "days_since_newest"}`
verbatim at `skills/vlt-setup/assets/hooks/vlt-vitals.py:251` (the filing's cited line,
correct); the locator table on the next line (`:252`) binds each kind to `glob`/`path` only,
and `file_count`'s implementation is
`sum(1 for f in vault_root.glob(spec) if f.is_file())` (`:395`) — a pure path predicate with
**no content read anywhere in the evaluator**. A count of pages whose *frontmatter carries a
key* is therefore inexpressible, and declaring it as `file_count` over `{wiki}/**/*.md`
would count every page and label the result a key-carrier count — a fabricated metric. The
vault's refusal to declare it was correct.

**The bound is stated in the module's own text, twice, and the filing quotes it accurately.**
`skills/vlt-setup/assets/tripwires.yaml:16-18`: "a derive beyond those kinds has no
vault-local home; its route is an upstream filing for a new canonical metric or a new kind
(the same route METRICS additions take), never a hand-edit of the module-owned reader"; the
reader restates the routing at `vlt-vitals.py:248-250`. **This filing is that route being
walked as designed** — the shipped bound working, not failing. What makes it a defect rather
than a clean referral is the acceptance consequence: B10-4(4) asked a vault to discharge by
declaring its lost derive, and for any vault whose lost derive was content-filtered, no
shipped surface can produce the discharging event. Per the rubric that is **BLOCKED**, not
STILL-OPEN — waiting cannot discharge it.

**One grounding sharpening the filing does not have (and which trims direction 3's case).**
The filing argues `expired_pages: 0` is "ambiguous between *nothing is stale* and *nothing
carries the key*". At v0.14.0 that ambiguity is **already partly closed in source**:
`vlt-vitals.py:631-634` emits a note beside the metric —
`f"{scanned} pages scanned; a page without \`review_after:\` is evergreen and cannot
expire"`. So the module *does* state a denominator and *does* name the evergreen semantics;
what it does not state is the **key-carrier count** (`scanned` is all pages under
`{wiki}` + `{research}`, `:617-630`). The honest-reporting argument for direction 3 is
therefore narrower than filed: not "the denominator is missing" but "the *stated*
denominator is the wrong one for judging staleness coverage". Direction 3 still stands on
its merits; its rhetorical case is smaller.

**PROVENANCE CORRECTION carried from the amendment (the field correcting its own earlier
filing).** Issue #1 was filed as an *upgrade-clobber* story. The amendment retracts that:
vlt-core never hand-edited `vlt-vitals.py`, and the loss was a **silent supersession at
install** — the vault's pre-module `_agent/vitals.sh` (6 derives) was superseded by the
shipped hook at 0.9.0, five derives carried into canonical `METRICS`, and
`pages_with_review_after` did not. No divergence report named the drop, because
supersession-at-install has no analogue of the divergence net that guards upgrades. **This
matters for scope:** the durable-host doctrine (B10-4's own frame) protects against
overwrite, and overwrite is not what happened here — so a durability fix would not have
prevented this loss.

> **Open design questions — carried verbatim, unresolved:** (1) a content predicate on
> `file_count` — an optional `matching:`/`frontmatter_key:` filter on the glob (smallest
> change; keeps the bounded-kinds posture); (2) a fourth bounded kind
> (`frontmatter_key_count` or similar); (3) promote `pages_with_review_after` to the
> canonical `METRICS` table. "Directions 1/2 solve the class; direction 3 solves this
> instance and is defensible on its own merits. Not mutually exclusive."
>
> **Carried as context, deliberately not a second filing (the filing's own choice, honored
> here):** whether install/first-provision owes a "superseded local instrumentation" report
> line — the gap the provenance correction exposes. Ideation may promote it; capture does
> not.

- **Ruled into:** **no build — HOLD FOR ARC 11** (owner, 2026-08-23), same reasoning as
  A10-18.
- **Ledger consequence:** **B10-4(4)** carries forward at closeout as **BLOCKED
  (unreachable)**, gated on the Arc 11 build that gives a content-filtered derive a home.
  Recorded per the rubric: a BLOCKED item is not discharged by waiting, so it must not be
  released as a watch.
- **Joint test:** `joint moved: none`.

### Addendum joint test — 2026-08-23

**`joint moved: none`, both filings.** No cross-build dependency, ordering, or interim
posture moves: both are routed *out* of Arc 10 entirely, into an arc with no plan yet to
disturb. **No roundtable delta convened.** The two ledger consequences above are closeout
bookkeeping (`arc-closeout` Stage 1 reads them), not plan joints.

**What this addendum deliberately does not do.** It mints no build, so `build-brief`'s
record gate has nothing to read here — correctly. Arc 11's roadmap does not exist yet and is
not created by this run: it is written by the capture run that follows `arc-closeout`, which
will re-ground these two filings' entries alongside the six still-un-captured filings and
the materialized #8, and inherit the two bound-debt items above.

## Next lifecycle move

**✅ v0.14.0 SHIPPED 2026-08-23** @ `283fe5d`, annotated tag `v0.14.0` (`55b739d`) pushed to
the public remote — the single option-C cut, builds B10-6..B10-12. Gate record: handshake
bipartite-consistent (9 conventions / 35 pins); `uv run tools/package-lint.py --expect-version
0.14.0` → **A/B/C/E PASS, D PASS**, exit 0 (verbatim line carried in the release commit); true
ff-merge to `main`, annotated tag, explicit-refspec push (`full-history` untouched). DA3's field
notice shipped in the CHANGELOG v0.14.0 entry — **DA3 RETIRED**. B10-7's label bootstrap ran
pre-tag (all 14 field-contract labels live on the tracker). Every second-half clerk disposition +
DA1..DA11 was owner-ruled before the tag — see the Owner review record above.

**Next: live acceptance — an owner action.** Run `vlt-upgrade` on vlt-core to v0.14.0. That run
discharges the arc's field-contingent ledger tail: **B10-6(5)** (the first persisted
`_agent/upgrade-reports/*.yaml` — now the acceptance instrument of record, replacing the retired
A1 hand-save), **B10-2(5)** re-discharge (an executing full-mode sweep that degrades loudly if at
all), **B10-1(5)** re-check (`manifest_write_divergence:` present), **B10-11**'s relocation offer
(accept or decline — both are legal and both are evidence), plus the standing 0.13.0 tails
(B10-3(3) run 2, B10-4(4), B10-5(5)/(6)). Then `acceptance-discharge` over that evidence, then
`arc-closeout` — which must also clear **B10-1..B10-5's first-half review markers**, the one
review debt this session deliberately left open.

**Acceptance-discharge run 2026-08-23 (over the vlt-core 0.14.0 upgrade + first full
lint).** Evidence of record: the persisted `2026-08-23-1217-upgrade.yaml` +
`2026-08-23-1504-lint.yaml` — the B10-6 instrument's first live use; no hand-carried
transcript. Outcome: **B10-1, B10-3, B10-6 discharged whole**; **B10-2(5)/B10-12(6)
FAILED narrowly** (sweep executes + degrades loudly — the repair is field-proven — but
the missing-target leg fails on 12/12 `crossLayerSlugs` false positives; seam sized:
`sources/` not a key ×8, `{index}` excluded ×3, non-`.md` linkable ×1; filing drafted,
routes into the next `inbox-capture`); the remaining tails are genuine first-exercise
waits, each with a named owner trigger (see the per-item annotations). Six source
filings archived to `inbox/archive/`. **Next:** the FAILED filing routes into the next
`inbox-capture` run (Arc 11 capture, or an owner-ruled in-arc escalation as with
B10-12); the open tails re-run through `acceptance-discharge` as their events occur —
the soonest are owner-seedable (a partner session discharges B10-5(5)+B10-11(5); an
`amended` label + capture discharges B10-7(3)). Arc closeout waits on the owner's
ruling over the FAILED item and the first-half review markers.

**Evening update 2026-08-23.** The owner-seedable events ran the same day: two vlt-core
`vlt-mint` convention-edit acts (session vlt-core-d4 — the frontmatter-overlay §D amend
`10d935e` and the first contract overlay `92a0e5d`, both same-act rung + decision-log,
factory-verified read-only) plus a routine football-analyst partner session
(16:15–17:09, no activation error). Result: **B10-5 and B10-11 discharged whole and
ticked**; **B10-9(3) birth-side discharged** (open: the next lint's no-orphan pass +
the v0.15.x survival half; named risk — the contract's overlay read path is unverified
at point-of-use, a factory-side read-path probe is the recommended instrument). The
vault filed **issue #8** (the instrument rule proposed for the shipped contract's
*Honest reporting* section) — routes through the next `issue-triage`/`inbox-capture`.
Carry-back also surfaced two filing-shaped module signals, FILED on owner confirmation
2026-08-23: `inbox/2026-08-23-180100-rule-shelved-as-trailing-clause-is-unreachable-by-subject.md`
(a rule recorded as a trailing clause under an unrelated `ref:` is invisible to every
ref-keyed read) and
`inbox/2026-08-23-180200-migrations-amend-the-base-but-walk-no-vault-local-overlay.md`
(the 0.14.0 base-contract migration walked no vault-local overlay; a human caught the
resulting stale rule). Both await Arc 11 capture. Ledger now: 5 of 12 items ticked; open = B10-2(5)/B10-12(6)
FAILED (build-gated), B10-4(4), B10-7(3)/(4), B10-8(4)/(5), B10-9(3) halves, B10-10(4).

---

**Superseded — the pre-release text:**

**Release v0.14.0** (`vlt-release`, owner-triggered) — the arc's **second** cut. All seven
builds of the cut are BUILT and committed on `arc10-v0.14.0`: B10-6 (`8879869`), B10-7
(`f958d66`), B10-8 (`aba700c`), B10-9 (`7d8ba9c`), B10-10 (`b7193e8`), B10-11 (`7a4b1a8`),
B10-12 (`b6dd3f6`). The cut's shape is the D1 RULED option (C) — B10-6..B10-12 as one cut
(owner, in-session 2026-08-22), widened from B10-6..B10-11 when the second capture addendum
escalated B10-12 as **release-blocking**; that blocker is now built, so nothing gates the
cut. Working tree clean at `b6dd3f6`. Each brief carries its own at-rest verification and
`package-lint` PASS line; B10-12's run also re-greens the harness at 23/23 (`CASE_FLOOR`
22→23). Per the release contract, `uv run tools/package-lint.py --expect-version 0.14.0`
must exit 0 before the tag, and its PASS summary goes in the release commit message —
expect D to fail only on the missing CHANGELOG `## v0.14.0` entry until `vlt-release`
Stage 3 authors it (the same pre-release state the v0.13.0 dry-run showed).

**After release:** the vlt-core v0.14.0 upgrade + `acceptance-discharge` run against this
roadmap's deferred ledger — which carries the field-contingent tails from **both** cuts,
including the still-open B10-1(5) and B10-2(5) FAILs whose fixes (B10-6 and B10-12
respectively) ride this cut. Then Arc 11 capture over the held filings (A10-12/A10-13 and
the other Arc-11 holds recorded in the addenda above).

**Superseded — the v0.13.0 cut (recorded 2026-08-21, shipped @ `a3ec505`):** B10-1
(`3d25cc4`), B10-2 (`c337cfa`), B10-3 (`ca0e700`), B10-4 (`9a904b5` — direction 2 on the
shipped direction-3 floor; frontmatter @10), B10-5 (`7bcdb91` — the fleet rung; frontmatter
@11 across all nine legs). Release-readiness gate dry-run 2026-08-21 passed A/B/C/E with D
failing only on the pre-release CHANGELOG gap. The roundtable convened 2026-08-21 — record
above: 15 amendments applied in-session, R4 declared (interim carrier: the review record),
4 owner rulings with one dissent on record, no OPEN disputes. Two capture addenda have run
since under the mid-arc posture (platform P-4, now closed): 2026-08-22 (scope-internal, no
delta) and 2026-08-22 second exercise (moved a joint → `## Roundtable review — addendum`).

---

## Closeout record — 2026-08-23 (arc-closeout run)

**Gate PASSED:** tag `v0.14.0` (`55b739d`) on the remote; ledger 6 of 12 ticked on dated
evidence, every open clause `[field-contingent]`-tagged and dispositioned below. **The tick
count is not a measure of what the arc proved** — B10-2 and B10-12 proved their repairs in
the field (the executing, loudly-degrading full sweep) and hold `[ ]` honestly on one
failed criterion leg; B10-4's mechanism shipped whole and its field check is BLOCKED on a
priced bound, not broken.

### Carried forward past Arc 10 (the authoritative hand-off — Arc 11's capture re-lists from here)

1. **B10-2(5)/B10-12(6) — BOUND inherited debt to Arc 11 (GATES).** Carried from the
   2026-08-23 FAILED grade — STILL OPEN at arc close, carries forward past Arc 10. The
   re-discharge is **ship-verifiable-re-check-tagged so it gates Arc 11's closeout**
   (owner-ruled at A10-18; the A4-4(5)/B8-2(4) mechanism). Discharging event: an
   executing full sweep whose missing-target flags survive verification (or a measured
   zero) after the A10-18 build lands the predicate's three missing populations
   (`sources/`, `{index}`, non-`.md` linkables) at `full-scale.md:7`. Criteria as amended
   by DA9, recorded at the B10-2(5) ledger entry.
2. **B10-4(4) — BLOCKED (unreachable) carry, explicitly not a watch** (owner-ruled at
   A10-19). The named metric `pages_with_review_after` is inexpressible under the shipped
   `local_metrics:` kinds (`vlt-vitals.py:251`); unblocks when Arc 11 rules A10-19
   (content predicate / fourth kind / canonical entry). Parts 2 (vacuous-zero honesty)
   and 3 (seed-merge durability) ride the same carry. The 0.9.0 silent-supersession
   pattern (a vault-authored derive dropped with no divergence report) travels inside the
   190100 filing.
3. **Released standing watches** (recorded here rather than ticked — the checks were
   never exercised; released, owner batch ruling 2026-08-23): **B10-7(4)** first genuine
   non-accept triage verdict (never manufactured); **B10-8(4)** next capability birth
   carries `requires:` from first commit; **B10-8(5)** the work-machine vault's first
   0.14.0+ setup/upgrade (evidence: the hand-carried persisted file, B10-6 transport
   caveat); **B10-9(3) remainder** — the contract overlay's v0.15.x byte-intact survival
   + subsumption offer, with the partner point-of-use read-path probe as the recommended
   discharge instrument (the vault council's unresolved change 12).
4. **DECLINE+WATCH pair, unchanged:** confidentiality-as-container-attribute (Maya's
   dissent preserved, not converted to a bound debt) and propagation-debt.
5. **Arc 11 held captures** (owner-ruled, awaiting Arc 11 ideation): A10-10 (#4
   wiki-index rule-vs-example), A10-12+A10-13 (#6+#7 decision-log pair, one build),
   A10-15 C3 (voice-rule single-homing), **A10-18** (crossLayerSlugs — the carry-1
   build), **A10-19** (local_metrics expressiveness — the carry-2 unlock).
6. **Un-captured filings — Arc 11's capture seed batch** (on disk in `inbox/`, named at
   the addendum-#3 preamble): `2026-08-22-150000` (relay-leg over-count),
   `2026-08-23-110913` (@mggower personal-handle trigger — also B10-7 disp. 7's named
   residue), `2026-08-23-111410` (council lens-shortfall, DA11), `2026-08-23-180100`
   (mis-shelved trailing clause unreachable), `2026-08-23-180200` (migrations walk no
   vault-local overlay), `2026-08-23-190200` (undeclared PARA type invisible), plus the
   materialized `2026-08-23-210653` (#8, the instrument rule — both wrapper instances,
   incl. the scoping-query bite that questions the byte-exact-only trigger).
7. **Inherited registers, re-carried not re-decided** (authoritative in the Arc 9
   archive's Closeout record): C6-c, B5-3..B5-9, the pre-Arc-5 and Arc-7 registers, and
   Arc 9's item-6 standing watches.

### Filing dispositions this close (per-filing criterion, Arc-3-widened rule)

**Archived** (every own-clause discharged, residue owned elsewhere): `093000` (PARA
write-path — B10-10 + B10-11 discharged whole), `100500` (scanner instructions —
field-clean 2026-08-23), `144554` (Gap-B — the 88% false class collapsed; issue #3
closed), `150500` (amendment leg — field-proven). Previously archived at discharge:
`144352` (#2), `100000`, `124500`, `124800`, `150213` (#5), `164445`. **Held live:**
`101000` (its `.base` cause persists → A10-18), `130455` (folded missing-target content →
A10-18), `155515` (#1 — the BLOCKED carry), `181500` (C1/C2 → the B10-7(4) watch; C3 →
Arc 11), `150800` (→ the B10-8 watches), `150212`/`150214`/`150215` (Arc 11 holds),
`160500`/`190100` (A10-18/A10-19), and the six + one un-captured (item 6 above). Issues
**#2, #3, #5 closed** at this close; **#1, #4, #6, #7, #8 stay open**, mirroring their
live filings.

**This arc is archived — do not append.**
