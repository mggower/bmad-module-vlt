# Attestation complaints still misroute after build-1 stripped the jurisdiction — second consecutive run

_Filed 2026-08-26. Evidence: the first post-0.16.0 full-mode `vlt-lint` sweep on
`{field-vault}` (`{lint_reports}/2026-08-25-1600-lint.yaml`, persisted; cold run, 146/146
pages, vault read-only throughout), plus the executor's own session report. Classification:
**defect — recurrence after an attempted fix**. Provenance: Cycle 12 build-1 acceptance check
(5), graded FAILED by `acceptance-discharge` on 2026-08-26._

## What was supposed to happen

Cycle 12 build-1 (`f134190`) narrowed the page scanner's jurisdiction at two sites, precisely
to kill this class:

- **F2** — `vlt-lint-full.js:144` `frontmatter_valid` lost jurisdiction over attestation
  (`per write-verification@3 Scope rule`).
- **F3** — `:153` `unmarked_supersession` lost the same.
- **F7** — `write-verification.md` §Scope gained the jurisdiction-boundary clause.

Build-1's acceptance check (5) states the field test: a page missing
`verified_by:`/`verified_at:` appears in the attestation slots **and not** in
`malformed_frontmatter`, **and not** in `unmarked_supersessions`, and the census reads
correctly **without hand-folding duplicates**.

The at-rest reader probe (brief Verification-3) **passed** all four of its pass conditions on
a purpose-built fixture — `frontmatter_valid: true` on an unattested-but-valid page, no
attestation complaint in `unmarked_supersession`.

## What actually happened

The field run reproduced the defect. From the report's own disposition block
(`2026-08-25-1600-lint.yaml:241`):

> "1 entry the fan-out returned under `unmarked_supersessions`
> (`execution-to-judgment-shift`) and 5 of the 7 `malformed_frontmatter` entries
> (`bistec-encebollado`, `k-curve-career-divergence`, `kettl`, `llm-wiki-pattern`,
> `obsidian-bases`) are attestation complaints misrouted by the page scanners, not
> supersessions or schema breaks — **folded into the attestation census, same as the
> 2026-08-24 run**."

All six were "missing `verified_by`/`verified_at`". The executor hand-folded them, exactly
as on 2026-08-24 — the hand-fold the check forbids. The census
(`146 / 97 fresh / 7 stale / 42 unattested_pre_adoption`) reads correctly **only because a
human did that fold**.

**This is the second consecutive full run reporting it identically.** The predecessor filing
is `2026-08-24-173002-page-scanner-double-reports-missing-attestation.md` (captured into
Cycle 12, built as build-1 F2/F3/F7).

## Why the fix did not take — the diagnosis this filing rests on

The magnitude fell (20 hand-folded → 6), so the narrowing did *something*. But the shape is
unchanged, and the reason looks structural rather than textual:

**F2/F3 removed the jurisdiction from two named slots; they did not give the attestation
complaint a terminal home the scanner is obliged to use.** A scanner that notices a missing
attestation pair and finds `frontmatter_valid` and `unmarked_supersession` both closed to it
will put the observation in whichever slot is still open — the prohibition is per-slot, so
it does not generalize. The 2026-08-24 filing's own stated fix direction said this and was
not built: *"make missing-attestation its own terminal class."* Build-1 built the
prohibition half and not the terminal-class half.

Corroborating signal from the same run (the executor's report, not this ledger item — filed
separately if the owner wants them captured): the scanners also **miscounted a pure
`len()` measurement twice out of two** (`kettl` summary reported 168, actually 156;
`l-theanine` 162, actually 159) and **invented a schema requirement** (`ashwagandha:
missing review_after` — `review_after:` is optional). Both suggest the page-scan prompt's
per-field discipline is weaker than its slot definitions assume, which is the same failure
mode as routing by availability.

## The fix direction

1. **Give the fact a terminal class.** A frontmatter block whose only defect is an absent
   `verified_by`/`verified_at` pair emits exactly one finding, into the attestation surface —
   stated positively in the schema, not as a set of per-slot prohibitions.
2. **Make the prohibition general, not enumerated.** "Attestation complaints never enter a
   non-attestation slot" holds for slots not yet invented; "not `frontmatter_valid`, not
   `unmarked_supersession`" does not.
3. **Grade it in the field, not only on a fixture.** The at-rest probe passed while the field
   failed — a fixture built to test the two closed slots cannot observe leakage into a third.
   If this is re-built, the acceptance instrument should be the real corpus that produced the
   six, not a constructed page.

## What this does NOT ask for

Not a re-carry of build-1's check (5) as-is. The check is discharged-or-failed on this run's
evidence and it failed; the honest route is a new build with the terminal-class fix, whose
own acceptance re-tests the class. Re-annotating (5) as STILL-OPEN would be false — the
discharging event occurred and the check did not pass.
