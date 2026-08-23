---
title: 'Build #B9-5 — the factory intake (accepted rail issues become inbox filings — the
  ingress loop closes factory-side, in no release)'
status: 'BUILT 2026-08-21 — all five F-surfaces landed; per A16 NO COMMIT (git status
  clean of tracked changes, verified at build end). F1: Discovery GitHub-intake step +
  Stages-table Location cell + headless `issues_materialized` key (empty-list-when-none
  clause added). F2: `references/github-intake.md` created (query/stale-gate/exclusion/
  materialize/transition + not-owned section; contract cited by line at every shape, zero
  restated tables — pointer-discipline grep clean). F3: Stage 5 "Materialized filings
  close their issue" subsection (criterion unchanged). F4: README §Remote filings archival
  bullet (no labels, no field ids — grep clean). F5 DONE in-session (owner-approved):
  before `gh issue view 1` = OPEN, labels []; after `gh issue edit 1 --add-label
  field:defect,vault-filed,vault-accepted,captured` = OPEN, labels [vault-filed,
  vault-accepted, captured, field:defect]. Verification 2 recorded: before-F5 the
  admitted-open query returned []; after-F5 it lists issue #1, and the decoration-tolerant
  exclusion matched the token at inbox/2026-08-19-155515-...md:4 (`- **origin:**
  `` `mggower/bmad-module-vlt#1` ``) → issue skipped, issues_materialized would be [];
  red probe confirmed a non-tolerant bare-shape grep misses that header. Verification 3
  recorded (scratchpad fixtures, never real inbox/): rail_contract: 0 → stale-shape/
  hand-handling; missing stamp → stale-shape/hand-handling; conforming rail_contract: 1
  body → 8 sections parsed, well-formed temp filing with bare origin: header. Acceptance
  (1) and (2) ship-verifiable checks: PASS, evidence above. Deviations: (1) the F2 query
  adds `createdAt` to the --json field list (the brief''s step-1 literal omitted it, but
  its step 4 requires the issue''s createdAt for the filing timestamp). No other
  deviations. No .decision-log.md existed to delete.'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-19-130120-feedback-loop-is-single-machine-github-issues-as-remote-rail.md
    (A9-4 — build B of D4''s two-build split: the factory-side intake at the two lifecycle
    seams capture confirmed, plus the intake-side reading of the origin: header contract.
    E1–E3 attach to B9-3, not here; E4 is a released standing watch — recorded, not built.)'
roadmap: 'skills/reports/inbox-evolution-arc9-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-20), B9-5 bullet — binds: D4 (build B: intake
  after the rail; labels exist since 2026-08-21, verified live), E1–E4 (all dispositioned to
  B9-3 / watch — none block this brief), roundtable A15 (the four intake rulings a–d; Victor''s
  stale-shape flag; Paige''s single-home move — the siting is B9-3''s, this brief cites it),
  A16 (factory-only, no release, no lint coverage, no commit). Ordering gate satisfied:
  B9-3 BUILT @ 2f1d757, v0.12.0 RELEASED @ 336d90b, all seven labels live on the repo.'
risk: 'low — factory-local only: no shipped surface, no convention touch, no version bump, no
  consumer walk, no package-lint exposure (A16). The risk that exists is lifecycle-shaped, not
  release-shaped: a wrong Discovery exclusion re-materializes or double-captures a filing, and
  a wrong trigger (candidacy instead of admission) lets any stranger mint a mandatory capture
  obligation — both are exactly what A15(a)–(d) exist to prevent, and both are probed at rest.'
---

# Build #B9-5 — the factory intake

