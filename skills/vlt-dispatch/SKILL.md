---
name: vlt-dispatch
description: The vault's partner communication bus — one routing record with a drain, three modes. `daily` scans the human capture stream (daily/) and routes each fragment to the domain partner it serves; `relay` appends a pre-addressed partner→partner handoff pointer; `ledger` is a read-only open-items board. Use when the user says 'dispatch my daily notes', 'triage today's memos', 'route my captures', 'what's still open across the team', or when a partner hands off a doc to another partner. A bare call lists the modes and asks which to run. Writes open, checkable pointers each partner drains; reads daily/ only in `daily` mode; never edits a daily note; never auto-ingests into the wiki.
---

# vlt-dispatch

## Overview

vlt-dispatch is the **vault's partner communication bus** — the one place a message gets a checkable home and reaches the partner it's for. It is **one record with a drain** (`_agent/dispatch.md`) read through **three modes**:

- **`daily`** — scan the human capture stream (`daily/`), *segment + classify + route* each fragment to the domain partner whose lane it serves. The hard part is *finding* the destination. *(This is the original "daily-note router," now named.)*
- **`relay`** — a partner hands over a *pre-addressed* pointer to another partner (a durable handoff doc is waiting). The destination arrives **known**, so classification is skipped — dispatch just appends the pointer with doc-path idempotency.
- **`ledger`** — read-only: grep the whole record for still-open items, grouped by partner, across both human and relay traffic. The standing signal of what's waiting.

All three modes are **the same machine**: every mode emits the **identical pointer line** (`- [ ] \`slug\` Partner — gist → [[link]]`) into the **identical record**, drained by the **identical grep-and-check loop** (The pickup loop, below). The drain is **source-agnostic** — it does not care whether a pointer came from a daily note or another partner. That is the whole design: one drain, many intakes.

It is a **surface-and-point** bus, never an ingest: it writes only the routing record in the agent zone, **never edits a daily note**, and **never promotes anything into the wiki** — graduation stays the human's and the receiving partner's deliberate call. The Librarian owns it (it is vault-routing, the same family as ingest and lint). It does **no web access**.

**Why a record, not an inbox.** The pain is *unprocessed accumulation*. Per-partner inbox queues would only redistribute the pile and rot the same way unless drained. `_agent/dispatch.md` is a **log with a drain, not a queue** — it is *supposed* to accumulate; a mode-appropriate idempotency key makes re-runs safe (a per-source **watermark** for `daily`, the **handoff-doc path** for `relay`), and each pointer carries an **open/picked-up status** so the log self-reports what is still waiting. Partners *pull* their slice (grep their slug for open items) and **check off their own items as they act**; the Librarian never *pushes* into another partner's private memory (`identity.md`/`thread.md` are per-partner and off-limits). **Two writers, cleanly separated:** dispatch creates blocks and writes every item open; the receiving partner owns the status of its own tagged lines and flips them. Dispatch never flips a status; a partner never edits another partner's line or another run's block.

**Single-writer holds even for relay.** A publishing partner never writes `_agent/dispatch.md` directly — it **invokes dispatch in `relay` mode** (the Librarian's op), which appends on its behalf. The Librarian remains the sole author of the record; the publisher supplies the addressing, dispatch is the scribe.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it, then ask for a vault root to proceed.

The vault is this project — resolve every path relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). The logical names this operation uses, with their defaults:

- `log` → `_agent/log.md`
- `backlog` → `_agent/backlog.md`
- `conventions` → `_meta/conventions/`
- `archive` → `_archive/`

