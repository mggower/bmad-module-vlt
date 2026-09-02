---
title: 'Build #3 — the denominated slots: after this ships, a vault owner reading a lint report sees each derived slot with the population it came from — "0 slugs found under `## Stubs…` across 1 index" — and a slot that arrived wrong is reported as wrong rather than as absent, before the scan phase dispatches'
status: >
  BUILT 2026-09-02 — all eight F-sites landed; **checks (1), (2), (3) and (4) — the four at-rest
  `[ship-verifiable]` checks — PASS at rest**, the type harness proven failable against the
  pre-build workflow (`450c886`: 25 expectations FAIL there, 0 here); (5) sits on the v0.18.0
  upgrade sweep. Version bump NOT taken — rides build-7 / v0.18.0. Branch `cycle15-v0.18.0`. No
  handshake moved (`// depends_on:` header and `vlt-lint/SKILL.md:4` pins untouched; `wiki-index.md`
  read, never edited; `PAGE_SCAN`/`pageScanPrompt` untouched — `scanFingerprint`
  `dcce0c50239720081cb5` before and after, E6 PAGE_SCAN still 3676).

  **Sites changed.**
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (F1): `:44-48` the `stubSlugs` contract row
  (pointer to `wiki-index.md` / `checks.md` Missing targets + "a present non-array is refused
  before dispatch"); `:67-76` the `rulesetComponents` contract's three-way sentence (absent /
  empty → cold cap under its own word; wrong type → refused before dispatch); `:118-133` intake —
  `typeName` / `isPlainObject` helpers, `wrongTypeSlots` recorded for a present-and-wrong
  `stubSlugs` (`:128`) / `rulesetComponents` (`:129`), the four not-refused args named in the
  comment (disposition 6), absent still coerces; `:251` comment names the three-way loop;
  `:302-327` the slot loop — `rulesetSlotsAbsent` / `rulesetSlotsEmpty` / `rulesetSlotsWrongType`
  over `RULESET_SLOTS`, slot-level test first (absent / `{}` / non-object → skip the name loop),
  then `convention_digests[<name>]` absent / `''` / non-string; a mis-typed `rulesetComponents`
  itself skips the loop (`:316-317` — nothing derived from its coerced `{}` is rendered as an
  absence); `:333-334` `composeRulesetFingerprint` returns `''` when any of the three lists is
  non-empty or the parent slot is mis-typed; `:406-419` two caps in place of one — `findings
  cache cold: rulesetComponents — absent [...]` / `… — empty [...]`, each only when non-empty;
  `:427-461` the pre-dispatch refusal, placed after the cache reader and the cap blocks and before
  the fan-out loop — mirrors the shortfall return field-for-field (`status: 'failed'`, `reason`
  one clause per offending slot joined `; `, `files_checked: 0`, `files_cached: 0`, empty
  `agent_failed`/`page_unreadable`, `coverage_caps`, `cost_accounting` with all four phase rows
  at 0 dispatched, `cache_miss_terms`, the reader's real `cache_records_read`/`cache_rejected`,
  a directed `next:` naming the slot(s) + step 2 / Missing targets); `:609-610` the reducer
  comment and `:666` `indexPrompt` → the pointer wording; `:224` `INDEX_SCAN.drift` description
  (see deviation 1). `:11` `// depends_on:` unchanged.
  `skills/vlt-lint/references/report.md` (F2): `:15` NEW `stub_discovery:` line after
  `files_listed:` (both modes); `:45` `governance_memory:` → `E log entries (## headings,
  instrument: <name>), S schema-keyed, X unclassifiable, N uncounted` with the N = E − S − X
  comment; `:79` the cold placeholder widened (the fourth member + its home); `:90` the fourth
  member appended to build-2's frame with its home named; `:92` the instrument sentence (E by an
  unwrapped named instrument, `grep -c '^## '` expected; S keyed; X the two-tier tail qualified as
  a **dated entry heading**; N rendered even when 0); `:94` NEW "Stub-discovery reporting"
  paragraph (two facts, compose yourself both modes, `located: no` ⇒ cap in full mode).
  `skills/vlt-lint/references/full-scale.md` (F3): step 1 (`:7`) the stub sentence → derive per
  `checks.md` Missing targets, keep the located/count facts for Step 5, pass an array; step 2
  (`:8`) the three-way sentence with the refusal pointer (digest steps, names, cold-when, D4
  unchanged); step 4 (`:19`) the predicate names both causes, the failed-run field list gains
  `lint_cache: cold (<reason>, rejected R of P records read, evicted E by request)` with the
  fourth-member note, the directed refusal names both next moves.
  `skills/vlt-lint/references/checks.md` (F4): `:13` the procedure homed in the Missing-targets
  bullet (heading from the merged convention, the `## ` match quoted, backtick slugs to the next
  `## `, `section located: yes|no` + count on `stub_discovery:`, the full-mode cap on `located:
  no`); `:39` the long-form heading copy → pointer; `:43` unchanged.
  `skills/vlt-lint/references/fix-and-file.md:9` (F5) and `skills/vlt-lint/SKILL.md:76` (F6):
  the pointer edits as tabled. `skills/vlt-ingest/SKILL.md:168`: see deviation 2.
  `factory/cycles/15-nothing-reads-it-back/fixtures/build-2-key-harness.mjs` (F7): case (g)'s
  cap literal re-keyed to `absent [convention_digests[write-verification]]` (build-2's 15/15 +
  the scanModel guard still hold; `--legacy` unaffected).
  **NEW fixtures** (F8): `build-3-index-stubs.md` / `build-3-index-bare-stubs.md` (the
  discriminator pair — long-form vs bare heading, the three specimen slugs), `build-3-decision-log-
  tail.md` (the twelve unbracketed headings frozen verbatim from `{field-vault}`'s live log
  2026-09-02 + 3 keyed + 1 `kind:`-no-`ref:`; E 16 · S 3 · X 13 · N 0; the twin is in-memory),
  `build-3-type-harness.mjs` (build-2's shim duplicated; counting agent stub; modes: case table /
  `--workflow <path>` / `--stubs` / `--tail`).

  **Verification.** (1) type harness, post-build: (a) `failed`, reason `slot rendered with the
  wrong type: convention_digests (got array, expected plain object)`, 0 agents, scan row 0,
  `next:` names step 2 + Missing targets, `cache_records_read 2 / rejected 0` · (b) `failed`,
  `convention_digests[frontmatter] (got number, expected string)`, 0 agents · (c) report,
  `files_cached 0`, cap `empty [convention_digests]` · (d) report, cap `absent
  [convention_digests[write-verification]]` · (e) report, cap `empty
  [convention_digests[frontmatter]]` · (f) `failed`, `stubSlugs (got string, expected array)`, 0
  agents · (g) `failed`, `rulesetComponents (got array, expected plain object)`, 0 agents, NO
  absent/empty cap · (h) report, 2 cached, no cold cap — **all 25 expectations hold, exit 0**.
  **Failability against `450c886`:** 25 FAIL — (a)/(b)/(g) there return a findings report with
  `files_cached: 0`, 2 agents dispatched (scan row 2) and the one-word cap `rulesetComponents
  incomplete — absent or empty slots [...]`; (f) returns a WARM findings report (2 cached — the
  string silently coerced to `[]`); the four cases flip between the builds as the brief
  predicted. (2) reader protocol (heading read from `wiki-index.md:83`, never from memory):
  `build-3-index-stubs.md` → `section located: yes ("## Stubs (linked, not yet written)"); 3
  slugs` (`birria`, `jesse-minter`, `nfl-draft-safety-archetypes`); `…-bare-stubs.md` → `located:
  no; 0 slugs` (+ the cap); the same protocol over `{field-vault}`'s live index → `located: yes;
  6 slugs` (the A15-11 manifest's 6 — check (5)'s expected value, pre-measured, not a discharge).
  `--stubs`: three slugs → `missing_targets: []`; `[]` → `['a → birria']`; `'birria'` → refused,
  0 agents — exit 0. (3) `grep -c '^## '` over the tail fixture → 16; `--tail` → `{E:16, S:3,
  X:13, N:0}`, mutated twin `{E:17, S:3, X:13, N:1}`; a same-matcher total (S + X = 16) reads
  back nothing on the twin — exit 0. (4) `grep -rn '## Stubs' skills/` → exactly 1 hit,
  `wiki-index.md:83`; `grep -rn 'absent or empty' skills/` → 0; `slot rendered with the wrong
  type` → report.md 2 / full-scale.md 2 / vlt-lint-full.js 1; `stub_discovery` → report.md 2 /
  checks.md 1 / full-scale.md 1; `section located` in checks.md → 1; step 4 names `pre-dispatch
  refusal` → 1. (5) `scanFingerprint` equal before/after; build-2 harness 15/15 + guard after F7.
  (6) `pageHashes: []` → NOT refused: findings report, `files_cached 0` (the on-record gap for
  the candidate filing). (7) `uv run tools/package-lint.py --expect-version 0.17.1` → A/B/C/E
  PASS, D PASS; PAGE_SCAN 3676, INDEX_SCAN 838 (both under 3700). (8) R4 n/a — no shipped file
  added. (9) R3 n/a — no finding class. (10) scrub: the twelve frozen headings name partners by
  domain role only; no path or personal name. (11) no `.decision-log.md`; scratch removed.

  **Deviations/notes:** (1) `INDEX_SCAN.drift`'s description (`:224`) carried the bare `## Stubs`
  form; F1.6 said INDEX_SCAN is not edited while Verification 4 / check (4) require exactly one
  hit — the gating check won: the description now reads "a malformed entry under the Stubs
  section" (E6 measures every fan-out schema; INDEX_SCAN serializes to 838, PAGE_SCAN untouched,
  the index pass is uncached so no key moves). (2) The retirement table missed
  `skills/vlt-ingest/SKILL.md:168` ("out of `## Stubs`") — retired to "out of the Stubs section
  (heading as that convention states it)", the same pointer class as `fix-and-file.md:9`; no pin
  moves (the sentence already points at `wiki-index.md`). (3) Case (g) exposed a gap the brief's
  table implied but did not spell out: a wrong-typed `rulesetComponents` coerces to `{}` at
  intake, and the slot loop over that default would push `absent [convention_digests]` beside the
  refusal — the loop is now skipped when the parent slot is mis-typed, so the failed record
  carries the refusal only. (4) The refusal returns four `cost_accounting` phase rows at 0
  dispatched (Scan pages / Index pass / Cluster pass / Seeded-pair pass) rather than an empty
  `phases: []` — the brief asked that "every phase renders at 0", which an empty list does not.
  (5) The refusal sits after the two cold-cap blocks and the overlay cap (the brief's permitted
  placement) so a refused record still carries any absent/empty/overlay facts that are
  independently true. (6) `X`'s definition in `report.md:92` and the harness qualifies the
  two-tier tail as a **dated entry heading** — without it a `## Notes` section heading would be
  absorbed as pre-schema and `N` could never be non-zero, defeating check (3)'s twin. (7) The
  type harness's case table uses a scan-returning stub (build-2's gen-pass stub) rather than a
  null stub, so cold cases reach a findings report instead of the shortfall guard — the null
  stub would have graded (c)/(d)/(e) against the wrong predicate. Build-5's briefer: `report.md`'s
  mandated-key fence at this commit carries `stub_discovery:` (`:15`, scalar) and the widened
  `governance_memory:` (`:45`, scalar); `lint_cache:`'s grammar is unchanged in shape (`:79`);
  `false_positives_refused:` is not present. Handoff owed: a `candidate` filing for the four
  not-refused args (disposition 6 / §Out of scope).
