---
title: 'Build #22 — mint & wearer surfaces (the module misdescribes who reviews a mint, who owns a mint, and where a wearer keeps its profile)'
status: >
  BUILT 2026-07-18. F1–F4 implemented per brief; at-rest verification green
  (KIND_PANEL new/retire partner = 4 lenses, cap :90 & narrowing :27/:86 untouched;
  vlt-mint provenance principle single-homed with all shipped-asset writes stripped from the
  four registration bullets, live-registry writes retained; vlt-upgrade classifier keys off
  incoming/bundled source with bracket-path fallback, B1/B2 mechanics unchanged; F4 loop-profile
  migration human-gated, both shapes, idempotent, records loop-profile-relocation). Workflow
  node --check OK. package-lint A/B/C PASS (D skipped, no --expect-version — release build's).
  No convention version moved → no handshake. No .decision-log.md created.
  Deviations from brief (all faithful completions, no scope change):
    (1) F2 :172 — additionally dropped the heavy-op retirement "(+ mirror)" shipped-asset write,
        not just the named retired-partner install-manifest clause: symmetry with the :169
        registration-mirror drop and coherence with the new "never write shipped assets" principle
        (the brief under-enumerated it while ruling heavy-op *live-CSV* deregistration unchanged —
        the live-CSV deregistration is unchanged; only its shipped mirror is dropped).
    (2) F2 :167 — trimmed the CSV-quoting bullet's trailing "live registry and the mirrored install
        manifest alike" → "every live-registry row written below," resolving the dangling reference
        to the now-removed mirror writes (the brief's own cross-surface dangling-ref check).
    (3) F4 :103 — added `loop-profile-relocation` to the `migrations_run` enumerated token list
        (has an `<other>` catch-all, but a newly-shipped token belongs in the enumeration).
module_code: 'vlt'
created: '2026-07-18'
derives_from:
  - 'inbox/2026-07-16-153000-new-partner-fields-one-lens.md (A3-13 — KIND_PANEL fields one lens on the roster-changing kinds; the build-16 bell-question interaction)'
  - 'inbox/2026-07-17-091000-vlt-mint-step4-registers-local-mints-into-shipped-artifacts.md (A3-16 — vlt-mint registration writes local mints into shipped assets; the classifier self-void interaction)'
  - 'inbox/2026-07-17-100000-loop-profile-drift-predates-build-11.md (A3-17 — build-11 rehomed the loop profile and shipped neither migration nor detector)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: >
  roadmap §Ideation rulings — A3-7..A3-17 (2026-07-17): build-22 = mint & wearer surfaces
  (A3-13 panel composition + A3-16 fix vlt-mint:152, classifier hardening + upstreaming path at brief
  + A3-17 loop-profile migration, carrying the explicit gate-2 migration check).
  Owner brief-session rulings (2026-07-18): Q17 widen — full panel (stub); Q27 upgrade migration
  offer only (lint detector deferred); Q25 harden the classifier too; Q24 defer upstreaming as a
  named debt with a live home. §Owner rulings (gate 2): a location/shape-change build owes a
  migration check discharged against the at-risk PRE-fix population.
risk: 'low-moderate — three independent surfaces (workflow code, vlt-mint prose, vlt-upgrade
  pre-flight + migrations), all additive or provenance-narrowing; no convention version moves, so
  no consumer walk. The only non-trivial edit is the vlt-upgrade classifier (F3), which touches the
  B2 durability net — re-check the B1/B2 preserve path per the durability standing rule.'
---

# Build #22 — mint & wearer surfaces

## Intent

Three filings, one shape: **the module's own descriptions of its mint-and-wearer machinery are
wrong, and nothing re-reads them.** A3-13 — the review-council convenes one lens on the kinds most
likely to create a boundary (`new partner`, `retire a partner`), so build-16's "WHERE'S THE BELL?"
rubric reaches exactly one reviewer on exactly the kind where the bell matters most. A3-16 —
`vlt-mint` tells every mint to register itself into *shipped* assets, and a mint that obeys writes
its own code into the `module.yaml agents[]` that `vlt-upgrade`'s pre-flight uses to tell local from
shipped, silently voiding its own B2 body-restore: the durability instruction attacks the durability
net. A3-17 — build-11 rehomed the loop profile into `capabilities/track.md` and shipped neither a
migration nor a detector, so two vlt-core partners drifted and build-11's own acceptance check named
them and was discharged against post-fix substitutes.

This build closes all three: widen the roster-kind panels (A3-13), split `vlt-mint`'s registration
by provenance so a field mint never touches shipped assets **and** harden `vlt-upgrade`'s
shipped-vs-local classifier so the net survives any mis-registration (A3-16), and add a human-gated
`vlt-upgrade` migration offer that lifts a mislocated loop profile into `capabilities/track.md` —
the offer being the rail that discharges A3-17's gate-2 migration check against the actual drifted
population (A3-17).

**All rejected alternatives in the parent filings and their captures are settled — do not
re-litigate them.** In particular: the panel composition is *widened*, not re-derived (Q17 ruled a
stub); the loop-profile fix is an *upgrade migration offer only* (Q27 — the lint detector and its
"should wear" roster declaration are a deferred, tracked follow-up, not this build); the deliberate
mint-upstreaming path is a *named debt*, not scoped here (Q24). The graduation-queue cluster
(A3-7/A3-8/A3-9), the build-15 residues (A3-10/A3-12), and the history-writes unit (A3-14/A3-15) are
other builds — untouched here.

## Brief-time dispositions

1. **Q17 (panel intent) — RULED by owner 2026-07-18: an unfilled stub; widen to the full panel.**
   The roster-changing kinds get `['architect', 'skeptic', 'pragmatist', 'historian']` — proposal A,
   which lands `new partner` exactly at the 4-lens cap (`vlt-review-council.js:89-90`), so nothing
   truncates. The comment records the blast-radius rationale (roster creation/removal is the highest
   blast radius) framed as *filling the stub*, not as a cost-tradeoff note (the owner ruled it was
   never a deliberate cost decision). See F1. Derives from roadmap Q17, ruled owner-only in the
   Ideation rulings §"Questions deliberately left to brief time" and answered this session.

2. **Q18 (proposal B widening semantics + the `:90` cap) — DISPOSITION: reject proposal B; ship
   proposal A only.** The filing's proposal B (let a caller *widen* an already-full kind's panel)
   collides with `vlt-review-council.js:89-90` (`if (lenses.length > 4) lenses = lenses.slice(0, 4)`)
   — widening past four silently drops a lens, and `:27` documents caller `lenses` as a *narrowing*
   affordance, the opposite semantic. Proposal A (edit the fixed `KIND_PANEL` map) needs no caller
   plumbing and never exceeds the cap. Leave the cap and `:27`'s narrowing semantics **untouched**.
   Derives from roadmap Q18 ("left to brief time"). See F1 out-of-scope note.

