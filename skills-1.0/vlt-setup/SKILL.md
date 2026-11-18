---
name: vlt-setup
description: Seeds the vlt kits into a vault — the rules, playbooks, named skills, tool conventions and task board — as files the vault then owns. Use when the user says "set up vlt", "install vlt in this vault", "seed the kits", or runs vlt in a vault that has no `_agent/kits.lock`.
---

# vlt-setup

Copies the four vlt kits (`core`, `wiki`, `research`, `task-board`) into the vault in the current directory. Every file it writes belongs to the vault from then on: the owner changes any of them freely, and later takes or leaves kit changes one file at a time with `vlt-pull`.

Setup **never overwrites or deletes a file that already exists.** It is safe to run in a vault that still has an older vlt installed, and safe to run twice.

The engine is `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/kits.py"`, called `kits.py` below. `--vault .` means the current directory.

## Steps

1. **Confirm the place.** The current directory is the vault's root and a git repository (`git rev-parse --show-toplevel` prints it). If either is not so, say which and stop. Tell the user the four kits are taken together.
2. **Seed.** Run `kits.py seed --vault .` and read its output. Each line is one file:
   - `seeded <path>`: written; it did not exist.
   - `same <path>`: already there, identical.
   - `kept-yours <path>`: already there and different. It was left alone.
   - `vault-removed <path>`: seeded once, deleted by the vault since. It was not re-created.
   An exit code of 2 means `_agent/kits.lock` exists but cannot be read, or a kit is broken: show the message and stop.
3. **Report.** Give the counts, then list every `kept-yours` and `vault-removed` path by name.
4. **Show each difference, change nothing.** For each `kept-yours` path run `kits.py diff --vault . <path>` and show it. Do not take the kit's copy here. If the user wants one, they commit their own version first and then say so; run `kits.py take --vault . <path>`, which refuses over uncommitted changes.
5. **The one line `CLAUDE.md` needs.** If `CLAUDE.md` was `kept-yours`, the vault's rules are not loaded until it imports them. Show the user this line to add, and add it only on their word:

   ```
   @_meta/vault.md
   ```
6. **Run the checks.** `python3 _agent/tools/checks/run.py`. Show the result as it is. In a vault that already had content, a failure describes that content (a wiki page without its attestation keys, a tool folder without a README); it is information, not something setup repairs.
7. **Hand over.** Tell the user what to commit: the seeded paths and `_agent/kits.lock`. Do not commit for them unless asked. Point at the three places to start: `_meta/vault.md` (the rules), `resources/playbooks/README.md` (how procedures work), and the `vlt-playbook` skill (the index).

## Coming from vlt 0.x

Nothing seeded here reads or depends on anything an older vlt installed, so the old machinery can be retired before, after or gradually. The module repository's `COMING-FROM-0.x.md` maps what 0.x installed to what replaces it, and `FLATTEN-A-PARTNER.md` is a reference for retiring a partner. Both are read from `${CLAUDE_PLUGIN_ROOT}`. Setup runs neither: migrating a vault is that vault's own work.
