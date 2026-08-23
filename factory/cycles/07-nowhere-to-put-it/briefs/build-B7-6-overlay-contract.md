---
title: 'Build #B7-6 — the overlay contract (workflow assets become first-class handshake nodes, the fan-out honors merged-on-read, and the wiki sources: wikilink form ships with its normalization clause)'
status: 'BUILT 2026-08-15 — all nine F-sites landed as briefed. F1: frontmatter 6→7, consumers: gains vlt-lint-full.js, rule 4''s interim trailer replaced by the form + normalization clause + coexistence posture, wiki schema sources: [] gains the rule-4 pointer comment; nothing else in the base touched. F2: all six skill consumers re-acked @7 (vlt-ingest/vlt-lint real edits; vlt-extract/vlt-research/vlt-mint/vlt-dispatch verified "no edit needed here" — none encodes the wiki sources: form); checks.md:36 rewritten to the node model (references stay by-declaration), legs 1+3 gain the applied rule-4 normalization by pointer; vlt-mint:144 walk-step-3 sentence rewritten to the node model. F3: vlt-lint-full.js header ack line (frontmatter@7, wiki-supersession@2, wiki-index@2), optional overlaysPath/overlayNames parsed on the same JSON-string intake, loud coverage_caps degrade when absent, convRead() merged-read wording in scanner + index prompts mirroring vlt-lint SKILL:17, Gap-B normalization instruction added; pair pass and B5-3 seam untouched. F4: full-scale.md step 1 globs {overlays}/*.overlay.md, step 2 passes overlaysPath+overlayNames, resume warning grows by two. F5: vlt-consult.js + vlt-review-council.js carry explicit // depends_on: [] headers + the merged-on-read sentence beside their prompt builders; no behavior change. F6: _e5_asset_nodes in package-lint.py (presence: exactly one parseable header per workflow file; bipartite both directions, E1 vocabulary), E1 skips .js entries via shared predicate _is_asset_node, docstrings state it in both homes; harness fixture gains vlt-fixture.js + testconv asset consumer, case 21 (covers _e5_asset_nodes, asserts stale-asset red AND E1 silent on the .js entry), CASE_FLOOR 20→21. F7: carve-out bullet added after the merged-on-read bullet (placeholder worked example); rule-card derived_from re-derived to sha256:ef0210cb…; digest prose judged not to need the bullet (ceremony-layer summary — sha-only re-derive, as the brief expected), card 5,541 bytes < 8,000 budget. F8: vlt-ingest wiki template sources: placeholder shows rule 4''s form, comment-style, rule text single-homed. F9: loss-shape fixture reproduction executed against the shipped workflow at this build''s HEAD. Deviations: (1) F9 ran via a node harness supplying the runtime seam (args delivered as a JSON string exactly as the runtime does; deterministic mock at the agent() LLM boundary that actually reads the fixture files — clustering, seeded pass, provenance merge, intake, and report assembly all the real shipped JS), the Workflow-tool route being unavailable to this builder session — sanctioned by the task contract. No other deviations. Verification: (a) R2 red-then-green observed binding: with _e5_asset_nodes defined and no covering case, package-lint FAILED E ("harness coverage: _e5_asset_nodes has no fixture case"); after case 21 + fixture + floor bump, uv run tools/test-package-lint.py → 21/21 green; in-process probe: a workflow stripped of its header fails E5 loudly ("carries 0 … header lines"); case 21 proves stale-asset-ack red + E1 silence. (b) C6 could-have-failed: pre-re-derive run FAILED C ("rule-card stale: c32b5cb8… != ef0210cb…"); post re-derive C PASS. (c) uv run tools/package-lint.py → A/B/C/E PASS; --expect-version 0.9.1 → exit 0 "A/B/C/E PASS, D PASS — vlt 0.9.1" (Group E the bipartite check of record at @7, asset nodes included); zero frontmatter@6 in the shipped tree (hits only in gitignored reports). (d) ACCEPTANCE CHECK 3 EVIDENCE (A4-4 (5), gates the arc) — positive run (fixture: 5 placeholder pages, hub-alpha consumes beta-topic + gamma-topic into the only cluster before alpha-notes — which links beta-topic and carries a name-verification callout questioning "Morgan Reeve" against it — can cluster): the recorded cluster call covers hub/beta/gamma ONLY (the directly-linked pair alpha-notes+beta-topic demonstrably split; the cluster pass returned zero collisions, so without the seeded pass the run yields no finding — the pre-B5-2 loss shape genuinely reproduces), yet entity_collisions returned ["alpha-notes vs beta-topic: Morgan Reeve — Crest Laboratory vs Harbor Institute (callout-seeded)"] with entity_scan_facts.seeded_pairs_checked = 1, seeded_pairs_total = 1. Negative run (same fixture minus the callout): seeded_pairs_total 0, seeded_pairs_checked 0, no (callout-seeded) entry, output contract intact. Run executed AFTER the F3 overlay edits with overlaysPath/overlayNames passed — also proving the edits did not regress the pass. (e) check-2 with/without pair: WITH overlay args the overlay-compliant page delta-local (accent_note:, allowed only by the overlay occupying the base''s named carve-out) drew NO finding and coverage_caps was empty; WITHOUT overlay args delta-local flagged in malformed_frontmatter ("unknown key(s) per frontmatter.md: accent_note") AND coverage_caps carried "no overlay args passed — pages were judged against base conventions only…". (f) check-4 desk-check: "[[_agent/research/2026-08-05-note]]" (quoted wikilink wiki entry) and _agent/research/2026-08-05-note.md (bare-path research twin) normalize equal under rule 4''s stated steps. (g) cross-file greps: depends_on header present in all three shipped workflows; no shipped file still asserts "covers its own workflow assets"; merged-read wording aligned across SKILL:17 / scanner prompt / index prompt / contract:100; all three .js files syntax-check as the runtime-shaped async function. (h) scrub: changed shipped files + fixture carry zero personal/vault-local content; fixture uses placeholder names/paths only. No .decision-log.md on disk. Carrier filing 160949 stays active until arc closeout archives it per Stage 5 (check 3 evidence recorded here).'
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-14-154422-lint-full-fan-out-is-blind-to-convention-overlays.md (A7-7 — the three-file overlay-blind class + the governance half: acks that cover assets by declaration drift silently)'
  - 'inbox/2026-08-14-154424-wiki-sources-should-ship-as-wikilinks.md (A7-9 — the sources: FORM half only; rule 4''s traverse-vs-verify split is B7-3''s, shipped)'
  - 'inbox/2026-08-14-154425-ingest-wiki-template-placeholder-teaches-a-form.md (A7-10 — the template placeholder, riding A7-9 per its binding contingency)'
  - 'inbox/2026-07-25-160949-auto-caption-name-substitution.md (CARRIER of the inherited A4-4 clause (5) FAILED debt — attached to this build AS ITS OWN SCOPE ITEM by the 2026-08-15 evidence-debt ruling; stays in the active inbox until this build''s ship-verifiable check for it passes)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-15): grouping (B7-6 = A7-7 + A7-9 form + A7-10, mechanism build, after B7-3); pre-ideation 4 (workflow assets become first-class handshake nodes; the brief owns the mechanical form; wire the check into package-lint.py); cross-filing class ruling (all three workflows receive the merged-on-read contract; a workflow with no convention read satisfies it at the point it would read one — the ruling forbids a blind read, it does not mandate a read); evidence-debt ruling (A4-4 (5) attaches here as its own scope item). §Post-ideation amendments: A1/A6 (post-ship base-rule need = frontmatter 6→7 bump + full six-consumer walk + bipartite verification — the only legal reopen), A2 (decline latitude = sources: form + A7-10 template ONLY; rule 4''s split is untouchable), A3 (the A4-4 (5) check must be tagged ship-verifiable and gates the arc), R2 (gate-check change extends the fixture same build).'
