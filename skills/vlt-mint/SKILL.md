---
name: vlt-mint
description: Grow the vault's cast — add a capability (light partner-owned or heavy op skill), mint a new partner, a persona self-edit, a convention edit, migrate or retire a capability, run family ops, or retire a partner. Use when a partner says 'I keep needing X — let me build it', or the user says 'mint a partner', 'add a capability', 'evolve the roster', 'edit my persona', 'move X to Y', or 'retire a partner'. The module's self-evolution engine; a capability every partner can reach for mid-flow.
---

# vlt-mint

## Overview

vlt-mint is how the cast grows itself — the re-homed heart of the old build cycle, minus its ceremony. It mints and owns the full lifecycle of the things that make up the roster. Everything a partner can do is a **Capability** with two weights (see the operating contract's *Capabilities*): **light** (a partner-owned file in its own `capabilities/` zone — featherweight, council-none, even self-growable live) or **heavy** (a registered operation skill — a hand any partner can reach). vlt-mint **adds a capability** (routing by what it writes), **migrates** or **retires** one, runs **family ops** (shared-invariant contracts), mints a **new partner** (*born through a discovery beat and a first-breath*, not hand-assembled), a **persona self-edit** (a partner's deliberate rebirth), a **convention edit**, and **retirement**. It is not a general agent builder — it mints things that fit the **Vault partner contract** specifically, and that narrowness is what keeps it fast and the output coherent. The default is always the cheapest, most reversible form (a light capability — or self-growth, no ceremony); lane-writing and persona-level change are the gated escape hatches. Runs in-flow (a partner reaches for it mid-session) or interactively (a deliberate design conversation).

## Conventions