3. **Q23 (health-coach manifest history) — DISPOSITION: a note, no decision.** Whether an upgrade
   reverted `decision-log.md:64`'s manifest registrations or the entry was aspirational is
   unestablished and unestablishable (no skill-asset divergence net existed at 0.4.0/0.5.0, per the
   A3-16 capture) — and the fix is identical either way. Recorded here so a later reader doesn't
   re-open it; it changes nothing in F2/F3. Derives from roadmap Q23 ("unestablished, same fix
   either way").

4. **Q24 (deliberate mint-upstreaming path) — RULED by owner 2026-07-18: DEFER as a named debt with
   a live home.** No module-source path exists for deliberately upstreaming a vault-local mint into
   shipped source; the `vlt-track` precedent shows it happens ad-hoc. This build does **not** open
   that path (it is a factory act — scrub per the CLAUDE.md publishing rules, version, handshake,
   land in `skills/` — and a proper contribution ceremony is its own design). The debt is recorded
   in the roadmap's carry-forward surface with the owner's design seed: the source module is a
   **public** repo with peers, **vlt-core is the only instance permitted to ship upstream**, and the
   promising shape is an **inbox-rail analogue** — adapt vlt-core's minted inbox-filing capability to
   file *minted capabilities* upstream — with the private/public access friction as the open
   tension. Per A3-13's own lesson (*deferral without tracking is itself a failure*), this is tracked
   live, not a note in a closable tree. See Out of scope.

5. **Q25 (classifier hardening vs instruction-only fix) — RULED by owner 2026-07-18: harden the
   classifier too.** F2 fixes the instruction (a field mint never touches shipped assets); F3
   additionally makes `vlt-upgrade`'s pre-flight classifier immune to a polluted live manifest, so
   the B2 net survives *any* mis-registration, not just this instruction's. Grounded precedent: B1's
   `merge-help-csv.py` already keys shipped-ness off **bundled source**, not the live `module.yaml` —
   B1 is immune; B2's classifier is the one place still trusting the polluteable signal. Derives from
   roadmap Q25 ("left to brief time").

6. **Q27 (loop-profile rail) — RULED by owner 2026-07-18: upgrade migration offer only.** A
   human-gated `vlt-upgrade` migration offer (F4) that detects a mislocated loop profile in **both**
   observed shapes and lifts it into `capabilities/track.md`. **No** standing `vlt-lint` detector and
   **no** roster-level "should wear track" declaration this build — those are deferred as a tracked
   follow-up (see Out of scope), because the detector needs a declaration substrate that doesn't
   exist and the adoption facet it would consume is build-20's frontmatter@4 work. The migration
   offer sidesteps that substrate by detecting *mislocated profile content* directly, which needs no
   "should wear" declaration. Derives from roadmap Q27 ("left to brief time").

## F1 — `vlt-review-council.js`: widen the roster-kind panels (A3-13)

**Current state** — `skills/vlt-setup/assets/workflows/vlt-review-council.js`, the `KIND_PANEL` map
(the single source of truth for panel composition, `:50-70`):

- `:66` — `  'new partner': ['architect'],`
- `:69` — `  'retire a partner': ['architect'],`

Both field one lens and carry **no rationale comment**, unlike every neighbour: `:57`
`'add a capability': ['architect', 'skeptic', 'pragmatist']` (commented), `:61`
`'change family invariants': [...4 lenses...]` ("cross-partner blast radius"), `:67`/`:68`
`'persona self-edit'`/`'convention edit'` (full panel). The 4-lens cap is `:89-90`
(`if (lenses.length > 4) lenses = lenses.slice(0, 4)`). Build-16's mint-mode bell rubric is injected
per-lens at `:132-137` (the "WHERE'S THE BELL?" line at `:135`) and enforced by the moderator HARD
RULE at `:167` — so the bell question reaches exactly as many reviewers as there are lenses.

> **Grounding correction (line-number re-derivation).** The A3-13 capture cited the return-assembly
> at `:194-199` and `lensesFielded` at `:198`; the current file is **183 lines** and unchanged since
> build-16 (`1142fb4`) — return-assembly is `:177-183`, `lensesFielded` `:181`, moderator HARD RULE
> `:167`. The capture read a differently-numbered installed copy; the composition sites themselves
> (`:57/:61/:66/:69`), the cap (`:89-90`), and the bell injection (`:135`) all hold at the lines
> above. No later build changed this file, so this is a fresh-line re-derivation, not a
> roadmap-superseding correction — the roadmap's substantive premise (one lens on the roster kinds)
> is intact.

**The exact change** — widen both roster kinds to the full deliberative panel, adding a rationale
comment matching the neighbours:

- `:66` → `  'new partner': ['architect', 'skeptic', 'pragmatist', 'historian'], // roster creation — the highest blast radius; full panel so build-16's bell question reaches more than one lens and the historian reads the record (build-22: filled a composition stub, per owner ruling)`
- `:69` → `  'retire a partner': ['architect', 'skeptic', 'pragmatist', 'historian'], // roster removal — full panel, same rationale as 'new partner' (build-22)`

`new partner` now lands exactly at the 4-lens cap (`:89-90`) — no truncation. Keep the comment
concise; match the terse one-clause style of `:57`/`:61`, not this brief's prose.

**Why.** Build-16 turned the panel into the delivery vehicle for the boundary-bell question; a
one-lens panel on the boundary-creating kinds means that question — and the historian, the lens whose
job is to read the historical record — is absent from exactly the kind whose classifier build-16's
own still-open tail suspects of misreading the record. Widening restores the panel the roster kinds
should always have had. (Grounded: A3-13, roadmap `:810-889`; the build-16 interaction at
`:868-880`.)

**Out of scope at this site (Q18):** do **not** add caller-driven widening (proposal B) — it
collides with the `:90` cap (silent truncation) and inverts `:27`'s documented narrowing semantics.
Leave `:27`, `:86` (debate honours the caller's narrower set), and `:89-90` untouched. The
`'add a capability'` 3-lens composition (`:57`) is also untouched — it is not a roster-changing kind
and the filing did not raise it.

## F2 — `vlt-mint/SKILL.md`: split registration by provenance (A3-16, instruction fix)

**Current state** — `skills/vlt-mint/SKILL.md`, Step 4 (Install and register), the registration
bullets. The A3-16 capture cited these at `:151-154`; **grounding correction — MOVED to `:169-172`**
(builds 20 and 21 pushed them down; content is byte-identical, verified against `a117f4f` — no later
build fixed A3-16). Fresh lines:

- `:169` — heavy capability / operation skill: "register its capability row in the live help
  registry `{project-root}/_bmad/module-help.csv` **(and mirror it into the install manifest
  `{module-skills}/vlt-setup/assets/module-help.csv` so a re-install reproduces it)**".
- `:170` — minted **partner**: "Register its capability row in `{project-root}/_bmad/module-help.csv`,
  **and add its `[agent]` entry to the install manifest `{module-skills}/vlt-setup/assets/module.yaml`
  `agents[]` (mirroring the row into that folder's `module-help.csv`)**." — the primary offender.
- `:171` — capability migration: "updates the help registry attribution for the migrated op **(and
  its mirror)**".
- `:172` — retired capability / **retired partner is removed from the live `module-help.csv` and from
  the install manifest (`module.yaml` `agents[]` + `module-help.csv`)**" — the site the filing missed.

None of the four makes a provenance distinction — they read identically for a shipped partner and a
vault-local mint. The clobber pathway is grounded: `vlt-setup/SKILL.md:161` ("module-owned, not
user-authored: overwrite… on every install/update") and `vlt-upgrade/SKILL.md:48` (own-the-apply
refreshes shipped assets) — a local write into `vlt-setup/assets/*` is refreshed away every upgrade.

**The exact change** — state the provenance principle **once** (single-home), then strip the
shipped-asset writes from each bullet's field path. Recommended placement: a lead sentence for the
registration bullets (at or just above `:168`), then edits to `:169/:170/:171/:172`:

- **New principle sentence** (author to match the surrounding prose): "**Every mint `vlt-mint`
  performs runs in an installed vault, so it is vault-local: register only in the live registry
  `{project-root}/_bmad/module-help.csv`. Never write the shipped install manifest
  (`{module-skills}/vlt-setup/assets/module.yaml` `agents[]` or `.../module-help.csv`) — those are
  module-owned and refreshed on every upgrade, so a local write there is futile (clobbered), records
  a false shipped-provenance fact, and — for a partner — writes the mint into the `agents[]` that
  `vlt-upgrade`'s pre-flight reads to tell local from shipped, voiding its own B2 restore (see
  `vlt-upgrade`, Step 1). A local mint's durability is the merge's job (B1 preserves its live
  registry row) plus B2 (body restore), never a shipped-asset write. Registering into the shipped
  manifest is a factory act (module release), out of scope here.**"
- `:169` → drop the parenthetical mirror-into-`vlt-setup/assets/module-help.csv` clause; keep the
  live-registry registration.
- `:170` → drop the "add its `[agent]` entry to the install manifest… `agents[]` (mirroring…)"
  clause; keep "Register its capability row in `{project-root}/_bmad/module-help.csv`". (A partner
  "joins the roster simply by existing" as an installed `vlt-agent-*` dir — the same sentence already
  states this — so no `agents[]` write is needed for discoverability.)
- `:171` → drop "(and its mirror)".
- `:172` → for the retired **partner**, drop "and from the install manifest (`module.yaml` `agents[]`
  + `module-help.csv`)"; a local retire removes the live registry row only (heavy-op deregistration
  from the live CSV is unchanged).

