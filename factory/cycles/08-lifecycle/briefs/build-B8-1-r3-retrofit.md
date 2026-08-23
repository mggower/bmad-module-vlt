---
title: 'Build #B8-1 — the R3 retrofit (every shipped check names its legal response, stated where the check lives)'
status: 'BUILT 2026-08-17 — all five F-sites landed (F1 25 markers tagged/appended per the walk table; F2 known-incomplete marker appended, response sentence byte-identical; F3 surface_text semantics sentence, comment-only, WIRE_REQUIRED_FIELDS untouched; F4 :134 aligned to canonical wording; F5 R3 ritual bullet between R2 and R4). Verification: vitals fixture run green (both stock wires parse/evaluate), package-lint A/B/C/E PASS. Deviations: (1) marker census — `grep -ci "legal response" checks.md` returns 26, not the brief''s stated 25: 25 marked entries plus the pre-existing :45 worked example, which the brief''s arithmetic excluded from the marked-entry count but which necessarily matches the grep; denominator reconciled against the F1 table (27 rows, row 17 no marker, row 22 no edit — 25 markers exactly); the :41 entry additionally carries its pre-existing plain "legal response for the latter" prose on the same line (one entry, one bold marker — the plain phrase is stated response, not a marker). (2) residue (i) grep — `grep -rn "declared, not yet" skills/` is not empty: three shipped governance conventions carry the distinct, undrifted frontmatter comment "declared, not yet adopted" (plus gitignored skills/reports/ history); the drifted wording proper ("declared, not yet (since created: — N days)") greps to zero across shipped skills/ — the out-of-scope files were left untouched per F4''s single named site. (3) F3''s comment extension wraps across three header comment lines in the file''s own wrap style rather than one long physical line; wording per brief verbatim.'
module_code: 'vlt'
created: '2026-08-17'
derives_from:
  - 'skills/reports/archive/inbox-evolution-arc7-roadmap.md (R3 — declared Arc 7, built Arc 8; the standing-rules entry and closeout carry-forward 12)'
  - 'inbox/2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload.md (A8-2 — the R3-home flag only: its finding class is R3''s first live field instance; the shape fix itself is B8-2''s)'
roadmap: 'skills/reports/inbox-evolution-arc8-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-17): grouping row B8-1 + roundtable A3/A4/A15; pre-ideation ruling 3 (R3''s home GENERALIZED — the field lives where each check lives); ruling 4a (R3 joins Arc 8 as a build, R1 binds); ruling 4d + A15 (residue (i) rides B8-1)'
risk: 'low — prose/comment edits across four shipped files plus one factory reference; no convention version bump, no consumer walk, no change to what any check detects; the sole behavior-adjacent edit is an appended marker on one response sentence'
---

# Build #B8-1 — the R3 retrofit

R3 — *no finding class ships without a stated legal response; every check names what a
vault may legally do about it* — was declared in Arc 7 (archived Arc 7 roadmap, *Three
standing rules*) and assigned to Arc 8 to build. This build is that retrofit: every
existing shipped check gains (or has tagged in place) a one-line legal response at the
check's own single home, per pre-ideation ruling 3's generalization — **the field lives
where the check lives**, never in a named-seat list. It opens the arc deliberately: every
later Arc 8 build adds or changes a finding class and inherits R3's bar on landing.

The field already has a shipped worked example: the dispatch-routing-profile check
(`skills/vlt-lint/references/checks.md:45`) carries *"Legal response, stated at the
check: fix the profile…"*. The retrofit makes that form universal.

All rejected alternatives in the parent material are settled — do not re-litigate. In
particular: R3's home is a **rule**, not a file (ruling 3 — a named-seat list is the
enumeration-drift class the standing rules refuse); the inline-payload delivery *shape*
is B8-2's, not this build's (grouping table); wires are ruled **out** of the per-check
field (roundtable A4 — the ruled exception, F3 below).

## Brief-time dispositions

*(Headless run — dispositions 2, 4, and 5 are judgment calls made without the owner,
recorded here at the point they apply; each is overturnable at build review.)*

1. **Interim posture (R1) — substantive.** B8-1 ships rule and mechanism together for
   every existing check (the field lands in the same build), so nothing ships ahead of
   its mechanism **except one deliberately incomplete seat**: the pointer-integrity
   check's response (`ledger.md:25`) is *unperformable* for the unsolicited
   inline-payload class (A8-2 — no correct key exists to re-fire with). Per roundtable
   A3, that seat is stamped with the **current response unchanged PLUS an explicit
   known-incomplete-pending-B8-2 marker — the marker IS this check's R1 interim
   posture.** Window posture for the inline-delivery class: **drain normally; no re-fire
   expected.** B8-2 discharges the marker — same release preferred; if v0.11.0 ships
   without B8-2, the marker is field-visible and honest. B8-1 never rewords the response
   sentence itself. (Exact marker text: F2.)
