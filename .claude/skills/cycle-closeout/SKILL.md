---
name: cycle-closeout
description: Closes a fully-accepted cycle: verifies discharge, stamps the roadmap CLOSED in place, moves accepted filings into the cycle directory, records carry-forwards, resets factory/CYCLE, syncs memory. Use when the user says 'close the cycle' or 'run cycle closeout' — 'close the arc' is accepted as an alias.
---

# cycle-closeout

## Overview

This skill runs the final move of the module's evolution lifecycle: retiring a cycle whose
builds have shipped and passed acceptance. Closing a cycle is a six-part ritual — verify the
ledger is discharged, record carry-forwards, stamp the roadmap CLOSED in place, move the
accepted filings into the cycle's `filings/`, reset `factory/CYCLE` to none, sync project
memory — and the record shows every manual pass leaks a step (Arc 1's roadmap simply never
recorded a shipped fix). Act as the cycle's closing registrar: this skill is the bell for
that boundary.

Two things it never does. It never **grades** acceptance — `acceptance-discharge` owns
evidence verdicts and runs first; this skill only verifies they happened and refuses to
close over an undischarged ledger. And it never **deletes** — a closed cycle's directory
simply stops changing (archival is a property of location, not a move), and the one move it
does make (filings into the cycle's `filings/`) is a `mv`, mirroring the module's own
never-destroy posture. Blocking on an undischarged ledger is the skill doing its job, not
failing: a cycle must never close over unresolved acceptance.

**Lifecycle position:** step 8c (cycle retirement, the loop's final move) of the loop mapped
in `.claude/skills/vlt-lifecycle.md` — see it for the full flow and the routing contract.
Every report this skill emits ends with a **Next lifecycle move** line. The same line is
**restamped into the foot of the roadmap it is closing** in the run that moves the position
— the chat report alone does not discharge it *(the map's standing rule; platform P-13)*.

## Conventions

- Bare paths (e.g. `references/closeout-checklist.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` if
present. Use sensible defaults for anything not configured — this skill needs none beyond
`user_name`/`communication_language` if set.

`--headless` / `-H`: run Discovery → the checklist stages with no clarifying questions. Any
carry-forward that would need an owner ruling (an ambiguous early filing release, a
first-exercise tail whose disposition isn't already recorded) is left as-is and surfaced in
the report rather than assumed. On completion, emit only:

```json
{"status": "complete", "cycle": "NN-<slug>", "closed": {"roadmap": "...", "briefs": N, "filings": N}, "carried_forward": ["..."], "next": "{next lifecycle move}"}
```

`status` is `blocked` with a one-line `reason` when the precondition gate fails (an undischarged
ledger item with no owner carry-forward ruling, the release not yet tagged, or an orphan spike
this cycle opened and left `proposed`/`running`) — no files are
moved or edited in that case. Point at `acceptance-discharge` in the reason when the ledger is
the cause.

## Discovery

1. **Find the open cycle roadmap.** Read `factory/CYCLE` — it names the open cycle as
   `NN-<slug>` (a "none — …" line means no cycle is open and there is nothing to close).
   The roadmap is `factory/cycles/NN-<slug>/roadmap.md`; its frontmatter `status` should not
   yet be closed/shipped. Read its **Deferred acceptance ledger** section (every item) and
   its frontmatter `status`, `derives_from`, and shipped version.
2. **Find its briefs.** The `build-N-*.md` files in `factory/cycles/NN-<slug>/briefs/` (the
   roadmap references them by name). They already live in the cycle's directory — nothing
   moves.
3. **Find its filings.** The `factory/inbox/*.md` filings this cycle derives from — the
   roadmap's `derives_from:` plus any the ledger items reference. `acceptance-discharge` may
   already have moved the accepted ones to `factory/cycles/NN-<slug>/filings/`; this run
   catches stragglers.

Confirm with the owner (interactive) that this is the cycle to close and that
`acceptance-discharge` has already run against it. Then route to the checklist.

## Stages

| # | Stage | Purpose | Location |
|---|-------|---------|----------|
| 1 | Discovery | Find the open roadmap, its ledger, briefs, and filings | SKILL.md (above) |
| 2 | Closeout | Gate on discharge, record carry-forwards, stamp CLOSED, move filings, reset CYCLE, sync memory | `references/closeout-checklist.md` |

Route to `references/closeout-checklist.md` — it is self-contained (don't assume this SKILL.md
is still in context by the time it runs).
