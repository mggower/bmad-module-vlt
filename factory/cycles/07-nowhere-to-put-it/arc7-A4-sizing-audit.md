# Arc-7 amendment-A4 sizing audit — "sizing ≠ fixing"

date: 2026-08-15
status: complete — read-only class count, run before B7-3 is briefed per amendment A4
scope: shipped module source only (`skills/` excluding `skills/reports/`, `.claude-plugin/`, `tools/`)
rule: this audit sizes; it fixes nothing. The fixes stay in B7-8.

## Method

1. Read the roadmap's authority sections first: capture entries A7-5, A7-6, A7-7, A7-8, A7-9,
   A7-10, A7-12; the ideation-rulings pre-ideation slot 3 (the count-since-N principle and its
   overturn clause); the B7-3 and B7-8 ruling slots; post-ideation amendment A4.
2. Enumerated the shipped surface (57 files) and swept it with targeted greps plus close reads
   of every hit's context:
   - **Class 1**: every shipped metric/counter/threshold site — `deferral_metric` /
     `deferral_threshold` / `review_after` / `adoption_first_instance` /
     `enforcement_counter` across all 9 conventions; the tripwire registry
     (`tripwires.yaml`) and the vitals reader's canonical `METRICS` table
     (`vlt-vitals.py`); every derived count in `vlt-lint/references/checks.md`
     (`spec_candidate` ≥2 relays, near-duplicate signals, `linkage_ripe`); the
     watermark/"since last" machinery in `vlt-dispatch` and `vlt-lint`; the
     write-verification ≥2-sweeps promotion path. For each, asked: **is the baseline the
     count runs from itself shipped (as a field, a persisted record, or a derivable vault
     read), or is it recorded nowhere a vault can read?**
   - **Class 2**: swept for permanent-property assertions near frontmatter fields
     ("cannot fire", "no first live instance", "only attainable value"), enumeration
     claims ("the module ships…", "council + lint-full", consumer lists), and
     cross-file semantic agreement (null-vs-absent semantics, threshold-schema vs shipped
     instances, workflow rosters vs install steps, `depends_on` acks vs `consumers:` lists —
     the frontmatter@5 bipartite set verified consistent: 6 listed, 6 acked @5).
3. Distinguished (a) instances already filed in the Arc-7 capture from (b) instances this
   audit found. Borderline non-instances are recorded with the reason they were excluded, so
   B7-8's fixing sweep does not re-litigate them.

## Class 1 — count-since-N metrics without a shipped baseline

Definition (pre-ideation ruling 3, applied per amendment A4): a shipped metric/counter/threshold
phrased relative to a count or a point in time whose baseline is not itself shipped alongside it.
The ruled principle: *a metric that counts from a baseline ships that baseline in its own
frontmatter*; the positive precedent is `adoption_first_instance:` (a shipped point-in-time
carry-forward).

### Instances

| # | file:line | text | why it belongs | provenance |
|---|---|---|---|---|
| 1 | `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:17` | `deferral_threshold: "2 drift findings, or the 3rd new convention"` | Both halves count from unshipped baselines: the drift-finding window start is stated nowhere, and the convention count "the 3rd" runs from is recorded nowhere a vault can read — half the metric is unevaluable from inside a vault. | **(a) already-filed** — A7-5, the instance that produced the ruling |

**Class 1 total: 1 instance. New instances found by this audit: 0.**

### Sites examined and excluded, with reason (so B7-8 need not re-sweep them)

- `spec.md:15` (`deferral_threshold: "1 — any such bump…"`) — threshold of 1 needs no baseline;
  any single observed instance trips it. The roadmap's own capture treats spec@2 as
  "metric now attainable, reads 0 honestly."
- `wiki-consolidation.md:15` (`"3 carried across 2 consecutive sweeps"`) — cross-sweep, but the
  baseline record ships: lint persists every report verbatim to `{lint_reports}/`
  (`vlt-lint/SKILL.md:72`, append-only), so "carried across sweeps" is derivable from
  vault-readable state.
