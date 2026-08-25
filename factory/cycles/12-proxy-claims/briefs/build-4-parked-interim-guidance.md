---
title: 'Build #4 — parked-interim guidance (a park records the blocker''s shape, and something re-reads it at the upgrade that can invalidate it)'
status: |
  BUILT 2026-08-25 — all seven F-sites shipped, `decision-log.md` 3 → 4 with five acks, all four
  ship-verifiable acceptance checks PASS at rest. Two deviations, both recorded below.

  **What shipped, per F-site.** F1 — `vlt-feedback/SKILL.md` gains `## The park a filing leaves
  behind` between Transport and the failure path: fires after the issue URL or the outbox write,
  offers (never automatic), names `_agent/mint/decision-log.md` under `kind: parked-interim`,
  carries the three required entry contents (blocker-as-current-shipped-behavior, filing
  reference, re-derive instruction), states the prohibition by pointer with its one-line reason,
  states the population bound, and names `vlt-upgrade`'s reconcile pass as the reader. `:3`
  `depends_on: []` → `["decision-log@4"]`. `description:` and `references/field-contract.md`
  untouched, as briefed. F2 — the convention: `version: 3` → `4`; `consumers:` gains
  `vlt-feedback` (now five); `:23`'s six-item gloss → point-at-the-map; `parked-interim` appended
  to the `kind:` enum; a new kind bullet after the `deviation` paragraph (gated, no `convention:`
  line, and — unlike `deviation` — **inside** the superseding-entry scan); the new
  `### Parked interims (v4)` subsection after `### Subject coherence (v3)`, the rule's single
  home, carrying the prohibition, the why-once (visible vs. silent degradation), supersession as
  resolution, the no-backfill population, and the two-mechanisms-one-rule statement; a fifth
  writers-roster bullet; the readers line extended to name `parked-interim`; a v4 Enforcement
  paragraph modelled on v2's (write-side, no new `vlt-lint` finding class). `enforcement_stage:`
  and `adoption_first_instance:` untouched, as briefed. F3 — five acks, below. F4 —
  `vlt-upgrade/SKILL.md:78` gains the third scan leg inside the same reconcile bullet:
  live-entry predicate, one line per park into `parked_interims_review:`, the
  `governance_rule_changes:`-non-empty clause, surface-only posture, idempotent-by-construction,
  and both declared constraints (no new `migrations_run` token; the classifiability tail does not
  apply). Step 3.7 and `:75` untouched. F5 — `parked_interims_review:` inserted at `:113`,
  immediately after `overlay_rules_review:`, never-omitted-when-empty; the prose paragraph at
  `:126` after the `governance_rule_changes` pairing. The persist-verify (now `:134`) needed no
  text edit and was **confirmed, not assumed** — see V4. The Crossing-v0.16.0 example and Step 5
  untouched. F6 — `vlt-mint/SKILL.md:104` gains one clause inside the existing parenthetical
  guidance, pointing at *Parked interims*; no restatement, `:26` untouched. F7 —
  `vlt-mint/assets/decision-log-template.md:3-5` becomes a subset gloss pointing at the
  convention's entry schema; the seed stays header-only.

  **Handshake (acceptance check 1) — PASS.** `consumers: [vlt-mint, vlt-upgrade, vlt-lint,
  vlt-ingest, vlt-feedback]`. Five acks, all `@4`, no strays:
  `vlt-feedback/SKILL.md:3`, `vlt-ingest/SKILL.md:4`, `vlt-mint/SKILL.md:3`,
  `vlt-lint/SKILL.md:4`, `vlt-upgrade/SKILL.md:3`. **The check of record is `package-lint`
  Group E**, run at rest: `PASS group E — self-description integrity`;
  `package-lint: A/B/C/E PASS, D SKIPPED — vlt 0.15.0` (D skipped by design — build-2 carries
  the version bump and the `--expect-version` gate). Group E earned its keep this build: its
  first run **FAILED** on a stray pin I had written into F4's prose (deviation 2).

  **Reader probe (acceptance check 2) — PASS, all four conditions.** Single agent, given the
  edited Step 3.5 + Step 4 and the edited convention, composing the Step-4 block over a
  four-entry fixture log. (a) `parked_interims_review:` carried **exactly one** line — entry 1,
  `conventions/extraction.md`, with its filing reference, the re-derive instruction, and the
  `governance_rule_changes`-non-empty clause fired. (b) The **negative control** — entry 2, a
  `parked-interim` superseded by entry 4 — was **absent**; the agent named the live-entry
  predicate as its reason. (c) The `deviation` entry was **absent** from the new key. (d) A
  second probe over a log with no parks rendered `parked_interims_review: []` — **present, not
  omitted**. `migrations_run` carried `decision-log-reconcile` in run A and nothing in run B; the
  agent independently stated that the parked leg "is a leg of that migration and adds no token of
  its own", which is the brief's declared exclusion read back off the shipped prose.

  **Prohibition battery (acceptance check 3) — PASS, six of six.** `"pre-authorized command
  sequence"` → **3** hits, one per file: the **rule** in `decision-log.md`, pointer clauses in
  `vlt-feedback` and `vlt-mint:104`. `"parked-interim"` → `decision-log.md` **5**,
  `vlt-upgrade` **3**, `vlt-feedback` **1**, **nowhere else**. `"decision-log@"` → **5** hits,
  **5** of them `@4` (aid only). `parked_interims_review` in `vlt-upgrade/SKILL.md` → **3** —
  third leg `:78`, schema key `:113`, prose `:126`. `grep -c "kind:"` on the convention → **6**,
  of which only `:39` is an enumeration (the rest are the `kind:` bullet, the subject-coherence
  and classifiability-tail prose, and the readers line) — **no second enumeration introduced**.
  `"stage promotions, upgrade-time rulings, retirements"` → **0**; both drifting glosses gone.
  Plus `package-lint` A/B/C **PASS**.

  **R4 audit (acceptance check 4) — PASS.** A rendered fixture report was parsed and its
  top-level key set compared against the shipped schema block: **21 schema keys, 21 rendered
  keys, SET MATCH True, ORDER MATCH True**. `parked_interims_review` sits at **index 16** in
  both, immediately after `overlay_rules_review` — so it renders in order under `:93`'s
  walk-the-block rule and passes the `:134` persist key-set verify. **Declared non-widening
  confirmed:** `migrations_run` (`:109`) still carries its **10** original tokens and contains no
  `parked` token, with the reason stated at the third leg.

  **V6 — PASS.** The legal response is at its own single home in both halves: the Step 3.5 bullet
  and the Step-4 prose ("surface only", "never auto-resolves", resolution as a superseding entry
  through the rostered route); the convention's Enforcement section carries the v4 write-side
  paragraph naming no new `vlt-lint` finding class. **V7 — PASS.** The population line is in
  **both** the `vlt-feedback` step and §Parked interims. A line-by-line audit of every deletion in
  `git diff skills/` confirms **no prohibition was removed anywhere** — the removals are the four
  old pins, the two drifting glosses, the `kind:` enum line (replaced by a wider one), the readers
  line (replaced by an extended one), and the `vlt-mint:104` sentence (replaced with its clause
  added). **This build is +1 prohibition added, 0 retired** — the number Cycle 12's closeout
  records for P-15's series. **V8 — PASS:** `grep -nE "mikeypioli|/Users/|vlt-core|gowermikey"`
  over every changed file → **0 hits**; the only illustrative references in shipped prose are
  `_agent/mint/decision-log.md` (a module-defined fixed agent-zone path) and placeholder forms.
  **V9 — PASS:** `find . -name ".decision-log.md" -not -path "./.git/*"` → **0**. The collision
  the brief flagged was handled: no `_agent/mint/decision-log.md` was touched, and the two fixture
  logs were built in the session scratchpad, never in the working tree.

  **Durability re-check (B1 local-mint preserve path).** F4/F5 touch `vlt-upgrade`, so the
  preserve path was re-checked: the diff is **four hunks** — the pin (`:3`), the third leg
  (`:78`), the schema key (`:113`), the prose (`:126`). Nothing in the own-the-apply path,
  `mints_preserved`, `bodies_restored`, the capabilities reconcile-not-replace step, or the
  overlay preservation rules was touched. The new leg is **read-and-surface only** and the new
  report key is report-only — neither writes, merges, or destroys anything a vault grew locally.

  **Cite re-grounding.** Every `file:line` the brief rests on was re-derived at HEAD (`5585877`)
  before editing: `vlt-feedback` `:14-16`, `:38-42`, `:104`, `:107-120`, `:115-116`, `:118-120`;
  `vlt-mint` `:26`, `:104`; `vlt-upgrade` `:78`, `:93`, `:109`, `:111`, `:112`, `:131`; the
  convention's `:11`, `:12`, `:23`, `:39`, `:46`, `:74-78`, `:80-89`, `:91-94`, `:102-108`; and
  `decision-log-template.md:3-4`. **All correct — no further drift found**, so build-2 inherits
  the thirteen already logged and no fourteenth. Line numbers that moved *because of this build*
  are restated above for build-2's benefit: in `vlt-upgrade/SKILL.md` the report key is `:113`,
  its prose `:126`, and the persist-verify moved `:131` → `:134`.

  **Deviations (2).**

  1. **`last_updated:` bumped 2026-08-24 → 2026-08-25 in `decision-log.md`.** The brief's F2
     enumerates nine changes and does not name this one. *Reason:* the file's own
     `frontmatter.md` schema carries `last_updated:`, and build-3 (`5585877`) bumped exactly this
     field on every governance file it edited this cycle. Leaving it stale on a file whose
     `version:` moved in the same commit would have shipped a governance file asserting it was
     last changed before its own rule change. Routine consistency call, no owner in the room.
  2. **F4's third-leg prose was rewritten to avoid a version pin.** As briefed, the leg explained
     that the classifiability tail does not apply because `parked-interim` "exists only from
     `decision-log@4`". `package-lint` **Group E FAILED** on that first run — E3 flagged it as a
     *stray pin*: `vlt-upgrade/SKILL.md:78 recites the pin decision-log@4 outside depends_on:`.
     E3 is right; the sentence is a pointer, not a second ack. *Reason:* rewritten to the
     version-free form "the decision-log convention's v4", which is E3's own named remedy. Lint
     re-run clean. Recording this because the failure is evidence Group E works, and because a
     later build writing convention-version prose into a skill body will hit the same edge.

  **Owner ruling still needed (recorded, not acted on).** Disposition 9 stands unchanged and is
  **not** discharged by this build: the roadmap's A46 grades A12-5's **module side** *"BLOCKED
  (unreachable) until A33's `governance_rule_changes:` key exists"*, and build-3 shipped that key
  (`vlt-upgrade/SKILL.md:111`, `5585877`). **The BLOCKED grading is stale on this branch.**
  Re-grading a platform item (`P-17`) is an owner act; this build changed no scope on account of
  it. Acceptance checks (5) and (6) remain field-contingent and ungraded, as briefed.
