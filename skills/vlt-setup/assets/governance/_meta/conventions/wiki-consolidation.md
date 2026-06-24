---
type: note
created: 2026-06-01
last_updated: 2026-06-01
title: Wiki Consolidation Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 1
consumers: [vlt-ingest]
---

# Wiki Consolidation Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/wiki-consolidation.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

This file defines the **merge discipline** for the wiki: what consolidation is, how candidate pairs are detected, how merge direction is chosen, how history is preserved via supersession, and how the subsumed page is archived.

**There is no standalone consolidate operation.** The work is split across two skills: `vlt-lint` **detects** near-duplicate / drifted pages and files a `maintenance` backlog item; `vlt-ingest` **executes** the merge — when an ingest meets a near-duplicate worth folding in, it does so here, under this discipline. Both read this file. Paths use the structure-map logical names (see the operating contract); defaults resolve through `vault_structure`.

## What consolidation is

Consolidation merges two (or more) wiki pages that have drifted into overlap — near-duplicates, split topics that should be unified, or a prior ingest that created a parallel page instead of extending an existing one. The wiki layer compounds well only if each concept has one canonical page; consolidation is the corrective pass that keeps the layer single-home.

Consolidation is **not detection.** `vlt-lint` finds candidates and files them to the backlog; it does not mutate. The merge — mutating wiki content, archiving pages, stamping supersessions — happens inside `vlt-ingest`.

Consolidation is **not a fresh ingest of new source material.** A merge reaches the wiki only, the same read boundary as `vlt-extract` — no new source is processed.

## When to consolidate

A merge candidate exists when:

- `vlt-lint`'s near-duplicate detection (or the fuzzy duplicate check in `vlt-ingest`) flags overlapping pages
- a topic has visibly split across pages (e.g. a concept page and an entity page that say most of the same things)
- two pages reference each other heavily and the reader keeps bouncing between them

Consolidation is **not automatic cleanup.** It requires human judgment on whether two pages *should* merge — many near-misses (slug overlap, shared wikilinks) are legitimately distinct concepts that should stay apart. If two pages are distinguishable by a single adjective or by reader intent, they are distinct — skip the merge.

## Candidate detection

When finding candidates (without a specific pair from the user), apply three heuristics:

**1. Slug stem overlap.** Pages sharing a leading token or primary noun (`shanahan-*`, `survivor-*`). Surface all clusters with ≥ 2 pages; highest precision.

**2. Wikilink co-occurrence.** Pages that link to ≥ 3 of the same other wiki pages. The floor is a rough heuristic — surface the overlap count alongside each pair so the operator can judge.

**3. Topic frontmatter overlap.** Pages whose `topic:` values intersect. Lower precision (topic labels are loose) but catches pairs that slugged differently while covering the same domain.

Present candidates as a ranked table with the signals broken out. Never propose a merge before human confirmation.

## Merge direction — primary vs subsumed

For each confirmed pair, one page becomes **primary** (retained, stays at its slug) and the other becomes **subsumed** (content merged into primary, page archived). Choose direction by, in order:

1. **Source count** — the page with more sources has more accumulated knowledge; prefer retaining it.
2. **Slug stability** — wider, more general slugs absorb narrower ones.
3. **Link incidence** — the page more often referenced from other wiki pages should stay (fewer backlinks to update).
4. **Recency of last update** — tiebreaker.

Always confirm merge direction with the operator before writing.

## Merge discipline

Merging is a wiki edit. It runs under the same supersession discipline as any other wiki change — defer to `wiki-supersession.md` for the shape of the callouts.

- **Additive content** from the subsumed page (new sections, sources, non-conflicting claims) folds into the primary with no callout — it's just new material arriving via a different channel.
- **Conflicting claims** use the inline `[!superseded]` callout, reason typically `contradicted` or `refined`. Never silently pick a winner.
- **Duplicated claims** (same fact in both pages) collapse into one — no callout; just de-duplication.

## Frontmatter — retained (primary) page

After a merge, the retained page's frontmatter:

- `created:` — unchanged (the retained page keeps its birth date)
- `last_updated:` — set to the merge date
- `author:` — stays `agent`
- `trust:` — stays `raw` (human can promote later)
- `status:` — typically `in-progress`
- `sources:` — union of both pages' `sources:`, de-duplicated; order not load-bearing
- `topic:` — union if they diverge
- All other fields (`type`, `title`) stay as the retained page's originals

## Frontmatter — subsumed page (before archival)

Before moving the subsumed page to `{archive}/_agent/wiki/`, stamp its frontmatter per `wiki-supersession.md` page-level rules:

```yaml
superseded_by: <retained-page-slug>
superseded_date: YYYY-MM-DD
superseded_reason: "merged into <retained-page-slug>; content preserved"
```

And add the top-of-body callout:

```markdown
> [!warning] This page has been superseded
> See [[<retained-page-slug>]] — merged; content is now in the retained page.
```

This ensures that if a reader later pulls the archived page out of `{archive}`, the provenance is obvious.

## Archive path

Move the subsumed page to `{archive}/_agent/wiki/<slug>.md`. Confirm the directory exists before writing. **Do not delete** the subsumed page — archive-and-stamp is the canonical pattern; history is preserved even when the page no longer lives in the active wiki.

## Index update

After the merge, update `{index}`:

- Remove the subsumed page's row from its category table
- Update the retained page's `Sources` count (new union size) and `Updated` date
- Adjust the retained page's description if the merge changed its scope meaningfully
- If a category table is left empty, collapse it — but do not restructure the index beyond what the merge requires

## Log entry

A merge has no log type of its own — it folds into the `ingest` entry that executed it, per the operating contract's `{log}` format. Name the merge in that entry's artifacts:

```
## [YYYY-MM-DD HH:MM] ingest (<partner>) | <summary>; merged near-duplicate — <signal summary> → wiki: [[{wiki}/<retained>]] (updated), merged: [[{archive}/_agent/wiki/<subsumed>]]
```

`<signal summary>` is a short phrase naming what drove the merge — e.g. "slug stem + 4 shared wikilinks", "topic overlap + contradictory claims resolved". One artifact clause per pair if several merge in one run — the log is the audit trail.

## Reading list

- `vault-operating-contract.md` — three layers, the `{log}` format, the archive structure
- `wiki-supersession.md` — supersession callouts used inline and page-level during merges
- `extraction.md` — the parallel reach-the-wiki-only discipline for `vlt-extract`
