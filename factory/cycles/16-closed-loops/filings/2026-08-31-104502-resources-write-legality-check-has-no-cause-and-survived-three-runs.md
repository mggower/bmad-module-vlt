# A check nothing causes: the `{resources}`-write legality tail survived three discharge runs unfired

_Filed 2026-08-31 from **Cycle 14's third acceptance-discharge run**, on the owner's ruling that
pass 1's own third-run instruction has come due. This filing is about a **check**, not a module
defect — the acceptance instrument, not the thing it measures. Evidence is `{field-vault}`,
read-only; nothing in the vault was edited._

## The tail

Cycle 12's build-3 check (7): *a partner resolving a `{resources}`-write legality question from the
rewritten bundle **without escalating*** (`factory/cycles/12-proxy-claims/roadmap.md:2896-2902`,
`:3082-3088`). Released as a standing watch at Cycle 12's closeout with the instruction *"re-read it
after Cycle 14 build-3, against a bundle that is no longer waiting on itself."* Recorded on Cycle
14's ledger by build-3's brief (roundtable A25) so closeout could not silently drop it.

## What has happened since

**The precondition is met and has been met for four days.** Build-3 shipped in v0.17.0 on
2026-08-27; both rulings the live parks were waiting on are in force, so an escalation would no
longer be the bundle's fault. `{field-vault}` has since taken the 0.17.1 hot-fix.

**The event has never occurred, across three discharge runs:**

| run | date | verdict | reason |
|---|---|---|---|
| pass 1 | 2026-08-27 | STILL-OPEN | precondition met, no observation on disk |
| pass 2 | 2026-08-27 | untouched | nothing new bore on it |
| this run | 2026-08-31 | **BLOCKED — filed** | third run unfired; pass 1's own instruction |

**And ordinary activity of the surrounding kind has run repeatedly without touching it.** Since the
0.17.1 upgrade `{field-vault}` has taken at least eight `{resources}` writes — five wiki pages
rewritten by the 2026-08-30 lint sweep's own fixer, three brief issues written into
`resources/briefs/` on 2026-08-31 — across multiple partner sessions
(`_agent/sessions/` 2026-08-28 through 2026-08-30, spanning misc, extract, lint and groom lanes).
No session record contains a `{resources}`-write **legality question**. The flow ran; the surface
under test was never reached.

## Why it is filed rather than re-annotated

Pass 1 wrote the trigger itself: *"If it survives a THIRD discharge run unfired, that is no longer a
waiting state and the honest reading is that nothing will ever cause it — re-grade it BLOCKED and
file it then."* Pass 1 also recorded, correctly, that the event is **reachable** in the literal
sense: the owner can open a partner session and pose the question at any time. Both are true, and
the tension between them is the finding.

The check does not need a *trigger*; it needs a **cause**. Nothing in a build, a release, or an
upgrade produces it — the item says so itself, tagging it `[field-contingent]` and naming it the
unbounded species at `brief-anatomy.md:203-210`. What it waits on is the owner performing an
artificial session whose only purpose is to make the check fire. A check dischargeable only by
staging its own evidence is not observing the field; it is asking the field to pose for it. Three
runs is enough evidence that ordinary use will not supply it.

## The generalizable shape

An acceptance check of the form *"a partner does X spontaneously, and the owner observes it"* has
no cause in the loop. It is distinguishable from a legitimate field-contingent check — *"the next
mint exercises the consumer lock"*, *"the next full sweep reports N"* — because those name an event
the owner **already performs on cadence** for reasons of their own. This one names an event that
exists only to be the evidence.

Cycle 14 amended its own ruling D3 to say a **bounded** check is ship-verifiable and gates, where a
bound is *at rest, at the release gate, or on the next ordinary upgrade*. The load-bearing word is
**ordinary**. This check has no bound of any of those three kinds, and it also has no ordinary
occasion. That gap — a check that is neither bounded nor caused by anything the vault does anyway —
is what has no name in the brief vocabulary today.

## Candidate directions (not a fix — capture's call)

1. **Give the vocabulary a third grade.** Alongside `[ship-verifiable]` and `[field-contingent]`,
   name the species whose event has a trigger but **no cause** — and rule at brief time that such a
   check may not be written, the way the unbounded species is already discouraged at
   `brief-anatomy.md:203-210`. The rubric's BLOCKED grade exists for events with no trigger; this
   is the adjacent case it has no word for.
2. **Re-express the underlying question at rest.** What Cycle 12 wanted to know was whether the
   rewritten bundle *answers* the `{resources}`-write legality question without sending the reader
   elsewhere. That is gradeable at rest against the bundle — read it as a partner would and see
   whether the answer is present — and does not require a partner to volunteer.
3. **Retire it.** Its substantive premise is satisfied: both blocking rulings shipped, and the
   bundle is no longer waiting on itself. If (2) is not wanted, ruling the watch discharged on the
   precondition and closing it is more honest than a fourth carry.

## Disposition on Cycle 14's ledger

Graded **BLOCKED (unreachable)** this run and annotated as such. It is `[field-contingent]` and does
**not** gate, so Cycle 14's closeout distance is unchanged by it. It is filed here so the gap
becomes capture's material rather than a fifth carry-forward.

_Factory-side signal: this concerns how acceptance checks are written, not shipped module behaviour.
Its directions land in the brief vocabulary (`brief-anatomy.md`) and are cousins of platform
**[P-20]**, the check adversary._
