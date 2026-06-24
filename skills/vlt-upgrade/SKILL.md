---
name: "vlt-upgrade"
description: Upgrades the Vault module in a vault durably — snapshots vault-specific evolution, refreshes the shipped bundle without destroying minted partners / local convention overlays / mint history, reconciles by merge-not-replace, and records the divergence. Use when the user requests to 'upgrade vlt', 'update the Vault module', or after pulling a new module version.
---

# Vault Module Upgrade

## Overview

A vault **grows into itself** — it mints its own `vlt-agent-*` partners, adds local convention overlays, accrues mint and decision history. But the generic, module-agnostic installer that refreshes the shipped bundle has **no concept of that vault-specific evolution** and can silently destroy or deregister it. `vlt-upgrade` is the skill that owns the lifecycle so the upgrade is **durable**: shipped things refresh, vault-specific things survive.

The governing idea (operating contract, *Durability across upgrades*): **two classes of evolution, two fates.** Generic state refreshes from the bundle; vault-specific state lives in the agent zone (`_agent/`, never overwritten) or is reconciled by **merge, never replace**.

**Two ways the new bits arrive — prefer to own the apply, degrade to bracket.** The upgrade is two welded jobs: *acquire* the new module bits and *apply* them to the vault.

- **Happy path — own the apply.** If the updated module source is reachable (a local path, the BMad module cache, a checkout), `vlt-upgrade` **merge-copies** the shipped `vlt-*` skills and governance into the install itself — refreshing shipped files, never touching unshipped `vlt-agent-*` dirs or the agent zone. **No destruction occurs.** This is the preferred path and the owner's ideal: vlt-upgrade owns the upgrade end-to-end.
- **Fallback — bracket the installer.** If the bits arrive only by running the generic installer (which copies destructively), `vlt-upgrade` runs **pre-flight first** (snapshotting while the vault is intact), lets the installer run, then **reconciles after** to restore/re-register what the installer dropped.

Either way the reconcile logic is identical. `vlt-upgrade` **calls `vlt-setup`** for provisioning — it never reimplements it.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance), tell the user to run `vlt-setup` first — there is nothing to upgrade.

Resolve paths through the `vault_structure` map (override wins, else shipped default). Logical names used (default, relative to the project root): `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/` (overlays + the stock `.baseline/`), `personas` → `_meta/personas/`, `contract` → `_meta/vault-operating-contract.md`, `upgrade_ledger` → `_agent/upgrade-ledger.md`. The **live skills dir** is `{project-root}/.claude/skills/`; the **live workflows dir** is `{project-root}/.claude/workflows/`. Below, `{overlays}` etc. mean the resolved path.

Determine the **module source** (where the new bits live) — ask the user for the path if it isn't obvious, or detect the BMad module cache. If no reachable source exists and the user will run the installer themselves, take the **bracket** path (pre-flight now; reconcile after they confirm the installer ran).

## Step 1 — Pre-flight (always, from the living vault)

Run this **before any destructive step**, while the vault is intact — its snapshot is the restore source. Capture the **divergence snapshot**:

- **Minted partners** — every `vlt-agent-*` dir under the live skills dir whose code is **not** a shipped agent in the module's `module.yaml` `agents[]` (librarian / researcher / creative are shipped; anything else was minted locally). Record dir path + its help-registry row(s).
- **Convention overlays** — every `{overlays}/*.overlay.md` (vault-local additions, durable — must never be lost).
- **Base convention divergence** — for each `{conventions}/{name}.md`, compare to its stock baseline `{overlays}/.baseline/{name}.md`. A base that **differs** from its baseline was hand-edited locally (it should have been an overlay or upstreamed) — record it as divergence (do **not** silently clobber it; the refresh will overwrite the base, so surface this so the local change isn't lost unnoticed). If a baseline is missing, record `baseline_missing` (can't classify — seed it from the incoming source this run, best-effort).
- **Mint history** — confirm `_agent/mint/decision-log.md` and any `_agent/mint/{date}-{slug}.md` planning docs exist (agent-zone; expected to survive untouched — recorded for the ledger).
- **Capabilities** — every vault-grown light capability under `{partners}/*/capabilities/*.md` and every family contract under `{capabilities}/families/*.md` (agent-zone; must survive untouched). Note which families are **shipped** (their invariants may change upstream — see reconcile) vs vault-grown.
- **Governance edits** — the operating contract / personas that differ from their shipped versions.

