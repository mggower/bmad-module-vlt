# The page scanner under-returns outbound links, and one miss manufactured an orphan

**Filed:** 2026-08-26 · **Vault:** `{field-vault}` · **Module:** v0.16.1
**Instrument:** full-mode `vlt-lint` sweep, `_agent/lint-reports/2026-08-26-1046-lint.yaml`
(146/146 pages, 0 cached — cold run)
**Filed by:** the factory session, transcribed from a `{field-vault}` session's relayed report,
**not** through the `vlt-feedback` rail — so this filing carries no `origin:` header and is not
rail-materialized. Do not re-file it upstream: a rail copy would materialize a second time
(the `origin:` header is the only idempotency key, and this filing has none). Claims were
re-verified factory-side against the lint report on disk and against shipped module source
before filing; the reproduction below was run at rest, not relayed.
**Related:** shares the scan→reduce seam shape with
`2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md`

## What happened

`fantasy-football-evaluation` returned **9** outbound links against **14** actually present on
the page. One of the five dropped links was a real wiki→wiki `[[link]]`, and its absence
manufactured **the sweep's only orphan** — a page reported as unreachable that is, in fact,
reached.

Measured across the full corpus, not inferred from the one case: **11 of 146 pages
under-returned, 23 dropped instances, exactly 1 of them wiki→wiki.**

## Why it matters, and the one thing that limits the damage

The link graph the reduce builds is **not complete**. Every consumer of it inherits the
incompleteness.

The saving grace is directional and worth stating precisely, because it bounds the severity:
a **dropped** outbound link can only ever *fake* an orphan — it can never *hide* one, and it
can never fake a `missing_target`. So `missing_targets` is undamaged in direction, and orphan
reports are **over-** rather than under-inclusive. The failure direction is the safe one. But
"safe direction" is not "correct": an orphan report that is 1-for-1 false is a report the
reader learns to distrust, and distrust of a true orphan is the expensive outcome.

## The shape

This is the reduce trusting a scanner-returned **enumeration** the way the guard filing's
defect is the reduce trusting scanner-returned **prose**. In both cases the reduce performs
exact, careful arithmetic over a value it has no way to know is complete. The link count is
independently checkable from page text — the reduce could verify the return rather than
consume it.

## Candidate direction (not a ruling)

1. **Verify the enumeration mechanically.** `[[...]]` extraction is a regex, not a judgment
   call — the reduce (or a cheap non-agent pass) can count them itself and use the scanner's
   return only for what genuinely needs reading. This is the same "decide what can be decided
   without an agent" move build-1 made for the frontmatter claim.
2. **Cross-check and flag divergence** rather than replace: keep the scanner's return, compare
   it against a mechanical count, and surface a seam-divergence finding when they disagree.
   Cheaper to ship, and it measures the seam instead of assuming it.
3. Ask the scanner to return links more carefully. **Named to be rejected** — this is the
   prompt-side fix whose failure is the entire premise of Cycle 13.
