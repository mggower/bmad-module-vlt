# Brief Anatomy

The shape every `build-N-<slug>.md` follows. Author the brief with these sections, in this
order. The two best current exemplars are **`build-18-durability-cluster.md`** (frontmatter,
F-sites, dispositions, the deviation-recording `status:`) and **`build-15-spec-convention.md`**
(brief-time dispositions resolving a filing's open questions against the rulings) — both in
`factory/cycles/00-origins/briefs/` — read them for the level of specificity expected and
match their rigor, not their length. A thin build gets a thin, honest brief; don't pad. A
closed cycle's briefs stay in that cycle's own `briefs/` directory.

Filename: `factory/cycles/<open cycle>/briefs/build-N-<slug>.md`, slug a short kebab theme
(e.g. `durability-cluster`, `spec-convention`).

## 1. Frontmatter

```yaml
title: 'Build #N — <theme> (<one clause on the why-now>)'
status: 'BRIEFED <date> — build via bmad-workflow-builder in a fresh session'
module_code: 'vlt'
created: '<date>'
derives_from:
  - 'factory/inbox/<filing>.md (A<cycle>-<i> <the specific latent-bug IDs it contributes>)'
  # one entry per filing this build folds in; name the LB/change IDs, not just the file
roadmap: 'factory/cycles/<NN-slug>/roadmap.md'
rulings: 'roadmap §Ideation rulings (<date>): <the one-line rulings this build cites>'
risk: '<low | low-moderate | moderate> — <one clause on why, and whether it bumps a convention
  version / triggers a consumer walk>'
```

- **`title`** is **public prose**: it is collected verbatim into the module's `CHANGELOG.md`
  entry for the release this build ships in, so it carries no personal names, no vault names,
  and no vault-local artifact paths (CLAUDE.md, "Git & publishing" — the same scrub every
  shipped surface passes).
- **`status`** starts `BRIEFED <date>`. The builder later rewrites it to a **BUILT record**:
  `BUILT <date> — <what landed>; <verification result>. Deviations/notes: (1) …` with
  **numbered deliberate deviations** from the brief. Describe this in the brief so the builder
  knows the target shape (the precedent is `build-15-spec-convention.md`'s `status:` — a BUILT
  line followed by numbered `(1)…(2)…` deviations). This skill writes only the BRIEFED line;
  updating it to BUILT is the builder's job (checked by `vlt-release` pre-flight, not here).
- **`derives_from`** names filings **and the specific latent-bug / change IDs** each
  contributes (e.g. `091006 LB1 overlay-aware reads + LB2 overlay-subsumption`), so the brief's
  scope is traceable to the capture that justified it.
- **`rulings`** is a pointer + one-line paraphrase of the Ideation rulings this build stands
  on — never a re-derivation of them.

## 2. Intent

A few sentences under the `# Build #N — <theme>` heading: what the build changes and why now.
State the goal, the cluster of latent bugs / changes it closes (cite the roadmap section they
came from), and — load-bearing — a line settling that **rejected alternatives in the parent
filings are not re-litigated** ("All rejected alternatives in the parent filings are settled —
do not re-litigate"). The builder should never re-open a design the capture or ideation closed.

## 3. Brief-time dispositions

Each open question the roadmap **left to brief time** gets an explicit ruling here, each citing
the ideation-rulings line (or the filing question) it derives from. This is where the brief
does its own decision-making — bounded to the questions ideation deliberately deferred, never
the ones ideation already ruled. Number them (`1.`, `2.`, …); the exemplars
(`build-15` §"Brief-time dispositions", `build-18` §"Brief-time dispositions") show the form:
a bolded ruling, then the reasoning that grounds it in the deferred question. In headless mode,
any judgment call made without the owner is recorded here as its disposition.

**Interim posture (R1) — required whenever the build ships a rule, check, or finding class
ahead of its mechanism.** A numbered disposition in this section states what a vault (or the
factory) legally does in the window before the mechanism exists — the rule declared in Arc 7
("a rule with no home is a wish; a rule whose mechanism can't ship this arc states its interim
posture or is withdrawn"). A brief that ships nothing ahead of its mechanism states `R1: not
applicable` in one line. *(Section landed 2026-08-17 at the Arc 8 roundtable — R1's declared
home from Arc 7, written here for the first time; R4 landed the same day in §7.)*

**Retirement clause — required whenever the build ships enforcement.** *(Platform P-15,
2026-08-25.)* A numbered disposition names the prohibition this build's check, net, or gate
makes redundant — with its `file:line` — and either retires it in this build or records why it
survives (a population the mechanism does not cover; a retirement ruled for a later build).
A build that ships no enforcement states `Retirement: not applicable` in one line.

This is R1 read backwards. R1 catches a **rule ahead of its mechanism**; this catches a
**mechanism that arrives beside the rule it obsoletes** instead of in place of it — which is
how eleven cycles retired zero rules while adding many, and how one root cause returned as a
symptom five times. The moment a net ships is the only moment anyone is looking at both halves
at once, so the question is asked here rather than left for a future filing to rediscover as
friction. Where the answer is a retirement this build does not make, the disposition names the
build or files a `supersession` note (`factory/inbox/README.md`) — never a silent survival.

## 4. F-sites

One `## F<n> — <what it touches>` section per file or feature the build changes. Each states:

- **Current state** with exact `file:line` (freshly re-grounded — see
  `grounding-at-brief-time.md`; the sites the capture cited are re-verified, not trusted).
- **The exact change** — precise enough that the builder edits without re-deciding scope
  (the exemplars quote the current text and the replacement, cite the sibling site the change
  mirrors, and call out single-home / handshake implications).
- **Why** — the latent bug or ruling it discharges.

Where a site moved since capture, the F-site carries the **grounding correction** inline (see
`grounding-at-brief-time.md`), and a superseding note is written into the roadmap. F-sites also
carry per-site **out-of-scope** notes where a nearby change is deliberately not made.

## 5. Registration

Always present, even when empty. States what the build registers in the module's help/version
surface: a new skill's `module-help.csv` row (canonical 13-col header — see CLAUDE.md), a new
workflow, or — the common case — **`None.`** with the one-line reason (a convention edit
registers nothing; no version bump ⇒ no consumer walk / re-ack). If a convention **rule** did
change, this is where the consumer walk (re-ack every listed consumer, same build) is named.

**A new shipped skill is not shipped until it is registered.** *(Arc 9 roundtable, 2026-08-20.)*
A build that creates `skills/vlt-<name>/` owes **both** halves in that same build:
`.claude-plugin/marketplace.json` `plugins[0].skills[]` **and** a quoted 13-field
`module-help.csv` row. Only the first is caught by lint — package-lint **C5** fails the release
on a `skills/vlt-*` dir absent from `skills[]` — while **the CSV row is caught by nothing**:
`check_group_b` validates the header, field count and quoting and never checks that every shipped
skill has a row. *A skill nobody's help surface lists is a mechanism vaults cannot find, and lint
exits 0.* Name both, and list both as ship-verifiable acceptance checks.

**"No bump owed" is not "no cost."** *(Arc 9 roundtable, 2026-08-20.)* The handshake is one gate
among several, and the others block the tag just as hard. When Registration says `None.`, the
brief still prices whichever of these the edit touches:
- **package-lint C6** — editing `governance/_meta/vault-operating-contract.md` requires
  **re-deriving `_meta/vault-rule-card.md`** and re-stamping its `derived_from: … sha256:`, and
  any act-blocking clause must fit inside `RULE_CARD_BUDGET`. The contract is deliberately not
  handshaked; it is **not** free.
- **package-lint E4** — `_e4_harness_coverage` introspects the check inventory by callable name,
  so **any new `package-lint` check owes a declaring case in `tools/test-package-lint.py` in the
  same build**, or the release gate blocks.
- **package-lint E5** — asset nodes (e.g. `vlt-lint-full.js`) ack via a `// depends_on:` header,
  a **different edit surface** from a skill's frontmatter. A consumer walk that counts only
  skills undercounts the work.

## 6. Out of scope (dispositioned)

Adjacent things deliberately not touched, each with a one-line disposition:
deferred-to-build-X / rejected-because / already-covered-by. This is what keeps a later reader
(or a field filing) from re-raising something the brief already considered and set aside.

## 7. Verification (unit, at rest — lifecycle step 5)

The checks the builder runs **at rest**, before any live use: greps for cross-file agreement,
script dry-runs against temp fixtures, end-to-end against real external code where possible.
Plus the standing per-build rituals when they apply:

- **Handshake bipartite re-check** — if any convention `version:` moved, or any `consumers:` list
  or the structure map changed, verify every consumer listed ↔ every ack current (CLAUDE.md
  version-handshake rule). **The check of record is `package-lint` Group E**
  (`tools/package-lint.py` — E1 handshake-bipartite, E2 structure-map SSoT, E3 stray-pin). Name
  Group E in this section as the check; do not compose your own.
  <br>**A hand-written `grep "<name>@" skills/` is not a substitute, and must not be written as
  one.** It is **self-confirming** — it greps for the token you just wrote, in the files you just
  edited, so it cannot fail on the drift Group E exists to catch (a `consumers:` list naming a skill
  that never acked; an ack pointing at a convention that moved). Group E derives both sides from the
  authoritative surfaces and compares them. A grep is fine as an *aid while editing*; it is never
  the recorded verification. (Build-23 shipped Group E to retire this ritual and the ritual survived
  it — because this instruction used to name no tool at all. See
  `factory/cycles/05-kept-promises/filings/2026-07-26-141500-group-e-did-not-retire-the-handwritten-handshake-grep.md`.)
- **Packaging lint** — the mid-cycle `package-lint.py` **A/B/C/E** run (D / `--expect-version` is the
  release gate, not per-build). At the release build, this section names the
  `--expect-version X.Y.Z` gate and the version bump (both strings).
- **Fixture extension (R2)** — any build that adds or changes a release-gate check extends
  `tools/test-package-lint.py` in the same build (a covering case + `CASE_FLOOR` bump);
  `package-lint` Group E4 fails an uncovered check, so skipping this is visible at the gate, not
  optional.
- **Legal response (R3)** — any build that adds or changes a finding class states that class's
  one-line legal response at the check's own single home (the file where the check lives —
  `checks.md` for lint, `ledger.md` for dispatch pointer integrity, and so on), **in the same
  build**. A wire is the ruled exception: its response homes in `surface_text` semantics
  (`tripwires.yaml`, header). A build that touches no finding class states `R3: not applicable`
  in one line.
- **Enumeration widening (R4)** — any build that adds a file to a class an existing vital or
  manifest enumerates (e.g. always-loaded partner files, accumulating agent-zone records, skill
  assets — the list is illustrative; the class test is the enumeration itself, or one the
  build's own walk establishes) widens that enumeration **in the same build**. A brief may
  instead **declare** the new file outside the enumerated class with the reasoning recorded — a
  declared exclusion, never a silent omission (files retired to cold storage under the Arc 8
  safety model are outside live-read enumerations by design: vitals measure wake-read mass, not
  vault mass). A build that adds no such file states `R4: not applicable` in one line.
  *(Ruled at Arc 8 ideation, cross-filing ruling 2; landed here 2026-08-17 at the roundtable.)*
- **Scrub** — no personal / vault-local content in any changed shipped file (CLAUDE.md
  publishing rules; worked examples use placeholder paths).

## 8. Release (release build only)

Present only when this build is the last in its version. Names the two version-string bumps
(`.claude-plugin/marketplace.json` and `vlt-setup/assets/module.yaml`), the pre-tag
`uv run tools/package-lint.py --expect-version X.Y.Z` gate (tag only on exit 0, PASS line in
the commit message), and the ff-merge → tag → push sequence. Non-release builds omit this
section and say so in `status:`/Verification (the version bump rides the release build).

## 9. Acceptance (live — appended to the roadmap ledger)

The checks that ride the next vault upgrade — behavioral, field-side, days-to-first-check where
it applies. **These same checks are appended to the roadmap's Deferred acceptance ledger in the
same run** (the Exit gate in SKILL.md). Write them once here in prose; the ledger bullet
carries the same content. This is the section the Exit gate reads to build its ledger append —
if it's empty or vague, the ledger append will be too.

### Build the instrument from the failure's shape, not the fix's

*(Platform P-18 Tier A, 2026-09-01; cause `ST-5`.)* Before writing a check that needs a corpus or
a set, look at what the filings behind this build actually preserved: their **specimen manifests**
(shape single-homed at `factory/inbox/README.md`) and any set the capture entry recovered. Build
the check against those specimens. Where they must be frozen to be usable, materialize them into
this cycle's `fixtures/` and cite the filing they came from.

**A fixture authored from the fix's shape passes because it was built to.** That is not a
hypothetical: Cycle 12's findings cache was proven on a two-run temp fixture that stubbed the one
seam which breaks in the field, shipped green, and has never once worked. Where no specimens
survived, say so in the check rather than quietly synthesizing a stand-in — the Exit gate's
`specimens:` figure will show the shortfall anyway, and a named gap is reviewable where a
confident fixture is not.

### Every check carries a tag: ship-verifiable or field-contingent

**Required, at brief time, per check.** This is the single most load-bearing thing this section
does, and it exists because Arc 3 could not close for eighteen days without it.

- **`[ship-verifiable]`** — dischargeable at rest, at the release gate, or on the next ordinary
  upgrade. **Bounded**: an event that is going to happen anyway will settle it. Examples: a
  handshake is bipartite-consistent; a migration leaves a stub; a seeded file is present; a lint
  reports zero coherence findings.
- **`[field-contingent]`** — needs a field event **of a specific kind** to occur before it can be
  graded at all. **Unbounded**: nothing in the build, the release, or the upgrade causes it.
  Examples: a boundary-creating mint; a roster-changing mint; a spec authored and version-bumped;
  a vault-local asset edit; a maintainer citing a limit correctly.

**A ship-verifiable check names its at-rest *instrument* at tag time.** *(Cycle 11
roundtable R1, 2026-08-24.)* The B9-1 standard — "the instrument is factory-side and
runnable at rest, or the tag is not true" — applies when the tag is written, not when
closeout tries to grade it. Name the fixture, harness, or reader protocol (an agent-run
check is legal, but it is *named as the instrument*, with what it is given and what the
recorded evidence is). Three of Cycle 11's ruled checks carried the tag with no instrument
behind it and had to be repaired at review; a tag that cannot name its instrument is the
same wish as a field check that cannot name its event.

### The adversary question (required, per ship-verifiable check)

*(Platform P-20, 2026-08-27.)* Beside the instrument declaration above, every ship-verifiable
check answers one question, and **the answer is recorded in this section**:

> **Name the property this check exists to protect. Now construct a state where the check
> PASSES and the property is VIOLATED.**

If such a state exists and is reachable on the shipped surface, the check is incomplete —
**widen it, or add a second check**, before the brief is complete. If no such state can be
constructed, write that down: *"property: …; no passing-violating state found."* A check that
survived the question must be visibly distinct from one that was never asked, so **a silent
pass is not an answer** — the same standard the obsolescence beat already holds
(`roadmap-roundtable`).

**Why this sits here and not in a review stage.** A check inherits the blind spot of the fix it
was written beside: the same reasoning designs the repair and its acceptance check, in one
sitting, from one framing. A briefer who has just ruled *"define the class in one place"* writes
a check verifying one definition exists — the property they meant to protect, *every site that
names it agrees*, is never tested because it was never stated **separately from the fix**. A
second reviewer inherits that framing and does not cure it; only restating the property on its
own terms does. Ask the question of your own check, at the moment you write it.

**Worked positive — Cycle 14 build-3 check (4).** Property: *the Layer-3 operational-record class
has one consistent definition.* Passing-but-violated state: *a second site names the class with
different members.* Every clause of the check held and the property was violated at
`extraction.md:84` vs `:190`; the contradiction shipped in v0.17.0 and was hot-fixed as v0.17.1
the same day. The question would have found it at brief time in minutes.

**Worked negatives — the question must not flag everything.** Cycle 14 build-1 check (2) was
graded on six real subjects with its instrument proven failable against the prior release's code;
build-2 check (1) runs three times precisely because two runs cannot observe reused-half loss.
Both were adversarially constructed already and answer the question cleanly. A pass that flags
every check is noise, not an instrument.

**Where the roadmap already names the property**, the answer here must **reconcile with it** —
the roundtable's instrument beat records properties at plan time, before any check exists (see
`.claude/skills/roadmap-roundtable/SKILL.md`). A brief that protects a different property than
the plan named states which is right and why; silently substituting one is the defect this
question exists to catch, one stage later.

**Field-contingent checks are out of scope for the question** — not because they are exempt from
rigor, but because the intervention is scoped to the checks that gate. A field-contingent check
that fires and fails is still a defect (Cycle 14 build-5 (6) is the recorded instance).

**A field-contingent check names its discharging *event*, not only its vault.** *(Arc 9
roundtable, 2026-08-20.)* "Discharges in the field" is not a bound — a debt whose discharge
requires an event **nothing in the plan schedules** is the shape that produced the four-arc
A4-4 (5) debt and ruling 4c's two-arc miss. Write the event as something someone could put in a
calendar ("a successful `vlt-feedback` run from the work machine's app-vault"), name who performs
it, and bind it. A check that cannot name its event is a wish; say so at brief time rather than
discovering it at closeout.

**A field-contingent check must also name which vault can produce its event, at brief time.** Four
of Arc 3's nine stuck tails needed a vault the factory machine cannot read, and **none of them said
so until discharge time** — by which point the check had already been re-annotated across four
passes as though it were merely slow. If the answer is "a vault we cannot read," write that down;
if the answer is "a vault that has no reason to do this," the check is probably measuring the wrong
thing and should be reconsidered now rather than at closeout.

**Why the tag matters:** `cycle-closeout` gates **only on ship-verifiable checks**. Field-contingent
checks go to the standing watch register that outlives cycles by design (see
`.claude/skills/cycle-closeout/references/closeout-checklist.md`, Stages 1 and 2). Untagged, the two
kinds sit under one checkbox, closeout gates on both, and the cycle acquires no bound — which is
exactly what happened to Arc 3.

**Do not use the tag to dodge rigor.** A check is field-contingent because of *what it measures*,
never because it looks inconvenient. Tagging a ship-verifiable check field-contingent to get it out
of the gate is the vacuous-discharge failure wearing a new hat — the gate-2 ruling (no vacuous
discharge; a discharging instance must be one that could have failed) governs both kinds equally.
