---
title: 'Build #8 — the small-edits batch (recipient-agnostic surfaces, the overlay walk clause, the wiki-index reconciliation, the rail voice rule single-homed, and the full-lint cost instrumented)'
status: 'BUILT 2026-08-24 — all five items landed: F1 vlt-upgrade SKILL.md instance (a) reads "a field vault''s firewall ruling" (grep -rn vlt-core skills/ .claude-plugin/ → ZERO hits); F2 clause (c) "Walk the overlays" appended to the relocation-migration discipline (SKILL.md:75) + overlay_rules_review: schema key inserted after governance_divergence: in the Step-4 block — grep overlay_rules_review → exactly 2 hits (:75 clause, :111 key), persist-verify key-set match picks it up automatically; F3 wiki-index.md:68 hub-row em-dash description deleted (row is now "- [[extraction-methods]] · hub"; grep -c "how grind" → 0), last_updated → 2026-08-24, version: 2 STANDS — no bump, no re-ack, no consumer walk (D2 conditional resolved no-bump); F4 voice rule single-homed as field-contract.md §The voice rule (after Contract version, before the payload field set), vlt-feedback SKILL.md gate paragraph keeps its procedure + gains the enacts-the-voice-rule pointer, issue-triage SKILL.md:19 freestanding restatement became a one-sentence pointer — grep "never writes to the public tracker" .claude/skills/ skills/ → ZERO (no second full statement), rail_contract: 1 unbumped; F5 cost_accounting computed in plain JS in vlt-lint-full.js (budgetSample/costRow/costAccounting helpers; four phase rows — Scan pages, Index pass, Cluster pass, Seeded-pair pass — each {phase, agents_dispatched, model, prompt_chars, tokens_spent} with budget.remaining() deltas guarded on budget.total, null otherwise; top level carries pages_total, budget_total, budget_remaining_at_return, and the agent-side-reads blind-spot note), attached to BOTH returns — findings (beside coverage_caps) and status:failed (with whatever phases had run); convRead / pageScanPrompt ordering / PAGE_SCAN / caps / models / budgetFloor / depends_on header ALL untouched (directions 1–4 stay deferred); F6 full-scale.md step 3 failed-run field list gains cost_accounting (verbatim-from-failed-return), step 4 gains the Cost + churn bullet (cost_accounting surfaced verbatim; churn_since_last_full mtime count vs the most recent prior full-mode report, unwrapped instrument named in the line, operating-contract instrument rule cited by pointer, literal "unmeasured (no prior full report)"), report.md schema gains cost_accounting ("not instrumented (inline run)" literal) + churn_since_last_full (incl. "not measured (scoped run)") beside coverage_caps. VERIFICATION: (1) E6(a) fixture harness (scratchpad harness-build8.mjs, build-5 precedent — stubbed agent/parallel/phase/log/budget, scripted budget total 500000 decrementing 1000/agent, args delivered as a JSON STRING, 4-page fixture) run twice: RUN A completing sweep → findings return carries cost_accounting with phases [Scan pages: 4 agents, haiku, 11176 prompt_chars, 4000 tokens_spent; Index pass: 1, sonnet, 673, 1000; Cluster pass: 1, sonnet, 1290, 1000; Seeded-pair pass: 1, sonnet, 683, 1000], pages_total 4, budget_total 500000, budget_remaining_at_return 493000, note present — all 11 asserts ok; RUN B shortfall sweep (3/4 scans scripted null → below majority floor) → status:failed return carries cost_accounting with exactly the Scan pages row (4 dispatched, 4000 tokens_spent), budget_remaining_at_return 496000 — all 4 asserts ok; HARNESS: PASS. (2) Greps: vlt-core → zero; voice-rule full statement → zero outside the single home (field-contract.md §The voice rule + two pointer sites only); overlay_rules_review → exactly 2 hits in vlt-upgrade SKILL.md; cost_accounting → workflow (:278 failed, :559 findings) + full-scale.md (steps 3, 4) + report.md schema, nowhere restating mechanics; "how grind" → 0 and version: 2 present. (3) Read checks pass: the :68 row conforms to :64 + :74; clause (c) reads as one discipline with (a)/(b); field-contract states the rule whole, both consumers procedure + pointer only. (4) Group E green — no version:/consumers: moved. (5) uv run tools/package-lint.py → "package-lint: A/B/C/E PASS, D SKIPPED — vlt 0.14.0", exit 0. No .decision-log.md artifacts on disk. Deviations: (1) the discipline paragraph''s closing sentence "Both rules hold for every relocation migration" updated to "All three rules hold" — a coherence-necessary micro-edit the brief''s clause-(c) draft implies but does not spell out; (2) instrumentation refactor extracted the index/cluster/pair prompts into named consts/functions (indexPrompt, clusterPrompt, pairPrompt) so prompt_chars is measured on the exact dispatched text — byte-identical prompts, no ask changed; no other deviations.'
module_code: 'vlt'
created: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-24-085505-vlt-upgrade-names-a-real-install-on-shipped-surface.md (A11-8 — the one shipped-surface vlt-core instance)'
  - 'factory/inbox/2026-08-21-150212-wiki-index-row-format-rule-contradicts-worked-example.md (A10-10 — rule-vs-example contradiction)'
  - 'factory/inbox/2026-08-21-181500-rail-triage-arc-surface-candidates.md (A10-15 C3 only — voice-rule single-homing; C1+C2 shipped with B10-7)'
  - 'factory/inbox/2026-08-23-180200-migrations-amend-the-base-but-walk-no-vault-local-overlay.md (A11-5 — clause (c) on the relocation-migration discipline)'
  - 'factory/inbox/2026-08-24-102813-full-lint-cost-scales-with-corpus-not-with-change.md (A11-11 direction 0 ONLY — instrument before optimizing; directions 1–4 deferred to Cycle 12)'
