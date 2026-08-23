---
title: 'Build #18 — the durability cluster (the upgrade rail''s missing return legs, and the overlay reach it always assumed)'
status: 'BUILT 2026-07-08 — all six F-sites landed; unit verification at rest PASS. Verified: no version drift (all conventions at their build-16 versions; no `depends_on` moved — durability-only, no consumer walk); F3 overlay-pairing clause present exactly once in each of the five readers (ingest/extract/research/track/lint), each resolving the `overlays` logical name; F5 shipped surface clean of live artifact paths (build-15''s `2026-06-13` leak absent; the sole dated-path hit `spec.md:38` is a compliant stock-cast placeholder, not a violation); F1/F2 report keys (`skill_asset_divergence`, `skill_manifest_missing`, `overlay-subsumption`) threaded through vlt-upgrade Steps 1/2/4/5 + Verify and the vlt-setup manifest step; `uv run tools/package-lint.py` → A/B/C PASS (D skipped — `--expect-version` is the release gate). Python fixture dry-runs PASS: F1 manifest builds over shipped `vlt-*`+workflows excluding `vlt-agent-*`, detects exactly a hand-edited file, handles manifest-missing; F2 subsumption prompts retire on a base-covered overlay section and spares a genuinely-additive one (no false retire). Deviations/notes, all minor: (1) the F1 manifest and F2 pass are prose instructions (no shipped script), mirroring the build-6 convention-baseline stash which is likewise prose — verified by fixture, not a committed tool. (2) The `overlay-subsumption` migrations_run enum entry was added in the same edit as `skill_asset_divergence` (edit ordering, not scope drift). (3) vlt-track''s `depends_on` deliberately unchanged — it is a convention *reader*, not a handshake consumer (F3 disposition). (4) vlt-track''s `health-coach`/`dog-trainer` domain slugs KEPT per disposition 5 (generic domain illustrations, not artifact-path leaks). Grounding correction carried: build-16 made vlt-research a frontmatter@3 consumer (`vlt-research/SKILL.md:3`), so the roadmap''s A3-6-LB1 "non-consumer today" note is superseded — research is overlay-blind and joined F3. Last build in 0.6.0 (14+15+16+18); the release carries the 0.6.0 version bump + the pre-tag `--expect-version 0.6.0` gate (see Release) — NOT done in this build (versions remain 0.5.0).'
module_code: 'vlt'
created: '2026-07-08'
derives_from:
  - 'inbox/2026-07-06-091004-no-boundary-without-a-bell.md (A3-4 LB2 — skill-asset divergence net)'
  - 'inbox/2026-07-06-091006-review-after-freshness-key.md (A3-6 LB1 overlay-aware reads + LB2 overlay-subsumption + LB3 handshake overlay-axis)'
  - 'inbox/2026-07-06-091001-spec-convention.md (A3-1 LB1 move-safety + LB2 worked-example placeholder + LB3 relay re-pointing)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-06): build-18 is the durability cluster and gets its OWN build (not riding parents, not deferred to Arc 4); ships in 0.6.0 (rationale: the divergence net + subsumption pass must protect the 0.6.0 upgrade run itself — vlt-core''s planned local template edits would otherwise be silently clobbered by that very upgrade); module-owned executable/asset home is module-owned + overwrite-on-update, vault never edits (the `.baseline/` + workflows precedent); build-15 shipped the two 091001 *instances*, build-18 ships the *rules*.'
risk: 'moderate — all durability/upgrade/activation machinery, no convention rule change, so NO version bump and NO consumer walk in this build. The one genuinely new mechanism is the skill-asset baseline net (F1: a vlt-setup stash + a vlt-upgrade detect/preserve/report pass, mirroring the build-6 convention `.baseline/` net exactly). Everything else is additive prose + one migration pass + activation-read rewording. No destructive migration anywhere (subsumption + skill-divergence are both detect-and-report/human-gated).'
---

# Build #18 — the durability cluster

Goal: close the four durability latent bugs the Arc 3 capture surfaced as one
B1-posture cluster (roadmap §Cross-cutting threads, final bullet), all in the machinery
that is supposed to make a vault's local evolution survive an upgrade. Three are the
**missing return legs of rails the module already half-built**, and one is a **reach the
convention consumers always assumed but never made explicit**:

