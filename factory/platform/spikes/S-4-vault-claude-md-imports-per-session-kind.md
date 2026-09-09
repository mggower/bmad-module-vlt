---
id: 'S-4'
slug: 'vault-claude-md-imports-per-session-kind'
status: 'proposed'
question: 'Does an `@path` import line in a vault-root CLAUDE.md load for EVERY session kind the module runs in the current Claude Code runtime — interactive, headless op (`claude -p`), partner summon, and subagent — or only for some; and does the same hold for a CLAUDE.md pointer that names a path without `@`?'
opened: '2026-09-09'
opened_by: 'capture — Cycle 16 (A16-3, the partnerless governance carrier — direction 1 rests on it)'
timebox: 'one session: read the runtime (the installed Claude Code CLI''s import handling — its source or its observable behavior on a scratch vault), not its docs; run one probe per session kind with a canary line in an imported file and record which kinds echo it'
verdict: ''
sources: []
findings: ''
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

**Consumers:** A16-3's brief (direction 1 is ungrounded until this is harvested); A16-5's cold summon
(which reads the card + rung through whichever carriage this spike proves).
