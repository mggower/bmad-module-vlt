---
title: Vault Module — Testing Feedback
status: active
created: 2026-06-01
last_updated: 2026-06-01
module: vlt
module_version: 0.1.0
---

# Vault Module — Testing Feedback

A running log of friction, bugs, and ideas found while dogfooding the `vlt` module. The goal is to
capture **as I go** (cheap, never lose a thought), then triage into action later.

## Test context

| | |
| --- | --- |
| Module version | 0.1.0 |
| Install method | `/plugin install vlt@vlt` (local marketplace) — _note the fix that made it work here_ |
| Vault under test | `{field-vault}` |
| Vault state | fresh / existing — _fill in_ |

## How to use this doc

1. **Capture freely** — drop anything into _Open_ the moment you hit it. One line is fine.
2. Tag each item with an **area** (which skill) and a **kind**, mirroring the module's own backlog:
   - `bug` — it does the wrong thing or errors
   - `friction` — it works but is clunky / surprising / slow
   - `capability-gap` — something it can't do that you wished it could
   - `idea` — an enhancement worth considering
3. When an item is acted on, move it to _Resolved_ with a one-line note on how.
4. **Promotion path:** real capability gaps and enhancements graduate into the vault's own
   `_agent/backlog.md` (filed by a partner or by hand), then get built via `vlt-mint`. This doc is
   the scratchpad; the backlog is the committed intake.

## Open

> `- [ ] [<area>] (<kind>) — <what happened> · <expected vs actual, repro if useful>`

### Install / setup
- [ ] [vlt-setup] (friction) — local `/plugin marketplace add` install didn't work first try; _capture the exact error + the fix here so the install docs can be corrected_.
- [ ] [bmm/core] (verify) — during the run, `merge-config.py --legacy-dir` consolidated `_bmad/core/config.yaml` into root `config.yaml` and **deleted** the per-module core file. Values were preserved at root (the modern location), so the base BMad agents *should* be fine — but confirm `bmm` agents still work; if not, the values live in root `config.yaml` now.

### Partners (librarian / researcher)

### Operations (ingest / research / query / extract / lint)

### BMad tooling (not Vault's to fix — flagged upstream)
- [ ] [bmad-installer] (bug) — installer's `_bmad/config.toml` serializes `vault_structure` as `"[object Object]"` (a JS bug). Harmless to Vault (which reads `config.yaml`), but it's a real installer defect.
- [ ] [bmad-tooling] (friction) — **TOML vs YAML config split.** The v6.8.0 installer writes `config.toml`; the module-builder setup skill + scripts write/read `config.yaml`. Nothing reconciles them. Vault deliberately treats `config.yaml` as authoritative (documented in vlt-setup); a true fix is BMad-core's, not the module's.

### vlt-setup (low-severity smells, deferred)
- [ ] [vlt-setup] (smell) — help-CSV `module` column is `Vault` (display) while `code` is `vlt`; `--module-code vlt` is inert on the non-legacy merge path (it self-derives from column 0). Re-runs are dedup-safe, so harmless — leave for now.
- [ ] [vlt-setup] (idea) — provisioning "created vs. already present" is narrated, not script-emitted. A small manifest/script would make re-run reporting robust. Deferred.

### Evolution (mint / review-council)

### Governance (contract / conventions / personas / thread / backlog)

## Resolved

> `- [x] [<area>] (<kind>) — <what it was> [resolved: <how>]`

