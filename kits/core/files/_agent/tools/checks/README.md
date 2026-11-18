---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Tool — checks
---
# checks

Runs every check the vault has, in place of a vault-wide lint.

```bash
python3 _agent/tools/checks/run.py
```

It runs, in order:

1. the playbook index's `--check` (`.claude/skills/vlt-playbook/index.py`);
2. that every folder under `_agent/tools/` has a `README.md`;
3. every `_agent/tools/<name>/check.py`.

All checks run even after one fails. The exit code is 1 if any failed.

**Adding a check.** Put a `check.py` in the tool's own folder. It exits non-zero when something is wrong and prints what. Keep it small: a check answers one question about what its tool owns, and says in its output what it looked at.

**Used by:** `add-a-tool.md`, and any playbook that ends by validating its work.