2. **The field's form: tag-in-place where present, append where absent (headless
   call).** Roughly fifteen of the twenty-six check entries already state their response
   in prose (walk table, F1). Relocating those into a uniform terminal line would reword
   settled shipped text for cosmetic uniformity — the A3 no-reword posture generalized.
   Ruling: where a response exists in prose, **bold-tag it in place** so it carries the
   greppable "legal response" phrase (label added, response content unreworded); where
   absent, **append one terminal `**Legal response:** …` sentence**. Either way the cap
   binds: **one line per check** — response, not rationale (roundtable A4; `checks.md`
   is JIT-read whole every lint Step 2). One check entry = one marker, even when the
   entry names several finding ids (e.g. the three attestation findings share one line).
3. **Wires are out of the per-check field — the ruled exception restated at the
   registry.** Per A4: `tripwires.yaml` is a vault-grown registry (merged by `id`,
   `WIRE_REQUIRED_FIELDS`-enforced at `vlt-vitals.py:222`) and takes **no new required
   field**; a wire's legal response homes in **`surface_text` semantics** — the phrase
   already names the responding act on both stock wires ("run vlt-lint", "summon its
   partner"). F3 states that semantics rule in the header schema comment, comment-only.
4. **R3-the-rule's durable factory home: `build-brief` §7, beside R2 and R4 (headless
   call).** Ruling 3 made the *field's* home a rule but left the *rule's* own text homed
   only in an archived roadmap — "a rule with no home is a wish" is this arc's own
   dictum. Precedent: R1's and R4's ruled home is `build-brief` (cross-filing ruling 2,
   landed by A1); R2 already sits in brief-anatomy §7's ritual list. Ruling: F5 adds an
   R3 ritual bullet to `references/brief-anatomy.md` §7 so every future brief inherits
   the bar mechanically, not by memory (the failure A1 found R1 had lived for an arc).
   No Exit-gate change (R3 is a per-build verification ritual like R2, not a required
   section like R1/R4).
5. **Already-conformant surfaces are recorded, not churned (headless call).** The walk
   (F1 preamble) found several check-bearing surfaces whose responses are already stated
   inline where the check lives — `vlt-upgrade`'s Step-4 report lines ("lift to overlay
   or upstream", "re-apply locally or upstream", "reconcile"), the op-skill Verify
   blocks' fix-before-closing posture, `vlt-vitals.py`'s loud per-wire errors naming the
   missing field / unknown id, `decision-log.md:99`'s forward declaration of R3's bar.
   Ruling: these are dispositioned **conformant, no edit** in the walk table — a
   normalization pass over them would be churn without behavior change and would bloat a
   low-risk build.

## F-sites

### F1 — `skills/vlt-lint/references/checks.md`: the retrofit proper

**Current state:** the Step-2 check catalog defines twenty-six check entries across
tier 1, tier 2, and the governance block. One (`checks.md:45`, dispatch routing profile)
already carries the field in explicit form; ~14 others state their response in prose
without the label; ~11 state none. Re-grounded 2026-08-17 against `b117d81` working
tree — all sites HOLD.

**The change:** per disposition 2, give every check entry exactly one one-line legal
response, per the walk table below (the A4-mandated evidence record — **corpus:** the
shipped `skills/` tree at brief time; **predicate:** a shipped surface that defines a
finding class — a named condition a routine run renders to the vault such that a reader
can ask "what may I legally do about this?"; **denominator: 26 check entries in this
file**, plus the out-of-file hits in F2–F4 and the conformant/out rows at the foot).
The builder reconciles the exact entry count while editing; a discrepancy against 26 is
recorded as a deviation, never silently absorbed.

