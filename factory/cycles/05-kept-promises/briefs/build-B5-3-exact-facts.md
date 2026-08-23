---
title: 'Build #B5-3 — exact facts (the lint asks LLM scanners for exactly-computable facts and declares a report slot no check fills; the earliest-shipping proxy-family build writes the extended proxy-check rule)'
status: 'BUILT 2026-07-29 — F1–F8 landed as briefed; verified by a positive 19-page fixture run and a clean negative fixture run (real Workflow invocations, all asserted expectations met), package-lint A/B/C/E PASS, and the whole Step-5 fence parsing under strict yaml.safe_load for the first time (the four-build PARTIAL retired). Deliberate deviations: (1) the Step-5 fence carried TWO additional pre-existing strict-YAML breaks beyond the known :166 line — convention_meta_missing (inner "version: " colon) and contradictions_deferred ("closes when: X | backlog: <item>") — fixed in the same drop-the-colon style, since verification 6''s whole-fence PASS is unreachable otherwise. (2) normalizeTarget additionally strips a wrapping [[ ]] — the negative fixture showed haiku scanners sometimes return the full wikilink despite the "inner text" ask, which manufactured a false missing target + false orphan until the JS normal form absorbed it (the seam principle applied once more: transcription variance is tolerated in computation, never re-asked of the model). (3) title added to PAGE_SCAN required (with a description) — scanners omitted the optional field and titleTokens'' slug fallback then re-manufactured the family signal as "title overlap" on family-stem pages; requiring the verbatim extraction closes the fallback for titled pages. (4) normalizeTarget is homed at args-intake rather than "near the reduce top" — crossLayerSlugs/stubSlugs normalize at intake and need it in scope; still defined exactly once. Exit obligations met: no .decision-log.md in the tree; one commit for the build.'
module_code: 'vlt'
created: '2026-07-29'
derives_from:
  - 'inbox/2026-07-26-184704-lint-full-asks-llms-for-exact-facts.md (A5-8 — the seam + both defect instances (links, summary length), the category_no_match same-class item, the separable near-dup stem defect, and the capture''s two grounding additions: the stub-exclusion gap and the report-shape observation)'
  - 'inbox/2026-07-25-193000-report-slot-with-no-check.md (A5-3 — the sources_vs_prose_mismatches declared-key-no-producer gap and its (a)/(b)/(c) disposition, designated to this brief; settles the known pre-existing strict-YAML fence break A4-2/A4-3/A4-4/A4-5 recorded as PARTIAL)'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): grouping (B5-3 = A5-8 + A5-3, "Exact facts", ships third; as the earliest-shipping proxy-family build it WRITES the extended proxy-check rule the later briefs cite — cross-filing ruling 3, A4-2 pattern); pre-ideation ruling 3 (proxy-check framing: one cross-cutting rule written once, per-filing fixes land where grouping assigns them); questions-designated (A5-3''s (a)/(b)/(c) slot disposition is this brief''s to rule)'
risk: 'low-moderate — one convention RULE change (write-verification 1→2, tier-1 wiki-page checklist gains an item) with a four-consumer re-ack (vlt-ingest, vlt-extract, vlt-research, vlt-lint; Group E is the net); the vlt-lint-full.js changes are finder-side and read-only; the contract edit is single-home prose (deliberately not handshaked)'
---

# Build #B5-3 — exact facts

Goal: close the seam A5-8 names — `vlt-lint-full.js` asks its LLM page scanners for
**exactly-computable facts** (slug-normalized links, char-counted summary verdicts, exact
category↔H2 string matches, date comparisons) and then compares those transcriptions exactly in
the JS reduce, so every finding in that class is only as good as a cheap model's arithmetic.
The re-cut applies one principle throughout: **LLMs extract facts from files verbatim (they are
the only ones who can read — the workflow has no filesystem access); JS computes every derived
value.** The same build settles A5-3: `sources_vs_prose_mismatches` is a declared `fix_now`
report key (`vlt-lint/SKILL.md:166`) that no check in the SKILL's own Step 2 fills — the
current state is the filing's feared "(c) plus silence", and the slot's placeholder is also the
known pre-existing strict-YAML fence break four Arc-4 builds recorded as PARTIAL. And because
B5-3 is the earliest-shipping build of the proxy-check family (pre-ideation ruling 3), it
writes the **extended proxy-check rule** — honest reporting extended from report *slots* to
*checks* — once, in the operating contract, where B5-4 and B5-9 will cite it.

