---
title: 'Cycle 16 — closed loops'
status: 'open — captured 2026-09-09 (A16-1..A16-5) + capture addendum 2026-09-16 (A16-6..A16-8); ideation FILLED 2026-09-16 (three builds; S-4 ruled RUN); ROUNDTABLE REVIEWED 2026-09-16 (full 13; 19 amendments A1–A19 applied, R1 declared, D9 added, 11 owner rulings, 0 open disputes; release shape amended to TWO releases — build 1 alone first, builds 2+3 held whole until S-4) — BUILD 1 BRIEFED 2026-09-16 (`briefs/build-1-own-writes-read-back.md`, its own release v0.18.1; ledger row 1 appended; one grounding correction under Q3) — BUILD 1 BUILT 2026-09-16 on `cycle16-v0.18.1` (F1–F11 landed; all at-rest verification green — both new harnesses PASS shipped / FAIL on v0.18.0, Cycle 15 build-2..5 regression green, scanFingerprint byte-identical, package-lint A/B/C/E PASS; three deviations recorded in the brief) — **v0.18.1 SHIPPED 2026-09-16 (build 1 alone, A10), @ `4fd8049`, tagged v0.18.1** (annotated; main + tag pushed to origin) — next: brief build 2; live acceptance for build 1 batched to the owner''s next `vlt-upgrade` on the field vault — ACCEPTANCE PASSES 1+2 2026-09-16 (`acceptance-discharge`) — pass 1 on upgrade evidence, pass 2 on the completed full sweep. **Ledger row 1 does NOT tick: (1)(3)(4)(5)(F1) DISCHARGED, (2) Census REVERSED to FAILED** (owner-ruled) — its census clause matched on three independent instruments (240 entries across 83 of 152 pages) but its *no per-page finding* clause was contradicted: build-1''s disposition 3 is **inert on any cached scanner record**, because `frontmatter_defect_fields` is not a `runKey` term, so it passes at rest forever and does nothing in the field (the Cycle 12 `b2(5)` shape). **(2) is ship-verifiable, so it GATES closeout.** Filed with a full specimen manifest as `2026-09-16-185500-…`. Cycle 15 build-2 (6)''s warm watch stays FAILED — the 132/152 warm re-run ran under a hand workaround, not the shipped surface. Rail issue #20 (`pageHashes` has no specified digest form) carries the cold-sweep cause. One owner call still outstanding under (3) — next: brief build 2; a build for #20 + the disposition-3 gap, then re-discharge (2) — BUILD 2 BRIEFED 2026-09-16 and BUILT 2026-09-17 on `cycle16-v0.19.0` (@ `6ab70b0`; F1–F17 landed, `frontmatter@14`→`@15`, package-lint A/B/C/E PASS, six-partner fixture PASSED its pre-written oracle and FAILS four ways against v0.18.1; four deviations recorded) — **`S-4` HARVESTED 2026-09-17, `verdict: proceed`**: `@path` imports in a vault-root CLAUDE.md load for every session kind probed (interactive, headless `claude -p`, in-session summon, Agent-tool subagent, workflow-`agent()` subagent, subdirectory cwd), transitively and root-relative, while a no-`@` pointer loads for none — A16-3 direction 1 grounded; the `SessionStart` fallback does NOT fire for in-session subagent spawns, and no size/depth ceiling was measured (A16-4''s question, left open on purpose). Artifact: `spike-s-4-claude-md-imports-2026-09-17.md` — next: brief build 3 — DONE. — **BUILD 3 BRIEFED 2026-09-17** (`briefs/build-3-carrier-and-tenants.md`; 18 F-sites, 13 brief-time dispositions, 8 acceptance checks appended to the ledger — 6 ship-verifiable GATE + 2 field-contingent, `specimens: 7/7`; five grounding corrections, one with scope consequences — `vlt-setup/SKILL.md:218`''s offer key would have kept the carrier out of every installed vault; `S-4` stamped **consumed**; promise does NOT narrow). Build 3 is the **release build**: v0.19.0 carries builds 2+3 whole (A10). next: **a fresh builder session implements the build-3 brief**'
module_code: 'vlt'
created: '2026-09-09'
updated: '2026-09-17'
derives_from:
  - 'factory/inbox/2026-09-03-124500-stub-heading-is-stated-inside-a-fence-so-a-faithful-section-scan-reads-located-no.md'
  - 'factory/inbox/2026-09-03-124600-lint-sources-reconciliation-writes-the-retired-bare-path-form.md'
  - 'factory/inbox/2026-09-09-160000-governance-has-no-partnerless-carrier.md'
  - 'factory/inbox/2026-09-09-160100-always-read-partner-memory-has-no-budget.md'
  - 'factory/inbox/2026-09-09-160200-partner-identity-has-no-owner-side-author-or-reset.md'
  - 'factory/inbox/2026-09-16-094501-research-is-not-a-lane-but-partners-enforce-one.md'
  - 'factory/inbox/2026-09-16-094502-no-seam-returns-worked-results-to-a-caller-who-keeps-the-wheel.md'
  - 'factory/inbox/2026-09-09-184840-rename-the-loop-profile-slot-non-negotiable-gate-to-write-gate.md'
predecessor: 'factory/cycles/15-nothing-reads-it-back/roadmap.md (Cycle 15 — CLOSED 2026-09-03, builds 1–7 shipped v0.18.0)'
intent: >
  Cycle 15 asked what happens when nobody reads a value back against the thing that specified
  it. Cycle 16 asks the question one step further in: what happens when the only reader a thing
  has is the hand that wrote it. Five filings, two surfaces, one shape. On the lint side, the
  sweep's own reconciliation wrote fifty-five frontmatter entries in a form the convention had
  retired eleven days earlier, and the checker that lives in the same skill flagged one of them —
  because the rule's legality is indexed on write date, which no reader can see in the bytes; and
  the stub-registry reader built last cycle to name a false negative re-manufactured the same
  false negative by reading the convention's own illustration as the convention. On the partner
  side, `ST-8`: a partner writes, is, and reads its own identity, the ladder only lifts material
  into the always-read set, and the rulebook rides the persona ritual — so the owner's escape from
  the loop, a partnerless session, is also an escape from the rules. Every one of these is a loop
  with no outside referent: no owner-side line in the file, no form clause at the writer, no
  fixture on the convention side of the read, no actor the contract names when the ritual is
  skipped. Cycle 15 said nothing reads it back. Cycle 16 says: and where something does, it is
  the writer reading itself. The 2026-09-16 addendum adds three filings of the same shape from the
  other direction: `ST-9`, where no rule states whether `{research}` is a lane, so partners wrote
  the nearest rule into themselves and now enforce it; where the cross-partner mechanism set was
  drawn on one axis and the cell it never drew — work moves, wheel stays — has no seam at all; and
  a template slot whose own description contradicts its key, re-explained by five wearers each
  inside their own profile, with no reader of the mismatch but the profile's author.
---

## The through-line

**Every filing in this cycle is a loop whose only reader is its own writer.**

The lint half is the sharpest instance because the loop closes inside one skill. `vlt-lint`'s
sources-vs-prose reconciliation **wrote** fifty-five `sources:` entries into twenty-two wiki pages
on 2026-08-26 (`{field-vault}` commit `dbd5292`, module 0.16.1), every one a bare `.md` path to a
`_agent/research/` note — the form `frontmatter.md` rule 4 retired on 2026-08-15. Three full sweeps
later, `vlt-lint`'s own `malformed_frontmatter` check flagged **one** of the fifty-five. Not because
that one differed — grounding read all fifty-five and they are byte-identical in form — but because
rule 4's *coexistence posture* makes an entry's legality a function of **when it was written**, and a
scanner reading a page's bytes cannot see when. The writer and the checker share a skill and a
convention and disagree about the form, and the checker's disagreement is arbitrary. (A16-2.)

The stub-registry read is the same loop from the other end. Cycle 15 build-3 shipped a procedure
that says *read the heading from the merged convention, never from memory* — and the convention
states the heading **inside a fenced illustration**, so a faithful section scan ends on the line that
carries the thing it was sent to read. The instrument built to name `located: no` honestly rendered
`located: no` on a wiki with a populated Stubs section, and was saved by an operator's judgment the
procedure never asks for. The fixture pair that shipped with the build grades the *index* side of the
read; the convention side, the side that broke, has none. (A16-1.)

The partner half is `ST-8`, three filings from one owner problem-solving session, and it is the
loop at its most literal. `## Self` is written by the partner, about the partner, in the partner's
voice, at sitting end, and loaded as instruction on every activation — there is no owner-writable
line in `identity.md` (A16-5). The promotion ladder has one axis: material moves *up* as it proves
durable, and the rung at the top below the wiki is the file every activation reads whole, so hygiene
is a ratchet into the always-read set — 19.8K words before the first user turn on the heaviest
partner (A16-4). And because the rule-card, the vault rung, and the sitting are all wired to the
activation ritual, the owner's escape from both — a session with no partner summoned, now the
owner's most productive shape for new thinking — reads one paragraph of governance and owes the
record nothing (A16-3).

Read the five by *who could have caught it* and the story is flat: nobody outside the loop was ever
given the job. The convention's form clause is not at the writer; the fixture is not on the
convention side; the charter is not the owner's; the budget has no instrument; the partnerless
session has no name. The module's honest-degradation posture — real, and working — cannot fire on a
loop that agrees with itself.

