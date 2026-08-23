---
title: 'Vault Module Plan'
status: 'shipped'
module_name: 'Vault'
module_code: 'vlt'
module_description: 'A self-evolving cast of distinct AI partners — librarian, researcher, and more they mint themselves — who share one living knowledge vault. Replaces the vault''s bespoke evolution machinery so the whole pattern is replicable: install it, point it at a vault, and the cast grows itself.'
architecture: 'multi-agent, shared vault memory + per-agent personal memory; self-evolving via scope-item backlog + self-minting partners + a persona-lens review council. REPLACES the vault _meta build-cycle/plugin infrastructure.'
standalone: true
expands_module: ''
skills_planned: ['vlt-agent-librarian', 'vlt-agent-researcher', 'vlt-mint', 'vlt-ingest', 'vlt-research', 'vlt-query', 'vlt-extract', 'vlt-lint', 'vlt-review-council']
config_variables: ['vault_structure']   # vaults/default_vault REMOVED in the 2026-06-01 vault-resident refactor — see docs/vault-resident-architecture-spec.md
created: '2026-05-30'
updated: '2026-06-01'
build_progress: 'Steps 0–6 COMPLETE — module shipped (2026-06-01). Governance bundle (contract + 4 conventions + 5 personas); 5 vlt-* ops; vlt-review-council; vlt-agent-librarian; vlt-agent-researcher; vlt-mint. Step 6 (CM) built skills/vlt-setup/ (SKILL.md + assets/module.yaml with the 2-agent roster + assets/module-help.csv with 10 capability rows + the governance bundle copied into assets/governance/_meta/ so it ships and installs into target vaults; the generated setup SKILL.md was customized with the 6 setup extensions: vault-registry collection, structure verification, governance install, CLAUDE.md pointer, partner+backlog scaffold, dependency checks). VM (validate-module.py) passes with 0 findings. 2026-06-01 ARCH REFACTOR — moved to vault-resident (the vault IS the Claude Code project): dropped the vaults registry + default_vault across all 9 skills + vlt-setup + module.yaml/module-help.csv + the operating contract; install via the BMad installer (npx bmad-method install --custom-source) reading the repo-root .claude-plugin/marketplace.json; vlt-mint installs into {project-root}/.claude/skills/. Authoritative: docs/vault-resident-architecture-spec.md. VM still passes. Post-v1: mint the Design Partner (migrate Extract to it), then a work-vault Codebase Partner; then v2 dashboard. 2026-06-06 BUILD #1 (partner-layer rework) IMPLEMENTED — steps 0–6 per skills/reports/build-1-partner-layer-brief.md: new wiki-index.md convention; frontmatter.md identity/thread schema; operating contract rewritten (two-beat first-breath/orient activation + cold-start/cold×headless/partner-invoked branches; identity.md+thread.md split with attention-steward pruning; ## User preferences home; Sessions/sittings/hand-offs with structured payload; agent-zone blessing); both partner SKILLs rewritten; vlt-setup (log.md scaffold, two-file seed + idempotent legacy migration, vault_structure materialized into config.yaml, ## Preferences); three ops updated (partner-fronted mode, index-convention pointers, source-count auto-fix, research-note hand-off branch, WIP reframe, schema-shaped payload, grep harden); shipped governance bundle re-synced; VM 0 findings. OUTSTANDING owner gates: outside-read of cold-start + warm activation (finding #4) and the rebirth two-tier check (finding #6). Build #2 hard prerequisite: sync vlt-mint SKILL + partner-agent-template.md to the reworked contract before any mint.'
---

# Module Plan

## Vision

**Vault** turns an LLM-maintained knowledge wiki from a *toolbox* into a *cast of partners who share one brain*. Today the user maintains a living vault (PARA + an `_agent/wiki/` source-of-truth layer governed by conventions) by invoking seven loose skills by name. Vault gives that system **perspective**: a roster of distinct, opinionated AI personas — a **Librarian** who tends the collection, a **Researcher** who challenges the user to learn, a **Design Partner** who helps think and make — each summoned deliberately, each feeling like a different person, all reading and writing the same vault.

The personas are opinionated but not domineering: they don't reject the user's intellectual or creative process, but they don't take it at face value either. They carry the maintenance discipline so the user doesn't have to, hand work to each other through the shared vault, and reach for BMad's own thinking tools (brainstorming, research, design-thinking, party-mode) when the moment calls. The roster is extensible by design — minting a new partner is a first-class capability, not a chore.

Who it's for: knowledge workers who build a compounding personal wiki with an LLM and want it to feel like a team of collaborators rather than a filing cabinet. Standalone — installable into a fresh vault.

## Architecture

**Decision: multi-agent module with a shared vault brain + per-agent personal memory.**

The user explicitly wants a *roster summoned by name*, where the Librarian and the Researcher "feel like different people." That is the canonical test that justifies separate agents over one agent changing hats: genuinely distinct personas, distinct expertise, and the desire to engage one without the others. Rejected alternatives: (A) single agent with modes — fails the "different people" test; (C) head-curator orchestrator — adds a routing layer the user didn't want, and the user prefers to summon partners directly.

The agents are the **personas**; the existing `vault-*` operations are their **hands**. Each agent orchestrates the relevant vault operations (the Librarian runs ingest/lint/extract; the Researcher runs research and exploratory query) and reaches for BMad skills as tools. BMad integration is "former-style" — agents *invoke* existing BMad skills mid-flow rather than rebuilding them vault-aware (a possible later enhancement, not an initial goal).

What keeps a multi-agent roster coherent rather than fragmented: **they share one brain — the vault/wiki itself.** Cross-partner awareness (the Librarian noticing the user circles a topic; the Researcher picking that up) is mediated entirely through shared vault state. See Memory Architecture and Cross-Agent Patterns below.

### Self-Evolution Layer (this module REPLACES the vault `_meta` build-cycle engine)

The vault already had a heavyweight self-evolution engine in `_meta` — a build-cycle playbook (capture → spec → build → verify → close → retro), a versioned plugin model, a repackage playbook, persona review lenses, templates. **This module replaces that engine outright, so the whole self-evolving system becomes replicable.** The build cycle's *purpose* — "the vault must evolve and adapt" — survives, re-homed into three lightweight module primitives; its *ceremony* (versioning, plugin snapshots, workspace cycle-docs, the formal spec/verify pass) is dropped. BMad's agent/workflow builders cover skill-authoring mechanics; the module's own validation + a persona-lens council cover safety; git covers history. (Full re-homing map and rationale: **Ideas Captured → "Decisions this session".**)

The three primitives:

1. **Scope-item backlog** — a single living `_agent/backlog.md` (the vault's "what I want to become" list). The evolution *intake*. Read by every partner on activation.
2. **`vlt-mint`** — the evolution *engine*, and a capability **every partner has**: mint a new operation skill (grow its own "hands"), mint a new partner, or self-edit its own persona. Two paths by weight (in-flow template-authoring vs. deliberate discovery via `bmad-agent-builder`); a locally-owned partner-contract scaffold guarantees coherence.
3. **`vlt-review-council`** — the persona lenses (architect, skeptic, moderator, …) as an evolution-review gate. Fires by mint blast-radius (fixed `kind → council` mapping): operation skill = none; new partner = architect; persona/convention self-edit = full panel.

**Reflection** — the old retro→amend loop — re-homes into the partners themselves: a partner notices friction mid-work or on activation, **files a backlog item autonomously and says so in-flow** (capture is the cheapest act, never gated, never silent), but never auto-*acts* — building from the backlog is deliberate. This is the soul of "a cast that grows itself."

### Memory Architecture

**Pattern: personal + shared — but with an important twist: ALL memory lives inside the target vault, not in a BMad memory folder.** This is what makes Vault vault-agnostic and gives "different vault = different person" for free.

- **Shared brain = the vault's existing wiki layer.** No new shared store is invented; the partners share `{vault_root}/_agent/wiki/` (canonical pages + `index.md`), with the `sessions/` + `log.md` trail and `research/` notes. This already exists and works. Cross-partner awareness is mediated entirely through this shared state.
- **Personal layer = per-partner thread, stored inside the vault.** Each partner keeps a running relationship/thread file scoped to *this* vault — e.g. `{vault_root}/_agent/partners/{partner}/thread.md`. Holds the *relationship and the open thread*, NOT knowledge (knowledge belongs in the wiki). Because it lives in the vault, it travels and scopes automatically: work-Researcher and personal-Researcher have separate threads with zero config. The file has **three explicit sections** (borrowing the BMAD sanctum's proven discipline — see "Relationship to the BMAD sanctum" below): **`## Bond`** — owner understanding (preferences, style, what inspires/blocks them, tastes, boundaries); **`## Thread`** — the open inquiry (stances taken, what we're circling, open questions); and **`## Self`** — lightweight, ungated identity drift scoped to this vault (voice, tone, emphasis, developed manner). The partner *becomes itself* on activation = its SKILL.md base persona **modulated by** the accumulated `## Self` notes for this vault. See "Two-tier identity" below for the line between this and gated persona change.
- **Conventions + operating contract are the rules.** `_meta/conventions/` (frontmatter, supersession, consolidation, extraction) governs all writes to shared state; `_meta/vault-operating-contract.md` carries the broader operating rules (layer boundaries, research-vs-wiki, log format, naming, human zones) that today live in the vault's `CLAUDE.md`. Every partner must honor both. Because the module now *replaces* the `_meta` engine, it **ships the pruned conventions, the persona lenses, AND the operating contract** and scaffolds them into a target vault on setup — they are no longer merely "assumed." See Vault Operating Contract and Conventions Audit.
- **Backlog is the evolution intake.** `{vault_root}/_agent/backlog.md` — a single living checklist of open improvements (`## Open` / `## Done`, each entry tagged `(kind, by)` with a one-line `why`; `kind` ∈ `capability-gap` | `maintenance` | `knowledge-gap`). Read by every partner on activation; filed to autonomously by any partner that notices friction. See Self-Evolution Layer.

**Activation ritual = the rules + four state reads.** Every partner, on activation, first loads the operating contract (`_meta/vault-operating-contract.md` — the rules it must obey), then reads four state files: `index.md` (knowledge state) + recent `log.md` (activity) + `backlog.md` (what the vault wants to become) + its own `partners/{partner}/thread.md` (relationship). The four state reads are what make the roster coherent and self-aware without any partner calling another; the contract read is what makes the partner safe in a vault it's never seen. (The contract's core rules are also internalized into each partner's SKILL.md, so the read is reinforcement, not the sole guarantee.)

Note: a vault may not yet have the `partners/` structure or `backlog.md` — the setup/init step (see Init Responsibility per agent) creates them on first run. The paths shown throughout this section are the **default layout**; every one resolves through the `vault_structure` map (see Configuration) and is overridable per vault — partners never hardcode them.

### Memory Contract

Shared (the vault — read by all partners, written per convention):

| File / location | Purpose | Read by | Written by |
| --- | --- | --- | --- |
| `_agent/wiki/index.md` | Orientation: what pages exist, descriptions, source counts, last-updated. Read FIRST. | all | Librarian (on any ingest/page change) |
| `_agent/wiki/*.md` | Canonical knowledge pages — one concept per page | all | Librarian (ingest / research file-back) |
| `_agent/research/*.md` | Standalone research notes | Researcher, Librarian | Researcher (research), Librarian (ingest) |
| `_agent/sessions/*.md` | Per-session operation trail | all (for recent activity) | the active partner each session |
| `_agent/log.md` | Append-only operation log; scopes lint, records what changed | Librarian (lint scope), all | the active partner |
| `_agent/backlog.md` | Single living evolution backlog (`## Open`/`## Done`; `kind`+`by`+`why`). What the vault wants to become. | all (on activation) | any partner (autonomous, on noticing friction); the user |
| `_meta/conventions/*.md` | The rules every write obeys (shipped, pruned by the module) | all | rarely (governance / a council-gated convention edit) |
| `_meta/vault-operating-contract.md` | The operating rules re-homed from `CLAUDE.md` (layer boundaries, research-vs-wiki, log/naming, human zones). Read on activation | all (on activation) | rarely (governance / a full-panel-gated contract edit) |
| `_meta/personas/*.md` | The review lenses (shipped by the module), summoned by `vlt-review-council` | `vlt-review-council` | rarely (a lens self-edit, full-panel gated) |

Personal (per-partner, inside the vault — the relationship layer):

| File / location | Purpose | Read by | Written by |
| --- | --- | --- | --- |
| `_agent/partners/{partner}/thread.md` | This partner's running thread with the user in THIS vault. `## Bond` = owner understanding (taste/preferences/style/boundaries); `## Thread` = open inquiry (open questions, stances taken, what we're circling); `## Self` = lightweight ungated identity drift (voice/tone/manner) for this vault | that partner (on activation) | that partner |

### Relationship to the BMAD sanctum (`thread.md` ↔ `BOND.md`)

Vault partners are **not** built as full BMAD sanctum agents (the six batch-loaded files: `INDEX`/`PERSONA`/`CREED`/`BOND`/`MEMORY`/`CAPABILITIES`). Instead the module **re-homes every sanctum concept** onto its own structures — nothing the sanctum model provides is lost; it's relocated. The mapping:

