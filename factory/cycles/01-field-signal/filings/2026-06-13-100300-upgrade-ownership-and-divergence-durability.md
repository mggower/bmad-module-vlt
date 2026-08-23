# Vault upgrade ownership: make self-evolution upgrade-durable + introduce a `vlt-upgrade` skill

**Filed:** 2026-06-13 · **Origin:** post-Chef-mint architecture review in `vlt-core` · **Target artifacts:** `vlt-mint` (shipped change, mirror now), `vlt-setup` (provisioning + migration), a **new `vlt-upgrade` skill** (design proposal), the operating contract (durability principle)

## Problem statement

Vault is a **self-evolving** module installed *into* a vault: the cast mints new partners and ops, amends conventions, and accrues a decision log — all **in the installed copy**. But upgrades are performed by the **generic BMad installer**, which is module-agnostic: it copies the new release's files over `.claude/skills/` (and ships fresh `assets/`), with no knowledge of what in this vault is *local evolution* vs *shipped baseline*. The result is a structural hazard: **the installer can silently destroy or deregister vault-specific evolution on every version bump.**

Concrete losses identified (grounded in reading `vlt-setup` + the install layout):

1. **The mint decision log lived inside a clobber-prone skill dir.** `.claude/skills/vlt-mint/.decision-log.md` held the entire council-gated mint history (every new-partner verdict + reasoning). A version upgrade that replaces the `vlt-mint/` directory destroys it. **(Fixed locally — see §A.)**
2. **Locally-minted partners are not in the module source**, so an upgrade endangers them two independent ways:
   - **Body:** if the installer clean-replaces `.claude/skills/vlt-*`, minted partners not in the shipped set (here: `vlt-agent-health-coach`, `vlt-agent-chef`) are deleted — orphaning their memory in `_agent/partners/` (relationship history with no partner to own it).
   - **Registration:** independently, `vlt-setup`'s `merge-help-csv.py` is **anti-zombie** — it strips *all* `vlt` rows from the live `module-help.csv` and rewrites them from the **bundled** `assets/module-help.csv`. The new release's bundle won't contain this vault's mint rows, so minted partners are **deregistered from help even if their skill dirs survive.**
