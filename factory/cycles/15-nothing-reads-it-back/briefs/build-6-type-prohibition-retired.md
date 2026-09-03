---
title: 'Build #6 — retire the PARA `type:` prohibition: after this ships, a vault owner who types a file accurately is no longer told to retype or move it — the declared `type:` is judged on whether it is recognized vocabulary, the module''s or the vault''s declared, rather than on which folder the file sits in, and `{wiki}` stops being a named exception to that'
status: 'BRIEFED 2026-09-02 — build via bmad-workflow-builder in a fresh session (headless brief; eleven dispositions recorded inline, none owner-ruled; the cycle''s FIRST retirement brief, authored under the roundtable''s R2 interim posture). The builder rewrites this line to a BUILT record — `BUILT <date> — <what landed>; <verification result>. Deviations/notes: (1) … (2) …` with numbered deliberate deviations (the `build-15-spec-convention.md` precedent) — deletes any `.decision-log.md`, and makes ONE commit for the build on `cycle15-v0.18.0`. Not the release build — no version bump; the `extraction` 9 → 10 handshake bump and its four re-acks land in this commit.'
module_code: 'vlt'
created: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md (A15-12 — `class: supersession`, the loop''s first; Half 1 the rule at `extraction.md:84` + `checks.md:19` case (b); Half 2 the shipped nets + declare-at-birth; the two non-negotiable halves D5.1/D5.2; tracker #17; cites `ST-2`)'
  - 'factory/cycles/14-no-enforcement-point/roadmap.md §Carried forward past Cycle 14 item 11 (Cycle 14 build-3 (6) — the two parks'' unwind, BOUND DEBT, clauses (a)+(c); split in place at this cycle''s roundtable, D-D/A18) and item 13 (the routing of both supersessions to this cycle)'
  - 'factory/cycles/14-no-enforcement-point/briefs/build-6-declared-typed-subtree.md (WITHDRAWN 2026-09-01, retained unbuilt as a worked negative — its grounding is reused, its shape (a subtree qualifier, the `{wiki}` unification cut out) is what this build must NOT ship)'
roadmap: 'factory/cycles/15-nothing-reads-it-back/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-01/02): build-6 bullet (binds D5, Q9, E2, + handshake (R1)); D5 all five halves adopted (D5.1 `para_type_unknown` NOT retired; D5.2 the `{wiki}` carve-out retires in the same act) and D5.2 as amended (A5 — the TYPE-LEGALITY carve-out retires, the Layer-2 population/container exclusion does not); Q9 as resolved (A18, owner ruling D-D — Cycle 14 build-3 (6) split in place, the at-rest half GATES here, build-7 carries none); E2 attached (the `_output/` provenance read, done — see disposition 10); A1/R1 the `handshake:` line (`extraction` 9 → 10, four re-acks, Group E bipartite); A6 the recognized set STATED and the promise re-ratified on recognized vocabulary; A20 the obsolescence-beat retirement list for build-6; §Cycle 14 carries — dispositions (carry 6 RELEASED here by reason); build-2''s grounding correction (iii) — `pin_vector` dropped from the cache key.'
risk: 'moderate — `extraction.md` moves a RULE (`version: 9 → 10`; four consumers re-ack in the same commit: vlt-extract, vlt-lint, vlt-track, vlt-query — package-lint Group E is the check); the operating contract is edited (`:66`, one word) so the rule card is RE-DERIVED and its `derived_from: sha256:` re-stamped (package-lint C6); `frontmatter.md` takes a prose re-noun with NO bump (A1) — but it is a scanner-read convention, so its byte change moves `convention_digests[frontmatter]` and this build is a v0.18.0 cold mover in its own right (grounding correction 1); `checks.md:19` is co-edited by build-5 (disjoint spans — see §Boundaries); no workflow asset moves.'
---

# Build #6 — retire the PARA `type:` prohibition

**Promise (owner-ratified 2026-09-02, re-ratified at the roundtable A6, carried verbatim):** *After
this ships, a vault owner who types a file accurately is no longer told to retype or move it — the
declared `type:` is judged on whether it is **recognized vocabulary, the module's or the vault's
declared,** rather than on which folder the file sits in, and `{wiki}` stops being a named exception
to that.*

This is the loop's **first retirement build**. `extraction.md:84` (`version: 9`, Cycle 14 build-3's
own text, `e42429d`) closes the PARA `type:` set and then carves one class of value *out* of a route
it otherwise accepts: a vault may declare an invented word (`dispatch-brief`) as overlay schema and be
conformant, but a vault using the module's own accurate word (`research` for a dated, single-pass,
`trust: raw` snapshot — `extraction.md:28-30`) is *"a mis-typed or mis-placed artifact"* whose only
legal responses are to retype it to something less true or to move it — *"never to declare module
vocabulary as vault-grown overlay schema."* `checks.md:19` restates that as legal-response case (b).
**Accuracy is penalized; invention is accommodated** (the build bullet's grounded inversion). The
mechanism that made the prohibition redundant already ships: the `para_*` nets judge the identical
population in both modes (Cycle 11 build-2, `8290416`), and declare-at-birth is the same enum's own
trusted escape. `ST-2` RC1 names this as the third field of the quartet — `author:`, `trust:` and
`verified_by:` are believed when honest; `type:` is believed only if the folder approves the noun.

**What this build does, precisely — the scope is the ruling (D5, as amended by A5/A6):**

1. **Retires the prohibition** — `extraction.md:84`'s *closed* set, its *"`frontmatter.md`'s list
   does not answer here"* sentence, its *"mis-typed or mis-placed artifact"* verdict on module-canonical
   non-PARA values, and its *"never to declare module vocabulary"* clause; `checks.md:19` legal-response
   case (b); the word *closed* at `vault-operating-contract.md:66` (and, by re-derivation, at
   `vault-rule-card.md:26`); `frontmatter.md:71`'s *"is closed … does not answer for that population"*
   PARA clause.
2. **States the recognized set** (A6): PARA `project | area | resource | moc` ∪ the operational-record
   class `charter | record | register` ∪ overlay-declared schema ∪ **the values `frontmatter.md:71`
   names** (closed by enumeration at that line, open by edit). `para_type_unknown` (D5.1, **kept**)
   fires only on a value in none of the four.
3. **Retires the `{wiki}` type-legality exception in the same act** (D5.2 as A5 named its object):
   after this build no rule text names `{wiki}` as an exception *to the type judgment* — `type: wiki` is
   recognized vocabulary like every other value at `frontmatter.md:71`. The Layer-2 **population /
   container** exclusion is **NOT touched** and this brief records why (disposition 2).
4. **Carries Cycle 14 build-3 (6)'s clauses (a) and (c)** — the at-rest half as the `[ship-verifiable]`
   check that GATES closeout, quoting Cycle 14's bound verbatim (check (4)); the vault-act half
   `[field-contingent]` on the post-upgrade `parked_interims_review:` line (check (5)).
5. **Bumps `extraction` 9 → 10 and re-acks all four consumers in the same commit** (A1/R1); the rule
   card is re-derived (C6); the v0.18.0 `governance_rule_changes` block is a **release-time**
   obligation whose text this brief records (§Release-time obligation).

**Consequence stated so the owner's experience is ruled, not discovered (A6):** the nine
`type: research` files on the field vault's briefs shelf **stop firing on upgrade with no vault act**;
park #15's unwind is a superseding decision-log entry citing v0.18.0, not a retype and not an overlay
declaration — the route park #15 refused on principle.

**All rejected alternatives in the parent filings are settled — do not re-litigate:** the withdrawn
Cycle 14 build-6 (*a declared typed subtree* — a fourth exception, `ST-2` RC2's *"four exceptions, zero
categories"*); the superseded `2026-08-31-152000` filing's carve-out (A15-14, WITHDRAWN at capture);
the overlay route for module vocabulary (park #15 declined it on principle and this build makes it
unnecessary rather than legal); retiring `para_type_unknown` (D5.1 forbids); retiring the Layer-2
population exclusion (A5 forbids — 146 pages would enter four nets); the filing's *"a subtree carries a
`type:`"* mechanism (reading (b) of D5.2 — exists in no shipped artifact, out of scope, a
mechanism-first `candidate` if the owner wants it); folding A15-13 into this build (the filing's own
argument, owner-ratified — build-7 is separate).

## Brief-time dispositions

### 1. The recognized set is stated ONCE, at `extraction.md:84`, with the fourth leg by pointer — never by copying `frontmatter.md:71`'s list *(A6; CLAUDE.md single-home + "lists that claim completeness drift")*

**Ruled: `extraction.md:84` names the four legs; the fourth leg — *the values `frontmatter.md`'s
canonical `type:` list names* — is a pointer to that line, not a second copy of its values.**
`frontmatter.md:71` is *"non-exhaustive … this convention names new values as they appear"*, i.e. it is
the list that grows. Copying its nine values into `extraction.md` would create exactly the two-home
drift Cycle 14 build-5 repaired for the operational-record class (v0.17.1 — two sites, different
members). `checks.md:19`'s reader-only parenthetical, which today re-enumerates three legs, becomes a
pointer to `extraction.md` for the same reason (F2). **Membership is therefore answered at two lines
that each own one thing:** `extraction.md:84` owns the *shape of the union* and the PARA/operational
legs; `frontmatter.md:71` owns the canonical-value list it always owned. Neither restates the other.

**Why the fourth leg exists at all, in the owner's words (A6):** *"Without this, 'retire the
prohibition' leaves the legal response* declare `research` in the overlay *— the route park #15 refused
on principle."* A retirement that leaves the vault's only exit through the door it declined is pass
five with better manners.

### 2. Why the `{wiki}` population exclusion is a ZONE rule and not a TYPE exception — recorded here because A5 asked for it *(D5.2 reading (a); A5)*

**Ruled: the Layer-2 population/container exclusion survives untouched at every site (the table in
disposition 9), and its survival satisfies — does not violate — D5.2's *"four exceptions, zero
categories"*.** The reasoning, so a later reader does not re-open it:

- **It is a statement about who WRITES, not about what a file IS.** `vault-operating-contract.md:64`
  (*"this is the sentence other sites point at"*) removes the `{wiki}` subtree from every PARA
  population *"by name, never as an exception applied inside a check or a resolver"* because it is
  **Librarian-only Layer-2 territory at a `{resources}` address** — a write boundary. The `para_*` nets
  judge Layer-3 files against Layer-3's entry condition (honest `author:`/`trust:`, a recognized
  `type:`, the attestation pair, a `writers:` posture). A wiki page is not a Layer-3 file, whatever
  noun its frontmatter carries; it is judged by the wiki checks. The exclusion is the **category**
  (Layer 2 zone); it is not a name written into the type judgment.
