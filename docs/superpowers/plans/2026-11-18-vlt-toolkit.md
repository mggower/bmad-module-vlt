# vlt 1.0 Toolkit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the v0.19.0 partner module with a plain Claude Code plugin that seeds four vault-owned kits (core, wiki, research, task-board) and lets a vault pull kit changes file by file.

**Architecture:** Kit files sit in the repo at `kits/<kit>/files/<vault-relative path>`, so the tree is the manifest. One stdlib script, `scripts/kits.py`, seeds them into a vault, records hashes in `_agent/kits.lock`, and reports a three-way status per file. The plugin ships two skills (`vlt-setup`, `vlt-pull`) that drive that script; every other skill and every procedure is a seeded file the vault owns.

**Tech Stack:** Python 3.9+ standard library only (no pyyaml in anything seeded or shipped), pytest run as `uv run --with pytest pytest tests/ -q`, Markdown, Obsidian `.base` files, git.

**Spec:** `docs/superpowers/specs/2026-11-18-vlt-toolkit-design.md`. Read it whole before any task.

## Global Constraints

- Work on a new branch `vlt-1.0` cut from `cycle16-v0.19.0`. One commit per task, `git commit -m "title" -m "body"`, no co-author trailer, never push.
- The repo is public. No machine paths, usernames, the owner's first name or a vault's real path in any tracked file. Use "the owner", `{field-vault}`, `~`. Content lifted from the field vault is scrubbed of its domains (football, food, design) except as one generic example.
- Module development happens in this repo only. The field vault is read for source material and never written.
- Setup and pull never overwrite or delete a vault file the owner has not accepted. Nothing in 1.0 reads a 0.19 artifact.
- No persona, role, mode, memory, ritual or routing in any shipped file. No word "partner" in `kits/`.
- A procedure a session runs is a playbook. There is no second mechanism.
- Shipped files name literal default paths. No `{logical-name}` path map.
- Page budgets, enforced by the package lint: `_meta/vault.md` ≤ 120 lines, `_meta/wiki.md` ≤ 120 lines, `_meta/frontmatter.md` ≤ 150 lines, each named skill's `SKILL.md` ≤ 15 lines.
- 0.19 source text is read from disk until Task 9 removes it, and from `git show v0.19.0:<path>` afterwards.
- Seeded Python is stdlib only and finds the vault from its own location, so the working directory does not matter.

## Review Focus

1. **Setup in a vault that already has a `CLAUDE.md`** (every 0.19 vault). The stub is not copied, so nothing imports `_meta/vault.md`. Setup must print the one line to add. Pinned in Task 1 (`kept-yours` report) and Task 8.
2. **Pull after the owner deleted a seeded file on purpose.** It must report the file as removed in the vault and never re-create it unasked. Pinned in Task 1.
3. **Taking a shipped change over a vault file with uncommitted edits.** The take must refuse, so the vault's version is always recoverable from git. Pinned in Task 1.
4. **A playbook with no frontmatter, or a broken one.** The index still prints the table for the others; `--check` names the file. Pinned in Task 2.
5. **Pull with a missing or unreadable `kits.lock`.** It must stop with a message pointing at setup, not treat every file as new. Pinned in Task 1.

---

## File structure

```
.claude-plugin/marketplace.json     version 1.0.0; skills: vlt-setup, vlt-pull
scripts/kits.py                     seed / status / diff / take / leave
skills/vlt-setup/SKILL.md
skills/vlt-pull/SKILL.md
kits/<kit>/kit.yaml                 name, version, description (flat key: value)
kits/<kit>/files/...                mirrors the vault path of every file
tools/package-lint.py               rewritten small
tests/                              pytest
COMING-FROM-0.x.md  FLATTEN-A-PARTNER.md  README.md  CHANGELOG.md  CLAUDE.md
```

Kit contents (paths are under `kits/<kit>/files/`):

| Kit | Files |
|---|---|
| `core` | `CLAUDE.md`, `_meta/vault.md`, `_meta/frontmatter.md`, `.claude/skills/vlt-playbook/{SKILL.md,index.py}`, `.claude/skills/vlt-feedback/SKILL.md`, `resources/playbooks/{README.md,playbooks.base,add-a-tool.md,feedback.md,feedback-field-contract.md}`, `_agent/tools/README.md`, `_agent/tools/checks/{README.md,run.py}`, `_agent/templates/{session-note.md,log-entry.md}`, `_agent/bases/review.base` |
| `wiki` | `_meta/wiki.md`, `resources/playbooks/{ingest.md,query.md,supersede.md,consolidate.md}`, `.claude/skills/{vlt-ingest,vlt-query}/SKILL.md`, `_agent/tools/wiki/{README.md,check.py}` |
| `research` | `resources/playbooks/research.md`, `.claude/skills/vlt-research/SKILL.md` |
| `task-board` | `resources/playbooks/{task-board.md,set-up-a-zone.md}`, `_agent/templates/{zone-task.md,tasks.base,zone-readme.md}`, `_agent/tasks.base`, `_agent/tasks/.gitkeep` |

