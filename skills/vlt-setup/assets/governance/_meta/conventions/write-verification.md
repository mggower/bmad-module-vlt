---
type: note
created: 2026-07-06
last_updated: 2026-07-06
title: Write-Verification Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 1
consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
---

# Write-Verification Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/write-verification.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

This file is the **write-side trust contract**: every agent write operation finishes by running the **tier-1 checklist** below on each artifact it created or updated, then writing the **attestation** (fields defined in `frontmatter.md`, *Write attestation*) into that artifact's frontmatter. One mechanism, two payoffs: the attestation is simultaneously `vlt-lint`'s re-scoping telemetry (skip what's attested and fresh) and the bypass detector (its *absence* on a file claiming vault provenance is the finding).

## The tier-1 checklist

Tier-1 = checks answerable from the one file being written, amortized into the write. This section is the checklist's **single home** — the op skills point here and never restate it.

**Every artifact (wiki page, research note, PARA extract):**

- [ ] Frontmatter complete and correct per `frontmatter.md` for its type — and **no stray `key:` field**
- [ ] Every `[[wikilink]]` resolves to an existing page or is explicitly flagged (a new stub, or a deliberately-missing target)
- [ ] Every non-trivial claim is traceable to a source (inline citation or the `sources:` list)
- [ ] `sources:` lists **every** contributing source (every source that fed a wiki page; every URL consulted for a research note; every wiki page cited in a PARA extract)
- [ ] The `{log}` entry was appended, is partner-tagged, and points at the right artifacts (where the op logs)

**Per artifact kind, additionally:**

- **Wiki page:** `summary:` present and ≤160 chars; `category:` matches an existing `{index}` H2; `topic:` is a YAML list; `review_after` present **iff** the content is time-sensitive — and a resolved date, not a duration.
- **Research note:** the Executive Summary is dense and specific; every URL consulted appears in **both** `sources:` and the prose Sources section.
- **PARA extract:** every wiki page referenced in the body appears in `sources:`; it reads as one shaped deliverable, not stitched wiki excerpts.

## Attestation

The fields (`verified_by`, `verified_at`) and the freshness rule (valid iff `verified_at` ≥ `last_updated`; stale → quiet tier-1 re-run, not a violation) are defined in `frontmatter.md` — referenced here, not redefined. This file owns the contract around them:

- After tier-1 completes, write `verified_by: <this op>` and `verified_at: <today>` on **every artifact created or updated**. Updates re-attest — an op that updates an existing page bumps both keys.
- **`verified_by` value set:** the three write ops (`vlt-ingest`, `vlt-extract`, `vlt-research`) plus `vlt-lint` — and lint attests **narrowly**: it writes the pair only on files its own auto-fix touched (an auto-fix bumps `last_updated` and would otherwise re-stale the attestation it just validated). Lint never attests a file it merely read.

## Fail-open rule

A write never blocks on its own verification: **fix what you can, flag what you can't, always complete the write.** A headless write that trips on a fixable defect must not lose good work. Unresolved gaps go in the op's closing report (and `{backlog}` where they warrant follow-up), never into a refusal to write.

## Scope rule (self-marker)

Attestation is a **self-marker, not a quality grade**. Lint flags only *unmarked cells claiming to be self* — files carrying vault frontmatter (`type: wiki|research|project|area|resource` with `author: agent|hybrid`) and no attestation — never bare human files. `daily/`, raw `sources/` deposits, and human-authored PARA files are out of jurisdiction. This exemption is load-bearing for lint-report trust.

## Tier membership and promotion

- **Membership test (mechanical, so future checks self-classify):** checkable on one file → **tier-1**, amortized into the write; needs corpus knowledge (contradictions, near-duplicates, orphans, staleness) → **tier-2**, the scheduled sweep (`vlt-lint`).
- **Promotion path:** a tier-2 finding class that recurs across ≥2 sweeps and proves deterministically checkable on one file gets promoted into tier-1 — the sweep teaches the writes.

## Sample audit

At each sweep, lint re-runs tier-1 on **≈1 in 5** attested-and-fresh files anyway (a stated default — tune on evidence after the first cycle). Threat model, stated honestly: attestation defends against *bypass* (a write path that never read the op skill won't know to attest), not *deception* (an op mis-reporting its own attestation) — the sample audit is the mitigation for the latter.

## Reading list

- `frontmatter.md` — the attestation field definitions + freshness rule, and the schemas tier-1 validates
- `wiki-supersession.md` — the callout discipline several tier-1 items check for
- `vault-operating-contract.md` — the `{log}` format the log-entry check validates against