B9-3 shipped the rail: the field contract single-homed at
`skills/vlt-feedback/references/field-contract.md` (`rail_contract: 1`), the two issue forms,
the `vlt-feedback` skill, and seven live labels on the transport repo. What does not exist is
the factory's half of the loop: nothing reads the tracker, nothing materializes an admitted
issue into `inbox/`, nothing transitions an issue's state when its filing is captured or its
build ships, and the one hand-materialized case (issue #1 / A9-3) sits OPEN and unlabeled with
no rule saying what becomes of it. This build lands the intake at exactly the two lifecycle
seams capture confirmed (`inbox-capture` Discovery, `arc-closeout` Stage 5) plus the
intake-side reading of the `origin:` header contract — and nothing else.

All rejected alternatives in the parent filing are settled — do not re-litigate. In
particular: the one-build version of D4 (ruled: two builds), any second home for the field
contract (A15/Paige: `field-contract.md` is the single home, B9-3's brief §F3 owns the siting,
this build **cites** it), and materialization-on-`vault-filed` (A15(a): candidacy is not
admission).

## Brief-time dispositions

1. **The roadmap's B9-5 brief-time question is already discharged — recorded, not decided.**
   The §"Questions deliberately left to brief time" entry ("A9-4 / B9-5: where the
   materialized-filing `origin:` header shape is single-homed — capture's candidate
   `inbox/README.md`") was superseded in the same session by roundtable A15/Paige and built by
   B9-3: the shape lives at `skills/vlt-feedback/references/field-contract.md:38-50`
   (`origin: <repo>#<n>`, machine-written by this intake, the idempotency key);
   `inbox/README.md:19-24` and both issue forms are pointers. This brief cites that siting
   (B9-3 brief, dispositions 3/6 and §F3) and adds only the intake-side *reading*. A
   superseding annotation is written at the roadmap's brief-time-questions entry in this run.

2. **The exclusion key is the `<repo>#<n>` token, matched decoration-tolerantly.** A15(d)
   says Discovery excludes any issue whose `origin:` already appears under `inbox/` or
   `inbox/archive/`. The contract's normative machine-written shape is the bare line
   `origin: <repo>#<n>` — but the one pre-rail materialization on disk
   (`inbox/2026-08-19-155515-...md:4`) carries the hand-written decorated form
   `- **origin:** `` `mggower/bmad-module-vlt#1` ``. Ruled: the intake **writes** only the
   bare contract shape (it is the sole writer, per the contract), but Discovery's exclusion
   **matches** by extracting the `<repo>#<n>` token from any `origin:`-labeled header line
   regardless of markdown decoration or backticks. No backfill edit to the A9-3 filing is
   made — rewriting a captured filing's header buys nothing the tolerant match doesn't, and
   the filing's header style is internally consistent as written. (Headless-mode judgment
   call, recorded here.)

3. **Issue #1 is brought onto the rail by an owner label backfill, priced as scope.** Issue
   #1 is OPEN with **no labels** (verified live 2026-08-21) — off-rail, invisible to a
   `vault-filed`/`vault-accepted` query by construction, and therefore never touched by
   Stage 5's new issue-close step when A9-3 eventually archives. Ruled: the build includes a
   one-time **owner action** applying `field:defect`, `vault-filed`, `vault-accepted`, and
   `captured` to issue #1 (F5) so the tracker states what is already true (it was admitted
   and materialized by hand during Arc 9 capture) and the lifecycle's terminal transition has
   a keyed target. Its body carries no `rail_contract` stamp (it predates the contract);
   that is immaterial — exclusion fires before stamp-reading, so the intake never parses it.

4. **The stale-shape flag is a report line, not a finding class.** Per A15/Victor (built into
   the contract at `field-contract.md:15-19`): the intake compares the issue body's
   `rail_contract` stamp against the current contract and, on mismatch **or absent stamp on a
   rail-labeled issue**, reports the issue as **stale-shape, held for hand-handling** — it is
   not materialized, not labeled `captured`, and not parsed hopefully. The legal response
   (hand-handle; the owner decides) is already homed in the contract's evolution rule; the
   intake cites it. No new lint/dispatch finding class ships (see R3, §Verification).

5. **`declined` is the owner's verb; the intake only respects it.** A15(b)'s terminal
   disposition — issue closed with a stated reason, nothing written to `inbox/` — is an
   owner triage action performed on GitHub, not an intake mechanism. The intake's whole
   contact with it: Discovery queries **open** `vault-accepted` issues, so a declined
   (closed) issue is structurally invisible; the mechanics reference states the flow once,
   pointing at the contract's label table rather than restating it.