---

### Task 1: The kit engine

**Files:**
- Create: `scripts/kits.py`
- Test: `tests/test_kits.py`, `tests/conftest.py`

**Interfaces:**
- Produces, as a CLI (`python3 scripts/kits.py <cmd> --vault <dir> [--kits-dir <dir>]`; `--kits-dir` defaults to `<script>/../kits`):
  - `seed` copies every kit file whose vault path does not exist, leaves every one that does, writes the lock, prints one line per file: `seeded <path>`, `same <path>` or `kept-yours <path>`. Exit 0.
  - `status [--json]` prints one line per file `<state> <kit> <path>`. States: `unchanged`, `shipped-changed`, `vault-changed`, `vault-removed`, `both-changed`, `new`, `retired`.
  - `diff <path>` prints a unified diff, vault copy against the kit's current copy.
  - `take <path>...` writes the kit's current copy and records its hash.
  - `leave <path>...` records the kit's current hash without touching the vault file, so the change is not offered again.
- Produces, as importable functions (tests and the lint use them): `kit_files(kits_dir) -> dict[str, tuple[str, Path]]` (vault path → (kit name, source file)); `read_lock(vault) -> dict`; `state(lock_hash, kit_hash, vault_hash) -> str`.
- Lock file `_agent/kits.lock`, JSON: `{"schema": 1, "kits": {"<kit>": {"version": "<kit.yaml version>", "files": {"<vault path>": "<sha256 of the shipped file>"}}}}`. Seed records the shipped hash even for `kept-yours`.
- State table, with L = lock hash, K = kit hash, V = vault hash, `None` = absent:

| Condition | State |
|---|---|
| V == K (any L) | `unchanged` (pull refreshes L silently) |
| L is None, V is None | `new` |
| K is None | `retired` (reported; the vault file is never touched) |
| V is None, L set | `vault-removed` |
| K != L, V == L | `shipped-changed` |
| K == L, V != L | `vault-changed` |
| otherwise | `both-changed` |

- [ ] **Step 1: Write the failing tests.** `conftest.py` provides `kits_dir` (a temp dir with kit `core`, version `1.0.0`, files `_meta/vault.md` and `resources/playbooks/README.md`) and `vault` (an empty temp dir with `git init` and one empty commit). Tests, each by name:

```python
def test_seed_copies_and_locks(vault, kits_dir): ...
    # both files exist in vault, byte-identical; lock["kits"]["core"]["version"] == "1.0.0";
    # lock hash == sha256 of the shipped file; stdout has "seeded _meta/vault.md"
def test_seed_never_overwrites(vault, kits_dir): ...
    # vault/_meta/vault.md pre-written as "mine"; after seed still "mine"; stdout "kept-yours _meta/vault.md"
def test_seed_twice_is_idempotent(vault, kits_dir): ...
    # second run prints only "same ..." lines; lock unchanged
def test_state_table(): ...
    # one assert per row of the table above, calling state(L, K, V)
def test_status_after_kit_edit(vault, kits_dir): ...            # "shipped-changed core _meta/vault.md"
def test_deleted_vault_file_is_vault_removed_not_recreated(vault, kits_dir): ...
    # delete the file, run status -> "vault-removed"; run seed again -> file still absent, status unchanged
def test_take_refuses_uncommitted_vault_edit(vault, kits_dir): ...
    # commit seeded files, edit vault file without committing, edit kit file; take exits 1,
    # stderr contains "uncommitted", vault file unchanged
def test_take_applies_and_records(vault, kits_dir): ...         # after take: file == kit copy, status "unchanged"
def test_leave_records_without_writing(vault, kits_dir): ...    # after leave: file untouched, status "vault-changed"
def test_missing_lock_stops_pull_commands(vault, kits_dir): ...
    # status/take/leave with no lock: exit 2, stderr contains "run vlt-setup"
def test_corrupt_lock_stops(vault, kits_dir): ...               # lock = "{", exit 2, same message
def test_retired_file_is_reported_and_kept(vault, kits_dir): ...
def test_path_with_spaces(vault, kits_dir): ...                 # a kit file "resources/play books/x.md" seeds and statuses
```

- [ ] **Step 2: Run them, confirm they fail.** `uv run --with pytest pytest tests/test_kits.py -q` → errors on the missing module.
- [ ] **Step 3: Implement `scripts/kits.py`.** `kit.yaml` is parsed as flat `key: value` lines. Hashes are sha256 of raw bytes. `take` checks `git status --porcelain -- <path>` in the vault and refuses on any output; a path that does not exist in the vault is allowed. `seed` after a lock exists does not re-create a `vault-removed` file.
- [ ] **Step 4: Run the tests, confirm they pass.**
- [ ] **Step 5: Commit.** `git add scripts tests && git commit -m "kits: the seed-and-pull engine" -m "seed, status, diff, take, leave over kits/<kit>/files; lock at _agent/kits.lock"`