**Why.** A vault-local mint gains nothing from a shipped-asset write and loses B2 coverage by it
(F3). Durability is already delivered by B1 (`merge-help-csv.py:188-230`,
`filter_rows_preserving_local`, keyed off the live dir existing) + B2 (body restore). (Grounded:
A3-16, roadmap `:1046-1109`; the self-void interaction at `:1086-1095`.)

**Registration / handshake:** none — `vlt-mint` prose, no convention `version:` moves.

## F3 — `vlt-upgrade/SKILL.md`: harden the shipped-vs-local classifier (A3-16, Q25)

**Current state** — `skills/vlt-upgrade/SKILL.md`, Step 1 pre-flight, the Minted-partners snapshot
bullet at **`:34`** (A3-16 capture cited `:33`; grounding correction — now `:34`, builds 20/21
shifted it): "every `vlt-agent-*` dir under the live skills dir whose code is **not** a shipped agent
in the module's `module.yaml` `agents[]` (librarian / researcher / creative are shipped; anything
else was minted locally)." The B2 body-restore that depends on this classification is Step 3 item 2
(`:66`). The module source determination is Step 0 (`:28`).

**The exact change** — determine shipped-ness from the **pristine incoming/bundled module source**,
not the live (installed) `module.yaml` that a mis-registering mint could have polluted. Rewrite the
test at `:34` to (author to match the surrounding prose):

