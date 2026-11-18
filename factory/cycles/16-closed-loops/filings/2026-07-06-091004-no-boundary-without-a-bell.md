# No boundary without a bell — declaration-first enforcement doctrine for every convention mint

_Filed from the `vlt-core` vault after the 2026-07-06 headless vault-evolution run traced four separate incidents to one failure shape — **defined-but-unenforced** — and a dedicated pressure-test session hardened the fix into a shippable doctrine: every boundary-creating mint declares its enforcement stage (owner, moment, counter) or carries a tripwired, expiring deferral. This filing is unconditionally ripe (no evidence gate — the evidence already happened four times). It is one of six filings landing together; it shares the `frontmatter.md` surface with `2026-07-06-091005-write-verification-attestation.md` and `2026-07-06-091006-review-after-freshness-key.md`, and its counters bind to `2026-07-06-091003-enforcement-kit-derive-first.md` when that lands._

## Problem statement + evidence

The module lets mints create boundaries — conventions, inter-partner contracts, invariants on writes, cadences — that ship as prose with **no enforcement attached**. Enforcement is structurally a separate, later act of will; deferring it is free (no tripwire, no expiry, no owner). Four instances in `vlt-core`, one shape:

1. **The personalized-extraction firewall sat checkable-but-unchecked for 4 days** — the rule shipped in `extraction.md`; the mechanical net (vlt-lint's Step 2b personalized-extraction findings) arrived only after a human happened to notice. The gap was exactly the time until someone supplied the missing moment by hand.
2. **Lint cadence has no forcing function** — `vlt-lint` says "proactively after several ingestions"; nothing counts ingests or triggers the run. The Librarian (Gwyn) hit 13 unlinted ingests since the 06-22 baseline.
3. **Dispatch failure modes #3/#4 deferred "until it bites"** — logged at the `vlt-dispatch` mint (2026-06-15) with no definition of what biting looks like and no expiry on the deferral.
4. **Staleness markers** — World Cup / NFL-draft / policy-deadline pages passed their events with no `[!stale]` convention firing, because no shelf-life rule ever declared who checks and when.

The brainstorm's Five Whys traced the root: **vault state lives in prose, so nothing can count, trigger, or trip** — and one level deeper, into the mint process itself: the mint templates have no Enforcement section, the review council has no lens that asks for one, and a deferral costs nothing. The failure lives precisely between *check exists* and *check runs at a moment someone owns*: in all four instances the rule was written and checkable. Enforcement that rides an existing moment (op final-steps, the SessionStart hook) never exhibited the gap.

## The decision and why the alternatives lost

**Ship the doctrine now, on existing surfaces; let the substrate arrive later.** The pressure-test ran three bundles through a decision matrix (prevents-recurrence / cheap-at-mint / substrate-independent / self-applying / drift-risk):

- **Full doctrine + checks-as-payload now** (machine-readable spec blocks parsed by vlt-lint) — rejected: couples the doctrine's fate to its most expensive component (the parser); if the parser stalls, everything stalls.
- **Substrate-first** (build enforcement-kit, doctrine later) — rejected: leaves the very next boundary-creating mint unprotected; it repeats the pattern while building the machine to prevent it.
- **Declaration-first** — **winner**: the declaration (stage/owner/moment) costs four frontmatter lines and needs zero unbuilt machinery; the enforcement-kit substrate upgrades declarations from `declared` to `checked/enforced` when it lands. Checks-as-payload is deferred **behind its own numeric tripwire and `review_after` expiry — the doctrine's first self-application**.

Also rejected on the way: a **"Warden" partner** owning enforcement (violates mint-verb-not-subject; re-centralizes the single-point-of-memory failure being fixed) and a **weekly "bell review" ritual** (human-memory-dependent — the original failure mode; the ledger view gives the same visibility free). Busted assumptions worth keeping: *"every boundary needs machine enforcement"* is false — a named human moment ("Librarian checks at every lint run") is a legitimate `checked` stage before any counter exists; *"the doctrine must wait for the enforcement-kit"* is false — declarations are forward-compatible slots for the substrate.

Success test: the next boundary-creating mint has **days-to-first-check = 0** (firewall baseline: 4), and zero conventions sit at `declared` without a tripwire.

## Exact module-side changes to ship

**1. Schema — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md` (`version: 2 → 3`).** Add an *Enforcement declaration* section defining, for every `_meta/conventions/*.md` file's own frontmatter:

```yaml
enforcement_stage: declared | checked | enforced
enforcement_checked_by: <owner — a partner or a skill, e.g. vlt-lint>
enforcement_moment: <the moment the check runs, e.g. lint run | op final-steps | SessionStart hook>
enforcement_counter: <derived counter, optional until enforcement-kit lands>
# deferral — ALL THREE required for any deferral; missing any field = invalid:
deferral_metric: <what is counted>
deferral_threshold: <numeric tripwire>
review_after: YYYY-MM-DD
```

**Flat keys, deliberately** — the pressure-test drafted a nested `enforcement: {…}` map, but frontmatter.md's own YAML rule 3 forbids nested properties; this filing flattens the schema to comply (see Latent bugs). Stage semantics: `declared` = rule exists in prose only; `checked` = a mechanical check exists **and** a named owner + moment; `enforced` = the check fires at a moment needing no human memory (op final-steps, hook, blocking gate). **`review_after` is a resolved date, never a duration** — semantically identical to the freshness key in `2026-07-06-091006-review-after-freshness-key.md`; define the key **once** in frontmatter@3 and let both uses (page freshness, deferral expiry) share it. Grow `consumers:` to `[vlt-ingest, vlt-lint, vlt-mint, vlt-research]` (the mint templates now encode this schema; `vlt-research` rides in per `2026-07-06-091005-…` latent bug 1 — it writes `type: research` frontmatter yet is invisible to the coherence check today, and the one coordinated frontmatter@3 bump carries the union of both filings' consumer additions). Frontmatter.md's **own** v3 frontmatter records the checks-as-payload deferral — the first self-application: `deferral_metric: prose/behavior drift lint findings + new conventions minted`, `deferral_threshold: 2 drift findings, or the 3rd new convention`, `review_after: 2026-08-17`.

**2. Backfill the five stock conventions** in `skills/vlt-setup/assets/governance/_meta/conventions/` with honest stamps: `frontmatter.md`, `wiki-index.md`, `wiki-supersession.md`, `extraction.md` are plausibly `checked` (vlt-lint carries their finding keys; `checked_by: vlt-lint`, `moment: lint run`); `wiki-consolidation.md` is the likely `declared` holdout (lint finds near-duplicates, but the consolidation discipline itself has no check) — it therefore needs a tripwired deferral, not a naked stage. Honesty note for the maintainer: `moment: lint run` is today a moment nobody owns (evidence item 2) — the lint-debt tripwire in `2026-07-06-091003-enforcement-kit-derive-first.md` is what makes that moment real; until it lands, `checked` is the ceiling.

**3. Mint templates — Enforcement section behind a boundary classifier.** All three of `skills/vlt-mint/assets/capability-template.md`, `skills/vlt-mint/assets/operation-skill-template.md`, `skills/vlt-mint/assets/partner-agent-template.md` gain an `## Enforcement` block: first the classifier question — *"does this mint create a rule someone else must obey?"* — with a one-line recorded exemption for non-boundary mints (a new recipe capability needs no bell; keep honest small mints fast); if boundary-creating, require *who checks / at what moment / against which counter*, or a complete tripwired deferral.

**4. `skills/vlt-mint/SKILL.md`** — three touches: (a) Phase 1 kind-determination asks the classifier question and records the answer in the planning doc; (b) the *Edit a convention* ceremony requires valid enforcement frontmatter on any new or base-edited convention (stamps ride the same base-edit + handshake ceremony that already exists there); (c) the Phase 2→3 exit gate adds: a boundary-creating mint cannot pass with neither a bell nor a valid deferral. Stage promotions (`declared → checked → enforced`) are dated entries in `_agent/mint/decision-log.md`.

**5. Council lens — "where's the bell?".** `skills/vlt-setup/assets/workflows/vlt-review-council.js` (the one panel engine; installed to `.claude/workflows/`): in `mode: 'mint'` for gated kinds, inject the standing question into the lens brief and give the moderator the rejection rule — a boundary-creating mint lacking the Enforcement section or carrying an incomplete deferral is a `revise`/`reject`, never a `pass`. Personas in `skills/vlt-setup/assets/governance/_meta/personas/` stay generic — the lens is a mint-mode rubric line, not a new persona (a Warden by another name).

**6. vlt-lint meta-check — the doctrine's own bell, same slice or the doctrine is instance five.** `skills/vlt-lint/SKILL.md` Step 2 gains a governance check (both modes) with `flag_for_human` report keys: `enforcement_missing` (a `{conventions}/*.md` lacking valid enforcement frontmatter), `deferral_invalid` (a deferral missing any of metric/threshold/review_after), `deferral_expired` (past `review_after`), `declared_untripwired` (`declared` stage with no deferral). Also flag a convention missing `version:`/`consumers:` entirely (see Latent bugs — today's coherence check is opt-in). Never auto-fix — stages promote through the mint ceremony, not through lint. Consumer handshake: bump `depends_on` to `frontmatter@3` in `skills/vlt-lint/SKILL.md` **and** `skills/vlt-ingest/SKILL.md` (its reconciliation will likely conclude "no edit needed" — the block applies to convention files, not wiki pages — but the ack records the verification), and add the pin to `skills/vlt-mint/SKILL.md` as a new consumer.

**7. Packaging.** Coordinate the **one** `frontmatter@3` bump across this filing, `091005` (attestation keys), and `091006` (`review_after`) — three filings, one version bump, one consumer walk; three uncoordinated bumps would churn the handshake and invite conflicting key semantics. Target the 0.6.0 release (which `2026-07-06-091002-module-packaging-lint.md` gates).

## Upgrade/migration path — planned vault-local rollout, then module absorption

**Status disclosure:** none of the vault-local state below exists yet — at filing time `vlt-core`'s `_agent/conventions/` holds only `.baseline/`, with no overlay file, no stage stamps, and no local template edits. `vlt-core` **will** ship the doctrine locally first via a `vlt-mint` convention edit; the reconciliation below applies once that mint lands, with `vlt-upgrade` merge-not-replace reconciling when the module absorbs it:

- **Schema**: the enforcement-declaration section will ride `_agent/conventions/frontmatter.overlay.md` (append-only, agent-zone — durable by construction; never touched by an upgrade).
- **Stage stamps**: stamping the five installed base conventions will be a **base frontmatter edit** — it will trip vlt-lint's `convention_base_divergence` and vlt-upgrade's Step-1 divergence snapshot until the module ships the stamps. That flag firing is not a bug; it is the designed *"this should be upstreamed"* signal, and **this filing is the upstreaming**.
- **On absorbing upgrade**: Step 2's base refresh overwrites the local stamps with the identical shipped ones (convergence, not loss); Step 3.3 refreshes `{overlays}/.baseline/`, clearing the divergence flag. The overlay's then-duplicated *Enforcement declaration* heading will trip lint's `overlay_not_append_only` at the next run — that flag is the cue to retire the local overlay section. Document this retire step in the release notes.
- **Templates**: the vault's planned local edits to the installed `.claude/skills/vlt-mint/assets/*.md` would be clobbered by any upgrade's skill refresh (no baseline net exists for skill assets — see Latent bugs). Shipping this in 0.6.0 turns that clobber into convergence; shipping a 0.6.0 *without* it would silently revert the vault's template edits once made.
- **Handshake**: ship vlt-lint/vlt-ingest pinned at `frontmatter@3`; a vault that has already bumped locally converges cleanly. Locally-set `review_after` dates (e.g. the 2026-08-17 payload deferral) will live in the decision log and the shipped v3 base — no per-vault state is lost.

## Latent bugs surfaced

1. **The plan artifact's schema violates the convention it lands in.** The pressure-test wrote `enforcement: {stage, checked_by, moment, counter}` — a nested map; frontmatter.md's YAML rule 3 ("no nested properties") forbids exactly that. Corrected to flat keys in this filing. Any future filing proposing frontmatter keys should be checked against rule 3 before build.
2. **Shipped skill assets have no divergence net.** Conventions get `{overlays}/.baseline/` + lint's base-divergence check; skill files (including the mint templates) get nothing — a local edit to `.claude/skills/vlt-mint/assets/*` is silently clobbered on upgrade with no snapshot, no flag. This doctrine's local-overlay path is the first real casualty-in-waiting. Worth its own fix (baseline or checksum for shipped skill assets in the vlt-upgrade Step-1 snapshot).
3. **The convention-coherence check is opt-in.** vlt-lint's handshake validation reads "for each `{conventions}/*.md` **carrying** a `version:` and `consumers:`" — a convention minted without those fields escapes the entire coherence machinery. The new meta-check should flag their absence, not only stale acks.

## Open design questions to decide module-wide

1. **Is `enforcement_stage` module-generic or vault-local?** Recommend generic — it describes whether shipped machinery exists, not whether a vault exercises it; a vault that builds a *local* check promotes the stage via a base edit, which correctly surfaces as upstream-bound divergence. The alternative (per-vault stage in an overlay) fragments the doctrine's one legible ledger.
2. **v1 scope**: conventions + the mint classifier only, or also family contracts (`{capabilities}/families/*.md` invariants are boundaries too) and the operating contract's own rules? Recommend conventions-first; family contracts adopt the same keys in a follow-up once the pattern proves.
3. **Overlay-path boundaries**: a vault-local overlay *addition* that creates a rule is also a boundary — does its enforcement declaration live in the overlay file's own frontmatter? Recommend yes (the classifier applies to every boundary-creating mint regardless of landing zone), but this needs a sentence in the mint ceremony.
4. **Lens placement**: rubric line in the workflow's mint-mode (recommended here) vs a persona-file question — decide once; the KIND_PANEL map ownership precedent (single-home in the workflow) argues for the workflow.
5. **`spec-convention` adoption**: per the synthesis's sequencing note, `2026-07-06-091001-spec-convention.md`'s spec schema should adopt the bell keys when both land — decide whether that is v1 of spec.md or its first version bump.

## Provenance

- Vault: `vlt-core`. Session: the 2026-07-06 headless vault-evolution run (gap analysis → brainstorm → six parallel pressure-tests → synthesis); synthesis action item 7 at `_agent/artifacts/vault-evolution-synthesis-2026-07-06.md`, vault commit `ef2cce6`.
- Pressure-test plan (authoritative design source): `_agent/artifacts/problem-solution-2026-07-06-no-boundary-without-a-bell.md` — Bundle-B decision matrix, rejected alternatives (payload-in-v1, substrate-first, Warden partner, bell-review ritual), milestones M1–M4, and the doctrine's self-application (payload deferral, `review_after: 2026-08-17`).
- Evidence: gap-analysis weaknesses 1/5/7/8 + meta-observation (in the synthesis); Five Whys root cause from `_agent/artifacts/brainstorming/brainstorm-vlt-evolution-2026-07-06/brainstorm-intent.md`; firewall arc (4 days checkable-but-unchecked, then vlt-lint Step 2b).
- Batch siblings: `2026-07-06-091001-spec-convention.md`, `2026-07-06-091002-module-packaging-lint.md`, `2026-07-06-091003-enforcement-kit-derive-first.md`, `2026-07-06-091005-write-verification-attestation.md`, `2026-07-06-091006-review-after-freshness-key.md`.
