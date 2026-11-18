# The findings cache cannot survive the release that makes it needed

_Filed 2026-09-01 from **`{field-vault}`**, on an owner cost objection during Cycle 14's build-6
briefing: *"I can't keep running full lints to verify these patches, it is way too expensive."*
Grounded against shipped source at v0.17.1 and against the measured cost of the 2026-08-30 sweep.
Evidence is `{field-vault}`, read-only._

⚠ **This filing refutes a premise currently on record.** Platform item **[P-19]**'s Out of scope
says: *"**Sweep cost.** Cycle 14 build-2's cache repair is the answer to that … 146/146 cold is the
broken cache, not the vault's size."* **The cache repair is not the answer, and 146/146 cold after a
release is not the breakage — it is the design.** P-19 is being amended in the same act; this filing
is the module half.

## The claim

The findings cache exists so a sweep can reuse page-scan facts instead of re-dispatching an agent per
page. Its reuse key is a **ruleset fingerprint** whose composition is single-homed at
`skills/vlt-lint/references/full-scale.md`, step 2 — **four named slots**:

> `module_version` (the installed one); `pin_vector` (this skill's own `depends_on:` pins, verbatim);
> `convention_digests`, a `{name: digest}` map with one entry per convention this run judges against;
> and `checks_digest` … **Any of those moving invalidates every record.**

The first slot is `module_version`. **Every release moves it.** So every release invalidates every
record, whatever the release contained. The document states the consequence itself, as settled fact:

> **the first full run after any release is a COLD one**

**The cache therefore reduces the cost of routine re-sweeps and cannot reduce the cost of
post-release verification — which is the only sweep an acceptance check ever forces.** The instrument
built to make sweeps affordable is invalidated, by construction, at precisely the moment a sweep
becomes mandatory.

## The measured cost of one cold sweep

From `{lint_reports}/2026-08-30-1123-lint.yaml`, `cost_accounting:` — the run's own numbers:

| phase | agents dispatched | model | prompt chars |
|---|---|---|---|
| Scan pages | **146** | haiku | 591,152 |
| Index pass | 1 | sonnet | 3,876 |
| Cluster pass | 25 | sonnet | 42,305 |
| **total** | **172** | | **637,333** |

`files_checked: 146`, `files_cached: 0`. And `prompt_chars` is the floor, not the cost: the report
notes it is *"workflow-composed prompt text only — agent-side file reads (page + convention bytes)
are not visible from JS."* Each of the 146 scanners also reads its page **and three conventions**.

Cycle 14 shipped **three releases** and has a fourth briefed. Under the current design that is four
mandatory cold sweeps, and the wiki grows monotonically.

## Why the slot is over-broad — the argument, gradeable

`module_version` is a **proxy** for *"something that changes what a finding means may have moved."*
The other three slots answer that question directly and with precision: `pin_vector` catches a
convention pin moving, `convention_digests` catches convention **content** moving, `checks_digest`
catches the check catalogue moving. Independently, the workflow-side `scanFingerprint`
(`vlt-lint-full.js:232-233`) catches the page-scan prompt and the `PAGE_SCAN` schema moving.

What does `module_version` uniquely catch that those four do not? Changes to the lint surface's own
logic that move no pin and no digest — `vlt-lint/SKILL.md`, `references/full-scale.md`, the reduce in
`vlt-lint-full.js`. **That is a real gap and the slot is not pointless.** But it is answerable by
**digesting those files**, which is what every other slot already does, rather than by a version
number that also fires for every release that touches none of them.

**Worked instance, available now.** Build-6 (briefed 2026-09-01) bumps **only** `extraction.md`
9 → 10. The page scanner does not read `extraction` — `pageScanPrompt` reads exactly
`frontmatter`, `wiki-supersession`, and `write-verification` (`vlt-lint-full.js:228`). A cached
**page-scan record** cannot be changed by an `extraction` edit. Yet v0.17.2 will invalidate all 146
of them, twice over: once via `module_version`, and once via `convention_digests`, which carries *"one
entry per convention **this run** judges against"* — extraction among them, because the run's `para_*`
checks judge against it even though the cached artifact does not.

**That second over-broadening is the deeper one.** The cache stores **page-scan facts**. Its key
should be scoped to what a page-scan fact depends on — the page-scan prompt, the `PAGE_SCAN` schema,
and the three conventions the scanner actually reads. It is currently keyed to everything the *whole
run* consults, so a change to a check the cached records never fed invalidates them all.

## Candidate directions (not a fix — capture's call)

1. **Key the cache to the cached artifact's own dependencies.** Page-scan records are invalidated by
   the page-scan surface (prompt + schema + the three conventions the scanner reads) and by nothing
   else. `checks_digest` and the non-scanner conventions move what the **reduce** concludes, not what
   a scanner **returned** — and the reduce re-runs every sweep regardless. This is the direction with
   the largest effect and it needs the *"what does a cached record actually depend on"* question
   answered explicitly, which no site answers today.
2. **Replace `module_version` with digests of the lint surface it proxies for** (`vlt-lint/SKILL.md`,
   `references/full-scale.md`, `vlt-lint-full.js`). Keeps the guarantee, drops the false positives.
   Smaller and independently shippable; correct even if (1) is declined.
3. **Do nothing to the key; make the release-time sweep unnecessary instead** by binding checks to the
   population they actually judge. ⚠ **This is free today and is already being applied** — see the
   companion finding below. It reduces how often a cold sweep is forced but does not make one cheaper.

⚠ **Not a direction: weakening invalidation on judgment.** A record reused under a moved rule is a
false clean, which is worse than an expensive sweep. Any repair must show the reused facts are
**independent** of what moved, not merely unlikely to be affected. `full-scale.md` already states the
honest posture for the degraded case — *"a missing, unparseable or schema-mismatched sidecar is a cold
run, stated in the report — never an error and never a silent full sweep presented as a cached one."*
The same standard applies to any narrowing: it must be stated in the report, never inferred.

## Companion finding, recorded here because it shares the cause

**Three of Cycle 14's acceptance checks were bound to a full sweep whose population they do not
judge.** `checks.md:19` places the `para_*` closing nets in **both modes**, and `vlt-lint/SKILL.md:41`
defines *"every PARA file"* as *"the PARA members of the scoped set in scoped mode."* The 146-agent
fan-out scans `{wiki}`; the `para_*` slots are filled by the SKILL from its own PARA jurisdiction scan
(`vlt-lint-full.js:812-814`).

| check | population | was bound to | needed |
|---|---|---|---|
| build-3 (7) | `para_missing_attestation` | first full sweep after release 2 | a scoped run |
| build-5 (5) | `para_missing_attestation` | one `vlt-lint --full` under 0.17.1 | a scoped run |
| build-6 (4)(5) | `para_type_unknown` | first full sweep after v0.17.2 | a scoped run |

Build-6's two were **corrected at brief time on 2026-09-01**; the other two are historical and are
annotated, not re-graded. **This is a brief-time discipline gap, not a module defect** — no shipped
behaviour is wrong — and it belongs to `build-brief`'s check anatomy, cousin to the corpus declaration
[P-19] is adding. It is recorded in this filing so the two halves of the cost problem are legible
together: **how often a cold sweep is forced** (this half, factory-side, free to fix) and **what a
cold sweep costs when it is** (the filing above, module-side).

_Ship-verifiable at rest: a repair to the fingerprint's composition is gradeable against a fixture —
two runs with a deliberately-moved slot, asserting which records survive — with no field event. The
field half (a real release that keeps the cache warm) rides the first release after the repair._
