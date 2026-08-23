# vlt-release — decision log

Canonical memory for this skill's build. Load-bearing decisions and rejected
alternatives live here, not in the conversation.

## Session 2026-07-12 — initial build

**Source:** `skills/reports/handoff-2026-07-12/briefs/brief-vlt-release.md` (BRIEFED
2026-07-12). Built via bmad-workflow-builder in a fresh session per the brief.

- **Classification: Complex Workflow.** SKILL.md routes to one carved reference
  (`references/choreography.md`) holding the 8-stage gated sequence, plus a `scripts/`
  surface. Modeled on `.claude/skills/inbox-capture/` (conventions block, stage table,
  carved reference) per the brief.
- **No `--headless`, no customization.** A release is an owner-present act by definition
  (brief). The skill asks exactly two things — the version, and final push confirmation —
  and otherwise runs. Fixed skill; no `customize.toml`.
- **Not a Decision-Log Workspace skill.** It produces no revisable artifact; it's a
  fragile gated procedure (like inbox-capture, which also has no runtime decision log).
- **Stage 2 handshake = Python script, not an inline grep procedure (owner ruling,
  2026-07-12).** The bipartite check is a pure parse-both-maps-and-diff; the quality
  principles put schema-comparison in a script, and the skill's whole reason to exist is
  that the by-hand version is error-prone. `scripts/handshake-check.py` + tests. This
  exceeds the brief's stated "SKILL.md + one reference" shape — owner chose it over the
  lighter grep-procedure alternative when asked.
- **Reuse, don't re-implement, `tools/package-lint.py`.** Confirmed it does NOT cover the
  handshake (it does cruft/csv/version-agreement/skills[] mapping — groups A–D), so stage
  2 is genuinely new. Stage 4 invokes the existing lint verbatim:
  `uv run tools/package-lint.py --expect-version X.Y.Z`, gate = exit 0.
- **Prescriptive procedure is deliberate here.** Per quality principles, exact steps earn
  their place for fragile/security-critical operations (git tag + push). The choreography
  gives exact commands, not outcomes, because deviation has consequences.
- **Grounded at build time:** two version strings at `marketplace.json:16` /
  `module.yaml:4` (both 0.6.0); 7 conventions ↔ 7 consumers bipartite-consistent at HEAD
  (handshake-check confirms: 21 pins); 0.6.0 release commit exemplar `a117f4f` for the
  message + PASS-line style; open roadmap `inbox-evolution-arc3-roadmap.md` for the
  SHIPPED-stamp target.

**Verification at rest:** `handshake-check.py` exits 0 on HEAD; 8 unit tests pass
(consistent-passes, stale-ack-both-directions, missing-pin, convention-omits-skill,
unknown-convention, malformed-entry, consumer-absent, real-repo-HEAD-consistent). Dry-run
of stages 1–7 against a throwaway branch is a first-live-use step (brief), not run here.
