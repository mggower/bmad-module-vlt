---
name: vlt-dispatch
depends_on: ["consult@1", "spec@2", "frontmatter@7"]
description: The vault's partner communication bus — one routing record with a drain, four modes. `daily` scans the human capture stream (daily/) and routes each fragment to the domain partner it serves; `relay` appends a pre-addressed partner→partner pointer (a handoff doc, or a doc-less ask/answer); `consult` asks another partner a question synchronously and returns its attributed answer now; `ledger` is a read-only open-items board. Use when the user says 'dispatch my daily notes', 'triage today's memos', 'route my captures', 'what's still open across the team', when a partner hands off a doc to another partner, or when a partner needs another partner's domain to finish its current move. A bare call lists the modes and asks which to run. Writes open, checkable pointers each partner drains; reads daily/ only in `daily` mode; never edits a daily note; never auto-ingests into the wiki.
---

# vlt-dispatch

## Overview

vlt-dispatch is the **vault's partner communication bus** — the one place a message gets a checkable home and reaches the partner it's for. It is **one record with a drain** (`_agent/dispatch.md`) read through **four modes**:

- **`daily`** — scan the human capture stream (`daily/`), *segment + classify + route* each fragment to the domain partner whose lane it serves. The hard part is *finding* the destination. *(This is the original "daily-note router," now named.)*
- **`relay`** — a partner hands over a *pre-addressed* pointer to another partner (a durable handoff doc is waiting — or a doc-less `ask`/`answer`; the shape facet, `references/relay.md`). The destination arrives **known**, so classification is skipped — dispatch just appends the pointer with keyed idempotency (see the mode reference).
- **`consult`** — a partner asks another partner a question **synchronously**, mid-turn, and gets that partner's own attributed answer back **now**. Nothing transfers: the caller keeps the wheel. *(A consult is a `relay` whose drain happens immediately, in-process, with the answer returned to the caller instead of left on the board.)*
- **`ledger`** — read-only: grep the whole record for still-open items, grouped by partner, across both human and relay traffic. The standing signal of what's waiting.

All four modes are **the same machine**: every mode emits the **identical pointer line** (`- [ ] \`slug\` Partner — gist → [[link]]`) into the **identical record**, drained by the **identical grep-and-check loop** (The pickup loop, below). The drain is **source-agnostic** — it does not care whether a pointer came from a daily note or another partner. That is the whole design: one drain, many intakes. *(`consult` emits the same line into the same record, but writes it already **checked** — it never waited, so there is nothing to drain. It is traffic, not a queue item.)*

It is a **surface-and-point** bus, never an ingest: it writes only the routing record in the agent zone, **never edits a daily note**, and **never promotes anything into the wiki** — graduation stays the human's and the receiving partner's deliberate call. The Librarian owns it (it is vault-routing, the same family as ingest and lint). It does **no web access**.

**Why a record, not an inbox.** The pain is *unprocessed accumulation*. Per-partner inbox queues would only redistribute the pile and rot the same way unless drained. `_agent/dispatch.md` is a **log with a drain, not a queue** — it is *supposed* to accumulate; a mode-appropriate idempotency key makes re-runs safe (a per-source **watermark** for `daily`; the **pointer's key** for `relay` — the handoff-doc path, or the `ask`/`answer` `ref`; the key rule's single home is `references/relay.md`), and each pointer carries an **open/picked-up status** so the log self-reports what is still waiting. Partners *pull* their slice (grep their slug for open items) and **check off their own items as they act**; the Librarian never *pushes* into another partner's private memory (`identity.md`/`thread.md` are per-partner and off-limits). **Two writers, cleanly separated:** dispatch creates blocks and writes every item open; the receiving partner owns the status of its own tagged lines and flips them. Dispatch never flips a status; a partner never edits another partner's line or another run's block.

**Single-writer holds even for relay.** A publishing partner never writes `_agent/dispatch.md` directly — it **invokes dispatch in `relay` mode** (the Librarian's op), which appends on its behalf. The Librarian remains the sole author of the record; the publisher supplies the addressing, dispatch is the scribe.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it, then ask for a vault root to proceed.

The vault is this project — resolve every path relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). The logical names this operation uses, with their defaults:

- `log` → `_agent/log.md`
- `backlog` → `_agent/backlog.md`
- `conventions` → `_meta/conventions/`
- `archive` → `_archive/`

