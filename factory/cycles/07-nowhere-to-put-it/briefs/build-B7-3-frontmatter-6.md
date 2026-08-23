---
title: 'Build #B7-3 — frontmatter@6: the coordinated rules bump (four rule changes, one six-consumer walk; rules ship ahead of their mechanisms with stated interim postures)'
status: 'BUILT 2026-08-15 — all F-sites landed as briefed. F1a version 6 + last_updated 2026-08-15, consumers unchanged; F1b rule 4 rewritten traverse-vs-verify with carve-out tail + R1 posture (bare-path form holds until the overlay-contract build); F1c vault-writable declared-fields paragraph after the adoption-axis paragraph, prose-only, no new field/slot, + R1 posture (review upstream / only move is to file); F1d self-baselined threshold string (baseline verified: 9 conventions on disk at build time); F1e template tripwire line reworded, no doctrine clause; F1f :238 comment + :243 prose aligned to vlt-upgrade three-distinct-values read; F1g local-convention two-property rule in the Narrow-convention escape hatch section + R1 posture (baseline_missing correct in the window); F1h :218 recipient clause dropped + address rule with three guards + limit paragraph + R1 posture (ask rides the relay build). F2: spec.md:16 → 2026-10-15, wiki-consolidation.md:16 → 2026-12-15, value-only, no sibling bumps, one-line diffs each. F3: six-consumer walk — reconciliation outcome at every consumer was the expected "no edit needed here — ack bumped" (vlt-ingest backlog drain + bare-path wiki writes legal under F1h/F1b postures; vlt-extract/vlt-research wikilink hits are body-citation prose, not frontmatter lists; vlt-lint checks and vlt-mint ceremony prose untouched; vlt-dispatch relay gains nothing until B7-5); all six acks frontmatter@5 → frontmatter@6. Deviations: NONE. Verification: (1) uv run tools/package-lint.py --expect-version 0.9.1 → exit 0, "package-lint: A/B/C/E PASS, D PASS — vlt 0.9.1" (Group E bipartite at @6); (2) uv run tools/test-package-lint.py → 20/20 green, no fixture hard-pinned frontmatter@5 so no R2 fixture edit needed, no floor bump (per brief, deliberate); (3) all four rules + four R1 posture sentences present in the @6 base; (4) exactly three review_after values changed repo-wide (2026-11-15/2026-10-15/2026-12-15), no version: moved except frontmatter.md 5→6; (5) F1d count matches ls | wc -l = 9; (6) scrub clean — logical names ({backlog}, {conventions}) and placeholder forms only; grep for stray frontmatter@5 in shipped tree = zero (only gitignored reports mention it). No .decision-log.md on disk. Doctrine-or-fix question remains held for owner review at the v0.10.0 release per disposition 1.'
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-14-142624-stock-deferral-dates-expire-with-no-vault-side-review-form.md (A7-5: vault-writable review_after rule + interim posture + the count-since-N threshold fix + the date renewal)'
  - 'inbox/2026-08-14-154423-no-legal-home-for-a-vault-originated-new-convention.md (A7-8: baseline-exempt local-convention rule, two-property bar)'
  - 'inbox/2026-08-14-154424-wiki-sources-should-ship-as-wikilinks.md (A7-9: YAML rule 4 traverse-vs-verify split — the rule only, never the form)'
  - 'inbox/2026-08-14-181000-knowledge-gap-addressed-to-a-rail-with-no-recipient.md (A7-12: the address rule + three guards + limit paragraph — the rule only)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-15): the frontmatter-bump plan (ONE coordinated 5→6 bump, DEDICATED build, four filings incl. the A7-9 amendment); the A7-5 shape ruling (overlay-writable review_after) + its two negations + "B7-3 sets the dates"; the authorized-carry-forward generalization; count-since-N principle (pre-ideation 3) as amended by A4; post-ideation amendments A1/A6 (reopen = 6→7 bump + full walk), A2 (rule 4 split not declinable by B7-6), R1 (interim posture per rule, binds immediately on B7-3)'
risk: 'moderate — bumps frontmatter 5→6, triggering the full six-consumer walk and bipartite re-verification; no mechanism/behavior changes (rules only), so the blast surface is the handshake, not runtime'
---

# Build #B7-3 — frontmatter@6: the coordinated rules bump

