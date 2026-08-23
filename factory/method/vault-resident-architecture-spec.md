---
title: Spec — Move Vault to a Vault-Resident Architecture (Model B)
status: accepted
created: 2026-06-01
last_updated: 2026-06-01
module: vlt
supersedes_sections: ['vault-module-plan.md → Configuration', 'vault-module-plan.md → Two-vault reality', 'vault-module-plan.md → Integration (portability)']
---

# Spec: Vault-Resident Architecture (Model B)

## Resolution (confirmed 2026-06-01)

**ACCEPTED — standard BMad, vault-resident.** Per the BMad distribution docs
(`bmad-builder-docs.bmad-method.org/how-to/distribute-your-module`), the install path is the **BMad
installer** (`npx bmad-method install --custom-source <path-or-url> --tools claude-code`, run with
the vault as CWD), which reads `.claude-plugin/marketplace.json` (**required, at repo root**) and
copies the skills into the vault's `.claude/skills/`. So:

- **The `marketplace.json` stays** (it's the required BMad manifest, not bespoke) — moved to repo
  root with `./skills/vlt-*` paths.
- **The `vaults` registry / `default_vault` is the bespoke part that goes** — install per vault.
- The earlier Claude Code `/plugin install` attempt + the manifest being at `skills/.claude-plugin/`
  (wrong location) is the likely source of the first-run install friction.
- All four open questions below are resolved by this model (see the conversation / the table in the
  README). The variant debate (B1 plugin-scope vs B2 copy) is moot: the BMad installer copies skills
  into the vault, which is the "B2/standard" outcome.

## The decision

Make **the vault itself the project**. Install the `vlt-*` skills and the `_bmad` config *into*
`{vault_root}`, so opening the vault as your Claude Code working directory gives you the cast,
the rules, and the knowledge all in one place — the way bmad installs into the repo it operates on.

This replaces the current **Model A** ("external skills + a `vaults` registry; one install points at
many vaults from a distance").

## Why (the case, in short)

The module already keeps *all content/memory* in the vault (wiki, research, sessions, `log`,
`backlog`, per-partner `thread.md`, the `_meta/` governance). Model B extends that line to the
*tool* itself, which:

1. **Makes "different vault = different person" total** — not just memory diverges per vault, the
   roster and ops can too.
2. **Fixes a real wrinkle.** Today `vlt-mint` installs minted skills into the *host project*
   (`bmad_builder_output_folder` = `{project-root}/skills`), so a "work-vault Codebase Partner" is
   actually a **global** skill that merely lacks a `thread.md` elsewhere — contradicting the plan's
   "the roster can differ per vault." Vault-resident mint makes per-vault rosters **real**.
3. **Matches how a vault is actually used** — you open the vault folder and work *in* it, rather
   than opening a separate control project and reaching into vault paths by name.
4. **Removes the shared-`_bmad` hazard** (the installer-cleanup bug from 2026-06-01): a vault's
   `_bmad/` is its own, not shared with `bmm`/`core`.

## The trade-off being accepted

- **Cost:** updating the module means re-syncing **N vaults** instead of one deployment. With the
  plugin this is cheap (re-install per vault), but it is N, not 1. Governance refresh needs an
  explicit update path (see Open Questions).
- **Multi-vault (work + personal):** served by **installing into each vault**. No registry, no
  cross-contamination, true divergence — at the price of per-vault installs.

## What changes, component by component

### 1. Config schema (`vlt-setup/assets/module.yaml`)
- **Remove** `vaults` (the registry) and `default_vault` — there is exactly one vault: this project
  (`{project-root}`). The whole "select a vault" indirection goes away.
- **Keep** `vault_structure` as optional layout overrides, now plainly "paths relative to the
  project root." Default map unchanged. Common case: unset (all defaults), so the `vlt` config
  section is often just metadata.
- Tweak `description`/greeting to "installs into your vault."

### 2. `vlt-setup/SKILL.md`
- **Collect Configuration:** drop the vault-registry loop and `default_vault`. Optionally collect
  `vault_structure` overrides. Core config unchanged.
- **Provision:** operate on `{project-root}` directly (it *is* the vault). One vault, no "for each
  vault in registry" loop:
  - verify/seed `wiki` + `index.md`
  - install governance → `{project-root}/_meta/` (skip-if-present)
  - write the `CLAUDE.md` pointer (never clobber)
  - scaffold `partners/{librarian,researcher}/thread.md` + `backlog.md`
- Keep the dependency checks and the additive/non-invasive posture (still correct, lower-stakes now).

### 3. The 9 operating skills (2 agents, 5 ops, `vlt-mint`, `vlt-review-council`)
- Replace every "resolve the target vault (named by caller, else `default_vault`) from the `vaults`
  registry" passage with: **"resolve paths relative to `{project-root}` via `vault_structure`
  (override wins, else default)."**
- Remove the `{vault}` args/prompts from the agents and ops (no vault to choose).
- Net effect: these skills get **simpler** — the config-indirection layer largely disappears.

### 4. `vlt-mint` (the key beneficiary)
- Install minted skills into **`{project-root}/.claude/skills/vlt-{op|agent-name}/`** (the vault's
  own active skills dir), not `{project-root}/skills`.
- Register the capability into the **live** `{project-root}/_bmad/module-help.csv`; scaffold the new
  partner's `thread.md` in-vault. Per-vault roster divergence becomes the natural default.
- The shipped `vlt-setup/assets/module.yaml` + `module-help.csv` remain the **baseline manifest**
  (the core 10 skills); per-vault mints extend the *live* registry, not the shipped baseline.

### 5. `module-help.csv` (shipped baseline)
- Drop the `{vault}` args on agent/op rows.
- `output-location`: from `default_vault` → vault-relative (`{project-root}` / the structure-map
  target). `vlt-mint` → `{project-root}/.claude/skills`.

### 6. Distribution (`marketplace.json`, `README.md`)
- Install target = **the vault folder as CWD**: `/plugin marketplace add …` → `/plugin install
  vlt@vlt` → `/vlt-setup`, all run from within the vault.
- Multi-vault = repeat per vault. Document this as the intended pattern (it replaces the registry).

### 7. The plan doc (`skills/reports/vault-module-plan.md`)
- Revise **Configuration** (kill the registry; `vault_structure` becomes project-root-relative),
  **Two-vault reality** (install-per-vault, not point-at-many), and **Integration → portability**
  (the unit that travels is now the vault, skills included).

### 8. Operating contract (`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`)
- Structure-map section: "relative to the vault root" == "relative to the project root."
- Note `.claude/` and `_bmad/` as **tool zones** (alongside the existing human zones), analogous to
  `.obsidian/` — not content, gitignore-able. (`.claude/` is hidden in Obsidian; `_bmad/` shows but
  fits the existing underscore-dir convention.)

## Migration for the already-installed `vlt-core`

Low effort — most of the vault is already provisioned:
1. Install the `vlt-*` skills into `vlt-core/.claude/skills/` (plugin install or copy, with the
   vault as CWD).
2. Run `/vlt-setup` from inside `vlt-core` — governance, threads, and backlog already exist there
   (from the earlier Model-A provisioning), so skip-if-present makes this a near-noop; it just
   writes the trimmed `vlt` config (no registry) into `vlt-core/_bmad/`.
3. Remove the old Model-A `vlt` config + skills from the former host project if no longer wanted.

## Open questions (resolve before/within implementation)

1. **Mint persistence across updates.** A plugin re-install must not wipe vault-local mints. Likely
   fine if updates only re-deploy the core 10 skill folders and leave additional `vlt-*` folders
   alone — but confirm the plugin update semantics, or keep mints in a sibling dir.
2. **Governance refresh.** Skip-if-present means `vlt-setup` won't update an improved
   contract/convention in an existing vault. Add an explicit `--update-governance` (or a version
   stamp + diff-on-update) so shipped-rule improvements can propagate without clobbering local edits.
3. **Does any `vlt` config remain in the common case?** With defaults, possibly nothing but
   metadata. Confirm bmad-help/agents tolerate an essentially-empty `vlt` section.
4. **Roster source of truth at runtime.** Confirm the active roster is "which `vlt-agent-*` skills
   exist in `.claude/skills/`" (so a vault-local mint is real) vs. anything that reads the shipped
   `module.yaml agents[]`.

## Rollout (if approved)

1. Land config-schema + `vlt-setup` changes (single-vault provisioning).
2. Sweep the 9 skills' path-resolution language; repoint `vlt-mint`'s install target.
3. Update `module-help.csv`, `marketplace.json`, `README.md`.
4. Revise the plan doc + operating-contract notes.
5. Re-run VM; migrate `vlt-core` as a live test.

Estimated as a focused but broad edit pass (touches all 10 skills + 4 docs); no new scripts needed —
it mostly *removes* indirection.
