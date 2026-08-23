# The 0.13.0 upgrade's Step-4 report omits the mandatory `manifest_write_divergence:` line

_Filed 2026-08-21 by the factory acceptance auditor (acceptance-discharge run over the
vlt-core 0.12.0 → 0.13.0 upgrade), classification: **defect / report-contract violation**.
**Provenance:** the A1 hand-saved Step-4 report
(`skills/reports/2026-08-21-vlt-core-upgrade-0.13.0-step4-report.md`, saved verbatim per
its provenance header) and the vlt-core upgrade-ledger entry `[2026-08-21 16:23]`.
Surfaced grading B10-1 acceptance check (5)._

## The defect, precisely (grounded 2026-08-21 against v0.13.0 @ `a3ec505`)

B10-1 added `manifest_write_divergence:` to the Step-4 report schema with an explicit
never-omitted contract — `vlt-upgrade/SKILL.md:106`: "the Step-3.6 write's
diverged/sanctioned output — **never omitted when empty**". The first live upgrade under
the fixed net (vlt-core 0.12.0 → 0.13.0, run from source @ `a3ec505`) produced a Step-4
report whose YAML jumps `skill_asset_divergence: []` directly to `migrations_run:` — the
`manifest_write_divergence:` line is absent, and the string appears nowhere in vlt-core.

## What is NOT broken

- **The mechanism ran and was honest.** The upgrade-ledger digest records the Step-3.6
  source-hashed write: `source_mode: source` (not live-hashed), 67 entries,
  `added/removed/diverged/sanctioned/sanction_stale` all empty. No silent absorption; the
  check's fail condition (a clean report over a tree differing from stock at an
  unsanctioned manifested path) did not occur.
- The Notes-line instruction (`vlt-upgrade/SKILL.md:138`) is when-non-empty, so its
  absence from the report is conforming.

## Why it matters

The never-omitted clause is B10-1's honesty bell: an empty line is affirmative evidence
the net ran; an absent line is indistinguishable from the pre-B10-1 blind spot the build
existed to close. The very first field exercise reproduced the omission — a report
renderer following the ledger digest shape (which has no such line) rather than the
Step-4 YAML schema, or the schema line being skippable when empty despite the comment.

## Candidate direction (for capture to grind, not a ruling)

Whatever makes the line structurally unskippable — e.g. the Step-4 emitter deriving the
YAML block from the schema rather than prose recall, or package-lint/fixture coverage
asserting the key's presence in a rendered report. B10-6 (the report-persistence build,
which retires the A1 hand-save posture) is the natural adjacent home; capture should rule.

## Acceptance linkage

B10-1 ledger item, check (5), graded **FAILED** by the 2026-08-21 acceptance-discharge
run — annotation in `inbox-evolution-arc10-roadmap.md`. A future upgrade's Step-4 report
carrying the line (empty or not) is the re-discharge evidence.
