# Flatten a partner

A reference for retiring a vlt 0.x partner (its persona, memory, partner-owned capabilities and ritual) into playbooks and tools any session can run. It was worked out in a live vault over several partners and is generalised here.

This is a document a session in the vault reads and follows. The module runs none of it, and `vlt-setup` does not copy it into a vault. It applies to the three partners 0.x shipped (librarian, researcher, creative) as much as to ones a vault minted. For the shipped three, steps 2 and 3 are usually short: the wiki procedures and research already exist as 1.0 playbooks, so what is left is the persona's own files and anything the vault added to it.

Run `vlt-setup` first, so `resources/playbooks/` and `_agent/tools/` exist with their conventions.

Nothing is deleted at any step. Every move is `git mv`.

## 0. Decide with the owner, before touching anything

- **Which capabilities become playbooks and which are retired** with the persona. Default: nothing is cut that the owner did not name. A procedure nobody is running this month is still a playbook; it gets `state: dormant` and a one-line callout, not a separate folder.
- **Where the code lives.** If scheduled jobs or other scripts import it from where it is, it stays there until a quiet moment, and the playbook's `tools:` names it where it is. If nothing imports it, move it now to `_agent/tools/<name>/` and fix its path constants in the same commit.
- **The PARA homes** for what the partner wrote for a reader: `areas/<domain>/` for standing responsibilities, `projects/<domain>-<period>/` for dated work, `resources/<domain>/` for method notes and reference records. Playbooks go to `resources/playbooks/`, flat, never nested by domain.

## 1. Inventory (read-only)

List, without changing anything:

- the partner's memory and capability files (`_agent/partners/<slug>/` and its `capabilities/`);
- the partner's working folder, with a file count per sub-folder;
- the scheduled jobs that belong to it (`_agent/schedule/` and the vault's scheduler entries);
- every hardcoded path in its scripts and scheduled jobs;
- open pointers addressed to it in `_agent/dispatch.md`;
- items in `_agent/backlog.md` attributed to it, which will be orphaned;
- subscriptions or recurring deliveries that name it.

Sort every file in its working folder into three bins:

- **machine**: code, stores, raw snapshots, derived data, build inputs;
- **reader**: anything a person reads (reports, boards, ledgers, rules, retrospectives);
- **persona**: the skill, identity, thread, casebook, reflexes, capabilities.

Watch for reader files that are also build inputs. They move, and the script's path constant moves with them.

## 2. Move the reader files

Create the PARA homes, then `git mv` by bin. Edit every path constant found in step 1. Before committing, verify with the domain's own dry run: one offline build, one real render against the new paths. Commit path-scoped. Then run one scheduled job by hand and confirm it writes to the new home and commits only what it wrote.

## 3. Write the replacements

- **One playbook per capability** in `resources/playbooks/`, to the convention in that folder's `README.md`: what it is, prerequisites, commands, where output lands, what runs on a schedule. Strip the persona's voice. Keep the owner's rulings verbatim, dated and attributed. Reference material a playbook needs sits beside it as a companion, `<playbook>-<what>.md`.
- **One method note** for any engine or store: what it is, how to build and render, and an honest verdict on what it is good for.
- **A `README.md`** in each PARA home and in each tool folder, saying what lives there and which playbooks use it.
- **No index to edit.** The `vlt-playbook` skill reads each playbook's frontmatter. Add the domain to the `domains:` list in `resources/playbooks/README.md` if it is new, and run `python3 .claude/skills/vlt-playbook/index.py --check`. Add words to the skill's `description:` only if the new playbooks answer a kind of request it does not name. One skill for all playbooks, never one per domain.

A rule of conduct or a path lives in the playbook it governs, never in a skill.

## 4. Archive the persona

```bash
git mv _agent/partners/<slug> _agent/archive/partners/<slug>
git mv .claude/skills/vlt-agent-<slug> _agent/archive/partners/<slug>/skill
```

Add a `RETIRED.md` beside them: why, what replaced it, and where the decision is recorded.

## 5. Close the loose ends

- **Inbound links.** Search the live PARA files for the old paths and rewrite them. Leave historic records alone: session notes, the log, past reports.
- **Dispatch.** Close every open pointer addressed to the partner, with a dated reason.
- **Backlog.** Dispose each item attributed to the partner with the owner: close it with a reason, or move it to the task board of the zone that owns the subject (`resources/playbooks/task-board.md`).
- **Recurring deliveries** that went to the partner: retire them (remove the scheduler entry and its file in `_agent/schedule/`) or re-address them.
- **Standing pointers.** If the vault's `CLAUDE.md` or `_agent/reflexes.md` sends sessions to the partner, replace that with where the playbooks are.
- A session note, a log entry, and path-scoped commits throughout.

## 6. Validate

Run `python3 _agent/tools/checks/run.py`. It checks the playbook index, that every tool folder has a README, and each tool's own check. It does not look at moved files that never had frontmatter, or at links between notes, so a clean run does not cover those: spot-check the moved reader files by opening them.

Expect residue that should be left alone: old records that name the retired partner are history.

## What a flatten does not do

Rewrite historic paths inside records. Change what a tool computes. Delete anything.
