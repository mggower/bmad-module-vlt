---
title: 'Build #1 — page-scanner corrections + waste removal (the full-lint page scanner stops reading raw text as link structure and frontmatter validity as attestation, and sheds the reads it never used)'
status: 'BUILT 2026-08-25 — all eight F-sites landed on branch `cycle12-v0.16.0`. **F1** `:143` `outbound_links` gained the shape predicate + code-span exclusion (`per frontmatter@13 rule 5`); **F2** `:144` `frontmatter_valid` and **F3** `:153` `unmarked_supersession` each lost jurisdiction over attestation (`per write-verification@3 Scope rule`); **F4** `key_claims` deleted from the schema and from `clusterPrompt` (the live re-read stands); **F5** `convRead(''wiki-index'')` dropped from `pageScanPrompt` only — the `:11` pin, `wiki-index.md:12`''s `consumers:` and `indexPrompt` all untouched; **F6** the return-only half reduced 1,130 B → 396 B (−734 B/agent); **F7** `write-verification.md` §Scope rule gained the jurisdiction-boundary clause (still `version: 3`, 5 consumers — no bump, no re-ack, Q6/R-2); **F8** `checks.md:13` *Missing targets* narrowed its population by citation, legal response unchanged.
  **V1 — E6 schema-size gate (package-lint''s own node extractor):** before `PAGE_SCAN` 3223 / `INDEX_SCAN` 823 / `CLUSTER_FINDINGS` 1630 / `PAIR_FINDINGS` 376 → after **`PAGE_SCAN` 3598** / 823 / 1630 / 376. **3598 ≤ 3700 — PASS, 102 chars of margin.** (`key_claims` drop measured 3223 → 3081 exactly as briefed; the three clauses spent 517 of the 619 available.)
  **V2 — packaging lint:** `PASS group A / B / C / E; SKIPPED group D (no --expect-version)` — `package-lint: A/B/C/E PASS, D SKIPPED — vlt 0.15.0`.
  **V3 — reader probe (one `haiku` agent, the *edited* composed prompt + the *edited* `PAGE_SCAN`, against a temp fixture carrying a fenced DQL block with `FROM [[note]]` / `FROM outgoing([[note]])`, a code-span `![[File.base]]` embed, a table row with `[[food]]` / `[[exercise]]` in code spans, a bare `## Sources` filename `2026-02-14-macdonald-defense`, exactly two genuine body wikilinks, and valid-but-unattested frontmatter). Returned verbatim:** `{"slug":"dataview-query-syntax","available":true,"title":"Dataview Query Syntax","created":"2026-05-02","last_updated":"2026-08-20","verified_by":"","verified_at":"","review_after":"","outbound_links":["obsidian-plugin-notes","bases-view-syntax"],"frontmatter_valid":true,"category":"Tooling","topic_is_list":true,"summary":"How DQL and Bases embeds are written, with the link-shaped syntax spelled out.","frontmatter_issue":"","sources_vs_prose":"diverge","sources_vs_prose_detail":"Prose Sources section lists ''2026-02-14-macdonald-defense'' but frontmatter sources: is empty list","stale_unmarked":[],"within_page_contradictions":[],"unmarked_supersession":[],"thin":false,"name_callout_targets":[]}` — **all four pass conditions met:** `outbound_links` is exactly the two genuine links (traps a–d contributed **zero**), `frontmatter_valid: true` on the unattested page, no attestation complaint in `unmarked_supersession`, and **14 of 14 required fields returned populated** (the three empty strings are genuinely-absent optional values, which the schema''s own descriptions require as `""`). `sources_vs_prose: diverge` is correct and expected — the fixture''s empty `sources:` against a prose entry.
  **V4 — fan-out audit (R4, `:16-21`), re-run because F5 changed the read list.** `pageScanPrompt` now receives `{frontmatter, wiki-supersession, write-verification}`; every ask it makes is covered — frontmatter validity + rule-4 sources normalization → `frontmatter@13`; the Gap B tri-state → `write-verification@3`; the callout-form gate → `wiki-supersession@2`; the three new schema clauses → `frontmatter@13 rule 5` / `write-verification@3` ×2. **No surviving ask judges against `wiki-index.md`** (`category:` is returned verbatim; the category↔H2 binding is JS — `h2set` at `:494`, consumed `:514`). `indexPrompt` (now `:370`) still reads and judges against `wiki-index.md`, so **the `wiki-index@2` pin at `:11` survives on `:370`''s strength and `wiki-index.md:12`''s `consumers: [..., vlt-lint-full.js]` entry is still true** — E5 parses the unchanged ack line and passes. `clusterPrompt`/`pairPrompt` read no conventions and carry their `per wiki-supersession@2` markers as before (pre-existing posture, untouched).
  **V5 — R3:** `checks.md:13`''s legal response present and unchanged; `checks.md:16` and `:34` not edited; the boundary is stated in exactly one place (`write-verification.md`). **V6 — R4 enumeration widening:** n/a (narrowing; V4 is its audit).
  **V7 — greps:** `key_claims` → **0**; `wiki-index` in the workflow → `:11`, `:166`, `:370` only; `write-verification.md` → `version: 3`, `consumers:` 5, unchanged; `grep -rn "frontmatter.validity" skills/` → one full statement (`write-verification.md:55`) plus the pre-existing `pageScanPrompt` instruction that cites it — single home holds; `per frontmatter@13|per write-verification@3` markers in the workflow → **5**.
  **V8 — harness sanity run** (shipped source loaded with stubbed `agent`/`parallel`/`phase`/`log`/`budget`, `args` delivered as a JSON **string**, 3-page fixture, scripted scan results): the reduce is unchanged — `missing_targets ["a-alpha → ghost-page"]`, `malformed_frontmatter ["c-gamma: title missing"]`, `unmarked_supersessions ["a-alpha: silent update"]`, `attestation_census {pages_total:3, fresh:0, stale:2, unattested_pre_adoption:1}`, `category_no_match`, `index_drift`, `frontmatter_drift`, `sources_vs_prose_mismatches` and `cost_accounting` all populate; **`clusterPrompt` composes with no `key_claims`**. **Composed `pageScanPrompt`: 2,990 B → 2,225 B/agent (−765 B, −25.6%)** ≈ **−112 KB/run** at 147 agents, on top of F5''s agent-side 8,133 B × 147 ≈ **1.2 MB/run** of convention text no longer read. **V9 — scrub:** clean (no machine paths, username, or vault-local artifact paths in any changed tracked file). **V10 —** no `.decision-log.md` anywhere in the working tree.
  **Build-2 note (out-of-scope item 4):** this build **changes the `pageScanPrompt` + `PAGE_SCAN` fingerprint** — any findings sidecar written before it holds verdicts adjudicated under a retired ruleset.
  Deviations/notes: **(1)** F6 gave the builder a judgment call on whether the A12-1/A12-2 clauses also need a prompt-side statement. They do **not**: the probe passed all four conditions with the clauses stated **once**, in the schema descriptions, so nothing was added to the rules half — single statement, as F6 asked. **(2)** Brief-time disposition 2''s required-field guard **held on the first probe** (14/14 populated), so no prompt text was restored and `:202`''s reduction stands at its full extent. **(3)** Verification 7''s expectation `grep -c "convRead(''wiki-index'')" → 0` is unsatisfiable as written and was read as scoped to `pageScanPrompt`: F5 explicitly preserves `indexPrompt`''s read, and that line contains the same token, so the **file-wide count is 1**. The brief''s companion grep (`wiki-index` → the pin, the `INDEX_SCAN` description, `indexPrompt`) is the check that actually discriminates, and it passed. **(4)** The two deletions shifted every cite below them: `pageScanPrompt` `:200`→**`:199`** (rules half `:201`→**`:200`**, reduced half `:202`→**`:201`**), `indexPrompt` `:371`→**`:370`**, `clusterPrompt` `:402-406`→**`:401-404`**, `h2set` `:496`/`:516`→**`:494`/`:514`**. Recorded for build-3 and build-2''s briefs — this is the fourth line-cite drift the cycle has logged (out-of-scope item 8). **(5)** F7 cites `frontmatter.md`''s attestation section by its **real heading**, *Write attestation (agent-written artifacts)*; the brief wrote *Attestation*, which is not a heading that exists in that file. **(6)** The commit also carries `factory/cycles/12-proxy-claims/roadmap.md`''s uncommitted brief-time edits (the six-check acceptance-ledger append, the two brief-time answers, the restamped routing block) — the briefing session left them in the working tree and they are this brief''s own record, with no other commit to ride. No shipped file was touched by that inclusion. **(7)** The composed-prompt baseline reported above is **2,990 B**, not the brief''s 2,803 B: the brief measured the raw template literal, the harness measures the composed string with `convRead` expanded under a named overlay. Same reduction, larger denominator; brief-time disposition 1''s conclusion (the cacheable prefix does not clear the 1,024-token floor) is unaffected — the variable head is still first, and the invariant remainder is still ~660 tokens after F6. **(8)** The brief''s terminal **Next lifecycle move** line was restamped on exit — it still routed to the builder session that had just run, which the lifecycle map''s standing rule names as the defect, not the position. It now reads `brief build 3`, agreeing with this `status:`.'