- A `vlt-agent-*` dir is a **local mint** unless its code is a shipped agent in the **incoming module
  source's** `module.yaml agents[]` (the version being installed), **not** the live installed
  manifest. A local mint may historically have written itself into the live `agents[]` (Step 4 once
  told it to — see `vlt-mint`), which would otherwise misclassify it as shipped and drop it from this
  snapshot, voiding its B2 restore. This mirrors B1's own test: `merge-help-csv.py` keys
  shipped-ness off bundled source, not the live manifest — B1 is already immune, and this closes the
  same gap in B2.
- **Bracket-path fallback (builder detail):** on the own-the-apply path the incoming source is in
  hand at pre-flight, so the pristine check runs directly. On the bracket path where incoming source
  isn't reachable yet (`:28`), fall back to the known-shipped set / live manifest for the pre-flight
  snapshot and **re-verify shipped-vs-local at reconcile** once the incoming manifest is present
  (the bracket path already defers reconciliation post-install). State this fallback so the builder
  doesn't leave the bracket path asserting the pristine check it cannot run yet.

**Why.** F2 stops the module's own instruction from polluting `agents[]`, but the durability net
should not depend on every instruction (or hand-edit, or future bug) being perfect — the arc's whole
thesis is that shape-checks miss content drift. Keying the classifier off pristine source makes B2 as
robust as B1. (Grounded: A3-16 self-void finding, roadmap `:1086-1095`; owner ruling Q25,
2026-07-18.)