| # | Check (current line) | Response today | Action |
|---|---|---|---|
| 1 | Missing targets (:13) | stated ("create now / remove / mark as a needed stub") | tag in place |
| 2 | Frontmatter / Bases-field drift (:14) | partial ("typo (fix)… flag") | add: *fix the field to the schema (typo) or flag the structural call (new category) for the human* |
| 3 | Sources-vs-prose (:15) | implied (frontmatter is source of truth) | add: *reconcile the prose section to frontmatter `sources:` — frontmatter is the source of truth* |
| 4 | Attestation findings (:16) | partial (stale → re-run tier-1) | add one shared line: *`para_missing_attestation` → the owning writer re-runs its verify pass and attests, or the human rules the file human-authored; `unattested_write` pre-adoption → informational, no act owed; `attestation_stale` → re-run tier-1 quietly* |
| 5 | `review_due` (:17) | stated (three-outcome review) | tag in place |
| 6 | Orphan pages (:21) | stated (add Connections / flag for deletion) | tag in place |
| 7 | Stale claims (:22) | thin ("surface it") | add: *update the page from the newer source or mark it `[!stale]` — surfacing is lint's act, the write is the owner's* |
| 8 | `[!stale]` handling (:23) | thin ("surface … for resolution") | add: *resolve the claim (update or supersede) or re-date the marker deliberately* |
| 9 | Contradictions (:24) | stated (callout + disposition; `adjudicable` → backlog) | tag in place |
| 10 | Entity collisions (:25) | stated ("re-verify the name against a non-transcribed source or remove it") | tag in place |
| 11 | Unmarked supersessions (:32) | stated ("add the appropriate callout") | tag in place |
| 12 | Near-duplicates (:33) | stated (file to backlog; resolution is `vlt-ingest`'s) | tag in place |
| 13 | Thin pages (:34) | stated-ish (flag as merge/stub candidates) | tag in place |
| 14 | Index drift (:35) | absent | add: *repair the index — add/remove/re-categorize the structural rows to match the wiki (`{conventions}/wiki-index.md`)* |
| 15 | Convention coherence (:36) | homed in router prose (`SKILL.md:59`) | add at the check: *a human reconciles the consumer against the convention, then bumps the ack; dangling consumer → correct the `consumers:` list* — the router's :59 sentence stays as the auto-fix prohibition, the response line here is the single home (cite, don't duplicate) |
| 16 | Enforcement doctrine meta-check (:37) | absent | add: *repair the enforcement frontmatter to the declaration schema; stage changes go through the mint ceremony, never lint* |
| 17 | Read-before-flag preface (:39) | — | **not a check** (a memory protocol over the findings below; `unclassifiable` is a denominator line) — no marker |
| 18 | Convention base divergence (:41) | stated (lift to overlay or upstream; `baseline_missing` → mint it or remove it) | tag in place |
| 19 | Overlay append-only (:42) | absent | add: *re-express the duplicated section as a true addition (or upstream the rule change); `overlay_orphan` → rename to its base or remove* |
| 20 | Capability lane-safety (:43) | absent | add: *the human reconciles declaration vs body (fix the `write_scope`/`weight` or the body); `capability_skill_missing` → install/mint the op skill or fix the pointer* |
| 21 | Family invariants (:44) | stated ("a human reconciles the body or the contract") | tag in place |
| 22 | Dispatch routing profile (:45) | **already in R3 form** — the worked example | no edit |
| 23 | Personalized-extraction firewall (:46) | stated ("re-ground the claim in the wiki or move it") | tag in place |
| 24 | Spec candidates (:47) | stated (backlog item, named next owner; declines honored) | tag in place |
| 25 | Consult preconditions (:48) | stated ("closed by *having* the consult") | tag in place |
| 26 | `linkage_ripe` / `revisit_due` (:57, :63) | partial | add one shared line: *`linkage_ripe` → route the note to a partner for graduation judgment (never auto-promote); `revisit_due` → the owner revisits — refresh, retire, or re-date `revisit_after:`* |
| 27 | High-value gaps (:66) | thin ("candidates for new pages") | add: *write the page or record it as a stub in the index — or decline; candidacy is a surfacing, not a debt* |