module_code: 'vlt'
created: '2026-08-25'
derives_from:
  - 'factory/inbox/2026-08-24-173001-lint-page-scanner-counts-code-span-wikilinks.md (A12-1 — symptom fix: the two extraction defects, code-span inclusion + non-wikilink text matched as a link)'
  - 'factory/inbox/2026-08-24-173002-page-scanner-double-reports-missing-attestation.md (A12-2 — cause fix: strip frontmatter_valid and unmarked_supersession jurisdiction over attestation; Q6 the boundary clause)'
  - 'factory/cycles/11-reachability/roadmap.md §A11-11 (direction 1 — workflow-only waste removal, carried into Cycle 12 by the closeout hand-off)'
roadmap: 'factory/cycles/12-proxy-claims/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-25): Q1 SPLIT PER FILING — A12-1 takes the symptom fix now, A12-2 takes the cause fix (subtractive); its cause-fix instrument is DECLARED for Cycle 13 · Q6 IN, as a prose clarification, NO BUMP, NO RE-ACK — and R-2/A8 moves its home to write-verification.md §Scope rule · Q8b direction 1 LANDS this cycle, direction 4 declared for Cycle 13 · D3 ONE RELEASE, whole cycle · grouping (clerk-drafted, owner-adopted): all four items edit pageScanPrompt and its schema, so they are one build · roundtable amendments A1–A9 apply before briefing'
risk: 'moderate — no convention version bump and no consumer re-ack (Q6 is a prose clarification per CLAUDE.md; write-verification.md stays version: 3 / 5 consumers), but the build sits against ONE hard release gate: package-lint E6 caps PAGE_SCAN at JSON.stringify(schema).length <= 3700 and it measures 3223 today. The build both spends and buys headroom in the same edit.'
---

# Build #1 — page-scanner corrections + waste removal

## Intent

The full-lint page scanner (`skills/vlt-setup/assets/workflows/vlt-lint-full.js`) carries two
proxy claims this cycle exists to retire, and two accretions it never used.

1. It reads **raw page text as a proxy for link structure**. `outbound_links` is described as
   *"every outbound link"* with no shape predicate and no code-span exclusion, so a page
   teaching DQL syntax reports ten broken links it does not have (A12-1 — ten of ten flags
   false on the 2026-08-24 full run; nine code-span, one bare filename).
