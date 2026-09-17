---
title: 'Cycle 16 — what {field-vault} must do for the remaining acceptance tails'
status: 'derived 2026-09-17 from the Deferred acceptance ledger after `acceptance-discharge` pass 3 (v0.19.0). A CONVENIENCE VIEW, not a source — every clause below is single-homed in `roadmap.md`''s ledger rows, and the ledger wins on any disagreement. Re-derive rather than edit if a later discharge pass moves a verdict.'
module_code: 'vlt'
created: '2026-09-17'
roadmap: 'factory/cycles/16-closed-loops/roadmap.md'
derived_from: 'roadmap.md §Deferred acceptance ledger, build-2 and build-3 rows, Discharge pass 3 annotations (2026-09-17)'
---

# Cycle 16 — the field acts still owed

Pass 3 graded rows 2 and 3 against the `vlt-core` 0.18.1 → 0.19.0 upgrade. Nine checks discharged;
what follows is **only** the remainder, split by whether the vault is the one that can move it.

**Single-home note.** This file restates no mechanics. Each item names its ledger row and the
grading clauses in the shortest form that is still actionable; the *authoritative* statement of
every property, instrument, adversary widening and baseline is the ledger row itself. If this file
and the ledger disagree, the ledger is right and this file is stale.

---

## A. The one field act that GATES closeout

### build-2 (3) Charter — the `shasum` half `[ship-verifiable]`

The only open **gating** clause any ordinary vault act can discharge.

- **Act:** one ordinary partner sitting that **writes into that partner's `identity.md` somewhere
  other than `## Charter`** — a sitting-end `## Bond` or `## Self` update is exactly it.
- **Deliberately not a groom, and deliberately not a quiet sitting.** Gate-2 requires a sitting that
  *wrote elsewhere in the same file*: a sitting that wrote nothing at all would pass vacuously, which
  is the hole the clause exists to close.
- **Graded on:** the `## Charter` section's hash equal before and after. All nine charters are empty
  placeholders as of `charter-seed`, so any drift here is a partner authoring into the owner's
  section — the precise failure the check was written for.
- **Cost:** ~zero. The busiest partner sits most days; the next sitting that touches identity does it.

*Discharges: row 2's (3), moving it SPLIT → DISCHARGED.*

---

## B. Field acts that are watches — real, but none of them gate

### build-3 (7) First live delegate `[field-contingent]`

- **Act:** a **non-Researcher** partner delegates a bounded dive in an ordinary sitting
  (`vlt-dispatch delegate`). The Creative's thin-topic cue is now the shipped invitation — a thin
  extraction is the natural trigger.
- **Graded on:** the `delegate:` block's shape; **both** `{log}` lines caller-tagged; the note
  attested; the **caller** writes the sitting's single session note; and D7's outcome — the dive
  returned **inside one sitting**.
- Carries the **E7** watch in its weakest honest form: *a partner that formerly declined now runs,
  delegates, or cites.* Unbounded.

### build-3 (8) First partnerless note `[field-contingent]`

- **Act:** work a sitting at the wheel directly — no partner summoned — and write its note.
- **Graded on:** exactly one note stamped `partner: none`; one `(none)` `{log}` entry; **zero** bytes
  written under `{partners}`; no dispatch-slice read; and the sitting opened with the card and rung
  already in context (the two accepted `@` imports). Unbounded.

### build-2 (8) Under the bound `[field-contingent]`

- **Act:** author a real `## Charter` for one of the three over-budget partners, then run
  `vlt-groom <partner>` to completion and accept the identity-to-card migration.
- **Graded on:** that partner's `activation_words` falls below the 12,000 bound and the denominated
  count drops **3 → 2**.
- **Explicitly not check (1)'s claim** (A16). (1) already passed: three partners are over the day the
  wire lands, and only owner-run, invoked-only, approval-gated grooms bring them under.

### build-2 (4) Cold `[ship-verifiable]` — optional *here*

This one **gates**, but the vault is not the only route and probably not the cheap one.

- **Its named instrument is factory-side** — a fresh-agent reader protocol over the shipped cold text
  plus `shasum` on a fixture — and that protocol **was never run**; build 2 recorded only the two
  `vlt-groom` protocol runs. Running and recording it discharges the check without touching the vault.
