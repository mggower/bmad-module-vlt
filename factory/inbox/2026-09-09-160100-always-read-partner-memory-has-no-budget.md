# The always-read partner memory has no budget — groom is a ratchet, and `identity.md` is 70% of Beat 1

_Filed 2026-09-09 by the **factory**, from an owner problem-solving session on the partner model
(`bmad-cis-problem-solving`; session artifact gitignored). Evidence is `{field-vault}` read-only
(2026-09-09) plus module source at `5ca31f0`. Kind: `candidate`. Cause: **`ST-8`**
(`factory/studies/ST-8-always-read-memory-has-no-budget-and-no-owner.md`, cause A) — cited, not
restated. Owner elected to file._

## The claim

The promotion ladder has one axis. Material moves **up** as it proves durable, and the rung at the top
(below the wiki) is `identity.md` — the file every activation reads whole in Beat 1. Nothing bounds
that file; the only cap in partner memory is `reflexes.md`'s, and it counts lines, not words. Groom's
three verbs — promote, compress, retire — cannot move material *down*, so hygiene concentrates weight
into the always-read set. The field vault's heaviest partner has been groomed three times and stands
at ~28.7K words of memory, ~19.8K of it read before the first user turn.

The owner noticed the cost **before** Cycle 8 shipped the ladder (`A8-3`, filing `2026-08-17-143641`);
the ladder was the response. It answered *what survives* and left *what must be read every time*
unbounded — so the repair for the symptom built the ratchet.

## Specimen manifest

**The set (9 of 9 partners in `{field-vault}`, words, measured 2026-09-09 with `wc -w`).** Beat 1 =
SKILL.md + `identity.md` + `reflexes.md` + rule-card (1,076) + vault rung (145); full activation adds
`## Thread`.

| Partner | SKILL.md | identity.md | thread.md | reflexes.md | Beat 1 | Full |
|---|---|---|---|---|---|---|
| football-analyst | 4,604 | 13,325 | 14,777 | 643 | ~19,800 | ~34,600 |
| creative | 2,037 | 11,871 | 16,393 | 1,243 | ~16,400 | ~32,800 |
| librarian | 1,744 | 15,789 | 6,606 | 493 | ~19,300 | ~25,900 |
| researcher | 1,812 | 5,111 | 8,565 | 1,060 | ~9,200 | ~17,800 |
| career-strategist | 3,872 | 2,202 | 4,417 | 455 | ~7,800 | ~12,200 |
| chef | 2,998 | 2,829 | 3,442 | 67 | ~7,100 | ~10,500 |
| chess-coach | 3,328 | 2,633 | 2,579 | 67 | ~7,300 | ~9,900 |
| health-coach | 2,585 | 1,610 | 917 | 67 | ~5,500 | ~6,400 |
| dog-trainer | 2,204 | 909 | 486 | 67 | ~4,400 | ~4,900 |

**The minimal triggering fragment** — the football-analyst's `identity.md` section weights
(`awk` over `## ` headings): `## Bond` 5,330 words, `## Self` 7,195 words. `## Self` holds 28 `###`
headings, each a dated first-person case narrative; the first four verbatim:

```
### I missed a pre-commitment I had written myself a date for, and only found it by being asked about something else — 2026-09-01
### The thing I pre-registered was worth less than the thing I found while checking it — 2026-09-01
### The first grade came in against me, and how I carried it is the only part that was mine to choose — 2026-08-30
### I proposed a call I should not have proposed, and he caught it in one line
```

And the one cap that exists, at cap and hollow — the Researcher's `reflexes.md` frontmatter and its
own verdict: `cap: 30` … "_30 of 30 — at cap._" at **1,060 words**, ~35 words per "one-line" rule.

Groom history for the heaviest partner (`{field-vault}/{log}`, `grep groom`): 2026-08-24 17:25
(promote 10 / compress 7 / retire …), 2026-08-28 18:45 (promote 6 …), 2026-08-28 19:10 (Bond pass).
Five of nine partners have never been groomed.

## Grounding (module source, `5ca31f0`)

