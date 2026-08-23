# `merge-config.py` strips the whole `vault_structure` block from `config.yaml` on re-run — the upgrade's own provision hand-off destroys the map it depends on

_Filed 2026-08-02 from **vlt-core**, during the `vlt-upgrade` 0.9.0 → 0.9.1 run (own-the-apply).
Classification: **defect**. Caught by a post-step diff, not by any check in the loop — the vault was
restored by hand before the upgrade closed._

## The claim

`vlt-upgrade` Step 3.6 hands provisioning to `vlt-setup`, which merges config via
`skills/vlt-setup/scripts/merge-config.py`. On this vault the script bumped `vlt.version`
correctly **and deleted the entire `vlt.vault_structure:` block** — all 18 keys, including this
vault's local `dog_training_root: _agent/dog-training/` override.

The `vault_structure` map is not decoration. Every vlt skill resolves its paths through it
(`vlt-upgrade` On Activation: "Resolve paths through the `vault_structure` map (override wins, else
shipped default)"). Deleting it silently converts an explicitly-configured vault into an
implicitly-defaulted one, and drops any non-shipped key with no way to recover it except from git.

## Grounding

Command run (vault root `{field-vault}`, module 0.9.1):

```
uv run .claude/skills/vlt-setup/scripts/merge-config.py \
  --config-path _bmad/config.yaml \
  --module-yaml .claude/skills/vlt-setup/assets/module.yaml \
  --answers <answers.json> \
  --user-config-path _bmad/config.user.yaml --verbose
```

The answers JSON was built from the **live config**, so `vault_structure` was present in the input:

```json
{"vault_structure": { ...18 keys, incl. "dog_training_root": "_agent/dog-training/" ... }, ...}
```

Script reported `"status": "success"` and:

```json
"module_keys": ["name", "description", "version", "default_selected"]
```

`vault_structure` is absent from `module_keys` — the merge simply did not carry it. Resulting diff
against the pre-run config:

```
8c8
<   version: 0.9.0
---
>   version: 0.9.1
10,28d9
<   vault_structure:
<     wiki: _agent/wiki/
      ... 18 lines deleted ...
<     lint_reports: _agent/lint-reports/
```

One line changed as intended; twenty were destroyed. Restored verbatim from the pre-run copy, so
vlt-core's committed config is intact — the version bump landed and the map is unchanged.

## Provenance — **a guess, marked as one**

I did not read enough of `merge-config.py` to name the mechanism, and this filing does not claim to.
What the evidence supports: the script's module-section writer emits a fixed set of scalar keys from
`module.yaml` and does not handle a variable whose `module.yaml` shape is
`{prompt:, default: <map>, example:}` — `vault_structure` is the only such variable. Whether that is
a missing branch, an answers-key mismatch (the answers JSON used the bare key `vault_structure`, which
may not be what the script expects), or an anti-zombie rewrite that rebuilds the section from a
whitelist, **I don't know** — the anti-zombie pattern named in the script's own docstring is the
suspect I'd look at first, since "removed 14 existing rows / rewrite the section" is exactly that
shape in the sibling `merge-help-csv.py`. Factory capture should re-ground this before building.

## Why it matters

1. **It fires on the durability path.** `vlt-upgrade` exists to make evolution survive upgrades, and
   its own mandated provision hand-off destroys a vault-local override. `dog_training_root:` is
   precisely the kind of vault-specific evolution the skill's opening paragraph promises to protect.
2. **Nothing in the loop catches it.** `vault_structure` has no baseline, no manifest entry, and no
   divergence check — the pre-flight snapshot covers conventions, skill assets, governance, mints and
   capabilities, but not `config.yaml`. I found this only because I diffed the config against a
   scratch copy I happened to take before running the script. A vault that trusted
   `"status": "success"` would close the upgrade silently degraded.
3. **The damage is invisible at read time.** With the block gone, every skill falls back to the
   shipped default map and keeps working for the 17 keys where default == override. Only
   `dog_training_root:` — a key with no shipped default — would eventually surface as a broken path,
   in the Dog Trainer's loop, long after the upgrade.
4. **Prior evidence this is not new.** The vlt-core ledger entry for 0.8.0 → 0.9.0 records "config
   bumped to 0.9.0 with `tripwires:` + `lint_reports:` structure keys (local `dog_training_root:`
   kept)" — the map was reconstructed that run too. Whether it was reconstructed *because* the same
   strip happened is not something I can assert from the ledger text; flagging it as a lead.

## What I'd want

- The merge to **carry `vault_structure` through** — shipped defaults refreshed, vault-local keys
  preserved (merge-not-replace, the same discipline `merge-help-csv.py` applies to local-mint rows via
  `--live-skills-dir`).
- Failing that, a **loud** `vault_structure` line in the script's JSON result so a caller can tell
  "merged" from "dropped" without diffing.
- Optionally: `vlt-upgrade` pre-flight snapshotting `config.yaml` alongside the conventions baseline,
  so config divergence joins `base_divergence` / `skill_asset_divergence` as a reported class rather
  than a thing a careful operator happens to notice.