6. **E4 is recorded, not built.** Community/noise traffic on a public tracker was released
   as a **standing watch** at Round 6 — no build can discharge it; it needs traffic to
   arrive. The mechanics reference names the watch in one line (the intake's
   admission-trigger design *is* the mitigation: an unadmitted stranger filing costs the
   factory nothing mandatory). It enters the arc's carry-forward register at closeout, not
   this build's acceptance checks.

7. **Interim posture (R1): not applicable — this build closes an interim window rather than
   opening one.** B9-3 shipped the label rules and the contract ahead of their factory
   mechanism; B9-5 is that mechanism. Nothing here ships a rule, check, or finding class
   ahead of its own mechanism.

## F1 — `.claude/skills/inbox-capture/SKILL.md`: Discovery gains the GitHub-intake step

**Current state:** Discovery (`SKILL.md:49-72`) lists `inbox/*.md`, resolves the open arc
roadmap, and confirms coverage with the user. It knows nothing of the tracker. The Stages
table (`:76-80`) routes Discovery → Grounding → Synthesis; the headless JSON contract
(`:42-44`) emits `filings_captured` only.

**The exact change:**
- Insert a short **GitHub intake** step at the top of Discovery (before the `inbox/*.md`
  listing, so a freshly materialized filing joins the same run's un-captured set): one
  paragraph that (i) names the transport repo (read `feedback_repo.default` from
  `skills/vlt-setup/assets/module.yaml:64` — the factory reads the module source default;
  it has no vault `config.yaml`), (ii) routes to `references/github-intake.md` for the
  mechanics, and (iii) states the one-line invariant inline: *materialization is triggered
  only by the owner-applied `vault-accepted` label — `vault-filed` marks candidacy, not
  admission (A15(a)); the field contract, labels, and `origin:` header shape are single-homed
  at `skills/vlt-feedback/references/field-contract.md` — point, never restate.* Degrade
  loudly: if `gh` is unavailable/unauthenticated, say so by name and continue with the
  filesystem-only Discovery (the intake half is skipped, never silently "empty").
- Stages table: no new stage — the intake is part of Discovery; add
  `references/github-intake.md` to Discovery's Location cell (or an adjacent routing line),
  matching the carved-reference pattern already used for Grounding/Synthesis.
- Headless JSON contract: add `"issues_materialized": ["<repo>#<n>", ...]` (empty list when
  none), so a headless run's materializations are visible in its one-line output.

**Why:** D4 build B — the first of the two confirmed lifecycle seams. The invariant sits
inline because it is the safety property (A15(a)); everything else is carved to F2.

**Out of scope here:** no change to Grounding or Synthesis — a materialized filing is an
ordinary inbox file from the moment it lands, which is precisely the design (capture stays
the airlock; everything keyed off inbox files stays untouched, per the A9-4 grounding).

## F2 — `.claude/skills/inbox-capture/references/github-intake.md` (NEW): the intake mechanics

**Current state:** does not exist. `references/` holds `grounding-methodology.md` and
`roadmap-synthesis.md`; this file joins them as Discovery's carved half.

**The exact change:** a self-contained mechanics reference (don't assume SKILL.md is in
context), carrying — as mechanics, with the contract cited for every shape:

1. **Query.** `gh issue list --repo <feedback_repo> --label vault-accepted --state open
   --json number,title,labels,body` — admitted, open, not yet captured. State why this
   query is the trigger: A15(a) (owner-applied admission), A15(b) (declined issues are
   closed → invisible), and the contract's state flow (`field-contract.md:67-69` — an
   issue without `vault-filed` is off the rail entirely; one already labeled `captured`
   is reported, not re-materialized, if it appears).
2. **Stale-shape gate (before any parse).** Read the body's `rail_contract` stamp; compare
   to the current contract version (`field-contract.md:12`). Mismatch or missing stamp →
   report the issue as **stale-shape, held for hand-handling** and stop for that issue: no
   materialization, no label change. Cite `field-contract.md:15-19` for the evolution rule
   and its legal response. (A15/Victor; disposition 4.)
