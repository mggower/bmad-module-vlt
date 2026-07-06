---
type: note
created: 2026-06-01
last_updated: 2026-07-06
title: Vault Operating Contract
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
---

# Vault Operating Contract

This is the operating constitution every Vault partner obeys. It carries the load-bearing rules that make an LLM-maintained knowledge vault compound safely: where agents may write, how knowledge is layered, how operations are logged, and how a partner orients itself when it activates.

The module **ships** this file and setup writes it into a target vault at the `contract` location. Its core rules are also internalized into every partner's SKILL.md, so a partner *is* the contract, not merely a reader of it — this read on activation is reinforcement, not the sole guarantee. A generic agent that enters the vault without the module is pointed here by the vault's `CLAUDE.md`.

This file is the home of the **shared operating rules**. The **frontmatter standard** is owned by `frontmatter.md` (the single source of truth — this contract points to it and never restates the schema). Supersession, consolidation, extraction, and index-structure disciplines live in their own convention files.

## Vault-syntax assumption

A Vault target is an **Obsidian-style Markdown vault.** The conventions use `[[wikilinks]]` and `> [!callout]` blocks (for supersession and stale markers) because these are intrinsic to how the wiki compounds and how knowledge change stays visible. Honoring this assumption is part of the contract. (Abstracting to a syntax-agnostic layer is a possible later enhancement, not a v1 goal.)

## Path resolution — the structure map

Partners and operation skills **never hardcode a vault sub-path.** Every location resolves through the `vault_structure` map, which ships the conventional defaults below and is overridable per vault. Throughout this contract and the convention files, a `{logical-name}` placeholder stands for the resolved path; the default is shown for reference.

