# vlt-dispatch — reference: Mode `relay`

Read on entering `relay` mode (router: `SKILL.md`, Mode dispatch).

## Mode: `relay` — append a pre-addressed partner→partner pointer

A publishing partner has something waiting for another partner — a **durable handoff doc** in `_agent/handoffs/`, a question with no doc yet, the answer that closes one, or an unsolicited delivery written inline — and needs the recipient to know. `relay` is the seam that closes: it appends a **pre-addressed** open pointer into the recipient's slice. **No `daily/` read, no classification** — the address arrives known. Relay is a **thin scribe, not a gatekeeper**: it takes the publisher's payload already decided and appends it without re-judging the content (YAGNI — no rigid gatekeeping until a real pollution problem appears). Every relay declares a **`shape`** — `handoff`, `ask`, `answer`, or `deliver` (The four shapes, below) — which determines what the pointer carries and what keys it.

### Who fires it, and the publish-side reflex (single home)

Relay is normally **fired automatically by the publishing partner** as the last step of writing a handoff doc — the **relay-when-done reflex**. This is the shared publish-side protocol, owned **here** as its single home (mirroring how the pickup loop is owned here for the drain side); a partner *names* the reflex and points at this mode, it does not restate the mechanics. The reflex, in full:

> **After writing (or revising) a handoff doc to `_agent/handoffs/`, the publishing partner invokes `vlt-dispatch relay (to-slug, gist, handoff-path)` as the final step of the write.** It supplies the recipient's slug, a one-line gist of what's waiting, and the stable path of the doc. It does **not** write `_agent/dispatch.md` itself — dispatch is the scribe (single-writer). **The reflex fires equally on a spec `version` bump** (a `{specs}` contract — see `{conventions}/spec.md`): the authoring partner fires one relay per partner listed in the spec's `consumers:`, in the same session as the bump.

A human may also **invoke `relay` directly** for debugging or a manual handoff (`/vlt-dispatch relay <to-slug> "<gist>" <handoff-path>`, optionally `from <from-slug>`, optionally a `shape`/`ref` for an ask, answer, or delivery) — reachable, but not the advertised main path.

### The four shapes

Every relay declares a **`shape`** — what the pointer carries, and what keys it:

- **`handoff`** — `handoff-path` **required**. The original contract, unchanged: a durable doc is waiting at a stable path. The relay-when-done reflex and the spec `consumers:` fan-out both fire this shape.
- **`ask`** — **no path** (the doc does not exist yet — that is the ask); **`ref` required**. The gist carries the question, why it matters, and what would close it. This is the shape the address rule (`{conventions}/frontmatter.md`, *The address rule*) routes onto this rail.
- **`answer`** — path **optional** (cite the durable artifact, typically a wiki page, as a `[[wikilink]]`); **`ref` required, and it must be the originating `ask`'s `ref`**.
- **`deliver`** — **no path required** (path optional, same clause as `answer`: cite durable artifacts as `[[wikilinks]]` — payload, never the key); **`ref` required**. An **unsolicited delivery whose payload is written inline**: the gist carries the delivery; nothing was asked. The `ref` is publisher-chosen — a kebab slug unique per delivery act, reused only to re-notify (a revised delivery = new information; the idempotency ladder below applies unchanged).

**`ref`** is a short kebab slug keying the pointer — chosen by the ask's publisher and reused verbatim by the answer, or chosen by the deliverer. It is not a path and points at nothing — **it exists to key the pointer.** A `[[wikilink]]` in **any** shape's pointer is **payload, never the key** — the key check never resolves a wikilink, **except** a key-path link resolving under the handoff zone (`_agent/handoffs/` or `_agent/specs/`), which is a `handoff-path` written as a link (`ledger` renders this rule read-side).

**Backward compatibility (no backfill).** An un-annotated header **with a path** reads as `handoff`. An un-annotated header **without a path** is **legacy pre-shape traffic** — tolerated as written, drained normally, exempt from the key check and from the idempotency guarantee it never had. A shape-annotated **pathless** pointer written **before `deliver` existed** is **proto-`deliver` traffic** — the same posture, extended to the shape's own pre-history: tolerated as written, drained normally, exempt from the key check, reported by `ledger` as a denominated count ("N proto-`deliver` pointers (pre-shape)"), never as a finding. Neither lane is ever a legal form to write anew. No existing record is ever edited to conform.

### Inputs and validation

