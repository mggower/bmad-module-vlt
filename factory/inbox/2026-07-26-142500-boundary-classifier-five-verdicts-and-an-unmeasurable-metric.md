# Finding: the boundary bell is live, correct, and has never rung — and its acceptance metric cannot be measured by anyone who has no reason to create a boundary

_Filed 2026-07-26 by the closing registrar during the Arc 3 `arc-closeout` run, converting build-16's
perpetually-open first-exercise tail into a finding per the owner's batch ruling. The tail has
survived five mints and four discharge passes; that pattern is the report._

## The metric, and why it has not moved

Build-16 shipped the boundary classifier — 091004's doctrine made mechanical: no boundary-creating
mint without a declared enforcement stage or a tripwired, expiring deferral. Its acceptance clause:

> next boundary-creating mint has **days-to-first-check = 0** and zero conventions sit `declared`
> untripwired
> (`skills/reports/inbox-evolution-arc3-roadmap.md`, build-16 ledger item)

Five classifier runs since the 0.6.0 upgrade. **Five `non-boundary` verdicts:**

| Date | Mint | Verdict |
|---|---|---|
| 2026-07-12 | add a capability — `file-module-feedback` | `non-boundary` |
| 2026-07-16 | **new partner** — Chess Coach | `non-boundary` |
| 2026-07-17 | atlas mint brief | `non-boundary` |
| 2026-07-18 | capability-refine — answer-key | `non-boundary` |
| 2026-07-18 | add a capability — `walkthrough-renderer` | `non-boundary` |

**Each verdict is substantively correct** — four capability adds/refines binding only their owning
partner's own zone, plus one new partner whose subject bound no other partner. This is not a
misfiring gate.

**And the gate is reachable**, re-verified at source on 2026-07-25 rather than assumed:
`vlt-mint/SKILL.md:59` names `convention edit` and `new partner` among the gated kinds, and `:42`
runs the classifier on **every** kind, with `:94`'s fixed `kind → council` map selecting the panel.
A shipped surface can produce a boundary-creating verdict today.

So: live, reachable, correct, never rung.

## The finding: the metric is conditioned on an event the vault has no reason to produce

`days-to-first-check = 0` is measurable **only** on a boundary-creating mint. A vault produces one
when it needs a new governing rule — and vlt-core, whose owner *is* the module owner, is
structurally steered away from ever needing one. `vlt-mint/SKILL.md:150` states an overlay *"can
only add; it cannot change an existing base rule. So a true rule change has **no overlay form**"*,
and directs generic rule changes to be *"filed upstream to the module"* — which for this vault is
the cheaper path. The same reasoning the ledger already recorded for build-18 F3 and build-21 A3-14
applies here: **the precondition is counter-incentivized, not merely absent.**

An acceptance check that can only discharge on an event the module actively discourages is not a
pending measurement. It is a check aimed at the wrong vault.

## The second half, which is the part actually worth acting on

The one **new partner** mint — the richest probe the vault has ever run, four council rounds, all
four lenses convened — reached `non-boundary` **only after two wrong answers by inference, both
caught by the council rather than by the classifier itself** (`_agent/mint/decision-log.md`,
2026-07-16):

1. A `non-boundary` resting on a **false premise** — `consumers:` read as an authorization, when
   `extraction.md:47`'s grant names no op.
2. A **fabricated root cause** — a claim that an upgrade had "eaten" the extraction registry table,
   when the table had been retired by owner ruling and the durability mechanism had worked
   correctly.

Blast radius before the council caught it: a convention overlay and a module bug report accusing the
module of a bug that never happened, both withdrawn. Root cause was a governance single-home
violation (the repeal reached only `upgrade-ledger.md:48`, never the decision log) and is separately
filed and since fixed by build-21's decision-log write-through.

But the standing caution remains, and it is what makes the tally worth reporting: **the classifier's
reliability is unestablished.** Five correct verdicts is weak evidence when the one hard case needed
two human corrections to reach its correct answer, and when every easy case (capability add, own
zone) is one the classifier could get right by always answering `non-boundary`. The current evidence
cannot distinguish *"correctly declining"* from *"biased toward silence."*

## Suggested shape (owner steers at ideation)

1. **Split the acceptance claim.** *"The gate is live, reachable, and reasons correctly"* is
   measurable and has five data points. *"days-to-first-check = 0"* needs an event no known vault
   will produce. These should never have been one checkbox, and the general fix — tagging each
   acceptance check ship-verifiable vs field-contingent at brief time — is the arc-closeout lesson
   below.
2. **A discriminating probe.** The cheapest way to distinguish correct-decline from
   biased-to-silence is a `convention edit` mint against a rule the vault genuinely wants, or a
   deliberate fixture case with a known-boundary subject. Neither exists today.
3. **Consider reporting the streak.** Five consecutive `non-boundary` verdicts is a signal no
   surface currently surfaces. Under A4-2's honest-reporting rule
   (`vault-operating-contract.md:252` — a count whose only attainable value is 'fine' must state
   what it cannot see) a bell that has never rung arguably owes the reader that fact.

## Honest limits

- All five verdicts are **vlt-core**. vlt-sayari is unreadable from this machine, untouched since
  2026-07-11, and its classifier history is unknown.
- Each verdict was independently assessed as substantively correct during discharge passes; this
  filing does **not** claim any of them is wrong.
- The convergence half of build-16's clause is separately and strongly discharged — the 2026-07-25
  full lint found 7 conventions pristine vs `.baseline`, every consumer pin current, zero coherence
  findings, no overlays, all 11 capabilities lane-safe. Only the `days-to-first-check` half is at
  issue here.
- 091006's first-review-cycle evidence rides build-16's item but is a **dated clock**
  (`spec.md`'s `review_after: 2026-08-17`) and is unaffected by this filing — it will fire on its own.

## Provenance

- Build-16 acceptance clause and full verdict history —
  `skills/reports/inbox-evolution-arc3-roadmap.md` (build-16 ledger item, annotations 2026-07-12 →
  2026-07-25); brief `skills/reports/build-16-frontmatter3-bell-attestation-freshness.md`.
- Doctrine — `inbox/2026-07-06-091004-no-boundary-without-a-bell.md`.
- Reachability at source — `skills/vlt-mint/SKILL.md:42`, `:59`, `:94`; overlay/upstream steering at
  `:150`.
- The two wrong answers — `_agent/mint/decision-log.md` (vlt-core, 2026-07-16 Chess Coach entry);
  root cause filed as `inbox/2026-07-17-090500-upgrade-rulings-never-reach-the-decision-log.md`.
