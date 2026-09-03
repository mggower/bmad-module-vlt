# A rendered lint report is never checked against its own mandated shape

_Filed 2026-08-31 from **Cycle 14's third acceptance-discharge run**, graded against
`{field-vault}`'s `{lint_reports}/2026-08-30-1123-lint.yaml` — the first full `vlt-lint --full`
sweep taken under **0.17.1**, and the sweep three separate ledger checks were bound to. Evidence
is `{field-vault}`, read-only; nothing in the vault was edited._

## The claim

`skills/vlt-lint/references/report.md` states the persisted report's shape slot by slot: which
keys appear, what each carries, and — for several — an explicit instruction never to omit or
collapse them. **Nothing anywhere reads a rendered report back and compares it to that shape.**
Step 6 hands the shape to an agent as prose and trusts the render. The shape is a rule with no
enforcement point, which is this cycle's own through-line arriving inside the cycle's own
instrument.

The harm is not cosmetic. A ledger check that names a report key as its observable **cannot be
graded** when the render omits the key, and a check that names a per-entry population **cannot be
graded** when the render collapses that population into a summary string. One such check was
graded `BLOCKED (unreachable)` on this run for exactly that reason.

## Specimen manifest — three instances, one sweep, one root cause

Corpus: `{lint_reports}/2026-08-30-1123-lint.yaml`, 146 pages, mode `full`, module 0.17.1.
Baseline for comparison: `{lint_reports}/2026-08-27-1104-lint.yaml`, same vault, same corpus size.

**(a) `para_missing_attestation` rendered as a rollup where the shape mandates a per-file list.**
`report.md:32` specifies
`para_missing_attestation: [<para-file: vault type + author agent|hybrid, no attestation — …>, ...]`
— one entry per file. The 2026-08-30 render carries a **single string** standing in for 27 files:

> `'27 PARA files carry a vault type: + author: agent|hybrid with no attestation pair - ADJUDICATED [2026-08-26] parked-interim (ref: conventions/write-verification.md; upstream filing #16, open). Count unchanged from the 2026-08-27 sweep. Disposed, not undisposed'`

The disposition is legitimate and the count is correct. What is lost is the population: no reader,
human or check, can learn from this report **which** 27 files, what `type:` each carries, or which
are pre-adoption and therefore informational. The 2026-08-27 render does the same thing, so this is
the standing behaviour and not a one-run slip.

**(b) `fixes_applied:` omitted entirely from a report that applied fixes.** `report.md:72` mandates
`fixes_applied: [<summary>, ...]`. The 2026-08-30 render has **no `fixes_applied:` key at all** —
the top-level keys are `mode`, `scope_since`, `files_checked`, `files_cached`, `files_listed`,
`fix_now`, `flag_for_human`, `rulings_recorded`, `coverage_caps`, `false_positives_refused`,
`lint_cache`, `churn_since_last_full`, `cost_accounting`. Five fixes **were** applied that run
(five wiki pages had entries written into their prose `## Sources` sections); they are recorded
inline inside `fix_now.sources_vs_prose_mismatches` instead. The 2026-08-27 render carries
`fixes_applied:` correctly (`:221-224`), so the key was dropped between two renders of the same
skill with no code change between — which is precisely what an unchecked hand-render does.

**(c) `backlog_filed:` omitted, and the finding it should have carried filed nowhere.** The same
render has no `backlog_filed:` key (2026-08-27 has one at `:225-226`). The run found a real
instrument defect and recorded it only under `false_positives_refused` — see the companion filing
`2026-08-31-104501`. A defect worth a backlog item was surfaced and left with no route.

## ⚠ Follow-up, 2026-09-01 — what recurred and what did not

The next full sweep (`{lint_reports}/2026-09-01-1406-lint.yaml`) splits this filing's three instances,
and the split is recorded here rather than left for a reader to discover:

- **Instance (a) — the `para_missing_attestation` rollup — RECURRED, third consecutive sweep**, in the
  identical single-string form ("27 PARA files carry a vault `type:` … ADJUDICATED"). This is standing
  behaviour and the filing's core claim is unaffected.
