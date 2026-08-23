# A rule recorded as a trailing clause under an unrelated `ref:` is structurally unreachable — and nothing detects it

_Filed 2026-08-23. Evidence: relayed carry-back from vlt-core session vlt-core-d4
(the B10-9(3) contract-overlay mint act, commit `92a0e5d`), factory-verified against
the vault read-only (`_agent/mint/decision-log.md:989` clause-scoped supersession;
upgrade-ledger `:272`/`:282`/`:307`). Classification: **pattern** — a general shape,
proven by one live instance that misled a mint brief. Provenance: surfaced mid-act
when the mint's stated premise ("the standing instrument note does not exist") was
found FALSE and had to be restated._

## The shape

vlt-core's "standing instrument note" (byte-exact comparisons must bypass the rtk
`diff` wrapper) was cited by three consecutive upgrade-ledger entries as a standing
rule. It *did* have a written home — as a **trailing clause of the [2026-08-18]
convention-edit decision-log entry**, which is `ref:`-keyed to
`overlays/write-verification.overlay.md`. Because the decision log's read side is
ref-keyed (vlt-lint's read-before-flag, vlt-upgrade's reconcile pass resolve entries
*by governed object*), a rule shelved as a trailing clause under an unrelated object
can never be surfaced by subject. Every session that honored it was re-deriving it
from ledger archaeology; a factory session searching for it concluded it didn't
exist.

## Why this is module signal, not vault hygiene

- The decision log's own machinery (ref-keyed reads) is what makes the mis-shelved
  clause invisible — the better the ref discipline gets, the more invisible a
  trailing off-subject clause becomes.
- Nothing detects the shape: no lint class flags an entry whose prose states a rule
  about a subject other than its `ref:`.
- The local discharge (a clause-scoped supersession into a proper home, per the
  Supersession idiom) worked — but only because a council happened to find the
  clause. Detection stayed human.

## Candidate directions (for capture, not answered here)

Either a decision-log discipline rule ("one entry, one governed subject; a rule
about another subject gets its own entry or its own home") recitable at write time,
or a lint heuristic over entries whose body names a governed surface absent from
their `ref:`. The write-time rule is cheaper and matches the existing
declare-at-birth posture.
