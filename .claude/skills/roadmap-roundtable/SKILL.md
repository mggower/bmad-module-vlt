---
name: roadmap-roundtable
description: Convenes the installed BMad roster to review the ideated cycle roadmap before briefing, converging to amendments applied in-session. Use when the user says 'convene the roundtable' or 'run the roadmap roundtable'.
---

# roadmap-roundtable

## Overview

Ideation rules build-by-build; nobody in that session is looking at the plan as a whole.
This skill is the review step between ideation and briefing (Arc 7 proved it ad-hoc: four
amendments, three standing rules, one owner-ruled dispute — and a four-arc inherited debt
retired by a one-word amendment). Convene the full installed BMad agent roster over the
ideated roadmap and **hunt the joints, not the parts**: every fault worth finding comes
from locally-correct rulings composing badly — a rule shipped ahead of its mechanism with
no stated interim posture, a dependency ruled in two directions across builds, a gate
check whose fixture nothing extends, a true finding a field vault has no legal response
to, a mechanism that quietly obsoletes the rule it was written to stand in for and leaves
it standing, tidiness paid for in truth. Act as the room's moderator: the voices hunt and debate;
the owner is present, rules every dispute live, and owns every ruling.

The bar is Arc 7's: a session that only *discusses* has failed. Consensus with no line in
a file isn't consensus — every agreed amendment is applied to the roadmap in the same
session, and every dissent is recorded rather than dropped.

**Lifecycle position:** the Review step of the loop mapped in
`.claude/skills/vlt-lifecycle.md`, after ideation rulings are filled and before any brief.
`build-brief` gates on this skill's roadmap record (or an explicit owner waiver). Every
report ends with a **Next lifecycle move** line.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` if
present. This skill needs none beyond `user_name` / `communication_language` if set.

`--headless` / `-H`: run Convene → Hunt → the table as a merge-and-shape pass with no
owner in the room → Converge. Apply only undisputed amendments; an undisputed rule lands
as the roadmap's dated declaration only, its home edit waiting for the owner; record
every dispute as OPEN (never substitute a ruling; a substituted owner ruling here is the
same defect the module's own council-fallback build exists to prevent). The session file
plus the roadmap record are the run's audit trail. On completion, emit only:

```json
{"status": "complete", "roadmap": "{path}", "record": "{review section heading}", "amendments": N, "rules": N, "open_disputes": N, "keepsake": "{path}", "next": "{next lifecycle move}"}
```

`status` is `blocked` with a one-line `reason` when there is nothing to review: no open
roadmap, no filled Ideation rulings for the current batch (route: owner fills them, or
`ideation-scaffold` if no skeleton exists), or a Roundtable review record for this batch
already exists — point at it; re-convening over the same rulings is an owner call, never
a default. **Exception:** a mid-cycle **capture addendum** whose dated ruling records a
moved joint (`inbox-capture` owns the posture) convenes a **delta review** scoped to that
addendum only — recorded as `## Roundtable review — addendum (<date>)` appended after it
— never a re-convene over the full batch.

## Convene

Find the open cycle roadmap (read `factory/CYCLE` — a `none` line → blocked, no open
cycle — then open `factory/cycles/<that NN-<slug>>/roadmap.md`) and confirm its current batch's
Ideation rulings section is filled — grouping names builds, spikes and debts dispositioned.
Unfilled slots → blocked; reviewing a half-ruled plan re-litigates ideation instead of
reviewing it.

