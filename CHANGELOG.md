# Changelog

Notable changes to the `vlt` module, one section per released version, newest first.

The record begins at `v0.4.0`; earlier tags predate the per-build commit history these entries
are derived from.

## v0.18.0 — 2026-09-02

**Cycle 15** — nothing reads it back. One release for the whole cycle: builds 1 through 7.

- **Build 1 — a `supersession` kind on the feedback rail:** a vault owner filing a retirement gets an issue that says it is one — findable by the `field:supersession` label, routed by its own issue form, and checked by triage against the body's two mandatory halves (`superseded_rule` / `superseding_mechanism`) — instead of a candidate whose real class survives only in a note nothing machine-readable can read. Additive only: the three existing kinds keep their meaning, the field contract's `rail_contract` does not bump, and `vlt-feedback` refuses to compose a supersession missing either half.
- **Build 2 — what the instrument costs to run:** a vault owner who re-runs `vlt-lint --full` — after an upgrade, or because a finding looks wrong — pays for what actually changed instead of for everything, and can force a re-derivation (`lint-cache.py evict --slug <slug>`, or `re-scan <slug>` on the skill) instead of being served the same suspect answer. The cache key is now **facts, not verdicts**: the page's bytes, the extractor model (`scanModel`), the scan surface, and the digests of the three scanner-read conventions (`SCANNER_CONVENTIONS`, one home) — `module_version` is no longer a key term, so a release that moves none of those leaves the cache warm. A cold run names the term that moved (`cache_miss_terms`; the `lint_cache:` line's cold reason), and `evicted E by request` is reported on every run.
- **Build 3 — the denominated slots:** a vault owner reading a lint report sees each derived slot with the population it came from — `stub_discovery: section located: yes ("## Stubs (linked, not yet written)"); N slugs across 1 index`; `governance_memory:` as E log entries counted by an unwrapped instrument, S schema-keyed, X unclassifiable, N uncounted — and a slot that arrived with the wrong type (`stubSlugs`, `rulesetComponents`, a digest) is refused before the scan phase dispatches, as a failed run with a directed `next:`, rather than coerced and rendered as an absence. Field consequence: a vault whose index still carries a bare `## Stubs` heading will render `stub_discovery: section located: no` on its first post-upgrade sweep — the honest reading; the fix is the index heading (`wiki-index.md`).
- **Build 4 — the scanner's returns:** a vault owner stops being sent to fix pages that are not broken — no orphan that has an inbound link, no missing target that exists, no over-length summary that is inside the limit. The link graph and summary lengths are **byte-derived** by a shipped script (`skills/vlt-lint/scripts/lint-page-facts.py`, code fences and spans stripped, anchors dropped, `summary:` measured in characters) and passed to the workflow as `pageLinks` / `summaryLengths`; the page scanner is no longer asked for `outbound_links` and is told that length is never a frontmatter defect (`PAGE_SCAN` 3676 → 3265). A scanner-returned callout target that fails read-back against the page's own links is rejected, reported on the new `scanner_return_rejected:` line, and never cached. The orphan and missing-target slots are byte-derived for the first time on the first sweep after this release.
- **Build 5 — the persisted report:** a vault owner can read every persisted lint report, and each slot `report.md` mandates per-file carries one entry per file — or the run fails loudly, writing a dated `…-lint-failed.yaml` record, instead of a report that quietly isn't one. Persisting is a three-move ritual (scratch → `skills/vlt-lint/scripts/lint-report-check.py` → `mv`); the schema the gate enforces is `report.md`'s own fence, never a second list (presence + type + cardinality, never closure — extra keys never fail a report); per-file populations come from an independent walker (`skills/vlt-lint/scripts/lint-para-facts.py`), never from the value's producer. `false_positives_refused:` is promoted to a mandated slot; `.json` reports are validated under bare `python3` with no YAML library. Reports persisted before this release are not rewritten.
- **Build 6 — retire the PARA `type:` prohibition:** a vault owner who types a file accurately is no longer told to retype or move it — the declared `type:` is judged on whether it is recognized vocabulary, the module's or the vault's declared, rather than on which folder the file sits in, and `{wiki}` stops being a named exception to that. The rule change is item 1 below.
- **Build 7 — retire the `verified_by` roster closure:** a partner's attestation is authorized once — by the container's `writers:` list where one is declared — instead of twice, by a roster that cannot admit a partner. The rule change is item 2 below; undeclared containers are now counted on the new `para_writer_scan:` report line.

**Governance rule changes crossing v0.18.0 — read these before writing.**