module_code: 'vlt'
created: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-08-31-104501-stub-discovery-regex-drops-the-stub-list-and-manufactures-missing-targets.md (A15-2 — directions 1 + 2 together (Q8 as amended by A17): discovery matches the heading as `wiki-index.md:83` states it, every other site a pointer, the bare `## Stubs` form retires; the denominated `stub_discovery:` line with `section located: yes|no`)'
  - 'factory/inbox/2026-08-27-160200-governance-memory-denominator-missed-twelve-entries.md (A15-6 — direction 2 (D2 as amended by A14 iv): the `governance_memory:` denominator renders with a population produced by an instrument independent of the matcher — a form-agnostic `## ` heading count against schema-keyed + unclassifiable, the remainder rendered)'
  - 'factory/inbox/2026-09-01-140600-ruleset-fingerprint-inputs-are-under-specified-and-a-wrong-reading-is-silent.md (A15-10 — the second-order direction only (D2 ii/iii as amended by A14): a present-but-wrong-type ruleset slot is a pre-dispatch refusal, never a cold cap; the `pin_vector` half DISSOLVED with build-2 (its brief, disposition 1); the `convention_digests` population half is build-2''s (A4))'
roadmap: 'factory/cycles/15-nothing-reads-it-back/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-01/02): D2 as rewritten by A14 in five moves (the `RULESET_SLOTS`-loop property; wrong type = pre-dispatch refusal with a directed `next:`; the denominator from an independent instrument; the `report.md` homes; merge order 3 → 5); Q8 as amended by A17 (together, one build; single home `wiki-index.md:83`, the rest pointers; the bare form retires); Q3 as extended by D-B (the population is the three scanner-read names — build-2 landed it; this build inherits `RULESET_SLOTS = [''convention_digests'']`); roundtable A4 (build-2 owns population, build-3 rendering/type; lands AFTER build-2), A14 v (the three `report.md` edits), A20 (the cap wording and step 2''s absent-slots sentence → three-way absent / empty / wrong-type); instrument-beat property for build-3.'
risk: 'low-moderate — one workflow asset (`vlt-lint-full.js`) gains a pre-dispatch refusal return and splits one cap into two; four reference docs and the SKILL''s failed-run pointer move; `report.md` gains one key and widens one line (build-5''s validator reads the key set from this commit — §Boundary); NO handshaked convention moves (`wiki-index.md` is read, not edited; SKILL pins and the `// depends_on:` header unchanged; `PAGE_SCAN` and `INDEX_SCAN` untouched — E5/E6/E7 stay green); no consumer walk; every acceptance check is at rest or bounded to the v0.18.0 sweep.'
specimens: '16/17 — observed: A15-2 (3) the three registered stubs reported as missing targets — `birria`, `jesse-minter`, `nfl-draft-safety-archetypes` — plus the field''s long-form heading `## Stubs (linked, not yet written)`; A15-6 (12) the twelve unbracketed `## YYYY-MM-DD —` entries (a count in the filing, the set recoverable from `{field-vault}`''s live log — re-measured at brief time 2026-09-02: 66 `## ` headings, 54 bracketed, 12 unbracketed — the population grew 59 → 66 since the filing while the tail stayed 12); A15-10 (2) `pin_vector` passed as a JSON array, `convention_digests` passed as an 8-name map. Preserved into this brief: A15-2 3/3 — the three slugs are the stub fixture''s registry and the harness''s link targets, the heading form is the fixture pair''s discriminator; A15-6 12/12 — F8 freezes the twelve heading lines from the live log into the decision-log fixture (the capture''s own instruction: "should be frozen from it"); A15-10 1/2 — the wrong-type SHAPE (a JSON array where a map is required) is harness case (a) against `convention_digests`; `pin_vector` itself is not preserved because the slot no longer exists (build-2). NOT preserved: the 8-name map — build-2''s extras-ignored case (c) already carries that shape.'
---

