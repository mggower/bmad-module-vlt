# Write the skill-asset manifest from stock content — hashing live files silently disables the divergence net

origin: mggower/bmad-module-vlt#2

- **filed:** 2026-08-21 (GitHub issue opened 14:43:52Z via the vlt-feedback rail)
- **origin vault:** app-vault · **module_version:** 0.12.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-08-21 by the factory intake (github-intake, first live run)

---

### what_happened

The skill-asset divergence net can silently disable itself, permanently, for any file it covers.

`verify-skill-manifest.py --write` computes each manifest entry by hashing the **live installed
file**. `--source-skills-dir` is consulted only for *provenance* — deciding which skill names count
as shipped — never for *content*. So if any manifested file is locally diverged at the moment
`--write` runs, the manifest records the hand-edited content as the reference. From then on
`--verify` reports that file as clean, because live == manifest. The next upgrade refreshes it and
destroys the local edit with no report.

That is the exact outcome the net was built to prevent.

Two shipped texts state the opposite, and a vault that follows either literally walks into it:

- `skills/vlt-setup/SKILL.md`, *Stash the skill-asset manifest*: "Compute it from the *installed*
  shipped files (which equal stock at install time)". The parenthetical is true at first install and
  false on every later run.
- `skills/vlt-upgrade/SKILL.md`, Step 2: "The skill manifest itself is refreshed to **the new
  shipped versions** by the Step-6 provision hand-off". It is refreshed to the live versions.

Reproducing it needs no upgrade at all, because `vlt-setup` never re-copies shipped skill files — it
provisions governance, workflows, and hooks only:

1. Hand-edit any manifested skill asset (e.g. a file under `skills/vlt-mint/assets/`).
2. Re-run `vlt-setup`, which the skill documents as safe "anytime to refresh".
3. Skills are untouched by that run, but the manifest is rewritten from the live tree and absorbs
   the edit as its new reference.
4. The next `vlt-upgrade` pre-flight reports `diverged: []`. Step 2 refreshes the file. The edit is
   gone, and `skill_asset_divergence` never mentioned it.

Hit in a real 0.11.0 -> 0.12.0 upgrade. A user-ruled re-application of a local edit to a manifested
hook was absorbed by the manifest write that followed it in the same run; the divergence had to be
re-established by hand, by writing the manifest against stock content instead of the live tree. Any
vault that re-applies a surfaced `skill_asset_divergence` before the manifest write — which the
shipped flow explicitly contemplates — loses the net for that file from then on.

### evidence

`scripts/verify-skill-manifest.py`, `compute_manifest` — both loops hash the live tree:

```python
shipped = {p.name for p in source_skills_dir.glob("vlt-*") if p.is_dir()}
for name in sorted(shipped):
    skill_dir = live_skills_dir / name          # <- live, not source
    ...
            entries[str(f.relative_to(root))] = sha256_file(f)

for sub in EXTRA_DIRS:
    shipped_tree = source_skills_dir / "vlt-setup" / "assets" / sub
    basenames = {p.name for p in shipped_tree.rglob("*") if p.is_file()}
    installed = root / ".claude" / sub          # <- live, not source
    ...
            entries[str(f.relative_to(root))] = sha256_file(f)
```

`source_skills_dir` supplies `shipped` (names) and `basenames` (names). Content always comes from
`live_skills_dir` / `root/.claude/<sub>`.

Observed on the affected vault, same run, one file diverged:

```
# manifest written from the live tree
{"mode": "write",  "entries": 67, "added": [...], "removed": []}
{"mode": "verify", "entries": 67, "diverged": [], "missing": []}      # net blind

# manifest written from stock content instead
{"mode": "write",  "entries": 67, "added": [],    "removed": []}
{"mode": "verify", "entries": 67, "diverged": ["<one module-owned file>"], "missing": []}
```

Same 67 entries, same live tree, opposite verdict — the only variable is which content the write
hashed.

### provenance_guess

**A guess — please ground it.** `compute_manifest` in `skills/vlt-setup/scripts/verify-skill-manifest.py`
looks like the single fix site: on `--write`, read content from the source tree for every path whose
provenance is the source tree, and fall back to live only where no source counterpart exists. The two
prose claims above would then become true rather than needing rewording.

Worth deciding explicitly: whether `--write` should refuse, or at minimum report, when a live file it
is about to manifest differs from its source counterpart. Silently recording a divergence as the new
baseline is the step that makes this unrecoverable — a `write` that reported `absorbed: [...]` the way
it already reports `added`/`removed` would have made this visible the first time.

Adjacent but distinct: issue #1 (vault-local metrics have no durable home). That is about *where a
vault-local edit may legally live*; this is about *the net that reports such an edit disabling
itself*. They compound — a vault re-applying an edit because #1 gives it nowhere else to go is
exactly the vault that trips this — but the fixes are independent.

### kind

defect

### origin_vault

app-vault

### acceptance_vault

Any vault with at least one hand-edited manifested skill asset. Synthetic reproduction is enough: edit
one manifested file, run `vlt-setup`, then `--verify`. Expected after fix: the edit still reports as
`diverged`.

### module_version

0.12.0

### rail_contract

1


