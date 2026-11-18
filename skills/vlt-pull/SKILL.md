---
name: vlt-pull
description: Shows what has changed in the vlt kits since this vault last took them, and applies only the files the owner accepts. Use when the user says "pull vlt", "update the kits", "what changed in vlt", or "take the new version of <a seeded file>".
---

# vlt-pull

The vault owns every file the kits seeded. Pull compares three things for each one: the copy the kit shipped when the vault last saw it (recorded in `_agent/kits.lock`), the kit's copy now, and the vault's copy. It shows what differs and changes only what the owner accepts.

The engine is `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kits.py"`, called `kits.py` below.

## Steps

1. **Read the state.** Run `kits.py status --vault .` from the vault's root. An exit code of 2 means there is no usable `_agent/kits.lock`: show the message and stop. If the vault was seeded before, the lock is restored from git (`git checkout -- _agent/kits.lock`), never rebuilt by running setup again: a fresh seed re-creates files the vault deleted on purpose and forgets which kit changes are still waiting. Only a vault that was never seeded needs `vlt-setup`. Do not guess which case it is; ask.
2. **Report every file that is not `unchanged`,** grouped by state:

   | State | Means | What pull does |
   |---|---|---|
   | `shipped-changed` | The kit changed it; the vault did not. | Shows the diff; asks take or leave. |
   | `new` | The kit added a file since the lock. | Shows the file; asks take or leave. |
   | `both-changed` | The kit and the vault both changed it. | Shows the diff; asks take or leave, with the warning below. |
   | `vault-changed` | The vault changed it; the kit did not. | Lists it. Nothing to pull. |
   | `vault-removed` | The vault deleted it. | Lists it. It is never re-created unasked. |
   | `retired` | The kit no longer ships it. | Lists it. The vault's copy is left alone. |

   If everything is `unchanged`, say so and stop.
3. **For each file that asks a question,** run `kits.py diff --vault . <path>` (it prints the vault's copy against the kit's), show it, and ask: take or leave.
   - **Take** writes the kit's copy over the vault's. On a `both-changed` file that replaces the vault's own edits, so say so before asking. The engine refuses when the vault's copy has uncommitted changes; commit it first, so the vault's version stays recoverable from git.
   - **Leave** keeps the vault's copy and records the kit's version as seen, so the same change is not offered again.
   - Undecided: do neither, and it is offered next time.
4. **Apply.** `kits.py take --vault . <path>...` and `kits.py leave --vault . <path>...` with the paths the owner chose. Read the output; a refused path is reported by name.
5. **On request only:** `take` also restores a `vault-removed` file or replaces a `vault-changed` one with the kit's copy, and `leave` on a `retired` path drops it from the lock. Do these only when the owner asks for that file.
6. **Run the checks.** `python3 _agent/tools/checks/run.py`.
7. **Hand over.** List the files taken and tell the owner to commit them with `_agent/kits.lock`.

## Rules

- Nothing is applied that the owner did not accept, file by file.
- Pull never deletes a vault file.
- A change worth having in the kits themselves goes upstream with the `vlt-feedback` skill; pull only brings changes down.
