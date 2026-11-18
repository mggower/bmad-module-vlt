---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — correct or retire a wiki claim or page
need: "This wiki claim is wrong or out of date: correct it, mark it stale, or retire the page"
state: live
domain: wiki
tools: [_agent/tools/wiki/check.py]
companion: _meta/wiki.md
---
# Correct or retire a wiki claim or page

Use this when a claim on a wiki page must change and no new source is being ingested: a task on the vault board says a page is wrong, the owner corrects something, a claim has gone stale, or a page has been replaced by another. When a new source is what drives the change, run `ingest.md` instead; it applies the same callouts.

The callout shapes and the page-level keys are in `_meta/wiki.md`, *When a claim changes*. They are not repeated here.

## Prerequisites

- The page, and what is wrong with it.
- **What the change rests on**: a file in `sources/`, a research note, or the owner's own statement in this session. A change with nothing behind it is not made. If the evidence is on the web, store it first (`ingest.md`, *Prerequisites*).

## Procedure

1. **Read the page and what the change rests on.**
2. **Choose the kind of change:**
   - a claim is replaced: write the new claim in the body and the `[!superseded]` callout after it, with the reason (`updated`, `contradicted`, `refined`, `retracted`);
   - a claim is doubtful and nothing replaces it: the `[!stale]` callout;
   - two credible sources disagree: the `[!contradiction]` callout on both pages, with its disposition; an `adjudicable` one gets a task on the vault board;
   - the whole page is replaced: the three `superseded_*` keys and the top callout on the old page, `git mv` it to `_agent/archive/resources/wiki/`, remove its index row, and repoint the pages that linked to it.
3. **Attest.** On each page changed: `verified_by: supersede`, today's `verified_at` and `last_updated`. Add what the change rests on to `sources:`; the owner's statement is cited as the session note.
4. **Run the wiki check**: `python3 _agent/tools/wiki/check.py`.
5. **Record it**: one line in `_agent/log.md`, `## [YYYY-MM-DD HH:MM] supersede | <what changed and why> → [[<page>]]`; close the task that asked for it; commit the paths written.

## Rules

- Nothing is overwritten silently and nothing is deleted.
- No winner is picked between two credible sources.
- A formatting fix, a link fix or an addition needs no callout.
