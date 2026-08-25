---
title: 'Build #3 — the PARA posture (PARA stops using location as a proxy for trust: honest, attested frontmatter becomes the entry condition, containers declare their own writers, and lint enforces it)'
status: 'BUILT 2026-08-25 — the PARA posture landed whole across all thirteen F-sites (F0..F12) in fifteen shipped files. PARA''s entry condition is now honest, attested frontmatter (`contract:66`); the Layer-3 location prohibition is replaced by the write-posture resolver (`contract:68`, nearest declaring ancestor + inheritance + `open` default, `{wiki}` removed at population time); `extraction.md` 6 → 7 with a four-ack walk and the new `writers:` charter field + `moc` artifact type; `vlt-lint` now SELECTS the PARA population in both modes (F0/step 0) and enforces authorization via the new `para_writer_unauthorized` check + report slot; `vlt-query` gains a legal PARA destination and its first `depends_on:`; the rule-card''s write-boundary line is a decidable TEST with a re-derived sha; the MOC prohibition is narrowed to content type; the `{wiki}` qualifier is single-homed at `contract:64` with nine pointers and the `checks.md:18` carve-out exempt; and `vlt-upgrade` gains `governance_rule_changes:` so the retroactive-open window is announced, not discovered. ALL FIVE ship-verifiable gating checks RUN AND PASSED at rest — real numbers below. Deviations: (1) two undeclared sites restated retirement-table row 3 and had to land or the V8 gate would fail — `extraction.md:26` (*"it does not add an artifact write-path"*, inside the very convention being bumped) and `vlt-track/SKILL.md:21` (*"PARA artifacts are still written only through extraction … it does not add an artifact write-path"*, a SIXTH site of the retired frame, named in no F-site). Both narrowed to op-specific/section-specific true statements, neither deleted; `vlt-track` was already an `extraction.md` consumer acking `@7`, so no handshake cost. **This is the brief''s own retirement-completeness rule (A25) doing its job — the table was one row short of the shipped truth, and the grep battery is what found it.** (2) The V3 probe''s FIRST run surfaced a real hole the brief did not anticipate: the resolver''s identity legs read only `author: human`/`author: agent`/`verified_by:`, so **`author: hybrid` resolved NO identity at all** — every human-ratified file (and every charter, which the schema *mandates* as `hybrid`) beneath a `writers: [human]` container silently escaped the join. Fixed by adding one clause at `contract:68` and `checks.md:19`: `author: hybrid` reads as `human` (the hybrid rung IS human ratification — the honesty rule), and a file resolving no identity at all is left to the honesty nets rather than flagged here. The contract sha was re-derived a second time and the probe RE-RUN against the final shipped text; the fence recorded below is from that second run. (3) The rule-card came out **net-longer, not net-shorter** as A28 predicted — 6,957 → 7,106 B (+149). Still 894 B inside `RULE_CARD_BUDGET = 8,000`; the iff-test needed both legs stated to stay decidable, and shortening it further would have traded decidability for bytes the budget does not need. (4) F11''s source rule was tightened at build time from "the CHANGELOG entry" to "the module source''s `CHANGELOG.md` entries for the versions being crossed, read from the same source tree this upgrade applies from" — the roadmap''s own capture finding is that `CHANGELOG.md` has no delivery path INTO a vault, so naming it without saying which tree reads it would have shipped an unresolvable pointer. **Build-2 owes the v0.16.0 CHANGELOG entry that this key renders from.** (5) `contract:64`''s canonical-home sentence was appended INLINE to the Layer-2 paragraph rather than added as a new paragraph, so that `:66`/`:68`/`:70`/`:190` keep their line numbers — the cycle has logged ten cite drifts and a gratuitous shift would have made eleven. **Line-cite drift found this build: ZERO new drift.** Every cite in the brief re-grounded at HEAD and HELD, including the five the brief had already corrected (`vlt-lint:32`, `:37`, `vlt-lint-full.js:515-517`/`:518`, `rule-card:11`, `contract:194`) — build-2''s brief inherits a clean cite set from this build''s file population. **Durability re-checked (F11 touches `vlt-upgrade`):** the B1 local-mint preserve path is UNTOUCHED — Step 1''s merge-not-replace registration (`:55`) and `mints_preserved` (`:100`) are byte-identical; F11 adds one report key and its prose only, no copy path, no overwrite path. No `.decision-log.md` anywhere in the tree. No version string bumped (build-2 is the release build, D3).

  VERIFICATION — real output, all five gating checks run at rest:

  V1/V2 package-lint (Group E = the handshake record; Group C carries C6): `uv run tools/package-lint.py` →
  `PASS group A — on-disk cruft / PASS group B — module-help.csv canon / PASS group C — resolvability + version agreement / SKIPPED group D — tag intent (no --expect-version) / PASS group E — self-description integrity / package-lint: A/B/C/E PASS, D SKIPPED — vlt 0.15.0`

  BIPARTITE, BOTH DIRECTIONS. Direction 1 (rosters): `extraction.md:11-12` → `version: 7` / `consumers: [vlt-extract, vlt-lint, vlt-track, vlt-query]`; `frontmatter.md:11-12` → `version: 13` (UNBUMPED) / `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch, vlt-setup, vlt-groom, vlt-query, vlt-lint-full.js]` (9 → 10); `write-verification.md:11-12` → `version: 3` / 5 consumers, untouched. Direction 2 (`grep -rn ''extraction@'' skills/` → exactly four hits, no strays): `vlt-extract/SKILL.md:4 ["extraction@7", "wiki-supersession@2", "frontmatter@13", "write-verification@3"]`; `vlt-query/SKILL.md:4 ["extraction@7", "frontmatter@13"]` (NEW — the skill carried no `depends_on:` at all); `vlt-track/SKILL.md:4 ["extraction@7", "wiki-supersession@2"]`; `vlt-lint/SKILL.md:4 [… "extraction@7" …]`. `grep -rln ''frontmatter@'' skills/` → exactly ten files, matching the ten-name roster. Every consumer listed ↔ every ack current, in both directions.

  C6 raw numbers (V9): `shasum -a 256 …/vault-operating-contract.md` → `670170b8f0f0d04f7e840b7f82b9b519623847115528d782f79c6361a84c6c97`; `vault-rule-card.md:11` `derived_from:` carries the same digest (re-derived twice — once after the F2/F8/F10 contract edits, once after deviation 2''s resolver clause). Card size `wc -c` → **7,106 B** against `RULE_CARD_BUDGET = 8,000` (`tools/package-lint.py:261`) — 894 B of headroom.

  V8 retirement grep battery, all seven run over `skills/`: `"two named surfaces\|never a third\|never open a third surface"` → **0**; `"outside those two surfaces\|outside the sanctioned surfaces"` → **0**; `"does not add an artifact write-path\|only through extraction"` → **0**; `"at least 2 contributing wiki pages\|≥2 contributing wiki pages"` → **0**; `"a thin wiki is a stop"` → **0**; `"writers:"` → extraction.md (2: prose + charter YAML), contract (2: hard rule + resolver), rule-card (2), checks.md, report.md, vlt-lint/SKILL.md, vlt-query/SKILL.md, vlt-upgrade/SKILL.md — schema + resolver + check + slot only, no stray restatement. **SURVIVAL CHECK (A19, the thing the room refused 4/4): `"excluded by name"` → `checks.md:18` PRESENT; `"carve-out by name"` → `contract:70` PRESENT.** The `{wiki}` carve-out survives at both sites.

  V3 — the gating instrument (A55 (b); A17''s ordinary-run constraint). One agent, handed the EDITED `vlt-lint/SKILL.md` Steps 0–2, the EDITED `checks.md` and `report.md`, `extraction.md@7` and the edited contract, asked to run an ORDINARY SCOPED `vlt-lint` — not to invoke a check — over the specified temp fixture tree (built in-session at `{fixture}`, never committed). Its returned Step-0 announcement: *"Scoped mode, timestamp 2026-08-24 00:00 … The selection covers both populations: the wiki page population = `resources/wiki/some-page.md` (1), and the PARA file population = the other 6, with the `{wiki}` subtree under `{resources}` dropped from it by name at selection time."* Report fence, verbatim in the `para_*` region:
  ```yaml
  mode: scoped
  scope_since: 2026-08-24 00:00
  files_checked: 7
  files_listed: 7
  flag_for_human:
    para_missing_attestation: []
    para_status_unknown: []
    para_type_unknown: []
    para_author_unknown: []
    para_writer_unauthorized: ["areas/health/notes/a-note.md: writers ''agent'' (author:) and ''vlt-agent-analyst'' (verified_by:) not in nearest declaring ancestor areas/health/charter.md writers: [human] — undeclared sub-container notes/ inherits; created 2026-08-25, post-adoption, loud"]
  ```
  **All four pass conditions met, negative control included.** (1) POPULATION SELECTED — the run reports on 6 files under `areas/`, `projects/` and `resources/`; before F0 it would have reported nothing there and the gate could not have seen its own hole. (2) `resources/briefs/2026-08-25-a-brief.md` **PASSES** — *"No ancestor container declares `writers:` … so the posture resolves `open`, which is an explicit pass, never a finding"* (A22''s pilot happy path). (3) **NEGATIVE CONTROL FIRED** — `areas/health/notes/a-note.md` **FAILS** with `para_writer_unauthorized`, on inheritance: *"the undeclared sub-container `notes/` inherits it, and the file''s two resolvable identities match neither"* (A23 implemented, not assumed). (4) `projects/thing/a-doc.md` PASSES (`agent` ∈ `writers:`); `resources/wiki/some-page.md` draws **no `para_*` finding of any kind** — *"removed from the `para_*` population by name at selection time"*, not by an in-check exception (it drew wiki-side findings instead, which is the correct population); `areas/health/record.md` draws **no `para_missing_attestation`** — the container carve-out at `checks.md:16` survives.

  V4 full-mode read-through: `full-scale.md` step 1''s predicate reads *"a key qualifies when its resolved value names a directory of walker-visible linkable notes — every directory-valued key except the wiki''s own (`wiki`), governance …, cold storage (`archive`), and report dirs"*, with *"a qualifying key''s glob excludes any subtree that is another mapped key''s home (concretely: `{wiki}` nests under `{resources}` by default)"* — the PARA keys with `{wiki}` carved out, exactly what full mode needs. F0''s added sentence POINTS at it (*"The same derived glob set is the SKILL''s full-mode PARA page set … the SKILL performs the `para_*` scan over that set itself; this workflow''s own page set is unchanged and stays `{wiki}`-only"*) and restates no predicate. V5 (R3): one finding class added, its legal response stated at its single home, never auto-fixed because `writers:` is human-gated; `checks.md:16`/`:17` legal responses unchanged; `:48`''s narrowing kept both flags'' responses (20 `Legal response` clauses, none dropped). V6 (R4): all four enumeration sites widened together — `SKILL.md:32` (scoped glob + the named exclusion), `:39` (full mode + the single-homed predicate pointer), `:41` (*"every PARA file"* defined), `:51-52` (step-sequence bullets), plus `full-scale.md:7`; the declared exclusion (the workflow''s `{wiki}`-only page set, disposition 4) is STATED, not silent. V7 (R2): N/A as briefed — no `package-lint` callable added, `CASE_FLOOR` untouched at 23, E4/E5/E6 all confirmed non-firing. V10 scrub: `git diff -- skills/` grepped for machine paths, the owner''s username and the field vault''s name → **0 hits**; the fixture tree is temp-only and uncommitted. V11: `find . -name ".decision-log.md"` → **0**.

  NOTHING NEEDS AN OWNER RULING. Both judgment calls (deviations 1 and 2) are recorded above; deviation 2 in particular is a resolver-semantics gap the brief could not have seen without running the instrument, and is exactly what A55 (b) bought.'