All rejected alternatives in the parent filings are settled — do not re-litigate. A5-8 poses no
open design questions (its "Suggested shape" blocks are owner-steered input, consumed here);
A5-3's (a)/(b)/(c) is ruled in disposition 1 below.

**Re-grounding (2026-07-29, HEAD `2c3740b`): clean, zero grounding corrections.** B5-2 landed
between capture and this brief and touched both target files, so every capture-time line
shifted (workflow ~+7, SKILL ~+4) — but every site HOLDS in substance. Fresh lines are used
throughout below. One sharpening, not a correction: the workflow's PAGE_SCAN has carried a
Gap-B `sources_vs_prose_mismatch` key since build-3, so full-mode-at-scale *does* fill the
slot (LLM-judged); A5-3's gap is precisely that **no check in the SKILL's own Step 2 fills
it** — scoped mode (the default) and small inline full sweeps render the key empty with no
producer. The capture's wording already scoped it that way.

## Brief-time dispositions

1. **A5-3's slot disposition — RULED (b): define the check** (the question designated to this
   brief by the roadmap's §Questions deliberately left to brief time). (a) delete would regress
   the full-mode producer the workflow already carries (Gap-B, protected since build-3) and
   loses the intent record; (c) keep-and-mark is the filing's own "weakest" — the slot keeps
   claiming a check that does not exist. (b)'s cost argument holds at HEAD: A4-1 made the
   wiki-side prose-`## Sources` read mandatory for the candidacy leg (`vlt-lint/SKILL.md:99`,
   and the Step-0 cross-read at `:43`), so the read is no longer additional cost. Tier
   membership, per `write-verification.md:59`'s mechanical membership test: checkable on one
   file → **tier-1**, amortized into the writes. That placement is load-bearing, not cosmetic:
   lint's re-scoping rule (`vlt-lint/SKILL.md:57`) **skips tier-1 re-checks on attested-fresh
   files**, so a lint-only tier-1 check the write ops never run would silently never run on
   exactly the files the vault writes most — the check must enter the write-side checklist's
   single home (`write-verification.md`), which is a convention **rule change**: `version:
   1→2`, re-ack all four consumers in this build (F7).
2. **What gets re-cut and what stays LLM — the seam principle applied honestly, both ways.**
   Re-cut to extract-verbatim/compute-in-JS: link-target normalization (F1), summary presence/
   length (F2), category↔H2 exact match (F3), attestation presence/freshness comparisons (F4) —
   all string ops, counts, and date comparisons on values the scanner can return verbatim.
   Deliberately **staying LLM**: `frontmatter_valid`, `topic_is_list`, `stale_unmarked`,
   contradictions, `thin`, and — pointedly — the sources-vs-prose divergence judgment itself:
   frontmatter `sources:` entries are sometimes human prose rather than paths
   (`vlt-lint/SKILL.md:99` records exactly this), so matching them against a prose `## Sources`
   section is reference-resolution, not string equality. A check is re-cut because its fact is
   exactly computable, never merely because an LLM currently computes it — that discriminator
   is what the extended rule (F8) states.
3. **`sources_count` is deleted, not re-cut.** The PAGE_SCAN key (`vlt-lint-full.js:82`,
   `required` at `:70`, prompt at `:131`) is an LLM-computed count that **nothing consumes** —
   grep confirms it appears nowhere in the reduce or the return, the Step-5 report has no
   source-count key, and the index deliberately carries none. An LLM-computed exact fact that
   nothing reads is this filing's limiting case; the honest fix is removal, not a verbatim
   re-cut of a write-only key.
