# The sayari 0.8.0 upgrade appended no convention-adoption line — the never-omit rule didn't survive its second execution

_Filed 2026-07-29 from **acceptance discharge run 3** (Arc 4 ledger, A4-2 clause 7's second-vault
check, graded FAILED on its adoption-line half). Evidence is a read-only comparison of the two
field vaults' upgrade ledgers._

## The claim

`vlt-upgrade`'s post-flight `convention_adoption:` report is specified as **never omitted when
empty** ("an absent line would read as 'all adopted'"), and vlt-core's 0.8.0 entry carries it
(prose form, three-valued, all 8 conventions). **vlt-sayari's 0.8.0 entry carries no adoption
line at all** — `grep -i adoption` over its entire upgrade ledger returns zero — even though the
installed skill that specifies the line was present in the very bundle that upgrade applied.

## Grounding

- Spec: sayari's installed `.claude/skills/vlt-upgrade/SKILL.md:105-112` — the three-valued read,
  "the line is **never omitted when empty**", report-never-a-gate.
- Conforming run: vlt-core `_agent/upgrade-ledger.md:141` (`[2026-07-26 12:50] 0.7.0 → 0.8.0`) —
  **Convention adoption** line, three-valued, plus the "worth a look" spec.md observation.
- Non-conforming run: vlt-sayari `_agent/upgrade-ledger.md`, `[2026-07-27 10:19] vlt 0.6.0 → 0.8.0
  (own)` — Mints/Overlays/Bases/Skill-asset/Migrations/Governance/Capabilities/Notes all present;
  no adoption line. Everything else about the entry is thorough, which makes the omission read as
  a skipped beat, not a truncated record.

## Why it matters

This is the honest-reporting rule failing in exactly the way it predicts: on sayari the absent
line silently reads as "all adopted / nothing to report," and only a cross-vault diff caught it.
One conforming run and one non-conforming run out of two is a **reliability** problem with the
reporting beat, not a spec problem — the own-the-apply path evidently makes it easy to skim past
the post-flight report items that aren't gates. Wants whatever makes the post-flight report's
required lines hard to drop (a checklist the ledger entry template carries, or the ledger-entry
format in `vlt-upgrade` Step 5 naming the line as a required field).
