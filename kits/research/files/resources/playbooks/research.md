---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — research a question and file a research note
need: "Research X: investigate a question on the web and file a research note"
state: live
domain: research
---
# Research a question

Research goes out to the web to build knowledge the vault does not hold, and files the result as one research note in `_agent/research/`. The note is the deliverable. Any session may run this. It never writes the wiki: a note reaches the wiki only through `ingest.md`.

## Prerequisites

- Web access, through whatever the vault's `CLAUDE.md` or the owner's setup prescribes. If the prescribed tool is unavailable, say so before using another.
- A question. A topic is not yet a question.

## Procedure

1. **Sharpen the brief**, in two or three exchanges, asking only what is not already clear:
   - the precise question, in a form that could title the note;
   - the angle (practical or theoretical, current or historical, the decision it informs);
   - the depth: *quick orientation* (3 to 5 sources), *moderate* (5 to 8, the main positions), or *deep dive* (8 to 15 or more, primary and dissenting sources);
   - any starting links, papers or people.
   Skip what the owner has already given. If the question cannot be answered from the open web at that depth (too broad, sources out of reach, no stable answer), propose a tighter one before spending effort.
2. **Check the vault first.** Read `resources/wiki/index.md`, the relevant pages and any research note on the subject. Tell the owner briefly what is already held and what this will add.
3. **Research**, to the agreed depth. Synthesise across sources; do not report them one by one. Note where they agree, disagree or hedge. Flag anything that updates or contradicts a wiki page.
   For a long dive, keep `_agent/research/YYYY-MM-DD-HHmmss-<slug>.WIP.md` (progress, sources so far, open threads) so an interruption loses nothing. Remove it when the note is written.
4. **Write the note**: `_agent/research/YYYY-MM-DD-HHmmss-<slug>.md`, the slug taken from the question. Frontmatter per `_meta/frontmatter.md` (research note): `author: agent`, `trust: draft`, `verified_by: research`, `verified_at` today, every source consulted in `sources:`. Sections:
   - **Research question**: one or two sentences; this defines done.
   - **Scope and approach**: depth, angle, what was left out.
   - **Summary**: three to five specific sentences: the answer, the most important finding, the biggest caveat. Written last, placed first.
   - **Findings**: by theme or sub-question, never by source.
   - **Open questions**: what is uncertain or contested, naming the tension.
   - **Sources**: every URL used, each with a line on what it contributed.
5. **Check the note**: every claim in Findings has a source in Sources; no secret or token copied from a page; frontmatter complete.
6. **Record it**: one line in `_agent/log.md`, `## [YYYY-MM-DD HH:MM] research | "<question>" → [[<note>]]`; if this is the whole session, the session note; commit the paths written.
7. **Offer the wiki pass.** Ask whether the findings should go into the wiki now, or after the owner has read the note. If yes, run `ingest.md` with the note as its source.

## Output

One research note, a log entry, and a report to the owner: the headline finding, where the note is, and anything left unverified.

## Rules

- A research note is written once. A correction is a new note.
- Disagreement between sources is a finding. Do not average it away.
- The wiki is never edited here.
