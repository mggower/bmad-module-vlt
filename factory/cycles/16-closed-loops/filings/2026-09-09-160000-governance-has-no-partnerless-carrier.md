# Governance has no partnerless carrier — a session without a partner reads a paragraph, not the rules

_Filed 2026-09-09 by the **factory**, from an owner problem-solving session on the partner model
(`bmad-cis-problem-solving`; session artifact gitignored). Evidence is `{field-vault}` read-only plus
module source at `5ca31f0`. Kind: `candidate`. Cause: **`ST-8`**
(`factory/studies/ST-8-always-read-memory-has-no-budget-and-no-owner.md`, cause C) — cited, not
restated. Owner elected to file._

## The claim

The act-blocking rules reach a session **only through the partner activation ritual**. A session in a
vault with no partner summoned — which the owner now runs deliberately, and reports as the most
productive shape for brainstorming — receives exactly one paragraph of governance: the `CLAUDE.md`
pointer `vlt-setup` seeds. It never reads the rule-card, never reads the vault rung, and has no name
in the contract's sitting model, so it writes no session note and leaves no log tag. The owner's word
for it is *lawless*.

The operations are **not** the gap. `vlt-ingest`, `vlt-lint`, `vlt-query`, `vlt-extract` all run
partnerless today (`skills/vlt-ingest/SKILL.md:24` — "If invoked standalone with no partner, omit the
tag"). What is coupled to the persona is the *carriage*: who reads the rules, and who owns the sitting.

## Grounding (module source, `5ca31f0`)

- **The rule-card read is a step of the ritual, nowhere else.** The contract's *Activation ritual*:
  "Every partner, on activation, **first loads the rule-card**"
  (`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:194`). No other actor is
  instructed to read it; the card's own frame is "*Becoming — the ceremony's frame*"
  (`vault-rule-card.md:15`).
- **The vault rung is read "in Beat 1 by every partner"** (contract `:224`, *Partner memory*) — the
  fleet-wide pointer layer never reaches a non-partner.
- **The sitting is defined on a partner.** "A sitting is one partner's continuous turn at the wheel; it
  yields one session note" (contract `:267`). There is no partnerless sitting, so nothing says what a
  partnerless session owes the record.
- **The schema already half-anticipates it.** `frontmatter.md:167`: "`partner:` … Omit only for a
  partner-less generic-agent session." The session-log schema has a slot for the case the contract
  never names — the field knows about the actor the ritual does not.
- **The seeded pointer is the whole carriage.** `skills/vlt-setup/SKILL.md:198–216` (§3) writes a
  `CLAUDE.md` that says the rules "live in `_meta/vault-operating-contract.md`; read it before writing
  anything" — a pointer at a 66K-character file, with no card, no rung, no conventions. The field
  vault's `CLAUDE.md` is that seed verbatim plus the owner's `## Preferences`.
- **The field evidence.** `{field-vault}/{sessions}` holds session notes with `partner: user` (1) and
  `partner: vlt-mint` (1) among ~240 partner-tagged notes; the owner reports further partnerless
  brainstorm sittings that wrote **no** note. Those sessions read the paragraph above and nothing else.

## Why it matters

- **The escape valve vents the rulebook.** `ST-8`'s causes A and B (weight, self-authored drift) push
  the owner toward partnerless sessions; this gap makes every such session ungoverned. The symptom
  presents as "sessions feel lawless" and hides the weight problem behind it.
- **Attribution has a hole.** A partnerless session that writes to the vault leaves no session note
  and no `(partner)` log tag — the trail `vlt-lint` and the review council rely on has a class of
  writer it cannot see.
- **Single-writer is unguarded there.** A bare session that never read the card has never been told
  the wiki is Librarian-only.

## Candidate shape (ideation rules; stated to bound scope, not to prescribe)

1. **Carry governance on a surface every session reads.** `vlt-setup` §3's seeded pointer gains
   import lines for the rule-card and the vault rung (`@_meta/vault-rule-card.md`,
   `@_agent/reflexes.md`) — pointers, never copies, so single-home holds and the card's derivation
   stays where it is. Additive under the existing "user's file, heading-scoped edits only" rule
   (`vlt-setup/SKILL.md:217`).
2. **Name the partnerless sitting in the contract.** *Sessions, sittings, and hand-offs* gains the
   `partner: none` sitting: one session note, log tag `(session)`, no partner-memory writes, wiki
   single-writer still holds. An optional `purpose:` (e.g. `brainstorm`) makes the owner's real
   pattern attributable without making it stateful.
3. **Ops unchanged** — their "omit the tag" path stands.

**External unknown — spike before any brief** (lifecycle step 3): whether `@path` import lines in a
vault `CLAUDE.md` load for *every* session kind in the current runtime (interactive, headless op,
partner summon, subagent). Read the runtime, not its docs. **Fallback if not:** the vault already
registers a `SessionStart` hook (`vlt-setup/SKILL.md:181` §2b, `vlt-vitals.py --strip`); the card
can ride the same hook.

## Acceptance (draft)

- **Ship-verifiable:** the seeded `CLAUDE.md` carries the two import lines; `frontmatter.md`'s session
  schema admits `partner: none`; `vlt-lint` accepts it; the contract names the sitting.
- **Field-contingent:** a `{field-vault}` brainstorm sitting yields a `partner: none` note and a
  `(session)` log line; the spike's positive result reproduced on the field vault's first session
  after upgrade.

## Related filings

`2026-07-29-082930` (the contract read as the boot whale — the rule-card was its repair, and it
worked: the ritual's governance reads are now ~1.3K words; this filing asks that the repair reach
sessions that never run the ritual).
