---
title: 'Build #B5-2 — the collision debt (pages that document their own suspects must never be the ones the check cannot see; carries the inherited A4-4 clause (5) FAILED debt)'
status: 'BUILT 2026-07-29 — all five F-sites landed as briefed: PAGE_SCAN grew name_callout_targets (schema + prompt), the callout-seeded pair pass + PAIR_FINDINGS + pairCap + entity_scan_facts landed in vlt-lint-full.js, and SKILL.md gained the Step 2 second-leg paragraph, the widened Step 5 entity_scan: denominator + composition rule, and the Step 4 duplicate-filing guard. Verified: positive fixture run (5-page temp wiki, greedy consumption split the directly-linked pair — clusters_total 1 with signal-relay unclustered) surfaced the pair in entity_collisions marked (callout-seeded) with seeded_pairs_checked=1; negative run (callout removed) ran zero pair agents, seeded_pairs_total=0, all existing top-level keys intact; cross-file greps agree at every named site; package-lint A/B/C/E PASS; scrub grep zero hits. Deviations/notes: (1) pairCap reads via Number.isInteger(a.pairCap) ? a.pairCap : 24 instead of the || idiom the other caps use, so the brief''s forced pairCap: 0 test value is honored rather than silently falling back to 24; (2) the cap path was verified by code inspection (the brief''s stated alternative), not a third fixture run — with pairCap 0 the slice empties the list and the coverage_caps message naming the uncompared count is pushed before any agents run.'
module_code: 'vlt'
created: '2026-07-29'
derives_from:
  - 'inbox/2026-07-29-120002-entity-collision-coverage-pair-incomplete.md (A5-16 — the whole filing: the sweep-shape claim and the callout-seeded proposal)'
  - 'inbox/2026-07-25-160949-auto-caption-name-substitution.md (held in the active inbox as the CARRIER of the inherited A4-4 clause (5) FAILED debt — this build is its fix; it releases only when the fix ships AND passes acceptance)'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): grouping (B5-2 = A5-16 alone, ships second per the A4-1 precedent — inherited debt ships early); evidence-debt disposition (the A4-4 clause (5) FAILED debt attaches to B5-2; its carrier filing stays in the active inbox until the fix ships and passes acceptance); questions-designated (A5-16''s cluster-aware second-pass shape is this brief''s to rule — carried as a proposal, not a ruling)'
risk: 'low — two shipped files edited (vlt-lint-full.js + vlt-lint/SKILL.md prose); no convention version bump, no consumer walk, no structure-map change; behavioral surface is full-mode lint at scale only'
---

# Build #B5-2 — the collision debt