4. **The near-dup family-stem fix shape: a stem shared by more than 3 pages is a family
   prefix, not a duplicate signal.** The two-segment stem (`vlt-lint-full.js:175`) makes every
   `nfl-2026-*` page share a stem, so within a topical family the secondary signal always fires
   and the two-signal design degenerates to shared-links-only (A5-8's separable third defect,
   4/4 false positives on the live wiki). Mirror the hub exclusion (`:172-173`): count pages
   per stem; a stem carried by **≥4 pages** is disqualified as a secondary signal (a true
   near-duplicate is a pair, and 2–3 shared stems are still legitimate drift suspects —
   `french-press` + `french-press-technique`). Title similarity is untouched.
5. **The stub-exclusion gap: yes, a third exclusion channel.** The capture's unnamed fourth
   gap — all 10 surviving `missing_targets` on the live run were index-registered stubs. A
   `[[link]]` to a slug cataloged under the index's `## Stubs` section (`wiki-index.md:83-90`:
   backtick-wrapped slugs, "linked, not yet written") is a **recorded** gap, not a missing
   target. The SKILL has filesystem access and already reads `{index}`; it parses the stub
   slugs and passes `stubSlugs` (F6). Ownership question in the capture ("unowned") is hereby
   owned: the SKILL supplies it, exactly as it supplies `crossLayerSlugs`.
6. **The extended proxy-check rule's home and text: one paragraph appended to the operating
   contract's *Honest reporting* section** (`vault-operating-contract.md:254`), per cross-filing
   ruling 3 and the A4-2 pattern (that build wrote the section; this one extends it — same
   single home, stated once, cited elsewhere). The contract is deliberately not handshaked
   (single-home + pointers), so no version machinery moves. Text at F8.

## F1 — `vlt-lint-full.js`: link targets extracted verbatim, normalized in JS

**Current state.** PAGE_SCAN asks the scanner for `outbound_links` already "normalized to
slugs" (`vlt-lint-full.js:81`; prompt `:131` "its outbound [[wikilink]] targets (as slugs)"),
and the reduce trusts the transcription exactly: `slugSet` membership and the `crossLayer` set
(`:152`, `:160`) gate `missing_targets` with **no stripping of path prefix, `.md`, `#anchor`,
or `|alias` anywhere** (`:161-162`). The same raw values feed the inbound map (`:153-154`) →
`orphans` (`:156`), the near-dup link sets (`:174`), cluster adjacency (`:221-224`), and —
B5-2's addition, same class — `name_callout_targets[].target` is asked "normalized to a slug"
(`:96`) and consumed raw at seed intake (`:275`). The archived 2026-06-06 filing measured the
consequence: **82% of reported missing targets were false** — valid links wearing aliases,
anchors, or path prefixes. Build-3 shipped only the `crossLayerSlugs` exclusion set — symptom,
not cause (`archive/build-3-lint-full-hardening.md:18,42-43`).

**The change.**
- PAGE_SCAN `outbound_links` description becomes raw extraction: *"the raw `[[wikilink]]`
  inner text of every outbound link on this page, verbatim — including any `|alias`,
  `#anchor`, or path prefix; do not normalize"*. Update the prompt (`:131`) to match.
- Add one normalization function near the reduce top, the single home of the rule:

  ```js
  // Deterministic slug normalization — the seam fix (B5-3): scanners EXTRACT link targets
  // verbatim; every comparison below runs on THIS normal form, computed here, never by a model.
  const normalizeTarget = (t) => String(t || '')
    .split('|')[0].split('#')[0]           // strip |alias, #anchor
    .trim().replace(/\.md$/i, '')          // strip extension
    .split('/').pop()                      // basename (path prefix off)
    .trim().toLowerCase()
  ```
- Apply it **once at intake**, then use normalized lists everywhere: build each scan's
  normalized outbound list right after the scan phase (or at `:152-154` where `slugSet`/
  `inbound` are built), and run `orphans`, `missing_targets`, the near-dup `linkSets`, and
  cluster adjacency off the normalized values. Normalize the *other* side too, defensively:
  `crossLayerSlugs` at intake (`:50`), page slugs into `slugSet`, and `name_callout_targets`
  targets at seed intake (`:275` — grounding addition, EXPANDED: B5-2's field is the same
  seam; one function serves both).
