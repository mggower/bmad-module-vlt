---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — task boards as a base over task files
need: "Tend a task board: add a task, set a task's status, see what is open in a zone or in the vault"
state: live
domain: vault
companion: resources/playbooks/set-up-a-zone.md
---
# Task boards

A task board is a folder of task files, `<zone>/tasks/`, and one base beside it, `<zone>/tasks.base`, that shows them. Every piece of open work scoped to the zone is one file in that folder. The file's `status:` is the only record of where the task stands, and the base groups and filters on it. It answers "what is open here, and whose move is it?" from one page.

The vault has a board of its own at `_agent/tasks/` with `_agent/tasks.base`, for work no zone owns: something the vault itself should become, a wiki change someone noticed, a stale playbook. It works the same way; its prefix is `VLT`.

Setting up a board in a new zone is `set-up-a-zone.md`.

## Prerequisites

- Obsidian's Bases core plugin is on.
- For the owner's **New** button: Templater is on, with *Trigger Templater on new file creation* enabled and a folder template that maps `<zone>/tasks` to `_agent/templates/zone-task.md`. Sessions do not use Templater.
- The zone's `README.md` allows the session to write there.

## What goes where

| Kind of thing | Home |
|---|---|
| Work scoped to one zone: build this, fix this, decide this | A task file in the zone's `tasks/` |
| Work on the vault itself, with no zone to own it | A task file in `_agent/tasks/` |
| What a brainstorm or a design decided, and why | A document in the zone. It does not track progress |
| The plan for building a design | Task files, one for each step that can be finished on its own |

A task file cites the design it builds in `grounding:` and carries the progress.

## Task files

`<zone>/tasks/<KEY>-<slug>.md`: the key, then a kebab-case slug named for the outcome (`GD-010-raised-bed-plan.md`). No date prefix. One flat folder. Every task is a file, however small.

**The key** is the zone's prefix and a three-digit number: `GD-010`. It is the task's name in a commit message, a log entry or conversation. It sits in the file name and in `key:`, and it makes the file name unique in the vault, so a link to a task is the bare file name. The prefix is the zone README's `task_prefix:`: two or three capitals, never shared between zones. A new task takes the highest number in the folder plus one. A number is never reused, including a dropped task's.

```markdown
---
type: record
created: 2026-11-06
last_updated: 2026-11-06
title: "Task — Plan the raised beds"
key: GD-010
status: ready
summary: "Plan the raised beds"
sub: beds
theme: spring-layout
grounding:
  - areas/garden/design/2026-11-05-layout.md
---
# Plan the raised beds

One paragraph: what is wanted and why.

## Done when

- A checkable statement.

## 2026-11-06

(session) Filed after the layout design was agreed.
```

The file opens with what is wanted, then `## Done when`, then dated entries, newest last, each attributed `(session)` or `(owner)`. A ruling is quoted verbatim with its date. A task that needs a long plan holds it in its own body under `## Plan`, before the dated entries.

**The task keys**, beyond the base keys in `_meta/frontmatter.md`:

| Key | Holds | Required |
|---|---|---|
| `key` | The task key | Yes |
| `status` | One value from the table below | Yes |
| `summary` | One line saying what the task is. It is the `Task` column, and the owner edits it in the table | Yes |
| `sub` | The sub-area: one of the zone README's `subs:`, or `area` for the whole zone | Yes |
| `theme` | One slug from the zone README's theme table: the design or workstream the task belongs to | No |
| `owner` | `owner` when the next move is something only the owner can do | No |
| `priority` | A number; lower sorts first within a status | No |
| `due` | A date the task waits for or is wanted by. Only when a real date exists; a dated entry says where it comes from | No |
| `done_on` | The date it was finished | When `done` |
| `sessions` | Wikilinks to the session notes of the sessions that worked it, oldest first | When a session worked it |
| `related` | Wikilinks to other tasks this one depends on or came out of | No |
| `grounding` | Paths to the documents the task builds from | No |

**Status.** One value, always present:

| `status` | The task is here when | Who sets it |
|---|---|---|
| `idea` | It is a candidate with no requirements yet. | Anyone |
| `needs-ruling` | It cannot move until the owner decides or does something. The body states the question. | Anyone; only the owner's ruling moves it on |
| `ready` | It is decided, and a session could start it. | Anyone, from a ruling or a design |
| `in-progress` | Work has started and is not finished. It does not mean a session is on it now. | The session that starts it |
| `done` | The `Done when` list is met. | The session that finishes it |
| `parked` | The owner does not want to delete it and does not want it prioritised now. | Only on the owner's word |
| `dropped` | It was decided against. The file and the key stay. | Only on the owner's word |

**Theme.** `theme:` ties together the tasks that build or follow from one design or workstream, so the base shows them as a group, finished and open together. Check the zone README's theme table before writing a slug, so one theme does not get two spellings. A new theme adds its row there in the same commit as its first task.

## The base

`<zone>/tasks.base` filters to `<zone>/tasks` and has these views:

| View | Shows |
|---|---|
| `Board` | Open tasks grouped by status: Ideas, Needs ruling, Ready, In progress. No `parked`, `done` or `dropped`. |
| `My move` | `needs-ruling` tasks and tasks with `owner: owner`. |
| `By sub` | Open tasks grouped by `sub`. |
| `By theme` | Every task grouped by `theme`, finished ones included. |
| `Backlog` | `parked` tasks. |
| `Done` | `done` tasks, newest first. |
| `By status (plain)` | Every task, grouped on the raw `status` value. |

The Key column is the link to the file. The group order comes from the `lane` formula, which prefixes each status with a number; a new status value needs a branch there or it shows under `0 · No status`.

## Procedure

**Add a task (a session).**

1. List the `tasks/` folder and take the highest number plus one.
2. Write the file with every required key, and `theme:` if it belongs to one. A task nobody has shaped yet is `idea`; one that waits on the owner is `needs-ruling` and states the question.
3. Before committing, list the folder again to confirm no other session took the same number.

**Add a task (the owner).** Press **New** on the base. The template asks for a title and a sub-area, takes the next key, renames the file and fills the frontmatter with `status: idea`.

**Work a task.**

1. When work starts, set `status: in-progress`. This is the first edit of the session, before any other work.
2. Append a dated entry for anything a later session would need.
3. At the end, add the session note to `sessions:` as a wikilink and bump `last_updated`.
4. When the `Done when` list is met, set `status: done` and `done_on:`. If the work is unfinished, the status stays `in-progress` and the last dated entry says what is next.

**Work found while working a task.** If it falls inside the current task's `Done when`, it is a dated entry on that task. If not, it is a new task with the current one in `related:` and the same `theme:`.

**Park, drop or bring back a task.** Only the owner decides. Set the status and add a dated entry quoting the ruling.

**Turn a plan document into tasks.** Leave the document where it is. Write one task for each step still open, with the document in `grounding:`, and add a line at the top of the plan saying its open steps are on the board.

## Output

Task files, committed by path. A session that only changes a task for work it did records that in its own log entry.

## Rules

- `status:` in the task file is the only status. No list, and no status word in a title or a summary.
- Every task is a file with a key. A key is unique in its zone and never reused. Two sessions can take the same number without git noticing, because the slugs differ; the session that finds a duplicate renumbers the newer file and fixes the links to it.
- A piece of work lives in one place: one task, on one board.
- A session changes a task's status only for work it did or a ruling the owner gave. The owner changes any task at any time, and a session takes the board as it finds it.
- A task leaves `needs-ruling` only on the owner's ruling, quoted in the file.
- A task becomes or stops being `parked` or `dropped` only on the owner's word, and a session does not pick up a `parked` task.
- Finished and dropped task files stay in `tasks/`. They are the record of what was built and what was decided against.

## Known gaps

- The Templater trigger is vault-wide. With it on, Templater runs template commands in any new file, including one a session writes, so a note that quotes Templater syntax can be executed.
- There is no drag between statuses and no manual order. Status changes by editing the cell; order within a status comes from `priority`, then the key.
- Nothing checks a task file's keys. A file with no `status:` shows on `Board` under `0 · No status`.
- `done` tasks accumulate in `tasks/` without limit.
