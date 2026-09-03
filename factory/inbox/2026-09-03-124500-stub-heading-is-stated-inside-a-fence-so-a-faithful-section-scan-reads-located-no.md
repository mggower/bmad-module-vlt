# The stub heading is stated inside a fence, so a faithful section scan reads `located: no`

_Filed 2026-09-03 by `acceptance-discharge` (Cycle 15 pass 2) from the operator record of the first
full `vlt-lint --full` after v0.18.0 on **`{field-vault}`** (`{lint_reports}/2026-09-03-1206-lint.yaml`,
session `core-lint`). Evidence is `{field-vault}` read-only plus module source at `ad071b9`. Filed
**without owner confirmation** — the run was autonomous; delete if unwanted, `inbox-capture` grounds
it either way. Kind: `defect`._

## The claim

`checks.md`'s stub-registry procedure (Cycle 15 build-3, A15-2) says: *read the stub heading **from the
merged convention** (`{conventions}/wiki-index.md` §The Stubs section) — never from memory; locate in
`{index}` the `## ` heading whose text equals it.* But in `wiki-index.md` the heading text is
**illustrated inside a fenced ```markdown block** under `## The Stubs section`:

```
78:## The Stubs section
82:```markdown
83:## Stubs (linked, not yet written)
86:```
```

A faithful section scan — *the text of §The Stubs section, up to the next `^## ` line* — terminates
**on line 83**, the very line that carries the heading it was sent to read, and returns no heading. The
operator's first discovery run rendered exactly that:

```
section located: false, 0 slugs
```

Under the shipped procedure that is a **loud, honest-shaped false negative**: `stub_discovery: section
located: no`, a mandated coverage cap, and every registered stub reported in `missing_targets` — the
A15-2 failure re-manufactured by the instrument that was built to name it. The run was saved only
because the operator judged *0 stubs on a wiki with a populated Stubs section* implausible and
re-read the convention by eye. Nothing in the procedure asks for that judgment.

## Why it matters

- Build-3 check (2)'s fixture pair (`fixtures/build-3-index-stubs.md` / `…-bare-stubs.md`) grades the
  **index side** of the read — long-form heading present vs bare `## Stubs`. The **convention side** of
  the read (how the reader obtains the heading text) has no fixture, and that is the side that broke.
- The failure is self-consistent: `located: no` + cap + six missing targets is exactly the shape a
  vault with a bare heading would produce. A discharger comparing the report to the procedure finds
  no contradiction. Only the number's implausibility gives it away, and a small wiki with two stubs
  would not even offer that.
- Second observation, same procedure: `checks.md:13` says *collect every **backtick-wrapped** slug in
  that section's list items*; `{field-vault}`'s index lists its stubs as `[[wikilinks]]`
  (`[[barbacoa]]`, `[[mike-macdonald-defensive-system]]`, …). The operator still derived six, so the
  live procedure and the live index disagree on the slug form — capture should rule whether the
  procedure's form or the index's is the one the convention mandates.

## Specimen manifest

**The set (1 of 1):** the convention site `skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md:78-86`
at `ad071b9` — `## The Stubs section` at `:78`, the fence opening at `:82`, the heading literal
`## Stubs (linked, not yet written)` at `:83`, the fence closing at `:86`. The live index heading that
the second read matched: `{field-vault}/{index}` `## Stubs (linked, not yet written)`, six slugs
(`barbacoa`, `mike-macdonald-defensive-system`, `positionless-defense-nfl`, `los-angeles-rams`,
`myles-garrett`, `training-set-politics`; `imagenet` appears twice in the section's link text —
recorded as read, not adjudicated here).

**The minimal triggering fragment** — the first discovery run's rendered value, as reported by the
operator session:

```
section located: false, 0 slugs
```

and the correct second read, as persisted at `2026-09-03-1206-lint.yaml:6`:

```
stub_discovery: "section located: yes (heading matched: \"Stubs (linked, not yet written)\", per {conventions}/wiki-index.md The Stubs section, no overlay present); 6 slugs across 1 index"
```

## Candidate direction (not a fix — capture's call)

Either the procedure says the heading is stated **inside the fenced example** and the reader takes
the first `## ` line inside that fence, or `wiki-index.md` states the heading text **outside** a fence
(a one-line *the heading is `## Stubs (linked, not yet written)`* sentence) so a section scan finds it.
The second is a convention prose clarification (no rule change, no bump); the first is a `checks.md`
edit. Both are one line. A fixture for the convention-side read belongs with whichever lands.

## Grounding

- `skills/vlt-lint/references/checks.md:13` — the procedure (build-3 F-site).
- `skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md:78-86` — the fenced heading.
- Cycle 15 roadmap, build-3 ledger item, check (2) — the index-side fixture pair; check (5)'s pass-2
  discharge note records this near-miss.
- Study: `ST-7` (prose-specified derivations have no read-back) — this is an instance arriving
  inside the build that answered it.
