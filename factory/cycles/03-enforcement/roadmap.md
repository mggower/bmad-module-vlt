---
title: 'Inbox Evolution Roadmap — Arc 3: the enforcement arc (no boundary without a bell)'
status: 'CLOSED 2026-07-26 — the enforcement arc, shipped in two releases: v0.6.0 (builds 14+15+16+18 @ a117f4f, tagged 2026-07-08) and v0.7.0 (builds 19+20+21+22+23 @ dbcf018, tagged 2026-07-18); build-17 was never built and is FOLDED INTO ARC 5 by owner ruling, so this arc closes with one build unshipped, stated plainly. Acceptance: six discharge passes (2026-07-12 → 2026-07-25) rode the vlt-core 0.6.0/0.7.0 upgrades and their lint cadences and fully discharged builds 14 and 19 plus every ship-verifiable clause; a seventh closeout pass (2026-07-26) rode the v0.8.0 release, graded build-23''s process-adoption clause FAILED (filed) and discharged its Q28 vacuity note, after which the remaining field-contingent checks were closed by an owner-ruled batch — three filed as findings, five released as standing watches, one staged, one dated — recorded in the **Closeout dispositions** block at the head of the Deferred acceptance ledger, the single home for every item''s final disposition (an unchecked box in this ledger no longer means pending). Still open elsewhere: build-20''s inherited FAILED clause and its adoption gap sit on the Arc-4 ledger (fixes shipped as A4-1/A4-2 in v0.8.0, acceptance pending); build-17 + 091003 M0 transfer to Arc 5; six standing watches, three design debts (Q21/Q24/Q27), the vault-side conformance spot-check, the standing 091002 packaging metric, the 2026-08-17 091006 clock and the Arc-2 BMB-drift upstream filing all carry forward — full list in **Carried forward past Arc 3**, which the next `inbox-capture` re-lists. The arc''s own lesson, carried as its highest-value item: this ledger conflated ship-verifiable with field-contingent checks under one checkbox, so closeout had no bound — `build-brief` must tag them at brief time and only ship-verifiable checks may gate `arc-closeout`. **This arc is archived — do not append.**'
module_code: 'vlt'
created: '2026-07-06'
updated: '2026-07-26 (CLOSED — closeout pass: build-23 process-adoption FAILED and filed, Q28 vacuity note written, owner-ruled batch disposition over the remaining field-contingent tails, build-17 folded into Arc 5, carry-forwards recorded, roadmap + briefs archived)'
derives_from:
  - 'inbox/2026-07-06-091001-spec-convention.md'
  - 'inbox/2026-07-06-091002-module-packaging-lint.md'
  - 'inbox/2026-07-06-091003-enforcement-kit-derive-first.md'
  - 'inbox/2026-07-06-091004-no-boundary-without-a-bell.md'
  - 'inbox/2026-07-06-091005-write-verification-attestation.md'
  - 'inbox/2026-07-06-091006-review-after-freshness-key.md'
  - 'inbox/2026-07-11-114226-research-note-graduation-queue.md'
  - 'inbox/2026-07-11-153000-graduation-queue-field-calibration.md'
  - 'inbox/2026-07-12-114837-graduation-queue-sayari-calibration.md'
  - 'inbox/2026-07-12-114910-dev-zone-contract-graduation.md'
  - 'inbox/2026-07-12-114940-sayari-060-upgrade-field-evidence.md'
  - 'inbox/2026-07-13-092341-spec-convention-has-no-advocate.md'
  - 'inbox/2026-07-16-153000-new-partner-fields-one-lens.md'
  - 'inbox/2026-07-17-090000-extraction-grant-authorizes-nobody.md'
  - 'inbox/2026-07-17-090500-upgrade-rulings-never-reach-the-decision-log.md'
  - 'inbox/2026-07-17-091000-vlt-mint-step4-registers-local-mints-into-shipped-artifacts.md'
  - 'inbox/2026-07-17-100000-loop-profile-drift-predates-build-11.md'
  - 'inbox/2026-07-18-115913-chess-coach-persona-line-seeds-fabricated-time.md'
  - 'inbox/2026-07-25-132141-partner-consult-synchronous-channel.md'
  - 'inbox/2026-07-25-144500-revisit-after-has-no-adoption-path.md'
  - 'inbox/2026-07-25-160239-contradictions-have-no-drain.md'
  - 'inbox/2026-07-25-160949-auto-caption-name-substitution.md'
  - 'inbox/2026-07-25-162416-linkage-ripe-cannot-see-graduation.md'
predecessor: 'skills/reports/archive/inbox-evolution-arc2-roadmap.md (Arc 2 — CLOSED, builds #12–#13 shipped v0.5.0)'
intent: >
  Capture the six-filing batch produced by vlt-core's 2026-07-06 headless vault-evolution
  run (gap analysis → brainstorm → six parallel CIS pressure-tests → synthesis, vault
  commit ef2cce6), grounded against module source at v0.5.0 (commit 6f21952). All six
  filings trace to one root cause the run's Five-Whys converged on — vault state lives in
  prose, so nothing can count, trigger, or trip — and together they form the module's
  enforcement layer: a doctrine, its substrate, two schema surfaces, one contract
  convention, and the factory's own instance of the same fix. This doc is the durable
  cache; it spawns per-build briefs the way Arc 1/2's roadmaps did.
---

# Inbox Evolution Roadmap — Arc 3

## The through-line (why these twenty-three filings are one story)

> **Reading order.** The arc opened with six filings (091001–091006) attacking
> *defined-but-unenforced*. Capture run 2 (2026-07-17) folded in eleven more, and they do
> **not** extend that theme — they invert it. Capture run 3 (2026-07-25) folded in six more,
> and they turn the lens a third time. Part 1 below is the original six-filing
> through-line, preserved as written. **Part 2 is the arc's revised spine** and is where a
> reader should start: the enforcement layer shipped, and what the field then reported is
> that *the module cannot see itself*. Read Part 2 before ideating anything in A3-7..A3-17.
> **Part 3 is the run-3 spine** — read it before ideating A3-18..A3-23; it is where the arc's
> shipped bells get measured against live vault populations for the first time, and where
> the arc's own remedy for the silent-zero class is found un-adopted.

### Part 1 — the original six (as captured 2026-07-06, preserved)

Arc 1 built the machinery; Arc 2 hardened it against first field contact. Arc 3 is the
vault turning that machinery on **itself**: the 2026-07-06 vault-evolution run traced four
separate live failures (the firewall's 4-day checkable-but-unchecked gap, lint cadence
with no forcing function, dispatch deferrals with no bite condition, staleness markers
specified but never applied) — plus every packaging defect shipped since 0.3.0 — to a
single failure shape, **defined-but-unenforced**, and filed one coordinated batch that
attacks it at every layer:

- **091004** is the *doctrine*: no boundary-creating mint without a declared enforcement
  stage or a tripwired, expiring deferral.
- **091003** is the *substrate*: derived vitals + a tripwire registry + a SessionStart
  moment + a ledger surface — with a design invariant (derive-don't-store; no mutable
  counters, ever) recorded for all future enforcement work.
- **091005** and **091006** are the *schema surfaces*: write-time attestation
  (`verified_by`/`verified`) and the freshness key (`review_after`) — both landing on
  `frontmatter.md`, both feeding lint and the vitals reader.
- **091001** is the doctrine applied to a *contract class before it forks*: the spec
  convention, ships with its own (declared-stage) bell.
- **091002** is the *factory-side worked instance*: the release boundary here has no bell
  either, and every tag since 0.3.0 proves it.

Three coordination facts bind the batch harder than thematic kinship: (1) filings
091004 + 091005 + 091006 all land on `frontmatter.md` and must ship as **one coordinated
`frontmatter@3` bump** — one version bump, one consumer walk, or the handshake churns
three times with conflicting key semantics; (2) `review_after:` appears in two filings
(091006's page freshness, 091004's deferral expiry) and must be defined **once**;
(3) two hard sequencing gates exist — the spec convention before the next partner mint
(the third consumer is the fork point), and the packaging lint before the 0.6.0 tag.

Filing-status caveat, carried honestly: **091003, 091005, and 091006 are design-stage
filings**, filed at the owner's request ahead of their plans' measurement milestones. The
schemas and rejected-alternative analyses are final; the field evidence (counter-accuracy
audit, two measured lint cycles, first review-cycle data) follows from vlt-core. 091001,
091002, and 091004 are unconditionally ripe.

### Part 2 — the revised spine (capture run 2, 2026-07-17): the module cannot see itself

Arc 3's first six filings said *the vault's state lives in prose, so nothing can count,
trigger, or trip*. v0.6.0 shipped the answer. The eleven filings that followed report what
the enforcement layer met on contact — and the pattern is **not** more unenforced rules.
It is that **the module's checks verify the shape of a declaration, never its content**,
so the module's own self-descriptions rot without anything noticing. Every headline
finding in this run is an instance:

- **Acks verify pins, never content.** `vlt-research/SKILL.md:3` acks `frontmatter@3`
  while `:65` emits `topic:` as a scalar against `frontmatter.md:131`. The handshake was
  bipartite-consistent the whole time. Nothing in the module can catch this class (A3-7).
- **Prose asserts facts about the shipped surface, and nothing re-reads it.**
  `extraction.md:47` + `:121` say "no skill shipped with the module uses it" — false since
  v0.4.0, falsified by the same commit (`299e70b`) that shipped the check depending on it,
  which passed every gate because adding a consumer correctly doesn't bump `version:`
  (A3-14).
- **Verification greps search for the ack, not the consumption.** Build-15 proved
  `spec@1`'s consumer list complete by grepping `spec@` — self-confirming, and it missed
  `vlt-upgrade:75`, which recites the convention with no `depends_on:` at all (A3-12).
- **Acceptance discharges against substitutes.** Build-11's check #1 named dog-trainer and
  health-coach; it was discharged by wearers minted *after* the drift it was meant to
  catch. The check "passed" on a non-adopting population (A3-17) — and the same shape
  plausibly explains build-15's dry spec tail.
- **Completeness lists drift, exactly as the standing rule says.** The contract's
  hand-transcribed structure map (`vault-operating-contract.md:29-44`) lacks the `specs`
  row its own `:227` uses, against an SSoT (`module.yaml:41-43`) that declares itself
  never-hand-transcribed (A3-10).
- **Instructions outlive the model they were written for.** `vlt-mint:152` tells every
  mint to register into the shipped manifest — and a mint that obeys writes itself into
  the very `agents[]` that `vlt-upgrade:33` uses to tell local from shipped, voiding its
  own B2 restore (A3-16).

Three of the eleven filings had their **central claim overturned** by grounding
(A3-12 origination, A3-14 the naming ceremony, A3-17 the pre-dating title) — a rate that
is itself the arc's evidence. Each filing reasoned carefully from what the module *says*
about itself, and the module said something untrue. That is the same failure the six
original filings named, moved up one level: **not "the rule has no bell" but "the rule's
own description of reality has no bell."**

The practical consequence for this arc: **the enforcement kit (build-17) is not obviously
the right home for most of this**. Build-17's design derives metrics from *event records*
(log headers, dispatch rows). The findings above are absences and contradictions —
there is no event to count. Several are one-line prose corrections; the cheapest and
highest-value item in the whole arc (`vlt-research:65`, one word) needs no enforcement at
all. Ideation should resist routing this batch to build-17 by default.

### Part 3 — the run-3 spine (capture run 2026-07-25): the bells ring, and the report reads clean either way

Run 2 said *the module cannot see itself*. v0.7.0 shipped the answer — `linkage_ripe`,
`revisit_due`, `spec_candidate`, the boundary classifier, the adoption facet. Run 3 is the
first time those bells met a **mature live population** (vlt-core at 130 wiki pages / 96–98
research notes, swept end-to-end by the 2026-07-25 full lint). The verdict is not that the
bells are absent. It is that **every one of them reports a number a human cannot read as
signal** — and the failure comes in two mirror-image forms:

- **Silent zero** — a detector whose absence-branch is silence, so *non-adoption renders as
  health*. `revisit_after:` is 0-of-96 on vlt-core and produces a permanently clean
  `revisit_due` report (A3-19).
- **Noise storm** — a detector whose hit-branch is undifferentiated, so *a working detector
  renders as a broken one*. `linkage_ripe` returned 41 hits, 0 real, ~100% FP — worse than
  the ~69–79% naive baseline the union exists to beat (A3-23).
- **Terminal success** — a bucket that only grows and is labelled a feature, so *deferral
  renders as a managed disagreement*. `contradictions_handled: 63` on the same sweep, with
  the identical defect class (an auto-caption name substitution) sitting on **both** sides of
  the handled/unhandled line, decided only by whether someone wrote a sentence (A3-20).

That is one class in three costumes: **a report line whose value is the same whether the
mechanism worked or nobody used it.** The arc already named this class — `spec.md`'s
`deferral_metric` (A3-12, build-19) — and already shipped its general remedy: build-20's
`adoption_first_instance:` facet. **Grounding's sharpest finding this run is that the remedy
is itself un-adopted:** `adoption_first_instance:` is declared at `frontmatter.md:237`/`:242`
and carried by **zero of the seven shipped conventions**, including the very `spec.md` its
own prose names as the motivating example. The arc's answer to shipped-but-unexercised is
shipped and unexercised. Ideation should treat *wiring the facet* as a candidate in its own
right, not as a sub-clause of any single key's fix.

Two of the six filings sit outside that spine and should not be forced into it:

- **A3-21** (auto-caption name substitution) is an **ingest-side source-fidelity** gap, not a
  reporting gap — it is the *cause* of one contradiction A3-20 cites, and the two filings
  deliberately claim it for different defects. Read them together; brief them apart.
- **A3-22** (partner→partner consult) is the run's only **candidate**, not a defect — the
  missing synchronous half of `vlt-dispatch`. It carries the run's most arc-idiomatic idea:
  pairing the mechanism with a handshaked `consult.md` convention + a lint check, so the
  channel is *exercised by construction* rather than shipped-and-dark. That is a direct
  answer to the scar Part 3 just named.

And **A3-18** is the run's overturned filing: the fabricated-time seed it reports is
vault-local mint prose, present in no module file. Its module-side residue is one honest
question for ideation — whether `vlt-mint`'s persona-authoring beat should warn that
concrete temporal color inside a *figure of speech* is a fabrication seed, since the shipped
anti-fabrication rules all target faked *continuity*, never invented *specifics*.

---

## Capture — all six filings (grounded against module source 2026-07-06, v0.5.0 @ 6f21952)

Capture-run notes: owner confirmed all six filings in scope, none deferred. Grounding ran
as six parallel source-verification passes, one per filing; every `file:line` below was
re-derived from current source, not taken from the filings. Headline result: **no claim
was SUPERSEDED anywhere** — greps for `spec.md`/`{specs}`, `tripwire|vitals|health-strip`,
`enforcement_stage|deferral_metric`, `verified_by|attestation`, `review_after`, and any
packaging-lint artifact all return zero hits in `skills/` — the entire batch is
greenfield. A small number of provenance corrections are recorded per filing.

### A3-1. The spec convention (2026-07-06) — `…091001-spec-convention.md`

**Context.** A council flag carried through two partner mints ("give 'the spec' a named
convention home BEFORE a third consumer appears") now has a live fork risk: a second
proto-spec exists vault-side (the Creative→Chef meal-plan format). vlt-core is minting the
convention locally as the blocking pre-step to its next partner mint; this filing is the
module-side half. Design source: a scored pressure-test (29/30) with rejected alternatives
already documented (auto-notify ruled architecturally impossible → push-MUST + pull-SHOULD;
registry file, overlay-only, spec-as-wiki-note, defer-until-n=3, lint-in-v1 all rejected
with reasons — don't re-litigate).

**Grounding: ✅ accurate to build essentially as-specified; everything greenfield.**

- **No `spec.md` exists** in `skills/vlt-setup/assets/governance/_meta/conventions/`
  (current set: frontmatter, wiki-index, wiki-supersession, wiki-consolidation,
  extraction) — GAP CONFIRMED; change 1 lands cleanly.
- **The handshake precedent is real and reinforcing**: `wiki-supersession.md:11-12`
  carries `version: 1` / `consumers: [vlt-ingest, vlt-lint, vlt-extract, vlt-track]` —
  convention-consumers are *skills*, which is exactly the "two `consumers:` semantics"
  disambiguation the new convention must own (spec-artifact consumers are *partners*).
- **All insertion points verified exact**: setup §2 enumeration `vlt-setup/SKILL.md:143`
  (baseline stash at `:146` loops over shipped conventions — covers spec.md
  automatically); `module.yaml:44-58` `vault_structure` default map (declared SSoT at
  `:41-43`; no `specs:` row — nor `tripwires:`/`bases:`, the siblings' rows); the
  illustrative path table is `vlt-setup/SKILL.md:55-70` (filing said ~57-69 — tail is
  `:70`); all five vlt-dispatch touch points (`skills/vlt-dispatch/SKILL.md:39`, `:152`,
  `:158`, `:176`, worked example hardcoding `_agent/handoffs/2026-06-13-…` at `:193`);
  vlt-mint Step 3 per-kind blocks from `:101`, *Mint a new partner* `:116`, *Edit a
  convention* `:124-134`; contract "two handoff timings" at
  `vault-operating-contract.md:223` (section starts `:208`).
- **CONFIRMED: neither vlt-dispatch nor vlt-mint has any `depends_on:` block today**
  (both frontmatters are `:1-4`, name + description only) — the filing's "adds the block"
  phrasing is right. vlt-lint is the exception: a future `spec@1` ack *appends* to its
  existing list at `vlt-lint/SKILL.md:4`.
- **⚠️ One adjustment the filing doesn't flag (change 6, the lint follow-on):**
  `spec_notification_missing` reads `_agent/dispatch.md`, but that record has **no logical
  path name** — `vlt-dispatch/SKILL.md:35-38` explicitly lists it among locations "not in
  the structure map" (hardcoded, agent-zone), and vlt-lint currently references dispatch.md
  nowhere. The check therefore introduces a new hardcoded-path read into lint. Either
  accept it (consistent with dispatch's own treatment) or add a `dispatch:` logical name
  first — decide at ideation, before the check lands anywhere.
- vlt-upgrade's migration host is real: the human-gated proto-spec retrofit offer lands in
  **Step 3, item 5 (Migrations)** at `vlt-upgrade/SKILL.md:67-70` (the filing's "Step 3.5"
  is a labeling nicety, not a distinct step), reported via `migrations_run:` (`:88`).
- Dispatch already uses "spec" informally throughout (`:162`, `:176`, `:193`) — untyped
  overloading, not a competing convention; the class-definition boundary in change 1 is
  what disambiguates it.

**Three latent bugs carried** (all generalizable): file moves vs parallel worktrees (stub
the old path, never touch worktree copies); shipped-skill worked examples coupled to live
vault artifact paths (`vlt-dispatch/SKILL.md:193` — use placeholder paths); relay
idempotency resets across a file move (migration offer should re-point open pointers).

**Hard sequencing:** before the next partner mint. Adopts 091004's enforcement/bell
frontmatter block when both land (v1 ships with an honest declared-stage bell + lint
deferral carrying a `review_after`). Its schema is the pattern donor for 091003's
`tripwires.yaml` format.

**Open design questions (carry, don't resolve):** (1) carried-flag scheduling — should
vlt-mint's Phase 2 gate check open decision-log flags whose trigger the current mint would
fire; cheaper variant: seed carried flags as tripwires in 091003's registry; (2) does the
class generalize to "contracts" — ruling from the pressure-test: do NOT pre-generalize,
test against a real second instance first; (3) where does notification-drift enforcement
live (lint Step-2 check vs dispatch ledger computed line vs enforcement-kit counters) —
pick one home before any lands twice; (4) pre-agreed escalation: a spec version bump
shipping without relay entries promotes the lint/ledger enforcement to "next mint."

### A3-2. Pre-tag packaging lint (2026-07-06) — `…091002-module-packaging-lint.md`

**Context.** Every tag 0.3.0→0.5.0 shipped a known packaging defect class, each caught
downstream by vlt-core's `vlt-upgrade` and hand-fixed at the cost of a full lifecycle
round-trip. The release boundary has no bell — this is the factory-side instance of
091004's doctrine. Unusually, **everything lives in this repo; nothing ships to vaults.**
Hard gate: script + negative tests green + CLAUDE.md wired **before the 0.6.0 tag**.

**Grounding: ✅ fully confirmed, zero provenance corrections — every citation re-derived
exactly.**

- **No mechanical release check of any kind exists**: no `tools/`, no `.github/`, no
  active git hooks, no lint script. GAP CONFIRMED.
- **CLAUDE.md citations exact**: lifecycle step 6 `:29-32`; CSV standing rule `:53-56`;
  no-`.decision-log.md` rule `:59-61` (itself the "two ship surfaces" evidence — the
  own-the-apply is a filesystem copy); Git & publishing at `:67-73`, with the
  release-surface enumeration to amend specifically at **`CLAUDE.md:71`**.
- **merge-help-csv.py symbols exact** (`skills/vlt-setup/scripts/merge-help-csv.py`):
  `HEADER` lines 38-52, `LEGACY_HEADER` line 58, `canonicalize_header` line 61, PEP 723
  block with `dependencies = []` at line 4. The filing's own grounding correction (bind
  the lint to the *symbol*, not build-13's stale `:36-37` cite — those lines are the
  comment) is itself CONFIRMED. Note: three other `merge-help-csv.py` copies exist under
  `.claude/skills/bmad-*` — upstream's, out of scope; the lint must bind to the
  `skills/vlt-setup/scripts/` one.
- **Both live defects are on disk right now**:
  `skills/vlt-setup/scripts/__pycache__/merge-help-csv.cpython-312.pyc` (the class-A hit
  under the shipped surface — group A fires today, as claimed), and
  `vlt-upgrade/SKILL.md:45` mandates excluding only `.decision-log.md` — the wider
  field-practice list (`__pycache__`, `*.pyc`, `reports/`, `.DS_Store`) exists only in
  vlt-core's upgrade-ledger. Latent bug 1's one-line vlt-upgrade fix is the filing's only
  vault-facing edit; it can ride along.
- **Group C targets verified**: `module.yaml:4` `module_version: 0.5.0`;
  `marketplace.json:16` `plugins[0].version: "0.5.0"` (nested, not top-level; exactly one
  plugin entry — assert that before indexing, as the filing warns). The two strings
  currently agree. Governance bundle home exists and is non-empty.
- **Grounding additions for open questions**: (Q2, group-A root scope) live instances
  exist outside the shipped surface today — `./.DS_Store` at repo root and
  `./docs/.DS_Store` — so a `skills/`+`.claude-plugin/`-only scope demonstrably misses
  real cruft; cheap to include the root. (Q3) `marketplace.json` `skills[]` (14 entries,
  lines 21-35) currently matches the 14 `skills/vlt-*` dirs one-to-one — the drift class
  is latent, not active.

**Two owner rulings the filing carries (resolve at ideation, not here):**
(1) `tools/` tracked vs gitignored — plan recommends tracked+public (the enforcement tool
*is* documentation of the release contract), at the cost of the one-line `CLAUDE.md:71`
amendment; (2) arc placement/build numbering — opening build of Arc 3 vs standalone
maintenance build; the only hard gate is green-before-tag.

**Open design questions (carry):** YAML dependency posture (PEP 723 + pyyaml via `uv run`,
recommended, vs stdlib line-scrape); group-A root scope (see live evidence above);
`skills[]`↔dirs cross-check as group C's fifth assertion vs slice-3 material; retroactive
doctrine registration as the factory boundary's `checked_by` once 091004 lands.

### A3-3. The enforcement kit, derive-first (2026-07-06) — `…091003-enforcement-kit-derive-first.md`

**Context.** The substrate: vitals (derived, never stored) + `_agent/tripwires.yaml` +
a SessionStart health strip + a computed "Tripped wires" section in `vlt-dispatch ledger`.
Design-stage filing (filed ahead of its plan's slice-5 evidence at owner request): spec
firm, vault-side measurement numbers pending. Carries the arc's **design invariant,
recorded for all enforcement work: no mutable stored counters — derived or append-only
state only** (the stored-counters alternative was killed as a recursion trap: the
increment obligation is itself prose-enforced, and a skipped increment reads false-healthy;
plus it's a universal merge-conflict point across parallel sessions). Rider: an optional
`blocked_on: user-decision | partner-bandwidth | external-event` facet for backlog/dispatch
triage.

**Grounding: ✅ confirmed with one real provenance correction.**

- **vlt-lint claims all exact**: description "proactively after several ingestions"
  (`vlt-lint/SKILL.md:3` — aspirational, nothing counts); Step 0 last-lint grep `:27` and
  `find -newermt` mtime scoping `:32`; Step 6 writes the lint log entry `:132-138` (the
  counter reset by derivation). Latent bug 1 (two "since last lint" definitions — op-debt
  from log headers vs file-scope from mtime — can disagree) is grounded in source: `:27`
  vs `:32` genuinely differ; change 6 must pin one definition per consumer.
- **⚠️ PROVENANCE CORRECTION (change 4):** the contract *already has* a "Canonical format"
  section with the strict grammar **verbatim** —
  `vault-operating-contract.md:115-119`: `## [YYYY-MM-DD HH:MM] <type> (<partner>) |
  <summary> [→ <artifacts>]`, and `:113` already says "vlt-lint scopes off it… Keep it
  parseable." Change 4 is a **tighten-and-relabel, not a new section**. What's genuinely
  new: the partner paren is currently *optional* (`:122` "Omit only for a partner-less
  generic-agent operation") — making it mandatory for partner-run ops is a real behavioral
  edit; the case-insensitive/paren-tolerant parser mandate and the keep-the-shape rule for
  new types are absent.
- **All the gaps are real**: no `tripwires:` row in `module.yaml:44-58`; vlt-setup
  installs no hooks and never touches `settings.json` (no such string anywhere in its
  SKILL); `assets/hooks/` doesn't exist (latent bug 3 — the moment is currently
  unprovisionable module-side); the workflows force-reinstall precedent change 3 leans on
  is real (`vlt-setup/SKILL.md:148-160`, "overwrite them on every install/update" `:158`).
- **Dispatch surface verified**: `ledger` mode is read-only grep+group at
  `vlt-dispatch/SKILL.md:199-213` (Tripped-wires section inserts ~after `:211`); "writes
  no `{log}` entry" confirmed verbatim `:237`; Verify block extension point `:255-256`.
- **Op-side rule hosts verified**: mint Step 2 blast-radius gate `vlt-mint/SKILL.md:71-73`
  and Step 2a council capture `:86-88`; council landing zone
  `vlt-review-council/SKILL.md:44-46`. No deferral-registers-a-wire rule exists anywhere —
  net-new.
- **Rider grounded**: backlog schema single-home confirmed (`frontmatter.md:169-190`,
  corroborated by contract `:151` "defined once in frontmatter.md"); entry tuple at
  `frontmatter.md:177` has no `blocked_on` facet; dispatch pointer-line carrier format at
  `vlt-dispatch/SKILL.md:100/:108/:184`.
- vlt-ingest confirmed untouched by slices 0-3 (nothing in it counts anything).
- Vault-side evidence numbers (175/184 grammar conformance, the 4-pointer board, the
  six-week-old pointer) are vault-local probes — re-verify in vlt-core before the M0
  audit closes.

**Open design questions (carry — two are cross-filing, decide once):** (1) **where does
module-owned executable code live in an installed vault?** Proposed `{root}/.claude/hooks/`
beside the workflows precedent; 091005 and 091002 may also ship scripts — decide once;
(2) **one metric vocabulary or two** — proposal: `tripwires.yaml` `metric` ids are
canonical and 091004's `enforcement_counter:` must reference an existing id, never coin
its own; (3) is `days_since_lint` a third seed wire or display-only (recommend
display-only until a time-based failure is observed — alert-fatigue budget is a hard
constraint, one strip line); (4) `blocked_on` shape — inline greppable facet (proposed) vs
frontmatter; should `external-event` require a companion date (dovetails with
`review_after`).

### A3-4. No boundary without a bell (2026-07-06) — `…091004-no-boundary-without-a-bell.md`

**Context.** The doctrine: every boundary-creating mint declares its enforcement stage
(`declared | checked | enforced`, with owner + moment + optional counter) or carries a
complete tripwired deferral (metric + threshold + `review_after`, all three required).
Declaration-first won the decision matrix over checks-as-payload-now (couples the doctrine
to its most expensive component) and substrate-first (leaves the next mint unprotected);
a Warden partner and a weekly bell-review ritual were also rejected. Checks-as-payload is
deferred behind the doctrine's own first self-application (`review_after: 2026-08-17`).
Success test: next boundary-creating mint has days-to-first-check = 0 (firewall baseline: 4).

**Grounding: ✅ everything confirmed exactly; no provenance corrections; entirely unbuilt.**

- **Schema target verified**: `frontmatter.md:11-12` — `version: 2`, `consumers:
  [vlt-ingest, vlt-lint]`; YAML rule 3 "No nested properties" at `frontmatter.md:29`,
  exact number and wording — the filing's flat-keys correction of its own pressure-test
  (latent bug 1) is properly grounded. Both proposed new consumers (vlt-mint,
  vlt-research) are real installed skills.
- **The backfill picture is exact, with one sharpening**: all five stock conventions carry
  `version:`/`consumers:`; vlt-lint has a mechanical finding for four — frontmatter drift
  (`vlt-lint/SKILL.md:62`), index drift (`:61`), unmarked supersessions (`:58`), the
  extraction firewall (`:68`). `wiki-consolidation.md` is confirmed the `declared` holdout:
  lint only finds near-duplicates (`:59`) and explicitly hands resolution to ingest
  (`:91` "lint finds, ingest resolves") — **and note its `consumers:` is `[vlt-ingest]`
  only; vlt-lint isn't even a listed consumer**, so its backfill stamp needs the tripwired
  deferral the filing prescribes.
- **Honesty note grounded**: `checked_by: vlt-lint, moment: lint run` stamps a moment
  nobody currently owns — 091003's lint-debt wire is what makes that moment real; until it
  lands, `checked` is the ceiling.
- **Templates + mint + council + lint all verified as net-new insertion points**: the
  three mint templates exist, none carries any Enforcement section; mint Phase 1
  kind-determination `vlt-mint/SKILL.md:31-52`, Edit-a-convention ceremony `:124-134`
  (stamps ride the existing base-edit + handshake), Phase 2→3 exit gate `:95`;
  `vlt-review-council.js` has `mode: 'mint'` (`:74`), `KIND_PANEL` (`:54-70`), lens briefs
  via `lensPrompt` (`:126-132` — the standing-question injection point; no per-kind
  question exists today), moderator verdict enum (`:114`, `:161-163`); personas are the
  five generic ones. Lint's `flag_for_human` block at `:109-120` hosts the four new keys.
- **Latent bug 3 confirmed verbatim** at `vlt-lint/SKILL.md:63`: the coherence check reads
  "For each `{conventions}/*.md` **carrying** a `version:` and `consumers:`…" — a
  convention minted without those fields escapes the machinery entirely. The meta-check
  must flag their absence, not only stale acks.
- **Latent bug 2 confirmed**: vlt-upgrade's Step 1 snapshot (`vlt-upgrade/SKILL.md:29-40`)
  covers minted partners, overlays, base divergence, mint history, capabilities, and
  governance edits — but **no shipped skill assets**; Step 2 (`:44`) "Refresh shipped
  files only" overwrites them with no baseline or flag. vlt-core's planned local template
  edits would be silently clobbered exactly as claimed. Worth its own fix.
- Current pins for the consumer walk: vlt-lint `:4` and vlt-ingest `:4` both at
  `frontmatter@2`; vlt-mint has no `depends_on` (its four "depends_on" grep hits are
  handshake prose, not frontmatter).

**Packaging (binding for ideation):** ONE coordinated `frontmatter@3` bump across
091004 + 091005 + 091006 — one version bump, one consumer walk, keys designed together.
Target the 0.6.0 release, which 091002 gates.

**Open design questions (carry):** (1) is `enforcement_stage` module-generic or
vault-local (recommend generic — a vault-local check promotes via base edit, correctly
surfacing as upstream-bound divergence); (2) v1 scope — conventions + mint classifier
only, or also family contracts and the operating contract's own rules (recommend
conventions-first); (3) do overlay-addition boundaries carry their declaration in the
overlay's own frontmatter (recommend yes; needs a sentence in the mint ceremony);
(4) lens placement — workflow mint-mode rubric line (recommended; KIND_PANEL single-home
precedent) vs persona file; (5) does spec.md adopt the bell keys in its v1 or its first
bump.

### A3-5. Write-verification attestation (2026-07-06) — `…091005-write-verification-attestation.md`

**Context.** Harden, don't add: the three write ops already end in Verify checklists —
the gap is that verification leaves no machine-readable trace, so lint re-checks
everything every sweep and nothing distinguishes an artifact that went through the op
from one that bypassed it (the Wispr deviation was caught by self-declared honesty, not
mechanism). Fix: refactor the existing Verify steps to execute a shared, versioned tier-1
checklist (new convention `write-verification.md`) and write `verified_by:` + `verified:`
into the artifact's frontmatter — simultaneously lint's re-scoping telemetry and the
bypass detector (absence on a file claiming vault provenance is the finding). Tier split
has a mechanical membership test (one-file-checkable → tier-1; corpus-knowledge → tier-2)
plus a promotion path. Threat model stated honestly: defends against bypass, not deception
(mitigated by 1-in-5 sample audit). Design-stage filing; two-cycle measurement data
follows at M4.

**Grounding: ✅ every claim verified; no provenance corrections; net-new throughout.**

- **The three Verify steps exist and do cover ~the same tier-1 set**: `vlt-ingest`
  Step 9 (`SKILL.md:148-156`), `vlt-extract` Step 8 (`:106-114`), `vlt-research` Phase 5
  (`:80-88`) — all three check frontmatter completeness + no `key:`, wikilink resolution,
  source coverage; ingest+extract also verify the log entry. The "unify, don't restate"
  refactor is well-founded.
- **depends_on ground truth for the consumer walk**: vlt-ingest `:4`
  `["frontmatter@2", "wiki-index@2", "wiki-consolidation@1", "wiki-supersession@1"]`;
  vlt-extract `:4` `["extraction@2", "wiki-supersession@1"]`; **vlt-research has no
  `depends_on` key at all** (frontmatter `:1-4` is name+description) — latent bug 1
  confirmed; vlt-lint `:4` as recorded under A3-4.
- **Latent bug 1 fully grounded**: `frontmatter.md:12` `consumers:` omits vlt-research
  (grounding note: it omits vlt-extract too), yet vlt-research writes `type: research`
  frontmatter defined by that convention (template `vlt-research/SKILL.md:57-69`; the
  type is canonical per `frontmatter.md:65` and `:107`). Invisible to the coherence check
  in both directions — the exact defined-but-unenforced shape this arc attacks. Fix rides
  the frontmatter@3 consumer walk.
- **Lint sub-claims all confirmed**: no tier split exists (Step 2 `:51-69` is one flat
  list); scoped mode is mtime-blind to provenance (`:32`, `:55` — latent bug 2); Step 3
  auto-fixes bump `last_updated` (`:73`) — open question 3's re-staling hazard is real;
  `flag_for_human` block `:109-120` lacks the three proposed keys.
- **Workflow + rollout machinery confirmed**: `vlt-lint-full.js` PAGE_SCAN carries
  `topic_is_list` (`:63`, `:73`), reducer at `:130` emitting `flag_for_human` `:247`, no
  attestation fields; the ack-covers-workflow-assets rule is verbatim at
  `vlt-lint/SKILL.md:63` — so the self-enforcing rollout claim (register four consumers,
  the existing coherence check polices partial rollout) holds with zero new machinery.
- **Both collision surfaces for open question 1 confirmed**: `trust:` ladder with a
  `verified` rung at `frontmatter.md:44`/`:62` (same word, different axis vs the
  `verified:` date key); the MHC scope predicate's `author: agent|hybrid` (`:43`,
  `:50-54`) and `type:` values (`:65`) all exist as relied upon.

**Open design questions (carry):** (1) `verified:` vs `verified_at:` naming (the
trust-rung collision — one-shot schema choice, decide before v1); (2) schema home — field
definitions in `frontmatter.md` v3 with checklist/contract in `write-verification.md`
(the joint-overlay discipline argues for this) vs everything in write-verification;
(3) is lint a legitimate attester (`verified_by: vlt-lint` after its own tier-1 pass on a
file its auto-fix touched — otherwise Step 3 re-stales what it just validated);
(4) sample-audit rate (1-in-5 is a guess, tune after cycle 1); (5) encode
"write ops verify and attest own output" as a family invariant now or after M4 (would
exercise build-7's shipped-but-unexercised family machinery).

### A3-6. The `review_after:` freshness key (2026-07-06) — `…091006-review-after-freshness-key.md`

**Context.** Two independently-flagged gaps (no queryable accession view; no freshness
mechanism — the schema conflates edit recency with content validity) collapsed under
pressure-testing into **one optional frontmatter key**: `review_after: YYYY-MM-DD`,
resolved date never a duration, absence = evergreen (so 100+ legacy pages generate zero
noise and backfill is a non-event by construction). The accession register needs no schema
at all — it's a pure Obsidian Base projection over fields every page already carries
(`ingested_from` was dropped as duplicating `sources:`; trust-decay rejected as
axis-conflation — trust is human-review, freshness is world-change). An owner ruling
already recorded in the filing supersedes its original packaging: views fold into
vlt-core's vault-grown `wiki.base`, **the module ships no `.base` file** — schema + skill
lines only, views as documented reference. Design-stage filing; first review-cycle
evidence follows. This is also the first full round trip of the
local-overlay→upstream rail, so it doubles as a test of that machinery.

**Grounding: ✅ confirmed throughout, one provenance correction.**

- **All four ship-sites verified**: `frontmatter.md` wiki schema block (heading `:67`,
  YAML block `:71-80` — and `:48` is the exact conflation line: `last_updated` is "the
  field vlt-lint reads to judge staleness"); vlt-ingest Step 6 frontmatter block
  (`:107-124`) + Step 9 checklist (`:148-156`), `depends_on` at `:4`; vlt-lint stale-claims
  inference at `:55` (`last_updated` + mtime cross-check — what a self-announcing
  `review_after` obviates) and `[!stale]` handling at `:56`, `flag_for_human` `:109-120`
  with no `review_due:` key; `vlt-lint-full.js` schema `:62-83` carries `last_updated`
  (`:68`) and `stale_unmarked` (`:78`), no `review_after`.
- **⚠️ PROVENANCE CORRECTION (latent bug 1's sweep list)**: the live overlay-blind
  consumers are **vlt-ingest and vlt-extract** — ingest's activation (`:26`) reads
  conventions without ever naming `{overlays}` (its path list `:22` doesn't even resolve
  the name), extract likewise (`:19`, `:21`). **vlt-research is a non-consumer** of
  frontmatter.md (not in `consumers:`, reads no convention at activation) — it has no
  overlay to be blind to *today*; folding it into the fix is harmless but only becomes
  meaningful when 091005 makes it a consumer. vlt-lint is partially blind: it JIT-reads
  `{conventions}/frontmatter.md` (`:17`) without pairing the overlay, though it does
  resolve and read overlays for governance checks.
- **Latent bug 2 confirmed**: vlt-upgrade Step 3.3 (`:64`) preserves overlays verbatim
  ("were never touched — confirm they are intact") with **no subsumption/retirement
  pass**; the only overlay-adjacent migration (Step 3 item 5, `:69`) is overlay-*lift* —
  the reverse direction. And lint's `overlay_not_append_only` (`vlt-lint/SKILL.md:65`)
  fires only on **verbatim** heading duplication, so a subsumed-but-reworded overlay
  section shadows silently. The proposed overlay-subsumption pass in vlt-upgrade is the
  missing half of the local-prototype→upstream rail — without it every future upstreamed
  overlay leaves a shadow.
- **Latent bug 3 confirmed**: `depends_on` pins are flat base-only `name@version` scalars
  (validated as such by the coherence check `:63`) — no overlay axis. Likely acceptable;
  should become a stated property.
- **No `.base` ships today** (zero `*.base` files module-wide; no `bases:` row in
  `module.yaml`) — the owner ruling's ship-no-base option is already the de-facto state;
  nothing to remove. `[!stale]` marker convention real at `wiki-supersession.md:64-69`.

**Open design questions (carry):** (1) does the module ship Obsidian Bases at all — owner
ruling tilts to no (vlt-core folds views into `wiki.base`; a shipped `ledger.base` would
diverge from the reference vault on day one), record as the standing posture or revisit;
(2) Bases date-filter syntax (`review_after <= today`) is assumed, not verified — verify
before shipping the Due-for-review view as documented reference; fallback: Horizon
(sorted ASC) + the lint `review_due` finding as the queue; (3) one `review_after`
definition across three surfaces — `frontmatter.md` owns it, 091004's deferral block and
091005's freshness semantics reference it (proposal, adopt at the joint bump); (4) aging
queue escalation — lint's job or an enforcement-kit tripwire (lean tripwire: lint finds,
it shouldn't also nag); (5) v2 keys (`source_type:`, `review_note:`) parked for a future
`frontmatter@4` against usage evidence.

---

## Capture — eleven filings (grounded against module source 2026-07-17, v0.6.0 @ a117f4f)

Capture-run notes (run 2, 2026-07-17). Owner confirmed **all eleven** un-captured filings
in scope; none deferred. Grounding ran as eight parallel source-verification passes (the
four graduation-queue filings graded together as one cluster; the rest one-per-filing);
every `file:line` below was re-derived from current source, not taken from the filings.

Two run-level facts shape everything that follows:

1. **Cited ≠ captured.** Five of these filings were already cross-referenced inside the
   deferred acceptance ledger as *evidence*. Being consumed as acceptance evidence is not
   capture: the ledger asks "did the shipped thing work?", capture asks "what does the
   module owe next." Each section below states explicitly which claims were already
   consumed (and are closed) versus which are live evolution material.
2. **Three central claims were REFUTED and one filing's title is false.** This is a high
   correction rate, and it is not a criticism of the filers — see the Part 2 through-line.
   Every reversal came from a filing reasoning correctly from a module self-description
   that was itself wrong. Briefs must cite the grounded verdict, never the filing's
   headline.

### A3-7. The research-note graduation queue (2026-07-11) — `…114226-research-note-graduation-queue.md`

**Context.** A vlt-core CIS run proposing a candidacy axis for research notes: keys
(`revisit_after`, `ingest:`), lint findings (`linkage_ripe`, `cluster_ripe`), an
ingest-time probe, and a dispatch queue line. The design half of a three-filing cluster
(A3-8/A3-9 are its calibrations).

**Grounding: premise survives, projection spec does not, and grounding found the defect
underneath the whole cluster.**

- **The gap is real.** `frontmatter.md:119-131` is the entire research-note schema
  (`topic`, `status`, `sources`) — no candidacy key. `frontmatter@3` scoped research notes
  out of the freshness axis deliberately: `review_after` is wiki-only (`:99`, `:115`), and
  `:131` states research notes are written-once with no `last_updated`. GAP CONFIRMED.
- **⚠ GAP CONFIRMED (new — the cluster's root cause, filed by nobody):**
  **`vlt-research/SKILL.md:65` writes `topic: <subject area>` as a SCALAR**, contradicting
  `frontmatter.md:131` ("Research notes use the same `topic:` list form as wiki pages")
  *and* its sibling `vlt-ingest/SKILL.md:84` (YAML list). Both skills ack `frontmatter@3`.
  **55 of 92 vlt-core research notes carry the scalar form the module told them to write.**
  The `topic:` raggedness A3-8/A3-9 report as *field data blocking `cluster_ripe`* is
  manufactured by the module's own write template. **One-line fix; cheapest item in the
  arc; correct independently of whether the queue ever ships.**
- **Unpoliced by construction.** `vlt-lint/SKILL.md:60` scopes the `topic:`-is-a-list check
  to "for every wiki page"; the string→list auto-fix at `:88` sits under the same wiki-only
  heading. The machinery to heal this exists and needs only its scope clause widened to
  `{research}`.
- **PROVENANCE CORRECTION — LB1's diagnosis.** The filing says discoverability "was
  under-specified as wiki-links-only." `grep -rni "discoverab\|undiscoverable"` across
  `governance/`, `vlt-research/`, `vlt-ingest/`, `vlt-lint/`, `vlt-query/` returns **zero
  hits** — the module never defines research-note discoverability *at all*. There is no
  over-narrow definition to correct; the gap is **total absence of a lifecycle statement**.
  The remedy may survive, reframed.
- **`vlt-lint-full.js` has no research read path.** LB2 is understated: `vlt-lint:43` — "The
  workflow sweeps `{wiki}` **only**"; research notes enter only as `crossLayerSlugs`,
  normalized basenames, never content (`vlt-lint-full.js:23`, `:48`, `:150`). Change 3 is
  not "add findings to the schema" — it is "give the workflow a research zone." Scope
  honestly before briefing.
- **Verbatim-copy mechanism is wrong.** Change 1 proposes copying `review_after` semantics
  "verbatim" into a research block. `frontmatter.md:115` forbids exactly this: "This is the
  **single definition** … every other use references it, never redefines it." Vocabulary
  alignment right; mechanism must be a pointer.
- **Vocabulary collision.** Change 2's `flag_for_human` orphan set collides with shipped
  `fix_now.orphans` (`vlt-lint:117`, computed `vlt-lint-full.js:146`), which already means
  *wiki pages with no inbound links*. Needs a distinct term.
- **PROVENANCE CORRECTION (handshake) — change 6 is not "optional surfacing."**
  `vlt-dispatch` is **not** a `frontmatter` consumer (`frontmatter.md:12` lists
  `[vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint]`; `vlt-dispatch:3` pins
  `spec@1` only). A ledger line is a **consumers-list edit** + a new ack, or `vlt-lint:74`
  flags it. Note `:239`: `ledger` is read-only — a computed line is compatible, a nagging
  one is not.
- **SUPERSEDED ×2.** Change 7 (Bases) — precedent already ships at `frontmatter.md:117`
  ("the module ships no `.base` file") plus the standing owner ruling (091006 OQ1);
  reduces to writing two documented reference views. Migration note re overlay-subsumption
  — **shipped in build-18** (`2b79e89`); the filing is stale here.
- **Consumer walk is wider than filed.** `@4` must re-pin `vlt-extract:4` and `vlt-mint:3`
  too (`frontmatter.md:12`); the exit gate at `vlt-mint:141` blocks on them.
- **frontmatter@4 has parked cargo from two arcs.** 091006 OQ5 parked `source_type:` /
  `review_note:` for `@4`; this filing independently parks `revisit_when:`. Whoever opens
  `@4` inherits ≥3 parked keys — a batching decision, per build-16's "one coordinated bump,
  NOT split" precedent.

### A3-8. Graduation-queue field calibration — vlt-core (2026-07-11) — `…153000-graduation-queue-field-calibration.md`

**Field evidence about a vault, correcting A3-7 before it ships.** Mostly
ungroundable-by-design against module source; graded where it touches the module.

- **The union projection — CONFIRMED as a module-relevant correction.** Naive
  frontmatter-only projection is ~79% false-positive (62/90 flagged, 49 absorbed); the
  union (frontmatter ∪ body wikilinks ∪ shared-source overlap) is what should ship.
  Module-side corroboration the filing didn't cite: `vlt-lint:59` already treats a wikilink
  resolving to a cross-layer note as a legitimate edge, and `vlt-lint-full.js:150` maintains
  `crossLayer` precisely so body-level `[[research]]` links aren't misread. **The union
  isn't a new idea — it's consistency with machinery already shipped.**
- **PROVENANCE CORRECTION — `topic:` raggedness is module-caused, not vault drift.** The
  filing reads the split as calendar ("pre-July ragged, July+ clean"). It tracks **which
  skill wrote the note**: `vlt-research:65` (scalar) vs `vlt-ingest:84` (list). See A3-7.
  Its remedy ("gate `cluster_ripe` behind a normalization rule") treats the symptom; the
  one-line source fix + widening `vlt-lint:60`/`:88` to `{research}` mostly dissolves it.
- **K-threshold accretion was not the observed pattern** — GAP CONFIRMED (design input,
  unbuilt). Five replacement signals proposed; none has a module site. Two are
  reducer-shaped and hit A3-7's no-research-surface wall. The **date-ordering tell** (note
  `created` postdates page `last_updated`) is the only one with a zero-cost substrate
  today (`frontmatter.md:91`, `:54`).
- **Per-source/per-section probe** (partial ingest outnumbered orphaning 8:5) — GAP
  CONFIRMED; sharpens A3-7's unbuilt probe before it's specced.
- **Exempt-backfill is ~1 note in 90** — corroborates A3-7's no-migration claim.
- **Living-document series carve-out** — GAP CONFIRMED; no module concept of a note series
  exists (`wiki-supersession.md` is wiki-scoped).
- **Half-built join — exact site.** `vlt-lint:67`/`:68` already cross-check newer
  `{research}` notes when *finding* staleness, but nothing tells the *resolver* to mine
  `{research}` first. Detection reads research; resolution doesn't.

### A3-9. Graduation-queue calibration — vlt-sayari (2026-07-12) — `…114837-graduation-queue-sayari-calibration.md`

**The cluster's strongest evidence, and it falsifies A3-7's stated pathology.**

- **Union validated on a second vault with the opposite profile** — naive 9/13 (69%) →
  union 3/13 (23%). Verified live: vlt-sayari has 13 research notes, 34 wiki pages, exactly
  as filed. Two vaults, opposite shapes, same conclusion. **This is the cluster's
  strongest-evidenced single recommendation.**
- **⚠ A3-7's premise did not reproduce.** A3-7 predicted true orphaning at the work vault;
  A3-8 predicted it too. A3-9 found **throughput/relay latency** instead (wiki froze
  post-migration; 4 librarian-bound relays open 12–15 days). **The mechanism as designed
  addresses a failure mode neither vault exhibits as its dominant loss.**
- **Scan-surface question is real — GAP CONFIRMED.** Graduation-ripe knowledge mostly isn't
  in `_agent/research/` (it's in 27 handoffs, partner threads, project status files). The
  contract names `partners` (`:37`) and `backlog` (`:36`) as first-class and blesses ad-hoc
  `_agent/` artifacts at `:54` ("the map names the *load-bearing* locations, not the *only*
  permitted ones"). A research-zone-only detector is scoped to one of several sanctioned
  zones. The filing's demand — *"decide it, don't default into it"* — is well-founded.
- **Lint-cadence dependency — CONFIRMED, and it's a designed property.** `vlt-lint:23-29`:
  scoped mode falls back to full when `{log}` has no prior entry, so the queue isn't lost —
  but `:62`'s `review_due` (and anything on the same rail) only fires **when lint runs**.
- **Provenance caveat is honest and self-corroborating.** Factory-side read of an
  Obsidian-Sync snapshot; `dev/` is indeed absent (Sync drops symlinks), exactly as the
  caveat predicts. Nothing in A3-9's claims depends on the dropped surfaces.
- **Vault-local demand ≠ module claim.** The researcher's backlog item and engineer's
  thread item are legitimate demand signal carrying no provenance weight over module
  source. Recorded per the classification rule.

### A3-10. The dev-zone contract graduation (2026-07-12) — `…114910-dev-zone-contract-graduation.md`

**A candidate, not a defect** — shares only vlt-sayari provenance with the cluster.

- **The zone is genuinely absent** — `vault-operating-contract.md:29-44` has no such row;
  `module.yaml:44-59` no such key. CONFIRMED.
- **The slot half-exists, and the real defect is sharper than filed.** `:79-81` defines a
  *tool zones* class, and vlt-sayari's own `dev/` prose (`CLAUDE.md:38`) was built by
  analogy to it verbatim. But `:81` hardcodes "**two** top-level folders" as a closed
  enumeration — **precisely the completeness-list drift the standing rules name.** The
  capture is arguably *"make tool zones an extensible class"*, not *"add a `dev/` row."*
- **⚠ GAP CONFIRMED — worse than filed: the contract is internally inconsistent.**
  `module.yaml:49` and `vlt-setup/SKILL.md:59` both carry the `specs` row; **the contract's
  table (`:29-44`) is the only one of three copies missing it — while the contract itself
  uses `{specs}` at `:227`.** Provenance: build-15 (`3795d86`) scoped exactly the two
  siblings (`build-15-spec-convention.md:98-108`) and never listed the contract table — a
  **build-15 scope omission**, not organic drift. Compounding: `module.yaml:41-43` declares
  itself SSoT ("never a hand-transcribed markdown table") while `:29-44` **is** one. **This
  is the second build-15 residue in this run** (see A3-12) — the two argue for treating
  build-15 follow-up as a unit.
- **PROVENANCE CORRECTION — the filing's own invariant is backwards.** It summarizes
  sayari's usage as "read-only-for-partners: yes." `vlt-sayari/CLAUDE.md:38` says the
  opposite: the symlinks exist so a dev context can "read the vault's spec/knowledge files
  **and edit the code in one tree**." The actual invariant is *"not a content layer"* —
  partners never ingest/lint/extract from it — **not** "read-only." Shipping the filing's
  framing would encode a boundary the field pattern doesn't have and doesn't want.
- **Contract-edit discipline reading is accurate** — verified structurally:
  `vault-operating-contract.md:1-10` carries no `version:`/`consumers:`, and it lives
  outside `{conventions}/`, so `vlt-lint:75`'s `convention_meta_missing` correctly doesn't
  fire.
- **No subsumption analogue for contract prose** — CONFIRMED. Overlays are conventions-only
  (`:92-94`; `vlt-lint:77`), so build-18's pass doesn't reach the contract. The filing's own
  remedy (upgrade note tells the owner to trim) is the only mechanism available.
- **"Related to nothing currently roadmapped" — PARTIALLY WRONG.** The `specs`-row drift is
  roadmap-adjacent: `:100` above already recorded that map's pre-build-15 state.

### A3-11. vlt-sayari 0.6.0 upgrade field evidence (2026-07-12) — `…114940-sayari-060-upgrade-field-evidence.md`

**~90% already consumed as acceptance evidence and DISCHARGED. Exactly one claim is live
evolution material.** Self-declared evidence filing; its own capture note is accurate.

- **Already consumed → closed, no capture:** §1 retrofit scan (build-15 migration-offer
  half, discharged `:645-650`); §1 overlay-subsumption vs a ~270-line overlay (build-18 F2,
  discharged `:749-757`); §1 header migration + jump path + 3 mints preserved (`:763-767`);
  §2a capability families (`:763-766`, with the ruling **exercise, don't prune**); §2c loop
  profiles (`:585-587`); §2d first field skill retirement (`:766-767`).
- **§2b overlays — PARTIAL, and the ledger is right to withhold.** F3 stays open, retargeted
  to vlt-sayari (`:758-762`): the filing evidences the *lifecycle* but never a post-upgrade
  write op honoring an overlaid rule. Discharging from lifecycle evidence would be
  inference. Needs a live event, not capture.
- **§3 — SUPERSEDED, and overtaken.** The filing asks to tick the loop-profile watch as
  half-discharged; the 07-17 pass closed **both** halves and filed the wearer half as a
  build-11 defect (→ A3-17). Its read of `vlt-track:16` is correct; its *ledger
  recommendation* is obsolete. Do not re-open.
- **⚠ §2e — PROVENANCE CORRECTION, uncaught anywhere (the ledger swept §2 in as bulk
  "bonus evidence" without grounding it).** The filing calls `vlt-track` and
  `vlt-project-spec` "the module's two named opt-ins." **The module names zero, and says so
  explicitly:** `extraction.md:47` — "no skill shipped with the module uses it"; `:121` —
  "No shipped op uses this." `vlt-track` is a *consumer* of `extraction@2` (the mechanism's
  implementer, not a grantee — `vlt-track:98` says so outright), and **`vlt-project-spec`
  does not exist in module source at all** (`grep -rn "project-spec" skills/` → zero
  outside `reports/`) — it is a sayari local mint. The naming lives in sayari's
  `extraction.overlay.md`, i.e. the convention's `:47` mechanism working as designed. The
  *substance* survives (the firewall is genuinely exercised); the *attribution* does not.
  **Record the correction so the framing doesn't become folklore** — this is the second
  filing to lean on it (see A3-14, which reasons from the same misreading in the opposite
  direction).
- **§4a — GAP CONFIRMED; the only live material here.** The filing hedges ("*If* the prose
  doesn't already say…"). It doesn't. The **behavior is already correct** — every Step-1
  enumeration is disk-derived by construction (`vlt-upgrade:29` "always, from the living
  vault", `:31`, `:33` "every `vlt-agent-*` dir under the live skills dir", `:34`, `:38`).
  **What's missing is the explicit negative:** `grep -rni "derive-first|prior ledger|from
  disk"` across the shipped surface → **zero hits**. The rule is *enacted* but never
  *stated*, so nothing stops a future session reading the prior ledger entry as the preserve
  checklist. Evidence is strong and dated: within 2 days of the 07-09 upgrade sayari grew 4
  light capabilities, 1 minted skill, and a family — **none in any ledger inventory**.
  Sharpened site: `:41`, where snapshot and ledger touch and the conflation is available to
  make. Ledger `:768-772` already defers this *to* capture — cited, not captured.
  **This is the derive-first invariant at a second layer** (`:451` records it for
  enforcement counters only).

### A3-12. The spec convention has no advocate (2026-07-13) — `…092341-spec-convention-has-no-advocate.md`

> ## ⚠ THE ARC-BLOCKING FILING — ITS CENTRAL CLAIM IS **FALSE**, AND THIS ROADMAP HAS BEEN CONTRADICTING ITSELF SINCE 07-13.

**Grounding verdict: PROVENANCE CORRECTION on the central claim. All cited sites are
accurate; the conclusion drawn from them is not.**

- **The claim.** Filing `:16`: "the spec class is touched by exactly two skills, and
  **neither can originate one**." This roadmap escalated it at `:653` to "**no shipped
  surface can originate a spec**" and reclassified build-15's tail from *awaiting first
  exercise* to **BLOCKED BY DESIGN GAP**, blocking arc-closeout.
- **⚠ REFUTED. `skills/vlt-upgrade/SKILL.md:75` originates specs** — the human-gated
  **proto-spec retrofit**: it scans `_agent/handoffs/` for spec-shaped docs ("revised in
  place, carrying 'What changed' sections, or with ≥2 relay entries … pointing at the same
  path"), **offers** the retrofit per `{conventions}/spec.md`, `git mv`s to `{specs}` and
  conforms frontmatter. That **is** origination: detect → ask → create the first `{specs}`
  artifact. It shipped **in build-15 itself** (`3795d86`), briefed as **F6** at
  `build-15-spec-convention.md:150-170`, reported via `migrations_run` at
  `vlt-upgrade:95`. The filing traced only `vlt-mint` and `vlt-dispatch`; the real
  spec-touching surface is **four** skills, not two (add `vlt-upgrade:25,71,75,95` and
  `vlt-setup:61,144`).
- **⚠ THE ROADMAP CONTRADICTS ITSELF.** `:644-651` — four lines *above* the reclassification
  — **discharges that very path**: sayari's retrofit scan "surfaced exactly one candidate,
  offered it, and accepted the owner's decline." Corroborated at `…114940:20-23`. **Both
  cannot be true.** `_agent/specs/` being empty is a **correct negative** — the origination
  path fired, and a human said no — not a silent zero.
- **Consequence for arc-closeout: the premise does not hold.** What remains dry is the
  **consumer lock** and **spec-bump relay**, and they are dry because sayari's owner
  *correctly judged its one candidate not to be a spec*. **That is a convention working,
  not a convention unreachable.** Whether zero-specs-across-two-vaults-in-9-days is a design
  gap or simply true scarcity of durable cross-partner contracts at current vault scale is
  **an open question the evidence does not settle** — but it is no longer evidence of
  unreachability. **Owner must re-rule on whether the arc is blocked at all.**
- **SUPERSEDED — the proposed detector already ships.** The filing's `spec_candidate`
  heuristic (`:74-77`: "a doc in `_agent/handoffs/` with more than one revision, or more
  than one relay pointer against the same path") is **verbatim what `vlt-upgrade:75`
  already does**. It independently reinvented a shipped detector. **What isn't shipped is
  running it at lint cadence rather than upgrade cadence — the residual gap is CADENCE,
  not existence.**
- **PROVENANCE CORRECTION — "a defect in build-15's shipped surface."** Build-15 shipped an
  origination path *and* dispositioned the rest explicitly
  (`build-15-spec-convention.md:177-187`). The lint checks were a **named, ruled follow-on**
  (`:179-181`), not an oversight. This is a scope-boundary question, not a defect.
- **CONFIRMED as filed** (cites exact): `vlt-dispatch:41` (never authors them), `:154`
  (relay reflex on a spec `version` bump), `vlt-mint:11` (no author-a-spec kind — zero-hit
  grep for "author a spec|promote a handoff|write a spec|create a spec" across shipped
  `skills/`), `:108` (lock fires only on an already-existing spec), `spec.md:13-16`
  (byte-accurate), `contract:227` (exact — but "only trigger" needs narrowing to *only
  trigger in steady-state operation*).
- **GAP CONFIRMED — the adoption-metric hole** (`frontmatter.md:216-231`): every facet
  (`enforcement_stage/checked_by/moment/counter`, `deferral_metric/threshold/review_after`)
  measures **violation**. No first-instance/adoption axis. **The filing's strongest point,
  and the one this roadmap under-weighted relative to the false origination claim.**
  Generalizes to any future class-declaring convention.
- **⚠ GAP CONFIRMED (new, adjacent) — `vlt-upgrade` is an unregistered consumer of
  `spec@1`.** `spec.md:12` lists `[vlt-mint, vlt-dispatch]`; `vlt-upgrade:1-4` carries
  **`name` + `description` only — no `depends_on:` line at all** — yet `:75` reads the
  convention, encodes its heuristic, and conforms artifacts to its schema. Build-15's own
  verification asserts the opposite (`:191-193`: "grep `spec@` across `skills/` finds
  exactly two") — **that grep searched for the ack, not the consumption, so F6's own new
  consumer was invisible to it.** If `spec.md` bumps to v2, the consumer walk
  (`vlt-mint:140`, exit-gated `:141`) and lint's coherence net (`vlt-lint:74`) both walk
  only the *listed* consumers — `:75` drifts silently. It is the only place in the module
  where a skill recites a convention's mechanics without appearing in its `consumers:`.
- **Build-17 ownership — the roadmap's "build-17 now also owns the spec-advocacy gap" is
  half-right.** *Fits:* 091003's thesis is this exact failure shape; its "no deferral
  without a wire" rule is the general form of spec.md's lonely tripwire; and derive-first is
  **satisfiable** here (a spec-candidate count derives from dispatch relay entries + handoff
  file state — the inputs `:75` already greps; no stored counter). *Doesn't fit:* the real
  residual is (a) cadence, (b) a `frontmatter.md` schema facet, (c) a `consumers:`
  registration — only (a) plausibly wants a tripwire. **The adoption-metric facet fits
  badly**: 091003 derives metrics from *event records*; an adoption metric measures an
  **absence** — no event to count. And 091003 is itself evidence-blocked, so hanging
  build-15's close on build-17 **trades one blocked tail for a longer one**. Note also
  091003's closing line declares the dependency in the **spec→tripwires** direction; the
  roadmap now proposes the reverse — a **two-way coupling** neither filing has weighed.
  **Re-ideate ownership against this grounding rather than inheriting the reclassification.**

### A3-13. New-partner mints field one lens (2026-07-16) — `…153000-new-partner-fields-one-lens.md`

**Core defect CONFIRMED verbatim. But this is not new material — it was surfaced two arcs
ago and parked.**

- **Path correction (benign).** The filing cites `workflows/vlt-review-council.js`; module
  source is `skills/vlt-setup/assets/workflows/vlt-review-council.js`. It read vlt-core's
  installed copy — **diffed identical**, so the citation is vault-shaped but the read is
  faithful. Flagged because citing `.claude/workflows/` as module source is exactly the
  pattern that produces real provenance errors later. Line numbers re-derived: the filing's
  `:54` for `KIND_PANEL` is **correct**.
- **CONFIRMED — the asymmetry.** `:66` `'new partner': ['architect']`; `:69` `'retire a
  partner': ['architect']`; against `:67`/`:68`/`:61` fielding all four. `:57` `'add a
  capability'` (gated) spends three — more frequent, more reversible. The comparative
  argument stands on source as written.
- **CONFIRMED — the laundering.** `:74-78` mint mode ignores caller `lenses`; `:86` debate
  mode honors them. "The way to get a real panel on a new partner is to not tell the council
  it's reviewing a mint" is a fair reading. Note `:27` documents caller `lenses` as a
  **narrowing** affordance — the filing's proposal B (widening) is a *different* semantic
  it doesn't acknowledge.
- **CONFIRMED — the comment asymmetry, and the filing is right to flag its own limits.**
  `:66`/`:69` carry **no rationale comment**; neighbours do (`:57`, `:61` "cross-partner
  blast radius", `:62`). The "by design" phrasing it quotes is genuinely **vault-local**
  (`vlt-core/_agent/mint/decision-log.md:129`) and the filing explicitly declines to treat
  it as module rationale. **Correct call.**
- **CORRECTION — undercount: four, not three.** The vault's own log says so
  (`decision-log.md:53`: "the **fourth** architect-only partner panel"); Dog Trainer
  (2026-06-09) was also a gated `new partner` (`inbox/archive/2026-06-13-092848`). **Every
  `new partner` mint in module history has fielded one lens.** The filing undersells itself.
- **⚠ NOT NEW — twice-deferred, and this is the finding above the defect.** Surfaced to the
  maintainer in June: `inbox/archive/2026-06-13-092848:87` — "*If richer new-partner review
  is wanted, that's a separate KIND_PANEL decision — out of scope for this filing, surfaced
  for visibility.*" Then captured into Arc 1's roadmap **as a note, not an item**:
  `archive/inbox-evolution-roadmap.md:153` — "*a separate KIND_PANEL decision.*" It was
  routed to a decision that was never made, across Arc 1 → 2 → 3. **The escalation
  worked; the parking is what failed.** Both prior homes are in archived trees the standing
  rules forbid appending to — **capturing it here is what finally gives it a live home.**
  This is one rung up from the roadmap's own adoption-gap thread (`:841-848`): *a surfaced
  defect whose deferral nothing tracks.*
- **CORRECTION — the cost is latency, not lost review.** The filing says three claims went
  untested across two rounds. The mint ran **four** rounds: `decision-log.md:29` — round 3
  in debate mode, "*all 4 lenses — the only way to convene a real panel on a partner*" —
  and all three claims resolved substantively. **Real cost = two wasted rounds + ~206k
  tokens + a mode-laundering workaround.** Still a strong case; state it accurately.
- **CORRECTION — the motivating example is self-retracted.** §3 rests the skeptic's
  necessity on a `trust: raw` single-source survey. The same mint voided that framing —
  `decision-log.md:44`: "*`trust: raw` is **not** an aggravating fact (128/128 wiki pages
  are `trust: raw` — it's a filing state, not an evidence grade)*." The single-source
  concern survives independently (`:42`); the `trust: raw` half must not reach a brief.
- **⚠ GAP CONFIRMED (new) — proposal B collides with the lens cap.** `:89-90`: `if
  (lenses.length > 4) lenses = lenses.slice(0, 4)`. Proposal A lands exactly at the cap
  (fine). **B is silently truncated** — widening an already-4-lens kind drops a lens with no
  warning. The filing never mentions the cap exists. **B is not shovel-ready.**
- **Proposal C — insertion point sharpened.** The workflow already returns `lensesFielded`
  (`:198`). But `SYNTHESIS` (`:105-118`) is `additionalProperties: false` with a fixed
  `required` list — a warning **cannot** go in the moderator's schema without a schema
  change. Correct home is the **return-assembly site `:194-199`**, outside the schema.
  Cheaper; say so in the brief so a builder doesn't reach for the schema first.
- **⚠ The build-16 interaction — the sharpest unnoticed consequence.** Build-16 ships the
  bell rubric as a **mint-mode standing question injected into every lens's brief**
  (`:132-136`), plus the moderator's HARD RULE (`:169`). **So on `new partner` — the kind
  most likely to create a boundary — build-16's "WHERE'S THE BELL?" question is asked of
  exactly one lens.** The rubric rode `KIND_PANEL`'s single-home by design
  (`build-16-…:56`, roadmap `:319`) and inherited its thinness on exactly the kinds where
  the bell matters most. **This is a live candidate explanation for the still-open build-16
  tail** (`:728-732`: three classifier runs, three `non-boundary`, "*the gate is live … and
  has never once rung*"; "*whether three straight declines is correct behavior or a
  classifier biased toward silence is not yet distinguishable*"). Note the **historian** —
  the lens that would read the record — is absent from exactly the kind whose classifier
  misfired twice by mis-reading the record. **Hypothesis worth capturing; grounding cannot
  settle it.**
- **No handshake.** `KIND_PANEL` is workflow code, not a versioned convention — proposal A
  is two lines (`:66`, `:69`), no migration, no consumer walk.
- **Roadmap reconciliation — no contradiction, but the phrasing obscures the defect.**
  `:659-661` says "four council rounds, all four lenses convened"; the filing says two
  rounds, one lens. **Both are right about different rounds** (1–2 mint mode = 1 lens; 3–4
  debate workaround = 4). Build-15's confirming-negative force is **undiminished** — but
  the entry should note the panel was obtained **by workaround, not by `KIND_PANEL`**, or
  it will later be misread as evidence that `new partner` mints get a full panel.

### A3-14. The extraction grant authorizes nobody (2026-07-17) — `…090000-extraction-grant-authorizes-nobody.md`

**All textual claims CONFIRMED verbatim. The load-bearing causal claim is REFUTED and the
headline is overstated.**

- **CONFIRMED as filed:** `extraction.md:47` text exact (incl. "no skill shipped with the
  module uses it"); frontmatter `:11-12` (`version: 2`, `consumers: [vlt-extract, vlt-lint,
  vlt-track]`); the section names no operation; `vlt-track:98` enforces the condition
  verbatim. **Two missed second sites:** `:121` repeats the false claim independently
  ("No shipped op uses this"), and `vlt-track:113` (Verify) re-asserts the sanction. **Any
  fix must touch `:47` AND `:121`; two enforcement sites, not one.**
- **CONFIRMED — the clause is false, and the version is exactly right.** `vlt-track` was
  added by `299e70b` (2026-06-25), after `v0.3.1` (`d21bfbd`); `git ls-tree v0.3.1` →
  absent, `v0.4.0` → present. **Grounding adds the origin the filing lacked:** `299e70b`
  added `vlt-track` to `consumers:` and **left the prose untouched**. Per the build-4 rule,
  adding a consumer is *not* a rule change and **correctly does not bump `version:`**. So
  **no rule was broken** — the ceremony simply has no step that asks *"does the prose still
  describe reality?"* **That is the actual defect origin: a process gap, not a violation.**
- **⚠ REFUTED — C5, the filing's load-bearing error.** It argues: only a base edit can name
  an op; durability doctrine forbids base edits; therefore "authorizes nobody, **forever**."
  **The module ships a third route the filing reasoned past:** `vlt-mint:131` — "*Vault-local
  addition → **write the overlay (the default)**. If the change adds to the convention (**a
  new rule, a new subsection**) for this vault only … **Do not touch the base** … **do not
  bump `version:`** … This path is **upgrade-durable by construction**.*" Corroborated at
  `contract:95` (convention = base + overlay, merged on read) and `extraction.md:20`.
  Naming an op is an *addition* → overlay → no base edit, no doctrine violation.
  **And it is not theoretical: `vlt-sayari/_agent/conventions/extraction.overlay.md:8`**
  — "*## Personalized extraction — named opt-ins (this vault)*" — **names `vlt-track`
  (`:13`) and `vlt-project-spec` (`:31`)**, and survived the 0.4.0→0.6.0 jump and its
  subsumption pass intact. **The ceremony works, has been performed, and is durable.** The
  grant authorizing nobody **by default** is what an opt-in grant is *supposed* to do.
  The severity framing ("a shipped skill is told to refuse its own purpose … forever") does
  not survive.
- **What genuinely survives from C5 — narrower and real.** `vlt-track` is **module-shipped**.
  It cannot rely on a vault-local overlay for its own authorization: **the module must name
  it in the base, or `vlt-track:98` is unsatisfiable-by-construction for the one op the
  module itself ships.**
- **⚠ PROVENANCE CORRECTION — C6: the module never had a registry table.** `git log
  -S"registry"` on the convention → **empty**; `git log -S"dog-trainer"` on
  `governance/_meta/` → **empty**. Both the naming clause and the false clause trace to
  `8c0955f` (**v0.3.0 initial public release**), and `version: 2` is unchanged since
  (`git log -L11,11` → one commit). The table, its 2026-06-13 council, and its 2026-06-24
  repeal are **entirely vlt-core-local** (`upgrade-ledger.md:48`). **The filing's §4
  recommendation ("delete the naming requirement — it's a relic") rests on a module history
  that does not exist.** Delete-the-clause may still be defensible — but not on relic
  grounds; it would be **repealing live original design**. *Irony worth recording:* this
  filing corrects an earlier fabrication ("an upgrade ate the table") and then commits a
  subtler version of the same error. It is the same misattribution class as A3-15's — and
  is itself evidence for A3-15.
- **CONFIRMED as fact, PROVENANCE CORRECTION on remedy — C7.** vlt-core's
  `_agent/conventions/` holds only `.baseline/` — **zero overlays** — so its partners are
  indeed unnamed. **The remedy is vault-side**, exactly as sayari did. **Not a module
  defect; no module change fixes it.**
- **GAP CONFIRMED — C8, but the framing is wrong.** `consumers:` **is** defined, at
  `vlt-mint:136` (unambiguously a handshake map, never an authorization). Two real gaps:
  the definition lives in a *minting* skill while the misread happens at `extraction.md:12`,
  read by anyone; and `grep -rni "not an authorization\|change-notification"` → **zero
  hits** — the negative is nowhere stated. A live reader (the Chess Coach mint) got it wrong
  and was council-rejected: **field evidence, not speculation.** **Single-home caveat the
  filing ignores:** its §4.5 (annotate `consumers:` in the file) would restate semantics
  across **8** convention files — exactly the completeness-drifting list the standing rules
  warn against. Conformant shape is a **pointer**, or one clause at `vlt-mint:136`.
- **Conclusion CONFIRMED, reasoning corrected — C9.** `vlt-lint:80` has no authorization
  check, correctly (build-8 shipped method-grounding only, deliberately). But the absence is
  **not** the trace of a retired check — there was never one to retire. The filing's
  instruction should read: *the rule never existed in module source — and the naming rule
  **does** still exist and is **deliberately** unenforced by lint.*
- **Half REFUTED — C10 "no migration."** No vault has rows (true), **but this ignores
  vlt-sayari**: rewriting the base to name `vlt-track` or to drop the naming rule makes
  sayari's overlay section wholly/partly **subsumed by the base** — precisely what
  build-18's subsumption pass detects and offers for retirement, and it **would fire** on
  `extraction.overlay.md:13` at the next upgrade. Not a data migration, but a live
  downstream consequence **in the vault the roadmap just designated the F2/F3 evidence
  vault.**
- **Ceremony if the base is touched:** rule change bumps `2 → 3`, re-walks `[vlt-extract,
  vlt-lint, vlt-track]` (current acks all `extraction@2` at each `:4`). **Caveat:** fixing
  *only* the false clause is arguably a **prose correction, which per `vlt-mint:139` does
  not bump** — it changes no rule a consumer follows. Naming the op **does** bump. Whether
  they ship together is a scoping call.

### A3-15. Upgrade rulings never reach the decision log (2026-07-17) — `…090500-upgrade-rulings-never-reach-the-decision-log.md`

**Unusually well-grounded — every module citation re-derives correctly. Core defect GAP
CONFIRMED. Two of four proposed fixes need correction; grounding found two module defects
the filing missed.**

- **Which log — settled first.** The filing means the **vault-side
  `_agent/mint/decision-log.md`** (agent-zone, upgrade-durable, canonical), **not** the
  gitignored per-skill `.decision-log.md` build artifact. Working tree is clean (`find`
  → nothing; `.gitignore:20`). The two are already firewalled at `vlt-mint:61` and
  `vlt-upgrade:46`. **No confusion in the filing.**
- **CONFIRMED — every path terminates at the ledger or the report.** `vlt-upgrade:35`,
  `:41` ("append the opening half of a ledger entry"), `:65` ("surface it in the report"),
  `:37`. Exhaustive sweep confirms the negative: `_agent/mint/decision-log.md` appears in
  `vlt-upgrade` at exactly **three** sites — `:37` (confirm exists), `:73` (relocation of a
  *legacy file*), `:134` (Verify: "exists"). **Every one treats the log as an object to
  preserve, never to write.** "Untouched is exactly the problem" is a fair reading of the
  skill's own words.
- **CONFIRMED — the concrete failure.** `vlt-core/_agent/upgrade-ledger.md:48` is the
  "Firewall decision (user)" line verbatim; the decision log carries **no superseding
  entry**. Vault-side evidence for a module gap, correctly used.
- **GAP CONFIRMED — and grounding makes the argument stronger than the filing does.** The
  module has a **fully developed supersession idiom, deployed twice, applied to the decision
  log zero times**: `wiki-supersession.md:31`, `:50-55` (inline callout + page-level keys);
  `spec.md:47-48`, `:63` ("*Never silent — the same visibility principle*"). **The module
  tells the wiki never to silently overwrite a claim** (`vlt-ingest:133`) **and tells specs
  never to supersede silently — while its own canonical governance record has no
  supersession concept at all.** The fix is not novel machinery; it is applying a shipped
  idiom to the one record lacking it.
- **Fix A mis-homed.** The filing puts the whole rule in `vlt-upgrade`, importing
  decision-log **entry mechanics** into it — forbidden by single-home, since those live in
  `vlt-mint` (`:59`, `:61`, `:66`, `:95`). Correct split: **`vlt-mint`** owns the entry
  shape; **`vlt-upgrade`** carries **trigger + exit gate + a pointer** at `:65`, `:95`
  (`migrations_run`), `:134`. The exit-gate wording itself is well-formed and matches
  `vlt-mint:141`/`:159` precedent.
- **Fix B — provenance correct, but under-scoped.** The local ⚠ header at
  `vlt-core/_agent/mint/decision-log.md:6-14` is vault-only; the filing says so. **But
  there is no shipped artifact to "ship the discipline" in:** `vlt-mint/assets/` holds
  `capability-template.md`, `operation-skill-template.md`, `partner-agent-template.md` —
  **no decision-log template**; `vlt-setup:237` ensures the *directory* exists but never
  seeds the log. **The log is created ad hoc by whichever mint runs first, with no header,
  no schema, and no defined entry shape anywhere in module source.** *That absence is what
  let a repeal have nowhere to land.*
- **Fix C — split verdict. The observation is true; the module did not cause it.** The
  vault's ledger heading order is genuinely scrambled (`:5` 07-08, `:23` 06-24, `:41`
  06-24, `:55` 06-26, `:75` 07-03). But `vlt-upgrade:105` specifies "**append-only** …
  **never rewritten**"; faithful *append* yields strict oldest-first. The file is **neither**
  order — **out of order in a way the module's instruction cannot produce**. **Vault-local
  drift, not a module defect**; the filing's "aggravating factor" attribution is wrong.
  **The residual gap is real but different:** the shipped header template (`:108-110`)
  states the *write* discipline but **never the resulting read order**, so a drifted file
  announces nothing. **REJECT "ship it newest-first"** (contradicts `:105`'s load-bearing
  invariant); **ACCEPT the filing's own alternative — state the ordering in the header.**
- **Fix D — CARRIED AS-IS.** Should `vlt-upgrade` refuse to proceed on unaccounted-for
  gated convention edits? Filing offers it "as a question, not a recommendation." Recording
  only that it inverts the current posture (`:101` — the net "does not auto-merge either")
  and would change the stated contract at `:101`/`:129`.
- **§5 migration — GAP CONFIRMED, idiomatic slot.** `vlt-upgrade:69-76` with `:71`'s
  relocation discipline and `:95`'s `migrations_run` enum. The **"do not auto-restore
  anything"** constraint is well-judged and consistent with `:66`/`:68`. **One premise
  correction:** it scopes "for each entry **of kind `convention edit`**" — but **there is no
  kind field and no entry schema** in the shipped log. **The migration as specified cannot
  be mechanically scoped today; it depends on the schema work, which orders the build.**
- **⚠ Defects grounding found that the filing did not.** (1) **`vlt-mint:141` carries a
  stale pre-relocation path** — "*records the mint + council verdict in `.decision-log.md`*"
  — while every other site says `_agent/mint/decision-log.md` (`:59, :61, :66, :95, :108,
  :112, :131, :134, :150, :157, :159`). `:141` is **the `convention edit` kind's own
  recording instruction** — precisely the kind whose repeal this filing is about — and it
  names the clobber-prone location `:61` retired and `vlt-upgrade:46`/`:73` exist to clean
  up. **A vault following `:141` literally writes the record to the file the module spends
  three sites destroying.** Small edit, directly in the blast radius. (2) **No decision-log
  schema or template exists** — the structural reason the gap exists.
- **Handshake note:** nothing here touches a convention's `version:`/`consumers:` — the work
  is skill prose + new `vlt-mint` assets. **No consumer walk implied by this filing.**
  (A3-14 does trigger one.)

### A3-16. vlt-mint Step 4 registers local mints into shipped artifacts (2026-07-17) — `…091000-…`

**Core defect real and accurately quoted, but the filing under-counts the sites, over-states
the harm, and misses the durability interaction that is the sharpest thing here.**

- **CONFIRMED — quoted verbatim and correctly.** `vlt-mint/SKILL.md:152` tells a mint to
  register its row in `_bmad/module-help.csv` **and** add its `[agent]` entry to
  `vlt-setup/assets/module.yaml` `agents[]` + mirror CSV. **The bullet makes no provenance
  distinction — it reads identically for a shipped partner and a vault-local mint.**
- **CONFIRMED — the assets are shipped and refreshed**, grounded better than the filing's
  evidence (it cited a vault-local ledger; module source says it directly):
  `vlt-upgrade:45` (own-the-apply refreshes shipped `vlt-*`) and `vlt-setup:149`
  ("**module-owned: overwrite it to the current shipped versions on every install/update**").
- **CONFIRMED, with a build-18 correction the filing didn't have.** The row is still
  refreshed away — but **as of 0.6.0 it is no longer silent**: `vlt-upgrade:36` (build-18
  F1, scope at `build-18-…:60-64`) covers `SKILL.md` + `assets/**` of every shipped skill,
  so a Step-4-compliant edit now trips `skill_asset_divergence` and is captured + flagged.
  **Scope the fix as "stop generating the divergence", not "stop the silent clobber."**
- **⚠ PROVENANCE CORRECTION — the stated harm has no channel.** "My private chess coach
  becomes part of your module" **cannot happen**: `vlt-upgrade:45-46` copies module-source →
  install, **one-directional**; there is no reverse path. Verified the factory is clean:
  `vlt-setup/assets/module-help.csv` = 14 shipped rows, zero local mints;
  `module.yaml:18-33` `agents[]` = exactly librarian/researcher/creative. **A vault
  following Step 4 pollutes only its own install's copy.** Real costs are futility, a false
  decision-log record, and the interaction below — **not cross-install contamination.**
- **CONFIRMED — B1 is intact.** `merge-help-csv.py:188-230` (`filter_rows_preserving_local`)
  keeps a `vlt` row absent from bundled source whose skill dir exists live, reporting
  `local_mints_preserved` (`:374`); wired at `vlt-upgrade:51-61`, checked at `:134`.
  **Ordering is safe** — Step 2 refreshes the mirror to stock *before* Step 3 reads it as
  `--source`, so a local row can never masquerade as shipped. The filing's "the CSV merge is
  their durability" is accurate.
- **CONFIRMED and now 4-for-4.** vlt-core: 4 local mints on disk
  (`chef`, `chess-coach`, `dog-trainer`, `health-coach`), all 4 in `_bmad/module-help.csv`,
  **none** in the installed shipped assets. **Practice has converged against the
  instruction.**
- **⚠ GAP CONFIRMED — the filing under-counts: three sites, not two.** `:151` (heavy
  capability — "mirror it into the install manifest … so a re-install reproduces it") and
  **`:154` (retire path — the filing missed it entirely)**: a vault-local retirement is told
  to edit shipped assets it should never have been in. `:153` is a fourth, weaker instance.
  **Any provenance split must cover `:151`, `:152`, `:154`.**
- **⚠ GAP CONFIRMED (new — not in the filing; the sharpest finding and the strongest
  argument for the fix).** `vlt-upgrade:33` defines the local-vs-shipped test as "*every
  `vlt-agent-*` dir … whose code is **not** a shipped agent in the module's `module.yaml`
  `agents[]`*". **A mint that OBEYS Step 4:152 writes its own code into that very
  `agents[]`, and therefore classifies itself as SHIPPED at the next pre-flight** — omitted
  from the minted-partner snapshot, **silently voiding its B2 body-restore coverage**
  (`:63`). B1 still saves the CSV row (it keys off bundled source, not `module.yaml`), but
  the insurance is gone. **Step 4 doesn't merely fail harmlessly — it actively degrades the
  durability net that protects it.** This raises the filing's own "mostly self-correcting"
  severity assessment.
- **§3 (health-coach `decision-log.md:64`) — CARRIED AS-IS, per the filing's explicit
  request.** Module-side bounds offered without asserting a mechanism: the 2026-06-13 mint
  **predates build-18** (0.6.0, 2026-07-08), so at 0.4.0/0.5.0 **no skill-asset divergence
  net existed** — the trace that would distinguish "an upgrade reverted it" from
  "aspirational entry" **was not being produced by any code path at that time**. Both
  branches are consistent with the absence of evidence; module history does not settle it.
  **The filing's discipline is correct and its "either way, same fix" conclusion holds
  independent of the answer.**
- **No upstream path exists.** The module has **no documented way to deliberately upstream a
  local mint** (grep found none) — a genuine gap the filing surfaced only implicitly. The
  `vlt-track` precedent (a shipped row that began as a vault mint) shows it happens.
- **Nothing here is SUPERSEDED.** Build-6 and build-18 both shipped *net* machinery; neither
  touched Step 4's **write** side. **This is the first filing to hit the instruction rather
  than the net.**

### A3-17. Loop-profile drift — the title is false (2026-07-17) — `…100000-loop-profile-drift-predates-build-11.md`

**Status note.** The 07-17 discharge pass closed the vlt-track loop-profile **watch item**
(`:581-599`) and filed the confirmed wearer-half drift as a build-11 defect — **this filing
is that defect.** The watch is discharged; the defect has never been captured. Fresh
material.

- **CONFIRMED — exact, and reinforced beyond the filing's cites.** `vlt-track:16` verbatim
  incl. "*This skill reads that profile from the invoking partner; **it hardcodes none of
  it**.*" Also `:31` (the On-Activation read beat) and **`:40`** (headless fallback: take it
  from `capabilities/track.md` "*or ask for the missing pieces — **never guess***"). `:40`
  matters: the skill's own fallback is **ask**, not improvise — weak evidence against the
  worst-case runtime reading, but it is prose, not a mechanism.
- **CONFIRMED, line added.** The template ships the block at
  `vlt-mint/assets/capability-template.md:55-67`; **`:67` is stronger than the filing
  credits** — it states the rule outright ("*'Wear `vlt-track`' = add a `capabilities/
  track.md` heavy pointer … **not** mint a duplicate loop op*"). Reinforced at
  `vlt-mint:55` and `:125`. **Nothing anywhere in module source tells a partner to declare a
  profile inline. The module-shipped half is coherent.**
- **CONFIRMED at rest, with a line-level correction.** vlt-core `dog-trainer/` and
  `health-coach/` hold `identity.md` + `thread.md`, **no `capabilities/`**;
  `chess-coach/capabilities/track.md` exists with the correct shape.
  `.claude/skills/vlt-agent-dog-trainer/SKILL.md:41` is exact. **But "health-coach — same
  shape" is imprecise:** it declares a **separate `### Loop profile` section at `:47`**,
  referenced forward from `:39`, not inline in the capability bullet. **Same class, different
  shape — a scan keyed to the dog-trainer shape would miss it.**
- **PROVENANCE — the precise half.** Every drifted artifact is **vault-local**; the module
  ships **zero vertical partners** (`build-11-…:141`). This is not module source that
  drifted — it is **module source that relocated a location the vault-local half was already
  occupying elsewhere, and shipped nothing to move it or notice it hadn't moved.** The
  filing's own "Why this is module signal" reaches this correctly; **its title does not.**
- **⚠ THE PRE-DATING CLAIM DOES NOT HOLD. Build-11 CREATED the drift.** Its brief is
  unambiguous that the relocation is its own deliberate act: `build-11-…:18` — "*the calling
  partner's loop profile **moves from inline-in-SKILL.md (vlt-core's field location)** into
  the partner's `capabilities/track.md` … **This is the single substantive design delta from
  a verbatim lift***"; `:76` — "*THE REHOMING (owner Q2 — the design delta)*"; and `:5`,
  `:61`, `:148` — "***Zero migration.** … Pure additive.*" `git log -- skills/vlt-track/`
  confirms the skill's first module appearance is `299e70b` = build-11. **Precisely:** the
  *inline placement* predates build-11 and **was correct** (vlt-core minted vlt-track locally
  with the profile inline; there was no contract to violate). **The *drift* does not — it is
  build-11's.** Build-11 moved the goalposts and declared "Zero migration" in the same brief:
  **true of the module's surface, false of the field.** The brief reasoned from the module's
  file tree, where the migration surface is **invisible by construction** — the module ships
  no verticals, so "no migration" looked like a fact rather than a scope decision.
- **⚠ THE SHARPEST FINDING, which the filing misses entirely: build-11's own acceptance
  check #1 IS this defect, written down in advance.** `build-11-…:162`: "*A vertical partner
  (e.g. **vlt-core's Dog Trainer / Health Coach**) wears vlt-track via its
  `capabilities/track.md` heavy pointer + loop profile; the skill reads … from **that
  file** (not the partner SKILL.md)*". **It names the two partners that drifted.** It was
  then discharged (07-17) against **vlt-sayari's Navigator and vlt-core's chess-coach** —
  wearers minted *after* build-11, **which were never going to be drifted. The check passed
  on substitutes.** *That substitution is the mechanism by which this stayed invisible for
  three arcs*, and it is a finding about **the acceptance process**, not just vlt-track.
  **Recommended re-title for any brief:** *build-11 rehomed the loop profile and shipped
  neither a migration nor a detector; its acceptance check named the two drifted partners
  and was discharged against substitutes.*
- **GAP CONFIRMED — exact site, and the gap is upstream of lint.** `vlt-lint:78` iterates
  "*for each capability file under `{partners}/*/capabilities/*.md`*" — **file-driven**, so a
  partner with no `capabilities/` dir contributes zero files and zero findings. Reads clean.
  The near-miss: `capability_skill_missing` fires on a **dangling pointer** (pointer →
  absent skill); **this defect is the mirror — absent pointer → present skill — and has no
  code.** `family_instance_missing` (`:79`) *does* implement declared-but-absent logic, but
  only against a family contract's `instances:` list. **There is no roster-level "should wear
  track" declaration, so there is nothing to check against.** *That is what makes this
  adoption-shaped rather than violation-shaped — the filing's central insight, confirmed.*
- **CONFIRMED — the retrofit precedent is real.** `vlt-upgrade:75` (human-gated, idempotent
  offer) + `:71` (relocation discipline: stub the old path, re-point open dispatch pointers).
  Field evidence: `…114940:18`.
- **⚠ CORRECTION — wrong mint kind.** The filing proposes "two overdue uses of *migrate a
  capability*." `vlt-mint:37` defines that as changing a capability's **owner**
  (confirmed `:80`, `:153`) — **an owner-change verb, not a home-change verb**. Lifting an
  inline prose block into a new `capabilities/track.md` migrates nothing: **there is no
  capability object to migrate — that is the whole defect.** The fitting kind is **`add a
  capability`** (heavy pointer creation), `council_class: none` when lane-rightful (`:80`) —
  cheap. The filing's conclusion about this option ("weakest alone") stands and is
  strengthened.
- **CONFIRMED and correctly scoped — the honest limit.** No track loop has run on either
  partner; **the runtime break is predicted, not measured.** The filing says so itself and
  asks capture to treat divergence as confirmed and consequence as unobserved. **That is the
  right disposition and grounding does not disturb it.**
- **The decision-log conflation guard is sound.** vlt-core's log ("*Dog Trainer / Health
  Coach have NO defect and need NO migration*") is scoped to the **gate-slot licensing
  rule**, not the profile location. Both readings are vault-local — evidence *about* the
  field, **not provenance**. The filing flags the conflation risk rather than falling into
  it.
- **Pairs with A3-12 — a real class with two instances in five days:** *a shipped location
  whose adoption nothing measures.* **Grounding adds a third, worse data point:** the failure
  isn't only "nothing measures adoption" — it's that **acceptance can be discharged against
  a non-adopting population.** That happened here, and it is arguably what happened to
  build-15's spec tail too.

---

## Capture — six filings (grounded against module source 2026-07-25, v0.7.0 @ dbcf018)

> **Run scope.** Owner confirmed **all six** un-captured filings in scope; none deferred.
> The `Next` line written by acceptance-discharge pass 6 predicted **five** (the 07-25 batch);
> the real total is **six** — `2026-07-18-115913` had never been captured and appeared nowhere
> in this doc, in either prior run. Recording that here rather than silently correcting the
> count, because it is the second run in a row whose predicted filing count was low, and the
> mechanism is the same both times: the acceptance pass names the filings *it* produced, and a
> filing produced by anything else (here, a partner-voice defect noticed in ordinary use) has
> no one to count it. That is a small instance of this run's own theme.
>
> **Grounding baseline:** all `file:line` citations below were re-derived against the working
> tree at `dbcf018` (v0.7.0, clean). Where a filing's cited line was off, the corrected line is
> given and the miss is named — filings that cite accurately are noted as such, because two of
> the six are notably precise and that is worth knowing when weighing their other claims.

### A3-18. The chess-coach persona line (2026-07-18) — `…115913-chess-coach-persona-line-seeds-fabricated-time.md`

**⛔ PROVENANCE CORRECTION — the filing's headline class is false.** The filing is titled
*"shipped-prose defect (latent, re-seeds on every install)"* and asserts that "the chess-coach
`SKILL.md` persona section **ships** an illustrative line" naming a concrete weekday.

**It does not exist in module source.** `grep -rn "Najdorf" skills .claude-plugin tools README.md`
→ **exit 1, zero matches**. The only occurrences anywhere on this machine are in the live vault:

- `{field-vault}/.claude/skills/vlt-agent-chess-coach/SKILL.md` — a
  **locally-minted** `vlt-agent-*` partner
- `…/vlt-core/_agent/partners/chess-coach/identity.md` and `…/capabilities/allocation-ledger.md`
- `…/vlt-core/_agent/artifacts/brainstorming/brainstorm-chess-coach-partner-2026-07-16/…` — the
  mint's own ideation record, which is where the line was authored

Per the standing rule in `CLAUDE.md` (*never treat vault-local evolution — minted partners,
overlays, capabilities — as module source*), this is vault-local mint prose. It ships to no
one and **cannot re-seed on any install**. The filing's remedy ("replace the weekday with a
non-temporal stand-in") is a correct fix applied to the wrong repo: it belongs in vlt-core, as
a `## Self`-tier or rebirth-tier edit to that partner, and no module change delivers it.

**GAP CONFIRMED (residual, much smaller than filed).** What survives grounding is one honest
module-side question. The shipped anti-fabrication posture is real but **aimed at a different
target**:

- `vlt-mint/assets/partner-agent-template.md:25` — "you do not fake continuity… you don't
  pretend a history you don't have"
- `:42` — "don't read an identity that isn't there and don't fake a thread… rather than
  inventing baselines that don't exist yet"

Every one of these forbids **faked continuity/relationship history**. None addresses
**invented specifics used as idiom** — a concrete weekday, a made-up week count, a fabricated
session number riding inside a figure of speech. And the module actively pushes toward the
prose style that produces them: `partner-agent-template.md:23` instructs the author to "lean
into a clear point of view — opinionated but not domineering," and `vlt-mint/SKILL.md:141`
seeds `identity.md ## Self` with "the distinctive starting register… so the partner is born
with an edge, not blank." Vivid persona prose is a shipped design goal with no shipped
counterweight naming temporal specificity as a hazard.

**Verified the module does not carry the seed itself:** a case-insensitive grep for weekday
names and relative-time idioms (`monday|…|sunday|last week|yesterday|this morning`) across
`vlt-agent-librarian`, `vlt-agent-researcher`, `vlt-agent-creative`,
`partner-agent-template.md` and `vlt-mint/SKILL.md` → **exit 1, zero matches**. The three
shipped personas are clean; the hazard is in what the module *invites authors to write*, not
in what it writes.

**Residual module-side scope, stated honestly:** at most one clause in the mint's
persona-authoring beat (Phase 1 / the template's persona placeholder) distinguishing
*characterizing prose* from *concrete temporal color*, and naming the figure-of-speech case
specifically — the filing's own strongest observation is that instance #3 slipped past a
written local guard **because the guard watched for calendar decoration, not a weekday riding
inside an idiom**. That distinction is the shippable content. Everything else is vault work.

**Evidence weight, marked:** three observed instances, one vault, one partner. Instances #1–2
predate the line entirely (the filing says so: #1 was "the day after the partner was minted").
So the line explains **one** of three occurrences; the other two are ordinary
invented-continuity, which the shipped rules already forbid. Ideation should weigh whether a
1-of-3 attribution justifies a template edit at all, or whether this is purely a vlt-core fix.

**Cross-filing:** this is the only run-3 filing not about a *report* being unreadable. It is
about a *partner utterance* being untrue — the same honesty axis, one layer down.

### A3-19. `revisit_after:` has no adoption path (2026-07-25) — `…144500-revisit-after-has-no-adoption-path.md`

**GAP CONFIRMED — every cited site verified exact, and grounding found a mechanism the filing
missed.** This filing's three factory-side citations are all correct to the line:

- `skills/vlt-research/SKILL.md:71` — `revisit_after: YYYY-MM-DD  # OPTIONAL — graduation-candidacy
  recheck date; absence = not a candidate (see frontmatter.md)`. **CONFIRMED verbatim.**
- `…/governance/_meta/conventions/frontmatter.md:138` — "**Absence = not a candidate**… only a
  note the writing partner judged graduation-relevant carries it, set at write time."
  **CONFIRMED verbatim.**
- `skills/vlt-lint/SKILL.md:84` (filing cited `:83`, off by one — `:83` is `linkage_ripe`) —
  "**Absence of `revisit_after:` = not a candidate = zero findings** — legacy research notes
  generate no noise (backfill is a non-event by construction)." **CONFIRMED verbatim** at `:84`.

**Grounding sharpens "nothing prompts it" into something stronger.**
`grep -rn "revisit_after" skills/vlt-research skills/vlt-ingest skills/vlt-extract skills/vlt-mint`
returns **exactly one hit** — `vlt-research/SKILL.md:71`. There is no beat, no question, no
gate, no second mention anywhere in the operational surface.

**⚠️ The discovery the filing did not make — the two research-note write paths disagree.**
Research notes have **two** shipped writers, and only one of them can see the key:

| Writer | Template site | Carries `revisit_after:`? |
|---|---|---|
| `vlt-research` (Researcher's own dive) | `SKILL.md:58-72` | **yes** — `:71`, commented optional |
| `vlt-ingest` Step 5 (ingest of an external source) | `SKILL.md:77-91` | **NO — the key is absent entirely** |

`vlt-ingest/SKILL.md:77-91` emits `type/created/title/author/trust/topic/status/sources` and
stops. A partner following the ingest path is never shown the slot, so it cannot decline it —
it never sees it. Since ingest is the **majority** research-note write path on a vault that
consumes external sources, this is a mechanical explanation for the filing's 0-of-96 that is
strictly better than "partners never elect it." It also means candidate shape 1 ("make the
write beat ask") is incomplete as scoped: it must land in **both** writers, or the omission
survives the fix.

**⚠️ The second discovery — the arc's own remedy is un-adopted.** The filing's shape 2 proposes
applying build-20's `adoption_first_instance:` facet. That facet is real and shipped:

- `frontmatter.md:237` — `adoption_first_instance: <null | dated reference to the boundary's
  first live instance>   # null/absent = declared-but-not-yet-adopted (an absence, not a violation)`
- `frontmatter.md:242` — defines the orthogonal adoption axis; names "**the first real spec
  minted under `spec.md`**" as its motivating example; states its absence is **not** a
  `vlt-lint` finding and that "whatever checks consume it… live where those checks live."

**But `grep -rn "adoption_first_instance" skills/vlt-setup/assets/governance/_meta/conventions/`
returns matches in `frontmatter.md` only — zero of the seven shipped conventions carry the
key.** All seven were checked (`extraction`, `frontmatter`, `spec`, `wiki-consolidation`,
`wiki-index`, `wiki-supersession`, `write-verification`); the two at `enforcement_stage:
declared` — `spec.md:13` and `wiki-consolidation.md:13` — are precisely the ones the facet
exists for, and neither carries it. **`spec.md` is the example `:242` itself names.**

So the facet is declared, has no instance, has no consumer, and by its own prose is invisible
to lint. It is a **fourth instance of the shipped-but-unexercised scar**, and the arc shipped
it as the answer to that scar. Ideation should note that shape 2 is not "apply an existing
facet" but "wire the facet for the first time" — a materially larger and more valuable piece
of work than the filing scoped, and one that pays off across every optional key the module
ships, not just this one.

**Residual scope after grounding:** (a) both write templates gain the key and a two-outcome
question, not just `vlt-research`; (b) the adoption facet gets its first real consumer — which
is a decision about *where the consuming check lives*, deliberately left open by `:242`;
(c) optionally the `vlt-lint:84` report line distinguishes "no candidates" from "no note has
ever carried the key" (the filing's shape 3, which grounds cleanly against the `vlt-lint:74`
honest-limit precedent build-23 shipped).

**Honest limits carried forward as filed:** one vault only (vlt-sayari unreadable from the
factory machine); the mechanism is not broken (`revisit_due` behaves exactly as specified —
this is adoption/visibility, not logic); four post-fix notes is a small sample for "partners
never elect it," though it is 4/4 plus 92/92 legacy.

**Acceptance consequence (already recorded in the ledger, restated here for the capture):**
build-20's `revisit_after` **positive** case is a pass-through, not a wait — no `vlt-lint`
run of any mode can discharge it because no subject exists. Its absence-branch half
(legacy-no-noise) **discharged** on the 07-25 full lint.

### A3-20. Contradictions have no drain (2026-07-25) — `…160239-contradictions-have-no-drain.md`

**GAP CONFIRMED, with one correction that makes the fix cheaper than filed.** All five cited
sites verified:

- `skills/vlt-lint/SKILL.md:69` — "**Contradictions** — … Document in both pages'
  Contradictions/Open Questions; note which source is more recent/authoritative, but never
  silently pick a winner." **CONFIRMED exact.** A documentation instruction with no next owner,
  no backlog filing, no revisit trigger.
- `skills/vlt-lint/SKILL.md:101` — "Do **not** auto-apply: page deletions (flag), contradiction
  resolutions (document both, flag), page merges (**file to backlog — see Step 4**)…"
  **CONFIRMED exact**, and the asymmetry the filing names is real and in one sentence: merges
  get a drain named inline; contradictions get a full stop.
- `skills/vlt-lint/SKILL.md:150` — `contradictions_handled: [...]  # already documented —
  surfaced, not vanished (**a managed disagreement is a feature**)`. **CONFIRMED exact.**
- `skills/vlt-lint/SKILL.md:175` — "**Contradictions are features, not bugs** — a well-documented
  disagreement beats false certainty." **CONFIRMED exact.**
- Write-side coverage: `wiki-supersession.md` and `wiki-consolidation.md` cover conflicting
  claims at ingest/merge time only. **CONFIRMED** — and `vlt-ingest/SKILL.md:133` is the live
  instance ("document both sides of a genuine, unresolved contradiction rather than picking a
  winner"), written by a partner who **holds the source**. The sweep-side case has no
  counterpart, exactly as filed.

**⚠️ CORRECTION — Step 4 is not closed to contradictions.** The filing states "Step 4 … its body
is near-duplicates only. Contradictions are never eligible for it." Grounding says otherwise:
`vlt-lint/SKILL.md:105` reads "For each near-duplicate/merge candidate **(and any other
maintenance worth doing later)**, append a `maintenance` item to `{backlog}`…". The catch-all
clause is already there. What is missing is **routing, not eligibility**: `:69` and `:101`
never point contradictions at Step 4, and the item template at `:108` and the routing sentence
at `:111` are both merge-shaped ("The merge itself is resolved later by `vlt-ingest`").

This materially cheapens the filing's shape 2. It is not "make Step 4 accept a new class" — it
is a second item template plus two pointers. And the backlog vocabulary already supports it
with no new type: `vault-operating-contract.md:234` — `kind ∈ capability-gap | maintenance |
knowledge-gap`.

**The evidentiary core is unrebutted and is the strongest thing in the run.** The same defect
class — a YouTube auto-caption substituting a plausible real name — appears on **both sides**
of the handled/unhandled line, separated only by whether a callout was written:
Schottenheimer/Flores counted `handled` while vlt-core's backlog carries an open
`knowledge-gap` for the same fact; Jonah/Alaric Jackson counted `unhandled`, identical failure
mode, same programme. A classification in which writing one sentence converts a factual error
into a documented feature is not tracking what it claims to track. Note this is also the
**cross-filing hinge**: the Jonah/Alaric pair is A3-21's evidence for a different defect
(source fidelity). Same symptom, two independent causes — brief them apart.

**The size-sensitivity point stands as filed and is the operational half:** `:69` is unbounded,
its cost scales with vault size while its value does not, and on this sweep the Librarian
**flagged 25 and documented none** — a skip that is invisible in the report. That is under-
delivery of exactly the kind build-23's `vlt-lint:74` honest-limit precedent exists to make
visible, and it argues shape 4 is not optional garnish.

**Cross-filing (the run's spine):** `contradictions_handled: 63` is a number that only grows
and is labelled health. Same shape as `spec.md`'s `deferral_metric` (A3-12) and
`revisit_after`'s silent zero (A3-19) — third mechanism, same class. See Part 3.

**Honest limits carried forward as filed:** one vault, one sweep (130 pages) — the mechanism is
size-sensitive by nature and a 30-page vault may have no complaint; the four-bucket triage
(11 fixable-now / 4 need-external-evidence / 8 genuine framing / 2 source-check) is the
Librarian's hand-work, offered as evidence the distinctions are actionable, **not** as a
proposed taxonomy; detection is not broken (the cluster pass caught a cross-page food-safety
conflict a human would not have) — this is disposition/visibility only; and "a managed
disagreement is a feature" is a good instinct the filing explicitly does not want removed.

**Provenance guess, carried as a guess (filing's own label):** contradictions were designed
write-side first, where the writer holds the source and *can* adjudicate, and the sweep-side
case inherited the vocabulary without the preconditions. **Grounding supports but does not
prove this** — `vlt-ingest:133` and the two write-side conventions do predate the sweep-side
report keys, and `:69`'s wording is verbatim the write-side instruction. Not established as
design intent; recorded as consistent with the source.

### A3-21. Auto-caption sources substitute plausible real names (2026-07-25) — `…160949-auto-caption-name-substitution.md`

**GAP CONFIRMED — the module-side claim is exactly right.** The filing's one factory-side
assertion is that `vlt-ingest` handles transcript sources with **no proper-noun guard of any
kind**, and that nothing cross-checks a new proper noun against what the wiki already knows.

Verified: `vlt-ingest/SKILL.md:48-63` is the heavy-source prep/interpret split — its concern is
**volume** (delegating fetch → normalize/clean → de-noise so the interpreting agent doesn't
saturate). `:83` and `:114` set `trust: raw`. Step 6's near-duplicate check (`:99`) compares
**concepts and slugs**, never entities. Step 9's attestation (`:153`) runs the tier-1
write-verification checklist, which is a structural check. **Nothing anywhere in the ingest
path validates a proper noun against existing wiki state.** The filing's provenance guess —
that transcript ingest was designed around the volume problem and source-fidelity never got
its own step — is **consistent with the source** and I record it as the filing did, as a guess
that grounding supports rather than proves.

**PROVENANCE handled correctly by the filing itself, and worth affirming.** The filing cites
`_agent/partners/librarian/capabilities/ingest-youtube.md:102-103` ("butcher proper nouns") but
explicitly marks it **vault-local and unshipped**, citing it as evidence that a careful local
author already tried and still missed the substitution case — not as a defect in shipped text.
That is the correct call and it is confirmed: no such capability exists in module source. Same
for `_agent/wiki/index.md:191`, the vault's improvised grounding-sufficiency rule — vault-local
prose, and the filing says so. **This is the run's most disciplined filing on provenance**, and
it is worth contrasting with A3-18, which made the opposite error about a vault-local artifact.

**The finding's substance, restated for the roadmap:** the hazard is not mangling but
**substitution toward the more famous figure in the same domain** — "Brian Schottenheimer" ×2
and "Brian Flores" for an unnamed Seahawks OC; "Aaron Rodgers" for Aaron Donald. A mangled
spelling announces itself and is caught every time; a substituted real name **reads as clean
data and gets encoded as fact**. Three firings, one source family. Observed cost: a cross-page
wiki contradiction (Jonah/Alaric Jackson), a hub page that records a role with **no name**
because the transcript offers two prominent wrong ones, a backlog `knowledge-gap` that no
source can close because it is caption damage rather than missing knowledge, and a prose rule
the vault wrote into its own wiki index that no mechanism reads.

**Residual module-side scope:** the filing's four shapes all ground cleanly. Shape 4 (fix the
shipped *framing* — distinguish self-announcing **mangling** from self-concealing
**substitution**) is the one with no shipped home today, because the "butcher proper nouns"
wording it corrects is vault-local; landing it means the module says something about transcript
fidelity it currently says **nothing** about, at `vlt-ingest`'s heavy-source section. Shapes 1
(ingest-time entity cross-check) and 3 (a `vlt-lint` entity-collision check) are complementary
prevent/catch, as filed. Note shape 3 lands in the same skill A3-20 touches — ideation may want
them in one build.

**Honest limits carried forward as filed:** one vault, one programme, one domain (all instances
from vlt-core ingesting the Mina Kimes Show) — the mechanism (ASR bias toward frequent names)
predicts it generalizes and worsens for *less* famous subjects, but that is prediction, not
evidence; the substitution table's right-hand column is **inference from context, not
verification** — no roster source was consulted, the Schottenheimer case is strong because it
collides with a well-sourced vault record, the Aaron Donald one is contextual, and **nobody has
verified the Jonah/Alaric pair either way**; frequency is three in one family — enough to call a
pattern, not enough to size the rate, and the other five episodes in the cluster were not
audited (by construction, undetected is the expected state).

**Cross-filing:** companion to A3-20 from the same sweep, and the filing says so. The
Jonah/Alaric contradiction is A3-20's evidence for a *disposition* defect and A3-21's evidence
for a *fidelity* defect. Both readings are correct; neither subsumes the other.

### A3-22. A synchronous partner→partner consult channel (2026-07-25) — `…132141-partner-consult-synchronous-channel.md`

**GAP CONFIRMED — the design gap is real and the filing's grounding is accurate.** This is the
run's only **candidate** (a proposed capability), not a defect. Sites verified:

- `skills/vlt-dispatch/SKILL.md:11` — "vlt-dispatch is the **vault's partner communication
  bus**… **one record with a drain** (`_agent/dispatch.md`) read through **three modes**."
  Modes at `:13-15` (`daily` / `relay` / `ledger`). **CONFIRMED.** (Filing cited `:12–21`; the
  bus line is `:11`, modes `:13-15` — a range approximation, not an error.) All three modes are
  write-and-wait; `:17` — "All three modes are **the same machine**… the **identical pointer
  line** into the **identical record**, drained by the **identical grep-and-check loop**." So
  the filing's claim that a `consult` mode is a **fourth channel of the same bus** rather than a
  new skill is well-founded, and it is the single-home-correct read.
- `skills/vlt-dispatch/SKILL.md:21` — "the Librarian never *pushes* into another partner's
  private memory (`identity.md`/`thread.md` are per-partner and off-limits)." **CONFIRMED
  exact.**
- `skills/vlt-dispatch/SKILL.md:225` — drain-loop step 2, "**Act on each** in your own voice and
  your own memory — fold it into your `thread.md`/working record…". **CONFIRMED exact.**

**The filing's load-bearing rebuttal is verified and should be carried into any brief.** The
naive reading of `:21` appears to forbid a stateful consult. It does not: `:21`'s prohibition is
on one partner **pushing into another's** memory, and `:225` establishes that the receiving
partner writes its own. In a consult the summoned partner **is the one running**, so it writes
its own memory — the same self-write the drain loop already prescribes. `:21`'s own framing
("**Two writers, cleanly separated**") holds. Recording this explicitly because, as the filing
notes, the naive reading blocks the feature outright.

**⚠️ CITATION CORRECTION.** The filing attributes to `vlt-review-council/SKILL.md:11–13` the
line about lenses being "independent reads — they don't see each other's positions." That text
is at **`vlt-review-council/SKILL.md:41`** (inside the workflow-behavior paragraph). `:10` is
the adjacent "**fixed lenses** applied in parallel… A moderator, who holds no stance" framing.
Both support the filing's point — council is a panel, not a conversation — but the line is `:41`.
Similarly, the "pass **live absolute paths** to ground in" pattern the filing calls council's
"Step-1 discipline" is at **`:35`**, in the Step-2 invoke block
(`subject: <question + context + live paths to ground in>`), not Step 1. Neither correction
changes the argument.

**The governance pairing is the filing's strongest content and grounds cleanly.** A handshaked
`{conventions}/consult.md` carrying `version:`/`consumers:` (per the build-4 handshake
discipline) declaring artifact **preconditions**, paired with a `vlt-lint` check for artifacts
claiming out-of-authority domain with no consult record. Two independent reasons to take it
seriously: it is squarely in the enforcement-arc idiom, and **a required consult is exercised
by construction** — which is the direct answer to the shipped-but-unexercised scar Part 3
names (capability families, and now `adoption_first_instance:` itself). The filing's
recommendation — *do not ship the mechanism without at least planning the convention + lint
pairing* — is carried into ideation as filed, not ruled on here.

**Two items the filing marks as shipping independently of the mechanism**, both verified as
pure prose with zero machinery: (1) a contract prohibition — *a partner never speaks in another
partner's voice; it consults, or it cites*; (2) the read-and-cite fallback as documented
default, which works today and supplies the trigger rule for the real mechanism — **spawn only
when the interaction should be remembered**. Note (2) is load-bearing for scoping: memory is
what justifies the consult's cost, so it is also the test for when *not* to build one.

**Explicitly deferred by the filing** (carried, not reopened): `dialogue` (A↔B for N turns) and
`convene` (true party-mode) — later *compositions* of the consult primitive; field traffic is
overwhelmingly single-question, and the roundtable already exists as `vlt-review-council`.
`summon` (answer to the human, caller overhears) — reduces to running the other partner's skill
directly; not a mechanism.

**Risks the filing says a brief must answer** (carried verbatim in substance): confabulated
authority from a thin payload — strictly worse than no mechanism, since read-and-cite cannot
impersonate; `thread.md` rot from unbounded consult appends; boundary erosion (the summoned
partner starting to *do* work, two writers in one turn); human-out-of-the-loop (two agents
converging visibly while a hedge is lost in digestion); and **upgrade durability — any
`dispatch.md` shape change is a B1 preserve-path question** for `vlt-setup`/`vlt-upgrade`/merge
scripts. The last is a standing-rule hit and is not optional.

**Registration surface a brief must not miss (grounding addition):** a fourth mode changes
`vlt-dispatch`'s public description in **three** places that must move together —
`vlt-dispatch/SKILL.md:4` (frontmatter description, "one routing record with…"), `:120` (the
Log/summary restatement), and `skills/vlt-setup/assets/module-help.csv:11` (the `DP` row, whose
free-text fields must stay quoted per the standing `module-help.csv` rule). The in-body mode
prompt at `:56` is a fourth.

**Provenance note:** filed by the **owner**, from `vlt-sayari` friction (Navigator + Engineer,
PM / staff-eng dynamic), out of a factory-side ideation session
(`_output/brainstorming/brainstorming-session-2026-07-25-1313.md`, gitignored). vlt-sayari is on
the work machine and was **not** read during grounding — the friction description is taken as
filed; every factory-side claim was verified here.

### A3-23. `linkage_ripe` cannot see graduation (2026-07-25) — `…162416-linkage-ripe-cannot-see-graduation.md`

**GAP CONFIRMED — and grounding makes the root cause *stronger* than filed.** This is the
run's most consequential filing: it is a **graded acceptance failure**, not a candidate, and
build-20's closure now depends on it. Every cited site verified exact:

- `skills/vlt-lint/SKILL.md:83` — `linkage_ripe` is the **union projection**: frontmatter
  `topic:` overlap with a wiki page **∪** an inbound body `[[wikilink]]` from ≥1 wiki page **∪**
  a shared `sources:` overlap with a wiki page; the same line states the calibration target
  (~21–23% union vs ~69–79% naive) and that "**a naive-level false-positive storm is the
  failure signature**." **CONFIRMED verbatim** — the filing's failure signature is the module's
  own words, not the auditor's gloss.
- `…/conventions/frontmatter.md:136` — research notes are "written-once… **No `last_updated`**"
  and hold no back-pointer. **CONFIRMED exact.**
- `…/conventions/frontmatter.md:138` — `revisit_after:` optional, absence-by-default.
  **CONFIRMED exact.** (Note `:138` also names `linkage_ripe` as the *other* surfacing path —
  the filing's "only candidacy **key**" phrasing is accurate, since `linkage_ripe` is derived,
  not stored.)
- `skills/vlt-ingest/SKILL.md:71-90` (Step 5) — writes the note; **CONFIRMED** that nothing in
  Steps 6–9 stamps a note as consumed when it graduates. Step 9's attestation (`:153`) covers
  "every page created or updated" — the research note is never re-touched.
- `skills/vlt-lint/SKILL.md:43` — the research-candidacy pass runs **inline** in the SKILL, not
  fanned out. **CONFIRMED exact**, which is the basis for the filing's honest-limit #2.

**The structural claim is verified end-to-end.** Graduation (`vlt-ingest` Step 6) writes a wiki
page that cites the note's sources (`:121-122`), shares its topics (`:117-119`), and links it
into the graph (`:131`). Nothing stamps the note. So the union's components are, precisely, the
residue graduation leaves — the projection cannot distinguish *ripe* from *already graduated*
because **no state on disk says "this note already graduated."** Missing state, not a bad
threshold. The filing's framing is exactly right.

**⚠️ Grounding discovery — one of the three union components has no shipped writer at all.**
`vlt-ingest` Step 6 never writes a wiki→research `[[wikilink]]`: the page template (`:107-124`)
has no such field, and the Connections section (`:131`) is specified as "`[[wikilinks]]`" among
pages. Cross-layer links are only ever **tolerated** by lint, never authored — `vlt-lint:41`
passes `crossLayerSlugs` "so a valid cross-layer link isn't reported as a missing target," and
`:59` exempts them from `missing targets`. So on a vault where no human hand-wrote such a link,
`linkage_ripe` is effectively a **two-component** projection, and **both** surviving components
(`topic:` overlap, `sources:` overlap) are pure graduation residue. That is a sharper root cause
than the filing's "all three are residue": the third isn't residue, it's **absent**.

This matters for the fix. The filing's cheapest suggested direction — *derive graduated-ness
instead of storing it, by treating "a wiki page whose `sources:` names this note" as the
signal* — has **no reliable substrate**: `vlt-ingest:121-122` populates a page's `sources:` with
"every source that has contributed," which for an ingest is the **external** source, not the
research-note path. (The one exception is the hand-off branch at `:73`, where the note *is* the
source.) The union's own `sources:`-overlap component confirms this reading: it matches note
and page on *shared external sources*, which is only meaningful if the page cites the external
source rather than the note. Ideation should therefore treat "derive it" as **needing its own
grounding pass**, not as the cheap option — and should weigh it against the arc's standing
**derive-first invariant** with that cost in view.

**Honest limits carried forward verbatim in substance (the filing states three, all material):**
1. **The 41-hit list was not preserved.** The finding rests on the vault's own verification of
   the set, not a re-derivable enumeration. A fix build **must re-run the projection and capture
   the list before changing anything.**
2. **How it was computed is not fully established.** `vlt-lint:43` says the pass runs inline,
   but the session grouped this class alongside genuine *delegate* measurement errors (7 false
   over-length summaries, 55 cross-layer link artifacts from a bad `crossLayerSlugs` invocation);
   whether an agent computed the union is unknown. **What was verified is
   computation-independent:** every surfaced note had already graduated — no measurement-rule
   error produces that.
3. **The 21% → 100% gap is unexplained and is the sharpest open question.** The A3-8 calibration
   that produced ~21% was measured on **this same vault** on 2026-07-11. The filing's leading
   hypothesis is that the calibration sample **excluded already-graduated notes** — i.e. it
   measured the projection against the population it was *hoped* to run on rather than the one
   it actually runs on. A fix build **must re-read the A3-8 calibration method before trusting
   either number.** Grounding did not attempt to resolve this and does not resolve it here — but
   note the shape: this would be **acceptance discharged against a non-adopting population**,
   the exact failure A3-17 named and this doc recorded at `:1196-1200`. Fourth instance of that
   class if it holds.

**What the check got right, preserved so a fix doesn't over-correct (as filed):** the
flag-for-human posture held under a 41-candidate load — the run surfaced and **did not act on**
any of them, and the human caught the class before promotion. `never auto-promote`
(`vlt-lint:82`) is the only reason this cost nothing. **Any fix must preserve it.** Note this
clause **discharged** on the same run.

**Ledger consequence (already recorded above; restated as capture):** build-20's
*FP-rate-tracks-calibration* clause is **FAILED** — exercised and failed, not waiting. Its three
sibling clauses discharged on the same run. **Build-20 now closes on the fix for this defect,
not on any further lint run.** That makes A3-23 the one run-3 filing with an Arc-3 dependency,
against its own stated "natural home: Arc 4" — see the arc-boundary question in *Open design
questions — capture run 3*.

**Vault-drift ruled out at source:** the filing states vlt-core's `vlt-lint/SKILL.md` is
byte-identical to factory (`diff -q`, this run). Consistent with everything grounded above —
the defect is in module source and reaches every install.

### Open design questions — capture run 3 (carried verbatim, NOT resolved here)

Per the grounding methodology, questions the filings deliberately left open are carried, not
answered. Ideation owns these.

1. **(A3-23, the filing's own "sharpest open question")** Why did the A3-8 calibration measure
   ~21% on the same vault that now measures ~100%? Leading hypothesis: the calibration sample
   excluded already-graduated notes. **Unresolved — and a fix build must re-read the A3-8
   calibration method before trusting either number.**
2. **(A3-23)** Where does graduation state live — stamped by `vlt-ingest` at Step 6 (a
   `graduated:`/`graduated_into:` key, costing a `frontmatter` version bump + full consumer
   walk), derived from wiki state (cheaper, but inference, and grounding shows the substrate is
   weaker than the filing assumed), or an inverted union (the filing rates this least likely to
   work)? **The acceptance clause it must satisfy is unchanged: FP rate tracking the ~21–23%
   union calibration on a live, mature research zone, measured after the fix.**
3. **(A3-19 / cross-cutting)** Does `adoption_first_instance:` get its first consumer in this
   work, and **where does that consuming check live**? `frontmatter.md:242` deliberately leaves
   this open ("whatever checks consume it… live where those checks live") and states the facet's
   absence is **not** a lint finding — so the consumer cannot be a lint absence-check without
   revisiting that sentence.
4. **(A3-19)** Fix the key, or fix the class? The filing's shapes 1 and 2 are explicitly
   non-exclusive — 1 fixes `revisit_after:`, 2 fixes every optional key the module ships.
   Grounding raises the stakes on 2 (the facet has zero instances today) and widens 1 (it must
   land in **both** research-note writers, not just `vlt-research`).
5. **(A3-20)** Is the `handled`/`unhandled` split replaced by an `open`/`deferred` split
   (shape 1), given a drain (shape 2), given a disposition on the callout (shape 3), or bounded
   (shape 4)? Shapes 1+2 are complementary per the filing — 1 makes the report honest, 2 gives
   the newly-visible half an owner. **The filing explicitly does not propose its four-bucket
   triage as a taxonomy.**
6. **(A3-20)** Should `vlt-lint:69`'s documentation instruction be bounded at all, and if so by
   what — top-N by severity, or an explicit judgment call so skipping becomes a **stated
   outcome** rather than silent under-delivery? (This sweep flagged 25 and documented 0.)
7. **(A3-21)** Prevent at ingest (entity cross-check before writing), catch at lint (entity
   collision across pages), codify in convention (a grounding-sufficiency rule), or reframe the
   shipped caveat (mangling vs substitution)? Filing rates 1+3 complementary and 4 as
   "whatever else ships." **Open: whether shape 1's entity pass is affordable at ingest scale.**
8. **(A3-22)** Does the consult mechanism ship at all without its governance pairing? The filing
   recommends **not** — "do not ship the mechanism without at least planning the convention +
   lint pairing" — but marks it a recommendation for capture to weigh, not a ruling.
9. **(A3-22)** Do the two zero-machinery items (the contract prohibition *a partner never speaks
   in another partner's voice*; read-and-cite as documented default) ship **independently and
   sooner**, even if the channel is deferred? The filing says they are shippable prose worth
   landing either way.
10. **(A3-18)** Does the mint's persona-authoring beat gain a temporal-specificity clause at all,
    given the evidence is 1-of-3 instances on one vault-local partner, and the module's own
    persona prose is verified clean? **Or is this purely a vlt-core fix with no module residue?**

### ⚖️ The arc-boundary question (new this run — owner-live)

**All six filings name Arc 4 as their natural home.** Arc 3 is shipped at v0.7.0 and gated only
on closeout. But **A3-23 is on build-20's closure path**: build-20's FP-rate clause is graded
FAILED, and the ledger now records that build-20 "closes on the Arc-4 fix of this defect rather
than on any further lint run." That is a live contradiction in the arc's own bookkeeping — an
**Arc 3** build whose acceptance discharges only via an **Arc 4** build.

This capture does not resolve it (it is an ideation/closeout ruling, and it interacts with the
pending build-19 tick-or-carry decision the ledger already flags). It states the two coherent
options so the owner can rule:

- **(a)** Arc 3 opens one more build for the A3-23 fix, closing build-20 inside its own arc.
  Cost: the arc grows a sixth build and a second release after it was declared shipped.
- **(b)** Build-20's FP-rate clause is carried forward into Arc 4 as an inherited acceptance
  debt, and `arc-closeout` records it as such. Cost: Arc 3 closes with a known-failed clause,
  which is precedent the closeout rubric may not currently sanction.

**Grounding note relevant to the choice:** whichever way it goes, ODQ #1 and #2 above mean the
A3-23 fix is **not a small build** — it needs a calibration re-read, a preserved 41-hit
baseline, and a schema-vs-derive decision with a weak derive substrate. Sizing it as a quick
patch to close an arc would repeat the mistake that produced the failed clause.

---

## Cross-cutting threads

- **One root cause, five layers.** Every filing is the same Five-Whys terminus ("vault
  state lives in prose, so nothing can count, trigger, or trip") attacked at a different
  layer: doctrine (091004), substrate (091003), write-time telemetry (091005),
  page-announced state (091006), contract class (091001), and the factory's own release
  boundary (091002). The arc's name is 091004's rule.
- **The derive-first invariant is arc-wide law.** Recorded in 091003 for *all* enforcement
  work: no mutable stored counters — derived or append-only state only (Plan B: an
  append-only events file folded at read time). 091005's attestation frontmatter is
  explicitly a second *derivable* surface, not a stored counter; 091001's
  `spec_notification_missing` is derivable read-only from the dispatch record. Any build
  in this arc proposing a stored counter is wrong by ruling, not by taste.
- **One `frontmatter@3` bump, one consumer walk.** 091004 (enforcement + deferral keys,
  on convention files), 091005 (attestation keys, on artifacts; + vlt-research becomes a
  consumer), and 091006 (`review_after`, on wiki pages) land as a single version bump.
  `review_after` is defined once (091006's definition; 091004's deferral references it).
  The metric vocabulary is defined once (091003's `metric` ids; 091004's
  `enforcement_counter` references them). Grounded current state for the walk:
  frontmatter@2 pinned by vlt-ingest + vlt-lint; vlt-extract, vlt-research, vlt-mint gain
  pins or blocks per their filings.
- **Two hard sequencing gates.** The spec convention lands before the next partner mint
  (091001 — the third consumer is the fork point; vault-side it's already the blocking
  pre-step). The packaging lint lands before the 0.6.0 tag (091002 — and 0.6.0 is the
  target release for the frontmatter@3 batch, so the lint plausibly ships first or
  alongside).
- **Three cross-filing decide-once questions** (flagged in multiple filings; resolve at
  ideation before any build lands them twice): (a) where module-owned executable code
  lives in an installed vault (091003 proposes `{root}/.claude/hooks/`; 091005/091002 may
  also ship scripts); (b) where notification-drift/aging enforcement lives — lint finding
  vs dispatch-ledger computed line vs tripwire (091001 Q3, 091006 Q4 both lean the same
  way: lint/dispatch find, tripwires nag); (c) whether lint may attest/own moments it
  doesn't currently own (091005 Q3; 091004's honesty note that `moment: lint run` is
  unowned until 091003's lint-debt wire lands).
- **Grounding surfaced a small defect cluster the filings only partially flagged, all in
  the durability machinery**: no divergence net for shipped skill assets (091004 latent
  bug 2 — templates clobbered silently on upgrade); no overlay-subsumption/retirement pass
  (091006 latent bug 2 — the upstream rail's missing return leg); overlay-blind consumer
  activations (091006 latent bug 1, corrected to ingest+extract); the opt-in coherence
  check (091004 latent bug 3); `_agent/dispatch.md` having no logical path name (grounding
  addition to 091001). These are all B1-durability-posture adjacent — worth grouping at
  ideation.
- **The factory eats its own dogfood.** 091002 is 091004's doctrine applied to this repo's
  release boundary — and its open question 4 proposes retroactively declaring the packaging
  lint as that boundary's `checked_by`, making the module repo the doctrine's first fully
  `checked` boundary.

### Cross-cutting threads — capture run 2 addendum (2026-07-17)

The six-filing threads above stand as written. The eleven new filings add these:

- **⚠ The arc's stated blocker rests on a false premise.** A3-12's central claim is refuted
  and this doc discharges the contradicting evidence four lines above the reclassification
  (`:644-651` vs `:653`). **Arc-closeout's block must be re-ruled before anything else in
  this run is ideated** — it may not exist.
- **Checks verify shape, never content — the run's unifying finding.** Acks verify *pins*
  (`vlt-research:3` acks `frontmatter@3` while `:65` contradicts it); verification greps
  search for the *ack* not the *consumption* (build-15's `spec@` grep, self-confirming,
  missed `vlt-upgrade:75`); prose asserts facts about the shipped surface that nothing
  re-reads (`extraction.md:47`/`:121`, false since v0.4.0, falsified by a commit that
  correctly didn't bump). **The coherence machinery cannot catch this class today.** Whether
  that is build-17's remit or a new one is an owner call — but note build-17 derives metrics
  from *event records*, and **these are absences**.
- **⚠ Acceptance can discharge against a non-adopting population.** Build-11's check #1
  named dog-trainer + health-coach and was discharged against wearers minted after the drift
  (A3-17). **This plausibly explains build-15's dry spec tail identically** — and it means
  *the deferred acceptance ledger itself has a soundness gap*. Candidate rule: **an
  acceptance check that names specific live artifacts is not dischargeable by substitutes.**
  Worth an explicit ruling; it would change how this arc's remaining tails are read.
- **Three filings' central claims were REFUTED, all by reasoning from a wrong module
  self-description** (A3-12, A3-14, A3-17). Not filer error — see Part 2. **Consequence for
  process: briefs must cite grounded verdicts, never filing headlines**, and the filings'
  own titles are actively misleading in two cases.
- **A second misattribution class: vault-local history narrated as module history.** A3-14's
  "relic of the retired registry table" never happened in module source (`git log -S` →
  empty; the table was vlt-core-local) — and A3-14 *corrects an earlier fabrication before
  committing a subtler version of it*. A3-15 is the general form: **a user ruling at upgrade
  time currently updates nothing but the ledger** — not the decision log (A3-15), not the
  governing prose (A3-14). **Both were found by the same mint, on the same day, walking the
  same broken trail.** They are separable (different surfaces, different fix classes, only
  A3-14 carries a handshake) but share this root — put the generalization to the owner.
- **Two build-15 residues argue for treating build-15 follow-up as a unit:** the
  unregistered `spec@1` consumer (A3-12) and the contract table's missing `specs` row
  (A3-10) — both scope omissions of the same build, both invisible to its own verification.
- **The durability net has an instruction that attacks it.** A mint obeying `vlt-mint:152`
  classifies itself as shipped at `vlt-upgrade:33` and voids its own B2 restore (A3-16).
  **B1-posture adjacent, and the first filing to hit the *instruction* rather than the
  *net*** — builds 6 and 18 both hardened the net only.
- **The cheapest item in the arc is a one-word fix nobody filed.** `vlt-research:65` scalar
  → list (A3-7). It manufactures the `topic:` raggedness two calibration filings blame on
  field data (55/92 vlt-core notes), blocks `cluster_ripe`, makes a shipped ack false, and
  needs no enforcement. **Ship it regardless of what happens to the graduation queue.**
- **The graduation-queue cluster's design premise did not reproduce in either vault.** A3-7
  predicted true orphaning; A3-8 and A3-9 independently killed its projection spec on
  opposite vault profiles (79% / 69% false-positive), and A3-9 found **throughput**, not
  orphaning, as the work vault's actual loss. **What survives: the union projection
  (double-validated), `revisit_after` as the cheap rail, `linkage_ripe`, defer
  `cluster_ripe`, trivial backfill.** Grounding also found `vlt-lint-full.js` has **no
  research read path at all** — scope that honestly before briefing.
- **`frontmatter@4` already has ≥3 parked keys from two arcs** (091006's `source_type:` /
  `review_note:`; A3-7's `revisit_when:`) plus A3-7's two candidacy keys. Build-16's
  precedent was "one coordinated bump, one consumer walk — NOT split." **Whoever opens `@4`
  inherits the batch**, and the walk is wider than A3-7 states (`vlt-extract`, `vlt-mint`
  too; exit-gated at `vlt-mint:141`).
- **Deferral without tracking is its own failure.** A3-13 was surfaced in June, captured
  into Arc 1's roadmap **as a note rather than an item**, and parked across three arcs — in
  archived trees the standing rules forbid appending to, so it had **no live home** until
  now. This is one rung up from the adoption-gap thread: **a surfaced defect whose deferral
  nothing tracks.**

### Cross-cutting threads — capture run 3 addendum (2026-07-25)

- **The adoption-gap thread now has a fourth instance — and it is the remedy itself.** Runs 1–2
  traced *a well-specified location whose adoption nothing measures* through `spec.md`'s
  `deferral_metric` (A3-12) and loop profiles (A3-17). Run 3 adds `revisit_after:` (A3-19,
  0-of-96) and `contradictions_handled:` (A3-20, a bucket that only grows and is labelled
  health). The thread's punchline this run is that **build-20's `adoption_first_instance:` facet
  — the arc's own general answer to this class — is carried by zero of the seven shipped
  conventions** (`frontmatter.md:237`/`:242` declare it; nothing uses it), including the
  `spec.md` its own prose names as the example. The remedy joined the disease.
- **A new sibling thread: the *noise storm*, the silent zero's mirror.** A3-23's `linkage_ripe`
  (41 hits, 0 real) fails in the opposite direction from every prior instance — not
  *non-adoption reading as clean* but *a working posture reading as a broken detector*. Both
  defeat the same faculty: **a human's ability to read the report as signal.** Any fix framed as
  "add an adoption facet" addresses only half the class.
- **Verification-by-residue.** A3-23's root cause generalizes past `linkage_ripe`: the module
  repeatedly measures a state by looking for **the traces that state leaves**, where those
  traces are also what the *completed* action leaves. Run 2 named the ack-vs-content version of
  this (a handshake that verifies the pin, never the conformance — A3-7/A3-12). A3-23 is the
  data version. Worth naming before Arc 4 designs another derived signal: **derive-first is
  sound only where the derivation distinguishes the two states.**
- **Two filings, one symptom, two causes — and the module can't tell them apart.** The
  Jonah/Alaric Jackson wiki contradiction is A3-20's evidence for a *disposition* defect and
  A3-21's evidence for a *source-fidelity* defect. Both readings are correct. The deeper point
  is that `vlt-lint` reports it as a **knowledge** problem when it is a **provenance** problem,
  and nothing downstream can re-route it. Brief them apart; read them together.
- **The bells that never rang vs. the bell that rang wrong.** The arc's acceptance story through
  pass 5 was "the bells work and mostly haven't rung." Pass 6 broke that framing: `linkage_ripe`
  rang, loudly, and was **wrong**. The distinction `arc-closeout` must now carry is three-way,
  not two-way — a tail waiting on a clock (091006), a tail waiting on an event nothing can cause
  (build-15), and a clause **exercised and failed** (build-20's FP rate). Only the third
  requires a build to close.
- **The run's one candidate answers the run's one scar.** A3-22's governance pairing — a
  handshaked `consult.md` whose preconditions make a consult **required**, plus a lint check for
  artifacts claiming out-of-authority domain with no consult record — is the only proposal in
  three capture runs that is *exercised by construction*. Whether or not the consult channel
  itself is ruled in, that property is what Arc 4 should be shopping for.
- **Provenance discipline is uneven across the field, in a legible way.** A3-21 cites a
  vault-local capability and an improvised wiki-index rule and **explicitly marks both as
  unshipped**, correctly. A3-18 cites a vault-local minted partner as **shipped module prose**,
  incorrectly, and builds its whole class on that. Same vault, same week, opposite outcomes. The
  lifecycle's answer is already correct — grounding at capture is exactly the step that caught
  it — but it is the second run in a row where a filing's central claim was overturned, and
  ideation should keep treating filing self-classification as a hypothesis.

---

## Open design questions — capture run 2 (carried verbatim, NOT resolved here)

Per the grounding methodology, these are ideation's to rule on. Grouped by filing; grounding
notes are marked and are context only, never resolutions.

**A3-7/A3-8/A3-9 (graduation queue):**
1. **K (cluster threshold) default.** *Grounding note: both calibrations independently argue
   `cluster_ripe` shouldn't ship in the first cut at all, which would moot K.*
2. **`topic:` consistency for clustering — RE-OPENED by grounding.** A3-8 answers "too
   ragged, gate it"; grounding shows the raggedness is a module defect (`vlt-research:65`),
   so the answer may change once the substrate is fixed. **Gate-then-fix or fix-then-measure
   is live and unsettled.**
3. **Ingest-probe scope:** any shared `topic:` vs most-specific? *A3-8's per-note vs
   per-source axis is orthogonal and does not answer it.*
4. **Where does an aging queue escalate — lint promotion or enforcement-kit tripwire?**
   *Grounding note: this is the **third** filing to raise it; the module already states a
   position for the review queue at `vlt-lint:62` ("escalation of an aging queue is a
   tripwire concern, not lint's"), and `:474-475`/`:500`/`:516` bind it to build-17. A
   precedent exists; extending it to the graduation queue is the owner's call.*
5. **`review_after` (wiki) vs `revisit_after` (research) as near-homophones** — explicitly
   "maintainer's call."
6. **Scan surface: research-zone-only vs widened to handoffs/threads.** A3-9's framing is
   binding on the *process*, not the answer: *"either widen … or ship research-zone-first
   and name the wider surface as the known second cut — **but decide it, don't default into
   it**."*

**A3-10 (dev zone):**
7. **Extensible tool-zone class vs. a named `dev/` row.** *Grounding reframed the option set
   (`:81` hardcodes "two top-level folders" — a completeness list); it does not choose.*
   Use the **actual** boundary rule from `vlt-sayari/CLAUDE.md:38` ("not a content layer"),
   **not** the filing's "read-only for partners" misreading.
8. **Should a hand-transcribed third copy of a map whose SSoT is `module.yaml:41-43` exist
   at all?** (Raised by grounding.)

**A3-11 (sayari evidence):**
9. **§4a wording and placement** — `vlt-upgrade:31` (framing) or `:41` (the snapshot/ledger
   seam)? One sentence, or does the invariant deserve a named rule with a lint check?
10. **Generalization scope of derive-first** — stated once as arc-wide law with pointers, or
    restated per layer? *Single-home says the former; the roadmap implies but never ruled it.*
11. **F3's discharge criterion on sayari** — the ledger needs "a named write op" and declines
    to infer; **neither the filing nor the ledger names which op would count.**

**A3-12 (spec advocate):**
12. **Does `frontmatter.md`'s enforcement declaration need an adoption/first-instance facet
    alongside its violation facet?** *(Filing `:63-64`, carried verbatim. Grounding: the
    filing's strongest point, and a poor fit for build-17 — an adoption metric measures an
    absence; there is no event to count.)*
13. **If a reflex lands at the handoff write path, how does it route back to the owning
    partner without breaching the deliberate "dispatch never authors them" firewall
    (`vlt-dispatch:41`)?**
14. **(New, grounding) Is upgrade-cadence origination sufficient, or does the class need a
    steady-state trigger?** I.e. is the real defect "no advocate" or "advocate on too slow a
    clock"?
15. **(New, grounding) Does `vlt-upgrade:75` "encode the rule" (→ must join `spec.md`
    `consumers:` + ack `spec@1`) or merely "point at the single home" (→ no ack)?**
    **Precedent-setting for the pointer-vs-ack line generally.**
16. **(New, grounding) Is zero-specs-at-9-days a gap signal at all**, given both observed
    candidates were human-judged not-specs?

**A3-13 (one lens):**
17. **Was `['architect']` for the roster-changing kinds a deliberate cost decision, or a stub
    never filled in?** *(The filing's §5, verbatim.) Grounding evidence for the ruling: the
    line originates in Build #2 (`28a197c`); `archive/build-2-mint-and-council-brief.md`
    **contains no rationale for panel composition anywhere**; no other brief or roadmap has
    one; the line has never been edited since origin (build-7 added kinds around it — with
    comments — and left it untouched). **Evidence is consistent with either reading. The
    maintainer is the only one who knows, which is precisely the filing's point.***
18. **(New, grounding) Should proposal B's widening semantics be reconciled with `:27`'s
    documented narrowing semantics, and what happens at the `:90` cap?**

**A3-14 (extraction grant):**
19. **Was the 0.3.0 invariant model intended to REPLACE per-op authorization entirely, or to
    sit UNDER a still-live naming gate?** *(Filing §6, verbatim.) **Grounding sharpens but
    does not settle it, and materially shifts the evidence:** the filing's inference toward
    *replace* rested on the retired-table narrative, **which grounding refutes** — that
    support is gone. The naming clause is original, deliberate v0.3.0 text at `version: 2`,
    never amended, never bound to a table → reads toward **under**. And **vlt-sayari's
    overlay treats it as live and satisfies it** → also **under**. **This is an owner ruling;
    the evidence has moved against the filing's recommended §4 and toward its stated
    alternative.***

**A3-15 (upgrade rulings):**
20. **Should `vlt-upgrade` invert from "refresh and report" to "prove the history survived"**
    — refusing to proceed when the decision log records gated convention edits it cannot
    account for? *(Filing §4D, offered "as a question, not a recommendation." Inverts the
    posture at `:101`; would change the stated contract at `:101`/`:129`.)*
21. **(New, grounding) Given the module already has two supersession idioms
    (`wiki-supersession.md:50-55`, `spec.md:47-48`), does the decision log get a third
    bespoke one, or does supersession become a governance-wide convention all three
    consume?** *The second is more coherent and considerably more expensive.*
22. **(New, grounding) Does the migration sweep, or merely prompt?** The filing states "One
    found. Nobody has swept for others." Interacts with (20).

**A3-16 (mint Step 4):**
23. **Did an upgrade revert the health-coach manifest registrations, or was
    `decision-log.md:64` aspirational?** *Unestablished; module history cannot discriminate
    (no divergence net existed at 0.4.0/0.5.0). The filing's "either way, same fix" holds.*
24. **How should a vault-local mint be DELIBERATELY upstreamed into the module — what is the
    sanctioned path, and does it belong in `vlt-mint` at all or in a separate contribution
    ceremony?** **No module-source home exists today.**
25. **(New, grounding) Should `vlt-upgrade:33`'s shipped-vs-local classifier be hardened
    against a polluted `agents[]`, or is fixing the instruction sufficient?** *A defensive
    fix makes the net robust to any mis-registration, not just this instruction's.*

**A3-17 (loop profile):**
26. **Is "a shipped location with no adoption check" a recurring class worth a general
    answer** — and if so, is this an instance of Q12 rather than a separate item?
27. **Which rail: a `vlt-lint` detection check, a `vlt-upgrade` gated migration offer, both,
    or neither — and does a detector need a roster-level "should wear" declaration to check
    against first?**
28. **✅ RULED 2026-07-17 (owner) — see the Owner ruling block below.** *(Original question:
    should an acceptance check that names specific live artifacts be dischargeable by
    substitutes? Reframed on grounding: the defect is not naming but **vacuity** — build-11
    check #1 is a class check ("a vertical partner, e.g. …"), so naming would not have bound
    it; what failed is that it was discharged against an instance that could not have failed.)*

---

## Owner rulings — capture run 2 follow-up (owner-steered, 2026-07-17)

The ideation-rulings block further down is dated 2026-07-06 and binds the original six
filings only; it is left untouched. This block records rulings the owner made on the run-2
findings. Briefs cite it; do not re-litigate.

**Gate 2 — RULED: a discharge must name an instance that could have failed ("no vacuous
discharge").** Reframed from "substitutes" to **vacuity**, because grounding showed
build-11 check #1 names no specific artifact — it is a class check ("*a vertical partner,
e.g. vlt-core's Dog Trainer / Health Coach*"), so a naming rule would not have bound it.
The property that was missing is that the discharging instance **could have failed the
check**. Concretely:

- For a check on a **change of location or shape**, a valid discharge needs an instance
  that **predates the change** (or otherwise sits in the at-risk population). An instance
  created *after* the fix, from the fixed template, is **vacuous by construction** — it is
  the intended output, and its success tests the template, not the delta the build
  introduced.
- **Escape hatch (keeps substitution possible, kills the silence):** a vacuous instance may
  discharge a check *only* by an **explicit recorded owner ruling** re-scoping it — never by
  quiet substitution. Substitution stays available; it becomes visible.
- **This names a principle the ledger was already using.** build-15's migration-offer half
  and build-18's F2/F3 were both retargeted off vlt-core with the words "vacuous by
  construction" (`:1586`, `:1701`) — correct applications, now retroactively blessed. The
  ruling formalizes them.
- **Audit result — no hidden reopenings.** Re-reading the 07-17 pass under this rule: the
  three explicit "vacuous → retarget to vlt-sayari" discharges (build-15 retrofit, build-18
  F2) each landed on an instance that *could* have failed (a real handoff wrongly promoted;
  a 270-line overlay wrongly retired) and correctly didn't — **valid**. build-16 M4 cycle 2
  caught a live attestation bypass — **valid**. The **one** place the principle was not
  applied is build-11 check #1, discharged against `chess-coach` + Navigator (both minted
  post-fix, vacuous) — **and that is already reopened** via A3-17, whose drift finding is
  filed as `inbox/2026-07-17-100000`. So the ruling reopens nothing new; it explains why
  A3-17 is correct and gives the ledger the vocabulary it lacked.
- **Structural consequence for briefs:** a location/shape-change build owes **two** checks,
  not one — a *machinery* check (the fixed template produces a working artifact; a post-fix
  instance is the right evidence) **and** a *migration* check (the at-risk pre-fix
  population was carried over; only a pre-fix instance is valid evidence). build-11 shipped
  only the first, mislabeled as covering both by its "Zero migration" claim. Any A3-17 build
  must carry the migration check explicitly.

**Gate 1 — RULED 2026-07-17: the arc is NOT blocked.** The A3-12 refutation stands:
build-15's own F6 (`vlt-upgrade:75`) originates specs and fired correctly on vlt-sayari
(one candidate surfaced, offered, human-declined); empty `_agent/specs/` is a correct
negative, not unreachability. Consequences:

- `arc-closeout` does **not** inherit the BLOCKED status; the build-15 ledger item's
  07-17 BLOCKED-BY-DESIGN-GAP reclassification is vacated (annotated in place, history
  preserved).
- Build-15's consumer-lock/spec-bump tail **reverts to STILL-OPEN (first-exercise)** —
  discharging event: the first real spec minted in a live vault, exercising the lock/relay
  **non-vacuously per gate 2** (the discharging instance must be one that could have
  failed).
- The residual **cadence** gap (origination is gated to upgrade cadence, a rare owner-run
  event) is ordinary captured work — it routes to ideation with the rest of the run-2
  batch, not to an arc gate.

**Gate 3 — RULED 2026-07-17: *under*.** The 0.3.0 invariant model sits **under a
still-live per-op naming gate**. Grounding basis: C6 showed the naming clause is live
original design from v0.3.0 (the module never had a registry table), so the filing's
delete-as-relic recommendation (§4) loses its footing; the fix is the filing's
**alternative** shape:

- **Keep the naming requirement.** Future ops are named via the base (module-shipped ops)
  or the overlay route (`vlt-mint:131`, vault-local ops) — the gate stays satisfiable.
- **Name `vlt-track` in the base** — it is module-shipped and cannot rely on a vault-local
  overlay for its own authorization (the surviving core of C5).
- **Delete the false clause** ("no skill shipped with the module uses it") at **both**
  `extraction.md:47` and `:121`; state explicitly that per-*partner* authorization was
  retired at 0.3.0 while per-*op* naming remains.
- **Ceremony:** naming an op is a rule change — `version: 2 → 3`, consumer walk re-acks
  `[vlt-extract, vlt-lint, vlt-track]`.
- **Expected downstream (not a defect):** vlt-sayari's `extraction.overlay.md:13` becomes
  base-subsumed; build-18's subsumption pass will correctly offer its retirement at that
  vault's next upgrade.

---

## Proposed grouping (a PROPOSAL — owner steers at ideation, per Arc 1/2 convention)

| Build | Theme | Folds in | Why this grouping |
|---|---|---|---|
| **build-14 — packaging lint** | Factory boundary gets its bell | 091002 (script + fixtures + CLAUDE.md wiring; rides: the one-line `vlt-upgrade/SKILL.md:45` exclusion-list fix; delete the live `.pyc`) | Entirely factory-side, zero vault surface, hard-gates the 0.6.0 tag every other build targets. Carries the two owner rulings (tools/ tracked?; build numbering). Cheapest, ships first. |
| **build-15 — spec convention** | The contract class, before the fork | 091001 (spec.md + setup/dispatch/mint/contract touches + upgrade retrofit migration; lint checks explicitly deferred) | Hard-sequenced before the next partner mint; self-contained governance-bundle work. Ships with a declared-stage bell; adopts 091004's block formally when build-16 lands (or ships after it — owner sequencing call). |
| **build-16 — frontmatter@3: bell + attestation + freshness** | The one coordinated schema bump | 091004 (schema v3 + backfill stamps + templates + mint/council/lint) + 091005 (write-verification.md + three op refactors + lint tiers) + 091006 (`review_after` + lint `review_due` + workflow schema) | The three filings share one file, one version bump, one consumer walk, and cross-referencing key semantics — splitting them re-creates the three-uncoordinated-overlays failure mode they were designed to avoid. Big, but mostly additive prose + frontmatter. |
| **build-17 — enforcement kit (slices 0–3)** | The substrate | 091003 (vitals + tripwires + hooks provisioning + dispatch Tripped-wires + mint/council wire rule + `blocked_on` rider + contract grammar tighten) | Depends on build-16's vocabulary decisions (metric ids, `review_after`) and the hooks-home ruling; vault-side slices 0–3 evidence may still be maturing. Last, and can trail the 0.6.0 release if its evidence isn't in. |
| *(durability cluster — placement open)* | Upgrade-rail hardening | 091004 LB2 (skill-asset divergence net), 091006 LB2 (overlay-subsumption pass) + LB1 (overlay-aware activations), 091001 LB1/LB3 (move-safety, relay re-pointing) | Grounding surfaced these as one B1-posture cluster; owner decides whether they ride their parent builds or form their own small build. |

---

## Ideation rulings (owner-steered, 2026-07-06 — binding for all Arc 3 briefs)

Session ran via `bmad-module-builder` ideation against this doc; all rulings below are the
owner's, recorded verbatim in effect. Briefs cite this section, never re-litigate.

**Grouping & order — proposal ACCEPTED as-is:**
- **build-14 — packaging lint** (091002). Opens Arc 3 (not a standalone maintenance build).
- **build-15 — spec convention** (091001). Before the next partner mint; ships with the
  declared-stage bell prose, adopts 091004's formal block when build-16 lands.
- **build-16 — frontmatter@3 batch** (091004 + 091005 + 091006). One coordinated bump,
  one consumer walk — NOT split.
- **build-17 — enforcement kit slices 0–3** (091003). Trails the 0.6.0 release pending
  its vault-side slice evidence.
- **build-18 — durability cluster** gets its OWN build (not riding parents, not deferred
  to Arc 4): 091004 LB2 skill-asset divergence net, 091006 LB2 overlay-subsumption pass +
  LB1 overlay-aware activations, 091001 LB1/LB3 move-safety + relay re-pointing.

**0.6.0 release contents:** builds **14 + 15 + 16 + 18** ship in 0.6.0; build-17 trails
into 0.6.x/0.7.0. Rationale for pulling 18 forward: the divergence net and
overlay-subsumption pass must protect the 0.6.0 upgrade run itself — vlt-core's planned
local template edits would otherwise be silently clobbered by that very upgrade.

**091002 owner rulings:**
1. `tools/` is **tracked + public** — the enforcement tool is documentation of the release
   contract. Build-14 carries the one-line `CLAUDE.md:71` release-surface amendment.
2. Build numbering: **Arc 3 build-14** (the factory-side instance of the arc's doctrine
   belongs in the arc).

**Cross-filing decide-once rulings:**
1. **Module-owned executable code home:** `{root}/.claude/hooks/`, beside the
   `.claude/workflows/` force-reinstall precedent (`vlt-setup/SKILL.md:148-160`) — module
   owns it, overwrites on every install/update, vault never edits it. Applies to 091003's
   hooks and any 091005/091002-adjacent scripts.
2. **Notification-drift / aging enforcement:** **lint/dispatch find, tripwires nag.**
   Lint and the dispatch ledger compute findings (derived, read-only); the enforcement-kit
   tripwire registry is the sole escalation/nagging layer. One finder per fact, one nagger
   overall. Resolves 091001 Q3 + 091006 Q4 identically.
3. **Lint as attester/moment-owner: yes, narrowly.** Lint may write `verified_by` on files
   its auto-fix touched (otherwise Step 3 re-stales what it just validated); `moment: lint
   run` becomes a legitimate `checked_by` only once 091003's lint-debt wire makes the
   cadence real — until then, `checked` stamps citing lint stay honest-ceiling.
4. **`_agent/dispatch.md` path (091001 lint follow-on):** **accept the hardcoded read** —
   consistent with dispatch's own deliberate agent-zone treatment (`vlt-dispatch/SKILL.md:35-38`);
   no `dispatch:` logical name. The check hardcodes the path with a comment citing the precedent.

**Spike obligations before briefs are written** (lifecycle step 3: external unknowns get
spikes, read the actual source): build-16 must spike **Obsidian Bases date-filter syntax**
(091006 Q2 — `review_after <= today` is assumed, not verified) before the Due-for-review
documented-reference view is briefed; fallback already named (Horizon sorted-ASC + lint
`review_due` finding).
**→ SPIKE CLOSED 2026-07-06** (sources: live `vlt-core/_agent/bases/wiki.base` — real
filter-expression grammar (`type == "wiki"`, `status != "complete"`, per-view `filters:`
blocks, `sort:` as `property`/`direction` list) — plus the official Bases syntax
reference, help.obsidian.md/bases/syntax): date comparisons are supported; `today()` is a
**global function**, so the correct spelling is `review_after <= today()`, not the bare
`today` the filing assumed. The Due-for-review view also needs a key-presence guard
(`and: [review_after, review_after <= today()]`) since absence = evergreen must not match.
One residual caveat for the brief: if the property registers as text rather than a Date
type, wrap it — `date(review_after) <= today()`; the brief should spec the documented
reference view with the guard + `date()` wrap as the robust form. Fallback no longer
needed.

**Questions deliberately left to brief time** (per-build, not cross-cutting):
`verified:` vs `verified_at:` naming (build-16, one-shot — decide in the brief);
091004 v1 scope + overlay-boundary declarations + lens placement (build-16, recommendations
stand); 091002 group-A root scope + YAML posture + `skills[]` cross-check (build-14);
091003 `days_since_lint` display-only + `blocked_on` shape (build-17); 091001 carried-flag
scheduling + escalation trigger (build-15/17 seam); family-invariant encoding (after M4).

---

## Ideation rulings — A3-7..A3-17 (owner-steered, 2026-07-17)

Rulings below are the owner's; briefs cite this section, never re-litigate. Session
COMPLETE 2026-07-17 — every slot is ruled (none left open). The three capture-run-2 gates
are already RULED (2026-07-17) in the *Owner rulings — capture run 2 follow-up* block above
and bind this session; do not re-ask them here. The unresolved question pool for this batch
is *Open design questions — capture run 2* (Q1–Q27; Q28 ruled) — each question ends this
session either ruled below, or explicitly left to brief time, per build.

**Grouping & order — RULED 2026-07-17: clerk's derived proposal ACCEPTED AS-IS** (owner
chose clerk-drafts-I-amend mode; accepted without amendment). Binding grouping:

- **build-19 — build-15 follow-up unit.** A3-12 residuals: the spec-advocacy **cadence**
  (ruled to ride here, not build-17) + the `vlt-upgrade` → `spec.md` `consumers:` join +
  `spec@1` ack (per the pointer-vs-ack ruling). Plus A3-10: the contract table's missing
  `specs` row, and the dev-zone questions (Q7/Q8) — both touch the operating contract.
  Smallest; ships first.
- **build-20 — graduation queue, first cut; OPENS `frontmatter@4`.** A3-7/A3-8/A3-9,
  surviving shape only: union projection, `revisit_after`, `linkage_ripe`, defer
  `cluster_ripe`, trivial backfill; research-zone-first (wider surface = named second
  cut); rides the severable `vlt-research:65` one-word fix (fix-then-measure); scopes the
  missing `vlt-lint-full.js` research read path honestly. As @4 opener it inherits the
  parked batch (`source_type:`, `review_note:`, `revisit_when:` + candidacy keys) **and
  the adoption/first-instance facet** — one bump, one consumer walk (incl. vlt-extract,
  vlt-mint; exit-gated at `vlt-mint:141`).
- **build-21 — history-writes unit.** A3-14 (gate 3 executed: name `vlt-track` in base,
  delete the false clause at `extraction.md:47`/`:121`, `extraction@2→3` + consumer
  re-ack) + A3-15 (decision-log write path, bespoke supersession idiom, the general
  upgrade-ruling write path rule defined here) + A3-11's prose items (§4a invariant
  sentence, derive-first stated-once).
- **build-22 — mint & wearer surfaces.** A3-13 (panel composition) + A3-16 (fix
  `vlt-mint:152`; classifier hardening + upstreaming path at brief) + A3-17 (loop-profile
  migration — **carries the explicit migration check per gate 2**).
- **build-23 — content-verification.** The checks-verify-shape-never-content class (own
  build per ruling). Deliberately last — its shape benefits from watching builds 19–22's
  own verification passes.
- **build-17 — unchanged remit minus the two re-homed pieces** (adoption facet →
  build-20's schema bump; cadence → build-19). Still trails pending vault-side evidence;
  M0 debt re-read at its brief time.

Capture's observations that informed the draft, carried below for provenance (now
subsumed by the accepted grouping):

- The graduation-queue cluster (A3-7/A3-8/A3-9) survives grounding only as: union
  projection, `revisit_after`, `linkage_ripe`, defer `cluster_ripe`, trivial backfill —
  and `vlt-lint-full.js` has no research read path at all (scope honestly).
- `vlt-research:65` scalar → list is a one-word fix, correct on its own terms, ships
  regardless of the queue's fate, needs no ruling — but does need a build home.
- Two build-15 residues argue for a build-15-follow-up unit: the unregistered `spec@1`
  consumer (A3-12) and the contract table's missing `specs` row (A3-10).
- A3-14 and A3-15 share one root (vault-local history narrated as module history) but are
  separable — different surfaces, different fix classes, only A3-14 carries a handshake
  (`extraction@2→3` per gate 3).
- A3-16 is B1-posture adjacent — the first filing to hit the durability *instruction*
  (`vlt-mint:152`) rather than the net.
- Whoever opens `frontmatter@4` inherits the parked batch (≥3 keys from two arcs) and a
  wider consumer walk than A3-7 states.
- Capture flagged the adoption facet as a poor fit for build-17 (metrics count events;
  adoption is an absence) — "re-ideate ownership rather than inheriting it."

**Pre-ideation rulings the capture demanded** — the three gates are RULED (arc NOT
blocked; no vacuous discharge; A3-14 = under). Still flagged for ruling this session:

- **RULED 2026-07-17: this batch OPENS `frontmatter@4`.** The opening build inherits the
  full parked batch (091006's `source_type:`/`review_note:`; A3-7's `revisit_when:` + two
  candidacy keys) — one coordinated bump, one consumer walk (incl. vlt-extract, vlt-mint;
  exit-gated at `vlt-mint:141`), per build-16 precedent.
- **RULED 2026-07-17 (owner delegated to clerk's recommendation): research-zone-first.**
  The first cut scans the research zone only; handoffs/threads are named here as the known
  second cut — a recorded decision, not a default, satisfying A3-9's process bind (Q6).
- **RULED 2026-07-17: fix-then-measure.** The `vlt-research:65` scalar → list fix ships
  first; `topic:` raggedness is re-measured on post-fix data before any `topic:` gate is
  ruled on (Q2). A3-8's gate answer does not stand as-is.
- **RULED 2026-07-17 (owner delegated to clerk's recommendation): the spec-advocacy
  cadence residual rides this batch, NOT build-17** — attached to the build-15 follow-up
  unit if grouping creates one, so build-15's first-exercise tail never waits on
  build-17's evidence gate.

**Cross-filing decide-once rulings** — decisions that resolve the same question across
filings identically — all five RULED 2026-07-17:

- **RULED 2026-07-17: checks-verify-shape-never-content is a NEW item with its OWN
  build** — not folded into build-17's event-record machinery (these are absences, not
  events), not a lint extension by default (the build decides its checks' homes).
- **RULED 2026-07-17 (owner delegated to clerk's recommendation): `vlt-upgrade:75`
  ENCODES → ack.** It carries the spec-shaped detection heuristic and conforms frontmatter
  to the spec schema, so it must change when the rule changes: `vlt-upgrade` joins
  `spec.md` `consumers:` and acks `spec@1`. **Precedent (the pointer-vs-ack line,
  general):** a site that must change when the rule changes is a consumer and acks; a site
  that would survive any rule change unedited is a pointer and never acks (Q15).
- **RULED 2026-07-17 (owner delegated to clerk's recommendation): adoption facet is
  GENERAL, as a schema facet.** `frontmatter.md`'s enforcement declaration grows an
  adoption/first-instance facet (build-16's lineage, one class-wide answer for specs +
  loop profiles — Q12/Q26); whatever checks consume it live where checks live.
- **RULED 2026-07-17 (owner delegated to clerk's recommendation): supersession —
  bespoke now, converge later.** The decision log ships its own idiom this batch; the
  governance-wide supersession convention (wiki + spec + decision log as consumers) is
  recorded as a **named debt with a live home** — per A3-13's lesson, tracked deferral,
  never a note in a closable tree (Q21).
- **RULED 2026-07-17 (owner delegated to clerk's recommendation): the misattribution
  root gets a GENERAL write path.** One rule, defined once: an upgrade-time user ruling
  propagates to the decision log **and** any governing prose whose assertions it changes —
  never the ledger alone. A3-15 and A3-14 are its first two instances (fixes remain
  separable; only A3-14 carries the `extraction@2→3` handshake per gate 3).

**Spike obligations** — **RULED 2026-07-17: none for this batch** (owner confirmed;
capture flagged no external unknowns — grounding read actual sources throughout: sayari
vault files, git history, live lint reports). A later-discovered unknown reopens this
slot with a SPIKE OPEN entry before its brief is written.

**Evidence-debt dispositions** — RULED 2026-07-17 (owner confirmed; F3 per clerk's
grounded recommendation after the owner asked whether vlt-core could host it):

- 091003 M0 counter-accuracy audit + tripwire-hit data: **re-read at build-17 brief
  time** — not a standing tail (unpayable before its build ships; the brief resolves the
  circularity rather than inherits it).
- 091006 first review-cycle evidence: **not-blocking clock tail** — fires on its own,
  earliest trigger `spec.md`'s `review_after: 2026-08-17`.
- build-15 consumer-lock/spec-bump tail: **attached to no build.** Discharging event
  stays "first real spec minted in a live vault, non-vacuous per gate 2" — build-19
  improves the odds (cadence + registration) but cannot cause it.
- A3-11 F3 (Q11): **stays retargeted to vlt-sayari; vlt-core cannot discharge it** (zero
  overlays — vacuous by construction per gate 2; an overlay minted to test it would be
  engineered evidence). **The named write op is ruled now** so the work-machine session
  can capture it without a round-trip: *the next `vlt-extract` run on vlt-sayari
  post-0.6.0 that honors an overlay-only extraction rule unprompted* (extraction is that
  vault's one overlaid convention). Evidence arrives **by filing**, the route F2 already
  used (`2026-07-12-114940` §1); the cross-machine sync difficulty is acknowledged and
  absorbed by the filing route.

**Questions deliberately left to brief time** (per-build, not cross-cutting) — every
open-design question not ruled above, sorted into its build per the accepted grouping:

- **build-19:** dev-zone shape + the third-copy map (Q7/Q8); reflex routing vs the
  dispatch firewall (Q13); steady-state trigger mechanics for the cadence residual (Q14);
  zero-specs-at-9-days as a signal (Q16).
- **build-20:** K's default (Q1 — likely mooted, `cluster_ripe` deferred); ingest-probe
  scope (Q3); aging-queue escalation (Q4 — the `vlt-lint:62` precedent exists, extending
  it is the brief's call); `review_after`/`revisit_after` naming (Q5).
- **build-21:** §4a wording and placement (Q9); derive-first stated-once vs per-layer
  (Q10); upgrade-posture inversion (Q20); sweep-or-prompt for the migration (Q22).
- **build-22:** `['architect']` intent + widening semantics and the `:90` cap (Q17/Q18 —
  Q17 is owner-only, answered in that brief's session); health-coach manifest history
  (Q23 — unestablished, same fix either way); the sanctioned upstreaming path (Q24);
  classifier hardening vs instruction-only fix (Q25); drift rail choice + the
  "should wear" declaration (Q27).
- **build-23:** carries no numbered question — its scoping is the brief's whole job.

Ruled this session and no longer open: Q2, Q6, Q11, Q12, Q15, Q21, Q26 (plus Q28 and the
three gates, ruled 2026-07-17 in the blocks above).

---

## Ideation rulings — A3-18..A3-23 (owner-steered, 2026-07-25)

> **⇢ These rulings govern ARC 4 work.** The batch produced no Arc-3 build (arc-boundary ruling
> (b)). The Arc-4 roadmap — `skills/reports/inbox-evolution-arc4-roadmap.md`, stood up
> 2026-07-25 — carries the build plan, the inherited acceptance debt and a digest of these
> rulings. **This section remains the binding text**; the digest defers to it on any
> disagreement. This section travels to `skills/reports/archive/` at Arc-3 closeout and stays
> readable there — do not append to it after that move.

Rulings below are the owner's; briefs cite this section, never re-litigate. **Session OPEN —
every slot below is unfilled.** The unresolved question pool for this batch is *Open design
questions — capture run 3* (ODQ #1–#10) plus *The ⚖️ arc-boundary question*, both in the
*Capture — six filings* section; each question ends this session either ruled here, or
explicitly left to brief time, per build. A slot left empty is honest — do not fill it with a
guess, and do not let a brief infer one.

**Sequencing note (not a ruling):** the arc-boundary question is upstream of grouping — until
it is ruled, "which builds" cannot be answered, because option (b) means this batch has no
Arc-3 build at all. Rule it first.

**Grouping & order** — which builds, numbered, and which filings each folds in. Build
numbering is itself an owner call.

**RULED 2026-07-25: FIVE builds, one filing each — no combining.** A3-18 folds into **no build**
(vlt-core only, per the ruling below). All five are **Arc 4** builds, per the arc-boundary
ruling; none of them closes Arc 3.

- **A3-19 build — the adoption unit.** `revisit_after:` lands in **both** research-note writers
  (`vlt-research/SKILL.md:71` and `vlt-ingest/SKILL.md:77-91`, which omits the key entirely) with
  a two-outcome question, **and** `adoption_first_instance:` gets its first real consumer — where
  that consuming check lives is a brief-time call bounded by `frontmatter.md:242`. Carries the
  **general honest-reporting rule** ruled below (this build writes it; the other sites cite it).
- **A3-20 build — the contradiction drain.** Routing, not eligibility: `vlt-lint:105`'s catch-all
  already admits the class; what's missing is a second item template plus two pointers from `:69`
  and `:101`, and a disposition for the report's `handled`/`unhandled` split. Bounding `:69` is a
  brief-time question (this sweep flagged 25, documented 0).
- **A3-21 build — source fidelity.** Entity substitution at ingest: prevent / catch / codify /
  reframe, per ODQ #7. **Briefed apart from A3-20 despite sharing `vlt-lint`** — capture's
  explicit instruction, because the Jonah/Alaric pair is one symptom with two independent causes
  and one build would blur them.
- **A3-22 build — the consult channel.** Mechanism (a fourth `dispatch` mode) **plus** its
  handshaked `{conventions}/consult.md` + `vlt-lint` pairing, which do not separate. Carries the
  B1 preserve-path precondition and the four-site registration surface
  (`vlt-dispatch/SKILL.md:4`, `:56`, `:120`, `module-help.csv:11`). *The two zero-machinery prose
  items ship independently and sooner — see the open sequencing question below.*
- **A3-23 build — `linkage_ripe` / graduation state.** **Gated on both spikes**; sized on its own
  merits, never against an arc deadline. Carries the 41-hit baseline re-capture as a precondition
  and the deferred derive-vs-store call.
  <br>**⟳ Re-shaped 2026-07-25 by SPIKE-1:** the build's subject is a **polarity inversion**
  (`vlt-lint:83` fires the calibration's absorption signals as ripeness signals) plus a
  substituted union leg (`topic:` overlap for frontmatter citation), **not** missing graduation
  state. On that reading the fix needs no schema key and no `frontmatter@5` bump, and the build
  is likely the batch's *smallest*, not its largest. It also inherits a **reworded acceptance
  target** (an FP rate measured against an FP rate — see the ledger). Sizing stays unfixed until
  SPIKE-2 confirms the absorption test reproduces.

**Build numbering — RULED 2026-07-25: the series RESTARTS with an arc prefix.** Arc 4's builds
are **`A4-1` … `A4-5`**, not `build-24…28`; the continuous `build-N` series ends at build-23. The
arc boundary becomes legible in the build name itself, which the arc-boundary ruling makes
load-bearing (Arc 3 closes carrying an inherited debt against these builds). **`build-17` keeps
its legacy number** — it is an unbuilt Arc-3 build and is not renamed.

**Numbers follow SHIP ORDER**, per the Arc-3 convention (build-14 opened the arc, build-23 was
deliberately last). *Corrected 2026-07-25 (owner challenge): the first assignment numbered by
filing order, because ship order was deliberately deferred to the spikes — leaving numbers that
did not mean what the arc's own precedent says they mean. Renumbered once both spikes closed and
order was set; nothing had been briefed. Precedent kept from build-17: a number records intended
order **at assignment** — a build that later slips does **not** trigger a renumber.*

| Build | Filing | Notes |
|---|---|---|
| **A4-1** | A3-23 | `linkage_ripe` polarity. Ships first: smallest build, highest latent severity. **Carries the two A3-22 prose items** as the earliest-shipping build. |
| **A4-2** | A3-19 | Adoption unit; writes the general honest-reporting rule the later builds cite. |
| **A4-3** | A3-20 | Contradiction drain. |
| **A4-4** | A3-21 | Source fidelity. Briefed apart from A4-3. |
| **A4-5** | A3-22 | Consult mechanism + convention + lint pairing (prose already shipped in A4-1). Most gated; last. |

**The two A3-22 prose items — RULED 2026-07-25: they RIDE THE EARLIEST-SHIPPING BUILD.** The
contract prohibition (*a partner never speaks in another partner's voice; it consults, or it
cites*) and read-and-cite-as-documented-default attach to whichever build ships first — on the
current expectation that is **A4-2** — and **A4-5 stays purely mechanism + convention + lint**.
Rationale: A4-5 is the batch's most gated build, and tying two sentences to it would have
reversed the ship-sooner ruling by the back door. The earliest build's brief names them
explicitly as inherited scope so they cannot be dropped as off-theme.

**Ship order — SET 2026-07-25 (owner delegated to clerk's recommendation), both spikes closed:
`A4-1 → A4-2 → A4-3 → A4-4 → A4-5`.** A4-1 leads on the evidence, reversing the "probably last"
expectation this slot was created to avoid fixing prematurely: SPIKE-1/2 make it the batch's
**smallest** build (restore polarity + the citation leg; no schema key, no `frontmatter@5`, no
consumer walk) and its **highest-severity** one — the next ordinary `vlt-lint` run on vlt-core
surfaces ~97 of 98 research notes, so every day unfixed is a day the primary vault's lint output
is noise on that axis. A4-2 follows because it writes the general honest-reporting rule the later
builds cite. A4-5 sits last, gated by its convention + lint pairing.
<br>**Consequent placement of the two A3-22 prose items:** they ride **A4-1** as the
earliest-shipping build, per the rule as ruled. Recorded because the rule was written expecting
A4-2 to lead — the ship-sooner rationale is what governs, and A4-1 is sooner. If the owner
prefers thematic coherence over speed for two paragraphs of contract prose, pin them to A4-2
instead; nothing else depends on it.

*(Superseded framing, kept for the record: **RULED 2026-07-25: SPIKES FIRST, then order by size
once they close.**)* Both A3-23
spikes run **before any of the five builds is briefed** — they are reads, not builds, and nothing
blocks them. Order is then set with A4-1's real size known: it may deserve to run earlier than
last, and the one thing this session refuses to do is size it by assumption. Recorded as a
deliberate deferral with a live home (this slot), not an omission.

**Clerk's note — RESOLVED 2026-07-25: the Arc-4 roadmap is stood up.**
`skills/reports/inbox-evolution-arc4-roadmap.md` now carries the build plan (A4-1…A4-5 + ship
order), build-20's inherited FAILED clause with its restated target, the two spike digests, and
an Arc-4 acceptance ledger. It **points at** this section and the capture section rather than
copying them, so there is one binding home for each. `arc-closeout` therefore inherits a
pointer-check, not a migration: confirm the Arc-4 roadmap's references still resolve after this
document moves to `archive/`.

Capture's observations that bear on grouping, carried as **capture's material, unaccepted** —
none of these is a proposal, and run-3 capture deliberately made no grouping proposal:

- A3-20 (shape 3, contradiction disposition) and A3-21 (shape 3, entity-collision check) both
  land in `vlt-lint` — capture notes "ideation may want them in one build."
- A3-20 and A3-21 share one symptom (the Jonah/Alaric pair) with **two independent causes**
  (disposition vs source fidelity) — capture's explicit instruction is "**brief them apart**."
- A3-23 is "not a small build": ODQ #1 and #2 require a calibration re-read, a preserved
  41-hit baseline, and a schema-vs-derive decision on a weak derive substrate. Capture warns
  that sizing it as a quick patch to close an arc "would repeat the mistake that produced the
  failed clause."
- A3-18's module-side residual is at most one clause in the mint's persona-authoring beat;
  everything else in that filing is vlt-core work.
- A3-19's shape 2 is not "apply an existing facet" but "wire `adoption_first_instance:` for
  the first time" — larger and wider-paying than the filing scoped.
- A3-22 is the run's only **candidate** (a proposed capability), not a defect.

**Pre-ideation rulings the capture demanded** — seeded as questions, unanswered:

- **⚖️ THE ARC-BOUNDARY QUESTION (owner-live, capture's named first ruling).** All six filings
  name Arc 4 as their natural home, yet A3-23 sits on build-20's Arc-3 closure path (build-20's
  FP-rate clause is graded FAILED and now closes on the A3-23 fix, not on any further lint).
  Capture states two coherent options and resolves neither:
  **(a)** Arc 3 opens one more build for the A3-23 fix, closing build-20 inside its own arc —
  cost: a sixth build and a second release after the arc was declared shipped.
  **(b)** Build-20's FP-rate clause carries forward into Arc 4 as an inherited acceptance debt,
  recorded as such by `arc-closeout` — cost: Arc 3 closes with a known-failed clause, precedent
  the closeout rubric may not currently sanction.
  → **RULED 2026-07-25: (b) — carry forward into Arc 4 as an inherited acceptance debt.**
  Build-20's FP-rate clause stays graded FAILED and does **not** re-open Arc 3; `arc-closeout`
  records it as an inherited debt against Arc 4 rather than leaving it as an open Arc-3 tail.
  Arc 3 therefore closes at v0.7.0 with a known-failed clause, and the closeout rubric must
  sanction that shape (if it does not today, closeout's own handling of an inherited failed
  clause is the thing to fix — not this ruling). Consequence for grouping: **this batch has no
  Arc-3 build** — every A3-18..A3-23 build is an Arc-4 build, and the A3-23 fix is sized on its
  own merits (ODQ #1/#2), never against an arc-closing deadline.
- **The build-19 tick-or-carry decision** (flagged by the Deferred acceptance ledger; interacts
  with the arc-boundary ruling and `arc-closeout` needs it). Build-19 has no remaining
  sub-clause after the 07-25 release of its negative case: tick it, or carry it owner-carried.
  Not flipped unilaterally. → **RULED 2026-07-25: TICK IT — build-19 is DISCHARGED.** The
  released empty-specs negative case is a standing watch `arc-closeout` carries separately, not
  an outstanding sub-clause; build-19 is no longer a closeout gate.
  <br>*Clerk's note on the seeding:* this slot was seeded as pending from the frontmatter
  `status:` line, but the **ledger had already recorded the tick** at the build-19 entry
  ("✅ TICKED — OWNER RULED 2026-07-25 (full-lint pass)", `- [x]`). The ruling above **confirms**
  that entry rather than newly deciding it; the frontmatter's "one owner decision is pending"
  sentence is stale and should be corrected at the next status write.
- **A3-18 — module residue or none at all?** (ODQ #10) Does the mint's persona-authoring beat
  gain a temporal-specificity clause, given the evidence is 1-of-3 instances on one vault-local
  partner and the module's three shipped personas are verified clean — or is this purely a
  vlt-core fix with **no module change at all**? → **RULED 2026-07-25: NO MODULE CHANGE —
  vlt-core only.** The filing's remedy is a correct fix applied to the wrong repo; it lands in
  vlt-core as a `## Self`-tier or rebirth-tier edit to that minted partner. A3-18 therefore
  **folds into no build** and carries no module residue — the mint's persona-authoring beat
  gains no temporal-specificity clause on 1-of-3 evidence against verified-clean shipped prose.
  The capture entry closes as vault work. (If the hazard recurs on a *shipped* persona or a
  second vault, it re-files fresh; it does not sit as a silent debt here.)
- **A3-22 — does the consult mechanism ship without its governance pairing?** (ODQ #8) The
  filing recommends **not** ("do not ship the mechanism without at least planning the
  convention + lint pairing") but marks it a recommendation, not a ruling. → **RULED 2026-07-25:
  NOT WITHOUT THE PAIRING — the filing's recommendation is adopted as a ruling.** The `consult`
  mechanism does not ship unaccompanied by its governance pairing: a handshaked
  `{conventions}/consult.md` carrying `version:`/`consumers:` (build-4 handshake discipline)
  declaring artifact **preconditions**, plus a `vlt-lint` check for artifacts claiming
  out-of-authority domain with no consult record. Rationale recorded: **a required consult is
  exercised by construction** — the direct answer to the shipped-but-unexercised scar, which now
  has four instances including `adoption_first_instance:` itself. A brief may sequence
  convention-then-mechanism, but may not ship the mode with the pairing merely "planned."
- **A3-22 — do the two zero-machinery items ship independently and sooner?** (ODQ #9) The
  contract prohibition (*a partner never speaks in another partner's voice; it consults, or it
  cites*) and read-and-cite as documented default are shippable prose either way.
  → **RULED 2026-07-25: YES — both ship INDEPENDENTLY of the mechanism, and sooner.** The
  contract prohibition and read-and-cite-as-documented-default are pure prose that work the day
  they land; they are **not** held behind the channel. Consequence, recorded because it bears on
  grouping: with the mechanism now gated on its convention + lint pairing, the channel is the
  long pole — tying the prose to it would have meant a long wait for two sentences. Read-and-cite
  also supplies the mechanism's own trigger rule (**spawn only when the interaction should be
  remembered**), so shipping it first hands the later channel its affordability test rather than
  inheriting it.

**Cross-filing decide-once rulings** — decisions that resolve the same question across filings
identically:

- **`adoption_first_instance:` — first consumer, and where the consuming check lives** (ODQ #3,
  capture-marked cross-cutting). The facet is declared, has zero instances across all seven
  shipped conventions (including `spec.md`, the example `frontmatter.md:242` itself names), has
  no consumer, and by `:242`'s own prose its absence is **not** a lint finding — so the consumer
  cannot be a lint absence-check without revisiting that sentence. Does this batch wire it?
  → **RULED 2026-07-25: YES — this batch wires it** (carried by the A3-19 scope ruling below;
  same decision, recorded once). **Where the consuming check lives is LEFT TO BRIEF TIME** — but
  the brief inherits a hard constraint, not a free choice: `frontmatter.md:242` states the
  facet's absence is **not** a `vlt-lint` finding, so the first consumer either lives outside
  lint, or the brief revisits `:242` explicitly and says so. It may not quietly contradict it.
- **Fix the key, or fix the class?** (ODQ #4) A3-19's shapes 1 and 2 are non-exclusive: 1 fixes
  `revisit_after:` (and must land in **both** research-note writers — `vlt-research:71` **and**
  `vlt-ingest:77-91`, which omits the key entirely), 2 fixes every optional key the module
  ships. → **RULED 2026-07-25 (owner delegated to clerk's recommendation): fix the key in BOTH
  writers **and** wire the adoption facet.** Concretely: (a) `revisit_after:` plus a two-outcome
  question lands in `vlt-research/SKILL.md:71` **and** `vlt-ingest/SKILL.md:77-91` — the ingest
  template omits the key entirely and is the majority write path, so a `vlt-research`-only fix
  leaves the 0-of-96 mechanism intact; (b) `adoption_first_instance:` gets its first real
  consumer in this work. Reasoning recorded: the facet shipped as the arc's own answer to the
  shipped-but-unexercised scar and is itself the scar's fourth instance (zero of seven
  conventions carry it, including `spec.md` — the example `frontmatter.md:242` names), and this
  session has already leaned on *exercised-by-construction* as the answer to that scar in the
  A3-22 pairing ruling; wiring it here keeps that posture consistent rather than adding a fifth
  declared-and-unused surface. **The filing's shape 3 (the `vlt-lint:84` report line
  distinguishing "no candidates" from "no note ever carried the key") is NOT scoped separately
  here** — it is an instance of the general honest-reporting rule ruled in the silent-zero
  decide-once below, and conforms to that rule rather than being briefed as its own A3-19 item.
  **Left to brief time:** *where* the consuming check lives (ODQ #3) — see the next ruling.
- **The silent-zero / noise-storm class** — A3-19 (`revisit_after` 0-of-96), A3-20
  (`contradictions_handled` only grows, labelled health), A3-23 (`linkage_ripe` 41/0) and the
  older `deferral_metric` scar are one class per *Cross-cutting threads*. Is there one
  decide-once answer (a general honest-reporting rule, per build-23's `vlt-lint:74` honest-limit
  precedent), or three per-site fixes? → **RULED 2026-07-25: ONE GENERAL RULE, STATED ONCE.**
  A single honest-reporting rule covers the class — *a count whose only attainable value is
  "fine" must state what it cannot see* — and each site conforms to it rather than inventing its
  own wording. This is the single-home posture applied to reporting; the cost the owner accepted
  is a governance decision about **where the rule lives**, which is left to the brief that
  writes it (build-23's `vlt-lint:74` honest-limit is the shipped precedent to extend, not
  necessarily the home). Known conformers at ruling time: `revisit_after`'s 0-of-96 (A3-19
  shape 3), `contradictions_handled`'s only-grows count (A3-20), `linkage_ripe`'s 41/0 (A3-23),
  and the original `deferral_metric` scar (A3-12). **Consequence for scoping:** none of these
  sites briefs its own bespoke report-line fix; they cite the rule.
- **Verification-by-residue** (capture's generalization of A3-23's root cause beyond
  `linkage_ripe`): does this batch state a general invariant — a check must not infer state from
  the residue of the process it is checking — or stay instance-local? → **RULED 2026-07-25
  (owner delegated to clerk's recommendation): STATE IT, but as a BOUNDARY CLAUSE ON DERIVE-FIRST
  — not as a new standalone invariant.** Wording to the effect of: *derive-first does not license
  deriving a state from the residue of the very process that produces it — where the only
  available signal is the process's own leavings, the state must be recorded, not inferred.*
  Reasoning recorded, because this is a middle path between the two options as put:
  - Against a standalone new law: there is **one** confirmed instance, and the arc has an
    explicit standing ruling against pre-generalizing from one (the "do NOT pre-generalize
    contracts" pressure-test ruling). Four instances earned the silent-zero rule; one does not
    earn its own invariant.
  - For stating it anyway: derive-first is **arc-wide law**, and A3-23 is the first case where
    obeying it literally produces the defect. Left unstated, the next build reads derive-first
    and re-derives the same mistake. Stated as a scoping clause, nothing new is legislated — an
    existing law gains the boundary it was always missing.
  - It is **load-bearing now**, not hypothetical: ODQ #2 (where graduation state lives) is
    exactly a derive-vs-store call on a substrate grounding already showed is weak, and this
    clause is what makes that call answerable without re-litigating derive-first.
  **Reversible:** if the owner prefers the pure instance-local option, strike this and fix
  `linkage_ripe` alone — nothing else in the session depends on it. **Interaction flagged:** this
  partly shapes the still-open *derive-first vs A3-23's weak substrate* ruling below, which is
  deliberately left open rather than treated as settled by this one.
- **The derive-first invariant vs A3-23's weak substrate.** Arc-wide law says derive, don't
  store; grounding shows the derive substrate here is weaker than the filing assumed
  (`vlt-ingest:121-122` populates a page's `sources:` with the *external* source, not the
  research-note path). Does the invariant bend for this case, and if so is the exception stated
  once and generally? → **RULED 2026-07-25: DELIBERATELY LEFT OPEN — deferred to the A3-23 brief,
  after both spikes close.** Recorded as a deferral with a live home, not an omission: ruling
  derive-vs-store now would decide it on exactly the grounding that produced the failed clause.
  The frame the brief inherits is already fixed — the **boundary clause on derive-first** ruled
  above, plus the unchanged acceptance target (FP rate tracking the ~21–23% union calibration on
  a live, mature research zone, measured after the fix), which SPIKE-1 may itself put in
  question. The brief states the call explicitly; it may not arrive at derive-or-store by default.
  <br>**⟳ SPIKE-1 update 2026-07-25 — the tension may dissolve rather than need resolving.** The
  calibration never derived graduated-ness: it tested **absorption** (no linkage ⇒ ripe) and
  measured ≈0% FP across two vaults. If SPIKE-2 confirms that reproduces, derive-first holds
  unbent, nothing is stored, and this slot closes without an exception. The **boundary clause on
  derive-first still stands on its own merits** — the general hazard (inferring state from a
  process's own residue) is exactly what the inverted check does, and stating it is what stops
  the next build re-deriving it. Ruling still deferred to the A4-1 brief.

**Spike obligations** — external unknowns needing a read-the-actual-source spike before a brief;
each carries **SPIKE OPEN** until a dated **SPIKE CLOSED** record replaces it.

- Capture flagged **no external unknown** for this batch — all grounding read module source and
  live vault state directly. No third-party-source spike is open.
- **RULED 2026-07-25: BOTH internal grounding obligations are SPIKES — they run BEFORE the
  A3-23 brief is written**, not as its opening section. Reasoning recorded: neither is an
  external unknown, but both are read-the-actual-source obligations whose answers change *what
  the build is* — if the calibration excluded already-graduated notes, the ~21–23% target the
  acceptance clause names is itself suspect, and a brief written against a suspect target
  repeats the failure that produced the failed clause.

  - **SPIKE OPEN — re-read the A3-8 calibration method** (ODQ #1). Why did A3-8 measure ~21% on
    this same vault on 2026-07-11 while the 07-25 full lint measures ~100%? Leading hypothesis:
    the calibration sample **excluded already-graduated notes** — i.e. it measured against the
    population it was *hoped* to run on rather than the one it runs on. Must establish: the
    actual sample and method, and whether the ~21–23% acceptance target survives. If the
    hypothesis holds, this is the **fourth instance** of acceptance discharging against a
    non-adopting population (A3-17's class, recorded at `:1196-1200`) and that finding is part
    of the spike's output. Closes with a dated **SPIKE CLOSED** record naming its sources.

    **→ SPIKE CLOSED 2026-07-25** (sources read: the live vlt-core audit artifact
    `{field-vault}/_agent/artifacts/research-wiki-audit-2026-07-11.md`
    `:4`, `:13-21`, `:69`, `:91`; `inbox/2026-07-11-153000-…field-calibration.md` §1 + Provenance;
    `inbox/2026-07-12-114837-…sayari-calibration.md:16-26`; `inbox/2026-07-11-114226-…queue.md:49`;
    roadmap A3-8/A3-9 captures; `skills/reports/build-20-graduation-queue.md:8-9`, `:210-216`,
    `:330-332`; shipped `skills/vlt-lint/SKILL.md:83-84`.) **The hypothesis is REFUTED and a
    different, larger defect is established in its place.**

    1. **Excluded-population hypothesis — REFUTED.** The audit sampled **all 90 notes**, and
       already-graduated notes were emphatically in-sample: `:13-21` records 76 **fully
       absorbed**, and the headline finding *is* that 49 of 62 naive-flagged notes were absorbed
       anyway. Nothing was excluded. **This is NOT a fourth instance of discharging against a
       non-adopting population** — see the retraction at the evidence-debt slot below.
    2. **`~21–23%` was never a false-positive rate.** Four numbers with three denominators:
       **79%** = FP rate *of the naive orphan signal* (49/62 absorbed, audit `:19`); **69%** =
       vlt-sayari's naive *flag rate over population* (9/13, `…114837:18`); **21%** = vlt-core's
       union residual as a *share of the naive flagged set* (13/62, audit `:69`); **23%** =
       vlt-sayari's union *flag rate over population* (3/13, `…114837:20`). The union's actual
       measured FP rate was ≈**0%** — the residual 13 "contains every genuine gap" (`:69`) and
       13 is exactly the genuine-gap set (8 partial-ingest + 5 orphaned-ripe, `:13-21`).
       **Therefore build-20's acceptance clause is unsatisfiable as written** — it asks an FP
       rate to track a set-reduction ratio. Reworded at the ledger; see below.
    3. **The real root cause is a POLARITY INVERSION — and it is not what A3-23 diagnosed.** In
       both calibrations the union is an **absorption test**: frontmatter citation ∪ body
       wikilinks ∪ shared-source overlap = evidence a note is *already absorbed* ⇒ **exclude**.
       A note was ripe when it had **no** linkage. The sayari filing states this in terms
       (`:22-26`): the shared-source leg is "the durable/project-state split working as designed,
       **not orphaning**." Shipped `vlt-lint:83` fires those same signals with the polarity
       flipped — ripe **when** the union hits — so it surfaces precisely the set the calibration
       excluded as false positives. That predicts 41 hits / 0 real exactly, with no appeal to
       missing state.
    4. **Two further drifts ride along:** `topic:` overlap was substituted for the calibration's
       **frontmatter-citation** leg (the audit used topic overlap only in its Phase-0 index,
       `:4`, never in the recommended union, `:69`); and the name came from A3-7's `linkage_ripe`
       (`…114226:49`), which meant a third thing again — *a newer note cites/links this orphan*.
       The shipped check matches neither source definition.
    5. **Where it entered — not the capture.** The roadmap's A3-8 capture is correct ("~79%
       false-positive… the union (frontmatter ∪ body wikilinks ∪ shared-source overlap) is what
       should ship"), claims no union FP number, and names the right legs. Both the mislabel and
       the inversion appear first at **`build-20-graduation-queue.md:211-216`** and ship verbatim
       into `vlt-lint:83`. `vlt-lint:83`'s parenthetical ("deliberately distinct from `orphans`,
       which means the *opposite*") shows the tension was noticed at build time and resolved in
       prose **in the wrong direction**, cementing the inversion.

    **Consequence for A4-1 — it is probably SMALLER, not larger, than sized.** A3-23 reasoned
    from the inverted check to "graduation state must be stored" (schema bump + full consumer
    walk). The calibration's own polarity needs **no graduation state**: absence of linkage *is*
    the signal, measured at ≈0% FP on real data across two opposite-profile vaults. If that
    reproduces, the fix is **restoring polarity + the citation leg**, not `frontmatter@5` — and
    the derive-first invariant does not bend. The A4-1 brief may not assume either sizing until
    SPIKE-2 reports.
  - **SPIKE OPEN — ground the derive-graduated-ness option** (ODQ #2). Capture: treat "derive
    it" as **needing its own grounding pass**, not as the cheap option — `vlt-ingest:121-122`
    populates a page's `sources:` with the external source, not the research-note path (the
    hand-off branch at `:73` being the exception). Must establish whether any reliable substrate
    for derived graduated-ness exists at all. Feeds the deferred derive-first ruling above.
    Closes with a dated **SPIKE CLOSED** record naming its sources.
    <br>**⟳ REFRAMED 2026-07-25 by SPIKE-1 (still OPEN, and still gating).** The question is no
    longer "can graduated-ness be derived?" — SPIKE-1 shows the calibration never derived it,
    it tested **absorption** and inverted the result. The reframed obligations: (a) does the
    absorption test still reproduce on today's vlt-core research zone (98 notes, vs 90 at
    calibration) — i.e. re-run the union in the **calibration's polarity** and check the residual
    against hand-verification; (b) does an implementation read the legs the audit found
    load-bearing — **body wikilinks** and **prose Sources entries** (audit `:69`) — or only
    frontmatter, which is the leg the audit measured at ~79% FP alone; (c) only if (a) fails,
    the original derive-vs-store substrate question. Note (a) **would subsume the A4-1 41-hit
    baseline precondition** — running it captures the enumeration for free. Pulling that
    precondition forward into the spike is **offered, not ruled** *(owner to decide)*; absent a
    ruling it stays attached to A4-1.

    **→ SPIKE CLOSED 2026-07-25** (sources: live vlt-core read-only re-run over
    `_agent/research/*.md` (98) × `_agent/wiki/*.md` (131) in both polarities, enumeration
    preserved at `skills/reports/spike2-projection-baseline-2026-07-25.md`;
    `_agent/sessions/2026-07-25-150500-lint.md:26`, `:52`;
    `_agent/artifacts/research-wiki-audit-2026-07-11.md:34-56`, `:69`; `vlt-lint/SKILL.md:83`.)

    1. **The absorption test REPRODUCES.** Calibration polarity on today's zone surfaces **8 of
       98** (8% of population, **14% of the naive set** of 59) against the audit's 13 of 90 (14%
       of population, 21% of naive). Same order, slightly tighter — the projection the
       calibration validated still works on a zone grown by 8 notes and drained by a manual pass.
    2. **It tracks the drain, which is the property that matters.** Of the audit's five
       hand-verified `orphaned_ripe` items, the **four that were since graduated** (ashwagandha,
       wispr-flow, youtube-to-markdown, kettl routing failure) now read **absorbed ⇒ correctly
       excluded**; the **one never drained** (`…world-cup-group-stage…` → the still-unbuilt
       `fifa-world-cup-2026` page) still surfaces. The shipped check surfaces **all** of them,
       drained or not. Same notes, same disk, opposite behavior — this is the polarity defect
       demonstrated rather than argued.
    3. **Shipped polarity re-run: 97 of 98 surface (99%), of which 90 are already absorbed
       (≥93% FP).** Seven of the eight genuine candidates are inside that set, so the check has
       recall and ~8% precision — it is not blind, it is undiscriminating.
    4. **⚠ THE 41 WAS AN UNDERCOUNT, AND THE SAME RUN DESTROYED THE CAUSE.** The 07-25 lint
       surfaced 41 `linkage_ripe` (`:26`) — and **exactly 41** of the then-96 notes carried a
       list-form `topic:` at candidacy time, because the same sweep auto-fixed **55 scalar
       `topic:` → YAML lists** (`:52`, build-20's own F1 fix). The scalar cohort's topics were
       unreadable to the overlap leg, silently damping the projection. **All 98 notes are now
       list-form**, so the next `vlt-lint` run on vlt-core surfaces ~97, not 41. The graded
       failure is **latent and ~2.4× worse than measured**, and it worsens by design as the fix
       that caused it was the correct fix.
    5. **The legs, as asked:** the shipped check reads body wikilinks (as a *ripeness* leg) and
       shared `sources:`, but has **no frontmatter-citation leg at all** — the audit's absorption
       legs fire at shared-source 71, wikilink 64, **citation 39**, and the citation leg is the
       one the module dropped in favor of `topic:` overlap. Nothing shipped addresses the audit's
       **prose Sources entries** (`sources:` holding human prose, not paths).
    6. **Derive-vs-store — RESOLVED toward DERIVE (recommendation to the A4-1 brief).** No
       graduation-state key is needed: absorption is computable from disk today, at 8% surfacing,
       and it tracks the drain. **Derive-first holds unbent**; the deferred cross-filing ruling
       can close without an exception. The boundary clause still earns its keep — it is what
       names the inverted check as the hazard.

    **Honest limits.** (a) The candidacy pass is **prose-specified and agent-run**, not code —
    this re-run *models* it faithfully but is not the same computation; the exact 41↔41 list-form
    correspondence is strong corroboration, not proof. (b) The 8-note ripe set is **mechanical
    only** — no 9-agent hand-verification as in the audit; three of the eight map to
    audit-identified items (world-cup `orphaned_ripe`, fiddleheads seasonal-orphan, the
    taste-interview terminal scaffold), which supports precision without establishing it.
    (c) **vlt-core only** — vlt-sayari unreadable from this machine. (d) The original 41-hit
    enumeration is **permanently unrecoverable**; the preserved artifact is a current-state
    baseline, and A4-1's precondition must be re-read in that light.

  **Ordering note (not a ruling):** SPIKE-1 can invalidate the target SPIKE-2's options are
  measured against; running 1 first is the cheaper order, but both must close before the brief.

**Evidence-debt dispositions** — each debt attached to a build, or ruled not-blocking.
**RULED 2026-07-25: six not-blocking, two attached.** The six honest limits below are carried
into their briefs as **context, not tails** — they create no standing acceptance debt and
nothing waits on them. The two hard obligations are **preconditions on their builds** and a
brief that omits either is incomplete: (i) the A3-23 41-hit baseline re-capture, (ii) the B1
upgrade-preserve-path check on any `dispatch.md` shape change. Marked per item below.

- **A3-23 honest-limit #1 — the 41-hit list was not preserved.** The finding rests on the
  vault's own verification, not a re-derivable enumeration. Capture: a fix build **must re-run
  the projection and capture the list before changing anything**. → **ATTACHED — precondition on
  the A3-23 build.** The projection is re-run and the hit list preserved as a baseline artifact
  *before* any change lands; a brief without this step is incomplete.
- **A3-23 honest-limit #2 — how the union was computed is not fully established**
  (`vlt-lint:43` says inline; whether an agent computed it is unknown). What was verified is
  computation-independent: every surfaced note had already graduated. → **NOT BLOCKING** —
  carried into the A3-23 brief as context. (SPIKE-1 may establish it incidentally; it is not that
  spike's obligation.)
- **A3-23 honest-limit #3 / ODQ #1 — the 21% → 100% gap is unexplained**, and if the
  excluded-population hypothesis holds it is the **fourth instance** of acceptance discharging
  against a non-adopting population (the class A3-17 named, recorded at `:1196-1200`).
  → **NOT BLOCKING as a debt — it is SPIKE-1's subject** (see Spike obligations). The
  fourth-instance finding, if it holds, is part of that spike's output.
  <br>**❌ RETRACTED 2026-07-25 by SPIKE-1 — the fourth-instance finding does NOT hold.** The
  A3-8 audit sampled **all 90 research notes** with 76 already fully absorbed *in sample*
  (`research-wiki-audit-2026-07-11.md:13-21`); no population was excluded, so this is not an
  instance of A3-17's discharge-against-a-non-adopting-population class. The class still has
  three instances, not four. **The gap is fully explained without it:** ~21% and ~100% are not
  the same measurement — the first is a set-reduction ratio under an **absorption** test, the
  second an FP rate under an **inverted ripeness** test (SPIKE-1 §2–§3). Recorded as a retraction
  rather than a silent edit because this finding was cited in the capture (`:1686-1694`), in
  ODQ #1, and in the ledger; those sites state it as a hypothesis and are left standing as
  written — **this record supersedes them.**
- **A3-19 — one vault, four post-fix notes.** vlt-sayari unreadable from the factory machine;
  4/4 post-fix plus 92/92 legacy is a small post-fix sample for "partners never elect it."
  Mechanism is not broken — this is adoption/visibility. → **NOT BLOCKING** — carried into the
  A3-19 brief as context. The fix does not wait on a second vault or a larger post-fix sample.
- **A3-20 — one vault, one sweep (130 pages).** Size-sensitive by nature; a 30-page vault may
  have no complaint. The four-bucket triage is the Librarian's hand-work, **not** a proposed
  taxonomy. → **NOT BLOCKING** — carried into the A3-20 brief as context, including the explicit
  instruction that the four buckets are **not** a proposed taxonomy.
- **A3-21 — the substitution table's right-hand column is inference, not verification.** No
  roster source was consulted; **nobody has verified the Jonah/Alaric pair either way**; three
  firings in one source family sizes a pattern, not a rate; the other five episodes were not
  audited. → **NOT BLOCKING** — carried into the A3-21 brief as context. The brief may not cite
  the substitution table's right-hand column as verified fact.
- **A3-22 — vlt-sayari was not read during grounding.** The Navigator/Engineer friction is taken
  as filed; every factory-side claim was verified here. → **NOT BLOCKING** — carried into the
  A3-22 brief as context; the friction description stands as filed.
- **A3-18 — 1-of-3 attribution.** Instances #1–2 predate the persona line and are ordinary
  invented-continuity, already forbidden by shipped rules. → **MOOT** — A3-18 folds into no
  build (ruled above); the debt closes with it.
- **A3-22 — B1 upgrade-durability question.** Any `dispatch.md` shape change is a preserve-path
  question for `vlt-setup`/`vlt-upgrade`/merge scripts. This is a **standing-rule hit and is not
  optional** — attach it to whichever build touches the bus. → **ATTACHED — precondition on the
  A3-22 build** (and on any later build that changes `dispatch.md`'s shape). The B1 local-mint /
  preserve-path re-check across `vlt-setup`/`vlt-upgrade`/merge scripts is named in the brief,
  not discovered at implementation.

**Questions deliberately left to brief time** (per-build, not cross-cutting) — fillable only
once grouping names builds:

**Sorted 2026-07-25 per the accepted grouping** (build ids per the A4-N table above):

- **A4-2 (A3-19):** where the `adoption_first_instance:` consuming check lives (ODQ #3, bounded
  by `frontmatter.md:242` — outside lint, or revisit `:242` explicitly); the wording and home of
  the general honest-reporting rule; the two-outcome question's shape in both templates.
- **A4-3 (A3-20):** `handled`/`unhandled` vs `open`/`deferred`, drain, callout disposition, or
  bounding (ODQ #5 — shapes 1+2 are complementary per the filing); whether `vlt-lint:69` is
  bounded at all and by what (ODQ #6 — this sweep flagged 25, documented 0).
- **A4-4 (A3-21):** prevent at ingest / catch at lint / codify in convention / reframe the
  shipped caveat (ODQ #7), including whether an entity pass is affordable at ingest scale.
- **A4-5 (A3-22):** the consult mode's payload shape and the convention's preconditions; the
  five risks the filing named (confabulated authority, `thread.md` rot, boundary erosion,
  human-out-of-the-loop, B1 durability — the last is a precondition, not a question).
- **A4-1 (A3-23):** derive-vs-store (ODQ #2), decided in the brief after both spikes, against the
  boundary clause on derive-first; the acceptance clause is unchanged unless SPIKE-1 unseats it.

Unsorted pool as it stood at session start, retained for provenance: **#1, #2** (A3-23 — calibration gap; where graduation state
  lives, with the acceptance clause unchanged: FP rate tracking the ~21–23% union calibration on
  a live mature research zone, measured after the fix); **#5, #6** (A3-20 — `handled`/`unhandled`
  vs `open`/`deferred`, drain, callout disposition, or bounding; and whether `vlt-lint:69` is
  bounded at all, given this sweep flagged 25 and documented 0); **#7** (A3-21 — prevent at
  ingest / catch at lint / codify in convention / reframe the shipped caveat; open sub-question:
  whether an entity pass is affordable at ingest scale); plus **#3, #4, #8, #9, #10** if not
  ruled in the cross-filing and pre-ideation blocks above.
- **Registration surface a brief must not miss** (grounding addition, A3-22): a fourth dispatch
  mode moves `vlt-dispatch/SKILL.md:4`, `:56`, `:120` and
  `skills/vlt-setup/assets/module-help.csv:11` (`DP` row, free-text fields stay quoted) together.

**Session COMPLETE 2026-07-25 — every slot is ruled.** Ruled this session and no longer open:
the ⚖️ arc-boundary question (b), build-19 tick-or-carry (tick), ODQ #10 (A3-18 → no module
change), ODQ #8 (A3-22 not without its pairing), ODQ #9 (A3-22 prose ships independently),
ODQ #3 + #4 (A3-19 fixes key **and** wires the facet; check location left to brief), the
silent-zero decide-once (one general rule), verification-by-residue (a boundary clause on
derive-first), both spike obligations (SPIKE OPEN ×2, before any brief), all eight evidence-debt
dispositions, grouping (five builds, A4-1…A4-5), build numbering (arc-prefixed restart), the
A3-22 prose home (earliest-shipping build), and ship order (spikes first, then by size — the
one deliberate deferral, with this slot as its home).

Two rulings were **owner-delegated to the clerk's recommendation** and are marked as such at
their slots — A3-19's scope and verification-by-residue's framing. Both are reversible; nothing
downstream depends on them except A4-1's derive-vs-store call, which is deferred anyway.

Still open by design (not omissions): ship order; where the honest-reporting rule lives; the
`adoption_first_instance:` check's home; derive-vs-store. Each has a named home above.

---

## Deferred acceptance ledger (Arc 3)

Per Arc 2 convention, acceptance rides the next ordinary vlt-core upgrade; per-build
checks appended at brief time. Standing items:

> **⚖️ CLOSEOUT DISPOSITIONS — 2026-07-26, owner-ruled batch. This block is the single home
> for every item's final disposition; the per-item annotations below carry a one-line pointer
> and are not restated here.** Read this block before reading any unchecked box below: an
> unchecked `- [ ]` in this ledger no longer means "pending." It means the item closed on a
> ruling rather than on evidence, and the ruling says which kind.

### Why a batch ruling was needed

Six discharge passes (07-12 → 07-25) extracted everything the available evidence held. What
remained were **field-contingent** checks — conditioned on an event of a specific kind — and
nine of thirteen had no reachable trigger: four need **vlt-sayari**, which lives on the work
machine and is unreadable from the factory; three need a **mint the vault is structurally
steered away from producing**; one needs a **fresh-install vault**; one needs a **field
interaction**. The ledger conflated two claims under one checkbox — *did the build ship
correctly* (bounded, always dischargeable) and *has the mechanism fired in anger* (unbounded).
Closeout gated on both, so closeout had no bound. **This is a defect in the lifecycle, not a
fact about Arc 3**, and the durable fix is recorded under *Carried forward* below.

Precedent for each disposition already existed in this arc: **build-19**'s empty-specs clause
was *released as a standing watch* on 2026-07-25 because it had no reachable subject, and
**build-20**'s FAILED clause was *carried into Arc 4* rather than re-opening Arc 3. This batch
applies both, as a class.

### The dispositions

| Item / tail | Disposition |
|---|---|
| **Arc-2 owner action** — file BMB `after,before` template drift upstream | **CARRIED** (as Arc 2 already carried it) → owner action, no arc owns it |
| **build-15** consumer-lock + spec-bump relay | **FILED AS A FINDING** → `inbox/2026-07-26-142000-spec-convention-surfaces-candidates-nobody-accepts.md`. Five mints and two lint cadences passed through the convention with zero specs authored; that is a result, not a pending measurement |
| **build-16** boundary-creating mint (`days-to-first-check = 0`) | **FILED AS A FINDING** → `inbox/2026-07-26-142500-boundary-classifier-five-verdicts-and-an-unmeasurable-metric.md`. Metric is conditioned on an event `vlt-mint:150` actively steers this vault away from producing |
| **build-16 / 091006** first review-cycle | **DATED WATCH** — clock `spec.md` `review_after: 2026-08-17`; fires without owner action |
| **build-18 F1** `skill_asset_divergence` detect | **STAGED** — deliberate local edit to a `vlt-core` `.claude/skills/vlt-mint/assets/*` file **before** the pending 0.7.0→0.8.0 upgrade; the upgrade then exercises or fails the detector. Named action, one upgrade |
| **build-18 F3** overlaid-rule write op | **RELEASED** — vlt-core carries zero overlays and is counter-incentivized to grow one (`vlt-mint:150`); sayari-relay watch |
| **build-20** FP-rate FAILED + `revisit_due` adoption gap | **ALREADY CARRIED** to Arc 4 (arc-boundary ruling (b), 2026-07-25); A4-1 + A4-2 shipped the fixes in v0.8.0, acceptance sits on Arc 4's ledger |
| **build-21** A3-14 downstream subsumption | **RELEASED** — sayari-only, no substitute path, no clock; relay watch |
| **build-22 F1** four-lens `KIND_PANEL` | **RELEASED** — needs a roster-changing mint with no vault-side reason to run; watch |
| **build-22 F2** live-CSV registration | **RELEASED** — same trigger; the *pristine* half was re-corroborated at rest twice (shipped CSV 15 lines vs live 19) |
| **build-23** process-adoption | **EXERCISED AND FAILED → FILED** → `inbox/2026-07-26-141500-group-e-did-not-retire-the-handwritten-handshake-grep.md`. Trigger fired twice in Arc 4 (A4-3, A4-5) and the hand-written grep kept being written; root cause is `.claude/skills/build-brief/references/brief-anatomy.md:94-96`, which still instructs the old ritual and names the lint as `A/B/C`. Closes on an Arc-5 fix |
| **build-23** non-vacuous catch (Q28) | **✅ DISCHARGED 2026-07-26 by explicit owner note** — see the Q28 note appended to build-23's item below. Q28's condition (the *next version* also producing no qualifying drift) is now met by v0.8.0 |
| **build-23** F4 in the field | **WATCH** — needs a field interaction citing `vlt-lint:74`'s pin-not-conformance limit |
| **091003 M0** counter-accuracy audit | **FOLLOWS build-17** → Arc 5 (below); unpayable until counters exist |
| **build-17** (never built, evidence-blocked) | **✅ OWNER RULED 2026-07-26: FOLDED INTO ARC 5.** Its remit (the enforcement kit; derived vitals, tripwire registry, ledger surface) and its unpayable M0 debt transfer to Arc 5's capture. Arc 3 closes with this build unshipped, stated plainly rather than left undeclared |

**Nothing above is ticked that was not exercised.** Where a check was released rather than run,
it says so — the build-19 form. A reader must not read this ledger's `[x]` count as a measure of
what Arc 3 proved.

- [x] **(carried from Arc 1/2)** vlt-track loop-profile watch item: first
  post-0.4.0-upgrade track loop on vlt-core's vertical partners may not find the inline
  loop profile → if it breaks, build-11 field defect → inbox.
  (Discharged 2026-07-17 — **both halves resolved, the item stops being a watch.**
  *Machinery half:* the shipped location works in anger, in two vaults — vlt-sayari's Navigator
  carries a complete `## Loop profile` driving 6 real project loops
  (`inbox/2026-07-12-114940-sayari-060-upgrade-field-evidence.md` §2), and vlt-core's own
  `chess-coach` (minted 2026-07-16) landed
  `_agent/partners/chess-coach/capabilities/track.md` with `procedure: { skill: vlt-track }`,
  `weight: heavy`, and a full profile block. *Wearer half:* the anticipated drift is **CONFIRMED
  at rest** — `_agent/partners/{dog-trainer,health-coach}/` hold `identity.md`+`thread.md` and
  **no `capabilities/` dir at all**, with the profile declared inline at
  `.claude/skills/vlt-agent-dog-trainer/SKILL.md:41`, contra `vlt-track/SKILL.md:16`
  ("reads that profile from the invoking partner; it hardcodes none of it"). The vault's own
  mint council named it independently — Chess Coach entry, *Standing anomaly*: "those two
  declare loop profiles inline in SKILL.md contra `vlt-track/SKILL.md:16` — *they* are the
  drift." Owner ruling this run: **file as a build-11 field defect** rather than tick as vault
  cleanup → `inbox/2026-07-17-100000-loop-profile-drift-predates-build-11.md`. Honest limit
  recorded in the filing: no track loop has run on those two, so the *runtime break* is
  predicted, not measured — the divergence is what's confirmed. The prediction is now a filing;
  the watch does not ride a fourth arc.)
  <br>*Gate-2 ruling (2026-07-17) reads this item retroactively:* the machinery half
  discharged against post-fix wearers (`chess-coach`, Navigator) is **valid** — a post-fix
  instance is the right evidence that the corrected template works. The wearer half was
  **not** discharged against substitutes; it was confirmed against the at-risk pre-fix
  partners and found drifted → filed. What build-11 lacked was a *migration* check distinct
  from its *machinery* check; see the Owner rulings block. No re-open here.
- [ ] **(owner action, carried from Arc 2)** file the bmad-module-builder template drift
  (`after,before` in template merge script + tests) upstream to BMAD-METHOD.
  <br>**⚖️ CARRIED FORWARD past Arc 3 (2026-07-26)** — carried from Arc 2, STILL OPEN at Arc 3
  close, carries forward past Arc 3. An owner action against an upstream repo; no arc owns it and
  no arc should hold for it.
- [x] **091002 success metric (standing, not one-shot):** zero packaging filings into
  `inbox/` for releases ≥ 0.6.0; the 0.6.0 upgrade-ledger entry on vlt-core is the
  regression probe (exclusion pass finds nothing; CSV canonical; module.yaml resolves).
  (Discharged 2026-07-12 — 0.6.0 probe on vlt-core clean: exclusion pass leaves only the
  intentional A1 `.decision-log` stub on disk; `_bmad/module-help.csv` canonical at 17 rows
  + the 13-col header; `module.yaml` resolves 0.6.0; zero packaging filings in `inbox/` for
  0.6.0. Filing `091002` archived. Metric stays standing — re-probes each release ≥0.6.0.)
  <br>*Metric re-read 2026-07-17 — still HOLDING.* No release since 0.6.0, so no new probe is
  due; the standing claim is re-checked against the inbox instead. Nine filings have landed
  since (07-11 → 07-17) and **none is a packaging filing** — they are adoption gaps, governance
  single-home violations, and mint-behavior defects. One judgment call recorded:
  `inbox/2026-07-17-091000-vlt-mint-step4-registers-local-mints-into-shipped-artifacts.md`
  touches shipped artifacts (the `vlt-setup` mirror + `module.yaml` `agents[]`) and so brushes
  the metric's edge, but it is a **mint-registration defect, not a release-packaging one** — it
  concerns what a *vault-local mint* writes into upgrade-refreshed assets, not the lint's domain
  (cruft exclusion / CSV canonicality / version resolution). Counted as **not** a packaging
  filing; flagged here so the ruling is visible rather than silent. Live CSV is canonical at
  **19 rows** (17 + chess-coach `CC` + header), `csv.QUOTE_ALL`, round-trip verified by the mint.
  <br>*Metric re-read 2026-07-25 (full-lint pass) — still HOLDING, and now under load.* Four filings
  have landed since the last re-read (07-25: `partner-consult-synchronous-channel`,
  `revisit-after-has-no-adoption-path`, `contradictions-have-no-drain`,
  `auto-caption-name-substitution`) plus this pass's `linkage-ripe` filing — **none is a packaging
  filing**; they are a channel gap, two adoption/silent-zero gaps, an ingest-fidelity pattern, and a
  lint-projection defect. The 0.7.0 release probe itself remains clean (Group E PASS at `dbcf018`).
  Zero packaging filings for releases ≥ 0.6.0 across two releases and 14 filings.
- [x] **build-14 (packaging lint, briefed 2026-07-06):** factory-side — the 0.6.0 tag is
  cut only after `uv run tools/package-lint.py --expect-version 0.6.0` exits 0, PASS line
  recorded in the release commit; field-side — vlt-core's 0.6.0 own-the-apply runs the
  **widened** exclusion list from `vlt-upgrade/SKILL.md` text (not session practice).
  (Discharged 2026-07-12 — factory: release commit `a117f4f` records
  `package-lint: A/B/C PASS, D PASS — vlt 0.6.0 (… --expect-version 0.6.0, exit 0)`; field:
  vlt-core 0.6.0 own-the-apply left no stray cruft — single `.decision-log` on disk is the
  A1 stub, no `__pycache__`/`*.pyc`/`reports/` residue.)
- [ ] **build-15 (spec convention, briefed 2026-07-06):** hard gate honored — next vlt-core
  partner mint happens only with the convention in place and exercises the consumer lock
  (days-to-first-check = 0 for that boundary); 0.6.0 upgrade — skip-if-present preserves
  vlt-core's minted `spec.md` base, baseline stash gains the shipped stock, `config.yaml`
  gains `specs:` via provision, divergence report clean or example-only; migration offer
  human-gated + idempotent (stub at old path, open pointers re-pointed, `migrations_run:`
  records it); a live spec version bump produces one relay per listed consumer with the
  `_agent/specs/` path accepted.
  <br>*Upgrade-side DISCHARGED 2026-07-12* — vlt-core 0.6.0: `spec.md` seeded into
  `_agent/conventions/.baseline/` (Jul 8) and live at `_meta/conventions/spec.md` (version 1),
  `config.yaml` gained `specs: _agent/specs/` via provision, dir created, divergence report
  clean (skip-if-present vacuous — vlt-core had no pre-existing minted `spec.md` base; seed was
  fresh, no migration offered). **STILL-OPEN (first-exercise):** consumer-lock at next partner
  mint (days-to-first-check = 0) — no mint since 07-03, pre-upgrade; live spec-bump relay per
  consumer — `_agent/specs/` empty, no spec instance minted yet.
  <br>*Migration-offer half DISCHARGED 2026-07-17 (on vlt-sayari, not vlt-core)* — vlt-core's
  retrofit scan was vacuous by construction (nothing to retrofit). vlt-sayari's 0.4.0→0.6.0
  jump gave it a real exercise: the **proto-spec retrofit scan surfaced exactly one candidate,
  offered it, and accepted the owner's decline** ("a resolved two-round handoff, not an ongoing
  versioned contract. Nothing moved.") — human-gated and non-destructive, as briefed
  (`inbox/2026-07-12-114940-sayari-060-upgrade-field-evidence.md` §1).
  <br>**⛔ THIS RECLASSIFICATION RESTS ON A REFUTED PREMISE — see A3-12 (capture run 2,
  2026-07-17). DO NOT ACT ON IT UNTIL THE OWNER RE-RULES.** Grounding found that
  `vlt-upgrade/SKILL.md:75` — the proto-spec retrofit, **build-15's own F6 deliverable**
  (`3795d86`, briefed at `build-15-spec-convention.md:150-170`) — **does originate specs**.
  The filing traced only `vlt-mint` and `vlt-dispatch` and missed it. Worse, **the discharge
  four lines above (`migration-offer half DISCHARGED 2026-07-17`) records that very path
  firing correctly on vlt-sayari** — one candidate surfaced, offered, human-declined. Empty
  `_agent/specs/` is therefore a **correct negative**, not proof of unreachability. The
  residual gap is **cadence** (origination is gated to upgrade-time, a rare owner-run event),
  not existence — a much smaller thing. **Arc-closeout may not be blocked at all.** The text
  below is preserved verbatim as the record of what was believed on 07-17; it is not current.
  <br>**✅ OWNER RE-RULED 2026-07-17 (gate 1, see Owner rulings — capture run 2 follow-up):
  the arc is NOT blocked.** This tail reverts to **STILL-OPEN (first-exercise)** —
  discharging event: the first real spec minted in a live vault, exercising the
  consumer-lock and spec-bump relay **non-vacuously per gate 2**. The cadence residual
  routes to run-2 ideation, not to this ledger item.
  <br>*Substrate now exists 2026-07-18 (vlt-core 0.7.0 upgrade — `upgrade-ledger.md`
  [2026-07-18 12:44] §Migrations run).* The `proto-spec-retrofit` migration `git mv`'d two
  handoffs into `_agent/specs/` — `2026-06-13-health-coach-to-chef-nutrition-spec` (v2) +
  `2026-06-21-creative-to-chef-meal-plan-format` (v1), frontmatter conformed to the spec
  schema, one-line stubs left at each old `_agent/handoffs/` path (verified on disk: 2 specs
  present, 2 stubs 707B/719B). **The vault holds real versioned specs for the first time** —
  where `_agent/specs/` was empty at every prior discharge run, the consumer-lock now has
  specs to consume and a spec-bump relay is now possible. **Both first-exercise tails STAY
  STILL-OPEN:** a retrofit is *not* a partner mint (consumer-lock fires at mint — none since
  the upgrade, post-upgrade activity is all chess-coach tracking) and no version bump has
  fired (relay). Discharging events unchanged — next partner mint (days-to-first-check = 0)
  and a live spec version bump per listed consumer; both owner-triggered. Non-vacuity is no
  longer blocked by an empty specs dir.
  <br>*Unmoved 2026-07-25 (fresh-note pass) — but the advocacy gap keeps closing on its own.* No
  partner mint since the upgrade (the two post-upgrade mints are a capability-refine and a light
  capability add) and no spec version bump — both tails STILL-OPEN, triggers unchanged
  (owner-run partner mint for the consumer lock; a live `version:` bump for the relay). Two
  independent signs the convention is now *reaching* people rather than sitting dark, recorded
  because the 07-13 "no advocate" filing predicted the opposite: (1) the `[2026-07-18 13:15]` lint
  filed a `spec_candidate` to backlog unprompted (build-19's steady-state advocacy, already
  discharged above); (2) the `walkthrough-renderer` mint reasoned about `{specs}` **unprompted and
  correctly** in its own boundary detail — "the position-list contract is a bilateral handoff
  schema… it graduates toward a `{specs}` contract only if a second producer adopts it"
  (`_agent/mint/decision-log.md:526`). That is the first time a vault-side mint has invoked the
  spec convention on its own initiative. It is **not** a discharge (no spec was authored, the
  consumer lock did not fire), but it is the strongest evidence yet that the tail is a slow one,
  not a dead one.
  <br>*Unmoved 2026-07-25 (full-lint pass) — and the advocacy signal fires a third time.* No partner
  mint since 2026-07-18 (`_agent/mint/decision-log.md` ends at the 07-18 `walkthrough-renderer`
  entry) and no spec `version:` bump — both tails STILL-OPEN, triggers unchanged (owner-run partner
  mint; a live version bump). The `[2026-07-25 15:05]` full lint filed a **second** `spec_candidate`
  to backlog unprompted — `creative→chess-coach spec candidate`, human-gated, never auto-promoted —
  against a `_agent/handoffs/` that has now grown to 5 docs and a `_agent/specs/` holding 2. The
  convention is being *offered* at every lint cadence; what is missing is an owner accepting one.
  <br>*(superseded reasoning follows)* **⚠ TAIL RECLASSIFIED 2026-07-17 — BLOCKED BY DESIGN GAP, not awaiting a natural event.**
  `_agent/specs/` is still empty at 9 days post-upgrade, and
  `inbox/2026-07-13-092341-spec-convention-has-no-advocate.md` establishes why: **no shipped
  surface can originate a spec.** `vlt-dispatch:41` points at specs but "never authors them";
  `vlt-mint:11`'s kind list has no author-a-spec kind, and its only spec contact is the consumer
  lock (`:108`), which fires on an *already-existing* spec. The sole promotion trigger is a prose
  rule in the operating contract (`:227`). Every load-bearing spec mechanism is downstream of a
  spec existing; creation is the one step with no home.
  <br>*Confirming negative test (2026-07-16)* — the **Chess Coach `new partner` mint** is the
  strongest possible probe and it came back dry: a council-gated mint, four council rounds, all
  four lenses convened, cross-partner precedent deliberately set and bounded, a heavy `vlt-track`
  capability pointer authored — and the spec convention **never came up once**. The consumer lock
  could not fire (zero specs to consume). This is not a slow tail; the richest mint event the
  vault has ever run passed straight through the convention without touching it.
  <br>**Consequence for acceptance:** the consumer-lock and spec-bump-relay checks cannot
  discharge until the advocacy gap is fixed — the 07-13 filing is **blocking build-15's
  acceptance close**, per its own grounding note, and must be captured (Arc 3 or build-17's
  enforcement kit) rather than waited out. Note the tripwire cannot rescue this:
  `spec.md` declares `deferral_metric: "spec version bumps shipping without their relay entries"`
  at threshold 1 — in a vault with zero specs that metric **reads clean forever**, measuring
  adoption failure as success. `review_after: 2026-08-17` would eventually surface it as a
  staleness bell about a document, never as "this convention has never been used."
  <br>**⚖️ CLOSED 2026-07-26 — FILED AS A FINDING.** Both tails converted to
  `inbox/2026-07-26-142000-spec-convention-surfaces-candidates-nobody-accepts.md`; disposition and
  reasoning in the *Closeout dispositions* block at the head of this ledger.
- [ ] **build-16 (frontmatter@3, briefed 2026-07-06):** 0.6.0 upgrade — consumer walk
  converges on vlt-core (post-upgrade lint: zero coherence findings; five skills at
  `frontmatter@3`, four at `write-verification@1`); first post-upgrade lint run is
  flood-free on the legacy corpus (`unattested_write` informational-only pre-convention,
  `review_due` only where set, `para_missing_attestation` true-positive only); next
  boundary-creating mint has days-to-first-check = 0 and zero conventions sit `declared`
  untripwired; local base stamps/overlays converge (with build-18's subsumption retire).
  Pending attachments: 091005 M4 two measured lint cycles; 091006 first review-cycle
  evidence.
  <br>*Upgrade-side DISCHARGED 2026-07-12* — vlt-core 0.6.0: consumer walk converged —
  5 skills at `frontmatter@3` (extract, ingest, lint, mint, research), 4 at
  `write-verification@1` (extract, ingest, lint, research), convention versions coherent
  (frontmatter 3 / write-verification 1 / spec 1) → zero coherence findings; first
  post-upgrade lint (`_agent/log.md` `[2026-07-08 19:28] lint | full`, 1h43m after the 17:45
  upgrade) flood-free — "all attested", no coherence/attestation flood. **STILL-OPEN:**
  next boundary-creating mint days-to-first-check = 0 (no post-upgrade mint); 091005 M4 needs
  a **2nd** measured lint cycle (only the 07-08 cycle so far); 091006 first review-cycle
  evidence unrun.
  <br>*Classifier gate exercised 2026-07-13 (partial)* — vlt-core's first post-upgrade mint
  (`_agent/mint/decision-log.md` `## [2026-07-12] add a capability — file-module-feedback`) ran
  the build-16 boundary classifier and recorded **`Boundary classifier: non-boundary`** with its
  reasoning (conforms to a factory-owned convention; defines no rule; "no vault-side bell
  needed"). The gate is live in the vault's mint path and correctly declined to ring — but a
  *non-boundary* verdict is not the bell firing. The tail stands: it needs a **boundary-creating**
  mint to show days-to-first-check = 0.
  <br>**091005 M4 (two measured lint cycles) DISCHARGED 2026-07-17.** Both cycles are now on the
  record in `_agent/log.md`, and the second is the one that proves the contract has teeth:
  *Cycle 1* — `[2026-07-08 19:28] lint | full`, 122 files, flood-free ("all attested"), 1h43m
  after the upgrade. *Cycle 2* — `[2026-07-13 09:40] lint | scoped since 2026-07-08 19:28`,
  35 files, structurally clean (governance clean, 7 conventions pristine vs `.baseline`, every
  consumer `depends_on` pin current, 4/4 capabilities lane-safe, no expired deferrals) — **and it
  caught a real attestation bypass**: the 07-13 dog ingest wrote/updated 4 pages and attested
  none, a week after `write-verification@1` adopted (6 unattested agent-lane pages total). The
  vault's own read: *"the bypass detector firing as designed — points at the op, not the pages"*,
  with `fixes: 0 auto-fixed` ("lint never attests what it merely read"). Two measured cycles, the
  detector demonstrated on a live bypass rather than a fixture. Cycle 2 also surfaced 6
  personalized-extraction firewall breaches — real findings, vault-side, not module defects.
  <br>*Classifier exercised a 3rd time 2026-07-16 — the reliability finding.* vlt-core's
  **Chess Coach `new partner` mint** ran the classifier and reached
  **`non-boundary` — but only after TWO WRONG ANSWERS BY INFERENCE, resolved by user ruling**
  (`_agent/mint/decision-log.md`, 2026-07-16). The classifier's wrong answers were caught by the
  council, not by itself: round 1 killed a `non-boundary` resting on a false premise
  (`consumers:` read as an authorization; `extraction.md:47`'s grant names no op), and round 2
  caught a **fabricated root cause** — a claim that an upgrade "ate" the extraction registry table,
  when in truth the table was retired by user ruling and *the durability mechanism worked*. Both
  errors trace to a **single-home violation at the governance layer**: the repeal lives only in
  `_agent/upgrade-ledger.md:48` and never reached the decision-log, whose own header now warns the
  log "is NOT self-sufficient" and "the ledger is not chronological." Blast radius before the
  council caught it: an overlay and a module bug report accusing the module of a bug that never
  happened, both withdrawn. Root cause is **vault-side** and already filed
  (`inbox/2026-07-17-090500-upgrade-rulings-never-reach-the-decision-log.md`; the grant-text half
  is `inbox/2026-07-17-090000-extraction-grant-authorizes-nobody.md`) — so this is not a build-16
  defect, but it is a standing caution: **the bell's classifier is only as good as the governance
  record it reasons over**, and here that record was silently incomplete.
  <br>**Tail STILL-OPEN, and now with a pattern worth naming:** three classifier runs since the
  upgrade (07-12 capability, 07-16 new partner, 07-17 atlas mint brief) and **three `non-boundary`
  verdicts** — the gate is live, reachable, and has never once rung. days-to-first-check = 0 needs
  a genuinely boundary-creating mint, which has not occurred. Whether three straight declines is
  correct behavior or a classifier biased toward silence is not yet distinguishable from this
  evidence; the 07-16 run (wrong twice, user-corrected) is the only reason to ask.
  <br>*No change from the 0.7.0 upgrade 2026-07-18 — tail STILL-OPEN.* frontmatter advanced
  `@3→@4` at this release (build-20), but build-16's own tail is the **boundary-creating
  mint** (days-to-first-check = 0), and none occurred: all post-upgrade vault activity is
  chess-coach answer-key tracking (games 5–8, `_agent/log.md`), zero mints. 091006
  first-review-cycle also unmoved — still waits on the first `review_after:` to come due
  (earliest `spec.md`'s own `2026-08-17`). Discharging trigger unchanged: an owner-run
  boundary-creating mint; the review-cycle tail is a dated clock (2026-08-17).
  <br>*Classifier 4th verdict 2026-07-18 (post-0.7.0-lint pass) — still never rung.* The one
  post-upgrade mint, a **capability-refine** (`_agent/mint/decision-log.md`
  `## [2026-07-18] capability-refine (chess-coach) — answer-key`), ran the boundary classifier
  and returned **`non-boundary`** (own-zone, binds only the owning partner's loop) — the **4th
  straight `non-boundary`** since the 0.6.0 upgrade (07-12 capability, 07-16 new-partner,
  07-17 atlas brief, 07-18 answer-key). Each verdict is *correctly* non-boundary (capability
  adds, no rule/convention/partner boundary), so this is **not** a reachability alarm: a
  boundary-creating mint (new-partner / convention-edit) *can* fire the bell — the owner has
  not run one. Tail STILL-OPEN, trigger unchanged (owner-run boundary-creating mint).
  <br>*Classifier 5th verdict 2026-07-25 (fresh-note pass) — reachability re-examined, not
  re-annotated.* A second post-0.7.0 mint has run: `add-a-capability (creative) —
  walkthrough-renderer (light, own-zone)` (`_agent/mint/decision-log.md:526`, `_agent/log.md`
  `[2026-07-18 15:45]`), verdict **`non-boundary`** with an explicitly reasoned detail — "the
  position-list contract is a bilateral handoff schema a producer opts into for renders, not
  enforced vault governance — it graduates toward a `{specs}` contract only if a second producer
  adopts it." That is the **5th straight `non-boundary`**, and per the discharge rubric's
  pass-through tripwire a tail this old may not simply be re-annotated, so reachability was
  re-checked at the source rather than assumed: `vlt-mint/SKILL.md:59` names **`convention edit`**
  and `new partner` among the *gated* kinds, and `:42` runs the classifier on **every** kind — so
  a boundary-creating verdict is producible by a shipped surface today (an owner-run `convention
  edit` mint, or a roster-changing `new partner`). **Reachable ⇒ STILL-OPEN, not BLOCKED**, and
  each of the 5 verdicts remains substantively correct (four capability adds/refines + one
  new-partner whose subject bound no other partner). The tally is worth watching, not yet
  alarming: what would flip this to BLOCKED is a *boundary-creating* mint that still verdicts
  `non-boundary`. 091006 first-review-cycle also unmoved — the clock (`spec.md`'s
  `review_after: 2026-08-17`) has not come due (today is 2026-07-25).
  <br>*Unmoved 2026-07-25 (full-lint pass) — no new classifier verdict at all, so no tripwire
  question arises.* Zero mints have run since the 07-18 `walkthrough-renderer` entry
  (`_agent/mint/decision-log.md`), so the classifier tally stays at 5 straight `non-boundary` and
  this pass adds no pass-through: the discharging *kind* of event did not occur, rather than
  occurring and failing to fire. Reachability stands as re-established at source on 07-25
  (`vlt-mint/SKILL.md:59`/`:94`). Trigger unchanged: an owner-run boundary-creating mint. Bonus
  corroboration for the item's convergence half from the full sweep: **7 conventions pristine vs
  `.baseline`, every consumer `depends_on` pin current, zero coherence findings, no overlays, all
  11 capabilities lane-safe** across a 130-page + 98-note + 16-artifact sweep — the widest surface
  the convergence claim has ever been checked against. 091006 first-review-cycle still 23 days from
  its clock (`spec.md` `review_after: 2026-08-17`).
  <br>**⚖️ CLOSED 2026-07-26.** Boundary-mint tail → FILED AS A FINDING
  (`inbox/2026-07-26-142500-boundary-classifier-five-verdicts-and-an-unmeasurable-metric.md`);
  091006 → DATED WATCH (2026-08-17). See the *Closeout dispositions* block at the head of this ledger.
- [ ] **build-18 (durability cluster, briefed 2026-07-08):** 0.6.0 upgrade on vlt-core —
  F2 subsumption pass offers vlt-core's `review_after` overlay section for retirement
  (`overlay-subsumption` in `migrations_run`), shadow gone, lint clean; F1 skill-asset net
  seeds `.skill-manifest` (0.6.0 run reports `skill_manifest_missing` once, then clean) and a
  subsequent local `vlt-mint/assets/*` edit surfaces as `skill_asset_divergence` on the next
  upgrade, not a silent clobber; F3 first post-upgrade write op honors an overlaid convention
  rule without a manual reminder; F4 next relocation migration leaves a stub, touches no
  worktree copy, re-points open pointers; F5 standing — no future shipped worked example
  couples to a live artifact path (0.6.0 shipped surface is the clean baseline).
  <br>*Partially DISCHARGED 2026-07-12* — vlt-core 0.6.0: F1 `.skill-manifest` seeded
  (42-line SHA-256 manifest at `_agent/conventions/.baseline/.skill-manifest`, Jul 8); **F2
  vacuous — no `review_after` overlay existed to subsume** (vault carried zero overlays); F5
  shipped surface clean at `a117f4f`. **STILL-OPEN:** F1 divergence-detect half (needs a local
  `vlt-mint/assets/*` edit + next upgrade to surface `skill_asset_divergence`); **F3 vacuous —
  no overlays to honor** (mechanism unexercised); F4 next relocation migration (none since
  upgrade).
  <br>**F2 DISCHARGED 2026-07-17 (on vlt-sayari — owner ruling this run).** vlt-core's F2 is
  **vacuous by construction, not pending**: the vault carries zero overlays, so the
  `review_after`-retirement instance the brief names can never occur there — leaving it open
  would be the silent-zero trap the 07-13 filing describes. The mechanism the check actually
  tests has real field evidence from vlt-sayari's 0.4.0→0.6.0 jump: a **subsumption pass against
  a live ~270-line `extraction.overlay.md`**, which **ran, decided, retired nothing — correctly —
  and recorded its reasoning** (`inbox/2026-07-12-114940-sayari-060-upgrade-field-evidence.md`
  §1). A pass that correctly declines is the check passing, not the check skipped. **Retargeted:
  vlt-sayari is the vault where F2/F3 discharge; vlt-core cannot exercise either.**
  <br>*F3 stays OPEN, retargeted to vlt-sayari.* Its filing evidences the full overlay lifecycle
  (creation, a council-gated overlay edit REVISE→PASS on 07-01, append-only RETIRED-in-place
  banners, the upgrade-time subsumption check) but **never a post-upgrade write op honoring an
  overlaid convention rule without a manual reminder** — which is what F3 checks. Discharging it
  from lifecycle evidence would be inference, not evidence. Needs a named write op on sayari.
  <br>*Bonus field evidence, no ledger item (recorded so it isn't lost):* vlt-sayari's upgrade
  also gave first real exercise to **capability families** (`families/project-hub.md`,
  `instances: [navigator, creative]` — the "families are dead weight?" question from build-7 is
  answered: **exercise, don't prune**), the **build-13 help-CSV header migration** on a harder
  two-version jump path, and the **first field retirement of a minted skill**
  (`vlt-spec-external`, minted 06-29 → retired 06-30, archived not deleted). Its §4 watch note —
  *preserve-sets must derive from disk, never from the prior ledger entry* (the vault grew 4
  capabilities, a minted skill, and a family within 2 days of its upgrade, none in any ledger
  inventory) — is a one-sentence candidate for `vlt-upgrade` Step 1 prose, below build threshold
  alone; it belongs with Arc 3's derive-first invariant at capture.
  <br>**F4 DISCHARGED 2026-07-18 (vlt-core 0.7.0 upgrade).** The `proto-spec-retrofit`
  migration is the "next relocation migration" F4 names: it `git mv`'d two handoffs
  `_agent/handoffs/` → `_agent/specs/`, **left a one-line stub at each old path** (verified on
  disk — 707B/719B stubs still present), touched no worktree copy (own-the-apply is a
  filesystem move), and re-pointed open pointers **vacuously — the dispatch relays were both
  closed `[x]`, so there were none to re-point** (`upgrade-ledger.md` [2026-07-18 12:44]
  §Migrations run). Stub-leaving + non-destructive + pointer-safe, exactly as briefed.
  <br>*F1 divergence-detect + F3 STAY STILL-OPEN.* F1's seed half was long discharged; its
  **divergence-detect** half needs a deliberate local `vlt-mint/assets/*` edit followed by an
  upgrade to surface `skill_asset_divergence` — the 0.7.0 pre-flight found *none* (all 42→43
  `.skill-manifest` SHAs matched; a new asset `decision-log-template.md` was added cleanly, not
  a local divergence), so the detector is still unexercised. Trigger: an intentional local
  asset edit + next upgrade. F3 stays **retargeted to vlt-sayari** — needs a named post-upgrade
  write op honoring an overlaid convention rule; vlt-core carries zero overlays and cannot
  exercise it. Trigger: a write op on vlt-sayari against its `extraction.overlay.md`.
  <br>*Unmoved 2026-07-25 (fresh-note pass).* **F1 divergence-detect:** no deliberate local
  `vlt-mint/assets/*` edit and no upgrade since 0.7.0 — detector still unexercised. **F3:**
  vlt-sayari untouched since 2026-07-11 (no write op against `extraction.overlay.md`), and
  vlt-core still carries zero overlays. Triggers unchanged; both owner-run.
  <br>*Unmoved 2026-07-25 (full-lint pass).* No upgrade and no deliberate local `vlt-mint/assets/*`
  edit since 0.7.0 → **F1 divergence-detect** still unexercised. vlt-sayari still untouched since
  2026-07-11 → **F3** unmoved; the full lint independently re-confirms vlt-core has **no overlays**
  ("no overlays" in the governance pass), so F3 remains subject-less there by construction, exactly
  as the 07-25 relay-or-nothing ruling records. Triggers unchanged; both owner-run.
  <br>**⚖️ CLOSED 2026-07-26.** F1 → **STAGED**: deliberately edit a `vlt-core`
  `.claude/skills/vlt-mint/assets/*` file before the pending 0.7.0→0.8.0 upgrade, which then
  exercises or fails the detector (a detector firing on a deliberate divergence is a valid
  exercise — F1 detects, it does not require a natural occurrence). F3 → **RELEASED** as a
  sayari-relay watch. See the *Closeout dispositions* block at the head of this ledger.
- [x] **build-19 (spec-followup, BUILT + unit-verified at rest 2026-07-17; F1–F4 in tree, versions still 0.6.0 — not yet released, acceptance rides the next release's upgrade):** next ordinary vlt-core/vlt-sayari
  upgrade — **spec-candidate surfacing works in anger:** a lint run on a vault with a
  spec-shaped handoff (revised in place / ≥2 relay pointers at one path) surfaces it as
  `spec_candidate`, human-gated, filed/flagged, **never auto-promoted**; a lint run on an
  empty `_agent/handoffs/` (or empty `_agent/specs/`) yields **no finding and no zero-specs
  alarm** (steady-state advocacy now fires at lint cadence, not only upgrade cadence).
  **Coherence converges on the new consumers:** post-upgrade `vlt-lint` convention-coherence
  reports zero `spec` findings — all four consumers (`vlt-mint`, `vlt-dispatch`, `vlt-upgrade`,
  `vlt-lint`) ack `spec@1`, `vlt-upgrade` no longer drifting silently, `spec.md` still
  `version: 1`. **Contract map shows `specs`:** the operating contract's structure-map table
  carries the `specs` row (semantic description + SSoT-mirror note); a partner/generic agent
  reading the contract resolves `{specs}` from the table. **Tool-zone reframe visible +
  non-regressing:** the contract reads as an extensible "not a content layer" class, and a
  vault carrying its own tool tree (e.g. a `dev/` tree) is not treated as vault content by lint
  or the partners. **Must NOT be read as discharging build-15's consumer-lock/spec-bump
  first-exercise tail** (that needs a real spec minted non-vacuously per gate 2 — build-19
  improves the odds but cannot cause it).
  <br>*Upgrade-side DISCHARGED 2026-07-18 (vlt-core 0.7.0 upgrade).* **Coherence converges on
  the new consumers, structurally:** `spec.md@1` lists `consumers: [vlt-mint, vlt-dispatch,
  vlt-upgrade, vlt-lint]` and all four ack it in their live `depends_on` (`vlt-dispatch:3`,
  `vlt-mint:3`, `vlt-upgrade:3`, `vlt-lint:4` all pin `spec@1`) — bipartite-consistent,
  `vlt-upgrade` no longer drifting silently, `spec.md` still `version: 1`. **Contract
  structure-map carries `specs`:** `_meta/vault-operating-contract.md:35` has the
  `specs | _agent/specs/ | Durable, owned…` row. **STILL-OPEN (first-exercise, all needing a
  post-upgrade `vlt-lint` run — none has run since the 12:44 upgrade; last lint was
  2026-07-13):** the *live* zero-`spec`-coherence-findings confirmation; `spec_candidate`
  surfacing on a real spec-shaped handoff (the vault now has non-empty `_agent/handoffs/` +
  `_agent/specs/`, so the empty-→-no-alarm branch also awaits a lint); tool-zone
  non-regression at runtime. Trigger: the next `vlt-lint` run on vlt-core (or vlt-sayari).
  <br>**Lint-side DISCHARGED 2026-07-18 (post-0.7.0-lint pass — the `[2026-07-18 13:15] lint
  (librarian)` run, first lint after the 12:44 upgrade, scoped since 2026-07-13 09:40).**
  Three lint-gated sub-clauses land: **live zero-`spec`-coherence** — the governance pass on
  the 0.7.0-upgrade delta reports all consumer `depends_on` pins current
  (`extraction@3/frontmatter@4/spec@1`), zero `spec` findings; **`spec_candidate` surfacing
  human-gated** — the run filed exactly one to backlog (`spec_candidate: health-coach→chef
  nutrition spec`), flagged not auto-promoted, and raised **no spurious zero-specs alarm**
  (steady-state advocacy firing at lint cadence, as designed); **tool-zone non-regression at
  runtime** — vlt-core now carries a real tool tree (`_agent/chess/tools/.venv/`, python-chess
  + site-packages) and the scoped run checked 4 files structurally clean, never sweeping the
  venv as vault content. **Residual (narrow, low-value):** the *empty*-`_agent/handoffs/` /
  *empty*-`_agent/specs/` → no-finding negative-case cannot be exercised on vlt-core (non-empty
  both) nor vlt-sayari — it needs a vault with empty specs; offered to the owner as an
  early-release / standing-watch candidate, not a blocking tail.
  <br>*Residual still unresolved 2026-07-25 (fresh-note pass) — the early-release offer is still
  awaiting an owner ruling, and vlt-core has moved further away from being able to answer it:*
  `_agent/handoffs/` gained two more entries since the offer
  (`2026-07-18-creative-to-chess-coach-walkthrough-contract.md`,
  `2026-07-19-researcher-to-librarian-chess-improvement-crosscheck.md`), so the empty-zone negative
  case is now doubly unreachable on both known vaults.
  <br>**✅ OWNER RULED 2026-07-25: released as a standing watch, not a blocking acceptance debt.**
  The negative case has no reachable subject in either known vault, so it does **not** gate
  build-19's acceptance close; `arc-closeout` **carries it forward** as a watch, discharged by the
  first fresh-install vault that runs a lint with an empty `_agent/specs/`. Recorded here rather
  than ticked — the check was never exercised, it was released.
  <br>*Corroborated on a FULL run 2026-07-25 (full-lint pass) — every sub-clause has now fired at
  full scope.* The `[2026-07-25 15:05]` run re-exercises the three lint-gated sub-clauses discharged
  on 07-18 against a far wider surface than the 4-file scoped run that first settled them:
  **`spec_candidate` surfacing human-gated** — a second candidate filed to backlog
  (`creative→chess-coach`), flagged not auto-promoted, against 5 handoffs + 2 specs, and **no
  zero-specs alarm** raised; **zero `spec`-coherence findings** — every consumer `depends_on` pin
  current across 7 conventions; **tool-zone non-regression at runtime** — the fan-out swept 130 wiki
  pages and never touched `_agent/chess/tools/.venv/` as vault content (the research count is 98
  notes, tools excluded).
  <br>**✅ TICKED — OWNER RULED 2026-07-25 (full-lint pass): build-19 is DISCHARGED.** Every
  sub-clause has landed — spec-candidate surfacing human-gated (twice, now at full scope), the
  empty-zone no-alarm branch, coherence convergence on all four `spec@1` consumers, the contract's
  `specs` structure-map row, and tool-zone reframe + runtime non-regression — **with one clause
  released rather than exercised**, stated here so the tick is not read as more than it is: the
  *empty*-`_agent/handoffs/`/*empty*-`_agent/specs/` negative case **was never run** and has no
  reachable subject in either known vault. It is **owner-released as a standing watch**, discharged
  by the first fresh-install vault that lints an empty specs zone; **`arc-closeout` carries it
  forward** as a watch item, not as acceptance debt. This is the first Arc 3 build to fully
  discharge since build-14.
- [ ] **build-20 (graduation-queue, briefed 2026-07-17):** next ordinary vlt-core/vlt-sayari
  upgrade — **`topic:` fix took:** a fresh `vlt-research` note writes `topic:` as a YAML list;
  no new research note carries the scalar form (the module-caused raggedness is healed at the
  source). **Handshake holds at `@4`:** all five frontmatter consumers (`vlt-ingest`,
  `vlt-extract`, `vlt-research`, `vlt-lint`, `vlt-mint`) pin `frontmatter@4`; a live `vlt-lint`
  run reports zero convention-coherence findings for frontmatter (no stale/unacked/dangling).
  **Union projection is honest on live data:** `vlt-lint` surfaces `linkage_ripe` candidates on
  the research zone via the union (frontmatter `topic:` ∪ body `[[wikilinks]]` ∪ shared
  `sources:`), **never auto-promoting**; the false-positive rate tracks the calibrations
  (union ≪ naive — A3-8 ~21% vs ~79%, A3-9 ~23% vs ~69%), measured on **both** vaults — a
  naive-level FP storm is a failure. **`revisit_after` behaves:** a research note with a past
  `revisit_after` is surfaced (`revisit_due`), never auto-resolved or nagged; **absence = zero
  findings** — legacy research notes (92 vlt-core, 13 vlt-sayari) generate no noise (trivial
  backfill by construction). **Fix-then-measure closes (Q2):** post-fix `topic:` raggedness is
  re-measured on vlt-core research notes, feeding any future `cluster_ripe`/K decision (this
  build makes no `topic:`-clustering ruling). **Honest scoping verified:** `vlt-lint-full.js`
  still sweeps `{wiki}` only, the SKILL's research-candidacy pass covers `{research}`, no capped
  sweep is presented as exhaustive, and the wider-surface second cut stays named. **Must NOT be
  read as landing `cluster_ripe`, the ingest-time probe, or the handoffs/threads scan surface** —
  all three are explicitly deferred (surviving-shape ruling; research-zone-first).
  <br>*Upgrade-side DISCHARGED 2026-07-18 (vlt-core 0.7.0 upgrade).* **Handshake holds at
  `@4`:** `frontmatter.md@4` and all five frontmatter consumers pin `frontmatter@4` in their
  live `depends_on` — `vlt-ingest:4`, `vlt-extract:4`, `vlt-research:3`, `vlt-lint:4`,
  `vlt-mint:3` — bipartite-consistent, no stale/unacked/dangling pin. **`topic:` source fix
  landed:** `vlt-research/SKILL.md:65` writes `topic:` as a YAML list (`# YAML list, general →
  specific`), refreshed into the vault by the upgrade. **STILL-OPEN (first-exercise):** a
  *fresh* research note actually writing `topic:` as a list — latest research note is
  2026-07-16, pre-upgrade, so the source fix is unexercised (trigger: next `vlt-research`
  run); the union-projection `linkage_ripe` honesty + FP-rate-tracks-calibration + `revisit_due`
  + legacy-notes-no-noise checks all need a live `vlt-lint` run on **both** vaults (none since
  the upgrade). Trigger: next `vlt-research` note, then a `vlt-lint` run on vlt-core + vlt-sayari.
  <br>*Lint-side partial 2026-07-18 (post-0.7.0-lint pass).* The `[2026-07-18 13:15]` run
  confirms the **live frontmatter coherence** half of *Handshake holds at @4*: the governance
  pass reports the `frontmatter@4` pins current across consumers, zero convention-coherence
  findings (no stale/unacked/dangling). **All the graduation-queue behavior STAYS STILL-OPEN:**
  the run was scoped (4 changed files, not research notes) and exercised no research-zone union
  projection — `linkage_ripe` honesty + FP-rate-tracks-calibration (on **both** vaults), the
  `revisit_due` positive case, and the fresh-note `topic:`-as-list check all remain unfired
  (no research note since 2026-07-16, pre-upgrade; vlt-sayari still at 0.6.0, no lint since
  07-11). Legacy-no-noise is only weakly corroborated (no flood on a 4-file scope). Triggers
  unchanged: a fresh `vlt-research` note, then a `vlt-lint` run on vlt-core **and** vlt-sayari.
  <br>**`topic:` fix took — DISCHARGED 2026-07-25 (fresh-note pass; the one tail that moved this
  run).** Four research notes have been written on vlt-core since the 0.7.0 upgrade, and **all
  four write `topic:` as a YAML list**, zero scalar: `_agent/research/2026-07-19-110053-chess-improvement-crosscheck-two-claims.md:7`
  and `2026-07-19-110510-black-opening-approach-sub-1000-ideas-not-lines.md:7` (both `vlt-research`
  runs — `_agent/log.md` `[2026-07-19 11:01]`, `[2026-07-19 11:05]`),
  `2026-07-25-131035-secure-offsite-backup-for-a-git-managed-vault.md:7` (`vlt-research`,
  `[2026-07-25 13:10]`), and `2026-07-25-131352-afc-west-preview-kimes-winks.md:9`
  (`verified_by: vlt-ingest`, `[2026-07-25 13:13]` — the ingest-side writer honors the same
  shape). The module-caused raggedness is healed **at the source**: the newest scalar-form note in
  the zone is `2026-06-27-151823-youtube-video-to-markdown-for-wiki-ingest.md`, pre-fix — nothing
  written after the fix carries the scalar form.
  <br>**Fix-then-measure (Q2) closes 2026-07-25 — the post-fix measurement, for the record.**
  vlt-core research zone at 96 notes: **55 scalar `topic:` / 41 list**, every scalar one dated
  ≤ 2026-06-27 (all pre-fix legacy, trivial backfill by construction as the brief predicted);
  **post-fix cohort 4/4 list, 0/4 scalar.** This is the raggedness number any future
  `cluster_ripe`/K decision reads from; this build still makes no `topic:`-clustering ruling.
  <br>*Everything lint-gated STAYS STILL-OPEN — no `vlt-lint` run on either vault since
  `[2026-07-18 13:15]`.* `linkage_ripe` union honesty, FP-rate-tracks-calibration, the
  `revisit_due` positive case, and legacy-notes-no-noise on the full zone all still need a lint.
  The fresh-note trigger is now **spent**; the remaining trigger is a `vlt-lint` run on vlt-core,
  which now holds 4 fresh union-eligible notes to project over.
  <br>**Lint-mode ruling 2026-07-25 — the discharging run must be a FULL lint, and scoped will not
  do (grounded, not assumed).** `vlt-lint/SKILL.md:82` runs the research-note candidacy pass in
  **both** modes, and scoped mode's candidate set at `:32` (`find {wiki} {research} {sessions}
  -newermt …`) *does* include `{research}` — so a scoped run since `[2026-07-18 13:15]` would fire
  `linkage_ripe` on the 4 fresh notes and exercise the `topic:`-list auto-fix path. But two clauses
  are **population-level and structurally unservable by a scope**: *FP-rate tracks the calibration*
  (`SKILL.md:83`, ~21–23% union vs ~69–79% naive) needs a population to compute a **rate** — 4 notes
  cannot produce one; and *legacy-notes-no-noise* is a claim about the **92-note legacy corpus**, of
  which a 4-file scope sees none (exactly the "only weakly corroborated" residual the 07-18 pass
  already recorded). **Discharging event, stated precisely: one `vlt-lint --full` run on vlt-core.**
  <br>**✅ OWNER RULED 2026-07-25 — the "measured on **both** vaults" clause is NOT a gate.**
  vlt-sayari lives on the work machine and is unreadable from the factory machine; its evidence can
  only ever arrive **relayed** (it has no inbox access of its own — it has filed that way twice,
  most recently `inbox/2026-07-25-132141-partner-consult-synchronous-channel.md:107` confirming it
  is still 0.6.0). Ruling: **the FP-rate + legacy-no-noise clauses discharge on a vlt-core full lint
  alone**; sayari's second data point is **bonus corroboration via relayed filing, never a
  requirement**. Rationale recorded so it isn't re-litigated: the two-vault wording is an artifact of
  how the *calibration* was originally measured (A3-8 vlt-core ~21% / A3-9 sayari ~23%, two
  opposite-profile vaults), not a property the shipped check needs re-proved twice — and making
  acceptance hostage to a machine boundary is how a ledger silently stalls. **Note this ruling does
  NOT touch build-21 A3-14 or build-18 F3**, which remain **sayari-only and relay-or-nothing** —
  and the reason is worth stating precisely, because "vlt-core cannot host them" is a compressed
  claim that reads wrong. vlt-core is not *incapable* of overlays; it **has** none
  (`_agent/conventions/` holds only `.baseline/`; sayari holds a 19.7K `extraction.overlay.md`), and
  overlays are "**created lazily**" (`vlt-mint/SKILL.md:149`) — the file exists only once a
  vault makes a vault-local convention *addition*. So both checks lack a **subject** there, not a
  capability. Two reasons it has never grown one: (a) **its divergences were the wrong shape** — both
  historical ones were *base-level* (the operating-contract dispatch-slice re-graft, upstreamed in
  0.3.1; the `extraction` registry table, retired by owner ruling), and `vlt-mint:150` states "an
  overlay can only add; it cannot change an existing base rule. So a true rule change has **no
  overlay form**"; (b) **the module steers the factory vault away from overlaying** — `:150` directs a
  generic rule change to the base "and should be **filed upstream to the module**," which for the
  vault whose owner *is* the module owner is the cheaper path (hence three consecutive fully-on-stock
  closes). sayari overlays because it cannot upstream Sayari-specific rules to every vault. The
  precondition is therefore **counter-incentivized** on vlt-core, not merely absent — which is the
  real argument for relay-or-nothing.
  <br>**⚠ NEW FINDING 2026-07-25 — the `revisit_due` positive case is not lint-gated at all; it is
  an ADOPTION gap, and it is being filed.** Grounding this run: **zero of 96 vlt-core research
  notes carry `revisit_after:`** — including **all 4 written after the fix shipped**. The key is
  optional-by-design and partner-set at write time (`vlt-research/SKILL.md:71`,
  `frontmatter.md:138` — "**Absence = not a candidate**… only a note the writing partner judged
  graduation-relevant carries it"). So **no lint, full or scoped, can discharge the positive case**:
  it needs a note that carries the key. Four fresh notes ran the exact write flow and all four
  declined it — a **pass-through**, not a wait, which per the rubric's tripwire forbids re-annotating
  it as an ordinary STILL-OPEN tail. And the failure mode is the arc's own scar: *absence = zero
  findings* means **non-adoption reads as clean**, structurally identical to `spec.md`'s
  `deferral_metric` reading clean forever at zero specs. **Owner ruled: file it** as an adoption gap
  → `inbox/2026-07-25-144500-revisit-after-has-no-adoption-path.md`; `inbox-capture` routes it into
  an Arc-4 build, after which the tail gets a real trigger and can be graded honestly. The
  *absence-branch* half ("legacy notes generate no noise") is unaffected and still discharges on the
  full lint above.
  <br>**═══ FULL-LINT PASS 2026-07-25 — the discharging run happened; three clauses land, one
  FAILS.** Evidence: `_agent/log.md` `[2026-07-25 15:05] lint (librarian) | full` + its session
  record `_agent/sessions/2026-07-25-150500-lint.md` — 130 wiki pages through the `vlt-lint-full`
  fan-out (155 agents, 0 errors), plus the SKILL's own inline passes over 98 research notes, 16 PARA
  artifacts, 7 conventions, 11 capabilities. Exactly the `vlt-lint --full` run on vlt-core the
  2026-07-25 ruling named as the discharging event.
  <br>**DISCHARGED — `revisit_after` absence branch (legacy-notes-no-noise).** 96 research notes,
  **zero** carrying `revisit_after:`, and the full run surfaced **zero `revisit_due` findings and
  zero noise from the legacy corpus on that axis** — absence = not a candidate = silence, exactly as
  `frontmatter.md:138` designs it and the brief predicted ("trivial backfill by construction"). This
  is the population-level clause a 4-file scope structurally could not serve; it is now served.
  *Read narrowly:* the clause is about `revisit_after` absence only — the same legacy corpus **did**
  generate noise on the sibling `linkage_ripe` axis (below), and one must not be read as covering
  the other.
  <br>**DISCHARGED — honest scoping verified.** `vlt-lint-full.js` swept `{wiki}` only (130 pages);
  the `{research}`/PARA/conventions/capabilities passes ran inline in the SKILL's own jurisdiction,
  exactly as `vlt-lint/SKILL.md:43` splits them; the run reported **no coverage caps** and the
  session names its own under-delivery (buckets C/D flagged-only) rather than presenting a partial
  sweep as exhaustive.
  <br>**DISCHARGED — never-auto-promoting.** The 41 `linkage_ripe` hits were **surfaced and not
  acted on** — the human verified them before any promotion, and the run promoted nothing. The
  flag-for-human posture held under a 41-candidate load, which is the harder test.
  <br>**⛔ FAILED — "FP-rate tracks the calibrations (union ≪ naive)".** The full run's
  `linkage_ripe` projection returned **41 raw hits and 0 real candidates — a ~100% false-positive
  rate** (`_agent/sessions/2026-07-25-150500-lint.md:26`: "41 `linkage_ripe` graduation candidates →
  **0** — all resolved to notes that had *already* graduated"; cost-if-trusted recorded as "would
  have re-graduated filed material"). The brief's own failure signature is met and exceeded: 100% is
  not merely off the ~21–23% union calibration, it is **worse than the ~69–79% naive baseline** the
  check exists to beat. **Root cause, grounded in module source, and it is structural rather than a
  tuning miss:** the union's three components — `topic:` overlap with a wiki page ∪ an inbound body
  `[[wikilink]]` from a wiki page ∪ shared `sources:` with a wiki page (`vlt-lint/SKILL.md:83`) —
  are **precisely the residue that graduation itself leaves behind**, and the research-note schema
  carries **no graduation-state key whatsoever** (`frontmatter.md:136-138` — `type: research` notes
  are written-once, no `last_updated`, no back-pointer to the page they fed; `revisit_after` is the
  *only* candidacy key and is absence-by-default). So the projection is structurally unable to
  distinguish *ripe for graduation* from *already graduated*, and its false-positive rate rises
  toward 100% as a vault matures — the opposite of the intended behavior. Vault-side drift is ruled
  out: vlt-core's `.claude/skills/vlt-lint/SKILL.md` is **byte-identical to factory source**
  (`diff -q`, this run), so the defect attributes to module source. **Honest limits recorded:**
  (a) the 41-hit list was not preserved, so the finding rests on the vault's own verification of the
  set rather than a re-derivable enumeration; (b) the session groups this class with genuine
  *delegate* measurement errors (the 7 over-length summaries, the 55 cross-layer link artifacts),
  and `linkage_ripe` is a SKILL-inline pass per `:43` — so *how* it was computed is not fully
  established, though what was verified (every surfaced note had already graduated) is
  computation-independent; (c) the A3-8 calibration that produced ~21% was measured on **this same
  vault** on 2026-07-11, so the gap between 21% and 100% is itself unexplained and is the sharpest
  open question for the filing — most likely the calibration sample excluded already-graduated
  notes, i.e. measured the projection on the population it was *hoped* to run against rather than
  the one it actually runs against. **Filed** → `inbox/2026-07-25-162416-linkage-ripe-cannot-see-graduation.md`;
  routes into the next `inbox-capture` as an Arc-4 candidate. The clause stays unchecked and is
  **not** a waiting tail — it has been exercised and it failed.
  <br>*Item disposition after this pass:* `topic:`-fix-took ✓, Q2 fix-then-measure ✓, handshake@4 ✓,
  legacy-no-noise ✓, honest-scoping ✓, never-auto-promote ✓ — **FP-rate FAILED (filed)**, and the
  `revisit_due` positive case remains the separately-filed adoption gap. Build-20's box stays
  unchecked and now closes on the Arc-4 fix of the `linkage_ripe` defect, not on any further lint.
  <br>**⚠ CLAUSE SUPERSEDED 2026-07-25 by SPIKE-1 (ideation, A3-18..A3-23) — the FAILED verdict
  STANDS; its wording and its stated root cause do not.** The grade is unchanged: the check
  returned 41/0 and that is a real failure. Three corrections ride on top, none of which rescues
  the clause:
  <br>(1) **The clause is unsatisfiable as written.** "FP-rate tracks the calibrations
  (~21–23%)" compares an FP rate to a **set-reduction ratio**: 21% is vlt-core's union residual
  as a share of the *naive flagged set* (13/62, `research-wiki-audit-2026-07-11.md:69`) and 23%
  is vlt-sayari's union *flag rate over population* (3/13, `…114837:20`). The union's measured FP
  rate was ≈**0%** — the residual 13 is exactly the genuine-gap set (8 partial + 5 orphaned).
  **Restated target for the Arc-4 fix:** *the projection's false-positive rate, hand-verified on
  a mature research zone, is near the calibration's ≈0% and must not exceed the naive signal's
  ~79%* — an FP rate compared against an FP rate.
  <br>(2) **Root cause restated.** Not "the components are graduation residue + no state exists"
  but a **polarity inversion**: in both calibrations the union is an **absorption test**
  (citation ∪ body wikilinks ∪ shared-source ⇒ the note is *already absorbed* ⇒ **exclude**);
  ripe meant **no** linkage. `vlt-lint:83` fires the same signals inverted, so it surfaces the
  set the calibration excluded. Two further drifts: `topic:` overlap replaced the
  **frontmatter-citation** leg, and the name was taken from A3-7's `linkage_ripe`
  (`…114226:49` — "a newer note cites/links this orphan"), a third meaning again. Entered at
  `build-20-graduation-queue.md:211-216`, not at capture.
  <br>(3) **Honest-limit (c) is RETRACTED.** The calibration did **not** exclude already-graduated
  notes — all 90 were in sample, 76 already absorbed (`audit:13-21`). The 21%→100% gap is fully
  explained by (1) and (2), and the A3-17 discharge-against-a-non-adopting-population class stays
  at three instances. Limits (a) and (b) stand.
  <br>*Consequence:* the Arc-4 fix (A4-1) may be **smaller** than the filing sized it — restoring
  polarity and the citation leg needs no graduation-state key and no `frontmatter@5` bump. Not
  settled: SPIKE-2 must confirm the absorption test still reproduces before any sizing is fixed.
  <br>**⚠ SEVERITY UPDATED 2026-07-25 by SPIKE-2 — the 41/0 measurement was an UNDERCOUNT.**
  Exactly 41 of the then-96 notes carried a **list-form `topic:`** at candidacy time; the same
  sweep auto-fixed **55 scalar `topic:` → YAML lists** (`sessions/2026-07-25-150500-lint.md:52`,
  build-20's own F1 fix), so the scalar cohort was invisible to the overlap leg and silently
  damped the projection. All 98 notes are now list-form: a read-only re-run in the shipped
  polarity surfaces **97 of 98 (99%), 90 of them already absorbed (≥93% FP)**. **The next
  ordinary `vlt-lint` run on vlt-core will surface ~97, not 41** — the failure is latent, ~2.4×
  worse than graded, and grows precisely because build-20's `topic:` fix was correct. The
  calibration polarity on the same disk surfaces **8 of 98** and correctly excludes the four
  audit-identified gaps that have since graduated while still surfacing the one that has not.
  Enumeration preserved: `skills/reports/spike2-projection-baseline-2026-07-25.md` (the original
  41-hit list is unrecoverable — its substrate was destroyed by the auto-fix in the same run).
  <br>**⚖️ CLOSED 2026-07-26 — ALREADY CARRIED to Arc 4** by the 2026-07-25 arc-boundary ruling (b);
  no new disposition was needed at closeout. The FAILED grade stands and travels with its restated
  target to the Arc-4 ledger (*Inherited from Arc 3*); **A4-1 shipped the polarity fix and A4-2 the
  adoption unit in v0.8.0**, so this clause discharges on Arc 4's acceptance run, not Arc 3's. The
  separately-filed `revisit_due` adoption gap became A4-2. The spike-2 baseline stays live at
  `skills/reports/` (deliberately unarchived — A4-1's acceptance reads it). See the *Closeout
  dispositions* block at the head of this ledger.
- [ ] **build-21 (history-writes, briefed 2026-07-17):** next ordinary vlt-core/vlt-sayari
  upgrade — **A3-14 downstream (gate-2 non-vacuous):** at vlt-sayari's next upgrade past this
  build, `extraction.overlay.md:13` (naming `vlt-track`) is now **base-subsumed** — build-18's
  overlay-subsumption pass fires and offers to retire that redundant section (a pre-fix overlay
  that could have failed, correctly detected — not engineered evidence). **Handshake took:** all
  three `extraction` consumers (`vlt-extract`, `vlt-lint`, `vlt-track`) pin `extraction@3`, none
  pins `@2`; a live `vlt-lint` run reports zero convention-coherence findings for `extraction`;
  the false clause ("no skill shipped with the module uses it" / "No shipped op uses this") is
  gone from both former sites and `vlt-track` is named in the base. **A3-15 write path lands:**
  a fresh install seeds `_agent/mint/decision-log.md` from the shipped template (header + read-
  order statement present); the first live upgrade that makes a gated ruling writes a real
  supersession-bearing entry to the **decision log** (not the ledger alone), propagating to any
  governing prose it changes; the `vlt-core` firewall ruling (`upgrade-ledger.md:48`) gets its
  superseding decision-log entry when next reconciled. **F8 migration behaves:** on a live log
  with a pre-existing unaccounted gated convention edit, the migration surfaces it **human-gated**
  (never auto-writes/auto-restores) and honestly flags pre-schema (no-`kind:`) entries it cannot
  classify. **A3-11 §4a derive-first holds:** the invariant sentence is present at the Step-1
  snapshot/ledger seam with its sibling pointer, and a post-upgrade session preserves disk-derived
  local growth (capabilities/mints/families) without consulting the prior ledger as its checklist
  — observable on the next sayari-style "grew-N-since-last-upgrade" run. **Must NOT be read as
  landing Fix D (upgrade-refuses-to-proceed posture) or a governance-wide supersession
  convention** — both explicitly deferred.
  <br>*Named carry-forward debt (Q21 ruling — bespoke now, converge later):* the decision log
  ships its **own** supersession idiom this build; the governance-wide convergence (wiki + spec +
  decision log as three consumers of one supersession convention) is recorded here as a tracked
  debt with a live home so `arc-closeout` carries it forward — not a note in a closable tree.
  <br>**A3-15 write path + F8 migration DISCHARGED 2026-07-18 (vlt-core 0.7.0 upgrade) — the
  headline discharge of this run.** The 0.7.0 upgrade is *the first upgrade to make a gated
  ruling and write it through*: `decision-log-write` + `decision-log-reconcile` ran and wrote
  the **2026-06-24 firewall ruling** (retire the `(partner → PARA target)` registry table;
  adopt the invariant model) — which had reached only `upgrade-ledger.md:48` — as a superseding
  entry into `_agent/mint/decision-log.md`, marking the two 2026-06-13 entries **superseded in
  place** (verified on disk: `decision-log.md:203-206` carries the `⚠ SUPERSEDED (marked in
  place 2026-07-18)` banner with `superseded_by:`/`superseded_date:`/`superseded_reason:`; the
  read-order warning header is live at `:8-10`). Propagated to governing prose was a **no-op by
  correctness** — shipped `extraction.md@3` already encodes the invariant model, so no
  convention bump; only the log was stale. **Fresh-install seed half:** `decision-log-template.md`
  now ships and is present at `vlt-mint/assets/decision-log-template.md` (3.1KB; the new-file
  addition the manifest recorded, 42→43). **F8 migration behaves:** `decision-log-reconcile`
  surfaced 3 pre-schema (no-`kind:`) entries as **cannot-classify, flagged for manual review,
  never auto-written/auto-restored** — each self-describes light/own-zone/ungated, correctly
  human-gated (`upgrade-ledger.md` [2026-07-18 12:44] §Decision-log). **Handshake structural
  half:** `extraction.md@3` names `consumers: [vlt-extract, vlt-lint, vlt-track]`, all three
  ack `extraction@3` (none at `@2`), and the false "no shipped op uses this" clause is **gone**
  from the base (grep-confirmed absent, factory + vault). **A3-11 §4a derive-first exercised:**
  the 0.7.0 pre-flight enumerated the 4 partners + all vault-grown capabilities **from disk**
  (`upgrade-ledger.md` §Pre-flight snapshot lines), not from the prior ledger entry.
  <br>*STILL-OPEN:* **A3-14 downstream** — needs **vlt-sayari's** next upgrade past this build
  for build-18's overlay-subsumption to fire on the now-base-subsumed `extraction.overlay.md:13`
  (trigger: owner-run sayari upgrade); and the *live* `vlt-lint` zero-`extraction`-coherence
  confirmation (no lint run since the upgrade — trigger: next `vlt-lint` run).
  <br>*Live extraction-coherence confirm DISCHARGED 2026-07-18 (post-0.7.0-lint pass).* The
  `[2026-07-18 13:15]` run supplies the *live* `vlt-lint` zero-`extraction`-coherence
  confirmation the upgrade-side discharge still owed: the governance pass on the 0.7.0-upgrade
  delta reports all consumer `depends_on` pins current including `extraction@3`, zero coherence
  findings, 3 changed base conventions pristine vs `.baseline`, 3 `track.md` capabilities
  lane-safe. **A3-14 downstream STAYS STILL-OPEN** — build-18's overlay-subsumption firing on
  vlt-sayari's now-base-subsumed `extraction.overlay.md:13` needs **vlt-sayari's next upgrade
  past this build**, and vlt-sayari is still at 0.6.0 (last upgraded 2026-07-09, untouched
  since 07-11). Trigger: an owner-run sayari 0.7.0 upgrade.
  <br>*Unmoved 2026-07-25 (fresh-note pass).* vlt-sayari is **still at 0.6.0** — no upgrade, no
  vault activity since 2026-07-11, independently re-confirmed today by
  `inbox/2026-07-25-132141-partner-consult-synchronous-channel.md:107` ("Vault: `vlt-sayari` (work
  machine, currently 0.6.0)"). A3-14 downstream STILL-OPEN; trigger unchanged (owner-run sayari
  0.7.0 upgrade).
  <br>*Unmoved 2026-07-25 (full-lint pass), extraction-coherence re-confirmed at full scope.* The
  `[2026-07-25 15:05]` full run reports **every consumer `depends_on` pin current** and **7
  conventions pristine vs `.baseline`** across the whole governance surface — the *Handshake took*
  half (discharged 07-18 on a 4-file scope) now holds on a full sweep. **A3-14 downstream STILL-OPEN
  and it is the arc's most stubborn tail:** vlt-sayari has sat at 0.6.0, untouched since 2026-07-11
  — 14 days — and only its own upgrade can fire build-18's subsumption on
  `extraction.overlay.md:13`. Trigger unchanged (owner-run sayari 0.7.0 upgrade); it is the one tail
  on this ledger with no substitute path and no clock.
  <br>**⚖️ CLOSED 2026-07-26 — RELEASED as a sayari-relay watch.** Not ticked: the check was never
  exercised, it was released (the build-19 form). Q21's governance-wide supersession convergence
  carries forward. See the *Closeout dispositions* block at the head of this ledger.
- [ ] **build-22 (mint-and-wearer, briefed 2026-07-18):** next ordinary vlt-core/vlt-sayari
  upgrade — **F1 panel widened (non-vacuous only on a roster-changing mint):** a real `new partner`
  or `retire a partner` mint convenes the **full four-lens panel** (architect + skeptic + pragmatist
  + historian) directly via `KIND_PANEL`, *not* via the debate-mode workaround build-15 recorded, and
  build-16's bell question reaches all four; an additive/reversible kind still skips the council (no
  regression). **F2 field mint stays local:** the next `vlt-mint` partner/heavy-cap mint registers
  **only** in the live `_bmad/module-help.csv`; the shipped `vlt-setup/assets/module.yaml agents[]`
  and `vlt-setup/assets/module-help.csv` stay the pristine shipped set (no local mint written in);
  B1 still reports the mint preserved across the upgrade. **F3 B2 classifier robust:** vlt-core's four
  local mints (chef, chess-coach, dog-trainer, health-coach) all classify as **local** at pre-flight
  off the pristine incoming source and appear in the minted-partner snapshot — *honesty bound:*
  vlt-core's live `agents[]` is currently clean, so the hardening guards a state the corrected
  instruction no longer produces; the load-bearing check is *machinery* (a post-fix mint doesn't
  pollute), the classifier robustness being belt-and-suspenders until a polluted-`agents[]` instance
  exists. **F4 loop-profile migration — the gate-2 migration check, non-vacuous against the pre-fix
  population:** the migration offer **detects and offers to relocate** dog-trainer's inline profile
  (shape a) **and** health-coach's `### Loop profile` section (shape b) into each partner's
  `capabilities/track.md`, human-gated; both partners *predate* build-11's rehoming and *could* have
  failed — the valid discharge. A post-fix wearer (chess-coach, Navigator) is **not** valid evidence
  for F4. Idempotent — a second upgrade finds nothing mislocated. **Must NOT be read as** discharging
  the deferred lint-detector/"should wear" follow-up or opening the mint-upstreaming path (both
  tracked debts below).
  <br>*Named carry-forward debts (this build):* (1) **Q27 — the standing `vlt-lint` loop-profile
  detector + its roster-level "should wear track" declaration** (deferred: needs a declaration
  substrate that overlaps build-20's frontmatter@4 adoption facet; F4's migration offer covers the
  actual drifted population without it). (2) **Q24 — a sanctioned deliberate mint-upstreaming path**
  (no module-source home today; owner seed: public repo + peers, vlt-core the only ship-upstream
  instance, inbox-rail-analogue the promising shape, private/public friction the open tension). Both
  recorded with live homes so `arc-closeout` carries them forward.
  <br>**F3 + F4 DISCHARGED 2026-07-18 (vlt-core 0.7.0 upgrade) — the two gate-2 / robustness
  checks, exact subject-match.** *F4 loop-profile migration (the gate-2 migration check,
  non-vacuous against the pre-fix population):* the `loop-profile-relocation` migration
  **detected and offered to relocate dog-trainer's inline profile (shape a) AND health-coach's
  `### Loop profile` section (shape b)** into each partner's `capabilities/track.md`,
  human-gated (both user-approved) — verified on disk: `_agent/partners/{dog-trainer,
  health-coach}/capabilities/track.md` now present (1.5K / 4.3K), and
  `vlt-agent-dog-trainer/SKILL.md:39` now carries the one-line pointer ("its single home… this
  file deliberately does not restate it"). Both partners **predate build-11's rehoming and
  could have failed** — named subjects matched exactly, not a post-fix substitute. Idempotent:
  chess-coach already externalized, chef has no loop — the pass found nothing else to move.
  *F3 B2 classifier robust:* the 0.7.0 pre-flight classified vlt-core's **four local mints
  (chef, chess-coach, dog-trainer, health-coach) as local off the pristine incoming source**,
  and **none had self-registered into a live `agents[]`** (`upgrade-ledger.md` [2026-07-18
  12:44] §Pre-flight) — the *honesty bound the brief states holds:* live `agents[]` is clean, so
  this guards a state the corrected instruction no longer produces; the load-bearing machinery
  (a post-fix mint doesn't pollute) is confirmed, robustness is belt-and-suspenders until a
  polluted instance exists.
  <br>*F1 + F2 STAY STILL-OPEN — both need a next mint, none since the upgrade.* F1 (full
  four-lens panel via `KIND_PANEL`, non-vacuous) needs a **roster-changing** `new partner` /
  `retire a partner` mint; F2 (field mint registers only in live CSV, shipped
  `module.yaml agents[]` + `vlt-setup` CSV stay pristine) needs any `vlt-mint` partner/heavy-cap
  mint. Trigger for both: an owner-run mint (a roster-changer for F1).
  <br>*No F1/F2 discharge from post-0.7.0 activity 2026-07-18 (post-0.7.0-lint pass).* The only
  post-upgrade mint is the **capability-refine (answer-key)** — own-zone, council-none,
  **not** roster-changing and **not** a partner/heavy-cap mint. **F1 STILL-OPEN** (needs a
  `new partner` / `retire a partner` mint convening the full four-lens `KIND_PANEL`; a
  council-none capability-refine convenes no panel). **F2 STILL-OPEN** on its literal subject
  (a partner/heavy-cap mint writing a live-CSV row) — *corroborating machinery only:* the
  answer-key mint worked from the corrected `vlt-mint` Step-4 provenance text and registered
  **locally without polluting** shipped `module.yaml agents[]` / `vlt-setup` CSV (the A3-16 /
  091000 fix exercised, confirmed in vlt-core's decision-log "Done"), but it adds no CSV row so
  the registration path itself stays untested. Trigger for both unchanged: an owner-run mint
  (a roster-changer for F1, any partner/heavy-cap for F2).
  <br>*Still no F1/F2 discharge 2026-07-25 (fresh-note pass) — 2nd unfired run, so reachability
  was re-examined per the tripwire rather than re-annotated.* The one further post-upgrade mint is
  `add-a-capability (creative) — walkthrough-renderer` (`_agent/mint/decision-log.md:526`,
  `_agent/log.md` `[2026-07-18 15:45]`) — **light / own-zone / council-none**, so it convenes no
  panel (F1 needs a roster-changer) and it "Registered nothing in the help CSV (light = own-zone,
  surfaced on activation)", so it writes no live-CSV row (F2's literal subject). **F1 reachable:**
  `vlt-mint/SKILL.md:59` still names `new partner` / `retire a partner` among the gated kinds and
  `:94`'s fixed `kind → council` map is what selects `KIND_PANEL` — a shipped surface can produce
  the event; the owner has not run one. **F2 reachable, and its *pristine* half re-corroborated at
  rest this run:** vlt-core's shipped `.claude/skills/vlt-setup/assets/module-help.csv` is still
  **15 lines (header + the 14 shipped rows)** against a live `_bmad/module-help.csv` of **19**, and
  the shipped `assets/module.yaml` `agents[]` still carries only the stock roster
  (librarian/researcher/creative…) — two post-upgrade mints later, zero local-mint bleed into
  upgrade-refreshed assets. Both STILL-OPEN, triggers unchanged.
  <br>*Unmoved 2026-07-25 (full-lint pass) — and, unlike the last two passes, this one produced no
  mint at all.* `_agent/mint/decision-log.md` still ends at the 07-18 `walkthrough-renderer` entry:
  zero mints of any kind since. That matters for the tripwire bookkeeping — this is **not** a third
  pass-through (no mint ran and declined to fire the check); the discharging *kind* of event simply
  did not occur, so the reachability re-examination recorded on 07-25 (`vlt-mint/SKILL.md:59`/`:94`
  produce the event; the owner has not run one) stands unrevised. F1 needs a roster-changing
  `new partner`/`retire a partner` mint; F2 needs any partner/heavy-cap mint writing a live-CSV row.
  Triggers unchanged, both owner-run.
  <br>**⚖️ CLOSED 2026-07-26 — both RELEASED as watches.** Not ticked: never exercised, released
  (the build-19 form). Q27 (lint loop-profile detector + roster-level "should wear track") and Q24
  (sanctioned mint-upstreaming path) carry forward. See the *Closeout dispositions* block at the head
  of this ledger.
- [ ] **build-23 (content-verification, briefed 2026-07-18, SHIPPED 2026-07-18 @ dbcf018 tag v0.7.0; release build — v0.7.0):** next ordinary
  vlt-core/vlt-sayari upgrade *plus* the v0.7.0 release itself — **the gate rings on real drift, not
  just seeds:** the next arc's first build that touches a convention `version:`, a `consumers:` list,
  or the structure map runs `package-lint` Group E as its handshake verification **instead of** a
  hand-written `grep "<name>@"`, and the brief/commit shows Group E — not the self-confirming grep —
  as the check of record (the process-adoption proof: the self-confirming grep every build 19–22 wrote
  by hand stops being written because the gate now owns the check). **A non-vacuous catch:** Group E
  FAILs at least once on a genuine mid-development drift (a consumer walk missed a re-ack, or a map row
  lagged an SSoT edit) **before that drift can be tagged** — caught at the gate, not in a later field
  filing; if no qualifying drift arises before the next version, the discharge is **vacuous by
  construction (gate 2 / Q28)** and must be recorded as such by explicit owner note, never a substitute.
  **F4 in the field:** a maintainer or minted partner reading `vlt-lint:74` in an installed vault
  understands the coherence check verifies the *pin*, not conformance, and knows the dev-side net exists
  — evidenced by a field interaction citing the limit correctly rather than re-filing "the handshake
  passed but the body drifted" as a new defect. **Must NOT be read as** landing the vault-side
  conformance spot-check, a general negative-claim detector, or any acceptance-ledger-vacuity fix — all
  explicitly out of scope (the vacuity rule is already Gate 2 dev-process, not module source).
  <br>*Named carry-forward debt (this build):* the **vault-side conformance spot-check** (extend
  `vlt-lint:74` to re-read each installed consumer's body against the convention rules — the named
  second cut) is deferred with a live home so `arc-closeout` carries it forward; it targets vault-local
  minted reciters and awaits field evidence of drift.
  <br>**Release-side DISCHARGED 2026-07-18 (v0.7.0 tag).** `package-lint` Group E
  (self-description integrity) **ran and passed at the pre-tag gate**: release commit `dbcf018`
  records `package-lint: A/B/C/E PASS, D PASS — vlt 0.7.0 (uv run tools/package-lint.py
  --expect-version 0.7.0, exit 0)` — the gate the build shipped exercised itself on the very
  release that shipped it. **STILL-OPEN (first-exercise, all in the next arc's development):**
  the *process-adoption* proof — the next build that touches a convention `version:`,
  `consumers:` list, or the structure map runs Group E as its handshake check **instead of** a
  hand-written `grep "<name>@"` (trigger: the next handshake-bumping build); a **non-vacuous
  catch** — Group E FAILing on a genuine mid-development drift before it can be tagged (**vacuous
  by construction so far** — no qualifying drift arose across builds 19–23; per gate-2 / Q28 this
  must be recorded by explicit owner note, never a substitute, if the next version also produces
  no drift); and **F4 in the field** — a maintainer/minted partner citing `vlt-lint:74`'s
  pin-not-conformance limit correctly rather than re-filing it (trigger: a field interaction).
  <br>*Unmoved 2026-07-25 (fresh-note pass).* No build has been started since v0.7.0 shipped, so
  no handshake-bumping build exists to adopt Group E as its check of record (process-adoption tail);
  no qualifying mid-development drift has arisen, so the non-vacuous-catch clause is **still
  vacuous by construction** — **owner ruled 2026-07-25: the Q28 vacuity note is NOT due yet**, since
  Q28 conditions it on the *next version* also producing no qualifying drift and no build has
  started since v0.7.0; writing it now would pre-empt its own condition. Re-read at the next
  release, not before; F4-in-the-field unmoved (no field interaction citing `vlt-lint:74`). Note the arc's
  next natural build is the Arc-4 candidate filed today
  (`inbox/2026-07-25-132141-partner-consult-synchronous-channel.md`), whose strongest recommendation
  is a **handshaked `{conventions}/consult.md` with `version:`/`consumers:`** — i.e. the
  process-adoption tail has a concrete, already-filed occasion waiting for it.
  <br>*Unmoved 2026-07-25 (full-lint pass) — no build started since v0.7.0, so all three tails are
  untouched* (process-adoption, the still-vacuous-by-construction non-vacuous catch with its Q28 note
  **still not due**, and F4-in-the-field). One thing did change around it: the Arc-4 candidate pool
  grew by three filings today (`partner-consult-synchronous-channel`,
  `revisit-after-has-no-adoption-path`, and this pass's `linkage-ripe` FAILED filing), which makes
  the next handshake-bumping build — the process-adoption trigger — materially likelier to be
  scheduled soon. Trigger unchanged: the next build that touches a convention `version:`,
  `consumers:` list, or the structure map.
  <br>**═══ CLOSEOUT PASS 2026-07-26 — the trigger fired twice, and the process-adoption clause
  FAILED.** v0.8.0 shipped five Arc-4 builds, two of which touched a convention `version:`/`consumers:`
  — **A4-3** (`wiki-supersession 1 → 2`, four consumers re-acked) and **A4-5** (new `consult@1`, two
  new acks). Both wrote the hand-written grep the clause says must **stop being written**: A4-3's
  verification check **1**, titled *Handshake bipartite*, is `grep -rn "wiki-supersession@" skills/`
  with Group E demoted to check 9 and hedged as *"the mechanical net for the handshake in check 1"*
  (`build-A4-3-contradiction-drain.md:469-471,494`); A4-5's check **4**, *Handshake bipartite (the
  standing ritual)*, is a manual `consumers:` ↔ `depends_on:` cross-read plus `git diff`, with
  `grep -rn "consult@"` at check 5 (`build-A4-5-consult-channel.md:615-620`). **The gate is not at
  fault** — Group E ran and PASSED on all five builds and A4-5's design section names it as the
  authority (`:571`). **Root cause is the brief scaffold:**
  `.claude/skills/build-brief/references/brief-anatomy.md:94-95` states the ritual with **no tool
  named**, so each builder invents one, and `:96` still calls the mid-arc run **`A/B/C`** — Group E
  did not exist when that line was written and build-23 never updated it. The clause asked builders
  to stop doing what their own instructions still told them to do. **FILED** →
  `inbox/2026-07-26-141500-group-e-did-not-retire-the-handwritten-handshake-grep.md`; closes on an
  Arc-5 fix, not on further waiting.
  <br>**✅ Q28 NON-VACUOUS-CATCH NOTE — DUE AND HEREBY WRITTEN (owner note, 2026-07-26).** Q28
  conditioned this note on *the next version also producing no qualifying mid-development drift*.
  v0.8.0 has now shipped and the condition is met: **no Group E FAIL occurred across A4-1…A4-5** —
  every build commit records `A/B/C/E PASS` and the release commit `557347f` records
  `A/B/C/E PASS, D PASS`; A4-5's only PARTIAL is the pre-existing `sources_vs_prose_mismatches:`
  template fence break, which is not a handshake failure. **Recorded explicitly as VACUOUS BY
  CONSTRUCTION across two versions (0.7.0 and 0.8.0), never as a substitute discharge.** Group E's
  *detection* power therefore remains unexercised on real drift — stated plainly so no reader mistakes
  two clean releases for a demonstrated catch. This sub-clause is **discharged**; per gate 2 a vacuity
  note is the honest close, not a tick of the underlying capability.
  <br>**⚖️ F4-in-the-field → WATCH.** See the *Closeout dispositions* block at the head of this ledger.
- [ ] **Design-stage evidence debts (vault-side, before their builds close acceptance):**
  091003 M0 counter-accuracy audit + tripwire-hit data; ~~091005 two measured lint cycles
  under the attestation contract (M4)~~; 091006 first review-cycle evidence (does the
  due-queue get worked). Filed as pending attachments by the filings themselves.
  <br>*Partially discharged 2026-07-17* — **091005 M4 PAID** (the 07-08 full + 07-13 scoped
  cycles; detail on build-16's item above). **Still owed:** 091003 M0 counter-accuracy audit +
  tripwire-hit data (build-17 unbuilt, so no counters exist to audit yet — this debt cannot be
  paid before its build ships, and should be re-read at build-17 brief time rather than treated
  as a standing tail); 091006 first review-cycle evidence — **still unrun, and the reason is now
  known**: the 07-13 scoped lint reports *"no expired deferrals"* and no `review_due` findings,
  i.e. **nothing is due yet**, so the queue has had nothing to work. `review_after:` itself is
  confirmed live and shipped — the 07-17 creative session grounded it at
  `enforcement_stage: checked` with lint's `review_due` check present (and corrected a stale
  vault backlog item that assumed it was pending). So 091006 waits on the **first date to come
  due**, which is a genuine clock-tail, not a design gap — unlike build-15's, this one will fire
  on its own. Earliest known trigger: `spec.md`'s own `review_after: 2026-08-17`.
  <br>*No change from the 0.7.0 upgrade 2026-07-18.* 091003 M0 still unpayable (build-17
  unbuilt — no counters to audit); 091006 still waits on the first `review_after:` to come due
  (clock, 2026-08-17). Both tails unmoved by this release.
  <br>*Unmoved 2026-07-25 (fresh-note pass).* 091003 M0 still unpayable (build-17 unbuilt).
  091006 is **23 days from its clock** — `spec.md`'s `review_after: 2026-08-17` has not come due;
  this is the one tail on the whole ledger that fires without an owner action.
  <br>*Unmoved 2026-07-25 (full-lint pass).* 091003 M0 still unpayable (build-17 unbuilt — no
  counters exist to audit). 091006 unmoved at **23 days from its clock**; the full lint independently
  corroborates *why* it is silent rather than broken — the run reported no `review_due` findings and
  no expired deferrals across 7 conventions, i.e. the due-queue is empty because nothing is due, not
  because the check is dark.
  <br>**⚖️ CLOSED 2026-07-26.** 091003 M0 **FOLLOWS build-17 into Arc 5** — the owner ruled build-17
  folded into Arc 5's capture, so its unpayable counter-audit debt travels with it rather than
  outliving the arc as a standing tail (the circularity the 07-17 note named is resolved by moving
  both, not by waiting). 091006 → **DATED WATCH** (2026-08-17, 22 days). See the *Closeout
  dispositions* block at the head of this ledger.

---

## Carried forward past Arc 3 (recorded at close, 2026-07-26)

**This section is the authoritative hand-off point.** The next arc's `inbox-capture` re-lists these
from this archived roadmap; anything left off is silently dropped. Phrasing per the Arc 2 form.

### Standing watches — released, not exercised

Each was **released** at close because its discharging event has no reachable subject, not because it
was verified. None may be read as passed.

- **build-19 — empty-`_agent/specs/` lint negative case.** Carried from build-19's 2026-07-25 owner
  release — STILL OPEN at Arc 3 close, carries forward past Arc 3. Discharges on the first
  fresh-install vault that runs a lint with an empty specs zone. Both known vaults are non-empty.
- **build-18 F3 — a post-upgrade write op honoring an overlaid convention rule.** Carried from
  build-18 — STILL OPEN at Arc 3 close, carries forward past Arc 3. **Sayari-relay only:** vlt-core
  carries zero overlays and `vlt-mint:150` counter-incentivizes growing one.
- **build-21 A3-14 — overlay-subsumption on the now-base-subsumed `extraction.overlay.md:13`.**
  Carried from build-21 — STILL OPEN at Arc 3 close, carries forward past Arc 3. **Sayari-relay
  only**, and the arc's most stubborn tail: no substitute path and no clock.
- **build-22 F1 — full four-lens `KIND_PANEL` on a roster-changing mint.** Carried from build-22 —
  STILL OPEN at Arc 3 close, carries forward past Arc 3. Needs a `new partner` / `retire a partner`
  mint the vault has no reason to run.
- **build-22 F2 — a partner/heavy-cap mint registering only in the live CSV.** Carried from
  build-22 — STILL OPEN at Arc 3 close, carries forward past Arc 3. The *pristine* half is
  re-corroborated at rest (shipped CSV 15 lines vs live 19, shipped `agents[]` stock-only); the
  registration path itself is untested.
- **build-23 F4 in the field** — a maintainer or minted partner citing `vlt-lint:74`'s
  pin-not-conformance limit correctly rather than re-filing it. Carried from build-23 — STILL OPEN at
  Arc 3 close, carries forward past Arc 3.

### Named actions with a trigger

- **build-18 F1 — `skill_asset_divergence` detect. STAGED.** Before the pending vlt-core 0.7.0→0.8.0
  upgrade, deliberately edit one line in `.claude/skills/vlt-mint/assets/*` in the vault. The upgrade
  then exercises or fails the detector. Note that A4-5 shipping a *new* asset (`vlt-consult.js`) is
  the legitimate refresh path, **not** a divergence — the test needs a vault-local edit.
- **091006 / build-16 — first review-cycle evidence. DATED WATCH, 2026-08-17** (`spec.md`'s own
  `review_after:`). The one carried item that fires without owner action.

### Tracked design debts (named at brief time, with live homes)

- **Q21 — governance-wide supersession convergence** (wiki + spec + decision log as three consumers
  of one supersession convention). The decision log ships its own idiom; convergence deferred. From
  build-21 — carries forward past Arc 3.
- **Q27 — standing `vlt-lint` loop-profile detector + its roster-level "should wear track"
  declaration.** Needs a declaration substrate overlapping build-20's frontmatter adoption facet.
  From build-22 — carries forward past Arc 3.
- **Q24 — a sanctioned deliberate mint-upstreaming path.** No module-source home today; owner seed:
  public repo + peers, vlt-core the only ship-upstream instance, the inbox rail as the promising
  shape, private/public friction the open tension. From build-22 — carries forward past Arc 3.
- **Vault-side conformance spot-check** — extend `vlt-lint:74` to re-read each installed consumer's
  body against the convention rules, not just its pin. Targets vault-local minted reciters; awaits
  field evidence of drift. From build-23 — carries forward past Arc 3.

### Standing metrics

- **091002 — zero packaging filings for releases ≥ 0.6.0.** **HOLDING** at close: three releases
  (0.6.0, 0.7.0, 0.8.0) and 18 filings, none a packaging filing. Re-probes each release; carries
  forward past Arc 3.

### Owner actions filed elsewhere

- **File the bmad-module-builder template drift** (`after,before` in the template merge script +
  tests) upstream to BMAD-METHOD. Carried from Arc 2 — STILL OPEN at Arc 3 close, carries forward
  past Arc 3. No arc owns it; no arc should hold for it.

### Transferred to Arc 5

- **build-17 — the enforcement kit, never built (evidence-blocked).** **Owner ruled 2026-07-26:
  folded into Arc 5.** Its remit (derived vitals, tripwire registry, the SessionStart moment, the
  ledger surface) and its filing `inbox/2026-07-06-091003-enforcement-kit-derive-first.md` transfer
  to Arc 5's capture. **Arc 3 closes with one build unshipped** — stated plainly rather than left
  undeclared.
- **091003 M0 — counter-accuracy audit + tripwire-hit data.** Travels with build-17; unpayable until
  counters exist.

### The durable fix this arc earned (highest-value carry-forward)

**Arc 3 could not close for 18 days because its ledger conflated two kinds of claim under one
checkbox.** The fix is at brief time, not at closeout:

1. **`build-brief`** — every acceptance check gets tagged **ship-verifiable** (at rest, at the
   release gate, or on the next upgrade — bounded) or **field-contingent** (needs an event of a
   specific kind — unbounded) when it is written.
2. **`arc-closeout`** — **only ship-verifiable checks may gate closeout.** Field-contingent checks go
   to a watch register that outlives arcs by design, which is what this section has become by hand.
3. A field-contingent check should also name, at brief time, **which vault can produce its event** —
   four of Arc 3's nine stuck tails needed a vault the factory machine cannot read, and none said so
   until discharge time.

Arc 4's ledger has the same shape and will strand the same way if this is not done before its
acceptance runs.

### Filings archived at close — and the criterion, which was widened

**Five filings moved to `inbox/archive/` at this close.** Two under the standing rule, three under a
widened one the owner ruled on 2026-07-26. Recorded here because it is a **rule change**, not a
judgment call to be re-made silently each closeout.

- **Under the standing rule** (*a filing archives once its build has shipped **and** passed
  acceptance* — CLAUDE.md lifecycle step 7): `…-114910-dev-zone-contract-graduation.md` and
  `…-092341-spec-convention-has-no-advocate.md`, both feeding **build-19**, the one Arc-3 build that
  fully discharged. (`091002` archived earlier, at the 2026-07-12 pass.)
- **Under the widened rule — archive by FILING when the filing's own content is wholly discharged and
  the build's remaining tails belong to *other* filings:**
  - `…-090500-upgrade-rulings-never-reach-the-decision-log.md` — build-21 **A3-15** discharged in full
    2026-07-18 (write path + F8 migration, the headline discharge of that pass). Build-21's open tail
    is **A3-14**, a different filing.
  - `…-100000-loop-profile-drift-predates-build-11.md` — build-22 **F4** discharged 2026-07-18, both
    named pre-fix partners relocated, exact subject match, idempotent. Build-22's open tails are
    **F1/F2**, different subjects.
  - `…-091005-write-verification-attestation.md` — build-16 **M4** discharged 2026-07-17 (two measured
    lint cycles, the second catching a real attestation bypass). Build-16's open tail is **091004's**
    boundary half.

**Why the rule was widened.** The standing rule's unit is the **build**, and after this arc's batch
disposition no build "passed acceptance" in the original sense — builds 15/16/18/21/22/23 closed on
**rulings** (released watches, filed findings), and *released is not passed*. Under a strict reading
every filing would sit in the active inbox indefinitely, which makes **the inbox lie about what is
outstanding** — the same honest-surface failure this arc filed against repeatedly. The closed
roadmap remains the authoritative per-filing record either way, so archiving costs no provenance.

**Bound on the widening, so it does not become "archive anything that looks done":** a filing may
archive by filing only when (a) every clause traceable to *that filing* is discharged with a dated
evidence line, and (b) the build's residue is attributable to a *different* filing. A filing whose
own clause is a released watch, a dated watch, a filed finding, or an inherited debt **stays** — which
is why `091001`, `091004`, `091006`, the four graduation-queue filings, the sayari filing, the
extraction-grant filing and the `vlt-mint` Step-4 filing all remain active.

### Filings awaiting `inbox-capture` at close

**No count is recorded here on purpose.** The active `inbox/` is the live list; this section
enumerating it would drift the moment the next filing lands — the failure this arc filed against
three times. `inbox-capture` must glob `inbox/` and trust no prior run's count, which is the standing
lesson from capture runs 2 and 3 (predicted nine, captured eleven; predicted five, captured six).

What is worth recording is the **mechanism**, because a third instance surfaced during this closeout:
an acceptance or closeout pass counts the filings **it** produced, and a filing produced by ordinary
vault use — or by an unrelated build's out-of-scope note — has no one to count it. This pass
initially wrote "four" and the real number was larger; `…-171500-brief-restatement-drift.md` is
referenced only as an out-of-scope note in A4-2's brief, `…-183003-upgrade-preserve-set-misses-vault-grown-op-skills.md`
is referenced nowhere at all, and `…-193000-report-slot-with-no-check.md` materially shaped three
Arc-4 builds without ever entering an arc's `derives_from:`. **Un-captured and un-referenced are
different states, and neither is visible from a roadmap** — only from the directory.

This closeout added three filings of its own (the build-15, build-16 and build-23 findings named in
the *Closeout dispositions* block above).

---

## Status & next step

> **⛔ This arc is archived — do not append.** Closed 2026-07-26. From the CLOSED stamp forward this
> document is read-only history; the carry-forwards above are its only live surface, and they are
> re-listed by the next arc's `inbox-capture`, never edited here.

- **Capture complete 2026-07-06** — all six filings grounded against module source
  (v0.5.0, commit `6f21952`) in six parallel verification passes. Zero SUPERSEDED
  verdicts; the batch is entirely greenfield. Provenance corrections recorded: A3-3's
  contract-grammar change is a tighten-and-relabel (the strict grammar already exists at
  `vault-operating-contract.md:115-119`; the real edit is making the partner paren
  mandatory); A3-6's overlay-blind sweep narrows to vlt-ingest + vlt-extract
  (vlt-research is a non-consumer today). Grounding additions: A3-1's lint follow-on
  needs a ruling on `_agent/dispatch.md`'s missing logical path name; A3-2 gains live
  root-scope cruft evidence (`./.DS_Store`, `./docs/.DS_Store`) and a confirmed-in-sync
  `skills[]` list.
- **This doc** = Arc 3's durable capture + grouping cache; the capture narrative above is
  this run's decision log (all-six scope confirmed by owner; no filings deferred).
- **Ideation complete 2026-07-06** (owner-steered via `bmad-module-builder`): grouping
  accepted as proposed plus a build-18 durability cluster; all cross-filing and 091002
  rulings recorded in the *Ideation rulings* section above. 0.6.0 = builds 14+15+16+18;
  build-17 trails.
- **Briefs written 2026-07-06:** `build-14-packaging-lint.md`,
  `build-15-spec-convention.md`, `build-16-frontmatter3-bell-attestation-freshness.md` —
  each with its acceptance checks appended to the ledger above. The Bases date-filter
  spike CLOSED (see Ideation rulings), so build-16 is ungated.
- **Builds 14 → 15 → 16 BUILT + committed** on `arc3-v0.6.0` (one commit per build; head
  `1142fb4`). **build-18 brief written 2026-07-08** — `skills/reports/build-18-durability-cluster.md`,
  grounded against post-16 source (one grounding correction: build-16 made vlt-research a
  frontmatter@3 consumer, so it is now overlay-blind and joins the F3 fix — the roadmap's
  A3-6-LB1 "non-consumer" note is superseded). Its acceptance checks are appended to the
  ledger above; the 0.6.0 version bump + pre-tag lint gate live in the brief's Release section.
- **v0.6.0 SHIPPED 2026-07-08.** build-18 committed (`2b79e89`), release commit (`a117f4f`)
  bumped both version strings, pre-tag `package-lint --expect-version 0.6.0` → A/B/C/D PASS
  (line recorded in the release commit). ff-merged to `main`, tagged `v0.6.0`, pushed to
  origin. 0.6.0 = builds 14+15+16+18.
- **Live acceptance ran** — vlt-core 0.6.0 upgrade 2026-07-08 17:45; discharged in two passes
  (`acceptance-discharge` 2026-07-12 and 2026-07-17). The 07-17 pass rode **no new upgrade**:
  nine days of ordinary vault activity — a `new partner` mint, two lint cycles, three classifier
  runs — turned out to be the evidence. A second vault, **vlt-sayari** (0.4.0→0.6.0 two-version
  jump, 2026-07-09), contributes via filing rather than direct read, and discharges machinery
  vlt-core structurally cannot exercise (overlays, families, retrofit scan).
- **The Arc 3 acceptance story in one line:** the enforcement arc shipped its bells, and the
  field's verdict is that **the bells work and mostly haven't rung** — which is the arc's own
  thesis turned back on it. Two of the three enforcement mechanisms (spec convention, boundary
  classifier) have never fired in anger; one (attestation) has, and caught a real bypass within
  five days. The distinction the ledger now draws, and that `arc-closeout` must respect, is
  between **a tail waiting on a clock** (091006 — will fire on its own, 2026-08-17) and
  **a tail waiting on an event nothing can cause** (build-15 — blocked, needs a build).
- **Next: capture, then arc-closeout — in that order.** `arc-closeout` is **blocked**, not
  merely early. Its gate is build-15's consumer-lock tail, which cannot discharge until the
  spec-advocacy gap is captured and fixed (`inbox/2026-07-13-092341`, which names itself
  blocking). Run `inbox-capture` first: **nine uncaptured filings** are in `inbox/` (07-11 →
  07-17), including three from the Chess Coach mint's own fallout and the two adoption-gap
  filings that likely share one answer (see below).
- **The pattern worth capturing as one thing:** two filings five days apart describe the same
  shape — *a well-specified location whose adoption nothing measures*. Specs (class-count zero,
  `inbox/2026-07-13-092341`) and loop profiles (two of three verticals never migrated,
  `inbox/2026-07-17-100000`). frontmatter@3's enforcement declaration has a **violation** facet
  and no **adoption** facet, so both read clean while unused. If that generalizes, it is
  build-17's most valuable slice — and it is exactly the "declared conventions need teeth" remit
  build-17 already owns.
- **The build-17 brief** (enforcement kit) waits on its vault-side slice evidence (091003 M0
  counters — unpayable until it ships, a circularity the brief should resolve rather than
  inherit), and has now **grown a second owner-ruled input**: the spec-advocacy gap.
- Filings stay in `inbox/` until their build ships **and** passes acceptance, then archive.
  **Nothing archived on the 07-17 pass** — 091001/091004/091005/091006 all still have open tails
  on their builds, and 091003's build is unbuilt. `091002` remains the only Arc 3 filing archived.

### ✅ CAPTURE RUN 2 COMPLETE — 2026-07-17 (supersedes the two bullets above where they conflict)

- **Eleven filings captured** (A3-7..A3-17), grounded against v0.6.0 @ `a117f4f` in eight
  parallel verification passes (the four graduation-queue filings graded as one cluster).
  Owner confirmed all eleven in scope; **none deferred**. The count in the *Next: capture*
  bullet above said "nine" — the real total was **eleven** (it omitted
  `2026-07-16-153000-new-partner-fields-one-lens`, the only filing with zero prior roadmap
  cross-references, and `2026-07-17-100000`, whose watch item was discharged while the
  defect itself was never captured). **Nothing archived this run** — no new build has
  shipped, so no filing has met the ships-and-passes bar.
- **⛔ The *Next* bullet's premise above is REFUTED.** It says arc-closeout is blocked
  because build-15's tail "cannot discharge until the spec-advocacy gap is captured and
  fixed." **Grounding refuted the gap's central claim** — `vlt-upgrade:75` (build-15's own
  F6) originates specs, and this doc discharges that path at `:644-651`. **Capture has now
  run, and the answer is that the block may never have existed.** The residual is cadence,
  not existence. **`arc-closeout` should NOT inherit the blocked status — the owner must
  re-rule first.** See A3-12.
- **⚠ The *pattern worth capturing as one thing* bullet above is CONFIRMED and enlarged.**
  Both instances hold, and grounding found the class is worse than "adoption isn't
  measured": **acceptance can be discharged against a non-adopting population.** Build-11's
  check #1 named the two partners that drifted and was discharged against wearers minted
  after the drift (A3-17). That is a soundness gap **in the deferred acceptance ledger
  itself**, and it plausibly explains build-15's dry tail identically. **This reaches
  further than build-17's remit** — see open question 28.
- **⚠ The bullet's build-17 routing is questionable.** It calls the adoption facet
  "build-17's most valuable slice." Grounding disagrees: build-17 derives metrics from
  **event records**; an adoption metric measures an **absence** — no event to count. It is a
  `frontmatter.md` schema change (build-16's lineage), not enforcement plumbing. **Re-ideate
  ownership rather than inheriting it.** Same for the "second owner-ruled input" bullet: the
  spec-advocacy residual is (a) cadence, (b) a schema facet, (c) a `consumers:`
  registration — only (a) plausibly wants a tripwire, and hanging build-15's close on
  evidence-blocked build-17 **trades one blocked tail for a longer one**.
- **✅ ALL THREE GATES RULED 2026-07-17** (see *Owner rulings — capture run 2 follow-up*):
  gate 1 — arc NOT blocked, build-15 tail reverts to STILL-OPEN (first-exercise,
  non-vacuous per gate 2); gate 2 — no vacuous discharge; gate 3 — A3-14 = **under**
  (naming gate live, name `vlt-track` in base, `extraction@2→3`). Ideation for
  A3-7..A3-17 is now ungated.
- **This doc remains its own decision log.** Every judgment call this run made — scope,
  grading, what was consumed-vs-live, what grounding overturned — is in the capture
  narrative above, at the point it is relevant. No separate artifact.
- **NOT ideated. No build assignments were made this run.** The *Proposed grouping* and
  *Ideation rulings* sections above cover the original six filings only and are **stale with
  respect to A3-7..A3-17**. Capture's output is a grounded roadmap, not a build plan.
- **Next: owner-steered ideation** (likely `bmad-module-builder`), with three rulings
  needed before anything else: **(1)** is the arc still blocked, given A3-12's refutation?
  **(2)** does an acceptance check naming specific live artifacts get to be discharged by
  substitutes (open question 28) — this governs how every remaining tail is read; **(3)**
  A3-14's §6, now that its *replace* reading lost its support and the evidence points at
  *under*. **Independent of all three:** `vlt-research/SKILL.md:65` scalar → list is a
  one-word fix, correct on its own terms, and unblocks the whole graduation-queue cluster's
  substrate. It needs no ruling.

### Status-line restructure — 2026-07-17 (lifecycle-audit Item 5, owner ruled option (b))

- The frontmatter `status:` line had grown to ~4,700 chars of accumulated discharge
  history — the arc's own state-in-prose disease in the factory's state store. Owner
  ruling (lifecycle-skills-audit Item 5): **cap `status:` to ~3 sentences; history lives
  in the ledger.** Before the cut, every claim in the old line was verified already homed
  per-item in the **Deferred acceptance ledger** annotations (discharge notes, the
  build-15 reclassification + its refutation warning, STILL-OPEN tails) or in this
  section's dated bullets — nothing was destroyed, only deduplicated. Standing shape from
  here: `status:` says open/closed, what shipped, where acceptance stands in one clause,
  and what's next; per-item history is appended to the ledger bullet it belongs to.

### ✅ CAPTURE RUN 3 COMPLETE — 2026-07-25

- **Six filings captured** (A3-18..A3-23), grounded against **v0.7.0 @ `dbcf018`** (working
  tree clean). Owner confirmed **all six** in scope; **none deferred**. **Nothing archived** —
  no new build has shipped since v0.7.0, so no filing has met the ships-and-passes bar.
- **The predicted count was wrong again, in the same way.** Acceptance-discharge pass 6 wrote
  "five filings now await it" and named the five 07-25 filings. The real total was **six**:
  `inbox/2026-07-18-115913-chess-coach-persona-line-seeds-fabricated-time.md` had **zero**
  references anywhere in this doc, in either prior run. Capture run 2 recorded the identical
  miss (predicted nine, captured eleven). The mechanism is the same both times: an acceptance
  pass counts the filings **it** produced, and a filing produced by ordinary vault use has no
  one to count it. Discovery must keep globbing `inbox/`, never trusting a prior run's count.
- **Two filings had a central claim overturned by grounding** — the third run in a row with a
  non-zero overturn rate, which the doc has already named as evidence in its own right:
  - **A3-18 — PROVENANCE CORRECTION, class-level.** The "Najdorf/Tuesday" persona line the
    filing calls *shipped prose that re-seeds on every install* exists in **no module file**
    (`grep -rn "Najdorf" skills .claude-plugin tools README.md` → exit 1). It lives only in
    vlt-core's **locally-minted** `vlt-agent-chess-coach` and that mint's own brainstorm
    record. Per the standing rule, vault-local mint prose is not module source. Residual
    module scope shrinks from "fix shipped prose" to one open question about the mint's
    persona-authoring beat — and the module's three shipped personas were verified clean of
    concrete temporal idiom (weekday/relative-time grep → exit 1).
  - **A3-20 — corrected, and the fix got cheaper.** The filing states Step 4 is
    near-duplicates-only and contradictions are "never eligible." `vlt-lint/SKILL.md:105`
    already reads "(and any other maintenance worth doing later)". The gap is **routing, not
    eligibility**: `:69`/`:101` never point contradictions at Step 4, and `:108`/`:111` are
    merge-shaped. Its shape-2 fix is a second item template plus two pointers, using the
    existing `maintenance` kind (`vault-operating-contract.md:234`) with no new vocabulary.
- **Three grounding discoveries none of the filings made** (each recorded in its capture
  subsection with citations):
  1. **`adoption_first_instance:` is un-adopted.** Build-20's adoption facet is declared at
     `frontmatter.md:237`/`:242` and carried by **zero of the seven shipped conventions** —
     including `spec.md`, the exact case `:242` names as its motivating example, and one of
     only two conventions still at `enforcement_stage: declared`. The arc's own remedy for
     shipped-but-unexercised is shipped and unexercised. This reframes A3-19's shape 2 from
     "apply an existing facet" to "wire the facet for the first time."
  2. **The two research-note write paths disagree.** `vlt-research/SKILL.md:71` carries the
     `revisit_after:` slot; `vlt-ingest/SKILL.md:77-91` (Step 5) **omits it entirely**. Ingest
     is the majority write path on a vault consuming external sources, so a partner on that
     path never sees the key and cannot decline it — a mechanical explanation for A3-19's
     0-of-96 that beats "partners never elect it," and a scope widening for its shape 1.
  3. **`linkage_ripe`'s third union component has no shipped writer.** `vlt-ingest` Step 6
     never writes a wiki→research `[[wikilink]]`; `vlt-lint:41`/`:59` only *tolerate* such
     links. The union is effectively two-component, and both survivors are graduation
     residue — a stronger root cause than filed. It also undercuts A3-23's cheapest suggested
     fix: wiki `sources:` holds the **external** source, not the note path, so "derive
     graduated-ness" has no reliable substrate and needs its own grounding pass.
- **A3-21 is the run's provenance benchmark.** It cites a vault-grown capability and an
  improvised wiki-index rule and marks both **explicitly unshipped**, using them as evidence
  that a careful local author still missed the failure — the correct handling, and the exact
  opposite of A3-18's error, from the same vault in the same week.
- **A3-23 is the run's only filing with an Arc-3 dependency.** Build-20's FP-rate clause is
  graded **FAILED** (exercised, not waiting), so build-20 closes on this fix. Every filing in
  the run names Arc 4 as its natural home. That contradiction is stated as the
  **⚖️ arc-boundary question** above with its two coherent options; it is an ideation /
  closeout ruling and this run does **not** resolve it. It compounds with the build-19
  tick-or-carry decision the ledger already flags as pending.
- **This doc is the decision log for this run** (no separate `.decision-log.md`, per the
  skill's own contract): scope confirmation, every grade, every citation correction, and the
  three discoveries above are in the capture narrative at the point they are relevant.
- **NOT ideated. No build assignments were made this run.** The *Proposed grouping* and both
  *Ideation rulings* sections above are **stale with respect to A3-18..A3-23**. Capture's
  output is a grounded roadmap, not a build plan.
- **Status-line discipline, noted honestly:** the 2026-07-17 owner ruling caps frontmatter
  `status:` at ~3 sentences with history in the ledger. That line had already regrown well past
  the cap through six acceptance passes **before** this run; this run added one compact clause
  and put its detail here rather than compounding the regrowth. **The cap is not currently
  being met** — flagging it for `arc-closeout` rather than silently widening it further.
