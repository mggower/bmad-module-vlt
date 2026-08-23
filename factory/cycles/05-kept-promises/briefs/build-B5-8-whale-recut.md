---
title: 'Build #B5-8 — the whale re-cut (the two skill whales still charge every invocation for content most invocations never use; the boot whale is already dieted)'
status: 'BUILT 2026-07-30 — implemented directly per this brief (F1–F5 landed; registration none, as briefed). Deliverables: dispatch router SKILL.md 11,281 B (≤ 14,000) + NEW references/daily.md 11,007 / relay.md 7,031 / consult.md 9,126 / ledger.md 1,811 (per-skill total 40,256 ≤ 40,785, the 105% bound on 38,843); lint router SKILL.md 6,261 B (≤ 12,000) + NEW references/full-scale.md 3,611 / checks.md 25,023 / fix-and-file.md 6,243 / report.md 10,306 (total 51,444 ≤ 51,476, the 105% bound on 49,025); package-lint gains C7 (router integrity both directions + ROUTER_BUDGETS beside RULE_CARD_BUDGET, homed in Group C per the granted choice so the A/B/C/E summary format holds) and E3 widened to skills/vlt-*/references/*.md; the ack-coverage clause widened to reference files (landed in references/checks.md, riding the F2 move); cost-manifest whale aggregates dir-aware with (router) rows beside each, skill-surface note added, harness truth table follows. Verified at rest per this brief: package-lint A/B/C/E PASS on the tree AND three temp-copy negatives each FAIL correctly (deleted reference -> dangling route; planted frontmatter@4 pin in a reference -> widened E3; stray unrouted reference -> orphan); test-cost-manifest 7/7 green; both routers frontmatter blocks byte-identical to pre-cut and zero convention files touched by this build — the no-bump is machine-confirmed (Group E PASS); the Step-5 fence strict-YAML-parses whole at its new home; single-home greps clean both directions; inbound-pointer walk (all ten sites) resolves through surviving mode/step names with ZERO inbound edits; vlt-upgrade:48-49 verified-not-edited (the wholesale copy carries references/, the exclusion list does not catch the name, skill_asset_divergence accommodates new shipped files); dry-walks complete (consult mode router+reference only; scoped lint; the nothing-in-scope exit reads the router alone); scrub clean; no .decision-log.md on disk. No deviations. No commit — release choreography rides the arc level.'
module_code: 'vlt'
created: '2026-07-30'
derives_from:
  - 'inbox/2026-07-29-082934-whale-files-carry-restated-weight.md (A5-14 — the three whales; dispositions (a)/(b)/(c)/(d))'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): grouping row B5-8 (A5-14 alone, apart from B5-7 — disposition (a) is the structurally largest change and carries the pinned `package-lint.py` pre-brief check; same gate as B5-7); pre-ideation ruling 2 (measure first — gate OPEN 2026-07-30, both artifacts landed); cross-filing ruling 1 (→ RULED 2026-07-30: POST-HOC DEFAULT — pre-hoc carries only identity-bearing or act-blocking content; mechanisms are this brief''s); §Spike obligations (the `package-lint.py` packaging-expectations check pins to THIS brief, performed before any re-cut was scoped — §The pinned pre-brief check below).'
risk: 'moderate — no convention version bump anywhere (no re-ack, Group E must confirm that by machine), but it restructures the module''s two heaviest op skills into router + reference files, which creates exactly the new cross-file agreement the capture warned about; the brief answers that with a deterministic router-integrity check and an E3 coverage widening in the same build. Behavior is preserved throughout: the re-cut moves text, it changes no check, no mode semantics, no report key.'
---

# Build #B5-8 — the whale re-cut

A5-14 named three whale files loaded whole whenever their surface is touched. One of the
three is already handled: B5-7's rule-card took the operating contract off the eager boot
path — the contract is a lazy point-of-use read, section-routed by the card's map, exactly
the filing's disposition (c) ("if a compiled digest ships … its editorial urgency drops to
(b)-level"). What remains are the **two skill whales**, and at this brief's working tree
they are heavier than at capture:

