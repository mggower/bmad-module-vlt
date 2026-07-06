# bmad-module-vault — the vlt module source repo

This repo is the **factory**: the development home of `vlt` (the Vault BMad module). It is
not a vault. The **field** is any live vault the module is installed into (a separate
project per vault). Module development happens **here only**; never "fix" a module bug by
editing an installed vault, and never treat vault-local evolution (minted partners,
overlays, capabilities) as module source.

@CLAUDE.local.md

## The evolution lifecycle (the loop this repo runs on)

1. **Field notes arrive** — live vaults file defects/patterns/candidates as dated markdown
   into `inbox/` (see `inbox/README.md` for the filing shape).
2. **Capture** — fold uncaptured filings into the current arc roadmap in `skills/reports/`
   (`inbox-evolution-arc*-roadmap.md`). **Ground every filing claim against current module
   source before capturing it** — filings regularly mis-attribute provenance or guess wrong
   fixes; grounding corrections belong in the capture. Closed arc roadmaps live in
   `skills/reports/archive/` — read them for history, **never append to them**.
3. **Ideate** — per-build, owner-steered (grouping, order, scope rulings). An external
   unknown gets a **spike before the brief is written** — read the actual external source
   rather than reasoning from its docs or from memory.
4. **Brief** — each build gets `skills/reports/build-N-<slug>.md` (scope, exact sites with
   `file:line` grounding, out-of-scope dispositions, verification + acceptance checks).
   Append its live-acceptance checks to the arc roadmap's ledger.
5. **Build** — implement the brief; **unit-verify at rest** (greps for cross-file agreement,
   real script runs against temp fixtures, end-to-end against real external code where
   possible). Record deliberate deviations from the brief in its `status:`.
6. **Release** — work on a branch (`arcN-vX.Y.Z`), one commit per build; at release bump
   **both** version strings (`.claude-plugin/marketplace.json` `"version"` and
   `skills/vlt-setup/assets/module.yaml` `module_version`). **Before tagging, run
   `uv run tools/package-lint.py --expect-version X.Y.Z` — tag only on exit 0**, and
   record its PASS summary line in the release commit message (skipping the lint is
   then visible in history). Then ff-merge to `main`, tag `vX.Y.Z`, push main + tag.
7. **Live acceptance** — batched to the next `vlt-upgrade` run on a live vault (the owner
   runs it). Defects found there file back into `inbox/` — the loop closes. A filing's
   inbox file moves to `inbox/archive/` once its build has shipped **and** passed
   acceptance.

## Standing rules (violations here have bitten before)

- **Governance SSoT:** the governance bundle lives ONLY at
  `skills/vlt-setup/assets/governance/_meta/`. Never create or edit a second copy — a
  top-level staging tree once diverged silently and was retired.
- **Version-handshake (build-4):** conventions in the governance bundle carry
  `version:`/`consumers:`; consumer skills carry flat `depends_on: ["name@version"]`. A
  convention **rule change** bumps `version:` and re-acks every consumer in the same build;
  verify bipartite-consistent (every consumer listed ↔ every ack current). Prose
  clarifications don't bump. The **operating contract is deliberately NOT handshaked** —
  it uses single-home + pointers instead.
- **Single-home discipline:** mechanics live in exactly one place; every other site carries
  a short pointer, never restated mechanics. Related: **lists that claim completeness
  drift** (they fall behind additions); subset-with-defaults listings don't — prefer
  point-at-the-map over full enumerations.
- **`module-help.csv`:** canonical BMad header (13 cols, `preceded-by,followed-by` — NOT
  `after,before`); **always quote** free-text fields (description/args/outputs/display-name),
  not just when a comma is present. `merge-help-csv.py` migrates the known-old header
  in place and skips/reports malformed rows — don't regress either.
- **Workflows (`.claude/workflows/*.js` assets):** the runtime delivers `args` as a JSON
  **string** in every invocation form — parse-on-intake at the top of every workflow.
- **No per-skill `.decision-log.md` in the working tree.** They're gitignored build
  artifacts, but `vlt-upgrade`'s own-the-apply is a *filesystem* copy — cruft on disk ships
  into vaults. Delete them when a build finishes.
- **Durability posture:** anything a vault grows locally (minted `vlt-agent-*`, convention
  overlays in `_agent/conventions/`, capabilities, mint history) must survive upgrades —
  merge-not-replace, never destroy. When touching `vlt-setup`/`vlt-upgrade`/merge scripts,
  re-check the B1 local-mint preserve path.

## Git & publishing

- This is a public repo. Dev artifacts are gitignored and stay local: `inbox/`,
  `skills/reports/`, `docs/`, `.claude/`, `_bmad/`, `CLAUDE.local.md`. A release commit
  therefore contains only the shipped surface (`skills/`, `.claude-plugin/`, `tools/`,
  README, LICENSE — `tools/` is tracked and public as documentation of the release
  contract, but is not part of the own-the-apply copy surface). Shipped content (examples, templates, docs) must carry **no personal or
  vault-local information** — scrub before it lands in `skills/`.

## What not to touch

- `.claude/skills/bmad-*` — installed BMad tooling (the module-builder, agents, etc.). It's
  upstream's; defects in it get filed upstream to BMAD-METHOD, not patched here.
- Installed vaults — read them for grounding/diagnosis freely; write fixes only as module
  source here, delivered via `vlt-upgrade`.
