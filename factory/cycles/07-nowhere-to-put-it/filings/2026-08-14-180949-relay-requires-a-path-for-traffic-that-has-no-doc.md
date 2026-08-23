# `vlt-dispatch` relay requires a `handoff-path`, but a third of real relay traffic has no doc to point at — and a pathless pointer is unkeyed, so the anti-spam guard is silently inert

_Filed 2026-08-14 from **vlt-core** (single-user vault, ~14 months of traffic), out of a
`convention edit` mint that set out to fix a backlog-routing problem and found this underneath it.
Classification: **defect** (two, one compounding the other). The companion filing —
`2026-08-14-181000-knowledge-gap-addressed-to-a-rail-with-no-recipient.md` — is the other half of
the same mint; they were applied together and should probably be read together._

## The claim

`references/relay.md` line 19 makes **`handoff-path` required** on every relay. In this vault it
isn't — and the deviation is systematic, successful, and structured.

Counted across the whole of `_agent/dispatch.md`: **40 relay pointers, 27 carry a handoff/spec path,
13 do not.** Every drained pathless pointer worked. This is not partners being sloppy about a rule;
it is the spec being narrower than the traffic.

## Evidence

Auditing the 13 rather than treating them as one leak, they sort cleanly into **two shapes the spec
never had**:

| shape | payload | why there is no path | count |
|---|---|---|---|
| **ask** | a question only the recipient's domain can close | **the doc does not exist yet — that is the ask** | ~8 |
| **answer** | closing the loop on a prior ask | the durable artifact is a **wiki page**, cited inline as `[[wikilinks]]` | ~5 |

The `ask` instances are nearly all → Researcher (`health-coach→researcher` 2026-06-16;
`chess-coach→researcher` 2026-07-18; `librarian→researcher` ×4 on 2026-07-25 — a full lint surfacing
four cross-page contradictions at once, food-safety first; `football-analyst→researcher` 2026-08-09
and 2026-08-11). The `answer` instances are the return leg (`researcher→career-strategist`,
`researcher→football-analyst`, `researcher→librarian`, `librarian→health-coach`, `chef→health-coach`,
`creative→librarian`).

So relay's `handoff-path` requirement encodes a **doc-handoff assumption**, and the bus has grown
into a **question-and-answer channel** around it. Partners route around the requirement because
inventing a doc to satisfy it would be ceremony with no reader.

## The compounding defect — and the more serious half

`relay.md`'s idempotency rule keys on **`(handoff-path, to-slug)`**. Therefore:

> **A pathless pointer is unkeyed.** The grep the rule specifies has nothing to match on, so
> **failure mode #1 (spam — a partner re-firing the same notice each awakening), which the spec
> itself names, is silently unguarded for a third of all traffic.**

Nothing detects this, because the guard's absence looks identical to the guard passing. Secondarily,
nothing links an `answer` back to the `ask` it closes — ask→answer pairs are two unrelated lines that
a human reconstructs by reading.

This is what turned a "widen the spec to match practice" mint into a hardening one. Ratifying the
drift at face value would have blessed a disabled guard.

## The local fix (applied; proposed upstream)

Relay declares a **`shape`**, which sets what the pointer must carry:

- **`handoff`** — `handoff-path` **required**. The original contract, unchanged.
- **`ask`** — **no path** (the doc does not exist yet); **`ref` required**. The gist carries the
  question, why it matters, and what would close it.
- **`answer`** — path **optional** (cite the resulting wiki page as `[[wikilinks]]`); **`ref`
  required, and it must be the originating `ask`'s `ref`**.

**`ref`** is a short kebab slug naming the question (`rb-workload-stickiness`,
`mech-tenderized-doneness`), chosen by the ask's publisher and reused verbatim by the answer. It is
not a path and points at nothing — **it exists to key the pointer**. The idempotency key becomes
`(handoff-path | ref, to-slug)`.

Two properties worth keeping if this is taken up:

- Because the key includes the recipient, **an `answer` reusing its `ask`'s `ref` does not collide
  with it** — the two travel in opposite directions, so `(ref, to-slug)` differs. The shared `ref`
  links the pair without either suppressing the other.
- **Backward-compatible, no backfill.** An un-annotated relay header reads as `handoff`, so all 40
  existing pointers in this vault stayed valid as written. Header form used locally:
  `## [YYYY-MM-DD HH:MM] relay: <from> → <to> (ask: <ref>) — N items`.

Also widened locally: the "one relay = one pointer" rule now admits a **batched `ask`** (one
publisher, several questions, same recipient, one moment), each pointer carrying its own `ref`. The
2026-07-25 four-contradiction lint relay was already doing this.

Files touched locally: `.claude/skills/vlt-dispatch/references/relay.md` (inputs/validation, the new
*three shapes* section, the idempotency rule + the "why `ref` is required" note, the block format,
the lifecycle scoping note, and Verify).

## Provenance guess — marked as a guess

I did not trace this to a specific build, and I am guessing: relay looks like it was specified for
the **spec/handoff notification** case first (the `relay-when-done` reflex and the spec `consumers:`
fan-out both read as the motivating scenario), and the `ask`/`answer` traffic arrived later as the
bus generalized — at which point the required path was never revisited. The `consult` mode's
existence may have masked it: `consult` is the *synchronous* question channel, so an asynchronous
question had no named home and landed on relay without the spec noticing. **That last point is the
part I'd most want the capture pass to check**, since if it is right, the cleaner fix might be a
`consult`-adjacent async mode rather than a relay shape facet — and this vault chose the relay facet
partly because it required no new mode.

## What a receiver-side check would need

If the module wants a bell for this rather than trusting the write side: the honest check is
"**every relay pointer resolves a key**" — a path that exists on disk, or a `ref` present in the
header. That catches the unkeyed pointer, which is the failure that cannot be seen by reading.
