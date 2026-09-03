---
title: 'Build #5 — the persisted report: after this ships, a vault owner can read every persisted lint report, and each slot `report.md` mandates per-file carries one entry per file — or the run fails loudly instead of writing a report that quietly isn''t one'
status: 'BRIEFED 2026-09-02 — build via bmad-workflow-builder in a fresh session (headless brief; nine dispositions recorded inline, none owner-ruled). The builder rewrites this line to a BUILT record — `BUILT <date> — <what landed>; <verification result>. Deviations/notes: (1) … (2) …` with numbered deliberate deviations (the `build-15-spec-convention.md` precedent) — deletes any `.decision-log.md`, and makes ONE commit for the build on `cycle15-v0.18.0`. Not the release build — no version bump.'
module_code: 'vlt'
created: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-08-27-153000-persisted-lint-report-is-not-machine-readable.md (A15-7 — the parse requirement; direction 1 the pre-persist parse gate; direction 3 dies (A20); the 1-of-6 manifest + the line-102 fragment)'
  - 'factory/inbox/2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md (A15-8 — direction 1 validate-at-persist + E1''s cardinality check; instances (a) the 27-file rollup, (b) `fixes_applied:` dropped, (c) `backlog_filed:` dropped; the `type:` distribution OUT)'
roadmap: 'factory/cycles/15-nothing-reads-it-back/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-01/02): build-5 bullet (binds E1, D2); E1 as ruled (validation + cardinality, `type:` distribution out) and as MADE BUILDABLE at the roundtable (A16 — one schema artifact never a second list, presence+type+cardinality never closure, `false_positives_refused:` promoted, mechanical populations never `len()`, the `uv run` gate, the `…-lint-failed.yaml` failure artifact, never no file); D2 as rewritten (A14 (iv) — the denominator comes from an instrument independent of the value''s producer); A14 (v) merge order on `report.md` 3 → 4 → 5; A20 the obsolescence retirement of `report.md:3`''s release-gate claim; the brief-time question REWORDED (which independent instrument produces each per-file population); Cycle 14 build-4 brief §3 (no serializer) honoured, not superseded.'
risk: 'low-moderate — no convention version moves (`report.md` is a skill reference, not a handshaked convention; `write-verification` / `extraction` / the operating contract are read, never edited — package-lint C6 not engaged); two new PEP 723 scripts under `skills/vlt-lint/scripts/` (the first with a real inline dependency, `pyyaml`, so the `uv`-absent posture is stated); the SKILL''s Step 6 becomes a three-move ritual (scratch → check → mv) and the report shape gains a line grammar, one promoted slot, one population line and two always-render rules; the workflow is untouched.'
---

# Build #5 — the persisted report

**Promise (owner-ratified 2026-09-02, carried verbatim):** *After this ships, a vault owner can
read every persisted lint report, and each slot `report.md` mandates per-file carries one entry
per file — or the run fails loudly instead of writing a report that quietly isn't one.*

The lint report is the module's most-read artifact and, until now, the one nothing reads back.
`vault-operating-contract.md:330` mandates that a structured report-emitting verb persist its
report; `vlt-lint/SKILL.md:74` persists an **agent-authored** block content-verbatim;
`references/report.md` states the block's shape slot by slot — and between the mandate and the
render there is nothing. A15-7 is that absence at the parse level (one archived report in six
does not load; re-verified this brief on the live archive: **one in nine**, the same report). A15-8
is the same absence one level up (a report that loads carried one string standing in for 27
files, and two mandated keys vanished between two renders of the same skill with no code change
between them — *"intermittence is the signature of no enforcement point"*). `ST-7` names both as
its output-side instance.

This build closes the absence with **one reader and one ritual**: a `uv run` script that parses the
block back under a strict parser, checks every mandated key for presence and type against the shape
`report.md` itself states (never a second list), and — the load-bearing clause — checks every
per-file slot's entries against a population an **independent instrument** walks from disk. The
SKILL's Step 6 runs it before any file lands under `{lint_reports}`; a failed gate re-renders once
from the same facts and, failing again, persists a `…-lint-failed.yaml` record that says why — never
no file, never a `-lint.yaml` that is not one.

**Three clauses of the promise, three obligations of this brief:** *read every report* → the parse
gate (F1, F3; check (1)); *one entry per file* → the cardinality check over a mechanically walked
population (F2, F1; check (4)); *fails loudly* → the two-attempt failure route with its named
artifact (F3; check (5)). The per-file clause is E1's ruling made gradeable — a presence-only draft
was rejected at ruling time because the rollup *has* the key. **A validator that passes the rollup
has built nothing.**

All rejected alternatives in the parent filings are settled — do not re-litigate: A15-7's direction
2 (constrain the emitting slots) is a cure available to the author, not an enforcement point;
direction 3 (declare the archive best-effort) **dies** in this build (A20); A15-8's direction 2
(move the population slots off the hand-render) is not taken as a slot mover — its population
*instrument* ships (F2) while the render stays the SKILL's; direction 3 (rule the rollup legal)
cannot explain instances (b) and (c) and is closed by the filing's own follow-up; the `type:`
distribution is mandated nowhere and stays **out** (E1). Cycle 14 build-4 §3's ruling — *the report
persist gets no serializer* — is **honoured, not superseded** (disposition 4): the gate is a reader;
the bytes it admits are the agent's.

## Brief-time dispositions

### 1. The shape source is `report.md`'s own fence, read by a line grammar stated once — never a second list *(A16 (1))*

**Ruled: the validator derives the mandated key set, each key's type, and the per-file marking by
parsing the fence at `report.md:9-81` line by line, under a grammar `report.md` states in one
paragraph directly above the fence. No key list, type table, or per-file roster is typed anywhere
else — not in the script, not in a schema file.** The roundtable offered *"parsed from the fence,
or a schema file `report.md` points at"*; the fence route is taken because a schema file beside a
fence is two statements of the shape until something compares them, which is the A14-8 defect with
an extra step. The grammar is small enough to state and mechanical enough to implement:

- **Structure by indentation.** A line `^(\s*)([a-z_]+):(.*)$` inside the fence is a key at the
  depth its indent gives; a key whose value part is empty and whose next line is deeper is a
  **map** whose children are the deeper keys (`fix_now:`, `flag_for_human:`, `opportunities:`).
- **Type by the value's first non-space character.** `[` → **list**; `{` → **map** (an inline map
  — its children are not parsed and not validated; declared, see §Out of scope); anything else →
  **scalar** (`<…>` placeholders and bare literals alike — `mode: scoped`, `files_checked: 10`,
  `high_value_gaps: unmeasured` are all scalars).
- **Per-file marking.** A list whose placeholder opens `[<para-file:` is a **per-file slot over the
  PARA walk** — the population disposition 3 names. The five today: `para_missing_attestation`,
  `para_status_unknown`, `para_type_unknown`, `para_author_unknown`, `para_writer_unauthorized`
  (`report.md:34`, `:38-41`). A `[<page…` list is a wiki per-page slot and is **not** cardinality
  checked this build (§Out of scope).
