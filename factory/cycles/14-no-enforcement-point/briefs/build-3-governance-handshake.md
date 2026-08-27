---
title: 'Build #3 — governance: the PARA type vocabulary gets a named owner, the attestation roster gets a class it can honestly exempt, and the handshake gets an enforcement point that can see prose'
status: >
  BUILT 2026-08-27 — every F-site landed; **all 5 at-rest acceptance checks PASS**; (6) and (7) are
  bound to the release-2 `{field-vault}` upgrade post-flight / first full sweep and are UNFILLED by
  construction. Version bump NOT taken — it rides build-4 / `vlt-release`. Branch `cycle14-release2`.

  **Sites changed — 11 shipped files + 2 tools files.**
  `.../governance/_meta/conventions/write-verification.md` (F1): `:11` `version: 3 → 4`; `:55` the
  jurisdiction sentence gains the operational-record class exemption cited to `extraction.md`,
  *PARA containers* (a **section** pointer, never a `file:line` — disposition 5) plus the
  by-class-never-by-writer clause. `:47`, `:38`, `:51` and the Jurisdiction-boundary sentences
  byte-identical. `:12` consumers: unchanged (5).
  `.../conventions/extraction.md` (F2): `:11` `version: 7 → 8`; **`:84` NEW** — the closed
  recognized-`type:`-set statement for the PARA population (the sentence `contract:66` now points
  at), naming `frontmatter.md`'s list as governing the base/agent lane only and routing a
  module-canonical non-PARA type in a PARA folder to retype-or-relocate; **`:190` NEW** — the
  operational-record class widened from filename position to a Layer-3 artifact class; `:192` the
  A15-falsified grounding sentence RETIRED and replaced (members of the recognized set stated in
  this file). `:118`, `:80-84`, the trust ladder untouched. `:12` consumers: unchanged (4).
  `.../conventions/frontmatter.md` (F3): `:11` `version: 13 → 14`; `:71` gains **`moc`** and scopes
  the open-vocabulary clause to the base/agent lane, pointing the PARA population at `extraction.md`
  (pointer, never a restatement of the set). `:294`/`:296` `local_consumers:` untouched. `:12`
  consumers: unchanged (10).
  `.../governance/_meta/vault-operating-contract.md` (F4, no bump — deliberately unhandshaked):
  `:66` the `type:` leg names its owner (**A14-6's whole repair**) and the attestation-pair leg is
  qualified to knowledge artifacts; `:70` the carve-out widened from container files to the class.
  `:64`, `:155`, `:325` (build-2's) untouched.
  `.../governance/_meta/vault-rule-card.md` (F4): `:26`'s act-blocking clause EDITED (not merely
  re-hashed) — the over-broad *"attestation pair"* now carries the class exemption and the
  `extraction.md` pointer; `:11` `derived_from:` re-stamped to
  `sha256:928583a432ecd9735d7b88f04dab06d84922d00e603b0576d5be581f0405b752 (derived 2026-08-27)`.
  Card **7,250 bytes** of `RULE_CARD_BUDGET` 8,000 — 750 headroom.
  `skills/vlt-lint/references/checks.md` (F5): `:17` the Population carve-out widened to the class
  (container files **plus any `para_*` file carrying `type: record|register`, container-sited or
  not**), the missing pre-adoption clause added with its per-file window, and R3's legal response
  restated as retype / attest / human-authored + pre-adoption informational; `:19` the recognized
  set demoted from **definition** to pointer at `extraction.md` (named for the reader, no longer
  owned) and `para_type_unknown`'s legal response rewritten to the **owner-ruled three routes**
  (a) vault-grown → overlay-declare, (b) module-canonical-but-non-PARA → retype to the target-folder
  type or relocate, never overlay-declare module vocabulary, (c) otherwise → relocate out of PARA.
  `:14`/`:15` (build-1's), `:18`, `:20`, `para_author_unknown` byte-identical.
  `skills/vlt-lint/references/report.md:32` (F6): the slot placeholder gains the class exclusion and
  the informational clause. `:3`/`:13` (build-4's) and `:77`/`:88` (build-2's) untouched.
  **F7 — the consumer walk, 19 ack tokens across 11 files:** `vlt-dispatch:3`, `vlt-extract:4`,
  `vlt-groom:3`, `vlt-ingest:4`, `vlt-lint:4`, `vlt-mint:3`, `vlt-query:4`, `vlt-research:3`,
  `vlt-setup:3`, `vlt-track:4` (re-derived, not copied — deviation 1), and
  `vlt-setup/assets/workflows/vlt-lint-full.js:11`. `wiki-index@2`, `wiki-supersession@2`,
  `wiki-consolidation@1`, `spec@2`, `consult@1`, `decision-log@4` untouched.
  **F8 — `vlt-lint-full.js`, nine tokens, zero content edits:** `:11` header (E5) plus the eight
  in-prose tokens at `:171`, `:178`, `:182`, `:229` ×3, `:682`, `:684`. File stays **870 lines**;
  `node --check` clean. Nothing else in the file touched.
  **F9 — `tools/package-lint.py`:** `_e7_asset_prose_pin_currency(root, conventions)` added at
  `:851`, wired into Group E at `:1097` after `_e5_asset_nodes`; `tools/test-package-lint.py`: case
  **24** added, `CASE_FLOOR` `23 → 24` at `:229`.

  **Verification, actually run.**
  **V1 — bipartite consistency, BOTH directions, all 19 pairs: CONSISTENT, 0 defects.** Verified by
  an independent walk that re-reads `version:`/`consumers:` from the three conventions and
  `depends_on:` from the ten SKILL.md files + the workflow's `// depends_on:` header, and asserts
  (a) every listed consumer acks at the convention's current version and (b) every acker appears in
  that convention's `consumers:`. `write-verification@4` → 5/5; `frontmatter@14` → 10/10;
  `extraction@8` → 4/4. **19 pairs checked, 0 mismatches, 0 unlisted ackers.** Group E's E1+E5 agree
  independently (V8).
  **V2 — E7 built, inventoried, and PROVEN able to fail.** E4's structural introspection now returns
  a **16-check** inventory including `_e7_asset_prose_pin_currency`, covered by case 24, **zero
  uncovered checks**; `len(CASES)` 24 = `CASE_FLOOR` 24. `uv run tools/test-package-lint.py` →
  **24/24 cases green.** Beyond the fixture, the check was exercised against the **shipped**
  workflow: each of the **eight** in-prose tokens was mutated in turn to a wrong version, package-lint
  run, and restored — **8/8 CAUGHT**, each naming its own `file:line`, and the tree returns to exit 0
  after every restore. Verbatim, the `:684` mutation:
  `asset prose pin: skills/vlt-setup/assets/workflows/vlt-lint-full.js:684 recites
  write-verification@3 but the file's \`// depends_on:\` header acks write-verification@4 — an
  in-prose pin left stale by a handshake bump ships a wrong citation to every vault; move the body
  token with the header` → `package-lint: FAIL (E)`. The **reverse drift** leg (a body pin naming a
  convention the header never acked) is exercised by case 24's probe 2, and case 24 also asserts the
  **green** side (restoring the token returns exit 0) — a check that cannot go green is not an
  instrument either. `grep -c` over the shipped workflow: **5 `frontmatter@14`, 5
  `write-verification@4`, 0 `@13`/`@3`/`extraction@7` survivors.**
  **V3 — E6 re-measured with package-lint's own `_E6_NODE_EXTRACTOR`, never a source char count:**
  `PAGE_SCAN` **3688** (budget 3700 — **unchanged from build-1, 12 chars spare**), `INDEX_SCAN` 823,
  `CLUSTER_FINDINGS` 1630, `PAIR_FINDINGS` 376. **The E6 price of build-3 is ZERO, as predicted.**
  No content edit was made inside `PAGE_SCAN` (`:158-189`); the binding constraint never bound.
  **V4 — C6.** `shasum -a 256 vault-operating-contract.md` =
  `928583a432ecd9735d7b88f04dab06d84922d00e603b0576d5be581f0405b752`, matching the re-stamped
  `vault-rule-card.md:11` exactly; card **7,250 / 8,000** bytes; package-lint **Group C PASS**.
  **V5 — the substance fixture pair (E3/A33), at rest: PASS on both legs.** Reader protocol: a fresh
  agent given ONLY the four edited shipped texts (`write-verification.md` §Scope rule, `checks.md:17`,
  `extraction.md`'s class + recognized-set statements, `contract:66`/`:70`) and the two fixture files,
  told nothing else, asked for a verdict and the deciding clause.
  **SUBJECT** (`{resources}/<container-slug>/<file-slug>.md`, `type: record`, `author: agent`, no
  attestation pair, not named `record.md`, no declaring `charter.md` at or above it) → **"No
  finding."** Cited clause, verbatim: *"**Population carve-out (by artifact class, never by writer):**
  the Layer-3 **operational-record class** — container files
  (`charter.md`/`record.md`/`register.md` under a `{projects}`/`{areas}`/`{resources}` container
  directory) **and any file in the `para_*` population carrying `type: record` or `type: register`,
  container-sited or not** — is judged by the container schema"* (TEXT B, `checks.md`).
  **CONTROL** (identical but `type: resource`) → **"Yes, finding."** Cited clause, verbatim:
  *"`para_missing_attestation`: a PARA file carrying vault `type:` + `author: agent|hybrid` with no
  attestation"* (TEXT B, `checks.md`). The narrowing works and the control still flags.
  ⚠ **R2 (P-18 Tier B observer) fires and is recorded: build-3 reached for a synthetic fixture.** It
  is unavoidable and the reason is grounded, not assumed — `para_missing_attestation` has **no code
  implementation** (`vlt-lint-full.js:809` emits a structural slot; `full-scale.md:11` leaves the PARA
  scan to the SKILL), so there is nothing executable to run it against. Not a gate; named at closeout.
  **V6 — two-surface agreement (A12b): PASS.** `grep -En "operational[- ]record"` over
  `skills/vlt-setup/assets/governance/_meta/` + `skills/vlt-lint/references/` names the class at
  `contract:66`, `contract:70`, `write-verification.md:55`, `checks.md:17`, `checks.md:19`,
  `report.md:32`, `vault-rule-card.md:26` and `extraction.md:84`/`:190`/`:192`. **Defined at exactly
  one site** — `grep -rn "name an \*\*artifact class\*\*" skills/` returns **1 hit,
  `extraction.md:190`**; the other three governance surfaces cite it (each quoted in full in V6's
  output). The class definition exists in one file and nowhere else.
  **V7 — the retirements landed (P-15).** `grep -rn "ride \`frontmatter.md\`'s declared
  non-exhaustive" skills/` → **zero (exit 1)**. `frontmatter.md:71` carries the PARA scoping clause
  and `moc` (`grep -c moc` 0 → 1). `checks.md:19` reads *"defined in `{conventions}/extraction.md`,
  *`type:` mapping by target folder*, which is its single home"* — the set is cited, not owned.
  D2's manual-grep prescription is retired by E7 (V2); the roadmap's brief-time superseding note
  already records all four retirements.
  **V8 — packaging lint, mid-cycle:** `uv run tools/package-lint.py` → **`A/B/C/E PASS, D SKIPPED —
  vlt 0.16.2`, exit 0.** D SKIPPED because `--expect-version` is the release gate and rides build-4.
  **R3 — legal response:** stated at `checks.md:17` and `:19`, the checks' single home; both finding
  classes' responses changed and both are written (F5 edits 3 and 5).
  **R4 — enumeration widening:** not applicable to shipped files, as declared. The three `consumers:`
  enumerations changed **version, not membership** (V1); the recognized `type:` set gained no member;
  the skill-asset manifest is untouched. Case 24 is R2, not R4.
  **Scrub:** no personal or vault-local content in any changed shipped file — `git diff -U0 --
  skills/` greps clean for machine paths, the owner's username and the field vault's name; the V5
  fixtures live only in the session scratchpad and use `{resources}` placeholders, never a real
  install path. `find . -name ".decision-log.md"` → nothing. `tools/__pycache__` removed.

  ── ACCEPTANCE, graded at rest ──────────────────────────────────────────────
  **(1) PARTIAL — the at-rest half PASSES; the `--expect-version` half is build-4's.** Group E is
  clean over `write-verification@4`/`frontmatter@14`/`extraction@8` with **19/19 bipartite**, E5
  confirms `vlt-lint-full.js:11` acks both at the new versions, **C6 PASSES** with the card re-stamped
  and 750 bytes under budget, and **E6 measures `PAGE_SCAN` 3688 — unchanged**. `D SKIPPED` by
  construction: build-3 is not the release build. Nothing is deferred that this build could have run.
  **(2) PASS — the cycle's thesis, made enforceable.** E7 exists, is inventoried by E4 with zero
  uncovered checks, and **can fail: 8/8 shipped body tokens caught on mutation and cleared on
  restore**, plus the reverse-drift leg and the green leg in case 24. `CASE_FLOOR` 24, 24/24 green.
  `grep -c` returns 5 `frontmatter@14` / 5 `write-verification@4` / **zero** `@13`/`@3` survivors.
  **(3) PASS.** The fixture pair adjudicated by an isolated reader: subject → no finding (the widened
  Population carve-out), control → finding (the base jurisdiction clause). Both verdicts and both
  cited clauses are verbatim in V5. The 27 appear nowhere in this grade (E3).
  **(4) PASS.** `contract:66`, `contract:70`, `write-verification.md:55` and `checks.md:17` name the
  Layer-3 operational-record class in the same terms; the class is defined in exactly one file
  (`extraction.md:190`, 1 grep hit) and cited at the other three. A14-7's two-surface disagreement is
  resolved without opening a new one.
  **(5) PASS.** `contract:66`'s `type:` leg now names `extraction.md`, *`type:` mapping by target
  folder* — a section that exists (`extraction.md:72`) and now carries an explicit **closed**
  recognized-set statement (the word "recognized" went **0 → 2** occurrences in the file);
  `frontmatter.md:71` carries the PARA scoping clause and `moc`; `checks.md:19` cites the set rather
  than defining it; the retirement grep returns zero.
  **(6) UNFILLED — bounded to the release-2 `{field-vault}` upgrade post-flight.** The two
  `kind: parked-interim` entries can only be unwound after the owner upgrades. The rulings both parks
  wait on are shipped by this build.
  **(7) UNFILLED — bounded to the first full `{field-vault}` sweep after release 2.** That sweep is
  **COLD by construction** (three convention digests + `checks.md` moved, and `PAGE_SCAN`'s strings
  moved) — priced at A26, not a cache regression.

  **Deviations (numbered).**
  1. **F7's `vlt-track` line and three of F2's cited line numbers were re-derived, and two of the
  brief's cites are off.** `vlt-track`'s `depends_on:` is at **`:4`**, not an unpinned offset — the
  brief correctly refused to pin it and the re-derivation found it. Separately, **F2's "`:74-78` the
  target-folder→`type:` table + the `moc` paragraph … `:78` already names `moc`" is stale**: at
  `d641050` the section heading is `:72`, the table `:76-80`, and the `moc` paragraph **`:82`** (the
  brief's disposition 6 cites `extraction.md:72-82` for the same material and is right). The owner
  ruling's `extraction.md:74-78` inherits the same drift. No substantive consequence — the anchors
  were matched on text, never on line number, and every edit landed in the intended paragraph.
  2. **The recognized-set statement landed at `extraction.md:84`, immediately after the `moc`
  paragraph, and the operational-record class at `:190`, immediately after `register.md` and before
  the Attestation posture.** F2 says "after `:78`'s `moc` paragraph" and "in §PARA containers"; both
  are honoured in text order. Sited so a reader meets the class definition before the posture that
  cites it.
  3. **The shipped §Scope rule sentence cites `ST-1` by id, exactly as the brief's disposition-5
  replacement text writes it.** Recorded rather than silently taken: `ST-N` is a **factory** study
  register (`factory/studies/`) a vault cannot open, so this is a pointer that does not resolve in the
  field. It is not without precedent — build-2 shipped `ST-5` into `vlt-lint-full.js:303` — and the
  clause reads as a reason, not a required lookup. **Flagged for the owner** as a candidate cleanup
  (rewrite as *"permission fused to provenance"* with no id) rather than deviated from unilaterally,
  since the brief specifies the text verbatim.
  4. **E7 stays silent where E5 already fails.** A workflow whose `// depends_on:` header is missing,
  duplicated or unparseable is E5's defect; E7 `continue`s rather than reporting the same file twice.
  Stated because it is a deliberate coverage choice, not an oversight: E7's population is exactly
  "workflows with one parseable header", which is E5's green set.
  5. **Case 24 asserts the PASSING side as well as the failing side.** `brief-anatomy.md` §7 and R2
  require a case that can fail; the case additionally restores the token and asserts exit 0, and its
  probe 2 exercises the reverse-drift leg with a second fixture convention. Three assertions where
  the brief specified one — strictly additive, and the reason is in the case's own comment.
  6. **`vault-rule-card.md:26` grew 144 bytes, not the "one clause" the brief budgeted.** 7,106 →
  **7,250** of 8,000. The clause carries both the `extraction.md` pointer and the class exemption
  because F4 edit 4 names both as required; 750 bytes of headroom remain and C6 passes.
module_code: 'vlt'
created: '2026-08-27'
derives_from:
  - 'factory/inbox/2026-08-26-125529-recognized-type-names-no-owning-convention.md (A14-6 — the `type:` leg of the Layer-3 entry condition names no owning convention; `origin: mggower/bmad-module-vlt#15`)'
  - 'factory/inbox/2026-08-26-141418-layer-3-open-entry-vs-closed-verified-by-roster.md (A14-7 — the contract''s open writer set meets `write-verification.md`''s closed `verified_by` roster; `origin: mggower/bmad-module-vlt#16`)'
roadmap: 'factory/cycles/14-no-enforcement-point/roadmap.md'
rulings: >
  roadmap §Ideation rulings (2026-08-26): Q3 (pointer, not vocabulary — the closed set governs the
  PARA population; amended A13 pointer-target unsettled, A14 legal response excludes the blocked
  population); Q4 (narrow the jurisdiction by ARTIFACT CLASS, not by writer; amended A11 needs a
  mechanical discriminator or reverts, A12 the transition is ruled here, A12b the contract still
  demands the pair); D2 (the handshake scope, decided once; amended A15 19-not-15, A16 `moc`,
  A3 seven in-prose pins); D3 as amended (A17 — BOUNDED ⇒ ship-verifiable ⇒ it GATES; A17b — an
  at-rest instrument buildable in scope MUST be built, and every check names its seam); D4 (`ST-6`
  is open and holds this cause); E3 (the single-vault counts are not a rate; amended A33 — replaced
  by an at-rest fixture PAIR); E5 (write A14-6 from the capture and current vault state, never from
  tracker #15''s prose; amended A34 — the shipped edit uses placeholders). Roundtable R1 (per-check
  seam) and R2 (P-18 Tier B synthetic-fixture observer) bind this brief.
risk: >
  moderate — the cycle''s largest and most irreversible build. THREE conventions bump and 19
  consumer acks move in one build (`write-verification` 3→4, `frontmatter` 13→14, `extraction`
  7→8); the operating contract and its derived rule-card both change (package-lint C6); a new
  release-gate check (E7) ships with its fixture case (package-lint E4/R2); and a real class of
  Layer-3 artifact permanently leaves structural coverage, accepted knowingly at Q4.
---

# Build #3 — governance: the handshake build

## Intent

Two filings, one shape. `vault-operating-contract.md:66` states the Layer-3 entry condition as four
legs; three name the convention that owns them inline and the `type:` leg names nothing (A14-6).
The same line declares the writer set **open** while `write-verification.md:47` closes the attester
roster to write ops, so a partner authoring a Layer-3 document in an ordinary sitting reaches
§Attestation and finds no value it may honestly hold — and `§Scope rule` then places the file in
jurisdiction with no route to clear the finding (A14-7). Both are `ST-6`'s cause — **a closed roster
meeting an actor the surrounding rules authorize** — one in the vocabulary register, one in the
writer register (`factory/studies/ST-6-closed-rosters-meet-authorized-actors.md`, opened at D4 from
the pre-repair state; this build is recorded in its `cited_by:`).

Build-3 gives the `type:` leg a named, handshaked owner; gives the attestation rule an artifact
class it can exempt **mechanically**; makes the contract, the convention and the shipped lint net
say the same thing; and — because this is the cycle named *no enforcement point* — gives the
handshake's blindest surface an enforcement point rather than a manual grep.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** Specifically
not reopened: widening the recognized `type:` set; generalizing the `{wiki}` by-name exclusion into
a declared list (both Q3, *Not taken*); widening the `verified_by` value set with a partner
identifier or in-sitting sentinel (Q4, *Not taken*); a writer-shaped exemption axis (Q4, refused on
`ST-1`); the precedence statement D2 rejected in favour of elimination.

**Cold by construction, stated up front.** Build-3 moves two — now three — convention digests and
`checks.md`'s, every one a component of `rulesetFingerprint`, and it edits `pageScanPrompt` and
`PAGE_SCAN`, both terms of `scanFingerprint`. **The first full lint after release 2 is COLD. That is
not a cache regression.** Release 1 already forced one cold sweep; this cycle knowingly costs two
(A26), and `{field-vault}` pays its owed COMPLETE sweep on the **second** sweep after release 2.

**This build is not the release build.** Release 2 is builds 2, 3 and 4; the dual version bump and
the `--expect-version` gate ride build-4 / `vlt-release`. §8 is omitted deliberately.

---

## Brief-time dispositions

### 1. THE RE-ACK FIGURE IS **19**, NOT 15 — three conventions move. *(settles A15 + A13; the roadmap ordered this settled here)*

D2 ruled 2 conventions / 15 re-acks with *"`extraction.md` does **NOT** move"*, and the roundtable
(A15) found D2's own narrowing may falsify a sentence inside `extraction.md`. **Settled: it does,
and A13 forces the same file independently. `extraction.md` moves. The figure is 19.**

Grounded against the worktree (post-build-1, post-build-2):

- **A13's dilemma is real and has only one honest exit.** `contract:66` must name the convention
  owning *"a recognized `type:`"*. Verified: `extraction.md` states a target-folder→`type:` mapping
  (`extraction.md:72-82`), names `moc` (`:78`) and the container types (`:184-186`), but **nowhere
  states a closed recognized set and nowhere uses the word "recognized"** — so pointing there today
  points at nothing. The alternative, `checks.md:19`, has **no frontmatter, no `version:`, no
  `consumers:`** (verified — `skills/vlt-lint/references/checks.md:1` is a bare `#` heading), so
  pointing there puts the module's most load-bearing boundary **beyond every handshake** and makes a
  lint check *define* a governance term instead of implementing one. The contract's other three legs
  each point at a handshaked convention. **RULED: the pointer target is `extraction.md`, and the
  closed recognized-set statement lands there.** That is a rule change: `extraction.md` **7 → 8**.
- **Grounding addition supporting the choice:** `extraction.md:78` already reads *"named here so it
  is recognizable schema (`vlt-lint`'s `para_type_unknown` set)"* — extraction is **already** the
  de-facto declaring home for at least one member of the recognized set. F2 makes formal what the
  file already does.
- **A15's falsification is then repaired inside a bump already owed, at zero marginal cost.**
  Verified at `extraction.md:188`: *"The three `type:` values (`charter`, `record`, `register`) ride
  `frontmatter.md`'s declared non-exhaustive `type:` list — named here, no contract edit owed."*
  Container files sit under `{projects}`/`{areas}`/`{resources}` and are therefore inside the
  `para_*` population (`checks.md:19`), which is precisely the population `frontmatter.md:71` stops
  answering for. The sentence names a mechanism that no longer reaches its own subject.
- **The trade D2 said must be "re-put with the true number in view" does not need re-putting.**
  D2 chose elimination over precedence partly on cost; the true number is 19, and the precedence
  statement is still the wrong instrument — `CLAUDE.md`'s *precedence by elimination* makes it the
  fallback, legal only where populations cannot be cut apart, and J2's answer verified the cut holds
  (`{research}` defaults to `_agent/research/`, outside PARA — `module.yaml:47`). Elimination stands
  at 19. **Owner Ruling 2 already absorbed this as a brief-time scoping fact.**

**The settled figure, itemized:**

| Convention | Version | Consumers re-acked | Why it moves |
|---|---|---|---|
| `write-verification.md` | **3 → 4** | **5** — `vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js` | Q4's §Scope rule class exemption |
| `frontmatter.md` | **13 → 14** | **10** — `vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch, vlt-setup, vlt-groom, vlt-query, vlt-lint-full.js` | `:71`'s open-vocabulary clause scoped out of the PARA population (D2); `moc` named (A16) |
| `extraction.md` | **7 → 8** | **4** — `vlt-extract, vlt-lint, vlt-track, vlt-query` | the recognized-set home (A13); the operational-record class (A11); `:188`'s grounding repair (A15) |
| `vault-operating-contract.md` | **no bump** | — | deliberately not handshaked (single-home + pointers, `CLAUDE.md`); **but C6 is not free** — see F4 |

**TOTAL: 3 conventions, 19 re-acks across 11 files, one bipartite-consistency check** (package-lint
Group E1 + E5), **plus 8 in-prose citation tokens at 6 sites that no shipped check can see today —
disposition 2 fixes that.** All three `consumers:` lists were verified bipartite-consistent against
current source before this brief was written (`package-lint` A/B/C/E PASS at `d641050`).

### 2. THE IN-PROSE PINS GET A REAL ENFORCEMENT POINT: package-lint **E7**. *(settles A3; required by D3 clause 1, not chosen)*

A3 found that `vlt-lint-full.js` recites the two conventions by version at seven in-prose sites that
**nothing checks**, and prescribed *"Build-3 greps … and its verification NAMES the grep — the
bipartite verification is manual for those seven."*

**RULED: build-3 ships a check instead, and retires the prescribed grep.** Two reasons, both binding:

1. **D3-as-amended, clause 1 (A17b):** *"Where a check's subject is gradeable at rest by an
   instrument buildable inside the build's own scope, the brief **must build it**. Declining is a
   written justification in the brief, never a tag choice."* Pin currency inside a workflow asset is
   gradeable at rest by a ~20-line structural check next to E5, which already parses that exact
   header. The instrument is buildable in scope. D3 does not leave this to taste.
2. **`brief-anatomy.md` §7 already forbids the prescribed remedy as a verification:** a hand-written
   `grep "<name>@" skills/` is **self-confirming** — it greps for the token you just wrote, in the
   files you just edited — *"It is never the recorded verification."* A3's manual-grep prescription
   is the retired build-23 ritual returning under a new name, in the cycle named for rules with no
   enforcement point.

**Verified, so the check is aimed correctly:**

- `_e3_stray_pin` (`tools/package-lint.py:728-760`) scans `skills/vlt-*/SKILL.md` +
  `skills/vlt-*/references/*.md` and **deliberately excludes** `vlt-setup/assets/**` — docstring
  verbatim at **`tools/package-lint.py:737-740`**: *"deliberately NOT a blanket `**/*.md`
  (`vlt-setup/assets/**` is installable payload with its own vault-side jurisdiction)."*
  ⚠ **Grounding correction:** the roadmap cites `:736-739`; the clause is at **`:737-740`**.
- `_e5_asset_nodes` (`:768-...`) parses **exactly one** `// depends_on: [...]` header line per
  workflow (`_DEPENDS_ON_LINE_RE`, `:765`) and never reads the body.
- So the seam between *the header ack* and *the body's recitations of the same pin* is covered by
  neither. **E7 covers exactly that seam and nothing else** — it is not E3 relocated: E3 asks *"is
  this an undeclared consumption?"*, which would be wrong here (the workflow **does** declare); E7
  asks *"does the body agree with the header this file already carries?"*

**E7, specified** (`tools/package-lint.py`, in Group E's composition at `:1024-1032`, ordered after
`_e5_asset_nodes`):

```
def _e7_asset_prose_pin_currency(root, conventions) -> list:
    """E7 (build-3, Cycle 14): in-prose pin currency inside workflow assets.

    E3's stray-pin net deliberately excludes vlt-setup/assets/** and E5 reads
    only the `// depends_on:` header line, so a workflow that recites a
    convention BY VERSION in its prose — schema descriptions, agent prompts,
    code comments — can carry a stale pin through a green handshake and ship it
    to every vault. This is not a consumption question (the asset declares in
    its header); it is a CURRENCY question. Every `name@version` token in a
    workflow body, anchored on the known convention names, must equal that
    file's own header ack for the same convention. A body pin naming a
    convention the header does not ack also FAILs (the reverse drift).
    """
```

- **Scope:** `skills/vlt-setup/assets/workflows/*.js` — every line except the single
  `// depends_on:` line E5 owns.
- **Pattern:** anchored on `set(conventions)` exactly as E3 is (`:745`), never a bare `\w+@\d+`.
- **Failure text** names `rel:lineno`, the recited pin, and the header's value.
- **R2 / package-lint E4 (mandatory, same build):** `_e4_harness_coverage` (`:857-897`) derives its
  inventory by introspecting `^_e\d+_` callables, so **E7 without a covering case FAILS the gate.**
  Add a case to `tools/test-package-lint.py` on the `case_e3_stray_pin` pattern (`:407-417`) —
  mutate one body pin in the fixture workflow to a wrong version, assert `FAIL group E` and the E7
  string — and bump **`CASE_FLOOR` 23 → 24** (`tools/test-package-lint.py:229`).

**What E7 retires (P-15):** D2's amendment sentence *"Build-3 greps … and its verification NAMES the
grep — the bipartite verification is manual for those seven."* The manual half ceases to exist. Say
so in the roadmap's superseding note, not silently.

### 3. THE SEVEN PINS ARE NOW **SIX SITES / EIGHT TOKENS**, AND **NONE IS A CONTENT RE-CHECK**. *(grounding correction to A3; re-derived at `d641050`)*

A3's seven sites were v0.16.1-era. Re-derived against current source (`vlt-lint-full.js`, **870
lines**), the count is `grep -c`-exact: **5 `frontmatter@13` and 5 `write-verification@3` tokens in
the file, one of each being the `:11` header ack** ⇒ **8 in-prose tokens at 6 sites.**

| Roadmap (v0.16.1) | Now | What it is | Q4 content impact |
|---|---|---|---|
| `:158` | **`:171`** | `outbound_links` description, *"per frontmatter@13 rule 5"* — **inside `PAGE_SCAN`** | none — cites `frontmatter.md` rule 5 (wikilink form), untouched |
| `:159` | **GONE** | `frontmatter_valid` — **RETIRED WHOLE by build-1** (A-R1; 208 chars paid the E6 budget) | n/a |
| `:164` | **`:178`** | `sources_vs_prose` description, *"per write-verification@3"* — **inside `PAGE_SCAN`** | **none — grounding correction:** it cites the **tier-1 wiki-page item** (`write-verification.md:38`, *frontmatter is the source of truth*), **NOT §Scope rule.** A3 says it restates §Scope rule; it does not. |
| `:168` | **`:182`** | `unmarked_supersession` description, *"(per write-verification@3 Scope rule)"* — **inside `PAGE_SCAN`**; **KEPT under owner ruling A-R1** | **none** — it restates §Scope rule's **Jurisdiction-boundary** clause (`write-verification.md:55`, *attestation is never an unmarked supersession*), which Q4 **does not amend**. The sentence stays true. |
| `:215` | **`:229`** | `pageScanPrompt` — **3 tokens on one line** (2× `frontmatter@13` rule 4, 1× `write-verification@3`) | none — the write-verification cite is again the **tier-1 item**, not §Scope rule |
| `:571` | **`:682`** | comment, *"(frontmatter@13, \*Wiki pages\*)"* — outside `PAGE_SCAN` | none |
| `:573` | **`:684`** | comment, *"Attestation is a self-marker under write-verification@3's Scope rule…"* — outside `PAGE_SCAN` | **the one true §Scope rule restatement in the file** — and it restates the Jurisdiction-boundary clause, unamended. Content stays true. |

**RULED: every one of the eight tokens is a pure version-string bump. Zero content re-checks.**
A3's *"three of them restate the very §Scope rule Q4 amends, making them wrong rather than merely
old"* is **superseded by grounding**: one of the three is retired, one cites a different section
entirely, and the third (plus the comment at `:684`, which A3's list omitted) cites the clause Q4
leaves alone. A superseding note goes into the roadmap.

**Consequence for the `:168` dissent (§Carried forward 9): NOT tripped.** The dissent becomes the
ruling *"the moment `unmarked_supersession` is structured"*. Build-3 structures nothing; `:182`
(formerly `:168`) changes by one digit in a citation. **`:168` survives this build unchanged in
substance; the dissent stays deferred.** Stated so no builder reads the edit as the trigger.

### 4. THE MECHANICAL DISCRIMINATOR IS **`type:`**, and the mechanism already ships. *(settles A11 — BLOCKING)*

A11 ruled Q4 reverts unless the exemption is *"expressible in the frontmatter §Scope rule already
reads — a `type:` value, a declared field, or a location"*, and that build-3 **names it**.

**RULED: a `type:` value — specifically the existing operational-record types `record` and
`register`, widened from container-file position to a Layer-3 artifact class.**

Grounded, and the reason this is the cheapest honest answer:

- §Scope rule's jurisdiction is already a **`type:` test**: `write-verification.md:55` — *"files
  carrying vault frontmatter (`type: wiki|research|project|area|resource` with `author:
  agent|hybrid`)"*. **`record` and `register` are already outside that list.** The container carve-out
  A11 correctly identifies as *"a label attached to three filenames"* at `extraction.md:188` is, in
  §Scope rule itself, already a **type** exclusion. Nothing about the predicate changes.
- `checks.md:19`'s recognized set **already admits** `charter|record|register`, so a Layer-3
  operational record carrying `type: record` outside a container is already recognized vocabulary —
  it does not trip `para_type_unknown`.
- The discriminator is therefore **readable by the actor that must decide** — and that matters more
  here than anywhere, because **`para_missing_attestation` has no code enforcement point at all**:
  ⚠ **grounding finding, load-bearing.** `vlt-lint-full.js:807-809` reads *"PARA files are outside
  this workflow's page set (it sweeps `{wiki}`) — `para_missing_attestation` is a structural slot
  the SKILL fills from its own PARA jurisdiction scan"*, and `full-scale.md:11` confirms *"the PARA
  scan … stay yours; fill those report slots from your own pass."* The check is an **agent reading
  prose**. A "class judgment" discriminator would have been unevaluable by the only thing that
  evaluates it; a frontmatter field is not. This is A11's finding one level deeper, and it is why
  the answer must be `type:` and not a new declared field.
- **Why not a new `type:` value.** A new value costs the same `extraction.md` declaration and adds a
  seventh member to a set two other checks read, for a class the shipped vocabulary already names
  precisely (`extraction.md:184`: *"the dated, append-shaped running record … each entry attributed
  `(<partner>)`"* — that is exactly what a partner-sitting operational record is). Widening beats
  minting; **`CLAUDE.md`'s single-home discipline and P-15 both point the same way.**
- **Why not `local_consumers:`.** Kept as-is per Q4's ⚠ clause (`write-verification.md:47`,
  `frontmatter.md:296`, both verified) — a vault-minted partner that genuinely *is* a write op can
  still register. This build removes the need to **pretend** to be one; it does not remove the route.

**A11's escape clause fires as predicted and costs nothing extra:** *"If the discriminator is a new
`type:` value it is declared in `extraction.md` and re-opens A13's scope."* A13's scope is already
open (disposition 1) — `extraction.md` is bumping regardless. **The discriminator rides a bump
already owed.**

### 5. THE EXEMPTION **CITES** `extraction.md`, IT DOES NOT RESTATE IT. *(settles the deferred wording question)*

The roadmap's §Questions deliberately left to brief time, build-3: *"the exact wording of
`write-verification.md` §Scope rule's class-based exemption, and whether it cites `extraction.md:188`
or restates the principle (single-home discipline says cite)."*

**RULED: cite.** `CLAUDE.md`'s single-home rule is unconditional — *"mechanics live in exactly one
place; every other site carries a short pointer, never restated mechanics"* — and this build is
already paying to make `extraction.md` the home of the PARA vocabulary. Restating the class
definition inside `write-verification.md` would create the second copy the very next cycle has to
reconcile: **A14-7's own shape, one file over.**

**But cite the class, not the line.** ⚠ The deferred question names `extraction.md:188`. A shipped
convention must not carry a `file:line` pointer — line numbers drift (this brief corrected four of
the roadmap's own). §Scope rule cites **`extraction.md`, *PARA containers* / the operational-record
class** — a section pointer, matching how `write-verification.md:44` already cites *"`frontmatter.md`
— referenced here, not redefined"* and how `:55` already cites *"`frontmatter.md`, *Base
frontmatter*"*. Same idiom, same file, three lines apart.

**Exact replacement text for `write-verification.md:55`** (the builder edits this sentence and no
other in the paragraph):

> …files carrying vault frontmatter (`type: wiki|research|project|area|resource` with `author:
> agent|hybrid`) and no attestation — never bare human files. `daily/`, raw `sources/` deposits, and
> human-authored PARA files are out of jurisdiction, **and so is the Layer-3 operational-record
> class — files whose `type:` is `record` or `register` (`extraction.md`, *PARA containers* — the
> class definition and its attestation posture live there, not here). The exemption is by artifact
> class, never by writer: a partner sitting is not a jurisdiction, and permission fused to
> provenance is `ST-1`'s named cause. A Layer-3 knowledge artifact written in a sitting is in
> jurisdiction like any other.**

### 6. THE LEGAL RESPONSE FOR A MODULE-CANONICAL TYPE: **retype or relocate per the target-folder mapping** — neither of A14's two options. ⚠ *(owner-visible)*

A14 found `checks.md:19`'s shipped legal response (*"declare the **vault-grown** type as overlay
schema…"*) does not reach the blocked population, because `type: research` is **module-canonical**
(`frontmatter.md:71`) rather than vault-grown, and it offered two routes: *"admit it to the set, or
state that overlay-declaration covers module-canonical values — and say which."*

**RULED: neither. Both are refuted by grounding; a third, better-grounded response is written.**

- **Admitting `research` to the PARA recognized set breaks the cut D2 stands on.** J2's answer holds
  only because `{research}` defaults to `_agent/research/`, **outside PARA** (`module.yaml:47`).
  Admitting `research` as a PARA artifact type re-imports the ambiguity D2 paid 19 re-acks to
  eliminate.
- **Overlay-declaring module-canonical values is exactly what the park exists to refuse.** A14 states
  it: the vault parked *"on the stated grounds that a local overlay would be a vault answering a
  module-level question"*, and telling it to overlay-declare module vocabulary makes the vault
  **assert local authorship of module vocabulary.**
- **The module already contains the right answer and never states it as a response.**
  `extraction.md:72-82` maps target folder → `type:`: `projects/`→`project`, `areas/`→`area`,
  `resources/`→`resource`, plus `moc` as the one readable-but-not-target-derived type. A
  module-canonical **non-PARA** type (`research`, `note`, `idea`, `wiki`, `session`) sitting in a
  PARA folder is a **mis-typed artifact or a mis-placed one** — not an unrecognized vocabulary.

`checks.md:19`'s `para_type_unknown` legal response is therefore amended to route by **three** cases:
(a) **vault-grown** type → declare as overlay schema (unchanged); (b) **module-canonical but
non-PARA** type → retype to the target-folder type (`extraction.md`, *`type:` mapping by target
folder*) **or** relocate to that type's home zone — **never overlay-declare module vocabulary**;
(c) otherwise → relocate out of PARA. **This is the written unpark trigger A14 demanded**: the vault
can execute (b) without declaring module vocabulary as its own, and acceptance check (6) grades it.

⚠ **Flagged for the owner:** this is outside A14's two-option menu. It is inside the delegated
question (*cover the blocked population*), both named options are refuted above, and A14's own text
says the module *"does not already give an answer for this population"* — so a third was always
going to be needed. Recorded here rather than assumed.

### 7. THE TRANSITION FOR THE MEASURED 27: a **pre-adoption informational posture**, on the shipped `unattested_write` precedent. *(settles A12)*

A12: *"Build-3 either satisfies the discriminator retroactively for files already on disk (stating
how) **or** ships a pre-adoption informational posture for `para_missing_attestation` matching
`checks.md:17`'s clause."*

**RULED: the pre-adoption posture.** Retroactive satisfaction is **impossible for the module** — the
discriminator is a `type:` value in vault frontmatter, and retyping a vault's files is a vault act
the module cannot and must not perform (the durability posture; `vlt-upgrade` merges, never rewrites
vault content).

Verified: `checks.md:17` carries the clause for `unattested_write` — *"informational, not a
violation, for files whose `created` predates convention adoption"* — and **`para_missing_attestation`
carries no such clause**, exactly as A12 found. `para_type_unknown` and `para_status_unknown`
(`checks.md:19`, `:18`) both carry one. `para_missing_attestation` is the outlier.

`checks.md:17` gains the matching clause, with the legal response naming the three routes: retype to
the operational-record class where the file **is** one, attest it where it is a knowledge artifact,
or the human rules it human-authored.

**R1 — interim posture (required; this is it).** In the window between release 2 and a vault's own
retype pass, a file in the measured class is **informational, not a violation**: it is listed, it is
denominated, no act is owed, and no partner is asked to write a `verified_by` value it cannot
honestly hold. That is the legal posture, stated rather than left to the field to infer. The window
closes per file on that file's next substantive edit — the same coexistence idiom
`extraction.md:118` already ships for `status:` enums.

### 8. THE CONTRACT AND THE CONVENTION MUST SAY THE SAME THING. *(settles A12b)*

A12b: the pair is a term of `contract:66`'s entry condition (*"Content that carries it is in;
content that does not is out, wherever it sits"*), and `:70`'s carve-out names container files **by
class and nothing else** — so exempting a partner-written operational record in the convention while
the contract still calls it "out" would resolve A14-7's two-surface disagreement **by creating a new
one, the same shape, one file over.**

**RULED: both surfaces move together in this build, and acceptance check (4) greps that they agree.**
`contract:66`'s attestation-pair leg is qualified for the operational-record class and `:70`'s
sentence is widened from *"Container files are operational records"* to the class (F4). No bump — the
contract is deliberately not handshaked — **but C6 is not free** (F4, and §5 Registration).

### 9. **Retirement disposition (P-15).** Four, each named with its site; none silent.

1. **`frontmatter.md:71`'s open-vocabulary clause, for the PARA population** — superseded by the
   closed recognized set at its new home. Named as a retirement by D2 and landed in F3.
2. **`extraction.md:188`'s closing grounding sentence** (*"…ride `frontmatter.md`'s declared
   non-exhaustive `type:` list — named here, no contract edit owed"*) — the mechanism it names stops
   reaching its own subject the moment F3 lands. **Retired and replaced in F2**, not left standing.
3. **`checks.md:19`'s *definition* of the recognized set** — retired **as a definition**; the line
   keeps the set only as a short pointer to `extraction.md`, per single-home. The check still
   implements; it no longer defines.
4. **D2's manual-grep prescription** (*"the bipartite verification is manual for those seven"*) —
   retired by E7 (disposition 2). The ritual `brief-anatomy.md` §7 forbids as a recorded verification
   does not survive into this build.

**Survives deliberately, with its reason:** `para_author_unknown` stays closed to `human|agent|hybrid`
with no overlay escape (Q3 ⚠; §Carried forward 6) — **and its owning convention is likewise unnamed,
the same defect A14-6 repairs for `type:`.** Not fixed here: fixing it is a second vocabulary ruling
the roadmap does not make, and folding it into a 19-re-ack build unmeasured is what E2 was scoped out
for. It is already carried at §Carried forward 6 with its bound.

---

## F1 — `write-verification.md`: §Scope rule gains the class exemption; `version: 3 → 4`

**Path:** `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md`
*(the governance SSoT — `CLAUDE.md`: the bundle lives ONLY here. Never a second copy.)*

**Current state, re-grounded:**
- `:11` `version: 3` — HOLDS.
- `:12` `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js]` — HOLDS (5).
- `:13-15` `enforcement_stage: checked` / `enforcement_checked_by: vlt-lint` / `enforcement_moment:
  lint run` — HOLDS; A11's premise verified.
- `:47` the `verified_by` closure and the write-op qualifier — HOLDS verbatim as captured.
- `:53` `## Scope rule (self-marker)` heading; **`:55` is the rule body.**
  ⚠ **Grounding correction:** capture and Q4 cite `:53-54`; the paragraph is at **`:55`**
  (`:54` is blank).

**The exact change:**
1. `:55` — replace the jurisdiction sentence with disposition 5's text (the exemption, cited to
   `extraction.md`, *PARA containers*, plus the by-class-never-by-writer clause). The
   **Jurisdiction boundary** sentences that follow it are **untouched** — they are what `:182` and
   `:684` restate, and they stay true (disposition 3).
2. `:11` — `version: 3` → `version: 4`.
3. `:12` — `consumers:` list **unchanged**; all five re-ack in F7/F8.

**Why:** Q4, as amended by A11 (the discriminator) and A12b (the contract must agree). A jurisdiction
narrowing is a **rule** change, not a prose clarification — the capture said so and this brief
confirms it: a file that was in jurisdiction leaves it.

**Out of scope at this site:** `:47`'s roster closure and the write-op qualifier stay exactly as
shipped (Q4, *Not taken* — widening the value set); the tier-1 checklist (`:28-40`) is untouched —
**E2's *"frontmatter is the source of truth"* re-scoping of `:38` is scoped OUT of this cycle** and
routed to `factory/inbox/` as a `pattern` by the owner (A32, §Carried forward 7). **Do not fold it
in.** The fail-open rule (`:51`) is untouched.

---

## F2 — `extraction.md`: the recognized-set home + the operational-record class; `version: 7 → 8`

**Path:** `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md`

**Current state, re-grounded:**
- `:11` `version: 7`, `:12` `consumers: [vlt-extract, vlt-lint, vlt-track, vlt-query]` — HOLDS (4).
- `:74-78` the target-folder→`type:` table + the `moc` paragraph — HOLDS; `:78` already names `moc`
  as *"recognizable schema (`vlt-lint`'s `para_type_unknown` set)"*.
- `:118` the declare-at-birth sentence — HOLDS, and A13 is right that it declares a vault-grown
  type's **`status:`** vocabulary, not the type.
- `:149-188` §PARA containers; `:184` `record.md`, `:186` `register.md`, `:188` the attestation
  posture + the grounding sentence — all HOLD at the cited lines.

**The exact change — three edits, one bump:**

1. **The recognized set gets its home** (A13's pointer target). In the `type:` mapping section
   (after `:78`'s `moc` paragraph), add the **closed recognized-set statement** for the PARA
   population: the set is `project | area | resource | moc` (artifact types) + `charter | record |
   register` (the operational-record class, §PARA containers) + any vault-declared schema in
   `{overlays}/extraction.overlay.md`. State that it is **closed for the PARA population**, that
   `frontmatter.md`'s non-exhaustive list governs the base/agent lane and does not answer here, and
   that a module-canonical **non-PARA** type in a PARA folder is a mis-typed or mis-placed artifact
   (disposition 6, route (b)). **This is the sentence `contract:66` will point at.**
2. **`record`/`register` widen from container-file position to a Layer-3 artifact class** (A11's
   discriminator). In §PARA containers, state that `record` and `register` name the **operational-record
   class** — dated, append-shaped, attribution-per-entry, **no attestation pair** — of which the
   container-sited `record.md`/`register.md` are the container instances, and that a Layer-3
   operational record written outside a container carries the same `type:` and the same posture.
3. **`:188`'s grounding sentence is retired and replaced** (A15). Strike *"ride `frontmatter.md`'s
   declared non-exhaustive `type:` list — named here, no contract edit owed"*; replace with the
   values being **members of the recognized set stated above in this file**. The attestation-posture
   sentence that precedes it, and its parenthetical naming `vlt-lint`'s `para_missing_attestation`
   carve-out, are **kept** — that parenthetical is now literally true of a wider class, and F5
   makes the check agree.
4. `:11` — `version: 7` → `version: 8`; `:12` `consumers:` **unchanged**; all four re-ack in F7.

**Why:** A13 (the pointer must land on a handshaked convention), A11 (the discriminator is declared
here), A15 (the falsified sentence), Q3 (the closed set governs the PARA population).

**Out of scope at this site:** `:118`'s declare-at-birth `status:` sentence is untouched. The trust
ladder (`contract:66`'s second leg already points here) is untouched. `resources/`'s live-target
posture and the legacy-preservation clauses at `:80-82` are untouched.

---

## F3 — `frontmatter.md`: `:71` narrowed, `moc` named; `version: 13 → 14`

**Path:** `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md`

**Current state, re-grounded:**
- `:11` `version: 13`, `:12` the 10-name `consumers:` list — HOLDS exactly as D2 states.
- `:71` — HOLDS verbatim: *"The `type:` list is **non-exhaustive.** Canonical values include `wiki`,
  `research`, `session`, `note`, `project`, `area`, `resource`, `idea`, and the PARA container files
  `charter`, `record`, `register` (`extraction.md`, *PARA containers*). `resource` is **live again as
  of extraction v6** … New artifact classes may introduce new `type:` values without a contract edit;
  this convention names new values as they appear."*
- **A16 CONFIRMED:** `grep -c moc frontmatter.md` = **0**.
  ⚠ **Grounding correction to A16's framing:** `moc` is *not* "named in no convention" — it is named
  at **`extraction.md:78`**, as recognizable `para_type_unknown` schema. A16's finding is true of
  `frontmatter.md` only. The edit below still lands (the canonical list should be complete), but the
  roadmap's stronger claim is corrected.
- `:294`, `:296` `local_consumers:` — HOLD (Q4's ⚠ clause verified).

**The exact change:**
1. `:71` — **scope the open-vocabulary clause.** *"New artifact classes may introduce new `type:`
   values without a contract edit"* is qualified to the **base/agent lane**, with one clause stating
   that for the **PARA population** the recognized set is **closed** and lives in `extraction.md`
   (pointer, never a restatement of the set).
2. `:71` — **add `moc`** to the canonical list (A16).
3. `:11` — `version: 13` → `version: 14`; `:12` `consumers:` **unchanged**; all ten re-ack in F7/F8.

**Why:** D2's elimination (narrow one rule's population rather than state precedence — `CLAUDE.md`,
Arc 9 D5), A16, and Q3's *"`frontmatter.md:71`'s non-exhaustiveness is scoped so it no longer answers
for that population."*

**Out of scope at this site:** the `status:` enums, the attestation field definitions (`§Write
attestation` — `write-verification.md:44` cites them and they do not move), `local_consumers:`
(`:294-296`), and the wikilink-form rules 4/5 that `vlt-lint-full.js:171`/`:229` cite. **`:71`'s
canonical list must keep naming `charter|record|register`** — F2 makes them recognized-set members
for PARA, and they remain canonical vocabulary generally.

---

## F4 — `vault-operating-contract.md` + the derived rule-card (no bump, **not free**)

**Path:** `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` and
`skills/vlt-setup/assets/governance/_meta/vault-rule-card.md`

**Current state, re-grounded:**
- **`:66`** — Layer 3's entry condition. HOLDS at the cited line, verbatim as captured: *"an honest
  `author:` (`human | agent | hybrid`), a `trust:` rung the writer is entitled to set (an agent sets
  `raw` and nothing above it — the trust ladder in `extraction.md`), a recognized `type:`, and the
  write-verification attestation pair (`write-verification.md`)"*, followed by the openness clause
  *"they are the shipped set, **not** a closed one."*
- **`:70`** — §PARA containers, *"Container files are **operational records, not knowledge
  artifacts** … they carry no `verified_by:`/`verified_at:` pair."* HOLDS.
- **`:64`** — the `{wiki}`-removed-at-selection-time canonical statement.
  ⚠ **Grounding correction:** A14-6's capture cites `:65`; it is at **`:64`**. Not edited by this
  build; corrected so the roadmap stops asserting a stale line.
- **`vault-rule-card.md:11`** `derived_from: 'vault-operating-contract.md
  sha256:990faf0a95eea68c1159ad658cc67ce9d4fa89b5fbc77171b7e999d8d8dc77ae (derived 2026-08-27)'` —
  **verified current against the shipped contract** (build-2's F6 re-stamp; `shasum -a 256` matches).
  Card size **7,106 bytes** of `RULE_CARD_BUDGET` 8,000 (`tools/package-lint.py:261`) — **894 bytes
  headroom.**

**The exact change:**
1. **`:66` — the A14-6 pointer.** The `type:` leg becomes *"a recognized `type:` (the PARA recognized
   set in `extraction.md`)"* — the same inline-home idiom the other three legs already use. **This
   is the whole of A14-6's repair** (Q3: *"the residual scope may therefore be a pointer, not a
   vocabulary decision"* — confirmed).
2. **`:66` — the A12b qualifier.** The attestation-pair leg is qualified: the pair is owed by Layer-3
   **knowledge artifacts**; the operational-record class carries none (`extraction.md` / `:70`
   below). Written so *"content that does not is out"* no longer contradicts the exempted class.
3. **`:70` — widen the carve-out to the class.** *"Container files are operational records"* becomes
   the class statement (operational records — container-sited or partner-written), matching F2. The
   `{wiki}`-by-name and location-membership clauses in that paragraph are **untouched**.
4. **`vault-rule-card.md:26` — the card restates the entry condition and goes stale.**
   ⚠ **Grounding finding the roadmap does not name.** `:26` reads *"you may write **iff** (a) your
   frontmatter is honest and attested — real `author:`, a `trust:` rung you are entitled to set,
   recognized `type:`, attestation pair"*. That is an **act-blocking** clause and after F1 it is
   **over-broad** — it would tell a partner it must attest an operational record it is exempt from
   attesting. The card gains a short qualifier on the same line (both the `extraction.md` pointer and
   the class exemption fit inside 894 bytes; keep it to one clause).
5. **Re-stamp `derived_from:`** with the new contract `sha256:` and the build date — **package-lint
   C6** (`check_rule_card`, `tools/package-lint.py:315-348`) fails the release otherwise. Re-check
   size against `RULE_CARD_BUDGET` after the edit.

**Why:** Q3/A13 (the pointer), A12b (the two surfaces must agree), C6 (`CLAUDE.md`: the contract is
deliberately not handshaked, **and it is not free** — `brief-anatomy.md` §5).

**Out of scope at this site:** no `version:` is added to the contract — it is deliberately unhandshaked
(single-home + pointers). The write-posture resolver, the hard rule's `writers:` clause, `:155`'s
`{log}` `<type>` set, and the Decay contracts table at `:325` (**build-2's**, `_agent/lint-cache.json`
— do not touch) are all untouched.

---

## F5 — `skills/vlt-lint/references/checks.md`: where §Scope rule actually binds

**Path:** `skills/vlt-lint/references/checks.md`
*(no frontmatter, no `version:`, no `consumers:` — verified `:1`. It is not a handshake node; its
digest **is** a `rulesetFingerprint` component, so editing it moves the fingerprint. Already cold.)*

**Current state, re-grounded — A11b CONFIRMED, at the cited line:**
- **`:17`** — *"**Population carve-out:** container files (`charter.md`/`record.md`/`register.md`
  under a `{projects}`/`{areas}`/`{resources}` container directory) are judged by the container
  schema … not by the artifact attestation rule"*. **This is a filename-plus-location test, not the
  `type:` test §Scope rule uses** — so a `type: record` file outside a container directory is
  exempt in the convention and **still flagged by the shipped net.** A11b is exactly right: ship
  without this and *"the convention exempts a class the shipped net still flags with no route to
  clear it — A14-7's exact shape relocated one file over."*
- **`:17`** — `para_missing_attestation` carries **no** pre-adoption clause; `unattested_write` on
  the same line does (*"informational, not a violation, for files whose `created` predates convention
  adoption"*). **A12 CONFIRMED.**
- **`:19`** — the recognized set and `para_type_unknown`'s legal response, verbatim as captured;
  the set includes `moc`. **A14 CONFIRMED** — the response says *"vault-grown"*.

**RULED IN SCOPE (A11b).** The exact change:

1. **`:17` — widen the Population carve-out to the class.** Container files **plus** any file in the
   `para_*` population carrying `type: record` or `type: register` — the Layer-3 operational-record
   class (`{conventions}/extraction.md`, *PARA containers*; `{conventions}/write-verification.md`,
   *Scope rule*) — judged by the container schema, not by the artifact attestation rule. **Cite,
   never restate the class definition** (disposition 5).
2. **`:17` — add the pre-adoption clause** to `para_missing_attestation`, matching `unattested_write`'s
   shipped wording (disposition 7 / A12).
3. **`:17` — R3, the legal response** (`brief-anatomy.md` §7, mandatory when a finding class changes):
   `para_missing_attestation` → *retype to the operational-record class where the file is one, or the
   owning writer re-runs its verify pass and attests, or the human rules the file human-authored*;
   pre-adoption → informational, no act owed.
4. **`:19` — the recognized set becomes a pointer.** The set stops being **defined** here and cites
   `extraction.md` as its home (retirement 3, single-home). The check still names the members for
   the reader; it no longer owns them.
5. **`:19` — R3, the amended legal response** for `para_type_unknown`: disposition 6's three routes,
   with (b) explicitly forbidding overlay-declaration of module-canonical vocabulary.

**Out of scope at this site:** `:14` and `:15` are **build-1's** (the entity-decoded category clause
and the restated `malformed_frontmatter` exclusions) — byte-identical, do not touch. `:18`
`para_status_unknown` and `:20` `para_writer_unauthorized` are untouched. **`para_author_unknown` at
`:19` stays closed with no overlay escape** — named, not silently survived (disposition 9;
§Carried forward 6).

---

## F6 — `skills/vlt-lint/references/report.md:32`: the slot description

**Current state, re-grounded:** `:32` — `para_missing_attestation: [<para-file: vault type + author
agent|hybrid, no attestation>, ...]`. The slot's shorthand states the jurisdiction and carries no
carve-out, so after F1/F5 it describes a wider population than the check judges.

**The exact change:** extend the placeholder with the exclusion in the same telegraphic register the
sibling slots use (`:37` carries *"— informational where created predates convention adoption"*):
`<para-file: vault type + author agent|hybrid, no attestation — excludes the operational-record
class; informational where created predates convention adoption>`.

**Out of scope / collision note:** `report.md:3` and `:13` are **build-4's** (Q5's `.json` persist),
`:77` and `:88` are **build-2's** (`cache_rejected`). `:32` is touched by neither — verified against
both BUILT briefs. Take `:32` only.

---

## F7 — The consumer walk: 19 re-acks across 11 files

**Every consumer of every bumped convention re-acks in this build** (`CLAUDE.md`'s version-handshake
rule). Re-grounded against current source — all three `consumers:` lists are bipartite-consistent
today, so the walk is a pure version-token update, no list membership changes.

| File | Line | Current `depends_on:` (verified) | Tokens to move |
|---|---|---|---|
| `skills/vlt-ingest/SKILL.md` | `:4` | `["frontmatter@13", "wiki-index@2", "wiki-consolidation@1", "wiki-supersession@2", "write-verification@3", "decision-log@4"]` | fm→14, wv→4 |
| `skills/vlt-extract/SKILL.md` | `:4` | `["extraction@7", "wiki-supersession@2", "frontmatter@13", "write-verification@3"]` | ex→8, fm→14, wv→4 |
| `skills/vlt-research/SKILL.md` | `:3` | `["frontmatter@13", "write-verification@3"]` | fm→14, wv→4 |
| `skills/vlt-lint/SKILL.md` | `:4` | `["frontmatter@13", "wiki-index@2", "wiki-supersession@2", "extraction@7", "write-verification@3", "spec@2", "consult@1", "decision-log@4"]` | fm→14, ex→8, wv→4 |
| `skills/vlt-mint/SKILL.md` | `:3` | `["spec@2", "frontmatter@13", "decision-log@4"]` | fm→14 |
| `skills/vlt-dispatch/SKILL.md` | `:3` | `["consult@1", "spec@2", "frontmatter@13"]` | fm→14 |
| `skills/vlt-setup/SKILL.md` | `:3` | `["frontmatter@13"]` | fm→14 |
| `skills/vlt-groom/SKILL.md` | `:3` | `["frontmatter@13"]` | fm→14 |
| `skills/vlt-query/SKILL.md` | `:4` | `["extraction@7", "frontmatter@13"]` | ex→8, fm→14 |
| `skills/vlt-track/SKILL.md` | `:—` | `extraction@7` (a listed `extraction` consumer) | ex→8 |
| `skills/vlt-setup/assets/workflows/vlt-lint-full.js` | `:11` | `// depends_on: ["frontmatter@13", "wiki-supersession@2", "wiki-index@2", "write-verification@3"]` | fm→14, wv→4 — **see F8** |

**Count: 5 + 10 + 4 = 19 ack tokens, 11 files.** `wiki-index@2`, `wiki-supersession@2`,
`wiki-consolidation@1`, `spec@2`, `consult@1`, `decision-log@4` **do not move** — do not touch them.

**⚠ `vlt-track`'s ack line is not at a line this brief pins.** It is a listed `extraction`
consumer (verified in `extraction.md:12` and by pin grep) but its `depends_on:` sits at a different
frontmatter offset from its siblings. **Re-derive it at build time; do not copy a line number.**

---

## F8 — `vlt-lint-full.js`: the header ack (E5) + eight in-prose tokens (E7)

**Path:** `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — **870 lines** at `d641050`.
⚠ **This is the THIRD build in this file** and the first to re-enter it after release 1 shipped
(A3). Every line below was re-derived against post-build-1, post-build-2 source; **the roadmap's
v0.16.1 numbers are all stale and must not be used.**

**The exact change — nine tokens, zero content edits:**

| Site | Now | Token |
|---|---|---|
| `:11` | `// depends_on: [...]` — **E5 parses this line; the release FAILS if it is missed** | `frontmatter@13`→`@14`, `write-verification@3`→`@4` |
| `:171` | `outbound_links` description (**inside `PAGE_SCAN`**) | `frontmatter@13`→`@14` |
| `:178` | `sources_vs_prose` description (**inside `PAGE_SCAN`**) | `write-verification@3`→`@4` |
| `:182` | `unmarked_supersession` description (**inside `PAGE_SCAN`**; the KEPT `:168`, A-R1) | `write-verification@3`→`@4` |
| `:229` | `pageScanPrompt` — **3 tokens on one line** | `frontmatter@13`×2→`@14`, `write-verification@3`→`@4` |
| `:682` | comment | `frontmatter@13`→`@14` |
| `:684` | comment | `write-verification@3`→`@4` |

**Nothing else in this file changes.** Per disposition 3, **no content re-check is owed at any of
these sites** — every citation names a section Q4 does not amend. `wiki-supersession@2` at `:182`,
`:229` and elsewhere (4 occurrences) does **not** move.

**E6 — the schema budget, MEASURED, not estimated.** Baseline measured with package-lint's own
`_E6_NODE_EXTRACTOR` against the worktree: `PAGE_SCAN` **3688**, `INDEX_SCAN` 823,
`CLUSTER_FINDINGS` 1630, `PAIR_FINDINGS` 376. The same extractor run over a simulated post-build-3
copy (all pins rewritten) returns **`PAGE_SCAN` 3688 — unchanged.**
**The E6 price of build-3 is ZERO**, because `13`→`14` and `3`→`4` are digit-count-neutral. Gate 3700;
**12 chars spare, exactly as build-1 left it.**
⚠ **Binding constraint:** that headroom exists only while build-3 makes **no content edit inside
`PAGE_SCAN` (`:158-189`)**. If the builder finds one necessary, **stop and re-measure with
`_E6_NODE_EXTRACTOR` before proceeding** — never a source char count.

**`scanFingerprint` moves anyway** (`pageScanPrompt(...) + JSON.stringify(PAGE_SCAN)` — the strings
differ even at equal length), so the first full sweep after release 2 is cold. Already priced (A26).

**Out of scope in this file:** everything build-1 and build-2 landed — `whollyWithin` and the
structured dispositions (`:596-637`), the `:686-701` retired `:664` guard, `decodeEntities`/`h2set`
(`:650-666`), `composeRulesetFingerprint` and `RULESET_SLOTS` (`:250-282`), `cacheRecords`
(`:426-450`), the return block (`:855-870`), and `para_missing_attestation: []` at `:809` (a
structural slot; the PARA scan is SKILL-side — F5 is where this build's jurisdiction change lands).

---

## F9 — `tools/package-lint.py` + `tools/test-package-lint.py`: the E7 check and its fixture case

**Current state, re-grounded:** `_e3_stray_pin` at `:728`, its exclusion docstring at **`:737-740`**;
`_e5_asset_nodes` at `:768` with `_DEPENDS_ON_LINE_RE` at `:765`; `_e4_harness_coverage` at `:857`
(introspects `^_e\d+_` callables); Group E composed at `:1029-1032`; `case_e3_stray_pin` at
`tools/test-package-lint.py:407-417`; `CASE_FLOOR = 23` at `:229`.

**The exact change:** add `_e7_asset_prose_pin_currency(root, conventions)` per disposition 2, wire
it into Group E's return after `_e5_asset_nodes`, add the covering fixture case, bump
`CASE_FLOOR` **23 → 24**.

**Why:** D3 clause 1 (A17b) makes the instrument mandatory, not optional; `brief-anatomy.md` §5's
**E4** rule makes the fixture case mandatory in the same build; §7's **R2** makes the `CASE_FLOOR`
bump mandatory. And it is the cycle's own thesis: A3 named a rule with no enforcement point, and the
answer to that is an enforcement point.

**Out of scope at this site:** E3's scope is **not** widened to `vlt-setup/assets/**` — its exclusion
is deliberate and correct (that tree is installable payload with vault-side jurisdiction, and the
workflow's pins are legitimate consumption, not stray). `SCHEMA_SIZE_BUDGET`, `RULE_CARD_BUDGET`, and
every other check are untouched.

---

## Registration

**No new skill, no new workflow, no `module-help.csv` row.** A convention edit registers nothing in
the help surface.

**But "no bump owed" is not "no cost" — and here a bump *is* owed.** The costs this build actually
carries (`brief-anatomy.md` §5):

- **The consumer walk is named and is the build's centre:** 19 re-acks across 11 files (F7), of which
  one is an **asset node** acking via a `// depends_on:` header, a different edit surface from a
  skill's frontmatter — **package-lint E5** owns that leg (F8, `:11`).
- **package-lint C6** — `vault-operating-contract.md` is edited, so `_meta/vault-rule-card.md` must
  be re-derived (its `:26` clause goes stale — F4) and its `derived_from: … sha256:` re-stamped, with
  `RULE_CARD_BUDGET` re-checked. The contract is deliberately not handshaked; it is **not free.**
- **package-lint E4 / R2** — E7 is a new check, so it owes a declaring case in
  `tools/test-package-lint.py` and a `CASE_FLOOR` bump in the same build, or the gate blocks (F9).

---

## Out of scope (dispositioned)

1. **Widening the `verified_by` value set** (a partner identifier / in-sitting sentinel) — rejected at
   Q4 with its reason on record. Do not re-litigate.
2. **A writer-shaped exemption axis** ("written during a partner sitting") — refused at Q4 on `ST-1`
   (*permission fused to provenance*), and A11 confirms `vlt-lint` could not evaluate it anyway.
3. **`para_author_unknown`'s closed `human|agent|hybrid` set, and its unnamed owning convention** —
   untouched (Q3 ⚠). Carried at §Carried forward 6 with its bound. Fixing it is a second vocabulary
   ruling this cycle does not make.
4. **E2 — `write-verification.md`'s tier-1 *"frontmatter is the source of truth"* qualifier** (`:38`)
   — **SCOPED OUT unmeasured** (A32). The owner files it to `factory/inbox/` as a `pattern`. Folding
   an unmeasured re-scoping into a 19-re-ack handshake is exactly what E2 forbids. **Do not touch
   `:38`.**
5. **E1 — A14-4's detectability-vs-remediability account** — build-4's context, and **no brief may
   assert it as a finding.** Not referenced here.
6. **Retyping or relocating any vault file.** The transition posture is shipped (disposition 7); the
   act is the vault's. `vlt-upgrade` merges, never rewrites vault content (the durability posture).
7. **`checks.md:14`/`:15`, `report.md:3`/`:13`/`:77`/`:88`, `full-scale.md` in full, `SKILL.md:74`** —
   builds 1, 2 and 4's. Verified against both BUILT briefs; take none of them.
8. **The `{field-vault}` unwind of the two parked interims** (`conventions/extraction.md` and
   `conventions/write-verification.md`, both parked 2026-08-26 against filings #15/#16). Build-3
   ships the rulings both parks wait on; **the unwind itself is a vault act at the release-2
   post-flight, re-derived against the rules in force, never executed as recorded.** Acceptance
   check (6) is its trigger and its grade.

---

## Verification (unit, at rest — lifecycle step 5)

Run all of these before writing the BUILT `status:`.

- **V1 — handshake bipartite: `uv run tools/package-lint.py`, Group E.** The check of record
  (`CLAUDE.md`; `brief-anatomy.md` §7). **E1** proves every skill consumer ↔ ack pair current across
  all three moved conventions; **E5** proves the asset node's `:11` header acks at the new versions
  and that every `.js` entry in a `consumers:` list resolves; **E2** structure map; **E3** stray pins.
  ⚠ **A hand-written `grep "<name>@" skills/` is NOT the recorded verification** — it is
  self-confirming over the files just edited. Group E derives both sides from the authoritative
  surfaces. (A grep is fine as an aid while editing; **E7 is what replaces the manual grep A3
  prescribed** — see V2.)
- **V2 — E7 proves it can fail.** Run `python3 tools/test-package-lint.py` (or the project's harness
  entry) and confirm the new case fails the gate on a deliberately-wrong body pin and passes when
  corrected. `CASE_FLOOR` is 24 and `len(CASES) >= CASE_FLOOR`. **E4 must report no uncovered check.**
- **V3 — E6 re-measured.** Re-run package-lint's `_E6_NODE_EXTRACTOR` over
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js` and record all four schema lengths.
  **Expected: `PAGE_SCAN` 3688 (unchanged), 823 / 1630 / 376.** Any other number means a content
  edit crept into `PAGE_SCAN` — stop and re-price.
- **V4 — C6.** `shasum -a 256` the edited contract, confirm `vault-rule-card.md:11`'s `derived_from:`
  matches, confirm the card is under `RULE_CARD_BUDGET` (8,000 bytes) after the `:26` edit, and
  confirm package-lint Group C passes.
- **V5 — the substance fixture pair (E3/A33), at rest.** Instrument: a **reader protocol** — an agent
  given (a) the edited `write-verification.md` §Scope rule, (b) the edited `checks.md:17`, (c) the
  edited `extraction.md` class statement, and (d) two synthetic fixture files, asked to adjudicate
  `para_missing_attestation` on each and to state which shipped clause decides it. Fixture:
  **subject** — a Layer-3 file at `{resources}/<container>/<slug>.md`, `type: record`, `author:
  agent`, no attestation pair, not named `record.md`, not in a container directory → **no finding**;
  **control** — the same file with `type: resource` → **finding**. Evidence: both verdicts and both
  cited clauses, verbatim, in the BUILT `status:`.
  ⚠ **R2 (P-18 Tier B observer) fires here: build-3 reaches for a synthetic fixture.** Recorded
  in `status:` and named at closeout, per the roundtable's interim posture. It is not a gate.
  The reason a synthetic fixture is unavoidable is grounded, not assumed: `para_missing_attestation`
  has no code implementation (`vlt-lint-full.js:809`; `full-scale.md:11`) — there is nothing
  executable to run it against.
- **V6 — two-surface agreement (A12b).** Read `contract:66`, `contract:70`,
  `write-verification.md:55` and `checks.md:17` side by side and confirm all four name the same
  exempt class in the same terms; `grep -n "operational record" skills/vlt-setup/assets/governance/
  skills/vlt-lint/references/` shows the class named at each site and defined at exactly one
  (`extraction.md`).
- **V7 — the retirements landed (P-15).**
  `grep -n "ride \`frontmatter.md\`'s declared non-exhaustive" skills/` → **zero**;
  `frontmatter.md:71` carries the PARA scoping clause and `moc`;
  `checks.md:19` cites `extraction.md` for the set rather than owning it.
- **V8 — packaging lint, mid-cycle:** `uv run tools/package-lint.py` → **A/B/C/E PASS**
  (D SKIPPED — `--expect-version` is the release gate and rides build-4).
- **R3 — legal response:** stated at `checks.md:17` and `:19` (F5 edits 3 and 5), the checks' own
  single home. Not `not applicable` — this build changes two finding classes' responses.
- **R4 — enumeration widening:** **not applicable to files** — build-3 adds no shipped file to any
  enumerated class (`tools/test-package-lint.py`'s new case is R2, not R4). Checked and declared:
  the three `consumers:` enumerations change **version, not membership**; the recognized `type:` set
  gains no new member (`moc` was already in it at `checks.md:19` and at `extraction.md:78` — F3 only
  names it in `frontmatter.md`); the skill-asset manifest is untouched.
- **Scrub:** no personal or vault-local content in any changed shipped file. ⚠ **E5-as-amended (A34)
  binds this build specifically**: the class exemption is the kind of rule that reaches for a worked
  instance, and the only worked instance in front of this brief is a live vault's. **Every shipped
  example uses placeholders** (`{resources}`, `{projects}`, `{field-vault}`) — never
  `resources/briefs/`, never a real install path (`CLAUDE.md`, worked-examples rule;
  build-15/build-18 precedent). Write A14-6 from the capture's grounded text and current vault state,
  **never from tracker #15's prospective framing** (E5).
- **Housekeeping:** delete any `**/.decision-log.md` before committing; one commit for the build.

---

## Acceptance (live — appended to the roadmap ledger)

**Seven checks — all `[ship-verifiable]`, all GATE; none field-contingent.** Cycle ruling **D3 as
amended (A17)** governs: a **BOUNDED** discharging event — at rest, at the release gate, or on the
next ordinary upgrade — is ship-verifiable and it **GATES**. Per **R1**, each names the seam its
instrument crosses. Per **D3 clause 1 (A17b)**, no check here declines an instrument that was
buildable in scope — the one instrument that did not exist (E7) is built by this build.

**(1) `[ship-verifiable]` — at the release gate — GATES.** The handshake is bipartite-consistent
across **three** moved conventions and **19** acks: `uv run tools/package-lint.py --expect-version
X.Y.Z` exits **0**, with **E1** clean over `write-verification@4` / `frontmatter@14` / `extraction@8`,
**E5** confirming `vlt-lint-full.js:11` acks both at the new versions, **C6** passing with
`vault-rule-card.md`'s `derived_from: sha256:` re-stamped against the edited contract and the card
under `RULE_CARD_BUDGET`, and **E6** measuring `PAGE_SCAN` unchanged at **3688** (build-3 must not
move build-1's schema). *Instrument:* package-lint Groups A/B/C/D/E at the release commit.
*Seam:* **convention `version:` ⟷ every consumer's declared ack**, across both edit surfaces (skill
frontmatter and the asset `// depends_on:` header), plus the **derived-artifact** seam a contract
edit opens. *Evidence:* the PASS summary line in the release commit message + the four E6 lengths.

**(2) `[ship-verifiable]` — at rest — GATES. ⚠ THIS IS THE CYCLE'S OWN THESIS, MADE ENFORCEABLE.**
The in-prose pins can no longer go stale silently: **E7 exists, is inventoried by E4, and can fail** —
mutating any one of the eight body tokens in `vlt-lint-full.js` (`:171`, `:178`, `:182`, `:229`×3,
`:682`, `:684`) to a wrong version makes `package-lint` exit non-zero naming that `file:line`, and
restoring it makes it pass; a body pin naming a convention the `:11` header does not ack also fails;
and `grep -c` over the file returns **5 `frontmatter@14` and 5 `write-verification@4`** with **zero**
`@13`/`@3` survivors. *Instrument:* `tools/test-package-lint.py`'s new E7 case (a fixture that can
fail, per `tools/package-lint.py:56-59`) plus a direct mutate-and-restore run against the shipped
workflow. *Seam:* **a convention's `version:` → the asset's header ack → the asset's PROSE
recitations of the same pin** — the seam **E3 deliberately excludes** (`tools/package-lint.py:737-740`)
and **E5 stops short of** (it reads one header line), and therefore the seam that could have shipped
stale citations to every vault through a green gate. *Evidence:* the failing and passing lint outputs
verbatim, the grep counts, `CASE_FLOOR` 24.

**(3) `[ship-verifiable]` — at rest — GATES.** The narrowing **works**, and the control still flags —
A33's replacement for the forbidden count. Over the fixture pair: a Layer-3 file bearing `author:
agent`, no attestation pair, `type: record`, outside a container directory yields **no**
`para_missing_attestation` finding; the knowledge-artifact control (identical but `type: resource`)
**does**; and the adjudicator cites the shipped clause that decided each. *Instrument:* a **reader
protocol** — an agent given the four edited shipped texts (F1, F2, F5's `:17`, plus `contract:66/:70`)
and the two fixture files, nothing else, asked for a verdict and its governing clause. *Seam:*
**shipped convention prose → the agent that actually executes `para_missing_attestation`** — the only
enforcement point this check has, because the workflow emits `para_missing_attestation: []` as a
structural slot (`vlt-lint-full.js:809`) and the PARA scan is SKILL-side (`full-scale.md:11`).
*Evidence:* both verdicts and both cited clauses verbatim in the BUILT `status:`.
⚠ **E3 binds the framing:** the 27 appear nowhere in this check. They are the observation that
motivated Q4, never a rate and never a measure.

**(4) `[ship-verifiable]` — at rest — GATES.** The contract and the convention state the **same**
exemption (A12b), so the batch does not resolve A14-7's two-surface disagreement by creating a new
one: `vault-operating-contract.md:66`'s attestation-pair leg and `:70`'s carve-out, and
`write-verification.md` §Scope rule, and `checks.md:17`'s Population carve-out all name the Layer-3
**operational-record class** in the same terms; the class is **defined in exactly one file**
(`extraction.md`) and cited — never restated — at the other three. *Instrument:* a four-site read plus
`grep -n "operational record" skills/vlt-setup/assets/governance/ skills/vlt-lint/references/`.
*Seam:* **contract ⟷ convention ⟷ shipped lint catalogue** — the three-surface agreement whose
breakage is A14-7 itself. *Evidence:* the grep output and the four quoted clauses.

**(5) `[ship-verifiable]` — at rest — GATES.** `contract:66` no longer has an unowned leg, and the
pointer resolves to something that exists: the `type:` leg names `extraction.md`; `extraction.md`
carries an explicit **closed recognized-set statement for the PARA population** (it did not before —
verified: zero occurrences of the word "recognized" in the file at `d641050`); `frontmatter.md:71`
carries the PARA scoping clause and names `moc`; and `checks.md:19` **cites** the set rather than
defining it. All four retirements landed: `grep -n "ride \`frontmatter.md\`'s declared
non-exhaustive" skills/` returns **zero**. *Instrument:* the V7 greps + a read of the four sites, at
rest. *Seam:* **governance boundary statement → the handshaked convention that owns its vocabulary**
— A14-6's whole defect, and the seam A13 showed had no valid target before this build made one.
*Evidence:* grep outputs + the four edited clauses verbatim.

**(6) `[ship-verifiable]` — bounded to the release-2 `vlt-upgrade` post-flight — GATES.** ⚠ **The
unpark trigger A14 demanded.** After the owner upgrades `{field-vault}` to release 2, the two live
`kind: parked-interim` entries — against `conventions/extraction.md` (filing #15, the PARA
recognized-`type:`-set ruling) and against `conventions/write-verification.md` (filing #16, the
`verified_by` roster ruling) — are each **re-derived against the rules in force and unwound**, and
the vault executes `para_type_unknown`'s stated legal response for its blocked files **without
declaring module vocabulary as its own** (route (b): retype to the target-folder type or relocate to
the type's home zone). *Event:* the owner runs `vlt-upgrade` on `{field-vault}` and works the
post-flight — the same post-flight that ran for v0.16.2, and therefore an event the plan already
schedules. *Performer:* the owner. *Vault:* `{field-vault}` only (it is the vault holding the parks).
*Seam:* **shipped ruling → the parked vault-local interim it was blocking** — the loop A14-6 and
A14-7 were filed to close. *Evidence:* the two parked entries removed or resolved, and the response
executed on at least one named file, recorded in the discharge run.
⚠ **A34/E5 bind the evidence too:** record it with placeholders, never a real install path.

**(7) `[ship-verifiable]` — bounded to the first full `{field-vault}` sweep after release 2 —
GATES.** The transition posture reaches the measured population (A12), and its reach is **measured
rather than assumed**: the sweep reports the **`type:` distribution** of every
`para_missing_attestation` entry across §Scope rule's jurisdiction list — the distribution A12 found
**unmeasured** — and **every** entry has a legal response available to it under the amended
`checks.md:17` (retype, attest, or human-authored ruling), with pre-adoption entries rendered
**informational**. The check **can fail**: an entry with no available response, or an entry rendered
as a violation where the pre-adoption clause should apply, fails it. *Instrument:* the first full
`vlt-lint --full` sweep after upgrading to release 2, read against the persisted `{lint_reports}`
archive baseline that recorded the 27. *Event:* the owner runs `vlt-lint --full` after upgrading —
already scheduled; note that sweep is **COLD by construction** (build-2's record shape, build-3's
three convention digests and `checks.md`'s), which is not a regression. *Performer:* the owner.
*Vault:* `{field-vault}` only. *Seam:* **the amended jurisdiction rule → the live PARA corpus that
predates it** — the only seam where a narrowing that legalizes just-written files gets caught
legalizing nothing. *Evidence:* the distribution table and the per-entry response, in the discharge
record.

---

## Next lifecycle move

A **fresh builder session** implements this brief via `bmad-workflow-builder`. Exit obligations:
rewrite this brief's `status:` to a **BUILT record with numbered deviations** (including R2's
synthetic-fixture observation), delete any `.decision-log.md`, **one commit for the build**. Then
**`brief build 4`** — the last build of release 2, which carries the version bump and the
`--expect-version` gate.

⚠ **Two cycles remain open and `factory/CYCLE` holds one line** (A24). Never run
`acceptance-discharge` or `cycle-closeout` headless while that is true.
