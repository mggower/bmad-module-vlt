# No seam returns a worked result to a caller who keeps the wheel — a one-fact gap costs a second session

_Filed 2026-09-16 by the **factory**, from an owner problem-solving session (`bmad-cis-problem-solving`)
and a same-day roundtable (`bmad-party-mode`); session artifact gitignored. Evidence is module source at
`caea0d5`. Kind: `candidate`. Cause: **`ST-9`**
(`factory/studies/ST-9-one-axis-design-leaves-the-diagonal-empty.md`, cause A) — cited, not restated.
Companion: `2026-09-16-094501` (the lane half). Owner elected to file._

## The claim

The contract's cross-partner mechanisms were designed on one axis — *does the wheel move?* — and the
cell *work moves, wheel stays* is empty. Consult "transfers **nothing**" and routes `needs-work` to a
handoff doc + relay; relay lands on the recipient's next orient, a later sitting; hand-off "ends one
sitting and begins another". A partner mid-task that needs knowledge the vault does not hold has only
the slow diagonal, so a task needing one external fact spans ≥2 sessions. The owner's field report is
exactly that.

## Grounding (module source, `caea0d5`)

- **Consult is read-only by identity.** `{conventions}/consult.md`: "A consult transfers
  **nothing**." `skills/vlt-dispatch/references/consult.md`: "It is read-only except its own memory
  … *Consult answers; relay assigns.*" Its routing: "`needs-work` → the caller writes the handoff doc
  and fires the existing **`relay`** path."
- **Relay is asynchronous by identity.** `vault-operating-contract.md:288–291` — a durable doc "has
  no pickup unless the recipient is *told it's waiting*"; the recipient "drains it via the ordinary
  pickup loop on its next orient."
- **Hand-off moves the wheel.** `:267` — "A hand-off to another partner **ends one sitting and
  begins another**." Partner SKILLs' *Partner-invoked* mode (`vlt-agent-researcher/SKILL.md`, Modes)
  orients "to the payload, not the user" — the caller is gone.
- **The engine shape that would fill the cell already exists.**
  `skills/vlt-setup/assets/workflows/vlt-consult.js`: one spawned agent, typed return union forced by
  schema, "depth-1 is STRUCTURAL … a spawned agent cannot re-enter a workflow." The lite boot
  (filing `2026-07-29-082931`, shipped) is engine-owned.
- **The op is delegable as-is.** `skills/vlt-research/SKILL.md` runs headless ("research X"), tags
  "the active partner", writes no session note, checkpoints a `.WIP.md` on interruption, and offers
  the Librarian hand-off in Phase 6 (which a spawned runner must **not** take — depth-1).
- **Governance carriage for a partnerless runner is an open Cycle 16 item.**
  `factory/cycles/16-closed-loops/roadmap.md` §A16-3 (ST-8 cause C; `S-4` proposed on whether
  `CLAUDE.md` imports load for a sub-agent). A delegate runner is an instance of that carrier, not a
  second one.

## Specimen manifest

Count only — the owner's report of multi-session task closes; no instrument persists the set. The
minimal triggering fragment is the consult mode's routing line quoted above: `needs-work` has exactly
one documented destination, and it is the slow path.

## Candidate dispositions (for capture to rule — not pre-empted here)

1. **Draw the axis in the contract.** *Sessions, sittings, and hand-offs* publishes the 2×2 (moves
   work? moves wheel?) and names the fourth timing: **delegate** — transfers bounded work, not the
   wheel; crosses no sitting boundary; no session note from the runner.
2. **Population cut, not enumeration (Arc 9 D5).** Delegate may target only ops whose write target
   is **not a shared lane** — for a single-writer lane the wheel *is* the authority, and hand-off
   stays the only route in. v1 tenant: `vlt-research`. The contract states the rule; the mode
   states the tenant.
3. **`vlt-dispatch` mode `delegate`** (`references/delegate.md`, single home for mechanics; engine
   `vlt-setup/assets/workflows/vlt-delegate.js` cloned from `vlt-consult.js`, `depends_on` acked
   per E5). Inputs: `op` (v1: `research`), `question`, `depth` (`quick|moderate`), `groundIn`,
   `why`, `fromSlug`. Return union: `done{notePath, headline, verification, wikiCandidate}` |
   `incomplete{wipPath}` | `insufficient-context` | `needs-human` | `too-big`. `deep` → `too-big`
   → relay (a deep dive is a sitting's worth of work). The runner **never** offers or performs the
   Librarian hand-off; the caller relays on `wikiCandidate`. Never unprompted; a human may invoke
   it directly for debugging, as `consult` allows.
4. **Runner is partnerless, always.** No `remember:` variant (rejected at the roundtable: the caller
   would decide another partner's memory from outside; the vault remembers by filing the note, and
   the Researcher's Phase 2 vault check / Beat 2 log read find it). Attests
   `verified_by: vlt-research` (legal — companion filing). **Governance carriage is A16-3's**: the
   engine prompt *points at* the rule-card and the vault rung, never copies; the runner honours the
   op's overlay/local-convention reads. **Sequence with or after A16-3** — never a second carrier.
5. **Record.** Pre-checked `delegate:` block in `_agent/dispatch.md` (traffic, never on the ledger
   by construction — same as `consult`); **two** `{log}` lines — `dispatch (<caller>) | delegate: …`
   and the op's own `research (<caller>) | …` — both tagged with the **caller** (the engine passes
   `fromSlug` as the active partner; a `(none)` tag fails the gate); no session note; the note
   carries no `partner:` field (true today for every research note — the log line is the
   attribution; do **not** touch `frontmatter@14` for this).
6. **Redirect the trapdoor.** Consult mode's `needs-work` routing → "delegate if bounded, relay if
   not"; `consult.md`'s neighbour list gains delegate. Clarifications — `consult@1` consumers'
   behaviour unchanged; the brief verifies bipartite consistency.
7. **Pointers only** in partner SKILLs (Creative `:37`; companion filing), the rule-card *Sessions*
   row, `module-help.csv` (quoted fields), `CHANGELOG`.

Dissents on record (roundtable): Victor — generalize `op` beyond research now (rejected by the
population cut; a second tenant is a separate ruling). Sally — an orphaned `.WIP.md` from an
interrupted runner has no decay contract (true today for headless; `incomplete{wipPath}` makes it
visible; **watch**, not build).

## Acceptance (proposed)

Ship-verifiable at rest, against a temp-vault fixture: exactly one agent spawned; typed return
honoured on a thin payload (`insufficient-context`), on `deep` (`too-big`), on a real quick dive
(`done`) and on a forced interruption (`incomplete`); one `delegate:` block written pre-checked and
absent from `ledger`; two caller-tagged `{log}` lines; no session note; the note passes tier-1 and
carries `verified_by: vlt-research`; the runner wrote nothing under `{wiki}` and fired no relay.
Prose agreement by grep: contract 2×2, consult routing line, `consult.md` neighbour list, rule-card
row. Field-contingent (watch): first live `delegate:` block in `{field-vault}` from a non-Researcher
partner; open relay pointers to `researcher` from other partners fall toward the `deep`-only residue.
