# The `memory: reflexes` posture has no always-read carrier — the rule-card's *Becoming* paragraph and the three shipped partners' Beat 1 text still read `## Bond`/`## Self` unconditionally, and only the point-of-use contract says otherwise

_Filed 2026-10-12 by the **factory**, while answering the owner's question "what does the switch to
`memory: reflexes` do, and how do I do it?" ahead of the Cycle 16 build-2 clause (7) Researcher
pilot. Evidence is module source at `592da5d` (shipped surface unchanged since v0.19.0 @ `03e4686`)
and `{field-vault}` read-only (`CLAUDE.md`, `_meta/vault-rule-card.md`, the Researcher's
`identity.md` frontmatter). Kind: **`defect`** (ship-verifiable). Causes: **`ST-7`** (a derivation
re-stamped without a content read-back) and **`ST-10`** (the pilot this blocks) — cited, not
restated. Filed **before** the pilot runs, so a null result on the pilot can be read against it._

## The claim

Cycle 16 build-2 shipped `memory: reflexes` as a partner's declared standing posture: Beat 1
reads SKILL.md, `## Charter` and the rule layers, and **skips `## Bond`/`## Self`**. The clause
lives in the contract's *Activation ritual*, in the mint template (new mints only), and in the
consult engine's lite boot. It is **absent from both surfaces a partner actually reads at
activation**: the rule-card, which arrives with every session by `@import`, still describes Beat 1
as *identity.md (`name`, `## Bond`, `## Self`)* with no exception; and the three shipped
partners' SKILL.md Beat 1 lines tell them to read `## Bond` and `## Self` — full stop. The
contract governs, but the contract is point-of-use and is not opened for the ceremony. So the
flip the pilot depends on has **no enforcement point in the files read when it matters**, and a
partner can honour it or not with nothing in the record to say which.

## Grounding (module source, `592da5d`)

**Where the posture is honoured:**

- Contract `vault-operating-contract.md:196`: *"…**unless its `identity.md` declares
  `memory: reflexes`, in which case Beat 1 reads SKILL.md, the charter, and the rule layers only,
  and the `## Bond`/`## Self` reads are skipped**…"*. Point-of-use: the rule-card's own frame
  (`vault-rule-card.md:20`) says *"Full mechanics … the contract"* — the contract is opened when
  *"the ceremony itself is in question"* (`:46`), not on every activation.
- Mint template `skills/vlt-mint/assets/partner-agent-template.md:39`: *"unless your `identity.md`
  declares `memory: reflexes`, in which case you read your SKILL, your charter and the rule
  layers only"*. Reaches partners minted **after** v0.19.0 only.
- Consult engine `skills/vlt-setup/assets/workflows/vlt-consult.js:141–143`: the lite boot reads
  the frontmatter first and honours the posture. Reaches **summoned-by-consult** partners only.
- Vitals `skills/vlt-setup/assets/hooks/vlt-vitals.py:548–563` (`_read_memory_posture`) reports
  the declared posture — a **report**, not a read-path.

**Where it is not:**

- Rule-card *Becoming* `vault-rule-card.md:20`: *"**Beat 1 — first breath** — your SKILL.md
  persona modulated by your `{partners}/<partner>/identity.md` (`name`, `## Bond`, `## Self`),
  plus your `reflexes.md`…"*. No `memory:` branch. `grep -c "memory:" vault-rule-card.md` → 0.
  This is the surface `vlt-setup` imports into every session (`skills/vlt-setup/SKILL.md:226`;
  `{field-vault}/CLAUDE.md:44` carries the `@_meta/vault-rule-card.md` line).
- Shipped partners, Beat 1, all three unconditional:
  `skills/vlt-agent-researcher/SKILL.md:24` *"Read your evergreen identity at
  `{partners}/researcher/identity.md` — your `name` …, your `## Bond` …, and your `## Self` …"*;
  `skills/vlt-agent-librarian/SKILL.md:24` same shape; `skills/vlt-agent-creative/SKILL.md:24`
  same shape. `grep -c "memory" skills/vlt-agent-*/SKILL.md` → 2 per file, neither about the
  posture (`:18` "your own memory lives at", `:56` "never from memory").

**How it happened (the brief, read against the result):**

- Build-2 F5 (`briefs/build-2-partner-memory-schema.md:398–432`) put the clause in the contract.
- Build-2 F8 (`:463–487`) scoped the rule-card to **two section-map rows and the hash**
  (`:46` gains "cold-by-choice"; `:47` gains the second axis, demote, the charter) — the *Becoming*
  paragraph was not in scope, although the posture changes **what Beat 1 reads**, which is the
  card's own admission criterion (*identity-bearing: who a partner is and how it becomes itself*,
  `vault-rule-card.md:16`).
