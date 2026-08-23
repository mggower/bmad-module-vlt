---
title: 'Build #5 — Mint Maturation: explicit Ideate→Validate→Build phases + resumable planning doc + the vertical-partner archetype (personalized extraction)'
status: 'BUILT 2026-06-24 — unit-verified; acceptance (a real gated mint exercising the phases/planning-doc/resume, and a personalized extraction) pending a real vault (deferred to first safe post-Phase-D upgrade per the roadmap acceptance ledger)'
build_log:
  - 'BUILT 2026-06-24. PRECURSOR (governance SSoT collapse, owner-ruled): discovered build-3/build-4 edited ONLY skills/vlt-setup/assets/governance/ and never the top-level governance/ "staging source" (README:71) — the two trees diverged since Build #1.1 (all 5 conventions + contract, assets-ahead). Owner chose COLLAPSE TO SINGLE SOURCE: git rm -r the top-level governance/ tree (11 files, all strictly older — verified no content lost), repointed README:71 + arch-spec:114 at the assets bundle. Decision-log refs left as historical records. vlt-setup unaffected (reads its own skill-relative ./assets/governance/). Part 3 (personalized extraction): lifted verbatim from vlt-core 4154b12 into the assets extraction.md — added "## Personalized extraction" section + the What-is/frontmatter-template/sources/skill-flow pointer clauses; bumped extraction version 1→2 + last_updated; reconciled the lone consumer vlt-extract''s depends_on extraction@1→@2 (stays wiki-only — bump records "verified unaffected"); contract {log} <type> set marked non-exhaustive; vlt-agent-creative non-negotiable carve-out added; frontmatter.md confirmed UNTOUCHED (single-home held). Parts 1+2+4 (vlt-mint, one restructure pass): regrouped Steps 1–4 under ## Phase 1 — Ideate / ## Phase 2 — Validate / ## Phase 3 — Build with three checkable Exit-gate lines; relocated the new-partner becoming conversation (ideation beat) from Step 3 into Phase 1, leaving scaffold-only in Phase 3; added the vertical/horizontal partner archetype guidance (Part 4) in Phase 1; added the resumable _agent/mint/{date}-{slug}.md planning doc (gated kinds only) + the On-Activation resume auto-scan branch (Part 2); council-none kinds clear Phase 2 explicitly; the build-4 convention-edit handshake gate is cross-referenced as the Phase-3 instance, not duplicated. VERIFIED: full convention→consumer handshake bipartite-consistent (all 9 consumer acks current, extraction@2 ↔ vlt-extract@2); no stale extraction@1 anywhere; frontmatter.md unchanged; top-level governance/ gone; all 3 phases + 3 exit gates present; contract non-exhaustive + creative carve-out present. NOT built (per owner rulings): vlt-lint method-traces firewall (deferred follow-up); Capability lightweight tier (separate build); decision-log relocation to _agent/mint/ (Phase D). vlt-core reference: {field-vault} @ 4154b12.'
phase: 'Phase C (Mint maturation)'
module_code: 'vlt'
created: '2026-06-24'
updated: '2026-06-24'
derives_from:
  - 'skills/reports/inbox-evolution-roadmap.md (Phase C row + Phase C scoping record)'
  - 'inbox filing #5 — vlt-mint phases + resumable planning doc (…092306…)'
  - 'inbox filing #6 — personalized extraction / vertical-partner archetype (…092514…)'
