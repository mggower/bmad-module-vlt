---
title: 'Build #13 — BMad installer interop (module.yaml resolvability + CSV header canon)'
status: 'BUILT 2026-07-03 (commit a27b6cc on arc2-v0.5.0) — 17 unit checks pass; F1 verified end-to-end against the real installer resolver (sandboxed HOME). Build deviations from brief: (1) seed is a MINIMAL STUB (.claude-plugin/ marker dir + module.yaml only), not a full source copy — sufficient for both warning sites and available even when no repo checkout exists on the machine; (2) seed single-homed in vlt-setup Provision §5 (vlt-upgrade inherits via its Step-3.6 provisioning hand-off, honoring "never reimplement vlt-setup") rather than duplicated in both skills. Live acceptance (zero warnings on a generic BMad run against vlt-core) rides the next upgrade.'
module_code: 'vlt'
created: '2026-07-03'
derives_from:
  - 'inbox/2026-07-03-120000-bmad-installer-interop-warnings.md (A2-3)'
roadmap: 'skills/reports/inbox-evolution-arc2-roadmap.md'
risk: 'low-moderate — one small live-vault migration (CSV header rename-in-place, B1-safe); one write into the BMad cache (graceful-degrade)'
---

# Build #13 — BMad installer interop

Goal: a generic BMad install/upgrade run against a vault with vlt installed emits **zero**
vlt warnings, the agent roster reaches `config.toml`, and nothing vault-local is disturbed.
Posture per the standing ruling: install the BMad way, no bespoke; `vlt-upgrade` owns
durability across the change.

## F1 — make vlt's `module.yaml` resolvable to the installer

### Spike record (CLOSED 2026-07-03 — read the installer source, npx cache `bmad-method`)

`resolveInstalledModuleYaml(moduleName)` (`tools/installer/project-root.js:102`) searches,
in order: (1) built-in `src/modules/<name>/module.yaml`; (2) `~/.bmad/cache/external-modules/<name>/`;
(3) `~/.bmad/cache/community-modules/<name>/`; (4) the same-run custom-module resolution
cache; (5) `~/.bmad/cache/custom-modules/` — walking every cached repo root (identified by
`.bmad-source.json` **or `.claude-plugin/`**), enumerating all `module.yaml` candidates, and
matching the yaml's `code` **or** `name` against the module name. Within each root the
candidate probes include **`{root}/skills/*-setup/assets/module.yaml`** (the "BMB standard"
probe, `project-root.js:126–138`).

**Root cause:** vlt's layout and identity are already conformant — `skills/vlt-setup/assets/module.yaml`
matches the `*-setup` probe and `code: vlt` matches the lookup. The warning fires because
**vlt exists in no BMad cache**: it was installed as a Claude plugin from GitHub, entirely
outside the installer's source-acquisition machinery (`external-modules/` holds only
bmb/cis/tea; `community-modules/` and `custom-modules/` are empty). The installer sees
`vlt` registered in the vault's `_bmad/` but has no source to read the yaml from. The
filing's guessed fix (`_bmad/vlt/module.yaml`) is a non-location — no module, canonical or
otherwise, keeps it there, and the installer never looks in the vault.

### Fix (recommended): seed + reconcile the custom-modules cache

Make `vlt-setup` (fresh install) and `vlt-upgrade` (reconcile step) ensure a current copy of
the module source exists at **`~/.bmad/cache/custom-modules/bmad-module-vlt/`**. This is not
bespoke: that cache is exactly where the installer itself would have placed vlt had it been
installed via the BMad custom-module URL path — we are reproducing the installer's own end
state, using its own discovery rules.

Mechanics:
- The cached copy must contain the **repo-root marker** (`.claude-plugin/` — vlt ships
  `marketplace.json` there, and the walker accepts that marker) plus
  `skills/vlt-setup/assets/module.yaml`. A full copy of the acquired module source (which
  `vlt-upgrade` already has in hand at acquire time) is simplest and fine.
- **vlt-upgrade** refreshes it during reconcile (so the cache tracks the installed version —
  stale cache = stale roster). **vlt-setup** seeds it on fresh install if absent.
