---
title: 'Build #4 — the scanner''s returns: after this ships, a vault owner stops being sent to fix pages that are not broken — no orphan that has an inbound link, no missing target that exists, no over-length summary that is inside the limit'
status: >
  BUILT 2026-09-02 — all eight F-sites landed; **checks (1), (2), (3) and (4) — the four at-rest
  `[ship-verifiable]` checks — PASS at rest** (17/17 expectations on the shipped workflow), the
  return harness proven failable against the pre-build workflow (`7222cd2`: **12 expectations
  FAIL there**, with exactly the controls passing — (d), (e), the single entity-pair dispatch and
  the cache-reuse half of (g) — 0 fail here). **Check (5), Cycle 14 build-1 (6) leg 3 — the
  at-rest leg (check (2)) is GREEN:** `frontmatter_drift` is computed from `summaryLengths` alone
  (159 / 160 / 162 / 0 from the script), the planted 162-char paraphrase for `l-theanine` and
  the at-the-cap `barbacoa` produce NOTHING, and the prompt carries the length-exclusion sentence
  once, outside every schema literal. **Recorded, not asserted (the instrument's stated bound):
  the planted `frontmatter_defect: 'unclassified'` length complaint for `l-theanine` STILL
  REACHES `malformed_frontmatter` at rest** — the reduce cannot refuse prose (D1) and the prompt
  sentence is the only elimination for that key; **leg 3 itself stays OPEN for the first
  `vlt-lint --full` sweep after v0.18.0 (GATES closeout)**, where 0 refuted ⇒ Cycle 14 carry 5
  is answered (D-F). Version bump NOT taken — rides build-7 / v0.18.0. Branch `cycle15-v0.18.0`.
  No handshake moved (`// depends_on:` header `:11`, every `write-verification@5` literal and
  the `vlt-lint/SKILL.md` pins untouched — `git diff 7222cd2` shows 0 changed lines carrying
  `write-verification@`; the new `per frontmatter@14` marker is the current pin, package-lint
  E7 passes). **Verification 1:** `lint-page-facts.py` over `fixtures/build-4-wiki/` deep-equals
  the hand-written oracle — diff EMPTY (via `uv run`; the harness falls back to `python3`).
  **Verification 2 — `scanFingerprint` MOVED, by design:** `dcce0c50239720081cb5` (at
  `7222cd2`) → **`c44d8912ed750afe1cdf`** (the `outbound_links` removal + the two prompt
  sentences; the one build besides build-7 that moves the scan surface). **Verification 3 — E6
  by package-lint's own extractor: `PAGE_SCAN` 3676 → 3265** (≤ 3700; required-only would have
  read 3659), `INDEX_SCAN` 838 / `CLUSTER_FINDINGS` 1630 / `PAIR_FINDINGS` 376 byte-identical;
  `uv run tools/package-lint.py --expect-version 0.17.1` → A/B/C/E PASS, D PASS. **Verification
  4–5 (greps):** `outbound_links|partialShortfall|not computed — inbound-derived` in the workflow
  → 0; `outbound_links` anywhere under `skills/` → 0; `the page's own bytes do not carry` under
  `skills/` → 0; `links(` consumers in the workflow → 7 (inbound, orphans is over `pages`,
  missing targets, linkSets, clusters ×3 incl. the adjacency test, the seed read-back — ≥ 6);
  `LENGTH is never a frontmatter defect` → 1, inside `pageScanPrompt`. **Verification 7:**
  `build-2-key-harness.mjs` all expectations hold (incl. the scanModel guard), `build-3-type-harness.mjs`
  31 PASS across default / `--stubs` / `--tail`; `grep -l vlt-lint-full-shim fixtures/*.mjs` → 3.
  **Verification 8:** `full-scale.md` step 1 names the script and both maps, step 3's args
  list carries both, `checks.md:13` carries the pointer, `report.md` carries
  `scanner_return_rejected:` at `:16` (key) and `:91` (§Findings-cache reporting), the workflow's
  arg contract / guard / refusal `next:` all name both slots. R3 satisfied at the single homes; R4
  not applicable (declared exclusion — `scripts/` is walked whole by `verify-skill-manifest.py:14`).
  Scrub: no machine paths or personal content in any new file (grep over the fixture wiki,
  harness, shim, script, references → 0). No `.decision-log.md` in the tree; scratch removed.
  The script's edge cases were exercised in scratch beyond the fixture: BOM, a `>` block scalar
  (31), `\"`/`\\` escapes (18), a plain scalar with a trailing `# comment` (11), `~~~` and
  nested four-backtick fences, a double-backtick span enclosing a single-backtick one, a lone
  unclosed backtick (literal — its link kept), the embed `!` outside the brackets, an undecodable
  file and a missing file both listed `unreadable`, exit 2 on a bad `--pages` (missing file / a
  non-object entry), exit 3 on an unwritable `--out`.

  **Sites changed.**
  `skills/vlt-lint/scripts/lint-page-facts.py` (F6, NEW — 220 lines, `# /// script` with
  `requires-python` only): the disposition-1 contract verbatim in its docstring; `--pages
  <path|->`, `--out <path>`; `strip_code` (fences + spans), `page_links` (the raw `[[…]]`
  regex over frontmatter and body alike), `frontmatter_lines` / `summary_value` (double- /
  single-quoted / plain / block-scalar forms) / `summary_length` (Python `len()`); `unreadable`.
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (F1): `:6-7` the phase details (see
  deviation 1); `:26-32` the header's no-filesystem paragraph gains the byte-fact sentence and the
  `pages` row names the guard's five; `:57-69` the `pageLinks` / `summaryLengths` contract rows
  (REQUIRED, refusal/cap posture, NOT a cache-key term — D4); `:148-150` the intake comment names
  the two slots as refused on this build's own ruling, the four legacy args' sentence intact;
  `:156-171` intake — map-level and per-slug wrong-type facts into `wrongTypeSlots` by name
  (`pageLinks[<slug>]` / `summaryLengths[<slug>]`); `:187-188` the args guard names all five and
  the script; `:225` `PAGE_SCAN.required` loses `outbound_links` and the property is gone —
  **no other character of the schema changed** (E6 per-schema lengths prove it); `:298` the
  verbatim clause re-nouned to the callout target + "Do NOT report the page's outbound links";
  `:299` the length-exclusion sentence appended to the frontmatter-verdict sentence (`per
  frontmatter@14`); `:496` the refusal's `next:` maps the two new slot roots and points at step 1
  / the script (build-3's `step 2` / `Missing targets` text kept — its harness asserts it);
  `:581` `recordOf(p)` factored from the two identical corpus/cache lookups; `:590-612`
  `linksOf` (over `pages`, normalized + set here) + `links(slug)` + the two denominated K-of-T
  caps (`pageLinks:` / `summaryLengths:`); `:614-641` the callout read-back — `scannerRejected`
  (slug → reason), `calloutsOf` (the seeds that passed), one cap only when N > 0; `:646-670`
  `cacheRecords` skips a rejected slug, the `:575-576` NORMAL FORM comment retired; `:672-699`
  the link graph — inbound over `pages` × `links` with self-links excluded, `orphans` over
  `pages`, `missing_targets` over `pages` × `links`, `partialShortfall` + its cap + the DA7
  comment block DELETED, the `:588` "stay scans-denominated (DA7)" clause replaced; `:711`
  `linkSets` from `links(s.slug)`; `:731` the near-dup loop guard loses `!partialShortfall`
  and its comment; `:765-768` cluster adjacency from `links(...)`; `:818-827` the seed loop
  iterates `calloutsOf`; `:863-871` `summaryIssue(slug)` from `summaryLengths` (0 → `summary
  missing`, > 160 → `over-length (N chars)`), called with `s.slug` at `:999-1000`; `:1091-1094`
  the return gains `scanner_return_rejected: {count, of, slugs}` beside `entity_scan_facts`.
  File grew 1021 → 1118 lines — **build-7 re-grounds every line number after this commit.**
  `skills/vlt-lint/references/report.md` (F2): `:16` the new `scanner_return_rejected:` scalar
  after `stub_discovery:` (full via the workflow; scoped/inline `not instrumented (inline run)`);
  `:91` §Findings-cache reporting's one sentence (never folded into `rejected R of P`). `:76`
  cap examples deliberately NOT widened. **Merge order on `report.md` is now 3 → 4 → 5.**
  `skills/vlt-lint/references/full-scale.md` (F3): step 1 (`:7`) the script sentence, instrument
  named by path; step 3 (`:9`) the args object gains both, "~84KB plus the two page-facts maps",
  the executable sentence points at step 1's script for the two facts and keeps the recipe for
  the rest, the resume list gains both, "over the SKILL-derived link sets", the follow-on
  sentence re-pointed per disposition 9 (`:18`); step 4 (`:10`, deviation 2); step 5 (`:21`) the
  refused-finding example re-worded + the `scanner_return_rejected` nothing-to-evict sentence.
  `skills/vlt-lint/references/checks.md` (F4): `:13` the executable-form pointer after the
  population statement (population untouched); `:14` the `summary:` clause's parenthetical;
  `:25` the orphan parenthetical (rule untouched). `:15` untouched.
  `skills/vlt-lint/references/fix-and-file.md:16` (F5): the second example re-worded.
  `factory/cycles/15-nothing-reads-it-back/fixtures/vlt-lint-full-shim.mjs` (F7, NEW): the
  shared runtime shim (compile / counting `run` returning `{result, logs, invocations, labels}`,
  `scanStubFrom`, `readSrc`); `build-2-key-harness.mjs` + `build-3-type-harness.mjs` import it
  and compose `pageLinks` / `summaryLengths` from the sidecar records (equal to what the scanner
  returned — every prior expectation unchanged); build-3's `--stubs` passes links as `pageLinks`
  and its planted scans carry no `outbound_links`. `build-2-sidecar.json`: keys re-generated by
  the harness's own `--regen` (3 key lines only — see note 3).
  `fixtures/build-4-wiki/` (F8, NEW — 11 pages, every page but `lonely-page` with an inbound
  `[[ ]]` from another fixture page; `lonely-page` also carries a SELF-link, so the
  self-link exclusion is exercised), `fixtures/build-4-expected-facts.json` (hand-written from the
  bytes — four of the by-eye short-summary counts were corrected against `len()` of the authored
  strings BEFORE the script ran; the script then matched it), `fixtures/build-4-return-harness.mjs`
  (phase 1 the script for real via `uv run`/`python3` over stdin, phase 2 the seven check-(1)
  cases + four check-(2) + four check-(3) assertions; `--workflow`, `--fingerprint`).

  **Registration:** none — no skill, intent or `module-help.csv` row; the manifest walks
  `scripts/` structurally. **Acceptance:** (1)–(4) PASS at rest (this record); (5) OPEN, bound to
  the first full sweep after v0.18.0 on `{field-vault}` — leg 3 grades live, the at-rest leg is
  green above; (6) field-contingent, second sweep. **Two `candidate` filings owed at handoff**
  (§Out of scope): the `pageHashes` digest-form under-specification (16-hex sidecar term vs
  `shasum -a 256` untruncated), and frontmatter facts from disk for the remaining consumed
  returns. **Not done here, by instruction:** the roadmap's A15-4 sentence ("the page
  `seattle-seahawks` links `[[_agent/research/…cornerbacks-2026]]`") is superseded by disposition
  7's dated note in THIS brief; the roadmap itself was not edited (the builder was told not to)
  — the briefer/owner applies the dated note there.

  **Deviations/notes:** (1) `meta.phases[0].detail` (`:6`) said the scanner returns "findings +
  graph data" and `phases[1]` described a scanner-fed graph — both false after this build and
  neither in the brief's site list; re-worded (nothing parses `meta`, E6 reads schemas only).
  (2) `full-scale.md` step 4's parenthetical enumerated the refusable slots (`rulesetComponents`,
  a `convention_digests` entry, `stubSlugs`) and its re-render clause the same three — a list
  that claims completeness and would have drifted; both gained the two new slots (F3 named
  steps 1/3/5 only). (3) `build-2-sidecar.json`'s committed keys went stale the moment
  `scanFingerprint` moved (its harness reported `committed fixture keys current: NO`); the
  harness's own `--regen` rewrote exactly the 3 key lines, scan payloads untouched — fixture
  upkeep the build-2 harness header provides for, recorded so the diff is attributable. (4) The
  read-back keys `scannerRejected` by the RECORD's slug (`s.slug`), which every existing consumer
  (the pair prompt's path lookup, the cluster labels, `cacheRecords`' `p.slug` skip) already
  reads as the page's slug — the brief's "declared beside `coverageCaps`" became "declared in the
  reduce, before `cacheRecords`", because the exclusion from the cache must precede the record
  loop and the seed loop runs after it; one predicate, evaluated once, its accepted seeds carried
  forward in `calloutsOf`. (5) The fixture's `l-theanine` summary measures 159 chars / 163 bytes
  (two em-dashes), `barbacoa` 160 / 162 (one) — the brief's parenthetical byte figures
  (161 / 163) were its own arithmetic, not a fixture requirement; the character counts, the
  quoted-value counts (161 / 162) and the raw-line counts (170 / 171) match the brief exactly.
  (6) `linksOf` SETS each page's links (duplicates dropped at derivation — the brief's "the reduce
  sets them"), so a duplicated `[[x]]` yields one `missing_targets` line, not two.
