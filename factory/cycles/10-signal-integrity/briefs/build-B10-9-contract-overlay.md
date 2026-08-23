---
title: 'Build #B10-9 — the contract overlay (the operating contract gains its vault-local
  overlay, closing the one durable-host gap in the governance surface)'
status: 'BUILT 2026-08-22 — all six F-sites landed on arc10-v0.14.0; unit-verified at
  rest; no version bump (rides the v0.14.0 release build). F-SITES: F1 contract — the
  contract''s-own-overlay paragraph added at the end of the convention-overlay block
  (merged-on-read rule, append-only + no-handshake-keys + per-section declaration + same-act
  rung line all by pointer, birth-time obligation discharged) + the {overlays} zone-map row
  widened to "overlays (convention + contract)" + last_updated bumped; F2 rule card
  re-derived — the A15 standing pointer landed in the derived-artifact callout (:16, one
  sentence, conditional, content-never-carried), the Durability map row gains "(the
  contract''s own included)", derived_from re-stamped
  sha256:ebc24292…1ca8de5 (derived 2026-08-22), card 6,498 bytes <= 8,000 (headroom 1,502 —
  C6 PASS); F3 vlt-mint — the :40 kind parenthetical widened ("the convention file — or the
  operating contract — + its change") + the contract-route paragraph added after the three
  landing bullets (council-gated, no bump/no walk, per-section declaration, same-act rung
  line, decision-log entry, exit shape stated, existing-rule change = upstream); F4
  checks.md:42 — base resolution widened in place ({name} matching the resolved {contract}
  basename resolves to {contract}; heading-dup test compares the resolved base;
  overlay_orphan now "no corresponding base convention or contract"; legal response updated
  in the same line: "rename the overlay to its base — convention or contract — or remove
  it"); F5 vlt-upgrade :70 — one clause in the subsumption pass''s first sentence (the
  contract overlay''s base is the newly refreshed {contract}, offer covers it identically);
  F6 full-scale.md:7 — the overlayNames derivation gains the declared exclusion with its
  reason (skip the overlay named for {contract}; scanners'' convention reads never consult
  it); vlt-lint-full.js byte-untouched. VERIFICATION: (1) cross-file grep — the literal
  vault-operating-contract.overlay.md name appears in the shipped surface at exactly F1
  (contract), F2 (card), F3 (mint); F4/F5/F6 resolve via {contract}, never a hardcoded
  path; mechanics stated once in F1, pointed at everywhere else. (2) package-lint A/B/C/E
  PASS, D SKIPPED (no --expect-version, non-release build); C6 the check of record —
  derived_from sha matches the post-F1 contract, card 6,498 bytes recorded; Group E PASS
  UNCHANGED (no pin, no consumers:, no ack moved). (3) A9 fixture re-run (scratchpad): the
  contract-overlay pointer line ("this vault overlays the operating contract — read
  {overlays}/vault-operating-contract.overlay.md before any act the contract governs")
  VALID under the shipped rung population + falsifier with ZERO rung wording edits
  (diff-confirmed: rung passage :218, ladder :228 untouched) — the class B10-5''s sentence
  covered vacuously is now live. (4) orphan desk-check, real script over a scratchpad
  fixture {overlays} dir: GREEN — vault-operating-contract.overlay.md resolves its base to
  {contract}, not an orphan; GREEN — frontmatter.overlay.md still resolves to its
  convention base; RED — no-such-convention.overlay.md still flags overlay_orphan. (5) R2
  n/a (no release-gate check added/changed). (6) R3 — no new finding class; the updated
  legal-response wording names the contract case in the same checks.md:42 line. (7) R4 —
  enumerations widened in-build (F1 zone-map row, F4 orphan population, F5 subsumption
  walk, F6 declared exclusion); covered-without-edit and declared: the Decay-contracts
  {overlays} row ("append-only local rules" is class-general) and the enforcement
  meta-check''s {overlays} glob (checks.md:37). (8) scrub clean — default placeholder paths
  only. (9) no .decision-log.md in the tree. DELIBERATE DEVIATIONS: none — every F-site
  landed per the brief''s letter (wording within the builder''s granted latitude). Acceptance
  checks 1-2 (ship-verifiable) discharged at rest this session; check 3 field-contingent
  (the owner''s first live contract-overlay mint + subsequent upgrade in vlt-core). One
  commit; no version bump rode it.'
module_code: 'vlt'
created: '2026-08-22'
derives_from:
  - 'No inbox filing — Q2''s ruled build. Provenance: the Arc 9 carry-forward
    narrow-vs-general ruling (roadmap §Pre-ideation rulings Q2, RULED Round 2 2026-08-21:
    NARROW — a contract overlay), consistent with Arc 9 Round 1''s "no single durable-host
    mechanism; the plumbing is per host".'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-9 bullet (contract-overlay read
  at contract-read time; a rung pointer line, B10-5''s shape; R1 fires — rule-card
  re-derive, 8,000-byte budget re-check) + roundtable A15 (this brief rules the derived
  rule card''s posture under overlays — pointer line or recorded exemption) + roundtable A9
  (B10-5''s writer population and falsifier worded non-enumeratively with B10-9 in view —
  the contract overlay must parse under the shipped rung wording with zero edit). binds:
  Q2, R1 (Arc 9 standing rule: "no bump owed" is not "no cost" — package-lint C6 rule-card
  re-derivation + RULE_CARD_BUDGET), B10-5''s shipped rung wording.'
risk: 'low-moderate — an operating-contract edit (R1: rule-card re-derive + re-stamp
  against the 8,000-byte budget, package-lint C6 the gate of record) but NO convention
  version bump (no consumer walk, no frontmatter change, no workflow edit, no new skill,
  no new lint finding class — existing classes widen in population only).'