- The three shipped SKILL.md were out of scope **by design**: *Adoption postures*
  (`vault-operating-contract.md:252`) rules *"adoption is contract-side … (zero SKILL.md edits)"*
  and *"a minted partner's SKILL.md Beat-1 text that doesn't yet name the reflex read is not an
  error — the contract governs"*. That ruling was written for the **reflex read** (an addition —
  an unmentioned read is a no-op) and extended silently to a posture that **subtracts** reads; a
  SKILL.md that says "read `## Bond`" is not a no-op against a posture that says don't.
- `tools/package-lint.py:253` (`check_rule_card`) verifies the card's `derived_from:` hash matches
  the contract's bytes. It verifies that a re-derive was **stamped**, not that the card's prose
  was **re-derived** — `ST-7`'s shape exactly.

**Specimen manifest.** The set is the shipped surfaces that state Beat 1: contract `:196`,
rule-card `:20`, template `:39`, `vlt-agent-researcher:24`, `vlt-agent-librarian:24`,
`vlt-agent-creative:24`, `vlt-consult.js:141–143` — **7 of 7 named**; 3 honour, 4 do not (card +
three shipped partners). Minimal triggering fragment: `vault-rule-card.md:20` as quoted above,
beside `vault-operating-contract.md:196` as quoted above, same release.

**Field state (`{field-vault}`, read-only, 2026-10-10):** the Researcher's `identity.md`
frontmatter has no `memory:` line (so `full`); its installed rule-card is the shipped card
(same `derived_from:` hash). The pilot has not run. **No sitting has yet shown whether a flipped
partner reads `## Bond`/`## Self` anyway** — that observation is the first thing the pilot
produces, and this filing is written so it can be graded against it.

## Why it matters

- **The pilot's result is uninterpretable without this.** Clause (7)'s discharging event is
  five post-flip dives depth-matched against a baseline. If the Researcher reads `## Bond`/`## Self`
  regardless, the five dives measure nothing, and a null result would be read as "statefulness
  doesn't matter" — the wrong finding, cheaply reached. `ST-10`'s whole test rests on the flip
  taking effect.
- **An always-read rule that lives only point-of-use is not a rule** — it is the pattern `ST-8`
  cause C named for governance (the rulebook rode a ritual the owner skipped) recurring one level
  down: the posture rode a document the ceremony does not open.
- **The derivation gate passed.** `package-lint` C-group was green at the v0.19.0 tag with a card
  that contradicts the contract it hashes. A hash is a read-back of bytes, not of meaning.

## Candidate shape (ideation rules; small)

1. **The card's *Becoming* paragraph carries the branch** — one clause, in the card's register:
   *"…modulated by your `identity.md` (`name`, `## Bond`, `## Self`) — unless its frontmatter
   declares `memory: reflexes`, in which case the `## Bond`/`## Self` reads are skipped —…"*.
   Re-derive the hash in the same commit. Within `RULE_CARD_BUDGET` or it displaces something
   less act-blocking; the posture is identity-bearing by the card's own test.
2. **The three shipped partners mirror the template's `:39` clause** at their `:24`. These are
   module-owned skills refreshed on upgrade, not vault-grown — *Adoption postures*' "zero
   SKILL.md edits" protects **minted** partners and is not breached. State in the contract at
   `:252` that the ruling covers additive reads (the reflex read) and that a subtractive posture
   must be carried by the file that would otherwise instruct the read — precedence by
   elimination: the "not an error" population narrows to additive clauses.
3. **A content read-back for the card**, the `ST-7` repair in miniature: `check_rule_card` (or a
   sibling) asserts that every Beat-1 **branch term** the contract's *Activation ritual* names
   (`memory: reflexes`, cold-by-choice, the charter-first read) appears in the card's *Becoming*
   paragraph or its map row — a term list the lint reads from the contract, not a hand-kept
   list that would drift.
4. **Pilot instrumentation, no build needed:** the first post-flip session note records which
   identity sections Beat 1 read. If the shipped text was honoured over the contract, that note
   is this filing's field specimen.

## Acceptance (draft)

- **Ship-verifiable:** `grep -c "memory: reflexes" vault-rule-card.md` ≥ 1 in the *Becoming*
  paragraph; `derived_from:` hash matches; `RULE_CARD_BUDGET` holds; the three shipped `:24`
  lines carry the clause byte-equivalently to the template's `:39`; the read-back check fails on
  a fixture card whose *Becoming* paragraph lacks a term the fixture contract names, and passes on
  the shipped pair; `:252` narrowed with no precedence statement added.
- **Field-contingent:** the first post-flip Researcher sitting's note shows `## Bond`/`## Self`
  unread; `partner_memory_bytes`'s per-partner line reports `(reflexes)` for the Researcher.

## Related filings

`2026-09-09-160200` (the posture's origin — direction 4, the Researcher pilot);
`2026-10-06-120300` (the lens cut — blocked on the pilot this filing unblocks);
`2026-10-06-120200` (birth posture — same field, the mint side);
`2026-09-03-124500` (a convention's heading stated inside a fence read `located: no` — the
nearest prior instance of a derived surface diverging from its source while its check passed).
