---
id: 'ST-6'
slug: 'closed-rosters-meet-authorized-actors'
title: 'The module authorizes actors in one convention and enumerates them in another, so a closed roster routinely excludes an actor the surrounding rules make legal'
status: 'standing'
opened: '2026-08-26'
opened_by: 'capture (Cycle 14 inbox-capture, grounding A14-7) — owner-ruled open at Cycle 14 ideation Round 4, D4'
session: 'none — this study was written from the capture''s own grounding, not distilled from a working session'
causes:
  - 'Primary: authorization and enumeration are written in different conventions, by different authors, at different times — so a rule that GRANTS a capability broadly and a roster that ENUMERATES who holds it drift apart silently, and neither site can see the gap because each is locally correct.'
  - 'Secondary: a roster is written from the actors that exist when it is written, and its membership rule is stated as a property of those actors (\"consumers that are write ops\") rather than as a property of the capability. So the roster cannot admit an actor of a kind its author did not anticipate, even when the granting rule plainly covers it.'
  - 'Enabling: the module has no check that a grant and its roster cover the same population. Both halves pass every shipped net independently; the contradiction is only visible to a reader holding both files at once, which is exactly what single-home discipline discourages.'
cited_by:
  - 'factory/cycles/14-no-enforcement-point/roadmap.md §A14-7 (the instance that provoked this study — grounded 2026-08-26)'
  - 'factory/cycles/14-no-enforcement-point/roadmap.md §Ideation rulings D4 (the owner ruling to open it)'
  - 'factory/inbox/2026-08-21-150214-decision-log-writer-roster-admits-no-discovery-site.md (origin: mggower/bmad-module-vlt#6) — INSTANCE 2, still UNCAPTURED in the inbox. Recorded by the roundtable 2026-08-26 because its later capture grounds against module source, not studies, and would otherwise re-derive this cause from scratch — the exact failure D4 opened this study to prevent.'
  - 'factory/cycles/14-no-enforcement-point/roadmap.md §Roundtable review (2026-08-26) — the review found a FRESH instance in the cycle''s own plan: Q1''s structured PAGE_SCAN enum is fail-CLOSED where the residue rule it replaces was fail-OPEN, so a scanner meeting a schema break outside the enum''s roster must mis-file or drop it. Cured by requiring an explicit unclassified member (shipped precedent: `sources_vs_prose`''s `no_prose_section`).'
superseded_by: ''
---

# Closed rosters meet authorized actors

## The cause, as a claim

**The module states who *may* do a thing in one place and lists who *does* it in another, and
nothing checks that the two describe the same population.** The granting rule is written to be
open, because openness is the honest posture for a system that expects to grow. The roster is
written closed, because a roster's whole value is that it is checkable. Both are correct choices.
Together they produce an actor that the rules authorize and the roster cannot name — and because
each file is locally coherent, no shipped net sees it.

This is not a documentation slip. It is what happens when **permission is expressed as a
property** and **membership is expressed as a list**, and the two are maintained by different
conventions on different clocks.

## The instances

Three, live and grounded as of 2026-08-26. The first is the one that provoked the study.

**1. Layer 3's writer set vs the `verified_by` roster** (Cycle 14 A14-7, tracker #16).
`vault-operating-contract.md:66` draws Layer 3's boundary as an **entry condition, not a list of
doors**, and says so explicitly: the two shipped dispositions *"are the shipped set, **not** a
closed one: another verb filing an honest, attested document under the condition above is
legal."* One of the conditions it requires is the write-verification attestation pair.
`write-verification.md:47` then closes that pair's value set: *"the `verified_by` value set is
this file's `consumers:` **that are write ops**, plus write-op `local_consumers:` registrants …
The roster is **membership and ceiling**, never an automatic grant."*

A partner authoring a Layer 3 document during an ordinary sitting satisfies every other clause —
honest `author: agent`, an entitled `trust:` rung, a recognized `type:` — and then has no value it
may honestly put in `verified_by`. **A write the contract calls legal cannot satisfy the condition
of its own legality.** Measured in one vault: 27 such files across six partners' domains; 5
attested files, all five written by an operation skill; zero partner-sitting-written Layer 3
documents attested, and under the shipped value set none can be.