module_code: 'vlt'
created: '2026-08-25'
derives_from:
  - 'factory/inbox/2026-08-25-111322-para-location-is-used-as-a-proxy-for-trust.md (A12-3 — all seven steps: step 0 the para_* file-selection path, step 1 retire the ≥2-wiki-pages gate, step 2 entry condition = honest attested frontmatter, step 3 demote extraction to a disposition, step 4 vlt-query gains a PARA destination, step 5 writers: per container charter, step 6 the vlt-lint authorization check)'
  - 'factory/studies/ST-2-location-as-proxy-for-trust.md (RC-A — location as a proxy for trust; Package C selected; traps 4/6/7)'
  - 'factory/studies/ST-1-para-write-path-single-door.md (RC-B — one PARA verb fusing write permission to wiki provenance; C1/C2/C3/C5 re-derived, C4 shipped, C3 unbuilt and now partly discharged by step 4)'
  - 'factory/cycles/11-reachability/roadmap.md §carry-forward b2(2) (the released resources/-write legality watch — RETIRED into this build''s acceptance by Q9)'
roadmap: 'factory/cycles/12-proxy-claims/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-25): Q4 ALL SIX STEPS, ONE RELEASE (Package C''s implementation, not a menu) · Q5 C4 IS ALREADY SHIPPED — step 4 carries a one-line conformance clause, but A30 re-opens the REGIME · Q9 carry-forward b2(2) RETIRES into this build''s acceptance · Q11 undeclared containers are OPEN, and A22/A23 make it a resolver with inheritance · Q12 the MOC prohibition is NARROWED TO CONTENT TYPE (precedence by elimination, Arc 9 D5) · Q13 `_vault/` STAYS HUMAN-ONLY, no contract edit · D2 this build carries the cycle''s marquee retirement — the Layer-3 location prohibition · D3 ONE RELEASE, whole cycle (build-2 is the release build, not this one) · E5 the acceptance instrument is attached here, field half `[field-contingent]` and non-gating · owner rulings R-1 (step 0 added) and R-6/A19 (the `{wiki}` carve-out is NOT retired, 4/4) · roundtable amendments A17–A35 apply.'
risk: 'moderate — the cycle''s weight, and the only build this cycle that bumps a convention. `extraction.md` 6 → 7 with a FOUR-consumer walk (three re-acks + one new consumer, A26), an edit to `vault-operating-contract.md` that forces a `vault-rule-card.md` sha256 re-derivation under package-lint C6, a new lint finding class owing its legal response (R3), and the retirement of the module''s most-restated shipped prohibition across eleven sites. No release gate is at risk of a numeric budget (rule-card 6,957 B of 8,000; no fan-out schema touched), and steps 2 and 6 co-ship so no interim posture is owed.'
---

# Build #3 — the PARA posture

## Intent

PARA's boundary is declared as **authorship-honesty** and implemented as a **location
prohibition**. That gap was correct while the honest fields had nothing enforcing them.
Cycle 11's build-6 shipped that enforcement across the whole PARA population —
`para_missing_attestation` (named in `checks.md:16` as *"the **authorship-honesty net**"*),
`para_status_unknown`, `para_type_unknown`, `para_author_unknown` — and the proxy survived
beside it. This build retires the proxy and completes the mechanism that replaces it.

What lands, in seven steps (A12-3, ruled whole by Q4, step 0 added by owner ruling R-1):

0. **`vlt-lint` selects the PARA population.** Today nothing does — the marquee retirement's
   premise was false until R-1 fixed it (F0).
1. **The `≥2 wiki pages` gate retires**, four prose sites, no handshake (F1).
2. **The entry condition becomes honest, attested frontmatter** — contract, rule-card,
   and the false human-initiation premise inside `extraction.md` (F2, F3, F4).
3. **Extraction is demoted from *the* PARA verb to *a* PARA disposition** (F5).
4. **`vlt-query` gains a PARA destination**, with its provenance posture ruled (F6).
5. **`writers:` per container charter**, a total resolver with inheritance (F4, F7).
6. **`vlt-lint` gains the authorization check** the prohibition could never perform (F7).

Plus Q12's MOC narrowing (F8), the surface-count restatements step 4 falsifies (F9), A21's
single-homing of the `{wiki}` qualifier (F10), and A33's vault-facing notification (F11).

**All rejected alternatives in the parent filings, in `ST-1`/`ST-2`, and in the ideation
rulings are settled — do not re-litigate.** In particular: the six steps are **Package C's
implementation, not a menu** (Q4 — three of the cuts the capture's framing invited each walk
into a recorded `ST-2` trap); `vlt-extract` is **demoted, not retired** (the bottleneck is the
clause, not the skill); `_vault/` **stays human-only** (Q13); the MOC prohibition is
**narrowed, not folded into `writers:`** (Q12); **no relocation mechanism is built** — once
the destination is legal a migration is an ordinary owner request, and the discipline for
performing one already ships at `vlt-upgrade/SKILL.md:75` (Round 8); and above all —

> **Cycle 12 retires the Layer-3 location prohibition and does NOT retire the `{wiki}`
> carve-out.** (A19, owner-remitted and converged 4/4. Written in the roadmap's own words at
> the room's request so a later cycle does not re-file it as a missed retirement — which is
> precisely the fifth-pass failure A12-3 exists to stop. Falsifiers on record in the review.)

**`ST-1`'s two reverse-brainstormed hard constraints are honoured, in its own words.**
(1) *Enforcement ships in the same build as the rule* — steps 2 and 6 are in this build, so
B9-2's enforcement-ships-with-widening is satisfied **in fact**, not structurally (R-1 is what
made that true: without step 0 the check had no population). (2) *`extraction.md`'s invariants
are not touched* — **this build does not relax an invariant.** F4 corrects the *justification*
at `extraction.md:60` (a false human-initiation premise the module already contradicts in its
own shipped surface) and narrows the *stated population* of the hard invariant at `:36` to the
class it always meant. Relaxing `sources:` to solve a permission problem would trade the
invariant for the convenience; nothing here does that.

**The under-claimed argument for this change, recorded because it is the one `ST-1` supplies
and the filing does not.** `ST-1`'s R1 erosion loop is driven by agents falsifying `sources:`
**as the price of entry** — 57 files in the surveyed vault, the firewall *"already breached,
silently."* Once an honest `author: agent` / `trust: raw` write is legal, that entry price
disappears and the falsification pressure drops. This build defuses RC-B by removing the
motive, not by policing the symptom.

## Brief-time dispositions

Fifteen. Each cites the ruling or amendment that deferred it. **No owner was in the room; every
one of these is a judgment call made by the briefer and recorded here as its disposition.**

**1. A21 — the canonical home for the `{wiki}`-is-not-PARA qualifier is `vault-operating-contract.md:64`.**
Mary and Sally proposed `contract:64`; Quinn proposed `extraction.md:148`. The decider is
already on disk: **`extraction.md:82` explicitly points at the contract for this exact
material** — *"the write-surface grant lives in the operating contract's Layer 3 and hard rule
— mechanics there, never restated here."* A convention that already declares the contract the
home for the zone's mechanics cannot also be the home. And the rule the ten sites restate is a
**layer** fact (`{wiki}` is Layer 2, living inside a Layer-3 address), which is what
`contract:64` defines. *Quinn's position recorded as the dissent; his separating insight —
`extraction.md:148` answers **membership**, step 5 asks **posture** — is honoured by F10 leaving
`:148`'s membership sentence intact and pointing only its `{wiki}` qualifier at `:64`.*
**`checks.md:18` is exempt and keeps its self-contained population sentence** (ruled at the
roundtable, Sally over Quinn — B10-12's twelve `crossLayerSlugs` false positives are this
cycle's own evidence for what a check that resolves its population elsewhere costs).

**2. A31 — `writers:` does NOT bump `frontmatter.md`. No 13 → 14, no nine-consumer re-ack.**
Mary asked this be priced rather than assumed free, on the `grounding:` precedent (`b7193e8`
bumped both conventions for one charter field). Grounded, the precedent does not transfer:
`grounding:` is a **general** frontmatter field with its own section
(`frontmatter.md:86-94`) carried by *PARA artifacts and container charters*, so it genuinely
lived in both homes. `writers:` is **charter-only**, and `frontmatter.md:171` opens the PARA
section by disclaiming exactly this: *"Defined in `extraction.md` (the canonical reference;
**not duplicated here**). Summary:"*. **Consequence, binding on the builder: do not add a
`writers:` bullet to `frontmatter.md`'s summary list at `:173-177`.** Doing so would convert a
free change into `frontmatter.md` 13 → 14 plus nine re-acks for zero information — and the
convention already says it doesn't carry this.

**3. A29 — `moc` becomes readable, and it lands in `extraction.md` and `checks.md` only.**
Q12 keys an act-blocking rule on an axis no shipped field carries — A12-1's exact failure mode,
installed fresh by this cycle, and the amendment is right to refuse it. `moc` is added to
`extraction.md`'s artifact-type material (F4) — which is bumped anyway — and to
`para_type_unknown`'s recognized set at `checks.md:18` (F7), which is a skill reference and
carries no version. **`frontmatter.md:71` is deliberately NOT edited:** it says of itself *"The
`type:` list is **non-exhaustive.** Canonical values include …"* — a non-exhaustive list is not
the rule, `para_type_unknown`'s closed set is, and touching `frontmatter.md` re-opens
disposition 2's bump question for no gain. *(Single-home discipline: the closed set has one
home, `checks.md:18`; `extraction.md` carries the schema.)*