---

# Build #B10-9 — the contract overlay

Q2 named the gap exactly: convention overlays (Arc 2) made vault-local governance additions
durable for every `{conventions}` file, but the operating contract itself — the constitution,
refreshed on every upgrade's own-the-apply (`vlt-upgrade/SKILL.md:49` refreshes the
governance bundle `_meta/`) — has **no durable host for a vault-local addition**. Today a
vault that wants a local operating rule at contract level must hand-edit the live contract,
which the upgrade then overwrites and reports as `governance_divergence` with a routing
instruction ("route to its durable host", `vlt-upgrade/SKILL.md:109`) that has nowhere to
point for this file. The contract's own birth-time obligation
(`vault-operating-contract.md:112`: a file declared overwrite-on-update must name where
vault-local additions of its kind live, or state that none exist) is undischarged for the
contract itself.

This build ships Q2's ruled narrow answer: **a contract overlay** —
`{overlays}/vault-operating-contract.overlay.md`, append-only, read at **contract-read
time** (any reader of the contract reads the base, then applies its overlay if one exists —
the same merged-on-read rule conventions already carry at `:117`), with a rung pointer line
written in the same act (B10-5's shipped writer clause at `:123` is already worded
non-enumeratively — "an overlay of any class this contract recognizes" — and B10-5's A9
fixture proved a contract-overlay pointer line parses under the shipped rung wording with
zero edit; this build makes the class real). R1 fires: the contract edit re-derives
`vault-rule-card.md` and re-stamps its `derived_from:` sha within the 8,000-byte budget
(package-lint C6). Per Q2: **skill assets remain overlay-less** (their durability story is
B10-1's detect-preserve-reapply), and **no general mechanism is built** — this is per-host
plumbing for the one uncovered file.

All rejected alternatives are settled — do not re-litigate. In particular: a general
durable-host mechanism (Q2 / Arc 9 Round 1 — rejected), a skill-text overlay
(`vault-operating-contract.md:125` — the standing veto), and re-opening B10-5's rung
wording (A9 worded it so this build needs zero rung edits).

## Brief-time dispositions

Clerk-resolved, autonomous run 2026-08-22, owner review pending (headless posture: every
call recorded here at the point it applies).

1. **A15 — the rule card's posture under overlays: POINTER, not exemption.** ✅
   **OWNER-RULED 2026-08-23 — POINTER CONFIRMED.** The card carries the standing
   one-line conditional overlay pointer; **no card-reading ceremony is declared exempt**
   and no new exemption is minted (the consult lite-boot stays exempt by its prior
   ruling, untouched). Accepted trade, on record: a permanent ~259 B / one-line tax on
   the card — a no-op in vaults with no contract overlay — paid so the overlay cannot be
   silently bypassed during a mint ceremony; the exemption route would have shipped a
   governance mechanism with a declared hole (the wish-class R1 forbids). Budget after:
   6,498 B at B10-9, 6,789 B at B10-11, C6 PASS throughout against the 8,000 B budget. The card
   carries a **standing one-line overlay pointer** so every card-reader inherits the
   contract-overlay read; **no card-reading ceremony is declared exempt**. Grounds: the
   card is module-owned and overwritten to shipped content on every install
   (`vlt-setup/SKILL.md:148` — HOLDS as A15 cited it), so it can never carry overlay
   *content* — but a static, conditional pointer ("if the overlay exists, the contract you
   open is base + overlay") is shipped text, born of the same R1 re-derive, and costs one
   line of the card's 1,761-byte headroom (6,239 B on disk today vs `RULE_CARD_BUDGET`
   8,000, `tools/package-lint.py:251`). This closes exactly the mint-time hole A15 names:
   the actor in a `vlt-mint` ceremony has read the card, not necessarily the full contract,
   and silence would leave the vault's contract overlay unenforced at that moment. The one
   ceremony that reads neither card nor contract — the consult lite-boot
   (`vlt-dispatch/references/consult.md:9`) — is **already exempt by prior ruling** (it
   skips the rule-card/contract read entirely); this brief mints no new exemption and
   leaves that one where it is.
2. **Overlay name and base resolution.** The overlay is the resolved `{contract}` file's
   basename + `.overlay.md`, living in `{overlays}` beside the convention overlays —
   default `_agent/conventions/vault-operating-contract.overlay.md`. Stated once, in the
   contract's new clause (F1); every checker resolves the base through `{contract}`, never
   a hardcoded path.
3. **The read rule's single home is the contract's Durability section — zero per-skill
   restatements.** "Contract-read time" = any deliberate open of the contract: a
   point-of-use section open via the card's map (`vault-operating-contract.md:17`, `:186`),
   or a skill/operation JIT-read that cites a contract section. Skills that open the
   contract inherit the rule from the contract's own clause (the same inheritance that
   makes `:117` work for conventions without per-consumer edits); the card's standing
   pointer (disposition 1) covers the reader who has only the card in hand. No shipped
   skill text is edited to restate the read.
