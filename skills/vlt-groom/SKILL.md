---
name: vlt-groom
depends_on: ["frontmatter@9"]
description: Run an approval-gated groom pass over one partner's memory files (identity.md, thread.md, reflexes.md) — classify every item against the promotion ladder and propose promote / compress-to-latest-form / retire as a diff grouped by class, one-line rationale per item, applied only on the user's approval. Use when the user says 'groom the librarian', 'groom <partner>', or 'run a groom pass' — or when the active partner has proposed a groom and the user says go. Invoked-only; runs inside the target partner's own sitting (the partner is the writer, this op is the procedure). Never destruction — the pre-groom state stays reachable via the `archive:` watermark.
---

# vlt-groom

## Overview

Partner memory accumulates: standing reads stack revisions, closed inquiries linger, rules hide as narrative. A **groom pass** is the hygiene act that moves it back into shape — **one partner, its three memory files (`identity.md`, `thread.md`, `reflexes.md`), the three verbs executed as one gated pass**: **promote** (up a ladder rung), **compress-to-latest-form** (a standing read's revision stack becomes its latest form), **retire** (a fired falsifier, closed item, or dead inquiry leaves the file — by reference, never deletion). The ladder, the verbs, and their entry criteria live in the operating contract's *Partner memory — identity, thread, and reflexes* section; every act of this op obeys the contract's *Hygiene and grooming — the safety model* — **cited here, restated nowhere**. Bond material is intimate: nothing is ever silently deleted, and nothing applies without the user's approval.

The op constrains **form and safety**; the partner supplies **judgment** (what is dead vs merely quiet, which rung, how a compressed form reads). That split is deliberate — see the pass protocol.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

The vault is this project — resolve paths through the `vault_structure` map (override wins, else the shipped default). Logical names used: `partners` → `_agent/partners/`, `log` → `_agent/log.md`, `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/`, `contract` → `_meta/vault-operating-contract.md`. Before any classification or write, JIT-read the contract's *Partner memory* and *Hygiene and grooming — the safety model* sections, and `{conventions}/frontmatter.md` (the partner-memory schemas and the *Hygiene watermarks* fields) together with `{overlays}/frontmatter.overlay.md` if present — never write watermarks from memory.

**The seat — who runs a groom.** Partner memory is the partner's **own zone**; an outside writer would cross the single-writer line. So a groom runs **inside the target partner's sitting**: invoking "groom the librarian" summons the Librarian, who runs this op on its own files. If another partner is at the wheel, this is a hand-off — the target partner's sitting begins, and the groom (its `{log}` entry, its session-note line, its commit) is attributed to the target partner. The op is the procedure; **the writer identity is always the partner being groomed**.

## Trigger model — invoked-only

**Hygiene machinery may detect and suggest; only an invocation executes.** A partner may *propose* a groom at a natural seam — end-of-sitting, reflex-cap pressure, a correction-as-signal recurrence — and a tripwire or vitals surface may *suggest* one. Proposing is free; **executing happens only on the user's explicit go**. No scheduled run, no tripwire-fired execution: the approval gate needs the user present, and invoked-only puts the user there by construction.

## The pass

Run the full protocol in `references/groom-pass.md` — the codified steps (pre-flight commit, whole-file reads, classify, stage, render the gated diff, halt, apply on approval), the diff-rendering contract, the decline markers and re-proposal rule, and the `groom` log-line format.

## Standing rules (act-blocking)

- **Never groom any partner other than the active one.** One invocation, one partner, its own files — no cross-partner writes, ever.
- **The partner's SKILL.md is untouchable.** Changing who the partner fundamentally is is council-gated rebirth territory (the contract's two-tier identity line), never a groom act.
- **A wiki-rung promotion is never a direct wiki write.** It renders in the diff as a proposed **Librarian hand-off** (relay) — single-writer holds at the wiki lane.
- **Nothing applies without the gate.** The proposal halts for the user's ruling; declined or unapproved material stays **byte-identical**. There is no ungated in-place rewriting of records.
- **No groom ledger, no decline registry.** A decline is recorded **inline in the material itself** (keep-with-marker); progress state lives in the files' own `groomed:`/`archive:` watermarks (`frontmatter.md`, *Hygiene watermarks*) — never in a new ever-growing ledger.
- **`capabilities/` files are out of scope.** They are contracts, not memory — no ladder rung homes there; `vlt-lint`'s duty over them is untouched.
- **The staging directory is transient.** Deleted on apply and on abort — git carries the history; no proposal file outlives the pass.

## Ending the run

The op appends its own partner-tagged **`groom`** entry to `{log}` (format in `references/groom-pass.md`) and adds one line to the sitting's session note; it **never owns the session note** — the partner does, at end of sitting (operating contract, session-ownership rule).
