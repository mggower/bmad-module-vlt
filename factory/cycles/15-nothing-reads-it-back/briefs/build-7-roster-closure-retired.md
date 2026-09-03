---
title: 'Build #7 — retire the `verified_by` roster closure: after this ships, a partner''s attestation is authorized once — by the container''s `writers:` list where one is declared — instead of twice, by a roster that cannot admit a partner'
status: >
  BUILT 2026-09-02 — F1 → F4 → F2 → F3 → F5 → F6 → F7 → F8 → F9 landed in the brief's order on
  `5eb90b5`; **F10 (the 0.18.0 version bump) deliberately NOT applied — it is `vlt-release`'s
  step, per the build's instructions (deviation 1)**; checks (1)–(4), the four at-rest
  `[ship-verifiable]` checks, PASS at rest (below); (5) field-contingent, unfired. **Handshake as
  shipped (R1, A1):** `write-verification.md` `version: 5 → 6` (`:11`), `last_updated` `:4`
  2026-09-02, `consumers:` `:12` unchanged; re-acked `write-verification@6` at
  `vlt-ingest/SKILL.md:4`, `vlt-extract/SKILL.md:4`, `vlt-research/SKILL.md:3`, `vlt-lint/SKILL.md:4`
  (no other pin on those lines moved), and `vlt-lint-full.js` header `:11` (E5) + body pins `:241`,
  `:245`, `:297`, `:911` (E7) — grep `write-verification@5` / `v5` over `skills/`, `tools/`,
  `.claude-plugin/` → 0 outside CHANGELOG history. `frontmatter.md` stays `version: 14` (prose
  re-nouns at `:78`/`:82`/`:296(c)` only, A7; `:71`/`:294` intact); `extraction.md` no hunk.
  `handshake-check.py` → `9 conventions, 39 consumer pins — bipartite-consistent`;
  `package-lint --expect-version 0.17.1` → `A/B/C/E PASS, D PASS — vlt 0.17.1` (E1/E3/E5/E7 clean;
  E6 by the extractor: `PAGE_SCAN` **3265** (≤ 3700), `INDEX_SCAN` 838, `CLUSTER_FINDINGS` 1630,
  `PAIR_FINDINGS` 376 — unchanged; `node --check` ok). **C6 (F4):** contract `:68` edited (the
  identities/admission clause only — the `open` default, inheritance, `{wiki}` removal and the
  human-gate byte-identical; `:70` intact); rule card `:26` wording unchanged, `derived_from:`
  re-stamped `sha256:470aaf2816f7a60e572af3a44ff7ae47d1bec641145830eda7678433ae253b9d (derived
  2026-09-02)` = `shasum -a 256` of the edited contract; card 7,295 bytes (< 8,000).
  **Cache-mover record (disposition 5):** `scanFingerprint` `c44d8912ed750afe1cdf` →
  `fe29c6f398d02c6b1cdf` (the `:297` prompt literal); `convention_digests[write-verification]`
  `2590f56e44a765ca3be31bd4985e9b06d24fdae139b825ea91df994a18c73d95` →
  `5e101c13c6cf04faee28a9f89d5b92df60c0010d9bde4d3616a522c99a3373ed`;
  `convention_digests[frontmatter]` moves again from build-6's `fca83321…` →
  `1255c3add9bf5e4df6d2e84df46c0fb3c48c7583e85fb12f7ff5eafd5d4b7f43`; `wiki-supersession`
  `6f52b678…` unchanged — v0.18.0's first sweep is cold on three movers (§Release item 3).
  **Check (1):** PASS at rest — Group E + handshake-check above. **Check (2) — grep manifest:**
  0 hits across `skills/` (rule card included) for `that are write ops`, `write-op
  `local_consumers:``, `write-op registrants`, `membership and ceiling`, `write-op qualifier`,
  `the attesting op`, `must be a **write op**`, `any of its identities`, `any match`, `admitting on
  **any**`, the semantic variants `an op listed in `consumers:``, `rostered attester`, `write ops
  only`, and the wider `write ops` / `write-op`; presence: `lint attests **narrowly**` → 1
  (`write-verification.md`), `handshake reasons alone acquires no attestation authority` → 1,
  `writer of record` → 2 (`checks.md:20`, contract `:68`), `para_writer_scan` → 4 files (`report.md`,
  `checks.md`, `lint-para-facts.py`, `lint-report-check.py`; the SKILL names the flag, not the key —
  deviation 4). Reader pass over each edited paragraph for surviving nouns of *roster* / *op-only*:
  `write-verification.md:47` carries *roster* twice — *"the roster of operation skills that answered
  it a second time"* (the retired thing, named as retired) and *"a handshake roster, not a grant"*
  (`consumers:` as what it is); `frontmatter.md:296(c)` *"never this roster's"* (the registration
  roster, denied attestation authority); `checks.md:20`, contract `:68`, card `:26` carry none.
  Byte-identity (`git diff -U0 5eb90b5`): `checks.md` hunk `:20` only, word-diff from *"and resolve
  the file's writer identities"* to just before *"A file resolving no identity"* (`:19` intact);
  `write-verification.md` `:4`/`:11`/`:46`–`:47` only (`:55` intact); `frontmatter.md`
  `:78`/`:82`/`:296` only; contract `:68` only; `extraction.md` no hunk; `report.md` the inserted
  fence line + the persist-gate clause + the write-posture paragraph. The walker's `M` predicate is
  untouched: `P`/`M` over `fixtures/build-5-para/` are `9`/`3` before and after (the `--line` string
  byte-identical), over `fixtures/build-7-para/` `15`/`1`. **Check (3) — the reader protocol
  (`fixtures/build-7-reader-protocol.md`) over `fixtures/build-7-para/` against the hand-written
  oracle `build-7-expected-findings.json` (oracle first):** shipped table — `draft.md`,
  `agent-note.md`, `human.md`, the three charters, `any.md` (the residual), `hybrid-op.md`,
  `plain.md`, both `delta/` files → no finding; `note.md`, `sub/deep.md` (inherited), `ratified.md`
  (D-E) → fire; `unattested.md` → fires on the author leg AND is in M (deviation 2); the `{wiki}` page
  in no list; the `fc44027` any-match run yields the `pre_build` table, differing on exactly
  `ratified.md` (failability). **Check (4):** the walker's `writers`/`declaring_ancestor`/`counts.D`
  and `--writer-line` deep-equal the oracle under `uv run` and bare `python3` (byte-identical output);
  edge runs in scratch — flow and block `writers:`, a quoted entry, `writers: []` (not declaring), a
  charter without `writers:` beneath a declaring parent (inherits the parent), a file at the `--dir`
  root and one with no charter anywhere (`null`) — all as specified; `lint-report-check.py schema`
  deep-equals the re-derived `build-5-expected-schema.json` at **18 / 74 / 5 / 1**, `SCHEMA_FLOOR` 18
  unchanged; the build-5 shape harness green at **39 rows, 0 failed** with rows (7a)–(7e) added
  (absent → `key missing: flag_for_human.para_writer_scan` in both modes; `O` off by one →
  `para_writer_scan: rendered line does not match the walk` and nothing else; equal → ok; the red leg
  — the ok report under `fc44027`'s fence reports the key EXTRA, never mandated). Prior harnesses:
  build-2 key, build-3 type, build-4 return → *all expectations hold*; build-6's walker step → `P: 9`.
  Scrub: 0 hits for machine paths / the owner's username / the field vault's name across `skills/`
  and the build-5/-7 fixtures; no `.decision-log.md`, no `__pycache__`. Field count 27 consumed as a
  count; specimens `0/27` stated in `build-7-para/README.md`. **Deviations/notes:** (1) **F10 not
  applied** — both version strings stay `0.17.1`; the bump, the `--expect-version 0.18.0` lint and
  the CHANGELOG text (§Release, items 1–4) are `vlt-release`'s, per the build instructions. (2)
  **`unattested.md` fires `para_writer_unauthorized`** (oracle + protocol), not *"not this net"* as F9
  and check (3) expected: the file resolves `agent` on the author leg and `[human, librarian]` does not
  admit it — the shipped text (and the pre-build text) both fire; only a file resolving *no* identity
  is left to the honesty nets. The fixture is kept where the brief put it and the oracle records the
  honest verdict — two nets, one file. (3) **F1's replacement text carried *"the roster of write
  ops"***, which verification 2's own manifest forbids (`write ops` → 0); shipped as *"the roster of
  operation skills"*. (4) **`vlt-lint/SKILL.md:47`** — the brief's wording put the router 76 bytes
  over its 12,000-byte budget (C, 11,982 at `5eb90b5`); shipped as a +2-byte edit naming
  `--writer-line` beside `--line` (*"keep its `--line`/`--writer-line` outputs for Step 5"*) — the
  key names live in `report.md`, so `para_writer_scan` is present in 4 files, not 5 as verification
  2 predicted. (5) The F2 pointer clause (*"the denominated line `para_writer_scan:` (`report.md`)
  carries N / D / O from the walker"*) sits inside the join hunk, before *"A file resolving no
  identity"*, so verification 3's word-diff bound holds. (6) The build-5 facts oracle
  (`build-5-expected-para-facts.json`) re-derived (two facts per file + `counts.D` = 5) and
  re-compacted to its one-line-per-file form; `build-5-report-ok.yaml` gained the
  `para_writer_scan:` line (`9 judged; 5 under a declaring ancestor; 4 passed on open posture …`).
  (7) `git status` at the start showed the roadmap/platform files modified — those were the parent
  session's, already committed; this build touches neither.
module_code: 'vlt'
created: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-09-01-170000-supersession-the-verified-by-roster-is-superseded-by-the-authorization-net.md (A15-13 — the roster closure at `write-verification.md:47` retired, restated never deleted; the three preserved constraints (pair kept, authorization answered once, open+PASS undisturbed); the residual floor question → Q5 NO FLOOR; park #16; ST-6 instance 3)'
roadmap: 'factory/cycles/15-nothing-reads-it-back/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-01/02): build-7 bullet (binds D5, Q5, Q9; += handshake R1); D5.3/D5.4/D5.5 (pair kept, authorization once, open+PASS kept); Q5 NO FLOOR; Q9 as resolved at the roundtable (A18, owner ruling D-D — build-7 carries NO gating Cycle 14 clause); roundtable A1 (`write-verification` 5 → 6, five re-acks incl. the workflow header and body pins; the `local_consumers:` field notice), A7 (`:47` restated never deleted; `frontmatter.md:78/:82/:296(c)` re-nouned with NO bump; the non-op attester sentence; promise subject → a partner''s), owner ruling D-E (the one-line `checks.md:20` change), A8 (one denominated line — D2 (iv) extends here), A20 reverse (the contradiction eliminated by narrowing, no precedence statement); R1/R2 interim postures; D2 (iv) by A8''s extension.'
risk: 'low-moderate — ONE convention rule change (`write-verification` 5 → 6) with a five-consumer walk that crosses two edit surfaces (four `SKILL.md` pins + the workflow asset''s `// depends_on:` header AND four in-prose body pins — package-lint E5 + E7); `frontmatter.md` is re-nouned with NO bump (A7, explicit); the operating contract''s resolver sentence at `:68` moves one clause (grounding correction 3 — the roundtable read it as untouched) so package-lint C6 engages (rule card re-derived + `sha256:` re-stamped); the workflow edit is pin-only but the prompt literal moves `scanFingerprint` (v0.18.0''s first sweep is cold by construction — the CHANGELOG states it); one new scalar line in `report.md`''s machine-read fence (the schema fixture re-derived, `SCHEMA_FLOOR` 18 unchanged — the line is nested); `lint-para-facts.py` gains two facts and one count so the new line''s denominator comes from the walker, not the agent (D2 (iv)). This is the v0.18.0 release build — both version strings bump here.'
---

# Build #7 — retire the `verified_by` roster closure

**Promise (owner-ratified 2026-09-02; subject corrected at the roundtable, A7; carried verbatim):**
*After this ships, a **partner's** attestation is authorized once — by the container's `writers:`
list where one is declared — instead of twice, by a roster that cannot admit a partner.*

Two shipped clauses cannot both be satisfied today. `write-verification.md:47` limits the legal values
of `verified_by:` to *"this file's `consumers:` that are write ops, plus write-op `local_consumers:`
registrants"* — a roster of operation skills. `checks.md:20`'s authorization net resolves *"the
attestation `verified_by:` → that partner slug"* — a leg no conformant vault can exercise, because a
partner slug is not a write op. The field consequence is exact: **27** partner-written Layer-3 files
carry `author: agent|hybrid` and no attestation pair, the tier-1 pass *is* run on them, and the module
forbids recording it (A15-13; park #16 re-parks against this filing). This build retires the roster's
**closure** — the membership rule stated as a property of the actors that existed when it was written
(`ST-6`, instance 3) — and restates the value set as a property of the capability: *whatever the
nearest declaring container's `writers:` join admits; unconstrained where none declares.* The
authorization question is then answered **once**, by the net built to answer it (D5.4), and
`checks.md:20`'s partner-slug leg becomes exercisable for the first time — the contradiction is
**eliminated by narrowing**, no precedence statement (A20 reverse; Arc 9 D5).

**The promise is capability, never a cleared backlog** (ruling-time over-claim rejected, on record in
the build-7 bullet): the 27 files clear only when partners re-attest them. A check graded on that count
dropping to zero at release would fail honestly, and none is written here.

**Separate from build-6 on the filing's own argument** (*"folding two retirements into one build is
how a structural change becomes unreviewable"*) — this is the cycle's **second** retirement brief, and
build-6's §9 site table is the precedent this brief's §9 follows. All rejected alternatives in the
parent filing are settled — a floor on unrostered attesters (Q5), re-widening the roster by naming more
actors (`ST-6`'s predicted bad fix), stamping a rostered op as a false provenance claim, ruling the
files human-authored — **do not re-litigate.**

## Brief-time dispositions

*(Headless run. Every disposition below is the briefer's, recorded where it applies; none re-rules an
ideation ruling. Dispositions 2 and 4 are the load-bearing judgment calls — read them before F2 and
F5.)*

### 1. The restated value set — the exact sentence, and the two clauses that survive verbatim *(A7)*

**Ruling: `write-verification.md:47` is rewritten, not deleted, and its new value-set sentence is
exactly A7's:** *"the `verified_by` value set is **whatever the nearest declaring container's
`writers:` join admits; unconstrained where none declares** (`vlt-lint`'s `para_writer_unauthorized` is
the net that answers it — once)."* `frontmatter.md:78` and `:82` point here (*"not restated here"*)
and would dangle on a deletion. Two clauses survive **verbatim**, because neither is the closure:
*lint attests narrowly — it writes the pair only on files its own auto-fix touched … Lint never attests
a file it merely read*; and *a skill added to `consumers:` for handshake reasons alone acquires no
attestation authority*. The second survives because it is still true and still needed: `consumers:`
is a handshake roster (`checks.md:40`), and after this build it grants nothing about attestation in
either direction — the sentence now reads as a clarification of what the roster is *for*, not as a
ceiling on the set. The phrases that go: *"that are write ops"*, *"plus write-op `local_consumers:`
registrants"*, *"The roster is membership and ceiling, never an automatic grant"*, *"the write-op
qualifier binds the whole set"*. (F1 quotes current and replacement text.)

### 2. What `writers:` admits when the attester is judged — the join stated once, roster-free *(owner ruling D-E; Q5)*

D-E rules the one-line `checks.md:20` change: *the `verified_by:` identity must itself be admitted by
the nearest declaring `writers:` list — never carried by the `author:` leg.* It does not say what
`agent` in a `writers:` list admits once specific attester slugs are legal values, and the shipped
vocabulary (`extraction.md:157`: each entry *"either `human`, `agent`, or a specific partner slug"*)
predates that question. **Ruling, roster-free — the only reading that keeps every shipped rule
satisfiable:**

- **Identities have a class and, optionally, a name.** `author: human` → `human`; `author: agent` →
  `agent`; `author: hybrid` → `human` (the honesty rule, unchanged); a `verified_by:` value → **that
  identity, by name** — an agent-kind identity whether it is an op (`vlt-ingest`) or a partner
  (`librarian`). *(Q5: the value is unconstrained; there is nothing to classify it against, and the
  brief adds no enumeration.)*
- **`writers:` admits:** `human` → the human class; `agent` → **every agent-kind identity, named or
  not**; a specific slug → that identity exactly.
- **The join (D-E):** where `verified_by:` is present, **the attester is the writer of record** — the
  file passes iff the attester is admitted, and the `author:` leg is **not consulted** (it can neither
  rescue nor refuse: a specific identity is the most specific thing the file says about who wrote it).
  Where no `verified_by:` is present, the `author:` leg is judged as today. A file resolving no identity
  at all stays with the honesty nets. **Undeclared containers pass `open` and are counted** (D5.5, A8).

**Why `agent` must admit any attester.** The pair is *required* on every `author: agent|hybrid`
knowledge artifact in the population (`para_missing_attestation`, D5.3). If `agent` admitted only the
`author:` class and not the attester, then under D-E a `writers: [human, agent]` container would
refuse **every conformant agent-written file** (each carries an attester the list does not name) — the
declared posture *"agents may write here"* would be unsatisfiable, and the only escape would be a
roster telling `agent` which slugs are ops: `ST-6`'s predicted bad fix. So `agent` is the class.
**The residual, stated so it is not discovered later:** under a declared `agent`, an arbitrary attester
value (`verified_by: banana`) **passes** — that is the human's declared posture (any agent), and Q5
ruled no floor. D-E's own example — `verified_by: banana` passing wherever `writers:` names **`human`**
via the hybrid → human carry — is **closed**: under `[human]` the attester is agent-kind and refused.
**Why the author leg is not consulted when an attester is present.** The alternative (both legs must
pass) refuses a `writers: [librarian]` container's own hybrid files (author → `human`, not listed) —
the human who named exactly one partner would be told their ratified drafts are unauthorized. Judging
the attester alone admits them, and refuses the same file under `[human]`, which is D-E's intent.

**Consequences this ruling accepts, named:** (a) a container declaring only `[human]` refuses every
attested file — *no partner drafts here* is a legitimate posture and the finding's legal response
(ratify a `writers:` line / relocate / rule human-authored) already covers it; (b) `vlt-lint`'s narrow
attestation on a file its auto-fix touched inside a container that refuses `agent` surfaces as a
`para_writer_unauthorized` naming `vlt-lint` — the honest report of an agent write into a container that
admits none (the `para_*` nets are never auto-fixed, so the case is confined to the wiki-adjacent
frontmatter fixes; noted, not designed around); (c) the field vault today declares **zero** `writers:`
lists (counted at brief time, read-only, counts only) — every field file passes `open` after this
build exactly as before, so the ruling changes no field verdict at v0.18.0 and is exercised at rest by
the fixture (check (3)).

**Where the join is stated:** once, at the operating contract `:68` (the resolver's home — grounding
correction 3: its *"admitted when **any** of its identities is in that list"* clause is the old join
and must move); `checks.md:20` carries the check-side restatement D-E ordered; `extraction.md:157`'s
*"a specific partner slug"* is read as *a specific slug* and **not edited** — `extraction` moved to v10
in build-6 and a re-noun there would be a second bump for a word the resolver already governs by
pointer (*"never restated here"*). Recorded as a prose-precision the builder may not widen.

### 3. Prose re-nouns in `frontmatter.md` with NO `frontmatter` bump *(A7 — explicit)*

**Ruling: `frontmatter.md:78`, `:82` and `:296(c)` are prose re-nouns; `frontmatter` stays at v14 and
its ten consumers are not walked.** A7 says so to stop a briefer picking `frontmatter@15` + ten
re-acks. The test (CLAUDE.md): a *rule* change bumps; a clarification does not. `:78`/`:82` define the
*field* and delegate the value set by pointer — the pointer's target changes, the pointer does not
(*"the attesting op"* → *"the attester — an op, or a partner"* is the noun catching up with the target).
`:296(c)` is the one clause that **restates** a rule (*"the base roster is the ceiling … a registrant
must be a write op"*) — it becomes a version-free pointer: `local_consumers:` **keeps** its handshake
role (`checks.md:40` walks it with the same vocabulary as `consumers:` — untouched) and **loses** its
attestation-widening role (there is no attestation ceiling left to widen). That loss is a consequence
of `write-verification`'s rule change, which is bumped; the sentence at `:296(c)` that described the
old consequence is corrected, and `frontmatter.md`'s own rule — what the field is, who may write it,
(a) and (b) — is unchanged. **`convention_digests[frontmatter]` moves again** (the bytes change;
`frontmatter` is a `SCANNER_CONVENTIONS` member) — already a v0.18.0 cold mover via build-6, so this
adds no new cold cause; recorded so the release statement is exact.

### 4. The denominated line — key name, composition, and the instrument that produces it *(A8; D2 (iv))*

A8 names the line `para_writer_unauthorized: N judged; D under a declaring ancestor; O passed on open
posture`. **That key already exists at `report.md:50` as a per-file list** (`[<para-file: writer 'X' …`),
and the fence grammar (`report.md:15`, rule 2) types a key by its value's first character — one key
cannot be both. **Ruling: the line is `para_writer_scan:`**, a scalar mirroring `para_scan:` (`:46`),
placed **immediately before** `para_writer_unauthorized:`, rendered in **both modes**, never omitted:
`para_writer_scan: <N judged; D under a declaring ancestor; O passed on open posture (instrument:
scripts/lint-para-facts.py)>`. **The roadmap's A8 key literal is corrected by a dated note** (grounding
correction 4). The list slot is untouched.

**Composition, D2 (iv) honoured — the denominator is produced by an instrument other than the net's
judge:** `N` = the walk's `P` (every population member is resolved, and a file that resolves no
identity is still *judged* — its answer is *left to the honesty nets*); `D` = members whose nearest
declaring ancestor exists; `O = N − D`. `D` needs a fact the walker does not emit today — the nearest
ancestor `charter.md` carrying a `writers:` list. **`lint-para-facts.py` gains two per-file facts and
one count** (F5): `writers` (the list, on files that carry one — charters), `declaring_ancestor` (the
walk-relative path of the nearest `charter.md` with a non-empty `writers:` at or above the file, or
`null`), and `counts.D`; plus `--writer-line`, printing the exact `para_writer_scan:` value. Facts,
never verdicts: whether a writer is *admitted* stays the SKILL's judgment against `checks.md:20`. The
persist gate compares the rendered `para_writer_scan:` to the walker's `--writer-line` **by string
equality**, exactly as it compares `para_scan:` (F6) — so a hand-composed line with plausible numbers is
refused, which is the whole of what A8 asked for made enforceable (this cycle's thesis applied to its
own new line). The fence gains one line ⇒ `fixtures/build-5-expected-schema.json` is **re-derived**
(`lint-report-check.py schema`, then deep-equal in the build-5 harness): top-level keys **18 → 18**
(the line is nested under `flag_for_human`), key paths **73 → 74**; `SCHEMA_FLOOR` stays 18.

### 5. The handshake — `write-verification` 5 → 6, and the exact roster *(A1; R1 interim posture)*

**Ruling: this is a convention RULE change; `version: 5 → 6` at `write-verification.md:11`;
`consumers:` at `:12` unchanged (`[vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js]`).**
Re-acks, re-grounded at `fc44027` — **the roundtable's A1 line numbers are stale** (grounding
corrections 1–2): `skills/vlt-ingest/SKILL.md:4`, `skills/vlt-extract/SKILL.md:4`,
**`skills/vlt-research/SKILL.md:3`** (its `depends_on:` is line 3, not 4), `skills/vlt-lint/SKILL.md:4`,
and `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the `// depends_on:` header at **`:11`**
(E5) **and every body pin, four of them** (E7 fails the tag on any one): **`:241`** (the
`sources_vs_prose` description literal, *"per write-verification@5"*), **`:245`** (the
`unmarked_supersession` description literal, *"per write-verification@5 Scope rule"*), **`:297`** (the
`pageScanPrompt` literal, *"per write-verification@5, the wiki-page tier-1 item"*), **`:911`** (a code
comment, *"under write-verification@5's Scope rule"* — E7's pattern reads comments too). Nothing else
under `skills/`, `.claude-plugin/`, `tools/` carries `write-verification@` (grep at brief time: exactly
the eight lines above plus `CHANGELOG.md` history). **R1's interim posture is discharged by this
disposition** — the `handshake:` line the bullet carries by A1 is honoured in full.

**What the workflow edit moves.** `:241`/`:245` sit inside `PAGE_SCAN` — a one-character edit each
(`5` → `6`), so E6's `JSON.stringify(schema).length` is **3265 → 3265** (measured at brief time with
package-lint's own extractor: `PAGE_SCAN` 3265, `INDEX_SCAN` 838, `CLUSTER_FINDINGS` 1630,
`PAIR_FINDINGS` 376; budget 3700). `:297` sits inside `pageScanPrompt`, which is a `canonicalScan`
input (`:315`) — so **`scanFingerprint` moves** by this build; build-4 already moved it, and the
`write-verification` digest moves regardless (`SCANNER_CONVENTIONS`, `:290`). v0.18.0's first sweep is
cold by construction on **three** movers — build-4 (scan surface), build-6 (`frontmatter.md` bytes),
build-7 (`write-verification.md` bytes + the prompt literal) — the release statement names all three
(§Release).

### 6. The `local_consumers:` field notice *(A1)*

**Ruling: the notice is CHANGELOG text at release, not a mechanism.** A vault-minted registrant on
`write-verification` acks `@5` in its own `depends_on:`; the module cannot re-ack a vault-minted op.
After the upgrade, `checks.md:40`'s `local_consumers:` walk reports **one expected `convention_drift`**
(*"write-verification@6 → <registrant> acks @5 (stale)"*) until the vault reconciles the registrant by
ceremony (`vlt-mint`'s convention-edit route). The field vault carries exactly one such registrant
(read at brief time, counts only) — the notice is not hypothetical. Text in §Release.

### 7. Q9 — build-7 carries NO gating Cycle 14 clause *(A18; owner ruling D-D)*

**Ruling: no Cycle 14 sub-clause is appended to this build's ledger bullet.** Q9 as resolved: build-6
carries Cycle 14 build-3 (6) clauses (a)+(c); clause (b) — park #16 — was *"already satisfied in
substance"* by Cycle 14 (the park was re-derived and superseded in the log; what it lacked was a legal
exit, which this retirement supplies). Park #16's **unwind** is the vault-act half: it rides check (5)
`[field-contingent]` on the first v0.18.0 `parked_interims_review:` — the owner's act, never a gate.
Every `- [ ]` in this ledger bullet is this cycle's own.

### 8. The instrument for the join is an agent-run reader protocol, proven failable — and the specimens are counts *(P-18 Tier A)*

**Ruling: check (3)'s instrument is a named reader protocol over `fixtures/build-7-para/` against a
hand-written oracle, on build-6's model** — `para_writer_unauthorized` is a governance check the SKILL
judges from `checks.md:20`; no executable renders the verdict (the walker emits facts). The oracle is
written **before** the protocol runs, carries cases only the new join yields, and the protocol is run
once against `fc44027`'s `checks.md:20` text to show a different table (failability). **Specimens:
`0/27`.** The filing observed 27 files (six partner domains) and preserved **counts only** — no path, no
frontmatter fragment (the filing is a supersession, not a defect specimen); and the observed state
(*unattested, cannot be attested*) is the state the retirement makes escapable, not one the net judges
— the pre-fix specimens cannot exercise the post-fix join by construction. The fixture is therefore
authored **from the failure's shape as the filing states it** (`author: agent|hybrid`, partner-written,
Layer-3, outside `{wiki}`) plus the D-E cases, and it says so in its README. The low figure is the
honest one; hiding it behind a synthetic count is the `ST-5` shape.

### 9. Retirement (P-15; obsolescence beat A20; R2 interim posture) — SUBSTANTIVE, and the site list is grep-derived

*(The cycle's second retirement brief; `brief-anatomy.md` still carries no retirement section — [P-24]
queued. R2's interim posture applies as build-6 applied it: every restatement and pointer of the
retired rule enumerated by grep, a disposition per site, and the population statements that must NOT
move. The roundtable's A7 hand-enumeration is the floor. Greps ran at `fc44027` over
`skills/vlt-setup/assets/governance/_meta/`, `skills/vlt-*/references/`, `skills/vlt-*/SKILL.md`,
`skills/vlt-setup/assets/workflows/`, `skills/vlt-setup/assets/module.yaml`, `tools/`, `CHANGELOG.md`
for: `write op`, `write-op`, `write ops`, `roster`, `verified_by`, `attesting op`, `attestation
authority`, `ceiling`, `membership and ceiling`, `any of its identities`, `writers:`, `local_consumers`,
`write-verification@`, `attest`, `tier-1`.)*

**Found: 6 restatement/pointer sites of the retired rule (the roundtable's A7 named 4 — the two it did
not name are the operating contract's resolver clause at `:68`, which carries the OLD join, and the
CHANGELOG's historical record), 14 sites that must NOT move, 6 that survive with unchanged wording.**

| # | Site (re-grounded at `fc44027`) | What it says | Disposition |
|---|---|---|---|
| R1 | `write-verification.md:47` | the closure — *"this file's `consumers:` **that are write ops**, plus write-op `local_consumers:` registrants … The roster is **membership and ceiling** … the write-op qualifier binds the **whole** set"* | **RETIRED — restated, never deleted** (F1, disposition 1). The two clauses named in disposition 1 survive verbatim. |
| R2 | `frontmatter.md:78` | `verified_by: <the attesting **op** — value set in write-verification.md §Attestation>` | **RE-NOUNED, no bump** (F3): *the attester — an op or a partner; value set in …*. Pointer target unchanged. |
| R3 | `frontmatter.md:82` | *"the **operation** that ran tier-1 on this file. The legal value set is the attestation contract's … not restated here."* | **RE-NOUNED, no bump** (F3): *the attester — an op, or a partner — that ran tier-1 on this file*; the pointer clause survives verbatim. |
| R4 | `frontmatter.md:296(c)` | *"the base roster is the **ceiling** of what registration can grant — for attestation authority specifically, a registrant must be a **write op** (`write-verification.md`, §Attestation …)"* | **RETIRED — becomes a version-free pointer, no bump** (F3, disposition 3): (c) registration grants a handshake seat (`checks.md:40`) and nothing about attestation — the attestation contract is `write-verification.md` §Attestation. `local_consumers:` keeps its handshake role, loses its attestation-widening one. |
| R5 | `vault-operating-contract.md:68` — the resolver's join | *"A writer is admitted when **any** of its identities is in that list: `author: human` reads as `human` … a specific partner slug is read from the attestation `verified_by:`."* | **MOVED — one clause** (F4, disposition 2): the any-match join is the rule D-E replaces. ⚠ **Not on the roundtable's list** — A20 read `:68` as *"already reads a partner slug — nothing to do"*; it does read the slug, and it also says *any*, which the `checks.md:20` change would otherwise contradict one file over (the contradiction A15-13 is about, re-created between the contract and its check). Contract edit ⇒ **C6**: rule card re-derived, `sha256:` re-stamped (card `:26`'s wording — *"admits you"* — is already right; hash only). |
| R6 | `CHANGELOG.md` v0.17.0 §Governance item 1 / v0.17.1 item 2 (the `write-verification` v3→v4→v5 record) and v0.16.x's B9-4 *"lawful, checked route onto a shipped convention's roster"* | history of the roster and its exemptions | **HISTORY — not edited.** The v0.18.0 block names what is retired (§Release). |
| P1 | `checks.md:20` — everything but the join | the net's purpose, the nearest-declaring-ancestor walk, the **`open` + PASS** default, sub-container inheritance, the `{wiki}` non-exception, the informational posture, the legal response (*human ratifies a `writers:` change / relocate / rule human-authored*; **never auto-fixed**) | **DOES NOT MOVE** (D5.5; the one-line change is the join only — F2). |
| P2 | `checks.md:19` | the `para_*` population + the closing nets | **DOES NOT MOVE** — the population every `para_*` net judges is unchanged; A15-13's *"no population is left uncovered"* rests on it. |
| P3 | `write-verification.md:55` — the Scope rule | the self-marker jurisdiction (*`type: wiki\|research\|project\|area\|resource` with `author: agent\|hybrid` and no attestation*), the operational-record exemption by class, *"fusing permission to provenance is the write-path failure this exemption exists to prevent"*, the jurisdiction boundary | **DOES NOT MOVE** — and *"fusing permission to provenance"* now reads true (A20). The five-value enumeration build-6 flagged (P16 there) is a sibling completeness-claiming list, **not this filing's ask** — §Out of scope. |
| P4 | `write-verification.md:44`-`:46` — the pair, the freshness pointer, *"After tier-1 completes, write `verified_by: <this op>` …"* | the attestation pair contract | **DOES NOT MOVE** (D5.3) — except `<this op>` at `:45`, which gains the non-op attester sentence beside it (F1; A7). |
| P5 | `extraction.md:190`, `:192` | the operational-record class carries **no** pair; `para_missing_attestation`'s carve-out | **DOES NOT MOVE.** |
| P6 | `extraction.md:157`, `:168` | `writers:` — *"each either `human`, `agent`, or a specific partner slug"*; resolver by pointer to the contract | **DOES NOT MOVE** (disposition 2: *a specific slug* read as written; no `extraction` bump). |
| P7 | `vault-operating-contract.md:70` | container files carry no pair; the class keys the exemption | **DOES NOT MOVE.** |
| P8 | `report.md:42` (`para_missing_attestation`), `:46` (`para_scan:`), `:50` (`para_writer_unauthorized:` list) | the per-file slots and the walk denominator | **DOES NOT MOVE** — `:50`'s list survives beside the new scalar (disposition 4). (The roundtable's `report.md:39` cite is the same slot, drifted by build-5's insertions — grounding correction 5.) |
| P9 | `lint-para-facts.py` — the predicate `M` (`:106`) | *attested = `verified_by` AND `verified_at` both present and non-empty* | **DOES NOT MOVE** — the pair is a presence test, never a value test (D5.3); the script gains facts, not a verdict (F5). |
| P10 | `checks.md:40` | `local_consumers:` walked with the same vocabulary as `consumers:`; registrants **inside** the handshake | **DOES NOT MOVE** — the handshake role `:296(c)` keeps. |
| P11 | `frontmatter.md:294`, `:296(a)`, `:296(b)` | the vault-writable member set; sanctioning; the registrant's flat pin | **DOES NOT MOVE** (only (c) moves). |
| P12 | `vlt-ingest/SKILL.md:182`, `vlt-extract/SKILL.md:110`, `vlt-research/SKILL.md:88`, `fix-and-file.md:18` | the op-side attestation instructions (`verified_by: vlt-ingest` / `vlt-extract` / `vlt-research` / `vlt-lint`, narrowly) | **DO NOT MOVE** — an op naming itself is a legal value after this build exactly as before (an op is an agent-kind identity; disposition 2). The pins on those SKILLs' line 3/4 move (F7); the instructions do not. |
| P13 | `vlt-query/SKILL.md:51` | resolves the write posture before a PARA write; *where a declared posture does not admit `agent`, propose the write* | **DOES NOT MOVE** — the write-time reading of the same resolver; consistent with disposition 2. |
| P14 | `vault-rule-card.md:26` | *"(b) the nearest declaring ancestor container's `writers:` admits you, or none declares"* | **DOES NOT MOVE in wording** — re-derived and re-stamped only (R5). |
| S1 | `write-verification.md:47` — *lint attests narrowly … never attests a file it merely read* | per-consumer scope | **SURVIVES verbatim** (A7). |
| S2 | `write-verification.md:47` — *a skill added to `consumers:` for handshake reasons alone acquires no attestation authority* | roster ≠ grant | **SURVIVES verbatim** (A7; disposition 1). |
| S3 | `vault-operating-contract.md:68` — *"a specific partner slug is read from the attestation `verified_by:`"*; the `open` default; inheritance; `{wiki}` removed at population time | the resolver's remaining sentences | **SURVIVE unchanged** (only the *any* clause moves — R5). |
| S4 | `vlt-lint-full.js:868` (`attested`), `:914` (`ATTESTATION_FRONTMATTER`), `:1017` (the reader's refutation comment) | the wiki-side attestation reduce | **SURVIVE unchanged** — presence tests; only the four pin literals move (F8). |
| S5 | `vlt-upgrade/SKILL.md:124` | the v0.16.0 `governance_rule_changes` rendering naming `para_writer_unauthorized` | **SURVIVES** — a rendering of history. |
| S6 | `decision-log.md:93`-`:103` — *"Writers and readers (the roster the handshake protects)"* | a **different** roster (who appends the log) | **SURVIVES** — not the attestation roster; named so a grep for *roster* is not mistaken for a hit. |

**Population statements that must NOT move, in one sentence:** the `para_*` population (`checks.md:19`
and the walker), the attestation pair's *presence* requirement and its class exemption (`:55`,
`extraction.md:190`/`:192`, contract `:70`, the walker's `M`), and the `open` + PASS default with
sub-container inheritance (`checks.md:20`, contract `:68`'s surviving sentences) — the property check
(2) protects is that **`P` and `M` are identical before and after this build over any fixed tree**,
and that no shipped text still limits `verified_by:` to a list of operation skills.

**Deliberately NOT retired (D5.3, D5.5):** the attestation pair and `para_missing_attestation`; the
no-ancestor `open` + PASS default. **Retired that the beat named (A20), all present above:** `:47`'s
closure (R1), `:296(c)`'s write-op ceiling (R4); `checks.md:20`'s partner-slug leg made exercisable
(F2). **Reverse dependents left standing** — enumerated: P3, P12, S1–S6.

### 10. Grounding corrections at brief time — every cite re-derived against `fc44027`

1. **`vlt-research/SKILL.md:3`, not `:4`** — its `depends_on:` is the third line (no `name:`/`description:`
   ordering like the others). The ledger and F7 say `:3`. *(Roadmap note written.)*
2. **The workflow body pins are `:241`, `:245`, `:297`, `:911`** — the roundtable's A1 named `:178`,
   `:182`, `:229`, `:684` (pre-builds 2–4); the header is still `:11`. Same four sites, shifted. *(Roadmap
   note written; the count and the E7 obligation are unchanged.)*
3. **Contract `:68` MOVES** — A20 read it as *"already reads a partner slug — nothing to do"*; its
   *"admitted when **any** of its identities"* clause is the pre-D-E join and would contradict the
   changed `checks.md:20`. One clause; C6 engages. *(Roadmap note written.)*
4. **A8's key literal collides** with the per-file list at `report.md:50` — the line is `para_writer_scan:`
   (disposition 4). *(Roadmap note written.)*
5. **`report.md:50`, not `:39`** for `para_writer_unauthorized` — drift from build-5's fence insertions;
   the slot is unchanged. *(Roadmap note written.)*
6. **HOLD:** `write-verification.md:11` (`version: 5`), `:12` (`consumers:`), `:47` (the closure),
   `:55` (the Scope rule); `checks.md:20`; `checks.md:40`; `frontmatter.md:78`, `:82`, `:296`; the four
   `SKILL.md` pins other than research's; the field count **27** (the filing's, re-verified by the
   filing on 2026-09-01 — not re-counted here; the brief consumes it as a count). The field vault
   declares **0** `writers:` lists (brief-time read, counts only) — disposition 2 (c).
7. **Not a correction, recorded:** `PAGE_SCAN` measured **3265** at `fc44027` by package-lint's E6
   extractor (build-4's BUILT figure holds); the `@5 → @6` edits are length-neutral.

### Interim posture (R1) — discharged

Every rule this build ships arrives with its mechanism in the same commit: the restated value set with
the join at `checks.md:20`/contract `:68`; the denominated line with the walker facts and the gate's
string-equality compare; the handshake with Group E. The R1 **standing-rule** interim posture (the
`handshake:` line by A1) is honoured in disposition 5. Nothing ships ahead of its mechanism — **R1: not
applicable** beyond that.

## Boundaries — stated so the builder inherits them

- **Build-6 ↔ build-7 on `checks.md` and the shared `SKILL.md` pin lines.** Build-6 landed
  (`fc44027`): `checks.md:19` is its; **`checks.md:20` is this build's** and is re-grounded above.
  `vlt-lint/SKILL.md:4` and `vlt-extract/SKILL.md:4` already carry `extraction@10`; this build edits the
  **same lines** to move `write-verification@5 → @6` and touches no other pin on them.
- **Build-5 ↔ build-7 on `report.md` and the two scripts.** Build-5 shipped the fence grammar, the
  gate and the walker; this build **adds** one fence line, two walker facts + one count + one flag, and
  one gate comparison — it restates none of build-5's mechanics and re-derives build-5's schema fixture
  (`report.md` merge order 3 → 4 → 5 → 7 holds).
- **Build-4 ↔ build-7 on `vlt-lint-full.js`.** Build-4 owned the workflow's mechanics; this build's
  edits are the five pin literals **only** — no schema key, no prompt sentence beyond the version digit.
- **Build-2's key.** The `write-verification` digest and the prompt literal are key terms; this build
  moves both by design (cold, stated). `pin_vector` is gone — the bump itself moves nothing in the key.

## F-sites

*(Edit order: F1 → F4 → F2 → F3 → F5 → F6 → F7 → F8 → F9 → F10 (release). The convention first — it is
the home; then the contract and card; then the check; then the field definitions; then the instrument
and the gate; then the acks; then the fixture; then the release.)*

### F1 — `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md` — the home: `:11` bump, `:45`/`:47` restated

**Current state.** `:11` `version: 5`; `:12` `consumers: [vlt-ingest, vlt-extract, vlt-research,
vlt-lint, vlt-lint-full.js]`; `:4` `last_updated: 2026-08-27`. `:45` *"After tier-1 completes, write
`verified_by: <this op>` and `verified_at: <today>` on every artifact created or updated. Updates
re-attest …"*. `:47`, verbatim: *"**`verified_by` value set:** the `verified_by` value set is this
file's `consumers:` **that are write ops**, plus write-op `local_consumers:` registrants
(`frontmatter.md`, *Vault-writable declared fields*). The roster is **membership and ceiling**, never an
automatic grant: a skill added to `consumers:` for handshake reasons alone acquires no attestation
authority — the write-op qualifier binds the **whole** set. Per-consumer scope stays stated where it
applies: lint attests **narrowly** — it writes the pair only on files its own auto-fix touched (an
auto-fix bumps `last_updated` and would otherwise re-stale the attestation it just validated). Lint
never attests a file it merely read."*

**The exact change.**
- `:11` `version: 6`; `:4` `last_updated: 2026-09-02`. `:12` unchanged.
- `:45` — `<this op>` → `<this attester>`, and one sentence appended (A7, the non-op attester): *"**A
  partner attesting a knowledge artifact it wrote in a sitting** runs the same tier-1 checklist and
  writes its **own slug** — the attester is whoever ran the checklist, an op or a partner; there is no
  op to name on its behalf."*
- `:47` → *"**`verified_by` value set:** the `verified_by` value set is **whatever the nearest declaring
  container's `writers:` join admits; unconstrained where none declares** (`vlt-lint`'s
  `para_writer_unauthorized` — `checks.md`, the resolver's home is the operating contract, *The three
  layers and the hard write boundaries* — is the net that answers it, **once**; v6 retired the roster of
  write ops that answered it a second time and could not admit a partner). This file's `consumers:` is a
  handshake roster, not a grant: a skill added to `consumers:` for handshake reasons alone acquires no
  attestation authority. Per-consumer scope stays stated where it applies: lint attests **narrowly** — it
  writes the pair only on files its own auto-fix touched (an auto-fix bumps `last_updated` and would
  otherwise re-stale the attestation it just validated). Lint never attests a file it merely read."*
  — the two surviving clauses verbatim; the four retired phrases gone.

**Why.** A15-13 half 1; D5.3/D5.4; A7 (restated never deleted; the non-op attester). **Out of scope
here:** `:55`'s five-value enumeration (§Out of scope); `:22`'s *"every agent write operation"* framing —
a partner sitting's write is an agent write operation; no edit.

### F2 — `skills/vlt-lint/references/checks.md:20` — the one-line join change (D-E)

**Current state** (`:20`, the join clause): *"… and join the file's writer identities against that
list, admitting on **any** match: `author: human` → `human`, `author: agent` → `agent`, **`author:
hybrid` → `human`** (the hybrid rung is human ratification), and the attestation `verified_by:` → that
partner slug. A file resolving no identity at all is left to the honesty nets …"*

**The exact change** (that clause only; every other sentence of `:20` is P1 and byte-identical):
*"… and resolve the file's writer identities — `author: human` → `human`, `author: agent` → `agent`,
**`author: hybrid` → `human`** (the hybrid rung is human ratification), and the attestation
`verified_by:` → **that identity, by name** (an op or a partner — the value set is
`{conventions}/write-verification.md` §Attestation). **Where `verified_by:` is present, the attester is
the writer of record: the file passes iff the list admits that identity — `agent` admits every
agent-kind identity, a specific slug admits only itself — and the `author:` leg neither rescues nor
refuses it (never carried by the `author:` leg). Where no `verified_by:` is present, the `author:` leg is
judged alone.** A file resolving no identity at all is left to the honesty nets …"*

**Why.** Owner ruling D-E; disposition 2 (the join stated once at the contract, restated check-side
here as D-E ordered). **R3 (legal response):** unchanged — the existing sentence covers the new
refusals (ratify a `writers:` change / relocate / rule human-authored; never auto-fixed). **The
`para_writer_scan:` line's composition** is stated at `report.md` (F6), pointed at from here in one
clause: *"the denominated line `para_writer_scan:` (report.md) carries N / D / O from the walker."*

### F3 — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:78`, `:82`, `:296(c)` — prose re-nouns, NO bump

**Current state.** `:78` `verified_by: <the attesting op — value set in write-verification.md
§Attestation>`; `:82` *"**`verified_by`** — the operation that ran tier-1 on this file. The legal value
set is the attestation contract's, defined in `write-verification.md` §Attestation — not restated
here."*; `:296` clause (c): *"**(c)** the base roster is the **ceiling** of what registration can grant
— for attestation authority specifically, a registrant must be a **write op** (`write-verification.md`,
§Attestation — the contract around `verified_by` lives there, not here)."* `:4` `version: 14`.

**The exact change.** `:78` → `verified_by: <the attester — an op or a partner; value set in
write-verification.md §Attestation>`. `:82` → *"**`verified_by`** — the attester — an op, or a partner —
that ran tier-1 on this file. The legal value set is the attestation contract's, defined in
`write-verification.md` §Attestation — not restated here."* `:296(c)` → *"**(c)** registration grants a
**handshake seat** and nothing else: a registrant is walked by the coherence check exactly as a base
consumer is, and acquires no attestation authority by registering — whether an attester is admitted is
the attestation contract's question (`write-verification.md`, §Attestation — the contract around
`verified_by` lives there, not here), never this roster's."* **`version: 14` unchanged; `last_updated`
bumped; no consumer walked.**

**Why.** A7 (explicit: no `frontmatter` bump); disposition 3. **Grounding note:** `frontmatter.md:71`
(build-6's re-noun) is untouched.

### F4 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:68` + `vault-rule-card.md` (C6)

**Current state** (`:68`, the resolver): *"A writer is admitted when **any** of its identities is in
that list: `author: human` reads as `human`, `author: agent` as `agent`, and **`author: hybrid` reads as
`human`** (the hybrid rung *is* human ratification — the honesty rule); a specific partner slug is read
from the attestation `verified_by:`. A file resolving no identity at all (no `author:`, no
`verified_by:`) is judged by the honesty nets, not by this resolver."* Card `:26` (b): *"the nearest
declaring ancestor container's `writers:` admits you, or none declares"*; `derived_from: … sha256:`
re-stamped by build-6.

**The exact change** (`:68`, that clause only): *"A writer's identities are: `author: human` reads as
`human`, `author: agent` as `agent`, **`author: hybrid` reads as `human`** (the hybrid rung *is* human
ratification — the honesty rule); and the attestation `verified_by:` names a **specific identity** — an
op or a partner. **Where the file carries `verified_by:`, that attester is the writer of record and
must itself be admitted** (`agent` in the list admits every agent-kind identity; a specific slug only
itself; the `author:` leg neither rescues nor refuses it); **where it carries none, the `author:` leg
is judged.** A file resolving no identity at all …"* — the rest of `:68` (the `open` default, inheritance,
`{wiki}` removed at population time, `writers:` human-gated) byte-identical. Then **re-derive
`vault-rule-card.md`** from the edited contract: `:26`'s wording stands; re-stamp `derived_from: …
sha256:<shasum -a 256 of the edited contract> (derived 2026-09-02)`; card stays under
`RULE_CARD_BUDGET` (7,295 bytes at `fc44027`; no card text grows).

**Why.** Grounding correction 3 (R5); disposition 2. **Not handshaked** (single-home + pointers) —
C6 is the gate.

### F5 — `skills/vlt-lint/scripts/lint-para-facts.py` — two facts, one count, one flag (D2 (iv))

**Current state.** `FACT_KEYS` (`:68`) carries scalars incl. `verified_by`/`verified_at`; `walk()`
(`:131`) returns `{instrument, population, files, missing_attestation, counts: {P, M}}`; `--line`
(`:184`) prints the `para_scan:` value (`:174`). Charter files are population members (their `writers:`
is a YAML list — block or flow form — which the scalar reader does not capture).

**The exact change.** (a) Read `writers` on any file that carries it as a **list** (flow `[a, b]` or
block `- a` lines directly under the key — `frontmatter.md` YAML rule 3/4 idiom; the reader is the
sibling `frontmatter_lines` import, extended by one list-shaped case, never a YAML library), emitted as
`writers: [..]` or `null`. (b) Per file, `declaring_ancestor`: walk **up** from the file's directory to
the `--dir` root it was found under; the first directory holding a `charter.md` whose `writers` list is
non-empty is the declaring ancestor — its `charter.md` walk-relative path, else `null` (`checks.md:20`:
nearest declaring ancestor; a declaring ancestor binds every sub-container). A charter's own declaring
ancestor is itself where it declares. (c) `counts.D` = files whose `declaring_ancestor` is non-null.
(d) `--writer-line` prints exactly: `<P> judged; <D> under a declaring ancestor; <P−D> passed on open
posture (instrument: scripts/lint-para-facts.py)`. (e) Docstring: the two facts named as facts (*whether
the writer is admitted is the SKILL's judgment against checks.md*), `--writer-line` documented beside
`--line`. Exit codes unchanged.

**Why.** Disposition 4; D2 (iv) — `D` and `O` come from the walker, not the agent that judges the net.
**Out of scope:** admission itself (a verdict) — never computed here.

### F6 — `skills/vlt-lint/references/report.md` (`:46`-`:50`, §Persist-gate reporting) + `skills/vlt-lint/scripts/lint-report-check.py` + `fixtures/build-5-expected-schema.json` + `build-5-shape-harness.py`

**Current state.** Fence `:46` `para_scan:` scalar; `:50` `para_writer_unauthorized:` list; `:107`
§Persist-gate reporting names the `para_scan:` string-equality compare; the gate's `SCAN_KEY =
"para_scan"` (`:89`) and the compare at `:291`; `SCHEMA_FLOOR = 18` (`:81`); the build-5 harness
deep-equals the fence parse against `build-5-expected-schema.json` (18 top-level keys, 73 key paths).

**The exact change.** (a) One fence line inserted **directly above `:50`**:
`  para_writer_scan: <N judged; D under a declaring ancestor; O passed on open posture (instrument: scripts/lint-para-facts.py)>   # the write-posture net's denominator — N, D, O from the walker's --writer-line verbatim, both modes, never omitted; the open-posture PASS population made visible (D5.5); Step 6 re-walks and compares this string`.
(b) §Persist-gate reporting gains one clause: *"… and the `para_writer_scan:` scalar equal — by string
equality — to the walker's `--writer-line` for the same directories"*. (c) A one-line paragraph after
§Governance-memory reporting (or folded into the `para_scan:` sentence of §Persist-gate): *"**Write-posture
reporting.** `para_writer_scan:` is pasted from `scripts/lint-para-facts.py --writer-line` verbatim, in
both modes; the list beneath it names the refusals, the line says how many files were judged and how
many passed only because no ancestor declares."* (d) Gate: a second compare — `WRITER_SCAN_KEY =
"para_writer_scan"` against the walker's writer line, reason `para_writer_scan: rendered line does not
match the walk`; the walker import already exists (`load_walker`, `:306`). (e) **Re-derive
`fixtures/build-5-expected-schema.json`** with `lint-report-check.py schema` (18 top-level, **74** key
paths, 5 per-file, 1 full-mode-only) and add harness rows: (7a) the shipped fence deep-equals the
re-derived oracle; (7b) a report whose `para_writer_scan:` is absent → fails presence; (7c) present but
`O` off by one → fails the string compare; (7d) equal to the walker's line → passes. `SCHEMA_FLOOR`
**stays 18**.

**Why.** A8; disposition 4; the merge order 3 → 4 → 5 → 7 on `report.md`. **R3:** the line is a
denominator, not a finding — no legal response owed beyond §Persist-gate's shape-failure response, which
already covers a mismatched scalar (re-render once from the same facts).

### F7 — the four SKILL acks: `skills/vlt-ingest/SKILL.md:4`, `skills/vlt-extract/SKILL.md:4`, `skills/vlt-research/SKILL.md:3`, `skills/vlt-lint/SKILL.md:4`

**Current state.** Each carries `"write-verification@5"` in its `depends_on:` (research's on line 3).
**The exact change.** `write-verification@5` → `write-verification@6` on each of those four lines; no
other pin on the line moves (`extraction@10`, `frontmatter@14`, … untouched). **Why.** A1; R1; the
consumer walk of a rule change (CLAUDE.md). Also `skills/vlt-lint/SKILL.md` Step 1 (`:47`) gains
`--writer-line` beside `--line` in its walker invocation sentence (F5's flag reaches Step 5 through it).

### F8 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js:11`, `:241`, `:245`, `:297`, `:911` — the asset ack and its four body pins

**Current state.** `:11` `// depends_on: ["frontmatter@14", "wiki-supersession@2", "wiki-index@2",
"write-verification@5"]`; `:241` *"… per write-verification@5"*; `:245` *"… (per write-verification@5
Scope rule)"*; `:297` *"… (per write-verification@5, the wiki-page tier-1 item: …)"*; `:911` *"//
Attestation is a self-marker under write-verification@5's Scope rule …"*.
**The exact change.** `@5` → `@6` at all five; nothing else in the file. **Why.** A1 (E5 + E7);
disposition 5 — `PAGE_SCAN` 3265 → 3265; `scanFingerprint` moves (the `:297` literal is a `canonicalScan`
input) — recorded in the BUILT status as build-4 recorded its own.

### F9 — `factory/cycles/15-nothing-reads-it-back/fixtures/build-7-para/` + `build-7-expected-findings.json` + `build-7-reader-protocol.md`

**The exact change.** A PARA tree (placeholder names, no personal content) with: **C1**
`projects/alpha/` — `charter.md` (`type: charter`, `author: hybrid`, `writers: [human, librarian]`) +
`draft.md` (`author: hybrid`, `verified_by: librarian`) → pass; `note.md` (`author: agent`, `verified_by:
banana`) → **fail** (`banana` not admitted; `agent` not in the list); `agent-note.md` (`author: agent`,
`verified_by: librarian`) → pass; `sub/deep.md` (no charter in `sub/`; `author: agent`, `verified_by:
researcher`) → **fail** by inheritance; `human.md` (`author: human`, no pair) → pass; `unattested.md`
(`author: agent`, no pair) → not this net (→ `para_missing_attestation`); the charter itself (hybrid →
human) → pass. **C2** `areas/beta/` — `charter.md` with `writers: [human, agent]` + `any.md` (`author:
agent`, `verified_by: banana`) → **pass** (declared `agent`; disposition 2's residual, on record);
`hybrid-op.md` (`author: hybrid`, `verified_by: vlt-extract`) → pass. **C3** `areas/gamma/` —
`charter.md` with `writers: [human]` + `ratified.md` (`author: hybrid`, `verified_by: librarian`) →
**fail** (D-E's case: the author leg does not carry it); `plain.md` (`author: human`) → pass. **C4**
`resources/delta/` — no charter → every file passes `open`, counted in `O`; `resources/wiki/page.md`
excluded by name. The oracle `build-7-expected-findings.json` (hand-written **first**): per-file verdict
+ the walker's expected facts (`declaring_ancestor`, `writers`), `counts: {P, M, D}`, the exact
`--writer-line` string, and a `pre_build` block giving the table under `fc44027`'s any-match join
(`note.md` passes there via `agent`? — no: `[human, librarian]` names neither `agent` nor `banana`, so
it fails under both; `ratified.md` **passes** under the old join via hybrid → human and **fails** under
the new; `any.md` passes under both; `hybrid-op.md` passes under both) — at least one row differs, which
is the failability leg. The reader protocol names its inputs (the fixture, `checks.md:20`, the contract
`:68`), its output (the per-file table), and the two runs (shipped text; `fc44027` text via `git show`).
A one-paragraph README states specimens `0/27` and why (disposition 8). **R4:** declared exclusion —
`fixtures/` is enumerated by no shipped vital or manifest (build-6's precedent).

### F10 — the release build: `.claude-plugin/marketplace.json` `"version"` + `skills/vlt-setup/assets/module.yaml` `module_version` → `0.18.0`

See §Release. The bump is this build's last edit, after F1–F9 verify at `0.17.1`.

## Registration

**None** in the help/version surface — no new skill, no new workflow, no CSV row. **The convention
walk is the registration:** `write-verification` 5 → 6 with the five re-acks in F7/F8 (four SKILL pins
+ the asset header **and** its four body pins). Priced beyond the handshake (brief-anatomy §5):
**C6 engaged** (F4 — card re-derived, hash re-stamped, under budget); **E4 not engaged** (no new
package-lint check); **E5/E7 engaged** (F8); **E6** measured, unchanged at 3265; **`module.yaml`**'s
scripts rows unchanged (both scripts already listed by build-5). `frontmatter@14` **not bumped** (A7).

## Out of scope (dispositioned)

- **A floor on unrostered attesters** — rejected (Q5); no enumeration is added anywhere.
- **`write-verification.md:55`'s five-value `type:` enumeration** (`wiki|research|project|area|resource`)
  — a sibling completeness-claiming list (build-6 §9 P16); not this filing's ask, not a supersession —
  **noted for `factory/inbox/` at handoff** as a `candidate` (the jurisdiction test could read *the
  recognized set minus the operational-record class* by pointer).
- **`para_author_unknown`'s closed `human|agent|hybrid`** — released at the roundtable (Cycle 14 carry
  6); the next `supersession` candidate, the owner's to file through the rail.
- **`extraction.md:157`/`:168` *"a specific partner slug"*** — read as *a specific slug*; no edit, no
  `extraction` bump (disposition 2).
- **Re-attesting the 27 files** — the partners' act after upgrade; capability, not backlog (the bullet's
  rejected over-claim). Check (5) observes one such act; none is scheduled by this build.
- **`vlt-lint` auto-fix honouring `writers:`** — the edge in disposition 2 (b); the `para_*` nets are never
  auto-fixed, and a wiki-side fix cannot land in PARA; no mechanism.
- **A partner-side attestation *instruction* in `vlt-agent-*` / `vlt-dispatch` / `vlt-mint`** — A7 found
  none exists; the one sentence at F1 `:45` is the convention's own statement, which every partner reads
  point-of-use (the contract's read rule). Adding a beat to partner templates is a `candidate` for the
  inbox, not this build.
- **The tracker re-kind of #18** — the owner's act (A9), after build-1 and before the tag.
- **`decision-log.md`'s writer roster** — a different roster (S6); untouched.

## Verification (unit, at rest — lifecycle step 5)

1. **Handshake bipartite re-check — `package-lint` Group E is the check of record** (never a hand grep):
   `uv run tools/package-lint.py` mid-cycle → A/B/C/E PASS; E1 sees `write-verification@6` on all five
   listed consumers (four SKILLs + the asset header via E5), E3 no stray pin, **E7 clean** (all four body
   pins at `@6`), E6 unchanged. Then `tools/handshake-check.py` (if present) → *9 conventions, 39 consumer
   pins — bipartite-consistent*. A grep is an editing aid only.
2. **Grep manifest (check (2)'s instrument), 0 hits across `skills/` incl. the rule card:** `that are write
   ops`, `write-op `local_consumers:``, `write-op registrants`, `membership and ceiling`, `write-op
   qualifier`, `the attesting op`, `must be a \*\*write op\*\*`, `any of its identities`, `any match`,
   `admitting on \*\*any\*\*` — plus the semantic variants `an op listed in `consumers:``, `rostered
   attester`, `write ops only`. And **presence** greps: `lint attests \*\*narrowly\*\*` → 1
   (`write-verification.md`); `handshake reasons alone acquires no attestation authority` → 1;
   `writer of record` → 2 (`checks.md:20`, contract `:68`); `para_writer_scan` → 4 files (`report.md`,
   `lint-report-check.py`, `lint-para-facts.py`, `vlt-lint/SKILL.md`).
3. **Byte-identity over the must-not-move sites** (`git diff -U0 fc44027`): `checks.md` hunk at `:20`
   only, and inside `:20` the word-diff begins at *"and resolve the file's writer identities"* and ends
   before *"A file resolving no identity"*; `write-verification.md` hunks `:4`/`:11`/`:45`/`:47` only
   (`:55` intact); `frontmatter.md` hunks `:4`(last_updated)/`:78`/`:82`/`:296` only (`:71`, `:294`
   intact); contract hunk `:68` only, and inside it only the identities/admission clause; `extraction.md`
   **no hunk**; `report.md` the inserted line + the two paragraph clauses only.
4. **C6:** `shasum -a 256` of the edited contract equals the card's re-stamped `sha256:`; card bytes <
   8,000; package-lint C PASS.
5. **E6 by package-lint's extractor:** `PAGE_SCAN` = 3265 (≤ 3700); `INDEX_SCAN`/`CLUSTER_FINDINGS`/
   `PAIR_FINDINGS` byte-identical. **`scanFingerprint` recorded before/after** (from the shim
   `fixtures/vlt-lint-full-shim.mjs`): it moves; `convention_digests[write-verification]`
   (`2590f56e…` at `fc44027`) moves; `convention_digests[frontmatter]` moves again from build-6's
   `fca83321…` — all three values recorded in the BUILT status.
6. **The walker over `fixtures/build-7-para/`** under `uv run` and bare `python3` (byte-identical output):
   per-file `declaring_ancestor`/`writers` and `counts: {P, M, D}` deep-equal the oracle; `--writer-line`
   equals the oracle's string; `--line` unchanged in form. Edge runs in scratch: a charter with
   `writers:` in flow form and in block form; an empty `writers: []` (not declaring); a charter with no
   `writers:` beneath a declaring parent (inherits — the parent is the ancestor); a file at the `--dir`
   root with no charter anywhere (`null`).
7. **The gate:** `lint-report-check.py schema` deep-equals the re-derived `build-5-expected-schema.json`
   (18 / 74 / 5 / 1); the build-5 harness green with rows 7a–7d added (`CASE`-style floor bumped as that
   harness does); the red leg: `fc44027`'s `report.md` fed through `--schema` → the new key absent → a
   report carrying `para_writer_scan:` is reported extra there, and the shipped fence refuses one
   without it.
8. **The reader protocol (check (3)):** oracle written first; the protocol over the fixture against the
   shipped `checks.md:20` + contract `:68` deep-equals the oracle's `shipped` table; against `fc44027`'s
   text deep-equals the `pre_build` table; the two tables differ on `ratified.md` at minimum.
9. **Prior harnesses green:** build-2 key harness (incl. the `scanModel` guard), build-3 type harness,
   build-4 return harness, build-5 shape harness, build-6 reader protocol (unaffected — `checks.md:19`
   untouched).
10. **Scrub:** no machine paths / personal content in any changed shipped file or fixture (a grep over
    `skills/` and `fixtures/build-7*` for machine home paths, the owner's username and the field vault's
    real name — the patterns live in `CLAUDE.local.md`, never here → 0);
    no `.decision-log.md`, no `__pycache__`.
11. **R3:** `checks.md:20`'s legal response unchanged and sufficient; the new line is a denominator (F6).
    **R4:** not applicable — declared exclusion (fixtures un-enumerated; the walker's new keys are
    additive facts inside an existing output object, not a new file class).

## Release (v0.18.0 — this is the release build)

- Both version strings → `0.18.0`: `.claude-plugin/marketplace.json` `"version"` and
  `skills/vlt-setup/assets/module.yaml` `module_version` (F10), **after** F1–F9 verify at `0.17.1`.
- `uv run tools/package-lint.py --expect-version 0.18.0` → **tag only on exit 0**; the PASS summary line
  goes in the release commit message.
- One commit for this build on `cycle15-v0.18.0`; then `vlt-release` choreography — ff-merge to `main`,
  tag `v0.18.0`, push main + tag (the owner's go).
- **CHANGELOG obligations (release-time, not written now — the release step copies these):**
  1. **`governance_rule_changes` block, `{conventions}/write-verification.md` v5 → v6:** *"**The
     `verified_by` roster closure is RETIRED.** `verified_by:` is no longer limited to a roster of
     write-op skills; its value set is **whatever the nearest declaring container's `writers:` join
     admits — unconstrained where none declares** — and `vlt-lint`'s `para_writer_unauthorized` answers
     the authorization question **once**: where a file carries `verified_by:`, that attester is the
     writer of record and must itself be admitted (`agent` admits every agent-kind identity; a named
     slug only itself; the `author:` leg no longer carries it); undeclared containers still pass `open`
     and are now **counted** on the new `para_writer_scan:` report line. **What a partner may now do
     differently:** attest a Layer-3 knowledge artifact it wrote in a sitting with its **own slug** —
     the tier-1 pass it already runs can finally be recorded. The attestation pair stays **required**;
     `para_missing_attestation` keeps its job. A container declaring only `[human]` now refuses every
     attested file (no partner drafts there) — ratify a `writers:` line to admit one. Five consumer
     acknowledgments re-pinned (`write-verification@6` × 5 — four skills and the lint workflow's header
     plus four in-prose pins); `frontmatter.md` stays at v14 (prose re-nouns at the field definitions
     and at `local_consumers:` (c), which now grants a handshake seat and nothing about attestation);
     the operating contract's resolver sentence moves one clause and the rule card is re-derived."*
  2. **Field notice:** *"A vault carrying `local_consumers:` registrants on `write-verification` (a
     vault-minted write op acking `@5`) will see **one expected `convention_drift`** finding per
     registrant on its next lint until the registrant is reconciled by ceremony (`vlt-mint`, convention
     edit) — the module cannot re-ack a vault-minted op. This is expected and is not a module defect."*
  3. **Cold-run statement (build-2 §Release), naming three movers:** *"The first full lint after this
     release is COLD BY CONSTRUCTION — build 4 moved the scan surface (prompt + schema), build 6 moved
     `frontmatter.md`'s bytes, and build 7 moved `write-verification.md`'s bytes and the scan prompt's
     version literal; every existing sidecar record is unreusable and `lint_cache:` will honestly report
     `cached 0` and name the moved terms. Expected; not a cache regression."* — beside build-6's
     `governance_rule_changes` text (build-6 §Release-time obligation) and build-2's block.
  4. **`parked_interims_review:` renders park #16 on the first v0.18.0 upgrade** — the unwind is the
     owner's superseding decision-log entry citing v0.18.0 (check (5)).
- Owed outside the build, before the tag: the owner re-kinds #17/#18 (A9; build-1 check (3)).

## Acceptance (live — appended to the roadmap ledger)

**Five checks — four `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 0/27`
(observed: the filing's 27 partner-written unattested Layer-3 files across six partner domains,
re-verified by the filing 2026-09-01 as *count unchanged*; preserved to this brief: **none** — the
filing preserved counts only, no path or fragment, and the observed state is the one this build makes
escapable rather than one its net judges; the fixture is authored from the failure's **shape** as the
filing states it and says so — disposition 8. The shortfall is named, not synthesized away.) **Q9: no
gating Cycle 14 clause rides here** (A18, D-D — build-6 carries (a)+(c); (b) is satisfied in substance).

**(1) `[ship-verifiable]` — at the release gate and at rest — GATES:** the `write-verification` 5 → 6
handshake is bipartite-consistent across both edit surfaces — instrument: `package-lint` Group E (E1
over `write-verification@6` × 5 consumers, E5 the asset header `:11`, **E7 the four body pins**
`:241`/`:245`/`:297`/`:911`, E3 no stray pin, E6 `PAGE_SCAN` ≤ 3700 at 3265), C6 with the rule card
re-stamped against the edited contract and under budget, mid-cycle A/B/C/E PASS and the
`--expect-version 0.18.0` PASS line in the release commit; *property:* every consumer
`write-verification.md:12` lists acks v6 in every place it recites the version, and nothing acks a
version it does not carry; *adversary:* an in-prose `write-verification v5`/`@5`/`v5 Scope rule`
citation inside a **skill body or reference** (E7 covers workflow assets only) — **widened:**
verification 2 adds a grep over `skills/` for `write-verification@5`, `write-verification v5`,
`write-verification.md v5` → 0 outside `CHANGELOG.md` history.

**(2) `[ship-verifiable]` — at rest — GATES:** the retirement landed whole and touched nothing it must
not — instrument: verification 2's grep manifest (0 hits for the ten retired phrases + three semantic
variants across `skills/`, the rule card included; the presence greps at their counts) and
verification 3's byte-identity diff over the must-not-move sites (`checks.md:19`, `:20` outside the join
clause, `write-verification.md:55`, `extraction.md` whole, `frontmatter.md:71`/`:294`, contract `:68`
outside the identities clause, `:70`, `report.md:42`/`:46`/`:50`, the walker's `M` predicate);
*property:* no shipped text limits `verified_by:` to a list of operation skills, the two surviving
clauses are present verbatim, and **`P` and `M` are identical before and after over any fixed tree**
(the walker at `fc44027` and at the build's commit over `fixtures/build-7-para/` and
`fixtures/build-5-para/` agree on `P`/`M`); *adversary:* the closure survives paraphrased (*"an op
listed in `consumers:`"*), or the `:82` pointer is rewritten to restate a set, or the card is
restamped with the old join summarized in it (C6 passes on the hash) — **widened:** semantic variants
in the manifest, the card in the grep, and a recorded reader pass over each edited paragraph naming
any surviving noun of *roster* or *op-only*.

**(3) `[ship-verifiable]` — at rest — GATES:** the join is D-E's — the attester is judged by name,
never carried by the `author:` leg, `agent` admits any attester, undeclared passes — instrument: the
agent-run reader protocol (`fixtures/build-7-reader-protocol.md`, named as the instrument) over
`fixtures/build-7-para/` against the hand-written oracle `build-7-expected-findings.json` (oracle first):
`draft.md`, `agent-note.md`, `human.md`, the charters, `any.md`, `hybrid-op.md`, `plain.md`, every
`delta/` file → **no** `para_writer_unauthorized`; `note.md`, `sub/deep.md` (inherited), `ratified.md` →
**fire**; `unattested.md` → not this net; the `{wiki}` page in no list; the protocol against `fc44027`'s
`checks.md:20` + contract `:68` yields the oracle's `pre_build` table, differing on `ratified.md`
(failability); *property* (the instrument beat's, reconciled — same): *a Layer-3 file whose
`verified_by:` names an identity the nearest declaring `writers:` admits raises no authorization finding
whatever kind of actor it is; one naming an identity that list refuses fails regardless of what
`author:` resolves to; with no declaring ancestor it passes and is counted; the pair remains required;
the handshake is bipartite-consistent* — clause by clause: `agent-note.md`/`draft.md`/`hybrid-op.md`
(any kind of actor), `ratified.md`/`note.md` (refused regardless of `author:`), `delta/` + the `O`
count (passes and is counted), `unattested.md` (pair required — `M` = 1), check (1) (handshake);
*adversary:* a reader applying the old any-match join from memory passes most rows — **widened:** the
failability leg requires the `pre_build` table from the pre-build text, and the oracle carries
`ratified.md`, which no any-match reading refuses.

**(4) `[ship-verifiable]` — at rest — GATES:** the denominated line is produced by the walker and
read back by the gate — instrument: verification 6 (walker facts + `counts.D` + `--writer-line`
deep-equal the oracle under `uv run` and `python3`) and verification 7 (`lint-report-check.py schema`
deep-equals the re-derived `build-5-expected-schema.json` at 18 / 74 / 5 / 1 with `SCHEMA_FLOOR` 18; the
build-5 harness green with rows 7a–7d: absent → presence fail; `O` off by one → `para_writer_scan:
rendered line does not match the walk`; equal → pass); *property:* `N`, `D`, `O` on a persisted report
come from an instrument other than the agent that judged the net, and a hand-composed line cannot land;
*adversary:* the line is rendered from the walker's **old** `--line` numbers with `D`/`O` invented so the
string happens to match a stale walk — **widened:** the gate re-walks the same `--dir`s at persist time
(build-5's ritual) so the comparison is against the live tree, and row 7c mutates `O` alone.

**(5) `[field-contingent]` — the partner-attestation half and the park's unwind:** event: the **first
`vlt-upgrade` to v0.18.0 on `{field-vault}`** renders the v0.18.0 `governance_rule_changes` block, the
`local_consumers:` field notice's one `convention_drift` (the registrant acks `@5`), and
`parked_interims_review:` with park **#16**; then, in a **partner sitting** (owner-run), the partner
re-attests **one** of the 27 files with its **own slug** and a **scoped `vlt-lint`** over that file
reports it in neither `para_missing_attestation` nor `para_writer_unauthorized` (undeclared → `open`,
counted in `para_writer_scan:`'s `O`), the line present and equal to the walker's; then the owner
writes the **superseding decision-log entry citing v0.18.0** through the rostered route (not a third
park). Performer: the owner (+ the partner in session); vault `{field-vault}` (readable from the factory
machine — counts and the log heading recorded, never paths). Grades: the entry exists and cites
v0.18.0, park #16 is no longer live, the re-attested file carries a partner slug and raises no finding,
the `convention_drift` count is exactly the registrant count. **Discharges `2026-09-01-170000`
(A15-13)** — Stage 5 may move it once (1)–(5) are green; tracker **#18** closes on the rail sync.
Unbounded; watch register if unfired — *a re-park is not an unwind* transfers. **Not graded:** the 27
dropping to zero (the promise is capability).
