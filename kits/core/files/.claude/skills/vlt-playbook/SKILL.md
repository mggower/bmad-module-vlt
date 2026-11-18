---
name: vlt-playbook
description: Use when asked to run, refresh, render or locate a standing vault procedure, to add a tool or a playbook, to set up a zone or tend a task board, and before improvising any multi-step vault task by hand, to check whether a playbook already covers it.
---

# Playbooks

A procedure any session can run is a playbook in `resources/playbooks/`. **The playbook is the authority: its rules, paths and schedule live in it and nowhere else.** Find the row, read that file whole, then run it from the vault root.

!`python3 "${CLAUDE_SKILL_DIR}/index.py"`

That command prints the need → playbook table from each playbook's `need:` frontmatter. If it fails, list `resources/playbooks/` and read the `need:` lines.

No row fits: say so and ask before improvising. Do not stretch a neighbouring playbook over a different job.

**Changing or adding a playbook:** the convention is `resources/playbooks/README.md`.
