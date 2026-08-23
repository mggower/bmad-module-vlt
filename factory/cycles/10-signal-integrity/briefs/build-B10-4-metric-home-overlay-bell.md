---
title: 'Build #B10-4 — the durable metric home, the overlay bell, and per-section enforcement addressing (the enforcement kit learns to hear vault-grown rules)'
status: 'BUILT 2026-08-21 — all eight F-sites landed; unit-verified at rest; not a release build. RED-THEN-GREEN RECORD (Verification 3, scratchpad fixture vault): (a) RED — pre-build reader, registry declaring `local_metrics: research_note_count` (file_count over {research}) + wire keyed to it → report `⚠ research-mass ERROR — unknown metric id `research_note_count` — not in the canonical table`, strip loud, exit 0; (b) GREEN — post-build the same fixture derives the metric (2 files → 2), evaluates the wire tripped (2 >= 2, strip renders surface_text) and ok (>= 5), and renders the denominated block ("1 local metric(s) (registry-declared): `research_note_count` (file_count): 2 — definition"); bytes + days_since_newest kinds fixture-run green (dir bytes 35; dated-name age 10 days beats frontmatter-dated sibling; unresolvable {nonexistent_key} locator → n/a with reason stated); (c) a wire naming a genuinely unknown id still errors loudly with the two-home text ("not in the canonical table or the registry''s `local_metrics:` declarations"); (d) malformed declarations loud per-entry (missing kind; shadowing canonical `log_bytes` → "shadows a canonical metric id"); (e) --strip empty + exit 0 on green, loud on every error class; seed copy (zero local_metrics) renders no local block, 4 stock wires evaluate as before. VERIFICATION: (1) package-lint A/B/C/E PASS (Group E the check of record — all eight skill pins + vlt-lint-full.js header ack at frontmatter@10; D SKIPPED, release is B10-5); (2) both :173 markers re-derived against the @10 rule 4 (untouched by this build — diff shows only the version line + enforcement-section hunks; normalization clause + coexistence posture both verify still-true) and re-stamped @10; grep shows zero frontmatter@9 in the shipped surface; (3) recorded above; (4) py_compile clean, uv run tools/test-cost-manifest.py 7/7 green; (5) C8 unchanged-PASS inside the full run; (6) `local_metrics` appears in exactly the six F-site homes (tripwires.yaml owns the schema; frontmatter.md/checks.md/vlt-mint:99/vitals docstring/vlt-setup:186 each carry one pointing sentence); *Per-section addressing* stated once (frontmatter.md) and pointed at from checks.md + vlt-mint:140; (7) `overlay_rule_undeclared` in exactly checks.md (with R3 response) + report.md (sibling slot); five existing slots name/position-stable at report.md:24-28; (8) six-case desk-check against the shipped check text — (a) rule-shaped section + valid per-section declaration → no finding; (b) rule-shaped, no declaration → overlay_rule_undeclared; (c) incomplete per-section deferral → deferral_invalid naming <overlay §section>; (d) counter naming a declared local id → no finding, undeclared id → counter_unknown_metric; (e) content-extension section → flags nothing (explicit clause); (f) base convention file → file-level validation exactly as today — all six resolve correctly; (9) scrub clean — placeholder paths only, fixtures confined to the scratchpad; node --check clean, parse-on-intake untouched. F7 WALK RECORD: the six expected-none consumers (ingest/extract/research/dispatch/setup/groom) grepped for enforcement-declaration recitations — zero found, pin bumps sufficient; vlt-lint reconciled via F4/F5, vlt-mint via F6, the asset via the header ack + marker re-stamps. DISPOSITION-5 FINALIZATION (in-bound): kinds file_count (`glob`), bytes (`path` — file st_size or dir via _dir_bytes), days_since_newest (`glob`; date from the dated filename else frontmatter created/date/last_updated, never mtime); flat fields id/kind/locator/definition; `{key}` locators resolve through the structure map. Deliberate deviations, numbered: (1) frontmatter.md''s *Per-section addressing* subsection names the meta-check as the finding''s home without restating the class name — keeps Verification 7''s "in exactly checks.md + report.md" literally true; (2) `parse_wires` refactored onto a shared `_parse_flat_entry_list` helper so `local_metrics:` may precede or follow `wires:` — behavioral delta: the wires scan no longer hard-stops at the first later top-level key; (3) registry local-metric problems render as their own `⚠ LOCAL METRIC ERROR:` stream (and `local metric error —` in --strip) beside the wire-error stream, per-entry loudness with the class named; (4) `load_registry` now returns (wires, local_defs, wire_errors, local_errors, note) and `evaluate_wire` gained an optional `local_ids` parameter — internal signatures, no external caller (cost-manifest imports derive helpers only; test green). No .decision-log.md in the tree. Ship-verifiable acceptance checks 1-3 discharged at rest this session; check 4 field-contingent (rides the owner''s vlt-core declaration + upgrade after v0.13.0). One commit.'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox (Arc 9, archived): 2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md (A9-3 — all three legs of the jointly-unsatisfiable argument; direction question; origin mggower/bmad-module-vlt#1)'
  - 'inbox (Arc 9, archived): 2026-08-18-121417-vault-grown-consumers-have-no-durable-registration.md (A9-2 Finding 4 per-section enforcement addressing + Finding 5 the overlay bell)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Grouping (2026-08-21): build-B10-4 bullet (binds: Q4, S3, Q3a, Q3b per roundtable A6, + the Arc 9 roster at archive :976-984). Arc 9 rulings travel whole (skills/reports/archive/inbox-evolution-arc9-roadmap.md): D2 (bell + metric ship in ONE build — the true ordering constraint), D3/A22 (Finding 4 rides this bump — @9 → @10, resolution (i), two bumps across two releases, nine consumers + workflow ack), Q9/A4-A6 (carve-out-vs-clobber doctrine; METRICS stays an illegal host; birth-time obligation), the cluster''s build-division item 2, roundtable A21 (direction 3 re-admitted as a FLOOR — shipped v0.12.0, see disposition 6; the brief-time question is direction 1 vs 2 ON TOP of it). Arc 10 roundtable: A2 (the inherited A22 second bump with the full nine-consumer + workflow-ack walk as explicit in-cut scope; the vlt-lint-full.js walk re-derives every marked restatement, not just the ack string), A6 (the durable metric home is born under Q3a''s persist shape or this brief records why it sits outside E2''s census — recorded, disposition 2), A8 (restated instructions carry per-convention@N markers that consumer walks re-derive). Q4/S3: briefed only after B10-1 landed — B10-1 BUILT 2026-08-21 @ 3d25cc4; gate open.'
risk: 'moderate — a frontmatter.md rule change (frontmatter@9 → @10: per-section enforcement addressing + the enforcement_counter vocabulary widening) with the full nine-consumer + workflow-ack walk in the same build (version-handshake standing rule; package-lint E1 + E5 both fire), plus a semantic widening of the enforcement kit''s one-vocabulary invariant (vlt-vitals.py known-id check) inside the SessionStart hook path. Bounded: no operating-contract edit (no C6 re-stamp), no new package-lint check (no E4/R2), no new persisted report surface (no E1-census membership, no Decay-contracts/zone-map rows), no release in this build.'
---

# Build #B10-4 — the durable metric home, the overlay bell, and per-section enforcement addressing

This is **B9-6 carried whole from Arc 9** — the half of v0.13.0's inherited target that was
ruled, roundtabled, and left unbuilt when Arc 9 closed. It closes the arc's structural
centre, stated by two filings from opposite ends and confirmed jointly unsatisfiable at
capture (Arc 9 archive, A9-2/A9-3):

1. **A9-3 — vault-local tripwire metrics have no durable home.** The registry is durable
   (`vlt-setup/SKILL.md:186`: skip-if-present, merge-by-id, local wires never dropped) but
   its vocabulary is clobbered (`vlt-vitals.py` is module-owned, overwritten on every
   install/update — `vlt-setup/SKILL.md:185`), and the two are hard-coupled: a wire's
   `metric` must name a `METRICS` id "and no other" (`tripwires.yaml:10-13`,
   `vlt-vitals.py:283-284`). A vault-grown metric survives only as a hand-edit the next
   upgrade eats.
2. **A9-2 Finding 5 — the overlay bell.** The enforcement-doctrine meta-check
   (`vlt-lint/references/checks.md:37`) validates "every `{conventions}/*.md` file" —
   overlays at `{overlays}` are never walked, so `deferral_expired` /
   `declared_untripwired` / `deferral_invalid` / `counter_unknown_metric` can never fire
   on an overlay-hosted rule.
3. **A9-2 Finding 4 — per-section enforcement addressing.** The enforcement declaration
   (`frontmatter.md:255-274`) is a set of flat **file-level** keys; an overlay **accretes
   sections**. The next genuinely rule-shaped overlay section cannot be declared honestly
   at all — and shipping the bell without fixing this would be a checker validating a
   declaration shape the filing says cannot be honest (D3's grounded reason Finding 4
   rides this build).

D2's ordering constraint is why all three land as **one build**: ship the overlay-walking
checker without the durable metric home and it fails every rule it newly walks (any
overlay `enforcement_counter:` names a vault-local id and `vlt-vitals.py:283`
hard-errors); ship the metric home without the bell and a durable local metric rings
nothing. Neither half ships alone.

The Q4/S3 gate is open: B10-1 (`3d25cc4`) closed the Step-3/Step-3.6 ordering trap by
source-hashing the manifest (`vlt-upgrade/SKILL.md:49` now states the trap closed by
construction), so this build owes **no** upgrade-ordering work — S3's residue here is
only that it informed the direction choice (disposition 1).

**All rejected alternatives in the parent filings and the Arc 9/Arc 10 rulings are
settled — do not re-litigate.** In particular: Q9 ruled no single durable-host mechanism
(per-host plumbing); Q9/A4 keeps `vlt-vitals.py`'s `METRICS` an **illegal** host for
vault-local additions (module-owned, overwrite-on-update — the axis is
carve-out-vs-clobber); D2 ruled one build; D3/A22 ruled two bumps across two releases,
resolution (i), with Carson's dissent on record; A21 ruled direction 3 a floor, not an
alternative; Q2 (Arc 10) ruled the contract overlay narrow and elsewhere (B10-9).

## Brief-time dispositions

**✅ OWNER-REVIEWED 2026-08-23 (first-half review): all seven dispositions CONFIRMED —
disposition 1 live-ruled with a premise correction on record.** Direction 2 stands on
its four grounds untouched (no new durable host, no vault code in the boot hook, a bell
validates declarations not code, S3's two-provenance lesson). **Premise correction:**
disposition 1's accepted-bound justification — "the filer's own lost derive function was
a count-shape" — is FALSE in the field: the lost derive is `pages_with_review_after`, a
*content-filtered* count inexpressible under the three kinds (`vlt-vitals.py:251`),
which BLOCKED acceptance check (4) on 2026-08-23. The bound's own escape route worked
exactly as designed — "its route is an upstream filing" — and that filing exists
(`inbox/2026-08-23-190100-…`, captured as A10-19, held for Arc 11). The field failure
argues for widening the kinds, not for vault-authored Python; direction 2 CONFIRMED
with the bound's cost priced. Dispositions 2–7 batch-confirmed. Review record: the arc
roadmap's first-half review section.

All seven below are **clerk-resolved (autonomous run 2026-08-21, owner review pending)** —
the owner is absent this run; each carries its grounded reasoning.

1. **The A9-3 direction question: direction 2 — declarative local metrics in the
   registry — lands on top of the shipped direction-3 floor.** (The standing brief-time
   question, roadmap §Questions deliberately left to brief time; Arc 9 archive `:2022-2030`;
   A21.) The filer declared no strong preference and offered three directions; ideation
   constrained the choice to 1 (a vault-local metrics module `vlt-vitals.py` optionally
   imports) or 2 (declarative local metrics inline in the registry — count/size/age
   shapes), with S3 informing it. **Direction 2 wins on four grounds:**
   - *The durable host already exists as a carve-out.* `{tripwires}` is vault-grown after
     seeding — skip-if-present, merge-by-id, "local wires are never dropped or rewritten"
     (`vlt-setup/SKILL.md:186`; `tripwires.yaml:36-40`). Declaring local metrics there
     mints **no new host**, so Q9's birth-time obligation (A6, Arc 9) is met with zero new
     machinery, and Q9's amended axis (a vault-local addition lands only where the base
     declares a carve-out) is satisfied by the file's existing fate-split. Direction 1
     mints a new agent-zone host (a `.py` file) whose durability story would need its own
     declaration.
   - *Direction 1 executes vault-authored Python inside the SessionStart hook.*
     `vlt-vitals.py` declares itself "Stdlib-only, read-only, derive-only"
     (`vlt-vitals.py:12`) and runs at every session start; an optional import of
     vault-authored code is an arbitrary-code surface at boot and a new failure mode the
     `--strip` contract (`vitals unavailable`, never silent-green) was not designed to
     contain. Declarative specs keep the reader's posture intact.
   - *The bell can validate a declaration; it cannot validate code.* Leg B's widened
     `counter_unknown_metric` and the wire-evaluation path can statically check a
     declarative spec (known kind, resolvable path, unique id). Against an arbitrary
     function they degrade to existence-checking — the checker would validate a shape it
     cannot see into, the exact defect class Finding 4 exists to close.
   - *S3's lesson, applied.* S3 found the manifest net's failure mode was hashing what it
     could not distinguish (live vs source). A vault-local `.py` beside a module-owned
     `.py` in `.claude/hooks/` re-creates a two-provenance code directory for every future
     net to distinguish; a declarative section in an already-vault-grown file creates
     nothing to misclassify.
   *Accepted bound, stated in shipped text (F1):* direction 2 covers the common
   count/size/age shapes the filing itself named. A derive outside the kind vocabulary has
   no vault-local home — its route is an upstream filing for a new canonical metric or a
   new kind, the same route `METRICS` additions already take. This is a bounded-expressiveness
   trade, not a gap: the filer's own lost derive function was a count-shape.
2. **The A6 binding (Q3a/Q3b): the durable metric home sits outside E2's census
   population — recorded here, per A6's "or the brief records why."** Q3a's persist shape
   (dated verbatim `.yaml` under a config path, retention row same build) governs
   **reports** — artifacts a verb emits and would otherwise discard. The metric home is
   neither: it is **vault-grown registry state**, written only at rare human-gated moments
   (`tripwires.yaml:27-35`, the write-moments contract), read at every vitals derive, and
   never emitted-and-discarded. E2's census population is report-emitting verbs; a
   registry section is not a verb. Consequently: no dated-file shape, no retention row, no
   Decay-contracts / zone-map rows (the `tripwires` row already exists —
   `vault-operating-contract.md:46`), and B10-4 stays out of E1's consumer census by
   construction — the same reasoning shape B10-3 recorded for its record-derived
   partition.
3. **Marker treatment on the walk (A2 × B10-2's shipped invariant): re-derive, then
   re-stamp to @10.** A2 says a marked restatement "must become @10 if rule content moves,
   or be verified still-true"; B10-2's shipped acceptance invariant says "every marker
   version matching the convention's `version:` on disk" (roadmap ledger, B10-2 check 3).
   Both are honored in sequence: the walk **re-derives** each `per frontmatter@9 ...`
   restatement against the @10 text (this build changes the *Enforcement declaration*
   section only; YAML rule 4 is untouched, so the restatements are expected to verify
   still-true), then **re-stamps** the marker to `@10` so marker == `version:` on disk
   holds. A restatement that fails re-derivation is a real drift finding and blocks the
   walk item until reconciled — that is the walk working, not an exception path.
4. **The rule-shaped test and the new finding class.** The meta-check must distinguish an
   overlay section that *states a rule* (constrains what may be written) from one that
   merely extends content (a worked example, a clarification, a field-value addition
   creating no obligation). This is a judgment call, and the meta-check is an agent-run
   lint check, so judgment is legal — the check's text states the test in the boundary
   classifier's own words (`vlt-mint/SKILL.md:42`: "does this create a rule someone else
   must obey?"). A rule-shaped overlay section with no per-section declaration flags the
   **new finding `overlay_rule_undeclared`** (R3 legal response shipped at the check —
   F4). Content-extension sections carry no declaration and flag nothing.
5. **The kind vocabulary and the flat schema are the builder's to finalize within the
   stated bound.** The bound: the count/size/age shapes the filing named — a starting set
   of `file_count` (files matching a glob under a vault-relative path or structure-map
   logical name), `bytes` (file or directory byte size — the `_dir_bytes` helper at
   `vlt-vitals.py:331` already exists), `days_since_newest` (age of the newest matching
   file's dated name or frontmatter date — **never mtime**, which git operations and
   copies corrupt; the vault's records are dated by convention). All declaration fields
   are **flat** (the registry's parser is a stdlib YAML-subset of flat wire fields —
   `parse_wires`, `vlt-vitals.py:239` — and the file's own style is flat; frontmatter YAML
   rule 3's no-nesting spirit applied even though this is not note frontmatter). A
   malformed or unresolvable local-metric declaration is a **loud per-metric error**,
   never a silent skip — the `evaluate_wire` posture (`vlt-vitals.py:275-284`) extended,
   not a new one.
6. **The direction-3 floor is already shipped — no floor work in this build.** A21
   attached "make the clobber legible at upgrade time" to a v0.12.0 build; grounding
   confirms it shipped: `vlt-setup/SKILL.md:185` carries the **clobber-legibility floor**
   (checksum-or-real-differ compare before overwriting an existing
   `.claude/hooks/vlt-vitals.py`, quoted differing content into provisioning notes,
   *overwrote local edits* marked for the Confirm line, ledger routing on upgrade). The
   brief-time question was therefore exactly as the roadmap words it — direction 1/2 *on
   top of* the floor — and this build adds nothing to the floor. After this build the
   floor keeps catching the *illegal* route (hand-editing the module-owned reader), which
   remains illegal per Q9/A4; the legal route is F1's registry section.
7. **Standing-ritual dispositions.** **R1 (interim posture): not applicable** — nothing
   ships ahead of its mechanism; the widened rules (per-section addressing, the widened
   counter vocabulary) and their enforcement (the meta-check's overlay walk, the widened
   known-id check) land in this same build — the *Enforcement ships with widening* rule
   (`frontmatter.md:274`) satisfied by construction. **R3: owed and shipped** — the new
   `overlay_rule_undeclared` class states its legal response at `checks.md:37` (F4).
   **R4 (enumeration widening): not applicable** — the build ships no new file into any
   enumerated class (the `local_metrics:` section lives inside the existing registry;
   the vault's `_agent/tripwires.yaml` is vault-grown and deliberately unmanifested; no
   always-loaded read changes).

## Grounding record (re-ground 2026-08-21, against arc10-v0.13.0 branch @ ca0e700)

Every Arc 9 capture-time site re-verified. **HOLDS:** `tripwires.yaml:10-13` (the
"and no other" coupling) and `:36-40` (vault-grown merge posture);
`vlt-vitals.py:189-236` (METRICS + WIRE_REQUIRED_FIELDS), `:239` (`parse_wires`),
`:275-298` (`evaluate_wire`, unknown-id error at `:283-284`), `:331` (`_dir_bytes`),
`:543` (`load_registry`); `frontmatter.md:11` (`version: 9`), `:12` (nine `consumers:`),
`:255-276` (*Enforcement declaration* — still flat file-level keys, no per-section
addressing anywhere: Finding 4 stands), `:263` (`enforcement_counter:` canonical-table
rule), `:274` (enforcement-ships-with-widening), `:278` (*Vault-writable declared
fields* — shifted from the archive's `:276`, trivial); `checks.md:37` (meta-check walks
`{conventions}/*.md` only: Finding 5 stands), `:42` (overlays deliberately unversioned —
untouched by this build); `report.md:24-28` (the meta-check's five report slots);
`vlt-setup/SKILL.md:185` (vitals overwrite-on-update + the shipped floor), `:186` (seed
merge-by-id); all nine consumer pins at `frontmatter@9` (`vlt-ingest/SKILL.md:4`,
`vlt-extract/SKILL.md:4`, `vlt-research/SKILL.md:3`, `vlt-lint/SKILL.md:4`,
`vlt-mint/SKILL.md:3`, `vlt-dispatch/SKILL.md:3`, `vlt-setup/SKILL.md:3`,
`vlt-groom/SKILL.md:3`, and the asset node `vlt-lint-full.js:11` `// depends_on:`).
**Grounding additions (EXPANDED), in scope beyond the filings' letter:**
- `vlt-mint/SKILL.md:140` — Arc 9's B9-2/B9-4 era shipped text directing that an overlay
  addition creating a rule "carries its enforcement declaration in the overlay file's
  **own** frontmatter" — a **file-level** placement rule for exactly the population
  Finding 4 proves file-level cannot address. It post-dates the A9-2 capture, so the
  capture never named it; it must be re-derived to per-section addressing in the same
  build or the mint ceremony directs vaults to author the dishonest shape the meta-check
  now flags. In scope as F6.
- `vlt-mint/SKILL.md:99` and the vitals docstring `vlt-vitals.py:14-16` — both restate
  the one-vocabulary rule ("from the vitals reader's canonical table") and must carry the
  widened wording (F6, F2).
- `report.md:28` — `counter_unknown_metric`'s slot annotation restates "names no
  canonical metric id"; widens with the check (F5).
**No grounding corrections owed to the roadmap** — no roadmap note asserts a stale
premise (the B10-4 bullet's "direction 1/2 choice on top of the direction-3 floor" is
exactly what grounding found). Zero superseding notes written.

## F-sites

### F1 — `skills/vlt-setup/assets/tripwires.yaml` (the registry grows the durable metric home)

**Current state:** header `:1-40` states the schema (seven required wire fields), the
one-vocabulary coupling — "a wire's `metric` must name an id from that table and no
other" (`:10-13`) — the write-moments contract (`:27-35`), and the vault-grown merge
posture (`:36-40`); `wires:` at `:45` carries the four stock wires.

**Change:**
1. Add an optional top-level **`local_metrics:`** section to the schema, documented in
   the header beside the wire schema: each entry a flat map — `id` (kebab-case, unique,
   and **not** shadowing a canonical `METRICS` id — a shadow is a loud error),
   `kind` (from the bounded vocabulary, disposition 5), the kind's flat locator field(s)
   (e.g. `path`/`glob`, resolving structure-map logical names the way wires' surfaces
   do), and `definition` (one line of prose — the METRICS-table analogue, so the vitals
   report can render it denominated). The seed **ships the section absent** (documented,
   not instantiated — zero local metrics is the shipped state; the section is the
   vault's to grow at the same human-gated write moments as wires).
2. Amend the `:10-13` coupling sentence: a wire's `metric` names an id from the canonical
   table **or a `local_metrics:` declaration in this same file** — an unknown id remains
   a loud per-wire error. State the accepted bound (disposition 1): kinds cover
   count/size/age; a derive beyond them routes upstream, never into a hand-edit of the
   reader.
3. Extend the write-moments and vault-grown paragraphs to name `local_metrics:` alongside
   wires (same moments, same "never dropped or rewritten" fate).

**Why:** A9-3's fix — the durable home is a carve-out in the file that already has the
right fate, per Q9's amended doctrine.

*Out of scope at this site:* no new stock wires; no change to the four shipped wires; no
`local_metrics` entries in the seed (so package-lint C8's seed checks are untouched —
see Verification 5).

### F2 — `skills/vlt-setup/assets/hooks/vlt-vitals.py` (the reader learns the declared vocabulary)

**Current state:** docstring `:14-16` states "must name these ids and no others";
`METRICS` comment block `:189-193` states registry wires and `enforcement_counter:`
values "must name these ids"; `parse_wires` (`:239`) parses only `wires:`;
`evaluate_wire` (`:275`) errors any `metric_id not in METRICS` (`:283-284`);
`load_registry` (`:543`) returns wires only; `render_report` (`:553+`) renders the
canonical metrics section headed "the only legal wire / enforcement_counter ids".

**Change:**
1. Parse the registry's `local_metrics:` section (extend the stdlib YAML-subset parser;
   same tolerance posture — a malformed entry is a loud per-entry error carried in the
   report and `--strip`, never a silent skip).
2. Derive declared local metrics by `kind` (disposition 5's bounded vocabulary), reusing
   the existing helpers (`_dir_bytes:331`, the glob/date patterns in
   `derive_metrics:337`). An unresolvable locator derives `None` with the reason stated —
   the existing underivable posture (`evaluate_wire:290-291`), not an error.
3. Widen the known-id test: a wire's `metric` is legal iff in `METRICS` **or** among the
   registry's validly-declared local ids; a local id shadowing a canonical id is a loud
   error (the canonical table stays authoritative for its own names). The error text at
   `:284` updates to name both vocabularies.
4. Render declared local metrics in the report's metrics section as a **denominated
   sibling block** ("N local metric(s) (registry-declared): id — definition — value";
   zero renders as nothing — the section only exists when declarations do), and update
   the docstring (`:14-16`) and the METRICS comment (`:189-193`) to the widened wording
   with a pointer to the registry section.
5. The module-owned posture is **unchanged**: the reader still ships overwrite-on-update;
   nothing vault-authored is imported or executed (disposition 1). State this in the
   docstring beside the widened-vocabulary sentence.

**Why:** the reader is the one vocabulary's enforcement point; the home is only durable
if the reader resolves it.

*Out of scope at this site:* no changes to canonical metric derivations, the strip
contract, exit codes, or `cost-manifest.py`'s imported substrate functions (it imports
derive helpers, not the wire path — verify with Verification 4's compile + fixture run).

### F3 — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md` (Finding 4 + the vocabulary widening; `version: 9 → 10`)

**Current state:** `:11` `version: 9`; `:12` the nine-consumer roster; `:255` *Enforcement
declaration (convention files)* — flat file-level keys only (`:259-271`); `:263`
`enforcement_counter:` "must name a metric id from the vitals reader's canonical table
… the enforcement kit's one vocabulary"; `:272` stage semantics; `:274`
enforcement-ships-with-widening.

**Change (one bump carries both rule changes — the A22 arithmetic):**
1. **Per-section addressing (Finding 4).** Add a subsection to *Enforcement declaration*
   — *Per-section addressing (overlays)*: a **rule-shaped overlay section** (the
   boundary-classifier test, disposition 4 — point at `vlt-mint`'s classifier, don't
   restate it) carries its **own** declaration block directly under the section heading —
   the same flat keys, the same stage semantics and deferral triple, addressed to that
   section alone. The overlay **file** carries no file-level enforcement declaration
   (one declaration cannot honestly stand in for independently-shaped accreted sections —
   the Finding 4 sentence, stated as the rule's why); base convention files keep the
   file-level shape unchanged. Content-extension sections carry no declaration.
2. **The vocabulary widening.** Amend `:263`: `enforcement_counter:` names a metric id
   from the vitals reader's canonical table **or a `local_metrics:` declaration in the
   vault's `{tripwires}` registry** (the durable vault-local vocabulary — pointer to the
   registry header, which owns the mechanics; never restate the schema here).
3. Bump `version: 9 → 10` and update `last_updated:`. The `consumers:` roster is
   unchanged (no membership change — a rule change, not a widening of the member set).

**Why:** D3/A22 ruled Finding 4 rides this bump; the counter widening must ride the same
bump or the declaration schema and the checker disagree for a release.

*Out of scope at this site:* the *Vault-writable declared fields* member set (`:278`) is
untouched (no new vault-writable base field — the metric home lives in the registry, not
in a base convention); YAML rules 1-6 untouched (load-bearing for disposition 3's marker
re-derivation); the adoption axis (`:276`) untouched.

### F4 — `skills/vlt-lint/references/checks.md:37` (the overlay bell)

**Current state:** the enforcement-doctrine meta-check validates "every
`{conventions}/*.md` file's enforcement frontmatter" — five finding classes
(`enforcement_missing`, `deferral_invalid`, `deferral_expired`, `declared_untripwired`,
`counter_unknown_metric`) plus `convention_meta_missing`; `counter_unknown_metric`
defined against "the vitals reader's canonical metric table … the enforcement kit's one
vocabulary". Overlays are not walked. (`checks.md:36`, the coherence check, and
`checks.md:42`, overlay append-only, are **untouched** — the handshake and append-only
jurisdictions do not change.)

**Change:** extend the meta-check to also walk `{overlays}/{name}.overlay.md`:
1. For each overlay, identify rule-shaped sections (the classifier test, disposition 4 —
   cite `vlt-mint`'s boundary classifier as the test's home) and validate each section's
   **per-section declaration** (`frontmatter.md`, *Per-section addressing* — point,
   never restate the schema) with the **same five finding classes**, entries naming
   `<overlay §section>` in the existing slots (slot names unchanged — `report.md`
   stability).
2. A rule-shaped section with **no** declaration flags the new class
   **`overlay_rule_undeclared`** — **legal response (R3), stated at the check:** add the
   per-section declaration block (a complete stage or tripwired deferral), or re-express
   the section as a content extension if it truly creates no obligation; stages still
   promote only through the mint ceremony, never lint.
3. Widen `counter_unknown_metric`'s vocabulary in the same sentence that defines it: an
   `enforcement_counter:` (file-level or per-section) must name a canonical `METRICS` id
   **or** a `local_metrics:` declaration in the vault's `{tripwires}` registry — read the
   registry, never a carried list. **Never auto-fix** stands on every class.

**Why:** Finding 5 — the bell. With F1-F3 in the same build, the walk cannot fail-on-
arrival (D2's ordering constraint satisfied by construction).

### F5 — `skills/vlt-lint/references/report.md:24-28` (the report surface follows)

**Current state:** the five meta-check slots at `:24-28`; `:28` annotates
`counter_unknown_metric` as "enforcement_counter names no canonical metric id".

**Change:** the five slots keep their names and positions; annotations widen to say
entries may name `<overlay §section>` as well as `<convention>`, and `:28`'s annotation
becomes "names no canonical or registry-declared metric id". Add
`overlay_rule_undeclared` as a sibling slot in the same block (a new finding class needs
a report home — the B10-3 precedent of shipping the slot with the check).

**Why:** a finding class with no report slot is invisible; the slot ships with the check.

### F6 — `skills/vlt-mint/SKILL.md` (the ceremony stops directing the dishonest shape)

**Current state:** `:140` — "An overlay addition that creates a rule carries its
enforcement declaration in the overlay file's **own** frontmatter (the classifier applies
to every boundary-creating mint regardless of landing zone)." `:99` — a deferral wire's
`metric` comes "(from the vitals reader's canonical table)". `:42` — the boundary
classifier (the test's single home — unchanged). `:3` — `depends_on:` pins
`frontmatter@9`.

**Change:**
1. `:140` — re-derive to per-section addressing: a rule-creating overlay addition carries
   its declaration **in the new section itself, directly under the section heading**
   (`frontmatter.md`, *Per-section addressing* — point at it). The classifier sentence
   stays.
2. `:99` — widen the parenthetical: "(a canonical metric id from the vitals reader's
   table, or a `local_metrics:` declaration in `{tripwires}` — the registry header owns
   the shape)".
3. `:3` — the pin bumps with the walk (F7).

**Why:** the grounding-addition site — without it the mint ceremony authors the exact
shape the new check flags; and the mint ceremony is where a vault-local metric is born
(the same human-gated moment that registers a deferral wire), so its text must know the
legal home.

### F7 — the nine-consumer + workflow-ack walk (`frontmatter@9 → @10`, same build)

Explicit in-cut scope per roundtable A2; the version-handshake standing rule. For each of
the nine `consumers:` (`frontmatter.md:12`):

| Consumer | Ack site | Walk item |
|---|---|---|
| `vlt-ingest` | `skills/vlt-ingest/SKILL.md:4` | re-derive any enforcement-declaration restatement (expected: none — it consumes field schemas), bump pin `@10` |
| `vlt-extract` | `skills/vlt-extract/SKILL.md:4` | same |
| `vlt-research` | `skills/vlt-research/SKILL.md:3` | same |
| `vlt-lint` | `skills/vlt-lint/SKILL.md:4` | F4/F5 are its content reconcile; bump pin `@10` |
| `vlt-mint` | `skills/vlt-mint/SKILL.md:3` | F6 is its content reconcile; bump pin `@10` |
| `vlt-dispatch` | `skills/vlt-dispatch/SKILL.md:3` | re-derive (expected: none), bump pin `@10` |
| `vlt-setup` | `skills/vlt-setup/SKILL.md:3` | F8 is adjacent (registry seeding); re-derive, bump pin `@10` |
| `vlt-groom` | `skills/vlt-groom/SKILL.md:3` | re-derive (expected: none), bump pin `@10` |
| `vlt-lint-full.js` | `skills/vlt-setup/assets/workflows/vlt-lint-full.js:11` (`// depends_on:` header — package-lint **E5**'s edit surface, not E1's) | bump header ack to `frontmatter@10` **and** re-derive both marked restatements at `:173` (`per frontmatter@9 rule 4`, twice — the normalization clause and the coexistence posture); rule 4 is untouched by this build, so both are expected to verify still-true, then re-stamp `@10` (disposition 3) |

"Re-derive" per the coherence check's own recites-vs-points test (`checks.md:36`): a
consumer that merely *points* at the convention needs only the pin bump; one that
*recites* mechanics must have the recited text reconciled against the @10 content. The
walk's findings (any unexpected recitation of enforcement-declaration mechanics beyond
F4/F5/F6) are the builder's to reconcile in the same build and record in the BUILT
status.

### F8 — `skills/vlt-setup/SKILL.md:186` (seed-merge durability for the new section)

**Current state:** the seed step merges by wire `id`; "Local thresholds win; local wires
are never dropped or rewritten — the registry is vault-grown state."

**Change:** one clause extending the merge contract to the new section: the vault's
`local_metrics:` declarations are vault-grown state exactly as local wires are — never
dropped, rewritten, or reordered by seeding; the seed ships none, so the merge has
nothing to add there. (The `:185` clobber-legibility floor and the module-owned vitals
posture are untouched — disposition 6.)

**Why:** the durable home's durability must be stated where the writer of the file
lives, or the next reader of the merge rule treats the unknown section as clobberable.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row (convention +
reference + asset edits register nothing). The costs that *are* owed, priced:

- **The consumer walk** — F7, the full nine + workflow-ack walk, in this build (the A22
  second bump; package-lint **E1** covers the eight skill legs, **E5** the asset leg).
- **No C6** — `vault-operating-contract.md` is not edited (the doctrine and its
  `tripwires` row at `:46` already say what this build makes true); no rule-card
  re-derivation owed.
- **No E4/R2** — no `package-lint` check is added or changed (C8's seed assertions remain
  true under F1's seed-ships-none posture — Verification 5).

## Out of scope (dispositioned)

1. **Direction 1 (a vault-local metrics module the reader imports)** — rejected-because:
   disposition 1's four grounds (new host, code execution at boot, unvalidatable by the
   bell, two-provenance code dir). Not a deferral — a vault needing a derive beyond the
   kind vocabulary files upstream for a canonical metric or a new kind.
2. **Any `METRICS` additions or a config knob to extend the canonical table** —
   rejected-because: Q9/A4 keeps the module-owned reader an illegal host for vault-local
   content; the canonical table stays module-owned and upstream-fed.
3. **The report persist contract (dated `.yaml`, retention rows, verb census)** —
   deferred-to-build-B10-6 (Q3a/Q3b/E1/E2); this build adds no persisted report surface
   (disposition 2).
4. **The contract overlay and the rule-card-under-overlays posture** —
   deferred-to-build-B10-9 (Q2's narrow build; A15). This build's overlay work is
   convention overlays only.
5. **The fleet-wide rung and its pointer-line shape** — deferred-to-build-B10-5 (S2
   cleared it; A9). The bell rings at lint cadence; the rung is the activation-time read.
6. **S3's sanctioned-lift tension and any Step-3/Step-3.6 ordering work** —
   already-covered-by B10-1 (`3d25cc4`): source-hashing closed the trap by construction
   (`vlt-upgrade/SKILL.md:49`), and the sanction record carries migration edits.
7. **The direction-3 floor** — already-covered-by v0.12.0 (`vlt-setup/SKILL.md:185`);
   disposition 6.
8. **`overlay_consumers_illegal` / handshake jurisdiction for overlays** —
   already-covered-by B9-4 (`checks.md:42`, `:36`): overlays stay handshake-invisible;
   registration goes through `local_consumers:`. This build changes overlay
   *enforcement* visibility, never handshake membership.
9. **Widening C8 to validate vault `local_metrics:` declarations factory-side** —
   rejected-because: C8 is the *packaging* net over shipped assets; vault declarations
   exist only in the field, where `vlt-vitals.py`'s own loud-error path (F2) and the
   lint meta-check (F4) are the nets. The seed ships zero declarations, so there is
   nothing for C8 to check.
10. **A `local_metrics` mint ceremony kind of its own** — rejected-because:
    `vlt-mint/SKILL.md:99`'s existing deferral-wire moment already covers the birth
    moment (F6 widens its wording); a new ceremony kind for the same human-gated write
    would be a second door to one room.

## Verification (unit, at rest — lifecycle step 5)

1. **Handshake bipartite re-check — package-lint Group E is the check of record**
   (`uv run tools/package-lint.py`, groups A/B/C/E; D is the release gate, not this
   build's). E1 must show all eight skill pins at `frontmatter@10`; E5 must show the
   `vlt-lint-full.js` header ack at `frontmatter@10`. A hand-written grep is not a
   substitute and is not the recorded verification.
2. **Marker re-derivation record (disposition 3):** both `:173` markers re-derived
   against the @10 rule-4 text and re-stamped `@10`; `grep -n "frontmatter@" skills/`
   shows no `@9` stragglers anywhere in the shipped surface (aid-while-editing; Group E
   remains the recorded check for the ack legs).
3. **Enforcement-kit fixture runs (red-then-green), real script against a temp vault**
   under the scratchpad: (a) *red* — on the pre-build reader, a registry carrying a
   `local_metrics:` declaration and a wire keyed to it errors `unknown metric id`;
   (b) *green* — post-build, the same fixture derives the metric, evaluates the wire
   (tripped and ok cases), and renders the denominated local block; (c) a wire naming a
   genuinely unknown id still errors loudly; (d) a malformed local declaration (missing
   `kind`, shadowing a canonical id) errors loudly per-entry; (e) `--strip` stays silent
   on green and loud on error. Record the run in the BUILT status.
4. **Reader integrity:** `python -m py_compile` on the edited `vlt-vitals.py` (C8 runs
   it too); `tools/cost-manifest.py` still imports its substrate functions
   (`uv run tools/test-cost-manifest.py` passes untouched).
5. **Packaging lint:** the full A/B/C/E run PASSes — including **C8** unchanged (seed
   parses, four stock wires complete and canonical, reader compiles, structure-map rows
   present).
6. **Cross-file agreement greps:** the widened-vocabulary wording agrees by pointer, not
   restatement — the registry header (F1) owns the local-metric schema; `frontmatter.md:263`,
   `checks.md:37`, `report.md:28`, `vlt-mint/SKILL.md:99`, and the vitals docstring each
   carry one widened sentence pointing at it (`grep -rn "local_metrics" skills/` returns
   exactly the F-site homes, no schema restated twice). Per-section addressing is stated
   once (`frontmatter.md`, F3) and pointed at from `checks.md:37` and
   `vlt-mint/SKILL.md:140`.
7. **Finding-class completeness:** `overlay_rule_undeclared` present in exactly
   `checks.md` (with its R3 legal response) and `report.md` (its slot); the five existing
   meta-check slots' names and positions unchanged.
8. **Desk-check, six paper cases against the edited check text:** (a) overlay with one
   rule-shaped section + valid per-section declaration → no finding; (b) rule-shaped
   section, no declaration → `overlay_rule_undeclared`; (c) per-section declaration with
   incomplete deferral → `deferral_invalid` naming `<overlay §section>`; (d) per-section
   `enforcement_counter:` naming a declared local metric → no finding; naming an
   undeclared id → `counter_unknown_metric`; (e) content-extension section, no
   declaration → no finding; (f) base convention file → file-level validation exactly as
   today. Record in the BUILT status.
9. **Scrub:** no personal or vault-local content in any changed shipped file; worked
   examples use placeholder paths and generic domain vocabulary.

## Acceptance (live — appended to the roadmap ledger)

1. **`[ship-verifiable]` — the @10 handshake is bipartite-consistent across all nine
   legs.** `frontmatter.md` at `version: 10` with the roster unchanged; all eight skill
   pins and the `vlt-lint-full.js` `// depends_on:` header ack `frontmatter@10`; both
   `:173` markers re-derived and re-stamped `@10` (no `@9` markers or pins anywhere in
   the shipped surface). Discharged at rest by package-lint Group E (E1+E5) PASS +
   Verification 2, recorded in the BUILT status.
2. **`[ship-verifiable]` — the durable metric home works end-to-end at rest, with a red
   record.** The Verification-3 fixture suite discharged: pre-build the declared local
   metric's wire errors `unknown metric id` (the red); post-build it derives, evaluates,
   and renders denominated; unknown ids and malformed declarations stay loud; `--strip`
   honest; C8 PASS unchanged. Recorded in the BUILT status.
3. **`[ship-verifiable]` — the bell and Finding 4 shipped whole and agree across their
   homes.** `frontmatter.md` carries *Per-section addressing (overlays)* and the widened
   `enforcement_counter:` vocabulary under one bump; `checks.md:37` walks `{overlays}`
   with the five classes + `overlay_rule_undeclared` (R3 response in place);
   `report.md` carries the widened annotations + the new slot with the five existing
   slots stable; `vlt-mint/SKILL.md:140` directs per-section (not file-level) placement
   and `:99` the widened vocabulary; `vlt-setup/SKILL.md:186` states `local_metrics:`
   durability. Discharged at rest by Verification 6-8's greps + desk-check.
4. **`[field-contingent]` — the first vault-grown metric survives an upgrade and the
   bell rings on a real overlay.** Discharging event, named: **the owner declares
   vlt-core's tripwire metric (the derive function issue #1 lost) as a `local_metrics:`
   entry with its wire after the v0.13.0 upgrade, then runs `vlt-lint` and the
   subsequent upgrade** (performer: the owner; vault: vlt-core; evidence via the
   persisted `{lint_reports}` file and the A1 hand-saved Step-4 report / upgrade
   ledger). Pass = the declared metric derives and its wire evaluates with no
   unknown-id error; the next upgrade's seed-merge and vitals overwrite leave the
   declaration and wire intact (no re-establish-by-hand); and the lint meta-check walks
   vlt-core's overlays, reporting any rule-shaped section's declaration state
   (including `overlay_rule_undeclared` on an undeclared one — vlt-core's
   locally-adopted overlay content is the live population). Fail = the declaration or
   wire needs hand re-establishment after upgrade, an unknown-id error on a declared
   metric, or an overlay-hosted rule still invisible to the meta-check.

---
*Brief authored by `build-brief` (autonomous run 2026-08-21, owner review pending on the
seven clerk-resolved dispositions — chiefly disposition 1, the direction-2 choice).
Grounding: all Arc 9 capture sites re-verified against arc10-v0.13.0 @ ca0e700 — every
site HOLDS; three grounding additions (vlt-mint:140/:99, report.md:28, vitals docstring)
in scope; zero roadmap superseding notes owed.*