roadmap: 'factory/cycles/11-reachability/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-24): build-8 grouping (five small items batched, A11-5 joined per Q1d); binds D1 (A11-5 row — write-time, clause (c), report-never-auto-edit) and E6 (SPLIT per roundtable A8: (a) instrumentation emits on a fixture run, ship-verifiable, GATES; (b) live measurement, field-contingent); D2 rows — vlt-upgrade SKILL prose no bump, wiki-index.md conditional bump (A15) resolved here; A11-11 deferral rationale (direction 0 is the precondition; anti-direction rides: no sampling, no coverage_caps removal); roundtable A1 (E1(b)''s gating sweep carries this instrumentation live) and A12 (residue grep moved to this brief)'
risk: 'low — no convention version: bump anywhere (the A10-10 conditional resolves to the no-bump branch), no consumer walk, no new finding class; five small surfaces, one of them a shipped workflow edited additively (new return key only, no ask changes, depends_on unchanged)'
---

# Build #8 — the small-edits batch

Five items, each a few lines, batched so none consumes a build slot alone (roadmap
§Grouping & order, build-8): **A11-8** genericizes the one shipped-surface `vlt-core`
instance; **A10-10** reconciles `wiki-index`'s row-format rule with its own worked
example; **A10-15 C3** single-homes the feedback rail's voice rule; **A11-5** adds
clause (c) — the overlay walk — to the standing relocation-migration discipline;
**A11-11 direction 0** instruments the full-lint cost so Cycle 12 decides directions 1–4
on measurement, not the filing's flagged ~4.1 M-token estimate. Every item is the cycle's
through-line in miniature: a name on a surface whose contract is to name nobody, a rule
contradicted by its own example, one rule in two homes, a discipline that protects bytes
but not meaning, and a cost claim nobody has measured.

All rejected alternatives in the parent filings are settled — do not re-litigate. In
particular: A11-11 directions 1–4 are **deferred to Cycle 12 by owner ruling** (Round 1) —
this build performs **no waste removal, no caching, no scanner cards, no prompt
reordering**; the A11-5 lint-class direction is settled write-time by D1; A10-15 C1+C2
shipped with B10-7 and are not reopened.

## Brief-time dispositions

1. **A11-8 wording (roadmap §Questions, build-8 / A11-8): instance (a) reads "a field
   vault's firewall ruling."** The capture's own suggested genericization, adopted as-is —
   the teaching content (ruling recorded in the ledger alone; superseding log entry
   written when next reconciled) is vault-agnostic already; only the name does no work.
   No `version:` bump: `vlt-upgrade` SKILL prose is not a handshaked convention and the
   rule itself does not change (capture A11-8; D2 row confirms).

