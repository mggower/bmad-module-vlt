---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbooks — procedures any session can run
domains: [vault, wiki, research]
---
# Playbooks

One flat folder, one file per procedure, no nesting by domain. Any session reads the page and runs it from the vault root. This page is the convention. The index is not written here: it is read from each file's frontmatter.

![[playbooks.base]]

The same index for a session: the `vlt-playbook` skill prints it, or run `python3 .claude/skills/vlt-playbook/index.py`.

This file is yours. Change the convention here and it is changed.

## What a playbook is

A playbook opens with a paragraph saying what the thing is. After that, each part it has sits under its own heading, with these names and in this order:

| Heading | Holds |
|---|---|
| `## Prerequisites` | Keys, auth, an environment, a file that must already exist. |
| `## Commands` | What to type, from the vault root. |
| `## Procedure` | Numbered steps, when the work is more than a command. |
| `## Output` | Where the result lands and what is committed. |
| `## Schedule` | What runs without a session, and when. |
| `## Rules` | What governs the work: the owner's rulings, refusals, things never done. |
| `## Known gaps` | What is unbuilt, unverified or deferred. |

A playbook omits a heading it has nothing for, and may add sections of its own between them.

The playbook is the one home for its own rules and paths. Nothing about a procedure is restated in a skill or in this page, so a rule is corrected in one place.

An owner's ruling stays verbatim, dated and attributed. A ruling is part of the procedure. The story of how a file got here is not: it belongs in a session note.

A playbook that outgrows one screen of procedure moves its reference material into a companion beside it, named `<playbook>-<what>.md`. The playbook is the entry point; the companion never repeats its rules.

## Frontmatter

The base keys (`type: resource`, `created`, `last_updated`, `title`), plus:

| Key | On | Value |
|---|---|---|
| `need:` | every playbook | One quoted line in the words the owner would use to ask for it. This is the index row. |
| `state:` | every playbook | `live`, or `dormant` for a procedure nobody is running now. A dormant playbook stays in this folder and opens with a one-line callout saying when it next applies or what remains undone. |
| `domain:` | every playbook | One of the values in this page's own `domains:` list. Grouping only; the folder stays flat. Add a value there when a playbook needs a new one. |
| `tools:` | a playbook with scripts | A list of what it runs, as vault paths under `_agent/tools/`: `tools: [_agent/tools/transcribe/run.py]`. |
| `companion:` | a playbook, optional | The one path it leans on outside its own page. |
| `companion_of:` | every companion | The playbook's file name. A companion carries no `need:` and no `state:`. |

`title:` reads `Playbook — <subject>` on a playbook. An edit bumps `last_updated`.

## Where the tools live

A playbook's scripts live in `_agent/tools/<name>/`, one folder per tool. The convention for that folder is `_agent/tools/README.md`. No script lives in this folder or anywhere else in PARA. Whatever a playbook runs, `tools:` is where a session looks first.

## Running one

A session that runs a playbook by hand writes one session note and one `_agent/log.md` entry, and commits path-scoped (`_meta/vault.md`, *Records*). A scheduled leg commits what it wrote and writes neither.

## Adding or changing one

A session may change a playbook that belongs to the zone it is already working in. A session that finds stale content in an unrelated playbook files a task on that zone's board, or on the vault board at `_agent/tasks/`, and leaves the body alone.

1. Write the file to the shape above.
2. Give it `need:`, `state:`, `domain:` and, if it has scripts, `tools:`. A companion gets `companion_of:` instead.
3. Run `python3 .claude/skills/vlt-playbook/index.py --check`. It fails on a file with no index keys, an unknown domain, a `tools:` path that does not exist or is outside `_agent/tools/`, or a companion whose playbook is missing.
4. If the playbook answers a kind of request the `vlt-playbook` skill's `description:` does not name, add the words there. That line is how a session decides to open the skill at all, and it is the one thing the frontmatter cannot generate.

Adding a tool with its playbook: `add-a-tool.md`.
