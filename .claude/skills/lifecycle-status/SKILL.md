---
name: lifecycle-status
description: Derives every active lifecycle position from disk and names each next move. Use when the user says 'lifecycle status' or 'where are we in the lifecycle'.
---

# lifecycle-status

## Overview

This skill answers "where am I?" for the module's evolution lifecycle by walking the
observable-state table in `.claude/skills/vlt-lifecycle.md` against the repo as it sits on
disk. It is the derive-first doctrine applied to the factory's own state: position is
computed from observables every run, never recalled from memory or read out of prose
status lines. Act as the lifecycle's surveyor — you measure and report; you change nothing.

**Read-only, zero writes — by design, not omission.** Every other lifecycle skill writes
(captures, briefs, stamps, archives). This one only reads. If a run surfaces something
that needs fixing — a disk/prose contradiction, an unfiled defect, a stale annotation —
the report *names the skill or owner action that fixes it*; this skill never applies the
fix itself. Do not optimize that away.

The map is the single home of the table, the blocked routes, and the routing contract.
This skill never restates them: it loads the map fresh each run, so a map edit propagates
here with no skill change. If the map and this file ever seem to disagree, the map wins.

**Lifecycle position:** this skill sits outside the loop mapped in
`.claude/skills/vlt-lifecycle.md` — it is the loop's instrument panel, invokable at any
position. Every report ends with a **Next lifecycle move** line.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` if
present. This skill needs none beyond `user_name` / `communication_language` if set.

`--headless` / `-H`: run Derivation with no questions. On completion, emit only:

```json
{"status": "complete", "positions": [{"position": "...", "evidence": "...", "next": "..."}], "flags": ["..."], "next": "{the single most actionable move}"}
```

`status` is `blocked` with a one-line `reason` only when derivation itself cannot run
(the map file is missing, or neither an open cycle's roadmap nor any closed cycle's can be
found under `factory/cycles/` — a repo state the map has no row for).

## Derivation

1. **Read the map first** — `.claude/skills/vlt-lifecycle.md`. Its observable-state
   table, blocked-outcome routes, and routing contract are the spec for this run; derive
   from what it says today, not from memory of it.
2. **Gather the observables the table's conditions name** — read-only, and cheap reads
   (frontmatter, section headings, ledger checkboxes — not whole-file studies): the
   `factory/inbox/` listing; `factory/CYCLE` and, when it names an open cycle, that cycle's
   roadmap at `factory/cycles/<that>/roadmap.md` (its `derives_from`, Ideation rulings
   section, Deferred acceptance ledger check states and grade annotations); the `status:`
   line of each `factory/cycles/<that>/briefs/build-*.md`; git tags (`git tag -l`) against
   the cycle's target version; whatever acceptance-evidence sources the map's rows name.
3. **Evaluate every row, not first-match-and-stop.** Positions coexist (the map says so:
   acceptance/closeout of shipped work and capture of new signal run as independent
   tracks). Report every row whose condition holds; within one track, the map's
   top-to-bottom order says which position is primary.
4. **Overlay blocked states.** For anything sitting in a blocked condition — a ledger
   item graded BLOCKED, an undischargeable gate, a `blocked` verdict recorded by another
   skill — attach the map's route out for that specific block.

## Report

Interactive: for each active position — the evidence that matched (file paths and facts,
so the reader can re-derive it), the position name, and its next move per the routing
contract (a skill invocation, an owner action, or the event being waited on — never just
a state description). Then flags: disk/prose contradictions (disk wins — report, don't
edit), pending owner rulings the roadmap records as gating the next step, and anything
observed that no map row covers (that's a map gap — say so; the fix is a map edit, not
improvisation here).

**Next lifecycle move** (routing contract): the single most actionable move across all
active positions — when tracks are independent, name one move per track and say they
don't wait on each other.

**Headless:** emit only the JSON contract above; the same moves go in `positions[].next`
and the overall `next`.