- **Mode conditionality by one marker.** A line whose trailing comment begins exactly `# full mode
  only` is mandated when `mode: full` and may be absent when `mode: scoped`. One key carries it
  after this build: `attestation_census` (`:37`, today's comment reads *"full mode — …"*; it is
  reworded to open with the marker). **Every other key renders in both modes** — disposition 2 gives
  the two slots that today do not their both-mode forms.
- **Comments are otherwise ignored**; everything after `#` outside a `<…>` placeholder is
  documentation for the reader. (A `#` inside a `<…>` placeholder — none exists today — would be
  part of the placeholder; the grammar paragraph says so.)

**The grammar is a contract between two files and it must fail loudly when broken.** The script
refuses (`status: schema_unreadable`, non-zero) when the fence is missing, when a line inside it
matches no rule, or when the parse yields fewer than the top-level keys the fence carried at this
build's commit — the last is the one number the script hard-codes, a **floor** (the `CASE_FLOOR`
precedent) that catches a fence someone accidentally truncated, not a key list. The at-rest oracle
`fixtures/build-5-expected-schema.json` (F7) is hand-written from the fence and must match the
parse byte-for-byte; **a later build that edits the fence re-derives the oracle** (build-7's A8
line is the first — §Boundary with build-7).

**Where the script finds `report.md`:** relative to its own `__file__`
(`../references/report.md`) — the skill tree ships whole (`verify-skill-manifest.py:14`), so the
sibling is always there; `--schema <path>` overrides it (the harness feeds mutated fences through it,
check (2)).

### 2. Presence + type, never closure; a slot that does not apply renders the empty form of its type *(A16 (2))*

**Ruled.** For every key the grammar yields: **present** (absent → `key missing: <path>`), **not
null** (`key:` with nothing after it parses to `None` and reads as absent — a bare key is not a
rendered slot), and **of the grammar's type** — `list` accepts a YAML/JSON sequence only, `map` a
mapping only, `scalar` a string, integer, float or boolean. **Extra keys pass** at every depth — every
one of the nine archived reports carries keys the fence does not (`instrument_findings`,
`enforcement_kit`, `scope_note`, `false_positives_refused` itself); closure would have failed all
nine and taught the SKILL to stop saying things. The check reports them (`extra_keys: [...]`) and
does not fail on them.

Two slots today render a **scalar literal in scoped mode where the fence types them otherwise**, and
one slot is **absent by design** — each is a passing-violating state under a type check, so each is
resolved in `report.md` rather than in the validator:

- **`cost_accounting` (`:78`)** — `{phases: [...], ...}` in full mode; *"inline/scoped runs render
  the literal: not instrumented (inline run)"* today. After this build a scoped run renders the
  **typed empty form** `cost_accounting: {phases: [], not_instrumented: "inline run"}` — the same
  device `attestation_census` already uses for a zero-page wiki (`{pages_total: 0, ...}`). The map
  stays a map. (`scanner_return_rejected:` at `:16` keeps its scoped literal — it is a scalar.)
- **`spec_candidate_standing` (`:66`)** — *"no line when [`_agent/handoffs/`] is empty"* today. A
  slot that is sometimes absent by rule is the ST-7 disease inside the shape statement: a reader
  cannot tell the rule's absence from a dropped key. After this build it **always renders**, the
  denominated zero reading `0 standing candidate(s) — _agent/handoffs/ empty`. `checks.md:51`
  restates the collapse-onto-one-line rule and not the no-line rule — it does not move.
- **`attestation_census` (`:37`)** — genuinely full-mode (the fan-out's reduce computes it over
  `{wiki}`; a scoped run has no census). It keeps its conditionality under the grammar's one marker.

**Non-per-file lists are not cardinality-checked**, and a one-entry `["NONE — …"]` in
`fixes_applied:` or `backlog_filed:` is legal (the field's honest denominated rendering, A15-8's
follow-up). The adversary reading — *a prose sentence in a list passes the type check* — is true and
is not this build's target: the promise's cardinality clause names slots `report.md` mandates
**per-file**, and those are the five the grammar marks.

### 3. Which independent instrument produces each per-file population — the reworded brief-time question *(A16 (3), D2 (iv))*

**Ruled: one new executable, `skills/vlt-lint/scripts/lint-para-facts.py`, walks the `para_*`
population from disk and is the population instrument for all five per-file slots. The validator
does not accept a population from the SKILL — it imports the walker and runs it itself over the
directories it is given.** This is A16's *"never `len()` of the rendered list"* made structural: the
population never transits the agent, so it cannot be rendered wrong the way the slot was.

