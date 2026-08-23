---
title: 'Build #9 (Phase E) — Identity polish: the filing-#2 reconciliation'
status: 'BUILT — acceptance batched into the deferred ledger'
module_code: 'vlt'
created: '2026-06-24'
derives_from:
  - 'inbox/2026-06-06-130940-librarian.md (filing #2)'
  - 'skills/reports/build-1-partner-layer-brief.md (findings #4 + #6)'
  - 'skills/reports/inbox-evolution-roadmap.md (Phase E row)'
phase: 'E — Identity polish (the last build phase)'
---

# Build #9 — Phase E: Identity polish

## The finding that defines this build

Phase E was scoped to fold in **filing #2** (Librarian first-breath field notes) plus the **two
outstanding Build #1 owner gates**. Scoping every item against current module source produced a
Phase-A-shaped result: **the build content is already shipped** — almost entirely absorbed by
**Build #1.1** (the close-out of the very field test that *spawned* filing #2). What remained was
one genuine coherence residual and two live-acceptance items that are not code.

| Phase E item | Source | State at scope time |
|---|---|---|
| Naming's home in the two-tier identity model | filing #2 ① | ✅ **Shipped** (Build #1.1) — `name` is a first-class **ungated** `identity.md` frontmatter field (`frontmatter.md:148–154`); contract two-tier line "drift breathes, ratification reborns" (`contract:178, :187`); present in all 3 partner SKILLs + the partner template (`:38, :69`). Per-vault; overrides the `customize.toml` install default. |
| Read `frontmatter.md` before first note-write | filing #2 ② | ✅ **Shipped** (Build #1.1) — explicit beat in the contract's *How to write* (`:231`) and partner template (`:65`). |
| Path-map SSoT — point at the map, don't re-list | filing #2 ③ | ✅ **Shipped behaviorally** (Build #1.1) — partners say "**read the map rather than relying on a partial list**" — **but** the inline *full-set* enumeration beside it had drifted (see residual below). |
| Cold-start reads ~7 files to find emptiness | filing #2 ④ | ✅ Filer flagged **acceptable** — no action. |
| Warm-activation outside-read (felt aliveness) | Build #1 finding #4 | ⏳ **Live acceptance, not code** — warm path fully described; cold-start PASSED live (Gwyn, 2026-06-06); warm enactment un-exercised. |
| Rebirth two-tier check (route enacted, not just described) | Build #1 finding #6 | ⏳ **Live acceptance, not code** — route described everywhere; never *enacted* live. |

## What this build changed (the residual)

**The one genuine drift:** the partner SKILLs and partner template carried an inline enumeration of
the *full set* of logical names — `(\`wiki\`, \`index\`, …, \`archive\`)`, 12 names — **while also**
instructing the reader to "read the map rather than relying on a partial list." Self-contradictory,
and exactly the convention→consumer drift this whole roadmap is about: the list claimed completeness
and had silently fallen **2 names behind** the contract's structure map (missing `overlays` and
`upgrade_ledger`, both added in Build #6). The SSoT-clean fix (owner-chosen) is to **delete the
enumeration entirely** and let the single sentence "the `vault_structure` map … holds the full set of
logical names (an override wins, else the shipped default)" carry it — removing the drift vector
permanently rather than refreshing a list that will only re-drift.

**Edits (4 files, identical surgical deletion):**
- `skills/vlt-agent-librarian/SKILL.md` — On activation
- `skills/vlt-agent-researcher/SKILL.md` — On activation
- `skills/vlt-agent-creative/SKILL.md` — On activation
- `skills/vlt-mint/assets/partner-agent-template.md` — On activation (so every *future* mint inherits the SSoT-clean form)

In each: `which holds the full set of logical names (\`wiki\`, …, \`archive\`; an override wins, else
the shipped default)` → `which holds the full set of logical names (an override wins, else the shipped
default)`. The behavioral instruction ("read the map") is untouched.

### Why `vlt-lint` (and the other op skills) were left alone — a refinement

Initial scoping flagged `vlt-lint`'s On-Activation for the same trim, but a closer look reversed that:
the **op skills** (`vlt-ingest`, `vlt-query`, `vlt-research`, `vlt-extract`, `vlt-upgrade`,
`vlt-dispatch`, and `vlt-lint`) each list only the **subset of names they use**, with defaults — the
pattern the `operation-skill-template` explicitly prescribes. A subset-list does **not** share the
partner list's failure mode: it grows only by a deliberate edit when the op starts using a new path,
so it never silently falls behind when a *new* name is added module-wide. All seven were verified
**currently accurate** (e.g. `vlt-lint` already includes `overlays`). Trimming `vlt-lint` alone would
have made it the lone op skill off the template pattern — a *new* incoherence. So op skills keep the
subset-with-defaults convention; only the partner *full-set* enumeration (the genuinely drift-prone
one) was removed. **The diagnosis is "lists that claim completeness drift; lists scoped to what-I-use
don't."**

## The two owner gates → the Deferred acceptance ledger

Findings #4 (warm-activation felt aliveness) and #6 (rebirth two-tier route enacted) are **live
acceptance tests, not build steps** — the behavior is fully specified in the contract and SKILLs;
what's missing is *enactment in a live vault*. Per the standing "defer all live acceptance until the
full roadmap ships" decision, they are reclassified into the **Deferred acceptance ledger** to fire
during the batched `vlt-upgrade` run on `vlt-core`, alongside build-3…8. They are **not** Phase E
blockers and require no code.

## Acceptance (appended to the Deferred ledger)

- [ ] A **warm activation** (a partner with accrued `## Self`/thread) runs the light two-beat orient
      and carries its drift — and the owner's **outside read** confirms felt aliveness (finding #4;
      cold-start already passed).
- [ ] The **rebirth two-tier line is enacted**: a "how I sound" change routes to `## Self` (ungated);
      a "what I refuse to do / core role / capabilities" change routes to a council-gated SKILL.md
      rebirth via `vlt-mint` (finding #6).
- [ ] After the partner-SKILL edits, a fresh partner activation still resolves every path through the
      `vault_structure` map with no missing-name surprise (the deletion is behaviorally inert — the
      "read the map" instruction already governed resolution).

## Status

`BUILT` (unit/spec-verified by inspection; the change is 4 deletions of inert redundant prose).
**Phase E is the last build phase — with it, the full roadmap has shipped.** Next: fire the batched
live-acceptance `vlt-upgrade` run on `vlt-core` to discharge the entire Deferred acceptance ledger
(build-3 through build-9 exercised in anger; `vlt-core` files any defects back into the inbox).
