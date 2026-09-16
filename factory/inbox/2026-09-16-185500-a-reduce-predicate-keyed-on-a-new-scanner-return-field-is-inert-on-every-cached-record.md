# A reduce predicate keyed on a new scanner-return field is inert on every cached record — build-1's disposition 3 did not fire on its only live target

_Filed 2026-09-16 by the **field vault** (`{field-vault}`), from the first post-upgrade full sweep after
`vlt-upgrade` 0.18.0 → 0.18.1, relayed to the factory during `acceptance-discharge` pass 1 and grounded
against module source the same session. Evidence: the persisted report
`_agent/lint-reports/2026-09-16-1827-lint.yaml` and the live sidecar `_agent/lint-cache.json`. Kind:
`defect`. **This is a live-acceptance contradiction of Cycle 16 build-1 check (2) (Census), a
`[ship-verifiable]` check that GATES cycle closeout.** Companion: rail issue **#20** (`pageHashes` has no
specified digest form) — same family, and the two interact; see §Interaction._

## The claim

Build 1 shipped a reduce-side refusal (`vlt-lint-full.js`, **disposition 3**) that suppresses the
per-page `malformed_frontmatter` finding for the bare-path `sources:` form, so the form is carried once
on the denominated `bare_path_sources:` census line instead of being flagged per page. The predicate is:
the scanner's returned verdict is `unclassified` **and** `frontmatter_defect_fields == ['sources']`
**and** the page's bytes carry the form (`bareSources[slug] >= 1`).

`frontmatter_defect_fields` is a **new scanner-return field**. It is **not a term of the findings
cache's `runKey`** (`vlt-lint-full.js:427` — `${pageHashes[slug]}|${scanFingerprint}|${rulesetFingerprint}`),
and no migration evicts records written before it existed. So a record written by a **pre-build-1
scanner** carries `frontmatter_defect_fields: []`, survives the build that began depending on it, and is
reused verbatim on the next warm sweep. **On any warm cache, disposition 3 is inert for exactly the pages
it was built to refuse** — it fires only on freshly-scanned pages.

The failure is silent by construction. It passes at rest, because a fixture's scanner returns are always
fresh. In the field it produces a legal-looking report: the page simply appears in
`flag_for_human.malformed_frontmatter`, which is what the pre-build-1 behavior looked like.

## What the field actually showed (build-1 check (2), clause 2)

Check (2)'s property is *"every bare-form `sources:` entry on disk is counted exactly once on one
denominated line whose value equals an independent recount; **no per-page finding is raised for the
form**; a full sweep never increases it."*

- **Clause 1 — HELD, twice over.** `bare_path_sources: 240 entries across 83 of 152 pages`, matched
  exactly by an independent `awk` recount and again by the persist gate's own walk
  (`census {N: 240, P: 83, M: 152}`, `status ok`).
- **Clause 2 — CONTRADICTED**, on the sweep's only target page.
- **Clause 3 — not yet observable** (needs a second full sweep).

## Specimen manifest

**Set 1 — the disposition-3 target population on this sweep: 1 of 1, named.**

```
dutch-oven-braising
```

Obtained from `_agent/lint-reports/2026-09-16-1827-lint.yaml`, key `flag_for_human.malformed_frontmatter`
(a one-member list) cross-read against the same run's `coverage_caps`. Its record satisfied the byte gate
(`bareSources = 1`) and the verdict test (`unclassified`) and failed only the field test
(`frontmatter_defect_fields: []`, needed `['sources']`).

**Minimal triggering fragment** — the per-page finding that should not have been raised, verbatim:

```
- "dutch-oven-braising: unclassified frontmatter defect: YAML rule 1 & rule 4 violation: sources entry
  `_agent/research/2026-05-11-193624-dutch-oven-barbacoa-chuck-roast.md` must be double-quoted wikilink
  without .md: `\"[[_agent/research/2026-05-11-193624-dutch-oven-barbacoa-chuck-roast]]\"`"
