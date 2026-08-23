# The upgrade's full post-flight report is never persisted — only a digest ledger line survives the session

_Filed 2026-08-21 by the owner (via the factory clerk, owner's words in-session),
classification: **pattern / design gap**. **Provenance:** the vlt-core 0.11.0 → 0.12.0
upgrade run (vault commit `029ee39`, 2026-08-21) — the owner, reviewing the run's report,
asked why it renders in-chat only when lint reports get a documented vault home. Companion
filing: `2026-08-21-124800-report-yaml-in-markdown-legibility.md` (same hat, same run)._

## The gap, precisely (grounded 2026-08-21 against v0.12.0 @ `336d90b`)

The module already has **two report-persistence postures, and they disagree**:

- **`vlt-lint` persists the full report.** `vlt-lint/SKILL.md:72`: "**persist the report**
  (both modes): write the Step-5 report block **verbatim** to
  `{lint_reports}/YYYY-MM-DD-HHMM-lint.md` (append-only …)" — with its retention exemption
  recorded in the operating contract's Decay-contracts table. Config path exists
  (`module.yaml:61`, `lint_reports: _agent/lint-reports/`).
- **`vlt-upgrade` persists only a digest.** Step 5 appends one dated block to
  `{upgrade_ledger}` (default `_agent/upgrade-ledger.md`) — nine summary bullet lines
  (Mints preserved … Notes). The **full Step-4 post-flight report** — the parseable
  `upgrade:` block with the three divergence keys' *contents*, `vault_writable_collisions`,
  the retirement annotations, the adoption census lines, the tripwire state — renders
  in-session and is persisted **nowhere**. The ledger's Notes line names *some* report
  fields when non-empty; it is a pointer to content that no longer exists anywhere.

## Why it matters

1. **The full report is acceptance evidence.** Arc 9 made a vlt-core upgrade run at
   v0.12.0 an *obligation* of the release split (roadmap A20), and B9-2's field-contingent
   check discharges by reading exactly the Step-4 report (all three divergence keys
   rendered; each non-empty line carrying its route-to-durable-host instruction). In the
   2026-08-21 run the owner had to hand-carry the chat transcript back to the factory to
   make that dischargeable. A persisted report makes acceptance readable from disk.
2. **The lost-report failure mode already bit, hard.** Ruling 4c's three-arc slip
   (Arc 7 → 8 → 9) happened because a vault-side lint report existed ephemerally and was
   lost — and lint's verbatim-persist rule is the fix that class received. The upgrade
   report is the same class, higher stakes, still unfixed.
3. **The report carries owner rulings.** The 2026-08-21 run's report records two overlay
   retirements "by your ruling" — durable elsewhere only insofar as a migration happened to
   write a decision-log entry.

## Design notes for capture (not a proposed build)

- The cheap symmetric shape: do what lint does — write the Step-4 block verbatim to a dated
  file under a `{upgrade_reports}`-style config path (or into the ledger block itself),
  append-only, **with its Decay-contracts retention row declared in the same build**
  (Arc 8's retention-at-birth rule; an unbounded report directory is the "nowhere to put
  it" anti-pattern re-imported).
- **Scope question for capture:** a census of which verbs report-and-discard vs
  report-and-persist (lint persists; upgrade digests; groom? decay? setup?) — one contract
  or per-verb postures.
- **Durable-host doctrine applies** (Q9, shipped v0.12.0): the home must be agent-zone,
  merge-not-replace, outside the own-the-apply copy surface — `_agent/` siblings of
  `lint-reports/` and `upgrade-ledger.md` already satisfy this.
- Whether the persisted report doubles as the factory's acceptance instrument (factory
  reads the vault) or also relays via the feedback rail is an ideation question — not
  resolved here.
