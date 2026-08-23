# `adoption_first_instance:` is unreachable for any instance that doesn't arrive through `vlt-mint`

_Filed 2026-07-29 from **acceptance discharge run 2 + 3** (Arc 4 ledger, A4-2 observations,
2026-07-26/27). Drafted at run 2, widened at run 2's re-annotation, owner confirmed filing at
run 3. Evidence is vlt-core, read-only._

## The claim

The adoption axis (A4-2 / F6) declared `adoption_first_instance:` on conventions and gave it a
reporter (`vlt-upgrade` post-flight) — but its **only writer is `vlt-mint`'s ceremony**. Any first
instance that arrives by another road can never be stamped, so the axis reads *declared, no first
instance yet* indefinitely for conventions with live instances on disk. Two instances, two
different roads:

1. **Pre-existing instances (retrofit road).** `spec.md` reads `adoption_first_instance: null`
   while `_agent/specs/` holds **two** live specs
   (`2026-06-13-health-coach-to-chef-nutrition-spec.md`,
   `2026-06-21-creative-to-chef-meal-plan-format.md`, both from the proto-spec retrofit). The
   instances predate the axis; no mint will ever re-produce them.
2. **Non-mint first exercise (the sharper one — not a retrofit artifact).** `consult@1` had its
   first live exercise 2026-07-26 (two consults, `_agent/dispatch.md` 19:21) and
   `_meta/conventions/consult.md` still reads `null`. Here the axis shipped **first** and the very
   build that declared it produced the instance the same week — and the stamp still cannot fire,
   because a consult is not a mint. The vault's operator recorded why it stays that way
   (`_agent/sessions/2026-07-26-180500-lint.md`, Watches): editing the shipped base would trip
   `convention_base_divergence`, so it wants an overlay or an upstream fix, not a quiet edit.

## Grounding

- Writer: `skills/vlt-mint/SKILL.md` — the ceremony is the only site that writes
  `adoption_first_instance:` (A4-2 brief, F6).
- Reporter: `skills/vlt-upgrade/SKILL.md:105-112` — three-valued read, never a gate, never omitted.
- The A4-2 acceptance clause 5 promised *"the stamp is reachable"* — true for mint-borne
  conventions only.

## Why it matters

A reachability gap, not a retrofit gap: the axis's honest third value (*declared, no first
instance yet*) becomes **permanently dishonest** for any convention whose instances arrive outside
the mint ceremony — exactly the "declared-and-unexercised surface" smell the arc was built to
drain, now produced by the arc's own instrument. Wants either a second authorized writer (an
owner-ruled stamp beat somewhere on the consult/spec paths), or an explicit statement that the
axis measures mint-borne adoption only.
