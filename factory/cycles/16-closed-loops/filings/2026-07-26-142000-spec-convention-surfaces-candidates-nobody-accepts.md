# Finding: the spec convention now has an advocate, and adoption is still zero — accepting a candidate has no beat

_Filed 2026-07-26 by the closing registrar during the Arc 3 `arc-closeout` run, converting build-15's
two perpetually-open first-exercise tails into a finding per the owner's batch ruling. **This is not
a "still waiting" note.** Eighteen days, five mints and two lint cadences have passed through the
convention without a single spec being authored; that is a result, and it is being reported as one._

## What was expected, and what the field did instead

Build-15 shipped the spec convention in v0.6.0 (2026-07-08) with two acceptance tails:

> hard gate honored — next vlt-core partner mint happens only with the convention in place and
> **exercises the consumer lock** (days-to-first-check = 0 for that boundary) … a live spec version
> bump produces **one relay per listed consumer** with the `_agent/specs/` path accepted.
> (`skills/reports/inbox-evolution-arc3-roadmap.md`, build-15 ledger item)

Neither has fired. The instructive part is *why*, because the obvious explanation was already tested
and refuted.

**The 07-13 diagnosis was "no advocate"** — no shipped surface could originate a spec
(`inbox/archive/2026-07-13-092341-spec-convention-has-no-advocate.md`). Grounding partly refuted it
(`vlt-upgrade:75`'s proto-spec retrofit *does* originate specs) and build-19 fixed the residual by
adding steady-state advocacy at **lint cadence** rather than upgrade cadence. **That fix works.**
Two `spec_candidate`s have since been surfaced unprompted, both human-gated, neither auto-promoted:

- `[2026-07-18 13:15]` lint — `spec_candidate: health-coach→chef nutrition spec`, filed to backlog.
- `[2026-07-25 15:05]` full lint — `creative→chess-coach spec candidate`, filed to backlog, against
  an `_agent/handoffs/` grown to 5 docs and an `_agent/specs/` holding 2.

A vault-side mint even reasoned about `{specs}` **on its own initiative** — the 07-18
`walkthrough-renderer` mint concluded a contract *"graduates toward a `{specs}` contract only if a
second producer adopts it"* (`_agent/mint/decision-log.md:526`), the first unprompted invocation of
the convention by a partner.

**And zero specs have been authored.** The two files in `_agent/specs/` arrived by the 0.7.0
`proto-spec-retrofit` migration (`git mv` of two existing handoffs, 2026-07-18) — retrofits, not
authorings. The consumer lock has never fired; no `version:` has ever bumped, so the relay has never
run.

## The finding: the missing step is *acceptance*, not advocacy or cadence

The convention is being **offered** at every lint cadence and **declined by default** — not by a
decision, but by the absence of one. A `spec_candidate` lands in a backlog. Nothing subsequently
asks anyone to act on it, and no surface reports that candidates are accumulating unaccepted. The
loop has a producer and no consumer.

Note what the richest possible probe did: the **Chess Coach `new partner` mint** (2026-07-16) — four
council rounds, all four lenses, cross-partner precedent deliberately set — passed straight through
the convention without touching it. The consumer lock could not fire because there were no specs to
consume, which is precisely the deadlock: the lock needs a spec, and authoring a spec has no
ceremony that would produce one.

**And the convention cannot report its own non-adoption.** `spec.md` declares
`deferral_metric: "spec version bumps shipping without their relay entries"` at threshold 1 — in a
vault with zero specs that metric **reads clean forever**, measuring adoption failure as success.
This is the arc's silent-zero scar, in the arc's own contract convention. `spec.md` is also one of
only two shipped conventions still at `enforcement_stage: declared`.

## Why this outlives Arc 3

Build-15's tails are conditioned on an owner-run partner mint and an owner-run version bump. The
owner has run five mints since the convention shipped and none produced a spec — so the trigger is
not rare, it is **not connected to anything**. Waiting for a sixth mint predicts the same result.

## Suggested shape (owner steers at ideation)

Candidate directions, not a design:

1. **An acceptance beat.** A `spec_candidate` in the backlog should have a named next owner and a
   promotion step, the way A4-3 gave adjudicable contradictions a route to Step 4 and a `Filed:`
   back-write that ends in the finding being gone. Today the candidate's terminal state is "still in
   the backlog."
2. **`adoption_first_instance:` on `spec.md`.** A4-2 wired the facet end to end and `spec.md`
   carries it as an explicit `null`. That null is now 18 days old and nothing reads it as a signal —
   worth checking whether the standing ledger surfaces a long-lived null, which is exactly the
   adoption axis build-20's facet was created for.
3. **Repair the `deferral_metric`.** A metric whose only attainable value at zero adoption is "fine"
   is the exact class A4-2's honest-reporting rule now governs
   (`vault-operating-contract.md:252` — *a count whose only attainable value is 'fine' must state
   what it cannot see*). `spec.md` predates that rule and does not conform to it.

## Honest limits

- All evidence is **vlt-core**. vlt-sayari is unreadable from this machine and sat at 0.6.0 and
  untouched since 2026-07-11; its spec adoption is unknown and could differ.
- Two specs *do* exist on disk, so mechanisms downstream of a spec existing (consumer lock, relay)
  are no longer blocked by an empty zone — they are unfired, which is a weaker claim than blocked.
- Nothing here says the convention is wrong. Build-19's advocacy fix demonstrably works; the gap is
  strictly at the accept-a-candidate step.

## Provenance

- Build-15 acceptance tails — `skills/reports/inbox-evolution-arc3-roadmap.md` (build-15 ledger
  item, with its full 2026-07-12 → 2026-07-25 annotation history); brief
  `skills/reports/build-15-spec-convention.md`.
- Advocacy fix — `skills/reports/build-19-spec-followup.md` (TICKED 2026-07-25).
- Superseded diagnosis — `inbox/archive/2026-07-13-092341-spec-convention-has-no-advocate.md` (A3-12,
  central claim overturned at capture run 2; archived at Arc 3 closeout with build-19).
- Silent-zero class — `inbox/2026-07-25-144500-revisit-after-has-no-adoption-path.md` and the
  contradictions/`deferral_metric` instances; general rule now at `vault-operating-contract.md:252`.
