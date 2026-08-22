---
name: "vlt-setup"
depends_on: ["frontmatter@11"]
description: Sets up the Vault module in a vault — installs the governance bundle, scaffolds the partner layer, and registers the module config. Use when the user requests to 'install vlt module', 'configure Vault', or 'setup Vault'.
---

# Vault Module Setup

## Overview

Installs and configures the **Vault** module: it writes the module config, then **provisions this vault** (the project) so the partners (Librarian, Researcher) have a vault that already carries its own rules, conventions, review lenses, and partner scaffolding. Because Vault replaces a vault's bespoke `_meta` engine, setup is what makes the whole self-evolving pattern travel — install it into a fresh vault and that vault becomes ready for the cast.

Setup does two things:

1. **Config** — writes module + core settings to the shared `_bmad` config (the generic BMad mechanism, below).
2. **Vault provisioning** — verify this vault's structure, install the shipped governance bundle (`./assets/governance/_meta/` → `{project-root}/_meta/`), install the **dynamic workflows** (`./assets/workflows/*.js` → `{project-root}/.claude/workflows/`), write a minimal `CLAUDE.md` pointer, and scaffold the partner + backlog layer.

Config is written to three files:

- **`{project-root}/_bmad/config.yaml`** — shared project config: core settings at root plus a `vlt` section with metadata and any `vault_structure` overrides. User-only keys (`user_name`, `communication_language`) are **never** written here.
- **`{project-root}/_bmad/config.user.yaml`** — personal, gitignored settings: `user_name`, `communication_language`, and any module variable marked `user_setting: true`.
- **`{project-root}/_bmad/module-help.csv`** — registers the Vault capabilities for the help system.

Both config scripts use an anti-zombie pattern — existing entries for this module are removed before writing fresh ones, so stale values never persist.

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root (which *is* the vault root), not the skill root.

## On Activation

1. Read `./assets/module.yaml` for module metadata and variable definitions (the `code` field, `vlt`, is the module identifier).
2. Check if `{project-root}/_bmad/config.yaml` exists — if a `vlt` section is already present, this is an **update / reconfigure**; read any existing `vault_structure` overrides as defaults.
3. **Vault is installed by the BMad installer into this vault (the vault is the project), and `_bmad/` here belongs to this vault.** The installer copies the skills into `.claude/skills/` and may also write its **own** config — a root `_bmad/config.toml` and staging dirs (`_bmad/vlt/`, `_bmad/core/`). Vault setup is **strictly additive and non-invasive**: it writes only Vault's own files — the `vlt:` section, user settings, and Vault help rows in the **YAML** `config.yaml` / `config.user.yaml` / `module-help.csv` that the Vault runtime skills actually read — and it **never deletes or rewrites the installer's `config.toml`, the `_config/`/`core/` install manifests, or another module's config.** See *Config files in an installer-built vault* below and *Do Not Run Installer Cleanup*. If a `vlt` section already exists in `config.yaml`, treat this as an **update / reconfigure** (point 2).

If the user passes arguments (`accept all defaults`, `--headless`/`-H`, or inline values), map provided values to config keys, use defaults for the rest, and skip interactive prompting. The vault is this project, so provisioning needs no path input — it just runs against `{project-root}`. Always display the confirmation summary at the end.

## Config files in an installer-built vault

