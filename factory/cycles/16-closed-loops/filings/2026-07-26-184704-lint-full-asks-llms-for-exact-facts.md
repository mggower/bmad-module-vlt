# Finding: `vlt-lint-full` asks LLM scanners for exact mechanical facts, then compares them exactly — 87% of its structural findings were false

_Filed 2026-07-26 by the Librarian (Gwyn) after a full lint of vlt-core (128 wiki pages). Classification:
**pattern**, with two `defect` instances. **This is a regression report against an archived filing** —
`inbox/archive/2026-06-06-193105-vlt-lint-full-infra-and-cost-fixes.md` §5 reported this class, its fix
(`crossLayerSlugs`) shipped, and the false-positive rate went **up**. The parameter treated the symptom
and left the seam._

## The seam, stated once

`vlt-lint-full.js` fans out one LLM scanner per page, asks each for **exactly-computable mechanical
facts** (character counts, normalized link keys, byte-level string identity), and then the JS reduce
performs **exact deterministic operations** — set membership, integer comparison — on those answers.

An LLM is a lossy channel for an exact fact. The reduce is written as though it is not. Every false
positive in this run entered through that seam; **not one** came from the judgment-shaped checks.

## The measurement (one full sweep, 128/128 pages, no coverage caps)

| Check class | Reported | False | Rate |
|---|---|---|---|
| `missing_targets` | 73 | 63 | 86% |
| `frontmatter_drift` (summary length) | 7 | 6 | 86% |
| `category_no_match` | 1 | 1 | 100% |
| `near_duplicates` | 4 | 4 | 100% |
| **Mechanical subtotal** | **85** | **74** | **87%** |
| `contradictions` / `entity_collisions` / `stale` / `thin_pages` | 24 | ~0 verified false | — |

Of the 10 surviving `missing_targets`, **all 10 were already registered** in the index's
`## Stubs (linked, not yet written)` section as deliberate stubs with graduation triggers — so the
check's actionable yield for the run was **zero**.

Meanwhile the judgment half did real work: all 3 `entity_collisions` verified genuine (two are
plausible auto-caption substitutions, one is probably a real 2019→2024 supersession), and both
contradictions I spot-checked were real enough to earn callouts on four pages.

## Instance 1 (defect) — path-form links never match the cross-layer set

`vlt-lint-full.js:78` specifies the scanner's return as:

> `outbound_links: … 'wiki page slugs this page links to ([[...]] targets), normalized to slugs'`

`:155` then does exact membership:

```js
for (const s of scans) for (const l of s.outbound_links || []) if (!slugSet.has(l) && !crossLayer.has(l)) missing_targets.push(...)
```

The SKILL supplies `crossLayerSlugs` as **basenames** (`2026-06-26-141500-quarter-beef-cut-atlas-method-fat`).
But vlt-core writes cross-layer links in **path form** — `[[_agent/research/2026-06-26-141500-quarter-beef-cut-atlas-method-fat]]`
— and the scanner returns that verbatim. It is not wrong to: for a path-form link, the path *is* the
target, and "normalized to slugs" does not tell a model to take a basename. The two sides disagree about
what a "slug" is, and the disagreement is only visible in the reduce, as a false finding.

**Why the shipped fix didn't hold.** The archived filing's remedy added the `crossLayerSlugs` channel.
That was necessary and it works — for links already in basename form. It did not add **normalization at
the comparison**, which is where the mismatch actually lives. Rate before: 14/17 (82%). After: 63/73 (86%).

**Suggested shape** (owner steers): normalize both sides at `:155` before comparison — strip any
directory prefix, `.md`, `#anchor` and `|alias` from `l`, and match on the basename; keep the raw string
for the report line. One-line-ish, deterministic, and it makes the scanner's "normalized to slugs"
instruction non-load-bearing rather than load-bearing-and-ambiguous.

## Instance 2 (defect) — the scanner is asked to count characters

`vlt-lint-full.js:83`:

> `summary_issue: … "empty if summary: is present and ≤160 chars; else 'missing' or 'over-length (N chars)'"`

Six of seven `over-length` findings were false. Measured against the actual `summary:` string values:
ashwagandha 155, carbon-steel-cleaning 159, carbon-steel-cookware 141, glucose-metabolic-health 156,
l-theanine 159, pickled-red-onions 160 — all inside the limit, all reported at 161–169. The consistent
overshoot (~+9 to +11) is the length of `summary: ` plus the surrounding quotes, so the model measured
the raw frontmatter *line* rather than the field *value* — and could not have verified either by counting.

