---
type: note
created: 2026-07-06
last_updated: 2026-07-06
title: Spec Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 1
consumers: [vlt-mint, vlt-dispatch]
enforcement_stage: declared
deferral_metric: "spec version bumps shipping without their relay entries"
deferral_threshold: "1 — any such bump promotes the deferred lint checks to next-mint priority"
review_after: 2026-08-17
---

# Spec Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/spec.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

A **spec** is a *durable, owned, versioned cross-partner contract*: authored by one partner, consumed by at least one other, cited into durable artifacts, and revised over time with consequences for its consumers. This file defines the class — its home, its schema, how it revises, and how its consumers hear about a change. Read it before writing or revising any spec.

## What a spec is (and is not)

The word "spec" is overloaded; this convention defines its meaning precisely. A spec is **not**:

- **A handoff pointer** — a dispatch line that closes on pickup (transient; `vlt-dispatch`'s routing record).
- **A handoff doc** — a one-shot payload in `_agent/handoffs/`, written for a single pickup. A doc that *outlives sittings, crosses a partner boundary, and revises over time* has outgrown the handoff class — it is a spec and belongs in `{specs}`.
- **A wiki note** — knowledge with sources and trust grades, governed by `wiki-supersession.md`. A spec is a contract with an owner and consumers, not knowledge.
- **BMad's SPEC kernel** (`bmad-spec`) — a host-tooling artifact for distilling intent into build contracts; unrelated to this class.

Example: the researcher maintains a sourcing-criteria contract the librarian files by — durable, owned, versioned, consumed: a spec. The librarian pointing the creative at one finished research note is a handoff.

## Home

Specs live in `{specs}` (default `_agent/specs/`) — the agent zone, upgrade-durable by construction. The directory is created **lazily on the first spec** (like `capabilities/` — no eager scaffold). Suggested filename shape: `{specs}/{date}-{owner}-to-{consumer}-{slug}.md` (e.g. `_agent/specs/2026-07-06-researcher-to-librarian-sourcing-criteria.md`).

## Frontmatter schema (spec artifacts)

- `type: spec`
- `title`
- `owner` — the authoring partner's slug (e.g. `researcher`)
- `consumers` — the list of **partner slugs** that consume this spec
- `version` — integer; bump **only** on changes to targets/constraints/rules — never for typos or prose polish
- `supersedes` — path of the prior spec (structural rewrites only; omit otherwise)
- `status` — `active` | `superseded`
- `created`, `last_updated`

## The two `consumers:` semantics

The same key appears on two artifact classes with different meanings — this convention owns the disambiguation:

- On a **convention file** (like this one), `consumers:` lists **skills**, each acknowledging via its flat `depends_on: ["name@version"]` — the existing convention handshake (see `vlt-mint`, *Edit a convention*).
- On a **spec artifact**, `consumers:` lists **partners**, notified via dispatch relay (below).

Same key, different registries. Don't conflate them.

## Supersession rules

- **Parameter change** (targets, constraints, or rules adjusted; the contract's identity intact) → revise **in place at the stable path**: bump `version`, update `last_updated`, and append an entry to a **"What changed"** changelog section in the body. The stable path is load-bearing — it preserves relay's doc-path idempotency, and an un-drained open pointer auto-tracks the freshest content.
- **Structural rewrite** (the contract is reconceived) → a **new file** carrying `supersedes:` pointing back at the old path; set the old spec's `status: superseded`. Never silent — the same visibility principle as `wiki-supersession.md`.

## Notification — push-MUST + pull-SHOULD

Notification is procedural, bound to existing write paths — there is no watcher, and this convention promises none.

- **Push (MUST):** on a `version` bump, the authoring partner fires `vlt-dispatch relay (to-slug, gist, spec-path)` **once per listed consumer, in the same session as the bump**. This is the relay-when-done reflex (`vlt-dispatch`, its single home) applied to specs.
- **Pull (SHOULD):** a consumer citing a spec re-checks its `version` against the last version it consumed, and drains any open pointer before relying on remembered terms.

A redundant pair by design: push survives a consumer that never runs; pull survives an author that forgets.

## Mint-time consumer lock

Any mint or capability change that makes a partner consume an existing spec **MUST add that partner to the spec's `consumers:` in the same change** (and `_agent/mint/decision-log.md` records it — see `vlt-mint`, Step 3). This is the anti-fork mechanism, placed at the only moment a new consumer can appear: consumer registration is never deferred to goodwill or memory.

## Enforcement

Stage and deferral are declared in this file's own frontmatter, per `frontmatter.md` *Enforcement declaration* — `declared`, with a tripwired deferral. Until the deferred machinery lands, the rules above are checked by inspection at mint and dispatch time. The deferred machinery is two `vlt-lint` checks — `spec_schema_violation` (a `{specs}` artifact missing required fields, or a `version` bump without its "What changed" entry) and `spec_notification_missing` (a `version` bump with no matching relay entries in the dispatch record). Escalation trigger, pre-agreed: a spec `version` bump ever shipping without its relay entries promotes the lint checks from scheduled follow-on to next-mint priority. When they land, `vlt-lint` joins this file's `consumers:`.

## Reading list

- `vault-operating-contract.md` — the handoff timings this class completes (synchronous payload / durable handoff doc / spec)
- `wiki-supersession.md` — the never-silent supersession principle, and the `version`/`consumers` handshake pattern this convention strengthens
- `frontmatter.md` — the general frontmatter standard (spec artifacts carry the schema above, not the note schema)