**Registration / handshake:** none — `vlt-upgrade` prose, no convention `version:` moves.

## F4 — `vlt-upgrade/SKILL.md`: loop-profile migration offer (A3-17, Q27)

**Current state** — `skills/vlt-upgrade/SKILL.md`, Step 3 item 5 (Migrations), `:72-80`. Build-21
established this section's pattern: the **relocation-migration discipline** (standing, `:74` — stub
the old path, don't touch worktree copies, re-point open dispatch pointers) and sibling **human-gated
offers** at `:76` (decision-log relocation), `:77` (decision-log reconcile), `:78` (overlay lift),
`:79` (proto-spec retrofit). Each records into `migrations_run` (`:88`). The wearer surface is
correct at rest: `vlt-track:16/:31/:40` reads the profile from `capabilities/track.md` and never
guesses; `capability-template.md:55-67` ships the block and `:67` states the rule ("Wear
`vlt-track`" = a `capabilities/track.md` heavy pointer, not a duplicate op). Nothing in the module
tells a partner to declare the profile inline — the module-shipped half is coherent. What's missing
is any migration for partners that carried the profile inline *before* build-11 rehomed it.

**The exact change** — add a new human-gated migration bullet in the Step 5 list (alongside `:79`,
before the catch-all `:80` "any other migrations"):

- **Loop-profile relocation (human-gated offer).** Scan installed `vlt-agent-*` partners for a
  **mislocated loop profile**: a loop-profile block (the characteristic keys —
  `root`/`target`/`subject-model`/`data-streams`/`log-tag`/`non-negotiable-gate`, per
  `vlt-mint/assets/capability-template.md`) that lives **anywhere other than the partner's
  `capabilities/track.md`**, in a partner that has **no** `capabilities/track.md` heavy pointer.
  **Detect both observed shapes:** (a) the profile inline in the partner's `SKILL.md` bullet, and
  (b) a **separate `### Loop profile` section** in the SKILL.md referenced from elsewhere in the
  file — a scan keyed to only one shape misses the other (grounded: vlt-core's dog-trainer is shape
  (a), health-coach is shape (b), roadmap `:1130-1136`). **Offer** (never auto-move; per-partner
  judgment) to lift the profile into the partner's `capabilities/track.md` (create the heavy pointer
  `procedure: { skill: vlt-track }` if absent, per the template), leaving the source location a
  one-line pointer to the new home. Model this on the **overlay-lift** offer (`:78`) — it is a
  content *lift* into the correct home, not a file *move*, so the relocation discipline's stub/
  re-point rules apply only insofar as any old path reference must stay resolvable. Record
  `loop-profile-relocation` in `migrations_run`. **Idempotent** — a partner already carrying its
  profile in `capabilities/track.md` yields nothing; a second run finds nothing mislocated.