ideation_decisions:
  - 'Sequencing: Phase C built BEFORE Phase D (owner ruling 2026-06-23) — both specifiable post-B2-spike; C is ready + lighter; D follows.'
  - 'Scope: filings #5 + #6 ONLY. The vlt-lint method-traces firewall is DEFERRED as a follow-up (owner ruling); the Capability-object lightweight tier is KEPT SEPARATE (its own later build on B''s handshake machinery).'
  - 'Phasing harmonizes with build-4: the convention-edit kind already has a handshake EXIT GATE (Step 3 "Edit a convention"). Phase C names that an instance of the Phase-2/Phase-3 boundary rather than re-introducing it.'
  - 'New-partner "ideation beat" relocates conceptually into Phase 1 (Ideate); the template scaffolding stays in Phase 3 (Build). Content unchanged — boundaries are new (filing #5''s explicit instruction: regroup, do not rewrite).'
  - 'Planning doc scope: gated kinds ONLY (new partner, persona self-edit, convention edit). operation skill + capability migration stay ceremony-free (the fast in-flow path).'
  - 'Resume: auto-scan _agent/mint/ on activation for an incomplete planning doc and offer resume (filing #5 rec — one ls, frictionless).'
  - 'extraction.md + contract + Creative edits: lift verbatim from vlt-core commit 4154b12 where available; else apply the deltas in Part 3.'
  - 'personalization_sources: stays GATED per-op (n=1 bound to vlt-track by name) — NOT generalized to all extractions (do not pre-generalize; historian''s caution).'
  - 'frontmatter.md: NO change (it already defers PARA frontmatter to extraction.md; personalization_sources: is a bare-path list under rule 4 — single-home held).'
  - 'Decision-log relocation (_agent/mint/) is Phase D / §A1 — NOT here. Phase C only adds the orthogonal live/resumable planning doc; .decision-log.md stays put, unchanged in role.'
---

# Build #5 — Mint Maturation

## Thesis

Build #2 made the mint engine. `vlt-core` then minted three partners *in anger* (Dog Trainer, Health
Coach, Chef), and the engine learned two things about itself it couldn't know before it ran:

1. **A live gated mint has no visible seams.** The Dog Trainer session slid ideation → staging → build
   with no "Phase 1 complete — entering validation" boundary, so a user who wants to approve the *brief*
   before any building has no natural gate; and all session state (kind, brief, four ideation decisions,
   a mid-flow architecture pivot, the council `revise` verdict, six hardenings) lived **only in
   conversation context** — closing the session mid-flow would have lost everything. The post-hoc
   `.decision-log.md` can't serve as a resume point. *(filing #5)*
