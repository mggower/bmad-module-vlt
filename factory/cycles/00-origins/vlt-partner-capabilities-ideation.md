---
title: 'vlt Partner Capabilities — Slug-Callable Capability Tier (Ideation)'
status: 'BUILT 2026-06-24 → build-7-capability-object.md (the 6-step build roadmap below was implemented 1:1; step 6 folded in since vlt-upgrade now exists). Live acceptance deferred to the batched first-safe vlt-core upgrade.'
module_name: 'Vault (vlt)'
module_code: 'vlt'
module_description: 'Exploring how to give vlt partners lightweight, slug-callable capabilities — a middle tier between "summon a partner" and "mint a whole operation skill"'
architecture: 'enhancement to existing multi-partner module'
standalone: false
expands_module: 'vlt (self)'
skills_planned: []
config_variables: []
created: '2026-06-15'
updated: '2026-06-15'
---

# vlt Partner Capabilities — Slug-Callable Capability Tier (Ideation)

> **Nature of this doc:** Not a new module. This is an architectural-pattern ideation *within* the existing vlt module — how partners acquire and expose capabilities. Captured in vlt's own reports idiom.

## Vision

Give vlt partners a way to acquire capabilities that is *proportional to the capability's weight*. Today the only way to add an ability is to mint a full registered operation skill — too heavy for small, partner-specific abilities, and unable to express "one shared idea, applied differently by each partner" (the `vlt-track` problem) without either a switch-on-identity skill or wasteful duplicate skills.

The answer: make **Capability** a first-class object with two weights. The owner declares only *what it writes*; weight, home, council route, and durability all derive from that. Lightweight capabilities are partner-owned files (or self-grown live), shared ideas become opt-in *families* with thin invariant contracts, and operation skills become simply the heavy weight of the same object. Nothing is duplicated, the single-writer lane discipline is preserved by construction, and the machinery reuses what vlt already ships (identity durability, council derivation, upgrade reconcile).

## Architecture

**Enhancement, not a new module.** Introduce a first-class **Capability** object into the existing vlt multi-partner module. Everything a partner can do is a Capability; an operation skill becomes simply the *heavy* weight. See "Converged model" in Ideas Captured for the spine.

### Capability homes & durability (DECIDED 2026-06-15)

**Principle: a capability's home is determined by its provenance, and lightweight capabilities reuse the partner-identity durability split vlt already ships — no new machinery.**