1. **`{conventions}/extraction.md` v9 → v10 — the PARA `type:` prohibition is RETIRED.** A file at a PARA address is judged on whether its `type:` is **recognized vocabulary — the module's or the vault's declared** — never on which folder it sits in. The recognized set is the union of the PARA artifact types, the operational-record class (`charter | record | register`), vault-declared overlay schema, and every value `frontmatter.md`'s canonical list names. **What a partner may now do differently:** file an honestly typed document (`type: research` for a dated `trust: raw` snapshot, for one) at a PARA address without retyping it to the folder's noun or relocating it; the instruction *"never declare module vocabulary as vault-grown overlay schema"* is gone because there is nothing left for it to forbid. `vlt-lint`'s `para_type_unknown` is **not** retired — a value declared nowhere still lands loud; its legal response no longer contains *retype or relocate* for an accurate value. **`{wiki}` stops being a named exception to the type judgment** — `type: wiki` is recognized vocabulary like any other; the `{wiki}` subtree's removal from the PARA population is a zone fact (Layer 2, Librarian-only) and is unchanged. **This retires the rule v0.17.0 item 2 introduced** (*"a closed, named set"*), which was reinforced in the very cycle whose thesis was that rules without enforcement points do not bind. The operating contract's Layer-3 entry condition and the derived rule card say *recognized* where they said *closed*. Four consumer acknowledgments re-pinned (`extraction@10` × 4 — `vlt-extract`, `vlt-lint`, `vlt-track`, `vlt-query`).
2. **`{conventions}/write-verification.md` v5 → v6 — the `verified_by` roster closure is RETIRED.** `verified_by:` is no longer limited to a roster of write-op skills; its value set is **whatever the nearest declaring container's `writers:` join admits — unconstrained where none declares** — and `vlt-lint`'s `para_writer_unauthorized` answers the authorization question **once**: where a file carries `verified_by:`, that attester is the writer of record and must itself be admitted (`agent` admits every agent-kind identity; a named slug only itself; the `author:` leg no longer carries it); undeclared containers still pass `open` and are now **counted** on the new `para_writer_scan:` report line. **What a partner may now do differently:** attest a Layer-3 knowledge artifact it wrote in a sitting with its **own slug** — the tier-1 pass it already runs can finally be recorded. The attestation pair stays **required**; `para_missing_attestation` keeps its job. A container declaring only `[human]` now refuses every attested file (no partner drafts there) — ratify a `writers:` line to admit one. Five consumer acknowledgments re-pinned (`write-verification@6` × 5 — `vlt-ingest`, `vlt-extract`, `vlt-research`, `vlt-lint`, and the lint workflow's header, plus its four in-prose pins); the operating contract's resolver sentence moves one clause and the rule card is re-derived.
3. **`{conventions}/frontmatter.md` stays at v14 — no rule of its own moved, no re-acks owed.** Its prose is re-nouned to match both retirements (the recognized-vocabulary clause under item 1; the `verified_by` field definitions and `local_consumers:` (c) under item 2 — a registration now grants a handshake seat and nothing about attestation). Its bytes moved, which matters for the cache (below), not for the handshake.

Every consumer acknowledgment of both moved conventions was **re-pinned in the same build** (9 acks — `extraction@10` 4, `write-verification@6` 5, the last including the `vlt-lint-full.js` header and its four body pins under the `E7` release-gate check), and the bipartite handshake check passes in both directions at release time — 9 conventions, 39 consumer pins, consistent.

**Field notice — vault-minted registrants on `write-verification`.** A vault carrying `local_consumers:` registrants on `write-verification` (a vault-minted write op acking `@5`) will see **one expected `convention_drift`** finding per registrant on its next lint until the registrant is reconciled by ceremony (`vlt-mint`, convention edit) — the module cannot re-ack a vault-minted op. This is expected and is not a module defect.

**Parked interims this release unblocks.** `parked_interims_review:` will render **park #15** (the agent-lane `type:` park — item 1) and **park #16** (the attestation-roster park — item 2) on the first v0.18.0 upgrade. Both recorded blockers are false at rest against the shipped conventions: under item 1 the two conventions give one answer and `type: research` is recognized, so files typed that way stop firing `para_type_unknown` with **no vault act**; under item 2 the closure a partner could not satisfy no longer exists. The unwind of each is the owner's superseding decision-log entry citing v0.18.0 — **a re-park is not an unwind.**

**The first full lint after this release is COLD BY CONSTRUCTION — three movers.** Build 4 moved the scan surface (the page-scan prompt and its `PAGE_SCAN` schema — the scanner is no longer asked for links and is told length is not its verdict); build 6 moved `frontmatter.md`'s bytes (a scanner-read convention); build 7 moved `write-verification.md`'s bytes and the scan prompt's `@6` version literal. Every existing sidecar record is therefore unreusable, and `lint_cache:` will honestly report `cached 0` and name the moved terms. This is **expected and is not a cache regression**. **It is also the last such statement.** From v0.18.0 the key is facts-not-verdicts: a release that moves no scanner-read convention, no scan surface and no extractor leaves the cache warm, so this paragraph is no longer a template — it appears only when a release actually moves one of those inputs, and names which.

**Changed paths:** `.claude-plugin/marketplace.json`, `.github/ISSUE_TEMPLATE`, `skills/vlt-extract`, `skills/vlt-feedback`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-query`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`

## v0.17.1 — 2026-08-27

**Cycle 14** — no enforcement point. A hot-fix patch: build 5, repairing a contradiction shipped in v0.17.0 earlier the same day.

- **Build 5 — the operational-record class has one membership:** `extraction.md` v8 named the Layer-3 operational-record class twice with **different members**, and the attestation exemption followed the narrower one. A `charter` file was simultaneously a recognized PARA `type:` and outside the class that recognition places it in. Six sites across four files are brought into agreement, and the class's defining property is restated so `charter` is a member on its own terms rather than forced into a predicate (*append-shaped*) it does not satisfy.

**Governance rule changes crossing v0.17.1 — read these before writing.**

1. **The Layer-3 operational-record class is `charter | record | register` — all three.** This is the membership `{conventions}/extraction.md` already stated at its recognized-`type:` set and at its attestation posture; the class's own definition site and the attestation exemption named only two of the three. The class is now stated identically at every site that enumerates it.
2. **A `charter` file is exempt from attestation jurisdiction.** `{conventions}/write-verification.md` **v4 → v5** — the *Scope rule* exemption now covers `type: charter` alongside `type: record` and `type: register`. A partner may now legally leave a `charter` unattested where yesterday it could not, and `vlt-lint` no longer reports one under `para_missing_attestation`. **This corrects a contradiction shipped in v0.17.0**: v0.17.0 introduced the class exemption with the wrong membership, so the one artifact class most likely to be human-ratified rather than agent-attested stayed in jurisdiction.
3. **`{conventions}/extraction.md` v8 → v9** — the class's definition site carries the corrected membership. Ruled a rule change rather than a prose correction because that line is the convention's appointed home for the answer (*"cited there, defined here"*) and the correction moves a shipped check's population.

Every consumer acknowledgment of both moved conventions was **re-pinned in the same build** (9 acks — `write-verification@5` 5, `extraction@9` 4), and the bipartite handshake check passes in both directions at release time — 9 conventions, 39 consumer pins, consistent. `{conventions}/frontmatter.md` **stays at v14 — no movement**: it already named all three members correctly and carries no edit in this release. One in-prose version citation inside `vlt-lint-full.js` was re-stated to match, caught by the `E7` release-gate check added in v0.17.0 — its first real catch.

`vault-operating-contract.md`'s Layer-3 entry condition also named the class with two members. It was **not** in the field filing and was found only by the membership-agreement check this build introduces — the check compares *members* across every enumerating site, where the v0.17.0 check compared only *how many sites define the class* and so could not see a membership disagreement at all.

**The first full lint after this release is COLD BY CONSTRUCTION.** Both moved conventions' digests feed the ruleset fingerprint, so every existing sidecar record is unreusable and `lint_cache:` will honestly report `cached 0`. This is **expected and is not a cache regression**. Note this is the **third forced cold sweep today** — v0.16.2 caused the first and v0.17.0 the second.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-query`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`

## v0.17.0 — 2026-08-27

**Cycle 14** — no enforcement point. Release 2 of the cycle: builds 2, 3 and 4.

- **Build 2 — the findings cache: write-ready records, an in-workflow composed key, and an executable sidecar writer:** the cache shipped two releases ago and has never once worked. The page scanner now returns write-ready records, the cache key is composed inside the workflow rather than assumed, and the sidecar is written by a real shipped script (`skills/vlt-lint/scripts/lint-cache.py`) instead of by prose instruction.
- **Build 3 — governance: the PARA type vocabulary gets a named owner, the attestation roster gets a class it can honestly exempt, and the handshake gets an enforcement point that can see prose:** three conventions move rules, nineteen consumer acknowledgments are re-pinned in the same build, and the version-handshake gains a release-gate check (E7) so a stale ack cannot reach a tag.
- **Build 4 — lint references: a destructive fix direction gets routed by the scanner, and the report persist gets the parse check it has always asserted:** the `sources_vs_prose` fix direction is routed by the scanner rather than left to the reader, and a persisted lint report is now parse-checked against the claim the contract makes about it.

**Governance rule changes crossing v0.17.0 — read these before writing.**

1. **`{conventions}/write-verification.md` v3 → v4** — the **Layer-3 operational-record class is exempt from attestation jurisdiction**. Attestation no longer claims jurisdiction over records the vault writes about its own operation; the exemption is a named class, cited to `extraction.md`, not a case-by-case judgement. A partner may now write an operational record that would previously have been refused or reported as unattested.
2. **`{conventions}/extraction.md` v7 → v8** — the PARA recognized **`type:` vocabulary is now a closed, named set**. The vocabulary has an owner and an enumeration; a `type:` outside the set is no longer silently tolerated. Re-derive any local rule or overlay that assumed the `type:` space was open.
3. **`{conventions}/frontmatter.md` v13 → v14** — re-pinned in coordination with the two rule changes above; consumers re-acknowledge in the same build.

Every consumer acknowledgment of the three moved conventions was **re-pinned in the same build** (**19 acks** across 11 shipped files — `write-verification@4` 5, `frontmatter@14` 10, `extraction@8` 4), and the bipartite handshake check passes in both directions at release time — 9 conventions, 39 consumer pins, consistent. A further **8 in-prose version citations** inside `vlt-lint-full.js` were re-stated to match; these are recitations, not acknowledgments, and are newly guarded by the `E7` release-gate check this version adds — before it, nothing could see them.

**The findings cache sidecar moves from `_agent/lint-cache.yaml` to `_agent/lint-cache.json`**, and is now written by a shipped script (`skills/vlt-lint/scripts/lint-cache.py`) rather than by prose instruction. The legacy `.yaml` file is **deleted automatically on first run**. There is **no migration** — prior records were unusable by construction.

**The first full lint after this release is COLD BY CONSTRUCTION.** Three separate fingerprint movers cross release 2: build 2 rewrites the record shape, build 3 moves two convention digests, and build 4 moves `checks.md`'s. Every existing sidecar record is therefore unreusable and `lint_cache:` will honestly report `cached 0`. This is **expected and is not a cache regression**. Note this is the **second forced cold sweep today** — v0.16.2 caused the first.

**Persisted lint reports may now be `.json` as well as `.yaml`** (`.yaml` remains the default).

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-groom`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-query`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `tools/package-lint.py`, `tools/test-package-lint.py`


**Auto-fix placement, stated where it was missing.** `references/fix-and-file.md` Step 3 now requires a `sources_vs_prose` entry to be added **as a member of the existing `sources:` list** — never a top-level key or a loose item outside it — and to **re-parse the frontmatter after the edit**, on the rule that a page whose frontmatter no longer parses is a defect the fixer caused, not a finding it cleared. Field-driven: a 2026-08-27 full sweep found 8 pages carrying orphaned frontmatter items written outside `sources:` by the previous sweep's own Step-3 fix, **5 of them unparseable**. The class had no written procedure, so the fixer improvised — the harm this version's `sources_vs_prose` routing exists to end.

## v0.16.2 — 2026-08-27

**Cycle 14** — no enforcement point. Release 1 of the cycle: build 1 alone, a repair patch.

- **Build 1 — a structured frontmatter verdict and an entity-decoded category seam:** the reduce-side guard shipped in v0.16.1 was defeated by a scanner that cited the rule it was applying, so the guard is replaced rather than patched. The page scanner now returns a **structured `PAGE_SCAN` frontmatter verdict** — a `frontmatter_defect` enum plus `frontmatter_defect_fields` / `frontmatter_defect_detail` — in place of the free-text `frontmatter_valid` / `frontmatter_issue` claim the reduce had to parse. The **reduce-side residue rule and the free-text claim parser are both retired**: the reduce reads the enum, so there is nothing left to defeat by wording. The category comparison seam is **entity-decoded**, so an HTML-escaped scanner return no longer fails an exact comparison.

**No governance rule changes cross v0.16.2** — no convention `version:` moves, no consumer re-acks owed.

**The first full lint after this upgrade is COLD BY CONSTRUCTION.** Both halves of `canonicalScan` are rewritten, so every record in an existing `_agent/lint-cache.yaml` is unreusable and the run recomputes from scratch. This is expected and is **not** a cache regression — the `lint_cache:` line will honestly report `cached 0`. The following full run caches normally again.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-lint`, `skills/vlt-setup`

## v0.16.1 — 2026-08-26

**Cycle 13** — trusted returns. A single-build patch.

- **Build 1 — reduce-side guards:** the full-lint reduce stops taking the page scanner's `frontmatter_valid` / `frontmatter_issue` claim on faith. An issue naming only the attestation pair, or only a claimed-missing *optional* field, is refused entry to `malformed_frontmatter` and `unmarked_supersessions` — both exclusions are conjunctions, so a page that is genuinely malformed **and** unattested still reports, and a claim the reduce cannot positively identify always reports. The attestation fact is not lost: it was already reported through `unattested_write` and `attestation_census`, computed independently from the same returned values, so what the guard removes is a duplicate. `malformed_frontmatter` also gains the check definition, exclusions and legal response it never had (`vlt-lint/references/checks.md`) and a documented report slot (`references/report.md`).

**No governance rule changes cross v0.16.1** — no convention `version:` moves, no consumer re-acks owed.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-lint`, `skills/vlt-setup`

## v0.16.0 — 2026-08-25

**Cycle 12** — the proxy-claims cycle.

- **Build 1 — page-scanner corrections + waste removal:** the full-lint page scanner stops reading raw text as link structure and frontmatter validity as attestation, and sheds the reads it never used.
- **Build 2 — the change-keyed findings cache:** full lint stops re-judging pages nothing changed, and says how many it reused and under which ruleset.
- **Build 3 — the PARA posture:** PARA stops using location as a proxy for trust — honest, attested frontmatter becomes the entry condition, containers declare their own `writers:`, and lint enforces it.
- **Build 4 — parked-interim guidance:** a park records the blocker's shape, and something re-reads it at the upgrade that can invalidate it.

**Governance rule changes crossing v0.16.0 — read these before writing.**

1. **PARA's entry condition changed** (`vault-operating-contract.md` **Layer 3** + `{conventions}/extraction.md` **v7**). Location is no longer the proxy for trust: the entry condition is now **honest, attested frontmatter** rather than a closed set of named write surfaces. A container may declare its own `writers:` on its `charter.md`; **an undeclared container is `open`**. Consequence for a vault: a partner may now file an honest `author: agent` / `trust: raw` document into `{projects}`/`{areas}`/`{resources}` **outside `{wiki}`**, wherever no ancestor `charter.md` refuses it. If you want a container closed, declare `writers:` on its charter — silence now means open, not closed.
2. **`vlt-lint` gains `para_writer_unauthorized`** — a PARA write into a container whose ancestor charter's `writers:` does not admit the author is now a finding.
3. **`{conventions}/decision-log.md` v4** — a new `kind: parked-interim` entry records a blocker's shape at the moment work parks against it. `vlt-upgrade`'s reconcile pass re-reads those entries at the upgrade that can invalidate them and surfaces them as `parked_interims_review:`.
4. **Retired in this release:** the Layer-3 **location prohibition** and the **surface-count prohibition** are **gone**. Any local rule, overlay or habit that reasons "PARA writes are illegal because of *where* they land" or "there are exactly N legal write surfaces" is now reasoning from a retired rule — re-derive it against the attestation-based entry condition above.

**Also in this release.** Full-mode `vlt-lint` keeps a per-page findings cache at `_agent/lint-cache.yaml` — extracted facts keyed on the page's own digest crossed with a ruleset fingerprint, never verdicts. It is vault-local, rewritten whole each full run, never wake-read, and safe to delete (the next run simply goes cold). The report's new `lint_cache:` line states `scanned N / cached M of T` beside the fingerprint the reused records were adjudicated under, so a cached run can never read as a fresh sweep. **The first full lint after this upgrade is a cold run** — every fingerprint input moved.

**Changed paths:** `.claude-plugin/marketplace.json`, `CLAUDE.md`, `skills/vlt-agent-creative`, `skills/vlt-extract`, `skills/vlt-feedback`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-query`, `skills/vlt-review-council`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`

## v0.15.0 — 2026-08-24

**Cycle 11** — the reachability cycle.

- **Build 1 — crossLayerSlugs reaches sources/, the index, and non-.md linkables:** the full-mode missing-target check's three blind populations join the derived cross-layer set — `sources/` files at any depth, the `{index}` slug, and non-`.md` linkables — and the check's wording is truthed from "note" to "target".
- **Build 2 — resources/ gains PARA parity:** the write-posture gap neither rule reached closes by grant (a fifth shape), the wiki inside it is named a Librarian-only zone, and the extraction retirement is reversed (extraction convention version 5 → 6).
- **Build 3 — decision-log v3:** subject coherence, a rostered discovery route, and a scoped-deviation kind — three reachability gaps closed on one convention, one coordinated handshake.
- **Build 4 — spec-candidate relay-leg retune:** the trigger counts revision, not traffic — the relay leg now fires on ≥2 same-key `handoff`-shaped entries (a genuine revised-spec event), not ordinary round-trips.
- **Build 5 — the council shortfall signal:** a partial panel says so instead of reading as full — availability shortfall is partitioned by cause and surfaced in the council's return.
- **Build 6 — the PARA closing net:** an undeclared `type:` or `author:` lands loud, not invisible; the nets reach `{resources}` and exclude the wiki by name.
- **Build 7 — the instrument rule:** a wrapped comparison can report "identical" for differing files — the record must name the instrument that actually ran.
- **Build 8 — the small-edits batch:** recipient-agnostic shipped surfaces, the overlay walk clause on relocation migrations, the wiki-index worked-example reconciliation, the rail voice rule single-homed, and the full-lint cost instrumented on both return shapes.
- **Build 9 — the vitals metric vocabulary:** a fourth local-metric kind for content-filtered counts, and the staleness denominator promoted to a canonical metric.

**New in the enforcement kit — a home for content-filtered counts.** `local_metrics:`
gains a fourth bounded kind, `frontmatter_key_count` (count of files matching `glob`
whose frontmatter carries `key:`), so a derive like *pages carrying `review_after:`*
— the exact class a vault previously had to refuse to declare (it had no legal home;
see issue #1) — is now declarable in `{tripwires}` without hand-editing the reader.
The lost instance itself, `pages_with_review_after`, also arrives as a canonical
metric with this release: it is derived for every vault automatically and now
denominates `expired_pages` honestly. If your vault refused a content-filtered
declaration under the old bound, the route exists now.

**Changed paths:** `.claude-plugin/marketplace.json`, `.github/PULL_REQUEST_TEMPLATE.md`, `CLAUDE.md`, `README.md`, `skills/vlt-extract`, `skills/vlt-feedback`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-review-council`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`, `tools/factory-paths-check.py`

## v0.14.0 — 2026-08-23

**Arc 10** — the signal-integrity arc, second release.

- **B10-6 — the report contract:** structured reports persist verbatim as dated plain-`.yaml` files under walker-exempt report dirs — the upgrade post-flight report gains a durable home, schema-derived emission makes mandatory report lines unskippable, and the unfillable `high_value_gaps` slot reports `unmeasured` honestly.
- **B10-7 — the rail amendment channel:** a captured issue stops being write-only — the owner-applied `amended` label routes post-capture comments into the factory, the triage verdict vocabulary becomes queryable labels, and the issue forms arrive triage-ready.
- **B10-8 — the dependency record:** a vault ports but its toolchain doesn't — the module declares the machine tools its shipped skills assume, capabilities record theirs at birth, and setup/upgrade probe the declared set at arrival (report, never gate).
- **B10-9 — the contract overlay:** the operating contract gains its vault-local overlay, closing the one durable-host gap in the governance surface.
- **B10-10 — the PARA container model and parameterization:** Layer 3 re-drawn by authorship, shipping the container the field already built twice.
- **B10-11 — the wiki-move capstone:** the wiki moves into human-browsable space and `resources/` retires as an extraction target — one operation at true cost.
- **B10-12 — the lint-full execution repair:** the full-mode wiki sweep runs again, and can no longer lie when it does not.

**A known issue in v0.13.0, fixed here — full-mode `vlt-lint` was not executable.** On v0.13.0 the full-mode wiki sweep's page-scan schema crossed a fan-out size ceiling, so effectively every scanner agent died; worse, the total failure rendered as a **clean-looking empty report** rather than an error. Standard and scoped lint modes were unaffected. If you ran a full-mode sweep on v0.13.0, treat its output as void — read any such report against its `files_checked:` line, and do not trust a shortfall that no coverage cap explains. B10-12 repairs execution and makes degradation loud: a sweep below majority coverage now returns an error and a dated failed-run record instead of a report, partial coverage is capped and reason-partitioned, and inbound-derived slots are suppressed rather than silently wrong.

**Upgrading a vault with a wiki:** B10-11 moves the default wiki home to `resources/wiki/`. The upgrade offers the relocation and **never moves anything on its own** — declining writes explicit `vault_structure` overrides so every consumer keeps resolving correctly, and wikilinks are slug-based, so the link graph survives the move either way.

**Changed paths:** `.claude-plugin/marketplace.json`, `.github/ISSUE_TEMPLATE`, `README.md`, `skills/vlt-agent-creative`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-feedback`, `skills/vlt-groom`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-query`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`, `tools/package-lint.py`, `tools/test-package-lint.py`

## v0.13.0 — 2026-08-21

**Arc 10** — the signal-integrity arc, first release.

- **B10-1 — the manifest source-hash:** the skill-asset divergence net stops blessing the edits it exists to catch — source-hashed on write, sanctioned edits self-recording, the live-as-source and version-skew escape paths closed.
- **B10-2 — the lint-full signal repair:** the fan-out scanners get the rules they enforce — write-verification joins the read list with a tri-state Gap B, coexistence posture and callout form made explicit, the cross-layer set derived from the structure map, and the fan-out currency rule lands in its home.
- **B10-3 — repeat-aware spec-candidate reporting:** new candidates report loud; unchanged already-filed candidates collapse to one denominated standing line instead of re-firing every run.
- **B10-4 — the durable metric home, the overlay bell, and per-section enforcement addressing:** the enforcement kit learns to hear vault-grown rules.
- **B10-5 — the fleet-wide reflex rung:** fleet-relevant rules stop condensing as per-partner copies — the vault-scoped always-loaded pointer layer lands, and v0.13.0 cuts here.

**Changed paths:** `.claude-plugin/marketplace.json`, `.github/ISSUE_TEMPLATE`, `skills/vlt-agent-creative`, `skills/vlt-agent-librarian`, `skills/vlt-agent-researcher`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-feedback`, `skills/vlt-groom`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-upgrade`

## v0.12.0 — 2026-08-21

**Arc 9** — the boundary arc.

- **B9-1 — the dispatch-ledger repair:** the proto-`deliver` era gets its datum, the key-check exemption is cut to the key requirement on both sites, and the ledger's denominators gain a factory-side reproducibility instrument.
- **B9-2 — the three standing rules:** the durable-host doctrine, rule precedence, and enforcement-ships-with-widening land ahead of the builds they govern.
- **B9-3 — the remote feedback rail:** GitHub issues become the module's reachable front door — the ingress two of this arc's own filings had to route around.
- **B9-4 — consumer registration:** vault-grown ops get a lawful, checked route onto a shipped convention's roster — closing the boundary the arc's load-bearing filing found shut on both sides.

**A note for vaults with agent-authored PARA content:** a known finding exists — agent overflow written into PARA can falsify `sources:` as provenance. Until the model for this lands (Arc 10), such content belongs under `_agent/`, not in PARA through a stretched `sources:` list; the PARA location rule itself stands unwidened.

**Changed paths:** `.claude-plugin/marketplace.json`, `.github/ISSUE_TEMPLATE`, `CLAUDE.md`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-feedback`, `skills/vlt-groom`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-upgrade`, `tools/dispatch-lane-check.py`

## v0.11.0 — 2026-08-17

**Arc 8** — the lifecycle arc.

- **B8-1 — the R3 retrofit:** every shipped check names its legal response, stated where the check lives.
- **B8-2 — the delivery shape:** unsolicited inline-payload delivery gets a legal form, and the pointer-integrity check's pending legal response ships with it.
- **B8-3 — the memory contracts:** partner memory gains a promotion ladder, an always-loaded reflex layer, and thread lifecycle rules (recorded knowledge was demonstrably failing to bind).
- **B8-4 — the groom op:** an invoked, approval-gated groom pass for partner memory (the arc's motivating deliverable — the manual prototype's method codified as an upstream skill).
- **B8-5 — the decay contracts:** rotate/drain verbs, retention-at-birth, and the mass/age wires (the agent zone finally gets a decomposer — every accumulating record gains a declared exit).

**Changed paths:** `.claude-plugin/marketplace.json`, `README.md`, `skills/vlt-agent-creative`, `skills/vlt-agent-librarian`, `skills/vlt-agent-researcher`, `skills/vlt-decay`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-groom`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-upgrade`

## v0.10.0 — 2026-08-15

**Arc 7** — the nowhere-to-put-it arc.

- **B7-1 — the harness baseline:** the release gate learns to prove its own checks can fail.
- **B7-2 — the durability nets:** the config merge preserves instead of rebuilding, and the skill-asset manifest walks the tree instead of trusting a list.
- **B7-3 — frontmatter@6, the coordinated rules bump:** four rule changes, one six-consumer walk; rules ship ahead of their mechanisms with stated interim postures.
- **B7-4 — the seam:** vault-writable fields honored, local conventions received, dispatch given a routing profile (the mechanisms behind the rules the frontmatter bump shipped).
- **B7-5 — relay & address:** the ask/answer shapes and the address rule's mechanism — the rails the frontmatter@6 rules already await.
- **B7-6 — the overlay contract:** workflow assets become first-class handshake nodes, the fan-out honors merged-on-read, and the wiki sources: wikilink form ships with its normalization clause.
- **B7-7 — the council fallback:** a gated mint meeting an unavailable council now parks or records a user-ruled verdict — never an unmarked substitute.
- **B7-8 — the stale-prose sweep:** shipped prose catches up with what the arc made true.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-agent-creative`, `skills/vlt-agent-librarian`, `skills/vlt-agent-researcher`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`, `tools/package-lint.py`, `tools/test-package-lint.py`

## v0.9.1 — 2026-08-01

**Arc 6** — the factory's own honest surface.

- **B6-1 — the changelog:** eight tags say a version happened and nothing says what it contains; the authoring was done thirty-six times and thrown away.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-setup`, `tools/package-lint.py`, `tools/test-package-lint.py`

## v0.9.0 — 2026-07-30

**Arc 5** — the kept-promises arc.

- **B5-1 — the cost instrument:** nothing measures what a partner session loads; every boot-diet disposition downstream is chosen against these numbers.
- **B5-2 — the collision debt:** pages that document their own suspects must never be the ones the check cannot see; carries the inherited A4-4 clause (5) FAILED debt.
- **B5-3 — exact facts:** the lint asks LLM scanners for exactly-computable facts and declares a report slot no check fills; the earliest-shipping proxy-family build writes the extended proxy-check rule.
- **B5-4 — the spec loop:** candidates get an owner and a promotion step, the revision signal stops reading the template back as history, and the adoption stamp becomes reachable off the mint path.
- **B5-5 — preserve & report:** the vlt-upgrade honesty pair: the preserve set widens from a name test to the provenance test B1 already uses, and the ledger's required lines get the close-out check that makes them hard to drop.
- **B5-6 — the decision-log convention:** the entry schema leaves its skill and becomes a handshaked convention; the log gains its machine key; lint joins the loop it was always outside; Q21 is discharged.
- **B5-7 — the boot diet:** the post-hoc ruling is made and the numbers are in; the fixed boot pays ~10K tokens per activation for reinforcement the ruling no longer requires.
- **B5-8 — the whale re-cut:** the two skill whales still charge every invocation for content most invocations never use; the boot whale is already dieted.
- **B5-9 — the enforcement kit:** registry, moment, surface — the promise three releases of shipped prose already make.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-agent-creative`, `skills/vlt-agent-librarian`, `skills/vlt-agent-researcher`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-review-council`, `skills/vlt-setup`, `skills/vlt-upgrade`, `tools/cost-manifest.py`, `tools/package-lint.py`, `tools/test-cost-manifest.py`

## v0.8.0 — 2026-07-26

**Arc 4** — the honest-surface arc.

- **A4-1 — `linkage_ripe` polarity:** the check fires the calibration's absorption signals inverted, and the next ordinary lint on the primary vault surfaces ~97 of 98 notes.
- **A4-2 — the adoption unit:** a key nobody is asked to fill, and a count whose only value is "fine".
- **A4-3 — the contradiction drain:** a bucket named `handled` that also holds things nobody handled.
- **A4-4 — source fidelity:** a wrong name that reads as clean data, and nothing in the ingest path looks.
- **A4-5 — the consult channel:** the bus grows its synchronous mode, and the rule that makes it exercised by construction.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`

## v0.7.0 — 2026-07-18

**Arc 3** — the enforcement arc, second of two releases.

- **19 — the build-15 follow-up unit:** spec advocacy gets a faster clock; two maps get their missing row.
- **20 — the research-note graduation queue, first cut:** opens frontmatter@4; kills the module-caused topic: scalar the whole cluster tripped on.
- **21 — history-writes:** make the module write its own history honestly.
- **22 — mint & wearer surfaces:** the module misdescribes who reviews a mint, who owns a mint, and where a wearer keeps its profile.
- **23 — content-verification:** give the release gate eyes: the module cannot see itself.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`, `tools/package-lint.py`

## v0.6.0 — 2026-07-08

**Arc 3** — the enforcement arc, first of two releases.

- **14 — pre-tag packaging lint:** the factory boundary gets its bell.
- **15 — the spec convention:** a named home for inter-partner contracts, before the third consumer forks the format.
- **16 — frontmatter@3: bell + attestation + freshness:** the one coordinated schema bump.
- **18 — the durability cluster:** the upgrade rail's missing return legs, and the overlay reach it always assumed.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`, `tools/package-lint.py`, `tools/test-package-lint.py`

## v0.5.0 — 2026-07-03

**Arc 2** — capability field-hardening + BMad installer interop.

- **12 — Capability field-hardening:** shared-lane definition, source-type front-end, prep/interpret split.
- **13 — BMad installer interop:** module.yaml resolvability + CSV header canon.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-setup`, `skills/vlt-upgrade`

## v0.4.0 — 2026-06-25

**Arc 1** — closing release.

- **11 — Upstream vlt-track: the shared longitudinal-loop hand:** Round 2 candidate #4.

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-mint`, `skills/vlt-setup`, `skills/vlt-track`
