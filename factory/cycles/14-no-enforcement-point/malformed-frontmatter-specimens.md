# `malformed_frontmatter` — the Q8/E4 specimen set

*Produced by Cycle 14 build-1 (`briefs/build-1-structured-claim-return.md`, disposition 8 and
acceptance check 6). A **factory record**, never shipped: it is not in any enumerated vital,
manifest, or skill-asset class, and own-the-apply never copies it into a vault (brief §Verification
R4).*

**What this file is for.** Q8 defers the `malformed_frontmatter` retirement for a third time and
build-1 ships its **measurement** instead. Per roundtable A19 the measurement is bound by three
constraints, and this file is the shape they require:

1. **It must be able to fail** — the post-change half asserts a stated bound (below), it does not
   merely report a number.
2. **It is a specimen set, never a bare count** — slug **plus the minimal triggering fragment** for
   every page reaching the class. Inheriting a cardinality would reproduce `ST-5` one section below
   the citation.
3. **Its two halves are different instruments** — the pre-change baseline comes from the persisted
   `{lint_reports}` archive (a real corpus needing no new sweep); the post-change half needs a
   **live sweep**, because build-1 changes the return's shape and pre-change recorded returns are
   free text the post-change schema cannot emit. **No wiki corpus ships in this repo.**

**⚠ E4 is BOUND by this file, not discharged.** Build-1 produces the datum; the debt transfers,
with the number attached, to the build that takes the retirement (roadmap §Carried forward item 5).

---

## Half 1 — the pre-change baseline (at rest, from the persisted archive)

*Instrument: the `{lint_reports}` archive on `{field-vault}`. Filled at build time, 2026-08-27,
against the three full sweeps that ran under the v0.16.0 / v0.16.1 reduce.*

| sweep | corpus (`files_checked`) | reduce shipped | entries reaching `malformed_frontmatter` |
|---|---|---|---|
| 2026-08-24 | 145 | v0.16.0 (no reduce-side guard) | **18** |
| 2026-08-25 | 146 | v0.16.0 (no reduce-side guard) | **7** |
| 2026-08-26 | 146 | v0.16.1 (guard shipped) | **3** |

### 2026-08-24 — 18 entries, adjudicated 18/18 NOT genuine

Minimal triggering fragment, recorded in the sweep's own `instrument_findings:` as a class rather
than per-slug: *"18 malformed_frontmatter entries the fan-out returned are all 'missing
verified_by/verified_at' — the same class as unattested_write, double-reported by the page
scanners; folded into the attestation census, not treated as a separate finding."*

**Honest limitation, recorded rather than papered over:** this sweep's report adjudicated the class
in aggregate and did **not** persist the 18 slugs individually, so per-slug fragments are
unavailable for this run. The class attribution (all attestation-only) is the archive's own
adjudication and is not re-derivable per slug from what was persisted. This is itself a datum for
the successor: the pre-change instrument's resolution is bounded by what the sweep chose to record.

- attestation-only complaints: **18**
- claimed-missing documented-optional fields: **0**
- genuine schema breaks: **0**

### 2026-08-25 — 7 entries, adjudicated 1/7 genuine

| slug | minimal triggering fragment | class |
|---|---|---|
| `bistec-encebollado` | attestation complaint — no `verified_by:`/`verified_at:` | attestation-only |
| `k-curve-career-divergence` | attestation complaint — no `verified_by:`/`verified_at:` | attestation-only |
| `kettl` | attestation complaint — no `verified_by:`/`verified_at:` | attestation-only |
| `llm-wiki-pattern` | attestation complaint — no `verified_by:`/`verified_at:` | attestation-only |
| `obsidian-bases` | attestation complaint — no `verified_by:`/`verified_at:` | attestation-only |
| `ashwagandha` | `"missing review_after"` | claimed-missing optional |
| *(1 further entry, not individually named in the persisted report)* | — | unadjudicated in archive |

Source: the sweep's `instrument_findings:` — *"5 of the 7 malformed_frontmatter entries
(bistec-encebollado, k-curve-career-divergence, kettl, llm-wiki-pattern, obsidian-bases) are
attestation complaints misrouted by the page scanners"* and *"1 malformed_frontmatter entry
(ashwagandha: 'missing review_after') is NOT a finding — review_after: is optional in the wiki
schema; the scanner invented the requirement."*

- attestation-only: **5** — claimed-missing optional: **1** — genuine: **0** — unadjudicated: **1**

**These five slugs are five of the six subjects of Cycle 13's acceptance check (2)**
(`factory/cycles/13-trusted-returns/roadmap.md:468-473`); the sixth,
`execution-to-judgment-shift`, reached `unmarked_supersessions` in the same sweep rather than this
class.

### 2026-08-26 — 3 entries, adjudicated 1/3 genuine (the sweep that refuted Cycle 13)

| slug | minimal triggering fragment (verbatim from the report) | class |
|---|---|---|
| `empyrean-series-overview` | *"review_after missing on time-bound content"* | claimed-missing optional — **leaked past the shipped guard** |
| `execution-to-judgment-shift` | *"attestation-only complaint"* | attestation-only — **leaked past the shipped guard** |
| `parallel-walk-introduction` | *"summary exceeds the 160-character limit (162 characters)"* | **GENUINE** |

