---
title: 'Build #B7-1 — the harness baseline (the release gate learns to prove its own checks can fail)'
status: 'BUILT 2026-08-15 — all F-sites landed (F1 fixture seeded from FIXTURE_STRUCTURE;
  F2 cases 1/7/9 load-bearing baselines; F3 six negatives + E4 self case = 18; F4 covers=
  required + COVERAGE map + CASE_FLOOR=18; F5 _e4_harness_coverage wired into check_group_e;
  F6 brief-anatomy R2 bullet). Deviations: (1) test-package-lint.py PEP 723 dependencies
  gained "pyyaml" — case 18 imports package-lint.py in-process, which imports yaml at module
  top; the brief was silent on the harness env. Builder picks recorded per brief: baselines
  1/9 carry covers=() (not every-check tags); case 16 re-derives the fixture card digest
  after its contract edit so the failure isolates to E2 (comment in the case). Verification:
  harness 18/18 green; real-repo lint exit 0 both bare (A/B/C/E PASS, D SKIPPED) and
  --expect-version 0.9.1 (all five groups PASS). Mutation probes: (a) uncovered
  `def check_probe` inserted into package-lint.py → FAIL group E "harness coverage:
  check_probe has no fixture case…", exit 1; restored → exit 0. Probe note: the function
  must be defined before the __main__ guard to be visible in that same run (real checks
  always are); (b) removing case 17''s registration → loud "17 registered cases <
  CASE_FLOOR 18" FAIL; restored; (c) seed-one-defect discipline: each of cases 12–18
  observed red by neutering its covered check (return [] mutation) — RED-OK for all seven —
  then restored to 18/18. No .decision-log.md on disk; one commit.'
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-01-143000-lint-fixture-stale-against-three-builds.md (A7-1 — fixture stale
    against B5-7/B5-9/B5-8-era additions; cases 1 and 7 red since B5-9; C6/C7/C8 and E have no
    fixture case at all)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-15): grouping row B7-1 (seed the four fixture gaps,
  restore case 1 exit-0 as the load-bearing baseline; first application of the structural
  doctrine — fixture built FROM the structure contract, not hand-listed); §Cross-filing
  decide-once ruling 5 (enumeration-vs-structure DOCTRINE: a durability net defines its
  protected surface structurally; a net that must carry a list carries a shrink check);
  §Post-ideation amendments R2 (any build adding/changing a release-gate check extends the
  fixture in the same build — mechanical: case-count shrink check + gate-check-with-no-fixture-
  case is itself a lint failure; home tools/package-lint.py + build-brief §7; WIRED BY THIS
  BUILD). Interim-posture ruling under A7-5: no date rider on B7-1 (let the finding stand).'
risk: 'low — factory-side tooling only (tools/*.py + one dev-skill reference edit); nothing on
  the shipped vault surface changes, no convention version moves, no consumer walk. The one
  operational effect is deliberate: the release gate acquires a new way to fail (E4 harness
  coverage), which is the build''s purpose.'
---

# Build #B7-1 — the harness baseline

`tools/test-package-lint.py`'s fixture predates three shipped builds' additions to
`tools/package-lint.py`. Confirmed at HEAD this session by running the harness: **9/11 green**,
cases 1 and 7 red on exactly three clean-fixture failures — C6 rule-card missing, C8 vitals
reader missing, E2 `'vault_structure'` KeyError — and groups C6/C7/C8/E1/E2/E3 have **no
positive and no negative case** (C7 passes vacuously: the fixture builds no `references/`).
Three release-gate assertions are exercised only against the real repo tree, which is the tree
they were authored from. The filing's ruling, enshrined by the roadmap ahead of the four seeds:
**a rule that can only be observed passing on the artifact it was authored from is not yet
tested.**

This build (1) seeds the fixture's four gaps and restores the whole-run exit-0 baseline, built
*from* a single structure source per the structural doctrine, and (2) **wires standing rule R2**
so the rot cannot recur: the harness carries a case-count shrink check, and a gate check with no
fixture case becomes a `package-lint` failure in its own right. It opens the arc and gates B7-2
(whose C7/E-class work cannot be proven against today's fixture) and B7-6 (whose handshake-node
check will be the first check R2 catches).

