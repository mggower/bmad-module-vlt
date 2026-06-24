---
type: note
created: 2026-06-06
last_updated: 2026-06-23
title: Wiki Index Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 2
consumers: [vlt-ingest, vlt-lint]
---

# Wiki Index Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/wiki-index.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

The `{index}` (`_agent/wiki/index.md` by default) is the **agent's structural map** of the wiki layer — read first on every activation and before any ingest or query. It answers "what concepts exist, how do they cluster, and where does new knowledge belong." This file defines its structure so it is governed by a written spec rather than one writer's mimicry: `vlt-ingest` writes it against this convention and `vlt-lint` validates it against this convention. (Paths use the structure-map logical names — see the operating contract.)

## What the index is — and is not

The index is **a map, not a catalog.** This is a deliberate division of labor:

- **Per-page descriptions** live in each page's `summary:` frontmatter — the single source of truth (see `frontmatter.md`). The human scans these through **Obsidian Bases** (dynamic tables over frontmatter: `title`, `summary`, `topic`, `status`, `trust`, `sources`, `last_updated`). The index does **not** repeat them.
- **Chronology** — when each page was touched and by what operation — lives in the `{log}` (the canonical chronological record per the operating contract). The index carries **no changelog**.
- **Anything derivable from frontmatter** — source counts (`len(sources:)`), update dates (`last_updated`) — is **not** hand-maintained in the index. Bases derives it live; duplicating it here only invites drift.

What remains — and what only the index provides — is **structure**: which pages exist, how they cluster into subject areas, the hub→entity relationships within a cluster, cross-cluster links, and filing guidance for where new knowledge lands. That is the index's whole job.

## Index frontmatter

```yaml
---
type: index
created: YYYY-MM-DD              # immutable
last_updated: YYYY-MM-DD         # bumped on every structural change to the index
title: Wiki Index
---
```

No `author`/`trust` — it is a generated map, not a knowledge artifact. `last_updated` bumps when the index's **structure** changes (a page added/removed, a category split/renamed, a hub relationship redrawn) — *not* when a page's count or date changes (those aren't in the index). It is what `vlt-lint` reads to judge index staleness.

## Category model

Pages are grouped under `##` (H2) subject-area headings. Categories are **emergent, not fixed**:

- A category earns a heading once it holds **two or more** related pages; a lone page sits under the closest existing category or waits.
- Heading names are short subject areas in Title Case, not questions or sentences.
- Order categories most- to least-developed (or by a stable domain order the user prefers); order pages within a category by structure first (hub before its entities), then alphabetically by slug.
- `vlt-ingest` adjusts categories as the wiki grows; splitting or renaming a category is a normal index edit, not a supersession event.

**The `category:` binding.** The index H2 set is the **controlled vocabulary** for the wiki page `category:` frontmatter field (see `frontmatter.md`). The binding is strict and bidirectional:

- Every wiki page's `category:` value **must be an existing index H2** — the index is the single source of truth for the vocabulary, the page's `category:` is a projection of it into frontmatter (so Obsidian Bases can group by it; the index is Markdown the agent reads, `category:` is the form Bases reads — same vocabulary, two representations).
- Renaming or merging an index H2 therefore means **rewriting the `category:` of every page under it** in the same edit — the two cannot drift. `vlt-lint` validates the binding (a `category:` matching no H2, or a wiki page missing `category:`, is a finding).
- The index keeps finer structure *within* a category (italic sub-groups, hub→entity nesting) that `category:` does not capture — that finer distinction lives in each page's `topic:` list. So a category may be broad (one Bases group) while the index still clusters its pages richly for filing.

## Row format — structure, not description

Each page is one list item: its wikilink, optionally a terse **structural tag**. **No description, no source count, no date.**

```markdown
## Coffee Brewing
- [[extraction-methods]] · hub — how grind, time, and pressure shape a cup, split by speed
  - [[cold-brew]] · slow
  - [[espresso]] · fast
```

- **`[[page-slug]]`** — the page's wikilink (resolves to the canonical page). No double-quoting (this is body text, not frontmatter).
- **structural tag** (optional, after `·`) — names the page's *role in the cluster*, not its content: `hub`, or a one- or two-word axis label that captures **why the entities are organized the way they are** (e.g. `slow`/`fast`, `hub`, `counterpart to [[french-press]]`). If a tag would just restate the page's `summary:`, omit it — the summary already says that.
- **nesting** — entity pages that hang off a hub are indented under it; this hierarchy *is* the structural information the index uniquely holds. Flat categories (no hub) are a flat list of slugs.
- A short prose **filing note** may follow a category when it helps future ingests land knowledge correctly (e.g. "new brew methods → attach to the hub or seed a sibling entity"). Keep it to a line or two.

## The Stubs section

A page may link to a concept with no page yet. Catalog these under a trailing section so the gap is visible:

```markdown
## Stubs (linked, not yet written)

- `slug` — <what it is / why it's linked>; <status, e.g. awaiting a source>.
```

- The stub identifier is a **backtick-wrapped slug**, not a `[[wikilink]]` (nothing to resolve yet).
- When a stub becomes a real page, it **moves** into its subject category in the row format above.
- `vlt-lint` may surface long-dangling stubs but never auto-creates a page.

## Writer / validator contract

| Role | Skill | Obligation |
| --- | --- | --- |
| **Writer** | `vlt-ingest` | Place each new/affected page in the right category, nested under its hub if it has one; add the optional structural tag; create/adjust categories and hub groupings as the wiki grows; move a stub to a category when its page is created; bump the index `last_updated`. Set the page's own `summary:`, `category:` (= the page's index H2), and `topic:` list (the description and tags live on the page, not in the index). When renaming/merging a category, rewrite the `category:` of every affected page in the same edit. Does **not** maintain counts or dates in the index. |
| **Validator** | `vlt-lint` (index-drift) | Check every index row's link resolves; surface pages on disk missing an index row (orphans) and rows with no page on disk (dangling); surface long-dangling stubs. Check every wiki page carries a `summary:` within the 160-char limit (flag missing or over-length); check every wiki page's `category:` exists and matches an index H2, and that `topic:` is a list (per `frontmatter.md`). Does **not** police source counts or dates in the index — they are not there to police. |

Because both the writer and the validator point here, the index has exactly one structural definition.

## Reading list

- `vault-operating-contract.md` — the operating constitution (activation read order, structure map, the `{log}` as canonical chronology)
- `frontmatter.md` — the frontmatter single source of truth (`type: index`, `summary:`, `created`/`last_updated`, `sources:`)
- `wiki-supersession.md` — how page-level supersession interacts with index rows
