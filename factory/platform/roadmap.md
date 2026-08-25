# Platform roadmap — the off-cadence channel

**Stood up 2026-08-21** as the inaugural act of the brainstorm it came from
(`_output/brainstorming/brainstorm-lifecycle-triage-and-platform-channel-2026-08-21/` —
memlog + keepsake are the design record). This ledger is cycle-less, kanban-style,
**never archived, never gates a release**. Born a gitignored dev artifact in
`skills/reports/`; tracked and public at `factory/platform/roadmap.md` since P-7/P-8
(2026-08-23).

## The channel contract (single-homed here until it earns a CLAUDE.md pointer)

- **Boundary — delivery, not topic:** an item is *platform* iff `vlt-upgrade` does not
  deliver it to vaults. Factory skills (`.claude/skills/`), `tools/`, process docs, this
  ledger — platform. Anything under the shipped surface (`skills/vlt-*`,
  `.claude-plugin/`) belongs on the **arc roadmap**, no exceptions.
- **Cadence separates; discipline doesn't.** Platform items keep grounding and at-rest
  verification; they drop only the release train. Each item gets a **brief-lite**
  (5 lines, inline below: intent / sites / verification / out-of-scope / done-when) —
  no `build-N` brief file.
- **Numbering & commits:** items are `P-N`. Commits carry a `plat:` subject prefix,
  land on `main` anytime, bump no version, join no acceptance ledger. (Most platform
  surface is gitignored — a `plat:` commit exists only when an item touches tracked
  files like `tools/`, `.github/`, or CLAUDE.md.)
- **Self-acceptance:** an item closes when the changed skill/tool is exercised once by
  a real lifecycle run. No closeout ceremony; record the exercising run's date on the
  item.
- **WIP limit 2.** New items queue below the line. The channel is a rail, not a second
  roadmap.
- **Skill budget:** the channel adds at most **one** new factory skill ever
  (`issue-triage`); all other platform work extends existing skills/tools.
- **Visibility floor:** each cycle-closeout notes "platform work landed during this
  cycle: P-…" in the closeout record — visibility without coupling.

### Enforcement debt (open, unblocked 2026-08-21 by the channel's first self-acceptance)

- Mechanical boundary check (D6 spirit): a `plat:` commit touching `skills/vlt-*` or
  `.claude-plugin/` should fail `package-lint`. Until built, the boundary is
  honor-system — flag any breach here.
- ~~CLAUDE.md pointer to this ledger (one line, point-at-the-map).~~ **DISCHARGED
  2026-08-24** — one line above CLAUDE.md's Standing rules section, owner-prompted.

---

## Active (WIP 1/2)

### P-10 — the loop, visible — **open: BUILT 2026-08-23, awaiting self-acceptance (Cycle 12's milestone + build issues generated, not typed — re-bound 2026-08-25)**

