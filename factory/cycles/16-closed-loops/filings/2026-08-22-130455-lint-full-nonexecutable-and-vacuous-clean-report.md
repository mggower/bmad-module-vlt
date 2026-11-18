# `vlt-lint-full` is non-executable at 0.13.0 — and a total scan failure reports as a clean vault

_Filed 2026-08-22, relayed evidence: the vlt-core acceptance handoff at
`<vault>/_agent/acceptance/2026-08-22-vlt-0.13-lint-full-defect.md` (agent-authored,
owner-relayed; vault read-only throughout — no report persisted, no log entry).
Classification: **defect ×2, filed together — the second makes the first dangerous
rather than inconvenient**. Provenance: the first full-mode `vlt-lint` attempt on
vlt-core post-0.13.0 — the discharging event for acceptance checks B10-2(5)/B10-3(3);
this run graded **B10-2(5) FAILED**. Factory grounding 2026-08-22 against
`arc10-v0.14.0` @ `aba700c`: all mechanism claims CONFIRMED verbatim._

## Defect 1 — `PAGE_SCAN` exceeds the harness classifier limit (a B10-2 regression)

Every page-scanner agent is rejected pre-read: `blocked by safety classifier: output
schema too large to classify safely`. 145/146 agents died; the survivor was
`INDEX_SCAN` (856 chars, grounded). `PAGE_SCAN` is **4,266 chars** (grounded exactly),
up from 3,920 at B7-6 — the delta is B10-2's `sources_vs_prose` tri-state +
descriptions (`c337cfa`). The 2026-08-14/-16 full lints produced real 13.8/16.8 KB
reports, so the fan-out worked before this window.

- **Era PROVEN, not inferred (vault follow-up 2026-08-22):** the vault `{log}` shows
  the 2026-08-16 full lint ran the fan-out successfully ("144 wiki fan-out", 16.8 KB
  report) **on 0.12.0** — whose `PAGE_SCAN` was 3,920 chars — with the upgrade to
  0.13.0 landing 2026-08-21. Same workflow, same harness, same wiki: working five days
  before, non-executable after the upgrade. A harness-side limit change wouldn't have
  waited for the upgrade. This also sharpens the ceiling bound far past the naive
  856/4,266 bracket: **3,920 passes, 4,266 fails on the same harness — the limit sits
  in a ≤346-char window**. Residual question: the exact ceiling is still unmeasured,
  so a one-time trim under an unknown ceiling re-breaks on the next field added — the
  fix wants a **standing schema budget** (trim to comfortably under 3,920, and a
  package-lint check holding the line).
- **Cheap direction (unvalidated):** `PAGE_SCAN` descriptions are near-duplicates of
  `pageScanPrompt` (`:166-169`); a lean schema with residual semantics in the prompt
  scanned one page successfully in the field before the harness (fairly) blocked the
  runtime reshape as tunneling. The fix must land as a deliberate source change checked
  against the documented limit — never a runtime workaround.

## Defect 2 — zero scans render as a clean bill of health (the release blocker)

With 145/146 agents dead the workflow returned a well-formed, entirely empty report:
every `fix_now`/`flag_for_human` bucket empty, `coverage_caps: []`,
`files_checked: 0` against `files_listed: 145`. Mechanism, all grounded:

- `:195` — `scans.push(...part.filter(Boolean).filter(s => s.available !== false))`:
  `parallel()` resolves a failed agent to `null`; the filter drops it silently. Zero
  scans and zero problems are the same downstream state.
- `:186-192` — the only guard that pushes a coverage cap is the **budget** guard; agent
  *failure* has no equivalent (the overlay path already has the loud-degrade posture at
  `:180-184` to mirror).
- `:380` — `files_checked: scans.length` carried the signal; nothing asserts on it.
- **Worse (vault follow-up 2026-08-22, grounded at `:208`):** `slugSet = new
  Set(scans.map(nslug))` — the link-target existence set is built from **scanned**
  pages only, so a partial sweep doesn't just under-report: it **fabricates
  `missing_targets` for every link into an unscanned page**. (The degraded run's six
  "missing" targets from `a-j-brown` were exactly this — all six exist and resolve
  clean in the 2026-08-22 scoped lint. An earlier same-day filing recorded them as a
  `normalizeTarget`/`crossLayerSlugs` seam; **retracted by its own author** on this
  evidence and withdrawn — superseded here.) The guard below must therefore gate
  `missing_targets` specifically, not just add a coverage cap.

Candidate direction (from the field report, sound on grounding): (1) shortfall →
coverage cap naming count + reason at the reduce boundary; (2) `scans.length === 0` →
error, never a findings report; (3) consumer-side defence — `vlt-lint` SKILL refuses to
persist or advance `lint-debt` when `files_checked` is 0.

## Acceptance linkage

B10-2(5) FAILED 2026-08-22 (this evidence). Re-discharge = a full-mode sweep that
executes (Defect 1 fixed) *and* degrades loudly under any shortfall (Defect 2 fixed),
then the original B10-2(5) pass criteria. Suggested follow-up from the field, endorsed:
audit that no prior release signed off on a vacuously-empty full-lint report
(2026-08-14/-16 look genuine; the exposure window is 0.12→0.13).