- Empty-after-normalization targets (e.g. a bare `[[#anchor]]`) are dropped, not compared.

**Why.** A5-8 instance 1. The scanner keeps the only job it can uniquely do (read the file);
the exactly-computable normalization becomes computation. The 82% class dies in one place.

**Out of scope at this site.** No change to the exclusion-set *semantics* (crossLayer and the
new stub channel stay exclusion sets); no re-litigation of build-3's design.

## F2 — `vlt-lint-full.js`: summary verdicts computed, `sources_count` deleted

**Current state.** `summary_issue` (`:86`) asks the scanner to char-count and verdict:
"'missing' or 'over-length (N chars)'" — the model does arithmetic the reduce could do.
`sources_count` (`:82`, `required` `:70`, prompt `:131`) is an LLM-computed integer nothing
consumes (disposition 3).

**The change.**
- Replace `summary_issue` in PAGE_SCAN with extraction: `summary: { type: 'string',
  description: 'the frontmatter summary: value verbatim (empty string if the field is
  absent)' }`. Update `required` and the prompt accordingly.
- Compute the verdict in JS at the `frontmatter_drift` assembly (`:316-318`): absent/empty →
  `summary missing`; `length > 160` → `` `over-length (${s.summary.length} chars)` `` (the
  160-char rule per `frontmatter.md` — count characters, which `String.prototype.length`'s
  UTF-16 count matches for the em-dash cases the rule names).
- Delete `sources_count` from PAGE_SCAN (`:82`), `required` (`:70`), and the prompt (`:131`).

**Why.** A5-8 instance 2 — the deterministic remedy the archived filing's §5 recommended and
build-3 deliberately left unshipped; plus disposition 3's write-only key.

## F3 — `vlt-lint-full.js`: category↔H2 match computed from extracted headings

**Current state.** The index pass hands the LLM every page's category value and asks it to
report exact-match violations against the index's H2 set (`INDEX_SCAN.category_violations`
`:109`; prompt `:206-207`) — exact string comparison by model. The scanner already returns
`category` verbatim (`:84`), which is the right half.

**The change.**
- INDEX_SCAN loses `category_violations` and gains extraction: `h2_headings: { type: 'array',
  items: { type: 'string' }, description: "every ## H2 heading in the index, verbatim, in
  order" }` (update `required` `:105`). The index-pass prompt (`:206-207`) drops the
  category-violation ask and instead asks for the H2 list verbatim; it keeps `drift` and
  `malformed` (structural judgment against `wiki-index.md` — genuinely a read-and-judge task).
- JS computes the violations where the return assembles `category_no_match` (`:323`):
  `scans.filter(s => !h2set.has(s.category))`, emitting the same message shape —
  `` `${s.slug}: category '${s.category || '(none)'}' matches no H2` `` — preserving the
  missing-field case ('(none)') the current prompt handles. Exact match means exact: no
  trimming beyond the heading extraction's `## ` prefix removal, no case folding — the strict
  binding (`frontmatter.md`, `wiki-index.md`) is case-sensitive Title Case by design.

**Why.** A5-8's named same-class item (`category_no_match`): the vocabulary is a *controlled*
vocabulary precisely so the check can be mechanical; asking a model to do set membership on it
re-introduces the fuzz the strict binding exists to exclude.

## F4 — `vlt-lint-full.js`: attestation comparisons computed from verbatim dates

**Current state.** `attestation_present` (`:77`) asks the scanner to compute "both
`verified_by` and `verified_at` present", and `attestation_fresh` (`:79`) asks it to compute
the date comparison `verified_at >= last_updated` — while `review_due`'s comparison is already
deterministic JS on a scanner-transcribed date (`:330-332`), the pattern's in-file exemplar.
`verified_by` is returned verbatim (`:78`); `verified_at` is not returned at all.

