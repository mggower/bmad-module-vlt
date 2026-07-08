---
name: vlt-track
description: Run a personalized, evidence-grounded longitudinal loop — design a protocol, log progress, review and adjust over weeks. The shared hand any vertical partner uses to run a program (a dog's training, a body's recomposition, …); the calling partner supplies the loop profile and the voice. Reads the wiki for method, keeps the working record in the agent zone, and writes the polished protocol to a PARA area via personalized-extraction discipline.
depends_on: ["extraction@2", "wiki-supersession@1"]
---

# vlt-track

## Overview

`vlt-track` is the shared hand for a **longitudinal personalized loop**: it **designs a protocol** from what the wiki knows, **logs progress** against it over time, and **reviews and adjusts** as the data comes in. It is the home of the genuinely-new act in the roster — *running a program across weeks*, not answering a one-off question.

It is **persona-neutral and profile-driven** by design — *one verb, many subjects*. The same loop runs a dog's training program and a human's recomposition program; what differs between them is not the verb but the **subject**, and that difference is **parameterization, not a separate skill**. Two things supply the difference at invocation time:

- **The calling partner brings the voice and the non-negotiable.** This skill does not encode a tone or a domain gate — the partner wearing the hand does. When the Dog Trainer runs the loop, the review reads like a behaviorist and the method must be least-intrusive; when the Health Coach runs it, the review reads like a blunt accountability coach and the method must never run past the evidence. The loop is the same; the partner colors it.
- **The calling partner declares a loop profile.** The varying machinery — where the working record lives, where the polished protocol lands, whether there's one subject or many, and which data streams the log keeps — is read from the **loop profile** the partner declares in its own **`capabilities/track.md`** (the heavy `skill: vlt-track` capability pointer, under a *Loop profile* block — see `vlt-mint/assets/capability-template.md`). This skill reads that profile from the invoking partner; it hardcodes none of it.

The loop touches two layers, by design (the maturity split every vertical partner holds):

- **The working record lives in the agent zone** — the profile's *agent-zone root* holds the running progress log(s) and any not-yet-polished drafts. This is partner-operational data (like research notes and session logs), written and maintained by the partner, read freely by the user.
- **The polished protocol lives in PARA** — the profile's *PARA target* holds the curated, human-facing deliverable, written via **personalized-extraction discipline** (see `{conventions}/extraction.md`, *Personalized extraction*). Its `sources:` cite **only the wiki pages** that supply the method (the hard, load-bearing invariant — every method claim traces to a wiki page), and a **separate** `personalization_sources:` field cites the agent-zone log(s) that supply the subject's lived state (situation, not fact). PARA is still written **only through extraction** — this widens what an extraction may cite *for personalization*, it does not open a second write-path.

Conceptual domain knowledge (how a method works, the evidence behind it) is **not** written here — that is wiki knowledge, and it reaches the wiki through the Researcher (`vlt-research`) and the Librarian (`vlt-ingest`). This skill consumes that knowledge; it does not author it. The personalized-extraction allowance this skill performs is **opt-in per the calling partner's gated mint** (see `{conventions}/extraction.md`, *Personalized extraction*): a domain op uses the widening only when its own mint explicitly extended that section to name it. The bound is **not** a standing license; it is the hard invariant, enforced at write-time here and by `vlt-lint`'s personalized-extraction check — **every method/general claim traces to a wiki page in `sources:`**, and `personalization_sources:` carries the subject's lived state, never method.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the `vlt` config is missing, tell the user `vlt-setup` can configure the module, then ask for a vault root to proceed.

The vault is this project — resolve every path relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). Logical names used (default, relative to the project root): `index` → `_agent/wiki/index.md`, `wiki` → `_agent/wiki/`, `log` → `_agent/log.md`, `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/` (vault-local convention overlays).

**Read the loop profile (the parameterization).** This skill is run by a partner; read that partner's **loop profile** from its **`capabilities/track.md`** (the heavy `skill: vlt-track` capability pointer) and bind these for the rest of the run:

- `{root}` — the **agent-zone working root** (e.g. `_agent/training/{dog}/`, `_agent/health/`). The contract sanctions ad-hoc owned folders under `_agent/`.
- `{target}` — the **PARA target** for the polished protocol (e.g. `areas/dog-training/{dog}/`, `areas/health/`).
- the **subject model** — *multi-subject* (scoped under a slug, e.g. `{dog}`; ask which if not named) or *single-subject* (one body — no nesting).
- the **data streams** — which agent-zone file(s) the log beat appends to and what each holds (e.g. a single `progress.md`; or `body-log.md` + `strength-log.md` + a per-block `program.md`).
- the **log tag** — the active partner's slug for the `{log}` line (e.g. `dog-trainer`, `health-coach`).
- the **non-negotiable gate** — the calling partner's specific method gate, named in its profile (e.g. Dog Trainer: *least-intrusive / LIMA*; Health Coach: *never past the evidence, evidence-strength stated*). Apply it at the design beat **and** re-assert it at the write — it is the gate that decides whether a method may be written at all, so it is checked, not assumed (see Verify).

If invoked headless with no partner context, take the profile from the named owning partner's **`capabilities/track.md`**, or ask for the missing pieces — never guess `{root}`/`{target}`.

Before writing anything, JIT-read the governance conventions this operation obeys from `{conventions}`: at minimum `frontmatter.md` (the PARA-artifact schema and YAML rules) and `extraction.md` (the personalized-extraction rule and its hard invariant, the trust ladder, filename and re-extraction supersession discipline) — read each together with its `{overlays}/{name}.overlay.md` if present, honoring the overlay's appended rules. The protocol write is an extraction — honor that convention exactly.

Determine which beat of the loop the user is on — **design**, **log**, or **review/adjust** — from their ask.

## Design a protocol

Establish, in a short exchange (not a numbered interrogation): the **goal**, the subject's **current level**, and any **constraints** (the user's schedule, the subject's history). Then:

1. Read `{index}`, then read fully the wiki pages that supply the **method** for this goal. The protocol's grounding is the wiki — if the wiki is too thin on the method to ground the plan honestly, **stop and hand off**: the goal needs a Researcher dive (`vlt-research`) → Librarian ingest (`vlt-ingest`) first. A protocol grounded in nothing is exactly what the partner's non-negotiable forbids.
2. Read the subject's existing agent-zone record under `{root}` if present (its progress log(s), prior protocols), so the plan meets the subject where it actually is.
3. Synthesize a **personalized protocol** — concrete, staged steps with criteria for advancing, shaped by the subject's level and the user's constraints, every method choice traceable to a wiki page and honoring the calling partner's non-negotiable (least-intrusive option / never past the evidence / …).
4. Write it to PARA as a **personalized extraction** (see the write spec below). For a substantial protocol, draft to `{target}/{slug}.draft.md` first so multi-turn work survives interruption; drop the suffix on confirm.

## Log progress

Append a dated entry to the relevant **data stream** under `{root}` (create the file and `{root}` on first use). Capture what was worked, the reps/duration/measurement, what improved, what stalled, and any observation about the subject — read the *subject and the data*, not just the outcome. Keep it terse and scannable; this is the operational record the review beat reads back. This is an **agent-zone write only** — no PARA touch, no extraction discipline.

A profile may declare **more than one stream** (e.g. a body-metrics log and a strength log kept separately because they have different cadences and parse shapes); append to the one the entry belongs to. Some profiles also **import a per-block plan** (e.g. a training block delivered as a PDF/sheet) into a `program.md` under `{root}` — the imported structured store is the source of truth for the loop, never a live external document.

**Operational-log discipline (single-home).** A progress/data log holds **state, never general/method knowledge** — *what this subject did*, not *how a method works*. If you find yourself wanting to write down a general principle or a method fact, that is wiki knowledge: send it to the Researcher/Librarian, don't park it in the log (parking it would create a second home for a fact the wiki should own). The log records the subject's situation so the protocol can be personalized to it; it is never a back-door provenance for a method claim.

Agent-zone log files are continuously-appended: `type: note`, `author: agent`, `trust: raw`, `created` + `last_updated`, `partner: {log tag}` for attribution. Entries are reverse-or-forward chronological under dated `## ` headings — pick one order and hold it.

## Review and adjust

Read the subject's stream(s) under `{root}` and the active protocol, and read them *back* to the user the way the calling partner would: surface trends (what's advancing, what's plateaued), reframe frustration to mechanism, and recommend a concrete adjustment grounded in the wiki and the partner's non-negotiable. Where a profile keeps a metric trend (e.g. a 7-day weight average, a strength curve), interpret the **trend, not the noisy point** — and interpret it *for the goal* (e.g. holding strength at maintenance reads as recomposition working), with the interpreting principle traced to a wiki page.