- `skills/vlt-lint/SKILL.md` — **49,025 bytes** (was 41,202 at capture; B5-2/B5-3/B5-4/B5-6
  each added checks), ~9.5–12.3K est. tokens, loaded whole at every lint activation.
- `skills/vlt-dispatch/SKILL.md` — **38,843 bytes** (was 38,285; B5-4/B5-7 consult
  additions), ~7.8–9.7K est. tokens, loaded whole even when the call is one `consult` or a
  `ledger` glance — four modes' mechanics in one file.

The claim is unchanged from capture: this is a weight problem, not a drift problem —
single-home discipline is holding. At this size *structure* is the lever, and the
surrounding skill ecosystem's canonical answer for large skills is a thin SKILL.md router
with depth in on-demand reference files. This build applies it, with cut lines chosen
against the B5-1 numbers (measure-first, satisfied — disposition 3 below) and the router
criterion supplied by the POST-HOC-DEFAULT ruling (cited, never re-litigated): what stays
eagerly loaded is what is identity/routing-bearing or **act-blocking**; mechanics are read
at the moment that uses them.

## The pinned pre-brief check — `package-lint.py`'s packaging expectations

Roadmap §Spike obligations pins this read to this brief, **before any progressive re-cut
is scoped**. Performed 2026-07-30 against the working tree's `tools/package-lint.py`
(post-B5-7, C6 included). Findings, each with a consequence for the scoping below:

1. **Reference files ship automatically — no packaging registration exists or is needed.**
   Group C5 maps `marketplace.json skills[]` one-to-one onto `skills/vlt-*` **directories**
   (`package-lint.py:205-212`), never onto files; the plugin install and `vlt-upgrade`'s
   own-the-apply both move whole skill dirs (`vlt-upgrade/SKILL.md:48` — "refresh the
   shipped `vlt-*` skills"). New `.md` files inside an existing skill dir ride for free.
2. **Group A is neutral** — the cruft scan rglobs the shipped surface for the cruft
   name/suffix sets only (`package-lint.py:59-61,74-87`); plain `.md` reference files are
   invisible to it.
3. **One naming constraint:** `vlt-upgrade`'s copy excludes `reports/` (and
   `.decision-log.md`, `__pycache__/`, `*.pyc`, `.DS_Store`) from everything copied
   (`vlt-upgrade/SKILL.md:49`). A reference directory must not collide with that list —
   ruled `references/` (disposition 7).
4. **The real gap — E3's scan scope.** The stray-pin check globs
   `skills/vlt-*/SKILL.md` **only** (`package-lint.py:383`). Mechanics moved into
   reference files exit E3's coverage: a `name@version` pin token recited in a reference
   file — the strongest machine-detectable de-facto-consumption tell — would go unseen.
   The re-cut must widen E3 in the same build (F3), or it ships a blind spot it created.