**The change.** Add `verified_at: { type: 'string', description: 'the frontmatter verified_at
value verbatim (empty if absent)' }` to PAGE_SCAN; drop `attestation_present` and
`attestation_fresh` from the schema and prompt (extraction of the three raw fields —
`verified_by`, `verified_at`, `last_updated` — replaces them); compute in JS at the return
sites: present = both non-empty (`:328`), stale = present && `last_updated` > `verified_at`
(`:329`). ISO `YYYY-MM-DD` strings compare lexicographically — the same property `review_due`
already relies on (`:331`).

**Why.** Grounding addition within A5-8's stated class ("the whole file-local check list is
LLM-asserted... partial exception: `review_due`'s comparison is deterministic"): presence and
date comparisons are exactly computable once the dates are extracted. `review_due` itself is
already correct — extraction (`review_after` verbatim, `:80`) + JS comparison — and is the
shape the rest now matches; **no change to it**.

## F5 — `vlt-lint-full.js`: family stems disqualified as a near-dup secondary signal

**Current state.** `stem = slug.split('-').slice(0, 2).join('-')` (`:175`); `sameStem`
(`:194`) is one of two accepted secondary signals (`:196-198`). Every `nfl-2026-*` page shares
a stem, so within that family the secondary signal always fires and near-dup detection
degenerates to shared-links-only — 4/4 reported pairs false (A5-8's separable third defect; a
build-3 C2 heuristic defect, not the LLM seam — but ruled into this build by the grouping).

**The change.** Per disposition 4, count stem populations before the pair loop and disqualify
family stems:

```js
const stemCounts = new Map()
for (const s of scans) { const k = stem(s.slug); stemCounts.set(k, (stemCounts.get(k) || 0) + 1) }
const familyStem = (k) => (stemCounts.get(k) || 0) >= 4 // a stem shared by 4+ pages is a topical family, not a duplicate signal (B5-3)
```

In the pair loop, `sameStem` becomes `stem(a) === stem(b) && !familyStem(stem(a))`. Title
similarity unchanged. No coverage-cap message — this is a precision fix, not a coverage bound.

**Why.** A true near-duplicate is a pair that drifted together; a stem four-plus pages share is
naming convention, and treating it as a duplication signal manufactures false merge candidates
at exactly the family sizes real vaults grow.

## F6 — the stub exclusion channel (`vlt-lint-full.js` + `vlt-lint/SKILL.md` Step 0)

**Current state.** The reduce excludes only `slugSet` and `crossLayer` (`:160-162`); a
`[[link]]` to an index-registered stub — a slug cataloged under `## Stubs (linked, not yet
written)` per `wiki-index.md:83-90` — always fires `missing_targets`. On the live run, **all
10** surviving missing targets were registered stubs (the capture's unnamed fourth gap). The
SKILL builds the workflow args at Step 0 (`vlt-lint/SKILL.md:41-42`) and already reads
`{index}` first (`:49`).

**The change.**
- `vlt-lint/SKILL.md:41` (Step 0, full-mode item 1): after the `crossLayerSlugs` sentence, add
  the third channel: *"Also parse `{index}`'s `## Stubs` section for its backtick-wrapped
  slugs and pass them as `stubSlugs` — a `[[link]]` to a registered stub is a recorded gap
  (the Stubs section is its record), not a missing target."* Add `stubSlugs` to the invoke
  line at `:42`.
- `vlt-lint-full.js`: document `stubSlugs` in the args block (after `crossLayerSlugs`,
  `:23-25`), intake it beside the others (`:50`, defaulting `[]`, normalized through
  `normalizeTarget` like the rest — F1), and exclude it in the missing-targets gate
  (`:161-162`): `!slugSet.has(l) && !crossLayer.has(l) && !stubs.has(l)`.
- `vlt-lint/SKILL.md:59` (Step 2 tier-1, missing targets): one parenthetical so inline mode
  states the same rule: *"(a target registered under the index's `## Stubs` section is a
  recorded gap, not a missing target)"*.

**Why.** Disposition 5. The stub section exists precisely so this gap is visible without
alarming; a lint that re-alarms on every recorded stub teaches readers to ignore
`missing_targets`.

**Out of scope at this site.** Long-dangling-stub surfacing (`wiki-index.md:90` already
assigns lint *may*-surface latitude) — no new finding key; unchanged.

