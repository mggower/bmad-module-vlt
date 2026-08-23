# Graduation Queue — field calibration from a full-zone audit (supplements the 114226 filing)

_Filed from `vlt-core` on 2026-07-11, same day as `2026-07-11-114226-research-note-graduation-queue.md`. That filing was design-stage with **no field evidence**; this one supplies it. The owner ran a one-time manual audit of the entire research zone against the wiki — a mechanical reverse-index over all 90 research notes × 123 wiki pages, then a 9-agent domain fan-out reading every note in full against its related pages. This is effectively **Slice 0 executed plus the first manual drain**, and it materially changes several of the 114226 filing's design assumptions. Full report: `vlt-core` `_agent/artifacts/research-wiki-audit-2026-07-11.md`._

## Headline results

90 notes audited: **76 fully absorbed, 8 partially ingested, 5 orphaned-ripe, 1 terminal.** The queue the mechanism would have surfaced is real (14 actionable items found, one high-priority) — the design's premise holds. But the detector as specced would have fired on the wrong set:

**Calibration caveat — this evidence is from the benign case.** `vlt-core` turns out to be a *low-orphaning* vault: research→ingest almost always runs, so most losses here are partial-ingest residue, not true orphaning. The owner's second vault (the work vault, where research supports development projects and routinely goes un-ingested) is where the 114226 filing's actual pathology lives — but it has no access to this inbox, so this filing carries the signal on its behalf: the mechanism's acceptance run should happen there, not here, and its audit may show a different signal mix (true K-threshold accretion, a lower orphan-projection false-positive rate because ingests never ran). Treat the numbers below as one vault's profile, not the population.

## 1. The orphan projection as specced is ~79% false-positive — CHANGES change 2

The 114226 filing's orphan projection is "reverse-index all wiki `sources:` → research notes cited nowhere." In `vlt-core` that marks **62 of 90 notes orphaned; 49 of the 62 are fully absorbed anyway.** Three causes, all structural:

- Wiki pages cite the **underlying source** (URL / `sources/` file), not the research note that read it. Research notes are only frontmatter-cited when they *are* the source (agent-authored dives). Both note and page cite the same upstream source — a **shared-source overlap** check catches this.
- Pages back-reference notes via **body wikilinks** (`[[_agent/research/…]]`) and **prose Sources entries** that a frontmatter-only scan misses (five reading notes + a tea note were flagged orphan while directly linked from page bodies).
- Frontmatter `sources:` entries are sometimes human prose ("QOS reading notes — Mikey, May 2026"), not paths.

**Ship the projection as a union: frontmatter citation ∪ body wikilinks ∪ shared-source overlap.** With the union, `vlt-core`'s residual orphan set is ~13 notes and contains every genuine gap. Without it, the Graduation Queue's first emission is a 49-item false-positive firehose — the exact alarm-fatigue failure the filing warns about, arriving through the projection rather than the terminal notes.

## 2. `cluster_ripe` is not viable on current `topic:` data — RESOLVES open question 2

The Slice-0 sample the filing asked for is done. Answer: **too ragged to cluster without normalization.** Four serialization styles coexist (bare string; comma-joined string that parses as ONE string; slash-joined string; proper YAML list) with a clean drift boundary (pre-July ragged, July+ clean). Vocabulary drifts within domains (`dog training` / `dogs` / `dog-training`) and collides across them (`football` tags both NFL and soccer notes; the wiki disambiguates, the research zone doesn't). Only list-style notes matched anything.

**Recommendation: ship `revisit_after` + `linkage_ripe` in the first cut; gate `cluster_ripe` behind a documented normalization rule (split on comma/slash, kebab-fold, singleton == list) — or a lint finding nudging notes toward list-form topics, which fixes the substrate over time.** This is the filing's own fallback path, now evidence-backed.

## 3. K-threshold accretion was NOT the observed gap pattern — RESHAPES the signal set

None of the 13 genuine gaps was "≥K thin siblings, no wiki home." The signals that actually found gaps, in yield order:

1. **Date-ordering tell** (highest yield, trivially computable): a note whose `created` postdates its topic's entity page `last_updated`, with zero linkage of any kind → the page was built and *closed*, then a later sibling source stranded. The cleanest gap in the audit (an ashwagandha note arriving six days after `ashwagandha.md` shipped) fits exactly.
2. **Bundled-note residue:** multi-source notes where one source graduated and the other didn't. Implies the ingest-probe (change 5) should check **per-source / per-section**, not per-note — partial ingestion outnumbered full orphaning **8 to 5** in this vault; most knowledge loss happens *inside* ingests that ran.
3. **Fan-out droppage:** thematic fan-outs consistently drop the section with no natural home (company profiles, tabular indexes, trivia "firsts").
4. **Explicit deferral markers in wiki pages:** "deliberately deferred to a later session", Connections entries reading "not yet a wiki page" — near-explicit graduation requests sitting in page prose, harvestable and ageable by lint.
5. **Declared-connection diff:** verify each note's own Connections/`[[…]]` targets received the content, not just that *some* page absorbed the note (caught a routing failure: fact absorbed into the entity page, never propagated to the concept hub the note itself named).

`linkage_ripe` (a newer note citing an orphan) remains sound. `revisit_due` remains the cheap rail. But if the module ships only the filing's three findings, it misses the patterns that produced most of this vault's real losses.

## 4. Exempt-backfill is tiny — SHRINKS the migration concern

One terminal note in 90 (an empty personal interview scaffold — detectable as `status: in-progress` + zero sources). The feared terminal-orphan firehose didn't materialize because progress-log notes get absorbed into living wiki pages rather than orphaned. The capped one-time exempt pass in the filing's migration section is correct and nearly free.

## 5. Smaller signals worth a line each

- **Seasonal orphans:** two of the gaps are seasonal reference (spring foraging, December eggnog) — a detector that resurfaces seasonal orphans *ahead of season* beats age-based surfacing for this class.
- **Stale-flag ↔ research-zone join:** standing wiki stale-flags were partially serviceable from content already sitting in an orphaned research note. Stale-resolution guidance should say "check existing research notes before demanding new sources."
- **Living-document series reads** (serial progress notes superseding each other onto the same pages) should never be flagged individually ripe — only checked for per-note residue. A detector needs this class carved out or every book-progress note becomes queue noise.
- **Positive calibration baselines exist** in-vault for any future detector eval: the carbon-steel and dog-training clusters (zero gaps, same-day hub-and-spoke ingests) and the post-06-15 cooking pipeline (frontmatter citation + `[!superseded]` back-propagation throughout).

## Provenance

- Vault: `vlt-core`, audit of 2026-07-11. Report + full reconciliation queue: `_agent/artifacts/research-wiki-audit-2026-07-11.md`. Method: Phase-0 mechanical index (citation / shared-source / topic overlap) + 9 parallel domain agents reading all 90 notes and ~60 wiki pages in full.
- Supplements (does not supersede) `2026-07-11-114226-research-note-graduation-queue.md` — capture them together; this filing's items map onto that filing's change 2 (projection), open question 2 (topics/K), change 5 (ingest-probe granularity), and the migration section (exempt pass).
