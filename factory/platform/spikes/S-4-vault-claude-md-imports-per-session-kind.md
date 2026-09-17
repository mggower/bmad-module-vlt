---
id: 'S-4'
slug: 'vault-claude-md-imports-per-session-kind'
status: 'harvested'
question: 'Does an `@path` import line in a vault-root CLAUDE.md load for EVERY session kind the module runs in the current Claude Code runtime — interactive, headless op (`claude -p`), partner summon, and subagent — or only for some; and does the same hold for a CLAUDE.md pointer that names a path without `@`?'
opened: '2026-09-09'
opened_by: 'capture — Cycle 16 (A16-3, the partnerless governance carrier — direction 1 rests on it)'
timebox: 'one session: read the runtime (the installed Claude Code CLI''s import handling — its source or its observable behavior on a scratch vault), not its docs; run one probe per session kind with a canary line in an imported file and record which kinds echo it'
verdict: 'proceed'
sources:
  - 'Claude Code CLI 2.1.274 (`~/.local/share/claude/versions/2.1.274`, bun-compiled arm64 binary) — the runtime itself, probed by observation; its embedded strings read for the `workflow-subagent` agent-type registration and the `agents-md` plugin''s `CONTEXT_MAX`/`withinCap`'
  - 'Session transcripts written by that runtime — the startup **attachment record** naming each delivered instruction file (`{type, path, content}`), read for six session kinds incl. two sidechain/subagent transcripts'
  - 'A disposable probe vault built for this run: root `CLAUDE.md` with one `@`-import + one no-`@` prose pointer, a second-level `@`-import, a `SessionStart` command hook, and a stand-in summon skill'
  - '`skills/vlt-setup/assets/workflows/vlt-consult.js:160` — confirms the workflow-`agent()` kind is the engine actually in use, so row 5 probes the real thing'
findings: 'factory/cycles/16-closed-loops/spike-s-4-claude-md-imports-2026-09-17.md'
consumed_by: []
legacy_id: ''
---

# S-4 — do vault `CLAUDE.md` `@imports` reach every session kind?

## The question, in full

Cycle 16's A16-3 (filing `2026-09-09-160000`) asks that governance ride a surface **every** session
reads, because the rule-card and the vault rung reach a session only through the partner activation
ritual today (`vault-operating-contract.md:194`, `:226`). The filing's direction 1 adds two import lines
to the `CLAUDE.md` that `vlt-setup` §3 seeds (`skills/vlt-setup/SKILL.md:198–216`):

```
@_meta/vault-rule-card.md
@_agent/reflexes.md
```

That only carries governance if the runtime loads `@path` imports for *every* kind of session the
module runs. **What a real source would have to say:** for each of — an interactive session at the
vault root; a headless `claude -p` op; a partner summon (a skill activation inside an interactive
session); a subagent spawned by a workflow or the Agent tool — whether a line in an `@`-imported file
is present in the session's context at its first turn. A docs page saying "CLAUDE.md supports imports"
does not answer it; the per-kind observation does.

**Fallback if any kind fails:** the vault already registers a `SessionStart` hook
(`vlt-setup/SKILL.md:187`, `vlt-vitals.py --strip`), and a session-kind that runs the hook can carry
the card through it. The spike should record which kinds run that hook too, so the fallback is
grounded in the same run.

**Consumers:** A16-3's brief (direction 1 is ungrounded until this is harvested); A16-7's delegate
runner (`vlt-delegate.js`) and, by the same ruling, `vlt-consult.js`'s lite boot — both are the
**workflow-`agent()` subagent kind**, which this spike probes on its own row (record whether the
`SessionStart` hook fires for an in-session spawn as well as whether imports load). Whatever this
row shows applies to both engines alike (Cycle 16 roundtable, D-5 owner-ruled symmetric).
*Corrected 2026-09-16 by the Cycle 16 roundtable (A5): this line previously named "A16-5's cold
summon (which reads the card + rung through whichever carriage this spike proves)" — the cold
summon reads through the activation ritual and is **not** a tenant of the carrier (ideation D6);
the register contradicted the ruling and is the record, so it is corrected here, not in roadmap
prose only.*

## Ruling (Cycle 16 ideation, round 2, 2026-09-16)

**RUN IT** — owner-ruled. Binds **Cycle 16 build 3** (`spike: S-4`; A16-3 direction 1 + the A16-7
delegate runner's carriage). The cycle's single release is conditional on this spike being harvested
before build 3 is briefed; builds 1 and 2 do not wait. Kill and rule-around (the `SessionStart` hook
as carriage) were both declined: the hook's per-session-kind reach is the same unknown, so the run
must record which kinds fire the hook as well as which load imports. `status:` moves to `running`
when the probing session opens.

## Harvest (2026-09-17) — `verdict: proceed`

Full artifact: `factory/cycles/16-closed-loops/spike-s-4-claude-md-imports-2026-09-17.md` (this entry
is the pointer, not a copy).

**`@path` imports load for every session kind probed** — interactive, headless `claude -p`, a summon
inside a session, an Agent-tool subagent, a **workflow-`agent()` subagent** (the engine
`vlt-consult.js:160` actually calls), and a session whose cwd is a vault subdirectory. Imports are
**transitive** (a second-level `@` loaded) and resolve **from the vault root**, not from cwd. A
`CLAUDE.md` pointer that names a path **without** `@` loaded in **none** of them. A16-3 direction 1
is grounded.

The evidence is the runtime's own startup **attachment record** — the per-file list it writes into the
transcript before any model turn, in which an `@`-imported file appears as its own entry beside the
`CLAUDE.md` that imported it. Passphrase probes corroborate; no finding rests on a model's self-report.

**The spike's fallback question is answered too, and it changes the fallback's standing:** the
`SessionStart` hook fires once per **CLI session start** and **not** for an in-session subagent spawn
(the Agent-tool row produced no hook line). So the hook misses exactly the kind A16-7's delegate
runner is, while imports reach it. Two limits recorded in the artifact and not papered over: the
hook's reach for the workflow kind was not probed, and **no size/depth ceiling was measured** — that
budget question is A16-4's, and build 3 must not read "imports load" as "imports load without bound".