# Build #3 — the denominated slots

## Intent

Three filings, one shape, three renderers: a value the SKILL derives from prose is consumed
without ever being compared to what specified it, and a wrong derivation produces the same
observable as an honest absence. **A15-2:** `stubSlugs` arrived empty because the operator matched
a bare `## Stubs` heading the field's index does not use — the module itself writes the heading two
ways (`full-scale.md:7` bare, `checks.md:39` long) and ships no matcher at all; three registered
stubs became `fix_now` missing targets whose legal response is to create pages that were
deliberately not created. **A15-6:** the `governance_memory` denominator read 47 where the truth
was 59 because the matcher implemented the schema and dropped the pre-schema tail the convention
says to count (`checks.md:43`, `decision-log.md:78`) — and *nothing about the output looked wrong*.
**A15-10:** a ruleset slot rendered as the wrong type read as **missing** at
`vlt-lint-full.js:291`/`:293` (`typeof v !== 'string'` separates the two cases and discards the
distinction), so 146 pages went cold under an honest-looking cold reason; the owner paid 146 agents
to learn nothing. The `pin_vector` half of that filing **dissolved** when build-2 dropped the slot
(`build-2-cache-cost.md` disposition 1); what remains is the wrong-type case itself, now applying to
`convention_digests` and — this brief's grounding addition — to the two intake sites that conflate
the same way one level up (`:111` `stubSlugs`, `:116` `rulesetComponents`).

This build makes the promise's two clauses true, each with its mechanism:

1. **Each derived slot arrives with the population it came from** (D2, A14 iv) —
   `stub_discovery: section located: yes|no; N slugs across 1 index` from a discovery procedure with
   one home and one heading source (`wiki-index.md:83`, overlay-merged); `governance_memory:` renders
   `E log entries (## headings, instrument named), S schema-keyed, X unclassifiable, N uncounted`
   where **E comes from a form-agnostic count, never from the matcher that produced S** — a 47-of-47
   rendered by one matcher reads back nothing.
2. **A slot that arrived wrong is reported as wrong, before the scan phase dispatches** (D2 ii/iii,
   A14) — a present-but-wrong-type `rulesetComponents` slot, required name, or `stubSlugs` value is a
   **pre-dispatch refusal** in the failed-run shape (`status: 'failed'`, a `reason:` naming the slot
   and the type received, a directed `next:`), never a cold-branch cap; **absent** and **empty** stay
   cold caps and are named under their own words. The cap that read *"absent or empty slots"*
   (`:374`) and step 2's *"any slot missing or empty … each absent required name"* become three-way.

And the retirements that come with them (A20, Q8/A17): the bare `## Stubs` form leaves every module
site but the convention's; the two-way cap wording and `report.md:89`'s closed reason list go with
it.

All rejected alternatives in the parent filings are settled — do not re-litigate: no shipped stub
regex to widen (there is none — A15-2's provenance correction; the discovery is a procedure with a
heading source, not a pattern); no re-widening of `convention_digests` to *"one entry per file in
`{conventions}`"* (A4 struck it — the population is build-2's three); no reconciliation of two
heading copies (A17 — a third copy was the trap; one home, the rest pointers); no wrong-type case
rendered as a `coverage_caps` entry (A14 iii — the owner would still pay 146 agents to read it
afterwards); no `ST-7`-wide read-back instrument (D1(a) — the study is citable, not binding; this
build's three slots are D2's whole population and it reaches no further).

**The property this build's acceptance protects** (roadmap §Instrument beat, stated without the
fix): *for every SKILL-rendered input slot, a reader can tell from the report alone whether the
value came from a non-empty population, was legitimately empty, or arrived in a form the workflow
could not use — three distinct renderings — and the population line comes from an instrument other
than the one that produced the value, before any agent dispatches.* Reconciled with the plan's
wording in §Acceptance: "every SKILL-rendered input slot" is read as D2's population (the three
slots this build denominates plus the workflow-side intake of the two that cross the fan-out
boundary) — the remaining args are dispositioned out below, not silently narrowed.

## Brief-time dispositions

Ideation left nothing to brief time for this build by name; the judgment calls below are the ones
this headless run made inside the rulings' letter, each recorded so the builder does not re-decide
them.

### 1. Three-way, at two levels — what is absent, what is empty, what is wrong