Goal: close the sweep-shape gap that failed A4-4's acceptance clause (5). The entity-collision
check works — vlt-core's 2026-07-26 full lint surfaced three real collisions — but the sweep is
cluster-bounded, clusters are built by **greedy consumption** (`vlt-lint-full.js:206-220`: each
page is consumed into the *first* matching cluster), and `entity_collisions` is only ever asked
within a cluster. Consequence, confirmed at capture and re-grounded this brief: **even
directly-linked pages can be split** — the vault page that documents the debt's named pair links
its counterpart directly (`los-angeles-rams.md:72` → `[[nfl-2026-offense-rankings]]`) and carries
a name-verification callout naming it explicitly (`:76-79`, with the pair-link "one lookup
settles both"), and the check still never compared the two. The fix is a **callout-seeded second
pass**: after the cluster pass, compare exactly the pairs the vault itself has marked as
suspicious, wherever clustering put them.

Why now: this build carries the arc's inherited debt — A4-4 clause (5), graded FAILED
2026-07-27, owner-confirmed 2026-07-29 — and the ideation grouping ships it second per the A4-1
precedent (inherited debt ships early). The Arc-4 ledger's `[x]` count may not be read as a
measure of what that arc proved until this lands.

**Rejected alternatives in the parent filing and capture are settled — do not re-litigate:**
the capture's sharpening is near-binding on direction — *"the fix is a cluster-aware second
pass, not a looser linkage test."* Do not rework cluster formation, do not loosen the
shared-link threshold, do not attempt an exhaustive all-pairs entity sweep (the affordability
logic of A4-4's brief §disposition 2 applies unchanged: bound the check by what is marked, not
by what the corpus contains). The single-mention blind spot (`vlt-lint:74`) is by construction
and stays; this build closes only the pair-shaped limit.

## Brief-time dispositions

The roadmap designates one question to this brief (§Questions deliberately left to brief time:
*"A5-16's cluster-aware second-pass shape — carried as a proposal, not a ruling"*). Ruled here,
with the two consequential calls that fall out of it.

1. **The shape: a callout-seeded pair pass appended after the cluster pass, in the workflow;
   cluster formation untouched.** The filing's proposal is adopted as filed: seed pairs from
   name-verification callouts already on disk — a callout on page A that questions a proper noun
   against page B is the vault marking the pair (A, B) as suspect. The pass compares every
   seeded pair the cluster pass did not already compare. Cluster formation (`:206-220`) is not
   edited: the capture rules the direction ("not a looser linkage test"), and any clustering
   change re-shapes the contradiction pass's cost and coverage — a different, unfiled build.
2. **Seed source is callouts only, not all cross-cluster direct links.** A directly-linked pair
   with *no* callout stays invisible to the pass — an honest residual, because comparing every
   split direct-link pair reintroduces the unbounded pair-population the cluster cap exists to
   bound. The filing's own letter draws this line ("pages that document their own suspects
   should never be the ones the check can't see"), and the residual is stated where the blind
   spots already live: the `entity_scan:` denominator (F4). If the residual bites in the field,
   that is a new filing, not silent scope creep here.
3. **Seeded findings land in `entity_collisions`, marked, and Step 4 gains a duplicate-filing
   guard.** A callout-seeded finding is by construction a *documented* suspicion — the Rams
   callout already records "Tracked in `{backlog}`." Without a guard, every full lint until the
   collision resolves would file a fresh backlog item for a pair the vault already tracks —
   a manufactured-duplicates regression. So: seeded findings carry a `(callout-seeded)` marker
   in the finding string, and Step 4's entity-collision filing (F5) checks the seeding callout's
   own tracking line before filing. Findings are not given a new report slot — one finding, one
   slot, per the standing precedence rule (`vlt-lint:70`), and the marker is provenance, not a
   bucket.

## F1 — `vlt-lint-full.js` PAGE_SCAN: extract name-callout targets

**Current state:** `PAGE_SCAN` (`vlt-lint-full.js:64-93`) extracts per-page findings; nothing
extracts callout-marked suspect pairs — the capture's finding verbatim: *"No pass reads
already-flagged name callouts to seed pairs (`:68` surfaces `[!stale]` generically; nothing
feeds the entity pass)."* The scanner prompt is `pageScanPrompt` (`:122-124`).

**Change:** add one required field to `PAGE_SCAN` (append to `required:` at `:67` and
`properties:`):

```js
name_callout_targets: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['target', 'name'], properties: {
  target: { type: 'string', description: 'the [[wikilinked]] page the callout names, normalized to a slug' },
  name: { type: 'string', description: 'the proper noun the callout questions' },
} }, description: 'one entry per callout on THIS page that questions a proper noun against another named wiki page (a name-verification / [!stale] callout whose body says this page and that page disagree about a name) — the vault marking a suspect pair. Empty when the page carries none.' },
```

and extend `pageScanPrompt` with the matching instruction (one clause in the existing "Return
ONLY findings about THIS page" list): report `name_callout_targets` — for each callout that
questions a proper noun against another wiki page, the target slug and the name in question;
an ordinary `[!stale]` marker with no cross-page name question yields nothing.

**Why:** the seeded pass (F2) can only run on what the per-page scanners return — the workflow
has no filesystem access (`:14-16`), so the pairs must ride the scan results.

## F2 — `vlt-lint-full.js`: the callout-seeded pair pass + honest scan facts

**Current state:** the cluster pass ends at `:241` (`clusterResults`); assembly begins `:243`;
`entity_collisions: flat('entity_collisions')` at `:282`; the comment at `:279-281` says the
SKILL composes the `entity_scan:` denominator "from files_checked + the cluster cap" — but the
workflow returns the cluster count only inside a cap message, so an uncapped run gives the SKILL
nothing exact to compose from.

**Change — insert between the cluster pass and assembly:**

1. Build the compared-pair set: for each group in `clustersToCheck`, every within-group pair,
   keyed order-independently (sorted `a|b`).
2. Build the seed set: for each scan `s`, each `{target, name}` in `s.name_callout_targets`
   where `slugSet.has(target) && target !== s.slug` — pair key + the name hint. Dedupe;
   drop pairs already in the compared set.
3. Cap: `pairCap` arg (document in the args block `:19-34`), default `24`; when seeds exceed
   it, slice and push a `coverage_caps` message naming how many seeded pairs were NOT compared
   (the no-silent-caps discipline the workflow already follows for clusters, `:222-227`).
4. Run one agent per remaining pair via `parallel` (`clusterModel`, phase
   `'Reduce + cross-page'`, label `entity-pair:<a>+<b>`), with a dedicated minimal schema
   (`PAIR_FINDINGS` — one required `entity_collisions` string-array property) and a prompt of
   the same discipline as the cluster prompt (`:233-236`): read both LIVE paths (resolve via
   `pages`), the pair was marked suspect by a callout questioning the name `<name>`; report
   `entity_collisions` — the same proper noun recorded with incompatible attributes across
   these two pages, as `"page-a vs page-b: <name> — <attribute A> vs <attribute B>"`; apply
   the precedence rule (a one-name conflict is an entity collision, never also a
   contradiction); report nothing else. The agent judges the *pages*, not the callout — a
   marked pair whose pages don't actually collide returns empty (that is the pass working,
   not failing).
5. Merge: append seeded findings to `entity_collisions` with a ` (callout-seeded)` suffix.
   Duplication with cluster findings is impossible by construction (only never-compared pairs
   run).
6. Return honest facts for the SKILL's denominator composition: add a top-level
   `entity_scan_facts: { clusters_checked, clusters_total, seeded_pairs_checked, seeded_pairs_total }`
   to the returned object, and update the `:279-281` comment to name it as the composition
   source.

**Why:** discharges A5-16's core gap — the pairs the vault itself has marked suspicious are
compared even when greedy consumption splits them — and makes the `entity_scan:` line
composable from returned facts instead of inferable only when capped.

**Out of scope at this site:** the cluster-formation loop (`:206-220`) is untouched
(brief-time disposition 1); no `documented_*`-style split for entity findings (disposition 3 —
the marker is provenance, not a bucket).

## F3 — `vlt-lint/SKILL.md` Step 2: the check states its new leg

**Current state:** the entity-collision check (`vlt-lint:70-74`) ends with the blind-spot
paragraph (`:74`): *"a substitution that entered once and was never contradicted by another
page is invisible to a cross-page test by construction."* Nothing states the pair-shaped limit
or its close.

**Change:** append one short paragraph after `:74`, in the check's own register:

> **Its second leg (full-mode fan-out):** pairs the vault has already marked as suspicious — a
> name-verification callout on one page questioning a proper noun against another — are
> compared by a callout-seeded second pass even when cluster bounding would split them. Pages
> that document their own suspects are never the ones the check can't see. A split pair
> carrying **no** callout remains uncompared — the denominator states it (Step 5,
> `entity_scan:`).

**Why:** the check's limits and legs live in the check's own text (the standing pattern at
`:74` and `:89`); a reader of Step 2 must not need the workflow source to know what the sweep
covers.

## F4 — `vlt-lint/SKILL.md` Step 5: denominator and composition rule

**Current state:** the report template's `entity_scan:` line (`:189`):
`<P pages compared in Q clusters; single-mention substitutions are invisible by construction>`;
the composition rule (`:207`) says the line carries "pages, and clusters in full mode (from
`files_checked` and the cluster cap the workflow surfaces)" and names the blind spot "a
cluster-bounded sweep did not compare every pair."