- Bare paths (e.g. `assets/operation-skill-template.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the `vlt` config is missing, say `vlt-setup` can configure the module and proceed only once a vault root is known.

The vault is this project — resolve every path relative to `{project-root}` through the `vault_structure` map materialized in `config.yaml`: `partners`, `backlog`, `personas`, `conventions`, `contract`, `archive`, `sessions`. The **module skills directory** `{module-skills}` — where the installed `vlt-*` skills live and where minted skills install — is `{project-root}/.claude/skills/` (the vault's own skills, alongside their siblings). Read the current **roster** (the installed `vlt-agent-*` skills in `{module-skills}` + their `customize.toml` `[agent]` blocks) and the `{backlog}` (pick up `capability-gap` items that motivate a mint).

**Resume an in-flight mint.** A gated mint can span sessions (see *The planning doc* in Phase 1). On activation, scan `_agent/mint/` for a planning doc whose checklist is **not** marked complete — a gated mint left mid-flow. If one is found, offer to **resume** it: read it to restore the kind, brief, current phase, council verdict, and open decisions, and continue at the live phase (analogous to a partner reading `identity.md`/`thread.md` to resume). Absent any incomplete doc, proceed to a fresh mint. (The scan is one `ls` of an agent-zone folder; `_agent/mint/` may not exist yet on a vault that has never run a gated mint — that is simply "no mint to resume.")

## Phase 1 — Ideate

Resolve *what's being minted* and — for a partner — *who it becomes*. The work of this phase shapes the **brief** the user approves before any validation or building happens.

### Step 1: Resolve what's being minted

Determine the **kind** and the subject. The kind sets both the path and the council gate; don't guess it — confirm with the caller. The kinds:

- **`add a capability`** — give a partner a new ability. This is the unified entry (it subsumes the old `operation skill` kind); it **routes by `write_scope`** (Step 3): *own-zone → light* (a partner-owned file, council-none, may even be self-grown live) or *a shared lane (e.g. `wiki`) → heavy* (a registered operation skill — today's op-skill path, now understood as the heavy weight). Subject: the capability gap + which partner owns it + what it writes.
- **`migrate a capability`** — change a capability's *owner* (weight-uniform: light = move the file to another partner's zone; heavy = re-point op-skill ownership). Subject: the capability + source/target partners.
- **`retire a capability`** — remove one (light = delete the file + log; heavy = retire the op skill). Subject: the capability.
- **family ops** — `create/extend a family` (gather shared invariants from instances — additive) and **`change family invariants`** (alter a family's contract — cross-partner blast radius). Subject: the family + the invariant change.
- **`new partner`**, **`persona self-edit`**, **`convention edit`**, **`retire a partner`** — as before (the partner brief; the partner + the change; the convention file + its change; the partner to retire).

**The drift boundary:** lightweight voice/tone/manner change is **not** minted — a partner writes that straight to its `identity.md ## Self`, ungated. vlt-mint enters only when a change touches *who the partner fundamentally is* (its non-negotiable, core role, or capabilities), or when accumulated `## Self` drift is being **ratified** into the canonical SKILL.md (a rebirth the partner initiates). (Operating contract § two-tier identity.)

### The becoming conversation (new partner — always)

A partner is **born through a discovery beat**, not hand-assembled — so for a `new partner` the ideation here is where it becomes someone. Shape *who the partner is*: its temperament, its non-negotiable, the core acts it owns, how it carries itself *differently* from the rest of the roster, and (optionally) a default name. Two paths by weight:

- **Native lightweight (default).** Run a short becoming conversation right here — a handful of questions that surface the partner's point of view and edge. This is the cheap, in-flow path; no external dependency.
- **Deliberate (`bmad-agent-builder` escape hatch).** For a rich from-scratch persona, you *may* invoke `bmad-agent-builder` for the discovery, then **map its sanctum output onto the Vault contract**: canonical persona/creed → the partner's SKILL.md persona; the PERSONA *evolution log* → `identity.md ## Self` (a starting register, not empty); `BOND` → `identity.md ## Bond`; capabilities → SKILL.md "What you do" + the operation pool; **`MEMORY` is dropped** (knowledge lives in the shared wiki). If `bmad-agent-builder` isn't installed, fall back to the native path.

This mint-time becoming shapes *who the partner is* (the canonical persona + its starting `## Self`); the partner still runs its own **live first-breath** the first time it meets a real user (Beat 1 of activation), where its `## Bond` and per-vault `## Self` drift accrue. Two distinct moments — don't conflate them. (The **scaffolding** of that partner from the template happens later, in Phase 3 — Phase 1 produces the *brief*, not the files.)

**Horizontal vs vertical partners (archetype guidance).** Most partners are *horizontal* — **function** partners (librarian / researcher / creative) defined by a mode of work that spans domains. A *vertical (**domain**) partner* (e.g. a Language Tutor) is instead defined by a **subject area**. When the becoming conversation reveals a domain partner, expect that it (a) **names its domain self-awarely**, (b) **typically needs its own operation skill** (a domain verb, minted alongside or soon after), and (c) **may need a bounded convention widening** — e.g. the personalized-extraction allowance in `{conventions}/extraction.md` that lets a domain deliverable cite the user's agent-zone state. Recognize the archetype *here* so the brief and the Phase-2 gate account for the op skill and any widening up front. (Keep this light; don't promote "vertical vs horizontal" to a contract concept until real domain partners accumulate.)

### The planning doc (gated kinds — resumable)

For the **gated kinds** (`new partner`, `persona self-edit`, `convention edit`) a mint may span sessions, so its live state is persisted in a **planning doc** — the *resumable* artifact, distinct from the post-hoc **mint decision log** at `_agent/mint/decision-log.md` (written at the end of Phase 3 as the permanent record). The cheap in-flow kinds (`operation skill`, `capability migration`) stay **ceremony-free — no planning doc** (a doc there would tax exactly the fast path the engine protects).