For the one ruleset slot (`convention_digests`, build-2's `RULESET_SLOTS`) the three cases are
defined at the **slot** level and again at the **required-name** level:

| Level | Absent (cold cap) | Empty (cold cap) | Wrong type (pre-dispatch refusal) |
|---|---|---|---|
| `rulesetComponents` itself (`:116`) | key not in `args` | `{}` | present and not a plain object (an array, a string, a number, `null`) |
| `rulesetComponents.convention_digests` (`:290`) | key not in the object | `{}` | present and not a plain object |
| `convention_digests[<name>]`, each of `SCANNER_CONVENTIONS` (`:291`) | key not in the map | `''` | present and not a string (a number, an array, an object, `null`) |

`stubSlugs` (`:111`) is two-way at the workflow — it is a list, so "empty" is `[]` and is legal
(a vault with no stubs); **wrong type** is present-and-not-an-array (a string, an object, a number).
Its absent/empty distinction is the SKILL's, rendered as `section located: yes|no` (disposition 3).
The tests are the existing predicates split, not new ones: `!v` / `typeof v !== 'object'` /
`Array.isArray(v)` already run; they stop collapsing to one word.

**Absent and empty are named under their own words** in `coverage_caps`: `findings cache cold:
rulesetComponents — absent [convention_digests[write-verification]]` and `… — empty
[convention_digests[frontmatter]]`, each entry present only when its list is non-empty, the bare
slot name only when the map itself is absent or empty (build-2's missing-by-name rule holds). D4 is
untouched: every cold case still composes `''` and reuses nothing.

### 2. The wrong-type refusal rides the failed-run shape, placed after the cache read and before the fan-out

D2 (iii) names the posture (*the failed-run posture, `SKILL.md` §Step 6*) and the roadmap cites
`SKILL.md`; grounding places the **predicate** at `full-scale.md` step 4 (`:19`) with `SKILL.md:76`
its pointer — the refusal joins step 4's predicate, not the SKILL's paragraph. **Ruling:** the
workflow returns the **same `status: 'failed'` object** the near-total-shortfall guard returns
(`:446-460` — `reason`, `files_listed`, `files_checked: 0`, `files_cached: 0`, empty
`agent_failed`/`page_unreadable`, `coverage_caps`, `cost_accounting` (every phase 0 dispatched),
`cache_miss_terms`, `cache_records_read`, `cache_rejected`, `next`), computed **after** the cache
reader (`:333-361`, so the record counts are real) and **before** `toScan`/the fan-out loop
(`:385`), so no agent has been dispatched and `cost_accounting` says so. `reason:` is `slot rendered
with the wrong type: <slot> (got <typeof-or-array>, expected <plain object | string | array>)` —
one reason per offending slot, joined with `; ` when several. `next:` is directed: *re-render
`rulesetComponents` / `stubSlugs` per `references/full-scale.md` step 2 / `references/checks.md`
Missing targets and re-run — no agent was dispatched, nothing was spent.* The SKILL's step 4 then
does what it already does for a failed return: writes `…-lint-failed.yaml`, applies nothing, writes
no log line (lint-debt not reset), surfaces the directed refusal.

**Why not the `{ error: … }` shape** the args guard uses at `:130`/`:134`: that shape is a caller
contract violation (no pages, a non-string `scanModel`) with no persisted record; a wrong-typed
component slot is the SKILL's own rendering error on a run that was otherwise legal, and the owner
must be left holding a record that names it (A16's *"never no file"* for build-5 is the same
instinct). Build-2's `scanModel` guard stays as it is — out of scope, and a different class.

**Why before the fan-out and not at the args guard:** the refusal wants `cache_records_read` /
`cache_rejected` on the record (they cost nothing and make the failed record comparable to a findings
report), and the reader runs before compose; nothing between the reader and the fan-out loop
dispatches. The harness asserts zero agent invocations for every refusal case (§Acceptance 1).

### 3. Stub discovery — one heading source, one procedure home, two facts rendered

A17 fixes the heading's single home at `{conventions}/wiki-index.md:83` (overlay-merged) and makes
`full-scale.md:7`, `checks.md:39`, `vlt-lint-full.js:44`/`:531` pointers. The *procedure* — what to
do with the heading — also needs one home, and it cannot be `full-scale.md`: scoped and small full
runs never load it (`full-scale.md:3`) yet still judge missing targets against the stub registry
(`checks.md:13`, both modes). **Ruling:** the procedure homes at **`checks.md:13`** (the Missing
targets bullet — the check that consumes the set, so the check names its own population, P-23's
spirit), and `full-scale.md:7` says *"derive `stubSlugs` per `checks.md` Missing targets and pass
them, with the `stub_discovery:` facts kept for Step 5"*. The procedure:

> Read the stub heading **from the merged convention** (`{conventions}/wiki-index.md` §The Stubs
> section + its overlay if present) — never from memory; locate in `{index}` the `## ` heading whose
> text equals it; collect every backtick-wrapped slug in that section's list items up to the next
> `## ` heading; report **`section located: yes|no`** and the count. `located: no` is a loud fact:
> render it, and in full mode add the coverage cap *"stub registry not located under the convention's
> heading — `missing_targets` may name registered stubs"* — the A15-2 observable, stated before it
> is refused by hand.

`section located` distinguishes *not located* from *empty*: D2's exemplar *"0 slugs across 1 index"*
cannot (A14 iv). The bare `## Stubs` form retires from every module site (F1, F3, F4, F5, F6); a
vault index still carrying the bare form renders `located: no` under the new procedure — correct,
because `wiki-index.md:83` is the only heading the module ever specified, and `checks.md:39` has
required the long form for index drift since before this cycle.

### 4. `governance_memory:` — the denominator's total from a count, not the matcher

A14 (iv): *form-agnostic `## ` heading count vs schema-matched entries.* **Ruling on the
rendering:** the line becomes `governance_memory: <G governance findings checked against the log;
A adjudicated, U undisposed; E log entries (## headings, instrument: <name>), S schema-keyed, X
unclassifiable, N uncounted>` where **E** is the count of lines matching `^## ` over
`_agent/mint/decision-log.md` by an **unwrapped instrument named in the line** (`grep -c '^## '` is
the expected one — the operating contract's instrument rule names a property, not a tool); **S** is
the entries the read-before-flag can key (`## [YYYY-MM-DD] <kind> — …` with `kind:` and `ref:`);
**X** is the two-tier tail `checks.md:43` already mandates be counted (`kind:` without `ref:`, or
pre-schema); **N = E − S − X**, rendered even when 0 — a remainder is a `## ` heading that is neither
a keyed entry nor a recognized tail member (a section heading, a form nobody anticipated), surfaced
rather than absorbed. The invariant S + X + N = E is the read-back; a SKILL that derives E from the
same matcher as S cannot fail it, which is exactly why the instrument is named. **Mechanics home:**
`report.md:91` (the SKILL composes the line there; `checks.md:43` keeps its pointer).

### 5. The fourth cold reason's home — reconciling A14 (iii) with A14 (v)

A14 (iii) says a wrong type is *never a cold-branch cap*; A14 (v) says `report.md` gains a fourth
`lint_cache:` cold reason *`slot rendered with the wrong type: <slot>`* at `:78`/`:89`. Read
together against the mechanism: a refused run produces **no findings report**, so a current workflow
copy can never put the fourth reason on a findings report's `lint_cache:` line. **Ruling:** the
fourth reason renders on the **failed-run record's** `lint_cache:` line — step 4's field list gains
`lint_cache: cold (slot rendered with the wrong type: <slot>, rejected R of P records read, evicted E
by request)` (the same grammar as `report.md:78`, the counts from the refusal return) — and
`report.md:78`/`:89` list it as the **fourth member of the reason vocabulary with its home named**:
*it appears on a `…-lint-failed` record, never on a findings report from a current workflow copy — a
findings report carrying it was rendered by a SKILL that ignored a refusal.* One vocabulary, two
records, the closed three-reason list retired (A20). Build-2's frame (*names which key term moved,
or that no prior cache existed or the sidecar was unreadable*) is the list this build appends to.

### 6. Scope of the wrong-type refusal — D2's slots and their workflow-side intake, no further

The instrument beat says *"every SKILL-rendered input slot"*; D2 says the posture *"reaches these
three slots and no further."* Grounding found the same present-but-wrong-type conflation at the
workflow's intake for **every** optional arg (`:108-116` — `overlayNames`, `crossLayerSlugs`,
`stubSlugs`, `pageHashes`, `cachedScans`, `rulesetComponents` all coerce a wrong type to their
empty value). **Ruling:** this build refuses on the two intake sites that are D2 slots'
(`stubSlugs` `:111`, `rulesetComponents` `:116`) plus the slot loop; the other four are **out of
scope, dispositioned** (§Out of scope) as a `candidate` filing for the next capture — the ruling
that would widen the posture is the owner's, and a build that quietly refused on `pageHashes` would
have re-ruled D2's population. The at-rest instrument notes the four as *not refused* so the gap is
on record, not discovered.

### 7. Interim posture (R1) — not applicable

Every rule this build states ships with its mechanism in the same build: the refusal with its
return; the discovery procedure with its report line; the denominator invariant with its instrument
sentence. No vault sees a window.

### 8. Retirement clause (P-15 / A20 / Q8-A17) — substantive

The obsolescence beat ruled for this build, re-checked at brief time by grep (`grep -rn '## Stubs'
skills/`, `grep -rn 'absent or empty' skills/`, `grep -n 'no prior cache' skills/vlt-lint/references/report.md`).
Every restatement, with its disposition (R2):

| Site | Text | Disposition |
|---|---|---|
| `wiki-index.md:83` | `## Stubs (linked, not yet written)` | **SINGLE HOME — not touched.** The convention is read, never edited; no handshake moves. |
| `full-scale.md:7` | *"parse `{index}`'s `## Stubs` section for its backtick-wrapped slugs and pass them as `stubSlugs`"* | **RETIRED** (bare form) → pointer to `checks.md` Missing targets + the `stub_discovery:` facts (F3). |
| `checks.md:13` | *"a target registered under the index's `## Stubs` section is a recorded gap"* | **RETIRED** (bare form) → *"under the index's Stubs section as `{conventions}/wiki-index.md` states it"* + the procedure (disposition 3) — grounding addition, both modes (F4). |
| `checks.md:39` | *"the `## Stubs (linked, not yet written)` section is well-formed"* | **RETIRED** (the second copy) → *"the Stubs section (heading as `{conventions}/wiki-index.md` states it) is well-formed"* (F4). |
| `fix-and-file.md:9` | *"move resolved stubs out of `## Stubs`"* | **RETIRED** (bare form) → *"out of the Stubs section"* — grounding addition (F5). |
| `vlt-lint-full.js:44` | `slugs cataloged under {index}'s "## Stubs" section` | **RETIRED** → *"under `{index}`'s Stubs section as `wiki-index.md` states it (the SKILL locates and parses it — `checks.md` Missing targets)"* (F1). |
| `vlt-lint-full.js:531` | *"A target registered under the index's ## Stubs section"* | **RETIRED** → same pointer form (F1). ~~roadmap `:476`~~ — moved by build-2. |
| `vlt-lint-full.js:587` (`indexPrompt`) | *"malformed ## Stubs entries"* | **RETIRED** → *"malformed entries under the Stubs section as the convention states it"* — the prompt already hands the agent `convRead('wiki-index')`; the index pass is not cached, so the text change moves no key (F1). |
| `vlt-lint-full.js:374` | *"absent or empty slots [...]"* | **RETIRED** → two caps, `absent [...]` / `empty [...]` (disposition 1) (F1). |
| `vlt-lint-full.js:68-69` header | *"Any slot missing or empty → the fingerprint is '' → a cold sweep, with a coverage_caps entry naming each absent required name"* | **RETIRED** → three-way sentence (F1). |
| `full-scale.md:8` step 2 | *"any slot missing or empty is a cold sweep with each absent required name named in `coverage_caps` (…, never the bare slot)"* — ⚠ **grounding correction:** A20 quotes the pre-build-2 wording *"absent slots named in `coverage_caps`"*; build-2 already re-worded it to the by-name form. The retirement applies to the sentence as it stands now. | **RETIRED** → the three-way sentence of disposition 1 + the refusal pointer (F3). |
| `report.md:89` | the reason list *"names which key term moved (…), or that no prior cache existed or the sidecar was unreadable"* — build-2's frame | **APPENDED, not retired** — the fourth member with its home (disposition 5); the *closed* list is what retires (F2). |
| `report.md:78` | `cold (<reason — names the moved term(s)>, …)` | **WIDENED** — the placeholder names the fourth member and its home (F2). |
| `full-scale.md:19` step 4 | *"if the workflow returns `status: 'failed'` (its near-total-shortfall error shape)"* | **WIDENED** — two predicates named: the shortfall and the pre-dispatch type refusal; the failed-run field list gains `lint_cache:` (F3). |
| `SKILL.md:76` | *"refused upstream at `references/full-scale.md` step 4 (the version-skew defence …)"* | **WIDENED** (pointer only) — *"…step 4 (the version-skew defence, or the pre-dispatch slot-type refusal — both predicates live there)"* (F6). |

**The population statements that must NOT move** (R2's third element): the stub-registered
exclusion itself — *a `[[link]]` to a registered stub is a recorded gap, not a missing target*
(`checks.md:13`, `vlt-lint-full.js:531-535`); `checks.md:43`'s *"counted in the report's
`governance_memory:` denominator line, never silently swept"* and `decision-log.md:78-85`'s two-tier
tail; build-2's stated-cold-run mandate and D4's bound in `full-scale.md` step 2; build-2's
missing-by-name rule (`convention_digests[write-verification]`, never the bare slot when the map is
present).

## Boundary with build-5 — stated so build-5's briefer inherits it (A14 v, A16)

**Merge order on `report.md` is build-3 → build-5; build-5's validator (E1/A16 — one artifact is
the key/type/cardinality source, parsed from `report.md`'s fence) reads the key set from `report.md`
at build-3's commit.** What build-3 leaves there:

| `report.md` site | Build-3 (this brief) lands | Build-5 inherits |
|---|---|---|
| a new scalar key `stub_discovery:` after `files_listed:` (`:14`) — both modes | the key, its `<section located: yes\|no (heading …); N slugs across 1 index>` grammar | a mandated scalar; its population is the index (1) — no per-file cardinality |
| `governance_memory:` (`:44`) widened with `E … S … X … N uncounted` | the four population terms | a mandated scalar whose invariant (S + X + N = E) is a self-check, not a per-file slot |
| `lint_cache:` (`:78`, `:89`) — the fourth cold reason and its home | the vocabulary member | unchanged grammar; the reason never appears on a findings report from a current copy |
| `false_positives_refused:` (promoted by build-5) | **not touched here** | build-5 adds it; the eviction response build-2 shipped is the mechanic it counts |
| `full-scale.md` step 4's failed-run field list | `lint_cache:` added; the second predicate named | build-5's `reason: shape — <slot>` failure artifact reuses the field list as of this commit |

Build-5's briefer should read disposition 5 (the fourth reason renders on the failed-run record, not
the findings report) before designing the shape validator's treatment of `…-lint-failed` records.

## F-sites

Every `file:line` below was re-derived against the working tree at brief time (branch
`cycle15-v0.18.0`, tip `450c886`, build-2 BUILT). Grounding outcome per site is marked. The
roadmap's capture-time cites were pre-build-2 and moved substantially: ~~`:263`~~ → `:287-294`;
~~`:322`~~ → `:374`; ~~`:476`~~ → `:531` (+ `:587`); the arg contract `:56-69` → `:56-71`.

### F1 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the three-way split, the refusal, the pointers (MOVED by build-2; re-grounded)

1. **`:108-116` — intake** *(grounding addition — EXPANDED)*. `:111` `stubSlugs` and `:116`
   `rulesetComponents` coerce a wrong type to `[]`/`{}`. Keep the coercions for the **absent** case
   (`a.stubSlugs === undefined`, `a.rulesetComponents === undefined`) and record a wrong-type fact
   for the present-and-wrong case: collect `wrongTypeSlots.push({slot: 'stubSlugs', got, expected:
   'array'})` / `{slot: 'rulesetComponents', got, expected: 'plain object'}`. `got` is
   `Array.isArray(v) ? 'array' : v === null ? 'null' : typeof v`. The other four optional args
   (`overlayNames`, `crossLayerSlugs`, `pageHashes`, `cachedScans`) are **not** changed
   (disposition 6) — add one comment line naming them as not refused and why.
2. **`:56-71` — the `rulesetComponents` contract comment.** The sentence at `:68-69` becomes:
   *"A slot or required name ABSENT or EMPTY → the fingerprint is '' → a cold sweep, each named in
   `coverage_caps` under its own word (`absent […]` / `empty […]`); a slot or name PRESENT BUT OF THE
   WRONG TYPE → the run is REFUSED before any agent dispatches (`status: 'failed'`, the reason names
   the slot and the type received) — a wrong type is the SKILL's own rendering error, detectable
   before the first dispatch (A15-10, D2)."* `:44-46` (`stubSlugs`) → the pointer wording in
   disposition 8's table, plus *"a present non-array is refused before dispatch"*.
3. **`:283-294` — the loop.** Replace `rulesetSlotsMissing` (one list) with three:
   `rulesetSlotsAbsent`, `rulesetSlotsEmpty`, `rulesetSlotsWrongType` (the last as
   `{slot, got, expected}` entries), computed over `RULESET_SLOTS` per disposition 1's table — the
   slot-level test first (absent → `[k]` in absent; `{}` → `[k]` in empty; non-object → wrong type,
   and the name loop is skipped), then the name loop over `SCANNER_CONVENTIONS`
   (`convention_digests[<name>]` absent / `''` / non-string). Rewrite the `:284-286` comment.
   `composeRulesetFingerprint` (`:298`) returns `''` when **any** of the three is non-empty (D4:
   nothing reusable on a refused run either — moot, since it never dispatches, but the invariant
   holds). `cacheComponents` (`:308-317`) unchanged.
4. **`:374-378` — the cap.** Two caps in place of one, each pushed only when its list is non-empty:
   `` `findings cache cold: rulesetComponents — absent [${rulesetSlotsAbsent.join(', ')}]; no page was reusable this run` `` and the `empty` twin. **Not** a cap for wrong type.
5. **New block between the cache reader (`:361`, after `cacheRejected`) and `toScan` (`:362`) —
   the pre-dispatch refusal** (disposition 2). `if (wrongTypeSlots.length || rulesetSlotsWrongType.length)`
   → `log(msg)` and `return { status: 'failed', mode: 'full', reason, files_listed: pages.length,
   files_checked: 0, files_cached: 0, agent_failed: [], page_unreadable: [], coverage_caps:
   coverageCaps, cost_accounting: costAccounting(), cache_miss_terms: cacheMissTerms,
   cache_records_read: cacheRecordsRead, cache_rejected: cacheRejected, next: … }` — mirror `:446-460`
   field-for-field so step 4's reader sees one shape; `reason` and `next` per disposition 2.
   ⚠ `coverageCaps` is declared at `:371` — move the `const coverageCaps = []` declaration (and the
   two cap blocks `:372-385`) **above** the refusal, or place the refusal after them; the cap blocks
   dispatch nothing. `costAccounting()` must be callable here — it is defined in the cost-accounting
   section (`:138+`) and reads phase rows that do not exist yet; verify it renders every phase at 0.
6. **`:531` comment + `:587` `indexPrompt`** — the pointer wording (disposition 8). ⚠ `INDEX_SCAN`
   (the schema) is **not** edited; only the prompt string. `PAGE_SCAN` and `pageScanPrompt` are not
   touched — `scanFingerprint` is unchanged by this build (verify: build-2's harness `--fingerprint`
   prints the same value before and after).
7. **`:11` `// depends_on:` header** — unchanged (no convention rule moved).

**Why:** the promise's second clause lives here; the workflow is the one executor that can tell a
wrong type from an absence, and after this build it says so before spending anything.

### F2 — `skills/vlt-lint/references/report.md` — `stub_discovery:`, `governance_memory:`, `lint_cache:` (HOLDS: `:14`, `:44`, `:78`, `:89`, `:91`)

- **New line after `:14` (`files_listed:`):** `stub_discovery: <section located: yes|no (heading as
  {conventions}/wiki-index.md states it, overlay-merged); N slugs across 1 index>   # both modes — the
  stub registry the missing-targets check judges against (checks.md, Missing targets); located: no is
  loud, never 0-as-health`.
- **`:44`** → disposition 4's line, the comment reading `# read-before-flag denominator — E is a
  form-agnostic ## heading count by a named instrument, never the matcher that produced S; N = E − S
  − X, rendered even when 0`.
- **`:78`** cold placeholder → `cold (<reason — names the moved term(s), or no prior cache / sidecar
  unreadable; the fourth member, slot rendered with the wrong type: <slot>, renders only on a
  …-lint-failed record>, rejected R of P records read, evicted E by request)`.
- **`:89`** — after *"or that no prior cache existed or the sidecar was unreadable"* append: *"The
  reason vocabulary has a fourth member — `slot rendered with the wrong type: <slot>` — that appears
  on the **failed-run record's** `lint_cache:` line (`full-scale.md` step 4): the workflow refuses a
  wrong-typed slot before any agent dispatches, so a findings report from a current workflow copy
  never carries it; one that does was rendered by a SKILL that ignored a refusal."*
- **`:91`** — after the first sentence add disposition 4's instrument sentence: *"Its total `E` is a
  form-agnostic count of `## ` headings by an unwrapped instrument named in the line (`grep -c
  '^## '` is the expected one; the operating contract's instrument rule names the property, not the
  tool); `S` keyed entries and `X` unclassifiable (the convention's two-tier tail, `checks.md`
  read-before-flag) are the matcher's; `N = E − S − X` is rendered even when 0 — a remainder is a
  heading that is neither, surfaced rather than absorbed. A total derived from the same matcher as
  `S` reads back nothing."*
- **New paragraph after `:91` — "Stub-discovery reporting":** `stub_discovery:` carries the two facts
  the procedure at `checks.md` Missing targets produces; *you compose it yourself in both modes*;
  `located: no` ⇒ `missing_targets` may name registered stubs (a coverage cap in full mode).

**Why:** the report is the only place a vault owner reads; A14 v found it had no home for "wrong"
and no population for two of the three slots.

### F3 — `skills/vlt-lint/references/full-scale.md` — steps 1, 2, 4 (HOLDS: `:7`, `:8`, `:19`; step 2's wording MOVED by build-2 — see disposition 8)

- **Step 1 (`:7`)** — the stub sentence → *"Also derive `stubSlugs` from `{index}` per
  `references/checks.md` Missing targets (the heading source is `{conventions}/wiki-index.md`,
  overlay-merged; the procedure lives there, once) and keep its `section located` / count facts for
  the Step-5 `stub_discovery:` line — a `[[link]]` to a registered stub is a recorded gap, not a
  missing target. Pass the list as an array — a present non-array is refused before dispatch."*
- **Step 2 (`:8`)** — the *"any slot missing or empty …"* sentence → disposition 1's three-way
  sentence with the refusal pointer (*"… the workflow refuses before any agent dispatches — step 4's
  failed-run posture, `reason: slot rendered with the wrong type: <slot> (got …, expected …)`;
  re-render the slot per this step and re-run, nothing was spent"*). The digest steps, the required
  names, build-2's cold-when text and D4's bound are **unchanged**.
- **Step 4 (`:19`)** — the predicate sentence → *"if the workflow returns `status: 'failed'` — its
  near-total-shortfall shape, **or** its pre-dispatch refusal of a wrong-typed input slot
  (`rulesetComponents`, a `convention_digests` entry, `stubSlugs`) — **or** …"*; the failed-run
  record's field list gains `lint_cache: cold (<reason>, rejected R of P records read, evicted E by
  request)` after `cost_accounting`, with the note that on a type refusal the reason is the fourth
  vocabulary member (`report.md`); the directed-refusal sentence names both causes and both next
  moves (re-run after `vlt-upgrade` / re-render the named slot and re-run).

### F4 — `skills/vlt-lint/references/checks.md:13` + `:39` (HOLDS; `:13` a grounding addition)

- **`:13`** — the parenthetical *"(a target registered under the index's `## Stubs` section is a
  recorded gap, not a missing target)"* → the procedure of disposition 3, as a sub-clause of the
  bullet: the heading read from the merged convention, the `## ` match, the backtick-slug collection
  to the next `## `, the two facts (`section located: yes|no`, count) rendered on `stub_discovery:`
  (Step 5), and `located: no`'s coverage-cap consequence in full mode. The population sentence that
  follows (`[[ ]]`-delimited text only) is unchanged.