5. **E1 reads acks from SKILL.md frontmatter only** (`package-lint.py:419-425`) —
   `depends_on:` therefore **stays in the router's frontmatter**, never moves to a
   reference file. The vault-side twin (`vlt-lint`'s convention-coherence check) reads the
   same surface; its "a consumer's ack covers its own workflow assets" clause
   (`vlt-lint/SKILL.md:82`) extends to reference files (F4) so the ack's coverage stays
   stated, not assumed.
6. **No existing check verifies router↔reference agreement** — the "new cross-file
   agreement to keep lintable" the capture named has no net. This build adds the
   deterministic check (F3, the C6/B5-7 precedent: the artifact class's characteristic
   drift gets a machine check the day the class ships).

## Re-grounding (2026-07-30, HEAD `2f19251` + B5-4..B5-7 uncommitted working-tree edits)

Every capture site **HOLDS**; zero grounding corrections. The grounding baseline is the
working tree (B5-2/B5-3/B5-4/B5-6 grew `vlt-lint`; B5-4/B5-7 grew `vlt-dispatch` and the
contract; B5-7 landed the rule-card + cost-manifest recomposition).

- Sizes at this tree: lint SKILL 49,025 / dispatch SKILL 38,843 / contract 39,688 /
  `frontmatter.md` 23,233. The two skill whales **strengthened** since capture; the
  contract's whale status is now a *lazy* fact (B5-7).
- Lint's convention span: `depends_on` now carries **8 acks of 9 conventions**
  (`vlt-lint/SKILL.md:4` — decision-log@1 added by B5-6; all but `wiki-consolidation.md`,
  which lint reads as the shared consolidation discipline, not an ack). Conventions total
  is now 84,032 bytes across 9 files. The capture's "7 of 8" aged in the whale's
  direction. HOLDS in substance.
- Dispatch's four modes in one file: `daily` `:69-147` (9,949 bytes), `relay` `:148-202`
  (6,108), `consult` `:203-298` (7,561), `ledger` `:299-316` (1,401) — mode bodies total
  **25,019 of 38,843**; shared core (frontmatter/Overview/On Activation/Mode
  dispatch/pickup loop/Log) ≈ 11,664; per-mode Verify `:342-370` (2,150). A `consult`
  caller carries `daily`'s watermark prose and vice versa — exactly as filed. HOLDS.
- Lint's step anatomy (this brief's own measurement, the (d) numbers applied): Step 0
  scope `:19-38` (1,059) + the **full-at-scale fan-out protocol `:39-46` (3,444 — full
  mode >~30 pages only)**; Step 2 catalog `:51-112` (**24,807** — tier 1 3,560, tier-2
  content 5,881, governance checks 11,928, research candidacy 3,438); Step 3 `:113-128`
  (2,960); Step 4 `:129-164` (3,479); Step 5 `:165-234` (**9,258**, the report fence +
  reporting paragraphs); Tips `:245-251` (875). HOLDS.
- Single-home is holding, as filed: lint JIT-reads conventions before fixes (`:17`);
  dispatch delegates the consult protocol to the engine (`:227-242`), the trigger rule to
  the contract (`:211`), the class to `consult.md` (`:207`).
