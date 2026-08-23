# Defect: vlt-core's two oldest verticals declare loop profiles inline — build-11's location shipped without a migration

_Filed 2026-07-17 from `vlt-core` (owner-observed, during the Arc 3 acceptance-discharge run).
This is the **build-11 field defect the Arc 1/2 watch item anticipated**, now confirmed at rest.
The watch item has ridden three arcs as a prediction; this filing closes it as an observation._

## The observation

`vlt-track/SKILL.md:16` is unambiguous about where the loop profile lives:

> The varying machinery — where the working record lives, where the polished protocol lands,
> whether there's one subject or many, and which data streams the log keeps — is read from the
> **loop profile** the partner declares in its own **`capabilities/track.md`** (the heavy
> `skill: vlt-track` capability pointer, under a *Loop profile* block). **This skill reads that
> profile from the invoking partner; it hardcodes none of it.**

vlt-core's two oldest vertical partners do not have that file. They do not have the directory:

- `_agent/partners/dog-trainer/` — `identity.md`, `thread.md`. **No `capabilities/`.**
  The profile is declared **inline in the shipped skill body** at
  `.claude/skills/vlt-agent-dog-trainer/SKILL.md:41` — *"**Loop profile** (what you hand `vlt-track`):"*
- `_agent/partners/health-coach/` — same shape. **No `capabilities/`.**

The vault's newest vertical, minted 2026-07-16, has the correct shape —
`_agent/partners/chess-coach/capabilities/track.md`, frontmatter `procedure: { skill: vlt-track }`,
`weight: heavy`, with a full `## Loop profile` block. So the location works when a mint lands after
the convention. It is the **pre-build-11 partners that never moved**.

The vault's own mint record names this independently. From the Chess Coach entry
(`_agent/mint/decision-log.md`, 2026-07-16), in the *Precedent this mint SETS* section:

> **Standing anomaly (not this mint's):** those two declare loop profiles inline in SKILL.md
> contra `vlt-track/SKILL.md:16` — *they* are the drift.

## Why this is module signal, not vault cleanup

Build-11 shipped the `capabilities/track.md` location and `vlt-track`'s read-the-profile-from-the-partner
contract. It shipped **no migration** for partners minted before it, and **no detection** that would
notice a vertical partner with a heavy `vlt-track` pointer and no profile in the contract-specified
place. The two affected partners predate the convention by design — nothing in the module ever asked
them to move, and nothing has told anyone they didn't.

The failure is silent in both directions:

- `vlt-track` "hardcodes none of it" — so on a `dog-trainer`/`health-coach` track loop it has no
  profile to read at the place it reads. Whether it then improvises from the SKILL.md prose in context,
  or asks, or writes to a guessed root, is **unobserved** (see the honest limit below).
- `vlt-lint`'s convention-coherence and capability checks have no notion of *a heavy capability pointer
  that should exist and doesn't*. A partner missing its `capabilities/` dir entirely reads as clean.

This is the same shape as the 2026-07-13 spec-convention filing (`…-092341-spec-convention-has-no-advocate.md`):
a well-specified location whose adoption nothing measures. There the class-count was zero; here the
adopters are two-of-three-short. Both are **adoption gaps invisible to a violation-shaped check** —
worth weighing together at capture.

## The honest limit on this evidence

**No track loop has actually run on `dog-trainer` or `health-coach` since 0.4.0.** The watch item's
literal trigger — *"first post-0.4.0-upgrade track loop … may not find the inline loop profile → if it
breaks"* — has not fired, because the event hasn't happened. What is established here is the
**precondition, at rest, in the vault's file tree**, plus the vault's own mint council independently
calling it drift. The break itself is predicted, not measured. Capture should treat the *divergence*
as confirmed and the *runtime consequence* as still unobserved.

Counter-consideration worth recording: the same decision-log entry rules that
**"Dog Trainer / Health Coach have NO defect and need NO migration"** — but that ruling is scoped to the
**gate-slot licensing rule** (the chess-coach precedent about which clause occupies the gate slot), *not*
to the loop-profile location. The two findings sit in the same paragraph and must not be conflated: the
gate-slot rule genuinely doesn't affect them; the profile location does.

## Directions for the capture to weigh (not a chosen fix)

- **A `vlt-lint` check** — a partner whose SKILL.md invokes `vlt-track` (or whose roster row is a
  vertical) with no `capabilities/track.md` carrying a `## Loop profile` is drifted. Detection-shaped,
  composes with the existing capability/coherence passes, and would have caught this the day build-11
  shipped. Cheapest honest answer.
- **A `vlt-upgrade` migration offer** — human-gated and idempotent, in the build-15 retrofit-scan
  tradition (which already has field evidence on vlt-sayari: scan surfaced one candidate, offered it,
  owner declined, nothing moved). Lift an inline *Loop profile* block into `capabilities/track.md`,
  leave the SKILL.md prose pointing at it. Fits the existing rail; costs an upgrade-time beat.
- **A `vlt-mint` migrate-a-capability kind invocation** — the kind already exists; this is arguably just
  two overdue uses of it. Answers "how" but not "who notices", so weakest alone — the same objection the
  spec-advocacy filing raises against its own mint-kind option.
- **The general form** — is *"a shipped location with no adoption check"* a recurring class? Two
  instances in five days (spec creation, loop-profile location). If frontmatter@3's enforcement
  declaration grows an adoption/first-instance facet (the open question in the 07-13 filing), this
  defect is an instance of it and should be captured against the same answer.

## Grounding notes (checked 2026-07-17)

- Contract that names the location: `skills/vlt-track/SKILL.md:16` (module source, v0.6.0).
- Template for the block: `skills/vlt-mint/assets/capability-template.md` (*Loop profile* section,
  added in 0.4.0 for shared longitudinal-loop ops).
- Live drift (vlt-core, 0.6.0): `_agent/partners/{dog-trainer,health-coach}/` — `identity.md` +
  `thread.md` only, no `capabilities/`; inline declaration at
  `.claude/skills/vlt-agent-dog-trainer/SKILL.md:41`.
- Correct shape, same vault: `_agent/partners/chess-coach/capabilities/track.md` (minted 2026-07-16).
- Vault's own naming of it: `_agent/mint/decision-log.md`, 2026-07-16 Chess Coach entry,
  *Precedent this mint SETS* → *Standing anomaly*.
- Machinery half (for contrast — the location works in anger): `vlt-sayari`'s Navigator carries a
  complete `## Loop profile` driving 6 real project loops — per
  `inbox/2026-07-12-114940-sayari-060-upgrade-field-evidence.md` §2/§3.

## Provenance

- Vault: `vlt-core`, 0.6.0 (upgraded 2026-07-08 17:45).
- Surfaced during the 2026-07-17 acceptance-discharge run, re-checking the Arc 1/2 loop-profile watch
  item carried into the Arc 3 ledger. Owner ruling this run: file it as a build-11 field defect rather
  than tick the item as vault-side cleanup.
- Ledger disposition this run: the watch item's **machinery half is DISCHARGED** (vlt-sayari's Navigator
  + vlt-core's chess-coach both wear the profile in the shipped location); the **wearer half converts
  from a prediction to this filing**. The item should not ride a fourth arc as a watch.
- Natural home: Arc 3 capture (it discharges a carried ledger item and pairs with the 07-13 adoption-gap
  filing), or wherever the adoption-metric question lands.