risk: 'moderate — reopens frontmatter via the A1/A6-sanctioned 6→7 bump (full six-consumer walk + bipartite verification), adds a release-gate check (R2 fires: fixture case + CASE_FLOOR bump), and touches the operating contract (C6 rule-card sha re-derive)'
---

# Build #B7-6 — the overlay contract

Goal: close the three-file overlay-blind class (A7-7) by giving every shipped workflow asset
the merged-on-read contract and making all three **first-class nodes in the version-handshake
graph** — so an asset's staleness is a *missing ack*, a checkable state, instead of a silence
behind a consumer's declaration. In the same build, ship the wikilink `sources:` **form** for
wiki pages (A7-9's form half — the rule half, rule 4's traverse-vs-verify split, shipped in
B7-3 @6 with an interim posture pointing at exactly this build) together with the
**normalization clause** that protects `linkage_ripe`'s shared-source leg, plus A7-10's
template fix so `vlt-ingest` teaches the form it binds. The severable **carve-out rule** lands
in the operating contract's overlay section regardless. And this build carries the inherited
**A4-4 clause (5) Jackson-pair debt as its own scope item** (fourth arc; amendment A3: its
acceptance check is ship-verifiable and gates the arc).

All rejected alternatives in the parent filings are settled — do not re-litigate. In
particular: the class ruling (all three workflows, not just where the break was observed), the
handshake-node ruling (the by-inspection alternative was rejected as an unverifiable prose
promise), and the skill-overlay veto (no local skill patching anywhere in this arc) are the
owner's, cited here, closed.

## Brief-time dispositions

Headless run — each judgment call below is recorded at the point it applies, per the
`build-brief` headless contract.

