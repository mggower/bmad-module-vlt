---
id: 'ST-4'
slug: 'provenance-staffed-cognition-unstaffed'
title: 'Every lifecycle artifact is written to be re-read later and none is written to be read now — so the loop preserves what happened and never staffs the decision in front of it'
status: 'standing'
opened: '2026-08-25'
opened_by: 'owner problem-solving session (brainstorm, Ideate-for-me stance)'
session: '_output/brainstorming/brainstorm-lifecycle-comprehension-2026-08-25/ (untracked — provenance only; memlog + keepsake)'
causes:
  - '(a) Provenance is fully staffed and cognition is unstaffed — every artifact in the loop is shaped for durable re-reading, none is shaped for the decision being made today, so the owner reads a record where a decision surface is needed.'
  - '(b) There is no promise artifact between the diagnosis chain and the implementation chain — nothing states the vault-visible delivered difference until the CHANGELOG, which is written after the surprise.'
  - '(c) The clerk is forbidden a view and then asked to prepare a decision — recommendation and authority were fused, so removing the clerk''s steering also removed the loop''s only staffed reading of the evidence.'
  - '(d) The inbox uses location as a proxy for lifecycle status — one directory encoding a four-state machine whose only exit is success, so the queue can grow but not drain.'
cited_by:
  - 'factory/platform/roadmap.md §P-16 (the `promise:` line — queued 2026-08-25, deferred past Cycle 12 by owner ruling)'
superseded_by: ''
---

# ST-4 — Provenance is staffed, cognition is not

**Scope precedent, stated rather than smuggled.** `ST-1`, `ST-2` and `ST-3` all read the
**module's** internal structure. This one reads the **factory's**, and the register's boundary
table assigns "the factory's own practice" to method notes (`factory/method/`). The cut this
study rests on is **descriptive vs causal**: a method note answers *how does the factory work*
(`cycles-were-arcs.md` is naming history), a study answers *why does this keep happening*. This
is causal, recurring, and cross-cycle — four symptoms in four subsystems from one omission — so
it is filed here. That widens the register. A later reader who thinks the widening was wrong
should say so in this file rather than quietly renumbering it; the register records
disagreement rather than resolving it.

## The presenting complaint

The owner, mid-flight in Cycle 12's ideation, reported four things at once:

1. *"Most of the time I feel completely lost during ideation. I don't understand what the clerk
   is asking me to rule on."*
2. *"Often the clerk is missing important context."*
3. *"There have been a few cycles recently which ultimately have not shipped what I expected to
   be delivered."*
4. *"`factory/inbox/` is always drowning in filings that make it difficult to sift through."*

These read as four unrelated complaints — a UX problem, a grounding problem, a scope problem
and a filing problem. They are one.

## Root cause (a) — the loop is written to be re-read, never to be read now

Every artifact the lifecycle produces is shaped for **durable re-reading**: the filing preserves
what a vault experienced, the capture preserves the grounding, the roadmap preserves the
rulings, the study register preserves the diagnosis, the ledger preserves the off-cadence work,
the acceptance ledger preserves the checks. This is a genuine strength and it is why the factory
can reconstruct any decision years later.

Nothing is shaped for **the decision being made today**. There is no artifact whose job is to
put one question in front of the owner with the evidence that made it a question, the cost of
being wrong, and what happens if they say nothing. The roadmap is asked to do that job, and it
cannot: it is a 1,375-line durable record, and the owner is asked to read it as a decision
surface.

**Five Whys, condensed.** *Why is ideation opaque?* → the seeded questions arrive in the clerk's
vocabulary (`binds:`, `spike:`, `Q4`), not in terms of what will be built. *Why?* → the scaffold
seeds questions the capture flagged, and the capture flagged them from grounding notes, so the
question arrives stripped of the evidence that generated it. *Why?* → capture's job is
compression (filing → roadmap entry) and the compression is tuned for the record's durability;
decision-relevant material is the first thing dropped because the record does not need it.
*Why?* → nothing in the loop is accountable for a decision packet; the roadmap is accountable
for the record, and the two are different artifacts. *Why?* → **because the loop was designed
against the failure of forgetting, and never against the failure of not understanding.**

The proof that this is structural rather than a bad session: the loop's own remedies all point
the same way. `ST-2` and `ST-3` exist because diagnoses were being lost; `factory/studies/`
exists so a cause survives; the spike register exists so an external read survives; the platform
ledger is *"never archived"*. Every mechanism the factory has built for itself is a memory
mechanism. It has built none for comprehension.

## Root cause (b) — no promise artifact between the two chains

