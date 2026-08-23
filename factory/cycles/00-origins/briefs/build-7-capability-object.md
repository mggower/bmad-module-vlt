---
title: 'Build #7 — The Capability Object: a lightweight first-class capability tier + opt-in families (the vlt-track problem)'
status: 'BUILT 2026-06-24 — unit-verified at rest (handshake bipartite-consistent, council.js parses); live acceptance (re-create vlt-track as a light family across 3 partners + survive an upgrade) deferred to the batched first-safe vlt-core upgrade per the roadmap.'
build_log:
  - 'BUILT 2026-06-24 against vlt-partner-capabilities-ideation.md (status complete). Step 1 (schema + template): new skills/vlt-mint/assets/capability-template.md — the Capability object (write_scope is the one declared field; weight/council_class DERIVE), the light-capability file template ({partners}/{name}/capabilities/{slug}.md), the heavy pointer form (procedure: {skill: vlt-op}), and the family-contract template (_agent/capabilities/families/{family}.md with ## Invariants). Step 2 (activation): operating contract gained a "## Capabilities" single-home section (two weights, ownership=location, contextual surfacing, families/Model B) + Beat-2 Orient now reads {partners}/<partner>/capabilities/; new logical names capabilities → _agent/capabilities/ in contract map + module.yaml + vlt-setup table; partner-agent-template + all 3 shipped partners (librarian/researcher/creative) read their capabilities/ folder in Beat 2 + "What you do" reframed as shipped(heavy) vs vault-grown(light). Step 3 (vlt-mint kinds): add-a-capability (subsumes operation-skill; routes by write_scope: own-zone→light file council-none + self-grow shortcut logging one line to _agent/mint/decision-log.md / shared-lane→heavy op skill); migrate/retire a capability (weight-uniform); council-class derivation table; Step-4 register branch (light registers nothing; heavy = op-skill row; families register nothing). Step 4 (families/Model B): family contract + create/extend (none) + change-invariants (GATED, walks instances = propagation). KIND_PANEL in vlt-review-council.js gained add-a-capability (gated lane case: architect/skeptic/pragmatist) + change-family-invariants (architect/skeptic/pragmatist/historian) + migrate/retire/create-extend ([] none) + back-compat aliases for operation-skill/capability-migration. Step 5 (vlt-lint guard): capability lane-safety (lane_violation/scope_mismatch/weight_mismatch/skill_missing) + family-invariant conformance (invariant_violation/instance_missing) + report keys; {capabilities}/{partners} added to lint path resolution. Step 6 (durability, folded in now that vlt-upgrade exists): vlt-setup scaffolds _agent/capabilities/families/ (per-partner capabilities/ lazy); vlt-upgrade pre-flight snapshots the capability zone + reconcile-not-replace + family-invariant propagation check (family_invariant_drift report key) + provision ensures the families home. VERIFIED: full handshake re-checked bipartite-consistent (build-8 added vlt-lint as an extraction@2 consumer — see build-8; all 5 conventions consistent); council.js parses (node --check); capability-template present; all 3 partners read capabilities/; capabilities logical name in all SSoTs. NOT changed: shipped partners keep their hand-listed heavy "What you do" (augmented, not rewritten — ownership=location, additive). Capability ideation plan cross-referenced (its build roadmap steps 1-6 map 1:1 to the above).'
phase: 'Strand — Capability object (threads B/C/D)'
module_code: 'vlt'
created: '2026-06-24'
updated: '2026-06-24'
derives_from:
  - 'skills/reports/vlt-partner-capabilities-ideation.md (status complete — the full plan + 6-step build roadmap)'
  - 'skills/reports/inbox-evolution-roadmap.md (Capability-object strand row)'