**Why (and the gate-2 obligation).** Build-11 rehomed the profile and shipped no migration; its
acceptance check #1 named dog-trainer + health-coach and was discharged against post-fix substitutes
— the vacuity the owner's gate-2 ruling now forbids. Per that ruling, an A3-17 build **owes the
migration check explicitly**, discharged against the at-risk **pre-fix** population. This offer is
that rail: it carries dog-trainer + health-coach (a population that *could* have failed), which no
lint detector would do. There is no template delta in this build (the template is already correct),
so the gate-2 "machinery check" is trivially satisfied and the load-bearing obligation is the
migration check. (Grounded: A3-17, roadmap `:1111-1200`; gate-2 ruling `:1468-1473`.)

**Registration / handshake:** none — `vlt-upgrade` prose, no convention `version:` moves.

## Registration

**None.** No new skill, no new workflow, no convention **rule** change:

- F1 edits workflow code (`vlt-review-council.js`) — `KIND_PANEL` is not a versioned convention, so
  no handshake and no consumer walk (grounded: A3-13, roadmap `:881`).
- F2/F3/F4 edit skill prose (`vlt-mint`, `vlt-upgrade`) — no convention `version:`/`consumers:` moves,
  so no re-ack.
- No `module-help.csv` row is added (no new op or partner ships).

Non-release build: the version bump (both `marketplace.json` and `module.yaml`) rides the arc's
release build (build-23 is deliberately last), not this one.

## Out of scope (dispositioned)

- **Standing `vlt-lint` loop-profile detector + the roster-level "should wear track" declaration** —
  deferred as a **tracked follow-up debt** (Q27 ruled upgrade-offer-only). The mirror of
  `capability_skill_missing` (absent pointer → present wearer) has no substrate to check against:
  `vlt-lint:78` is file-driven (a partner with no `capabilities/` dir contributes zero files), and
  `family_instance_missing` (`:79`) only checks a family contract's `instances:` list. A detector
  needs a roster declaration of who *should* wear track, which is adoption-shaped and overlaps
  build-20's frontmatter@4 adoption facet — sequence it after build-20 settles that facet. The
  migration offer (F4) covers the actual drifted population without it.
- **Deliberate mint-upstreaming path (Q24)** — deferred as a **named debt with a live home**
  (roadmap carry-forward), with the owner's design seed recorded: public repo + peers, vlt-core is
  the only ship-upstream instance, inbox-rail-analogue as the promising shape, private/public friction
  as the open tension. A contribution ceremony is its own design; not bolted onto a field skill.
- **Caller-driven panel widening (proposal B, Q18)** — rejected: collides with the `:90` cap and
  inverts `:27`'s narrowing semantics. See F1.
- **health-coach manifest history (Q23)** — unestablished, same fix either way; a note in the
  dispositions, no work.
- **`'add a capability'` panel composition** — untouched; not a roster-changing kind, not raised by
  the filing.
- **The build-16 "never rung" classifier tail** — F1 is a *candidate* remedy (widening puts the
  historian and more bell-askers on the boundary kinds), but confirming it fixed the tail is
  acceptance-side observation, not a build claim.

## Verification (unit, at rest — lifecycle step 5)

- **F1 grep/read:** `KIND_PANEL['new partner']` and `['retire a partner']` each list all four lenses
  `['architect', 'skeptic', 'pragmatist', 'historian']` and carry a rationale comment; `new partner`
  length == 4 (== the `:89-90` cap, no truncation). Confirm `:27`, `:86`, `:89-90` are **unchanged**
  (proposal B not introduced). Optionally dry-run the workflow against a temp `mint`/`new partner`
  subject with stub personas and confirm four lenses + moderator are selected and the bell question
  is injected into each lens prompt.
- **F2 grep:** no `vlt-mint/SKILL.md` registration bullet instructs a write to
  `vlt-setup/assets/module.yaml` or `vlt-setup/assets/module-help.csv` on the field/local path; the
  provenance principle sentence is present and single-homed (stated once, the four bullets point at
  it, no restated mechanics). Confirm the live-registry registration (`{project-root}/_bmad/module-help.csv`)
  is retained for partner, heavy-cap, migration, and retire paths.
