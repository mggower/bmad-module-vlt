---
title: 'Build #16 — frontmatter@3: bell + attestation + freshness (the one coordinated schema bump)'
status: 'BUILT 2026-07-06 — all nine F-sites landed; unit verification PASS (bipartite handshake exact: frontmatter@3 × 5 pins, write-verification@1 × 4 pins; doctrine self-test scripted over all 7 conventions → valid, zero declared_untripwired/deferral_invalid; verified: naming sweep clean on shipped surface; review_after semantics defined once; node --check both workflows; package-lint A/B/C PASS). Deviations, all additive: (1) vlt-lint-full.js gained an optional `today: YYYY-MM-DD` arg (workflow scripts have no clock — Date.now() throws) so the reducer can compute review_due; the vlt-lint SKILL invocation now passes it, and its absence is reported as a coverage cap, never silently skipped. (2) para_missing_attestation is emitted by the workflow reducer as an empty structural slot with a comment — PARA files are outside its {wiki} page set; the SKILL fills that slot from its own jurisdiction scan (stated in the SKILL fan-out step). (3) The version:/consumers:-absence flag (091004 LB3) got a named report key, convention_meta_missing. (4) PAGE_SCAN also gained `created` so the SKILL can gate unattested_write as informational for pre-convention files. Ships in 0.6.0 alongside build-18 (overlay-subsumption pass, same release — see Migration).'
module_code: 'vlt'
created: '2026-07-06'
derives_from:
  - 'inbox/2026-07-06-091004-no-boundary-without-a-bell.md (A3-4 — the doctrine)'
  - 'inbox/2026-07-06-091005-write-verification-attestation.md (A3-5 — design-stage; measurements pending at M4)'
  - 'inbox/2026-07-06-091006-review-after-freshness-key.md (A3-6 — design-stage; first review-cycle evidence pending)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-06): one bump/one walk, NOT split; lint attests narrowly; lint/dispatch find + tripwires nag; ship no .base (owner ruling in 091006); 091004 LB2 + 091006 LB1/LB2/LB3 are build-18; Bases date-filter spike CLOSED (today() function; guard + date() wrap)'
risk: 'moderate — the arc''s largest build, but mostly additive prose + frontmatter; one convention version bump with a five-consumer walk; no destructive migration anywhere (absence = evergreen; unattested legacy files informational-only)'
---

# Build #16 — frontmatter@3: bell + attestation + freshness

Goal: one coordinated `frontmatter.md` `version: 2 → 3` carrying three designed-together
key families — the enforcement/bell declaration (091004), the write-attestation pair
(091005), and the `review_after:` freshness key (091006) — plus the new
`write-verification.md` convention, the mint/council/lint machinery that makes the
doctrine bite, and the backfill stamps that make every shipped convention honest about its
own enforcement. Splitting these re-creates the three-uncoordinated-overlays failure mode
they were designed against; they share one file, one bump, one consumer walk, and
cross-referencing semantics (`review_after` defined once; attestation freshness keys off
`last_updated`, never `review_after`).

**All rejected alternatives in the three filings are settled — do not re-litigate**
(payload-in-v1, substrate-first, Warden partner, bell-review ritual; micro-lint-beside-
Verify, body-block attestation, blocking gate, pre-commit hook; trust-decay, shelf_life
durations, accessions file, SQLite, per-source strings).

## Brief-time decisions (the filings' open questions, resolved here)

1. **Date-key naming (091005 Q1, one-shot): `verified_at:`, not `verified:`.** The
   `trust:` ladder already has a `verified` *rung* (`frontmatter.md:44/:62`) — same word,
   orthogonal axis. In an arc whose whole point is machine-readable state, a key a grep
   can't distinguish from a rung value is a self-inflicted wound; `verified_by`/
   `verified_at` is also the cleaner symmetric pair. Everything in 091005 that says
   `verified:` ships as `verified_at:` (freshness rule: valid iff `verified_at` ≥
   `last_updated`).
