---
title: 'Build #B10-11 — the wiki-move capstone (the wiki moves into human-browsable space and `resources/` retires as an extraction target — one operation at true cost)'
status: 'BUILT 2026-08-22 — all F-sites landed on arc10-v0.14.0 (one commit). Verification: package-lint A/B/C/E PASS (D skipped, rides the release), test-package-lint 22/22 green, node --check OK, census desk-check PASS against the real reduce code ({pages_total: 4, fresh: 2, stale: 1, unattested_pre_adoption: 1}, per-page attestation_stale slot unchanged), migration desk-walk accept + decline + idempotence OK on a scratchpad fixture, stale-token sweep clean (_agent/wiki survives only in the F10 migration bullet), rule card re-derived at 6,789 bytes with sha re-stamped. R4 audit re-run and recorded: no ask touched, no convRead change, PAGE_SCAN byte-untouched — the census is reduce-only arithmetic; the two vlt-lint-full.js:173 rule-4 markers verified still-true (this build touches the type: list, not YAML rule 4) and re-stamped @13. Deviations, numbered: (1) module.yaml module_greeting reworded ("shape a resource doc on…" → "shape a deliverable on…") — a shipped-surface recitation of the retired offering the F-sites did not list; grounding addition under the F6 vocabulary sweep. (2) Two further retired-vocabulary sites beyond the listed F5/F6 cites: vlt-extract Step 3 dropped its "a resource doc with clear explanation" shape clause, and vlt-agent-creative:27 first-meeting example reworded ("ripe for a resource doc" → "ripe for a deliverable") — same rule, same sweep. (3) vlt-setup:116 keeps its creation keyed on the resolved {wiki} with the new default in the parenthetical, phrased "keyed on the resolved {wiki}" rather than the brief''s exact wording — semantics identical. No other deviations; A10-10 untouched, write-verification.md:55 untouched, package-lint fixtures untouched (verified synthetic).'
module_code: 'vlt'
created: '2026-08-22'
derives_from:
  - 'inbox/2026-08-20-093000-para-write-path-single-door-wrong-shape.md (A9-1: residual scope item 7 — the wiki move + resources/ retirement, R-d + K14 at Q7''s re-priced true cost; K16 — the attestation-census pattern, E6)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): Q6 (the whole series ships this arc, model-first, the move as the capstone at true cost; fallback on record — deferral without re-litigating direction), E6 (the attestation census ships with the move), roundtable A2 (frontmatter bump from the version current at brief time, nine-consumer + workflow-ack walk), A10 (owner-ruled: ships as its own cut, alone; fired-fallback = bound inherited debt), plus the version-handshake and relocation-migration standing rules (vlt-upgrade/SKILL.md:75).'
risk: 'moderate — two convention rule changes (frontmatter@12→@13 nine-leg walk + extraction@4→@5 three-leg walk), a contract re-draw with rule-card re-derive (C6), a structure-map default change (E2 three-home agreement), and one new live-vault relocation migration; concentrated in the field relocation, which is bounded by the map (a declined offer is a two-line override, never a broken vault) and by the standing relocation-migration discipline.'
---

# Build #B10-11 — the wiki-move capstone

**The last build of Arc 10's A9-1 series, and its own release cut.** B10-10 shipped the
container model, the PARA parameterization (five `vault_structure` keys), the authorship
re-draw, and `grounding:`; what remains is the move itself: the wiki leaves the agent zone
for human-browsable space (`resources/wiki/`), and `resources/` retires as a PARA layer
member and extraction target — the vestigial state B10-10 stamped into the contract
(`vault-operating-contract.md:41` "vestigial; see `extraction.md`") resolves into the
directory's new purpose. Q7's re-priced true cost is this brief's scope, whole: two
`vault_structure` entries (`wiki`, `index`), the `type: resource` retirement riding a
`frontmatter` bump with the full nine-consumer + workflow-ack walk, an `extraction` bump
with its three-leg walk, the relocation-migration discipline applied to a live vault's
largest directory, and E6's attestation census designed and shipped **in the same build**
(enforcement-ships-with-widening).

All rejected alternatives in the parent filing are settled — do not re-litigate. In
particular: the write-time gate (R-a), the posture axis (C2), the verb-name question, and
the direction itself (Q6: "the direction is ruled") are closed. This brief also does not
re-open any B10-10 disposition (the container model, the five keys, the two-surface
authorship rule, the A11 adopt/decline calls).

## Q6 risk verdict — made explicitly at brief time, per the recorded fallback

**Verdict: BRIEF — the fallback does not fire.** ✅ **OWNER-RULED 2026-08-23 — VERDICT
CONFIRMED, with ground (4) superseded.** The owner's D1 ruling (option C — one cut)
postdates this verdict and falsifies ground 4: B10-11 is **not** isolated, it ships in
the v0.14.0 cut with B10-6..B10-10 and B10-12, and its acceptance run is entangled with
theirs. The verdict stands on grounds (1)–(3), and the entanglement is ruled acceptable
on the D1 record's own reasoning — the same cut carries **B10-12**, the repair to the
instrument that reads a relocation (full-mode lint's `missing_targets` moved-link
class), so the relocation's acceptance run is readable in a way option A's would not
have been. Accepted cost, on record: if the v0.14.0 acceptance run goes sideways,
attributing it to the relocation versus a sibling build is harder. No fallback, no delta
re-harvest, no bound-debt conversion. Grounds as recorded at brief time follow.

