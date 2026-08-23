---
name: inbox-capture
description: Grounds inbox field filings against module source and folds them into the cycle roadmap. Use when the user says 'run inbox capture'.
---

# inbox-capture

## Overview

This skill runs the Capture step of the module's evolution lifecycle: it turns raw field
filings in `factory/inbox/` into a grounded, durable roadmap under `factory/cycles/`. Act as
the module's field-intake analyst. For each un-captured filing, verify its claims against the
actual current module source (never trust a filing's self-description — filings
mis-attribute provenance and guess wrong fixes often enough that this is the whole point of
the step) and fold the grounded result into the current cycle's roadmap doc — creating one if
the last cycle has shipped and closed. Ideation and build-briefing (turning a captured roadmap
entry into a scoped, buildable brief) are a separate, owner-steered step and out of scope
here — this skill's output is a grounded roadmap, not a build plan.

**Lifecycle position:** step 2 (Capture) of the loop mapped in
`.claude/skills/vlt-lifecycle.md` — see it for the full flow and the routing contract.
Every report this skill emits ends with a **Next lifecycle move** line.

## Conventions

- Bare paths (e.g. `references/grounding-methodology.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` if
present. Use sensible defaults for anything not configured — this skill needs none beyond
`user_name`/`communication_language` if set.

`--headless` / `-H`: skip straight through Discovery → Grounding → Synthesis with no
clarifying questions; every judgment call this run made without the user gets a line in the
roadmap doc's own capture narrative (there is no separate decision log for this skill — see
Synthesis). On completion, emit only:

```json
{"status": "complete", "roadmap": "{path}", "filings_captured": ["{inbox paths}"], "issues_materialized": ["<repo>#<n>", "..."], "next": "{next lifecycle move}"}
```

`issues_materialized` is the empty list when the run materialized nothing (including a
skipped intake). `status` is `blocked` with a one-line `reason` if grounding turned up something the user must
rule on (e.g. a filing's core claim conflicts with a recent, unshipped module change).

## Discovery

**GitHub intake (first, so a freshly materialized filing joins this run's un-captured
set).** Read the transport repo from `feedback_repo.default` in
`skills/vlt-setup/assets/module.yaml` (the factory reads the module source default — it has
no vault `config.yaml`), then run the intake per `references/github-intake.md` (query,
stale-shape gate, idempotence exclusion, materialization, `captured` transition, amendment
leg — the mechanics live there). The one invariant, inline: **materialization is triggered only by
the owner-applied `vault-accepted` label — `vault-filed` marks candidacy, not admission
(A15(a)); the field contract, labels, and `origin:` header shape are single-homed at
`skills/vlt-feedback/references/field-contract.md` — point, never restate.** Degrade
loudly: if `gh` is unavailable or unauthenticated, say so by name and continue with the
filesystem-only Discovery below — the intake half is skipped, never silently "empty".

List `factory/inbox/*.md` — these are the un-captured filings this run may fold in.
(Consumed filings live at `factory/cycles/NN-<slug>/filings/` under the cycle that captured
them; there is no inbox archive.) Read `factory/CYCLE`: if it names a cycle `NN-<slug>`,
open `factory/cycles/NN-<slug>/roadmap.md` and read its frontmatter `status` — that roadmap
is the **open cycle** this run appends to only if its `status` isn't closed **and its
builds have not yet shipped** (no release cut for the cycle). A cycle that has shipped but
still awaits acceptance/closeout is **closed to capture** — it stays open for
`acceptance-discharge` and `cycle-closeout`, but new filings belong to the *next* cycle:
start it (number = one past that cycle's), even while the prior cycle is still discharging.
If `factory/CYCLE` reads `none` or no roadmap qualifies, likewise start a fresh cycle
(number = one past the highest existing cycle directory). Starting a cycle means: create
`factory/cycles/NN-<slug>/roadmap.md` (slug chosen from the cycle's theme, as roadmap
titles were) **and write the `NN-<slug>` line into `factory/CYCLE`** — this skill opens the
cycle; `cycle-closeout` resets the pointer to none.

*(Rule sharpened 2026-07-29 by owner ruling: the A4-6..A4-23 batch was captured into Arc
4's roadmap three days after Arc 4 shipped, solely because Arc 5 hadn't been scaffolded —
post-ship filings had to be re-slugged into Arc 5. Capture ids carry the cycle they are
captured into; ship day, not closeout day, is the capture boundary.)*

**Mid-cycle capture addendum** *(platform P-4, 2026-08-22)*. An open cycle whose current
batch is already ideation-ruled and roundtable-stamped is still open to capture — but never
by silently widening a ruled build's scope. A mid-cycle run folds new filings into **unbuilt
builds only** (no BUILT brief record, no release carrying the build), as a dated **capture
addendum** whose scope delta the owner rules in the same session (headless: that ruling is
the owner's to make — ground the filing and report `blocked`). The **joint test** decides
review: a roundtable **delta** convenes only when the addendum moves a *joint* — a
cross-build dependency, an ordering, an interim posture (`roadmap-roundtable`'s frame); a
scope-internal addition does not re-convene the room. A filing targeting an
already-shipped build routes to the unbuilt build that owns the surface, or holds on an
explicit owner ruling. The addendum's written form lives in
`references/roadmap-synthesis.md`.

Skimming a prior cycle's closed roadmap or filings (`factory/cycles/NN-<slug>/roadmap.md`
and `filings/`) for continuity is useful when a new filing clearly follows on from past
work, but never required — don't block discovery on reading history that isn't relevant to
the filings at hand.

Confirm with the user which filings this run covers before grounding (all un-captured ones,
by default) — a filing may be explicitly deferred if the user knows it needs a vault-side
follow-up first.

## Stages

| # | Stage | Purpose | Location |
|---|-------|---------|----------|
| 1 | Discovery | GitHub intake + find un-captured filings + the open (or new) cycle roadmap | SKILL.md (above) + `references/github-intake.md` |
| 2 | Grounding | Verify each filing's claims against current module source | `references/grounding-methodology.md` |
| 3 | Synthesis | Fold grounded findings into the roadmap doc | `references/roadmap-synthesis.md` |

Route to each in order; each carved file is self-contained (don't assume this SKILL.md is
still in context by the time Synthesis runs).