**Build record (2026-08-23):** `issue-triage` gained its second mode — **'sync the
tracker'**, mechanics single-homed at the new
`.claude/skills/issue-triage/references/tracker-sync.md`: milestone `Cycle NN — <Title>`
per open cycle, issue `B<NN>-<i> — <slug>` per ruled build, one `stage:` label per
lifecycle position (7-rung ladder derived from the map's observables), the acceptance
ledger as a task list with `check:ship-verifiable`/`check:field-contingent` labels,
inherited debt re-milestoned never recreated. **One direction writes** (disk → tracker);
the rail population is disjoint by construction (factory-authored `B<NN>-<i>` titles vs
filer-authored `vault-filed`) — elimination, no precedence statement. Every apply passes
the same owner batch gate as triage. Bootstrapped live: all 9 `stage:`/`check:` labels
on the tracker (documented in the reference, config.yml-style, NOT in the field
contract); pinned issue #9 "How this project evolves"; `.github/PULL_REQUEST_TEMPLATE.md`
(build ID + brief + build-issue links). factory-paths-check PASS (110 refs, 20 files).
**Process note:** third queue-jump while WIP reads 2/2 (P-2 open, P-8 built-awaiting) —
owner-directed, seam-bound, flagged as before.

*(Original adoption block: same as P-7.)*

**Brief-lite:**
- **Intent:** stop the roadmap doing by hand what a milestone and a label set do for free.
- **Sites:** extend `issue-triage` with one-way roadmap → GitHub sync (milestone per cycle, issue
  per build, `stage:` labels, ledger as task list); `.github/PULL_REQUEST_TEMPLATE.md` (build ID +
  brief link); a pinned "How this project evolves" issue; new `stage:` and `check:` labels
  bootstrapped the way `config.yml` documents the field-contract labels.
- **Verification:** one real cycle opens with its milestone and build issues **generated, not
  typed**; the roadmap file and the tracker never diverge because only one direction writes.
- **Out of scope:** flipping source-of-truth to issues (a later item, only if this proves out);
  **any change to the field contract or its labels** (shipped surface → arc roadmap, and a
  `rail_contract` bump).
- **Done-when:** the open cycle's roadmap is readable as a milestone by someone who never
  opens a file. *(Amended 2026-08-25, owner-ruled: the clause read "Cycle 11's roadmap" and
  became **unsatisfiable** when Cycle 11 closed 2026-08-25 with zero milestones ever created —
  `gh api repos/:owner/:repo/milestones` empty, no `B11-<i>` issues, every tracker issue
  filer-authored and unmilestoned. Under `acceptance-discharge`'s rubric that is not a waiting
  state but **BLOCKED (unreachable)** — no future event satisfies a sentence naming a closed
  cycle — so the owner re-bound it rather than let a dead clause hold a slot. The subject is now
  the open cycle, not a numbered one, so a missed window re-binds itself instead of needing this
  ruling again. Retro-projecting the closed Cycle 11 was rejected: it satisfies the letter and
  misses the verification's point, which wants a **live** cycle legible on the tracker.)*

**Sequencing (recorded 2026-08-25).** `tracker-sync` mints `B<NN>-<i>` issues per **ruled**
build, so it cannot produce them until ideation has numbered the builds. The discharge path is:
`inbox-capture` opens Cycle 12 → `ideation-scaffold` + owner rulings number the builds →
`sync the tracker` (owner batch gate) → that run **is** the self-acceptance; record its date
here. Only the third step is new work.


## Queued

### P-3 — channel plumbing: platform lane, intake route, closeout hook — **queued**

**Brief-lite:**
- **Intent:** close the three structural gaps the untracked-ideas sweep found
  (2026-08-21): the instrument panel is blind to the channel, candidates reach the
  queue only by hand, and the visibility-floor contract line has no mechanism.
- **Sites:** `vlt-lifecycle.md` gains platform observable rows (open/queued P-items
  from this ledger's headings — cheap heading reads, per lifecycle-status's doctrine);
  `factory/inbox/` filings gain an optional `channel: platform` marker and
  `inbox-capture` routes marked filings to this ledger's Queued section instead of the
  cycle roadmap (one intake, two destinations); `cycle-closeout` gains the one-line
  "platform work landed during this cycle" step the contract already promises.
- **Verification:** a `lifecycle-status` run reports the channel positions; a fixture
  filing with `channel: platform` routes to Queued, not the roadmap; grep cycle-closeout
  for the visibility line.
- **Out of scope:** any automated candidate detection (agent-initiated platform
  filings stay a brainstorm future); spike rows (P-2's).
- **Done-when:** one real lifecycle-status run shows the platform lane and one real
  capture run exercises the routing fork (or reports no marked filings).

### P-5 — citation resolution: make grounding checkable — **queued**

*(Queued 2026-08-23 from the eval brainstorm
(`_output/brainstorming/brainstorm-vlt-eval-harness-2026-08-23/`) and its ROI count
(`factory/cycles/10-signal-integrity/eval-roi-count-2026-08-23.md`). Routed here, not inbox: the fix site is
`tools/` — `vlt-upgrade` never delivers it. Filed separately from P-6 because it is a
class of one, independent of both the check suite and any fixture, and carries the
corpus's single worst instance.)*

**Brief-lite:**
- **Intent:** close the hole the `171500` filing names in its own words — *"No step in
  the loop re-reads a filing to check what a brief said about it, so the inversion was
  never checkable in principle."* A brief restated a field calibration with its polarity
  **inverted**, and it survived a brief, a build, unit-verification at rest, a release
  lint, a tagged release, six acceptance passes and a graded acceptance clause — caught
  only when a spike re-read the source filing 14 days later. CLAUDE.md states the
  grounding discipline twice; nothing mechanically enforces it.
- **Sites:** new `tools/citation-check.py` — walk every `file:line` citation in
  `factory/cycles/*/{roadmap.md,briefs/*.md}` (briefs + roadmaps), assert the path
  resolves, the line exists,
  and where the citing text carries a quotation the cited line contains it verbatim;
  wired as a new `package-lint.py` group so it rides the existing stage-4 gate rather
  than adding a second gate; `build-brief`'s verification section gains a pointer to it.
- **Verification:** red-then-green against the historical inversion — reconstruct
  `build-20`'s pre-repair sentence from the `171500` filing's cited chain if the live
  text is already fixed — then a full-tree run with the output triaged (expect real
  reds; they are the point).
- **Out of scope:** citations into shipped surface prose (`skills/vlt-*`) — briefs and
  roadmaps only for the first cut; semantic paraphrase checking (exact substring only,
  no model); auto-fix; the polarity/inversion *judgment* itself, which stays human.
- **Done-when:** one real `build-brief` run cites the check in its verification section,
  and the check runs clean or with triaged known-reds recorded here.

**Note:** `tools/` is tracked, so this lands as a `plat:` commit (unlike P-4, which
touched only gitignored surface).

### P-6 — the deterministic check tranche: four classes, eleven historical instances — **queued**

*(Queued 2026-08-23 from the same ROI count. Scoped deliberately: the count found nine
recurring deterministic classes, and this item takes only the four that need no design
argument. See Out of scope for the three deferred and why.)*

**Brief-lite:**
- **Intent:** the ROI count classified all 98 filings and found **35 deterministically
  catchable at commit time with no model** (54% of the real defect population of 65).
  Those 35 collapse into nine recurring classes — and **two of them are already written
  in CLAUDE.md as standing rules that nothing enforces** ("lists that claim completeness
  drift"; no personal or vault-local content on shipped surface). Extend `package-lint`;
  build no runner and no skill (the channel's skill budget is spent).
- **Sites:** `tools/package-lint.py` gains four checks — (a) **list-vs-source-map
  completeness**: hardcoded path/slug lists ⊇ their `vault_structure` source (rows 82,
  89, 67 — and the *live* instance: today's 0.14.0 discharge failed B10-2(5)/B10-12(6)
  on 12/12 `crossLayerSlugs` missing-target false positives); (b) **declared field has no
  producer**: every key a report or detector declares is written by ≥1 producer site
  (rows 23, 53, 88); (c) **byte budgets** on shipped files and agent prompt schemas (rows
  62, 95 — the `95` filing already prescribes exactly this: *"a standing schema budget …
  and a package-lint check holding the line"*); (d) **personal or vault-local content on
  shipped surface** (row 97 + the `091001` path leak). `tools/test-package-lint.py` gains
  a case per new group — non-negotiable, per row 33, where the harness sat silently red
  for three builds because a new group shipped without one.
- **Verification:** each check gets a **red fixture built from its own historical
  instance** (rows named above) — red-then-green per check, so no check lands green-only;
  full `test-package-lint.py` green before any check counts as landed.
- **Out of scope:** the three classes needing real design work before they can be
  briefed — *site A promises what site B does not do* (5 instances, but mechanically
  detecting a "promise" is unsolved), *stale self-referential claim* (3, semantic), *rule
  contradicts its own worked example* (2, semantic). They stay in the ROI count's class
  table and may become P-7 once (a) is built and the pattern is clearer. Also out: the
  **T3 behaviour tier and `fixtures/vaults/`** (19 cases — needs a fixture vault and
  model runs; a later item, and only once this tranche proves the approach);
  `--emit-cases` or any separate eval runner (unnecessary once the checks live in
  package-lint); the `repro:` field on the field-defect issue form and `vlt-upgrade`
  pre-apply refusal (both shipped surface → **arc roadmap**, not here).
- **Done-when:** the four checks land with red fixtures, `test-package-lint.py` is green,
  and one real `vlt-release` run carries the widened PASS line.

**Folds in existing enforcement debt.** The header's open item — *"a `plat:` commit
touching `skills/vlt-*` or `.claude-plugin/` should fail `package-lint`"* — is the same
family as check (d) and should land in this item's tranche rather than stay loose.

### P-11 — widen factory-paths-check to the factory's live surfaces — **queued**

*(Queued 2026-08-24 off the going-public review (`review-going-public-2026-08-24.md`,
F3's follow-on): the path gate born in P-8 scans only the 9 factory skills + the map +
CLAUDE.md — `tools/factory-paths-check.py` SCAN_FILES covers no `factory/` file at all,
which is exactly why F3's dead paths in this ledger's live entries survived to a
fresh-eyes review. A blind widening would go red on history: closed cycles' roadmaps
and this ledger's closed records quote retired paths by design.)*

**Brief-lite:**
- **Intent:** the gate should cover every surface whose paths are *promises* (live
  instructions) while never flagging surfaces whose paths are *history* (closed
  records). Make that distinction explicit and mechanical.
- **Sites:** `tools/factory-paths-check.py` — SCAN_FILES gains the live factory
  surfaces: `factory/method/*.md`, `factory/inbox/README.md`, `factory/CYCLE`, the
  open cycle's `roadmap.md` (via the CYCLE pointer; skipped when `none`), and this
  ledger **section-aware** (Active + Queued entries scanned; the channel contract
  header scanned; `## Closed` records excluded). Closed cycle directories stay
  entirely out of scope.
- **Verification:** red-then-green from F3's own corpus — reconstruct one of its dead
  paths (e.g. the pre-fix `skills/reports/spikes/` line) in a fixture ledger and watch
  the widened check catch it; then a full-tree run green; confirm a deliberately
  planted old path inside a `## Closed` record is NOT flagged.
- **Out of scope:** scanning closed cycles' contents; quotation/citation checking
  (P-5's `citation-check.py` owns `file:line` assertions); any factory skill edits.
- **Done-when:** the widened check is green on the live tree, the F3-class fixture is
  red-then-green, and one real run rides a lifecycle transition (capture or closeout)
  as its self-acceptance.

### P-12 — require PRs into `main` (choreography-aware) — **queued**

*(Queued 2026-08-24, owner-raised at the going-public closeout. The trivial half
shipped same day, outside any item: branch protection on `main` now blocks force
pushes and deletion and **requires linear history** (the ff-merge discipline,
server-enforced; `enforce_admins: true`). What remains is the design half — the owner
wants **everything** to reach `main` via a PR, and that collides with two live
workflows: `vlt-release` Stage 6 ff-merges and pushes `main` directly, and `plat:`
commits land on `main` directly. Flipping the protection on without redesigning those
would brick the next release at its final stage.)*

**Brief-lite:**
- **Intent:** every change to `main` arrives as a PR — review surface, CI hook point,
  and the just-shipped PR template (build ID + brief + build-issue links) actually
  exercised, closing the loop P-10 opened.
- **Sites:** `.claude/skills/vlt-release/references/choreography.md` Stage 6 (ff-merge
  + push → push the cycle branch, open a PR via `gh pr create --fill` against the
  template, merge it — linear-history-compatible merge mode ruled at build time:
  rebase-merge vs. merge-commit-with-linear-history-off is the design call); the
  `plat:` commit convention in this ledger's contract header (platform work lands on a
  short-lived branch + PR); the branch-protection rule itself gains
  `required_pull_request_reviews` (0 approvals — solo maintainer; the PR is the
  record, not a gate on another human) once both workflows are converted.
- **Verification:** one real `plat:` change lands via PR with the template filled;
  the branch-protection API state matches the ruled config; a `vlt-release` dry walk
  of Stage 6 confirms the choreography's commands agree with the protection.
- **Out of scope:** required status checks / CI (nothing runs in Actions yet — a later
  item can wire package-lint there); protection on the private mirror.
- **Done-when:** the next release reaches `main` through a PR without breaking the
  choreography's gate sequence, and direct pushes to `main` are refused server-side.

### P-13 — say "the roadmap's foot", not "the report": disambiguate the terminal-restamp obligation — **queued**

*(Filed 2026-08-24, from a lifecycle-status flag: the v0.15.0 release run updated the
Cycle 11 roadmap's frontmatter but wrote no foot restamp — the roadmap had **zero**
`Next lifecycle move` stamps across its whole lifecycle, where Cycles 9/10 carry 2–3.
Mechanical cause: `vlt-release` choreography Stage 8 says "End the **report** with the
Next lifecycle move", and "report" resolved to the chat report only. The instance was
repaired by hand the same day; this item closes the recurrence path.)*

- **Intent:** every lifecycle skill's text says explicitly that the terminal routing
  restamp is written **into the open cycle roadmap's foot** (the map's Arc 9 standing
  rule), not only emitted in the chat report — one clause each, pointing at the map,
  never restating its mechanics (single-home).
- **Sites:** `.claude/skills/vlt-release/references/choreography.md:178` (Stage 8 — the
  site that bit); the sibling "report ends with a Next lifecycle move line" sentences in
  `inbox-capture` (SKILL.md:22, references/roadmap-synthesis.md:85), `build-brief`
  (SKILL.md:32/:177), `acceptance-discharge` (SKILL.md:29,
  references/evidence-rubric.md:123), `cycle-closeout` (SKILL.md:28,
  references/closeout-checklist.md:194), `roadmap-roundtable` (SKILL.md:28/:132),
  `ideation-scaffold` (SKILL.md:28/:106); optionally one clarifying clause in
  `vlt-lifecycle.md`'s standing-rule paragraph ("the foot of the roadmap" said plainly).
- **Verification:** grep — every lifecycle skill that moves the position carries a
  roadmap-foot restamp clause; none restates the map's rule body; `lifecycle-status`
  (read-only, restamps nothing) correctly excluded.
- **Out of scope:** any mechanical lint for a missing/stale foot stamp (a later item or
  a P-6-class deterministic check); retro-stamping closed cycles' roadmaps.
- **Done-when:** the next lifecycle run that moves the position (likely Cycle 11's
  `acceptance-discharge`) leaves the roadmap's foot restamped without being prompted.


## Closed

### P-1 — `issue-triage`: the factory-side triage skill — **CLOSED 2026-08-21 (self-accepted on first run)**

The inaugural entry, and the channel's proof case: the rail gap that motivated the
channel was the channel's first passenger.

**Self-acceptance run (2026-08-21):** the first real triage disposed the full #4-#7
queue — all four grounded CONFIRMED against module source, owner batch-approved as-is,
8 operations (4 grounding comments + 4 `vault-accepted` labels) applied cleanly, and
the re-derived untriaged queue is empty. This run also self-accepted **the channel
itself**, unblocking the enforcement-debt items in the header.

**Built:** `.claude/skills/issue-triage/SKILL.md` + map rows in `vlt-lifecycle.md` (loop
step 1t, the untriaged-rail observable with its off-disk degradability note, the blocked
route). `lifecycle-status` needed no edit — the map is its spec (a map edit propagates).
**Deviation from brief-lite (deliberate, 1):** the widened verdict vocabulary
(needs-info/duplicate/upstream as labels) was cut at grounding — the label set is
contract-fixed at `field-contract.md:54-69` (shipped surface, boundary-protected);
verdicts are accept/decline/hold, with the reason taxonomy in comment prose.
**At-rest verification:** restatement grep clean (contract cited, never copied);
report-only discovery run derived the queue exactly (#4-#7 in, #1-#3 excluded as
captured); grounding pass confirmed all four filings against module source.
**Ruled:** owner approved the batch as-is, 2026-08-21.

**Original brief-lite (as adopted):**
- **Intent:** close the triage gap — `github-intake` only respects results
  (field-contract `:63-65`, github-intake `:87`); open issues sit `vault-filed` and
  invisible until manually labeled. Build a factory skill that scans, grounds, and
  verdicts open issues in-session.
- **Sites:** new `.claude/skills/issue-triage/`; `lifecycle-status` gains an
  untriaged-count position with a named next move.
- **Design (from the brainstorm, converged):** stateless scan (untriaged = open AND
  unlabeled; no watermark); same run scans `amended`-labeled issues (B10-7 admit path);
  grounding before any verdict (`file:line`); agent proposes / owner disposes with one
  batch approval; the issue thread is the durable triage record; transport pointed at
  the `vlt-feedback` approval-gated `gh` contract, never copied.
- **Verification (at rest):** report-only run against the live queue (#4-#7); greps
  confirm the transport contract is pointed-to, not restated.
- **Out of scope:** repo-side issue-form field changes (shipped surface → arc roadmap);
  declined-corpus case-law grep (future P-item once a declined corpus exists);
  trust-tiering by consumer roster (future, multi-vault).
- **Done-when:** first real triage run disposes the #4-#7 queue with owner batch
  approval. That run is also the item's self-acceptance **and the channel's**. ✓

### P-4 — mid-arc capture posture: the addendum rail for multi-release arcs — **CLOSED 2026-08-23 (self-accepted over two exercises)**

*(Queued 2026-08-21 from the Arc 10 mid-arc state — v0.13.0 shipped, B10-6..B10-11
remain under a stamped roundtable record, six inbox filings uncaptured, including the
`164445` Step-4 acceptance-FAILED filing whose natural home (B10-6) is an already-ruled
unbuilt build. Routed here, not inbox: every fix site is factory-side — the
delivery-not-topic test. Drafted as an inbox filing first, converted on the boundary
check; draft discarded.)*

**Built 2026-08-22.** All five sites landed:
- `inbox-capture/SKILL.md` (Discovery) — the posture: unbuilt-builds-only rule, in-session
  owner ruling (headless → `blocked`), joint test, shipped-build routing (route to the
  unbuilt owner of the surface, or hold on ruling).
- `inbox-capture/references/roadmap-synthesis.md` — the addendum form:
  `## Capture addendum — <date> (mid-arc)` after the roundtable record, standard
  `### A<arc>-<i>` subsections, each closing with a dated **Ruled into** / **Joint test** ruling.
- `build-brief/SKILL.md` — Discovery lists addendum sections naming build N as binding
  record; the Readiness gate accepts roundtable record + dated addendum rulings as
  complete, and blocks only when a moved-joint addendum lacks its
  `## Roundtable review — addendum` record.
- `vlt-lifecycle.md` — new "Mid-arc uncaptured signal" row above the general uncaptured
  row (first-match ordering), routing to the addendum posture; `lifecycle-status` needs no
  edit (the map is its spec).
- `roadmap-roundtable/SKILL.md` — the delta review: the existing-record blocked clause
  gains the moved-joint exception, scoped to the addendum, recorded as
  `## Roundtable review — addendum (<date>)`.

**At-rest verification (2026-08-22):** vocabulary grep — "capture addendum" present and
identical at all four gate homes (inbox-capture ×2, build-brief ×2, lifecycle map,
roundtable); unbuilt-only stated in capture + the map. Desk-check of `164445` through the
posture: Arc 10 mid-arc holds (batch stamped, B10-6..B10-11 unbuilt); the filing's surface
(Step-4 report emission) is owned by unbuilt B10-6 → routes there as a scope-internal
delta, `joint moved: none` → no roundtable delta. Passes.

No `plat:` commit — every touched file is gitignored (`.claude/skills/`,
`skills/reports/`).

**Self-acceptance run(s) — 2026-08-22, discharged twice, both joint-test branches
exercised.** The posture ran for real within a day of landing, and Arc 10's remaining
window was indeed the motivating first exercise:

- **Exercise 1 — the scope-internal branch** (roadmap `:931`, `## Capture addendum —
  2026-08-22 (mid-arc)`): six filings folded under the posture, four owner rulings taken
  in-session, all `joint moved: none` → no roundtable delta convened. The `164445` filing
  landed as **A10-14** and routed exactly where the item predicted — *Ruled into: build
  B10-6 (unbuilt) (owner, 2026-08-22, confirming the discharge annotation's "natural home"
  at the ledger's B10-1 entry)*. Two filings held for Arc 11 under the unbuilt-only rule
  (no unbuilt B10 build owned their surface) — the rule's refusal path, not just its
  admit path.
- **Exercise 2 — the moved-joint branch** (roadmap `:1087`, second exercise): two filings
  from the failed B10-2(5) discharge, owner-ruled **ESCALATED** into a new unbuilt
  **B10-12**, release-blocking. This batch *did* move a joint, so the delta convened and
  recorded itself at `:1224` as `## Roundtable review — addendum (2026-08-22)`.
- **The `build-brief` gate passed over both.** B10-6's brief carries the addendum rulings
  in its `rulings:` frontmatter (`build-B10-6-report-contract.md:31`: *"capture addendum
  2026-08-22 (owner-ruled: A10-11 → B10-6 …; A10-14 → B10-6 …; no joint moved)"*),
  and B10-7's likewise (`:60`, A10-15 C1+C2). B10-12 — the moved-joint case — gated on the
  delta record itself (`build-B10-12-…:64`: *"§Roundtable review — addendum (2026-08-22)
  DA4..DA8/DA11"*). All three briefed and built: B10-6 `8879869`, B10-7 `f958d66`,
  B10-12 `b6dd3f6`.

Done-when required one exercise and one passing gate; it got two of each, covering both
sides of the joint test. **The counterfactual is the real evidence:** without the posture,
A10-14 (an acceptance-FAILED filing whose surface B10-6 owned) and the two release-blocking
lint filings would have taken one of the three bad paths the intent names — silent scope
change, brief-time absorption, or a full-arc hold while B10-6 shipped without the fix.
Instead all three have dated rulings on the provenance trail and B10-12 exists as a
first-class build.

*(Ledger note: closed 2026-08-23, a day after the fact — the exercises ran during the
B10-6..B10-12 push and the record lagged the reality. Platform WIP was 2/2 on paper and
1/2 in truth for that stretch.)*

**Original brief-lite (as adopted):**
- **Intent:** give the intake side (capture → ideation → roundtable) an incremental
  mid-arc posture to match the acceptance side, which already runs in waves. Today a
  new filing facing an ideation-complete, roundtable-stamped roadmap has three bad
  paths: silent scope change to a ruled build (no ruling/roundtable trail, and
  `build-brief` gates on a record predating the filing), brief-time absorption
  (duplicates capture's grounding off the provenance trail), or holding a full arc
  (an acceptance-failure filing waits while the build that owns its surface ships
  without it). The posture: a mid-arc `inbox-capture` run may fold filings into
  **unbuilt builds only**, as a dated **capture addendum** section with the scope
  delta owner-ruled in the same session; a roundtable delta convenes only when the
  addendum moves a *joint* (cross-build dependency, ordering, interim posture), not
  for scope-internal additions; filings targeting a shipped build route to the unbuilt
  build owning the surface, or hold. One arc / one roadmap / one closeout preserved;
  the arc==release alternative was considered and declined (re-runs capture +
  roundtable over ruled builds; fights the arc-as-signal-cluster definition,
  `inbox/README.md`).
- **Sites:** `inbox-capture` (the addendum form + unbuilt-only rule + joint test);
  `build-brief` (its record gate accepts "roundtable record + dated addendum rulings"
  as complete); `vlt-lifecycle.md` (the mid-arc-uncaptured state becomes a named
  position with a next move, so `lifecycle-status` stops reading it as "await next
  arc"); `roadmap-roundtable` only if the delta form needs its own wording. *(Built:
  it did — the delta review's entry point and record heading.)*
- **Verification:** grep the three gate sites for agreement (addendum vocabulary named
  identically); desk-check the `164445` filing through the posture (routes to B10-6,
  no joint moved → no roundtable delta). ✓ (see built record above)
- **Out of scope:** any shipped-surface change (the `164445` defect itself stays an arc
  item); retroactive addendum records for past arcs; P-3's `channel: platform` intake
  fork (sibling, not this).
- **Done-when:** the first real mid-arc capture run folds a filing into an unbuilt
  build with a dated addendum ruling on record, and the subsequent `build-brief` run
  passes its gate over that addendum. **Timing note:** Arc 10's remaining window is
  the natural (and motivating) first exercise.


### P-7 — track the factory (private first) — **CLOSED 2026-08-23 (self-accepted on the mirror round-trip)**

**Self-acceptance run (2026-08-23):** built and closed same day, in the open seam.
Cruft swept (`roadmap-roundtable/.analysis/`, one upstream `__pycache__`); gitignore
inverted (2 upstream-prefix lines replace the wholesale `.claude/` + `inbox/` + `docs/`
+ `skills/reports/` ignores; `_bmad/`, `_output/`, `CLAUDE.local.md`,
`**/.decision-log.md` stay ignored); 241 files added, **78 → 319 tracked**, commit
`bd605aa` (`plat:` prefix) on `main`. Private repo created
(`github.com/mggower/bmad-module-vlt-private`, visibility verified PRIVATE), added as
remote `private` (HTTPS), `main` + all tags pushed. **Verification, all green:** origin
`main` still at `283fe5d` (v0.14.0 — received nothing); a fresh clone from the private
remote holds 319 files incl. the factory (platform roadmap, inbox, the 9 skills) and
zero `bmad-*` dirs. **Standing hazard until P-9:** local `main` now carries the
unscrubbed factory — do NOT push `main` to `origin` before the publication act (the
release commit message on `bd605aa` says the same). **Owner-ruled clarification on the
record:** the outruled thing was a second hand-synced *repo* (memlog 91/157); this is a
second *remote* on the same history (memlog 14/180) — accepted 2026-08-23.

**Original brief-lite (as adopted):**

*(Queued 2026-08-23 from the going-public design record —
`_output/brainstorming/brainstorm-untracked-work-git-strategy-2026-08-23/brainstorm-intent.md`,
adopted with P-8..P-10 as one ordered block. The record numbered them P-5..P-8; shifted
here because those numbers were already taken — relative order kept, and **the order is
load-bearing: each item is the safety net for the next (P-7 → P-8 → P-9 → P-10, not
negotiable)**. Gate (the record's §1): all four run in the Arc-10-closeout →
Cycle-11-capture seam. The seam is **OPEN at adoption** — G1 v0.14.0 released ✔, G2
Arc 10 CLOSED/archived ✔, G3 no Cycle-11 capture ✔ — and **closes when Cycle 11's
capture opens**, so rule the queue order against that before running `inbox-capture`.
Every count below was measured 2026-08-23; re-derive per the record's §8 before
building.)*

**Brief-lite:**
- **Intent:** end the durability exposure and give every later item a git safety net, with zero
  public trace. Uses the session's own finding: *tracked ≠ pushed*.
- **Sites:** `.gitignore` (invert — ignore `.claude/skills/bmad-*` and `.claude/settings.local.json`,
  un-ignore `inbox/`, `docs/`, `skills/reports/`, the 9 factory skills); a **private remote** added
  as a second push target; cruft swept (`.claude/skills/roadmap-roundtable/.analysis/`,
  `tools/__pycache__/`, any stray `**/.decision-log.md` per CLAUDE.md's standing rule).
- **Verification:** `git ls-files | wc -l` rises from ~78 to the expected count; `git push private`
  round-trips; `git remote -v` shows the public remote receiving nothing; a fresh clone from the
  private remote contains the factory.
- **Out of scope:** any rename, any move, any public push, any scrub.
- **Done-when:** the full factory tree is committed and mirrored to a private remote.


### P-9 — the publication act — **CLOSED 2026-08-23 (done-when met on the push)**

**Record (2026-08-23):** the 30-file scrub landed (`{field-vault}`/`{owner}`/`~`
placeholders; tolerated remnants: meta-references naming the scrub tokens, and
marketplace.json's deliberate public author email); README gained "How this project
evolves" + a truthful Notable-files list; `factory/method/README.md` indexes the loop's
homes; CLAUDE.md's Git & publishing rewritten to the factory-public posture. Verified:
zero personal-token hits across all tracked files, factory-paths-check PASS (107 refs),
package-lint A/B/C/E PASS at 0.14.0, stranger test walked (README = what, tracker =
how it evolves, `factory/CYCLE` = now). **[Correction 2026-08-24, off review finding
F2: "personal-token" here means exactly the three scrubbed tokens — the owner's
username, `/Users/` paths, and the field vault's real *path*. The vault's *name*
(`vlt-core`) was never a scrub target and remains throughout the factory record under
the same publish-as-is posture ruled for vlt-sayari (names no path). Its one
shipped-surface occurrence was owner-ruled a defect 2026-08-24 and filed to
`factory/inbox/2026-08-24-085505-…` for Cycle 11 capture — shipped surface routes
through the cycle roadmap, never this channel.]** **Push shape — owner-ruled at publish:** the
P-7..P-9 commits were **squashed to one publication commit `b785abd`** parented on the
v0.14.0 release commit, so public history carries no pre-scrub file states; the full
build-by-build history survives on the private mirror's `p7-p9-history` branch.
**Commit provenance note:** the per-item hashes cited in P-7/P-8's records (`bd605aa`,
`a9d8403`, `8ef152b`, `e8c92ae`) live on that private branch, not on public `main`.
**Process note:** ran from the queue while WIP sat 2/2 (P-2 open, P-8 built-awaiting) —
owner-directed and seam-bound; flagged here for the record rather than papered over.
*(vlt-sayari name: flagged at publish, owner chose to publish without scrubbing it —
it names no path.)*

**Original brief-lite (as adopted):**

*(Same block as P-7.)*

**Brief-lite:**
- **Intent:** make the factory public, cleanly, in one commit against an already-tidy structure.
- **Sites:** the ~30-file scrub to `{field-vault}` placeholders; `README.md` gains a short
  "how this project evolves"; a `factory/method/` index; the public remote push; CLAUDE.md's
  "Git & publishing" section rewritten (its gitignored-artifacts list is now wrong).
- **Verification:** grepping every tracked file for the owner's username, `/Users/` paths,
  or the field vault's real name returns nothing (the only tolerated hits are meta-references
  that *name* the scrub tokens, rewritten to `{owner}`-style placeholders, and
  `.claude-plugin/marketplace.json`'s deliberate public author email); **the 30-second
  stranger test** — README says *what vlt is*, the tracker says *how it evolves*, the open
  cycle says *what's happening now*.
- **Out of scope:** the GitHub mapping (P-10); publishing a demo vault; rewriting git history.
- **Done-when:** `main` carries the factory publicly and the stranger test passes.


### P-8 — the one build: `cycle` + `factory/` — **CLOSED 2026-08-24 (self-accepted on the Cycle 11 `lifecycle-status` run)**

**Self-acceptance run (2026-08-24):** a real `lifecycle-status` run derived Cycle 11's
position end-to-end against the renamed-and-moved surface, and both halves of the
done-when met in the same run. *The path:* the 2026-08-24 `inbox-capture` opened the
cycle at **`factory/cycles/11-reachability/`** — the first cycle born at the new location
rather than migrated into it, with `factory/CYCLE` resolving the pointer and the roadmap
titled `Cycle 11 — reachability` per deviation (3)'s shape. *The clean derivation:* the
run read `factory/CYCLE`, the cycle roadmap's frontmatter and headings, the (absent)
`briefs/` directory, `factory/inbox/`, and the tags — every observable resolved at its
`factory/` path, no stale `skills/reports/` fallback, no map row pointing anywhere dead —
and reported **Awaiting ideation** with no path flags raised. *The gate, re-run:*
`tools/factory-paths-check.py` → **PASS — 112 concrete path references resolve (20 files
scanned)** (105/19 at build time; the delta is P-11's widening and the new cycle's own
refs). The renamed skill answered to its new name in the same run (`cycle-closeout` is
what the map's closable row now routes to).

**Watch discharged by observation:** deviation-note's `ideation-scaffold` exemplar
concern is now live — Cycle 11's roadmap is the first with no 2026-07-06 rulings section
to read. Not fixed here (P-8 is closed on its done-when, not widened); recorded as a
candidate follow-up, and **P-2 is the item that touches that file next**.


**Build record (2026-08-23, commit `a9d8403` on `main`, mirrored to `private`):** the
whole surface landed in one act — 221 tracked renames (history preserved), 17 files
edited, 4 born. The `factory/` tree stands per §5B as ruled: `cycles/00-origins` +
`01-field-signal` … `10-signal-integrity` (slugs from roadmap titles), `inbox/` (D2),
`platform/`, `method/` (`cycles-were-arcs.md`), `CYCLE` pointer (reads `none`).
Filing→cycle mapping ran mechanically (timestamp-token grep over the ten roadmaps),
audited against close dates — 3 corrections (two `100000`/`150500` round-number false
matches → cycle 10; the one unmatched 2026-06-14 filing → cycle 01 by slug grep).
`cycle-closeout` renamed (D1) **with its archival mechanics rewritten to
location-archival** (stamp CLOSED in place, reset CYCLE, the one remaining `mv` is
inbox→`filings/`; headless JSON keys renamed `"arc"`→`"cycle"`, `"archived"`→`"closed"`
— any consumer parsing those needs the same rename). All 9 skills + `vlt-lifecycle.md`
+ CLAUDE.md re-pointed to `factory/CYCLE` resolution. **Gate:** new
`tools/factory-paths-check.py` born red (15 stale paths mid-build) then PASS — 105
concrete refs across 19 files. **Verified:** zero diff on `skills/vlt-*`,
`.claude-plugin/`, and the 8 shipped provenance citations; all 48 remaining "arc"
mentions deliberate (historical citations, identifiers, the D1 alias); one real
`lifecycle-status` run derived clean against every new mechanism.
**Deviations (deliberate, 3):** (1) cycle 10's roadmap moved whole, NOT split into
roadmap/ledger/rulings — it is closed history and the split's payoff targets live
roadmaps; Cycle 11 starts fresh. (2) CLAUDE.md's Git-&-publishing bullet and the release
choreography's public-surface line got interim truthful rewrites (small P-9 overlap —
both were false post-P-7; P-9 still owns the full rewrite). (3) New roadmap title shape
set to `Cycle NN — <theme>` (no ruled shape existed; matches D3's milestone style).
**Watch:** ideation-scaffold still points at "the roadmap's existing 2026-07-06 rulings
section" as a shape exemplar — fine while closed roadmaps exist to read, but a fresh
Cycle 11 roadmap won't contain it; candidate small follow-up.

*(Adoption block: same as P-7. R1–R3 owner-ruled 2026-08-23. **R4 + D1–D4 all owner-ruled
2026-08-23**, each on the record's recommendation: R4 rename forward only; D1
`arc-closeout` → `cycle-closeout` with "close the arc" kept as alias for one cycle; D2
keep `inbox-capture` + `factory/inbox/` (skill and directory agree — supersedes the
record's §5B `field/` sketch); D3 `cycleN-vX.Y.Z` branches + `vlt-cycle-N` memory
topics, existing artifacts untouched; D4 plain-numbered briefs (22 at build time) →
`factory/cycles/00-origins/briefs/`, no archaeology. Counts re-derived at build: 192
"arc" mentions in the 9 skills, 33 path refs.)*

**Brief-lite:**
- **Intent:** rename forward to *cycle* and move the lifecycle output to `factory/` in a single
  act — the rename, the move and the path re-points touch the **same 9 skills and the same ~35
  path references**, so splitting them re-opens the same files three times.
- **Sites:** the 9 factory skills (~264 forward-facing "arc" mentions + ~35 `skills/reports` path
  refs); `.claude/skills/vlt-lifecycle.md`; `CLAUDE.md` (lines ~14–47, 87–88); the `factory/` tree
  and migration map per the record's §5B; one line in `factory/method/` recording *"Cycles 1–10
  were called arcs"*; D1–D4 applied as ruled.
- **Verification:** a new `tools/` path-existence check — every path a factory skill names
  resolves — so the move gets a gate like every other build here; `grep -ri '\barcs\?\b'` over the
  9 skills returns only deliberate historical references; **no diff in `skills/vlt-*`,
  `.claude-plugin/`, or the provenance citations listed in the record's §5A**.
- **Out of scope:** archived roadmap *contents*, code-comment provenance citations, identifiers
  (`B11-3`/`A11-15`), relocating `tools/`, anything on the shipped surface, the GitHub mapping.
- **Done-when:** Cycle 11's capture opens at `factory/cycles/11-<slug>/` and one real
  `lifecycle-status` run reports clean against the new paths. *(That run is the item's
  self-acceptance, per the channel contract.)*

### P-2 — spike register + adoption-visible/brief-blocking gates — **CLOSED 2026-08-25 (self-accepted on Cycle 11's ideation, briefing, and closeout)**

**Self-acceptance run — 2026-08-25 (recorded retroactively; the exercising runs are Cycle
11's, 2026-08-24/25).** Five of the six sites were exercised by real lifecycle runs before
anyone recorded it; a `lifecycle-status`-adjacent read of the ledger surfaced the gap.

- **`ideation-scaffold`** — Cycle 11's ideation carries a populated **`### Spikes`** section
  (`factory/cycles/11-reachability/roadmap.md:952`). It collected `S-3` from the register by
  `opened_by:` with **no roadmap edit pointing at it** — the design's central claim, working.
  Ruled at `:963-972`: no Cycle 11 build binds `S-3`; "Spikes this batch newly demands: none".
- **`ideation-scaffold` (Grouping & order)** — all nine build bullets carry the `spike:` field
  beside `binds:` (`roadmap.md:517`, `:552`, `:564`, `:570`, `:582`, `:593`, `:599`, `:614`,
  `:626`).
- **`build-brief`** — the readiness gate read the field on every build; each brief's status
  records its disposition. **Build-4 is the load-bearing instance**: it held for `S-3`'s
  harvest (the A9 window) and briefed only after, recording `spike: none (the S-3 sequencing
  was A9's window constraint…)` at `briefs/build-4-relay-leg-retune.md:37`.
- **`inbox-capture`** — `S-3` was born through the external-unknown stub path
  (`opened_by: 'capture — Cycle 11 (A11-2, open question 1…)'`), which is the rung this build
  added.
- **`cycle-closeout`** — the orphan-spike precondition was live at the 2026-08-25 closeout and
  **passed** because `S-3` reads `harvested` (`verdict: reshape`, honoring the docs-only-read
  bound written into the file). An unharvested `S-3` would have blocked the closeout — the
  teeth the item was opened for, in position.
- **`vlt-lifecycle.md`** — its two spike rows are `lifecycle-status`'s spec; the map needed no
  edit and got none.

**Caveat on record: the gate's blocking branch is unexercised.** Every Cycle 11 build read
`spike: none`, so `build-brief` fired only its pass-through branch. The channel contract's bar
is "exercised once by a real lifecycle run", which this clears — but the first build that
actually binds an open `S-N` will be the first test of the block itself. Cycle 12's A11-2 build
binds `S-3` (already `harvested`), so the *consuming* path — `build-brief` appending
`consumed_by:` — gets its first exercise there; the true blocking branch waits on a spike that
is still `proposed`/`running` at brief time.

**Deviation from the done-when, immaterial:** the done-when said "Cycle 11's ideation runs with
the Spikes section populated **and build-brief's gate live**". Both held. It did not anticipate
that the register would be non-empty at hand-off (the `S-3` deviation in the build record), which
is what made the ideation exercise non-vacuous — the section rendered a real entry, not an empty view.


**Build record (2026-08-24).** All six sites landed.

- **The register** — `factory/platform/spikes/`, with `README.md` as the **single home** for
  spike mechanics: `S-N` global ids (allocated once, never reused, never renumbered), the
  four-rung ladder `proposed → running → harvested → consumed`, the frontmatter parse target,
  and one line per gate. Two rules written down that the brainstorm implied but nobody had
  stated: **harvest artifacts stay in the cycle directory that produced them** (archival is
  location — the register entry is a pointer, never a copy), and **a spent timebox reports
  `verdict: reshape`, not `kill`** (`kill` is for a question that turned out not to need
  answering).
- **`ideation-scaffold`** — Discovery now reads the register for `proposed`/`running` entries;
  the skeleton's *Spike obligations* bullet became a **Spikes** section that renders them as a
  view over the register, with owner rulings written back to the register file in-session; the
  **Grouping & order** bullet now lays a **`spike:`** field beside `binds:` on every build
  bullet.
- **`build-brief`** — the Readiness gate turns on that field: `none`, or an `S-N` whose
  register file reads `harvested`/`consumed`. Three distinct block causes named
  (open spike / id resolves to no file / **unfilled field**), plus the consuming-run
  obligation to append `consumed_by:`. Discovery reads the field alongside `binds:`; the
  headless `blocked` reason updated.
- **`cycle-closeout`** — Stage 1 went from two preconditions to three: the **orphan-spike
  check**. No spike whose `opened_by:` names the closing cycle may still read
  `proposed`/`running`; each is harvested, owner-killed with a recorded reason, or explicitly
  carried forward (re-stamping `opened_by:`). Kill-or-carry is an **owner batch ruling**, not
  the skill's. Headless `blocked` reason updated.
- **`inbox-capture`** — `references/grounding-methodology.md` gained *When grounding hits an
  external unknown*: open a `proposed` stub, because the question is sharpest at the moment
  grounding failed to answer it. Bound stated explicitly — **a stub is a question with an id,
  not a ruling**; capture never runs the spike, never binds a build, and must say plainly that
  a claim is ungrounded pending `S-N` rather than letting the unknown become an assumption.
- **`vlt-lifecycle.md`** — two observable rows (**Spike running**, **Spike open**) placed after
  *Review unresolved* and before *Ready to brief*, so an open spike is reported ahead of
  ready-to-brief under the table's first-match ordering; the `build-brief` blocked route
  rewritten from "SPIKE CLOSED in the roadmap" to the register gate; a new orphan-spike route
  on `cycle-closeout` blocked; the step-3 owner row points at the register.
  `lifecycle-status` needed **no edit** — the map is its spec.

**Back-fits (the brief-lite's verification).** `S-1` (the PARA container harvest, legacy `S1`,
Cycle 9 → consumed Cycle 10) and `S-2` (the graduation projection baseline, legacy `SPIKE-2`,
Cycle 3) — both `consumed`, both `verdict: proceed`, both pointing at their harvest artifacts
in place. Per-cycle local names are preserved as `legacy_id:` rather than renumbered.
**Finding surfaced by the back-fit:** both harvests are cited in their roadmaps at pre-P-8
`skills/reports/` paths. Those roadmaps are closed and append-only, so the stale citations
stand as history and the register entries are now the live pointers — an unplanned worked
argument for the register itself (*a spike artifact outlives the path its citers wrote down*),
recorded in both entries.

**Deviation (deliberate, 1): `S-3` opened, and the register is not empty at hand-off.**
Cycle 11's capture had already flagged A11-2's open question 1 (GitHub notification semantics)
as *"an external unknown … register it per P-2's spike register when that lands."* It landed,
so the flag was materialized as `S-3` (`proposed`) rather than left as roadmap prose — which
also gives the done-when a live subject and exercises the birth path end to end. The Cycle 11
roadmap was **not** edited to point at it: `ideation-scaffold`'s Discovery collects it from the
register by `opened_by:`, which is the design working. Its bound is inherited from A11-2 and
written into the file — the trigger must demonstrably fire, so **a docs-only read reports
`reshape`, not `proceed`.**

**At-rest verification (2026-08-24):**
- `tools/factory-paths-check.py` → **PASS, 120 concrete path references resolve (20 files
  scanned)** — 112 before the build; the 8 new register references all resolve.
- Pointer grep: all five gate sites (`ideation-scaffold`, `build-brief`,
  `cycle-closeout/references/closeout-checklist.md`,
  `inbox-capture/references/grounding-methodology.md`, `vlt-lifecycle.md`) name
  `factory/platform/spikes/` and point at the README; **the ladder and the frontmatter shape
  appear in full only in the README** — each gate names just the field it turns on.
- Vocabulary grep: `proposed`/`running`/`harvested`/`consumed` used identically at every site;
  no surviving "SPIKE CLOSED" gate language outside the deliberate pre-Cycle-11 compatibility
  clause in `build-brief`.
- Desk-check against live state: the map's *Spike open* row fires on `S-3` (its `opened_by:`
  names Cycle 11) → the next `lifecycle-status` run reports a spike position that did not exist
  before this build; `cycle-closeout` would now **block** Cycle 11 over `S-3` until it is
  harvested, killed, or carried — which is the teeth the item was opened for.
- Personal-information sweep over every new and edited file: clean (A11-2's literal handle is
  described, never reproduced).

**Out of scope, honored:** closed cycles' spike history beyond `S-1`/`S-2` is not migrated. The
one known unmigrated artifact — the B10-12 harness-classifier-ceiling spike — is **named in the
README** so the register's silence about it is a recorded choice rather than an oversight.

**Candidate follow-up (not taken):** `CLAUDE.md:24` states the spike-before-brief rule and does
not point at the register. It is outside this item's sites and the rule text is still true;
a one-line pointer is a cheap future item.

**Brief-lite:**
- **Intent:** give spikes durable IDs and lifecycle teeth: visible at adoption,
  blocking at brief (the ruling that survived the brainstorm — blocking *adoption*
  front-loads spikes at their dumbest moment; S3 proved questions sharpen after
  ideation).
- **Sites:** `factory/platform/spikes/S-N-<slug>.md` register (status:
  proposed/running/harvested/consumed; timebox; `verdict: proceed/reshape/kill`);
  `ideation-scaffold` gains a Spikes section; `build-brief` gates on candidate spike
  field = `none` or `S-N harvested`; `cycle-closeout` gains an orphan-spike check;
  `inbox-capture` may open a spike stub when grounding hits an external unknown;
  `vlt-lifecycle.md` gains spike observable rows (an open/running spike is a lifecycle
  position with a named next move) so `lifecycle-status` sees the register.
  *(Amended 2026-08-21: spike map rows folded in from the untracked-ideas sweep —
  they're siblings of this item's gates.)*
- **Verification:** back-fit S1 (PARA harvest) and spike2 into the register shape;
  grep the three gate sites for agreement.
- **Out of scope:** migrating closed arcs' spike history beyond S1/spike2.
- **Done-when:** Cycle 11's ideation runs with the Spikes section populated and
  build-brief's gate live.