**Addendum, 2026-09-16 — three more, same shape, from the other direction.** `ST-9` is the loop
closed by *inference*: the contract never states whether `{research}` is a single-writer lane, so
partners resolved the silence against the nearest rule they could see (the wiki's), and the
resolution — *"that's the Researcher's lane"* — became a rule with no author but the partner that
obeys it (A16-6). Beside it, the seam that would have let that partner delegate a bounded dive and
keep the wheel was never drawn, because the mechanism set was designed on one axis — *does the
wheel move?* — and consult, relay, and hand-off looked complete from that side; the empty cell was
only ever a symptom, *research takes two sessions* (A16-7). Nothing outside the loop was given the
job of noticing either: the lane is in prose and memory, the cell is in no table. And the smallest
filing in the cycle is the same thing in one line: the loop-profile template's slot key says
`non-negotiable-gate` and its own description says *method gate, re-asserted at the write*; the
only reader who ever compared them was each wearing partner, alone, in its own profile, and five
of them wrote the comparison down there instead of anywhere the module could read it (A16-8, the
first rail issue admitted this cycle).

**Not a fifth study.** `ST-8` holds the partner-side cause in full and is cited, not re-derived;
`ST-9` likewise holds the lane-and-diagonal cause (A16-6/A16-7) and is cited at both entries.
The lint-side cause — *a coexistence posture indexed on write time has no at-rest enforcement point*
— is narrower than a study and is stated at A16-2 where it belongs; if a later filing finds the same
shape under another time-indexed rule, that is the moment to open one.

## Capture — 5 filings (grounded against module source 2026-09-09, at v0.18.0 @ `1e119a4`)

Every `file:line` below was re-derived this run against working-tree source. Two of the five filings
were drafted autonomously by `acceptance-discharge` on 2026-09-03 and filed without owner
confirmation (Cycle 15 closeout carry 8) — they are grounded here exactly as any other filing; one
of them had a second observation that grounding **refuted**.

Where a filing reported a count and the set was observable, the set was recovered by dereferencing
the named evidence in `{field-vault}`, read-only (P-18 Tier A's second grounding axis). It paid for
itself again: A16-2's *"22 reconciled, page set not recovered"* became 22 pages, 55 entries, and a
finding the filing could not have made from one specimen.

---

### A16-1. The stub heading is stated inside a fence, so a faithful section scan reads `located: no` (2026-09-03) — `factory/inbox/2026-09-03-124500-stub-heading-is-stated-inside-a-fence-so-a-faithful-section-scan-reads-located-no.md`

**GAP CONFIRMED on the heading site; the filing's second observation is REFUTED.**

**The procedure, grounded.** `skills/vlt-lint/references/checks.md:13` (the *Missing targets* bullet,
which homes the stub registry because it is the check that consumes the set): *"read the stub heading
**from the merged convention** (`{conventions}/wiki-index.md` §The Stubs section, plus its overlay if
present) — never from memory; locate in `{index}` the `## ` heading whose text equals it; collect every
backtick-wrapped slug in that section's list items up to the next `## ` heading; report
`section located: yes|no`."* Cycle 15 build-3 (A15-2) shipped this sentence.

**The convention site, grounded.** `skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md`:
`:78` `## The Stubs section`; `:80` the one prose sentence (*"Catalog these under a trailing section so
the gap is visible"*); `:82` a ```` ```markdown ```` fence opens; **`:83` `## Stubs (linked, not yet
written)`** — the heading literal, inside the fence; `:86` the fence closes; `:88` the backtick-slug
rule. Exactly as filed. A reader that takes *the text of §The Stubs section up to the next `^## `
line* terminates on `:83` — the heading it was sent to read is the line that ends its scan. The
convention never states the heading text **outside** a fence, and `checks.md:13` never says the
heading is stated inside one. Both halves of the read are prose; neither has a fixture on this side.

**What shipped for the read, and what it covers.** Cycle 15's fixture pair
`factory/cycles/15-nothing-reads-it-back/fixtures/build-3-index-stubs.md` /
`build-3-index-bare-stubs.md` grades the **index side** (long-form heading present vs bare `## Stubs`).
The convention side — how the reader obtains the heading text — has no fixture, and that is the side
that broke. The specimen is the filing's own: first discovery run `section located: false, 0 slugs`
(operator record, unpersisted); second read, by eye, persisted at `{lint_reports}/2026-09-03-1206-lint.yaml:6`
as `section located: yes (heading matched: "Stubs (linked, not yet written)" …); 6 slugs across 1 index`.
Set 1 of 1, fully recovered; the triggering fragment is the unpersisted first render, which is itself
the finding — a `located: no` that was overridden leaves no trace in the report.

**The second observation — REFUTED, with the convention's own text.** The filing reports that
`{field-vault}`'s index *"lists its stubs as `[[wikilinks]]`"* and asks capture to *"rule whether the
procedure's form or the index's is the one the convention mandates."* Grounding read the live section
(`{field-vault}/{index}`, §Stubs, 2026-09-09): every stub identifier is a **backtick-wrapped slug**
(`` `birria` ``, `` `jesse-minter` ``, `` `nfl-draft-safety-archetypes` ``, `` `jared-verse` ``,
`` `ms-celeb-1m` ``, `` `kliff-kingsbury` ``). The `[[wikilinks]]` the filing saw are the *linked-from*
pages inside each stub's description (*"linked from [[positionless-defense-nfl]]"*), which is what the
convention's own template says a description carries (`wiki-index.md:85`). The live index conforms to
`wiki-index.md:88`; the procedure's *backtick-wrapped slug* clause is the convention's own rule; there is
nothing to rule. (The filing's *"`imagenet` appears twice in the section's link text"* is the same
misread: `[[imagenet]]` appears in one stub's description twice, as a linked-from page.) **No module
change follows from the second observation**, and the capture records it so a brief does not build a
tolerance for a form the index never used.

**Residual scope (the filing's two directions stand, either one line):**
1. **Convention-side:** `wiki-index.md` states the heading text *outside* the fence — one sentence at
   `:80` (*the section heading is `## Stubs (linked, not yet written)`*). A prose clarification: no rule
   change, no `version:` bump, no consumer re-ack. **or**
2. **Procedure-side:** `checks.md:13` says the heading is stated inside the convention's fenced example
   and the reader takes the first `## ` line inside that fence.
3. **Either way: a convention-side fixture** — the `wiki-index.md` §Stubs bytes as the input, the heading
   string as the expected output — so the read that broke has a check on its own side of the seam. This
   cycle's `fixtures/` is where it lands (the cycle directory's shape is the map's).

**Cause.** `ST-7` — *prose-specified derivations have no read-back* — an instance arriving **inside the
build that answered it** (A15-2's repair was the procedure; the procedure's own input had no read-back).
Appended to `ST-7`'s `cited_by:`.

---

### A16-2. The lint's sources reconciliation writes the retired bare-path form — and the checker cannot tell which entries it wrote (2026-09-03) — `factory/inbox/2026-09-03-124600-lint-sources-reconciliation-writes-the-retired-bare-path-form.md`

**GAP CONFIRMED — and the recovered set changes the shape of the defect from a writer bug to a
writer bug *plus* an unobservable rule.**

**The rule, grounded.** `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:36` (rule 4,
`version: 14` at `:11`): a wiki page's `sources:` entry that references a vault note is *"a
**double-quoted wikilink** (rule 1) carrying the **full vault-relative path, no `.md`**"*, with the
coexistence posture the filing quotes — existing bare-path entries stay legal, no backfill sweep, a page
adopts the form on its next substantive edit. `:108` restates it in the schema comment (*vault notes as
"[[path]]" wikilinks, URLs plain — YAML rule 4*). Shipped 2026-08-15 (v0.10.0, B7-6).

**The writer, grounded — three states of one bullet.**
- **At the time of the write (module 0.16.1, `{field-vault}` 2026-08-26):** `fix-and-file.md` carried
  no sources bullet at all (`git show v0.16.0:skills/vlt-lint/references/fix-and-file.md` — no match).
  The only instruction was `checks.md:15` (v0.16.0): *"reconcile the prose section to frontmatter
  `sources:` — frontmatter is the source of truth."* The Librarian's sweep did the opposite — it wrote
  **frontmatter** from prose — and in the form the convention had retired. Neither the direction nor
  the form was stated at the writer.
- **One day later (`5122aa1`, 2026-08-27, Cycle 14 build-4; shipped v0.17.0 @ `c02fe3d`):** the direction
  was routed by the scanner's returned verdict. `checks.md:16` (today) is unambiguous: *"add the
  frontmatter `sources:` entries the prose `## Sources` section omits **to the prose section** — nothing
  is deleted; frontmatter is the source of truth … so the prose section is the side that moves."*
- **Today, `skills/vlt-lint/references/fix-and-file.md:12`** — the mechanics bullet `checks.md:16` points
  at — **contradicts itself in one paragraph.** Its first sentence is prose-side (*"add the frontmatter
  `sources:` entries the page's prose `## Sources` section omits, in the section's existing form"*); its
  next three are frontmatter-side (*"Each added entry is a **member of the existing `sources:` list** —
  never a new top-level frontmatter key … If `sources:` is absent, create it as a list … Re-parse the
  frontmatter after the edit"*). Those sentences only make sense for a write into frontmatter, which
  `checks.md:16` says never happens. A residue of the pre-`5122aa1` direction survived the routing
  edit, so the single home of the fix mechanics still half-describes the write that produced the
  defect — **and neither half names rule 4's form.**

**Specimen manifest — recovered to 22 pages and 55 entries, from the filing's 1.** The filing's
*"22 reconciled … the page set was not recovered by this filing"* was dereferenced against
`{field-vault}` commit `dbd5292` (2026-08-26, *"lint (librarian): full sweep — 146 pages, 22 reconciled,
2 filed"*, installed module 0.16.1). The commit touches exactly 22 wiki pages; every one of them gained
one to six lines of the form `  - _agent/research/<note>.md` inside `sources:` and **zero** lines in any
prose `## Sources` section. Complete set (page: entries added):

```
ai-ghost-work 1 · barbacoa 1 · career-history-as-evidence 3 · creatine-monohydrate 1 ·
dutch-oven-braising 1 · fantasy-platform-read-access 2 · myles-garrett 1 ·
nfl-2026-defense-rankings 5 · nfl-2026-draft-first-round 1 · nfl-2026-offense-rankings 4 ·
nfl-2026-player-outlook 3 · nfl-2026-position-rankings 1 · nfl-team-season-projection 5 ·
protein-intake 1 · seattle-seahawks 5 · shanahan-coaching-tree 2 · shanahan-offensive-system 2 ·
single-nutrient-claims 1 · technical-hiring-pipeline 4 · throne-of-glass-series-overview 6 ·
tog-characters 4 · training-set-politics 1                                    — 55 entries
```

(obtained by `git show dbd5292 -- resources/wiki/<page>.md`, counting added lines matching
`^\+\s+- .*\.md$`; every entry is a `_agent/research/` note, i.e. a **vault note** — rule 4 applies to all
55.) The triggering fragment is the filing's: the `dutch-oven-braising` line and the report entry at
`2026-09-03-1206-lint.yaml:218`. **Attrition: 55 observed by the field, 1 preserved by the filing.**

**The finding the set makes.** The 2026-09-03 full sweep — the first after v0.18.0, 145 of 146 pages
scanned cold — reported `malformed_frontmatter` on **one** of these 55 post-adoption entries. The other
54 are byte-identical in form, sit on 21 pages that scanned in the same run, and were not flagged. The
scanner's complaint on the one (*"YAML rule 1 & rule 4 violation … must be double-quoted wikilink
without .md"*) is correct; its silence on the 54 is not a judgment — it is the rule being unobservable.
Rule 4's legality is indexed on **write date** (pre-2026-08-15 entries legal, later ones not, and a page
adopts on its next substantive edit), and a page's bytes carry no write date per entry. On disk today
`{field-vault}` holds **240 bare-path `.md` entries across 83 of 146 wiki pages** (`sources:` scalars
ending `.md`, unquoted); some unknown majority are legal pre-adoption entries and 55 are not, and no
reader of the page can tell which. A per-page `malformed_frontmatter` flag on this class is therefore
**arbitrary** — it will name whichever page a scanner happens to notice, and the legal response the
convention states (*repair by hand*) is owed for 55 and forbidden as a sweep for the rest. **The
enforcement point for rule 4's form is the writer, and only the writer.**

**Residual scope (sharpened from the filing's one direction to three):**
1. **The writer states the form.** `fix-and-file.md:12` loses its frontmatter-write residue (or, if a
   frontmatter write is ever legal on this path, states rule 4's form for it in the same sentence) —
   a `checks.md:16`-consistent bullet. One paragraph; the F-site is exact.
2. **The checker's posture on bare-path entries is ruled, not left to chance.** Either the class is
   dropped from `malformed_frontmatter` (unobservable at rest ⇒ not a per-page finding) and surfaced as
   a **denominated census line** (`bare_path_sources: N entries / M pages` — the `attestation_census`
   idiom, `checks.md:18`), or the scanner verdict keeps it and the reduce refuses it by name as it
   refuses the attestation-only complaint. Ideation's call; the capture's read is that a count the
   owner can watch fall beats a flag the owner cannot act on.
3. **The 55 are the vault's to repair** — a hand pass or an owner-ruled one-time exception to the
   no-backfill clause, both vault-side. Not module scope; recorded so the field debt has a name. The
   module's contribution is (1), so the count stops growing.

**Adjacent, not captured — no filing.** The filing's closing note (*`sources_vs_prose_mismatches` refused
wholesale on consecutive sweeps; `{backlog}` carries a standing human ruling on four pages — a tier
question*) is Cycle 15 closeout carry 9, an operator finding awaiting its own filing. It is named here
because direction (2) above and that tier question touch the same reduce; a brief for (2) should read
the carry before it scopes.

**Cause.** Not `ST-2` (location-as-proxy) and not quite `ST-7` (this derivation *was* read back — once,
arbitrarily). Nearest shape: Cycle 14's *no enforcement point* — a rule whose legality depends on a fact
the artifact does not carry. Narrower than a study; stated here. `ST-7` is cited for the writer half
(the fix mechanics are prose an executor renders, and the rendering went the wrong way twice).

---

### A16-3. Governance has no partnerless carrier — a session without a partner reads a paragraph, not the rules (2026-09-09) — `factory/inbox/2026-09-09-160000-governance-has-no-partnerless-carrier.md`

**GAP CONFIRMED (candidate). One line reference corrected; one external unknown registered as `S-4`.**
Cause `ST-8` C — cited, not restated.

**Grounded, site by site.**
- **The rule-card read is a step of the ritual and nowhere else.** `vault-operating-contract.md:194`:
  *"Every partner, on activation, **first loads the rule-card** (`vault-rule-card.md` …)"*. The card
  frames itself the same way — `vault-rule-card.md:16` (*"Derived artifact … distilled from the shipped
  contract"*) and `:18` `## Becoming — the ceremony's frame` (the filing's `:15–17` is off by one to
  three lines; the claim holds). Grepping the shipped surface for any other reader of the card finds
  the ritual and the card's own frame; no operation skill and no seeded `CLAUDE.md` names it.
- **The vault rung is a Beat 1 read "by every partner".** Contract **`:226`** (the filing cites `:224`,
  which is the per-partner `reflexes.md` line): *"`_agent/reflexes.md` — the vault rung (always-loaded,
  read in Beat 1 by every partner)"*. Same conclusion, corrected line.
- **The sitting is defined on a partner.** `:267`: *"A sitting is one partner's continuous turn at the
  wheel; it yields one session note"*; `:269` *Ending a sitting* names the active partner as the writer
  of the note, the `{log}` entry, and the memory updates. No partnerless sitting exists in the section.
- **The schema half-anticipates it.** `frontmatter.md:167`, last sentence, verbatim: *"Omit only for a
  partner-less generic-agent session."* The session-log schema has a slot for the actor the contract
  never names — confirmed exactly as filed.
- **The seeded pointer is the whole carriage.** `skills/vlt-setup/SKILL.md:198–216` (§3): the seed
  (`:202–213`) says the rules *"live in `_meta/vault-operating-contract.md`; read it before writing
  anything"* — a pointer at a **67,844-character** file (`wc -c`, this run) with no card, no rung, no
  conventions; `:215` is the *user's file, additive heading-scoped edits only* rule the filing's
  direction 1 would ride on. The rule-card is **1,076 words** (`wc -w`).
- **Ops run partnerless today.** `skills/vlt-ingest/SKILL.md:24`: *"If invoked standalone with no
  partner, omit the tag."* Confirmed; the gap is carriage, not operation.
- **Field evidence, re-counted.** `{field-vault}/{sessions}` holds 246 notes: 244 partner-tagged across
  nine roster partners, 1 `partner: user`, 1 `partner: vlt-mint` (the filing's *~240* and *1 + 1* hold).
  The owner's partnerless brainstorm sittings wrote no note by construction — there is nothing to count,
  which is the finding.

**The external unknown — registered, not assumed.** Direction 1 (import lines in the seeded `CLAUDE.md`)
rests on whether `@path` imports in a vault `CLAUDE.md` load for **every** session kind the module
runs — interactive, headless op, partner summon, subagent. That is a runtime fact, not a module fact,
and CLAUDE.md step 3 says read the runtime, not its docs. Opened as **`S-4`**
(`factory/platform/spikes/S-4-vault-claude-md-imports-per-session-kind.md`, `proposed`). The fallback
the filing names is grounded: `vlt-setup/SKILL.md:187` registers a `SessionStart` hook
(`vlt-vitals.py --strip`) that already fires per session — the card can ride it if imports do not.
**Direction 1 is ungrounded pending `S-4`**; direction 2 (the `partner: none` sitting in the contract)
does not depend on it. Whether `S-4` binds a build is ideation's ruling; whether it blocks a brief is
`build-brief`'s gate.

**Residual scope — the filing's shape, unchanged by grounding:**
1. Carry governance on a surface every session reads — pointers to the card and the rung, never copies
   (single-home holds); mechanism per `S-4`.
2. Name the `partner: none` sitting in the contract (*Sessions, sittings, and hand-offs*): one session
   note, log tag `(session)`, no partner-memory writes, wiki single-writer still holds; optional
   `purpose:`. `frontmatter.md:167`'s *omit* becomes an explicit value — **a rule change to
   `frontmatter@14` ⇒ `version:` bump + every consumer re-acked in the same build** (the version
   handshake; ideation should group this with A16-4/A16-5's schema edits so the bump happens once).
3. Ops unchanged.

**Open design questions (carried verbatim, not resolved):** whether `purpose:` is worth a field or a
free-text line in the note; whether a `partner: none` sitting should read `_agent/dispatch.md`'s open
slice (it has no addressee, so probably not — but the contract should say).

---

### A16-4. The always-read partner memory has no budget — groom is a ratchet, and `identity.md` is 70% of Beat 1 (2026-09-09) — `factory/inbox/2026-09-09-160100-always-read-partner-memory-has-no-budget.md`

**GAP CONFIRMED (candidate), with one PROVENANCE CORRECTION: an instrument *does* see partner-memory
mass — fleet-wide, display-only, and with no budget behind it.** Cause `ST-8` A — cited, not restated.

**Grounded, site by site.**
- **`identity.md` is evergreen and Beat 1; `## Self` is ungated; no cap field.** Contract `:214`
  (*"evergreen (read in Beat 1)"*), `:217` (*"lightweight, **ungated** identity drift … A partner writes
  this freely"*), `:196` (Beat 1 reads it whole, *modulated by*). `frontmatter.md:187–195`, the
  `identity.md` schema: `type`, `partner`, `name`, `created`, `last_updated`, `groomed`, `archive` —
  no cap, no budget, no size field.
- **Only `reflexes.md` is capped, by line.** Contract `:224` (*"one line per rule, hard-capped"*);
  `frontmatter.md:224–225`: `cap: 30 # … at most 30 one-line rules` and the falsifier, verbatim:
  *"if … reflexes routinely exceed one line, the cap value (or the one-line form) is mis-set — file
  it."* The filing's Researcher specimen (`cap: 30`, *"30 of 30 — at cap"*, 1,060 words ≈ 35 words per
  "one-line" rule) is the falsifier fired, and this filing is the *file it* the falsifier asks for.
- **The ladder only lifts.** Contract `:228–238` (the rung table — remark → thread note → standing read
  → reflex → fleet rung → identity → wiki; no rung *below* Beat 1 for durable-but-not-always-needed
  material) and `:240` (*"The three verbs. promote — move material up a rung … compress-to-latest-form
  … retire"*). `skills/vlt-groom/SKILL.md:4` restates the same three; **`grep -n "reset\|demote"`
  across `vlt-groom/SKILL.md` and `references/` returns nothing.** No verb moves material down.
- **Beat 2's bound.** Contract `:198`: *"`thread.md` `## Thread` **only** (the open inquiry — `## Set
  aside` is pruned attention, not an orient read)"*. The bound exists and is a section, not a size;
  the filing's *~9% excluded* on the heaviest thread is a field measurement this run did not repeat.
- **The instrument — corrected.** The filing says *"`vlt-vitals.py:203`'s `METRICS` table has no
  activation-weight metric"*. `METRICS` opens at `:203`, and **`:242` carries `partner_memory_bytes`:
  *"total bytes of per-partner identity.md + thread.md + reflexes.md + capabilities/ under {partners}
  (display-only size vital)"*** (computed at `:742`). So an instrument sees the mass — as **one fleet
  total, in bytes, display-only, never wired**. What the filing asks for and the module lacks is
  **per-partner**, **Beat 1-subset** (SKILL.md + `identity.md` + `reflexes.md`, not `thread.md` or
  capabilities), and a **bound** a wire can trip on. The correction narrows the ask, it does not
  dissolve it. `tripwires.yaml:32–58` confirms the vault could already declare a `bytes`/`path` local
  metric on one `identity.md` (B10-4's kinds) — one file, one number, no per-partner derive, no
  budget; and the seed ships no `local_metrics` (`:58`).
- **The contract solved this for itself.** `vault-rule-card.md:16` — the 67,844-character contract
  distilled to 1,076 words and opened point-of-use. Confirmed; partner memory has no card.

**Specimen manifest — carried as filed (9 of 9 partners, words, `wc -w` 2026-09-09).** The set is
complete in the filing and was not re-measured this run; the fleet-wide `partner_memory_bytes` figure
this run *could* have read is the wrong unit (bytes, fleet, includes `thread.md` and capabilities) to
corroborate a Beat 1 word table, which is itself the instrument gap. The triggering fragment (the
football-analyst's `## Self` at 7,195 words, 28 dated first-person case narratives) stands as filed.

**Residual scope (the filing's four directions, one adjustment):**
1. **A second axis — a Beat 1 budget.** The contract declares a word bound for the always-read set;
   `vlt-vitals` gains a **per-partner `activation_words`** canonical metric (the route
   `tripwires.yaml:12–18` names — a new id in `METRICS`, never a hand-edit of the reader); a shipped
   wire trips on it; `vlt-lint` reports it. *Adjustment:* `partner_memory_bytes` at `:242` is the
   neighbouring metric — a brief should say whether the new one replaces, refines, or sits beside it.
2. **The missing verb — demote**, and the rung it needs: a **casebook** below Beat 1 (never wake-read,
   point-of-use, with a decay contract per the contract's *Decay contracts* section) for dated
   narratives, and the wiki/PARA profile (Librarian hand-off) for owner-model material.
3. **`identity.md` becomes the card** — capped `## Self` (manner only) and `## Bond` (relationship facts
   only), mirroring the contract's card + point-of-use pattern; migration a groom act per partner, by
   reference, approval-gated (`:304` — council-free, lossless-by-reference).
4. **Rider:** the reflex cap counts words (`cap_words:`), per its own falsifier — its `review_after:
   2026-11-17` (`frontmatter.md:226`) is the n=1 recalibration expiry the falsifier was written for.

Every direction touching `frontmatter.md`'s partner-memory schema is a **rule change to
`frontmatter@14`** — one bump, all consumers re-acked, grouped with A16-3/A16-5.

**Open design questions (carried verbatim):** the budget value is an owner ruling — the filing's
defensible first bound is *the light partners' median ×2 (~12K words)*, to be tightened on the
instrument; whether the casebook is a fourth memory file or a section of `thread.md` below `## Set
aside`; whether `## Bond`'s owner-model material migrates to the wiki (single-writer, Librarian hand-off)
or to a PARA area the partner may write.

---

### A16-5. Partner identity has no owner-side author, no reset, and no cold summon — the partner writes, is, and reads itself (2026-09-09) — `factory/inbox/2026-09-09-160200-partner-identity-has-no-owner-side-author-or-reset.md`

**GAP CONFIRMED (candidate), every site as filed.** Cause `ST-8` B and the amplifying cause — cited,
not restated.

**Grounded, site by site.**
- **Self is partner-authored and ungated; no owner-writable section.** Contract `:217` verbatim (*"A
  partner writes this freely, like a `## Bond` note"*); `frontmatter.md:187–195` — the schema has
  `partner`, `name`, dates, `groomed`, `archive`, and the two sections `## Bond`/`## Self`; nothing the
  owner owns.
- **The two-tier line has nothing in the middle.** `:246`: *"Drift in `## Self` is free and
  reversible. Changing who the partner fundamentally is … a deliberate, council-gated edit to its
  SKILL.md (via `vlt-mint`)."* *Reversible* names no verb: `:240`'s three are item-wise, and
  `vlt-groom` has no whole-section act (grep for `reset`, `demote`, `charter`, `cold` across
  `skills/vlt-groom/` — zero matches).
- **Three activation postures, none cold-by-choice.** `:202` cold start (first meeting — *identity.md
  carries only its seed placeholders*), `:204` cold × headless (defer the ceremony), `:206`
  partner-invoked (skip the greeting). Each reads `identity.md` when it has content; none lets the
  owner summon a mature partner without its Self, Bond, and Thread.
- **Statefulness is uniform.** No field in `frontmatter.md`'s partner-memory schema (`:183–230`) and no
  sentence in the contract's *Partner memory* section lets a partner or a mint declare how stateful it
  is. Confirmed by absence.
- **Field evidence.** Carried as filed (the Researcher's `## Self` opening *"The correction-of-framing
  edge — my signature move"*, the football-analyst's 28 narratives); not re-read this run beyond the
  session census at A16-3.

**Residual scope (the filing's four directions, unchanged; cross-filing dependencies named):**
1. **`## Charter`** — owner-written (or minted, then owner-editable), first in Beat 1, owner write
   posture (the `writers:` test PARA containers use); `vlt-groom` checks `## Self` against it and
   proposes **demotion** of off-charter material — **depends on A16-4 (2)'s demote verb**; `vlt-lint`
   flags partner edits to it. **Adoption:** every existing partner's `identity.md` lacks the section —
   the contract's *Adoption postures* (`:244`) make it legal-until-groomed; `vlt-setup`/`vlt-upgrade` may
   seed an empty `## Charter`, never author one (durability posture: merge-not-replace, and the
   B1 local-mint preserve path is in play).
2. **`vlt-groom --reset self|bond|thread`** — whole-section retire by reference, `archive:` watermark,
   approval-gated, council-free per `:304`; leaves `name` and the charter.
3. **A cold summon** — a fourth posture beside `:202–206`: Beat 1 reads SKILL.md + charter + rule-card
   + rung only; the sitting is tagged `cold`, writes its note and log line, writes **no** identity or
   thread drift. Per-summon, never per-partner. **Pairs with A16-3:** the cold summon is the governed
   form of the fresh-eyes move that the partnerless session currently provides ungoverned.
4. **`memory: full | reflexes | none`** as an `identity.md` frontmatter posture — pilot on the
   Researcher, not fleet; `vlt-setup` seeds `full` for every existing partner; `vlt-mint` asks at mint.

All four are `frontmatter@14` rule changes (new section, new field, new sitting tag) — grouped with
A16-3/A16-4 for one bump.

**Open design questions (carried verbatim):** whether the charter is minted (from `vlt-mint`'s partner
ideation beat) or blank at birth; whether `cold` is a `partner:` modifier or its own `sitting:` field on
the session note; the breadth measure for the Researcher pilot (*distinct source domains per dive over
five dives before and after*) — and the filing's own note that **a null result is a finding** relocating
the cause to `vlt-research`'s search discipline.

---

### Capture addendum — 3 filings (grounded against module source 2026-09-16, at v0.18.0 @ `b46d48b`)

Appended by the 2026-09-16 `inbox-capture` run, before ideation resumed (the owner held round 1 open
for exactly this). Numbering continues the cycle's sequence. Two of the three were written by the
factory itself from the owner's problem-solving session and arrive with a grounding of their own at
`caea0d5`; that grounding is **not** this capture's — every site below was re-derived against the
working tree (`git diff --stat caea0d5 HEAD -- skills/` is empty, so both readings are of the same
bytes, and the differences recorded here are sharpenings, not drift). The third is the first rail
issue admitted this cycle (#19), materialized by this run's intake.

---

### A16-6. `{research}` is not a shared lane, but partners enforce one — the lane status is unstated and the belief lives in memory (2026-09-16) — `factory/inbox/2026-09-16-094501-research-is-not-a-lane-but-partners-enforce-one.md`

**GAP CONFIRMED (candidate). Every cited line holds; one section-only citation pinned; the
filing's own recovery path for the belief was run and found nothing — that negative is the one
thing grounding adds.** Cause `ST-9` B + amplifying — cited, not restated; this capture appended
to its `cited_by:`.

**Grounded, site by site.**
- **No single-writer rule covers `{research}`.** `vault-operating-contract.md:64` names `{research}`
  notes in the Layer-2 sentence beside the wiki and restricts *only* the wiki (*"a Librarian-only
  zone: the Librarian is its only writer"*). `:255` defines a shared lane as *"a synthesized,
  single-writer lane — the wiki above all"*; `:139` makes research notes dated snapshots, *"not
  promoted"*. Confirmed as filed.
- **The op tags the active partner.** `skills/vlt-research/SKILL.md:17`, verbatim: *"Note the
  **active partner** for the log tag."* `:32` is the partner-fronted mode; `:94–97` writes
  `research (<partner>)`; `:100` writes no session note. Contract `:155` lists `research` as an
  ordinary log type. Confirmed.
- **Attestation is unconstrained there.** `conventions/write-verification.md:47` (*"unconstrained
  where none declares"*); `grep -rn "writers:"` over `skills/vlt-setup/assets/` and `skills/vlt-lint/`
  returns no research-scoped posture (this run). A non-Researcher attesting `verified_by:
  vlt-research` is legal today. Confirmed. Current handshake values the filing's acceptance names:
  `consult@1` (consumers `vlt-dispatch`, `vlt-lint`), `frontmatter@14`, `write-verification@6`.
- **The belief's author, in module source.** Contract `:253` (*"must be owned by that lane's rightful
  partner"*) and `:257` (*"Ownership = location"*); `vlt-agent-researcher/SKILL.md:37` (*"Run
  `vlt-research` … This is your main work"*). **Creative `:37` — pinned and narrowed.** The clause
  is the tail of the *Shape a PARA deliverable* bullet: *"A thin topic (fewer than 2 contributing
  wiki pages) is a **cue**, surfaced to the user: send them to the Librarian or Researcher first
  rather than thinning out an artifact — a caveat you name, not a refusal."* It is a thin-wiki cue
  for **extraction**, not a research prohibition. The filing's reading (a route-away) is fair — the
  only remedy the sentence names is another partner — but the fix is a wording change to the named
  remedy, and the *surface to the user* posture stays. Hygiene row `:318` (*"Wiki + research"* under
  the wiki lane's machinery) confirmed.
- **The read-and-cite paragraph the filing names by section is `:282`** (*"Read-and-cite is the
  documented default"*); the consult mechanism is `:284`. The rule-card rows that point there are
  `vault-rule-card.md:30` (authority boundary) and `:50` (the *Sessions* reading-list row).
- **The rung is seeded and never rewritten.** `skills/vlt-setup/SKILL.md:275`: create `_agent/reflexes.md`
  *"if absent … never touch an existing populated file"*; contract `:226` names it the Beat 1 read
  for every partner. Confirmed — and it makes disposition 2 reach **new vaults only** unless an
  upgrade-side additive step is ruled (Q16).
- **Where the belief lives — the filing's recovery grep, run.** The filing says a capture wanting a
  set *"can grep `{partners}/*/identity.md` for `Researcher` under `## Self`"*. Done, read-only, nine
  files: `Researcher` near `lane` → **0 hits**; `Researcher` at all → four files (chef 1, creative 1,
  football-analyst 5, librarian 3), every hit a hand-off, relay, or addressing context, none a lane
  statement. **The set stays count-only and the proposed recovery path is closed.** ST-8 cause B's
  mechanism (belief written into `## Self`, read back as instruction) is therefore *inferred* for
  this instance, not observed; the owner's report of partner speech is the whole evidence. The
  evidenced author is module source — the listing and the *Capabilities* prose. This does not
  weaken dispositions 1/3/4/5; it means disposition 2 ships against an inferred cause (E7).

**Residual scope — the filing's five dispositions, shape unchanged, one narrowed:**
1. **State the lane, once** — one sentence in *Capabilities* (`:248–259`): `{research}` is not a
   shared lane; any partner may run `vlt-research`, tagged as itself. Contract prose; the contract is
   deliberately unhandshaked — no bump (verify at brief, as filed).
2. **Reach the memory** — one pointer line on the vault rung. Seed site `vlt-setup:275`; reaches
   existing vaults only by a ruled additive step or by hand (Q16).
3. **Fix the cue's remedy** — Creative `:37`: beside *Librarian or Researcher*, name *delegate a dive
   (A16-7) or search-and-cite for a single fact*; the cue itself stays.
4. **Disambiguate the hygiene row** `:318` — a clause: decay machinery, not write ownership.
5. **Extend read-and-cite to the web** at `:282` — a single fact fetched and cited inline in the
   caller's artifact with a `sources:` entry; anything that should be *findable later* earns a note.
   **The blind spot is stated in the rule** (prose bound, no instrument; the delegate record is the
   visible half). Dissent on record, kept: the tier is an honor-system hole (Quinn).

**Open design questions (carried, plus two grounding raised):** how the rung line reaches a populated
rung; whether the web extension's blind-spot sentence is enough or wants a lint census it cannot
have; whether Creative `:37` keeps *surfaced to the user* and changes only the remedy (capture's read:
yes).

**Acceptance as filed** — all ship-verifiable at rest: greps for the *Capabilities* sentence, the
rung seed line, Creative `:37`, the `:318` clause; `package-lint` handshake bipartite-consistent
with `consult@1` / `frontmatter@14` / `write-verification@6` unchanged. Field-contingent, **watch
not gate**: a partner that formerly declined now runs, delegates, or cites.

---

### A16-7. No seam returns a worked result to a caller who keeps the wheel — a one-fact gap costs a second session (2026-09-16) — `factory/inbox/2026-09-16-094502-no-seam-returns-worked-results-to-a-caller-who-keeps-the-wheel.md`

**GAP CONFIRMED (candidate). Every cited site holds; one site the filing did not name is added;
the neighbour list it would extend lives in a versioned convention, which raises a handshake
question the filing did not ask.** Cause `ST-9` A — cited, not restated; this capture appended to
its `cited_by:`. Companion: A16-6 (the lane half).

**Grounded, site by site.**
- **Consult is read-only by identity.** `conventions/consult.md:27`: *"A consult transfers
  **nothing**."* Its neighbour list is `:29–32` — relay, hand-off, council — each by *what moves*; a
  fourth neighbour lands there. `skills/vlt-dispatch/references/consult.md:7` (*"a `relay` whose drain
  happens immediately"*), **`:63`** verbatim: *"**`needs-work`** → the caller writes the handoff doc
  and fires the existing **`relay`** path. Consult answers; relay assigns"*; `:89` no session note
  from the summoned partner; `:15` a human may invoke directly, never unprompted. Confirmed.
- **Relay is asynchronous by identity.** Contract `:286` (two timings), `:290` (the relay-when-done
  reflex — the recipient *"drains it via the ordinary pickup loop"*). Confirmed.
- **Hand-off moves the wheel.** `:267` (*"ends one sitting and begins another"*);
  `vlt-agent-researcher/SKILL.md:66` *Partner-invoked* mode. Confirmed.
- **The sentence the 2×2 extends is `:288`**: *"Both timings **transfer work**, which is what makes
  them hand-offs. A **consult** is neither: it transfers none…"* — the contract already reasons on
  the two axes in one sentence and names three of the four cells. The empty one is a sentence away.
- **The engine shape exists.** `skills/vlt-setup/assets/workflows/vlt-consult.js:19` (*"Depth-1 is
  STRUCTURAL, not an honor system: this workflow spawns exactly ONE"*), `:24` (return union *forced
  by the schema*), `:57` (parse-on-intake — the standing rule), `:138` (the lite boot), `:10` the
  `// depends_on: []` header line `package-lint` reads. Confirmed; a clone is the filing's shape.
- **The op is delegable as-is.** `vlt-research/SKILL.md:50` (`.WIP` checkpoint by interruption
  risk), `:94–100` (caller-tagged log line, no session note), `:102–104` (the Phase 6 Librarian
  hand-off offer — the runner must *not* take it, depth-1), note frontmatter `:60–64` (`type:
  research`, `trust: raw`) — **no `partner:` field**, and `frontmatter.md:133–148` (§Research notes)
  declares none. *"Do not touch `frontmatter@14` for this"* is confirmed, not assumed.
- **A site the filing did not name.** `skills/vlt-dispatch/SKILL.md:13–16` lists four modes and
  **`:18`** says *"All four modes are **the same machine**"* — a fifth mode edits the list, that
  sentence, and the `module-help.csv:13` row (quoted fields). `module-help.csv:7` is the research row.
- **Carrier dependency confirmed.** §A16-3 above; `S-4` `proposed`. A delegate runner is an instance
  of that carrier — the filing's *never a second carrier* is the right constraint and this capture
  makes it a decide-once (D6).
- **Specimen manifest.** Count only, honestly stated as filed: the owner's report of multi-session
  task closes; no instrument persists it (E8). The minimal triggering fragment is `:63` above.

**The handshake question grounding adds.** `conventions/consult.md` is `consult@1`, consumers
`vlt-dispatch` and `vlt-lint`. Adding delegate to the neighbour list at `:29–32` changes no rule —
the class definition (`:23–27`) and the trigger pointer (`:36`) are untouched — so it reads as a
prose clarification, **provided delegate is a sibling and never "a consult that does bounded work"**
(the `consult@2` alternative `ST-9` rejects). The brief verifies bipartite consistency either way;
ideation rules which (Q18).

**Residual scope — the filing's seven dispositions, shape unchanged:**
1. Publish the 2×2 in *Sessions* at `:288` and name the fourth timing, **delegate** — bounded work
   moves, the wheel does not, no sitting boundary, no session note from the runner.
2. Population cut, not enumeration (Arc 9 D5): delegate targets only ops whose write target is not a
   shared lane. v1 tenant `vlt-research`; the contract states the rule, the mode states the tenant.
3. `vlt-dispatch` mode `delegate` — `references/delegate.md` single home for mechanics; engine
   `vlt-delegate.js` cloned from `vlt-consult.js` with its `depends_on` header; inputs `op` (v1
   `research`), `question`, `depth` (`quick|moderate`), `groundIn`, `why`, `fromSlug`; return union
   `done{notePath, headline, verification, wikiCandidate} | incomplete{wipPath} |
   insufficient-context | needs-human | too-big`; `deep` → `too-big` → relay. The runner never offers
   or performs the Librarian hand-off; the caller relays on `wikiCandidate`. Never unprompted.
4. Runner partnerless, always; no `remember:` variant (rejected, on record in `ST-9`); attests
   `verified_by: vlt-research`; governance carriage is A16-3's — sequence with or after it.
5. Record: pre-checked `delegate:` block in `_agent/dispatch.md` (never on the ledger by
   construction); two `{log}` lines both tagged with the **caller**; no session note; no
   `frontmatter@14` change.
6. Redirect the trapdoor: `references/consult.md:63` → *delegate if bounded, relay if not*;
   `conventions/consult.md:29–32` gains the neighbour (Q18).
7. Pointers only: Creative `:37` (A16-6), rule-card `:50`, `vlt-dispatch/SKILL.md:13–18`,
   `module-help.csv:13`, `CHANGELOG`.

**Dissents on record (roundtable), carried:** Victor — generalize `op` now (rejected by the
population cut; a second tenant is a separate ruling). Sally — an orphaned `.WIP.md` from an
interrupted runner has no decay contract (true today for headless too; `incomplete{wipPath}` makes it
visible; **watch**, not build).

**Open design questions (carried verbatim):** the 2×2's wording and whether the section gains a
table; whether `delegate:`'s header shape is the mode signal as `relay:` is; whether a human-invoked
delegate (debugging) tags `(user)`.

**Acceptance as filed** — ship-verifiable at rest against a temp-vault fixture: exactly one agent
spawned; typed return honoured on a thin payload (`insufficient-context`), on `deep` (`too-big`), on
a real quick dive (`done`) and on a forced interruption (`incomplete`); one `delegate:` block written
pre-checked and absent from `ledger`; two caller-tagged `{log}` lines; no session note; the note
passes tier-1 and carries `verified_by: vlt-research`; nothing written under `{wiki}`, no relay
fired. Prose agreement by grep: contract 2×2, `:63` routing line, the neighbour list, rule-card
`:50`. Field-contingent (**watch**): first live `delegate:` block in `{field-vault}` from a
non-Researcher partner; open relay pointers to `researcher` from other partners fall toward the
`deep`-only residue.

---

### A16-8. Rename the loop-profile slot `non-negotiable-gate` to `write-gate` (2026-09-09, rail issue #19, materialized 2026-09-16) — `factory/inbox/2026-09-09-184840-rename-the-loop-profile-slot-non-negotiable-gate-to-write-gate.md`

**CONFIRMED (defect). The provenance guess is confirmed to the exact line of the 2026-06-25 lift;
one site the filing did not name is added; the field wearer set is recovered at five, and the
filing's apology count is corrected from three (the council's) to two on disk.** No study: nearest
is `ST-7` (a derivation specified in prose with no read-back — the key and its own description
disagree in one line and nothing reads one against the other), but the cause is a lift-time naming
error, narrower than a study; not opened.

**Grounded, site by site.**
- **The template line, verbatim.** `skills/vlt-mint/assets/capability-template.md:68`:
  `- non-negotiable-gate: <this partner's named method gate — re-asserted at the write, e.g.
  least-intrusive / never past the evidence>`. Key says *non-negotiable*; description says *method
  gate, re-asserted at the write*. Confirmed exactly as filed.
- **`vlt-track` reads the slot by description, not by key.** `skills/vlt-track/SKILL.md:38`: *"the
  **non-negotiable gate** — the calling partner's specific method gate, named in its profile … Apply
  it at the design beat **and** re-assert it at the write — it is the gate that decides whether a
  method may be written"*. There is no literal key parse anywhere in the shipped surface: `grep` of
  the profile keys over `skills/vlt-lint/` and `skills/vlt-setup/assets/hooks/` returns nothing — **no
  checker reads loop-profile keys**. So a deprecated alias is nearly free, and the rename is a prose
  edit at `:38`. The conflation is also in the op's own framing, `:15`: *"The calling partner brings
  the voice and the non-negotiable."*
- **A site the filing did not name.** `skills/vlt-upgrade/SKILL.md:81` — the *loop-profile relocation*
  human-gated offer identifies a profile by its characteristic keys, enumerated: `root` / `target` /
  `subject-model` / `data-streams` / `log-tag` / **`non-negotiable-gate`**. A renamed profile that
  drops the old key would fall outside this scan's signature; the list must accept either key.
- **Provenance confirmed to the line.** `factory/cycles/00-origins/briefs/build-11-vlt-track-upstream.md:106`
  carries `- non-negotiable-gate: <this partner's named method gate, re-asserted at the write>` at
  the 2026-06-25 lift of `vlt-track` from the field vault; `build-22-mint-and-wearer.md:283` repeats
  the key list. The filing's guess — *"the name likely dates from that lift"* — holds.
- **No handshake.** `vlt-track` `depends_on: ["extraction@10", "wiki-supersession@2"]`; the template is a
  `vlt-mint` asset, not a governance convention. A rename bumps nothing.
- **Field wearer set, recovered** (read-only, `{field-vault}/{partners}/*/capabilities/track.md`):
  **five** wearers. Bare key, no note: `dog-trainer:20` (*least-intrusive / LIMA*), `health-coach:25`
  (*never past the evidence*), `chess-coach:30` (*invent nothing*). Apology present:
  `career-strategist:37` + `:48` (*"the profile slot is named `non-negotiable-gate` in the template
  … same mismatch as an upstream schema defect"*), `football-analyst:181–182` (*"slot named
  `non-negotiable-gate` by the shipped schema … **moot** as of this mint — the partner's
  non-negotiable and its write-gate are the same rule"* — the rebuilt partner the filing calls
  accidentally honest). Council record `_agent/mint/decision-log.md:739`, verbatim: *"Upstream
  `write-gate` slot-name bug — third occurrence, and the note must not be written a fourth time …
  Chess and Football each already carry the apologetic parenthetical; this is the third copy … the
  filing has no owner and no date."* **Attrition:** the record counts three apologies (Chess,
  Football, Career Strategist); disk today holds two — `chess-coach:30` carries the bare key and no
  note, so one copy was removed or never landed. Neither count changes the defect; the filing's
  *"three wearing partners"* is the council's count and is recorded as such.
- **"No filing had been posted" — confirmed.** The intake found no `origin:` for #19 on disk, and
  `grep -rl write-gate` over the inbox and every `filings/` finds only the filing this run wrote.
  The decision-log's *"standing upstream filing"* referred to nothing until 2026-09-09.

**Residual scope — the filing's proposal, with the added site:**
1. `capability-template.md:68`: key `non-negotiable-gate` → `write-gate`; description unchanged (it
   is already right).
2. `vlt-track/SKILL.md:38` names the slot `write-gate` and accepts `non-negotiable-gate` as a
   deprecated alias (lifetime: Q20); `:15`'s framing considered with it.
3. `vlt-upgrade/SKILL.md:81`: the relocation scan's key list accepts either key.
4. `CHANGELOG` field notice so wearers rename at leisure. **The five profiles are the vault's to
   rename** (durability: a partner's capability file is never rewritten unasked) — unless ideation
   rules a human-gated offer in the `:79–84` migration list (Q21).

**Open design questions:** alias for one release or indefinitely (Q20); the `:15` framing; the
upgrade offer (Q21).

**Acceptance.** Ship-verifiable at rest: greps for the template key, the `vlt-track:38` read naming
both keys, the `vlt-upgrade:81` list. The filing's own acceptance clause — *a coaching-style wearer's
profile parses under the new key and the old key with no explanatory note needed* — is
field-contingent: **watch**, not gate; `acceptance_vault` as filed (any vault with a wearer whose
live non-negotiable is not its write-gate).

---

### Grounding corrections — build-2 brief (2026-09-17)

Appended by `build-brief` at build-2 brief time (second grounding, per `grounding-at-brief-time.md`).
Module source moved between the 2026-09-16 ideation/roundtable and today — build 1 shipped v0.18.1 in
between. The capture bodies above are append-only and are **not** rewritten; these notes supersede the
stale line refs they name. None of them contradicts a ruling; the brief carries each inline.

- **`vlt-lint-full.js:297/:299` → `:321`/`:323` (and a third literal at `:946`).** D1 and roundtable
  A10 cite the pre-build-1 line numbers for the `frontmatter@14` literals inside the scanner prompt.
  Build 1's v0.18.1 moved them. **Superseded** — the build-2 brief's F2 re-acks three literals at the
  fresh lines. A10's *conclusion* is unaffected: the re-ack still moves `scanFingerprint`.
- **Contract `:154`/`:159` → `:155`/`:156`.** Roundtable A8's cites for the `{log}` `<type>` set and
  the paren-omit clause. **Superseded**; F6 edits `:156`.
- **Contract `:312` → `:316`.** The A18 count-word sweep list's cite for the partner-memory decay row.
  **Superseded**; A11's separate `:314` cite (the dispatch row's `consult:` retention) HOLDS.
- **`vlt-consult.js:141` → `:143`** (the lite boot's one write exception). **Superseded**; F16 cites
  the fresh line. `:136`/`:138` HOLD.
- **`vlt-setup/SKILL.md:215` → `:217`** (the *user's file, additive heading-scoped edits only* rule,
  A16-3's capture). **Superseded**; informational for build 2, live for build 3.
- **`partner-agent-template.md:111` → `:112`** for the `## Self` seed instruction (`:111` is the
  heading). **Superseded**; F13 deletes `:112`'s clause per dispute D-11.
- **D9 and R1 name the wrong `vlt-upgrade` steps.** D9 sites the additive-write class in *"Step 5"*
  and R1 homes its rule in the *"Step-4/Step-5 durability posture"*. Current source: **Step 5
  (`:136`) is the standing divergence ledger**; the migration list is **Step 3 item 5** (`:77-84` —
  D9's own `:79-84` cite points correctly into it) and *"never auto-rewrite a partner's body"* is
  **Step 3 item 4** (`:72`). **Superseded on the step numbers only — the substance stands**, and the
  brief's F15 lands both in Step 3. No re-ruling is owed.
- **Grounding additions (sites the A18 sweep list missed):** `groom-pass.md:9` (*"any of the three
  memory files"*) and `vlt-setup/SKILL.md:225` (*"create the three memory files if absent"*) are in
  scope for the count-word sweep. `vlt-groom/SKILL.md:4` carries **no count word** and needs no edit —
  the roadmap's list named it.

### Grounding corrections — build-3 brief (2026-09-17)

Appended by `build-brief` at build-3 brief time. Build 2 shipped on `cycle16-v0.19.0` (`6ab70b0`)
between the roundtable and today, moving the operating contract and the consult engine. The capture
bodies above are append-only and are **not** rewritten; these notes supersede the stale refs they
name. Neither contradicts a ruling; the brief carries both inline.

- **`conventions/consult.md:29–32` → `:29–31`.** A16-7's capture, Q18 and roundtable A11 all cite the
  neighbour list as `:29–32`. It is **three bullets at `:29`, `:30`, `:31`**; `:32` is blank and `:33`
  is the closing *"A consult is none of these…"* sentence. **Superseded** — the build-3 brief's F7
  adds the fourth bullet after `:31` and re-points `:33`. The ruling's *premise* is confirmed exactly:
  the rule-bearing lines (`:23–27` class definition, `:36` trigger pointer) sit outside the edit, so
  the prose-clarification ruling stands and `consult@1` does not bump.
- **Contract `:226` → `:229`** for the vault rung's pointer-grammar and copy falsifier (roundtable A4,
  Paige: *"(2)'s rung line is pointer-grammar per contract `:226` … the brief greps it against `:226`'s
  copy falsifier"*). Build 2's *Partner memory* edits moved it. **Superseded**; F15 greps the seeded
  line against `:229`.
- **`vlt-consult.js:138` → `:143`** for the lite boot's *"no rule-card or contract read"* clause (D-5,
  Q18, D6's gloss all cite `:138`, which is now the *"You are the vault partner…"* opener), and
  **`:147` → `:152`** for the engine's copy of the `needs-work` → relay routing rule (the obsolescence
  beat's cite). **Superseded**; F5 and F11 cite the fresh lines. `vlt-consult.js:160` (the single
  `agent()` call, as the `S-4` artifact names it) HOLDS.
- **Contract `:318` → `:331`** for the *Wiki + research* hygiene row (A16-6 disposition 4) and
  **`:314` → `:324`** for the `_agent/dispatch.md` decay row (roundtable A11 (i)). **Superseded**;
  F16 and F12 cite the fresh lines.
- **Grounding correction with scope consequences — `vlt-setup/SKILL.md:218`'s offer key.** A16-3
  direction 1 and Q6 assume the seeded `CLAUDE.md` is the carriage question. Grounding shows the
  **existing-file branch** is where reach is decided, and its offer is keyed on *"if it doesn't
  already reference the contract"* — a test **every installed vault already passes**, so the offer
  would never fire and the import lines would reach no live vault. The brief's F2 re-keys the offer on
  the import lines' own absence. No ruling is contradicted (Q6 rules the mechanism, not the key); the
  brief records it as a grounding-driven scope item and Acceptance (1)'s second leg tests it.

---

## Routed away from this cycle — the platform fork

**No filing was marked `channel: platform`, and none is factory-side by re-derivation.** All five name
fix sites under the shipped surface (`skills/vlt-lint/references/`, the governance bundle's conventions
and contract, `skills/vlt-setup/`, `skills/vlt-groom/`, `skills/vlt-setup/assets/hooks/vlt-vitals.py`).
A16-1's convention-side fixture lands in this cycle's `fixtures/` — cycle side. The fork ran and found
nothing; `platform_routed` is empty.

**Addendum, 2026-09-16.** The three addendum filings likewise carry no `channel: platform` marker
and every named fix site is under `skills/` (the contract and `conventions/consult.md` in the
governance bundle; `vlt-dispatch`, `vlt-research`, `vlt-agent-creative`, `vlt-setup`'s rung seed and
workflow assets; `vlt-mint`'s capability template, `vlt-track`, `vlt-upgrade`). Nothing is
factory-side by re-derivation. The fork ran again and found nothing; `platform_routed` stays empty.

## Capture narrative — the judgment calls this run made

- **Coverage.** All five un-captured filings, the skill's default; no filing deferred. The two
  2026-09-03 drafts were filed by `acceptance-discharge` without owner confirmation (*"delete if
  unwanted"*) — the owner did not delete them in six days, and the skill grounds them either way; both
  earned their capture (one with a refuted half, one with a fifty-five-fold sharpening).
- **The un-captured set is five, not more.** Every other file in `factory/inbox/` appears in a prior
  cycle's `derives_from:` — the pre-Cycle-15 holds and the four filings Cycle 15 held on their own
  clauses (`093000`, `183000`, `160000`/#17, `170000`/#18) are captured and waiting on field events,
  not on capture. Cycle 15 closeout carry 10 (*"un-captured inbox backlog"*) resolves, on inspection,
  to filings captured elsewhere and held; nothing there re-enters here.
- **Cycle number and slug.** `factory/CYCLE` read `none`; highest cycle directory 15 ⇒ Cycle 16.
  Slug `closed-loops` from the through-line.
- **Field-vault reads** (`{field-vault}`, read-only): `git show dbd5292` and per-page diffs (A16-2's
  set); a frontmatter scan of `resources/wiki/*.md` for bare `.md` `sources:` scalars (240 / 83
  pages); `{lint_reports}/2026-09-03-1206-lint.yaml` lines 6 and 217–218; the live `{index}` §Stubs
  (A16-1's refutation); a `partner:` census over `{sessions}` (A16-3). No vault file was written.
- **A refutation is recorded, not dropped.** A16-1's second observation was wrong about the index's
  form; the capture says so with the convention's line so a brief does not build a tolerance for it.
- **Study register asked, per filing.** A16-1 → `ST-7` (cited). A16-2 → nearest is Cycle 14's shape;
  narrower than a study; not opened (stated at the entry). A16-3/4/5 → `ST-8`, already citing the
  filings; the captures are appended to `cited_by:`. No new study.
- **Spike register.** `S-4` opened `proposed` from A16-3 (the `@import` question). Highest existing was
  `S-3`.
- **Line-number corrections to the filings** are stated inline (A16-3: `:226` not `:224`; rule-card
  `:16`/`:18` not `:15`; A16-4: `partner_memory_bytes` at `:242` exists). The claims survived every
  correction.
- **Handshake grouping is flagged, not ruled.** Four of five captures change `frontmatter@14`'s rules;
  the capture names it at each entry so ideation bumps once. Ideation's call.

**Addendum run, 2026-09-16 — the judgment calls this run made:**

- **Posture.** `factory/CYCLE` reads `16-closed-loops`; the roadmap is open, no build is ruled, no
  brief exists, no release cut — so this is an **amend**, not a mid-cycle addendum in P-4's sense
  (no roundtable-stamped batch to widen, no scope-delta ruling owed). The previous run's foot
  anticipated exactly this shape: entries continue the sequence (A16-6..A16-8), and the ideation
  skeleton is **re-seeded, not re-laid**. Cycle 17 is not opened.
- **Coverage.** All three un-captured filings, the default. The un-captured set was derived by
  `grep` of each inbox filename against every `factory/cycles/*/roadmap.md`: exactly three files
  appear in none — the two 2026-09-16 factory filings and the filing materialized this run from
  rail issue #19. The other sixty-two are captured elsewhere and held, as the 2026-09-09 narrative
  found. No filing deferred; the owner may still defer one before ideation resumes.
- **The two ST-9 filings were written by the factory and already carry a grounding at `caea0d5`.**
  A filing's own grounding is not the capture's: this run re-derived every site against the working
  tree (`git diff --stat caea0d5 HEAD -- skills/` is empty, so the two readings are of the same
  bytes). Every claim held. One site the filing named by section only is pinned (`:282`), one site
  the filing did not name is added (`vlt-dispatch/SKILL.md:18`), and one recovery path the filing
  proposed is **closed** by running it (A16-6's `## Self` grep found nothing).
- **The `## Self` grep is recorded as a negative, not dropped.** A16-6 rests partly on ST-8 cause B
  (the belief lives in partner memory). The filing's own recovery grep, run read-only over nine
  `identity.md` files, found no lane statement. The claim's *evidenced* author is module source;
  the memory half is inferred. The capture says so and lets ideation weigh disposition 2 (the rung
  pointer) accordingly.
- **The field wearer set for A16-8 was recovered** (five `capabilities/track.md`, read-only) and the
  filing's count corrected: the council record says three apologies; disk holds two. Neither number
  changes the defect.
- **Study register asked, per filing.** A16-6/A16-7 → `ST-9`, opened 2026-09-16 and already
  `cited_by:` both filings; the captures are appended there this run. A16-8 → no study; nearest is
  `ST-7` (a prose-specified derivation with no read-back — the key and its description disagree in
  one line and nothing reads one against the other), but the cause is a lift-time naming error,
  narrower than a study; not opened.
- **Spike register.** No new external unknown: the delegate engine's shape is `vlt-consult.js`,
  module source; the runtime question A16-7 depends on is `S-4`'s, already open. `S-4` is now
  load-bearing for **two** entries (A16-3 direction 1, A16-7's carrier), which the re-seeded spike
  view says.
- **Field-vault reads** (`{field-vault}`, read-only): `grep` over `{partners}/*/capabilities/track.md`
  and `{partners}/*/identity.md`; `_agent/mint/decision-log.md:739`. No vault file was written.
- **Line-number corrections and sharpenings** are stated inline at each entry (A16-6: Creative `:37`
  holds but is a thin-topic cue, not a research prohibition; A16-7: the neighbour list is in the
  versioned convention; A16-8: `vlt-upgrade/SKILL.md:81` is an unnamed site).

## GitHub intake — this run's record

Transport `mggower/bmad-module-vlt` (`feedback_repo.default`, `module.yaml:74`); `gh` present and
authenticated. Query (`--label vault-accepted --state open`) returned six issues — #1, #6, #7, #11,
#17, #18 — **all already `captured`** and all carrying an `origin:` header on disk (#1/#6/#7/#11 in the
inbox under their cycles' captures; #17/#18 held on Cycle 15's build-6 (5)/build-7 (5)). Nothing
materialized; no label drift. Amendment sweep (`captured` + `amended`): none. Stale-shape gate: not
reached (no untriaged body). `issues_materialized` is empty by exercise, not by skip. The same-day
`issue-triage` run found the untriaged queue empty and the only off-rail traffic the owner's pinned
#9.

**Addendum run, 2026-09-16.** Same transport, `gh` present and authenticated. Query returned seven
issues: #1, #6, #7, #11, #17, #18 — all `captured`, all with an `origin:` hit on disk, no label
drift — and **#19** (*Rename the loop-profile slot non-negotiable-gate to write-gate*, opened
2026-09-09 18:48:40Z, `vault-accepted`, not `captured`). Stale-shape gate: `rail_contract: 1`
matches `field-contract.md:12`; all eight required fields present; `kind: defect`. Idempotence: no
`origin:` line carrying `mggower/bmad-module-vlt#19` in `factory/inbox/` or any `filings/`.
**Materialized** as
`factory/inbox/2026-09-09-184840-rename-the-loop-profile-slot-non-negotiable-gate-to-write-gate.md`
(timestamp from `createdAt`, slug from the title, bare `origin:` header); `captured` label applied;
issue stays open. It joined this run's un-captured set and is captured as **A16-8**. Amendment leg
(`captured` + `amended`, open): none. `issues_materialized: ["mggower/bmad-module-vlt#19"]`.

## Carried forward INTO this cycle from Cycle 15

Re-listed from `factory/cycles/15-nothing-reads-it-back/roadmap.md` §Closeout record (the
authoritative hand-off); disposition here is *where each now sits*, not a ruling:

1. **Four released standing watches** (build-1 (5) next live `supersession` filing; build-2 (6) first
   warm *release*; build-6 (5) scoped lint with a planted control; build-7 (5) partner
   self-attestation) — **field-contingent, unchanged.** build-2 (6) has its first chance at the release
   this cycle cuts.
2. **Four filings held on their clauses** (`093000`, `183000`, `160000`/#17, `170000`/#18) — held,
   unchanged; not re-captured (narrative above).
3. Cycle 14 park filings — **nothing left** (moved and closed 2026-09-03).
4. **`para_author_unknown`'s closed enum** — the next `supersession` candidate, owner to file via the
   rail; unfiled as of this run.
5. **Cycle 12's never-delivered hand-off** (b3(7), A12-4, A12-5, A11-11 d4 + A12-1) — **fourth cycle,
   unchanged**; the `:168` dissent — unchanged, ruling-in-waiting for `unmarked_supersession`.
6. **`{field-vault}` overlay staleness** — vault-side, unchanged.
7. **Candidate filings owed at handoff** (build-3's optional args; build-4's `pageHashes` digest form,
   field-confirmed; build-5's `para_type_unknown` count leg; build-7's five-value enum + partner-side
   attestation beat; A15-12's subtree-`type:` mechanism) — **still unwritten**, six days on.
8. The two 2026-09-03 drafts — **CAPTURED here as A16-1 and A16-2.**
9. **Seven operator findings, uncaptured** — unchanged; one of them (the `sources_vs_prose_mismatches`
   tier question) is named adjacent to A16-2.
10. Un-captured inbox backlog — **resolved on inspection** (narrative above): nothing un-captured
    remains in the inbox after this run.
11. **`S-3`** harvested, unconsumed — **fifth cycle**; `S-4` now joins it `proposed`. **[P-23]/[P-24]**
    queued, unchanged.

## Open design questions carried into ideation

Collected from the entries above, verbatim there; listed here so the scaffold can slot them:

- **A16-1:** convention-side vs procedure-side heading fix (both one line; the fixture follows whichever).
- **A16-2:** the checker's posture on bare-path entries — census line vs reduce-side refusal vs status
  quo; whether the vault's 55 get an owner-ruled one-time exception to no-backfill.
- **A16-3:** `S-4`'s answer decides the carriage mechanism; `purpose:` field or free text; dispatch
  slice for a `partner: none` sitting.
- **A16-4:** the budget value (owner ruling; ~12K words proposed); casebook as file or section; where
  owner-model material migrates; `activation_words` vs `partner_memory_bytes`.
- **A16-5:** charter minted or blank; `cold` as modifier or field; the Researcher pilot's breadth
  measure and its null-result reading.
- **Cross-cutting:** one `frontmatter@14` bump for A16-3/4/5 (and A16-2 (2) if it adds a report slot,
  which is `report.md`, not the convention); build grouping across the lint pair and the partner triple.

*Added 2026-09-16 by the capture addendum:*

- **A16-6:** how the rung pointer reaches a vault whose `_agent/reflexes.md` is already populated
  (seed-if-absent never touches it); whether the web extension of read-and-cite carries its blind
  spot as a sentence in the rule (Quinn's dissent, kept); whether the Creative's `:37` cue keeps
  "surface to the user" and only changes the named remedy.
- **A16-7:** whether adding `delegate` to `conventions/consult.md`'s neighbour list is a prose
  clarification (no `consult@1` bump) or touches the class definition; `deep` → `too-big` → relay as
  the only deep route; `op` single-tenant in v1; where the 2×2 lands (`:288` is the sentence it
  extends); the orphaned `.WIP.md` watch.
- **A16-8:** deprecated alias for one release or indefinitely (no reader parses the key); whether
  `vlt-track:15`'s framing changes with the key; whether `vlt-upgrade` offers the wearer-side
  rename as a human-gated migration (`:79–84`) or the CHANGELOG notice is enough.
- **Cross-cutting (new):** the delegate runner is an instance of A16-3's partnerless carrier — one
  carrier, sequenced; `S-4` now underlies two entries. A16-4's Beat 1 weight is `ST-9`'s amplifying
  cause — the budget build and the delegate build pull the same lever from two sides.

## Ideation rulings — A16-1..A16-8 (owner-steered, 2026-09-16)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**HELD by the owner 2026-09-16, before round 1 was ruled — no slot is filled.** The owner may add
filings to this cycle, so the batch is **not closed**: the material below was seeded from the
2026-09-09 capture of A16-1..A16-5 and from the spike register, and a later capture addendum
**extends this section's batch label and re-seeds it** rather than laying a second skeleton (one
skeleton per batch — `ideation-scaffold`'s own rule). Round 1 (cycle scope, the build cut, build 1)
was put to the owner in-session and **deliberately not answered**; nothing was recorded, and the
questions below stand exactly as laid.

`build-brief` gates on this section being filled — it is not yet, and it should not be until the
cycle's contents are settled.

**Re-seeded 2026-09-16 by the capture addendum (A16-6..A16-8).** The batch label above is extended
per the previous foot's instruction; no second skeleton is laid. Additions are marked *(added
2026-09-16)* and numbered past the existing Q14 / D5 / E6. Nothing previously seeded is removed or
reworded; D1 and D2 are re-checked below and **do not move** (neither addendum filing touches
`frontmatter@14` — A16-7 states that explicitly and grounding confirms a research note carries no
`partner:` field — and none adds a `demote` consumer). D3 gains a third member (D6).

Question numbering is the clerk's, for reference in session only; it implies no ordering or
priority. Where the capture proposed something, it is carried as **capture's proposal,
unaccepted** — never as a ruling.

### Grouping & order

**Cycle scope — RULED 2026-09-16: all eight.** A16-1..A16-8 are in Cycle 16; nothing leaves.
(The capture's grouping question and the addendum's widening, below, are retained as the record of
what was put to the owner.)

**The grouping question the capture flagged, unresolved:** *"build grouping across the lint pair
and the partner triple"* — A16-1/A16-2 share a skill (`vlt-lint`) and share nothing else;
A16-3/A16-4/A16-5 share a cause (`ST-8`), a file (`frontmatter.md`), and a handshake bump. Whether
that is two builds, five, or some other cut is the owner's call.

*(added 2026-09-16)* **The addendum widens the cut to eight.** A16-6/A16-7 share a cause (`ST-9`) and
a seam (a non-Researcher partner needing a dive mid-sitting); A16-7 **depends on A16-3** for its
runner's governance carriage (one carrier, never two — the filing's own constraint) and so on `S-4`
or its fallback; A16-6 is prose plus a rung line and could ship alone or ride A16-7. A16-8 is a
one-line rename with an alias and shares nothing with any other entry — a candidate for whichever
build ships first, or its own small build.

**Build cut — RULED 2026-09-16 (round 1): three builds, A16-3 split across builds 2 and 3 so the
spike touches exactly one build.** Put to the owner as the clerk's read after the owner asked for it;
approved as laid. The reasoning on record: the capture's two-build shape puts `S-4` under the
`frontmatter` bump, so an unrun spike would block the schema brief too; a schema-first cut ships a
bump with no behaviour behind it for a whole build; splitting A16-3 costs one line in two briefs and
buys two builds that are briefable immediately. The cold summon (A16-5 (3)) sits in build 2 without a
carrier ruling because it is a partner activation and the ritual already loads the card
(`vault-operating-contract.md:194`). A16-6 rides build 3, not build 1, because its Creative cue
(A16-6 (3)) names delegate.

- **build-1 — the at-rest fixes: A16-1, A16-2 (directions 1 and 2; direction 3 is the vault's), A16-8.**
  All prose and fixtures inside `vlt-lint`, `vlt-mint`, `vlt-track`, `vlt-upgrade`; no handshake bump;
  no dependency on any other build. ~~A16-8's CHANGELOG notice reaches wearers first.~~ *(struck —
  roundtable A17, 2026-09-16: under A10 build 1 is its own release, so the notice ships with it, and
  build 1's brief carries its CHANGELOG notice text verbatim in a §8 stub headed "notice text —
  collated at release". The A16-8 notice says* delete the apology parenthetical, *not only* rename
  the key, *and* old key accepted indefinitely *so nobody hunts for a sunset.)*
  *(roundtable A9/A10 constraint, 2026-09-16: build 1 ships alone so that Cycle 15's build-2 (6)
  "first warm release" watch has its chance — therefore build 1's brief must achieve Q3 (a)'s
  per-page drop **without touching `PAGE_SCAN`, the scanner enum, or the scanner conventions** (the
  census is script-side in `lint-page-facts.py` either way; the drop is a reduce-side exclusion keyed
  on script-derived page facts, never on complaint wording) — or the brief states that the watch's
  chance is false on this release too, and the ledger says so. Amelia's finding; brief's call.)*
  - `binds:` Q1, Q2, Q3, Q4, Q5, Q20, Q21, D5, E1, E2, E3 *(confirmed 2026-09-16 with the round-3 rulings)*
  - `spike:` none *(ruled with the cut)*
  - `promise:` After this ships, a vault owner running `vlt-lint` or `vlt-track` sees the module read its own writes back, instead of a lint that mislocates the heading it was sent for, a sweep that writes a form its own checker rejects, and a slot whose key contradicts its description. *(owner-ruled 2026-09-16, chosen from three clerk drafts at ruling time)*

- **build-2 — the partner-memory schema: A16-4 whole, A16-5 whole, A16-3 direction 2 only (the
  `partner: none` sitting named in the contract).** The one `frontmatter@14` → `@15` bump, all ten
  consumers re-acked in this build. Internal order forced: demote verb → charter → cold summon.
  - `binds:` Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, D1, D2, D3, D4, D7, D8, E4, E5 *(confirmed 2026-09-16 with the round-4 rulings)*, **D9** *(roundtable A4 — build 2 defines the class)*
  - `spike:` none *(ruled with the cut — the cold summon reads the card through the ritual)*
  - `promise:` After this ships, a vault owner sees the partner loop opened from outside: a budget a wire trips on, a charter slot the owner fills, a demote verb, a cold summon, and a named partnerless sitting, instead of a partner memory whose only reader is its writer. *(owner-ruled 2026-09-16, chosen from three clerk drafts at ruling time; enumerates five deliverables)* *(re-stamped 2026-09-16, roundtable A1/A3: "a budget the lint enforces" → "a budget a wire trips on" — nothing in build 2 gates a write, and "enforces" would promise an enforcement point one cycle after the no-enforcement-point cycle; "a charter the owner holds" → "a charter slot the owner fills" — minted for new partners, seeded with the mint prompts as placeholders for the nine existing ones, whom the owner fills by hand. "A named partnerless sitting" stays: per A6 the paragraph names what the sitting OWES and is mechanism-free about what it reads.)*

- **build-3 — the carrier and what rides it: A16-3 direction 1 (governance on a surface every session
  reads), A16-7 delegate, A16-6.** One carrier, two tenants (D6). Sequenced after build 2 (A16-7's
  runner is partnerless; A16-6 (3)'s cue names delegate).
  - `binds:` Q6, Q15, Q16, Q17, Q18, Q19, D3, D6, D7, D8, E7, E8 *(confirmed 2026-09-16 with the round-5 rulings)*, **D9** *(roundtable A4 — build 3 consumes the class for the rung line)*
  - `spike:` S-4 *(as laid; an owner ruling that the `SessionStart` hook is the carriage retires `S-4` unrun and turns this to `none` — written back to the register file in the same session)* *(roundtable A5: the harvest records the workflow-`agent()` subagent kind on its own row — the delegate runner and the consult lite boot are that kind; the register's Consumers line is corrected this session to drop the cold summon, which D6 rules is not a tenant)*
  - `promise:` After this ships, a vault owner sees every session, partnered or not, open on the same rules, and a partner running `vlt-dispatch` can delegate a bounded research dive and get the result back in the same sitting, instead of rules that ride only the summoning ritual and a one-fact dive deferred to another session because the partner inferred a lane the contract never stated. *(owner-ruled 2026-09-16, a blend of two clerk drafts approved at ruling time; carriage mechanism deliberately absent so the sentence survives `S-4` either way)* *(roundtable A5, 2026-09-16: if the harvest narrows the reach, the narrowing is written into THIS line — "every session" becomes the kinds reached — not only into the brief; briefs cite this line. Only the every-session clause can narrow; the delegate half cannot, because the runner's carriage is whatever the harvest shows for its kind and an engine-prompt pointer is the carriage of last resort for that kind.)*

*(An unfilled `spike:` or `promise:` is **not** `none` — it blocks `build-brief`, which is the field
working. `binds:` is reconstructible and is disclosed rather than blocking; a promise is not
reconstructible, which is why it blocks.)*

**Release shape — RULED 2026-09-16 (round 2): one release carrying all three builds, conditional on
`S-4` being RUN before build 3 is briefed** (ruled in the same round, below). Put to the owner as: one
release, two releases split after build 2, or one release conditional on ruling `S-4` around; the owner
took the conditional form and then ruled `S-4` *run*, not ruled-around — so the condition is a harvested
spike, not a hook assumption. Builds 1 and 2 are briefed on the rulings alone; build 3's brief waits on
the harvest. ~~(Cycle 15's build-2 (6) watch — *first warm release* — gets exactly one chance this cycle.)~~

**AMENDED 2026-09-16 (roundtable A10, owner-ruled live): TWO releases, and the S-4 condition gains its
failure branch.** Two findings forced it. Amelia: Cycle 15's build-2 (6) watch fires only on a release
whose diff touches none of `frontmatter`/`wiki-supersession`/`write-verification`, the scan prompt, or
the scan model (C15 roadmap, the (6) clause) — and D1's `@14→@15` re-ack edits the literal
`frontmatter@14` inside the scanner prompt (`vlt-lint-full.js:297/:299`), moving `scanFingerprint`,
while the merged convention digest moves too; both cache-key halves move, so the parenthetical above
was false as written. Seven voices: the single release's condition had no branch for "S-4 not
harvested", and the recorded alternative (split after build 2) would ship the `partner: none`
paragraph with no carriage and no stated interim. Ruled:
- **Build 1 ships alone, first**, as a patch release (clerk's read: v0.18.1) — it touches none of the
  six cache inputs *provided its brief honours the A9/A10 constraint in the build-1 bullet*, so the
  warm-release watch gets its one chance there. Build 1 gains nothing from waiting on `S-4`.
- **Builds 2 + 3 ship as one release** (clerk's read: v0.19.0), **held whole until `S-4` is harvested
  — no split branch exists.** If the harvest drags, the release waits; the `partner: none` paragraph
  never reaches a vault without its carriage.
- *(roundtable A17)* Builds 1 and 2 each carry their CHANGELOG notice text verbatim in their own brief
  (a §8 stub headed "notice text — collated at release"); the release build's §8 **collates, never
  authors**, earlier builds' notices. The v0.19.0 field-notice block states R1 (below, D9) once, above
  the two builds, so the three postures toward vault-owned files read as one hand.
- *(roundtable A6, Maya)* Build 2's acceptance for the `partner: none` sitting is at-rest prose (grep)
  only; the *first partnerless note written* check is entered on **build 3's** ledger, because build 2
  ships no actor that reads the rule.

### Pre-ideation rulings the capture demanded

Seeded as questions, unanswered. Each cites the capture entry that raised it.

**Q1 — A16-1: which side of the seam gets the heading fix?** The capture's two directions are
mutually exclusive in practice and both are one line:
(a) **convention-side** — `wiki-index.md` states the heading text *outside* the fence at `:80`
(prose clarification: no rule change, **no `version:` bump, no consumer re-ack**); or
(b) **procedure-side** — `checks.md:13` says the heading is stated inside the convention's fenced
example and the reader takes the first `## ` line inside that fence.
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): (a), convention-side.** `wiki-index.md:80` states the heading outside the fence; no bump. The convention was the ambiguous thing; a fence-aware procedure would be a workaround for a document that should just say the heading.

**Q2 — A16-1: does the convention-side fixture ship, and where?** The capture's direction 3 —
`wiki-index.md` §Stubs bytes in, the heading string out — lands in this cycle's `fixtures/`
whichever of Q1 (a)/(b) is ruled. Ship it, or defer it?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): SHIP.** The fixture lands in `factory/cycles/16-closed-loops/fixtures/`; it is the only check on the side that broke.

**Q3 — A16-2: the checker's posture on bare-path `sources:` entries.** The capture sharpened this
to three options and explicitly left it to ideation:
(a) **drop the class from `malformed_frontmatter`** (unobservable at rest ⇒ not a per-page
finding) and surface it as a **denominated census line** (`bare_path_sources: N entries / M pages`,
the `attestation_census` idiom at `checks.md:18`);
(b) **keep the scanner verdict** and have the **reduce refuse it by name**, as it refuses the
attestation-only complaint;
(c) **status quo.**
*Capture's proposal, unaccepted: "a count the owner can watch fall beats a flag the owner cannot
act on."*
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): (a).** The class leaves `malformed_frontmatter` and surfaces as a denominated census line (`bare_path_sources: N entries / M pages`). Legality is indexed on write date, which bytes cannot carry, so a per-page flag can only be arbitrary.
*(roundtable A9, 2026-09-16 — the line's shape and gate, Caravaggio/Amelia/Mary/Sophia, no dissent):* the line is **full-mode only** (`# full mode only` per `report.md`'s grammar, or the literal `not instrumented (scoped run)` as `scanner_return_rejected` renders — scoped mode's denominator changes every run); its shape is three-term, **`N entries across P of M pages`**; it is **computed script-side by `lint-page-facts.py`** (which already parses the frontmatter block and rule 4's form, `:43`), never from scanner returns; and **`lint-report-check.py` compares it by string equality** as it does `para_scan:` — an inline map's children are not validated (`report.md:9` rule 2), so without this the census is a self-reported number. The drop from `malformed_frontmatter` has no reduce-side enforcement point as ruled (a bare-path complaint arrives `unclassified`, which the reduce never refuses, `vlt-lint-full.js:1067`); the brief must site one — **under the A9/A10 constraint** (build-1 bullet): keyed on script-derived page facts, never a new scanner verdict kind, so `PAGE_SCAN` stays byte-identical for the warm-release watch.
*(grounding correction — `build-brief` build 1, 2026-09-16):* A9's premise that `lint-page-facts.py` *"already parses the frontmatter block and rule 4's form, `:43`"* is **superseded**: `:42-44` is a docstring remark that a quoted `"[[path]]"` `sources:` entry counts as a link; the script delimits the frontmatter block and parses only `summary:` — no `sources:` entry is read and no form is classified. The ruling (script-side, never from scanner returns) stands; **build 1 adds the parser** (`bare_sources()`, a `--census` walk, and the per-page `bareSources` map — brief F4). The line's shape and gate are unchanged.

**Q4 — A16-2: does the writer-side repair ship this cycle?** Direction 1 — `fix-and-file.md:12`
loses its frontmatter-write residue (or states rule 4's form for it if a frontmatter write is ever
legal on that path), made `checks.md:16`-consistent. One paragraph, exact F-site. In or out?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): SHIP.** `fix-and-file.md:12` loses its frontmatter-write residue, `checks.md:16`-consistent. It is the enforcement point.

**Q5 — A16-2: the vault's 55 entries.** The capture calls this **not module scope** and records it
so the field debt has a name — a hand pass, or an owner-ruled one-time exception to rule 4's
no-backfill clause, both vault-side. Does the owner rule the exception now, or leave it?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): LEAVE.** Vault-side, after this ships; ~~the Q3 census line shows it done~~ **the Q3 census line shows it stopped growing** *(roundtable A9, Sophia/Mary: ~185 of the 240 entries stay legal forever under rule 4's no-backfill clause, so the line falls toward a floor nobody had named and an owner watching it plateau would read a stalled fix — the line's job is* never rises, *not* falls to zero*; the floor is recorded at E2)*. No module ruling, no exception ruled.

**Q6 — A16-3: the carriage mechanism for partnerless governance.** Direction 1 is **ungrounded
pending `S-4`** — whether `@path` imports in a vault `CLAUDE.md` load for every session kind. The
grounded fallback is the existing `SessionStart` hook (`vlt-setup/SKILL.md:187`,
`vlt-vitals.py --strip`), which already fires per session. Ruling needed on: does a build bind
`S-4`, and does the fallback ship if `S-4` returns *no*?
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): MECHANISM FOLLOWS THE `S-4` HARVEST; the fallback ships on a *no*.** Build 3 binds `S-4`. Imports carry the card and rung for every session kind the harvest shows they reach; the `SessionStart` hook carries them for any kind imports miss; if both miss a kind, build 3's promise narrows from *every session* to the kinds reached, stated in the brief.
*(roundtable A5, 2026-09-16, no dissent):* **(i)** the hook fallback is a **second `SessionStart` entry keyed on its own command path** (per `vlt-setup/SKILL.md` §2b's merge rule), never a flag on `vlt-vitals.py --strip` — the strip's contract is at most one line, nothing when green, and §2b's idempotency key is the script path so a second flag is invisible to the merge (Winston). **(ii)** The narrowing is written into build 3's `promise:` line as well as the brief (John). **(iii)** Only the *every session* clause can narrow; the delegate runner's carriage is decided by the harvest for its own kind (D6 gloss) and cannot narrow the promise's delegate half (Sophia).

**Q7 — A16-3: the `partner: none` sitting.** Direction 2 does **not** depend on `S-4`. Naming it in
the contract's *Sessions, sittings, and hand-offs* turns `frontmatter.md:167`'s *"Omit only for a
partner-less generic-agent session"* into an explicit value — **a rule change to `frontmatter@14`**
(see D1). In or out, and with what clauses (one session note, log tag `(session)`, no
partner-memory writes, wiki single-writer)?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): IN**, with the four clauses as filed (one session note, ~~`(session)` log tag~~ **`(none)` log tag** *(roundtable A8)*, no partner-memory writes, wiki single-writer holds) **plus one**: the sitting does not read `_agent/dispatch.md`'s open slice — it has no addressee. `purpose:` is free text in the note, not a field.
*(roundtable A8, 2026-09-16 — owner-ruled live, dispute D-7):* **one string on every surface** — `partner: none` on the note ↔ **`(none)`** in the `{log}` paren ↔ `none` in a dispatch pointer's slug slot (build 3's runner has no slug otherwise). As ruled before, the sitting's log line would have read `session (session)` (the type slot and the paren slot spelling one word — `session` is a `<type>` at contract `:154`), ops inside it would stay paren-less, and Q13's own reasoning — a `partner:` modifier overloads the field every reader parses — applies to the paren, which is that field's log twin (`frontmatter.md:167`). The three omit clauses — contract `:159` (the `{log}` section, which D8 assigned to nobody), `frontmatter.md:167`, `vlt-ingest/SKILL.md:24` — **narrow to headless ops outside any sitting** and are edited in build 2; A16-3 (3) "ops unchanged" narrows to *op mechanics unchanged; the tag follows the sitting*. **Mary's rider, no dissent:** the field's two pre-adoption values (`partner: user` ×1, `partner: vlt-mint` ×1 in `{sessions}`) are declared **legal-until-groomed** in the `@15` bump, or the schema's one specimen of the very thing it names becomes malformed the day the value is born.

**Q8 — A16-4: the Beat 1 budget value.** An owner ruling by construction. *Capture's proposal,
unaccepted: the light partners' median ×2 (~12K words), to be tightened once the instrument
exists.*
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): 12,000 words**, on the per-partner Beat 1 set only (SKILL.md + `identity.md` + `reflexes.md`; the card and rung are fleet-constant and excluded). Three partners trip it at ship — the instrument doing its job. The wire's recalibration clause: tighten once the metric has run a few sweeps.
*(roundtable A1, 2026-09-16 — all thirteen voices; owner-ruled live on two disputes):* **(i) The number lives once.** A16-4 (1)'s "the contract declares a word bound" would give 12,000 two homes with different owners, and the registry's seed-merge is *local thresholds win* (`tripwires.yaml`), so only the vault copy is live and the recalibration clause could never reach an existing vault through the module. **The bound's single home is the seed wire's `threshold:`; the contract states that a bound exists and points at the wire** — the posture the reflex cap already takes (`frontmatter.md:224`). **(ii) The legal response has a named home.** `tripwires.yaml`: *a wire's legal response homes in `surface_text`*. The wire's `surface_text` names the response **and its order**: *author the charter, then `groom <partner>` (D4's identity-to-card migration — the only act that moves the librarian from 22,144 to under 12,000; item-wise demotion cannot)*; the recalibration clause runs on sweeps after that order has been walked once (Maya). **(iii) Dispute D-1, owner-ruled: the wired set stays SKILL.md + `identity.md` + `reflexes.md`**; the `surface_text` names the fork — *identity-heavy → groom; SKILL-heavy → rebirth via `vlt-mint`* — and the per-partner detail shows the split. Dissent on record (Builder): narrow the wired set to the two groom-reachable files; minted partners spend 3.3–3.9K of the 12K on template scaffold. **(iv) The read set is posture-aware** (Carson, Victor): the metric derives over the Beat 1 set the partner's declared `memory:` posture actually reads (`full` → all three; `reflexes` → SKILL + reflexes), and the report names the posture beside the number. Three trips at ship are **the expected state, stated in the acceptance, not a defect** (Amelia).

Beat 1 words per partner, re-measured read-only in `{field-vault}` 2026-09-16 (SKILL.md + `identity.md` + `reflexes.md`; `thread.md` shown for scale, not counted):

| partner | SKILL | identity | reflexes | **Beat 1** | thread |
|---|---|---|---|---|---|
| librarian | 1,744 | 19,840 | 560 | **22,144** | 10,914 |
| football-analyst | 3,840 | 14,873 | 681 | **19,394** | 21,898 |
| creative | 2,037 | 12,192 | 1,792 | **16,021** | 17,411 |
| researcher | 1,812 | 6,421 | 1,060 | **9,293** | 10,033 |
| career-strategist | 3,872 | 2,651 | 475 | **6,998** | 5,114 |
| chef | 2,998 | 3,472 | 67 | **6,537** | 3,770 |
| chess-coach | 3,328 | 2,633 | 67 | **6,028** | 2,579 |
| health-coach | 2,585 | 1,610 | 67 | **4,262** | 917 |
| dog-trainer | 2,204 | 909 | 67 | **3,180** | 486 |

Fleet-constant on top of every partner: vault rung 171 words + rule-card 1,076 words = 1,247. The
heaviest partner has changed since the filing (librarian now above football-analyst). Light-six median
6,283 → ×2 ≈ 12.5K, consistent with the capture's ~12K.

**Q9 — A16-4: `activation_words` vs `partner_memory_bytes`.** `vlt-vitals.py:242` already carries
`partner_memory_bytes` (fleet-wide, bytes, includes `thread.md` + capabilities, display-only,
never wired). The ask is per-partner, Beat 1-subset, bounded. Does the new metric **replace,
refine, or sit beside** it?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): SITS BESIDE.** `partner_memory_bytes` is a fleet total including `thread.md` + capabilities — a different question. Replacing deletes a working display; refining changes its meaning under whatever reads it.
*(roundtable A1, 2026-09-16 — the scalar the wire binds, which this ruling never named):* a per-partner metric cannot be a tripwire's metric — `evaluate_wire` compares one scalar to one integer (`vlt-vitals.py:479-486`), a wire carries one `owner:`, the strip prints one line, and the ledger's Tripped-wires row shows a value and an owner slug, never a partner (B10-4 (4)'s shape, A10-19). Ruled: **the wire binds a denominated count, `partners_over_activation_budget: N of M partners`** (the `expired_pages` idiom), whose tripped detail names each partner slug; **the per-partner Beat 1 words render as a second column on the existing per-partner display block beside bytes** (`vlt-vitals.py:806-809`, the `partner_rows` idiom: `- <partner>: <bytes> bytes · <words> words [over budget]`), so strip, ledger row and vitals block all name the partner. Winston conceded the fleet-max alternative: a max hides the second and third partner on the surface that matters. **Dispute D-2, owner-ruled: `owner: human`** — the owner runs the summon-and-groom; partners are named in the detail; the registry schema's single static owner is filed as a defect (inbox). *(roundtable A18, Paige)* **`casebook.md` is IN `partner_memory_bytes`**, stated in the METRICS description — it is partner memory on disk and the metric is a disk-mass vital.

**Q10 — A16-4: the casebook's shape.** A fourth partner-memory file, or a section of `thread.md`
below `## Set aside`? And where does `## Bond`'s owner-model material migrate — the wiki
(single-writer, Librarian hand-off) or a PARA area the partner may write?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): a fourth file, `casebook.md`, never wake-read** (a `thread.md` section keeps it in a file Beat 2 opens, defeating the rung). Owner-model material migrates to the **wiki via Librarian hand-off**, not a PARA area — single-writer is the rule everywhere else and this is the wrong cycle to open a partner-writable exception.

**Q11 — A16-4: does the reflex `cap_words:` rider ship?** Its own falsifier fired
(`frontmatter.md:224–226`; `review_after: 2026-11-17` is the n=1 recalibration expiry the falsifier
was written for). Ride with the budget build, or stand alone, or defer?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): RIDES BUILD 2.** Its falsifier fired; it is one field in the same schema edit; deferring means a second bump for one line.

**Q12 — A16-5: is `## Charter` minted or blank at birth?** From `vlt-mint`'s partner-ideation beat,
or empty and owner-authored? And the adoption posture for the nine existing partners —
`vlt-setup`/`vlt-upgrade` may **seed an empty section, never author one** (durability posture; the
B1 local-mint preserve path is in play).
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): MINTED** from `vlt-mint`'s partner-ideation beat, then owner-editable. Adoption for existing partners: `vlt-setup`/`vlt-upgrade` **seed an empty section, never author one** (durability posture; B1 local-mint preserve path re-checked at brief).
*(roundtable A3, 2026-09-16 — John/Maya/Carson/Sally/Builder, no dissent on the first three; two owner rulings):* **(i) The empty charter has a stated posture.** Nine existing partners hold an empty `## Charter` on upgrade day — the day the three heaviest trip the wire, whose response is a groom against the charter. An empty `## Charter` **disables the charter check** — no finding, never "all off-charter" — and the groom diff header says *charter empty — nothing to check against*, never silence; demote still proposes on the **casebook shape criterion** (dated first-person case narratives → `casebook.md`) with no charter. **(ii) The seeded section carries the mint template's prompts as placeholder text** (*what do you want this partner for; what should it refuse; what should it never remember*) — the seed-placeholder idiom `identity.md` already uses at cold start (contract `:202`); setup/upgrade still author nothing. The seed is a **D9** act (below). **(iii) The first-meeting detector narrows** (Victor): contract `:202`'s test reads `## Bond`/`## Self` only; `## Charter` content never counts as a filled identity, or no minted partner ever has a first meeting. **(iv) Dispute D-4, owner-ruled: the lint half of A16-5 (1) — "`vlt-lint` flags partner edits to `## Charter`" — is DROPPED.** A section's author is not in its bytes (Q3 (a)'s own reasoning), `identity.md` carries no `author:` (`frontmatter.md:234`), `vlt-lint` has zero partner-memory checks, and `frontmatter.md:290` says enforcement ships with the widening or is withdrawn. The guard is the **render surface**: `## Charter` is **keep-only in every groom diff and every partner end-of-sitting write**, `enforcement_stage: declared` with the deferral triple — the reflex cap's posture (Builder, Carson, Sally). **(v) Dispute D-11, owner-ruled: the mint-time `## Self` seed is RETIRED** (`vlt-mint/SKILL.md:132` "seed `## Self` with the distinctive starting register"; `partner-agent-template.md:111`) — two seeds from one becoming conversation, the second written in the voice the charter check will later grade; **`## Self` is born empty, like `reflexes.md`** (Builder). Obsolescence beat.

**Q13 — A16-5: is `cold` a `partner:` modifier or its own `sitting:` field?** The session-note
shape follows the answer.
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): its own `sitting: cold` field** on the session note. A `partner:` modifier overloads the field every log reader parses.
*(roundtable A2, 2026-09-16 — the cold summon's read set, trigger, log form, and the groom it may host):* **(i) Dispute D-3, owner-ruled: a `sitting: cold` MAY host an owner-invoked, approval-gated `vlt-groom` pass.** Cold's write ban is on *drift*, not on hygiene by reference; the writer identity stays the partner. This is the intended response to a budget trip: without it, curing the librarian's 22,144-word Beat 1 means summoning the librarian warm at 22,144 words — three partners, three full-weight sittings before the instrument's first response (John, Victor, Sally, Builder; ST-8 cause B executing the remedy for cause A). The honest alternative — keep cold groom-free, a partner should read what it is asked to demote — was recorded, not argued. **(ii) Cold reads SKILL.md + `## Charter` + `reflexes.md` + card + rung; it sheds `## Self`/`## Bond`/`## Thread` only** (Builder): A16-5 (3) as filed dropped `reflexes.md`, the rules that "must fire unasked" (`:224`) — ST-8 cause C reproduced inside the fix. **(iii) The trigger is the summon utterance** (Maya): the contract's fourth posture states the partner honours it *before* Beat 1's identity read and skips Beat 2; the sitting-end identity/thread update (`:269`) is suspended for it. Wording at brief time (D8 — build 2 owns the section). **(iv) `cold` goes in the `{log}` summary after `|`, never inside the paren** (Sally): `LOG_HEADER_RE` (`vlt-vitals.py:49-51`) captures everything inside the parens as the partner; `(librarian, cold)` breaks every per-partner log read. `sitting: cold` on the note is the greppable record.

**Q14 — A16-5: the Researcher pilot for `memory: full | reflexes | none`.** Pilot on the Researcher
only, or fleet? Its breadth measure (*capture's proposal, unaccepted: distinct source domains per
dive over five dives before and after*), and the filing's own note that **a null result is a
finding** relocating the cause to `vlt-research`'s search discipline.
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): RESEARCHER ONLY**; breadth measure as proposed (distinct source domains per dive, five dives before and after); **field-contingent, watch not gate**; a null result relocates the cause to `vlt-research`'s search discipline, as filed.
*(roundtable A14, 2026-09-16):* **(i) Dispute D-9, owner-ruled: the enum narrows to `memory: full | reflexes` this cycle.** `none` is unexercised by the pilot; a `memory: none` partner never writes `## Bond`/`## Self`, so contract `:202`'s first-meeting detector would fire on every activation, and its every sitting would be cold without the tag — the population D3 was meant to cut, cut for the wrong pair (Builder, Carson; elimination, not precedence). Dissent on record (Victor): keep `none` and narrow the detector's population to `full`. Per-summon statelessness is `sitting: cold`; a later cycle may add `none` on evidence. **(ii) The pilot gets a baseline and an arm** (Mary, Maya) — the "before" is measurable only *before* the field Researcher is flipped, i.e. before the upgrade lands, and no build owned it: **build 2's brief derives the baseline** (the last five Researcher dives identified by the `{log}` `research (researcher)` line; distinct source domains from each note's `sources:`, vault-internal entries excluded) **and records the five numbers in the ledger row**, naming the derivation as the instrument; the arm value is named (`reflexes` is the clerk's read); the flip date is the `identity.md` commit; compare **depth-matched** dives only (domain count is depth-confounded, `vlt-research/SKILL.md:44-46`); **delegate runs (build 3, same release) are excluded** or the pilot is confounded by its own cycle; discharging vault `{field-vault}`. Field today: 46 `research (researcher)` lines, 8 in the last ten days — five-after is weeks. Still watch-not-gate, but a watch a human can run.

*(added 2026-09-16)* **Q15 — A16-6: which of the five dispositions ship?** (1) the *Capabilities*
sentence; (2) the rung pointer line; (3) the Creative `:37` remedy wording; (4) the hygiene-row
clause at `:318`; (5) read-and-cite extended to the web at `:282` with its blind spot stated. The
capture flags (2) as reaching **new vaults only** by seed and (5) as carrying an honor-system tier
the roundtable dissented on and kept.
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): ALL FIVE.** (1)–(4) are one sentence each; (5) ships with its blind spot stated in the rule and Quinn's dissent recorded as a **watch**. Dropping (5) leaves the one-fact case no route but delegate, heavier than the case needs.
*(roundtable A15, 2026-09-16, Quinn — no dissent):* **(5) names the wrong field for the class it most serves.** The caller Creative `:37` names is shaping a **PARA deliverable**, where `sources:` is *wiki-only method provenance* and non-wiki evidence goes in `grounding:` (`frontmatter.md:94`; `extraction.md`'s segregation rule and `method_in_grounding` firewall) — a Creative obeying (5) as ruled trips an existing lint. Amended: *cited inline with a `sources:` entry on wiki-class artifacts and a `grounding:` entry on PARA artifacts; the blind-spot sentence names **`web_cited_entries: N entries / M pages`** as its only read-back — one line in `report.md` under the Q3 (a) census idiom* (URL-form entries are countable on disk; the honor-system tier gets the visible half it was not being given). Build 3 appends the line; build 1's reduce edit is the precedent, not a dependency. *(roundtable A4, Paige)* **(2)'s rung line is pointer-grammar** per contract `:226` (subject + directed read — *"research runs — any partner, as itself: Capabilities, the lane sentence"*), never rule content; the brief greps it against `:226`'s copy falsifier. *(roundtable A19, Quinn)* **(3)** retires the word *Researcher* from Creative `:37`'s remedy; the *Librarian* half (thin wiki) stands.

*(added 2026-09-16)* **Q16 — A16-6: how does the rung line reach an existing vault?** `vlt-setup:275`
seeds `_agent/reflexes.md` *if absent, never touching a populated file*. Options the capture sees:
(a) seed-only — existing vaults add the line by hand (a CHANGELOG notice); (b) an additive
upgrade-side step that appends one pointer line under the rung's promote-in/edit-one-out rule and
cap (a durability-posture question — B1 preserve path in play); (c) skip the rung, contract sentence
only.
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): (b) — an additive upgrade-side step** appending one pointer line under the rung's cap and promote-in/edit-one-out rule. The rung is the Beat 1 file every partner reads; a contract sentence alone does not reach the memory the belief lives in. B1 preserve path re-checked at brief.
*(roundtable A4, 2026-09-16 — seven voices, no dissent):* (b) stands and becomes a **consumer of D9** (below) — the same act class Q12's charter seed needs, defined once in build 2. Two clauses (b) lacked: **idempotent by exact line** (a second upgrade never appends twice); and **at cap the step degrades to a human-gated offer** in `vlt-upgrade/SKILL.md:79-84`'s migration list and records the skip in the upgrade report — an unattended upgrade can neither edit-one-out nor argue the cap, so it **never exceeds the cap** (Paige, Winston, Carson). Winston's always-offer position conceded once the class was named.

*(added 2026-09-16)* **Q17 — A16-7: is `delegate` in Cycle 16 at all, and if so is it bound to
A16-3's build?** The runner is partnerless by construction and its governance carriage *is* A16-3's
(pointer to the card and rung in the engine prompt). Sequence with or after A16-3; whether that is
one build or two with an ordering is the owner's.
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): IN, and bound to A16-3's build (build 3).** Internal order: carrier, then runner.

*(added 2026-09-16)* **Q18 — A16-7: the neighbour list and `consult@1`.** Adding `delegate` to
`conventions/consult.md:29–32` (what moves, per neighbour) reads as a prose clarification — the class
definition at `:23–27` and the trigger rule pointer at `:36` are untouched. Ruling: clarification
(no bump; brief verifies bipartite consistency), or a rule change (bump + re-ack `vlt-dispatch`,
`vlt-lint`)? *Capture's read, unaccepted: clarification, provided delegate stays a sibling and never
"a consult that does work".*
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): PROSE CLARIFICATION, no `consult@1` bump**, provided delegate stays a **sibling** of consult and is never "a consult that does work". The brief verifies bipartite consistency; the roundtable is asked to hunt the sibling claim.
*(roundtable A11, 2026-09-16 — the sibling claim, hunted; Winston, Carson, Caravaggio, Quinn):* **The convention half holds; the machine half did not.** **(i) The `delegate:` block had no decay contract:** the shipped drain predicate is a positive header list (`vlt-vitals.py:604-617` files any other header as `other` and skips it; `vlt-decay/references/drain.md:9`; `vlt-decay/SKILL.md:36`; contract `:314`'s decay row names `consult:` retained) — a `delegate:` block would accumulate on the live board forever with none of consult's reason for exemption, and the table's own rule (*enters this table in the act that creates it*) would be violated. Ruled: **`delegate:` blocks are drain-eligible when written** (bounded, like `relay`); the four sites gain the kind; **the header is a distinct kind, never `consult:` with an `op` field.** **(ii) The sibling's real ground is trigger populations, not the neighbour list** (Carson): consult reaches for a **partner** (test: memory, `:282`); delegate reaches for a **runner** (test: findable-later, A16-6 (5)) — disjoint, eliminated, no precedence. The 2×2 paragraph says so, and `:282`'s "reaching for another partner … its test is memory" narrows to partner reaches. **(iii) The surface that already defines consult as a relay** (`vlt-dispatch/SKILL.md:15` "a `relay` whose drain happens immediately") **would produce "a consult whose return is a note"** in the same house style (Caravaggio): the brief's verification adds a **grep-negative** over `skills/vlt-dispatch/` and the contract — no sentence defines `delegate` in terms of `consult` ("a consult that/whose", "like a consult"); the mode bullet at `:13-16` is written on the 2×2's two axes; `conventions/consult.md:29-32` **points at the contract's 2×2** for the full set rather than enumerating it. **(iv) Dispute D-5, owner-ruled: SYMMETRIC** — whatever `S-4` shows for the subagent kind applies to `vlt-consult.js` and `vlt-delegate.js` alike; `vlt-consult.js:138`'s "no rule-card or contract read" clause (and `references/consult.md:9`) is **retired** if the carriage reaches subagents and **replaced by the same pointer** if it does not — consult writes its own `thread.md` (`:141`), so it is a writer (Quinn, Carson, Amelia, Winston). Dissent on record (Sally): exempt consult by write posture and let the promise read "every session that writes".

*(added 2026-09-16)* **Q19 — A16-7: the return union and depth ceiling as filed.** `done{notePath,
headline, verification, wikiCandidate} | incomplete{wipPath} | insufficient-context | needs-human |
too-big`; depth `quick|moderate`, `deep` → `too-big` → relay; `op` single-tenant (`research`) under
the population cut (not a shared lane). Accept as filed, or amend? Victor's dissent (generalize now)
is on record and was rejected by the cut.
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): ACCEPT AS FILED.** `deep` → `too-big` → relay is the only deep route ~~.~~ **through delegate** *(roundtable A11, Carson — four words: as worded, build 3 would re-state in module source the belief A16-6 (1) exists to dissolve, "deep research goes to the Researcher", when a Creative may run `vlt-research` deep in its own sitting; the 2×2 paragraph names the in-sitting run as the other route)*; `op` single-tenant (`research`). Victor's dissent stays on record and stays rejected — and Victor conceded at the table that the single-tenant ruling composes with D6 once the carrier is the pointer pair and delivery is per kind: *a second tenant next cycle is an enum change, never a second engine.*
*(roundtable A12, 2026-09-16 — `incomplete` and the killed runner; Amelia, Sally, no dissent):* **(i) `incomplete` is engine-derived:** `agent()` returns null on non-return (`vlt-consult.js:155-166`) and nothing typed comes back from an interrupted subagent — the engine derives `incomplete{wipPath}` from *null return + newest `{research}/*.WIP.md` since spawn*; its **at-rest instrument is a pre-planted `.WIP.md` fixture with a runner forced to null** (e.g. unreadable `skillsPath`), because a cooperative "stop after writing WIP" prompt tests the fix's shape (brief-anatomy §9 forbids it); the true-interruption leg stays Sally's field watch. **(ii) Spawn count is per leg:** 1 for thin / quick / incomplete, **0 for `too-big`** — the engine returns *before* spawning on `deep`, or `too-big` is a spawned agent's opinion ("exactly one agent spawned" in the acceptance as filed was wrong for that leg). **(iii) A killed runner's `.WIP.md` names neither caller nor question**, and `linkage_ripe` (`checks.md:61`) would call it ripe with a nonsense legal response: the engine prompt requires the runner's `.WIP.md` first lines to carry **`delegated_by: <caller>` and the question**, and the candidacy pass **excludes `*.WIP.md`** and reports **`wip_notes: N of M`** (one line at `checks.md:55`) — pre-existing for headless dives, but build 3 multiplies the population and one line is cheaper than a filing.

*(added 2026-09-16)* **Q20 — A16-8: alias lifetime.** `non-negotiable-gate` accepted beside
`write-gate` for one release (the filing), or indefinitely (no shipped reader parses the key —
`vlt-track:38` binds by description and no lint reads loop-profile keys — so an alias costs nothing
to keep and a sunset costs every wearer an edit).
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): INDEFINITE.** Nothing parses the key; the alias is free to keep and a sunset costs every wearer an edit.

*(added 2026-09-16)* **Q21 — A16-8: does `vlt-upgrade` offer the wearer-side rename?** Its migration
list (`vlt-upgrade/SKILL.md:79–84`) is where human-gated offers live and `:81` already enumerates the
profile keys. Offer the rename per wearer (never rewrite a partner's capability file unasked), or a
CHANGELOG notice only?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): CHANGELOG notice only.** Five wearers, one-word edit each, alias means nothing breaks; a migration offer is machinery for a non-problem.

### Cross-filing decide-once rulings

Decisions that must resolve identically across filings. Unfilled.

**D1 — one `frontmatter@14` bump, or several?** The capture flags this at four entries: A16-3 (2),
A16-4 (1)/(2)/(3), and all four of A16-5's directions are **rule changes** to `frontmatter.md`
(version 14 at `:11`), each demanding a `version:` bump **and every consumer re-acked in the same
build**. The capture's read is that ideation should group them so the bump happens **once**; it
explicitly calls this *ideation's call*. Note the exclusions the capture already drew: A16-1 (a) is
a **prose clarification, no bump**; A16-2 (2)'s report slot, if any, is `report.md`, **not** the
convention.
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): ONCE, in build 2** (`frontmatter@14` → `@15`); build 2 owns the bipartite-consistency verification across all ten consumers.
*(roundtable A14, 2026-09-16, Builder — no dissent):* one re-ack is otherwise hollow. `vlt-consult.js:136`'s lite boot reads `identity.md` + `thread.md` **unconditionally**; after build 2 a consult of the Researcher would still load its `## Self` whatever `memory:` says, so `vlt-dispatch`'s `@15` ack would be true in the summon and false in the consult. **D1's re-ack list carries one site line: `vlt-consult.js` honours `memory:`** (skip identity/thread reads on `reflexes`); build 3's `vlt-delegate.js` clone inherits it. *(roundtable A10, Amelia)* The re-ack edits the literal `frontmatter@14` inside the scanner prompt (`vlt-lint-full.js:297/:299`), which moves `scanFingerprint` — the reason the `@15` release can never be the warm release Cycle 15's watch waits for; see Release shape.

**D2 — the `demote` verb is a shared dependency.** A16-4 (2) asks for it (the ladder only lifts;
`grep` for `reset`/`demote` across `vlt-groom` returns nothing) and A16-5 (1)'s charter check
**depends on it** (groom proposes demotion of off-charter material). It must be sited once. Which
build owns it, and do both consumers ship in the same cycle or does one wait?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): BUILD 2 OWNS `demote`**; both consumers (A16-4 (2) casebook, A16-5 (1) charter check) ship in the same build — it is the same `vlt-groom` edit.
*(roundtable A13, 2026-09-16, Quinn — no dissent):* **the verb ships with the axis it moves on.** The contract's ladder (`:228-238`) is one column of rungs ordered by *durability*; `promote` is "move material up a rung" (`:240`); `vlt-groom` classifies every item against the ladder's *entry criteria* (`groom-pass.md:11`) — so as ruled `demote` has no position on the ladder and no criterion of the same kind (every existing criterion is the item's own test; demote's trigger is the *file's* budget or the *owner's* charter). The casebook is durable AND low wake-cost — on a one-axis ladder it is both above and below `identity`, and groom would "promote" casebook narratives back into `## Self` because that is what *up* means. ST-8 asked for "a second axis" in so many words. **D2 gains:** *the ladder table gains a second column, **wake-read** (`Beat 1` / `Beat 2` / `point-of-use`); `casebook.md` and the wiki are point-of-use; `demote` moves material along the wake-read axis only, never along durability; its criteria are budget (Q8) and charter-fit (A16-5 (1)), stated as file-level, not item-level, tests.* Contract prose in build 2; no extra bump. Brief-time (Quinn): whether `casebook.md` is seeded for the nine existing partners or born on first demote.

**D3 — the cold summon and the partnerless session are the same move, governed and ungoverned.**
The capture states the pairing explicitly: A16-5 (3)'s cold summon is *"the governed form of the
fresh-eyes move that the partnerless session"* (A16-3) *"currently provides ungoverned."* Are they
one mechanism with two entry points, or two independent postures? Ruled once, or the contract
gains two overlapping populations — the **precedence-by-elimination** rule applies.
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): TWO POSTURES, DISJOINT POPULATIONS — eliminated, not precedenced.** Cold summon has a partner and writes a partner-tagged note; the partnerless sitting has none and writes a ~~`(session)`~~ **`(none)`** *(roundtable A8)* note. Nothing overlaps; no precedence statement.
*(roundtable A14, 2026-09-16):* the room found the pair this ruling did **not** cut — cold vs `memory: none` (a `none` partner's every sitting is cold without the tag; one behaviour, two records — Victor, Builder). Resolved by elimination under D-9: `none` leaves the enum this cycle, so `sitting: cold` is the **only** per-summon statelessness and is meaningful on every partner. No third posture remains to precedence.

**D4 — `vlt-groom`'s whole-section acts.** A16-5 (2) (`--reset self|bond|thread`) and A16-4 (3)
(the `identity.md`-becomes-a-card migration, *"a groom act per partner, by reference,
approval-gated"*) both add acts to a skill whose three verbs are item-wise. Are these one new
class of groom act or two separate ones?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): ONE CLASS** — *whole-section acts by reference, approval-gated* — with two members (`--reset`, the identity-to-card migration). Two classes for two acts invites a third definition next cycle.

**D5 — fixtures on the convention side of a read.** A16-1 (3) asks for one specific fixture. Is
that a one-off for this seam, or does the cycle adopt the shape (a read whose input is a
convention gets a fixture on the convention's side)?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): ONE-OFF for this seam.** The shape (a read whose input is a convention gets a fixture on the convention's side) is recorded as a **platform-ledger candidate**, not a build bullet — a standing rule needs an enumeration of convention-reading sites nobody has made.

*(added 2026-09-16)* **D6 — one partnerless carrier, three tenants.** A16-3's partnerless session,
A16-5's cold summon (D3), and A16-7's delegate runner are three entry points onto the same
question: *what does a session with no partner (or a partner without its memory) read, and what
does it owe the record?* The delegate filing's own constraint is *never a second carrier*. Ruled
once: which build owns the carrier, and do the other two consume it in the same cycle or wait?
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): BUILD 3 OWNS THE CARRIER.** Tenants: the `partner: none` sitting (lands in build 2 as a contract posture, gains carriage in build 3) and the delegate runner (consumes in build 3). The cold summon reads through the ritual and is **not** a tenant. Stated in build 3's brief so no second carrier is built.
*(roundtable A5, 2026-09-16 — the most-hunted joint after the wire; Winston, Victor, Quinn, Amelia, Sophia, Carson, Sally):* as ruled, "one carrier" named **three delivery surfaces** — `@import` (Q6), the `SessionStart` hook (Q6 fallback), and "pointer to the card and rung in the engine prompt" (A16-7 (4), decided in the filing before `S-4` and never re-pointed at the harvest) — and the engine build 3 clones (`vlt-consult.js:138`) forbids exactly the third for its own summoned partner. **The gloss:** *the carrier is the **pointer pair** (card + rung), single-homed as text once; a **delivery** per session kind — import, hook, or engine-prompt line — is not a second carrier; a second **copy** is.* An engine-prompt pointer ships **only** for a kind the harvest shows reached by neither import nor hook, and is then *the* carriage for that kind, never in addition (Victor's carried dissent dissolves on that sentence, by his own concession). Whatever the harvest shows for the workflow-`agent()` subagent kind **applies to `vlt-consult.js` and `vlt-delegate.js` alike** (D-5, owner-ruled symmetric; Q18). **The `S-4` register is corrected this session** (the §Spikes rule — written back, never roadmap-only): its Consumers line named "A16-5's cold summon (which reads the card + rung through whichever carriage this spike proves)", contradicting this ruling; the cold summon is struck and the workflow-`agent()` kind is named as its own probe row (Carson). *(roundtable A6)* Under A10 there is no split-release branch, so the "posture with no carriage" interim never reaches a vault; build 2's paragraph is nonetheless written **owes-only** (D8) so that this stays true by construction, not by release timing.

*(added 2026-09-16)* **D7 — the weight lever is pulled from two sides.** A16-4 bounds Beat 1 so
that a full activation is cheaper; A16-7 makes a lite partnerless runner so that a full activation
is unnecessary for a bounded dive. Both are honest; both reduce the rational pressure `ST-9` names
as amplifying. Does the cycle ship both, or does one carry the other's promise?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): BOTH SHIP, each claiming its own outcome at acceptance.** ~~Build 2: activation words under the bound.~~ Build 3: a dive returned in one sitting. Neither claims the other's.
*(roundtable A16, 2026-09-16, Quinn — no dissent):* build 2's line was not ship-verifiable and its ST-9 lever was mis-named. Three partners are over 12,000 the day the wire lands and only owner-run, invoked-only, approval-gated grooms bring them under — "under the bound" cannot discharge at ship. And the Researcher, the partner whose weight ST-9 names as the amplifier, sits at 9,293 — Q8 does not touch the ST-9 pressure at all. **Build 2's line becomes:** *the metric derives per partner and the wire trips for exactly the partners over the vault's bound — ship-verifiable on a fixture; "under the bound" is a field watch owed to owner groom acts; build 2's ST-9 contribution is Q14 (`memory: reflexes`), watch not gate.* Build 3's line stands as ruled.

*(added 2026-09-16)* **D8 — the contract's *Sessions* section is edited by three entries.** A16-3
(2) names the `partner: none` sitting; A16-7 (1) publishes the 2×2 and names delegate; A16-6 (5)
extends read-and-cite at `:282`. The contract is unhandshaked by design (single-home + pointers), so
no bump — but three builds editing one section in one cycle want one owner of the section's prose,
or the rule-card's *Sessions* row (`vault-rule-card.md:50`) is re-pointed three times.
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): BUILD 2 OWNS the *Sessions* section's prose** and lands the `partner: none` paragraph. Build 3 appends the delegate cell and the read-and-cite extension as **additive** edits and re-points the rule-card row (`vault-rule-card.md:50`) **once, at the end**.
*(roundtable A6 + A7, 2026-09-16 — Paige, Caravaggio, Sally, Carson; no dissent):* **(i) The card is hash-checked, so "once, at the end" was a hidden dependency on the single release.** `vault-rule-card.md:11` carries `derived_from: 'vault-operating-contract.md sha256:…'` and `tools/package-lint.py:315` (`check_rule_card`) fails the tag gate whenever the contract's bytes move without a re-derive — build 2's edits would have left the card stale in build 2's own commit. Ruled: **every build that edits the contract re-derives the card's `derived_from:` hash in its own commit**; only the row *wording* at `:50` waits for build 3. **(ii) Three card sites change, not one:** rows `:46` (*cold-start, the hand-off skip* — a fourth posture) and `:47` (*the three files … the promotion ladder + verbs* — four files, four-plus verbs, a charter) go stale in build 2 and are **re-derived by build 2**; the act-blocking line `:30` (*"a partner consults, or it cites"*) changes meaning in build 3 — a card rule line is identity-bearing wording, not a pointer — and **build 3 owns it** ("consults, cites, or delegates a bounded dive") beside `:50`. **(iii) Placement:** build 2 inserts the `partner: none` paragraph (and, per D3/A2, the cold-sitting obligations) **directly after *Ending a sitting* (`:269`) and leaves `:284-288` byte-identical**; build 3's 2×2 lands at `:288`. Session *kinds* and the mechanism 2×2 are different tables. **(iv) What the paragraph says:** build 2's `partner: none` paragraph states what the sitting **owes** (one note, the `(none)` tag, no partner-memory writes, wiki single-writer, no dispatch-slice read) and is **mechanism-free about what it reads** ("reads what the vault `CLAUDE.md` loads") — so build 3 never edits it, which is the only way "additive" can hold whatever `S-4` returns (Sally, Carson). Contract `:159` (the `{log}` section's omit clause) gets an owner: **build 2**, per A8.

*(added 2026-09-16, roundtable A4)* **D9 — the additive write into a populated vault-grown file.** Three
rulings in two builds needed the same new act and none named it: Q12 seeds an empty `## Charter` into
nine populated `identity.md`s (`vlt-setup/SKILL.md:225` enumerates the three *shipped* partners and
never edits a populated file); Q16 (b) appends a pointer line to a populated `_agent/reflexes.md`
(`:275` "never touch"); Q21 declined even an *offer* for a one-word capability edit on the
"never rewrite unasked" principle — and a vault owner reading the release would call the three
inconsistent (Sophia). Builder, Sally, Sophia, Winston, Paige, John, Carson.
**RULED 2026-09-16 (roundtable A4, no dissent): ONE CLASS, DEFINED IN BUILD 2, CONSUMED IN BUILD 3.**
`vlt-upgrade` Step 5 defines *insert-if-absent into a vault-grown agent-zone file*: by heading (a
section) or by exact line (a rung line); **idempotent** (a second upgrade never inserts twice);
`migrations_run`-tokened; walks **installed** `vlt-agent-*` partners, not the shipped three; the B1
local-mint preserve path checked **once**, here; never rewrites, never reorders. **At cap it degrades
to a human-gated offer** in the migration list (`SKILL.md:79-84`) and records the skip in the upgrade
report — never edit-one-out, never exceed the cap. Members: the empty `## Charter` with placeholder
prompts (build 2 — Q12); the rung pointer line (build 3 — Q16 (b)). Both `binds:` rosters carry D9.

**R1 — a standing rule, home named (roundtable, 2026-09-16, Sophia; no dissent).** *"An upgrade may
add **empty structure** to a vault-owned file — a section heading, one pointer line under the file's
cap; it never adds or changes **content**, and never touches a partner's capability body."* **Home:**
`vlt-upgrade/SKILL.md`'s Step-4/Step-5 durability posture (Step 4 today says only *never auto-rewrite
a partner's body*). The home's edit is itself build 2's (D9's defining build), so this declaration is
the interim posture until build 2 ships; the v0.19.0 field-notice block states the rule once, above
the builds, so the three postures read as one hand.

### Spikes

**The register is the record; this section is its view.** Mechanics single-homed at
`factory/platform/spikes/README.md`. An owner ruling here — open a spike, kill one, rule a build
`spike: none` — is **written back to the register file in the same session**; status and
`verdict:` live there, never only in roadmap prose.

Open against this cycle (register `status:` as of 2026-09-16):

- **`S-4` (vault-claude-md-imports-per-session-kind) — `proposed`** — *Does an `@path` import line
  in a vault-root `CLAUDE.md` load for EVERY session kind the module runs in the current Claude
  Code runtime — interactive, headless op (`claude -p`), partner summon, and subagent — or only for
  some; and does the same hold for a `CLAUDE.md` pointer that names a path without `@`?*
  Opened by capture from A16-3; **direction 1 rests on it**, direction 2 does not. `build-brief`
  blocks a build whose `spike:` names `S-4` until the register file reads `harvested` or
  `consumed`. Owner ruling needed: **run it, kill it, or rule the A16-3 build `spike: none` by
  taking the `SessionStart`-hook fallback instead.**
  **RULED 2026-09-16 (round 2): RUN IT.** `S-4` binds build 3 (`spike: S-4`); its harvest is the
  condition on the cycle's single release. The owner's stated reason on record: it is one session,
  and it is the only thing in the cycle that can make build 3's already-written promise ("every
  session, partnered or not") come out false — the fallback hook's per-kind reach is the same
  unknown in another form, so ruling the hook would carry the reach as an assumption. The
  timebox as registered stands (one session, one probe per session kind, canary line, record which
  kinds run the hook too). Written back to the register file (`## Ruling` section) this session;
  `status:` stays `proposed` until the probing session starts, per the register's own table.
  *(roundtable A5, 2026-09-16 — written back to the register file this session):* the Consumers line
  **drops the cold summon** (D6 rules it not a tenant; the register contradicted the ruling — Carson)
  and **names the workflow-`agent()` subagent kind as its own probe row** — the delegate runner and
  the consult lite boot are that kind and, per D-5, come out identical whatever it shows. The
  harvest must also record whether the `SessionStart` hook fires for an in-session spawn.

Carried, not open (visible so it is not rediscovered at brief time):

- **`S-3` (github-notification-semantics) — `harvested`, `verdict: reshape`, `consumed_by: []`** —
  harvested 2026-08-24, **unconsumed for a fifth cycle** (Cycle 15 carry 11). It gates nothing (a
  harvested spike satisfies `build-brief`), but its reshape has never been cut into an answerable
  question. Does Cycle 16 consume it, re-cut it, or carry it again?
  **RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): CARRY AGAIN**, `opened_by` restamped to Cycle 16 in the register file this session. Nothing in this cycle touches GitHub notification semantics; re-cutting a spike nothing needs is work for its own sake.

Spikes this batch newly demands: **RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): NONE.** The engine question is module source; the rest is greppable prose.

*(added 2026-09-16)* **The addendum opened no spike, and `S-4` now underlies two entries.** A16-7's
runner is partnerless; its governance carriage is whatever A16-3 direction 1 or its
`SessionStart`-hook fallback turns out to be — so **`S-4`'s ruling (run / kill / rule-around) now
gates A16-7's brief as well as A16-3's.** The engine question (one spawned agent, typed return,
depth-1) is module source (`vlt-consult.js:19–24`), not external — no spike. A16-6 and A16-8 are
greppable prose; no spike.

### Evidence-debt dispositions

Each debt attached to a build, or ruled not-blocking. Unfilled.

**E1 — A16-1's triggering fragment is unpersisted.** The first discovery run's
`section located: false, 0 slugs` exists only as an operator record; the persisted report
(`{lint_reports}/2026-09-03-1206-lint.yaml:6`) carries the second, by-eye read. *A `located: no`
that was overridden leaves no trace in the report* — which is itself the finding. Attach to a
build, or rule not-blocking?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): NOT BLOCKING.** The Q2 fixture is the catch; a report-shape change to log overridden reads is a separate filing if ever wanted.

**E2 — A16-2's field debt is denominated but unowned.** 55 entries across 22 pages are
post-adoption and illegal; 240 bare-path entries across 83 of 146 pages exist on disk and **no
reader can tell which are legal**. Vault-side by the capture's reading (see Q5). Not-blocking for
the module builds, or does a build owe the census that makes the count watchable?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): DISCHARGED BY Q3 (a) — attached to build 1.** The census line is the instrument that makes the count watchable.
*(roundtable A9, 2026-09-16, Mary — no dissent):* "watchable" now has a number. Re-derived read-only today: **240 entries / 83 pages of 152** (the wiki grew six pages since capture); 55 are the post-adoption debt, **≈185 are legal-until-edited** under rule 4's no-backfill clause — repairing the 55 moves the line to ≈185, not 0, and the count also falls for a *legal* reason (a substantive edit adopts the form) while it rises only through the writer build 1 fixes. So a falling number is not evidence the 55 were repaired and a flat one is not evidence they weren't. **Baseline `240 / 83` and floor `≈185 entries`** (the page figure is not derivable — some pages hold both kinds) are the meaning of "done". Build 1's ledger carries **one bounded check** instead of the unbounded "watch it fall": *the first post-upgrade full sweep on `{field-vault}` renders the census line and its value equals an independent recount* — ship-verifiable on upgrade evidence.

**E3 — A16-2's adjacent carry must be read before (2) is scoped.** Cycle 15 closeout carry 9's
`sources_vs_prose_mismatches` tier question (refused wholesale on consecutive sweeps;
`{backlog}` carries a standing human ruling on four pages) touches **the same reduce** as Q3. The
capture states: *a brief for (2) should read the carry before it scopes.* Is that an obligation on
the brief, or does the carry get filed first?
**RULED 2026-09-16 (round 3, build 1 — clerk's read accepted by the owner): OBLIGATION ON THE BRIEF.** Build 1's briefer reads Cycle 15 carry 9 before scoping the reduce edit; the carry is not filed first.

**E4 — A16-4's word table was not re-measured.** The 9-of-9 partner word census is carried as
filed (2026-09-09, `wc -w`); the one instrument that could have corroborated it reports the wrong
unit — which **is** the gap the filing names. A build that sets a budget sets it against numbers
nobody re-derived this run. Blocking, or accepted?
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): DISCHARGED** — re-measured this session (table at Q8); the budget is set against today's numbers.

**E5 — A16-5's field evidence was not re-read** beyond the session census at A16-3. Same shape as
E4, smaller stakes.
**RULED 2026-09-16 (round 4, build 2 — clerk's read accepted by the owner): ACCEPTED, NOT BLOCKING.** The `identity.md` sizes at Q8 are the same evidence in a coarser unit; the specimen quotes are in the filing.

**E6 — five candidate filings are owed and unwritten** (Cycle 15 carry 7: build-3's optional args;
build-4's `pageHashes` digest form, field-confirmed; build-5's `para_type_unknown` count leg;
build-7's five-value enum + partner-side attestation beat; A15-12's subtree-`type:` mechanism).
None blocks a Cycle 16 build on its face; recorded so the cycle does not close over them silently.
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): NOT BLOCKING any Cycle 16 build.** The owner writes them via the rail when ready; recorded so closeout does not pass over them silently.
*(roundtable A9, 2026-09-16, Mary):* a **sixth** owed filing joins the list so E1's ruling is not the silence E6 exists to prevent — *build-1: an overridden `stub_discovery` read (`located: no` corrected by eye) leaves no trace in the persisted report — owner to file.*

*(added 2026-09-16)* **E7 — A16-6's belief-in-memory half is inferred, not observed.** The filing's
own recovery grep (`Researcher` near `lane` under `## Self`, nine `identity.md` files, read-only)
found **nothing**; the owner's report of partner speech is the whole evidence and no instrument
persisted it. The module-source half (the SKILL listing + *Capabilities* prose) is fully grounded.
A build that ships the rung pointer (Q15 (2)) ships it against an inferred cause. Blocking, or
accepted with the watch (*a partner that formerly declined now runs, delegates, or cites*) as the
only read-back?
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): ACCEPTED, with the watch as the only read-back.** The module-source half is fully grounded and is what the sentence fixes.

*(added 2026-09-16)* **E8 — A16-7's cost claim is the owner's report, count only.** *"A task needing
one external fact spans ≥2 sessions"* — no instrument persists task closes across sittings, so the
set is unrecoverable and the capture says so. The acceptance the filing proposes is entirely
at-rest (temp-vault fixture), which is right; the field tail (first live `delegate:` block from a
non-Researcher partner) is a watch. Not-blocking on the capture's read.
**RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): NOT BLOCKING.** Acceptance at rest against a temp vault, as filed; the field tail is a watch.

### Questions deliberately left to brief time

Per-build, not cross-cutting. **RULED 2026-09-16 (round 5, build 3 + cycle-wide — clerk's read accepted by the owner): exactly these, nothing cross-cutting.**

- **build-1:** the census line's exact report field (Q3 (a)'s `bare_path_sources` shape in `report.md`)
  — *within A9's constraints: full-mode only, three-term, script-side, string-equality gate*; the
  reduce-side drop mechanism *within the A9/A10 constraint* (no `PAGE_SCAN` edit); the C15 build-3
  check (4) `grep '## Stubs'` count moves from 1 to 2 under Q1 (a) — note it, expected 2 (Amelia).
- **build-2:** the casebook's decay-contract values; the charter's minted template text (Q12) and the
  placeholder prompts the seed carries (A3); the `partner: none` paragraph's wording in *Sessions* (D8
  — build 2 owns the section; owes-only, mechanism-free about reads); the cold summon's utterance
  wording (A2); whether `casebook.md` is seeded for the nine or born on first demote (A13); the
  demote criterion when the charter is empty (A3); *(roundtable A18)* **the count-word sweep** — every
  "three files"/"three verbs" site re-nouned or turned into a pointer at *Partner memory* (contract
  `:212`/`:240`, `frontmatter.md:183`, rule-card `:47`, `vlt-groom/SKILL.md:4`+`:11`,
  `groom-pass.md:5`/`:10`, decay row `:312`, `vlt-vitals.py:242`'s description).
- **build-3:** the 2×2's wording and whether the section gains a table; whether the `delegate:`
  header shape is the mode signal as `relay:` is; whether a human-invoked delegate tags `(user)`;
  *(roundtable A11/A12/A18)* the four decay sites' exact edits; the grep-negative's pattern list;
  the `.WIP.md` header lines; the `wip_notes` line; **`references/daily.md:60`** and the
  `module-help.csv:13` **`args` enum** join A16-7 (7)'s pointer list ("four modes" claims
  completeness in both).

## Roundtable review — A16-1..A16-8 (2026-09-16)

**Convened** over the filled Ideation rulings above (five rounds, all Q/D/S/E slots ruled), before any
brief. **Roster** discovered fresh, **full 13, nobody excused** (owner-ruled): Mary (analyst), Winston
(architect), Builder, Amelia (dev), John (PM), Paige (tech writer), Sally (UX), Carson (brainstorming),
Dr. Quinn (problem-solving), Maya (design thinking), Victor (innovation), Caravaggio (presentation),
Sophia (storytelling). Owner's prior worries: none named; the roadmap's five seams (D6 carrier gap,
Q18 sibling claim, D8 three-build section, Q8 three-trip budget, the S-4 release condition) carried
verbatim into every prompt. Thirteen returns, ~75 findings, merged to nineteen joints; every voice
returned both mandatory beats. Session file:
`_output/party-mode/2026-09-16-cycle16-roadmap-roundtable-session.md`; keepsake:
`_output/party-mode/2026-09-16-cycle16-roadmap-roundtable.html`.

**Amendments — applied above, each marked *(roundtable A#)* at the section it amends:**
- **A1** — Q8/Q9 + build-2 promise: the wire binds a denominated count (`partners_over_activation_budget: N of M`); per-partner words render beside bytes; 12,000 lives once in the seed wire's `threshold:`, the contract points at it; `surface_text` names the response in order (charter, then D4 groom) and the fork (identity-heavy → groom; SKILL-heavy → rebirth); the read set is `memory:`-posture-aware; three trips at ship are the expected state; promise "a budget a wire trips on".
- **A2** — Q13: a `sitting: cold` may host an owner-invoked, approval-gated groom; cold reads SKILL + charter + reflexes + card + rung; trigger is the summon utterance before the identity read; `cold` in the log summary, never the paren.
- **A3** — Q12 + build-2 promise: an empty `## Charter` disables the charter check and says so; the seed carries the mint prompts as placeholders; the first-meeting test reads Bond/Self only; the lint half of A16-5 (1) dropped for keep-only in the groom diff (`declared`); the mint-time `## Self` seed retired; promise "a charter slot the owner fills".
- **A4** — new decide-once **D9** (additive write into a populated vault-grown file, defined build 2, consumed build 3; idempotent; at cap → human-gated offer); Q16 (b) consumes it; Q15 (2)'s rung line is pointer-grammar per `:226`; both `binds:` carry D9.
- **A5** — D6 gloss (carrier = the pointer pair; a delivery per kind is not a second carrier, a copy is; engine-prompt pointer only for an unreached kind); Q6: hook fallback is a second `SessionStart` entry keyed on its own path, never `--strip`; narrowing written into build 3's promise line; the S-4 register's Consumers line corrected (cold summon struck; workflow-`agent()` kind its own row).
- **A6** — D8/Release shape: build 2's `partner: none` paragraph is owes-only and mechanism-free about reads, never edited by build 3; the first-partnerless-note check enters build 3's ledger.
- **A7** — D8: every contract-editing build re-derives the rule-card hash in its own commit; build 2 re-derives rows `:46`/`:47`; build 3 owns `:30` ("consults, cites, or delegates") and `:50`; build 2 inserts after *Ending a sitting* (`:269`), leaves `:284-288` byte-identical; build 3's 2×2 at `:288`.
- **A8** — Q7/D3: one string on every surface — `partner: none` ↔ `(none)` ↔ `none`; the three omit clauses (`:159`, `frontmatter:167`, `vlt-ingest:24`) narrow to headless ops outside any sitting, edited in build 2; `partner: user`/`partner: vlt-mint` legal-until-groomed.
- **A9** — Q3/Q5/E2/E6 + build-1 park: the census line is full-mode only, three-term, script-side, string-equality-gated; "shows it done" → "shows it stopped growing"; baseline 240/83, floor ≈185; one bounded ledger check (first post-upgrade full sweep equals an independent recount); the drop needs a reduce-side enforcement point under the A9/A10 constraint; E6 gains the E1 filing.
- **A10** — Release shape: **two releases** — build 1 alone first (v0.18.x) so Cycle 15's warm-release watch has its chance; builds 2 + 3 as one release **held whole until S-4 is harvested, no split**; the false "one chance this cycle" parenthetical struck with Amelia's cache-key finding.
- **A11** — Q18/Q19: `delegate:` blocks drain-eligible when written, four decay sites gain the kind, header a distinct kind; the sibling's ground is disjoint trigger populations stated in the 2×2; grep-negative for delegate-defined-as-consult; `conventions/consult.md` points at the 2×2; "the only deep route **through delegate**".
- **A12** — Q19: `incomplete` engine-derived (null + newest WIP), at-rest fixture pre-planted; spawn count per leg (0 on `deep`); `.WIP.md` carries `delegated_by` + question; candidacy excludes WIP and reports `wip_notes`.
- **A13** — D2: the ladder gains a wake-read column; demote moves along it only; file-level criteria.
- **A14** — Q14/D1/D3: `memory:` narrowed to `full | reflexes`; `vlt-consult.js` honours `memory:` (D1 site line); the pilot's baseline derived at brief time, arm named, depth-matched, delegate runs excluded.
- **A15** — Q15 (5): `grounding:` on PARA artifacts, `sources:` on wiki-class; `web_cited_entries` census read-back; Creative `:37` loses the word *Researcher*.
- **A16** — D7: build 2's outcome is "trips for exactly the partners over"; its ST-9 lever is Q14.
- **A17** — build-1 bullet + Release shape: "reaches wearers first" struck; builds 1 and 2 carry CHANGELOG notice text in their own briefs (§8 stub); the release build collates; A16-8's notice says *delete the apology* and *old key accepted indefinitely*.
- **A18** — parks/Q9/A16-7 (7): the count-word sweep; `casebook.md` IN `partner_memory_bytes`; `references/daily.md:60` + the `module-help.csv:13` `args` enum join the pointer list.
- **A19** — the retirements below, written into the build scopes they belong to.

**Rules:**
- **R1** — *an upgrade may add empty structure to a vault-owned file, never content, never a capability body.* Home: `vlt-upgrade/SKILL.md` Step-4/5 durability posture; the edit lands in build 2 with D9; interim posture is the dated declaration at D9 above.

**Owner rulings (live) and dissents on record:**
- **D-1** wired set — keep SKILL.md in it; fork named in `surface_text`. *Dissent: Builder (narrow to identity + reflexes).*
- **D-2** wire owner — `owner: human`, partners in the detail.
- **D-3** cold groom — a cold sitting may host an approval-gated groom. *Alternative recorded, not argued.*
- **D-4** charter lint flag — dropped; keep-only in the groom diff, `declared`.
- **D-5** consult symmetry — symmetric per harvest. *Dissent: Sally (exempt by write posture).*
- **D-6/D-8** release — build 1 alone first; 2+3 held whole, no split.
- **D-7** spelling — `(none)` everywhere.
- **D-9** `memory: none` — narrowed out this cycle. *Dissent: Victor (keep, narrow the detector).*
- **D-10** `cap: 30` — `cap_words:` replaces it. *Dissent: Maya, Paige (keep as shape-only).*
- **D-11** mint `## Self` seed — retired; Self born empty.
- **Open disputes: none.**

**Obsolescence beat — retirements found (P-15):**
- *build-1:* Q3 (a) and Q4 **are retirements** and the record now says so (the bare-path class leaves `malformed_frontmatter`'s verdict kinds; `fix-and-file.md:12`'s residue is deleted, not re-caveated). Q20's indefinite alias is a **deliberate non-retirement**, recorded so no later cycle "discovers" a second spelling. C15 build-3 check (4)'s `grep '## Stubs'` = 1 is obsoleted by Q1 (a) — expected 2.
- *build-2:* `frontmatter.md:167`'s omit clause and its twin contract `:159` → retired by `partner: none`/`(none)`; the reflex cap's deferral posture (`frontmatter.md:224-230`, "mechanical bell deferred … threshold 2 … expiry") → superseded by the Beat 1 wire, retired; the fired line-form falsifier half → retired per `:222`; **`cap: 30` → retired, `cap_words:` replaces** (D-10); contract `:244` "informational until the groom op exists" → dead since v0.11.0, retired; `:217` "writes this freely" → narrowed to below the charter; `:246` "reversible" → points at `--reset`; the mint-time `## Self` seed (`vlt-mint/SKILL.md:132`, template `:111`) → retired (D-11); the "three files"/"three verbs" enumerations → pointers.
- *build-3:* contract `:194`/`:226` ritual card-and-rung read → for every kind the harvest names reached, "arrives with the session; the ritual reads it only for kinds the harvest says are missed" (conditional on harvest, stated in the brief); the seeded `CLAUDE.md` pointer at the 67,844-char contract (`vlt-setup/SKILL.md:202-213` "read it before writing anything") → retired to point at the card (conditional on the interactive kind); `vlt-consult.js:138` + `references/consult.md:9` exemption → retired or replaced per D-5; `references/consult.md:63` needs-work → relay → replacement line; `vlt-consult.js:147`'s engine copy of the routing rule → pointer; rule-card `:18` "Becoming — the ceremony's frame" → re-framed; Creative `:37`'s *Researcher* → retired; `:282`'s population → partner reaches only; `vlt-setup/SKILL.md:200`'s one-line strip promise → retired for any hook-carried kind.

**Instrument beat — the property each build's acceptance must protect (P-20), stated fix-free:**
- *build-1:* **Stub read** — given only the shipped `wiki-index.md` bytes (and an overlay variant), a reader following the procedure returns the heading string a human reads from the convention's Stubs rule: `located: yes` on a long-form index, `located: no` on bare `## Stubs`, with no reference to fences; a fixture that is a *copy* of the convention is not the instrument. **Census** — every bare-path `sources:` entry on disk is counted exactly once on one denominated line whose value equals an independent recount; no per-page finding is raised for the form; a full sweep never increases it. **Writer** — a full sweep over a page whose prose cites a note absent from frontmatter leaves that page's frontmatter byte-identical. **Slot** — a loop profile carrying either key reaches the same gate in `vlt-track` and the relocation scan recognizes both. A16-8 otherwise: none named.
- *build-2:* **Budget** — for every partner, the number reported equals the word count of exactly the files that partner's next activation reads under its declared posture, measured by counting files, never by the metric's own output; every partner over the bound is named by slug on the surface the owner sees at next session start with the act that answers it, and none under is (adversary: a fleet aggregate under while one partner is over; a `reflexes` partner counted full). **Demote** — after an approved demote the material exists at exactly one rung below Beat 1, absent from every Beat 1 read, reachable at its new home and via `archive:`, and the words across all memory files did not fall. **Charter** — an owner-held section is byte-identical after any partner sitting that wrote elsewhere in the file; an empty charter proposes nothing and says so. **Cold** — a `sitting: cold` leaves `identity.md` and `thread.md` byte-identical, yields exactly one note, and a human reading the log alone can tell it was cold. **`partner: none`** — one `(none)`-tagged note, zero bytes under `{partners}/` and `{wiki}`, no dispatch-slice read. **Handshake** — every consumer acks `@15`, none `@14`. **Q14** — watch, graded against the A14 baseline row.
- *build-3:* **Carrier** — in every session kind the harvest names as reached, opened at the vault root with no partner summoned, a canary line in the card and one in the rung are in context at the first turn, once not twice; unreached kinds are stated. **Delegate** — from partner P: exactly one agent (zero on `deep`); at most one note under `{research}` carrying `verified_by: vlt-research` and passing tier-1; P's sitting ends with exactly one session note authored by P; nothing under `{wiki}`; zero relays fired; both `{log}` lines caller-tagged; the `delegate:` block absent from the ledger's open board and every open slice and drained on its bound; a dive stopped before its note, by choice or by kill, leaves a file a human can attribute to caller and question with no log line present. **Sibling** — `conventions/consult.md:23-27`'s bytes and both consumers' `consult@1` acks unchanged after the neighbour list grows; a grep for delegate defined in terms of consult returns nothing. **Lane** — no shipped sentence names `{research}` single-writer or routes a non-Researcher away from `vlt-research`; otherwise none named (E7 watch).

**Capture-don't-interrupt — for `factory/inbox/` at handoff:** the tripwire registry schema takes one static `owner:` (a count wire's debtor varies per trip); `## Thread` has a section bound, not a size (Cycle 17); `vlt-lint-full.js:297`'s prompt-side prohibition ignored in the field (files only if build 1 takes a route the A9/A10 constraint forbids); `vlt-setup/SKILL.md:200`'s one-line strip promise vs hook carriage (files after S-4).

## Deferred acceptance ledger

*(Populated per build at brief time — `build-brief` appends each build's live-acceptance checks here,
tagged ship-verifiable or field-contingent.)*

- [ ] **build-1 (own-writes-read-back, briefed 2026-09-16):** brief
  `factory/cycles/16-closed-loops/briefs/build-1-own-writes-read-back.md`. **Six checks — five
  `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 56/61` (A16-1 1/1 — the convention
  site read by path + the Cycle 15 index pair; A16-2 55/55 as the per-page manifest into `build-1-wiki/`,
  bytes preserved for 1 — the `dutch-oven-braising` line/fragment as the planted return; A16-8 0/5 — no
  wearer bytes reach an at-rest grep). R1 n/a (every rule ships with its mechanism). **Retirement
  SUBSTANTIVE** — the bare-path `sources:` form leaves `malformed_frontmatter`'s population
  (`checks.md:15` exclusion (c) + reduce disposition 3); `fix-and-file.md:12`'s frontmatter-write residue
  deleted; Cycle 15 build-3 (4)'s `grep -c '## Stubs'` = 1 obsoleted (expected 2); **deliberate
  non-retirement:** `non-negotiable-gate` accepted indefinitely (Q20). R4 n/a (no shipped file added;
  fixtures are factory-side). This build is **v0.18.1, alone** (A10). **(1) `[ship-verifiable]` Stub read**
  — property: from the shipped `wiki-index.md` bytes (+ an overlay-merged variant) a reader following
  `checks.md:13` returns the heading; `located: yes` on the long-form index fixture, `no` on the bare one,
  no reference to fences. Instrument: `fixtures/build-1-stub-heading-harness.py` (reads the shipped file
  by path, two readers, overlay case, Cycle 15 index pair; failable against `v0.18.0` bytes — record the
  FAIL count); `grep -c '## Stubs' wiki-index.md` = 2. Adversary answered: read-by-path (a copy would
  pass on a changed heading); overlay restating a heading is `overlay_issues`, named. **(2)
  `[ship-verifiable]` Census** — property: every bare-form `sources:` entry on disk counted exactly once
  on one denominated line equal to an independent recount; no per-page finding for the form; a full sweep
  never increases it. Instrument: `fixtures/build-1-census-harness.mjs` + `build-1-wiki/` +
  `build-1-expected-census.json` (oracle written before the script runs): the 22-page/55-entry manifest +
  controls (flow-form list counted; `.md` under `grounding:` not counted; prose `## Sources` not counted;
  scalar `sources:` absent from the map; `index.md` excluded) → oracle line `57 entries across 23 of 29
  pages …`; reduce cases: `unclassified/['sources']` on a manifest page REFUSED; the same on the
  unparsed page, with `bareSources` absent (+ cap line), as `missing_required/['sources']`, as
  `unclassified/['sources','title']`, as `malformed_block`, and as `unclassified/[]` with sources-naming
  prose ALL REPORT; gate `ok` on the oracle line, `failed` on an off-by-one, exit 2 without `--wiki-dir`
  in full mode; failable against `v0.18.0`'s workflow. Adversary answered with four widenings in the
  fixture; the accepted residual (a bare entry beside a second genuine `sources:` defect reported only as
  `unclassified/['sources']` is refused) is stated. **(3) `[ship-verifiable]` Writer** — property: a
  sweep over a page whose prose `## Sources` lacks an entry frontmatter carries leaves the frontmatter
  byte-identical. Instrument: `fixtures/build-1-reader-protocol.md` (fresh agent, shipped `fix-and-file.md`
  Step 3, `build-1-writer-page.md`, `shasum -a 256` over the frontmatter block before/after equal, prose
  +1 line) + the grep-negative over `skills/vlt-lint/` (brief §Verification 4). Adversary answered: the
  prose-form residual accepted; direction-ambiguous sentences elsewhere unreachable by the grep. **(4)
  `[ship-verifiable]` Slot** — property: a profile under either key reaches the same gate in `vlt-track`,
  the relocation scan recognizes both, the persona *non-negotiable* concept survives. Instrument: the
  greps of brief §Verification 5 recorded verbatim (`non-negotiable-gate` in exactly `vlt-track/SKILL.md`
  + `vlt-upgrade/SKILL.md`, both in accepted clauses; template `write-gate` = 1; persona
  `non-negotiable` count unchanged vs `v0.18.0`; `module-help.csv` Group B pass). Adversary answered: the
  hyphenated key is grepped, the persona count asserted unchanged. **(5) `[ship-verifiable]` Warm-release
  chance + E2 census** — property: v0.18.1 moves none of the cache-key inputs; the first post-upgrade full
  sweep on `{field-vault}` renders `bare_path_sources:` equal to an independent recount. Instrument, at
  rest: `build-4-return-harness.mjs --fingerprint` equal over `v0.18.0` and `v0.18.1`, empty
  `git diff v0.18.0 --stat` over `frontmatter`/`wiki-supersession`/`write-verification`, the `scanModel`
  default line. Instrument, upgrade evidence (bounded — the owner's ordinary `vlt-upgrade` to 0.18.1 + the
  ordinary post-upgrade full sweep on `{field-vault}`): the persisted line vs an `awk` recount over each
  page's frontmatter `sources:` block (unquoted, ends `.md`), one-liner recorded verbatim; baseline
  `240 / 83 of 152` (A9, 2026-09-16). Adversary answered: the discharge recount is not the script.
  **(F1) `[field-contingent]` Wearer parse** — a coaching-style wearer's profile parses under either key
  with no explanatory note. Event: the next `vlt-mint` of a `vlt-track` wearer, or an owner-run rename of
  an existing wearer's `capabilities/track.md` on `{field-vault}`; performer: the owner; vault:
  `{field-vault}` (`career-strategist` is the named case). Watch, not gate.

  **Discharge pass 1 — 2026-09-16 (`acceptance-discharge`, upgrade evidence only; the post-upgrade full
  sweep had not landed at run time).** Upgrade: `vlt-core` **0.18.0 → 0.18.1** at `[2026-09-16 17:43]`
  (`_agent/upgrade-ledger.md:417`; report `_agent/upgrade-reports/2026-09-16-1743-upgrade.yaml`) — own-the-apply,
  7 mints preserved, base divergence none, `wiki-index.md` the one convention refreshed, 4 skill-asset
  divergences ruled *sanctioned* by the owner in-session. **Item stays unchecked — split** (one sub-clause open).
  **Upgrade-side + at-rest DISCHARGED: (1), (2), (3), (4), (5) at-rest half, (F1). STILL-OPEN: (5)'s E2 census
  recount.** Every at-rest instrument was **re-run independently in this discharge run**, not taken from the
  BUILT record.
  - **(1) Stub read — DISCHARGED 2026-09-16.** `fixtures/build-1-stub-heading-harness.py` re-run: **8 rows,
    0 failed**, reading the shipped convention by path (both readers, base + overlay, the Cycle 15 index pair,
    the stated-twice row); `grep -c '## Stubs'` = **2** (disposition 3). Reached the field: the vault's installed
    `_meta/conventions/wiki-index.md` is byte-identical to shipped (`md5 -q` = `e6deb3ce2e8d8783ae73131629ca6604`
    both sides), stating the heading in prose at `:80`; the field index carries the long form at
    `resources/wiki/index.md:374`, so the first sweep has a `located: yes` to return. Failability on record
    (6/8 FAIL over `v0.18.0` bytes).
  - **(2) Census — ~~DISCHARGED~~ → REVERSED to FAILED in pass 2, same day (owner-ruled). Pass-1 note kept for the record:** `fixtures/build-1-census-harness.mjs` re-run: **all expectations
    hold** across all three phases — phase 1 oracle `57 entries across 23 of 29 pages` deep-equal; phase 2 A(a)–(j),
    B(a)–(c), C, D, E, F (disposition 3 refuses only the byte-gated case; `bareSources` absent degrades with the cap
    and never refuses; wrong-typed intake refused pre-dispatch by name at 0 agent invocations); phase 3 gate `ok`,
    `failed` on the off-by-one with the exact reason string, scoped-mode ok, `exit 2` without `--wiki-dir`.
    Failability on record (5 FAIL over `v0.18.0`'s workflow).
  - **(3) Writer — DISCHARGED 2026-09-16, one owner call outstanding.** Grep-negative re-run over
    `skills/vlt-lint/`: `never writes into frontmatter` exactly **1**, the three prohibited patterns **0**. The
    vault's installed `fix-and-file.md:12` carries the shipped clause verbatim. The fresh-agent reader-protocol
    leg is not re-runnable in a discharge run and rests on its recorded result (frontmatter sha256
    `851f5dcf…ceca` before == after, prose list 2 → 3) — stated, not re-proved. ⚠ **Owner call the BUILT record
    deferred to this check (deviation 4):** whether a mismatch fix is a *substantive edit* for the Step 3 preamble
    (`fix-and-file.md:7`) and the attester paragraph (`:18`), both of which instruct frontmatter writes while the
    F3 bullet demands a byte-identical frontmatter block. **Unruled as of this run**; the failure direction is
    over-reporting (a tripped clause), never a silent `sources:` write.
  - **(4) Slot — DISCHARGED 2026-09-16.** Greps re-run over `skills/`: `non-negotiable-gate` in exactly
    `vlt-track/SKILL.md` + `vlt-upgrade/SKILL.md` (both the accepted-indefinitely clauses), template `write-gate`
    = 1. Reached the field: the vault's installed `capability-template.md:68`, `vlt-track:15`/`:38` and
    `vlt-upgrade:81` all carry the rename post-apply.
  - **(5) Warm-release chance + E2 census — SPLIT in pass 1, FULLY DISCHARGED in pass 2 (E2 matched).** *At-rest half DISCHARGED 2026-09-16:*
    `build-4-return-harness.mjs --fingerprint` = `fe29c6f398d02c6b1cdf` on the 0.18.1 tree, equal to the value
    recorded on `v0.18.0`; `git diff v0.18.0 v0.18.1 --stat` over `frontmatter`/`wiki-supersession`/`write-verification`
    **empty**; and the vault's own upgrade record states it independently — *"the first full `vlt-lint` after this
    release is WARM by construction (no cache-key input moved) — a cold `lint_cache:` line on the next full sweep
    is a finding to file."* *STILL-OPEN:* **the E2 census recount.** No post-upgrade sweep exists — the newest is
    `_agent/lint-reports/2026-09-15-1134-lint.yaml`, pre-upgrade. **Discharging event:** the first post-upgrade
    full sweep's persisted `bare_path_sources:` line compared against the independent `awk` recount over each
    `{wiki}` page's frontmatter block, the one-liner recorded verbatim (baseline `240 entries across 83 of 152
    pages`, A9 2026-09-16 — the vault may have moved). **Trigger:** the owner's agent, sweep in flight as of this
    run. **(Cycle 15 build-2 (6)'s warm `lint_cache:` line rode the same sweep and FAILED — see the addendum
    below; it is that closed cycle's watch, not this row's, and nothing here is re-graded on it.)**
  - **(F1) Wearer parse — DISCHARGED 2026-09-16 (residual stated; no subject substitution).** The named event
    fired **five minutes after the upgrade**: the owner renamed the slot in two wearers' profiles —
    `_agent/partners/career-strategist/capabilities/track.md:37` and `.../football-analyst/capabilities/track.md:181`
    now read `write-gate:` (mtimes 17:48:49 / 17:48:54; vault commit `2fd4a01`, *"cut the loop-profile
    parentheticals"*), and the explanatory notes the release told wearers to delete are **gone**. The three
    unrenamed wearers (`chess-coach:30`, `dog-trainer:20`, `health-coach:25`) still read `non-negotiable-gate:`
    and stay legal indefinitely (Q20; `vlt-track:38`) — **both keys live side by side in one vault, neither
    carrying an apology.** `career-strategist` is the check's named case; nothing substituted. **Residual:** no
    `vlt-track` loop has yet run against a renamed profile — nothing parses the key by design, so the rename act
    is the exercise the check named, and the parse proper rides the next loop session.


- [ ] **build-2 (partner-memory-schema, briefed 2026-09-17):** brief
  `factory/cycles/16-closed-loops/briefs/build-2-partner-memory-schema.md`. **Eight checks — six
  `[ship-verifiable]` (GATE), two `[field-contingent]`.** `specimens: 13/15` (A16-4 11 observed — the
  9-partner Beat 1 word table re-measured 2026-09-16 and carried as Q8's basis, the Researcher reflex
  specimen as the `cap_words:` calibration, and the football-analyst triggering fragment preserved **as
  shape, not bytes** — its live `## Self` is a real person's vault prose and cannot ship into
  `fixtures/`, so the §Verification-6 fixture reconstructs four dated `###` narratives rather than
  freezing them, and the brief says so; A16-3 2/2 — the two anomalous `partner:` values become the
  `@15` bump's legal-until-groomed clause; A16-5 0/2 — its two quoted `identity.md` fragments are the
  same unshippable class and no check rests on them, E5 ACCEPTED). **R1 SUBSTANTIVE, two instances** —
  (a) the `partner: none` paragraph is a rule whose carriage is build 3's, so it is written **owes-only
  and mechanism-free about reads** (A6), and under A10's no-split release the window never reaches a
  vault; (b) the charter guard ships `enforcement_stage: declared` with the full deferral triple
  (metric: observed partner edits to a `## Charter`; threshold 2; `review_after: 2027-03-17`), the
  render surface being keep-only in every groom diff (dispute D-4). **Retirement SUBSTANTIVE** —
  `frontmatter.md:167`'s omit clause, contract `:156`'s twin and `vlt-ingest:24`'s third all narrow to
  headless ops outside any sitting; the reflex cap's deferred-bell posture (`frontmatter.md:230`) and
  its fired line-form falsifier half are superseded by the Beat 1 wire; `cap: 30` → `cap_words:`
  (D-10); contract `:244`'s *"until the groom op exists"* dead since v0.11.0; `:217`'s *"writes this
  freely"* narrowed to below the charter; `:246`'s *"reversible"* gains `--reset`; the mint-time
  `## Self` seed retired (D-11); the "three files"/"three verbs" enumerations → pointers.
  **Deliberate non-retirements:** `partner_memory_bytes` sits beside the new metric (Q9), and the
  field's `partner: user` / `partner: vlt-mint` values stay legal-until-groomed (A8). **R4** — the new
  `casebook.md` widens `partner_memory_bytes`' filename tuple and description, the contract's *Decay
  contracts* table, and `frontmatter.md`'s partner-memory section; **declared exclusions:** it is
  outside `activation_words` (never wake-read) and takes no wire. **R3** — the one new finding class is
  the `activation-budget` trip, whose legal response homes in `surface_text` with its order (charter,
  then groom; identity-heavy → groom, SKILL-heavy → rebirth). **R2 n/a** (no new `package-lint`
  check). **This build is NOT the release** — builds 2+3 ship as one v0.19.0, held whole until `S-4`
  harvests (A10). **(1) `[ship-verifiable]` Budget** — property: per partner the reported number equals
  the word count of exactly the files that partner's next activation reads under its declared posture,
  every partner over the bound is named by slug on the surface the owner sees at next session start
  with the act that answers it, and none under is. First post-upgrade SessionStart on `{field-vault}`:
  `activation-budget` tripped, denominated, detail naming exactly the partners over 12,000 — expected
  **librarian / football-analyst / creative** (22,144 / 19,394 / 16,021) and **the other six expected
  under, which is half the check**. Instrument: a six-partner temp-vault fixture with a hand-written
  oracle (over on identity mass, over on SKILL mass, under, a `reflexes` partner whose `full` total is
  over, one missing `reflexes.md`, one with a `casebook.md`), proven failable against v0.18.1.
  Adversary answered: the fleet-aggregate-under state is unreachable because the wire binds a
  denominated count, not a total (A1); the `reflexes`-counted-full state is the fixture's fourth
  partner; a **third** state was found and **widened**, not accepted — an unresolvable `SKILL.md`
  derives `None` and reads *not tripped*, i.e. a missing file looks like a partner under budget, so the
  derivation names it in `notes[]` and the display prints `n/a`. **(2) `[ship-verifiable]` Demote** —
  property: after an approved demote the material sits exactly one rung below Beat 1, absent from every
  Beat 1 read, reachable at its new home and via `archive:`, and the words across all memory files did
  **not** fall. `casebook.md` holds the narratives, `## Self` does not, `activation_words` falls,
  `partner_memory_bytes` does not (A18). Instrument: the §Verification-6 reader protocol + the fixture
  re-derived before/after. Adversary answered: demote-as-delete passes "absent" and "words fell" — the
  words-did-not-fall and `archive:`-reachability clauses exist for it; wiki-by-Librarian-hand-off is a
  legal second destination and is accepted. **(3) `[ship-verifiable]` Charter** — property: an
  owner-held section is byte-identical after any partner sitting that wrote **elsewhere in the same
  file**; an empty charter proposes nothing and says so. `shasum` before/after equal; the groom diff
  prints *charter empty — nothing to check against*; a filled charter proposes off-charter demotions.
  Adversary answered: a sitting writing nothing at all would pass vacuously, which is why the property
  requires a sitting that wrote elsewhere (gate-2, applied at brief time). **(4) `[ship-verifiable]`
  Cold** — property: a `sitting: cold` leaves `identity.md` and `thread.md` byte-identical, yields
  exactly one note, and a human reading the log alone can tell it was cold (paren holds only the slug;
  `cold` after the `|`). Instrument: an agent reader protocol over the shipped contract text plus
  `shasum` on the fixture. Adversary answered: a cold sitting hosting an approved groom legitimately
  writes `identity.md` and would fail byte-identity though no *drift* occurred — **widened**: the
  byte-identity clause is scoped to a cold sitting with no approved groom, and a second clause requires
  every `identity.md` change to trace to an approved line in that groom's diff with `groomed:` moved.
  **(5) `[ship-verifiable]` `partner: none`, at rest** — property: the contract states what the sitting
  **owes** and states nothing about what it **reads**. At-rest prose grep only (A6 — build 2 ships no
  actor that reads the rule; the first-partnerless-note check is entered on **build 3's** ledger): the
  paragraph sits directly after *Ending a sitting*, names all five obligations, and a **negative** grep
  for `@import` / `SessionStart` / `hook` / `CLAUDE.md` returns only the mechanism-free sentence.
  Adversary answered: a paragraph naming all five **and** a mechanism passes a presence-only check
  while breaking build 3's additive landing — hence the negative grep. **(6) `[ship-verifiable]`
  Handshake** — property: every consumer acks `@15`, none `@14`, and no prose still cites `@14`.
  `package-lint` Group E clean on the A/B/C/E run **and** `grep -rn "frontmatter@14"` over
  `skills/ tools/ .claude-plugin/` = 0. Adversary answered: Group E passes while three prompt literals
  inside `vlt-lint-full.js` still read `@14` — it checks acks, not prose; not hypothetical, since those
  literals moved `:297/:299` → `:321/:323` under build 1 unnoticed until this brief re-ground them.
  **(7) `[field-contingent]` Q14 Researcher pilot** — event: **five completed Researcher dives on
  `{field-vault}` after the flip** (the commit setting `memory: reflexes` in the Researcher's
  `identity.md`); performed by the owner in ordinary use; `{field-vault}` only (no other vault has a
  Researcher history). Measure: distinct external source domains per dive from each note's `sources:`,
  vault-internal entries excluded, **delegate runs excluded** (build 3, same release). **Baseline
  derived at brief time per A14 (ii)** — the five most recent dives, counts and dates only:
  **33 · 6 · 1 · 31 · 16** (`sources:` entries 57 · 13 · 5 · 42 · 28; dates 2026-09-09 ×3, 2026-09-14
  ×2), median 16, mean 17.4, range 1–33, derived from the 46 `research (researcher)` `{log}` lines
  across the live log and its `{archive}` mirror. One derivation correction on record: the fifth-newest
  such line is a *correction* entry with no note and is excluded. ⚠ **The depth-match A14 (ii) asks for
  is not derivable** — research notes persist no `depth:` field (`vlt-research/SKILL.md:27` is an
  in-flight choice nothing writes down); `sources:` entry count is recorded as the stated stand-in and
  is weak (correlated with domain count by construction). Given the 1–33 spread, **a before/after
  comparison on the mean is not a result this pilot can honestly claim** — the protocol is that a human
  depth-matches by reading the questions and grades matched pairs only. Watch, never gate; a null
  result relocates the cause to `vlt-research`'s search discipline. **(8) `[field-contingent]` Under
  the bound** — event: the owner authors a `## Charter` for an over-budget partner and runs
  `vlt-groom <partner>` to completion, accepting the identity-to-card migration; performed by the
  owner on `{field-vault}`; that partner's `activation_words` falls below 12,000 and the denominated
  count drops by one. **Explicitly not a gate and explicitly not (1)'s claim** (A16) — three partners
  are over the day the wire lands and only owner-run, invoked-only, approval-gated grooms bring them
  under. Build 2's ST-9 contribution is (7), watch not gate: the Researcher sits at 9,293 words, so Q8
  does not touch the ST-9 pressure at all.
- [ ] **build-3 (carrier-and-tenants, briefed 2026-09-17):** brief
  `factory/cycles/16-closed-loops/briefs/build-3-carrier-and-tenants.md`. **Eight checks — six
  `[ship-verifiable]` (GATE), two `[field-contingent]`.** `specimens: 7/7` — `S-4`'s six probe rows
  (the per-kind attachment records) become check (1)'s instrument and A16-7's one minimal triggering
  fragment (`references/consult.md:63`) is the site F11 edits; **two classes preserved no set at all
  and no stand-in is synthesized** — A16-6's belief half (the filing's own recovery grep over nine
  `identity.md` files returned **zero** — E7) and A16-7's cost claim (no instrument persists task
  closes across sittings — E8); both are watches below. **R1 n/a** (every rule ships with its
  mechanism; R1's own rule text landed in build 2 at `vlt-upgrade/SKILL.md:72`). **Retirement
  SUBSTANTIVE — five retirements, one deliberate survival:** the lite-boot *"no rule-card or contract
  read"* exemption (`vlt-consult.js:143` + `references/consult.md:9`, D-5 symmetric); the seeded
  `CLAUDE.md`'s *"read it before writing anything"* pointer at the 67,844-char contract
  (`vlt-setup/SKILL.md:206-207`); the engine's copy of the `needs-work`→relay routing rule
  (`vlt-consult.js:152` → a pointer); rule-card `:30` *"a partner consults, or it cites"* → *"consults,
  cites, or delegates a bounded dive"*; the word *Researcher* in Creative `:37`'s remedy (A19).
  **Deliberate survival:** `conventions/consult.md:23-27`/`:36` and `consult@1` — delegate narrows no
  population, it fills an empty cell. **R4 substantive** — the new shipped asset `vlt-delegate.js`
  widens the workflow enumeration at `vlt-setup/SKILL.md:171-173`; the skill-asset manifest needs none
  (structural walk). **This build is the release build — v0.19.0, carrying builds 2+3** (A10).
  **Promise does NOT narrow** (A5 ii): the harvest reached all six probed kinds; the two blank cells
  are measurements not taken, carried as check (1)'s residual. **(1) `[ship-verifiable]` Carrier** —
  property: in every kind the harvest names reached, a partnerless session at the vault root has a card
  canary and a rung canary in context at turn one, **once not twice**. Instrument:
  `fixtures/build-3-carrier-probe/` — the `S-4` harness re-pointed at a vault provisioned by the
  **shipped** `vlt-setup` §3 text, graded on the runtime's **attachment record** (+ passphrase
  corroboration), legs: `claude -p`, in-session summon, Agent-tool subagent, workflow-`agent()`
  subagent. Adversary answered with two widenings: a **second leg over a pre-existing `CLAUDE.md` that
  already references the contract** (F2's re-keyed offer must fire — the old key never would), and
  *once-not-twice* asserted on the record so a double delivery cannot pass. **(2) `[ship-verifiable]`
  Delegate** — property: one runner (zero on `deep`), at most one attested note, no wiki write, the
  caller keeps the wheel and owns the sitting's single session note, and the record can neither rot
  open nor accumulate. Instrument: `fixtures/build-3-delegate-vault/` end-to-end through the shipped
  engine with a **pre-written oracle**, five legs (thin→`insufficient-context`; `deep`→`too-big` with
  **zero** spawns; real quick→`done`; forced-null over a **pre-planted `.WIP.md`**→`incomplete`;
  unreadable op→degraded); failable against v0.18.1. Adversary answered with one widening: the single
  session note's **`partner:` must equal the caller** — a count-only check passes in a world where the
  runner writes the caller's note. **(3) `[ship-verifiable]` Sibling** — property: delegate is a
  neighbour, not a variant. Instrument: byte-compare `conventions/consult.md:23-27`/`:36` against
  `HEAD~`, `package-lint` Group E for both acks, and the grep-negative pattern list. Adversary answered:
  the grep ships with a **positive control** against a planted sentence — a silent pass is
  indistinguishable from a broken pattern list. **(4) `[ship-verifiable]` Lane** — property: no shipped
  sentence names `{research}` single-writer or routes a non-Researcher away; the four replacement
  sentences are present and the census renders. Instrument: greps (contract `:263`, rung seed line
  against `:229`'s copy falsifier, Creative `:37` — *Researcher* absent / *Librarian* + *surfaced to
  the user* present, contract `:331`) + `--web-census` against `fixtures/build-3-web-census/`'s
  pre-written oracle, gate accepting the line and **rejecting an off-by-one**. Adversary answered with
  one widening: the check is written as a **negative over the shipped surface**, not only a positive
  for the new sentences. **(5) `[ship-verifiable]` Decay** — property: a `delegate:` block enters the
  decay table in the act that creates it. Instrument: the shipped `vlt-vitals.py` reports a non-zero
  `oldest_drainable_section_days` on a closed dated `delegate:` fixture and the **pre-build** reader
  reports `0` on the identical fixture; four sites agree by grep. Adversary: a list-only assertion
  passes while the classifier still files the header as `other` (two edits, ~25 lines apart — the A11
  (i) failure); executing the reader closes it. No remaining passing-violating state found. **(6)
  `[ship-verifiable]` Rung line reaches an installed vault** — property: exactly one line, once, never
  over the cap. Event: the owner's **next `vlt-upgrade` of `{field-vault}` to v0.19.0** (bounded —
  scheduled by this release). Graded on: the line inserted once; a **second run inserts nothing**;
  `migrations_run` carries `rung-lane-pointer`; under `cap_words:`; at cap a human-gated offer + a
  recorded skip, never edit-one-out. Adversary answered with one widening: the **second run is part of
  the check** — non-idempotency only appears there. **(7) `[field-contingent]` First live delegate** —
  event: the first `delegate:` block written in `{field-vault}` by a **non-Researcher** partner in an
  ordinary sitting; performed by the owner; graded on block shape, both `{log}` lines caller-tagged,
  the note attested, the caller's single session note, and D7's outcome — **the dive returned inside
  one sitting**. Carries the E7 watch in its weakest honest form (*a partner that formerly declined now
  runs, delegates, or cites*). Unbounded; watch, never gate. **(8) `[field-contingent]` First
  partnerless note** — carried from build 2 by A6 (build 2 shipped the posture, build 3 the carriage).
  Event: the owner works a partnerless sitting in `{field-vault}` and writes its note; graded on exactly
  one note stamped `partner: none`, one `(none)` `{log}` entry, **zero** bytes under `{partners}`, no
  dispatch-slice read, and that the sitting opened with the card and rung in context. Unbounded; watch.
---

<details>
<summary>Superseded routing — 2026-09-09, `inbox-capture`</summary>

**Next lifecycle move (2026-09-09, `inbox-capture`): owner-steered ideation — run `ideation-scaffold`
("scaffold ideation") to lay the rulings skeleton for A16-1..A16-5, then the owner rules grouping,
order, and scope (the lint pair vs the partner triple; one `frontmatter@14` bump; `S-4` bound or not),
then `roadmap-roundtable` before any brief. `S-4` is `proposed` and must be run or ruled before A16-3's
direction 1 is briefed.** — DISCHARGED 2026-09-16 (this run laid the skeleton).

</details>

<details>
<summary>Superseded routing — 2026-09-16, `ideation-scaffold` (skeleton laid; ideation then held)</summary>

**Next lifecycle move (2026-09-16, `ideation-scaffold`): the owner fills the rulings skeleton
above** — `## Ideation rulings — A16-1..A16-5`, laid unfilled this run with 14 seeded questions
(Q1–Q14), 5 cross-filing decide-once slots (D1–D5), the spike view (`S-4` `proposed`, `S-3`
`harvested`/unconsumed), and 6 evidence debts (E1–E6). Build numbering, `binds:`, `spike:` and
`promise:` are placeholders; an unfilled `spike:` or `promise:` blocks `build-brief`, by design.
**Once the rulings are filled: `roadmap-roundtable` ("convene the roundtable") — briefs follow the
review, never precede it.** `S-4` must be run, killed, or ruled-around (the `SessionStart`-hook
fallback) before A16-3's direction 1 is briefed; any spike ruling is written back to its register
file in the same session.

</details>

<details>
<summary>Superseded routing — 2026-09-16, owner hold (cycle opened to further filings)</summary>

**Next lifecycle move (2026-09-16, owner hold): the cycle is OPEN TO FURTHER FILINGS — ideation is
paused, not abandoned.** The rulings skeleton above is laid and unfilled; round 1 was put and not
ruled, by the owner's choice. The route from here:

1. **The owner files what they want to add** into `factory/inbox/` (filing shape:
   `factory/inbox/README.md`). The inbox is **fully captured as of this run** — 62 files, every one
   named in some cycle's `derives_from:` — so anything new is unambiguously the addendum set.
2. **Run `inbox-capture` again** ("run inbox capture"). `factory/CYCLE` reads `16-closed-loops`, so
   it appends to **this** roadmap as an addendum batch (A16-6…) rather than opening Cycle 17 —
   the shape Cycle 10 used three times.
3. **Re-seed this section, do not lay a second one** — extend the batch label past `A16-5`, add the
   addendum's questions, and re-check the cross-filing decide-once slots (D1's one-bump ruling and
   D2's shared `demote` verb are the two most likely to move when filings are added).
4. **Then resume ideation at round 1** (cycle scope, the build cut, build 1), then
   `roadmap-roundtable`, then briefs.

If the owner instead decides to add nothing, the move reverts to **resume ideation at round 1** —
the skeleton is current as it stands.

`S-4` is unaffected and still `proposed`: it must be run, killed, or ruled-around (the
`SessionStart`-hook fallback) before A16-3's direction 1 is briefed, whenever briefing happens.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing, and the roadmap's newest-at-top convention does **not** apply to it. The chat report
is a copy; this line is the obligation.

— DISCHARGED 2026-09-16, later the same day (this `inbox-capture` run captured the addendum set A16-6..A16-8 and re-seeded the skeleton).

</details>

**Next lifecycle move (2026-09-16, `inbox-capture` addendum): resume ideation at round 1 over the
extended batch A16-1..A16-8.** The addendum set is captured (the ST-9 pair A16-6/A16-7 and rail issue
#19 as A16-8) and the rulings skeleton above is **re-seeded, not re-laid**: batch label extended,
Q15–Q21, D6–D8, E7–E8 added, D1/D2 re-checked and unmoved, `S-4` now load-bearing for two entries.
The inbox is again fully captured (64 filings, every one named in some cycle's `derives_from:`), so:

1. **Resume owner-steered ideation at round 1** — cycle scope (all eight, or A16-8 / the ST-9 pair
   leave), the build cut (the grouping question now spans the lint pair, the ST-8 triple, the ST-9
   pair, and the one-line rename), build 1. Then the pre-ideation questions Q1–Q21, the decide-once
   slots D1–D8, spikes, and evidence debts E1–E8. Not `ideation-scaffold` — the skeleton is current.
2. **`S-4` must be run, killed, or ruled-around** (the `SessionStart`-hook fallback) **before either
   A16-3 direction 1 or A16-7 is briefed**; any spike ruling is written back to its register file in
   the same session.
3. **Once the rulings are filled: `roadmap-roundtable`** ("convene the roundtable") — briefs follow
   the review, never precede it.

If the owner files more before resuming, `inbox-capture` runs again and extends this batch the same
way (A16-9…); the skeleton is re-seeded again, never re-laid.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing, and the roadmap's newest-at-top convention does **not** apply to it. The chat report
is a copy; this line is the obligation.

---

**Next lifecycle move (2026-09-16, ideation round 1 ruled): continue owner-steered ideation at round 2 —
release shape, then the pre-ideation questions Q1–Q21, the decide-once slots D1–D8, the `S-4`
disposition (run / kill / rule-around via the `SessionStart` hook — written back to its register file),
and the evidence debts E1–E8.** Round 1 is on record in §Grouping & order: cycle scope all eight; three
builds (1 at-rest fixes, 2 partner-memory schema with the single `frontmatter@15` bump, 3 the carrier +
delegate + lane); `spike:` ruled on every build (`none`, `none`, `S-4`); every `promise:` filled by the
owner at ruling time. `binds:` rosters are laid as clerk reconstructions awaiting owner confirmation.
Once the remaining slots are ruled: **`roadmap-roundtable`** ("convene the roundtable") — briefs follow
the review, never precede it.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing.

---

**Next lifecycle move (2026-09-16, ideation FILLED): `roadmap-roundtable` — "convene the roundtable".**
Every slot in §Ideation rulings is ruled: cycle scope (all eight), three builds with `binds:`/`spike:`/
`promise:` all filled, release shape (one release, conditional on `S-4` harvested before build 3 is
briefed), `S-4` RUN (register written back), `S-3` carried again, no new spikes, Q1–Q21, D1–D8, E1–E8,
and the brief-time parks. Two obligations sit outside the roundtable and are not gated by it:
**run `S-4`** (one session, the register's timebox) before build 3's brief; and the owner's five owed
candidate filings (E6). Briefs follow the roundtable, never precede it; build 1 and build 2 are
briefable on the review's amendments alone.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing.

---

**Next lifecycle move (2026-09-16, `roadmap-roundtable`): `brief build 1` (`build-brief`).** The
Roundtable review record is in place (§Roundtable review — A16-1..A16-8, above the ledger): 19
amendments applied in-section with `(roundtable A#)` markers, R1 declared with its home, D9 added to
§Cross-filing, 11 owner rulings live, **0 open disputes**. Build 1 is briefable now and, per A10, is
**its own release** (v0.18.x — clerk's read v0.18.1) so that Cycle 15's build-2 (6) warm-release
watch gets its chance; its brief must honour the A9/A10 constraint (no `PAGE_SCAN` or scanner-
convention edit) and carry its CHANGELOG notice text in a §8 stub. Build 2 is briefable on the
amendments alone; build 3's brief waits on the **S-4 harvest** (register corrected this session —
the workflow-`agent()` kind is its own row). Builds 2 + 3 ship as one release (v0.19.0), **held whole
until S-4 is harvested — no split**. Outside the roundtable: run `S-4`; file the four
capture-don't-interrupt items to `factory/inbox/` (tripwire single-owner schema; `## Thread` size
bound; `vlt-lint-full.js:297` conditional; strip-promise conditional); the owner's six owed
candidate filings (E6, now including E1's).

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing.

---

**Next lifecycle move (2026-09-16, `build-brief` build 1): a fresh builder session implements
`briefs/build-1-own-writes-read-back.md` via `bmad-workflow-builder`.** The Readiness gate passed on the
roundtable record (0 open disputes, `promise:` filled, `spike: none`, E1–E3 dispositioned); every site was
re-grounded at `601b09b` (= `v0.18.0` bytes); one grounding correction is on record under Q3 (the
`lint-page-facts.py` parser premise — build 1 adds it) and one site was added (`module-help.csv:17`). The
ledger carries build-1's six checks (five ship-verifiable, one field-contingent watch; `specimens: 56/61`).
**Builder's exit obligations:** rewrite the brief's `status:` to a BUILT record with numbered deviations;
delete any `.decision-log.md`; one commit for the build on `cycle16-v0.18.1`; then `vlt-release` for
**v0.18.1 (build 1 alone — A10)**, with the brief's §Release notice text landing in `CHANGELOG.md`. After
the release: **brief build 2** (`build-brief`, briefable on the amendments alone); build 3 waits on the
**S-4 harvest**. Outside the lifecycle: run `S-4`; the four capture-don't-interrupt filings; the owner's
six owed candidate filings (E6).

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing.

---

**Next lifecycle move (2026-09-16, `bmad-workflow-builder` build 1): run `vlt-release` for v0.18.1 — build 1
alone (A10).** Build 1 is BUILT on branch `cycle16-v0.18.1` (one commit; the brief's `status:` carries the
BUILT record with its verification results and three numbered deviations — a Cycle 15 oracle extended, a
Cycle 15 harness literal moved, and two wording adjustments forced by `package-lint` C/E). Warm-safety proven at
rest: `scanFingerprint` `fe29c6f398d02c6b1cdf` on both trees, the three scanner-read conventions byte-identical
to `v0.18.0`, `PAGE_SCAN`/`pageScanPrompt`/`SCANNER_CONVENTIONS` untouched, `scanModel` default unchanged (now
`:207`). The release lands the brief's §Release notice text in `CHANGELOG.md` (`vlt-release` stage 3), bumps
both version strings, runs `package-lint --expect-version 0.18.1`, ff-merges, tags, pushes. After the release:
**brief build 2** (`build-brief`, briefable on the amendments alone); build 3 waits on the **S-4 harvest**.
Acceptance for build 1 (ledger row 1: five ship-verifiable + one watch) discharges on the owner's `vlt-upgrade`
to 0.18.1 + the first post-upgrade full sweep (`acceptance-discharge`). Outside the lifecycle: run `S-4`; the
four capture-don't-interrupt filings; the owner's six owed candidate filings (E6).

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing.

---

**Next lifecycle move (2026-09-16, `vlt-release` v0.18.1): live acceptance for build 1 — the owner runs
`vlt-upgrade` to 0.18.1 on the field vault and one ordinary post-upgrade full sweep; then `acceptance-discharge`
over ledger row 1 (five ship-verifiable + one watch), including the E2 census recount by an independent `awk`
instrument and Cycle 15 build-2 (6)'s warm `lint_cache:` line — a cold line after this upgrade is a finding.**
v0.18.1 shipped at `4fd8049`, annotated tag `v0.18.1`, pushed to origin (main + tag); `package-lint: A/B/C/E PASS,
D PASS — vlt 0.18.1`. In parallel, factory-side: **brief build 2** (`build-brief`, briefable on the roundtable
amendments alone); build 3 waits on the **S-4 harvest**; run `S-4`; the four capture-don't-interrupt filings; the
owner's six owed candidate filings (E6). Memory sync: the `vlt-cycle-16-roadmap` topic records the ship.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing.
  **Addendum — 2026-09-16, same day, from the field sweep (`vlt-core`, relayed by the vault session).** The
  post-upgrade full sweep ran and **Cycle 15 build-2 (6)'s warm-cache watch FAILED: `files_cached: 0` — 0 of
  144 records reused, 152 scans where ~20 were due.** Two things follow, and they point in opposite directions:
  - **v0.18.1 is exonerated, by field evidence independent of this factory's at-rest proof.** The vault
    confirmed all three scanner-read convention digests matched the sidecar's stored components, `scan_model`
    unchanged (haiku), and `pageScanPrompt` + `PAGE_SCAN` byte-identical across 0.18.0/0.18.1 (`md5`
    `e54b7990…` / `2b84caff…`). Check **(5)'s at-rest half stands** — the release moved no cache-key input,
    proven now on both sides of the seam. What it does **not** get to claim is the watch: **A9/A10 spent
    Cycle 15 build-2 (6)'s one warm chance, and the chance was lost to something else.**
  - **The something else is a spec gap, filed as rail issue #20** (`github.com/mggower/bmad-module-vlt/issues/20`;
    the vault withdrew its `factory/inbox/` copy — it carried no `origin:` header, so an accepted #20 would have
    materialized a second filing. The issue is the only copy; `factory/inbox/` and `factory/CYCLE` are untouched).
    **Grounded against module source this run, and it is one notch worse than the filing states:**
    `full-scale.md` step 2 pins `convention_digests` to *"the first **16 hex characters**, lowercase"*; step 1
    gives `pageHashes` an instrument and **no form** — and explicitly licenses a *different tool*
    (*"`shasum -a 256` … is the expected instrument, but the rule names a property, not a tool"*). So the
    divergence is not merely truncated-vs-untruncated: two conformant executors may legally use **different
    digest algorithms** for the first term of `runKey` (`vlt-lint-full.js:427`,
    `${pageHashes[slug]}|${scanFingerprint}|${rulesetFingerprint}`). Field proof: stored `8410d5ed45c6b19c` vs
    this run's instrument output `8410d5ed45c6b19c7f5fa80c…`; after truncating to 16 and re-running, **132 of 152
    matched.** Pinning the *tool* would therefore not fix it and would contradict the contract's instrument rule —
    **pinning the form is the only fix**, which is why the suggested hardening (refuse an entry failing
    `/^[0-9a-f]{16}$/` at the pre-dispatch gate that already refuses wrong-typed slots by name) sits at the
    reader, the one place the two executors meet.
  - **Why it needs a build, not a doc edit:** no instrument catches it. `files_checked: 152 / files_cached: 0` is
    a legal rendering, and a 100% `page_bytes` miss reads as *"the whole wiki changed"* because step 5 renders the
    cold reason from the other two terms. The workflow's own comment at `:420` claims *"two conformant executors
    cannot disagree about it"* — of the **third** term. The first term is exactly where they can.
  - **Lineage:** the residue of Cycle 14's *"the findings cache cannot round-trip"* filing, which fixed the record
    shape and `rulesetFingerprint`'s algorithm, specified the key as `${pageHashes[slug]}|${cache_fingerprint}`,
    and never pinned the first term's form. Step 3's parenthetical already defers the whole-derivation executable
    *"gated on the pageHashes digest-form filing"* — **#20 is that filing.** Issue #13 touches `pageHashes` only
    as payload bulk, not its form. **Routes to the next `inbox-capture` via `issue-triage`; nothing in this
    cycle's ledger is re-graded on it.**

  **Discharge pass 2 — 2026-09-16, evening (`acceptance-discharge`, the completed post-upgrade full sweep;
  report `_agent/lint-reports/2026-09-16-1827-lint.yaml`, vault commit `23430dc`).** The sweep landed clean —
  0 orphans, 0 missing targets, 0 index drift, 0 frontmatter drift, 0 review_due, 0 thin pages,
  `scanner_return_rejected 0 of 152`, governance clean, all 10 conventions carrying `version:`+`consumers:`.
  **Row 1 still does NOT tick — and now for a harder reason than pass 1:** its last open sub-clause closed,
  and a discharged one reversed. **Net: (1)(3)(4)(5)(F1) DISCHARGED · (2) FAILED (gates).**
  - **(5) E2 census — DISCHARGED 2026-09-16.** The recount **matched on three independent instruments**:
    the persisted `bare_path_sources: "240 entries across 83 of 152 pages — sources: scalars unquoted and
    ending .md (instrument: scripts/lint-page-facts.py --census)"`; the vault's `awk` pass over each
    `{wiki}` page's frontmatter block (one-liner recorded verbatim in the filing relay and in the vault's
    report); and the persist gate's own walk, `census {N: 240, P: 83, M: 152}`, `status ok`, 78 schema keys,
    no extra keys. Exactly the A9 baseline. **(5) is now discharged whole** — its at-rest half held in pass 1,
    its field half here.
  - **(2) Census — REVERSED to FAILED 2026-09-16 (owner-ruled at pass 2).** Its property has three clauses;
    clause 1 held twice over (above), clause 3 is not yet observable, and **clause 2 — *"no per-page finding
    is raised for the form"* — was contradicted on the sweep's only target page.** `dutch-oven-braising`
    satisfied the byte gate (`bareSources = 1`) and the verdict test (`unclassified`) and still landed in
    `flag_for_human.malformed_frontmatter`, because build-1's **disposition 3** needs
    `frontmatter_defect_fields == ['sources']` and the page's record — **served from cache, written
    2026-09-03 by a pre-build-1 scanner** — carries `[]`. `frontmatter_defect_fields` is **not a `runKey`
    term** (`vlt-lint-full.js:427`), so records written before the field existed survive the build that
    began depending on it. **On any warm cache, disposition 3 is inert for exactly the pages it was built
    to refuse.** It passes at rest forever — a fixture's scanner returns are fresh by construction — which
    is the **Cycle 12 `b2(5)` lesson in a new place**, and the reason the grade is FAILED rather than a
    separate defect filed around an intact check. **(2) is `[ship-verifiable]`, so this GATES cycle
    closeout:** row 1 cannot tick, and Cycle 16 cannot close on it, until a fix ships and re-discharges.
    Filed with a complete specimen manifest as
    `factory/inbox/2026-09-16-185500-a-reduce-predicate-keyed-on-a-new-scanner-return-field-is-inert-on-every-cached-record.md`
    (1/1 target named; 5/5 sidecar records with non-empty `frontmatter_defect_fields` named with values —
    all five `missing_required`, so **disposition 3's live population in the sidecar is empty**; both
    triggering fragments quoted). **The module named its own blind spot** — the report's `coverage_caps`
    carries the whole diagnosis, so the defect arrived loud, not silent. The vault evicted
    `dutch-oven-braising` (a one-page remedy, not a fix).
  - **Cycle 15 build-2 (6)'s warm watch stays FAILED (owner-ruled).** The vault re-ran the sweep under a
    hand-applied 16-char truncation and got the round trip the watch wanted — `files_cached 132 of 152`,
    `cache_rejected 0`, `cache_miss_terms {page_bytes: 12, scan_surface: 0, ruleset: 0}`, all 12 genuine
    churn, `coverage_caps` empty. **It does not discharge the watch:** the shipped surface still cannot
    round-trip, and the workaround was a human hand applied outside it. Its value is as **evidence for
    #20's fix** — the mechanism demonstrably works the moment the digest form is pinned. (Cycle 15 is
    closed; its roadmap is not appended to either way.)
  - **#20 updated** with this factory's grounding refinement (the instrument-licensing clause and the
    `vlt-lint-full.js:420` site, appended to `provenance_guess`; nothing rewritten).
  - **Two standing items are the vault's, not this ledger's:** the undisposed `researcher`/`brief`
    `weight_mismatch`, and 8 `para_writer_unauthorized` under `areas/career/charter.md`.


---

**Next lifecycle move (2026-09-16, `acceptance-discharge` pass 1): re-run `acceptance-discharge` once the
first post-upgrade full sweep lands on `{field-vault}` — one sub-clause is open, `(5)`'s E2 census recount.**
Pass 1 ran on upgrade evidence alone (`vlt-core` 0.18.0 → 0.18.1, `[2026-09-16 17:43]`; the newest lint report
is `2026-09-15-1134`, pre-upgrade). Ledger row 1 is **SPLIT and stays unchecked**: (1) stub read, (2) census,
(3) writer, (4) slot, (5)'s at-rest warm-safety half and the (F1) wearer watch are **DISCHARGED** — every
at-rest instrument re-run independently in the discharge run (stub harness 8/8, census harness all
expectations, grep-negatives, fingerprint `fe29c6f398d02c6b1cdf`), and (F1)'s named event fired five minutes
after the upgrade (`2fd4a01` renamed two wearers' profiles and cut the parentheticals). What the sweep must
carry on the next pass:

1. **(5) E2 census recount** — the persisted `bare_path_sources:` line vs an independent `awk` recount over
   each `{wiki}` page's frontmatter block, the one-liner recorded verbatim (A9 baseline `240 entries across 83
   of 152 pages`). **Trigger: the owner's agent, sweep in flight.**
2. **~~Riding the same sweep~~ — ANSWERED the same day, see the addendum above the ledger foot:** Cycle 15
   build-2 (6)'s warm `lint_cache:` line came back **COLD — 0 of 144 records reused, 152 scans**. Filed by the
   vault as rail **issue #20** (not `factory/inbox/` — the vault's session withdrew its inbox copy so an accepted
   #20 materializes exactly one filing at `issue-triage`). **v0.18.1 is exonerated by independent field evidence.**
   Nothing here is re-graded on it.
3. **(1)'s field render** — `stub_discovery: section located: yes` on the field index — is confirmatory, not
   gating: (1) is ship-verifiable and already discharged.

**Two owner items, neither blocking the sweep:** (a) the call the BUILT record deferred to check (3) — whether
a mismatch fix is a *substantive edit* for `fix-and-file.md:7`/`:18`, unruled; (b) **ruled this run:** the two filings whose
own clauses have all passed — `2026-09-03-124500-…` (A16-1, check (1)) and `2026-09-09-184840-…` (A16-8,
checks (4)+(F1)) — are **archived to `filings/`** on the owner's call (an ordinary archive, not an early
release: neither carries an open clause). `2026-09-03-124600-…` (A16-2) stays in `factory/inbox/` — check
(5)'s census half is its own clause.

**New this evening, routing to the next capture, not to this ledger:** rail **issue #20** (`pageHashes` has no
specified digest form — the field cause of the cold sweep, grounded against module source in the addendum above).
It needs a build, not a doc edit, and it is the residue Cycle 14's cache filing left behind; `issue-triage` admits
it and `inbox-capture` routes it. **Do not re-grade check (5) on it** — the release is exonerated.

In parallel, factory-side, unchanged by this run: **brief build 2** (`build-brief`, briefable on the roundtable
amendments alone); build 3 waits on the **S-4 harvest**; run `S-4`; the four capture-don't-interrupt filings;
the owner's six owed candidate filings (E6).

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing. The chat report is a copy; this line is the obligation.

---

**Next lifecycle move (2026-09-16, `acceptance-discharge` pass 2): brief a build for the two cache-key
defects — rail issue #20 and filing `2026-09-16-185500-…` — because check (2) is now a GATING FAIL and
Cycle 16 cannot close until it re-discharges.** The post-upgrade full sweep landed clean
(`_agent/lint-reports/2026-09-16-1827-lint.yaml`, vault commit `23430dc`) and closed row 1's last open
sub-clause — **(5)'s E2 census recount MATCHED on three independent instruments**, `240 entries across 83 of
152 pages`. But the same sweep reversed a discharged check. **Row 1 stands at (1)(3)(4)(5)(F1) DISCHARGED ·
(2) FAILED, and stays unchecked.**

1. **The gating fail — (2) Census, clause 2.** Build-1's disposition 3 is **inert on any cached scanner
   record**: it needs `frontmatter_defect_fields == ['sources']`, and `frontmatter_defect_fields` is not a
   `runKey` term (`vlt-lint-full.js:427`), so pre-build-1 records survive the build that began depending on
   them. It passes at rest forever and does nothing in the field wherever cache reuse is highest. Filed with
   a complete specimen manifest; routes to the next `inbox-capture`.
2. **Its sibling — rail issue #20.** Same family (a term the key does not cover). **Sequence them together:
   fixing #20 makes the disposition-3 defect *more* likely, not less** — warm sweeps are the point of the
   cache, and the predicate is inert in proportion to cache reuse. This vault's current exposure is zero
   only because #20's cold sweep re-derived every record; that is an accident resting on a bug.
3. **Worth an owner call at capture:** whether the class — *a reduce predicate depending on a scanner-return
   field is inert unless a cache-key term covers it or a migration runs* — earns a study-register entry
   (`ST-N`). Two instances surfaced the same day.
4. **Unchanged and still owed:** the owner call under (3) (is a mismatch fix a *substantive edit* for
   `fix-and-file.md:7`/`:18`); **brief build 2** (`build-brief`, briefable on the roundtable amendments
   alone); build 3 waits on the **S-4 harvest**; run `S-4`; the four capture-don't-interrupt filings; the
   owner's six owed candidate filings (E6).
5. **Not this ledger's:** Cycle 15 build-2 (6)'s warm watch stays FAILED (the 132/152 round trip ran under a
   hand workaround, not the shipped surface — its value is evidence for #20's fix). The vault's own two
   standing items — the undisposed `researcher`/`brief` `weight_mismatch` and 8 `para_writer_unauthorized`
   under `areas/career/charter.md` — are the vault's.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing. The chat report is a copy; this line is the obligation.

---

**Next lifecycle move (2026-09-16, `inbox-capture` — DEFERRED by owner ruling): unchanged from pass 2 —
`brief build 2` (`build-brief`). The two cache-key defects do NOT enter this cycle.** Owner ruling, this
session: rail issue **#20** (`pageHashes` has no specified digest form) and filing
**`2026-09-16-185500`** (a reduce predicate keyed on a new scanner-return field is inert on every cached
record) are **deferred to Cycle 17**, and **capture itself is deferred until Cycle 16 wraps** — no Cycle 17
roadmap is opened yet, `factory/CYCLE` still reads `16-closed-loops`, and neither filing is folded anywhere.
Both sit un-captured in `factory/inbox/`.

- **What did happen this run:** the GitHub intake leg ran before the ruling — **#20 is materialized** to
  `factory/inbox/2026-09-16-221715-state-the-digest-form-for-pagehashes-an-unspecified-key-term-silently-runs-every-full-lint-cold.md`
  and carries the `captured` label on the tracker. **Materialization is not capture** (`github-intake.md` §4:
  *"the filing is raw field signal; materialization does not ground it"*) — the filing waits in the inbox like
  any other. Triage grounding is on the issue thread; every claim verified, no corrections.
- **Routing fork exercised:** neither filing is marked `channel: platform`, and the boundary was re-derived,
  not trusted — both fix sites (`skills/vlt-lint/references/full-scale.md`,
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js`) are shipped surface. Both are cycle-roadmap channel
  when they are captured.
- **The consequence to hold onto:** build-1 check **(2) stays FAILED and still GATES this cycle's closeout**,
  and its fix now rides **Cycle 17**. So Cycle 16 closes carrying **(2) as a bound inherited debt bound to
  Cycle 17** — the mechanism this factory has retired four times running (B8-2(4), B10-2(5)/B10-12(6), and
  Cycle 14's two, all on their bounds). `cycle-closeout` must record it that way, tagged **ship-verifiable so
  it gates**, which is the A4-4(5) lesson applied preemptively.
- **Owed platform candidate (unfiled, surfaced here so it is not lost):** the **capture boundary has no row
  for a partially-shipped cycle.** Discovery's ship-day rule says a cycle that has cut a release is closed to
  capture; P-4's mid-cycle addendum says an open cycle folds into unbuilt builds only. Ruling A10's
  two-release shape put Cycle 16 in both states at once, and the owner had to rule the boundary by hand. Same
  family as Cycle 13's *"closeout's Stage 4 has no row for two open cycles."* Joins the owner's owed candidate
  set (E6).
- **`build-brief` for the cache-key build is BLOCKED and correctly so** — its Readiness gate needs an ideation
  ruling naming the build, a roundtable record, a filled `promise:` and a `spike:` field, and none exist until
  Cycle 17 captures and ideates. The route is `inbox-capture` once Cycle 16 wraps, not a brief now.
- **Unchanged and still owed:** the owner call under check (3) (is a mismatch fix a *substantive edit* for
  `fix-and-file.md:7`/`:18`); **brief build 2**; build 3 waits on the **S-4 harvest**; run `S-4`; the four
  capture-don't-interrupt filings; the owner's owed candidate filings (E6, now including the boundary gap
  above).

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing. The chat report is a copy; this line is the obligation.

---

### Routing — historical record (superseded by the stamp at the foot of this file)

**Next lifecycle move (2026-09-17, `build-brief` — build 2 BRIEFED): a fresh builder session
implements `factory/cycles/16-closed-loops/briefs/build-2-partner-memory-schema.md` via
`bmad-workflow-builder`.** The brief's `status:` line states the builder's exit obligations: rewrite
`status:` to a BUILT record with numbered deliberate deviations, delete any `.decision-log.md` left on
disk, **one commit for the build**, on `cycle16-v0.19.0`. Ideation is not re-opened.

- **What landed this run.** Build 2's brief — 17 F-sites, 8 brief-time dispositions, Registration (the
  ten-consumer `frontmatter@14` → `@15` walk + the `module-help.csv` `vlt-groom` row + package-lint
  C6's rule-card re-derive), 13 at-rest verification items, the §8 CHANGELOG notice text (A17), and 8
  acceptance checks **appended to the Deferred acceptance ledger above** (6 ship-verifiable GATE, 2
  field-contingent; `specimens: 13/15`).
- **Readiness gate passed on all five clauses:** ideation ruled build 2 (rounds 1 and 4); the
  roundtable covers the batch with **no OPEN disputes**; `promise:` is filled (and is carried verbatim
  into the brief's `title:`); `spike: none` — ruled with the cut, so nothing waits on `S-4` here; E4
  DISCHARGED and E5 ACCEPTED-not-blocking.
- **Seven grounding corrections issued**, each recorded twice (inline in the brief, and as superseding
  notes in §*Grounding corrections — build-2 brief* above): the `vlt-lint-full.js` `@14` literals moved
  `:297/:299` → `:321/:323` (+ a third at `:946`) under build 1; contract `:154`/`:159` → `:155`/`:156`;
  contract `:312` → `:316`; `vlt-consult.js:141` → `:143`; `vlt-setup:215` → `:217`;
  `partner-agent-template.md:111` → `:112`; and **D9/R1 name the wrong `vlt-upgrade` steps** — the
  additive-write class belongs in **Step 3 item 5** (the migration list) and R1's rule in **Step 3
  item 4**, not Steps 4/5. **Step numbers only; no ruling is contradicted and no re-ruling is owed.**
  Two grounding **additions** widen the A18 count-word sweep (`groom-pass.md:9`,
  `vlt-setup/SKILL.md:225`).
- **A14 (ii)'s brief-time obligation is discharged:** the Q14 pilot baseline is derived (five dives —
  **33 · 6 · 1 · 31 · 16** distinct external source domains; median 16, range 1–33) and recorded in the
  ledger row, counts and dates only. ⚠ It surfaced a gap the plan assumed away: **research notes
  persist no `depth:` field**, so the depth-matching A14 (ii) asks for is not derivable from the record.
  The brief states the stand-in, states that it is weak, and rules the pilot ungradeable on a mean —
  matched pairs only, by a human. *That research notes record no depth is a candidate filing the owner
  has not written.*
- **Unchanged and still owed:** the owner call under build-1 check (3) (is a mismatch fix a
  *substantive edit* for `fix-and-file.md:7`/`:18`); **build 3 waits on the `S-4` harvest** — run
  `S-4`; the four capture-don't-interrupt filings (now five — add *research notes persist no `depth:`
  field*, surfaced above); the owner's owed candidate filings (E6, including the
  partially-shipped-cycle capture-boundary gap). Build-1 check **(2) stays FAILED and still GATES
  closeout**, bound to Cycle 17.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing. The chat report is a copy; this line is the obligation.

### Routing — historical record (superseded by the stamp at the foot of this file)

**Next lifecycle move (2026-09-17, `S-4` harvested) — SPENT, demoted 2026-09-17 by the build-3 brief.**

**`S-4` is HARVESTED, `verdict: proceed`. Build 3's spike gate is open — next move: `brief build 3`
(`build-brief`).** Harvest artifact:
`factory/cycles/16-closed-loops/spike-s-4-claude-md-imports-2026-09-17.md`; the register entry
`factory/platform/spikes/S-4-vault-claude-md-imports-per-session-kind.md` reads `harvested` and is the
pointer, not a copy. Build 2 is **BUILT** (2026-09-17, `6ab70b0`) — the earlier stamp routing a builder
session at build 2 is spent and demoted above. Under A10's no-split release, builds 2+3 ship together
as the single **v0.19.0**; nothing releases until build 3 is built.

- **What the spike found.** `@path` imports in a vault-root `CLAUDE.md` load for **every** session kind
  probed — interactive, headless `claude -p`, a summon inside a session, an Agent-tool subagent, a
  **workflow-`agent()` subagent** (the engine `vlt-consult.js:160` calls, which A16-7's delegate runner
  inherits), and a session whose cwd is a vault subdirectory. Imports are transitive and resolve from the
  vault root. A `CLAUDE.md` pointer **without** `@` loaded in none of them. Evidence is the runtime's own
  startup attachment record, not a model's self-report. **A16-3 direction 1 is grounded.**
- **Two findings build 3 must carry, not just the green.** (i) The `SessionStart` hook — the filing's
  fallback carriage — fires once per **CLI session start** and **not** for an in-session subagent spawn,
  so it misses exactly the kind the delegate runner is; imports reach it. The fallback is the weaker
  carrier and should not be chosen. (ii) **No size or depth ceiling was measured.** "Imports load" is not
  "imports load without bound" — the budget question is A16-4's, and build 3 may not assume it away.
  The artifact records both limits, plus the two rows it could not probe.
- **Unchanged and still owed** (carried verbatim from the demoted stamp): the owner call under build-1
  check (3) (is a mismatch fix a *substantive edit* for `fix-and-file.md:7`/`:18`); the five
  capture-don't-interrupt filings (incl. *research notes persist no `depth:` field*); the owner's owed
  candidate filings (E6, incl. the partially-shipped-cycle capture-boundary gap); **capture stays
  DEFERRED to Cycle 17** by owner ruling. Build-1 check **(2) stays FAILED and still GATES closeout**,
  bound to Cycle 17.

*(This block was the routing of record until the build-3 brief; the stamp below supersedes it.)*


## Next lifecycle move (2026-09-17, `build-brief` — build 3 BRIEFED) — authoritative

**A fresh builder session implements `factory/cycles/16-closed-loops/briefs/build-3-carrier-and-tenants.md`
via `bmad-workflow-builder`.** The brief's `status:` line states the builder's exit obligations: rewrite
`status:` to a BUILT record with numbered deliberate deviations, delete any `.decision-log.md` left on
disk, **one commit for the build**, on `cycle16-v0.19.0`. **Build 3 is the RELEASE build** — its §8
carries the dual version bump to **v0.19.0**, the `--expect-version 0.19.0` gate, and the CHANGELOG
collation of build 2's notice text (A17). Ideation is not re-opened.

- **What landed this run.** Build 3's brief — 18 F-sites in three parts (the carrier, the delegate
  mechanism, the lane), 13 brief-time dispositions, Registration (no new skill and **no new
  `module-help.csv` row** — a mode, not a skill; one new workflow asset with its `depends_on` header;
  package-lint **C6** owed for the contract edit, **E4/R2 not owed**), 15 at-rest verification items,
  §8 release + notice text, and **8 acceptance checks appended to the Deferred acceptance ledger**
  (6 ship-verifiable GATE, 2 field-contingent; `specimens: 7/7` with two classes honestly at zero).
- **Readiness gate passed on all five clauses:** ideation ruled build 3 (rounds 1 and 5); the
  roundtable covers the batch with **no OPEN disputes**; `promise:` is filled and is carried into the
  brief's `title:` **without narrowing** (A5 (ii) — the harvest reached all six probed kinds); `spike:
  S-4` reads **harvested** and is now stamped **`consumed`** in its register file with build 3 appended
  to `consumed_by:`; E7 and E8 both ACCEPTED-not-blocking.
- **Five grounding corrections issued**, each recorded twice (inline in the brief, and as superseding
  notes in §*Grounding corrections — build-3 brief* above): `conventions/consult.md:29–32` → `:29–31`;
  contract `:226` → `:229`, `:318` → `:331`, `:314` → `:324`; `vlt-consult.js:138` → `:143` and
  `:147` → `:152`. **No ruling is contradicted and no re-ruling is owed** — Q18's premise is confirmed
  exactly (the rule-bearing lines sit outside the edit, so `consult@1` does not bump).
- **One correction has scope consequences, and it is the reason the carrier would otherwise have
  reached nobody.** `vlt-setup/SKILL.md:218`'s additive offer is keyed on *"if it doesn't already
  reference the contract"* — a test **every installed vault already passes**, so the import lines would
  have shipped to new vaults only. F2 re-keys the offer on the import lines' own absence, and
  Acceptance (1)'s second leg tests exactly that path.
- **Unchanged and still owed:** the owner call under build-1 check (3) (is a mismatch fix a
  *substantive edit* for `fix-and-file.md:7`/`:18`); the five capture-don't-interrupt filings (incl.
  *research notes persist no `depth:` field*); the owner's owed candidate filings (E6, incl. the
  partially-shipped-cycle capture-boundary gap); **capture stays DEFERRED to Cycle 17** by owner
  ruling. Build-1 check **(2) stays FAILED and still GATES closeout**, bound to Cycle 17.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing, and nothing follows it. The chat report is a copy; this line is the obligation.