All rejected alternatives in the parent filing are settled — do not re-litigate. In particular:
patching only the three current holes without a load-bearing baseline (the filing's "quiet
ratchet" paragraph rejects it), and deferring the fixture repair again (owner-ruled at B6-1 that
it files rather than rides; Arc 7 ruled it ships first).

## Brief-time dispositions

The roadmap ruled *that* R2 is mechanical and *where* it lives; the mechanical form is this
brief's to fix (headless run — each call is recorded here as its disposition).

1. **E4 is a Group E sub-check ("harness coverage"), and its inventory is derived by
   introspection, never by list.** The no-fixture-case failure lives in `package-lint.py` as
   `_e4_harness_coverage`, aggregated by `check_group_e` (`package-lint.py:564-596`) beside
   E1/E2/E3 — Group E is "self-description integrity" and this is precisely the gate describing
   itself. The gate-check inventory is the set of module-level callables in `package-lint.py`
   whose names match `^check_` or `^_e\d+_` — a structural read of the module's own shape, so a
   new check function enters the inventory the moment it is defined, with no registry to forget.
   Grounding for the pattern's fit today: it yields exactly `check_group_a/b/c/d/e`,
   `check_rule_card` (C6), `check_router_integrity` (C7), `check_enforcement_kit` (C8), and
   `_e1_handshake`/`_e2_structure_map`/`_e3_stray_pin` — the full check surface, no helpers
   (`is_cruft`, `load_canonical_header`, `field_quote_flags`, `_read_frontmatter` don't match).
2. **Coverage is declared per-case, by the case, and imported — never re-stated.** The
   harness's `case()` decorator (`test-package-lint.py:105-109`) gains a **required**
   `covers=(...)` argument naming the inventory callables the case can make fail; the
   registrations aggregate into a module-level mapping. `package-lint.py` imports the harness
   by path exactly the way it already imports `merge-help-csv.py`'s `HEADER`
   (`load_canonical_header`, `package-lint.py:103-109` — the established
   single-source-never-a-copy idiom; `main()` is `__main__`-guarded so import is side-effect
   free, and both files already set `sys.dont_write_bytecode`). E4 fails when any inventoried
   check has no covering case. This is the doctrine's sanctioned second form: a declaration the
   protected thing carries about itself.
3. **E4 binds the gate's own repo, invariant of `--root`.** The lint's `--root` points at the
   tree being linted (fixture trees have no `tools/`); the harness whose coverage E4 asserts is
   the gate's own, resolved from `Path(__file__)` the way `REPO` already is in the harness
   (`test-package-lint.py:28-29`). Consequence, deliberate: every fixture-case subprocess run
   also exercises E4 against the real repo — a coverage regression turns the baseline cases red
   loudly, which is the load-bearing behavior the filing asked for.
4. **E4 covers itself via one in-process case, not by self-exclusion.** An uncovered E4 would
   be the filing's defect reborn ("observed passing only on the artifact it was authored
   from"). A subprocess negative is disproportionate (it would need a mutated copy of the
   harness); instead one harness case imports `_e4_harness_coverage` and calls it against a
   fabricated inventory/coverage pair with a known hole, asserting the failure string. Cheap,
   deterministic, and it can fail.
5. **The shrink check is a floor constant in the harness, checked in `main()`.** The doctrine:
   *a net that must carry a list carries a shrink check* — `CASES` is the one list this build
   cannot avoid carrying, so `test-package-lint.py` carries `CASE_FLOOR` (set to the final case
   count this build lands, expected **18**) and `main()` (`:209-223`) fails loudly when
   `len(CASES) < CASE_FLOOR`, printing count vs floor. A build adding cases bumps the floor in
   the same edit (ratchet; a stale-low floor still catches any shrink below it). Per-check
   shrink is already covered by E4 — deleting the only case covering a check is a lint failure.
6. **Coverage granularity is the check callable, not the sub-assertion.** One case per
   inventoried callable satisfies R2. Exhaustive sub-assertion negatives (rule-card budget,
   router byte budgets, wire missing-field, orphan *and* dangling variants…) are out of scope
   — see §Out of scope. They become cheap now that the fixture can satisfy the groups at all,
   which is the filing's own closing observation.
