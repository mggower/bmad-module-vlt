---
title: 'Build #1 — reduce-side: a structured frontmatter verdict and an entity-decoded category seam (the guard shipped last release was defeated by a scanner that cited the rule it applied)'
status: >
  BUILT 2026-08-27 — all F-sites landed; 6 of 8 acceptance checks gradeable at rest, **6/6 PASS**;
  (6) and (7) are bound to the first live `{field-vault}` sweep after release 1 and are UNFILLED by
  construction. Version bump NOT taken — it belongs to the release step (`vlt-release`), not the
  build. Branch `cycle14-v0.16.2`.

  **Sites changed** — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (724 → 767 lines):
  `:148` `required:` `'frontmatter_valid'` → `'frontmatter_defect'`; `:159` the enum property
  replaces `frontmatter_valid`; `:163-164` `frontmatter_defect_fields` + `frontmatter_defect_detail`
  replace `frontmatter_issue`; `:216` prompt clause renamed off the retired field; `:218` the new
  scanner-guidance paragraph (zero E6 cost, per D1 documentation not enforcement); `:552-555` the
  kept historical record, two dead property references renamed (deviation 1); `:561-577` the retired
  safety comment replaced by the new invariant stated for the structured return; `:579-585` the
  page-schema-vs-return-schema comment extended with the sets' new live role; `:596-608`
  `whollyWithin` replaces `KNOWN_FRONTMATTER` / `KNOWN_FRONTMATTER_BY_LENGTH` / `normalizeClaim` /
  `claimWords` / `CLAIM_FILLER` / `parseClaim` / `fieldsNamed`; `:615-616`
  `attestationOnlyComplaint` and `:622-623` `inventedRequirement` rewritten to the structured
  record, names kept; `:625` `refusedFrontmatterClaim` kept, input changed; `:626-637`
  `frontmatterDefectText`, the finding line rendered from structure (deviation 2); `:650-666`
  `HTML_ENTITIES` + `decodeEntities` + `h2set` built from decoded headings; `:686-701` the `:664`
  guard retired with its reason, cost, dissent and R1 interim posture on record; `:705-712`
  `category_no_match` decoded on both sides, strictness comment extended; `:740-745`
  `malformed_frontmatter` filters the structured verdict.
  `skills/vlt-lint/references/checks.md`: `:14` the entity-decoded still-exact category clause;
  `:15` the exclusions restated as set containments, the conjunction/residue prose and the
  over-reporting *guarantee* retired, the `unclassified`-always-reports escape stated, legal
  response unchanged (R3).
  **New factory record:** `factory/cycles/14-no-enforcement-point/malformed-frontmatter-specimens.md`
  (the Q8/E4 specimen set — half 1 filled at rest, half 2 bound to the live sweep).
  **KEPT, verified byte-identical to v0.16.1:** `unmarked_supersession`'s description at `:169`
  (was `:168`; +1 from the `:163` split) — `git diff HEAD` returns zero hits on that property.
  **Not touched, as briefed:** the `depends_on:` ack at `:11` (verified unchanged — build-3 owns
  it); `report.md` (F6 — both exclusions survive, sentence still true); `checks.md:17`/`:19`;
  `runKey` / `fresh_scans` / fingerprint composition; every other `verbatim:` marker;
  the args parse-on-intake at `:77`.

  **V4 — E6 budget, measured with package-lint's own `_E6_NODE_EXTRACTOR`, never a source char
  count.** Baseline (v0.16.1 working tree): `PAGE_SCAN` **3598**. After F1: **3688**. Gate 3700 —
  **PASS, 12 chars spare**, exactly the brief's prediction. The named 42-char reserve
  (empty `_detail`'s description +30, `'malformed_block'`→`'malformed'` ~+12) was **not needed and
  not spent**. Other schemas unchanged: `INDEX_SCAN` 823, `CLUSTER_FINDINGS` 1630,
  `PAIR_FINDINGS` 376.

  **V5 — packaging lint.** `uv run tools/package-lint.py` →
  `package-lint: A/B/C/E PASS, D SKIPPED — vlt 0.16.1`. D is SKIPPED because no `--expect-version`
  was passed: the dual version bump and the `--expect-version X.Y.Z` gate are the RELEASE step's,
  not the build's.

  **V6 — handshake bipartite.** Stated rather than left silent: **no convention `version:` moved and
  no `consumers:` list changed**, so nothing is owed beyond Group E in V5, which PASSES. The
  workflow's own `depends_on: ["frontmatter@13", "wiki-supersession@2", "wiki-index@2",
  "write-verification@3"]` is unchanged (`git diff HEAD` on that line is empty) — build-1 enforces
  no new convention rule and drops no convention read.

  **V1 — the guard harness (14/14 PASS).** The shipped workflow source loaded with stubbed
  `agent`/`parallel`/`phase`/`log`/`budget` and `args` delivered as a **JSON string** (the runtime
  contract; the workflow's own parse-on-intake at `:77` is what consumes it). Arrays verbatim:
  - attestation-only (`missing_required` + `['verified_by','verified_at']`) → `malformed_frontmatter: []` — REFUSED
  - the same **with the 2026-08-26 rule-citing text from the filing in `_detail`** → `[]` — STILL REFUSED
  - invented requirement (`missing_required` + `['review_after']`) → `[]` — DROPPED
  - CONTROL genuine break (`['summary']`) → `["p: missing required frontmatter: summary"]`
  - CONTROL compound (`['summary','verified_by']`) → `["p: missing required frontmatter: summary, verified_by"]`
  - CONTROL escape (`unclassified`) → `["p: unclassified frontmatter defect: two YAML delimiters but the body is a JSON object"]` — A35's invariant holds
  - CONTROL `malformed_block` → `["p: frontmatter block absent or unparseable — no frontmatter block at all"]`
  - CONTROL prose smuggled into `_fields` → reports (set containment gives wording no purchase)
  - CONTROL `defect: 'none'` → `[]`
  On the attestation-only case the other three arrays: `unmarked_supersessions: []`;
  `unattested_write: ["p (created 2026-01-01)"]`;
  `attestation_census: {"pages_total":1,"fresh":0,"stale":0,"unattested_pre_adoption":1}` — the
  refused entry loses no fact. CONTROL: a genuine unmarked supersession still reaches the class →
  `["p: the 2024 headcount claim was silently updated with no [!superseded] callout"]`.

  **The harness can fail, demonstrated rather than asserted.** The same rule-citing text run against
  the **v0.16.1** predicate (extracted from `git show HEAD:…`): bare claim →
  `attestationOnlyComplaint` `true` (correctly refused); rule-citing claim → **`false` — DEFEATED**,
  with residue `"validity defect per write verification 3 scope rule attestation reported through
  values above this c…"` and `named: ["verified_by","verified_at"]`. The field failure reproduces
  exactly on the old code and does not on the new. The defeat mechanism is dead.

  **V2 — the entity-decode fixture (8/8 PASS).** `category_no_match` verbatim:
  page-side `Energy &amp; Clean Tech` vs H2 `Energy & Clean Tech` → `[]`;
  **index-side** `Energy &amp; Clean Tech` vs page `Energy & Clean Tech` → `[]` (the fan-out-wide
  half A14-3's filing did not notice); `&#38;` → `[]`; `&#x26;` → `[]`.
  No cascade: `&amp;amp;` decodes **once** to `&amp;` and still differs →
  `["p: category 'Energy &amp; Clean Tech' matches no H2"]`.
  Controls, strictness not softened (D5): different category → `["p: category 'Finance' matches no
  H2"]`; case difference → `["p: category 'energy & clean tech' matches no H2"]`; leading space →
  `["p: category ' Energy & Clean Tech' matches no H2"]`.

  **V3 — retirement + survivor greps.**
  `grep -rn "parseClaim\|fieldsNamed\|KNOWN_FRONTMATTER\|normalizeClaim\|claimWords\|CLAIM_FILLER\|frontmatter_issue\|frontmatter_valid" skills/`
  → **zero hits (exit 1)**, all eight retired symbols including the grounding-addition
  `KNOWN_FRONTMATTER`. Survivors are each referenced from the rewritten predicates, not merely
  defined: `PAGE_REQUIRED_FRONTMATTER` `:587` (def) + **`:608`** (live, in `whollyWithin`);
  `PAGE_OPTIONAL_FRONTMATTER` `:590` (def) + **`:623`** (live); `ATTESTATION_FRONTMATTER` `:594`
  (def) + **`:616`** (live). `node --check` parses.

  **R2 (roundtable) — fixture posture, the split honoured.** V1/V2 are **synthetic unit fixtures for
  the controls** — they exercise only the surfaces this build changes and are declared as such.
  **Acceptance check 2 is graded against the six REAL subjects**, never a fixture: read-only copies
  of the six pages from `{field-vault}`, six real single-agent reader probes running the
  **post-build** `pageScanPrompt` and `PAGE_SCAN` emitted from the shipped source, against the real
  merged conventions (base + the vault's `frontmatter.overlay.md`), then the **shipped** rewritten
  reduce applied to the returns. The vault was never written (copies `chmod a-w`; `git status` in
  the vault clean of any change by this build).

  **R3 — legal response.** Applicable and satisfied: `malformed_frontmatter`'s and
  `category_no_match`'s legal responses are stated at their single home, `checks.md` (`:15`/`:14`),
  and both are unchanged in substance.
  **R4 — enumeration widening.** Not applicable; the specimen set is a factory record outside every
  shipped enumeration and is never copied into a vault by own-the-apply.
  **Scrub.** No personal or vault-local content in any changed shipped file. The six subject slugs
  are referenced by pointer (`factory/cycles/13-trusted-returns/roadmap.md:468-473`) and appear only
  in the factory-side specimen set, never in a shipped file. No `.decision-log.md` anywhere in the
  working tree (`find . -name ".decision-log.md"` → nothing).

  ── ACCEPTANCE, graded at rest ──────────────────────────────────────────────
  **(1) PASS** — the defeat mechanism is gone and the escape reports. V1's 14 assertions above;
  the old-code reproduction proves the instrument can fail.
  **(2) PASS — ⚠ this is the check that RE-GRADES CYCLE 13's ACCEPTANCE CHECK (2), and it is graded
  on the REAL six subjects, not a fixture.** The six post-build returns (verbatim, the frontmatter
  verdict and attestation half):
  - `bistec-encebollado` — `defect:"none"`, `_fields:[]`, `_detail:""`, `category:"Cooking"`, `verified_by:""`
  - `k-curve-career-divergence` — `defect:"none"`, `_fields:[]`, `_detail:""`, `category:"Tech Careers & AI Era"`, `verified_by:""`
  - `kettl` — `defect:"none"`, `_fields:[]`, `_detail:""`, `category:"Japanese Tea"`, `verified_by:""`
  - `llm-wiki-pattern` — `defect:"none"`, `_fields:[]`, `_detail:""`, `category:"Productivity & Learning Systems"`, `verified_by:""`
  - `obsidian-bases` — **`defect:"missing_required"`, `_fields:["review_after"]`**, `_detail:""`, `category:"Productivity & Learning Systems"`, `verified_by:""`
  - `execution-to-judgment-shift` — `defect:"none"`, `_fields:[]`, `_detail:""`, `category:"Tech Careers & AI Era"`, `verified_by:""`
  All six returned `unmarked_supersession: []`. **`obsidian-bases` is the live exercise**: the same
  invented-requirement complaint the 2026-08-25 sweep raised against `ashwagandha` recurred here
  under the new schema, arrived as a *structured* `missing_required` naming exactly `review_after`,
  and disposition 2 dropped it arithmetically. Post-reduce arrays, verbatim, from the shipped
  reduce over the real `{index}` H2 set:
  `malformed_frontmatter: []`; `unmarked_supersessions: []`;
  `unattested_write: ["bistec-encebollado (created 2026-06-26)","k-curve-career-divergence (created
  2026-04-11)","kettl (created 2026-04-22)","llm-wiki-pattern (created 2026-04-12)","obsidian-bases
  (created 2026-07-01)","execution-to-judgment-shift (created 2026-04-11)"]`;
  `attestation_census: {"pages_total":6,"fresh":0,"stale":0,"unattested_pre_adoption":6}`;
  `category_no_match: []`.
  **Zero of the six reach `malformed_frontmatter` or `unmarked_supersessions`, and the attestation
  surface still carries all six.** Cycle 13's check (2) re-grades **PASS**; its closeout gate
  reopens on release 1.
  *Honest limitation recorded (deviation 4):* this probe is six single-agent reads, not the 146-page
  fan-out, and five of six scanners returned `defect:"none"` — so the guards' refusal path was
  exercised live on **one** real subject (`obsidian-bases`), with the attestation-only path
  exercised only synthetically (V1). Check (6)'s live sweep is where the refusal path meets scale.
  **(3) PASS** — retirement landed whole, survivors alive; V3's outputs above; `node --check` parses;
  `:169` (`unmarked_supersession`'s description) byte-identical to v0.16.1. **Deviation 1** narrows
  the "`:550-557` byte-identical" clause; see below.
  **(4) PARTIAL — the at-rest half PASSES, the tag half is the release step's.** `PAGE_SCAN` **3688
  ≤ 3700** by `_E6_NODE_EXTRACTOR`; `uv run tools/package-lint.py` A/B/C/E PASS. The
  `--expect-version X.Y.Z` exit-0 gate with both version strings bumped is **owed at the release
  commit** and is not this build's to discharge.
  **(5) PASS** — V2's 8 arrays above; both sides closed, numeric and hex references decode, all three
  controls still flag.
  **(6) UNFILLED — bound to the first live `{field-vault}` sweep after release 1; performer: the
  owner.** Build-1's obligation was to *produce the measurement*, and it does:
  `factory/cycles/14-no-enforcement-point/malformed-frontmatter-specimens.md`. **Half 1 (pre-change
  baseline) is FILLED at rest** from the persisted `{lint_reports}` archive — 3 sweeps, 28 entries,
  **1 genuine (3.6%)**: 2026-08-24 (145 pages) 18 entries, all attestation-only; 2026-08-25 (146)
  7 entries — 5 attestation-only (and those five are five of Cycle 13's six subjects), 1
  claimed-missing-optional (`ashwagandha: "missing review_after"`), 1 unadjudicated in the archive;
  2026-08-26 (146) 3 entries — `empyrean-series-overview` (optional-field, leaked past the shipped
  guard), `execution-to-judgment-shift` (attestation-only, leaked), `parallel-walk-introduction`
  (`summary` 162 chars — **the one genuine entry across all three sweeps**). Half 2 carries the
  stated bound that can fail (zero attestation-only, zero optional-field, every remainder
  adjudicated genuine one-by-one), and cannot be produced at rest — the post-change schema emits a
  structured verdict no pre-change recorded return can supply, and no wiki corpus ships here.
  **⚠ E4 transfers BOUND, not discharged.** Recorded honestly in the file: the 2026-08-24 sweep did
  not persist its 18 slugs individually, so per-slug fragments are unavailable for that run — a
  resolution limit of the pre-change instrument, not of this build.
  **(7) UNFILLED — bound to the same sweep; performer: the owner.** The `:664` retirement's exposure
  is on record at the site itself (`:686-698`), with the cost stated, the dissent (Victor, Amelia)
  named as carried-not-resolved, and R1's interim posture written where a reader of that class will
  meet it. Baseline for the grade, from the archive: the 2026-08-26 sweep's
  `unmarked_supersessions_fixed: []` — all 3 entries refuted, and entry (1)
  (`costa-rican-village-dog`) was **exactly** an attestation-only complaint that leaked because the
  scanner quoted the rule text. That is the number check (7) must beat.
  **(8) PASS** — `checks.md:15` carries no conjunction/residue mechanism prose and no over-reporting
  *guarantee*; it now describes the structured verdict, states both exclusions as **exact set
  containments**, states that an `unclassified` defect **always reports**, and keeps the legal
  response unchanged. `checks.md:14` states the entity-decoded, still-exact, case-sensitive,
  no-trimming category binding. `grep -rn "Both exclusions are conjunctions" skills/` → **zero
  (exit 1)**; `grep -rn "residue" skills/vlt-lint/references/checks.md` → the class's own residue
  prose is gone. **Deviation 3** records that the check's literal grep is over-broad.

  ── DEVIATIONS ──────────────────────────────────────────────────────────────
  **1. The "keep `:550-557` byte-identical" clause was NOT met literally, and the brief is
  internally contradictory here.** F3 item 5 and check (3) require that block byte-identical;
  check (3) *also* requires the retirement grep return **zero** across `skills/`. The block
  literally contains the words `frontmatter_valid` and `frontmatter_issue` (at v0.16.1 `:552` and
  `:554`), so **both clauses cannot hold**. Ruled in favour of the grep, because the grep is the
  retirement's whole ship-verifiable proof and the clause's *stated purpose* is preserving the
  dissent evidence, which survives intact. Two phrases renamed, nothing else:
  `"used to admit \`frontmatter_valid === false\` and print \`frontmatter_issue\` unread"` →
  `"used to admit the scanner's boolean validity verdict and print its free-text issue slot unread"`;
  `"(see frontmatter_valid)"` → `"(see the frontmatter verdict's description)"`. Every fact is
  untouched — Cycle 12 shipped the prompt-side prohibition, the next two sweeps reported the defect
  unchanged, 20 entries hand-folded 2026-08-24 and 6 on 2026-08-25. Both renamed phrases were also
  **dangling pointers** after this build: they named properties that no longer exist. Trivially
  reversible if the owner prefers the literal reading — at the cost of two grep hits.
  *(The brief's cites for this block are off by one-to-two lines against the working tree: the
  historical record is `:551-559` and the retired safety comment `:561-563`, not `:550-557` and
  `:559-561`. Scope identical; recorded because A29 and the brief have both already had to correct
  drift in this region.)*
  **2. A renderer was added that the brief does not name.** Retiring `frontmatter_issue` removes the
  string the finding line used to echo (`${s.frontmatter_issue || 'invalid'}`), so the line has to be
  *composed* from the structured verdict. `frontmatterDefectText` (`:626-637`) does that. Not a
  ruling re-opened — a consequence of disposition 1 the brief did not price. It is reduce-side, costs
  **zero** against E6, and its output is asserted verbatim by V1's five controls.
  **3. Acceptance check (8)'s literal grep is over-broad and was narrowed.** As written,
  `grep -rn "residue\|Both exclusions are conjunctions" skills/` cannot return zero: three
  **pre-existing, unrelated** uses of the word "residue" live in the shipped tree and are none of
  them this build's subject — `checks.md:52` (the consult-precondition derive-first note),
  `vlt-lint-full.js:243` (the cache record's derive-first branch comment) and
  `governance/_meta/vault-operating-contract.md:350` (the derive-first boundary clause, a governance
  SSoT file this build must not touch). Graded on the check's actual subject instead: the
  conjunction/residue prose in `checks.md:15`, which is gone. Deleting the other three would be a
  scope breach and, at `:350`, an edit to the governance bundle.
  **4. Check (2)'s live exercise is narrower than the numbers suggest.** Recorded above under (2):
  five of six scanners returned `defect:"none"` under the new schema, so only `obsidian-bases`
  exercised a refusal path live. The check's own bound (zero of six reach either class, attestation
  surface still carries them) is met on real subjects and its binding is honoured — but the
  attestation-only refusal is proven synthetically (V1) plus by the old-code defeat reproduction,
  not by a live 2026-08-27 scanner emitting one. Check (6)'s 146-page sweep is the instrument that
  closes that gap, and it gates.
  **5. No version bump taken.** `.claude-plugin/marketplace.json` and
  `skills/vlt-setup/assets/module.yaml` are untouched; package-lint reports `vlt 0.16.1` and Group D
  SKIPPED. The dual bump, the `--expect-version` gate, the tag and the push are the release step's,
  and the brief flags the number itself as the owner's at release time (recommendation: `0.16.2`).
  **6. `factory/CYCLE` untouched.** It still reads `14-no-enforcement-point`. The two-open-cycles
  hazard (roundtable A24) applies to `acceptance-discharge` / `cycle-closeout` runs against Cycle 13,
  neither of which this build ran.

  ── RELEASE NOTE COPY OWED (⚠ do not drop at release) ───────────────────────
  **The first full lint after this release is COLD by construction and is not a cache regression.**
  `scanFingerprint` is `fnv1a(pageScanPrompt(…) + JSON.stringify(PAGE_SCAN))` and reuse is an exact
  key match; this build rewrites **both** halves of `canonicalScan`, so every existing
  `_agent/lint-cache.yaml` record is unreusable and the first post-upgrade sweep scans 100% of pages.
module_code: 'vlt'
created: '2026-08-26'
derives_from:
  - 'factory/inbox/2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md (A14-1 — the residue rule defeated on two independent legs; the refuted safety comment)'
  - 'factory/inbox/2026-08-26-164502-html-escaped-scanner-return-fails-an-exact-comparison.md (A14-3 — the HTML-escaped category return; the symmetric index-side exposure capture added)'
roadmap: 'factory/cycles/14-no-enforcement-point/roadmap.md'
rulings: >
  roadmap §Ideation rulings (2026-08-26): Q1 (structure the claim return, entity-decode the
  category seam on both sides, defer the two faces needing page bytes) as amended by roundtable
  A35 (the enum carries an unclassified escape that REPORTS); Q7 (the refuted safety comment
  retires with the mechanism it documents); Q8 + E4 as amended by A19 (build-1 produces the
  malformed_frontmatter specimen set; the debt transfers bound, not discharged); D1 (structure or
  normalize at the seam — `verbatim` is never an enforcement point); D3 as amended by A17/A17b
  (bounded ⇒ ship-verifiable ⇒ GATES; build the at-rest instrument where one is buildable in
  scope); D5 (both named-to-be-rejected directions stand); §Grouping & order build-1 block incl.
  A2 (`:664`), A20, A21 (the Cycle 13 re-grade), A37 (the retirement list), A38 (`checks.md`),
  and owner ruling A-R1 (retire `:159`, keep `:168`; dissent on record).
risk: 'moderate — no convention version moves and no consumer walk is owed, but the build removes a required `PAGE_SCAN` property, invalidates every existing lint sidecar record, sits 12 chars under a hard release gate, and is the sole repair that reopens Cycle 13''s closeout.'
---

# Build #1 — reduce-side: a structured frontmatter verdict and an entity-decoded category seam

## Intent

Cycle 13 shipped two reduce-side guards so the full-lint reduce would stop believing the page
scanner's `frontmatter_valid` / `frontmatter_issue` claims unread. On the first live full sweep
after the upgrade the defect recurred in the same shape, because **the enforcement point still had
to parse scanner-returned free text in order to decide whether to trust a scanner-returned claim**.
A scanner that cited the rule it was applying defeated the guard's closing conjunction on two
independent legs at once — leftover prose made `claim.residue !== ''`, and the quoted rule named
real `PAGE_REQUIRED_FRONTMATTER` members. Nothing about the pages changed; only the phrasing did.

This build removes the parse rather than tuning it. The frontmatter verdict becomes a **structured
return** — an enum, a bare field-name list, and a detail slot — so the reduce classifies a
machine-shaped value instead of interpreting prose, and the whole residue-rule apparatus that
existed only to read prose retires with it. The same posture is applied to A14-3's second face:
the `category` ↔ H2 comparison is **entity-decoded on both sides at the seam**, because `h2set` is
agent-returned too and a `&amp;` on the index side falsifies every page in that category at once.

Build-1 is **Release 1, cut alone**, because it is the only thing that reopens Cycle 13's closeout
gate (Cycle 13's acceptance check (2) is ship-verifiable, GATES, and is FAILED on this filing's
evidence with no discharge path left).

**⚠ The first full lint after this release is COLD by construction, and that is not a regression.**
`scanFingerprint` is `fnv1a(pageScanPrompt(…) + JSON.stringify(PAGE_SCAN))` (`:232-233`) and reuse
is an exact key match (`runKey`, `:242`; `reusable`, `:244-245`). This build rewrites both halves of
`canonicalScan`, so **every existing `_agent/lint-cache.yaml` record is unreusable and the first
post-upgrade sweep scans 100% of pages.** Say so in the release note; do not let a later reader
grade it as a cache failure. (The cycle knowingly accepts two cold sweeps — roadmap §Next lifecycle
move, roundtable A26.)

**All rejected alternatives in the parent filings are settled — do not re-litigate.** Specifically:
A14-3's candidate 3 (loosen the category comparison) is rejected and the comparison's
case-sensitivity is **not** softened (D5); asking the scanner to try harder at the same free-text
task is rejected (D5, and it is Cycle 13's whole premise). Q1's *restructuring* of what the schema
asks for is a different act from that plea, and the distinction is load-bearing (D5 as sharpened).

## Brief-time dispositions

### 1. The structured return's exact shape — an enum + a bare field list + a detail slot, and it REPLACES `frontmatter_valid`

*Derives from: §Questions deliberately left to brief time → build-1 ("the exact shape of the
structured claim return … and its cost against `PAGE_SCAN`'s size budget"); Q1 ruling 1; roundtable
A1 and A35.*

**Ruled: three properties replace two.** `frontmatter_valid` (`:159`) and `frontmatter_issue`
(`:163`) both retire; `frontmatter_defect`, `frontmatter_defect_fields` and
`frontmatter_defect_detail` take their place, and `required:` at `:148` swaps
`'frontmatter_valid'` for `'frontmatter_defect'`.

```js
frontmatter_defect: { type: 'string', enum: ['none', 'missing_required', 'malformed_block', 'unclassified'],
  description: 'none | missing_required (keys in _fields) | malformed_block (absent/unparseable) | unclassified (_detail)' },
frontmatter_defect_fields: { type: 'array', items: { type: 'string' },
  description: 'bare key names, one per entry; else empty' },
frontmatter_defect_detail: { type: 'string', description: 'the break in words; else empty' },
```

**Why the boolean goes too.** A `'none'` enum member expresses everything `frontmatter_valid`
expressed, and keeping both would leave two returned values that can disagree — a fresh instance of
the shape this cycle is named for. It is also what makes the budget close (below). The disposition
is squarely inside the deferred question ("the exact shape of the structured claim return"); Q1
rules the *kind* of return, not its property count.

**Why an enum + field list rather than a discriminated union.** The reduce's two shipped
dispositions are both *set* tests over named fields — attestation-and-nothing-else, and
optional-and-nothing-else. A field-name array lets those tests be written as exact set arithmetic
against `ATTESTATION_FRONTMATTER` / `PAGE_OPTIONAL_FRONTMATTER` / `PAGE_REQUIRED_FRONTMATTER`, which
is what gives the two surviving constant sets their live code role (disposition 3). A discriminated
union would cost more schema bytes for the same arithmetic, and the budget has none to give.

**The `unclassified` member is mandatory and it REPORTS (A35).** The mechanism being retired is
fail-OPEN: `:603` returns anything unrecognized as residue and the entry reports. A closed enum
would be fail-CLOSED — a scanner meeting a genuine break outside the roster would have to mis-file
it or drop it, inverting the invariant Q7 requires survive the move. So: `unclassified` is an
explicit member with a free-text detail slot, **an `unclassified` verdict is never refused by either
disposition**, and the invariant is *tested* by this build's acceptance rather than asserted
(acceptance check 1's controls). Shipped precedent in the same file: `sources_vs_prose`'s
`no_prose_section` member.

**Scanner guidance goes in the PROMPT, not the schema.** `_e6_schema_size_budget` measures
`JSON.stringify(schema).length` only — `pageScanPrompt` (`:214-216`) is **not** in that measure
(it is in `canonicalScan`, and this build makes the sweep cold anyway). The schema descriptions are
therefore deliberately terse and the fuller instruction — what each enum member means, that
`_fields` carries bare unadorned key names and never prose, that a rule citation belongs in
`_detail` and never in `_fields` — is added to `pageScanPrompt`'s second paragraph at **zero E6
cost**. Per D1 this prompt text is documentation, never the enforcement point; the enforcement is
the enum's range.

### 2. The budget — measured, and it closes at 3688/3700 with 12 chars spare

*Derives from: roundtable A1 (§Questions left to brief time → build-1).*

Re-measured this run with **package-lint's own `_E6_NODE_EXTRACTOR`**, never a source char count:

| state | `JSON.stringify(PAGE_SCAN).length` |
|---|---|
| working tree at v0.16.1 (baseline) | **3598** (gate 3700 — 102 spare, confirming A1 against the stale ~477 figure) |
| disposition 1's shape, empty descriptions | **3512** |
| disposition 1's shape, descriptions as written above | **3688 — PASS, 12 spare** |

**What paid for it, named as A1 requires:** `frontmatter_issue`'s whole property (`:163`);
`frontmatter_valid`'s whole property (`:159`), which carries the 208-char prohibition owner ruling
A-R1 retires — *"Absent verified_by:/verified_at: is NOT a validity defect (per write-verification@3
Scope rule) — attestation is reported through the verified_by/verified_at values above."* That
prohibition becomes **unexpressible by construction**: the enum's range excludes the route rather
than forbidding it in prose, and an attestation-only complaint can now only arrive as
`missing_required` naming exactly the two attestation keys — which disposition 1 refuses
arithmetically.

**Named reserve, if the builder needs bytes.** In order: (a) empty
`frontmatter_defect_detail`'s description (**+30**, the prompt already carries it); (b) shorten the
enum member `'malformed_block'` → `'malformed'` (**~+12**). **Do not** reach for `:168`'s
prohibition — it is owner-ruled KEPT (disposition 4). **Re-measure with the extractor after every
edit; a source char count is the wrong number.**

### 3. `PAGE_REQUIRED_FRONTMATTER` / `PAGE_OPTIONAL_FRONTMATTER` survive — and this build is what gives them a live code role

*Derives from: roundtable A37; grounding correction below.*

**Grounding correction.** A37 states the two sets "carry a live second role at `:563-568`" and must
survive. Re-grounded against current source: **`:563-568` is a comment block, not a code use.**
Every *code* reference to the two sets today is inside the machinery A37 retires — `:577`
(`KNOWN_FRONTMATTER`, feeding `KNOWN_FRONTMATTER_BY_LENGTH`), `:614-615`, `:625-626`. A naive
retirement would leave both constants orphaned, which is exactly the "deleting them by association"
error A37 warns about, reached by the opposite route.

**Ruled: the survival is made real, not asserted.** The rewritten dispositions classify
`frontmatter_defect_fields` **against these sets directly**, which is both the replacement for
`fieldsNamed` and the reason the sets are load-bearing:

- disposition 1 (attestation-only complaint) — `defect === 'missing_required'` **and** every entry
  of `_fields` is in `ATTESTATION_FRONTMATTER` **and** `_fields` is non-empty. (The "and NOTHING
  else" half is now set containment, not residue emptiness — it cannot be defeated by wording.)
- disposition 2 (invented requirement) — `defect === 'missing_required'` **and** every entry of
  `_fields` is in `PAGE_OPTIONAL_FRONTMATTER` **and** `_fields` is non-empty.
- neither disposition may fire on `'unclassified'` or `'malformed_block'`.
- `PAGE_REQUIRED_FRONTMATTER` keeps its role as the set that makes a **compound** claim report: a
  `_fields` list containing any required key satisfies neither containment test, so
  "malformed *and* unattested" survives as a finding. Keep the `:563-568` comment (updated to
  describe the new use); it is the record of *why* the page schema and the return schema are
  deliberately different lists.

**Grounding addition (beyond A37's letter).** `KNOWN_FRONTMATTER` (`:577`) exists only to feed
`KNOWN_FRONTMATTER_BY_LENGTH` and is dead the moment `:580` goes. A37 does not name it; it retires
with the apparatus, and the retirement grep (acceptance check 3) covers it.
`ATTESTATION_FRONTMATTER` (`:576`) **survives** with its `:573-575` comment.

### 4. `:664` — the second call site. RULED: the guard is retired, and `:168` is the compensation

*Derives from: roundtable A2 (the brief must rule `:664` explicitly), owner ruling A-R1, Q7,
§Carried forward item 9.*

`attestationOnlyComplaint()` has two call sites, re-verified this run:

- **`:701`** — `malformed_frontmatter`, via `refusedFrontmatterClaim` (`:630`). This is the site Q1
  structures.
- **`:664`** — `unmarked_supersessions`, filtering `s.unmarked_supersession`, an **array of
  free-text strings Q1 does not structure**. Its `:659-663` comment records why it exists: *"A13-1
  Finding 1's sixth entry (an attestation complaint) arrived here after the same prompt-side
  prohibition was ignored."*

**Ruled: retire the guard at `:664`, with its reason on record** — A2's third option.

**Why the other two options are not available.**

1. *Structure `unmarked_supersession` too.* Ruled out on measured evidence: `PAGE_SCAN` closes at
   **3688 of 3700** after disposition 1. Turning a string array into an object array cannot fit,
   and build-1 is released alone so it has no sibling to absorb a trim. It is also not the brief's
   to take: the roadmap states that **the moment `unmarked_supersession` is structured, the
   `:168` dissent becomes the ruling** (§Carried forward item 9) — reversing an owner ruling made
   at the roundtable is ideation's act, not a brief's.
2. *Keep the parser scoped to `:664` alone.* Ruled out because it contradicts three converged
   roundtable amendments at once: A37 (the seven-symbol retirement list, with a ship-verifiable
   grep behind it), Q7 (the refuted comment at `:559-561` retires **with the mechanism it
   documents** — keeping the mechanism keeps the comment's subject alive), and A-R1, whose stated
   premise is that *"build-1 removes its reduce-side guard at `:664`"*.

**The honest statement of the cost.** Once the predicate takes a structured record instead of text,
it **cannot be applied to a free-text string at all** — the guard at `:664` is not removed by
preference, it becomes inexpressible. The A13-1 Finding 1 exposure therefore returns: an
attestation-only complaint can again reach `unmarked_supersessions`. It is not a *silent* regression
— it is named here, compensated by disposition 5's interim posture, **measured** by acceptance
check 6, and it is the datum that decides §Carried forward item 9.

**`:168` is KEPT** (owner ruling A-R1) and becomes the only remaining depth for this class.
**DISSENT ON RECORD (Victor, Amelia), carried, not resolved:** `:550-557` records that Cycle 12
shipped exactly that kind of prompt-side prohibition and the next two full sweeps reported the
defect unchanged, and D1 rules in this same cycle that a schema description is never an enforcement
point — so the module ships a prohibition it has itself refuted, as the sole guard on this class.
**Do not delete `:168` and do not "strengthen" it.** Acceptance check 6 exists precisely because
`:168` is not believed.

### 5. R1 — interim posture for `unmarked_supersessions`

*Required by R1 (a rule shipped ahead of its mechanism).*

**Substantive, and it applies.** Between release 1 and the build that structures
`unmarked_supersession`, the rule *"a missing or stale attestation is NEVER an unmarked
supersession"* is stated at `:168` and enforced **nowhere**. What a vault legally does in that
window:

- `unmarked_supersessions` entries are **read as candidates, not verdicts.** An entry naming only
  `verified_by`/`verified_at` is refuted by the reader and **no fix is applied** — the page's
  unattestedness is already reported independently by `unattested_write` and `attestation_census`,
  computed from `attested()` (`:546`) over the same returned values.
- The hand-fold this creates is **recorded** in the sweep's `fixes_applied:` so it is countable —
  it is acceptance check 6's evidence, not invisible friction.
- The posture expires when `unmarked_supersession` is structured. That build is named at
  §Carried forward item 9 and inherits check 6's number.

### 6. A14-3 — decode at the comparison seam, not at scan intake

*Derives from: Q1 ruling 2; D1; §Questions left to brief time (the seam's exact placement is the
shape question this build owns).*

**Ruled: entity-decode where the comparison happens (`:643` and `:670`), never where the scan is
stored.** Both `h2set` and `s.category` are decoded through one shared helper; the finding message
renders the **decoded** value (the page's real category), and the `Set` is built from decoded
headings.

**Why not decode on intake into `scans`.** `scans` records are what build-2 will persist to the
sidecar as verbatim `PAGE_SCAN` returns. Decoding on intake would make the stored record a
*processed* value rather than the agent's return, which (a) breaks the verbatim contract the schema
states for these fields and (b) hands build-2 a record shape whose fidelity depends on a normalizer
version nothing fingerprints. Decoding at the seam keeps the sidecar byte-faithful and keeps the
normalization single-homed at the one place the exactness matters.

**Scope of the decode:** the named entities that appear in Markdown/HTML-escaped headings and
frontmatter — `&amp; &lt; &gt; &quot; &apos; &#39; &nbsp;` — plus numeric character references
(`&#NN;` / `&#xHH;`). Decode **once**, not repeatedly (no `&amp;amp;` cascade). **The comparison's
strictness is otherwise untouched: no trimming, no case folding** (D5; the `:668-669` comment
stays, extended by one clause naming the decode as a *transport* normalization).

### 7. Retirement clause (P-15) — the complete list, and it ships in this build

*Derives from: roundtable A37 / A38 / A-R1 and the obsolescence beat's retirements 1–3.*

Every item below is retired **in this build**; a ship-verifiable grep (acceptance check 3) proves
none survives.

| # | Retired | Site (re-grounded) | Because |
|---|---|---|---|
| 1 | `frontmatter_valid` property incl. its 208-char prohibition | `:159` | route unexpressible under the enum (A-R1); pays the budget |
| 2 | `frontmatter_issue` free-text schema slot | `:163` | the prose the structured return no longer sends (A37) |
| 3 | the refuted safety comment | `:559-561` | it documents the residue rule (Q7); the property it asserts was field-refuted |
| 4 | `KNOWN_FRONTMATTER_BY_LENGTH` + its `:578-579` comment | `:580` | longest-first scanning exists only to shred prose |
| 5 | `KNOWN_FRONTMATTER` | `:577` | dead once (4) goes — **grounding addition**, not in A37's list |
| 6 | `normalizeClaim` | `:584` | prose normalization |
| 7 | `claimWords` | `:585` | prose normalization |
| 8 | `CLAIM_FILLER` + the residue-rule comment `:586-590` | **`:591`** | **grounding correction — A37 cites `:589`; `:589` is comment text** |
| 9 | `parseClaim` | **`:594-604`** | **grounding correction — A37 cites `:593-603`; `:593` is comment text** |
| 10 | `fieldsNamed` | `:605` | replaced by set containment over `_fields` |
| 11 | the `attestationOnlyComplaint` call at `:664` | `:664` | disposition 4 |
| 12 | the conjunction/residue mechanism + the refuted over-reporting claim, vault-facing | `skills/vlt-lint/references/checks.md:15` | A38 — Q7 would have left the shipped copy asserting it |

**SURVIVE — do not delete:** `PAGE_REQUIRED_FRONTMATTER` (`:569`), `PAGE_OPTIONAL_FRONTMATTER`
(`:572`), `ATTESTATION_FRONTMATTER` (`:576`) and their comments (disposition 3);
`vlt-lint-full.js:168` (owner ruling A-R1, disposition 4); `:550-557` (the historical record of the
prompt-side prohibition's field refutation — it is the evidence behind the live dissent).

**Rewritten, not retired:** `attestationOnlyComplaint` (`:612-617`), `inventedRequirement`
(`:623-628`) and `refusedFrontmatterClaim` (`:630`) keep their names and their two dispositions;
only their input changes from text to the structured record. Keeping the names keeps
`checks.md:15`'s vocabulary and the `:607-611` / `:619-622` rationale comments true.

### 8. Q8 / E4 — the measurement build-1 produces, and what it does NOT discharge

*Derives from: Q8 as amended by roundtable A19; E4 as amended by A19; A20 (build-1 `binds:` E4).*

**The `malformed_frontmatter` retirement does NOT ride this build.** Build-1 produces the
measurement its successor needs, and **E4 transfers bound, not discharged** — a build that produces
a datum does not discharge a debt owed by the build that acts on it. Recorded at closeout as a
Stage-2 carry-forward with the specimen set attached (§Carried forward item 5).

Per A19, the measurement is bound by three constraints the brief must honour and the builder must
not simplify:

1. **It must be able to fail.** It asserts a stated bound (acceptance check 5), never merely reports
   a number — a count discharges on the act of counting.
2. **It is a SPECIMEN SET, never a bare count**: slug plus the minimal triggering fragment for every
   page reaching the class, materialized as a file under
   `factory/cycles/14-no-enforcement-point/`. Inheriting a cardinality would reproduce `ST-5` one
   section below the citation.
3. **Its two halves are different instruments.** *Pre-change* (the baseline): the persisted
   `{lint_reports}` archive already holds `malformed_frontmatter:` entries across multiple full
   sweeps — a real corpus needing no new sweep. *Post-change*: only a live sweep produces it,
   because this build changes the return's shape and pre-change recorded returns are free text the
   post-change schema cannot emit. **No wiki corpus ships in this repo.**

## F-sites

All `file:line` below re-derived against the working tree at v0.16.1 (`c18c591`) on 2026-08-26.
**The roadmap and the captures write the workflow as `vlt-lint-full.js`; its real path is
`skills/vlt-setup/assets/workflows/vlt-lint-full.js`** — 724 lines. Bare `:N` below is that file.

### F1 — `PAGE_SCAN`: the structured frontmatter verdict

**Current state.** `:145-178` is `PAGE_SCAN`. `:148` `required:` lists `'frontmatter_valid'`.
`:159` is `frontmatter_valid: { type: 'boolean', description: 'frontmatter present and well-formed.
Absent verified_by:/verified_at: is NOT a validity defect (per write-verification@3 Scope rule) —
attestation is reported through the verified_by/verified_at values above.' },`. `:163` is
`frontmatter_issue: { type: 'string', description: 'what is wrong if frontmatter_valid is false' },`.

**The exact change.** Replace `:159` and `:163` with the three properties in disposition 1, in that
order and at those positions (`frontmatter_defect` at the old `:159` slot so the verdict still reads
beside `outbound_links`; `_fields` and `_detail` at the old `:163` slot, mirroring the shipped
`sources_vs_prose` / `sources_vs_prose_detail` pairing two lines below). In `:148`, replace
`'frontmatter_valid'` with `'frontmatter_defect'` — **do not add the two new companions to
`required:`**; they mirror `sources_vs_prose_detail`, which is optional, and each `required:` entry
costs schema bytes the budget does not have.

**KEEP `:168`** (`unmarked_supersession`'s description, including *"A missing or stale attestation is
NEVER an unmarked supersession (per write-verification@3 Scope rule)."*) — owner ruling A-R1,
disposition 4. **KEEP `:160`** (`category`, verbatim) — F4 decodes at the comparison, not here.

**Why.** A14-1: the free-text claim is the parse the enforcement point cannot win. Q1 ruling 1;
A-R1; A35.

*Out of scope at this site:* every other `verbatim:` marker in `:152-171` — Victor's obsolescence
negative, checked in session: each is an instruction about what the scanner must *return*, and no
build displaces one. `summary` (`:162`) stays free text: its paraphrase face is deferred with A14-2
(Q1 ruling 3, §Carried forward item 2).

### F2 — `pageScanPrompt`: where the scanner guidance goes

**Current state.** `:214-216`. `:215` is the invariant instruction paragraph; `:216` is the
return-contract paragraph (*"return EVERY field the schema requires … The schema's field
descriptions are the field contract; follow them exactly. Extract verbatim…"*).

**The exact change.** Add to `:216` the guidance disposition 1 keeps out of the schema: what each
`frontmatter_defect` member means; that `frontmatter_defect_fields` carries **bare frontmatter key
names only** (`summary`, not "missing summary field", never a sentence and never a rule citation);
that anything not fitting a member is `'unclassified'` with the words in `frontmatter_defect_detail`
rather than forced into a member that fits badly; and that a **rule citation belongs in `_detail`,
never in `_fields`** — the sentence that names this build's own defeat mechanism. Adjust `:215`'s
*"judge frontmatter validity"* clause to the new field names.

**Why.** D1: this text is documentation and never the enforcement point — the enum's range is the
enforcement. It is here because it costs **zero** against the E6 gate (`_e6_schema_size_budget`
measures `JSON.stringify(PAGE_SCAN)` only) while the schema has 12 chars left.

### F3 — the reduce-side guards: from residue parsing to set arithmetic

**Current state.** The guard block is `:549-630`.
- `:549-561` — the block comment; `:559-561` is the refuted safety claim.
- `:563-568` — the page-schema-vs-return-schema comment; `:569` `PAGE_REQUIRED_FRONTMATTER`;
  `:570-571` comment; `:572` `PAGE_OPTIONAL_FRONTMATTER`; `:573-575` comment; `:576`
  `ATTESTATION_FRONTMATTER`; `:577` `KNOWN_FRONTMATTER`; `:578-579` comment; `:580`
  `KNOWN_FRONTMATTER_BY_LENGTH`.
- `:582-583` comment; `:584` `normalizeClaim`; `:585` `claimWords`; `:586-590` the residue-rule
  comment; **`:591` `CLAIM_FILLER`**; `:592-593` comment; **`:594-604` `parseClaim`**; `:605`
  `fieldsNamed`.
- `:607-611` comment; `:612-617` `attestationOnlyComplaint`; `:619-622` comment; `:623-628`
  `inventedRequirement`; `:630` `refusedFrontmatterClaim`.

**Grounding correction (two cites, marked).** The roadmap's A37 list gives `CLAIM_FILLER` at `:589`
and `parseClaim` at `:593-603`; current source has them at **`:591`** and **`:594-604`** — `:589`
and `:593` are comment text. A29 already corrected four cites in this region against an earlier
drift; these two survived it. Scope is unchanged; the retirement list is the same seven symbols.
*A superseding note is appended to the roadmap's build-1 block.*

**The exact change.**
1. Retire items 3–10 of the disposition-7 table (`:559-561`, `:577`, `:580` + `:578-579`, `:584`,
   `:585`, `:591` + `:586-590`, `:594-604`, `:605`).
2. Replace `:559-561` with the **new invariant, stated for the structured return** (Q7: *"the build
   states the new invariant in its place"*). The honest half of the old comment must survive the
   move — say that the guards only ever REFUSE, never add; that they fire only on
   `defect === 'missing_required'` with a field list wholly inside a known set; that
   `'unclassified'` and `'malformed_block'` are never refused; and that **the failure direction is
   over-reporting, never swallowing a genuine schema break** — now a property of the escape member
   rather than of a filler list, and **tested by acceptance check 1 rather than asserted**.
3. Rewrite `:612-617` and `:623-628` to take the structured record (disposition 3's three
   predicates), keeping their names, their `:607-611` / `:619-622` rationale comments (the duplicate
   /non-event asymmetry is unchanged and still true), and `:630` `refusedFrontmatterClaim` as is.
4. Update `:563-568`'s comment to describe the sets' new use, keeping its explanation of why the
   page schema and `PAGE_SCAN.required` are deliberately different lists — that conflation is the
   defect the sets guard, and it is still live.
5. **Keep `:550-557` verbatim.** It is the record that a prompt-side prohibition of exactly this
   kind was shipped and field-refuted — the evidence behind the live `:168` dissent.

**Why.** A14-1's durable diagnosis: the enforcement point parses scanner-returned free text in order
to decide whether to trust a scanner-returned claim. Set containment over a bare field list cannot
be defeated by wording. Q1 ruling 1; Q7; A37.

### F4 — the category seam: entity-decode on both sides

**Current state.** `:643` `const h2set = new Set(indexScan ? indexScan.h2_headings || [] : [])`.
`:668-669` the strictness comment. `:670` `category_no_match: indexScan ? scans.filter((s) =>
!h2set.has(s.category)).map((s) => \`${s.slug}: category '${s.category || '(none)'}' matches no
H2\`) : []`. Verified this run: **`s.category` is read at `:670` and nowhere else; `h2set` at `:643`
and `:670` and nowhere else** — a narrow, two-sided seam. `h2_headings` is agent-returned
(`INDEX_SCAN`, `:184`; `required` at `:180`).

**The exact change.** Add a small `decodeEntities(text)` helper immediately above `:643` (named
entities + numeric references, single pass, no cascade). Build `h2set` from decoded headings; test
and render the decoded `category`. Extend the `:668-669` comment by one clause: HTML entities are
decoded on **both** sides as a transport normalization before the comparison — the binding stays
case-sensitive with no trimming and no case folding.

**Why.** A14-3: a scanner returning `Energy &amp; Clean Tech` for a page carrying `Energy & Clean
Tech` fails `Set.has()` against the un-escaped heading. Capture's sharpening: `h2set` is
agent-returned too, so **an entity on the index side falsifies every page in that category at once**
— the fan-out-wide half that has not fired yet. Q1 ruling 2; D1.

*Out of scope at this site:* loosening the comparison (D5, rejected); normalizing any other exactly
compared field (no other seam is in this build's captures — if one is found, it is a filing).

### F5 — `checks.md`: the vault-facing catalogue

**Current state.** `skills/vlt-lint/references/checks.md` has **no frontmatter, no `version:`, no
`consumers:`** (verified `checks.md:1` — it is a plain `# vlt-lint — reference: Step 2` heading).
`:15` defines `malformed_frontmatter` and carries, in the vault-facing copy: the two exclusions
described as *"**Both exclusions are conjunctions**"*, the sentence *"a claim the reduce cannot
positively identify as one of these two shapes always reports"*, and **the refuted claim** *"The
failure direction is deliberately over-reporting, never swallowing a schema break."*
`:14` defines the `category_no_match` half of frontmatter/Bases-field drift (*"`category:` present
and **exactly matching an existing `{index}` H2**"*).

**The exact change.**
1. `:15` — rewrite the exclusions in the structured return's terms: both dispositions test the
   returned defect verdict and its named-field list, not the wording of a complaint; a defect the
   scanner cannot classify is returned as `unclassified` and **always reports**. Retire the
   conjunction/residue prose and the over-reporting *safety guarantee* as a guarantee. Keep the
   over-reporting **failure direction** as the stated design intent of the `unclassified` escape,
   which is what now makes it true. **Keep the legal response unchanged** (R3 — repair the
   frontmatter to the page schema; never auto-write a page whose frontmatter could not be parsed).
2. `:14` — add one clause: the category↔H2 binding is compared **entity-decoded on both sides**; it
   remains exact, case-sensitive, no trimming (R3 for the changed `category_no_match` class).

**Why.** A38: `checks.md:15` carries the same refuted safety claim in the vault-facing catalogue and
documents the mechanism this build removes; Q7 retires the claim at `:559-561` and would leave the
shipped, vault-read copy asserting it. **No new cost:** `checks.md`'s digest is already a component
of the ruleset fingerprint, and this build is cold by construction.

*Out of scope at this site:* `checks.md:17`'s `para_missing_attestation` carve-out (build-3, per
roundtable A11b) and `checks.md:19`'s recognized set (build-3, per Q3/A14). **Do not touch either
— build-3 owns them and rebases onto this build.**

### F6 — `report.md`: verified, no edit owed

**Current state + disposition.** `report.md:66` documents the `malformed_frontmatter` slot and its
two exclusions (*"an attestation-only complaint (→ unattested_write) and a claimed-missing OPTIONAL
field (→ not a finding) are excluded at the reduce, never listed here"*). Both exclusions **survive
this build** — only their input changes — so the sentence remains true and **no edit is owed**.
`report.md:20`'s `unmarked_supersessions_fixed:` slot is likewise unchanged. Verified, not assumed:
this is the only other file in `skills/` mentioning either class
(`grep -rn "frontmatter_issue\|frontmatter_valid\|unmarked_supersession\|malformed_frontmatter"
skills/ tools/`).

## Registration

**None.** This build creates no skill and no workflow, and **no convention `version:` moves** — so
no consumer walk and no re-ack is owed. Priced explicitly, per brief-anatomy §5's "no bump owed is
not no cost":

- **package-lint E5 (asset ack)** — `:11`'s `depends_on: ["frontmatter@13", "wiki-supersession@2",
  "wiki-index@2", "write-verification@3"]` is **unchanged**: this build enforces no new convention
  rule and drops no convention read. **Build-3 changes this line** (roundtable A3); build-1 must
  not, or build-3 rebases onto a wrong baseline.
- **package-lint E6 (schema budget)** — **the gate this build actually spends against.** See
  disposition 2 and acceptance check 4.
- **package-lint E4 (harness coverage) / R2 fixture extension** — **not applicable**: this build
  adds and changes no `package-lint` check, so `tools/test-package-lint.py` and `CASE_FLOOR` are
  untouched.
- **package-lint C6 (rule card)** — **not applicable**: `governance/_meta/vault-operating-contract.md`
  is not touched (build-3's).
- **`module-help.csv`** — unchanged; no new skill, no changed args or outputs.

## Out of scope (dispositioned)

- **A14-2, the outbound-link enumeration** — deferred by Q1 ruling 3; needs the page's text, which
  the workflow structurally cannot fetch (`:26-28`, `:37`). §Carried forward item 1; **its filing
  stays in `factory/inbox/`** (roundtable A23). Do not "improve" `outbound_links` here.
- **Cycle 13 carry-forward 1, the `summary` paraphrase** — deferred with the above (§Carried forward
  item 2). Carson's cheap route (a SKILL-side `{slug: summary_len}` map, since `:545` reads only
  `.trim()` and `.length`) is **recorded for the successor and not taken** — owner Ruling 3:
  build-1 is the release-1 critical path and already over its schema budget.
- **Tracker #13 (`argsPath`)** — not re-admitted (Q2). Bound to Cycle 15's `inbox-capture`.
- **The `malformed_frontmatter` retirement** — deferred a third time (Q8); this build ships its
  measurement. §Carried forward item 5.
- **`checks.md:17` and `:19`; `write-verification.md`; `frontmatter.md`; `contract:66`** — build-3.
- **`fresh_scans` / the sidecar record shape / fingerprint composition (`:719-723`, `:232-243`)** —
  build-2. ⚠ **Build-2 depends on this build** (roundtable A4): its `scan` payload **is** this
  build's `PAGE_SCAN` return, and `scanFingerprint` is a key component. Do not pre-empt it; do not
  change `runKey`'s composition here.
- **`report.md`, `full-scale.md`, `SKILL.md:74`, `fix-and-file.md`** — builds 2 and 4.
- **`vlt-lint-full.js:168`** — kept by owner ruling, with a live dissent (disposition 4).
- **Every other `verbatim:` marker** — obsolescence negative returned explicitly at the roundtable.

## Verification (unit, at rest — lifecycle step 5)

Run all of these before the commit; record the outputs in the BUILT `status:`.

1. **V1 — the guard harness.** Load the shipped workflow source with stubbed
   `agent`/`parallel`/`phase`/`log`/`budget` and `args` delivered as a **JSON string** (the runtime
   contract; parse-on-intake). Drive the reduce with hand-built structured returns and assert the
   four arrays (`malformed_frontmatter`, `unmarked_supersessions`, `unattested_write`,
   `attestation_census`) verbatim. Cases, each of which must be able to fail:
   - attestation-only: `missing_required` + `_fields: ['verified_by','verified_at']` → **refused**;
   - the same, with `_detail` carrying the **2026-08-26 rule-citing text from the filing** →
     **still refused** (the defeat mechanism, dead);
   - invented requirement: `missing_required` + `_fields: ['review_after']` → **dropped**;
   - **control** — genuine break: `missing_required` + `_fields: ['summary']` → **reports**;
   - **control** — compound: `_fields: ['summary','verified_by']` → **reports**;
   - **control** — escape: `unclassified` + arbitrary `_detail` → **reports** (A35's invariant);
   - **control** — `malformed_block` → **reports**;
   - **control** — a genuine unmarked supersession still reaches `unmarked_supersessions`.
2. **V2 — the entity-decode fixture.** Page-side `Energy &amp; Clean Tech` vs an H2 `Energy & Clean
   Tech` → **no finding**; index-side `Energy &amp; Clean Tech` vs page `Energy & Clean Tech` →
   **no finding** (the fan-out-wide half); `&#38;` numeric form → no finding; **controls that must
   still flag:** a genuinely different category, a case difference, a leading-space difference
   (D5 — strictness not softened).
3. **V3 — the retirement + survivor grep.**
   `grep -n "parseClaim\|fieldsNamed\|KNOWN_FRONTMATTER\|normalizeClaim\|claimWords\|CLAIM_FILLER\|frontmatter_issue\|frontmatter_valid" skills/`
   returns **zero** hits. `grep -n "PAGE_REQUIRED_FRONTMATTER\|PAGE_OPTIONAL_FRONTMATTER\|ATTESTATION_FRONTMATTER" `
   on the workflow returns hits **inside the rewritten predicates** (a live code role, not a
   definition standing alone). `node --check` on the workflow parses.
4. **V4 — the E6 re-measure.** Re-measure `JSON.stringify(PAGE_SCAN).length` with **package-lint's
   own `_E6_NODE_EXTRACTOR`** (never a source char count) and record the number. Must be **≤ 3700**.
5. **V5 — packaging lint.** `uv run tools/package-lint.py` — **A/B/C/E PASS** (Group E is the check
   of record for the handshake; do not hand-write a `grep "<name>@" skills/` substitute). At the
   release commit, the `--expect-version` gate per §Release.
6. **V6 — handshake bipartite.** No convention `version:` moved and no `consumers:` list changed, so
   nothing is owed beyond Group E in V5. State that in `status:` rather than leaving it silent.
7. **R3 — legal response.** `malformed_frontmatter`'s and `category_no_match`'s legal responses are
   stated at their single home, `checks.md` (F5). **Applicable and satisfied in this build.**
8. **R4 — enumeration widening.** **Not applicable** — this build adds no file to any enumerated
   vital, manifest, or skill-asset class. The Q8 specimen set is a **factory record** under
   `factory/cycles/14-no-enforcement-point/`, declared outside every shipped enumeration (it is
   never copied into a vault by own-the-apply).
9. **R2 (roundtable) — fixture posture.** Build-1 has a real prior failure behind it, so a synthetic
   fixture is not reached for unchallenged: V1/V2 are synthetic **unit** fixtures for the controls,
   and **acceptance check 2 forbids a synthetic fixture** and requires the real six-page corpus.
   Record this split in `status:`.
10. **Scrub.** No personal or vault-local content in any changed shipped file. In particular:
    the six subject slugs of Cycle 13's check (2) are referenced **by pointer**
    (`factory/cycles/13-trusted-returns/roadmap.md:468-473`), never copied into a shipped file, and
    the specimen set is a factory artifact, never a shipped one. Delete any `.decision-log.md`.

## Release (release build only — build-1 IS Release 1)

Build-1 is cut alone because it is the only thing that reopens Cycle 13's closeout gate.

- Branch `cycle14-vX.Y.Z`, one commit for this build.
- Bump **both** version strings: `.claude-plugin/marketplace.json` `"version"` and
  `skills/vlt-setup/assets/module.yaml` `module_version`.
- **⚠ The version number is the owner's at release time** — the roadmap rules "Release 1 = build-1
  alone" and names no number. The brief's recommendation is **`0.16.2`** (a defect repair with no
  new capability), but `vlt-release` takes it as its argument; confirm before tagging.
- Pre-tag gate: `uv run tools/package-lint.py --expect-version X.Y.Z` — **tag only on exit 0**, and
  put its PASS summary line in the release commit message.
- ff-merge to `main`, tag `vX.Y.Z`, push main + tag.
- **Release note must state the cold sweep up front** (see §Intent): every existing lint sidecar
  record is unreusable and the first post-upgrade full sweep scans 100% of pages. This is by
  construction, not a cache regression.
- **⚠ `factory/CYCLE` hazard — do not run either cycle-scoped skill headless.** Two cycles are open
  (13 gate-shut, 14 open) and `factory/CYCLE` holds one line, currently `14-no-enforcement-point`.
  Before running `acceptance-discharge` or `cycle-closeout` **against Cycle 13**, hand-point
  `factory/CYCLE` at `13-trusted-returns` and restore it immediately after (roundtable A24).

## Acceptance (live — appended to the roadmap ledger)

**Cycle ruling D3 as amended (roundtable A17) governs every check below: a check whose discharging
event is BOUNDED — at rest, at the release gate, or on the next ordinary upgrade — is
`[ship-verifiable]` and it GATES. `field-contingent` is reserved for the genuinely unbounded.**
All eight checks below are bounded; **none is field-contingent, and all eight gate.** Per A17b
clause 1, every subject gradeable at rest by an instrument buildable in this build's scope has one
built — nothing is declined. Per **rule R1**, each check names **which seam its instrument actually
crosses**.

**(1) `[ship-verifiable]` — at rest — GATES.** *The defeat mechanism is gone, and the escape
reports.* Over the V1 harness against the **shipped** workflow source: the attestation-only case is
refused **whether or not `_detail` carries the 2026-08-26 rule-citing text from the filing**, the
invented-requirement case is dropped, and **all five controls survive** (genuine break, compound
break, `unclassified`, `malformed_block`, genuine unmarked supersession). *Instrument:* the V1
harness, factory-side at rest, stubbed `agent`/`parallel`/`phase`/`log`/`budget`, `args` as a JSON
string. *Seam crossed:* the **scan → reduce** seam — the instrument feeds the reduce the exact
values a scanner returns, which is the surface the field defeated. *Evidence:* the four arrays
recorded verbatim in the BUILT `status:`.

**(2) `[ship-verifiable]` — at rest — GATES. ⚠ THIS IS THE CHECK THAT RE-GRADES CYCLE 13's
ACCEPTANCE CHECK (2)** *(roundtable A21 — without it, release 1 could ship and Cycle 13 still not
close).* Cycle 13's (2) reads: *"the six pages that actually failed stop reaching the wrong classes
— re-scanned, zero of [six named subjects] reach `malformed_frontmatter` or
`unmarked_supersessions`, and the attestation surface still carries them"*
(`factory/cycles/13-trusted-returns/roadmap.md:468-477`). It was refuted **at rest** on a named
subject, so its re-grade is at rest. **Re-grade:** re-scan **read-only copies of those same six
pages** with the **post-build** `PAGE_SCAN` and prompt, apply the **shipped** rewritten reduce, and
assert zero of the six reach either class while `unattested_write` / `attestation_census` still
carry them. *Instrument:* a single-agent reader probe over read-only copies of the six subjects from
`{field-vault}` (the vault is never written), plus the shipped reduce applied to the returns —
factory-side, at rest. *Seam crossed:* the **page bytes → scanner → reduce** seam end-to-end; this
is the only check here that crosses the agent, and that is precisely why it cannot be replaced by a
fixture. *Binding, carried forward verbatim from Cycle 13's (2):* **a fixture built to exercise only
the surfaces this build changes does NOT satisfy this check** — Cycle 13's own instrument passed by
replaying 2026-08-25 bare-form returns, the exact subset the guard handled, and could not observe
the failure it was written to catch (`ST-5` cause 2). *Evidence:* the returned JSON and the
post-reduce arrays, verbatim, in the BUILT `status:`.

**(3) `[ship-verifiable]` — at rest — GATES.** *The retirement landed whole and the survivors are
alive.* `grep -n "parseClaim\|fieldsNamed\|KNOWN_FRONTMATTER\|normalizeClaim\|claimWords\|CLAIM_FILLER\|frontmatter_issue\|frontmatter_valid" skills/`
returns **zero** hits across the whole shipped surface; `PAGE_REQUIRED_FRONTMATTER`,
`PAGE_OPTIONAL_FRONTMATTER` and `ATTESTATION_FRONTMATTER` are each **referenced from the rewritten
predicates**, not merely defined; `node --check` parses the workflow; `:168` and `:550-557` are
byte-identical to v0.16.1. *Instrument:* the V3 greps + `node --check`, at rest. *Seam crossed:*
none at runtime — this is a **source-agreement** check across the shipped tree, and it is named as
such rather than dressed as a behavioural one. *Evidence:* grep outputs verbatim.

**(4) `[ship-verifiable]` — at the release gate — GATES.** *The hard schema budget holds.*
`JSON.stringify(PAGE_SCAN).length ≤ 3700`, re-measured by **package-lint's own
`_E6_NODE_EXTRACTOR`** (`tools/package-lint.py:900-940`), and
`uv run tools/package-lint.py --expect-version X.Y.Z` exits **0** with both version strings at
X.Y.Z. *Instrument:* package-lint Group E (E6 for the budget, E1/E2/E3/E5 for the handshake) plus
Group D at the tag. *Seam crossed:* the **source literal → runtime serialization** seam — the reason
a source char count is the wrong number (a 4,266-char literal serializes to 4,100). *Evidence:* the
measured length and the PASS summary line, in the release commit message.

**(5) `[ship-verifiable]` — at rest — GATES.** *The category seam is closed on both sides and the
comparison is no looser.* Over the V2 fixture: page-side and index-side escaped forms each produce
**no** `category_no_match`, numeric references decode, and **all three controls still flag** (a
different category, a case difference, a leading space). *Instrument:* the V2 fixture against the
shipped reduce, at rest. *Seam crossed:* the **index scanner → reduce** and **page scanner →
reduce** seams — both sides of the comparison, which is the half A14-3's filing did not notice.
*Evidence:* the `category_no_match` arrays for all six cases, verbatim.

**(6) `[ship-verifiable]` — bounded to the first full `{field-vault}` sweep after release 1 —
GATES.** *The `malformed_frontmatter` measurement Q8/E4 owes, as a specimen set with a bound it
can fail.* **Bound asserted (A19 fault 1 — not a bare count):** in the post-repair class,
**zero** specimens are attestation-only complaints and **zero** are claimed-missing
documented-optional fields; **every** remaining specimen is adjudicated, one by one against its
page, as a genuine schema break. The class's cardinality is recorded but is **not** the check.
**Deliverable (A19 fault 2):** a specimen set — slug **plus the minimal triggering fragment** for
every page reaching the class — materialized as a file under
`factory/cycles/14-no-enforcement-point/`, with corpus size and date, and summarized in the BUILT
`status:`. *Instruments — two, and they are different (A19 fault 3):* **pre-change baseline** — the
persisted `{lint_reports}` archive, a real corpus needing no new sweep (the 2026-08-24 / 2026-08-25
/ 2026-08-26 sweeps); **post-change** — a live full sweep, because this build changes the return's
shape and pre-change recorded returns are free text the post-change schema cannot emit, and **no
wiki corpus ships in this repo**. *Seam crossed:* the **live page corpus → scanner → reduce** seam
at 146-page scale — the only instrument that observes what genuinely reaches the class. *Event:*
the owner runs `vlt-lint --full` on `{field-vault}` after upgrading to release 1. *Performer:* the
owner (standing rule). *Vault:* `{field-vault}` only — the sole install with the 146-page wiki and
this defect's multi-run baseline. **⚠ E4 is BOUND, not discharged, by this check** — build-1
produces the datum; the debt transfers with the number attached to the build that takes the
retirement (§Carried forward item 5).

**(7) `[ship-verifiable]` — bounded to the same sweep as (6) — GATES.** *The `:664` retirement's
exposure, measured rather than assumed.* Retiring the reduce-side guard at `:664` leaves `:168` as
the only depth for `unmarked_supersessions` (disposition 4, owner ruling A-R1, live dissent).
**Bound asserted:** in that sweep, **no** `unmarked_supersessions` entry is an attestation-only
complaint, and `fixes_applied:` records **no** hand-fold of a misrouted attestation entry — against
a baseline in which all three entries of the 2026-08-26 sweep were false and one was exactly this.
**This check can fail, and if it does, the dissent (Victor, Amelia) becomes the ruling and
`unmarked_supersession` is structured by the successor build** — that is the decision this number
exists to make (§Carried forward item 9). *Instrument:* the same live full sweep as (6), read
against the `{lint_reports}` archive baseline. *Seam crossed:* the **prompt instruction (`:168`) →
scanner return → reduce** seam — the one seam this build deliberately leaves with no reduce-side
enforcement point, which is why it is measured and not asserted. *Event / performer / vault:* as (6).

**(8) `[ship-verifiable]` — at rest — GATES.** *The vault-facing catalogue no longer asserts the
refuted claim.* `checks.md:15` contains **no** conjunction/residue mechanism prose and **no**
over-reporting *guarantee*; it describes the structured verdict and its two exclusions, states that
an `unclassified` defect always reports, and retains the class's legal response unchanged (R3);
`checks.md:14` states the entity-decoded, still-exact category binding. `grep -rn "residue\|Both
exclusions are conjunctions" skills/` returns **zero**. *Instrument:* the V3 greps plus a read of
the two lines, at rest. *Seam crossed:* the **module source → vault-read documentation** seam — the
copy a vault actually reads, which Q7's retirement at `:559-561` would have left asserting the
refuted property. *Evidence:* the grep output and the two rewritten lines, quoted in `status:`.