---

### Task 2: Playbook convention, index and entry-point skill

**Files:**
- Create: `kits/core/kit.yaml`, and under `kits/core/files/`: `.claude/skills/vlt-playbook/SKILL.md`, `.claude/skills/vlt-playbook/index.py`, `resources/playbooks/README.md`, `resources/playbooks/playbooks.base`
- Test: `tests/test_playbook_index.py`

**Source to lift:** `{field-vault}`'s `resources/runbooks/README.md`, `.claude/skills/runbooks/SKILL.md` and `index.py`. Rename runbook → playbook throughout.

**Interfaces:**
- Produces: `python3 .claude/skills/vlt-playbook/index.py` prints a `| Domain | Need | Read |` table; `--check` prints problems and exits 1 on any. Later tasks' playbooks must pass it.
- Playbook frontmatter: `type: resource`, `created`, `last_updated`, `title: Playbook — <subject>`, `need:` (quoted line), `state: live | dormant`, `domain:`, optional `tools:` (list of paths under `_agent/tools/`), optional `companion:`. A companion carries `companion_of: <file>.md` and no `need:` or `state:`. No attestation keys on playbooks.
- The allowed `domain:` values are read from the `domains:` list in `resources/playbooks/README.md` frontmatter. Shipped value: `domains: [vault, wiki, research]`.
- Section names, in order: Prerequisites, Commands, Procedure, Output, Schedule, Rules, Known gaps.

Changes from the field version: `FOLDER` is `resources/playbooks`; `DOMAINS` comes from the README frontmatter (an empty or missing list fails `--check` with one problem naming the README); the `verified_at` comparison is dropped; a `tools:` path must start with `_agent/tools/`.

- [ ] **Step 1: Write the failing tests.** Each builds a temp vault with the README and a few playbooks, and runs the script as a subprocess.

```python
def test_table_lists_need_and_path(): ...          # row contains the need text and "`resources/playbooks/a.md`"
def test_dormant_is_marked(): ...
def test_companion_is_appended_not_listed(): ...   # "then `a-reference.md`" on a's row; no row of its own
def test_check_passes_on_clean_folder(): ...       # exit 0, last line "2 playbooks, 1 companions, 0 problems"
def test_check_fails_on_missing_need(): ...
def test_check_fails_on_unknown_domain(): ...      # domain: football with domains: [vault]
def test_check_fails_on_missing_tool_path(): ...
def test_check_fails_on_tool_outside_agent_tools(): ...
def test_check_fails_on_orphan_companion(): ...
def test_file_without_frontmatter_does_not_crash_table(): ...
    # a.md valid, b.md has no frontmatter: table exits 0 and still has a's row; --check names b.md
def test_domains_read_from_readme(): ...           # add "cooking" to README domains -> a cooking playbook passes
```

- [ ] **Step 2: Run, confirm fail.**
- [ ] **Step 3: Write `index.py`** to the interface above.
- [ ] **Step 4: Write `resources/playbooks/README.md`** from the field README: what a playbook is, the section table, the frontmatter table, where tools live (`_agent/tools/<name>/`, one folder per tool, flat; data in `_agent/stores/<name>/`), running one (one session note, one log entry, path-scoped commits; a scheduled leg writes neither), adding or changing one. Drop every sentence about partners, the operating contract, attestation and the adoption-date grandfather clause. Owner rulings quoted in the field version are restated as plain rules.
- [ ] **Step 5: Write `SKILL.md`.** `name: vlt-playbook`. The description names the generic triggers only: running or locating a standing vault procedure, and checking for a playbook before improvising any multi-step vault task. Body: the playbook is the authority; `` !`python3 "${CLAUDE_SKILL_DIR}/index.py"` ``; the fallback if it fails; "no row fits: say so and ask"; where the convention lives. Nothing else.
- [ ] **Step 6: Write `playbooks.base`**: one table over `resources/playbooks`, excluding `README.md` and files with `companion_of`, columns need, state, domain, grouped by domain.
- [ ] **Step 7: Run the tests, confirm pass. Commit** as `core kit: playbook convention, index and vlt-playbook skill`.

---

### Task 3: Core rules, templates and the check runner

**Files:**
- Create under `kits/core/files/`: `CLAUDE.md`, `_meta/vault.md`, `_meta/frontmatter.md`, `_agent/tools/README.md`, `_agent/tools/checks/README.md`, `_agent/tools/checks/run.py`, `_agent/templates/session-note.md`, `_agent/templates/log-entry.md`, `_agent/bases/review.base`
- Test: `tests/test_check_runner.py`

