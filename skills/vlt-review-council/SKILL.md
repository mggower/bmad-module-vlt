---
name: vlt-review-council
description: Run a persona-lens panel over a mint or a contested question and synthesize a structured verdict. Use when a partner says 'debate this', 'run the panel on X', 'review-council on Y', or 'get the lenses on this'. Produces a Consensus / Disputed-resolved / Disputed-open / Recommended-actions verdict.
---

# vlt-review-council

## Overview

A panel is not a vote and not a brainstorm — it is a set of **fixed lenses** applied in parallel to one subject, then synthesized into a structured verdict. Each persona optimizes a single distinct axis; the value of the roster is that its members produce *observably different* signal. A moderator, who holds no stance, maps their positions into a verdict the caller can act on. This is the module's evolution-review gate — discipline applied only where blast-radius warrants it, replacing the old spec/verify ceremony.

**The panel engine is a dynamic workflow** — `vlt-review-council` (installed at `{project-root}/.claude/workflows/vlt-review-council.js`). It spawns the selected lenses in parallel, forces each into a structured `VERDICT`, and has the moderator synthesize the four-part result — so a caller gets a typed verdict back (invoke-and-return) and the reasoning is always captured, never reconstructed from prose. This SKILL is the **conversational front**: it resolves the subject and the live paths, invokes the workflow, and routes the verdict. `vlt-mint` invokes the *same* workflow directly to gate a mint (it does not go through this SKILL).

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config, no `_meta` governance, or no `.claude/workflows/vlt-review-council.js` in this project), tell the user `vlt-setup` can configure it (it installs both the governance bundle and the council workflow).

The vault is this project — resolve paths relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). You need the **live, absolute** `{personas}` directory (default `_meta/personas/`) to hand the workflow — resolve `{project-root}` to the real path so the lenses read the live tree, not a plugin-cache copy. Also resolve `{wiki}` / `{research}` for grounding a debate, and note the **active partner** (for attribution if a verdict is filed).

## Step 1: Resolve mode and subject

- **Debate a contested question** (this SKILL's primary entry) — a partner or the user supplies the question and the relevant context. `mode: 'debate'`. Don't run a panel on a settled question; a council exists for genuinely contested or blast-radius-bearing calls.
- **Review a mint** — this is normally invoked by `vlt-mint` calling the workflow directly with `mode: 'mint'` + the mint `kind`. You only handle it here if a user explicitly asks you to run a mint-review by hand, in which case mirror what `vlt-mint` would pass.

For a debate, assemble the `subject` as the question plus the relevant context, **including the live absolute paths** of any `{wiki}`/`{research}` files the lenses should ground in (the workflow tells each lens to read referenced paths from the live tree).

## Step 2: Invoke the workflow

Call the panel engine via the Workflow tool:

```
workflow('vlt-review-council', {
  mode:         'debate',                 // or 'mint' if running a mint-review by hand
  kind:         <mint kind>,              // mint mode only — drives panel selection
  subject:      <question + context + live paths to ground in>,
  personasPath: <resolved LIVE absolute path to {personas}>,
  lenses:       [<optional narrower lens set>],   // debate may narrow; the moderator is always included
})
```

The workflow selects the panel (full panel for a debate, the fixed `kind → council` map for a mint), spawns the lenses in parallel (independent reads — they don't see each other's positions), and returns the structured verdict: `consensus` / `disputedResolved` / `disputedOpen` / `recommendedActions` (plus `verdict` = pass/revise/reject for a mint). It degrades gracefully if a lens persona is missing.

## Step 3: Return or file the verdict

- **Debate** → return the verdict to the summoning partner / user. If it's worth preserving, **hand it to the Librarian** (`vlt-ingest`) to file — typically as a `{research}` note capturing the question, the positions, and the verdict. The council never writes canonical wiki pages itself (single-writer); the Librarian files and logs. If the verdict isn't worth keeping, it lives in the partner's session note.
- **Mint review run by hand** → return the verdict; `vlt-mint` owns recording it and gating the mint. (When `vlt-mint` invokes the workflow itself, capture is part of its Step 2a — not this SKILL's job.)

## This skill does not…

- Write to `{wiki}`, PARA, `sources/`, or the human zones — a file-back flows through the Librarian.
- **Re-implement the panel in prose** — the workflow is the one engine; this SKILL invokes it, it does not hand-spawn lenses.
- **Implement** a debate's recommendation or a mint — it produces the verdict; building is `vlt-mint`'s or a partner's job.
- **Guess** its mode or fabricate a `kind` — the caller names them.
- Promote a persona or run a retrospective — there is no retro mode; reflection re-homes into the partners and the backlog.