Write this snapshot to a working note and **append the opening half of a ledger entry** (Step 5).

## Step 2 — Apply (own it, or bracket)

- **Own the apply (preferred):** merge-copy from the module source into the install — refresh the shipped `vlt-*` skills, the governance bundle (`_meta/`), and the workflows (`.claude/workflows/*.js`). **Refresh shipped files only**; never delete an unshipped `vlt-agent-*` dir, never write into the agent zone, never overwrite an `{overlays}/*.overlay.md`. Base conventions **are** refreshed (they are pristine by design — local edits live in overlays); a base recorded as locally-diverged in Step 1 is refreshed too, but its prior content is preserved in the ledger and flagged in the post-flight report for the user to re-express as an overlay or upstream.
- **Bracket the installer (fallback):** let the generic installer run now (Step 1 already snapshotted), then continue to reconcile.

## Step 3 — Reconcile (merge, never replace)

1. **Registration — merge-not-replace (B1, the must-ship).** Re-run the help-registry merge with the live skills dir so locally-minted rows are preserved, not stripped:

   ```bash
   uv run {project-root}/.claude/skills/vlt-setup/scripts/merge-help-csv.py \
     --target {project-root}/_bmad/module-help.csv \
     --source {project-root}/.claude/skills/vlt-setup/assets/module-help.csv \
     --live-skills-dir {project-root}/.claude/skills \
     --verbose
   ```

   With `--live-skills-dir`, a `vlt` row whose skill is absent from the bundled source but whose **skill dir still exists live** is preserved (a local mint); a row whose dir is gone is a true zombie and still dropped. Confirm the JSON `local_mints_preserved` lists every partner from the Step-1 snapshot.

2. **Bodies — restore dropped mints (B2, insurance).** For each minted-partner dir in the Step-1 snapshot, confirm it still exists under the live skills dir. If a destructive apply removed one, **restore it** from the snapshot. On the own-the-apply path nothing was deleted, so this is a no-op — but always verify (the cost is a directory check).

3. **Conventions — overlays + baseline.** Overlays in `{overlays}/*.overlay.md` are agent-zone and were never touched — confirm they are intact. Refresh the stock baselines `{overlays}/.baseline/{name}.md` to the newly shipped versions (the new stock reference, used by the next divergence check). For any base recorded as locally-diverged in Step 1, surface it in the report (see Step 4) so the user can lift the change into an overlay or file it upstream.