```

**And the module stating its own blind spot** — `coverage_caps`, same report, verbatim. This is the one
genuinely good news in the filing: the cap fired, so the defect arrived loud rather than silent:

```
- "flag_for_human.malformed_frontmatter carries dutch-oven-braising, which the 0.18.1 bare-path refusal
  (disposition 3) was built to suppress: the page's bytes do carry the bare-path form (bareSources = 1)
  but its cached scanner return predates the build and carries frontmatter_defect_fields: [] rather than
  [\"sources\"], so the predicate could not fire. frontmatter_defect_fields is not a cache-key term, so
  the record survived the build that began depending on it. cache: evicted dutch-oven-braising so the
  next sweep re-derives it under the current scanner"
```

**Set 2 — every sidecar record carrying a non-empty `frontmatter_defect_fields`: 5 of 5, named,
with values.** Read from the live `_agent/lint-cache.json` (150 records) during this discharge run,
after the vault's eviction of `dutch-oven-braising` and one refused false positive:

```
acotar-world-building     missing_required  ['verified_by', 'verified_at']
costa-rican-village-dog   missing_required  ['verified_by', 'verified_at']
mat-training              missing_required  ['verified_by', 'verified_at']
obsidian-bases            missing_required  ['review_after']
yamaguchi-family-tea      missing_required  ['verified_by', 'verified_at']
```

All five are from this run's fresh scans, and **all five are `missing_required`** — dispositions 1 and
2's population. **Disposition 3's live population in the sidecar is empty.** The remaining 145 records
carry `frontmatter_defect: 'none'` with an empty field list, which is conformant and indistinguishable
from the stale-record case by inspection — that indistinguishability is the defect's cover.

**Exposure, stated honestly.** In this vault the blind-spot population is **now 0**, but only by
accident: see §Interaction. The general exposure is *every defect-bearing record written before a
scanner-return field that a reduce predicate later depends on*.

## Grounding (module source, `4fd8049` = v0.18.1)

- `vlt-lint-full.js:427` — `const runKey = (slug) => `${pageHashes[slug] || ''}|${scanFingerprint}|${rulesetFingerprint}``.
  Three terms: page bytes, scan surface, ruleset. **No term covers the shape of a scanner's return.**
- `full-scale.md` step 2 — the ruleset key is deliberately *"facts, not verdicts"*, carrying only the
  three scanner-read convention digests: *"no version string, no pin vector, no `checks.md` digest,
  because none of those is an input to any page scanner, and the reduce re-runs over the cached facts
  every sweep."* **That reasoning is sound and is exactly what breaks here:** the reduce does re-run
  every sweep, but it now re-runs over cached facts whose *schema* is older than the predicate reading
  them. The invariant the design rests on is "the reduce can always recompute from cached facts" — and
  it silently stops holding the moment the fact set grows.
- `checks.md:15` exclusion (c) and `report.md`'s *Bare-path census reporting* describe the intended
  suppression; neither can observe whether the record it is reading predates the field.

## Why it needs a build, not a doc edit

No instrument catches it. The report is legal: a suppressed-class page appearing under
`malformed_frontmatter` is precisely what v0.18.0 did, so there is no shape to diff against. The
`coverage_caps` line that caught it this time exists because the vault's session **reasoned about the
discrepancy by hand** — a fresh scanner return would not have produced it. The at-rest census harness
passes and will keep passing: its fixtures are fresh returns by construction, which is the Cycle 12
`b2(5)` lesson in a new place (a fixture built from the fix's shape passes because it was built to).

## Directions (not rulings)

1. **A schema term in the key.** Add a scanner-**return-schema** version/digest as a fourth `runKey`
   term, bumped whenever a scanner's returned field set changes. Invalidates every record on such a
   build — correct, and costly exactly once per schema change.
2. **A migration at read.** `lint-cache.py read` drops (or marks) records whose returned object lacks a
   field the current reduce depends on. Cheaper than (1); needs a declared dependency list somewhere a
   reader can see.
3. **Make the predicate fail loud instead of open.** Where the verdict is `unclassified` and the byte
   gate is satisfied but the field list is empty, treat it as *undecidable* and say so on a cap line
   rather than silently falling through to report. Strictly weaker than (1)/(2), but it converts a
   silent inert predicate into a visible one for any future instance of the shape.
4. **The general rule, wherever it lands:** a reduce-side predicate that depends on a scanner-return
   field must either be covered by a cache-key term or ship with a migration. This is a *class*, not
   one bug — worth a study-register entry (`ST-N`) rather than only a build, since rail issue **#20** is
   the same family (a term the key does not cover) discovered the same day.

## Interaction with rail issue #20 — and why this vault's exposure is currently zero

**#20's bug hid this one, and then accidentally repaired it.** Because `pageHashes` has no pinned digest
form, the first post-upgrade full sweep ran **100% cold** (0 of 144 reused, 152 fresh scans). A cold
sweep re-derives every record under the current scanner, so every defect-bearing record in this vault is
now fresh and disposition 3's blind-spot population is empty. The defect only became *observable* on the
vault's **warm re-run** under a hand-applied 16-char truncation workaround (132 of 152 cached), where
`dutch-oven-braising`'s 2026-09-03 record was reused and the predicate could not fire.

Two consequences worth stating plainly:

- **Fixing #20 makes this defect more likely, not less.** Warm sweeps are the point of the cache, and
  this predicate is inert exactly in proportion to cache reuse. The two should be sequenced together.
- **The accidental repair is not a remedy.** It rests on a bug, and it holds only until the next build
  adds a scanner-return field.
