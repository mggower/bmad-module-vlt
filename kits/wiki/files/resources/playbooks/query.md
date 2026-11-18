---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — answer a question from the wiki
need: "What do I know about X: answer a question from the wiki"
state: live
domain: wiki
companion: _meta/wiki.md
---
# Answer a question from the wiki

A query answers from what the owner has curated, not from general knowledge. Every significant claim names the page it came from. It reads the vault only; a question the vault cannot answer is a job for `research.md` or a source to ingest.

## Procedure

1. **Read `resources/wiki/index.md`.** Pick the pages that bear on the question and the ones with nearby context. If nothing does, say so plainly: "the vault has little on this". You may add what you know from general knowledge, marked as that, and name the source or research that would fill the gap.
2. **Read those pages**, and a research note they cite when you need a detail, a quote or a claim's origin.
3. **Answer.**
   - Cite the exact page for each claim: "According to [[page]], …". Mark anything from general knowledge inline as "general knowledge, not in the vault".
   - Where pages disagree, say so and order the views by support (more recent, more sources). Do not pick one quietly.
   - Say where the vault's knowledge is thin or uncertain.
   - Fit the form to the question: prose for a lookup, a table for a comparison, headed sections for an analysis.
4. **Decide whether to keep the answer.** Keep it when it connects three or more pages, when the question will come back, when it reaches a conclusion no single page states, or when the owner asks. A single-page lookup is answered and not kept.

## Output

- **Not kept:** the answer, in the conversation. No note, no log entry.
- **Kept as an investigation:** a research note, `_agent/research/YYYY-MM-DD-HHmmss-<slug>.md`, with `trust: draft`, `verified_by: query` and the pages consulted in `sources:`.
- **Kept as reference the owner will use:** a document in the zone the owner names, written under that zone's README. Set `review: requested` if the zone or the owner asks for review.
- **It belongs in the wiki:** do not write the page. A kept research note can be ingested once the owner has raised its trust (`ingest.md`); otherwise file a task on the vault board.
- When something was kept, one line in `_agent/log.md`: `## [YYYY-MM-DD HH:MM] query | "<question>" → [[<note>]]`, and a path-scoped commit.

## Rules

- Never write or edit a wiki page from a query.
- Never present general knowledge as the vault's.
- An empty answer is a finding. Say what is missing.