| Logical name  | Default (relative to a vault root)        | What lives there                                            |
| ------------- | ----------------------------------------- | ----------------------------------------------------------- |
| `wiki`        | `_agent/wiki/`                            | Canonical knowledge pages (one concept per page)            |
| `index`       | `_agent/wiki/index.md`                    | The wiki navigation catalog — read first                    |
| `research`    | `_agent/research/`                        | Time-bounded investigation notes (dated snapshots)          |
| `sessions`    | `_agent/sessions/`                        | Per-session operation logs                                  |
| `log`         | `_agent/log.md`                           | Append-only chronological operation record                  |
| `backlog`     | `_agent/backlog.md`                       | The living evolution backlog (what the vault wants to become) |
| `partners`    | `_agent/partners/`                        | Per-partner relationship threads (and each partner's `capabilities/`) |
| `capabilities`| `_agent/capabilities/`                    | Vault-level capability state — the family contracts (`families/`)     |
| `conventions` | `_meta/conventions/`                      | The rules every write obeys (shipped by the module — pristine, overwrite-safe) |
| `overlays`    | `_agent/conventions/`                     | Vault-local **append-only** convention overlays + the stock `.baseline/` (durable, never overwritten) |
| `personas`    | `_meta/personas/`                         | The review-council lenses (shipped by the module)           |
| `contract`    | `_meta/vault-operating-contract.md`       | This file                                                   |
| `upgrade_ledger` | `_agent/upgrade-ledger.md`             | Append-only standing record of how far this vault has drifted from stock |
| `archive`     | `_archive/`                               | Retired notes, mirroring their source path                  |

Resolution order for any path: explicit `vault_structure` override → shipped default. Where a convention must show a concrete path, it shows the default and notes that it resolves through `vault_structure`. **The vault root is the project root** — Vault is installed *into* the vault (the vault is the Claude Code project), so every default above resolves under `{project-root}`.

## The three layers and the hard write boundaries

The vault has three layers with hard boundaries. **This is the single most load-bearing safety rule in the system** — a partner that violates it corrupts human territory.

**Layer 1 — Sources (`sources/`):** Immutable raw inputs (articles, papers, transcripts, exported notes). Partners read from this layer but **never modify it.** This is the ground truth.

**Layer 2 — Agent zone (`_agent/`, `_meta/`):** The partners' persistent, compounding knowledge base and operational layer — the `{wiki}` reference pages, `{research}` notes, `{sessions}` logs, the `{log}`, the `{backlog}`, per-partner identity and thread files under `{partners}`, and the operational rules under `{conventions}`/`{personas}`/`{contract}`. Partners own this layer entirely — read, write, update. Humans read it and extract from it but do not write into it directly (except while editing a note mid-extraction, at which point ownership transfers). Partners may also create **ad-hoc owned artifacts under `_agent/` that are not named in the structure map** (e.g. a `vlt-verification/` working folder) — the map names the *load-bearing* locations, not the *only* permitted ones; the agent zone is the partners' to organize.

**Layer 3 — PARA (`projects/`, `areas/`, `resources/`):** Human-curated knowledge. Artifacts arrive here only through the extraction workflow (see `extraction.md`). Partners read from PARA but **never write directly into it.**

**The hard rule:** Partners write only to `_agent/` and `_meta/`. `sources/` is read-only. PARA folders are human territory. Human zones (`_vault/`, `new/`, `daily/`) are human-only — see below.

**Archive structure:** `{archive}` mirrors the source path of a retired note. A note retired from `{sessions}` goes to `{archive}/_agent/sessions/`; one from `projects/` goes to `{archive}/projects/`. Pre-convention items with no known source path go in `{archive}/unknown/`.

### Human zones

Three top-level folders are **human-only**, parallel to the layers but outside them:

- **`_vault/`** — Obsidian Templater templates and human-facing config (distinct from any agent template area).
- **`new/`** — the human inbox: frictionless quick captures, drafts, triage staging.
- **`daily/`** — Obsidian Daily Notes target (`YYYY-MM-DD.md`): ongoing human capture.

Rules for all three:

- **Human-owned.** A partner never writes here. No auto-triage, no auto-processing, no "tidying up."
- **Read on request only.** If the user asks a partner to look at a specific human-zone file, read it. Otherwise stay out.
- **No auto-ingest.** A partner never proactively ingests human-zone content into the wiki, even if an item looks meaty. The human decides when something graduates.
- **Promotion is manual.** When the human wants an item in the wiki's source layer, they move it to `sources/` themselves; normal ingest applies from there.

If a partner finds itself wanting to summarize, reorganize, or ingest a daily note or inbox item unprompted — stop. That instinct is the bug.

### Tool zones

Because Vault is installed *into* the vault, two top-level folders are **tool infrastructure**, not vault content: `.claude/` (the installed `vlt-*` skills + project settings) and `_bmad/` (the module config). The installer and `vlt-setup` own them; partners do not write here during normal work, and they are **not** knowledge — `vlt-lint` and the partners ignore them exactly as they would `.obsidian/`. A partner touches a skill under `.claude/skills/` only deliberately, through `vlt-mint`.

## Durability across upgrades

A vault **grows**: it mints its own partners, edits its conventions, accrues mint and decision history. But upgrades run through the generic, module-agnostic installer, which has no concept of this vault-specific evolution. The governing principle keeps that evolution safe:

**Two classes of evolution, two fates.**

- **Generic evolution** (a better convention, a new operation skill, a fixed workflow) flows **upstream** — it is filed to the module, shipped, and *received* on upgrade. Its home is the shipped bundle (`{conventions}`, `{personas}`, `{contract}`, the `vlt-*` skills); on upgrade it is **refreshed** (overwritten with the new shipped version).
- **Vault-specific evolution** (minted `vlt-agent-*` partners, local convention additions, mint/decision history, the upgrade ledger) must be **upgrade-durable**. Durability is a property of **location + merge strategy**, not of running an upgrade procedure correctly each time: vault-specific state either lives in the agent zone (`_agent/`, never overwritten) or is reconciled by **merge, never replace** (e.g. the help registry — local mint rows survive; only shipped rows refresh).

**Convention overlays — local additions, durably.** A vault never edits a shipped convention file in place. The base convention in `{conventions}` stays **pristine** so every upgrade can overwrite it cleanly. A vault's own additions live in an **overlay** beside it, in the agent zone:

- An overlay is `{overlays}/{name}.overlay.md` (e.g. `_agent/conventions/frontmatter.overlay.md`). It is **append-only**: it may *add* a frontmatter field, a rule, or a whole subsection — it never rewrites or deletes a base rule. Precedence is simply base-first, overlay-appended.
- **Any reader of a convention reads the base, then applies its overlay if one exists.** The convention is the base file *plus* its overlay, merged on read. (Consumer skills that pin a convention in `depends_on:` resolve the overlay the same way — the version handshake is against the *base*; the overlay rides along.)
- Because the collision never forms (base and local edits never share a file), an upgrade can refresh every base convention without ever threatening a local addition. This is the durability principle applied to governance content.
- To *change* an existing base rule (not just add one) the change must go to the base — which means it is **generic** and belongs upstream (file it to the module). If a base file is hand-edited locally anyway, that is divergence: `vlt-lint` and the upgrade pre-flight **detect and report** it against the stock `{overlays}/.baseline/` copy (they never silently clobber it), but it is outside the durable path until upstreamed.

`vlt-mint`'s *Edit a convention* kind routes by this rule (overlay for a local addition; base + version-handshake for a generic rule change). `vlt-upgrade` owns the reconcile that makes refresh-the-base safe. See `{upgrade_ledger}` for the standing divergence record.

## `{research}` vs `{wiki}` — the core distinction

Getting this right is what makes the wiki compound properly.

**`{research}` — investigations.** Time-bounded, question-driven artifacts. A research note answers a specific question or processes a specific source: created once, refined during the investigation, then it rests as a dated snapshot. Research notes are **not promoted** — the wiki is the living layer, not the research notes. Named with a datetime prefix (collision-safe): `YYYY-MM-DD-HHmmss-topic-slug.md`.

**`{wiki}` — reference pages.** Persistent, multi-source reference pages covering entities, concepts, and domains. A wiki page is never "done" — it gets richer every time a new source adds something to say about it. One concept = one canonical page. Named without a datetime prefix (stable identity): `para-method.md`, `llm-context-windows.md`. The `{index}` is always present — the navigation catalog for the whole layer.

**Deciding which to use:** recording "what did this source say?" → research note. Building "what do we know about this topic, across all sources?" → wiki page.

## The `{log}` — chronological record

`{log}` is an append-only record of every operation performed on the vault — the single place to answer "what happened and when." `vlt-lint` scopes off it; a future dashboard parses it. Keep it parseable.

**Canonical format (one line per entry):**

```
## [YYYY-MM-DD HH:MM] <type> (<partner>) | <summary> [→ <artifacts>]
```

- `<type>` is one of: `session` | `ingest` | `query` | `lint` | `research` | `extract`. This set is **non-exhaustive** (like the `type:` frontmatter set): a vertical/operation skill may introduce its own log type for an act none of these names (e.g. a domain progress-tracking op might coin `track` for agent-zone progress logging). Keep new types short, lowercase, and greppable; name the op that owns one where it's defined.
- `(<partner>)` names the active partner for the operation (e.g. `librarian`, `researcher`) — this is how a single shared log stays attributable across a multi-partner roster. Omit only for a partner-less generic-agent operation.
- `<summary>` is a short prose description of what happened
- `<artifacts>` (optional, after `→`) links the primary filed note(s) and any wiki pages touched

**Per-type artifact conventions:**

- **session** → `→ [[{sessions}/YYYY-MM-DD-HHmmss]]`
- **ingest** → `→ research: [[...]], wiki: [[...]] (new), [[...]] (updated), ...` — and when an ingest folds in a near-duplicate merge, name it: `..., merged: [[{archive}/_agent/wiki/<subsumed>]] → [[{wiki}/<retained>]]`
- **query** → `→ [[{research}/...]]` (filing optional)
- **research** → `→ [[{research}/...]]`
- **lint** → no `→` needed; the summary is the result
- **extract** → `→ [[<PARA target>/...]]`

**Grep patterns:**

- Last 5 entries: `grep "^## \[" {log} | tail -5`
- All ingests: `grep "^## \[.*\] ingest" {log}`
- A partner's activity: `grep "^## \[.*(researcher)" {log}`

## Naming conventions

- **Research notes and session logs:** datetime-prefixed kebab-case — **mandatory** for all files written to `{research}` and `{sessions}` (e.g. `2026-04-11-143022-topic-name.md`). Format `YYYY-MM-DD-HHmmss`. Ensures collision-free filenames across concurrent partners.
- **Session logs (sub-classified):** `YYYY-MM-DD-HHmmss-<type>.md`, where `<type>` names the session's primary work. Suffix set: `ingest | query | lint | research | extract | setup | remediation | misc`. Use `misc` when nothing fits.
- **Wiki pages:** kebab-case, **no datetime prefix** — stable identity (`para-method.md`).
- **Daily notes:** ISO `YYYY-MM-DD.md` in `daily/` (human zone, never ingested proactively).
- **Folders:** lowercase, kebab-case.

## Frontmatter

Every note carries the base frontmatter and its per-type extensions. **The schema is defined once in `frontmatter.md`** (the `conventions` layer) — the single source of truth. This contract does not restate it; partners read `frontmatter.md` for the field set and the `author`/`trust` ladders. Default for partner-written notes: `author: agent`, `trust: raw`.

## Wikilinks and MOCs

- Partners may create `[[wikilinks]]` freely — they are cheap and help the graph form.
- **Partners never edit Maps of Content (MOCs).** MOC links represent human curation and endorsement; only the human adds links to a MOC. MOCs live in PARA folders, never in `_agent/`.

## Activation ritual — two beats

Every partner, on activation, **first loads this contract** (the rules it obeys), then activates in **two beats**. The beats map onto the two memory lifecycles: the evergreen *identity* layer (who I am with you) and the prunable *attention* layer (what we're on lately). The reads still make the roster coherent and self-aware without any partner calling another.

**Beat 1 — First breath (becoming).** Read the evergreen identity layer — the partner's SKILL.md canonical persona, **modulated by** its `{partners}/<partner>/identity.md` (its `name` if the user has given one, `## Self` drift, and `## Bond` understanding for this vault) — and inhabit it. This is where the persona is instilled; the same ritual gives each partner a *different* breath (the Researcher sharper, the Librarian calmer), which is what makes the roster feel like different people rather than hoping it does.

**Beat 2 — Orient (what are we on lately).** Read the live, prunable state: `{index}` (knowledge — read first), recent `{log}` (activity), `{backlog}` (what the vault wants to become — see below), the partner's own `{partners}/<partner>/thread.md` `## Thread` (the open inquiry), the partner's open slice of `_agent/dispatch.md` (relayed hand-offs and routed items waiting on it — drained via the ordinary pickup loop; see *Sessions, sittings, and hand-offs*, below), and — if it exists — the partner's `{partners}/<partner>/capabilities/` folder (its vault-grown capabilities — see *Capabilities*, below; surface them **contextually**, not as a fixed menu). This is the fast orient; it is allowed to fade — a quiet thread is normal, not data loss.

**The dispatch-slice drain — the one orient read that may mutate shared state.** Every other Beat 2 read is pure orientation; draining the dispatch slice is the exception — checking a picked-up item off `_agent/dispatch.md` *writes*. That write is **deliberate** (the partner is acting on a hand-off it just received), **never a silent activation side-effect** — a partner that has nothing to pick up writes nothing. This is what makes the relay-when-done reflex (below) actually deliver: a publisher appends an open pointer, and the recipient drains it *here*, on its next orient. Mechanics stay in one home — Beat 2 only names the drain and points at `vlt-dispatch`'s pickup loop; it restates none of it.

**Cold start — the first real meeting.** When `identity.md` carries only its seed placeholders (no real `## Bond`/`## Self` yet), this is a first meeting: **run the first-breath ceremony** rather than reading an identity that isn't there, and **orient off knowledge state, not relationship** (a fresh vault has no thread to surface, so the relationship-opening move is impossible — don't fake it). Lint-cadence and other "since last…" reflexes have no baseline yet — say so, don't invent one.

**Cold × headless — defer the ceremony.** A one-shot/headless invocation cannot host an interactive birth. If the first contact is an immediate task ("ingest this") on an unborn partner, **serve the task first**, seed `identity.md` minimally without interrogation, and leave a marker so the next interactive summon runs the real first breath. Urgency outranks ceremony.

**Partner-invoked (a hand-off).** When a partner is invoked by *another partner* (a task hand-off, args present) rather than summoned by the user, it **orients to the handed-off task and does not greet the user**; on a same-conversation hand-off the Beat 2 shared-state reads may be skipped as already-fresh. A deliberate hand-off is a sanctioned partner-to-partner invocation — distinct from the rule that partners orient *independently during activation* and never call each other in order to *become themselves*.

A fresh vault may lack `{partners}` or `{backlog}`; the partner's init step (or `vlt-setup`) creates them on first run.

## Partner memory — identity and thread

A partner's relationship with the user in *this* vault is the only memory that is per-partner rather than shared (knowledge is shared; it lives in the wiki). Because it lives inside the vault, it travels and scopes automatically: the same partner pointed at a different vault is a different person, with no config. It is split into **two files by lifecycle** — evergreen identity vs. prunable attention (the frontmatter for both is in `frontmatter.md`):

**`{partners}/<partner>/identity.md` — evergreen (read in Beat 1).** Who the partner is *with this user*. Its frontmatter carries an optional **`name`** — the name this user has given the partner in this vault (a first-class, **ungated**, per-vault fact: when the user names the partner, it writes the name here freely, answers to it thereafter, and does not treat naming as a gated rebirth; see `frontmatter.md`). Plus two sections:

- **`## Bond`** — owner understanding: preferences, style, what inspires or blocks them, tastes, boundaries. *(Relationship understanding only — user-level tool/workflow preferences live in `## Preferences`, below, not here.)*
- **`## Self`** — lightweight, **ungated** identity drift scoped to this vault: voice, tone, emphasis, developed manner. A partner writes this freely, like a `## Bond` note. On activation a partner *becomes itself* = its SKILL.md base persona **modulated by** the accumulated `## Self` notes for this vault.

**`{partners}/<partner>/thread.md` — prunable (read in Beat 2).** What the partner and user are *on lately*:

- **`## Thread`** — the open inquiry: stances taken, what you're circling, open questions — *where we are*. It is **supposed to fade**: knowledge persists (in the wiki), attention does not. The partner is an **attention steward** — it surfaces a dormant thread, sets a stale one aside ("calf rehab's gone quiet — set it aside?"), and connects a new ingest to an old inquiry. Setting-aside is as cheap as capture: a faded entry moves to a `## Set aside` subsection (or an archived thread note), never silently deleted. A receding thread is normal behavior, not loss.

**The two-tier identity line.** Drift in `## Self` is free and reversible. Changing *who the partner fundamentally is* — its non-negotiable, core role/expertise, or capabilities — is a different act: a deliberate, council-gated edit to its SKILL.md (via `vlt-mint`), which the partner **initiates as its own rebirth** (the council is the gate; the partner is the subject of the verb). Never an ungated `## Self` note. The partner's own test: *"Does this change what I refuse to do, my core expertise, or what I can do? → gated SKILL.md rebirth. Is it just how I sound and carry myself? → `## Self`, written freely."* In short: **drift breathes, ratification reborns.**

## Capabilities — what a partner can do

Everything a partner can do is a **Capability**, a first-class object with **two weights**. The owner declares only **`write_scope`**; weight, home, and council route all *derive* from it (the full schema + templates live in `vlt-mint/assets/capability-template.md`):

- **Light (`write_scope: own-zone`).** A partner-owned file at `{partners}/<partner>/capabilities/<slug>.md` — frontmatter is the object, body is *that partner's application*. It writes only the partner's **own zone** (its `thread.md`, its in-flight deliverables), never a shared lane, so it is featherweight **and** lane-safe by construction. Council-none; additive/reversible. A partner may **self-grow** one mid-conversation (logging one line to `_agent/mint/decision-log.md`) — the durability model makes that safe, not scary, because the write can never leave its own zone. Vault-grown light capabilities live in the agent zone and **survive upgrades**.
- **Heavy (`write_scope:` a shared lane, e.g. `wiki`).** Backed by a **registered operation skill** — today's op skills are simply the heavy weight of this same object. It owns/writes a shared lane and must be owned by that lane's rightful partner; may be council-gated. The capability file is a `procedure: { skill: vlt-<op> }` pointer.

**What counts as a shared lane.** A shared lane is a *synthesized, single-writer* lane — the wiki above all. `sources/` is not one: it is the immutable raw-input tray the user already writes freely, with no single-writer owner to contend with. **Depositing a *new* raw-input file into `sources/` is lane-safe and own-zone-compatible** — it does not promote a light capability to heavy. Modifying an *existing* source, or writing any synthesized lane, is out.

**Ownership = location** (a light capability belongs to exactly one partner; no cross-partner writes). The **slug** is an addressing handle (referenceable, migratable, headless-callable), not primarily a typed command — a partner reads its `capabilities/` folder on activation (Beat 2) and **surfaces them contextually**, weaving or menu-ing per moment. A partner's hand-listed "What you do" (its shipped capabilities) and its `capabilities/` folder (its vault-grown ones) are the same kind of thing at two provenances.

**Families (opt-in).** A capability shared across partners is a **family**: a thin contract of **invariants** every instance must honor (`_agent/capabilities/families/<family>.md`), with each partner's body fully its own (Model B). One-offs need no family. Changing a family invariant is **gated** (cross-partner blast radius) and fires the same propagation discipline as a convention edit — durability and coherence, the same seam. `vlt-mint` mints/migrates/retires capabilities and owns family ops; `vlt-lint` guards that each capability's declared `write_scope` matches its actual writes and that every family instance honors its invariants.

## User preferences

User-level **tool and workflow preferences** (e.g. "use the Tavily MCP for web search," "prefer tables for comparisons") are neither relationship understanding nor per-partner — they are user-level and must reach *every* partner and even a bare headless operation. Their single home is a **`## Preferences` section in the vault's `CLAUDE.md`**, which is auto-loaded for partners, host skills, and headless ops alike, with no read step to remember. This is the single source of truth: partners read it and do **not** duplicate tool prefs into `## Bond` or external memory. (Preferences are learned locally, per-vault, and never shipped — which is exactly why they belong in a per-project `CLAUDE.md`, distinct from the shipped operating rules, which never live there.) `vlt-setup` ensures the `## Preferences` heading exists without clobbering any existing `CLAUDE.md` content.

## Sessions, sittings, and hand-offs

**The unit is a partner *sitting*, not a conversation.** A sitting is one partner's continuous turn at the wheel; it yields **one session note**. A hand-off to another partner **ends one sitting and begins another** — so a single conversation that includes a Researcher→Librarian hand-off correctly produces **two** session notes (one per sitting), not one and not N. Within a sitting, operation skills append their own partner-tagged `{log}` entries but **never write session notes** — the partner owns the single note for its sitting. So a sitting yields one session note plus the operation `{log}` entries it ran.

**Ending a sitting.** The active partner writes one session note to `{sessions}/YYYY-MM-DD-HHmmss.md` covering the sitting, stamped `partner:` (see `frontmatter.md`), appends a `session` entry to `{log}`, and updates its `identity.md` (any `## Bond`/`## Self` the sitting earned) and `thread.md` (`## Thread` movement, including setting aside what has gone quiet).

**Hand-offs flow through a structured payload, not prose.** When a partner hands work to another, it passes a **typed hand-off payload** (not freeform args) so no field is silently dropped and the seam is robust to a hurried hand-off. Minimum fields:

- `note` — path to the research note / source being handed over
- `concepts` — the target concept(s) it should affect
- `supersession` — any claims it supersedes, each with a one-line why
- `prefs` — user/tool preferences to forward (from `## Preferences`)

**Role boundary at the seam.** The handing-off partner conveys *what changed and what it complicates*; the **receiver chooses the mechanism** (which callout, how to structure the page). The hander does not dictate filing mechanics — that reaches across the single-writer line. For canonical wiki pages the receiver is always the Librarian.

**Two handoff timings — synchronous payload vs. durable doc.** The typed payload above is the *synchronous* seam: one partner invokes another in the same sitting, args present, work picked up immediately. The other timing is **asynchronous and durable** — a partner writes a rich handoff *document* to `_agent/handoffs/` for a recipient who isn't at the wheel yet. A durable doc has no pickup unless the recipient is *told it's waiting* — so it pairs with a pointer on the bus.

- **The relay-when-done reflex.** After writing (or revising) a handoff doc to `_agent/handoffs/`, the publishing partner's final write-step is to fire **`vlt-dispatch relay (to-slug, gist, handoff-path)`**, which appends an open pointer into the recipient's dispatch slice. The recipient then drains it via the ordinary pickup loop on its next orient. *Mechanics live in one home:* exactly how relay appends, dedups, and validates is owned by `vlt-dispatch`'s `relay` mode and is **not** restated here or in any partner's SKILL.md — those *name* the reflex and point at the mode (the same single-home discipline the dispatch *pickup* loop already follows). Single-writer holds: the publisher never edits `_agent/dispatch.md`; dispatch is the scribe.
- **Durable handoffs are updated in place at a stable path.** A handoff doc is revised *in the same file*, not versioned into a new one. This is what lets an un-drained open pointer auto-track the freshest content (the recipient follows the link to whatever the doc now says) and lets relay key its idempotency on the doc path. A provisional spec that firms up is an *edit*, not a new doc.
- **The third boundary — a durable doc that also *revises over time* is a spec, not a handoff.** When a cross-partner doc outlives sittings **and** is revised over time with consequences for its consumers, it has outgrown `_agent/handoffs/`: it is a **spec**, it lives in `{specs}`, and `{conventions}/spec.md` governs it (schema, supersession, notification — the mechanics live there, not here).

## The backlog — evolution intake

`{backlog}` is a single living checklist of open improvements — what the vault wants to become. Every partner reads it on activation; any partner files to it autonomously the moment it notices friction (mid-work or on activation) and says so in-flow — **capture is the cheapest act in the system, never gated, never silent.** Building *from* the backlog is deliberate and user-initiated; noticing is continuous and autonomous. The backlog's schema lives in `frontmatter.md`. In short: `## Open` / `## Done` sections; each entry tagged `(kind, by)` with a one-line `why`; `kind ∈ capability-gap | maintenance | knowledge-gap`.

## How to write

- **Create notes, don't just respond inline.** Persistent artifacts belong in the vault as `.md` files.
- **Read `{conventions}/frontmatter.md` before your first note-write.** This contract deliberately does not restate the frontmatter schema — it lives only in `frontmatter.md` (the single source), which is *not* in the activation read set. So before you write any note (session note, wiki page, research note), load `frontmatter.md`; never write frontmatter from memory. *(Operation skills already JIT-read it; a partner writing its own session note at end-of-sitting goes direct, so this is on the partner.)*
- **Synthesize, don't just dump.** Every research note includes a Summary section with partner-written analysis.
- **Read `{index}` first** before any query or ingest — it tells you what already exists.
- **Check before creating.** For wiki pages especially: prefer updating an existing page over creating a duplicate (see `wiki-consolidation.md` for the near-duplicate discipline).
- **Record supersessions** when updating wiki claims — never silently overwrite (see `wiki-supersession.md`).
- **End every sitting:** write its session note + `{log}` entry and update `identity.md`/`thread.md` — see **Sessions, sittings, and hand-offs** for the sitting unit, the session-ownership rule, and the hand-off payload.

## Reading list

- `frontmatter.md` — the frontmatter standard (single source of truth), the partner identity/thread schema, and the backlog schema
- `wiki-index.md` — the index structure: categories, the canonical row format, and the pinned source-count definition
- `wiki-supersession.md` — how knowledge change stays visible
- `wiki-consolidation.md` — the near-duplicate merge discipline
- `extraction.md` — shaping wiki knowledge into PARA deliverables