**4. A32 — step 0 and step 6 are implemented SKILL-side. `extraction.md` gains no fourth
consumer from them, and `vlt-lint-full.js:11` is not touched.** Winston asked where they land,
because if either reaches the workflow the build owes a fourth ack there. It does not, and the
workflow's own comment says why: `vlt-lint-full.js:515-517` already declares
`para_missing_attestation` *"a structural slot the SKILL fills from its own PARA jurisdiction
scan"* — the workflow sweeps `{wiki}`, and PARA is outside its page set **by design**. Step 0
therefore widens the **SKILL's** Step 0/1 selection (F0) and step 6 lands in the **SKILL's**
`checks.md` (F7). The workflow keeps its `{wiki}` population, its four empty `para_*` structural
slots, and its unchanged `depends_on:` pins at `:11`. *(This is also what keeps build-1's
just-shipped fan-out work untouched by build-3 — the two builds edit disjoint files.)*

**5. A55 — the gating instrument, ruled (b): a named agent-run reader protocol over a temp
fixture vault. Option (a) is impossible, not merely unattractive.** Amelia and Mary correctly
found that *"at rest on a fixture"* named a fixture nothing creates. Expressing the
authorization check as a `package-lint` callable so E4 forces a case **cannot work**: E4
introspects callables in `package-lint.py` (`tools/package-lint.py:857-877`, the
`^check_ / ^_e\d+_` regex), and the harness's `build_fixture` (`tools/test-package-lint.py:58`)
synthesizes a **module package** — `module.yaml`, the contract's pipe table, `CSV_ROWS`,
`FIXTURE_STRUCTURE`. It has no vault, no PARA container, no charter, no wiki page, and cannot
grow one without becoming a different harness. The authorization check is LLM-executed prose in
`checks.md`, and nothing in `tools/` executes `checks.md`. **So the instrument is named
concretely instead** — Verification 3 below, with its fixture tree, its inputs, its four pass
conditions, its **negative control**, and the evidence rule (the returned report fence recorded
verbatim in the BUILT `status:`). The precedent is build-1's Verification 3 reader probe, which
discharged an equivalent claim in this same cycle. **A55's fallback does not fire:** the gating
half keeps its `[ship-verifiable]` tag because it now names an instrument.

**6. A17/R-1 — the gating run is an ORDINARY `vlt-lint` invocation, scoped mode.** Winston's
constraint is the point of step 0: a fixture that invokes the check directly *"passes with the
file-selection path still missing — the gate cannot see its own hole."* The probe therefore
hands the agent the **edited SKILL.md Steps 0–2 and the references those steps route to**, and
asks it to run the skill, not the check. **Scoped mode** is chosen over full: full mode above
~30 pages delegates page-*finding* to the fan-out workflow (`full-scale.md:5`), which would put
the workflow between the probe and the answer for no benefit; the fixture is small, and step 0
widens **both** modes, so scoped exercises the same new selection path with less machinery.
*Full mode's PARA selection is covered by Verification 4's read-through against
`full-scale.md:7`, whose `crossLayerSlugs` derivation already globs the three PARA keys.*

**7. Q5 / A30 — the provenance posture for the class step 4 admits: NARROW THE INVARIANT'S
POPULATION (option ii), not exempt by `type:`.** A30 is correct that Q5 closed too early:
C4's *field* shipped (`sources:` wiki-only at `extraction.md:40`, `grounding:` at `:121`,
enforced by `method_in_grounding` at `checks.md:48`), but the *regime* was never relieved —
`extraction.md:36` states the hard invariant unconditionally, `:121` scopes `grounding:`
*against* it (*"never method"*), and `vlt-query/SKILL.md:10` says every significant claim cites
*"a wiki page **or research note**"*. Move the research notes into `grounding:` per Q5's clause
and every claim resting only on them fires **both** `method_in_grounding` and
`method_not_in_sources`. Ruling:

- **The hard invariant's population is stated as what it always meant: extracted artifacts.**
  `extraction.md:36` sits inside the personalized-extraction section and speaks of *"an
  extracted artifact"*; a `vlt-query`-filed document does not arrive by that verb. F4 states
  the population explicitly rather than leaving it to be inferred from a section boundary.
- **The new class is `author: agent`, `trust: raw`** — an unreviewed agent answer that makes
  **no** verified-provenance claim. `sources:` carries the wiki pages it drew on; `grounding:`
  carries the `{research}` notes and any external evidence (Q5's conformance clause, and
  Winston's carried qualification honoured: it is a **requirement**, not a routing note — an
  artifact that omits `grounding:` drops its provenance silently).
- **`checks.md:48`'s population is narrowed on a shipped field:** `method_in_grounding` and
  `method_not_in_sources` judge PARA files at **`trust: reviewed` or above**; a `trust: raw`
  file is outside them. This is **precedence by elimination** (Arc 9 D5) on an axis that already
  exists — the trust ladder at `extraction.md:53-60` reserves everything above `raw` to the
  Human and starts extracted artifacts at `reviewed`, so the two populations cut cleanly apart
  with no new schema and no precedence statement.
- **This is `ST-1`'s C3 arriving** — *a second verb owning the non-wiki-derived artifact* —
  which A30 correctly records as unbuilt. It is not built whole here (no new skill); step 4
  gives the existing second verb a legal destination and an honest provenance rule.
- *Considered and recorded: this makes `trust: raw` a nominal dodge around the firewall. It is
  not a new hole. `raw` is the ladder's bottom rung and the only agent-settable one; anything
  claiming to be an extraction must carry `trust: reviewed`, which is human-set
  (`extraction.md:56`). A18's point — the nets judge presence and enum membership, never truth —
  is true of the shipped system today and is not worsened here. `ST-1`'s C5 (lint catches
  non-wiki `sources:` entries) remains unbuilt and is filed as out-of-scope item 3.*

**8. A34 — the confidentiality-as-container-attribute DECLINE stands; its WATCH is
RE-POINTED.** Sally is right that Q11 is retroactive and that E4 re-carried this pair
*"untouched, not re-graded"* in the same session Q11 inverted its default posture. Re-graded
against the world this build creates: **the DECLINE's premise — "the module has no field for
it" — is the half that changed.** `writers:` is precisely a declarable container attribute on
the write axis, human-gated on the charter, and a human who wants a container closed can now
say so mechanically (`writers: [human]`) instead of in prose nothing reads. That is a *better*
answer than a confidentiality field for this axis, and it ships here. What genuinely remains is
the **transition**: every charter that exists today is undeclared by construction and becomes
`open` on upgrade, silently — which is exactly what A33's `governance_rule_changes:` key (F11)
exists to make loud. **Disposition: DECLINE stands, unchanged; the watch is re-pointed** at
whether a vault, on discovering the new posture through its post-flight report, declares
`writers:` on a container it had framed in prose (acceptance check 9). **Maya's dissent is
preserved, not converted to a bound debt** — the repatriation and leak-pressure arguments it
records are about *confidentiality as a content property*, which `writers:` does not answer and
this build does not claim to. The propagation-debt half of the pair is untouched by A12-3 and
is re-carried unchanged.

**9. A35 — `{archive}`: `writers:` travels with an archived container as inert text; the
resolver never runs there.** Quinn is right that the resolver makes the question askable for
the first time. The answer is already determined by two shipped sentences: a `closed`/`retired`
container archives **whole** to `{archive}` mirroring its source path (`contract:70`, `:72`),
so the charter — and its `writers:` — travels; and the `para_*` population is *"files under
`{projects}`, `{areas}`, and `{resources}`"* (`checks.md:18`), which `{archive}` is not.
`full-scale.md:7` independently excludes `archive` as cold storage. **No edit is owed**, and
F7's check text must not grow an `{archive}` clause — its population sentence already excludes
it. *Recorded so a later reader does not mistake the silence for an oversight.*

**10. Interim posture (R1) — substantive, and it is about retroactivity, not sequencing.**
The *rule ahead of mechanism* hazard does not arise: steps 2 and 6 are in **one build**, so
there is no window in which writes are legal and authorization uncheckable (Q4, the grouping,
B9-2 satisfied in fact per R-1). But Q11 **is** retroactive, and the window it opens is real:
**between the upgrade landing and a vault declaring `writers:` on anything, every existing PARA
container resolves to `open`.** What a vault legally does in that window: honest, attested
`author: agent` / `trust: raw` writes are legal anywhere in `{projects}`/`{areas}`/`{resources}`
outside `{wiki}`; the protection is the honesty nets plus step 6's check, not the declaration;
nothing above `trust: raw` is agent-settable; MOCs stay untouchable by content type (F8); and
`{wiki}` is removed at population time, not by an exception (A22). The window is **announced**,
not silent — that is F11's whole job. *This is the honest statement of the change's moment of
discovery, and it is stated here rather than found at acceptance.*

