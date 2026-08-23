---
name: acceptance-discharge
description: Discharges a cycle roadmap's deferred acceptance ledger against live-vault upgrade evidence. Use when the user says 'run acceptance discharge'.
---

# acceptance-discharge

## Overview

This skill runs the second half of the module's evolution lifecycle step 8 (live
acceptance): the owner runs `vlt-upgrade` on a live vault, and this skill walks the
resulting evidence back onto the open cycle roadmap's **Deferred acceptance ledger** —
ticking discharged items with dated evidence lines, leaving genuine first-exercise tails
open, filing contradictions back to `factory/inbox/`, and archiving the field filings whose
builds have now passed acceptance. Act as the module's acceptance auditor.

The first half (running the upgrade) is owner-run by standing rule and out of scope. So is
closing the roadmap — that is `cycle-closeout`'s job; this skill's output feeds it. This skill
never closes a cycle and never fixes anything found in the vault.

**Why this exists:** the mapping-evidence-back half is pure discipline, and it silently
failed once — a vault was upgraded and for four days the roadmap ledger, inbox, and project
memory all still said "acceptance pending" while the evidence sat on disk. This skill is the
bell for that boundary. It is also the cheap way to *check* acceptance state at any time: run
it, and it either discharges what's ready or tells you the upgrade hasn't happened yet.

**Lifecycle position:** step 8b (acceptance discharge) of the loop mapped in
`.claude/skills/vlt-lifecycle.md` — see it for the full flow and the routing contract.
Every report this skill emits ends with a **Next lifecycle move** line; a discharge run
must never leave the owner without an actionable next step.

**The vault is read-only without exception.** This skill reads a live vault to gather
evidence and writes nothing into it — no fixes, no cleanup, no annotations. A defect found in
a vault is module signal that files into `factory/inbox/`, never a patch applied in place.
Its only writes are to the factory: the roadmap doc, and `mv` of archived filings.

## Conventions

- Bare paths (e.g. `references/evidence-rubric.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` if
present. Use sensible defaults for anything not configured — this skill needs none beyond
`user_name`/`communication_language` if set.

`--headless` / `-H`: run Discovery → Evidence → Verdict → Archive → Report with no clarifying
questions. Any verdict that would need an owner ruling (a FAILED or BLOCKED item, a subject
substitution on a would-be DISCHARGED item, or an early filing release on a STILL-OPEN
first-exercise tail) is left as-is and surfaced in the report rather than assumed. On
completion, emit only:

```json
{"status": "complete", "roadmap": "{path}", "discharged": N, "still_open": N, "failed": N, "blocked": N, "filings_archived": ["..."], "next": "{next lifecycle move}"}
```

`status` is `blocked` with a one-line `reason` when a verdict genuinely needs an owner ruling
before the run can finish (e.g. a FAILED item whose inbox filing the owner must confirm, or
an ambiguous early-release call).

## Discovery

1. **Find the open cycle roadmap.** Read `factory/CYCLE` — it names the open cycle as
   `NN-<slug>` (or "none" between cycles); the roadmap is
   `factory/cycles/<that>/roadmap.md`. Confirm via its frontmatter `status` that it isn't
   closed/shipped. Its **Deferred acceptance ledger** section holds the unchecked `- [ ]`
   items this run discharges (Arc 3 exemplar: the "Deferred acceptance ledger (Arc 3)"
   section of `factory/cycles/03-enforcement/roadmap.md`).
2. **Enumerate the field vaults.** `{project-root}/CLAUDE.local.md` records every vault this
   machine knows — the primary field vault plus any others it names (including vaults whose
   evidence arrives relayed rather than read directly). Enumerate **all** of them; for each
   locally readable one, read its append-only upgrade record at
   `<vault>/_agent/upgrade-ledger.md` (entry format defined in `vlt-upgrade/SKILL.md`, Step 5).
3. **Gather the acceptance-bearing evidence sources.** Legal evidence sources are: an
   upgrade-ledger entry at or above the open cycle's release version (e.g. Arc 3 → 0.6.0);
   a relayed evidence filing in `{project-root}/factory/inbox/` reporting on a vault's behalf; and
   post-upgrade vault activity (mints, tracked artifacts, overlay use since the upgrade) —
   a discharge run needs no *new* upgrade when vault activity since the last one is the
   evidence. Only when **no evidence source of any kind exists** does the run end here:
   report **"no acceptance evidence yet — acceptance state unchanged"** and stop. That is a
   valid, useful answer, not a failure.

Confirm with the owner (interactive) which ledger items this run covers — all unchecked ones
by default. Then route to the rubric.

## Stages

| # | Stage | Purpose | Location |
|---|-------|---------|----------|
| 1 | Discovery | Find the open roadmap, its unchecked ledger items, and the acceptance-bearing evidence sources across all named vaults | SKILL.md (above) |
| 2 | Evidence & Verdict | Gather each item's named evidence read-only from the vaults/factory and grade DISCHARGED / STILL-OPEN / FAILED / BLOCKED | `references/evidence-rubric.md` |
| 3 | Archive & Sync | Move accepted filings to the open cycle's `filings/`, update roadmap frontmatter status, sync project memory | `references/evidence-rubric.md` |

Route to `references/evidence-rubric.md` — it is self-contained (don't assume this SKILL.md is
still in context by the time it runs).
