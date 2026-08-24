# Rule explicitly whether resources/ outside {wiki} is partner-writable — the hard rule neither grants nor prohibits it

origin: mggower/bmad-module-vlt#11

- **filed:** 2026-08-24 (GitHub issue opened 14:28:28Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.14.0 · **rail_contract:** 1 · **kind:** candidate
- **materialized:** 2026-08-24 by the factory intake (github-intake)

---

### what_happened

The operating contract's hard rule neither grants nor clearly prohibits partner writes to `resources/` outside `{wiki}`. It is a gap, not a wall — and a vault that hits it has no way to resolve it from the governance bundle alone.

This is an **ask for an explicit ruling**, not a proposed answer. The vault filing it deliberately did not guess.

The shape of the gap: the hard rule's allowlist does not include `resources/`, and its prohibition clause is scoped to PARA — but `resources/` is not in Layer 3 PARA. So a write to `resources/<anything-not-wiki>/` falls between the two clauses. A partner reading the contract carefully cannot determine whether it is permitted, forbidden, or simply unconsidered.

Root cause, as far as we can tell: the 0.14.0 relocation of the wiki into `resources/` changed that folder from a PARA leaf into a **mixed zone** — part partner-owned (`{wiki}`), part human-curated, part legacy-grandfathered — and the write rule was not revisited to match.

### evidence

All from `_meta/vault-operating-contract.md`:

- **:66** — Layer 3 PARA is defined as `{projects}` / `{areas}`.
- **:68** (the hard rule) — "Partners write only to `_agent/`, `_meta/`, and the wiki's home `{wiki}` — plus the two named PARA surfaces above, and nothing else in PARA."
- **:41** (structure table) — `resources/` is listed separately as "The wiki's human-browsable home (`{wiki}` lives here) — retired as an extraction target; legacy reference artifacts grandfathered".

Compose those three: the allowlist at :68 does not name `resources/`; the prohibition at :68 says "nothing else **in PARA**", and per :66 `resources/` is not in PARA; :41 defines `resources/` as a zone in its own right without stating a write posture. `resources/<not-wiki>/` is therefore in neither the grant nor the prohibition.

**The ruling wanted.** Is `resources/` outside `{wiki}` partner-writable? And if so, under what discipline — attestation? extraction-only? a named surface, in the way the two existing PARA surfaces are named? Or is it explicitly closed? Any of those four is a usable answer; the current silence is not.

**Live instance that forced the question.** This vault wanted to relocate a vault-grown op skill's output shelf from the agent zone to `resources/{shelf}/`, on the reasoning that its output is a delivered, human-facing artifact and the agent zone buries it. We could not determine whether that write was legal. Because an **autonomous weekly scheduled job** writes to that shelf, an unruled write would have run unsupervised every week — so we declined to guess, parked the shelf in the agent zone as a deliberate reversible interim, recorded that in the vault's mint decision log, and addressed the shelf through a structure-map key so acting on the eventual ruling costs one config value rather than a skill edit.

Worth noting as motivation: the pull toward `resources/` is not idiosyncratic. Once `{wiki}` moved there, `resources/` became the vault's human-browsable space, and "put the human-facing artifact where humans browse" is the obvious next inference for any partner. We expect other vaults to reach the same edge.

### provenance_guess

A guess, grounded where possible:

- `_meta/vault-operating-contract.md:68` — the hard rule; the clause needing the ruling.
- `_meta/vault-operating-contract.md:66` and `:41` — the two definitions that, composed, open the gap.
- Root cause: the 0.14.0 wiki relocation into `resources/`.
- **Sibling filings on the same root:** the `extraction.md` prose defect filed alongside this one, #10, and **A11-5**, already captured module-side (the 0.14.0 wiki-relocation migration walked no vault-local overlay). Three symptoms, one relocation. Related, not duplicates — this one is the contract's own side, and it is the only one of the three that needs an owner design ruling rather than an edit.

### kind

candidate

### origin_vault

vlt-core

### acceptance_vault

Any vault with the 0.14.0+ governance bundle. Acceptance is that the contract states a posture for `resources/` outside `{wiki}` explicitly enough that a partner can answer the question without escalating to the user — whichever way the ruling goes. A ruling of "explicitly closed" satisfies this issue as fully as a ruling of "writable under discipline X".

### module_version

0.14.0

### rail_contract

1
