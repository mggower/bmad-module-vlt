# Hand-offs and consults re-pay the full boot the conversation already paid

_Filed 2026-07-29 from the **factory**, prompted by a field signal: owner-observed token expense in
partner sessions on the work-machine consumer vault. Converged out of a token-efficiency ideation
session (`_output/brainstorming/brainstorming-session-2026-07-29-0804.md`, candidate C2); grounding
measured against module source at 9f05579. Owner elected to file (2026-07-29)._

## The claim

Two paths multiply the activation boot cost (see companion filing `2026-07-29-082930-*` for the
boot itself):

1. **Same-conversation hand-offs skip Beat 2 but not the contract read.** The skip is scoped
   precisely: *"On a same-conversation hand-off you may skip the Beat 2 reads as already-fresh."*
   The contract read sits **before** Beat 1, outside the skip — so a researcher→librarian hand-off
   re-reads the full ~38K contract in the same context window where the researcher just read it.
2. **A consult plausibly boots the whole ritual for one question.** The consult engine's prompt
   tells the summoned agent to read its full SKILL.md and *"BECOME that partner"* — and that SKILL
   mandates the contract read plus Beat 2 orient, with no consult exemption anywhere in the prompt.
   A conscientious summoned partner pays SKILL (~10K chars) + contract (38K) + orient reads to
   answer one attributed question, inside a mode whose whole design premise is that it is cheap
   traffic, not a sitting.

## Grounding

- `skills/vlt-agent-researcher/SKILL.md:31` (and `:31` in librarian/creative) — the Beat-2-only
  skip; `:22` — the contract read it does not cover.
- `skills/vlt-setup/assets/workflows/vlt-consult.js:125-127` — the summoned-partner prompt: read
  SKILL.md + identity.md + thread.md; no instruction to skip the SKILL's activation ritual.
- `skills/vlt-dispatch/SKILL.md:205` — consult is "depth-1 hard", framed as *"traffic, not a queue
  item"* (`:18`) — the design intent is lightweight; the boot cost isn't.
- Hand-off chains are the module's normal shape: researcher→librarian is the canonical ingest
  hand-off (`vlt-agent-researcher/SKILL.md:46`), so the double-pay is on the main path, not an edge.

## Why it matters

The costs are multiplicative with the boot whale: a two-partner conversation with one consult
plausibly pays the ~38K contract three times in one context window. Consults were shipped (A4-5)
specifically as the cheap synchronous alternative to a full relay hand-off; if a consult's true
cost approaches a sitting's, the convention's economics are inverted in the field.

## Candidate dispositions (for capture to rule — not pre-empted here)

- **(a) Extend the already-fresh skip to the contract read.** Same rationale the Beat 2 skip already
  states; one-line-class change in three partner SKILLs. Cheapest, and honest — the contract *is*
  already fresh in the window.
- **(b) Consult-lite boot, stated in the engine prompt.** `vlt-consult.js` explicitly exempts the
  summoned partner from the activation ritual: read SKILL for voice/domain + identity/thread +
  `groundIn` paths; skip contract and Beat 2 orient. The engine is the single home for consult
  protocol (`vlt-dispatch/SKILL.md:207`), so the exemption lands in exactly one place. Note the
  consult convention (`consult@1`) governs *when* a consult is earned, not the summoned boot — a
  prose clarification there may suffice without a version bump, but that is capture's call under
  the handshake rules.
- **(c) Both.** They are independent and both small; (a) fixes relays, (b) fixes consults.

Preference, weakly held: **(c)** — the two legs don't overlap and each is a scoped edit at its
single home.