7. **Cases 7 and 9 join case 1 as whole-run baselines.** The roadmap names only case 1's
   exit-0 restoration; grounding shows case 7 (`:163-168`) asserts `PASS group A/B/C` and must
   gain E, and case 9 (`:181-187`) carries B6-1's recorded workaround comment ("the fixture is
   stale against C6/C7/C8 and E … a whole-run exit-0 assertion would grade unrelated debt") —
   this build removes the debt the comment cites, so case 9 asserts exit 0 with `PASS group D`,
   becoming the D-active twin of case 1's D-skipped baseline, and the comment is replaced by
   one naming this build. Grounding addition, in scope: leaving either as-is would ship a
   baseline that tolerates exactly the class of silent red this build exists to end.
8. **The fixture grows E1/E3/C7 seeds beyond the filing's four.** The filing's candidate shape
   predates R2. Under R2, `check_router_integrity`, `_e1_handshake` and `_e3_stray_pin` each
   need a case that can fail, and the current fixture gives them nothing to fail *on* (no
   `references/`, no conventions, no `depends_on:`). Grounding addition, in scope: F1 seeds a
   minimal routed reference, one convention with a consumer, and that consumer's ack.

## F1 — `tools/test-package-lint.py` `build_fixture`: seed the gaps from one structure source

**Current state** (`test-package-lint.py:37-85`): the fixture writes a one-line contract stub
(`"# contract\n"`, `:58-60`), a three-key `module.yaml` with **no** `vault_structure`
(`:61-63`), a bare `# vlt-mint` SKILL.md (`:64`), no rule-card, no `hooks/vlt-vitals.py`, no
`tripwires.yaml`, no `references/`, no conventions.

**The change** — extend `build_fixture` so a clean fixture passes every group. Per the
structural doctrine (first application, per the grouping row: *built from the structure
contract, not hand-listed*), the structure map is written **once** as a Python dict and both of
its homes are rendered from it:

- **One source**: a `FIXTURE_STRUCTURE` dict (module scope) carrying a minimal map that MUST
  include `tripwires` and `lint_reports` rows — C8(d) hard-requires both
  (`package-lint.py:393-399`) — e.g. `{"wiki": "_agent/wiki/", "log": "_agent/log.md",
  "tripwires": "_agent/tripwires.yaml", "lint_reports": "_agent/lint-reports/"}`. Rendered
  twice, never transcribed by hand:
  - into `module.yaml` as `vault_structure:\n  default:\n    <key>: <path>` (the real shape,
    `skills/vlt-setup/assets/module.yaml:39-61`);
  - into the fixture contract as the pipe table under the **exact** heading
    `## Path resolution — the structure map` — E2 anchors on `line.strip() == heading`
    (`package-lint.py:497-515`) and reads rows whose first cell is backticked, second cell
    backticked path: `| `wiki` | `_agent/wiki/` | fixture zone |`. Terminate the section (end
    of file or a following `## ` heading).
- **Rule-card** (C6, `check_rule_card` `package-lint.py:288-322`):
  `assets/governance/_meta/vault-rule-card.md` with YAML frontmatter whose `derived_from:`
  carries `sha256:<64-hex>` **computed at fixture-build time** over the final bytes of the
  fixture contract (`hashlib.sha256(contract_path.read_bytes()).hexdigest()` — never a
  hard-coded digest; the real card's form is
  `derived_from: 'vault-operating-contract.md sha256:… (derived …)'`, `vault-rule-card.md:11`).
  Ordering constraint the builder must respect: the contract (with its rendered table) is
  written **before** the card's digest is computed. Body tiny — well under the 8,000-byte
  budget (`:234`, `:303`).
