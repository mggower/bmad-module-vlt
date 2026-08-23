# The skill-asset manifest spec enumerates `assets/` — so the whale re-cut moved eight governing files out from under the divergence net, and a hand-widened manifest is narrowed back on every `vlt-setup` re-run

_Filed 2026-08-03 from the **work vault** (second consumer install, fresh from public GitHub),
during the `vlt-upgrade` 0.8.0 → 0.9.1 run. Classification: **defect** (durability regression) with a
**maintenance** ask attached. Caught by the operator while hand-widening the manifest during the
upgrade — not by any check in the loop. Arc 6 is closed; this is new signal for the next capture._

## The claim

`vlt-setup` SKILL.md:150 defines the skill-asset manifest scope by **enumeration**:

> …covering every **shipped** `vlt-*` skill dir (those in `module.yaml` …), across `SKILL.md` +
> everything under each skill's `assets/`, plus the installed `.claude/workflows/*.js`.

That enumeration was written (build-18, Arc 3) when shipped skill content lived only in `SKILL.md`
and `assets/`. It no longer describes the shipped surface. Two classes of shipped, governing content
sit outside it:

1. **`references/` — a regression.** Eight files, all created by the Arc 5 back-half commit:
   - `skills/vlt-dispatch/references/{consult,daily,ledger,relay}.md`
   - `skills/vlt-lint/references/{checks,fix-and-file,full-scale,report}.md`
2. **`scripts/` — an original gap.** `skills/vlt-setup/scripts/{cleanup-legacy,merge-config,merge-help-csv}.py`
   — present since v0.3.0, i.e. already on disk when build-18 wrote the manifest spec at 0.6.0, and
   never covered by it.

A local hand-edit to `vlt-lint/references/checks.md` (24.8K of governing lint prose) is today
clobbered on the next upgrade with **nothing surfaced** — precisely the failure
`vlt-upgrade` SKILL.md:37 exists to prevent ("the net that turns a local skill-asset edit into a
surfaced divergence instead of a silent clobber").

## Grounding

Verified against module source at `e930a40` (v0.9.1):

- **The spec, verbatim scope**: `skills/vlt-setup/SKILL.md:150` — enumerates `SKILL.md` +
  `assets/**` + `.claude/workflows/*.js`. Same line declares the ownership posture:
  *"the manifest is **module-owned: overwrite it to the current shipped versions on every
  install/update**"*.
- **The consumer**: `skills/vlt-upgrade/SKILL.md:37` — skill-asset divergence is computed *only* over
  "each file the manifest records". Scope loss in the manifest is therefore silent by construction:
  an unrecorded file has no SHA to differ from, so it produces no divergence and no report line.
- **The directories**: `find skills -type d -name references` → exactly the two dirs above;
  `-name scripts` → `skills/vlt-setup/scripts` (3 `.py`).
- **Provenance of the regression** — `git log --diff-filter=A`:
  - `references/` first appears in `43795fa` ("Arc 5 back half … whale re-cut"), which shipped as
    **v0.9.0** (`f3b343d`). **Correction to the backlog entry as written**: the loss landed at
    **0.9.0**, not 0.9.1 — B5-8 is an Arc 5 build. 0.9.1 (Arc 6, the changelog build) is merely where
    this vault *observed* it, because it upgraded 0.8.0 → 0.9.1 in one hop.
  - `skills/vlt-setup/scripts/*.py` first appears in `8c0955f` (v0.3.0). So the `scripts/` gap is not
    a regression at all — it predates the manifest and was never in scope. Worth stating separately,
    because the two want the same fix but carry different blame.

## The friction, as hit

The 0.8.0 → 0.9.1 upgrade widened the manifest **by hand**, 40 → 55 entries, ruling recorded in the
vault's `_agent/mint/decision-log.md` [2026-08-03].

That widening does not survive. The manifest is declared module-owned and overwritten to the current
shipped versions on every install/update, so **any `vlt-setup` re-run silently narrows it back to
40** — and every future upgrade has to re-widen by hand until the spec itself changes. The hand-fix
is not a fix; it is a recurring tax with a silent-reversion failure mode.

## Why it matters

1. **The loss was a side effect, not a decision.** B5-8 was a token-cost refactor. Content that was
   protected at 0.8.0 (it lived in `SKILL.md`) lost its divergence net at 0.9.0 purely because it
   moved directories. No durability ruling was made, and nothing in the build or its lint gate
   noticed — which means the same thing happens again the next time prose moves.
2. **It is invisible in exactly the way the net was built to defeat.** Both failure modes are silent:
   the unrecorded file yields no divergence line, and the narrowed manifest reports `success`. The
   operator only found this by reasoning about the re-cut, not by any signal the loop emitted.
3. **It is an enumeration that claims completeness** — the module's own standing rule
   ("lists that claim completeness drift"), firing inside the durability machinery. `assets/` was a
   snapshot of where shipped content *happened to live* in Arc 3, frozen into a spec.
4. **It is a documented-and-then-reverted state.** A ruling exists in the vault's decision log for a
   change the module will overwrite. That is a worse resting state than either extreme.

## What I'd want

- **Redefine the manifest scope structurally**: all shipped, non-`SKILL.md` content under each
  shipped `vlt-*` skill dir — `assets/`, `references/`, `scripts/`, and whatever a future build adds —
  rather than an enumerated list of directory names. Phrase it so the net tracks the shipped surface
  as it moves. (`SKILL.md` and `.claude/workflows/*.js` stay named explicitly; they're outside the
  per-skill subtree.)
- Consider whether the manifest should be **computed by a script** rather than by prose instruction.
  The 2026-07-12 handoff already flagged this class ("Prose where a script should be", and a proposed
  `verify-skill-manifest.py`); a directory-walk implementation cannot drift the way a prose
  enumeration just did.
- A **check that the manifest entry count didn't shrink** across an upgrade, so a future scope
  regression surfaces as a report line instead of as an absence.
- On capture, decide explicitly whether `scripts/` inclusion is in the same build or split — it is the
  same one-line spec change, but it is a *new* protection, not a restored one.

## Related

- The `dev/` zone request in the same work-vault backlog (generic-evolution-flows-upstream) — filed
  separately by the owner if wanted; not grounded here.
- `2026-08-02-080528-merge-config-strips-vault-structure.md` — different mechanism, same shape: a
  durability-path step that destroys vault-local state and reports `success`. Both argue for
  widening what the upgrade pre-flight snapshots.
