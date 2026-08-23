---
date: 2026-06-15
slug: vlt-dispatch-partner-communication-bus
target: vlt module (bmad-module-vault)
kind: skill + convention change-analysis (for next module version)
status: applied in the vlt-core install; mirror into module source
---

# vlt-dispatch → the partner communication bus (daily / relay / ledger)

## Problem statement + evidence

`vlt-dispatch` shipped as a **daily-note router**: read `daily/`, classify each fragment to a domain partner, write open checkable pointers into `_agent/dispatch.md`, each partner greps its slug and checks off. That solved human-capture → partner.

It did **not** solve **partner → partner**. Evidence from the live vlt-core vault: a rich handoff doc existed at `_agent/handoffs/2026-06-13-health-coach-to-chef-nutrition-spec.md` (the Health Coach's nutrition spec for the Chef) with **no pointer anywhere telling the Chef it was waiting**. The handoff had no pickup path. Partners had a contract-level *synchronous* handoff (typed payload, same sitting) but no *asynchronous/durable* one.

**Core insight (validated in a brainstorm):** dispatch's drain mechanism — open pointer + slug-grep + check-off — is **source-agnostic**. It doesn't care whether the pointer came from a daily note or another partner. So the fix is to **generalize the existing record into a multi-intake bus**, not to build a second mechanism.

## The decision and rationale

`vlt-dispatch` becomes the **vault's partner communication bus**: **one record (`_agent/dispatch.md`), one drain, three modes.**

- **`daily`** — the original scan/classify/route, now behind an explicit subcommand. Only this mode reads `daily/` (the human-zone boundary tightens — relay/ledger never touch `daily/`).
- **`relay`** — NEW. A publishing partner supplies a **pre-addressed** `(to-slug, gist, handoff-path)`; dispatch appends a `relay: A → B` pointer. Destination arrives **known**, so classification is skipped. **Thin scribe, not gatekeeper** — no content judgment (YAGNI; mirrors the `unrouted` retirement: don't add gatekeeping until pollution is real).
- **`ledger`** — NEW. Read-only open board (grep the whole record for open items, grouped by partner, across daily + relay). Promoted from the inline standing-ledger report into its own callable mode.
- **Bare invocation** → lists the three modes and asks which (the mode menu is the home, not a silent default).

**Why generalize, not fork:** every mode emits the *identical pointer line* into the *identical record*, drained by the *identical pickup loop*. A relayed item is indistinguishable from a daily-routed one once in a partner's slice — which is the whole point. The header shape (`relay: A → B` vs `daily/… (routed through line N)`) **is the mode signal** and selects the idempotency rule.

**Single-writer preserved:** the publishing partner never writes `_agent/dispatch.md`; it invokes the Librarian's `relay` op, which writes on its behalf. Librarian stays sole author of the record.

### Relay idempotency — keyed on `(handoff-doc-path, recipient-slug)`

- no pointer for the pair → append fresh open pointer (first relay)
- an **open** pointer exists → **no-op** (kills #1 spam: a partner re-relaying the same doc each awakening)
- latest pointer is **checked off** → re-relay = new info (a revised spec) → append fresh open pointer (handles #2 stale-spec)

This forces a **handoff lifecycle rule**: durable handoffs are **updated in place at a stable path**, not versioned into new files. An un-drained open pointer then auto-tracks the freshest content; a stable path also blunts #3 dangling-link.

### Failure modes (reverse-brainstorm) and what we did with each

| # | Failure | Disposition |
|---|---------|-------------|
| 1 | Spam (re-relay each awakening → dup pointers) | **Solved now** — open-pointer no-op |
| 2 | Stale spec (revise provisional → old pointer wrong) | **Solved now** — re-relay after check-off + in-place edit |
| 3 | Dangling link (doc moved/rewritten) | **Deferred** ("log when it bites"); stable-path blunts it |
| 4 | Phantom recipient (relay to retired slug → orphan) | **Light check now** (recipient must match a live `vlt-agent-{slug}`, else stop — no orphan written); full treatment deferred |

The defer-until-it-bites discipline is the same one that retired `unrouted`.

### Three open seams settled with the user (AskUserQuestion at mint time)

1. **Relay-when-done reflex → shared hand**, not per-skill copy-paste. Single home = `relay` mode (mechanics) + the operating contract's hand-offs section (the cross-cutting reflex). Partners *name* it and point at it.
2. **Ledger → keep inline in `daily` AND add the `ledger` mode** (same board, two surfaces).
3. **Manual relay → keep reachable** for debugging; partner-fired-automatic is the normal path.

## Exact changes to ship in the module-side artifacts

1. **`skills/vlt-dispatch/SKILL.md`** — replace wholesale with the bus version. Structure:
   - Frontmatter `description` rewritten (three modes; "reads daily/ only in `daily` mode").
   - Overview: "the vault's partner communication bus — one record, one drain, three modes"; source-agnostic drain; single-writer-holds-for-relay paragraph.
   - On Activation: add the **handoff zone** `_agent/handoffs/` to the not-in-structure-map locations; state daily/ is touched by `daily` mode **only**.
   - New **Mode dispatch** section (explicit subcommand vs bare→menu).
   - **`daily` mode** section = the prior Step 0/Classify/Write/Report content verbatim in substance, now nested under the mode; Step 3 ends by printing the `ledger` read inline.
   - **`relay` mode** section: who-fires + the relay-when-done reflex (full text, this is its single home); inputs/validation (incl. light liveness); the `(doc-path, recipient-slug)` idempotency rule; the stable-path lifecycle note (points at the contract as owner); the `relay: A → B` block format; brief report.
   - **`ledger` mode** section: read-only board build steps.
   - **Pickup loop** reframed source-agnostic (a relayed item carries a `[[_agent/handoffs/…]]` link).
   - **Log**: per-mode `{log}` lines; `ledger` writes none.
   - **Verify**: split per mode.
   - File-header blurb (`# Dispatch` _…_) rewritten for three modes / two idempotency keys.

2. **`_meta/vault-operating-contract.md` § Sessions, sittings, and hand-offs** — add after the "Role boundary at the seam" paragraph:
   - **Two handoff timings** — synchronous typed payload (existing) vs **durable doc** in `_agent/handoffs/`.
   - **The relay-when-done reflex** (named here, mechanics owned by `vlt-dispatch`'s `relay` mode — single-home, not restated).
   - **Durable handoffs updated in place at a stable path** (the lifecycle rule relay's idempotency depends on).

3. **Partner skills** — one concise pointer each, only where a partner produces/consumes a durable handoff:
   - `skills/vlt-agent-health-coach/SKILL.md` (in "Handing knowledge…"): fire the relay reflex after writing the nutrition-spec doc; revise in place.
   - `skills/vlt-agent-chef/SKILL.md` (in "The spec→menu handoff"): the durable spec arrives as an open pointer in its dispatch slice (ordinary pickup loop).
   - *Note for the maintainer:* these two are the only partners with a live durable-handoff relationship today. If the module ships more such relationships, add the same one-liner to each producing partner — but resist baking it into all partners by default (the contract carries the cross-cutting rule; per-partner is just a pointer where a real handoff exists).

4. **`module-help.csv` (both the module copy and the install mirror)** — retitle the dispatch row "The Partner Communication Bus"; rewrite the description for the three modes and the scope column to `{mode: daily | relay | ledger; bare call → menu}`. Keep live + `vlt-setup/assets/module-help.csv` identical.

## Upgrade / migration path for existing installs

- **Skill/contract/partner edits are idempotent text replacements** — a reinstall that ships the bus version simply overwrites the daily-only router. No state migration.
- **Existing `_agent/dispatch.md` records are forward-compatible**: all prior blocks are `daily/…` blocks; the `daily`-mode watermark logic reads them unchanged. `relay`/`ledger` only add new block shapes / read the existing ones. **No record rewrite needed.**
- **One-time, optional (data not skill):** any handoff docs already sitting in `_agent/handoffs/` without a pointer can be relayed live whenever the producing partner next sits (or by a manual `/vlt-dispatch relay …`). In vlt-core that's the single Health Coach→Chef spec.
- **`daily` idempotency for old installs:** unchanged — the watermark header format is preserved exactly.

## Latent bugs surfaced

- **CSV quoting drift:** in the vlt-core install, the *live* `module-help.csv` had the dispatch scope column **unquoted despite containing a comma** (`{scope: since last dispatch (default, all notes) | …}`), while the `vlt-setup` mirror had it quoted. A strict CSV parser would mis-split the live row. The new rows quote the scope column in both copies — **the module should audit every row for embedded commas in unquoted fields.**

## Open design questions to decide module-wide

- **Relay liveness depth:** we ship only the cheap check (recipient slug must be a live partner). Should #4 (a recipient retired *after* a pointer is written → orphan in the ledger) get a `ledger`-mode sweep that flags pointers whose slug no longer resolves? Deferred for now.
- **Relay across more partner pairs:** as the roster grows, is a shared *workflow* (one fan-out that relays a batch of handoffs) warranted, or does the per-handoff reflex stay sufficient? (Parallels the open `vlt-dispatch` daily-fan-out backlog item, but for relay.)
- **Ledger as the canonical board:** now that `ledger` exists as its own mode, should the `daily`-mode inline print eventually be *replaced* by a pointer to `ledger` (we kept both per the user's call), or stay duplicated? Revisit if the inline copy drifts from the mode.
