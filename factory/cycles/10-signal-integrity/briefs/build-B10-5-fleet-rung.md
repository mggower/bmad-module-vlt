---
title: 'Build #B10-5 — the fleet-wide reflex rung (fleet-relevant rules stop condensing as per-partner copies; the vault-scoped always-loaded pointer layer lands, and v0.13.0 cuts here)'
status: 'BUILT 2026-08-21 — all nine F-sites landed; unit-verified at rest; the v0.13.0 release choreography deliberately NOT run (deviation 1). F-SITES: F1 contract five touches (Beat-1 rung read :187, rung passage single-home :217, ladder fleet-rung row :227, same-act overlay clause :122 worded non-enumeratively, decay row :308 per the :314 rule); F2 rule card re-derived (:20 vault-rung clause, :47 map row absorbs the ladder addition), derived_from re-stamped sha256:718c2362…f140cf3 (derived 2026-08-21), 6,239 bytes <= 8,000 (C6 PASS); F3 frontmatter.md vault-rung stanza (type: reflexes + scope: vault in place of partner:, pointers-one-per-line, behavior pointed at the contract) + the :220 sentence rescoped to the per-partner files, version 10->11; F4 nine legs re-pinned @11 (eight SKILL pins + vlt-lint-full.js header ack) + both :173 markers re-stamped @11; F5 vlt-setup seed-if-absent vault-rung block (frontmatter-only + italic hint, never-clobber wording mirrored) + :326 report enumeration widened; F6 vlt-upgrade Step-6 provisioning parenthetical widened with the vault rung seed; F7 vlt-mint :140 overlay bullet gains the same-act rung-pointer step (pointer-style, no mechanics restated); F8 four Beat-1 recitations extended identically (three shipped partners + mint template); F9 groom-pass scope gains the fleet-rung promote destination sentence (wiki-rung hand-off shape). VERIFICATION: (1) package-lint A/B/C/E PASS (Group E the check of record — E1 all eight pins @11, E5 header ack @11; D SKIPPED, no --expect-version per deviation 1); grep-after: zero frontmatter@10 in the shipped surface (skills/ minus reports), 10 @11 legs. (2) C6 PASS inside the full run; rule card 6,239 bytes recorded. (3) MARKER RE-DERIVATION (A8/R4): frontmatter.md diff shows exactly two hunks — the version line and the F3 stanza/:220 rescope — rule 4 (normalization + coexistence posture) untouched; both :173 markers verified still-true and re-stamped @11 only; R4 fan-out audit re-run: js diff is the two version stamps + the header ack — NO convRead change (convRead definition and all four call sites byte-identical); node --check clean; parse-on-intake untouched. (4) A9 FIXTURE (scratchpad, seed + three body lines): (a) convention-overlay pointer ("this vault overlays frontmatter — read {overlays}/frontmatter.overlay.md before writing frontmatter") — names the governed subject, directs the pre-act read -> VALID POINTER; (b) contract-overlay pointer ("this vault overlays the operating contract — read {overlays}/vault-operating-contract.overlay.md before any act the contract governs") -> VALID POINTER under the shipped population ("any class this contract recognizes") and shape-based falsifier WITH ZERO WORDING EDIT; (c) copy-shaped line ("session notes must always use sentence-case titles and never exceed 40 lines") — carries rule content, points at no home -> FIRES THE FALSIFIER (the red case). (5) SEED DRY-RUN: temp-dir instantiation parses (type: reflexes, scope: vault, cap/falsifier/review_after present); 555 bytes — 43 bytes over the 0.5 KB band top, attributed wholly to the brief-mandated italic hint (frontmatter alone ~370 B); recorded per the deviation clause, judged not material to S2 pricing (deviation 3). (6) cross-file grep: _agent/reflexes.md at exactly the F-site homes — contract x5, rule card x2, frontmatter stanza, setup seed :273 + report :342, upgrade :84, mint :140, four Beat-1 recitations, groom-pass :5; the rung rules stated once (F1b), every other site points. (7)-(8) per brief: no lint class shipped (R3 n/a); enumerations widened in-build (decay table, Beat 1, setup :326, upgrade :84); declared exclusions stand (partner_memory_bytes, crossLayerSlugs/lint walkers). (9) scrub clean — placeholder paths only; 30 appears only as the seed cap value, never as a module constant in prose. (10) no .decision-log.md in the tree. DELIBERATE DEVIATIONS, NUMBERED: (1) ORCHESTRATOR-RULED — release decoupled from the build commit; readiness verified separately: version strings stay 0.12.0, no bump, no tag, no push, no ff-merge; the dual bump (.claude-plugin/marketplace.json "version" + vlt-setup/assets/module.yaml module_version) and the uv run tools/package-lint.py --expect-version 0.13.0 gate remain owed to the owner-triggered release step (vlt-release). (2) F6 wording: the vault rung seed added as a sibling list item beside the agent-zone-homes parenthetical rather than nested inside it — same enumeration widened, cleaner sentence. (3) seed mass 555 B vs the ~0.4-0.5 KB priced band — the hint-line overhang recorded above, ruled not material. Ship-verifiable acceptance checks 1-3 discharged at rest this session; check 4 (the release gate) rides the decoupled release step; checks 5-6 field-contingent (the owner''s vlt-core upgrade + first post-upgrade overlay act). One commit; no version bump rode it.'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-18-094459-activation-ritual-omits-overlays-fleet-rules-land-as-per-partner-reflexes.md (Arc 9 A9-5 — the confirmed no-fleet-rung gap + the ritual-reads-no-convention sharpening; capture ruled out the rule-card host)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-5 bullet (B9-7 carried; S2 cleared it on cost; the Arc 9 roster travels whole per archive :995-1008) + roundtable A9 (non-enumerative writer population + pointer-shape falsifier, contract-overlay fixture check). Arc 9 rulings binding whole (archive inbox-evolution-arc9-roadmap.md): Q8 (:1410 — THE FLEET-WIDE RUNG ONLY; pointer-not-copy is mandatory brief text), A17 (:1439 — the rung has authors: overlay mint/amend writes the pointer line in the same act; fleet-relevant reflex promotes; the brief carries a falsifier), A21 (:1462 — S2''s negative branch pre-ruled; NOT triggered, S2 verdict affordable), D1 (:1667 — the Beat 1 {overlays} read is NOT built), R1 (contract touch re-derives the rule card).'
risk: 'moderate — carries a frontmatter@10→@11 convention bump (nine-leg consumer walk + marker re-derive, the B10-4 walk repeated) and an operating-contract edit (R1: rule-card re-derive against the 8,000-byte budget, second C6 gate this cut); and it is the v0.13.0 release build (dual version bump + --expect-version gate). No new skill, no new lint check, no new workflow.'
---

