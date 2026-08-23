# `vlt-lint-full.js` scanner prompts don't honor `frontmatter` rule 4's coexistence posture or the callout-vs-bullet distinction

_Filed 2026-08-21 from the factory on the owner's go-ahead, classification: **defect**
(module-feedback candidate). **Provenance:** lint-surfaced on vlt-core (the 2026-08-16 full
`vlt-lint` run, Arc 8 era — the owner's vault-side report, second of three strength-ordered
candidates); content recovered from Arc 7's Closeout record item 8
(`skills/reports/archive/inbox-evolution-arc7-roadmap.md:1852-1856` — the substance was never
lost, only the pointer to it); filed 2026-08-21 on the owner's go-ahead discharging ruling
4c's pre-tag bound (Arc 9 roadmap, roundtable A8, discharge route 1)._

## The claim, as recorded in Arc 7's closeout (item 8, verbatim substance)

> `vlt-lint-full.js` scanner prompts not honoring `frontmatter` rule 4's coexistence posture
> nor the callout-vs-bullet distinction

On the 2026-08-16 run, per-page scanners flagged content that the conventions declare legal:
legacy bare-path `sources:` entries (rule 4's **coexistence posture** — existing bare-path
entries stay legal, there is no backfill sweep, a page adopts the wikilink form on its next
substantive edit), and marker forms judged without the **callout-vs-bullet distinction** (a
`> [!superseded]`/`> [!stale]` callout is the convention's unit of supersession evidence; a
bullet or bare heading is not a callout and must not be credited — nor should a page be
flagged for a form the convention accepts).

## Grounding against current module source (HEAD 86efd48, v0.11.0)

The scanner prompt is `pageScanPrompt` at
`skills/vlt-setup/assets/workflows/vlt-lint-full.js:166-169`, with the per-page schema at
`:97-128`.

**Partially addressed; the defect still stands in part.**

- **Addressed:** B7-6 (`525f077`) added an explicit rule-4 instruction to the prompt for the
  Gap B (sources-vs-prose) comparison — "normalize both sides first per frontmatter.md YAML
  rule 4 — strip surrounding quotes and `[[ ]]`, strip a trailing `.md`, compare on the
  vault-relative path — so a wikilink-form entry and its bare-path twin compare equal." The
  scanners are also told to read the (overlay-merged) `frontmatter.md` itself, and current
  `frontmatter.md` (version 9, rule 4 at
  `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:36`) now states both
  the normalization clause and the coexistence posture explicitly.
- **Still standing:** the prompt never restates the **coexistence posture** itself — the
  `frontmatter_valid` schema description (":110, 'frontmatter present and well-formed per
  frontmatter.md (no key:, sources: parseable)'") leaves it to the scan model's faithful read
  of the convention whether a legal mixed/bare-path state gets flagged; and the
  **callout-vs-bullet distinction** appears nowhere in the prompt — `unmarked_supersession`
  (":119") and `name_callout_targets` (":122-125") name callouts, but nothing instructs the
  scanner that a bullet- or heading-form marker is not a callout (in either direction: not
  evidence, and not a flaggable defect where the convention accepts the form). Both remain
  convention-read-dependent rather than prompt-encoded — exactly the seam class (model
  judgment where a deterministic or explicit instruction should sit) that B5-3 fixed for slug
  normalization.
