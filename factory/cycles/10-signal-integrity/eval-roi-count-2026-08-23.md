# Eval-suite ROI count — would an at-rest suite have caught it?

_Run 2026-08-23 from the factory, at rest, against the full filing corpus.
Derived from the brainstorm at
`_output/brainstorming/brainstorm-vlt-eval-harness-2026-08-23/` (memlog + keepsake are
the design record). This is analysis, not a build — it exists to decide whether the
eval work is worth filing at all._

## Method

**Population:** all 98 inbox filings — 41 in `inbox/archive/`, 57 active. Every filing is
by definition a *found-late* event: signal that reached the factory only after a release,
which is exactly the cost an at-rest suite exists to avoid.

**Why not the `Classification:` line.** Filings carry an italic `Classification:` header,
but the convention only starts ~2026-07-26 and its formatting is not uniform — 84 of 98
yield nothing to a bulk extract. It cannot carry the analysis. Classification below is by
filing **title plus header claim**, which in this corpus state the defect mechanism
explicitly.

**Verification.** Three highest-stakes classifications were read in full rather than
trusted from title: #27, #33, #95. All three confirmed; #95 confirmed *stronger* (the
filing itself prescribes a package-lint check as the fix). Remaining rows are
title-and-header evidence, not full reads — stated so the confidence level is visible.

