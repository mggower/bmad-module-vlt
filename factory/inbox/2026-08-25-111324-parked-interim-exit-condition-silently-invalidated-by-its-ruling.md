# A parked interim's exit condition is a claim about a rule that can change underneath it

_Filed 2026-08-25 by the owner, on field evidence from `{field-vault}`'s mint decision log
(verified against the file, not recalled). Classification: **hazard — general**, one instance
observed. Related: the two PARA/rail filings of the same date._

## The hazard

When a vault hits an upstream blocker, the sanctioned posture is to **park a deliberate,
reversible interim** and file for a ruling. Good practice — and `{field-vault}` followed it
exactly: it parked a partner's output in the agent zone, filed the ruling request, and wrote
down its own **exit condition** so the unwind would be mechanical when the ruling landed.

The recorded exit was, in substance, *"one `git mv` plus one structure-map value"* — true under
the reading of the blocker the vault held at parking time (the blocker is about **which zone**).

The ruling then shipped under a **different** reading (the blocker is about **which surface**).
The exit condition was not merely unmet — it became **wrong**, and nothing said so.

## Why this is worse than an unmet exit

An unmet exit is visible: the vault checks, sees the condition unsatisfied, and waits. An
**invalidated** exit is invisible and reads as satisfied:

> Anyone reading that decision-log entry after the release sees "ruling landed, one-line exit,
> pre-authorized" — and executes a move that is now **illegal** under the shipped rules.

The record's confidence is inherited from the moment it was written; the rule it depends on has
moved since. The vault has no signal, because the interim's own record is the only place the
dependency exists, and rulings do not read vault-local decision logs.

Generalized: **a dated interim's stated exit condition is a claim about a rule that has since
changed underneath it.** Every parked interim carries this exposure. The more careful the vault
is about writing a precise, mechanical exit, the more precisely wrong the record becomes when the
ruling reframes the problem.

## The fix direction

The vault side and the module side both have a move; ideation should rule which (or both).

**Module side — make the ruling carry the obligation.** When a ruling answers a filing that a
vault parked against, the shipped record should state **what it changed about the framing**, not
only what it changed in the rules. A ruling that re-reads the problem (zone → surface) is
materially different from one that answers the problem as asked, and only the former invalidates
downstream exits. Candidate: a ruling that reframes carries an explicit *"if you parked against
this, re-derive your exit"* note in the CHANGELOG entry — the same shape as the v0.12.0
field-facing posture note, which is precedent that this rail exists and works.

**Vault side — make the exit re-derivable rather than recorded.** Guidance (shipped in whichever
skill owns interim posture) that an exit condition should record **the blocker's shape and the
filing reference**, not a pre-authorized command sequence — so the unwind is re-derived against
the rules in force at unwind time rather than replayed from a stale claim.

**Preference:** the module-side move is the stronger of the two, because it does not depend on
every vault having read the guidance. The vault-side move is cheap and can ride along.

## Scope note

Filed as a **hazard with one observed instance**, not as a defect with a known blast radius. What
is unknown, and worth a question at capture: how many parked interims exist across live vaults,
and whether any others were invalidated by Cycle 11's rulings without anyone noticing. The
mechanism guarantees silence, so absence of reports is not evidence of absence.