ideation_decisions:
  - 'Scope: the full plan (its 6-step roadmap). Step 6 (vlt-upgrade reconciliation) folded in here because build-6 already shipped vlt-upgrade.'
  - 'Capability is a first-class object with two weights; the owner declares only write_scope; weight/home/council-class DERIVE. An operation skill is simply the heavy weight (procedure: {skill:}).'
  - 'Light = own-zone-only partner-owned file (council-none, self-growable live, logs one line). Heavy = registered op skill owning a shared lane (gated only when it writes a lane it does not rightfully own / adds a second writer).'
  - 'Families = Model B (thin shared invariants + per-partner body, opt-in). change-invariants is gated and fires the propagation check (== convention→consumer machinery, applied to capabilities).'
  - 'Surfacing is contextual data, not a fixed menu; slug is an addressing handle. Shipped "What you do" + vault-grown capabilities/ folder are the same object at two provenances.'
  - 'Durability: capability agent-zone (partners/*/capabilities/, _agent/capabilities/) is reconciled-not-replaced; a shipped family invariant change on upgrade fires the same propagation hook (durability == coherence).'
  - 'build-7 lint lane-firewall (write_scope vs actual writes) and build-8 extraction method-traces firewall are SIBLING checks, not merged.'
---

# Build #7 — The Capability Object

## Thesis

`vlt-core` minted a `vlt-track` skill and hit a wall: **each partner has a unique *application* of the same idea.** A single skill would be a `switch` on partner identity; three duplicate skills are three registrations of one idea. Both fail. The unit the friction reveals is not "a skill" but **"a partner's owned application of a shared idea."** And minting a full registered op skill is too heavy for small, partner-specific abilities in the first place — vlt had only the heavy tier.

Build #7 makes **Capability** a first-class object with **two weights**, where the owner declares only **`write_scope`** and everything else (weight, home, council route, durability) *derives*. Light capabilities are partner-owned files (self-growable live); shared ideas become opt-in **families** (thin invariants + free body); operation skills become simply the heavy weight of the same object. Nothing is duplicated, single-writer lane discipline holds by construction, and the machinery **reuses what vlt already ships** — identity durability (agent zone), council derivation, the convention→consumer propagation check (build-4), and the upgrade reconcile (build-6).

## What shipped — the plan's 6 steps

1. **Schema + template** — `vlt-mint/assets/capability-template.md`: the object (write_scope → weight/council_class), the light file form, the heavy pointer form, the family contract.
2. **Activation** — operating contract `## Capabilities` single-home + Beat-2 reads `capabilities/`; new `capabilities` logical name across all SSoTs; partner template + 3 shipped partners read their folder and surface contextually.
3. **vlt-mint kinds** — `add a capability` (routes light/heavy by write_scope; self-grow shortcut), `migrate`/`retire a capability` (weight-uniform), council-class derivation, register branch (light registers nothing).
4. **Families (Model B)** — family contracts under `{capabilities}/families/`; `create/extend` (none) + `change family invariants` (gated, walks instances = propagation); KIND_PANEL updated.
5. **vlt-lint guard** — capability lane-safety (write_scope vs actual writes) + family-invariant conformance + report keys.
6. **Durability (folded in)** — vlt-setup scaffolds the families zone; vlt-upgrade snapshots + reconciles-not-replaces the capability zone and fires the family-invariant propagation check on upgrade.

## Acceptance (deferred — batched to the first safe vlt-core upgrade)

- [ ] Re-create `vlt-track` as a **light, vault-grown** capability with a `track` **family** across Researcher/Librarian/Creative — proving no duplication, no switch-skill, lane-safety held.
- [ ] A partner **self-grows** a light capability mid-conversation (one decision-log line; no full mint).
- [ ] `vlt-lint` flags a deliberately lane-violating light capability and a family-invariant breach.
- [ ] A simulated upgrade with a changed shipped family invariant fires `family_invariant_drift`; the capability zone survives reconcile-not-replace.

## Explicitly NOT in build-7
- Shipped partners' hand-listed heavy "What you do" is **augmented, not rewritten** (ownership = location; additive).
- A bespoke "capability surface" UI (plan §UI — out of scope).
- Promoting `module-help.csv` `menu-code` to an invocation surface (the slug is an addressing handle, not a typed command).
