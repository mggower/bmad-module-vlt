# Vault (`vlt`) — a self-evolving cast of knowledge partners

A BMad module: a roster of distinct AI partners — a **Librarian** who tends the wiki, a
**Researcher** who pushes you to learn, and a **Creative** who turns curated knowledge into made
things — who share one living knowledge vault and can grow the roster themselves. Install it into a
vault (existing or fresh) and the cast grows itself.

- **What's in it:** 3 partner agents (`vlt-agent-librarian`, `vlt-agent-researcher`,
  `vlt-agent-creative`), 6 operations (`vlt-ingest`, `vlt-research`, `vlt-query`, `vlt-extract`,
  `vlt-lint`, `vlt-dispatch`), the self-evolution engine (`vlt-mint`) and its review gate
  (`vlt-review-council`), and the lifecycle pair (`vlt-setup`, `vlt-upgrade`) — **13 skills** in all.
- **Self-contained:** the governance bundle (operating contract + conventions + review-lens
  personas) ships inside `vlt-setup/assets/` and installs into each target vault at setup.

## Install

Vault is a standard BMad module, installed with the **BMad installer**. **The vault is the
project** — install Vault *into* each vault you want a cast for, and run setup there. There is no
external registry; one vault = one install.

Run the installer with the vault as your working directory, pointing `--custom-source` at this
module (a local path or its Git URL):

```bash
cd /path/to/your/vault

# from a local checkout of this repo:
npx bmad-method install --custom-source /path/to/bmad-module-vault --tools claude-code

# …or from GitHub, once published:
npx bmad-method install --custom-source https://github.com/<you>/bmad-module-vault --tools claude-code
```

Or run `npx bmad-method install` interactively and give it the source path/URL when prompted. A
**local path works — no GitHub required.**

The installer reads `.claude-plugin/marketplace.json`, copies the `vlt-*` skills into the
vault's `.claude/skills/`, and runs `vlt-setup`, which installs the governance bundle into the
vault's `_meta/`, writes a `CLAUDE.md` pointer, and scaffolds the partner + backlog layer. Setup is
**additive and non-invasive** — it only writes Vault's own config and never touches another
module's.

**Multiple vaults** (e.g. work + personal): install into each — that's the whole multi-vault story.
Each vault keeps its own cast, threads, and backlog. **Updating:** re-run the installer in a vault
to pull a newer module version; re-running `vlt-setup` refreshes registration (governance install
is skip-if-present, so local rule edits are preserved).

## Recommended companion (optional)

Vault is **standalone** — it degrades gracefully and never hard-requires another module. One
companion makes it *fuller*, and `vlt-setup` will tell you if it's missing:

- **`bmad-agent-builder`** (from the **BMad Builder / BMB** module) — only used by `vlt-mint`'s
  *deliberate, from-scratch* partner-minting path, for a richer persona-discovery interview.
  Without it, `vlt-mint` still mints partners and operations via its bundled in-flow templates — you
  just lose the guided interview. Install BMB (via the BMad installer or as a plugin) if you want
  it; `vlt-mint` picks it up automatically.
- **`bmad-brainstorming` / `deep-research`** — the Researcher reaches for these mid-flow when
  present; otherwise it proceeds with available web tooling and says so.

There is no way (and no need) to *force* these at install time: BMad's philosophy — and Vault's
design — is detect → warn → degrade, never block.

## A vault ≠ this repo

This repo is **module development**. A *vault* is whatever folder holds your knowledge wiki (e.g.
`~/Vaults/core`); you register its path during `/vlt-setup`, and the module provisions it. One
install Vault into each vault you want a cast for; each keeps its own wiki, partner threads, and backlog.

## Notable files

- `.claude-plugin/marketplace.json` — the plugin manifest; lists the 13 `vlt-*` skills the installer copies.
- `skills/` — the 13 `vlt-*` skills (the installable module).
- `skills/vlt-setup/assets/governance/_meta/` — the canonical governance bundle (pruned conventions, review-lens personas, operating contract) that `vlt-setup` installs into a vault. Edit the bundle here (single source).