The loop has a **diagnosis chain** (filing → capture → ruling) and an **implementation chain**
(brief → build → release). The diagnosis chain describes what is broken. The implementation
chain describes which sites change. **Neither states what a vault owner will see afterwards.**

The first sentence anywhere in the loop written in vault-facing terms is the `CHANGELOG.md`
entry, authored at Stage 8 of `vlt-release` — after the build has shipped. So a cycle can be
correctly grounded, correctly briefed, correctly built and cleanly released, with no rule
violated at any stage, and still deliver something the owner did not expect. There is no gate
this passes through, because there is nothing to gate.

**The worked instance is the session that produced this study.** Cycle 12's ideation, read live:
fourteen questions RULED across six rounds — the lint cost joint, the five-cycle carry, the
convention bump, the `_vault/` posture, the P-14 withholding — every one of them
*diagnosis-shaped*. And the **Grouping & order** section, which is the only part that determines
what actually ships, stood entirely empty: cycle scope unfilled, every `build-N` bullet
unfilled, every `binds:` and `spike:` unfilled. The owner had ruled fourteen substantive things
and had not yet ruled **what ships**, and nothing in the section's shape made that gap legible.
Downstream, `build-brief` infers scope from a `binds:` roster nobody filled
(`build-brief` SKILL.md:88 — *"If the bullet carries no `binds:` line, reconstruct…"*).

## Root cause (c) — the clerk is forbidden a view, then asked to prepare a decision

`ideation-scaffold` is explicit: *"Act as the ideation session's clerk… it scaffolds the
recording, never the deciding"*, *"clerk, not advisor: capture, read back, never steer"*, and
*"a slot the owner hasn't filled stays visibly empty; an empty slot is honest, a guessed answer
is a lifecycle violation"* (ruled 2026-07-12).

The intent is sound and the ruling protects something real: an owner who rubber-stamps a clerk's
proposal is not steering. But **recommendation and authority were removed together.** The party
required to have read all the evidence is the one party forbidden from saying what it thinks the
evidence means, so the reading is never staffed by anyone, and the owner receives the least
processed material in the building and is asked for the most consequential judgment.

This is a **TRIZ contradiction**, not a trade-off: the clerk must not steer (or authority is
theatre) *and* the owner cannot decide without a reading (or comprehension collapses). It is
resolvable by separating the two along an axis other than existence — by **time and label** (the
clerk's read is written before the question, marked non-binding, and the owner's confirm is one
word), or by **person** (the roster carries the recommendation; the clerk stays mute). The
factory already runs the second pattern successfully: `roadmap-roundtable` convenes agents who
*are* allowed views, and records dissents. Ideation has no equivalent.

## Root cause (d) — the inbox is location-as-proxy-for-status

A filing leaves `factory/inbox/` only at **retirement** — its build shipped *and* its own clauses
passed acceptance (`factory/inbox/README.md`, lifecycle step 4; criterion single-homed in
`cycle-closeout` Stage 5). Acceptance is frequently **field-contingent**, bound to a live-vault
event that may never fire. So:

- One flat directory encodes a **four-state machine** — filed, captured, built, accepted — with
  no way to see which state any file is in short of reading the open roadmap.
- The queue's **only exit is success**. There is no kill rail: a filing cannot be closed
  won't-fix, and nothing ages out. It can grow and cannot drain.
- The owner's instinct in the session — *"Should the inbox only hold unclaimed filings?"* — is
  correct, and the reason it is correct is that provenance is **already** preserved elsewhere:
  the cycle roadmap is described in that same README as the authoritative per-filing record.
  Location was never carrying the story.

**This is `ST-2`'s cause, inside the factory.** `ST-2` names PARA location standing in for a
trust level the `trust:` field already states. The inbox has location standing in for a
lifecycle state the roadmap already records. Same shape, different building — and it was found
during the very cycle built to cure the module-side instance. Cycle 12's own through-line
sentence describes it exactly: *an answer exists and the surface that stood in for it never
learned.*

A second instance surfaced in the same reading: Cycle 12's ideation section header reads
*"Session OPEN — skeleton laid 2026-08-25, no slot filled"* after six rounds of rulings had
filled it. A written status standing in for a live one, still reading as true.

## Contributing factors

- **Batch size.** A 1,375-line roadmap covering five filings plus a full predecessor hand-off is
  the comprehension problem made physical. Comprehension scales inversely with batch size and
  nothing in the loop caps a batch.
- **Seven legal homes.** A thought arriving at the factory may legally live in the inbox, a cycle
  roadmap, the study register, the spike register, the platform ledger, a watch register, or the
  issue tracker. Filing correctly requires taxonomy expertise the filer does not have at the
  moment of noticing.
