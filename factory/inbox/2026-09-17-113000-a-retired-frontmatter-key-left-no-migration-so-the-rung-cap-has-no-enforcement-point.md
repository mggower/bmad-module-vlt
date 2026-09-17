# A retired frontmatter key shipped with no vault-side migration, so the rung cap the migration reads does not exist in any installed vault

_Filed 2026-09-17 by the **field vault** (`{field-vault}`), from the `vlt-upgrade` 0.18.1 → 0.19.0 run at
`[2026-09-17 10:46]`, relayed to the factory and grounded against module source in the same
`acceptance-discharge` session. Evidence: the vault's `_agent/upgrade-ledger.md` block, the live
`reflexes.md` set, and the shipped text at `skills/vlt-upgrade/SKILL.md:82`. Kind: `defect`.
**This is a live-acceptance contradiction of Cycle 16 build-3 check (6) (Rung line reaches an installed
vault), a `[ship-verifiable]` check that GATES cycle closeout.**_

## What happened

Build 2 retired `cap:` in favour of `cap_words:` at `frontmatter@15` (D-10). It migrated the three
**shipped seeds** — its own deviation (1) says so explicitly: *"leaving the seeds would ship a key `@15`
no longer names."* It shipped **no migration for the files already on disk in installed vaults**, and
`frontmatter@15` carries no legal-until-groomed clause for `cap:` the way A8 gave one to `partner:`.

Build 3's `rung-lane-pointer` migration then wrote its degrade path against the **new** key
(`skills/vlt-upgrade/SKILL.md:82`):

> The rung **has a cap** (`cap_words:` in its own frontmatter), so the class's degrade path is live here:
> at cap, this becomes a **human-gated offer** in this migration list and the skip is **recorded in the
> post-flight report** — never edit-one-out, never exceed the cap.

On the field vault that key is absent from every `reflexes.md`. The upgrade operator resolved the cap
check by reading the **retired** key and counting **lines**, which the ledger records verbatim:

> **rung-lane-pointer** — the exact line was appended to `_agent/reflexes.md`, which stood at 3 lines
> against its `cap: 30`, so the class's degrade-to-offer path was not live and no cap was argued (now 4
> lines).

`cap_words: 900` is a **word** cap; `cap: 30` was a **line** cap. The recorded pass was obtained under a
hand substitution of both the key and its unit — not the shipped surface. (Precedent for the grade: this
same roadmap's Cycle 15 build-2 (6), FAILED because *"the 132/152 warm re-run ran under a hand
workaround, not the shipped surface."*)

## Why it matters beyond one cosmetic key

The degrade path is the whole point of the clause — *never edit-one-out, never exceed the cap*. Keyed to
`cap_words:`, it reads absent on every installed vault, so it derives "no cap declared" forever: the
at-cap branch **cannot fire in the field**, in the shape a caller cannot distinguish from "under the
cap." Today the field rung is 4 lines and nothing breaks; the branch is unreachable, not merely unused.
That is the `ST-2`/`b2(5)` family this factory keeps filing — a rule whose enforcement point does not
exist where the rule applies.

## Specimen manifest — the complete set

**Set: every `reflexes.md` on the field vault, all 10, each with its cap key as it stands post-upgrade.**
Obtained by reading each file's frontmatter directly (`grep -o "^cap[_a-z]*:.*"`), 2026-09-17, after the
0.19.0 apply.

```
_agent/reflexes.md                               cap: 30
_agent/partners/career-strategist/reflexes.md    (no cap key at all)
_agent/partners/chef/reflexes.md                 cap: 30
_agent/partners/chess-coach/reflexes.md          cap: 30
_agent/partners/creative/reflexes.md             cap: 30
_agent/partners/dog-trainer/reflexes.md          cap: 30
_agent/partners/football-analyst/reflexes.md     cap: 30
_agent/partners/health-coach/reflexes.md         cap: 30
_agent/partners/librarian/reflexes.md            cap: 30
_agent/partners/researcher/reflexes.md           cap: 30
```

**9 of 10 carry the retired `cap:`. 0 of 10 carry `cap_words:`. 1 of 10 (`career-strategist`) carries
neither** — a pre-existing gap the rename would otherwise have papered over, and the one specimen that
shows "absent" and "retired-but-present" are two different field states the migration must tell apart.

**Minimal triggering fragment** — the live vault rung's frontmatter, the file the shipped migration
actually wrote into this run:

```yaml
---
type: reflexes
scope: vault
created: 2026-08-21
last_updated: 2026-09-09
cap: 30
falsifier: "if a partner writes against an overlaid subject without the pre-act read after this rung named it, or a rung line carries rule content rather than pointing at the rule's home, the pointer shape is failing — file it"
review_after: 2026-11-17
---
```

**Module-side corroboration, complete:** `grep -rn "^cap: \|\`cap:\`" skills/` returns **0** (the seeds
were migrated), and `grep -rn "cap_words" skills/vlt-upgrade/ skills/vlt-groom/ skills/vlt-lint/` returns
exactly **one** line — `skills/vlt-upgrade/SKILL.md:82`, the degrade-path sentence above. There is no
migration, no lint check, and no groom step anywhere in shipped source that renames `cap:` → `cap_words:`
or reports a `reflexes.md` carrying the retired key.

## What the fix probably is (not a ruling)

An additive-write migration in `vlt-upgrade`'s Step 5 list — build 2's own D9 act class, the same class
`charter-seed` belongs to — that renames `cap:` → `cap_words:` on every `reflexes.md` and converts the
unit (the shipped seed's own arithmetic is stated at `frontmatter.md:252`: *900 words = 30 one-line rules
× the ~30-word line the falsifier fired on*), leaves a file carrying neither alone or seeds the default,
and records itself in `migrations_run`. Whether the conversion is automatic or a human-gated offer is an
ideation question, not this filing's.

**The general shape is the more valuable half:** `frontmatter@N`'s version handshake re-acks *consumers*,
and nothing in it asks whether a **retired key still sits in installed vaults**. A convention key
retirement is a field migration, and the handshake does not know that. Whether that belongs as a
re-check in `build-brief`'s retirement discipline or as a `vlt-lint` finding class is the open design
question.