- `tripwires.yaml:42-57` (`lint-debt` ≥ 10, `relay-overdue` > 21) — both metrics name canonical
  vitals ids whose baselines are vault reads (`{log}` headers, dispatch run-header dates);
  `vlt-vitals.py:349` even states the no-baseline degradation explicitly ("no `lint` baseline —
  every ingest header counts").
- `vlt-vitals.py:190-220` METRICS table — all ten ids are derive-only from vault files; the
  module's stated posture ("NO OP EVER WRITES COUNTERS") is the anti-class.
- `checks.md:46` (`spec_candidate` ≥2 relay entries) — "derive the count from handoff file state
  + dispatch relay entries; **no stored counter**" — baseline is the state itself.
- `write-verification.md:60` (tier-2 class "recurs across ≥2 sweeps") — same persisted-report
  baseline as wiki-consolidation.
- `vlt-dispatch/references/daily.md:11-13` and `vlt-lint/SKILL.md:23-35` ("since last run/lint")
  — watermarks and `{log}` headers are the shipped baselines by design.
- **Borderline, recorded as a watch, not counted:** `vlt-upgrade/SKILL.md:112` reports a null
  adoption axis as "declared since `created:` — N days". The baseline is shipped, but it is a
  proxy: `created:` is the file's birth, not the axis's declaration date. Accurate today only
  because the four null-carrying conventions were born with the axis; an axis retrofitted onto
  an older convention (e.g. `extraction.md`, created 2026-06-01) would misdate. Not an instance
  now; the exact shape that becomes one.

## Class 2 — stale shipped prose (the A7-6 class)

Definition: statements in shipped skills that current source contradicts — including the A4
narrow form, *prose asserting a permanent property a frontmatter field can invalidate*, and the
wider form the capture grounded (enumerations fallen behind additions; cross-file semantic
disagreement).

### (a) Already-filed instances

| # | file:line | text / claim | filed under |
|---|---|---|---|
| 1 | `skills/vlt-setup/assets/governance/_meta/conventions/spec.md:92` | "at zero adoption the `deferral_metric` cannot fire … its only attainable value is 'fine'" — permanent phrasing that `adoption_first_instance:` stamping invalidates per-vault | A7-6 |
| 2 | `skills/vlt-setup/assets/governance/_meta/conventions/spec.md:14` | the frontmatter comment duplicating the same assertion ("# at zero adoption this cannot fire") — the second stale site the capture found | A7-6 |
| 3 | `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:36` | YAML rule 4's tail sweeps `sources:` into the bare-path rule; the filed traverse-vs-verify distinction says the wiki-page `sources:` is a link graph the rule mis-classes | A7-9 |
| 4 | `skills/vlt-ingest/SKILL.md:147` | wiki template placeholder `- <every source that has contributed>` hides the form the convention constrains | A7-10 |
| 5 | `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:218` | "`knowledge-gap` — … a cue for the Researcher" — names a recipient on a rail with no recipient field, drain, or pickup loop (`:215-218`) | A7-12 (other build, listed for completeness) |
| 6 | `skills/vlt-mint/SKILL.md:144` | "A consumer's ack covers its own workflow assets (e.g. `vlt-lint` acks for `vlt-lint-full.js`)" — asserts a reconciliation A7-7 grounded as never happening (the asset is overlay-blind under a current ack) | A7-7 (other build, listed for completeness) |

### (b) New instances found by this audit

| # | file:line | text / claim | why it belongs |
|---|---|---|---|
| N1 | `skills/vlt-setup/SKILL.md:295` | Step-final report line: "the **dynamic workflows** (`.claude/workflows/*.js` — council + lint-full) installed/refreshed" | The module ships **three** workflows — §2a at `vlt-setup/SKILL.md:156-158` installs `vlt-review-council.js`, `vlt-lint-full.js`, **and `vlt-consult.js`** ("copy every `*.js`", `:162`) — the report enumeration fell behind the consult addition; exactly the lists-that-claim-completeness drift CLAUDE.md warns of, in the skill's own honest-surface report line. |
| N2 | `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:238` (and the same phrasing at `:243`) | "`# null/absent = declared-but-not-yet-adopted`" / "null/absent while the class is declared-but-unexercised" — equates the two states | Current source contradicts it: `vlt-upgrade/SKILL.md:112` reads the same key with **three distinct values** — explicit `null` = "declared, no first instance yet", total absence = "**axis not declared**" — and says so in its own text ("which is why the three values are distinct"). Two shipped statements assign different semantics to key-absence; the declaring convention is the stale side. |
| N3 | `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:235` | schema template `deferral_threshold: <numeric tripwire>` | Every shipped instance contradicts the template's own claim: all three live thresholds are prose strings, not numerics (`frontmatter.md:17`, `spec.md:15`, `wiki-consolidation.md:15`). The template asserts a form the file's own frontmatter — four lines up — does not honor; also the reason the class-1 instance could ship unevaluable. |

**Class 2 totals: 6 already-filed sites (4 under the A7-6/A7-9/A7-10 set B7-8 owns + 2 under
other Arc-7 builds) + 3 new = 9 grounded sites.**

Borderline, examined and excluded: the `adoption_first_instance: null # no first live instance
yet` comments (`spec.md:17`, `wiki-consolidation.md:17`, `consult.md:16`, `decision-log.md:16`)
self-heal — stamping replaces the whole line, and the divergence diff excludes that line
(`checks.md:41`) — so the prose can never outlive the state it describes. `frontmatter.md:121`
("the module ships no `.base` file") and `vault-operating-contract.md:86` ("the module ships two"
tool-infrastructure folders) verified true against the shipped tree. `vlt-lint/SKILL.md:11`'s
"every 5–10 ingestions" vs the wire's `>= 10` is advice beside a nag threshold, not a
contradiction.

## Totals

| class | already-filed | new (this audit) | total |
|---|---|---|---|
| 1 — count-since-N without shipped baseline | 1 | **0** | **1** |
| 2 — stale shipped prose | 6 (4 in B7-8's set, 2 in other builds) | **3** | **9** |

## Implication for B7-3's overturn clause

The count-since-N ruling was marked **"overturnable if the sweep shows `frontmatter@5` is the
only instance — a class of one is a fix, not a doctrine,"** and amendment A4 ran this count
precisely so that clause is executable before B7-3 is briefed. The count is now on record:
**class 1 is a class of one** — `frontmatter.md:17` is the only shipped metric whose baseline a
vault cannot read, so the overturn clause's stated condition is **met on its letter**, and
reconsideration of enshrining the principle as frontmatter@6 doctrine (rather than fixing the one
threshold) is plausibly triggered — that reconsideration is the owner's, not this audit's. Two
findings bear on the deliberation without deciding it: first, every *other* shipped counter
already practices the principle (persisted lint reports, log-header baselines, watermarks, the
`adoption_first_instance` stamp), so writing the rule down would codify existing practice rather
than impose new work — the doctrine's cost is one sentence, its class currently one violation;
second, the stale-prose sibling class is **not** a class of one (3 new sites on top of the filed
set, two inside the same `frontmatter.md` Enforcement-declaration section B7-3 will edit —
`:235`, `:238`), so B7-8's sweep remains a real build either way, and B7-3's brief should know
that the enforcement-declaration block it is about to version-bump carries two of the new stale
sites. Nothing in these counts disturbs the *dedicated-build* half of the B7-3 ruling itself,
whose justification (four base edits from four filings, one 5→6 bump, one six-consumer walk) is
independent of either class's size.