2. It reads **frontmatter validity as a proxy for attestation**. `frontmatter_valid` is a
   model judgment made against the merged `frontmatter` convention, which genuinely defines
   `verified_by:` — so a page with no attestation surfaces under `malformed_frontmatter`
   *and* `unmarked_supersessions` *and* the attestation slots at once, inflating counts the
   factory reads as signal (A12-2 — 18 + 2 duplicate entries the executor folded back by
   hand). The correct answer is already computed deterministically ten lines away:
   `attested = (s) => !!(s.verified_by && s.verified_at)` at `vlt-lint-full.js:482`.
3. It pays for reads and fields nobody consumes: the `wiki-index` convention read in the page
   scanner (nothing in that prompt judges against it — the category↔H2 binding is computed in
   JS), and `key_claims`, bought at scan time and then discarded because the cluster prompt
   re-reads every page live (A11-11 direction 1).

All four edit **one block** — `pageScanPrompt` at `:200-202` and the `PAGE_SCAN` schema at
`:130-160`. That is why they are one build: split across builds, the second rewrites the
first's work (roadmap §Grouping, clerk-drafted and owner-adopted).

**All rejected alternatives in the parent filings and in the ideation rulings are settled —
do not re-litigate.** In particular: A12-1's **cause** fix (a deterministic pre-pass
instrument handing the workflow a slug → links map) is **declared for Cycle 13**, not folded
here (Q1 as amended Round 7, Q8b); A11-11 **direction 4** is declared for Cycle 13; direction
3 is not taken; `key_claims` is **dropped, not gated** (owner ruling R-3, `ST-3`'s standing
anti-direction against sampling); and Q6's clause homes in `write-verification.md`, not
`frontmatter.md` (owner ruling R-2 / amendment A8 — Winston and Amelia dissent on *home*,
not on *grade*).

## Brief-time dispositions

1. **The cache-hostile prompt reorder is DROPPED. It is a no-op, and A6 said to confirm or
   drop it.** A11-11 direction 1 proposed reordering `pageScanPrompt` invariant-first so the
   prompt prefix becomes cacheable. Roundtable A6 required the brief to confirm the prefix
   clears the cache floor. **Measured at HEAD this session:** `pageScanPrompt` is 2,803 B
   total; the variable head (`${p.path}` / `${p.slug}`) is the first **100 B**, so the
   invariant remainder available for a cacheable prefix is **2,703 B ≈ 676 tokens**. The
   cache minimum is **1,024 tokens** (2,048 on Haiku), and `:94` defaults `scanModel` to
   `'haiku'`. The prefix does not clear the floor under either threshold, and F6's reduction
   of `:202` shrinks it further. **Per A6 the reorder is dropped**, and this disposition is
   the record so Cycle 13 does not re-propose it without new numbers. *(A6 / Builder.)*
2. **A4's reduction of `:202` is bounded by a required-field guard.** A4 rules `:202` — 1,128 B,
   40% of the prompt, ×147 agents ≈ 166 KB/run — down to *"what the schema cannot carry"*,
   because the runtime delivers `PAGE_SCAN` as `schema:` and `:202` re-states five field
   descriptions verbatim. The brief adopts A4, **with a bound it does not state**: the
   reduction is only correct if every one of `PAGE_SCAN`'s **14 required fields** still comes
   back populated. F6 therefore carries the reduction *and* Verification 3 makes a populated
   14-of-14 return the pass condition of the reader probe. If the probe shows a required field
   degrading, the builder restores the minimum text that recovers it and records it as a
   numbered deviation — never silently.
3. **The A12-1 clauses CITE `frontmatter.md` rule 5; they do not restate it, and they carry
   their source marker.** A3 established that `frontmatter.md:37` already states the rule
   (*"Never wrap a wikilink in backticks anywhere a link is intended"*) and that the DQL pages
   **were complying** — this is a contradiction repair inside one prompt, not a new rule. Per
   the workflow's own R4 fan-out currency rule (`vlt-lint-full.js:16-21`), the restated
   instruction carries an inline `per frontmatter@13` marker (A9); the attestation clause
   carries `per write-verification@3`. Both conventions are already in the scanner's
   `convRead` set and already pinned at `:11`.
