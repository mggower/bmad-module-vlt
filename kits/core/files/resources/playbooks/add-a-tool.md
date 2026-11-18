---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Playbook — add a tool or a playbook
need: "Add a new tool or a new playbook to the vault"
state: live
domain: vault
tools: [_agent/tools/checks/run.py]
---
# Add a tool or a playbook

A way to give the vault something new it can do. It is a short method, not a ceremony: use the steps that apply and skip the rest.

A **playbook** is a procedure a session follows. A **tool** is code a playbook runs. Most new abilities are a playbook alone. Add a tool only when there is something to compute, fetch or render that a session should not redo by hand each time.

## Procedure

1. **Say the need in one line**, in the words the owner would use to ask for it. That line becomes the playbook's `need:`. If an existing playbook already answers it (`vlt-playbook` prints the index), change that one instead.
2. **If code is needed, make the tool folder**: `_agent/tools/<name>/` with the code and a `README.md` saying what it is, how to run it and which playbooks use it. Data it keeps goes in `_agent/stores/<name>/`. A tool that produces sources (a transcript, a saved page) deposits them in `sources/`, and `ingest` takes it from there.
3. **Write the playbook** in `resources/playbooks/<name>.md`, to the shape in that folder's `README.md`. List the tool's scripts in `tools:`. Put the rules where the procedure is.
4. **If the playbook needs a new `domain:` value,** add it to the `domains:` list in `resources/playbooks/README.md`.
5. **If the work repeats on a schedule,** put the job in `_agent/schedule/` and say so under the playbook's `## Schedule`.
6. **Run the checks:** `python3 _agent/tools/checks/run.py`.
7. **If sessions will not find it from the index alone,** add the words to the `vlt-playbook` skill's `description:`.

## Rules

- No script in PARA, and no procedure in a tool's README beyond how to run it.
- A new tool does not change what an existing tool does.