The BMad installer writes a root **`_bmad/config.toml`** plus per-module staging (`_bmad/vlt/config.yaml`, `_bmad/core/config.yaml`). The Vault **runtime** skills, however, load **`_bmad/config.yaml`** (the BMad-module convention this skill's scripts produce). So hold a clear stance:

- **`config.yaml` is authoritative for Vault.** It is what `vlt-setup` writes and what the partners/ops read — write it correctly and Vault works, regardless of the TOML.
- **Leave the installer's `config.toml` and staging dirs alone** — the installer owns them; don't reconcile or delete them. *(Known BMad wart, not Vault's to fix: the TOML and YAML can drift, and the installer's TOML may serialize `vault_structure` as `"[object Object]"`. Neither affects Vault, which reads `config.yaml`.)*
- **"Write core only if absent" means absent from `config.yaml` specifically** — not "present in the TOML or staging." If `config.yaml` lacks core keys (`output_folder`, `document_output_language`), collect/write them there even if the installer's TOML already has them; the runtime reads the YAML.

## Collect Configuration

Ask the user for values. Show defaults in brackets. Present values together so the user can answer once with only what they want to change. Never tell the user to "press enter" or "leave blank".

**Default priority** (highest wins): existing new config values > legacy config values > `./assets/module.yaml` defaults.

**Core config** (only if no core keys exist yet): `user_name` (default: BMad), `communication_language` + `document_output_language` (default: English — one language question, both keys get the answer), `output_folder` (default: `{project-root}/_bmad-output`). `user_name` and `communication_language` are written exclusively to `config.user.yaml`; the rest go to `config.yaml` root.

**Module config.** The vault *is* this project (`{project-root}`) — there is no vault registry to collect (you install Vault into each vault you want a cast for). There are two module variables; neither is prompted for in the normal flow:

- **`feedback_repo`** *(not prompted — materialized silently from the `module.yaml` default)* — the transport endpoint `vlt-feedback` posts field notes to (an `OWNER/REPO` slug for `gh --repo`). Setup writes the default into `config.yaml`'s `vlt:` section; a vault that files elsewhere overrides by editing `config.yaml` or at reconfigure. The filing shape itself is single-homed in the `vlt-feedback` skill's field-contract reference.

- **`vault_structure`** *(advanced — you usually won't change it)* — the map of `{logical_name → path-relative-to-project-root}` every skill resolves paths through. **Setup materializes the full default map into `config.yaml`** so the override mechanism is visible and editable in one place. **Read the canonical default map from `./assets/module.yaml` (`vault_structure.default`) — do not hand-transcribe the table below; `module.yaml` is the single source of truth.** Don't prompt for each path; merge any user override entries over the `module.yaml` defaults and write the complete map. The table below is **illustrative only** (authoritative copy is `module.yaml`):

   | Logical name | Default (relative to the project root) |
   | --- | --- |
   | `wiki` | `_agent/wiki/` |
   | `index` | `_agent/wiki/index.md` |
   | `research` | `_agent/research/` |
   | `sessions` | `_agent/sessions/` |
   | `specs` | `_agent/specs/` |
   | `log` | `_agent/log.md` |
   | `backlog` | `_agent/backlog.md` |
   | `partners` | `_agent/partners/` |
   | `capabilities` | `_agent/capabilities/` |
   | `conventions` | `_meta/conventions/` |
   | `overlays` | `_agent/conventions/` |
   | `personas` | `_meta/personas/` |
   | `contract` | `_meta/vault-operating-contract.md` |
   | `upgrade_ledger` | `_agent/upgrade-ledger.md` |
   | `archive` | `_archive/` |

## Write Files

Write a temp JSON file with the collected answers as `{"core": {...}, "module": {...}}` (omit `core` if it already exists). The `module` object **always carries `vault_structure`** — the full default map **read from `./assets/module.yaml` (`vault_structure.default`)** with any user overrides merged on top — so the resolved map is materialized into `config.yaml`, sourced from the one canonical place rather than transcribed. (The script itself now preserves any defined variable absent from the answers — existing config value, else the `module.yaml` default — and reports every removal, so a malformed payload is no longer destructive, only lazy; the full-map contract here is the belt, the script the suspenders.) Then run both scripts.

**Resolve paths and tooling first — two real traps:**

- **Use `uv run`, not bare `python3`.** The scripts declare PEP 723 inline dependencies (`pyyaml`); bare `python3` lacks pyyaml and exits with `Error: pyyaml is required`.
- **`{project-root}` is a literal token only in *config values* — not in these shell commands.** In the commands below it must be the **actual** vault root. The skill runs with the vault root as the working directory, so use `$ROOT="$(pwd)"`. Passing the literal string `{project-root}` to `--config-path` creates a junk directory literally named `{project-root}` and writes a broken config into it.
- **Anchor the scripts/assets to this skill's installed directory** — the working directory is the vault root, *not* the skill dir, so `./scripts/…` won't resolve. Use the **"Base directory for this skill"** shown at activation as `$SKILL`.

```bash
ROOT="$(pwd)"                            # the vault / project root (cwd at activation)
SKILL="<the Base directory for this skill shown at activation>"   # e.g. "$ROOT/.claude/skills/vlt-setup"

uv run --quiet "$SKILL/scripts/merge-config.py" \
  --config-path "$ROOT/_bmad/config.yaml" \
  --user-config-path "$ROOT/_bmad/config.user.yaml" \
  --module-yaml "$SKILL/assets/module.yaml" \
  --answers "$TEMP_FILE"

uv run --quiet "$SKILL/scripts/merge-help-csv.py" \
  --target "$ROOT/_bmad/module-help.csv" \
  --source "$SKILL/assets/module-help.csv" \
  --module-code vlt
```

(The scripts write `config.yaml`/`config.user.yaml`/`module-help.csv` with the literal `{project-root}` token preserved *inside config values* — only the path **arguments** above use the resolved `$ROOT`.)

**Do not pass `--legacy-dir`.** That flag makes `merge-config.py` read and then **delete** `{_bmad}/core/config.yaml` and `{_bmad}/{module}/config.yaml` as an installer-migration step. Vault has no legacy per-module staging to migrate, and in a shared `_bmad/` that `core/config.yaml` belongs to the base BMad install (`core`/`bmm`) — deleting it can break co-installed modules. Both scripts are anti-zombie for the `vlt` section / Vault rows only, so they're safe to re-run without legacy handling.

The merge writes core values at root **only if** you collected core answers (i.e. no core config existed yet); it never touches another module's section. A collected `vault_structure` map passes through to the config as YAML (it carries no result-template). If either script exits non-zero, surface the error and stop — and echo `module_keys_removed` (and any `module_keys_defaulted`) from `merge-config.py`'s result JSON in the confirmation summary: a removal the user never sees is a silent strip one layer up.

Run `uv run "$SKILL/scripts/merge-config.py" --help` or the same for `merge-help-csv.py` for full usage.

## Provision the Vault

This is the heart of Vault setup. It operates on **this project** — `{project-root}` is the vault root (called `{root}` below). For each step, resolve sub-paths through the structure map — an explicit `vault_structure` override wins, else the conventional default from the table above. Report what was created vs. already present.

### 1. Verify and seed the core state files (wiki, index, log)

- Confirm the `wiki` directory exists (`{root}/_agent/wiki/` by default); create it if absent.
- If `log` (`{log}`, `_agent/log.md` by default) is missing, **create it with its header** — the activation "read the `{log}`" step and `vlt-ingest`'s re-ingest grep both assume it exists; without it the read silently no-ops and the grep errors on a fresh vault:

  ```markdown
  # Operation Log

  _Append-only chronological record — one line per operation. See the operating contract's `{log}` format (`## [YYYY-MM-DD HH:MM] <type> (<partner>) | <summary> [→ <artifacts>]`)._
  ```

- If `index` (`{wiki}/index.md`) is missing, create an empty one — a fresh vault starts with no pages:

  ```markdown
  ---
  type: index
  created: <today YYYY-MM-DD>
  last_updated: <today YYYY-MM-DD>
  title: Wiki Index
  ---

  # Wiki Index

  _No pages yet. The Librarian populates this as sources are ingested._
  ```

- Do **not** touch existing wiki pages or an existing `index.md` — leave a populated vault as-is.

### 2. Install the shipped governance bundle

The module ships its governance at `./assets/governance/_meta/` (the pruned conventions, the review-lens personas, and the operating contract). Copy it into the vault **only where files are absent** — never clobber a vault's existing rules:

- Target: `{root}/_meta/` (verbatim copy of `./assets/governance/_meta/`). If the vault overrode the `conventions`, `personas`, or `contract` logical names to non-default locations, place those files at the override locations instead.
- For each of: `_meta/vault-operating-contract.md`, `_meta/conventions/{frontmatter,wiki-index,wiki-supersession,wiki-consolidation,extraction,spec,consult,write-verification,decision-log}.md`, `_meta/personas/{architect,skeptic,pragmatist,historian,moderator}.md` — if the file already exists in the vault, **skip it** (the vault's own version wins) and note the skip; otherwise copy it in.
- **`_meta/vault-rule-card.md`** (the ceremony's rule-card — **derived** from the shipped contract, marked by its `derived_from:` hash) is the exception to skip-if-present: it is **module-owned — overwrite it on every install/update** (the `.baseline/`/workflows posture below), because it must track the *shipped* contract, never a vault's edit of it. A vault-edited live contract is surfaced by the upgrade's `governance_divergence` report, not by this card.
- This is the engine Vault replaces: install the rules, conventions, and lenses — **not** any plugin/versioning/repackage machinery (that ceremony was deliberately dropped).

**Stash the stock baseline (durability — build-6).** After the conventions are placed, copy each **shipped** convention to `{overlays}/.baseline/{name}.md` (default `_agent/conventions/.baseline/`), creating the dir if absent. The baseline is the *stock reference* — what the module ships — so it is **module-owned: overwrite it to the current shipped version on every install/update** (like the workflows above), independent of the skip-if-present rule for the live base. It lets `vlt-lint` and `vlt-upgrade` tell a local hand-edit of a base convention (base ≠ baseline → should be an overlay or upstreamed) from a clean install (base == baseline). Also ensure the overlay zone itself exists: create `{overlays}/` (default `_agent/conventions/`) if absent — it holds vault-local `{name}.overlay.md` additions, which are **never** written or clobbered by setup (they are the vault's, append-only, durable).

**Stash the skill-asset manifest (durability — build-18; structural scope — build B7-2).** Conventions have the baseline above; the **shipped skill surface** needs the same divergence net so a local hand-edit of an installed skill asset isn't silently clobbered on upgrade. Once the shipped skills, workflows, and hooks are in place, write the **SHA-256 manifest** `{overlays}/.baseline/.skill-manifest` (one `<sha256>␉<path>` line per file, paths relative to the vault root) by running `verify-skill-manifest.py --write` — the manifest covers **every file the module ships into the vault**, derived by the script's structural walk, **never by a hand-kept scope list**: every file under each **shipped** `vlt-*` skill dir (shipped-ness is provenance-based, from the **module source's** skills dir — a locally-minted `vlt-agent-*`/`vlt-*` dir is never manifested), plus the installed module-owned extras under `.claude/workflows/` and `.claude/hooks/` (basenames from the shipped `assets/workflows/` and `assets/hooks/` trees). Worked consequence of the walk, not its definition: it covers each skill's `references/` and `scripts/` and the installed vitals hook — the surfaces a hand-kept enumeration once dropped. Like the baseline (and the workflows), the manifest is **module-owned: overwrite it to the current shipped versions on every install/update** — and the write reports `added`/`removed` vs any prior manifest; surface removals in the Confirm summary (a path that left the net must be seen, never silent). The manifest records **stock content — hashed from the module source tree for every source-provenanced path, live only where no source counterpart exists** (build B10-1) — so a local edit present at write time is *reported as divergence, never absorbed as the new baseline*, and the next upgrade's pre-flight compares against what the module shipped. The write-time report surfaces `diverged`/`sanctioned` (partition mechanics live in the script's docstring — single-home), and the write **refuses with the named error `version-skew`** when the source tree's `module_version` differs from the installed record's. `{overlays}/.skill-manifest.sanctioned` is the vault's sanction record (written by the sanctioning acts in `vlt-upgrade` Step 3, read by the script) — **`vlt-setup` never creates, writes, or clobbers it** (the overlay-zone posture above applied):

```bash
uv run --quiet "$SKILL/scripts/verify-skill-manifest.py" --write \
  --root "$ROOT" \
  --live-skills-dir "$ROOT/.claude/skills" \
  --source-skills-dir "<the module source's skills/ dir>" \
  --overlays-dir "$ROOT/<resolved {overlays}>"
```

(`--overlays-dir` also derives the sanction-record default, `{overlays}/.skill-manifest.sanctioned` — pass `--sanctioned` only to override it.)

`--source-skills-dir` is the shipped-ness provenance: on an upgrade's provision hand-off the module source is in hand — pass its `skills/` dir; on a fresh install the just-installed live skills dir is verbatim the shipped set, so it serves as the source. On a later re-run with no reachable source, it serves again **only if no locally-minted `vlt-*` dir exists in the live dir** — provenance comes from the module source, never a mint. Whenever the live dir serves as the source, the write reports `source_mode: live` and a **loud warning that the net is live-hashed for that write** (blind to any pre-existing local edit) — surface that warning in the Confirm summary, never swallow it.

### 2a. Install the dynamic workflows

The module ships **dynamic workflows** at `./assets/workflows/` that the skills invoke via `workflow('<name>', …)`, which resolves from `{project-root}/.claude/workflows/`:

- **`vlt-review-council.js`** — the review-council panel engine (`vlt-mint` gates a mint with it; the `vlt-review-council` SKILL runs a debate through it).
- **`vlt-lint-full.js`** — the fan-out wiki health-check (`vlt-lint` delegates a large `--full` sweep to it).
- **`vlt-consult.js`** — the synchronous partner→partner consult engine (`vlt-dispatch`'s `consult` mode invokes it).

Install all of them:

- Copy every `*.js` in `./assets/workflows/` → `{root}/.claude/workflows/`. Create `{root}/.claude/workflows/` if absent.
- These files are **module-owned, not user-authored** (unlike `CLAUDE.md`): **overwrite them on every install/update** so a re-run refreshes the engines to the shipped versions. (They carry no user state — they read live `{personas}`/`{wiki}` at run time and return findings/verdicts the caller captures.)
- The workflows read the **live** vault files at run time (the caller passes resolved absolute paths), so the governance bundle above must be installed for the council to field any lenses — if `_meta/personas/` is missing, `vlt-review-council` degrades to a "no lenses available" verdict.

### 2b. Install the enforcement kit

The kit is three provisioned surfaces — the vitals reader (module-owned code), the tripwire registry seed (vault-grown after seeding), and the SessionStart strip hook registration:

- **Copy `./assets/hooks/vlt-vitals.py` → `{root}/.claude/hooks/vlt-vitals.py`** (create `{root}/.claude/hooks/` if absent). This file is **module-owned, not user-authored — overwrite it on every install/update**, exactly like the workflows above (`{root}/.claude/hooks/` is the module-owned code home beside the `.claude/workflows/` force-reinstall precedent; the vault never edits it). It is stdlib-only Python, read-only, derive-only. **Clobber-legibility floor:** before overwriting an *existing* `{root}/.claude/hooks/vlt-vitals.py`, compare it to the incoming file **by checksum (`sha256`) or a real line differ — never a bare `diff` invocation** (a shell-wrapped `diff` fails toward "no divergence", the dangerous direction). Identical → overwrite silently as today. Different → still overwrite (module-owned stands; this is a floor, not a preserve path) but **quote the differing content into the provisioning notes first** and mark the refresh as *overwrote local edits* for the Confirm line. On an upgrade (`vlt-upgrade` Step 6's provision hand-off) the quoted content reaches the upgrade ledger's Notes line by the existing "name the report's entries here when non-empty" mechanism.
- **Seed `{tripwires}`** (default `_agent/tripwires.yaml`) from `./assets/tripwires.yaml` — **skip-if-present with merge-by-id**: if the registry is absent, copy the seed whole; if present, add **only** ship-seeded wires whose `id` is absent from the vault's file. **Local thresholds win; local wires are never dropped or rewritten** — and the vault's `local_metrics:` declarations are vault-grown state exactly as local wires are: never dropped, rewritten, or reordered by seeding (the seed ships none, so the merge has nothing to add there) — the registry is vault-grown state (the mint-zone never-clobber posture in §4, applied). Note the merge result (seeded whole / N wires added / all present) for the report.
- **Register the SessionStart strip hook in `{root}/.claude/settings.json`** by **idempotent JSON merge keyed on the command path**. The hook entry to ensure (under `hooks.SessionStart`, the standard hooks shape):

  ```json
  { "hooks": [ { "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/vlt-vitals.py\" --strip" } ] }
  ```

  Create the file and the `hooks`/`SessionStart` keys if absent (preserving all existing content). Append this entry **only if no existing SessionStart entry's command already contains `vlt-vitals.py`** (the script path is the idempotency key — key on the bare path, not path-plus-flags: quoting between path and flags would defeat a longer substring) — and **never touch, reorder, or rewrite unrelated hooks**: a vault-local SessionStart hook must survive **byte-identical**. Re-running is a no-op. (The strip prints at most one line — tripped wires only, nothing when green, `vitals unavailable (<reason>)` on reader failure; a machine without `python3` degrades to the hook printing only its own error line — loud, never silent-green.)
- **Create `{lint_reports}`** (default `_agent/lint-reports/`, empty dir) if absent — `vlt-lint` persists its dated Step-5 reports there (plain `.yaml`). Same never-clobber line: existing reports are the vault's, append-only, untouched.
- **Create `_agent/upgrade-reports/`** (literal path, no `vault_structure` key — see the operating contract's zone-map row) if absent — `vlt-upgrade` persists its dated Step-4 reports there (plain `.yaml`; the upgrade also creates it lazily). Same never-clobber line: existing reports are the vault's, append-only, untouched.

### 3. Write the `CLAUDE.md` pointer

- If the vault root has **no** `CLAUDE.md`, write a minimal one that points a generic agent at the operating contract **and carries the `## Preferences` home** (the single source of truth for user-level tool/workflow prefs — see the contract's *User preferences*):

  ```markdown
  # Vault

  This vault is tended by the **Vault** BMad module — a cast of partners (Librarian, Researcher)
  who share this wiki. The operating rules live in `_meta/vault-operating-contract.md`; read it
  before writing anything. The conventions every write obeys are in `_meta/conventions/`.

  Summon a partner by name (e.g. "Librarian, ingest this") or run the operation skills directly.

  ## Preferences

  _User-level tool and workflow preferences — the single home, auto-loaded for every partner and
  headless op (e.g. "use the Tavily MCP for web search"). Empty until you set one._
  ```

- If a `CLAUDE.md` **already exists**, do **not** overwrite it — it is the user's file; only make additive, heading-scoped edits:
  - Offer to append a one-line pointer (`See \`_meta/vault-operating-contract.md\` for the Vault operating rules.`) if it doesn't already reference the contract.
  - **Append a `## Preferences` heading only if one is absent** (with the same placeholder line); if a `## Preferences` section already exists, leave its contents untouched. Never rewrite existing content — this keeps the never-clobber promise while still giving prefs a home.

### 4. Scaffold the partner + evolution layer

- Ensure `partners` (`{root}/_agent/partners/`) exists.
- **Upgrade migration (idempotent — finding from the partner-layer rework).** Before seeding, check each `{partners}/{partner}/` for a **legacy single `thread.md`** that carries all three sections (`## Bond` + `## Self` + `## Thread`). If found, split it into the two-file layout: move `## Bond` and `## Self` into a new `identity.md`, leave `## Thread` in `thread.md`, set both files' frontmatter `type:` accordingly. This is safe to re-run — a vault already on the two-file layout (an `identity.md` exists) is skipped. The split now also seeds `reflexes.md` if absent (the seed-if-absent pass below covers migrated partners the same as fresh ones). **Never discard relationship history** — migrate, don't reset.
- For each shipped partner — `librarian`, `researcher`, and `creative` — create the **three memory files if absent**, per the operating contract's *Partner memory* and `frontmatter.md` (never overwrite an existing file — it holds the relationship history; an existing populated `reflexes.md` is vault relationship history and is never touched):

  `{partners}/{partner}/identity.md` (evergreen):

  ```markdown
  ---
  type: identity
  partner: <librarian|researcher|creative>
  name:                              # the name the user gives this partner in this vault; empty until then (goes by role)
  created: <today YYYY-MM-DD>
  last_updated: <today YYYY-MM-DD>
  ---

  ## Bond
  _What I understand about you — preferences, style, tastes, boundaries. (Empty until we work together.)_

  ## Self
  _How I've come to carry myself in this vault — voice, tone, emphasis. (Empty; drifts as we go.)_
  ```

  `{partners}/{partner}/thread.md` (prunable):

  ```markdown
  ---
  type: thread
  partner: <librarian|researcher|creative>
  created: <today YYYY-MM-DD>
  last_updated: <today YYYY-MM-DD>
  ---

  ## Thread
  _Our open inquiry — stances taken, what we're circling, open questions. (Empty for now.)_
  ```

  `{partners}/{partner}/reflexes.md` (always-loaded — **seed if absent only**; body empty at birth, reflexes are earned by promotion):

  ```markdown
  ---
  type: reflexes
  partner: <librarian|researcher|creative>
  created: <today YYYY-MM-DD>
  last_updated: <today YYYY-MM-DD>
  cap: 30
  falsifier: "if a partner in ordinary use twice argues the cap rather than consolidating, or reflexes routinely exceed one line, the cap value (or the one-line form) is mis-set — file it"
  review_after: 2026-11-17
  ---

  _One line per rule — empty at birth; promoting one in at cap means editing one out or arguing the cap._
  ```

- Create the **vault rung** `_agent/reflexes.md` **if absent** (vault-scoped, fleet-wide — the always-loaded pointer layer every partner reads in Beat 1; see the operating contract, *Partner memory*, the vault rung). **Seed if absent only — never touch an existing populated file** (it holds the vault's grown rung):

  ```markdown
  ---
  type: reflexes
  scope: vault
  created: <today YYYY-MM-DD>
  last_updated: <today YYYY-MM-DD>
  cap: 30
  falsifier: "if a partner writes against an overlaid subject without the pre-act read after this rung named it, or a rung line carries rule content rather than pointing at the rule's home, the pointer shape is failing — file it"
  review_after: 2026-11-17
  ---

  _One pointer line per overlaid subject — empty at birth; written by overlay mints/amends and fleet-relevant promotions (contract, *Partner memory*); hand-adding a line is legal — this file is vault-owned._
  ```

- Create `backlog` (`{root}/_agent/backlog.md`) **if absent**. The backlog is a frontmatter-less structured checklist (per `conventions/frontmatter.md`) — do not give it YAML frontmatter:

  ```markdown
  # Backlog

  _What this vault wants to become. Any partner files here on noticing friction; building is deliberate._

  ## Open

  ## Done
  ```

- Ensure the **mint institutional-memory zone** `_agent/mint/` exists (it holds the resumable planning docs **and** `_agent/mint/decision-log.md` — both upgrade-durable in the agent zone). Create it if absent; never clobber existing contents. When `_agent/mint/decision-log.md` is **absent**, seed it from the shipped `$SKILL/../vlt-mint/assets/decision-log-template.md` (the sibling `vlt-mint` skill's asset) — **header only**: copy the template's header block (title, read-order statement, entry-shape + supersession notes) and drop the worked example below the `---`, which is documentation, not real history. This gives the log its defined shape and read-order statement from install-time. Preserve the never-clobber discipline: **seed only when absent; never overwrite an existing log.**
- Ensure the **capability family zone** `{capabilities}/families/` (default `_agent/capabilities/families/`) exists — it holds the cross-partner family contracts (Model B). Create it if absent; never clobber. Per-partner `{partners}/{name}/capabilities/` folders are **not** pre-created — they appear lazily when a partner grows or is given its first light capability.

### 5. Seed the generic-BMad installer cache (interop)

The generic BMad installer resolves an installed module's `module.yaml` **only from its own source caches** — never from the vault. vlt installed as a Claude plugin exists in no such cache, so every generic BMad run warns (`collectAgentsFromModuleYaml` / `writeCentralConfig`), the agent roster never reaches `config.toml`, and config answers mis-scope to team. Fix: seed the installer's custom-modules cache with a minimal resolvable stub — a `.claude-plugin/` marker dir (its presence is the repo-root marker; contents not needed) plus this skill's own `module.yaml` at the standard `skills/*-setup/assets/` probe path (the installer matches on the yaml's `code: vlt`):

```bash
if [ -d "$HOME/.bmad" ]; then
  BMAD_CACHE="$HOME/.bmad/cache/custom-modules/bmad-module-vlt"
  mkdir -p "$BMAD_CACHE/.claude-plugin" "$BMAD_CACHE/skills/vlt-setup/assets"
  cp "$SKILL/assets/module.yaml" "$BMAD_CACHE/skills/vlt-setup/assets/module.yaml"
fi
```

**Refresh (overwrite) the yaml on every run** so the cache tracks the installed version — a stale cache means a stale roster. **Graceful degrade:** if `~/.bmad/` doesn't exist, skip silently — that machine never runs the generic BMad installer, and vlt must not create the tree just for this. (`vlt-upgrade` reaches this step through its provisioning hand-off — the seed refreshes on every upgrade automatically.)

## Check Dependencies

Vault degrades gracefully without these — **warn, never hard-fail**. Check whether each is installed, and **count a host/global-provided skill as present** — a skill the partner can actually reach is *not* missing just because it isn't in the project's `.claude/skills/`. Look in `{project-root}/.claude/skills/` *and* consider host/global skills; if you can't confirm a host skill either way, report it as "not found in project skills (may be host-provided)" rather than a flat "missing". Note any genuinely absent ones in the confirmation summary:

- **`bmad-agent-builder`** *(recommended companion — part of the BMad Builder / BMB module)* — used by `vlt-mint`'s *deliberate* (from-scratch) partner path for richer persona discovery. Absent → `vlt-mint` still mints partners and ops via its bundled in-flow templates; you only lose the guided interview. If it's missing and the user wants the fuller path, tell them how to add it: install the BMB module (its `bmad-agent-builder` skill), e.g. via the BMad installer or by adding the BMB plugin, then re-run nothing — `vlt-mint` picks it up automatically next time. **Not required; never block setup on it.**
- **`bmad-brainstorming`**, **`deep-research`** (and any design-thinking skills) — the Researcher reaches for these mid-flow. Absent → the Researcher proceeds with available web tooling and says so. Optional; same install note applies.

### Machine-tool probe (both layers — report, never gate)

The machine-level toolchain gets the same warn-never-hard-fail treatment, over two layers:

1. **Module layer** — read `machine_tools:` from `./assets/module.yaml` (already read on activation; the declaration lives there, deliberately outside config.yaml — no per-vault override).
2. **Vault-grown layer** — walk `{partners}/*/capabilities/*.md` (resolve `{partners}` through the structure map; skip the archive zone) and collect every `requires:` entry (the birth record — schema + rule in `vlt-mint/assets/capability-template.md`). A fresh install with no partner zones yet probes the module layer only.

Probe each distinct tool with `command -v <tool>` — **presence only, never versions**. For each absent tool report one named line:

- `tool-missing: <tool>` — carrying the declaration's `needed_by:`/`absent:` text (module rows) or the owning `partner/slug` plus any parenthesized install hint (vault-grown entries).

**Report, never gate.** The legal response to a `tool-missing:` line is: install the tool per its hint, or accept the named degraded behavior — setup completes either way; the vault stays usable degraded. (This generalizes `vlt-feedback`'s `gh-missing` pattern to the whole declared set; `vlt-feedback`'s own exercise-time pre-flight is unchanged — arrival-time and exercise-time are complementary moments.)

**No web-tool check.** Web access is a host concern — the operation skills use whatever web tooling the host provides; setup ships and checks no web policy.

## Create Output Directories

After writing config, create any configured output directories whose value starts with `{project-root}/` (e.g. `output_folder`) and that don't yet exist — resolve `{project-root}` to the actual path for the `mkdir` only; the config values keep the literal token. (Vault sub-paths are handled in *Provision the Vault*, not here.)

## Do Not Run Installer Cleanup

**Skip the `cleanup-legacy.py` step.** It removes installer staging dirs under `_bmad/{module}/` after migrating their values into one config. In a Vault install that's both unnecessary and risky: Vault reads `config.yaml`, which `vlt-setup` writes directly (no migration needed), and the `_bmad/` here also holds the base BMad install's `core/` and `_config/` (install manifests) plus the installer's `config.toml`. Running cleanup — especially with `--also-remove _config` — would delete files the installer and `core` own. **Never do that.**

The `cleanup-legacy.py` script ships in the skill's `scripts/` only for parity with the BMad template; this skill does not invoke it. Leave the installer's staging (`_bmad/vlt/`, `_bmad/core/`) in place — the installer manages its own lifecycle.

## Confirm

Display what happened, using the script JSON output plus your provisioning notes:

- Config written — the `vlt` section (metadata + any `vault_structure` overrides), core values, user settings (`user_keys`), help entries, fresh-install vs. update.
- **Per vault provisioned** — for each: governance files installed vs. skipped (already present), the **dynamic workflows** (`.claude/workflows/*.js` — every workflow §2a ships) installed/refreshed, the **enforcement kit** (§2b: `vlt-vitals.py` installed / refreshed (identical) / **refreshed — overwrote local edits (diff preserved in the notes; a vault-local derive function does not survive here — a durable home for local metrics lands in a later release)**, `{tripwires}` seeded / merged (N wires added) / kept, SessionStart hook registration added / already-present, `{lint_reports}` created / present, `_agent/upgrade-reports/` created / present), `log.md` + `index.md` created or left, the `vault_structure` map materialized into `config.yaml`, the **skill-asset manifest** written (entry count, plus `added`/`removed` vs the prior manifest when one existed — removals always shown, **plus its write-time `diverged` (unsanctioned local edits preserved-and-reported, never absorbed) and `sanctioned` (N sanctioned divergences: paths) lines, and the live-hashed warning when `source_mode: live`** — always shown when non-empty), `CLAUDE.md` pointer + `## Preferences` written / appended / left, partner `identity.md`+`thread.md`+`reflexes.md` + the vault rung `_agent/reflexes.md` + `backlog` scaffolded vs. already present, and any **legacy `thread.md` → two-file migration** performed.
- **Dependencies** — any genuinely missing skills (not host-provided ones) and any `tool-missing:` lines from the machine-tool probe (declared module tools + capability `requires:` entries), each with its degrade note.
- **Installer TOML quirk (if present)** — if the installer's `config.toml` serialized `vault_structure` as `"[object Object]"`, acknowledge it in one line: a known BMad-installer serialization quirk that Vault **ignores** (the runtime reads `config.yaml`, which `vlt-setup` wrote correctly). Surfacing it here saves a future debugging detour.
- **Co-installed modules untouched** — confirm only the `vlt` section, user settings, and Vault help rows were written; no other module's config was read or removed.

Then display the `module_greeting` from `./assets/module.yaml`.

## Outcome

Once `user_name` and `communication_language` are known, use them for the rest of the session. Tell the user how to start: summon a partner by name ("Librarian, …" / "Researcher, …") in this vault, or run an operation skill directly. Re-run `vlt-setup` anytime to refresh the governance bundle or reconfigure.