module_code: 'vlt'
created: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-08-27-160100-orphan-false-positive-two-consecutive-sweeps.md (A15-1 — the orphan slot: three consecutive 1-of-1 false orphans; the recurrence datum for A14-2)'
  - 'factory/inbox/2026-08-26-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md (A14-2 — the diagnosis A15-1 rests on; pinned in the inbox since Cycle 14; DISCHARGED by this build, roundtable A12)'
  - 'factory/inbox/2026-09-01-140601-same-page-heading-anchors-are-reported-as-missing-targets.md (A15-3 — the stripped `#`; folds in, no build of its own (Q7); the anchor-existence question DECLINED)'
  - 'factory/inbox/2026-09-01-140602-a-scanner-substituted-a-proper-noun-and-the-cache-made-it-permanent.md (A15-4 FIDELITY HALF — direction 1; the eviction half shipped in build-2 (D3); direction 3 stays refused)'
  - 'factory/inbox/2026-08-27-160000-summary-length-check-counts-the-raw-yaml-line.md (A15-5 — direction 1, re-mechanised at the roundtable (A11, D-A); direction 2 eliminated at capture)'
  - 'factory/cycles/14-no-enforcement-point/roadmap.md §Carried forward past Cycle 14 item 12 + §Deferred acceptance ledger build-1 (6) (the BOUND DEBT — `malformed_frontmatter` E4 at 10/8/2; leg 3 alone is the bound; carried here by Q9/A18, with an at-rest leg by D-A) and carries 2, 3 (consumed) and 5 (ruled at the leg-3 grading event)'
roadmap: 'factory/cycles/15-nothing-reads-it-back/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-01/02) → build-4 bullet + its roundtable amendments: Q7 (A15-3 folds; anchor-existence declined), Q9 (Cycle 14 build-1 (6) rides this build, ship-verifiable, GATES), Q2b (after build-2 — satisfied, build-2 BUILT), D3 (A15-4 halved; direction 3 refused; direction 1 cures no poisoned record), D4 (invalidation never weakened on judgment — `pageLinks`/`summaryLengths` do not enter the key), the Round 1 grounding correction (the reduce has no filesystem access), D-C/A12 (REPLACE the scanner''s link return with a SKILL-derived set from an EXECUTABLE; `outbound_links` leaves `PAGE_SCAN`; DA7 retires; single-writer clause → `scanner_return_rejected`; the instrument is the fixture), D-A/A11 (SKILL passes `{slug: summary_len}` from disk; the reduce measures from that; the scanner is told length is not its verdict — prompt string only; hard E6 constraint 3676/3700), A18 (the debt is appended to THIS ledger quoting Cycle 14 verbatim), A21/D-F (carries 2+3 consumed, 5 ruled at leg 3).'
risk: 'moderate — the fan-out''s link graph changes its SOURCE (bytes, not a model) and `PAGE_SCAN` loses a required member, so `scanFingerprint` moves (v0.18.0 is cold by construction already — build-7); a new shipped executable under `skills/vlt-lint/scripts/`; two prior harnesses re-based on the new required args. No convention version moves, no consumer walk, the `// depends_on:` header is untouched (build-7''s). E6 budget FALLS (3676 → 3265 measured) — the one build this cycle that frees it.'
---

# Build #4 — the scanner's returns (A15-1 + A15-3 + A15-4 fidelity half + A15-5, carrying Cycle 14 build-1 (6))

**Intent.** One unaudited return, four mutations, two `fix_now` slots and one `flag_for_human` slot.
The fan-out's reduce (`skills/vlt-setup/assets/workflows/vlt-lint-full.js`) builds its inbound map
and its missing-target list from whatever the page scanners *returned* as `outbound_links` — a link
the scanner does not return does not exist (`:590-591`, `:614`), a link it returns altered is
compared as returned. Three field mutations reached `fix_now` this way: a **dropped** wiki→wiki link
manufactured an orphan three sweeps running (A15-1 — 100% of every orphan the instrument has ever
reported was false), a **stripped `#`** turned a same-page anchor into a missing page (A15-3 — not
the normalizer defect the filing named; `:553-556` already drops a bare `[[#anchor]]`, the value
that arrived had no `#`), and a **substituted proper noun** (`cornerboxes` for `cornerbacks`,
A15-4) reached `missing_targets` and, because the findings cache now works, became permanent. The
fourth mutation is a **measurement**: the scanner's own summary-length verdict counted the raw YAML
line or the quoted value (`171`, `161`) and reached `malformed_frontmatter`, while the reduce's own
`summaryIssue` (`:774`) measured the verbatim return and got both specimens right — two measurers,
one wrong, no comparison (A15-5, corrected at the roundtable A11). That measurement is the third leg
of **Cycle 14 build-1 (6)**, the bound debt this build carries and that GATES closeout.