1. **091004 LB2 — shipped skill assets have no divergence net.** Conventions get
   `{overlays}/.baseline/` + lint's base-divergence check + vlt-upgrade's preserve-and-flag;
   skill files (including the mint templates) get nothing. A local edit to an installed
   `vlt-*` skill asset is silently clobbered on upgrade — no snapshot, no flag. This build
   gives skills the same net conventions have had since build-6.
2. **091006 LB2 — no overlay-retirement path in vlt-upgrade.** Merge-not-replace *preserves*
   overlays; nothing reconciles an overlay whose addition the refreshed base has now
   **absorbed** (upstreamed). Without it, every future local-prototype→upstream round trip
   leaves a shadow definition. This build ships the subsumption pass — **the coupling that
   put build-18 in 0.6.0** (build-16's Migration note names it explicitly).
3. **091006 LB1 — overlay resolution is indirection-dependent.** Consumers' On-Activation
   says "read `{conventions}/{name}.md`" and never names `{overlays}` — overlay reach relies
   on the base's own "read together with the overlay" note being followed. Make it explicit
   in every convention reader.
4. **091001 LB1 + LB3 — relocation migrations have no standing discipline.** Build-15
   shipped the proto-spec-retrofit *instance* (stub the old path, re-point open pointers);
   the *generalized rules* (worktree-copy safety, open-pointer re-pointing for every move)
   were explicitly deferred here. Plus 091001 LB2's worked-example placeholder rule (build-15
   fixed the dispatch *instance*; the *rule* is this build) and its punted `vlt-track` slug.

Also lands **091006 LB3** — the handshake's missing overlay axis — as a one-sentence
stated property (it is deliberately absent, not accidentally; say so).

**All rejected alternatives in the parent filings are settled — do not re-litigate.**
This build adds no doctrine and no schema; it is durability plumbing.

## Brief-time dispositions (the cluster's carried open questions, resolved here)

1. **Skill-asset net mechanism (091004 LB2, one-shot): a checksum manifest, not a full
   file stash.** The convention `.baseline/` copies whole files because there are seven
   small ones and a diverged base's prior *content* must be re-expressible. The shipped
   skill surface is ~14 `vlt-*` trees (SKILL.md + assets + workflows) — a full stash is
   heavy on every install/update. A **SHA-256 manifest** (`{overlays}/.baseline/.skill-manifest`)
   is enough for detect-and-report; on the rare divergence hit, Step 1 copies just the
   *diverged* files' content into the working note/ledger, so the "prior content preserved"
   promise holds without stashing everything. (The filing said "baseline **or** checksum" —
   this takes the checksum branch.)
2. **What the skill manifest covers:** exactly the files vlt-upgrade's own-the-apply
   refreshes — the shipped `vlt-*` skill trees (SKILL.md + `assets/**`) and the
   `.claude/workflows/*.js`. It **excludes** unshipped `vlt-agent-*` dirs, the agent zone,
   and the governance bundle (already covered by the convention `.baseline/`). Same seam as
   Step 2's copy — one exclusion list, one home.
3. **Relocation discipline home (091001 LB1/LB3): a standing preamble in vlt-upgrade
   Step 3 item 5 (Migrations).** Every move migration obeys it; build-15's
   proto-spec-retrofit stops restating the stub/re-point mechanics and cites it (single-home).
4. **Worked-example placeholder rule home (091001 LB2): a CLAUDE.md standing rule.** It is a
   factory *authoring* discipline (which files may reference which paths), not shipped module
   mechanics — and CLAUDE.md already carries the scrub rule it sharpens (Git & publishing).
   Tracked + public, consistent with build-14's `CLAUDE.md:71` amendment.
5. **`vlt-track/SKILL.md` `health-coach`/`dog-trainer` slugs (build-15 punt): KEEP — they
   are generic *domain* illustrations, not a live-install leak.** 091001 LB2 targets artifact
   *paths* coupled to a specific install (`_agent/handoffs/2026-06-13-…`), and the shipped
   surface is clean of those (Verify). `health-coach` appears in the shipped surface only in
   `vlt-track` (grep: all other hits are gitignored `skills/reports/`), as one of the
   canonical vertical-partner domain examples (dog-training = multi-subject, health = single-
   subject) the module has used throughout. Genericizing one instance would be inconsistent
   and lose the illustration's teaching value. The rule F5 ships prevents the real hazard
   (artifact-path coupling) without touching domain illustrations.
