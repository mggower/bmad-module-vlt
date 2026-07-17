---
name: vlt-lint
description: Health-check the vault wiki and fix safe structural problems. Use when the user says 'lint the vault', 'health check the wiki', 'find orphan pages', 'check for contradictions', or 'audit the notes', and proactively after several ingestions. Defaults to scoped mode (files changed since the last lint); 'full lint' / '--full' sweeps everything.
depends_on: ["frontmatter@3", "wiki-index@2", "wiki-supersession@1", "extraction@2", "write-verification@1", "spec@1"]
---

# vlt-lint

## Overview

A wiki that grows without maintenance becomes a liability — orphan pages, stale claims superseded by newer sources, contradictions accumulating unresolved. Lint is preventive care: find problems before they compound, fix the safe structural ones, flag the rest, and file merge candidates to the backlog for `vlt-ingest` to resolve. It is the Librarian's upkeep tool — run it after every 5–10 ingestions or at the start of a research push. Its report is **structured and parseable** (so a dashboard can read it), not free prose. Reads the vault only. Runs interactively or headless.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

The vault is this project — resolve paths relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). Logical names used (default, relative to the project root): `wiki` → `_agent/wiki/`, `index` → `_agent/wiki/index.md`, `research` → `_agent/research/`, `sessions` → `_agent/sessions/`, `log` → `_agent/log.md`, `backlog` → `_agent/backlog.md`, `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/` (vault-local convention overlays + the stock `.baseline/`), `partners` → `_agent/partners/` (each carries a `capabilities/` folder), `capabilities` → `_agent/capabilities/` (family contracts under `families/`). Below, `{wiki}` etc. mean the resolved path. Note the **active partner** for the log tag and backlog attribution. Before applying any fix, JIT-read `{conventions}/frontmatter.md`, `{conventions}/wiki-supersession.md`, and `{conventions}/wiki-index.md` — read each together with its `{overlays}/{name}.overlay.md` if present, honoring the overlay's appended rules (the latter governs every index check and fix below).

## Step 0: Determine scope

Pick one mode at the top of the run and announce it (with the scoping timestamp and file count, e.g. "Scoped lint — since 2026-04-19 15:00 — 7 wiki pages + 3 research notes").

**Scoped (default)** — only files changed since the last lint:

```bash
grep "^## \[.*\] lint" {log} | tail -1
```

Extract the `[YYYY-MM-DD HH:MM]` timestamp and **validate it parses as a real datetime.** If there's no prior `lint` entry, or the timestamp is missing/malformed, fall back to **full mode** and say so — there's no reliable incremental baseline. With a valid timestamp, build the candidate set by filesystem mtime (always including `{index}`, since index drift is cheap to check regardless):

```bash
find {wiki} {research} {sessions} -type f -name "*.md" -newermt "YYYY-MM-DD HH:MM"
```

**Full** — only when the user says "full lint" / "lint everything" / `--full`. Read every page in `{wiki}` (and `{research}` for deeper checks).

Below, "every wiki page" means the scoped set in scoped mode, or the whole wiki in full mode.

**Full mode at scale → the fan-out workflow.** Reading the whole wiki in one context stops scaling as it grows. When full mode would cover **more than ~30 pages**, delegate the *finding* to the `vlt-lint-full` workflow (installed at `{project-root}/.claude/workflows/vlt-lint-full.js`) instead of reading every page inline:

1. **Discover the page list** — glob `{wiki}` for `*.md` (excluding `{index}`), building `pages: [{slug, path}]` with **live absolute paths** (the agents read the live tree, not a plugin cache). Also glob `{research}` (and any agent-zone note location the wiki conventionally `[[links]]` into) for `*.md` basenames, normalized the same way page slugs are — pass these as `crossLayerSlugs` so a valid cross-layer link isn't reported as a missing target.
2. **Invoke** `workflow('vlt-lint-full', { pages, indexPath, conventionsPath, crossLayerSlugs, today })` — passing the live absolute `{index}` and `{conventions}` paths, and `today` as `'YYYY-MM-DD'` (the script has no clock; it needs it to compute `review_due`). It fans out one agent per page (budget-guarded, chunked), reduces the link graph in JS (orphans / missing targets / near-duplicates), and runs an index pass + bounded cross-page contradiction-cluster pass. It is **read-only** — it returns the structured findings (Steps 2 shape, pre-fix), never writes. The workflow tiers its models for cost — page scanners default to a cheap model, the index/cluster passes to a mid model; pass `scanModel`/`indexModel`/`clusterModel` only to override. **On resume** (`resumeFromRunId`), re-pass the full args object — the runtime delivers args fresh per run, so omitting them nulls `pages`/`crossLayerSlugs`/models.
3. **Then apply Step 3 fixes and Step 4 backlog items yourself**, serially, from the returned `fix_now` / `flag_for_human` / `opportunities` — single-writer safety lives here in the SKILL, not in the parallel finders. The workflow sweeps `{wiki}` only — the PARA attestation scan (`para_missing_attestation`), the governance checks, and the enforcement doctrine meta-check stay yours; fill those report slots from your own pass. Honor any `coverage_caps` the workflow reports (budget stop, near-dup cap, cluster cap) by surfacing them in the report — **never present a capped sweep as exhaustive.**

If the workflow isn't installed, fall back to reading inline. Small full sweeps (≤ ~30 pages) and all scoped runs stay inline — the fan-out only earns its overhead at scale.

## Step 1: Read the selected files

Read `{index}` first for the overview, then each selected page in full, noting topics, claims (and sources), outbound links, source count, and `last_updated`.

## Step 2: Checks — two tiers

The split follows the **membership test** in `{conventions}/write-verification.md` (one-file-checkable → tier 1, amortized into the writes; corpus-knowledge → tier 2, this sweep — the test and its promotion path live there, not here).

### Tier 1 — structural (one-file checks)

**Re-scoping rule:** a file whose attestation is present and fresh (`verified_at` ≥ `last_updated` — see `{conventions}/frontmatter.md`, *Write attestation*) **skips tier-1 re-checks** — the writing op already ran them; still re-run tier-1 on **≈1 in 5** attested-and-fresh files (the sample audit, per `write-verification.md`). Unattested or stale-attested files get the full tier-1 pass.

- **Missing targets** — `[[wikilinks]]` pointing at targets that don't exist anywhere. A link that resolves to a **cross-layer note** (a `{research}` or agent-zone note the wiki legitimately references) is **not** missing — only a target that resolves to nothing in the wiki *or* the cross-layer set counts. Per genuinely-missing link: create now (if there's enough to say), remove (speculative), or mark explicitly as a needed stub.
- **Frontmatter / Bases-field drift** — for every wiki page: `summary:` present and ≤160 chars; `category:` present and **exactly matching an existing `{index}` H2** (the strict binding in `{conventions}/wiki-index.md` — a `category:` that matches no H2, or a wiki page missing one, is a finding); `topic:` present and a **YAML list** (not a delimited string). A category that matches no H2 means either a typo (fix) or a page that needs a new index category (flag — a structural judgment call).
- **Attestation findings** (scope rule: `write-verification.md` — attestation is a self-marker; only *unmarked cells claiming to be self* are in jurisdiction, never bare human files) — `para_missing_attestation`: a PARA file carrying vault `type:` + `author: agent|hybrid` with no attestation (the out-of-path-write net — a real finding from day one); `unattested_write`: an agent-lane wiki/research file with no attestation — **informational, not a violation, for files whose `created` predates convention adoption**; `attestation_stale`: `last_updated` > `verified_at` → quietly re-run tier-1 on the file (not a violation).
- **`review_due`** — `review_after:` in the past → `flag_for_human` (page + date). Checked on **every** file in scope regardless of attestation (attestation is structural, expiry is content). **Never auto-fix, never nag** — the three-outcome review (bump / mark `[!stale]` / remove the key) is judgment work, and escalation of an aging queue is a tripwire concern, not lint's.

