# The `governance_memory` denominator missed 12 entries for an unknown number of sweeps

_Filed 2026-08-27 from the first full `{field-vault}` sweep after the v0.16.2 upgrade
(`{lint_reports}/2026-08-27-1104-lint.yaml`, `instrument_findings`). Evidence read-only._

## The claim

`governance_memory` counted decision-log entries with a pattern that matches only the **bracketed**
heading form, silently excluding the 12 oldest entries, which use an unbracketed
`## YYYY-MM-DD —` heading. The sweep's own correction:

> `governance_memory` denominator corrected: prior sweeps' 47-entry decision-log count missed the
> 12 oldest entries, which use an unbracketed `## YYYY-MM-DD —` heading. **True population is 59
> entries, 24 unclassifiable.**

## Specimen manifest

| Quantity | Reported by prior sweeps | True |
|---|---|---|
| Decision-log entries | 47 | **59** |
| Undercount | — | **12 (20.3% of the true population)** |
| Unclassifiable | — | 24 |

The 12 missed entries are **the oldest**, so every prior sweep's governance-memory metric was
computed over a window biased toward recent decisions.

## Why it matters

This is a denominator, so it silently rescales every ratio built on it. Unlike a false positive,
**nothing about the output looked wrong** — 47 is a plausible number and no finding was raised.
It was caught only because a sweep re-derived the population rather than trusting the counter.

The failure is a heading-shape assumption hardcoded where the decision-log convention permits more
than one shape. That makes it a **format-drift blind spot**, not an arithmetic bug: the counter is
correct about the entries it can see, and has no way to know it cannot see the rest.

## Candidate directions (capture will ground these)

1. Match both heading forms, and state the matched population in the report so a future undercount
   is visible rather than inferred.
2. Better: have the counter report **what it matched against what exists** — a count with no
   denominator is the shape Cycle 14 build-2 ruled against for `cache_rejected` (rendered with its
   denominator, precisely so a discard is never silent). The same reasoning applies here.