4. **No new lint finding class — existing classes widen in population.** The contract
   overlay enters `overlay_orphan` / `overlay_not_append_only` /
   `overlay_consumers_illegal` (base resolution widened, F4) and the enforcement doctrine
   meta-check's per-section walk (`checks.md:37` already globs `{overlays}/{name}.overlay.md`
   — the contract overlay is covered **by construction**, no edit; a rule-shaped
   contract-overlay section owes a per-section declaration exactly as a convention
   overlay's does, B10-4's bell). R3 consequence: the existing legal responses at
   `checks.md:42` are updated in place where their wording assumes a convention base;
   no new response text is minted.
5. **Enforcement declaration of the new clause itself: rides the Durability section's
   existing block.** The contract-overlay clause lands inside *Durability across upgrades*,
   whose declaration (`vault-operating-contract.md:100-108`, `enforcement_stage: checked`,
   checked by `vlt-upgrade` via the three divergence report keys) already covers it — the
   contract overlay's protection bell is `governance_divergence` (a hand-edited live
   contract) plus the upgrade's overlay-intact confirmation (Step 3.3). No new declaration
   block.
6. **`full-scale.md` overlayNames: one exclusion clause, honesty not mechanism.** Step 1's
   derivation ("glob `{overlays}/*.overlay.md` and collect the convention names",
   `vlt-lint/references/full-scale.md:7`) would sweep the contract overlay into
   `overlayNames`. It is inert downstream (`vlt-lint-full.js:168` only consults
   `overlayNames` for convention names its `convRead` actually reads — verified against the
   post-B10-2 workflow), but a literal builder of the arg would ship a false "convention
   names" claim. One clause excludes it with the reason. **The workflow itself is
   byte-untouched** (R4 fan-out currency not triggered: no ask, no `convRead`, no ack
   change).
