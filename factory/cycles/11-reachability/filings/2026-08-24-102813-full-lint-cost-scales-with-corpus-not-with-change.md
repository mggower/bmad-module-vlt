# Full lint's cost scales with corpus size, not with change — and the curve is on a path to convert expense into refusal

_Filed 2026-08-24. Evidence: read-only measurement of the `vlt-core` wiki (147 pages,
2.21 MB) against `skills/vlt-setup/assets/workflows/vlt-lint-full.js` and
`skills/vlt-lint/references/full-scale.md`, factory-side. Classification: **pattern** —
a structural cost defect produced by ~8 cycles of individually-correct decisions, none
of which ever removed work. Provenance: an owner-run problem-solving session on
"full lint has become very expensive"; the session artifact carries the full
force-field / decision-matrix working._

## The measurement

Per-page scanner agents in the fan-out each read the same four conventions:

| Convention | Bytes |
|---|---|
| `frontmatter.md` | 38,672 |
| `wiki-index.md` | 8,195 |
| `write-verification.md` | 6,114 |
| `wiki-supersession.md` | 5,550 |
| **per-agent total** | **58,531** (+ overlays) |

At 147 pages that is **147 byte-identical copies** of ~58.5 KB — roughly **70% of the
dominant phase's input**, none of it varying by page.

Estimated whole-run shape (from the script's control flow; **estimate, not
instrumented** — see Direction 0):

| Phase | Agents | Model | Est. input tok |
|---|---|---|---|
| Scan pages | 147 | haiku | ~3.3 M |
| Index drift | 1 | sonnet | ~10 k |
| Contradiction clusters | ~37 (`max(12, ⌈147/4⌉)`) | sonnet | ~600 k |
| Callout-seeded entity pairs | ≤24 | sonnet | ~180 k |
| **Total** | **~209** | | **~4.1 M** |

Three multipliers scale with the corpus simultaneously: page count drives the scan phase,
drives `clusterCap`, and drives cluster *size* — so the mid-model cluster phase amounts to
a **second full read of the corpus** every run.

## Why this is module signal

Three assumptions are load-bearing for the cost, and each is assumed rather than real:

1. **"An agent must read whole convention files to be faithful to them."** A scanner needs
   perhaps 15% of `frontmatter@13`; there is no legal way to take that 15%. Single-home
   discipline correctly forbids restating rules in a prompt — so the design pays whole-file
   price for a slice, per consumer, per run. **The addressable unit of a convention is the
   file, and nothing smaller.** That is a *reachability* defect: the rule the scanner needs
   is declared, but not reachable at the granularity that needs it.

2. **"Full mode means recomputing every page."** `full-scale.md` and the workflow define
   full as full *recomputation*; the correctness requirement is full *coverage*. The
   pipeline keeps no memory of a page's findings across runs, despite already persisting a
   report per run to `{lint_reports}/`.

3. **"The cluster pass needs to re-read pages."** It already receives `key_claims` from the
   scan phase (`vlt-lint-full.js`, the cluster prompt) and then instructs each agent to read
   every page live anyway. The cheap triage signal is bought and discarded.

Two smaller findings fall out of the same read:

- **`wiki-index` is in the page-scanner read set but unused by it.** The page ask
  (`pageScanPrompt`) judges frontmatter, supersession and Gap B; index judgment belongs to
  the dedicated index pass, which reads `wiki-index` correctly. ~1.2 MB per run of pure
  waste.
- **`pageScanPrompt` leads with the variable part** (`${p.path}`, `${p.slug}`) and follows
  with the invariant instruction block — inverting the one ordering under which 147
  near-identical prompts could share a cached prefix.

## The dynamic (why this is not only an efficiency item)

**Vicious loop, running now:** wiki grows → full lint costs more → owner defers full lint →
`lint-debt` accrues → the eventual sweep covers more drift on a bigger corpus → costs more.
Deferral is the current de-facto cost control, and it trades cost for exactly the staleness
lint exists to prevent. The `lint-debt` tripwire nudges toward full runs while the cost
curve penalizes them — the wire is economically at odds with itself.