**Source to lift:** 0.19 `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` and `conventions/frontmatter.md`, for wording of the parts that survive only.

**Interfaces:**
- Produces: `python3 _agent/tools/checks/run.py` runs, in order, (a) the playbook index `--check`, (b) its built-in check that every directory under `_agent/tools/` has a `README.md`, (c) every `_agent/tools/*/check.py`. It prints each check's name and result, then `N checks, M failed`, and exits 1 if M > 0. A `check.py` is any script that exits non-zero on failure.
- Frontmatter keys other tasks rely on:
  - Base, every agent-written note: `type`, `created`, `last_updated`, `title`.
  - Attestation, required on wiki pages and research notes only: `author`, `trust` (`draft` set by an agent; only the owner raises it), `verified_by` (the playbook that wrote the note, e.g. `ingest`), `verified_at`.
  - Review, opt-in in PARA: `review: requested`, then `review: approved` set by the owner. A zone README may declare `review_default: requested`.

- [ ] **Step 1: Write the failing tests** for `run.py` against a temp vault holding the Task 2 files:

```python
def test_clean_vault_passes(): ...                     # exit 0, "0 failed"
def test_tool_folder_without_readme_fails(): ...       # _agent/tools/foo/ with only a script -> exit 1, names "foo"
def test_failing_check_py_fails_the_run(): ...         # _agent/tools/bar/check.py exits 3 -> exit 1, names "bar"
def test_all_checks_run_after_a_failure(): ...         # two tool checks, first fails, second's name still printed
def test_missing_playbook_index_is_reported(): ...     # skill folder absent -> that check fails with a clear line, run continues
```

- [ ] **Step 2: Run, confirm fail. Step 3: Implement `run.py`. Step 4: Run, confirm pass.**
- [ ] **Step 5: Write `_meta/vault.md`** (≤ 120 lines), five sections exactly as the spec's "The rules" lists them: write boundaries, records, naming and link syntax, honest reporting and grounding, where things live. Include the wiki-change rule: a session not running a wiki playbook files a task on the vault board (`_agent/tasks/`). Nothing from the spec's cut list.
- [ ] **Step 6: Write `_meta/frontmatter.md`** (≤ 150 lines): the base keys, then one short schema each for wiki page, research note, session note, playbook (pointer to the playbooks README, not a copy), task (pointer to the task-board playbook), zone README. Then attestation and review as above.
- [ ] **Step 7: Write the rest.** `CLAUDE.md` is a stub of at most ten lines whose one required line is `@_meta/vault.md`. `_agent/tools/README.md` states the tool convention (one folder per tool, a README naming what it is, how to run it and which playbooks use it; a multi-script engine is one folder; data in `_agent/stores/<name>/`; tests with the tool; scheduled legs in `_agent/schedule/`; an optional `check.py`). `review.base` lists notes where `review == "requested"`. The two templates carry the schemas from Step 6.
- [ ] **Step 8: Commit** as `core kit: the rules, frontmatter, templates and check runner`.

---

### Task 4: Feedback and add-a-tool playbooks

**Files:**
- Create under `kits/core/files/`: `resources/playbooks/feedback.md`, `resources/playbooks/feedback-field-contract.md`, `resources/playbooks/add-a-tool.md`, `.claude/skills/vlt-feedback/SKILL.md`

**Source to lift:** 0.19 `skills/vlt-feedback/SKILL.md` and `references/field-contract.md`; 0.19 `skills/vlt-mint/SKILL.md` for the little of mint that survives.

- [ ] **Step 1: Write `feedback.md`** (`domain: vault`) in the convention's sections. Keep: classify (defect, pattern, candidate, supersession), scrub, render the exact public payload and stop for the owner's approval, post with `gh`, and the loud degrade to a paste-ready local filing. Replace the `_bmad` config lookup with the literal repo slug from `.claude-plugin/marketplace.json`'s `repository`. The version stamp is read from `_agent/kits.lock` (the `core` kit's version). Remove every mention of a partner proposing a filing.
- [ ] **Step 2: Write `feedback-field-contract.md`** as its companion (`companion_of: feedback.md`), the 0.19 field contract with the same labels and field set, so `.github/ISSUE_TEMPLATE/` needs no change. Confirm that by reading the four issue templates against it.
- [ ] **Step 3: Write `add-a-tool.md`** (`domain: vault`), one screen: decide whether the need is a playbook only or a playbook plus a tool; make `_agent/tools/<name>/` with its README; write the playbook; add the domain to the README's `domains:` if new; run the check runner. It prescribes no interview and no ceremony.
- [ ] **Step 4: Write `vlt-feedback/SKILL.md`** (≤ 15 lines): frontmatter `name`, a `description` with the trigger phrases ("file this upstream", "send feedback to the module"), and one instruction: read `resources/playbooks/feedback.md` whole and run it.
- [ ] **Step 5: Verify.** Seed a temp vault (`python3 scripts/kits.py seed --vault "$T"`) and run `python3 "$T/_agent/tools/checks/run.py"`. Expected: `0 failed`. `grep -ri partner kits/` prints nothing.
- [ ] **Step 6: Commit** as `core kit: feedback and add-a-tool playbooks, vlt-feedback skill`.