2. **A10-10 — the example yields to the rule (roadmap §Questions, build-8 / A10-10, added
   roundtable A15): prose clarification, NO bump.** Grounded reading: the section's own
   title is "Row format — structure, not description" (`wiki-index.md:62`); the rule at
   `:64` ("No description, no source count, no date") is load-bearing and enforced —
   `vlt-lint`'s index-drift check (`skills/vlt-lint/references/checks.md:37`; the
   capture's `:35`, trivially shifted) states the index "carries no descriptions, source
   counts, or dates", so shipped enforcement already sides with the prose; and the
   structural-tag definition (`:74`) admits only a role/axis label, a slot `hub` already
   occupies in the contradicting row. Ruling the rule toward the example would be a rule
   change requiring a lint retune, a 2 → 3 bump, a three-consumer walk
   (`vlt-ingest`, `vlt-lint`, `vlt-lint-full.js`), and a migration for every existing
   index — all to legalize a decoration the convention's identity argues against. The
   worked example's hub-row description is deleted instead. **This resolves D2's
   conditional build-8/`wiki-index.md` row to the no-bump branch: `version: 2` stands,
   no re-ack, no consumer walk.**

3. **A11-5 — the drafting recommendation is DROPPED; report-never-auto-edit confirmed
   (roadmap §Questions, build-8 / A11-5, moved from build-2 per Q1d).** The
   predicate-over-territory drafting advice targets overlay-*authoring* practice
   (vault-side, mint-time), a different surface with no filed defect of its own; the
   capture itself grades it "shrinks exposure, doesn't close the walk gap". Carrying it
   would widen a small-edits build into overlay-authoring guidance. Clause (c) closes the
   filed gap; the advice can return by filing if field evidence wants it. The
   **report-never-auto-edit** posture is confirmed and written into the clause verbatim —
   overlays are vault-owned, the same never-write-into-the-agent-zone posture as
   `SKILL.md:49` (D1's A11-5 row: write-time, clause (c), report-never-auto-edit).

4. **A11-5 surfacing shape — hits land under a new Step-4 report key,
   `overlay_rules_review:`.** The capture says hits surface "as a human-gated review
   bullet"; in `vlt-upgrade` the human-gated review surface is the Step-4 post-flight
   report, whose schema block is walked top-to-bottom with per-line never-omit contracts
   (`SKILL.md:95`). A prose-only clause with no report key would be a rule with no
   mechanism — this cycle's own named failure mode. The key is never-omitted-when-empty
   (`[]` = no relocation migration moved a path this run, or the grep found no overlay
   naming an affected path), and flows through the existing persist-verify (key-set
   match, `SKILL.md:125`) automatically.

5. **A10-15 C3 — the voice rule single-homes in
   `skills/vlt-feedback/references/field-contract.md`, not the operating contract.** The
   capture flagged the operating contract as "half-shipped/half-factory work, weaker-fit";
   grounding settles it: both duplicating sites already declare the field contract the
   rail's single home (`skills/vlt-feedback/SKILL.md:19`,
   `.claude/skills/issue-triage/SKILL.md:23` — "Every rail shape … is single-homed at
   `field-contract.md`"), and the voice rule is a rail shape (who may write to the public
   tracker, under what gate). The rule lands there once; both skill sites keep their
   operational instructions and point at it. **No `rail_contract` bump:** the evolution
   rule (`field-contract.md:15-18`) covers payload fields and labels; a prose section
   codifying behavior both consumers already state changes no field, no label, no
   meaning.