- **Vitals reader** (C8 a–c, `check_enforcement_kit` `package-lint.py:325-401`):
  `assets/hooks/vlt-vitals.py`, minimal but real: compiles, defines a non-empty `METRICS` dict
  (one entry suffices, e.g. `{"ingests_since_lint": "fixture metric"}`) and
  `WIRE_REQUIRED_FIELDS` as the real seven-field list
  (`["id", "metric", "threshold", "owner", "moment", "surface_text", "review_after"]` — the
  real asset's `:222`). The lint imports it from the fixture root (`:356-360`), so nothing
  else from the 500-line real asset is needed.
- **Tripwires seed** (C8 a–b): `assets/tripwires.yaml` with a `wires:` list of one wire
  carrying all seven required fields, whose `metric` names the fixture METRICS id (real wire
  shape at `skills/vlt-setup/assets/tripwires.yaml:43-49`).
- **Routed reference** (C7, `check_router_integrity` `package-lint.py:242-285`):
  `skills/vlt-mint/references/how.md`, and vlt-mint's SKILL.md body names
  `references/how.md` — no orphan, no dangling route. (Router budgets key on
  `vlt-dispatch`/`vlt-lint` names, `:235-238` — the fixture has neither; deliberately
  untouched.)
- **One convention + ack** (E1/E3, `package-lint.py:448-469`, `:529-561`, `:571-590`):
  `assets/governance/_meta/conventions/testconv.md` with frontmatter `version: 1` /
  `consumers: [vlt-mint]`, and vlt-mint's SKILL.md gains YAML frontmatter
  `depends_on: ["testconv@1"]`. Bipartite-consistent clean; gives E1 something to break and E3
  a convention name to anchor its pattern on.

**Why**: the four filing-named seeds close cases 1/7's red; the structure-source rendering is
the doctrine's first application; the E1/E3/C7 seeds are disposition 8. **Out-of-scope note,
per-site**: the fixture models `vault_structure` and `references/` *for the harness* — the
nets whose scope holes A7-2/A7-3 file against those same surfaces are B7-2's, untouched here
(the capture's "three filings, one under-modelled fixture" coupling is discharged on the
fixture side only).

## F2 — the whole-run baselines: cases 1, 7, 9

**Current state**: case 1 (`test-package-lint.py:112-118`) asserts exit 0 but only
`PASS group A/B/C` + `SKIPPED group D`; case 7 (`:163-168`) asserts `FAIL group D` +
`PASS group A/B/C`; case 9 (`:181-187`) asserts only `PASS group D` with the B6-1 stale-debt
comment (`:183-185`).

**The change** (dispositions 7): case 1 asserts exit 0 **and** `PASS group {A,B,C,E}` **and**
`SKIPPED group D` — the load-bearing D-skipped baseline. Case 7 adds `PASS group E` to its
loop. Case 9 asserts `r.returncode == 0` and `PASS group D` (the D-active baseline); its
comment is rewritten to say the baseline is load-bearing per this build (cite A7-1/B7-1), so
the next reader knows exit-0 is deliberate, not incidental.

**Why**: the filing's closing ask — make the clean baseline *load-bearing*, "a case that fails
loudly the moment a new group is added without a fixture seed". With E4 (F4/F5) these two
baselines and the coverage check are belt and braces.

## F3 — six new negative cases, one per uncovered check

**Current state**: no case can make C6, C7, C8, E1, E2 or E3 fail (fixture cannot even reach
their failure paths).

**The change** — add six cases in the existing seed-one-defect idiom (`edit()` helper `:96-99`),
each tagged with its `covers=`:

- **C6** (`covers=("check_rule_card",)`): corrupt the fixture contract *after* fixture build
  (append a byte) → `FAIL group C` with `rule-card stale` (`package-lint.py:317-321`).
- **C7** (`covers=("check_router_integrity",)`): edit vlt-mint's SKILL.md to name
  `references/missing.md` → `FAIL group C`, `dangling route` (`:268-275`). (Orphan variant out
  of scope, disposition 6.)
- **C8** (`covers=("check_enforcement_kit",)`): edit the seed wire's `metric:` to an unknown id
  → `FAIL group C`, `not in vlt-vitals.py's canonical table` (`:383-387`).
- **E1** (`covers=("_e1_handshake", "check_group_e")`): remove/alter vlt-mint's
  `depends_on:` ack → `FAIL group E`, `unacknowledged` (`:463-466`).
- **E2** (`covers=("_e2_structure_map",)`): edit one path cell in the fixture contract's table
  (not the YAML) → `FAIL group E`, `structure map:` path mismatch (`:517-526`). Note this case
  must re-derive nothing — but the C6 sha256 now mismatches too; assert on the E failure string
  and non-zero exit only (a C co-failure is legitimate), or re-write the card digest after the
  edit; builder's pick, recorded in the case comment.
- **E3** (`covers=("_e3_stray_pin",)`): append a body line reciting `testconv@1` to
  `skills/vlt-mint/references/how.md` → `FAIL group E`, `stray pin` (`:546-561`).

Existing cases gain their `covers=` retroactively: 2 → `check_group_a`; 3/4/5 →
`check_group_b`; 6/8 → `check_group_c`; 7/10/11 → `check_group_d`. Plus the E4 self-coverage
case (disposition 4) → **18 cases total**.

**Why**: R2's no-uncovered-check rule made mandatory what the filing called "cheap once the
fixture can satisfy them at all"; each check in the gate is now observed failing at least once.

## F4 — R2 in the harness: `covers=` declarations + `CASE_FLOOR`

**Current state**: `case()` (`test-package-lint.py:105-109`) takes only `name`; `main()`
(`:209-223`) counts whatever is registered — deleting cases shrinks the denominator silently
(exactly how 8 became 11 became "9/11 is normal").

**The change** (dispositions 2, 5): `case(name, covers=(...))` with `covers` **required**
(empty allowed only for the whole-run baselines 1/9 if the builder prefers — or tag them with
every group check; builder's pick, recorded); registrations aggregate into a module-level
`COVERAGE` dict (`check name -> [case names]`) that E4 imports. `CASE_FLOOR = 18` asserted in
`main()` before the loop, failing loudly with count vs floor.

**Why**: R2's "case-count shrink check", verbatim from the amendment; the covers mapping is
E4's data source and the per-check shrink net.

## F5 — R2 in the gate: `_e4_harness_coverage` in `package-lint.py`

**Current state**: `check_group_e` (`package-lint.py:564-596`) aggregates E1+E2+E3; nothing in
the gate knows the harness exists.

**The change** (dispositions 1–4): add `_e4_harness_coverage(...)`:

- derive the inventory by introspecting `package-lint`'s own module for callables matching
  `^check_` or `^_e\d+_` (excluding nothing by hand — see disposition 1's grounding that the
  pattern is exact today);
- import the harness from the gate's own repo (`Path(__file__).resolve().parent /
  "test-package-lint.py"`, the `load_canonical_header` idiom, `:103-109`), read `COVERAGE`;
- FAIL with one line per inventoried check that no case covers
  (`harness coverage: <name> has no fixture case that can fail it (R2 — extend
  tools/test-package-lint.py in the same build)`), and FAIL if the harness itself is missing
  or unimportable (absence must be loud, never a skip);
- wire it into `check_group_e`'s return alongside E1/E2/E3; extend the Group E docstring
  (`:40-50`) with one E4 line naming R2 and this build.

**Why**: R2's second mechanical half — *a gate check with no fixture case is itself a lint
failure* — homed in `tools/package-lint.py` per the amendment, in the group whose charter is
self-description integrity.

## F6 — R2's prose home: `build-brief` §7

**Current state**: `.claude/skills/build-brief/references/brief-anatomy.md:93-115` (§7,
"Verification") carries the standing per-build rituals — handshake Group E, packaging lint,
scrub. Nothing mentions the fixture.

**The change**: add one standing-ritual bullet after the "Packaging lint" bullet (`:112-114`):
**Fixture extension (R2)** — *any build that adds or changes a release-gate check extends
`tools/test-package-lint.py` in the same build (a covering case + `CASE_FLOOR` bump);
`package-lint` Group E4 fails an uncovered check, so skipping this is visible at the gate, not
optional.* Short — the mechanics live in the two tools; this is the pointer (single-home).

**Why**: the amendment homes R2 in "`tools/package-lint.py` + `build-brief`'s verification
section"; without the brief-side pointer every future brief re-discovers the rule from a lint
failure instead of scoping it in.

## Registration

**None.** No skill, workflow or `module-help.csv` change; no convention `version:` moves, so no
consumer walk / re-ack; non-release build, so no version bump (rides the arc's release build).

## Out of scope (dispositioned)

- **A7-2 (`merge-config.py` strips `vault_structure`) and A7-3 (manifest enumeration)** —
  deferred-to-B7-2 by the grouping ruling. F1 models their surfaces in the *fixture* only; the
  nets themselves are untouched.
- **The three expiring `review_after: 2026-08-17` dates** — owner-ruled interim posture under
  A7-5: *let the finding stand; no date-only patch, no rider on B7-1*. Not touched.
- **B7-6's handshake-node lint check** — will be the first check R2 catches; it ships its own
  fixture case in B7-6, per R2. Not pre-built here.
- **Exhaustive sub-assertion negatives** (rule-card budget, router byte budgets, wire
  missing-field, orphan-reference variant, E1 stale-version variant, D sub-cases beyond
  existing) — rejected-because R2's granularity is the check callable (disposition 6); each is
  now cheap to add when a build touches its assertion.
- **R3** (per-check legal-response field) — declared in the roadmap, built in Arc 8; no Arc-7
  scope.
- **`tools/test-cost-manifest.py` / `cost-manifest.py`** — a sibling harness outside the
  release gate; R2 binds release-gate checks only. Already-covered-by its own harness; not
  swept in.
- **CHANGELOG.md entry** — authored at the release build from this brief's `title:`, per the
  B6-1 convention.

## Verification (unit, at rest — lifecycle step 5)

- `uv run tools/test-package-lint.py` → **18/18 green**, output ending `18/18 cases green`;
  case 1 asserts exit 0 + PASS A/B/C/E + SKIPPED D; case 9 asserts exit 0 + PASS D.
- `uv run tools/package-lint.py` on the real repo → exit 0, `A/B/C/E PASS, D SKIPPED` — proving
  E4 passes against the real harness (the real tree is now also covered by the coverage check).
- **Mutation probes** (each red-then-restored, recorded in the BUILT status):
  1. temporarily add `def check_probe(root): return []` to `package-lint.py` → real-repo run
     FAILs group E naming `check_probe` (E4 catches an uncovered new check);
  2. temporarily comment out one registered case → harness fails the `CASE_FLOOR` assertion;
  3. each of the six new negative cases observed red before its assertion was finalized (the
     seed-one-defect discipline — a case that never failed proves nothing).
- **Handshake** — no convention `version:` moved and no `consumers:`/structure-map change on
  the shipped surface; the check of record is the real-repo `package-lint` **Group E** run
  above (never a hand-written grep).
- **Packaging lint** — the mid-arc A/B/C/E run above; `--expect-version` is the release
  build's, not this one's.
- **Scrub** — all fixture content is synthetic (version `9.9.9`, `testconv`, fixture-arc
  idioms); grep the diff for personal/vault-local strings; nothing here ships into vaults
  (`tools/` is public documentation of the release contract, not own-the-apply surface).
- Delete any `.decision-log.md`; one commit for the build.

Builder exit obligations: rewrite this `status:` to a BUILT record with numbered deviations
(the build-15 form), delete `.decision-log.md`, one commit.

## Acceptance (live — appended to the roadmap ledger)

All checks are **ship-verifiable**; none is field-contingent — this build is entirely
factory-side (harness + gate + one dev-skill reference), and nothing in it ships into or waits
on a vault.

1. **[ship-verifiable] Harness baseline restored and load-bearing.** `uv run
   tools/test-package-lint.py` reports all cases green (expected 18/18) with case 1 asserting
   whole-run exit 0 (PASS A/B/C/E, SKIPPED D) and case 9 exit 0 with D PASS — dischargeable at
   rest; re-confirmed by the arc's release-gate run.
2. **[ship-verifiable] E4 live at the gate.** The real-repo `package-lint` run passes with the
   harness-coverage check active, and the recorded mutation probe (an uncovered `check_`-named
   function turns group E red) shows the check could have failed.
3. **[ship-verifiable] Shrink check live.** The recorded probe shows removing one case (or any
   count below `CASE_FLOOR`) fails the harness loudly.
4. **[ship-verifiable] R2 observed binding in-arc.** The first later Arc-7 build that adds or
   changes a release-gate check (B7-6's handshake-node check is already ruled; B7-2 if its net
   work touches the gate) ships its fixture case in the same build, with E4 red-then-green
   recorded in that build's verification — bounded by the arc's own ruled builds.
5. **[ship-verifiable] The arc's pre-tag gate carries R2.** The release build's
   `uv run tools/package-lint.py --expect-version X.Y.Z` exits 0 **with E4 in the run**, and
   its PASS line lands in the release commit message per standing rule — the gate now proves
   its own checks can fail before any tag is cut.
