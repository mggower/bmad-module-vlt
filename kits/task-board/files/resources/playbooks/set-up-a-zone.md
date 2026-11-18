---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — set up a zone and its task board
need: "Set up a new zone (a project, area or resource) with its README and task board, or add a board to a zone that has none"
state: live
domain: vault
companion: resources/playbooks/task-board.md
---
# Set up a zone

A zone is a PARA container the owner works in: a folder under `projects/`, `areas/` or `resources/`, with three things in it:

- a `README.md` saying what the zone is, who may write there, and its sub-areas and themes;
- a `tasks/` folder, one file per piece of work;
- a `tasks.base` that shows them.

Zones often relate to each other. A task that touches two zones lives in the one that owns the outcome and links the other in `related:` or `grounding:`.

## Prerequisites

- The owner has named the zone and its kind (project, area or resource).
- The templates are in `_agent/templates/`: `zone-readme.md`, `tasks.base`, `zone-task.md`.

## Procedure

1. **Choose the prefix**: two or three capitals for the zone's task keys. Search the vault's zone READMEs for `task_prefix:` and take one that is not used. `VLT` is the vault board's.
2. **Create the folder** if it does not exist, and `tasks/` inside it.
3. **Write `README.md`** from `_agent/templates/zone-readme.md`: the kind, the title, `task_prefix:`, the zone's `subs:` (keep `area`, for the whole zone), and the paragraph on what the zone is for. Add `writers: owner` or `review_default: requested` only if the owner asks. If the zone already has a README, add the keys and the board's row to it; do not replace it.
4. **Copy `_agent/templates/tasks.base` to `<zone>/tasks.base`** and replace `ZONE_TASKS_FOLDER` with the zone's task folder path (`areas/garden/tasks`). It appears once.
5. **If the zone already has open work**, read its documents and any tasks on the vault board that belong to it, and write one task file for each open item (`task-board.md`, *Add a task*). The status comes from what the source says; an item whose state is unclear is `needs-ruling` with the question. A task moved from the vault board is marked `dropped` there with a dated entry naming its new key.
6. **Ask the owner to add the Templater folder template** mapping `<zone>/tasks` to `_agent/templates/zone-task.md`, if they want the **New** button.
7. **Check**: open `<zone>/tasks.base` in Obsidian and confirm the `Board` view groups in order. Run `grep -c ZONE_TASKS_FOLDER <zone>/tasks.base`; it prints 0.

## Output

`<zone>/README.md`, `<zone>/tasks/`, `<zone>/tasks.base`, and any task files written. Commit by path, with the session note and log entry (`_meta/vault.md`, *Records*).

## Rules

- A prefix is never shared between zones and never changed once tasks carry it.
- A zone's README is the owner's to shape. A session adds what this playbook needs and leaves the rest.