The arc's only `frontmatter` bump. One 5→6 version bump of the base convention
(`skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md`) carrying **all four base
rule changes** from A7-5, A7-8, A7-9 and A7-12, one six-consumer re-ack, and the in-build
bipartite-consistency verification — per the ruled build-16 precedent (*one coordinated bump, one
consumer walk — NOT split*). This build ships **rules, not mechanisms**: the mechanisms land in
B7-4 (the seam: vault-writable diff honoring + local-convention reads), B7-5 (relay `ask` shape +
the contract-owned reflex), and B7-6 (the wikilink `sources:` form + normalization clause + the
overlay-merge contract for workflow assets), and each mechanism brief cites this build's shipped
rule text as its contract. A `declared`-stage rule is a real rule; because the mechanisms do not
yet exist, **every rule shipped here carries its R1 interim-posture sentence in the same file**
— what a vault may legally do in the window, and whether findings generated in the window are
correct — and this build's acceptance checks are about the **handshake**, not behavior.

Also in scope, because they sit inside the exact Enforcement-declaration block this bump forces
all six consumers to re-ack: the count-since-N fix to `frontmatter.md:17`'s own threshold
(conservative path — see D1), and two of the A4 sizing audit's new stale-prose sites
(`frontmatter.md:235` and `:238`/`:243` — see D2). And the three `review_after` date renewals,
which the A7-5 ruling assigns to this build ("B7-3 sets the dates when it sets everything else").