**The population (P).** `checks.md:19`'s statement, implemented: every file under `{projects}`,
`{areas}` and `{resources}` with the `{wiki}` subtree excluded **by name** (`full-scale.md:7`'s
carve-out — the wiki's pages are the page population, never `para_*` candidates). The script takes
`--dir <path>` (repeated; the SKILL resolves the three from the `vault_structure` map, exactly as it
resolves `crossLayerSlugs`) and `--exclude <path>` (repeated; `{wiki}`), walks every `*.md`
recursively, and emits per-file **facts, never verdicts** (the build-4 posture): path relative to
`{project-root}`, `has_frontmatter`, `type`, `author`, `status`, `created`, `attested`
(`verified_by` **and** `verified_at` both present and non-empty — `write-verification.md:44`'s pair),
and `basename`. The instrument is named in the report by path, per the operating contract's
instrument rule (`vault-operating-contract.md:352`).

**Per slot — what the validator checks, and why the answer differs:**

| slot | membership (every mode) | count-equals (full mode) | instrument for the count |
|---|---|---|---|
| `para_missing_attestation` | yes | **yes** | the walker's mechanical predicate: `type` present ∧ `author ∈ {agent, hybrid}` ∧ ¬`attested` ∧ not operational-record class (`basename ∈ {charter.md, record.md, register.md}` ∨ `type ∈ {charter, record, register}` — `checks.md:17`'s carve-out, both halves stated there) |
| `para_status_unknown` | yes | no — declared | the per-type `status:` enums live in `{conventions}/extraction.md` prose; encoding them in a script is a second home |
| `para_type_unknown` | yes | no — declared | the recognized set's single home is `extraction.md` and **build-6 moves it in this same release** (A6) — an instrument written the week its source moves would be wrong on arrival |
| `para_author_unknown` | yes | no — declared | the closed `human\|agent\|hybrid` enum is Cycle 14 carry 6's next supersession candidate (roundtable §Out of scope); a count instrument would harden the enum this cycle set out to loosen |
| `para_writer_unauthorized` | yes | no — declared | the identity join at `checks.md:20` is **build-7's** edit (D-E); the walk-up-to-charter resolver is build-7's to instrument if it wants one |

**Membership** is the clause the promise names — *one entry per file*: every entry of a per-file
slot must open with a path token (the text before the first `: ` or ` — `, whichever comes first;
`report.md:34`'s own placeholder `<para-file: …>` fixes that form) that resolves to **one member of
P**, and no two entries may name the same file. A rollup — *"27 PARA files carry a vault `type:` …"*
— opens with no member of P and fails; so does *"same 4 no-frontmatter files as `para_type_unknown`
above"*, and so does a prose sentence standing where zero findings belong (*"NO FINDINGS, and the
zero is not health this run: …"* — the field's 2026-09-01 `para_writer_unauthorized` entry, observed
this brief). All three forms are on the live archive today. The honest home for the prose those
entries carry is the population line below, `rulings_recorded:`, or `coverage_caps:` — never a
per-file slot.

**Count-equals** applies to the one slot whose class is a pure byte fact and whose rule is stable
this release. It catches what membership cannot: 26 well-formed entries where the walk finds 27. It
runs in **full mode only** — a scoped run lists the files in scope, not the population — so a scoped
report is membership-checked and its `para_scan:` line still states P.

**The population line.** `report.md` gains, beside the `para_*` slots, one denominated scalar:
`para_scan: <P files walked under {projects}/{areas}/{resources}, {wiki} subtree carved out
(instrument: scripts/lint-para-facts.py); M carry author agent|hybrid with no attestation outside
the operational-record class>` — E's role for `governance_memory:` (`:46`), read the same way. The
script prints the exact line text (`--line`) and the SKILL pastes it at Step 5; the validator
re-walks at Step 6 and compares its own line text with the report's scalar **by string equality** —
a read-back with no regex over prose. A mismatch fails as `para_scan: rendered line does not match
the walk`.

**Why the other four are declared and not deferred silently.** Each declaration names the site
whose single-home status blocks the instrument; when that site gains a machine-readable form (an
overlay-declared vocabulary is already data; the recognized set after build-6 could be), the count
leg is a one-table extension of the walker. A `candidate` filing is owed at handoff for the
`para_type_unknown` leg, bound to build-6's recognized set (§Out of scope).

### 4. The gate is a reader; the SKILL persists the bytes it validated — Cycle 14 build-4 §3 honoured *(A16 (4), (5))*

**Ruled: `scripts/lint-report-check.py check` writes nothing.** It reads one file, prints one JSON
object on stdout and exits 0 (`status: ok`) or 1 (`status: failed`, with `reason` — one clause per
defect joined `; `, in the fixed vocabulary `key missing: <path>` / `wrong type: <path> (got …,
expected …)` / `not a member: <slot> ← <entry head>` / `duplicate: <slot> ← <path>` / `count: <slot>
rendered N, walk finds M` / `para_scan: rendered line does not match the walk` / `parse: <parser
message>`) or 2 (`status: schema_unreadable`). Cycle 14 build-4's ruling that *"the report persist
gets no writer at all"* stands untouched: there is still no object to serialize from, the block is
still the agent's, and exactly one serializer exists in `vlt-lint` (`lint-cache.py`, for the
machine-constructed cache records).

**The Step 6 ritual (F3)** is therefore three moves the SKILL makes, in order, in both modes:

1. Write the Step-5 block — fence stripped, content-verbatim — to a scratch path **outside the
   vault** (`mktemp`), never under `{lint_reports}`.
2. Run `uv run --quiet "$SKILL/scripts/lint-report-check.py" check --report <scratch> --mode
   <mode> --dir {projects} --dir {areas} --dir {resources} --exclude {wiki}`.
3. On `ok`: `mv` the scratch file to `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` (or `.json`) —
   the bytes that were validated are the bytes that land — then append the Step-6 `{log}` line.

**The `.yaml` home needs `pyyaml`; the `.json` home needs nothing.** The script declares
`dependencies = ["pyyaml"]` in its PEP 723 header and imports `yaml` **lazily, only for a `.yaml`
report**; `json.loads` is stdlib. `report.md:3`'s no-dependency clause is re-pointed at exactly this
route (F1): with `uv` present either home validates; **with `uv` absent** the SKILL renders the
`.json` home (`report.md:3`'s JSON-subset strategy — a rendering, not a second authoring act) and
runs `python3 "$SKILL/scripts/lint-report-check.py" …` directly. `module.yaml:87-89`'s `uv` row
gains that posture (F6). The gate is never skipped for want of a library — that is the whole point of
the JSON subset.

**Strict** means `yaml.safe_load` over the whole file as one document (a multi-document stream or a
non-mapping top level fails as `parse:`), and `json.loads` likewise.

### 5. "Fails loudly" names what the owner is left holding — the two-attempt route and the failure artifact *(A16 (5))*

**Ruled.** On a `failed` verdict at Step 6:

- **Attempt 2 — re-render once from the same Step-5 facts.** The workflow's returned object (full
  mode) and the SKILL's own pass results are still in session; the SKILL re-authors the block against
  the check's `reason` (a missing key rendered, a rollup expanded to its members from the walk's
  paths, a wrong-typed slot re-typed) and runs the check again. **Never a re-sweep** — nothing was
  wrong with the facts.
- **Attempt 2 fails → the failed-run record.** The SKILL writes
  `{lint_reports}/YYYY-MM-DD-HHMM-lint-failed.yaml` (or `.json`) — the **existing** failed-run shape
  `full-scale.md:19` step 4 defines, with `status: failed`, `reason: shape — <the check's reason
  verbatim>`, `files_listed` / `files_checked` / `files_cached` as this run knew them, `lint_cache:`
  as it would have rendered, `next: re-render from the returned workflow object, not re-sweep`, and
  one field the shape gains for this predicate: **`unvalidated_report: |`** — the full Step-5 block
  as a YAML literal block scalar (indented two spaces; a literal scalar parses whatever the block
  contains, including the line that broke it). The record is itself run through the check
  (`--kind failed`: presence of `status` / `reason` / `next` / `unvalidated_report`, the same
  scratch → check → mv ritual) so the failure artifact cannot be a second unreadable file.
- **The Step-6 `{log}` line does not write.** `lint-debt` does not reset (the B10-12 mirror at
  `SKILL.md:76`): fixes were applied at Step 3 and a report the archive cannot read is the *"silently
  rests on 5 of 6"* produced by the fix; a debt counter that reset on it would hide that.
- **The in-session YAML remains the owner's copy.** The SKILL surfaces the check's `reason` and the
  record's path in chat. Should the failed record itself fail its check (a botched literal-scalar
  indent — the only way), nothing lands under `{lint_reports}`, the SKILL says so, and the
  in-session block is what the owner holds. **Never a `-lint.yaml` that failed the gate.**

**A scoped run takes the same route** — the failed-run record's shape is homed at `full-scale.md`
step 4 today, which a scoped run never reads; F3 states the shape-failure record's fields at Step 6
(router-visible) and F4 gives step 4 the pointer for its third predicate, so the two homes are one
record with one field list and a pointer, not two shapes.

