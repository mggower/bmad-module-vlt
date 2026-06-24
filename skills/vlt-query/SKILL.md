---
name: vlt-query
description: Answer a question by synthesizing from the vault wiki. Use when the user asks something the wiki might speak to — 'what do I know about X', 'what have I read on Y', 'what's my current thinking on Z', or wants a comparison/synthesis/decision-support grounded in their own curated sources. Reads the wiki only (no web — for that, use vlt-research).
---

# vlt-query

## Overview

A query is not just a lookup — it synthesizes knowledge built up over time and, when the answer is valuable, files it back so the wiki compounds. What sets it apart from a normal chat answer: **it is grounded in sources the user curated.** Every significant claim cites a wiki page or research note; anything from general knowledge is marked as such. vlt-query reads the wiki only — it never reaches the web. Runs interactively or headless ("what do I know about X").

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

The vault is this project — resolve paths relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). Logical names this skill uses (default, relative to the project root): `index` → `_agent/wiki/index.md`, `wiki` → `_agent/wiki/`, `research` → `_agent/research/`, `log` → `_agent/log.md`, `conventions` → `_meta/conventions/`. Below, `{index}` etc. mean the resolved path. Note the **active partner** for the log tag, used only if the answer is filed.

## Step 1: Read the index

Read `{index}` first — it maps the wiki. Identify the pages directly relevant, the pages with adjacent context, and whether the question falls outside what's been ingested.

If the index shows nothing relevant, **say so plainly** rather than padding with general knowledge: "The vault doesn't have much on this yet — here's what I can say from general knowledge, but to build it up properly, run `vlt-research` on [X] or ingest a source." Don't pretend the wiki has what it doesn't.

## Step 2: Read the relevant pages

Read the identified `{wiki}` pages, and any related `{research}` notes they link to when those matter. Prefer wiki pages for synthesis — they're the distilled multi-source view; research notes are for specific source details, exact quotes, or tracing a claim's origin.

## Step 3: Synthesize and respond

Answer the question directly, and:

- **Tag provenance on every claim.** A claim grounded in the vault cites the exact page: "According to `[[llm-context-windows]]`, …". A claim from general knowledge is marked inline as such ("— general knowledge, not in the vault"). The reader should never have to guess which is which.
- **Rank contradictions, don't bury them.** When pages disagree on something relevant, name the disagreement and order the views by support — more recent (`last_updated`) and more sources first — rather than silently picking a winner. Surfacing the tension is more useful than a false consensus.
- **Flag the edges** — where the vault's knowledge is incomplete or uncertain.
- **Fit the format to the question.** A factual lookup → a concise prose answer with citations. A comparison → a markdown table with a short prose summary. A decision-support or complex analytical question → headed sections.

## Step 4: Decide whether to file

File the answer back when it earns persistence — use the rubric, not a gut call:

- **File** if the synthesis connects **≥3 pages**, the question is likely to recur, or the answer contains conclusions not already in any single page (or the user asks to save it).
- **Don't file** a single-page lookup or a one-liner — just answer in chat.

When filing:

- **A one-off investigation answer** → write a `{research}/YYYY-MM-DD-HHmmss-<slug>.md` note directly. Frontmatter per `{conventions}/frontmatter.md`: `type: research`, `created`, `title`, `author: agent`, `trust: raw`, `topic`, `status: complete`, `sources:` (the pages/notes consulted) — **no `key:`**.
- **A synthesis that belongs as a canonical wiki page** → **hand it to the Librarian** (`vlt-ingest` is the single writer of canonical pages). Propose the page and the claims; do not write or edit the wiki page here.
- Append a partner-tagged entry to `{log}`:

  ```
  ## [YYYY-MM-DD HH:MM] query (<partner>) | "<question summary>" → [[<research-note>]]
  ```

  Write **no** session note — the summoning partner owns the session log (operating contract § session-ownership).

## Tips

- **Cite specifically** — link the exact page, never "the wiki says…".
- **An empty vault is a finding.** Be direct when the wiki is thin and name the source that would fill the gap; that beats a vague answer padded with general knowledge.
- **Filing compounds value** — a non-trivial answer filed today makes the next related question easier. Treat the rubric's threshold as the default, not the exception.