6. **A11-11 direction 0 — the instrumentation's two halves and their homes.** Per the
   filing's Direction 0 ("a per-phase accounting line in the workflow's return … likewise
   measure the actual page-change rate between full runs"):
   - **Cost accounting is computed in the workflow, in JS, from facts already in hand** —
     agents dispatched per phase, model per phase, prompt characters summed per phase,
     and per-phase token spend sampled from the runtime `budget` global
     (`budget.remaining()` deltas at phase boundaries when `budget.total` is set; `null`
     when unset, with prompt-chars as the honest fallback estimate). No new agent asks,
     no fs reads, no schema change to `PAGE_SCAN` — pure arithmetic, the B5-3
     facts-not-verdicts posture.
   - **It emits on BOTH return shapes** — the findings return *and* the
     `status: 'failed'` near-total-shortfall return. Roundtable A1 rules that an
     availability-failed sweep's "instrumentation counts as A11-11 measurement evidence";
     an accounting line that dies with the failed run would void exactly that ruling.
   - **Churn measurement is SKILL-side** (`full-scale.md` step 4): the workflow has no
     filesystem access and no memory; the SKILL has both `{lint_reports}` history and the
     live tree. Count pages whose mtime postdates the previous persisted full-run report;
     no prior full report → the literal `unmeasured (no prior full report)` (the
     A10-11 `high_value_gaps: unmeasured` precedent — never an empty value that reads as
     "measured, zero").
   - **The mtime count is exactly D3's instrument-rule class** (a count mechanically
     derived from an external instrument's output — the wrapped `find -newermt` incident
     was this very query). The drafted line instructs an **unwrapped instrument, named in
     the report line**, by pointer to the operating contract's *Honest reporting*
     instrument rule — never restated (build-7's single-home).

7. **A12 residue grep — RUN (roadmap §Questions, build-8 / A11-2's residue grep, moved
   from Cycle 12 by roundtable A12): zero in-class person-name residue on shipped
   surface.** `grep -rn 'mggower\|mikeypioli\|Mikey\|Pioli\|gowermikey' skills/
   .claude-plugin/` returns 8 hits, all dispositioned legal:
   - `.claude-plugin/marketplace.json:4-5,18-19` (author name + email) — the **deliberate
     exception** CLAUDE.md's publishing rules name (public plugin metadata);
     `:8-9` (homepage/repository URLs) — the public repo's own address.
   - `skills/vlt-feedback/references/field-contract.md:49` (`origin:
     mggower/bmad-module-vlt#1` example) and `skills/vlt-setup/assets/module.yaml:74`
     (`default: mggower/bmad-module-vlt`) — **repo-address identifiers, not person names
     on a recipient-facing surface**: the rail's issues must be filed against the real
     public repo (A11-2's own preserved constraint — "the trigger must remain real, not
     prose"), and `mggower` here is the repo path's org segment, the same public address
     marketplace.json already carries. Distinct in kind from A11-2's `@mention @mggower`
     trigger (an instruction to ping a person), which lives in `.github/` and **stays
     deferred to Cycle 12 as ruled**.
   Nothing files forward; no fixes ride build-8 beyond A11-8 itself (whose grep —
   `grep -rn 'vlt-core' skills/ .claude-plugin/` — goes to zero with F1).

8. **R1 (interim posture): not applicable** — every rule this build ships lands with its
   mechanism in the same build (clause (c) ships with its report key; the voice rule's
   gate mechanism already ships at both consumer sites; the instrumentation is the
   mechanism).

## F-sites

### F1 — `skills/vlt-upgrade/SKILL.md:89` — genericize instance (a) (A11-8)

**Current state (re-ground HOLDS at `:89`; build-7's pointer clauses landed at `:37`/`:38`
and did not move this line):** Step 3 item 7's "First two instances of this rule" note,
instance (a): *"the `vlt-core` firewall ruling that should have superseded the decision
log"* — the single shipped-surface hit of the capture's verification grep, shipped into
every vault by the own-the-apply copy.

**Change:** replace the vault name only —

> `(a) the \`vlt-core\` firewall ruling that should have superseded the decision log`

becomes

> `(a) a field vault's firewall ruling that should have superseded the decision log`

Everything else on the line (the `_agent/upgrade-ledger.md` parenthetical, the
written-when-next-reconciled clause) stands — it is already vault-agnostic.

**Why:** a shipped skill must be recipient-agnostic (owner-ruled a defect 2026-08-24;
capture A11-8). Disposition 1. **Out of scope here:** the ~179 factory-record files naming
vlt-core — publish-as-is posture, per the capture's scope guard.

### F2 — `skills/vlt-upgrade/SKILL.md:75` + the Step-4 schema — clause (c), the overlay walk (A11-5)

**Current state (re-ground HOLDS at `:75`):** the standing relocation-migration
discipline carries exactly two clauses — (a) never touch parallel-worktree copies / stub
the old path; (b) re-point open dispatch pointers. No clause visits overlays whose rules
are stated in terms of a moved path — the gap that let the 0.14.0 wiki relocation carry
`{wiki}` out of a vault's `frontmatter.overlay.md` §A scope with no ruling and no report.

**Change (two touches, one mechanism):**

1. At `:75`, append clause (c) to the discipline paragraph, after clause (b):

   > (c) **Walk the overlays.** Any migration that changes what a path resolves to greps
   > `{overlays}/` for the affected path/key and surfaces every hit in the post-flight
   > report's `overlay_rules_review:` line as a human-gated review bullet (overlay file +
   > the section naming the moved path) — **report, never auto-edit**: overlays are
   > vault-owned, the same never-write posture as own-the-apply's overlay rule. A
   > migration that moves a file moves territory an overlay's rules may be stated in
   > terms of; byte-preservation alone does not preserve meaning.

   (Builder drafts to this content at the discipline's own register; the bolded
   report-never-auto-edit and the grep-`{overlays}/` obligation are load-bearing and
   land verbatim in substance.)

2. In the Step-4 schema block (`SKILL.md:96`, the `upgrade:` YAML — insert beside the
   other review-shaped keys, e.g. after `governance_divergence:` at `:112`):

   > `overlay_rules_review: [<overlay: section naming <old path> — path resolution changed by <migration>; review — report-only, never auto-edited>, ...]   # clause (c) hits — never omitted when empty ([] = no migration this run changed a path resolution, or no overlay names an affected path)`

   The persist-verify (`:125`, key-set match) picks the key up automatically — no other
   edit.

**Why:** D1's A11-5 row (write-time, the tightest chokepoint that exists — the module
author at build time); the durability posture protects overlay *bytes* everywhere but
nothing walked overlay *meaning* (capture A11-5). Dispositions 3 and 4.

