# BMad installer interop: module.yaml not locatable + module-help.csv header off-canon

_Filed from the `vlt-core` vault, 2026-07-03. Surfaced during a **manual BMad upgrade (vlt excluded)** run to install the **CIS module** — i.e., not a vlt operation at all. The generic BMad installer scanned the vault's installed modules, found `vlt` registered, and emitted three warnings against it. Nothing broke, but all three are the installer telling us vlt's install surface deviates from the canonical BMad module shape — exactly the class of friction the "prefer standard BMad, no bespoke" ruling exists to eliminate._

## Evidence (verbatim installer output)

```
[warn] collectAgentsFromModuleYaml: could not locate module.yaml for 'vlt'. Agents declared by this module will not be written to config.toml.
[warn] writeCentralConfig: could not locate module.yaml for 'vlt'. Answers from this module will default to team scope — user-scoped keys may mis-file into config.toml.

▲ vlt/module-help.csv header does not match canonical schema.
  Expected: module,skill,display-name,menu-code,description,action,args,phase,preceded-by,followed-by,required,output-location,outputs
  Found:    module,skill,display-name,menu-code,description,action,args,phase,after,before,required,output-location,outputs
  Data loaded positionally.
```

## Finding 1 — installer cannot locate vlt's `module.yaml` (agents + config-scope fallout)

The module's `module.yaml` lives at `skills/vlt-setup/assets/module.yaml` and is placed into the vault by **vlt-setup's own copy step** — but wherever it lands (or doesn't), it is **not where the generic BMad installer looks** when it enumerates installed modules (`collectAgentsFromModuleYaml` / `writeCentralConfig`).

Two concrete consequences, per the warnings:

1. **The agent roster is invisible to central config.** `module.yaml` declares the three shipped partners (`librarian`, `researcher`, `creative`) precisely so roster UIs and `config.toml` can see them — including the owner's ability to set a personal name via `[agents.<code>]` (the Build #1 naming ceremony's config-side half). If the installer can't find the file, none of that gets written.
2. **Config answers mis-scope.** vlt's install-time answers default to **team scope**; user-scoped keys may mis-file into `config.toml`. Today vlt's only variable is the advanced `vault_structure` override, so blast radius is small — but it's a standing scope bug for any future config variable.

**What to figure out at ideation:** where does the canonical installer expect an installed module's `module.yaml` (e.g. `_bmad/<code>/module.yaml` at the vault root)? Then either (a) vlt-setup/vlt-upgrade place (or symlink/copy) the file there as part of their apply/reconcile steps, or (b) the plugin manifest points the installer at it. This must survive `vlt-upgrade`'s own-the-apply merge-copy and be reconciled on every upgrade, not just fresh install. Worth checking whether the same gap explains any past roster-UI blankness in vlt-core.

## Finding 2 — `module-help.csv` header drifted from canonical schema (`after,before` vs `preceded-by,followed-by`)

Canonical BMad schema names columns 9–10 `preceded-by,followed-by`; vlt ships `after,before`. Same 13 columns, same positions — the installer recovers by loading positionally — but it's a warning on every install/upgrade touching the vault, and positional loading is exactly the kind of silent coupling that bites when either side changes column order.

The header is hardcoded in (at least) three module-owned places, all of which must move together:

- `skills/vlt-setup/assets/module-help.csv` line 1 (the shipped source of truth)
- `skills/vlt-setup/scripts/merge-help-csv.py` — the canonical-header constant (the `"after"` / `"before"` entries around lines 46–47)
- any prose in `vlt-mint` / `vlt-setup` that names the columns when teaching the always-quote registration rule (build-10 #3)

**Migration wrinkle (real, don't skip it):** `merge-help-csv.py` prefers the **target's existing header** when merging into a live vault (`header = target_header if target_header else source_header`). So shipping a renamed source header alone will NOT fix already-installed vaults — vlt-core's live `_bmad/module-help.csv` keeps the old header forever and the installer keeps warning. Needs an explicit header-migration step (rename-in-place when the target header is the known-old variant), most naturally in `vlt-upgrade`'s reconcile or inside the merge script itself. Local-mint rows (chef, dog-trainer, health-coach, the retired local vlt-track) are positionally unaffected but must survive the rewrite (B1 rule).

## Why this is one filing, not two

Both findings are the same root pressure: **vlt's install surface predates or drifted from the canonical BMad module contract**, and the generic installer is now the thing that notices. The fix posture should match the standing rulings — install the BMad way, keep `vlt-upgrade` owning durability across the change, zero destruction of vault-local evolution.

## Suggested shape (for capture/ideation, not binding)

One small hardening build: (1) determine the canonical `module.yaml` location + make vlt-setup/vlt-upgrade put it there durably; (2) rename the two CSV columns across the three module-owned sites + add the target-header migration to the merge/upgrade path; (3) acceptance = re-run any BMad install/upgrade against a vault with vlt installed and see **zero** vlt warnings, with all local mints and the agent roster intact in `config.toml`.