3. **Idempotence exclusion.** Build the key `<repo>#<n>`; grep `inbox/*.md` **and**
   `inbox/archive/*.md` for an `origin:`-labeled header line carrying that token,
   decoration-tolerant (bare `origin: <repo>#<n>` or a markdown-decorated variant —
   disposition 2 names the one live decorated instance). A hit → the issue is already
   materialized: skip it, and if it lacks the `captured` label, report the label drift
   (offer the one-line `gh issue edit <n> --add-label captured` fix) rather than
   re-materializing. (A15(d).)
4. **Materialize.** Parse the eight `### <field_id>` sections per the contract's field
   table (`field-contract.md:27-36` — cite, never restate the table). Write
   `inbox/YYYY-MM-DD-HHmmss-<slug>.md` (timestamp = the issue's `createdAt`, slug from the
   title — matching `inbox/README.md`'s filename convention) with the machine-written
   header line `origin: <repo>#<n>` (bare contract shape — the intake is the only writer,
   `field-contract.md:47-50`), the origin vault, kind, and the body content. The filing is
   raw field signal: materialization does **not** ground it — that is Capture's next stage,
   unchanged.
5. **Transition.** Apply `captured` via `gh issue edit <n> --add-label captured` (A15(c)).
   The issue stays **open** — it closes at archival, not at capture (F3). Report each
   materialization (issue → filing path) in the run's output.
6. **What this file does not own** (stated, with pointers): admission (`vault-accepted`)
   and decline (`declined` + close-with-reason) are **owner triage verbs** performed on
   GitHub (disposition 5); the label vocabulary and state flow live in the contract; the
   E4 noise watch is named in one line per disposition 6.

**Why:** A15's four rulings need a mechanics home; the contract explicitly assigns
"state-transition mechanics" to the factory intake (`field-contract.md:54-55`), and B9-3's
brief (§Out of scope 1) hands exactly this set here.

## F3 — `.claude/skills/arc-closeout/references/closeout-checklist.md`: Stage 5 gains the issue transition

**Current state:** Stage 5 (`closeout-checklist.md:84-113`) archives accepted filings by
`mv` into `inbox/archive/`, under the per-filing criterion (both conditions at `:99-102`).
It knows nothing of a filing's remote origin: a materialized filing archives and its issue
stays open and labeled forever — the exact re-materialization / stale-state hazard A15
names.

**The exact change:** append a short subsection to Stage 5 (the archive criterion itself is
**unchanged** — this extends the *act* of archiving, mirroring the `mv`):

> **Materialized filings close their issue.** A filing being archived whose header carries
> `origin: <repo>#<n>` (see the field contract at
> `skills/vlt-feedback/references/field-contract.md` — the single home; point, never
> restate) gets its issue closed in the same stage:
> `gh issue close <n> --repo <repo> --comment "<shipped version/build + one-line
> disposition>"`. The `captured` label stays (history, and the `origin:` header remains the
> idempotency key either way). A filing that **stays active** (live carry-forward) leaves
> its issue **open** — the tracker mirrors the inbox, in both directions. If `gh` is
> unavailable, record the owed close in the closeout report rather than skipping silently.

**Why:** D4 build B's second seam; A15's state-transition gap ("nothing rules the label's
state transitions… a `vault-filed` issue stays open and labelled across arcs"). The
filesystem archive already has a bell (this checklist); the remote mirror now rings it too.

**Out of scope here:** no change to Stages 1–4, 6; no change to `acceptance-discharge`
(when it moves a filing early, Stage 5's "catches stragglers" pass still runs and now also
catches the un-closed issue — one home for the transition, deliberately).

## F4 — `inbox/README.md`: the archival clause joins the Remote filings pointer

**Current state:** `inbox/README.md:19-24` (§Remote filings, shipped by B9-3) points at the
contract for payload/labels/`origin:` and states that a materialized filing carries the
header. Its Lifecycle step 4 (`:16-17`) describes archival with no remote mirror. B9-3's
brief (§F—README, "Why") explicitly left this extension to B9-5.

**The exact change:** one added bullet in §Remote filings:

> - When a materialized filing archives (its build shipped and passed acceptance), the
>   factory closes its issue — and a declined issue is closed at triage with a reason,
>   nothing materialized. Mechanics: `inbox-capture`'s github-intake reference and
>   `arc-closeout` Stage 5; vocabulary: the field contract (same home as above).

**Why:** the front door should state the full loop in pointer form; without it, a
contributor watching their issue has no stated expectation of when it closes.
Pointer-discipline check: the bullet names no labels and no field ids.

## F5 — Owner action (build-time): bring issue #1 onto the rail

**Current state:** `mggower/bmad-module-vlt#1` is OPEN, zero labels (verified live
2026-08-21). Its filing `inbox/2026-08-19-155515-tripwire-metrics-have-no-durable-vault-local-home.md`
carries the decorated `origin:` header at `:4` and is **captured as A9-3** (build B9-6,
v0.13.0 — so it archives no earlier than Arc 9's B9-6 acceptance, likely Arc 10).

**The exact change:** the builder stages and the **owner runs** (or approves in-session):

```
gh issue edit 1 --repo mggower/bmad-module-vlt \
  --add-label field:defect,vault-filed,vault-accepted,captured
```

The issue stays open — A9-3 is captured, not archived. Record the before/after
`gh issue view 1 --json labels` in the BUILT record.

**Why:** disposition 3. Reconciliation, not machinery: the tracker comes to state what Arc 9
capture already did by hand, and Stage 5's new transition has its keyed target when A9-3
eventually archives. Without this, the arc's one real issue is permanently invisible to the
very intake it prototyped.

## Registration

**None.** No shipped skill, no `module-help.csv` row, no `marketplace.json` entry, no
convention edit, no version bump, no consumer walk. R1-pricing of the non-handshake gates
(roundtable R1): **none apply** — no governance-bundle edit (no C6 re-derivation), no new
`package-lint` check (no E4 harness case), no asset-node ack (no E5). Per A16 the build also
produces **no commit and no release content**; `package-lint` never sees any of it (all five
F-surfaces are gitignored — `.claude/`, `inbox/` — verified by the roadmap's
`git check-ignore` record).

## Out of scope (dispositioned)

1. **Everything B9-3 shipped** — the contract, forms, labels, `vlt-feedback`, transport
   config: BUILT @ 2f1d757; this build cites `field-contract.md` and edits none of it.
   Additive contract evolution (new fields without a bump) needs no intake change by design.
2. **E4 (community/noise traffic)** — released standing watch, disposition 6; carried
   forward at closeout, no build can discharge it.
3. **E1–E3** — attached to B9-3 as `[field-contingent]` with named events; B9-5's checks are
   about ingest correctness, not whether the rail's assumptions held (Round 6 disposition,
   verbatim).
4. **Backfilling the A9-3 filing's header to the bare contract shape** — rejected,
   disposition 2: tolerant matching covers it; the sole-writer rule governs future writes.
5. **`vlt-lifecycle.md` step-1 row wording** ("owner relays for vaults without inbox
   access") — left untouched: still true as written; the rail is the additional route and
   is documented at the front door (F4). A freshness edit here would widen scope for zero
   mechanism.
6. **Automating owner triage** (auto-accept heuristics, scheduled Discovery runs) —
   rejected-because: A15(a)'s entire point is that admission is a human act; a one-person
   factory's protection is the trigger, not throughput.

## Verification (unit, at rest — lifecycle step 5)

No handshake moved and no shipped file changed → **no Group E run owed, no mid-arc
package-lint run owed (A16 — lint cannot see these files), no scrub surface** (nothing
ships; still: the materialization mechanics quote no vault-local literals, and the worked
example in F2 uses the placeholder `<repo>#<n>`, with issue #1 permitted as the one live
citation since the repo is public).

1. **Pointer-discipline grep:** neither new/edited factory file restates the contract's
   field table or label table — grep the four edited/created files for `what_happened`,
   `origin_vault`, `vault-accepted`-style enumerations beyond the single inline invariant
   F1 carries; every mechanics step in F2 cites `field-contract.md` by line.
2. **Discovery dry-run against the real repo (recorded):**
   `gh issue list --repo mggower/bmad-module-vlt --label vault-accepted --state open` —
   **before F5**: empty (issue #1 is off-rail, invisible by construction — the A15(a)
   invariant observed live); **after F5**: issue #1 appears, and the exclusion step must
   then skip it by the origin token matched against
   `inbox/2026-08-19-155515-...md:4` (the decorated form — the probe that could fail: a
   non-tolerant grep misses it and the dry-run wrongly proposes re-materialization). Record
   both runs — this is the red-then-green shape for exclusion rule (d).
3. **Stale-shape probe (fixture, not a real issue):** run the F2 gate against a temp
   fixture body with `rail_contract: 0` and against one with no stamp — both must route to
   stale-shape/hand-handling, neither to materialization. Against a conforming
   `rail_contract: 1` fixture body, the parse yields the eight sections and a well-formed
   filing in a temp dir (never the real `inbox/` during verification).
4. **Stage 5 walkthrough (paper, plus grep):** the closeout-checklist addition names close,
   comment, label-stays, stays-active-stays-open, and the gh-unavailable degradation; grep
   confirms it points at the contract and adds no second criterion sentence.
5. **R3: not applicable as a new class** — the stale-shape flag's legal response is homed in
   the contract's evolution rule (`field-contract.md:15-19`), cited not restated
   (disposition 4). **R4: not applicable** — the new reference file joins no shipped or
   enumerated class (factory `.claude/skills/` files are outside every manifest and vital;
   materialized filings are ordinary inbox files, a class `inbox/README.md` already
   describes without enumeration).

No Release section: B9-5 ships in no version (A16); no bump, no gate, no tag rides it.

## Acceptance (live — appended to the roadmap ledger)

**Ledger home, stated per A16/A20:** the ledger partitions by release and B9-5 is in
neither — its bullet sits under a third, explicit heading **[factory-local — no release
run]**. Its ship-verifiable checks discharge **at rest on the factory machine**; they can
gate Arc 9 closeout (they depend on no v0.13.0 event, so Dispute 3's bound is untouched).

1. **`[ship-verifiable]` — the intake exists, is safe, and excludes correctly, at rest:**
   (a) all four file surfaces landed (F1 Discovery step + JSON key, F2 mechanics reference,
   F3 Stage 5 transition, F4 README clause) with the pointer-discipline grep clean;
   (b) the recorded double dry-run of Verification 2 — empty before the F5 backfill,
   issue #1 listed-then-excluded by the origin token after it — plus the recorded
   stale-shape fixture probes (Verification 3). Discharges when the BUILT record carries
   the recorded runs; each probe is one that could have failed.
2. **`[ship-verifiable]` — issue #1 reconciled:** `gh issue view 1` shows
   `field:defect,vault-filed,vault-accepted,captured`, state OPEN (A9-3 is captured, not
   archived); the before/after is in the BUILT record. Owner action, bound **in-build**.
3. **`[field-contingent]` — first real end-to-end materialization**, event named per
   R5/A20: **the issue produced by B9-3 check (3)'s bound event (the owner's `vlt-feedback`
   run from the work machine's app-vault, bound before Arc 9 closeout) is owner-triaged
   `vault-accepted`, and the next `inbox-capture` run materializes it** — filing lands in
   `inbox/` with a bare `origin:` header, `captured` applied, issue left open, and the
   stamp check passes on a genuine `rail_contract: 1` body. Vaults: app-vault produces the
   issue; the factory materializes. Rides B9-3's existing bound — no new unscheduled event
   is created. Does not gate closeout. *(The terminal half — Stage 5 closing an archived
   filing's issue — first fires when a materialized filing archives, no earlier than that
   filing's build ships and passes acceptance; named here, unbounded by nature, watched
   not gated.)*