Required always: **`to-slug`** (the recipient's routing slug) and **`gist`** (one-line, in the publisher's framing). Per shape: **`handoff-path`** (the stable path under `_agent/handoffs/` or `_agent/specs/`) is **required** for `handoff`, never assumed for `ask` (an ask has no doc — that is the point), and optional for `answer` and `deliver`; **`ref`** is **required** for `ask`, `answer`, and `deliver`. Optional: **`from-slug`** (the publisher; infer from the calling partner when fired as a reflex); **`to-principal`** (a roster principal-slug, only meaningful where a routing profile declares one — `SKILL.md`, *the routing profile*; absent = the default principal; an unknown principal-slug stops the act — never guess a roster). Then:

- **Liveness (light).** Confirm `to-slug` matches a live `vlt-agent-{to-slug}` in `{project-root}/.claude/skills/`. If it doesn't, don't write a dangling pointer — say so and stop (a relay to a retired/typo'd slug is **failure mode #4**, phantom recipient; we surface it rather than parking an orphan). *(Deeper liveness checks stay deferred until they bite.)*
- **`from-slug ≠ to-slug`** — a partner does not relay to itself (mirrors consult's "a partner does not consult itself"). Stated against the addressee model in force: **"self" means the same `(partner-slug, principal)` pair** — under a routing profile, the same partner acting for a **different** principal is a legal relay (the cross-principal handoff is the traffic a roster exists for); with no profile there is one principal, and the pair test reduces to the same slug-equality this rule has always been.
- **Secret hygiene.** Same as `daily` — never put a credential in the gist.
- **The handoff doc itself is the publisher's, not dispatch's** — relay points at it, never reads it for content, never edits it. Surface-and-point holds: the pointer carries a gist; the rich spec stays in `_agent/handoffs/`.

### The idempotency rule — keyed on `(handoff-path | ref, to-slug, principal)`

The key is per shape: a `handoff` keys on its **doc path** exactly as it always has; an `ask`, `answer`, or `deliver` keys on its **`ref`**. This is why `ref` is required — an unkeyed pointer disables the spam guard below **invisibly**: the guard's absence is indistinguishable from the guard passing. The key carries the **recipient pair**, not the recipient slug alone: the same ask relayed to the same partner for two different principals is two distinct waits, not a duplicate; an un-annotated pointer keys as the default principal, so every existing key is unchanged (backward-compatible, no backfill — the pre-shape idiom, *Backward compatibility* above, extends to the facet: an un-faceted pointer *is* default-principal traffic, exempt from nothing because it needs no exemption). Two kept properties: an `answer` reusing its `ask`'s `ref` **does not collide** (opposite directions — different `to-slug`), and the open/checked/no-op ladder below applies per key, unchanged.

Before appending, grep the record for an existing relay pointer with this **same `(key, to-slug, principal)` tuple** and apply:

- **No pointer exists** → append a fresh open pointer (first relay).
- **An *open* pointer exists** (`- [ ]`) → **no-op.** The recipient hasn't drained the prior notice yet; a second relay of the same key is the **#1 spam** failure mode (a partner re-firing each awakening). Say "already open in `<to-slug>`'s slice — no-op" and write nothing.
- **The latest pointer is *checked off*** (`- [x]`) → the recipient already picked up the prior version and the publisher is relaying **again** = new information (a revised spec — **#2 stale-spec**). Append a **fresh open pointer** to re-notify.

This is **idempotency hygiene, not content judgment** — dispatch enforces "one open pointer per `(key, recipient pair)`," nothing about whether the handoff is *good*. The scribe stays thin.

### The handoff lifecycle this rule assumes (stable path, updated in place)

This section governs the **`handoff` shape**, whose key is the doc path: it only works if **handoffs are updated in place at a stable path, not versioned into new files.** A publisher revising a provisional spec edits the *same* `_agent/handoffs/…` doc; an un-drained open pointer then **auto-tracks the freshest content** (the recipient follows the link to whatever the doc now says), and a fresh pointer is only needed when the recipient had already checked the prior one off. A stable path also blunts **#3 dangling link**. Specs follow the same discipline: an in-place `version` bump *is* the stable-path rule at work — the path holds and the idempotency rule above governs the re-notify; a `supersedes:` structural rewrite is a **new path** and gets fresh pointers (see `{conventions}/spec.md`). An `ask`/`answer`/`deliver` needs no lifecycle rule beyond its `ref` lifetime: a `ref` is stable by construction — it is never revised, only answered (an ask's) or re-fired (a delivery's). *(This lifecycle rule is the cross-cutting half; its single home is the operating contract's hand-offs section — relay depends on it, but the contract owns it.)*

### Write the relay block

Append a **`relay` block** to `_agent/dispatch.md`. The header shape — `relay: <from> → <to>` — **is the mode signal** (vs `daily/…`), so a human scanning sees partner-traffic at a glance and the next run knows to apply the pointer's-key (not watermark) idempotency. The header also **carries the shape when it is not `handoff`** — that annotation is where the key lives for a doc-less pointer (`ask`/`answer`/`deliver`):

```
## [YYYY-MM-DD HH:MM] relay: <from-slug> → <to-slug> — 1 item
- [ ] `to-slug` Partner Name — gist of what's waiting → [[_agent/handoffs/…]]
```

```
## [YYYY-MM-DD HH:MM] relay: <from-slug> → <to-slug> (ask: <ref>) — N items
- [ ] `to-slug` Partner Name — the question, why it matters, what would close it
```

An `answer` is analogous — `(answer: <ref>)`, reusing the ask's `ref`, its pointer optionally citing the durable artifact as a `[[wikilink]]`. A `deliver` carries its publisher-chosen `ref` the same way:

```
## [YYYY-MM-DD HH:MM] relay: <from-slug> → <to-slug> (deliver: <ref>) — 1 item
- [ ] `to-slug` Partner Name — the delivery, written inline; durable artifacts cited as [[wikilinks]]
```

Where a routing profile declares a roster and the act is addressed to a non-default principal, the pointer carries the **principal facet** in a paren after the gist (the same paren idiom as `blocked:` — `SKILL.md`, *Why a record, not an inbox*):

```
- [ ] `to-slug` Partner Name — gist of what's waiting (for: {principal-slug}) → [[_agent/handoffs/…]]
```

An un-faceted pointer is the default principal's — never annotate the default.

One relay = one **pre-addressed act**: a `handoff`, `answer`, or `deliver` carries a single pointer; a **batched `ask`** may carry several questions when they are one act — one publisher, one recipient, one moment, each pointer its own `ref`. *(The pattern the field surfaced: a backlog accumulates items one at a time and never sees that nine of them are one act; the triage onto an addressed rail is where that becomes visible — an observation, not a rule.)* The pointer **may** optionally carry the `blocked:` triage facet in a paren after the gist (the backlog facet in `{conventions}/frontmatter.md` — absence = untagged; `ledger` groups by it). The pointer is the **same line format** every mode emits, so the recipient drains it with the **same** pickup loop — a relayed item is indistinguishable from a daily-routed one once in the slice, which is exactly the point.

### Report

Brief, since relay is usually a sub-step of a partner's handoff:

> Relayed to **Creative**: spec waiting at `_agent/specs/{date}-{owner}-to-{consumer}-{slug}.md`. Open in the Creative's slice; it'll surface when the Creative next orients.

Or, for an `ask`:

> Relayed an ask to **Researcher** (`ask: {question-slug}`): what would close it is a source the vault doesn't hold. Open in the Researcher's slice; it'll surface when the Researcher next orients.

Or, for a `deliver`:

> Relayed a delivery to **Researcher** (`deliver: {delivery-slug}`): the payload is in the gist, with durable notes cited as wikilinks. Open in the Researcher's slice; it'll surface when the Researcher next orients.

Or, addressed to a roster principal:

> Relayed to **Researcher** for `{principal-slug}` (`for: {principal-slug}`): spec waiting at `_agent/handoffs/{doc-slug}.md`. Open in the Researcher's slice, faceted to `{principal-slug}`'s thread.

On a no-op (open pointer already present): "Creative already has an open pointer for this spec — nothing appended." On a phantom recipient: "No live partner `<to-slug>` — nothing written; check the slug."

### Log line

The mode's `{log}` entry (router: Log):

```
## [YYYY-MM-DD HH:MM] dispatch (librarian) | relay: <from> → <to> — <gist> [→ [[_agent/dispatch.md]]]
```

### Verify

After writing, re-read what you produced and confirm:

- The recipient slug is **live** (a real `vlt-agent-{to-slug}`); no dangling pointer was written.
- The **idempotency rule was applied against the shape's key, pair-inclusive**: no second open pointer exists for the same `(handoff-path | ref, to-slug, principal)` (a no-op was honored), and a re-relay after check-off appended a fresh open pointer.
- Any `(for: …)` facet written this run names a principal on the routing profile's roster (an unknown slug should have stopped the act — never guess a roster).
- **Every pointer written this run resolves a key** — a path on disk (`handoff`), or a `ref` in the header (`ask`/`answer`/`deliver`).
- Exactly one `relay: <from> → <to>` block was appended (or none, on a no-op), pointer(s) open, a `handoff` linking the real `_agent/handoffs/…` doc, an `ask`/`answer`/`deliver` carrying its `ref` in the header. `daily/` untouched, wiki untouched. The `{log}` relay entry was appended. No secret in the gist.

Report the result; fix any gap before closing.