Grounds, against the current tree
(`arc10-v0.14.0` @ `b7193e8`, B10-6..B10-10 landed):

1. **The design risk is retired.** The prior clerk read ("moderate, concentrated in the
   live-vault relocation, not the design") has strengthened since: B10-10 shipped the
   model, the keys (including `resources`), the merge-config injection fix with its
   fixture, and the authorship re-draw. What this build changes is default *values*, prose
   recitations of those defaults, two convention rule rows, and one migration — no new
   mechanism class.
2. **The live-vault relocation is bounded three ways.** (a) Every consumer resolves paths
   through the `vault_structure` map, so a vault that declines the move (or hasn't
   upgraded) is made coherent by a two-line override — the failure mode is never a broken
   vault, only an un-moved wiki. (b) The relocation-migration discipline is standing and
   field-exercised (`vlt-upgrade/SKILL.md:75` — stub the old path, never touch worktree
   copies, re-point open dispatch pointers; the proto-spec retrofit and decision-log
   relocation already run under it). (c) Wikilinks are slug-based, not path-based — the
   link graph survives a directory move by construction; only the map values and the
   dispatch doc-path keys care.
3. **The handshake walk is practiced.** This is the fourth consecutive nine-leg
   frontmatter walk (B10-4 @10, B10-5 @11, B10-10 @12), gated by package-lint Group E.
4. **The cut is isolated by ruling.** Roundtable A10: B10-11 ships as its own release,
   alone, so its acceptance run is not entangled with B10-6..B10-10's
   (B10-10-without-B10-11 is a pre-ruled legal interim field state).

Because the verdict is BRIEF, the A10 bound-debt conversion does not fire, and this brief
may — and does — cite S1 (`skills/reports/spike-s1-para-container-harvest-2026-08-21.md`)
without a delta re-harvest: its Q7 note ("the wiki-into-resources move matches the field —
`resources/` already vestigial in both vaults") is part of this build's evidence base.

## Grounding correction (1)

**The roadmap's B10-11 bullet's bump arithmetic is stale again — expected bump is
`frontmatter@12 → @13`.** The bullet (roadmap §Grouping & order) says "the expected bump
here is @10 → @11" (A2's 2026-08-21 arithmetic). Since then B10-5 took @11 and B10-10 took
@12 (`frontmatter.md:11` reads `version: 12` on the current tree). A2's governing clause —
"from the version current at brief time" — is what binds; the parenthetical numbers were
illustrative and are superseded. A superseding note is appended to the roadmap (two-place
record, per `build-brief`'s grounding rule). Likewise `extraction.md` is at `version: 4`
(B10-10's A2 leg), so this build's extraction bump is **@4 → @5**.

All other capture-time sites re-grounded HOLDS with fresh lines (cited per F-site below);
the A9-1 capture's `frontmatter.md:159` / `:164` cites now live at `:169` / `:175`.

## Brief-time dispositions

1. **The new wiki home is `resources/wiki/` (a bounded subtree), not `resources/` root.**
   ✅ **OWNER-RULED 2026-08-23 — CONFIRMED** (with disposition 2).
   New defaults: `wiki: resources/wiki/`, `index: resources/wiki/index.md` — exactly the
   two `vault_structure` entries Q7 priced. Why a subtree: legacy loose `resource`
   artifacts (grandfathered, disposition 2) coexist at the `resources/` root without
   colliding with wiki pages; the archive mirror stays clean; the relocation is one
   directory move with one stub. The `resources` key itself is **kept** (B10-10 minted it;
   the derivation and links consume it) — its contract row re-semanticizes (F2).

2. **`type: resource` retires by grandfathering — no backfill, no forced re-type.**
   ✅ **OWNER-RULED 2026-08-23 — CONFIRMED** (the roadmap's designated brief-time
   question, ruled). Accepted on record: `resources/` carries two populations
   indefinitely — wiki pages under `wiki/`, and grandfathered loose `resource`
   artifacts at the root that nothing migrates. Consistent with the coexistence posture
   confirmed for legacy `status:` values (B10-10 disp. 7) and legacy `.md` reports
   (B10-6 disp. 8).
   (The roadmap's designated brief-time question.) The value leaves the mintable set: the
   extraction target table loses its `resources/` row and `vlt-extract` no longer offers
   the folder. Existing `type: resource` files stay **legal indefinitely** (the module's
   standard coexistence posture, already stated for enum values at `extraction.md`'s
   coexistence paragraph); no sweep, no lint finding class for legacy files, and
   `write-verification.md:55`'s jurisdiction sentence keeps `resource` (grandfathered
   files remain attestation-checkable). Where reference material goes now: **the wiki
   itself** — human-browsable is the whole point of this build; a "resource doc" request
   routes to the wiki (or to `areas/` when it serves an ongoing commitment). `vlt-extract`
   states this routing at its folder ask (F5).

3. **The relocation migration is a human-gated offer with a coherent decline path.**
   ✅ **OWNER-RULED 2026-08-23 — CONFIRMED as designed**: narrow firing condition
   (legacy default + no override), human-gated, main-tree-only, stub at the old
   `{index}`, decline writes the two pinning overrides and is idempotent by
   construction, archive mirror deliberately not rewritten. Reviewed expressly as the
   build's residual-risk site (a live vault's largest directory moved by an automated
   step); accepted on the desk-walked accept/decline/idempotence evidence.
   New `vlt-upgrade` Step-3 migration, **wiki-relocation** (F10): fires only when the
   vault's resolved `{wiki}` is the legacy default `_agent/wiki/` with no explicit
   override. On **accept**: move the directory to the new default per the
   relocation-migration discipline (main tree only; one-line pointer stub left at the old
   `{index}` path `_agent/wiki/index.md` — the single entry point every reader reads
   first; re-point open dispatch pointers whose doc path lies under the old wiki path);
   record `wiki-relocation` in `migrations_run`. On **decline**: write explicit
   `vault_structure` overrides (`wiki: _agent/wiki/`, `index: _agent/wiki/index.md`) into
   `config.yaml`'s `vlt:` section, so every consumer keeps resolving correctly —
   idempotent by construction (the override ends the offer's firing condition). Never
   auto-move. The archive mirror is **not** rewritten: `{archive}` mirrors the source path
   *at archive time* (the contract's archive-structure rule); pages archived from
   `_agent/wiki/` stay where they are, pages archived after the move mirror the new path.

4. **E6's census/staleness posture — the concrete check shapes** ✅ **OWNER-RULED
   2026-08-23 — CONFIRMED** (the roadmap's second designated brief-time question,
   ruled): the denominated `attestation_census:` slot computed reduce-only from values
   the scanners already return (no new ask, no `convRead` change, `PAGE_SCAN`
   byte-untouched — which B10-12's ceiling finding makes load-bearing), `attestation_stale`
   keeping its per-page listing beneath it, the one-sentence human-edit posture at the
   contract, and R3 satisfied at `checks.md:16`. E6 discharged in the same build as the
   move, as ruled. (the roadmap's second
   designated brief-time question). The K16 prediction: a browsable wiki gets human edits,
   which mass-produce `attestation_stale`. The design, in the arc's own signal-integrity
   idiom (the B10-3 collapse pattern):
   - **The census line.** The full-mode lint report gains one denominated slot,
     `attestation_census:` — `{pages_total, fresh, stale, unattested_pre_adoption}` —
     computed in the workflow's reduce step from the `verified_by`/`verified_at` values
     the page scanners **already return** (no new ask, no `convRead` change, no schema
     addition to `PAGE_SCAN`). `attestation_stale` keeps its per-page listing and its
     existing quiet legal response; the census is the scale-honesty layer above it, never
     a replacement for the entries.
   - **The human-edit posture, stated at the contract.** A human edit to a browsable wiki
     page is legal and expected; it surfaces as staleness, the next tier-1 re-run
     re-attests (the existing freshness mechanics, unchanged), and a substantive human
     revision moves `author:` toward `hybrid` per the honesty rule. One sentence in the
     contract's Layer-2 paragraph (F2) — pointer-not-mechanism; the mechanics stay in
     `frontmatter.md`/`write-verification.md`, untouched.
   - **R3:** the census line's legal response — informational, denominated, nothing owed
     per se; per-page responses unchanged — is stated at `checks.md:16` in the same edit.
   This discharges E6 in the same build as the move, as ruled.

5. **The write-boundary re-draw is the minimal one.** ✅ **OWNER-RULED 2026-08-23 —
   CONFIRMED**: `{resources}` leaves the Layer-3 enumeration, `{wiki}` is named
   partner-writable **through the map** (never by widening the `_agent/` prefix), and
   **no new PARA write surface is created** — the two named surfaces confirmed under
   B10-10 disp. 10 carry through unchanged. `{resources}` leaves the Layer-3
   enumeration (Layer 3 becomes `{projects}`, `{areas}`); the hard rule gains `{wiki}` as
   partner-writable territory *by name through the map*, not by widening the `_agent/`
   prefix — the wiki's ownership never changed, only its address. No new PARA write
   surface is created: extraction and container maintenance remain the only two, and the
   Layer-3 sentence keeps saying so verbatim.

6. **`extraction@4 → @5` is a rule change and bumps.** ✅ **OWNER-RULED 2026-08-23 —
   CONFIRMED**, including the no-bump call for `wiki-index@2` / `wiki-supersession@2` /
   `write-verification@3` / `decision-log@2` (a changed *default path* recited in a
   convention is prose — the rule "resolve through the map" is unchanged), and the
   grounding correction it rests on (`frontmatter@12 → @13`, `extraction@4 → @5`; A2's
   version-current-at-brief-time clause governs, the roadmap's illustrative numbers
   superseded, two-place record made). The target-folder table loses a
   row, the required-frontmatter `type:` enum narrows, and the per-type `status:` enum
   table loses its `resource` row — schema rule changes, not prose. Three-leg walk:
   `vlt-extract`, `vlt-lint`, `vlt-track` re-ack `extraction@5` in the same build.
   **No other convention bumps:** `wiki-index@2`, `wiki-supersession@2`,
   `write-verification@3`, `decision-log@2` carry only default-path or no recitation
   changes (prose clarifications don't bump).

7. **R1 (interim posture): the pre-release/pre-upgrade window is already legal by
   ruling.** ✅ **OWNER-RULED 2026-08-23 — CONFIRMED.** Recorded caveat: the A10 citation
   (B10-10-without-B10-11 as a legal interim field state) is moot under the owner's D1
   option-C ruling — that window never occurs in the field. The disposition's substance
   is unaffected: a not-yet-upgraded or declining vault is legal and coherent on the
   decline path's own overrides (disp. 3). The census ships with its mechanism in this build (nothing rules ahead of a
   mechanism). The field window between this release and a vault's upgrade — or after a
   declined offer — is the pre-declared legal state: the wiki stays at `_agent/wiki/`
   under the old default or an explicit override, and every consumer resolves through the
   map. Roundtable A10 already ruled B10-10-without-B10-11 (vestigial `resources/`
   standing) a legal interim field state.

8. **The stale-token sweep is scoped, not blanket.** ✅ **OWNER-RULED 2026-08-23 —
   CONFIRMED.** Recorded against the shipped result: the sweep came out cleaner than
   declared — context (b) (historical archive-mirror language) has **no surviving
   instance** in the shipped surface, and `_agent/wiki` survives only in context (a),
   the F10 migration bullet. The three-context declaration below over-declares against
   what shipped; no defect, noted so the record matches the tree.

   **Deviations accepted (owner, 2026-08-23):** the three numbered deviations in this
   brief's `status:` — `module.yaml`'s `module_greeting` reworded off "resource doc",
   `vlt-extract` Step 3's shape clause dropped and `vlt-agent-creative:27`'s example
   reworded, and `vlt-setup:116`'s phrasing — are **accepted as briefed-rule-reaching-
   unenumerated-sites**, the correct behavior for a vocabulary sweep, recorded not
   silent. `_agent/wiki/` legitimately survives
   in exactly three shipped contexts after this build: (a) the migration bullet's own
   firing condition and decline-override text (F10), (b) historical archive-mirror
   language where it describes *already-archived* content, and (c) nothing else. Every
   other `_agent/wiki` recitation is a default-path cite and updates (F7). The
   verification grep (§Verification) whitelists (a) explicitly.

## F-sites

### F1 — `skills/vlt-setup/assets/module.yaml` — the two entries (the SSoT)

**Current:** `:45` `wiki: _agent/wiki/`, `:46` `index: _agent/wiki/index.md`; `:67`
example line `"wiki → _agent/wiki/ — override a single entry only if this vault
diverges"`.

**Change:** `:45` → `wiki: resources/wiki/`; `:46` → `index: resources/wiki/index.md`;
`:67` example updated to the new default (`"wiki → resources/wiki/ — …"`). The
`resources: resources/` entry (`:54`) is **unchanged** (disposition 1).

**Why:** Q7's two entries; module.yaml is the single source of truth for path values
(its own `:41-43` comment) — every other home mirrors it (E2 checks the mirroring).

### F2 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` — the re-draw (+ rule card, C6)

Freshly grounded sites, all on the current tree:

1. **`:31-32` (structure-map table):** `wiki` row default → `resources/wiki/`, semantic
   column gains the browsability ("Canonical knowledge pages (one concept per page) — the
   human-browsable knowledge layer, partner-written"); `index` row default →
   `resources/wiki/index.md`. Middle column must keep mirroring module.yaml (E2).
2. **`:41` (`resources` row):** re-semanticize from "Reference artifacts — vestigial; see
   `extraction.md`" to the new purpose: "The wiki's human-browsable home (`{wiki}` lives
   here) — retired as an extraction target; legacy reference artifacts grandfathered
   (`extraction.md`)".
3. **`:64` (Layer 2):** the paragraph names the `{wiki}` among the agent zone's contents
   and says humans "do not write into it directly". Amend: the wiki remains **partner-
   owned** Layer-2 territory that now *lives at* `{wiki}` (default `resources/wiki/`)
   outside the `_agent/` prefix — ownership unchanged, address changed; add the one
   human-edit-posture sentence from disposition 4 (a human edit to a browsable wiki page
   is legal; it surfaces as attestation staleness and re-attests on the next tier-1 pass;
   substantive human revision moves `author:` toward `hybrid`).
4. **`:66` (Layer 3):** the enumeration `(`{projects}`, `{areas}`, `{resources}`)` drops
   `{resources}` → `(`{projects}`, `{areas}`)`. The two-named-surfaces sentence stays
   verbatim (disposition 5).
5. **`:68` (the hard rule):** "Partners write only to `_agent/` and `_meta/`" gains the
   wiki's new home: "Partners write only to `_agent/`, `_meta/`, and the wiki's home
   `{wiki}` — plus the two named PARA surfaces above…". Keep the rest byte-equivalent.
6. **`:163` (log line worked example):** the merge clause recites
   `{archive}/_agent/wiki/<subsumed>` — recast to the placeholder form
   `{archive}/{wiki}/<subsumed>` (the shipped-example placeholder-path rule; the archive
   mirrors the source path at archive time, so the placeholder is also more accurate).
7. **Rule card:** `_meta/vault-rule-card.md:26` recites the PARA triple and the write
   boundaries — **re-derive the card** against the edited contract, re-stamp
   `derived_from: … sha256:`, stay ≤ 8,000 bytes (**package-lint C6** is the gate).

**Out-of-scope at this site:** `:70` (PARA containers — unaffected; containers were never
in `resources/`), `:253-255`/`:278`/`:282`/`:318`/`:334`/`:337-338` (wiki mentions that
are semantic, not path recitations — no edit), the Decay-contracts and zone-map report
rows (no new persisted surface — E1/E2 census untouched).

### F3 — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md` — `@12 → @13`

**Current:** `:11` `version: 12`; `:12` nine consumers; `:71` canonical `type:` list
includes `resource`; `:169` heading `## PARA artifacts (`projects/`, `areas/`,
`resources/`)`; `:175` "`type:` mapped to target folder: `projects/` → `project`;
`areas/` → `area`; `resources/` → `resource`."

**Change:** `version: 12` → `13` (roster unchanged). `:71`: `resource` moves out of the
canonical list into a one-clause retired-legacy note ("`resource` is retired as of this
version — legal on existing files, no longer minted; `extraction.md`"). `:169` heading
drops `resources/`. `:175` mapping drops the `resources/` clause and gains the same
one-line legacy note. The attestation field definitions (`:73-84`) are untouched.

**Why:** Q7's grounded finding — retiring a `type:` value is frontmatter schema, a rule
change, hence the bump (A2: from the version current at brief time = @12 → @13).

**The nine-leg walk (same build, version-handshake standing rule):** re-ack
`frontmatter@13` at every leg —
`vlt-dispatch/SKILL.md:3`, `vlt-extract/SKILL.md:4`, `vlt-groom/SKILL.md:3`,
`vlt-research/SKILL.md:3`, `vlt-ingest/SKILL.md:4`, `vlt-mint/SKILL.md:3`,
`vlt-lint/SKILL.md:4`, `vlt-setup/SKILL.md:3`, and the workflow ack
`skills/vlt-setup/assets/workflows/vlt-lint-full.js:11` (`// depends_on:` header — the
E5 leg, a different edit surface). Per roundtable A8, the walk **re-derives the marked
restatements, not just the ack strings**: both `per frontmatter@12` markers at
`vlt-lint-full.js:173` cite **rule 4** (sources normalization + coexistence) — this build
does not touch rule 4, so verify still-true and re-stamp `@13`. Zero `frontmatter@12`
tokens anywhere in the shipped surface after the walk.

### F4 — `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md` — `@4 → @5`

**Current:** `:11` `version: 4`; `:12` `consumers: [vlt-extract, vlt-lint, vlt-track]`;
`:26` "PARA artifacts (`projects/`, `areas/`, `resources/`) are **extracted from the
wiki**…"; `:69` filename example `resources/spaced-repetition-primer.md`; `:81` target
table row `| resources/ | resource |`; `:87` `type: <project | area | resource>`; `:112`
status-enum row `| resource | complete | resources arrive finished |`.

**Change:** `version: 4` → `5`. `:26` folder list → two folders. `:69` example line
removed (two examples remain). `:81` row removed; add one sentence under the table:
legacy `resource` artifacts predating this version stay legal at the `resources/` root —
no backfill sweep, no re-type (the file's existing coexistence paragraph's posture,
extended to the retired type). `:87` → `type: <project | area>`. `:112` row removed; the
legacy sentence covers `status: complete` on grandfathered resources. Add the routing
sentence (disposition 2): reference material now lives in the wiki itself — the
human-browsable `{wiki}` — or in `areas/` when it serves an ongoing commitment.

**Three-leg walk (same build):** `vlt-extract/SKILL.md:4`, `vlt-track/SKILL.md:4`,
`vlt-lint/SKILL.md:4` re-ack `extraction@5`. Zero `extraction@4` tokens after the walk.

### F5 — `skills/vlt-extract/SKILL.md` — the write op loses its third target

**Current:** `:3` description ("…filed into projects/, areas/, or resources/… 'build a
resource doc on X'"); `:11` Overview (same triple + "extract a resource doc on X");
`:19` path-resolution line (recites `index` → `_agent/wiki/index.md`, `wiki` →
`_agent/wiki/`, and the three PARA targets); `:56-58` the folder ask ("Which PARA folder —
`projects/`, `areas/`, or `resources/`?" + the three-way guidance); `:74`
`type: <project | area | resource>`; `:81` status line's per-type enum recitation.

**Change:** description and Overview drop the resources/resource-doc phrasing (the
deliverable examples become project brief / area dashboard / wiki-bound reference); `:19`
recites the new defaults (`index` → `resources/wiki/index.md`, `wiki` →
`resources/wiki/`) and the two PARA targets; `:56-58` becomes a two-way ask with the
disposition-2 routing sentence for reference-material requests (point the user at the
browsable wiki; `areas/` when it serves a commitment); `:74` and `:81` match the @5
enums. Frontmatter ack: `extraction@5` + `frontmatter@13` (F3/F4 walks).

### F6 — `skills/vlt-agent-creative/SKILL.md` — the partner's vocabulary

**Current:** `:3` description ("…'extract a resource doc on X'"); `:18` "The PARA targets
you make into resolve through the structure map — `{projects}`, `{areas}`,
`{resources}`."; `:37` ("…project brief, area dashboard, or resource doc…"); `:63`
headless example ("extract a resource doc on X").

**Change:** drop the resource-doc phrasing at all four sites (`:3`, `:37`, `:63` — e.g.
"extract a deliverable on X"); `:18` targets become `{projects}`, `{areas}`. No ack edits
(partners carry no `depends_on:` pins — verified on the current tree).

### F7 — the default-path recitation sweep (prose, no bumps)

Each site recites the old `wiki`/`index` defaults; each updates to the new defaults, no
mechanics change, no version bumps (prose clarifications don't bump):

- `skills/vlt-ingest/SKILL.md:22` (path-resolution line) — new defaults.
- `skills/vlt-ingest/SKILL.md:111` and `:176` — `{archive}/_agent/wiki/` → the
  placeholder form `{archive}/{wiki}/` (matches F2 item 6; same rule).
- `skills/vlt-research/SKILL.md:17`, `skills/vlt-query/SKILL.md:16`,
  `skills/vlt-track/SKILL.md:29`, `skills/vlt-lint/SKILL.md:17` — path-resolution lines,
  new defaults.
- `skills/vlt-mint/assets/operation-skill-template.md:16` — the template's example
  defaults, new values (a template is copied verbatim — the K9 lesson).
- `skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md:22` —
  "(`_agent/wiki/index.md` by default)" → new default. **No bump** (`wiki-index` stays
  @2; the row-format rule is untouched — A10-10's contradiction is held for Arc 11 by
  owner ruling and is explicitly out of scope here).
- `skills/vlt-setup/assets/governance/_meta/conventions/wiki-consolidation.md:92`,
  `:111`, `:127` — `{archive}/_agent/wiki/` → `{archive}/{wiki}/` placeholder form.
  **No bump** (path recitation only).
- `skills/module-help.csv` **is not a file** — the canonical CSV is
  `skills/vlt-setup/assets/module-help.csv`: row `:5` (creative — args example "extract a
  resource doc on X") and row `:9` (extract — description/args/outputs recite the
  resources target) reword to the two-target reality. Keep the canonical 13-col header
  and full quoting (CLAUDE.md standing rule); no rows added or removed.
- `README.md:40` ("briefs, dashboards, resource docs") and `:71` ("project brief, area
  dashboard, resource doc") — reword; README is shipped surface.

### F8 — `skills/vlt-setup/SKILL.md` — the provisioning half

**Current:** `:60-61` the default-table rows for `wiki`/`index` (E2's third home);
`:116` "Confirm the `wiki` directory exists (`{root}/_agent/wiki/` by default)"; `:196`
container-layers creation line (creates `{resources}` among the four); `:357` the report
line naming the four container layers.

**Change:** `:60-61` new defaults (must mirror module.yaml — E2). `:116` new default in
the parenthetical; creation stays keyed on the resolved `{wiki}` (a fresh install now
materializes `resources/wiki/`). `:196` and `:357`: keep creating/reporting `{resources}`
(it is now the wiki's parent and still a mapped dir) — reword the `:196` clause so
`{resources}` is described as the wiki's home rather than a container layer; the
`{projects}`/`{areas}` halves are unchanged. Frontmatter ack: `frontmatter@13` (F3 walk).

### F9 — `skills/vlt-setup/assets/hooks/vlt-vitals.py` — the fallback mirror

**Current:** `DEFAULT_STRUCTURE_MAP` at `:137-138` carries `"wiki": "_agent/wiki/"`,
`"index": "_agent/wiki/index.md"` (the stated minimal mirror of module.yaml's SSoT).

**Change:** both values to the new defaults. (Grounding addition — the capture never
named this site; the map's own comment binds it to module.yaml.) The synthetic fixture
maps inside `tools/package-lint.py` (`:459`, `:473`, `:510`) and
`tools/test-package-lint.py` (`FIXTURE_STRUCTURE :51`, case 16 `:400`) are
**self-contained fixtures with arbitrary values — no edit** (verified: the harness builds
a fully synthetic tree; case 16 perturbs the fixture's own table). `tools/test-cost-manifest.py`
likewise fixture-internal — no edit.

### F10 — `skills/vlt-upgrade/SKILL.md` — the wiki-relocation migration

**Current:** the Step-3 migrations list runs `:77-82` under the standing
relocation-migration discipline preamble at `:75`; `:83` "Run any other migrations…";
`:108` the `migrations_run` enum.

**Change:** insert one new bullet before `:83`, **wiki-relocation (human-gated offer)**,
exactly as disposition 3 rules it: firing condition (resolved `{wiki}` is the legacy
`_agent/wiki/` with no explicit override), accept path (directory move per the discipline
at `:75` — cite it by pointer, never restate: stub at the old `{index}` path, main tree
only, re-point open dispatch pointers under the old wiki path), decline path (write the
two overrides into `config.yaml` `vlt:` `vault_structure`), idempotence (the override or
the completed move ends the firing condition), never auto-move, archive mirror untouched.
`:108`: add `wiki-relocation` to the `migrations_run` enum. No new Step-4 report key
(`migrations_run` carries the record; the persisted report contract is untouched — this
build stays out of E1/E2's census population).

**Why:** the ruled relocation-migration scope; the decline path is what makes the field
risk bounded (Q6 verdict, ground 2a).

### F11 — the E6 census (checks + report + workflow reduce)

1. **`skills/vlt-lint/references/checks.md:16`** (Attestation findings): add the census
   sentences — full mode renders the denominated `attestation_census:` line
   (`pages_total` / `fresh` / `stale` / `unattested_pre_adoption`) over `{wiki}`; the
   K16 rationale in one clause (the wiki now sits in human-browsable space — staleness at
   scale is expected, and the census is the honest rendering of scale); **R3 legal
   response stated in the same edit**: the census line is informational and denominated —
   nothing owed per se; per-entry responses (`attestation_stale` → quiet tier-1 re-run,
   etc.) unchanged.
2. **`skills/vlt-lint/references/report.md`**: add the `attestation_census:` slot beside
   the existing attestation slots (`:31-33`), annotated `# full mode`, never omitted in
   full mode (denominated empty form on a zero-page wiki); existing slots name/position
   stable.
3. **`skills/vlt-setup/assets/workflows/vlt-lint-full.js`** (reduce/assemble step): count
   the census from the per-page `verified_by`/`verified_at`/`created` values the scanners
   already return — pure JS arithmetic; **no `PAGE_SCAN` schema change, no prompt change,
   no `convRead` change** (R4 fan-out audit re-run and recorded in the BUILT status:
   no ask touched, no convention added — the audit is a verification, not an edit).

### F12 — `skills/vlt-lint/references/full-scale.md:7` — the derivation's nesting clause

**Current:** step 1's single-homed qualifying-key predicate excludes `wiki`, governance,
cold storage, and report dirs from `crossLayerSlugs`.

**Change:** one clause: a qualifying key's glob **excludes any subtree that is another
mapped key's home** (concretely: `{wiki}` now nests under `{resources}` — the wiki's
pages are the page population, not cross-layer targets). Single-homed here; no other site
restates it.

**Why:** with `wiki: resources/wiki/`, the `resources` key qualifies and would otherwise
double-cover wiki pages. (Grounding addition.)

## Registration

**No new skill, no new workflow — no marketplace.json or module-help.csv row additions**
(the CSV edits in F7 are rewording of existing rows). What this build does register:

- **`frontmatter@13`** — nine-leg re-ack walk, F3 (eight skill pins + the
  `vlt-lint-full.js` `// depends_on:` header, the E5 surface) + marker re-derive.
- **`extraction@5`** — three-leg re-ack walk, F4.
- **package-lint C6** — the contract edit re-derives `vault-rule-card.md` (F2 item 7).
- **package-lint E2** — the structure-map change lands in all three homes in the same
  build (module.yaml F1, contract table F2, vlt-setup table F8).
- **package-lint E5** — the workflow ack is its own edit surface; counted in the walk.
- No new package-lint check → **R2 not triggered** (no `test-package-lint.py` case owed;
  verified the existing fixtures are synthetic and unaffected, F9).

## Out of scope (dispositioned)

1. **A10-10 (wiki-index row-format contradiction)** — owner-ruled hold for Arc 11
   (2026-08-22, B10-11 ride-along explicitly declined). `wiki-index.md` gets only the F7
   default recite.
2. **Rewriting archived wiki paths** (`{archive}/_agent/wiki/` content in live vaults) —
   rejected: the archive mirrors the source path at archive time; history stays put
   (disposition 3).
3. **A factory sweep of live-vault wikis / any vault-side edit** — module source only;
   the field change rides `vlt-upgrade` (CLAUDE.md: never fix a module bug in a vault).
4. **The research-zone fan-out second cut** (`full-scale.md:7`'s named second-cut work) —
   untouched.
5. **The confidentiality field, trust-fork, propagation-debt** — B10-10's recorded
   decline/watch calls stand; not re-opened.
6. **`write-verification.md` jurisdiction sentence (`:55`)** — deliberately unchanged
   (grandfathered `resource` files stay in the attestation net; disposition 2). No bump.
7. **A `resources`-key deletion from the map** — rejected (disposition 1): B10-10 minted
   it, the derivation consumes it, and the directory has a successor purpose.
8. **Beat-2 / boot-cost re-measure** — the wiki was never in the fixed boot (the `{index}`
   read is map-resolved and unchanged in size); S2's figures are unaffected.

## Verification (unit, at rest)

1. **Handshake bipartite re-check — package-lint Group E (E1+E5) PASS** is the check of
   record for both walks (frontmatter@13 × 9 legs, extraction@5 × 3 legs). Aids while
   editing (never the recorded verification): `grep -rn "frontmatter@12\|extraction@4"
   skills/` → zero hits in the shipped surface.
2. **Structure-map three-home agreement — package-lint E2 PASS** (module.yaml ↔ contract
   table ↔ vlt-setup table).
3. **Rule card — package-lint C6 PASS** (re-derived, sha re-stamped, ≤ 8,000 bytes).
4. **Packaging lint — `uv run tools/package-lint.py` A/B/C/E PASS** mid-build (D rides
   the release, §Release).
5. **Stale-token sweep:** `grep -rn "_agent/wiki" skills/ README.md` → hits only in the
   F10 migration bullet (firing condition + decline overrides) — the disposition-8
   whitelist; and `grep -rn "resources/" skills/` shows no surviving claim that
   `resources/` is an extraction target or PARA layer member.
6. **Workflow:** `node --check skills/vlt-setup/assets/workflows/vlt-lint-full.js`; the
   census desk-check — hand-compose a 4-page scan result (fresh / stale /
   pre-adoption-unattested / attested-fresh) and verify the reduce renders
   `attestation_census: {pages_total: 4, fresh: 2, stale: 1, unattested_pre_adoption: 1}`
   and the per-page slots unchanged. **R4 audit re-run recorded** (no ask or read-list
   change expected — confirm and record in the BUILT status).
7. **Migration desk-walk against a temp fixture vault** (scratchpad): a config with no
   override + `_agent/wiki/{index.md, page.md}` + one open dispatch pointer at
   `_agent/wiki/page.md` → walk the accept path (files at `resources/wiki/`, one-line
   stub at `_agent/wiki/index.md`, pointer re-pointed, `migrations_run` carries
   `wiki-relocation`) and the decline path (overrides written; re-run offers nothing —
   idempotence). A real `vlt-upgrade` run is not scriptable at rest; the walk is the
   at-rest bound, the live half is acceptance check (5).
8. **Cross-file agreement greps:** the two-folder Layer-3 enumeration appears identically
   at every recitation site (contract `:66`, rule card, `frontmatter.md:169`,
   `extraction.md:26`, `vlt-extract`, `vlt-agent-creative`); the type enums agree
   (`extraction.md:87` ↔ `vlt-extract:74` ↔ `frontmatter.md:71`).
9. **R1** (interim posture): disposition 7. **R3** (legal response): F11 item 1. **R4,
   both senses:** *enumeration widening* (Arc 8 rule) — **not applicable**: no file joins
   an enumerated class (the wiki's files are the same population at a new address; the
   migration's stub is vault-grown, not shipped; F11 edits an already-manifested asset,
   adds none); *fan-out currency* (the roadmap's roundtable R4) — audit re-run per
   verification 6. **Scrub:** no
   personal or vault-local content in any changed shipped file; worked examples stay
   placeholder-form (F2 item 6, F7 archive recitations).

## Release (this build is its own cut — roundtable A10, owner-ruled)

B10-11 ships **alone**, in the release after the one carrying B10-6..B10-10 (expected
v0.14.0 → this cut expected **v0.15.0**; the number is called at release, not here). Per
the standing choreography (`vlt-release`): dual version bump
(`.claude-plugin/marketplace.json` `"version"` + `skills/vlt-setup/assets/module.yaml`
`module_version`), `uv run tools/package-lint.py --expect-version X.Y.Z` → tag only on
exit 0 with the PASS line in the release commit message, ff-merge to `main`, tag, push.
The build commit itself lands on `arc10-v0.14.0` (one commit, no release mechanics) —
the cut branches per `vlt-release` when the owner calls it.

## Acceptance (live — the same checks appended to the roadmap ledger)

**(1) `[ship-verifiable]`** — both handshakes bipartite-consistent under one build:
`frontmatter@13` across all nine legs with both `vlt-lint-full.js:173` markers re-derived
(rule 4 untouched, verified still-true) and re-stamped `@13`; `extraction@5` across all
three legs; zero `frontmatter@12`/`extraction@4` tokens in the shipped surface.
Discharged at rest by **package-lint Group E (E1+E5) PASS**, recorded in the BUILT
status.

**(2) `[ship-verifiable]`** — the move is coherent across every home at rest: the two new
defaults agree in all three structure-map homes (**E2 PASS**); the rule card is
re-derived ≤ 8,000 bytes (**C6 PASS**); the Layer-3 two-folder enumeration and the
two-named-surfaces sentence agree across all recitation sites; `_agent/wiki` survives
only in the migration bullet's firing/decline text; no shipped text still offers
`resources/` as an extraction target; **package-lint A/B/C/E PASS**. Discharged at rest
by the brief's greps + desk-checks.

**(3) `[ship-verifiable]`** — E6 shipped whole in the same build: `checks.md:16` carries
the census + its R3 response, `report.md` carries `attestation_census:` (existing slots
name/position-stable), the workflow reduce computes it with `PAGE_SCAN` and every scan
prompt byte-untouched (R4 audit re-run recorded), and the four-page desk-check renders
the denominated line. Discharged at rest.

**(4) `[ship-verifiable]`** — the release gate, own cut: both version strings bumped,
`package-lint --expect-version` exit 0 with its PASS line in the release commit, ff-merge
+ tag + push per `vlt-release`. Bounded by the release that ships this build.

**(5) `[field-contingent]`** — the relocation offer runs honestly on a live vault;
discharging event named: **the owner's vlt-core upgrade to the release carrying this
build** (performer: the owner; vault: vlt-core — factory-readable; evidence: the
persisted `_agent/upgrade-reports/*.yaml` Step-4 report — the B10-6 instrument — plus a
factory read of the vault). Pass, accept path = the wiki lands whole at
`resources/wiki/` (page count preserved), the one-line stub sits at
`_agent/wiki/index.md`, any open dispatch pointers under the old path are re-pointed,
`migrations_run` carries `wiki-relocation`, and the next partner activation reads the
`{index}` at its new home with no error. Pass, decline path = both overrides in
`config.yaml` and every skill still resolving the old home. Fail = a half-moved wiki, a
clobbered worktree copy, an orphaned open pointer, or a declined offer leaving default
resolution pointing at an empty `resources/wiki/`.

**(6) `[field-contingent]`** — the census reads the browsable wiki honestly at scale;
discharging event named: **the owner's first full-mode (>30 pages) `vlt-lint` run on
vlt-core after the relocation** (performer: the owner; vault: vlt-core; evidence: the
persisted `{lint_reports}` `.yaml` file — same event class as the open B10-2(5) /
B10-3(3) / B10-6(6) / B10-10(5) lint tails; one run can feed them all). Pass = the report
renders a denominated `attestation_census:` line whose `pages_total` matches the moved
wiki, `missing_targets` shows no new false class from the move (slug-keyed links
survived) and no wiki page double-reported as a cross-layer target, and any human-edited
page appears in the census counts rather than as a new loud finding class. Fail = a
missing/undenominated census line, a mass `attestation_stale` loud class, or a
path-shaped missing-target class born of the move.