**The decision log lives in the agent zone (durability — build-6).** The permanent mint decision log is `_agent/mint/decision-log.md` — **not** a file inside this skill's own directory. A skill dir under `.claude/skills/vlt-mint/` is clobber-prone: a module upgrade that replaces `vlt-mint/` would destroy a decision log kept there. The agent zone is never overwritten, so the institutional record survives every upgrade. **Migration (idempotent):** if a legacy `.decision-log.md` exists in this skill's directory, move its entries into `_agent/mint/decision-log.md` (creating it if absent) and leave a one-line pointer stub at the old path; a second run finds nothing to move. (This mirrors the `_agent/mint/` home the planning doc already uses.)

- **Create it at the start of Phase 1** at `_agent/mint/{YYYY-MM-DD}-{slug}.md` — agent zone, durable and upgrade-safe; the contract already sanctions ad-hoc `_agent/` owned folders (the `_agent/verification/` precedent), so no contract change is needed. Created **lazily** on the first gated mint.
- **Contents:** the kind; the brief; architecture decisions + rationale; staged-artifact absolute paths; the **current phase + a done/pending checklist**; the council verdict (or "not yet run"); open user-decisions with their resolutions.
- **Update it at each phase boundary** — the exit gates are the write points: after the brief is confirmed (Phase 1), after the verdict + decisions resolve (Phase 2), and on completion (Phase 3).
- The planning doc is *live/resumable*; the decision log (`_agent/mint/decision-log.md`) is *post-hoc/permanent* — **don't conflate them**. On completion, leave the planning doc in place (git has it; the decision log summarizes).

**Exit gate — Phase 1 → 2:** the user has **confirmed the brief** (for a gated kind, the planning doc records the confirmed brief + decisions-so-far). Don't enter validation until the brief is agreed.

## Phase 2 — Validate

Gate the mint through the council where its kind requires it, and resolve every open call before anything goes live.

### Step 2: The blast-radius gate

The blast-radius gate is a **fixed `kind → council` map**, not a per-mint judgment call — and that map is **owned in one place: the `vlt-review-council` workflow** (`KIND_PANEL`), which selects the lenses for each kind. vlt-mint does **not** restate the panel composition (that was a single-home violation). It keeps only the cheap gate predicate — *does this kind need the council at all?*:

- **Council-none — skip the workflow and proceed frictionlessly:**
  - **`add a capability` when it's light or lane-rightful-additive** — an *own-zone (light)* capability (writes only the owning partner's zone), **or** a *heavy* one that the lane's **rightful owner** is adding additively (the old `operation skill` rule). Additive/reversible, no new blast radius.
  - **`migrate a capability`** and **`retire a capability`** (additive/reversible — re-owning or removing an ability the vault already had).
  - **`create/extend a family`** (gathering existing invariants — additive).