**Change:**

- `:189` becomes:
  `entity_scan: <P pages compared in Q clusters + R callout-seeded pairs; single-mention substitutions are invisible by construction; unmarked split pairs are not compared>`
- `:190`'s example gains the optional marker:
  `entity_collisions: [<page-a vs page-b: <name> — <attribute A> vs <attribute B> (suspected source substitution | callout-seeded)>, ...]`
- `:207`: the compared population now reads "pages, clusters, and callout-seeded pairs in full
  mode (**from the workflow's returned `entity_scan_facts`** and any pair-cap it surfaces)";
  the blind-spot clause updates honestly: "a cluster-bounded sweep did not compare every pair —
  callout-marked pairs are the stated exception, compared by the seeded second pass; an
  unmarked split pair remains invisible."

**Why:** the denominator is where A4-4 put the check's honesty; the compared population changed,
so the line and its composition source change with it — exactly the site the capture named
("plus `vlt-lint:207`'s `entity_scan:` composition rule if the compared population changes").

## F5 — `vlt-lint/SKILL.md` Step 4: the duplicate-filing guard

**Current state:** Step 4 files a backlog item per entity collision (`:137-143`), with "No
`**Filed:**` back-write — there is no callout to write back into." For a **callout-seeded**
finding that premise is false by construction: the seeding callout exists and may already
record tracking (the Rams callout: "Tracked in `{backlog}` alongside the Seahawks-coordinator
instance").

**Change:** append one clause to the entity-collision filing block: for a finding marked
`(callout-seeded)`, first read the seeding callout — if it records an existing `{backlog}`
item (a "Tracked in" / "Filed" line) and that item is still open under `## Open`, do **not**
file a second; mention the existing item in-flow instead. If the callout claims tracking but no
open item exists, file one and note the mismatch. The "no `**Filed:**` back-write" rule stands
for *unseeded* findings; a seeded finding's callout is the vault's own record and is left as
the page's author wrote it.

**Why:** brief-time disposition 3 — without this, the fix manufactures a duplicate backlog item
on every full lint until the named collision resolves.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row. No convention edited, no
`version:` bump ⇒ no consumer walk, no re-ack — the capture's "no handshake implications
apparent" re-confirmed at brief time: `vlt-lint`'s `depends_on` (`SKILL.md:4`) is untouched,
and its existing ack covers its own workflow asset (`vlt-lint:79`, "a consumer's ack covers
its own workflow assets").

## Out of scope (dispositioned)

1. **Reworking cluster formation** (non-greedy, overlapping, or looser-linkage clustering) —
   rejected by the capture's sharpening ("a cluster-aware second pass, not a looser linkage
   test"); would re-shape the contradiction pass's cost/coverage, an unfiled build.
2. **An exhaustive or direct-link-seeded pair pass** — rejected on cost (brief-time
   disposition 2); the residual (unmarked split pairs) is stated in the denominator, and a
   field instance of it is a new filing.
3. **The single-mention blind spot** — by construction, unclosable by any cross-page check;
   already stated at `vlt-lint:74`; unchanged.
4. **Scoped-mode and small-inline-full pair-completeness** — scoped mode is bounded by its
   scope by design, and inline full mode (≤ ~30 pages) reads every page in one context with no
   cluster bound; the sweep-shape gap exists only in the fan-out path, which is where the fix
   lands.
5. **A documented/undocumented split for entity findings** (mirroring the contradiction
   slots) — not filed, not needed: the `(callout-seeded)` marker plus the Step 4 guard carry
   the only behavioral consequence of documentedness; a slot split is A5-18/B5-9-adjacent
   report-surface work.
6. **The Jonah/Alaric adjudication itself** — the A4-4 evidence-debt rule stands: nobody has
   verified either name, and no F-site text or acceptance check may assert which is correct.
   The build's subject is that the module can now *see the question*; answering it is the
   vault's backlog item ("closes on: any staff/roster/depth-chart source").
7. **A5-18 (lint report persistence)** — B5-9's, per the grouping; noted at capture as
   non-blocking either way for this build.

## Verification (unit, at rest)

- **Fixture run (positive):** build a temp fixture wiki (placeholder content only — public
  repo; no NFL/vlt-core names) of ~5 pages engineered so greedy consumption splits a
  directly-linked pair: a hub page whose links consume page B into cluster 1 before page A
  (linking B directly, carrying a name-verification callout naming B) forms its own cluster.
  Run `vlt-lint-full.js` via the Workflow tool (`{scriptPath, args}` — args as the JSON the
  SKILL would pass: `pages`, `indexPath`, `conventionsPath`, `today`). Assert: the pair is NOT
  co-clustered (the pre-fix loss shape reproduces), yet `entity_collisions` carries the pair
  with the `(callout-seeded)` marker, and `entity_scan_facts.seeded_pairs_checked` ≥ 1.
- **Fixture run (negative):** same fixture minus the callout → the seeded pass runs zero pair
  agents, `entity_scan_facts` present with `seeded_pairs_total: 0`, output shape otherwise
  unchanged from the current contract (all existing top-level keys intact).
- **Cap path:** assert (fixture or code-inspection with a forced `pairCap: 0`) that excess
  seeded pairs produce a `coverage_caps` message, never a silent slice.
- **Cross-file agreement greps (editing aid, not the recorded verification):**
  `name_callout_targets` appears in `PAGE_SCAN.required`, `PAGE_SCAN.properties`, the scanner
  prompt, and the seed-building code; `entity_scan_facts` appears in the workflow return and
  in `vlt-lint:207`'s composition rule; `(callout-seeded)` appears in F2's merge, `:190`'s
  example, and Step 4's guard.
- **Handshake re-check: not applicable** — no convention `version:`, `consumers:`, or
  structure-map change (package-lint Group E is the check of record when one occurs; none
  does).
- Mid-arc packaging lint: `uv run tools/package-lint.py` groups A/B/C/E → PASS.
- **Scrub:** grep the two changed shipped files and the fixture for `vlt-core`, `{owner}`,
  `/Users/`, `Jonah`, `Alaric`, `Rams`, `Seahawks` → zero hits (the debt's instance names stay
  in dev artifacts only).
- Delete any `.decision-log.md` before commit; one commit for the build.

(No Release section — B5-2 is not the arc's release build; the version bump rides the arc's
release build per standing practice.)

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable] Both halves of the fix reach the field.** On the next ordinary vlt-core
   upgrade, the installed `.claude/workflows/vlt-lint-full.js` carries the seeded pass
   (`name_callout_targets` in PAGE_SCAN + the pair pass + `entity_scan_facts` in the return)
   and the installed `vlt-lint/SKILL.md` carries the second-leg paragraph (Step 2), the
   widened `entity_scan:` denominator (Step 5), and the Step 4 duplicate-filing guard —
   checkable by grep on the installed vault. Bounded: the upgrade is going to happen anyway.
2. **[field-contingent] The named lost pair surfaces — this is the inherited A4-4 clause (5)
   debt's discharge.** Producing vault: **vlt-core** (factory-readable; the owner runs the
   lint). On the first full `vlt-lint` after the upgrade, with the "Which Jackson?" callout
   (`los-angeles-rams.md:76`) still standing unresolved: the los-angeles-rams ↔
   nfl-2026-offense-rankings pair surfaces in `entity_collisions` marked `(callout-seeded)`;
   the report's `entity_scan:` line carries the seeded-pair count (R ≥ 1); and **no duplicate
   backlog item is filed** (the pair is already tracked — the Step 4 guard's first live
   exercise, a discharge that could fail on either half). If the vault resolves the callout
   before any full lint runs, the named subject can no longer produce the event — the check
   then re-targets the next standing name callout, and if none exists it is graded on the
   fixture evidence plus the first live callout-bearing lint thereafter; it is never
   vacuously passed. On pass, the inherited debt discharges and both the carrier filing
   (`inbox/2026-07-25-160949-auto-caption-name-substitution.md`) and this build's filing
   become archivable per `arc-closeout` Stage 5.