---

### Task 5: The wiki kit

**Files:**
- Create: `kits/wiki/kit.yaml`, and under `kits/wiki/files/`: `_meta/wiki.md`, `resources/playbooks/{ingest,query,supersede,consolidate}.md`, `.claude/skills/vlt-ingest/SKILL.md`, `.claude/skills/vlt-query/SKILL.md`, `_agent/tools/wiki/README.md`, `_agent/tools/wiki/check.py`
- Test: `tests/test_wiki_check.py`

**Source to lift:** 0.19 `skills/vlt-ingest/SKILL.md`, `skills/vlt-query/SKILL.md`, and conventions `wiki-index.md`, `wiki-supersession.md`, `wiki-consolidation.md`. Keep the 0.19 key names and callout shapes for the index, supersession and consolidation unchanged, so existing wiki pages stay valid.

**Interfaces:**
- Consumes: attestation keys from Task 3; the playbook convention from Task 2 (`domain: wiki`).
- Produces: `_agent/tools/wiki/check.py`, exit 1 on any of: a page under `resources/wiki/` missing an attestation key; a page marked superseded whose successor file does not exist; a page not listed in the wiki index, or an index entry with no page.

- [ ] **Step 1: Write the failing tests**, one temp wiki each:

```python
def test_clean_wiki_passes(): ...
def test_missing_attestation_key_fails(): ...       # page without verified_by -> exit 1, names the page and the key
def test_dangling_successor_fails(): ...
def test_page_missing_from_index_fails(): ...
def test_index_entry_without_page_fails(): ...
def test_empty_wiki_passes(): ...                   # resources/wiki/ absent or empty -> exit 0
def test_page_without_frontmatter_fails_cleanly(): ...   # named in output, no traceback
```

- [ ] **Step 2: Run, confirm fail. Step 3: Implement `check.py`. Step 4: Run, confirm pass.**
- [ ] **Step 5: Write `_meta/wiki.md`** (≤ 120 lines): the wiki is written only by the four wiki playbooks, from a stored source; page shape; the index rule; supersession; consolidation. It names no Librarian and no persona.
- [ ] **Step 6: Write `ingest.md`.** Its Prerequisites section states the four accepted inputs from the spec's "Sources and ingest": a file already in `sources/`; a URL, which the playbook first saves into `sources/`; the output of a vault tool that deposits into `sources/`; an attested research note. URL capture, as decided here: fetch the page, save it as `sources/web/<YYYY-MM-DD>-<slug>.md` with frontmatter `type: source`, `url`, `captured_at`, `title`, body the page's readable text; a page that cannot be fetched stops the ingest with the reason. The rule that nothing edits a source afterwards is stated once, here.
- [ ] **Step 7: Write `query.md`, `supersede.md`, `consolidate.md`** from the 0.19 text, reduced to the convention's sections. Write the two named skills as in Task 4 Step 4, pointing at `ingest.md` and `query.md`.
- [ ] **Step 8: Verify** by seeding a temp vault and running the check runner: `0 failed`, and the index table shows four `wiki` rows. **Commit** as `wiki kit: rules, four playbooks, two named skills, the wiki check`.

---

### Task 6: The research kit

**Files:**
- Create: `kits/research/kit.yaml`, `kits/research/files/resources/playbooks/research.md`, `kits/research/files/.claude/skills/vlt-research/SKILL.md`

**Source to lift:** 0.19 `skills/vlt-research/SKILL.md`. The research-note schema already lives in `_meta/frontmatter.md` (Task 3); the playbook points at it.

- [ ] **Step 1: Write `research.md`** (`domain: research`): any session may run it; output is one dedicated research note in `_agent/research/` with attestation (`trust: draft`, `verified_by: research`); a research note never writes the wiki, and reaches it only through ingest once the owner has raised its trust. Drop the Researcher persona, its memory and delegate mode.
- [ ] **Step 2: Write the `vlt-research` skill** as in Task 4 Step 4.
- [ ] **Step 3: Verify** as in Task 5 Step 8 (one `research` row). **Commit** as `research kit: the research playbook and vlt-research skill`.

---

### Task 7: The task-board kit

