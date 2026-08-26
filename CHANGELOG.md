# Changelog

Notable changes to the `vlt` module, one section per released version, newest first.

The record begins at `v0.4.0`; earlier tags predate the per-build commit history these entries
are derived from.

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
