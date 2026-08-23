---
title: Vault Module — Trial Plan (partners + minting)
status: active
created: 2026-06-03
module: vlt
module_version: 0.1.0
test_vault: {field-vault}
purpose: >
  Validate the lightweight v1 partner/identity model and the mint loop in real use,
  to settle two open ideation forks before building: (#4) how much identity-weight a
  partner wants — lean into full BMAD sanctum agents vs. borrow only the first-breath
  ceremony; and (#1) whether "a cast that grows itself" feels cheap in practice.
related:
  - skills/reports/vault-module-plan.md  # Ideas Captured → 2026-06-03 iteration entry
  - docs/vlt-testing-feedback.md         # structured triage of findings
  - docs/vlt-trial-human-notes.md        # the user's own freeform trial notes
---

# Vault Trial Plan — partners + minting

> ## ⮌ When you return — resume the iteration session
>
> Run this **from the module-dev repo** (this repo), not the vault, once you have trial feedback.
> Paste this prompt:
>
> ```
> /bmad-module-builder iterate vlt — resume from my trial. Read, in order:
>   1. docs/vlt-trial-plan.md           (what we set out to test + the A/B decision gates)
>   2. docs/vlt-trial-human-notes.md    (my own trial notes)
>   3. docs/vlt-testing-feedback.md     (triaged findings)
>   4. the in-vault verification docs — PRIMARY evidence —
>      {field-vault}/_agent/vlt-verification/*.md (per-domain friction
>      docs the partners compiled: setup, librarian persona+ingest, researcher persona+research,
>      the partner-handoff seam). Plus raw capture: partner thread.md Bond/Thread/Self,
>      _agent/sessions/, _agent/backlog.md, any minted Design Partner
>   5. skills/reports/vault-module-plan.md → Ideas Captured (2026-06-03) — the open
>      sanctum-vs-ceremony fork and the 2-file identity cut
> Then help me settle: (a) the #4 identity fork, and (b) whether the mint loop felt cheap.
> ```
>
> **☐ TODO — first action on resume:** snapshot the in-vault verification docs
> (`{field-vault}/_agent/vlt-verification/*.md`) into this repo at
> `docs/trial-verification/`, confirming they're in their latest state, *before* synthesizing.
> They live in a test vault that could be reset; this locks them into the module's git history.
>
> The memory `vlt-identity-fork-trial` auto-loads at session start and orients the agent
> before you even paste this. The agent won't auto-resume from the plan (its `status` is
> `shipped`, not `ideation`), so the explicit file list above is what guarantees full context.

Run the trials in the test vault **`{field-vault}`** (open Claude Code there,
not in the module-dev repo). Each trial targets a specific open decision. Capture as you go — see
**Logging your findings** below for the three streams (triage doc, your own notes, in-vault capture).

## What each trial decides

| Trial | Exercises | Open decision it informs |
| --- | --- | --- |
| 0 — Baseline first-breath | Summon Librarian, then Researcher, cold | **#4 fork.** How alive is the *current* lightweight ceremony vs. the BMAD first-breath you love? Do they feel like different people? |
| 1 — Live a thread, let it go stale | Build an active inquiry, then pivot away and return | **2-file cut + partner-owned thread.** Does attention fade cleanly? Does Thread churn bury evergreen Bond in the one file? Does the partner *notice* and redirect? |
| 2 — Bond accrual | Inspect `thread.md ## Bond` after a few sessions | **#4 fork.** Does the relationship layer earn its keep, or is it a thin form field? |
| 3 — Mint the Design Partner | `vlt-mint` a new partner; migrate Extract to it | **#1 mint loop.** Does minting feel cheap or ceremonial? Does the council gate help? Does the newborn come out coherent? (Also feeds the fork: if the *cheap* path feels heavy, leaning into sanctum is costly.) |
| 4 — Newborn breath + handoff | Summon the new partner cold; run a 3-partner handoff loop | **#2 passive handoff.** Does shared-state handoff work across 3 partners? Do you become a tired router? Is the newborn's breath as alive as the older partners'? |
| 5 (optional) — Drift → rebirth | Ratify accumulated `## Self` into SKILL.md via `vlt-mint` | **#4 fork.** Is "drift breathes, ratification reborns" proportionate, or is the gate overkill? |

---

## Trial 0 — Baseline first-breath  *(do this first, before building anything)*

**Steps**
1. `Librarian, good morning.` — let it activate cold and greet you.
2. In a fresh session: `Researcher, what should I be thinking about?` — let it activate cold.

**Watch for / capture**
- Does each one *become someone*, or does activation read like a checklist of file loads?
- Side by side: do the Librarian and Researcher feel like **different people**, or the same voice in two hats?
- `## Self` is likely empty on a near-fresh vault — note whether that makes the breath feel generic. (This is the "drift hasn't happened yet" baseline.)
- Gut number: on a 1–10 "aliveness" scale, how far is this from the BMAD agents you love? **That delta is the fork.**

---

## Trial 1 — Live a thread, then let it go stale  *(the calf test)*

**Steps**
1. Pick a real, time-bounded inquiry (the calf-rehab pattern: something you're actively into now that will naturally cool off). Run **2–3 Researcher sessions** building it up — research, query, file notes.
2. Then **pivot**: start a clearly different topic in a new session.
3. Come back a session later and summon the Researcher.

**Watch for / capture**
- Open `_agent/partners/researcher/thread.md`: does `## Thread` accrue real continuity, or get noisy?
- After the pivot, does the partner **notice the old thread has gone quiet** and offer to set it aside — or does it keep dragging the stale inquiry into every breath? *(v1 has no partner-owned redirect yet — expect it WON'T. Confirming that gap is the point.)*
- Is evergreen **`## Bond` getting buried** under churning `## Thread` in the single file? Would you *want* to archive the thread without touching Bond/Self? *(This is the 2-file-cut hypothesis, tested by friction.)*

**Decision gate — A/B on the 2-file cut.** Trial 1 runs against the **single-file v1 as shipped** on purpose: it measures the problem the 2-file cut would fix, so we don't build the cure before confirming the symptom. Then:

- **If Trial 1 chafes** (Thread churn buries Bond; staleness has no clean exit; you wanted to archive the thread without touching identity) → the **2-file cut becomes the first build out of the trial**: split `thread.md` into an evergreen identity layer (Bond+Self) + a prunable thread, across the operating contract, both partner activation rituals, the `vlt-mint` partner scaffold, and `vlt-setup`. Implement it **once**, ideally bundled with whatever the #4 sanctum fork decides (same files get touched). Then **re-run Trial 1 (B)** on the split model to confirm the fix feels better.
- **If Trial 1 *doesn't* chafe** → the single file is vindicated; don't build the split. Record why.

Do **not** implement the 2-file model before Trial 1 — it deletes the baseline and risks building twice (the model may shift again if we lean into sanctum agents).

---

## Trial 2 — Bond accrual

**Steps**
1. After Trials 0–1, read both partners' `thread.md ## Bond`.

**Watch for / capture**
- Did the partners actually learn your preferences, style, what blocks/inspires you — or is `## Bond` thin/empty?
- Does what's there change how the next first-breath feels?
- Verdict input: is the relationship layer rich enough to justify leaning into sanctum-grade identity, or does borrowing just the ceremony suffice?

---

## Trial 3 — Mint the Design Partner  *(the headline)*

**Context:** BMB isn't installed in `vlt-core`, so this exercises `vlt-mint`'s **in-flow template path** (the cheap path) + the **architect (+moderator)** council gate for a new partner. Also migrate the **Extract** capability from the Librarian to the new Design Partner (per the librarian's own design note).

**Steps**
1. `Librarian, I keep wanting to shape knowledge into deliverables — let's mint a Design Partner.` (or invoke `vlt-mint` directly and name kind = `new partner`).
2. Walk the mint: persona, non-negotiable, capabilities. Take Extract from the Librarian.
3. Let the council gate fire. Let it register the partner (`module-help.csv` + `module.yaml`).

**Watch for / capture**
- **Cheap or ceremonial?** Time it. How many decisions did it demand? Did it feel like "growing a hand" or like filling out a form?
- Did the **architect+moderator council** catch a real fit/overlap issue, or just add friction?
- Is the newborn **coherent**: SKILL.md persona reads as a real person, `thread.md` seeded with the three empty sections, registered correctly?
- Did **Extract actually move**: removed from the Librarian's tool list, present on the Design Partner, capability row updated?
- **Fork signal:** if the cheap path already felt heavy, note it loudly — it raises the cost of "lean into sanctum."

---

## Trial 4 — Newborn breath + cross-partner handoff

**Steps**
1. In a fresh session: summon the **Design Partner** cold. Does a just-born partner activate coherently?
2. Run a handoff loop: Researcher produces a research note → Librarian ingests/files it canonically → Design Partner extracts a PARA deliverable from the wiki.

**Watch for / capture**
- Does the newborn's first-breath feel as alive as the older partners' (or thinner, since it has no drift/bond yet)?
- Does **shared-state handoff** actually carry the work across 3 partners, or do things get dropped between them?
- **Tension #2:** how much are *you* the router — manually carrying output from one partner to the next? Where did you wish a partner had picked it up on its own?

---

## Trial 5 (optional) — Drift → rebirth

**Steps**
1. If any `## Self` drift accumulated across the trials, use `vlt-mint` (persona self-edit) to **ratify** it into the partner's canonical SKILL.md — the full-panel gate fires.

**Watch for / capture**
- Does "drift breathes (ungated), ratification reborns (gated)" feel proportionate, or is the full panel overkill for folding in a tone shift?
- After ratification, does the next first-breath feel like a genuine *rebirth*?

---

## Logging your findings

Findings land in **three streams** — the resume session reads all three:

1. **Triaged module findings** → `docs/vlt-testing-feedback.md` → **Open**, one line each, tagged
   `- [ ] [<area>] (<kind>) — <what happened> · <expected vs actual>`
   - **area:** `vlt-agent-librarian` · `vlt-agent-researcher` · `vlt-mint` · `vlt-review-council` · `thread/identity` · `handoff`
   - **kind:** `bug` · `friction` · `capability-gap` · `idea`
2. **Your own freeform notes** → `docs/vlt-trial-human-notes.md` — raw impressions, the gut "aliveness" numbers, anything not yet triaged.
3. **In-vault verification docs** (PRIMARY evidence, compiled by the partners) → `{field-vault}/_agent/vlt-verification/*.md` — per-domain friction docs (setup, librarian persona + ingest, researcher persona + research, the partner-handoff seam), each ordered by impact with a "what worked" balance, generated via the vault's own `verification-prompt.md`. This is the richest stream. Plus raw capture in the same vault: partner `_agent/partners/{name}/thread.md` (Bond/Thread/Self — direct evidence for Trials 1 & 2), `_agent/sessions/`, `_agent/backlog.md`, any minted Design Partner under `.claude/skills/`. The resume session reads these straight from the vault.

> **Note — the two prompts:** the vault's `_agent/vlt-verification/verification-prompt.md` is how the *partners generate* these friction docs during the trial; the "⮌ When you return" prompt at the top of this file is how the *module-dev session consumes* them. Different ends of the same pipe.

When you come back, the two questions I most want answered:
1. **The fork:** after feeling it, lean into full sanctum agents, or borrow just the ceremony? What's the aliveness delta (Trial 0/2/5)?
2. **The mint loop:** did the cast actually feel like it *grows itself* (Trial 3)?