**11. Retirement disposition (P-15's required clause) — five retirements and one refusal.**
This build ships enforcement, so the clause is substantive. Named, with sites re-derived at
HEAD:

| # | prohibition retired or narrowed | site(s) at HEAD | F-site | pre-named / beat-produced |
|---|---|---|---|---|
| 1 | **The Layer-3 location prohibition** — *"partners never create, rewrite, or delete human-curated PARA content outside those two surfaces"* | `vault-operating-contract.md:68`; `vault-rule-card.md:26` | F2, F3 | **pre-named** (D2) |
| 2 | **The surface-count prohibition** — *"exactly **two named surfaces** … never a third"*, which step 4 literally falsifies by adding a third | `vault-operating-contract.md:66`; `vlt-extract/SKILL.md:13`; `vlt-review-council/SKILL.md:51`; `vlt-agent-creative/SKILL.md:14`; `vlt-upgrade/SKILL.md:159`; `vault-rule-card.md:26` | F2, F3, F9 | **beat-produced** (A25, the session's most-converged finding) |
| 3 | **`extraction.md:45`** — *"This does not add an artifact write-path. Artifacts reach PARA **only** through extraction"*, inside the very convention this build bumps | `extraction.md:45` | F4 | **beat-produced** |
| 4 | **`checks.md:16`'s rationale** — *"outside the sanctioned surfaces"*, the retired frame restated **inside the enforcement that replaces it** | `checks.md:16` | F12 | **beat-produced** |
| 5 | **The `≥2 wiki pages` gate**, 4 sites | `vlt-extract/SKILL.md:38`, `:118`; `vlt-agent-creative/SKILL.md:37`, `:14` | F1 | pre-named as scope (*Quinn's dissent recorded: not an obsolescence finding — prose-only ceremony with no mechanism ever behind it; retired because it never earned its place*) |
| — | **REFUSED: the `{wiki}` carve-out** (`contract:70`, `checks.md:18`) — it is D5 elimination's **output**, not an overlap awaiting one; under Q11 it is a **lock**, not friction | not edited | A19 | **refused, 4/4** |

**All five retire or narrow together, or the prohibition survives in prose** (A25). The builder
must not land steps 2/4 and leave any row of this table standing.

**12. The MOC prohibition survives, narrowed (Q12) — and its narrowing is elimination, not
precedence.** After step 5 a container declares `writers:` and a MOC lives in a container, so
two rules would address one file. D5 says narrow one population so the overlap ceases to exist.
Keying `:190` on **content type** does that: partners never edit a MOC *because MOC links are
human endorsement*, **regardless of the container's `writers:` posture**. *Considered and
rejected at ideation, not re-opened here: folding MOCs into `writers:` and retiring `:190` —
unlike the location proxy, no shipped field carries the endorsement claim, so the fold would
make human endorsement a per-vault setting with nothing behind it.* A29's `moc` type is what
makes the narrowed rule decidable (disposition 3).

**13. A28 — the rule-card's write-boundary line becomes a TEST, not a list, and it fits.**
Paige and Sally are right that `:26` is a closed enumeration and that after step 5 posture is
per-container-declared, which the card cannot enumerate. Priced: the card is **6,957 bytes**
against `RULE_CARD_BUDGET = 8,000` (`tools/package-lint.py:261`) — **1,043 bytes of headroom**,
and the rewrite is expected to be net-shorter (a test is shorter than an enumeration). No
budget risk. The test form is specified in F3.

**14. `vlt-upgrade:159` and `vlt-review-council:51` are NARROWED, not deleted.** Both are
op-specific self-restrictions that happen to be phrased as restatements of the retired rule.
`vlt-upgrade` is not an authoring partner and must not gain a PARA write surface; the review
council files back through the Librarian. Each keeps its restriction and loses the retired
frame (F9) — the alternative (deleting them) would quietly grant two ops a write surface
nobody ruled.

**15. R4 / enumeration widening — substantive, and it is step 0.** The class this build adds a
member to is `vlt-lint`'s **selected file population**, enumerated in three router-only places
(`SKILL.md:23-41`, `:43-45`, `:49-50`) and once more in the fan-out's page-list discovery
(`full-scale.md:7`). All four are widened in this build (F0). **No new shipped file is created**,
so no manifest, vital, or always-loaded enumeration gains a member; `module-help.csv` and
`marketplace.json` are untouched (§5). *Declared exclusion, per the rule: the fan-out workflow's
own page set stays `{wiki}`-only by design (disposition 4) — that is not a silent omission but
the standing division of labour stated at `vlt-lint-full.js:515-517`.*

## F0 — `vlt-lint` selects the PARA population (step 0, owner ruling R-1)

**⚠ This F-site exists because a capture claim was false, and it is the reason the marquee
retirement is honest.** The capture grounded the four `para_*` check *definitions* and never
asked whether anything selects their population. Nothing does.

**Current state (re-derived at HEAD).**

- `skills/vlt-lint/SKILL.md:19-41` — **Step 0: Determine scope.** Scoped mode globs
  `find {wiki} {research} {sessions} -type f -name "*.md" -newermt …` at **`:32`** *(the
  roadmap and A17 cite `:33`; at HEAD the `find` line is `:32` — the cite is inside a fenced
  block at `:31-33`. **Grounding correction, cite-only.**)*
- `skills/vlt-lint/SKILL.md:37` — full mode: *"Read every page in `{wiki}` (and `{research}`
  for deeper checks)."* *(A17 cites `:39`; at HEAD `:39` is the "every wiki page" definition
  line and the full-mode sentence is `:37`. **Grounding correction, cite-only.**)*
- `skills/vlt-lint/SKILL.md:49-50` — the step-sequence restatement of both.
- `grep -c "PARA\|para_" skills/vlt-lint/SKILL.md` → **0.** Confirmed at HEAD.
- `skills/vlt-setup/assets/workflows/vlt-lint-full.js:515-518` — the workflow states the
  division of labour and the hole in one comment: *"PARA files are outside this workflow's page
  set (it sweeps `{wiki}`) — `para_missing_attestation` is a structural slot **the SKILL fills
  from its own PARA jurisdiction scan**; it is emitted here so the report shape is complete."*
  *(A17 cites `:517-519`; build-1's two deletions shifted this by 2 — comment `:515-517`, slot
  `:518`. **Grounding correction, cite-only — the fifth line-cite drift this cycle has logged.**)*
- `skills/vlt-lint/references/report.md:31, :35, :36, :37` — **four** `para_*` report slots,
  all with no producer. Confirmed at HEAD.
- `skills/vlt-lint/references/full-scale.md:7` — the fan-out's page-list discovery already
  derives a glob set over the PARA keys for `crossLayerSlugs` (every directory-valued
  `vault_structure` key except wiki/governance/archive/report dirs, with nested mapped keys
  carved out). **The selection predicate this step needs already exists here, single-homed.**

**The exact change.**

1. **`SKILL.md` Step 0 (scoped), at the `:31-33` fenced block.** Add the PARA reach to the
   scope glob, keeping the same mtime predicate:
   `find {wiki} {research} {sessions} {projects} {areas} {resources} -type f -name "*.md" -newermt "…"`,
   with a following sentence stating the one exclusion by name: **the `{wiki}` subtree under
   `{resources}` is removed at selection time — it is the Layer-2 Librarian-only zone and its
   pages are the wiki page population** (pointer to `contract:64` per F10; A22's *"removed at
   **population** time, never by an exception inside the check"*).
2. **`SKILL.md` Step 0 (full), at `:37`.** Full mode reads every page in `{wiki}` **and every
   file under `{projects}`/`{areas}`/`{resources}` outside the `{wiki}` subtree** — the PARA
   page set. State that at scale the PARA set is derived by the **same predicate already
   single-homed at `full-scale.md:7`**; do not restate the predicate here (single-home
   discipline).
3. **`SKILL.md:39`** — the *"every wiki page"* definition sentence gains its sibling: what
   *"every PARA file"* means in each mode.
4. **`SKILL.md:49-50`** — the step-sequence bullets updated to match, so the router's own
   summary does not contradict the steps.
5. **`full-scale.md:7`** — one added sentence: the PARA glob set it already derives for
   `crossLayerSlugs` is **also** the full-mode PARA page set the SKILL scans for `para_*`; the
   SKILL performs that scan itself (the workflow's page set is unchanged). No new predicate.

**Why.** Owner ruling R-1: *"Enforcement now genuinely ships with the widening — B9-2 satisfied
in fact, not merely structurally."* Without this, step 6 ships a check against a population
nothing selects, and E5's gating half would pass on a fixture while the hole stayed open.

**Out of scope at this site.** The workflow's page set is **not** widened (disposition 4). The
four structural `para_*` slots in `vlt-lint-full.js` stay empty and stay where they are.

## F1 — the `≥2 wiki pages` gate retires (step 1)

**Current state (re-derived at HEAD — four sites, one more than the capture's three).**

| site | text |
|---|---|
| `skills/vlt-extract/SKILL.md:38` | *"**Hard gate:** extraction requires **at least 2 contributing wiki pages.** If only one (or none) covers the topic, **stop** …"* |
| `skills/vlt-extract/SKILL.md:118` | *"**A thin wiki is a stop, not a caveat.** Fewer than two pages → offer a wiki pass or a direct link…"* |
| `skills/vlt-agent-creative/SKILL.md:37` | *"The hard gate (≥2 contributing wiki pages) is a feature: a thin topic is a cue to send the user to the Librarian or Researcher first…"* |
| `skills/vlt-agent-creative/SKILL.md:14` | *"…you do not invent knowledge to fill a gap: **a thin wiki is a stop**, not a thing to paper over."* |

**Grounding — A24 confirmed in all three parts, verbatim at HEAD.** (i) the gate has **four**
sites, not three; (ii) `vlt-agent-creative:14` is a *wiki-grounding provenance* statement, so
citing it as a PARA **location** rule is a mis-cite — but it is a genuine **thin-wiki gate**
site and (F9) a genuine **surface-count** site; (iii) `vlt-agent-creative:37` is a *different
line* from `:14` — *"a brief that reads the bullet linearly retires the wrong line."*

**The exact change.** All four lose the **hard stop**. A thin wiki becomes a **caveat the skill
surfaces**, not a refusal: `vlt-extract` offers the wiki pass and names it as the better path,
then proceeds if the user asks; `vlt-agent-creative:37` keeps the *cue* and drops the *feature*
framing. **`vlt-agent-creative:14`'s provenance sentence stays** — *"every non-trivial claim
cites the wiki page it came from"* is the grounding rule, not the gate; only its
*"a thin wiki is a stop"* clause changes to the caveat form.

**Why.** The gate is the location proxy's enforcement arm at the extraction door: it exists to
keep thin agent synthesis out of PARA, which is now the honesty nets' job. Confirmed prose-only
— **no handshake cost**: grepped across the governance bundle and every `vlt-lint` check
reference, the gate appears in **no convention and no check**.

## F2 — the contract's Layer-3 entry condition and hard rule (step 2)

**Current state (re-derived at HEAD, all cites HOLD).**
`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`

- **`:66` (Layer 3)** — declares the boundary as authorship-honesty *"and partner-touched
  content reaches it through exactly **two named surfaces** — **extraction** … and **container
  maintenance** …"*, closing with *"Charters are human-gated: partner-drafted at most,
  human-ratified (`author: hybrid`)."*
- **`:68` (The hard rule)** — implements it as a location prohibition: *"…and nothing else in
  PARA: partners never create, rewrite, or delete human-curated PARA content outside those two
  surfaces. `sources/` is read-only. Human zones (`_vault/`, `new/`, `daily/`) are human-only."*
- **`:62`** Layer 1 read-only, **`:64`** Layer 2 (the `{wiki}` Librarian-only floor — **already
  shipped**, see F4 disposition), **`:70`** the container model + the `{wiki}` carve-out by
  name, **`:76-80`** the three human zones. All unchanged by this build except as stated.

**The exact change at `:66`.** The two-named-surfaces enumeration is replaced by the **entry
condition**: partner-touched content reaches Layer 3 by carrying **honest, attested
frontmatter** — an honest `author:` (`human | agent | hybrid`), a `trust:` rung the writer is
entitled to set (agents set `raw` and nothing above it — `extraction.md`'s trust ladder), a
recognized `type:`, and the write-verification attestation pair. Extraction and container
maintenance are named as **dispositions** — the two the module ships — not as the closed set.
Charter human-gating is **unchanged**.

**The exact change at `:68`.** The location prohibition is replaced by the **write-posture
resolver** (A22, and it is load-bearing — step 6 cannot be written without it):

> Write posture at any PARA path is the `writers:` of its **nearest declaring ancestor
> container**; where no ancestor declares, **`open`** — and `open` is a **PASS, never a
> finding**. A declared posture **binds its sub-containers**: an undeclared sub-container
> beneath a declaring parent **inherits** the parent's `writers:` and does not default to
> `open` (A23 — *"the alternative makes any closed posture unenforceable one directory
> down"*). The `{wiki}` subtree is **removed at population time**, never by an exception
> inside the resolver: it is the Layer-2 Librarian-only zone (`:64`), outside the declaration
> system rather than absent from it.

Everything else on `:68` **survives verbatim**: `sources/` read-only, human zones human-only
(Q13 — `_vault/` stays, no edit), and the `_agent/`/`_meta/`/`{wiki}` write grant.

**Retirements landing here:** row 1 (the location prohibition, `:68`) and row 2's contract site
(the surface-count enumeration, `:66`) of disposition 11's table.

**Out of scope at this site.** `:62`, `:70`, `:72`, `:76-80` are not edited (Q13; A19 — the
carve-out at `:70` stays). `:64` gains only F10's canonical-home sentence — its Librarian-only
floor is **already shipped** and is not re-authored.

## F3 — the rule-card: a test, not a list — and its hash (step 2, A27/A28)

**Current state (re-derived at HEAD).**
`skills/vlt-setup/assets/governance/_meta/vault-rule-card.md`

- **`:11`** — `derived_from: 'vault-operating-contract.md sha256:57df3488…3666 (derived 2026-08-24)'`.
  *(A27 cites `:10`; at HEAD the key is on **`:11`**. **Grounding correction, cite-only.**)*
  **Verified this session:** `shasum -a 256` of the shipped contract returns
  `57df3488f721c98188ed1e05f11324639fdd80431d5a1f014b8f4345327b3666` — the card's claim is
  **true today**, which is exactly why editing the contract without re-deriving it would make
  the card carry *a verifiable, false derivation claim, in the cycle about exactly that.*
- **`:26` (Write boundaries)** — the act-blocking closed enumeration: *"PARA (`{projects}`,
  `{areas}`, `{resources}` outside its `{wiki}` subtree) is human-curated, its boundary
  authorship-honesty — partners reach it through exactly two named surfaces … **never a
  third**"*.
- **`:27`** — Single-writer wiki (**not edited**; A19). **`:28`** — the MOC prohibition (F8).
- Card size: **6,957 bytes** against `RULE_CARD_BUDGET = 8,000` (`tools/package-lint.py:261`).

**The exact change.**

1. **`:26` is rewritten as a decidable test** (A28), not a list — because after step 5 posture
   is per-container-declared and the card cannot enumerate what each vault declares:
   > **Write boundaries.** Write only to `_agent/`, `_meta/`, and `{wiki}` (Librarian-only).
   > `sources/` and the human zones (`_vault/`, `new/`, `daily/`) are closed. In PARA
   > (`{projects}`, `{areas}`, `{resources}` outside `{wiki}`): **you may write iff (a) your
   > frontmatter is honest and attested — real `author:`, a `trust:` rung you are entitled to
   > set, recognized `type:`, attestation pair — and (b) the nearest declaring ancestor
   > container's `writers:` admits you, or none declares.** → *The three layers and the hard
   > write boundaries*
   The card stays a line, not the mechanics; the contract remains the home.
2. **`:11`'s `derived_from:` sha256 is re-derived** against the edited contract in the **same
   build**, with the `(derived <date>)` stamp updated.

**Why.** `contract:194` — *"Every partner, on activation, **first loads the rule-card**"* —
makes this the most load-bearing restatement site in the module *(the capture called it "the
most load-bearing of all"; it cites `:192`, which at HEAD is `:194` — **grounding correction,
cite-only**)*. And package-lint **C6** (`tools/package-lint.py:330-346`) fails the release on a
stale hash or an over-budget card, so a missed re-derivation blocks the tag rather than
shipping a lie.

## F4 — `extraction.md` 6 → 7 (steps 2 + 5, and the retirement at `:45`)

**This is the build's only convention rule change. The version-handshake applies in full** —
see §5 Registration for the consumer walk, which is where the acks are named.

**Current state (re-derived at HEAD).**
`skills/vlt-setup/assets/governance/_meta/conventions/extraction.md`

| line | text | disposition |
|---|---|---|
| `:11` | `version: 6` | **→ 7** |
| `:12` | `consumers: [vlt-extract, vlt-lint, vlt-track]` | **→ `[vlt-extract, vlt-lint, vlt-track, vlt-query]`** (A26) |
| `:36` | the hard invariant — *"Every general or method claim in the body still traces to a wiki page listed in `sources:` … the amendment does not touch it."* | **population stated** (disposition 7) — not relaxed |
| `:40` | *"`sources:` continues to list **only wiki pages**"* | unchanged (C4, shipped) |
| `:45` | *"**This does not add an artifact write-path.** Artifacts reach PARA **only** through extraction…"* | **RETIRED** (disposition 11, row 3) |
| `:47` | names **`vlt-track`** as the one module-shipped op sanctioned for personalized extraction | unchanged — but it is the evidence for the `:60` correction |
| `:53-60` | the trust ladder; `reviewed`/`verified`/`canonical` are **Human**-set, only `raw` is agent-set | unchanged — load-bearing for disposition 7 |
| `:60` | *"the act of extraction is a human-initiated curation step"* | **CORRECTED** |
| `:107-113` | per-type artifact `status:` enums (`project`/`area`/`resource`) | **gains `moc`** (disposition 3) |
| `:121` | `grounding:` — *"never method"* | scoped by disposition 7's narrowing |
| `:146-181` | **PARA containers** — `:150` charter, `:152-164` the charter YAML block, `:166-171` container status enums, `:181` the attestation carve-out | **gains `writers:`** |
| `:148` | *"membership and containment are answered by location"* | membership sentence unchanged (F10 touches only its `{wiki}` qualifier) |

**The exact changes.**

1. **`:11` → `version: 7`; `:12` gains `vlt-query`.**
2. **`:60` — the false premise is corrected.** *"the act of extraction is a human-initiated
   curation step"* is contradicted by the module's own shipped surface: `:47` names `vlt-track`
   as the sanctioned personalized-extraction op and `vlt-track` runs on a longitudinal loop.
   Replace the justification with the true one: extracted artifacts enter at `trust: reviewed`
   because **the trust ladder reserves that rung to the Human** (`:56`) and extraction is a
   *curation* disposition whose output the human is expected to have asked for — **not** because
   a human necessarily initiated the act. **This is a correction of a *justification*, not a
   relaxation of an *invariant*** — `ST-1`'s second hard constraint, honoured in its own words.
3. **`:36` states its population.** The hard invariant governs **extracted artifacts** — the
   class that arrives by the extraction verb and enters at `trust: reviewed`. Files at
   `trust: raw` make no verified-provenance claim and are outside it (disposition 7).
4. **`:45` retires.** *"This does not add an artifact write-path. Artifacts reach PARA **only**
   through extraction"* is false the moment step 4 lands. It is replaced by the honest statement
   of what the section does say: the **container maintenance surface** is a distinct
   disposition with its own shape (the sentence's surviving half), and extraction is **one**
   artifact disposition among the module's shipped set, not the only one.
5. **`writers:` joins the charter schema** at `:152-164`, as an **optional** commented key in
   the YAML block beside `grounding:`, plus a prose paragraph after `:150` defining it:
   - Shape: a flat list of writer identities — `human`, `agent`, or a specific partner slug —
     following `frontmatter.md` YAML rule 3/4 idiom. Absent = **undeclared**.
   - Semantics (single home, the contract points here for the schema and this points at
     `contract:68` for the resolver — **mechanics in one place**): the resolver, inheritance,
     and the `open` default live at `contract:68` (F2); this convention defines the **field**.
   - **Human-gated**, because it lives on `charter.md` (`:150`, `contract:66`) — partner-drafted
     at most, human-ratified. A partner may propose `writers:`; it may not ratify one.
   - **Not added to `frontmatter.md`** (disposition 2).
6. **`moc` becomes a readable artifact type** (disposition 3): added to the per-type
   `status:` enum table at `:109-113` with the **unbounded** enum `ongoing | retired` (a MOC is
   a curated index, not bounded work — the `area`/`resource` axis), and named in the type
   material alongside `project|area|resource`. This is what makes Q12's narrowed MOC rule
   decidable by a shipped field.

**Why.** Steps 2 and 5 both land here; the bump is **shared, not doubled** (the filing's own
step 2 already budgeted it). `writers:` is **new schema** — `grep -rn "writers:" skills/` → **0
hits at HEAD**, confirming the PROVENANCE SHARPENING in the capture: the container model and
charter human-gating shipped with B10-10, the key did not.

**Out of scope at this site.** `:40`, `:41`, `:43`, `:82`, `:148`'s membership sentence, and the
container `status:` enums at `:166-171` are not changed. `frontmatter.md` is not edited at all
(disposition 2 — its `consumers:` list is a §5 matter, not a rule edit).

## F5 — extraction demoted to a disposition (step 3)

**Current state (re-derived at HEAD).**

- `skills/vlt-extract/SKILL.md:13` — *"PARA is the human-curated layer, its boundary drawn by
  authorship-honesty; **extraction is the sanctioned artifact path into it** (the operating
  contract's Layer 3 names one other surface — container maintenance appends — which is not
  this skill's)…"*
- `skills/vlt-agent-creative/SKILL.md:37` — *"Run `vlt-extract`. This is your primary work and
  your sanctioned write into PARA."*

**The exact change.** `vlt-extract:13` states extraction as **a** disposition — the one that
turns accumulated wiki knowledge into a curated artifact entering at `author: hybrid` /
`trust: reviewed` — and points at `contract:66` for the entry condition rather than claiming
the monopoly. `vlt-agent-creative:37` keeps *"your primary work"* (true) and drops
*"**the** sanctioned write into PARA"* (false after step 4).

**Why.** The bottleneck is the clause, not the skill — **retirement of `vlt-extract` was
considered and rejected in the filing**, and `ST-2` records the demotion as the settled owner
ruling. This F-site is the demotion; F9 is the surface-count cleanup that rides with it.

## F6 — `vlt-query` gains a PARA destination (step 4)

**Current state (re-derived at HEAD).**

- `skills/vlt-query/SKILL.md:1-4` — frontmatter carries `name:` and `description:` and **no
  `depends_on:` at all** (A26 confirmed; `grep -c depends_on skills/vlt-query/SKILL.md` → 0).
- `:10` — *"Every significant claim cites a wiki page **or research note**."*
- `:46` — *"**A one-off investigation answer** → write a `{research}/YYYY-MM-DD-HHmmss-<slug>.md`
  note directly. Frontmatter per `{conventions}/frontmatter.md`: `type: research`, `created`,
  `title`, `author: agent`, `trust: raw`, `topic`, `status: complete`, `sources:` (the pages/notes
  consulted)…"* — it files to `{research}` **only because that is the sole legal home** for a raw
  agent-authored document.

**The exact change.**

1. **`:46` gains a PARA disposition** beside the `{research}` one: an answer the user wants to
   **keep as reference material** may be filed into PARA — `{projects}/`, `{areas}/`, or
   `{resources}/` (outside `{wiki}`), at the container the user names or loose at a layer root —
   carrying `author: agent`, `trust: raw`, a recognized `type:`, the attestation pair, and:
   - **`sources:` — wiki pages only** (the shipped C4 rule, `extraction.md:40`).
   - **`grounding:` — required, not optional, for this class**: the `{research}` notes and any
     external evidence the answer rested on (Q5's conformance clause; Winston's carried
     qualification — an artifact that *omits* `grounding:` drops its provenance silently, and
     `method_in_grounding` fires only on files that carry it).
   - **No relabeling, no pointer-container indirection, no bespoke carve-out** — it is filed as
     what it is (E5's own acceptance condition).
2. **`:10` is made consistent with the segregation rule**: a significant claim cites a wiki page
   in `sources:`; a research note or external reference is cited in `grounding:`. Same claims,
   correct fields.
3. **`depends_on: ["extraction@7", "frontmatter@13"]` is added to the frontmatter at `:3`**
   (A26), and `vlt-query` is added to **`extraction.md:12`** and **`frontmatter.md:12`**'s
   `consumers:` lists (9 → 10 for frontmatter). See §5.

**Why.** Q4: dropping step 4 kills the acceptance instrument — *"`trust: raw` is currently
unrepresentable in PARA; if no `raw` content appears there after the change, it did not take"*
needs a **producer**. And A26 is the reason this is a registration change, not just prose:
`frontmatter.md:12`'s nine consumers omit `vlt-query`, which carries no ack at all — **E1
derives from declared consumers both ways and E3 fires only on a literal `name@version` token,
so an undeclared consumer is invisible to every gate.**

**Out of scope at this site.** No new skill is created; `ST-1`'s C3 (a second verb as its own
skill) is not built — step 4 gives the existing verb a legal destination and an honest
provenance rule, which is the part this cycle ruled.

## F7 — the authorization check (step 6) and the `para_*` population

**Current state (re-derived at HEAD).**
`skills/vlt-lint/references/checks.md`

- **`:16`** — attestation findings; `para_missing_attestation` described as *"the
  **authorship-honesty net** — it catches unstamped, unattested artifact-shaped agent writes
  reaching the layer **outside the sanctioned surfaces**"*, with the container-files population
  carve-out. *(The rationale clause is retired at F12.)*
- **`:17`** — `para_status_unknown`. **`:18`** — the `para_*` population sentence (*"files under
  `{projects}`, `{areas}`, and `{resources}` — with the `{wiki}` subtree under `{resources}`
  **excluded by name, never by location**"*) plus the two closing nets `para_type_unknown`
  (**closed recognized set**, no `moc`) and `para_author_unknown`. **Exempt from F10** — it keeps
  its self-contained population sentence (A21, ruled).
- **`:48`** — the personalized-extraction firewall: `method_not_in_sources` and
  `method_in_grounding`, firing on *"each extracted artifact carrying `personalization_sources:`,
  and each PARA artifact or container charter carrying `grounding:`"*.
- `skills/vlt-lint/references/report.md:31, :35, :36, :37` — the four `para_*` slots.

**The exact change.**

1. **A new governance check, `para_writer_unauthorized`**, as a bullet in the `para_*` group
   immediately after `:18`, stating **the resolution order explicitly** (A22 — without it the
   check has nothing to join for `{resources}/briefs/`, E5's own field pilot population, and
   *"this is the pilot's happy path, not a corner case"*):
   > For each file in the `para_*` population, resolve the write posture: walk **up** to the
   > **nearest declaring ancestor container** (a directory carrying a `charter.md` with
   > `writers:`) and join the file's writer identity — `author:` for `human`/`agent`, the
   > attestation `verified_by:` for a partner slug — against that `writers:` list. **If no
   > ancestor declares, the posture is `open` and the file PASSES** — never a finding. A
   > declaring ancestor **binds every sub-container beneath it** (A23), declaring or not.
   > `{wiki}` is not in the population (`:18`) and is never handled as an exception here.
   > Informational for files whose `created` predates convention adoption, loud after — the
   > standing `para_*` posture.
   > **Legal response (R3):** the human ratifies a `writers:` change on the container's
   > charter, or the write is relocated to a container that admits its writer, or the human
   > rules the file human-authored. **Never auto-fixed** — `writers:` is human-gated, so a
   > partner may propose the charter edit and may not make it.
2. **`:18`'s `para_type_unknown` recognized set gains `moc`** (disposition 3): the artifact
   types become `project|area|resource|moc`, container types unchanged.
3. **`:48`'s population is narrowed** (disposition 7): `method_not_in_sources` and
   `method_in_grounding` judge PARA files at **`trust: reviewed` or above**; `trust: raw` files
   are outside them. State the reason in one clause — a `raw` file makes no verified-provenance
   claim, so there is no firewall to breach — so a later reader does not read the narrowing as
   a loosening.
4. **`report.md` gains one slot**, matching the four existing `para_*` lines' shape:
   `para_writer_unauthorized: [<para-file: writer 'X' not in nearest declaring ancestor's writers: [...] — informational where created predates convention adoption>, ...]`
   placed with the other `para_*` slots at `:31-37`, under `flag_for_human` (governance findings
   are never auto-fixed — `SKILL.md:58`).

**Why.** This is the enforcement a prohibition cannot perform: a location rule can only say
*where*, and the question is *who*. It is what makes step 2 safe to ship in the same build.

**Out of scope at this site.** `:16`'s attestation mechanics, the container-files carve-out, and
`:18`'s `{wiki}` exclusion sentence are **not** changed (A19, A21's exemption). No `{archive}`
clause is added (disposition 9). The workflow emits no new slot (disposition 4) — the SKILL
fills this one from its own scan, exactly as it does `para_missing_attestation`.

## F8 — the MOC prohibition, narrowed to content type (Q12)

**Current state (re-derived at HEAD).**

- `vault-operating-contract.md:190` — *"**Partners never edit Maps of Content (MOCs).** MOC
  links represent human curation and endorsement; only the human adds links to a MOC. MOCs live
  in PARA folders, never in `_agent/`."* (Section *Wikilinks and MOCs*, `:187`.)
- `vault-rule-card.md:28` — *"**MOC prohibition.** Never edit a Map of Content — MOC links are
  human curation and endorsement."* *(The capture cites the card's MOC line implicitly; at HEAD
  it is `:28`.)*
- `extraction.md:60` — *"MOCs only link artifacts at `canonical`"*; `canonical` is Human-set
  (`:58`, `frontmatter.md:69`).

**The exact change.** `:190` is restated as a rule about **MOCs as a content type**: partners
never edit a MOC — identified by `type: moc` (F4) — because MOC links are human endorsement,
**regardless of the container's `writers:` posture**. The card's `:28` gains the same
`regardless of posture` clause in card form. `extraction.md:60`'s canonical-linkage sentence is
untouched.

**Why.** Precedence by elimination (disposition 12). Leaving `:190` unchanged is the branch that
would later require a precedence statement — the outcome D5 exists to prevent.

## F9 — the surface-count restatements (A25, disposition 11 row 2)

Step 4 **literally falsifies** *"exactly two named surfaces … never a third."* Five sites, all
re-derived at HEAD:

| site | current text | change |
|---|---|---|
| `vault-operating-contract.md:66` | *"exactly **two named surfaces** — extraction … and container maintenance"* | replaced by the entry condition (**F2**) |
| `vault-rule-card.md:26` | *"exactly two named surfaces … **never a third**"* | replaced by the test (**F3**) |
| `skills/vlt-extract/SKILL.md:13` | *"extraction is **the** sanctioned artifact path into it (the contract's Layer 3 names one other surface…)"* | *a* disposition; points at `contract:66` (**F5**) |
| `skills/vlt-agent-creative/SKILL.md:14` | *"…you honor the authorship-honesty boundary and **never open a third surface**"* | keeps the authorship-honesty sentence; the surface-count clause becomes *"and you write only where the container's posture admits you"* |
| `skills/vlt-review-council/SKILL.md:51` | *"Write to `{wiki}`, PARA, `sources/`, or the human zones — a file-back flows through the Librarian."* | **narrowed, not deleted** (disposition 14): the council's own restriction survives — *"Write to `{wiki}`, `sources/`, or the human zones, or file into PARA yourself — a file-back flows through the Librarian."* |
| `skills/vlt-upgrade/SKILL.md:159` | *"**Touch the human zones or PARA.** Same boundaries as every partner — `_agent/` and `_meta/` only."* | **narrowed, not deleted** (disposition 14): *"**Touch the human zones or PARA.** `vlt-upgrade` is not an authoring partner — `_agent/` and `_meta/` only."* |

**All of these land, or the prohibition survives in prose** (A25 — six voices, the session's
most-converged finding). *Note: `vlt-agent-creative:14` and `vlt-extract:13` are edited by both
F1/F5 and this F-site; the builder makes one edit per line, satisfying both.*

## F10 — single-home the `{wiki}`-is-not-PARA qualifier (A21)

**The friction is real and it is a restatement problem** — a partner filing one artifact reads
the full `{wiki}` qualifier **six to nine times** before writing a byte. **Ten shipped sites,
all re-derived at HEAD:**

`vault-rule-card.md:26` · `vault-operating-contract.md:41`, `:64`, `:66`, `:68`, `:70` ·
`extraction.md:80`, `:82`, `:148` · `frontmatter.md:175` · `checks.md:18` **(exempt)**

**The exact change.** **`contract:64` is the canonical home** (disposition 1) — it already
defines the zone and already carries the Librarian-only floor. It gains one sentence making the
statement complete and quotable: *the `{wiki}` subtree lives at a `{resources}` address and is
Layer-2 Librarian-only territory — it is never PARA, never a container or container member, and
is removed from PARA populations at selection time.* **The other nine sites reduce to short
pointers** — the qualifier's *fact* stated once where the reader needs it, with the mechanics
pointed at `:64`, never restated. **`checks.md:18` keeps its self-contained sentence** (A21,
ruled — a check that resolves its population elsewhere is B10-12's twelve false positives).

**Scope note, as ruled: this is a NARROWING, not new work.** Six of the ten sites are already
being edited by F2/F3/F4/F7 in this build. The four that are not — `contract:41`,
`extraction.md:80`, `:82`, `frontmatter.md:175` — are pointer edits only.

**⚠ Constraint on `frontmatter.md:175`.** It reads *"live again as of extraction v6"*. That is a
historical fact, not a version pin, and **it is not updated to v7** — the sentence records when
`resources/` became a target, which this build does not change. Reducing its `{wiki}` clause to
a pointer is a **prose** edit to a summary the file itself declares non-canonical (`:171`), so
it does **not** bump `frontmatter.md` (disposition 2). *If the builder finds itself changing what
`frontmatter.md` asserts rather than where it points, stop — that is 13 → 14 and nine re-acks,
and it is not in this brief's scope.*

## F11 — the vault-facing notification (A33)

**Current state (re-derived at HEAD).** `skills/vlt-upgrade/SKILL.md:95-116` is the post-flight
report schema — a **closed key set** with **no key for a governance rule change**.
`governance_divergence` (`:110`) renders `[]` on a pristine vault and **reads as health**. The
rule card is **overwritten silently by design** (`vlt-setup/SKILL.md:148` — *"module-owned —
overwrite it on every…"*). *"The honest description of the vault's moment of discovery is: a
partner writes somewhere it could not write yesterday, and that is the notification."*

**The exact change.** The schema gains, beside `governance_divergence`:

```yaml
  governance_rule_changes: [<convention/contract: what changed and what a partner may now do differently — from the release's own record>, ...]   # never omitted when empty
```

plus the prose paragraph after `:118` stating the render rule (**never omitted when empty** —
the `local_conventions_intact` idiom already in the file at `:103`) and its source: the
release's shipped record, not a diff computed at upgrade time. This build populates it for its
own release with the PARA posture change.

**Why.** Shipped-surface work, in a build already editing shipped surface, in the same release
(Sally + Victor). It is also disposition 10's mechanism: the retroactive-open window is
**announced**, not discovered. *(This is the module's answer on the notification axis; A34's
re-pointed watch measures whether it works.)*

## F12 — `checks.md:16`'s rationale (disposition 11, row 4)

**Current state (re-derived at HEAD).** `:16` describes `para_missing_attestation` as catching
*"unstamped, unattested artifact-shaped agent writes reaching the layer **outside the sanctioned
surfaces**"* — **the retired frame restated inside the enforcement that replaces it**, and
incoherent once no closed set of sanctioned surfaces exists.

**The exact change.** The clause becomes *"…reaching the layer **without honest, attested
frontmatter**"* — the net's actual criterion, and now the layer's actual entry condition. The
finding's mechanics, its container carve-out, and its legal response are **unchanged**.

## Registration

**No new skill, no new workflow, no `module-help.csv` row, no `marketplace.json` change.** This
build creates no `skills/vlt-*/` directory, so neither half of the Arc-9 registration rule
applies.

**But this is a convention rule change, so the consumer walk is the registration work.**

**`extraction.md` 6 → 7 — four acks, all in this build.**

| consumer | ack site at HEAD | current | after |
|---|---|---|---|
| `vlt-extract` | `skills/vlt-extract/SKILL.md:4` | `depends_on: ["extraction@6", "wiki-supersession@2", "frontmatter@13", "write-ver…"]` | `extraction@7` |
| `vlt-lint` | `skills/vlt-lint/SKILL.md:4` | `depends_on: ["frontmatter@13", "wiki-index@2", "wiki-supersession@2", "extraction@6", "write-verification@3", "spec@2", "consult@1", "decision-log@3"]` | `extraction@7` |
| `vlt-track` | `skills/vlt-track/SKILL.md:4` | `depends_on: ["extraction@6", "wiki-supersession@2"]` | `extraction@7` |
| **`vlt-query`** *(new consumer, A26)* | `skills/vlt-query/SKILL.md` — **no `depends_on:` line exists** | — | **add** `depends_on: ["extraction@7", "frontmatter@13"]` |

**`extraction.md:12`'s `consumers:` becomes `[vlt-extract, vlt-lint, vlt-track, vlt-query]`.**
Verified bipartite-consistent **today** at three: each of the three pins `extraction@6` at its
`:4`. The build must leave it bipartite-consistent at four.

**`frontmatter.md` — `consumers:` 9 → 10, NO version bump.**
`frontmatter.md:11-12` reads `version: 13` / `consumers: [vlt-ingest, vlt-extract, vlt-research,
vlt-lint, vlt-mint, vlt-dispatch, vlt-setup, vlt-groom, vlt-lint-full.js]`. `vlt-query` is added
to that list; its new ack pins **`frontmatter@13`**, the current version. **This is a roster
change, not a rule change** — `frontmatter.md`'s assertions are untouched (disposition 2), so
`version:` stays 13 and the other nine acks are untouched.

**Not touched, deliberately:** `skills/vlt-setup/assets/workflows/vlt-lint-full.js:11` — the
asset node's `depends_on:` pins (`frontmatter@13`, `wiki-supersession@2`, `wiki-index@2`,
`write-verification@3`). It is **not** an `extraction.md` consumer and does not become one
(disposition 4), so E5's asset-node parse is unaffected. **`write-verification.md` stays
`version: 3` / 5 consumers** (build-1's F7 landed there; this build does not touch it).

**"No bump owed" is not "no cost" — the three named non-handshake gates, priced:**

- **package-lint C6** (`tools/package-lint.py:330-346`) — **FIRES.** This build edits
  `vault-operating-contract.md` at `:66`, `:68`, `:190` (and `:64` for F10), so
  `vault-rule-card.md`'s `derived_from: … sha256:` **must be re-derived in the same build**
  (F3), and the card must stay inside `RULE_CARD_BUDGET` (**6,957 / 8,000** at HEAD — 1,043
  bytes of headroom, and A28's rewrite is expected to be net-shorter).
- **package-lint E4** (`tools/package-lint.py:857-877`) — **does not fire.** No new
  `package-lint` callable is added (disposition 5: the authorization check is `checks.md` prose,
  outside E4 by construction). `tools/test-package-lint.py`'s `CASE_FLOOR = 23` is unchanged.
- **package-lint E5** (`_e5_asset_nodes`) — **does not fire.** No asset node's `// depends_on:`
  header changes (disposition 4).
- **package-lint E6** (`SCHEMA_SIZE_BUDGET = 3700`) — **does not fire.** No fan-out schema is
  touched. *(Build-1 left `PAGE_SCAN` at 3598 with 102 chars of margin; this build must not
  spend any of it, and it does not.)*

## Out of scope (dispositioned)

1. **`ST-1`'s C5 — lint catches non-wiki `sources:` entries.** *Not built.* A18 is right that
   the nets judge presence and enum membership, never truth, and that `ST-1`'s grounded finding
   is 57 PARA files with correct-looking frontmatter and falsified `sources:`. No ideation
   ruling covers it. **Filed to `factory/inbox/` as roundtable out-of-scope item 3** — the
   roadmap already queues it; this brief does not fold it in.
2. **A relocation mechanism / `vlt-groom` extension.** *Rejected at ideation (Round 8).* Once
   the destination is legal, a migration is an ordinary owner request, and the discipline for
   performing one already ships at `vlt-upgrade/SKILL.md:75`. **`ST-2` trap 7 is honoured as an
   acceptance caveat, not as scope: occupancy is not this cycle's measure** — judged on
   occupancy, a correct change reads as a failed one.
3. **The `{wiki}` carve-out** (`contract:70`, `checks.md:18`). *Refused, 4/4 (A19).* Retiring it
   would fire `para_*` against every page in the wiki and open the Librarian-only zone to
   `trust: raw` writes against act-blocking `vault-rule-card.md:27`.
4. **The `{wiki}` module-fixed floor** (step 5's other half). *Already shipped* —
   `contract:64` reads *"a Librarian-only zone: the Librarian is its only writer."* **Struck as
   built (A20, the fifth capture claim overturned this cycle).** F10 adds a pointer sentence at
   `:64`; it does not re-author the floor.
5. **`_vault/`** — stays human-only, no contract edit (Q13). `sources/` was never an open
   question: it is absent from the human-only list because it is **Layer 1, read-only for
   everyone** (`contract:62`, `:68`), not a human-only folder.
6. **`frontmatter.md` as a rule** — not edited (disposition 2, disposition 3, F10's constraint).
   Its `consumers:` list is a roster change only.
7. **`vlt-lint-full.js`** — not edited by this build at all (disposition 4). Build-1 owns it this
   cycle; build-2 owns it next.
8. **A confidentiality field on containers** — DECLINE stands (disposition 8). Maya's dissent
   preserved.
9. **`checks.md:49`'s narrowing (A14)** — a build-2 question, not this build's. Mary's dissent
   is recorded there.
10. **A new skill for `ST-1`'s C3.** Step 4 gives the existing verb a destination; a second
    skill was never ruled.

## Verification (unit, at rest — lifecycle step 5)

**V1 — the handshake bipartite re-check. The check of record is `package-lint` Group E.**
`uv run tools/package-lint.py` — **E1** (handshake-bipartite), **E2** (structure-map SSoT),
**E3** (stray-pin), **E5** (asset nodes). Every consumer listed ↔ every ack current, across
`extraction.md`'s new four-consumer roster and `frontmatter.md`'s new ten. **Do not write a
hand-rolled `grep "extraction@" skills/` as the recorded verification** — it is self-confirming
(it greps for the token you just wrote, in the files you just edited) and cannot fail on the
drift Group E exists to catch. A grep is fine as an aid while editing; Group E is the record.

**V2 — packaging lint, mid-cycle A/B/C/E run.** `uv run tools/package-lint.py` — expect
`PASS group A / B / C / E; SKIPPED group D (no --expect-version)`. **C6 is the one to watch**:
it fails on a stale `derived_from:` sha or an over-budget rule-card. Record the PASS line and
the card's new byte size.

**V3 — the step-6 + step-0 gating instrument (A55 ruled (b); A17's ordinary-run constraint).**
One agent, given: the **edited** `vlt-lint/SKILL.md` Steps 0–2, the **edited** `checks.md`, the
**edited** `report.md`, and `extraction.md@7` — asked to **run an ordinary scoped `vlt-lint`**
over a temp fixture vault and return its report fence. **Not** to invoke a check.

Fixture tree (built in the working session, never committed):

```
{fixture}/resources/wiki/some-page.md              # Layer 2 — MUST NOT appear in any para_* slot
{fixture}/resources/briefs/2026-08-25-a-brief.md   # loose at a layer root, no ancestor charter
{fixture}/areas/health/charter.md                  # writers: [human]
{fixture}/areas/health/notes/a-note.md             # sub-container, UNDECLARED — inherits [human]
{fixture}/areas/health/record.md                   # container file — attestation carve-out
{fixture}/projects/thing/charter.md                # writers: [human, agent]
{fixture}/projects/thing/a-doc.md                  # author: agent, trust: raw, attested
```

**Four pass conditions, and one of them is the negative control** (gate-2: a discharging
instance must be one that could have failed):

1. **The population is selected at all** — the run reports on files under `areas/`, `projects/`
   and `resources/` (outside `resources/wiki/`). *This is what step 0 buys; before it, the run
   reports nothing here and the gate cannot see its own hole.*
2. **`resources/briefs/2026-08-25-a-brief.md` PASSES** — no declaring ancestor → `open` → not a
   finding (A22: *"this is the pilot's happy path, not a corner case"*).
3. **NEGATIVE CONTROL — `areas/health/notes/a-note.md` FAILS** with
   `para_writer_unauthorized`: it is `author: agent` beneath a parent declaring
   `writers: [human]`, and an undeclared sub-container **inherits** (A23). *If this file passes,
   inheritance is not implemented and the build is not done.*
4. **`projects/thing/a-doc.md` PASSES** (`agent` ∈ `writers:`), **`resources/wiki/some-page.md`
   appears in no `para_*` slot at all** (removed at population time, not by an exception), and
   `areas/health/record.md` draws no `para_missing_attestation` (the container carve-out at
   `checks.md:16` survives).

**Evidence:** the returned report fence recorded **verbatim** in the brief's BUILT `status:`.
*(Precedent: build-1's Verification 3 reader probe, same cycle, same evidence rule.)*

**V4 — full-mode read-through.** Confirm by reading that `full-scale.md:7`'s derived glob set
covers `{projects}`/`{areas}`/`{resources}` with `{wiki}` carved out, and that F0's added
sentence points at that predicate rather than restating it. Record the predicate's own words.

**V5 — R3 (legal response).** This build adds **one** finding class,
`para_writer_unauthorized`. Its one-line legal response is stated at the check's own single home
(`checks.md`) in the same build — **never auto-fixed**, because `writers:` is human-gated
(F7). Confirm `checks.md:16`'s and `:17`'s existing legal responses are unchanged and that
`:48`'s narrowing did not drop its two flags' responses.

**V6 — R4 (enumeration widening).** Disposition 15: the widened enumeration is `vlt-lint`'s
file population, at all four sites (`SKILL.md:23-41`, `:43-45`, `:49-50`, `full-scale.md:7`).
Confirm all four moved together; confirm the declared exclusion (the workflow's `{wiki}`-only
page set) is stated, not silent.

**V7 — R2 (fixture extension).** **Not applicable, stated:** no `package-lint` gate check is
added or changed, so E4's inventory is unchanged and `CASE_FLOOR` stays 23. *(Verified: E4
introspects `^check_ / ^_e\d+_` callables in `package-lint.py`; a `checks.md` rule is outside it
by construction.)*

**V8 — the retirement greps.** For each row of disposition 11's table, confirm the retired
phrase is gone from **every** site and that no site restates the retired frame:

```
grep -rn "two named surfaces\|never a third\|never open a third surface" skills/     # → 0
grep -rn "outside those two surfaces\|outside the sanctioned surfaces" skills/       # → 0
grep -rn "does not add an artifact write-path\|only through extraction" skills/      # → 0
grep -rn "at least 2 contributing wiki pages\|≥2 contributing wiki pages" skills/    # → 0
grep -rn "a thin wiki is a stop" skills/                                             # → 0
grep -rn "writers:" skills/                                                          # → extraction.md schema + contract:68 + checks.md + F0 only
grep -rn "excluded by name\|carve-out by name" skills/                               # → contract:70 + checks.md:18 STILL PRESENT (A19)
```

The last line is a **survival** check, not a retirement check: if the `{wiki}` carve-out
disappears, the build has done the one thing the room refused 4/4.

**V9 — sha + budget.** `shasum -a 256 skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`
matches `vault-rule-card.md:11`'s `derived_from:`; `wc -c` on the card ≤ 8,000. *(Both are
inside C6, but record the raw numbers — C6's PASS line does not print them.)*

**V10 — scrub.** No personal or vault-local content in any changed shipped file; worked examples
use placeholder paths (`{field-vault}`, `{owner}`, `{fixture}`). The fixture tree above is
**temp-only and never committed**.

**V11 — no `.decision-log.md` anywhere in the working tree** before the commit.

## Release

**Not the release build.** Build order is **1 → 3 → 2** and **build-2 is the cycle's last build**
(roundtable A11 — build-2 queues behind builds 1 **and** 3, because this build bumps
`extraction.md` 6 → 7 and adds a lint check, both of which change what a cached finding
*means*). D3 rules **one release, whole cycle**: the dual version bump
(`.claude-plugin/marketplace.json` `"version"` + `skills/vlt-setup/assets/module.yaml`
`module_version`), the `uv run tools/package-lint.py --expect-version X.Y.Z` gate, and the
ff-merge → tag → push sequence all ride **build-2's** brief. **This build bumps no version
string.**

**Note for build-2's brief (A10, the cache key):** this build bumps a convention `version:` and
adds a check, so any findings sidecar written before it holds verdicts adjudicated under a
retired ruleset. Both must be in build-2's cache-key fingerprint.

**Owner action when this build ships (roundtable A57), noted and NOT performed here:**
hand-deliver the re-derive notice to `{field-vault}`'s known PARA park — the same act as the
17:06Z comment on tracker #11. That is the owner's, not the builder's.

## Acceptance (live — appended to the roadmap ledger)

Nine checks: **five `[ship-verifiable]`, all gating; four `[field-contingent]`, none gating.**
The filing's request that retiring a load-bearing rule **gate** closeout (the A4-4(5) lesson) is
honoured by the ship-verifiable half, **not** by mis-tagging the field half (E5, ruled Round 8).

**(1) `[ship-verifiable]` — GATES.** The handshake is bipartite-consistent after
`extraction.md` 6 → 7: `extraction.md:12` lists four consumers and all four ack `extraction@7`
(`vlt-extract:4`, `vlt-lint:4`, `vlt-track:4`, and `vlt-query`'s new `depends_on:` line);
`frontmatter.md` stays `version: 13` with ten consumers and `vlt-query` acking `frontmatter@13`;
`write-verification.md` untouched at `version: 3` / 5. **Instrument:** `package-lint` **Group E**
(`tools/package-lint.py` — E1/E2/E3/E5), run at rest. **Evidence:** the Group E PASS line and
the two `consumers:` lines recorded in the BUILT `status:`.

**(2) `[ship-verifiable]` — GATES.** The rule-card's derivation claim is true after the contract
edit: `vault-rule-card.md:11`'s `derived_from: … sha256:` equals the shipped contract's actual
digest, and the card is inside `RULE_CARD_BUDGET` (8,000 B; 6,957 at HEAD). **Instrument:**
`package-lint` **C6** (`tools/package-lint.py:330-346`), plus the raw `shasum -a 256` / `wc -c`
numbers. **Evidence:** the PASS line, the new digest, and the new byte count in the BUILT
`status:`.

**(3) `[ship-verifiable]` — GATES.** The retirement landed **whole** — all five rows of the
brief's retirement table are gone from every named site, no site restates the retired frame,
and the `{wiki}` carve-out **survives** at `contract:70` and `checks.md:18`. **Instrument:** the
brief's Verification-8 grep battery (seven greps, six expecting 0 and one expecting survival),
run factory-side at rest. **Evidence:** the seven grep outputs recorded verbatim.

**(4) `[ship-verifiable]` — GATES.** A `para_*` finding is produced by an **ordinary `vlt-lint`
run** — not by direct check invocation — over a fixture vault, proving the file-selection path
exists (owner ruling R-1 / A17: *"a fixture that invokes the check directly passes with the
file-selection path still missing; the gate cannot see its own hole"*). **Instrument:** the
brief's Verification-3 single-agent reader probe over the specified temp fixture tree,
factory-side and at rest, with the negative control at pass condition 3. **Evidence:** the
returned report fence recorded verbatim in the BUILT `status:`.

**(5) `[ship-verifiable]` — GATES.** The write-posture resolver behaves as ruled on that same
fixture: nearest-declaring-ancestor resolution; **inheritance** binds an undeclared
sub-container beneath a declaring parent (A23); **undeclared → `open` → PASS**, never a finding
(A22, and `{resources}/briefs/` is E5's own pilot population); `{wiki}` removed at **population**
time with no exception clause inside the check; the container-file attestation carve-out
intact. **Instrument:** Verification 3's pass conditions 2, 3 and 4. **Evidence:** as (4).

**(6) `[field-contingent]` — does not gate.** `trust: raw` becomes **representable and
present** in PARA — the change's own test (`ST-2`: *"if no `raw` content appears there after the
entry-condition change, the change did not take"*, regardless of contract text). **Three
outcomes, not two** (A18): (a) `raw` appears honestly — the change took; (b) nothing appears —
it did not; (c) **`raw` appears and `author:` is falsified** — the nets judge field presence and
enum membership, never truth, and this is the reading that says the honesty layer needs C5.
**Event:** `vlt-brief`'s next scheduled issue files to `{resources}/briefs/` at honest
`author: agent` / `trust: raw` — no relabeling, no pointer-container indirection, no bespoke
carve-out. **Performer:** the owner. **Vault:** `{field-vault}` (the only install running
`vlt-brief` on a schedule). **Bound:** the first scheduled `vlt-brief` issue after the release,
no later than Cycle 13's `inbox-capture`. *One live run also closes tracker **#11**, which is why
A12-3 and A12-4 are one story.*

**(7) `[field-contingent]` — does not gate.** *(Carry-forward **b2(2)**, RETIRED into this
build's acceptance by Q9 — the watch's premise is obsolete on landing and it must not discharge
against text this cycle rewrote.)* A partner resolves a `{resources}`-write legality question
**from the rewritten bundle** without escalating — i.e. it reads the entry condition at
`contract:66`, resolves posture via `contract:68`, and writes or declines without asking a human
to adjudicate the rule. **Event:** any partner session in which a `{resources}` write is
attempted after the upgrade. **Performer:** any partner in a live vault; observed by the owner.
**Vault:** `{field-vault}`. **Bound:** Cycle 13's `inbox-capture`.

**(8) `[field-contingent]` — does not gate.** The vault is **told**: the post-flight report of
the upgrade that carries this release renders `governance_rule_changes:` **non-empty**, naming
the PARA posture change (A33 — *"a partner writes somewhere it could not write yesterday, and
that is the notification"* is the failure this check exists to detect). **Event:** the owner's
`vlt-upgrade` run onto this cycle's release. **Performer:** the owner (standing rule).
**Vault:** `{field-vault}`. **Bound:** the first upgrade after the release. *(The key's presence
and its never-omitted-when-empty rule are verified at rest under check 3; this is the live
rendering only.)*

**(9) `[field-contingent]` — does not gate.** *(The **re-pointed** confidentiality DECLINE+WATCH,
re-graded at brief time per A34 — Maya's dissent preserved, the DECLINE unchanged.)* A vault,
on discovering the new posture, **declares `writers:`** on a container it had previously framed
in prose — the mechanical answer arriving where the prose one never read. **Event:** a
human-ratified `writers:` line appearing on any live `charter.md`. **Performer:** the human
(charters are human-gated — a partner may propose, never ratify). **Vault:** `{field-vault}`,
the only install with live containers. **Bound:** Cycle 13's `inbox-capture`; if no charter
declares by then, the honest reading is that the retroactive-open window was never noticed, and
that routes to an owner ruling on whether A33's notification is sufficient — **not** a fourth
re-carry.

## Next lifecycle move

A **fresh builder session** implements this brief via `bmad-workflow-builder`. Its exit
obligations: rewrite this brief's `status:` to a **BUILT record with numbered deviations**,
delete any `.decision-log.md` in the working tree, and make **one commit** for the build.

**Then: `brief build 2`** (`build-brief`) — the cycle's last build and its release build
(order 1 → 3 → 2; build-2 queues behind this one, roundtable A11/A10).
