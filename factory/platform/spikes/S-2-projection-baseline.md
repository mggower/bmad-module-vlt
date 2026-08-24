---
id: 'S-2'
slug: 'projection-baseline'
status: 'consumed'
question: 'Does the graduation absorption test still reproduce on the live research zone, and does any reliable substrate for derived graduated-ness exist at all?'
opened: '2026-07-25'
opened_by: 'ideation — Cycle 3 (A3-18..A3-23, ODQ #2); reframed the same day by SPIKE-1'
timebox: 'one read-only re-run over the live zone in both polarities'
verdict: 'proceed'
sources:
  - 'live {field-vault} read-only re-run over `_agent/research/*.md` (98) x `_agent/wiki/*.md` (131), both polarities'
  - '`_agent/sessions/2026-07-25-150500-lint.md:26`, `:52`'
  - '`_agent/artifacts/research-wiki-audit-2026-07-11.md:34-56`, `:69`'
  - '`skills/vlt-lint/SKILL.md:83` (shipped polarity)'
findings: 'factory/cycles/03-enforcement/spike2-projection-baseline-2026-07-25.md'
consumed_by:
  - 'Cycle 3 ship order (SET 2026-07-25 once both spikes closed)'
  - 'A3-23 build reshape (polarity inversion) + the A4-1 severity update'
legacy_id: 'SPIKE-2 (Arc 3 local numbering)'
---

# S-2 — the graduation projection baseline

**Back-filled into the register 2026-08-24** (platform P-2). The spike ran and closed
2026-07-25; this entry gives it a register id and a live pointer.

## The question

Reframed mid-flight by SPIKE-1, which showed the original calibration never derived
graduated-ness at all — it tested **absorption** and inverted the result. The reframed
obligations: (a) does the absorption test still reproduce on the grown zone; (b) does an
implementation read the legs the audit found load-bearing (body wikilinks, prose Sources
entries) or only frontmatter; (c) only if (a) fails, the original derive-vs-store
substrate question.

## Findings

Full enumeration: `factory/cycles/03-enforcement/spike2-projection-baseline-2026-07-25.md`.

**The absorption test reproduces.** Calibration polarity on the grown zone surfaces 8 of
98 (14% of the naive set of 59) against the audit's 13 of 90 (21% of naive) — same order,
slightly tighter. **It tracks the drain**, which is the property that matters: of the
audit's five hand-verified `orphaned_ripe` items, the four since graduated now read
absorbed and are correctly excluded; the one never drained still surfaces.

**Verdict `proceed`** — with a severity correction on the record (the 41/0 measurement
the earlier filing rested on could not be reconstructed; its substrate no longer exists).

## Register note

Cycle 3's roadmap cites this enumeration at its pre-P-8 path
(`skills/reports/spike2-…`), twice. Closed and append-only; this entry is the live
pointer — same lesson as `S-1`.