2. **The first vertical (domain) partner broke an assumption baked into the write boundary.** The Dog
   Trainer's deliverable is part general method (belongs in the wiki) and part the user's lived state
   (this dog's progress, which the dog-agnostic wiki deliberately doesn't hold) — colliding with the
   contract's most load-bearing rule (*PARA is written only through extraction, which draws from the wiki
   only*). The council found the real safety property is **method-grounding**, not path-count, and blessed
   a **bounded provenance widening**. *(filing #6)*

Both are "self-evolution growing up": the engine gains **explicit phase boundaries + a resumable planning
doc** (so a gated mint is approvable and survives a closed session), and the convention layer gains a
**recognized vertical-partner archetype** with a single, council-validated widening of what one extraction
may cite. The two filings share an origin (the same Dog Trainer mint surfaced both) and a spirit (make the
mint process legible and durable), so they ship together.

| Part | Filing | Shape |
|---|---|---|
| **1 — Phase structure + exit gates** | #5 | Regroup `vlt-mint` steps under `## Phase 1/2/3` with named exit gates (boundaries new, content same) |
| **2 — Resumable planning doc + resume branch** | #5 | New live artifact at `_agent/mint/{date}-{slug}.md` for gated kinds; activation auto-scans + offers resume |
| **3 — Personalized extraction (the widening)** | #6 | `extraction.md` + contract + Creative carve-out — bounded `personalization_sources:`, n=1 to `vlt-track` |
| **4 — Vertical-partner archetype docs** | #6 | Name the domain partner as a recognized archetype in the `vlt-mint` template/docs |

---

## Part 1 — Explicit Ideate→Validate→Build phases (filing #5)

Restructure `vlt-mint/SKILL.md`'s flat step list under three named phase headers, each ending with an
explicit **Exit gate** line. **This is regrouping + gate-naming, NOT a rewrite** — preserve every current
step's content verbatim in substance; only the headers and gate lines are new.

The mapping (current → phase):

| Phase | Absorbs current steps | Exit gate |
|---|---|---|
| **`## Phase 1 — Ideate`** | Step 1 (resolve kind/subject) + **the new-partner "ideation beat"/becoming conversation** (today nested inside Step 3) | **User confirms the brief** |
| **`## Phase 2 — Validate`** | Step 2 (blast-radius gate) + Step 2a (council + capture verdict) + resolving any `revise` and open user-decisions | **Verdict resolved (pass or revised-to-pass) + open user-decisions ruled** |
| **`## Phase 3 — Build`** | Step 3 (author from scaffold — *minus* the new-partner ideation beat, which moved to Phase 1) + Step 4 (install/register/record) | **Verified + offer to commit** |

Restructuring notes (the only real surgery):

- **Relocate the new-partner ideation beat to Phase 1.** Step 3's `Mint a new partner` currently opens with
  "The ideation beat (always — this is how a partner becomes someone)" + the two becoming paths (native
  lightweight / `bmad-agent-builder` escape hatch). Move that *conversation* under Phase 1 (it is the
  becoming that the brief-confirmation gate approves); leave the **scaffold-from-template** half in Phase 3.
  Keep the existing "two distinct moments — don't conflate them" caveat (mint-time ideation vs the partner's
  own live first-breath) intact at the Phase-1/Phase-3 seam.
- **The `convention edit` kind already has its Phase-2/3 boundary.** Build-4 wired Step 3's `Edit a convention`
  path to end with a mandatory **handshake exit gate** ("the mint cannot close while any `consumers:` skill's
  `depends_on` still pins the old version"). Phase C **names that an instance of the Phase-3 build gate** — do
  not re-introduce or duplicate it; add a one-line cross-reference so the handshake gate reads as the
  convention-edit specialization of "Verified + offer to commit."
- **Council-none kinds skip Phase 2's body but keep the header.** `operation skill` and `capability migration`
  pass straight through Validate (the gate predicate returns "no review required") — the phase structure still
  holds; they just clear Phase 2 trivially. Make that explicit so the in-flow fast path doesn't read as
  skipping a phase.
- **Gates are decision points the user controls** — the brief-approval gate (Phase 1) and the council-`revise`
  ruling (Phase 2) are exactly where the user wants a seam. Word each exit gate as a checkable predicate, not
  prose.

---

## Part 2 — The resumable planning doc + resume branch (filing #5)

A **live, resumable** artifact orthogonal to the post-hoc `.decision-log.md`. Scope: **gated kinds only**
(`new partner`, `persona self-edit`, `convention edit`). `operation skill` + `capability migration` stay
**ceremony-free** (no doc) — they are the cheap in-flow path and rarely span sessions; a doc there would tax
exactly the case the engine keeps fast.

- **Location:** `_agent/mint/{YYYY-MM-DD}-{slug}.md` — agent zone, durable, upgrade-safe. The operating
  contract already blesses ad-hoc `_agent/` owned folders (the `_agent/verification/` precedent), so **no
  contract change is required** to legitimize it. Created **lazily** on the first gated mint; `vlt-setup` need
  not scaffold `_agent/mint/` (it may, harmlessly).
- **Contents:** kind; the brief; architecture decisions + rationale; staged-artifact absolute paths; **current
  phase + done/pending checklist**; council verdict (or "not yet run"); open user-decisions + their
  resolutions.
- **Lifecycle:** created at the **start of Phase 1**; **updated at each phase boundary** (the exit-gate lines
  are the natural write points); on completion the post-hoc `.decision-log.md` entry is still written, and the
  planning doc is **left in place** (git already has it; cheap; the decision-log summarizes). State the
  distinction explicitly so the two artifacts aren't conflated: planning doc = *live/resumable*,
  `.decision-log.md` = *post-hoc/permanent*.
- **Resume activation branch:** add to `## On Activation` a branch that **auto-scans `_agent/mint/`** for an
  in-flight planning doc (a gated mint not marked complete) and **offers to resume** it — reading the doc to
  restore phase state and continuing at the live phase, analogous to how a partner reads `identity.md`/
  `thread.md` to resume. (filing #5 rec: auto-scan, not "only when the user says resume" — it's one `ls` and
  frictionless resume is the whole point.)

Subsection placement in the SKILL: introduce the planning doc under `## Phase 1 — Ideate` (where it's
created), with the per-boundary update calls noted at each phase's exit gate, and the resume branch in
`## On Activation`.

**Module-side files:** `vlt-mint/SKILL.md` only. Operating-contract line naming `_agent/mint/` is **optional
+ low-priority** (the contract already sanctions ad-hoc `_agent/` folders) — include it as a one-line symmetry
add only if it reads cleanly; otherwise skip (no functional dependency).

---

## Part 3 — Personalized extraction: the bounded provenance widening (filing #6)

The council-validated design: extraction stays the **one** verb into PARA; widen only **what a single
extraction may cite for personalization**, holding the real firewall fixed.

- **Hard invariant (unchanged, load-bearing):** every general/method claim in an extracted artifact's body
  traces to a wiki page in `sources:`. This *is* the firewall — the council confirmed it (not path-count) is
  the actual safety property.
- **Soft parameter (the one widening):** a *personalized extraction* may additionally read a partner's own
  **agent-zone operational data** for personalization, cited in a **separate** `personalization_sources:`
  frontmatter field — **never** in `sources:`. The two fields stay distinct so "is every method claim
  wiki-grounded?" remains mechanically checkable (a method claim supported only by `personalization_sources`
  is a *visible* violation). Bound **n=1 to `vlt-track` by name**; a future op extends the convention through
  its own gated mint, never inherits it. Operational-log discipline: the agent-zone source holds **state,
  never method/general knowledge**.

**Exact module-side edits** — lift verbatim from vlt-core commit `4154b12` where available; else apply these
deltas:

1. **`_meta/conventions/extraction.md`** — add the **`## Personalized extraction — drawing on agent-zone
   state`** section (hard-invariant / soft-parameter framing; `sources:` wiki-only vs separate
   `personalization_sources:`; n=1 scope bound to `vlt-track`; operational-log discipline). Add the pointer
   clauses in *What extraction is*, *Required frontmatter* (commented-optional `personalization_sources:`),
   and *Skill flow*. **`extraction.md` carries a `version:` + `consumers:` (build-4).** This edit touches the
   *rules a consumer follows* (a new optional field + provenance discipline) → **bump `version:` and walk the
   handshake** per the build-4 ceremony: confirm whether `vlt-extract` (and any other `consumers:` of
   `extraction.md`) need a matching edit, and bump each consumer's `depends_on` ack for `extraction`. *(This
   is the first real cross-phase use of the Phase-B machinery — Part 3 is itself a convention edit and should
   honor the handshake even though it's reached via build-5, not a `convention edit` mint.)*
2. **Operating contract (`_meta/vault-operating-contract.md`)** — the `{log}` `<type>` set becomes stated
   **non-exhaustive** (ops may coin a type, e.g. `vlt-track`'s `track`), mirroring the non-exhaustive `type:`
   frontmatter set. One-line change in the `{log}` section. *(The operating contract is held OUT of the
   version-handshake until Phase D — this single-line edit rides the same single-home discipline, not a
   versioned ack.)*
3. **`vlt-agent-creative/SKILL.md`** — one-line carve-out pointer in the non-negotiable: a domain partner's
   personalized extraction may list an agent-zone path under `personalization_sources:`; that is the same
   single write-path with a bounded widening, **not a second one**. (Prevents a reader of the Creative file
   alone from misreading a non-wiki source path as a violation.)
4. **`frontmatter.md`** — **NO change.** It already defers PARA-artifact frontmatter to `extraction.md` as the
   canonical reference, and `personalization_sources:` is a bare-path list covered by YAML rule 4. Single-home
   held — the new field is documented only in `extraction.md`. *(Confirm it is genuinely untouched so its
   build-4 `version:` does NOT bump.)*

---

## Part 4 — The vertical (domain) partner archetype (filing #6)

Name the **vertical (domain) partner** as a recognized archetype alongside the horizontal (function) partners
(librarian / researcher / creative), so the next domain mint has a path. `partner-agent-template.md` works
as-is; this is a **documentation add**, not a template rewrite.

- **`vlt-mint/SKILL.md`** (and/or `vlt-mint/assets/partner-agent-template.md` — place where the new-partner
  ideation beat now lives in Phase 1) — add a short note that a **vertical (domain) partner**: (a) names its
  domain self-awarely, (b) **typically needs its own operation skill**, and (c) **may need a bounded
  convention widening** like Part 3's personalized extraction. Frame it as recognized-archetype guidance the
  Phase-1 ideation beat can lean on when the becoming conversation reveals a domain (vs function) partner.
- Keep it light — n=1 today (Dog Trainer). Do **not** promote "vertical vs horizontal" to a first-class
  *contract* concept yet (open question #2 in filing #6 — wait for n=2). This is template/skill guidance only.

---

## Explicitly NOT in build-5 (and why)

- **The `vlt-lint` method-traces-to-wiki firewall check** → **DEFERRED follow-up** (owner ruling). Shipping the
  widening with prose + a `vlt-track` verify-step is acceptable: exposure is bounded (n=1, gated), and
  frontmatter segregation (`sources:` vs `personalization_sources:`) keeps it lint-able later. Note it in the
  roadmap as the next Phase-C-adjacent follow-up. *(The skeptic's precondition position is recorded; revisit if
  a second vertical partner arrives or the firewall is observed violated.)*
- **The Capability-object lightweight tier** → **SEPARATE build** (owner ruling). It solves the same
  vertical-partner problem from the other side (own-zone write → light, no ceremony) and its lane-firewall lint
  *is* the deferred firewall above — but it has its own complete plan (`vlt-partner-capabilities-ideation.md`)
  and ships on Phase B's handshake machinery as its own small build. Keeping it out keeps build-5 coherent.
- **Decision-log relocation to `_agent/mint/`** → **Phase D / §A1.** Build-5 adds only the orthogonal
  *live/resumable* planning doc; `.decision-log.md` stays exactly where it is, unchanged in role. (The two are
  deliberately distinct — don't fold them.)
- **Generalizing `personalization_sources:` to all extractions** → **no.** Stays gated per-op, n=1 to
  `vlt-track` by name (don't pre-generalize — historian's caution; revisit at n=2).
- **The resumable-working-doc pattern generalized to other ops** (`vlt-research`, big `vlt-extract`) → **defer**
  (n=1 caution). Bake it into `vlt-mint` only for now; extract a shared `_agent/{op}/` convention if a second
  op wants it.

---

## Migration / upgrade path

**None required — both filings are additive, reversible skill/convention edits.**

- **Filing #5:** pure additive `vlt-mint` edit. No data migration; no in-flight mints persist today (the gap
  being fixed). The first gated mint after upgrade just starts producing planning docs. `_agent/mint/` is
  created lazily.
- **Filing #6:** `extraction.md` + contract + Creative edits are additive + council-confirmed reversible.
  **No existing extracted artifact changes** — `personalization_sources:` is optional and absent on every
  standard extraction. Installs without a domain partner are unaffected (the allowance is dormant). Rollback
  cost ≈ the few `vlt-track` protocol files.
- The Part-3 `extraction.md` `version:` bump propagates through the build-4 handshake to its consumers — that
  is the *coherence* machinery doing its job, not a data migration.

---

## Build order

1. **Part 3 + Part 4 first (the convention layer)** — apply the `extraction.md` widening (lift from `4154b12`),
   the contract `{log}` non-exhaustive line, the Creative carve-out, and the vertical-partner archetype note.
   **Run the build-4 handshake** for `extraction.md`'s `version:` bump (walk its `consumers:`, bump acks).
   *Verify: `vlt-lint`'s convention-coherence check is green after the bump; `frontmatter.md` untouched.*
2. **Part 1 second (phase restructure)** — regroup `vlt-mint/SKILL.md` under Phase 1/2/3 headers + exit gates;
   relocate the new-partner ideation beat to Phase 1; cross-reference the existing convention-edit handshake
   gate as the Phase-3 instance. *Verify: every prior step's content is preserved; the convention-edit gate is
   referenced, not duplicated; council-none kinds clear Phase 2 explicitly.*
3. **Part 2 last (planning doc + resume)** — add the planning-doc subsection under Phase 1, the per-boundary
   update calls at each exit gate, and the resume auto-scan branch in `## On Activation`. *Verify: a simulated
   incomplete `_agent/mint/{date}-{slug}.md` is detected on activation and offered for resume; a completed one
   is not re-offered.*

Order rationale: the convention layer (3+4) is independent and can land first; the phase restructure (1) is
the scaffold the planning doc (2) attaches to, so 2 follows 1.

---

## Acceptance / verification

- **Phases visible:** `vlt-mint/SKILL.md` has `## Phase 1 — Ideate` / `## Phase 2 — Validate` / `## Phase 3 —
  Build`, each ending in a checkable **Exit gate** line. All prior step content is present (diff shows
  regrouping, not deletion).
- **Brief gate real:** Phase 1 cannot exit without explicit user brief-confirmation; the new-partner becoming
  conversation sits in Phase 1.
- **Convention-edit gate harmonized:** the build-4 handshake exit gate reads as the Phase-3 instance for the
  `convention edit` kind (referenced once, not duplicated).
- **Planning doc:** a gated mint creates `_agent/mint/{date}-{slug}.md` at Phase 1 and updates it at each
  boundary; an `operation skill` mint creates **no** doc. The doc and `.decision-log.md` are described as
  distinct (live vs post-hoc).
- **Resume works:** activation auto-scans `_agent/mint/`; an incomplete doc is offered for resume and restores
  phase state; a completed doc is not re-offered.
- **Personalized extraction:** `extraction.md` has the new section + the three pointer clauses;
  `personalization_sources:` is documented **only** there (single-home); the contract `{log}` set reads
  non-exhaustive; the Creative non-negotiable carries the one-line carve-out; `frontmatter.md` is unchanged.
- **Handshake honored:** `extraction.md`'s `version:` is bumped and every `consumers:` skill's `depends_on`
  ack is current → `vlt-lint` convention-coherence is green.
- **Vertical archetype documented:** the `vlt-mint` template/docs name the domain-partner archetype (names
  domain self-awarely / own op skill / bounded widening).
- **Reversibility:** no existing extracted artifact changed; no in-flight-mint back-compat concern.

---

## Open questions for the build

- **`extraction.md` consumer set:** confirm from build-4 which skills are in `extraction.md`'s `consumers:`
  (likely `vlt-extract`; possibly `vlt-ingest`) so the Part-3 handshake walk hits exactly the right acks.
- **vlt-core `4154b12` availability:** can the build read the vlt-core install's amended `extraction.md` +
  contract line to lift verbatim, or must it reconstruct from the Part-3 deltas? (vlt-core path:
  `{field-vault}`.)
- **Optional contract line for `_agent/mint/`:** include the one-line symmetry add or skip (no functional
  dependency — the contract already sanctions ad-hoc `_agent/` folders)?
- **Ideation-beat relocation seam:** confirm the cleanest split point so the "two distinct moments" caveat
  (mint-time ideation vs live first-breath) stays intact across the new Phase-1/Phase-3 boundary.
- **Archetype note home:** does the vertical-partner guidance read best inline in `vlt-mint/SKILL.md`'s
  new-partner Phase-1 beat, or in `partner-agent-template.md`, or both (pointer + detail)?