- **Graceful degrade:** if `~/.bmad/` doesn't exist, skip silently — that machine never runs
  the generic BMad installer, and vlt must not create the tree just for this.
- Record the seed/refresh in the upgrade ledger line (it's part of the vault's evolution).

Rejected alternatives: (a) placing `module.yaml` in `_bmad/vlt/` — installer never looks
there; (b) renaming the setup skill — name already conforms; (c) switching vlt's install
story to the BMad custom-URL path — a distribution-channel decision, not a defect fix; note
it in the README as an alternative install route if ever desired, out of scope here.

### What F1 unlocks (verify at acceptance)
- `collectAgentsFromModuleYaml` writes the three shipped partners to `config.toml` —
  including the **empty-string `name` fields** (the First-Breath convention: roster UIs fall
  back to `title` until the owner sets `[agents.<code>] name = "…"` — Build #1's naming
  ceremony config half finally reaches its intended surface).
- `writeCentralConfig` scopes vlt's answers per `module.yaml` instead of defaulting to team
  scope (today only `vault_structure`, but the standing scope bug closes).

## F2 — CSV header to canon (`after,before` → `preceded-by,followed-by`)

Sites that move together (grounded; vlt-mint's always-quote prose at `SKILL.md:142` does
**not** name the two columns, so no prose site):
1. `skills/vlt-setup/assets/module-help.csv:1` — the shipped header.
2. `skills/vlt-setup/scripts/merge-help-csv.py:36–37` — the canonical-header list entries.
3. **Read-side migration (the wrinkle that makes this a build, not an edit):**
   `merge-help-csv.py:291` prefers the target's existing header (`target_header if
   target_header else source_header`), so renaming the source alone never fixes a live
   vault. Add to the merge script: when the **target header is the known-old variant**
   (exact match on the 13-column `after,before` form), rewrite the header line in place to
   canonical before merging — rows are positionally identical, so data is untouched.
   Report the migration in the script's JSON output (e.g. `header_migrated: true`) and let
   `vlt-upgrade`'s post-flight divergence report surface it. Any *other* unknown header
   still follows the existing behavior (no blind rewrites).
   **B1 rule holds:** local-mint rows (vlt-core: chef, dog-trainer, health-coach, retired
   local vlt-track) pass through the rewrite untouched — the header migration must run
   *before* row parsing so `filter_rows_preserving_local` and the build-10 malformed-row
   skip/report operate on the canonical schema.
4. Unit tests: old-header target migrates + merges + preserves local mints; canonical target
   unchanged; fresh-install (no target) writes canonical; malformed-row skip (build-10 #3)
   unregressed.

## Out of scope (dispositioned)
- **bmad-module-builder template drift** — the split (template assets CSV canonical, but
  template `merge-help-csv.py:36–37` + scaffold tests still `after,before`) exists in the
  **latest upstream BMB** (verified in `~/.bmad/cache/external-modules/bmb` 2026-07-03), so
  neither upgrading BMB nor fixing our installed copy resolves it durably — **file upstream
  to BMAD-METHOD** (owner action; sibling of this build, not part of it). vlt's F2 fix
  stands alone either way.
- Switching vlt's distribution to the BMad custom-URL install path (note-only).

## Verification (unit, at rest)
- Header canonical in shipped CSV + script constant; migration branch unit-tested per the
  four cases above; cache-seed step present in both vlt-setup and vlt-upgrade with the
  no-`~/.bmad` degrade; no other skill references the old column names (grep).

## Acceptance (live, next vlt-core upgrade + one generic BMad run — ledger in Arc 2 roadmap)
- Run any generic BMad install/upgrade against vlt-core after the vlt upgrade: **zero** vlt
  warnings (both `module.yaml` warns gone, no header warning).
- `config.toml` carries the vlt agent roster (3 partners, `team = vlt`, empty names
  tolerated); vlt-core's live `module-help.csv` header is canonical **with all four
  local-mint rows intact**; `_agent/upgrade-ledger.md` records the migration + cache seed.