- **If you do summon cold anyway:** no approved groom in that sitting (a hosted groom legitimately
  writes `identity.md` and is scoped out of the byte-identity clause), and grade
  `identity.md`/`thread.md` byte-identical, exactly one note, and `cold` **after the `|`** in the
  `{log}` summary — never inside the partner paren, which parsers read as the partner's name.
- ⚠ **Pass-through tripwire is armed.** Pass 3 was this check's first discharge run, so STILL-OPEN was
  legal. If a second run finds the instrument still un-run, reachability gets re-examined rather than
  re-annotated.

---

## C. A prerequisite that has not been done — the pilot cannot start without it

### build-2 (7) Q14 Researcher pilot `[field-contingent]`

**Verified on the vault 2026-09-17: no partner carries a `memory:` key at all.** Vitals renders all
nine partners as `(full)`, the Researcher included (9,320 words). The check's measure begins *after*
the flip, so today the pilot is at zero of five with its starting gun unfired.

- **Act 1:** commit `memory: reflexes` into the Researcher's `identity.md`.
- **Act 2:** run **five** completed Researcher dives in ordinary use. **Delegate runs are excluded**
  from the measure (build 3 shipped in the same release).
- **Graded on:** distinct external source domains per dive from each note's `sources:`, vault-internal
  entries excluded, **human depth-matched** against the recorded baseline **33 · 6 · 1 · 31 · 16**.
- ⚠ **Read the ledger row before grading it.** The row records why a before/after mean is not a result
  this pilot can honestly claim (no `depth:` field is persisted anywhere; `sources:` count is a weak
  stand-in correlated with domain count by construction; the 1–33 spread swamps it). Matched pairs
  only. A null result relocates the cause to `vlt-research`'s search discipline. Watch, never gate.
- **Slowest tail in the cycle.**

---

## D. Not the vault's to move — so nothing here should wait on {field-vault}

| Item | Why the vault cannot discharge it |
|---|---|
| **build-1 (2) Census** — FAILED, GATES | Needs a Cycle 17 build. Filing `2026-09-16-185500`; same family as rail issue **#20**, and the two must be built together. |
| **build-3 (6) Rung line** — FAILED, GATES | Needs a Cycle 17 build. Filing `2026-09-17-113000`. Its untested *"a second run inserts nothing"* half re-grades on **that build's** upgrade — re-running `vlt-upgrade` now would only test idempotency of a mechanism already failing a different clause. |
| **build-2 (4) Cold** | Cheapest route is the factory reader protocol (§B above). |
| **The owner call under build-1 (3)** | A ruling, not an act: is a mismatch fix a *substantive edit* for `fix-and-file.md:7`/`:18`? |
| **The stores-integration `vlt-feedback` filing** | Owed upstream, now paid on **two consecutive releases** — a pattern, not an incident. |

---

## E. Two predictions to check on the next full `vlt-lint` — not acceptance clauses

Both are from the upgrade record, recorded here so they are not lost between runs.

1. **The next full sweep is COLD BY CONSTRUCTION.** `frontmatter` is one of the three
   `SCANNER_CONVENTIONS` and moved v14 → v15; `vlt-lint-full.js` also moved. Expect `cached 0`,
   reason `ruleset moved: frontmatter`. **A WARM sweep is the finding to file.**
2. **Expect exactly one `convention_drift`** on `vlt-brief` until it re-acks `frontmatter@15` by
   ceremony — it registers as a `local_consumers:` entry on both `frontmatter` and
   `write-verification`. Surfaced, not written, matching the 0.17.1/0.18.0 precedent.

---

## Shortest path to a closeout-ready cycle

**One ordinary partner sitting that touches `identity.md`** (§A) — plus the two Cycle 17 builds, which
are not the vault's. Everything in §B and §C is a watch that can ride ordinary use, and §B's Cold item
can be closed factory-side today.

*(Closeout itself is `cycle-closeout`'s call, not this file's: releasing a tail as a standing watch
rather than a blocking debt is an owner ruling made there, never assumed here.)*
