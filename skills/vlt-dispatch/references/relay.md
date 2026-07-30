# vlt-dispatch — reference: Mode `relay`

Read on entering `relay` mode (router: `SKILL.md`, Mode dispatch).

## Mode: `relay` — append a partner→partner handoff pointer

A publishing partner has written a **durable handoff doc** to `_agent/handoffs/` and needs the recipient to know it's waiting. `relay` is the seam that closes: it appends a **pre-addressed** open pointer into the recipient's slice. **No `daily/` read, no classification** — the address arrives known. Relay is a **thin scribe, not a gatekeeper**: it takes the publisher's `(slug, gist, handoff-path)` already decided and appends it without re-judging the content (YAGNI — no rigid gatekeeping until a real pollution problem appears).

### Who fires it, and the publish-side reflex (single home)

Relay is normally **fired automatically by the publishing partner** as the last step of writing a handoff doc — the **relay-when-done reflex**. This is the shared publish-side protocol, owned **here** as its single home (mirroring how the pickup loop is owned here for the drain side); a partner *names* the reflex and points at this mode, it does not restate the mechanics. The reflex, in full:

> **After writing (or revising) a handoff doc to `_agent/handoffs/`, the publishing partner invokes `vlt-dispatch relay (to-slug, gist, handoff-path)` as the final step of the write.** It supplies the recipient's slug, a one-line gist of what's waiting, and the stable path of the doc. It does **not** write `_agent/dispatch.md` itself — dispatch is the scribe (single-writer). **The reflex fires equally on a spec `version` bump** (a `{specs}` contract — see `{conventions}/spec.md`): the authoring partner fires one relay per partner listed in the spec's `consumers:`, in the same session as the bump.

A human may also **invoke `relay` directly** for debugging or a manual handoff (`/vlt-dispatch relay <to-slug> "<gist>" <handoff-path>`, optionally `from <from-slug>`) — reachable, but not the advertised main path.

### Inputs and validation

Required: **`to-slug`** (the recipient's routing slug), **`gist`** (one-line, in the publisher's framing), **`handoff-path`** (the stable path under `_agent/handoffs/` or `_agent/specs/`). Optional: **`from-slug`** (the publisher; infer from the calling partner when fired as a reflex). Then:

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

The idempotency key is the doc path, so it only works if **handoffs are updated in place at a stable path, not versioned into new files.** A publisher revising a provisional spec edits the *same* `_agent/handoffs/…` doc; an un-drained open pointer then **auto-tracks the freshest content** (the recipient follows the link to whatever the doc now says), and a fresh pointer is only needed when the recipient had already checked the prior one off. A stable path also blunts **#3 dangling link**. Specs follow the same discipline: an in-place `version` bump *is* the stable-path rule at work — the path holds and the idempotency rule above governs the re-notify; a `supersedes:` structural rewrite is a **new path** and gets fresh pointers (see `{conventions}/spec.md`). *(This lifecycle rule is the cross-cutting half; its single home is the operating contract's hand-offs section — relay depends on it, but the contract owns it.)*

### Write the relay block

Append a **`relay` block** to `_agent/dispatch.md`. The header shape — `relay: <from> → <to>` — **is the mode signal** (vs `daily/…`), so a human scanning sees partner-traffic at a glance and the next run knows to apply doc-path (not watermark) idempotency:

```
## [YYYY-MM-DD HH:MM] relay: <from-slug> → <to-slug> — 1 item
- [ ] `to-slug` Partner Name — gist of what's waiting → [[_agent/handoffs/…]]
```

One relay = one pointer (a relay carries a single pre-addressed handoff). The pointer **may** optionally carry the `blocked:` triage facet in a paren after the gist (the backlog facet in `{conventions}/frontmatter.md` — absence = untagged; `ledger` groups by it). The pointer is the **same line format** every mode emits, so the recipient drains it with the **same** pickup loop — a relayed item is indistinguishable from a daily-routed one once in the slice, which is exactly the point.

### Report

Brief, since relay is usually a sub-step of a partner's handoff:

> Relayed to **Creative**: spec waiting at `_agent/specs/{date}-{owner}-to-{consumer}-{slug}.md`. Open in the Creative's slice; it'll surface when the Creative next orients.

On a no-op (open pointer already present): "Creative already has an open pointer for this spec — nothing appended." On a phantom recipient: "No live partner `<to-slug>` — nothing written; check the slug."

### Log line

The mode's `{log}` entry (router: Log):

```
## [YYYY-MM-DD HH:MM] dispatch (librarian) | relay: <from> → <to> — <gist> [→ [[_agent/dispatch.md]]]
```

### Verify

After writing, re-read what you produced and confirm:

- The recipient slug is **live** (a real `vlt-agent-{to-slug}`); no dangling pointer was written.
- The **idempotency rule was applied**: no second open pointer exists for the same `(handoff-path, to-slug)` (a no-op was honored), and a re-relay after check-off appended a fresh open pointer.
- Exactly one `relay: <from> → <to>` block was appended (or none, on a no-op), pointer open, linking the real `_agent/handoffs/…` doc. `daily/` untouched, wiki untouched. The `{log}` relay entry was appended. No secret in the gist.

Report the result; fix any gap before closing.
