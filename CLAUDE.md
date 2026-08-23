# bmad-module-vault — the vlt module source repo

This repo is the **factory**: the development home of `vlt` (the Vault BMad module). It is
not a vault. The **field** is any live vault the module is installed into (a separate
project per vault). Module development happens **here only**; never "fix" a module bug by
editing an installed vault, and never treat vault-local evolution (minted partners,
overlays, capabilities) as module source.

@CLAUDE.local.md

## The evolution lifecycle (the loop this repo runs on)

1. **Field notes arrive** — live vaults file defects/patterns/candidates as dated markdown
   into `factory/inbox/` (see `factory/inbox/README.md` for the filing shape).
2. **Capture** — fold uncaptured filings into the open cycle's roadmap at
   `factory/cycles/<NN-slug>/roadmap.md` (the open cycle is named by `factory/CYCLE`;
   capture opens the next cycle when none is open). **Ground every filing claim against
   current module source before capturing it** — filings regularly mis-attribute
   provenance or guess wrong fixes; grounding corrections belong in the capture. Closed
   cycles' roadmaps stay in their own `factory/cycles/` directories — read them for
   history, **never append to them**. (Cycles 1–10 were called arcs —
   `factory/method/cycles-were-arcs.md`.)
3. **Ideate** — per-build, owner-steered (grouping, order, scope rulings). An external
   unknown gets a **spike before the brief is written** — read the actual external source
   rather than reasoning from its docs or from memory.
4. **Review** — convene the roadmap roundtable (`roadmap-roundtable`) over the filled
   ideation rulings before any brief: the installed roster hunts the plan's *joints*
   (cross-build dependencies, rules ahead of mechanisms, interim postures), agreed
   amendments are applied to the roadmap in-session, disputes are owner-ruled live with
   dissents on record. Skipping is an explicit owner waiver in the roadmap, never a
   silence — `build-brief` gates on the record.
5. **Brief** — each build gets `factory/cycles/<NN-slug>/briefs/build-N-<slug>.md`
   (scope, exact sites with `file:line` grounding, out-of-scope dispositions,
   verification + acceptance checks). Append its live-acceptance checks to the cycle
   roadmap's ledger.
6. **Build** — implement the brief; **unit-verify at rest** (greps for cross-file agreement,
   real script runs against temp fixtures, end-to-end against real external code where
   possible). Record deliberate deviations from the brief in its `status:`.
7. **Release** — work on a branch (`cycleN-vX.Y.Z`), one commit per build; at release bump
   **both** version strings (`.claude-plugin/marketplace.json` `"version"` and
   `skills/vlt-setup/assets/module.yaml` `module_version`). **Before tagging, run
   `uv run tools/package-lint.py --expect-version X.Y.Z` — tag only on exit 0**, and
   record its PASS summary line in the release commit message (skipping the lint is
   then visible in history). Then ff-merge to `main`, tag `vX.Y.Z`, push main + tag.
8. **Live acceptance** — batched to the next `vlt-upgrade` run on a live vault (the owner
   runs it). Defects found there file back into `factory/inbox/` — the loop closes. A
   filing's inbox file moves to its cycle's `filings/` directory once its build has
   shipped **and** its own clauses have passed acceptance — the exact criterion (and its
   bound) lives in `cycle-closeout`'s Stage 5; don't restate it here. Acceptance checks
   are tagged **ship-verifiable** or **field-contingent** at brief time, and **only
   ship-verifiable checks gate cycle closeout** — see `build-brief` §9 and
   `cycle-closeout` Stage 1.

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
- **Precedence by elimination (Arc 9 D5):** where two shipped rules address the same
  population, eliminate the overlap by **narrowing one rule's population**; an explicit
  precedence statement is the **fallback**, used only where the populations genuinely
  cannot be cut apart. Prefer elimination; state precedence only when elimination is
  impossible. (Worked example: the B9-1 dispatch-ledger repair — `vlt-dispatch`'s
  `ledger.md:25`/`:26` overlap ceased to exist by narrowing, no precedence statement
  needed.) A vault-facing restatement, if ever wanted, is a pointer, never a copy.
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

- This is a public repo, **factory included** (P-9, 2026-08-23): the shipped surface
  (`skills/`, `.claude-plugin/`), the factory record (`factory/`, the 9 factory skills
  under `.claude/skills/`), `tools/`, and `.github/` are all tracked and public.
  `tools/` documents the release contract but is not part of the own-the-apply copy
  surface; `.github/` is the repo-side half of the feedback rail's field contract,
  likewise never copied into vaults. Still gitignored and local-only:
  `.claude/skills/bmad-*` (upstream's), `_bmad/`, `_output/`, `.vscode/`,
  `CLAUDE.local.md`, `**/.decision-log.md`. Remotes: `origin` (public) and `private`
  (mirror; kept as an off-machine backup).
- **No personal or vault-local information anywhere tracked** — that now covers the
  factory, not just `skills/`. Machine paths, the owner's username, and the field
  vault's real path stay out (placeholders like `{field-vault}`, `{owner}`, `~` in
  their stead); machine/personal specifics live only in `CLAUDE.local.md`. The one
  deliberate exception: the author email in `.claude-plugin/marketplace.json` (public
  plugin metadata).
- **Worked examples in shipped skills use placeholder paths**
  (`_agent/specs/{date}-{owner}-to-{consumer}-{slug}.md` style), never a specific install's
  artifact paths — a vault-side file move otherwise strands the module's own documentation
  (091001 LB2; build-15 fixed the `vlt-dispatch:193` instance, build-18 states the rule).
  Generic *domain* illustrations (e.g. the dog-training / health-coaching loop-profile
  examples in `vlt-track`) are fine — the rule targets live artifact **paths**, not example
  vocabulary.

## What not to touch

- `.claude/skills/bmad-*` — installed BMad tooling (the module-builder, agents, etc.). It's
  upstream's; defects in it get filed upstream to BMAD-METHOD, not patched here.
- Installed vaults — read them for grounding/diagnosis freely; write fixes only as module
  source here, delivered via `vlt-upgrade`.