1. **A7-9's two closes: close (1) — the normalization clause, wiki schema only. Close (2) is
   REJECTED as forbidden, not merely disfavored.** The roadmap left "the two closes carried
   unranked: *(1)* a normalization clause … or *(2)* convert both schemas together" to this
   brief. Close (2) would put research-note `sources:` on wikilink form — but rule 4 as
   shipped by B7-3 (`frontmatter.md:36`) classes a research note's `sources:` as a
   *verify-against* audit trail holding bare paths. Converting it would contradict rule 4's
   split, which amendment A2 forbids this build to do ("it may not decline, narrow, or
   contradict rule 4's traverse-vs-verify split"). So the shipped rule text itself decides the
   ranking: **the wiki-page schema converts; the research schema stays bare-path; the
   normalization clause makes the two forms comparable forever** — which is also the close
   that keeps `linkage_ripe` safe against any future divergence, per the filing's own note
   that close (2) "still wants the clause as a defence."
2. **The form ships — no decline, so no R1 pair-posture is owed.** A2 gave this brief decline
   latitude over the form and the template; it is not exercised. The @6 interim posture
   ("the wikilink form … ships with the overlay-contract build") is discharged, not extended.
3. **Shipping the form is a base rule change after the opener shipped — this build takes the
   A1/A6 reopen deliberately: a coordinated `frontmatter` 6→7 bump with a full six-consumer
   walk and bipartite verification.** The form details (quoting, path shape, reserved
   characters, the normalization clause) change what a vault must write; that is a rule
   change, and acks at @6 cover text that did not carry it. A1/A6 names exactly one legal
   post-ship path and prices it as a full walk precisely so briefs don't reach for it
   casually; this brief reaches for it because B7-3's own shipped rule text *pre-announces*
   this edit — the demonstration A1 requires is already on record in `frontmatter.md:36`.
   Editing the base without the bump would be the ack-covers-text-it-never-saw drift this
   very build exists to prosecute.
4. **The handshake-node mechanical form (ruling 4 gave this brief ownership): asset acks live
   in a machine-parseable `depends_on` header line in each `.js`; asset consumers are named
   in the convention's existing `consumers:` list by filename; a new gate check `_e5` owns
   the asset leg of the bipartite comparison.** One graph, one vocabulary: a convention's
   `consumers:` entry ending `.js` resolves against `skills/vlt-setup/assets/workflows/`,
   and its ack is the flat `"name@version"` pin in that file's header comment — the same
   shape as a skill's frontmatter ack, so staleness reads identically ("stale — X acks
   frontmatter@6 but convention is @7"). The rejected sub-option (an asset list on the
   consumer skill's frontmatter) re-creates by-declaration coverage one level down — the
   skill would again vouch for a file nothing re-reads.
5. **`vlt-consult.js` and `vlt-review-council.js` become named nodes with explicit empty
   acks.** Both read zero conventions today (re-grounded: `grep -c overlay` and any
   conventions-path read = 0 in both). Per the class ruling's brief-time latitude, they
   satisfy the contract by carrying (a) a `depends_on: []` header line — the checkable
   "reads no conventions" state, which E5 requires present on every workflow file so a
   future convention read cannot arrive unacked and structurally unnoticed — and (b) the
   merged-on-read requirement stated at the point a convention read would enter. No
   convention read is added; the ruling forbids a blind read, it does not mandate a read.
6. **The A4-4 (5) debt's clause IS statable ship-verifiably — restated as the mechanism
   property, discharged at rest against the real shipped workflow.** What three arcs of
   field-contingent framing measured was a named vlt-core instance ("the Jackson pair
   surfaces on the first full lint"); what the debt actually claims is the mechanism
   property underneath it: *a pair the vault has explicitly marked suspicious is never lost
   to greedy cluster splitting*. That property is reproducible at rest: run the shipped
   `vlt-lint-full.js` (via the Workflow tool, real end-to-end code) against a temp fixture
   engineered into the exact loss shape, and assert the pair surfaces `(callout-seeded)` —
   a check that fails on pre-B5-2 code by construction and fails again if this build's
   overlay changes regress the pass. So per amendment A3 the escalation branch is not
   taken; the ship-verifiable check is F9/acceptance check 3, it gates the arc, and the
   named vlt-core instance demotes to an explicitly **non-gating** field observation
   (acceptance check 6, watch register). A3's optional move to B7-7 is declined: the tag is
   the load-bearing half by A3's own text, the fixture run rides machinery this build is
   already inside, and a headless run does not exercise owner-optional insurance.
7. **A7-10's generalizable rule is applied at its one shipped instance and recorded here,
   not minted as a convention rule.** *Where a template's field has a form the convention
   constrains, the template should show the form.* The only shipped template with a
   form-constrained field hidden behind a neutral placeholder is `vlt-ingest`'s wiki
   template (`SKILL.md:147-148`); F8 fixes it. Minting the sentence into a convention would
   create a rule with no checker (the Strand-3 shape) for a class of one; if a second
   instance arrives, that filing carries this paragraph as its precedent.
8. **`checks.md:36` and `vlt-mint/SKILL.md:144` — the two shipped homes of "a consumer's ack
   covers its own workflow assets" — are rewritten to the node model in this build**, as
   consumer edits riding the @7 walk. Leaving either standing would ship prose asserting
   the exact model this build retires. **Reference files stay by-declaration** (ruling 4's
   scope is the three workflow assets; `references/*.md` are read as part of the skill's own
   text, which is what the skill's ack attests) — the B5-8 "and reference files" clause
   survives with its meaning narrowed to references only.

## F-sites

All sites re-grounded 2026-08-15 against the working tree at HEAD of `arc7-v0.10.0`
(`7b1bc6c` + B7-5 ledger edits; B7-1/B7-2/B7-3/B7-5 shipped). Every capture-cited line HOLDS
(A7-7's `:22`/`:62`/`:77-78`/`:95`/`:142`-area sites; `checks.md:59`; contract `:100`;
`vlt-ingest:26`/`:147`; `vlt-mint:144`). Rule 4 at `frontmatter.md:36` carries B7-3's split +
interim posture as B7-3's brief specified — the planned state, not drift. Zero grounding
corrections; no roadmap superseding note owed.

### F1 — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md` (the base, 6→7: the A1/A6 reopen)

- **Current:** `:4` `last_updated: 2026-08-15`; `:11` `version: 6`; `:12`
  `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch]`;
  `:36` rule 4 ending in the R1 interim-posture trailer ("*Interim posture:* the wikilink
  **form** for wiki `sources:` … ships with the overlay-contract build; **until it does, wiki
  pages stay on the bare-path form** …"); `:98` the wiki schema's `sources: []` with the
  accretion note at `:104`.
- **Change (one coherent edit, four clusters):**
  1. `version: 7`; `last_updated:` to build date; `consumers:` gains **`vlt-lint-full.js`**
     (the asset node — disposition 4). No skill consumer is added or removed.
  2. **Rule 4's interim-posture trailer is replaced by the form itself** (the split sentence
     and the carve-out tail are untouched — A2). The form, each detail grounded in A7-9's
     capture: a wiki page's `sources:` entry that references a **vault note** is a
     **double-quoted wikilink** (rule 1) carrying the **full vault-relative path, no `.md`**
     — full path because basenames collide across zones; no `.md` per rule 1's own example
     (`superseded_by: "[[page-slug]]"`). Entries that are **external URLs are not page
     references and stay plain strings**. **Reserved characters, stated positively**: `[`,
     `]`, `#`, `^`, `|` are reserved inside a wikilink target; **`?` is not** — a target
     containing it keeps it (the field-earned dead-link lesson). Then the **normalization
     clause**: *any consumer comparing `sources:` entries — across pages, across zones, or
     against a prose `## Sources` section — normalizes both sides first: strip surrounding
     quotes and `[[ ]]`, strip a trailing `.md`, and compare on the vault-relative path
     (tolerating a bare-basename legacy entry by basename match)* — so the wikilink and
     bare-path forms compare equal forever. Close with the **coexistence posture**: existing
     bare-path entries stay legal, there is **no backfill sweep**; a page adopts the form on
     its next substantive edit — the normalization clause is what makes the mixed state
     permanently safe.
  3. The wiki schema at `:98`: `sources: []` gains a trailing comment pointing at rule 4's
     form (`# vault notes as "[[path]]" wikilinks, URLs plain — YAML rule 4`), placeholder
     style only — the rule text is single-homed in rule 4.
  4. Nothing else in the base changes. The deferral block (`:15-17`), the address rule, the
     vault-writable and local-convention rules, and every schema other than the wiki
     `sources:` comment are out of this build's reach.
- **Why:** dispositions 1–3; A2 (ship-the-form path); A1/A6 (the sanctioned reopen).

### F2 — the six-consumer walk to @7 + bipartite verification

- **Current:** all six consumers ack `frontmatter@6` (`vlt-ingest/SKILL.md:4`,
  `vlt-lint/SKILL.md:4`, and siblings).
- **Change:** bump every listed skill consumer's `depends_on` entry to `frontmatter@7`,
  reconciling each against the one rule change (the `sources:` form). Reconciliation
  outcomes expected: **vlt-ingest** — real edit (F8, the template); **vlt-lint** — real
  edits (F4 overlay plumbing hand-off, plus `references/checks.md` — see below);
  **vlt-extract, vlt-research, vlt-mint, vlt-dispatch** — expected "no edit needed here"
  re-acks (none encodes the wiki `sources:` form; the builder verifies per skill rather than
  assuming). The asset node `vlt-lint-full.js` acks @7 via its header line (F3). Two
  consumer text edits ride the walk beyond the ack bumps:
  - `vlt-lint/references/checks.md:36` (convention coherence) — rewrite the "A consumer's
    ack covers its own workflow assets and reference files" clause to the node model
    (disposition 8): a workflow asset that reads conventions is a **listed consumer in its
    own right**, acking via the `depends_on` header line in the installed
    `.claude/workflows/*.js`; the vault-side check walks those acks with the same
    stale/unacknowledged/dangling vocabulary; reference files remain covered by the skill's
    own ack.
  - `vlt-lint/references/checks.md:57` and `:59` (`linkage_ripe` legs 1 and 3) — add the
    applied normalization instruction: both legs compare `sources:` entries **after** rule
    4's normalization (pointer to `frontmatter.md` rule 4 — mechanics stated once there),
    so a wikilinked wiki entry still matches a bare-path research entry. This is the edit
    that discharges A7-9's design constraint ("the leg silently stops firing … a blind spot
    in an absorption test is a false positive", `checks.md:57`).
  - `vlt-mint/SKILL.md:144` — rewrite the trailing sentence of walk step 3 to the node
    model (disposition 8): assets that read conventions appear in `consumers:` by filename
    and are walked like any consumer — their ack is the header pin, bumped on
    reconciliation.
- **Why:** the coordinated-bump ruling as amended by A1/A6; ruling 4's visibility half.
- **Verification of record:** `package-lint` Group E (never a hand-written `grep "name@"`).

### F3 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (the merged-on-read contract + the asset ack)

- **Current:** overlay-blind end to end (`grep -c overlay` → 0). `conventionsPath` doc `:22`,
  intake `:62`, required-args guard `:77-78` names `pages`/`indexPath`/`conventionsPath`
  only; the per-page scanner prompt `:141-143` instructs reading
  `${conventionsPath}/frontmatter.md`, `wiki-supersession.md`, `wiki-index.md` bare; the
  scanner judges `frontmatter_valid` "per frontmatter.md" (`:95`); the Gap-B
  `sources:`-vs-prose divergence judgment sits in the same prompt; the index pass `:231-235`
  reads `${conventionsPath}/wiki-index.md` bare. This breaks
  `vault-operating-contract.md:100` (*"the convention is the base file plus its overlay,
  merged on read"*) — an overlay-compliant page lands as a real `frontmatter_valid: false`
  finding (A7-7's biting failure mode).
- **Change:**
  1. **Header ack line** (machine-parseable, near the top with `meta`):
     `// depends_on: ["frontmatter@7", "wiki-supersession@2", "wiki-index@2"]` — the three
     conventions this workflow's prompts instruct agents to read. Exact token format is E5's
     to parse (F6); keep it a single line, flat pins, same vocabulary as skill acks.
  2. **New optional args** `overlaysPath: string` and `overlayNames: [string]` (the overlay
     files that actually exist — the SKILL has filesystem access, the script has none; same
     division as `crossLayerSlugs`/`stubSlugs`). Document in the args block, parse at intake
     beside `:62` (defaults: empty). **Not added to the `:77` required guard** — instead,
     when the caller passes no `overlaysPath`, push a `coverage_caps` message (*"no overlay
     args passed — pages were judged against base conventions only; overlay-compliant
     content may be falsely flagged"*): the honest-surface pattern, never a silent base-only
     judgment, and old callers degrade loudly rather than break.
  3. **Scanner prompt** (`:141-143`): for each of the three conventions, instruct reading
     the base **together with its overlay when that overlay is in `overlayNames`** (pass the
     resolved `${overlaysPath}/<name>.overlay.md` path inline), honoring the overlay's
     appended rules — the convention is base plus overlay, merged on read; judge
     `frontmatter_valid` and the Gap-B divergence against the **merged** rules. Mirror the
     wording of `vlt-lint/SKILL.md:17`'s own merged read so the two homes read alike. Also
     add the Gap-B normalization instruction: compare `sources:` entries per rule 4's
     normalization (both forms compare equal).
  4. **Index pass prompt** (`:231-235`): same merged read for `wiki-index.md` + its overlay.
- **Args intake note (standing rule):** the runtime delivers `args` as a JSON string — the
  existing parse-on-intake at `:48-49` stays; new args ride the same parsed object.
- **Why:** A7-7 as ruled (the class ruling); ruling 4's ack half.
- **Out of scope at this site:** giving the workflow a `{research}` zone (named second-cut
  work, `full-scale.md:9`); any change to the B5-2 pair pass (`:276-328`) or B5-3
  normalization seam beyond the prompt edits above — F9 proves them preserved.

### F4 — `skills/vlt-lint/references/full-scale.md` (the invocation site passes the overlay set)

- **Current:** step 1 (`:7`) discovers pages/`crossLayerSlugs`/`stubSlugs`; step 2 (`:8`)
  invokes `workflow('vlt-lint-full', { pages, indexPath, conventionsPath, crossLayerSlugs,
  stubSlugs, today })` — no overlay information crosses the boundary, which is the exact
  point the SKILL's own overlay honesty (`SKILL.md:17`) stops.
- **Change:** step 1 additionally globs `{overlays}/*.overlay.md` and collects the basenames
  that exist; step 2 passes `overlaysPath` (the resolved live absolute `{overlays}` path) and
  `overlayNames` in the args object, and the on-resume re-pass sentence names them too
  (omitting args on resume nulls them — the existing warning's list grows by two).
- **Why:** the fan-out inherits the same contract the SKILL already honors inline; without
  this site the F3 plumbing is dead code.

### F5 — `vlt-consult.js` + `vlt-review-council.js` (named nodes, explicit empty acks)

- **Current:** neither reads a convention (re-grounded — zero conventions-path reads; consult
  reads partner SKILLs/identity/thread `:125-134`; council reads personas `:126-137`).
- **Change (each file):** a header line `// depends_on: []` — the explicit, checkable
  "reads no conventions" declaration E5 requires present (disposition 5) — plus one comment
  sentence at the point a convention read would enter (beside the prompt builders): any
  future convention read must be merged-on-read per `vault-operating-contract.md`
  (*Convention overlays*) and must add its pin to this header line. No behavior change.
- **Why:** the class ruling's exact latitude: the contract is satisfied "at the point it
  would read one"; the named-node state is what makes a later blind read impossible to add
  silently (E5 sees a new pin the moment it is written — or its absence when a read arrives
  without one, via review; the mechanical net is the presence-and-bipartite check, F6).

### F6 — `tools/package-lint.py` + `tools/test-package-lint.py` (the E5 asset-node gate; R2 fires)

- **Current:** Group E (`:751-785`) aggregates E1–E4; E1 (`:585-606`) derives
  `conventions[name] = (version, [consumers])` from the shipped conventions dir and acks
  from `skills/vlt-*/SKILL.md` `depends_on:`, and fails any `consumers:` entry not in
  `skill_dirs` as dangling — so an asset entry like `vlt-lint-full.js` would today FAIL E1.
  E4 (`:708-748`) inventories every `^check_|^_e\d+_` callable structurally and fails one
  with no fixture coverage. Harness: 20 cases, `CASE_FLOOR = 20`
  (`test-package-lint.py:218`), `COVERAGE` map at `:213`.
- **Change:**
  1. **New `_e5_asset_nodes(root)`**, aggregated by `check_group_e`. Structural on both
     sides, never an enumeration: **(a)** walk `skills/vlt-setup/assets/workflows/*.js` —
     every workflow file MUST carry exactly one `// depends_on: [...]` header line parsing
     as flat `"name@version"` pins (or `[]`); a missing/unparseable line FAILS (absence must
     be loud — the named-node state is the deliverable). **(b)** bipartite, both directions,
     E1's vocabulary: every `consumers:` entry ending `.js` must resolve to an existing
     workflow file whose header acks that convention at the current version
     (dangling / unacknowledged / stale); every non-empty pin in a workflow header must
     appear in that convention's `consumers:` (an asset consuming unlisted is the reverse
     drift).
  2. **E1** skips `consumers:` entries ending `.js` (E5 owns them) — one shared predicate,
     stated in both docstrings.
  3. **R2, mechanical:** extend the fixture so case 1's clean baseline carries a workflow
     asset node end-to-end (a minimal fixture `.js` with a `depends_on` header + the fixture
     convention listing it); add **case 21** covering `_e5_asset_nodes` (`covers=
     ("_e5_asset_nodes",)`) — a stale asset ack turns E red — with the case also asserting
     E1 stays silent on the `.js` entry (the E1-change probe); bump **`CASE_FLOOR` 20 → 21**.
     Record the E4 red-then-green mutation probe (E5 defined with no covering case → E4 red;
     with case 21 → green) in the build's verification — this is R2 observed binding in-arc,
     the instance B7-1's acceptance check (4) anticipated for this build (B7-2 discharged
     the first; this build honors it again).
- **Why:** ruling 4's "wire the check into package-lint.py so the release gate carries it";
  R2 as amended by A7 (the legal response is stated at the check: *add the fixture case, in
  the build that added the check* — case 21 is this build's own compliance with it).

### F7 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` (the carve-out rule) + the C6 sha re-derive

- **Current:** the *Convention overlays* block `:97-104`; the append-only bullet `:99`; the
  merged-on-read invariant `:100` with its parenthetical on consumer skills; the
  base-rule-change bullet `:102`. Rule 4's carve-out tail ("unless a specific schema says
  otherwise") is a delegation slot whose occupancy test is today derived, not stated —
  A7-9's separable finding.
- **Change:** add one bullet to the overlay block (after `:100`'s merged-on-read bullet, its
  natural neighbor): **an overlay may occupy a carve-out the base names in its own words** —
  legal where *(a)* the base itself names the delegation ("unless a specific schema says
  otherwise") and *(b)* the overlay names the exact schema it occupies and scopes narrowly
  to it; an overlay claiming a carve-out the base never cut is a base-rule change in
  disguise and routes per the next bullet (`:102`). Worked example in placeholder form only
  (no vault-local paths). **Then re-derive `vault-rule-card.md`**: recompute the shipped
  contract's SHA-256 into the card's `derived_from:` (package-lint C6, `:298-333`, binds
  this mechanically — B7-5's builder note honored); the builder judges whether the card's
  digest prose needs the new bullet (expected: no — the card summarizes the ceremony layer;
  sha-only re-derive) and stays under `RULE_CARD_BUDGET`.
- **Why:** the roadmap's B7-6 designation: "the carve-out rule is severable and lands in the
  contract regardless"; it is also the durability-model rule the F1 form quietly relies on
  (the wiki `sources:` reclassification itself rode rule 4's named carve-out).

### F8 — `skills/vlt-ingest/SKILL.md` (A7-10: the template shows the form)

- **Current:** `:26` binds ingest to the conventions with the merged overlay read (verified
  intact — no defect, per the filing's own self-correction); the wiki-page template's
  `sources:` block at `:147-148` emits the form-neutral placeholder
  `sources:\n  - <every source that has contributed>`.
- **Change:** the placeholder shows rule 4's form (disposition 7):

  ```yaml
  sources:                                     # accretes; form: frontmatter.md YAML rule 4
    - "[[<vault-relative-path-to-note>]]"      # vault notes: double-quoted wikilink, full path, no .md
    - <plain external URL>                     # external sources are not page links — plain strings
  ```

  Comment style, placeholder paths only; the rule text stays single-homed in rule 4 (the
  template *shows*, the convention *states*). `:26` is untouched. The re-ack to
  `frontmatter@7` rides F2.
- **Why:** A7-10's residual risk is an agent copying the placeholder's shape rather than
  resolving it — "a template inline in the skill is the most concrete thing in context at
  write time." Its binding contingency is satisfied: A7-9's form ships (disposition 2).

### F9 — the A4-4 clause (5) scope item (its own F-site, not a rider)

- **Current state of the debt:** the mechanism shipped in B5-2 and is intact at HEAD —
  `name_callout_targets` in PAGE_SCAN (`vlt-lint-full.js:107-110`), the callout-seeded pair
  pass (`:276-328`), `entity_scan_facts` (`:389-394`), `(callout-seeded)` provenance
  (`:328`) merged into `entity_collisions` (`:379`). What never happened, across four arcs,
  is a **discharge**: every check written for it was field-contingent, and arcs close on
  ship-verifiable checks only (amendment A3 names this the actual mechanism of loss).
- **The work:** execute, and record as evidence, the **loss-shape fixture reproduction**
  against the shipped workflow at this build's HEAD (i.e. *after* the F3 overlay edits — the
  run also proves those edits did not regress the pass):
  - Temp fixture wiki (scratchpad; placeholder content only — no NFL/vlt-core names, per the
    scrub rule and B5-2's precedent): ~5 pages engineered so greedy cluster consumption
    (`:239-253`) splits a directly-linked pair — a hub consumes page B into cluster 1 before
    page A (which links B and carries a name-verification callout questioning a proper noun
    against B) forms its own cluster. Include a minimal conventions dir + one overlay so the
    same run exercises F3's plumbing.
  - Run `vlt-lint-full.js` via the Workflow tool with the full args the SKILL would pass
    (including `overlaysPath`/`overlayNames`).
  - **Assert (positive):** the pair is NOT co-clustered (the pre-B5-2 loss shape genuinely
    reproduces — without the seeded pass this run yields no finding, which is what makes the
    check one that could fail), yet `entity_collisions` carries the pair with the
    `(callout-seeded)` marker and `entity_scan_facts.seeded_pairs_checked ≥ 1`.
  - **Assert (negative):** the same fixture minus the callout → `seeded_pairs_total: 0`,
    no `(callout-seeded)` entry, output contract otherwise intact.
  - If the reproduction FAILS, fixing it is **in this build's scope** (that is what "own
    scope item" purchases); the brief's acceptance check 3 stays red until it passes.
- **Why:** the evidence-debt ruling ("attaches to B7-6 as its own scope item … must give it
  its own acceptance check") + amendment A3 (the check is ship-verifiable and gates the
  arc). Disposition 6 records why this restatement is faithful to the debt's clause. The
  carrier filing `inbox/2026-07-25-160949-auto-caption-name-substitution.md` stays active
  until acceptance check 3 passes; on pass it archives per `arc-closeout` Stage 5.

## Registration

**No new skill, no new workflow, no `module-help.csv` change.** The registrations this build
makes are in the handshake surface: `frontmatter` 6→7 with the full six-consumer walk (F2 —
every listed consumer re-acked in the same build, bipartite verified by `package-lint`
Group E), `frontmatter.md` `consumers:` gains the asset node `vlt-lint-full.js`, and
`wiki-supersession.md:12` / `wiki-index.md:12` `consumers:` each gain `vlt-lint-full.js`
(no version bump on either — adding a consumer + its ack is not a rule change; both stay
@2 and the asset acks them at @2).

## Out of scope (dispositioned)

- **Rule 4's traverse-vs-verify split** — B7-3's, shipped, untouchable here (amendment A2).
  This build fills the form slot the shipped rule reserved; it does not restate or narrow
  the split.
- **Converting the research-note `sources:` schema (A7-9 close 2)** — rejected-because it
  would contradict rule 4's shipped classification (disposition 1).
- **A backfill sweep of existing wiki pages to the wikilink form** — rejected-because the
  normalization clause makes coexistence permanently safe; conversion happens on next
  substantive edit (F1's posture). No lint finding class is added for bare-path wiki
  `sources:` — a finding would demand a response the posture says isn't owed (R3's shape).
- **Adding convention reads to `vlt-consult.js` / `vlt-review-council.js`** — the class
  ruling forbids a blind read, it does not mandate a read; they become named empty nodes
  (F5, disposition 5).
- **Reference files (`references/*.md`) as handshake nodes** — outside ruling 4's scope;
  they remain covered by the skill's own ack (disposition 8).
- **A generic skill-overlay mechanism** — the standing veto holds; nothing here patches a
  skill locally. The `vlt-track` designed-parameter-read pattern is the sanctioned shape
  and is not needed by this build.
- **The `{research}` zone in the fan-out** — named second-cut work (`full-scale.md:9`),
  unchanged.
- **The vault-side `deferral_expired`/date surface, the address rule, the seam mechanisms**
  — B7-3 shipped the rules; B7-4/B7-5 own their mechanisms. The 6→7 walk re-acks without
  reopening any of them.
- **The candidate shapes in the A4-4 carrier filing's own body** (ingest-time proper-noun
  cross-check, grounding-sufficiency convention rule, caveat reframing) — already
  dispositioned by Arc 4/Arc 5 capture history; what this build owes the carrier is the
  debt's discharge check (F9), not new mechanism. A future filing may re-raise shape 1 on
  its own evidence.

## Verification (unit, at rest — lifecycle step 5)

- **Fixture run, positive + negative (F9)** — as specified in F9; the recorded transcript is
  the discharge evidence for acceptance check 3 and doubles as F3's end-to-end proof (the
  overlay-carrying run returns a clean `frontmatter_valid` for the overlay-compliant fixture
  page).
- **Overlay-contract probe (A7-7's acceptance case, at rest):** in the same fixture, one page
  compliant with an overlay rule that contradicts its base: run **with** overlay args → no
  finding on that page; run **without** overlay args → the page is flagged AND
  `coverage_caps` carries the no-overlay-args message. The with/without pair is the
  could-have-failed structure (gate-2: no vacuous discharge).
- **Handshake bipartite re-check:** `package-lint` Group E is the check of record — E1 six
  skill consumers at `frontmatter@7`, E5 asset nodes current, zero stray pins. **A
  hand-written `grep "frontmatter@" skills/` is not a substitute** (self-confirming; the
  brief-anatomy warning applies verbatim).
- **E5/R2 mechanics:** `uv run tools/test-package-lint.py` → 21/21 green, `CASE_FLOOR` 21;
  recorded mutation probes: (a) E5 defined without case 21 → E4 red (the R2 net observed
  binding — B7-1 check (4)'s instance for this build); (b) case 21's stale-asset-ack fixture
  turns E red; (c) a fixture workflow stripped of its `depends_on` header line fails E5
  loudly.
- **C6:** `package-lint` group C passes after the contract edit — the rule-card
  `derived_from:` sha re-derived (a deliberate pre-re-derive C failure observed and recorded
  is the could-have-failed probe; case 12 already covers the check class).
- **Mid-arc packaging lint:** `uv run tools/package-lint.py` groups **A/B/C/E** → PASS (C7
  boot-budget holds after the checks.md/SKILL text growth). D/`--expect-version` is the
  release gate, not this build's (B7-6 is not the release build; the version-string bumps
  ride the arc's release).
- **Cross-file agreement greps (editing aid, not the recorded verification):** the
  normalization clause stated normatively once (rule 4) and applied at all three comparison
  sites (checks.md legs 1/3, the Gap-B scanner prompt); the merged-read wording aligned
  across `vlt-lint/SKILL.md:17`, the scanner prompt, the index-pass prompt, and contract
  `:100`; `depends_on` header lines present in all three workflow files; no shipped file
  still asserts "a consumer's ack covers its own workflow assets."
- **Scrub:** grep every changed shipped file + the fixture for personal/vault-local content
  (`vlt-core`, `{owner}`, `/Users/`, the carrier's instance names) → zero hits; worked
  examples use placeholder paths.
- Delete any `.decision-log.md` before commit; **one commit for the build**. The builder
  rewrites `status:` to a BUILT record with numbered deliberate deviations
  (`BUILT <date> — …; …. Deviations/notes: (1) …`).

## Acceptance (live — appended to the roadmap ledger)

Six checks: five **ship-verifiable**, one **field-contingent** (explicitly non-gating).
Check 3 is the A4-4 (5) debt's check — ship-verifiable and **mandatory to the arc gate**
per amendment A3.

1. **[ship-verifiable]** `frontmatter@7` handshake closed, bipartite-consistent, **asset
   nodes included** — `package-lint` Group E passes at rest and inside the arc's pre-tag
   `--expect-version` run: six skill consumers acked @7, `vlt-lint-full.js` listed in
   `frontmatter`/`wiki-supersession`/`wiki-index` `consumers:` and acking via its header
   line, `vlt-consult.js` + `vlt-review-council.js` carrying explicit `depends_on: []`,
   zero stray pins; recorded probes show E5 able to fail (stale asset ack → red; stripped
   header → red) and E4 red-then-green on E5's introduction (R2 observed binding — the
   B7-1 check (4) instance for this build). Harness 21/21, `CASE_FLOOR` 21.
2. **[ship-verifiable]** the fan-out honors merged-on-read — the recorded with/without
   fixture pair: an overlay-compliant page contradicting its base survives a full sweep
   with **no finding** when overlay args are passed (A7-7's acceptance case, carried as
   filed), and the same page is flagged **with a `coverage_caps` no-overlay-args message**
   when they are not — dischargeable at rest from the build's recorded runs, re-confirmed
   at the release gate by the shipped file carrying the plumbing (`overlaysPath`,
   `overlayNames`, merged-read prompts).
3. **[ship-verifiable — GATES THE ARC (amendment A3)]** the inherited **A4-4 clause (5)**
   debt discharges at rest: the loss-shape fixture reproduction of record (F9) — greedy
   clustering demonstrably splits the callout-marked pair, yet the shipped
   `vlt-lint-full.js` at HEAD returns the pair in `entity_collisions` marked
   `(callout-seeded)` with `entity_scan_facts.seeded_pairs_checked ≥ 1`, negative run
   clean — a check that fails by construction on the pre-B5-2 shape and fails again if
   this build's overlay edits regress the pass. On pass, the carrier filing
   `inbox/2026-07-25-160949-auto-caption-name-substitution.md` becomes archivable per
   `arc-closeout` Stage 5 (after four arcs). If this check cannot be discharged, the arc
   does not close around it — that is the entire point of the tag.
4. **[ship-verifiable]** the `sources:` form shipped coherently — rule 4 carries the form +
   normalization clause + coexistence posture with the interim-posture trailer gone;
   `vlt-ingest`'s template shows the form (quoted wikilink, full path, no `.md`, URLs
   plain); `checks.md` legs 1/3 and the Gap-B scanner prompt each apply the normalization
   by pointer; readable at rest, and a desk-check of record shows a wikilink-form wiki
   entry and its bare-path research twin normalize equal (A7-9's acceptance case: an
   absorbed research note is still excluded from `linkage_ripe` when the citing wiki page
   is on the wikilink form and the note is on bare paths).
5. **[ship-verifiable — next ordinary upgrade, either vault]** delivery — the installed
   `.claude/workflows/` carries all three workflows with their `depends_on` header lines
   and the overlay plumbing; the installed `frontmatter.md` is @7 with the form; the
   installed `vlt-ingest`/`vlt-lint` texts carry the F2/F8 edits — checkable by grep on
   the installed vault; bounded, the upgrade happens anyway.
6. **[field-contingent — NON-GATING, watch register by design]** the named instance: on
   vlt-core's first **full** lint after its 0.10.0 upgrade, with the "Which Jackson?"
   callout still standing, the known pair surfaces `(callout-seeded)` in the live report.
   Producing vault: **vlt-core only** (owner-run; evidence arrives as the owner's pasted
   report). This is corroboration of check 3's property in the wild, deliberately **not**
   the debt's discharge — per disposition 6 and amendment A3, the debt discharges at
   check 3. If the callout is resolved before any full lint, the observation re-targets
   the next standing name callout and otherwise lapses without prejudice.