- **F3 grep/read:** the Step-1 Minted-partners test references the **incoming/bundled** source (not
  the live `module.yaml`) as the shipped-ness authority, names the pollution rationale, and states
  the bracket-path fallback. Confirm the B1 preserve path (`merge-help-csv.py` invocation at
  `vlt-upgrade` Step 3 item 1) and B2 (item 2) are **unchanged** — F3 only changes how the snapshot
  is *derived*, not the preserve/restore mechanics (durability standing rule: re-check B1/B2).
- **F4 read:** the new migration bullet is human-gated (offer, never auto-move), detects **both**
  profile shapes, is idempotent, records `loop-profile-relocation` in `migrations_run`, and sits in
  the Step 5 list under the relocation discipline (`:74`). Confirm no other migration bullet is
  disturbed.
- **Cross-surface:** `git grep` confirms no dangling reference to the removed `agents[]`-write
  instruction elsewhere (e.g. the operating contract or `vlt-setup` shouldn't cite it).
- **Handshake:** no convention `version:` moved → the bipartite re-check does not apply this build.
- **Packaging lint (mid-arc A/B/C):** `uv run tools/package-lint.py` groups A/B/C green (no version
  assertion — the `--expect-version` D gate is the release build's, not this one).
- **Scrub:** no personal/vault-local content in any changed shipped file; the F4 bullet describes the
  drift shapes generically (no vlt-core artifact paths) — the dog-trainer/health-coach evidence stays
  in the roadmap/brief, not in shipped prose (CLAUDE.md publishing + placeholder-path rules).
- **Delete** any per-skill `.decision-log.md` the build session created before finishing.

## Acceptance (live — appended to the roadmap ledger)

Rides the next ordinary vlt-core / vlt-sayari upgrade past this build:

- **F1 (panel) — non-vacuous on the next roster-changing mint:** a real `new partner` or
  `retire a partner` mint convenes the **full four-lens panel** (architect + skeptic + pragmatist +
  historian) directly via `KIND_PANEL` — *not* by the debate-mode workaround build-15 recorded — and
  build-16's bell question reaches all four. A mint of an additive/reversible kind still skips the
  council (no regression). (Discharge is non-vacuous only on an actual roster-changing mint; a run
  with no such mint leaves this open.)
- **F2 (registration) — a field mint stays local:** the next `vlt-mint` partner/heavy-cap mint on
  vlt-core registers **only** in the live `_bmad/module-help.csv`; the shipped
  `vlt-setup/assets/module.yaml agents[]` and `vlt-setup/assets/module-help.csv` remain the pristine
  shipped set (no local mint written into them); B1 still reports the local mint preserved across the
  upgrade.
- **F3 (classifier) — B2 robust:** vlt-core's four existing local mints (chef, chess-coach,
  dog-trainer, health-coach) all classify as **local** at pre-flight and appear in the minted-partner
  snapshot, driving off the pristine incoming source. (Note honestly: vlt-core's live `agents[]` is
  currently *clean* — the hardening guards a state the corrected instruction no longer produces, so a
  fully non-vacuous discharge would need a partner with a polluted `agents[]`; absent one, this
  discharges as the belt-and-suspenders it is, and the *machinery* check — a post-fix mint doesn't
  pollute — carries the weight.)
- **F4 (loop-profile migration) — gate-2 migration check, non-vacuous against the pre-fix
  population:** at vlt-core's next upgrade, the loop-profile migration offer **detects and offers to
  relocate** dog-trainer's inline profile (shape a) **and** health-coach's `### Loop profile` section
  (shape b) into each partner's `capabilities/track.md`, human-gated; on acceptance each partner's
  profile lives at `capabilities/track.md` and `vlt-track` reads it there. These two partners
  *predate* build-11's rehoming and *could* have failed — the valid gate-2 discharge; a post-fix
  wearer (chess-coach, Navigator) is **not** valid evidence for this check. Idempotent: a second
  upgrade finds nothing mislocated. **Must NOT be read as discharging the deferred lint-detector /
  "should wear" follow-up** (a separate tracked debt).

**Next lifecycle move:** a **fresh builder session** implements this brief via `bmad-workflow-builder`
— edit F1–F4, run the at-rest verification above, rewrite this brief's `status:` to a BUILT record
with numbered deviations, delete any `.decision-log.md`, one commit for the build. Then the arc
proceeds to build-23 (content-verification), the last build before the release bump.