3. **Convention divergence is invisible and unmanaged.** `vlt-setup` installs governance **skip-if-present** (the vault's edited file wins). This *protects* local amendments (good — e.g. the personalized-extraction `extraction.md` edit survives), but it also means a new version's **improved** conventions silently **don't apply** — the vault freezes on its old edited copy with no notification of the drift either way.

The reconciliation philosophy is otherwise sound and already in use: **generic evolution flows back via this inbox → ships in the module → arrives on upgrade.** The gap is everything that is *legitimately vault-specific* (a vault's own minted partners, its local convention edits, its mint history) — that must **survive** upgrades, not be expected to round-trip through the module.

## The durability principle (propose adding to the operating contract)

> **Two classes of evolution, two fates.** *Generic* evolution (a bug fix, a better convention, a new core capability) belongs **upstream** — filed to the module, shipped, and received on upgrade. *Vault-specific* evolution (a vault's own minted partners, its local convention edits, its mint/decision history) must be **upgrade-durable**: it lives in the **agent zone (`_agent/`)** — which neither the installer nor `vlt-setup` ever overwrites — or is reconciled by a **merge, never a replace**. No valuable state lives where the installer copies.

This makes durability a property of *location and merge strategy*, not of getting an upgrade *procedure* right every time — robust even against a dumb installer.

---

## §A. Shipped locally now — mirror these in the module

### A1. Relocate the mint decision log to the agent zone
- **Done in `vlt-core`:** moved `.claude/skills/vlt-mint/.decision-log.md` → **`_agent/mint/decision-log.md`**; left a pointer stub at the old path; updated `vlt-mint/SKILL.md` Step 2a (capture) and the Step-4 record line to write to `{project-root}/_agent/mint/decision-log.md` ("the agent zone — upgrade-durable; a module upgrade overwrites this skill directory, so the log is not kept inside it"), creating `_agent/mint/` if absent.
- **Module-side changes to ship:**
  - `vlt-mint/SKILL.md`: both decision-log references → `{project-root}/_agent/mint/decision-log.md` (verbatim from the local edit).
  - `vlt-setup`: in *Provision the Vault → Scaffold the partner + evolution layer*, ensure `_agent/mint/` exists (create-if-absent), alongside `partners`/`backlog`.
  - **Note the aligned precedent:** the 2026-06-09 filing already proposed `_agent/mint/{YYYY-MM-DD}-{slug}.md` for resumable mint **planning docs**. The decision log now joins them — `_agent/mint/` becomes the single durable home for all mint institutional memory.
- **Migration for existing installs** (idempotent, mirrors the legacy `thread.md`→two-file split already in `vlt-setup`): on upgrade, if `.claude/skills/vlt-mint/.decision-log.md` exists and is a real log (not the stub), move/append it into `_agent/mint/decision-log.md`, then replace it with the pointer stub. Safe to re-run.

---

## §B. Durability fixes still needed (decide + ship)

### B1. Minted-partner registration: merge, don't replace
`merge-help-csv.py`'s anti-zombie rewrite is the hazard for mint rows. Options (pick one):
- **(preferred) Preserve unrecognized local mint rows.** When regenerating the `vlt` rows, keep any row whose `skill` (`vlt-agent-*`) exists in the live `.claude/skills/` but is absent from the bundled `assets/module-help.csv` — i.e. a locally-minted partner. Rewrite only the shipped rows; never drop a row backed by an installed-but-unshipped skill.
- **(alternative) A durable mint registry in the agent zone.** Minted partners also register in `_agent/mint/roster.md` (or similar); `vlt-setup` re-derives their help rows from there on every run. Moves the source of truth for *local* mints out of the clobber-prone bundle entirely.

### B2. Minted-partner bodies must survive the installer copy
Specify (and verify against the actual installer): **a Vault upgrade must not delete `.claude/skills/vlt-agent-*` directories that are not part of the shipped set.** If the installer's strategy is "clean-replace the skills dir," that's incompatible with a self-evolving module and needs either an installer flag or the `vlt-upgrade` skill (below) owning the copy. *This is the one behavior I could not confirm from inside the vault — it determines whether B2 is already safe or actively broken.*

### B3. Governance divergence: detect and report (at least)
Keep skip-if-present (it protects local edits), but **stop it being silent**. On update, for each governance file that exists locally *and* differs from the shipped version, **report the divergence** in the confirm summary ("`_meta/conventions/extraction.md` is locally modified — shipped v0.3.0 differs; left your version in place; review if you want the upstream changes"). Lets the user make a 3-way-merge decision instead of unknowingly freezing. (Full 3-way merge is a nice-to-have; *detection + report* is the floor.)

---

## §C. Proposal — a `vlt-upgrade` skill that owns the lifecycle

**Rationale:** reconciliation is Vault domain knowledge; the generic installer can't hold it. Vault already asserts ownership of its own provisioning (`vlt-setup` refuses installer cleanup, declares `config.yaml` authoritative). A dedicated upgrade skill is the natural extension — and it keeps `vlt-setup` a clean provisioning primitive rather than overloading it with upgrade semantics (mirrors the existing setup/mint/lint/upgrade separation of concerns).

**Shape (the vault-owned upgrade front door):**

1. **Pre-flight — snapshot the divergence ledger.** Enumerate what is non-stock in this vault before anything is copied: locally-minted `vlt-agent-*` (skill dirs not in the shipped manifest), locally-edited governance files (diff vs shipped), the mint decision log + planning docs, any locally-edited workflows. Write/refresh `_agent/mint/divergence.md` (or `_agent/upgrade-ledger.md`) — the durable record of "what this vault added on top of stock."
2. **Refresh.** Either drive the installer/fetch of the new module version, or (if it must run externally) detect that it just ran. Design for the safe assumption: **installer copies first, `vlt-upgrade` reconciles after.**
3. **Reconcile (merge, never replace).** Using the ledger: restore/re-register any minted partner the copy dropped (B1/B2); run the decision-log + thread.md migrations (§A1, existing); for divergent governance, report and offer merge (B3); refresh module-owned workflows to shipped versions (already correct behavior).
4. **Post-flight — divergence report.** Show exactly what changed, what was preserved, what diverged and was left alone, and what the user should review. Then hand off to `vlt-setup` for the normal provisioning confirm.

`vlt-upgrade` **calls `vlt-setup`** for provisioning; it does not duplicate it. `vlt-setup` gains only the small idempotent migrations (§A1, B-items); the *orchestration and divergence intelligence* lives in `vlt-upgrade`.

## Exact module-side change list

| Artifact | Change |
|---|---|
| `vlt-mint/SKILL.md` | decision-log path → `{project-root}/_agent/mint/decision-log.md` (both refs) — **A1, shipped locally** |
| `vlt-setup` (provision step) | create `_agent/mint/` if absent; idempotent `.decision-log.md`→`_agent/mint/` migration; **B3** governance-divergence detection+report in the confirm summary |
| `merge-help-csv.py` | **B1** preserve mint rows backed by an installed-but-unshipped `vlt-agent-*` skill (merge, not blanket replace) |
| installer contract / `vlt-upgrade` | **B2** never purge unshipped `vlt-agent-*` dirs (confirm installer behavior first) |
| **new `vlt-upgrade` skill** | **§C** vault-owned upgrade: snapshot ledger → refresh → reconcile → report; calls `vlt-setup` |
| operating contract | add the **durability principle** (generic→upstream, vault-specific→durable-by-location/merge) |

## Upgrade / migration path

- All §A/§B changes are additive and idempotent; safe on re-run. The decision-log and (existing) thread.md migrations are the model.
- Existing installs get the durability retro-fix the first time the upgraded `vlt-setup`/`vlt-upgrade` runs (decision-log relocated, mint rows preserved, `_agent/mint/` created).
- No change to vault content semantics; only *where* durable state lives and *how* the registry/governance reconcile.

## Open questions for the maintainer

1. **Installer copy strategy (blocks B2):** does a BMad module version upgrade *purge* `.claude/skills/` of unshipped dirs, or copy-over-and-leave? Determines whether minted-partner bodies are already safe or actively at risk.
2. **Can `vlt-upgrade` control the installer**, or is the realistic contract always "installer runs, then `vlt-upgrade` reconciles after"? The design assumes the latter (safer); confirm.
3. **Ledger location/name:** `_agent/mint/divergence.md` vs a top-level `_agent/upgrade-ledger.md`? It spans more than mints (governance, workflows), so a mint-scoped folder may be too narrow.
4. **Should some current local mints be upstreamed instead of kept local?** The Dog Trainer reads as a generic vertical worth shipping in the module (upgrade-safe by definition); the Health Coach/Chef may be vault-specific. A maintainer call on where the line sits informs how much weight B1/B2 must carry.