Only `doneness-and-carryover` (171) was genuinely over. Fixed this run.

The same shape produced the `category_no_match` finding: the scanner reported `grid-bottleneck-thesis`
carrying an HTML-entity `Energy &amp; Clean Tech` against an H2 of `Energy & Clean Tech`. The file's raw
bytes hold a literal `&`, and the H2 matches exactly. A byte-identity claim, asserted by a model, wrong.

**Suggested shape:** these are file-local, exactly-computable, and need no page comprehension —
frontmatter field presence, field length, `topic:`-is-a-list, `category:` membership in the H2 set, link
extraction, attestation freshness, `review_after` / `revisit_after` expiry, and the thin-page counts.
Compute them in the reduce (or in the SKILL, which already has filesystem access) directly over the raw
files, and delete them from the scanner schema.

## Why this is worth a re-cut and not another patch

The checks that misfire are precisely the ones a short script computes **exactly and for free**. The
checks that held up are the ones that genuinely need a reader. The current design has these backwards:
it spends the expensive, lossy resource on the cheap, exact work.

The corroborating datapoint from the same session: the SKILL-side governance passes (convention/baseline
diff, `depends_on` handshake, capability lane-safety, family invariants, PARA attestation, the
`{research}` absorption-union sweep) are plain scripts plus targeted reads. Ten checks, **zero false
positives**, negligible cost.

**Cost, since it argues the same way:** this run spent **151 agents, 6,466,038 subagent tokens, 996 tool
uses, ~38 minutes** — the large majority on 128 per-page scanners whose mechanical output was 87% noise
and whose judgment output would survive a much smaller cluster-reader fan-out.

Candidate direction, explicitly **not a design**: keep the fan-out for contradictions, entity collisions,
stale claims, unmarked supersessions and sources-vs-prose divergence; move every file-local determinable
into a deterministic pass; and let the scanner schema shrink to the judgment fields plus the key-claim
summaries the cluster passes need.

## The cost the false positives actually impose

Not reviewer annoyance — **the SKILL is the single writer**, so every one of these lands in front of a
partner who must verify before applying. Verifying 85 mechanical findings to salvage 11 took the larger
part of this sitting. And the failure is asymmetric in the dangerous direction: a lint whose structural
findings are 87% noise trains its reader to skim, which is exactly the posture in which the *real*
findings — three entity collisions, an unflagged acid-on-carbon-steel recommendation — get waved through.

There is also a silent-zero edge here worth a look: because `files_checked == files_listed == 128` and
`coverage_caps: []`, the run reports as **exhaustive**, and it was — the sweep's *coverage* was complete
while its *accuracy* was not. Nothing in the report shape distinguishes those.

## Honest limits

- **Single vault, single run** for the 87% figure. The 2026-06-06 archived filing is the only prior
  measurement and it agrees on the class (82%) — but both are vlt-core, and vlt-core's heavy use of
  path-form cross-layer links may be a local writing habit rather than a general one. If vlt-sayari
  writes basename-form links, instance 1 would not fire there at all.
- **The `crossLayerSlugs` regression claim is about rate, not mechanism.** I did not diff the shipped
  workflow against its pre-fix version; I am reading `:155` as it stands today. The characterization
  "the fix treated the symptom" is my reading of the code, offered as a guess.
- **Near-duplicates (4/4 false) may be a different root cause.** The pairs fired on `nfl-2026-*` — a slug
  stem shared across six pages — plus co-cited links. That looks like the hub-exclusion heuristic from
  the archived filing's §4 being defeated by a *stem* that is really a namespace, which is adjacent to
  but not the same as this seam. Worth separating at capture.
- I did not re-verify the 16 contradictions individually; I verified 2 in depth and both were real. The
  "~0 false" for the judgment column is therefore weaker evidence than the mechanical column's count.

## Provenance

- This run's report + fixes — `_agent/log.md` `## [2026-07-26 18:05] lint (librarian) | full`; commit `c081a52`.
- Prior filing of the same class, captured and archived —
  `inbox/archive/2026-06-06-193105-vlt-lint-full-infra-and-cost-fixes.md` §5 (cross-layer links) and §4
  (near-duplicate over-fire).
- Code read this run — `.claude/workflows/vlt-lint-full.js:78` (scanner schema), `:83` (summary_issue),
  `:145–155` (the reduce), `:153` (`crossLayer`).
- Backlog items filed from the surviving real findings — `_agent/backlog.md` (5 items, 2026-07-26).
