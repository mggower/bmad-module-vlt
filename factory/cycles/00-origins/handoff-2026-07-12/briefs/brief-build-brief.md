---
title: "Factory skill: build-brief"
status: BRIEFED 2026-07-12 — build via bmad-workflow-builder in a fresh session
kind: factory lifecycle skill (lives in `.claude/skills/`, gitignored, never ships)
created: 2026-07-12
derives_from: handoff-2026-07-12 (00-handoff §1.2; 01-lifecycle-archaeology §1 step 4 + §4.2)
risk: low — writes one new brief file + appends to the open roadmap's ledger
---

# build-brief — scaffold a build brief from a captured roadmap entry

## Why this exists (the bite)

The brief is the most conventionalized *unformalized* artifact in the lifecycle: all 16
briefs to date share a shape (frontmatter, F-site grounding, dispositions, acceptance
checks) sustained purely by imitation of prior briefs. Two failure modes have shown up:
(1) sites drift between capture time and brief time — build-18's brief had to be
re-grounded against post-build-16 source and issued a grounding correction superseding
a roadmap note; (2) the step most likely to be forgotten is the one that edits a
*different* file — appending the brief's acceptance checks to the arc roadmap's ledger.
This skill codifies the shape and makes the ledger append an exit gate.

## Skill shape

- Home: `{project-root}/.claude/skills/build-brief/` — SKILL.md +
  `references/brief-anatomy.md` (the shape spec) + `references/grounding-at-brief-time.md`.
  Model on `.claude/skills/inbox-capture/` (conventions block, activation, stage table,
  headless mode with JSON contract).
- Trigger: "Scaffolds a build brief from the open arc roadmap's captured entry and
  ideation rulings. Use when the user says 'write the build brief for build N' or
  'brief build N'."
- Headless contract:
  `{"status": "complete", "brief": "{path}", "ledger_appended": true, "grounding_corrections": N}`
  — `status: blocked` + `reason` when an ideation ruling the brief needs is missing, a
  spike obligation is unclosed, or a grounding pass contradicts the roadmap in a way
  the owner must rule on. Blocked is the CORRECT outcome in those cases — briefing
  ahead of ideation is the lifecycle violation this skill must refuse.

## Inputs and grounding sites (re-ground all line refs at build time)

- **The open arc roadmap**: the build's row in the proposed-grouping table, the
  per-filing captures it derives from, and the **Ideation rulings** section (binding:
  "Briefs cite this section, never re-litigate" — Arc 3 exemplar at
  `inbox-evolution-arc3-roadmap.md:505-573`, including decide-once rulings, spike
  records, and "questions deliberately left to brief time").
- **Current module source** — every site the capture cited gets re-verified fresh.
- **Style precedents** (named, the inbox-capture pattern): the best current exemplars
  are `skills/reports/build-18-durability-cluster.md` (frontmatter, F-sites,
  dispositions, deviation-recording) and `build-15-spec-convention.md` (brief-time
  dispositions resolving a filing's open questions against the rulings). After Arc 3
  closes these move to `skills/reports/archive/` — the skill should look in both places.
- CLAUDE.md lifecycle step 4 (the one-paragraph canonical statement).

## The brief anatomy (what `references/brief-anatomy.md` specifies)

1. **Frontmatter**: `title`, `status` (starts `BRIEFED <date>`; the builder later
   rewrites it to a BUILT record **with numbered deliberate deviations** — the shape at
   `build-15-spec-convention.md:3` is the precedent to describe), `module_code`,
   `created`, `derives_from` (filings + the specific latent-bug IDs they contribute),
   `roadmap`, `rulings` (pointer to the rulings section), `risk`.
2. **Intent** — a few sentences: what the build changes and why now.
3. **F-sites** — one `## F<n>` section per file/feature touched: current state with
   `file:line`, exact change, and why. Every site freshly grounded (stage 3 below).
4. **Brief-time dispositions** — each open question the roadmap left to brief time gets
   an explicit ruling here, citing the ideation-rulings line it derives from.
5. **Out of scope** — adjacent things deliberately not touched, each with a one-line
   disposition (deferred-to-X / rejected-because / already-covered-by).
6. **Verification (at rest)** — greps for cross-file agreement, script runs against
   temp fixtures, end-to-end against real external code where possible; plus the
   standing per-build rituals (handshake bipartite re-check if any convention moved;
   mid-arc `package-lint` A/B/C).
7. **Acceptance (live)** — the checks that ride the next vault upgrade. These MUST be
   appended to the roadmap's Deferred acceptance ledger in the same run (see exit gate).

## Procedure (stages)

1. **Discover** — resolve the build number to its roadmap grouping-table row; collect
   its filings' captures and every ruling that names it.
2. **Readiness gate** — confirm ideation has run for this build (rulings exist), all
   spike obligations it depends on are closed (spike records in the roadmap), and any
   declared evidence debts are either attached or explicitly ruled not-blocking.
   Anything missing → `blocked`.
3. **Re-ground** — verify every capture-time `file:line` site against current source.
   Where source has moved on (a later build changed it), record a **grounding
   correction** in the brief AND a superseding note in the roadmap's status section
   (precedent: `inbox-evolution-arc3-roadmap.md:649-653`).
4. **Author** — write `skills/reports/build-N-<slug>.md` per the anatomy. Scope rulings
   and anything judgment-shaped: ask the owner (interactive) or record the call inline
   and proceed (headless).
5. **Exit gate: ledger append** — append the brief's acceptance checks to the roadmap's
   Deferred acceptance ledger as a dated per-build bullet (shape:
   `inbox-evolution-arc3-roadmap.md:589-618`). The skill does not report complete
   until this append is verified present (`ledger_appended: true` is earned, not
   assumed).

## Out of scope (dispositions)

- Ideation itself — owner-steered by design; this skill *consumes* rulings and blocks
  when they're missing, it never invents them.
- Building — separate sessions, per brief.
- Capture — `inbox-capture` owns folding filings into the roadmap.
- Enforcing that later builders actually update `status:` to a BUILT record — described
  in the anatomy, checked by `vlt-release` pre-flight (all briefs BUILT), not here.

## Verification (at rest, before first live use)

- Regression-style dry run: point the skill at an ALREADY-BRIEFED build (e.g. build-18
  + the Arc 3 roadmap as of its briefing) in a scratch copy and compare the scaffold's
  structure against the real brief — every anatomy section present, ledger bullet
  produced, rulings cited rather than re-decided. Content will differ; structure must not.
- Negative test: request a brief for a build with no ideation rulings → must return
  `blocked`, not a brief.

## Acceptance (live)

- The next real brief (likely build-17 once its M0 evidence is verified, or the first
  `frontmatter@4` build) is authored through this skill; the builder session that
  consumes it needs no shape questions; its acceptance checks appear in the roadmap
  ledger the same day the brief lands.