2. **Schema home (091005 Q2): split, as the filing recommends.** Field *definitions*
   (`verified_by`, `verified_at`, `review_after`, the enforcement/deferral keys) live in
   `frontmatter.md` v3 — one joint schema surface; the tier-1 *checklist and contract*
   (fail-open rule, MHC scope rule, membership test, promotion path, sample-audit) live in
   `write-verification.md`.
3. **`enforcement_stage` is module-generic (091004 Q1).** It describes whether shipped
   machinery exists. A vault-local check promotes the stage via a base edit, which
   correctly surfaces as upstream-bound divergence — that's the rail working, not a leak.
4. **v1 scope: conventions + the mint classifier only (091004 Q2).** Family contracts and
   the operating contract's own rules adopt the keys in a follow-up once the pattern
   proves. (The operating contract is deliberately un-handshaked — stamping it needs its
   own thought, not a rider.)
5. **Overlay-created boundaries declare in the overlay's own frontmatter (091004 Q3):
   yes.** One sentence in vlt-mint's Edit-a-convention overlay path (F5). The classifier
   applies to every boundary-creating mint regardless of landing zone.
6. **Lens placement (091004 Q4): workflow mint-mode rubric line**, per the KIND_PANEL
   single-home precedent. Personas stay generic — a bell persona is a Warden by another
   name.
7. **spec.md adoption (091004 Q5): this build's backfill walk retrofits the formal keys**,
   replacing build-15's declared-stage prose bell with the equivalent frontmatter
   (`enforcement_stage: declared` + the lint-check deferral, `review_after: 2026-08-17`,
   escalation trigger preserved in prose). Resolved by the ruled build order.
8. **Lint as attester (091005 Q3): RULED at ideation — yes, narrowly.** Lint writes
   `verified_by: vlt-lint` + `verified_at:` ONLY on files its Step-3 auto-fix touched
   (otherwise auto-fix bumps `last_updated` and re-stales the attestation it just
   validated). Lint never attests files it merely read. `verified_by`'s value set is
   therefore the three write ops + `vlt-lint`, stated in the convention.
9. **Sample-audit rate (091005 Q4): ship 1-in-5** as the stated default, explicitly
   tunable after cycle 1 (the convention says "≈1 in 5, tune on evidence").
10. **Family invariant (091005 Q5): after M4.** Parked in the roadmap; would exercise
    build-7's shipped-but-unexercised family machinery — do it deliberately, not as a rider.
11. **Bases (091006 Q1/Q2): ship NO `.base` file** (owner ruling in the filing — vlt-core
    folds views into its vault-grown `wiki.base`; a shipped `ledger.base` would diverge
    from the reference vault on day one). No `bases:` structure-map row. The three views
    ship as **documented reference** in the convention text, using the spike-verified
    syntax (roadmap §Ideation rulings): Due-for-review filter
    `and: [review_after, review_after <= today()]` — `today()` is a global function; the
    presence guard is load-bearing (absence = evergreen must not match); note the
    `date(review_after)` wrap as the robust form if the property registers as text.
    Fallback view (Horizon sorted ASC) documented but no longer the primary.
12. **Aging-queue escalation (091006 Q4): RULED — tripwire (build-17).** Lint emits
    `review_due` findings; it does not nag. The escalation wire is registry material.
13. **v2 keys (091006 Q5): parked** for a future `frontmatter@4` against usage evidence
    (`source_type:`, `review_note:` — named in the roadmap, not here).
14. **Consumer-walk union — vlt-extract joins too.** The filings add vlt-mint (091004) and
    vlt-research (091005 LB1) to `frontmatter.md`'s `consumers:`; capture grounding found
    **vlt-extract equally omitted** (it writes PARA frontmatter the convention defines —
    the same defined-but-unenforced shape). The walk registers the full writer/checker
    set: `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint]`.

## F1 — `frontmatter.md` v3 (the one bump)

`skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md`, `version: 2 → 3`,
`consumers:` per decision 14. Three additions, all **flat keys** (YAML rule 3 at `:29`
forbids nesting — 091004 LB1's correction is binding; check every key against rule 3):

- **§Enforcement declaration** (new section; applies to `{conventions}/*.md` files' own
  frontmatter): `enforcement_stage: declared | checked | enforced`,
  `enforcement_checked_by:` (partner or skill), `enforcement_moment:` (e.g. `lint run`,
  `op final-steps`, `SessionStart hook`), `enforcement_counter:` (optional until the
  enforcement kit lands; when 091003 ships, its `metric` ids are the only legal values —
  the vocabulary is defined once, there). Deferral block — **all three required, missing
  any = invalid**: `deferral_metric`, `deferral_threshold`, `review_after`. Stage
  semantics verbatim from the filing (`checked` = mechanical check + named owner + moment;
  `enforced` = fires at a moment needing no human memory).
- **Attestation keys** (on agent-written artifacts): `verified_by:` (value set per
  decision 8) and `verified_at: YYYY-MM-DD`, with the freshness rule (valid iff
  `verified_at` ≥ `last_updated`; stale → quiet tier-1 re-run, not a violation) and a
  pointer to `write-verification.md` for the contract. Explicit disambiguation sentence
  against the `trust: verified` rung (different axis: structural verification vs claim
  verification).
- **`review_after: YYYY-MM-DD`** in the wiki-page schema block (`:71-80`) + semantics
  paragraph: optional; **resolved date, never a duration; absence = evergreen**; set at
  write time only for time-sensitive content (pricing, versioned tools, event timelines,
  dosing/market state); on review exactly one of three legal outcomes — bump the date,
  mark claims `[!stale]` per `wiki-supersession.md`, or remove the key. **Defined once,
  here** — the deferral block above references this definition; 091005's freshness rule
  deliberately does NOT key off it. Amend the conflation line at `:48` (`last_updated` as
  lint's staleness signal) to note that a page carrying `review_after` announces its own
  expiry.
- **frontmatter.md's own v3 frontmatter is the doctrine's first self-application:** stamp
  it `checked` (`checked_by: vlt-lint`, `moment: lint run`) and record the
  checks-as-payload deferral — `deferral_metric: prose/behavior drift lint findings + new
  conventions minted`, `deferral_threshold: 2 drift findings, or the 3rd new convention`,
  `review_after: 2026-08-17`.

## F2 — NEW convention: `write-verification.md`

`skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md`,
`version: 1`, `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint]`. Contents:
the unified tier-1 checklist per artifact kind (extracted from the three ops' current
Verify steps — `vlt-ingest` Step 9 `:148-156`, `vlt-extract` Step 8 `:106-114`,
`vlt-research` Phase 5 `:80-88`, which already cover ~the same set: frontmatter
completeness + no stray `key:`, wikilink resolution, source coverage, log entry where
applicable); the attestation schema (pointer to F1's definitions) + freshness rule; the
**fail-open rule** (fix what you can, flag what you can't, always complete the write); the
**MHC scope rule** verbatim (attestation is a self-marker — lint flags only unmarked cells
*claiming to be self*: vault `type:` + `author: agent|hybrid`, no attestation; `daily/`,
raw `sources/`, human PARA files are out of jurisdiction — load-bearing for report trust);
the **tier membership test** (one-file-checkable → tier-1; corpus-knowledge → tier-2) +
**promotion path** (tier-2 class recurring ≥2 sweeps and deterministically checkable →
tier-1); the sample-audit rate (decision 9); the threat model sentence (defends bypass,
not deception). Ships **with its own bell natively**: `enforcement_stage: checked`,
`enforcement_checked_by: vlt-lint`, `enforcement_moment: lint run`.

`skills/vlt-setup/SKILL.md:143` §2 enumeration gains `write-verification` (after build-15
the set is `{frontmatter,wiki-index,wiki-supersession,wiki-consolidation,extraction,spec,
write-verification}`). Baseline stash covers it automatically.

## F3 — backfill stamps: every shipped convention gets an honest bell

All conventions in the bundle (five stock + build-15's `spec.md`; `write-verification.md`
arrives stamped):

- `frontmatter.md`, `wiki-index.md`, `wiki-supersession.md`, `extraction.md` →
  `checked` (`checked_by: vlt-lint`, `moment: lint run`) — lint carries their finding
  keys (`vlt-lint/SKILL.md:62`, `:61`, `:58`, `:68` respectively). **Honesty note carried
  into each stamp's decision-log entry:** `moment: lint run` is today a moment nobody
  owns; 091003's lint-debt wire is what makes it real — until then `checked` is the
  ceiling, and that is the ruled posture (ideation ruling 3: lint-moment bells stay
  honest-ceiling).
- `wiki-consolidation.md` → the `declared` holdout (lint only finds near-duplicates `:59`
  and hands resolution to ingest `:91`; note its `consumers:` is `[vlt-ingest]` only).
  Gets the **tripwired deferral**, not a naked stage — proposal (build may tune numbers,
  not shape): `deferral_metric: near-duplicate findings carried unresolved across sweeps`,
  `deferral_threshold: 3 carried across 2 consecutive sweeps`,
  `review_after: 2026-08-17`.
- `spec.md` → formal keys per decision 7 (replacing build-15's prose bell; the escalation
  trigger sentence stays in the body).

These are base frontmatter edits on module source — no consumer re-ack beyond the walk
already in flight (the stamps ARE part of the v3 rule change for frontmatter.md; for the
other conventions the stamps add fields without changing any rule consumers follow, so
**their** `version:` fields do NOT bump — prose/frontmatter additions that alter no
consumer-facing rule, per the standing bump discipline).

## F4 — mint templates: the boundary classifier

`skills/vlt-mint/assets/{capability-template,operation-skill-template,
partner-agent-template}.md` each gain an `## Enforcement` block: the classifier question —
**"does this mint create a rule someone else must obey?"** — with a one-line recorded
exemption for non-boundary mints (keep honest small mints fast); if boundary-creating:
who checks / at what moment / against which counter, or a complete tripwired deferral
(all three fields).

## F5 — `vlt-mint/SKILL.md`: three touches + the overlay sentence

- **(a)** Phase 1 kind-determination (`:31-52`): ask the classifier, record the answer in
  the planning doc.
- **(b)** *Edit a convention* (`:124-134`): a new or base-edited convention must carry
  valid enforcement frontmatter (stamps ride the existing base-edit + handshake ceremony);
  **plus the decision-5 sentence on the overlay path**: an overlay addition that creates
  a rule carries its enforcement declaration in the overlay file's own frontmatter.
- **(c)** Phase 2→3 exit gate (`:95`): a boundary-creating mint cannot pass with neither
  a bell nor a valid deferral.
- Stage promotions (`declared → checked → enforced`) are dated entries in
  `_agent/mint/decision-log.md`.
- Frontmatter: `depends_on` gains `frontmatter@3` — appended to build-15's
  `["spec@1"]` block (build order matters; vlt-mint is a NEW frontmatter consumer: the
  templates now encode the schema).

## F6 — council: the "where's the bell?" lens

`skills/vlt-setup/assets/workflows/vlt-review-council.js`, `mode: 'mint'` (`:74`), gated
kinds only: inject the standing question into the lens briefs via `lensPrompt`
(`:126-132`) and give the moderator (verdict enum `:114/:161-163`) the rejection rule — a
boundary-creating mint lacking the Enforcement section, or carrying an incomplete
deferral, is `revise`/`reject`, never `pass`. Personas untouched (decision 6). Workflow
`args` parse-on-intake discipline unchanged. vlt-mint's ack covers this asset per the
existing rule.

## F7 — the three write ops: refactor Verify, attest

- **`vlt-ingest/SKILL.md`**: Step 9 → "run tier-1 per `{conventions}/write-verification.md`,
  then write `verified_by`/`verified_at` on every page created or updated" — do NOT
  restate the checklist (single-home). Step 6 frontmatter block (`:107-124`) gains the
  optional `review_after` line ("if content is time-sensitive, set a resolved date");
  Step 9 gains the matching checkbox ("present iff time-sensitive, a date not a
  duration"). `depends_on` → `["frontmatter@3", "wiki-index@2", "wiki-consolidation@1",
  "wiki-supersession@1", "write-verification@1"]`.
- **`vlt-extract/SKILL.md`**: Step 8 same refactor + attest. `depends_on` →
  `["extraction@2", "wiki-supersession@1", "frontmatter@3", "write-verification@1"]`
  (frontmatter pin new, per decision 14).
- **`vlt-research/SKILL.md`**: Phase 5 same refactor + attest (research attests the note
  it creates). **ADD the `depends_on:` block — it has none today** (`:1-4`):
  `["frontmatter@3", "write-verification@1"]`. This closes 091005 LB1 (invisible in both
  directions).

## F8 — `vlt-lint/SKILL.md`: tiers, doctrine meta-check, freshness finding

- **(a) Tier reorganization:** Step 2 (`:51-69`, currently one flat list) splits into
  *Tier 1 — structural* (re-checked only on unattested/stale files) and *Tier 2 —
  judgment* (the sweep), with the membership test stated by pointer to
  write-verification.md.
- **(b) Doctrine meta-check** (both modes) — new `flag_for_human` keys (`:109-120`):
  `enforcement_missing`, `deferral_invalid` (any of metric/threshold/review_after absent),
  `deferral_expired` (past `review_after`), `declared_untripwired`. **Plus:** flag a
  `{conventions}/*.md` missing `version:`/`consumers:` entirely — closing 091004 LB3 (the
  coherence check at `:63` currently reads "carrying", making the whole machinery opt-in).
  Never auto-fix — stages promote through the mint ceremony only.
- **(c) Attestation findings** — `para_missing_attestation` (the Wispr net: vault `type:`
  + `author: agent|hybrid`, no attestation, PARA location — a real finding from day one),
  `unattested_write` (agent-lane wiki/research file, no attestation — **informational,
  not a violation, for files with `created` predating convention adoption**),
  `attestation_stale` (`last_updated` > `verified_at` → quiet tier-1 re-check). Re-scoping
  rule: attested-and-fresh files skip tier-1; sample-audit ≈1 in 5. Lint-as-attester per
  decision 8 (auto-fix-touched files only). Note in the stale-claims bullet (`:55`) that
  `review_after` pages self-announce (no mtime inference needed for them).
- **(d) `review_due`** — new finding: `review_after` in the past → `flag_for_human`
  (page + date). Never auto-fix; never nag (escalation is build-17's tripwire).
- **(e)** `depends_on` → bump to `frontmatter@3`, add `write-verification@1` (appended to
  the existing list at `:4`).

## F9 — `vlt-lint-full.js`: the fan-out schema

`skills/vlt-setup/assets/workflows/vlt-lint-full.js`: PAGE_SCAN schema (`:62-83`) gains
the attestation fields (present / `verified_by` / fresh-vs-`last_updated`) and
`review_after`; the reducer (`:130`, emitting `flag_for_human` at `:247`) emits the four
new keys (`para_missing_attestation`, `unattested_write`, `attestation_stale`,
`review_due`). vlt-lint's ack covers this asset (the rule at `:63`) — the self-enforcing
rollout claim holds with zero new machinery.

## Consumer walk (the one walk — exit gate: bipartite-consistent)

| Convention | v | consumers (after) | acks (after) |
|---|---|---|---|
| frontmatter.md | **3** | vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint | all five pin `frontmatter@3` |
| write-verification.md | 1 (new) | vlt-ingest, vlt-extract, vlt-research, vlt-lint | all four pin `write-verification@1` |
| spec.md, wiki-* , extraction.md | unchanged | unchanged | unchanged (stamps bump no `version:`) |

Every consumer's reconciliation is a real edit in this build (not a bare ack) except
possibly none — each of the five encodes changed rules. The existing coherence check +
the new (b) meta-check police drift after.

## Migration / upgrade path

- **No corpus backfill, by construction.** `review_after` absent = evergreen (122 legacy
  pages, zero noise); attestation is written on next touch; `unattested_write` stays
  informational for pre-convention files. Only `para_missing_attestation` is a real
  finding from day one. Seeded-backfill guidance (~10–15 clearly time-sensitive pages,
  Librarian judgment) ships as an optional note, not a migration step.
- **vlt-core convergence:** the vault lands (or will land) the local prototypes as
  overlays + base stamps; the 0.6.0 refresh overwrites local stamps with identical shipped
  ones (convergence, not loss), the baseline refresh clears `convention_base_divergence`,
  and the then-subsumed overlay sections are retired via **build-18's
  overlay-subsumption pass — the coupling that put build-18 in the same release.**
  Document the retire cue in the release notes (per 091004's migration section).
- **Skill-file acks ride the normal skill refresh**; post-upgrade lint confirms the
  handshake.
- **vlt-core's planned local template edits** are protected from the 0.6.0 clobber by
  shipping the template changes IN 0.6.0 (this build) + build-18's divergence net —
  091004 LB2's fix is build-18 scope, but the convergence is this build's.

## Out of scope (dispositioned)

- **091003 (enforcement kit)** — build-17, trails 0.6.0. `enforcement_counter` values
  stay optional/absent until its `metric` vocabulary exists.
- **Overlay-subsumption pass, overlay-aware consumer activations, skill-asset divergence
  net, handshake-overlay-axis stated property** (091006 LB1/LB2/LB3, 091004 LB2) —
  **build-18**, same release.
- **Family-contract + operating-contract bells** (091004 Q2), **family invariant for
  write ops** (091005 Q5), **v2 keys** (091006 Q5) — parked per decisions 4/10/13.
- **Aging-queue escalation** — build-17 tripwire (decision 12).
- **Shipped `.base` file / `bases:` row** — ruled out (decision 11); revisit only if the
  reference-vault posture changes.

## Verification (unit, at rest — lifecycle step 5)

- **Handshake bipartite:** greps confirm the walk table exactly — `frontmatter@3` pinned
  by exactly five skills; `write-verification@1` by exactly four; `frontmatter.md:12`
  consumers list matches; no skill still pins `frontmatter@2`.
- **Rule 3 compliance:** grep the new schema blocks for nested maps → zero (all keys
  flat).
- **Doctrine self-test:** run the F8(b) meta-check logic by hand (or a throwaway script)
  against `skills/vlt-setup/assets/governance/_meta/conventions/` → all seven conventions
  valid (six stamped + write-verification native); zero `declared_untripwired`; zero
  `deferral_invalid`; every file carries `version:`/`consumers:`.
- **Naming sweep:** grep `verified:` across changed files → hits only in trust-rung
  contexts; the attestation key is uniformly `verified_at:`.
- **`review_after` single definition:** grep across the bundle → semantics paragraph
  exists once (frontmatter.md); every other mention is a reference.
- **Templates + council:** all three templates carry `## Enforcement` with the classifier;
  `node --check` passes on `vlt-review-council.js` and `vlt-lint-full.js`; the rubric
  line appears in mint-mode only.
- **Single-home:** the tier-1 checklist text exists only in write-verification.md; the
  three ops point at it (grep for checklist items in op SKILLs → zero restatements).
- **Packaging:** `uv run tools/package-lint.py` → exit 0.
- **Scrub:** no vlt-core personal content in any changed shipped file.

## Acceptance (live — appended to the Arc 3 roadmap ledger)

- **0.6.0 upgrade on vlt-core:** consumer handshake converges (post-upgrade lint run shows
  zero coherence findings); base stamps converge with local ones; divergence flags clear
  after build-18's subsumption pass retires shadowed overlay sections.
- **First post-upgrade lint run behaves on a legacy corpus:** no false-positive flood —
  `unattested_write` informational-only on pre-convention files, `review_due` fires only
  where the key is set, `para_missing_attestation` fires only on genuine bypass artifacts
  (the Wispr file, if unremediated, is the expected true positive).
- **Doctrine live test (shared with build-15):** the next boundary-creating mint on
  vlt-core passes through classifier + council lens + exit gate and lands with
  days-to-first-check = 0 (firewall baseline: 4); zero conventions sit `declared` without
  a tripwire.
- **Design-stage evidence debts (pending attachments, from the filings):** 091005's two
  measured lint cycles under the attestation contract (M4 — re-scoping actually shrinks
  sweep cost; sample-audit rate tuned); 091006's first review-cycle evidence (the due
  queue gets worked, or the aging tripwire case lands in build-17). These close
  acceptance for their filings; the build itself doesn't wait on them.
