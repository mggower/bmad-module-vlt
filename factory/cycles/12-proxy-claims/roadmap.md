---
title: 'Cycle 12 — proxy claims'
status: 'OPEN — **v0.16.0 SHIPPED 2026-08-25** (builds 1-4 @ `216bea2`, tagged `v0.16.0`, pushed to origin). Cycle 12 = four builds, one release, built in order 1 -> 3 -> 2 with build-4 independent: b1 page-scanner corrections @ `f134190`, b3 the PARA posture @ `5585877`, b4 parked-interim guidance @ `0e76901`, b2 the change-keyed findings cache @ `93797b9` (the release build). Two convention rule changes shipped with full re-acks — `extraction.md` 6 -> 7 (four consumers) and `decision-log.md` 3 -> 4 (five consumers); handshake bipartite-clean at the gate (9 conventions, 39 pins). Release gate: `package-lint: A/B/C/E PASS, D PASS — vlt 0.16.0`, exit 0. **Ideated + roundtable-reviewed 2026-08-25** (nine owner-steered rounds, nine voices, six owner rulings, one dispute converged 4/4). **Acceptance PARTIALLY DISCHARGED 2026-08-26** over the `{field-vault}` 0.15.0 → 0.16.0 upgrade (2026-08-25 17:54) and the first post-release full lint (cold, 146/146 pages). **All 16 ship-verifiable checks PASS — the closeout gate is GREEN** (`cycle-closeout` gates on ship-verifiable only). Of the 11 field-contingent checks: **4 DISCHARGED** (b1(4) `missing_targets: []` against the corpus that produced ten-of-ten false flags; b1(6) Scan-pages `prompt_chars` 473,622 → 356,676 at equal page count; b3(8) + b2(6) `governance_rule_changes:` rendering non-empty with all four required facts), **6 STILL-OPEN first-exercise tails** — b3(6) next scheduled `vlt-brief` issue, b3(7) a partner''s first `{resources}`-write legality call, b3(9) a human-ratified `writers:` on a live charter (declaring population is **1** — the vault holds exactly one `charter.md`), b4(5) a real park through `vlt-feedback` + b4(6) coupled to it, b2(5) the **second** full lint where the churn saving is measured (this one was the predicted cold run, A10 confirmed in the field) — and **1 FAILED**: b1(5), attestation complaints still misrouting into `malformed_frontmatter` (5 of 7) and `unmarked_supersessions` (1), hand-folded "same as the 2026-08-24 run", **second consecutive run**; filed `factory/inbox/2026-08-26-075130-attestation-misroute-survives-the-jurisdiction-narrowing.md` for Cycle 13 `inbox-capture`, **not re-carried**. No filing archived — every ledger item is split, so none has all its clauses discharged. **Open owner acts, none gated by the release:** re-grade A46/`P-17` (build-3 shipped the `governance_rule_changes:` key, so its BLOCKED-unreachable grading is stale — flagged by three briefs); hand-deliver build-3''s re-derive notice to `{field-vault}`''s PARA park (A57); run the parked-interim survey (E6, a list not a count, bounded before Cycle 13''s `inbox-capture`). Next: **`cycle-closeout`** — the ship-verifiable gate is green; closeout rules the six open tails forward as standing watches and carries the b1(5) failure to Cycle 13 as its filing.'
module_code: 'vlt'
created: '2026-08-25'
updated: '2026-08-26 (BOUNDED TAILS RULED AT THE BOUND — the six field-contingent tails bounded to "Cycle 13 inbox-capture" landed on Cycle 14''s capture instead; 3 DISCHARGED (b3(6) on substance by owner ruling, b4(5), b4(6)), 1 CLOSED by owner ruling (b3(9) — A33''s notification sufficient, no re-carry), **1 FAILED (b2(5) — the findings cache cannot round-trip; an earlier same-day CARRIED ruling is superseded in place)**, 1 STILL OPEN (b3(7)). Field-contingent ledger 7/11 + 1 FAILED. See §Owner ruling — the six bounded tails at their bound. Earlier: ACCEPTANCE PARTIALLY DISCHARGED — 16/16 ship-verifiable PASS, 4/11 field-contingent discharged, 6 open tails, 1 FAILED + filed)'
derives_from:
  - 'factory/inbox/2026-08-24-173001-lint-page-scanner-counts-code-span-wikilinks.md'
  - 'factory/inbox/2026-08-24-173002-page-scanner-double-reports-missing-attestation.md'
  - 'factory/inbox/2026-08-25-111322-para-location-is-used-as-a-proxy-for-trust.md'
  - 'factory/inbox/2026-08-25-111323-ruling-shipped-by-release-never-resolved-its-filing-issue.md'
  - 'factory/inbox/2026-08-25-111324-parked-interim-exit-condition-silently-invalidated-by-its-ruling.md'
predecessor: 'factory/cycles/11-reachability/roadmap.md (Cycle 11 — CLOSED 2026-08-25, builds 1–9 shipped v0.15.0 @ 93c342f)'
intent: >
  Capture five cases of one shape: a surface carrying a claim on behalf of something else,
  and still carrying it after the thing it stood for moved. Raw page text standing in for
  link structure; frontmatter validity standing in for attestation; PARA location standing
  in for a trust level the `trust:` field already states; open issue state standing in for
  an unanswered question; a written exit condition standing in for a rule that has since
  been rewritten. Cycle 11 asked whether the module's declared surface could be *reached*.
  This cycle asks a narrower question about the same surfaces: when they are reached, is
  what they say still true — and who is entitled to say it.
---

# Cycle 12 — proxy claims

## The through-line

A **proxy** is a cheap stand-in for an expensive fact. Every one in this cycle was correct
when it was written, and each stayed in place after the fact it stood for became directly
available.

- **A12-1** — the full-lint page scanner reads *raw page text* as a proxy for *link
  structure*. A `[[wikilink]]` inside a backtick code span is documentation, not a link;
  the scanner cannot tell, so a page teaching DQL syntax reports ten broken links it does
  not have. Ten of ten flags false in one run.
- **A12-2** — the same scanner reads *frontmatter validity* as a proxy for *attestation*.
  A page missing `verified_by:`/`verified_at:` is one fact with one home (the attestation
  surface), and it surfaced under three classes at once, inflating counts the factory
  reads as signal.
- **A12-3** — PARA *location* is a proxy for a *trust level*. It was the only protection
  available when the honest fields had nothing enforcing them. Cycle 11's own build-6
  shipped that enforcement across the whole PARA population, and the proxy survived beside
  it. Fifth appearance of one cause (`ST-2`).
- **A12-4** — an *open issue* is a proxy for *an unanswered question*. Issue #11's question
  was answered by v0.15.0's build-2; its issue is open with zero comments, because the
  close is bound to filing **archival**, and archival is bound to a field-contingent watch
  that may never fire.
- **A12-5** — a written *exit condition* is a proxy for *a rule in force*. `{field-vault}`
  recorded a precise, mechanical unwind that was true under the reading of the blocker it
  held at parking time. The ruling shipped under a different reading, and the record did
  not merely go unmet — it went **wrong**, silently, still reading as pre-authorized.

All five are cases where **an answer exists and the surface that stood in for it never
learned** — a governance rule (A12-3), a rail state (A12-4), a vault-local record (A12-5),
and two model-made judgments where the deterministic answer was already available (A12-1,
A12-2). A12-3 names the process cause outright, and that cause already has a channel:
platform **P-15** (the retirement rail) shipped 2026-08-25 and is awaiting exactly this
cycle's roundtable to self-accept. A12-3 is its first real customer.

**The study register holds three of the five causes already, and that is the story of this
cycle's capture.** *(This paragraph replaces a first-pass reading that treated A12-1 and
A12-2 as isolated prompt bugs; see the capture narrative's item 16 for how that was caught.)*

- **`ST-3`** (governance has no addressable projection) names the *exact-facts-from-LLMs
  residue* as a contributing factor, in the very asset A12-1 and A12-2 are about. Both
  filings are that factor producing field defects — and both are **`B5-3(2)`'s watch firing
  after five cycles**, the *"exact facts on the first real full + scoped lints"* clause
  carried since Arc 5 and re-listed into this cycle as the opaque token *"B5-3..B5-9"*. The
  first real full lints have now run, and these two filings are what they produced.
- **`ST-2`** (location as proxy for trust) is A12-3's whole derivation, and its **RC2** —
  *the loop can process defects but not obsolescence* — is the reason A12-3 is a fifth
  appearance rather than a first.
- **`ST-1`** (the PARA write-path is a single door of the wrong shape) is the half A12-3's
  filing does not carry: **RC-B**, permission fused to provenance, and its **C4** provenance
  segregation. `ST-1` says outright that RC-A and RC-B are not retired.

So the cycle has a second through-line under the first, and it is a sequencing one: **two of
the five filings are the discharge evidence for a watch nobody connected to them, and the
cheap fix for those two runs directly against a cost cause a third study already priced.**
Which makes this a cycle whose *ideation order* matters more than usual — the joints are
between the new captures and the carry-ins, not among the new captures.

## Carried in from Cycle 11 (re-listed from the authoritative closeout hand-off)

Re-listed, not re-graded — the authority is `factory/cycles/11-reachability/roadmap.md`'s
frontmatter `status:` ("Still open elsewhere"). Ideation rules whether any becomes a build
here.

