# Write-verification attestation — harden the ops' Verify steps into a trust contract lint can consume

_Filed from the `vlt-core` vault after the 2026-07-06 vault-evolution run (gap analysis → brainstorm → six parallel pressure-tests → synthesis) traced the lint-debt loop to its root and reframed the fix: the micro-lint checks the brainstorm proposed **already exist** as prose Verify steps inside the three write ops — the real gap is that verification leaves no machine-readable trace, so lint has no trust contract with the writes and the absence of one is undetectable. One of six filings from that run; siblings referenced below by filename._

**Filing status:** the synthesis planned this filing at the M4 decision gate — after two measured lint cycles under the new contract, carrying the two-tier taxonomy plus data. It is filed **now, at the owner's request, as a design-stage proposal**: the attestation schema and the convention design are final; the two-cycle measurement data follows at M4. Treat the schema as ready to build against and the measurements as a pending attachment.

## Problem statement + evidence

The vault's quality enforcement is batch-shaped while its writes are stream-shaped. `vlt-ingest`, `vlt-extract`, and `vlt-research` emit deterministic-local defect classes (frontmatter drift, unresolved links, missing provenance, index drift) that are only *durably* caught by a periodic lint whose cost grows with both backlog and corpus. Causal-loop mapping confirmed a reinforcing loop: write rate ↑ → unlinted set ↑ → sweep cost ↑ → deferral ↑. Measured in `vlt-core` on 2026-07-06:

- **14 write ops** (9 ingest, 1 extract, 4 research) since the last lint on 2026-06-27 — 9 days of open debt.
- **4 lint entries in 183 log entries**, against 45 ingests + 13 extracts + 23 research runs.
- The wiki is at **122 pages** — past the ~30-page threshold where a full sweep needs the fan-out workflow. Full lint is now structurally expensive, permanently.
- **The Wispr deviation (2026-06-14):** an extract wrote `resources/workflow/wispr-obsidian-shortcut` from a single research note, bypassing `vlt-extract`'s wiki-only ≥2-page discipline. It was caught only because the partner self-declared `DEVIATION:` in the log — honesty, not mechanism. This is gap-analysis weakness 7: lint cannot detect a PARA file that never went through the sanctioned write path.

Five Whys bottomed out here: write-time verification *runs* (all three ops end with a Verify checklist: `vlt-ingest` Step 9, `vlt-extract` Step 8, `vlt-research` Phase 5) but **leaves no machine-readable trace**. Lint cannot know verification ran, so it re-checks everything from scratch every sweep; and nothing distinguishes an artifact that went through the op from one that bypassed it.

## The decision and its rationale

**Harden, don't add.** The pressure-test materially reframed the brainstorm idea. "Add a micro-lint to every write" would bolt a duplicate step onto ops that already have one, creating two lists that drift. Instead: refactor the existing Verify steps to execute a **shared, versioned tier-1 checklist** and write an **attestation** into the artifact's frontmatter — turning write-time verification from a ritual into telemetry. One mechanism, two payoffs: the attestation is simultaneously lint's re-scoping telemetry (skip what's attested and fresh) and the bypass detector (its *absence* on a file claiming vault provenance is the finding). The Wispr net is not a separate feature; it is the absence-case of the same field.

The tier split gets a **mechanical membership test**: checkable on one file → tier-1, amortized into the write; needs corpus knowledge (contradictions, near-dups, orphans, staleness) → tier-2, the scheduled sweep. Future checks self-classify. Plus a promotion path: a tier-2 finding class recurring ≥2 sweeps that proves deterministically checkable gets promoted into tier-1 — the sweep teaches the writes.

**Rejected alternatives** (documented in the pressure-test artifact):

- *Micro-lint as a new step beside Verify* — duplication and drift; refactor Verify to *be* tier-1.
- *Attestation as a body block* — frontmatter fields are machine-readable via Bases, invisible in reading view, greppable; a body block is none of those.
- *Structured verify in the log only* (no frontmatter) — unbounded log growth, parse fragility, and the artifact itself stays unmarked: no bypass detection at the file.
- *Deterministic shared script first* — correct end-state (LLM cost → 0 for tier-1), wrong first move: freeze the checklist in code only after two real cycles stabilize it. Slice B, on a measured trigger (rubber-stamped attestations).
- *Git pre-commit hook* — intercepts human commits in human territory; deferred behind a named tripwire (a bypass landing unflagged, or recurring despite flagging).
- *Blocking verification gate* — a headless write that trips on a fixable defect must not lose good work. Fail-open: fix what you can, flag what you can't, always complete the write.

