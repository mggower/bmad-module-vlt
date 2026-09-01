# An HTML-escaped scanner return failed the reduce's exact comparison

**Filed:** 2026-08-26 · **Vault:** `{field-vault}` · **Module:** v0.16.1
**Instrument:** full-mode `vlt-lint` sweep, `_agent/lint-reports/2026-08-26-1046-lint.yaml`
**Filed by:** the factory session, transcribed from a `{field-vault}` session's relayed report,
**not** through the `vlt-feedback` rail — so this filing carries no `origin:` header and is not
rail-materialized. Do not re-file it upstream: a rail copy would materialize a second time
(the `origin:` header is the only idempotency key, and this filing has none). Claims were
re-verified factory-side against the lint report on disk and against shipped module source
before filing; the reproduction below was run at rest, not relayed.
**Related:** shares the scan→reduce seam shape with
`2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md`

## What happened

`battery-storage-technologies` carries `category: "Energy & Clean Tech"`. The wiki index H2 is
`Energy & Clean Tech`. **They match.** The scanner returned `Energy &amp; Clean Tech`, and the
reduce's category comparison — deliberately exact, case-sensitive and un-trimmed — failed.

That produced **the sweep's only `category_no_match`**, and it was false.

## Why the comparison is right and the input is wrong

The exactness is not the bug, and it should not be softened as a reflex. The comparison is
strict on purpose: a category that differs from its index heading by case or trailing space is
a real drift the vault wants caught, and every loosening of the comparison retires a class of
true finding.

The bug is that a value **passed through an agent** arrived transformed. The scanner did not
mis-read the page; it re-encoded what it read, and the encoding is invisible at the seam. Any
character with an HTML entity form is exposed — `&`, `<`, `>`, quotes — and `&` in a category
name is not exotic.

## The shape

Same seam, third instance today: the reduce performing exact work over a value it assumes is
verbatim. `PAGE_SCAN` marks fields *verbatim* in its schema description — and A13-1 Finding 2
already established that the schema description is an instruction, not an enforcement point.
This is that finding's second face: not a field the agent **paraphrased**, but one it
**re-encoded**. The prohibition is stated where it cannot bind, again.

## Candidate direction (not a ruling)

1. **Normalize entity-encoding on intake at the seam**, once, for every value the reduce
   compares exactly — decode HTML entities as a scanner-return hygiene step, without touching
   the comparison's strictness. Narrow, cheap, and it preserves every true finding the exact
   comparison exists to produce.
2. **Read the category mechanically** rather than through the agent — frontmatter is parseable
   without judgment, so the exact comparison could run against parsed YAML on both sides and
   never traverse an agent at all. Strictly better where it applies; the question is how much
   of `PAGE_SCAN`'s return that argument generalizes to.
3. Loosen the comparison (trim, case-fold, entity-agnostic match). **Named to be rejected** —
   it retires real drift findings to work around a transport defect, and leaves the transport
   defect live for every other exactly-compared field.
