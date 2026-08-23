---
title: 'Build #B9-1 — the dispatch-ledger repair: the proto-`deliver` era gets its datum, the key-check exemption is cut to the key requirement on both sites, and the ledger''s denominators gain a factory-side reproducibility instrument (Arc 8''s bound re-check gates this arc''s closeout)'
status: 'BUILT 2026-08-21 — all six F-sites landed: relay.md:28 rewritten (both lanes exemption cut to the key requirement, era datum + no-`deliver` edge stated, key-failing proto membership at point of use), relay.md:41 gains the ref-on-handoff payload sentence, ledger.md:25 narrowed to exclude both lanes + existence-test marker, ledger.md:26 immunity narrowed to "never a key-requirement finding", ledger.md:28 states location vs existence + the lane derivation (era/key-failing clauses by pointer at relay.md) + extension-optional resolution + header/leading-only shape detection, ledger.md:46 verifies by pointer and names the instrument; tools/dispatch-lane-check.py shipped standalone per disposition 1 (NOT the priced package-lint deviation — no E4 case owed, CASE_FLOOR stays 21). Verification: instrument 15 cases / 2 fixtures exit 0; red-then-green probe recorded (flipped pre-era-handoff-ref-is-payload-proto expectation -> exit 1 naming the case; restored -> exit 0); cross-file greps clean (blanket immunities gone; era datum once, relay.md only; "resolving" absent from ledger.md; eligible-for-unrelated-finding phrasing at both F1+F4 sites and nowhere else); uv run tools/test-package-lint.py 21/21 green; package-lint mid-arc A/B/C/E PASS (D skipped, rides B9-4). Acceptance 1 (ship-verifiable, GATES): all seven B8-2 (4) elements discharged at rest. Acceptance 2 (ship-verifiable): A11 delta record stands, shipped F5 text + instrument derivation match the adopted readings. Acceptance 3 field-contingent, awaits the vlt-core v0.12.0 upgrade. Deviations/notes: (1) F1 carries Q4''s wording ("remains eligible to be a finding for any unrelated reason") as the equivalent phrasing of the narrowed immunity; the literal "never a key-requirement finding" sits at F4 — grep-verified agreeing, not restating. (2) The header/pointer-leading-only shape-detection clause shipped as one sentence in ledger.md:28 (disposition 3''s "kept out of shipped text" read as covering the vault-record measurement artifact, not the detection rule the instrument implements — the live ledger run must agree with the checker, so the rule needed a prose home).'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md (A9-6 — Gap 1 era-datum, Gap 2 handoff/`ref`, the capture-added `ledger.md:25`/`:26` precedence conflict, the reproducibility blind spot; carries Arc 8''s bound B8-2 (4) re-check, ship-verifiable from birth, GATES Arc 9 closeout)'
roadmap: 'skills/reports/inbox-evolution-arc9-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-20): build-B9-1 grouping bullet (seven scope items — A19 corrected the header; A12 added item 7); Q4 (exemption scoped to the key requirement, datum = candidate (a), no-`deliver` edge stated — discharges Arc 8''s bound scope question); Q5 (`:26` governs; `:25`''s population narrowed so the overlap ceases to exist); Gap 2 (`ref` on a `handoff` is payload, never the key); the Round-4 `resolving`/`on disk` location-vs-existence ruling (item 5, as amended by A11 — "no denominator moves" STRICKEN, replaced by the measure-both-readings obligation this brief discharges); roundtable A9 (E4 prices a same-build harness case IF the instrument is a package-lint check), A10 (the instrument is factory-side, runnable at rest — a `ledger.md` Verify bullet alone does not satisfy element 6), A12 (`ledger.md:26` narrowed; element (2) names both sites), A19 (D5 is sited in B9-2 — B9-1 is its worked example, not its home). Capture scope question (c): early and small.'
risk: 'low — two reference files in one skill plus one new factory-side tool; no convention `version:` moves, no consumer walk, no governance edit, no release in this build (v0.12.0 rides B9-4); the one hazard is semantic — a narrowing that shifts a live vault''s denominators unmeasured — and the A11 measurement below bounds it at zero'
---

# Build #B9-1 — the dispatch-ledger repair