- attestation-only: **1** — claimed-missing optional: **1** — genuine: **1**

**Why the two leaked** — the archive's own diagnosis, and the reason Cycle 14 exists: *"the v0.16.1
reduce-side guard is correct in intent but its conjunction is defeated whenever a scanner cites the
rule it is applying."* The scanner's prose named real page-schema keys in a parenthetical and left
residue behind, defeating both legs of the `and NOTHING else` conjunction at once.

**Baseline summary across the three sweeps: 28 entries, 1 genuine (3.6%).**

---

## Half 2 — the post-change measurement (UNFILLED — bound to the first live sweep)

*Instrument: a live `vlt-lint --full` sweep on `{field-vault}` after upgrading to release 1.
Performer: the owner (standing rule). Vault: `{field-vault}` only — the sole install with the
146-page wiki and this defect's multi-run baseline. This half **cannot** be produced at rest: the
post-change schema emits a structured verdict that no pre-change recorded return can supply, and no
wiki corpus ships in this repo.*

**The bound this check asserts, and can fail (A19 fault 1):**

> In the post-repair `malformed_frontmatter` class, **zero** specimens are attestation-only
> complaints and **zero** are claimed-missing documented-optional fields; **every** remaining
> specimen is adjudicated, one by one against its page, as a genuine schema break. The class's
> cardinality is **recorded but is not the check.**

**FILLED 2026-08-27** from `{lint_reports}/2026-08-27-1104-lint.yaml` — the first full
`vlt-lint --full` sweep on `{field-vault}` after the 0.16.1 → **0.16.2** upgrade
(`{upgrade_reports}/2026-08-27-0947-upgrade.yaml`). Owner-run, read-only. `lint_cache: cold`
(ruleset fingerprint moved with `module_version`), `files_checked: 146` of `files_listed: 146`.

| slug | minimal triggering fragment | adjudication |
|---|---|---|
| `ai-ghost-work` | orphaned frontmatter list items written **outside** `sources:` | **GENUINE** |
| `career-history-as-evidence` | same class — *and it parses cleanly under PyYAML*, i.e. a semantic mis-key a parse test alone passes | **GENUINE** |
| `creatine-monohydrate` | orphaned frontmatter list items outside `sources:` | **GENUINE** |
| `fantasy-platform-read-access` | orphaned frontmatter list items outside `sources:` | **GENUINE** |
| `nfl-2026-position-rankings` | same class — parses cleanly under PyYAML, still correctly flagged | **GENUINE** |
| `seattle-seahawks` | orphaned frontmatter list items outside `sources:` (4 genuinely new entries) | **GENUINE** |
| `single-nutrient-claims` | orphaned frontmatter list items outside `sources:` | **GENUINE** |
| `technical-hiring-pipeline` | same class — parses cleanly under PyYAML, still correctly flagged | **GENUINE** |
| `barbacoa` | *"summary exceeds 160 characters (171)"* | **REFUTED** — the parsed scalar is under the limit; the scanner counted the raw YAML line, quoting included |
| `l-theanine` | *"summary exceeds 160 characters (161)"* | **REFUTED** — same instrument artefact |

**Resolution limit, recorded not papered over.** The 8 genuine specimens are persisted by the
sweep as a **class** with its slugs, not per-slug fragments, and all 8 were repaired in the same
run (`fix_now.frontmatter_drift` / `fixes_applied`), so the triggering bytes no longer exist on
disk and a per-slug minimal fragment is not re-derivable after the fact. This is the **same
resolution bound** the 2026-08-24 baseline hit, and it is itself the datum for the successor: the
instrument's specimen resolution is capped by what the sweep chooses to record before it fixes.
The class fragment is verbatim from the report; 5 of the 8 pages were unparseable YAML before the
fix, 3 were not.

- corpus size (`files_checked`): **146**
- sweep date: **2026-08-27** (`2026-08-27-1104-lint.yaml`)
- attestation-only: **0** (bound: **0**) — **MET**
- claimed-missing optional: **0** (bound: **0**) — **MET**
- genuine schema breaks: **8 of 10** (bound: **all remaining**) — **NOT MET**
- **VERDICT: the bound FAILS on its third leg.** Both classes build-1's reduce-side repair was
  written to refuse are at **zero**, down from a baseline where they were 100% (2026-08-24, 18/18),
  86% (2026-08-25, 6/7) and 67% (2026-08-26, 2/3) of the class. But 2 of the 10 remaining specimens
  are **not** genuine schema breaks. They escape by a **different mechanism** than the one build-1
  closed — not a rule-citing scanner defeating a reduce-side conjunction, but a scanner-side
  measurement bug: the summary-length test measures the raw frontmatter line instead of the parsed
  scalar, and both refutations sit within 11 characters of the limit. Filed the same day as
  `factory/inbox/2026-08-27-160000-summary-length-check-counts-the-raw-yaml-line.md`.
  **The number that transfers with E4 to the retirement build is therefore 10 flagged / 8 genuine
  / 2 refuted at 146 pages — a 20% false-positive rate, not zero.**

**⚠ The first full lint after release 1 is COLD by construction.** Build-1 rewrites both halves of
`canonicalScan`, so every existing `_agent/lint-cache.yaml` record is unreusable and the sweep
scans 100% of pages. That is not a cache regression, and it does not affect this measurement.