4. **Capabilities — reconcile-not-replace + family propagation.** The capability agent-zone (`{partners}/*/capabilities/`, `{capabilities}/families/`) is never overwritten — confirm every light capability and family contract from the Step-1 snapshot is intact. If a **shipped family's invariants changed** in this upgrade, fire the **propagation check** against the vault's instances (the same discipline as a convention edit's consumer walk): for each instance whose body no longer honors a changed invariant, surface it in the post-flight report (`family_invariant_drift`) for a human to reconcile — never auto-rewrite a partner's body. (Durability and coherence, the same seam — a family invariant change on upgrade *is* Model B's propagation hook firing.)
5. **Migrations — run pending one-time fixups (idempotent).**
   - **Decision-log relocation (§A1):** if a legacy `.decision-log.md` exists in `{project-root}/.claude/skills/vlt-mint/`, move its entries into `_agent/mint/decision-log.md` (create if absent) and leave a one-line pointer stub at the old path. Idempotent — a second run finds nothing to move.
   - **Overlay lift (first upgrade):** if Step 1 found base conventions diverged from baseline and no overlays yet exist for them, offer to **lift** the local additions into `{overlays}/{name}.overlay.md` (per-file judgment — additions move to the overlay, the base is restored to pristine stock). This is the one-time exercise that puts an already-diverged vault onto the durable path.
   - Run any other migrations the new version documents.

6. **Provision — hand off to `vlt-setup`.** Invoke `vlt-setup` (reconfigure branch) to ensure structure, governance bundle, workflows, and the new agent-zone homes (`_agent/conventions/`, `_agent/mint/`, `_agent/capabilities/families/`) are present. `vlt-upgrade` calls it; it does not duplicate provisioning.

## Step 4 — Post-flight divergence report

Report in a parseable summary so the user sees exactly what changed and what needs their attention:

```yaml
upgrade:
  from_version: <prev>            # module_version before
  to_version: <new>              # module_version after
  apply_path: own | bracket
  mints_preserved: [<vlt-agent-x>, ...]      # registration kept
  bodies_restored: [<vlt-agent-x>, ...]      # B2 — empty on the own path
  overlays_intact: [<name.overlay.md>, ...]
  baselines_refreshed: [<name>, ...]
  base_divergence: [<convention: base was hand-edited (prev content preserved in ledger) — lift to overlay or upstream>, ...]
  migrations_run: [decision-log-relocation | overlay-lift | <other>, ...]
  governance_divergence: [<file differs from shipped — review>, ...]
  capabilities_intact: [<partner/slug>, <family>, ...]            # vault-grown caps + family contracts preserved
  family_invariant_drift: [<family: instance <partner> no longer honors invariant X — reconcile>, ...]
```

`base_divergence` and `governance_divergence` are the **detect-and-report** safety net (filing #8 B3): the upgrade never silently clobbers a local edit without surfacing it — but it does not auto-merge either (overlays make that unnecessary going forward; a hand-edited base is the user's to re-express).

## Step 5 — The standing divergence ledger

`{upgrade_ledger}` (default `_agent/upgrade-ledger.md`) is an **append-only standing record** of how far this vault has drifted from stock — read it between upgrades to see the vault's evolution over time. It is agent-zone (durable) and **never rewritten**: each upgrade appends one dated block. Create it lazily on first upgrade with a title line, then append:

```markdown
# Upgrade Ledger

_How this vault has evolved from stock, one upgrade at a time. Append-only._

## [YYYY-MM-DD HH:MM] vlt <from_version> → <to_version> (<apply_path>)
- Mints preserved: <list>            # local partners kept registered
- Bodies restored: <list or none>    # B2
- Overlays: <list of *.overlay.md>   # local convention additions, durable
- Base divergence: <list or none>    # hand-edited bases surfaced (prev content quoted/linked)
- Migrations: <list or none>
- Governance divergence: <list or none>
- Notes: <anything the user should remember>
```

Pass the timestamp in explicitly (the agent knows the date on activation). The opening half is appended at pre-flight; the entry is completed at post-flight.

## This skill does not…

- **Reimplement `vlt-setup`.** Provisioning is `vlt-setup`'s job; `vlt-upgrade` calls it.
- **Control the generic installer.** Whether the installer clean-replaces or copies-over is external and unknowable from here; the prefer-own/degrade-to-bracket design makes that unknown irrelevant — own the apply when possible, reconcile defensively when not.
- **Auto-merge a hand-edited base convention.** Overlays prevent that collision going forward; an existing base hand-edit is surfaced (report + ledger) for the user to lift into an overlay or upstream. It never silently overwrites without recording the prior content.
- **Touch the human zones or PARA.** Same boundaries as every partner — `_agent/` and `_meta/` only.

## Verify

Before closing: the live `module-help.csv` still carries every locally-minted partner row (Step 3.1 JSON confirms); every minted-partner dir from the Step-1 snapshot still exists (Step 3.2); every `{overlays}/*.overlay.md` is intact; `_agent/mint/decision-log.md` exists (relocation done if a legacy file was present); the ledger has a new dated block; the post-flight report names any base/governance divergence for the user. Then offer to commit.