Arc 8's acceptance check B8-2 (4) FAILED on the first post-0.11.0 `vlt-dispatch ledger` run:
the proto-`deliver` era test names no datum (`relay.md:28`), a `ref` on a `handoff` has no
defined meaning (`relay.md:41`), and — capture's own addition — `ledger.md:25` and
`ledger.md:26` claim the same population one line apart with no precedence, so two readers
obeying shipped text produce different boards. The run reported a clean proto-`deliver` zero
while seven pointers sat in the lane it was denominating, and asked a maintainer to act on
two of them. This build repairs the two reference files so the overlap ceases to exist rather
than being ordered, states the era datum and both tests explicitly, and ships the factory-side
instrument that makes the re-check's `[ship-verifiable]` tag mean something. It carries the
arc's one closeout-gating check.

**Scope is the roadmap's seven items** (build-B9-1 bullet, Rounds 3–4 + roundtable A12 —
A19's warning applies: the bullet's own lead-in once said fewer; the list governs):
(1) narrow `ledger.md:25`'s population; (2) split `relay.md:28`'s dual grant, both lanes;
(3) state the era datum including the no-`deliver` edge; (4) `ref` on a `handoff` is payload,
never the key; (5) state the location-test vs existence-test distinction; (6) build the
reproducibility instrument; (7) narrow `ledger.md:26`'s blanket immunity to mirror (2).

All rejected alternatives in the parent filing and the rulings are settled — do not
re-litigate. In particular: a precedence *sentence* (Q5 chose narrowing), letting `ref` key a
`handoff` (Gap 2 ruled payload), *unifying* the two tests (A11's note: a behavior change with
no filing behind it), and an era-rule expiry (candidate (d) — the lane drains via `vlt-decay`
instead).

**`binds:` roster — reconstructed, and said so per R3.** The roadmap's build-B9-1 bullet
carries no `binds:` line (A19 added rosters to B9-2..B9-7; B9-1's rulings sit inline in its
own scope list). Reconstructed from the rulings that govern this build without naming it:
**Q4, Q5, Gap 2, the Round-4 item-5 ruling, capture scope question (c), roundtable A9, A10,
A11, A12, A19, standing rules R1/R2 (as pricing rules), R5 (§9 tagging), and the pre-seeded
B8-2 (4) ledger entry (seven elements).** D5 is deliberately *not* in the roster (A19: sited
in B9-2). No contradiction with the bullet's text was found.