| Capability provenance | Home | On `vlt-upgrade` |
| --------------------- | ---- | ---------------- |
| **Shipped** (ships with a partner) | shipped skill territory (`skills/` / partner SKILL.md) | replaced ✓ (correct — not the vault's to keep) |
| **Vault-grown, light** (e.g. `vlt-track` grown in vlt-core) | **agent zone**, beside the partner's `identity.md`/`thread.md` | survives ✓ (agent zone is sacred to the installer) |
| **Vault-grown family contract** (shared invariants, Model B) | agent zone, vault-level (`_agent/capabilities/…`, alongside `_agent/mint/`) | survives ✓; invariant change → propagation check |

Two convergences this produces:
- **Family propagation == upgrade reconcile.** A shipped family whose invariants change on upgrade, against vault-grown instances, *is* Model B's propagation hook firing. ("Durability and coherence are the same gap from opposite ends" — roadmap.)
- **Self-grown capabilities are safe.** Because a light capability is council-none and writes only the partner's *own* zone, a partner can grow one mid-conversation without a full mint ceremony — the durability model makes this safe, not scary. (Open: whether self-growth still logs a one-line decision-log entry — see Phase 4.)

### Memory Architecture

Reuses vlt's existing partner zone. A partner discovers its vault-grown capabilities on activation the same way it already reads `identity.md`/`thread.md` — capabilities are *more vault-specific partner state*, not a separate subsystem.

**DECIDED 2026-06-15:**
- **Body home: distributed.** A capability body lives at `{partners}/{name}/capabilities/{slug}.md`, beside the partner's `identity.md`/`thread.md`. Ownership = location. Partner reads this folder on activation.
- **Family contracts: vault-level.** Shared invariants live at `_agent/capabilities/families/{family}.md` (belong to no single partner; survive upgrade).
- **Self-grow logs one line.** A partner that grows a capability mid-conversation appends a featherweight entry to `_agent/mint/decision-log.md` — keeps the vault's evolution trail intact without imposing mint ceremony.

### How vlt-mint drives this (PROPOSED 2026-06-15)

Mint asks one routing question — **"what does this capability write?"** — and everything cascades (same derivation as the schema). The owner never hand-picks light/heavy or council-class.

**Kinds, revised:**
- **`add a capability`** (replaces today's `operation skill` kind). Route by `write_scope`:
  - **own-zone → light.** Write `{partners}/{name}/capabilities/{slug}.md`. Council-none. *May bypass mint entirely* — a partner can self-grow it mid-conversation (logs one line). This is the new featherweight default.
  - **shared-lane → heavy.** Mint a registered op skill via the existing `operation-skill-template`; the capability file is a `skill:` pointer. Must be owned by the lane's rightful owner.
- **`migrate a capability`** (kept, now weight-uniform): light = move the file to another partner's zone (re-own); heavy = re-point ownership. Council-none (additive/reversible).
- **`retire a capability`** (new, symmetric with retire-a-partner): light = delete file + log; heavy = retire the op skill.
- **family ops** (new): `create/extend a family` (gather invariants from instances — additive, flagged not gated); **`change family invariants` → GATED** (cross-partner blast radius — this is the propagation trigger).
- **unchanged kinds:** `new partner`, `persona self-edit`, `convention edit`, `retire a partner`.

**Council-class derivation (auto):**
| Situation | Council |
| --------- | ------- |
| own-zone (light), additive | none |
| heavy, owned by the lane's rightful owner, additive | none *(same as today's op-skill rule)* |
| changes lane ownership / adds a second writer to a lane | **gated** |
| change family invariants | **gated** |
| new partner / persona edit / convention edit / retire partner | **gated** (unchanged) |

Fits Phase C's planned **Ideate → Validate → Build** mint phases cleanly: Ideate (what does it write?) → Validate (lane-safety check + council if gated) → Build (write the file, or mint the op skill).

### The Capability object schema (PROPOSED 2026-06-15)

A capability is a single markdown file: **frontmatter = the object, body = the partner's application.**

**Fields:**

| Field | Meaning | Notes |
| ----- | ------- | ----- |
| `slug` | the addressing handle (e.g. `track`) | unique within an owner; how it's referenced/migrated/headless-called |
| `name` | human name | |
| `description` | one-line | what shows when surfaced |
| `owner` | the partner that owns it | for light caps, also = file location |
| `write_scope` | `own-zone` \| named shared lane e.g. `wiki` | **the single source of truth** — the owner declares only this |
| `weight` | `light` \| `heavy` — **DERIVED** from `write_scope` | own-zone → light; shared-lane → heavy. Never hand-set. |
| `procedure` | the body (light) **or** `skill: vlt-track` (heavy) | mutually exclusive — mirrors BMad's `prompt` vs `skill` |
| `council_class` | auto-derived: `none` if light+additive; `gated` if heavy/lane-writing/family-invariant change | owner never sets this by hand |
| `family` | optional `{ name, inherits: [invariant-ids] }` | present only if opted into a family |
| `provenance` | `shipped` \| `vault-grown` | usually implied by location; explicit for clarity |

**Example — light, vault-grown, family member** (`{partners}/researcher/capabilities/track.md`):
```markdown
---
slug: track
name: Track
description: Keep a live read on the Researcher's open inquiries and nudge stale ones.
owner: researcher
weight: light
write_scope: own-zone        # writes only researcher/thread.md
council_class: none
family: { name: track, inherits: [append-only, own-zone-only, dated-observation] }
provenance: vault-grown
---
## Application
<the Researcher's specific procedure: how IT tracks open inquiries —
 reads thread.md, compares against recent log, surfaces what's gone quiet…>
```

**Example — the family contract** (`_agent/capabilities/families/track.md`):
```markdown
---
family: track
description: A partner keeps a live read on something it owns, over time.
instances: [researcher, librarian, creative]   # derived/maintained
---
## Invariants  (every track instance MUST honor these)
- append-only — a track never overwrites prior observations
- own-zone-only — writes only the owner's own zone, never a shared lane
- dated-observation — every run emits a dated observation entry
```

Heavy capabilities keep their body in the registered op skill; the capability file is just the frontmatter pointer (`procedure: { skill: vlt-track }`, `write_scope: wiki`, `council_class: gated`). This is the unification: **op skill = heavy capability with a `skill:` procedure.**

### Memory Contract

| File | Purpose | Read by | Written by |
| ---- | ------- | ------- | ---------- |
| `{partners}/{name}/capabilities/{slug}.md` | a light capability: object (frontmatter) + application (body) | the owning partner, on activation | the owning partner (mint or self-grow) |
| `_agent/capabilities/families/{family}.md` | shared invariants for a capability family | any partner with an instance | `vlt-mint` (family ops) |
| `_agent/mint/decision-log.md` (existing) | chronological evolution trail | owner/auditors | `vlt-mint` + self-grow (one line each) |

### Cross-Agent Patterns

- **Ownership = location.** A light capability belongs to exactly one partner and lives in that partner's zone. No cross-partner writes (preserves single-writer discipline).
- **Families are the only cross-partner object.** A family contract is shared; its invariants bind every instance. Changing them is gated (cross-partner blast radius) and fires the propagation check.
- **Migration re-owns.** Moving a capability to another partner moves the file (light) or re-points ownership (heavy) — the existing typed hand-off / capability-migration seam, now weight-uniform.

## Skills

This is an enhancement to existing skills, not new standalone skills. Affected:

### vlt-mint (revise)
**Type:** workflow/skill. Add the `add a capability` routing (write_scope → light/heavy), `retire a capability`, and family ops (`create/extend`, `change invariants`=gated). Add a **light-capability-file template** to its assets (alongside operation-skill-template / partner-agent-template). Council-class derivation table embedded. Self-grow path documented (partner grows own-zone capability live + logs one line).

### Partner SKILL.md + vault-operating-contract (revise)
**Type:** agents / governance. Beat-2 "Orient" of the activation ritual gains a step: read `{partners}/{name}/capabilities/`. Partner surfaces capabilities **contextually** (data, not a fixed menu). "What you do" sections become generated/derived from the capability set rather than hand-listed.

### vlt-lint (revise)
**Type:** operation. Add a coherence check: every capability file's declared `write_scope` matches what its body actually writes (lane-safety firewall), and every family instance honors its invariants. This is the propagation/coherence guard (Phase B-aligned).

### vlt-upgrade (future, Phase D)
**Type:** orchestration. The capability agent-zone (`{partners}/*/capabilities/`, `_agent/capabilities/`) is reconciled-not-replaced; family-invariant changes on upgrade fire the same propagation check.

## Configuration

This module requires no custom configuration beyond core BMad settings. Capability homes are conventional paths under the existing partner/agent zones; no new config variables.

## External Dependencies

None. Capabilities are markdown files read/written by existing skills. No new CLI tools or MCP servers.

## UI and Visualization

Optional, not required. A future "capability surface" view (per-vault: what each partner can do, which families exist, where instances diverge) could be valuable but is out of scope for the first build. The contextual-surfacing-by-partner model is the primary UX.

## Setup Extensions

`vlt-setup` scaffolds the empty `_agent/capabilities/families/` directory on install/update. Per-partner `capabilities/` folders are created lazily on first capability (mint or self-grow). No other setup work.

## Integration

This is a self-expansion of vlt. It intersects the **inbox-evolution-roadmap** directly: it pre-stages **Phase B** (the propagation check = convention→consumer coherence), **Phase C** (fits the planned Ideate→Validate→Build mint phases; lightweight tier is a new mint output), and **Phase D** (capability agent-zone reconciliation rides the durability work). Recommend cross-linking this doc from the roadmap rather than treating it as orphan scope.

## Creative Use Cases

- **Self-grown capabilities as relationship memory.** A partner notices it keeps being asked to do a small bounded thing and *grows* a capability for it mid-conversation — the roster literally learns ergonomic shortcuts per-vault, surviving upgrades.
- **Families as cross-partner conventions in miniature.** `track`, `digest`, `watch` — recurring verbs become thin shared contracts, giving the vault a vocabulary of partner behaviors without central code.
- **Lint-surfaced drift as a coaching signal.** When instances of a family drift from their invariants, lint surfaces it — a gentle nudge that an idea has fragmented and might want re-curation (or a deliberate fork into two families).

## Ideas Captured

### The spark (owner's framing)
- How does the BMad agent builder add *new capabilities* to an agent? The vlt default has been "create a new skill," but that isn't always the right paradigm.
- BMad agents carry capabilities callable by a short slug (e.g., `CS` = Create Story). Want to understand that mechanism and consider embedding it into vlt's "partner" model.

### Grounded findings — how BMad does it (researched 2026-06-15)
- BMad agent capabilities live in `customize.toml` as a `[[agent.menu]]` array-of-tables. Each entry has: `code` (the slug, e.g. PRD/CE/CS), `description`, and **exactly one of** `skill = "..."` (invoke a registered skill) OR `prompt = "Read and follow {skill-root}/foo.md"` (run an inline mini-procedure that lives in the agent's own folder).
- Surfaced as a numbered menu on activation; user invokes by slug code, number, fuzzy description match, or direct skill name. Persona in SKILL.md modulates *how* it runs.
- **KEY INSIGHT — the `prompt` tier is the "missing middle."** BMad has TWO weights of capability: (a) heavy = a full registered `skill`; (b) light = a `prompt` file owned by the agent, surfaced via the menu, callable by slug, with NO standalone registration. vlt today only has the heavy tier (minted op skill) — there is no lightweight agent-owned capability.
- Menus merge by `code` across base/team/user override layers (matching code replaces, new code appends) — i.e. capabilities are customizable per-vault without editing the shipped skill.

### Grounded findings — how vlt does it today (researched 2026-06-15)
- vlt partners (Librarian/Researcher/Creative) are in-vault personas (SKILL.md canonical + per-vault identity.md/thread.md), summoned by name; they internally route to operation skills.
- 11 vlt-* skills: 3 partners, 5 operations (ingest/research/query/extract/lint), vlt-mint (self-evolution engine), vlt-review-council (blast-radius gate, a dynamic workflow), vlt-setup.
- **New capability = mint a new operation skill** via vlt-mint's operation-skill-template (or mint a partner). Council-gated for blast-radius kinds; council-NONE for `operation skill` + `capability migration` (additive/reversible).
- **No slug-callable commands today.** `module-help.csv` carries a `menu-code` (LB, IN, RE…) but it's for help/discovery, NOT invocation. Invocation = summon partner by name, partner routes; or headless one-shot op call; or typed hand-off payload between partners.
- Capability *ownership* already exists conceptually: each partner's "What you do" section lists which ops it delegates to, and vlt-mint supports "capability migration" between partners without moving the op skill.

### Owner's framing (decided 2026-06-15)
- **Heat is on TWO things:** (1) the *lightweight capability tier* (vlt has none; minting a full op skill is too heavy for small bounded abilities), and (2) *capabilities as first-class objects* — owned, migratable, composable between partners. The slug-menu *invocation surface* is NOT the goal.
- **Surfacing is contextual, not a fixed menu.** The capability registry should exist as **data**; whether a partner shows it as a menu or weaves it into conversation is a presentation choice the partner makes per-moment. → implication: the slug is an *addressing/identity handle* for a capability-object (makes it referenceable, migratable, callable headless), NOT primarily a CLI command the user types.

### Working synthesis (emerging)
- Reframe: **everything a partner can do is a "Capability."** Some Capabilities are backed by a registered op skill (heavy); some by an inline agent-owned procedure (light). This *unifies* today's split — an operation skill becomes just one weight of capability.
- A Capability object likely carries: `slug` (handle), `name`, `description`, `owner` (partner), `weight` (light=inline procedure / heavy=skill ref), `procedure-pointer` (prompt path OR skill name), `lane`/`write-scope` (must respect single-writer discipline), `council-class` (light+additive = council-none, like today's op-skill + capability-migration kinds).
- Migration becomes uniform: heavy migration already exists in vlt-mint; light capabilities migrate by re-owning the pointer.

### Grounding case study — `vlt-track` (from vlt-core, owner-reported 2026-06-15)
- A `vlt-track` skill was minted, but the friction: **each partner has a unique *application* of the same idea.** A single skill would be a `switch` on partner identity; duplicate skills (vlt-track-librarian/-researcher/-creative) are three registrations of one idea. Both fail.
- **The unit it reveals:** not "a skill" but **"a partner's owned application of a shared idea."** The idea is thin and shared; the body lives with (and is owned by) the partner.
- **Confirms lane-safety:** tracking writes only to the partner's *own* zone (Researcher → its thread.md; Creative → its in-flight deliverables), never a shared lane. So a lightweight capability can be both featherweight AND lane-safe by construction → supports the "light = no foreign-lane writes" rule.
- This is the canonical worked example the lightweight-capability tier must serve.

### The fork this forces: how is the "shared idea" shared? → DECIDED: Model B (2026-06-15)
- **A — Archetype / stamp-and-own (copy):** reusable seed template, used once; instances are strangers after stamping. Zero coupling, no home for the idea, silent drift. (Rejected — loses coherence.)
- **B — Thin contract + free body (hybrid) [CHOSEN]:** a capability *family* carries a short list of **invariants** every instance must obey (e.g. append-only; writes owner's-own-zone only; emits a dated observation); the **body** (what each partner tracks + how) is fully partner-owned. Changing an invariant fires a propagation check (dovetails with Phase B convention→consumer map); changing a body touches nobody else. The invariants are *also where the lane-safety rule lives*, so the contract earns its keep rather than being bureaucracy.
- **C — Living contract (shared body parts):** shared procedure steps run for everyone, partner supplies hook overrides. Most coherent, but re-creates the switch-on-identity coupling that made the single vlt-track skill painful. (Rejected — re-couples.)
- **Caveat accepted:** B costs writing down invariants at mint time. If most lightweight capabilities turn out to be genuine one-offs, the resting point is "A by default, B only when you opt a capability into a *family*." → families are opt-in, not mandatory.

### Converged model so far (end of Phase 2)
1. **Capability is a first-class object.** Everything a partner can do is a Capability. An operation skill is just the *heavy* weight of a capability; a lightweight capability is a partner-owned inline procedure (BMad's `prompt`-tier analogue).
2. **Two weights.** Light = inline procedure owned by one partner, writes only its own zone, council-none (additive/reversible). Heavy = backed by a registered op skill, owns/writes a shared lane, may be council-gated.
3. **Lane-safety as the weight discriminator.** If a capability writes a *shared* lane (e.g. the wiki) it is heavy-by-definition and must be owned by that lane's partner. Light capabilities are read/transform/emit + own-zone-write only.
4. **Families (opt-in) via Model B.** A capability shared across partners is a *family*: thin shared invariants + per-partner body. Opt-in; one-offs need no family.
5. **Surfacing is contextual data, not a fixed menu.** The slug is an addressing/identity handle (referenceable, migratable, headless-callable), not primarily a typed command. Partner reads its capability registry on activation and weaves/menus it per-moment.

### Open tensions / questions to explore (Phase 2)
- Is the right vlt analogue to BMad's `prompt` tier a NEW lightweight capability kind in vlt-mint (council-none, agent-owned, lives in the partner's folder)? Or does it break the "single writer / defined lanes" discipline?
- vlt deliberately uses summon-by-name + internal routing rather than a slug menu. Does a slug menu *help* (discoverability, headless ergonomics) or *fight* the ceremony/relationship feel of a partner?
- Where does a lightweight capability's PROCEDURE live and how does it survive upgrade (Phase D durability concern)? Agent zone vs. shipped skill folder.
- Does this interact with "capability migration" — could capabilities be first-class objects that move between partners regardless of weight?
- Relationship to the existing `menu-code` in module-help.csv — promote it from discovery-only to actually invocable?

## Build Roadmap

Recommended order — each step is independently shippable and de-risks the next:

1. **The Capability object + light-capability template.** Define the schema (frontmatter fields, `procedure` skill-XOR-body, `write_scope`→`weight` derivation) and add the template to `vlt-mint` assets. Foundational; pure convention, no behavior change yet. *Smallest first because everything references it.*
2. **Partner activation reads + surfaces capabilities.** Update the operating-contract Beat-2 Orient and partner SKILL.md to read `{partners}/{name}/capabilities/` and surface contextually. *Now a hand-authored capability file actually does something — provable end-to-end with one test file.*
3. **`vlt-mint` `add a capability` routing + self-grow + retire.** The light/heavy routing by `write_scope`, council-class derivation, and the live self-grow path. *The headline feature; build it once it has a home to write into.*
4. **Families (Model B).** `_agent/capabilities/families/` contract files, `add to family` / `change invariants`(gated) mint ops. *Migrate `vlt-track` into a real family as the acceptance test.*
5. **`vlt-lint` coherence guard.** write_scope-vs-actual-writes firewall + family-invariant conformance. *Built last in this arc — it polices the structures the earlier steps create.*
6. **(Phase D, separate track) `vlt-upgrade` reconciliation** of the capability agent-zone. *Folds into durability work already roadmapped; not blocking the above.*

**Acceptance test threading the whole design:** re-create `vlt-track` as a light, vault-grown capability with a `track` family across Researcher/Librarian/Creative — proving no duplication, no switch-skill, lane-safety held, and survival across a simulated upgrade.

**Next steps:**

1. Enhancement to existing skills, not a fresh module — path is **Edit a Skill / Build a Workflow** against `vlt-mint`, the partner agents, and `vlt-lint`, sharing this plan as context (not Create Module CM).
2. File this as a numbered entry in the **inbox-evolution-roadmap** and cross-link — it pre-stages Phases B/C/D.