- **Retiring it is not a retirement, it is a regression with a number:** 146 pages enter
  `para_type_unknown` / `para_author_unknown` / `para_status_unknown` / `para_writer_unauthorized`
  (the field vault's count, re-verified this brief: 146 `type: wiki` under the wiki), and
  `para_missing_attestation` double-covers `unattested_write` — the exact duplicate `checks.md:15`
  exclusion (a) was written to remove (*"refusing it removes a duplicate, never a fact"*).
- **The retirement this build DOES make is the one the filing's own argument needs:** after F1, no
  rule text says a `type: wiki` value is legal *solely because* the file sits under `{wiki}`. `wiki` is
  a value `frontmatter.md:71` names; it is recognized vocabulary at any PARA address. The by-name
  removal stops carrying a **type-legality** job it was never written for (that job was an artifact of
  the closure) and keeps the **zone** job it was written for. That is *"the exception retires from the
  type judgment; the population statement is a category"* — D5.2 read (a), the roundtable's ruling.
- **Corollary recorded, not hidden:** a `type: wiki` (or `type: note`, `type: session`, `type: idea`)
  file at a PARA address outside `{wiki}` raises **no** `para_type_unknown` after this build. That is
  the promise as re-ratified — *"the only judge is vocabulary membership"* — and it is by design: a
  Layer-3 file typed with a canonical value is still judged by every other `para_*` net and by
  attestation jurisdiction (`write-verification.md:55` lists `wiki|research|project|area|resource`),
  so honesty is still enforced; only the folder's veto over the noun is gone. Check (3) plants one.

### 3. `para_type_unknown` keeps its job and gets a legal response it can state without lying — the R3 restatement at `checks.md:19` *(D5.1; R3)*

**Ruled: the finding's population and modes are unchanged; its predicate becomes *"a value in none of
the four legs"*; its legal response drops case (b) and reads, at the check's single home:**
**(a)** a **vault-grown** value → declare it as overlay schema in `{overlays}/extraction.overlay.md`
(declare-at-birth, unchanged); **(b)** a value that is a **misspelling or near-miss of a recognized
value** → correct it to the honest recognized value; **(c)** otherwise — the file is **not a PARA
artifact** — relocate it out of PARA. Never auto-fixed (unchanged). The retired case (b)'s two verbs
(*retype to the folder's type* / *relocate to the type's home zone*) do not survive under a new label:
a canonical value is recognized, so the case has no member. A genuinely undeclared value
(`type: banana` at an `{areas}` address — the filing's own example) still lands loud (check (3)).

### 4. `frontmatter.md:71` is a prose re-noun with NO version bump — and it is nevertheless a cold-sweep mover *(A1; grounding correction 1)*

**Ruled: `frontmatter.md` stays at `version: 14`.** The roundtable ruled the re-noun *"prose … with no
bump"* (A1), and the brief agrees on the merits: the rule that moves is `extraction.md`'s (it owns the
set); `frontmatter.md:71`'s PARA clause is a pointer to that home, and a pointer re-nouned from *closed*
to *recognized* changes no rule `frontmatter.md` itself states. Bumping it would walk ten consumers for
a pointer. `last_updated:` moves (it is a date, not a handshake).

**But the bytes move, and `frontmatter` is a scanner-read convention** (`vlt-lint-full.js:290` —
`SCANNER_CONVENTIONS = ['frontmatter', 'wiki-supersession', 'write-verification']`; `full-scale.md`
step 2 digests the merged base + overlay file). So `convention_digests[frontmatter]` changes and every
cached page-scan record is unreusable on the first sweep after v0.18.0 — **from this build, not only
from build-7.** That is correct under D4 (a scanner-read rule's bytes moved) and it changes nothing
the release already states (A2: v0.18.0's first sweep is COLD BY CONSTRUCTION); it corrects the
roadmap's *"on build-7 alone"* sentence and is recorded at the build-6 bullet. The `extraction` bump
itself moves **nothing** in the key — `pin_vector` was dropped (build-2, grounding correction (iii)) and
`extraction` is not a scanner convention. The brief does not claim the bump invalidates the cache.

### 5. The `extraction` 9 → 10 bump is a RULE change, and its roster is exactly four *(A1/R1; CLAUDE.md version-handshake)*

**Ruled: `extraction.md:11` `version: 9 → 10`; `consumers:` at `:12` is unchanged
(`[vlt-extract, vlt-lint, vlt-track, vlt-query]`); every one of the four re-acks `extraction@10` at its
`SKILL.md:4` in the same commit.** Re-grounded this brief: `vlt-extract/SKILL.md:4`, `vlt-lint/SKILL.md:4`,
`vlt-track/SKILL.md:4`, `vlt-query/SKILL.md:4` each carry `extraction@9` today and nothing else in
`skills/` pins `extraction@` (a grep over `skills/`, `.claude-plugin/`, `tools/` returns those four
lines only). **No asset node acks `extraction`** — `vlt-lint-full.js`'s header pins do not include it
and the workflow body carries no `extraction@N` / `extraction vN` literal (E5 and E7 do not engage). The
check of record is **`package-lint` Group E** (E1 bipartite, E3 stray-pin), not a grep (brief-anatomy §7).
Why a rule change and not prose: the line is the convention's appointed home for the answer
(*"this file is its home"*) and the edit moves a shipped check's predicate — the same test Cycle 14
build-5 applied to v8 → v9.

### 6. The recognized set gets NO machine-readable home in this build *(scope; build-5's owed candidate)*

**Ruled: not shipped.** A6 states the set in prose at its convention home; nothing in the rulings asks
for a script, and build-5's foot already owes the inbox a `candidate` — *"the `para_type_unknown` count
leg becomes a one-table extension of `lint-para-facts.py` once build-6's recognized set has a
machine-readable home."* Shipping one here would be a mechanism the roundtable did not review, and the
fourth leg (a pointer to a growing list) is exactly the part a table would have to restate. The
at-rest instrument for the type judgment is therefore an **agent-run reader protocol over a fixture**,
named as such (check (3)), with its expected table hand-written first and proven failable against
the pre-build text.

### 7. The v0.18.0 `governance_rule_changes` block is a release-time obligation; this brief records its text *(A1; `vlt-upgrade/SKILL.md:122`)*

**Ruled: nothing is written to `CHANGELOG.md` in this build.** `vlt-upgrade/SKILL.md:122` renders the
key *"from the module source's `CHANGELOG.md` entries for the versions being crossed … never a diff"*,
and the v0.18.0 entry is authored at release (build-2 §Release owns the entry; build-4 and build-5 each
recorded lines it must carry). The text this build owes it is in §Release-time obligation below, so
the release step copies rather than reconstructs. Also owed there: the CHANGELOG's own v0.17.0 item 2
(*"the PARA recognized `type:` vocabulary is now a closed, named set"*) is **history and is not
edited**; the v0.18.0 block names it as the rule this release retires.

### 8. Cycle 14 build-3 (6) — how the split lands in this ledger *(Q9; A18; owner ruling D-D)*

**Ruled: check (4) is the at-rest half and GATES; check (5) is the vault-act half and is
`[field-contingent]`; both quote Cycle 14's bound; clause (b) is not re-litigated.** What "each park's
recorded blocker claim is demonstrably false against shipped `extraction.md`" resolves to, read at rest
from the field vault's `_agent/mint/decision-log.md` (the entry headed `[2026-08-26] parked-interim —
agent-lane `type:` in the PARA population`, read this brief): the park's blocker is the claim that
*the module ships two conventions answering differently* — `frontmatter.md` non-exhaustive and naming
`research`, `extraction.md` closed and excluding it — *and the bundle does not pick a winner*. Under
shipped v10 both conventions give the same answer (`research` is recognized for the PARA population,
by `extraction.md:84`'s fourth leg and `frontmatter.md:71`'s amended clause), so the claim is false
**at rest**, by reading — no vault act needed to grade it. Clause (c) (*"the vault executes
`para_type_unknown`'s stated legal response … on at least one named file"*) resolves to **no act
owed**: under v10 the nine files raise no finding, so the response is the empty one — graded at rest by
reading the nine files against the shipped rule (counts only, never paths). The *unwind* — the
superseding decision-log entry citing v0.18.0 — is the human's act and is check (5). *"A re-park is not
an unwind"* transfers with the debt: check (5) is not discharged by a third park.

### 9. Retirement (P-15; obsolescence beat A20; R2 interim posture) — SUBSTANTIVE, and the site list is grep-derived

*(This is the cycle's first retirement brief; `brief-anatomy.md` carries no retirement section yet —
[P-24] is queued. The roundtable's R2 interim posture applies: enumerate every restatement and
pointer of the retired rule by grep, a disposition per site, and the population statement that must
NOT move. The roundtable's hand-enumeration (A5) is the floor; the greps ran over
`skills/vlt-setup/assets/governance/_meta/`, `skills/vlt-*/references/`, `skills/vlt-*/SKILL.md`,
`skills/vlt-setup/assets/workflows/`, `skills/vlt-setup/assets/hooks/`, `tools/` and `CHANGELOG.md`
for: `closed set`, `Closed for this population`, `closed PARA`, `closed recognized`, `recognized set`,
`recognized \`type`, `does not answer`, `mis-typed`, `mis-placed`, `retype`, `relocate`,
`declare module vocabulary`, `overlay-declare`, `non-PARA`, `para_type_unknown`, `type: wiki`,
`{wiki}`, `carve-out`.)*

**Found: 6 restatement sites of the retired rule (the roundtable's A5 named 4 — the two it did not
name are the derived rule card and the CHANGELOG's historical record), 17 population/other-rule sites
that must NOT move, 2 sites that survive with unchanged wording.**

| # | Site (re-grounded at `ed0d96b`) | What it says | Disposition |
|---|---|---|---|
| R1 | `extraction.md:84` | the closure (*"from the **closed** set … Closed for this population"*), *"`frontmatter.md`'s … list … does not answer here"*, *"a mis-typed or mis-placed artifact, never unrecognized vocabulary"*, *"never to declare module vocabulary as vault-grown overlay schema"* | **RETIRED — rewritten** (F1). The paragraph keeps its role as the set's home and gains the fourth leg. |
| R2 | `checks.md:19` — `para_type_unknown`'s reader-only enumeration + legal-response case (b) | *"(the artifact types … the operational-record class … and any vault-declared schema …)"*; *"(b) a module-canonical but non-PARA type … retype … or relocate … never overlay-declare module vocabulary"* | **RETIRED** (F2): case (b) deleted; the enumeration becomes a pointer; cases restated per disposition 3. |
| R3 | `frontmatter.md:71` — the PARA clause | *"For the PARA population … the recognized `type:` set is **closed**, and its home is `extraction.md` … this list does not answer for that population and never widens it."* | **RETIRED — re-nouned, no bump** (F3): the set is *recognized*; its home is `extraction.md`; the values named here are members of it by that home's statement. |
| R4 | `vault-operating-contract.md:66` | *"a recognized `type:` (the **closed** PARA recognized set in `extraction.md` …)"* | **RETIRED — one word** (F4): *closed* → *recognized*. Contract edit ⇒ C6. |
| R5 | `vault-rule-card.md:26` (derived) | *"a `type:` in the **closed** PARA recognized set (`extraction.md`)"* | **RETIRED by re-derivation** (F4): the card is re-derived from the edited contract and its `derived_from: sha256:` re-stamped. ⚠ **Not on the roundtable's list** — and C6 would pass a restamped card that still says *closed* (it checks the hash, not the words), which is why the grep manifest covers the card (check (2)). |
| R6 | `CHANGELOG.md` v0.17.0 §Governance rule changes item 2 | *"the PARA recognized **`type:` vocabulary is now a closed, named set** … a `type:` outside the set is no longer silently tolerated"* | **HISTORY — not edited.** The v0.18.0 block names it as the rule retired (§Release-time obligation). |
| P1 | `vault-operating-contract.md:64` | the canonical `{wiki}`-is-not-PARA sentence — *"this is the sentence other sites point at … removed from any PARA population at selection time, by name"* | **DOES NOT MOVE** — the zone rule (disposition 2). |
| P2 | `vault-operating-contract.md:66` (the parenthetical *"the last outside its `{wiki}` subtree, which is not PARA"*) | population | **DOES NOT MOVE** (only the word *closed* later in the line moves). |
| P3 | `vault-operating-contract.md:68` | *"the `{wiki}` subtree removed at population time per Layer 2 above"*; the resolver's *"removed at population time, never by an exception inside the resolver"* | **DOES NOT MOVE.** |
| P4 | `vault-operating-contract.md:70` | *"one carve-out by name: the `{wiki}` subtree under `{resources}` is **never** a container or a container member"* | **DOES NOT MOVE** — container membership is location; the by-name carve-out is the zone. (The filing counts this as one of the singular's four sites; A5 already read it as over — *"three sites over"*.) |
| P5 | `vault-operating-contract.md:41` | the `resources` structure-map row: *"the nested `{wiki}` subtree is not PARA (Layer 2 below is the canonical statement)"* | **DOES NOT MOVE** — a pointer to P1. |
| P6 | `extraction.md:80` | the `resources/` mapping row: *"(the `{wiki}` subtree is not a target folder — the operating contract, Layer 2 …)"* | **DOES NOT MOVE** — extraction-target population. |
| P7 | `extraction.md:86` | *"its `{wiki}` subtree is excluded (the operating contract, Layer 2 …)"* | **DOES NOT MOVE.** |
| P8 | `extraction.md:153` | *"one carve-out answered **by name, not location**: the `{wiki}` subtree under `{resources}`"* (container membership) | **DOES NOT MOVE.** |
| P9 | `checks.md:19` — the population clause | *"with the `{wiki}` subtree under `{resources}` excluded by name, never by location … never PARA artifacts, container members, or `para_*` candidates"* | **DOES NOT MOVE** — the walker's spec (build-5 cites it by pointer; see §Boundaries for the co-edit). |
| P10 | `checks.md:20` | *"`{wiki}` is not in the population (above) and is never handled as an exception here"* | **DOES NOT MOVE** — build-7's line; untouched by this build. |
| P11 | `checks.md:17` | the operational-record carve-out (by artifact class) | **DOES NOT MOVE.** |
| P12 | `full-scale.md:7` step 1 | the `crossLayerSlugs` predicate — *"every directory-valued key except the wiki's own"* | **DOES NOT MOVE.** |
| P13 | `vlt-lint/SKILL.md:35`, `:51` (Step 0) | *"The one exclusion, applied at selection time: drop the `{wiki}` subtree … removed by name at population time, never as an exception inside a check"* | **DOES NOT MOVE.** |
| P14 | `frontmatter.md:175` | the PARA summary's mapping bullet — *"the nested `{wiki}` subtree is not a target folder"* | **DOES NOT MOVE.** |
| P15 | `vlt-query/SKILL.md:48` | *"file it into PARA … (outside the `{wiki}` subtree)"* | **DOES NOT MOVE** — a population pointer. |
| P16 | `write-verification.md:55` | attestation jurisdiction's own enumeration *"`type: wiki\|research\|project\|area\|resource` with `author: agent\|hybrid`"* | **DOES NOT MOVE — a different rule (attestation jurisdiction), build-7's convention.** Observation for build-7's briefer, not this build's: that list names five values and neither `moc` nor any overlay-declared type; it is the sibling completeness-claiming enumeration. Not a `supersession`; a note. |
| P17 | `extraction.md:190`, `:192` | *"the same membership the recognized `type:` set states above"*; *"members of the recognized `type:` set for the PARA population stated above"* | **DOES NOT MOVE** — they already say *recognized*; the operational-record class's membership is unchanged. |
| S1 | `extraction.md:82` | *"named here so it is recognizable schema (`vlt-lint`'s `para_type_unknown` set)"* | **SURVIVES unchanged** — `moc` remains a leg. |
| S2 | `report.md:39` | the slot placeholder *"type 'X' outside the recognized set"* | **SURVIVES unchanged** — already the right noun; the set it names is the union. |

**Population statements that must NOT move, in one sentence:** every site that removes the `{wiki}`
subtree from a PARA population *by name at selection time* (P1–P15) is a zone rule and is untouched;
the property check (3) protects is that the `para_*` population count is **identical before and after**
this build.

**Deliberately NOT retired (D5.1, A5):** `para_type_unknown` itself; the Layer-2 population/container
exclusion. **Retired that the beat named (A20), all present above:** `:84`'s closure, `checks.md:19`
case (b), the `{wiki}` type-legality exception, `:84`'s *"does not answer here"* sentence, the word
*closed* at contract `:66`. **Reverse dependents left standing** — enumerated: P16, P17, S1, S2.

### 10. E2 — the `_output/` provenance read: DONE, before this brief was written *(E2; the build bullet's ⚠)*

**Recorded: `_output/problem-solution-2026-08-25.md` (gitignored, provenance only, 777 lines) was read
in full before any section of this brief was authored.** Nothing from it is quoted here or in any
tracked file, per E2. What the read grounded, stated as this brief's own conclusions: (i) that the
retirement is the right shape — a redundant proxy removed, not a mechanism added — and that a
subtree/exception patch would be the recurrence the study named (disposition 2's reasoning and the
settled-alternatives list rest on it); (ii) that the `{wiki}` Librarian-only zone is a module-fixed
write boundary in every vault and must stay expressed as a population narrowing, never a precedence
statement (disposition 2); (iii) that the retirement of a load-bearing rule should GATE (check (4)'s
tag, which Q9/D-D independently rule); (iv) that the field's two failure directions (falsify or
abandon) are what an honest-value-with-no-legal-destination produces — the reason check (5) grades the
nine files leaving the finding *without being retyped*. The document's own later sequencing and
package proposals are not consumed here; Cycle 12 and this cycle's rulings are the record.

### 11. Grounding corrections at brief time — every cite re-derived against `ed0d96b` (build-5 BRIEFED; builds 1–4 BUILT)

1. **The cache mover (roadmap build-2 bullet, correction (iii) → A2 Ordering note): PARTLY STALE.**
   `~~"build-6 moves `pin_vector` as shipped"~~` is already struck (correct — `pin_vector` is gone); the
   sentence *"v0.18.0 stays COLD BY CONSTRUCTION on build-7 alone"* is now **wrong**: this build edits
   `frontmatter.md:71`'s bytes and `frontmatter` is a `SCANNER_CONVENTIONS` member
   (`vlt-lint-full.js:290`), so `convention_digests[frontmatter]` moves. Two cold movers, one release,
   same A2 outcome. The A1 line at the build-6 bullet (*"The pin move is what invalidates the cache"*)
   is stale for the same reason. Both noted at the roadmap.
2. **The recognized-set restatements: EXPANDED by one.** `vault-rule-card.md:26` restates *closed*
   (derived from contract `:66`); the roundtable's A5 named the contract but not the card. C6's hash
   check does not read the card's words — so the grep manifest does (check (2)).
3. **The filing's four-site count for the singular `{wiki}` carve-out: HOLDS as sites, re-read as
   populations.** `:70`, `:41`, `extraction.md:80`, `:84` — three are zone/container statements (A5:
   *"three sites over"*); only `:84`'s is a type-legality use and it retires.
4. **Field evidence: HOLDS at today's read.** 146 `type: wiki` files under the wiki (plus `index.md`,
   `type: index`, outside the population by the same carve-out); **9** `type: research` files across
   **4** subscription directories on the briefs shelf (the filing said 3 subscriptions at 9 — one more
   directory, same count; counts only, no paths recorded). The PARA population outside `{wiki}`
   otherwise carries `area` 22, `project` 3, `resource` 2, `charter` 1, `record` 1 — every one already
   recognized; the nine are the whole standing finding.
5. **`decision-log.md:1204` (A6's cite for park #15's refusal of the overlay route): line drift in a
   vault record — immaterial.** The park's entry heads at `:1197` today; the refusal sentence sits
   inside it. The brief cites the entry by its heading, never by line.
6. **`checks.md:19` — HOLDS at HEAD** (line 19 of the file at `ed0d96b`: the `para_*` population + the
   two closing nets; case (b) verbatim as the filing quotes). ⚠ Build-5 (BRIEFED, F5) adds pointer text
   to the same line's population clause; the spans are disjoint (§Boundaries).
7. **Consumer roster — HOLDS exactly:** `consumers: [vlt-extract, vlt-lint, vlt-track, vlt-query]` at
   `extraction.md:12`; the four `SKILL.md:4` lines each pin `extraction@9`; no fifth pin anywhere; no
   asset-node pin (disposition 5).
8. **`vlt-upgrade/SKILL.md:124`** (*"Crossing v0.16.0 it renders, at minimum …"*) is the only per-version
   minimum the SKILL states; v0.17.0/v0.17.1 added none — the CHANGELOG is the source. **No SKILL edit
   owed** for v0.18.0 (disposition 7).
9. **`vlt-lint-full.js` carries no `extraction` citation** (a grep for `extraction` finds only the
   words *"pure extraction"* in two comments); E7 has nothing to see here.
10. **The version strings HOLD at `0.17.1`** (`module.yaml:4`, `marketplace.json:16`) — not this build's
    to move.

### Interim posture (R1) — not applicable

Every rule this build changes ships with its mechanism: `para_type_unknown` already runs over the
population in both modes and simply reads a wider set; the handshake, the rule card and the CHANGELOG
block are release-gate mechanics. Nothing is declared ahead of an enforcement point. *(The one absence
— the set has no machine-readable home — predates this build and is owed to the inbox by build-5, not
a rule this build declares; disposition 6.)* `R1: not applicable.`

## Boundaries — stated so the co-editing builders inherit them

- **Build-5 ↔ build-6 on `checks.md:19`.** Build-5 (F5) adds pointer text to the **population clause**
  (the opening of the line, through *"`para_*` candidates"*); build-6 edits the **`para_type_unknown`
  clause** (from *"Two closing nets"* through the end of `para_type_unknown`'s legal response).
  Disjoint spans of one line. Whichever build lands second **re-grounds the line at the other's
  commit** and edits its own span only; neither restates the other's. Build-5 also touches `checks.md:17`,
  `module.yaml`, `report.md`, `full-scale.md`, `SKILL.md` Step 6 — none of which this build edits.
  Build-5's `para_type_unknown` count leg is semantics-free (membership only) and is unaffected by the
  set's widening (build-5 §Boundary).
- **Build-6 ↔ build-7 on `checks.md` and `vlt-lint/SKILL.md:4`.** Build-6 edits `checks.md:19`; build-7
  edits `checks.md:20` (D-E — the one-line `verified_by:` leg change). Build-6 rewrites
  `vlt-lint/SKILL.md:4` to `extraction@10`; build-7 later edits **the same line** to add
  `write-verification@6` (and `vlt-extract/SKILL.md:4` likewise carries both pins — build-7 re-acks
  `write-verification` on a line this build already touched). Build-7 re-grounds both files after this
  commit. File-edit order stands: 2 → 3 → 4 → 6 → 7; build-5 independent.
- **Build-6 ↔ the release.** The v0.18.0 CHANGELOG entry is authored at release (build-2 §Release);
  this brief's §Release-time obligation supplies the `governance_rule_changes` text.

## F-sites

### F1 — `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md` — the home of the set: the closure, the two sentences and the clause retire; the fourth leg enters; `version: 10`

**Current state (re-grounded):** `:4` `last_updated: 2026-08-27`; `:11` `version: 9`; `:12`
`consumers: [vlt-extract, vlt-lint, vlt-track, vlt-query]`; `:84` the paragraph quoted in the Intent —
its operative text, verbatim:

> **The recognized `type:` set for the PARA population — this file is its home.** A file in the `para_*` population (under `{projects}`, `{areas}`, `{resources}`, the `{wiki}` subtree removed by name at selection time — the operating contract, Layer 2) carries a `type:` from the **closed** set: the artifact types `project | area | resource | moc` above, the **operational-record class** `charter | record | register` (*PARA containers* below), and any vault-declared schema in `{overlays}/extraction.overlay.md` (the declare-at-birth rule). **Closed for this population, and this statement is what the operating contract's Layer-3 entry condition points at** for its *recognized `type:`* leg. `frontmatter.md`'s non-exhaustive canonical `type:` list governs the base/agent lane — wiki pages, research notes, sessions, notes, ideas — and **does not answer here**. A module-canonical but **non-PARA** `type:` (`wiki`, `research`, `session`, `note`, `idea`) sitting in a PARA folder is therefore a **mis-typed or mis-placed artifact**, never unrecognized vocabulary: the response is to retype it to the target folder's `type:` per the mapping above, or to relocate it to that type's home zone — never to declare module vocabulary as vault-grown overlay schema.

**The exact change:**

1. `:11` `version: 9` → `version: 10`; `:4` `last_updated:` → `2026-09-02`. `:12` unchanged.
2. `:84` becomes (the builder may tighten wording; every clause below is load-bearing and stays):

> **The recognized `type:` set for the PARA population — this file is its home.** A file in the `para_*` population (under `{projects}`, `{areas}`, `{resources}`, the `{wiki}` subtree removed by name at selection time — the operating contract, Layer 2) carries a `type:` from the **recognized** set, which is the union of four: the artifact types `project | area | resource | moc` above; the **operational-record class** `charter | record | register` (*PARA containers* below); any vault-declared schema in `{overlays}/extraction.overlay.md` (the declare-at-birth rule); and **every value `frontmatter.md`'s canonical `type:` list names** (*Base frontmatter* — that list is the fourth leg's home and is not restated here; it is closed by enumeration at that line and open by edit). **This statement is what the operating contract's Layer-3 entry condition points at** for its *recognized `type:`* leg. Recognition is a judgment about the **value**, never about the folder: a file's `type:` is recognized or it is not, at any PARA address, and a value in none of the four legs is `vlt-lint`'s `para_type_unknown` (the net keeps its job — a genuinely undeclared value lands loud). What a recognized value says about the file's provenance and trust is answered by its own `author:`/`trust:` and its attestation, judged by the honesty nets — a `type:` that is accurate for what the file is (`research` for a dated, single-pass, `trust: raw` snapshot filed at a PARA address; `wiki` for a wiki page) is the right value wherever the file sits, and is never a reason to retype or relocate it. The `{wiki}` subtree's removal from this population (above) is a **zone** fact — Layer 2 is Librarian-only territory — not a statement about the legality of any `type:` value.

3. **Nothing else in the file moves.** `:80` (row parenthetical), `:82` (`moc` — *"`vlt-lint`'s
   `para_type_unknown` set"*), `:86`, `:153`, `:190`, `:192` are population/class statements and stay
   byte-identical (disposition 9, P6–P8, P17, S1). The `status:` enums and the declare-at-birth rule at
   `:120` are untouched.

**Why:** A15-12 Half 1; D5.2 (A5 — the type-legality carve-out retires here: the *"does not answer
here"* sentence and the *"mis-typed or mis-placed"* verdict were the only text making `{wiki}`'s
by-name removal do a type-legality job); A6 (the fourth leg); A1 (rule change ⇒ bump). The *"never to
declare module vocabulary"* clause does not survive under any wording: with the fourth leg in the set,
there is nothing left for it to forbid.

**Out of scope at this site:** `:47`'s named `vlt-track` sanction (the personalized-extraction
allowlist — `ST-2`'s other named exception, not this filing's); `:60`'s human-initiation premise
(Cycle 12 territory); the `status:` enums.

### F2 — `skills/vlt-lint/references/checks.md:19` — `para_type_unknown`'s enumeration becomes a pointer; case (b) retires; the legal response is restated (R3)

**Current state (re-grounded, HEAD line 19; the `para_type_unknown` span):**

> **`para_type_unknown`** — a file in the population carrying a `type:` outside the recognized set — **defined in `{conventions}/extraction.md`, *`type:` mapping by target folder*, which is its single home; named here for the reader only** (the artifact types `project|area|resource|moc`, the operational-record class `charter|record|register`, and any vault-declared schema in `{overlays}/extraction.overlay.md`) — informational for files whose `created` predates convention adoption, loud after. **Legal response,** by which of three cases the value falls in: **(a)** a **vault-grown** type → declare it as overlay schema in `{overlays}/extraction.overlay.md` (declare-at-birth, `{conventions}/extraction.md`); **(b)** a **module-canonical but non-PARA** type (`wiki|research|session|note|idea`) → **retype** to the target folder's `type:` (`{conventions}/extraction.md`, *`type:` mapping by target folder*) **or relocate** the file to that type's home zone — **never overlay-declare module vocabulary**, which would make the vault assert local authorship of a module-level answer; **(c)** otherwise → relocate the file out of PARA.

**The exact change (this span only — the population clause before *"Two closing nets"* and everything
from `para_author_unknown` on are untouched):**

> **`para_type_unknown`** — a file in the population carrying a `type:` outside the recognized set — **defined in `{conventions}/extraction.md`, *`type:` mapping by target folder*, which is its single home and the only place the set's four legs are enumerated; named here for the reader only** (the PARA artifact types, the operational-record class, vault-declared overlay schema, and every value `{conventions}/frontmatter.md`'s canonical `type:` list names — a value in **none** of the four is the finding; recognition is a judgment about the value, never about the folder) — informational for files whose `created` predates convention adoption, loud after. **Legal response,** by which of three cases the value falls in: **(a)** a **vault-grown** type → declare it as overlay schema in `{overlays}/extraction.overlay.md` (declare-at-birth, `{conventions}/extraction.md`); **(b)** a **misspelling or near-miss** of a recognized value → correct it to the honest recognized value; **(c)** otherwise — the file is not a PARA artifact of any recognized kind → relocate it out of PARA. A file whose `type:` is accurate for what it is — a module-canonical value at a PARA address included — is **never** retyped or relocated on this finding's account (v0.18.0; the prior case (b) is retired).

The closing sentence *"Neither net is ever auto-fixed."* stays.

**Why:** A15-12 Half 1 (*"restated at `checks.md:19` as legal-response case (b)"*); R3 — the finding
class's legal response is stated at the check's own single home in the same build; disposition 1
(the enumeration was a second home for the set's members and would have needed a fourth leg copied
in — a pointer instead); disposition 3.

**Boundary:** build-5 adds walker-pointer text to this line's population clause; build-7 edits `:20`.
See §Boundaries.

### F3 — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:71` — the PARA clause re-nouned; `version: 14` unchanged; `last_updated` bumped

**Current state (re-grounded):** `:11` `version: 14`; `:12` `consumers:` (ten, incl. the workflow asset);
`:4` `last_updated: 2026-08-24`; `:71`'s tail, verbatim:

> New artifact classes may introduce new `type:` values without a contract edit, and this convention names new values as they appear — **but that openness is scoped to the base/agent lane.** For the **PARA population** (files under `{projects}`/`{areas}`/`{resources}`, the `{wiki}` subtree removed by name) the recognized `type:` set is **closed**, and its home is `extraction.md`, *`type:` mapping by target folder* — this list does not answer for that population and never widens it.

**The exact change:** the tail from *"— **but that openness …"* becomes:

> New artifact classes may introduce new `type:` values without a contract edit, and this convention names new values as they appear. For the **PARA population** (files under `{projects}`/`{areas}`/`{resources}`, the `{wiki}` subtree removed by name) the recognized `type:` set is stated at its home, `extraction.md`, *`type:` mapping by target folder* — a union of four legs of which **this list is one**: every value named here is recognized there, at any PARA address, and a value this list gains is recognized there on the same edit. This list does not define the other three legs and never restates them.

`:4` `last_updated:` → `2026-09-02`. **`version:` stays 14** (disposition 4). No consumer re-acks
`frontmatter`.

**Why:** A6 (*"`frontmatter.md:71`'s PARA clause amended in the same act"*); A1 (*"prose re-nouns in
`frontmatter.md` with no bump"*). ⚠ **Cold-sweep note for the builder's BUILT record:** this edit moves
`convention_digests[frontmatter]` (disposition 4 / grounding correction 1) — record the digest before
and after in the BUILT status so the release's cold-run statement can cite both movers.

**Out of scope at this site:** `:175` (the PARA summary bullet — a mapping pointer, P14); the
`local_consumers:` / vault-writable-field sections.

### F4 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:66` (one word) and the re-derived `vault-rule-card.md:26` (C6)

**Current state (re-grounded):** contract `:66`, inside the entry condition: *"a recognized `type:`
(the **closed** PARA recognized set in `extraction.md`, *`type:` mapping by target folder*)"*. Rule card
`:26`: *"a `type:` in the **closed** PARA recognized set (`extraction.md`)"*; `derived_from:
'vault-operating-contract.md sha256:8f8a7116…7b9f20 (derived 2026-08-27)'` (the sha matches the shipped
contract today — verified); `last_updated: 2026-08-25`.

**The exact change:**

1. Contract `:66`: *"(the **closed** PARA recognized set in `extraction.md`, …)"* → *"(the **recognized**
   PARA `type:` set stated in `extraction.md`, *`type:` mapping by target folder* — a judgment about the
   value, never the folder)"*. Nothing else on `:66` moves; `:64`, `:68`, `:70`, `:41` are byte-identical
   (P1–P5).
2. Rule card `:26`: *"a `type:` in the **closed** PARA recognized set (`extraction.md`)"* → *"a `type:`
   in the **recognized** PARA set (`extraction.md` — the module's vocabulary or the vault's declared)"*;
   re-stamp `derived_from:` with the edited contract's `sha256` and *(derived 2026-09-02)*; bump
   `last_updated:`. The card must stay under `RULE_CARD_BUDGET` (8000 bytes) — this edit is net ~+30
   bytes.

**Why:** A5 (*"contract `:66`: closed → recognized (a contract edit ⇒ rule-card re-derivation,
package-lint C6)"*); grounding correction 2 (the card is a restatement site in its own right, and C6
checks freshness, not words — check (2)'s grep covers it).

### F5 — the four consumer acks: `skills/vlt-extract/SKILL.md:4`, `skills/vlt-lint/SKILL.md:4`, `skills/vlt-track/SKILL.md:4`, `skills/vlt-query/SKILL.md:4` — `extraction@9` → `extraction@10`

**Current state (re-grounded, each `:4`):**
`vlt-extract`: `["extraction@9", "wiki-supersession@2", "frontmatter@14", "write-verification@5"]`;
`vlt-lint`: `["frontmatter@14", "wiki-index@2", "wiki-supersession@2", "extraction@9", "write-verification@5", "spec@2", "consult@1", "decision-log@4"]`;
`vlt-track`: `["extraction@9", "wiki-supersession@2"]`; `vlt-query`: `["extraction@9", "frontmatter@14"]`.

**The exact change:** `extraction@9` → `extraction@10` in each; no other pin moves (build-7 moves
`write-verification@5 → @6` on two of these lines later — §Boundaries). No body text in any of the four
SKILLs restates the retired rule (grep: `vlt-extract/SKILL.md:58` is folder-choice guidance, not a
type rule; `vlt-query/SKILL.md:47-48` names `type: research` for a `{research}` note and *"outside the
`{wiki}` subtree"* for PARA filing — both unchanged).

**Why:** A1/R1 — the bipartite roster is exactly `extraction.md:12`'s four; disposition 5.

### F6 — `factory/cycles/15-nothing-reads-it-back/fixtures/` — the type-judgment fixture, its hand-written expected table, and the reader protocol (check (3), check (4)'s failability leg)

**NEW, factory-side only (never shipped):**

- `fixtures/build-6-para/` — a minimal PARA tree, every file frontmatter-only plus one line of body,
  placeholder content, no vault-local names:
  - `resources/briefs/sub-a/2026-09-01-090000-issue.md` — `type: research`, `author: agent`,
    `trust: raw`, attested (the shape of the nine field specimens, one representative, scrubbed) →
    **no finding**;
  - `resources/wiki/a-page.md` — `type: wiki` → **outside the population** (excluded by name; the
    count leg);
  - `projects/a-note.md` — `type: wiki` (a canonical value at a PARA address — disposition 2's
    corollary) → **no finding**;
  - `areas/session-log.md` — `type: note` → **no finding** (a fourth-leg value not in the old case (b)
    list's first two);
  - `projects/p/charter.md` — `type: charter` → **no finding** (leg 2);
  - `areas/plan.md` — `type: area` → **no finding** (leg 1);
  - `areas/declared.md` — `type: dispatch-brief` **with** `_agent/conventions/extraction.overlay.md`
    declaring it → **no finding** (leg 3);
  - `resources/undeclared.md` — `type: dispatch-brief` with the overlay **absent** (a second copy of
    the tree, or the harness runs the reader twice — once with the overlay, once without) → **fires**
    (control for leg 3);
  - `resources/banana.md` — `type: banana` → **fires** (the filing's own control);
  - `resources/resourse.md` — `type: resourse` → **fires**, legal response (b) *correct it*.
- `fixtures/build-6-expected-findings.json` — the hand-written oracle: per file, `finding: true|false`
  and, where true, the legal-response case; plus `population: 9` (the ten files minus the wiki page)
  under both overlay states.
- `fixtures/build-6-reader-protocol.md` — the agent-run instrument, named: *given* the shipped
  `checks.md:19` + `extraction.md:84` + `frontmatter.md:71` at a stated commit, and the fixture tree with
  `{projects}`/`{areas}`/`{resources}`/`{wiki}`/`{overlays}` resolved to it, *produce* the finding table
  and the population count; *evidence* is the produced table diffed against the oracle, recorded in the
  brief's BUILT status. **Failability:** the same protocol run against the pre-build text (`ed0d96b`)
  must produce a *different* table — `research`, `wiki`-in-`projects/` and `note` fire under case (b) —
  or the instrument has not been shown to read the rule.

**Why:** brief-anatomy §9 (*"build the instrument from the failure's shape"* — the field specimens are
homogeneous, one representative each is frozen; the nine themselves are read live at rest in check (4));
Cycle 11 roundtable R1 (a ship-verifiable check names its at-rest instrument); disposition 6 (no
script — the protocol is the named instrument).

## Registration

**None** — no new skill, no new workflow, no `module-help.csv` row. **But not free** (brief-anatomy §5):

- **Handshake — a convention RULE changed:** `extraction` **9 → 10**; the consumer walk is the four
  acks in F5, same commit; the check of record is **`package-lint` Group E** (E1 bipartite, E3 stray-pin),
  never a hand grep. No asset node acks `extraction` (E5/E7 do not engage — disposition 5).
- **`package-lint` C6** — the contract edit (F4) requires the rule card re-derived and its
  `derived_from: sha256:` re-stamped; the card stays under `RULE_CARD_BUDGET`.
- **`package-lint` E4** — no new check is added to `package-lint`; no `tools/test-package-lint.py` case
  owed; `CASE_FLOOR` unchanged (24).
- **`frontmatter@14`** — no bump; no walk (disposition 4).

## Out of scope (dispositioned)

- **A subtree-carries-a-`type:` declaration** (the filing's Half 2 (ii) mechanism; D5.2 reading (b)) —
  *rejected for this build*: exists in no shipped artifact; the roundtable routed it to a
  mechanism-first `candidate` filing if the owner wants it. The withdrawn Cycle 14 build-6 brief is the
  worked negative.
- **A machine-readable home for the recognized set** — *deferred*: build-5's owed `candidate`
  (disposition 6).
- **`para_author_unknown`'s closed `human|agent|hybrid`** (Cycle 14 carry 6) — *released with reason
  at the roundtable* (D-F): no filing asks it; the sibling closed enumeration and the next
  `supersession` candidate through the rail build-1 completed. Not touched here.
- **`write-verification.md:55`'s type enumeration** (P16) — *not this build's*: attestation
  jurisdiction, build-7's convention; noted for build-7's briefer.
- **`write-verification.md:47`'s `verified_by` roster closure** (A15-13, park #16, Cycle 14 build-3 (6)
  clause (b)) — *build-7*; clause (b) is not re-litigated (Cycle 14's own record).
- **`extraction.md:47`'s named `vlt-track` sanction** — *out of scope*: `ST-2`'s other named exception
  (the personalized-extraction allowlist); no filing asks it this cycle.
- **`vlt-upgrade/SKILL.md:124`** (the v0.16.0 crossing minimum) — *already covered by*: the CHANGELOG
  source rule at `:122`; no per-version SKILL line is owed (grounding correction 8).
- **`CHANGELOG.md` v0.17.0 item 2** — *history, not edited* (R6); the v0.18.0 block supersedes it by
  name.
- **The field vault's decision log** (park #15's superseding entry) — *the human's act*, check (5); the
  module ships nothing into a vault's log.
- **Re-kinding #17/#18** — *owner's act after build-1*, unchanged.
- **`vlt-agent-*` partner SKILLs** — grep finds no restatement of the type rule in any partner or
  operation SKILL; nothing to edit (the *"partner skill text still carries the old posture"* hazard was
  checked, not assumed).

## Verification (unit, at rest — lifecycle step 5)

1. **Grep manifest — the retirement landed whole (check (2)).** Over `skills/` (all files):
   `Closed for this population`, `closed set`, `closed PARA`, `closed recognized`, `does not answer
   here`, `does not answer for that population`, `mis-typed or mis-placed`, `never to declare module
   vocabulary`, `never overlay-declare`, `module-canonical but non-PARA`, `never widens it` → **0 hits**
   each. Positive: `recognized` appears at `extraction.md:84`, `checks.md:19`, `frontmatter.md:71`,
   contract `:66`, rule card `:26`; `frontmatter.md` named as the fourth leg at `extraction.md:84` and
   `checks.md:19`.
2. **Population sites byte-identical.** `git diff ed0d96b -- <file>` restricted to the P1–P15 lines
   (contract `:41`, `:64`, `:68`, `:70`; `extraction.md:80`, `:86`, `:153`; `checks.md:19`'s population
   clause and `:20`; `full-scale.md:7`; `vlt-lint/SKILL.md:35`, `:51`; `frontmatter.md:175`;
   `vlt-query/SKILL.md:48`) shows **no change** (build-5's pointer edit to `checks.md:19`'s population
   clause, if it has landed, is the one permitted diff and is not this build's).
3. **Handshake — `package-lint` Group E** (E1/E3/E5/E7) clean with `extraction@10` × 4 and no `@9`
   survivor; mid-cycle **A/B/C/E** run PASS. (A grep for `extraction@` is an aid while editing, never the
   recorded verification.)
4. **C6** — rule card re-derived, `derived_from: sha256:` equal to `shasum -a 256` of the edited
   contract, size under 8000 bytes; the card's `:26` says *recognized*.
5. **The fixture (F6).** Oracle hand-written **first**; the reader protocol run over the shipped text
   → table equals the oracle under both overlay states, `population: 9` both times; then run against
   `ed0d96b`'s text → the table differs on `research`/`wiki`-in-`projects/`/`note` (failability
   recorded).
6. **The field vault at rest (check (4)).** From the factory machine, read-only: the nine `type:
   research` files and the population count P, then the rule as shipped applied to the nine → **0**
   `para_type_unknown`; counts only in the BUILT record, no paths. The park entry's blocker claim read
   against v10: false (disposition 8).
7. **Cache-mover record.** `convention_digests[frontmatter]` before/after this build (the SKILL's
   digest instrument, `full-scale.md` step 2) — two values in the BUILT status; `convention_digests`
   for `wiki-supersession` and `write-verification` unchanged by this build.
8. **R3** — the restated legal response is at `checks.md:19` (F2). **R4 — not applicable:** no shipped
   file is added; `fixtures/` is an un-enumerated cycle directory (declared exclusion, the build-1/4/5
   precedent).
9. **Scrub** — no personal or vault-local content in any changed shipped file or fixture; the fixture
   uses placeholder slugs; the BUILT record carries counts, never the field vault's paths.
10. **Decision-log hygiene** — no `.decision-log.md` left in the working tree.

## Release-time obligation (not this build's edit — the release step copies this)

**`CHANGELOG.md` v0.18.0 §Governance rule changes must carry, verbatim or sharpened for what
shipped:**

> **N. `{conventions}/extraction.md` v9 → v10 — the PARA `type:` prohibition is RETIRED.** A file at a PARA address is judged on whether its `type:` is **recognized vocabulary — the module's or the vault's declared** — never on which folder it sits in. The recognized set is the union of the PARA artifact types, the operational-record class, vault-declared overlay schema, and every value `frontmatter.md`'s canonical list names. **What a partner may now do differently:** file an honestly typed document (`type: research` for a dated `trust: raw` snapshot, for one) at a PARA address without retyping it to the folder's noun or relocating it; the instruction *"never declare module vocabulary as vault-grown overlay schema"* is gone because there is nothing left for it to forbid. `vlt-lint`'s `para_type_unknown` is **not** retired — a value declared nowhere still lands loud; its legal response no longer contains *retype or relocate* for an accurate value. **`{wiki}` stops being a named exception to the type judgment** — `type: wiki` is recognized vocabulary like any other; the `{wiki}` subtree's removal from the PARA population is a zone fact (Layer 2, Librarian-only) and is unchanged. **This retires the rule v0.17.0 item 2 introduced** (*"a closed, named set"*), which was reinforced in the very cycle whose thesis was that rules without enforcement points do not bind. The operating contract's Layer-3 entry condition (`:66`) and the rule card say *recognized* where they said *closed*. Four consumer acknowledgments re-pinned (`extraction@10` × 4); `frontmatter.md` stays at v14 (a prose re-noun, no rule of its own moved).

**And the release's cold-run statement (build-2 §Release) names build-6 as a cold mover** —
`frontmatter.md`'s bytes moved — alongside build-7's `write-verification` bytes and build-4's scan
surface.

**And `parked_interims_review:` will render park #15 on the first v0.18.0 upgrade** — the unwind is a
superseding decision-log entry citing v0.18.0, the human's act (check (5)).

## Acceptance (live — appended to the roadmap ledger)

**Five checks — four `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 2/155`
(observed: the filing's two homogeneous sets — 146 `type: wiki` pages under the wiki, 9 `type:
research` files on the briefs shelf (5 → 8 → 9), both re-verified at brief time at 146 / 9; preserved
to this brief: one representative of each shape frozen in `fixtures/build-6-para/`, the nine consumed
live at rest by check (4) as counts on the readable vault; the low ratio is homogeneity, not
attrition — every specimen has the same frontmatter shape as its representative).

**(1) `[ship-verifiable]` — at the release gate and at rest — GATES:** the `extraction` 9 → 10
handshake is bipartite-consistent — instrument: `package-lint` Group E (E1 over `extraction@10` with all
four consumers acked, E3 no stray pin, E5/E7 unengaged and clean), C6 with the rule card re-stamped
against the edited contract and under budget, mid-cycle A/B/C/E PASS and the release's
`--expect-version 0.18.0` PASS line; *property:* every consumer `extraction.md:12` lists acks the
version it carries and nothing acks a version it does not; *adversary:* an in-prose citation of
`extraction v9`/`@9` inside a skill body or the workflow — E7 covers workflow assets only and
`extraction` has no asset consumer — **widened:** verification 3 adds a grep over `skills/` for
`extraction@9` / `extraction v9` / `extraction.md v9` → 0 outside `CHANGELOG.md` history.

**(2) `[ship-verifiable]` — at rest — GATES:** the retirement landed whole and touched nothing it must
not — instrument: verification 1's grep manifest (0 hits for the eleven retired phrases across
`skills/`, **`vault-rule-card.md` included**) and verification 2's byte-identity diff over the fifteen
population sites; *property:* no shipped text names `{wiki}` as an exception to the type judgment, no
shipped text tells a vault to retype or relocate an accurately typed file, and the `para_*` population
definition is unchanged at every site; *adversary:* the prohibition survives paraphrased (e.g. *"must
not overlay-declare"*), or the rule card is restamped with *closed* still in it (C6 passes on the hash)
— **widened:** the manifest lists semantic variants, covers the derived card, and the builder records a
reader pass over each edited paragraph in the BUILT status naming any remaining verb of relocation.

**(3) `[ship-verifiable]` — at rest — GATES:** the type judgment is vocabulary membership, not folder,
and the population count does not move — instrument: the agent-run reader protocol
(`fixtures/build-6-reader-protocol.md`) over `fixtures/build-6-para/` against the hand-written oracle
`build-6-expected-findings.json`: `research`, `wiki`-in-`projects/`, `note`, `charter`, `area` and the
overlay-declared `dispatch-brief` raise **no** `para_type_unknown`; `banana`, `resourse` and the
undeclared `dispatch-brief` **fire** with legal responses (c)/(b)/(a); `population: 9` under both overlay
states (the `type: wiki` page under `{wiki}` excluded by name, counted nowhere); the protocol run against
`ed0d96b`'s text yields a different table (failability); *property (the roundtable's instrument beat,
reconciled — same property):* a PARA-addressed file carrying any module-canonical or vault-declared
`type:` raises no `para_type_unknown` whatever folder it sits in; a value declared nowhere still does;
the `para_*` population count is unchanged before and after; *adversary:* a reader applying the rule
from memory rather than from the shipped text passes the oracle by coincidence — **widened:** the
failability leg requires the same reader to produce the pre-build table from the pre-build text, and
the oracle carries a fourth-leg value (`note`) that no pre-build reading admits.

**(4) `[ship-verifiable]` — at rest — GATES CLOSEOUT (Q9, A18, owner ruling D-D): Cycle 14 build-3
(6), clauses (a) and (c), the at-rest half, quoting Cycle 14's bound verbatim** — *"**The bound, stated so
Cycle 15's closeout can grade it without re-deriving it:** Cycle 15 rules the two retirements at ideation
(see item 13), and the re-check is graded on the **first `parked_interims_review` of the first
`vlt-upgrade` after that release**, against `{field-vault}`'s `_agent/mint/decision-log.md` read at rest.
**Clause (b) is already satisfied in substance and is not re-litigated** — park #16 was re-derived and
superseded in the log; what it lacks is a *legal* exit, which is the retirement's to supply. **Clauses
(a) and (c) are the bound.** ⚠ **A re-park is not an unwind, and a re-park at Cycle 15's bound does not
discharge this** — that distinction is what produced this FAIL and it transfers with the debt."* — the
at-rest half being: (a) park #15's recorded blocker claim (*two conventions answer differently and the
bundle picks no winner; `type: research` is outside `extraction.md`'s closed set*) read from the field
vault's decision log at rest is **demonstrably false against shipped v10 `extraction.md` +
`frontmatter.md:71`** — both name `research` recognized for the PARA population; and (c) the legal
response owed on the nine `type: research` files is the **empty one** — read at rest against the
shipped rule, the nine raise **0** `para_type_unknown`, their count and the population P recorded (counts
only, never paths); instrument: the discharger's read of the decision-log entry and the nine files on
the readable `{field-vault}`, from the factory machine, against the build's commit; *property:* the
parks' blocker no longer exists in shipped text, and its unwind requires writing nothing false;
*adversary:* the count is 0 because the population was mis-derived (the briefs subtree dropped, or a
walk that never saw the nine) — **widened:** the nine are counted **present in P** before the judgment,
and P equals the vault's `para_scan:` on its latest persisted report where one exists; second
adversary: (a) graded on the roadmap's paraphrase of the park rather than the entry — **widened:** the
entry is read from the log itself and its heading recorded. Vault-act half → check (5).

**(5) `[field-contingent]` — Cycle 14 build-3 (6), the vault-act half (D-D), and the filing's own field
half:** event: the **first `vlt-upgrade` to v0.18.0 on `{field-vault}`** — its post-flight
`governance_rule_changes:` renders the v0.18.0 block and `parked_interims_review:` renders park #15;
then the owner writes the **superseding decision-log entry citing v0.18.0** through the rostered write
route (not a third park; not a retype; not an overlay declaration); then a **scoped** `vlt-lint` over
the briefs shelf (the filing's named instrument — the `para_*` nets run in both modes) reports **zero**
`para_type_unknown` with the nine files untouched, **and a control still reporting** (the discharger
plants one scratch file with an undeclared value for the run and removes it after, recorded);
performer: the owner; vault: `{field-vault}` (readable); grades: the entry exists and cites v0.18.0, the
park is no longer live, the scoped run's slot is `[]` with the control's finding present.
**Discharges `factory/inbox/2026-09-01-160000` (A15-12)** — Stage 5 may move it once (1)–(5) are green
(the filing's own ship-verifiable and field halves); tracker **#17** closes on the rail sync.
Unbounded; watch register if unfired — but *"a re-park is not an unwind"* transfers: a third park does
not discharge it.