4. **`checks.md:13` is in scope as a grounding addition — scoped mode carries the same
   defect.** The roadmap's build-1 site list names only the workflow and the convention. But
   *Missing targets* is a **both-modes** check whose single home is
   `skills/vlt-lint/references/checks.md:13`, and scoped mode does not run the workflow at all
   (`vlt-lint/SKILL.md` Step 2 reads pages directly). Fixing only the workflow leaves the
   false-positive class alive in scoped mode and leaves the check's own single home asserting
   the un-narrowed population. This is also what standing rule **R3** (legal response at the
   check's own single home, same build) requires of a build that changes a finding class's
   population. Scope: **one clause, citing `frontmatter.md` rule 5** — not a restatement.
   *(Judgment call made without the owner; recorded here as its disposition.)*
5. **Interim posture (R1): not applicable.** This build ships no rule, check, or finding class
   ahead of its mechanism. Every clause it writes is *narrowing* — it removes population from
   three existing classes and adds none. The mechanism (the scanner honoring the narrowed
   descriptions) is the same edit as the rule.
6. **Retirement clause — ANSWERED, substantively, and it is beat-produced.** This build
   performs the roundtable's build-1 obsolescence finding: **the model-side attestation
   judgments at `vlt-lint-full.js:144` (`frontmatter_valid` over attestation) and `:153`
   (`unmarked_supersession` over attestation), and their restatement in the prompt at
   `:201-202`, are superseded by the deterministic `attested` predicate at `:482` and the
   `attestation_census` arithmetic at `:483-491`.** The build does not merely add a guard
   beside them — F2, F3 and F6 **retire their jurisdiction**, which is why Q1 graded A12-2's
   fix *subtractive*. Marked **beat-produced** per standing rule R-B (roadmap §Obsolescence
   beat, build-1 row). Nothing else in this build's scope is a prohibition awaiting
   retirement; `frontmatter.md:37` rule 5 is **not** retired — it is the authority the new
   clauses cite.

## F-sites

Every `file:line` below was re-derived against module source **as it sits on disk today**
(2026-08-25, branch `cycle12-v0.16.0`), never trusted from the roadmap. Grounding outcomes are
marked per site. Roundtable A1 had already corrected the roadmap's v0.14.0-vintage cites; this
pass re-verified A1's corrections too, and found one further drift (F5).

### F1 — `vlt-lint-full.js:143` — `PAGE_SCAN.outbound_links` gains the shape predicate and the code-span exclusion

**Grounding: HOLDS.** Line 143 reads:

```js
outbound_links: { type: 'array', items: { type: 'string' }, description: 'raw [[wikilink]] inner text of every outbound link, verbatim; do not normalize' },
```

**The change.** Extend the description so it states **both** of A12-1's clauses — because the
filing's two defects are distinct and a code-span exclusion alone fixes only nine of the ten
flags (roadmap §Questions deliberately left to brief time, A12-1):

- **(a) shape predicate** — an outbound link is `[[ ]]`-delimited text and **nothing else**;
  bare text, a filename, or a path that is not inside `[[ ]]` is not an outbound link. *(This
  is the clause that catches the 10th flag:
  `nfl-defensive-scheme-evolution` → `2026-02-14-macdonald-defense`, a bare source filename in
  a sources list with no `[[ ]]` anywhere.)*
- **(b) code-span exclusion** — a `[[wikilink]]` inside an inline backtick span or a fenced
  code block is documentation, not a link, and is not reported (`per frontmatter@13` rule 5:
  backtick-wrapped wikilinks do not resolve, so text in that position was never a link).

Keep `verbatim; do not normalize` — the JS reduce at `:289` owns normalization.

**Why.** A12-1. Neither `:143` nor `:202` defined what a link *is*, and
`:319-320`'s three suppressions are all about whether a target **resolves**, never about
whether the source text was a link at all — so a DQL example's `[[food]]`, resolving nowhere,
is structurally guaranteed to fire.

**The pattern already exists in this prompt.** `:201` narrows the callout gate by form
(*"A callout is only the Obsidian `> [!type]` blockquote form … a bullet, heading, or plain
prose is NOT a marker"*). Mirror that shape; link extraction simply never got one.

**Budget (A2 — hard release gate).** See §Registration. This description grows; F4 pays for it.

### F2 — `vlt-lint-full.js:144` — `PAGE_SCAN.frontmatter_valid` loses jurisdiction over attestation

**Grounding: HOLDS.** Line 144 reads:

```js
frontmatter_valid: { type: 'boolean', description: 'frontmatter present and well-formed' },
```

**The change.** Add the negative clause: absent `verified_by:` / `verified_at:` is **not** a
frontmatter-validity defect (`per write-verification@3` §Scope rule) — attestation is reported
through the `verified_by` / `verified_at` values this same schema already extracts verbatim at
`:140-141`.

**Why.** A12-2's cause fix, ruled by **Q1** (Round 1). The convention genuinely defines
`verified_by:` (`frontmatter.md:78`, `:82`), and `:201` tells the scanner to judge validity
*"against the MERGED rules"* of that file — so an agent reading a block with no `verified_by:`
had every reason to answer *no*. **The 18 entries were the prompt working as written.** The
deterministic answer already exists at `:482` and feeds `attestation_census` (`:483-491`) and
the `unattested_write` slot (`:522`); the defect is that a second, model-made judgment answers
the same question in parallel with nothing saying which wins.

**Out of scope at this site:** `frontmatter_issue` (`:148`) is untouched — it explains a
genuine validity failure and is correct as written.

### F3 — `vlt-lint-full.js:153` — `PAGE_SCAN.unmarked_supersession` loses the same jurisdiction

**Grounding: HOLDS.** Line 153's description is broad enough to absorb an attestation
complaint: *"silently-updated/conflicting claims lacking a `[!superseded]`/`[!stale]` callout,
or consensus claims lacking citations"*. The two live misroutes were `acotar-world-building`
and `katsuo-dashi`.

**The change.** Add: a missing or stale attestation is **never** an unmarked supersession
(`per write-verification@3` §Scope rule).

**Why.** A12-2's second leak path. `:510` collects this array verbatim into
`unmarked_supersessions`; nothing downstream can tell a misroute from a real finding.

### F4 — `vlt-lint-full.js:155` and `:404` — `key_claims` is DROPPED from both sites

**Grounding: HOLDS** (A1's correction re-verified: the cluster prompt is `:402-406`, **not**
`:369-370` — `:371` is the *index* pass).

**The change**, in one edit:

- Delete the `key_claims` property at `:155`. *(It is **not** in `PAGE_SCAN.required` at
  `:133` — verified — so nothing else needs touching in the schema.)*
- Delete the `Key claims already extracted: …` sentence at `:404` from `clusterPrompt`.
- `:403`'s live re-read (*"For each, read its LIVE path"*) **stands** — it is what makes the
  drop safe.

**Why.** A11-11 direction 1: `key_claims` is bought at scan time (×147 agents) and then
discarded, because the cluster prompt re-reads every page live anyway. **Owner ruling R-3
(amendment A5): DROP the field, do not gate the cluster on it** — gating is *sampling*, which
`ST-3`'s standing anti-direction forbids unconditionally, and cluster membership is only
knowable after the scan. *Dissent on record: Amelia and Victor would gate the cluster and drop
the live re-read instead. Ruled against; do not re-open.*

**This is also the E6 budget's funding.** Measured with the E6 extractor at HEAD:
`PAGE_SCAN` = **3223**; with `key_claims` removed = **3081**. The drop buys **142 chars**, so
F1/F2/F3's clauses spend against **619 chars** of headroom, not 477.

### F5 — `vlt-lint-full.js:201` — the `wiki-index` convention read leaves the page scanner; the pin STAYS

**Grounding: HOLDS, with one drift correction.** `:201` reads
`${convRead('frontmatter')}; ${convRead('wiki-supersession')}; ${convRead('wiki-index')}; ${convRead('write-verification')}`.

**The change.** Drop **`${convRead('wiki-index')}`** from `pageScanPrompt` at `:201` only.

**Do NOT touch:**
- the `// depends_on:` asset ack at `:11` — `"wiki-index@2"` **stays pinned**;
- `wiki-index.md:12`'s `consumers: [vlt-ingest, vlt-lint, vlt-lint-full.js]` — **unchanged**;
- `indexPrompt` at `:371`, which still judges the index against `wiki-index.md` and is what
  keeps the pin honest.

**Why.** A11-11 direction 1, and amendment A7: nothing in `pageScanPrompt` judges against
`wiki-index.md`. The scanner returns `category:` **verbatim**; the strict category↔H2 binding
is computed in JS from `INDEX_SCAN.h2_headings`. **Measured waste:** 8,133 B × 147 agents ≈
**1.2 MB/run** of convention text read for nothing.

> **⚠ Grounding correction (site drift).** Amendment A7 cites the JS binding at
> `:514-516`. At HEAD it is **`h2set` built at `:496`** and consumed at **`:516`**
> (`category_no_match`). The finding is unchanged and Quinn's check still holds clean — the
> drop breaks nothing — but the F-site's cite is `:496` + `:516`. *(This is the fifth
> line-cite drift this cycle has caught; it is already filed as out-of-scope item 4, §Out of
> scope below.)*

**Obligation (A7, and the workflow's own R4 rule at `:16-21`):** this edit changes the read
list, so the build **re-runs the fan-out audit** — every ask in the file checked against the
convention set its scanner receives — and **records in the `status:` line that the
`wiki-index@2` pin survives on `:371`'s strength.** See Verification 4.

### F6 — `vlt-lint-full.js:202` — reduced to what the schema cannot carry, and the two new clauses stated ONCE

**Grounding: HOLDS.** `:202` is **1,128 B — 40% of the 2,803 B prompt**, ×147 agents ≈
**166 KB/run**. It re-states `PAGE_SCAN` field descriptions the runtime already delivers as
`schema:` — `outbound_links`, `category`, `topic_is_list`, `summary`, `name_callout_targets`
are all described at `:143`–`:159` **and again** at `:202`.

**The change** (amendment A4, bounded by brief-time disposition 2):

- **Keep** what the schema cannot express: the page-scoping instruction (*"Return ONLY
  findings about THIS page"*, *"Do not assess other pages — cross-page checks happen later"*).
- **Delete** the verbatim re-statements of field descriptions that `:143`–`:159` already
  carry. The schema is the field contract; the prompt is the *rules* contract.
- **State A12-1's and A12-2's clauses once.** They live at `:143` / `:144` / `:153` (F1–F3).
  Where a prompt-side statement of the extraction rule genuinely helps the model — a judgment
  the builder makes against the probe in Verification 3 — it appears **once**, in the rules
  half of `:201`, with its `per frontmatter@13` / `per write-verification@3` marker (A9),
  never duplicated across `:201` and `:202`.
- **Do not touch** `:201`'s Gap B conditional, the frontmatter@13 rule-4 normalization
  paragraph, or the callout-form gate — those are rules, not field descriptions, and they are
  the pattern F1 mirrors.

**Why.** Amendment A4 (Builder): *"`:202` is the biggest waste in the file and is unlisted."*
It is also the reason A12-1 and A12-2 must not each add prose here — `ST-3`'s *ratcheted
caution* root cause is *"every honesty repair correctly added coverage guards; none of them
ever removed work."* This build is the first that removes.

**Cost frame, recorded so the next reader does not re-merge two pools** (Q1's grounding note):
the prompt string is 2,803 B/agent ≈ 414 KB/run — **not** `ST-3`'s 58,531 B/agent, which is
the *convention read* (8.6 MB/run) that direction 4 retires and this build only dents by
1.2 MB via F5. `cost_accounting`'s `scanPromptChars` (`:236`) measures the prompt pool only,
and the live report's own `cost_accounting.note` says so.

### F7 — `write-verification.md:53-55` — §Scope rule (self-marker) gains the jurisdiction boundary

**Grounding: HOLDS.** `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md`
is `version: 3` with `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js]`
(`:11-12`). `## Scope rule (self-marker)` is at **`:53`**, its body at **`:55`**.

**The change.** Append one clause to the Scope rule paragraph, in the shape of its
sibling boundary clause at `frontmatter.md:84` (*"Not the `trust:` rung … Same word, orthogonal
axes"*): **attestation is out of frontmatter-validity jurisdiction.** A file's missing or stale
attestation is an attestation finding — it is never a frontmatter-validity defect and never an
unmarked supersession. Frontmatter validity judges the base schema
(`frontmatter.md` §Base frontmatter); attestation is judged by this file's rule, against the
`verified_by:` / `verified_at:` fields `frontmatter.md:73-84` defines.

**Why, and why HERE.** **Q6, RULED Round 6: IN, as a prose clarification — no bump, no
re-ack.** The capture over-priced it as a rule change; the clause does not change what any
convention *asserts* — `frontmatter.md:74-84` never conditions validity on attestation, and the
scope rule plus the pre-adoption posture are already single-homed at
`skills/vlt-lint/references/checks.md:16`. Per CLAUDE.md's version-handshake rule, *prose
clarifications don't bump*.

**Owner ruling R-2 / amendment A8 moved the home**, and it is binding: `frontmatter.md:74`
opens its own attestation section by **disclaiming scope** — *"This section defines only the
**fields**; the checklist, fail-open rule, **scope rule**, and audit contract live in
`write-verification.md`"* — and `checks.md:16`, which Round 6 named as the single home, is
itself a **pointer there**. The rehome also makes the clause cheaper: `write-verification.md`
is v3 with 5 consumers against `frontmatter.md`'s v13 with 9.

> **DO NOT write this clause into `frontmatter.md`.** Paige's stronger form is on record as the
> risk: no shipped file defines *"frontmatter validity"* as a term, and `:201` tells the scanner
> to judge validity against the **merged** rules of `frontmatter.md` — so excluding a section
> *there* would narrow what the convention asserts, and **that would be a rule change: 13 → 14
> and nine re-acks.** R-2 exists to avoid exactly that. Dissent on record: Winston and Amelia
> each re-tested Round 6 independently and confirmed it holds *as written*; **they lose on
> home, not on grade.** Do not re-open either half.

### F8 — `skills/vlt-lint/references/checks.md:13` — *Missing targets* narrows its population (grounding addition)

**Grounding: EXPANDED — see brief-time disposition 4.** `:13` currently reads *"`[[wikilinks]]`
pointing at targets that don't exist anywhere"*, and its three suppressions (cross-layer target,
index-registered stub) are all about **resolution**, exactly mirroring `:319-320`.

**The change.** One clause narrowing the population, citing the existing authority rather than
restating it: a `[[wikilink]]` inside an inline code span or a fenced block is **not** an
outbound link and is never a missing target (`{conventions}/frontmatter.md` rule 5 — backtick-
wrapped wikilinks do not resolve, so they were never links); nor is bare text that is not
`[[ ]]`-delimited. **The legal response is unchanged** — it still applies per genuinely-missing
link.

**Why.** *Missing targets* is a **both-modes** check. Scoped mode never runs
`vlt-lint-full.js`, so a workflow-only fix leaves the false-positive class alive there and
leaves the check's single home asserting the un-narrowed population. This is standing rule R3
(legal response at the check's own home, same build) applied to a population change.

**Out of scope at this site:** `checks.md:16` (Attestation findings) is **not** edited — it
already points at `write-verification.md` for the scope rule, and F7 is what that pointer now
resolves to. `checks.md:34` (Unmarked supersessions) is **not** edited — same reason. Adding a
second statement of the boundary at either site would violate single-home discipline.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row, no `marketplace.json` entry.
No convention `version:` moves and no `consumers:` list changes, so **no consumer walk and no
re-ack** — `write-verification.md` stays `version: 3` / 5 consumers (Q6, R-2), `frontmatter.md`
stays `version: 13` / 9 consumers (untouched), `wiki-index.md` stays `version: 2` / 3 consumers
(F5 — the pin and the consumers entry both survive on `:371`'s strength).

**"No bump owed" is not "no cost."** The gates this build's edits actually touch:

- **🔴 package-lint E6 — schema-size budget. THIS IS THE BUILD'S HARD GATE.**
  `tools/package-lint.py:900` sets `SCHEMA_SIZE_BUDGET = 3700` and measures every fan-out
  output schema with a node subprocess reproducing `JSON.stringify(schema).length`. **Measured
  at HEAD this session: `PAGE_SCAN` = 3223** (INDEX_SCAN 823, CLUSTER_FINDINGS 1630,
  PAIR_FINDINGS 376). F4's `key_claims` drop takes it to **3081**, so F1 + F2 + F3 have
  **619 chars** of headroom. Q1 priced the symptom fix at *"~400–500 B"* on the **prompt**
  side; written at that scale on the **schema** side it fails the tag (A2). Write the schema
  clauses tight, and measure — Verification 1.
- **package-lint E5 — asset-node handshake.** `vlt-lint-full.js:11`'s `// depends_on:` header
  is the workflow's own ack line and E5 parses it. F5 **does not change it**; E5 must still
  pass, and the fan-out audit (Verification 4) is what makes leaving it unchanged honest.
- **package-lint E1 / E3** — unaffected (no `consumers:` edit, no new `name@version` token).
- **package-lint C6** — not applicable: this build does not touch
  `governance/_meta/vault-operating-contract.md`, so no `vault-rule-card.md` sha256 re-derive
  is owed. *(That obligation is build-3's — roadmap A27.)*
- **package-lint E4 / standing rule R2 (fixture extension)** — not applicable: no release-gate
  check is added or changed, so no `tools/test-package-lint.py` case and no `CASE_FLOOR` bump.

## Out of scope (dispositioned)

1. **A12-1's cause fix — a deterministic pre-pass instrument extracting `outbound_links` in
   JS.** *Declared for Cycle 13* (Q1 as amended Round 7 / Q8b), not deferred. Grounding
   correction on record: it is **not** available as a JS refactor — `vlt-lint-full.js:32`
   receives `pages: [{ slug, path }]`, paths only, and the file contains no `fs` and no file
   read; page text reaches only the fan-out agents. It needs a stdlib pre-pass the SKILL runs
   at Step 0 (precedent: `skills/vlt-setup/assets/hooks/vlt-vitals.py`). *The roundtable's one
   correction to that correction, carried forward: the SKILL **does** have filesystem access
   and already runs pre-passes of that class, so what Cycle 13 owes is **determinism**, not a
   home (A6/Amelia).*
2. **A11-11 direction 4 (scanner-card projection).** Declared for Cycle 13 (Q8b). Note for
   that ideation, per A51: **direction 2 retires direction 4's own cost case** — a cached page
   is never scanned, so its agent never reads a convention; at `churn 5 of 146` the 8.6 MB
   pool falls to ~0.29 MB/run. Rule it on `ST-3` cause (a), not on the stale number.
3. **A11-11 direction 3.** Not taken (Q8b).
4. **A11-11 direction 2 (the change-keyed findings cache).** Build-2, which **queues behind
   this build and behind build-3** (roundtable A11). This build is one of the two reasons:
   it redefines `outbound_links` and `frontmatter_valid`, so any sidecar populated before it
   lands holds findings adjudicated under a retired ruleset (A10 — the cache key must carry a
   `pageScanPrompt` + `PAGE_SCAN` fingerprint). **Build-1 changes that fingerprint; say so in
   the build commit** so build-2's brief can cite it.
5. **`coverage_caps` is NOT retired or trimmed here** (A16) — `ST-3` anti-direction 2 stands.
6. **The prompt reorder** — dropped, with measurements: brief-time disposition 1.
7. **Gating the cluster pass on `key_claims`** — ruled against (R-3 / A5); the dissent is on
   record and is not re-opened.
8. **A pattern already filed, not re-raised here:** *the loop's line-number cites go stale
   silently* — two v0.14.0 cites survived a capture and nine ideation rounds (A1/A4), and F5
   found a third at HEAD. Roadmap §Out-of-scope material item 4; candidate fix is
   cites re-verified at brief time, which is what this section documents happening.

## Verification (unit, at rest — lifecycle step 5)

1. **🔴 E6 schema-size measurement — the gate, measured before and after (A2).** Run the
   release gate's own instrument, not a hand count:
   `uv run tools/package-lint.py` (Group E) — and for the isolated figure, the same node
   extractor package-lint uses, against `skills/vlt-setup/assets/workflows/vlt-lint-full.js`.
   **Record the four schema lengths in the `status:` line.** Baseline at HEAD: `PAGE_SCAN`
   3223 → post-`key_claims`-drop 3081 → post-edit **must be ≤ 3700**. If it is not, tighten
   the `:143`/`:144`/`:153` descriptions — never raise the budget.
2. **Packaging lint, mid-cycle:** `uv run tools/package-lint.py` Groups **A/B/C/E** all PASS.
   (`--expect-version` / Group D is the **release** gate, not this build's — this is **not**
   the release build; the dual version bump rides the cycle's release per D3, one release for
   the whole cycle.)
3. **The scanner reader probe — the instrument of record for acceptance check 2.** Dispatch
   **one** agent with the **edited** `pageScanPrompt` text and `PAGE_SCAN` schema (`model:
   'haiku'`, matching `:94`'s default) against a temp fixture page carrying, deliberately:
   (a) a fenced DQL block with `FROM [[note]]` and `FROM outgoing([[note]])`; (b) an
   `![[File.base]]` embed inside an inline code span; (c) a table row containing `[[food]]`
   and `[[exercise]]` in code spans; (d) a prose `## Sources` section listing a **bare
   filename** (`2026-02-14-macdonald-defense`) with no `[[ ]]`; (e) exactly **two genuine**
   body wikilinks outside any code context; (f) frontmatter with **no** `verified_by:` /
   `verified_at:` and otherwise valid base frontmatter. **Pass conditions, all four:**
   `outbound_links` contains **exactly** the two genuine links (a–d contribute zero);
   `frontmatter_valid` is **true**; `unmarked_supersession` carries **no** attestation
   complaint; and **all 14 required fields return populated** (brief-time disposition 2's
   guard). Record the returned JSON verbatim in the `status:` line.
4. **The fan-out audit (the workflow's own R4 currency rule, `vlt-lint-full.js:16-21`; A7).**
   Re-run it because F5 changes the read list: walk **every** ask in the file and check it
   against the convention set its own scanner receives. **Record the result explicitly,
   including that `wiki-index@2`'s pin at `:11` survives on `indexPrompt`'s (`:371`) strength
   and that `wiki-index.md:12`'s `consumers:` entry is therefore still true.** Every restated
   convention instruction in an edited prompt carries its inline `per <convention>@N` marker
   (A9).
5. **Standing rule R3 (legal response at the check's own home):** `checks.md:13`'s legal
   response is present and unchanged after F8's population narrowing; `checks.md:16`'s
   attestation legal responses are present and unchanged; the boundary is stated **once**, in
   `write-verification.md` (F7).
6. **Standing rule R4 (enumeration widening): not applicable** — this build adds no file to
   any enumerated class. It **removes** a convention from one prompt's read list (F5), which
   is the enumeration *narrowing* case, and Verification 4 is its audit.
7. **Greps, cross-file agreement:**
   - `grep -c "key_claims" skills/vlt-setup/assets/workflows/vlt-lint-full.js` → **0**.
   - `grep -c "convRead('wiki-index')" skills/vlt-setup/assets/workflows/vlt-lint-full.js` → **0**;
     `grep -n "wiki-index" …/vlt-lint-full.js` → `:11` (the pin), `:168`, `:371` only.
   - `grep -n "verified_by" skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md`
     → the new Scope-rule clause plus the pre-existing `:47` / `:66` references; and
     `grep -n "^version:" …/write-verification.md` → **still `version: 3`** (no bump), with
     `consumers:` unchanged at 5.
   - `grep -rn "frontmatter-validity\|frontmatter validity" skills/` → the boundary stated in
     **one** place (`write-verification.md`), plus the workflow's schema/prompt clauses that
     *cite* it — no second full statement (single-home discipline).
   - `grep -c "per frontmatter@13\|per write-verification@3" skills/vlt-setup/assets/workflows/vlt-lint-full.js`
     → every restated convention instruction carries its marker (A9).
8. **Harness sanity run (the build-5 / build-8 precedent).** Load the shipped workflow source
   with stubbed runtime globals (`agent`, `parallel`, `phase`, `log`, `budget`), `args`
   delivered **as a JSON string** (the runtime contract — CLAUDE.md's parse-on-intake rule), a
   3–4 page fixture set with **scripted** scan results. Assert the reduce is unchanged by this
   build: `missing_targets` (`:319-320`), `malformed_frontmatter` (`:543`),
   `unmarked_supersessions` (`:510`), `attestation_census` (`:483-491`) and `cost_accounting`
   all still populate correctly, and that `clusterPrompt` composes without `key_claims`.
   Record the output.
9. **Scrub** — no personal or vault-local content in any changed shipped file; no live-vault
   artifact paths in any worked example (CLAUDE.md, Git & publishing).
10. **Housekeeping** — delete any `.decision-log.md` the build session produced before
    committing (CLAUDE.md standing rule; they are gitignored but `vlt-upgrade`'s own-the-apply
    is a filesystem copy).

**`status:` on completion.** Rewrite the frontmatter `status:` to a BUILT record:
`BUILT <date> — <what landed>; <verification results, incl. the four E6 schema lengths, the reader-probe JSON, the fan-out audit result and the harness output>. Deviations/notes: (1) … (2) …`
with **numbered** deliberate deviations. One commit for the build.

## Release

Not applicable — this is **not** the release build. Per **D3 (Round 7): ONE RELEASE, WHOLE
CYCLE**. The dual version bump
(`.claude-plugin/marketplace.json` `"version"` + `skills/vlt-setup/assets/module.yaml`
`module_version`), the `uv run tools/package-lint.py --expect-version X.Y.Z` gate and the
ff-merge → tag → push sequence ride the cycle's **last** build (build-2 — order is
**1 → 3 → 2**, roundtable A11).

## Acceptance (live — appended to the roadmap ledger)

1. **`[ship-verifiable]` — GATES closeout. The schema stays inside the E6 budget.**
   `JSON.stringify(PAGE_SCAN).length ≤ 3700` after the edits. **Instrument:** package-lint
   Group E6 (`tools/package-lint.py:900`, the node-subprocess measurement), run at rest;
   baseline 3223 at HEAD, 3081 after `key_claims` is dropped. **Evidence:** the four measured
   schema lengths recorded in the brief's `status:` line and the Group E PASS line.
2. **`[ship-verifiable]` — GATES closeout. The narrowed extraction actually holds on a page
   built to break it.** Given the edited prompt + schema, a scanner returns **exactly** the
   two genuine wikilinks from the Verification-3 fixture (fenced DQL, code-span embeds,
   code-span table cells and a bare source filename all contribute **zero**),
   `frontmatter_valid: true` on an unattested-but-valid page, no attestation complaint in
   `unmarked_supersession`, and all 14 required fields populated. **Instrument:** the
   Verification-3 single-agent reader probe against the temp fixture, factory-side and at
   rest; an agent-run check, named here as the instrument with its inputs and pass conditions.
   **Evidence:** the returned JSON recorded verbatim in the brief's `status:`.
3. **`[ship-verifiable]` — GATES closeout. The waste is gone and the handshake survived it.**
   `key_claims` absent from both `:155` and the cluster prompt; `convRead('wiki-index')` absent
   from `pageScanPrompt` while `wiki-index@2` stays pinned at `:11` and `wiki-index.md`'s
   `consumers:` still lists `vlt-lint-full.js`; `:202` reduced with the required-field guard
   met; `write-verification.md` still `version: 3` with 5 consumers (no bump, Q6/R-2).
   **Instrument:** the Verification-4 fan-out audit + Verification-7 greps + package-lint
   Groups A/B/C/E (E5 parses the asset ack line; E1/E3 confirm no stray pin). **Evidence:**
   the recorded audit result, grep outputs and PASS line.
4. **`[field-contingent]` — the ten false missing-target flags do not return on real content.**
   The next real full lint reports **zero** `missing_targets` entries sourced from a code span
   or from bare non-wikilink text — measured against the same corpus that produced ten of ten
   false flags on 2026-08-24. **Discharging event:** the owner runs `vlt-lint --full` on
   `{field-vault}` after upgrading it to this cycle's release. **Who performs it:** the owner
   (the standing rule — the owner runs upgrades and lint sweeps). **Which vault:**
   `{field-vault}`, the primary field vault; it is the only vault carrying the
   obsidian-dataview / obsidian-bases pages that produce the class, so no other install can
   discharge this. **Bound:** the first full lint after the release, and no later than Cycle
   13's `inbox-capture`.
5. **`[field-contingent]` — attestation is reported once, in its own home.** On that same run,
   a page missing `verified_by:`/`verified_at:` appears in the attestation slots
   (`unattested_write` / `attestation_census`) and **not** in `malformed_frontmatter` and
   **not** in `unmarked_supersessions`; the census reads correctly **without the executor
   folding duplicates back by hand** — the 2026-08-24 run needed 20 folded by hand.
   **Discharging event / performer / vault:** as check 4. **Bound:** as check 4.
6. **`[field-contingent]` — the waste removal shows up in the instrument that can see it.**
   On that same run, `cost_accounting.phases[Scan pages].prompt_chars` is materially below the
   2026-08-24 baseline at comparable `pages_total`, consistent with `:202`'s reduction.
   **Stated honestly, and this is why it gates nothing:** the 1.2 MB/run `wiki-index` saving
   is **agent-side** and is invisible to `cost_accounting` by that instrument's own declared
   blind spot (`:127` — *"agent-side file reads … are not visible from JS"*). Do not grade the
   convention-read saving from this number. **Discharging event / performer / vault:** as
   check 4. **Bound:** as check 4.

---

**Next lifecycle move:** **`brief build 3`** (`build-brief`) — order is **1 → 3 → 2**;
build-2 is briefed and built last. This brief is **BUILT** (2026-08-25, one commit on
`cycle12-v0.16.0`): Verification 1–10 run at rest, the three ship-verifiable acceptance
checks all met, seven numbered deviations on the `status:` line. Its three field-contingent
checks (4–6) wait on the owner's next `vlt-lint --full` after the cycle release.
*Restamped by the builder on exit, per the lifecycle map's standing rule that a report's
terminal routing line is authoritative — the line it replaced still routed to the build
that had just run.*