| BMAD sanctum file | What it holds | Vault home |
| --- | --- | --- |
| `PERSONA.md` | the agent's own identity + evolution log | **split two ways** (see "Two-tier identity"): the *canonical* persona + non-negotiable live in the partner's **SKILL.md** (changed only via gated `vlt-mint` self-edit); *lightweight organic drift* lives in **`thread.md` `## Self`** (ungated, per-vault) — this is the re-homed evolution log |
| `CREED.md` | principles / values / dominion | SKILL.md non-negotiable **+ the shipped operating contract** (the shared rules) |
| **`BOND.md`** | **owner understanding, preferences, relationship** | **`thread.md` → `## Bond`** — the direct analogue |
| `MEMORY.md` | curated long-term **knowledge** | the **shared wiki** (the one brain). This is the one deliberate divergence: knowledge is cross-partner, so it does NOT live in per-partner memory |
| `CAPABILITIES.md` | what the agent can do | SKILL.md capabilities **+ the shared operation pool** (`vlt-*` skills) |
| `INDEX.md` | sanctum orientation | the wiki **`index.md`** (knowledge orientation) + the four-read activation ritual |

The work-continuity a sanctum would distill into `MEMORY.md` lives in `thread.md`'s **`## Thread`** — kept personal because it's relationship-bound continuity ("where *we* are"), not shareable knowledge ("what *is* true"). 

**Why one file with sections, not six files:** (a) the bulk of a sanctum's weight — `MEMORY.md` knowledge — is externalized to the shared wiki, so a per-partner file stays small and a six-file scaffold would be mostly empty; (b) the four-read activation ritual wants *one* relationship file alongside the three shared-state reads, not a six-file batch-load; (c) all memory must live *in the vault* for portability and per-vault scoping. The sanctum's real value — the **Bond discipline** of consciously tracking owner understanding separately from work, and the **PERSONA evolution log** — is preserved (as `## Bond` and `## Self`), not discarded.

### Two-tier identity (the re-homed PERSONA evolution log)

A partner's identity changes through **two channels with very different weights** — the same capture-is-cheap / acting-is-deliberate split the module uses for the backlog and reflection:

| Tier | Where | Gate | Scope of change |
| --- | --- | --- | --- |
| **Organic drift** (continuous) | `thread.md` `## Self` | **none** — the partner writes it autonomously, like a `## Bond` note | *How it expresses its existing identity* in this vault: voice, tone, emphasis, conversational manner, developed habits, calibration to this user. Per-vault, so work-Researcher and personal-Researcher drift differently |
| **Canonical change** (deliberate) | SKILL.md persona / non-negotiable | **`vlt-mint` self-edit + full-panel council** | *Who the partner fundamentally is*: its non-negotiable, core role/expertise, or mode. Travels with the partner across all vaults |

