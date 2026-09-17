---
spike: 'S-4'
slug: 'vault-claude-md-imports-per-session-kind'
run: '2026-09-17'
runtime: 'Claude Code 2.1.274 (`~/.local/share/claude/versions/2.1.274`, bun-compiled arm64 binary)'
verdict: 'proceed'
---

# S-4 harvest — do vault `CLAUDE.md` `@imports` reach every session kind?

**Answer: yes, for every session kind probed — and a pointer without `@` reaches none of them.**

## The instrument (why this is an observation, not a self-report)

A model asked "is the passphrase in your context?" can answer from the question itself, so the
model's word is not the evidence here. The runtime writes, at every session's first turn, an
**attachment record** into the session transcript listing each instruction file it delivered —
`{type, path, content}` per file. That record is the instrument: it is written by the runtime
before any model turn, it names the `@`-imported file **as its own entry** beside the `CLAUDE.md`
that imported it, and it cannot be produced by a model guessing.

Every row below carries **both**: the attachment record (authoritative) and an unforgeable
passphrase probe (corroborating). The passphrases live only inside the imported files and are never
named in the prompt — the prompt asks for *the* passphrase, so `UNKNOWN` is the honest answer from a
session that did not receive the file.

**Probe vault** (scratch, disposable): a root `CLAUDE.md` carrying `@_meta/imported-card.md` and a
prose pointer naming `_meta/pointer-only.md` *without* `@`; the imported card carrying
`ZEPHYR-7731` and a second-level `@nested-card.md` carrying `CINDER-9912`; the pointer-only file
carrying `OBSIDIAN-4420`; a `.claude/settings.json` registering a `SessionStart` command hook that
appends to `hook.log`; and a `.claude/skills/probe-partner/SKILL.md` standing in for a partner summon.

## Results

| # | Session kind | How it was produced | Attachment record | Probe reply | `SessionStart` |
|---|---|---|---|---|---|
| 1 | **Interactive** (CLI, at a project root) | this live session, factory repo | `Project CLAUDE.md` + `Project CLAUDE.local.md` + `User CLAUDE.md` + `User RTK.md` — both `@`-imports delivered as their own entries | n/a (observed directly in context) | fires (`source: startup`) |
| 2 | **Headless op** (`claude -p`) | probe vault, `--model` haiku | `Project CLAUDE.md` + `Project imported-card.md` (+ nested) | `IMPORT=ZEPHYR-7731 NESTED=CINDER-9912 POINTER=UNKNOWN` | fires (`source: startup`) |
| 3 | **Partner summon** (skill activation inside a session) | headless session that first invoked `probe-partner`, then answered | same as row 2 | `IMPORT=ZEPHYR-7731 POINTER=UNKNOWN`, after the summon line | fires once, at session start — the summon adds none |
| 4 | **Agent-tool subagent** | `Agent(general-purpose)` spawned inside a probe session | own sidechain transcript carries `Project CLAUDE.md` + `Project imported-card.md` | `IMPORT=ZEPHYR-7731 POINTER=UNKNOWN` | **does not fire** — 3 CLI invocations produced exactly 3 `hook.log` lines; the spawn produced none |
| 5 | **Workflow `agent()` subagent** | a one-agent `Workflow` run (the engine `vlt-consult.js:160` actually calls) | sidechain transcript carries `Project CLAUDE.md` + **`Project CLAUDE.local.md`** + `User CLAUDE.md` + `User RTK.md` + `AutoMem MEMORY.md` — the `@`-imports delivered whole | see §*Corroboration* | not probed (see *Limits*) |
| 6 | **Headless, cwd = a vault subdirectory** | `claude -p` run from `_meta/` | root `CLAUDE.md` + both imports, resolved from the **vault root**, not from cwd | `IMPORT=ZEPHYR-7731 NESTED=CINDER-9912 POINTER=UNKNOWN` | fires (`source: startup`) |

**Three facts hold across every row:**

1. **`@path` imports load.** In all six kinds the imported file arrives as a first-class instruction
   entry, not as a path the session must go read.
2. **A pointer without `@` loads nothing.** `POINTER=UNKNOWN` in every probe that was asked, and
   `pointer-only.md` appears in **no** attachment record anywhere in the run. A `CLAUDE.md` sentence
   naming a path is an instruction to go read it, not a carrier.
3. **Imports are transitive and root-relative.** A second-level `@nested-card.md` inside the imported
   card loaded in every kind asked for it, and the whole set resolved from the vault root even when
   the session's cwd was a subdirectory.

## What this means for A16-3 direction 1

The two lines A16-3 proposes for the `vlt-setup` §3 seed —

```
@_meta/vault-rule-card.md
@_agent/reflexes.md
```

— **do carry governance to every session kind the module runs**, including the partnerless session
the filing exists for, and including both subagent kinds (which is the carriage A16-7's delegate
runner and `vlt-consult.js`'s lite boot inherit, per the roundtable's D-5 symmetric ruling). The
direction is grounded. `verdict: proceed`.

**The fallback is now known to be the weaker carrier, and the spike's instruction to record it is
what showed that.** The `SessionStart` hook (`vlt-setup/SKILL.md:187`, `vlt-vitals.py --strip`) fires
once **per CLI session start** and **not** for an in-session subagent spawn: the Agent-tool row
produced no hook line at all. So a hook-carried rule-card reaches rows 1–3 and 6 and **misses row 4**
— exactly the kind the delegate runner is. Imports reach all of them. If build 3 ever has to choose,
it should not choose the hook.

## Corroboration, row 5

The workflow agent's own structured return, verbatim:

```json
{"instructionFileBasenames":["CLAUDE.md","RTK.md","CLAUDE.local.md","MEMORY.md"],
 "sawProjectClaudeMd":true,"sawImportedLocalFile":true,
 "note":"The startup system-reminder printed each file with its full path: the global CLAUDE.md with
 its @RTK.md import, the project CLAUDE.md with its @CLAUDE.local.md import, and the auto-memory
 MEMORY.md."}
```

It agrees with the attachment record entry for entry. It is corroboration only — the attachment
record above is the finding, and it was read out of the transcript the runtime wrote before the
agent's first turn. (Run `wf_e966db78-4bd`, 1 agent, 0 errors.)

## Limits — what this run does NOT establish

- **The hook's reach for row 5 was not probed.** The scratch vault carried the hook; the workflow run
  had to happen in the factory repo (the `Workflow` tool refused to run inside `claude -p`, so it
  could not be pointed at the probe vault). Row 5's hook cell is honestly blank, not assumed. It is
  an in-session spawn like row 4, so the row-4 result is the expectation — but expectation is not
  this spike's currency.
- **No size or depth ceiling was measured.** Two import levels were observed to load; the runtime
  binary carries a `CONTEXT_MAX` of 32000 and a `withinCap` guard, but those strings sit in the
  binary's `agents-md` plugin module (off by default), not in the core path this run exercised. **A
  budget question about what happens when the imported governance set grows is open and is not this
  spike's to answer** — it is A16-4's territory, and build 3 should not assume "imports load" means
  "imports load without bound".
- **Row 1 was observed in the factory repo, not a vault.** The mechanism is the same (a project-root
  `CLAUDE.md` with `@`-imports) and the attachment record is identical in shape, but no interactive
  session was run inside the probe vault — a TTY session cannot be driven from this harness.
- **One runtime, one version.** 2.1.274 on darwin/arm64. Nothing here is a promise about other
  versions; the import behavior is runtime behavior, not a module contract.