**Readiness note (A8's pre-brief gate).** Ruling 4c's dated locate-attempt — required
"before B9-1's brief" — is discharged: the 2026-08-21 owner-prompted correction on the
roadmap (Q10/A8 block) recovered all three candidates' subjects from Arc 7's Closeout record
item 8. The gate's ledger entry now binds to those three named subjects; it remains an owner
filing action, bound before v0.12.0 is tagged, and is not this build's scope.

## Brief-time dispositions (headless — each judgment call recorded with its reasoning)

1. **The instrument (item 6) is a standalone factory-side checker under `tools/`, NOT a
   package-lint check: `tools/dispatch-lane-check.py`, fixture records embedded.** *(A10
   rules the home class — factory-side, runnable at rest, "a fixture record plus a checker
   the builder runs against it"; a `ledger.md` Verify bullet alone does not satisfy. A9
   prices the package-lint alternative. The choice between the two at-rest shapes was left
   to the brief.)* Grounding for how E4/R2 apply to this shape: `_e4_harness_coverage`
   derives its check inventory by introspecting **`package-lint.py`'s own module-level
   callables** matching `^(check_|_e\d+_)` (`tools/package-lint.py:794` `_E4_CHECK_NAME_RE`,
   `:829-832` the `globals()` walk) — a script that is its own file under `tools/` is outside
   that inventory, so **no declaring case in `tools/test-package-lint.py` is owed and
   `CASE_FLOOR` (21, `tools/test-package-lint.py:229`) does not move**. R2 binds "any build
   that adds or changes a **release-gate** check" — this checker is not wired into the gate,
   so R2 is not triggered. Why standalone rather than gate-wired: (a) package-lint's contract
   is package self-consistency (groups A–E all read the shipped tree); lane membership is a
   derivation over a *dispatch record*, a different subject — `tools/cost-manifest.py` is the
   precedent for a standalone tracked instrument with its own contract; (b) B9-1 is
   deliberately the arc's smallest build (capture scope question (c)) and A9's mandatory
   same-build harness case is scope this shape does not incur. **Priced deviation path:** if
   the builder instead lands the instrument as a package-lint callable (`check_*` / `_e*_`),
   A9 fires — a declaring case in `tools/test-package-lint.py` plus the `CASE_FLOOR` 21→22
   bump become mandatory in the same build or E4 blocks the tag. Record whichever shape
   shipped in `status:`.

2. **The stated derivation the instrument encodes (lane membership, post-fix).** The lanes
   the denominated lines count, derived per pointer line (the unit — `ledger.md:28`), in this
   order:
   - **path-keyed** — the line carries a key-path: a trailing link (wikilink or plain path)
     whose *written* target sits under the handoff zone (`_agent/handoffs/` or
     `_agent/specs/`). A **location** test — no disk read. Any other wikilink is payload.
   - **legacy pre-shape lane** — un-annotated (no shape in block header or pointer-leading
     annotation) and not path-keyed.
   - **proto-`deliver` lane** — shape-annotated, not path-keyed, block-dated **before the
     era** (the first `deliver` pointer in this record), and **its shape's key requirement is
     unmet as written** (an annotated `handoff` with no key-path; an `ask`/`answer`/`deliver`
     with no `ref`). A shape-annotated pre-era pointer whose key is present needs no
     exemption and is ordinary traffic, not lane traffic.
   - **findings** — every other key-requirement failure (post-era, or any population
     `ledger.md:25` retains after F3's narrowing).
   The key-failing clause in the proto lane is the brief's derivation, not a quoted ruling
   sentence — recorded per headless protocol. It is inside ruled bounds, not a new ruling:
   Q4's text ("exempt from the key check … remains eligible to be a finding for any unrelated
   reason") makes the exemption meaningful only for key-failing traffic, and the Gap-2
   ruling's accepted cost says exactly this population ("**the six pointers stay in the proto
   lane** rather than becoming legal-as-written"). The strict pre-fix sentence licenses the
   broader construction (every annotated pre-era pathless pointer — 27 on the measured
   record, including 19 legitimately `ref`-keyed asks/answers); F1/F5 must therefore say the
   narrower membership explicitly, and the measurement below records both constructions so
   the choice is visible, not smuggled.

3. **The A11 measurement — discharged, computed 2026-08-21 on the primary acceptance vault's
   live dispatch record (read-only; nothing in the vault was touched).** Record shape: 73
   `relay:` blocks, 88 pointer lines (the unit; `consult:`/`daily` out of scope by
   `ledger.md:23`). Era under candidate (a): the first `deliver` pointer is
   **2026-08-18 10:21** (`deliver: career-cluster-wiki-pass` — itself the re-fire of the
   2026-08-17 15:12 unkeyed batched ask, the finding whose repair discharged B8-1 (5)/
   B8-2 (5)).

   | pre-fix denominator | reading: location | reading: existence |
   |---|---|---|
   | path-keyed pointers | 26 | 26 |
   | legacy lane (un-annotated pathless) | **15** | **15** |
   | annotated pathless, pre-era — strict shipped text | **27** | **27** |
   | annotated pathless, pre-era — key-failing construction (disposition 2) | **8** | **8** |
   | annotated pathless, at/after era (`ref`-keyed, ordinary) | 20 | 20 |

   The key-failing 8 = seven `(handoff…)`-annotated header blocks of 2026-08-15 with no
   handoff-zone path at all (six of the seven carry a `ref:` in the header — Gap 2's six,
   which stay in the lane under item 4) + the checked-off 2026-08-17 15:12 unkeyed ask. This
   matches the filing's field count ("seven pointers sat in the lane").

   **Which reading the fix adopts:** `resolving under the handoff zone` (`relay.md:26`,
   `ledger.md:28`) is the **location** test and defines *pathless* — hence both denominators;
   `no path on disk` (`ledger.md:25`) is the **existence** test and defines the annotated-
   `handoff` finding. **Measured delta between the two readings: 0 on every lane.** Not
   vacuous: the readings diverge exactly on a pointer whose written handoff-zone path is
   missing from disk, and the measured record has none — all 22 distinct written zone paths
   resolve **under wikilink semantics (extension-optional: `path` or `path.md`)**. The
   near-miss is real and is why F5 states the resolution rule: a naive existence resolver
   demanding the literal `.md` reads all 22 as missing and swings the lanes by ±22. A
   measurement artifact, kept out of shipped text: the record's prose mentions shape
   annotations inside pointer bodies (e.g. the 15:12 pointer's supersession note quotes
   `(deliver: …)`), so shape detection reads the block header and the pointer-leading
   annotation only — the fixture (F6) encodes this trap.

4. **The no-`deliver` edge ships as one sentence in F1** (Q4: "it must be stated in
   `relay.md:28`, not inferred"): in a record containing no `deliver` pointer at all, every
   shape-annotated pathless key-failing pointer is proto-`deliver` traffic — the feature
   demonstrably never ran in that record. The fixture carries a second record exercising
   exactly this edge.

5. **R1 (interim posture): not applicable.** Every rule this build states ships with its
   instrument in the same build (the checker is element 6; the narrowings are point-of-use
   text in the files `ledger` executes from). Nothing ships ahead of its mechanism; D6's
   test is satisfied by a named bell, no `enforcement_stage: declared` posture is owed.

6. **The denominated line formats do not change.** "N legacy unkeyed pointers (pre-shape)" /
   "N proto-`deliver` pointers (pre-shape)" render exactly as shipped (`ledger.md:26`); this
   build changes membership rules and immunity scope, never the surface a human scans.

## F-sites

*All capture-time sites re-grounded 2026-08-21 against current source: every one HOLDS at
its cited line. Grounding corrections issued: 0 (no superseding notes owed to the roadmap).*

### F1 — `skills/vlt-dispatch/references/relay.md:28` (*Backward compatibility*): split the dual grant; state the datum and its edge

**Current:** one sentence grants the proto lane two things as one — "tolerated as written,
drained normally, exempt from the key check, reported by `ledger` as a denominated count
('N proto-`deliver` pointers (pre-shape)'), **never as a finding**" — and "before `deliver`
existed" is never qualified; the un-annotated legacy lane's grant ("exempt from the key check
and from the idempotency guarantee it never had") has the same over-breadth question (capture:
it applies to **both** lanes).

**Change (scope items 2 and 3):** rewrite the paragraph so that, for **both** lanes:
- the exemption covers the **key requirement only** — a legacy or proto pointer stays exempt
  from the key check, stays a denominated count, and **remains eligible to be a finding for
  any unrelated reason** (Q4's wording; the sentence that, read strictly, would have
  suppressed the B8-1 (5)/B8-2 (5) repair is deleted, not qualified);
- the era datum is stated: "before `deliver` existed" means **before the first `deliver`
  pointer exists in this record** — per-record, derivable at read time, no version knowledge;
- the no-`deliver` edge is stated (disposition 4);
- proto-lane membership is the key-failing construction (disposition 2) — a pre-era
  shape-annotated pathless pointer **whose key is present is ordinary traffic**, in the lane's
  own text, so the strict broader reading dies at the point of use.
Keep unchanged: "Neither lane is ever a legal form to write anew. No existing record is ever
edited to conform." This paragraph stays the single home of lane semantics; `ledger.md:26`
(F4) points here, never restates the datum.

**Why:** A9-6 Gap 1; Q4 discharges Arc 8's bound scope question; element (2) and (3) of the
B8-2 (4) re-check.

### F2 — `skills/vlt-dispatch/references/relay.md:41` (*The idempotency rule*): `ref` on a `handoff` is payload, never the key

**Current:** ":41" states the per-shape key ("a `handoff` keys on its **doc path** exactly as
it always has; an `ask`, `answer`, or `deliver` keys on its **`ref`**") and is silent on a
`ref` supplied *on* a `handoff` — six live pointers change lane on a sentence nobody wrote.

**Change (scope item 4):** one sentence at `:41`, reusing `:26`'s shipped vocabulary: **a
`ref` supplied on a `handoff` is payload, never the key** — the `handoff` keys on its doc
path or, lacking one, fails its key requirement; a `ref` never rescues it. (Why not let it
key: `:41`'s own warning — key ambiguity disables the spam guard invisibly. Accepted cost,
ruled: the six pointers stay in the proto lane and drain via `vlt-decay`.)

**Why:** A9-6 Gap 2; element (4).

### F3 — `skills/vlt-dispatch/references/ledger.md:25` (*Findings*): narrow the population so the overlap ceases to exist

**Current:** "**Findings** — a *shape-annotated* pointer that fails its shape's key
requirement: an `ask`/`answer`/`deliver` with no `ref`, or an annotated `handoff` with no
path on disk." A pre-era annotated pathless `handoff` satisfies this **and** `:26`
simultaneously — the rule conflict capture found.

**Change (scope items 1 and 5):** narrow the population **to exclude both legacy lanes**
(Q5 — elimination, not ordering: a reader who reads only `:25` gets the right answer), e.g.
append the qualifier "— excluding the two legacy lanes below, which are exempt from the key
check (*Backward compatibility*, `references/relay.md`)". And mark the test kind: "no path
**on disk**" is an **existence** test (the written key-path's target is missing), distinct
from the *pathless* **location** test the counting rules define — the F5 sentence is the
distinction's home; `:25` gets the two-word marker and the reader is pointed down.

**Why:** capture-added `:25`/`:26` conflict; elements (1) and (5).

### F4 — `skills/vlt-dispatch/references/ledger.md:26` (*The legacy lines*): narrow the blanket immunity to mirror Q4's split

**Current:** "reported as **counts, never findings**" — verbatim the blanket immunity Q4
struck from `relay.md:28`; leaving it here ships Q4's cure on one file and its disease on the
other, with the diseased file ruled the winner by Q5 (roundtable A12).

**Change (scope item 7):** "counts, never findings" → "counts, **never a key-requirement
finding**" — the lane stays denominated and key-exempt, and remains eligible to be a finding
for any unrelated reason (agreeing with F1's text by pointer, not restatement). Keep the
denominated-zero idiom, the live-record/re-baseline sentence, and both lane names unchanged.
The lane-membership description here stays a **pointer** at `relay.md`'s *Backward
compatibility* (it already is — keep it so; the datum lives only in F1).

**Why:** roundtable A12; element (2) extended to name both sites; element (7).

### F5 — `skills/vlt-dispatch/references/ledger.md:28` (*Counting rules*) and `:46` (*Verify*): state both tests, and the derivation the instrument mirrors

**Current:** `:28` defines the unit and defines *pathless* via "a trailing `→ [[…]]` link (or
plain path) **resolving** under the handoff zone" — `resolving` does double duty (location vs
existence) and reads either way; `:46`'s Verify restates lane membership in the strict
pre-fix construction ("the proto-`deliver` count the pre-`deliver` shape-annotated pathless
pointer lines actually present").

**Change (scope items 5 and 6's prose half):**
- `:28` states the distinction explicitly: *pathless* is a **location** test — the written
  target sits under the handoff zone, no disk read; "no path **on disk**" (`:25`) is an
  **existence** test — the written target is missing from disk. Two tests, both real, said
  once. State the resolution rule for the existence test: wikilink semantics,
  extension-optional (disposition 3's near-miss).
- `:28` carries the lane-membership derivation of disposition 2 (or points at F1's text for
  the era/key-failing clauses and adds only the counting-side half) — one home per clause,
  no duplicated datum.
- `:46`'s Verify bullet is updated to verify **against the counting rules by pointer**
  ("pathless and lane membership per the counting rules above") instead of restating a
  membership sentence that F1 just narrowed — and gains one line naming the factory-side
  instrument as the derivation's fixture-backed check of record
  (`tools/dispatch-lane-check.py`). Per A10 this Verify line is an *auxiliary* surface — it
  does not itself satisfy element (6); the checker does.

**Why:** the Round-4 item-5 ruling (as amended by A11); the reproducibility blind spot A9-6
confirmed (counting rules defined the unit, never membership); keeps `:46` from re-importing
the ambiguity F1 removes.

### F6 — `tools/dispatch-lane-check.py` (new): the reproducibility instrument, fixture + checker, runnable at rest

**Change (scope item 6, per A10):** a new tracked, public, standalone script (stdlib-only,
`uv run tools/dispatch-lane-check.py`, exit 0/1) that:
- embeds (or carries alongside, builder's choice — embedded keeps it one file like the test
  harnesses) **two fixture dispatch records** in the shipped block/pointer grammar, with
  **placeholder slugs and paths only** (`_agent/handoffs/{date}-{owner}-to-{consumer}-{slug}.md`
  style — CLAUDE.md worked-example rule; no vault-local content);
- implements the stated derivation (disposition 2 / F5's text) and asserts each fixture
  pointer's expected lane, exiting non-zero with a named line on any disagreement;
- fixture record 1 covers, at minimum, one pointer per membership class: path-keyed `handoff`
  via extension-less wikilink; annotated `handoff` with a written zone path **missing from
  disk-model** (existence finding — NOT pathless: the location/existence distinction's
  falsifier); un-annotated pathless (legacy lane); pre-era `ask` with `ref` (ordinary — NOT
  proto: the key-failing clause's falsifier); pre-era annotated `handoff` with no path
  (proto); pre-era `ask` with no `ref` (proto); pre-era `handoff` carrying a `ref` and no
  path (proto — `ref` is payload, F2's falsifier); post-era `deliver` with `ref` (ordinary);
  post-era `answer` with no `ref` (finding); a payload wikilink outside the handoff zone
  (never a path); and a pointer whose *body prose* quotes a shape annotation (the header/
  leading-annotation-only trap, disposition 3);
- fixture record 2 contains **no `deliver` pointer at all** and exercises the no-`deliver`
  edge (disposition 4): its annotated pathless key-failing pointers all land proto.
Each fixture case is a case **that could fail** — the gate-2 no-vacuous-discharge ruling
governs; the build's verification records one deliberate red (flip an expected lane, watch it
fail, restore).

**Why:** element (6) — the instrument that makes B8-2 (4)'s `[ship-verifiable]` tag discharge
at rest rather than on a prose re-read; B8-2 (3) verified the counting *unit* and structurally
could not catch *membership*, the half that failed.

## Registration

**None.** No skill is created (R2's registration rule does not fire: no `marketplace.json`
`skills[]` entry, no `module-help.csv` row owed). No convention `version:` moves and no
`consumers:` list changes — the edited files are `vlt-dispatch` reference prose, not
handshaked conventions; `vlt-dispatch`'s own acks (`SKILL.md:3` `depends_on: ["consult@1",
"spec@2", "frontmatter@8"]`) are untouched. R1-pricing of the non-handshake gates: **C6** not
touched (no governance/contract edit — D5 is B9-2's); **E4** not touched under disposition 1
(standalone instrument; the priced deviation path is stated there); **E5** not touched (no
asset-node ack changes). `tools/dispatch-lane-check.py` joins the already-enumerated public
`tools/` release-commit surface (CLAUDE.md, Git & publishing) — tracked, not part of the
own-the-apply copy surface, reaches no vault.

## Out of scope (dispositioned)

1. **D5's precedence standing rule** — sited in **B9-2** (roundtable A19/Dispute 2); B9-1 is
   its worked example, not its home. No governance edit, no `CLAUDE.md` edit, no handshake
   here. B9-2's brief re-reads this build's shipped narrowing against D5's rule text as
   authored (A11's conformance line) — that check is B9-2's, not this build's.
2. **Candidate (d), era-rule expiry** — not shipped; the lanes drain via `vlt-decay`
   (`ledger.md:26`'s re-baseline sentence stands unchanged); the Gap-2 accepted cost already
   points this direction.
3. **Unifying the location and existence tests** — rejected at ideation (A11 note): changes
   denominators on existing records, a behavior change with no filing, in the build whose
   purpose is denominator reproducibility.
4. **Editing any live record to conform** (the seven 2026-08-15 pointers, the checked-off
   2026-08-17 15:12 ask) — forbidden by `relay.md:28`'s own closing rule, kept verbatim.
5. **`skills/vlt-decay/references/drain.md:33`** — refers to the lanes **by pointer**
   ("`vlt-dispatch`'s ledger reference states it") and its invariants survive the narrowing
   (findings still live only in open/terminal lines; drained blocks are fully closed). No
   edit. Verified in re-grounding: no third site restates lane mechanics anywhere in
   `skills/` (grep, 2026-08-21: only `relay.md:28`, `ledger.md:26`, `ledger.md:46`).
6. **The `(bell declaration)` header idiom** observed in the field record — un-annotated
   under the shape grammar, tolerated as written; not this filing's defect. If it recurs it
   files on its own.
7. **A package-lint-hosted lane check** — considered and not chosen (disposition 1, with the
   deviation path priced).

## Verification (unit, at rest — lifecycle step 5)

- **Instrument run:** `uv run tools/dispatch-lane-check.py` → exit 0; **red-then-green
  probe** recorded (flip one fixture expectation → non-zero with a named case; restore →
  exit 0). This is element (6)'s at-rest discharge.
- **Cross-file agreement greps:** `grep -rn "never as a finding\|counts, never findings"
  skills/vlt-dispatch/` returns nothing (both blanket immunities replaced); "never a
  key-requirement finding" (or the builder's equivalent phrasing) present at **both** F1 and
  F4 sites and nowhere else; the era datum sentence appears **once** (relay.md, F1) with
  `ledger.md` pointing, never restating; `resolving` in `ledger.md:28` now reads
  location-test only.
- **Handshake bipartite re-check:** no convention `version:` moved — **package-lint Group E**
  is still the check of record and runs as part of the mid-arc **A/B/C/E** pass (no
  hand-written handshake grep is recorded as verification). `--expect-version`/D is the
  release gate and rides B9-4, not this build.
- **Fixture extension (R2): not applicable** — no release-gate check added or changed
  (disposition 1). If the builder takes the priced deviation (package-lint home), R2 fires:
  covering case + `CASE_FLOOR` 21→22 in the same commit.
- **Legal response (R3):** no new finding class. The Findings class keeps its shipped legal
  response at its single home, `ledger.md:25` (re-fire correctly keyed / recipient checks off
  as superseded) — unchanged in substance by F3's narrowing. Item 7 widens *eligibility* of
  lane pointers to existing non-key finding classes; it creates none.
- **Enumeration widening (R4): not applicable — declared exclusion.**
  `tools/dispatch-lane-check.py` is factory tooling outside every vault-side enumeration:
  the skill-asset manifest walks `skills/`, vitals walk the vault, the own-the-apply copy
  surface excludes `tools/`. It joins the `tools/` surface CLAUDE.md already enumerates for
  release commits — no vital or manifest widens.
- **Scrub:** fixture records and all changed shipped text carry placeholder paths/slugs only;
  no personal or vault-local content (the A11 measurement's vault specifics live in this
  gitignored brief and the roadmap, never in `skills/` or `tools/`).
- **Hygiene:** no `.decision-log.md` in the working tree at finish; one commit for the build.

## Acceptance (live — appended to the roadmap ledger, tagged per §9; all three entries [v0.12.0 run])

1. **`[ship-verifiable]` — the B8-2 (4) re-check, all seven elements, discharged at rest.**
   Elements (1)–(5) and (7): the shipped diff shows each F-site landed and agreeing across
   both files (the cross-file greps above, re-runnable by any reader). Element (6):
   `uv run tools/dispatch-lane-check.py` exits 0 against its fixtures **and** the recorded
   red-then-green probe shows the checker can fail. **GATES Arc 9 closeout** (bound,
   ship-verifiable from birth — the roadmap's pre-seeded B8-2 (4) entry defines the seven
   elements; this check discharges it and says so there rather than restating them).
2. **`[ship-verifiable]` — the A11 delta record stands and is re-derivable.** The brief
   records the pre-fix denominators computed on the real primary-vault dispatch record under
   **both** readings of `resolving` (legacy 15/15; annotated-pathless-pre-era 27/27 strict,
   8/8 under the adopted key-failing membership; era datum 2026-08-18 10:21), states the
   adopted readings (location for denominators, existence for the `handoff` finding), and
   records the **measured delta: 0** — with the wikilink-resolution caveat that makes the
   zero non-vacuous. Dischargeable at rest by re-reading this brief against the shipped F5
   text and the instrument's derivation.
3. **`[field-contingent]` — first post-0.12.0 `ledger` run agrees with the instrument's
   derivation on a live record.** Discharging event, named per R5: **the owner's vlt-core
   upgrade to v0.12.0** (itself an obligation of the two-release split, roadmap A20) followed
   by a `vlt-dispatch ledger` run in ordinary use, on vlt-core (factory machine — the vault
   that can produce the event). Pass: the run's two denominated lines match the stated
   derivation computed over the same live record; the seven historical 2026-08-15 pointers
   render inside the proto denominator (not as findings, not as a zero); no key-requirement
   finding is raised against either lane. Could-have-failed: the pre-fix 0.11.0 run got
   exactly this wrong on this record.

*(No §8 Release — B9-1 is not the last build in v0.12.0; the dual version bump and the
`--expect-version` gate ride B9-4.)*
