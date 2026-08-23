---
title: 'Build #14 — pre-tag packaging lint (the factory boundary gets its bell)'
status: >-
  BUILT 2026-07-06 — 8/8 negative tests green; live-fire confirmed (pre-cleanup run
  failed A on the known cruft AND B on a real shipped defect); post-fix run exits 0.
  Deviations from brief: (1) group B's live fire caught `module-help.csv` violating
  always-quote in `display-name` (all 14 rows) and `outputs` (7 rows) — re-quoted in
  place this build, parsed field content verified byte-identical; (2) lint grew a
  `--root` flag so the test harness can point it at fixtures (default unchanged);
  (3) both tools set `sys.dont_write_bytecode` — the HEADER import would otherwise
  create the very `__pycache__` cruft group A polices. Remaining gate: run with
  `--expect-version 0.6.0` at tag time (deferred-acceptance ledger).
module_code: 'vlt'
created: '2026-07-06'
derives_from:
  - 'inbox/2026-07-06-091002-module-packaging-lint.md (A3-2)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-06): tools/ tracked + public; opens Arc 3 as build-14; ships in 0.6.0'
risk: 'low — entirely factory-side except one one-line vlt-upgrade prose edit (vault-facing, B1-safe: widens an exclusion list, touches nothing vault-grown)'
---

# Build #14 — pre-tag packaging lint

Goal: the release boundary (lifecycle step 6) becomes mechanically `checked` — every tag
from 0.6.0 on is cut only after `tools/package-lint.py` exits 0, retiring the packaging
defect class that shipped in every release 0.3.0→0.5.0. Everything lives in this repo;
the only vault-facing edit is the ride-along exclusion-list fix (F4).

## Brief-time decisions (the filing's open questions, resolved here with rationale)

1. **YAML posture: PEP 723 + pyyaml via `uv run`.** Group C needs a real parse — "resolves"
   via line-scrape is exactly the weak semantics this build exists to retire. Matches the
   repo's uv posture; the merge scripts' `dependencies = []` (`merge-help-csv.py:4`) stays
   untouched — only the lint carries `dependencies = ["pyyaml"]`.
2. **Group-A scope: shipped surface + repo-root top level.** Concretely: all of
   `skills/vlt-*/**` and `.claude-plugin/**`, plus repo root at depth 1. Live evidence
   demands the root (`./.DS_Store` exists today); gitignored dev trees (`inbox/`, `docs/`,
   `.claude/`, `_bmad/`, `skills/reports/`) are out of scope — they ship by no path
   (neither git archive nor own-the-apply, which copies only shipped `vlt-*` skills,
   governance, workflows). Note `skills/reports/` is inside `skills/` — the `vlt-*` glob,
   not a bare `skills/` walk, is load-bearing.
3. **`skills[]` ↔ dirs cross-check: IN, as group C's fifth assertion.** It's assert-only
   over data group C already parses (~5 lines), the list demonstrably churns (vlt-track's
   0.4.0 upstreaming), and grounding pre-verified the current 14↔14 sync
   (`marketplace.json:21-35` ↔ `skills/vlt-*` dirs) so it lands green. The R6 scope freeze
   governs *new groups*, not a fifth assertion in kind.
4. **Doctrine registration (`checked_by` stamp): deferred to build-16 as a rider.** The
   lint ships first; when 091004's enforcement-frontmatter schema lands, build-16
   retroactively declares this lint the factory boundary's `checked_by` — the doctrine's
   first fully-`checked` boundary. Out of scope here.

## F1 — `tools/package-lint.py` (new file, new tracked `tools/` dir)

~100–150 lines, PEP 723 inline metadata (`requires-python = ">=3.9"`,
`dependencies = ["pyyaml"]`), invoked `uv run tools/package-lint.py [--expect-version X.Y.Z]`.
Output: one `PASS`/`FAIL` line per group with specifics on failure, a one-line summary
suitable for pasting into the release commit message, exit non-zero on any failure.
All checks read the **working tree on disk, never the git index** — the own-the-apply
ship surface is a filesystem copy (`CLAUDE.md:59-61`), so a git-scoped check silently
misses the worst class.

- **Group A — on-disk cruft.** Fail if any `.decision-log.md`, `__pycache__/`, `*.pyc`,
  or `.DS_Store` exists within the scope from decision 2. Fires today:
  `skills/vlt-setup/scripts/__pycache__/merge-help-csv.cpython-312.pyc` and `./.DS_Store`
  are both on disk (F4 deletes them; the lint keeps them out).
- **Group B — CSV canon, single-sourced.** Load `HEADER` from
  `skills/vlt-setup/scripts/merge-help-csv.py` (symbol at lines 38-52; hyphenated filename
  → `importlib.util.spec_from_file_location`; **never a duplicated list** — a local copy
  makes the enforcement tool the next drift site). Assert: header row of
  `skills/vlt-setup/assets/module-help.csv` equals `HEADER`; every data row parses to
  exactly 13 fields via the `csv` module; the four free-text fields (`display-name`,
  `description`, `args`, `outputs`) are double-quoted **in the raw line** when non-empty,
  per the always-quote rule (`CLAUDE.md:53-56`) — not only when a comma is present.
