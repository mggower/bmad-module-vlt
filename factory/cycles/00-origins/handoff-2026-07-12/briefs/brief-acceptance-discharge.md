---
title: "Factory skill: acceptance-discharge"
status: BRIEFED 2026-07-12 — build via bmad-workflow-builder in a fresh session
kind: factory lifecycle skill (lives in `.claude/skills/`, gitignored, never ships)
created: 2026-07-12
derives_from: handoff-2026-07-12 (00-handoff §0/§1.2; 01-lifecycle-archaeology §4.5; 04-open-threads §2)
risk: low — reads a live vault (STRICTLY read-only) and edits one roadmap doc + moves inbox files
---

# acceptance-discharge — walk field evidence back onto the arc ledger

## Why this exists (the bite)

The vlt lifecycle's step 7 (live acceptance) has two halves: the owner runs
`vlt-upgrade` on a live vault, and someone maps the resulting evidence back onto the
open arc roadmap's **Deferred acceptance ledger**, ticks items, and archives accepted
filings. The second half is pure discipline and it just failed in production: vlt-core
was upgraded to 0.6.0 on 2026-07-08, but as of 2026-07-12 the Arc 3 ledger was
untouched, all six 091001–091006 filings sat un-archived, and roadmap + project memory
still said "acceptance pending." Nobody noticed for four days. This skill is the bell
for that boundary.

## Skill shape

- Home: `{project-root}/.claude/skills/acceptance-discharge/` — SKILL.md +
  `references/evidence-rubric.md`. Model on `.claude/skills/inbox-capture/` (same
  conventions block, activation config load, stage table routing to carved references,
  `--headless` mode).
- Frontmatter description / trigger: "Discharges an arc roadmap's deferred acceptance
  ledger against live-vault upgrade evidence. Use when the user says 'run acceptance
  discharge'."
- Headless completion contract (mirror inbox-capture's):
  `{"status": "complete", "roadmap": "{path}", "discharged": N, "still_open": N, "failed": N, "filings_archived": ["..."]}`
  — `status: blocked` + one-line `reason` when a verdict needs an owner ruling.

## Inputs and grounding sites (re-ground all line refs at build time)

- **The open arc roadmap**: `skills/reports/inbox-evolution-arc*-roadmap.md` whose
  frontmatter `status` is open — its "Deferred acceptance ledger" section (Arc 3
  exemplar: `inbox-evolution-arc3-roadmap.md:576-622`; unchecked `- [ ]` items).
- **The field vault** (path from `CLAUDE.local.md` — currently
  `{field-vault}`): `_agent/upgrade-ledger.md` (append-only; entry
  format defined at `skills/vlt-upgrade/SKILL.md:103-123`), plus targeted read-only
  inspection of whatever a ledger item names (e.g. `_agent/conventions/.baseline/`,
  `.skill-manifest`, `_meta/conventions/`, `_bmad/module-help.csv`, lint reports in
  session notes).
- **Factory git** for factory-side halves (e.g. "PASS line recorded in the release
  commit" → `git log`).
- **Lifecycle rules**: CLAUDE.md step 7 (filing archives only after its build ships AND
  passes acceptance); `inbox/README.md` for the archive location.

## Procedure (stages)

1. **Discover** — find the open roadmap and its unchecked ledger items; find the most
   recent vault upgrade-ledger entry at or above the arc's release version. If no such
   entry exists, report "upgrade not yet run" and stop (that is a valid, useful answer —
   the skill is also the cheap way to CHECK acceptance state).
2. **Gather evidence per item** — each unchecked item names observable facts (a ledger
   key like `migrations_run:`/`header_migrated:`, a file that must exist, a lint result,
   a behavior at next-use). Read only what the item names. The vault is **read-only
   without exception** — this skill never fixes, cleans, or annotates anything in a
   vault; a defect found here is module signal, not a patch site.
3. **Verdict per item** — exactly one of:
   - **DISCHARGED** — evidence found; tick the checkbox and append a dated evidence
     line in the roadmap (style precedent: Arc 2's build-13 discharge note,
     `archive/inbox-evolution-arc2-roadmap.md:282-286` — evidence + date, one line).
   - **STILL-OPEN** — the item needs first-exercise evidence that hasn't occurred yet
     (e.g. "next mint exercises the consumer lock"). Leave unchecked; annotate with
     what event will discharge it. Never tick on "should be fine."
   - **FAILED** — evidence contradicts the check. Leave unchecked, annotate, and draft
     an inbox filing (shape per `inbox/README.md`) capturing the defect — write the
     draft, show the owner, file on confirmation. This is how the loop closes on a bad
     acceptance.
4. **Archive filings** — a filing moves `inbox/` → `inbox/archive/` only when its
   build's ledger items are all DISCHARGED (STILL-OPEN first-exercise tails with an
   explicit owner ruling may release a filing early — ask, don't assume). Plain `mv`
   (inbox is gitignored).
5. **Report + sync** — summarize verdicts; update the roadmap's frontmatter `status`
   line if the overall arc acceptance state changed (e.g. "acceptance pending" →
   "acceptance discharged except <named first-exercise tails>"); remind/perform the
   project-memory sync (CLAUDE.local.md obligation). Do NOT close the arc — that is
   `arc-closeout`'s job; this skill's output feeds it.

## Out of scope (dispositions)

- Running the upgrade itself — owner-run by standing rule.
- Closing/archiving the roadmap — `arc-closeout`.
- Fixing anything found in the vault — files into `inbox/` instead (stage 3 FAILED).
- Discharging design-stage evidence debts (M0 audits etc.) — those are filing-owned
  attachments; the skill lists them as STILL-OPEN with their named evidence.

## Verification (at rest, before first live run)

- Dry-run against the CURRENT real state: Arc 3 ledger + vlt-core's 0.6.0 entry. The
  expected outcome is known (see `../03-field-inspection-vlt-core.md`): most 0.6.0
  items dischargeable (manifest seeded, conventions seeded from shipped text, exclusion
  pass clean, CSV canonical at 17 rows), with first-exercise tails STILL-OPEN (spec
  consumer lock, first post-upgrade flood-free lint claim needs the lint report read,
  subsumption offer — note vlt-core had NO overlays, so build-18's F2 item discharges
  vacuously and the skill must be comfortable saying "vacuous — no overlay existed").
- Confirm the skill refuses to write into the vault (grep its text: no vault-path Write
  instruction anywhere).

## Acceptance (live)

- First real run discharges the Arc 3 ledger with evidence lines, archives whichever of
  091001–091006 the verdicts release, and flips roadmap `status` — the current
  four-day-stale bookkeeping gap is retired by the skill's own first use.
- Standing: after every future owner-run upgrade, one invocation brings roadmap +
  inbox + memory into agreement with the vault ledger.
