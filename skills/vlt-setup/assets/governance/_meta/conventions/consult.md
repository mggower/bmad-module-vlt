---
type: note
created: 2026-07-26
last_updated: 2026-07-26
title: Consult Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 1
consumers: [vlt-dispatch, vlt-lint]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
adoption_first_instance: null        # no first live instance yet — declared, not yet adopted
---

# Consult Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/consult.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

A **consult** is a *synchronous, depth-1, cross-partner question* in which the summoned partner answers **as itself** and remembers that it did. This file defines the class — what it is, when it is earned, and the one precondition it imposes on durable artifacts. Read it before writing a spec that binds a partner other than its owner.

## What a consult is (and is not)

A consult transfers **nothing**. The caller keeps the wheel and gets an attributed answer back. Its three neighbours in the vault differ by what moves:

- **A relay** routes and waits — the answer lands on the board later, drained by the recipient on its own next orient (`vlt-dispatch`, its `relay` mode).
- **A hand-off** transfers the work *and the wheel* — it ends one sitting and begins another (`vault-operating-contract.md`, *Sessions, sittings, and hand-offs*).
- **A council** is fixed lenses applied in parallel with no cross-talk, returning a *verdict* — not a partner (`vlt-review-council`).

A consult is none of these: the work does not move, the wheel does not move, and what comes back is a named partner's answer in its own voice. The summoned partner answers from a **lite boot**, not a full activation (mechanics at `vlt-dispatch`, *Mode: consult*).

## When a consult is earned

The trigger rule is **not restated here** — it is single-homed at `vault-operating-contract.md`, *Read-and-cite is the documented default*, and its test is memory. Read it there. Read-and-cite remains the documented default; a consult is the exception that must earn itself against that test.

## The precondition — a spec that binds another partner requires a consult

A `{specs}` artifact whose `consumers:` name a partner other than its `owner` — a contract one partner writes to bind another's domain — **requires a consult record for each such consumer before it is filed.**

A spec written to bind another partner's domain without ever asking that partner is exactly the manufactured authority the operating contract forbids (*Authority boundary at the seam — a partner never speaks in another partner's voice*), in durable form. The prohibition there governs a sentence; this governs a contract, which outlives the sitting that wrote it.

## What a consult record is

A dated `consult:` block in `_agent/dispatch.md` naming `(from-slug, to-slug)`, the artifact path the consult grounded in, and the typed return.

The record is **derived, never stored**: no frontmatter key on the spec, no `consulted:` field, no counter. How the block is written — its header shape, its pointer line, its pre-checked status — is `vlt-dispatch`'s single home; read the mechanics there.

## The honest limit, stated in the rule itself

The precondition is bounded to `{specs}`. A partner claiming another's domain in an ordinary wiki page, research note, or session note is **invisible to this rule and to its check by construction** — those artifacts carry no machine-readable authority axis to derive from, where a spec carries `owner` and `consumers` (`spec.md`, *Frontmatter schema*). This rule reduces the class; it does not close it.

## Enforcement

Stage and owner are declared in this file's own frontmatter, per `frontmatter.md` *Enforcement declaration* — `checked`, by `vlt-lint`, at every lint run. The check derives **two states** from the records that already exist: **presence** — for each `{specs}` artifact binding a partner other than its owner, `vlt-lint` confirms a `consult:` block in `_agent/dispatch.md` names that `(spec-path, consumer-slug)` pair, flagging the absence as `consult_missing` — and **precedence** — a consult block whose header timestamp is dated **after** the spec's `created:` reports `consult_retroactive`, its own state, not a failure: the precondition was honored late, and the report says so rather than reading presence as precedence. It reports the population it compared alongside the blind spot named above. It **never auto-fixes** — a missing consult is closed by *having the consult*, not by lint writing anything.

There is no deferral: the check exists, its owner is named, and its moment is named, all as of this convention's first version.

## Reading list

- `vault-operating-contract.md` — the authority boundary and the trigger rule this convention operationalizes
- `spec.md` — the artifact class the precondition applies to, and the `owner`/`consumers` axis it derives from
- `frontmatter.md` — the enforcement declaration this file's frontmatter follows