If the adjustment changes the protocol, **re-extract it in place** (overwrite `{target}/{slug}.md`, bump `last_updated`, apply `[!superseded]` callouts for materially changed steps per `{conventions}/wiki-supersession.md`) — never spawn a near-duplicate protocol file.

## The protocol write — personalized-extraction spec

The protocol is a PARA artifact governed by `extraction.md`. Write `{target}/{slug}.md` with:

```yaml
---
type: area                          # matches the PARA target folder
created: YYYY-MM-DD                  # immutable
last_updated: YYYY-MM-DD             # set today; bump on every re-extraction
title: <human-readable title, e.g. "Penny — Loose-Leash Protocol" / "Recomposition Protocol">
author: hybrid
trust: reviewed
topic:
  - <domain, e.g. dog-training / health>
  - <goal facet, e.g. loose-leash / recomposition>
status: ongoing
sources:                             # WIKI PAGES ONLY — the method grounding (bare page references)
  - <wiki page 1>
  - <wiki page N>
personalization_sources:             # SEPARATE field — agent-zone state, never a method-claim provenance
  - <root>/<stream file 1>
  - <root>/<stream file N>
---
```

Follow every `extraction.md` rule: `author: hybrid`, `trust: reviewed` by depth, stable kebab-case slug (no datetime prefix), near-duplicate check in `{target}` before creating, re-extraction overwrites in place with supersession callouts. The one widening from a standard extraction is the **soft parameter** — what the extraction may cite *for personalization*: the subject's agent-zone stream(s) go in `personalization_sources:`, a **separate** field from `sources:`. The **hard invariant is unchanged** — `sources:` lists only wiki pages and every method/general claim in the body traces to one of them; the log supplies situation, not fact. Keeping the two in distinct fields is what keeps that invariant mechanically checkable. No `key:` field.

The calling partner's use of personalized extraction **must already be sanctioned by its own gated mint** (the mint that extended `extraction.md`'s *Personalized extraction* to name the op — see that convention). If you are running a loop for a partner whose op was never granted the widening, **stop** — the allowance is earned through a gated mint, not taken here.

## Log

Append one partner-tagged entry to `{log}` in the operating-contract format, using the profile's **log tag**. Use `extract` as the type when the beat wrote the PARA protocol (it is an extraction), and a short prose summary for a log-only or review-only beat (no `→` needed when nothing was filed):

```
## [YYYY-MM-DD HH:MM] extract ({tag}) | "<Title>" — N wiki sources + <stream> → [[<target>/<slug>]]
## [YYYY-MM-DD HH:MM] track ({tag}) | logged <subject> <stream> — <one-line> → [[<root>/<stream>]]
```

(`track` is this skill's own log type for the agent-zone beats; the contract's type set is non-exhaustive in the same way its `type:` set is.) Write **no** session note — the owning partner owns the single session note for the sitting (operating contract § session-ownership).

## Verify

When the beat wrote a PARA protocol, re-read it and confirm against the extraction checklist — frontmatter complete and correct (`type:` matches `{target}`, `author: hybrid`, `trust` by depth, no `key:`), every `[[wikilink]]` resolves, it reads as a shaped protocol not a wiki dump, the near-duplicate check ran. **Firewall check (the load-bearing one):** `sources:` holds **wiki pages only**, the agent-zone stream(s) are under `personalization_sources:` and **not** in `sources:`, **every method/general claim in the body traces to a wiki page in `sources:`** (a claim supported only by a `personalization_sources:` entry is a violation — ground it in the wiki, or cut it), and the calling partner's op carries the gated personalized-extraction sanction (`extraction.md`, *Personalized extraction*). **Non-negotiable re-check (the gate, not the tone):** re-assert the calling partner's **named non-negotiable gate** from its loop profile against the written protocol — every method choice is the least-intrusive option the evidence supports (Dog Trainer) / does not run past the evidence and states its strength honestly (Health Coach) / the partner's own gate. This is the gate that licenses the write; if a step fails it, fix or cut the step before closing — do not leave it to assumed adherence. When the beat only logged progress, confirm the entry landed in the right `{root}` stream, the file's `last_updated` bumped, and **no general/method knowledge leaked into the log** (state only — see *Operational-log discipline*). In all cases confirm the `{log}` entry was appended and is partner-tagged. Report the result; fix gaps before closing.
