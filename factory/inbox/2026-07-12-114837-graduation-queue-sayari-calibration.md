# Graduation Queue — second calibration, from the work vault (supplements 114226 + the 07-11 calibration)

_Filed 2026-07-12 **on behalf of `vlt-sayari`** (the work vault named in the 07-11
calibration filing as "where the 114226 filing's actual pathology lives"; it has no
access to this inbox). Provenance caveat: this evidence comes from a **factory-side
read-only inspection of an Obsidian-Sync snapshot** of the vault
(`~/Vaults/vlt-sayari`), not from a vault session — Sync drops hidden
folders and most non-md files, so `.claude/`, `_bmad/` contents, and `.baseline/` were
unverifiable; nothing below depends on those surfaces. Full dossier:
`skills/reports/handoff-2026-07-12/05-field-inspection-vlt-sayari.md`._

The 07-11 calibration warned its numbers were "the benign case" and predicted the work
vault "may show a different signal mix." The prediction was half right — and the half
that's wrong matters more for the design.

## 1. The union projection is now validated on BOTH vaults — ship it

Naive frontmatter-only projection on vlt-sayari: **9 of 13 research notes (69%)
"orphaned."** The union projection (frontmatter citation ∪ body wikilinks ∪
shared-source overlap) collapses that to **3 of 13 (23%)** — and one of the three is a
documented deliberate island (promotion condition evaluated and explicitly declined in
a resolved backlog item, 2026-07-09). The shared-source-overlap leg did the heavy
lifting here exactly as in vlt-core: five standup/testing notes each cite one
`sources/transcripts/` file that 2–3 wiki pages also cite — the durable/project-state
split working as designed, not orphaning. Two vaults, opposite usage profiles, same
result: the 114226 spec's projection is a false-positive firehose; the union is not.

## 2. The work vault's REAL pathology is throughput, not per-note orphaning — WIDENS the design

The predicted "true orphaning because ingests never ran" is not the dominant loss mode
here either. What the audit actually found, in order of severity:

- **The wiki froze after migration.** 29 of 34 pages are the 06-24/25 migration burst;
  **5 new pages in the following 17 days** against ~156 post-migration log operations
  and 94 sessions. Knowledge production is furious; wiki graduation is a trickle.
- **The pipeline stalls at the librarian-bound relay queue.** Of 9 open dispatch
  pointers, 4 are librarian-bound ingest relays open **12–15 days** (one itself carrying
  a second ingest "parked since 06-26"); the oldest open pointer of all is 16 days. The
  graduation mechanism's acceptance here should measure **drain latency** (relay-open →
  ingested), not just citation coverage.
- **Graduation-ripe knowledge mostly isn't in `_agent/research/`.** The clearest
  stranded items live in **handoffs (27 files), partner threads, and project status
  files**: e.g. the engineer's "failure-as-invisibility / over-claim" pattern distilled
  across 4 PR reviews sits in a thread wanting "a Librarian-filed wiki page … so it's
  canon rather than re-derived each review" — a graduation candidate that is not a
  research note at all. A detector scoped to the research zone alone misses most of
  what's stranded in this vault. Design implication: either widen the projection's
  scan surface (at least handoffs), or ship research-zone-first and name the wider
  surface as the known second cut — but decide it, don't default into it.
- **Deferred backfill compounds it:** the librarian thread carries a paused
  workspace-v2 migration ("carry the top ~8 research notes … archive the 22 transcripts
  read-only") — an acknowledged, unscheduled pile the queue inherits on arrival.

## 3. Substrate + demand signals — confirms the 07-11 filing

- **`topic:` raggedness reproduces:** 11 notes with YAML lists, 1 with a comma-joined
  string. The normalization prerequisite for `cluster_ripe` holds on this vault too.
- **The vault has asked for the mechanism, twice**, independently of vlt-core: the
  researcher's 2026-07-09 backlog item ("the vault has **no** mechanism to surface an
  old `{research}` note that has earned a wiki page … research notes carry no expiry
  axis and deliberately 'rest'") and the engineer's thread item above.
- **Lint coverage gap as a compounding factor:** no lint since 07-02; the 5 newest
  pages have never seen a lint pass; the librarian thread itself flags a page carrying
  "live external risk" for "the next lint pass." A due-queue with no lint cadence
  behind it surfaces nothing — the mechanism's acceptance run should note lint cadence
  as a dependency.

## 4. Acceptance-run design for this vault (the 07-11 filing assigned it here)

Measure: (a) first-emission size and false-positive rate under the union projection
(prediction from this audit: ~2 true items from the research zone, several more if
handoffs are in scope); (b) relay drain latency before/after; (c) whether the
date-ordering tell and bundled-note residue signals (07-11 calibration §3) fire — this
vault's two development-era research clusters give them a real substrate. Since this
vault cannot file results back, its acceptance evidence must be carried by the owner or
by a factory-side inspection like this one.

## Provenance

- Vault: `vlt-sayari` (work machine; synced snapshot), inspected 2026-07-12,
  version 0.6.0. Method: mechanical reverse-index over 13 research notes × 34 wiki
  pages (frontmatter + body links + shared-source overlap), plus full reads of
  dispatch, backlog, librarian/engineer threads, and the upgrade ledger.
- Supplements (does not supersede) `2026-07-11-114226-research-note-graduation-queue.md`
  and `2026-07-11-153000-graduation-queue-field-calibration.md` — **capture all three
  together**. This filing's items map onto 114226's change 2 (projection — now
  double-validated), the scan-surface question (new: §2), and the acceptance plan
  (153000's assignment of the run to this vault — now with concrete measures).
