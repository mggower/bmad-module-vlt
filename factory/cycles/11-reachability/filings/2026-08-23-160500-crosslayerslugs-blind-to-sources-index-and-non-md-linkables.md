# The missing-target check cannot be trusted until `crossLayerSlugs` reaches `sources/`, `{index}`, and non-`.md` linkables

_Filed 2026-08-23. Evidence: the first post-0.14.0 full-mode `vlt-lint` sweep on
vlt-core (`{lint_reports}/2026-08-23-1504-lint.yaml`, persisted; vault read-only
throughout). Classification: **defect** — a check whose entire output was false this
run. Provenance: the B10-2(5)/B10-12(6) re-discharge event (DA9's triple-duty run);
this run graded **B10-2(5) FAILED (narrowly)** and sized the residual seam DA9 named._

## The defect

The sweep itself executed end-to-end (145/146 pages, loud coverage caps — the B10-12
repair is field-proven). But the workflow returned **12 missing targets and all 12
were verified false positives** — every flagged target exists on disk. The report
renders `missing_targets: []` only because the executor verified each by hand and
recorded the cause in `coverage_caps`: "MISSING-TARGET CHECK IS BROKEN THIS RUN, not
the wiki."

Three causes, all in the `crossLayerSlugs` derivation (`vlt-lint-full.js`, the
qualifying-key predicate over resolved `vault_structure` keys):

1. **`{index}` is invisible** (3 hits — `[[index]]`): `resources/wiki/index.md` is
   excluded from the page population by construction and is never added to the
   cross-layer set, so every wikilink to the index reads as missing.
2. **`sources/` is unreachable** (8 hits): `sources/` is not a `vault_structure` key,
   so the qualifying-key predicate cannot admit it — yet vault pages legally link
   source deposits (`sources/fantasy/…`, `sources/articles/…`).
3. **Non-`.md` linkables are outside the glob** (1 hit — `[[_agent/bases/wiki.base]]`):
   the derivation only collects `*.md`, so a legal link to a `.base` file reads as
   missing.

## Why this is a persisting class, not a new one

Causes 1 and 3 are **the pre-B10-2 class surviving that fix**: the 2026-08-16 full
lint (0.12.0) reported the same `[[index]]` ×3 and `.base` false flags. B10-2's
derivation-from-`vault_structure`-keys repaired the `handoffs`/`areas` causes
(confirmed gone this run) but never covered the index or non-`.md` files, and
`sources/` emerged as a new cause because it is a real vault zone that has no
structure-map key at all. B10-2(5)'s fail wording — "any class persists or returns
under a new name" — fired on exactly this.

## What acceptance needs

Re-discharge of B10-2(5)/B10-12(6)'s missing-target leg = a full sweep whose
missing-target flags survive verification (or a measured zero) after the predicate
gains the three populations. Design questions for capture, not answered here:
whether `sources/` should become a `vault_structure` key (the B10-10 minting route
exists now), whether `{index}` joins the cross-layer set or the page population, and
whether the linkable set widens past `*.md` (`.base` today; the general class is
"non-markdown files the vault legally links").
