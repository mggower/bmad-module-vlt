# Defect: `revisit_after:` has no adoption path — and its detector reads non-adoption as clean

_Filed 2026-07-25 by the acceptance auditor during the Arc 3 discharge run (pass 5, "fresh-note
pass"), from grounding done against **`vlt-core`** while trying to discharge build-20's `revisit_due`
acceptance check. Owner-ruled to file rather than hold as a watch. This is a **defect/design gap**
(the same silent-zero shape the enforcement arc exists to close), not a candidate._

## The finding, measured

**Zero of 96 `vlt-core` research notes carry `revisit_after:`** — including **all four written after
the key shipped**:

- `_agent/research/2026-07-19-110053-chess-improvement-crosscheck-two-claims.md`
- `_agent/research/2026-07-19-110510-black-opening-approach-sub-1000-ideas-not-lines.md`
- `_agent/research/2026-07-25-131035-secure-offsite-backup-for-a-git-managed-vault.md`
- `_agent/research/2026-07-25-131352-afc-west-preview-kimes-winks.md`

All four carry the *other* build-20 deliverable correctly (`topic:` as a YAML list — that half is
discharged). All four declined `revisit_after:`. For contrast, the wiki zone has 2 pages carrying
`review_after:`, so the sibling key **is** in live use; only the research-zone key is dark.

## Grounding notes (factory-side, checked 2026-07-25 against v0.7.0 source)

- `skills/vlt-research/SKILL.md:71` — `revisit_after: YYYY-MM-DD  # OPTIONAL — graduation-candidacy
  recheck date; absence = not a candidate`. It sits in the write template as a commented optional
  slot. **Nothing prompts it, no beat asks the question, no gate notices its absence.**
- `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:138` — "**Absence = not a
  candidate** (the note is not offered for graduation): only a note the writing partner judged
  graduation-relevant carries it, set at write time." The semantics are deliberate and correct; the
  problem is that nothing ever causes the judgment to be made.
- `skills/vlt-lint/SKILL.md:83` — `revisit_due` surfaces a note whose `revisit_after:` is past, and
  "**Absence of `revisit_after:` = not a candidate = zero findings** — legacy research notes generate
  no noise (backfill is a non-event by construction)."

The absence-clause is right for *legacy* notes. The defect is that it is indistinguishable from
total non-adoption by *new* notes: **a vault where no partner ever sets the key produces a
permanently clean `revisit_due` report**, and that clean report is indistinguishable from "the
graduation queue is healthy."

## Why this is the arc's own scar, again

This is structurally identical to the failure `inbox/2026-07-13-092341-spec-convention-has-no-advocate.md`
named for the spec convention, and which build-19 shipped a fix for:

> `spec.md` declares `deferral_metric: "spec version bumps shipping without their relay entries"` at
> threshold 1 — in a vault with zero specs that metric **reads clean forever**, measuring adoption
> failure as success.

Same shape, different key: an optional declaration + a detector whose absence-branch is silence
= adoption failure rendered as health. Build-20 opened `frontmatter@4` partly to add the
`adoption_first_instance:` **enforcement facet** for exactly this class — this filing is evidence
that `revisit_after:` is a key that facet should have covered and does not.

## The acceptance consequence (why this got filed instead of waited out)

Build-20's ledger check includes "*`revisit_after` behaves:* a research note with a past
`revisit_after` is surfaced (`revisit_due`), never auto-resolved or nagged." That positive case
**cannot be discharged by any `vlt-lint` run, full or scoped** — there is no note to surface. Four
post-fix notes ran the exact write flow and none produced a subject, which is a *pass-through*, not
a wait. Per the discharge rubric's pass-through tripwire, re-annotating it as an ordinary
first-exercise tail is forbidden; it needed either a BLOCKED grade or a filing. Filed.

The absence-branch half of the check (legacy notes generate no noise) is unaffected and discharges
on the next full lint.

## Candidate shapes (for the capture to weigh — not rulings)

1. **Make the write beat ask.** `vlt-research`'s write step decides `revisit_after:` explicitly —
   set a date, or record that the note is not graduation-relevant. Turns an ignorable slot into a
   two-outcome question. Cheapest fix; no new machinery.
2. **Give the key an adoption facet.** Apply build-20's `adoption_first_instance:` enforcement facet
   to `revisit_after:` so a zone with zero instances is *visible as un-adopted* rather than clean —
   the general fix, and it likely generalizes to every optional key the module ships.
3. **A zero-adoption surface in `vlt-lint`.** Distinguish "no candidates" from "no note has ever
   carried the key" in the `revisit_due` report line. One sentence of honesty in the reporting, not
   a new check; mirrors the `vlt-lint:74` honest-limit precedent from build-23.

Shape 1 and shape 2 are not exclusive — 1 fixes this key, 2 fixes the class.

## Honest limits of this filing

- **Measured on one vault.** `vlt-core` only; `vlt-sayari` is on the work machine and unreadable
  from here. Its research-zone adoption is unknown and would strengthen or weaken the "nobody sets
  it" claim.
- **The mechanism is not broken.** `revisit_due` behaves exactly as specified; `linkage_ripe` is the
  *other*, union-based candidacy path and is unaffected by this. This is an adoption/visibility
  defect, not a logic defect — no vault is producing wrong output today.
- **Four notes is a small sample** for "partners never elect it," though it is 4/4 plus 92/92 legacy.

## Provenance

- Vault: `vlt-core` (0.7.0, factory machine), research zone at 96 notes.
- Surfaced by: Arc 3 acceptance-discharge pass 5, 2026-07-25 — see the build-20 item in
  `skills/reports/inbox-evolution-arc3-roadmap.md` for the ledger-side record and the owner ruling.
- Natural home: **Arc 4**, alongside the adoption-facet work Arc 3 opened but did not finish.
