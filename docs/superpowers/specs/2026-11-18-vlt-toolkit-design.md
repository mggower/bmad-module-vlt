# vlt 1.0: from a cast of partners to a vault toolkit

Status: approved by the owner, 2026-11-18. Supersedes the direction of v0.19.0.

Paths in this document are vault-relative or repo-relative. `{field-vault}` is the primary live vault; "the work vault" is the second install.

## Intent

vlt stops being a cast of partners governed by a contract. It becomes a small toolkit: conventions, an extension point, and a few starter kits that any agent session can run and each vault can change.

Why: partners are expensive to run and they accumulate biases (memory, taste, standing rulings) that work against the owner. The field has already moved. In `{field-vault}` two partners were flattened into procedures any session runs (`resources/runbooks/`, with one pointer skill and a frontmatter index), zone task boards have replaced the backlog, and the vault-wide lint has not been run in a long time. The module should adopt what the field proved and drop the rest.

There is one consumer: the owner, with two vaults that have diverged on purpose. Backwards compatibility is not a goal.

## Goals

1. A core set of tools that any agent session can use, with no persona, memory or ritual between the session and the tool.
2. The partner model retired completely. The module ships no persona, memory, ritual or routing, and nothing that assumes one.
3. Governance the vault owns. Any rule can be changed in the vault, with no module release.
4. Clear conventions for where things live, so a vault stays clean as it grows tools.
5. Starter kits for the patterns the owner has rebuilt more than once. The task board is the first.

## Non-goals

- A general install story for other users.
- Migrating any vault. That is done in each vault, by its own sessions.
- Rebuilding the vault-wide lint.
- Changing what any existing vault tool does (the football engine, the transcriber). They move; they do not change.
- Propagating fixes across vaults automatically.

## Anti-goals

These make the work a failure even if it ships:

- A new contract that grows back. If the rules file needs a derived summary card, it is too long.
- Any vault rule that needs a module release to change.
- Personas returning under another name ("roles", "modes", "owners" of a procedure).
- Deleting history. Vault moves are `git mv` into an archive.
- A second mechanism beside playbooks for "a procedure a session runs".

## Approaches considered

**A. Seed and own (chosen).** The module is a starter kit. Setup copies defaults and kits into the vault once. The vault owns every file afterwards. Updates are pulled per kit as a diff the owner takes or leaves. Cost: the two vaults drift, and an improvement crosses only through a feedback filing and a pull.

**B. Thin core, vault-owned rules.** The module keeps owning a small core that upgrades overwrite; governance moves to vault files that fully replace the shipped ones. Gain: fixes reach both vaults on upgrade. Cost: upgrade machinery and a "module's file or mine?" boundary stay.

**C. No module.** One vault is the reference and pieces are copied by hand. Rejected: personal content and tooling would share a repo, and feedback would have no destination.

The owner chose A. With one consumer and two deliberately different vaults, drift is already the practice, and A makes "the vault can change any rule" true by construction.

## Decisions the owner made