7. **Mint route: the existing `convention edit` kind widens — no new kind.** The contract
   is governance; a contract-overlay mint is council-gated exactly as a convention edit is
   (`vlt-mint/SKILL.md:138`). The kind bullet (`:40`) and the *Edit a convention* routing
   (`:140-142`) gain the contract landing (F3); the boundary classifier (`:42`) already
   applies "regardless of where the mint lands".

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

**Interim posture (R1 — the Arc 7 rule): not applicable.** Rule and mechanism ship
together: the read rule, the mint route, the checker widenings, and the card pointer land in
one build. This build also *closes* the one vacuously-legal window B10-5's brief declared
(its writer-population sentence covered a class that could not yet exist); from this build
on, the sentence has a live population.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

## F-sites

Re-grounded 2026-08-22 against branch `arc10-v0.14.0` @ `aba700c` (post-B10-6/7/8). Note:
the B10-5 status's contract cites shifted by +1 (B10-6's zone-map row for
`_agent/upgrade-reports/` at `:48`); fresh lines below. The roadmap's A15 cite
(`vlt-setup/SKILL.md:148`) HOLDS exactly.

## F1 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` (the clause + the row)

**Current state.** *Durability across upgrades* (`:89-125`): the durable-host doctrine
(`:98`), the birth-time obligation (`:112` — undischarged for the contract itself), the
convention-overlay block (`:114-123`: the overlay shape `:116`, the merged-on-read rule
`:117` — "Any reader of a convention reads the base, then applies its overlay if one
exists", the carve-out rule `:118`, the mint routing + non-enumerative same-act rung clause
`:123`). The zone map's `{overlays}` row (`:41`) reads "Vault-local **append-only**
convention overlays + the stock `.baseline/`". The vault rung's worked example (`:218`) and
the fleet-rung ladder row (`:228`) need no edit (A9). The Decay-contracts `{overlays}` row
(`:317` — "append-only local rules") already covers the new file by its wording — no edit
(declared under R4 below).

**The change.**

- **Add one bolded paragraph at the end of the convention-overlay block** (after `:123`,
  before *Designed parameter reads* `:125`), pointer-not-restatement, to this effect:

  > **The contract's own overlay.** This contract is module-shipped and refreshed on
  > upgrade, so a vault-local *addition* to it lives the same way: an append-only overlay
  > at `{overlays}/` named for this file — default
  > `_agent/conventions/vault-operating-contract.overlay.md` (the resolved `{contract}`
  > basename + `.overlay.md`). **Any reader of this contract reads the base, then applies
  > its overlay if one exists** — at every contract-read: a point-of-use section open via
  > the rule-card's map, or a skill's read of a contract section. The overlay rules above
  > apply unchanged: append-only (a change to an existing contract rule is generic — file
  > it upstream; it has no overlay form), no `version:`/`consumers:`/handshake keys (this
  > contract is deliberately unhandshaked — single-home + pointers), a rule-shaped overlay
  > section carries its per-section enforcement declaration
  > (`{conventions}/frontmatter.md`, *Per-section addressing*), and minting or amending it
  > writes its rung pointer line in the same act (the writer clause above — a contract
  > overlay is a class this contract recognizes). Route via `vlt-mint`'s *Edit a
  > convention* kind (council-gated). This names the durable host for vault-local
  > additions of this file's kind, per the birth-time obligation above.

  Exact wording is the builder's within this content; keep every mechanic a pointer to
  where it already lives (the overlay rules `:116-121`, the rung clause `:123`, the
  per-section schema in `frontmatter.md`, the mint route in `vlt-mint`).