- **Cycles are named for their disease.** *proxy-claims*, *reachability*, *signal-integrity* —
  every cycle name states the diagnosis. No artifact names the cure in the language of the person
  who will use it, which is the same omission as (b) at the cycle's own title.
- **Completion depends on an exogenous event.** A cycle cannot finish itself when its checks are
  discharged by a live upgrade that may never run — so tails carry, and carrying is normal rather
  than exceptional. The ship-verifiable/field-contingent split (Arc 3 → Arc 4) fixed the *gating*
  half of this and left the *draining* half open.

## Assumptions this study challenged

- **"Ideation is unformalized because it is owner-steered"** (ruled 2026-07-12, and the premise
  `ideation-scaffold` opens with). Challenged: owner-steered work needs **more** format, not
  less — the format is what protects the owner's attention. Unformalized is what makes it opaque.
  This study does not overturn the ruling; it records that the ruling's cost is now measurable.
- **"An empty slot is honest."** Challenged: an empty slot is honest about the *record* and
  silent about the *decision*. Fourteen filled slots beside an empty Grouping section were
  perfectly honest and still produced a cycle whose scope was unruled.
- **"Provenance-by-location is worth the queue depth."** Challenged and rejected: the roadmap is
  already the authoritative record, so the inbox's location semantics buy nothing and cost
  legibility.

## Rejected alternatives

- **"The owner needs to read more carefully."** Rejected: the record is 1,375 lines and correct.
  A cause that resolves to *try harder* is a cause that has not been found.
- **"This is a capture-quality problem."** Rejected: Cycle 12's capture is unusually good — it
  ran two passes, took an owner challenge, regraded three filings and wrote its judgment calls
  onto the record. The comprehension failure happened *downstream of excellent grounding*, which
  is what makes it structural.
- **"`factory/studies/` already fixes this."** Rejected, and this is the sharpest cut: a study
  preserves a **diagnosis across cycles**; the missing artifact preserves a **decision context
  within a session**. The register solves the memory half of the problem, which is the half the
  loop was already good at. It is orthogonal, not overlapping.
- **"Add a comprehension gate."** Rejected: five skills already carry adoption gates, and a sixth
  set is the accretion `ST-2`/`ST-3` were written about. The repairs this cause implies are
  *shape* changes (a field, a directory rule, a grade), not new gates.

## What this session got wrong

- It first recommended filing the repairs into `factory/inbox/`. Wrong channel: the boundary is
  **delivery-not-topic**, `vlt-upgrade` delivers none of this to a vault, so every direction is
  platform-channel work. Corrected in session.
- It then recommended opening this study **before** checking the register's boundary table, and
  reversed itself on reading *"do not open one for how the factory itself works (that is a method
  note)"*. The reversal was then re-reversed on the descriptive-vs-causal cut recorded at the top
  of this file. Both reversals are on the record because the boundary is genuinely close, and a
  later reader deserves to know this entry was argued rather than assumed.
- It proposed applying the repair to Cycle 12's still-open slots mid-flight. The owner ruled
  against it — three of the directions touch `ideation-scaffold` and `build-brief`, which Cycle
  12 is mid-way through using, and a contract change against a half-filled skeleton risks a
  section that parses under neither shape. The ruling is correct and this study is filed under it.

## Disposition

**Nothing is actioned until Cycle 12 ships** (owner ruling, 2026-08-25). The cause is live and
the fix is deferred, which is precisely the condition under which the register README says a
diagnosis is *never excluded*.

Repairs this cause implies, in the order they were converged on — each to be argued on its own
merits when its channel opens, none authorized by this study, which gates nothing:

1. **`promise:` line per build** — queued as **P-16**. The cheapest repair for (b): one
   vault-facing sentence at ruling time, reused at acceptance and in the CHANGELOG.
2. **Inbox holds unclaimed only; filings migrate at capture** — repairs (d) directly.
3. **A seven-field ruling shape** (question, evidence `file:line`, options, clerk's read, default
   if silent, cost of being wrong, reversibility) — repairs (a) at its source, and is the
   precondition for any generated decision view.
4. **Ruling by exception** — repairs (c), and is a **reversal of a standing 2026-07-12 ruling**.
   It belongs to `roadmap-roundtable`, not to a queued platform item.
5. **A `NEVER-VERIFIABLE` acceptance grade** — lets a tail die rather than carry when no
   plausible event can discharge it.

## The sharpest acceptance test

The next time an ideation session runs, the owner should be able to answer, without opening the
roadmap: **what will be different in a vault after this cycle ships, and what am I risking if I
am wrong?** If that requires reading a 1,300-line record, this cause is still standing, whatever
has shipped against it.
