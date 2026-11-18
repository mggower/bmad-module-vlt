---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: The vault's rules
---
# The vault's rules

These are the rules every session works under, whatever it is doing. The file is the vault's own: change a rule here and it is changed. Keep it to two pages. A rule that belongs to one procedure lives in that procedure's playbook, not here.

The vault is an Obsidian-style Markdown vault: `[[wikilinks]]`, `> [!callout]` blocks, YAML frontmatter.

## Write boundaries

| Place | Who writes |
|---|---|
| `projects/`, `areas/`, `resources/` | Any session, and the owner. A zone's `README.md` may restrict writers; read it before writing in a zone. |
| `resources/wiki/` | Only a session running a wiki playbook (`ingest`, `supersede`, `consolidate`), under `_meta/wiki.md`. |
| `sources/` | Add-only. A session or a tool may deposit a new source. Nothing edits or deletes a source afterwards. |
| `_agent/`, `_meta/`, `.claude/` | Any session. |
| `_vault/`, `new/`, `daily/` | The owner only. Read a file there when the owner asks; never write, tidy, triage or ingest from there unasked. |

Three rules sit on top of the table:

- **A wiki change you are not making through a wiki playbook is a task.** File it on the vault board (`_agent/tasks/`), or write a research note. Do not edit the page.
- **A Map of Content is never edited by a session.** Its links are the owner's curation. A MOC is any note with `type: moc`.
- **Nothing is deleted.** A file that is retired moves with `git mv` into `_agent/archive/`, keeping its path under that folder.

## Records

A session that changes the vault by hand leaves three things:

1. **One session note** in `_agent/sessions/`, named `YYYY-MM-DD-HHmmss-<slug>.md`: what was asked, what was done, what was decided and by whom, what is left open.
2. **One entry in `_agent/log.md`**, appended, one line:
   `## [YYYY-MM-DD HH:MM] <type> | <summary> → <the notes written>`
   `<type>` is a short lowercase word for the work (`session`, `ingest`, `query`, `research`, or a playbook's own). Older entries carry a name in parentheses after the type; anything reading the log tolerates both shapes.
3. **Path-scoped commits.** Commit only the paths the session wrote, by name. Never `git add -A`.

A scheduled leg (a job with no session) commits what it wrote and writes neither a note nor a log entry.

Open work goes on a task board, not into a note: the zone's `tasks/` for work scoped to a zone, `_agent/tasks/` for the vault itself (`resources/playbooks/task-board.md`).

## Naming and links

- **Folders and files:** lowercase kebab-case.
- **Session notes and research notes:** datetime-prefixed, `YYYY-MM-DD-HHmmss-<slug>.md`. They are written once; a correction is a new note.
- **Wiki pages and playbooks:** no date prefix. Their name is their identity.
- **Links:** `[[wikilinks]]` in body text, freely. A wikilink inside frontmatter is double-quoted. A wikilink inside backticks does not resolve; use backticks only when you mean the literal text.
- **Frontmatter** is flat (no nested maps) and its schemas are in `_meta/frontmatter.md`.

## Honest reporting and grounding

- **A count states what it ran against and what it cannot see.** A bare zero reads the same as "never ran" and "cannot detect this". Give the denominator and the blind spot with the number.
- **Report what was measured, in those words.** If the signal is a stand-in for the thing claimed, say so beside the finding, or narrow the claim to what the signal shows.
- **Say what was not done.** A skipped step, a failed command or an unverified claim is reported as that, with the output.
- **One mention in a machine transcript does not ground a name.** A proper noun that appears once in auto-generated captions or other machine transcription, and collides with what the vault already records, is suspect: keep the claim, leave the name out, and say what would settle it.
- **Trust is the owner's to raise.** A session writes `trust: draft`. Only the owner moves a note up the ladder.

## Where things live

| What | Where |
|---|---|
| Procedures a session runs | `resources/playbooks/`, one file each. The convention is its `README.md`; the `vlt-playbook` skill prints the index. |
| Scripts | `_agent/tools/<name>/`, one folder per tool. The convention is `_agent/tools/README.md`. |
| A tool's data | `_agent/stores/<name>/` |
| Scheduled jobs | `_agent/schedule/` |
| Task boards | `<zone>/tasks/` and `<zone>/tasks.base`; the vault's own at `_agent/tasks/` |
| Session notes, the log | `_agent/sessions/`, `_agent/log.md` |
| Research notes | `_agent/research/` |
| The wiki and its rules | `resources/wiki/`, `_meta/wiki.md` |
| Frontmatter schemas | `_meta/frontmatter.md` |
| Checks | `python3 _agent/tools/checks/run.py` |
| Retired files | `_agent/archive/` |
| What was seeded from the vlt kits | `_agent/kits.lock` (pull changes with `vlt-pull`) |
