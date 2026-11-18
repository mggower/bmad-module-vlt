---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Tools — where scripts live
---
# Tools

Every script in the vault lives here, in `_agent/tools/<name>/`. One folder per tool, flat. No script lives in PARA.

## A tool folder

- **A `README.md`**, saying what the tool is, how to run it, and which playbooks use it.
- **The code.** A tool with many scripts (an engine) is still one folder, with its own sub-folders inside.
- **Its tests**, beside the code.
- **Optionally a `check.py`**, run by `_agent/tools/checks/run.py` (see `checks/README.md`).

What a tool folder does not hold:

- **Data.** A database, snapshots and derived files live in `_agent/stores/<name>/`.
- **Output a person reads.** That goes to the PARA zone it belongs to, or to `sources/` when the tool produces a source (a transcript, a saved page).
- **The procedure.** How and when to run the tool, and its rules, are a playbook in `resources/playbooks/`. The playbook's `tools:` list names the scripts.

## Scheduled legs

A job that runs without a session lives in `_agent/schedule/` and calls into a tool folder. It commits what it wrote, and writes no session note and no log entry.

## Adding one

`resources/playbooks/add-a-tool.md`.