6. **Handshake overlay axis (091006 LB3): state the property, don't build machinery.**
   `depends_on` pins are flat base-only `name@version` scalars; overlays are deliberately
   *unversioned* local additions and carry no handshake axis — by design, not omission. One
   sentence at the overlay check that owns the adjacent rule (F6). No lint behavior change.
7. **No version bump, no consumer walk.** Nothing here changes a convention's *rules* — the
   overlay-aware reads change consumers' activation *procedure*, not `frontmatter.md`'s text;
   the durability edits are upgrade/setup machinery. Every convention stays at its
   build-16 version; no `depends_on` moves. (Confirmed in Verify.)

## F1 — 091004 LB2: the skill-asset divergence net (mirror the convention `.baseline/`)

The convention net has three organs — a **stash** written by setup
(`vlt-setup/SKILL.md:147`), a **detect** at upgrade pre-flight
(`vlt-upgrade/SKILL.md:35`), and a **report** (`convention_base_divergence`, post-flight +
ledger + lint's `:76` check). Skills get the same three, scoped per disposition 2.

- **(a) Stash — `vlt-setup/SKILL.md`**: after the existing convention-baseline stash
  (`:147`, the build-6 "Stash the stock baseline" step), add a sibling step that writes a
  **SHA-256 manifest** of the shipped skill surface to `{overlays}/.baseline/.skill-manifest`
  (one `path\tsha256` line per shipped file across the `vlt-*` trees + `.claude/workflows/*.js`;
  the workflows dir is resolved at `vlt-setup` install time, same list it already copies at
  §2a `:151-160`). Module-owned, **overwrite on every install/update** (identical posture to
  the convention baseline and the workflows — say so, cite `:147`). It lets vlt-upgrade tell
  a local hand-edit of a shipped skill asset (live ≠ manifest) from a clean install
  (live == manifest).
- **(b) Detect — `vlt-upgrade/SKILL.md` Step 1 (pre-flight, `:31-40`)**: add a snapshot line
  beside "Base convention divergence" (`:35`) — **Skill-asset divergence**: for each file in
  `{overlays}/.baseline/.skill-manifest`, recompute its SHA against the live copy; a file that
  **differs** was hand-edited locally (should have been upstreamed) — record it as divergence
  and **copy its current content into the working note** (only the diverged files, cheap) so
  the refresh doesn't lose it. If the manifest is **missing** (pre-0.6.0 installs), record
  `skill_manifest_missing` and seed it best-effort from the incoming source this run — the
  exact `baseline_missing` handling at `:35`, verbatim in shape.
- **(c) Preserve — Step 2 (`:44`)**: the own-the-apply already "refreshes shipped files";
  extend the parenthetical so a skill asset recorded as locally-diverged in Step 1 is
  refreshed too, **but its prior content is preserved in the ledger and flagged in the
  post-flight report** — the exact sentence the base-convention case already carries at `:44`
  ("its prior content is preserved in the ledger and flagged"). One clause, same treatment.
- **(d) Report — Step 4 post-flight (`:86-90`) + Step 5 ledger (`:109-111`)**: add
  `skill_asset_divergence: [<path: shipped skill asset was hand-edited (prev content preserved
  in ledger) — re-apply locally or upstream>, ...]` to the report block (beside
  `base_divergence` `:88` and `governance_divergence` `:90`) and the matching ledger line
  (beside `:110`). Fold it into the `:95` detect-and-report framing sentence (it never
  silently clobbers a local edit; it does not auto-merge — a hand-edited skill is the user's
  to re-apply or upstream, since skills have no overlay mechanism). Refresh the manifest to
  the new shipped versions as part of the apply (mirrors baselines_refreshed `:87`).
- **(e) Verify checklist (`:127`)**: add "the `.skill-manifest` exists and was refreshed to
  the shipped versions" to the closing checklist.

**Out of scope for F1:** no lint-time half. The convention net has a lint mirror (`:76`)
because lint already reads `{conventions}`; lint does not read the installed skill trees'
provenance, and adding that is a new jurisdiction — the upgrade-time half alone closes LB2's
casualty-in-waiting (the mint-template clobber). A lint skill-divergence check is a future
candidate, not this build.

## F2 — 091006 LB2: the overlay-subsumption pass (the rail's return leg)

`vlt-upgrade/SKILL.md` Step 3 item 3 (*Conventions — overlays + baseline*, `:64`). Today it
reads "Overlays … were never touched — confirm they are intact." Add, **after** the baseline
refresh in that same item: an **overlay-subsumption pass** — for each
`{overlays}/{name}.overlay.md`, diff its sections against the **newly refreshed** base
`{conventions}/{name}.md`; where the base now covers an overlay addition (the addition was
upstreamed into stock this release), **prompt the user to retire that overlay section**
(human-gated, never auto-delete — the overlay is the vault's). Record `overlay-subsumption` in
`migrations_run` (`:89` enum — add it beside `overlay-lift`) and in the ledger's Migrations
line (`:111`).

- This is the missing half of the local-prototype→upstream rail: `overlay-lift` (`:69`)
  lifts local base-edits *into* an overlay; **subsumption retires** an overlay once its
  content has gone the rest of the way (overlay → upstream → base). 091006 is the first real
  round trip of that rail (its `review_after` overlay is exactly what build-16 upstreamed
  into `frontmatter@3`), so the pass has a live first customer on the 0.6.0 upgrade.
- **Coupling honored:** build-16's Migration note (`build-16-…:286`) says the then-subsumed
  overlay sections "are retired via **build-18's overlay-subsumption pass**." This F2 is that
  pass; without it in 0.6.0, vlt-core's `frontmatter.overlay.md` `review_after` section
  shadows the shipped base silently (lint's `overlay_not_append_only` at `vlt-lint/SKILL.md:77`
  only catches **verbatim** heading duplication, so a reworded shadow escapes — confirmed).
- **Note (not a fix here):** the pass is detect-and-prompt; the standing steady-state guard
  against reworded shadows is out of scope (it would be a fuzzy-match lint check — future).

## F3 — 091006 LB1: overlay-aware consumer activations

The rule, verbatim from the filing: every convention reader's On-Activation reads
`{conventions}/{name}.md` **together with `{overlays}/{name}.overlay.md` if present**, and
honors the overlay's appended rules. Two edits per skill — add `overlays` to the logical-name
path list, then reword the read instruction. `overlays` resolves to `_agent/conventions/`
(the value vlt-lint `:17` and vlt-upgrade `:25` already use).

- **`vlt-ingest/SKILL.md`**: path list `:22` (add `overlays` → `_agent/conventions/`);
  read instruction `:26` ("Read the conventions you will obey … `{conventions}/frontmatter.md`
  and `{conventions}/wiki-supersession.md`") → "…read each together with its
  `{overlays}/{name}.overlay.md` if present."
- **`vlt-extract/SKILL.md`**: path list `:19`; read instruction `:21`
  (`{conventions}/extraction.md` + `wiki-supersession.md`) → same rewording.
- **`vlt-research/SKILL.md`** *(grounding correction — now in scope)*: path list `:17` (no
  `overlays` today); its convention reads (`write-verification.md` at `:83`, and the
  `frontmatter.md` field references it now pins via `depends_on: ["frontmatter@3", …]` at
  `:3`) → pair the overlay. Build-16 made research a frontmatter consumer, so it is exactly
  the overlay-blind shape LB1 describes; the roadmap's "non-consumer today" note is stale.
- **`vlt-track/SKILL.md`** *(grounding addition beyond the filing's ingest+extract)*: the
  JIT-read block ("Before writing anything, JIT-read the governance conventions … from
  `{conventions}`: at minimum `frontmatter.md` … and `extraction.md`", ~`:45`) reads
  conventions without pairing overlays — same blindness. Add `overlays` to its path list and
  pair the read. (Track is a convention *reader*, not a handshake consumer — no `depends_on`
  change; the fix is purely the activation read.)
- **`vlt-lint/SKILL.md`** *(partial blindness — its fix-application reads)*: the tail of `:17`
  ("Before applying any fix, JIT-read `{conventions}/frontmatter.md`, `wiki-supersession.md`,
  and `wiki-index.md`") pairs no overlay, though lint *does* resolve overlays for its
  governance checks (`:76`, `:77`). Pair the overlay on those fix-application reads so a fix
  honors a locally-overlaid rule. (Lint already lists `overlays` `:17` — read reword only.)

**Single-home check:** the overlay-read *rule* is stated once in each activation (a local
instruction, not a shared convention) — there is no central "how to read conventions" doc to
point at, so per-skill statement is correct here. The wording is identical across the five so
a grep confirms uniformity (Verify).

## F4 — 091001 LB1 + LB3: the relocation-migration discipline (standing rule)

`vlt-upgrade/SKILL.md` Step 3 item 5 (*Migrations*, `:67`). Add a **standing preamble**
before the per-migration items — every relocation (file-move) migration MUST:

- **(LB1) Never touch parallel-worktree copies; stub the old path.** The vault runs parallel
  sessions in git worktrees — a `git mv` in one leaves stale copies at the old path in every
  other live worktree, which a parallel session can silently keep writing to. So a move
  leaves a **one-line pointer stub at the old path** (append-only records stay untouched) and
  touches only the main tree.
- **(LB3) Re-point open dispatch pointers at move time.** `vlt-dispatch` relay dedups on
  `(handoff-doc-path, recipient-slug)` (`vlt-dispatch/SKILL.md:166-174`); moving a doc resets
  the key, so an un-drained **open** pointer at the old path and a fresh relay at the new path
  can coexist. Any move migration re-points open pointers from the old path to the new one.

Then build-15's **proto-spec-retrofit** item (`:71`, the migration that added the
`stub + re-point` mechanics inline) is trimmed to **cite this preamble** rather than restate
it (single-home). The generalized rule now governs the decision-log-relocation and overlay-lift
migrations too, and any future one.

## F5 — 091001 LB2: the worked-example placeholder rule (CLAUDE.md)

`CLAUDE.md` Git & publishing section (the scrub rule at `:67-73`). Sharpen the existing
"Shipped content … must carry no personal or vault-local information" bullet with an explicit
standing rule:

> **Worked examples in shipped skills use placeholder paths**
> (`_agent/specs/{date}-{owner}-to-{consumer}-{slug}.md` style), never a specific install's
> artifact paths — a vault-side file move otherwise strands the module's own documentation
> (091001 LB2; build-15 fixed the `vlt-dispatch:193` instance). Generic *domain* illustrations
> (e.g. the dog-training / health-coaching loop-profile examples) are fine; the rule targets
> live artifact **paths**, not example vocabulary.

No shipped-skill edit here (the one live instance was fixed in build-15; the surface is clean
— Verify). Per disposition 5, `vlt-track/SKILL.md`'s domain slugs are explicitly in-bounds.

## F6 — 091006 LB3: the handshake's overlay axis (stated property)

`vlt-lint/SKILL.md` — the *Overlay append-only* check (`:77`). Add one clause stating the
property so it is documented intent, not accident:

> `depends_on` pins are flat base-only `name@version` scalars (validated as such by the
> coherence check `:74`); overlays are **deliberately unversioned** vault-local additions and
> carry no handshake axis — an overlay addition is invisible to the version handshake by
> design (it is a local extension, not a consumer-facing rule change).

No behavior change; documents why the coherence check reads bases only.

## Registration

**None.** No new skill, no `module-help.csv` row, no new workflow. F1's manifest and F2's
migration are internal to setup/upgrade; F3–F6 are edits to existing skills and CLAUDE.md.
No convention version bump ⇒ no consumer-walk, no re-ack (disposition 7).

## Out of scope (dispositioned)

- **Lint-time skill-asset divergence check** — F1 note: upgrade-time half only closes LB2;
  a lint mirror is new jurisdiction, future.
- **Steady-state reworded-overlay-shadow lint check** — F2 note: the subsumption pass is
  upgrade-time detect-and-prompt; a fuzzy-match lint guard is future.
- **091003 enforcement kit / tripwires** — build-17, trails 0.6.0 (roadmap ruling).
- **Family-invariant / operating-contract bells, family write-op invariant, `frontmatter@4`
  v2 keys** — parked per build-16 decisions 4/10/13.
- **Genericizing `vlt-track` domain slugs** — dispositioned KEEP (disposition 5).

## Verification (unit, at rest — lifecycle step 5)

- **No version drift:** grep every `{conventions}/*.md` `version:` and every skill
  `depends_on:` → unchanged from build-16 (frontmatter@3 × 5, write-verification@1 × 4,
  spec@1 × 2, wiki-*/extraction unchanged); no convention bumped, no ack moved. (Confirms
  disposition 7 — this build is durability-only.)
- **F1 manifest:** dry-run `vlt-setup`'s manifest step against a temp fixture skill tree →
  a `path\tsha256` line per shipped file, `vlt-agent-*` and agent-zone excluded; edit one
  file, re-run the Step-1 detect logic by hand → exactly that file flags
  `skill_asset_divergence`, its prior content captured; delete the manifest → `skill_manifest_missing`
  + best-effort reseed (mirrors `baseline_missing`). All three report keys thread through
  post-flight + ledger + Verify checklist (grep the four sites).
- **F2 subsumption:** construct a temp overlay whose section the (refreshed) base now covers →
  the pass prompts to retire it and records `overlay-subsumption`; a still-additive overlay →
  left intact (no false retire). `overlay-subsumption` present in the `migrations_run` enum
  (`:89`) and ledger line.
- **F3 overlay-aware reads:** grep the five skills for the overlay-pairing clause → present
  and uniform in ingest/extract/research/track/lint; each skill's path list resolves
  `overlays`. Place a temp `frontmatter.overlay.md` in a fixture and confirm each activation's
  instruction would read it (by inspection of the reworded text).
- **F4 relocation discipline:** the preamble states worktree-safety + open-pointer re-pointing
  once in Step 3 item 5; build-15's proto-spec-retrofit now cites it (grep: the stub/re-point
  mechanics text appears once, in the preamble, not restated in the item).
- **F5 placeholder rule:** `grep -rEn "_agent/(handoffs|specs)/20[0-9]{2}-[0-9]{2}-[0-9]{2}"
  skills/vlt-*` (shipped surface only, excluding `skills/reports/`) → **zero** (build-15's
  instance holds); the CLAUDE.md rule reads as specified.
- **F6 property:** the overlay-axis sentence appears once, at `vlt-lint/SKILL.md:77`.
- **Packaging:** `uv run tools/package-lint.py --expect-version 0.6.0` → exit 0 (this is the
  0.6.0 release build — the version bump lands with it; see Release).
- **Scrub:** no vlt-core-private content in any changed shipped file (the only slugs are the
  dispositioned generic domain illustrations in `vlt-track`, untouched).

## Release (build-18 is the last 0.6.0 build — the tag gate lives here)

Per CLAUDE.md lifecycle step 6: at the 0.6.0 release, bump **both** version strings —
`.claude-plugin/marketplace.json` `plugins[0].version` (`:16`) and
`skills/vlt-setup/assets/module.yaml` `module_version` (`:4`) — from `0.5.0` to `0.6.0`. Then
run `uv run tools/package-lint.py --expect-version 0.6.0`; **tag only on exit 0**, and record
its PASS summary line in the release commit message. ff-merge `arc3-v0.6.0` → `main`, tag
`v0.6.0`, push main + tag. (0.6.0 = builds 14+15+16+18; build-17 trails.)

## Acceptance (live — appended to the Arc 3 roadmap ledger)

- **0.6.0 upgrade on vlt-core — the coupling pays off:** vlt-core's `frontmatter.overlay.md`
  `review_after` section, once the base refresh delivers `frontmatter@3` covering it, is
  offered for retirement by F2's subsumption pass (`overlay-subsumption` in `migrations_run`);
  on accept, the shadow is gone and lint shows no residual overlay finding.
- **Skill-asset net protects the template edits (F1):** after the 0.6.0 upgrade seeds the
  `.skill-manifest`, a subsequent vlt-core local edit to an installed `vlt-mint/assets/*.md`
  template survives the *next* upgrade as a surfaced `skill_asset_divergence` (prior content
  in the ledger), not a silent clobber. (The 0.6.0 run itself seeds the manifest best-effort —
  `skill_manifest_missing` reported once, then clean.)
- **Overlay-aware reads (F3):** vlt-core's first write op run after upgrade that touches an
  overlaid convention honors the overlay's appended rule (e.g. a `review_after` overlay rule,
  if vlt-core kept one pre-subsumption) — verified by the write conforming without a manual
  reminder.
- **Relocation discipline (F4):** the next move migration on any install (or vlt-core's
  proto-spec retrofit if it runs via the offer) leaves a stub, touches no worktree copy, and
  re-points open pointers — days-to-stale-pointer = 0.
- **Placeholder rule (F5):** standing — no future shipped worked example couples to a live
  artifact path (the 0.6.0 shipped surface is the clean baseline).