**Threat model, stated honestly:** attestation defends against *bypass* (a write path that never read the op skill won't know to attest), not *deception* (an op lying in its own attestation — mitigated by a 1-in-5 sample-audit at each sweep, escalation = the slice-B deterministic script).

## The attestation schema (joint, collision-checked)

Two frontmatter keys on every agent-written artifact (wiki page, research note, PARA extract):

```yaml
verified_by: vlt-ingest | vlt-extract | vlt-research   # the op that ran tier-1 on this file
verified: YYYY-MM-DD                                    # date of that verification
```

- **Freshness rule:** an attestation is valid iff `verified` ≥ `last_updated`. Stale → lint quietly re-runs tier-1 on the file (not a violation). Updates re-attest: an ingest that updates an existing page bumps both keys; research attests the note it creates.
- **Scope rule (MHC / self-marker, verbatim in the convention):** attestation is a self-marker, not a quality grade. Lint flags only *unmarked cells claiming to be self* — files carrying vault frontmatter (`type: wiki|research|project|area|resource` with `author: agent|hybrid`) and no attestation — never bare human files. `daily/`, raw `sources/` deposits, and human-authored PARA files are out of jurisdiction. This exemption is load-bearing for lint-report trust.
- **Collision check against the sibling filings** (per the synthesis sequencing note: attestation + freshness + enforcement keys are designed against `_meta/conventions/frontmatter.md` *together*): disjoint from the bell filing's convention-level enforcement keys (`enforcement_stage`/`enforcement_checked_by`/`enforcement_moment`/`enforcement_counter`) and deferral schema (`deferral_metric`/`deferral_threshold`/`review_after`) in `2026-07-06-091004-no-boundary-without-a-bell.md` — flat keys, not a nested `enforcement:` map, as mandated by frontmatter.md YAML rule 3 ("no nested properties") per that filing's latent bug 1; disjoint from `2026-07-06-091003-enforcement-kit-derive-first.md`, which stores nothing (derive-first — its counters read `_agent/log.md`/`_agent/dispatch.md`, and attestation frontmatter becomes a second derivable surface, not a stored counter); orthogonal to `2026-07-06-091006-review-after-freshness-key.md`'s `review_after:` (editorial shelf-life of *content*; attestation freshness keys off `last_updated`, never `review_after`). One joint overlay pass on `frontmatter.md`, not three uncoordinated ones.

## Exact module-side changes to ship

1. **New shipped convention** — `skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md`, `version: 1`, `consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint]`. Contents: the tier-1 checklist per artifact kind (unified from the three ops' current Verify steps — they already cover ~the same set); the attestation schema + freshness rule; the fail-open rule; the MHC scope rule; the tier-membership test; the promotion path. Per `2026-07-06-091004-…`, it ships carrying its own enforcement keys (`enforcement_stage: checked`, `enforcement_checked_by: vlt-lint` — the flat form, per frontmatter.md rule 3 and 091004 latent bug 1) — the convention arrives with its bell.
2. **`skills/vlt-setup/SKILL.md`** — §2 (governance bundle) enumerates the shipped conventions by name (`_meta/conventions/{frontmatter,wiki-index,wiki-supersession,wiki-consolidation,extraction}.md`); add `write-verification`. The baseline stash (`{overlays}/.baseline/`) picks it up automatically.
3. **`skills/vlt-ingest/SKILL.md`** — refactor Step 9 (Verify) to "run tier-1 per `{conventions}/write-verification.md`, then write `verified_by`/`verified` on every page created or updated"; do not restate the checklist. Add `write-verification@1` to `depends_on` (currently `["frontmatter@2", "wiki-index@2", "wiki-consolidation@1", "wiki-supersession@1"]`).
4. **`skills/vlt-extract/SKILL.md`** — same refactor of Step 8 (Verify); `depends_on` (currently `["extraction@2", "wiki-supersession@1"]`) gains `write-verification@1`.
5. **`skills/vlt-research/SKILL.md`** — same refactor of Phase 5 (Verify); **add a `depends_on:` block — it has none today** (see Latent bugs).
6. **`skills/vlt-lint/SKILL.md`** — (a) reorganize Step 2 into *Tier 1 — structural* (re-checked only on unattested/stale files) and *Tier 2 — judgment* (the sweep), with the membership test stated; (b) three new finding keys: `para_missing_attestation` (PARA file with vault `type:` + `author: agent|hybrid`, no attestation — the Wispr net, closes gap-analysis weakness 7), `unattested_write` (agent-lane wiki/research file, vault frontmatter, no attestation — **informational, not a violation, for files predating the convention**), `attestation_stale` (`last_updated` > `verified` → quiet tier-1 re-check); (c) the re-scoping rule: attested-and-fresh files skip tier-1 re-checks, sample-audit ~1 in 5; (d) Step 5 report schema rows for the three keys under `flag_for_human`; (e) `depends_on` gains `write-verification@1`.
7. **`skills/vlt-setup/assets/workflows/vlt-lint-full.js`** — the per-page scan schema (which already carries fields like `topic_is_list`) gains the attestation fields (present / `verified_by` / fresh-vs-`last_updated`); the reducer emits the three new keys. `vlt-lint`'s convention ack covers this asset per the existing coherence-check rule.

Rollout is self-enforcing with zero new machinery: registering the four skills as `consumers:` makes the **existing convention-coherence check** (lint Step 2) flag any consumer that hasn't acked `write-verification@1` — the partial-rollout failure mode is policed by the system's current immune system.

## Upgrade/migration path for existing installs

- **Fresh installs:** `vlt-setup` §2 copies the new convention skip-if-present and stashes the baseline; nothing else needed.
- **`vlt-core` (already carrying the local v1):** the local version was minted via `vlt-mint` (convention kind, council-gated) with upgrade-ledger divergence records on the three op SKILL.md files. On the next `vlt-upgrade`: skip-if-present leaves the vault's `write-verification.md` in place; the baseline refresh stashes the shipped copy; lint's `convention_base_divergence` surfaces any local-vs-shipped delta for an explicit overlay-vs-adopt decision. The refreshed op SKILL.md files close the three divergence records — the same conveyor `vlt-track` rode at 0.4.0.
- **Existing corpus (122 pages in `vlt-core`, any N elsewhere):** no backfill. Attestation is written on next touch (op update, or lint's own tier-1 pass); until then `unattested_write` stays informational for pre-convention files (gate on `created` < convention adoption date). Only `para_missing_attestation` is a real finding from day one — the bypass class it detects was never sanctioned.

## Latent bugs surfaced

1. **`skills/vlt-research/SKILL.md` has no `depends_on:` at all**, and `frontmatter.md`'s `consumers: [vlt-ingest, vlt-lint]` omits it — yet vlt-research writes `type: research` frontmatter defined by that convention. It is invisible to the coherence check in both directions (not listed, nothing pinned): the exact defined-but-unenforced shape this whole arc attacks. Fix alongside change 5: add `frontmatter@2` (and bump `frontmatter.md`'s `consumers:`) in the same pass.
2. **Lint's scoped mode scopes by mtime**, so it cannot distinguish "changed and verified by the op" from "changed by who-knows-what" — the re-scoping rule fixes this, but note the general lesson: mtime is provenance-blind.
3. **No finding key existed for out-of-path writes** — the Wispr deviation was representable only as freeform `DEVIATION:` prose in the log; nothing structured could ever have caught the next one.

## Open design questions to decide module-wide

1. **Date-key naming:** `verified:` sits next to the `trust:` ladder's `verified` *rung* (frontmatter.md) — same word, different axis (structural verification vs claim verification). The convention text disambiguates; if the module prefers zero confusability, `verified_at:` is the alternative — decide before v1 ships, it's a one-shot schema choice (versioned, but churn is churn).
2. **Schema home:** field *definitions* in `frontmatter.md` (v3, jointly with `review_after:` per the sequencing note) with the checklist/contract in `write-verification.md` — or everything in `write-verification.md`? The joint-overlay discipline argues for the former.
3. **Does lint re-attest?** Lint Step 3 auto-fixes bump `last_updated`, staling the attestation it just validated. Proposal: lint writes `verified_by: vlt-lint` after running tier-1 on a file it touched — but that widens `verified_by`'s value set; decide whether lint is a legitimate attester.
4. **Sample-audit rate** — 1-in-5 is a guess; tune after cycle 1.
5. **Family invariant:** encode "write ops verify and attest own output" as a family invariant so future minted write-capable capabilities (and `vlt-track`'s PARA writes) inherit it via lint's existing family-invariant check — now, or after M4?

## Provenance

- Vault: `vlt-core`. Vault-evolution session 2026-07-06 — synthesis at `_agent/artifacts/vault-evolution-synthesis-2026-07-06.md` (action item 8, tagged `both`; cross-cutting sequencing notes bind this schema to the enforcement-kit and freshness-key designs), vault commit `ef2cce6`.
- Pressure-test plan (primary source, incl. rejected alternatives, decision matrix, M0–M4 milestones, risk table): `_agent/artifacts/problem-solution-2026-07-06-self-cleaning-writes.md`.
- Gap-analysis evidence: weakness 1 (lint cadence has no forcing function; 13–14 ops of live debt), weakness 7 (non-canonical extraction path — the Wispr bypass, 2026-06-14), improvement opportunity 7 (PARA provenance check as lint "Step 2c").
- Sibling filings this batch: `2026-07-06-091003-enforcement-kit-derive-first.md`, `2026-07-06-091004-no-boundary-without-a-bell.md`, `2026-07-06-091006-review-after-freshness-key.md` (shared frontmatter surface), plus `2026-07-06-091001-spec-convention.md`, `2026-07-06-091002-module-packaging-lint.md`.
