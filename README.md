# vlt — a vault toolkit

vlt is a small toolkit for running a knowledge vault with an AI agent: conventions for where things live, **playbooks** any session can run, a strict wiki, research notes and task boards. It ships as a Claude Code plugin.

It has no cast, no personas and no memory of its own. A session reads the vault's rules, finds the playbook for the job, and runs it.

**The vault owns everything.** Setup copies the kits into your vault once. From then on every rule, playbook and skill is a file in your vault that you change freely. Later changes to the kits are offered one file at a time, as a diff you take or leave.

> **Coming from 0.x?** 1.0 is a different design: the partner model, the operating contract and the BMad module packaging are gone. Start with [`COMING-FROM-0.x.md`](COMING-FROM-0.x.md). The last 0.x release is the `v0.19.0` tag.

## What a vault looks like

```
CLAUDE.md                  imports _meta/vault.md
_meta/
  vault.md                 the rules, two pages
  wiki.md                  the wiki's rules
  frontmatter.md           the keys each kind of note carries
resources/playbooks/       one file per procedure; README.md is the convention
resources/wiki/            written only through the wiki playbooks
sources/                   add-only
projects/ areas/ resources/   zones, each with a README, tasks/ and tasks.base
_agent/
  tools/<name>/            one folder per tool, each with a README
  tasks/ + tasks.base      the vault's own task board
  sessions/  log.md        session notes and the log
  research/                research notes
  kits.lock                what was seeded, and from which version
.claude/skills/
  vlt-playbook/            prints the playbook index
  vlt-research/ vlt-ingest/ vlt-query/ vlt-feedback/    thin pointers at their playbooks
```

The vault is an Obsidian-style Markdown vault: wikilinks, callouts, YAML frontmatter, and `.base` files for the boards and indexes.

## The ideas

- **Playbooks are the extension point.** A procedure a session runs is one Markdown file in `resources/playbooks/`, with the need it answers in its frontmatter. The `vlt-playbook` skill prints the index. The playbook holds its own rules and paths; nothing restates them. To teach the vault something new, write a playbook (and a tool, if there is something to compute).
- **Tools live in one place.** Every script is in `_agent/tools/<name>/`, one folder per tool with a README. No scripts in PARA.
- **The wiki is strict.** It is written only by a session running `ingest`, `supersede` or `consolidate`, from a stored source. Every page carries who wrote it, how, and how far it is trusted. A changed claim is always shown, never overwritten.
- **Ingest takes more than files.** A file in `sources/`, a URL (captured first), pasted text, a research note, or anything a vault tool can turn into a source, such as a video transcriber.
- **Research is its own thing.** Any session can investigate a question on the web and file one research note. A note reaches the wiki only through ingest.
- **PARA is shared ground.** Any session may write in a zone unless its README says otherwise. A document that must be read before it is used carries `review: requested`.
- **Task boards, not a backlog.** Each zone has a folder of task files and a base that shows them; the vault has one of its own.
- **Checks, not a lint.** `python3 _agent/tools/checks/run.py` runs the small checks a vault has. A tool can add its own.

## The four kits

| Kit | Holds |
|---|---|
| `core` | `_meta/vault.md`, `_meta/frontmatter.md`, the `CLAUDE.md` stub, the playbook convention and the `vlt-playbook` skill, the tool convention, the check runner, the `add-a-tool` and `feedback` playbooks |
| `wiki` | `_meta/wiki.md`; the `ingest`, `query`, `supersede` and `consolidate` playbooks; the `vlt-ingest` and `vlt-query` skills; the wiki check |
| `research` | the `research` playbook and the `vlt-research` skill |
| `task-board` | the `task-board` and `set-up-a-zone` playbooks, the task template and base, the vault's own board |

A vault takes all four.

## Install

In Claude Code:

```
/plugin marketplace add mggower/bmad-module-vlt
/plugin install vlt@vlt
```

Then open a session in your vault (a git repository) and say **"set up vlt"**. `vlt-setup` copies the kits in, never overwrites a file that already exists, shows a diff for each one it left alone, and runs the checks.

## Updating

Update the plugin, then say **"pull vlt"** in the vault. `vlt-pull` compares, for each seeded file, what the kit shipped when you last took it, what it ships now, and your copy. It shows what changed and applies only the files you accept. It refuses to replace a file with uncommitted changes, and it never deletes anything.

Two vaults seeded from the same kits will drift apart, on purpose. An improvement made in one reaches the other by going upstream: say **"file this upstream"** and `vlt-feedback` files a scrubbed issue you approve first.

## This repository

This repo is where the plugin is developed. A vault is a separate folder; nothing here is one.

| Path | What |
|---|---|
| `.claude-plugin/marketplace.json` | The plugin manifest |
| `skills/` | The two skills the plugin serves: `vlt-setup`, `vlt-pull` |
| `kits/<kit>/files/` | Every seeded file, at the path it has in a vault. `kit.yaml` carries the kit's version |
| `scripts/kits.py` | The seed-and-pull engine |
| `tools/package-lint.py` | The pre-release check |
| `tests/` | `uv run --with pytest pytest tests/ -q` |
| `COMING-FROM-0.x.md`, `FLATTEN-A-PARTNER.md` | For vaults on 0.x |
| `factory/` | The development record: `inbox/` holds open field filings; `cycles/`, `studies/`, `platform/` and `method/` are the history of 0.x |
| `docs/superpowers/` | The 1.0 design and its build plan |

Changes follow four steps: a filing lands in `factory/inbox/`, a change is made on a branch, the package check passes, and the release is tagged and noted in `CHANGELOG.md`.

Found a defect in a live vault? Open an issue with one of the templates, or use `vlt-feedback` from the vault.

## License

MIT. See `LICENSE`.