# Build #B10-5 — the fleet-wide reflex rung

Arc 9's A9-5 confirmed the shape gap with live field evidence: the always-loaded surface has
exactly two rungs — the module-shipped `vault-rule-card.md` and the **per-partner**
`reflexes.md` — and nothing vault-scoped-and-fleet-wide between them, so fleet-relevant rules
condense as N per-partner copies (or don't land at all: two partners violated the same overlay
on the same day, the second after reading the log entry recording the first's correction).
This build ships the middle rung: **`_agent/reflexes.md`** — a vault-scoped sibling of the
per-partner rule layer, read in Beat 1 by every partner, **pointer lines only, hard-capped**,
with cap/falsifier/posture declared in its own frontmatter (the contract's existing rule-layer
shape, reused not invented). S2 priced it (SPIKE CLOSED 2026-08-21): ≈+1% of eager boot at
birth, ~6% cap-full worst case — A21's negative branch is **not** triggered; B9-7 is clear on
cost. Per roundtable A9, the rung's **writer population and pointer-shape falsifier are worded
non-enumeratively** — any overlay class the contract recognizes — with B10-9's contract
overlay (next cut) in view, and this brief carries the fixture check that a contract-overlay
pointer line parses under the falsifier as shipped.

All rejected alternatives in the parent filing and the Arc 9 record are settled — do not
re-litigate: the rule-card host (clobbered — capture), the Beat 1 `{overlays}` read (design —
Q8; reinstatable only under A21's cost branch, which did not fire), rung-as-digest (recorded
alternative, A17 — **pointer stands**).

**v0.13.0 cuts after this build** (roadmap, Round 6 + release line). §Release applies.

## Brief-time dispositions

**✅ OWNER-REVIEWED 2026-08-23 (first-half review): all eight dispositions CONFIRMED —
dispositions 1 and 2 (the "chiefly" pair) live-ruled as field-proven.** The rung seeded
clean at 0.13.0, survived the 0.14.0 upgrade, took both 2026-08-23 same-act pointer
lines (frontmatter-overlay amend + the first contract overlay), and its falsifier has
not tripped; B10-10's later key-minting created no friction with the literal-path
choice; the @10→@11 nine-leg walk held through two subsequent bumps. Dispositions 3–8
batch-confirmed (the declined lint check's file-it clause remains the watch).
Review record: the arc roadmap's first-half review section.

The roadmap left no numbered brief-time question to B10-5 (its "Questions deliberately left to
brief time" list names B10-4/6/10/11 only). The dispositions below are the shape calls the
rulings deliberately left open at this altitude; the run is autonomous, so each is marked
**clerk-resolved (autonomous run 2026-08-21, owner review pending)** with its reasoning.

1. **The rung's path is the literal `_agent/reflexes.md` — no `vault_structure` key.**
   Clerk-resolved (autonomous run 2026-08-21, owner review pending). Precedent:
   `_agent/dispatch.md` and `_agent/dispatch-profile.md` are literal agent-zone paths with no
   map key (`module.yaml:39-61` maps content dirs and a few named files; dispatch never
   joined it). A new key would ripple into E2's structure-map SSoT check and B10-2's
   qualifying-key predicate for the lint fan-out for zero benefit — no shipped mechanism needs
   to resolve the rung by logical name, and every referencing site is shipped text this build
   writes. If a vault relocates its agent zone it has bigger overrides to make; nothing here
   forecloses adding a key later.
2. **The frontmatter schema addition is a rule change → `frontmatter` bumps @10→@11 with the
   full nine-leg walk.** Clerk-resolved (autonomous run 2026-08-21, owner review pending). The
   rung needs a declared schema (`frontmatter.md:203` — "the frontmatter for all three is in
   `frontmatter.md`"; a vault-scoped instance without `partner:` violates the stanza at
   `frontmatter.md:220` unless the standard says so). A new legal file shape that writers must
   follow is a rule addition, not a prose clarification — the same call B10-4 made for
   `local_metrics:` (@9→@10). Cost priced: eight skill pins + the `vlt-lint-full.js`
   `// depends_on:` header re-ack @11, plus both `per frontmatter@10` markers on
   `vlt-lint-full.js:173` re-derived (rule 4 untouched by this build) and re-stamped @11 (A8
   discipline). Roundtable A2 deliberately moved all bump arithmetic to *relative* wording, so
   this extra bump breaks no stated expectation — the B10-10/B10-11 capstone bump simply
   becomes "from the version current at brief time" (@11→@12 if nothing else moves).
3. **Schema shape: `type: reflexes` + `scope: vault` in place of `partner:`.** Clerk-resolved
   (autonomous run 2026-08-21, owner review pending). Reuses the shipped stanza wholesale
   (cap/falsifier/review_after keys identical to the per-partner seed at
   `vlt-setup/SKILL.md:257-270`); `scope: vault` is the one distinguishing key, so a reader
   can tell the rung from a misplaced partner file without path inference. Rejected: a new
   `type:` value (would widen the type vocabulary B10-11 is about to migrate) and a bare
   partner-less file (schema-violating per disposition 2's premise).
4. **Writer population and falsifier wording — the A9 non-enumerative form.** Clerk-resolved
   (autonomous run 2026-08-21, owner review pending). Population: *"any act that mints or
   amends an overlay of any class this contract recognizes writes or refreshes that overlay's
   rung pointer line in the same act; and a fleet-relevant reflex — a rule any partner in this
   vault must obey unasked — promotes here from a partner's `reflexes.md`."* No overlay class
   is named in the population sentence — today that resolves to convention overlays
   (`{overlays}/{name}.overlay.md`); the moment B10-9 ships the contract overlay the sentence
   covers it with zero edit (the A9 point). Falsifier (seeded in the rung's own frontmatter,
   field-side "file it" posture mirroring the per-partner falsifier): *"if a partner writes
   against an overlaid subject without the pre-act read after this rung named it, or a rung
   line carries rule content rather than pointing at the rule's home, the pointer shape is
   failing — file it."* The pointer-vs-copy test is on **shape** (names the governed subject +
   directs the pre-act read vs. restates content), never on a class list.
5. **No `vlt-lint` check on the rung ships this build.** Clerk-resolved (autonomous run
   2026-08-21, owner review pending). Nothing in Q8/A17/A9 orders one; the ruled enforcement
   posture is the rule-layer shape — cap/falsifier/posture in the file's own frontmatter,
   falsifier field-side. Adding a pointer-shape lint class would drag R2/R3/E4 costs into the
   release build ungoverned by any ruling. If the falsifier fires in the field, that filing is
   the evidence a check needs — the module's standing pattern (rules earn mechanisms on
   evidence). Declared out of scope, not forgotten (§Out of scope 4).
6. **Existing overlays are not backfilled with pointer lines.** Clerk-resolved (autonomous run
   2026-08-21, owner review pending). The contract's adoption posture
   (`vault-operating-contract.md:232`) is the precedent: contracts bind **at-write going
   forward**, no backfill sweep. A vault's existing overlays get their rung line at their next
   mint/amend act; the rung is vault-owned, so an owner hand-adding lines earlier is legal
   (seed body says so). Acceptance check 6 measures exactly this at-write behavior.
7. **The shipped partner Beat-1 texts update in this build; minted partners adopt
   contract-side.** Clerk-resolved (autonomous run 2026-08-21, owner review pending). The
   contract governs (adoption posture, `:232` — zero SKILL edits *required*), but the three
   module-shipped partner SKILLs and the mint template already recite the Beat-1 reflexes read
   (`vlt-agent-*/SKILL.md:24`, `partner-agent-template.md:39` — the B8-3 pattern), so leaving
   them silent would ship a stale recitation beside a changed contract. Four one-line edits; a
   minted partner's un-updated Beat-1 text remains **not an error**, per the contract's own
   sentence.
8. **Groom scope: a fleet-rung promote writes the one out-of-scope destination, wiki-rung
   style.** Clerk-resolved (autonomous run 2026-08-21, owner review pending). A17's second
   sentence ("a fleet-relevant reflex promotes to the rung") crosses `vlt-groom`'s declared
   scope ("the three memory files", `groom-pass.md:5`). The ladder already contains the shape
   for this: the wiki rung is a destination outside partner memory, handled as a hand-off
   note in the pass. The fleet rung follows suit — classification flows automatically from
   the contract's ladder table (groom-pass points at it, `groom-pass.md:11`, no enumeration
   to widen); the pass gains one scope sentence naming `_agent/reflexes.md` as the legal
   promote destination, executed under the same approval gate.

**Interim posture (R1 — the Arc 7 rule).** One rule in this build runs ahead of its subject:
the writer-population sentence covers **contract overlays**, a class B10-9 ships next cut. The
interim state is vacuously legal — no vault can hold a contract overlay before B10-9 exists,
so there is no unprotected window and nothing for a vault to do; the sentence simply binds the
moment the class is born. Everything else ships rule-and-mechanism together (the seed, the
writers, the read). Stated here per brief-anatomy §3; no shipped-text interim clause is
needed.

## Grounding record (re-ground 2026-08-21, against arc10-v0.13.0 branch @ 9a904b5)

Every Arc 9-era `file:line` was re-derived; the archive's cites (contract `:106`/`:167`/
`:199`) have all drifted under B9-2/B9-4/B10-1/B10-4 — **premises HOLD at fresh lines**
throughout; no capture premise was superseded, so no roadmap superseding note is owed (the
Arc 10 roadmap's B10-5 bullet asserts no line numbers of its own; the drifted cites live only
in the closed Arc 9 archive, which is never edited).