**Tiers** (from the brainstorm's synthesis):

| tier | what it is | when it runs | judge |
|---|---|---|---|
| **T1 structure** | packaging, manifests, schemas, byte budgets, exit codes, file presence | every commit | script |
| **T2 contract** | cross-file agreement: two or more sites must say the same thing | every commit | script |
| **T3 behaviour** | needs a model run against a fixture vault to observe | per build | model + council |
| **U untestable** | no at-rest check can reach it | — | — |

**Counting rule applied throughout:** if nothing in shipped source was factually *wrong*,
no eval can catch it. A missing capability is not a defect.

## Result

| tier | count | share of 98 |
|---|---|---|
| T1 — structure | **9** | 9% |
| T2 — contract | **26** | 27% |
| T3 — behaviour | **19** | 19% |
| U — untestable at rest | **44** | 45% |

- **Eval-catchable: 54 of 98 (55%)**
- **Deterministic, gate-able at commit with no model: 35 of 98 (36%)** — 65% of everything catchable
- Model-and-fixture tier: 19 of 98 (19%)

### The meaningful denominator

44 of the 98 are untestable, but most are not defects — they are features, candidates,
calibration data, and field notes. Excluding those leaves **11 genuine defects that no
eval can reach** (rows 24, 25, 56, 68, 70, 71, 73, 74, 76, 91, 92 below).

Against the actual defect population of **65**:

- **Catchable: 54 of 65 — 83%**
- **Deterministic at commit: 35 of 65 — 54%**

## The residue has a shape, and it is not "field-contingent"

All 11 uncatchable defects share one form: **they name an absence.** "no legal home,"
"no fallback," "no form for," "no promotion ladder," "no durable registration," "no
dependency record," "no drain," "needs a second axis," "cannot be measured by anyone."

An eval asserts that what exists is correct. It cannot assert that something absent
should exist.

That is a cleaner boundary than ship-verifiable / field-contingent, and it carries a
consequence: **absence-defects are not found by running a live vault either.** They are
found by reasoning about the model — which is what ideation and the roundtable are for,
and two of the eleven (70, 71) were in fact surfaced by the review council, not by
execution.

So live-vault acceptance was never the mechanism catching this class. Demoting it from
gate to sampler costs less than the brainstorm assumed.

Corroborating: two of the three fully-verified cases (**#27**, **#33**) are
**factory-origin** filings — found at rest in this repo, never in a vault. They are 100%
eval-catchable and 0% acceptance-catchable.

## What to actually build: nine named checks cover 28 of the 35 deterministic cases

The deterministic tier is not 35 bespoke cases. It is nine recurring classes.

| # | check | instances | rows |
|---|---|---|---|
| 1 | **Site A promises what site B does not do** | 5 | 28, 51, 52, 63, 75 |
| 2 | **False-positive rate on real data** *(T3, fixtures)* | 6 | 26, 57, 58, 80, 86, 96 |
| 3 | **Silent partial failure renders as success** | 4 | 39, 85, 95, 98 |
| 4 | **Declared field has no producer** | 3 | 23, 53, 88 |
| 5 | **List claiming completeness has drifted** | 3 | 67, 82, 89 |
| 6 | **Stale self-referential claim** | 3 | 35, 51, 69 |
| 7 | **Rule contradicts its own worked example** | 2 | 38, 87 |
| 8 | **Byte / size budget breached** | 2 | 62, 95 |
| 9 | **Personal or vault-local content on shipped surface** | 2 | 97, + the 091001 path leak |

Class 5 is already named in CLAUDE.md as a standing failure mode ("lists that claim
completeness drift"). Class 9 is already a standing rule. Neither is mechanically
enforced today.

**Citation resolution is not in the table because it is a class of one — and it is the
strongest single case in the corpus.** Row 27: a brief restated a field calibration with
its polarity inverted, and the inversion survived *a brief, a build, unit-verification at
rest, a release lint, a tagged release, six acceptance passes, and a graded acceptance
clause* — caught only when a spike re-read the source filing 14 days later. The filing's
own words: **"No step in the loop re-reads a filing to check what a brief said about it,
so the inversion was never checkable in principle."**

A checker that resolves every `file:line` citation in every brief and roadmap entry and
asserts the quoted text is really there closes that hole. It is ~40 lines and it defends
the discipline CLAUDE.md names twice.

## Verdict

**Clears comfortably.** 83% of real defects are reachable at rest; 54% need no model at
all. The deterministic half is ~9 checks, not 35, and two of those classes are already
written down as standing rules that nothing enforces.

Recommended split, per the platform ledger's boundary rule (*platform iff `vlt-upgrade`
does not deliver it*):

- **Platform (`tools/`, off-cadence, no version bump):** the nine checks + citation
  resolution + `fixtures/vaults/`. Extends `package-lint.py`; adds no skill, respecting
  the channel's spent skill budget.
- **Arc roadmap (shipped surface, later, only if warranted):** `vlt-upgrade` pre-apply
  integrity refusal; the `repro:` field on the field-defect issue template.

**Sequencing note:** citation resolution is independent of fixtures and tiers, is the
single highest value-per-line item, and has the corpus's most damning instance behind it.
It should go first and can go alone.

---

## Audit trail — all 98 rows

Ordered as `inbox/archive/*` (1–41) then `inbox/*` (42–98), matching filing date order
within each. `T` = tier.

| # | T | filing | basis |
|---|---|---|---|
| 01 | U | vlt-setup friction notes | install friction notes, no stated defect |
| 02 | U | librarian first breath | field notes |
| 03 | U | vlt-lint-full issues & optimizations | optimization bundle |
| 04 | U | wiki category/topic model | convention change proposal |
| 05 | U | vlt-mint phases + planning doc | feature |
| 06 | U | personalized extraction | feature |
| 07 | T1 | council args not threaded | workflow invocation contract; assert parse-on-intake |
| 08 | U | upgrade ownership + vlt-upgrade skill | feature |
| 09 | U | dispatch routes sources to Librarian | feature/refactor |
| 10 | U | dispatch → communication bus | feature |
| 11 | U | 0.2.0→0.3.0 field notes | notes |
| 12 | U | light capability first instantiation | pattern/feature |
| 13 | U | heavy-source prep/interpret split | feature |
| 14 | T1 | installer interop: module.yaml + CSV header | path locatability + canonical header |
| 15 | U | pre-tag packaging lint | this is the proposal for package-lint itself |
| 16 | U | write-verification attestation | feature |
| 17 | U | dev/ zone graduation | explicitly a candidate |
| 18 | T2 | spec convention has no advocate | reachability: shipped convention referenced by ≥1 flow site |
| 19 | T3 | repeal ruling never reaches decision log | needs an upgrade run to produce the ruling |
| 20 | T2 | loop profiles inline, no migration shipped | old-location instances present after a relocating build |
| 21 | T3 | chess-coach prose seeds fabricated time | shipped content induces bad output; needs a run |
| 22 | U | synchronous consult channel | explicitly a candidate |
| 23 | T2 | revisit_after has no adoption path | declared field has no producer |
| 24 | U | contradiction model needs a second axis | modelling insight; names an absence |
| 25 | U | auto-caption name substitution | external data pathology, module source correct |
| 26 | T3 | linkage_ripe 41/41 false | false-positive rate; needs fixture + run |
| 27 | T2 | brief restated calibration, polarity flipped | **citation resolution** — verified in full |
| 28 | T2 | preserve set misses vault-grown op skill | mint Step 4 promises what upgrade Step 1 omits |
| 29 | T2 | retired ritual still written by hand | grep for the retired form |
| 30 | U | nothing measures session cost | names an absence (the cost instrument) |
| 31 | U | B5-1 work-vault numbers | calibration data |
| 32 | U | eight releases, no changelog | missing practice |
| 33 | T1 | package-lint fixture stale, harness red 3 builds | **verified in full**; assert harness green + fixture covers all groups |
| 34 | T2 | merge-config strips vault_structure | golden diff: config in, config out, no key loss |
| 35 | T1 | stock review_after dates expire | shipped dates in the past |
| 36 | T2 | lint-full blind to convention overlays | skill declares overlays govern; script does not read them |
| 37 | U | wiki sources should be wikilinks | classified candidate |
| 38 | T2 | ingest template teaches wrong sources shape | template contradicts the rule |
| 39 | T3 | pathless relay pointer, guard silently inert | inert-guard behaviour; needs a run |
| 40 | T2 | knowledge-gap rail has no recipient | declared route has no consumer |
| 41 | T2 | proto-deliver era names no datum; handoff ref slips rule | rule vs instance |
| 42 | U | spec convention home | feature |
| 43 | U | enforcement kit derive-first | feature |
| 44 | U | no boundary without a bell | doctrine |
| 45 | U | review_after freshness key | frontmatter@3 proposal |
| 46 | U | graduation queue | frontmatter@4 proposal |
| 47 | U | graduation queue calibration | calibration data |
| 48 | U | graduation queue 2nd calibration | calibration data |
| 49 | U | sayari 0.4.0→0.6.0 exercised untested half | field evidence; argues for fixtures |
| 50 | T2 | new-partner mint gets thinnest panel | panel size vs gate stakes |
| 51 | T2 | extraction grant authorizes nobody | stale text vs current model; day-zero resolvable |
| 52 | T2 | mint tells local mints to write shipped manifest | shipped instruction violates durability rule |
| 53 | T2 | sources_vs_prose slot no check fills | declared field has no producer |
| 54 | T2 | lint outside the decision-log loop | op roster vs decision-log consumer list |
| 55 | U | spec advocate exists, adoption still zero | adoption metric, needs real usage |
| 56 | U | boundary bell never rung, metric unmeasurable | filing states it is unmeasurable |
| 57 | T3 | lint-full asks LLMs for exact facts; 87% false | false-positive rate; needs fixture runs |
| 58 | T3 | spec_candidate revision signal detects a template | false-positive; needs runs |
| 59 | T3 | activation reads full contract, ~10K tokens | cost budget dimension |
| 60 | T3 | handoffs re-pay the full boot | cost budget dimension |
| 61 | T3 | beat 2 orient unbounded, scales with vault age | cost budget on an aged fixture |
| 62 | T1 | three whale files 41K/38K/38K | byte budget on shipped files |
| 63 | T2 | adoption_first_instance unreachable off-mint | producer/reachability |
| 64 | T3 | entity-collision coverage pair-incomplete | needs fixture with known collisions |
| 65 | T3 | sayari upgrade omitted adoption line | never-omit rule failed on 2nd execution; needs a run |
| 66 | T3 | lint report block never persisted | run once, assert artifact |
| 67 | T1 | manifest scope lost references/ + scripts/ | manifest completeness vs on-disk assets |
| 68 | U | dispatch hardcodes single-user addressee | classified design gap; names an absence |
| 69 | T2 | spec.md blind-spot statement stale | self-referential claim vs current state |
| 70 | U | no legal home for vault-originated convention | names an absence |
| 71 | U | mint mandates council with no fallback path | names an absence |
| 72 | U | append-only files have no decay contract | names an absence |
| 73 | U | handoff has no inline-payload form | names an absence |
| 74 | U | partner memory has no promotion ladder | names an absence |
| 75 | T2 | activation ritual omits {overlays} | ritual omits what other sites assume |
| 76 | U | vault-grown consumer has no durable registration | names an absence |
| 77 | U | feedback loop single-machine | feature |
| 78 | T2 | tripwire metrics in module-overwritten file | vault-local state in module-owned path |
| 79 | T3 | PARA guard produces falsified provenance | behavioural; needs a run |
| 80 | T3 | relay count fires same 6 false positives | false-positive + repeatability |
| 81 | T2 | scanner prompts ignore frontmatter rule 4 | embedded prompt vs convention text |
| 82 | T2 | crossLayerSlugs omits three roots | hardcoded list vs vault_structure map |
| 83 | T3 | upgrade post-flight report never persisted | run + assert artifact |
| 84 | U | reports YAML-in-markdown | open question |
| 85 | T1 | manifest hashed from live files | net silently disabled; assert hashes match stock |
| 86 | T3 | Gap B asked unconditionally, 88% misfire | false-positive rate |
| 87 | T2 | wiki-index rule forbids its own example | rule vs worked example |
| 88 | T2 | high_value_gaps declared, no producer | declared field has no producer |
| 89 | T2 | decision-log writer roster admits no discovery site | roster completeness vs actual write ops |
| 90 | U | no kind: value for scoped deviation | names an absence |
| 91 | U | captured issues accept unread comments | names an absence |
| 92 | U | capabilities install tools with no dependency record | names an absence |
| 93 | T3 | Step-4 report omits mandatory divergence line | declared-vs-produced; needs the run |
| 94 | T2 | rail-triage residue: form alignment, voice single-homing | cross-file agreement + single-home |
| 95 | T1 | lint-full non-executable; total failure reads clean | **verified in full**; filing prescribes a package-lint budget check |
| 96 | T3 | relay leg fires on ordinary round trips | false positive |
| 97 | T1 | amendment trigger is a personal handle | personal content on shipped surface |
| 98 | T3 | council fan-out has no partial-shortfall signal | silent partial failure; needs a run |