- **Instances (b) and (c) — DID NOT RECUR.** The 2026-09-01 report carries **both** `fixes_applied:`
  (one entry, well-formed) and `backlog_filed:` (a denominated *"NONE - every filable finding this run
  already carries an open item"*, which is the honest rendering rather than an omission).

**This makes the filing's claim stronger, not weaker, and the framing should change with it.** Two
renders of the same skill over comparable runs produced **different report shapes**, with no code
change between them. An unchecked hand-render is not *consistently* wrong — it is **intermittently**
wrong, which is the harder failure for a consumer to defend against: a slot cannot be relied on to be
present, and a reader has no way to tell an absent key from a legitimately empty one without a
denominated line. **Intermittence is the symptom of no enforcement point**; a consistent deviation
would at least be a de-facto contract.

**Consequence for the directions below:** direction 1 (validate at persist) is unchanged and is the
right shape. Direction 3 (rule the rollup legal and fix the checks instead) now clearly **cannot**
explain (b) and (c) — they were not a policy, they were a miss — which is stated in that direction
already and is now confirmed by evidence.

## Why this is not three filings

All three are the same absence: **the report shape is stated in one file and enforced in none.**
A per-slot repair (add a `fixes_applied:` reminder, add a "list per file, never a rollup" note to
`:32`) would be another rule stated at the same altitude as the rules that just failed. The
question this filing asks is whether a render should be **read back and validated** before it is
persisted — and, if so, by what. The module now ships a strict-YAML-parse expectation for archived
reports (Cycle 14 build-4 check (1), filing `2026-08-27-153000`, still FAILED): a parse is already
required, and a parse is the natural place a **key-presence and slot-type check** could live. The
two filings are cousins — `153000` says a persisted report must load; this one says a report that
loads must also carry its mandated slots in their mandated form.

## Grounding against current module source (0.17.1)

- `skills/vlt-lint/references/report.md:32` — the `para_missing_attestation` list form.
- `skills/vlt-lint/references/report.md:72` — `fixes_applied: [<summary>, ...]`.
- `skills/vlt-lint/references/report.md:73` — `backlog_filed: [<merge item>, ...]`.
- `skills/vlt-setup/assets/workflows/vlt-lint-full.js:812-814` — the workflow returns
  `para_missing_attestation: []` and comments that it is *"a structural slot the SKILL fills"*.
  The workflow does not and cannot render it; the SKILL does, unchecked.
- No grep hit anywhere in `skills/` validates a rendered report against `report.md`'s slots.

## What this cost, concretely

Cycle 14's build-3 check (7) reads: *"the sweep reports the **`type:` distribution** of every
`para_missing_attestation` entry across §Scope rule's jurisdiction list."* Its bound event — the
first full sweep after release 2 — has now occurred. The sweep rendered instance (a). No shipped
surface produces a `type:` distribution, and the render did not even produce the per-file list the
shape mandates, so the check's observable cannot be obtained. It was graded **BLOCKED
(unreachable)** rather than left waiting, because waiting cannot discharge it. The check
`[ship-verifiable]` and **GATES**, so Cycle 14 gained a third gating blocker from a report-shape
defect.

Cycle 14 build-4's check (6) reads *"…is applied (**it appears in `fixes_applied:`**)…"*. It was
graded DISCHARGED on the substance — the 0% application rate is genuinely cured, 5 of 10 applied —
but with instance (b) recorded as a caveat, because the check's named location was not there to
look in.

## Candidate directions (not a fix — capture's call)

1. **Validate at persist.** Wherever Step 6 writes the dated report, parse it back and assert the
   mandated top-level keys are present and each is of its mandated type (list vs scalar vs map).
   Fail loudly. This is the enforcement point the shape has never had, and it composes with
   `2026-08-27-153000`'s parse requirement rather than duplicating it.
2. **Move the population slots off the hand-render.** `para_missing_attestation` is filled by the
   SKILL because the workflow sweeps `{wiki}` and the population is PARA-wide. If the SKILL emitted
   it from a script the way the findings cache is written, the rollup could not happen.
3. **Rule the rollup legal and fix the checks instead.** If a 27-line list is genuinely not wanted
   in a persisted report, say so at `report.md:32` and stop writing acceptance checks that read the
   population — but note that (b) and (c) are not explainable this way.

_Ship-verifiable at rest: a repair can be graded against a rendered report without any field event._
