---
title: 'Cycle 16 — closed loops'
status: 'open — captured 2026-09-09 (five filings, grounded at v0.18.0 @ `1e119a4`); awaiting owner-steered ideation'
module_code: 'vlt'
created: '2026-09-09'
updated: '2026-09-09'
derives_from:
  - 'factory/inbox/2026-09-03-124500-stub-heading-is-stated-inside-a-fence-so-a-faithful-section-scan-reads-located-no.md'
  - 'factory/inbox/2026-09-03-124600-lint-sources-reconciliation-writes-the-retired-bare-path-form.md'
  - 'factory/inbox/2026-09-09-160000-governance-has-no-partnerless-carrier.md'
  - 'factory/inbox/2026-09-09-160100-always-read-partner-memory-has-no-budget.md'
  - 'factory/inbox/2026-09-09-160200-partner-identity-has-no-owner-side-author-or-reset.md'
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
  the writer reading itself.
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

**Not a fifth study.** `ST-8` holds the partner-side cause in full and is cited, not re-derived.
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

## Routed away from this cycle — the platform fork

**No filing was marked `channel: platform`, and none is factory-side by re-derivation.** All five name
fix sites under the shipped surface (`skills/vlt-lint/references/`, the governance bundle's conventions
and contract, `skills/vlt-setup/`, `skills/vlt-groom/`, `skills/vlt-setup/assets/hooks/vlt-vitals.py`).
A16-1's convention-side fixture lands in this cycle's `fixtures/` — cycle side. The fork ran and found
nothing; `platform_routed` is empty.

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

## GitHub intake — this run's record

Transport `mggower/bmad-module-vlt` (`feedback_repo.default`, `module.yaml:74`); `gh` present and
authenticated. Query (`--label vault-accepted --state open`) returned six issues — #1, #6, #7, #11,
#17, #18 — **all already `captured`** and all carrying an `origin:` header on disk (#1/#6/#7/#11 in the
inbox under their cycles' captures; #17/#18 held on Cycle 15's build-6 (5)/build-7 (5)). Nothing
materialized; no label drift. Amendment sweep (`captured` + `amended`): none. Stale-shape gate: not
reached (no untriaged body). `issues_materialized` is empty by exercise, not by skip. The same-day
`issue-triage` run found the untriaged queue empty and the only off-rail traffic the owner's pinned
#9.

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

## Deferred acceptance ledger

*(Populated per build at brief time — `build-brief` appends each build's live-acceptance checks here,
tagged ship-verifiable or field-contingent.)*

---

**Next lifecycle move (2026-09-09, `inbox-capture`): owner-steered ideation — run `ideation-scaffold`
("scaffold ideation") to lay the rulings skeleton for A16-1..A16-5, then the owner rules grouping,
order, and scope (the lint pair vs the partner triple; one `frontmatter@14` bump; `S-4` bound or not),
then `roadmap-roundtable` before any brief. `S-4` is `proposed` and must be run or ruled before A16-3's
direction 1 is briefed.**

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing, and the roadmap's newest-at-top convention does **not** apply to it. The chat report
is a copy; this line is the obligation.
