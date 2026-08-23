---
title: "Factory skill: vlt-release"
status: BRIEFED 2026-07-12 — build via bmad-workflow-builder in a fresh session
kind: factory lifecycle skill (lives in `.claude/skills/`, gitignored, never ships)
created: 2026-07-12
derives_from: handoff-2026-07-12 (00-handoff §1.2; 01-lifecycle-archaeology §1 step 6 + §4.1; 04-open-threads §1)
risk: medium — performs git operations including tag + push (outward-facing; push is owner-confirmed)
---

# vlt-release — the release choreography as one gated sequence

## Why this exists (the bite)

Release is a seven-move ritual held together by prose: branch → dual version bump →
pre-tag lint → PASS line in the release commit → ff-merge → tag → push. Only one move
is mechanized (`tools/package-lint.py`), and nothing forces even that to run — there is
no git hook and no CI; the PASS-line-in-commit convention only makes a skipped lint
visible *after* the tag ships. Every pre-lint tag (0.3.0, 0.4.0, 0.5.0) shipped a
packaging defect that cost a full lifecycle round-trip to catch. Separately, the
version bump itself has been botched before (the 0.3.0 bump had to retro-fix
marketplace `skills[]` omissions). This skill makes the whole sequence one thing that
either completes or stops cleanly — nothing tagged, nothing pushed, on any failure.

## Skill shape

- Home: `{project-root}/.claude/skills/vlt-release/` — SKILL.md +
  `references/choreography.md`. Model on `.claude/skills/inbox-capture/` (conventions
  block, stage table, carved reference). No `--headless` mode: a release is an
  owner-present act by definition; the skill asks exactly two questions (the version,
  and final push confirmation) and otherwise runs.
- Trigger: "Runs the vlt release choreography — pre-flight checks, dual version bump,
  package lint gate, release commit, ff-merge, tag, push. Use when the user says
  'release vlt X.Y.Z' or 'run the release'."

## Inputs and grounding sites (re-ground all line refs at build time)

- CLAUDE.md "Git & publishing" + lifecycle step 6 (the canonical choreography).
- `tools/package-lint.py` — invocation is exactly
  `uv run tools/package-lint.py --expect-version X.Y.Z`, gate is exit 0; its summary
  line is the text that goes in the commit (exemplar in `git show a117f4f` — the
  0.6.0 release commit carries "package-lint: A/B/C PASS, D PASS — vlt 0.6.0 (…, exit 0)").
- The two version strings: `.claude-plugin/marketplace.json` `plugins[0].version` and
  `skills/vlt-setup/assets/module.yaml` `module_version` — always bumped together.
- The governance handshake surfaces: every `skills/vlt-setup/assets/governance/_meta/*.md`
  convention's `version:`/`consumers:` vs every `skills/vlt-*/SKILL.md` `depends_on:`.
- Build briefs for the arc: `skills/reports/build-*.md` frontmatter `status:`.
- The open arc roadmap's frontmatter `status` (gets the SHIPPED stamp at the end).

## Procedure (stages — strictly ordered, each a gate; any failure stops the run with a
## clear report and NOTHING later executes)

1. **Pre-flight**
   - On the arc branch `arcN-vX.Y.Z` (create from main if the owner says this run
     starts the release; never release from a dirty tree).
   - Working tree clean apart from the bump this run will make.
   - Every build brief the arc roadmap lists for this release has `status:` BUILT.
   - One-commit-per-build check: the arc branch's commits map 1:1 onto the roadmap's
     build list (advisory — report mismatches, owner rules).
2. **Handshake bipartite check** (factory-side; today a hand grep ritual repeated in
   nearly every build record — mechanize it here):
   - Forward: every convention's `consumers:` skill pins that convention's current
     `version:` in its `depends_on`.
   - Reverse: every `depends_on` entry names a convention that lists that skill.
   - Any mismatch is a hard stop — a release must never ship a stale ack.
3. **Dual version bump** — edit both strings to X.Y.Z. If they already match X.Y.Z
   (bump landed in a prior attempt), proceed; if they disagree with each other, stop.
4. **Lint gate** — `uv run tools/package-lint.py --expect-version X.Y.Z`; require
   exit 0; capture the PASS summary line verbatim. Exit ≠ 0 → print the failure, revert
   nothing (the bump is fine to leave), stop.
5. **Release commit** — commit the bump with the PASS line in the message. Message
   style per the 0.6.0 exemplar: title `vlt X.Y.Z — Arc N: <arc name> (builds …)`,
   body includes the verbatim lint PASS line. **Use simple `-m` flags only (one per
   paragraph), never heredocs/command substitution, and never any Co-Authored-By /
   signing trailer** (owner's standing git rules).
6. **Ship** — ff-merge the arc branch to `main` (must be a true fast-forward; if not,
   stop and report), tag `vX.Y.Z` at the merge result.
7. **Push** — show the owner exactly what will be pushed (`main` + the tag to
   `github.com/mggower/bmad-module-vlt`) and push only on explicit confirmation. This
   is a public repo: remind that the release commit contains only shipped surface, and
   **never push `full-history`** (hard rule; the skill should refuse if the current
   branch state would include it).
8. **Post-stamp** — update the open roadmap's frontmatter `status` to the SHIPPED form
   (exemplar: `inbox-evolution-arc3-roadmap.md:3`) and remind about the project-memory
   sync. Report where acceptance now stands (points at `acceptance-discharge` for
   after the owner runs the vault upgrade).

## Out of scope (dispositions)

- Registering the lint as the release boundary's `checked_by` in doctrine terms
  (091002 open Q4) — a one-time documentation decision for an ordinary module build,
  not this skill; noted in `04-open-threads.md` §3c so it isn't lost.
- A git pre-tag hook / CI — worth considering someday, but the skill is the chosen
  formalization now (owner rulings favor plain conventions over infrastructure here).
- Scrubbing shipped content of personal data — a build-time obligation; the lint
  doesn't check it and neither does this skill (candidate future lint group).
- Deciding the version number — owner input, always.

## Verification (at rest, before first live use)

- Dry-run against a throwaway branch of the repo at HEAD with a fake version: stages
  1–5 must complete (commit created), stages 6–7 exercised up to (not including) push,
  then the branch deleted. The handshake check must PASS on HEAD (it was verified
  bipartite-consistent 2026-07-12 — `../02-module-map.md` §2.4).
- Negative test: seed one defect (e.g. touch `skills/vlt-setup/.DS_Store`) and confirm
  the run stops at stage 4 with no commit/tag created.
- Negative test: bump one version string only and confirm stage 3 stops.

## Acceptance (live)

- The next real release (0.6.x or 0.7.0) runs end-to-end through this skill; the
  release commit carries the PASS line; the 091002 standing metric holds (zero
  packaging filings into `inbox/` for that release).
- The handshake stage catches nothing on a clean release (silence is the pass) — and
  the first time it ever fires, that's the skill paying for itself.
