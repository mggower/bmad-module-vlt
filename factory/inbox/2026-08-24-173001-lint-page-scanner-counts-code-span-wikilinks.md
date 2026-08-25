# The full-lint page scanner counts wikilinks inside backtick code spans — 10 of 10 missing-target flags were false this run

_Filed 2026-08-24. Evidence: the first post-0.15.0 full-mode `vlt-lint` sweep on
`{field-vault}` (`{lint_reports}/2026-08-24-1700-lint.yaml`, persisted; vault read-only
throughout). Classification: **defect** — a check class whose entire raw output was false
this run. Provenance: the E1(b)/DA9 re-discharge sweep; build-1's `crossLayerSlugs`
widening is field-proven (zero false positives of the old `sources/`/`{index}`/`.base`
class), and this is the **residual** false-positive source that replaced it._

## The defect

The per-page scan agents dispatched by `vlt-lint-full.js` extract wikilink targets from
raw page text without excluding backtick code spans (inline code or fenced blocks). The
run returned 10 `missing_targets`; the executor adjudicated **all 10 as false positives**
and applied none:

- 9 are DQL/Bases **syntax examples** inside code spans: obsidian-dataview's
  `FROM [[note]]`, `FROM outgoing([[note]])`, and its `[[food]]`/`[[exercise]]`/
  `[[link]]`/`[[assignment math]]`/`[[math]]`/`[[class]]` table-example rows;
  obsidian-bases' `![[File.base]]` and `![[File.base#View]]`.
- The 10th (`nfl-defensive-scheme-evolution` → `2026-02-14-macdonald-defense`) is a bare
  source **filename in a sources list**, not a wikilink at all — a second extraction
  defect (matching non-wikilink text), same scanner.

A less careful executor would have "repaired" working documentation pages — the
report's `fixes_applied:` block records the adjudication. The failure shape is the same
one B10-2(5) named (a check whose whole output is false), one layer up: the population
predicate is now right; the per-page extractor is the remaining liar.

## The fix direction

Exclude code spans (inline backticks and fenced blocks) from wikilink extraction in the
page-scan prompt/logic of `skills/vlt-lint/assets` (the full-mode fan-out), and require
extracted targets to actually be wikilink-shaped. Fixture: a page carrying a fenced DQL
example plus a bare filename in a sources list must contribute zero missing-target flags.