## F7 — the `sources_vs_prose_mismatches` producer (write-verification@2 + `vlt-lint` Step 2 + the fence fix)

**Current state.** `sources_vs_prose_mismatches` is declared under `fix_now:` in the Step-5
template (`vlt-lint/SKILL.md:166`) and **no check in Step 2 (`:51-107`) fills it** — the full
inventory was walked at capture and re-walked at this brief; nothing in the SKILL compares a
wiki page's frontmatter `sources:` against its prose `## Sources`. The workflow's Gap-B
PAGE_SCAN key (`vlt-lint-full.js:88-89`, return `:320`) fills it in full-mode-at-scale only,
so the default scoped mode renders the key checked-and-clean — "(c) plus silence". The
template line at `:166` is also the known pre-existing strict-YAML fence break (a second
`: ` inside the flow-sequence placeholder), recorded PARTIAL by A4-2 (deviation 1), A4-3
(verification 8), A4-4, and A4-5 (check 13), each deferring it to this slot's disposition.
`write-verification.md` is at `version: 1`, `consumers: [vlt-ingest, vlt-extract,
vlt-research, vlt-lint]` (`:11-12`); its per-kind tier-1 bullets are at `:38-40`.

**The change** (disposition 1 — ruled (b), define the check):
- **`write-verification.md:38`** (tier-1, **Wiki page** bullet) gains the item: *"where the
  page carries a prose `## Sources` section, it agrees with frontmatter `sources:` — every
  entry in one is traceable in the other (frontmatter is the source of truth; a page with no
  prose section is conformant)"*. The polarity is deliberate: no convention requires the prose
  section on wiki pages (`frontmatter.md` wiki schema carries none), so absence is not
  divergence — only carrying both surfaces and disagreeing is.
- **`version: 1` → `version: 2`** (`:11`) — a rule change per the version-handshake standing
  rule — and re-ack **all four consumers in this build**: `vlt-ingest/SKILL.md:4`,
  `vlt-extract/SKILL.md:4`, `vlt-research/SKILL.md:4`, `vlt-lint/SKILL.md:4` each move
  `write-verification@1` → `write-verification@2`. The op skills point at the checklist and
  never restate it (`write-verification.md:22`), so the re-ack is the pin bump plus a
  confirming read that each consumer's body still points rather than restates.
- **`vlt-lint/SKILL.md` Step 2 tier-1** (after the frontmatter-drift bullet, `:60`) gains the
  lint-side check: *"**Sources-vs-prose agreement** — where a wiki page carries a prose
  `## Sources` section, compare it against frontmatter `sources:` (the tier-1 item in
  `{conventions}/write-verification.md`); an entry in one not traceable in the other →
  `sources_vs_prose_mismatches`. A page with no prose section is conformant — frontmatter is
  the source of truth."* This gives the slot a producer in **both** modes: scoped/inline runs
  check it here; full-mode-at-scale keeps the workflow's Gap-B key (which stays LLM-judged per
  disposition 2 — entries are sometimes prose, so matching is reference-resolution).
- **Fix the fence break**: rewrite `:166` to parse as strict YAML by dropping the second
  colon — `sources_vs_prose_mismatches: [<page: frontmatter sources vs prose Sources
  diverge>, ...]`. The whole Step-5 fence is then expected to parse strict for the first time
  (verification 6).

