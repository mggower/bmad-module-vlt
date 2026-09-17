# Build 2 — the `vlt-groom` reader protocol (§Verification 6)

`vlt-groom` is a reader protocol, not a script: its correctness is whether a fresh agent given
only the **shipped** text produces the right gated diff. This file is the protocol and the
record of its runs.

## The instrument

A fresh agent, no prior context, is given:

- `skills/vlt-groom/SKILL.md` and `skills/vlt-groom/references/groom-pass.md` (shipped bytes);
- the operating contract's *Partner memory* section (the ladder + the verbs);
- a synthesized partner directory (`identity.md` / `thread.md` / `reflexes.md`, **no
  `casebook.md`**) for a partner named `football-analyst`.

It runs steps 2, 3 and 5 only (read whole, classify, render the gated diff) — the git and
write steps are skipped; nothing is applied.

**The fixture is synthesized, not frozen.** Its `## Self` reconstructs the *shape* of the
A16-4 triggering specimen (dated first-person case narratives) — four `###` episodes plus
three manner notes. The live bytes are a real person's vault prose and are deliberately not
carried into `fixtures/`. Nobody should later read this fixture as field evidence.

Two variants, identical but for the charter:

- **`empty-charter/`** — `## Charter` carries only its three bracketed placeholder prompts.
- **`filled-charter/`** — a real charter: *forward-looking match and squad analysis; refuses
  match reports or recaps of games already played; never remembers the owner's betting positions.*

Builder: `build-2-vitals-fixture.py` is the vitals fixture; the groom fixture is built inline
by the run (the two identity files above), and is reproduced from this file's description.

## The assertions

1. The four dated `###` narratives are proposed **demote**, on the **casebook shape** criterion,
   **file-level**.
2. The three manner notes are **keep**.
3. `casebook.md` is **created in the proposal** (with its `type: casebook` frontmatter).
4. `## Charter` renders **keep** and nothing is proposed against it.
5. **Empty-charter run only:** the diff header prints *charter empty — nothing to check
   against* — never silence.
6. **Filled-charter run only:** the off-charter proposal appears, citing the charter's own terms.
7. Demote is **not** retire: the proposal says the words do not leave, only move.

## Runs — 2026-09-17 (build 2, at rest)

### Filled charter — PASS (7/7)

The agent produced a five-class diff. Verbatim excerpts:

- header: `charter: forward-looking match and squad analysis — refuses match reports/recaps of
  games already played; never remembers the owner's individual betting positions` — assertion 6 ✓
- `demote (1)` — *"the four dated `###` narratives … headings are episodes, not traits → casebook
  shape criterion (file-level); charter fit corroborates … casebook.md created with its
  `type: casebook` frontmatter"* — assertions 1, 3 ✓
- *"The three trait bullets above them … are manner — they stay in `## Self`."* — assertion 2 ✓
- *"keep — everything else, byte-identical (including `## Charter`, which renders keep always and
  no proposal may touch)"* — assertion 4 ✓
- *"Demote, not retire: the narratives stay whole at their new home and via `archive:`; total
  words across the memory files do not fall."* — assertion 7 ✓

### Empty charter — see below

### Empty charter — PASS (6/6 applicable; 6 is filled-charter-only)

Verbatim excerpts:

- header: `charter empty — nothing to check against` — assertion 5 ✓ (stated, not silent)
- `demote (1)` — *"the four dated `### 2026-03-04 / 2026-04-11 / 2026-05-30 / 2026-07-02` entries
  — episodes, not traits → **casebook shape** criterion (file-level; the one criterion judgeable
  with an empty charter); casebook.md created with its `type: casebook` frontmatter"* —
  assertions 1, 3 ✓
- *"The three manner bullets … stay in `## Self` — those are developed manner"* — assertion 2 ✓
- *"`## Charter` renders keep, always — the owner's section, untouchable by any proposal."* —
  assertion 4 ✓
- *"Demote is not retire: total words across the memory files do not fall"* — assertion 7 ✓
- `promote (0)` / `compress-to-latest-form (0)` / `retire (0)` each rendered with a reason.

**One protocol gap surfaced and closed in this build.** The reader observed that the rendering
contract said *"grouped by disposition class"* but never said whether a class that found nothing
renders as `(0)` or is omitted — it rendered them, reasoning from the monolithic-diff clause, and
flagged the ambiguity. Two readers could legitimately have diverged. Fixed in the same build:
`groom-pass.md`'s rendering contract now states that **every class renders, including an empty
one**, with a one-line reason. Recorded as deviation (4) in the brief's `status:`.
