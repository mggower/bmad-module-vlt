---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — ingest a source into the wiki
need: "Ingest this: a file, a URL, a video or pasted text, into the wiki"
state: live
domain: wiki
tools: [_agent/tools/wiki/check.py]
companion: _meta/wiki.md
---
# Ingest a source

Ingest is how new knowledge enters the wiki. A source comes in; by the end its ideas are part of the wiki, connected to what was already there, and anything it changes or contradicts is shown. The question throughout is not "what does this say" but **what changes in the wiki because of this?**

The wiki's rules (page shape, the index, how a changed claim is shown) are in `_meta/wiki.md`. Read it before writing.

## Prerequisites

Something to ingest. Any of:

- **A file already in `sources/`.**
- **A URL.** Capture it first: fetch the page and save it as `sources/web/<YYYY-MM-DD>-<slug>.md`, with frontmatter `type: source`, `url:`, `captured_at:`, `title:`, and the page's readable text as the body. If the page cannot be fetched, stop and say why; do not ingest from a summary or from memory.
- **Anything a vault tool can turn into a source.** Run the tool's playbook (a video transcriber, a PDF extractor, whatever this vault has); it deposits a file in `sources/`, and ingest proceeds from that file. A vault adds a new kind of source by adding such a tool (`add-a-tool.md`). This playbook does not change.
- **Pasted text.** Save it to `sources/notes/<YYYY-MM-DD>-<slug>.md` first, with `type: source` and where it came from.
- **A research note** in `_agent/research/` that the owner has raised above `trust: draft`. It is used as it stands: skip step 5.

`sources/` is add-only. A capture or a tool writes a new file there, and **nothing edits or deletes a source afterwards**. A correction is a new source.

## Procedure

1. **Check whether it was ingested before.** Search `_agent/log.md` for the source's URL, file name or a phrase of its title. If it was, read the research note that entry links, tell the owner what a second pass would add or change, and ask: update, ingest as new, or skip. Default to update.
2. **Scan for secrets.** Before writing anything derived from the source, look for API keys, tokens, account and card numbers. If any appear, stop and tell the owner; never copy one into a note.
3. **Read the source in full.** A very long one (more than roughly 15,000 words) is read in sections, from the stored file, going back to it for each passage you will use. If you delegate the reading, the helper returns a map (sections, locations, verbatim quotes) and no interpretation; verify each quote against the stored file.
4. **Agree the emphasis.** Tell the owner the three to five most significant claims, anything surprising, and where it belongs. Ask what to emphasise or connect. Skip this when the owner has already said, or asked for it to run unattended.
5. **Write the research note**: `_agent/research/YYYY-MM-DD-HHmmss-<slug>.md`, the dated record of what this source said. Frontmatter per `_meta/frontmatter.md` (research note), with `trust: draft` and `verified_by: ingest`. Sections: Summary, Key points, Connections, Open questions, Source.
6. **Update the wiki.** Read `resources/wiki/index.md` first. For each concept the source touches, choose: update an existing page, create a page (a concept that recurs and has three or four substantial points), or leave it (a passing mention).
   - Before creating a page, list the existing ones and compare the concept, not only the name. If a page covers it, update that page.
   - If the source shows that two existing pages are really one, merge them with `consolidate.md`.
   - Where the source changes, contradicts, refines or retracts a claim, show it with the callouts in `_meta/wiki.md`. If one source contradicts several pages, say so once, as a pattern, to the owner.
   - Set `author: agent`, `trust: draft` on a new page; on any page written, `verified_by: ingest` and today's `verified_at` and `last_updated`. Add the source to `sources:`.
7. **Update the index**: a row for each new page under its category, nested under its hub; a new category when two pages need one.
8. **Run the wiki check**: `python3 _agent/tools/wiki/check.py`. Fix what it finds in the pages you wrote. Report what it finds elsewhere; do not fix that here.
9. **Record it.** One line in `_agent/log.md`:
   `## [YYYY-MM-DD HH:MM] ingest | "<source title>" → research: [[<note>]], wiki: [[<page>]] (new), [[<page>]] (updated)`
   If this ingest is the whole session, also the session note (`_meta/vault.md`, *Records*). Commit the paths written, by name.

## Output

A stored source, a research note, the wiki pages created or updated, the index, and a log entry. Tell the owner which pages are new and which changed, and anything the check found.

## Rules

- **A name that appears once in a machine transcript is not grounded.** For each proper noun from auto-generated captions or other machine transcription that would go on a page, search the wiki for it. No match and a single mention: record the claim without the name. A match whose recorded facts cannot both be true with this source: suspect the source, leave the existing page alone, record the claim without the name. In both cases write the name as the source rendered it, and where, under Open questions in the research note. This is not a contradiction and gets no contradiction callout.
- **Contradictions are kept, not smoothed.** Two credible sources that disagree are both recorded.
- **Three pages touched well beat ten touched thinly.**
- **Nothing in `_vault/`, `new/` or `daily/` is ingested unless the owner points at the file.**

## Known gaps

- The check in step 8 is structural. Nothing verifies that a page's claims match its sources; that is the owner's review, recorded by raising `trust`.
- Capturing a URL saves text only. Images, embedded video and pages behind a login are not captured.