- **Inbound pointers into the whales are mode/section-named, never line-numbered** — they
  survive a re-cut that keeps the mode/step names routable: contract `:169` (dispatch's
  pickup loop), `:230` (dispatch's `consult` mode), `:236` (relay mode's mechanics home);
  `consult.md:33` ("mechanics at `vlt-dispatch`, *Mode: consult*"), `:49` (the block
  shape's single home); `spec.md:70` (relay-when-done reflex); `vlt-mint:162` +
  `frontmatter.md:242` (dispatch's consult record); `vlt-lint:93` (dispatch's block
  shape); `wiki-consolidation.md:26` (lint detects / ingest executes). F1/F2 carry the
  survival obligation; Verification 6 walks the list.
- **Grounding additions (in scope beyond the filing's letter):**
  1. `tools/cost-manifest.py:331-343` — the named aggregates track "lint SKILL" /
     "dispatch SKILL" as **SKILL.md-only** rows; after the re-cut those rows would report
     the router alone and the whale would silently exit the tracking that produced this
     build. The instrument follows the declaration (F5, the B5-7 F7 precedent).
  2. `package-lint.py:383` E3 SKILL.md-only scan — finding 4 above (F3).
  3. `vlt-upgrade:48-49` — the wholesale dir copy carries reference files (verify, don't
     edit — the B5-7 registration precedent) and its `reports/` exclusion constrains the
     dir name (disposition 7).
  4. `vlt-lint:82`'s ack-coverage clause — finding 5 above (F4).

## Brief-time dispositions

1. **A5-14 (c) — DISCHARGED by B5-7, no work here.** The contract's inline weight stopped
   taxing activations when the rule-card became the ceremony read; the filing's own clause
   prices its remaining editorial urgency at (b)-level. This build does **not** restructure
   or editorially re-cut the contract: any byte change would force a rule-card re-derivation
   (C6's sha), the card's 19-row section map already *is* the contract's progressive
   disclosure, and B5-9 (the enforcement kit) is about to touch the same governance surface.
   Out of scope, dispositioned.
2. **A5-14 (d) — SATISFIED.** The measure-first sequence completed before this brief
   opened: vlt-core baseline (`skills/reports/cost-baseline-2026-07-29.md`) + the
   work-vault run (`inbox/2026-07-30-111133-b5-1-work-vault-cost-manifest-run.md`). Cut
   lines below are chosen from measured section sizes (the Re-grounding's byte figures are
   this brief's own `wc -c`-grade measurement of the sections), not guessed.
3. **A5-14 (a) — ADOPTED for both skill whales**, the roadmap row's named shape, with the
   router criterion derived from the POST-HOC-DEFAULT ruling (cited, not re-litigated):
   the router keeps what is **identity/routing-bearing** (what the skill is, which mode/step
   applies, how to route) or **act-blocking** (rules whose violation a later read cannot
   cheaply undo — the human-zone boundary, single-writer, never-auto-fix, never-spawn/depth-1,
   secret hygiene); **mechanics, templates, worked examples, and reporting pedagogy** move
   to reference files read at the moment that uses them. This is the same criterion the
   rule-card applied to the contract, one layer down — the arc's one distillation rule,
   applied twice.
4. **The dispatch cut is per-mode; the savings are real per invocation.** Mode bodies are
   genuinely disjoint (25,019 of 38,843 bytes). Measured expectation: a `consult`
   invocation drops from 38,843 to ≈ router + consult reference ≈ 20–22K (~45% cut); a
   `ledger` glance to ≈ 13–15K (~60% cut); `daily` (the heaviest mode) to ≈ 22–24K.
5. **The lint cut is per-step, and the brief states its honest bound:** a full lint run
   walks every step, so its *total* load is roughly conserved — the savings concentrate in
   (i) every **scoped** run, which never reads the 3,444-byte fan-out protocol; (ii) runs
   that stop early (no `vlt` setup, nothing in scope since the last lint — a real and
   common exit at `:29`), which now pay the router alone (~7–12K vs 49K); (iii) runs that
   file nothing (Step 4's shapes unread); and (iv) the activation itself — the trigger
   surface every summoning pays before any step runs. No claim beyond that is made: this
   is deferral-shaped for the full path, avoidance-shaped for the scoped/early paths, and
   the report says which is which.
6. **A5-14 (b) — composable, executed inside the move, not as a separate pass.** The
   builder hunts restated mechanics *while relocating* (the single-home greps in
   Verification are the check); no standalone editorial pass runs on the contract or on
   `frontmatter.md` (dispositions 1 and 10).
7. **The reference directory is `skills/<skill>/references/`, module-owned, shipped.**
   Not `reports/` (the upgrade copy excludes that name, pre-brief finding 3); not
   `assets/` (that name is established for *installable* payloads — `vlt-setup/assets/`,
   `vlt-mint/assets/` — not for the skill's own on-demand depth). References are shipped
   skill files: refreshed wholesale on upgrade like the SKILL.md beside them, subject to
   `skill_asset_divergence` exactly as any shipped skill file is.
8. **Size budgets, from the numbers (build acceptance bounds, F3 checks the routers):**
   dispatch router SKILL.md ≤ **14,000 bytes** (measured shared core ≈ 11.7K); lint router
   SKILL.md ≤ **12,000 bytes** (measured residue ≈ 6–8K); per skill, **router + references
   total ≤ 105% of the pre-cut file** (splitting pays a small header tax; a re-cut that
   *grows* the surface re-creates the whale across more files — the C6 lesson).
9. **No convention bump anywhere; no handshake motion.** `depends_on:` stays in each
   router's frontmatter (pre-brief finding 5); moving a consumer's own text between its
   files is not a convention rule change; no convention file is edited except none. Group
   E must PASS with every `version:`/`consumers:`/ack byte-identical — the no-bump is
   machine-confirmed, not asserted.
10. **`frontmatter.md` (the conventions whale) — declined here, named as future-filing
    territory.** It is a *lazy* point-of-use surface (governance stock — the ruling's
    post-hoc side), so a split buys no eager-read savings; and re-cutting a `version: 4`
    convention with five consumers into multiple files is a structural change that would
    demand `frontmatter@5` + a five-consumer re-ack — not paid for by any measured number.
    If the field prices the conventions' point-of-use reads as a standing tax, that is a
    new filing with its own numbers. (B5-7's out-of-scope note sketched
    "lint/dispatch/frontmatter" for this build; that note was a pointer, not a ruling —
    the roadmap row binds this build to A5-14, and this disposition records the narrowing
    with its reason.)

## F1 — the dispatch re-cut (`skills/vlt-dispatch/SKILL.md` → router + NEW `skills/vlt-dispatch/references/`)

**Current state:** one 38,843-byte file — frontmatter+head `:1-8`, Overview `:9-25`, On
Activation `:26-49`, Mode dispatch `:50-68`, the four mode bodies `:69-316`, pickup loop
`:317-327`, Log `:328-341`, per-mode Verify `:342-370`.

**The change:** cut per mode along disposition 3's criterion.

- **The router (SKILL.md) keeps:** the frontmatter whole (`name`, `description`,
  `depends_on: ["consult@1", "spec@2"]` — E1/triggering read here, pre-brief finding 5);
  the Overview (identity — the one-machine/one-record framing and the four-mode digest);
  On Activation **including its act-blocking rules verbatim** (the human-zone boundary
  `:46`, secret hygiene `:48`, single-writer framing); Mode dispatch (`:50-68` — the
  routing beat, now also naming each mode's reference file as the read-on-entry); **the
  pickup loop `:317-327` in full** (it is the drain protocol's single home, pointed at by
  contract `:169`, and it is what *partners* — not dispatch invocations — read; small and
  truly shared); and a short Log preamble (the log is per-mode; each mode's line shape
  moves with its mode).
- **Four reference files, read on mode entry:** `references/daily.md` (`:69-147` + its
  Verify block + its log line), `references/relay.md` (`:148-202` + Verify + log line),
  `references/consult.md` (`:203-298` + Verify + log line — including the engine
  invocation block, the typed return union, the trail-and-bound, the adoption-stamp beat),
  `references/ledger.md` (`:299-316` + Verify — small (1.4K), moved anyway for mode
  uniformity so the router's rule is "every mode: read your reference on entry", never a
  list with exceptions). Each mode's reference restates **nothing** from the router; the
  router restates **no** mechanics from a reference (single-home both directions — the
  Verification greps).
- **Mode-name survival:** the router's Mode dispatch section keeps every mode's name and
  one-line what-it-is, so every inbound pointer in the Re-grounding's list ("`vlt-dispatch`'s
  `relay` mode", "*Mode: consult*", "the pickup loop", "the block shape") resolves through
  the router to the reference. **No inbound file is edited for this** — verify, don't
  assume (Verification 6); note in the BUILT record if one needed it.

**Why:** A5-14 (a) at the file where the modes are genuinely disjoint — the measured
25K/38.8K mode-body share is the saving (disposition 4).

## F2 — the lint re-cut (`skills/vlt-lint/SKILL.md` → router + NEW `skills/vlt-lint/references/`)

**Current state:** one 49,025-byte file — head `:1-18`, Step 0 `:19-46` (scope 1,059 +
fan-out 3,444), Step 1 `:47-50`, Step 2 `:51-112` (24,807), Step 3 `:113-128`, Step 4
`:129-164`, Step 5 `:165-234` (9,258), Step 6 `:235-244`, Tips `:245-251`.

**The change:** cut per step along the same criterion.

- **The router (SKILL.md) keeps:** the frontmatter whole (all 8 `depends_on` acks —
  byte-identical); Overview; On Activation `:13-18` **including** the JIT-read rule and
  overlay honoring (act-blocking: it governs every fix); Step 0's scope determination
  `:19-38` (every run starts here; the early "nothing in scope" exit stays router-only);
  Step 1; a **step sequence map** — one line per step naming what it does and which
  reference to read on reaching it; the **act-blocking postures stated once as rules**:
  never-auto-fix on every tier-2/governance finding, the never-auto-apply list (`:125`),
  single-writer safety lives in the SKILL not the finders (`:43`'s clause), lint never
  stamps adoption, write-through records a human's ruling only; and Step 6's log line
  (`:235-244`, small, every run ends here).
- **Four reference files, read at the step that uses them:**
  `references/full-scale.md` — the fan-out workflow protocol `:39-46` (read only when
  full mode exceeds ~30 pages; scoped runs never load it);
  `references/checks.md` — the Step 2 catalog `:51-112` whole (tier 1, tier 2, the
  governance checks with read-before-flag, research candidacy, gaps) — read at Step 2 in
  both modes; it is the rules' mechanics-depth, and keeping it one file matches its real
  read pattern (all of Step 2 runs whenever Step 2 runs);
  `references/fix-and-file.md` — Steps 3+4 `:113-164` (the auto-fix details, attestation
  beat, write-through entry mechanics, the backlog item shapes and guards);
  `references/report.md` — Step 5 `:165-234` (the report fence + the five reporting
  paragraphs) + Tips. **The Step-5 fence keeps its whole-fence strict-YAML property at its
  new home** (Verification 5) — the B5-3 repair must not regress in the move.
- The router's rule statements **point at, never restate**, the reference mechanics (e.g.
  the router says "tier-2 findings are never auto-fixed; the catalog and each check's
  mechanics: `references/checks.md`"). The builder may merge `full-scale.md` into Step 0's
  router text ONLY if the router stays ≤ 12,000 — the default is the four-file cut.

**Why:** A5-14 (a) at the file where the weight is step-serial — disposition 5 states the
honest saving shape; the biggest single win is the trigger/early-exit surface (49K → router)
and the scoped-mode fan-out skip.

## F3 — the packaging net follows the new artifact class (`tools/package-lint.py`)

**Current state:** E3 scans `skills/vlt-*/SKILL.md` only (`:383`); no check reads
router↔reference agreement; C6 is the only derived/companion-artifact check.

**The change, two parts (homed per the B5-7 C6 precedent — builder's choice of letter,
inside an existing group so the `A/B/C/E PASS` summary format holds):**

1. **Router-integrity check (C7-shaped):** for every `skills/vlt-*/references/*.md`, the
   owning skill's `SKILL.md` (or a sibling reference) names its basename; and for every
   `` `references/<name>.md` `` token in a `skills/vlt-*/SKILL.md` or reference file, the
   file exists. Both directions — a dangling route and an orphan reference each FAIL. Also
   enforce disposition 8's budgets here: `vlt-dispatch/SKILL.md` ≤ 14,000 bytes,
   `vlt-lint/SKILL.md` ≤ 12,000 bytes (constants beside `RULE_CARD_BUDGET`, same idiom).
2. **E3 widening:** the stray-pin scan covers `skills/vlt-*/SKILL.md` **and**
   `skills/vlt-*/references/*.md` (not a blanket `**/*.md` — `vlt-setup/assets/**` is
   installable payload with its own jurisdiction, `vlt-lint`'s vault-side checks; scoping
   the widening to the new class keeps E3's near-zero false-positive property). The
   `depends_on:`-line skip is unchanged (reference files carry no frontmatter acks — a pin
   token there is exactly the tell E3 exists to catch).

**Why:** pre-brief findings 4 and 6 — the re-cut creates a cross-file agreement and a
coverage hole in the same act; both get their deterministic net in the same build, or the
build ships drift-inviting structure with no bell.

## F4 — the ack-coverage clause widens (`vlt-lint/SKILL.md:82`, riding F2's move)

**Current state:** the convention-coherence check's prose says "A consumer's ack covers
its own workflow assets (e.g. `vlt-lint` acks for `vlt-lint-full.js`)."

**The change:** "…covers its own workflow assets **and reference files** (e.g. `vlt-lint`
acks for `vlt-lint-full.js` and its `references/`)." One clause, landing wherever F2 homes
the coherence check (`references/checks.md`). Prose clarification of lint's own check —
no convention is edited, nothing bumps.

**Why:** pre-brief finding 5 — the vault-side coherence check must state that reference
files ride the router's ack, or the coverage is assumed rather than declared.

## F5 — the instrument follows the re-cut (`tools/cost-manifest.py:321-343` + harness)

**Current state:** the "Skill surface" section is deliberately SKILL.md-only (the
capture's population correction — keep it and its label); the **named aggregates**
(`:331-343`) track `lint SKILL` and `dispatch SKILL` as `measure_file(<skill>/SKILL.md)`
— post-cut these rows would silently report the router alone.

**The change:** the two whale aggregate rows become **dir-aware**: `lint surface
(SKILL.md + references/)` and `dispatch surface (SKILL.md + references/)` — each the sum
over the router and its `references/*.md` — so the tracked whale line still measures the
whole surface the skill can read; add beside each a `(router)` row for the eager/trigger
share, since that split *is* this build's claim. The SKILL.md-only section keeps its
label and gains one sentence noting the two re-cut skills carry on-demand `references/`
measured in the aggregates. Re-run `tools/test-cost-manifest.py` and fix what the
recomposition breaks — the harness stays green.

**Why:** grounding addition 1 — the instrument measures the declared surface; this build
changes the declaration (the B5-7 F7 precedent, verbatim).

## Registration

**None.** No new skill (no `module-help.csv` row), no workflow, no convention `version:`
bump (disposition 9 — no consumer walk / re-ack), no structure-map change, no
marketplace change (C5 maps dirs; the dirs are unchanged). The reference files register
in **no list at all**: they ship because their skill dir ships — the plugin install and
`vlt-upgrade:48`'s wholesale `vlt-*` refresh both carry them (verify, don't assume, in
Verification 8; note in the BUILT record if an edit was needed). Their integrity net is
F3, their measurement home F5.

## Out of scope (dispositioned)

- **The operating contract** — discharged-by-B5-7 (disposition 1): no structural or
  editorial byte lands on it this build (C6 sha churn, card-map churn, B5-9 incoming).
- **`frontmatter.md` and the conventions bundle** — declined-because (disposition 10):
  lazy surface, five-consumer re-ack not paid for by any measured number; future filing
  territory.
- **The other SKILL whales** (`vlt-mint` 32.7K, `vlt-setup` 27K+, `vlt-upgrade` 27K+) —
  A5-14 names three files; the re-cut pattern + F3's net now exist as precedent any
  future filing can invoke per-skill with its own numbers (point-at-the-map, not a
  completeness sweep).
- **Behavior changes of any kind** — no check added/removed/re-scoped, no mode semantics
  touched, no report key changed, no change to *when* governance checks run. The re-cut
  moves text. (A scoped lint still runs every Step-2 check; only what it *reads to get
  there* changes.)
- **`vlt-lint-full.js` / `vlt-consult.js` internals** — untouched; the workflows are
  already the fan-out/engine halves of the progressive structure.
- **A generic router/reference convention file** — not created: two instances are a
  pattern, not yet a convention (the capability-family lesson — machinery shipped ahead
  of exercise sits unexercised); F3 is deterministic structure-enforcement without a
  prose convention to keep acked.

## Verification (unit, at rest)

1. **Budgets:** `vlt-dispatch/SKILL.md` ≤ 14,000 bytes; `vlt-lint/SKILL.md` ≤ 12,000;
   per skill, router + `references/*.md` total ≤ 105% of the pre-cut file (49,025 /
   38,843 — record the exact post-cut figures in the BUILT record).
2. **Router-integrity check exercised both ways:** `uv run tools/package-lint.py` →
   PASS; then in a temp copy delete one reference file and confirm FAIL; separately
   plant a `frontmatter@4` token in a temp reference file and confirm the widened E3
   FAILs; restore.
3. **Single-home greps, both directions:** each moved mechanic (the watermark rule, the
   relay idempotency pair, the engine invocation block, the typed return union, the
   Step-2 check bodies, the Step-4 item shapes, the Step-5 fence) appears in **exactly
   one** file across the skill dir; the routers restate none of them (surviving router
   mentions are rule-statements + pointers only).
4. **Group E unchanged, machine-confirmed:** package-lint Group E PASS with every
   convention `version:`/`consumers:` and every `depends_on:` ack byte-identical to
   pre-build (diff the frontmatter blocks) — the no-bump ruling is confirmed, not
   asserted.
5. **The Step-5 fence still parses whole** as strict YAML (`yaml.safe_load`) at its new
   home in `references/report.md` — the B5-3 repair does not regress in the move.
6. **Inbound-pointer walk (verify, don't edit):** each pointer in the Re-grounding's
   list (contract `:169/:230/:236`, `consult.md:33/:49`, `spec.md:70`, `vlt-mint:162`,
   `frontmatter.md:242`, `vlt-lint`'s dispatch-block-shape reference,
   `wiki-consolidation.md:26`) dry-reads as resolving through the router; zero edits
   expected — any needed edit is a numbered deviation.
7. **Behavior dry-walk:** read router → reference end-to-end for one dispatch mode
   (`consult`) and one lint run shape (scoped), confirming every step/mode beat of the
   pre-cut file is reachable from the router and nothing is orphaned; the early
   "nothing in scope" lint exit completes without opening any reference.
8. **Copy surface:** confirm by reading `vlt-upgrade:48` that the wholesale `vlt-*`
   refresh carries `references/` (and that `:49`'s exclusion list does not catch the
   name); confirm `skill_asset_divergence`'s per-file compare accommodates new shipped
   files. Note in the BUILT record if either needed an edit.
9. **Instrument:** `tools/test-cost-manifest.py` green; module mode at the build's tree
   shows the dir-aware whale aggregates + `(router)` rows, with the router figures
   matching check 1's budgets.
10. **Scrub + cruft:** no personal/vault-local content or live artifact paths in any new
    file (placeholder paths only); delete any `.decision-log.md`; no commit beyond the
    build's own (release choreography rides the arc level).

## Acceptance (live — appended to the roadmap ledger)

(1) **[ship-verifiable]** the re-cut reaches the field intact — on the next ordinary
vlt-core upgrade: (a) the installed `vlt-dispatch` and `vlt-lint` dirs each carry the
router `SKILL.md` + `references/*.md`, routers within budget (dispatch ≤ 14,000 bytes,
lint ≤ 12,000), every reference named by its router present on disk and no orphan
reference (the F3 agreement, grep/ls-checkable on the installed vault); (b) the installed
routers' `depends_on:` acks are byte-identical to 0.8.0's plus B5-3..B5-6's shipped bumps
— no convention moved in this build — and the installed vault's convention-coherence
surface stays clean; (c) the installed `references/report.md` Step-5 fence parses whole
as strict YAML; (d) at rest at the release, `cost-manifest` module mode reports the
dir-aware whale aggregates with router rows within the budgets. Bounded — the upgrade
happens anyway.

(2) **[field-contingent]** the re-cut behaves and pays in live use — producing vault:
**vlt-core** (owner-run, factory-readable). On the first post-upgrade single-mode
dispatch invocation (a `consult` or a `ledger` glance): the session reads the router plus
that mode's reference only — no other mode's reference is opened (owner spot-check of the
session's reads). On the first post-upgrade scoped lint: the run never opens
`references/full-scale.md`, and its report is shape-identical to the pre-cut contract
(same keys, same fence, `entity_scan`/`governance_memory` lines composed as before) — the
re-cut moved text without moving behavior. Outcome measure, non-gating: the dispatch/lint
share of the originating token-expense signal shrinks on the invocation paths measured in
disposition 4/5; the owner's say-so note closes it. Non-gating at closeout.