Plus four more locations (the first three are **not in the structure map** — the agent zone is the partners' to organize; see the operating contract):

- **the human capture zone** → `daily/` (Obsidian Daily Notes, `YYYY-MM-DD.md`) — **human-owned, read-only**; touched by the `daily` mode **only**.
- **the routing record** → `_agent/dispatch.md` (this operation's own agent-zone artifact; created on first run).
- **the handoff zone** → `_agent/handoffs/` (durable partner→partner handoff docs; the `relay` mode points at these, never authors them).
- **the spec zone** → `{specs}` (default `_agent/specs/`) — durable, owned, **versioned** cross-partner contracts, governed by `{conventions}/spec.md`; `relay` points at these too, never authors them.

The **active partner** for the log tag is the **Librarian**.

**The human-zone boundary is load-bearing — do not cross it.** `daily/` is human territory (operating contract § human zones). Only the **`daily`** mode may read it, and only because the user explicitly invoked dispatch — that invocation *is* the "read on request" the contract permits. **`relay` and `ledger` never touch `daily/` at all** (relay is pure append+dedup in the agent zone; ledger is a read of the record). Within any mode you therefore: **never write to, edit, reorganize, or tidy any file in `daily/`**; **never auto-ingest** a daily fragment into the wiki; and **never run unprompted** — there is no background sweep, dispatch fires only when summoned (by the human, or by a partner invoking `relay`).

Daily memos are personal human capture, not curated sources — so scan a fragment for secrets before writing its pointer, and if a fragment contains a credential, route a redacted gist (never the secret) or skip it and say so. The same secret-hygiene applies to a relay gist.

## Mode dispatch

Resolve the mode **first**, before any other work:

- **An explicit subcommand** names the mode: `daily` / `relay` / `consult` / `ledger` (e.g. `/vlt-dispatch daily`, `/vlt-dispatch relay …`, `/vlt-dispatch consult …`, `/vlt-dispatch ledger`). A partner firing a handoff calls `relay` with its arguments; a partner needing another's domain mid-turn calls `consult` with its own. Natural-language requests resolve the same way — "dispatch my daily notes" / "route my captures" → `daily`; "what's still open" / "show the board" → `ledger`; a partner-supplied `(to-slug, gist, handoff-path)` → `relay` (plus `shape`/`ref` where the payload is an ask or answer); a partner-supplied `(to-slug, question, groundIn, why)` → `consult`.
- **A bare invocation** (`/vlt-dispatch` with no mode and no relay payload) does **not** silently default to `daily`. List the available modes and ask which to run:

  > vlt-dispatch is the partner communication bus. Which mode?
  > - **daily** — scan your daily notes and route them to the team.
  > - **relay** — append a partner→partner handoff pointer *(usually fired automatically by a partner; runnable here for debugging)*.
  > - **consult** — ask another partner a question and get an attributed answer back now *(usually fired by a partner mid-turn)*.
  > - **ledger** — show the standing board of everything still open, plus tripped wires.

  The mode menu is the home, not a hidden default — most discoverable as modes grow. (This is a deliberate reframe: dispatch is no longer "the daily-note router that sometimes does other things"; it is a bus whose first question is *which channel*.)

Once the mode is known, **read its reference file and run it** — `references/daily.md` / `references/relay.md` / `references/consult.md` / `references/ledger.md`. The rule has no exceptions: **every mode reads its reference on entry**, `ledger` included (uniformity is the rule, not size). Each reference carries the mode's mechanics, its `{log}` line shape, and its Verify checklist; each mode writes its own `{log}` line (see Log) and ends in its own report, verified against that checklist.

---

## The pickup loop (how a partner drains its slice)

The other half of the bus — documented **here as the single home for the protocol**, so any partner follows the same drain regardless of which mode wrote the item. **Source-agnostic: a daily-routed pointer and a relayed pointer drain identically.** Dispatch writes open items; the **receiving partner**, on its own activation, drains them:

1. **Find your open items** — grep your own slug for unchecked boxes across the whole record:
   `grep -nF '[ ] \`researcher\`' _agent/dispatch.md` (substitute your slug). This is a *pull*: a partner reads the shared record, never the human's `daily/` directly unless it chooses to follow a `[[daily/…]]` link. A relayed item carries a `[[_agent/handoffs/…]]` link instead — follow it to the full handoff doc.
2. **Act on each** in your own voice and your own memory — fold it into your `thread.md`/working record, start a protocol, answer it, whatever your domain calls for. Dispatch did not do this for you; the gist is only a pointer.
3. **Check it off** — flip that one line `- [ ]` → `- [x]` and stamp it: append ` ✓ picked up YYYY-MM-DD`. You edit **only your own tagged lines**; never another partner's line, never a run header, never another run's block. A checked item stays in the log as history — the loop is "drained," not "deleted."

Because items are checked in place and dispatch only ever *appends* fresh blocks, the two writers never collide: dispatch owns block creation, each partner owns the status of its own lines. A partner that re-greps later sees its checked items as done and only acts on what's still open.

## Log

Every mode except `ledger` appends **one partner-tagged entry** to `{log}` in the operating-contract format (the `dispatch` log type; the contract's type set is non-exhaustive — this op owns `dispatch`). The exact line shape is per-mode and lives in each mode's reference. `ledger` is read-only — it writes **no** `{log}` entry (nothing changed). Write **no** session note in any mode — the summoning partner (the Librarian, or the publishing partner on a relay) owns the single session note for the sitting (operating contract § session-ownership).