### 6. `false_positives_refused:` is promoted into the shape as a mandated list *(A16 (2))*

**Ruled.** The slot the field invented (every full-mode report since 2026-08-30 carries it, and it
carried every specimen this cycle — A15-1's three orphans, A15-3's anchor, A15-4's substitution,
A15-5's summaries) ships nowhere; a validator that admitted it only as an extra key would leave the
cycle's best evidence channel unmandated. It enters `report.md` after `rulings_recorded:` as
`false_positives_refused: [<slot: entry — why refused (the page / target / value on disk that
contradicts it); cache: evicted <slug> | not cached | n/a (scoped)>, ...]`, a **list in both
modes, `[]` when nothing was refused**. `full-scale.md:21`'s refused-finding eviction gains the
pointer *"record the refusal in `false_positives_refused:`"* (F4) — the response route D3/A13 ruled
(refuse → evict → the next sweep re-derives) is unchanged; it now has the report home the roadmap's
A13 amendment assumed. Not per-file (entries name a slot and a finding, not a walked file), so
membership does not apply.

### 7. Grounding corrections at brief time — every cite re-derived against `171feb8` (build-4 BUILT)

Scope unchanged. `report.md` moved by **+2 lines** for everything below the fence's first fourteen
lines: build-3's `stub_discovery:` at `:15` and build-4's `scanner_return_rejected:` at `:16`. So
A15-8's ~~`report.md:32`~~ (`para_missing_attestation`) → **`:34`**; ~~`:72`~~ / ~~`:73`~~
(`fixes_applied` / `backlog_filed`) → **`:74` / `:75`**; A16's ~~`report.md:9-79`~~ (the fence) →
**`:9-81`**; D2/A14's ~~`:78`/`:89`~~ (`lint_cache:` and the reason list) → **`:80` / `:91`**;
~~`:44`~~ (`governance_memory:`) → **`:46`**. A15-8's ~~`vlt-lint-full.js:812-814`~~ (the structural
slot the SKILL fills) → **`:1039-1041`** — unchanged in substance, **not edited by this build** (the
workflow's page set stays `{wiki}`; build-5 is independent of the workflow, as the foot recorded).
**HOLD:** `vault-operating-contract.md:330` (the persist mandate — *"in the format that verb
declares"*), `SKILL.md:74` (Step 6's persist sentence), `report.md:3` (both the no-dependency clause
and the release-gate claim A20 retires — present verbatim), `checks.md:17` / `:19` / `:20`,
`full-scale.md:7` / `:19` / `:20` / `:21`, `write-verification.md:44` (the attestation pair).
**Grounding additions:** (i) the A15-7 manifest re-verified strict (`yaml.safe_load`) on the live
archive at brief time: **9 reports, 1 fails — the same `2026-08-24-1700`, line 102 column 59**; the
three post-filing reports parse. (ii) The 2026-08-30 render also lacked **`opportunities:`** (the
filing lists thirteen top-level keys and it is not among them) — a fourth dropped key, same
instance class as (b)/(c). (iii) The newest field report carries **four further rollup-form
entries** beyond instance (a): two in `para_type_unknown` (a 9-file and a 4-file rollup), one in
`para_author_unknown` (*"same 4 no-frontmatter files as … above"*), and a prose sentence in
`para_writer_unauthorized` standing where `[]` belongs — disposition 3's membership check fails all
four; the *"same N files as … above"* form is preserved as a fixture case. (iv) `module.yaml:88`'s
`uv` row names *"vlt-lint's findings-cache script"* — build-4 added `lint-page-facts.py` without
widening it; a list that claims completeness drifted once already, so F6 re-points it at the
directory. (v) `lint-cache.py` (the `uv run` precedent A16 names) declares **no** inline
dependency — `requires-python` only — so this build's script is the module's first with a real one;
the `uv`-absent posture in disposition 4 exists because of that.

### 8. Interim posture (R1) — not applicable

Every rule this build states ships with its mechanism in the same commit: the grammar with the
parser, the per-file clause with the walker, the failure route with its artifact. The four declared
count-leg exclusions are not rules shipped ahead of a mechanism — the promise names membership (*one
entry per file*), which ships whole; a count leg is an extension named for the day its source is
data.

### 9. Retirement (P-15; obsolescence beat A20) — SUBSTANTIVE

- **`report.md:3` — *"the module's release gate parses real persisted reports before the tag"*:
  RETIRED, re-pointed.** No such `package-lint` group exists (grep `lint_reports` in
  `tools/package-lint.py` → the C8 map rows only) and none can — the vault's archive is not a
  factory surface. The sentence becomes: *"the persist gate parses the block back before any file
  lands under `{lint_reports}` (`scripts/lint-report-check.py`, `vlt-lint` Step 6)"*. The clause's
  *why* (em-dashes, colons inside values, arrows) stays — it is the A15-7 fragment foretold.
- **A15-7 direction 3 — *declare the archive best-effort* — DIES** as an option; nothing in the
  shipped surface may describe `{lint_reports}` as best-effort after this build.
- **`report.md:66` — *"no line when it is empty"* (`spec_candidate_standing`): RETIRED** — always
  rendered, denominated zero (disposition 2).
- **`report.md:78` — the scoped literal `not instrumented (inline run)` for `cost_accounting`:
  RETIRED** in favour of the typed empty form (disposition 2). `scanner_return_rejected:`'s literal
  at `:16` is a scalar and **survives**.
- **Honoured, not superseded:** Cycle 14 build-4 §3 (no serializer); `full-scale.md:19` step 4's
  *"do not persist a findings report"* on a refused sweep (this build's route is downstream of it);
  `report.md:91`'s statement that the wrong-type cold reason lives only on a failed-run record.
- **Population statements that do not move:** `checks.md:19` (the `para_*` population — now the
  walker's spec, cited by pointer), `checks.md:17`'s carve-out (the walker's predicate, cited by
  pointer), `full-scale.md:7`'s `{wiki}` carve-out.

## Boundary with builds 6 and 7 — stated so their briefers inherit it

- **Build-6** moves the recognized `type:` set (`extraction.md`, A6). Build-5's `para_type_unknown`
  check is **semantics-free** (membership only, disposition 3) and does not care what the set is;
  the walker emits `type` as a fact. Nothing to merge.
- **Build-7** (A8) adds *one denominated line* to `report.md` for the `open`-posture PASS
  population, and edits `checks.md:20`. **Merge order on `report.md` is now 3 → 4 → 5 → 7.**
  Build-7's line must obey the grammar (a scalar `<…>` placeholder, or a `[<page…` / `[<para-file:`
  list if it is per-file — in which case it is membership-checked automatically) and **build-7
  re-derives `fixtures/build-5-expected-schema.json`** and re-runs the build-5 harness; the schema
  floor in the script (disposition 1) is a floor, so an added key does not trip it. Build-5 touches
  `checks.md:17` and `:19` (pointers) and not `:20`.

## F-sites

### F1 — `skills/vlt-lint/references/report.md` — the grammar paragraph, the promoted slot, the population line, two always-render forms, one marker, the re-pointed claim

**Current state.** `:3` the intro: the JSON-subset no-dependency clause and the release-gate claim,
verbatim: *"**Keep it parsing whole in both homes** — a requirement with an enforcement point, not
an assertion: the module's release gate parses real persisted reports before the tag, because …"*.
`:9-81` the fence. `:34` `para_missing_attestation`; `:37` `attestation_census` with its *"full mode
— …"* comment; `:38-41` the other four `para_*` slots; `:46` `governance_memory:`; `:66`
`spec_candidate_standing` with *"no line when it is empty"*; `:76` `rulings_recorded:`; `:78`
`cost_accounting` with the scoped literal; `:80` `lint_cache:`; `:83-95` the reporting paragraphs.

**The change.**

1. `:3` — replace the release-gate clause per §9 (the persist gate, by script and step); re-point the
   no-dependency sentence: *"… which is why the block is written in the JSON subset of YAML — and
   why the persist gate can always run: `.yaml` validates under `uv run` with the script's inline
   `pyyaml`, `.json` under bare `python3` (disposition 4)."*
2. **Insert the grammar paragraph** between `:7` and the fence (`:9`), headed in bold *"The fence is
   the shape's single home, read by machine"* — disposition 1's five rules, in that order, plus the
   two sentences: *"`scripts/lint-report-check.py` parses this fence at Step 6 and validates the
   rendered block against it — presence, type, and for `[<para-file:` slots membership and count over
   the walk `scripts/lint-para-facts.py` performs. Nothing else states the key set; a line added here
   is a line validated there."*
3. `:34`-`:41` region — insert `para_scan:` (disposition 3's exact placeholder text) directly
   **before** `para_status_unknown:` (`:38`), so the five slots and their line sit together, and a
   trailing comment: `# the para_* denominator — P and M from the walker, pasted from its --line
   output verbatim; Step 6 re-walks and compares this string`.
4. `:37` `attestation_census` — reword the trailing comment to open `# full mode only — the
   denominated wiki-wide census …` (the marker; the rest of the comment unchanged).
5. `:66` `spec_candidate_standing` — replace *"renders (denominated zero included) whenever
   `_agent/handoffs/` is non-empty; no line when it is empty"* with *"always rendered; the
   denominated zero reads `0 standing candidate(s) — _agent/handoffs/ empty`"*.
6. After `:76` `rulings_recorded:` — insert `false_positives_refused:` (disposition 6's placeholder)
   with the comment `# both modes, [] when nothing was refused — the refused-finding route
   (full-scale.md step 5) records here; cache: names the eviction or its absence`.
7. `:78` `cost_accounting` — the comment's scoped clause becomes *"inline/scoped runs render the typed
   empty form `{phases: [], not_instrumented: "inline run"}` — never a scalar where the shape says
   map"*.
8. A new reporting paragraph after `:95` (**Stub-discovery reporting**): **"Persist-gate
   reporting."** — one paragraph: what `check` verifies, the two-attempt route by pointer to
   `SKILL.md` Step 6 (single home for the ritual — not restated here), the `para_scan:` read-back,
   and the R3 line: *legal response to a shape failure: re-render from the same Step-5 facts; a
   second failure persists the failed-run record and resets no counter.*

**Why.** A15-8 (the shape stated in one file and enforced in none — this file becomes the file the
enforcer reads), A16 (1)/(2)/(3), A20 (the retirement), disposition 2 (the two forms that would
otherwise be passing-violating states).

### F2 — `skills/vlt-lint/scripts/lint-para-facts.py` — NEW: the population instrument (disposition 3)

**Current state.** No PARA-population instrument exists anywhere in `skills/`; the SKILL walks the
population in prose (`full-scale.md:7`, `:20`; `SKILL.md:47` Step 1). `lint-page-facts.py` is the
shape precedent (PEP 723, `requires-python = ">=3.9"`, no deps, `--pages`/`--out`, facts never
verdicts, stdlib only).

**The change.** Ship the script per disposition 3: `--dir` (repeat), `--exclude` (repeat), `--root
{project-root}` (for relative paths in the output), `--out <path|->`, and `--line` (print the exact
`para_scan:` value and nothing else). Output: `{instrument: "scripts/lint-para-facts.py", population:
[<relpath>, ...], files: {<relpath>: {has_frontmatter, type, author, status, created, attested,
basename}}, missing_attestation: [<relpath>, ...], counts: {P, M}}`. Frontmatter is read the way
`lint-page-facts.py` reads it (`frontmatter_lines` — the leading `---` block, line-parsed, no YAML
library: the walker must run without `uv`, disposition 4); a file whose block is absent is a member
with `has_frontmatter: false` (it is in the population — `checks.md:19` — and is what the field's
*"no-frontmatter files"* rollups were about). Expose `walk(dirs, excludes, root)` as an importable
function — `lint-report-check.py` imports it by sibling path. The operational-record predicate and
the attestation pair are implemented **here, once**, with `checks.md:17` and `write-verification.md:44`
cited in the docstring as the rule text they implement.

**Why.** A16 (3), D2 (iv) — the denominator is produced by an instrument independent of the value's
producer; the promise's *one entry per file* needs a population that is not the render's.

### F3 — `skills/vlt-lint/SKILL.md` — Step 6 becomes the ritual; the failed-run shape-predicate is router-visible

**Current state.** `:66-74` Step 6: the log line, then *"Also **persist the report** (both modes):
write the Step-5 report block to `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` … **or** to
`…-lint.json` … content-verbatim …"*. `:76` the B10-12 failed-run paragraph (a refused sweep persists
`…-lint-failed.yaml` and writes no log line; mechanics at `full-scale.md`). `:1-4` frontmatter pins
(untouched). `:47` Step 1 reads PARA files.

**The change.**

1. Step 6 (`:68-74`) is restructured so the **persist precedes the log line** and reads as
   disposition 4's three moves (scratch → `check` → `mv`), the `uv`/`python3` route, and *"the log
   line writes only after `status: ok`"*. Content-verbatim, append-only, the `.md` legacy sentence,
   the no-session-note sentence and the cache sentence stay as they are.
2. A new paragraph after `:76`: **"Failed persist gate (build-5):"** — disposition 5 in full (the
   one re-render; the failed-run record with `reason: shape — …`, `unvalidated_report: |` and
   `next: re-render from the returned workflow object, not re-sweep`; `--kind failed`; no log line;
   the in-session block the owner's copy). This is the single home of the shape-failure record's
   field list because scoped runs never read `full-scale.md` (disposition 5).
3. `:47` Step 1 — one clause: *"… (the inputs the `para_*` checks judge; the population itself is
   walked by `scripts/lint-para-facts.py` — run it here in both modes and keep its `--line` output for
   Step 5's `para_scan:`)"*.

**Why.** A15-7 direction 1 (*the reader exists; run it before the write*); A16 (5); B10-12's
counter rule extended to the second failure predicate.

### F4 — `skills/vlt-lint/references/full-scale.md` — three pointers (steps 1, 4, 5)

**Current state.** `:7` step 1 names the SKILL's PARA page set and runs `lint-page-facts.py`. `:19`
step 4 defines the failed-run record (fields listed; two predicates — shortfall, wrong-typed slot).
`:20` step 5: *"the PARA scan … stay yours; fill those report slots from your own pass."* `:21` the
refused-finding eviction with no report home.

**The change.** `:7` — after the `lint-page-facts.py` sentence: *"The `para_*` population is walked
by `scripts/lint-para-facts.py` (Step 1, both modes — its spec is `checks.md`'s population
statement); the SKILL never derives P or M itself."* `:19` — one sentence at the end: *"A third
predicate, the persist gate's shape failure, writes the same record from Step 6 — its extra field
and its `reason: shape — …` vocabulary are stated there, once."* `:20` — after *"fill those report
slots from your own pass"*: *"— one entry per walked file, never a rollup; the walk is
`lint-para-facts.py`'s and Step 6 checks each entry against it."* `:21` — after the evict sentence:
*"Record each refusal in the report's `false_positives_refused:` slot (`report.md`) — the finding,
why the bytes contradict it, and the eviction."*

**Why.** Single-home discipline: the population, the record and the slot each gain pointers at the
sites that consume them, and mechanics stay where they are stated.

### F5 — `skills/vlt-lint/references/checks.md:17`, `:19` — two pointers

**Current state.** `:17` states the `para_missing_attestation` rule and the operational-record
carve-out in prose. `:19` states the `para_*` population in prose.

**The change.** `:17` — after the carve-out's closing parenthesis: *"— the predicate
`scripts/lint-para-facts.py` implements for the report's `para_scan:` M and Step 6's count check."*
`:19` — after *"never PARA artifacts, container members, or `para_*` candidates"*: *"— the walk
`scripts/lint-para-facts.py` performs; every `para_*` entry names one member of it (Step 6)."*
`:20` is **not touched** (build-7's).

**Why.** The rule text stays here; the instrument is named where the rule is, so the next reader
finds the executable from the rule and not the reverse.

### F6 — `skills/vlt-setup/assets/module.yaml:87-89` — the `uv` row's posture

**Current state.** `needed_by: "vlt-setup / vlt-upgrade merge + manifest scripts and vlt-lint's
findings-cache script (PEP 723 inline deps)"`; `absent:` names only the cache's cold-run
degradation.

**The change.** `needed_by` → *"… and vlt-lint's `scripts/` (findings cache, page facts, PARA
walk, persist gate — PEP 723 inline deps)"*; `absent` gains: *"; the vlt-lint persist gate then runs
under bare `python3` over the `.json` report home — the `.yaml` home needs `uv` for `pyyaml`"*.

**Why.** Grounding addition (iv) — the row is an enumeration that drifted; disposition 4's route
must be visible where the tool requirement is declared. No version bump (a metadata prose edit).

### F7 — `skills/vlt-lint/scripts/lint-report-check.py` — NEW: the gate (dispositions 1, 2, 3, 4, 5)

**The change.** PEP 723 header with `dependencies = ["pyyaml"]`, `requires-python = ">=3.9"`;
lazy `import yaml` inside the `.yaml` branch; the fence parser (disposition 1's grammar, the
schema floor); `check --report <path> --mode full|scoped --dir … --exclude … [--root …] [--schema
…] [--kind report|failed]`; the JSON verdict on stdout, exit 0/1/2 (disposition 4's vocabulary,
which is the R3 single home for the class); membership + duplicate + count + `para_scan` equality
via `lint_para_facts.walk` (import by sibling path, never a copied function). The docstring names
A15-7 / A15-8 / E1 / A16 and Cycle 14 build-4 §3 (*this script writes nothing — it is the reader
that ruling said the enforcement point would be*).

### F8 — `factory/cycles/15-nothing-reads-it-back/fixtures/` — the harness, the PARA tree, two oracles, one conforming report

- `build-5-para/` — a small PARA tree: `projects/<c>/charter.md` (with `writers:`), a
  `record.md`, three agent-authored knowledge files (one attested, two not), one `type: charter`
  file outside a container (the carve-out's second half), one `author: human` file, one file with
  no frontmatter, one `hybrid` unattested, and `resources/wiki/<page>.md` that the `--exclude` must
  carve out. Every path generic; no vault content (the F8 scrub rule from build-3/4 applies).
- `build-5-expected-para-facts.json` — the hand-written oracle for the walk (P, M, per-file facts),
  written **before** the script is run against it (build-4's order).
- `build-5-expected-schema.json` — the hand-written oracle for the fence parse at this build's
  commit: every key path, its type, the per-file flag, the full-mode-only flag.
- `build-5-report-ok.yaml` — a full-mode report over `build-5-para/` that passes every check.
  **Authored, and said so:** it is built from the archive's real structure (the nine reports' key
  order and forms, read at brief time) with the fixture's paths; it is the shape of the fix's
  success, so the harness never grades on it alone — every specimen below is a **mutation** of it.
- `build-5-shape-harness.py` (PEP 723, `pyyaml`) — runs the cases in check (1)–(5) and prints a
  table; proven failable by mutation (there is no pre-build script to run it against — the failable
  proof is that each planted defect flips exactly its own row, and that the mutated-fence cases move
  the verdict).

## Registration

**None.** No new skill (both scripts live inside `skills/vlt-lint/scripts/`, a tree the manifest
walks whole — `verify-skill-manifest.py:14`); no `module-help.csv` row; no workflow. **No convention
`version:` moves** — `report.md`, `full-scale.md`, `checks.md` and `SKILL.md` are skill files, and
the two conventions this build reads (`write-verification.md:44`, `extraction.md` by reference) are
not edited; `vlt-lint/SKILL.md:4`'s pins and `vlt-lint-full.js:11`'s `// depends_on:` header are
untouched. **Costs priced although no bump is owed:** package-lint **C6** not engaged (the operating
contract is cited at `:330` and `:352`, never edited — no rule-card re-derivation); **E4** not
engaged (no new `package-lint` check — the gate is a `vlt-lint` script, not a release-gate group,
which is the retirement in §9); **E5** not engaged (the workflow is untouched). `module.yaml` F6 is
a prose edit to `machine_tools`, not a version string.

## Out of scope (dispositioned)

- **The `type:` distribution of `para_missing_attestation` entries** — OUT by E1; mandated nowhere;
  the check that wanted it (Cycle 14 build-3 (7)) is DISCHARGED with a caveat on record.
- **Count-equals for `para_status_unknown` / `para_type_unknown` / `para_author_unknown` /
  `para_writer_unauthorized`** — declared membership-only with the site that blocks each
  (disposition 3). **Owed at handoff:** one `candidate` filing — *the `para_type_unknown` count leg
  becomes a one-table extension of `lint-para-facts.py` once build-6's recognized set has a
  machine-readable home* — bound to build-6's ship.
- **Membership for the wiki per-page slots** (`[<page…` lists: `orphans`, `unattested_write`,
  `thin_pages`, …) against the workflow's `pages` list — real, narrower, and the workflow already
  renders those from its own `scans` (a rollup there is structurally impossible on the full-mode
  path; scoped runs render them by hand). Not this build; a `candidate` if the scoped path ever
  shows a rollup.
- **Inline-map children** (`attestation_census`'s four counts, `cost_accounting`'s `phases`) — type
  `map` only; their internals are the workflow's verbatim return and are not re-validated.
- **`.md` legacy reports and every report already in the archive** — never validated, never
  converted (`SKILL.md:74`'s standing sentence). The A15-7 failing report stays as it is — the
  owner's record.
- **The workflow (`vlt-lint-full.js`)** — untouched; `:1039-1041` keeps returning the empty
  structural slot; build-5 is independent of it.
- **A `package-lint` group over persisted reports** — dies with the claim (§9); the vault archive is
  not a factory surface.
- **`para_type_unknown`'s treatment of no-frontmatter files** (the field lists them there; `:19`'s
  rule says *"carrying a `type:` outside the set"*) — a check-semantics question for build-6's
  domain; membership merely forces the honest per-file form either way.
- **The `human|agent|hybrid` closure** (Cycle 14 carry 6) — the next `supersession` candidate,
  filed through the rail build-1 completed; not hardened here (disposition 3).

## Verification (unit, at rest — lifecycle step 5)

1. **The walk against its oracle** — `uv run --quiet skills/vlt-lint/scripts/lint-para-facts.py
   --dir fixtures/build-5-para/projects --dir fixtures/build-5-para/areas --dir
   fixtures/build-5-para/resources --exclude fixtures/build-5-para/resources/wiki --root
   fixtures/build-5-para --out -` deep-equals `build-5-expected-para-facts.json` (diff EMPTY); also
   under bare `python3` (no `uv`) — identical output.
2. **The fence against its oracle** — the script's parse of the shipped `report.md` deep-equals
   `build-5-expected-schema.json`; the top-level key count is recorded in the BUILT status and set
   as the schema floor.
3. **The harness** — `uv run --quiet fixtures/build-5-shape-harness.py` green on every row of
   checks (1)–(5); each planted defect flips exactly its own row (the failable proof).
4. **The live archive, read-only, counts only** — run `check --mode full` over every `-lint.yaml`
   in `{field-vault}`'s `{lint_reports}` (the machine-local path lives in `CLAUDE.local.md`; **no
   path, slug or entry text reaches the BUILT record — counts and reason classes only**): expect
   parse FAIL on exactly one, and a shape FAIL on every one of the nine (missing `para_scan:` and
   `false_positives_refused:` at minimum; the rollups on the newest). This is A15-7's manifest
   re-run by the shipped instrument, and the strongest at-rest corroboration that the gate is not
   vacuous.
5. **Greps** — `release gate parses` under `skills/` → 0; `no line when it is empty` → 0;
   `not instrumented (inline run)` → only `report.md:16` (the scalar) and the `cost_accounting`
   comment's quoted form; `false_positives_refused` → `report.md` + `full-scale.md` (2 sites);
   `lint-para-facts.py` → `report.md`, `full-scale.md`, `checks.md`, `SKILL.md`, `module.yaml`
   (5 files, 6+ sites); `unvalidated_report` → `SKILL.md` + the gate script (2 sites).
6. **Handshake** — `package-lint` **Group E** (E1/E2/E3) PASS; `git diff 171feb8 -- skills/` shows
   0 changed lines carrying `@[0-9]` pins. Not a hand-written grep.
7. **Packaging lint** — `uv run tools/package-lint.py` A/B/C/E PASS (D rides build-7).
8. **Scrub** — no personal / vault-local content in any changed shipped file or fixture; fixture
   paths generic (`projects/<c>/…`), the rollup fixture text carries only the module's own words.
9. **`.decision-log.md`** — none in the working tree at commit.
10. **`uv`-absent route** — `python3 skills/vlt-lint/scripts/lint-report-check.py check --report
    <a .json render of build-5-report-ok> …` → `ok` with no `yaml` import attempted (assert by
    `python3 -X importtime` or a `sys.modules` probe in the harness).

**R2 (fixture extension)** — not applicable: no `package-lint` check is added or changed.
**R3 (legal response)** — substantive: the shape-failure class's one-line response homes at the
gate's own site (`report.md` §Persist-gate reporting, F1 item 8) and the record's `next:` line.
**R4 (enumeration widening)** — the two new scripts sit inside a tree the manifest walks whole
(`verify-skill-manifest.py:14`) — no enumeration to widen; `module.yaml:88`'s `needed_by` **is**
widened (F6) because it enumerates by role; `fixtures/` is un-enumerated — declared exclusion (the
build-4 precedent). **Handshake bipartite re-check** — Group E (item 6).

## Release

Not the release build — no version bump; the two version strings and the `--expect-version 0.18.0`
gate ride build-7. The v0.18.0 CHANGELOG entry collects this brief's `title:`; the cold-run statement
(build-2 §Release) is unaffected by this build (the scan surface does not move — Verification 6).

## Acceptance (live — appended to the roadmap ledger)

**Seven checks — six `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 4/9`
(observed: A15-7's six-report manifest with its line-102 fragment, A15-8's three instances (a), (b),
(c); preserved, reaching this brief as fixture mutations: the fragment verbatim
(`research_zone: 145 notes scanned; 24 carry revisit_after:` unquoted), the 27-file rollup string
verbatim, the absent `fixes_applied:`, the absent `backlog_filed:`; not preserved: the five parsing
reports and the failing report beyond its fragment — vault content, read at brief time for counts
only. Observed at brief time and preserved outside the figure: the *"same N no-frontmatter files as …
above"* rollup form and the prose-where-`[]`-belongs form.)

**(1) `[ship-verifiable]` — at rest — GATES.** *Property: every file persisted as `-lint.yaml` /
`-lint.json` under `{lint_reports}` loads under a strict parser.* **Instrument:**
`fixtures/build-5-shape-harness.py` over `build-5-report-ok.yaml`: (a) the A15-7 fragment planted
unquoted at `research_zone:` → `parse:` failure, exit 1; (b) the same line double-quoted → passes
parse; (c) a two-document stream → `parse:`; (d) the `.json` render of the ok report → `ok` under
bare `python3` with no `yaml` import (Verification 10). **Adversary:** *the SKILL validates one file
and persists another (re-authors after the check, or writes the in-session block by hand).* Reachable
on the shipped surface — the ritual is prose. **Widened:** check (6) grades the first persisted
post-release report with the same script, so a bypass shows as a failing archived file; and Step 6
mandates `mv` of the validated path, not a second write (F3).

**(2) `[ship-verifiable]` — at rest — GATES.** *Property: the key / type / per-file set the gate
enforces is `report.md`'s fence and nothing else.* **Instrument:** the harness: (a) the shipped
fence's parse deep-equals the hand-written `build-5-expected-schema.json`; (b) a mutated fence copy
with `fixes_applied:` removed, passed via `--schema` → the (b)-mutation report (no `fixes_applied:`)
now passes; (c) a mutated fence with a new key `owner_notes: [<…>, ...]` added → the ok report now
fails `key missing: owner_notes`; (d) a fence line that matches no grammar rule → exit 2
`schema_unreadable`; (e) a fence truncated below the floor → exit 2. **Adversary:** *the script
carries a hard-coded key list and consults the fence only for show.* **Widened** by (b) and (c) —
the verdict must move with the fence in both directions; a hidden list would hold (c) green.

**(3) `[ship-verifiable]` — at rest — GATES.** *Property: a report that loads carries every
mandated key in its mandated type, and extra keys never fail it.* **Instrument:** the harness:
(a) `fixes_applied:` deleted (A15-8 (b)) → `key missing: fixes_applied`; (b) `backlog_filed:`
deleted ((c)) → `key missing: backlog_filed`; (c) `opportunities:` deleted (grounding addition (ii))
→ `key missing: opportunities`; (d) `fixes_applied: "5 fixes applied"` → `wrong type … (got scalar,
expected list)`; (e) `cost_accounting: not instrumented (inline run)` under `mode: scoped` → wrong
type (the retired literal); (f) `spec_candidate_standing` absent → key missing (the retired no-line
rule); (g) `attestation_census` absent under `mode: scoped` → passes; absent under `mode: full` →
key missing; (h) `backlog_filed:` with no value (`null`) → key missing; (i) three extra keys at two
depths → `ok` with `extra_keys` listing them. **Adversary:** *a list slot carrying one prose entry
(`["NONE — …"]`) passes as a list.* True by design for non-per-file slots (disposition 2) — the
property named is presence + type; **no passing-violating state found** for that property; the
per-file property is check (4)'s.

**(4) `[ship-verifiable]` — at rest — GATES.** *Property: every per-file slot's entries each name
one member of an independently walked population, no file twice, and — full mode,
`para_missing_attestation` — exactly as many entries as the walk finds.* **Instrument:** the harness
over `build-5-para/`: (a) the 27-file rollup string (A15-8 (a), verbatim) as the sole entry → `not a
member` **and** `count: rendered 1, walk finds 3`; (b) the *"same 2 no-frontmatter files as
para_type_unknown above"* form in `para_author_unknown` → `not a member`; (c) a prose sentence in
`para_writer_unauthorized` where `[]` belongs → `not a member`; (d) the correct three entries minus
one → `count: rendered 2, walk finds 3`; (e) three entries, one naming a path outside the walk (the
carved-out `resources/wiki/<page>.md`) → `not a member`; (f) the same file twice → `duplicate`;
(g) the exact three, each `<relpath>: <text>` → `ok`; (h) `mode: scoped` with one well-formed entry
→ `ok` (membership only); (i) `para_scan:` edited by one character → `para_scan: rendered line does
not match the walk`; (j) the walk itself: `record.md`, the out-of-container `type: charter` file,
the attested file and the human file are **not** in M; the two unattested agent/hybrid files and —
control — nothing from `resources/wiki/` are. **Adversary:** *the population is handed to the
validator by the agent that rendered the slot (a facts file it wrote).* **Widened by construction** —
`check` takes directories, imports the walker and walks itself; no facts file is accepted. Second
adversary: *the agent points `--dir` at a directory containing exactly the files it listed.* Then P
shrinks, the count leg still compares against that walk, and `para_scan:` — pasted at Step 5 from
the real walk — no longer matches (i): recorded, not asserted beyond (i).

**(5) `[ship-verifiable]` — at rest — GATES.** *Property: a failed gate leaves the owner a readable
failed-run record and never a `-lint.yaml` that is not one.* **Instrument:** the harness drives the
Step-6 ritual over a scratch dir standing in for `{lint_reports}`: (a) a report failing (4a) →
attempt 1 prints `failed` and **no file** exists under the dir; (b) the attempt-2 record written by
the harness as the SKILL would (`status: failed`, `reason: shape — not a member: …`, `next: …`,
`unvalidated_report: |` embedding the failing block — the A15-7 fragment inside it, unquoted) →
`check --kind failed` → `ok`, the file parses whole, and the embedded scalar round-trips
byte-identical; (c) no `-lint.yaml` for that stamp; (d) the log-line rule is prose — recorded as the
field leg of (6). **Adversary:** *the SKILL persists the failed block as `-lint.yaml` "to be safe".*
Reachable; the same bypass as (1)'s — **widened** by (6)'s archived-file grading, which fails on it.

**(6) `[ship-verifiable]` — bounded to the first full `vlt-lint --full` sweep on `{field-vault}`
after the v0.18.0 upgrade — GATES.** *Property: the first report written under the gate is what the
promise says — readable, whole, per-file — or its failure artifact is.* **Instrument:** the
discharger runs the shipped `check --mode full` over that sweep's persisted file: it is a
`-lint.yaml`/`.json` that returns `ok` (every mandated key including `para_scan:` and
`false_positives_refused:`; `para_missing_attestation` per-file, its count equal to the walk's M —
27 or the then-current number, recorded), **or** it is a `-lint-failed.yaml` with `reason: shape —
…` and no `-lint.yaml` for that stamp, and `{log}` carries no lint line for it. **This is A15-7's own
bound** — the owner's 2026-08-27 ruling that the re-grade belongs to acceptance-discharge against
reports written *under* the mandate. Performer: the owner; vault `{field-vault}` (readable).
**Discharges `factory/inbox/2026-08-27-153000` (A15-7) and `2026-08-31-104500` (A15-8)** — Stage 5
may move both once (1)–(6) are green. **Adversary:** *the gate passed because the SKILL trimmed the
population to make the count fit.* **Widened:** the discharger re-walks with `lint-para-facts.py`
over the vault's real three dirs and compares P and M with the report's `para_scan:` line.

**(7) `[field-contingent]`.** *The intermittence is gone: two consecutive sweeps produce the same
key set.* Event: the **second** full sweep after the v0.18.0 upgrade; performer: the owner on
`{field-vault}`; grade: `check` returns `ok` on both, and the two reports' top-level key sets are
equal. Unbounded; watch register if unfired.
