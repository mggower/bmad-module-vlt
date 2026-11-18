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

## Addendum — 2026-08-27, factory-side re-grounding (evidence strengthened, claim unchanged)

_Surfaced by the owner reading `vlt-upgrade`'s post-flight after the v0.16.2 upgrade
(`_agent/upgrade-reports/2026-08-27-0947-upgrade.yaml`): "consult declared 32 days with no first
instance? i have definitely used consult a number of times." Re-derived against vlt-core, read-only.
The original claim holds unchanged; three facts make it sharper._

1. **Four instances now, not two.** `_agent/dispatch.md` carries `consult:` blocks at
   `2026-07-26 19:21` (librarian → chef, ×2 — the pair this filing already named),
   `2026-08-18 13:28` and `2026-08-19 10:55` (both career-strategist → creative).
   `_meta/conventions/consult.md` still reads `adoption_first_instance: null`. The convention's own
   definition of the record (*"a dated `consult:` block in `_agent/dispatch.md`"*) is satisfied four
   times over, so the correct value is `2026-07-26` and has been for a month.

2. **The dishonest window is measured, not predicted.** This filing said the axis reads *declared,
   no first instance yet* "indefinitely". The 2026-08-27 post-flight renders
   `"consult: declared, no first instance yet (created 2026-07-26 — 32 days)"` — and the
   parenthetical age is the instrument reporting the size of its own error.

3. **The sharpest instance: `vlt-lint` enforced the convention and the axis still says
   unadopted.** The first 2026-07-26 consult exists *because* a lint run raised `consult_missing`
   and the vault closed it by having the consult — recorded in the relay at `dispatch.md:188`
   (*"Surfaced by a retroactive consult (2026-07-26) closing a `consult_missing` lint finding — the
   spec bound the Chef and never asked him"*). So the enforcement point fired, the convention was
   honored on its own terms, and the adoption axis reports it unexercised. **That is the Cycle 14
   through-line — a rule the module states, a place named responsible for it, and that place unable
   to carry out the judgment the rule requires — arising inside the instrument built to measure
   adoption.** It also means the two dispositions this filing offers are not equivalent: "the axis
   measures mint-borne adoption only" would have to explain why a lint-enforced consult is not
   adoption.

_Uncaptured as of 2026-08-27 by the Cycle 14 scope ruling (defects and blockers from Cycles 12–13
only; net-new deferred). Candidate for Cycle 15 capture — this addendum exists so the evidence is
not re-derived then._