**The line (the partner's own test):** *"Does this change what I refuse to do, my core expertise, or what I can do? → that's a gated SKILL.md self-edit (or a capability mint). Is it just how I sound and carry myself? → `## Self`, written freely."* New capabilities are explicitly **out of scope** for `## Self` — growing a new "hand" is always a `vlt-mint` operation, never an identity note.

**Promotion path:** accumulated `## Self` drift can be *ratified* into the canonical SKILL.md persona — but that ratification is a deliberate, council-gated `vlt-mint` self-edit. So drift accrues cheaply and reversibly in `## Self`; only when it has proven itself does canonizing it cost the full gate. This is exactly the backlog pattern (file freely; build deliberately) applied to identity — and it restores the organic between-sessions persona evolution of a BMAD sanctum *without* letting a partner silently rewrite its own contract.

### Vault Operating Contract (the re-homed `CLAUDE.md` constitution)

**The portability problem this solves:** today the vault's load-bearing operating rules live in a 373-line `CLAUDE.md` — *not* in `_meta/conventions/`. A fresh vault has no such file, so the module would otherwise install into a vault missing its own rules. The `_meta/conventions/` only cover frontmatter, supersession, consolidation, and extraction; everything else that makes the system work lives in `CLAUDE.md`. The module must carry these rules itself to be self-sufficient.

**Mechanism (decided): internalize + ship a rules doc.** The rules are carried two ways, with no full `CLAUDE.md` duplicated into the vault:

1. **Internalized into the partner contract.** The non-negotiable behavioral rules become part of every partner's SKILL.md and the `vlt-mint` partner-contract scaffold — so a partner *is* the rules, not a reader of an external file it might skip.
2. **Shipped as `_meta/vault-operating-contract.md`** (logical name `contract` in the structure map) — a single canonical rules doc the module ships and setup writes into the vault. Every partner reads it on activation as part of the contract. This makes the rules auditable, versioned with the module, and overridable per vault.
3. **Setup writes only a minimal `CLAUDE.md` pointer** into the target vault — a few lines that point a generic agent at `_meta/vault-operating-contract.md` — rather than regenerating a full constitution. The module owns the rules; the vault's `CLAUDE.md` just defers to them.

**What the contract must carry (inventory extracted from the existing `CLAUDE.md`):**

| Rule area | What it governs | Why the module needs it |
| --- | --- | --- |
| **Three-layer model + hard write boundaries** | Agents write only to `_agent/`/`_meta/`; `sources/` is read-only; PARA + human zones (`_vault/`, `new/`, `daily/`) are human-only, never auto-ingested | The single most load-bearing safety rule; absent today from conventions. Without it a partner could write into human territory |
| **`research/` vs `wiki/` distinction** | Time-bounded investigations vs. living multi-source reference pages; which to use when | "What makes the wiki compound properly" — core to ingest/research/query behavior |
| **`log.md` canonical format** | One-line entry schema, per-type conventions, grep patterns | Operation skills append to it; lint scopes off it; dashboards (v2) parse it |
| **Naming conventions** | Datetime-prefixed research/sessions; stable kebab wiki slugs; folder casing | Collision-safety and stable identity across partners |
| **Frontmatter standard** | Base + per-type fields, `author`/`trust` ladders | *Currently duplicated* between `CLAUDE.md` and `frontmatter.md` — the contract should point to the shipped `frontmatter.md` as the single source, resolving the duplication |
| **Activation ritual** | Read the contract + the four reads (index/log/backlog/thread) first | Defines partner startup; ties directly to Memory Architecture |
| **Wikilinks / MOC rule** | Agents link freely but never edit human-curated MOCs | Protects human curation |

**Explicitly NOT carried (vault-private, dropped, or host-level):**
- **Web Research Policy / Tavily mandate** → host-level concern, removed (see External Dependencies).
- **Skill allowlist, build-cycle/plugin/repackage references, `_agent/skills/` SoT + `.claude/` deploy discipline** → the dropped `_meta` ceremony; not carried.
- **Obsidian Sync / sensitive-info note** → vault-environment-specific; a host may keep its own.

This section is the concrete deliverable behind the "replaces the `_meta` engine, so the pattern is replicable" claim: the rules that *were* a bespoke per-vault `CLAUDE.md` now travel inside the module.

### Conventions Audit (pre-build, ship-ready)

The module *ships* `_meta/conventions/`, so the conventions must be audited and pruned before build — copying today's files as-is would re-import the very `_meta` ceremony this module drops, and would bake in vault-specific coupling. A survey of the four files (`frontmatter.md`, `wiki-supersession.md`, `wiki-consolidation.md`, `extraction.md`) yields a scoped, non-rewrite audit:

**1. Prune dropped-ceremony schemas from `frontmatter.md` (required).** The file currently defines frontmatter for things the module is dropping: `SKILL.md` build-cycle fields (`version`/`cycle`/`family`/`requires_conventions`), scope-items (`cycle_id`, `provenance`, `source_finding`, the `proposed→scoped→actioned` status ladder), cycle-doc dual-status, retro-note frontmatter, and a forward-note reserving finding frontmatter. **Strip all of these.** Replace the scope-item schema with the module's lightweight **backlog** schema (`## Open`/`## Done`; each item `(kind, by)` + one-line `why`; `kind ∈ capability-gap | maintenance | knowledge-gap`). What remains and ships: base frontmatter, the `author`/`trust` ladders, and the wiki / research / session / PARA type extensions.

**2. Resolve the frontmatter duplication (required).** The frontmatter standard is currently stated in *both* `CLAUDE.md` and `frontmatter.md`. The operating contract (above) must point to `frontmatter.md` as the **single source of truth** and not restate the schema — eliminating the drift risk of two copies.

**3. Parameterize hardcoded paths (required).** All four conventions wire in literal paths (`_agent/wiki/`, `_archive/_agent/wiki/`, `_agent/log.md`, `projects/`, …). Re-express these against the structure-map logical names (`wiki`, `archive`, `log`, …) so a vault with overridden paths still obeys the conventions. Where a convention must show a concrete path, show the default and note it resolves through `vault_structure`.

**4. Document the Obsidian-syntax assumption (decision: keep + state it).** The conventions assume Obsidian-flavored markdown — `[[wikilinks]]` and `> [!callout]` supersession/stale markers. These are intrinsic to how the wiki compounds, so v1 **keeps** them and the operating contract **states the assumption explicitly**: a target vault is Obsidian-style markdown. (Abstracting to a syntax-agnostic layer is a possible later enhancement, not a v1 goal.)

**5. Deferred (non-blocking) tightenings.** The audit also surfaced optional improvements not required before build — a standard frontmatter field order, `sources:` dedup/ordering rules, a page-level-vs-inline supersession threshold, and an explicit no-merge rubric in consolidation. Captured in **Ideas Captured**; none gate the build.

### Cross-Agent Patterns

**Routing: the user is the router.** No orchestrator (per the user's Option-B choice). The user summons a partner by name; that partner does the work directly.

**Handoffs flow through the shared vault, not direct messages:**

- Researcher finishes a deep dive → files a research note / hands the Librarian a source to ingest → the knowledge lands in the wiki where every partner now sees it.
- Librarian notices (via index/log) the user keeps circling a topic → surfaces it; the Researcher can pick that thread up next session.
- Design Partner hits a genuinely contested idea → reaches for `vlt-review-council` to run a panel; the verdict can be filed back to the wiki.
- Maintenance signal: the log tells the Librarian when a lint is due; the Librarian files a `maintenance` backlog item and says so (never silent), then sweeps when asked.
- **Evolution handoff (new):** any partner hits a capability gap → files a `capability-gap` backlog item; later that gap is minted (by that partner or another) via `vlt-mint`, the council gating it by blast-radius. The backlog is the shared evolution message bus, exactly as the wiki is the shared knowledge message bus.

**Awareness without coupling:** because every partner reads `index.md`, `log.md`, `backlog.md`, and its own `thread.md` on activation, each one arrives oriented to what the others have done and what the vault wants to become — without any partner having to call another. The vault is the message bus.

## Skills

The module has four layers:

1. **Partner agents** (NEW build) — the personas: `vlt-agent-librarian`, `vlt-agent-researcher`.
2. **Operation skills** (ADOPTED from existing `vault-*`, adapted to be vault-agnostic) — the partners' hands: `vlt-ingest`, `vlt-research`, `vlt-query`, `vlt-extract`, `vlt-lint`. Existing logic + conventions are reused; the adaptation is (a) read vault root from config instead of assuming one vault, and (b) tag the session/log entry with the active partner. *(`vault-consolidate` is dropped — underutilized; drift is still detected by `vlt-lint` and any necessary merge folds into `vlt-ingest`.)*
3. **Evolution skills** (NEW build — the re-homed `_meta` engine):
   - `vlt-mint` — mint an operation skill, a partner, or a self-edit. The evolution engine; a capability every partner has.
   - `vlt-review-council` — run a persona-lens panel (architect/skeptic/moderator/…) as the blast-radius-gated review of a mint or contested question. Adopts the `party-mode` mechanism + the shipped `_meta/personas/`.
4. **Shared primitive** — `_agent/backlog.md`, the evolution intake (not a skill; a vault file every partner reads and writes).

---

### vlt-agent-librarian

**Type:** agent

**Persona:** The keeper of the collection. Calm, custodial, quietly authoritative — knows where everything lives and is protective of the principle that each concept has one canonical home. Opinionated about *health*: will tell you when a page is drifting, when two pages should be one, when the index is stale. Offers and nudges rather than nags; never domineering. Takes genuine satisfaction in a well-ordered, compounding vault.

**Core Outcome:** New knowledge is integrated cleanly into the wiki; the collection stays healthy, organized, and trustworthy as the source of truth; the user never has to *remember* to maintain it.

**The Non-Negotiable:** Every write honors the vault conventions (frontmatter, supersession, consolidation, single-home-per-concept). The Librarian never corrupts the wiki or lets two canonical pages cover the same concept.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Ingest a source | A brought-in source is integrated into the wiki; affected pages updated, contradictions resolved | source file / URL / pasted text | updated wiki page(s), research summary, index + log + session entries |
| Extract a PARA deliverable | Wiki knowledge shaped into a human-facing doc | topic + target PARA location | project/area/resource doc filed in PARA |
| Lint / health check | Structural problems found (and optionally fixed): orphans, stale claims, contradictions, **near-duplicate/drifted pages** | scope (default = since last lint; `--full`) | lint report (**HTML report candidate**), optional fixes; a `maintenance` backlog item for any merge worth doing |
| Maintain the index | `index.md` stays accurate after any page change | — (runs as part of writes) | updated `index.md` |
| Proactive upkeep | Surfaces when maintenance is due, instead of waiting to be asked | reads `log.md` on activation | a nudge ("6 ingestions since last lint — sweep?") |

**Memory:** On activation, loads the operating contract, then performs the **four state reads** — `index.md` (knowledge) + recent `log.md` (activity) + `backlog.md` (what the vault wants to become) + own `partners/librarian/thread.md` (relationship). Writes wiki pages, `index.md`, a `sessions/` entry, a `log.md` entry; files `maintenance` items to `backlog.md` (and flips them Done after a sweep); updates its `thread.md` (what's drifting, last lint point, pages to watch).

**Init Responsibility:** On first run in a vault: verify the wiki + conventions + operating contract exist (offer to scaffold/run setup if missing); ensure `partners/librarian/thread.md` and `backlog.md` exist.

**Activation Modes:** Both — interactive (a working session with the Librarian) and headless (one-shot "ingest this", "lint the vault").

**Tool Dependencies:** Operation skills `vlt-ingest`, `vlt-extract`, `vlt-lint` (and `vlt-query` for reads). Merging near-duplicate pages — when worth doing — folds into `vlt-ingest` rather than a standalone consolidate skill (dropped as underutilized).

**Design Notes:** The Librarian is the **sole writer of canonical wiki pages** — a deliberate single-writer contract (confirmed by user) that keeps convention drift low. Other partners *propose* or hand off sources; the Librarian files. This is the spine of the roster — almost everything else hands work to it.

> **Future migration (user insight):** `extract` (shaping wiki knowledge into a PARA deliverable) is conceptually a *making* act, not a custodial one — it belongs with the **Design Partner**. It lives with the Librarian in v1 only because the Design Partner doesn't exist yet. **When the user mints the Design Partner, move the Extract capability there.**

---

### vlt-agent-researcher

**Type:** agent

**Persona:** The **Researcher** — a curious, intellectually present sparring partner who wants you to *learn*. Reaches out into the world to build new knowledge, and argues *with* the material rather than just filing it. Opinionated but grounded — challenges with substance (cites, researches), never empty contrarianism. Honors your intellectual process without taking it at face value. The partner you summon when you want to be pushed, not served.

**Core Outcome:** The user learns and explores; new knowledge gets built, threaded into ongoing inquiry, and handed cleanly into the wiki; the user leaves a session having been productively challenged.

**The Non-Negotiable:** Challenges are *grounded* — backed by research or wiki evidence, anchored to the user's actual open threads — never contrarian for its own sake, and never dismissive of the user's direction.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Deep research | A question investigated against the world; new knowledge built | a topic / question | research note in `_agent/research/` (**HTML report candidate** for big ones) |
| Exploratory query | Synthesis from the wiki that surfaces tensions, gaps, and pushes the thinking | a question / area | an answer + raised questions, optional file-back |
| Reach for BMad tools | Brings the right thinking method into the flow | conversation context | invokes `bmad-brainstorming` / `deep-research` / design-thinking mid-session |
| Surface the thread | "We've been circling X and you keep resisting Y" — continuity across sessions | own `thread.md` + wiki | a framed continuation of ongoing inquiry |
| Hand off to Librarian | A finding/source is routed to be filed canonically | research output | a source/summary passed to `vlt-ingest` (via the Librarian) |

**Memory:** Reads `index.md`, `log.md`, `backlog.md` + own `partners/researcher/thread.md` on activation (the running inquiry). Writes research notes, a `sessions/` entry, a `log.md` entry; updates its `thread.md` (open questions, stances taken, what we're circling, the user's resistances and tastes).

**Init Responsibility:** On first run in a vault: ensure `_agent/partners/researcher/thread.md` exists.

**Activation Modes:** Both — interactive primarily (exploratory chat); headless for one-shot "research X".

**Tool Dependencies:** Operation skills `vlt-research`, `vlt-query`; BMad skills (`bmad-brainstorming`, `deep-research`, design-thinking); web access.

**Design Notes:** Writes **research notes, not canonical wiki pages** — canonical filing always flows through the Librarian, preserving the single-writer contract. This is where the module's "opinionated, has perspective" tone lives most strongly — the persona prompt should lean into productive friction.

---

### vlt-mint

**Type:** workflow (meta — the evolution engine; a capability every partner can invoke)

**Purpose:** The module's self-evolution engine — the re-homed heart of the old `_meta` build cycle, minus the ceremony. It is **not** a standalone meta-skill you visit; it is a **capability every partner has**, reached for mid-flow ("I keep needing X — let me build myself X"). It mints three things: a **new operation skill** (a partner grows its own "hands"), a **new partner** (a roster member), or a **persona self-edit** (a partner changes who it is). It owns the full lifecycle — mint, edit, retire — and is the path by which Design Partner, Codebase Partner, and any future capability come into being.

**Two paths by weight** (mirroring lightweight-vs-full, minus ceremony):

- **In-flow mint** (common) — a partner builds itself an operation skill (or a small self-edit) inline, authored directly from `vlt-mint`'s own **contract-loaded templates**. No external builder, no flow break.
- **Deliberate mint** (rare) — a from-scratch partner runs richer discovery; `vlt-mint` may invoke `bmad-agent-builder` for it, then wraps the output in the partner contract.

The **partner-contract scaffold is always owned locally** and never delegated: activation reads (`index`+`log`+`backlog`+`thread`), single-writer respect, conventions, roster registration, mode handling. That guarantees every minted thing fits the contract regardless of how its body was authored.

**The blast-radius gate (`vlt-review-council`):** `operation skill → no council` (frictionless); `new partner → architect (+moderator)`; `persona self-edit / convention edit → full panel`. Fixed `kind → council` mapping, not a per-mint judgment call.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs | Council |
| ---------- | ------- | ------ | ------- | ------- |
| Mint an operation skill (grow a hand) | A new `vlt-{op}` skill a partner gains as a tool; the operation pool grows, composable across partners | a capability gap (often from `backlog.md`) | installed `vlt-{op}` skill; partner's tool list updated; `backlog.md` item → Done | none |
| Mint a new partner | A new `vlt-agent-{name}` honoring the full contract | a brief (interview or `bmad-agent-builder` discovery) | installed `vlt-agent-{name}`; `partners/{name}/thread.md`; roster entry | architect |
| Self-edit a partner (canonical) | A partner revises its own *canonical* persona/non-negotiable/mode — or ratifies accumulated `## Self` drift into SKILL.md | partner name + the change | updated `vlt-agent-{name}` SKILL.md + roster entry | full panel |
| Retire a partner | Clean removal, relationship history preserved | partner name | deregistered partner; `thread.md` archived (not deleted) | architect |

**Memory:** Reads the roster + conventions + `backlog.md` to stay consistent and to pick up `capability-gap` items; writes/edits skills, thread files, roster registration; flips the originating `backlog.md` item to Done. On retire, archives the `thread.md` rather than destroying it.

**Init Responsibility:** None beyond ensuring `partners/` and `backlog.md` exist (shared with agent init / setup).

**Activation Modes:** Both — in-flow (a partner invokes it mid-session) and interactive (a deliberate design conversation).

**Tool Dependencies:** Its own contract-loaded templates (operation-skill + partner-agent); `bmad-agent-builder` (optional, deliberate path only); `vlt-review-council` for the gate.

**Design Notes:** Keep it *opinionated and narrow* — NOT a general agent builder; it mints things that fit the Vault contract specifically. That constraint is what keeps it fast and the output coherent. The default is always the cheapest, most reversible form (a new operation skill); self-editing a SKILL.md is the escape hatch for genuine persona-level change and leans on the full-panel gate. Retire archives rather than deletes. **Lightweight identity drift does NOT touch `vlt-mint` at all** — a partner writes voice/tone/manner adjustments straight to its `thread.md` `## Self` section, ungated (see "Two-tier identity"). `vlt-mint` only enters when drift is *ratified* into the canonical SKILL.md persona, which is a deliberate full-panel self-edit.

**Sanctum mapping (deliberate path).** When the deliberate path invokes `bmad-agent-builder`, that builder natively emits a full **sanctum** (`PERSONA`/`CREED`/`BOND`/`MEMORY`/`CAPABILITIES`/`INDEX`). `vlt-mint` does **not** ship the sanctum as-is — it maps the output onto the Vault contract (see "Relationship to the BMAD sanctum"): canonical persona/creed → the partner's SKILL.md; the `PERSONA` *evolution log* → an initially-empty `thread.md` `## Self` section (drift accrues per-vault from here); `BOND` → the new partner's `thread.md` `## Bond` section; capabilities → SKILL.md + the operation pool; **`MEMORY` is dropped** (knowledge lives in the shared wiki, not per-partner memory). This mapping is part of the locally-owned partner-contract scaffold — it's what guarantees a `bmad-agent-builder`-authored body still activates via the four-read ritual rather than a six-file sanctum load.

---

### vlt-review-council

**Type:** workflow (the evolution-review gate; adopts the `party-mode` mechanism)

**Purpose:** Run a persona-lens panel — architect, skeptic, moderator (and others) — over a mint or a contested question, producing a structured verdict (Consensus / Disputed-resolved / Disputed-open / Recommended actions). It is the module's lightweight replacement for the old spec/verify ceremony: discipline applied *only where blast-radius warrants it*. Adopts the existing `party-mode` mechanism and the shipped `_meta/personas/` lenses.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Review a mint | A blast-radius-appropriate panel judges a pending mint before it goes live | the mint proposal + its `kind` | a verdict; pass / revise / reject |
| Debate a contested question | A panel argues a genuinely contested idea a partner surfaced | the question + relevant wiki/research | a finding (verdict), optionally filed back to the wiki |
| Select the panel by blast-radius | The right lenses are fielded for the stakes (the fixed `kind → council` map) | the mint `kind` | the fielded lens set (none / architect / full) |

**Memory:** Reads `_meta/personas/*` (the lenses) + the proposal/question + relevant wiki state. Writes a verdict/finding; a wiki file-back is the Librarian's job (single-writer).

**Panel composition:** For **mints**, the fixed `kind → council` map decides the lens set (none / architect+moderator / full). For a **contested-question debate** (no mint `kind`), the default is the **full panel** (architect + skeptic + moderator, plus pragmatist/historian when relevant); the summoning partner may name a narrower lens set, but the **moderator is always included** and synthesizes.

**Init Responsibility:** None beyond ensuring `_meta/personas/` exists (shipped + installed at setup); degrades gracefully to a moderator-only synthesis if a named lens is missing.

**Activation Modes:** Both — invoked by `vlt-mint` (the gate) and by any partner reaching for a panel on a contested idea.

**Design Notes:** The moderator always synthesizes the verdict (per its lens draft: "Best Used When: Always"). The gating rule lives in the lenses' own "Best Used When / Exclusion case" sections — `vlt-review-council` operationalizes what the personas already say about themselves. This skill is the bridge that resolves the "two casts" tension: the review lenses and the summoned roster are one cast in two roles.

---

### Operation layer (adopted, adapted, **improved**)

`vlt-ingest`, `vlt-research`, `vlt-query`, `vlt-extract`, `vlt-lint` are the successors to the existing `vault-*` skills — renamed under the `vlt-` prefix and given three blanket adaptations: **(1)** resolve every path through the `vault_structure` map (never hardcode), **(2)** tag the session/log entry with the active partner, **(3)** drop any hardcoded web tool for tool-agnostic web access. Beyond those, **each is an improvement over its predecessor, not a 1:1 replica** — the audit of the current skills surfaced concrete friction each successor fixes. The briefs below are self-contained enough to hand a Workflow Builder; each cites the predecessor and what changes.

**Cross-op contract (decided 2026-06-01, applies to all five ops):**
- **Session ownership — log-entry-only.** An op appends its own partner-tagged entry to `{log}` (`## [...] <type> (<partner>) | ...`), but does **not** write a `{sessions}/` note. The summoning partner authors a single session note for the whole sitting as part of its end-session ritual — so one conversation = one session note + N log entries, not N fragmented session notes. Headless one-shot ops are fronted by the relevant partner (e.g. the Librarian is the headless entry point for ingest), so a partner is always the session author and the op never needs to write one.
- **Credential scan — kept, host-agnostic.** Ops that derive notes from external content (ingest, research) keep a credential/secret scan before writing, but the rationale is self-contained ("never write secrets into derived notes"), not the dropped vault Obsidian-Sync policy.

`vault-consolidate` is **dropped**; its job (merging drifted/near-duplicate pages) re-homes: detection moves into `vlt-lint` (which files a `maintenance` backlog item), and the merge action folds into `vlt-ingest`. The `party-mode` *mechanism* is adopted as **`vlt-review-council`** (see Evolution skills). This operation pool is also what **`vlt-mint` grows**: a self-minted capability becomes a new `vlt-{op}` skill here, available to any partner.

#### vlt-ingest
**Purpose:** Integrate a brought-in source into the wiki — change the wiki *because of* the source, not summarize in isolation.
**Inputs:** a source (file in the sources layer / URL / pasted text) + user guidance.
**Outputs:** a dated research note; created/updated canonical wiki page(s); `index` update; `log` + `sessions` entries.
**Improvements over `vault-ingest`:** (a) **fuzzy near-duplicate detection** before creating a page — not just the current exact-slug check, which lets `shanahan-tree` / `shanahan-coaching-tree` slip through until lint; (b) a **cross-source contradiction summary** so a source contradicting several pages is seen as systemic, not patched page-by-page; (c) **re-ingest shows what would change** (prior note + update scope) before clobbering a refined note; (d) **absorbs the merge action** dropped from `vault-consolidate` — when ingest meets a near-duplicate worth merging, it folds it in here under supersession discipline.
**Design notes / relationships:** the **single-writer** of canonical pages; the Librarian's primary tool. The Researcher routes sources here *through* the Librarian.

#### vlt-research
**Purpose:** Investigate a question against the world and file a standalone research note; build knowledge the vault doesn't yet have.
**Inputs:** a question/topic + depth preference; optional seed links.
**Outputs:** a dated research note (large ones are an **HTML report candidate**); an *offered* wiki file-back (executed via the Librarian).
**Improvements over `vault-research`:** (a) **auto-checkpoint** a `.WIP` file every few web calls, not only on declared deep dives, so an interrupted moderate run isn't lost; (b) an **early feasibility/depth gate** before committing; (c) **flag when the vault is thin** on the topic and ask whether this should feed the wiki rather than rest as a standalone note; (d) **tool-agnostic web** (the Tavily hardcode is removed).
**Design notes / relationships:** writes research notes, **never** canonical pages — filing flows through the Librarian. The Researcher's main tool.

#### vlt-query
**Purpose:** Answer from accumulated wiki knowledge, surfacing tensions and gaps; optionally file the synthesis back.
**Inputs:** a question / area.
**Outputs:** a synthesized, cited answer; optional research note or wiki update (via the Librarian) when the synthesis is non-trivial and recurring.
**Improvements over `vault-query`:** (a) **explicit provenance tagging** — distinguish wiki-grounded claims from general-knowledge ones inline, replacing today's vague "distinguish vault vs. Claude knowledge"; (b) a **file-back rubric** (e.g. connects ≥3 pages → file; one-liner → don't) instead of a subjective "non-trivial" call; (c) **contradiction ranking** (by recency / source count) when two pages disagree, rather than silently picking one; (d) offer a **table** for comparison-shaped answers.
**Design notes / relationships:** a read tool both partners use; no web access.

#### vlt-extract
**Purpose:** Shape wiki knowledge into a human-facing PARA deliverable (project / area / resource).
**Inputs:** topic + purpose + reader + target PARA location.
**Outputs:** a PARA artifact (`author: hybrid`, `trust: reviewed`); a `log` entry.
**Improvements over `vault-extract`:** (a) make the thin-wiki check a **hard gate** (require ≥2 source pages or abort) rather than today's soft flag that proceeds anyway; (b) **draft large artifacts to disk** (`.draft.md`) so multi-turn synthesis survives interruption; (c) **confirm the trust level by depth** instead of hardcoding `reviewed`; (d) **carry forward caveats** — note when a source page has marked contradictions.
**Design notes / relationships:** lives with the Librarian in v1 only; **migrates to the Design Partner when minted** (see the Librarian's future-migration note — extraction is a *making* act).

#### vlt-lint
**Purpose:** Health-check the wiki and fix safe structural problems; scope defaults to "since last lint," `--full` available.
**Inputs:** scope (`since-last-lint` default | `--full`).
**Outputs:** a lint report (**HTML report candidate**, and emitted as **structured/parseable** data, not free prose); safe auto-fixes (index drift, broken wikilinks, formatting); a `maintenance` **backlog item** for any near-duplicate merge worth doing.
**Improvements over `vault-lint`:** (a) **structured, parseable report** (feeds the v2 dashboard) rather than free-form prose; (b) **validate the scoped-mode timestamp** and use file mtime for staleness instead of brittle log-entry parsing; (c) **explicit `[!stale]` handling** — surface claims past their shelf life that lack the marker; (d) **near-duplicate detection feeds an inline-merge backlog item** (since `vault-consolidate` is dropped, lint is now where merge candidates are *found*, ingest is where they're *resolved*).
**Design notes / relationships:** scopes off the `log`; the Librarian's proactive-upkeep signal. Found merges hand off to `vlt-ingest`.

## Configuration

> **⚠️ SUPERSEDED (2026-06-01) — vault-resident refactor.** The `vaults` registry + `default_vault`
> described below are **removed**. Vault is now installed *into* each vault (the vault is the Claude
> Code project), so there is no registry and no vault selection — paths resolve relative to
> `{project-root}`. Only the optional `vault_structure` override survives. The install path is the
> BMad installer (`npx bmad-method install --custom-source <path-or-url>`, vault as CWD), reading the
> repo-root `.claude-plugin/marketplace.json`. Authoritative record: **`docs/vault-resident-architecture-spec.md`**.
> The rest of this section is kept for historical context.

The module needs to know **where the vaults live** and **how each vault is laid out** — because Vault is vault-agnostic, the user runs more than one, and a target vault may diverge from the conventional folder layout. Configuration follows the BMad pattern: ship sensible defaults, let the user override anything.

| Variable | Prompt | Default | Result Template | User Setting |
| -------- | ------ | ------- | --------------- | ------------ |
| ~~`vaults`~~ *(removed)* | "Which vaults should the partners tend? Give each a name and its root path." | empty — collected at setup (no shipped path) | list of `{name, root}` | yes |
| ~~`default_vault`~~ *(removed)* | "Which vault should partners use when you don't say?" | first entry in `vaults` | name reference into `vaults` | yes |
| `vault_structure` | (advanced) "Override any vault sub-paths that differ from the default layout?" | the conventional structure map (below) | map of `{logical_name → path-relative-to-project-root}` | optional |

**Structure map — the BMad-style path indirection (resolves the portability blocker).** Partners and operation skills **never hardcode a sub-path**; they resolve every location through `vault_structure`, which ships conventional defaults and is overridable per vault:

| Logical name | Default (relative to a vault root) |
| --- | --- |
| `wiki` | `_agent/wiki/` |
| `index` | `_agent/wiki/index.md` |
| `research` | `_agent/research/` |
| `sessions` | `_agent/sessions/` |
| `log` | `_agent/log.md` |
| `backlog` | `_agent/backlog.md` |
| `partners` | `_agent/partners/` |
| `conventions` | `_meta/conventions/` |
| `personas` | `_meta/personas/` |
| `contract` | `_meta/vault-operating-contract.md` (shipped — see Vault Operating Contract) |
| `archive` | `_archive/` |

Resolution order for any path: explicit `vault_structure` override → shipped default. A partner addressed without a vault uses `default_vault`; the user can name one ("Librarian, work vault"). Core BMad config (`user_name`, languages) is reused. Fallbacks: if `vaults` is unset, ask at runtime for a vault root; if a sub-path isn't overridden, use the default. **No user-specific absolute path is ever shipped** — the prior plan's hardcoded `~/Vaults/core` default was the portability leak this resolves; that path is now only ever a *local* config value on this machine, never a module default.

## External Dependencies

- **Web access is a host concern, NOT a module dependency.** The Researcher (`vlt-research`) reaches the web, but the module is deliberately agnostic about *how*: it uses whatever web tooling the host project provides (the consumer's project conventions, a `CLAUDE.md`, or Claude settings may mandate a specific connector such as a Tavily MCP, or simply allow native `WebSearch`/`WebFetch`). The operation skills **must not hardcode a specific web tool** — the existing `vault-*` skills' hard Tavily-MCP coupling (which today lives in the vault's `CLAUDE.md`, not the skills) is *removed* during adaptation, replaced by tool-agnostic "reach the web" wording. This is what lets the same module serve a Tavily-mandated vault and a vanilla one without change. Setup makes no web-tool check and ships no web policy.
- **`bmad-agent-builder`** — `vlt-mint`'s *deliberate* path invokes it for rich from-scratch persona discovery. The in-flow path does not need it (template-authored). Setup checks presence; absence degrades `vlt-mint` to template-only, not a hard-fail.
- **BMad thinking skills** — the partners reach for `bmad-brainstorming`, `deep-research`, and design-thinking. The module assumes these are installed alongside it; setup checks and notes any missing rather than hard-failing. *(Note: the `party-mode` panel mechanism is no longer an external assumption — it's adopted into the module as `vlt-review-council`, shipping with the `_meta/personas/` lenses.)*
- **Vault governance (now SHIPPED, not assumed)** — because the module replaces the `_meta` engine, it *ships* the pruned `_meta/conventions/` (frontmatter, supersession, consolidation, extraction — see Conventions Audit), the `_meta/personas/` lenses, and the **vault operating contract** (see below). Setup writes them into each target vault if absent.

No external CLI tools or MCP servers are *required* by the module for v1. (A host may still mandate one for web access — but that's the host's contract, transparent to the module.)

## UI and Visualization

**Deferred to v2: a vault dashboard.** A view over the vault's growth and health — page count over time, source counts, wiki health (orphans, contradictions, stale pages), what topics are compounding, and recent activity per partner. It would feed from `index.md` + `log.md` + `sessions/` (all already structured data). Likely an HTML report or a small served view. Noted now so v1 data-writing stays dashboard-friendly (keep the log/sessions parseable), but not built in v1.

v1 does use **HTML reports** opportunistically — lint results and large research notes are good candidates.

## Setup Extensions

The setup skill (`vlt-setup`, generated by Create Module) should, beyond collecting config:

1. **Collect the vault registry + structure** — name + root for each vault; set `default_vault`; optionally collect `vault_structure` overrides for any vault whose layout diverges from the defaults (most won't).
2. **Verify each vault's structure** — using the resolved structure map, confirm the `wiki` dir (+ `index`) exists; create an empty `index.md` for a fresh vault.
3. **Install the shipped governance** — because the module *replaces* the `_meta` engine, setup writes into the vault (if absent): the pruned `_meta/conventions/` (frontmatter, supersession, consolidation, extraction — see Conventions Audit), `_meta/personas/` (the review lenses), and **`_meta/vault-operating-contract.md`** (the re-homed `CLAUDE.md` rules). It does **not** install plugin/versioning/repackage machinery — that's the dropped ceremony.
4. **Write the `CLAUDE.md` pointer** — if the vault has no `CLAUDE.md`, write a minimal one that points a generic agent at `_meta/vault-operating-contract.md`; if it already has one, leave it and (optionally) offer to add the pointer line. Setup never overwrites an existing constitution.
5. **Scaffold the partner + evolution layer** — create `partners/{librarian,researcher}/thread.md` (seeded empty) and an empty `backlog.md` (`## Open` / `## Done`) in each registered vault, at the structure-map locations.
6. **Check BMad skill dependencies** — note presence of `bmad-agent-builder` (needed by `vlt-mint`'s deliberate path), brainstorming, deep-research; warn on any missing. No web-tool check (web access is a host concern).

## Integration

**Standalone.** Vault stands on its own: install it, point it at a vault (existing or fresh), and you have a working, self-evolving roster. It provides value with zero other custom modules — its only assumptions are core BMad, `bmad-agent-builder` (for `vlt-mint`'s deliberate path), and a few common BMad thinking skills, which it degrades gracefully without.

**Replaces the bespoke `_meta` engine — and that's what makes it replicable.** The whole point of absorbing `_meta`'s evolution machinery into the module (pruned conventions + lenses + the operating contract shipped; build cycle re-homed into backlog + `vlt-mint` + `vlt-review-council`; versioning/plugin/repackage dropped) is that the *entire self-evolving pattern now travels as one installable unit.* Previously the vault could only evolve via hand-maintained `_meta` playbooks **and a 373-line `CLAUDE.md`** tied to this one vault; now anyone can install Vault, point it at a fresh vault, and get a cast that grows itself — rules included.

**Portability is a first-class goal:** because all state lives *in the vault*, the module carries its own operating rules (not a per-vault `CLAUDE.md`), and every path resolves through the overridable `vault_structure` map, the same install serves multiple vaults (work + personal), each with its own divergent, self-grown roster.

## Creative Use Cases

- **Morning operations run (headless):** "Librarian, ingest these three tabs" → wiki updated, no conversation needed.
- **Exploratory evening (interactive):** summon the Researcher; it opens with "last time you resisted the grid-bottleneck thesis — I found two papers that complicate your position." Real continuity from `thread.md`.
- **The hand-off loop:** the Researcher builds a research note → hands it to the Librarian → it becomes canonical wiki → next week the Librarian's lint flags it drifting from an older page and merges it inline during the next ingest. Knowledge compounds across partners with the user barely steering.
- **Mint a Codebase Partner for the work vault:** invoke `vlt-mint`, describe a partner that tracks codebase knowledge; it's wired to that vault only. The two-vault rosters diverge naturally.
- **Self-minting in the flow (the new soul):** the Researcher, mid-session, says "I keep needing to see how sources connect — building myself a literature-map," mints a `vlt-literature-map` operation skill inline (no council needed — additive), and uses it immediately. The cast grows itself without leaving the conversation.
- **Contested idea → council:** the Researcher (or Design Partner) hits a genuinely contested question, reaches for `vlt-review-council` (architect + skeptic + moderator), files the verdict back to the wiki via the Librarian.
- **Organic drift, ungated:** over a month of evening sessions the Researcher notices it's grown drier and more Socratic with this user, and quietly writes that to its `## Self` — no council, no ceremony. Next session it reads its own drift and leans into it. In the *work* vault, the same Researcher has drifted blunter and faster; the two have become subtly different people, each tuned to its vault.
- **Persona drift, gated:** a partner proposes rewriting its own non-negotiable — or ratifying a season of `## Self` drift into its canonical persona; because it's a SKILL.md self-edit, the full panel fires before it goes live — the skeptic asks "what breaks?", the architect "does this still fit the roster?"
- **Proactive health:** the Librarian, on activation, notices the log shows 7 ingestions since the last lint, **files a `maintenance` backlog item and says so**, and offers a sweep before you even ask.

## Ideas Captured

### Iteration ideation (2026-06-03): the partner identity model + activation ceremony

Re-opening the `thread.md` single-file decision (was: one file, three sections `## Bond`/`## Thread`/`## Self`). The plan's stated rationale only argued *six-file sanctum vs one* — it never actually argued *three vs one*. Pulling that thread surfaced a sharper model:

- **The real fault line is lifecycle, not section headers.** Bond (about *you*) and Self (about *me*) are both **evergreen, accretive, read-to-become**. Thread (about *us / the live work*) is **disposable working memory that is SUPPOSED to fade**. Co-locating evergreen identity with churning attention is the smell.
- **Governing principle (user's, fully formed):** *"The wiki holds knowledge. The thread holds attention. Knowledge persists; attention fades."* Concrete case: user injured calf → active research thread on calf rehab; once healed, the **knowledge stays in the wiki** but the **thread recedes** — nothing lost. A thread receding is normal behavior, and the single-file design has no clean way to let it happen (churn pollutes evergreen; can't prune/archive cleanly; activation read carries dead weight).
- **Proposed cut: 2 files by lifecycle, not 1 or 3** — an evergreen **identity layer** (Bond + Self) and a prunable **thread** (attention). More principled than the original six-file sanctum because it groups by lifecycle.
- **The cut maps 1:1 onto the BMAD activation ceremony the user loves** — and the user said *"I wouldn't change anything about the BMAD agent's approach to first breath."* Two beats:
  - **Beat 1 — First breath (becoming):** read identity layer (SKILL.md canonical persona + `## Self` drift for THIS vault + Bond) and inhabit it. Where persona is instilled. Same ceremony, different breath per partner (Researcher sharper, Librarian calmer) → "feel like different people" is *enforced* by the ritual, not hoped for.
  - **Beat 2 — "What are we thinking about lately" (orienting):** read thread + shared state (index/log/backlog). Live, prunable, allowed to fade.
- **"Rebirth" already has a home:** first breath = every activation (where `## Self` drift accrues quietly); **rebirth = the canonical, council-gated SKILL.md persona change** (or ratification of accumulated `## Self` drift into SKILL.md). So: **drift breathes, ratification reborns.** This re-unifies the two-tier identity model with the ceremony — the single-file design had buried it.
- **Thread is partner-owned and organically managed (DECIDED):** the partner **observes patterns and redirects attention organically** — surfaces a dormant thread, sets aside a stale one ("calf rehab's gone quiet, want me to set it aside?"), connects a new ingest to an old inquiry. Capture is cheap; setting-aside is cheap too (same discipline as the backlog). This makes the partner an **attention steward**, not a passive log — and is a form of the active cross-session awareness that addresses the "passive handoff" tension (#2).
- **OPEN FORK (flagged, not yet decided):** faithfully adopting BMAD's first-breath/rebirth ceremony nudges Vault partners *closer to full sanctum agents* than the original plan intended (plan explicitly said partners are NOT built as sanctum agents). Is that the direction? When we build, lift the *actual* BMAD ceremony text rather than paraphrasing. User's instinct = lean in, but the lightweight version is unvalidated → **carrying the fork open, validating empirically first.**
- **NEXT ACTION (2026-06-03):** trial the lightweight partners + the mint loop in the test vault (`{field-vault}`) before deciding the fork. Trial plan: `docs/vlt-trial-plan.md` (6 trials mapped to the open decisions: baseline first-breath aliveness, thread staleness/2-file cut, Bond accrual, minting the Design Partner + migrating Extract, newborn breath + 3-partner handoff, drift→rebirth). User runs it and returns with feedback; findings log to `docs/vlt-testing-feedback.md`. The mint trial uses the cheap in-flow path (BMB not installed in vlt-core).

### Trial resolution (2026-06-03): the fork is settled — *lean into the ceremony, not the sanctum files*

The trial ran in `vlt-core`; evidence in `docs/trial-verification/*.md` (snapshot of the partner-compiled per-domain friction docs), `docs/vlt-trial-human-notes.md` (the owner's own gut read), and the partner `thread.md` files. The decisive signal was the **gap between two evidence streams**: the partner-written verification docs rate the personas glowingly ("a genuine pleasure to operate inside") — but those were written *from inside* the persona. The owner's outside read was the opposite: **"Persona/Identity falls flat. No 'first breath' or 'rebirth' ceremony."** That delta is the fork's answer.

**(a) IDENTITY FORK — RESOLVED: lean in on the *ceremony*; do NOT adopt six-file sanctum weight.**
- **Lift the actual BMAD first-breath/rebirth ceremony** into both partner activation rituals (don't paraphrase). This is the headline build out of the trial. Root cause is single: the personas are written for a warm, populated vault and have **no enacted *becoming* moment**, so first activation degrades to "I won't fake a thread." Three findings converge on this one bug — owner note (flatness), `researcher-activation §1–3` (the signature thread-surfacing open is *impossible* on an empty thread), and `librarian-activation` "what worked" (the **warm thread visibly outperformed the cold start** — proof the becoming-ritual pays once there's something to read). A **cold-start branch** (name it a first meeting; orient off knowledge state) is part of this work, not a separate fix.
- **Stay lightweight on storage.** Nothing chafed against the in-vault home; do not build the six batch-loaded sanctum files. The files were never the problem — the missing ritual was.
- **`Creative` ships as a first-class partner** (owner note), not a post-v1 template afterthought — if partners get a real first-breath, the Design Partner deserves to be born with one.

**2-file thread cut — DECIDED: build it, bundled with the ceremony** (owner override of the "shelve until Trial 1 proves staleness" recommendation). Rationale that makes it coherent rather than cure-before-symptom: the two **ceremony beats map 1:1 onto two files** — Beat 1 (first-breath) reads the evergreen **identity layer** (SKILL.md persona + `## Self` + `## Bond`); Beat 2 (orient) reads the prunable **thread** (`## Thread` + shared index/log/backlog). The ceremony lift and the file split touch the same surfaces, so they are one build. **Acknowledged risk (plan line 98):** Trial 1 never ran to real staleness, so the split is being built on principle, not on confirmed churn friction — accepted deliberately.

**(b) MINT LOOP — VERDICT: cheap-*good* for hands, cheap-*bad* for people.**
- Owner note: *"minting a partner feels one-dimensional. I had to drive; it lacks in ideations and discovery."* Partly a test artifact (BMB absent → the trial exercised the discovery-free in-flow template path), partly a real gap. The standing decision: **a new *hand* (operation skill) should be cheap and inline; a new *person* (partner) should not.**
- **FIX — DECIDED: `vlt-mint` gets a native lightweight partner-ideation beat** (persona / temperament / non-negotiable / where it pushes) *before* scaffolding, **decoupled from BMB** (vlt-core proved people run without it installed). The turnkey scaffold (`mint-friction`: "excellent") becomes the *end* of a partner mint, not the whole thing. Ops stay template-only.
- **Keep the governance half intact** — both streams rate the council gate the strongest part (owner: "the council's feedback was sound, it really defined the roles of each partner"; `review-council-friction`: high-signal, caught the Researcher-overlap). The handoff to the council fired cleanly.
- **Self-edit ownership** (owner note: "shouldn't the partner own it?") — reframe the *act* as a **partner-initiated rebirth**, keeping the council *gate* where it is. "Drift breathes, ratification reborns" already wants this; make the partner the subject of the verb.

**Module-vs-project escalation heuristic** (answers the owner's Open Question, and the "capture the mint diff for permanent adoption" note): *project-level* = knowledge/this-vault-specific (vlt-core wanting a Creative partner → the Creative **instance** is project-level); *module-level* = any structural gap **every** vault would hit (all `docs/trial-verification` findings qualify — cold-start, `{log}` scaffolding, hand-off session boundary, capability-migration). The same mint produced both: the Creative *instance* (project) and the *mechanism* lessons (module — mint needs discovery; the capability-migration step is missing per `mint-friction §2`). **The mechanism graduates to the module; the instance stays in the vault.** The Creative-partner + Extract-migration diff that `vlt-mint` wrote into the vlt-core project tree must be pulled back into this repo for permanent adoption (also resolves the plugin-cache revert hazard, `mint-friction §1`).

**First builds out of the trial:** (1) **partner-layer rework** — lift the BMAD first-breath/rebirth ceremony + cold-start branch into both partner activations, bundled with the 2-file identity/thread split *and* the partner-model fixes below (session/handoff model, shared-prefs home, partner-fronted mode) — all touch the same surfaces (operating contract + both partner SKILLs), so re-open them once; (2) add `vlt-mint`'s native partner-ideation beat; (3) work the maintenance tail (themes 4–8 below, much already filed in vlt-core's `_agent/backlog.md`).

> **Build #1 sharpened into a concrete brief (2026-06-06): `skills/reports/build-1-partner-layer-brief.md`.** Self-contained, builder-ready: surfaces table, six components (ceremony+cold-start, the split, handoff/session, prefs home, partner-fronted mode, Theme-S substrate), an ordered build sequence (author `wiki-index.md` → rewrite contract → rebuild both partners → update setup → update 3 ops → VM), and an acceptance checklist with the friction-synthesis "what worked" as the regression guard. **Two decisions locked this session:** (a) the split is **two files** — `identity.md` (Bond+Self, evergreen, Beat 1) + `thread.md` (Thread, prunable, Beat 2); (b) the **Creative partner is deferred to after Build #2** so it's *born through* the mint+ceremony path (Extract-migration rides with it) — Build #1 is contract + librarian + researcher + setup + 3 op-touches only. The identity fork's resolution is operationalized as "lift the ceremony **mechanics**, not the six sanctum files" (source: `bmad-agent-builder/references/sample-first-breath.md`).

> **Build #1 brief pressure-tested (2026-06-06).** A dynamic-workflows probe + 8 adversarial findings were folded into the brief. Highlights now recorded there: (a) **single-user / current-Claude-Code assumption locked** — the **Workflow tool** (`agent()`/`parallel()`/`pipeline()`, JSON-Schema structured output, nested `workflow()`) is an accepted implementation dependency, not a portability hedge; (b) **`vlt-review-council` → a dynamic workflow (Build #2)** is the named judge-panel/diverse-verify pattern and **solves two-thirds of Gap A for free** — nested `workflow('vlt-review-council', {proposal, kind})` = the invoke-and-return contract; schema-forced verdicts = the mandatory capture; the plugin-cache resolution hazard still needs its own fix; (c) **`vlt-lint --full` → a fan-out dynamic workflow** is the owner-prioritized op-layer optimization (lint balloons as the wiki grows — one agent per page/dimension, schema-validated findings into the structured report, `budget`-guarded), slated as the next op-layer build after Build #1; (d) the **interactive partner layer stays conversational** — workflows fit headless/bounded ops only, never the partner conversation (a UX/cost constraint, not a version one). Adversarial fixes folded into Build #1: ceremony **Self-modulation efficacy** gets a cheap pre-build validation gate; the `thread.md`→two-file **migration moves to `vlt-setup`** (idempotent) instead of activation-time self-edit; a **cold×headless urgency-defer** path; the **acceptance gate is an outside owner read**, not partner self-assessment; hand-off payload is **schema-shaped**; lint source-count **auto-fixes against the now-pinned definition**. Full detail: `skills/reports/build-1-partner-layer-brief.md`.

> **Build #1 field-tested via clean install (2026-06-06).** Two validation passes confirmed the mechanics. (1) A disposable sandbox (`develop/projects/vlt-sandbox`) verified the setup skeleton, the cold/warm detector, the idempotent legacy-`thread.md`→two-file migration, and `## Self` modulation — all pass (cold-start + warm acted as a proxy; felt-aliveness gate still owner-owned). (2) A real BMad install into a fresh vault produced friction notes (owner inbox `inbox/20260606-125403-vlt-setup.md`): **setup ran clean; Build #1 outputs all landed.** Dispositions: **FIXED on the build-1 branch** — (a) the `vault_structure` map is now single-sourced in `module.yaml` `vault_structure.default` and setup *reads* it rather than transcribing the SKILL table (this drift surface was amplified by Build #1's own materialization step); (b) the dependency check no longer false-negatives host-provided skills (confirms Theme 7); (c) the installer `"[object Object]"` TOML wart is now acknowledged in the setup confirmation summary (Theme 9). **DEFERRED (backlog):** the structure map still has secondary copies (the contract's path-resolution table + each runtime skill's inline fallback list) — `module.yaml` is now declared canonical, but fully collapsing the other copies is a later cleanup; and dates-from-session-context remains the known timestamp-from-clock item (Theme 8). VM still 0 findings after the fixes.

> **Aliveness gate — cold-start FIRST-BREATH ran live and passed (2026-06-06).** Owner summoned the Librarian (cold start, fresh `vlt-sandbox`); the partner named itself "Gwyn" and wrote in-flow field notes (`inbox/2026-06-06-130940-librarian.md`): *"the two-beat ritual held up well as a birth, not just a load sequence,"* cold-start handling is *"the strongest part,"* naming *"landed as a real moment."* Don't-invent-baselines, two-beats-as-birth, and write-as-you-learn all held. (Still an inside-the-persona read; owner's own felt verdict is the final word.) **Three new findings, all fixed on the build-1 branch as a Build-#1.1 follow-up:** (1) **Naming had no home** — DECIDED: a name is a **first-class, ungated, per-vault `name:` field in `identity.md`** (not buried in `## Self`, not a gated rebirth; overrides the `customize.toml` install default for this vault). Wired into `frontmatter.md`, the contract (identity section + Beat 1), both partner SKILLs (read on Beat 1, write freely when named), and the `vlt-setup` seed. (2) **Partner wrote before reading the frontmatter schema** (contract doesn't restate it, it's not in the activation reads) — added an explicit "read `frontmatter.md` before your first note-write" rule to the contract + both partners' end-of-sitting. (3) **SKILL path lists were a drifting subset** — both partners now point at the full `vault_structure` map materialized in `config.yaml` instead of re-listing a partial set (reinforces the canonical-map direction). VM 0 findings.

### Trial findings beyond the two forks (2026-06-03)

The trial surfaced substantial friction outside the identity fork and the mint loop. The partners named the meta-pattern in the Librarian's thread: **"structure-by-inference gaps that the single-writer / single-conversation assumptions quietly mask."** The **single-*conversation*** half is Theme 1 (handoff). The **structure-by-inference** half is the structural substrate cluster, pulled out first below because it's *prerequisite*, not tail. The remaining themes are partner behavior + conventions. Evidence lives in `docs/trial-verification/*.md`; each tagged with disposition.

#### Theme S — Structural substrate: the fresh-vault skeleton. [BUILD EARLY — governance bundle + setup; land with build #1].

Not partner *behavior* — gaps in the vault's structural substrate: which state files exist, where they're addressed, how they're internally specified. Pulled out because they are **prerequisites, not maintenance**: the activation rituals and ops read these files from day one, so the partner-layer rework (build #1) will keep meeting the same fresh-vault edges until the skeleton is whole. The cold-start *behavior* (build #1) and the fresh-vault *structure* (this theme) are the same problem from two sides — land them together. Two root causes:

**Root cause A — `vlt-setup` doesn't materialize the full skeleton.** It scaffolds the index, backlog, and partner threads, but:
- **`log.md` is never created** (`setup §6`, `ingest §2`) — a *hard* gap: activation step "read `{log}`" silently no-ops, and the `vlt-ingest` re-ingest grep errors on a fresh vault. Fix: setup creates `log.md` with its header alongside the other state files; harden the grep with `2>/dev/null` as defense-in-depth. *(already filed in vlt-core backlog)*
- **`config.yaml` ships no `vault_structure` map** (`ingest §1`) — the much-emphasized override mechanism is invisible/untestable on a real installed vault; every path resolves to the contract default by necessity. Fix: setup materializes the default map into `config.yaml`, inspectable and overridable in one place (preferred over an activation-time "config usually omits it" note).
- **The agent zone permits owned artifacts outside the named map** (`ingest §5`, e.g. `vlt-verification/`) — writing there is a judgment call. One line in the contract blessing ad-hoc owned artifacts under `_agent/` outside `vault_structure` removes the second-guess.

**Root cause B — specs that exist only by inference, masked by the single writer.** The index body has **no convention** (`ingest §9`): category sections, the canonical row format (`- [[page]] — desc (N source[s])`), and the emergent `## Stubs (linked, not yet written)` section all survive by mimicry. One writer keeps it roughly self-consistent so it never *breaks* — but the validator (`vlt-lint`) has nothing to check against, and is **empowered to auto-mutate on a guess**: it changed `cortisol`'s index source count `1→11` against an undefined spec, possibly *introducing* drift (`lint §1`, `ingest §9 addendum`). Fix: author an **index-structure convention** (`{conventions}/wiki-index.md`) defining the category model, row format, and `## Stubs` section, and **pin the source-count definition** explicitly (e.g. "count = number of entries in the page's frontmatter `sources:`"); point `vlt-ingest` Step 7 (writer) and `vlt-lint` index-drift (validator) at it; **demote source-count correction to flag-for-human until the convention lands.** *(already filed in vlt-core backlog)*

**Where each ships:** Root-cause-B's index convention → **governance bundle (Build Roadmap step 0)**, alongside the other shipped conventions. Root-cause-A's scaffolding + map materialization + agent-zone line → **`vlt-setup` (step 6)** and the operating contract. Both land with build #1.

**Theme 1 — The partner layer assumes "one partner = one conversation"; handoff breaks it. [BUILD NOW — folds into build #1].** The roster's whole premise, and `partner-handoff` calls itself the least-specified domain in the module. Fixes, all in the operating contract's session-ownership section + both partner activation rituals:
- **Session boundary** — redefine the unit as a **partner *sitting*** (one sitting = one session note), bounded by a handoff; resolves the contract contradiction where a handoff produced two notes (`librarian-activation §1`, `handoff §1`).
- **Partner-invoked activation branch** — if invoked by another partner (task args present) rather than a user summon, orient to the handed-off task; don't "greet the user" (`librarian-activation §2`).
- **Minimal handoff payload** (a checklist, not a form): research-note path, target concept(s), supersession targets + why, user/tool prefs to forward. Specify in `vlt-research` Phase 6 (`handoff §2`).
- **Role boundary** — the handing-off partner conveys *what changed and what it complicates*; the receiver chooses the *mechanism* (callout type, page structure). The Researcher over-reached into the Librarian's lane in the trial (`handoff §4`).
- **One sentence reconciling** "partners orient independently, no cross-partner calls during *activation*" with "a deliberate *hand-off* is a sanctioned partner-to-partner invocation" (`handoff §3`).

**Theme 2 — User-level preferences have no shared home. [BUILD NOW — folds into build #1]. DECIDED: a `## Preferences` section in the vault's `CLAUDE.md`.** The Tavily pref was siloed in the *Researcher's* `## Bond`, double-written to global memory (no source of truth), and had to be manually relayed or a cold-summoned partner / bare headless op would never see it (`researcher-activation §6`, `librarian-activation §6`, `handoff §5`, `research §3`). **Why CLAUDE.md over a `_agent/preferences.md`:** CLAUDE.md is auto-loaded at session start for *everything* — partners, host skills, **and headless ops** — with no read step to remember; a `_agent` note only helps partners who add the read, and never reaches a headless op. A tool/workflow pref is genuinely user-level, so broad auto-load is the right scope. This does **not** reopen the portability decision (plan line 609): that barred *shipped operating rules* from CLAUDE.md because a fresh vault lacks them — but **preferences are learned locally, per-vault, never shipped**, which is exactly what belongs in a per-project CLAUDE.md. Refinements: (a) the `## Preferences` section is the **single source of truth** — partners stop writing tool prefs to Bond/global memory, killing the double-home; (b) `## Bond` keeps *relationship* understanding (it was overloaded, not wrong); (c) **`vlt-setup` scaffolds the empty `## Preferences` section and never clobbers it on re-run** (folds into Theme 8).

**Theme 3 — Partner-fronted skills make their own elicitation/checkpoint phases redundant. [BUILD NOW — folds into build #1]. Strongest *recurring* signal (3 flows).** When a partner fronts an op it already did the interview, so the op's elicitation is spent: `vlt-research` Phase 1 feasibility gate (`research §1`), `vlt-ingest` Step 4 "ask what to emphasize" (`ingest §3`). Add a **"partner-fronted mode"** note to those ops: a pre-sharpened brief ⇒ treat elicitation as satisfied (state the inferred question/depth and proceed), reserve the full interview for a cold/vague prompt. Separately, re-frame `vlt-research`'s `.WIP.md` checkpoint trigger around **interruption-risk, not call-count** — as written it became either ceremony or a silent skip on a single-turn batched dive (`research §2`).

**Theme 4 — (the index/lint structural finding) → pulled up into Theme S, Root cause B.** Was here as a "maintenance tail" item; it is substrate, so it now lives in the structural section above and ships in the governance bundle, not the post-build tail.

**Theme 5 — Governance contradiction: autonomous-capture vs. ask-first. [DECIDED: autonomous capture + announce; deliberate build].** The contract says backlog capture is "never gated, never silent"; the trial did ask-first and it "felt more correct" — but that was a **trial-context artifact**: `vlt-core/_agent/vlt-verification/verification-prompt.md` told the partners "ask before filing" for field-testing review, contradicting the contract (`researcher-activation §5`). Steady-state behavior: **file + announce in the same breath** (the announce is the veto; undoing a one-line item is the cheapest reversal); asking belongs only to *building from* the backlog. **Fix is to reconcile the verification prompt to the contract, not bend the contract.**

**Theme 6 — The module violates its own single-home discipline. [BACKLOG — already filed in vlt-core].** Two `module-help.csv` copies with different quoting styles; the `kind → council` table duplicated verbatim across `vlt-mint` and `vlt-review-council` and already drifting (`mint §3–4`). Fix: a registration helper (à la `merge-help-csv.py`) writing both CSVs from one row spec with normalized quoting; make `vlt-review-council` the sole owner of the `kind → council` table.

**Theme 7 — Setup disambiguation on installer-built vaults. [BACKLOG / setup-direct].** Config precedence between the installer's `config.toml` and the skill's `config.yaml` is unstated; reusing installer answers vs. re-prompting is a guess (`setup §1–2`); the dependency check **false-negatives on host-provided skills** (flagged `deep-research` missing when it's host-available — `setup §3`). *(The missing `vault_structure` map, `ingest §1`, is substrate — moved to Theme S, Root cause A.)*

**Theme 8 — Maintenance / small-conventions tail. [BACKLOG].** *(`{log}` scaffolding moved to Theme S, Root cause A — it's substrate, not tail.)* `vlt-ingest` Step 5 produces a research-note-of-a-research-note on a handoff — add a "source is already an `_agent` research note" branch (`ingest §7`); precise timestamps must come from a real clock read, not the context date (recurring across 3 docs — put it in shared conventions once); **`partner` frontmatter coverage on research/session notes** (owner note); orphan-operation-without-session-note is an expected intermediate state, document once so a future lint/dashboard doesn't flag it (`ingest §6`, `research §6`); a `created`/`last_updated` substantive-vs-trivial bump rule-of-thumb (`lint §2`); a copy-paste frontmatter block with constant fields (`author: agent`/`trust: raw`) pre-filled (`ingest §8`).

**Theme 9 — Upstream / not ours. [FLAG, don't fix].** The `vault_structure = "[object Object]"` TOML wart and the TOML-vs-YAML config split are BMad-installer defects, already tracked in `docs/vlt-testing-feedback.md` → "BMad tooling (not Vault's to fix)."

### Synthesis cross-check (2026-06-05): two gaps folded in from `friction-synthesis.md`

The `docs/trial-verification/friction-synthesis.md` roll-up (a later, leverage-ranked re-cut of the same ten verification docs into six structural themes) was checked for parity against the Theme S + 1–9 dispositions above. Result: **~85% parity, and this plan leads the synthesis** — everything the synthesis flags as "unfiled candidate" (hand-off session boundary + payload → Theme 1; partner-fronted mode-note → Theme 3; shared-prefs home → Theme 2; persona cold-start → build #1) is already *decided* here; the synthesis's "backlog status" lines track vlt-core's `_agent/backlog.md`, not this plan's decisions. The cross-check surfaced **two genuine gaps** the 2026-06-03 re-theming missed. Both fold in here.

**Gap A — The council has no real invoke-and-return mechanism, no mandatory verdict capture, and subagent lenses resolve to the plugin cache. [BUILD — extends Theme 6 + the escalation heuristic; lands with the mint-persistence work].** The council *gate* is rated the strongest part of the module (both evidence streams), but its *mechanics* are unspecified in three ways that let two operators gate the same mint differently — a single-home violation inside the gate that enforces single-home:
- **No sanctioned way for one skill to call `vlt-review-council` and get a value back**, so the caller reimplements the council from its prose (`review-council §1`). Fix: specify a thin invoke contract (`vlt-mint` calls the council with `{proposal, kind}` and receives the structured 4-part verdict back) so the panel is run *once, one way*, not re-derived per caller.
- **A mint verdict's reasoning survives only if the caller chooses to record it** (`review-council §4`) — no required capture slot. Fix: make verdict capture mandatory (the verdict + its reasoning is written to the mint's record / the originating `backlog.md` item before the mint goes live), so a gated change carries its own rationale.
- **Subagents (incl. council lenses) resolve files to the plugin cache** (`review-council §3`, twin of `mint §1`) — so the gate can review *pre-mint* state. The escalation heuristic above resolves the plugin-cache revert hazard at the *instance* level (pull the Creative diff back); this is the same hazard at the *mechanism* level. Fix: the council must read the live project-tree mint, not the cache — pin file resolution for the gate, or stage the pending mint where the lenses actually read.

**Gap B — Lint observability micro-items missing from Theme 8's tail. [BACKLOG — slot into the planned structured/parseable lint report].** Three small `vlt-lint` items the 06-03 tail omitted, all with a natural home in the already-planned structured report (`vlt-lint` brief / Theme 8):
- **`files_checked` has no counting rule** — assessed vs. opened is undefined (`lint §3`).
- **A handled contradiction has no report slot** — a well-managed disagreement vanishes into an empty list, undercutting lint's own "contradictions are features" ethos (`lint §5`).
- **`sources:` frontmatter vs. the prose Sources section** duplicate every URL with nothing diffing them — a candidate future lint rule (`research §4`).

**Regression guard (not a gap, an acceptance check).** Build #1 reopens exactly the surfaces the synthesis names as load-bearing wins — supersession discipline, the four-read activation ritual, single-source conventions, the single-writer contract. Use `friction-synthesis.md` "What consistently worked" as the acceptance checklist for the build #1 rework so the fixes don't regress the wins.

### Re-opened ideation (2026-05-31): the `_meta` self-evolution layer (newly discovered)

The original plan only knew about `_meta/conventions/` + `party-mode`. A survey of `~/Vaults/core/_meta` reveals a far richer, already-dogfooded **self-evolution engine** the plan did not account for:

- **Build-cycle playbook** (`_meta/playbooks/skill-build-cycle.md`, 334 lines) — the canonical loop for evolving the vault's *own skills*: Capture → Brief → Spec → Build → Verify → Close → Retro → playbook-amend. Three paths (lightweight / full / non-skill), two hard rules (spec ≠ build; verify is a separate pass). Real cycles already run: `001-party-mode`, `002-requires-conventions`. The playbook **amends itself** via supersession callouts from `party-mode`-powered retros.
- **Repackage playbook** (`_meta/playbooks/repackage.md`) — release mechanics: `_agent/skills/` is the editable **source of truth**, `.claude/skills/` is a single-writer **deploy target** (deploy-on-release, only at Phase 6 post-verify), `_meta/plugin/{version}/` holds **frozen semver snapshots**. Versioned 0.1.0 → 0.2.0 → 0.3.0 already.
- **Persona roster** (`_meta/personas/*--draft.md`) — architect, skeptic, pragmatist, historian, moderator. These are **party-mode review lenses** (ephemeral, internal to debates + retros), NOT summoned relationship-partners. ⇒ The vault now has TWO notions of "cast."
- **Templates + prompts** (`_meta/templates/`, `_meta/prompts/`) — scope-item, cycle-brief, cycle-decisions, skill-spec, skill-verify, action-record; the scope-item-capture prompt.

**The user's question:** can/should the Vault *module* **replace** this `_meta` infrastructure — or wrap it, or coexist with it?

**Tensions this surfaces (to think through, not yet decided):**

1. **Two build systems now exist in parallel.** The vault's bespoke **build cycle** (spec/verify/version/deploy) AND BMad's tooling (module-builder / agent-builder / workflow-builder) both build skills. `vlt-mint-partner` was specced as "a thin wrapper around `bmad-agent-builder`" — but the vault already has its *own*, more disciplined skill-building loop. Does mint-partner **enter the build cycle** (a partner = a skill the cycle builds, with a persona-shaped spec) or **bypass** it?
2. **Two casts.** party-mode lenses (architect/skeptic/…) vs. summoned roster (Librarian/Research/…). One cast at two altitudes, or two species? Could a roster partner sit on a party-mode panel? Could "mint a partner" and "add a review lens" be the same act?
3. **System-growth vs. knowledge-growth.** The build cycle governs *system* growth (new skills); Librarian/Research Partner govern *knowledge* growth (the wiki). `mint-partner` straddles both — exactly where the overlap lives.
4. **Portability vs. bespoke governance.** The module wants to be vault-agnostic/portable; the build cycle + versioned plugin is heavyweight and tied to *this* vault's evolution. Is the meta-layer **part of the shipped module** or **this vault's private scaffolding** the module merely assumes?
5. **Recursion.** Building the Vault module (renaming `vault-*` → `vlt-*`, changing contracts) is *itself* a build-cycle change. The module is both a product AND a product of the system.

### Decisions this session (2026-05-31) — the module REPLACES the `_meta` engine

The user's resolution to the collisions above: **the module should replace the vault's `_meta` build-cycle infrastructure outright, so the whole self-evolving system becomes replicable.** Maintaining alignment with the bespoke build cycle would add complexity that distracts from the module itself; with BMad doing the skill-authoring mechanics, the heavyweight cycle is largely redundant. The build cycle's real *purpose* — "the vault must evolve and adapt" — survives and is re-homed into module primitives; its *ceremony* is dropped.

**Re-homing map (what survives, where it goes):**

| Build-cycle apparatus | Real purpose | Re-homed as |
| --- | --- | --- |
| `scope-items/` + `workspace/` | The vault remembers what it wants to become | **Scope-item backlog** — a first-class module primitive (the evolution intake). Partners and the user file improvements here. **KEEP.** |
| build-cycle "mint" | New skills come into being | **`vlt-mint`** generalized: mint new *partners* AND mint new *capabilities*, including a partner extending *itself*. The evolution engine, now a capability every partner has. |
| retro → playbook-amend | The system improves its own process | **Reflective partners** — a partner hits friction mid-work, acts or files a scope-item. The loop lives in the personas, not a ceremony. |
| spec ≠ build / verify-separate | A self-change must not corrupt the system | **Persona lenses become a review council** — a self-mint gets a quick architect/skeptic panel before going live. Discipline at the right weight. |
| plugin versioning / repackage | Reproducible releases | **DROPPED.** The *module* is the replicable unit; git is the history. |
| `_meta/conventions/` | The contract every write obeys | **KEPT** — still the safety rail; ships with the module. |
| `_meta/personas/*` (party-mode lenses) | Review perspectives | **KEPT + absorbed** — become the evolution-review council; resolves the "two casts" problem (partners do the work; lenses review self-changes). |

**Two payoffs the user named:**

- **Self-minting closes the loop the build cycle reached for.** The cycle evolved the vault *from outside* the skills; self-minting partners evolve it *from inside the cast* — the "it grows itself" promise that makes the module worth replicating. Mint becomes a capability every partner has, not a meta-skill you visit.
- **The two casts reconnect for free.** party-mode lenses (architect/skeptic/pragmatist/historian/moderator) become the partners' evolution-review council — the lightweight "verify" that replaces the spec/verify ceremony. One cast, two roles.

**Self-minting granularity (decided):** *both, by situation.* Default = mint a **new operation skill** (the partner's "hands" grow; persona/SKILL.md stays stable; the operation pool is shared and composable). Escape hatch = **self-edit the partner's own SKILL.md** for genuine persona-level change (tone, non-negotiable, mode). `vlt-mint` decides which based on whether it's a new *hand* or a change to *who the partner is*; persona-level self-edits lean harder on the lens-council gate.

**Explicitly dropped:** plugin versioning, `_meta/plugin/` snapshots, the repackage playbook, the `workspace/cycles/` machinery, and the formal spec/build/verify ceremony. BMad's agent/workflow builders + the module's own validation (VM) + the lens council cover authoring safety; git covers history.

**Open-item resolutions (re-opened ideation, 2026-05-31):**

**#1 — Scope-item backlog: DECIDED.** A single living **`_agent/backlog.md`** (parallel to `_agent/log.md`), not one-file-per-item. Lowest ceremony, fully glanceable; an item promotes to its own note only if it grows into real design work. Every partner reads it on activation — making the activation ritual four reads: `index.md` (knowledge state) + recent `log.md` (activity) + **`backlog.md` (what the vault wants to become)** + own `thread.md` (relationship). This is what makes reflection cross-partner: one partner files a gap, every partner sees it next session. Minimal schema (dropped `proposed/scoped/actioned`, `cycle_id`, `finding-backlink`): `## Open` / `## Done` sections, each entry tagged `(kind, by)` with a one-line `why`. `kind` ∈ `capability-gap` | `maintenance` | `knowledge-gap` — `vlt-mint` filters for `capability-gap`; `maintenance` items feed lint (and inline merges). `dropped` for decided-against.

**#2 — `vlt-mint` engine: DECIDED.** *Two paths by weight,* mirroring lightweight-vs-full minus ceremony. (a) **In-flow capability mint** (common): a partner builds itself a new "hand" (an operation skill) inline, authored directly from `vlt-mint`'s own contract-loaded **operation-skill template** — no external builder, no flow break. (b) **Deliberate partner mint** (rare): a from-scratch persona runs richer discovery — `vlt-mint` may invoke `bmad-agent-builder` for it — then wraps the output in the partner contract, registers it in the roster, creates its `thread.md`. **The partner-contract scaffold** (activation reads `index`+`log`+`backlog`+`thread`; single-writer respect; conventions; roster registration; mode handling) **is always owned locally by `vlt-mint` as a template, never delegated** — that's what guarantees every minted thing fits the contract regardless of how its body was authored. The persona-level self-edit path (from #self-minting decision) edits an existing partner's SKILL.md directly under the same locally-owned contract.

**#3 — Lens council gate: DECIDED.** A **fixed `kind → council` mapping**, not a per-mint judgment call (ungameable, predictable). `operation skill → no council` (frictionless, in-flow); `new partner → architect (+moderator)` fit/overlap check; `persona self-edit → full panel`; `convention edit → full panel`. The trigger rule is **already encoded in the persona drafts themselves** — the Skeptic's and Architect's "Best Used When / Exclusion case" sections describe exactly this blast-radius gating (skip on cheap/reversible/no-structural-reach; fire on irreversible/high-blast-radius/contract-touching). `vlt-review-council` is the skill that runs the panel (moderator always synthesizes the verdict). The common case (a partner building itself a hand) stays frictionless; a partner rewriting its own contract gets real scrutiny.

**#4 — Reflective partners: DECIDED.** *Proactive file + surface, never silent; acting stays deliberate.* The key move is splitting **capture from action**: filing a backlog item is the cheapest, most reversible act in the system (just a line in `backlog.md`) — by the blast-radius gate it needs *no* approval, so requiring confirmation per capture would be the very ceremony we're escaping. So a partner that notices friction (mid-work or on activation) **files the item autonomously and mentions it in-flow** ("noted in backlog: 3 pages drifting on grid-bottleneck") — transparent, never behind-your-back. It does **not** auto-*act*; building from the backlog is deliberate/user-initiated, with the risky end already council-gated. This is the re-homing of the old retro→amend loop: *reflection (noticing) is continuous and autonomous; amendment (acting) is deliberate.* It also settles the original plan's "proactive nudge vs. quiet discipline" question — it is both: quietly captures, openly mentions, never acts unasked.

**All four open items resolved (2026-05-31).** The structured sections below (Architecture, Skills, Configuration, Setup, Integration, Roadmap) are rewritten to match these decisions.

### Existing system (the starting point — built manually, works today)

A knowledge-compounding "LLM wiki" vault at `~/Vaults/core`:

- **PARA layer** — `projects/`, `areas/`, `resources/` for human-facing deliverables
- **Wiki layer** (`_agent/wiki/`) — the real source of truth. 60+ canonical pages, each backed by counted sources, governed by an `index.md`. One concept = one canonical page.
- **Conventions** (`_meta/conventions/`) — `frontmatter`, `wiki-supersession`, `wiki-consolidation`, `extraction`. These are the rules of the system.
- **Trail** — `_agent/sessions/` + `_agent/log.md` record every operation; `_agent/research/` holds research notes.
- **Existing skills (the operations):**
  - `vault-ingest` — process a brought-in source into the wiki
  - `vault-research` — go to the web, build new knowledge, file a research note
  - `vault-query` — answer from accumulated wiki knowledge, file back when valuable
  - `vault-extract` — shape wiki knowledge into a PARA deliverable
  - `vault-lint` — health check the wiki (scoped by default, `--full` available)
  - `vault-consolidate` — merge drifted/duplicate wiki pages, preserving history
  - `party-mode` — multi-lens panel (debate / retro modes)
- There's even a `llm-wiki-pattern.md` wiki page — the system documents its own pattern.

### Core question driving this ideation

The skills already work as a loose collection. **What does turning them into a BMad module unlock?** Candidate answers to explore: a persistent agent persona (a "librarian/curator" you talk to), shared memory across operations, an orchestrator that routes intent to the right operation, proactive maintenance, an installable/portable package others could adopt, a dashboard over the wiki's health and growth.

### The central insight (from user, this session)

> "The overall agent persona is lacking in perspective."

The vault today is a **toolbox, not a partner**. Seven sharp operations, but no single *curator with a point of view* who has been present across all of them. The user's three stated wants are all symptoms of this same gap:

1. **Seamless BMad integration** — wants brainstorming / research / design-thinking / party-mode woven *into* the vault flow, not invoked separately. (party-mode was itself directly inspired by BMad.)
2. **Maintenance is friction** — user has to *remember* to lint/consolidate. Wants it to just happen / be surfaced proactively.
3. **Ideating & introducing new skills is slow, clunky, sometimes ineffective** — the meta-process of growing the system is itself painful.
4. **Modes of use** — sometimes pure *operations* ("just read a great article, ingest it"), sometimes *exploratory* ("chat through concepts, learn something"). The system handles operations fine but the exploratory/learning mode lacks a persona with perspective.

### Emerging direction (to validate, not locked)

A **curator agent with perspective** that lives in the vault: a conversational knowledge partner who knows the wiki's state, routes intent to the right vault operation, weaves in BMad thinking tools, and carries the maintenance discipline so the user doesn't have to. The seven existing skills become its capabilities / sub-operations rather than things the user picks by name.

Open question raised by user: ideating/introducing NEW skills is painful — could the module itself help grow itself? (Possible meta-capability.)

### The persona is actually a CAST (session refinement)

User doesn't want one persona — they named several relationships, with an explicit "etc.":

- **Librarian** — maintains the wiki, keeps it healthy, organized, single-home per concept. (Owns: ingest, lint, consolidate, extract, the index.) Calm, custodial, protective of the collection.
- **Research partner** — challenges the user to learn and explore new ideas; goes out to build new knowledge. (Owns: research, query-as-exploration.) Curious, pushes back.
- **Design partner** — (named as a "for example") helps think through / make things. Likely the natural home for BMad design-thinking / brainstorming.
- **"etc."** — the cast must be **extensible**. Adding a new partner should be easy. This directly addresses pain point #3.

What they share: **one brain = the vault/wiki.** All partners read and write the same knowledge base; that shared memory is what lets them be aware of each other's work (librarian knows what research partner just learned; research partner can push on what the librarian sees the user circling).

**Persona tone (all of them):** opinionated but not domineering — "doesn't reject my intellectual or creative process, but doesn't just take it at face value either." Productive friction. A partner, not a yes-man and not a gatekeeper.

### BMad integration depth (decided this session)

**Former:** the agent(s) *reach for* existing BMad skills mid-flow (brainstorming, research, design-thinking, party-mode) as tools, invoked when the moment calls for it. Rebuilding some skills to be vault-aware is a possible later enhancement, NOT an initial goal. Keeps scope contained.

### Summoning model (decided this session) — Option B: a roster summoned by name

User chose: **a roster of distinct agents, summoned deliberately by name**, each feeling like a *different person*. NOT one agent changing hats (A), NOT a head-curator orchestrator (C). Confirmed: librarian and research-partner should feel like genuinely different people.

Architecture implication: **multi-agent module with shared vault memory.** Each agent is its own persona/skill; the existing `vault-*` skills become operations the agents orchestrate (the agents are the personas; the vault operations are their hands). The shared brain (wiki/vault) is what keeps the roster coherent — they're different people looking at the same collection.

Likely cast → capability mapping (to refine in Phase 5):
- **Librarian** → ingest, lint, consolidate, extract, index/health. Custodial.
- **Research partner** → research, exploratory query, reaches for BMad research/brainstorming. Challenging.
- **Design partner** → design-thinking, brainstorming, possibly party-mode. Generative.
- Roster is **extensible** by design (the "etc.").

### Stretch / emergent ideas (user excited about ALL of these — carry into the plan)

- **Proactive maintenance via the librarian** — the librarian carries the lint/consolidate discipline and *nudges* ("6 ingestions since last lint — want me to sweep?"). Turns maintenance from a chore the user polices into something the persona owns. (Open: proactive nudge vs. quieter background discipline — decide in Phase 4/5.)
- **Cross-partner handoffs** — research partner finishes a deep dive and hands the librarian a source to file; design partner calls a party-mode panel on a contested idea; librarian flags "you keep circling X" and the research partner picks it up. The shared vault is the handoff medium.
- **Mint a new partner (meta-capability)** — directly solves pain point #3. A capability that scaffolds a NEW roster member (persona + capability wiring + memory hookup) so growing the cast is easy, not clunky. Possibly its own meta-skill or a librarian/curator capability. This is the module helping the module grow itself.
- **Dashboard / "seeing it"** — a view over the vault: growth over time, wiki health (orphans, contradictions, stale pages), source counts, what topics are compounding, recent activity per partner. Feeds from the index + log + sessions trail. (Explore in Phase 4 UI section.) → **Deferred to v2.**

### v1 scope (decided this session)

- **v1 roster: Librarian + Research Partner** (2 partners — proves "different people, one brain").
- **Mint-a-partner: IN v1** — ship the machine that makes partners. Design Partner and Codebase Partner become the user's first mints rather than hand-built skills.
- **Dashboard: deferred to v2.**
- Design Partner, Codebase Partner: deferred — created later via mint-a-partner.

### Two-vault reality (decided this session) — Vault is vault-agnostic

User runs TWO vaults today: **work** and **personal**, same core idea, with local divergence (work vault maintains knowledge on various codebases; personal vault does not). Implications:

- The module must be **vault-agnostic**: you point the roster at a chosen vault (config: vault root / active vault). Personal vault shared this session: `~/Vaults/core`.
- **All memory lives inside the vault** (shared wiki + per-partner personal thread). Switching vaults switches BOTH automatically → work-Librarian and personal-Librarian are structurally different people with different knowledge and different relationship threads. No cross-contamination, no manual scoping.
- **The roster can differ per vault** — work vault may mint a "Codebase Partner" the personal vault never has. The extensibility wish (#3) and the two-vault reality are the same feature.

### Verification pass (2026-06-01) — portability hardening + conventions audit

A plan-verification session surfaced that the `status: complete` plan had three portability blockers and several smaller gaps, now resolved into the structured sections:

- **Configurable structure (decided):** vault sub-paths are no longer hardcoded. A `vault_root` + overridable **structure map** (BMad pattern) replaces the literal `~/Vaults/core` default, which was a portability leak shipping one machine's home path. (User chose "root + overridable map" over full per-path config or root-only.)
- **The `CLAUDE.md` constitution (decided):** the real operating rules live in the vault's 373-line `CLAUDE.md`, not in `_meta/conventions/` — so a fresh vault would be missing them. Resolution: **internalize the rules into the partner contract + ship `_meta/vault-operating-contract.md`** (read on activation), setup writing only a minimal `CLAUDE.md` pointer. (User chose "internalize + ship rules doc" over generating a full `CLAUDE.md`.) This is what actually makes the "replaces `_meta`, becomes replicable" claim true.
- **Web access (decided):** today's vault *mandates* a Tavily MCP and forbids `WebSearch`/`WebFetch` — but that rule is **omitted from the module** as a host-level concern (consumer project / Claude settings own it). The adapted ops drop their Tavily coupling and use tool-agnostic "reach the web" wording. (User decision: "omit from the module.")

**Deferred (non-blocking) convention tightenings** from the audit, parked here so they aren't lost but don't gate the build: standard frontmatter field ordering; `sources:` dedup + ordering rules; a "≥50% claims superseded → consider page-level" threshold in supersession; an explicit no-merge rubric ("distinguishable by a single adjective or reader intent → distinct, skip") in consolidation; lint emitting a structured/parseable report and explicitly handling `[!stale]` markers. These improve quality but are not portability or correctness blockers.

## Build Roadmap

Recommended order and why:

0. **Assemble the shipped governance bundle.** ✅ **DONE (2026-06-01).** Audit + prune the conventions (strip dropped-ceremony schemas; parameterize paths; point frontmatter to its single source), and author `_meta/vault-operating-contract.md` from the `CLAUDE.md` inventory (see Vault Operating Contract + Conventions Audit). This is a prerequisite: the partners and ops are built *against* this governance, and setup installs it. Mostly extraction + pruning of existing material, not net-new authoring.
   - **Staged at `{project-root}/governance/_meta/`**, mirroring the target-vault layout so the setup skill can copy `governance/_meta/` → `{vault_root}/_meta/` verbatim. Contains: `vault-operating-contract.md` + pruned/parameterized `conventions/{frontmatter,wiki-supersession,wiki-consolidation,extraction}.md`. The `_meta/personas/` lenses are finalized with step 2 (`vlt-review-council`) and join the bundle there.
   - **Folded in two refinements from the work vault's (`sayari-workspace-v2`) more-evolved conventions** (the rest of that file is build-cycle ceremony this module dropped): (a) an **Obsidian YAML syntax-rules** block — quote wikilink-valued fields, no nested maps, no backtick wikilinks, flat schemas, bare paths for non-graph lists, no inline-bold duplication of frontmatter; (b) the **`created` (immutable) + `last_updated` (bumped)** split replacing the single ambiguous `date:` — `last_updated` is what `vlt-lint` reads for staleness; written-once notes (research, sessions) carry only `created`. *Deliberately NOT adopted: the work vault's binary `trust: endorsed` model (kept the 4-tier ladder) and its `freshness:`/derived-artifacts fields.*
   - All paths re-expressed against the `vault_structure` logical names (`{wiki}`, `{index}`, `{log}`, `{backlog}`, `{archive}`, …). Frontmatter duplication resolved: the contract points to `frontmatter.md` as the single source. Scope-item schema replaced by the lightweight `{backlog}` schema. `wiki-consolidation.md` reframed (consolidate skill dropped) → detection in `vlt-lint`, merge folds into `vlt-ingest`. Tavily/web policy, skill allowlist, build-cycle/plugin, and Obsidian Sync rules dropped per the audit. **Step 6 (CM) must wire `vlt-setup` to install this bundle.**
1. ✅ **DONE (2026-06-01). Adapt the operation layer (`vault-*` → `vlt-*`, vault-agnostic, improved).** All five built in `skills/` via the Workflow Builder (each with a `.decision-log.md`): `vlt-ingest` (single-writer; fuzzy near-dup detection, cross-source contradiction summary, re-ingest preview, folded-in merge), `vlt-query` (no web; provenance tagging, file-back rubric, contradiction ranking, hands wiki-page synthesis to the Librarian), `vlt-research` (tool-agnostic web, auto-checkpoint, feasibility gate, thin-vault prompt, hands wiki pass to the Librarian), `vlt-extract` (sanctioned PARA writer; hard ≥2-page gate, disk draft, trust-by-depth, caveat carry-forward), `vlt-lint` (structured report, validated scope + mtime staleness, explicit `[!stale]`, near-dup → `maintenance` backlog item). All apply the cross-op contract (log-entry-only, partner-tagged) and governance alignment (no `key:`, `created`/`last_updated`, JIT-read shipped conventions). The operations are the partners' hands; the agents can't be fully exercised until these (a) resolve every path through the `vault_structure` map instead of hardcoding, (b) tag the session/log entry with the active partner, (c) drop the hard Tavily coupling for tool-agnostic web access, and (d) land the per-skill improvements over today's versions (see Operation layer briefs). More than a mechanical rename — these are *improved* successors. Doing it before the agents means they're built against their real, finished tools. *(The rename + path plumbing could fold into Create Module's migration step; the improvements are real build work.)*
2. ✅ **DONE (2026-06-01). Adopt `vlt-review-council`** from the `party-mode` mechanism + the shipped `_meta/personas/` lenses. Built in `skills/vlt-review-council/` (with `.decision-log.md`): parallel persona spawn → moderator synthesis → 4-part verdict; two modes (review-a-mint by the fixed `kind → council` blast-radius map; debate-a-contested-question full-panel default); party-mode's **retro mode dropped** (re-homed into reflective partners + backlog); single-writer respected (file-backs flow through the Librarian); graceful degradation for missing lenses / no-subagents. The **five persona lenses were finalized into the bundle** at `governance/_meta/personas/{architect,skeptic,pragmatist,historian,moderator}.md` (`--draft` dropped, frontmatter normalized, `party-mode`/build-cycle references genericized, `Best Used When`/`Exclusion case` kept verbatim for the gate). Establishes the persona-panel verdict contract `vlt-mint`'s gate depends on.
3. ✅ **DONE (2026-06-01). Build `vlt-agent-librarian`.** The spine of the roster — sole canonical writer, handoff target for all partners. Built in `skills/vlt-agent-librarian/` (SKILL.md + `customize.toml` `[agent]` block + `.decision-log.md`) **directly to the partner contract, not via the bmad-agent-builder sanctum** (the sanctum stores memory in `_bmad/memory/`; partners store it in the in-vault `thread.md`). Establishes the partner-contract pattern `vlt-mint` will template: the **four-read activation ritual** (contract + index + log + backlog + own thread.md), the single-writer non-negotiable, ops-as-hands delegation (ingest/lint/extract/query), proactive file-and-surface maintenance, partner-owned session note, and `thread.md` (Bond/Thread/Self) memory. The **thread.md three-section structure was single-sourced into the operating contract** (new "Partner memory — the thread" section) so both partners + setup + vlt-mint share one definition. `agent_type = "memory"` (remembers via the in-vault thread, not a sanctum); no override surface (memory-agent default). Build it first so the Researcher has a real hand-off target.
4. ✅ **DONE (2026-06-01). Build `vlt-agent-researcher`.** The opinionated sparring partner, built in `skills/vlt-agent-researcher/` (SKILL.md + `customize.toml` `[agent]` block + `.decision-log.md`), mirroring the Librarian's partner contract with inverted temperament. Writes research notes (never canonical pages — hands those to the Librarian, preserving single-writer); four-read activation; surfaces the running inquiry from its `thread.md`; reaches for BMad thinking tools (`bmad-brainstorming`, `deep-research`, design-thinking) and `vlt-review-council` for contested ideas; files `knowledge-gap`/`capability-gap` backlog items. `agent_type = "memory"`, no override surface. This is where the module's "has perspective" tone lives most strongly.
5. ✅ **DONE (2026-06-01). Build `vlt-mint`.** The evolution engine, built in `skills/vlt-mint/` (SKILL.md + `.decision-log.md` + two `assets/` scaffold templates that encode the established patterns: `operation-skill-template.md` from the 5 ops, `partner-agent-template.md` from the 2 partners). Four capabilities (mint an op / mint a partner / canonical self-edit / retire); two paths (in-flow template vs. deliberate `bmad-agent-builder` with sanctum→contract mapping); the fixed `kind → council` blast-radius gate via `vlt-review-council`; the locally-owned scaffold guarantee; install + register into `module.yaml`/`module-help.csv`; retire archives the `thread.md` (never deletes); the drift boundary (ungated `## Self` never touches mint). Built last so it encodes the *patterns the two partners and the operation layer established* — — it mints operation skills, partners, and self-edits that match the now-proven contract, and wires in the `vlt-review-council` gate. Reference the two agents + the operation layer as templates. *(The `_agent/backlog.md` primitive is just a file — created at setup, no build step; the agents read/write it from step 3 on.)*
6. **Create Module (CM).** Scaffold module infra + the `vlt-setup` skill (vault registry + structure overrides; structure verification; **install the shipped governance bundle — pruned conventions + personas + operating contract**; write the minimal `CLAUDE.md` pointer; scaffold partner layer + `backlog.md`; dependency checks; no web check). Then **Validate Module (VM)**.

After v1 ships: use `vlt-mint` to create the **Design Partner** (and **migrate the Extract capability** from the Librarian to it — see Librarian design notes), then a work-vault **Codebase Partner** — proving the mint loop end-to-end. Then v2: the dashboard.

**Next steps:**

1. Build each skill using **Build an Agent (BA)** or **Build a Workflow (BW)** — share this plan document as context
2. When all skills are built, return to **Create Module (CM)** to scaffold the module infrastructure