- [x] [vlt-setup] (bug) — **`{project-root}` literal-token junk-dir trap.** The documented `merge-config.py` invocation passed `--config-path "{project-root}/_bmad/config.yaml"`; the script only resolves `{project-root}` inside config *values*, so as a path *arg* it created a real dir literally named `{project-root}` and (in headless) would report success on a broken write. [resolved: 2026-06-01 — Write Files now sets `ROOT="$(pwd)"` and passes resolved `$ROOT/...` paths, with an explicit note that the token stays literal only inside config values.]
- [x] [vlt-setup] (bug) — **`python3 ./scripts/...` fails (PEP 723 deps).** The scripts declare inline `pyyaml`; bare `python3` errors. [resolved: switched documented invocation to `uv run --quiet`.]
- [x] [vlt-setup] (bug) — **wrong distribution premise.** SKILL still claimed "Vault is plugin-distributed, never stages under `_bmad/`" — false now that we install via the BMad installer (which writes `config.toml` + `_bmad/vlt/`,`_bmad/core/`). [resolved: On Activation reframed to "installer-built vault, additive/non-invasive"; cleanup-section rationale corrected.]
- [x] [vlt-setup] (friction) — **commands assumed cwd == skill dir** (`./scripts`, `./assets`). cwd is the vault root. [resolved: anchored to `$SKILL` = the skill's activation "Base directory".]
- [x] [vlt-setup] (friction) — **"write core only if no core keys exist" was ambiguous** across config.toml/staging/config.yaml. [resolved: new "Config files in an installer-built vault" section says check `config.yaml` specifically — that's what the runtime reads.]

- [x] [vlt-setup] (bug) — setup inherited the BMad **installer's** legacy-migration + cleanup machinery (`merge-config --legacy-dir`, `cleanup-legacy.py --also-remove _config`), but Vault is **plugin-distributed** and a guest in a shared `_bmad/`. The steps had no Vault staging to clean and instead reached for *other modules'* config (`core/config.yaml`, `_config/`, `bmm/`). The setup agent correctly deviated to avoid corrupting the live `bmm` install. [resolved: 2026-06-01 — `vlt-setup/SKILL.md` now (a) drops `--legacy-dir` from both merge commands, (b) replaced the cleanup step with "Do Not Run Installer Cleanup", and (c) reframed activation as strictly additive / non-invasive in a shared `_bmad/`. The first run's already-applied `core/config.yaml` consolidation is tracked under Open → verify bmm.]

## Decisions

- **Architecture: ACCEPTED — vault-resident, standard BMad install** (2026-06-01). Drop the bespoke `vaults` registry; install the module *into* each vault via the BMad installer (`npx bmad-method install --custom-source …`), which reads the repo-root `.claude-plugin/marketplace.json` and copies skills into the vault's `.claude/skills/`. Full change-set in [`vault-resident-architecture-spec.md`](./vault-resident-architecture-spec.md). Distribution fix (manifest moved to repo root, README install steps) done; the skill-sweep (drop registry across the 9 skills + setup + module-help.csv + plan + contract) is the remaining implementation.
- [x] [install] (fix) — the first-run install friction was a wrong-mechanism + wrong-location issue: BMad installs via `npx bmad-method install --custom-source`, not Claude Code's `/plugin install`, and `marketplace.json` must be at the **repo root** (it was under `skills/.claude-plugin/`). [resolved: 2026-06-01 — manifest moved to `./.claude-plugin/marketplace.json` with `./skills/vlt-*` paths; README updated to the installer command.]
- **BMB is an optional recommended companion, not a co-dependency** (2026-06-01). Only `vlt-mint`'s deliberate from-scratch path uses `bmad-agent-builder` (a BMB skill); everything else — both partners, all 5 ops, `vlt-review-council`, and `vlt-mint`'s in-flow template path — needs zero BMB. Neither the plugin format nor the BMad installer enforces hard module deps (both degrade, don't block), and forcing it would contradict Vault's standalone design. Chosen posture: **document as recommended** — `README.md` "Recommended companion" section + an actionable missing-dep warning in `vlt-setup`'s Check Dependencies step.

## Ideas / enhancements (v2+)

- Dashboard over vault growth & health (already deferred to v2 in the plan).

## Session log

> Quick notes per testing session — what you tried, the headline impression.

### 2026-06-01 — _first run_
- Installed into `{field-vault}`. _Impressions:_
