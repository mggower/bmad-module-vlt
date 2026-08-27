# The summary-length check counts the raw YAML line, not the parsed value

_Filed 2026-08-27 from the first full `{field-vault}` sweep after the v0.16.2 upgrade
(`{lint_reports}/2026-08-27-1104-lint.yaml`, `instrument_findings`). Evidence read-only._

## The claim

`malformed_frontmatter` flags `summary exceeds 160 characters` by measuring **the raw frontmatter
line including its quoting**, not the parsed scalar. Two of ten findings in this sweep were
refuted on exactly that basis — the parsed values are under the limit.

## Specimen manifest

Population: 10 `malformed_frontmatter` findings, one sweep. **8 genuine, 2 refuted (20% false
positive).** Both refutations are the same artefact.

| Page | Reported | Verdict |
|---|---|---|
| `barbacoa` | `summary exceeds 160 characters (171)` | **REFUTED** — parsed value under the limit; the raw line was counted, quoting included |
| `l-theanine` | `summary exceeds 160 characters (161)` | **REFUTED** — same artefact |

The 8 genuine findings are notable in the other direction and should not be lost: **3 of them
(`career-history-as-evidence`, `nfl-2026-position-rankings`, `technical-hiring-pipeline`) parse
cleanly under PyYAML and were still correctly flagged** — the scanner caught a semantic mis-key
that a parser cannot see. The instrument is not weak; it is measuring the wrong string in one
specific test.

## Why it matters

A false positive in `malformed_frontmatter` is not cosmetic: the class routes to `fix_now`, so a
refuted finding invites an auto-fix that rewrites a `summary:` which was never too long. The
2026-08-27 sweep refuted these by hand; nothing in the shipped surface would have.

The near-miss margin makes it worse — `161` against a `160` limit. Quoting overhead alone can
carry a compliant value over the line, so the error is systematically biased toward flagging
values that sit just under.

## Candidate directions (capture will ground these)

1. Measure the **parsed** scalar, not the source line.
2. If the raw line is deliberate (a byte-budget concern rather than a prose-length one), say so in
   the finding text and rename the check — the current wording states a claim about the summary.

Related: this sweep is the same one that discharged Cycle 14 build-1's population measurement.