- **Partners:** none survive, the Librarian included.
- **The wiki stays strict, without a persona.** The wiki is written only by the wiki procedures (ingest, supersede, consolidate), run from an immutable source under the wiki conventions. Any session may run them. No session writes the wiki outside them; everything else files a research note or proposes a change.
- **Kept capabilities:** research (dedicated research notes, run by any agent), ingest, query, the wiki conventions, immutable sources, feedback to the module repo.
- **Mint** survives only as a short, non-prescriptive method for adding a tool or a playbook.
- **Dropped:** dispatch, track, review-council, decay, groom, extract, the vault-wide lint, partner memory, the activation ritual, consult and spec conventions, council personas.
- **Session notes and the log stay.** They carry history that is otherwise lost.
- **The backlog is replaced** by task boards: one per zone, plus one for the vault itself.
- **Tools live in `_agent/tools/<name>/`**, one folder per tool, flat, with the domain as metadata. No scripts in PARA.
- **Write attestation** (`author`, `trust`, `verified_by`, `verified_at`) is always on wiki pages and research notes, and opt-in per document in PARA, for documents the owner must review before they are used or published.
- **Write boundaries loosen.** PARA zones are hybrid authorship by default.
- **Ownership model:** A, above.
- **Not a BMad module.** vlt ships as a plain Claude Code plugin. `module.yaml`, the help registry, the `_bmad` config writes and every installer interop path are removed.
- **Research and the wiki procedures keep their own named skills** (`vlt-research`, `vlt-ingest`, `vlt-query`). They are what feels distinctly vlt and should be reachable by name. Feedback is reachable by name too (`vlt-feedback`).
- **Named skills are thin pointers, seeded into the vault.** The playbook holds the procedure; the skill only points at it. The skills are seeded into the vault's `.claude/skills/`, not served from the plugin, so the vault can change them.
- **The playbook entry-point skill is `vlt-playbook`.**
- **Flatten-a-partner ships as a migration reference**, not a kit: a generalised copy in the module repo beside the coming-from note. Nothing is seeded into a vault.
- **Ingest accepts more than a file.** A URL, or anything a vault tool can turn into a source (in `{field-vault}`, a YouTube video through the transcription tool), is a valid thing to ingest.
- **Playbooks stay in PARA** at `resources/playbooks/`, as documents the owner reads. Only scripts live under `_agent/`.
- **Migrating a vault is the vault's business, not the module's.** Which vaults move, when, and what happens to vault-grown things such as `{field-vault}`'s briefs are decided and done in each vault.

## Design

### What a vault looks like after

```
CLAUDE.md                  vault-owned; imports _meta/vault.md
_meta/
  vault.md                 the rules, one or two pages
  wiki.md                  the wiki rules
  frontmatter.md           base keys, then one short schema per note type
resources/playbooks/       one file per procedure, flat; README.md is the convention
resources/wiki/            written only by the wiki playbooks
sources/                   add-only
projects/ areas/ resources/   zones; open to any session unless the zone says otherwise
_agent/
  tools/<name>/            one folder per tool, each with a README
  tasks/ + tasks.base      the vault's own task board
  sessions/  log.md        session notes and the log
  research/                research notes
  schedule/                scheduled legs
  kits.lock                which kits were taken, at what version, with file hashes
  archive/                 everything retired, moved not deleted
.claude/skills/
  vlt-playbook/            the entry-point skill for playbooks, and its index script
  vlt-research/ vlt-ingest/ vlt-query/ vlt-feedback/    thin named pointers at their playbooks
```

### The rules (`_meta/vault.md`)

One or two pages. It holds only:

- **Write boundaries.** PARA is open to any session. A zone's README may restrict writers. `sources/` is add-only: a tool or session may deposit, nothing edits afterwards. The wiki changes only through the wiki playbooks. `_vault/`, `new/` and `daily/` are the owner's: read on request, never written unasked. Maps of content are never edited by an agent.
- **Records.** A session that changes the vault by hand writes one session note and one log entry, and commits path-scoped. A scheduled leg commits what it wrote and writes neither.
- **Naming and link syntax**, briefly.
- **Honest reporting and grounding**, carried over in short form.
- **Where things live**, pointing at the playbook README and the tools README.

Everything partner-shaped in the 0.19 contract is cut: activation ritual, partner memory, capabilities, hand-offs, backlog, grooming and decay tables, durability and overlays, the structure map.

The `{logical-name}` path map is removed. Shipped files name literal default paths. A vault that wants a different path edits its own files.

### Frontmatter (`_meta/frontmatter.md`)

Base keys for every note, then a short schema each for: wiki page, research note, session note, playbook, task, zone README. Attestation keys are required on wiki pages and research notes only.

Opt-in review in PARA is one key, `review:`, on a document (`requested`, then `approved` set by the owner), or declared as a default in a zone README. A shipped base lists documents awaiting review. The exact key values are the builder's call.

### Playbooks, the extension point

Adopted from `{field-vault}`'s runbook convention, renamed. The convention is the folder's own `README.md`:

- One flat folder, one file per procedure, no nesting by domain.
- Frontmatter carries the index: `need:` (one line in the owner's words), `state:` (`live` or `dormant`), `domain:`, `tools:` (paths under `_agent/tools/`), `companion:` and `companion_of:`.
- Named body sections in a fixed order (Prerequisites, Commands, Procedure, Output, Schedule, Rules, Known gaps), each omitted when empty.
- The playbook is the single home of its rules and paths. Nothing restates them.
- One entry-point skill, `vlt-playbook`, prints the need-to-file table from frontmatter. An index script has a `--check` mode that fails on missing keys, an unknown domain, a missing tool path or an orphaned companion.
- The set of `domain:` values is vault-owned.

Every shipped procedure (ingest, query, research, supersede, consolidate, feedback, add-a-tool, task board, set up a zone) is a playbook. The playbook is the authority.

Four of them also get a named skill: `vlt-research`, `vlt-ingest`, `vlt-query` and `vlt-feedback`. Each is a thin pointer: a description that triggers it, and one instruction to read its playbook whole and run it. It restates no rule. These skills are seeded into the vault's `.claude/skills/` like every other kit file, so the vault owns them. A skill that stayed in the plugin could not be changed by the vault.

### Sources and ingest

The wiki is always traceable to a stored source. Ingest takes any of:

- a file already in `sources/`;
- a URL, which ingest first captures into `sources/` as a saved copy;
- anything a vault tool can turn into a source. The tool deposits its output in `sources/` and ingest proceeds from that file. `{field-vault}`'s YouTube transcriber is the model;
- an attested research note.

So `sources/` is add-only but open: a capture step or a tool may write there, and nothing edits a source afterwards. A vault adds a new kind of source by adding a tool and a playbook that deposits into `sources/`; ingest needs no change. How a URL capture is stored (format, naming, what metadata it records) is the builder's call.

### Tools

`_agent/tools/<name>/`, each with a README naming what it is, how to run it, and which playbooks use it. Outputs and data stores stay out of the tool folder. A playbook's `tools:` list is where a session looks first. Scheduled legs live in `_agent/schedule/` and call into tool folders.

### Zones and task boards

A zone is a PARA container with a README (what it is, optional writer restriction, optional review default), a `tasks/` folder and a `tasks.base`. The task-board kit is `{field-vault}`'s current `task-board` runbook, its task template and its base, generalised. The vault's own board is the same kit at `_agent/tasks/`.

### Checks in place of lint

No vault-wide lint. A kit may ship a small check beside its tool, in the style of the playbook index's `--check`. One runner executes every check a vault has. What the wiki kit checks (index agreement, supersession links, attestation present) is the builder's call, kept small.

### Kits

A kit is a set of playbooks, their tool folders, templates and an optional check, with a manifest mapping each shipped file to its vault destination.

| Kit | Holds |
|---|---|
| `core` | `_meta/vault.md`, `_meta/frontmatter.md`, the `CLAUDE.md` stub, the `vlt-playbook` skill and index, the playbook and tools READMEs, session-note and log templates, the check runner, the add-a-tool and feedback playbooks, the `vlt-feedback` skill |
| `wiki` | `_meta/wiki.md`; ingest, query, supersede and consolidate playbooks; the `vlt-ingest` and `vlt-query` skills; the wiki check |
| `research` | the research playbook, the `vlt-research` skill and the research-note schema |
| `task-board` | the task-board and set-up-a-zone playbooks, task template, base, the vault board |

### The module repo after

```
.claude-plugin/            the plugin manifest; the only install path
kits/<kit>/                files as they land in a vault, plus kit.yaml
skills/vlt-setup           seed a vault: copy the kits, write kits.lock
skills/vlt-pull            show a kit's changes since the lock; the owner takes or leaves each file
```

- **The plugin carries two skills and the kits.** Pull reads a kit's current version from the installed plugin copy.

- **Setup** never overwrites an existing vault file. Where one exists it shows the difference and leaves the vault's copy.
- **Pull** compares three things per file: the version recorded in `kits.lock`, the kit's current version, and the vault's copy. It reports unchanged, shipped-changed, vault-changed or both-changed, and applies only what the owner accepts.
- Everything else in `skills/` at v0.19.0 is removed from the branch and stays reachable at the `v0.19.0` tag.
- Removed with it: the governance bundle, overlays, the version handshake, enforcement declarations, the rule card, `tripwires.yaml`, the `vlt-vitals` hook, the four workflow scripts, the skill-manifest verifier, the config and help-csv merge scripts, `module.yaml` and the help registry.

The release is `v1.0.0`.

## Migration

### Module

Build 1.0 on a new branch from the current head. The kits' content is lifted from what `{field-vault}` already runs (the runbooks README, the pointer skill and index, the task-board runbook and its template and base) and from the 0.19 wiki and research skills, reduced to playbooks.

### Each vault

Out of the module's scope by the owner's ruling. The module ships no migration procedure and makes no assumption about a vault's state. It ships one short note, `COMING-FROM-0.x.md`, that lists what 0.19 installed into a vault (skills, workflows, the hook, the `_meta/` bundle, `_bmad` entries, partner folders and ledgers) and what, if anything, replaces each in 1.0. A session in the vault uses it as a map.

Beside it the module ships one procedure document, `FLATTEN-A-PARTNER.md`: `{field-vault}`'s flatten procedure, generalised (no domain or scheduler specifics, no lint step). It is a reference a vault session reads when retiring a partner. It is not a kit, not a skill, and setup does not copy it into a vault.

What the module must guarantee so a vault can migrate on its own terms:

- Setup runs safely in a vault that still has 0.19 installed. It never overwrites an existing file; where one exists it shows the difference and leaves the vault's copy.
- Nothing in 1.0 reads or depends on a 0.19 artifact, so a vault may remove the old machinery before, after or gradually.
- The flatten procedure is not shipped as a kit. A vault gets it only by reading the reference above.

### The factory

The eight-step cycle lifecycle exists to govern a governance bundle that no longer ships. It collapses to: a filing lands in `factory/inbox/`, a change is made on a branch, a package check runs, the release is tagged and noted in `CHANGELOG.md`. Cycle 16 closes with a note that 1.0 supersedes it. Open inbox filings about removed machinery are closed in one pass with one note. `factory/` history stays where it is.

## Constraints

- The module repo is public. No machine paths, usernames or vault paths in tracked files.
- Vault-grown content is never destroyed, in migration or by setup or pull.
- Setup must be safe to run in a vault that still has 0.19 installed.
- Module development happens in the module repo only.

## Left to the builder

- The kit manifest format and the `kits.lock` format.
- How pull presents a diff and records an accepted file.
- The exact reduced text of `vault.md`, `wiki.md` and `frontmatter.md`, within the page budgets above.
- Which wiki checks ship.
- Which factory skills under `.claude/skills/` are kept, slimmed or removed.
- The exact contents of `COMING-FROM-0.x.md` and the generalised text of `FLATTEN-A-PARTNER.md`.

## Calls made by the designer (confirmed by the owner on approval)

- **Proposing a wiki change.** A session that is not running a wiki playbook files a task on the vault board. It does not write a proposal file.
- **Attestation without a Librarian.** `verified_by` names the playbook that wrote the page. An agent sets `trust: draft`; only the owner raises it.
- **Data stores.** A tool's database, snapshots and derived files live in `_agent/stores/<name>/`, not in the tool folder. Tests live with the tool.
- **A domain engine is one tool.** A multi-script engine is one folder under `_agent/tools/`, with its own sub-folders.
- **Kits are not optional pieces.** A vault takes all four. `core` names no rule that lives in another kit; it points at `_meta/wiki.md`. There is no dependency system.
- **The module ships a map and one reference, not a migration** (see Migration). It runs nothing in a vault.
- **Cycle 16.** 1.0 branches from the current head. Filings about removed machinery close in one pass; the rest are re-read against 1.0 and kept or closed one by one.
- **The name.** Runbooks become playbooks.
- **The repo's name** still says "bmad-module". Renaming it is the owner's to do or not; nothing here depends on it.