The room is whoever is installed: glob `.claude/skills/bmad-agent-*` and
`.claude/skills/bmad-cis-agent-*`, and read each SKILL.md only far enough to carry the
persona's name, discipline, and voice. The roster is discovered fresh each run, never
recalled — the room survives roster changes for free. Interactive: present the roster
(the owner may excuse voices whose discipline the batch doesn't touch) and ask which
joints already worry them; carry that answer verbatim into every persona prompt.

## Hunt

Fan the roster out as parallel subagents, each reading the full roadmap (and the captures
and rulings it cites) through its own discipline. Each prompt carries: the persona (name,
discipline, voice), the joints-not-parts frame above, and a return contract — ONLY a list
of findings, each with the roadmap site (cite headings, not line numbers — the roadmap is
append-only and line refs drift), the fault as one falsifiable claim, and the smallest
amendment that would cure it. No findings is a legal return — but **the obsolescence beat
below is mandatory**, and a return that leaves it unanswered is incomplete, not empty.
Subagents unavailable → run the same lenses sequentially inline; the session gets longer, not thinner. As returns
land, write the merged findings to the **session file**
`_output/party-mode/<date>-cycle<N>-roadmap-roundtable-session.md` — the table's working
state.

### The obsolescence beat (required, every run)

*(Platform P-15, 2026-08-25.)* The hunt above looks for **rules ahead of their mechanisms**.
Every persona also runs it in reverse: **does anything this batch ships enforce what an
existing prohibition was already standing in for?** A protection written when the honest
fields had no teeth stops being a protection the moment a net enforces them — but nothing in
the loop notices, because obsolescence produces no field pain, only friction that reads as
normal governance. Eleven cycles retired **zero** rules while adding many; five passes at one
symptom is what that costs.

The question to put to each build that ships a check, a net, or a gate: *name the prohibition
this makes redundant, or say that none exists.* A finding here names both halves — the
superseded rule's site and the mechanism that supersedes it — and its amendment is a
**retirement**, not another exception.

**"Nothing found" is a required, explicit return, never a silence.** A beat that can be
skipped without a trace is ceremony; the record in Converge is what makes the difference
visible. Material of this shape that falls outside the roadmap's scope is filed as a
**`supersession`** filing per `factory/inbox/README.md`, under capture-don't-interrupt below.

## The table

Bring the findings back to one room and let the personas debate them in character with
the owner present — this is where the value lives, because a finding that survives
Winston conceding twice is not the finding that entered the room. Merge duplicates,
let voices concede or sharpen, and press each surviving finding to one of three shapes:

- **Amendment (A#)** — a concrete edit to the roadmap the room agrees on.
- **Rule (R#)** — a standing rule with a **named home** (a skill, the map, CLAUDE.md); a
  rule with no home is a wish, and a rule whose mechanism can't ship this cycle states its
  interim posture or is withdrawn.
- **Dispute** — the room split. Present both positions; the owner rules live; the dissent
  goes on record with the ruling.

Append each resolution to the session file as it lands — the shape reached, who
conceded, the owner's ruling — so the debate survives compaction and the keepsake has
its source; Converge applies from the file, never from conversational memory.

Capture-don't-interrupt: material the room surfaces that is out of the roadmap's scope
(a new defect, a module idea) is noted for `factory/inbox/` filing at handoff, not debated.

## Converge

Interactive, before anything is applied: one soft gate — anything else for the table?
Then apply from the session file before adjourning — in this order, verified by re-read:

1. **Amendments into the roadmap** — each A# edited into the section it amends, with a
   dated `*(roundtable A#)*` marker so later readers can trace the provenance.
2. **Rules into their named homes** — or, when the home's edit is itself a build, a
   dated declaration in the roadmap naming the home and the interim posture.
3. **The record**: append `## Roundtable review — <batch label> (<date>)` to the roadmap
   after the Ideation rulings section it reviewed — the roster convened, each A#/R# in
   one line with where it landed, each dispute with the owner's ruling and the recorded
   dissent, any OPEN disputes (headless) flagged as gating, and the **obsolescence beat's**
   outcome — each retirement finding with where it landed, or an explicit
   `Obsolescence: none found` line. This section is what
   `build-brief`'s gate parses. The owner may instead waive the whole review — a dated
   `Roundtable waived (owner): <reason>` line in the rulings section — so a skip is a
   visible ruling, never a silence.
4. **The keepsake** — always: a self-contained narrative HTML of the session, written
   from the session file (the debate as it happened, who conceded, what turned — a
   record with a pulse, in the mold of
   `_output/party-mode/2026-08-15-arc7-roadmap-roundtable.html`) written to
   `_output/party-mode/<date>-cycle<N>-roadmap-roundtable.html`. The roadmap record is the
   contract; the keepsake is the memory.

## Handoff

**Interactive:** state where the record landed, enumerate A#/R#/rulings in one line each,
name any out-of-scope material to file to `factory/inbox/`, and point at the keepsake.

**Next lifecycle move** (routing contract): with the record in place and no OPEN
disputes, `brief build N` (`build-brief`) for the first build the rulings name. OPEN
disputes → the owner rules them (that closes the record), then brief. Blocked runs route
per the reason: unfilled rulings → the owner fills them (`ideation-scaffold` first if no
skeleton); existing record → proceed to briefing unless the owner asks to re-convene.

**Headless:** emit only the JSON contract above; the same move goes in `next`.