Plus three locations **not in the structure map** (the agent zone is the partners' to organize — see the operating contract):

- **the human capture zone** → `daily/` (Obsidian Daily Notes, `YYYY-MM-DD.md`) — **human-owned, read-only**; touched by the `daily` mode **only**.
- **the routing record** → `_agent/dispatch.md` (this operation's own agent-zone artifact; created on first run).
- **the handoff zone** → `_agent/handoffs/` (durable partner→partner handoff docs; the `relay` mode points at these, never authors them).

The **active partner** for the log tag is the **Librarian**.

**The human-zone boundary is load-bearing — do not cross it.** `daily/` is human territory (operating contract § human zones). Only the **`daily`** mode may read it, and only because the user explicitly invoked dispatch — that invocation *is* the "read on request" the contract permits. **`relay` and `ledger` never touch `daily/` at all** (relay is pure append+dedup in the agent zone; ledger is a read of the record). Within any mode you therefore: **never write to, edit, reorganize, or tidy any file in `daily/`**; **never auto-ingest** a daily fragment into the wiki; and **never run unprompted** — there is no background sweep, dispatch fires only when summoned (by the human, or by a partner invoking `relay`).

Daily memos are personal human capture, not curated sources — so scan a fragment for secrets before writing its pointer, and if a fragment contains a credential, route a redacted gist (never the secret) or skip it and say so. The same secret-hygiene applies to a relay gist.

## Mode dispatch

Resolve the mode **first**, before any other work:

- **An explicit subcommand** names the mode: `daily` / `relay` / `ledger` (e.g. `/vlt-dispatch daily`, `/vlt-dispatch relay …`, `/vlt-dispatch ledger`). A partner firing a handoff calls `relay` with its arguments. Natural-language requests resolve the same way — "dispatch my daily notes" / "route my captures" → `daily`; "what's still open" / "show the board" → `ledger`; a partner-supplied `(to-slug, gist, handoff-path)` → `relay`.
- **A bare invocation** (`/vlt-dispatch` with no mode and no relay payload) does **not** silently default to `daily`. List the available modes and ask which to run:

  > vlt-dispatch is the partner communication bus. Which mode?
  > - **daily** — scan your daily notes and route them to the team.
  > - **relay** — append a partner→partner handoff pointer *(usually fired automatically by a partner; runnable here for debugging)*.
  > - **ledger** — show the standing board of everything still open.

  The mode menu is the home, not a hidden default — most discoverable as modes grow. (This is a deliberate reframe: dispatch is no longer "the daily-note router that sometimes does other things"; it is a bus whose first question is *which channel*.)

Once the mode is known, run the matching section below. Each mode writes its own `{log}` line (see Log) and ends in its own report.

---

## Mode: `daily` — scan the human capture stream

The original behavior, now named and behind an explicit subcommand. **Only this mode reads `daily/`.**

### Step 0: Determine scope

Like `vlt-lint`, pick one scope at the top of the run and announce it (with the file count, e.g. "Scoped dispatch — 3 daily notes with new content since last run"). The per-source **watermark** in `_agent/dispatch.md` is the baseline — read that file first, building `watermark[file]` = the `routed through line N` recorded in each file's most recent `daily/` run header (a never-dispatched note has watermark 0; relay blocks carry no watermark and are ignored here).

**Scoped (default)** — every daily note with content **beyond its watermark**. Glob `daily/*.md`, and for each compare current line count to `watermark[file]`; include every note with new lines (on the first scoped run, the entire backlog of never-dispatched notes; thereafter only what's been appended). Process only the lines beyond each note's watermark; a run with nothing new anywhere routes nothing (report "nothing new since the last dispatch").

**Full** — only when the user says "full dispatch" / "dispatch everything" / `--full`: re-route **every** `daily/*.md` from line 0, ignoring watermarks. Use after a format change or to rebuild the record. (Re-routing writes fresh open items; it does not resurrect items a partner already checked off in a prior block — those stay as their own historical blocks.)

**A named date or range** — "dispatch the 10th" / "this week's notes" / "today" → resolve to the matching `daily/YYYY-MM-DD.md` file(s) and process each beyond its watermark (or from line 0 if the user says "re-dispatch").

If a resolved note doesn't exist, say so plainly and skip it — don't invent content. If a daily note was edited *above* a watermark (rare — the human's prerogative), the line offset may be stale; if the content clearly doesn't line up, note it and offer a full re-dispatch of that file rather than guessing.

### Step 1: Classify against the live roster

Build the domain map from the **live roster**, not a hardcoded list — read the installed `vlt-agent-*` skills under `{project-root}/.claude/skills/` and use each partner's `description` to know which domain it serves (Researcher → open questions worth investigating; Creative → ideas worth making; Librarian → vault/knowledge-meta; plus any domain partners the roster has grown). Deriving the map live means dispatch stays correct as the roster grows — a newly minted partner's domain is routable the next run with no edit here.

**The routing slug is the skill basename minus `vlt-agent-`** — `vlt-agent-researcher` → `researcher`, `vlt-agent-creative` → `creative`, `vlt-agent-librarian` → `librarian`. This is the greppable key on every pointer line. Deriving it mechanically (not from a hand-chosen domain word) means a partner's grep is stable and exact, and a newly minted partner is routable with zero edits here — the slug *is* its identity. Pair it with the partner's human name (from its `description`) for legibility.

**Segment, then route.** Transcribed voice memos run together, so segment by **intent, not punctuation**: a fragment is one coherent thought/memo/ask, and a single `daily/` paragraph often holds two. Split on topic shifts; don't let a paragraph break decide a fragment for you. For each fragment:

- **One owner (common)** — assign the single partner whose domain it most serves → one pointer line with that slug.
- **A captured source or link → the Librarian.** A saved article, URL, or "read this" is *material*, not a question — it belongs to the Librarian's ingest queue (`librarian`), never the Researcher. Hold the line: the **Researcher** gets open *questions worth investigating*; the **Librarian** gets *sources and material to file*. A daily fragment that is just a saved link, or a "to-do: ingest X," routes to `librarian`.
- **Genuinely two domains** — a fragment that materially serves two partners is **cross-routed**: emit one pointer line per partner, each independently checkable, each gist framed for that partner. Don't over-split — only when each partner would actually act on it.
- **No owner → flag and skip (write no pointer).** A stray idea, reminder, shopping list, order, social observation, or to-do that fits no partner has **no home in the vault** — do **not** write it a pointer. A persistent no-owner pointer would sit open in the ledger forever, never drained — that accumulation is the very clutter dispatch exists to prevent. Instead, **surface it once in the run report** (Report → *Flagged and skipped*) and move on; nothing is written to `_agent/dispatch.md` for it.

### Step 2: Write the routing record

Append one **`daily` run block** per in-scope source to `_agent/dispatch.md` (create the file with the header below if absent). **Dispatch's only write is appending blocks with every item open** — it never flips a status. Format — a greppable run header (the **header shape is the mode signal**) plus one checkable pointer line per routed fragment:

```
## [YYYY-MM-DD HH:MM] daily/YYYY-MM-DD (routed through line N) — K item(s)
- [ ] `slug` Partner Name — one-line gist of the fragment, in the user's own framing → [[daily/YYYY-MM-DD]]
```

Only **owned** fragments get a pointer line. A no-owner fragment is flagged in the run report and written nowhere; the header's `K item(s)` counts only the pointers actually written.

Rules for the block:

- The **run header** carries the watermark: `routed through line N` = the source file's line count at this run (what the next run's watermark check reads). The `daily/…` shape *is* the mode signal — it tells the next `daily` run (and a human scanning) that this block uses watermark idempotency. It omits the `dispatch (librarian)` type/partner prefix — every line here would carry it, so it's pure boilerplate. (The `{log}` entry keeps `dispatch (librarian)` — that's a mixed stream where the tag is load-bearing.)
- Every pointer is a **checkbox written open (`- [ ]`)**. After the box comes the **routing slug in backticks** — the partner's skill basename minus `vlt-agent-` — the greppable key, followed by the human Partner Name. The backtick-wrapped slug makes a partner's grep exact and collision-free: `grep -nF '[ ] \`researcher\`' _agent/dispatch.md` returns only its open items. Every pointer carries a live partner slug — there is no domain-less pointer.
- The **gist** is a faithful one-line compression of the fragment in the user's framing — enough for the partner to know what's waiting and decide. It is a *pointer*, not an extraction: the `[[daily/…]]` wikilink sends the partner to the full memo. Do not interpret, grade, or fold the memo into anything here — that is the receiving partner's job (and preserves the personalization firewall).
- A **cross-routed** fragment gets one pointer line per partner (each its own checkbox).
- If multiple daily notes are in scope, write one run block per source file.

The file's header (written once, on creation):

```
# Dispatch

_The vault's partner communication bus — one routing record with a drain, read through three modes. `daily` routes human daily-note captures to the partner whose domain they serve; `relay` appends pre-addressed partner→partner handoff pointers; `ledger` is the read-only open-items board. Every pointer is written open (`- [ ]`); a partner greps its `` `slug` `` for open items and checks off (`- [x]`) what it picks up. Never edits daily notes; never auto-ingests. Idempotency is per-source watermark for `daily`, handoff-doc path for `relay`; the open/picked-up status makes the backlog self-reporting._
```

`_agent/dispatch.md` is a log-style agent record (like `{log}`), not a "note" — it carries **no per-note frontmatter**.

### Step 3: Report (and print the standing ledger inline)

Lead with the **scope you ran** (scope + how many notes), then what was routed, grouped by partner, and **name who to summon** — `daily` mode ends at the routing record + this report; it does not summon partners or move fragments into anyone's working record. Example:

> Scoped dispatch — 3 daily notes with new content since the last run. Routed 4 open items:
> - **Researcher** (2) — a question on transformer attention; a thread to chase on context-window pricing.
> - **Librarian** (1) — a saved article to ingest.
> - **Creative** (1) — cross-routed: an idea worth making.
>
> Summon each partner to drain theirs (each greps its `` `slug` `` for open items and checks them off). Nothing was written into your daily notes or the wiki.

If there were no new fragments anywhere in scope, say "nothing new since the last dispatch."

**Flagged and skipped (no-owner fragments).** When a fragment had no partner home, list it here — a one-time surface so nothing is silently dropped — and say plainly it was **not** written to the record (it lives in the daily note; place it yourself if you want it somewhere). This is the *only* trace a no-owner fragment leaves. Example:

> **Flagged, not routed (2):** a personal reminder; a shopping list. No vault home — left in your daily note, nothing written to the record.

**Then print the standing open ledger inline** (not just this run's routes). A `daily` run is a natural moment to show the human the whole open backlog — so after routing, run the **`ledger` read** (below) and append it to the report. This inline ledger and the standalone `ledger` mode are the **same board**; `daily` prints it as the closing signal of a routing run, `ledger` serves it on demand without scanning `daily/`.

---

## Mode: `relay` — append a partner→partner handoff pointer

A publishing partner has written a **durable handoff doc** to `_agent/handoffs/` and needs the recipient to know it's waiting. `relay` is the seam that closes: it appends a **pre-addressed** open pointer into the recipient's slice. **No `daily/` read, no classification** — the address arrives known. Relay is a **thin scribe, not a gatekeeper**: it takes the publisher's `(slug, gist, handoff-path)` already decided and appends it without re-judging the content (YAGNI — no rigid gatekeeping until a real pollution problem appears).

### Who fires it, and the publish-side reflex (single home)

Relay is normally **fired automatically by the publishing partner** as the last step of writing a handoff doc — the **relay-when-done reflex**. This is the shared publish-side protocol, owned **here** as its single home (mirroring how the pickup loop is owned here for the drain side); a partner *names* the reflex and points at this mode, it does not restate the mechanics. The reflex, in full:

> **After writing (or revising) a handoff doc to `_agent/handoffs/`, the publishing partner invokes `vlt-dispatch relay (to-slug, gist, handoff-path)` as the final step of the write.** It supplies the recipient's slug, a one-line gist of what's waiting, and the stable path of the doc. It does **not** write `_agent/dispatch.md` itself — dispatch is the scribe (single-writer).

A human may also **invoke `relay` directly** for debugging or a manual handoff (`/vlt-dispatch relay <to-slug> "<gist>" <handoff-path>`, optionally `from <from-slug>`) — reachable, but not the advertised main path.

### Inputs and validation

Required: **`to-slug`** (the recipient's routing slug), **`gist`** (one-line, in the publisher's framing), **`handoff-path`** (the stable path under `_agent/handoffs/`). Optional: **`from-slug`** (the publisher; infer from the calling partner when fired as a reflex). Then:

- **Liveness (light).** Confirm `to-slug` matches a live `vlt-agent-{to-slug}` in `{project-root}/.claude/skills/`. If it doesn't, don't write a dangling pointer — say so and stop (a relay to a retired/typo'd slug is **failure mode #4**, phantom recipient; we surface it rather than parking an orphan). *(Deeper liveness checks stay deferred until they bite.)*
- **Secret hygiene.** Same as `daily` — never put a credential in the gist.
- **The handoff doc itself is the publisher's, not dispatch's** — relay points at it, never reads it for content, never edits it. Surface-and-point holds: the pointer carries a gist; the rich spec stays in `_agent/handoffs/`.

### The idempotency rule — keyed on `(handoff-doc-path, recipient-slug)`

Before appending, grep the record for an existing relay pointer with this **same `(handoff-path, to-slug)` pair** and apply:

- **No pointer exists** → append a fresh open pointer (first relay).
- **An *open* pointer exists** (`- [ ]`) → **no-op.** The recipient hasn't drained the prior notice yet; a second relay of the same doc is the **#1 spam** failure mode (a partner re-firing each awakening). Say "already open in `<to-slug>`'s slice — no-op" and write nothing.
- **The latest pointer is *checked off*** (`- [x]`) → the recipient already picked up the prior version and the publisher is relaying **again** = new information (a revised spec — **#2 stale-spec**). Append a **fresh open pointer** to re-notify.

This is **idempotency hygiene, not content judgment** — dispatch enforces "one open pointer per `(doc, recipient)`," nothing about whether the handoff is *good*. The scribe stays thin.

### The handoff lifecycle this rule assumes (stable path, updated in place)

The idempotency key is the doc path, so it only works if **handoffs are updated in place at a stable path, not versioned into new files.** A publisher revising a provisional spec edits the *same* `_agent/handoffs/…` doc; an un-drained open pointer then **auto-tracks the freshest content** (the recipient follows the link to whatever the doc now says), and a fresh pointer is only needed when the recipient had already checked the prior one off. A stable path also blunts **#3 dangling link**. *(This lifecycle rule is the cross-cutting half; its single home is the operating contract's hand-offs section — relay depends on it, but the contract owns it.)*

### Write the relay block

Append a **`relay` block** to `_agent/dispatch.md`. The header shape — `relay: <from> → <to>` — **is the mode signal** (vs `daily/…`), so a human scanning sees partner-traffic at a glance and the next run knows to apply doc-path (not watermark) idempotency:

```
## [YYYY-MM-DD HH:MM] relay: <from-slug> → <to-slug> — 1 item
- [ ] `to-slug` Partner Name — gist of what's waiting → [[_agent/handoffs/…]]
```

One relay = one pointer (a relay carries a single pre-addressed handoff). The pointer is the **same line format** every mode emits, so the recipient drains it with the **same** pickup loop — a relayed item is indistinguishable from a daily-routed one once in the slice, which is exactly the point.

### Report

Brief, since relay is usually a sub-step of a partner's handoff:

> Relayed to **Creative**: spec waiting at `_agent/handoffs/2026-06-13-…`. Open in the Creative's slice; it'll surface when the Creative next orients.

On a no-op (open pointer already present): "Creative already has an open pointer for this spec — nothing appended." On a phantom recipient: "No live partner `<to-slug>` — nothing written; check the slug."

---

## Mode: `ledger` — the read-only open board

A **read-only** view: grep the *whole* record for still-open items and group them by partner, across **both** daily and relay traffic. No write, no `daily/` read — pure report. This is the human's **standing signal**: a partner only drains its slice when next summoned, so an item routed to a rarely-summoned partner could sit open, unseen, indefinitely; `ledger` shows the full open backlog without summoning anyone.

Build it:

1. Count all open items: `grep -c '^- \[ \]' _agent/dispatch.md`.
2. Per live slug, count open: `grep -cF '[ ] \`<slug>\`' _agent/dispatch.md`, and find the oldest (the earliest run header above an open line).
3. Present grouped by partner, oldest-first signal:

> **Still open across the record:** Researcher 3 (oldest 2026-05-21) · Librarian 1 · Creative 2 *(1 relayed: a spec)*. Summon a partner to drain its column.

If everything is picked up, say "all routed items have been picked up — nothing open." The ledger holds **only partner-owned work** — every open item belongs to someone who can drain it (no-owner captures were flagged in their run report, never recorded), so the board stays an honest signal of real waiting work, not a graveyard.

`ledger` is also printed **inline at the end of a `daily` run** (Step 3) — same board, two surfaces: `daily` closes with it, `ledger` serves it on demand.

---

## The pickup loop (how a partner drains its slice)

The other half of the bus — documented **here as the single home for the protocol**, so any partner follows the same drain regardless of which mode wrote the item. **Source-agnostic: a daily-routed pointer and a relayed pointer drain identically.** Dispatch writes open items; the **receiving partner**, on its own activation, drains them:

1. **Find your open items** — grep your own slug for unchecked boxes across the whole record:
   `grep -nF '[ ] \`researcher\`' _agent/dispatch.md` (substitute your slug). This is a *pull*: a partner reads the shared record, never the human's `daily/` directly unless it chooses to follow a `[[daily/…]]` link. A relayed item carries a `[[_agent/handoffs/…]]` link instead — follow it to the full handoff doc.
2. **Act on each** in your own voice and your own memory — fold it into your `thread.md`/working record, start a protocol, answer it, whatever your domain calls for. Dispatch did not do this for you; the gist is only a pointer.
3. **Check it off** — flip that one line `- [ ]` → `- [x]` and stamp it: append ` ✓ picked up YYYY-MM-DD`. You edit **only your own tagged lines**; never another partner's line, never a run header, never another run's block. A checked item stays in the log as history — the loop is "drained," not "deleted."

Because items are checked in place and dispatch only ever *appends* fresh blocks, the two writers never collide: dispatch owns block creation, each partner owns the status of its own lines. A partner that re-greps later sees its checked items as done and only acts on what's still open.

## Log

Append one partner-tagged entry to `{log}` in the operating-contract format, per mode (the `dispatch` log type; the contract's type set is non-exhaustive — this op owns `dispatch`):

```
## [YYYY-MM-DD HH:MM] dispatch (librarian) | daily <scope>: <N> fragment(s) from <M> daily note(s) routed to <partners> [→ [[_agent/dispatch.md]]]
## [YYYY-MM-DD HH:MM] dispatch (librarian) | relay: <from> → <to> — <gist> [→ [[_agent/dispatch.md]]]
```

`ledger` is read-only — it writes **no** `{log}` entry (nothing changed). Write **no** session note in any mode — the summoning partner (the Librarian, or the publishing partner on a relay) owns the single session note for the sitting (operating contract § session-ownership).

## Verify

After writing, re-read what you produced and confirm — by mode:

**`daily`:**
- `_agent/dispatch.md` gained exactly one `daily/…` run block per in-scope source, each with a valid `routed through line N` watermark and one pointer line per routed fragment.
- **Every new pointer is written open** (`- [ ]`); dispatch flipped no status and touched no prior block.
- **No file under `daily/` was modified** and **nothing was written to the wiki**.
- Every pointer resolves: `- [ ]` + a backtick `` `slug` `` matching a live `vlt-agent-{slug}` + a `[[daily/…]]` link to a real file. No domain-less slug.
- The `{log}` entry was appended, tagged `(librarian)`. No secret in a pointer.

**`relay`:**
- The recipient slug is **live** (a real `vlt-agent-{to-slug}`); no dangling pointer was written.
- The **idempotency rule was applied**: no second open pointer exists for the same `(handoff-path, to-slug)` (a no-op was honored), and a re-relay after check-off appended a fresh open pointer.
- Exactly one `relay: <from> → <to>` block was appended (or none, on a no-op), pointer open, linking the real `_agent/handoffs/…` doc. `daily/` untouched, wiki untouched. The `{log}` relay entry was appended. No secret in the gist.

**`ledger`:**
- **Nothing was written** — read-only. The counts match a fresh grep of open items; the board groups only live, partner-owned slugs.

Report the result; fix any gap before closing.