**Files:**
- Create: `kits/task-board/kit.yaml`, and under `kits/task-board/files/`: `resources/playbooks/task-board.md`, `resources/playbooks/set-up-a-zone.md`, `_agent/templates/zone-task.md`, `_agent/templates/tasks.base`, `_agent/templates/zone-readme.md`, `_agent/tasks.base`, `_agent/tasks/.gitkeep`

**Source to lift:** `{field-vault}`'s `resources/runbooks/task-board.md`, `_agent/templates/zone-task.md` and `areas/food/tasks.base`.

**Interfaces:**
- Task frontmatter, lifted unchanged: `type: record`, `key`, `status` (`idea`, `needs-ruling`, `ready`, `in-progress`, `parked`, `done`, `dropped`), `summary`, `sub`, `theme`, `owner` (`owner` or `agent`), `priority`, `due`, `done_on`, `sessions`, `related`.
- `_agent/templates/tasks.base` carries the literal token `ZONE_TASKS_FOLDER` in its one `file.inFolder(...)` filter; setting up a zone copies it and replaces the token. `_agent/tasks.base` is the same file with `_agent/tasks`.

- [ ] **Step 1: Write `tasks.base`** from the field base: same seven views and the `lane` formula; the "My move" filter becomes `owner == "owner"`.
- [ ] **Step 2: Write `zone-task.md`** with no hardcoded sub-domain list: `sub:` is free text, and the zone README lists the zone's values.
- [ ] **Step 3: Write `task-board.md`** (`domain: vault`) from the field runbook, generalised: drop the Kanban history, the football paths and the worked example's domain; keep what goes where, the task file shape, the status meanings, add-a-task, set-a-status and the rules. One generic example task.
- [ ] **Step 4: Write `set-up-a-zone.md` and `zone-readme.md`.** A zone is a PARA container with a README (what it is; optional `writers:`; optional `review_default:`; its `sub:` values), a `tasks/` folder and a `tasks.base`. The procedure creates those three from the templates.
- [ ] **Step 5: Verify.** Seed a temp vault; run the check runner (`0 failed`); follow `set-up-a-zone.md` by hand for `areas/example` and confirm `areas/example/tasks.base` holds `areas/example/tasks` and no `ZONE_TASKS_FOLDER`. `grep -rn "ZONE_TASKS_FOLDER" kits/task-board/files/_agent/tasks.base` prints nothing.
- [ ] **Step 6: Commit** as `task-board kit: zone boards, the vault board, set-up-a-zone`.

---

### Task 8: The plugin's two skills, and the whole seed end to end

**Files:**
- Create: `skills-1.0/vlt-setup/SKILL.md`, `skills-1.0/vlt-pull/SKILL.md` (moved to `skills/` in Task 9, once the 0.19 skills are gone)
- Test: `tests/test_seed_end_to_end.py`, `tests/fixtures/vault-0.19/` (a minimal stand-in: `CLAUDE.md`, `_meta/vault-operating-contract.md`, `_meta/conventions/frontmatter.md`, `.claude/skills/vlt-ingest/SKILL.md`, `_agent/backlog.md`, `_bmad/config.yaml`, each a few lines)

**Interfaces:**
- Consumes: `scripts/kits.py` (Task 1), reached from a skill as `python3 "${CLAUDE_SKILL_DIR}/../../scripts/kits.py"`.

