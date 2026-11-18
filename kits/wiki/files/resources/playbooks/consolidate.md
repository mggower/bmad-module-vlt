---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — merge wiki pages that have become one
need: "These wiki pages overlap: find duplicates, or merge two pages into one"
state: live
domain: wiki
tools: [_agent/tools/wiki/check.py]
companion: _meta/wiki.md
---
# Merge wiki pages that have become one

The wiki works only if each concept has one page. Pages drift into overlap: near-duplicates, a topic split in two, an ingest that made a parallel page. This playbook merges them and keeps the history. It reads and writes the wiki only; no new source is processed.

Merging is a judgment. Two pages that differ by a single adjective, or by what a reader wants from them, are distinct and stay apart.

## Procedure

1. **Find candidates** (skip when the owner names the pair). Three signals, shown side by side for each pair:
   - names that share a leading word or main noun;
   - pages that link to three or more of the same pages;
   - `topic:` lists that overlap.
   Show the owner a ranked table. Propose nothing further until they confirm a pair.
2. **Choose which page stays.** In order: more sources; the wider, more general name; more links pointing at it; more recently updated. Confirm the direction with the owner before writing.
3. **Merge into the page that stays.**
   - Material only the other page has is woven in, with no callout.
   - The same fact in both becomes one.
   - Claims that conflict get the `[!superseded]` callout (`_meta/wiki.md`), reason `contradicted` or `refined`. No winner is picked silently.
   - Frontmatter: `created` unchanged; `last_updated` today; `sources:` and `topic:` the union of both; `trust` unchanged; `verified_by: consolidate`, `verified_at` today.
4. **Retire the other page.** Add the three `superseded_*` keys and the top callout (`_meta/wiki.md`), with the reason "merged into <page>; content preserved". `git mv` it to `_agent/archive/resources/wiki/`. Do not delete it.
5. **Repoint links** to the retired page in the rest of the wiki.
6. **Update the index**: remove the retired page's row; if a category is left with nothing, remove the heading. Change nothing else.
7. **Run the wiki check**: `python3 _agent/tools/wiki/check.py`.
8. **Record it**: one line in `_agent/log.md`, `## [YYYY-MM-DD HH:MM] consolidate | merged <signals> → [[<kept>]], archived: <path>`; commit the paths written.

## Rules

- Never merge without the owner's confirmation of the pair and the direction.
- One log clause for each pair merged.