module_code: 'vlt'
created: '2026-08-25'
derives_from:
  - 'factory/inbox/2026-08-25-111324-parked-interim-exit-condition-silently-invalidated-by-its-ruling.md (A12-5, vault side — the exit-condition-as-command-sequence hazard and its re-read gap)'
roadmap: 'factory/cycles/12-proxy-claims/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-25): Q7 (BOTH moves; the vault side rides this cycle as new prose in `skills/vlt-feedback/`), D1 (one obligation, tracker half and field half built separately on separate channels), E6 (the parked-interim survey is a scheduled, non-blocking owner task and does not gate this build), D2 (every brief answers the retirement clause); §Roundtable amendments A36–A40 (make it a step with an artifact; name a home something re-reads; state the population; rule the `vlt-mint` relationship; grade the obsolescence beat honestly)'
risk: 'moderate — it bumps `decision-log.md` 3 → 4 (a genuine rule change: a new `kind:` in the entry schema and a new writer on the protected roster), so the consumer walk is five acks in this build (four re-acks + one new). No contract edit (no C6), no new lint check (no E4), no asset node touched (no E5).'
---

# Build #4 — parked-interim guidance

## 2. Intent

A vault that hits an upstream blocker does the right thing today: it files the question
through `vlt-feedback` and parks whatever it was doing. What it then writes down is the
problem. `{field-vault}` recorded its exit condition as *a mechanical unwind* — in substance
*"one `git mv` plus one structure-map value"* — which was true under the reading of the
blocker it held at parking time. The ruling shipped under a different reading. The exit was
not left unmet; it became **wrong**, silently, and it still reads to a later reader as
*"ruling landed, one-line exit, pre-authorized."* That asymmetry is the whole filing: an
**unmet** exit is visible (the vault checks, sees it unsatisfied, waits); an **invalidated**
exit reads as satisfied.

This build ships A12-5's vault side, whole, in three parts that are one mechanism:

1. **A prohibition with an artifact to attach to.** `vlt-feedback` gains a step: after the
   filing lands, offer to record a **parked-interim** entry carrying the blocker as a claim
   about *current shipped behavior*, the filing reference, and the standing instruction to
   re-derive the unwind against the rules in force at unwind time — **never a pre-authorized
   command sequence**. (A36: *"the prohibition attaches to a field of an artifact the skill
   actually writes, or it does nothing."*)
2. **A record home that something re-reads.** The entry is a mint-decision-log entry under a
   new `kind: parked-interim`. `vlt-feedback` is invoked-only and never re-reads anything
   (`SKILL.md:38-42`), so a record it alone owned would be write-only. The decision log is
   already re-read by `vlt-upgrade`'s reconcile pass — and an **upgrade is precisely the event
   that moves the rules an exit rests on**. (A37.)
3. **The re-read itself.** `vlt-upgrade`'s decision-log reconcile gains a third scan leg and
   the post-flight report gains `parked_interims_review:` — so the release that invalidates a
   park is the moment the park is surfaced, beside `governance_rule_changes:` (build-3's F11),
   which says what moved.

**Population, stated up front and not over-claimed (A38):** this changes parks written
**after** the upgrade that carries it. It repairs **none already recorded** — including the
single observed instance the filing rests on, which is served instead by the owner's
hand-delivered re-derive notice when build-3 ships (roadmap §Owner actions, A57).

**All rejected alternatives in the parent filing are settled — do not re-litigate.** In
particular: the module-side CHANGELOG re-derive notice is **not** this build (Q7 rules BOTH
moves, and the module side is platform work — see §6), and no relocation or repair mechanism
is built (E6's survey is an owner task and explicitly does not gate this build).

## 3. Brief-time dispositions

**1. The re-read home is the mint decision log, as a new `kind: parked-interim`, read by a
third leg of `vlt-upgrade`'s reconcile pass.** *(Answers A37, which named the decision log as
"the candidate" and required the brief to name a home something re-reads.)*

The alternatives were: (a) a new agent-zone folder scanned by `vlt-upgrade`; (b) `vlt-mint`'s
activation resume scan (`vlt-mint/SKILL.md:26`); (c) the decision log. (a) builds a second
parallel record system for gated vault decisions and violates single-home discipline for zero
new capability. (b) is the wrong reader — the mint resume scan fires at *mint* activation and
resolves *council* blockers; an upstream park resumes on a **release**, which the mint scan
never sees. (c) fits without strain: the log is already *"the vault's permanent,
upgrade-durable record of every gated decision"* (`decision-log.md:23`), it is already
append-only with a supersession idiom whose superseding entry is exactly what a resolved park
produces, and `vlt-upgrade`'s reconcile already implements *"entries with no accounted-for
superseding entry"* (`vlt-upgrade/SKILL.md:78`) — the precise predicate a live park needs.
The upgrade is also the *right moment*: it is the only recurring vault event that both (i)
crosses the versions in which a rule can have moved and (ii) already renders what moved
(`governance_rule_changes:`, `vlt-upgrade/SKILL.md:111`).

**2. The prohibition single-homes at `{conventions}/decision-log.md`; `vlt-mint:104` gains a
one-clause pointer; the two parks stay separate mechanisms.** *(A39 required this be ruled
and "not a silence".)*

A39 is right that `vlt-mint/SKILL.md:104` is a second population and already complies —
*"Write the condition into the planning doc"* is a condition, not a command sequence. But the
two parks are genuinely different objects: `vlt-mint`'s park is against an **unfieldable
council** and resumes on an activation-time scan of `_agent/mint/`; a `vlt-feedback` park is
against an **upstream ruling** and resumes on a release the vault must notice. Merging them
would force one mechanism to carry two resume paths. So: the **rule** (*an exit condition
records the blocker's shape and the filing reference, never a pre-authorized command
sequence*) is generic and single-homes once, in the convention; the **mechanisms** stay
separate; `vlt-mint:104` carries a short pointer so the mint park is visibly governed by the
same rule without restating it. This is point-at-the-map, per CLAUDE.md's single-home rule.

**3. `vlt-feedback` becomes a rostered decision-log writer, and its write is a human-gated
offer.** The convention's writer roster is *"the roster the handshake protects"*
(`decision-log.md:80-89`) and an op outside it *"never appends"* — so shipping this step
without the roster edit would ship an illegal write. The write is an **offer**, never
automatic, matching the skill's existing posture on both axes: invoked-only (`:38-42`) and
approval-gated (`:77-83`). Nothing appends as a side effect of a filing.

**4. Interim posture (R1) — applicable, and satisfied structurally, not by declaration.** The
prohibition, the artifact that carries it, the record home, and the reader all ship in **this
one build**. There is no window in which the rule exists and its mechanism does not, so no
interim posture is declared. The honest residual is not an interim posture but a **population
bound** (disposition 5).

**5. The population bound is written into the shipped prose, not only into this brief (A38).**
The `vlt-feedback` step and the convention section both say plainly that the rule governs
entries written from this version on, and that **pre-existing parked records are not
retroactively repaired** — append-only means no backfill, exactly as the convention already
rules for its `ref:` key and verdict provenance (`decision-log.md:57`, `:72`). A reader who
finds an old park with a command-sequence exit is told to supersede it, not to rewrite it.

**6. Retirement clause (A40) — ONE PROHIBITION ADDED, NONE RETIRED. Recorded as such, not as
`not applicable`.** *"Never a pre-authorized command sequence"* is a new prohibition and this
build withdraws no counterpart. The room asked specifically that this be entered honestly
rather than dressed up: it is the eleven-cycles-add-nothing-retires pattern P-15 exists to
make visible, and Cycle 12's retirement count (P-15's tripwire series, A50) must record this
build as **+1 added, 0 retired**. The nearest candidate was examined and rejected: `vlt-mint`
`SKILL.md:104`'s park instruction is not a prohibition and is not made redundant — it is
brought under the new rule by pointer (disposition 2). *No `supersession` note is filed,
because nothing is superseded.*

**7. The completeness-claiming kind lists are converted to point-at-the-map.** Two sites
gloss the log as covering *"mints, capability changes, convention edits, stage promotions,
upgrade-time rulings, retirements"* — `decision-log.md:23` and
`vlt-mint/assets/decision-log-template.md:3-4`. **Both already drifted at v3**: neither lists
`deviation`, which shipped as a kind. Rather than widen two lists that will drift again (the
standing rule: *lists that claim completeness drift*), both become a subset-with-pointer
gloss naming the entry schema as the enumeration's single home. This is bundled here because
adding a seventh kind is the moment the drift becomes two-deep.

**8. `parked_interims_review:` is a new report key, not a reuse.** It mirrors
`overlay_rules_review:` (`vlt-upgrade/SKILL.md:112`) exactly: report-only, never auto-edited,
**never omitted when empty**. Folding it into `governance_divergence` or
`governance_rule_changes` would be wrong on both counts — it is not a divergence (nothing in
the vault drifted) and it is not a rule change (it is the vault's *record* of one it is
waiting on). The empty-render rule is load-bearing here for the same reason it is for
`governance_rule_changes`: an absent line reads as "no parks", which is precisely the silence
the filing is about.

**9. Not self-authorized — flagged for the owner: A46's BLOCKED grading is now stale.** The
roadmap grades A12-5's **module side** *"BLOCKED (unreachable) until A33's
`governance_rule_changes:` key exists"* (§Owner actions, A46). Build-3 shipped that key
(`vlt-upgrade/SKILL.md:111`, commit `5585877`, F11), so the precondition **now exists on this
branch**. That does not change this build's scope by one line — the module-side move is the
CHANGELOG re-derive notice in the release choreography, which is platform work on `P-17`, not
a cycle build. But the grading it rests on is no longer true, and re-grading a platform item
is an owner act, not a briefer's. **Recorded, not performed.**

## 4. F-sites

*Every `file:line` below was re-derived against HEAD (`5585877`, branch `cycle12-v0.16.0`) in
this session. Three roadmap cites had drifted — see §"Grounding corrections" at the foot.*

---

### F1 — `skills/vlt-feedback/SKILL.md` — the parking step (the artifact A36 demanded)

**Current state.** The file is 7,186 bytes and contains **zero** occurrences of *park*,
*interim*, *exit condition* or *blocker* (`grep -cin "park\|interim\|exit condition\|blocker"`
→ **0**, verified at HEAD — Q7's grounding figure re-confirmed). Its shape is a sequence of
steps that each produce an output and a gate:

- `:14-16` — *"The issue is **transport**, not the record — the module's factory materializes
  accepted issues into its own inbox…"*
- `:38-42` — `## Trigger model — invoked-only, never auto-file`.
- `:59-83` — compose, the scrub checklist, the mandatory approval `HALT`.
- `:85-105` — `## Transport`: labels, pre-flight, the `gh issue create` call, *"Show the user
  the created issue URL."* (`:104`).
- `:107-120` — `## The failure path`: writes `_agent/feedback-outbox/{YYYY-MM-DD-HHmmss}-{slug}.md`,
  and says of it *"it is a recovery artifact, **not a record**"* (`:115-116`) and that the
  folder is *"deliberately **not** a `vault_structure` logical name"* (`:118-120`).

So the skill's only vault-side write today is a transient outbox that declares itself not a
record. There is nothing here for a prohibition to attach to.

**The exact change.** Insert a new section **between `:105` and `:107`** — after Transport
ends, before the failure path — titled `## The park a filing leaves behind`. It states, in
this order:

1. **When it fires.** After the issue URL is shown (`:104`) **or** after the outbox file is
   written on the failure path — a filing that failed transport still parks the vault — ask
   one question: *is the vault holding an interim arrangement until the module answers this?*
   If no, nothing happens. If yes, **offer** to record it. Human-gated; never automatic
   (disposition 3, and the skill's own `:38-42` posture).
2. **What the record is.** An append to `_agent/mint/decision-log.md` under
   `kind: parked-interim`, `ref:` naming the governed object the park is against. The entry
   shape, the `ref:` key, the classifiability tail and the supersession idiom are
   **single-homed at `{conventions}/decision-log.md`** — read them there, restate them
   nowhere. (Mirrors `:18-20`'s treatment of the field contract, and `:124-126`'s References
   discipline.)
3. **The three things the entry must carry**, which is where the rule lives from the writer's
   side: **(a)** the blocker stated as a claim about **current shipped behavior** — what the
   module does today that forces the interim — never as a prediction of what the ruling will
   say; **(b)** the **filing reference** (the issue URL, or the outbox path plus its intended
   title where transport failed); **(c)** the standing instruction: *when the ruling lands,
   re-derive the unwind against the rules in force at unwind time.*
4. **The prohibition, by pointer.** *An exit condition never records a pre-authorized command
   sequence.* Cite `{conventions}/decision-log.md` (*Parked interims*) as its home; give the
   one-line reason so the writer understands rather than obeys: **the rule the unwind depends
   on can move underneath the record, and a command sequence goes wrong silently while a
   description of the blocker goes stale visibly.**
5. **The population line (A38 / disposition 5).** This governs parks recorded from here on; it
   repairs nothing already written. An existing park with a command-sequence exit is
   **superseded**, never rewritten (append-only).
6. **Who reads it.** One clause naming `vlt-upgrade`'s reconcile pass, so the writer knows the
   record is not write-only — the release that can invalidate the park is the moment it is
   surfaced.

**Also change `:3`:** `depends_on: []` → `depends_on: ["decision-log@4"]`. This is the
handshake ack the roster edit in F2 requires; see F3.

**Why.** A12-5's vault side, ruled by Q7 to ride this cycle; A36's requirement that the rule
attach to an artifact the skill actually writes.

**Out of scope at this site.** The `description:` in frontmatter (`:4`) is **not** changed —
the parking step is a sub-beat of an existing invocation, not a new trigger, and changing it
would owe a `module-help.csv` row edit for zero information (see §5). `references/field-contract.md`
is **not** touched: the record is vault-side and never enters the issue payload, so
`rail_contract` stays `1` and the additive-only evolution rule is not engaged.

---

### F2 — `skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md` — the kind, the roster, the rule (3 → 4)

**Governance SSoT reminder:** this bundle at `skills/vlt-setup/assets/governance/_meta/` is
the **only** legal home. Do not create or edit any second copy.

**Current state**, re-derived at HEAD:

| line | current text (abridged) |
|---|---|
| `:11` | `version: 3` |
| `:12` | `consumers: [vlt-mint, vlt-upgrade, vlt-lint, vlt-ingest]` |
| `:23` | *"…record of every gated decision — mints, capability changes, convention edits, stage promotions, upgrade-time rulings, retirements."* (**omits `deviation` — already drifted at v3**) |
| `:39` | `- kind: mint \| capability-change \| convention-edit \| stage-promotion \| upgrade-ruling \| retirement \| deviation` |
| `:46` | the `kind:` bullet — *"it is how `vlt-upgrade`'s reconcile pass finds gated `convention-edit`/`upgrade-ruling` entries with no accounted-for superseding entry"*, plus the `deviation` paragraph |
| `:74-78` | `## Supersession idiom` — `supersedes:` / `superseded_by:` / *"A **live** entry is one no later entry supersedes"* |
| `:80-89` | `## Writers and readers (the roster the handshake protects)` — four writers (`:84-87`), *"An op outside this roster **never appends**"* (`:89`) |
| `:91-94` | Readers — `vlt-upgrade`'s reconcile pass scopes by `kind:` (`:93`); `vlt-lint`'s read-before-flag matches by `ref:` (`:94`) |
| `:102-108` | `## Enforcement` — the read-before-flag; the v2 write-side paragraph (`:108`) that is the template for v4's |

**The exact changes.**

1. **`:11`** — `version: 3` → `version: 4`. This *is* a rule change, not a clarification: it
   adds a value to an enumerated schema key and adds a writer to the protected roster. The
   consumer walk is F3 and lands in **this build** (CLAUDE.md version-handshake rule).
2. **`:12`** — `consumers: [vlt-mint, vlt-upgrade, vlt-lint, vlt-ingest, vlt-feedback]`.
3. **`:23`** — replace the six-item gloss with a subset-with-pointer form: *"…record of every
   gated decision — mints, convention edits, upgrade-time rulings and the rest; **the kinds
   are enumerated once, in the entry schema below**."* (Disposition 7.)
4. **`:39`** — append ` | parked-interim` to the `kind:` enum.
5. **After `:46`'s `deviation` paragraph** — a new bullet defining the kind, in the same voice:
   a **`parked-interim`** records that the vault is holding an interim arrangement **pending an
   upstream ruling it has filed**. Its `ref:` names the governed object the park is against;
   it is a **gated** kind (`verdict:` with provenance required, per v2 — the human accepting
   the offer is the gate, so `user-ruled` provenance with its required *why* is the ordinary
   form); it carries **no `convention:` line** (nothing moved); and — the point of the kind —
   it **is inside the reconcile pass's superseding-entry scan**, because its whole purpose is
   to be superseded when the ruling lands. Contrast `deviation`, which is explicitly outside
   that scan.
6. **New subsection `### Parked interims (v4)`**, placed after `### Subject coherence (v3)`
   (`:59-63`) so the versioned rules read in order. It is the **single home** of the rule:
   - *An exit condition records the **blocker's shape** and the **filing reference** — never a
     pre-authorized command sequence.* State the blocker as a claim about **current shipped
     behavior**; state the resume instruction as *re-derive the unwind against the rules in
     force at unwind time*.
   - **The why, once:** the record's confidence is inherited from the rule it was written
     against, and that rule can move. An **unmet** exit is visible — the vault checks and
     waits. An **invalidated** exit reads as *satisfied and pre-authorized*, and a later reader
     executes a move that is now illegal. A description of the blocker degrades **visibly**; a
     command sequence degrades **silently**.
   - **Resolution is supersession**, per *Supersession idiom* (`:74-78`) — the resolving entry
     carries `supersedes:`, the park is marked in place. A live park is one no later entry
     supersedes; that is exactly what the reconcile pass reads.
   - **Applies to every new entry from v4 on. No backfill** — the same posture as v2's
     provenance rule (`:57`) and v3's subject coherence (`:63`).
   - The two shipped park mechanisms are named and kept separate (disposition 2): a
     `vlt-feedback` park against an upstream ruling resumes on a **release**; a `vlt-mint` park
     against an unfieldable council resumes on an **activation scan** (`vlt-mint/SKILL.md:104`,
     `:26`). One rule, two mechanisms.
7. **`:84-87` writers roster** — add a fifth bullet: *"`vlt-feedback`'s parking offer —
   parked-interim entries, human-gated, after a filing is posted or written to the outbox."*
8. **`:93` readers** — extend the reconcile-pass line to say it scopes by `kind:` **for
   `convention-edit`/`upgrade-ruling` and for `parked-interim`**, so the reader roster names
   the new traffic. (`:94`'s `vlt-lint` line is unchanged — see §6.)
9. **`## Enforcement` (`:102-108`)** — append a v4 paragraph modelled verbatim on `:108`'s v2
   paragraph: the parked-interim rule is **write-side**, enforced by the ceremony that writes
   the entry (`vlt-feedback`'s parking offer is the first), and is **not** covered by the
   read-before-flag check, which keys on `ref:` only. **No new `vlt-lint` finding class ships
   with v4**; a build that later adds a parked-interim checker owes that check its own stated
   legal response. *(This paragraph is also this build's R3 answer for the convention half —
   see §7.)*
10. **Reading list (`:110-115`)** — unchanged. No new cross-reference is created.

**Why.** A37's re-read home requires the kind to exist in the schema the reader scopes by; A36's
prohibition needs one home; disposition 2 places it here.

**Out of scope at this site.** No `enforcement_stage:` change (`:13` stays `checked`, owner
`vlt-lint`, moment *lint run*) — the v4 rule is write-side and adds no check, exactly as v2 and
v3 did. `adoption_first_instance:` (`:16`) is **not** stamped by this build — it is stamped by
the first authorized ceremony ref-keyed entry, in a vault, and this build ships no instance.

---

### F3 — the consumer walk: five acks in this build

**Current state**, re-derived at HEAD:

| file:line | current |
|---|---|
| `skills/vlt-mint/SKILL.md:3` | `depends_on: ["spec@2", "frontmatter@13", "decision-log@3"]` |
| `skills/vlt-upgrade/SKILL.md:3` | `depends_on: ["spec@2", "decision-log@3"]` |
| `skills/vlt-lint/SKILL.md:4` | `depends_on: [… "decision-log@3" …]` (multi-pin line) |
| `skills/vlt-ingest/SKILL.md:4` | `depends_on: [… "decision-log@3" …]` (multi-pin line) |
| `skills/vlt-feedback/SKILL.md:3` | `depends_on: []` |

**The exact change.** Re-pin `decision-log@3` → `decision-log@4` in the four existing
consumers, and give `vlt-feedback` its first `depends_on:` line carrying
`["decision-log@4"]` (F1 makes the edit; it is listed here so the walk is one table).

**Verify bipartite in both directions** — every skill in `:12`'s `consumers:` acks `@4`, and
no skill acks `decision-log@` that `:12` does not list. **The check of record is `package-lint`
Group E** (`tools/package-lint.py`, E1 handshake-bipartite / E2 structure-map SSoT / E3
stray-pin). A hand-written `grep "decision-log@" skills/` is **self-confirming** and is not the
recorded verification — it greps the token you just wrote in the files you just edited. Use it
while editing if you like; record Group E.

**Why.** CLAUDE.md's version-handshake rule: a convention **rule** change bumps `version:` and
re-acks every consumer **in the same build**.

**Note (E5 does not apply).** `decision-log.md` has no `.js` asset-node consumer — every entry
in `:12` is a skill. No `// depends_on:` header is touched.

---

### F4 — `skills/vlt-upgrade/SKILL.md:78` — the third reconcile leg (the re-read)

**Current state.** `:78`, inside Step 3.5's migration list, is the
**Decision-log reconcile (human-gated, post-schema only)** bullet. It already carries:

- **Leg 1** — scan `_agent/mint/decision-log.md` for gated `convention-edit` (or
  `upgrade-ruling`) entries with **no accounted-for superseding entry**, and **surface** each.
- **Leg 2** — the `ref:`-key migration for existing installs (overlays, base divergences,
  retired capabilities with no live `ref:`-keyed entry) → one `undisposed` line each.
- The shared posture: *"never auto-writes, never auto-restores"*; *"this pass only surfaces"*;
  record `decision-log-reconcile` in `migrations_run`; the honesty bound for pre-schema and
  pre-key entries (*"cannot classify — review manually"*, never a silent skip).

**The exact change.** Add a **third scan leg** to the same bullet, in the same voice:

> **Third scan leg (parked interims).** Scan `_agent/mint/decision-log.md` for **live**
> `kind: parked-interim` entries — live per `{conventions}/decision-log.md` (*Supersession
> idiom*): no later entry supersedes it. Surface one line per live park in
> `parked_interims_review:`, carrying the entry's `ref:`, its filing reference, and the
> standing instruction: **re-derive the unwind against the rules in force now — do not execute
> the exit as recorded.** Where this run's `governance_rule_changes:` is non-empty, say so on
> the line: *the rules this park rests on may be among the ones that just moved.* **Surface
> only** — never supersede an entry, never edit the log, never resolve a park (the same posture
> as the two legs above). A park is resolved by the human, and the resolution lands as a
> **superseding entry** through the rostered write route (Step 3.7), which is what makes the
> next run's scan skip it. **Idempotent by construction** — a superseded park is not live and
> is not surfaced again.

**Two deliberate constraints, stated in the bullet so the builder does not have to infer them:**

- The leg reuses the existing `decision-log-reconcile` token in `migrations_run` — it is a leg
  of that pass, not a new migration. No new `migrations_run` value. *(Declared R4 non-widening;
  see §7.)*
- The leg is **not** "post-schema only" in the way legs 1 and 2 are: `parked-interim` exists
  only from v4, so every entry carrying the kind is by construction fully-keyed. The
  classifiability tail does not apply to it; say so in one clause rather than leaving a reader
  to wonder whether the honesty bound covers it.

**Why.** A37 — the record must be re-read by something, and the upgrade is the event that can
invalidate a park.

**Out of scope at this site.** `:88`'s Step 3.7 (*Upgrade-time rulings — write them through*)
is **not** changed: a park resolved during an upgrade is already covered by its general rule
(*"an upgrade-time user ruling propagates to the mint decision log"*) and the superseding-entry
route it names. Adding a parked-interim clause there would restate a rule that already covers
it. The relocation-migration discipline at `:75` is untouched — a park is not a file move.

---

### F5 — `skills/vlt-upgrade/SKILL.md` Step 4 — the report key (R4 widening)

**Current state.** The Step-4 post-flight report (`:91-133`) is composed by **walking the
schema block top-to-bottom and rendering every key in order — never from memory** (`:93`), and
the persist is verified by parsing the written YAML and checking *"its top-level key set matches
the schema block"* (`:131`). Re-derived key lines:

| line | key |
|---|---|
| `:109` | `migrations_run: [decision-log-relocation \| overlay-lift \| … \| decision-log-reconcile \| decision-log-write \| …]` |
| `:111` | `governance_rule_changes: […]   # never omitted when empty` (build-3 F11) |
| `:112` | `overlay_rules_review: […]   # never omitted when empty` |
| `:116` | `family_invariant_drift: […]` |

**The exact change, three parts:**

1. **Insert a new key immediately after `:112`** — after `overlay_rules_review:`, keeping the
   two report-only review lines adjacent:

   ```yaml
   parked_interims_review: [<ref: parked pending <filing reference> — re-derive the unwind against the rules in force now; do not execute the exit as recorded>, ...]   # live kind: parked-interim entries — report-only, never auto-resolved; never omitted when empty ([] = no live park in the log, or no log)
   ```

2. **A prose paragraph** after `:112`'s siblings are explained (the `governance_rule_changes`
   paragraph is `:121-123`; place this one after it, so the pairing reads in the order the
   keys render): `parked_interims_review` is the **park-invalidation surface**. It renders one
   line per live `kind: parked-interim` entry in `_agent/mint/decision-log.md`, sourced by
   Step 3.5's third reconcile leg. It is a **report, never a gate**, and it **never
   auto-resolves** — a park is resolved by a human, as a superseding entry through the rostered
   write route. It is **never omitted when empty** (the `local_conventions_intact` idiom): an
   absent line would read as *"no parks", which is precisely the silence this key exists to
   break* — an invalidated exit already reads as satisfied, and a missing report line would
   confirm the wrong reading. Its natural companion is `governance_rule_changes:` above it:
   that key says what moved, this one says who was waiting on it.

3. **`:131`'s persist-verify** needs no text edit — it checks the key set against the schema
   block, which now contains the new key. **Confirm this at build time and record the
   confirmation**; do not assume it.

**Why.** R4 (enumeration widening): the schema block is the enumeration, the report is composed
by walking it, and the persist verifies against it. A leg that surfaces into a report without a
key in that block would render "from memory", which `:93` forbids.

**Out of scope at this site.** `:123`'s **Crossing v0.16.0** worked example (build-3's) is
**not** extended — it illustrates `governance_rule_changes`, and this build changes no
governance rule a *vault* reads differently. The upgrade ledger (Step 5) is not touched: parks
are the log's business, and the ledger records drift from stock.

---

### F6 — `skills/vlt-mint/SKILL.md:104` — the pointer (A39, answered)

**Current state.** `:104` is the park fallback for an unfieldable council:

> **Park (the default — the only path in an unattended session).** Write the condition into the
> planning doc (`council verdict: not fielded — <why>; parked`), leave the checklist incomplete
> at Phase 2, and stop. The activation-time resume scan picks the mint up in a session that can
> field the panel — parking is the *designed* response, not a failure.

**The exact change.** Append **one clause** to the first sentence's parenthetical guidance —
not a new paragraph, not a restatement:

> …and state the condition as the **blocker's shape**, never a pre-authorized command sequence
> (`{conventions}/decision-log.md`, *Parked interims* — one rule, both parks).

**Why.** A39 required the brief to rule the `vlt-mint` relationship rather than be silent, and
observed that `:104` **already complies**. So this is a pointer that makes the governing rule
visible at the second population, not a fix. Single-home discipline: the mechanics stay in the
convention.

**Out of scope at this site.** `vlt-mint:26`'s activation resume scan is **not** extended to
read parked-interim entries. It scans `_agent/mint/` for **incomplete planning docs** and
resumes mints; a `vlt-feedback` park has no planning doc and does not resume at mint
activation. Conflating them would give one scan two resume semantics.

---

### F7 — `skills/vlt-mint/assets/decision-log-template.md:3-4` — the seeded gloss

**Current state.** `:3-4`: *"The vault's permanent record of every gated decision — mints,
capability changes, convention edits, stage promotions, upgrade-time rulings, retirements."*
Same drift as `decision-log.md:23`: `deviation` is missing, and `parked-interim` would make it
two behind. `:12-15` already does the right thing for the entry shape — it points at
`_meta/conventions/decision-log.md` and says *"do not restate the mechanics here."*

**The exact change.** Bring `:3-4` under the same discipline as `:12-15`: a subset gloss ending
in a pointer to the convention's entry schema as the enumeration's single home.

**Why.** Disposition 7. This asset is what `vlt-setup` seeds a fresh log from
(`vlt-setup/SKILL.md:303`, header-only, seed-only-when-absent), so the gloss is the first
description of the log a new vault ever reads.

**Out of scope at this site.** No other template content changes; the seed remains header-only
and `vlt-setup`'s never-clobber discipline is untouched.

## 5. Registration

**None.** No new skill directory, no new workflow, no `module-help.csv` row change (the
`vlt-feedback` row at `module-help.csv:18` stands — F1 deliberately leaves the skill's
`description:` unchanged, so the CSV mirrors nothing new).

**But a convention rule DID change, so the walk is named:** `decision-log.md` **3 → 4**, five
acks in this build (F3) — four re-acks plus `vlt-feedback`'s first pin. Verified by
`package-lint` **Group E**.

**"No bump owed" is not "no cost" — the other gates, priced:**

- **C6 (rule-card derivation)** — **not triggered.** This build does not touch
  `vault-operating-contract.md`, so no re-derivation of `_meta/vault-rule-card.md` and no
  `RULE_CARD_BUDGET` pressure. *(Build-3 already spent that budget this cycle.)*
- **E4 (harness coverage)** — **not triggered.** No new `package-lint` check is added, so
  `tools/test-package-lint.py` needs no declaring case and `CASE_FLOOR` does not move.
- **E5 (asset nodes)** — **not triggered.** No `.js` asset is edited and
  `decision-log.md`'s `consumers:` contains no `.js` entry, so no `// depends_on:` header is in
  the walk.
- **E6 (fan-out schema size)** — **not triggered.** No fan-out schema is touched.

## 6. Out of scope (dispositioned)

1. **A12-5's module side — the "if you parked against this, re-derive your exit" CHANGELOG
   note.** *Platform channel.* Q7 rules BOTH moves but places the module side on the new
   platform item (`P-17` per Q3/D1); `.github/` and the release choreography are never
   delivered to vaults. **See disposition 9 — its A46 BLOCKED grading is stale and needs an
   owner re-grade; this brief flags, does not act.**
2. **A `vlt-lint` finding class for parked interims** (e.g. `parked_interim_command_sequence`).
   *Deliberately not built.* Three reasons: the invalidating event is a **release**, which is
   upgrade-time, not lint-time, so the upgrade reader is the correct one and the lint one would
   fire at the wrong moment; the v4 rule is write-side, matching how v2 and v3 shipped; and
   build-3 already adds a governance check to this release. The convention's Enforcement
   section says so explicitly (F2 item 9), so a later build that wants the checker knows it
   owes it a legal response.
3. **Repairing parks already recorded, including the one observed instance.** *Out of
   population by construction* (A38, disposition 5) — append-only means no backfill. The known
   instance is served by the owner's hand-delivered re-derive notice when build-3 ships
   (roadmap §Owner actions, A57).
4. **E6 — the parked-interim survey across live vaults.** *Owner task, non-blocking* (E6,
   RULED Round 8): the owner runs it against `{field-vault}`'s mint decision log and any parked
   records, **bounded to before Cycle 13's `inbox-capture`, reporting a list, not a count**
   (A56). Findings file forward as new filings. It does not gate this build, which is written
   against the mechanism and the one observed instance, not against a count.
5. **The field contract (`references/field-contract.md`) and `rail_contract`.** *Untouched.*
   The park record is vault-side and never enters the issue payload; the additive-only
   evolution rule is not engaged.
6. **`_agent/feedback-outbox/` being promoted to a `vault_structure` logical name.**
   *Rejected — already ruled at `vlt-feedback:118-120`.* The park record lives in the decision
   log, which is already a durable agent-zone home; the outbox stays transient.
7. **`vlt-mint:26`'s resume scan reading parked-interim entries.** *Rejected* — see F6's
   out-of-scope note.
8. **A `supersession` note to `factory/inbox/`.** *Not owed* — this build retires nothing
   (disposition 6), so there is no silent survival to record.

## 7. Verification (unit, at rest)

Run all of these before writing the BUILT `status:`; record the named evidence in it.

**V1 — Packaging lint.** `uv run tools/package-lint.py` — Groups **A/B/C/E** must PASS. **D is
skipped** (no `--expect-version`): this is **not** the release build; the dual version bump and
the `--expect-version` gate ride **build-2**. Record the PASS summary line.

**V2 — Handshake bipartite re-check (the ritual, by its check of record).** `decision-log.md`
moved 3 → 4 and its `consumers:` moved 4 → 5, so **Group E** is the check: E1 verifies
`consumers: ↔ depends_on:` in **both** directions, E3 catches a stray pin. Record the Group E
result plus the final `consumers:` line. **Do not record a hand-written `grep "decision-log@"`
as the verification** — it is self-confirming (build-23 shipped Group E to retire exactly this
ritual and the ritual survived it). A grep is a fine editing aid; Group E is the record.

**V3 — Reader probe: the third reconcile leg, over a temp fixture (the gating instrument).**
Build a temp fixture `_agent/mint/decision-log.md` containing **four** entries, then give a
**single agent** the edited `vlt-upgrade/SKILL.md` Step 3.5 + Step 4 and the edited
`decision-log.md`, and ask it to render the Step-4 report block for a run over that fixture.
Fixture entries:

| # | entry | expected |
|---|---|---|
| 1 | `kind: parked-interim`, `ref: conventions/extraction.md`, no superseding entry | **surfaced** in `parked_interims_review:` with its `ref:` and filing reference |
| 2 | `kind: parked-interim`, `ref: partners/example`, **superseded** by entry 4 | **not surfaced** — *negative control; if this appears, the live-entry predicate is wrong* |
| 3 | `kind: deviation`, `ref: conventions/frontmatter.md`, no superseding entry | **not surfaced** in `parked_interims_review:` — `deviation` is outside the scan by design |
| 4 | the superseding entry for #2, carrying `supersedes:` | not itself a park |

**Four pass conditions:** (a) exactly one line in `parked_interims_review:`, and it is entry 1;
(b) the negative control (entry 2) is absent; (c) entry 3 is absent from the new key; (d) a
**second** probe over a fixture log with **zero** parked entries renders
`parked_interims_review: []` — present, not omitted. Record the returned report block verbatim.

**V4 — R4 enumeration audit.** Confirm the new key appears in **all three** places the Step-4
machinery enumerates keys: the schema block (F5 item 1), the composition rule's walk (`:93` —
it walks the block, so confirm the key's position renders in order), and the persist-verify key
set (`:131` — parse a rendered fixture report and confirm the key set matches). Also confirm
the **declared non-widening**: `migrations_run` (`:109`) gains **no** new token, because the
third leg is a leg of `decision-log-reconcile` — a declared exclusion with its reason recorded
(F4), never a silent omission.

**V5 — Single-home grep battery.** Six greps, expectations stated:

| grep | expect |
|---|---|
| `grep -rn "pre-authorized command sequence" skills/` | the **rule** stated once (`decision-log.md`); every other hit is a pointer clause (`vlt-feedback`, `vlt-mint:104`) |
| `grep -rn "parked-interim" skills/` | present in `decision-log.md` (kind enum, definition, §Parked interims, roster, enforcement), `vlt-feedback/SKILL.md`, `vlt-upgrade/SKILL.md` — and **nowhere else** |
| `grep -rn "decision-log@" skills/` | exactly **five** hits, all `@4` (aid only — Group E is the record) |
| `grep -n "parked_interims_review" skills/vlt-upgrade/SKILL.md` | the schema key + the prose paragraph + the third-leg text |
| `grep -c "kind:" skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md` | the enum line and its bullets only — no second enumeration introduced |
| `grep -rn "stage promotions, upgrade-time rulings, retirements" skills/` | **0** — both drifting glosses replaced (F2 item 3, F7) |

**V6 — R3 (legal response for a new finding class).** `parked_interims_review:` is a new
surfaced class. Its one-line legal response is stated at **its own single home** — the Step 3.5
reconcile bullet and the Step-4 key's prose (F4, F5): *surface only; the human re-derives the
unwind and resolves the park as a superseding entry; never auto-resolved, never auto-edited.*
The convention half is stated at `decision-log.md`'s Enforcement section (F2 item 9): the v4
rule is **write-side**, no new `vlt-lint` finding class ships with it. Confirm both are present.

**V7 — R1 / retirement / population.** Confirm the shipped prose carries what the dispositions
promised: the population line is in **both** `vlt-feedback`'s step and the convention's §Parked
interims (disposition 5); no prohibition was removed anywhere (disposition 6 — this build is
**+1 added, 0 retired**, and that is the number Cycle 12's closeout records for P-15's series).

**V8 — Scrub.** No personal or vault-local content in any changed shipped file. Worked examples
use placeholder paths. Note the one thing that looks like a violation and is not:
`_agent/mint/decision-log.md` is a **module-defined fixed agent-zone path**, not a specific
install's artifact path — the same standing as `_agent/feedback-outbox/` at
`vlt-feedback:111`. Any *example* `ref:` or filing reference in shipped prose uses placeholder
form (`conventions/{name}.md`, `<issue URL>`), never a real issue number or a real vault path.

**V9 — Cruft.** `find . -name ".decision-log.md" -not -path "./.git/*"` → **0**. *(Note the
collision the builder must not fumble: the gitignored build artifact `.decision-log.md` — which
must not exist on disk when the build finishes — is a different file from
`_agent/mint/decision-log.md`, the vault's durable log this build writes rules for. Delete the
former; never touch the latter.)*

## 8. Release

**Not the release build.** Build-2 is the cycle's last build and carries the dual version bump
(`.claude-plugin/marketplace.json` `"version"` and `skills/vlt-setup/assets/module.yaml`
`module_version`), the pre-tag `uv run tools/package-lint.py --expect-version 0.16.0` gate, and
the ff-merge → tag → push sequence. This build ships one commit on `cycle12-v0.16.0` and bumps
no version string.

## 9. Acceptance (live)

Six checks — **four ship-verifiable (all gate closeout), two field-contingent (neither gates).**

**(1) `[ship-verifiable]` — GATES closeout.** The handshake is bipartite-consistent after
`decision-log.md` **3 → 4**: `:12` lists **five** consumers
(`[vlt-mint, vlt-upgrade, vlt-lint, vlt-ingest, vlt-feedback]`) and all five ack
`decision-log@4` (`vlt-mint/SKILL.md:3`, `vlt-upgrade/SKILL.md:3`, `vlt-lint/SKILL.md:4`,
`vlt-ingest/SKILL.md:4`, and `vlt-feedback/SKILL.md:3`'s newly-added line), with no stray pin.
**Instrument:** `package-lint` **Group E** (`tools/package-lint.py`, E1/E2/E3) run at rest —
never a hand-written `grep "decision-log@"`, which is self-confirming. **Evidence:** the Group E
PASS line plus the final `consumers:` line, recorded in the BUILT `status:`.

**(2) `[ship-verifiable]` — GATES closeout.** The re-read works and knows what *not* to
surface: over the temp fixture log, the third reconcile leg surfaces **exactly** the one live
`parked-interim` entry, does **not** surface the superseded one (the negative control), does
**not** surface the `deviation` entry, and renders `parked_interims_review: []` — present, not
omitted — over a log with no parks. **Instrument:** the brief's **Verification-3** single-agent
reader probe over the specified four-entry fixture plus the empty-log fixture, factory-side and
at rest, carrying its negative control. **Evidence:** the returned report blocks recorded
verbatim in the BUILT `status:`.

**(3) `[ship-verifiable]` — GATES closeout.** The prohibition ships **attached to an artifact**,
once (A36 + single-home): `decision-log.md:39`'s kind enum contains `parked-interim`; the
convention carries §*Parked interims* as the rule's only statement; `vlt-feedback/SKILL.md`
carries a parking step naming `_agent/mint/decision-log.md`, the three required entry contents
(blocker-as-current-behavior, filing reference, re-derive instruction) and the population line;
`vlt-mint/SKILL.md:104` carries a pointer clause and no restatement; and both drifting
completeness glosses are gone. **Instrument:** the brief's **Verification-5** six-grep battery
plus `package-lint` Groups A/B/C. **Evidence:** the six grep outputs verbatim and the PASS line.

**(4) `[ship-verifiable]` — GATES closeout.** The R4 widening landed whole and its exclusion is
declared, not silent: `parked_interims_review:` is in the Step-4 schema block, renders in key
order under the walk-the-block rule (`vlt-upgrade/SKILL.md:93`), and passes the persist
key-set verify (`:131`) on a rendered fixture report; `migrations_run` (`:109`) gains **no**
token, with the reason recorded at the third leg. **Instrument:** the brief's **Verification-4**
enumeration audit (a parse of the fixture-rendered report's top-level key set against the schema
block). **Evidence:** the parsed key set and the recorded declaration.

**(5) `[field-contingent]` — does not gate.** A real park is recorded through the new step: on
the next `vlt-feedback` filing the vault is parking against, the human accepts the offer and an
entry appears in `_agent/mint/decision-log.md` with `kind: parked-interim`, a `ref:`, the issue
URL, the blocker stated as a claim about **current shipped behavior**, `user-ruled` verdict
provenance with its required *why* — and **no command sequence**. **Event:** a `vlt-feedback`
filing of a blocker the vault is holding an interim against. **Performer:** the owner (the skill
is invoked-only and approval-gated). **Vault:** `{field-vault}` — the only install with the
feedback rail configured and a filing history. **Bound:** Cycle 13's `inbox-capture`. *Stated
honestly: **nothing in this plan schedules a new upstream blocker.** If none occurs by the
bound, this routes to an owner ruling on whether the mechanism is graded on check (2)'s at-rest
evidence alone — **not to a re-carry**. That is A56's lesson applied at brief time rather than
discovered at closeout.*

**(6) `[field-contingent]` — does not gate.** The re-read fires where it matters: the owner's
next `vlt-upgrade` run on a vault holding at least one live `parked-interim` entry renders a
**non-empty** `parked_interims_review:` naming that entry and its filing reference, and — when
that run also carries governance rule changes — says so on the line, beside a non-empty
`governance_rule_changes:`. **Event:** the first `vlt-upgrade` after check (5)'s entry exists.
**Performer:** the owner (standing rule). **Vault:** `{field-vault}`. **Bound:** Cycle 13's
`inbox-capture`. *Dependency stated: this check cannot be graded before (5) discharges — if (5)
routes to an owner ruling, so does this.*

---

## Grounding corrections issued at brief time — build-4 (2026-08-25)

*The superseding notes the Re-ground stage owes the roadmap, so the file does not keep asserting
a stale cite. **The capture and roundtable bodies are append-only and are not rewritten** —
these notes supersede specific cites within them. Three cites had drifted; none contradicted an
ideation ruling, so none blocked.*

**Cite drift (three — the eleventh, twelfth and thirteenth this cycle has logged; the live
instance of out-of-scope item 4, *the loop's line-number cites go stale silently*). All three
are in roundtable amendment A36, and all three are capture/roundtable approximation — no build
this cycle moved these lines.**

| roadmap cite (A36) | at HEAD (`5585877`) | source of the drift |
|---|---|---|
| `vlt-feedback/SKILL.md:19-20` — *"The issue is **transport**, not the record."* | **`:14-16`** (`:18-20` is the field-contract single-home paragraph) | roundtable approximation |
| `vlt-feedback/SKILL.md:112-113` — *"a recovery artifact, **not a record**"* | **`:115-116`** | roundtable approximation |
| `vlt-feedback/SKILL.md:112-113` (same cite, second claim) — *"`_agent/feedback-outbox/` is deliberately **not** a `vault_structure` logical name"* | **`:118-120`** — a **different** paragraph from the one above; A36 cited one range for two separate statements | roundtable approximation |

**Cites re-verified and standing** (recorded because the brief rests on them): `vlt-mint/SKILL.md:104`
(the park fallback) and `:26` (the activation resume scan) are **correct at HEAD**;
`vlt-feedback/SKILL.md:38-42` (invoked-only) is **correct**; `vlt-upgrade/SKILL.md:78` (the
decision-log reconcile) is **correct**; Q7's grounding figures re-measured this session —
`vlt-feedback/SKILL.md` is **7,186 bytes** and
`grep -cin "park\|interim\|exit condition\|blocker"` returns **0**, so *"there is no existing
parking discipline to extend"* holds at HEAD.

**One roadmap grading corrected on grounding — flagged, not acted on.** A46 grades A12-5's
module side **BLOCKED (unreachable) until A33's `governance_rule_changes:` key exists.**
Build-3 shipped that key (`vlt-upgrade/SKILL.md:111`, commit `5585877`, F11), so **the
precondition now exists on this branch and the BLOCKED grading is stale.** Re-grading a platform
item is an owner act; this brief records the fact and changes no scope. See disposition 9.

**Two pre-existing drifts found and folded into scope** (not cite drift — content drift):
`decision-log.md:23` and `vlt-mint/assets/decision-log-template.md:3-4` both gloss the log's
kinds as a six-item list that **omits `deviation`**, which shipped at v3. Adding a seventh kind
would make them two behind, so both become point-at-the-map (disposition 7, F2 item 3, F7).