- [ ] **Step 1: Spike the install path before writing either skill.** Read the current Claude Code plugin documentation (Tavily first, per the owner's rule) and confirm three things: a marketplace entry with `"source": "./"` and a `skills` list installs without a separate `plugin.json`; the installed copy includes `scripts/` and `kits/` beside `skills/`; `${CLAUDE_SKILL_DIR}` resolves inside a plugin skill. If any is false, record what is true at the top of this task and adjust the path the skills use. Do not reason from memory.
- [ ] **Step 2: Write the failing end-to-end tests**, using the real `kits/`:

```python
def test_fresh_vault_passes_every_check(): ...
    # seed into an empty git vault -> run _agent/tools/checks/run.py -> exit 0
def test_every_seeded_skill_points_at_an_existing_playbook(): ...
    # vlt-research, vlt-ingest, vlt-query, vlt-feedback: the playbook path named in SKILL.md exists in the vault
def test_no_file_ships_in_two_kits(): ...               # kit_files() raises or the test finds no duplicate vault path
def test_seed_into_0_19_vault_changes_no_existing_file(): ...
    # copy fixtures/vault-0.19, hash every file, seed, re-hash: all original hashes equal;
    # stdout contains "kept-yours CLAUDE.md" and "kept-yours .claude/skills/vlt-ingest/SKILL.md"
def test_lock_lists_all_four_kits(): ...
```

- [ ] **Step 3: Run, fix whatever the real kits get wrong, confirm pass.**
- [ ] **Step 4: Write `vlt-setup/SKILL.md`.** Steps: confirm the working directory is the vault and a git repo; run `seed`; show the report grouped by `seeded` and `kept-yours`; for each `kept-yours` file run `diff` and show it, changing nothing; if `CLAUDE.md` was kept, print the one line to add (`@_meta/vault.md`); run the check runner; tell the owner to commit. It names all four kits and offers no choice among them.
- [ ] **Step 5: Write `vlt-pull/SKILL.md`.** Steps: run `status`; if it exits 2 say setup has not been run and stop; list every file not `unchanged`, grouped by state; for `shipped-changed`, `both-changed` and `new` show `diff` and ask take or leave per file; apply with `take` / `leave`; for `vault-removed` and `retired` report only; run the check runner; tell the owner to commit. It states that a `both-changed` take replaces the vault's edits and is refused unless they are committed.
- [ ] **Step 6: Commit** as `plugin: vlt-setup and vlt-pull, with the end-to-end seed tests`.

---

### Task 9: Remove 0.19 and rewrite the package lint

**Files:**
- Delete (`git rm -r`): every directory under `skills/` (all 17), `tools/cost-manifest.py`, `tools/test-cost-manifest.py`, `tools/dispatch-lane-check.py`, `tools/factory-paths-check.py`, `tools/test-package-lint.py`
- Move: `skills-1.0/*` → `skills/`
- Rewrite: `tools/package-lint.py`, `.claude-plugin/marketplace.json`
- Test: `tests/test_package_lint.py`

**Interfaces:**
- Produces: `python3 tools/package-lint.py --expect-version X.Y.Z` prints one line per failure and a final `PASS: N checks` or `FAIL: M of N`, exit 0 or 1. Checks:
  1. No cruft (`.decision-log.md`, `__pycache__`, `*.pyc`, `.DS_Store`) under `skills/`, `kits/`, `scripts/`, `.claude-plugin/`.
  2. `marketplace.json` version equals `--expect-version`, and every `kits/*/kit.yaml` version equals it.
  3. The manifest's `skills` list is exactly the directories under `skills/`.
  4. No vault path appears in two kits.
  5. The four page budgets from Global Constraints.
  6. Every named skill under `kits/*/files/.claude/skills/` other than `vlt-playbook` names a playbook that exists in some kit.
  7. No `/Users/`, `/home/` or the word `partner` (case-insensitive) in `kits/`.
  8. Seeding all kits into a temp directory and running the check runner there exits 0.

- [ ] **Step 1: Write the failing tests**: one case per check that copies the repo's shipped surface to a temp dir, seeds one defect, and asserts `FAIL` naming that check; plus `test_real_tree_passes`.
- [ ] **Step 2: Run, confirm fail.**
- [ ] **Step 3: Do the deletions and the move.** Rewrite `marketplace.json`: version `1.0.0`, skills `./skills/vlt-setup` and `./skills/vlt-pull`, a description of a vault toolkit with no cast, keywords without `bmad`, `agents` or `self-evolving`. The author block is unchanged.
- [ ] **Step 4: Rewrite `tools/package-lint.py`** to the eight checks, stdlib only.
- [ ] **Step 5: Run everything.** `uv run --with pytest pytest tests/ -q` all green; `python3 tools/package-lint.py --expect-version 1.0.0` prints `PASS: 8 checks`. `git grep -l "_bmad\|module.yaml\|module-help" -- skills kits scripts tools` prints nothing.
- [ ] **Step 6: Commit** as `remove the 0.19 surface; package lint rewritten for kits`.

---

### Task 10: The two migration documents

**Files:**
- Create: `COMING-FROM-0.x.md`, `FLATTEN-A-PARTNER.md` (repo root; neither is in a kit)

- [ ] **Step 1: Build the 0.19 inventory from source, not memory.** From `git show v0.19.0:skills/vlt-setup/SKILL.md` and the `assets/` tree at that tag, list everything setup and upgrade wrote into a vault: the 17 skills, four workflow scripts, the `vlt-vitals` hook and its settings entry, the `_meta/` bundle (contract, rule card, conventions, personas), `tripwires.yaml`, `_bmad` entries, partner folders, and the ledgers (`backlog.md`, `dispatch.md`, `reflexes.md`, `upgrade-ledger.md`, lint reports and cache).
- [ ] **Step 2: Write `COMING-FROM-0.x.md`** as one table: what 0.19 installed, where it is in a vault, what replaces it in 1.0 or "nothing". Then three short statements: setup is safe to run first; nothing in 1.0 reads any row of the table; retiring is `git mv` into `_agent/archive/`, never deletion. It prescribes no order and no procedure.
- [ ] **Step 3: Write `FLATTEN-A-PARTNER.md`** from `{field-vault}`'s `resources/runbooks/flatten-a-partner.md`, keeping its seven steps (decide, inventory, move reader files, write replacements, archive the persona, close loose ends, validate). Generalise: no domain names, no scheduler-specific commands (say "the vault's scheduler entries"), runbooks → playbooks at `resources/playbooks/`, tools → `_agent/tools/<name>/`, validation is the check runner in place of the lint. It opens by saying it is a reference a vault session reads, that the module runs nothing, and that it applies to the three shipped partners as much as to minted ones.
- [ ] **Step 4: Verify.** `git grep -n "/Users/\|football\|launchctl" -- COMING-FROM-0.x.md FLATTEN-A-PARTNER.md` prints nothing. Every row of the Step 1 inventory appears in the table.
- [ ] **Step 5: Commit** as `migration: the coming-from map and the flatten reference`.

---

### Task 11: Collapse the factory and close cycle 16

**Files:**
- Rewrite: `CLAUDE.md`, `README.md`, `.claude/skills/vlt-release/SKILL.md`, `.claude/skills/issue-triage/SKILL.md`
- Delete (`git rm -r`): `.claude/skills/{acceptance-discharge,build-brief,cycle-closeout,ideation-scaffold,inbox-capture,lifecycle-status,roadmap-roundtable}`, `.claude/skills/vlt-lifecycle.md`
- Modify: `factory/CYCLE` (to `none`), `factory/cycles/16-closed-loops/roadmap.md` (closing stamp), `factory/inbox/README.md`, `CHANGELOG.md`
- Create: `factory/inbox/2026-11-18-1.0-disposition.md`

- [ ] **Step 1: Draft the inbox disposition and stop for the owner.** Read every open filing in `factory/inbox/`. Write `2026-11-18-1.0-disposition.md` as a table: filing, one-line subject, and either "closed: concerns removed machinery (<which>)" or "re-read: <keep or close, with the reason against 1.0>". Show the owner the table. Move nothing until they answer.
- [ ] **Step 2: Apply the owner's ruling.** `git mv` closed filings to `factory/cycles/16-closed-loops/filings/`. Kept filings stay in the inbox.
- [ ] **Step 3: Close cycle 16.** Add a closing stamp at the top of its roadmap, under the title: closed 2026-11-18, superseded by 1.0, pointing at the design doc and the disposition file; its two gating FAILs and unfired tails are recorded as void because the machinery they tested no longer ships. Append nothing else to it. Set `factory/CYCLE` to `none` with a comment that cycles ended at 16.
- [ ] **Step 4: Rewrite `CLAUDE.md`.** Keep: factory versus field, the public-repo and no-personal-information rules, placeholder paths in shipped examples, what not to touch, the commit-at-every-milestone rule. Replace the eight-step lifecycle with four: a filing lands in `factory/inbox/`; a change is made on a branch; `python3 tools/package-lint.py --expect-version X.Y.Z` exits 0; the release is tagged and noted in `CHANGELOG.md`. Remove the governance SSoT, version handshake, `module-help.csv`, workflows, decision-log and durability rules. Add the standing rules 1.0 needs: kit files mirror vault paths; a rule lives in the vault's file, never in a plugin skill; every procedure is a playbook.
- [ ] **Step 5: Rewrite the two kept factory skills** to the four-step flow. `vlt-release` becomes: pre-flight, bump `marketplace.json` and every `kit.yaml`, lint gate, commit with the PASS line, ff-merge, tag, push, each outward step on the owner's go. `issue-triage` keeps grounding an issue against source and materialising an accepted one into the inbox; the roadmap-to-tracker sync is removed.
- [ ] **Step 6: Rewrite `README.md`** for 1.0 (what it is, install, `vlt-setup`, `vlt-pull`, the four kits, playbooks, coming from 0.x) **and add the `1.0.0` entry to `CHANGELOG.md`**, leaving earlier entries untouched.
- [ ] **Step 7: Verify.** `git grep -n "vlt-upgrade\|vlt-lint\|vlt-mint\|roundtable\|acceptance-discharge" -- CLAUDE.md README.md .claude/skills` prints nothing. The lint still prints `PASS: 8 checks`.
- [ ] **Step 8: Commit** as `factory: four-step flow; cycle 16 closed as superseded by 1.0`.

---

### Task 12: Release readiness

- [ ] **Step 1: Run the whole gate.** `uv run --with pytest pytest tests/ -q` and `python3 tools/package-lint.py --expect-version 1.0.0`. Both green.
- [ ] **Step 2: Dry-run against a copy of the field vault.** `cp -R` the field vault to the scratchpad, run `seed` there, and confirm from `git status` in the copy that no tracked file is modified and only new files appear. Run the check runner in the copy and record what it reports (failures here are information about the vault, not the module). Delete the copy.
- [ ] **Step 3: Check the spec, section by section,** against the branch, and list any requirement with no file behind it.
- [ ] **Step 4: Stop and report to the owner.** Merging to `main`, tagging `v1.0.0` and pushing are theirs to order; do none of them unasked.