- **Widen the `{overlays}` zone-map row** (`:41`): "Vault-local **append-only** convention
  overlays" → wording that covers both classes, e.g. "Vault-local **append-only** overlays
  (convention + contract) + the stock `.baseline/`".

**Why.** Q2's ruled mechanism; discharges the `:112` birth-time obligation for the contract
itself; single-homes the contract-read rule (disposition 3).

**Out of scope at this site:** the intro (`:17`) and the activation ritual (`:186`) are not
edited — the card pointer (F2) plus the rung line (written at mint time) carry the read to
ceremonies; restating it there would be a second home. The vault rung passage (`:218`),
ladder (`:228`), decay rows (`:309`, `:317`) — untouched (A9; R4 declarations below).

## F2 — `skills/vlt-setup/assets/governance/_meta/vault-rule-card.md` (R1: re-derive + the A15 pointer)

**Current state.** 6,239 bytes; `derived_from: … sha256:bd06909a… (derived 2026-08-22)`
(`:11`, re-stamped by B10-6). The derived-artifact callout (`:16`) states the card's honest
limit (derives from the *shipped* contract, never the vault's live copy). The *Becoming*
frame (`:20`) names the Beat-1 vault-rung read ("pointer lines to this vault's overlays").
The section map's *Durability* row (`:40`) says "open before touching conventions or
durable state".

**The change.** Re-derive the card from the post-F1 contract (R1). Two content deltas:

- **The standing overlay pointer (A15, disposition 1)** — one line, in the derived-artifact
  callout at `:16` (its natural home: it is exactly a scope statement about what the card
  can and cannot carry), to this effect: *"If this vault holds a contract overlay
  (`{overlays}/vault-operating-contract.overlay.md`), the contract you open is the base
  **plus** that overlay — apply it at every contract-read; this shipped card never carries
  its content."*
- **The Durability rows absorb the new clause** as the re-derive naturally renders it (the
  act-blocking *Durability — never destroy* line at `:29` already says "a vault-local
  addition lands only where the base declares a carve-out (overlay, …)" — verify it still
  reads true, likely unchanged; the `:40` map row may gain "or the contract's own overlay"
  in its open-when clause if the re-derive warrants).

Re-stamp `derived_from:` with the new contract sha256 and today's date. **Budget:** the
additions must keep the card ≤ 8,000 bytes (headroom 1,761 B; the pointer line is ~200 B).
Package-lint **C6** is the gate of record.

**Why.** R1 (Q2's own text: any contract touch re-derives the card against the budget);
A15's ruled pointer posture.

## F3 — `skills/vlt-mint/SKILL.md` (the mint route)

**Current state.** The kinds list names `convention edit` — "(the convention file + its
change)" (`:40`). *Edit a convention* (`:138`) routes by landing zone: vault-local addition
→ overlay (`:140`, which carries the same-act rung-pointer step B10-5 added);
vault-originated new subject → local convention (`:141`); generic rule change → base +
handshake (`:142`). No route exists for the operating contract — a vault-local
contract-level rule currently has no legal mint path at all.

**The change.**

- **`:40`** — widen the kind's parenthetical: "(the convention file — or the operating
  contract — + its change)".