- **`:39`** — *"the `## Stubs (linked, not yet written)` section is well-formed"* → *"the Stubs
  section (heading as `{conventions}/wiki-index.md` states it, overlay-merged) is well-formed"*.
- **`:43`** — unchanged (its pointer to the Step-5 line stands; the mechanics home at
  `report.md:91`).

### F5 — `skills/vlt-lint/references/fix-and-file.md:9` (HOLDS; grounding addition)

*"move resolved stubs out of `## Stubs`"* → *"move resolved stubs out of the Stubs section
(`{conventions}/wiki-index.md`)"*. A pointer; the auto-fix is unchanged.

### F6 — `skills/vlt-lint/SKILL.md:76` (HOLDS)

The pointer widening in disposition 8's table — one clause. `:3`/`:4`/`:39`/`:74` unchanged.

### F7 — `factory/cycles/15-nothing-reads-it-back/fixtures/build-2-key-harness.mjs` — case (g)'s cap literal (BUILT fixture; cross-build obligation)

Build-2's case (g) asserts the cap text *"absent or empty slots [convention_digests[write-verification]]"*
(its BUILT `status:`, Verification 1). After F1.4 the string is `absent [convention_digests[write-verification]]`.
Update the assertion in the same build and re-run the whole build-2 case table (all 15 expectations
must still hold; `--legacy` mode is unaffected). Recorded so build-2's check (1) is not silently
broken by this build — the ledger's build-3 bullet names it.

