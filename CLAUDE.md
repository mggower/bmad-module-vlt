# vlt — the plugin's source repo

This repo is the **factory**: the development home of `vlt`, a Claude Code plugin that seeds a vault toolkit. It is not a vault. The **field** is any live vault the kits were seeded into (a separate project per vault). Plugin development happens **here only**; never "fix" a kit defect by editing a vault, and never treat what a vault changed or grew as plugin source.

@CLAUDE.local.md

## What ships

- **Two skills served by the plugin:** `skills/vlt-setup`, `skills/vlt-pull`.
- **Four kits** (`core`, `wiki`, `research`, `task-board`) under `kits/<kit>/files/`, each file at the exact path it has in a vault. `kits/<kit>/kit.yaml` carries the kit's version. The tree is the manifest; there is no file list to maintain.
- **One engine,** `scripts/kits.py` (seed, status, diff, take, leave), stdlib only.

The design is `docs/superpowers/specs/2026-11-18-vlt-toolkit-design.md`. Read it before changing what ships.

## The flow

1. **A filing lands** in `factory/inbox/` (see its `README.md`), written directly or materialised from a tracker issue by `issue-triage`.
2. **A change is made on a branch.** Ground the filing against current source first; filings regularly guess the wrong cause. Tests first (`uv run --with pytest pytest tests/ -q -p no:cacheprovider`).
3. **The package check passes:** `python3 tools/package-lint.py --expect-version X.Y.Z`, exit 0.
4. **The release is tagged and noted in `CHANGELOG.md`** (`vlt-release`): the plugin version and every kit's version move together, the lint's PASS line goes in the release commit, then ff-merge to `main`, an annotated tag, and a push on the owner's word.

Cycles, roadmaps, briefs, roundtables and acceptance ledgers ended with Cycle 16 (closed 2026-11-18 as superseded by 1.0). `factory/cycles/`, `factory/platform/`, `factory/studies/` and `factory/method/` are history: read them, never append to them.

## Standing rules

- **The vault owns every seeded file.** Nothing the plugin ships may overwrite or delete a vault file the owner has not accepted, and no rule may live where a vault cannot change it. A rule goes in a kit file, never in `skills/vlt-setup` or `skills/vlt-pull`.
- **Every procedure a session runs is a playbook** (`kits/*/files/resources/playbooks/`). There is no second mechanism. A named skill in a kit is a pointer at its playbook and restates nothing; the lint holds it to 15 lines.
- **No persona, role, mode, memory or ritual** in anything shipped. The lint fails on the word "partner" in `kits/`.
- **Page budgets:** `_meta/vault.md` 120 lines, `_meta/wiki.md` 120, `_meta/frontmatter.md` 150. A rules file that needs a summary is too long.
- **Single home.** A rule or a path is stated in one file; everything else points at it. Lists that claim completeness drift; prefer pointing at the folder.
- **Seeded Python is stdlib only** and finds the vault from its own location.
- **No bytecode or other cruft on disk in the shipped surface** (`skills/`, `kits/`, `scripts/`, `.claude-plugin/`). The plugin is installed as a file copy, so what is on disk ships.
- **Commit at every milestone,** in the session that made the change. One commit per finished piece of work; never push unless asked.

## Git and publishing

- This is a public repo, **factory included**. Tracked and public: `skills/`, `kits/`, `scripts/`, `.claude-plugin/`, `tools/`, `tests/`, `docs/`, `factory/`, the two factory skills under `.claude/skills/`, `.github/`. Gitignored and local-only: `.claude/skills/bmad-*`, `_bmad/`, `_output/`, `.vscode/`, `CLAUDE.local.md`, `**/.decision-log.md`.
- **No personal or vault-local information anywhere tracked.** Machine paths, the owner's username or first name, and a field vault's real path stay out; use `{field-vault}`, "the owner", `~`. Machine and personal specifics live only in `CLAUDE.local.md`. The one deliberate exception is the author block in `.claude-plugin/marketplace.json`.
- **Examples in kit files use placeholder paths and generic domains,** never a specific vault's artifacts.
- `.github/ISSUE_TEMPLATE/` is the tracker's half of the feedback contract (`kits/core/files/resources/playbooks/feedback-field-contract.md`). Change the two together.

## What not to touch

- `.claude/skills/bmad-*` — installed BMad tooling. It is upstream's; defects in it are filed upstream, not patched here.
- Live vaults — read them freely for grounding; write fixes only as plugin source here.
- Tags `v0.4.0` to `v0.19.0` and the `factory/` history — the record of 0.x.
