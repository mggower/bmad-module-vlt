# The package-lint test fixture is stale against C6/C7/C8 and E — the harness has been red for three builds and nobody noticed

_Filed 2026-08-01 from **build B6-1** (Arc 6), at rest in the factory. Not a field filing: the
evidence is this repo's own working tree. Surfaced because B6-1 added the first positive Group-D
case and it tripped on debt it did not create._

## The claim

`tools/test-package-lint.py` builds a synthetic fixture tree (`build_fixture`, `:37-85`) that
predates three shipped builds' additions to `tools/package-lint.py`. At `f3b343d` (the `v0.9.0`
tag commit) the harness reports **6/8 cases green** — and has, silently, since B5-9 landed.

The two red cases are the only two that assert a *whole-run* verdict rather than a single group:

- **Case 1** (`clean tree -> exit 0, all groups PASS`) — asserts `PASS group A/B/C` + `SKIPPED D`.
- **Case 7** (`--expect-version mismatch -> D fails`) — asserts D fails *and* `PASS group A/B/C`.

Both fail on group C and group E. Every group-scoped negative case (2–6, 8) still passes, which
is why the rot never announced itself: the harness's *purpose* — proving each group can fail —
is still being served. Only its clean-baseline claim is false.

## Grounding

Run `uv run tools/test-package-lint.py` at `f3b343d`. The clean-fixture failures are exactly three:

```
FAIL group C — resolvability + version agreement:
  - rule-card missing: skills/vlt-setup/assets/governance/_meta/vault-rule-card.md
  - enforcement kit: vitals reader missing: skills/vlt-setup/assets/hooks/vlt-vitals.py
FAIL group E — self-description integrity:
  - structure map: cannot read module.yaml vault_structure.default: 'vault_structure'
```

Each traces to a build that widened the lint without widening the fixture:

| Fixture gap | Assertion added by | Lint site |
|---|---|---|
| no `vault-rule-card.md` (+ its `derived_from:` sha256, + the 8,000-byte budget) | **B5-7** (C6, derived-artifact freshness) | `tools/package-lint.py:22-27` |
| no `assets/hooks/vlt-vitals.py`, no tripwires seed, no `tripwires`/`lint_reports` rows in the default map | **B5-9** (C8, enforcement-kit agreement) | `tools/package-lint.py:33-40` |
| `module.yaml` has no `vault_structure.default` to compare against the contract's table | **B5-8 / B5-9 era** (E2, structure-map SSoT) | `tools/package-lint.py:44-46` |

C7 (router integrity, B5-8) passes only vacuously — the fixture has no `references/` directories,
so there is nothing to orphan.

## Why it matters

The shallow cost is a misleading test report: `6/8` reads as "two known failures" when it is
really "the baseline is wrong." The deeper cost is the one this class of defect always has —
**the fixture is the only thing that proves a group can pass.** Group D had no positive case at
all until B6-1 added one; C6, C7 and C8 still have none, and no negative case either. Three
builds shipped release-gate assertions whose only exercise is the real repo tree, which is a
sample of one and is always green by construction (it is the tree the assertion was written
against). A rule that can only be observed passing on the artifact it was authored from is not
yet tested.

There is also a quiet ratchet here: each new group makes the clean fixture harder to satisfy, so
the incentive at every build is to skip the fixture update — exactly what happened three times
running. Whatever fixes this should probably make the clean baseline *load-bearing* (a case that
fails loudly the moment a new group is added without a fixture seed), not just patch the three
current holes.

## What B6-1 did instead (and why this is a filing, not a build)

B6-1's F3 added three Group-D cases (9, 10, 11 — one positive, two negative). Case 9 was written
to assert `PASS group D` rather than exit 0, matching the group-scoped idiom cases 2–8 already
use, so it grades the rule B6-1 shipped and not this inherited debt. The harness is now **9/11**,
with cases 1 and 7 red exactly as they were at HEAD.

Owner-ruled at build time (2026-08-01): repairing the fixture is real work across three other
builds' surfaces and does not belong inside a build briefed as low-moderate risk with no
`vlt-*` skill changes. It files here for capture into Arc 6 or later.

## Candidate shape (not a ruling)

Seed the four gaps in `build_fixture` — rule-card with a correct `derived_from:` sha256 over the
fixture's own contract, a minimal `vlt-vitals.py` carrying a parseable `METRICS` table, a
tripwires seed whose metric ids resolve into it, and a `vault_structure.default` map agreeing
with the fixture contract's table — then restore case 1's exit-0 assertion as the baseline that
makes the next omission fail loudly. Positive and negative cases for C6/C7/C8 become cheap once
the fixture can satisfy them at all.
