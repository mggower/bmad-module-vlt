---
title: 'Build #B9-4 — consumer registration (vault-grown ops get a lawful, checked route
  onto a shipped convention''s roster — closing the boundary the arc''s load-bearing filing
  found shut on both sides)'
status: 'BUILT 2026-08-21 — all eight F-sites landed in one commit on arc9-v0.12.0:
  F1 frontmatter.md member set gains local_consumers: (third member, three properties with
  bells, at the single home), :82 enumeration → §Attestation pointer, version 8→9 with the
  D6-paragraph guard confirmed at bump time (the deferred B9-2 bump discharged — one bump,
  two rule changes); F2 write-verification.md:47 → roster + whole-set write-op qualifier
  with the narrow-attest text intact, version 2→3; F3 nine consumers re-acked frontmatter@9
  (eight SKILL.md pins + the vlt-lint-full.js:11 // depends_on: header — E5''s leg), zero
  body edits (attestation greps found no roster recitals); F4 four consumers re-acked
  write-verification@3 (same files as F3 rows 1–4, one touch per file); F5 checks.md:
  overlay_consumers_illegal added to Overlay append-only with its legal response,
  Convention coherence extended with the local_consumers: stale/unacknowledged/dangling
  walk + local_consumer_unsanctioned with theirs (R3 in-place; base-divergence bullet
  verified to carry no member list — no edit); F6 vlt-upgrade Step-4 overlays_intact
  retirement annotation, render-when-present, overlay never edited; F7 vlt-setup §2b
  clobber-legibility floor (sha256/real-differ compare, quote-then-overwrite) + the
  three-outcome Confirm line; F8 CHANGELOG.md v0.12.0 entry with the four briefs'' titles
  and the scrubbed PARA posture paragraph. Verification: package-lint A/B/C/E PASS
  (D SKIPPED mid-arc; E1/E3/E5 attest the bipartite state — all nine at frontmatter@9,
  all four at write-verification@3, no stragglers by grep); test-package-lint 21/21 green;
  single-home greps 3(a)–(c) clean; bell-presence greps clean; fixture walk (temp
  conventions+overlays+mint-log): overlay consumers: line → overlay_consumers_illegal,
  registrant with no mint entry → local_consumer_unsanctioned, live ref:-keyed entry +
  older pin → stale-ack not silence; F7 probe: modified hook → sha256 differ, diff quoted,
  overwrote-local-edits Confirm form; identical → silent refresh. Disposition 6: all three
  bells shipped — no interim posture, contingency unused. Disposition 2 grep re-run: no
  shipped bare-diff instruction. Scrub grep clean; no .decision-log.md. Acceptance 1 + 2
  ship-verifiable halves discharged at rest (the --expect-version 0.12.0 gate half rides
  vlt-release); acceptance 3 field-contingent, awaits the vlt-core v0.12.0 upgrade run.
  Deviations/notes: (1) F1 also replaced the verified_by code-block enumeration at
  frontmatter.md:78 ("vlt-ingest | vlt-extract | vlt-research | vlt-lint") with a
  §Attestation-pointer placeholder — the brief''s exact-change named only :82, but
  verification 3(a) requires the file carry NO enumeration-shaped value-set text, and the
  code block was the second instance. (2) F8 authored in this build per the brief''s
  either-writer clause, dated 2026-08-21; the posture paragraph phrases the landing as
  "Until the model for this lands (Arc 10)". The release choreography itself (dual version
  bump, --expect-version gate, pre-tag owner actions, ff-merge/tag/push) still runs via
  vlt-release — §8 lists what it owes.'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-18-121417-vault-grown-consumers-have-no-durable-registration.md (A9-2
    Findings 1, 2, 3 + the preferred fix local_consumers:; Findings 4 and 5 are B9-6''s)'
  - 'inbox/2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md (A9-3
    direction 3 ONLY — the A21 clobber-legibility floor, ruled onto a v0.12.0 build;
    directions 1/2 remain B9-6''s)'
  - 'inbox/2026-08-20-093000-para-write-path-single-door-wrong-shape.md (A9-1 K1b''s op-half
    via Q3 — the shared write-verification.md:47 sentence — and the A21 field-facing PARA
    posture; A9-1 itself is Arc 10''s)'
roadmap: 'skills/reports/inbox-evolution-arc9-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-20), per the B9-4 bullet''s binds: roster — Q1
  (overlay consumers: NOT LEGAL, settle in the base; local_consumers: is the contract''s own
  prescribed shape), Q2 (overlay route CLOSED, not a fallback; no grandfather), Q3 (the
  verified_by value set IS the consumer roster — write-verification@2→3, four-consumer
  re-ack, write-op qualifier on the whole set per A18), D3/A22 (frontmatter@8→9 here, nine
  consumers, ninth is the vlt-lint-full.js E5 asset node; B9-2''s D6 bump deferred into this
  walk), D6 via A3 (B9-4 runs D6''s test on itself), roundtable A7 (the three bells), A18
  (K1b partner half NOT solved — carried), A21 (two field-facing v0.12.0 items land here),
  R1 (non-handshake gate pricing).'
risk: 'moderate — two convention version bumps in one build (frontmatter@8→9, a nine-consumer
  walk including one workflow-asset // depends_on: header; write-verification@2→3, a
  four-consumer walk), and this is the v0.12.0 release build.'