- **`identity.md` is evergreen and Beat 1.** Contract `:214` ("evergreen (read in Beat 1)"); `## Self`
  is "**ungated** identity drift … A partner writes this freely" (`:217`). The schema
  (`frontmatter.md:185–193`) carries no cap field.
- **Only `reflexes.md` is capped, by line count.** Contract `:224` ("one line per rule, hard-capped");
  `frontmatter.md:221–228` (`cap: 30 # at most 30 one-line rules`). The cap's own `falsifier:` names
  "reflexes routinely exceed one line" — it has fired on the Researcher and nothing reported it.
- **The ladder only lifts.** Contract `:240` — "**The three verbs.** promote — move material up a rung
  … compress-to-latest-form … retire". `skills/vlt-groom/SKILL.md:11` restates the same three. No
  verb moves material down; the ladder table (contract *Partner memory*) has no rung *below* Beat 1
  for durable-but-not-always-needed material.
- **Beat 2's bound does not bind.** Contract *Activation ritual* reads "`## Thread` **only**"; in the
  heaviest `thread.md`, `## Set aside` begins at line 1,046 of 1,150 (~9% excluded).
- **No instrument sees it.** `vlt-vitals.py:203`'s `METRICS` table has no activation-weight metric;
  `tripwires.yaml` therefore cannot wire one; `vlt-lint` has no partner-memory weight check. The
  registry's own bound (`tripwires.yaml`, B10-4: local metrics cover count/size/age kinds) means a
  vault *could* declare a size metric on `identity.md` today — but the module ships no wire, no
  budget, and no verb to act on a trip.
- **The contract solved this for itself.** A 66K-character contract is never read on activation; it
  is distilled to a ~1.1K-word rule-card and opened point-of-use (`vault-rule-card.md:15–17`). Partner
  memory got no such card.

## Why it matters

- The most-used partners (session counts: librarian 70, researcher 49, creative 36, football-analyst
  31) are the most expensive, because weight follows use and nothing bounds it. The tax lands where
  the owner works most.
- `## Bond` has become a user-model store ("How he drafts", "Instruments, and how he uses them", "The
  leagues" — ~5.3K words) because it is the only per-partner home for that knowledge; the contract
  would file it in the wiki or a PARA area, on demand.
- Any fix to drift (`ST-8` cause B) that leaves the ladder one-way is re-eaten by growth within two
  cycles — R2 keeps running.

## Candidate shape (ideation rules)

1. **A second axis: a Beat 1 budget.** The contract declares a word bound for the always-read set;
   `vlt-vitals` derives `activation_words` per partner (a new canonical metric — the route
   `tripwires.yaml`'s header names); a shipped wire trips on it; `vlt-lint` reports it.
2. **The missing verb: demote.** `vlt-groom` gains *demote* (down a rung); the contract's ladder
   gains the rung it lacks — a **casebook** (`{partners}/<partner>/casebook.md`, never wake-read,
   point-of-use, with a decay contract) for dated narratives, and the wiki/PARA profile (Librarian
   hand-off) for owner-model material.
3. **`identity.md` becomes the card.** Capped `## Self` (manner only) and `## Bond` (relationship
   facts only), mirroring the contract's card + point-of-use pattern. Migration is a groom act per
   partner, by reference, approval-gated — durability holds.
4. **Rider:** the reflex cap counts words (`cap_words:`), per its own falsifier.

Budget value is an owner ruling; the light partners' median ×2 (~12K words) is a defensible first
bound, to be tightened on the instrument.

## Acceptance (draft)

- **Ship-verifiable:** budget stated in the contract; `activation_words` in `METRICS` with a fixture
  vault; demote round-trips on a fixture (source rung loses the copy, casebook gains it, watermark
  set); casebook absent from every Beat 1/2 read list; `frontmatter.md` handshake bumped and every
  consumer re-acked.
- **Field-contingent:** the heaviest `{field-vault}` partner under budget after one groom; fleet
  median Beat 1 flat cycle-over-cycle.

## Related filings

`2026-08-17-143641` (the ladder, `A8-3` — this filing names its missing axis);
`2026-07-29-082932` (Beat 2 unbounded, `A4-17` — the `## Thread` observation above is its residue);
`2026-07-29-082930` (the contract read — repaired by the card this filing asks to extend to memory).