**2. The decision log's Writers roster vs a shipped write op mid-run**
(`factory/inbox/2026-08-21-150214-decision-log-writer-roster-admits-no-discovery-site.md`,
tracker #6, captured Cycle 10, still open). A shipped write op that legitimately discovers a
deviation mid-run has no route to the decision log, because the roster admits no discovery site.
Same shape, different register: the surrounding rules make the act legal and the roster has no row
for the actor performing it.

**3. The `type:` vocabulary** (Cycle 14 A14-6, tracker #15) — the same shape in a *vocabulary*
register rather than a *writer* register, which is why it is the weakest of the three and is
included with that caveat. `frontmatter.md:71` declares the `type:` list **non-exhaustive** and
names `research` canonical; `checks.md:19`'s `para_type_unknown` defines a **closed** recognized
set that excludes it. A file carrying `type: research` in PARA is simultaneously well-formed and a
loud finding. The grant is open, the enumeration is closed, and no site picks a winner.

## Why the enabling cause matters more than it looks

Each of the three pairs is **individually consistent**. `write-verification.md` is right that a
roster must be closed to be a ceiling. `contract:66` is right that Layer 3's boundary is a
condition rather than a door list. `frontmatter.md` is right that new artifact classes should not
need a contract edit. **Every one of these files passes every check the module ships.**

The contradiction is visible only to a reader holding both files at once — and **single-home
discipline, correctly, discourages exactly that.** The module's strongest structural rule (mechanics
live in one place; every other site carries a pointer) is what makes this class of defect
invisible: the two halves of one rule live in two homes by design, and no pointer between them
carries the obligation that their populations agree.

That is the durable finding. **The fix for any single instance is cheap and local; the reason the
class recurs is that the module has no way to express "these two sites must cover the same
population," and its best practice actively separates them.**

## What this predicts

Stated so a later cycle can test it rather than rediscover it: **every place the module pairs an
open grant with a closed enumeration is a candidate instance.** Two known, unexamined at the time
of writing:

- `para_author_unknown` (`checks.md:19`) closes `author:` to `human|agent|hybrid` with **no overlay
  escape at all** — a strictly tighter roster than the `type:` one beside it, which at least admits
  vault-declared schema. Named in Cycle 14's Q3 ruling as untouched.
- Convention `consumers:` lists generally. The version handshake requires bipartite consistency
  (every consumer listed ↔ every ack current), which is a *coverage* check between two sites — the
  only place the module already does what this study says is missing. **Worth reading as the
  positive precedent**: the handshake proves the check is expressible; nothing has generalized it
  beyond convention acks.

## Rejected alternatives

**"This is ST-1 with different files."** `ST-1`'s primary cause is one vault posture shipped as a
universal invariant, and its secondary is **permission fused to provenance in one verb**. That is
close — A14-7's Round 2 ruling explicitly cites it, choosing a class-based narrowing over a
writer-based one precisely to avoid re-fusing permission to provenance. But ST-1 bottoms out in
**one verb's shape**; this study is about **two sites failing to cover one population**, which is
present in registers that have no verb at all (instance 3 is a vocabulary, not an actor). Keeping
them separate; if a later session judges that wrong, this is the paragraph to argue with.

**"It is a documentation problem."** Two of the three instances were repaired in Cycle 14 by
editing prose, which makes this reading tempting. It is wrong for the reason the enabling cause
gives: the prose was never incorrect. Each site said what it meant. A documentation fix repairs an
instance and leaves the generator running.

**"Wait for a fourth instance."** Considered and declined at Cycle 14 D4. The register's own
documented failure mode is a cause re-derived because nobody thought to look — twice already
(ST-1 → ST-2 at five days; the 2026-08-24 session → ST-2's RC2 at one day). Three grounded
instances in hand is the cheapest moment this will ever be written.

## What this study's own session did not do

**No fix is proposed and none is implied.** Cycle 14 repairs instances 1 and 3 by local edits
(A14-7 narrows jurisdiction by artifact class; A14-6 adds a pointer), and those repairs are
correct for those instances. **This study does not claim they are insufficient** — it claims the
cause survives them, which is a different and weaker statement.

**The enabling cause is unmeasured.** "No check that a grant and its roster cover the same
population" is stated from three instances and one positive precedent (the version handshake), not
from a survey. Nobody has enumerated the module's open-grant/closed-roster pairs. That survey is
the obvious next move and was not run.

**Instance 3 is the weakest and is carried anyway.** A vocabulary register is not a writer roster,
and a later reader may reasonably cut it out. It is included because the shape held under
grounding, not because the session was confident.