- Contract activation ritual: archive `:167` → **`vault-operating-contract.md:183-189`**
  (Beat 1 at `:187`; per-partner reflexes read present, no vault rung — HOLDS).
- Rule-layer shape: archive `:199` → **`:215`** (one line per rule, hard-capped,
  cap/falsifier/posture in own frontmatter — HOLDS; this is the shape the rung reuses).
- Overlay routing: archive `:106` → **`:113-122`** (overlay section; mint routing sentence at
  `:122` — HOLDS; A17's same-act clause lands here).
- Promotion ladder: **`:217-228`** (table `:219-226`; verbs `:228`) — HOLDS; no fleet rung
  row exists.
- Durable-host doctrine names "a vault-scoped sibling" as a legal carve-out class:
  **`:97`** — HOLDS (the rung is exactly this class; no doctrine edit needed).
- Decay contracts table **`:295-314`**; the closing rule at `:314` — "a new accumulating
  agent-zone file class enters this table in the act that creates it" — **binds this build**:
  the rung is a new cap-bounded agent-zone accumulator and owes its row here (F1e).
- Rule card: **`vault-rule-card.md:11`** (`derived_from: … sha256:…`), `:20` (Beat-1 reads,
  incl. per-partner reflexes), `:47` (Partner memory map row); current size **6,022 bytes**
  against `RULE_CARD_BUDGET = 8000` (`tools/package-lint.py:251`) — ~2KB headroom. HOLDS.
- Frontmatter convention: **`frontmatter.md:11-12`** (`version: 10`, nine-member
  `consumers:`), `:171` ("the contract owns behavior; this file owns fields"),
  `:204-220` (the reflexes stanza; `:220` — all three partner-private, carry `partner:`).
  HOLDS.
- Consumer legs (all currently @10 — verified by grep): `vlt-dispatch/SKILL.md:3`,
  `vlt-extract/SKILL.md:4`, `vlt-groom/SKILL.md:3`, `vlt-research/SKILL.md:3`,
  `vlt-ingest/SKILL.md:4`, `vlt-mint/SKILL.md:3`, `vlt-lint/SKILL.md:4`,
  `vlt-setup/SKILL.md:3`, plus `vlt-setup/assets/workflows/vlt-lint-full.js:11` (header ack)
  and the two `per frontmatter@10` markers both on **`vlt-lint-full.js:173`**.
- Seeding machinery: `vlt-setup/SKILL.md:222-223` (split migration seeds per-partner
  reflexes), `:257-270` (the per-partner seed block — the template the rung seed mirrors),
  `:273` (backlog seed-if-absent — the sibling pattern), `:326` (report enumeration of
  scaffolded items). `vlt-upgrade/SKILL.md:84` (Step 6 provisioning hand-off; parenthetical
  enumerates agent-zone homes). HOLDS.
- Mint machinery: `vlt-mint/SKILL.md:138-151` (*Edit a convention*; the overlay bullet at
  `:140`), `:132` (mint-a-partner seeds three memory files),
  `assets/partner-agent-template.md:39` (Beat-1 text), `:122-133` (per-partner reflexes
  seed). HOLDS.
- Groom: `vlt-groom/references/groom-pass.md:5` (scope: the three files; wiki-rung hand-off
  idiom), `:11` (classification points at the contract's ladder table — no enumeration).
  HOLDS.
- Shipped partner Beat-1 recitations: `vlt-agent-librarian/SKILL.md:24`,
  `vlt-agent-researcher/SKILL.md:24`, `vlt-agent-creative/SKILL.md:24`. HOLDS.
- Version strings both `0.12.0`: `.claude-plugin/marketplace.json:16`,
  `vlt-setup/assets/module.yaml:4`. HOLDS (release-time bump owed here).

## F-sites

### F1 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` (the rung's single home; R1 fires)

The contract is the rung's **behavioral single home** — every other site below points here.
Five touches, one file:

- **F1a — Beat 1 (`:187`).** After the per-partner reflexes clause ("…read it in the same
  breath (one line per rule; if absent or seed-empty, a no-op)"), add the rung read: *"— and
  the vault rung `_agent/reflexes.md` in the same breath (the vault-scoped pointer layer,
  fleet-wide; absent or seed-empty, a no-op — see* Partner memory*, the vault rung)"*. Keep
  the no-op clause — pre-upgrade vaults and fresh installs must not error.
- **F1b — the rung passage (new paragraph after `:215`, before the ladder at `:217`).** The
  single home for the rung's rules, containing: the file (`_agent/reflexes.md`, vault-scoped
  sibling of the per-partner rule layer, always-loaded in Beat 1 by every partner); **pointer
  lines only, hard-capped** — cap, falsifier, and enforcement posture declared in the file's
  own frontmatter (schema: `frontmatter.md`); the pointer shape (*a rung line names the
  governed subject and directs the pre-act read — "this vault overlays `frontmatter`; read
  `{overlays}/frontmatter.overlay.md` before writing frontmatter" — a line carrying rule
  content is a copy, the single-home violation the falsifier names*); the **non-enumerative
  writer population** (disposition 4's two sentences, verbatim); and at-cap discipline (edit
  one out or argue the cap — the per-partner rule, restated by pointer to `:215`). Use
  placeholder path style only — no vault-specific content.
- **F1c — ladder row (`:219-226`).** Insert between *reflex* and *identity*:
  `| fleet rung | `_agent/reflexes.md` (vault-scoped) | the rule is partner-independent — any partner in this vault must obey it unasked; pointer lines only |`
- **F1d — overlay routing clause (`:122`).** Append one sentence where mint routing already
  lives (A17's sited home): *"Minting or amending an overlay — of any class this contract
  recognizes — writes or refreshes that overlay's rung pointer line in `_agent/reflexes.md`
  in the same act (see* Partner memory*, the vault rung)."*
- **F1e — decay row (after `:304`).** The `:314` rule demands it in the creating act. Add:
  `| `_agent/reflexes.md` (the vault rung) | cap-managed in place — promote-in pairs with edit-one-out; retire by reference (the groom gate where a groom pass carries it) | at the cap, or a fired falsifier | `{archive}/_agent/reflexes.md` | cap/falsifier/posture in the file's own frontmatter (schema: `frontmatter.md`) |`

**Why:** A9-5's confirmed gap (no vault-scoped always-loaded rung); Q8's ruled shape; A17's
writer obligations; A9's non-enumerative wording. **R1 consequence:** any contract touch
re-derives the rule card — F2.

**Out-of-scope note:** the durable-host doctrine (`:97`) already names "a vault-scoped
sibling" — do not edit it; the rung is an instance, not a doctrine change.

### F2 — `…/governance/_meta/vault-rule-card.md` (R1: re-derive; second C6 gate this cut)

**Current:** `:20` names the Beat-1 reads including per-partner `reflexes.md`; `:47` maps
*Partner memory*; `:11` carries `derived_from: 'vault-operating-contract.md sha256:…'`;
6,022 bytes. **Change:** re-derive against the edited contract — `:20` gains the vault-rung
read in the same breath (one clause, e.g. *"plus the vault rung `_agent/reflexes.md` —
pointer lines to this vault's overlays, read fleet-wide"*); `:47`'s row summary may absorb
the ladder addition; re-stamp the `sha256:` to the edited contract's hash. **Bound:** total
≤ 8,000 bytes (`RULE_CARD_BUDGET`); record the resulting byte count in the BUILT status.
**Why:** R1 (Arc 9 roster, binding); package-lint **C6** fails the release on a stale
`derived_from:` sha or a busted budget — and this is the release build, so the gate is live
this commit.

### F3 — `…/governance/_meta/conventions/frontmatter.md` (the schema; the rule change that bumps)

**Current:** `:204-220` — the `reflexes.md` stanza (`type: reflexes`, `partner:`, `cap:`,
`falsifier:`, `review_after:`); `:220` asserts all three files are partner-private and carry
`partner:`; header `version: 10`, `consumers:` nine members (`:11-12`). **Change:** after the
per-partner stanza, add the vault-rung variant (disposition 3): the vault rung
`_agent/reflexes.md` uses the same `type: reflexes` schema with **`scope: vault` in place of
`partner:`** (vault-scoped, partner-independent); body lines are **pointers**, one per line,
under the same cap discipline; behavior — writers, pointer shape, promotion — lives in the
operating contract (*Partner memory*, the vault rung; the `:171` division of labor: "the
contract owns behavior; this file owns fields"). Adjust `:220`'s "all three are
partner-private" sentence so it scopes to the per-partner files and doesn't contradict the
new stanza. **Bump `version: 10` → `11`** (`consumers:` roster unchanged — no membership
change). **Why:** disposition 2 — a new legal file shape is a rule change; the B10-4
precedent.

### F4 — the nine-leg consumer walk + marker re-derive (the @11 handshake)

**Current:** eight `SKILL.md` `depends_on:` pins at `frontmatter@10` (paths in the grounding
record) + `vlt-lint-full.js:11` header ack + the two `per frontmatter@10` markers on
`vlt-lint-full.js:173`. **Change:** re-pin all nine legs `frontmatter@11`. For each of the
eight skills, this build changes no frontmatter-recitation in their bodies — the walk is
pin-plus-verify (B10-4's F7 pattern: grep each for recited frontmatter mechanics; expect
none beyond the already-reconciled sites). For the workflow: re-ack the header, and
**re-derive both `:173` markers** — rule 4 (normalization + coexistence posture) is untouched
by this build's schema addition, so the marker text stands and only the version re-stamps to
`@11` (A8: a consumer walk re-derives marked restatements, never blind-restamps — record the
re-derivation in the BUILT status). **R4 (roundtable rule):** the `:173` edit is an edit to
an ask → re-run the fan-out audit (B10-2's F8 table shape); expected result: no `convRead`
change (the rung is not a convention and no ask enforces it) — record the audit line.
**Why:** the version-handshake standing rule; Group E is the check of record.

### F5 — `skills/vlt-setup/SKILL.md` (seed the rung at birth)

**Current:** `:257-270` seeds per-partner `reflexes.md` if absent; `:273` seeds the backlog
if absent (the sibling pattern for a vault-level file); `:326` enumerates scaffolded items in
the report. **Change:** (a) add a **seed-if-absent** block for `_agent/reflexes.md` beside
the vault-level seeds (near `:273`): frontmatter per the F3 stanza — `type: reflexes`,
`scope: vault`, `created:`/`last_updated:`, `cap: 30` (the same shipped default as the
per-partner seed — thereafter vault-declared, per the Arc 9 provenance correction: never
write 30 into prose as a module constant), the disposition-4 falsifier, `review_after:` —
and an empty body with the one-line italic hint (*"One pointer line per overlaid subject —
empty at birth; written by overlay mints/amends and fleet-relevant promotions (contract,*
Partner memory*); hand-adding a line is legal — this file is vault-owned."*). **Never touch
an existing populated file** (mirror the `:223` never-clobber wording). (b) Widen the `:326`
report enumeration: "…partner `identity.md`+`thread.md`+`reflexes.md` + **the vault rung
`_agent/reflexes.md`** + `backlog` scaffolded vs. already present…". **Why:** the birth-time
obligation (a durable host is seeded at birth — Arc 9 A6 doctrine); S2's birth pricing
assumed a frontmatter-only seed (≈0.4–0.5 KB — keep the seed to that mass); R4 on the `:326`
enumeration.

### F6 — `skills/vlt-upgrade/SKILL.md:84` (provisioning reaches existing vaults)

**Current:** Step 6 hands provisioning to `vlt-setup` and enumerates "the new agent-zone
homes (`_agent/conventions/`, `_agent/mint/`, `_agent/capabilities/families/`)".
**Change:** widen the parenthetical with "the vault rung seed (`_agent/reflexes.md`,
seed-if-absent)". One line. **Why:** upgrades are how the fleet gets the rung; R4 — this
parenthetical is an enumeration of what provisioning ensures, and the build adds a member.
**Durability:** the rung is agent-zone — the upgrade's blanket never-touch covers it by
construction; no preserve-checklist line is added (§Out of scope 6).

### F7 — `skills/vlt-mint/SKILL.md:140` (the same-act writer)

**Current:** the *Edit a convention* overlay bullet (`:140`) directs the vault-local addition
to the overlay, names per-section addressing, records the mint — no rung obligation.
**Change:** append the same-act step: *"In the same act, write or refresh the overlay's rung
pointer line in `_agent/reflexes.md` (the vault rung — contract,* Partner memory*): one
pointer line naming the overlaid subject and directing the pre-act read; never rule
content."* **Why:** A17 — the rung had no author; the mint is the primary writer. The
contract carries the population rule (F1d, non-enumeratively); this is the operational
recitation at the one shipped writer, pointer-style (no mechanics restated). The generic
base-change path (`:142`) and local conventions take no rung step (§Out of scope 5).

### F8 — Beat-1 recitations: three shipped partners + the mint template

**Current:** `vlt-agent-librarian/SKILL.md:24`, `vlt-agent-researcher/SKILL.md:24`,
`vlt-agent-creative/SKILL.md:24`, and `vlt-mint/assets/partner-agent-template.md:39` each
recite the Beat-1 breath ("…plus your `reflexes.md` in the same breath…"). **Change:** in
each, extend the breath: *"— and the vault rung `_agent/reflexes.md` (the vault-scoped
pointer layer; absent or seed-empty = no-op)"*. Four one-line edits, identical wording.
**Why:** disposition 7 — the shipped recitations must not go stale beside the contract; the
template mirrors for new mints; existing *minted* partners adopt contract-side (`:232` — an
un-updated minted SKILL is not an error; do not force-patch anything vault-side).

### F9 — `skills/vlt-groom/references/groom-pass.md:5` (the promote destination)

**Current:** scope is "the three memory files"; the ladder classification (`:11`) points at
the contract's table (no enumeration to widen — F1c's row propagates automatically); the wiki
rung already models an out-of-scope promote destination. **Change:** append to the scope
paragraph: *"A promote whose target rung is the **fleet rung** writes `_agent/reflexes.md` —
the one destination outside the three files, mirroring the wiki rung's hand-off shape:
rendered in the diff like any promote (a pointer line, paired with its source-line removal),
executed under the same gate."* **Why:** A17's promote sentence crosses the pass's declared
scope; disposition 8.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row (no skill's invocation
surface changes). But per the "no bump owed is not no cost" rule, this build's gates beyond
the handshake are named: **C6** (F2 — rule-card re-derive, sha re-stamp, 8,000-byte budget),
**Group E** E1+E5 (F4 — nine legs @11, workflow header ack), **D/`--expect-version`** (this
is the release build — §Release). **E4:** no new package-lint check ships → no
`test-package-lint.py` case owed (R2 not applicable; `CASE_FLOOR` untouched).

## Out of scope (dispositioned)

1. **The Beat 1 `{overlays}` read** — rejected-because: Q8 ruled it out on design grounds
   (convention content at the identity beat); reinstatable only under A21's cost branch,
   which S2 did not trigger. Do not build it.
2. **The contract overlay mechanism and the rule-card-under-overlays posture** —
   deferred-to-build-B10-9 (Q2's narrow build; roundtable A15). This build's wording merely
   *accommodates* the class (disposition 4 + the fixture check); it ships none of it.
3. **A `vault_structure` key for the rung** — rejected-because: disposition 1 (dispatch
   precedent; E2/fan-out ripple for zero consumers).
4. **A `vlt-lint` pointer-shape check on the rung** — rejected-because: disposition 5 (no
   ruling orders it; the falsifier is the field-side instrument; a fired falsifier files the
   evidence a future check would be built on).
5. **Rung lines for local conventions and base changes** — rejected-because: A17/A9 scope the
   writer population to **overlay** mints/amends; a local convention is discovered via its
   own `consumers:` roster and lint inventory line, a base change via the handshake. A vault
   may hand-add a rung line for one (the file is vault-owned); no obligation ships.
6. **An upgrade preserve-checklist line for the rung** — already-covered-by the agent-zone
   blanket (`vlt-upgrade/SKILL.md:13` — never overwritten by construction); adding per-file
   lines to the "Before closing" list for blanket-covered files is the
   completeness-claiming-list drift CLAUDE.md warns against.
7. **Backfilling existing overlays' pointer lines (field-side)** — rejected-because:
   disposition 6 (at-write going forward, the `:232` adoption posture). Acceptance check 6
   measures the at-write behavior instead.
8. **`partner_memory_bytes` widening to count the rung** — declared exclusion (R4): the
   metric's class is per-partner files under `{partners}`
   (`vlt-vitals.py:239`); the rung is vault-scoped and outside it by definition. The rung's
   mass is cap-bounded (~2.9 KB worst case per S2) and visible on disk; if a rung-mass vital
   is ever wanted it routes upstream as a new canonical metric, never a vault hand-edit.
9. **B10-6's report-persist contract** — not touched: the rung is a governed vault file, not
   a report; it adds no reader of `{lint_reports}` or any persisted report, so E1's
   "any reader added by B10-1..B10-5" walk finds nothing from this build (noted here so
   B10-6's brief can cite it).
10. **Per-partner `reflexes.md` machinery** — untouched everywhere (seed, cap, groom
    participation, template stanza `partner-agent-template.md:122-133`).

## Verification (unit, at rest — lifecycle step 5)

1. **Handshake bipartite re-check — `package-lint` Group E is the check of record** (E1 the
   nine legs at `frontmatter@11`, E5 the `vlt-lint-full.js` header ack). A hand-written grep
   is an editing aid only, never the recorded verification. Expected: PASS with zero
   `frontmatter@10` tokens anywhere in `skills/` (confirm with a grep *after* Group E, as an
   aid).
2. **Packaging lint** — full `uv run tools/package-lint.py --expect-version 0.13.0` (this is
   the release build; A/B/C/D/E all gate). **C6** must pass against the re-stamped rule card;
   record the card's byte count (≤ 8,000) in the BUILT status.
3. **Marker re-derivation record (A8/R4)** — for both `vlt-lint-full.js:173` markers: verify
   rule 4's text in `frontmatter.md`@11 is unchanged from @10 (diff shows only the version
   line + the F3 stanza/`:220` hunks), state "re-derived, still true", re-stamp `@11`; re-run
   the fan-out audit (R4) and record "no convRead change". `node --check` on the workflow.
4. **The A9 fixture check (ship-verifiable, at rest)** — in the scratchpad, write a fixture
   `_agent/reflexes.md` per the shipped seed + three body lines: (a) a convention-overlay
   pointer (*"this vault overlays `frontmatter` — read `{overlays}/frontmatter.overlay.md`
   before writing frontmatter"*), (b) a **contract-overlay** pointer (*"this vault overlays
   the operating contract — read `{overlays}/vault-operating-contract.overlay.md` before any
   act the contract governs"*), (c) a copy-shaped line restating a rule's content. Desk-check
   each against the shipped population + falsifier wording: (a) and (b) parse as valid
   pointers — (b) **without any wording edit** (the non-enumerative test; B10-9's exact
   filename may differ, the wording must not care) — and (c) fires the falsifier (the red
   case). Record all three verdicts in the BUILT status.
5. **Seed dry-run** — instantiate the F5 seed block in a temp dir; parse its frontmatter
   (`type: reflexes`, `scope: vault`, cap/falsifier/review_after present); byte-count it
   against S2's birth band (≈0.4–0.5 KB — a seed materially heavier than the priced band is a
   deviation to record).
6. **Cross-file agreement greps** — `_agent/reflexes.md` appears at exactly the F-site homes
   (contract ×5 touches, rule card, frontmatter stanza, setup seed + report line, upgrade
   `:84`, mint `:140`, four Beat-1 recitations, groom-pass scope); the rung's *rules* (pointer
   shape, population, cap discipline) are stated **once** (F1b) — every other site points.
7. **Legal response (R3): not applicable as a lint class** — no finding class is added; the
   rung's field-side legal response is its own frontmatter falsifier ("file it"), shipped in
   the seed (disposition 5).
8. **Enumeration widening (R4)** — widened in-build: the decay table (F1e — the `:314` rule),
   Beat 1 itself (F1a), `vlt-setup:326` report enumeration (F5b), `vlt-upgrade:84`
   provisioning parenthetical (F6). Declared exclusions recorded: `partner_memory_bytes`
   (§Out of scope 8), `crossLayerSlugs`/lint walkers (the rung is an `_agent/` root file,
   not a content dir or wiki page — outside both derivations by class).
9. **Scrub** — no vault-local or personal content in any shipped edit; worked examples use
   `{overlays}/…` placeholder style; the cap default `30` appears only as a seed value, never
   as a module constant in prose (the Arc 9 provenance correction).
10. **No `.decision-log.md`** left in the working tree.

## Release (v0.13.0 — this build cuts it)

Per the roadmap's release line (Round 6 + roundtable A1): builds B10-1..B10-5 ship as
v0.13.0. In this build's commit: bump **both** version strings —
`.claude-plugin/marketplace.json:16` `"version": "0.13.0"` and
`skills/vlt-setup/assets/module.yaml:4` `module_version: 0.13.0`. Gate: **`uv run
tools/package-lint.py --expect-version 0.13.0` — tag only on exit 0**, PASS summary line in
the release commit message. Then the choreography per `vlt-release`: ff-merge
`arc10-v0.13.0` → `main`, tag `v0.13.0`, push main + tag. **Interim evidence posture (A1,
owner-ruled):** the v0.13.0 discharge runs with the owner hand-saving the upgrade's Step-4
report verbatim to a dated file — the last transcript-regime run; B10-6 retires the posture.

## Acceptance (live — appended to the roadmap ledger)

Six checks; tags per build-brief §9.

1. **`[ship-verifiable]`** — the `frontmatter@11` handshake is bipartite-consistent across
   all nine legs (eight skill pins + the `vlt-lint-full.js` header ack), both `:173` markers
   re-derived (rule 4 untouched, verified still-true) and re-stamped `@11`, zero
   `frontmatter@10` in the shipped surface, and the R4 fan-out audit re-run recorded (no
   `convRead` change). Discharged at rest by **package-lint Group E (E1+E5) PASS**, recorded
   in the BUILT status.
2. **`[ship-verifiable]`** — the rung shipped whole and agrees across its homes: the contract
   carries all five F1 touches (Beat-1 read, the rung passage as the single home, the ladder
   row, the same-act overlay clause worded non-enumeratively, the decay row per `:314`); the
   rule card is re-derived with the rung read, sha re-stamped, ≤ 8,000 bytes (**C6 PASS**);
   the `frontmatter` stanza (`scope: vault`) is in place under the @11 bump; the seed,
   provisioning line, mint same-act step, four Beat-1 recitations, and groom-pass scope
   sentence each land with pointer-not-restatement discipline. Discharged at rest by the
   Verification 6 greps + the seed dry-run.
3. **`[ship-verifiable]`** — the A9 fixture check: a **contract-overlay** pointer line parses
   under the shipped population + falsifier wording with no wording edit, a convention-overlay
   pointer likewise, and a copy-shaped line fires the falsifier (the red case). Discharged at
   rest; three verdicts recorded in the BUILT status.
4. **`[ship-verifiable]`** — the v0.13.0 release gate: both version strings at `0.13.0`,
   `package-lint --expect-version 0.13.0` exit 0 with its PASS line in the release commit
   message, ff-merge + annotated tag + push per `vlt-release`.
5. **`[field-contingent]`** — the rung arrives in the fleet without harm; discharging event
   named: **the owner's vlt-core upgrade to v0.13.0** (performer: the owner; vault: vlt-core;
   evidence via the A1 hand-saved Step-4 report + a factory read of vlt-core, which this
   machine can read). Pass = `_agent/reflexes.md` exists post-upgrade, seeded
   frontmatter-only (`scope: vault`, cap/falsifier/posture present, ≈0.4–0.5 KB — S2's birth
   band), nothing existing was clobbered (per-partner `reflexes.md` files untouched; the
   upgrade ledger records no rung-related divergence), and partner activations proceed
   normally with the no-op read. Fail = a missing or overwritten file, a seed carrying rule
   content, or an activation error on the absent/empty rung.
6. **`[field-contingent]`** — the writers write: the first overlay mint or amend in vlt-core
   after the v0.13.0 upgrade writes its rung pointer line **in the same act**; discharging
   event named: **the owner's (or a vlt-core partner's) next `vlt-mint` *Edit a convention*
   overlay act after the upgrade** (performer: the owner in vlt-core; vlt-core has standing
   overlays, so an amend is a natural near-term event; evidence: `_agent/reflexes.md` gains
   the pointer line and the mint decision-log entry records the act — read directly from
   vlt-core). Pass = the pointer line lands in the same act, pointer-shaped (names the
   subject, directs the pre-act read, no rule content), and existing overlays were **not**
   backfilled outside an act (the at-write posture holds). Fail = an overlay act closing with
   no rung line, or a rung line that restates rule content (the falsifier's copy case —
   which, if observed, is itself the filing disposition 5 waits on).
