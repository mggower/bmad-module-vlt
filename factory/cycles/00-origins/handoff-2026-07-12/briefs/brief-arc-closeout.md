---
title: "Factory skill: arc-closeout"
status: BRIEFED 2026-07-12 — build via bmad-workflow-builder in a fresh session
kind: factory lifecycle skill (lives in `.claude/skills/`, gitignored, never ships)
created: 2026-07-12
derives_from: handoff-2026-07-12 (00-handoff §1.2; 01-lifecycle-archaeology §4.3)
risk: low-medium — moves roadmap/brief/filing files to archives and edits inbox/README once; nothing leaves the machine
---

# arc-closeout — retire a fully-accepted arc cleanly

## Why this exists (the bite)

Closing an arc is a six-move manual ritual (discharge check, CLOSED banner, carry
forwards, archive the roadmap + briefs, archive filings, sync memory) and the record
shows it leaks: Arc 1's roadmap "simply never recorded" a shipped fix; `inbox/README.md`
carries a completeness-claiming description of the archive that has drifted (describes
10 filings; the archive holds 15) — the exact "lists that claim completeness drift"
failure CLAUDE.md warns about, in the lifecycle's own front door. Closed-roadmap
hygiene matters because closed roadmaps are read-only history ("do not append") that
later arcs and captures rely on.

## Skill shape

- Home: `{project-root}/.claude/skills/arc-closeout/` — SKILL.md +
  `references/closeout-checklist.md`. Model on `.claude/skills/inbox-capture/`.
- Trigger: "Closes a fully-accepted arc: verifies discharge, stamps the roadmap CLOSED,
  archives roadmap/briefs/filings, records carry-forwards, syncs memory. Use when the
  user says 'close the arc' or 'run arc closeout'."
- Headless contract:
  `{"status": "complete", "arc": N, "archived": {"roadmap": "...", "briefs": N, "filings": N}, "carried_forward": ["..."]}`
  — `status: blocked` + `reason` when the discharge precondition fails or a
  carry-forward needs an owner ruling. Blocked-on-undischargedd-ledger is the skill
  doing its job: an arc must never close over unresolved acceptance.

## Inputs and grounding sites (re-ground all line refs at build time)

- **The open arc roadmap** — ledger section (all items), frontmatter `status`.
- **`acceptance-discharge`'s output** — this skill runs AFTER it; the ledger should
  arrive fully discharged or with explicitly-ruled carry-forwards.
- **Archive precedents**: `skills/reports/archive/inbox-evolution-arc2-roadmap.md` —
  the CLOSED status form, the do-not-append banner, and the carried-item form
  ("carried from 0.4.0 watch item — STILL OPEN at arc close, carries forward past
  Arc 2", `:273`). Match this, don't invent.
- **`inbox/README.md`** — filing shape doc + the drifted archive paragraph (`:22-28`
  region as of 2026-07-12).
- **Project memory**: the arc's topic file + `MEMORY.md` index line (CLAUDE.local.md
  sync obligation; precedent: `vlt-arc2-roadmap.md` memory marked CLOSED/archived with
  do-not-append and residual open items).
- CLAUDE.md lifecycle steps 2 and 7 (archival rules).

## Procedure (stages)

1. **Precondition gate** — every ledger item is either checked-with-evidence or has an
   explicit owner carry-forward ruling recorded; the arc's release is tagged and pushed
   (check `git tag`). Anything else → `blocked` with the list of open items (and a
   pointer to run `acceptance-discharge` first).
2. **Carry-forwards** — collect still-open watch items, standing metrics, deferred
   questions, and evidence debts. Record them in the CLOSED roadmap's status section in
   the Arc 2 form ("STILL OPEN at arc close, carries forward"). These are what the next
   arc's capture re-lists; the closed roadmap is their authoritative hand-off point.
3. **Stamp CLOSED** — rewrite the roadmap frontmatter `status` to the closed form with
   date, shipped version, and the do-not-append banner (Arc 2 precedent). From this
   moment the doc is read-only history.
4. **Archive the reports** — move the roadmap and all its `build-N-*.md` briefs to
   `skills/reports/archive/` (plain `mv` — `skills/reports/` is gitignored, there is
   no git history to preserve). Verify nothing belonging to a LATER arc rides along.
5. **Archive the filings** — move each accepted filing `inbox/` → `inbox/archive/`
   (those `acceptance-discharge` already moved are fine; this stage catches stragglers).
   A filing whose acceptance was carried forward stays live — list it in the report.
6. **Fix the front door (first run only)** — replace `inbox/README.md`'s
   completeness-claiming archive description with a non-enumerating pointer
   ("`archive/` holds filings whose builds have shipped and passed acceptance; the
   closed arc roadmaps in `skills/reports/archive/` are the per-filing record").
   Thereafter the skill never maintains any list there — subset-with-defaults or
   point-at-the-map only (standing single-home rule).
7. **Sync memory** — update the arc's project-memory topic file to
   CLOSED/archived + carried items, and its `MEMORY.md` index line (Arc 2's memory is
   the form). Emit the completion report.

## Out of scope (dispositions)

- Discharging ledger items — `acceptance-discharge` owns evidence verdicts; this skill
  only verifies they happened.
- Opening the next arc — `inbox-capture` creates a fresh roadmap when the next filings
  arrive; carry-forwards flow to it via the closed roadmap's status section.
- Git commits — everything this skill touches is gitignored; there is nothing to commit.
- Deleting anything — archival is always a move, never a delete (mirrors the module's
  own never-destroy posture).

## Verification (at rest, before first live use)

- Fixture dry-run: copy the repo's `skills/reports/` + `inbox/` into the scratchpad,
  point the skill at the copy with Arc 3 artificially fully-discharged, and verify:
  CLOSED stamp matches the Arc 2 form; roadmap + 4 briefs land in `archive/`; the six
  091001–091006 filings land in `inbox/archive/`; carry-forwards captured (loop-profile
  watch, BMB upstream filing, 091002 standing metric, design-stage evidence debts);
  README paragraph replaced; no file deleted anywhere (count before == count after).
- Negative test: run against the copy with one ledger item unchecked and no ruling →
  `blocked`, zero files moved.

## Acceptance (live)

- Arc 3's real closeout runs through this skill (after `acceptance-discharge` clears
  the ledger): archive complete, memory synced, README fixed, and the next capture run
  (`inbox-capture` on the two 2026-07-11 graduation-queue filings) finds a clean
  open-arc slate and picks up the carry-forwards from the closed roadmap.