**Why.** A5-3 in full: the slot stops being a promise the SKILL does not keep, the tier-1
placement survives the attested-fresh re-scoping skip (disposition 1's load-bearing point),
and the four-build-old PARTIAL is settled rather than re-recorded.

**Out of scope at this site.** A factory-side report-contract lint (every declared report key
traces to a producer — `tools/package-lint.py` territory): the ideation ships-decides ruling
routes it as ordinary arc work *if taken up*; not taken up here. The transition population —
files attested under checklist v1 never had this check run — is covered by the standing
1-in-5 sample audit (`write-verification.md:64`), not by any retro-sweep.

## F8 — `vault-operating-contract.md`: the extended proxy-check rule

**Current state.** The *Honest reporting — what a check may claim* section
(`vault-operating-contract.md:254-260`) governs what a **count** may claim (denominator +
blind spot; the always-empty slot as limiting case) and carries the derive-first boundary
clause. Nothing yet governs the **check's own signal** — a check may currently report in a
vocabulary its measurement does not earn (A5-8: "links resolve" measured as "a model
transcribed the links"; A5-9, for B5-4: "revised" measured as "contains the template's own
vocabulary"; A5-7, for B5-9: a classifier whose bell has never rung).

**The change.** Append one paragraph to the section, after the single-home line (`:258`),
before the boundary clause (`:260`):

> **The rule extends from report slots to the checks that fill them: a check must be able to
> state what it actually measures, and must report in that vocabulary.** A check whose signal
> is a proxy — a model's transcription of a mechanical fact, a template's own vocabulary read
> back as evidence, a heuristic standing in for the property it names — either narrows its
> claim to what the signal actually establishes, or changes the signal to match the claim.
> Where the fact a check consumes is exactly computable from the record, compute it: a
> transcription of the record is testimony about the record, not the record. A proxy that
> stays is stated as one, beside the finding it produces.

Match the section's voice; this is the only contract edit. The contract is deliberately not
handshaked — no version machinery, no re-ack (single-home + pointers, per the standing rule).

**Why.** Cross-filing ruling 3 assigns the writing to this build (A4-2 pattern). B5-4's and
B5-9's briefs cite this paragraph instead of wording their own versions; this build's own
F1–F4 are its first application.

## Registration

No new skill, no new workflow — no `module-help.csv` row. **The consumer walk is real:**
`write-verification` bumps `1→2` (F7), and all four listed consumers re-ack in this build
(`vlt-ingest`, `vlt-extract`, `vlt-research`, `vlt-lint`). Bipartite consistency is verified
by `package-lint` Group E (verification 4), not by hand. No structure-map change. Not the
release build — no version-string bumps (they ride the arc's release build).

## Out of scope (dispositioned)

- **The report-shape complete-vs-accurate observation** (A5-8's last item: coverage axes can't
  distinguish "compared everything" from "compared correctly") — no mechanical change ruled
  anywhere; the honesty side is exactly what F8's rule and B5-2's `entity_scan_facts` address.
  Observed, not built.
- **`topic_is_list`, `frontmatter_valid`, `stale_unmarked`, contradiction/supersession
  judgments, `thin`, `key_claims`** — stay LLM per disposition 2: validity-against-convention
  and content judgment, not arithmetic. Re-cutting them would trade a read-and-judge task the
  scanner is fit for against raw-frontmatter round-tripping the schema does not need.
- **The workflow's Gap-B `sources_vs_prose_mismatch` key** — stays LLM-judged (disposition 2's
  reference-resolution point); F7 adds the SKILL-side producer, it does not re-cut the
  workflow's.
- **A factory report-contract lint** (`package-lint.py` gains "every declared report key has a
  producer") — routed by ships-decides as ordinary arc work if taken up; not this build.
- **`review_due`** — already the correct shape (extract verbatim, compare in JS); untouched,
  named in F4 as the exemplar.
- **Long-dangling-stub surfacing** — existing `wiki-index.md:90` latitude; no new finding key.
- **Model-tiering, budget guards, chunking, caps** (build-3/B5-2 machinery) — untouched;
  protect-don't-regress per `archive/build-3-lint-full-hardening.md:125`.

## Verification (unit, at rest)

1. **`node --check`** on `skills/vlt-setup/assets/workflows/vlt-lint-full.js` exits 0; the
   parse-on-intake block (`:45-46`) untouched (standing rule: workflows parse `args` as a JSON
   string on intake).
2. **Positive fixture run** (temp vault fixture, real Workflow invocation — the B5-2
   precedent): a small wiki whose pages carry (a) valid links written with `|alias`,
   `#anchor`, a path prefix, and `.md` (must NOT report as missing after F1), (b) one
   genuinely missing target (MUST still report), (c) a link to an index-registered stub (must
   NOT report, F6), (d) an over-length summary and a missing summary (JS verdicts, F2),
   (e) one page whose `category` mismatches the index H2 set and one missing the field (both
   reported via computed `category_no_match`, F3), (f) one stale attestation
   (`last_updated` > `verified_at`) and one unattested page (F4), (g) four pages sharing a
   two-segment stem with ≥3 shared non-hub links (must NOT pair as near-duplicates, F5)
   alongside one two-page same-stem pair that MUST still pair. Assert each expectation on the
   returned object.
3. **Negative fixture run**: a clean fixture returns empty `missing_targets`,
   `frontmatter_drift`, `category_no_match`, `attestation_stale`, `near_duplicates` — and the
   return shape carries every pre-existing top-level key (no key lost in the schema re-cut;
   `sources_count` gone from PAGE_SCAN is invisible here since it never reached the return).
4. **Group E** (`tools/package-lint.py` — E1 handshake-bipartite, E2 structure-map, E3
   stray-pin) passes with `write-verification` at `version: 2` and all four consumers at `@2`.
   Group E is the check of record for the re-ack; a hand-written `grep "write-verification@"`
   is an editing aid only, never the recorded verification.
5. **Packaging lint** — `uv run tools/package-lint.py` A/B/C/E PASS (D / `--expect-version` is
   the release gate, not this build's).
6. **Strict-YAML fence** — the `vlt-lint/SKILL.md` Step-5 fenced block parses whole under
   `yaml.safe_load` (e.g. `uv run python -c ...`) — the first build where whole-fence PASS is
   the expectation, retiring the four-build PARTIAL lineage (A4-2 dev.1, A4-3 v.8, A4-4,
   A4-5 c.13).
7. **Single-home greps**: the extended-rule wording exists only in
   `vault-operating-contract.md` (consumers point, never restate); the sources-vs-prose
   mechanics exist in `write-verification.md:38`'s item with `vlt-lint` Step 2 pointing at it;
   `normalizeTarget` is defined once in the workflow.
8. **Dry-read coherence**: Steps 2→5 of `vlt-lint/SKILL.md` — every `fix_now`/`flag_for_human`
   slot in the Step-5 template is fillable by a check that exists in Step 2 or the workflow
   return (the A5-3 class, checked by reading); `sources_vs_prose_mismatches` now traces to
   the new tier-1 check (scoped/inline) and the Gap-B key (full-at-scale).
9. **Scrub** — no personal/vault-local content in any changed shipped file; fixture content
   uses generic domains (the dog-training/coffee style), never live-vault page names.
10. **No `.decision-log.md`** in the working tree at commit time.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** the exact-facts re-cut reaches the field — on the next ordinary
   vlt-core upgrade, the installed `.claude/workflows/vlt-lint-full.js` carries
   `normalizeTarget`, the `stubSlugs` channel, computed summary/category/attestation verdicts
   (and no `summary_issue`/`category_violations`/`sources_count` in its schemas); the
   installed `vlt-lint/SKILL.md` carries the tier-1 sources-vs-prose check, the `stubSlugs`
   passing at Step 0, and a Step-5 fence that parses as strict YAML whole; the installed
   `write-verification.md` is `version: 2` with all four installed consumers acking `@2`; the
   installed contract carries the extended proxy-check rule. Grep/parse-checkable on the
   installed vault; bounded — the upgrade happens anyway.
2. **[field-contingent]** the deterministic facts behave on real data — on the first full
   (>~30-page) `vlt-lint` after the upgrade: (a) `missing_targets` contains no entry whose
   target actually resolves after normalization (the 82% alias/anchor/prefix class — spot-check
   every reported entry) and no index-registered stub; (b) `near_duplicates` contains no pair
   whose only secondary signal is a stem shared by ≥4 pages; (c) `sources_vs_prose_mismatches`
   has a producer in the run's mode — and on the first *scoped* lint after the upgrade, the
   tier-1 pass fills or honestly empties it (a zero now means "checked, none", which is the
   whole point). Producing vault: **vlt-core** (factory-readable; the owner runs the lint —
   both scoped and full runs occur in ordinary use, so the event is expected but not caused by
   the upgrade).