The roundtable ruled the branch the roadmap had left to brief time: **replace, not audit** (D-C).
The reduce holds every page's *path* and cannot open it — no filesystem access, stated at `:26`,
`:37-38`, `:67-68`, `:606-608` — so the link set moves to the side of the boundary that can read
bytes: the `vlt-lint` SKILL derives each page's `[[…]]` set and each page's parsed `summary:`
length **by an executable it runs** (a sibling of `scripts/lint-cache.py`, never a prose recipe —
A15-2's regex-nobody-ships is the counter-example) and passes them across as `pageLinks` and
`summaryLengths`, on the `crossLayerSlugs` / `pageHashes` precedent. The reduce builds the inbound
map, `missing_targets`, the near-duplicate link sets and the contradiction clusters from that; the
scanner is no longer asked for links at all (`outbound_links` leaves `PAGE_SCAN` — `required` **and**
`properties`); the DA7 `partialShortfall` orphan suppression retires with its cause; the scanner is
told, in the prompt string only, that a summary's length is not its verdict. What the reduce still
consumes from a scanner and *can* read back — a name-verification callout's target, against the
page's own link set — is read back, and a return that fails is never persisted to the cache
(`scanner_return_rejected`, N of T). The promise is the **outcome**: the fixture at rest must show
the report following the bytes against a planted return that contradicts them.

**All rejected alternatives in the parent filings are settled — do not re-litigate:** the audit
branch (compare the return against a value the consumer already holds — ceremony, D-C dissent
conceded); A15-4 direction 3 (move the scan phase off haiku — refused by the filing and by D3);
A15-3's filed direction (drop an empty normalization — already shipped as B5-3, a graded no-op);
A15-5 direction 2 (rename the check as a byte budget — eliminated by `frontmatter.md:125`); the
anchor-existence check (Q7, declined); A14-2's direction 3 (ask the scanner more carefully — the
prompt-side fix whose failure is Cycle 13's premise); replacing the scanner with a parser for the
validity verdict (the filing's own constraint — three genuine specimens parse cleanly under PyYAML
and were correctly flagged; the scanner keeps the verdict, this build takes only the measurement).

## Brief-time dispositions

Every question below is one the roadmap left open or one this headless run had to rule without the
owner; each cites the ruling it stands on. Nothing here re-decides an ideation ruling.

### 1. The executable — `skills/vlt-lint/scripts/lint-page-facts.py`, one run, two per-page facts (D-C, D-A)

**Ruled: one script, `lint-page-facts.py`, emits BOTH maps from ONE read of each page's bytes**, and
it emits **facts, never verdicts** — raw `[[…]]` inner texts and an integer length, with the
normalization (`normalizeTarget`, `:104-109`, B5-3) and the 160-character verdict (`:774`) staying
in the workflow where they already live. Two scripts would read every page twice; a verdict in the
script would put the limit in a second home. Contract:

- **Input** — `--pages <path|->`: the same `[{slug, path}]` array step 1 already builds (a file, or
  stdin), so the two maps are keyed by the **SKILL-supplied slug**, never a slug the script derives
  (the `cacheRecords` principle at `:566-568`: keying on anything else lets a derivation drift from
  the population).
- **Output** — `--out <path>` (default stdout): one JSON object
  `{"pageLinks": {slug: [inner, …]}, "summaryLengths": {slug: int}, "unreadable": [slug, …],
  "pages": N}`. At scale the SKILL writes it to the scratch directory and the wrapper-writing step
  (full-scale.md step 3) embeds the two maps — the payload never transits the caller's context
  (A15-11's posture, Q2b's reason for the ordering).
- **`pageLinks` population — the executable form of `checks.md:13`'s population statement,
  verbatim:** only `[[ ]]`-delimited text is an outbound link; a `[[wikilink]]` inside an inline
  code span or a fenced code block is not one (`frontmatter.md` rule 5); bare text, a filename or a
  path that is not `[[ ]]`-delimited is not one. Concretely: the file's bytes read as UTF-8;
  fenced blocks (a line opening with ``` or `~~~`, to the matching closer) removed; inline spans (a
  run of N backticks to the next run of N on the same line) removed; then every match of
  `\[\[([^\[\]]+?)\]\]` yields its inner text **raw** — `|alias`, `#anchor`, path prefix, all
  intact; an embed's leading `!` is outside the brackets and is not part of the text. **Frontmatter
  is scanned like body text** — a wiki page's quoted `"[[path]]"` `sources:` entry is a link (rule 4:
  *a wiki page's `sources:` is a link graph*), which is also what the scanners have been returning
  (the live sidecar's `seattle-seahawks` record carries the frontmatter wikilink's basename).
  Duplicates are kept as they occur (the reduce sets them; counts are not a fact anything reads).
- **`summaryLengths` — the parsed scalar, in characters (code points), never bytes**
  (`frontmatter.md:125`: *counting characters, not bytes — em-dashes count as one*). The
  frontmatter block is the leading `---` line to the next `---`/`...` line; the first `summary:`
  line's value is unquoted per its form — double-quoted (`\"`, `\\` unescaped), single-quoted
  (`''` → `'`), plain (trailing ` #comment` stripped); a block-scalar indicator (`>`/`|`, a form rule
  2 forbids) collects its indented continuation lines joined by one space, a documented
  approximation. The length is Python `len()` of that string. No frontmatter, no `summary:` key,
  or an empty value → **0**, which the reduce renders as `summary missing`. **No dependency**
  (`# /// script` with `requires-python` only, the `lint-cache.py` precedent) — the module's
  release gate and every vault must run it with nothing installed; a PyYAML parse would be the
  honest "parsed scalar" but is not available at that cost, and the three specimen forms above are
  the whole of what the convention permits.
- **`unreadable`** — a page whose bytes cannot be read or decoded is listed by slug and absent from
  both maps; the workflow renders the gap denominated (disposition 4). Exit 0 whenever the input
  parsed; non-zero only for an unreadable `--pages` input or an unwritable `--out`.

**The whole args derivation is NOT folded here.** Build-2 and build-3 both recorded *"a shipped
discovery executable"* as this build's follow-on (build-2 disposition 6, build-3 §Out of scope).
Grounded against the letter of D-C — *the SKILL derives each page's `[[…]]` set by an executable*
— the executable this build owes is the one that derives the two byte-facts; folding `pageHashes`,
`crossLayerSlugs` (the `vault_structure` predicate single-homed at full-scale.md step 1),
`stubSlugs` (the heading procedure build-3 just homed at `checks.md:13`), `overlayNames`, the three
convention digests and the wrapper file into it would move five single-homed prose mechanics into
a script in a build ruled for four filings about one seam. It is recorded again as the follow-on,
now with a grounding datum that argues for a ruling before it is taken: the live sidecar's per-page
key term is **16 hex characters** (`_agent/lint-cache.json`, every record) while full-scale.md step
1 names `shasum -a 256` for `pageHashes` and states **no truncation** — the SKILL has been
truncating by analogy with step 2's convention digests. A script that emitted the full digest would
make every page cold once and then disagree with any run that fell back to the recipe. That is a
`candidate` filing at handoff (§Out of scope), not this build's to fix. The follow-on sentence at
full-scale.md `:18` is re-pointed (F3): it now says which two facts ship as an executable and which
remain the recipe.

### 2. `pageLinks` and `summaryLengths` are REQUIRED args; wrong type is a pre-dispatch refusal; a missing slug entry is a denominated cap (build-3's split, applied to this build's own slots)

- **Absent** (key not in `args`) → the **args-guard error** at `:150-152` names them beside `pages`
  / `indexPath` / `conventionsPath`: a fan-out with no link set cannot produce `orphans`,
  `missing_targets`, `near_duplicates` or clusters, and one with no length map cannot produce the
  summary clauses of `frontmatter_drift` — four `fix_now`-side slots would render empty and read as
  health. An optional-with-a-cap posture (the overlay args' shape at `:420-426`) was considered and
  refused: it re-creates A15-1's observable (an empty orphan slot that means "not computed") under a
  new cause. This is the **caller-contract** class (build-3 disposition 2 — the `{error}` shape,
  not the failed-run shape): the SKILL did not run the script.
- **Present but of the wrong type** — `pageLinks` not a plain object, `summaryLengths` not a plain
  object, `pageLinks[<slug>]` not an array, `summaryLengths[<slug>]` not a non-negative integer →
  the **pre-dispatch refusal** (`:435-462`), by name (`pageLinks[<slug>]`, the
  `convention_digests[<name>]` grammar), joining `wrongTypeSlots` at intake. A rendering error is
  detectable before the first agent dispatches and is never rendered as an absence (D2 iii, A14).
  **This does not re-rule D2's population** — D2's three denominated slots are unchanged, and
  build-3's `candidate` about the four legacy optional args (`overlayNames`, `crossLayerSlugs`,
  `pageHashes`, `cachedScans`) is unchanged; a slot *introduced* by this build takes the posture the
  cycle established rather than adding a fifth to that filing.
- **A slug in `pages` with no entry in `pageLinks` / `summaryLengths`** (the script's `unreadable`
  list, or a hand-composed map) → **computed anyway, denominated**: a coverage cap
  `pageLinks: K of T pages carry no link set — [slugs]; an orphan whose only inbound link would sit
  on one of these is not visible` (and the sibling for `summaryLengths`, the summary clauses
  rendered for T − K pages). Suppressing the slots was DA7's shape and is what this build retires;
  naming exactly which pages were blind is D2's.

### 3. What "replace" changes in the reduce, site by site — and what the cache stores (D-C, D4)

`linksOf(slug)` = `(pageLinks[slug] || []).map(normalizeTarget).filter(Boolean)` — computed once
after intake, over **`pages`** (filesystem truth, the A10-17 posture), never over `scans`. Then:

- **inbound** (`:590-591`) — from `linksOf` over every page, **excluding self-links** (a page's link
  to itself is not an inbound link; `checks.md:25` reads *"no inbound links from other wiki pages"*
  — the shipped code counted self-links, a latent over-count grounded here and corrected to the
  rule's letter).
- **`orphans`** (`:605`) — `pages.filter((p) => !(inbound.get(nslug(p)) > 0)).map((p) => p.slug)`:
  the population is every page on disk, not every page that scanned. The `partialShortfall`
  predicate, its cap, and the `:647` loop guard **retire** (disposition 8).
- **`missing_targets`** (`:613-614`) — `for p of pages, for l of linksOf(p.slug)`: a target in none
  of `pageSlugSet` / `crossLayer` / `stubs` is missing, rendered `${p.slug} → ${l}`. `[[#anchor]]`
  still normalizes to `''` and is dropped (B5-3, unchanged); `[[page#anchor]]` still resolves to
  `page`. The same-page anchor of A15-3 and the substituted noun of A15-4 cannot reach this slot
  because the value compared is the page's own bytes.
- **near-duplicate link sets** (`:626`) and **cluster adjacency** (`:681-684`) — `linksOf(s.slug)`
  in place of `s.outbound_links`; the pair loop's `!partialShortfall` guard goes.
- **The cache** — `cacheRecords` (`:577-583`) is unchanged in shape and key. A record's `scan` no
  longer carries `outbound_links` (the scanner is not asked); the `:575-576` comment retires.
  **D4, shown not asserted:** `pageLinks` and `summaryLengths` are not scanner inputs — no cached
  fact depends on them, and the reduce recomputes every link-derived and length-derived verdict from
  them **every run** (the cache stores extracted facts, never verdicts — `full-scale.md` step 5) —
  so they do **not** enter `runKey` (`:367`), and a page whose bytes change already misses on
  `pageHashes`. The harness proves it (§Acceptance (1) case (g)): the same cached record, a changed
  `pageLinks`, and the orphan verdict follows `pageLinks`. Widening the key to them would be
  weakening nothing and strengthening nothing — it would cold-miss every page on every run because
  the maps are recomputed from bytes each time. D4 stands with its reason.
- **Sidecar records written before this build** still carry `outbound_links` inside `scan`; they are
  ignored, not rejected — and v0.18.0's first sweep is cold by construction anyway (build-7 moves a
  scanner-read convention; this build moves the scan surface too, §Verification 2).

### 4. `summaryLengths` is the ONLY source of the summary clauses; the returned `summary` is no longer read (D-A)

`summaryIssue` (`:774`) becomes a function of `summaryLengths[slug]`: `0` → `summary missing`;
`> 160` → `over-length (N chars)`; otherwise no clause. The returned `summary` string is not read by
any verdict after this build — it stays in `PAGE_SCAN` (D-A's letter: the scanner is *told* length
is not its verdict; removing the field is a retirement the beat did not name and this brief does not
take) and is carried in the record as a fact. **Cycle 14 carry 2 is consumed here**: the paraphrase
case (Cycle 13 CF1, `l-theanine` 162 returned vs 159 on disk) cannot reach a verdict because no
verdict reads the return. **Why the read-back on `summary` is NOT taken** (it was drafted): a
read-back protects a *consumed* value; after this build `summary` is consumed by nothing, so
comparing its length against `summaryLengths` and rejecting the record on a mismatch would be the
ceremony D-C refused — and it would cold-miss every page a scanner cannot return byte-exact, for no
verdict's benefit. The cost of that decision is stated: a paraphrased `summary` persists in the
sidecar as a fact nothing reads; the field-contingent check counts how often the callout read-back
(disposition 5) rejects, which is the rate this decision leaves unmeasured for `summary`.

### 5. The single-writer clause reaches ONE consumed value: the callout target (A12)

*"Any scanner-returned value the reduce still consumes after this build is subject to step 5's
single-writer clause: a return that fails a read-back is never persisted."* Grounded against every
value the reduce reads after this build: `name_callout_targets[].target` is compared (`:737-741`)
against `pageSlugSet` and is the seed of the entity-pair pass — **it has a read-back source now**
(`linksOf(s.slug)`): a callout's target must be one of the page's own links. A returned target not
among them is a fabricated seed → the seed is dropped, the page's record is **excluded from
`cacheRecords`**, and one denominated cap renders: `scanner_return_rejected: N of T records — <slug>:
callout target '<target>' is not among the page's links; …` (T = `scans.length`, both halves). The
remaining consumed values — `title`, `category`, `created`, `last_updated`, `verified_by`,
`verified_at`, `review_after`, `topic_is_list`, `thin`, the frontmatter verdict, the Gap B verdict,
the prose arrays — have **no SKILL-passed fact to read against**; the clause reaches them when a
fact does, and that widening (frontmatter facts from disk) is named in §Out of scope as a
`candidate`, not smuggled in. **Why exclusion from the cache and not only a cap:** a record whose
returned callout target is invented is a record the same scanner can invent again from the cache,
permanently (A15-4's amplification) — the next sweep re-derives it, which is the eviction posture
build-2 shipped, applied at derivation time.

### 6. The fixture is the instrument; the specimens are corroboration (A12)

The `[ship-verifiable]` checks run over `fixtures/build-4-wiki/` (real files on disk — the script
must actually read bytes), a hand-written oracle `fixtures/build-4-expected-facts.json`, and
`fixtures/build-4-return-harness.mjs` planting scanner returns **at odds with the bytes**. The
specimens reach the fixture as its page shapes: `fantasy-football-evaluation` →
`[[fantasy-platform-read-access]]` and `chicken-soup` → `[[katsuo-dashi]]` (A15-1's second and
third sweeps), `calf-strain`'s `[[#Early Loading Phase (≈ Days 3–7)]]` (A15-3, the `≈` and `–`
deliberately kept — multi-byte), `seattle-seahawks`'s `cornerbacks` research-note link (A15-4),
and the two refuted summaries frozen from disk at their exact lengths (A15-5, disposition 7).
Specimens clearing in the field is `[field-contingent]` (§Acceptance (6)): the v0.18.0 cold sweep
re-rolls every scanner and a specimen can clear by a lucky roll with no mechanism in the tree.

### 7. Grounding correction — the A15-5 fixture arithmetic and the A15-4 link form (recorded here and in the roadmap)

- Roundtable A11 specified the at-rest leg's fixture as *"a quoted 158-char summary whose raw line
  is 161"*. Measured on disk 2026-09-02 (read-only): **`l-theanine`** — parsed **159** characters
  (161 bytes), quoted value **161** characters, raw line 170; **`barbacoa`** — parsed **160**
  characters (163 bytes, exactly at the cap), quoted value 162, raw line **171** characters. The two
  reported numbers are therefore two *different* wrong measurements — `161` is the quoted value (or
  the parsed byte count), `171` the raw line. The fixture freezes **both specimen shapes at their
  real lengths** (159/161 and 160/162/171) rather than A11's 158/161, which no measurement of either
  page produces. The live sidecar confirms the returned `summary` strings are currently verbatim (159
  and 160) with `frontmatter_defect: none` — the refuted verdicts arrived through the verdict slot,
  not through the return, exactly as A11 re-grounded.
- A15-4's capture states *"the page `seattle-seahawks` links
  `[[_agent/research/2026-07-26-112444-espn-top-10-cornerbacks-2026]]`"*. On disk 2026-09-02 the
  page carries that note as a **bare-path `sources:` entry** (rule 4's legacy form), not a `[[ ]]`
  link — and no `[[ ]]` form of it anywhere on the page. So the specimen was **two** mutations at
  once: the scanner treated a bare path as a link (the population statement's own exclusion) *and*
  substituted the noun. Under this build the entry is not a link at all and the finding vanishes by
  population; the fixture plants the `[[ ]]` form the roadmap describes **and** the bare-path twin,
  so both mutations are exercised. The roadmap's sentence is superseded by a dated note.

### 8. Interim posture (R1) — not applicable

Every finding, cap and refusal this build changes ships with its mechanism in the same commit:
the executable, the reduce, the prompt sentence and the docs land together. `R1: not applicable.`

### 9. Retirement (P-15; obsolescence beat A20) — SUBSTANTIVE

| Retired | Site (re-grounded) | Superseded by |
|---|---|---|
| `outbound_links` as a scanner ask — from `required` **and** `properties` | `vlt-lint-full.js:188`, `:198` | `pageLinks` from `lint-page-facts.py`. A half-retirement (kept in `properties`, dropped from `required`) would leave the ask in the schema an executor still answers and pays for; the beat's *"leaves `required`"* is honoured by removing the member whole (E6: 3676 → **3265**; required-only would read 3659). |
| the verbatim-extraction sentence's link clause — *"keep any \|alias, #anchor, or path prefix intact"* as an instruction about links | `:262` | narrowed to the callout target (which the scanner still returns raw) + one sentence saying links are never asked; the sentence survives re-nouned, not deleted |
| the DA7 `partialShortfall` suppression — predicate, cap, the `:647` guard, the `:588` *"stay scans-denominated (DA7)"* clause | `:593-605`, `:647`, `:588` | link-graph slots computed over `pages` from bytes; a page without a link set is a **denominated** cap (disposition 2), never a suppressed slot |
| the scanner's summary-length verdict | the prompt's frontmatter-verdict sentence, `:263` (prompt string only — A11's hard constraint) | `summaryLengths` → `summaryIssue` (`:774`); `checks.md:15` already excludes *"a way the field-level check above … does not already cover"* — an Arc 9 D5 elimination, no precedence statement |
| the cache comment *"the payload carries outbound_links in the NORMAL FORM"* | `:575-576` | the record carries no link list |
| the follow-on sentence *"A shipped discovery executable … is not this reference's — the recipe above is the route until one ships"* | `full-scale.md:18` | re-pointed: two facts ship as `lint-page-facts.py`; the rest remains the recipe (disposition 1) |
| *"reduces the link graph in JS (orphans / missing targets / near-duplicates)"* as a description of a scanner-fed graph | `full-scale.md:18` | *"over the SKILL-derived link sets"* |
| the refusal example *"a `missing_targets` slug the page's own bytes do not carry"* | `full-scale.md:21`, `fix-and-file.md:16` | impossible after this build; the example becomes *"a `missing_targets` target that does exist on disk — a cross-layer file the derivation missed"* |

**Population statements that do NOT move:** `checks.md:13`'s link population (it becomes the
script's specification — the rule's home is unchanged, the script is its executable); `checks.md:25`'s
orphan definition; `frontmatter.md:125`'s 160-character, characters-not-bytes limit;
`normalizeTarget`'s normal form (`:104-109`) — raw in, normal form in the reduce, one home;
`checks.md:15`'s validity verdict stays the **scanner's** (the filing's constraint — three genuine
specimens parse cleanly and were correctly flagged; no parser replaces it); the Layer-2 population
exclusion. **Cycle 14 carry 5** — the `malformed_frontmatter` *retirement* — is **not** taken here:
D-F re-bound it to this build's leg-3 grading event (§Acceptance (5)); this brief retires the
length verdict *inside* the class, not the class.

## Boundary with build-7 — stated so build-7's briefer inherits it (A1, A2)

Builds 4 and 7 both edit `vlt-lint-full.js`, both move `scanFingerprint`, and neither touches the
other's literals. **Merge order 4 → 7; build-7 re-grounds every line number after this build's
commit** (the edits below shift the file by tens of lines).

| Region (at `7222cd2`) | Build-4 (this brief) edits | Build-7 edits |
|---|---|---|
| `:11` `// depends_on:` header | untouched | `write-verification@5` → `@6` |
| `:26-93` arg contract | `pageLinks` / `summaryLengths` rows; `pages`' required list gains them | untouched |
| `:185-216` `PAGE_SCAN` | `outbound_links` removed from `:188` and `:198`; **no description edited** | `:205` (`sources_vs_prose` description) and `:209` (`unmarked_supersession` description) `@5` literals → `@6` — a **description** edit build-7 owns; budget after build-4 is 3265, so the two-character bumps fit with room |
| `:260-263` `pageScanPrompt` | `:262` link clause re-nouned; `:263` gains the length-exclusion sentence (end of the string) | `:261`'s `per write-verification@5` literal → `@6` (same template literal, different line) |
| `:818` `write-verification@5` comment | untouched | `@6` |
| `:553-614`, `:626`, `:647`, `:681-684`, `:774` reduce | the link-source and length-source rewrite | untouched |

Both builds make v0.18.0's first sweep cold; build-2's check (4) expects the cold reason to name
`write-verification` **and** the scan surface — true after either or both. Build-7's briefer reads
disposition 3 (the cache is untouched in shape) before pricing its own `:229`-region edit.

## F-sites

Every `file:line` below was re-derived against the working tree at brief time (branch
`cycle15-v0.18.0`, tip `7222cd2`, builds 1–3 BUILT). The roadmap's capture-time cites were
pre-build-2 and moved substantially — the corrections are written at the build-4 bullet in the
roadmap and restated per site here.

### F1 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the link source, the length source, the retirements (MOVED by builds 2/3; re-grounded)

1. **`:26-93` — the arg contract** *(HOLDS at `:30-90`)*. Add two rows after `pageHashes` (`:49`):
   `pageLinks: {slug: [string]}` — *"every `[[…]]` inner text on the page, RAW, derived from the
   page's bytes by `vlt-lint/scripts/lint-page-facts.py` (the SKILL has filesystem access, this
   script has none — the `crossLayerSlugs` division); the reduce normalizes (`normalizeTarget`) and
   builds the link graph from THIS, never from a scanner return (A15-1/A15-3/A15-4, D-C). REQUIRED.
   A present non-object, or a non-array entry, is refused before dispatch; a page with no entry is
   a denominated cap"* — and `summaryLengths: {slug: int}` — *"the parsed `summary:` scalar's length
   in characters, from the same script (A15-5, D-A); the reduce measures from THIS, never from the
   returned `summary`. REQUIRED; same refusal/cap posture."* Both state: *"NOT a cache-key term —
   recomputed from bytes every run; no cached fact depends on them (D4)."* The `:32` `pages` row's
   *required* note and the guard message (`:150-151`) name them.
2. **`:111-136` — intake** *(HOLDS)*. After `:134` `pageHashes`: `const pageLinks =
   isPlainObject(a.pageLinks) ? a.pageLinks : {}` and `summaryLengths` likewise; **wrong-type facts
   into `wrongTypeSlots`** (`:127-129` pattern): the map itself (`expected: 'plain object'`), and
   per slug in `pages` — `pageLinks[<slug>]` not an array (`expected: 'array'`),
   `summaryLengths[<slug>]` not a non-negative integer (`expected: 'integer'`) — refused by name in
   the `:435-462` refusal (its `next:` gains *"pageLinks / summaryLengths per references/full-scale.md
   step 1 (re-run scripts/lint-page-facts.py)"*). The comment at `:118-124` names the two new slots
   as refused **on this build's own ruling** and leaves the four legacy args' sentence intact.
3. **`:150-152` — the args guard** *(HOLDS)*. `if (!pages.length || !indexPath || !conventionsPath
   || a.pageLinks === undefined || a.summaryLengths === undefined)` → the error names all five and
   says *"the vlt-lint SKILL derives pageLinks/summaryLengths by scripts/lint-page-facts.py
   (references/full-scale.md step 1)"*.
4. **`:185-216` — `PAGE_SCAN`** *(roadmap `PAGE_SCAN` HOLDS; `:198` is the row)*. Remove
   `'outbound_links'` from `required` (`:188`) and the `outbound_links` property (`:198`). **No other
   character of the schema changes** (A11's hard constraint). Measured with `package-lint`'s own
   `_E6_NODE_EXTRACTOR`: **3676 → 3265**; the builder re-measures and records the number.
5. **`:260-263` — `pageScanPrompt`** *(roadmap `:229-230` → `:260-263`; the `@5` literal at `:261` is
   build-7's — untouched)*. `:262`: *"Extract verbatim: do not normalize, and keep any |alias,
   #anchor, or path prefix intact."* → *"Extract verbatim: do not normalize — a name-verification
   callout's [[wikilink]] target keeps any |alias, #anchor, or path prefix intact. Do NOT report the
   page's outbound links: the link set is derived from the page's own bytes downstream and is never
   asked of you."* `:263`, appended to the frontmatter-verdict sentence: *"The summary's LENGTH is
   never a frontmatter defect of any kind — it is measured downstream from the page's own bytes (per
   frontmatter@14, the 160-character limit); never report a length complaint in frontmatter_defect,
   frontmatter_defect_fields, or frontmatter_defect_detail."* (`per frontmatter@14` is the R4
   inline source marker the header at `:16-21` requires of a restated rule; `frontmatter` is not
   bumped this cycle — A7.) This moves `scanFingerprint` (`:279-280`) — deliberate, §Verification 2.
6. **`:553-556` — the normalize-in-place** *(roadmap `:420-423` → `:553-556`)*. Replace with
   `const linksOf = new Map(pages.map((p) => [p.slug, (pageLinks[p.slug] || [])
   .map(normalizeTarget).filter(Boolean)]))` and the denominated gap cap of disposition 2 (K of T,
   slugs named; the sibling for `summaryLengths`). The B5-3 comment survives re-nouned: *the SKILL's
   script extracts raw inner text; every comparison below runs on the normal form computed HERE.*
7. **`:559-583` — `cacheRecords`** *(HOLDS)*. `:575-576` comment retired (disposition 9). The
   rejection of disposition 5 is applied here: a slug in `scannerRejected` is skipped, with the
   comment stating why (a fabricated return must not be served from the cache next sweep).
8. **`:585-614` — the link graph** *(roadmap `:457` → `:590-591`; `:472` → `:605`; `:480` →
   `:613-614`; `:460-472` DA7 → `:593-605` + `:647` + the `:588` clause)*. Per disposition 3: inbound
   over `pages` × `linksOf`, self-links excluded; `partialShortfall` and its cap **deleted**;
   `orphans` over `pages`; `missing_targets` over `pages` × `linksOf`. The `:585-588` comment's last
   sentence becomes *"Inbound-derived slots are computed from the SKILL-derived link sets and are
   complete regardless of scan coverage (Cycle 15 build-4, D-C)."*
9. **`:616-661` — near-duplicates** *(HOLDS)*. `:626` `linkSets` from `linksOf(s.slug)`; `:647`
   loop guard loses `!partialShortfall &&`; the `:646` comment retires.
10. **`:671-687` — clusters** *(HOLDS)*. `:681`, `:683`, `:684` read `linksOf(s.slug)` /
    `linksOf(t.slug)`.
11. **`:734-742` — the callout seed loop** *(HOLDS)*. Before `pageSlugSet.has(target)`: `if
    (!linksOf.get(s.slug).includes(target)) { scannerRejected.set(s.slug, …); continue }` — the
    read-back of disposition 5; `scannerRejected` is a `Map<slug, reason>` declared beside
    `coverageCaps`; after the loop, one cap `scanner_return_rejected: N of T records — …` (rendered
    only when N > 0 — a `0 of T` line in the caps list would read as a health claim; the denominated
    zero lives instead in the top-level fact `scanner_return_rejected: {count, of, slugs}`, returned
    on every completing run, which the SKILL renders as the report's own line (F2)).
12. **`:773-774` — `summaryIssue`** *(roadmap `:640` → `:774`)*. Per disposition 4:
    `const summaryIssue = (slug) => { const n = summaryLengths[slug]; if (!Number.isInteger(n))
    return ''; return n === 0 ? 'summary missing' : n > 160 ? \`over-length (${n} chars)\` : '' }` —
    called with `s.slug` at `:906-908`; the B5-3 comment at `:773` re-nouned (*the SKILL's script
    measures, JS does the verdict*). The `160` stays here — the reduce's single home for the limit
    (`checks.md:14` and `frontmatter.md:125` are the rule's).
13. **`:895-1021` — the return** *(HOLDS)*. Add `scanner_return_rejected: {count, of, slugs}` beside
    `entity_scan_facts` (`:992`), with the comment that the SKILL renders it on the report (F2).
14. **Header `:16-21` (R4)** — unchanged: no ask is added, no convention joins the read list;
    `SCANNER_CONVENTIONS` (`:254`) unchanged. The `// depends_on:` line (`:11`) is **build-7's**.

**Out of scope at this site:** `unmarked_supersession`'s structure (Cycle 14's carried dissent);
the `:945-948` `para_*` slots; `INDEX_SCAN` / `CLUSTER_FINDINGS` / `PAIR_FINDINGS` (no link return in
them — the index pass reads the index itself, a SKILL-side read the workflow does not duplicate).

### F2 — `skills/vlt-lint/references/report.md` — one fact, rendered (HOLDS)

- `:76` `coverage_caps:` — the illustrative list is a subset and is **not** widened (CLAUDE.md: lists
  that claim completeness drift); the new caps ride the slot as caps do.
- `:79` `lint_cache:` — unchanged.
- **New scalar** after `stub_discovery:` (`:15`): `scanner_return_rejected: <N of T records — a
  scanner-returned value the reduce read back against the page's own bytes and refused; the page's
  record was not cached and is re-derived next sweep; 0 of T renders>` — full mode via the
  workflow; scoped/inline render `not instrumented (inline run)` (the `cost_accounting` idiom at
  `:77`). **Build-5 boundary:** this is a mandated scalar with no per-file cardinality; build-5's
  validator reads `report.md` at build-3's commit **plus this key** — merge order on `report.md`
  becomes **3 → 4 → 5**, stated so build-5's briefer re-grounds the key set after this commit
  (build-3's brief §Boundary is BUILT and is not edited; build-5's briefer reads both tables).
- `:90` **Findings-cache reporting** gains one sentence: *a record refused by the reduce's read-back
  (`scanner_return_rejected`) is not among `cache_records` — the next sweep re-derives that page; the
  count is the report's own line, never folded into `rejected R of P` (which counts sidecar records
  the reader filter discarded, a different seam).*

### F3 — `skills/vlt-lint/references/full-scale.md` — steps 1, 3, 5 (HOLDS; build-2/3 text re-grounded)

- **Step 1 (`:7`)** — after the `pageHashes` sentence: *"Then derive the two per-page byte facts the
  reduce's link graph and summary-length clauses run on — run `uv run --quiet
  "$SKILL/scripts/lint-page-facts.py" --pages <pages.json> --out <scratch>/page-facts.json` over the
  same `pages` list (keyed by the slugs you supplied) and pass its `pageLinks` and `summaryLengths`
  maps **as returned** — you never derive a link set or a length yourself, and the workflow refuses a
  run without them. The script implements `references/checks.md` Missing targets' population
  statement (only `[[ ]]`-delimited text; code spans and fenced blocks excluded) and
  `{conventions}/frontmatter.md`'s character-not-byte length; a page it lists as `unreadable` is
  named on the report's coverage cap by the workflow."* Instrument named per the operating
  contract's *Honest reporting* rule: the script, by path.
- **Step 3 (`:9-18`)** — the args object gains `pageLinks, summaryLengths`; the size note becomes
  *"~84KB plus the two page-facts maps"*; the sentence *"derive it by an executable you run"* now
  points at step 1's script for the two facts and keeps the recipe for the rest; the follow-on
  sentence at `:18` is rewritten per disposition 9 (*"`lint-page-facts.py` ships the two byte-facts;
  `pageHashes`, `crossLayerSlugs`, `stubSlugs`, `overlayNames`, the digests and the wrapper remain
  this recipe's — a whole-derivation executable is the recorded follow-on, gated on the
  `pageHashes` digest-form filing"*); *"reduces the link graph in JS (orphans / missing targets /
  near-duplicates)"* → *"over the SKILL-derived link sets"*; the resume sentence's nulled-args list
  gains the two.
- **Step 5 (`:20-21`)** — the refused-finding example re-worded (disposition 9); one sentence after
  the `write`: *"A record the workflow refused on read-back (`scanner_return_rejected`) is already
  absent from `cache_records` — nothing to evict; the report's line carries the count."* (R3 for
  the cap: nothing owed — the next sweep re-derives.)

### F4 — `skills/vlt-lint/references/checks.md` — two pointers, one word (HOLDS at `:13`, `:14`, `:25`)

- `:13` **Population (both modes)** — after the sentence: *"The executable form of this statement is
  `scripts/lint-page-facts.py`; full mode at scale runs it (`full-scale.md` step 1) and the fan-out
  builds its link graph from its output, never from a scanner's link return; an inline run may run it
  too."* The population itself is untouched (disposition 9).
- `:14` **Frontmatter / Bases-field drift** — `summary:` clause gains *"(measured on the parsed
  scalar in characters — at scale by the same script; the scanner's verdict never carries a length
  complaint)"*.
- `:25` **Orphan pages** — untouched in rule; a parenthetical *"(at scale: computed from the
  SKILL-derived link sets over every page on disk, never from what scanned)"*.
- `:15` **Malformed frontmatter** — untouched: its *"in a way the field-level check above does not
  already cover"* is the exclusion the prompt now states; no second statement of the rule.

### F5 — `skills/vlt-lint/references/fix-and-file.md:16` — the refusal example (HOLDS)

The parenthetical's second example re-worded per disposition 9. Nothing else.

### F6 — `skills/vlt-lint/scripts/lint-page-facts.py` — NEW (disposition 1)

The contract of disposition 1, verbatim in its docstring (input, output, the population statement's
executable clauses, the length rule, the `unreadable` list, exit codes, *facts never verdicts*, the
no-dependency rule). Sibling of `lint-cache.py`: same `# /// script` header, `argparse`, one
`--pages` and one `--out`. A `--self-test`-style mode is **not** shipped — the factory harness
(F8) is the test; a vault does not run tests.

### F7 — the prior harnesses — `fixtures/build-2-key-harness.mjs`, `fixtures/build-3-type-harness.mjs` (cross-build obligation, the build-3 F7 precedent)

Both compose `baselineArgs` without the two now-required args (`build-2:70-74`, `build-3:105-111`)
and would hit the guard. Each gains `pageLinks` (from every fixture record's `scan.outbound_links` —
the sidecar fixture still carries them; the maps are equal to what the scanner returned, so every
prior expectation is unchanged) and `summaryLengths` (`scan.summary.length`). Build-3's `--stubs`
mode (`:133-150`) feeds links through `scanFor(slug, links)` → it passes them as `pageLinks` instead.
**The runtime shim is factored into `fixtures/vlt-lint-full-shim.mjs`** and imported by all three
harnesses — build-3's own header ruled *"a shared shim is a refactor for whichever build adds a
third harness"*; this is the third. Build-2 check (1) stays **15/15**; build-3 checks (1)–(3) stay
green; both re-run in §Verification.

### F8 — `fixtures/build-4-wiki/`, `fixtures/build-4-expected-facts.json`, `fixtures/build-4-return-harness.mjs` — NEW (disposition 6)

**The fixture wiki** (eleven pages; slugs are the specimens' where a specimen exists — every slug
is already on the public roadmap or is synthetic; no vault-local content). **Every page except
`lonely-page` carries at least one inbound `[[ ]]` from another fixture page** (the builder wires
the "one link" / "two other links" cells so that this holds — it is what makes `orphans ===
['lonely-page']` a sharp expectation rather than a list to eyeball):

| page | bytes carry | exercises |
|---|---|---|
| `fantasy-football-evaluation` | `[[fantasy-platform-read-access]]` + two other links | A15-1 (the dropped link) |
| `fantasy-platform-read-access` | links out, none back | must NOT be an orphan |
| `chicken-soup` | `[[katsuo-dashi]]`, `[[katsuo-dashi#Simmer]]` | A15-1 second sweep; `page#anchor` → page |
| `katsuo-dashi` | one link | must NOT be an orphan |
| `calf-strain` | `[[#Early Loading Phase (≈ Days 3–7)]]`, `[[#Red Flags]]`, both headings present | A15-3 |
| `seattle-seahawks` | frontmatter `"[[sources/articles/2026-07-07-espn-top-10-cornerbacks-2026-execs-coaches-scouts]]"`, a bare-path `_agent/research/2026-07-26-112444-espn-top-10-cornerbacks-2026.md` `sources:` entry, and a body `[[_agent/research/2026-07-26-112444-espn-top-10-cornerbacks-2026]]` | A15-4 both forms; `crossLayerSlugs` carries both basenames |
| `l-theanine` | the frozen summary: parsed **159** chars / quoted 161 / two em-dashes | A15-5 refuted #2 |
| `barbacoa` | the frozen summary: parsed **160** chars / quoted 162 / raw line 171 | A15-5 refuted #1 — exactly at the cap |
| `parallel-walk-introduction` | a synthetic 162-char summary with an em-dash | the GENUINE over-length control (Cycle 14's 2026-08-26 specimen, length only) |
| `lonely-page` | no inbound link anywhere; `summary: ""` | the genuine orphan + `summary missing` controls |
| `code-fence-page` | ```` ```[[ghost-page]]``` ```` in a fence, `` `[[ghost-two]]` `` in a span, and a real `[[missing-target-page]]` | population exclusions + the genuine missing-target control |

**The oracle** `build-4-expected-facts.json` is **hand-written from the bytes** (every `[[ ]]` listed
by eye, every length counted by the convention's rule), never generated by the script — it is what
makes the script's check failable (§Acceptance (1) adversary). **The harness** runs the script for
real over the fixture wiki (`uv run --quiet`, falling back to `python3`), deep-compares its output to
the oracle, then loads the workflow through the shared shim with a **counting** agent stub whose
`scan:` returns are the planted, at-odds records and whose `entity-pair:` labels are captured;
`--workflow <path>` runs the same table over another copy (failability against `7222cd2`).

## Registration

**None.** No new skill, no new intent, no `module-help.csv` row (`vlt-lint`'s row is unchanged — no
user-facing phrase changes). `lint-page-facts.py` is a skill asset under `skills/vlt-lint/scripts/`,
a tree `verify-skill-manifest.py` walks whole (`:14` — *"whole trees: SKILL.md, assets/, references/,
scripts/, and anything a future build adds"*), so the manifest picks it up structurally. No
convention `version:` moves; no consumer walk; the workflow's `// depends_on:` header is untouched.
**Priced anyway:** package-lint **E6** falls (3265), **E5** reads the unchanged header, **E7** sees the
existing `@5`/`@14` body literals plus one new `frontmatter@14` marker (current pin — passes); no
new package-lint check, so **E4** owes no `test-package-lint.py` case; **C6** untouched (no contract
edit).

## Out of scope (dispositioned)

- **A whole-args discovery executable** (build-2 disposition 6, build-3 §Out of scope) — the
  follow-on again, now gated on a **`candidate` filing at handoff**: *"`pageHashes` digest form is
  under-specified — the live sidecar's page term is 16 hex characters while `full-scale.md` step 1
  names `shasum -a 256` with no truncation; a script and the recipe would disagree."*
- **Read-back of the remaining consumed returns** (`title`, `category`, dates, the attestation pair,
  `topic_is_list`) — no SKILL-passed fact exists to read against; a **`candidate`** at handoff:
  *"frontmatter facts from disk (`lint-page-facts.py` already parses the block) would let the reduce
  read back category/attestation/date returns."* Not smuggled in — the promise names three clauses.
- **The `summary` read-back** — drafted and refused (disposition 4); the rate it leaves unmeasured
  is stated there.
- **Anchor existence** — Q7 DECLINED; a `[[#heading]]` whose heading is absent is not judged.
- **Inline / scoped mode's orphan and summary checks** — agent reads (`checks.md:13-14`, `:25`);
  the pointer at `checks.md:13` says an inline run *may* run the script. The filings are all
  full-mode; no promise clause names scoped runs.
- **`unmarked_supersession` structuring** — Cycle 14 carry 9's dissent, untouched.
- **The `malformed_frontmatter` retirement** (Cycle 14 carry 5) — ruled at §Acceptance (5)'s
  grading event, not here.
- **Record provenance** (A15-4 direction 2's deferred half) — D3.
- **`report.md:76`'s cap examples** — subset listing, deliberately not widened.
- **`PAGE_SCAN`'s `summary` field** — stays (disposition 4).
- **The four legacy optional args' wrong-type intake** — build-3's candidate, unchanged.

## Verification (unit, at rest — lifecycle step 5)

1. **The script against the oracle** (P-18 — built from the failure's shape): `node
   fixtures/build-4-return-harness.mjs` phase 1 — `lint-page-facts.py` over `fixtures/build-4-wiki/`
   deep-equals `build-4-expected-facts.json`: the fence and span links absent, the frontmatter
   wikilink present, the bare path absent, `l-theanine` **159** (not 161 bytes, not the quoted 161),
   `barbacoa` **160**, `parallel-walk-introduction` 162, `lonely-page` 0. Record the diff (empty)
   in the BUILT `status:`.
2. **`scanFingerprint` MOVES — recorded, not asserted equal:** print it from the shim before and
   after F1 edits 4–5; the two values go in the BUILT `status:` (the one build this cycle that changes
   the scan surface besides build-7; build-2's Verification 2 and build-3's Verification 5 asserted
   their own builds moved nothing — this one does, by design).
3. **E6 re-measured by `package-lint`'s own extractor** — `node -e "$_E6_NODE_EXTRACTOR"` over the
   workflow → `PAGE_SCAN` **≤ 3700**, expected **3265**; record the number. `uv run
   tools/package-lint.py` Groups **A/B/C/E** PASS (D / `--expect-version` is build-7's).
4. **Retirement grep:** `grep -n 'outbound_links\|partialShortfall\|not computed — inbound-derived'
   skills/vlt-setup/assets/workflows/vlt-lint-full.js` → **0**; `grep -rn 'outbound_links' skills/`
   → 0; `grep -rn "the page's own bytes do not carry" skills/` → 0; `grep -c 'linksOf'
   vlt-lint-full.js` ≥ 6 (inbound, orphans, missing, linkSets, clusters ×2, the seed read-back).
5. **The prompt sentence:** `grep -n 'LENGTH is never a frontmatter defect' vlt-lint-full.js` → 1,
   inside `pageScanPrompt` and **not** inside any schema literal (the E6 extractor's per-schema
   lengths prove no description grew — every schema other than `PAGE_SCAN` reads exactly as at
   `7222cd2`: 838 / 1630 / 376).
6. **The harness case table** (§Acceptance (1)–(3)) — all PASS on the shipped workflow; then
   `--workflow <(git show 7222cd2:skills/vlt-setup/assets/workflows/vlt-lint-full.js)` — cases
   (a)/(b)/(c)/(g) **FAIL there** (the planted returns are consumed), (d)/(e)/(f) pass on both
   (controls), recorded as the failability proof.
7. **Prior harnesses after F7:** `node fixtures/build-2-key-harness.mjs` → 15/15; `node
   fixtures/build-3-type-harness.mjs` (all three modes) → green; the shared shim imported by all
   three (`grep -l vlt-lint-full-shim fixtures/*.mjs` → 3).
8. **Cross-file agreement:** `full-scale.md` step 1 names `lint-page-facts.py` and both map names;
   step 3's args list carries both; `checks.md:13` carries the pointer; `report.md` carries
   `scanner_return_rejected:` once as a key and once in §Findings-cache reporting; the workflow's
   arg contract, guard message and refusal `next:` all name both slots (grep each).
9. **Handshake:** nothing moved; `package-lint` Group E is the check of record (E1/E2/E3/E5/E7).
10. **R3 (legal response):** the three classes whose *derivation* changes (`orphans`,
    `missing_targets`, `frontmatter_drift`'s summary clauses) keep their legal responses at
    `checks.md:25`/`:13`/`:14` unchanged; the new cap's response (*nothing owed — the page is
    re-derived next sweep*) is stated once at `full-scale.md` step 5 beside the cache write.
    `R3: satisfied at the single homes; no new finding class.`
11. **R4 (enumeration widening):** the one shipped file added (`scripts/lint-page-facts.py`) is
    inside a tree the manifest walks structurally (`verify-skill-manifest.py:14`); the scratch
    `page-facts.json` lives outside the vault by the step-3 recipe; fixtures live in the
    un-enumerated cycle `fixtures/` dir. `R4: not applicable — declared exclusion, reasoning above.`
12. **Scrub:** no vault-local paths or personal content in any shipped edit or fixture — fixture
    slugs are those already on the public roadmap plus synthetic ones; the two frozen summaries are
    domain prose (a supplement, a braise) carrying nothing personal; placeholder paths in every
    recipe.
13. **Cleanup:** no `.decision-log.md` in the tree; the scratch dir from step 1 removed.

## Release

Not the release build — v0.18.0's bump, `--expect-version 0.18.0` gate and tag ride build-7. **One
release-time note this brief hands to build-7's briefer and `vlt-release`:** the v0.18.0 CHANGELOG's
cold-run statement (build-2 §Release) names build-7's movers; it should also say the scan surface
moved because **the scanner is no longer asked for links and told length is not its verdict** — so
a reader of the CHANGELOG knows the first sweep's orphan and missing-target slots are byte-derived
for the first time.

## Acceptance (live — appended to the roadmap ledger)

**Six checks — five `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 6/15`
(observed: A15-1's three false orphans, A15-3's anchor, A15-4's substitution, A15-5's ten — the
Cycle 14 specimen file names all ten; preserved: two orphan pairs, the anchor, the substitution
in both forms, the two refuted summaries at their real lengths; not preserved: the 2026-08-26
orphan (its inbound page was never named) and the eight genuine `malformed_frontmatter` specimens
(repaired in the sweep that found them — their bytes no longer exist; they reach this brief only as
the *no-parser* constraint)).

**(1) `[ship-verifiable]` — at rest — GATES.** *No orphan or missing-target finding names a page
whose own bytes contradict it.* **Instrument:** `fixtures/build-4-return-harness.mjs` over
`fixtures/build-4-wiki/` — the script run for real, its output deep-equal to the hand-written
oracle `build-4-expected-facts.json`, then the workflow with planted returns at odds with the bytes:
(a) `fantasy-football-evaluation`'s return omits `[[fantasy-platform-read-access]]` (and
`chicken-soup`'s omits `[[katsuo-dashi]]`) → `orphans` = `['lonely-page']` exactly; (b)
`seattle-seahawks`'s return carries `…cornerboxes-2026` → `missing_targets` names no
`cornerboxes` (the bare-path twin is not a link; the `[[ ]]` twin resolves via `crossLayerSlugs`);
(c) `calf-strain`'s return carries `early loading phase (≈ days 3–7)` with the `#` stripped → no
missing target for `calf-strain`; (d) control: `code-fence-page → missing-target-page` **is** reported
and `ghost-page` / `ghost-two` are not; (e) control: `katsuo-dashi#Simmer` resolves to
`katsuo-dashi`; (f) a return with **no** `outbound_links` at all (the post-build scanner) → identical
report; (g) D4: the same cached record for `fantasy-football-evaluation` reused (key unchanged) while
`pageLinks` for it is edited to drop the link → `fantasy-platform-read-access` IS an orphan — the
verdict follows `pageLinks`, never the cache. **Adversary:** property — *the link graph is the page's
bytes*; passing-violating state — the script drops the same link the planted return drops (a
shared bug in the extraction regex), so script output and reduce agree and every case passes with
the bytes still contradicted. **Widened:** the oracle is hand-written from the bytes and the
script's output must equal it byte-for-byte before the reduce cases run — a script defect fails
phase 1; and the whole table is proven failable against `7222cd2` ((a)/(b)/(c)/(g) flip).

**(2) `[ship-verifiable]` — at rest — GATES** *(the at-rest leg of Cycle 14 build-1 (6), D-A)*. *An
over-length or missing-summary finding is true of the page's parsed `summary:` in characters.*
**Instrument:** the same harness: `summaryLengths` from the script (159 / 160 / 162 / 0), planted
returns carrying `summary` paraphrased to 162 chars for `l-theanine` and an unchanged 160 for
`barbacoa` → `frontmatter_drift` carries `parallel-walk-introduction: over-length (162 chars)` and
`lonely-page: summary missing` and **nothing** for `l-theanine` or `barbacoa`; the prompt carries the
length-exclusion sentence (Verification 5). **Recorded, not asserted** (the instrument's stated
bound): a planted `frontmatter_defect: 'unclassified'` with detail *"summary exceeds 160 characters
(161)"* for `l-theanine` still reaches `malformed_frontmatter` — the reduce cannot refuse prose
(D1) and the prompt is the only elimination for that key; leg 3 in check (5) grades it live.
**Adversary:** property — *the measure is the parsed scalar in code points*; passing-violating state
— the script counts bytes, or the quoted value, and the fixture's summaries are ASCII so every
count agrees. **Widened:** both frozen summaries carry em-dashes (159 chars / 161 bytes; 160 / 163),
the oracle pins the character counts, and `barbacoa` sits exactly at 160 — a byte counter, a
quote-inclusive counter and an off-by-one each FAIL phase 1.

**(3) `[ship-verifiable]` — at rest — GATES.** *A scanner-returned value the reduce still consumes
is never persisted after failing its read-back.* **Instrument:** the harness: `chicken-soup` returns
`name_callout_targets: [{target: 'katsuo-dashi', …}]` (on the page) and `seattle-seahawks` returns
`[{target: 'new-england-patriots', …}]` (not among its links) → exactly one `entity-pair:` label
dispatched (`chicken-soup+katsuo-dashi`), `scanner_return_rejected` = `{count: 1, of: 11, slugs:
['seattle-seahawks']}`, the cap names the slug and target, and `cache_records` has **10** entries
with `seattle-seahawks` absent. **Adversary:** property — *rejection and non-persistence are one
act*; passing-violating state — the cap renders and the seed is dropped but `cacheRecords` (a
separate loop) still writes the record, so the fabricated return is served next sweep. **Widened:**
the harness asserts `cache_records.length === scans − count` **and** the rejected slug's absence,
not the cap alone.

**(4) `[ship-verifiable]` — at rest — GATES.** *The scanner is no longer asked for links, nothing
downstream reads a returned link list, the retirements landed whole, and the budget fell.*
**Instrument:** Verification 3–5 + 7–8 — the E6 extractor's `PAGE_SCAN` length (**3265**, ≤ 3700) with
the other three schemas byte-identical (838 / 1630 / 376), the grep manifest at zero, `linksOf` at
≥ 6 consumers, build-2 15/15 and build-3 green after F7, package-lint A/B/C/E PASS. **Adversary:**
property — *no site still consumes a scanner link*; passing-violating state — `outbound_links` is
out of `required` but still in `properties`, and one reduce site (`:683`'s cluster adjacency, say)
still reads `s.outbound_links` — a scanner keeps returning links and one slot keeps trusting them.
**Widened:** the grep is over the token in the **whole workflow** (property + consumers), not the
`required` list, and `linksOf`'s consumer count is asserted.

**(5) `[ship-verifiable]` — bounded to the first full `vlt-lint --full` sweep on `{field-vault}`
after the v0.18.0 upgrade (it happens anyway) — GATES CLOSEOUT (Q9, A18).** **Cycle 14 build-1 (6),
leg 3, appended here quoting Cycle 14's bound text verbatim** (`14-no-enforcement-point/roadmap.md`
§Carried forward item 12 + §ledger build-1 (6)): *"**Bound:** the repair ships in Cycle 15 and is
graded on the **first full `vlt-lint --full` sweep after that release**, against a corpus whose
identity is recorded at grading time; **leg 3 alone is the bound**, legs 1 and 2 are already met
and are not re-litigated."* — leg 3 being *"**every** remaining specimen is adjudicated one by one
against its page as a genuine schema break (the cardinality is recorded, and is **not** the
check)"*, with E4 transferring at **10 flagged / 8 genuine / 2 refuted at 146 pages**. **Instruments,
two (D-A):** the at-rest leg is check (2) (`frontmatter_drift` from bytes, named as the instrument);
the live leg is that sweep's report: every `malformed_frontmatter` entry adjudicated against its
page as genuine — **zero** refuted, and in particular **zero** whose complaint is the summary's
length — **and** every `frontmatter_drift` over-length entry re-measured by the discharger against
the page's parsed scalar in characters (the key the class now renders under); corpus identity
(`files_listed`, sweep date) recorded. **Discharges** `factory/inbox/2026-08-26-164501` (A14-2) —
Stage 5 may move it once this and (1) are green. **Cycle 14 carry 5** (the `malformed_frontmatter`
retirement) is **ruled at this event** (D-F): 0 refuted ⇒ the question is answered here — the check
measures correctly and the retirement is not owed; any refuted entry ⇒ a new filing and the debt
re-binds with its number. Performer: the owner; vault: `{field-vault}` (readable). **Adversary:**
property — *every entry in the class is a genuine break of its page*; passing-violating state —
the sweep flags **zero** `malformed_frontmatter` entries (a vacuous population; or a scanner that
now returns `none` everywhere) and the leg reads as met. **Widened:** the discharger records the
population; on an empty class the live leg is graded on the `frontmatter_drift` half (which cannot
be empty on a 146-page wiki with `lonely`-style pages — its `summary missing` and over-length entries
are each checked against bytes) and the at-rest leg — an empty `malformed_frontmatter` class with
those two green is DISCHARGED with the vacuity recorded, never silently.

**(6) `[field-contingent]`.** *The specimens clear and stay clear, and the read-back rate is a
number.* Event: the **second** full sweep after the v0.18.0 upgrade on `{field-vault}` (the first is
cold by construction and re-rolls every scanner — a specimen clearing there proves nothing about the
mechanism, A12); performer: the owner; vault: `{field-vault}` (readable). Grades: across both sweeps
`false_positives_refused` carries **no** `orphans`, `missing_targets` or summary-length refusal;
`fantasy-platform-read-access` is not an orphan, `calf-strain` and `seattle-seahawks` name no missing
target, `l-theanine`/`barbacoa` no length finding; and `scanner_return_rejected:` renders `N of 146`
on both — N recorded as the measured fabrication rate of the callout return (the rate disposition 4
leaves unmeasured for `summary` is named beside it). Unbounded (nothing schedules a second sweep);
watch register if unfired.
