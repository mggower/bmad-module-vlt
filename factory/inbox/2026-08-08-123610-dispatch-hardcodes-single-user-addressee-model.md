# `vlt-dispatch` hardcodes a single-user addressee model — a team vault can't route handoffs to another human without editing module source

_Filed 2026-08-08 from a **new team-vault install** (shared vault, multiple humans; not vlt-core),
via a factory problem-solving session. Classification: **design gap**. Not a defect — the module
behaves exactly as designed; the design assumes a vault population the team vault doesn't have._

## The claim

The team vault needed handoffs filed into **another user's inbox** — same dispatch mechanics
(surface-and-point, routing record, relay idempotency), different destination. There is no
sanctioned way to give `vlt-dispatch` that destination:

- Its addressee/inbox model is fixed in module-owned prose: `daily/`, `_agent/dispatch.md`,
  `_agent/handoffs/`, `{specs}` are the four hardcoded locations, and the `vault_structure`
  logical names it resolves are `log`, `backlog`, `conventions`, `archive` only
  (`skills/vlt-dispatch/SKILL.md:30-44`). No roster, no per-user inboxes.
- It has **none** of the module's three durable-extension seams: no convention-overlay read
  (zero `overlay` hits under `skills/vlt-dispatch/`; vlt-ingest/extract/track all state the
  base+overlay merge read), no agent-zone behavior-file read (the way partners read
  `capabilities/` and `vlt-track` reads Loop profiles), and no `customize.toml` surface (only
  `vlt-agent-*` carry one, declared metadata-only).
- The module states the boundary itself: *"skills have no overlay mechanism, so a local skill
  edit is the user's to re-apply"* (`skills/vlt-upgrade/SKILL.md:48`). A hand-edit becomes a
  `skill_asset_divergence` the user re-applies every upgrade — a treadmill, not a home.

**Workaround in place:** a standalone minted capability handles the cross-user filing. It is
sanctioned and upgrade-durable (B1 preserve path), but it lives *outside* dispatch's single
routing record — dispatch-shaped behavior accumulating beside dispatch, against the "one record,
four modes" design.

## Root cause (from the factory session, grounded 2026-08-08)

The gap is not a missing overlay feature. `vlt-dispatch` **welds vault-population policy into
module-owned mechanism**: the four modes, two-writer status discipline, and relay idempotency are
mechanism (correctly frozen); the addressee model — one human, three partners, one inbox
topology — is policy that was a constant in every single-user vault and became a variable the
moment a second human existed. The team vault doesn't want dispatch to do a different thing; it
wants the same thing to more destinations.

The module already shipped the right pattern once: `vlt-track` reads a per-partner Loop profile
from the invoking partner's `capabilities/track.md` and "hardcodes none of it"
(`skills/vlt-track/SKILL.md:16, 31-40`; mint side `skills/vlt-mint/SKILL.md:55, 129`). That is a
**designed parameter read** — vault-local data a module skill is built to consume — and it
extends per-vault with zero source divergence. Dispatch simply was never given one.

Full diagnosis, decision matrix, and rejected alternatives (generic skill overlays,
`customize.toml` on op skills, dispatch-v2 rewrite, permanent-workaround) are in the factory
session artifact `_output/problem-solution-2026-08-08.md`; the matrix's losing shapes lost on
invariants — text/behavior overrides of module skills are the silent-fork pattern the SHA
manifest and single-home discipline exist to refuse.

## Why it matters

1. **Team vaults are a real deployment context now**, and this is the first structural need they
   generate. Every op skill carrying population assumptions (dispatch's addressees; consult's
   partner roster; ledger's grouping) will regenerate this pressure as shared vaults multiply.
2. **The workaround cost compounds silently.** Standalone mints absorb each instance well enough
   that nothing forces the question — while dispatch-adjacent behavior fragments across minted
   skills, each with its own record habits, dissolving the single-routing-record design at the
   edges.
3. **The alternative failure is worse.** If the answer ever becomes "just edit the skill," the
   upgrade honesty surface degrades into a re-apply treadmill, and lint can no longer reason
   about field behavior. The gap deserves a designed answer before either drift wins.

## What I'd want

- **Not** a generic skill-overlay/extension mechanism — the session evaluated it and the
  existing veto (`vlt-upgrade/SKILL.md:48`) should stand.
- **A designed routing-profile read for dispatch**, on the vlt-track precedent: a vault-local
  profile declaring the human roster, per-user inbox destinations, and relay/daily addressing
  rules; `daily` and `relay` consult it on entry; homed where upgrades never write
  (overlays dir or agent zone — owner's ruling). **Absent profile ⇒ byte-identical current
  behavior**, so single-user vaults (vlt-core) notice nothing.
- Rule-like vocabulary (e.g. addressee facets on the record), if any emerges, homed in a
  **convention** rather than the profile — so the existing overlay seam covers it.
- A one-paragraph statement in the operating contract of the general answer — *designed
  parameter reads yes, skill-text overlays no, new behavior mints* — so the next "can I overlay
  skill X?" has a standing answer. (Or hold this until a second op skill hits the same gap;
  owner's call at ideation.)
- Lint coverage for profile shape (dangling destinations reported, malformed profile loud not
  silent), so the profile joins the checked surface rather than becoming un-linted behavior.

## Open ideation questions for the owner

(a) profile home: `{overlays}/`-adjacent vs agent zone; (b) one vault-wide profile vs
per-partner `capabilities/dispatch.md` files; (c) v1 parameter scope (roster + inbox
destinations + relay addressing — more?); (d) which vocabulary, if any, belongs in a convention
instead; (e) state the generalized designed-read pattern in the contract now, or wait for a
second instance.
