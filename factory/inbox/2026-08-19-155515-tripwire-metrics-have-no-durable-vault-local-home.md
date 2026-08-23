# Enforcement kit: vault-local tripwire metrics have no durable home — the metric table lives in a module-owned file overwritten on every upgrade

- **filed:** 2026-08-19 (GitHub issue opened 2026-08-19T15:55:15Z)
- **origin:** `mggower/bmad-module-vlt#1`
- **origin vault:** app-vault (work machine) — filed through the GitHub account of the module owner; the tracker carries no origin-vault field yet (see the 2026-08-19 feedback-rail filing's declared attribution debt)
- **kind:** defect (durability gap in the enforcement kit)
- **materialized by:** `inbox-capture`, Arc 9 capture run 1 (2026-08-20), by hand, as the
  intake prototype named in `inbox/2026-08-19-130120-feedback-loop-is-single-machine-github-issues-as-remote-rail.md`.
  Body below is the issue text as filed, unedited. Grounding lives in the Arc 9 roadmap, not here.
- **labels at materialization:** none (the `field:defect` / `vault-filed` label set is proposed, not yet created)

---

## Summary

The enforcement kit lets a vault grow its own tripwires durably, but gives it no durable place to define the **metric** a local wire needs. The only home for a metric is `assets/hooks/vlt-vitals.py`, which `vlt-setup` §2b overwrites on every install/update. So a vault-local wire and the metric it depends on have opposite fates on upgrade, and the wire is left pointing at an id that no longer exists.

## The contract gap

Three shipped rules are individually reasonable and jointly unsatisfiable:

1. **`tripwires.yaml` is vault-grown after seeding.** Its header: seeded wires merge by `id`, *"LOCAL THRESHOLDS WIN; local wires are never dropped or rewritten. Everything below the seed is this vault's to evolve."*
2. **A wire's `metric` must name an id from the canonical table**, and no other — an unknown id is a per-wire error (`vitals.py`: `return "error", f"unknown metric id ..."`).
3. **The canonical table lives only in `vlt-vitals.py`**, which is *"module-owned, not user-authored — overwrite it on every install/update ... the vault never edits it"* (`vlt-setup` SKILL.md §2b).

A vault that wants a local wire over a vault-local concern therefore has nowhere in-contract to put its metric. `vault_structure` explicitly supports vault-local logical keys with no `module.yaml` counterpart (and `resolve_structure_map` unions config keys over the shipped defaults, so the reader already anticipates them) — but there is no way to derive a metric over one without editing the file the module reserves to itself.

The practical result: the vault edits `vlt-vitals.py` anyway, because that is the only option, and the edit is destroyed on the next upgrade.

## Why the B7-2 manifest doesn't close it

B7-2's structural walk was a real improvement — `.claude/hooks/` is now inside the manifest net, so a hand-edited reader is *reported* as `skill_asset_divergence` from here on. Two things remain:

- **Detection is not preservation.** Skill assets have no overlay mechanism, so the surfaced divergence is the user's to re-apply by hand after every upgrade, forever. For conventions the module solved exactly this shape with `{overlays}/*.overlay.md`; the metric vocabulary has no equivalent.
- **The gap was invisible for the upgrade that introduced it.** Any vault that edited the reader before B7-2 had `.claude/hooks/` outside the manifest, so pre-flight could not classify it and the refresh dropped the edit with nothing in the post-flight report. That is a one-time tail, but it is the population most likely to have edited the reader.

Severity is *degraded-loud*, not silent-green: the orphaned wire reports `error` and `vlt-lint` has a `counter_unknown_metric` flag, so a vault does eventually find out. But the clobber itself is silent, and what it destroys is a derive function that has to be rewritten from scratch rather than re-pointed.

## A second-order trap worth a line in the docs

`vlt-upgrade` Step 3 (reconcile) runs before Step 3.6 (provision → manifest write), and the manifest is computed from *installed* files. If anything re-applies a local edit to a manifested file during the reconcile, the subsequent manifest write records the **modified** SHA as though it were stock — silently blessing the local edit and guaranteeing the next upgrade clobbers it without a report. The skill's own step order makes this reachable, and nothing warns about it. Whatever the fix below, the manifest write should key off the **module source** for shipped-ness of *content*, not just of *path*.

## Possible directions

Not a strong preference between these, but roughly in order of how well they match existing patterns:

1. **A vault-local metrics module.** Have `vlt-vitals.py` optionally import/exec a vault-owned file (e.g. `_agent/metrics.py` or `{overlays}/metrics.py`) that registers extra `(id, description, derive_fn)` entries into `METRICS`. Agent-zone, never overwritten — the same fate split the conventions overlay already uses. Absent file = no-op; a failing local module degrades loudly per wire rather than taking the reader down.
2. **Declarative local metrics in the registry.** Let a wire declare a small derived quantity inline (e.g. `derive: {kind: file_count, zone: <structure-key>, exclude: [...]}`) for the common count/size/age shapes, so the frequent cases need no Python at all. Narrower, but keeps the derive-first invariant obvious and keeps everything in one vault-grown file.
3. **At minimum, make the loss legible.** If neither lands soon: have the §2b hook refresh diff the installed reader against the shipped one and, on a difference, report it in the Confirm summary *before* overwriting — plus a `vlt-upgrade` note that a hand-edited reader must be re-applied. This does not fix the gap but converts a silent destruction into a stated one, which is the module's usual posture (`base_divergence` / `governance_divergence`).

---

## Amendment (2026-08-21) — a second instance of the class, relayed by hand from the issue's comment thread

*(Appended by the factory clerk: a comment landed on `mggower/bmad-module-vlt#1`
2026-08-21T14:45:55Z from app-vault (module_version 0.12.0, rail_contract 1). The intake
does not read comments on captured issues — that gap is itself filed as
`2026-08-21-150500-captured-issues-accept-comments-the-intake-never-reads.md` — so this
amendment is hand-folded to keep B9-6's brief whole.)*

**`_meta/vault-operating-contract.md` has no overlay mechanism.** Conventions ship a
first-class overlay system; the contract ships none, so a vault-local addition to it is
overwritten wholesale by the bundle refresh on every upgrade. Concrete instance: a
vault-local structure-map key documented in the contract's *Path resolution* table has been
clobbered and hand-restored on two consecutive upgrades (0.9.1 → 0.11.0, 0.11.0 → 0.12.0).

**Why it bears on this filing's fix:** the v0.12.0 durable-host doctrine names three
carve-outs (vault-writable declared field, overlay, vault-scoped sibling) — for a
contract-level row **none is reachable**, so the doctrine's own hosts do not cover the
artifact that states the doctrine. The commenter poses B9-6's scope choice explicitly:

- **Narrow** — durable home for vault-local *metrics* only (closes this filing as written;
  leaves the contract instance open).
- **General** — "a vault-local fact whose only home is a module-owned file" is the class;
  the contract gains an overlay (or the map a carve-out) in the same build.

Related, per the commenter: compounds with `mggower/bmad-module-vlt#2` (the divergence-net
manifest defect) — a vault re-applying a clobbered edit is the vault whose divergence net
goes blind. **This scope choice is an owner ruling at B9-6 ideation/brief time, recorded
here so the brief cannot miss it.**

## Amendment — mggower/bmad-module-vlt#1 comment 2026-08-23T21:55:08Z (mggower)

Field amendment from vlt-core, 2026-08-23 (module at 0.14.0): the lost derive this issue describes has now been identified and its recovery attempted under B10-4's `local_metrics:` home. The metric is `pages_with_review_after` — the denominator for canonical `expired_pages` — recovered from vault git history (`_agent/vitals.sh`, superseded at 0.9.0). Two corrections to this issue's framing: the loss mechanism was a silent supersession at install-time, not an upgrade overwrite (this vault never hand-edited `vlt-vitals.py`), and the recovery **could not be completed** — the shipped `local_metrics:` kinds (`file_count`/`bytes`/`days_since_newest`) carry no content predicate, so a count of pages *carrying a frontmatter key* is inexpressible and declaring it as a bare glob count would fabricate the metric. Filed factory-side as the B10-4(4) BLOCKED routing; the module owes a content predicate, a fourth kind, or a canonical entry.