**Latent availability failure, on the current trajectory:** cost pressure and the Cycle 10
honesty guards share one budget. `budgetFloor` truncation plus the majority-coverage floor
mean a large enough corpus produces a sweep that stops mid-way, falls below the floor, and
returns `status: 'failed'` — refusing to persist findings and **refusing to reset
`lint-debt`** (`full-scale.md` step 3). At that point expense has become refusal. `vlt-core`
is at 147 pages and growing.

**Note the ratchet.** Every honesty repair (A10-16, A10-17, B10-12, DA7) correctly *added*
coverage guards; none ever removed work. Monotonic accretion of correctness is still
monotonic accretion. A guard's cost deserves review on the same cadence as its correctness.

## Candidate directions (for capture, not answered here)

**0. Instrument before optimizing.** The ~4.1 M figure above is an estimate. A per-phase
accounting line in the workflow's return (agent count, input estimate, cached-vs-scanned)
is the baseline every later claim must be measured against. Likewise **measure the actual
page-change rate** between full runs from `{lint_reports}` history + wiki mtimes — a cache's
yield is a function of churn, and churn here is unmeasured.

**1. Waste removal, workflow-only, no governance surface touched.** Drop `wiki-index` from
the page-scanner read set; move the invariant block to the front of `pageScanPrompt`; make
the cluster pass two-stage (triage on the `key_claims` already in hand; escalate to live
reads only on a candidate, recall-biased). Findings should be identical by construction —
which makes an A/B parity run over the live wiki the natural acceptance check.

**2. Separate coverage from recomputation.** A per-page findings cache keyed on
`sha256(page bytes) + the convention `version:` vector`. Full mode re-scans only pages whose
key changed and reuses validated records for the rest. Two design constraints look
non-negotiable: cache **extracted facts, never verdicts**, so the JS reduce still runs
whole-corpus every run (orphans / missing targets stay correct when only 9 pages
re-scanned); and the coverage line must state `scanned N / cached M of T`, so a cached run
can never read as a fresh sweep. Worth noting the invalidation key **already exists and is
already maintained** — a convention rule change bumps `version:` under the handshake, which
invalidates every scan judged under the old rules for free.

This direction also inverts the vicious loop: under change-keyed costing, running full lint
*often* becomes the cheap strategy, and `lint-debt`'s nudge stops fighting itself.

**3. Give governance an addressable sub-unit — projection, not restatement.** A
`## Scanner card` section in each convention: the enforceable rule slice, authored **in the
convention** (so it remains the single home) and covered by the same `version:` handshake.
Consumers that fan out pass card text instead of whole files. Est. 58.5 KB → ~8 KB per
agent. This is the root-cause fix and it generalizes — `vlt-consult` and
`vlt-review-council` fan out against conventions too. It is also the direction with real
governance-surface exposure, so it likely wants to be ruled last rather than first.

**4. Pairs naturally with an existing filing.** Cross-run finding suppression (don't
re-report a flag a human already dismissed) needs the same durable sidecar state as
direction 2 — see `2026-07-26-124223-lint-has-no-memory-of-adjudicated-divergence.md`.
Separate build, shared mechanism; worth ideating together.

**Adjacent, already filed:** `2026-07-26-184704-lint-full-asks-llms-for-exact-facts.md` is
this same seam seen from the correctness side. ~9 of 16 `PAGE_SCAN` fields are pure
deterministic extraction (frontmatter values, `[[wikilinks]]`, callout form, `## Sources`
sets). B5-3 already moved the *arithmetic* into JS ("the scanner reads, JS does the
arithmetic"); moving the *reading* out too is what would let `frontmatter@13`'s 38.7 KB stop
being loaded at all. Cost and correctness want the same change.

**Explicitly not proposed: sampling.** Auditing a rotating fraction deeply would fix the
curve and buy it with honesty — the report could no longer answer "is the wiki healthy?",
only "was this fifth of it healthy?". Cycle 10 was spent purchasing that honesty; this
should not spend it back.

## Sequencing note for capture

Direction 2 touches the same full-mode coverage predicate as **A10-18** (the
`crossLayerSlugs` missing-populations build), which carries the **B10-2(5)/B10-12(6) bound
debt that gates Cycle 11 closeout**. An owner sequencing ruling is owed before direction 2
is briefed. Direction 1 has no such entanglement.

Standing rule worth stating for any build in this family: **no `coverage_caps` entry is
ever removed to make a run look cleaner.** A cheaper lint that finds less is a regression
regardless of what it saves.