---

# Build #B9-4 — consumer registration

## Intent

A vault-grown operation skill today has **no durable way to register as a consumer of a
shipped convention** (A9-2). The base names no carve-out (`write-verification.md:47` is a flat
closed enumeration), the overlay route was ruled **not legal** (Q1 — the base cut no
delegation, `vault-operating-contract.md:117`'s test (a) unsatisfied on the plain text) and is
**closed, not a fallback** (Q2), and the one live instance — vlt-core's owner-adopted overlay
`consumers:` line — sat outside every checker, which is how `vlt-sweep` pinned `frontmatter@7`
against a base at `version: 8` with no alarm.

This build ships the lawful route and its bells, in one walk:

1. **`local_consumers:`** joins the *Vault-writable declared fields* member set
   (`frontmatter.md:278`) — the contract's own prescribed shape (`:124`, the
   designed-parameter-read veto: *parameters yes, filed upstream*; Q1 consequence 3). One
   list edit; the consuming nets (lint base-divergence, upgrade pre-flight + carry-forward)
   follow for free because they read the member set by pointer and carry no list of their own.
2. **Q3's edit**: `write-verification.md:47`'s duplicated enumeration is replaced by a pointer
   to the roster — the `verified_by` value set *is* `consumers:` (write ops only) plus
   write-op `local_consumers:` registrants (A18's qualifier on the **whole** set).
3. **A7's three bells**, so the new route ships neither legal-and-invisible nor
   silently-retired: `overlay_consumers_illegal` in the existing *Overlay append-only* check +
   one retirement line in `vlt-upgrade`'s post-flight report; mint-log backing for every
   `local_consumers:` entry (`local_consumer_unsanctioned`); the *Convention coherence* check
   walks `local_consumers:` with the same stale/unacknowledged/dangling vocabulary.
4. **The two handshakes**: `frontmatter@8 → @9` (nine consumers — this walk also carries
   B9-2's D6 rule paragraph, the bump B9-2 deliberately deferred here; commit `d8707bf` and
   B9-2's brief disposition 1 bind it) and `write-verification@2 → @3` (four consumers).
5. **The two A21 field-facing v0.12.0 items** that had no other v0.12.0 home: the
   clobber-legibility floor on the vitals-reader overwrite, and the field-facing PARA posture
   (dispositions 3–4).

**All rejected alternatives in the parent filings and rulings are settled — do not
re-litigate.** In particular: the overlay registration path (Q1/Q2 — closed, dissent on
record), the closed-with-a-named-error variant (superseded by A7's bell), grandfathering
vlt-core's live line (Q1 consequence 1 — no grandfather clause), and folding Finding 4 or the
B9-6 bump into this build (D3 ruled (i) at Dispute 1 — two bumps across two releases, reasons
recorded).

## Brief-time dispositions

1. **The deferred B9-2 bump is honored here, and the walk covers both rule changes.**
   (Binding: commit `d8707bf`'s body; B9-2 brief dispositions 1–2; D3/A22; Dispute 2.)
   `frontmatter.md` today carries B9-2's *Enforcement ships with widening* paragraph
   (`frontmatter.md:271`) with `version: 8` **deliberately untouched**. This build performs
   the single `@8 → @9` bump, and the nine-consumer re-ack attests to **both**
   `local_consumers:` **and** the D6 paragraph. The builder verifies the D6 paragraph is
   present in the file at bump time (it is at `:271` now) before writing `version: 9` — the
   bump must never ship covering only one of the two rule changes it prices.

2. **The owed grep is discharged: no shipped doc instructs a raw base-vs-baseline `diff`.**
   (Roadmap §Questions deliberately left to brief time, third bullet — "the brief owes the
   grep"; the filing's bonus-instrument note.) Run this session over `skills/`: every shipped
   base-vs-baseline comparison either says "compare" abstractly with the mechanics elsewhere
   (`checks.md:41`, `vlt-upgrade/SKILL.md:37`) or routes through
   `verify-skill-manifest.py` (SHA-256 — already a checksum). `vlt-groom`'s "diff" is a
   rendered proposal surface, not a base-vs-baseline compare. **No retrofit is owed.** The
   rule survives forward: the one *new* compare this build ships (F7) specifies **sha256 or a
   real line differ, never a bare `diff` invocation** — a shell-wrapped `diff` fails toward
   "no divergence", the dangerous direction.

3. **The A21 clobber-legibility floor is ruled INTO this build's scope (F7).** (Roadmap A21 /
   Dispute 4 — "all three land" in v0.12.0; "make the clobber legible at upgrade time attaches
   to a v0.12.0 build as a floor".) B9-2's brief explicitly declined to absorb it (its F5
   out-of-scope note) and B9-6 — the floor's parent filing's build — ships in **v0.13.0**, so
   without a ruling here the owner's v0.12.0 floor would ship in no v0.12.0 build at all.
   B9-4 is the last v0.12.0 build; the floor lands here. Scope is the floor **only** — a
   checksum-compare before the module-owned `vlt-vitals.py` overwrite plus a legibility line
   in the Confirm summary (grounded at `vlt-setup/SKILL.md:183` and `:324`) — never a preserve
   mechanism or an import hook; directions 1/2 remain B9-6's brief-time question, built **on
   top of** this floor. B9-6's brief re-checks whether the floor as shipped already satisfies
   its "make the loss legible" leg and says so there rather than double-shipping.

4. **The A21 field-facing PARA posture — siting ruled (the call B9-2's disposition 7 flagged
   here).** Sited in **two homes, neither widening anything**: **(a)** a short paragraph in
   `CHANGELOG.md`'s v0.12.0 entry (public release surface — F8) stating that for vaults with
   agent-authored PARA content the finding is known, that overflow belongs under `_agent/`
   rather than through a falsified `sources:`, and that the model lands in Arc 10; **(b)** the
   arc roadmap's carry-forward at closeout (factory-side — recorded as an `arc-closeout`
   obligation in Acceptance, not an edit this build makes). The changelog is the one shipped
   surface every upgrading vault reads at exactly upgrade time, and the posture names no
   vault and widens no rule — `vault-operating-contract.md:61`/`:63` and `extraction.md`
   remain unchanged per D6's interim posture.

5. **Finding-id names (clerk-named where the roadmap left them unnamed).** A7 names
   `overlay_consumers_illegal` (bell 1); bell 2's finding id is
   **`local_consumer_unsanctioned`**; bell 3 reuses the coherence check's existing
   stale/unacknowledged/dangling vocabulary (extended classes, not new ids). Each new class
   states its legal response at `checks.md`, in the same build (standing rule R3).

6. **D6's test, run on B9-4 itself — result: SATISFIED BY NAMED BELLS; no interim posture
   ships.** (Roundtable A3.) B9-4 is a widening (a new vault-writable field with arbitrary op
   names; a `verified_by` value set that becomes open-ended), and all three A7 bells ship in
   this same build: the widening's violations are caught by `overlay_consumers_illegal`
   (illegal route), `local_consumer_unsanctioned` (unsanctioned registration), and the
   extended coherence walk (stale/unacknowledged/dangling registrants). **Contingency, stated
   at brief time as the roadmap requires:** if the builder must slip any bell, the interim
   posture is the sentence *"a `local_consumers:` registrant must be a write op; unenforced
   until the registration check ships"* in shipped text at `write-verification.md`
   §Attestation — and the slip is a numbered deviation naming which bell. The brief's ruling
   is all-ship; the contingency exists so a slip cannot be silent.

7. **A18 recorded: Q3 does NOT solve K1b's partner-writer half — carried to Arc 10, not
   solved here.** Q3 buys a lawful attestation route for vault-minted **write ops** that
   register via `local_consumers:`. The writer behind the 0-of-56 unattested-PARA census is a
   **partner writing in its own sitting**, not a registered op, and no `local_consumers:`
   line admits it. After this build ships, that census still has no lawful response. This
   brief changes nothing about it and the builder must not try; the record here exists so
   Arc 10's capture inherits the debt named, not rediscovered.

8. **R1 pricing (non-handshake gates) — "no bump owed" is not "no cost", applied.**
   **C6 (rule-card):** *not applicable* — B9-4 touches `frontmatter.md`,
   `write-verification.md`, `checks.md`, `vlt-upgrade/SKILL.md`, `vlt-setup/SKILL.md`,
   `CHANGELOG.md`, and nine consumer ack surfaces; it does **not** touch
   `vault-operating-contract.md`, so no rule-card re-derivation is owed (C6 still runs at the
   gate and passes unchanged — B9-2 left it green). **E4:** *not applicable* — this build adds
   vault-side `vlt-lint` finding classes, not `package-lint` checks; no harness case owed,
   `CASE_FLOOR` stays 21. **E5:** *applies* — the ninth frontmatter consumer is
   `vlt-lint-full.js`, whose ack is the `// depends_on:` header at
   `skills/vlt-setup/assets/workflows/vlt-lint-full.js:11` — a different edit surface from
   skill frontmatter (and a comment: workflow assets parse their `args` as JSON strings at
   runtime, but the ack line is a machine-parseable comment, edited as text). A walk that
   counts only skills undercounts this build by one.

## F-sites

### F1 — `frontmatter.md`: the member set gains `local_consumers:`, the `:82` restatement becomes a pointer, `version: 8 → 9`

File: `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md`.

**Current state.**
- `:11-12` — `version: 8`; `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint,
  vlt-mint, vlt-dispatch, vlt-setup, vlt-groom, vlt-lint-full.js]` (nine, matching D3/A22).
- `:75` opens the *Write attestation* section: "This section defines only the **fields**; the
  checklist, fail-open rule, scope rule, and audit contract live in `write-verification.md`."
- `:82` — eight lines later, the file violates the sentence it opens with: "The legal value
  set is the three write ops plus `vlt-lint` (lint attests **narrowly** — only files its own
  auto-fix touched; see `write-verification.md`)." A value set is contract, not field schema
  (A9-2 Finding 3; `write-verification.md:44` states the reciprocal division).
- `:271` — B9-2's *Enforcement ships with widening* paragraph, present, unbumped
  (disposition 1).
- `:278` — *Vault-writable declared fields* (**moved from the roadmap's `:276` by B9-2's
  edit; content intact — trivial shift, not a correction**): "**This section is the member
  set's single home** — today `adoption_first_instance:` and `review_after:` — and the
  consuming nets point here rather than carrying their own list. Declaring a further field
  vault-writable is a base rule change: it bumps this file's `version:` and walks every
  consumer."
- `:284` — *Local conventions (vault-originated)*: the sanctioning pattern bell 2 reuses ("a
  live, `ref:`-keyed convention-mint entry in `_agent/mint/decision-log.md`").

**The exact change.**
1. **`:278`** — extend the member-set sentence to three members and define the new field in
   the same paragraph (the member set's single home is also the right definition site — the
   other two members are defined exactly here). Add, after the `review_after:` clause, prose
   to this effect: **`local_consumers:`** is the third member — a vault-written YAML list of
   **vault-grown operation skills** registering as consumers of *this base convention*
   (`local_consumers: [vlt-sweep]`), the durable registration route the overlay path never
   was (an overlay `consumers:` line is illegal — the *Overlay append-only* check flags it
   `overlay_consumers_illegal`). Three properties, each with its bell: **(a)** every entry is
   backed by a **live, `ref:`-keyed mint entry** in `_agent/mint/decision-log.md` naming the
   registering op — the same sanctioning pattern *Local conventions* below requires — and an
   unsanctioned entry is a `vlt-lint` finding (`local_consumer_unsanctioned`); **(b)** a
   registrant acks exactly as a base consumer does — a flat `name@version` pin in its own
   `depends_on:` — and the coherence check walks `local_consumers:` with the same
   stale/unacknowledged/dangling vocabulary as `consumers:`; **(c)** the base roster is the
   **ceiling** of what registration can grant — for attestation authority specifically, a
   registrant must be a **write op** (`write-verification.md`, §Attestation — the contract
   around `verified_by` lives there, not here).
2. **`:82`** — replace the restated value set with a pointer, keeping the field-definition
   half: "**`verified_by`** — the operation that ran tier-1 on this file. The legal value set
   is the attestation contract's, defined in `write-verification.md` §Attestation — not
   restated here." Delete the enumeration and the parenthetical narrow-attest recital (that
   contract text lives at `write-verification.md:47` and survives there — F2). **Prose
   clarification removing a duplicated rule: this edit on its own owes no bump** (roadmap,
   §Promoted out of brief time) — the bump this file takes is bought by item 3.
3. **`:11`** — `version: 8` → `version: 9`. The bump prices **two** rule changes: item 1
   (`local_consumers:`, a new vault-writable member — `:278`'s own stated price) **and**
   B9-2's D6 paragraph at `:271` (the deferred bump, disposition 1). `consumers:` at `:12` is
   unchanged — no consumer joins or leaves.

**Why.** A9-2 Finding 3 (`:82`), the preferred fix (`:278`), Q1 consequence 3
(`vault-operating-contract.md:124` — cite as grounding, do not edit the contract), A7 bells
2–3 declared at the field's single home, D3/A22, disposition 1.

**Out of scope at this site:** per-section enforcement addressing (Finding 4) — ruled into
B9-6 by D3, riding the `@9 → @10` bump; do not touch the *Enforcement declaration* schema.
The *Local conventions* paragraph (`:284`) is untouched — bell 2 points at its pattern, never
restates its mechanics.

### F2 — `write-verification.md`: the value set becomes the roster with the write-op qualifier, `version: 2 → 3`

File: `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md`.

**Current state.** `:12` — `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint]`.
`:44` — the division of labor ("The fields … are defined in `frontmatter.md` — referenced
here, not redefined. This file owns the contract around them"). `:47` — "**`verified_by`
value set:** the three write ops (`vlt-ingest`, `vlt-extract`, `vlt-research`) plus
`vlt-lint` — and lint attests **narrowly**: it writes the pair only on files its own auto-fix
touched (an auto-fix bumps `last_updated` and would otherwise re-stale the attestation it
just validated). Lint never attests a file it merely read." The enumeration is the same four
names as `:12`, written twice — Q3's single-home violation.

**The exact change.**
1. **`:47`** — replace the enumeration with the roster pointer carrying A18's qualifier **on
   the whole set**, verbatim in force: *"the `verified_by` value set is this file's
   `consumers:` **that are write ops**, plus write-op `local_consumers:` registrants
   (`frontmatter.md`, *Vault-writable declared fields*)"* — the roster is **membership and
   ceiling**, never an automatic grant: a skill added to `consumers:` for handshake reasons
   alone acquires no attestation authority (the write-op qualifier is what blocks the
   over-admission vector A18 named). **Keep the per-consumer narrowing intact** (Q3 caveat
   1): the "lint attests **narrowly** … Lint never attests a file it merely read" sentences
   survive unchanged — the roster is membership; per-consumer scope stays stated where it
   applies.
2. **`:10`** (`version:` key) — `version: 2` → `version: 3`. This is a base rule change (the
   value set's definition changes from closed enumeration to qualified roster) and re-acks
   all four consumers (F4). `consumers:` at `:12` is unchanged.

**Why.** Q3 as ruled ("the value set IS the consumer roster") + A18's two amendments; A9-2
Finding 1 (the base now cuts the delegation explicitly and narrowly — Q1's test (a) satisfied
for the one field that needed it); A9-1 K1b's **op-half** (disposition 7 records the partner
half as carried, not solved).

**Out of scope at this site:** no delegation clause anywhere else in the *Attestation*
section; no change to the fail-open rule, scope rule, or audit contract.

### F3 — the nine-consumer `frontmatter@9` re-ack (eight skills + one asset header)

**Current state** (all pins verified this session at `frontmatter@8`):

| # | Consumer | Ack surface |
|---|---|---|
| 1 | vlt-ingest | `skills/vlt-ingest/SKILL.md:4` |
| 2 | vlt-extract | `skills/vlt-extract/SKILL.md:4` |
| 3 | vlt-research | `skills/vlt-research/SKILL.md:3` |
| 4 | vlt-lint | `skills/vlt-lint/SKILL.md:4` |
| 5 | vlt-mint | `skills/vlt-mint/SKILL.md:3` |
| 6 | vlt-dispatch | `skills/vlt-dispatch/SKILL.md:3` |
| 7 | vlt-setup | `skills/vlt-setup/SKILL.md:3` |
| 8 | vlt-groom | `skills/vlt-groom/SKILL.md:3` |
| 9 | **vlt-lint-full.js** | `skills/vlt-setup/assets/workflows/vlt-lint-full.js:11` — the `// depends_on:` comment header (E5's leg, not E1's) |

**The exact change.** Each pin `frontmatter@8` → `frontmatter@9`. A re-ack is an attestation,
not a find-and-replace: for each consumer, confirm its text does not contradict the two rule
changes the bump carries (`local_consumers:` + the D6 paragraph) before bumping the pin. The
expected result is **zero body edits** — consumers point at the convention rather than
reciting the roster (the coherence check's own recite-vs-point test), and neither rule change
alters any field these consumers recite. If a consumer's body is found reciting the
consumer-roster mechanics, the fix is a pointer, recorded as a deviation — never a restated
list.

**Why.** D3/A22 (nine, not "seven-plus"; the ninth is an E5 asset node); the version-handshake
standing rule (rule change bumps and re-acks in the same build).

### F4 — the four-consumer `write-verification@3` re-ack

**Current state** (verified at `write-verification@2`): vlt-ingest (`SKILL.md:4`), vlt-extract
(`SKILL.md:4`), vlt-research (`SKILL.md:3`), vlt-lint (`SKILL.md:4`) — the same files as F3
rows 1–4; both pin edits land in one touch per file.

**The exact change.** Each pin `write-verification@2` → `write-verification@3`, with the same
attest-then-bump discipline: the three write ops confirm nothing in their attestation steps
recites the closed enumeration; vlt-lint confirms its narrow-attest behavior is unchanged
(it is — F2 keeps the narrowing text).

**Why.** Q3's flagged second handshake ("the brief prices two handshakes, not one").

### F5 — `vlt-lint/references/checks.md`: bells 1 (finding id) and 3 (coherence walk), plus bell 2's check home

File: `skills/vlt-lint/references/checks.md`.

**Current state.** `:36` — *Convention coherence* walks "each `{conventions}/*.md` carrying a
`version:` and `consumers:`" and reads listed consumers' `depends_on:` pins (skill acks and
`.js` asset-header acks alike); `local_consumers:` is not in its vocabulary. `:41` —
*Convention base divergence* already excludes "the lines of fields declared vault-writable"
by reading `frontmatter.md`'s member set ("read it there, never carry a list here") and
already runs the live-mint-entry test against `_agent/mint/decision-log.md` — so the
divergence exclusion for `local_consumers:` needs **no edit**. `:42` — *Overlay append-only*
opens every `{overlays}/{name}.overlay.md`, inspects **section headings only** (ids
`overlay_not_append_only`, `overlay_orphan`); an overlay `consumers:` line in frontmatter
passes clean.

**The exact change.**
1. **`:42`, bell 1** — add one finding id to the existing check: an overlay carrying a
   `consumers:` line or any handshake key (`version:`/`depends_on:`-shaped frontmatter)
   flags **`overlay_consumers_illegal`**. **Legal response, stated in the same sentence
   (R3):** "register via `local_consumers:` in the base convention (`frontmatter.md`,
   *Vault-writable declared fields*); an overlay is content extension, never handshake
   membership (Q1: the route is closed, not a fallback)." No new walker — the check already
   opens the exact file.
2. **`:36`, bells 2 + 3** — extend *Convention coherence* with one addition (the roadmap
   sizes it "one bullet"; landing it inside the existing check's paragraph keeps
   single-home): the check also walks each base convention's **`local_consumers:`** (the
   vault-writable registration field — `frontmatter.md`, *Vault-writable declared fields*)
   with the **same vocabulary as `consumers:`** — a registrant whose `depends_on` pins an
   older version is a stale ack; a registrant with no `depends_on` entry is unacknowledged;
   an entry naming a skill that isn't installed is **dangling** (the vault-local-registrant
   test the roadmap names explicitly — legal response: correct the list). Plus the
   sanctioning test (bell 2): an entry with **no live `ref:`-keyed mint entry** in
   `_agent/mint/decision-log.md` naming the registering op flags
   **`local_consumer_unsanctioned`** — same log, same liveness rule as the base-divergence
   bullet's local-convention test. **Legal response (R3):** mint the registration (a dated
   `ref:`-keyed entry) or remove the entry. Note in the same breath that
   `local_consumers:` registrants are **inside** the version handshake by design (unlike a
   sanctioned local convention's discovery roster, which stays exempt from the pin half —
   that existing exemption text is untouched).

**Why.** A7's three bells verbatim; without bell 3, v0.12.0 ships a lawful registration route
and *still* no stale-ack alarm — the exact defect A9-2 Finding 2 filed (`vlt-sweep` at
`frontmatter@7` against `version: 8`). Without bell 2, the vault-writable exclusion converts
registration from detected-but-homeless into legal-and-invisible (Dr. Quinn's finding — the
arc's thesis executed against its own repair).

**Out of scope at this site:** the enforcement-doctrine meta-check (`:37`) and overlay
walking for enforcement frontmatter — B9-6's (Finding 5/D2). The base-divergence bullet
(`:41`) — verified this session to need no edit; the builder confirms by grep that it still
carries no member list of its own.

### F6 — `vlt-upgrade/SKILL.md`: the retirement line in the post-flight report (bell 1's second half)

File: `skills/vlt-upgrade/SKILL.md`.

**Current state.** Step 4's report shape (`:89-115`) carries `overlays_intact:` at `:100` and
routes each divergence line to a durable host; nothing names an overlay-carried `consumers:`
line, so at v0.12.0 vlt-core's live owner-adopted line would become illegal on disk in
silence — "the operator's entire experience of the ruling would be that nothing happens"
(A7). Step 1's overlay snapshot (`:35`) and Step 2's vault-writable carry-forward (`:49`)
already read the member set by pointer — `local_consumers:` values are carried forward across
base refreshes with **no edit here**.

**The exact change.** One line, sited on the Step-4 report: the `overlays_intact:` entry
annotation gains the retirement note — when a preserved overlay carries a `consumers:` (or
other handshake-shaped) line, the report line for that overlay appends *"carries a
`consumers:` line — the overlay registration route is retired (v0.12.0): re-register via
`local_consumers:` in the base (`frontmatter.md`, *Vault-writable declared fields*) and a
mint entry, then remove the overlay line — `vlt-lint` flags it `overlay_consumers_illegal`
until then"*. Render-when-present; the overlay itself is **never edited or dropped** by the
upgrade (append-only preservation holds — the retirement is the vault's move, surfaced, not
performed).

**Why.** A7 bell 1, second half: "one line in `vlt-upgrade`'s reconcile report naming the
retirement, so vlt-core's live owner-adopted line does not simply become illegal in silence."

**Out of scope at this site:** Step-3.6/Step-3 ordering (S3's spike, B9-6); any A9-3
direction-1/2 machinery; the Step-5 ledger template (the Notes line already carries
non-empty report specifics — no template change owed for a render-when-present annotation).

### F7 — `vlt-setup/SKILL.md`: the A21 clobber-legibility floor on the vitals overwrite

File: `skills/vlt-setup/SKILL.md`. (Disposition 3 rules this into scope.)

**Current state.** `:183` — "Copy `./assets/hooks/vlt-vitals.py` → 
`{root}/.claude/hooks/vlt-vitals.py` … **module-owned, not user-authored — overwrite it on
every install/update** … the vault never edits it." The overwrite is silent: unlike shipped
skill assets (SHA-manifest net) and base conventions (baseline compare), the hook has no
divergence surface — the exact clobber A9-3's issue #1 filed, destroying a derive function
that must be rewritten rather than re-pointed, on every upgrade. `:324` — the Confirm summary
reports only "`vlt-vitals.py` hook installed/refreshed".

**The exact change.**
1. **`:183`** — before overwriting an *existing* `{root}/.claude/hooks/vlt-vitals.py`,
   compare it to the incoming file **by checksum (`sha256`) or a real line differ — never a
   bare `diff` invocation** (a shell-wrapped `diff` fails toward "no divergence", the
   dangerous direction — disposition 2). Identical → overwrite silently as today. Different →
   still overwrite (module-owned stands; this is a floor, not a preserve path) but **quote
   the differing content into the provisioning notes first** and mark the refresh as
   *overwrote local edits* for the Confirm line. On an upgrade (`vlt-upgrade` Step 6's
   provision hand-off) the quoted content reaches the upgrade ledger's Notes line by the
   existing "name the report's … entries here when non-empty" mechanism — state that in one
   pointer clause.
2. **`:324`** — the Confirm summary's enforcement-kit clause distinguishes three outcomes:
   "`vlt-vitals.py` installed / refreshed (identical) / **refreshed — overwrote local edits
   (diff preserved in the notes; a vault-local derive function does not survive here — a
   durable home for local metrics lands in a later release)**".

**Why.** A21 / Dispute 4: the floor is "the only thing that helps the vault losing its derive
function on every upgrade between now and v0.13.0". Grounded home: the overwrite site and its
report surface — not `vlt-upgrade`, which merely invokes this provision.

**Out of scope at this site:** any import hook, local-metrics module, or declarative inline
metrics (B9-6, directions 1/2, S3-gated); tripwire-registry behavior at `:184`
(merge-by-id already preserves local wires — not the clobber A9-3 filed).

### F8 — `CHANGELOG.md`: the v0.12.0 entry carries the field-facing PARA posture

File: `CHANGELOG.md` (repo root, public).

**Current state.** Newest-first sections; top is `## v0.11.0 — 2026-08-17`. The v0.12.0 entry
does not exist yet — it is authored at release time from the four briefs' titles per the
Arc 6 changelog contract.

**The exact change.** The v0.12.0 entry (authored in this build as part of §8's release
choreography prep, or by `vlt-release` — whichever writes the entry carries this) includes
the disposition-4 posture paragraph, scrubbed (no vault names, no counts, no filing paths):
a note for vaults with agent-authored PARA content that a known finding exists — agent
overflow written into PARA can falsify `sources:` as provenance; until the Arc 10 model
lands, such content belongs under `_agent/`, not in PARA through a stretched `sources:`
list; the PARA location rule itself stands unwidened.

**Why.** A21 / Dispute 4 (Maya's charge upheld: the D6 interim posture was addressed to the
factory, not the field); disposition 4 sites it here.

## Registration

**No new skill, no workflow, no `module-help.csv` row** (R2 satisfied vacuously — this build
creates no `skills/vlt-*` dir). The registration story is the **two consumer walks**:

- **`frontmatter@8 → @9`** — nine consumers re-acked (F3), including the `vlt-lint-full.js`
  asset-node header (E5's leg). The walk covers both rule changes: `local_consumers:` and
  B9-2's deferred D6 paragraph (disposition 1).
- **`write-verification@2 → @3`** — four consumers re-acked (F4).

Bipartite consistency after both walks: every consumer listed ↔ every ack current, both
conventions, both directions. The check of record is `package-lint` Group E (§7). R1's
non-handshake gates are priced in disposition 8 (C6 n/a — contract untouched; E4 n/a; E5
applies via F3 row 9).

## Out of scope (dispositioned)

1. **Finding 4 (per-section enforcement addressing for overlays)** — ruled into B9-6 by D3;
   rides the `@9 → @10` bump (Dispute 1, option (i)). Do not touch `frontmatter.md:255`'s
   schema.
2. **Finding 5 (the overlay bell — enforcement meta-check walking `{overlays}`)** — B9-6's,
   jointly gated with A9-3's durable metric home (D2); S3-gated, v0.13.0.
3. **A9-3 directions 1/2 (durable vault-local metric home)** — B9-6's brief-time question,
   built on top of F7's floor; F7 must not grow toward them.
4. **K1b's partner-writer half** — carried to Arc 10, not solved (A18; disposition 7).
5. **`vault-operating-contract.md`** — untouched. Q1's grounding cites `:117`
   (carve-out test), `:120` (base-rule-change routing), `:124` (designed-parameter-read
   veto) as they now stand (shifted from the roadmap's `:101/:105/:104` by B9-2's insertion —
   content intact); the brief cites, the builder does not edit. Hence no rule-card
   re-derivation (disposition 8) — **R1's contract clause: not applicable.**
6. **A sanctioned local convention's `consumers:` roster** — stays a discovery roster,
   exempt from the pin half (`checks.md:36`'s existing exemption); `local_consumers:` is the
   reverse direction (registering against a *shipped* base) and does not alter it.
7. **`vlt-mint` body text** — no routing clause added for registration unless the F3 re-ack
   finds its *Edit a convention* text contradicting the new field; expected zero edits
   (point-at-the-map), any exception recorded as a deviation.
8. **The wrapped-`diff` retrofit across shipped docs** — grep run, clean; no retrofit owed
   (disposition 2). New compare text (F7) carries the checksum/real-differ specification.
9. **vlt-core's live overlay `consumers:` line itself** — vault-local state; the module
   never edits an installed vault. Its retirement is surfaced by F5/F6 and performed by the
   owner on the v0.12.0 upgrade run (Acceptance check 3).

## Verification (unit, at rest — lifecycle step 6's exit)

1. **Handshake bipartite re-check — `package-lint` Group E is the check of record** (E1
   handshake-bipartite both directions, E3 stray-pin, E5 asset nodes): run
   `uv run tools/package-lint.py` mid-arc groups A/B/C/E — expect PASS with
   `frontmatter@9` across all nine acks (eight `depends_on:` pins + the
   `vlt-lint-full.js:11` header) and `write-verification@3` across all four. A hand-written
   `grep "frontmatter@" skills/` is an editing aid, never the recorded verification.
2. **The bump covers both rule changes**: before writing `version: 9`, confirm
   `frontmatter.md` carries the D6 paragraph (currently `:271`) — the deferred-bump guard
   (disposition 1).
3. **Single-home greps**: (a) `frontmatter.md` no longer enumerates the `verified_by` value
   set (the `:82` pointer stands; the only enumeration-shaped text lives in
   `write-verification.md` §Attestation); (b) neither `checks.md` nor `vlt-upgrade/SKILL.md`
   carries a vault-writable member list of its own (both point at `frontmatter.md` — the
   free-ride premise, verified not assumed); (c) `local_consumers:` semantics are stated
   once (F1) and pointed at everywhere else (F2, F5, F6).
4. **Bell presence greps**: `overlay_consumers_illegal` appears in `checks.md`'s *Overlay
   append-only* check with its legal response; `local_consumer_unsanctioned` and the
   `local_consumers:` stale/unacknowledged/dangling walk appear in *Convention coherence*
   with theirs (R3 satisfied in-place); the F6 retirement annotation appears in Step 4's
   report shape.
5. **Fixture walk for bell 2/3 semantics** (real run against a temp fixture, per the
   unit-verify-at-rest standard): a temp `{conventions}`+`{overlays}`+mint-log fixture with
   (i) an overlay carrying `consumers:` → expect `overlay_consumers_illegal`; (ii) a base
   with `local_consumers: [vlt-fixture-op]` and no mint entry → expect
   `local_consumer_unsanctioned`; (iii) the same with a live `ref:`-keyed entry and a
   registrant pinning an older version → expect the stale-ack class, not silence. (These are
   prose checks in `checks.md` executed by `vlt-lint` at run time — the fixture walk
   exercises the checker's *instructions* by a dry-run read; where the builder can drive the
   real `vlt-lint` flow against the fixture, prefer that.)
6. **F7 floor probe**: temp-dir run of the §2b provision with a locally-modified existing
   `vlt-vitals.py` → the compare detects, the note quotes the differing content, the Confirm
   line renders the *overwrote local edits* form; with an identical file → silent refresh
   (no vacuous alarm).
7. **R3**: satisfied at `checks.md` for both new finding classes (check 4). **R4: not
   applicable** — this build adds no file to any enumerated class (every F-site edits an
   existing file). **E4/C6: not applicable** (disposition 8); `tools/test-package-lint.py`
   stays 21/21.
8. **Scrub**: no personal or vault-local content in any changed shipped file — in
   particular the F8 changelog paragraph names no vault, no census count, no filing path;
   F1/F5 worked examples use placeholder op names (`vlt-sweep`-style generic slugs are
   acceptable as the filing's public example; never a partner or person name).

## Release (this is v0.12.0's release build)

- Dual version bump: `.claude-plugin/marketplace.json` `"version"` → `0.12.0` and
  `skills/vlt-setup/assets/module.yaml` `module_version` → `0.12.0`.
- Gate: `uv run tools/package-lint.py --expect-version 0.12.0` — **tag only on exit 0**;
  record the PASS summary line in the release commit message. Group D plus the E1/E3/E5
  pin checks at the gate are the mechanical net for this build's two walks.
- Pre-tag owner actions (inherited, restated so the gate is visible): **(a)** the B9-3
  `gh label create` sequence (seven labels; `.github/ISSUE_TEMPLATE/config.yml`); **(b)**
  ruling 4c's bound — the three lint-surfaced module-feedback candidates discharge **before
  v0.12.0 is tagged** (ledger entry; roadmap A8 — added to this release's pre-flight).
- Then: ff-merge `arc9-v0.12.0` → `main`, tag `v0.12.0`, push main + tag (`vlt-release`
  runs the choreography as one gated sequence).
- The v0.12.0 `CHANGELOG.md` entry collects the four briefs' titles verbatim and carries the
  F8 posture paragraph.

## Acceptance (live — appended to the roadmap ledger)

Three checks; (1)–(2) `[ship-verifiable]`, (3) `[field-contingent]` under the
**[v0.12.0 run]** partition with its event named per R5/A20.

1. **`[ship-verifiable]` — the two walks are bipartite-consistent and the route + bells
   shipped, at rest / at the v0.12.0 gate:** `package-lint` Group E PASS with all nine
   consumers at `frontmatter@9` (incl. the `vlt-lint-full.js` `// depends_on:` header, E5)
   and all four at `write-verification@3`; the single `@8 → @9` bump covers both rule
   changes (D6 paragraph present in the shipped file — the B9-2 deferred-bump obligation
   discharged); `write-verification.md:47` reads as roster + write-op qualifier with the
   narrow-attest text intact; `frontmatter.md:82` is a pointer; the member set carries
   `local_consumers:` with the mint-backing, ack, and ceiling properties; both finding
   classes (`overlay_consumers_illegal`, `local_consumer_unsanctioned`) and the
   `local_consumers:` coherence walk are present in `checks.md` with legal responses; the
   F6 retirement annotation, F7 floor (checksum-compare + three-outcome Confirm line), and
   F8 changelog posture are present in shipped text. Discharged by the release gate
   (`--expect-version 0.12.0` exit 0) plus the recorded verification greps and fixture
   probes (§7 items 3–6).
2. **`[ship-verifiable]` — the D6 self-test record stands:** B9-4 is a widening and shipped
   with all three A7 bells in the same build — no interim posture in shipped text (brief
   disposition 6; the contingency sentence was not needed, or the BUILT record's numbered
   deviation says which bell slipped and the posture shipped instead). Discharged by reading
   the BUILT record against the shipped diff.
3. **`[field-contingent, v0.12.0 run]`** — discharging event named per R5: **the owner's
   vlt-core upgrade to v0.12.0 (the A20 obligation run), on vlt-core — the one vault
   carrying the live owner-adopted overlay `consumers:` line, so the retirement path is
   exercised exactly here.** Pass = the post-flight report's overlay line renders the F6
   retirement annotation (not silence); the next `vlt-lint` run flags
   `overlay_consumers_illegal` with its route; the owner's re-registration
   (`local_consumers:` entry + dated `ref:`-keyed mint entry, overlay line removed) clears
   it; and the coherence walk then covers the registrant — the vlt-sweep-class stale-ack
   scenario (a registrant pinning an older version) is detectable rather than structurally
   invisible. The Confirm summary's vitals line renders in the new three-outcome shape (if
   no local vitals edit exists at upgrade time, only the render-shape half discharges — no
   vacuous "legibility worked" tick against a clean overwrite). **Also recorded here as an
   `arc-closeout` obligation, not a check: the arc carry-forward carries the disposition-4
   PARA posture (the A21 factory-side half).**