### Tier 2 — judgment and corpus (the sweep)

- **Orphan pages** — no inbound links from other wiki pages. (In scoped mode this is orphan-relative-to-scope; flag, don't exhaustively re-check the whole vault.) Fix by adding to related pages' Connections, or flag thin/redundant ones for deletion.
- **Stale claims** — judge staleness from `last_updated` (frontmatter) and file mtime, cross-checked against newer `{research}` notes / `{log}` ingests on the same topic — not by parsing prose. A page carrying `review_after:` **announces its own expiry** — the tier-1 `review_due` check covers it; no mtime inference needed there. Where a newer source should update a page, surface it.
- **`[!stale]` handling (explicit)** — surface time-bound claims (a specific date, deadline, or time-sensitive figure) that are past their shelf life and **lack** a `[!stale]` marker, and surface existing `[!stale]` markers for resolution.
- **Contradictions** — incompatible claims across two pages, self-contradictions within a page, or `{research}` findings that conflict with the wiki. Document in both pages' Contradictions/Open Questions; note which source is more recent/authoritative, but never silently pick a winner.
- **Unmarked supersessions** — claims silently updated or conflicting without a `[!superseded]`/`[!stale]` callout; consensus claims ("all sources agree") lacking individual citations or that read like training knowledge; claims missing qualifiers documented in the source. Add the appropriate callout per `{conventions}/wiki-supersession.md`.
- **Near-duplicates / drift** — pages that have drifted into overlap. Require **two coinciding signals**, not one: a shared-link signal (several shared wikilinks, *excluding* hub/entity pages everything cites) **and** a structural secondary signal (shared slug stem or title overlap). Shared links alone are co-citation noise, not duplication. Compare the *concept*, not just the slug. These are **merge candidates** — file them to the backlog (Step 4); resolution is `vlt-ingest`'s job, not lint's.
- **Thin pages** — few claims, no connections, single source; flag as merge/stub candidates for the user.
- **Index drift** — validate `{index}` against `{conventions}/wiki-index.md`: every page appears as a structural row under a sensible `##` category; the index lists no missing or nonexistent pages; the `## Stubs (linked, not yet written)` section is well-formed. The index is a **structural map** — it carries no descriptions, source counts, or dates, so do **not** check those against it (they live in frontmatter, surfaced via Bases). (Runs in both modes.)
- **Convention coherence** (governance check; both modes) — validate the convention→consumer version handshake. For each `{conventions}/*.md` carrying a `version:` and `consumers:`, read every listed consumer skill's `SKILL.md` `depends_on:` and confirm it pins that convention at the current `version` (entries are flat `name@version` scalars). **Flag** — a consumer whose `depends_on` pins an **older** version (stale ack — the convention moved and the consumer didn't follow), a listed consumer with **no** `depends_on` entry for the convention (unacknowledged), or a `consumers:` entry naming a skill that **isn't installed** (dangling). A consumer's ack covers its own workflow assets (e.g. `vlt-lint` acks for `vlt-lint-full.js`). **Never auto-fix** — see Step 3.
- **Enforcement doctrine meta-check** (governance check; both modes) — validate every `{conventions}/*.md` file's enforcement frontmatter against `{conventions}/frontmatter.md` *Enforcement declaration*. **Flag** (`flag_for_human`): `enforcement_missing` (no valid enforcement frontmatter at all), `deferral_invalid` (a deferral missing any of `deferral_metric`/`deferral_threshold`/`review_after`), `deferral_expired` (past its `review_after`), `declared_untripwired` (`enforcement_stage: declared` with no complete deferral). **Also flag** a `{conventions}/*.md` missing `version:`/`consumers:` entirely (`convention_meta_missing`) — without them the file escapes the coherence machinery above. **Never auto-fix** — stages promote through the mint ceremony only, never through lint.
- **Convention base divergence** (durability safety net; both modes) — a shipped base convention must stay **pristine** so upgrades can refresh it; local additions belong in an overlay (`{overlays}/{name}.overlay.md`), never in the base. For each `{conventions}/{name}.md` with a stock baseline at `{overlays}/.baseline/{name}.md`, compare the two: if the base **differs from its baseline**, the base was hand-edited locally — **flag** it (`convention_base_divergence`) as needing to be lifted into the overlay or upstreamed to the module (the change is generic if it alters a rule rather than adds one). If no baseline exists for a base file, **flag** it once as `baseline_missing` (the upgrade path can't classify hand-edits without it). **Never auto-fix** — a human decides overlay-vs-upstream. *(This is the lint-time half of the detect-and-report safety net; `vlt-upgrade`'s pre-flight is the upgrade-time half.)*
- **Overlay append-only** (governance check; both modes) — an overlay may only *add*. For each `{overlays}/{name}.overlay.md`, flag (`overlay_not_append_only`) a section heading that duplicates a base heading verbatim (a likely attempt to *replace* a base rule rather than extend it) and any overlay whose `{name}` has no corresponding base convention (`overlay_orphan`). **Never auto-fix** — flag for a human. *(Property: `depends_on` pins are flat base-only `name@version` scalars — see the coherence check above — and overlays are **deliberately unversioned** vault-local additions carrying no handshake axis; an overlay addition is invisible to the version handshake by design, a local extension rather than a consumer-facing rule change.)*
- **Capability lane-safety** (governance check; both modes) — for each capability file under `{partners}/*/capabilities/*.md`, validate the lane firewall (see the contract's *Capabilities*): a **light** capability (`weight: light` / `write_scope: own-zone`) whose **body describes a write to a *synthesized, single-writer* lane (the wiki), another partner's zone, or a modification of an *existing* `sources/` file** is a lane violation (`capability_lane_violation`) — a **new-file deposit into `sources/`** (the raw-input tray; no single-writer owner) is permitted and is *neither* a lane violation *nor* a scope mismatch (definition: the contract's *Capabilities*); a capability whose declared `write_scope` doesn't otherwise match what its body actually writes is `capability_scope_mismatch`; a `weight:`/`council_class:` not consistent with `write_scope` (own-zone must be light+none; a shared lane must be heavy) is `capability_weight_mismatch`. **Heavy** capabilities should carry a `procedure: { skill: vlt-* }` pointer to an installed op skill — a dangling pointer is `capability_skill_missing`.
- **Family-invariant conformance** (governance check; both modes) — for each `{capabilities}/families/{family}.md`, read its `## Invariants` and its `instances:`; for every instance partner, confirm a capability declaring `family: { name: {family} }` exists and that its body honors each invariant (e.g. an `own-zone-only` invariant with a body that writes a shared lane is a violation). **Flag** (`family_invariant_violation`) an instance that breaches an invariant, and (`family_instance_missing`) a listed instance with no matching capability file. **Never auto-fix** — these are the propagation/coherence guard; a human reconciles the body or the contract.
- **Personalized-extraction firewall** (governance check; both modes) — the personalized-extraction widening (`{conventions}/extraction.md`) lets a domain deliverable additionally read the partner's agent-zone state via a separate `personalization_sources:` field, but the hard invariant holds: **every method/general claim must still trace to a wiki page in `sources:`**, and `personalization_sources:` carries **state, never method**. For each extracted artifact carrying `personalization_sources:`, **flag** (a) `method_not_in_sources` — a body claim that reads as general method/knowledge but is **not** covered by any page in its `sources:` (it leaked in via personalization), and (b) `method_in_personalization` — a `personalization_sources:` entry (or operational-log file it points at) that carries general/method knowledge rather than the user's operational state. **Never auto-fix** — flag for the partner to re-ground the claim in the wiki or move it. *(This is the enforcement the widening's prose + verify-checkbox deferred; lint is the net.)*
- **Spec candidates** (governance check; both modes) — surface handoff docs that have outgrown the handoff class. For each doc in `_agent/handoffs/` that is **revised in place** (carries a "What changed" section) **or** has **≥2 relay entries in `_agent/dispatch.md` pointing at the same path**, flag it (`spec_candidate`) as a possible `{specs}` contract per `{conventions}/spec.md` — the same signals the proto-spec retrofit (`vlt-upgrade`, *Proto-spec retrofit* — the human-gated offer) surfaces at upgrade time, surfaced here at lint cadence. Derive the count from handoff file state + dispatch relay entries; **no stored counter**. **Never auto-promote** — spec-vs-handoff is a judgment call, so file to the backlog / flag for the human, exactly as merge candidates and `review_due` are surfaced (routing back to the owning partner is not lint's job). An empty `_agent/handoffs/` yields no findings; **the check never alarms on the absence of specs** — it surfaces candidates that exist, never zero-specs.
- **High-value gaps** (full mode only) — concepts referenced across many pages without their own page; candidates for new pages.

## Step 3: Auto-fix the safe issues

Fix directly (bump `last_updated` on any page you substantively edit — e.g. adding a callout; skip the bump for trivial formatting):

- **Index drift** — add missing pages (structural row + right category per `{conventions}/wiki-index.md`), remove non-existent ones, move resolved stubs out of `## Stubs`; set the index `last_updated`. Do **not** add or "correct" source counts/dates — the index doesn't carry them.
- **Frontmatter / Bases-field drift** — a `category:` with a clear typo for an existing H2 → repoint it. A `topic:` still in old delimited-string form (`a / b` or `a, b`) → convert to a YAML list (general→specific, lowercase). A missing `summary:` on a page with enough to summarize → draft one ≤160 chars. **Flag, don't mutate:** a `category:` that fits no existing H2 (needs a structural index decision) → `flag_for_human`.
- **Broken wikilinks** — repoint renamed targets; remove links to targets that clearly won't exist.
- **Formatting** — standardize frontmatter and required sections.
- **Unmarked supersession/stale callouts** — add them per the convention.

**Attest what you touched (lint-as-attester, narrowly):** on every file this step's auto-fix substantively edited, re-run tier-1 and write `verified_by: vlt-lint` + `verified_at: <today>` — the auto-fix bumped `last_updated` and would otherwise re-stale the attestation just validated. Never attest a file you merely read (contract: `{conventions}/write-verification.md`).

Do **not** auto-apply: page deletions (flag), contradiction resolutions (document both, flag), page merges (file to backlog — see Step 4), or **convention-coherence drift** (flag — a stale `depends_on` ack must be cleared by a human reconciling the consumer against the convention and then bumping the ack; lint must never bump the integer itself, or it would rubber-stamp conformance it didn't verify).

## Step 4: File maintenance backlog items

For each near-duplicate/merge candidate (and any other maintenance worth doing later), append a `maintenance` item to `{backlog}` under `## Open`, then **mention it in-flow** (capture is cheap and never silent):

```
- [ ] Merge <page-a> + <page-b> (maintenance, by: <partner>) — near-duplicate: <signal, e.g. slug stem + 4 shared wikilinks>
```

The merge itself is resolved later by `vlt-ingest` under the consolidation discipline — lint finds, ingest resolves.

## Step 5: Emit the structured report

Produce a parseable report (stable keys, so a dashboard can consume it), opening with the mode/scope line. Use a fenced block:

```yaml
mode: scoped            # scoped | full
scope_since: 2026-04-19 15:00    # or: full
files_checked: 10       # pages an agent/this run actually SCANNED (not merely listed/globbed)
files_listed: 10        # pages discovered in scope (full mode via the workflow reports both — files_checked < files_listed signals a coverage cap)
fix_now:
  orphans: [<page>, ...]
  missing_targets: [<page → target>, ...]
  index_drift: [<what was fixed>, ...]
  frontmatter_drift: [<page: summary missing/over-length | topic string→list | category typo repointed>, ...]
  unmarked_supersessions_fixed: [<page: claim>, ...]
  sources_vs_prose_mismatches: [<page: frontmatter sources: vs prose Sources diverge>, ...]
flag_for_human:
  category_no_match: [<page: category 'X' matches no index H2 — needs a category decision>, ...]
  convention_drift: [<convention@version → consumer acks @N (stale) | <consumer> unacknowledged | <consumer> dangling/not-installed>, ...]
  enforcement_missing: [<convention: no valid enforcement frontmatter>, ...]
  deferral_invalid: [<convention: deferral missing metric | threshold | review_after>, ...]
  deferral_expired: [<convention: deferral past review_after YYYY-MM-DD>, ...]
  declared_untripwired: [<convention: stage declared, no complete deferral>, ...]
  convention_meta_missing: [<convention: missing version: and/or consumers:>, ...]
  para_missing_attestation: [<para-file: vault type + author agent|hybrid, no attestation>, ...]
  unattested_write: [<page (created YYYY-MM-DD) — informational where created predates convention adoption>, ...]
  attestation_stale: [<page: last_updated > verified_at — quiet tier-1 re-run>, ...]
  review_due: [<page — review_after YYYY-MM-DD past>, ...]
  convention_base_divergence: [<convention: base differs from .baseline — lift to overlay or upstream | baseline_missing>, ...]
  overlay_issues: [<overlay: duplicates base heading 'X' (not append-only) | overlay_orphan (no base convention)>, ...]
  capability_issues: [<partner/slug: lane_violation (light cap writes a shared lane) | scope_mismatch (write_scope ≠ actual writes) | weight_mismatch | skill_missing (dangling heavy pointer)>, ...]
  family_issues: [<family: invariant_violation (instance breaches X) | instance_missing (listed instance has no capability)>, ...]
  personalized_extraction_issues: [<artifact: method_not_in_sources (general claim not traced to wiki sources:) | method_in_personalization (personalization_sources carries method, not state)>, ...]
  stale: [<page — reason>, ...]
  contradictions: [<page-a vs page-b: claim>, ...]          # unhandled — no callout yet
  contradictions_handled: [<page-a vs page-b: claim>, ...]  # already documented — surfaced, not vanished (a managed disagreement is a feature)
  thin_pages: [<page>, ...]
opportunities:
  high_value_gaps: [<concept>, ...]     # full mode
  near_duplicates: [<page-a + page-b (signal)>, ...]
  source_gaps: [<topic — source type that would help>, ...]
fixes_applied: [<summary>, ...]
backlog_filed: [<merge item>, ...]
coverage_caps: [<what was NOT exhaustively checked — budget stop / near-dup cap / cluster cap>, ...]   # full-mode workflow only; empty when the sweep was exhaustive
```

**`files_checked` counting rule (Gap B):** count a page as *checked* only if it was actually read/scanned this run — distinct from `files_listed` (discovered in scope). When the fan-out workflow hits a budget or coverage cap, `files_checked < files_listed` and `coverage_caps` names what was skipped — **surface that; never report a capped sweep as exhaustive.** For a large full-mode sweep, you may additionally offer an HTML rendering if the host has a renderer — otherwise skip it.

## Step 6: Append to the log

Append a partner-tagged entry to `{log}`:

```
## [YYYY-MM-DD HH:MM] lint (<partner>) | <mode> — checked N files — orphans: X, contradictions: Y, gaps: Z, fixes: <summary>, backlog: M filed
```

`<mode>` is `scoped since <timestamp>` or `full`. Write **no** session note — the summoning partner owns the session log (operating contract § session-ownership).

## Tips

- **Contradictions are features, not bugs** — a well-documented disagreement beats false certainty. Say so loudly, don't quietly pick one.
- **Suggest sources, not just fixes** — the best lint output is often a list of specific source types that would fill a gap.
- **Don't over-clean** — fix the clear-cut structural issues, flag the content decisions, and leave the judgment calls to the human.
- **Trust scoped mode** — full-vault linting gets expensive as the wiki grows; trust the scoping unless there's a reason to distrust `{log}`.