- **In *Edit a convention*** — add one short paragraph (after the three landing bullets,
  before *Enforcement frontmatter* `:144`), pointer-style:

  > **The operating contract routes the same way** (contract, *Durability across
  > upgrades*, the contract's-own-overlay clause): a **vault-local addition** →
  > `{overlays}/vault-operating-contract.overlay.md` — append-only, created lazily,
  > council-gated as every convention change is (Step 2), **no version bump and no
  > consumer walk** (the contract is deliberately unhandshaked); a rule-shaped section
  > carries its per-section declaration (`{conventions}/frontmatter.md`, *Per-section
  > addressing*); write or refresh the overlay's rung pointer line in `_agent/reflexes.md`
  > in the same act (the vault rung — contract, *Partner memory*); record the mint +
  > council verdict in the decision log. A **change to an existing contract rule** is
  > generic by definition — file it upstream to the module; it has no overlay form and no
  > base-edit ceremony here (the contract has no handshake to run).

  Exit shape for this route (state it in the paragraph or by pointer): overlay written
  append-only + per-section declarations present + rung line written + decision-log entry
  — no handshake gate applies.

**Why.** The mechanism is unreachable without a ceremony route; the durability doctrine
routes `vlt-mint` by exactly this rule (`vault-operating-contract.md:123`).

## F4 — `skills/vlt-lint/references/checks.md:42` (overlay-check base resolution)

**Current state.** *Overlay append-only* (`:42`): "For each `{overlays}/{name}.overlay.md`,
flag (`overlay_not_append_only`) a section heading that duplicates a base heading verbatim …
and any overlay whose `{name}` has no corresponding base convention (`overlay_orphan`)."
**Grounding addition (beyond the roadmap's letter):** as shipped, a legal contract overlay
would **misfire `overlay_orphan`** — its base is at `{contract}`, not
`{conventions}/{name}.md` — and the heading-duplication test would have no base to compare.
The `overlay_consumers_illegal` clause applies to it correctly as-is (a contract overlay
carries no handshake keys — F1).

**The change.** Widen the base resolution in place: an overlay whose `{name}` matches the
resolved `{contract}` file's basename resolves its base to `{contract}` — the
heading-duplication test compares against the contract base, and it is **not** an orphan;
`overlay_orphan` now reads "no corresponding base convention **or contract**" (legal
response updated in the same line: "rename the overlay to its base — convention or contract
— or remove it"). No new finding class (disposition 4); the enforcement meta-check at
`:37` needs **no edit** (its `{overlays}/{name}.overlay.md` glob already walks the contract
overlay; per-section semantics are identical).

**Why.** Without this, the build ships a mechanism whose first legal use trips the module's
own governance check — a false-positive class manufactured at birth.

## F5 — `skills/vlt-upgrade/SKILL.md:69-70` (overlay intact + subsumption base)

**Current state.** Step 3.3 (`:69`) confirms `{overlays}/*.overlay.md` intact (glob-covers
the contract overlay — no edit) and refreshes convention baselines. The
**overlay-subsumption pass** (`:70`) diffs each overlay's sections "against the **newly
refreshed** base `{conventions}/{name}.md`" — for the contract overlay that path does not
exist; the pass as worded either errors or silently skips the file.

**The change.** One clause in `:70`'s first sentence: the contract overlay's base is the
newly refreshed `{contract}` (the Step-2 apply refreshes the governance bundle, `:49`), so
the subsumption offer covers it identically — an overlay addition that this release's
shipped contract now covers is offered for human-gated retirement, same
`overlay-subsumption` migration record.

**Why.** The upstream rail's return leg must not have a blind spot for exactly the file
class this build creates; the contract overlay's upstream path ("a rule change is generic —
file it upstream") makes subsumption its natural end-of-life.

**Out of scope at this site:** the `governance_divergence` routing text (`:109`) already
says "route to its durable host (overlay / …)" — with F1 shipped that instruction is now
*satisfiable* for the contract with no wording change. Step 1's governance-edit detection
(`:41`) — unchanged.

## F6 — `skills/vlt-lint/references/full-scale.md:7` (overlayNames honesty clause)

**Current state.** Step 1 derives `overlayNames` by globbing `{overlays}/*.overlay.md` and
"collect[ing] the convention names that have one". A contract overlay would be collected as
a pseudo-convention name — inert in the workflow (disposition 6) but a false claim in the
derivation instruction.

**The change.** One parenthetical clause in that sentence: skip the overlay named for the
`{contract}` file — it is the contract's overlay, not a convention's, and the page
scanners' convention reads never consult it. No workflow edit (`vlt-lint-full.js`
byte-untouched; R4 fan-out currency not triggered — no ask, no `convRead`, no ack change).

**Why.** Honest derivation text; keeps the merged-on-read claim ("scanners judge each
convention merged with its overlay") exactly true.

## Registration

**None.** No new skill (no `marketplace.json` `skills[]` entry, no `module-help.csv` row —
R2 not triggered), no new workflow, and **no convention `version:` bump** — the overlay
mechanism adds no frontmatter field and changes no convention rule (`frontmatter.md` is not
edited; overlays remain deliberately unversioned per `checks.md:42`), so no consumer walk
and no re-ack. **"No bump owed" is not "no cost" (R1):** the priced non-handshake gates are
**package-lint C6** (F2's re-derive + re-stamp + `RULE_CARD_BUDGET` — the gate of record
for this build) and nothing else — **E4** n/a (no new package-lint check), **E5** n/a (no
asset-node ack touched).

## Out of scope (dispositioned)

1. **A general durable-host/overlay mechanism** — rejected by Q2 (NARROW); the plumbing is
   per host (Arc 9 Round 1). Personas and any other shipped governance file stay
   overlay-less; a future need is its own filing, not this build's stretch.
2. **Skill-text overlays** — the standing veto (`vault-operating-contract.md:125`)
   unchanged; skill durability remains B10-1's detect-preserve-reapply.
3. **B10-5's rung wording** — zero edits (A9's non-enumerative form covers the new class;
   B10-5's fixture verdict (b) proved it). Re-confirmed at verification, not re-worded.
4. **A `vlt-lint` check on the rung pointer lines** — stays out per B10-5's disposition 5
   (rules earn mechanisms on evidence).
5. **The Decay-contracts `{overlays}` row** (`:317`) — no edit: "append-only local rules"
   already covers the contract overlay; declared under R4 below, not silently assumed.
6. **The enforcement meta-check** (`checks.md:37`) — no edit: its glob already walks the
   contract overlay per-section (B10-4's machinery inherits whole).
7. **`vlt-setup`** — no edit: setup never writes or clobbers overlays (`SKILL.md:151`'s
   overlay-zone posture); the contract overlay is born only by mint. The rule-card
   overwrite posture (`:148`) is exactly what A15's pointer ruling is built on — unchanged.
8. **Contract baseline / divergence detection** — governance divergence remains the
   upgrade's shipped-source comparison (Step 1 `:41`); no `.baseline/` copy of the
   contract is minted (out of Q2's scope; the overlay removes the *reason* to hand-edit).
9. **Backfill** — no sweep converts any vault's existing hand-carried contract deviation
   into an overlay; the route exists at-write going forward (the contract's adoption
   posture, `:236` precedent). `governance_divergence` + its now-satisfiable routing text
   is the migration path, human-gated at upgrade time.

## Verification (unit, at rest)

1. **Cross-file agreement greps** — `vault-operating-contract.overlay.md` appears at
   exactly the F-site homes (contract clause F1, card pointer F2, mint route F3, checks
   base-resolution F4, upgrade subsumption F5, full-scale exclusion F6) and **nowhere
   else**; the mechanics (append-only, merged-on-read, per-section declaration, same-act
   rung write) are stated once in F1 and pointed at everywhere else — no restatement.
2. **Package-lint A/B/C/E** (mid-arc run; D/`--expect-version` rides the release build).
   **C6 is the check of record**: card re-derived, `derived_from:` sha matches the post-F1
   contract, size ≤ 8,000 bytes (record the byte count in the BUILT status). Group E must
   still PASS **unchanged** (regression: no pin, no `consumers:`, no ack moved — a Group-E
   delta means this build did something it ruled out).
3. **Fixture re-run (the A9 line, now with a live class)** — re-run B10-5's fixture case
   (b) against the shipped post-build text: a contract-overlay pointer line ("this vault
   overlays the operating contract — read
   `{overlays}/vault-operating-contract.overlay.md` before any act the contract governs")
   parses under the rung's shipped population + falsifier **with zero wording edit**;
   record the verdict.
4. **Orphan-widening desk-check (red + green)** — against a temp fixture `{overlays}` dir:
   (green) `vault-operating-contract.overlay.md` resolves its base to `{contract}` under
   F4's wording — not an orphan; (red) a `no-such-convention.overlay.md` still reads as
   `overlay_orphan`. Record both verdicts.
5. **R2 (fixture extension): not applicable** — no release-gate check added or changed
   (C6's behavior is untouched; only its input files change).
6. **R3 (legal response):** no new finding class; the widened `overlay_orphan` /
   `overlay_not_append_only` population carries its updated legal-response wording **in the
   same `checks.md:42` lines** (F4) — verify the response text names the contract case.
7. **R4 (enumeration widening) — substantive.** The new file class enters every
   enumeration that would otherwise exclude it, in this build: the `{overlays}` zone-map
   row wording (F1), the orphan/base-resolution population (F4), the subsumption walk
   (F5), the `overlayNames` derivation (F6, as a **declared exclusion** with its reason).
   Two enumerations are covered **without edit** and declared so: the Decay-contracts
   `{overlays}` row (`:317` — "append-only local rules" is class-general) and the
   enforcement meta-check's `{overlays}` glob (`checks.md:37`). No silent omission.
8. **Scrub** — no personal or vault-local content in any changed shipped file; the worked
   pointer-line examples use the default placeholder paths already in the contract.
9. **No `.decision-log.md`** left in the working tree.

*(No Release section: B10-9 is not called as a release build — the v0.14.0 dual bump +
`--expect-version` gate ride whichever build cuts the release, per the roadmap's release
line and declared fold order.)*

## Acceptance (live — appended to the roadmap ledger)

Three checks.

1. **`[ship-verifiable]`** — the contract overlay shipped whole and agrees across its six
   homes: the contract clause (merged-on-read rule + birth-time obligation discharged +
   `{overlays}` row widened), the re-derived card carrying the A15 standing pointer with
   `derived_from:` re-stamped ≤ 8,000 bytes (**C6 PASS**), the mint route (council-gated,
   no-handshake, same-act rung line), the `checks.md:42` base-resolution widening, the
   upgrade subsumption base clause, the `full-scale.md` declared exclusion — all
   pointer-not-restatement, `vlt-lint-full.js` byte-untouched, **package-lint A/B/C/E
   PASS with Group E unchanged**. Discharged at rest by the verification greps +
   fixture/desk-check verdicts recorded in the BUILT status.
2. **`[ship-verifiable]`** — the A9 seam holds with zero rung edits: the fixture re-run
   (verification 3) shows a contract-overlay pointer line VALID under the shipped rung
   population + falsifier, and the orphan desk-check (verification 4) shows the
   red-then-green pair (unknown-name overlay still orphans; the contract overlay does
   not). Discharged at rest.
3. **`[field-contingent]`** — the first live contract overlay is born, enforced, and
   survives; discharging event named: **the owner mints a vault-local contract-level
   addition in vlt-core via `vlt-mint`'s widened `convention edit` route, then runs the
   subsequent upgrade** (performer: the owner with a partner at the wheel; vault:
   vlt-core — factory-readable; nothing schedules this event, and the owner can legally
   seed it — a standing local operating rule is a natural candidate). Pass = the overlay
   lands at `_agent/conventions/vault-operating-contract.overlay.md` append-only with a
   per-section declaration on any rule-shaped section, the rung pointer line is written
   **in the same act** with the decision-log entry, the next `vlt-lint` governance pass
   flags **no** `overlay_orphan` for it, and the next upgrade leaves it byte-intact while
   running the subsumption offer against the refreshed contract base. Fail = an orphan
   flag on a legal overlay, a mint that closes without the rung line, a clobbered overlay
   on upgrade, or a contract-level addition hand-edited into the live contract because the
   route was unfindable.