All rejected alternatives in the parent filings are settled — do not re-litigate. In particular:
sequential per-filing bumps (rejected for the build-16 precedent), a date-only patch release or
B7-1 rider (interim posture RULED: **let the finding stand**), suppressing the 2026-08-17
`deferral_expired` findings in any form (they are true statements about a real gap), and any
generic skill-overlay mechanism (the veto stands; not this build's surface anyway).

## The reopen seam (amendment A1/A6) — stated up front

This bump closes `frontmatter` for Arc 7 **with a named reopen condition**: a mechanism brief
(B7-4/B7-5/B7-6) that demonstrates it needs a base rule or field reopens this build — re-cut
before it ships, or, once shipped, a coordinated **6→7 bump with a full six-consumer walk and
bipartite verification** (A6: a mechanical, checkable state, never a "recorded event with a
stated reason"). **One candidate is already known:** the seam's generalization of the
authorized-carry exclusion as *"a declaration the base file carries about itself"* is a new
convention-frontmatter field B7-4 may need. This build therefore **leaves a clean seam rather
than pre-building it**: the vault-writable rule ships as prose naming `review_after:`
specifically (F1c), with **no** new declaration field, no field registry, and no schema slot
reserved — if B7-4's design proves the field, it arrives via the reopen path with its own walk.
Pre-building a guessed field here would ship an unconsumed schema on a guess, and a wrong guess
would burn the 6→7 reopen on a correction.

## Brief-time dispositions

1. **The count-since-N overturn clause: condition MET on its letter; conservative path taken;
   doctrine question held for owner review at release.** Pre-ideation ruling 3 was marked
   *"overturnable if the sweep shows `frontmatter@5` is the only instance — a class of one is a
   fix, not a doctrine,"* and amendment A4 ran the count before this brief precisely so the
   clause is executable. The count is on record (`skills/reports/arc7-A4-sizing-audit.md`):
   **class 1 is a class of one** — `frontmatter.md:17` is the only shipped metric whose baseline
   a vault cannot read. The owner was not available this session, so this brief takes the
   conservative path autonomously: **fix the one instance** (the threshold ships its own
   baseline — F1d) and **do not enshrine a general count-since-N doctrine sentence** in the @6
   schema template or prose. The audit's two counter-weights are recorded for the owner's
   deliberation, not acted on: every other shipped counter already practices the principle
   (persisted lint reports, log-header baselines, watermarks, the `adoption_first_instance`
   stamp), so the doctrine's cost would be one sentence; and the ruled principle text stays in
   the roadmap as a ruling either way. **The doctrine-or-fix question is explicitly held for
   owner review at the v0.10.0 release** — the builder must not resolve it.
2. **The audit's two new Enforcement-block stale sites land HERE; the rest stay in B7-8.** The
   task's grounding: B7-3 version-bumps the exact block that carries them, so leaving them stale
   would force six consumers to re-ack a block containing two statements current source
   contradicts — and fixing them post-bump would be a second edit to a just-acked block.
   **In scope:** `frontmatter.md:235` (schema template `deferral_threshold: <numeric tripwire>`
   contradicted by all three shipped thresholds, which are prose strings — F1e) and
   `frontmatter.md:238` + `:243` (the `null/absent` conflation contradicting
   `vlt-upgrade/SKILL.md:112`'s three-distinct-values read — F1f). **Out of scope, stay B7-8:**
   `spec.md:92`/`:14` (A7-6's build), `vlt-setup/SKILL.md:295` (audit N1 — a different file this
   build never touches), and the audit's borderline watch (`vlt-upgrade:112`'s `created:` proxy).
3. **A7-5's pinned provenance question — ANSWERED: the three dates were one uniform horizon, not
   per-convention.** Archive read performed (the pin): all three `review_after: 2026-08-17`
   dates were set in builds 15/16, both committed **2026-07-06** (`3795d86`, `1142fb4`);
   `build-15-spec-convention.md:45-46` says so outright — *"aligned with 091004's own first
   self-application date"* — and `build-16-frontmatter3-bell-attestation-freshness.md:125,:167`
   assigned the same date to `frontmatter.md` and `wiki-consolidation.md` in one stroke. The
   filing's guess is confirmed. Per the capture, the answer changes *which* date-setting
   candidate is right: the renewals in this build are **derived per-convention from each metric**
   (disposition 4), never a shared horizon again.
4. **The new dates (per-convention derivation, recorded so the builder edits without
   re-deciding):**
   - `frontmatter.md` → **`review_after: 2026-11-15`.** Its metric (drift findings + new
     conventions minted) accrues at lint cadence and mint cadence; with the threshold now
     self-baselined (F1d) the metric is fully evaluable for the first time, and a ~3-month
     window spans Arc 8's likely minting (R3's retrofit build touches the checks surface).
   - `spec.md` → **`review_after: 2026-10-15`** (value-only edit at `spec.md:16`; **no `spec`
     bump** — a deferral date renewal is the deferral's own review outcome, not a consumer-facing
     rule change). Earliest of the three: threshold is 1, adoption is live in the field
     (vlt-core's two specs), and B7-8 edits this file's prose the same arc — the next review
     should land after that fix has had field time.
   - `wiki-consolidation.md` → **`review_after: 2026-12-15`** (value-only edit at
     `wiki-consolidation.md:16`; no bump). Longest window: the metric has read 0 on every sweep;
     more sweeps is the only thing that makes the next review better-informed than this one, and
     if it is still 0 at review the deferral's shape gets re-derived rather than re-dated.
   These renewals **are** the upstream review A7-5 says a vault cannot perform — performed where
   the interim posture (F1c) says it lives: at the factory. Recorded per the honest-surface
   rule: `wiki-consolidation@1` is renewed on a clean-record metric and `frontmatter@5`'s was
   half-unevaluable until this build — the renewal fixes the evaluability, it does not claim the
   expired window was reviewed on evidence that didn't exist.
5. **Scope ruling — the two sibling date lines are in scope as value-only edits.** "Base edits
   only" scopes the *rule changes* to `frontmatter.md`; the A7-5 interim-posture ruling assigns
   all three dates to this build, no other build owns them, and leaving spec/wiki-consolidation
   expired after B7-3 ships would keep two true-but-fixed `deferral_expired` findings firing
   past the build that owned the fix. Neither sibling takes a version bump (disposition 4).
6. **A7-13's calibration input honored: the four rules were re-derived, not inherited.** The
   vlt-core preview of these edits was reviewed by a substituted council (A7-13's provenance
   gap), so this brief grounded each rule against the module's own shipped design rather than
   adopting vlt-core's text: rule 4's split against `checks.md:59`'s shared-source leg and rule
   1's own example; the address rule against the backlog schema at `frontmatter.md:215-219` and
   the two op-skill sites; the vault-writable rule against the `adoption_first_instance:`
   exclusion at `vlt-lint/references/checks.md:41`; the local-convention rule against the three
   landing-zone outcomes at `checks.md:41-42`. Where vlt-core's wording and the module's design
   disagree, the module's design wins and vlt-core reconciles at upgrade (acceptance check 5).
7. **The consumer walk's asset coverage is by-declaration until B7-6 — recorded, not fixed
   here.** `vlt-mint/SKILL.md:144` still holds that *"a consumer's ack covers its own workflow
   assets"*; A7-7 grounded that as the silent-drift shape, and the handshake-node ruling makes
   the three workflow assets first-class nodes **in B7-6**. This walk therefore re-acks
   `vlt-lint` while `vlt-lint-full.js` remains overlay-blind — which is correct and known: none
   of the four @6 rule changes alters anything the workflow assets currently execute (the form
   change and the merged-read contract are B7-6's), so the declaration-covered ack is truthful
   for this bump. The builder must not reach into the `.js` assets.

## F-sites

All sites re-grounded 2026-08-15 against working tree at `e930a40` (branch `arc7-v0.10.0`, clean
+ B7-1/B7-2 briefs). Every capture-cited line HOLDS; zero grounding corrections.

## F1 — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md` (the base, 5→6)

One file, six edit clusters. The builder makes them as one coherent edit; they are separated
here so each traces to its filing and ruling.

### F1a — version block

- **Current:** `:4` `last_updated: 2026-07-30`; `:11` `version: 5`; `:12`
  `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch]`.
- **Change:** `version: 6`; bump `last_updated:` to the build date. **`consumers:` is
  unchanged** — no consumer is added or removed by any of the four rules.
- **Why:** the coordinated-bump ruling; whichever build opens `frontmatter@6` inherits the full
  base-edit set, and this build is, by ruling, the only opener.

### F1b — YAML rule 4: the traverse-vs-verify split (A7-9; amendment A2)

- **Current:** `:36` — *"**Non-graph list fields use bare paths/basenames, not wikilinks.** A
  list that is an audit trail rather than a link graph (e.g. a session log's `artifacts:`)
  holds plain vault-relative paths. Do not wrap these in `[[...]]` — the audit trail is not a
  wikilink graph. (`sources:` likewise holds plain page references unless a specific schema
  says otherwise.)"*
- **Change:** rewrite rule 4 to draw the distinction the filing grounds — **traverse vs
  verify**. A list you *verify against* (an audit trail — a session log's `artifacts:`, a
  research note's `sources:`) holds bare vault-relative paths, never wikilinks. A list you
  *traverse* (a link graph — claims answerable to origins where following the link is the
  point) is wikilink-form territory; **a wiki page's `sources:` is a link graph** and is the
  first field so classed. Keep the carve-out tail ("unless a specific schema says otherwise")
  — it is the delegation slot A7-9's carve-out rule (B7-6's contract half) builds on. Then the
  **R1 interim posture, in the rule's own text**: the wikilink *form* for wiki `sources:`
  (quoting, path shape, reserved characters, and the normalization clause that protects
  `linkage_ripe`'s shared-source leg — `vlt-lint/references/checks.md:59`) ships with the
  overlay-contract build; **until it does, wiki pages stay on the bare-path form** — the split
  is declared, the schema at `:98` (`sources: []`) is unchanged, and converting early is the
  one illegal move in the window because it silently breaks the absorption test the form change
  is designed to protect.
- **Why:** A7-9's grounded distinction, ruled into B7-3 by the four-filing amendment. **Per
  amendment A2, stated for B7-6's brief: this split is B7-3's and B7-3's alone to revisit (via
  A1's reopen). B7-6's decline latitude covers the `sources:` form and A7-10's template only —
  it may not decline, narrow, or contradict this rule; if B7-6 declines the form, it must state
  what the split means with no form behind it (that statement is R1's posture for the pair,
  B7-6's job).** The builder copies that sentence's substance into the brief-visible record if
  B7-6's briefer asks; here it needs only the rule + posture above.
- **Out of scope at this site:** the form details (double-quoting, drop-`.md`,
  full-path-not-basename, the reserved-character note), the normalization clause itself, the
  contract's carve-out rule, and `vlt-ingest`'s template placeholder (A7-10) — all B7-6.

### F1c — the vault-writable `review_after` rule + interim posture (A7-5; R1; A1 seam)

- **Current:** the Enforcement-declaration section `:224-243`; the deferral keys at `:233-236`
  with `review_after:` referenced-not-redefined at `:236`; the sole authorized vault-local
  carry today is `adoption_first_instance:` (excluded from the divergence diff at
  `vlt-lint/references/checks.md:41`). Nothing in the base says a vault may ever legally record
  a deferral review.
- **Change:** add a short paragraph to the Enforcement-declaration section (after the adoption-
  axis paragraph at `:243`), stating the ruled rule in its **general form** (the A7-5 ruling:
  "the brief must state the general form, not a `review_after` special case"): *a base
  convention field may be **declared vault-writable** — an authorized vault-local carry on a
  shipped base, the class `adoption_first_instance:` already instantiates — and a declared
  field's local value is not base divergence. The deferral-expiry key `review_after:` on a
  shipped convention is the second member of that class: a vault records a performed review's
  outcome without forking the base.* Then the **R1 interim posture**, verbatim in intent, which
  is A7-5's fourth carried candidate shipped as posture rather than as an alternative: *until
  the mechanism that honors the declaration ships (the seam build's divergence-diff
  generalization), a shipped deferral's expiry is **reviewed upstream, and a vault's only legal
  move is to file** — an expired `review_after:` on a stock convention produces a
  `deferral_expired` finding that is **correct**, a base edit to clear it still flags
  `convention_base_divergence` (also correctly), and neither finding should be suppressed
  locally.* Per the A1 seam ruling above: **prose naming `review_after:` — no new declaration
  field, no reserved schema slot.** How the declaration becomes machine-readable is B7-4's
  design, reachable via the reopen if it needs base carriage.
- **Why:** the A7-5 shape ruling (overlay-writable `review_after` as authorized vault-local
  carry) + the ruled-by-consequence generalization (a second instance of a one-off is a
  category) + R1, which binds immediately on B7-3 and names exactly this sentence as A7-5's
  missing field-facing posture ("*let the finding stand* told the factory what to do and the
  field nothing"). Without it, every 0.9.1 vault meets a true finding whose only door is the
  base edit the module then has to reconcile — manufacturing the divergences this build exists
  to accept.
- **Out of scope at this site:** any edit to `vlt-lint/references/checks.md:41`'s exclusion
  (B7-4's mechanism); the who-reviews-and-on-what-cadence question (the ruling's second
  negation — untouched, the field data in the capture is carried for whoever does it).

### F1d — the self-baselined threshold (A7-5 + pre-ideation ruling 3 as amended by A4)

- **Current:** `:17` — `deferral_threshold: "2 drift findings, or the 3rd new convention"`.
  Both halves count from unshipped baselines: no window start for the drift-finding count, and
  the convention count "the 3rd" runs from is recorded nowhere a vault can read (the audit's
  sole class-1 instance).
- **Change:** replace with a self-baselined threshold string — the baseline shipped **in the
  threshold's own text**, no new schema field (disposition 1's conservative path):
  `deferral_threshold: "2 prose/behavior drift findings since 2026-08-15, or the 3rd convention minted beyond the 9 shipped at that baseline"`.
  The builder verifies the count at build time (`ls skills/vlt-setup/assets/governance/_meta/conventions/`
  → 9 files today: consult, decision-log, extraction, frontmatter, spec, wiki-consolidation,
  wiki-index, wiki-supersession, write-verification) and adjusts the number if the tree moved.
  Both halves are now evaluable from vault-readable state alone: drift findings since a stated
  date are derivable from the append-only persisted lint reports (`vlt-lint/SKILL.md:72`), and
  minted-beyond-baseline from counting `{conventions}/*.md` against the stated 9 (a sanctioned
  local convention counts — that is F1g's tripwire-visibility property doing its job).
- **Why:** the ruled principle applied to its own producing instance, on the conservative path:
  fix the one instance, no doctrine sentence (disposition 1). This also discharges A7-8's
  compounding note — the metric guarding the escape hatch was provably blind and half-
  unevaluable; the renewal in disposition 4 would otherwise re-date a threshold nobody could
  read.

### F1e — the schema template's `<numeric tripwire>` (audit N3; disposition 2)

- **Current:** `:235` — `deferral_threshold: <numeric tripwire>` in the Enforcement-declaration
  schema block. All three shipped instances are prose strings (`frontmatter.md:17`,
  `spec.md:15`, `wiki-consolidation.md:15`); the template asserts a form its own frontmatter,
  four lines up, does not honor.
- **Change:** `deferral_threshold: <the tripwire — a number, or a short prose threshold a vault
  can evaluate from its own state>`. **Deliberately no baseline-doctrine clause** — the
  template describes the shipped reality without enshrining the count-since-N doctrine the
  owner has not yet ruled on (disposition 1). If the owner later adopts the doctrine, the
  clause lands in that ruling's build, on a 6→7 via the reopen or in Arc 8.
- **Why:** stale shipped prose inside the exact block this bump re-acks; also the template
  form that let the class-1 instance ship unevaluable.

### F1f — the `null`/absent conflation (audit N2; disposition 2)

- **Current:** `:238` — `adoption_first_instance: <null | dated reference …>   # null/absent =
  declared-but-not-yet-adopted (an absence, not a violation)`; `:243` — *"null/absent while the
  class is declared-but-unexercised"*. Both equate the two states. Current source contradicts
  it: `vlt-upgrade/SKILL.md:112` reads the same key with **three distinct values** — explicit
  `null` = "declared, no first instance yet"; total absence = "**axis not declared**" — *"which
  is why the three values are distinct."*
- **Change:** align the declaring convention with the reader it already has. `:238` comment →
  `# null = declared-but-not-yet-adopted; key absent = axis not declared (both absences, not
  violations)`. `:243` → *"…and **explicit `null`** while the class is declared-but-unexercised
  (a wholly absent key means the axis is not declared — `vlt-upgrade`'s adoption report
  distinguishes the three values)."* Prose alignment with shipped behavior — no semantic
  change to any consumer.
- **Why:** two shipped statements assign different semantics to key-absence; the declaring
  convention is the stale side, and it sits inside the block being re-acked.

### F1g — the local-convention rule (A7-8; R1)

- **Current:** no legal home exists for a vault-originated new convention — the three landing
  zones ground as `baseline_missing` (`vlt-lint/references/checks.md:41`), `overlay_orphan`
  (`:42`), or **silence** (a novel heading in an unrelated overlay passes
  `overlay_not_append_only`, which fires only on verbatim-duplicate headings). The base's own
  SSoT claim (`:25`) and the escape hatch (`:245-247`) say nothing about vault-originated
  subjects.
- **Change:** add a short rule paragraph — natural home: with the *Narrow-convention escape
  hatch* section (`:245-247`), which is already this file's placement-of-conventions prose —
  declaring the class: *a vault may originate a **local convention** — a convention file with
  no stock counterpart, carrying its own enforcement declaration. Two properties are
  mandatory:* **(a)** *it exists without a stock counterpart (it is not an overlay and shadows
  no shipped base), and* **(b)** *it is visible to the split tripwire as a convention in its own
  right — it counts toward this file's `deferral_metric` ("new conventions minted") exactly as
  a module-shipped mint would.* The two-property bar is the ruled floor (*"a landing zone that
  is merely silent would reproduce today's outcome with better manners"*). Then the **R1
  interim posture**: *until the seam build ships the mechanism (the `baseline_missing`
  exemption and the consumer read), a vault-originated convention file in `{conventions}` still
  flags `baseline_missing` — the finding is correct in the window; the legal move is to carry
  the file and file the finding upstream, not to suppress the check or disguise the rule inside
  an unrelated overlay (the silent third zone this rule exists to close).*
- **Why:** A7-8's ruled shape (B7-3 rules the declaration form, B7-4 the mechanism; the
  two-property bar binds both) + R1.
- **Out of scope at this site:** the `checks.md` exemption, the known-location decision, how
  consumers read local conventions (all B7-4); any prose-drift check (none exists; not this
  arc's scope).

### F1h — the address rule (A7-12; R1)

- **Current:** `:215-219` — the backlog `kind` list; `:218` — *"`knowledge-gap` — a topic the
  vault is thin on; a cue for the Researcher"* (a sentence naming a recipient on a rail whose
  schema at `:208` carries `kind` and `by:` only — no recipient field, no drain, no pickup
  loop). `:222` — the filing/promotion sentence closing the section.
- **Change:** two edits in the Backlog section. (1) `:218` drops the recipient clause —
  `knowledge-gap` becomes *"a topic the vault is thin on"* (the cue-for-the-Researcher read
  moves to the address rule, where it is an *address*, not a schema comment). (2) After the
  facet definitions, add the **address rule with its three guards, as ruled** (carried as filed
  in the capture; adopted here): *a noticed gap goes to `{backlog}` only when the filing
  partner does not know whose turn it is; when it does, the gap is **relayed to that partner**
  (`vlt-dispatch relay`, shape `ask`). The backlog is evolution intake, not a shared to-do
  list — it holds the unassignable.* Guards: **(1)** the rule binds every `kind`, not just
  `knowledge-gap` — it is a rule about address, not subject; **(2)** self-addressed work is not
  a relay — a partner does not relay to itself; **(3)** migration is one-home — an item that
  acquires an owner is relayed **and struck** from `## Open`, never left on both rails. Take
  the **limit paragraph with the rule, verbatim in intent** (the filing's condition): *relay
  does not schedule work — it buys an **address and a drain**, which the backlog has neither
  of, and not execution; a stale relayed slice is not evidence the rail failed.* Then the **R1
  interim posture**: *the `ask` shape and the relay-side machinery ship with the relay build;
  until then this rule is declared — the existing relay form carries what it can, filing to
  `{backlog}` remains legal for anything it cannot, and no check fires on either choice.*
- **Why:** A7-12's ruled rule (B7-5's brief owns the mechanism; the base rule rides this bump
  because it changes what the backlog section *means*) + R1. Guard 2's multi-user scoping
  caveat (amendment A8) is **B7-5's** to state against the addressee model at its ship time —
  this base text states the rule; B7-5 states the scope.
- **Out of scope at this site:** the `shape` facet and `ref` key, both key-definition sites,
  the contract's ownership of the reflex + four pointers, the Beat-2 `{backlog}` bound at
  `vault-operating-contract.md:169`, the partner-template edits, and every `vlt-dispatch` /
  `vlt-lint` / `vlt-ingest` edit — all B7-5.

## F2 — the deferral-date renewals (siblings; value-only, no bumps)

- **Current:** `frontmatter.md:18`, `spec.md:16`, `wiki-consolidation.md:16` — all
  `review_after: 2026-08-17` (one uniform horizon set 2026-07-06; disposition 3).
- **Change:** per disposition 4 — `frontmatter.md:18` → `2026-11-15` (rides the @6 edit);
  `spec.md:16` → `2026-10-15`; `wiki-consolidation.md:16` → `2026-12-15`. No other line in the
  two sibling files changes; neither sibling's `version:` moves (disposition 4's rationale).
- **Why:** the A7-5 interim-posture ruling — *"B7-3 sets the dates when it sets everything
  else"* — with per-convention derivation per the answered provenance pin. The 2026-08-17 →
  ship-date window's `deferral_expired` findings **stand as true**; nothing in this build
  back-dates, suppresses, or apologizes for them.

## F3 — the six-consumer walk (the re-ack)

- **Current, verified this session (bipartite-consistent at @5):** `consumers:` lists exactly
  six; exactly six acks exist, all `frontmatter@5`, no strays —
  `skills/vlt-ingest/SKILL.md:4`, `skills/vlt-extract/SKILL.md:4`,
  `skills/vlt-research/SKILL.md:3`, `skills/vlt-lint/SKILL.md:4`,
  `skills/vlt-mint/SKILL.md:3`, `skills/vlt-dispatch/SKILL.md:3`.
- **Change:** per the base-edit ceremony (`vlt-mint/SKILL.md:140-145`), walk every listed
  consumer, reconcile its text against the four rule changes, and bump each ack
  `frontmatter@5` → `frontmatter@6`. **Expected reconciliation outcome at every consumer: "no
  edit needed here — ack bumped"** — the four changes are declared rules whose mechanisms are
  deliberately deferred, and no consumer's current text encodes the old rules in a way the new
  rules contradict: `vlt-ingest`'s wiki writes stay on the bare-path `sources:` form (F1b's
  posture says so); `vlt-lint`'s checks are untouched until B7-4/B7-6; `vlt-dispatch`'s relay
  gains nothing until B7-5; `vlt-extract`/`vlt-research` consume schemas this bump does not
  alter; `vlt-mint`'s ceremony prose is version-agnostic. A reconciliation that concludes an
  edit *is* needed has found something this brief missed — record it as a deviation in
  `status:`, and if it is a rule-level finding, that is A1's reopen knocking, not a quiet fix.
- **Why:** the version-handshake rule (build-4; CLAUDE.md): a convention rule change bumps
  `version:` and re-acks every consumer **in the same build**, bipartite-consistent. Note
  disposition 7: this walk covers workflow assets by declaration, truthfully, until B7-6.

## Registration

**None** in the help/version surface — no new skill, no workflow, no `module-help.csv` row.
The registration this build *does* perform is the handshake itself: the `frontmatter` 5→6 bump
with the six-consumer re-ack (F3), verified bipartite-consistent by `package-lint` Group E.

## Out of scope (dispositioned)

- **Every mechanism** — the divergence-diff generalization + local-convention reads + dispatch
  designed-read (B7-4), the `ask`/`ref` relay machinery + contract reflex + Beat-2 bound
  (B7-5), the wikilink form + normalization clause + carve-out rule + template + workflow-asset
  handshake nodes and merged-read contract (B7-6). This build's rules are their contracts.
- **A vault-writable declaration field / registry** — deliberately not pre-built (the A1 clean
  seam, stated above); B7-4 reopens if its design proves the field.
- **The count-since-N doctrine sentence** — held for owner review at release (disposition 1).
- **`spec.md:92`/`:14`, `vlt-setup/SKILL.md:295`, and the `created:`-proxy watch** — B7-8's
  sweep (disposition 2).
- **`vlt-mint/SKILL.md:144`'s ack-covers-assets sentence** — stale by A7-7's grounding, but its
  correction is the handshake-node mechanism's (B7-6); rewriting the prose here without the
  mechanism would be a rule ahead of a mechanism with no posture, in the one build that can't
  spare a second bump.
- **Who reviews a module-owned deferral, and on what cadence** — the A7-5 ruling's second
  negation; the capture's field data rides in the roadmap for whoever does it.
- **The 2026-08-17→ship window findings** — stand as true; no suppression, no patch release
  (ruled interim posture).
- **vlt-core's standing base divergence** — correct until this build ships; nobody "fixes" it
  early (the evidence-debt disposition says so out loud). It resolves at vlt-core's 0.10.0
  upgrade (acceptance check 5).

## Verification (unit, at rest)

1. **Handshake bipartite re-check — `package-lint` Group E is the check of record** (E1
   handshake-bipartite, E2 structure-map, E3 stray-pin): `uv run tools/package-lint.py` groups
   A/B/C/E all PASS on the working tree, with `frontmatter` at 6, six consumers listed, six
   acks at `frontmatter@6`, zero `frontmatter@5` stragglers. A hand grep may aid the editing;
   it is never the recorded verification.
2. **Harness regression:** `uv run tools/test-package-lint.py` — all cases green at the
   current floor (20/20, `CASE_FLOOR` 20, post-B7-2). **R2 check: this build adds or changes no
   release-gate check**, so no new fixture case and no floor bump — stated here so its absence
   at review reads as deliberate, not skipped. If the builder finds the harness fixture
   hard-pins a `frontmatter` version that the bump breaks, that is an R2-relevant fixture
   defect: fix the fixture in-build and record the deviation.
3. **Rules-present greps (editing aid + builder self-check):** the four rules and their four
   interim-posture sentences all present in the @6 base — one posture per rule shipped ahead of
   its mechanism (R1's letter): F1b (form rides B7-6), F1c (review upstream / only move is to
   file), F1g (`baseline_missing` correct in the window), F1h (`ask` rides B7-5).
4. **Dates:** exactly three `review_after:` values changed repo-wide, to the disposition-4
   values; `spec.md` and `wiki-consolidation.md` diffs are one line each; no `version:` moved
   except `frontmatter.md`'s.
5. **Threshold evaluability spot-check:** the F1d string's convention count matches
   `ls skills/vlt-setup/assets/governance/_meta/conventions/ | wc -l` at build time.
6. **Scrub:** no personal or vault-local content in any changed shipped file; the new rule
   prose uses logical names (`{backlog}`, `{conventions}`) and placeholder forms only.

No Release section — B7-3 is not the arc's release build; the dual version bump and
`--expect-version` gate ride the arc's final build per `vlt-release`.

**Builder exit obligations:** rewrite this `status:` to a BUILT record with numbered
deviations; delete any `.decision-log.md` from the working tree; one commit for the build.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** `frontmatter@6` handshake closed and bipartite-consistent — Group E
   passes at rest and again inside the arc's pre-tag `--expect-version` gate run: six
   consumers listed, six acks at @6, zero stray @5 pins anywhere in `skills/`.
2. **[ship-verifiable]** rules-with-postures shipped — the @6 base carries all four rule
   changes (rule 4 split; vault-writable `review_after`; local-convention two-property rule;
   address rule + guards + limit paragraph) **and** one R1 interim-posture sentence per rule;
   verifiable at rest by reading the shipped base, re-confirmed on the next ordinary upgrade
   delivering the pristine base.
3. **[ship-verifiable — next ordinary upgrade, either vault]** the deferral clock reset holds:
   post-upgrade lint reports **zero** `deferral_expired` across
   `frontmatter@6`/`spec@2`/`wiki-consolidation@1` (dates 2026-11-15 / 2026-10-15 /
   2026-12-15), and the pre-upgrade window's `deferral_expired` findings were never suppressed
   (the vault's lint-report trail still shows them — they were true).
4. **[ship-verifiable]** the class-1 fix — `frontmatter.md:17`'s threshold is self-baselined
   and evaluable from vault-readable state alone (persisted lint reports + a countable
   `{conventions}` tree vs the stated baseline of 9); dischargeable at rest. The overturn
   record rides this check: condition met, conservative path taken, **doctrine question
   presented to the owner at the v0.10.0 release** (that presentation is part of this check's
   discharge).
5. **[field-contingent]** vlt-core's standing `frontmatter` base divergence resolves at its
   0.10.0 upgrade: the divergence clears where B7-3 adopted the previewed edits and re-flags
   correctly wherever the module's ruled text differs from vlt-core's local wording (the
   re-derived-not-inherited disposition predicts some diff survives). Producing vault:
   **vlt-core only** (owner-run; the factory cannot read it — evidence arrives as the owner's
   pasted upgrade report / lint findings + ledger entry). If unread by closeout it goes to the
   watch register, not the gate.