### F8 — `factory/cycles/15-nothing-reads-it-back/fixtures/` — three fixtures + one harness (NEW; factory-side, un-enumerated)

- **`build-3-index-stubs.md`** — a minimal index (frontmatter, two category `##` rows, then
  `## Stubs (linked, not yet written)` with the three specimen slugs as `- \`birria\` — …` items) and
  **`build-3-index-bare-stubs.md`** — the same with the bare `## Stubs` heading. The pair is the
  discriminator for check (2).
- **`build-3-decision-log-tail.md`** — the **twelve unbracketed `## YYYY-MM-DD — …` heading lines
  frozen verbatim from `{field-vault}`'s live `_agent/mint/decision-log.md`** (headings only, one
  placeholder body line each — the capture's instruction that the tail be frozen from the live file,
  not reconstructed from its shape), plus three schema-keyed entries (`## [YYYY-MM-DD] <kind> — …`
  with `- kind:` and `- ref:`) and one `kind:`-without-`ref:` entry. E = 16, S = 3, X = 13, N = 0.
  A **mutated twin** for the widening (a `## Notes` section heading appended) is produced by the
  harness in memory, not committed. **Scrub:** the heading lines name minted partners by domain role
  (a dog trainer, a health coach, a chess coach — generic domain vocabulary the module's own examples
  already use); any personal name or real path in a heading is replaced with `{owner}` /
  `{field-vault}` before commit.