*(Rows 17 and 22 carry no marker/no edit, so the marker denominator is **25 marked
entries** in this file — the builder's verification grep counts against 25 here, 26 with
`ledger.md`'s seat.)* The response wordings above are the brief's drafts; the builder may
tighten phrasing to fit one line but not change what act each names — a changed act is a
deviation to record.

**Why:** R3's bar, retrofit half — every finding class a lint run renders becomes one a
vault can lawfully act on without leaving the file.

**Per-site out-of-scope:** the report shape (`references/report.md`) and routing
(`fix-and-file.md`) do not start rendering the response per finding — see Out of scope.

### F2 — `skills/vlt-dispatch/references/ledger.md:25`: the known-incomplete stamp

**Current state (re-grounded, HOLDS):** the pointer-integrity findings bullet ends:
*"The finding's legal response: **the publishing partner re-fires the relay correctly
keyed; the recipient checks the malformed line off as superseded** (its own tagged
line — two-writer discipline holds)."* Already labeled — already R3-form.

**The change (roundtable A3, exact scope):** append to that bullet, **without rewording
anything before it**:

> *(Known-incomplete: for an unsolicited delivery whose payload is written inline, no
> correct key exists to re-fire with — this class's response is pending the
> delivery-shape build. Interim posture: drain the finding normally; no re-fire is
> expected of anyone.)*

B8-2 discharges this marker (removes it when it ships the shape and rewrites the
response sentence under R3's regime — same release preferred). The marker is this
check's R1 posture; leaving it in a shipped release is legal and honest.

**Why:** A8-2 proved this response unperformable for one class — R3's first live field
instance. Stamping the truth beats either silence or a premature reword of B8-2's
territory.

**Per-site out-of-scope:** the legacy line (`:26`) — its unit and wikilink-as-path rule
are B8-2's (evidence debt 3); B8-1 touches nothing there.

### F3 — `skills/vlt-setup/assets/tripwires.yaml` header: the ruled exception, stated where wires live

**Current state (re-grounded, HOLDS):** the schema comment reads
`surface_text  — the short phrase rendered beside the value on a trip` (line ~21). Both
stock wires' `surface_text` already name the responding act.

**The change:** extend that comment line (comment-only; no schema change):
`surface_text  — the short phrase rendered beside the value on a trip; phrase it as the responding act — a wire's legal response homes HERE, not in any per-check field`.
`WIRE_REQUIRED_FIELDS` (`vlt-vitals.py:222`) is untouched; the vault-grown registry
gains no new required field, so every existing vault's registry (local thresholds, local
wires) merges clean on upgrade exactly as today.

**Why:** roundtable A4 — the walk rules wires **out** of R3's per-check field explicitly;
the exception is stated at the registry so it is a recorded ruling, not a silent
omission.

### F4 — `skills/vlt-upgrade/SKILL.md:134`: residue (i)'s rider

**Current state (re-grounded, HOLDS — the drift confirmed):** the Step-5 ledger-template
comment reads `# per-convention: adopted <ref> | declared, not yet (since created: — N days) | axis not declared`,
while the canonical three-value wording at `:108` and `:115` is
`declared, no first instance yet (created YYYY-MM-DD — N days)`.

**The change:** align the `:134` comment to the canonical wording:
`# per-convention: adopted <ref> | declared, no first instance yet (created YYYY-MM-DD — N days) | axis not declared`.

**Why:** drift residue (i) from Arc 7's closeout (carry-forward 9), attached to B8-1 by
ruling 4d + roundtable A15 (B8-1 deterministically touches shipped prose first). Same
stale-wording class B7-8 swept; outside B7-8's stated scope then, closed now.

### F5 — `.claude/skills/build-brief/references/brief-anatomy.md` §7: R3's factory ritual line

**Current state (re-grounded, HOLDS):** §7's standing per-build rituals list carries R2
(fixture extension) and R4 (enumeration widening); R3 appears nowhere in the factory's
brief machinery — its text lives only in the archived Arc 7 roadmap.

**The change (disposition 4):** add one ritual bullet between R2 and R4:

> - **Legal response (R3)** — any build that adds or changes a finding class states that
>   class's one-line legal response at the check's own single home (the file where the
>   check lives — `checks.md` for lint, `ledger.md` for dispatch pointer integrity, and
>   so on), **in the same build**. A wire is the ruled exception: its response homes in
>   `surface_text` semantics (`tripwires.yaml`, header). A build that touches no finding
>   class states `R3: not applicable` in one line.

Factory-side file (gitignored dev machinery is `.claude/` — this edit does not ship into
vaults); no Exit-gate change (disposition 4).

**Why:** ruling 3 generalized the field's home to a rule; the rule itself needs the same
mechanical home R1/R2/R4 have, or it binds by memory — the exact failure A1 found.

## Registration

**None.** No new skill or workflow (no `module-help.csv` row); no `{conventions}/*.md`
rule change, so no convention `version:` bump and no consumer walk / re-ack —
`checks.md` and `ledger.md` are skill reference files covered by their skills' own acks,
`tripwires.yaml` is a seeded asset, and the F4/F5 edits are prose/factory.

## Out of scope (dispositioned)

- **The delivery shape and everything downstream of it** — the fourth relay form (or
  widened `answer`), the reword of `ledger.md:25`'s response sentence, the legacy line's
  unit + wikilink-as-path rule, the terminal state of the seven drained findings:
  **deferred-to-B8-2** (grouping table; A5). B8-1's marker is the seam.
- **Report-side rendering of responses** (`vlt-lint/references/report.md`,
  `fix-and-file.md`): the field is available at the check, which lint JIT-reads whole in
  Step 2 — **rejected-because** rendering it per finding would grow the report shape for
  no new information; a field filing may promote this later.
- **`vlt-lint-full.js` scanner prompts** — recite tier-1/2 *detection*, which this build
  does not change; responses are triage-side. **Rejected-because** no behavior depends
  on them carrying the field.
- **Normalizing already-conformant surfaces** (`vlt-upgrade` Step-1/4 finding lines,
  `vlt-track:113` / `vlt-extract:108` Verify blocks, `verify-skill-manifest.py`,
  `vlt-vitals.py` error surfaces, `decision-log.md:99`'s forward declaration):
  **already-covered-by** inline responses where each check lives — disposition 5;
  recorded in the walk, not edited.
- **A shipped preamble stating R3 inside `checks.md`** — **rejected-because** vaults do
  not author module checks; the bar binds module builds, so its home is the factory's
  brief machinery (F5). A vault-grown check surface, if one ever exists, files first.
- **Backfilling vault-side history** — the A8-2 field disposition stands
  (capture concurrence); nothing retro-fixed anywhere, and history is B8-2's seam
  regardless.

## Verification (unit, at rest)

- **Marker census against the walk denominator:** `grep -ci "legal response" skills/vlt-lint/references/checks.md`
  returns **25** (rows 1–27 minus the no-marker preface row and the already-formed :45
  row — the builder reconciles the exact figure against the F1 table and records any
  delta as a deviation); `ledger.md` still greps exactly one "legal response".
- **A3 no-reword check:** the diff on `ledger.md` shows only the appended marker — the
  response sentence before it is byte-identical.
- **Residue (i) closed:** `grep -rn "declared, not yet" skills/` returns nothing.
- **Wires unchanged mechanically:** `WIRE_REQUIRED_FIELDS` (`vlt-vitals.py:222`)
  untouched; run `vlt-vitals.py` against a temp fixture vault (fixture `_bmad/config.yaml`
  + seeded `tripwires.yaml`) and confirm both stock wires still parse and evaluate —
  the F3 edit is comment-only.
- **One-line cap honored:** no `**Legal response:**` addition in `checks.md` exceeds one
  sentence/line of response (rationale lives here in this brief, not in the file).
- **Packaging lint:** mid-arc `uv run tools/package-lint.py` groups A/B/C/E pass
  (D/`--expect-version` is the release gate, not this build's).
- **Fixture extension (R2): not applicable** — no release-gate check added or changed.
- **Enumeration widening (R4): not applicable** — B8-1 adds zero files; nothing joins
  any enumerated class (declared, not silent: every edit in this build is in-place).
- **A13 (arc cross-build rule):** B8-1 creates no new accumulating file.
- **Scrub:** no personal or vault-local content in any changed shipped file; the F2
  marker and all F1 response lines use placeholder/role vocabulary only.

Builder exit obligations (standing): rewrite this `status:` to a BUILT record with
numbered deviations; delete any `.decision-log.md`; one commit for the build.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** Every check entry in the shipped `checks.md` carries exactly
   one one-line legal-response marker — 25 in `checks.md` + 1 in `ledger.md`, matching
   this brief's walk denominator (26 entries, 2 no-marker rows) — verifiable at rest and
   again on the next ordinary upgrade's installed copy.
2. **[ship-verifiable]** `ledger.md`'s pointer-integrity seat carries the unchanged
   response plus the known-incomplete-pending-B8-2 marker; if B8-2 lands in the same
   release, the marker is discharged (removed) by B8-2 — either terminal state is legal,
   a silent third state (marker gone with no B8-2, or reword without B8-2) is the
   failure.
3. **[ship-verifiable]** `tripwires.yaml`'s `surface_text` semantics sentence is present
   and `WIRE_REQUIRED_FIELDS` is unchanged — on the next vlt-core upgrade the vault's
   registry (local thresholds/wires) merges clean with no new-field friction.
4. **[ship-verifiable]** Residue (i) closed: the third adoption wording in
   `vlt-upgrade/SKILL.md`'s ledger template matches the canonical Step-4 wording; the
   drifted phrase greps to zero across `skills/`.
5. **[field-contingent — vlt-core]** On the first post-upgrade lint or `ledger` run that
   renders at least one finding, the maintainer can perform (or explicitly decline) the
   response named at the check without leaving the file — no rendered finding class
   whose response is absent or unperformable (the inline-delivery class is exempted by
   its marker, honestly, until B8-2's discharge). Producing vault: **vlt-core** — the
   readable primary field vault, which runs lint/ledger routinely, so the event is of a
   kind that will occur; it needs a real finding to render, which nothing in the release
   itself causes.
