# A persisted lint report is not machine-readable — the mandate has no emission discipline behind it

_Filed 2026-08-27 from **Cycle 14 build-4's at-rest acceptance run** (check (1), graded against
read-only copies of `{field-vault}`'s `{lint_reports}` archive). This is the **first grading of a
`vlt-lint` report as a parseable artifact** — the check that A14-5 asked for. It FAILED, and the
failure is A14-5's predicted harm arriving on a real file rather than in argument. Evidence is
`{field-vault}`, read-only; nothing in the vault was edited._

## The claim

`vault-operating-contract.md` mandates that a structured report-emitting verb persist its report
as a dated plain file under its report dir, and `vlt-lint` Step 6 persists a report block an
**agent hand-authors**. Nothing between those two facts is an emission discipline. **One archived
report in six does not parse**, so the mandate produces artifacts that a machine cannot read —
which is the entire reason the mandate exists.

## Specimen manifest

Population: 6 `.yaml` reports in `{field-vault}`'s `{lint_reports}`, parsed with `yaml.safe_load`.

| Report | Result |
|---|---|
| `2026-08-23-1504-lint.yaml` | OK |
| `2026-08-23-1739-lint.yaml` | OK |
| **`2026-08-24-1700-lint.yaml`** | **FAIL** |
| `2026-08-25-1600-lint.yaml` | OK |
| `2026-08-26-1046-lint.yaml` | OK |
| `2026-08-27-1104-lint.yaml` | OK |

**1 of 6 (16.7%).** Minimal triggering fragment, at line 102:

```yaml
  research_zone: 145 notes scanned; 24 carry revisit_after:
```

A bare unquoted scalar containing `: `. YAML reads the second colon as a nested mapping key:
`mapping values are not allowed here, line 102, column 59`. Quoting the scalar
(`"145 notes scanned; 24 carry revisit_after:"`) parses clean — verified.

## Grounding

- `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:330` — the persist mandate
  (widened this cycle from a `.yaml` literal to *the format that verb declares*).
- `skills/vlt-lint/SKILL.md:74` — Step 6 persists the Step-5 block content-verbatim.
- `skills/vlt-lint/references/report.md` — the report block is **agent-authored**; there is no
  source object and, by Cycle 14 build-4's ruling, deliberately **no serializer**. The enforcement
  point for a report is a **reader**, not a writer.
- Cycle 14 build-4's acceptance check (1) is that reader. It exists, it ran, it failed.

## Why it matters

The failing scalar is prose a scanner wrote into a structured slot. No rule forbids it, no
instrument saw it, and the report was persisted, dated, and archived looking exactly like the five
that parse. **A report that cannot be read is indistinguishable on disk from one that can** — so
every downstream claim resting on "the archive" silently rests on 5 of 6.

This is the cycle's own through-line landing on the cycle's own instrument: the module states the
rule, `vlt-lint` Step 6 is the place responsible for it, and that place has no way to decide
whether what it is about to persist satisfies it.

## Bound and disposition

Build-4's check (1) **gates and is graded FAIL** — owner-ruled 2026-08-27: *do not re-scope a
check to make it pass.* The check's honest subject going forward is reports written **under** the
mandate; a report predating the rule cannot be evidence about the rule. That re-grade belongs to
`acceptance-discharge` against post-release-2 reports, not to a narrowing written after the fact.

The archived report was **not repaired** — the vault's archive is the owner's record, append-only,
and editing field evidence to satisfy a test is the failure mode this cycle exists to close.

## Candidate directions (not a fix — capture will ground these)

1. **A pre-persist parse gate in Step 6** — the reader exists; run it before the write, not after.
2. **Constrain the emitting slots** — a free-prose scalar in a structured slot is the proximate
   cause; the `.json` render already sidesteps it, which is why the `.json` limb passed.
3. **Neither, and say so** — declare the archive best-effort and stop claiming it is machine-read.

Related: the `.json` alternative shipped in the same build is a **cure available to the author**,
not an enforcement point. Nothing makes an author choose it.