- **Group C — resolvability + version agreement.**
  `skills/vlt-setup/assets/module.yaml` parses as YAML; `module_version` present
  (currently `:4`); equals `.claude-plugin/marketplace.json` → `plugins[0].version`
  (currently `:16` — nested, not top-level; assert `len(plugins) == 1` before indexing);
  governance bundle home `skills/vlt-setup/assets/governance/_meta/` exists and is
  non-empty (governance-SSoT rule); **C5:** `marketplace.json` `skills[]` entries map
  one-to-one onto `skills/vlt-*` directories (both directions — a listed-but-missing dir
  breaks install, an unlisted dir silently doesn't ship).
- **Group D — tag intent.** With `--expect-version X.Y.Z`: both version strings equal the
  tag about to be cut. Without the flag, group D reports SKIPPED (not PASS).

## F2 — negative-test harness: `tools/test-package-lint.py`

Tracked beside the lint (same PEP 723 posture) so verification is repeatable, not a
one-off session act. Builds a temp-dir fixture (copy of the shipped surface — or a
minimal synthetic tree with the same shape; builder's choice, minimal preferred for
speed), then asserts **seven** cases:

1. Clean tree → exit 0, all groups PASS.
2. Seeded stray `.decision-log.md` under `skills/vlt-mint/` → group A fails.
3. Seeded `after,before` legacy header → group B fails.
4. Seeded unquoted description containing a comma → group B fails.
5. Seeded malformed row (wrong column count) → group B fails.
6. Seeded version-string mismatch (module.yaml vs marketplace.json) → group C fails.
7. `--expect-version` mismatch against an otherwise-clean tree → group D fails.

Plus one C5 case: remove one `skills[]` entry from the fixture's marketplace.json → C fails.

## F3 — `CLAUDE.md` wiring (two edits; in a no-CI agent-driven repo the procedure text IS
the execution substrate — wiring is enforcement, not documentation)

- **(a)** Lifecycle step 6 (`CLAUDE.md:29-32`): before tagging, run
  `uv run tools/package-lint.py --expect-version X.Y.Z`; tag only on exit 0; record the
  PASS summary line in the release commit message (makes skipping visible in history).
- **(b)** Git & publishing (`CLAUDE.md:67-73`): the release-surface enumeration at
  `CLAUDE.md:71` (`skills/`, `.claude-plugin/`, README, LICENSE) gains `tools/` — per the
  ideation ruling (tracked + public: the enforcement tool is documentation of the release
  contract).

## F4 — ride-alongs

1. **`vlt-upgrade/SKILL.md:45` exclusion-list widening** (the filing's latent bug 1; the
   build's only vault-facing edit). The "Exclude dev cruft from the copy" bullet mandates
   excluding only `.decision-log.md`; widen to the field-practice list:
   `.decision-log.md`, `__pycache__/`, `*.pyc`, `.DS_Store`, `reports/` — one sentence,
   same bullet, keep the rsync-style example current. A fresh session following the SKILL
   as written today would ship the live `.pyc`.
2. **Delete the live cruft** (full inventory, verified on disk 2026-07-06):
   `skills/vlt-setup/scripts/__pycache__/` (and its `.pyc`), `./.DS_Store`,
   `./docs/.DS_Store`, `.claude/skills/inbox-capture/.decision-log.md` (dev-zone, outside
   lint scope, but the CLAUDE.md:59-61 rule says delete when a build finishes — this
   build finishes one).

## Out of scope (dispositioned)

- **Slices 2–3** (release.sh wrapper, pre-push tag hook, CI on tag push, vlt-upgrade
  auto-drafted exclusion filings) — evidence-triggered per the filing's R6 scope freeze;
  escalation trigger: any packaging defect shipping in ≥ 0.6.0.
- **Doctrine `checked_by` registration** — build-16 rider (decision 4 above).
- **Fixing the generator** (bmad-module-builder writes `.decision-log.md` every build;
  upstream templates still carry `after,before`) — off-limits per "What not to touch";
  files upstream to BMAD-METHOD (owner action, already carried in the arc ledger).
- **Shipping the lint in `vlt-setup/scripts/`** — rejected in the filing: factory tool;
  shipping it violates the factory/field split. `tools/` is tracked and public but is
  **not** part of the own-the-apply copy surface (nothing in vlt-upgrade reads it).
- **vlt-upgrade's exclusion pass stays as the second bell** — unchanged beyond F4.1; it
  uniquely covers cruft regenerated between tag time and a later own-the-apply (R2).

## Verification (unit, at rest — lifecycle step 5)

- `uv run tools/test-package-lint.py` → all 8 cases green.
- `uv run tools/package-lint.py` against the real tree **after F4.2's deletions** → exit 0
  (and before them → group A fails, confirming the live-fire path).
- Grep: no duplicated header list anywhere under `tools/` (single-source check); no other
  file references `tools/package-lint.py` except `CLAUDE.md` (single wiring point).
- `CLAUDE.md` edits render: step 6 names the exact invocation; `:71` enumeration includes
  `tools/`.
- F4.1: `vlt-upgrade/SKILL.md:45` bullet names all five exclusion patterns; no other
  vlt-upgrade text change (diff is one bullet).

## Acceptance (live — appended to the Arc 3 roadmap ledger)

- **Factory-side, at 0.6.0 release time:** the tag is cut only after
  `--expect-version 0.6.0` exits 0; the release commit message carries the PASS line.
- **Field-side, on vlt-core's 0.6.0 upgrade** (the standing 091002 metric): the
  upgrade-ledger entry records the exclusion pass finding nothing, CSV canonical + quoted,
  `module.yaml` resolves — and the own-the-apply ran the **widened** exclusion list from
  the SKILL text, not session practice.
- **Standing thereafter:** zero packaging filings into `inbox/` for releases ≥ 0.6.0.