- **Gated — gate through the council workflow (Step 2a):**
  - **`add a capability` that changes lane ownership or adds a *second writer* to a shared lane** (a heavy capability writing a lane it doesn't rightfully own — a single-writer-discipline risk).
  - **`change family invariants`** (cross-partner blast radius — every instance must re-conform; this is the propagation trigger).
  - **`new partner`, `persona self-edit`, `convention edit`, `retire a partner`** (as before).

  The workflow picks the lenses by `kind` and returns the verdict; if it is ever handed a none-kind it returns "no review required." **Council-class derives from `write_scope`, never hand-picked:** own-zone → none; heavy-and-lane-rightful-additive → none; lane-ownership-change / second-writer / family-invariant-change → gated.

#### Step 2a: Invoke the council and capture the verdict (mandatory)

Where the map requires a panel, gate the mint through the council **workflow** — do not re-derive a panel from prose:

1. **Stage the pending mint in the live project tree** (not the plugin cache) so the lenses review what will actually go live — write the proposed SKILL.md / edit to its real `{module-skills}` path (or a clearly-marked pending sibling), then point the council at that live, absolute path. (Subagents otherwise resolve files to the plugin cache and would review a stale prior build.)
2. **Invoke** the council via the Workflow tool — `workflow('vlt-review-council', { mode: 'mint', kind, subject, personasPath })` — where `subject` is a tight summary **plus the live absolute path(s)** of the staged mint (the lenses read those paths directly), `kind` drives panel selection, and `personasPath` is the resolved **live** `{personas}` directory (absolute, `{project-root}`-anchored — passing the live path is the plugin-cache fix). It returns a **structured verdict** — `pass` / `revise` (with the specific `changes`) / `reject` (with the `reason`), plus the moderator's four-part synthesis.
3. **Capture is mandatory, not optional.** Before the mint goes live, record the verdict **and its reasoning** in the mint decision log (`_agent/mint/decision-log.md`) for the mint, and annotate the originating `{backlog}` item with the outcome. A gated change must carry its own rationale.
4. **Act on the verdict:** proceed on `pass`; apply the named changes and re-stage on `revise`; stop (and say why) on `reject`.

**Exit gate — Phase 2 → 3:** the council verdict is **resolved** (a `pass`, or a `revise` applied and re-staged to pass) **and** every open user-decision is **ruled**. Council-none kinds (a light or lane-rightful `add a capability`, `migrate a capability`, `retire a capability`, `create/extend a family`) clear this phase *trivially* — the gate predicate returns "no review required" — but still pass *through* it (the phase boundary holds; they just have nothing to validate). For a gated kind, write the verdict + decisions into the planning doc before building.

## Phase 3 — Build

Author the minted thing from the locally-owned scaffold, install and register it, and record the mint. This is where files are written.

### Step 3: Author from the locally-owned scaffold

The contract scaffold is **owned here and never delegated** — it is what guarantees every minted thing activates via the **two-beat ritual** (first breath + orient), respects the single-writer rule, honors the conventions, and keeps its memory in the in-vault `identity.md` + `thread.md`, regardless of how its body was authored.

**Add a capability** (in-flow, common). Route by **`write_scope`** — the one field the owner declares (full schema + templates in `assets/capability-template.md`):

- **Own-zone → light.** Instantiate the *light capability* template into `{partners}/{name}/capabilities/{slug}.md` (frontmatter object + the partner's application body). `weight: light`, `council_class: none` derive automatically. It writes **only the owning partner's own zone** — no shared lane. Register **nothing** in the help CSV (it is partner-zone state, surfaced on activation, not a globally-callable op). Create the partner's `capabilities/` folder lazily. **Self-grow shortcut:** a partner may write this file *itself* mid-conversation without a full mint ceremony — the only ceremony is **one line to `_agent/mint/decision-log.md`** (keeps the evolution trail; the lane-safety of own-zone-only writes makes it safe).
- **Shared lane → heavy.** This is the old `operation skill` path. Instantiate `assets/operation-skill-template.md` into `{module-skills}/vlt-{op}/SKILL.md`, filling the operation's flow; **also** write the thin pointer capability file (`procedure: { skill: vlt-{op} }`, `write_scope: {lane}`, `weight: heavy`) at the owner's `capabilities/{slug}.md` if you want it surfaced there. Then **update the owning partner's "What you do"** and, if the mint came from a `capability-gap` backlog item, flip that item to `## Done`. A heavy capability must be owned by the **lane's rightful partner** (else Step 2 gated it).

**Migrate a capability.** Light = **move the file** `{partners}/{src}/capabilities/{slug}.md` → `{partners}/{dst}/capabilities/{slug}.md` and update its `owner`. Heavy = re-point advertised ownership (the op skill stays put in `{module-skills}`) — see *Migrate a capability between partners* below for the help-registry re-attribution.

**Retire a capability.** Light = delete `{partners}/{name}/capabilities/{slug}.md` + log one line. Heavy = retire the op skill (deregister it, Step 4) — symmetric with *Retire a partner*.

**Family ops (Model B).** `create/extend a family` — write/append `{capabilities}/families/{family}.md` (the *family contract* template: `description` + the `## Invariants` list, where the lane-safety rule lives), and add `family: { name, inherits: [...] }` to each participating instance's frontmatter. `change family invariants` (**gated** — Step 2) — edit the contract's invariants, then **walk every `instances:` partner** and reconcile its capability body to the new invariants (the propagation discipline, mirroring a convention edit's consumer walk); `vlt-lint`'s capability guard is the lint-time net.

**Mint a new partner** — *scaffold the partner shaped in Phase 1's becoming conversation.* The ideation (who the partner is — temperament, non-negotiable, core acts, starting register, optional name, and whether it's a horizontal or vertical archetype) happened in Phase 1; here you instantiate it:

- **Scaffold from the template.** Instantiate `assets/partner-agent-template.md` (SKILL.md + `customize.toml`) into `{module-skills}/vlt-agent-{name}/`, filling persona, non-negotiable, and capabilities from the Phase-1 brief. Then **seed two memory files** at `{partners}/{name}/`: `identity.md` (`name` frontmatter + `## Bond` + `## Self` — seed `## Self` with the distinctive starting register from the becoming conversation so the partner is born with an edge, not blank) and `thread.md` (`## Thread`, empty at birth).

(The partner runs its own **live first-breath** on its first real activation — see Phase 1's note on the two distinct moments. A **vertical/domain** partner typically also gets its own operation skill minted here or soon after, per the Phase-1 archetype guidance.)

**Self-edit a partner (rebirth).** Edit the partner's own SKILL.md persona / non-negotiable / mode, or fold ratified `identity.md ## Self` drift into it. The partner initiates this; the council gates it (full panel, Step 2). Keep `customize.toml`'s `[agent]` metadata in sync if the title/description changed.

**Edit a convention.** Convention files are governance, so a change is **council-gated** (Step 2) regardless of where it lands. But *where* it lands is the first decision — it determines durability across upgrades (see the operating contract, *Durability across upgrades*):

- **Vault-local addition → write the overlay (the default).** If the change *adds* to the convention (a new frontmatter field, a new rule, a new subsection) for **this vault only**, write it to `{overlays}/{name}.overlay.md` — **append-only**, created lazily. **Do not touch the base** in `{conventions}`, **do not bump `version:`**, and **do not walk consumers**: the base is unchanged, so the handshake is undisturbed, and every reader already merges the overlay on read (contract rule). This path is **upgrade-durable by construction** — the overlay lives in the agent zone and survives every refresh. Record the mint + council verdict in the decision log as usual; no handshake ceremony applies.
- **Generic rule change → edit the base + run the handshake.** If the change alters *an existing rule consumers must follow* (a schema field's meaning, a row format, a validation rule) — i.e. it is **generic**, true for every vault — it belongs in the base and should be **filed upstream to the module**. Edit the base and run the coherence handshake below. (An overlay can only add; it cannot change an existing base rule. So a true rule change has no overlay form.)

The convention→consumer dependency map is not hand-kept: it lives in each convention's own `consumers:` frontmatter (seeded from its Writer/validator contract + Reading list), and each consumer pins the version it last reconciled against in its `depends_on:`. The **base-edit** ceremony:

1. **Apply the change** to the file in `{conventions}`; bump its `last_updated`.
2. **Bump the convention's `version:`** — but *only* if the change touches *the rules consumers must follow* (a schema field, a row format, a validation rule). A typo, a `## Reading list` tweak, or prose clarification does **not** bump `version` (that would churn the handshake for nothing).
3. **Read the convention's `consumers:` and walk every listed skill.** For each consumer whose text encodes the changed rule, make the matching edit and **bump its `depends_on` entry** for this convention to the new version (the flat `"name@version"` ack). Reconciliation may legitimately conclude "no edit needed here" — bumping the ack still records that a human verified it against the new version. A consumer's ack covers its own workflow assets (e.g. `vlt-lint` acks for `vlt-lint-full.js`).
4. **Exit gate (mandatory):** the mint cannot close while any `consumers:` skill's `depends_on` still pins the old version. This is the edit-time half of the coherence machinery; `vlt-lint`'s convention-coherence check is the lint-time net that catches drift introduced *outside* this ceremony (a hand edit, or a consumer added later). A base hand-edit in an installed vault also trips `vlt-lint`'s **base-divergence** safety net (base vs `{overlays}/.baseline/`) until it is upstreamed — that is the signal the change should have been overlay-or-upstream. A convention edit registers nothing in the help registry (Step 4) — it only records the mint + council verdict in `.decision-log.md`.

**Migrate a capability between partners — the heavy detail.** (Light migration just moves the file, per *Migrate a capability* above.) For a **heavy** capability the op skill itself does not move (it's a shared hand in `{module-skills}`); only its *advertised ownership* changes. Remove the op from the **source** partner's "What you do" (and any framing that ties it to that partner), add it to the **target** partner's "What you do" in the target's voice, and re-attribute its capability row in the help registry (Step 4). Council: **none**.

**Retire a partner.** Deregister it (Step 4) and **archive its memory** — move both `{partners}/{name}/identity.md` and `thread.md` to `{archive}/_agent/partners/{name}/` — never delete; the relationship history is preserved.

### Step 4: Install and register

- A **light capability** registers **nothing** in the help CSV — it lives in the owning partner's `{partners}/{name}/capabilities/` zone and is surfaced contextually on activation, not as a globally-callable op. (Self-grown ones likewise: the only record is the one-line decision-log entry.)
- A **heavy capability / operation skill** lives at `{module-skills}/vlt-{op}/` and becomes available to any partner; register its capability row in the live help registry `{project-root}/_bmad/module-help.csv` (and mirror it into the install manifest `{module-skills}/vlt-setup/assets/module-help.csv` so a re-install reproduces it).
- A minted **partner** lives at `{module-skills}/vlt-agent-{name}/`; it joins the roster simply by existing there (the active roster is the installed `vlt-agent-*` skills). Register its capability row in `{project-root}/_bmad/module-help.csv`, and add its `[agent]` entry to the install manifest `{module-skills}/vlt-setup/assets/module.yaml` `agents[]` (mirroring the row into that folder's `module-help.csv`).
- A **capability migration** (heavy) updates the help registry attribution for the migrated op (and its mirror) to the new owning partner; no new skill is created. A **light** migration moves the capability file between partner zones — nothing in the registry.
- A **retired capability**: light = the file is deleted (nothing in the registry); heavy = the op skill is deregistered from `module-help.csv` (+ mirror). A **retired** partner is removed from the live `module-help.csv` and from the install manifest (`module.yaml` `agents[]` + `module-help.csv`); its skill folder is removed after its `identity.md` + `thread.md` are archived.
- **Family ops** register nothing in the help CSV — a family contract lives at `{capabilities}/families/{family}.md` (agent zone).

Record the mint: note it in the mint decision log (`_agent/mint/decision-log.md`) (with the council verdict + reasoning where Step 2a applied), and the new skill carries its own. The new skill is loadable on its next activation.

**Exit gate — Phase 3 (done):** the minted thing is **verified** (it loads/activates correctly; a partner's `identity.md`+`thread.md` exist; a registry row resolves), the mint is **recorded** (`_agent/mint/decision-log.md` + the help registry), and for a gated kind the planning doc's checklist is marked complete. Then **offer to commit**. For a **`convention edit`**, the **coherence handshake exit gate** in *Edit a convention* above — every `consumers:` skill's `depends_on` re-pinned to the new `version` — *is* this phase's gate for that kind; it is specified once there, not duplicated here.

## This skill does not…

- Act as a **general** agent/skill builder — it mints only things that fit the Vault contract.
- Touch a partner's `identity.md ## Self` — ungated voice/tone drift is the partner's own write, never a mint.
- **Delete** a retired partner's relationship history — retire archives.
- **Guess** the kind or skip the gate — the kind is named, the `kind → council` map is fixed, and a required verdict is captured before go-live.
- Write canonical wiki pages — that is the Librarian's single-writer role.
