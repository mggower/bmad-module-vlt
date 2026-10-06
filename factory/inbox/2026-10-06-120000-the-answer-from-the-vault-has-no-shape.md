# The answer from the vault has no shape — `vlt-query` asks for tensions and gaps in prose, fixes no structure for either, and ranks disagreement by recency

_Filed 2026-10-06 by the **factory**, from an owner problem-solving session contrasting the module
with an external partnerless vault kit (`bmad-cis-problem-solving`; session artifact gitignored).
Evidence is module source at `d3111e0` (v0.19.0), read-only, plus the external kit read in source.
Kind: `candidate`. Cause: **`ST-10`** (`factory/studies/ST-10-continuity-is-actor-held-by-default.md`,
the contributing cause — the return path is the thinnest shipped surface) — cited, not restated.
Owner elected to file. **Independent** of the three sibling filings; needs no convention bump._

## The claim

The skill that turns the corpus into an answer is among the smallest op skills the module ships
(`skills/vlt-query/SKILL.md`, one file, ~1.0K words) and its output has no fixed parts. It does
ask for the right things — provenance per claim, contradictions named, edges flagged — but as
bullets of advice inside *Step 3: Synthesize and respond*, so whether an answer carries a
tensions section or a gaps section is the executor's call on the day. Where pages disagree it
orders them by recency and source count, which rewards the newest and most-cited page whether or
not its evidence is better.

## Grounding (module source, `d3111e0`)

- **Tensions are advice, not structure.** `vlt-query:34`: *"Rank contradictions, don't bury them.
  When pages disagree on something relevant, name the disagreement and order the views by support
  — more recent (`last_updated`) and more sources first."* Recency is the first ranking key.
- **Gaps are one line.** `vlt-query:35`: *"Flag the edges — where the vault's knowledge is
  incomplete or uncertain."* Nothing routes a gap anywhere; the backlog's `knowledge-gap` kind
  (`frontmatter.md:290`) is the existing home and the skill never names it.
- **Format follows the question type** (`:36`: lookup → prose, comparison → table, decision →
  headed sections), so no part of an answer is guaranteed present.
- **No reading-before-concluding rule.** Steps 1–3 (`:19`, `:25`, `:29`) are read index → read
  pages → respond; nothing separates gathering from weighing.
- **The contradiction record is richer than the reader of it.** `wiki-supersession.md:77–97`
  gives every contradiction callout an `open | adjudicable` disposition. `vlt-query` does not
  read the disposition when it reports a disagreement.

**No set was observed** — this filing rests on one skill file's text, not on a population of
answers. No `{field-vault}` query output was sampled.

## The external contrast (read in source, `seanathon/vault-starter` @ `fef0118`)

Its `consult` skill binds five things: vault first with general knowledge labelled; all reading
finished before any conclusion; one claim table across every relevant source, weighed by evidence
type, source incentive and corroboration, with freshly read material given no extra weight;
disagreements surfaced as the most valuable output; and a fixed delivery — **answer first,
grounds, tensions, gaps, provenance flags**. A brief borrowing from it owes a spike over that file.

## Why it matters

- **A corpus is a cost until it is consulted.** Seven cycles of work went to whether the
  machinery reports honestly; this is the surface where the owner gets something back.
- **It is the cheapest test of `ST-10`.** If a shaped answer makes the corpus visibly carry what
  the owner now asks a partner to remember, the home question starts answering itself.
- **Recency ranking is a quiet bias** of the same family `ST-8` named: what was touched last
  reads as what is true.

## Candidate shape (ideation rules)

1. **A fixed four-part answer** for any question that is not a single-page lookup: *answer* (for
   this question, a few sentences) · *grounds* (cited, grouped by where they agree) · *tensions*
   (stated as open choices, each side's evidence, the callout's disposition where one exists) ·
   *gaps* (what the question needs that the vault lacks).
2. **Gather, then weigh.** All reading completes before any conclusion is formed.
3. **Weigh by evidence, not freshness.** Replace `:34`'s ordering with corroboration and evidence
   quality; `last_updated` breaks ties only.
4. **Gaps write through** to the backlog as `knowledge-gap` items (or a relay where addressed —
   the address rule, `frontmatter.md:294`), offered, not automatic.
5. **A name that is not "consult".** `consult` is already the cross-partner mechanism
   (`conventions/consult.md`, `vlt-dispatch`). This is an answer shape inside `vlt-query`, not a
   new mode and not a new skill.

Page-level citation is sufficient for all five. Claim-level grounds arrive, if they do, with
`2026-10-06-120100`.

## Acceptance (draft)

- **Ship-verifiable:** the four parts named in `vlt-query` with the lookup carve-out; the
  recency-first ordering gone from `:34`; a fixture question over a fixture wiki with one
  dispositioned contradiction yields an answer whose tensions part quotes the disposition;
  `depends_on` unchanged.
- **Field-contingent:** three real questions in `{field-vault}` answered in the shape, with at
  least one gap filed to the backlog from an answer.

## Related filings

`2026-10-06-120100` (claim addresses — upgrades this filing's grounds from page to claim);
`2026-10-06-120300` (the lens cut — this filing is what a lens reads continuity through).
