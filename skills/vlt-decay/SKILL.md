---
name: vlt-decay
description: Run the vault's mechanical decay verbs over the accumulating agent-zone records — rotate the append-only log (everything before the newest lint header moves to its archive mirror) and drain the dispatch board and backlog (fully-closed history moves whole to the archive). Use when the user says 'rotate the log', 'drain the dispatch board', 'drain the backlog', or 'run vault decay' / 'run vault hygiene' — and proactively when the `log-mass` or `drain-due` tripwire (`{tripwires}`) rings; each wire's surface line names the verb that answers it. Invoked-only; never destruction — archives stay readable markdown at the `{archive}`-mirrored path, and a verb with nothing eligible is a said-out-loud no-op.
---

# vlt-decay

## Overview

The agent zone's operational records accumulate: the `{log}` grows one header per operation forever, `_agent/dispatch.md` keeps every routed block after its items close, `{backlog}`'s `## Done` holds every resolved item. **Decay** is the mechanical exit — two verbs that move **closed, whole, unedited** history to cold storage so the wake-read surface stays lean while the record stays complete:

- **`rotate`** — `{log}`: move everything strictly before the newest `lint` header to `{archive}/_agent/log.md` (`references/rotate.md`).
- **`drain`** — `_agent/dispatch.md` + `{backlog}`: move fully-closed run blocks and `## Done` items to their `{archive}` mirrors (`references/drain.md`). One invocation may run both drains; report what moved per file.

**Tend is not here.** Partner memory is groomed, never drained — `vlt-groom` is that verb's single home (the promotion ladder, the approval gate, the watermarks). The operating contract's *Decay contracts* table registers every file class's verb or exemption; this skill executes the two mechanical ones and nothing else.

Every act obeys the operating contract's *Hygiene and grooming — the safety model* — **cited here, restated nowhere**: retirement by reference, watermarks not ledgers, mechanical lossless-by-reference acts council-free, derivability preserved in the same act.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

The vault is this project — resolve paths through the `vault_structure` map (override wins, else the shipped default). Logical names used: `log` → `_agent/log.md`, `backlog` → `_agent/backlog.md`, `archive` → `_archive/`, `contract` → `_meta/vault-operating-contract.md`, `tripwires` → `_agent/tripwires.yaml`. The dispatch record's home is fixed: `_agent/dispatch.md`. Before any move, JIT-read the contract's *Hygiene and grooming — the safety model* section (including its *Decay contracts* table). Note the **active partner** for the log tag.

## Trigger model — invoked-only

**Hygiene machinery may detect and suggest; only an invocation executes** — `vlt-groom`'s Trigger model is the decide-once home of this idiom, and this skill conforms to it. The `log-mass` and `drain-due` wires and the ledger's vitals block *suggest* a verb; running one happens only on an explicit invocation. No scheduled run, no tripwire-fired execution, no upgrade-time auto-run.

## The verbs

- **Rotate** — read `references/rotate.md` (the cut point, the never-linted refusal, the archive append, the breadcrumb, the reader invariants).
- **Drain** — read `references/drain.md` (block eligibility, the protected blocks, the backlog `## Done` move, the breadcrumbs, the reader invariants).

## Standing rules (act-blocking)

- **Never touch an open (`- [ ]`) row or any `consult:` block.** An open row anywhere keeps its whole block live; consult blocks are permanently drain-exempt (their evidentiary window is unbounded).
- **Never cross the newest `lint` header.** Rotation cuts strictly before it; a `{log}` with no `lint` header refuses loudly (`references/rotate.md`).
- **Never touch the newest `daily/<source>` block per source.** It carries the source's `routed through line N` watermark; draining it would re-route the whole note as duplicates.
- **Never touch `## Open`.** A backlog drain moves `## Done` items only; `## Open` stays byte-identical.
- **Content moves whole and unedited.** Nothing is reworded, summarized, or compressed in flight — archives stay readable markdown, **appended** at the `{archive}`-mirrored path (the contract's archive-structure rule), chronological order preserved.
- **Every run commits** — the live-file cut and the archive append land in one commit (the safety model's append-pairs-with-commit posture; the pre-state stays reachable via git).
- **A verb with nothing eligible is a said-out-loud no-op, never an error.** Re-running a verb is safe by construction: the cut points are content-derived, so a second pass finds nothing and says so.
- **One breadcrumb line per live file, updated in place** — mechanical hygiene metadata beneath the title, never an appended series, never frontmatter on these files.

## Ending the run

Append one partner-tagged **`decay`** entry to `{log}` (this SKILL.md is the type's naming site — the contract's `<type>` set is declared non-exhaustive):

```
## [YYYY-MM-DD HH:MM] decay (<partner>) | rotate|drain: <what moved, in lines/bytes> → [[{archive}/...]]
```

Write **no** session note — the summoning partner owns the session log (operating contract § session-ownership).