### F3 — `skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md:68` — the example yields (A10-10)

**Current state (re-ground HOLDS: rule `:64`, example `:68`, tag definition `:74`;
`version: 2`, `consumers: [vlt-ingest, vlt-lint, vlt-lint-full.js]` at `:11-12`):** the
rule says "No description, no source count, no date"; the worked example's hub row reads

> `- [[extraction-methods]] · hub — how grind, time, and pressure shape a cup, split by speed`

— a description by the prose's own definition, with `hub` already occupying the one
permitted tag slot.

**Change:** delete the em-dash trailer; the row becomes

> `- [[extraction-methods]] · hub`

No other row changes (`· slow` / `· fast` are conformant axis labels). Update the base's
own `last_updated:` to the build date. **`version: 2` stands — no bump, no re-ack, no
consumer walk** (disposition 2; D2's conditional row, no-bump branch). `vlt-lint`'s
index-drift text (`checks.md:37`) already matches the rule — untouched.

**Why:** the ambiguity is live inside a shipped check — lint's text sides with the prose
while the example teaches the opposite (capture A10-10, Cycle 10 roadmap). A worked
example is the surface a writer actually imitates; an example contradicting its rule is
the reachability defect in its cheapest form.

### F4 — the voice rule single-homed at `skills/vlt-feedback/references/field-contract.md` (A10-15 C3)

**Current state (re-ground HOLDS):** the rule lives twice —
`skills/vlt-feedback/SKILL.md:77-81` (the approval gate: "Nothing posts without the
gate", exact bytes rendered, HALT) and `.claude/skills/issue-triage/SKILL.md:19-20` ("The
agent never writes to the public tracker unapproved; there is no headless path across the
gate"). The field contract — which both files already name as the rail's single home
(`vlt-feedback/SKILL.md:19`, `issue-triage/SKILL.md:23`) — carries no voice statement at
all.

**Change (three touches):**

1. **`field-contract.md`** gains a short section (after *Contract version*, before *The
   payload field set*), the rule's single home:

   > `## The voice rule`
   >
   > Every write to the public tracker is **human-approved, byte-exact, every time**: the
   > agent renders the exact title, body, and labels that would post, then halts for
   > approval — **nothing posts without the gate, and there is no headless path across
   > it.** This binds every surface of the rail — the filing skill, the factory's triage,
   > and any future writer. Declined material is not posted and not retained.

2. **`vlt-feedback/SKILL.md:77-81`** keeps its operational gate paragraph (the
   render-exact-bytes/HALT mechanics stay — they are the *procedure*, sited where the act
   happens) and gains a pointer clause in that paragraph: the gate enacts **the field
   contract's voice rule** (cite it; restate nothing beyond the procedure).

3. **`.claude/skills/issue-triage/SKILL.md:19-20`** — the freestanding restatement
   becomes a pointer: "…applies the ruled results via `gh` **under the field contract's
   voice rule** (single-homed there; no headless path across the gate)." One sentence,
   no mechanics.

**No `rail_contract` bump** (disposition 5). **Why:** one rule, two homes, zero pointers
was the C3 finding (Cycle 10 roadmap, A10-15); single-home discipline (CLAUDE.md) says
mechanics live in exactly one place. The factory skill edit is legal build scope — the
factory is tracked and public, and `issue-triage` is one of the 9 factory skills.

### F5 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the cost-accounting return key (A11-11 direction 0, workflow half)

**Current state (re-ground — trivial shifts from the filing only):** phase boundaries at
`:160` (`phase('Scan pages')`) and `:248` (`phase('Reduce + cross-page')`); the budget
guard reads `budget.total && budget.remaining()` at `:195`; the failed return
(`status: 'failed'`) at `:233-246`; the findings return at `:455-515` ending with
`coverage_caps` at `:514`; scan fan-out dispatches per chunk at `:203-212`
(`agentFailedSlugs`/`pageUnreadableSlugs` partition); cluster/pair dispatch counts already
surface as `entity_scan_facts` (`:506-511`); models `scanModel`/`indexModel`/
`clusterModel` at `:94-96`. The `// depends_on:` ack header (`:11`) lists the four
conventions the prompts instruct agents to read.

**Change:** add a `cost_accounting` object, computed in plain JS and attached to **both**
returns:

- Sample `budget.remaining()` into a local (e.g. `budgetAt`) at the start of each phase
  and after the last dispatch of each phase (guarded on `budget.total`; `null` spend
  otherwise).
- Accumulate per phase, from values already in hand:
  `{ phase, agents_dispatched, model, prompt_chars, tokens_spent }` — scan phase:
  dispatched = scans + agentFailed + pageUnreadable counts, prompt_chars =
  Σ `pageScanPrompt(p).length` over dispatched pages; index pass: 1 agent, its prompt
  length; cluster pass: `clustersToCheck.length`, Σ cluster-prompt lengths; seeded-pair
  pass: `seededPairs.length`, Σ pair-prompt lengths. `tokens_spent` = the phase's
  budget-delta or `null`.
- Top-level shape:
  `cost_accounting: { phases: [...], pages_total: pages.length, budget_total: budget.total || null, budget_remaining_at_return: <sample or null>, note: 'prompt_chars is workflow-composed prompt text only — agent-side file reads (page + convention bytes) are not visible from JS; tokens_spent is the runtime budget delta where a budget was set' }`
  — the blind spot named in the object itself, per the honest-reporting posture.
- Attach to the findings return (beside `coverage_caps`, `:514`) **and** to the failed
  return (`:233-246`) with whatever phases had run by the failure point (roundtable A1 —
  a failed sweep's numbers are A11-11 evidence).

**Explicitly NOT changed:** the convention read set (`convRead`, `:167-170` — `wiki-index`
stays in it), `pageScanPrompt`'s ordering (`:172-174`), the cluster pass's live-read
instruction (`:369-370`), `PAGE_SCAN`, caps, models, `budgetFloor`, and the
`// depends_on:` header (no new convention ask ⇒ no ack change ⇒ no E5 surface). Those
are directions 1–4, deferred by owner ruling.

**Why:** E6 — the filing's ~4.1 M-token total is its own flagged estimate; direction 0 is
the ruled precondition on every later direction, and E1(b)'s gating sweep carries this
instrumentation live (roundtable A1). Disposition 6.

### F6 — `skills/vlt-lint/references/full-scale.md` (steps 3–4) + `skills/vlt-lint/references/report.md` — the accounting reaches the persisted record (A11-11 direction 0, SKILL half)

**Current state (re-ground HOLDS):** `full-scale.md` step 3 names the failed-run record's
YAML fields; step 4 tells the SKILL to fill report slots and surface `coverage_caps`;
`report.md`'s schema carries `files_listed` annotated `# full mode via the workflow`
(`:13`) and `coverage_caps` (`:71`); neither carries a cost or churn line.

**Change (three touches):**

1. **`full-scale.md` step 3** — the failed-run record's field list gains
   `cost_accounting` (written verbatim from the failed return). One phrase in the
   existing parenthetical list.
2. **`full-scale.md` step 4** — add one bullet: surface the workflow's `cost_accounting`
   **verbatim** in the report, and compute `churn_since_last_full:` — count pages in the
   `pages` list whose mtime postdates the previous persisted full-run report in
   `{lint_reports}` (most recent prior full-mode report, by its dated filename), rendered
   `<N of T pages changed since YYYY-MM-DD (instrument: <the unwrapped instrument that
   ran>)`; with no prior full report, the literal `unmeasured (no prior full report)`.
   The mtime read uses an **unwrapped instrument and names it in the line** — the
   operating contract's instrument rule (*Honest reporting*): **cite it by pointer, never
   restate it** (build-7's single home; this query class — a scoping/enumeration count —
   is exactly what D3's widening put under the rule).
3. **`report.md`** — the schema block gains two lines beside `coverage_caps:` (`:71`),
   both annotated full-mode and never-omitted:
   - `cost_accounting: {phases: [...], ...}   # full mode via the workflow — verbatim from the workflow return; inline/scoped runs render the literal: not instrumented (inline run)`
   - `churn_since_last_full: <N of T pages changed since YYYY-MM-DD (instrument: <name>) | unmeasured (no prior full report) | not measured (scoped run)>`

   The literals follow the `high_value_gaps: unmeasured` precedent — absence must never
   read as "cheap" or "no churn".

**Why:** the return object dies with the session; E6(b)'s live measurement and E1(b)'s
budget-sizing (roundtable A1) both need the numbers in the durable record. **Out of scope
here:** `full-scale.md` step 1 — the `crossLayerSlugs` predicate is build-1's landed
surface; this build touches steps 3–4 only.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row. No convention
`version:` moved (F3 resolves to no-bump; F1/F2 are SKILL prose; F4's home is a skill
reference under `rail_contract`, unbumped) ⇒ no consumer walk, no re-ack. Priced
non-handshake gates: **C6** not touched (no `vault-operating-contract.md` edit — F4
deliberately homes in the field contract instead); **E4** not touched (no new
package-lint check); **E5** not touched (F5 adds no convention ask, `// depends_on:`
unchanged).

## Out of scope (dispositioned)

- **A11-11 directions 1–4** (waste removal, findings cache, scanner cards,
  adjudicated-divergence pairing) — deferred to Cycle 12 by owner ruling (Round 1);
  Cycle 12 prices them against this build's measurements. The anti-direction rides the
  deferral: **no sampling; no `coverage_caps` entry is ever removed to make a run look
  cleaner.**
- **A11-2 proper** (the `@mggower` trigger mechanism in `.github/ISSUE_TEMPLATE/*.yml:17`
  × 3) — deferred to Cycle 12, spike-blocked on `S-3` (harvested 2026-08-24; Cycle 12
  briefs over it). Only its residue grep ran here (disposition 7 — clean).
- **The ~179 factory-record files naming vlt-core** — publish-as-is posture (capture
  A11-8 scope guard; names no path).
- **A11-5's lint-class direction** (overlay-section-naming-a-moved-path heuristic) —
  rejected by D1 (write-time; the cheapest lint class is the one not added, A11-11 being
  this same cycle's cost finding).
- **The predicate-over-territory overlay drafting advice** — dropped (disposition 3);
  returns by filing if field evidence wants it.
- **`full-scale.md:7` / the `crossLayerSlugs` predicate** — build-1's surface; untouched.
- **`wiki-index` in the page-scanner read set** — the filing's own smaller finding, but
  it is direction-1 waste removal; deferred with it.
- **A rule-card / operating-contract restatement of any of the above** — nothing here
  edits the contract; single-home + pointers throughout.

## Verification (unit, at rest)

1. **E6(a) instrument — the fixture harness run (the check of record for acceptance
   check 1).** A factory-side Node harness (the build-5 precedent): load the shipped
   `vlt-lint-full.js` source with stubbed runtime globals (`agent`, `parallel`, `phase`,
   `log`, `budget` with a scripted `total`/`remaining()` sequence), `args` delivered **as
   a JSON string** (the runtime contract), a 3–4 page fixture set with scripted scan
   results. Run twice: (a) a completing sweep — assert the findings return carries
   `cost_accounting` with a row per executed phase, correct `agents_dispatched`,
   non-null `tokens_spent` from the scripted budget deltas; (b) a shortfall sweep
   (scripted nulls below the majority floor) — assert the `status: 'failed'` return
   carries `cost_accounting` too. Record both outputs.
2. **Greps, cross-file agreement:**
   - `grep -rn 'vlt-core' skills/ .claude-plugin/` → **zero** (F1).
   - `grep -rn 'never writes to the public tracker' .claude/skills/ skills/` → the
     single home + pointers only; no second full statement of the voice rule (F4).
   - `grep -n 'overlay_rules_review' skills/vlt-upgrade/SKILL.md` → exactly two hits:
     clause (c) and the schema key (F2).
   - `grep -n 'cost_accounting' skills/` → the workflow (both returns), `full-scale.md`
     (steps 3 and 4), `report.md` (schema) — and nowhere restating mechanics.
   - `grep -c 'how grind' skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md`
     → 0 (F3), and `grep -n 'version: 2' …/wiki-index.md` → still present (no bump).
3. **Read checks:** the amended `:68` example row conforms to `:64`'s rule and `:74`'s
   tag definition; clause (c) reads as one discipline with (a)/(b); the field-contract
   voice-rule section states the rule whole while both skill sites carry procedure +
   pointer only.
4. **Handshake bipartite re-check:** no `version:` moved and no `consumers:` changed, so
   nothing new to verify — still run **`package-lint` Group E** as the check of record
   (it must stay green; a hand grep is not a substitute).
5. **Packaging lint:** mid-cycle `uv run tools/package-lint.py` **A/B/C/E** run, PASS
   recorded. (D/`--expect-version` is build-9's release gate, not this build's.)
6. **R2 (fixture extension): not applicable** — no release-gate check added or changed.
7. **R3 (legal response): not applicable** — no finding class added or changed
   (`overlay_rules_review:` is an upgrade-report review line, not a lint finding class;
   its response is stated in-line: human review, report-only).
8. **R4 (enumeration widening): not applicable** — no file added to any enumerated
   class (no new files at all; the report keys extend schemas that are their own
   enumerations, both edited in the same build).
9. **Scrub:** no personal or vault-local content in any changed shipped file — this
   build *removes* the one known instance; disposition 7's grep is the evidence.

**No Release section:** build-8 is not the release build — v0.15.0's dual bump and
`--expect-version` gate ride build-9.

**Builder exit obligations (target `status:` shape):** rewrite this brief's `status:` to
`BUILT <date> — <what landed>; <verification results incl. the harness outputs and the
Group E / A-B-C-E PASS lines>. Deviations/notes: (1) …` with numbered deliberate
deviations; delete any `.decision-log.md`; one commit for the build.

## Acceptance (live — appended to the roadmap ledger)

1. **`[ship-verifiable]` — GATES closeout (= E6(a), roundtable A8):** the direction-0
   instrumentation exists and emits its cost line on a fixture/at-rest run — the shipped
   `vlt-lint-full.js` returns `cost_accounting` (per-phase agents/model/prompt-chars/
   budget-delta tokens) on **both** the findings return and the `status: 'failed'`
   return; **instrument (R1):** the brief's Verification-1 fixture harness — a
   factory-side Node script with stubbed runtime globals and a scripted budget, `args`
   delivered as a JSON string, run at rest against the shipped workflow source (the
   build-5 harness precedent); **evidence:** the two recorded harness outputs (completing
   + shortfall) in the brief's BUILT status.
2. **`[ship-verifiable]` — GATES closeout:** the four small edits hold at rest —
   `grep -rn 'vlt-core' skills/ .claude-plugin/` returns zero (A11-8); the voice rule is
   stated whole exactly once, at `field-contract.md`, with both consumer sites carrying
   procedure + pointer and no restatement, `rail_contract: 1` unbumped (A10-15 C3);
   `wiki-index.md`'s worked example carries no description and `version: 2` stands —
   no bump, no re-ack (A10-10, the D2 conditional resolved no-bump); clause (c) stands
   at the relocation-migration discipline with its `overlay_rules_review:` schema key,
   report-never-auto-edit stated (A11-5); and `package-lint` A/B/C/E (incl. Group E
   bipartite) passes with nothing moved; **instrument (R1):** the brief's
   Verification-2/3 grep-and-read protocol plus the `package-lint` A/B/C/E run,
   factory-side, at rest; **evidence:** the recorded grep outputs and PASS line in the
   brief's BUILT status.
3. **`[field-contingent]` — does not gate (= E6(b)):** the live full-lint measurement —
   the first owner-run full-mode `vlt-lint` sweep on `{field-vault}` after the v0.15.0
   upgrade persists a report carrying `cost_accounting` (real per-phase spend) and
   `churn_since_last_full:` with a named unwrapped instrument; this is the **same run**
   as E1(b)'s gating sweep, which carries this instrumentation live and sizes its budget
   from it (roundtable A1) — and per A1 an availability-failed run's numbers still count
   as this check's measurement evidence; vault: `{field-vault}` (readable; the filing's
   own 147-page corpus); event: the first post-release full lint (owner-run — scheduled
   by E1(b)'s own discharge need); Cycle 12's directions 1–4 ideation consumes the
   numbers. A second, unbounded tail rides the watch register: the first relocation
   migration in a live vault actually rendering `overlay_rules_review:` with a real hit
   (A11-5's exercise — a fault-shaped event nothing schedules).