- **`build-3-type-harness.mjs`** — loads the workflow the way `build-2-key-harness.mjs` does
  (duplicate the ~30-line shim with a comment naming the source — a shared shim is a refactor for
  whichever build adds a third harness, not this one), wraps `agent` in a **counting** stub, and runs
  the case table in §Acceptance (1); a `--stubs` mode runs the link-target cases in (2) over a
  two-page fixture where page A links `[[birria]]`; a `--tail` mode runs the decision-log counts in
  (3) as a node re-implementation of the two instruments (`^## ` count; schema/tail classification)
  over the fixture and its mutated twin. Exit 0 iff every expectation holds.

## Registration

**None.** No new skill, workflow, or package-lint check (E4 untouched). **No handshake owed:**
`wiki-index.md` is read, not edited; no `governance/_meta` file changes; `vlt-lint/SKILL.md:4` pins
unchanged; the workflow's `// depends_on:` header unchanged — E5/E7 green; **E6 unchanged**
(`PAGE_SCAN`/`INDEX_SCAN` not edited — an `indexPrompt` string edit is outside E6's measure).
`module-help.csv` untouched. The contract is not touched (no C6 cost).

## Out of scope (dispositioned)

- **The four other optional args' wrong-type intake** (`overlayNames`, `crossLayerSlugs`,
  `pageHashes`, `cachedScans` — `:108-115`) — D2 reaches three slots and no further; refusing on
  these would re-rule the population. **File as a `candidate`** at handoff: *"the fan-out's intake
  coerces a wrong-typed optional arg to its empty value for four args build-3 did not cover"* —
  the harness records them as not refused (§Verification 6).
- **A shipped stub-discovery executable** — build-4's `pageLinks` sibling script (A12) is the natural
  home for index parsing alongside link derivation; this build ships the procedure as prose with an
  independent located/count read-back, per Q8's letter. Recorded as a follow-on, not scope.
- **`pin_vector` rendering** — dissolved (build-2 disposition 1); no site names the slot.
- **`convention_digests` population** — build-2's (A4); the three names and `SCANNER_CONVENTIONS` are
  not touched here.
- **`scanModel`'s `{ error }` guard shape** — build-2's; a caller-contract class, not a rendering one
  (disposition 2).
- **`false_positives_refused:` promotion and the shape validator** — build-5 (E1/A16); §Boundary.
- **The `governance_memory` count itself being wrong in a vault** (47 vs 59) — no code to repair
  (A15-6 grounding); the invariant line is the repair, and the live specimen grades check (5).
- **`report.md:3`'s release-gate claim** — build-5's retirement (A20).
- **A stub-age finding** (`wiki-index.md:90`, *"may surface long-dangling stubs"*) — no filing asks
  for it.

## Verification (unit, at rest — lifecycle step 5)

