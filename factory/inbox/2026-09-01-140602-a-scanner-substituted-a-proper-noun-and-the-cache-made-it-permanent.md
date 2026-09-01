# A scanner substituted a proper noun, and the cache made it permanent

_Filed 2026-09-01 from **`{field-vault}`**'s `{lint_reports}/2026-09-01-1406-lint.yaml`. **Second
consecutive sweep**, and the second occurrence is the one that matters — it arrived from the
**findings cache**, not from a re-scan. Evidence is `{field-vault}`, read-only._

## The claim

A page scanner (haiku) **substituted a proper noun** in a returned wikilink, and the substituted value
reached `fix_now` as a missing target.

The page `seattle-seahawks` links
`[[_agent/research/2026-07-26-112444-espn-top-10-cornerbacks-2026]]`, which **resolves**. The scanner
returned `...-espn-top-10-cornerboxes-2026` — **`cornerboxes` for `cornerbacks`**. The prompt is
explicit about this: *"Extract verbatim: do not normalize, and keep any |alias, #anchor, or path
prefix intact."*

⚠ **This is the failure class the entity-collision check exists to catch in sources, occurring in the
instrument that feeds it.** A check that hunts substituted proper nouns across pages is being fed by a
reader that substitutes proper nouns.

## The amplification, which is new this run and is the reason to file

On 2026-08-30 this was one scanner's bad return on one page — recorded as variance. **On 2026-09-01 it
recurred, and `seattle-seahawks` was NOT among the five pages that were re-scanned** (those were
`drake-maye`, `fading-food-and-cue-reliability`, `nfl-2026-offense-rankings`,
`shanahan-offensive-system`, `throne-of-glass-series-overview`). It was served **from the cached
record**.

**A scanner error, once cached, is now permanent for the life of the sidecar.** It survives every
subsequent sweep, and re-running the lint — the ordinary response to a suspect finding — **cannot
re-derive it**, because reuse is the cache working correctly. The finding is stable, wrong, and no
longer traceable to a model call anyone can inspect. The cache is not defective here; it faithfully
preserves what it was given. That is precisely why the input's fidelity now matters more than it did.

## Candidate directions (not a fix — capture's call)

1. **Verify a `missing_targets` entry against the page before it is auto-fixable.** The slot sits in
   `fix_now`, whose legal response creates or repoints a target — acting on a substituted slug creates
   a page that should not exist or repoints a link that was correct. The SKILL today leaves this to
   the operator's judgement; both sweeps caught it **only because a careful operator checked every
   entry by hand**. A slug the scanner returned that is absent from the page's own bytes is
   mechanically detectable, and it is the same *verify-the-return-before-trusting-it* posture Cycle 13
   and Cycle 14 build-1 already established for the frontmatter verdict.
2. **Give a cached record a provenance and an invalidation path**, so a return later shown to be wrong
   can be evicted without discarding the whole sidecar. Today the only remedies are editing the page
   or a full cold sweep.
3. **Model choice is NOT the direction, and is named here to be refused.** One substitution across two
   sweeps does not justify moving the scan phase off haiku — the scan phase is 146 agents cold and the
   cost case for haiku is unchanged. **Direction 1 makes the substitution harmless regardless of which
   model made it**, which is the more robust fix and the one that survives a future model change.

## Grounding

- `skills/vlt-setup/assets/workflows/vlt-lint-full.js:228-229` — `pageScanPrompt`'s verbatim-extraction
  instruction.
- `{lint_reports}/2026-09-01-1406-lint.yaml:225` (the refusal, and the run's `lint_cache` line naming
  the five re-scanned pages) and `{lint_reports}/2026-08-30-1123-lint.yaml:229` (the first occurrence).

⚠ **Confidence:** the substitution itself is certain (both reports name it, and the live link resolves).
The claim that the second occurrence came from cache is **inferred** from `seattle-seahawks` being
absent from the named five re-scans — strong, but capture should confirm against the sidecar's record
for that page rather than take it from this filing.

_Ship-verifiable at rest for direction 1: a returned slug absent from the page's bytes is checkable
against a fixture. The substitution itself is not reproducible on demand — see `[P-19]`._

⚠ **THIRD consecutive sweep, 2026-09-01 15:19** (`{lint_reports}/2026-09-01-1519-lint.yaml`) — the
`cornerboxes` substitution re-fired unchanged. That sweep reused **145 of 146** records (one rescan:
`fading-food-and-cue-reliability`), so `seattle-seahawks` was again served **from cache**. This is the
second independent confirmation of the amplification claim above — the ⚠ confidence caveat on it can
now be discharged by capture rather than re-derived.
