# The lint's sources reconciliation writes the retired bare-path form

_Filed 2026-09-03 by `acceptance-discharge` (Cycle 15 pass 2) while adjudicating Cycle 14 build-1 (6)
leg 3 on the first full `vlt-lint --full` after v0.18.0 on **`{field-vault}`**
(`{lint_reports}/2026-09-03-1206-lint.yaml`). Evidence is `{field-vault}` read-only (its git history
included) plus module source. Filed **without owner confirmation** — the run was autonomous; delete if
unwanted. Kind: `defect`._

## The claim

The one `malformed_frontmatter` entry on the sweep is **genuine** — a wiki page's `sources:` carries a
vault note as a bare path with a `.md` suffix, which `frontmatter.md` rule 4 (v14) forbids for entries
written after the wikilink form shipped (2026-08-15, v0.10.0 B7-6). **The entry was written by the
module's own lint.** The 2026-08-26 full sweep's sources reconciliation ("22 reconciled") appended the
research note to the page in exactly the form the convention had retired eleven days earlier, and the
next two full sweeps (2026-09-01 ×2) did not flag it. So the write path that reconciles `sources:`
against prose emits the legacy form, and the read path that should catch it caught it only on the
third sweep after the write.

## Why it matters

- Rule 4's **coexistence posture** keeps *pre-existing* bare-path entries legal and forbids a backfill
  sweep; a page adopts the form on its next substantive edit. A writer that emits the legacy form on a
  substantive edit **re-creates the mixed state the posture was designed to let die out**, one
  reconciliation at a time, and each such entry is a real `malformed_frontmatter` finding for a human
  to repair by hand.
- The scanner's complaint arrived as *unclassified frontmatter defect* — the class Cycle 15 build-4
  recorded it **cannot refuse** (the reduce cannot refuse prose). It was correct this time; the point is
  that the writer and the checker are in the same skill and disagree about the form.

## Specimen manifest

**The set (1 of 1):** `{field-vault}/{wiki}/dutch-oven-braising.md`, frontmatter line 22, inside
`sources:`:

```
  - _agent/research/2026-05-11-193624-dutch-oven-barbacoa-chuck-roast.md
```

Written at vault commit `dbd5292` (2026-08-26, *"lint (librarian): full sweep — 146 pages, 22
reconciled …"*); no later edit to the page (`a9a0052` on 2026-08-23 is the prior touch). The
convention form shipped at module `525f077` (2026-08-15).

**The minimal triggering fragment** — the report line, `2026-09-03-1206-lint.yaml`,
`flag_for_human.malformed_frontmatter`:

```
- "dutch-oven-braising: unclassified frontmatter defect: YAML rule 1 & rule 4 violation: sources entry `_agent/research/2026-05-11-193624-dutch-oven-barbacoa-chuck-roast.md` must be double-quoted wikilink without .md: `\"[[_agent/research/2026-05-11-193624-dutch-oven-barbacoa-chuck-roast]]\"`"
```

and the rule, `frontmatter.md` rule 4: *"a wiki page's `sources:` entry that references a vault note is
a double-quoted wikilink (rule 1) carrying the full vault-relative path, no `.md` … Coexistence posture:
existing bare-path entries stay legal and there is no backfill sweep; a page adopts the form on its
next substantive edit."*

## Candidate direction (not a fix — capture's call)

Find the `sources:` writer in `vlt-lint`'s fix path (`fix-and-file.md` / `full-scale.md` step 4's
`sources_vs_prose_mismatches` application, and any reconciliation that appends a vault note to
`sources:`) and have it emit rule 4's form — the same normalization clause the checker uses, run in
reverse. Whether the 2026-08-26 sweep's other 21 reconciliations wrote the same form is a question for
capture's grounding (count only here: *22 reconciled* per the vault's commit message; the page set was
not recovered by this filing).

## Grounding

- `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:36` (rule 4) and `:108`.
- `skills/vlt-lint/references/fix-and-file.md`, `full-scale.md` step 4 — the application path.
- Cycle 15 roadmap, build-4 ledger item, check (5) pass-2 note — the adjudication this filing rests on.
- Related open sweep signal (operator, same run): `sources_vs_prose_mismatches` has been refused
  wholesale on three consecutive full sweeps and `{backlog}` carries a standing human ruling on four of
  its pages — a tier question (`fix_now` → `flag_for_human`) the owner may want captured alongside.