1. **Six released field-tail standing watches** — b2(2) a partner resolves a
   `resources/`-write legality question from the bundle without escalating *(note: A12-3
   below may make this watch's premise obsolete — see its residual scope)*; b3(3) the
   decision log's new routes used live; b4(2) the false-fire window at run 1 of 2; b5(2) a
   live council lens-shortfall surfacing end-to-end; b6(3) the resolution half of the
   caught draft-night instance; b9(3) the first live `frontmatter_key_count` declaration
   (B10-4(4) parts 2–3 ride it).
2. **Build-8's `overlay_rules_review` tail** — A11-5's live exercise; unbounded by
   construction (a fault-shaped event nothing schedules).
3. **A11-2 + E4 deferred here** — spike **S-3** harvested, verdict **reshape**; the
   preserved constraint stands: *the trigger stays real, not prose*.
4. **A11-11 directions 1–4 deferred here** — their ideation consumes the direction-0 live
   numbers now in hand (`cost_accounting` persisted; `churn_since_last_full` 5 of 146,
   instrument `python3 os.stat`). **Entangled with A12-1 + A12-2** (`ST-3` is the common
   home): the cheap fix for those two lengthens the ×147 page-scan prompt these directions
   exist to shorten. Rule them in one sitting.
5. **The E8 inherited registers, unchanged** — C6-c, B5-3..B5-9, the pre-Arc-5 and Arc-7
   registers, Arc 9 item-6 watches, Cycle-10 released watches (B10-7(4), B10-8(4),
   B10-8(5), B10-9(3) remainder), and the DECLINE+WATCH pair (confidentiality-as-container-
   attribute, with A16's noted growth).

   **`B5-3(2)` is called out of that register by name, because its triggering event has
   happened.** The clause is *"exact facts on the first real full + scoped lints"* (filing
   `2026-07-26-184704`, held active since Arc 5 —
   `factory/cycles/06-factory-honest-surface/roadmap.md:584`). The first real full lints have
   now run twice, and **A12-1 and A12-2 are their result.** A released watch whose event has
   finally fired is owed a grading rather than another silent re-carry; ideation should rule
   whether B5-3(2) discharges against these two filings, or whether it survives until the
   *reading* moves out of the model (`ST-3`'s cause fix, A11-11 direction 4's territory).
   This is the fifth cycle the clause has been carried as a bare token in a list.

**Platform channel, stated because two items self-accept on this cycle and ideation must
not double-book them as builds:** P-15 (retirement rail) discharges on *this cycle's
roundtable running its obsolescence beat* plus *this cycle's briefs carrying the retirement
clause answered*. P-14 (study register) discharges on a capture citing an `ST-N` — **A12-3
does this**, and this run appends itself to `ST-2`'s `cited_by:`. P-10 (roadmap → tracker
sync) is BUILT-awaiting on this cycle's milestone + build issues being generated rather
than typed, and **A12-4 is plausibly its territory** — ideation rules that.

## Capture — 5 filings (grounded against module source 2026-08-25, at v0.15.0/HEAD)

### A12-1. The full-lint page scanner counts wikilinks inside code spans (2026-08-24) — `2026-08-24-173001-lint-page-scanner-counts-code-span-wikilinks.md`

**PROVENANCE CORRECTION (site).** The filing directs the fix at "the page-scan prompt/logic
of `skills/vlt-lint/assets` (the full-mode fan-out)". **`skills/vlt-lint/assets/` does not
exist** — `skills/vlt-lint/` holds `SKILL.md` and `references/` only. The fan-out workflow
is a `vlt-setup` shipped asset: **`skills/vlt-setup/assets/workflows/vlt-lint-full.js`**.
This matters for briefing, because the file is also the site of A12-2, of A11-11's
`cost_accounting` instrumentation, and of the B10-2(5) widening whose residue this filing
is — four live concerns in one 560-line asset.

**CONFIRMED — the extractor has no shape predicate and no code-span exclusion.** Two sites,
both saying "every outbound link" and neither defining one:

- `vlt-lint-full.js:143` — the `PAGE_SCAN` schema: `outbound_links` is *"raw `[[wikilink]]`
  inner text of every outbound link, verbatim; do not normalize"*.
- `vlt-lint-full.js:202` — the scanner prompt's return clause repeats it verbatim, adding
  *"including any |alias, #anchor, or path prefix; do not normalize"*.

Neither excludes inline backticks or fenced blocks, and neither requires an extracted
target to be wikilink-shaped. The prompt does carry a comparable exclusion elsewhere — the
callout gate at `:201` is narrowed by form (*"A callout is only the Obsidian `> [!type]`
blockquote form … a bullet, heading, or plain prose is NOT a marker"*) — so **the pattern
for stating a form restriction already exists in this prompt**; link extraction simply
never got one.

**CONFIRMED — the false positives reach the report unfiltered.** `vlt-lint-full.js:319-320`
derives `missing_targets` by set difference against filesystem truth, cross-layer slugs and
recorded stubs:

```js
for (const s of scans) for (const l of s.outbound_links)
  if (!pageSlugSet.has(l) && !crossLayer.has(l) && !stubs.has(l)) missing_targets.push(...)
```

Every suppression here is about **whether a target resolves**. None is about **whether the
source text was a link at all**. A DQL example's `[[food]]` resolves to nothing anywhere,
so it is structurally guaranteed to fire.

**GAP CONFIRMED — two distinct extraction defects, not one.** The filing separates them and
grounding keeps them separate:

1. **Code-span inclusion** — 9 of 10 flags. Fixture class: obsidian-dataview
   (`FROM [[note]]`, `FROM outgoing([[note]])`, the `[[food]]`/`[[exercise]]`/`[[link]]`/
   `[[assignment math]]`/`[[math]]`/`[[class]]` table-example rows) and obsidian-bases
   (`![[File.base]]`, `![[File.base#View]]`).
2. **Non-wikilink text matched as a link** — the 10th flag
   (`nfl-defensive-scheme-evolution` → `2026-02-14-macdonald-defense`), a bare source
   filename in a sources list. No `[[ ]]` present at all. A code-span exclusion alone does
   **not** fix this one; the shape predicate does.

**Residual scope.** Two clauses at `:143` and `:202` (schema description + prompt), stating
(a) targets inside inline-code or fenced blocks are not outbound links, and (b) an outbound
link is `[[ ]]`-delimited text and nothing else. No convention changes, **no version bump,
no re-ack** — the extraction contract lives in the workflow asset, not in a governance
convention. The filing's own fixture is the right acceptance instrument: *a page carrying a
fenced DQL example plus a bare filename in a sources list must contribute zero
missing-target flags*, runnable at rest on the build-5/build-8 factory-side harness
precedent.

**Relationship to the retired debt.** This is the residual of the class B10-2(5)/B10-12(6)
retired on its bound: the *population predicate* (`crossLayerSlugs`) is field-proven at
zero false positives, and the *per-page extractor* is what still lies. Same failure shape —
a check whose whole raw output was false — one layer up. Grade this a fresh defect, not a
reopening: the retired debt's own measurement was correct.

**Study check (P-14) — rests on `ST-3` (`factory/studies/ST-3-governance-has-no-addressable-projection.md`). *(Corrected 2026-08-25, same session — see the capture narrative's item 16.)*** This
capture first graded the cause *"local to one asset's prompt, no entry earned."* That is
wrong, and reading `ST-3` whole is what showed it. `ST-3`'s **Contributing factors** name
this exact seam:

> *"~9 of 16 `PAGE_SCAN` fields are pure deterministic extraction. B5-3 already moved
> **comparison** into JS ('the scanner reads, JS does the arithmetic') — but **reading** is
> still done by a model … The open filing
> `2026-07-26-184704-lint-full-asks-llms-for-exact-facts.md` is the same seam seen from the
> correctness side rather than the cost side."*

`outbound_links` is pure deterministic extraction — a regex over markdown with code spans
excluded — and it is being asked of a model with no shape predicate. **A12-1 is that
contributing factor producing a field defect.**

**This is `B5-3(2)`'s watch firing, after five cycles.** The chain, traced this run:
filing `2026-07-26-184704` → captured **A4-13** (Arc 4,
`factory/cycles/04-honest-surface/roadmap.md:1263`) → built as **B5-3** (Arc 5, brief
`build-B5-3-exact-facts.md`) → its clause **(2)** — *"exact facts on the first real full +
scoped lints"* — **held active ever since**
(`factory/cycles/06-factory-honest-surface/roadmap.md:584`), and re-carried into this cycle
inside the E8 register as the bare token *"B5-3..B5-9"*. The first real full lint has now
run twice, and **it produced A12-1 and A12-2.** Ideation should read these two filings as
that watch's discharge evidence, not as unrelated fresh bugs — a released watch whose
triggering event has finally happened is owed a grading.

**Residual scope — reframed by the study, and it is no longer obviously cheap.** Two reads
now sit on the table and ideation must rule between them:

- **Symptom fix (what this capture first proposed).** Add the two clauses at `:143`/`:202`.
  Cheap, fast, and it is what B5-3 did for *comparison* — leave the reading with the model
  and tell it more carefully what to read.
- **Cause fix (`ST-3` cause (a) territory).** Stop asking a model for a deterministic fact:
  extract `outbound_links` in JS from page text the workflow already has a path to. This is
  the same move `ST-3` says *"retires the 38.7 KB read"*, and Cycle 11's A11-11 capture
  already recorded the adjacency in writing
  (`factory/cycles/11-reachability/roadmap.md:392`).

**JOINT — and it is a real one, for the roundtable, not a note.** The symptom fix **adds
instruction bytes to `pageScanPrompt`, which runs ×147 agents**. `ST-3` prices that phase at
58,531 bytes per agent and names *ratcheted caution* as a root contributing factor:
*"every honesty repair correctly added coverage guards; **none of them ever removed work**,
so the pipeline has monotonically accreted cost."* A prompt-only fix to A12-1 + A12-2 is
another turn of exactly that ratchet — **and Cycle 11's build-8 just shipped the
instrumentation that would measure it.** Fixing a false-positive defect by making the run
more expensive, in the same cycle that is ruling on A11-11 directions 1–4 (deferred here to
cut that cost), is a decision that must be made once, deliberately, with both filings and
all four directions on the table together. It must not be made twice, cheaply, in two
separate briefs.

### A12-2. Page scanners double-report missing attestation under two other classes (2026-08-24) — `2026-08-24-173002-page-scanner-double-reports-missing-attestation.md`

**PROVENANCE CORRECTION (site).** Same as A12-1 — the site is
`skills/vlt-setup/assets/workflows/vlt-lint-full.js`, not `skills/vlt-lint/assets`.

**CONFIRMED — the terminal home exists and is JS-computed.** The attestation surface is
real and correct: `vlt-lint-full.js:482` defines `attested = (s) => !!(s.verified_by &&
s.verified_at)`, and `:483-491` build the `attestation_census` as pure arithmetic over
values the scanners already return (`pages_total` / `fresh` / `stale` /
`unattested_pre_adoption`, the three buckets partitioning `pages_total`). The per-page
counterpart `unattested_write` is a declared report slot at
`skills/vlt-lint/references/report.md:32`, with its scope rule and pre-adoption
informationality posture single-homed at `checks.md:16`.

**CONFIRMED — both leak paths are agent-judged, with nothing telling the agent where the
boundary is.**

- **`malformed_frontmatter`** — `vlt-lint-full.js:543` filters on
  `s.frontmatter_valid === false`. That boolean is **the scanner agent's judgment**
  (`PAGE_SCAN:144`, *"frontmatter present and well-formed"*), made against the merged
  `frontmatter` convention. And the convention genuinely defines `verified_by:`
  (`frontmatter.md:78`, `:82`) — so an agent asked "is this frontmatter well-formed?"
  reading a block with no `verified_by:` has every reason to answer *no*. **The 18 entries
  were the prompt working as written.**
- **`unmarked_supersessions`** — `vlt-lint-full.js:510` collects the agent's free-text
  `unmarked_supersession` array (`PAGE_SCAN:153`), whose description is broad enough to
  absorb an attestation complaint: *"silently-updated/conflicting claims lacking a
  `[!superseded]`/`[!stale]` callout, or consensus claims lacking citations"*. The 2
  entries (`acotar-world-building`, `katsuo-dashi`) are misroutes into that breadth.

**GAP CONFIRMED — and the census is the reason it matters.** `attestation_census` is
denominated arithmetic over `scans.length`. The census read *145 pages: 97 fresh / 6 stale
/ 42 unattested pre-adoption* **only because the executor folded all 20 duplicates back by
hand**. A less careful run reports the same gap three times, and the factory reads inflated
counts as signal — the honest-surface failure the module files against, in the instrument
the factory uses to measure honesty.

**Residual scope.** A negative clause in the scanner prompt (`:201-202`) plus tightened
schema descriptions at `:144` and `:153`: absent `verified_by:`/`verified_at:` is **not** a
frontmatter-validity defect and **never** an unmarked supersession — it is reported through
the attestation values already extracted (`verified_by`, `verified_at`), which the reduce
turns into the census and the `unattested_write` slot. Note for ideation: the fix is
*subtractive on two classes* and adds no new extraction, so it is cheap — but it edits the
same prompt block as A12-1. *(First written here as "an ordering fact for briefing, not a
joint." The study check below revises that: it **is** a joint — see A12-1's JOINT paragraph.)*

**Open question carried forward, unresolved here.** `checks.md:16` states the attestation
scope rule and `frontmatter.md:82` states the field's home; neither says explicitly that
attestation is **out of** frontmatter-validity jurisdiction. Whether the fix is prompt-only
or also needs a one-line boundary statement in `frontmatter.md` (**which would be a rule
change: version bump + re-ack every consumer**) is ideation's ruling, not capture's. The
cheap read is prompt-only; the durable read is that an agent will keep re-deriving the
wrong answer from a convention that does not state the boundary.

**Study check (P-14) — rests on `ST-3`, same as A12-1. *(Corrected 2026-08-25, same session — see the capture narrative's item 16.)*** Also
first graded *"cause local to this prompt's class boundaries."* Also wrong, and for a
sharper reason than A12-1: **the deterministic answer is already computed, ten lines away.**
`vlt-lint-full.js:482` defines `attested = (s) => !!(s.verified_by && s.verified_at)` in JS,
over two fields the scanner extracts verbatim. Attestation is therefore **already** on the
correct side of B5-3's *"the scanner reads, JS does the arithmetic"* line — and the defect
is that a *second*, model-made judgment (`frontmatter_valid`) is allowed to answer the same
question in parallel and disagree with it. That is `ST-3`'s exact-facts residue in its
purest observable form: not a fact the model should never be asked for, but a fact **the
model is asked for twice — once deterministically, once not** — with no rule saying which
wins.

**Same watch, same joint.** A12-2 is `B5-3(2)`'s discharge evidence alongside A12-1 (chain
traced in A12-1's study check: filing `184704` → A4-13 → B5-3 → clause (2), held five
cycles), and its symptom fix edits the same `pageScanPrompt` block, so it carries the same
×147 cost-ratchet joint. **Brief these two together, or rule explicitly why not.**
Grounding's own read, offered because it cuts against treating them as a pair: A12-2's
*cause* fix is materially cheaper than A12-1's, because the JS-side answer already exists
and the change is **subtractive** — removing two classes' jurisdiction rather than adding an
extraction. So the two filings may deserve the same brief but **not** the same disposition.

### A12-3. PARA uses location as a proxy for trust (2026-08-25) — `2026-08-25-111322-para-location-is-used-as-a-proxy-for-trust.md`

**Rests on `ST-2` (`factory/studies/ST-2-location-as-proxy-for-trust.md`) — and on `ST-1`
(`factory/studies/ST-1-para-write-path-single-door.md`), which this capture first omitted.**
The derivation, the rejected packages and the settled owner rulings live in `ST-2`; read it
whole before briefing. This capture states the grounding and the residual scope only, and
appends itself to both studies' `cited_by:`. *(This is also P-14's discharging event: a
capture citing an `ST-N` instead of re-deriving it — though see the capture narrative's item
16 for how nearly that discharge was a false pass.)*

**Why `ST-1` is not optional here.** `ST-2`'s frontmatter and `ST-1`'s closing section both
say to read them together, and `ST-1` states plainly: **"RC-A and RC-B are not retired."**
`ST-2` sharpens RC-A (location as a proxy for trust) and adds the process cause; it
supersedes nothing. Laid against `ST-1`'s recommended package, the filing's six steps are
**four of five components re-derived and one missing**:

| `ST-1` component | A12-3's step | Status |
|---|---|---|
| **C1** — re-draw Layer 3 by authorship, not location | step 2 (entry condition = honest, attested frontmatter) | re-derived |
| **C2** — per-zone posture as a declared parameter | step 5 (`writers:` per container + module-fixed `{wiki}` floor) | re-derived, and sharper (`ST-1` had no container model to hang it on; B10-10 shipped one since) |
| **C3** — a second verb owning the non-wiki-derived artifact | steps 3 + 4 (demote extraction to a disposition; give `vlt-query` a PARA destination) | re-derived from the other side — `ST-1` adds a verb, A12-3 stops one verb owning the turnstile |
| **C5** — enforcement in the same build as the rule | step 6 (`vlt-lint` authorization check) + the *rule ahead of mechanism* hazard | re-derived; since shipped as the **B9-2 standing rule**, so it is now a rule to be measured against, not a preference |
| **C4** — **provenance segregation**: `sources:` stays wiki-only forever, a new `grounding:` field carries external evidence | **— none —** | **NOT CARRIED** |

**The un-carried half, stated as ideation's question.** `ST-1`'s **RC-B** is *"exactly one
PARA verb exists, fusing write permission to wiki provenance,"* and its named leverage point
is **the fusion**, not the strictness. A12-3 attacks RC-A (the location proxy) and is silent
on the provenance half. Two consequences a brief must not inherit unexamined:

1. **A12-3 may defuse RC-B without addressing it.** `ST-1`'s R1 erosion loop is driven by
   agents falsifying `sources:` *as the price of entry* — 57 files in `app-vault`, the
   firewall *"already breached, silently."* If honest `author: agent` / `trust: raw` writes
   become legal, that entry price disappears and the falsification pressure drops. That is a
   genuine and under-claimed argument **for** A12-3, and it belongs in the brief's rationale.
2. **But nothing then says what `sources:` means on the new artifacts.** Step 4 routes
   `vlt-query` output into PARA, and that output's `sources:` lists wiki pages *and*
   `{research}` notes (`vlt-query/SKILL.md:46`). `ST-1`'s C4 says `sources:` stays wiki-only
   **forever** and external evidence goes in a separate `grounding:` field. A12-3 opens a
   door without ruling what provenance field the things coming through it carry. **Ideation
   owes an explicit ruling: adopt C4, or state why the firewall does not need it once entry
   no longer requires the disguise.** Capture's read is that this is the single largest
   unexamined risk in the six-step package, and it is invisible unless `ST-1` is read.

**`ST-1`'s two reverse-brainstormed hard constraints, carried verbatim** (they were derived
by asking *"how would we guarantee this fails?"*, which makes them the closest thing this
change has to a pre-mortem): **enforcement ships in the same build as the rule**, and
**`extraction.md`'s invariants are not touched** — *"relaxing `sources:` to solve a
permission problem trades the invariant for the convenience."* The second is a live guard on
step 2, which does edit `extraction.md`: bumping `:60`'s false human-initiation premise is a
correction of a *justification*, not a relaxation of an *invariant*, and the brief should say
so in those words so the constraint is honoured rather than tripped.

**CONFIRMED — the contradiction is exactly where the filing puts it, line for line.**

- `vault-operating-contract.md:66` (Layer 3) declares the boundary as **authorship-honesty**
  — *"everything here carries an honest `author:` … and partner-touched content reaches it
  through exactly **two named surfaces**"* — extraction and container maintenance.
- `vault-operating-contract.md:68` (**The hard rule**) implements it as a **location
  prohibition** — *"partners never create, rewrite, or delete human-curated PARA content
  outside those two surfaces."*
- `vault-rule-card.md:26` restates it in the act-blocking card: *"partners reach it through
  exactly two named surfaces … **never a third**."*

Both named surfaces presuppose prior human or wiki passage: extraction is a *graduation*
surface (`extraction.md:60` — artifacts enter at `author: hybrid`, `trust: reviewed`) and
container maintenance is an *annotation* surface (`extraction.md:45` — *"operational
records, never artifacts"*). **There is no authorship surface.** An honestly
`author: agent` / `trust: raw` standalone document has no legal PARA placement, and the
only way to place one is to falsify the two fields the layer's stated boundary is drawn on.

**CONFIRMED — the `extraction.md:60` premise is false in shipped code.** The clause
justifies the `trust: reviewed` entry level with *"the act of extraction is a
human-initiated curation step."* Grounded against the ops that perform it: `extraction.md:47`
names **`vlt-track`** as the one module-shipped op sanctioned for personalized extraction,
and `vlt-track` runs on a longitudinal loop; `vlt-query/SKILL.md:10` states it *"runs
interactively or headless."* The human-initiation fiction does not hold today, and the
trust level the location rule protects is being set by a premise the module has already
contradicted elsewhere in its own shipped surface.

**CONFIRMED — the enforcement that makes the proxy redundant has shipped.**
`skills/vlt-lint/references/checks.md:16-18` is unambiguous: `para_missing_attestation`
(explicitly *"the **authorship-honesty net** — it catches unstamped, unattested
artifact-shaped agent writes reaching the layer outside the sanctioned surfaces"*),
`para_status_unknown`, `para_type_unknown` and `para_author_unknown` all judge the same
population — *"files under `{projects}`, `{areas}`, and `{resources}` — **with the `{wiki}`
subtree under `{resources}` excluded by name, never by location**"*. That is Cycle 11's
build-6, and it is precisely the mechanism the filing says obsoletes the prohibition:
**honest fields now have enforcement behind them**, which is the one condition under which
the location proxy was ever necessary.

**CONFIRMED — the human's curation monopoly is untouched by opening the layer.**
`extraction.md:53-60` (the trust ladder) reserves `reviewed`, `verified` and `canonical` to
the **Human**; only `raw` is agent-set. A surface admitting honest `author: agent` /
`trust: raw` documents therefore concedes nothing above `raw`. The MOC rule
(`vault-operating-contract.md:190`) independently keeps `canonical` linkage human-only.

**CONFIRMED — the counter-example is inside the module.** `{wiki}` lives in human-browsable
space (`vault-operating-contract.md:64` — *"a human-browsable address precisely so humans
can read it"*), is agent-written, and is protected by **authoring discipline** — single
writer (*"a Librarian-only zone: the Librarian is its only writer"*), a convention set,
attestation, an index — not by prohibition. It produces no friction. The module already
holds the working pattern it declines to generalize.

**CONFIRMED — the `≥2 wiki pages` gate is prose-only, and there is a third site the filing
missed.** Grepped across the whole governance bundle and every `vlt-lint` check reference:
the gate appears in **no convention and no check**. Its three shipped homes are all skill
prose — `vlt-extract/SKILL.md:38` (*"**Hard gate:** extraction requires **at least 2
contributing wiki pages**"*), `vlt-extract/SKILL.md:118` (*"A thin wiki is a stop, not a
caveat"* — **not named in the filing**), and `vlt-agent-creative/SKILL.md:37` (*"The hard
gate (≥2 contributing wiki pages) is a feature"*). The filing's *"no handshake cost"* claim
is **correct** — confirmed, with the site count corrected from two to three.

**CONFIRMED — the restatement sites, all four, verbatim.** `vlt-agent-creative/SKILL.md:14`
(*"never open a third surface"*), `vlt-extract/SKILL.md:13`, `vlt-review-council/SKILL.md:51`
(*"Write to `{wiki}`, PARA, `sources/`, or the human zones"* — listed as a prohibition),
`vlt-upgrade/SKILL.md:159` (*"Touch the human zones or PARA"*). The filing's sharpest
acceptance test rests on these, and it is right to: **a contract change that leaves four
skill restatements standing will not take.** `vault-rule-card.md:26` is a fifth site and
the most load-bearing of all, since it is the act-blocking card every partner loads first
(`vault-operating-contract.md:192`).

**PROVENANCE SHARPENING — `writers:` is new schema, not shipped.** Fix step 5 reads *"a
`writers:` declaration on the container `charter.md` (human-gated, already shipped by
B10-10)"*. Grounding splits that: the **container model and charter human-gating** did ship
(B10-10 — `vault-operating-contract.md:70`, *"**`charter.md`** (the stable frame … human-gated
as above)"*). **`writers:` itself does not exist anywhere in `skills/`** — zero hits. It
would be a new key in `extraction.md`'s *PARA containers* schema, i.e. a **rule change**:
`extraction.md` 6 → 7 and re-ack all three consumers (`consumers: [vlt-extract, vlt-lint,
vlt-track]`, `extraction.md:12`). The filing's own step 2 already budgets that bump, so the
cost is shared, not doubled — but the brief must not inherit "already shipped" for the key.

**CONFIRMED — `_vault/` is human-only and was omitted from the owner's list.**
`vault-operating-contract.md:78` lists `_vault/` alongside `new/` and `daily/` as human-only.
The owner ruling of 2026-08-25 names only `daily/`, `new/`, `sources/`. The filing flags
this itself and leaves the disposition open — carried forward below, unresolved.

**CONFIRMED — the process cause, and it already has a channel.** The filing's *"the
evolution loop has no way to process obsolescence"* diagnosis is `ST-2`'s Root Cause 2, and
it was filed to the platform channel as **P-15 — the retirement rail**, which is **BUILT
2026-08-25** (`factory/platform/roadmap.md:105`). Its three sites shipped:
`roadmap-roundtable` gained the reverse beat (*mechanisms that have obsoleted their rules*),
`factory/inbox/README.md:21-43` gained the **`supersession`** filing class, and `build-brief`
gained the required retirement clause. **P-15 self-accepts on this cycle's roundtable and
briefs.** Two consequences for ideation, both concrete:

1. **A12-3 is a supersession, not a clause repair.** The filing says so and grounding
   agrees. `factory/inbox/README.md:43` draws the line capture must honour: *"Here
   supersession is the filing's **claim**, not its verdict"* — the retirement is what gets
   captured; whether the rule retires, narrows or survives is ideation's ruling.
2. **The roundtable's obsolescence beat has its first real case.** P-15's done-when asks
   for the beat exercised with a finding *or* an explicit nothing-found; this cycle hands
   it a finding it did not have to hunt for.

**GAP CONFIRMED — residual scope, per the filing's six steps, graded.** Grounding did not
change the shape of any step; it sharpened sites and costs:

| # | Step | Grounded cost |
|---|---|---|
| 1 | Retire the `≥2 wiki pages` gate | `vlt-extract:38`, `vlt-extract:118`, `vlt-agent-creative:37`. **No handshake** — confirmed prose-only. |
| 2 | PARA entry condition = honest, attested frontmatter | `vault-operating-contract.md:66`/`:68`, `vault-rule-card.md:26`; correct `extraction.md:60`; `extraction.md` 6 → 7 + re-ack 3 consumers. |
| 3 | Demote extraction to a disposition | `vlt-extract`, `vlt-agent-creative:37`. Retirement of the skill was considered and **rejected in the filing** — bottleneck is the clause, not the skill. |
| 4 | Give `vlt-query` a PARA destination | `vlt-query/SKILL.md:46` currently files to `{research}` **only because that is the sole legal home** for a raw agent-authored document. |
| 5 | `writers:` per container charter + module-fixed `{wiki}` floor | New schema in `extraction.md` *PARA containers* (rides step 2's bump). Retires the `{wiki}` carve-out **by name** into an instance of the general rule — **precedence by elimination**, Arc 9 D5. |
| 6 | `vlt-lint` authorization check | New check joining each write against its domain's declared writers — the enforcement a prohibition cannot perform. |

**Sequencing hazards — carried verbatim into the roundtable's joint-hunt, unresolved here.**

- **Rule ahead of mechanism.** Step 2 legalizes writes; step 6 supplies the authorization
  net. Between them writes are legal and authorization uncheckable. One release, or an
  explicit interim posture in the roadmap. *(Grounding note: this is precisely what the
  roundtable's existing forward beat hunts, and B9-2 shipped
  **enforcement-ships-with-widening** as a standing rule — so this hazard has a named rule
  to be measured against, not just a preference.)*
- **Legalizing relocates nothing.** The field symptom is content already buried in
  `_agent/`. Future-write legality moves no existing file; without an owner-gated
  relocation pass (a `vlt-groom`-shaped proposal the human ratifies), occupancy barely
  moves and a correct change reads at acceptance as a failed one.

**Open questions for ideation — carried verbatim, unresolved here.**

- **Undeclared-location default** — open to honest writes, or closed? (Provisionally *open*
  by the `trust: raw` ruling; confirm explicitly rather than defaulting into it.)
- **MOC prohibition** (`vault-operating-contract.md:190`) — recommended by the filing to
  survive as a **content-type** rule independent of zone posture, since it protects human
  *endorsement*, not human *territory*.
- **`_vault/`** — confirm its disposition (contract `:78` lists it human-only; the owner's
  2026-08-25 list omitted it).
- **Ship-verifiable vs field-contingent tagging** — the filing asks that retiring a
  load-bearing rule **gate** closeout (the A4-4(5) lesson). Capture flags this as the right
  instinct and leaves the tag to brief time (`build-brief` §9).

**Acceptance shape the filing already fixed, recorded so briefing does not re-invent it.**
*`trust: raw` is currently unrepresentable in PARA; if no `raw` content appears there after
the entry-condition change, the change did not take* — regardless of contract text. Field
pilot: `vlt-brief`'s next scheduled issue files to `{resources}/briefs/` at honest
`author: agent` / `trust: raw`, no relabeling, no pointer-container indirection, no bespoke
carve-out. One live run exercises the chain and closes tracker **#11** — which is A12-4's
subject, and the reason these two filings are one story.

**Interaction with a Cycle-11 carry-forward, flagged for ideation.** Carry-forward b2(2) is
a released watch on *"a partner resolves a `resources/`-write legality question from the
bundle without escalating."* If A12-3 ships, the bundle that partner reads is a different
bundle and the watch's premise is obsolete. Rule whether b2(2) is retired into A12-3's
acceptance or held separately — do not let it discharge against text this cycle rewrote.

### A12-4. A ruling answered by a release never reaches the issue that asked for it (2026-08-25) — `2026-08-25-111323-ruling-shipped-by-release-never-resolved-its-filing-issue.md`

**CONFIRMED — the symptom, verified live against the tracker this run.**
`gh issue list --repo mggower/bmad-module-vlt --state open` returns **#11 open**, labelled
`vault-filed, vault-accepted, captured, field:candidate`, zero comments. v0.15.0's build-2
rewrote the contract clauses the issue asked about. The tracker misreports candidacy, and a
vault or person asking *"is this still open?"* gets the wrong answer indefinitely. The
filing is right about what is broken.

**PROVENANCE CORRECTION — and it inverts the diagnosis.** The filing states: *"This issue
was never materialized. It arrived as a **ruling request** … and so was never bound to a
filing that could retire and carry it closed."* **All three clauses are false.**

- **#11 was materialized.**
  `factory/inbox/2026-08-24-142828-resources-outside-wiki-write-posture-unruled.md:3`
  carries the machine-written header `origin: mggower/bmad-module-vlt#11`, with
  *"GitHub issue opened 14:28:28Z via the vlt-feedback rail … kind: candidate"*.
- **It was bound to a roadmap entry.** It was captured as **A11-10** in Cycle 11 and
  answered by that cycle's **build-2**.
- **A close mechanism for it exists and is single-homed.**
  `.claude/skills/cycle-closeout/references/closeout-checklist.md:132-158`, *"Materialized
  filings close their issue"*: a filing being moved whose header carries
  `origin: <repo>#<n>` gets `gh issue close <n> --repo <repo> --comment "<shipped
  version/build + one-line disposition>"` in the same stage.

The filing's own preferred fix — candidate 1, *"Bind at capture … record the issue number
on that entry"* — **already shipped**, in B9-5's intake and closeout Stage 5. Building it
again would be the fifth-pass failure A12-3 warns about, wearing a different filing.

**GAP CONFIRMED — reshaped by grounding, and sharper than the filing's version.** #11 is
open **by design**, and the design is the defect. Two facts collide:

1. Cycle 11's closeout record holds `2026-08-24-142828` in the **active inbox** — A11-10's
   own clause is the `[field-contingent]` released watch **b2(2)**, unbounded by
   construction.
2. `closeout-checklist.md:155-157` binds issue state to that: *"A filing that **stays
   active** … leaves its issue **open** — the tracker mirrors the inbox, in both
   directions."*

So the close is bound to **archival**, archival is bound to the per-filing acceptance
criterion (`closeout-checklist.md:125-129` — *"Every clause traceable to that filing is
discharged"*), and A11-10's clause is a watch that may never fire. **Issue state is being
asked to carry two different questions with one signal:** *is this filing retired?* (what
the mirror rule actually states) and *is this question answered?* (what a reader takes from
an open issue). The first is honestly reported. The second is not reported at all.

This is the cycle's shape exactly: an open issue is a **proxy** for an unanswered question,
and it kept standing in after the answer shipped.

**Residual scope — what is left after the correction.** Not a new binding and not a close
mechanism. What is missing is a way to say **answered** on an issue *before* archival — a
second signal, or a comment. Grading the filing's three candidates against grounding:

- **"Bind at capture"** — **already shipped**; nothing to build. Drop it.
- **"Bind at ruling"** — *the ruling records the issue number, and the release that carries
  it comments the ruling text onto the issue.* **This is the shape that survives.** It adds
  the missing signal without touching the mirror rule, and the comment is the artifact a
  reader of #11 needed and did not get.
- **"Sweep at closeout"** — **barred by a standing rule**, not merely dispreferred:
  CLAUDE.md's *lists that claim completeness drift*. The filing reaches the same conclusion
  independently; record it as a rejected alternative so it is not re-proposed.

**Channel ruling owed at ideation — flagged, not decided.** Every site this touches is
**factory-side**: `.claude/skills/cycle-closeout/`, `.claude/skills/issue-triage/`,
`vlt-release`. None ships to vaults via `vlt-upgrade`. Per CLAUDE.md that is the **platform
ledger**, not a cycle build — and the filing itself points at **P-10** (the one-way
roadmap → tracker sync, `factory/platform/roadmap.md:57`, BUILT-awaiting on *this* cycle's
milestone + build issues). *"Close the issues this cycle answered"* is the same direction of
travel as a sync that already writes milestones, build issues and stage labels from the
roadmap. Ideation rules: **extend P-10, open a new platform item, or admit it as a cycle
build against the shipped `vlt-feedback` half.** Capture's read is that it is
platform-channel work, and that the vault-facing half (if any) is at most a pointer.

**Immediate action, independent of the fix — owner's, unblocked by any of the above.** Close
**#11** with the ruling text, noting that the ruling changed the boundary without opening
the folder, and that the filer's operation is carried forward in A12-3. *(Capture did not
do this: closing an issue is an outward-facing act on the public tracker and is the owner's
call. Note the ordering interaction — if #11 is closed now and A12-3 ships, the filer's
actual need is answered by a **different** issue's build. Say that in the close comment.)*

**Study check (P-14).** The cause — *one signal carrying two questions* — is arguably wider
than this filing (it is A12-5's shape too, and A12-2's). No study opened: the fix direction
is known and bounded, which `factory/studies/README.md` puts on the filing side of the
boundary. Recorded as a candidate if a third instance arrives — **and see A12-5's study
check for the test that must run before any `ST-4` is opened.**

### A12-5. A parked interim's exit condition is a claim about a rule that can change underneath it (2026-08-25) — `2026-08-25-111324-parked-interim-exit-condition-silently-invalidated-by-its-ruling.md`

**Filed as a hazard with one observed instance** — capture keeps that grading. The
instance: `{field-vault}` hit an upstream blocker, parked a partner's output in the agent
zone, filed the ruling request (#11), and recorded its own exit condition — in substance
*"one `git mv` plus one structure-map value"* — true under the reading of the blocker it
held at parking time (**which zone**). The ruling shipped under a different reading
(**which surface**). The exit was not unmet; it became **wrong**, and nothing said so.

**CONFIRMED — the asymmetry the filing names is real.** An unmet exit is visible (the vault
checks, sees it unsatisfied, waits). An **invalidated** exit reads as satisfied: a later
reader sees *"ruling landed, one-line exit, pre-authorized"* and executes a move that is now
illegal under the shipped rules. The record's confidence is inherited from the moment it was
written; the rule it depends on has moved since; the interim's own record is the only place
the dependency exists, and rulings do not read vault-local decision logs.

**GAP CONFIRMED — no shipped skill owns interim posture against an upstream blocker.**
Grepped every shipped skill: **`vlt-feedback` says nothing about parking, interims, or exit
conditions** — it files the question and stops. The only shipped parking discipline is
`vlt-mint/SKILL.md:104` (*"**Park (the default — the only path in an unattended session).**
Write the condition into the planning doc … parking is the *designed* response, not a
failure"*), and it is about an **unfieldable council verdict**, not an upstream ruling —
different blocker, different resume path (`vlt-mint`'s parks resume on an activation-time
scan; an upstream park resumes on a release the vault must notice). The filing's phrase
*"shipped in whichever skill owns interim posture"* has an answer, and the answer is
**none**. `frontmatter.md:290` is the sole other use of the word, and it governs a *shipped
declaration's* interim posture — factory-side discipline, not a vault's park.

**CONFIRMED — the module-side precedent the filing cites exists and worked.**
`CHANGELOG.md:74` (v0.12.0) carries a field-facing posture note addressed to vaults:
*"**A note for vaults with agent-authored PARA content:** … Until the model for this lands
(Arc 10), such content belongs under `_agent/`, not in PARA … the PARA location rule itself
stands unwidened."* That is the rail the filing wants reused, and it is precedent that it
reaches vaults. Two grounding notes on it: the mechanism is **DA3's CHANGELOG-notice**,
exercised again as recently as build-9's `frontmatter_key_count` notice in v0.15.0 — so it
is live, not archaeology. And with some irony, **that very note is the Arc 9 pass in
`ST-2`'s fifth-appearance table** — the module has already used this channel to tell vaults
to keep waiting on the exact question that invalidated this exit.

**Residual scope — both moves, graded.** The filing offers a module-side and a vault-side
move and asks ideation to rule which (or both). Grounding supports its stated preference:

- **Module side (stronger).** A ruling that **reframes** the problem carries an explicit
  *"if you parked against this, re-derive your exit"* note in the CHANGELOG entry. Site:
  the release choreography — `.claude/skills/vlt-release/` and/or `build-brief`'s
  CHANGELOG-notice staging. **Factory-side, therefore plausibly platform-channel** — same
  channel question as A12-4, and ideation should rule them together. Its virtue is that it
  does not depend on every vault having read guidance.
- **Vault side (cheap, rides along).** Guidance that an exit condition records **the
  blocker's shape and the filing reference**, not a pre-authorized command sequence — so
  the unwind is re-derived against the rules in force at unwind time. Grounding names the
  home the filing left open: **`vlt-feedback`**, which is where a vault files the question
  it is parking against, and which currently ends at transport.

**Open question carried forward, unresolved here — and it is a real unknown.** *How many
parked interims exist across live vaults, and were any others invalidated by Cycle 11's
rulings without anyone noticing?* Two grounding notes: (a) the mechanism **guarantees
silence**, so absence of reports is not evidence of absence — the filing says this and it is
correct; (b) this is **not a spike**. A spike reads an *external* source
(`factory/platform/spikes/README.md`'s boundary table); this reads *live vault content*,
which is an owner-run field question. No `S-N` stub opened. The honest instrument is a look
at `{field-vault}`'s mint decision log and any parked-interim records, which the owner can
run — capture flags it and does not schedule it.

**Study check (P-14).** The cause — *a record's confidence is inherited from a rule that has
since moved* — **is bigger than this filing**, and generalizes past parked interims (it is
the same shape as A12-4's stale issue state and, at a stretch, A12-3's stale location
proxy). Per `factory/studies/README.md` (*Opening a study*) that is a genuine opener, and
per *Citable, never blocking* opening one needs no ruling. **This run did not open one** —
deliberately: with one observed instance and a known fix direction, the register's own
near-miss test (*"a defect with a known fix is a filing"*) is closer to met than not, and
the owner filed it as a hazard rather than a diagnosis. Recorded as a **missed-chance
candidate**: if the Cycle-11-rulings sweep above finds further invalidated interims, or if
A12-4 recurs, open `ST-4` then rather than re-deriving this paragraph.

**Test it against `ST-2` §RC2 and `ST-3` §Convergence before opening anything.** *(Added
2026-08-25, same session.)* `ST-3` documents that one cause — *the loop can process defects
but not obsolescence* — has already been derived **three times independently**: from the cost
side (`ST-3`, 2026-08-24), the governance side (`ST-2` RC2, 2026-08-25), and as P-15's
measured baseline. A12-5 is adjacent to that cause and may be a fourth derivation rather than
a new one: an exit condition obsoleted by its own ruling, with nothing in the loop able to
notice, is RC2's shape one layer down — at the *vault-record* level rather than the *module-rule*
level. Capture does **not** rule it identical, and the honest difference is worth stating:
RC2 is about the loop's **input vocabulary** (nothing can express *"this is now redundant"*),
while A12-5 is about **downstream records going stale on a ruling** — related, not obviously
the same. But the register's own hard-won lesson is that *the pattern of independent
re-derivation is itself the diagnostic signal* (`ST-3` §Convergence, and `ST-2`'s existence at
all). So the rule for this cycle: **an `ST-4` is opened only after A12-5 has been read against
RC2 and found genuinely distinct** — otherwise the finding belongs in `ST-2` as a fourth
derivation, appended there, and the register gains a confirmation instead of a duplicate.
That check costs one read and is exactly the check this capture skipped on its first pass.

**Cross-filing relationship.** A12-4 and A12-5 are the same event seen from the two ends of
one rail: **A12-4 is the ruling never reaching the issue; A12-5 is the ruling never
reaching the record that was waiting on it.** Both are #11. Both are answered by *making a
ruling carry a terminal obligation to the thing that asked* — one to the tracker, one to
the field. Ideation should consider them as one package before splitting them, and the
roundtable should hunt the joint between them.

## Capture narrative — 2026-08-25 run (the judgment calls, on the record)

This run's scope was owner-confirmed in-session: **all five un-captured filings**, and the
cycle slug proposed at Synthesis rather than at Discovery (the owner's election). Judgment
calls, each at the point it was made:

1. **Cycle 12 opened, not amended.** `factory/CYCLE` read `none`; Cycle 11 CLOSED
   2026-08-25 with v0.15.0 shipped. New cycle, number one past the highest existing
   directory. `factory/CYCLE` updated to `12-proxy-claims` by this run.

2. **Slug chosen at Synthesis from the grounded set.** *proxy-claims* — all five filings are
   one surface carrying a claim on behalf of something else and outliving it. *reachability*
   (Cycle 11) asked whether the declared surface can be found; this asks whether what it
   says is still true. Rejected: *trust-and-closure* (leans on three of five),
   *answers-that-reach* (too near Cycle 11's name).

3. **A12-1 and A12-2 both re-sited.** Both filings name `skills/vlt-lint/assets`, which does
   not exist. The real site — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — is
   recorded in both captures because it changes briefing: four live concerns share that one
   560-line asset, and two of this cycle's fixes edit the same prompt block.

4. **A12-1 graded fresh, not a reopening of retired debt.** The B10-2(5)/B10-12(6)
   three-cycle debt retired on its bound with a correct measurement (the population
   predicate is field-proven at zero false positives). The extractor is a distinct layer.
   Grading it a reopening would falsify a retirement that was honestly earned.

5. **A12-2's convention question left open on purpose.** Whether `frontmatter.md` needs a
   one-line jurisdiction statement (a rule change: bump + re-ack) or whether the prompt fix
   suffices is a scope ruling with real handshake cost. Capture states both reads and rules
   neither.

6. **A12-3 captured as a supersession, per P-15's own class.** `factory/inbox/README.md:43`
   — *"supersession is the filing's claim, not its verdict"*. The capture names the rule to
   retire and the mechanism that earns it; it deliberately does **not** convert it into a
   fifth named surface, which the filing itself identifies as the failure mode a careless
   capture would produce.

7. **`writers:` corrected from "already shipped" to new schema.** Zero hits across
   `skills/`. The container model shipped; the key did not. Left uncorrected, a brief would
   have inherited a free lunch that does not exist.

8. **The `≥2 wiki pages` gate gained a third site.** `vlt-extract/SKILL.md:118`, not named
   in the filing. The *no handshake cost* claim survives verification.

9. **A12-4's diagnosis inverted.** The filing's core causal claim — never materialized,
   never bound, no close mechanism — is false on all three counts, and its own preferred
   fix already shipped. This is the exact failure mode the grounding step exists for, and
   the capture states the correction before the residual scope so a brief cannot skim past
   it. The residual gap is real and sharper than the filed one.

10. **Two channel rulings flagged, neither decided.** A12-4 and A12-5's module-side move are
    both factory-side (`cycle-closeout`, `issue-triage`, `vlt-release`), which CLAUDE.md
    routes to the platform ledger, and A12-4 names P-10 by hand. Capture's read is
    platform-channel; the ruling is the owner's at ideation. Recorded rather than assumed,
    because a cycle build and a platform item have different acceptance rails.

11. **Issue #11 not closed by this run.** Closing a public-tracker issue is outward-facing
    and the owner's act. The filing's *immediate action* is carried into A12-4 with an
    ordering note, not executed.

12. **No study opened; one candidate recorded.** The P-14 question was asked per filing.
    A12-3 **cites `ST-2`** and this run appends itself to that study's `cited_by:` — which
    is P-14's own discharging event. A12-5's cause is genuinely wider than its filing and is
    recorded as a missed-chance candidate (`ST-4`) with the trigger that should open it,
    rather than opened on one instance against a known fix. **Item 16 revises this item
    substantially — read it.**

13. **No spike opened.** Nothing here needed an external source. A12-5's *how many parked
    interims exist* is a live-vault question, not an external one — the spike register's
    boundary table puts it outside. Flagged as owner-runnable field work.

14. **GitHub intake ran clean, and materialized nothing.** `gh` authenticated (account
    `mggower`); all four open `vault-accepted` issues (#1, #6, #7, #11) already carry
    `captured` **and** have `origin:` hits on disk — no drift, no re-materialization. The
    amendment leg (`captured` + `amended`) returned empty. Reported here rather than
    silently, per the intake's degrade-loudly rule.

15. **Carry-forwards re-listed, not re-graded.** Cycle 11's frontmatter `status:` is the
    authority. One interaction was flagged rather than resolved: carry-forward **b2(2)**
    watches a question A12-3 may rewrite out of existence.

16. **The study check was run wrong on the first pass, and corrected in-session. This is a
    defect against P-14, filed below rather than buried here.** Owner challenge mid-run:
    *"have you seen the connection to `factory/studies/` with these items?"* The honest
    answer was no. The register question had been asked for all five filings and answered
    for four of them **from the README's index table**, not from the studies themselves.
    Reading `ST-1` and `ST-3` whole changed three gradings:

    - **A12-1 and A12-2** were graded *"cause local to one asset's prompt, no study."*
      Both are in fact instances of `ST-3`'s named *exact-facts-from-LLMs residue*
      contributing factor, in the very asset `ST-3` is about — **and both are `B5-3(2)`'s
      five-cycle-old watch firing**, a chain (`184704` → A4-13 → B5-3 → clause (2), held
      since Arc 5) that this run re-listed as the opaque token *"B5-3..B5-9"* in the carry-in
      register without connecting it to the two filings that discharge it. Cycle 11's own
      A11-11 capture had already written the adjacency down at
      `factory/cycles/11-reachability/roadmap.md:392`. It was in the record; nobody read it.
    - The correction also surfaced **a joint that the first pass explicitly denied** — it
      called the shared prompt block *"an ordering fact for briefing, not a joint."* With
      `ST-3`'s cost analysis in hand it is a joint: the cheap fix for both filings makes a
      ×147-agent prompt longer, in the same cycle that is ruling on A11-11's cost
      directions.
    - **A12-3** cited `ST-2` only. `ST-1` — which `ST-2` and the README both say to read
      alongside it, and which states outright that *"RC-A and RC-B are not retired"* — went
      unread, hiding that the filing's package re-derives four of `ST-1`'s five components
      and **omits C4 (provenance segregation)** entirely.

    **The generalizable finding: a one-line index entry cannot answer the register question.**
    `ST-3`'s index line reads *"…and full-mode lint has no memory across runs"* — nothing in
    it suggests the study owns the `PAGE_SCAN` extraction seam, which lives in its
    *Contributing factors*. The relevant cause was two levels below the surface the check
    was run against, in **both** misses.

    **The irony is load-bearing and should not be smoothed over.** `ST-3` §Convergence records
    that P-14's own back-fill reproduced the register's failure mode inside the register's
    own build. This run — **the first capture to execute P-14's grounding prompt** — reproduced
    it again, in the mechanism built to prevent it, and was caught by an owner question rather
    than by the check. That is the same failure a third time, and it is the strongest evidence
    available for what the check needs to be.

## Platform finding — P-14's grounding prompt, filed before it self-accepts

*(Raised 2026-08-25 by this run, against a **BUILT-awaiting** platform item that discharges
on this very capture. Recorded here so ideation sees it; the platform ledger is its home and
the owner routes it.)*

**The defect.** `.claude/skills/inbox-capture/references/grounding-methodology.md`, *Does this
cause already have a study?*, specifies the check as:

> *"The register is small; `ls` plus the README's index table is the whole check."*

That instruction was followed exactly, and it failed twice in one run (narrative item 16). It
is wrong for a reason that will not improve as the register grows: **a study's index line
names its headline cause, and a citing filing's cause is frequently one of its *contributing
factors*.** `ST-3` is indexed on governance projection and lint memory; it *owns* the
exact-facts extraction seam three sections down. No index table of any quality would have
surfaced that.

**Why this matters now rather than later.** P-14's own README already carries the guard that
*"a live diagnosis is never excluded"* — written because the back-fill got `ST-3` wrong. The
same build's **grounding prompt** still tells the one beat that is *already reading source*
to answer the register question from a summary. The register's stated failure mode is *a
cause re-derived that a study already holds*; an index-only check is a mechanism for
producing exactly that.

**Fix direction (ideation/owner rules, capture does not).** Change the check from *read the
index* to **read the studies whole** — which the README's own *Using a study* section already
demands (*"Read it whole before resting on it"*), making this an internal contradiction
inside P-14's own build rather than a new requirement. Three files is minutes; the register's
own history says the alternative costs a cycle. If cost ever becomes real at scale, the
honest instrument is a `causes:` **and** contributing-factor index, not a cheaper read.

**Bearing on P-14's self-acceptance.** P-14 discharges on a capture citing an `ST-N`. This
capture does cite `ST-2`, `ST-1` and `ST-3` — so the check passes on its face. Capture's
recommendation is that **it should not be discharged on its face**: the citation happened
because the owner asked a question, not because the mechanism worked, and discharging on the
artifact while the mechanism that produced it is known-defective is precisely the
false-green the module files against. Suggested disposition: **P-14 self-accepts only once
the grounding prompt is corrected**, with this run as the evidence for why.

## Ideation rulings — A12-1..A12-5 + the Cycle-11 deferrals (owner-steered, 2026-08-25)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**COMPLETE — filled 2026-08-25 over nine owner-steered rounds. Every slot is ruled.** *(Round count corrected from "eight" at the roundtable — the record carries nine, and Round 9 is the reversal; a written count standing in for a record that grew is this cycle's own thesis on its own cover page. Paige/Victor/Quinn, three independent hits — roundtable A21.)*
`build-brief` gates on this section being filled — it is. The **grouping** below is a
clerk-drafted ruling, **owner-adopted in full** (the Arc 9 / Cycle 11 precedent for delegated
rulings), and is marked as such; every other ruling is the owner's directly.

**What each round settled.**
- **Round 1 — the lint cost joint.** Q1 **splits per filing**: A12-2 takes the cause fix
  (subtractive), A12-1 the symptom fix now. Directions 1–4 unblocked. The capture's cost
  framing corrected — it merged two pools.
- **Round 2 — the five-cycle carry.** `B5-3(2)` **DISCHARGED on the letter**, graded leg by
  leg against the live reports; A12-1/A12-2 shown to be a class the clause never named.
- **Round 3 — the channel.** A new **`P-N`** takes both A12-4 and A12-5's module side (the
  boundary rule decided the channel mechanically); D1 rules them **one item, built
  separately**, with a **done-when per move** so neither drags the other into BLOCKED.
- **Round 4 — the PARA package.** Q4 takes **all six steps in one release** (Package C's
  implementation, three `ST-2` traps cleared); Q5 dissolves — **`ST-1`'s C4 already shipped**.
- **Round 5 — the boundary details.** Undeclared containers are **open**; the MOC rule is
  **narrowed to content type** (precedence by elimination); `_vault/` **stays human-only**.
- **Round 6 — the cheap halves.** Q6 lands as a **prose clarification, no bump** (the capture
  over-priced it); A12-5's vault side **rides this cycle**; b2(2) **retires** into A12-3;
  P-14's self-acceptance **withheld**.
- **Round 7 — the deferrals.** A11-2 **built** on `S-3`'s settled semantics with **no
  successor spike**; directions **1 + 2 land**, direction 4 **declared for Cycle 13**; **one
  release**. Q1 amended — A12-1's cause fix is neither direction 4 nor a JS refactor.
- **Round 8 — the ledger.** The `ST-4` test **run in session** (distinct from RC2, but no
  study); the five released watches re-carried **stamped with their triggering events**;
  E5 split; **no relocation mechanism** — it is an ordinary owner request once the
  destination is legal.
- **Round 9 — one amendment.** E8's *close #11* ruling **STRICKEN**: the owner had already
  answered #11 by comment at 17:06Z, and the shipped mirror rule keeps it open while its
  filing is active. Round 8 had ruled from the capture's morning observation without
  re-checking the tracker — the cycle's own proxy failure, committed by the session ruling on
  it. **No owner action remains on #11.**

**Two retirements rather than carries this cycle** — `B5-3(2)` (five cycles) and b2(2) — on
the cycle P-15's retirement rail self-accepts in.

Question numbering is the clerk's, for reference in session only; it implies no ordering or
priority. Seeded from the Cycle 12 capture run (2026-08-25, both passes) and the Cycle 11
closeout hand-off. **Seeded questions are the capture's, unanswered — nothing below is a
proposal, and no answer here is the clerk's.**

**Batch population (as captured):** A12-1..A12-5 (this cycle's five filings) + the Cycle-11
deferrals carried in — **A11-2 + E4** (`S-3` harvested, verdict *reshape*) and **A11-11
directions 1–4**. Carry-ins 1, 2 and 5 (the six released field-tail watches, build-8's
`overlay_rules_review` tail, and the E8 inherited registers) are re-listed, not re-graded;
their dispositions are the evidence-debt slot below.

**Capture's stated ordering constraint, recorded because it binds the session rather than a
build:** *"Do not brief A12-1/A12-2 before [the lint cost joint] is settled"* — Q1 below.
The capture also names A12-1 + A12-2 + A11-11 directions 1–4 as one sitting.

### Grouping & order

**Cycle scope — RULED Rounds 4/7/8 (2026-08-25): FIVE BUILDS, ONE RELEASE.** Cycle 12 takes
**A12-1, A12-2, A12-3, A12-5's vault side, A11-2 + E4, and A11-11 directions 1 + 2**.
**Not cycle builds:** A12-4 and A12-5's module side (the new **`P-N`**, platform channel —
Q3). **Declared for Cycle 13:** A11-11 **direction 4** and **A12-1's cause-fix instrument**
(Q8b) — *declared*, not deferred, each with its reason written. **Not taken:** direction 3.

*The grouping below is **clerk-drafted and owner-adopted in full** (2026-08-25), on the Arc 9
/ Cycle 11 precedent. ~~Build order: **1 before 2** (same file); the rest are independent.~~
**BUILD ORDER AMENDED AT THE ROUNDTABLE (2026-08-25, A11) — the sequence is `1 → 3 → 2`, and
build-2 is NOT independent of build-3.** Build-1 before build-2 because they edit one file;
**build-3 before build-2** because build-3 bumps `extraction.md` 6 → 7 **and adds a lint check**,
both of which change what a cached finding *means* — a sidecar populated before build-3 lands
serves findings adjudicated under a retired ruleset (A10's cache key). **Build-3 has no
predecessor and may be briefed first if preferred; build-2 must be briefed and built last.**
*(Quinn; five voices converged on the underlying cache-key defect.)*
**Renumbering, same amendment set:** the old **build-4 (the amendment trigger) moved to the
platform channel** (ruling R-5), so the old **build-5 (`vlt-feedback`) is now build-4**. The
bullets below keep their original numbers for traceability with the ideation rounds that ruled
them — **the authoritative current numbering is the table in `## Next lifecycle move`.***

- **build-1 — page-scanner corrections + waste removal.** A12-1's symptom clauses
  (`vlt-lint-full.js:143` schema + `:202` prompt), A12-2's cause fix (strip
  `frontmatter_valid`'s and `unmarked_supersession`'s jurisdiction over attestation, `:144` /
  `:153` / `:201-202`), Q6's `frontmatter.md` boundary clarification (**prose, no bump**), and
  **A11-11 direction 1** (drop the unused `wiki-index` read, reorder `pageScanPrompt`
  invariant-first, gate the cluster on `key_claims`).

  *Grouped on a hard constraint, not preference:* **all four edit `pageScanPrompt` and its
  schema**, and direction 1 **reorders the very block** A12-1/A12-2 add and subtract clauses
  in (`:172-174` lead vs `:201-202` body). Split across builds, the second rewrites the
  first's work.
  - `binds:` Q1, Q6, Q8b
  - `spike:` none

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25) — apply before briefing.**
  - **A1 — the site cites are v0.14.0 vintage.** `:172-174` and `:369-370` were correct at
    v0.14.0; build-8's cost-accounting block (`86a05e8`, `:102-128`) shifted them ~28 lines.
    **`pageScanPrompt` is ONE block at `:200-202`** — which is *why* the grouping constraint
    binds. Cluster prompt is `:402-406`, not `:369-370` (that is the **index** pass). Every
    other cite in the section is correct at HEAD. *(Mary/Builder/Amelia/Victor — 4 hits.)*
  - **A2 — 🔴 HARD RELEASE GATE, unpriced.** `package-lint.py:66-75` (E6) caps every fan-out
    schema at `JSON.stringify(schema).length <= 3700`. **Measured: `PAGE_SCAN` = 3223 — 477
    chars of headroom.** Q1 priced "~400–500 B" on the *prompt* side; written at that scale on
    the *schema* side this **fails the tag**. Ship-verifiable check: measure before and after.
  - **A3 — cite, don't restate.** `frontmatter.md:37` **already states A12-1's rule**
    (*"Never wrap a wikilink in backticks anywhere a link is intended"*) and the scanner
    already reads that file. **The DQL pages were COMPLYING.** The two clauses cite `:37` as
    authority — *a contradiction repair inside one prompt, not a new rule*. *(Sally.)*
  - **A4 — `:202` is the biggest waste in the file and is unlisted.** 1,132 B = **40% of the
    prompt**, restating `PAGE_SCAN` field descriptions the runtime already delivers as
    `schema:` (`outbound_links`/`category`/`topic_is_list`/`summary`/`name_callout_targets`
    duplicated at `:143`–`:159` **and** `:202`). ×147 = **166 KB/run**. Reduce `:202` to what
    the schema cannot carry; state A12-1's and A12-2's clauses **once**. *(Builder.)*
  - **A5 — `key_claims`: DROP, do not gate (owner ruling R-3).** Gating is **sampling**, which
    `ST-3`'s standing anti-direction forbids unconditionally; cluster membership is only
    knowable after the scan. Drop from `PAGE_SCAN` (`:155`) **and** the cluster prompt
    (`:404`) in one edit; `:403`'s live re-read stands. *Dissent: Amelia + Victor would gate
    the cluster and drop the re-read.*
  - **A6 — the reorder may be a no-op; confirm or drop it.** Invariant prefix after reorder is
    **~2.1 KB ≈ 550 tokens** against a **1,024-token cache minimum (2,048 on Haiku)**, and
    `:94` defaults `scanModel` to `haiku`. The 58 KB that dominates is `convRead` **tool
    output — never in a cacheable prefix under any ordering**. Brief confirms the prefix
    clears the floor, **else the reorder is dropped**. *(Builder.)*
    <br>**ANSWERED at brief time (2026-08-25, build-1 brief §Brief-time dispositions 1): the
    reorder is DROPPED.** Measured at HEAD: `pageScanPrompt` = **2,803 B**; the variable head
    (`${p.path}` / `${p.slug}`) is only the first **100 B**, so the invariant remainder
    available as a cacheable prefix is **2,703 B ≈ 676 tokens** — below the 1,024-token floor
    and far below Haiku's 2,048, and A4's reduction of `:202` shrinks it further. *A2's
    companion figure re-measured the same session with package-lint's own E6 extractor:
    `PAGE_SCAN` = **3223**, and F4's `key_claims` drop takes it to **3081** — so the schema
    clauses spend against **619** chars of headroom, not 477.*
  - **A7 — the `wiki-index@2` pin STAYS.** Drop the `convRead('wiki-index')` at `:201` only;
    `:371` (`indexPrompt`) still judges against it. Pin at `:11` and `consumers:` at
    `wiki-index.md:12` **unchanged**; build-1 re-runs R4's fan-out audit and records the pin
    survives. *(Builder + Amelia.)* Checked and clean: the `category:`-matches-H2 binding is
    computed **in JS** at ~~`:514-516`~~, so the drop breaks nothing *(Quinn)*.
    <br>**⚠ GROUNDING CORRECTION at brief time (2026-08-25, build-1 brief F5) — the cite has
    drifted again.** At HEAD the binding is `h2set` built at **`:496`** and consumed at
    **`:516`** (`category_no_match`). Quinn's finding is unchanged and the drop still breaks
    nothing; only the cite is superseded. *This is the third stale line-cite this cycle has
    caught in build-1's own site list (A1 caught two) — it is the live instance of the pattern
    already queued for `factory/inbox/` as out-of-scope item 4.*
  - **A8 — Q6's clause moves home (owner ruling R-2).** See Q6 as amended: it lands in
    **`write-verification.md` §Scope rule (self-marker)**, not `frontmatter.md`.
  - **A9 — carry the `per frontmatter@13` marker** R4 (`:16-21`) requires on any restated
    convention instruction. *(Mary.)*

- **build-2 — the change-keyed findings cache.** A11-11 **direction 2**: sidecar findings
  state keyed on change, facts-not-verdicts, plus the honest `scanned N / cached M of T`
  coverage line. Justified by the direction-0 live number — `churn_since_last_full: 5 of 146`,
  i.e. **141 of 146 pages re-judged for nothing**. ~~Queues **behind build-1** (same file).~~
  **AMENDED (roundtable A11, 2026-08-25): queues behind build-1 AND build-3** — same file as
  build-1; and build-3 changes what a cached finding means. **This is the cycle's last build.**
  - **Brief-time obligation (Q8b):** design the sidecar with the adjudicated-divergence memory
    filing `124223` (`B5-6(2)`) in view — shared mechanism, or it gets built twice.
  - `binds:` Q8b
  - `spike:` none

- **build-3 — the PARA posture (A12-3, ~~all six steps~~ **SEVEN steps — step 0 added at the
  roundtable, ruling R-1/A17**).** Package C's implementation, whole:
  retire the `≥2 wiki pages` gate (3 prose sites, no handshake); entry condition = honest
  attested frontmatter (contract `:66`/`:68`, `vault-rule-card.md:26`, correct
  `extraction.md:60`'s false human-initiation premise, **`extraction.md` 6 → 7 + re-ack
  `[vlt-extract, vlt-lint, vlt-track]`**); demote extraction to a disposition; give `vlt-query`
  a PARA destination **carrying Q5's `grounding:` conformance clause**; `writers:` per
  container charter + the module-fixed `{wiki}` floor; and step 6's `vlt-lint` authorization
  check. Plus **Q12's MOC narrowing** and the four restatement sites
  (`vlt-agent-creative:14`, `vlt-extract:13`, `vlt-review-council:51`, `vlt-upgrade:159`).

  **Steps 2 and 6 stay in ONE build** so enforcement-ships-with-widening (B9-2) is auditable at
  build level, not merely at release level — and so no interim posture is needed at all.
  **Carries the cycle's marquee retirement disposition** (D2): the Layer 3 location
  prohibition, `vault-operating-contract.md:68` + `vault-rule-card.md:26`.
  - `binds:` Q4, Q5, Q9, Q11, Q12, Q13, D2, E5
  - `spike:` none

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25) — build-3 grew a step and lost a retirement claim.**
  - **A17 — 🔴 STEP 0 ADDED (owner ruling R-1). The marquee retirement's premise was false.**
    **No step of `vlt-lint` selects the PARA population.** Scoped mode globs
    `find {wiki} {research} {sessions}` (`vlt-lint/SKILL.md:33`); full mode reads *"every page
    in `{wiki}`"* (`:39`); `grep -c "PARA\|para_" skills/vlt-lint/SKILL.md` → **0**. The
    workflow says so: `vlt-lint-full.js:517-519` defers `para_missing_attestation` to *"the
    SKILL's own PARA jurisdiction scan"* — **which does not exist**; three more `para_*` checks
    have report slots and **no producer**. The capture grounded the check *definitions* and
    never asked whether anything selects the population. **Step 0: extend `vlt-lint` Step 0/1
    to select `{projects}`/`{areas}`/`{resources}` in both modes**, and give full mode either
    the PARA page set or the SKILL-side scan the workflow already assumes. *Enforcement now
    genuinely ships with the widening — B9-2 satisfied in fact, not merely structurally.*
    *(Winston; moderator re-verified at the desk.)*
  - **A18 — presence is not truth.** The nets judge **field presence and enum membership**,
    never field truth — an agent writing `author: human` satisfies every one. `ST-1`'s grounded
    finding is **57 PARA files with correct-looking frontmatter and falsified `sources:`**;
    `ST-1`'s **C5** (*lint catches non-wiki `sources:` entries*) has **no shipped check**.
    Named in the sequencing hazards, and **E5's failure reading gains a distinct outcome:
    *`raw` appears but `author:` is falsified*.** *(Quinn.)*
  - **A19 — the `{wiki}` carve-out is NOT retired. Step 5's retirement claim is STRUCK.**
    *(Owner remitted the dispute; the room converged **4/4** — see the review record.)*
    `git log -S "carve-out by name"` → **one commit, `8290416`, Cycle 11 build-2, 2026-08-24**,
    which authored the carve-out **in the same hunk that widened Layer 3 over `{resources}`**.
    It is **D5 elimination already shipped** — *elimination's output, not an overlap awaiting
    one*; it keeps `{wiki}` out of the `para_*` population (`checks.md:18`); and under **Q11
    it is a LOCK, not friction** — `{wiki}` can carry no charter, so a vault cannot open the
    zone. **Retiring it would fire `para_*` against every page in the wiki and open the
    Librarian-only zone to `trust: raw` writes** against act-blocking `vault-rule-card.md:27`.
    **Stated in the roadmap's own words so a later cycle does not re-file it as a missed
    retirement — the fifth-pass failure A12-3 exists to stop: *Cycle 12 retires the Layer-3
    location prohibition and does NOT retire the `{wiki}` carve-out.***
  - **A20 — 🔵 FIFTH CAPTURE CLAIM OVERTURNED: the *module-fixed `{wiki}` floor* is already
    shipped.** `vault-operating-contract.md:64` already reads *"a Librarian-only zone: the
    Librarian is its only writer."* **That half of step 5 is struck as built.** *(Mary.)*
  - **A21 — the friction is REAL and is a RESTATEMENT problem — single-home it.** **Ten**
    shipped sites carry the full `{wiki}` qualifier (`vault-rule-card.md:26`, contract `:41`
    `:66` `:68` `:70`, `extraction.md:80` `:82` `:148`, `frontmatter.md:175`, `checks.md:18`);
    a partner filing one artifact reads it **six to nine times** before writing a byte. They
    reduce to **a canonical home plus short pointers** — build-3 already edits six, so this is
    a **scope narrowing, not new work**. **`checks.md:18` is exempt and keeps its explicit
    self-contained population sentence** — *B10-12's twelve `crossLayerSlugs` false positives
    are this cycle's own evidence for what a check that resolves its population elsewhere
    costs.* *Brief-time: canonical home is `contract:64` (Mary, Sally) or `extraction.md:148`
    (Quinn) — pick one, point the rest at it.*
  - **A22 — step 6 gains an explicit RESOLUTION ORDER, and it is load-bearing.** Nearest
    declaring ancestor's `writers:` → **else Q11's `open`, which is a PASS, never a finding**;
    `{wiki}` is removed at **population** time, never by an exception inside the check.
    Without it **step 6 has nothing to join for `{resources}/briefs/` — E5's own field pilot
    population.** *"This is the pilot's happy path, not a corner case."* *(Quinn + Sally.)*
  - **A23 — ⚠ NEW SCOPE step 5 never budgeted: inheritance.** A declared posture **binds its
    sub-containers** — an undeclared sub-container beneath a declaring parent inherits, it does
    not default to `open`; *"the alternative makes any closed posture unenforceable one
    directory down."* *(Quinn.)*
  - **A24 — the restatement list is wrong in three ways.** (i) The build spec says *four*
    sites and the summary says *five* — **`build-brief` parses the spec**, and the fifth
    (`vault-rule-card.md:26`) is the one the capture called *"the most load-bearing of all"*
    (`contract:192`: partners *"first load the rule-card"*). (ii) **`vlt-agent-creative:14` is
    a mis-cite** — it states wiki-grounding provenance, not a PARA location rule. (iii) The
    `≥2 wiki pages` gate's third site is **`vlt-agent-creative:37`**, a *different line* — *"a
    brief that reads the bullet linearly retires the wrong line"*; a **fourth** gate site is
    `vlt-agent-creative:14`'s *"a thin wiki is a stop"* clause. *(Paige/John/Amelia.)*
  - **A25 — three retirement sites D2 missed** (see D2 as amended): **`extraction.md:45`**
    (*"This does not add an artifact write-path"* — inside the bumped convention, on no site
    list), **`checks.md:16`'s rationale** (*"outside the sanctioned surfaces"* — the retired
    frame restated **inside the enforcement that replaces it**), and the **surface-count**
    prohibition (*"exactly two named surfaces … never a third"*) which step 4 **literally
    falsifies** by adding a third. *(Mary/Winston/Victor/Quinn/Paige.)*
  - **A26 — `vlt-query` becomes an undeclared consumer, and NO gate can see it.**
    `grounding:` is a `frontmatter.md` field (`:86`); `frontmatter.md:12`'s nine consumers omit
    `vlt-query`, which carries **no `depends_on:` at all**. E1 derives from declared consumers
    both ways; E3 fires only on a literal `name@version` token. **Add `depends_on:
    ["extraction@7", "frontmatter@13"]` to `vlt-query/SKILL.md`; add `vlt-query` to
    `extraction.md`'s and `frontmatter.md`'s `consumers:` (9 → 10).** *(Amelia + Quinn.)*
  - **A27 — the rule card carries a LIVE sha256 of the contract, and nothing re-derives it.**
    `vault-rule-card.md:10` — `derived_from: 'vault-operating-contract.md sha256:57df3488…3666'`
    — **verified to match the shipped contract today**. Build-3 edits the contract at `:66`,
    `:68`, `:190`. **Re-derive `:10` in the same build; ship-verifiable at rest.** Otherwise the
    vault-facing card carries a *verifiable, false* derivation claim — *a proxy for a rule that
    moved, in the cycle about exactly that.* *(Paige.)*
  - **A28 — the card's rule changes SHAPE, not just text.** `:26` is a **closed enumeration**;
    after step 5 posture is per-container-declared and **the card cannot enumerate what each
    vault declares**. Rewrite `:26` as a **test, not a list**, so the act-blocking card stays
    decidable at load time (CLAUDE.md, completeness-lists). *(Paige + Sally.)*
  - **A29 — `moc` must become a readable `type:` value.** `para_type_unknown`'s recognized set
    is **closed** (`checks.md:18`) and has no `moc`; `frontmatter.md:71`'s canonical list has
    none either. Q12 keys an **act-blocking** rule on an axis **no shipped field carries** —
    *A12-1's exact failure mode, installed fresh by this cycle*. The 6→7 bump adds `moc`.
    *(Winston + Sally.)*
  - **A30 — Q5 is not closed; the REGIME was never relieved.** See Q5 as amended.
  - **A31 — `writers:` may not be free in `frontmatter.md`.** The `grounding:` precedent
    (B10-10, `b7193e8`) bumped **both** conventions for one charter field — *"frontmatter@11-to-12
    nine-leg walk + extraction@3-to-4 three-leg walk"*. Price `frontmatter.md` **13 → 14 + a
    nine-consumer re-ack** at brief time; **not assumed free**. *(Mary.)*
  - **A32 — the handshake is complete today, conditionally.** `extraction.md:12` reads
    `consumers: [vlt-extract, vlt-lint, vlt-track]`, bipartite-consistent (each pins
    `extraction@6` at `:4`). **But `vlt-lint-full.js:11` is a listed consumer in its own right
    (`:12-15`)** — if step 6 or step 0 reaches that file, `extraction.md` gains a **fourth**
    consumer and the build owes a fourth ack. **State where step 0/6 are implemented.**
    *(Winston.)*
  - **A33 — no vault-facing surface announces any of this.** `vlt-upgrade`'s post-flight schema
    (`:96-116`) is a **closed key set** with **no key for a governance rule change**;
    `governance_divergence` renders `[]` on a pristine vault and *reads as health*; the rule
    card is **overwritten silently by design** (`vlt-setup/SKILL.md:148`). *"The honest
    description of the vault's moment of discovery is: a partner writes somewhere it could not
    write yesterday, and that is the notification."* **Add `governance_rule_changes: [...]`,
    never omitted when empty** — shipped-surface work, in a build already editing shipped
    surface, in the same release. *(Sally + Victor.)*
  - **A34 — Q11 is RETROACTIVE and inverts a live DECLINE+WATCH.** `writers:` is new schema, so
    **every charter that exists today is undeclared by construction** — and charters are
    human-gated, so *the population being opened is precisely the set a human deliberately
    framed*; **nothing machine-reads a charter's prose**, so a charter saying "human-maintained
    only" in words is open. `factory/cycles/10-signal-integrity/roadmap.md:764` carries the
    **confidentiality-as-container-attribute** DECLINE+WATCH (Maya's dissent preserved), which
    **E4 re-carried "untouched, not re-graded" in the same session Q11 inverted its default
    posture.** Re-grade the pair at brief time against the world A12-3 creates. *(Sally.)*
  - **A35 — brief-time, flagged now so it is not found at acceptance:** `{archive}` mirrors PARA
    source paths — **does an archived container's `writers:` travel with it?** *"The resolver
    makes this question askable for the first time."* *(Quinn.)*

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25).**
  - **A10 — the cache key. FIVE independent hits; the roadmap never says what "change" is.**
    Key = page content hash **× a `pageScanPrompt` + `PAGE_SCAN` schema fingerprint × the
    convention `version:` pins and check set the scan was judged under.** Any prompt, schema,
    convention-bump or new-check edit **invalidates the sidecar**; the coverage line names the
    fingerprint it cached under, and **the release's first full run is a COLD one, stated
    rather than discovered.** Build-1 redefines `outbound_links` and `frontmatter_valid`;
    build-3 bumps `extraction.md` 6→7 **and adds a check** — all in this release. *The word
    "invalidate" appears nowhere in the roadmap.* Precedent: `full-scale.md` step 3 already
    carries a version-skew defence. *(Winston/Amelia/Victor/Quinn/John.)*
  - **A11 — build-2 is NOT independent of build-3.** D3's *"the rest are independent"* is
    false; see D3 as amended.
  - **A12 — the acceptance shape, named now (E5's treatment).** Ship-verifiable half: the
    sidecar **at rest on a two-run temp fixture** — run 1 populates, run 2 reports
    `scanned N / cached M of T` with M > 0 and re-judges only changed pages. The live
    `churn`-ratio saving is `[field-contingent]` and **gates nothing**. *(John.)*
  - **A13 — the derive-first boundary must be answered, not asserted.**
    `vault-operating-contract.md:349`: *"Derive-first does not license deriving a state from
    the residue of the very process that produces it."* Worked instance at
    `vlt-upgrade/SKILL.md:45` (*"never read from the prior ledger entry … Two concrete homes,
    one discipline"*). **Build-2 opens a third home and points it the other way.**
    "Facts-not-verdicts" is *the claim, not the proof* — the brief states which side it sits
    on. *(Sally.)*
  - **A14 — `checks.md:49` owes a narrowing (obsolescence beat).** *"never prior lint reports
    (`{lint_reports}` is not read; reports stay walker-exempt)"* + a sanctioned store of lint
    state = **two rules over one population**; D5 says narrow one. Proposed: *"no stored
    **verdict**; derived facts may be carried in the sidecar keyed on change, and every run
    states its cached denominator."* *(Winston + Paige; **Mary dissents** — reads `:49` as
    surviving intact, "facts-not-verdicts is that rule honoured, not repealed." Brief rules.)*
  - **A15 — `lint-debt`'s premise changes.** The tripwire (`tripwires.yaml:83`) rations full
    runs **because a full run is expensive**; direction 2 makes that premise false. Re-tune on
    the first post-release numbers **or record why it stands** — not blind. *(Victor.)*
  - **A16 — `coverage_caps` is NOT retired by the coverage line.** `ST-3` anti-direction 2
    stands; the honest line is **additive**. *"Retiring a coverage disclosure to make a cache
    look complete is the exact move `ST-3` forbids."* Recorded so no brief reads it as an
    opening. *(Quinn.)*

- **~~build-4~~ — the amendment trigger. ⚠ MOVED TO THE PLATFORM CHANNEL (ruling R-5,
  2026-08-25) — NOT A CYCLE BUILD. Retained here for the ideation record; see the block below.** A11-2 + E4: replace the literal personal handle in all
  **three** templates
  (`.github/ISSUE_TEMPLATE/{field-pattern,field-candidate,field-defect}.yml:17`) with the
  repo-watch mechanism `S-3` settled (**All Activity** — already configured). Decide the
  `rail_contract` bump question at brief time.
  - `binds:` Q8a, Spikes
  - `spike:` **`S-3`** *(harvested — the gate is satisfied; the brief cites it into
    `consumed_by:`)*

  **🔴 ROUNDTABLE RULING R-5 (2026-08-25): BUILD-4 IS MOVED TO THE PLATFORM CHANNEL. Cycle 12
  is FOUR builds, not five.** *(Owner-ruled live on Sally's finding.)* Build-4's only sites are
  `.github/ISSUE_TEMPLATE/*.yml`, and CLAUDE.md is unambiguous: *"`.github/` is the repo-side
  half of the feedback rail's field contract, **likewise never copied into vaults**."* By the
  **same boundary rule Q3 applied mechanically** to A12-4 and A12-5 — *"an item is platform iff
  `vlt-upgrade` does not deliver it to vaults"* — **this is platform work.** Q3's table has
  three rows and **none is `.github/`: the boundary's third case was never asked, and the cycle
  ruled the same test in two directions in one session.** Q3's table gains a fourth row.
  - **A41 — the `@mention` retires, but the LABEL GATE MUST NOT.** *(Owner ruling R-4 —
    Victor's position adopted, Quinn's caveat binding either way.)* `S-3` settled that
    `@mention` is the filer's **only** post-creation lever; the replacement watch is real but
    **unobservable** — *"a personal notification preference on one account, unowned by any
    tracked file, invisible to filers, and silent on failure."* **Keep a filer-side residue**
    (what to do if an amendment goes unanswered) and record the watch as a **declared external
    dependency with a named silent-failure mode**. **The `amended` label admission rule in the
    same sentence is a separate mechanism with no replacement — retiring the mention must NOT
    retire the label gate.** *Dissent: Amelia and Sally each graded it a clean retirement —
    "the module's first retirement of a personal-handle dependency" (Victor's own phrase,
    against his own position).*
  - **A42 — the `rail_contract` bump question is ALREADY ANSWERED: NO BUMP.** The evolution
    rule at `field-contract.md:15-18` covers **payload fields and labels**; `:17` is
    instructional markdown, **neither**. Recorded so the brief does not re-derive it. *(Amelia.)*
  - **A43 — the single home never learns the mechanism.** All three templates say at `:1-4`
    *"The shape's single source of truth is `field-contract.md` — this form derives from it and
    **never restates it**."* **Line 17 IS the restatement**, and the single home (`:77`,
    `:82-84`) states only the **label** half. **After the build the repo-watch mechanism would
    exist in three derived forms and nowhere in its own home.** The home gains the trigger
    sentence; the three `:17` lines become pointers. *(Amelia.)*
  - **A44 — the fix is invisible to the filers it is about.** The templates say at `:15`
    *"Filing from an installed vault? **Prefer the `vlt-feedback` skill**"* — and that skill
    posts via `gh issue create --title --body` (`:100`), which **never renders template
    markdown**; grep of `vlt-feedback/SKILL.md` finds **zero** occurrences of amend /
    comment-back / `@mention`. **`vlt-feedback` gains the amendment line in the same build, or
    the fix reaches nobody who files through the skill.** *(Sally.)*
  - **Bound + grade, stated now rather than at closeout (John):** the template edit is
    `[ship-verifiable]`; the firing observation is `[field-contingent]` with a **named bound —
    the first issue opened on the repo by anyone other than the owner.** `S-3` records **no such
    event has ever occurred in the repo's history**. If none has by Cycle 13's closeout, this is
    graded **BLOCKED (unreachable)** on the platform rubric (`factory/platform/roadmap.md:33-37`)
    and routes to an owner ruling — **not re-carried as a watch a fourth time.**

- **build-5 — parked-interim guidance. *(Renumbered: this is now **build-4**, the cycle's third
  build — R-5 moved the amendment trigger off the cycle.)*.** A12-5's vault side, **new prose in
  `skills/vlt-feedback/`**: an exit condition records the blocker's **shape** and the filing
  reference, never a pre-authorized command sequence.
  - `binds:` Q7, D1
  - `spike:` none

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25) — FOUR voices independently challenged the home.**
  - **A36 — `vlt-feedback` is transport, and the rule needs an ARTIFACT.** `SKILL.md:19-20`:
    *"The issue is **transport**, not the record."* Its only vault-side write is a transient
    outbox that says so — *"a recovery artifact, **not a record**"* (`:112-113`) — and
    `_agent/feedback-outbox/` is *"deliberately **not** a `vault_structure` logical name."*
    Every other instruction in the file is **a step with an output and a gate** (the scrub
    checklist, the approval `HALT`). *"An exit condition records the blocker's shape"* names no
    file, no moment, no check. **Make it a step with an artifact:** after a successful post,
    offer to write a parked-interim record carrying (a) the blocker as a claim about **current
    shipped behavior**, (b) the issue URL, (c) *"re-derive the unwind against the contract in
    force at unwind time."* **The prohibition attaches to a field of an artifact the skill
    actually writes, or it does nothing.** *(Builder/Paige/Sally/Quinn.)*
  - **A37 — nothing ever RE-READS the record.** `vlt-feedback` is **invoked-only, never
    auto-file** (`:38-42`) — it runs only when a vault files something *new*. `vlt-mint` has the
    reading half (`:26` activation scan, `:104`). **Name a home something re-reads** — the
    decision log is the candidate (`vlt-upgrade/SKILL.md:78` reconciles it; E6's own instrument
    names the mint decision log). *"Guidance that improves what a vault writes but not what
    re-reads it ships the honest half of the fix only."* *(Sally + Paige.)*
  - **A38 — state the population.** This changes parks written **after** the upgrade and
    repairs **none already recorded** — including the single observed instance the filing rests
    on. *"A brief that implies otherwise over-claims the fix."* *(Quinn + Sally.)*
  - **A39 — `vlt-mint:104` is the second population, and it already complies.** *"Write the
    condition into the planning doc"* is a condition, not a command sequence. Brief rules
    whether the rule single-homes with `vlt-mint` pointing at it, or the two stay separate —
    **not a silence**. *(Mary + Quinn.)*
  - **A40 — obsolescence: ONE ADDED, none retired.** *"Never a pre-authorized command
    sequence"* is a new prohibition with no counterpart withdrawn — *"the
    eleven-cycles-add-nothing-retires pattern P-15 exists to make visible."* Enter it in the
    brief's retirement clause **as such**, not as `not applicable`. *(Builder.)*

**Ordering questions the capture left standing, unresolved — for the grouping ruling and
the roundtable's joint-hunt:**

- **A12-3's *rule ahead of mechanism* hazard.** Step 2 legalizes writes; step 6 supplies the
  authorization net; between them writes are legal and authorization uncheckable. One
  release, or an explicit interim posture in the roadmap. B9-2 shipped
  enforcement-ships-with-widening as a standing rule, so this is measured against a rule.

  **RESOLVED — the hazard does not arise.** Q4 rules all six steps into one release and the
  grouping keeps **steps 2 and 6 in one build** (build-3). There is no window in which writes
  are legal and authorization is uncheckable, so **no interim posture is needed** and B9-2 is
  satisfied structurally rather than by declaration.
- **A12-3's *legalizing relocates nothing*.** Future-write legality moves no existing file;
  without an owner-gated relocation pass a correct change reads at acceptance as a failed
  one.

  **RULED Round 8 (2026-08-25): NO RELOCATION MECHANISM IS BUILT — because none is needed.**
  Once the destination is legal, a migration is an **ordinary owner request** to a partner
  (*"migrate `_agent/briefs` to `resources/briefs`"*), not a capability the module must grow.
  **`vlt-groom` is not extended to rule relocation.**

  *Grounding (clerk, Round 8):* the discipline for performing a move **already ships, and it
  is not a prohibition** — `skills/vlt-upgrade/SKILL.md:75` carries the standing
  **relocation-migration discipline** (stub the old path, never touch parallel worktrees;
  re-point open dispatch pointers; walk `{overlays}/` and surface hits — report, never
  auto-edit) and states it holds for *"every relocation migration … and any future one."* The
  module also ships **five** human-gated relocation offers already (decision-log, proto-spec
  retrofit, loop-profile, wiki). The only thing ever missing was a **legal destination**, which
  is precisely what build-3 supplies. **A brief cites `:75`; it invents nothing.**

  **`ST-2` trap 7 is honoured as an acceptance caveat, not as scope:** *occupancy is not this
  cycle's measure.* Legalizing writes moves no existing file, so A12-3's acceptance is E5's
  instrument (**does `trust: raw` become representable and appear**), never a count of how full
  PARA is. Judged on occupancy, a correct change reads as a failed one.

  **Consequence recorded against E2:** `:75`(c) requires a migration to surface overlay hits in
  `overlay_rules_review:` — **which is E2's watch.** E2 is graded unbounded (*"a fault-shaped
  event nothing schedules"*); an owner-requested relocation after build-3 lands **would
  schedule it**. E2 stays released, but its event is now reachable by an ordinary act rather
  than only by a fault.
- **A12-1/A12-2 vs A11-11 directions 1–4 ordering.** Capture: rule in one sitting (Q1).

  **RESOLVED.** The sitting happened (Rounds 1 and 7) and its outcome is that the questions
  **separate**: A12-1/A12-2's fixes and **direction 1** share **build-1** (they edit one
  prompt block); **direction 2** is build-2, queued behind it; **direction 4** and A12-1's
  cause-fix instrument are **declared for Cycle 13**.

### Pre-ideation rulings the capture demanded

Seeded verbatim from the capture's *Next lifecycle move* list and the filings' carried-forward
open questions. Each is a question, not a position.

- **Q1 — the lint cost joint. Capture asks this be ruled first, because Q2 and the A11-11
  deferral depend on it.** A12-1 + A12-2's **symptom fix** adds instruction bytes to a
  `pageScanPrompt` that runs ×147 agents (`ST-3` prices the phase at 58,531 bytes/agent and
  names *ratcheted caution* as a root contributing factor); the **cause fix** moves
  deterministic extraction into JS. A11-11 directions 1–4 exist to shorten the same prompt.
  Symptom fix or cause fix, per filing, and in which order relative to the directions?
  *(Capture's grounding note, offered as a fact not a recommendation: A12-2's cause fix is
  subtractive and materially cheaper than A12-1's, because the JS-side answer already exists
  at `vlt-lint-full.js:482` — so the two may deserve the same brief but not the same
  disposition.)*

  **RULED Round 1 (2026-08-25): SPLIT PER FILING.**
  - **A12-2 takes the cause fix** — strip `frontmatter_valid`'s and `unmarked_supersession`'s
    jurisdiction over attestation. Subtractive: the deterministic answer already exists in JS
    at `vlt-lint-full.js:482`, and the change **removes** prompt bytes rather than adding them.
  - **A12-1 takes the symptom fix now** — the two clauses at `:143` (schema description) and
    `:202` (prompt return clause): targets inside inline-code or fenced blocks are not outbound
    links, and an outbound link is `[[ ]]`-delimited text and nothing else. ~~**Its cause fix (extract `outbound_links` in JS) folds into direction 4's
    territory** rather than being built here.~~ **AMENDED Round 7 (2026-08-25)** — the cause
    fix is neither direction 4 nor a JS refactor (the workflow has no page text; see Q8's
    grounding correction). It is a **new deterministic pre-pass instrument**, and it is
    **declared for Cycle 13** alongside direction 4. The symptom-fix half above stands.
  - **Directions 1–4 are ruled separately and are not blocked by this** — the sitting the
    capture asked for happened here, and its outcome is that the two questions separate.

  *Grounding the ruling was taken on (clerk, Round 1, measured this session — recorded because
  it corrects the capture's framing, which merged two cost pools):* the symptom fix touches the
  **prompt string** (2,813 B/agent, 414 KB/run) and adds ~400–500 B — **+16% of the prompt but
  +0.7% of per-agent input**, ~70 KB/run. `ST-3`'s 58,531 B/agent is the **convention read**
  (`frontmatter` 38,725 + `wiki-index` 8,133 + `write-verification` 6,114 + `wiki-supersession`
  5,550 = 58,522 measured today), 8.6 MB/run, which **neither fix touches** — direction 4 is
  what retires it. Note carried forward for directions 1–4: **`cost_accounting` measures the
  pool the symptom fix grows and not the pool that dominates** — `scanPromptChars`
  (`vlt-lint-full.js:236`) sums prompt strings only; the 8.6 MB of agent-side convention reads
  is absent from the instrument. **The instrument already said so** — the live report's own
  `cost_accounting.note` reads *"prompt_chars is workflow-composed prompt text only —
  agent-side file reads (page + convention bytes) are not visible from JS"*
  (`{field-vault}` `_agent/lint-reports/2026-08-24-1700-lint.yaml`). The blind spot was
  declared honestly at build-8; the capture's framing did not read it.

  **Left open by this ruling, for the grouping:** whether A12-1's symptom fix and A12-2's cause
  fix share one build. They edit the same prompt block; they now have different dispositions.
- **Q2 — `B5-3(2)`'s disposition. Its triggering event has fired** (carry-in 5; the clause is
  *"exact facts on the first real full + scoped lints"*, filing `2026-07-26-184704`, held
  active since Arc 5 — `factory/cycles/06-factory-honest-surface/roadmap.md:584`). Discharge
  it against A12-1 + A12-2, or hold it until the *reading* leaves the model (`ST-3` cause (a);
  A11-11 direction 4's territory)? Five cycles of silent re-carry ends either way.

  **RULED Round 2 (2026-08-25): DISCHARGE ON THE LETTER. The five-cycle carry ends here.**

  *Graded against the live reports this session, leg by leg — the clause text is
  `factory/cycles/05-kept-promises/roadmap.md:478-486`, and this grading is the discharge
  record:*

  | leg | criterion | field evidence | reads |
  |---|---|---|---|
  | **(a)** | `missing_targets` has no entry **whose target actually resolves** after normalization, and no index-registered stub | **2026-08-16 full:** fan-out reported 7, report note *"all resolve on disk"* — `crossLayerSlugs` omitting the handoffs/bases/areas zones. **2026-08-24 full:** fan-out reported 10, **none resolves** (9 code-span, 1 bare filename); the resolving class measured **zero** | failed once, **MET at 08-24** |
  | **(b)** | `near_duplicates` has no pair whose only secondary signal is a stem shared by ≥4 pages | **2026-08-16 full:** 6 two-signal pairs, all dismissed as documented structure; no bare-stem pair. 08-23 / 08-24: `not computed` (coverage caps) | **MET at 08-16** |
  | **(c)** | `sources_vs_prose_mismatches` has a producer in full mode; the first scoped lint fills or honestly empties it | **2026-08-24 full:** 9 entries. **2026-08-22 scoped:** one entry filled | **MET, both modes** |

  **The grounding correction the ruling rests on (clerk, Round 2): A12-1 is not the class
  leg (a) names.** Leg (a) asks about entries whose target *actually resolves* — the 82%
  alias/anchor/prefix class. A12-1's ten flags resolve to **nothing anywhere**, which is why
  they are structurally guaranteed to fire. The one time (a) genuinely failed was the
  `crossLayerSlugs` omission at 08-16 — and that is **B10-2(5)/B10-12(6), already retired on
  its bound in Cycle 11**. So **A12-1 and A12-2 neither discharge nor fail this clause**;
  they are a class it never named. Cycle 11's closeout had already ruled the code-span
  residue *"fresh signal and filed"*, and this ruling agrees with that grading rather than
  with the capture's.

  **What this ruling does NOT carry forward.** The *spirit* reading — *"the deterministic
  facts behave on real data"*, under which any model-made extraction defect keeps the clause
  alive until the reading leaves the model — was considered and **not adopted**. Recorded as
  a rejected alternative so it is not re-proposed: the concern it names is live, but it now
  lives in A12-1's own build and in direction 4, under criteria that match it, rather than
  inside a clause written for a different class.
- **Q3 — channel for A12-4 + A12-5's module-side move.** Every site is factory-side
  (`.claude/skills/cycle-closeout/`, `.claude/skills/issue-triage/`, `vlt-release`) and none
  ships to vaults. Extend **P-10** (the roadmap → tracker sync, BUILT-awaiting on this
  cycle), open a new platform item, or admit it as a cycle build against the shipped
  `vlt-feedback` half? Capture's read is platform-channel, vault-facing half at most a
  pointer. **They share a rail and capture asks they be ruled together.**

  **RULED Round 3 (2026-08-25): A NEW `P-N`, CARRYING BOTH MOVES.** P-10 is not extended —
  it stays clean and self-accepts on this cycle's tracker sync as re-bound (2026-08-25).

  *Grounding the ruling was taken on (clerk, Round 3): **the boundary rule decides the
  channel mechanically, and the capture left it more open than it is.*** The contract
  (`factory/platform/roadmap.md:11-14`) reads *"an item is **platform** iff `vlt-upgrade`
  does not deliver it to vaults … Anything under the shipped surface (`skills/vlt-*`,
  `.claude-plugin/`) belongs on the arc roadmap, **no exceptions**."* Applied to the sites:

  | move | sites | channel |
  |---|---|---|
  | A12-4 "bind at ruling" | `.claude/skills/cycle-closeout/`, `.claude/skills/issue-triage/`, `.claude/skills/vlt-release/` | **platform** — all factory |
  | A12-5 module side (the re-derive-your-exit notice) | `.claude/skills/vlt-release/`, `.claude/skills/build-brief/` | **platform** — all factory |
  | A12-5 vault side (exit records the blocker's shape) | `skills/vlt-feedback/` | **cycle build** — shipped surface, no exceptions |

  So the channel was never the open question; **extend-or-open was**, and it is ruled open.

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25).**
  - **A45 — the fallback channel is MIS-CITED and UNAVAILABLE.** *"Step-6 report,
    `vlt-upgrade/SKILL.md:93`"* does not exist: the skill has **five** Step headings and `:93`
    sits under **`## Step 4 — Post-flight divergence report`** (`:91`); "Step 6" is item 6
    *inside* Step 3 (Provision), which renders nothing. **And the report's key set is CLOSED** —
    `vlt-upgrade/SKILL.md:126`: *"verify its top-level key set matches the schema block above;
    **a missing or extra key is fixed and re-persisted**."* A free-text notice is an *extra key*
    and **the shipped verification deletes it.** *(John + Sally.)*
  - **A46 — therefore BOTH surviving options are `skills/vlt-*` work**, which Q3's own table
    rules a **cycle build, no exceptions**. **The new platform item carries A12-4 ONLY**;
    A12-5's module side is **BLOCKED (unreachable)**, not waiting, and its unlock is A33's
    `governance_rule_changes:` schema key. *(John + Sally.)*
  - **A47 — 🔴 THE ITEM NUMBER IS STALE. `P-16` IS TAKEN.** `factory/platform/roadmap.md:525`
    already carries **`P-16` — the `promise:` line**, filed 2026-08-25 and *"**Not actioned
    mid-flight by owner ruling** … **This item waits for Cycle 12 to ship**."* **The new item is
    `P-17`.** P-16's own correction block also bears on this ruling: *"This entry was written on
    the premise that the CHANGELOG is the first vault-facing sentence in the loop. **It is
    not.** A brief's `title:` is already 'public prose … collected verbatim into the module's
    CHANGELOG.md entry' (`brief-anatomy.md:30-31`)."* *(Victor; moderator verified.)*

  **⚠ GROUNDING CORRECTION carried into the new `P-N`'s brief-lite — the CHANGELOG has no
  delivery path to a vault.** `CHANGELOG.md` is referenced **only by factory skills**:
  `.claude/skills/build-brief/SKILL.md:173`, `references/brief-anatomy.md:30`, and
  `.claude/skills/vlt-release/references/choreography.md:51`/`:59`/`:64`/`:71`/`:73`/`:119`
  + `SKILL.md:56`. **Zero references anywhere under `skills/vlt-*`, `vlt-upgrade` included.**
  Nothing in the module's shipped surface routes a vault to it. The capture graded the
  module-side move *"stronger … it does not depend on every vault having read guidance"* —
  grounded, it depends on something **weaker**: a file nothing points a vault at. The
  v0.12.0 precedent reached the owner because the owner reads this repo. Two live options
  for the brief-lite to price, neither ruled here: a shipped surface starts pointing at
  release notes (**that is `skills/vlt-*` work — a cycle build, not this `P-N`**), or the
  notice rides a channel `vlt-upgrade` already renders (its Step-6 report,
  `skills/vlt-upgrade/SKILL.md:93`).
- **Q4 — A12-3's six steps: whole or cut.** Steps and grounded costs are tabled in the
  capture (A12-3, *residual scope*).

  **RULED Round 4 (2026-08-25): ALL SIX STEPS, ONE RELEASE.**

  *The framing this ruling was made under (clerk, Round 4 — recorded because the question as
  posed by the capture invited a scope cut that `ST-2` had already argued against):* the six
  steps are not a menu, they are **Package C's implementation**. `ST-2`'s *What was
  recommended, and what the owner ruled* records four **settled owner rulings** from the
  2026-08-25 problem-solving session — `trust: raw` accepted in browsable space; only
  `daily/`, `new/`, `sources/` truly human-only; `vlt-extract` demoted not retired; **Package
  C selected** (trust re-attachment **plus** declared per-domain stewardship). The
  substantive decision was already the owner's; Q4 ruled **how much lands in Cycle 12**, and
  the answer is all of it, together.

  **One release is what clears the traps.** `ST-2` records seven, and three cuts the capture's
  framing invited each walked into one:
  - **Step 2 without step 6** is trap 6 — *"do not ship trust re-attachment without its
    authorization net or a declared interim posture."* Co-shipping them means **no interim
    posture is needed** and the *rule ahead of mechanism* hazard does not arise. B9-2's
    enforcement-ships-with-widening is satisfied structurally rather than by declaration.
  - **Dropping step 4** would kill the acceptance instrument. `ST-2`'s sharpest test —
    *"`trust: raw` is currently unrepresentable in PARA; if no `raw` content appears there
    after the change, it did not take"* — needs a **producer**. No step 4, no `raw` content,
    nothing to measure (E5).
  - **Dropping step 5** would drop half of Package C; `ST-2` calls the two interventions
    *"complementary, not competing"* and names step 5's territory (posture moved from
    module-global to vault-declared) as what **drains Loop 3**, the allowlist-accretion
    dynamic.
  - Trap 4 stands over all three: *"do not treat the minimal patch as the neutral choice."*

  **Build count is not ruled here** — one release may still carry several builds. That is the
  grouping's call.
- **Q5 — `ST-1`'s C4 (provenance segregation): adopted, or explicitly declined.** `sources:`
  stays wiki-only forever with a new `grounding:` field for external evidence. A12-3 carries
  four of `ST-1`'s five components and **not this one**; step 4 routes `vlt-query` output
  (whose `sources:` lists `{research}` notes, `vlt-query/SKILL.md:46`) into PARA without
  ruling what provenance field it carries. Capture: *"the single largest unexamined risk in
  the six-step package."*

  **RULED Round 4 (2026-08-25): C4 IS ALREADY SHIPPED — RECORD IT AS SUCH. Step 4 carries a
  one-line conformance clause. No new component, no open design risk.**

  **⚠ GROUNDING CORRECTION — the capture's `NOT CARRIED` grading of C4 is wrong.** C4 is
  *"`sources:` stays wiki-only forever; a new `grounding:` field carries external evidence —
  the component that restores the firewall"* (`ST-1` §What the session recommended). Every
  part of it is live in the module at v0.15.0:
  - `extraction.md:40` — *"**`sources:`** continues to list **only wiki pages** — exactly as
    before, the wiki-provenance audit trail."*
  - `extraction.md:121` — **`grounding:`** is *"an optional flat list of evidence and context
    references that are **not wiki provenance** … the relation/evidence edge `sources:` was
    never meant to carry. It may appear on PARA artifacts and on container charters."*
  - `frontmatter.md:94` and `:177` — the segregation stated in the field schema, PARA
    artifacts included.
  - **Enforced, not merely declared:** `skills/vlt-lint/references/checks.md:48` defines
    `method_in_grounding` and fires it on *"each PARA artifact or container charter carrying
    `grounding:`"*. Never auto-fix; both modes.

  The capture mis-graded C4 the same way its first pass mis-graded A12-1/A12-2: it read
  `ST-1`'s recommendation table without checking whether the module had since implemented it.
  `ST-1`'s own *What became of it* says only that **RC-A and RC-B** are not retired — it never
  says C4 is unbuilt. `ST-2` §Where this differs from `ST-1` independently records that
  `ST-1`'s second verb is *"not refuted, only out-priced."*

  **What is actually owed, and it is one line.** A12-3 step 4 routes `vlt-query` output into
  PARA, and `vlt-query/SKILL.md:46` lists `{research}` notes in `sources:`. Under the shipped
  rule those entries are **illegal in `sources:`** — they belong in `grounding:`. **Step 4's
  brief carries that conformance clause.**

  *(Considered and not taken: widening `method_in_grounding`'s population for the artifacts
  step 4 newly admits. The check already fires on PARA artifacts carrying `grounding:`, which
  the new arrivals will — so the population reaches them without an edit. Recorded so the
  question is not re-opened at brief time without new evidence.)*

  **⚠ ROUNDTABLE AMENDMENT A30 (2026-08-25) — Q5 IS NOT CLOSED. The correction is true of the
  FIELD and false of the REGIME.** C4's field shipped; the regime it needed relieved did not.
  `extraction.md:36` states unconditionally: *"Every general or method claim in the body still
  traces to a wiki page listed in `sources:` … the amendment does not touch it."* `:121` scopes
  the new field **against** it: *"`grounding:` carries evidence and relations, **never method** —
  a method/general claim whose only support is a `grounding:` entry is a **violation**."* And
  `checks.md:48` enforces **both**, never auto-fixed, both modes — `method_in_grounding` **and
  `method_not_in_sources`**. Against that, `vlt-query/SKILL.md:10`: *"Every significant claim
  cites a wiki page **or research note**."* **Move the research notes to `grounding:` per Q5's
  clause and every claim resting only on them fires both flags.** Q5's parenthetical read the
  population question and stopped there — **the population reaching them is the defect, not the
  reassurance.** C4 was one leg of a package whose **C3** supplied a second verb owning the
  non-wiki-derived artifact; **C3 is unbuilt.** Build-3's brief **rules the posture for the new
  class** (exempt by `type:`, or narrow the invariant's population) and **may not treat this
  closed**. *Winston's qualification, carried:* `method_in_grounding` fires only on files
  *carrying* `grounding:` — an artifact that **omits** it drops its provenance silently, so the
  conformance clause is a **requirement**, not a routing note. *(Mary + Winston.)*
- **Q6 — A12-2's convention clause: in or out.** `checks.md:16` states the attestation scope
  rule and `frontmatter.md:82` states the field's home; neither says attestation is **out of**
  frontmatter-validity jurisdiction. Prompt-only, or also a boundary statement in
  `frontmatter.md` — **which is a rule change: `version:` bump + re-ack every consumer.**

  **RULED Round 6 (2026-08-25): IN, AS A PROSE CLARIFICATION — NO BUMP, NO RE-ACK.**

  **⚠ GROUNDING CORRECTION — the capture over-priced this clause.** It states the clause
  *"would be a rule change: `version:` bump + re-ack every consumer."* That cost is real and
  it is the module's largest: `frontmatter.md` is **`version: 13` with 9 consumers**
  (`vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch, vlt-setup,
  vlt-groom, vlt-lint-full.js`). But the clause **does not change what the convention
  asserts.** The Write-attestation section (`frontmatter.md:74-84`) says only *"Two keys
  record that the writing operation ran the tier-1 write-verification checklist on the
  file"* — it **never declares them required** for base frontmatter validity, and the scope
  rule plus the pre-adoption informationality posture are already single-homed at
  `skills/vlt-lint/references/checks.md:16`. So **absent `verified_by:`/`verified_at:` was
  never a frontmatter-validity defect**, and saying so states what is already true. Per
  CLAUDE.md's version-handshake rule, *prose clarifications don't bump*.

  **Precedent inside the same file:** `frontmatter.md:84` already carries a boundary clause of
  exactly this shape — *"**Not the `trust:` rung.** `verified_by`/`verified_at` record
  structural verification … the `trust: verified` rung records claim verification. Same word,
  orthogonal axes."* The new clause is its sibling: same file, same job, same cost.

  **Consequence: the cheap-vs-durable trade the capture framed dissolves.** *(See the
  roundtable amendment below — the trade still dissolves, at a different site.)*

  **🔴 ROUNDTABLE RULING R-2 / AMENDMENT A8 (2026-08-25): THE CLAUSE MOVES HOME — it lands in
  `write-verification.md` §Scope rule (self-marker), NOT `frontmatter.md`.** *(Owner-ruled on
  Victor's and Paige's independent convergence.)* `frontmatter.md:74` **opens the very section
  by disclaiming scope**: *"This section defines only the **fields**; the checklist, fail-open
  rule, **scope rule**, and audit contract live in `write-verification.md`."* And
  `write-verification.md:53` **is** `## Scope rule (self-marker)`. `checks.md:16` — which this
  ruling named as the single home — **is itself a pointer there**. Q6's own precedent argument
  cuts the other way: `:84`'s *"Not the `trust:` rung"* is a clause **about fields**, which is
  exactly what that section says it carries. **The no-bump grading STANDS and gets cheaper** —
  `write-verification.md` is `version: 3` with **5** consumers, against `frontmatter.md`'s
  `version: 13` with **9**.

  **Dissent on record (Winston, Amelia).** Both re-tested the Round-6 ruling independently
  against source and both confirmed it holds **as written**: `frontmatter.md:74-84` never
  conditions validity on attestation, and `:84` is a genuine sibling precedent. **They lose on
  *home*, not on *grade*.** **Paige's stronger form, recorded because it is the risk if the
  brief ignores R-2:** no shipped file defines *"frontmatter validity"* as a term, and
  `vlt-lint-full.js:200` tells the scanner to judge validity *"against the MERGED rules"* of
  `frontmatter.md` — **excluding a section narrows what the convention asserts.** *If the brief
  writes a jurisdiction clause into `frontmatter.md` after all, it is a rule change: 13 → 14 and
  nine re-acks, budgeted in build-1.* The durable fix —
  the convention stating the boundary, so *every* consumer stops re-deriving the wrong answer
  rather than just the page scanner — lands at clarification cost, alongside Q1's cause fix
  in the prompt and schema.
- **Q7 — A12-5's two moves: module side, vault side, or both.** Module side (stronger): a
  ruling that reframes a problem carries an explicit *"if you parked against this, re-derive
  your exit"* CHANGELOG note (DA3's rail, live as recently as v0.15.0's build-9 notice).
  Vault side (cheap): guidance that an exit condition records the blocker's **shape** and the
  filing reference, not a pre-authorized command sequence — home named as `vlt-feedback`,
  which currently ends at transport.

  **RULED Round 6 (2026-08-25): BOTH — and the vault side RIDES THIS CYCLE.** The module-side
  move is on the new `P-N` per Q3; the vault-side guidance is built here as shipped-surface
  work in **`skills/vlt-feedback/`**: an exit condition records **the blocker's shape and the
  filing reference**, never a pre-authorized command sequence, so the unwind is re-derived
  against the rules in force at unwind time.

  *Grounding (clerk, Round 6):* `skills/vlt-feedback/SKILL.md` is 7,186 bytes and contains
  **zero** occurrences of *park*, *interim*, *exit condition* or *blocker* — the capture's
  "no shipped skill owns interim posture" finding holds at this site too. There is no existing
  parking discipline to extend; this is **new prose in a shipped skill**, and the brief prices
  it as such rather than as an amendment.

  **Why the vault side is not the optional half.** Q3's correction established that the
  module-side notice has **no delivery path to a vault that does not read this repo**
  (`CHANGELOG.md` is referenced only by factory skills). The vault-side guidance does not
  depend on that path at all — it changes what a vault writes at parking time. The two halves
  are complementary rather than redundant, and the cheaper one is the one that works unaided.
- **Q8 — the Cycle-11 deferrals' grouping.** A11-2 + E4 (`S-3` **harvested**, verdict
  *reshape*; preserved constraint: *the trigger stays real, not prose*) and A11-11
  directions 1–4 were deferred **to this cycle** and are owed a grouping ruling alongside the
  new captures. Directions 1–4 are Q1's other half.

  **RULED Round 7 (2026-08-25), in two parts.**

  **(a) A11-2 + E4 — BUILT THIS CYCLE.** `S-3` answered the design question, so the build
  ships against settled semantics: the repo watch on **All Activity** (already set — see the
  Spikes section) replaces the literal personal-handle trigger in all three templates
  (`.github/ISSUE_TEMPLATE/{field-pattern,field-candidate,field-defect}.yml:17` — three
  instances, per Cycle 11's grounding correction). The observation leg rides acceptance as
  **field-contingent**. The preserved constraint is honoured on `S-3`'s own terms: *the
  trigger stays real, not prose* — the mechanism is verified to exist and to be configured,
  and the notification's firing is the acceptance evidence, not the brief's premise.

  **(b) A11-11 directions — 1 + 2 LAND THIS CYCLE; direction 4 is DECLARED FOR CYCLE 13;
  direction 3 is not taken.**
  - **Direction 1 (workflow-only waste removal)** — justified by measurement at its sites:
    `wiki-index.md` sits in the page-scanner read set and is unused by it (8,133 B × 147 ≈
    **1.2 MB/run** of pure waste), the cache-hostile prompt ordering
    (`vlt-lint-full.js:172-174` — variable before invariant), and `key_claims` bought at scan
    then discarded when the cluster prompt re-reads every page live (`:369-370`). No
    correctness surface.
  - **Direction 2 (change-keyed findings cache, facts-not-verdicts, honest
    `scanned N / cached M of T` coverage line)** — justified by the direction-0 live number:
    **`churn_since_last_full: 5 of 146`**, i.e. **141 of 146 pages re-judged for nothing** on
    the 2026-08-24 full run. **Brief-time obligation attached:** its sidecar-state mechanism
    is shared with the adjudicated-divergence memory filing `124223` (E8 register, `B5-6(2)`),
    and the A11-11 capture asked they be ideated together — **direction 2's brief designs the
    sidecar with that companion in view, or the mechanism gets built twice.**
  - **Direction 4 (scanner-card projection) — DECLARED FOR CYCLE 13, not deferred.** The
    distinction is deliberate and is this cycle's own lesson applied: *deferred* is how
    `B5-3(2)` spent five cycles as a token in a list (Q2). **Declared** means named, with its
    reason written, and owed a grouping ruling at Cycle 13's ideation.

    *The reasons, on the record:* **(i) it collides with A12-3 inside one tag** — D3 rules one
    release, and direction 4 builds addressable projections **of conventions** while A12-3
    rewrites `extraction.md` (6 → 7) and the contract in that same release; the projection
    would be authored against a moving target, and single-home discipline — the very thing
    that makes projection hard (`ST-3` cause (a)) — is what A12-3 is also disturbing.
    **(ii) It is the only one of the four with a live design unknown**: what a scanner card
    *is* (derived artifact? addressable convention anchor?) and how it stays in sync without
    breaking single-home. `ST-3` says cause (a) *"binds every future skill of that shape"* —
    a wrong projection mechanism is inherited by every future fan-out consumer.
    **(iii) Release size** — the one release already carries A12-3's six steps, A12-1, A12-2,
    Q6, A11-2 and `vlt-feedback`.

    *`ST-2` trap 4 (*do not treat the minimal patch as the neutral choice*) was weighed and
    answered rather than ignored: directions 1 + 2 are **not** the minimal patch — they are
    the measured wins — and direction 4 is declared with a cycle rather than dropped.*

  **⚠ GROUNDING CORRECTION, carried from this ruling back into Q1 (clerk, Round 7).** Q1
  recorded that A12-1's cause fix *"folds into direction 4's territory"*, following the
  capture. That is wrong twice:
  1. **Direction 4 is not link extraction.** It is convention projection — it retires the
     38.7 KB `frontmatter.md` **read**, and says nothing about who extracts wikilinks.
  2. **The cause fix is not a JS refactor.** The workflow receives `pages: [{ slug, path }]`
     — **paths only** (`vlt-lint-full.js:32`) — and contains no `fs` and no file read
     anywhere; page text reaches **only the fan-out agents**. "Extract `outbound_links` in JS"
     is therefore **not available as stated**. It requires a **new deterministic pre-pass
     instrument** — a stdlib script the SKILL runs at Step 0 handing the workflow a
     slug → links map (precedent: `skills/vlt-setup/assets/hooks/vlt-vitals.py`).

  **Consequence:** A12-1's cause fix is **declared for Cycle 13 alongside direction 4**, as a
  named instrument rather than as a fold into another build. Q1's symptom-fix ruling is
  unaffected and stands.
- **Q9 — carry-forward b2(2)'s disposition.** The released watch is *"a partner resolves a
  `resources/`-write legality question from the bundle without escalating."* If A12-3 ships,
  the bundle that partner reads is a different bundle and the watch's premise is obsolete.
  Retire it into A12-3's acceptance, or hold it separately — capture's constraint: **do not
  let it discharge against text this cycle rewrote.**

  **RULED Round 6 (2026-08-25): RETIRE INTO A12-3's ACCEPTANCE.** Q4 ruled all six steps into
  one release, so the bundle the watched partner would read is rewritten by this cycle. The
  watch's premise is obsolete on landing, and carrying it forward would let it discharge
  against text this cycle authored — the capture's stated constraint, honoured. Its question
  is absorbed by A12-3's own acceptance shape (E5), which measures the same thing against the
  rules that will actually be in force.

  *Recorded as the cycle's second retirement-not-carry (with Q2's `B5-3(2)`) — both on the
  cycle P-15's retirement rail self-accepts in.*
- **Q10 — P-14's self-acceptance.** Discharge on this capture's `ST-1`/`ST-2`/`ST-3`
  citations, or withhold until the grounding prompt is corrected (see *Platform finding*
  above)? Capture recommends withholding: the citation happened because the owner asked a
  question, not because the mechanism worked.

  **RULED Round 6 (2026-08-25): WITHHOLD — P-14 self-accepts only once the grounding prompt is
  corrected.** Capture's recommendation adopted. Discharging on the artifact while the
  mechanism that produced it is known-defective is the false-green the module files against.

  **This ideation session is further evidence, and it is recorded as such.** Two of the
  session's largest corrections came from reading a study **whole** and would have been
  invisible to the index-table check specified at
  `.claude/skills/inbox-capture/references/grounding-methodology.md`:
  - **Q5** — `ST-1`'s **C4 has already shipped**; the capture graded it `NOT CARRIED` and
    called it the package's largest unexamined risk. C4 is one row of `ST-1`'s recommendation
    table, not its headline.
  - **Q4** — `ST-2` §*What was recommended, and what the owner ruled* records **Package C and
    four settled owner rulings**, which reframed Q4 from *whether to do this* to *how much
    lands this cycle*, and surfaced three recorded traps the capture's scope-cut framing
    walked into.

  That is **four instances across two runs** of the failure the platform finding names: *a
  study's index line names its headline cause, while a citing consumer's need is frequently
  one of its contributing factors — or one row of its recommendation table.* The fix direction
  stays as the platform finding states it (**read the studies whole**); widening it to a
  `causes:`-and-contributing-factors index was considered and **NOT ruled here** — the
  finding's own text puts that instrument on the far side of a cost problem that does not
  exist at three entries.
- **Q11 — A12-3's undeclared-location default.** Open to honest writes, or closed?
  Provisionally *open* by the `trust: raw` ruling; capture asks it be confirmed explicitly
  rather than defaulted into.

  **RULED Round 5 (2026-08-25): OPEN — the provisional is confirmed.** An undeclared PARA
  container is open to honest, attested `author: agent` / `trust: raw` writes; the honesty
  nets are the protection, not the declaration. `{wiki}`'s module-fixed floor (step 5) stays
  the **named exception** to that general case. Consequence recorded because it is the point:
  **no vault has to declare anything to get the fix's benefit** — which keeps `ST-2`'s
  acceptance test measuring *the change* rather than *vault adoption*.

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25) — Q11 becomes a RESOLVER, and its retroactive reach is
  stated.**
  - **A22/A23 — the open default is one arm of a total resolver, not a lookup.** Write posture
    at any PARA path = the `writers:` of its **nearest declaring ancestor**; absent any declaring
    ancestor, **`open`**. Two consequences ruled here *"because step 6 cannot be written without
    them"*: **(i)** a loose artifact at a layer root — **`{resources}/briefs/`, E5's own field
    pilot population** — resolves to `open` and **PASSES**; the resolver never joins against a
    charter that may not exist. **(ii) ⚠ NEW SCOPE — a declared posture BINDS its
    sub-containers**: an undeclared sub-container beneath a declaring parent **inherits** the
    parent's `writers:` and does **not** default to `open`, *"the alternative makes any closed
    posture unenforceable one directory down."* `{wiki}`'s floor is **outside the declaration
    system**, not absent from it — *"'no charter' reads as undeclared, and undeclared is now
    open."* *(Quinn, sharpened by Sally.)*
  - **A34 — the ruling is RETROACTIVE, and it inverts a live DECLINE+WATCH.** `writers:` is new
    schema, so **every charter that exists today is undeclared by construction** — and charters
    are human-gated, so the population being opened is *precisely the set a human deliberately
    framed*. **Nothing machine-reads a charter's prose**, so a charter saying *"human-maintained
    only"* in words is undeclared and therefore **open**.
    `factory/cycles/10-signal-integrity/roadmap.md:764` carries the
    **confidentiality-as-container-attribute** DECLINE+WATCH (Maya's dissent preserved at
    `:2719`) — and **E4 re-carried it "untouched, not re-graded" in the same session this ruling
    inverted its default posture.** The pair is **re-graded at brief time against the world
    A12-3 creates**, not re-carried untouched. *(Sally.)*
- **Q12 — A12-3 and the MOC prohibition** (`vault-operating-contract.md:190`). The filing
  recommends it survive as a **content-type** rule independent of zone posture, since it
  protects human *endorsement*, not human *territory*.

  **RULED Round 5 (2026-08-25): KEY IT ON CONTENT TYPE — NARROW IT NOW.** `:190` is restated
  as a rule about **MOCs as a content type**: partners never edit them because MOC links are
  human endorsement, **regardless of the container's `writers:` posture**. Rides A12-3's
  contract edit; no separate build.

  *Why now rather than when instances exist (clerk, Round 5 — the grounding the ruling was
  taken on):* **the prohibition has zero live instances in `{field-vault}`, and structurally
  cannot have any yet.** A MOC may only link `canonical` artifacts (`extraction.md:60`),
  `canonical` is human-set (`extraction.md:58`, `frontmatter.md:69`), and PARA is empty
  because of the very problem A12-3 fixes. The rule has never had anything to govern. It
  starts mattering **in the world A12-3 creates**.

  That is exactly why it is narrowed in the same build. After step 5 a container declares
  `writers:` and a MOC lives in a container — so **two rules would address one file**, and
  CLAUDE.md's *precedence by elimination* (Arc 9 D5) says to narrow one rule's population so
  the overlap ceases to exist, stating precedence only where elimination is impossible.
  Keying on content type **is** that narrowing, and it costs one clause in a build already
  editing the contract. Leaving `:190` unchanged is the branch that would later require a
  precedence statement — the outcome D5 exists to prevent.

  *(Considered and rejected: folding MOCs into `writers:` and retiring `:190`. Unlike the
  location proxy this cycle is retiring, **no shipped field carries the endorsement claim** —
  so the fold would make human endorsement a per-vault setting with nothing standing behind
  it, rather than retiring a redundant protection.)*
- **Q13 — `_vault/`'s disposition.** `vault-operating-contract.md:78` lists it human-only
  alongside `new/` and `daily/`; the owner's 2026-08-25 list named only `daily/`, `new/`,
  `sources/`.

  **RULED Round 5 (2026-08-25): `_vault/` STAYS HUMAN-ONLY — the omission was an oversight.**
  All three of `_vault/` / `new/` / `daily/` remain human-only exactly as
  `vault-operating-contract.md:76-80` already states. `_vault/` holds Obsidian Templater
  templates and human-facing config — tooling, not curated knowledge — and nothing in A12-3's
  case needs it opened. **No contract edit.**

  *Grounding correction on the other half of the discrepancy (clerk, Round 5): `sources/` was
  never an open question.* It is absent from the human-only list because it is not a
  human-only **folder** — it is **Layer 1, read-only for everyone**
  (`vault-operating-contract.md:62`, and `:68` states *"`sources/` is read-only"* separately
  from the human zones on the same line). The 2026-08-25 list and the contract therefore
  differed in only **one** place, not two, and that place is now ruled.

### Cross-filing decide-once rulings

Decisions that resolve the same question across filings identically.

- **D1 — A12-4 and A12-5 as one package, or split.** Capture: *"the same event seen from the
  two ends of one rail … both are #11. Both are answered by making a ruling carry a terminal
  obligation to the thing that asked — one to the tracker, one to the field. Ideation should
  consider them as one package before splitting them."*

  **RULED Round 3 (2026-08-25): ONE ITEM, RULED TOGETHER, BUILT SEPARATELY.** They are one
  obligation — *a ruling carries a terminal obligation to the thing that asked* — with the
  tracker half and the field half as separate builds on their separate channels (Q3). The
  joint stays visible for the roundtable rather than being dissolved by an early split.

  **Attached condition — the `P-N` carries a done-when PER MOVE, each with its own bound.**
  *(Clerk-flagged in the same round and owner-accepted; grounded in the channel contract,
  `factory/platform/roadmap.md:33-37`: each built-awaiting item must "name its discharging
  event and bound on its entry", and where the event cannot occur it is **BLOCKED
  (unreachable)**, not waiting.)* A single done-when reading *"both moves exercised"* would
  let A12-5's half — whose notice has no path to a vault that does not read this repo (see
  Q3's correction) — drag the whole item into BLOCKED, holding A12-4's fix, which has a
  perfectly reachable discharging event, behind it. **That is the very failure A12-4 files
  against: one signal carrying two questions.** So: A12-4's half discharges on a ruling
  reaching an issue as a comment; A12-5's half names the delivery question as its own
  precondition and bounds it.
- **D2 — P-15's retirement clause across this cycle's briefs.** P-15 (the retirement rail)
  is BUILT-awaiting and **self-accepts on this cycle**: on the roundtable running its
  obsolescence beat *and* this cycle's briefs carrying the retirement clause answered. Which
  builds carry it, and is the clause answered per build or once?

  **RULED Round 7 (2026-08-25): NO IDEATION RULING NEEDED — the shipped skill already decides
  it. EVERY brief carries the clause.** `.claude/skills/build-brief/SKILL.md:167-171` makes it
  a completeness condition: *"the prohibition this build's enforcement makes redundant, named
  with its site, or an explicit one-line `Retirement: not applicable`. **A blank is not an
  answer**; a build that ships a net without asking what it obsoletes is how the rule set only
  ever grows."*

  **What ideation does add — naming the marquee answer.** A12-3's build carries the
  *substantive* retirement disposition, and it is the one P-15's self-acceptance needs:
  **the Layer 3 location prohibition**, at `vault-operating-contract.md:68` and restated in
  `vault-rule-card.md:26`, made redundant by Cycle 11 build-6's `para_*` nets and retired by
  step 2 + step 6. A cycle whose every brief answered `not applicable` would satisfy P-15's
  letter and miss its point.

  **P-15's bound, flagged because it is tight:** *"If Cycle 12 reaches its roundtable without
  the beat present, or closes with the clause never asked, this is not a waiting state but
  **BLOCKED (unreachable)**"* (`factory/platform/roadmap.md` §P-15).

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25).**
  - **A25 — the marquee's site list is short by three, and one entry is a mis-cite.** The Layer-3
    prohibition is restated beyond `contract:68` + `rule-card:26` at: **`extraction.md:45`**
    (*"This does not add an artifact write-path. Artifacts reach PARA **only** through
    extraction"* — **inside the convention build-3 bumps**, on no site list anywhere in this
    roadmap); **`checks.md:16`'s own rationale** (*"outside the sanctioned surfaces"* — **the
    retired frame restated inside the enforcement that replaces it**, incoherent once no closed
    set of sanctioned surfaces exists); and the **surface-count** prohibition — *"exactly two
    named surfaces … never a third"* at `contract:66`, `vlt-extract:13`,
    `vlt-review-council:51`, `vlt-agent-creative:14`, `vlt-upgrade:159` — **which step 4
    literally falsifies by adding a third.** *"D2 names the **location** proxy; this is the
    **surface-count** proxy — it counts doorways where the other counted addresses."* **All
    retire or narrow together, or the prohibition survives in prose.**
    *(Mary/Winston/Victor/Quinn/Paige/John — the most-converged finding of the session.)*
  - **A19 — and one thing D2 must NOT gain: the `{wiki}` carve-out.** The room converged **4/4**
    that it is **not** retirable (see build-3's A19). *Mary's first-round beat grading is
    **withdrawn**, and her request to extend D2's list with `contract:70` withdrawn with it.*
    **Recorded in the roadmap's own words per Sally's ask: *Cycle 12 retires the Layer-3 location
    prohibition and does NOT retire the `{wiki}` carve-out*** — so a later cycle does not re-file
    it as a missed retirement, *"which is precisely the fifth-pass failure A12-3 exists to stop."*
  - **A48 — mark each retirement PRE-NAMED or BEAT-PRODUCED.** P-15's done-when asks only that
    the beat be *exercised*, and its tripwire counts *rules retired per cycle* — **so a cycle
    whose only retirement is the one ideation pre-named satisfies the letter and misses the
    point.** P-15's own stated risk is exactly this: *"the rail ships and never fires — added,
    then ignored, indistinguishable from working."* The review record marks which is which, and
    **P-15's self-acceptance names what it got.** *(Victor.)*
  - **A49 — 🔴 P-15 DOES NOT SELF-ACCEPT ON THIS SESSION.** Its done-when is *"Cycle 12's
    roundtable runs with the obsolescence beat exercised **AND** that cycle's briefs carry the
    retirement clause answered"* (`factory/platform/roadmap.md:146-147`). **The roundtable record
    is half the evidence, not the discharge.** *(Quinn; moderator verified.)*
  - **A50 — the tripwire has no recording site.** *"Rules retired per cycle, baseline zero"* is
    measurable nowhere: `roadmap-roundtable` records the beat in its own section only, and
    `cycle-closeout`'s Stage-2 categories and the platform visibility floor **name no retirement
    count**. *"A metric with no home is precisely `ST-4` root cause (d)'s shape."* **The cycle
    records its retirement count at closeout beside the visibility-floor line.** *(Quinn.)*
- **D3 — releases.** One release or more, and which builds ride which. Bears on A12-3's
  *rule ahead of mechanism* hazard above.

  **RULED Round 7 (2026-08-25): ONE RELEASE, WHOLE CYCLE.** One dual version bump, one
  `package-lint --expect-version` gate, one tag. A12-3's six steps ride it together per Q4, so
  the *rule ahead of mechanism* hazard does not arise at all — steps 2 and 6 co-ship and no
  interim posture is needed.

  *Consequence recorded, because Q8b turned on it:* this single release already carries
  A12-3's six steps, A12-1's symptom fix, A12-2's cause fix, Q6's `frontmatter.md`
  clarification, Q12's MOC narrowing, A11-2's three templates, A12-5's `vlt-feedback` prose,
  and A11-11 directions 1 + 2. **Release size was one of the three stated reasons direction 4
  is declared for Cycle 13 rather than built here.**

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25).**
  - **A11 — "the rest are independent" is FALSE. build-2 depends on build-3.** Build-3 bumps
    `extraction.md` 6 → 7 **and adds a lint check**, both of which change what a cached finding
    *means*. Ordering note becomes: **1 before 2; and 2's cache key must carry build-3's
    convention pins and check set** (A10). *(Quinn.)*
  - **A3 (John) — the release-size argument runs one way only.** Release size bounded direction 4
    **out** and bounded nothing **in**; the roadmap's own hazard note grades build-3 as *"the
    cycle's weight … in a release that also carries four other builds"*, which is over the line
    the argument drew, and **nothing tests it**. *Asymmetry acknowledged: if the one-tag load
    proves over the line at brief time, the cut point is **build-2** (independent of build-3's
    text, no shared file, no acceptance dependency) — never build-3's steps.* **Note build-4's
    move to platform (R-5) already reduces the tag by one build.**
  - **A51 — direction 2 RETIRES direction 4's own cost case, and Cycle 13 must not inherit the
    stale number.** `ST-3` prices the convention read at 8.6 MB/run — but **a cached page is not
    scanned, so its agent never runs and never reads a convention.** After direction 2 at
    `churn 5 of 146`, the pool is ~**0.29 MB/run** and direction 4's marginal saving ~**0.19
    MB/run**. Q8b's three reasons never include *"its value drops once direction 2 lands."*
    **Cycle 13 rules direction 4 on `ST-3` cause (a) — *projection binds every future fan-out
    consumer*, which survives direction 2 untouched — and re-measures the residual pool
    post-build-2.** *(Victor.)*
- **D4 — the "one signal carrying two questions" cause.** Capture grades it as arguably wider
  than A12-4 (it is A12-5's shape, and A12-2's) and opened no study. If it is ruled a
  cross-filing cause here, the disposition is a study, not a build — see E7.

  **RULED Round 8 (2026-08-25): NO `ST-4`. The test was RUN this session; its result and its
  third-instance trigger are recorded below.** This discharges E7 in the same ruling.

  **The test capture asked for, executed (clerk, Round 8 — all three studies read whole).**
  A12-5 measured against `ST-2` §RC2 and `ST-3` §Convergence:

  | | `ST-2` RC2 | A12-5 |
  |---|---|---|
  | subject | the **factory loop's input vocabulary** — nothing can express *"this protection is now redundant"* | a **vault's local record** whose premise was invalidated by an upstream ruling |
  | failure | the loop cannot **receive** a kind of news | the loop, having acted, does not **emit** the consequence to what was waiting |
  | fix | supersession filing class + roundtable beat + brief clause (**P-15**) | a ruling carries a terminal obligation to what asked (the new `P-N`, Q3/D1) |
  | actor | the factory, about itself | the ruling → the vault |

  **Finding: genuinely distinct.** The decisive check is that **each other's fix would not have
  caught it** — P-15's supersession class and obsolescence beat notify no parked vault record,
  and A12-5's re-derive-your-exit note does nothing for RC2. An input-vocabulary failure is not
  a propagation failure. **So A12-5 is NOT a fourth derivation of RC2 and is NOT appended to
  `ST-2`.**

  **But distinct does not earn a study.** `factory/studies/README.md` puts *a defect with a
  known fix* on the filing side, and A12-5's fix direction is known and bounded — both halves
  were ruled this session (Q7, D1). **No `ST-4` opens.**

  **Third-instance trigger, named so the finding is not lost:** `ST-4` opens if **A12-4's fix
  fails in the field**, or if **a second propagation failure appears** (a ruling that again
  leaves a waiting record wrong). At that point the analysis above is the opener's first
  paragraph rather than something to re-derive.

  **One narrowing of D4 as posed:** **A12-2 is dropped from the grouping.** Its shape is *two
  judgments holding duplicate jurisdiction over one question*, not *a record going stale on a
  ruling* — the capture's grouping was loose there. The candidate cause covers A12-4 and
  A12-5 only.

  **🔴 ROUNDTABLE AMENDMENTS (2026-08-25) — D4 IS RE-OPENED ON TWO GROUNDS.**
  - **A52 — the ruling declined the study on a criterion the register STRUCK.** D4 reads
    *"`factory/studies/README.md` puts **a defect with a known fix** on the filing side."*
    **The README says the opposite** *(moderator verified, `README.md:110-132`)*: *"The test is
    the **cause**, not the fix… A cause whose repair already shipped **still passes** if the
    answer is yes"*, and in bold: ***"Not `it reached its fix` — a shipped fix retires
    nothing."*** With the footnote: ***"(The bolded guard is here because this register's own
    build failed it: `ST-3` was excluded at back-fill as 'reached its fix' when its cause was
    live and deferred to the next cycle.)"*** And *"**A live diagnosis is never excluded.**
    Where the fix is deferred, unbuilt, or only partly shipped…"* — **A12-5's module-side fix is
    neither built nor scheduled**; it sits on an unopened platform item whose delivery
    precondition is itself unresolved (A45/A46). **Re-rule D4 on the register's actual
    cause-reusability test.** *(Quinn.)*
  - **A53 — 🔴 THE RESERVED ID IS TAKEN, and the study that took it reads THIS SESSION.**
    `factory/studies/ST-4-provenance-staffed-cognition-unstaffed.md` was opened **2026-08-25**,
    the same day, 25.2 KB, `cited_by: factory/platform/roadmap.md §P-16`. Its root cause **(d)**
    is *"the inbox uses **location as a proxy for lifecycle status**"* — **`ST-2`'s cause inside
    the factory, found during the cycle built to cure the module-side instance.** Its §Worked
    instance reads Cycle 12's ideation directly, including *"the single highest-stakes ruling in
    a cycle — what ships — was not ruled from the material; it was drafted by the clerk and
    adopted whole."* **The roadmap cites it nowhere.** Replace `ST-4` with **the next free
    `ST-N`** (ids are allocated once, never reused — `README:76-78`).
    *"This is the fifth instance of the failure the Platform finding names, and it is **not** an
    index-vs-whole-read miss this time — **the study did not exist when the check ran, and
    nothing re-ran it.** That is the honest answer to whether 'read the studies whole' is a
    sufficient control: **it is a control against a static register, and the register is not
    static.**"* *(Victor; moderator verified.)*
  - **A54 — the third-instance trigger cannot fire on the instance already on this roadmap.** It
    names only **outward** propagation (*"a ruling that again leaves a waiting record wrong"*),
    while **E8's Round-9 amendment records the reverse instance in the session's own room**.
    Widen to: *"a second instance of a decision taken from a record whose underlying fact had
    moved — **in either direction**. One is already on this roadmap (E8, Round 9)."* *(Quinn.)*

### Spikes

**The register is the record; this section is its view.** Mechanics:
`factory/platform/spikes/README.md`.

- **No register entry reads `proposed` or `running`.** Checked 2026-08-25 against
  `factory/platform/spikes/`: `S-1` (para-container-harvest) `consumed`, `S-2`
  (projection-baseline) `consumed`, `S-3` (github-notification-semantics) **`harvested`**.
  This batch inherits **no open spike**.
- `S-3` (github-notification-semantics) — **`harvested`, verdict `reshape`, `consumed_by: []`.**
  Listed because it is not open but is also not finished with: it was run in Cycle 11 so that
  **Cycle 12 briefs over a harvested spike**, and A11-2 + E4 — the item it was opened against
  — defer into this batch (Q8). `harvested` satisfies `build-brief`'s gate as it stands.
  **Ruling owed:** does the `reshape` verdict mean A11-2's brief proceeds on this harvest
  (and cites it into `consumed_by:`), or does the reshaped question need a **successor
  spike** with a new `S-N`?

  **RULED Round 7 (2026-08-25): NO SUCCESSOR. `S-3` harvested is the record; the reshaped
  residual becomes A11-2's ACCEPTANCE CHECK, field-contingent.** A11-2's brief cites `S-3`
  into its `consumed_by:` — the register file is updated in this session.

  *Grounding (clerk, Round 7 — `S-3` was read whole):* the harvest ran both legs (Tavily docs
  + live authenticated `gh` probes, read-only, no degradation) and **settled the semantics** —
  a repo watch notifies on third-party comments to non-participated issues under **All
  Activity** or **Custom→Issues** but not under *Participating and @mentions*; the permission
  model is **owner-only** except template-applied labels (filer-reachable at **creation**,
  never on an existing thread) and `@mentions`; and **no non-person mention target exists**
  (team mentions need an organization; the repo is under a personal account). The `reshape`
  verdict was recorded because the inherited bound — *a real observed notification settles
  it* — was **unmeetable**: no third-party event has ever occurred on the repo, and
  `/notifications` was scope-walled.

  **Two facts make the successor unnecessary.** (1) `S-3` says outright that the residual is
  *"no longer a read; it is an **act-and-observe** that coincides with A11-2's own acceptance
  evidence."* A spike reads an **external source** — the register's own boundary table — and
  an act-and-observe is not one; registering it would stretch `spike` past the line P-2 drew
  deliberately. (2) **The precondition is already satisfied**: `S-3`'s post-harvest addendum
  records that the owner flipped the repo watch to **All Activity** minutes after the harvest,
  clearing the `viewerSubscription: UNSUBSCRIBED` state the harvest surfaced.
- **Spikes this batch newly demands: NONE — ruled Round 7 (2026-08-25).** No item in the
  ruled batch turns on an **external** unknown. Two internal unknowns were checked against the
  register's boundary and are **not** spikes: **A12-1's cause-fix instrument** (a deterministic
  pre-pass over the module's own pages — internal, and declared for Cycle 13 per Q8b) and
  **direction 4's scanner-card design** (a question about this module's own conventions —
  internal, and the reason direction 4 gets its own cycle rather than a spike).
  One boundary already ruled by capture and recorded so it is not re-opened here: A12-5's
  *"how many parked interims exist across live vaults"* question is **not a spike** — it
  reads live vault content, not an external source (`factory/platform/spikes/README.md`'s
  boundary table). It is an owner-run field question, carried as E6 below.

**An owner ruling in this section is written back to the register file in the same session**
— status and `verdict:` live there, never only in roadmap prose.

**⚠ ROUNDTABLE AMENDMENT A59 (2026-08-25) — the spike register is clean, but the STUDY register
moved under this session and nothing re-read it.** `S-1`/`S-2` `consumed`, `S-3` `harvested`,
no open spike — all confirmed. **But `ST-4` was opened on 2026-08-25, after the capture's
grounding pass ran, and the roadmap cites it nowhere** (A53). *The spikes section checks its
register live; the studies were checked once, from a snapshot.* **Standing consequence for the
next capture and the next roundtable: the study register is re-read at the roundtable, not only
at capture** — *"it is a control against a static register, and the register is not static."*

### Evidence-debt dispositions

Each debt attached to a build, or ruled not-blocking, per build.

- **E1 — the six released field-tail standing watches** (carry-in 1): b2(2) `resources/`-write
  legality from the bundle *(see Q9 — its premise may be obsoleted by A12-3)*; b3(3) the
  decision log's new routes used live; b4(2) the false-fire window at run 1 of 2; b5(2) a live
  council lens-shortfall end-to-end; b6(3) the resolution half of the caught draft-night
  instance; b9(3) the first live `frontmatter_key_count` declaration (B10-4(4) parts 2–3 ride
  it).

  **RULED Round 8 (2026-08-25): RE-CARRY ALL FIVE, EACH STAMPED WITH ITS TRIGGERING EVENT IN
  PLAIN LANGUAGE.** b2(2) is retired separately by Q9. None of the five events has fired;
  they are re-listed as released watches, and they are re-listed **readable**:

  | watch | its triggering event, stated plainly |
  |---|---|
  | **b3(3)** | a live vault actually uses the decision log's new routes (a rostered `vlt-ingest` write-through entry and/or a `kind: deviation` supersession read clean by the next reconcile) |
  | **b4(2)** | the retuned signal survives a second post-upgrade `vlt-lint` without false-firing — **run 1 of 2 is clean**; the trigger is the owner's second post-upgrade lint |
  | **b5(2)** | a real council session surfaces a lens shortfall end-to-end |
  | **b6(3)** | the vault states its legal response (overlay-declare / retype / relocate) to the draft-night instance build-6 already caught — the **resolution** half |
  | **b9(3)** | the first live `frontmatter_key_count` declaration by a vault (B10-4(4) parts 2–3 ride it) |

  *Why the stamping, on the record:* this is Q2's lesson applied prospectively. `B5-3(2)` was
  carried five cycles as the bare token *"B5-3..B5-9"*, and grading it this session required
  reconstructing its three legs from a 2026-07-29 brief. **A watch nobody can read is a watch
  nobody can discharge.** One line each is the whole cost.
- **E2 — build-8's `overlay_rules_review` tail** (carry-in 2): A11-5's live exercise,
  unbounded by construction (a fault-shaped event nothing schedules).

  **RULED Round 8 (2026-08-25): RE-CARRY, STAMPED (E1's treatment).** *Triggering event,
  plainly:* **the first relocation migration in a live vault that actually renders
  `overlay_rules_review:` with a real hit.** Unbounded by construction — nothing schedules a
  fault — so it is re-carried as a released watch and is **not** owed a bound.
- **E3 — `B5-3(2)`, called out of the E8 register by name because its event has fired.**
  Disposition is Q2's ruling; the ledger entry follows it.

  **DISCHARGED Round 2 (2026-08-25) — no carry.** Q2 graded all three legs against the live
  reports and discharged the clause on its letter; the grading table there **is** the
  discharge record. `B5-3(2)` leaves the E8 register and is not re-listed. **First of this
  cycle's two retirements-rather-than-carries** (with b2(2), Q9).
- **E4 — the E8 inherited registers, unchanged** (carry-in 5): C6-c, B5-3..B5-9, the
  pre-Arc-5 and Arc-7 registers, Arc 9 item-6 watches, Cycle-10 released watches (B10-7(4),
  B10-8(4), B10-8(5), B10-9(3) remainder), and the DECLINE+WATCH pair. Re-carry, or grade any
  of them here.

  **RULED Round 8 (2026-08-25): RE-CARRY UNCHANGED — with one subtraction, recorded so the
  register is honest.** `B5-3(2)` is **removed** from the `B5-3..B5-9` token per Q2/E3; the
  token now covers `B5-4..B5-9` and must be written that way rather than carried as the old
  string. Everything else — C6-c, the pre-Arc-5 and Arc-7 registers, Arc 9 item-6 watches, the
  Cycle-10 released watches (B10-7(4), B10-8(4), B10-8(5), B10-9(3) remainder) and the
  DECLINE+WATCH pair — re-carries untouched, not re-graded here.

  *Standing note for the next capture, from this session's experience:* the register is
  carried as opaque tokens, and grading one of them (`B5-3(2)`) required reconstructing its
  criteria from a 2026-07-29 brief. E1's stamping treatment is the fix; applying it to this
  register is **not** ruled here (it is a larger pass), but it is named as a candidate.

  **⚠ ROUNDTABLE AMENDMENT A58 (2026-08-25) — the one concrete act this ruling creates is
  assigned to nobody.** The token rewrite (`B5-3..B5-9` → **`B5-4..B5-9`**) appears in **no
  owner-action list**, and the register is carried by `cycle-closeout`'s carry-forward record and
  by project memory, neither of which this roadmap instructs. *"Q2 closed a five-cycle carry that
  survived precisely because a token got copied forward unread; leaving the corrected token
  untracked **reproduces the mechanism in the same session that diagnosed it**."* **Added to the
  owner actions, at closeout.** *(John.)*
- **E5 — A12-3's acceptance instrument, already fixed by the filing and recorded so briefing
  does not re-invent it:** *`trust: raw` is currently unrepresentable in PARA; if no `raw`
  content appears there after the entry-condition change, the change did not take* —
  regardless of contract text. Field pilot: `vlt-brief`'s next scheduled issue files to
  `{resources}/briefs/` at honest `author: agent` / `trust: raw`, no relabeling, no
  pointer-container indirection, no bespoke carve-out. Attach to which build, and is it
  blocking?

  **RULED Round 8 (2026-08-25): ATTACHED TO A12-3's BUILD — `[field-contingent]`, NON-GATING.**
  The instrument needs a live `vlt-brief` run in a field vault, which nothing this cycle
  schedules; tagging it ship-verifiable would make it gate on an event the cycle cannot cause,
  which is the false-green this module files against.

  **It is paired, not orphaned.** A12-3's gating half is **ship-verifiable and lands in the
  same build**: the six steps' text at rest (contract, `extraction.md` 6 → 7 with its three
  re-acks, the `writers:` schema, the retired `≥2 wiki pages` gate at all three sites, the
  MOC narrowing) **plus step 6's authorization check firing correctly at rest on a fixture**.
  That is what gates closeout; the `trust: raw` appearance is what proves it took.

  *Recorded against the filing's request that retiring a load-bearing rule GATE closeout (the
  A4-4(5) lesson): the request is honoured by the ship-verifiable half, not by mis-tagging the
  field half.* Per-check tagging remains `build-brief` §9's at brief time.

  **🔴 ROUNDTABLE AMENDMENTS (2026-08-25) — THE GATING INSTRUMENT DOES NOT EXIST AS NAMED.**
  - **A55 — "at rest on a fixture" names a fixture nothing creates.** The repo has **exactly one**
    fixture harness — `tools/test-package-lint.py`, whose `build_fixture` (`:58`) synthesizes a
    **module package** tree (`module.yaml`, the contract's pipe table, `CSV_ROWS`,
    `FIXTURE_STRUCTURE`). **No vault, no PARA container, no `writers:` charter, no wiki page.**
    Step 6 is **LLM-executed prose** in `checks.md`, and **nothing in `tools/` executes
    `checks.md`**. `package-lint.py:57-59` states E4's rule — *"a gate check with no fixture case
    is itself a lint failure"* — but it **introspects callables in `package-lint.py`**, so a
    `checks.md` rule is **outside E4 by construction**. And `ls skills/vlt-lint/` → `SKILL.md` +
    `references/` only, **no `scripts/`**. **Precedent that this rots silently:**
    `factory/cycles/06-factory-honest-surface/filings/2026-08-01-143000-lint-fixture-stale-against-three-builds.md`
    — *three builds widened the lint without widening the fixture and the harness was red for
    three builds.* **Brief-time ruling required: (a) express the authorization check as a
    `package-lint` callable so E4 forces a case, or (b) name the concrete artifact. Absent both,
    E5's gating half is re-tagged `[field-contingent]` and A12-3 gates on the text-at-rest half
    alone.** *(Amelia + Mary.)*
  - **A17 (carried) — the gating half now REQUIRES an ordinary run.** Per owner ruling R-1, the
    ship-verifiable half becomes *"a `para_*` finding produced by an **ordinary `vlt-lint` run**
    over a fixture vault — **not by direct check invocation**"*, because a fixture that invokes
    the check directly **passes with the file-selection path still missing**. *"The gate cannot
    see its own hole."* *(Winston.)*
  - **A18 (carried) — the failure reading gains a third outcome.** Not only *`raw` appears* vs
    *nothing appears*, but ***`raw` appears and `author:` is falsified*** — because the nets
    judge field presence and enum membership, never truth. *(Quinn.)*
- **E6 — the parked-interim survey** (A12-5's carried open question): *how many parked
  interims exist across live vaults, and were any others invalidated by Cycle 11's rulings
  without anyone noticing?* The mechanism **guarantees silence**, so absence of reports is
  not evidence of absence. Owner-run instrument named by capture: a look at `{field-vault}`'s
  mint decision log and any parked-interim records. Not a spike (see above). Scheduled, or
  ruled not-blocking?

  **RULED Round 8 (2026-08-25): SCHEDULED AS AN OWNER TASK, NON-BLOCKING.** The owner runs it
  against `{field-vault}`'s mint decision log and any parked-interim records — the instrument
  capture named. Findings **file forward as new filings**; they do not gate this cycle, and
  they do not gate A12-5's `vlt-feedback` build (which is written against the one observed
  instance and the mechanism, not against a count).

  *Carried with capture's caveat intact: the mechanism **guarantees silence**, so a null
  result is not evidence of absence — it is one vault reporting nothing, which is what the
  mechanism produces either way.*

  **⚠ ROUNDTABLE AMENDMENTS (2026-08-25).**
  - **A56 — an owner task with no bound, no date, and a caveat that pre-invalidates its likely
    result is the shape of a thing that never happens.** *"Worse than unreadable — it is
    **unfalsifiable as written**, so even running it produces no state change."* Compare E1's own
    ruling in this section, which exists **because** unreadable carries rot. **Bound: run it
    before Cycle 13's `inbox-capture`, or it is DROPPED rather than re-carried.** And because
    the null result is uninformative, **the output is not a count but a list of every parked
    record found and the ruling each rests on** — *zero records found* and *zero rulings checked*
    are different results, and only the second is a null. *(John.)*
  - **A57 — the one vault we can name gets nothing, twice.** The observed instance is
    `{field-vault}` parking partner output in `_agent/` **because PARA was illegal** — and
    **build-3 is the ruling that makes it legal, invalidating that record a second time**, with
    no comment thread open on it this time. E6 is non-blocking, build-5 is prospective, and the
    module-side notice is blocked (A46). *"Three fixes for one defect, none of which reaches the
    one instance we can name."* **Owner action added: when build-3 ships, hand-deliver the
    re-derive notice to `{field-vault}`'s known PARA park — the same act as the 17:06Z comment on
    #11.** *"One known instance is not a population, and a hand-run notice is not a mechanism; it
    is what the cycle owes the vault whose filing it is built on."* *(Sally.)*
- **E7 — the `ST-4` opening test** (P-14 territory, capture's own rule for this cycle): an
  `ST-4` is opened **only after A12-5 has been read against `ST-2` §RC2 and `ST-3`
  §Convergence and found genuinely distinct** — otherwise the finding is appended to `ST-2`
  as a fourth derivation. Who runs the test and when?

  **DISCHARGED Round 8 (2026-08-25) — the clerk ran it in session; see D4 for the comparison
  table, the finding (genuinely distinct from RC2), the disposition (**no `ST-4`** — known
  bounded fix puts it on the filing side) and the named third-instance trigger. Nothing
  carries forward.**
- **E8 — the immediate close of tracker #11**, owner's and unblocked by any ruling above:
  close with the ruling text, noting the ruling changed the boundary without opening the
  folder and that the filer's operation is carried forward in A12-3. **Ordering interaction:
  if #11 closes now and A12-3 ships, the filer's actual need is answered by a *different*
  issue's build — say so in the close comment.**

  ~~**RULED Round 8 (2026-08-25): DO IT — owner's act, unblocked by every ruling above, and
  not waiting on any build.** Close **#11** with the ruling text.~~ **STRICKEN AND AMENDED
  Round 9 (2026-08-25) — see below. #11 is NOT closed.**

  **AMENDED RULING (Round 9, 2026-08-25): #11 STAYS OPEN. The answer was already delivered
  by comment, and closing would break the shipped mirror rule.**

  **⚠ THE ROUND-8 RULING WAS TAKEN ON STALE OBSERVATION — recorded because the failure is
  this cycle's own subject.** The capture wrote *"#11 open … **zero comments**"*, verified live
  on the morning of 2026-08-25. It was true when written. **At 17:06Z the same day the owner
  commented on #11**, and Round 8 was posed and ruled from the capture's observation without
  re-checking the live tracker — a one-command check. **An ideation round used a proxy (the
  capture's record of tracker state) for a fact that had moved underneath it**, which is
  precisely A12-4's shape and this cycle's through-line, committed by the session ruling on it.

  **What the owner's comment already contains** (`#11`, comment
  `5413941209`, 2026-08-25T17:06:42Z) — substantially everything E8 asked to put in a *close*
  comment, minus the close:
  - the shipped ruling — v0.15.0 / Cycle 11 build-2, *"`resources/` gains PARA parity … the
    write-posture gap neither rule reached **closes by grant**"*;
  - **the re-read notice**, which is A12-5's fix performed by hand: *"the ruling re-read the
    question. It was filed as a question about **which zone** is writable and was answered as
    a question about **which surface**. An exit condition written against the zone reading is
    therefore not merely unmet — it is **invalid**. Re-derive any parked unwind against the
    shipped contract rather than replaying a pre-authorized sequence."*;
  - an explicit *"This issue **stays open on purpose** … Open here means **acceptance
    outstanding**, not **unanswered**"*;
  - and the statement that the structural question is **not** resolved by that ruling and is
    captured as **A12-3**.

  **Why staying open is correct, not merely the owner's preference.** The mirror rule is
  shipped: `.claude/skills/cycle-closeout/references/closeout-checklist.md:155-157` — *"A
  filing that **stays active** … leaves its issue **open** — the tracker mirrors the inbox, in
  both directions."* Filing `2026-08-24-142828` remains in the active inbox, so **closing #11
  would violate the rule**, not merely pre-empt it. The owner supplied the missing *answered*
  signal by **comment**, leaving the mirror honest — which is exactly the shape A12-4's
  surviving candidate proposes (*bind at ruling; the release comments the ruling text onto the
  issue*).

  **One binding did move, and the comment predates it.** The comment gives the reason for
  staying open as the live carry-forward **`b2(2)`**. Later the same session **Q9 retired
  `b2(2)`** into A12-3's acceptance. #11 still stays open under the mirror rule, but its
  binding is now **A12-3's acceptance**, not `b2(2)`'s watch. No tracker action follows from
  this; it is recorded so a future reader does not resolve #11 against a retired watch.

  **Carried into the new `P-N` as evidence:** the 17:06Z comment is a **live, hand-executed
  instance of A12-4's fix working** — the answered signal delivered without touching issue
  state. The `P-N`'s brief-lite cites it rather than reasoning from the defect alone.

  *Owner action remaining: none on #11.* Its close comes at closeout, when its filing archives
  against A12-3's acceptance.

### Questions deliberately left to brief time

Per-build, not cross-cutting. Seeded from the filings' carried-verbatim open questions; the
owner may promote any of these into a ruling above instead.

- **A12-3 — ship-verifiable vs field-contingent tagging.** The filing asks that retiring a
  load-bearing rule **gate** closeout (the A4-4(5) lesson, applied preemptively as in Cycle
  11's Round 5). Capture flags this as the right instinct and leaves the tag to brief time
  (`build-brief` §9). — *(brief-time)*
- **A12-1 — the two extraction defects are distinct and a code-span exclusion fixes only
  one.** (1) code-span inclusion, 9 of 10 flags; (2) non-wikilink text matched as a link,
  the 10th flag — needs the **shape predicate**. Whichever fix Q1 rules, the brief states
  both clauses at `vlt-lint-full.js:143` and `:202`. — *(brief-time)*
- *(add per-build brief-time questions as rounds surface them)*

## Roundtable review — A12-1..A12-5 + the Cycle-11 deferrals (2026-08-25)

**Convened** `roadmap-roundtable` over the filled Ideation rulings, before any brief. Roster
discovered fresh (`.claude/skills/bmad-agent-*` + `bmad-cis-agent-*` — 13 installed); the owner
seated **nine** and excused four (Carson, Maya, Caravaggio, Sophia). Room: **Mary** (analyst),
**Winston** (architect), **Amelia** (dev), **John** (PM), **Paige** (tech writer), **Sally** (UX),
the **agent-builder**, **Dr. Quinn** (problem-solving), **Victor** (innovation strategy).

**Owner's steer, carried verbatim into every persona prompt:** *"The four overturned claims. ST-1's
C4 already shipped, Q6 is a clarification not a rule change, A12-1's cause fix needs a new
instrument, CHANGELOG has no vault delivery path. **Re-test whether the corrections themselves
hold.**"*

**Verdict on the steer: all four corrections HOLD as facts. Three are incomplete as rulings.**
C4's *field* shipped but its **regime** was never relieved (A30). Q6 is a clarification but is
**homed in the file that disclaims owning scope rules** (R-2/A8). The CHANGELOG has no vault path —
and **neither do both of the fallbacks the ruling left open** (A45/A46). A12-1's instrument
correction holds on every clause; it **overreaches by one notch** — the SKILL does have filesystem
access and already runs three pre-passes of that class, so what Cycle 13 owes is **determinism**,
not a home (A6/Amelia). **A fifth capture claim was overturned in-session:** step 5's *module-fixed
`{wiki}` floor* is **already shipped** at `vault-operating-contract.md:64` (A20).

**Session file:** `_output/party-mode/2026-08-25-cycle12-roadmap-roundtable-session.md`.
**Keepsake:** `_output/party-mode/2026-08-25-cycle12-roadmap-roundtable.html`.

### Owner rulings taken live

| # | ruling | dissent on record |
|---|---|---|
| **R-1** | **Build-3 gains a step 0** — build the `para_*` file-selection path. E5's ship-verifiable half becomes *a finding from an ordinary `vlt-lint` run*, not direct check invocation | none — Winston's finding, moderator-verified |
| **R-2** | **Q6's clause moves to `write-verification.md` §Scope rule.** No-bump grading stands and gets cheaper (v3/5 consumers vs v13/9) | **Winston, Amelia** — each re-tested and confirmed the Round-6 ruling holds *as written*; they lose on **home**, not on **grade** |
| **R-3** | **`key_claims`: DROP the field**, do not gate — gating is sampling, forbidden by `ST-3`'s standing anti-direction | **Amelia, Victor** — would gate the cluster and drop the live re-read instead |
| **R-4** | **build-4 keeps a filer-side residue**; the watch is a declared external dependency with a named silent-failure mode | **Amelia, Sally** — each graded the `@mention` a clean retirement. **Quinn's caveat binds either way: the `amended` label gate must survive** |
| **R-5** | **build-4 moves to the platform channel** — `.github/` is never delivered to vaults, so the cycle's own boundary rule makes it platform. **Cycle 12 is four builds** | none |
| **R-6** | **The `{wiki}` carve-out — REMITTED to the room**, owner's gut with Mary+Sally, *"debate until consensus"* | see below |

### R-6 — the remitted dispute, converged 4/4

**Both voices holding the owner's lean withdrew, on evidence they went and found themselves.**

- **Mary conceded on a commit.** `git log -S "carve-out by name"` → **one commit, `8290416`,
  Cycle 11 build-2, 2026-08-24** — the carve-out was authored **in the same hunk that widened
  Layer 3 over `{resources}`**. *"Build-2 could have written a precedence statement. It didn't.
  It narrowed the population by name. **The carve-out is already an act of D5 elimination. Step 5
  reverses it.**"* She read the B9-1 precedent nobody had opened: the sentence *"is elimination's
  **output**, not an overlap awaiting one."* **Her first-round beat grading and her D2 request are
  withdrawn.**
- **Sally conceded with the argument that finished her own side off.** `{wiki}` lives
  **geographically inside** `{resources}` and the general mechanism is **location**, so *"the
  carve-out is the only thing preventing the general rule from reaching a subtree it physically
  contains."* And the regression nobody had named: under **Q11**, dissolving `{wiki}` into *a
  container with no charter* drops it into the **open** default — *"**my own position, executed,
  breaks the single-writer wiki. I withdraw it.**"*
- **Winston sharpened, conceding the end-state:** *"I was defending the **word** 'carve-out' as if
  it were the rule. It isn't."* And on Sally's case: *"Today 'Librarian-only' is unenforced prose.
  **Her position buys real enforcement; my original position bought nothing. That is the part of
  this I got wrong.**"*
- **Quinn withdrew the objection as stated and inverted the finding.** Two questions were fused
  into one word — `extraction.md:148` answers **membership**, step 5 asks **posture**. Separated
  (TRIZ, by reader), the contradiction dissolves. And: *"Sally called it friction with no
  protective value. Under the resolver it is **the opposite of both** — because `{wiki}` can carry
  no charter, **the classification is what makes the Librarian floor unoverridable. It is a
  lock**, read by nobody at act time and paid for by nobody."*

**Consensus:** the carve-out is **not retired** (A19); step 5's retirement claim and its
already-shipped floor half are **struck** (A19/A20); **the friction Sally named is real and is a
restatement problem** — ten sites reduce to a canonical home plus pointers, a scope *narrowing*
(A21); **`checks.md:18` is exempt** and keeps its self-contained population sentence (Sally's
B10-12 argument, over Quinn's pointer proposal); **step 6 gains an explicit resolution order**
(A22) and **Q11 gains an inheritance rule that is genuinely new scope** (A23).
**Open sub-question left to brief time rather than manufactured into a ruling:** the canonical home
— `contract:64` (Mary, Sally) or `extraction.md:148` (Quinn).
**Falsifiers on record**, so the consensus is checkable: Winston's (*exhibit a rule excluding
`resources/wiki/foo.md` without naming it*), Quinn's (*find a site that must branch on
`{wiki}`-is-not-a-container to decide a **write permission***), Sally's (*collapse ten sites to one
home plus pointers with no `vlt-lint` verdict changing on any fixture*).

### Amendments applied — A1..A59, each at the section it amends

**build-1** A1 (cites are v0.14.0 vintage; `pageScanPrompt` is one block at `:200-202`) · **A2 🔴
hard release gate — `PAGE_SCAN` 3223 vs E6's 3700 cap, 477 chars of headroom** · A3 (cite
`frontmatter.md:37`, don't restate — *the DQL pages were complying*) · A4 (`:202` = 40% of the
prompt restating the schema, 166 KB/run) · A5 (drop `key_claims`) · A6 (the reorder may be a
no-op — 550 tokens vs a 1,024–2,048 cache floor) · A7 (the `wiki-index@2` pin stays) · A8 (Q6
rehomed) · A9 (`per frontmatter@13` marker).
**build-2** A10 (**cache key — five independent hits**) · A11 (not independent of build-3) · A12
(ship-verifiable two-run fixture) · A13 (derive-first boundary, `contract:349`) · A14
(`checks.md:49` owes a narrowing — *Mary dissents*) · A15 (`lint-debt`'s premise) · A16
(`coverage_caps` not retired).
**build-3** **A17 🔴 step 0** · A18 (presence ≠ truth) · **A19 the carve-out is not retired** ·
**A20 fifth overturned claim** · A21 (single-home the ten sites) · A22 (step 6 resolution order) ·
A23 (inheritance — new scope) · A24 (restatement list wrong three ways) · A25 (**three retirement
sites D2 missed**) · A26 (`vlt-query` undeclared consumer) · A27 (**live sha256 on the rule card**)
· A28 (card becomes a test, not a list) · A29 (`moc` must be a readable type) · A30 (**Q5 is not
closed**) · A31 (`writers:` may cost `frontmatter.md` 13→14) · A32 (a fourth ack if step 0/6 reach
the workflow) · A33 (**no vault-facing surface announces any of this**) · A34 (Q11 is retroactive;
DECLINE+WATCH inverted) · A35 (`{archive}` posture — brief-time).
**build-4 → platform** A41 (`@mention` retires, label gate must not) · A42 (no `rail_contract`
bump) · A43 (single home never learns) · A44 (invisible to skill-filers) · bound + BLOCKED grade.
**build-5** A36 (needs an artifact) · A37 (nothing re-reads it) · A38 (state the population) ·
A39 (`vlt-mint:104` is the second population) · A40 (one prohibition added, none retired).
**Rulings** A45/A46/A47 (Q3 — mis-cite, closed key set, **`P-16` is taken → `P-17`**) · A48/A49/A50
(D2 — pre-named vs beat-produced; **P-15 does not self-accept here**; the tripwire has no home) ·
A51 (D3 — direction 2 retires direction 4's cost case) · A52/A53/A54 (D4 — **struck criterion**,
**`ST-4` id taken**, trigger widened) · A55 (E5 — **the fixture does not exist**) · A56/A57 (E6 —
bound; the known vault gets nothing twice) · A58 (E4 — token rewrite assigned to nobody) · A59
(Spikes — the study register moved under the session).

### Standing rules adopted, with named homes

- **R-A — the study register is re-read at the roundtable, not only at capture.** Home:
  `.claude/skills/roadmap-roundtable/SKILL.md` (Convene). *Interim posture: recorded here as a
  dated declaration and honoured in this session; the skill edit is platform work and is queued,
  not built this cycle.* Cause: `ST-4` opened mid-cycle and no check re-ran (A53/A59).
- **R-B — a retirement finding is marked *pre-named* or *beat-produced*.** Home:
  `.claude/skills/roadmap-roundtable/SKILL.md` (Converge, the record's obsolescence line).
  *Interim posture: this record marks them (below).* Cause: P-15 would otherwise self-accept
  against its own input (A48).
- **R-C — a cycle records its retirement count at closeout.** Home:
  `.claude/skills/cycle-closeout/references/closeout-checklist.md` (Stage 2, beside the platform
  visibility floor). *Interim posture: declared here; the edit rides the same platform item.*
  Cause: P-15's tripwire is unmeasurable (A50).
- **R-D — "declared for cycle N+1" is a Stage-2 carry-forward category, or it is not a grade.**
  Home: `closeout-checklist.md:61-68`. *Interim posture: this roadmap records both declared items
  explicitly under Owner actions.* Cause: *"anything left off is silently dropped"* (`:75`) — the
  exact mechanism the grade was invented to prevent (Quinn, A8-lens).

### Obsolescence beat — the outcome (P-15's required record)

**Run by all nine voices; every one returned an explicit per-build answer. The beat FIRED.**

| build | retirement | pre-named or beat-produced |
|---|---|---|
| **1** | the model-side attestation clauses (`vlt-lint-full.js:144`/`:153`/`:201-202`) superseded by the deterministic `attested` check at **`:482`**, census `:483-491` | **beat-produced** |
| **2** | `checks.md:10`'s **attestation-freshness re-scoping rule + its 1-in-5 sample audit** — attestation freshness is a *proxy* for "unchanged since last judged"; the cache measures it **directly** | **beat-produced** *(Winston; Paige converged via `checks.md:49`. **Mary dissents** — reads both as surviving)* |
| **3** | the **Layer-3 location prohibition** (`contract:68` + `rule-card:26`) | **pre-named** (D2) |
| **3** | **`extraction.md:45`** — *"This does not add an artifact write-path"*, inside the bumped convention | **beat-produced** *(4 voices)* |
| **3** | **`checks.md:16`'s rationale** — the retired frame restated **inside the enforcement that replaces it** | **beat-produced** *(3 voices)* |
| **3** | the **surface-count prohibition** — *"exactly two named surfaces … never a third"*, which step 4 **literally falsifies** | **beat-produced** *(Paige, Victor)* |
| **3** | the **`≥2 wiki pages` gate**, 4 sites | pre-named as scope; *Quinn's dissent, recorded: "**not** an obsolescence finding — prose-only ceremony with no mechanism ever standing behind it. It is retired because it never earned its place."* |
| **4** *(now platform)* | the filer-side **`@mention` requirement** — the module's first retirement of a **personal-handle dependency**; the `amended` label gate **survives** | **beat-produced** |
| **5** | **none found** — and **one prohibition ADDED with no counterpart withdrawn**, entered as such rather than as `not applicable` | — |

**Beat-produced retirements this cycle: six.** D2 carried **one**. *"A cycle whose only retirement
is pre-named exercises the clause and not the beat"* — this one exercised the beat.
**A retirement REFUSED, and the refusal is part of the record:** the **`{wiki}` carve-out**, 4/4,
after the owner's own lean went the other way. *"A beat that only ever retires is as wrong as one
that never does; this cycle has one of each, which is the honest outcome."* (Amelia)

### Out-of-scope material for `factory/inbox/` (capture-don't-interrupt)

1. **`supersession` filing — `checks.md:10`'s attestation-freshness re-scoping rule** vs direction
   2's change key (two skip mechanisms, one population, different criteria; Mary dissents).
2. **Defect — `vlt-lint` has no PARA jurisdiction scan** while `vlt-lint-full.js:517-519` and four
   report slots assume one. *Folded into build-3 step 0 by R-1; file only if step 0 is descoped.*
3. **Defect — `ST-1`'s C5 has no shipped check** (*lint catches non-wiki `sources:` entries*),
   leaving the honesty nets unable to judge field truth (A18).
4. **Pattern — the loop's line-number cites go stale silently.** Two v0.14.0 cites survived a
   capture and nine ideation rounds (A1/A4). Candidate: cites re-verified at brief time.
5. **Candidate — `.github/` has no row in the platform boundary table** (R-5).

### Routing at the close of review (2026-08-25 — historical; DISCHARGED by build-1's brief)

*This is the roundtable's own exit routing, kept as part of its record. **It is not the file's
authoritative next move** — that is the single terminal `## Next lifecycle move` block at the
foot of this file, per the lifecycle map's standing rule that a report's terminal routing line
is authoritative. Restamped by `build-brief` on 2026-08-25 when build-1's brief landed; the
duplicate terminal block this file used to carry (still routing to the roundtable that had
already run) was collapsed into that one block in the same run.*

**`brief build 1`** (`build-brief`) — the record is in place and **there are no OPEN disputes**;
R-6 converged 4/4 and R-1..R-5 are owner-ruled. Order: **1 → 3 → 2** (build-2 now queues behind
both, A11). **Before the first brief lands, note A55: `build-brief`'s exit gate appends to a
`## Deferred acceptance ledger` that did not exist — it is added below.**

## Deferred acceptance ledger

*Per-build `- [ ] **build-N (<slug>, briefed <date>):** …` bullets, appended by `build-brief`;
form per `factory/cycles/11-reachability/roadmap.md` §Deferred acceptance ledger. Added at the
roundtable (A55/Quinn) — the section was missing and every brief this cycle would have gated
against it.*

- [ ] **build-1 (page-scanner-corrections, briefed 2026-08-25):** brief
  `factory/cycles/12-proxy-claims/briefs/build-1-page-scanner-corrections.md`. Six checks —
  three ship-verifiable (all gate), three field-contingent (none gate).
  **(1) `[ship-verifiable]` — GATES closeout:** `JSON.stringify(PAGE_SCAN).length ≤ 3700`
  after the edits (A2's hard release gate) — instrument: package-lint **Group E6**
  (`tools/package-lint.py:900`, the node-subprocess measurement), run at rest; baseline
  measured this session **3223** at HEAD, **3081** once `key_claims` is dropped, so the new
  clauses spend against 619 chars; evidence: the four schema lengths + the Group E PASS line
  recorded in the brief's BUILT `status:`.
  **(2) `[ship-verifiable]` — GATES closeout:** the narrowed extraction holds on a page built
  to break it — given the edited `pageScanPrompt` + `PAGE_SCAN`, a scanner returns **exactly**
  the two genuine wikilinks (fenced DQL, code-span `![[File.base]]` embeds, code-span table
  cells and a bare source filename in a `## Sources` list all contribute **zero**),
  `frontmatter_valid: true` on an unattested-but-valid page, no attestation complaint in
  `unmarked_supersession`, and all 14 required fields populated (A4's reduction guard) —
  instrument: the brief's Verification-3 single-agent reader probe (haiku, matching `:94`)
  against a temp fixture, factory-side and at rest; evidence: the returned JSON recorded
  verbatim in the BUILT `status:`.
  **(3) `[ship-verifiable]` — GATES closeout:** the waste is gone and the handshake survived
  it — `key_claims` absent from `:155` **and** the cluster prompt; `convRead('wiki-index')`
  absent from `pageScanPrompt` while `wiki-index@2` stays pinned at `:11` and
  `wiki-index.md:12` still lists `vlt-lint-full.js` (A7); `:202` reduced (A4);
  `write-verification.md` still `version: 3` / 5 consumers — **no bump, no re-ack** (Q6, R-2)
  — instrument: the brief's Verification-4 fan-out audit (the workflow's own R4 rule at
  `:16-21`) + the Verification-7 greps + package-lint Groups A/B/C/E; evidence: the recorded
  audit result, grep outputs and PASS line.
  **(4) `[field-contingent]` — does not gate:** the next real full lint reports **zero**
  `missing_targets` entries sourced from a code span or from bare non-wikilink text, against
  the corpus that produced ten of ten false flags on 2026-08-24 — event: the owner runs
  `vlt-lint --full` on `{field-vault}` after upgrading it to this cycle's release; performer:
  the owner (standing rule); vault: `{field-vault}` only — it is the sole install carrying the
  obsidian-dataview/obsidian-bases pages that produce the class; bound: the first full lint
  after the release, no later than Cycle 13's `inbox-capture`.
  **(5) `[field-contingent]` — does not gate:** on that same run, a page missing
  `verified_by:`/`verified_at:` appears in the attestation slots (`unattested_write` /
  `attestation_census`) and **not** in `malformed_frontmatter` and **not** in
  `unmarked_supersessions`, and the census reads correctly **without hand-folding duplicates**
  (the 2026-08-24 run needed 20 folded by hand) — event/performer/vault/bound: as (4).
  **(6) `[field-contingent]` — does not gate:** on that same run,
  `cost_accounting.phases[Scan pages].prompt_chars` sits materially below the 2026-08-24
  baseline at comparable `pages_total`. Stated honestly and **deliberately not gating**: the
  1.2 MB/run `wiki-index` saving is agent-side and invisible to this instrument by its own
  declared blind spot (`vlt-lint-full.js:127`) — the convention-read saving is **not** graded
  from this number — event/performer/vault/bound: as (4).


  **Acceptance 2026-08-26 (`acceptance-discharge`, evidence: the `{field-vault}` 0.15.0 → 0.16.0
  upgrade at `_agent/upgrade-ledger.md` §0.16.0 + `{lint_reports}/2026-08-25-1600-lint.yaml`, the
  first post-release full lint, cold, 146/146 pages).** Split — **NOT ticked, one check FAILED.**
  **Upgrade-side/ship-verifiable DISCHARGED:** (1) `PAGE_SCAN` **3598 ≤ 3700**, E6 PASS
  (brief BUILT `status:` V1); (2) the reader probe returned the two genuine wikilinks with all
  four traps at zero, `frontmatter_valid: true` unattested, 14/14 fields (V3, verbatim JSON in
  the brief); (3) `key_claims` → 0 hits, `wiki-index@2` pin surviving on `indexPrompt`,
  `write-verification.md` still `version: 3`/5 consumers (V4/V7). **(4) DISCHARGED —**
  `missing_targets: []` at `:9`, **zero**, against the same unchanged obsidian-dataview /
  obsidian-bases corpus that produced **ten of ten** false flags on 2026-08-24; the code-span
  exclusion landed. **(6) DISCHARGED —** `cost_accounting.phases[Scan pages].prompt_chars`
  **473,622 → 356,676** at identical `pages_total: 146` (−116,946, −24.7%), matching V8's
  predicted ≈ −112 KB/run; the Cluster pass fell **123,172 → 42,279** on the `key_claims` drop.
  (The 1.2 MB/run agent-side convention saving remains invisible to this instrument by its own
  declared blind spot, as the check states — not graded from this number.)
  **(5) FAILED — the defect recurred.** Report `:241`: one entry under `unmarked_supersessions`
  (`execution-to-judgment-shift`) and **5 of 7** `malformed_frontmatter` entries
  (`bistec-encebollado`, `k-curve-career-divergence`, `kettl`, `llm-wiki-pattern`,
  `obsidian-bases`) were all "missing `verified_by`/`verified_at`" — attestation complaints
  misrouted, **"folded into the attestation census, same as the 2026-08-24 run"**, the exact
  hand-fold the check forbids. Magnitude fell 20 → 6; shape unchanged; **second consecutive
  run**. Diagnosis: F2/F3 shipped the per-slot prohibition without the *terminal class* the
  2026-08-24 filing's fix direction asked for, so the complaint routes to whichever slot is
  still open — and the at-rest probe could not observe it, being built to test the two closed
  slots. **Filed:** `factory/inbox/2026-08-26-075130-attestation-misroute-survives-the-jurisdiction-narrowing.md`
  → routes to Cycle 13 `inbox-capture`. **Not re-carried as STILL-OPEN** — the discharging
  event occurred and the check did not pass.

- [ ] **build-3 (para-posture, briefed 2026-08-25):** brief
  `factory/cycles/12-proxy-claims/briefs/build-3-para-posture.md`. Nine checks — five
  ship-verifiable (all gate), four field-contingent (none gate). The filing's request that
  retiring a load-bearing rule **gate** closeout (the A4-4(5) lesson) is honoured by the
  ship-verifiable half, never by mis-tagging the field half (E5, Round 8).
  **(1) `[ship-verifiable]` — GATES closeout:** the handshake is bipartite-consistent after
  `extraction.md` **6 → 7** — `extraction.md:12` lists **four** consumers
  (`[vlt-extract, vlt-lint, vlt-track, vlt-query]`, the fourth new per A26) and all four ack
  `extraction@7` (`vlt-extract/SKILL.md:4`, `vlt-lint/SKILL.md:4`, `vlt-track/SKILL.md:4`, and
  `vlt-query/SKILL.md`'s newly-added `depends_on:` line); `frontmatter.md` stays `version: 13`
  with `consumers:` 9 → 10 and `vlt-query` acking `frontmatter@13` (a **roster** change, not a
  rule change — brief disposition 2); `write-verification.md` untouched at `version: 3` / 5 —
  instrument: package-lint **Group E** (`tools/package-lint.py`, E1/E2/E3/E5) at rest, never a
  hand-written `grep "extraction@"` (self-confirming); evidence: the Group E PASS line + both
  `consumers:` lines in the brief's BUILT `status:`.
  **(2) `[ship-verifiable]` — GATES closeout:** the rule-card's derivation claim survives the
  contract edit — `vault-rule-card.md:11`'s `derived_from: … sha256:` re-derived to equal the
  edited contract's digest, and the card inside `RULE_CARD_BUDGET` (8,000 B; measured **6,957**
  at HEAD, 1,043 of headroom for A28's list→test rewrite) — instrument: package-lint **C6**
  (`tools/package-lint.py:330-346`) plus the raw `shasum -a 256` / `wc -c` numbers; evidence:
  the PASS line, the new digest and the new byte count.
  **(3) `[ship-verifiable]` — GATES closeout:** the retirement landed **whole** — all five rows
  of the brief's retirement table gone from every named site (the Layer-3 location prohibition
  `contract:68` + `rule-card:26`; the surface-count prohibition across `contract:66`,
  `rule-card:26`, `vlt-extract:13`, `vlt-agent-creative:14`, `vlt-review-council:51`,
  `vlt-upgrade:159`; `extraction.md:45`; `checks.md:16`'s rationale; the `≥2 wiki pages` gate at
  `vlt-extract:38`/`:118` + `vlt-agent-creative:37`/`:14`), no site restating the retired frame,
  **and the `{wiki}` carve-out SURVIVING** at `contract:70` and `checks.md:18` (A19, refused
  4/4) — instrument: the brief's Verification-8 grep battery (seven greps: six expecting 0, one
  expecting survival), factory-side at rest; evidence: the seven grep outputs verbatim.
  **(4) `[ship-verifiable]` — GATES closeout:** a `para_*` finding produced by an **ordinary
  `vlt-lint` run**, not by direct check invocation, over a fixture vault — proving step 0's
  file-selection path exists (owner ruling R-1 / A17: *"the gate cannot see its own hole"*) —
  instrument: the brief's Verification-3 single-agent reader probe over the specified temp
  fixture tree (seven files: a wiki page, a loose layer-root brief, two containers, an
  undeclared sub-container, a container `record.md`), scoped mode, at rest, **carrying a
  negative control** (pass condition 3 — the inheriting sub-container MUST fail); evidence: the
  returned report fence recorded verbatim in the BUILT `status:`.
  **(5) `[ship-verifiable]` — GATES closeout:** the write-posture resolver behaves as ruled on
  that same fixture — nearest declaring ancestor; **inheritance** binds an undeclared
  sub-container beneath a declaring parent (A23); **undeclared → `open` → PASS, never a
  finding** (A22, and `{resources}/briefs/` is E5's own pilot population); `{wiki}` removed at
  **population** time with no exception inside the check; the `checks.md:16` container-file
  attestation carve-out intact — instrument: Verification 3's pass conditions 2, 3 and 4;
  evidence: as (4).
  **(6) `[field-contingent]` — does not gate:** `trust: raw` becomes **representable and
  present** in PARA (`ST-2`'s own test — *"if no `raw` content appears there after the
  entry-condition change, the change did not take"*, regardless of contract text), read on
  **three** outcomes per A18: (a) `raw` appears honestly; (b) nothing appears; (c) **`raw`
  appears and `author:` is falsified** — event: `vlt-brief`'s next scheduled issue files to
  `{resources}/briefs/` at honest `author: agent` / `trust: raw`, no relabeling, no
  pointer-container indirection, no bespoke carve-out; performer: the owner; vault:
  `{field-vault}` (the only install running `vlt-brief` on a schedule); bound: the first
  scheduled issue after the release, no later than Cycle 13's `inbox-capture`. *One live run
  also closes tracker #11 — which is A12-4's subject.*
  **(7) `[field-contingent]` — does not gate:** *(carry-forward **b2(2)**, RETIRED into this
  build's acceptance by Q9 — it must not discharge against text this cycle rewrote)* a partner
  resolves a `{resources}`-write legality question **from the rewritten bundle** without
  escalating — reads the entry condition at `contract:66`, resolves posture via `contract:68`,
  and writes or declines without asking a human to adjudicate the rule — event: any partner
  session attempting a `{resources}` write after the upgrade; performer: any partner, observed
  by the owner; vault: `{field-vault}`; bound: Cycle 13's `inbox-capture`.
  **(8) `[field-contingent]` — does not gate:** the vault is **told** — the post-flight report
  of the upgrade carrying this release renders `governance_rule_changes:` **non-empty**, naming
  the PARA posture change (A33; the key's presence and its never-omitted-when-empty rule are
  graded at rest under check 3 — this is the live rendering only) — event: the owner's
  `vlt-upgrade` run onto this cycle's release; performer: the owner (standing rule); vault:
  `{field-vault}`; bound: the first upgrade after the release.
  **(9) `[field-contingent]` — does not gate:** *(the **re-pointed** confidentiality
  DECLINE+WATCH, re-graded at brief time per A34 — the DECLINE **stands**, Maya's dissent
  preserved; `writers:` is the declarable container attribute the DECLINE said was missing, on
  the write axis, so what remains is the **transition**, not the field)* a vault, on discovering
  the new posture, **declares `writers:`** on a container it had previously framed in prose —
  event: a human-ratified `writers:` line appearing on any live `charter.md`; performer: the
  human (charters are human-gated — a partner proposes, never ratifies); vault: `{field-vault}`;
  bound: Cycle 13's `inbox-capture` — **and if none declares by then, that routes to an owner
  ruling on whether A33's notification is sufficient, not to a fourth re-carry.**


  **Acceptance 2026-08-26 (`acceptance-discharge`, same evidence base).** Split — **NOT ticked;
  no FAILED, three genuine first-exercise tails.** **All five ship-verifiable DISCHARGED:**
  (1) handshake bipartite-clean after `extraction.md` **6 → 7** — `extraction.md:11-12`
  `version: 7` / `consumers: [vlt-extract, vlt-lint, vlt-track, vlt-query]`, exactly four
  `extraction@7` acks and no strays, `frontmatter.md` unbumped at `13` with `consumers:` 9 → 10,
  `write-verification.md` untouched at `3`/5; Group E PASS (brief BUILT `status:` V1/V2).
  (2) contract re-derived **twice** (the second after deviation 2's resolver clause) —
  `shasum -a 256` `670170b8…6c97` matching `vault-rule-card.md:11`; card **7,106 B** against
  `RULE_CARD_BUDGET = 8,000`, C6 green. (3) the seven-grep retirement battery — six at 0, the
  `{wiki}` carve-out **surviving** (A19); the battery found a **sixth** undeclared site the
  table missed (`extraction.md:26`, `vlt-track/SKILL.md:21`), which is the completeness rule
  working. (4) a `para_*` finding produced by an **ordinary** `vlt-lint` run over the fixture,
  negative control firing. (5) the resolver as ruled — nearest declaring ancestor, inheritance,
  undeclared → `open` → PASS, `{wiki}` removed at population time; the probe's first run
  surfaced the **`author: hybrid` hole** (every charter, schema-mandated `hybrid`, escaped the
  join), fixed at `contract:68` + `checks.md:19` and re-run.
  **(8) DISCHARGED — the vault was told.** The upgrade report's `governance_rule_changes:`
  (`_agent/upgrade-reports/2026-08-25-1754-upgrade.yaml:16-22`) came back **non-empty with six
  entries**, `:17` naming the PARA entry-condition change with the `writers:` /
  undeclared-is-`open` consequence and `:18` naming **both retirements** by name with the
  re-derive instruction. First live render of build-3's F11 key.
  **STILL-OPEN (three, all with named triggers):**
  **(6)** `trust: raw` representable-and-present in PARA outside `{wiki}` — the newest
  `vlt-brief` issue is `_agent/briefs/ai-tech-industry/2026-08-24-issue-003.md`, **pre-upgrade**;
  no scheduled issue has run since. The only `trust: raw` outside `{wiki}` today is the
  pre-existing `resources/workflow/wispr-obsidian-shortcut.md`, not a post-upgrade write.
  Event/trigger: the owner's next scheduled `vlt-brief` issue; bound: Cycle 13 `inbox-capture`.
  *(One live run also closes tracker #11.)*
  **(7)** a partner resolving a `{resources}`-write legality question from the rewritten bundle
  without escalating — no `{resources}` write has been attempted post-upgrade. Trigger: any
  partner session attempting one, observed by the owner; bound: Cycle 13 `inbox-capture`.
  **(9)** a human-ratified `writers:` line on a live `charter.md` — **zero** `writers:`
  declarations vault-wide today. ⚠ **Reachability note the owner should carry into that
  ruling, not a re-grade:** the executor reports the entire PARA tree holds **exactly one**
  `charter.md` (`projects/fantasy-2026`), declaring no `writers:` — so the posture resolved
  `open` for all 60 PARA files and `para_writer_unauthorized` fired on an **empty population**
  in its first release (`para_writer_unauthorized: []` at `:114`). The fall-through is correct
  and deliberate; the point is that the declaring population is 1, so "no vault declared by the
  bound" would be weak evidence about the mechanism. This is **not** BLOCKED — the trigger
  exists (a human declaring on that one charter, and A33's notification has now fired to prompt
  it) — but the check's own escape hatch already anticipates it: if none declares by Cycle 13's
  `inbox-capture`, that **routes to an owner ruling on whether A33's notification is
  sufficient, not to a fourth re-carry**.

- [ ] **build-4 (parked-interim-guidance, briefed 2026-08-25):** brief
  `factory/cycles/12-proxy-claims/briefs/build-4-parked-interim-guidance.md`. Six checks — four
  ship-verifiable (all gate), two field-contingent (neither gates). A40's grading rides the
  brief: **one prohibition added, none retired** — the number Cycle 12's closeout records for
  P-15's series (A50).
  **(1) `[ship-verifiable]` — GATES closeout:** the handshake is bipartite-consistent after
  `decision-log.md` **3 → 4** — `decision-log.md:12` lists **five** consumers
  (`[vlt-mint, vlt-upgrade, vlt-lint, vlt-ingest, vlt-feedback]`) and all five ack
  `decision-log@4` (`vlt-mint/SKILL.md:3`, `vlt-upgrade/SKILL.md:3`, `vlt-lint/SKILL.md:4`,
  `vlt-ingest/SKILL.md:4`, and `vlt-feedback/SKILL.md:3`'s newly-added `depends_on:` line), no
  stray pin — instrument: package-lint **Group E** (`tools/package-lint.py`, E1/E2/E3) at rest,
  never a hand-written `grep "decision-log@"` (self-confirming); evidence: the Group E PASS line
  + the final `consumers:` line in the brief's BUILT `status:`.
  **(2) `[ship-verifiable]` — GATES closeout:** the re-read works **and knows what not to
  surface** — over a temp fixture `_agent/mint/decision-log.md`, `vlt-upgrade`'s third reconcile
  leg surfaces **exactly** the one live `kind: parked-interim` entry, **not** the superseded one
  (the negative control), **not** the `deviation` entry (outside the scan by design), and
  renders `parked_interims_review: []` — present, not omitted — over a log with no parks —
  instrument: the brief's Verification-3 single-agent reader probe over the specified four-entry
  fixture plus the empty-log fixture, factory-side at rest; evidence: the returned report blocks
  recorded verbatim in the BUILT `status:`.
  **(3) `[ship-verifiable]` — GATES closeout:** the prohibition ships **attached to an artifact**
  and stated **once** (A36 + single-home) — `decision-log.md:39`'s kind enum carries
  `parked-interim`, the convention's new §*Parked interims* is the rule's only statement,
  `vlt-feedback/SKILL.md` carries a parking step naming `_agent/mint/decision-log.md` + the three
  required entry contents + the population line (A38), `vlt-mint/SKILL.md:104` carries a pointer
  clause and no restatement, and both drifting completeness glosses (`decision-log.md:23`,
  `vlt-mint/assets/decision-log-template.md:3-4`) are gone — instrument: the brief's
  Verification-5 six-grep battery + package-lint Groups A/B/C; evidence: the six grep outputs
  verbatim and the PASS line.
  **(4) `[ship-verifiable]` — GATES closeout:** the R4 widening landed whole and its exclusion is
  **declared, not silent** — `parked_interims_review:` present in `vlt-upgrade`'s Step-4 schema
  block, rendering in key order under the walk-the-block rule (`:93`) and passing the persist
  key-set verify (`:131`) on a rendered fixture report; `migrations_run` (`:109`) gains **no**
  token because the third leg is a leg of `decision-log-reconcile`, with the reason recorded at
  the leg — instrument: the brief's Verification-4 enumeration audit (a parse of the
  fixture-rendered report's top-level key set against the schema block); evidence: the parsed key
  set and the recorded declaration.
  **(5) `[field-contingent]` — does not gate:** a real park is recorded through the new step — an
  entry appears in `_agent/mint/decision-log.md` with `kind: parked-interim`, a `ref:`, the issue
  URL, the blocker stated as a claim about **current shipped behavior**, `user-ruled` verdict
  provenance with its required *why*, and **no command sequence** — event: the next
  `vlt-feedback` filing of a blocker the vault is holding an interim against; performer: the
  owner (the skill is invoked-only and approval-gated); vault: `{field-vault}` — the only install
  with the rail configured and a filing history; bound: Cycle 13's `inbox-capture`. *Stated
  honestly at brief time: **nothing in this plan schedules a new upstream blocker.** If none
  occurs by the bound, this routes to an owner ruling on whether the mechanism is graded on check
  (2)'s at-rest evidence alone — **not to a re-carry** (A56's lesson applied at brief time).*
  **(6) `[field-contingent]` — does not gate:** the re-read fires where it matters — the next
  `vlt-upgrade` run on a vault holding a live `parked-interim` entry renders a **non-empty**
  `parked_interims_review:` naming that entry and its filing reference, and where the run also
  carries governance rule changes, says so on the line beside a non-empty
  `governance_rule_changes:` — event: the first `vlt-upgrade` after (5)'s entry exists;
  performer: the owner (standing rule); vault: `{field-vault}`; bound: Cycle 13's
  `inbox-capture`. *Dependency stated: ungradeable before (5) discharges — if (5) routes to an
  owner ruling, so does this.*


  **Acceptance 2026-08-26 (`acceptance-discharge`, same evidence base).** Split — **NOT ticked;
  no FAILED, two coupled first-exercise tails.** **All four ship-verifiable DISCHARGED:**
  (1) handshake bipartite-clean after `decision-log.md` **3 → 4** — five consumers, five acks,
  no stray pin, Group E PASS (brief BUILT `status:`). (2) the fixture re-read surfaced
  **exactly** the one live `kind: parked-interim` entry — not the superseded one, not the
  `deviation` entry — and rendered `parked_interims_review: []` present-not-omitted over an
  empty log. (3) the prohibition ships attached to an artifact and stated **once**; both
  drifting completeness glosses gone (six-grep battery). (4) `parked_interims_review:` present
  in the Step-4 schema block, key-order render + persist key-set verify passing,
  `migrations_run` gaining **no** token with the reason recorded at the leg.
  **Live corroboration of (2)'s empty-case half:** the real upgrade report renders
  `parked_interims_review: []` at `_agent/upgrade-reports/2026-08-25-1754-upgrade.yaml:24` —
  **present, not omitted**, over a vault with no parks. This is the at-rest property confirmed
  in the field; it is *not* check (6), which needs a non-empty render.
  **STILL-OPEN (two, coupled):**
  **(5)** a real park recorded through the new step — `grep -n "parked-interim"
  _agent/mint/decision-log.md` → **0 matches**; no `vlt-feedback` filing has parked since the
  release. Trigger: the owner's next `vlt-feedback` filing of a blocker the vault holds an
  interim against (invoked-only, approval-gated); bound: Cycle 13 `inbox-capture`. *The brief's
  own honest statement stands and the owner should hold it: **nothing in the plan schedules a
  new upstream blocker.** If none occurs by the bound, this routes to an owner ruling on whether
  the mechanism is graded on (2)'s at-rest evidence alone — **not to a re-carry** (A56).*
  **(6)** ungradeable before (5) discharges, as the check itself declares — the empty render is
  confirmed live (above), the non-empty render needs (5)'s entry to exist first. Trigger: the
  first `vlt-upgrade` after (5); bound: as (5). *If (5) routes to an owner ruling, so does this.*

- [ ] **build-2 (change-keyed-findings-cache, briefed 2026-08-25):** brief
  `factory/cycles/12-proxy-claims/briefs/build-2-change-keyed-findings-cache.md`. Six checks —
  four ship-verifiable (all gate), two field-contingent (neither gates). **This is the cycle's
  release build**, so the release gate rides check (4). A12's shape honoured exactly: the
  ship-verifiable half is the sidecar **at rest on a two-run temp fixture**; the live
  `churn`-ratio saving is field-contingent and gates nothing.
  **(1) `[ship-verifiable]` — GATES closeout:** the two-run fixture — on a temp fixture vault of
  ≥ 6 pages, run 1 (no sidecar) writes `_agent/lint-cache.yaml` with a fingerprint and one record
  per page and reports `lint_cache: scanned T / cached 0 of T … cold (no prior cache)`; run 2,
  with one page's bytes edited and nothing else changed, dispatches **exactly one** scan agent
  and reports `files_checked: 1` / `files_cached: T-1` under the same fingerprint — instrument:
  the brief's Verification-5 harness run against the shipped workflow source with stubbed
  `agent`/`parallel`/`phase`/`log`/`budget` and a real temp fixture, factory-side and at rest;
  evidence: the three count triples and both `lint_cache:` lines recorded verbatim in the BUILT
  `status:`.
  **(2) `[ship-verifiable]` — GATES closeout:** findings parity — the cold run and the
  fully-cached run over the same fixture return **byte-identical** `fix_now`, `flag_for_human`
  and `opportunities` blocks, and the one-page-changed run's reduce is still correct across the
  whole corpus (orphans and `missing_targets` computed over all T pages, not over the 1
  rescanned) — instrument: Verification-5's runs 1–3 compared with an **unwrapped** `diff` whose
  invocation is named in the record (the contract's instrument rule, `contract:351`); evidence:
  the diff result and the third run's `missing_targets`/`orphans`.
  **(3) `[ship-verifiable]` — GATES closeout:** each of the three predecessor builds invalidates
  the cache, and the release's first full run is COLD (A10) — four mutations against a sidecar
  written under the current fingerprint, one at a time: `module_version` 0.15.0 → 0.16.0;
  `vlt-lint/SKILL.md:4`'s pin vector with `extraction@7` reverted to `@6` (build-3); the same
  line with `decision-log@4` reverted to `@3` (build-4); one character of `pageScanPrompt`'s
  invariant half or of `PAGE_SCAN` (build-1). Each yields `files_cached: 0` and a `lint_cache:`
  line reading `cold (fingerprint changed)` — instrument: the Verification-5 harness plus a
  fingerprint-recomputation probe over the four mutated inputs, at rest; evidence: the four
  fingerprints and the four cold lines.
  **(4) `[ship-verifiable]` — GATES closeout:** the release gate and the honesty surfaces survive
  the build — `uv run tools/package-lint.py --expect-version 0.16.0` exits **0** with **C6**
  green against the re-derived `vault-rule-card.md` sha and **E6** showing `PAGE_SCAN` unchanged
  at **3598**; both version strings read `0.16.0`; the B10-12 refusal still fires on a stale-copy
  simulation and does **not** fire on a fully-cached run (the narrowed predicate, brief
  disposition 10); and `coverage_caps` is unchanged in count (A16) — instrument: `package-lint`'s
  own D/C6/E6 run plus the brief's Verification-4 and Verification-10 greps, at rest; evidence:
  the PASS summary line, the new contract sha, the card byte count and the V4 returns.
  **(5) `[field-contingent]` — does not gate:** the saving is real at live churn — on the first
  full lint after the release's own cold run, `files_cached` is materially greater than
  `files_checked` at comparable `pages_total`, and
  `cost_accounting.phases[Scan pages].agents_dispatched` falls proportionally against the
  2026-08-24 baseline of 146 — event: the owner runs `vlt-lint --full` on `{field-vault}`
  **twice** after upgrading it to v0.16.0 (the first is the stated cold run, the second is the
  measurement); performer: the owner (standing rule); vault: `{field-vault}` only — the sole
  install with a 146-page wiki and a measured churn history; bound: the second full lint after
  the release, no later than Cycle 13's `inbox-capture`. *Stated honestly: this is the number
  direction 2 exists for, and it deliberately gates nothing — a fixture proves the mechanism,
  only the field proves the ratio.*
  **(6) `[field-contingent]` — does not gate:** the v0.16.0 rule-change notification actually
  renders — `vlt-upgrade`'s `governance_rule_changes:` comes back non-empty carrying all four
  facts the brief's F6 requires (the Layer-3/`extraction@7` entry-condition change with the
  `writers:`/undeclared-is-`open` consequence, `para_writer_unauthorized`, `decision-log@4`'s
  `kind: parked-interim`, and the named retirement), sourced from this build's CHANGELOG entry
  rather than from a diff — event: the owner's `vlt-upgrade` run on `{field-vault}` crossing
  0.15.0 → 0.16.0; performer: the owner; vault: `{field-vault}` (the only install crossing this
  boundary from 0.15.0); bound: that upgrade run, no later than Cycle 13's `inbox-capture`.
  *First live exercise of build-3's F11 key, and the only check that proves the CHANGELOG entry
  was written as a functional input rather than as release prose.*


  **Acceptance 2026-08-26 (`acceptance-discharge`, same evidence base).** Split — **NOT ticked;
  no FAILED, one genuine first-exercise tail.** **All four ship-verifiable DISCHARGED:**
  (1) the two-run fixture — run 1 `files_checked 6 / files_cached 0`, sidecar with 6 records;
  run 2 (one page's bytes edited) `files_checked 1 / files_cached 5`, **exactly one** agent
  dispatched, same `cache_fingerprint`, reduce still correct over all six. (2) findings parity —
  `/usr/bin/diff` (unwrapped, named) over the cold and fully-cached `fix_now`/`flag_for_human`/
  `opportunities` blocks exited **0**, both `sha256:45cc87b1e3b4…`; the fully-cached run
  dispatched **0** agents against a fan-out stubbed to throw. (3) all four fingerprint mutations
  forced cold (`module_version`, `extraction` 7→6, `decision-log` 4→3, one char of
  `pageScanPrompt`), four fingerprints recorded. (4) the release gate —
  `uv run tools/package-lint.py --expect-version 0.16.0` **exit 0**,
  `package-lint: A/B/C/E PASS, D PASS — vlt 0.16.0`, C6 green on the re-derived sha, E6
  `PAGE_SCAN` unchanged at **3598**; the B10-12 refusal fires on a stale-copy sim, **not** on a
  fully-cached run, **and does** on a half-cached run whose fan-out all died — the case that
  passes wrongly if the guard stays denominated on `pages.length`; `coverage_caps` unchanged.
  **(6) DISCHARGED — the CHANGELOG entry worked as a functional input.**
  `governance_rule_changes:` came back non-empty carrying **all four** facts F6 requires:
  the Layer-3/`extraction@7` entry-condition change with the `writers:`/undeclared-is-`open`
  consequence (`:17`), the named retirement of both prohibitions with the re-derive instruction
  (`:18`), `para_writer_unauthorized` (`:19`), and `decision-log@4`'s `kind: parked-interim`
  (`:20`) — plus `:21` on `extraction@7` and `:22` correctly marking the lint cache
  *"operational, not a rule change"*. Sourced from the CHANGELOG, not from a diff.
  **A10 CONFIRMED IN THE FIELD:** the release's first full run **was** cold —
  `lint_cache: "cold (no _agent/lint-cache.yaml existed, and the 0.15.0 -> 0.16.0 release moved
  module_version, the extraction pin 6 -> 7 and the decision-log pin 3 -> 4, so every prior
  record would have been invalidated anyway) — scanned 146 / cached 0 of 146 pages; written
  2026-08-25 under fingerprint 8a90c46fcba0e377173f|60c3ac0c3fc866ba"`, with
  `files_checked: 146 / files_cached: 0` at `:3-4`. The sidecar wrote (150.5 KB on disk). The
  mechanism is live; the predicted cold run is exactly what the field produced.
  **STILL-OPEN (one):**
  **(5)** the churn-ratio saving — this run is the **stated cold run**, i.e. the *first* of the
  two the check requires; `files_cached: 0` is its predicted value, not a failure. Event: the
  owner runs `vlt-lint --full` on `{field-vault}` a **second** time, where the measurement lands
  (`files_cached` materially greater than `files_checked` at comparable `pages_total`, and
  `agents_dispatched` falling against the 2026-08-24 baseline of 146; this run held at 146 as a
  cold run must). Trigger: the owner (standing rule); bound: the second full lint after the
  release, no later than Cycle 13 `inbox-capture`. **Live cost datum for that comparison,
  recorded now:** 172 agents / 10.3M subagent tokens / 1,894 tool calls / ~60 min wall clock for
  146 pages + 25 clusters, at `churn_since_last_full: 5 of 146`.

## Owner ruling — the six bounded tails at their bound (2026-08-26)

*Every one of Cycle 12's six field-contingent tails was bounded to **"Cycle 13's `inbox-capture`."**
Cycle 13's capture was a narrow patch capture that explicitly did not trigger the attachment
(Cycle 13 §Owner ruling — narrow-capture carve-out), and Cycle 13 shipped and closed to capture
without ever running a full batch. **Cycle 14's `inbox-capture` on 2026-08-26 is that batch, so
the bound landed there** — recorded at `factory/cycles/14-no-enforcement-point/roadmap.md`
§Cycle 12's six bounded tails. This section records the grades and the owner rulings taken in
that session, against evidence re-gathered from `{field-vault}` at the bound rather than from the
ledger's last-known state.*

*The ledger bullets above are append-only and are **not** rewritten; this section supersedes their
STILL-OPEN notes where it says so.*

**b4(5) — DISCHARGED (grading, not a ruling).** A real park recorded through the new step. The
ledger's own instrument — `grep -n "parked-interim" _agent/mint/decision-log.md` — returned **0**
at the discharge run and returns **two entries** at the bound, both dated 2026-08-26:
`decision-log.md:1197` (agent-lane `type:` in the PARA population, `ref: conventions/extraction.md`,
filing #15) and `:1255` (partner-sitting writes to Layer 3 left unattested,
`ref: conventions/write-verification.md`, filing #16). The trigger fired exactly as specified —
*the owner's next `vlt-feedback` filing of a blocker the vault holds an interim against*. **The
brief's honest caveat is worth preserving rather than quietly overwritten:** it stated that
*nothing in the plan schedules a new upstream blocker*, and that was true; two arrived anyway,
from the 0.16.1 sweep. The check discharged on its own terms, not on a re-reading of them.

**b4(6) — DISCHARGED (grading, not a ruling).** The non-empty render.
`_agent/upgrade-reports/2026-08-26-1046-upgrade.yaml:18-20` renders `parked_interims_review:` with
**both** entries, each naming its convention, its park and its filing URL. The conditional half is
satisfied more strongly than the check asked: each line states the `governance_rule_changes:`
relationship explicitly — *"This run's `governance_rule_changes` is empty: the rules this park
rests on did not move at 0.16.1, and the filing is still open."* The coupling to b4(5) is resolved
because b4(5) discharged; this is the first live non-empty render of build-4's key.

**b3(6) — DISCHARGED on substance (owner ruling, 2026-08-26).**

⚠ **The ledger's STILL-OPEN note for this check is stale and is superseded here.** It records the
newest `vlt-brief` issue at `_agent/briefs/ai-tech-industry/2026-08-24-issue-003.md` and states
*"the only `trust: raw` outside `{wiki}` today is the pre-existing
`resources/workflow/wispr-obsidian-shortcut.md`."* Neither holds at the bound. The shelf is at
**`resources/briefs/`** — a `{resources}` address, i.e. in PARA — carrying five issues across three
series, every one `type: research` / `author: agent` / `trust: raw`, with **no relabeling, no
pointer-container indirection and no bespoke carve-out**. The 2026-08-26 10:46 full lint enumerates
all five by path independently (`_agent/lint-reports/2026-08-26-1046-lint.yaml:34`). Tracker #15,
filed at 12:55 the same day, still describes moving the shelf as prospective — so the filing is
stale against the vault too, and A14-6's capture should be read with that in mind.

**The ruling.** The check names **`ST-2`'s own test** as its authority — *"if no `raw` content
appears there after the entry-condition change, the change did not take"* — and says **"regardless
of contract text."** Outcome **(a) `raw` appears honestly** is satisfied, on five files, verified by
an instrument that is not the vault's own claim. The specified event (*the first scheduled issue
after the release*) was **a way of producing that state, not the state itself**; the state exists
and was reached without falsifying `author:` (outcome (c) refuted explicitly). Graded
**DISCHARGED**. *Recorded honestly: the five files predate the release, so this discharges the
check's substance and does **not** evidence that a post-0.16.0 scheduled run behaves correctly.
That is a weaker claim than the event would have supported, and the ruling accepts it knowingly.*

**b3(9) — CLOSED by owner ruling: A33's notification is sufficient (2026-08-26).** No re-carry.

Evidence at the bound, independently confirmed: the vault holds **exactly one** `charter.md`
(`projects/fantasy-2026`), declaring **no** `writers:`, and `para_writer_unauthorized: []` at
`_agent/lint-reports/2026-08-26-1046-lint.yaml:38` carries the report's own note — *"no charter in
the vault declares `writers:`, so every container's posture is `open` and every file PASSES
(0.16.0 rule: silence means open, not closed)."*

The check's own escape hatch is invoked as written: *if none declares by the bound, that routes to
an owner ruling on whether A33's notification is sufficient, **not to a fourth re-carry***. The
owner rules it **sufficient**. Reasoning on record: the mechanism is already proven at rest —
build-3 check (5) discharged the resolver whole (nearest declaring ancestor, inheritance,
undeclared → `open` → PASS, `{wiki}` removed at population time), and its first run surfaced and
fixed the `author: hybrid` hole. A33's notification fired to prompt declaration. With a declaring
population of **1**, "no vault declared by the bound" was never going to be evidence about the
mechanism, and the ledger's own ⚠ note said so before the bound arrived. Waiting longer buys
nothing this check can spend.

⚠ **The population problem is the durable finding here, and it outlives this grade.** A
field-contingent check whose discharging population is a *single vault artifact* was not gradeable
in the field on the day it was written. That is `ST-5`'s territory — instruments built at the point
of least evidence — and it is named here so the third instance does not re-derive it.

**b2(5) — FAILED (2026-08-26, same day, on a live test of the corrected bound).**

⚠ **This supersedes an earlier ruling in this same section, made hours before and committed.** That
ruling read: *"This is not owner inaction, and it is not a defect — it is build-2 check (3) working
exactly as specified"*, and CARRIED the tail with a corrected bound of *two consecutive full runs
under the same ruleset fingerprint*. **The corrected bound was then tested and the check failed it.**
The reasoning was wrong in one specific way worth recording: the cold run *was* correctly attributed
to the 0.16.0 → 0.16.1 crossing, and that attribution **masked a mechanism that would have missed
regardless**. An honest report line pointed at the wrong cause.

**The test.** A second full sweep on `{field-vault}`, run deliberately as this check's acceptance
test: **146 pages, 0 of 146 changed** since the 10:46 sweep (instrument: `python3
os.path.getmtime`, unwrapped), byte-identical corpus, same `module_version`, same conventions, **no
release in between** — i.e. the corrected bound, satisfied. Result: **146 queued for fresh scan, 0
served from cache.** The sweep was cancelled before completion; the verdict did not need it to
finish.

**Two independent defects, either alone sufficient for a permanent 100% miss rate**, both grounded
factory-side against shipped source: (1) the sidecar schema mismatch — `full-scale.md` step 5 tells
the SKILL to write the workflow's returned `fresh_scans`, which are raw PAGE_SCAN objects carrying
no `key` and no `scan` wrapper, while the reader at `vlt-lint-full.js:243` requires all three and
`:344` dereferences `.scan`; and (2) `rulesetFingerprint` has no single-homed deterministic
algorithm — `full-scale.md` step 2 names the inputs and specifies no digest construction, so two
runs over an identical ruleset compute different values (`980d749d9acf418e` vs `66d27a0e6cd8fabe`).

**Grade: FAILED.** Not carried, not re-bounded. There is no bound at which a structurally
unreachable mechanism discharges. **Filed:**
`factory/inbox/2026-08-26-141838-findings-cache-cannot-round-trip-writer-and-reader-disagree.md`,
captured as Cycle 14 §A14-8.

⚠ **The instrument lesson is `ST-5`'s, and it is exact.** Build-2's checks (1)–(3) proved the cache
on a two-run temp fixture *inside one harness invocation*, where the SKILL-side write step never ran
because the harness stubbed it. The one seam that breaks in the field is the one the at-rest
instrument could not exercise — an instrument authored from the fix's shape, unable to observe what
the fix's author did not anticipate. **And the field check that would have caught it was b2(5)
itself, which was written as field-contingent and therefore did not gate.** Cycle 12 shipped a
mechanism that has never once worked, with a green ship-verifiable ledger.

**b3(7) — STILL OPEN, not ruled.** A partner resolving a `{resources}`-write legality question from
the rewritten bundle without escalating. No evidence either way exists on disk: this check requires
the owner to *observe* a partner session attempting such a write, and none is recorded. Carried
unchanged, bound to Cycle 14's closeout. *Note the interaction: A14-6 and A14-7 are both live parks
against the same bundle, so a partner attempting a `{resources}` write today may legitimately
escalate — which would not be a failure of the rewritten bundle but of the two vocabularies it is
waiting on.*

**Tally at the bound: 6 tails → 3 DISCHARGED (b3(6), b4(5), b4(6)), 1 CLOSED by ruling (b3(9)),
1 FAILED (b2(5) — tested and refuted the same day; filed and captured as A14-8), 1 STILL OPEN
(b3(7)).** Cycle 12's field-contingent ledger is 7 of 11 discharged, **1 FAILED**, and holds no
no-re-carry item. The FAILED one is the cycle's first: v0.16.0 shipped the findings cache with a
green ship-verifiable ledger, and the mechanism has never once worked in the field.

## Grounding corrections issued at brief time — build-3 (2026-08-25)

*The superseding notes `build-brief`'s Re-ground stage owes the roadmap, so this file does not
keep asserting a stale premise to the next reader. **The capture bodies above are append-only
and are not rewritten** — these notes supersede specific cites within them. Five cites had
drifted; three roadmap claims were corrected on grounding; none contradicted an ideation
ruling, so none blocked.*

**Cite drift (five — the sixth, seventh, eighth, ninth and tenth this cycle has logged; the
live instance of out-of-scope item 4, *the loop's line-number cites go stale silently*).**

| roadmap/capture cite | at HEAD | source of the drift |
|---|---|---|
| `vlt-lint/SKILL.md:33` (A17 — the scoped-mode `find` glob) | **`:32`** (the fenced block runs `:31-33`) | capture approximation |
| `vlt-lint/SKILL.md:39` (A17 — full mode *"every page in `{wiki}`"*) | **`:37`** (`:39` is the *"every wiki page"* definition sentence) | capture approximation |
| `vlt-lint-full.js:517-519` (A17 — the deferral comment + `para_missing_attestation` slot) | **`:515-517`** comment, **`:518`** slot | **build-1's two deletions**, `f134190` |
| `vault-rule-card.md:10` (A27 — the live `derived_from:` sha256) | **`:11`** | capture approximation |
| `vault-operating-contract.md:192` (the capture's *"partners first load the rule-card"*) | **`:194`** | capture approximation |

*A27's substance is unaffected and was re-verified this session: `shasum -a 256` of the shipped
contract returns `57df3488…3666`, matching the card exactly — the card's derivation claim is
**true today**, which is why editing the contract without re-deriving it would ship a
verifiable, false claim.*

**Three roadmap claims corrected on grounding (none is a ruling; each is a cost estimate or a
roster count the brief re-derived).**

1. **A31 — `writers:` does NOT cost `frontmatter.md` 13 → 14.** Mary asked it be priced on the
   `grounding:` precedent (`b7193e8` bumped both conventions for one charter field). The
   precedent does not transfer: `grounding:` is a **general** frontmatter field with its own
   section (`frontmatter.md:86-94`) carried by PARA artifacts *and* charters; `writers:` is
   **charter-only**, and `frontmatter.md:171` opens the PARA section by disclaiming exactly
   this — *"Defined in `extraction.md` (the canonical reference; **not duplicated here**)."*
   **No bump, no nine-consumer re-ack** (brief disposition 2). *Binding on the builder: adding a
   `writers:` bullet to `frontmatter.md:173-177` would convert a free change into 13 → 14 plus
   nine re-acks for zero information.*
2. **A32 — step 0 and step 6 do NOT reach `vlt-lint-full.js`, so `extraction.md` gains no
   fourth consumer from them.** Winston asked where they land. Both are **SKILL-side**, and the
   workflow's own comment says why: `vlt-lint-full.js:515-517` already declares
   `para_missing_attestation` *"a structural slot **the SKILL fills from its own PARA
   jurisdiction scan**"* — the workflow sweeps `{wiki}` and PARA is outside its page set by
   design. The workflow's `depends_on:` pins at `:11` are untouched (E5 unaffected), and
   build-1's and build-3's file sets stay disjoint.
3. **The `extraction.md` consumer walk is FOUR acks, not three — an EXPANSION, not an error.**
   The roadmap and the capture both say *"re-ack all three consumers"*; `extraction.md:12` does
   read `[vlt-extract, vlt-lint, vlt-track]` and is bipartite-consistent at three today. But
   **A26 adds `vlt-query`** as a consumer (it becomes one at step 4 and carries **no
   `depends_on:` at all** — verified, `grep -c depends_on skills/vlt-query/SKILL.md` → 0), so
   the walk is **three re-acks + one new ack**, and `frontmatter.md`'s `consumers:` goes 9 → 10
   at `version: 13`.

**Two roadmap claims re-verified and standing, recorded because the brief rests on them.**
A20's *the module-fixed `{wiki}` floor is already shipped* — `contract:64` reads *"a
Librarian-only zone: the Librarian is its only writer"*, confirmed verbatim; that half of step 5
is struck as built. A17's *nothing selects the PARA population* —
`grep -c "PARA\|para_" skills/vlt-lint/SKILL.md` → **0**, and `report.md` carries **four**
producerless `para_*` slots at `:31`, `:35`, `:36`, `:37`. Both confirmed at HEAD.

## Grounding corrections issued at brief time — build-4 (2026-08-25)

*The superseding notes the Re-ground stage owes this file. **The capture and roundtable bodies
above are append-only and are not rewritten** — these notes supersede specific cites within
them. Three cites had drifted; one roadmap **grading** was found stale on grounding; none
contradicted an ideation ruling, so none blocked.*

**Cite drift (three — the eleventh, twelfth and thirteenth this cycle has logged; again the live
instance of out-of-scope item 4, *the loop's line-number cites go stale silently*). All three sit
in roundtable amendment A36, and all three are approximation — no build this cycle moved these
lines.**

| roadmap cite (A36) | at HEAD (`5585877`) | source of the drift |
|---|---|---|
| `vlt-feedback/SKILL.md:19-20` — *"The issue is **transport**, not the record."* | **`:14-16`** (`:18-20` is the field-contract single-home paragraph) | roundtable approximation |
| `vlt-feedback/SKILL.md:112-113` — *"a recovery artifact, **not a record**"* | **`:115-116`** | roundtable approximation |
| `vlt-feedback/SKILL.md:112-113` (same cite, second claim) — *"`_agent/feedback-outbox/` is deliberately **not** a `vault_structure` logical name"* | **`:118-120`** — a **different** paragraph; A36 cited one range for two separate statements | roundtable approximation |

**Cites re-verified and standing, recorded because the brief rests on them:**
`vlt-mint/SKILL.md:104` (the park fallback) and `:26` (the activation resume scan) are correct at
HEAD; `vlt-feedback/SKILL.md:38-42` (invoked-only) is correct; `vlt-upgrade/SKILL.md:78` (the
decision-log reconcile) is correct. Q7's grounding figures were re-measured this session and
hold: `skills/vlt-feedback/SKILL.md` is **7,186 bytes** and
`grep -cin "park\|interim\|exit condition\|blocker"` returns **0** — *"there is no existing
parking discipline to extend"* is true at HEAD.

**⚠ One roadmap GRADING corrected on grounding — recorded, NOT acted on (owner ruling owed).**
A46 (§Owner actions, below) grades A12-5's **module side** *"BLOCKED (unreachable) until A33's
`governance_rule_changes:` key exists."* **Build-3 shipped that key** — `vlt-upgrade/SKILL.md:111`,
commit `5585877`, F11 — so the precondition **now exists on this branch and the BLOCKED grading
is stale.** It changes build-4's scope by nothing (the module-side move is the release
choreography's CHANGELOG re-derive notice, which is platform work on `P-17`), but re-grading a
platform item is an owner act, not a briefer's. See build-4's brief, disposition 9.

**Two pre-existing CONTENT drifts found and folded into build-4's scope** (not cite drift):
`decision-log.md:23` and `vlt-mint/assets/decision-log-template.md:3-4` both gloss the log's
kinds as a six-item list that **omits `deviation`**, which shipped at v3. Adding a seventh kind
would leave both two behind, so both become point-at-the-map — the standing rule that *lists
claiming completeness drift*.

## Grounding corrections issued at brief time — build-2 (2026-08-25)

*The superseding notes the Re-ground stage owes this file. **The capture and roundtable bodies
above are append-only and are not rewritten** — these notes supersede specific cites within
them. Two cites had drifted; one of them corrected a **mechanism input**, not merely a line
number; none contradicted an ideation ruling, so none blocked.*

**Cite drift (two — the fourteenth and fifteenth this cycle has logged).**

| roadmap cite | at HEAD (`0e76901`) | source of the drift |
|---|---|---|
| **A14** — `checks.md:49`, quoting *"never prior lint reports (`{lint_reports}` is not read; reports stay walker-exempt)"* | **`checks.md:50`** (the *Spec candidates* bullet). `:49` at HEAD is the *personalized-extraction firewall* | build-3's catalog work shifted the bullet by one — a sibling build in the same release |
| **A10** — *"the convention `version:` pins … the scan was judged under"*, read as the workflow's own pin line | the pin vector of record is **`vlt-lint/SKILL.md:4`**, not `vlt-lint-full.js:12` | roundtable approximation, and the more serious of the two |

**⚠ The A10 correction is a mechanism correction, not a cite correction — recorded loudly.**
`vlt-lint-full.js:12` reads `["frontmatter@13", "wiki-supersession@2", "wiki-index@2",
"write-verification@3"]`. **`extraction` is not in it and never was**, because the page scanners
do not judge against `extraction.md`. Build-3 bumped `extraction.md` **6 → 7** and added
`para_writer_unauthorized`; **neither moves a character of `:12`.** A cache key built on the
workflow's own pins would therefore have failed to invalidate on **the exact build the
roundtable ordered build-2 to queue behind** — A11's ordering ruling would have been enforced
in prose and violated in fact. The pin vector of record is `vlt-lint/SKILL.md:4`, which at HEAD
carries **both** build-3's `extraction@7` **and** build-4's `decision-log@4`. A10's finding is
unchanged and its ruling stands; only its mechanism input is superseded. *(This is the cycle's
own thesis turning up inside the build that exists to fix it: a pin line standing in for "the
ruleset this was judged under", still standing in after the ruleset moved somewhere else.)*

**Cites re-verified and standing, recorded because the brief rests on them:** all three of
build-4's restated moved lines hold at HEAD — `vlt-upgrade/SKILL.md:113` (the report key),
`:126` (its prose), `:134` (persist-verify) — as do `:45` (the derive-first worked instance),
`:111` (`governance_rule_changes:`) and `:124` (its **"Crossing v0.16.0"** worked example);
`vault-operating-contract.md:349` (the derive-first boundary clause) and `:351` (the instrument
rule); `checks.md:42` (the read-before-flag preface); `decision-log.md:48`/`:108`/`:118`;
`report.md:43`; `tripwires.yaml:83-89`; `vault-rule-card.md:11` (`derived_from:`, card at
**7,106 B** against an 8,000 B budget); and build-1's eight moved workflow cites.

**⚠ A46's stale grading is UNCHANGED and still unacted — second brief to carry it forward.**
Build-4's brief found it; this brief re-checked it and it still stands stale
(`vlt-upgrade/SKILL.md:111` exists at HEAD). It is an **owner** re-grade of platform item
**`P-17`**, surfaced again in the routing block below so it is seen at release.

## Next lifecycle move

*This is the file's **single** terminal routing block, and it is authoritative
(`.claude/skills/vlt-lifecycle.md` §"a report's terminal routing line is authoritative"). It is
restamped by every lifecycle skill that moves the position. **Restamped 2026-08-25 by
`build-brief` when build-2's brief landed — the cycle's last brief.** *(Earlier the same day it
was restamped when build-4's, build-3's and build-1's briefs landed; in that first run the
file's defect was repaired — it carried **two** `Next lifecycle move` sections, this one still
routing to a roundtable that had already run. The mid-file section is now titled §"Routing at
the close of review" and marked historical.)*

**Restamped 2026-08-25 by `vlt-release` — v0.16.0 SHIPPED.** All four builds are BUILT and
released: build-1 `f134190`, build-3 `5585877`, build-4 `0e76901`, build-2 `93797b9` (the release
build), release commit `216bea2`, annotated tag `v0.16.0`, `main` pushed to origin. The release
gate passed at `package-lint: A/B/C/E PASS, D PASS — vlt 0.16.0` (exit 0), and the handshake gate
at 9 conventions / 39 pins bipartite-consistent.

**The next lifecycle move is an OWNER ACTION: run `vlt-upgrade` on a live vault.** Live acceptance
is batched to that run (CLAUDE.md step 8a). Once the upgrade evidence exists, `acceptance-discharge`
discharges this cycle's Deferred acceptance ledger, which is **wholly undischarged** — every check
of all four builds is unticked. Only ship-verifiable checks gate closeout; each build's
ship-verifiable checks passed **at rest** during its build, and the ledger records them for
discharge against field evidence.

**Owner acts that do not wait on the upgrade:**
- **Re-grade A46 / `P-17`** — it grades A12-5's module side *BLOCKED (unreachable) until A33's
  `governance_rule_changes:` key exists*, and build-3 shipped that key at `vlt-upgrade/SKILL.md:111`.
  The grading is stale on shipped code; re-grading a platform item is an owner act. **Three briefs
  flagged it** (build-3's, build-4's, build-2's) and none could act on it.
- **Hand-deliver build-3's re-derive notice** to `{field-vault}`'s known PARA park (A57) — build-3
  has now shipped, so this is due.
- **Run the parked-interim survey** against `{field-vault}` (E6) — a **list**, not a count, bounded
  to before Cycle 13's `inbox-capture`.
- **Sync project memory** (`vlt-cycle-12-roadmap`) with the shipped state.

*(Historical — the routing this block carried before the release:)*

**Every build in the cycle is now briefed. Two moves, in this order.**

**(a) A fresh builder session implements build-2** (`bmad-workflow-builder`) —
`briefs/build-2-change-keyed-findings-cache.md`, 2026-08-25; seven F-sites, twelve brief-time
dispositions, six acceptance checks in the Deferred acceptance ledger above (**four
ship-verifiable and gating**, two field-contingent). It is the cycle's **last** build and its
**release build**: it carries the dual version bump, the `--expect-version` gate and the
**v0.16.0 `CHANGELOG.md` entry** build-3's deviation 4 left owing (`vlt-upgrade/SKILL.md:122`
makes that entry a *functional input* to `governance_rule_changes:`, not release prose). Exit
obligations: rewrite the brief's `status:` to a **BUILT** record with **numbered deviations**,
delete any `.decision-log.md` from the working tree (*not* `_agent/mint/decision-log.md`), one
commit on `cycle12-v0.16.0` — **and stop before the tag.**

**(b) The cycle is then RELEASE-READY: `release vlt 0.16.0`** (`vlt-release`) — one dual version
bump (`.claude-plugin/marketplace.json` `"version"` **and**
`skills/vlt-setup/assets/module.yaml` `module_version`, both still reading **0.15.0** at this
stamp), the `uv run tools/package-lint.py --expect-version 0.16.0` gate (**tag only on exit 0**,
PASS line in the commit message), then ff-merge → tag → push.
**🛑 The release is HELD for the owner's explicit approval, and the target version is NOT an
owner ruling on record.** `0.16.0` is the branch-implied target (`cycle12-v0.16.0`), already
written into build-4's brief and — decisively — **already shipped into a shipped surface** by
build-3 at `vlt-upgrade/SKILL.md:124` (*"Crossing v0.16.0…"*). A different number requires
editing that line. The owner confirms the number and gives the go.

**Build state:** build-1 **BUILT** (`f134190`, eight F-sites, eight numbered deviations);
build-3 **BUILT** (`5585877`, thirteen F-sites, five deviations); build-4 **BUILT** (`0e76901`,
seven F-sites, two deviations); build-2 **BRIEFED**, awaiting a fresh builder session. Branch
`cycle12-v0.16.0`. **All four briefs written; three of four builds built.**

**Carried out of build-2's briefing, for the builder and for the release:**
- **Re-derive every `file:line` against HEAD; never trust a cite carried in this roadmap.**
  Fifteen stale cites have now been caught this cycle — and build-2's brief caught the first one
  that would have changed a *mechanism* (A10's pin vector), not merely a line number.
- **A46's BLOCKED grading is stale and remains unacted — an OWNER re-grade of `P-17`.** Build-3
  shipped the `governance_rule_changes:` key A46 says A12-5's module side waits on
  (`vlt-upgrade/SKILL.md:111`). **Two briefs have now flagged this.** It is surfaced here so the
  owner sees it at release rather than at Cycle 13's capture.
- **Owner acts still outstanding at release:** hand-deliver build-3's re-derive notice to
  `{field-vault}`'s known PARA park (A57); run the parked-interim survey against `{field-vault}`
  (E6), bounded to before Cycle 13's `inbox-capture` and reporting a list, not a count (A56).
- **For Cycle 13's ideation, on roundtable A51 and build-2's out-of-scope item 2:** direction 2
  **retires direction 4's own cost case**. After this build at `churn 5 of 146` the
  convention-read pool falls from `ST-3`'s 8.6 MB/run to ~0.29 MB/run and direction 4's marginal
  saving to ~0.19 MB/run. Rule direction 4 on `ST-3` cause (a) — *projection binds every future
  fan-out consumer*, which survives direction 2 untouched — and **re-measure the residual pool
  against build-2's acceptance check (5), never against the stale 8.6 MB figure.**

**Ideation is COMPLETE** (2026-08-25, nine owner-steered rounds — every slot ruled; see the
rulings section's round summary) and **REVIEWED** (roadmap roundtable, 2026-08-25 — see the review
record above). The cycle is **four builds, one release** — build-4 moved to the platform channel at
the roundtable (R-5):

| build | subject | `spike:` |
|---|---|---|
| 1 | page-scanner corrections + waste removal (A12-1, A12-2, Q6→`write-verification.md`, direction 1) | none |
| 2 | change-keyed findings cache (direction 2) — **queues behind builds 1 AND 3** | none |
| 3 | the PARA posture (A12-3, **seven steps** — step 0 added, roundtable R-1/A17) | none |
| 4 | parked-interim guidance (`vlt-feedback` + a re-read home) | none |

*(Renumbered at the roundtable: **the amendment trigger moved to the platform channel** —
ruling R-5, `.github/` is never delivered to vaults. **Four builds, one release.**)*

**What the roundtable carried into the room, beyond the ordinary joint-hunt** *(written before
the session; kept as the record of what it was asked to test — all four items were tested and
are answered in the review record above)*:

1. **P-15's obsolescence beat self-accepts here, and A12-3 is the finding it was built to
   catch.** P-15's bound is hard: *"If Cycle 12 reaches its roundtable without the beat
   present, or closes with the clause never asked, this is not a waiting state but **BLOCKED
   (unreachable)**."* The marquee retirement disposition is named in D2 — the Layer 3 location
   prohibition.
2. **Build-3 is the cycle's weight** — six steps, one `extraction.md` 6 → 7 handshake with
   three re-acks, five restatement sites, a new schema key and a new lint check, in a release
   that also carries four other builds.
3. **Four grounding corrections this session overturned capture claims** and are the joints
   most worth re-testing: `ST-1`'s **C4 already shipped** (Q5); Q6's clause is a
   **clarification, not a rule change** (Q6); A12-1's cause fix is **neither direction 4 nor a
   JS refactor** (Q8b, which amended Q1); and the `CHANGELOG` has **no delivery path to a
   vault** (Q3).
4. **Direction 4 and A12-1's cause-fix instrument are DECLARED for Cycle 13**, not deferred —
   the room should test whether that declaration holds or whether either belongs here.

**Owner actions, unblocked by any build** *(amended at the roundtable — the list was short by
three, A47/A57/A58)*: run the parked-interim survey against `{field-vault}` (E6), **bounded to
before Cycle 13's `inbox-capture` and reporting a list, not a count** (A56). ~~close tracker #11~~ — **STRICKEN (Round 9): #11 stays open**, already
answered by the owner's 2026-08-25 comment; the mirror rule holds it open until its filing
archives against A12-3's acceptance (E8). **Platform:**
open **`P-17`** — **not `P-16`, which is already taken** by *"the `promise:` line"*, filed
2026-08-25 and explicitly *"waits for Cycle 12 to ship"* (A47) — carrying **A12-4 only**;
A12-5's module side is **BLOCKED (unreachable)** until A33's `governance_rule_changes:` key
exists (A46). <br>**⚠ A46 SUPERSEDED ON GROUNDING (2026-08-25, build-4's and build-2's briefs) —
the key EXISTS at `vlt-upgrade/SKILL.md:111`, shipped by build-3 (`5585877`). The BLOCKED grading
is stale and the re-grade is an owner act on `P-17`; two briefs have now flagged it and it is
carried in the routing block above.** **P-14 self-acceptance is withheld** until its grounding
prompt is corrected (Q10).
**P-15 does NOT self-accept on this session** — its done-when is roundtable **and** briefs (A49).
<br>**Observation recorded at the last brief (2026-08-25), not a self-acceptance:** A49's second
half is now *materially* satisfied — **all four** of this cycle's briefs carry the retirement
clause answered (build-3 pre-named D2's marquee retirement and shipped it plus two build-time
additions; build-1, build-4 and build-2 each answered it with reasoning, and build-2 examined
three beat-produced candidates and refused all three, entering **zero** honestly). Per A48 and
A50, the closeout's retirement count should record **which retirements were pre-named and which
beat-produced**, and note that the beat also produced three *reasoned refusals* — a rail that
fires and says no is not the same as a rail that never fired. **P-15's self-acceptance remains
the platform channel's act, not this file's.**

**Added by the roundtable:**
- **At closeout: write the E8 register token as `B5-4..B5-9`**, never the old string (A58).
- **When build-3 ships: hand-deliver the re-derive notice to `{field-vault}`'s known PARA park**
  — the same act as the 17:06Z comment on #11 (A57).
- **Read `ST-4`** (`provenance-staffed-cognition-unstaffed`, opened 2026-08-25) — it reads this
  cycle's own ideation as its worked instance and is cited nowhere in this roadmap (A53).
- **Record the cycle's retirement count at closeout**, so P-15's tripwire has a readable series
  (A50).