1. **Type harness (P-18 — built from the failure's shape):** `node fixtures/build-3-type-harness.mjs`
   over the case table in §Acceptance (1); record the per-case `status` / `reason` / agent-invocation
   count / `cost_accounting` scan row in the BUILT `status:`. **Failability:** run the same table
   against `git show 450c886:skills/vlt-setup/assets/workflows/vlt-lint-full.js` (pre-build-3) and
   record that cases (a), (b), (f), (g) there return a **findings report with `files_cached: 0` and
   the `absent or empty` cap** (the conflation A15-10 filed) instead of a refusal — four cases that
   flip between the builds.
2. **Stub-discovery reader protocol:** apply the `checks.md:13` procedure by hand (no `gh`, scratch
   output) to both index fixtures; record `located`/count for each; then `--stubs` mode: with the
   three slugs passed → `missing_targets: []`; with `[]` → `missing_targets: ['a → birria']`; with
   `'birria'` (a string) → refused pre-dispatch.
3. **Decision-log instruments:** `grep -c '^## ' fixtures/build-3-decision-log-tail.md` → 16;
   `--tail` mode → `{E: 16, S: 3, X: 13, N: 0}` and over the mutated twin `{E: 17, S: 3, X: 13, N: 1}`.
4. **Single-home / retirement greps:** `grep -rn '## Stubs' skills/` → exactly one hit,
   `wiki-index.md:83` (the `(linked, not yet written)` form; comments and prose all point);
   `grep -rn 'absent or empty' skills/` → 0; `grep -n 'slot rendered with the wrong type'
   skills/vlt-lint/references/report.md skills/vlt-lint/references/full-scale.md
   skills/vlt-setup/assets/workflows/vlt-lint-full.js` → ≥ 1 in each; `grep -n 'stub_discovery'
   skills/vlt-lint/references/report.md skills/vlt-lint/references/checks.md
   skills/vlt-lint/references/full-scale.md` → ≥ 1 in each; `grep -c 'section located'
   skills/vlt-lint/references/checks.md` ≥ 1 (the procedure is in the both-modes file, not only
   `full-scale.md`).
5. **Scan-surface invariance:** `node fixtures/build-2-key-harness.mjs --fingerprint` before and after
   — **equal** (this build touches no `PAGE_SCAN`/`pageScanPrompt` byte); the full build-2 case table
   still passes after F7 (15/15).
6. **The not-refused four:** the harness passes `pageHashes: []` (an array) and records the
   pre-existing coercion to `{}` — a cold sweep with no refusal — as the on-record gap for the
   candidate filing (§Out of scope). Informational, not an expectation.
7. **Package lint** — `uv run tools/package-lint.py` Groups **A/B/C/E** PASS (E5/E6/E7: header and
   schema budgets unchanged — E6 must still read PAGE_SCAN 3676). D / `--expect-version` is build-7's.
   **Handshake:** nothing moved; Group E is the check of record.
8. **R4 (enumeration widening):** no shipped file is added; fixtures live in the un-enumerated cycle
   `fixtures/` dir. `R4: not applicable — declared exclusion, reasoning above.`
9. **R3 (legal response):** no finding class is added or changed — the refusal is a failed-run
   record (its `next:` is its response, homed in the workflow return and `full-scale.md` step 4);
   `stub_discovery:` and `governance_memory:` are report lines, not findings. `R3: not applicable
   (no finding class); the refusal's response is single-homed at step 4.`
10. **Scrub** — no vault-local paths or personal content in any shipped edit or fixture (F8's scrub
    rule applied to the frozen headings; the three stub slugs and the research-note vocabulary are
    already on the public roadmap).
11. **Cleanup** — no `.decision-log.md` in the tree; scratch outputs removed.

## Release

Not the release build — v0.18.0's bump, `--expect-version 0.18.0` gate and tag ride build-7. One
release-time note for build-7's briefer and `vlt-release`: the v0.18.0 CHANGELOG collects this
brief's `title:` verbatim; the field-facing consequence worth one sentence beside it is that a vault
whose index still carries a bare `## Stubs` heading will render `stub_discovery: section located: no`
on its first post-upgrade sweep — the honest reading, and the fix is the index heading (`wiki-index.md`).

## Acceptance (live — appended to the roadmap ledger)

**Five checks — all `[ship-verifiable]` (GATE); no field-contingent check.** `specimens: 16/17`.
*(A sixth, "a wrong-type refusal fires in the field," was considered and not written: its event is a
SKILL rendering error nothing schedules and no vault has a reason to produce — the anatomy's own test
for a check measuring the wrong thing; check (1) is the instrument.)*

**(1) `[ship-verifiable]` — at rest — GATES.** *A wrong-typed input slot is refused before any agent
dispatches, and absent/empty are named as such.* **Instrument:** `fixtures/build-3-type-harness.mjs`
over a two-page fixture (baseline inputs from build-2's harness), agent stub **counting**
invocations; cases: (a) `convention_digests: []` → `status: 'failed'`, `reason` names
`convention_digests` + `array`, `next:` names step 2, agent count 0, `cost_accounting` scan row 0
dispatched; (b) `convention_digests.frontmatter: 42` → refused naming
`convention_digests[frontmatter]` + `number`; (c) `convention_digests: {}` → findings report,
`files_cached: 0`, cap `empty [convention_digests]`; (d) `write-verification` key absent → cap
`absent [convention_digests[write-verification]]`; (e) `convention_digests.frontmatter: ''` → cap
`empty [convention_digests[frontmatter]]`; (f) `stubSlugs: 'birria'` → refused naming `stubSlugs` +
`string`; (g) `rulesetComponents: []` → refused naming `rulesetComponents` + `array`; (h) baseline →
2 cached, no cap. **Adversary:** property — *a wrong type never reaches dispatch and is never
rendered as an absence*; passing-violating state — the refusal return exists but sits **after** the
fan-out loop (agents already dispatched, then "refused"), or `reason` names the slot but the SKILL's
step 4 reads only the shortfall predicate and falls through. **Widened:** the counting stub asserts
**0 invocations** on every refusal case (not merely `files_checked: 0`), and Verification 4 asserts
`full-scale.md` step 4 names the refusal predicate; the harness is proven failable against
`450c886` (cases (a)/(b)/(f)/(g) flip from cold-cap to refusal).

**(2) `[ship-verifiable]` — at rest — GATES.** *A failed stub discovery is distinguishable from an
empty registry, and registered stubs are never missing targets.* **Instrument:** the `checks.md:13`
procedure applied as a reader protocol to `fixtures/build-3-index-stubs.md` → `section located:
yes; 3 slugs` (`birria`, `jesse-minter`, `nfl-draft-safety-archetypes`) and to
`…-bare-stubs.md` → `section located: no; 0 slugs` + the coverage cap; then `--stubs` mode: the
three slugs passed → `missing_targets: []`; `[]` passed → one missing target (the A15-2 observable
reproduced); a string passed → refused. **Adversary:** property — *`located: yes` is earned by a
heading read from the merged convention, not from memory*; passing-violating state — a reader who
"knows" the long form writes `yes` on both fixtures. **Widened:** the fixture **pair** is the
instrument — a protocol run that reports `yes` on the bare-heading fixture FAILS; and the rendered
line must quote the heading text it matched.

**(3) `[ship-verifiable]` — at rest — GATES.** *The `governance_memory` total is produced by an
instrument independent of the matcher, and a remainder is rendered.* **Instrument:** over
`fixtures/build-3-decision-log-tail.md` (the twelve live-frozen unbracketed headings + 3 keyed + 1
`kind`-no-`ref`): `grep -c '^## '` → 16; the classification → S 3, X 13, N 0; over the mutated twin
(a `## Notes` heading appended) → E 17, N 1. **Adversary:** property — *E is not derived from the
matcher that produced S*; passing-violating state — a SKILL computing E as `S + X` (or by the schema
regex over both heading forms) renders `N: 0` on the fixture and passes. **Widened:** the mutated
twin — any same-matcher derivation renders `E 16, N 0` where the instrument says `E 17, N 1`, and
the line must name the instrument.

**(4) `[ship-verifiable]` — at rest — GATES.** *The stub heading has one home, the retired wordings
are gone, and the fourth reason has its home.* **Instrument:** Verification 4's grep manifest +
Verification 5's `scanFingerprint` equality + build-2's 15/15 after F7, recorded in the BUILT
`status:`. **Adversary:** property — *every site that names the stub heading or the slot cases agrees
with the single home, in every mode*; passing-violating state — every site points at `wiki-index.md`
but the procedure lives only in `full-scale.md`, which scoped and small-full runs never load, so an
inline run has a pointer and no procedure. **Widened:** the manifest requires `section located` in
`checks.md` (the both-modes file), not only in `full-scale.md`.

**(5) `[ship-verifiable]` — on the v0.18.0 upgrade sweep (bounded: it happens anyway) — GATES.** *The
live report's population lines are instrument-derived.* **Instrument:** the first full-mode report
persisted after the `{field-vault}` 0.18.0 upgrade carries `stub_discovery: section located: yes …; 6
slugs across 1 index` (the field index's registry — A15-11's manifest counts 6) with none of the six
in `missing_targets`, and `governance_memory:` whose `E` equals `grep -c '^## '` over the live log
**run independently by the discharger at discharge time**, with `N uncounted` rendered (0 expected)
and the instrument named. **Adversary:** property — *the numbers on the line are what the instruments
return, not what the renderer remembers*; passing-violating state — a plausible `E` (say 66) rendered
from memory of this brief. **Widened:** the discharger re-runs both instruments (the heading count and
the index parse) and compares; a mismatch on either FAILS. No further passing-violating state found.
