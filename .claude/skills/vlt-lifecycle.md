# The vlt lifecycle map

**This is the single home for the lifecycle flow as practiced.** The eight-step loop is
declared in CLAUDE.md; this map adds what that list doesn't carry — which skill owns each
step, what observable repo state corresponds to which position, and where every outcome
(including every `blocked`) routes next. Skills point here; this file never restates a
skill's mechanics (single-home discipline: mechanics live in exactly one place).

**The open cycle** is named by `factory/CYCLE` (one line, `NN-<slug>`, "none" between
cycles); its artifacts live under `factory/cycles/<that>/` — `roadmap.md`, `briefs/`,
`filings/`. A closed cycle's directory simply stops changing (archival is location, not
a move). *(Cycles 1–10 were called arcs — `factory/method/cycles-were-arcs.md`.)*

## The loop, with owners

| Step | Name | Owner | Skill |
|---|------|-------|-------|
| 1 | Field notes | live vaults (owner relays for vaults without inbox access) | — (files land in `factory/inbox/`) |
| 1t | Rail triage (remote filings only) | agent grounds + drafts; **owner rules the batch** | `issue-triage` |
| 2 | Capture | skill | `inbox-capture` |
| 3 | Ideate | **owner-steered, deliberately unformalized** | `ideation-scaffold` lays the empty rulings skeleton; the deciding stays the owner's (rulings recorded in the roadmap's Ideation rulings section). External unknowns get **spikes**, tracked in the register at `factory/platform/spikes/` (mechanics single-homed in its `README.md`) — visible at adoption, blocking at brief |
| 4 | Review | skill convenes; **owner rules disputes live** | `roadmap-roundtable` (skippable only by an explicit owner waiver recorded in the roadmap) |
| 5 | Brief | skill | `build-brief` |
| 6 | Build | fresh builder session per brief (via `bmad-workflow-builder`) | — (obligations: implement the brief, unit-verify at rest, rewrite the brief `status:` to a BUILT record with numbered deviations, delete any `.decision-log.md`, one commit) |
| 7 | Release | skill | `vlt-release` |
| 8a | Live acceptance — upgrade | **owner runs `vlt-upgrade` on a live vault** (standing rule) | — |
| 8b | Live acceptance — discharge | skill | `acceptance-discharge` |
| 8c | Cycle retirement | skill | `cycle-closeout` |

## Where am I? (observable state → position → next move)

Derive the position from disk, never from memory of where things stood (derive-first).
First row that matches, top to bottom — or run `lifecycle-status`, which walks this table
read-only and reports every active position:

| Observable condition | Position | Next lifecycle move |
|---|---|---|
| An open `vault-filed` issue on the transport repo carries neither `vault-accepted` nor `captured` (via `gh` — see note below) | Untriaged rail signal | `run issue triage` (`issue-triage`) |
| An open `captured` issue on the transport repo carries `amended` (via `gh` — see note below) | Admitted amendment pending | run `inbox-capture` (the amendment leg consumes it) |
| `factory/inbox/*.md` exist that no open roadmap's `derives_from` lists, and the open roadmap's batch is roundtable-stamped with unbuilt builds remaining | Mid-cycle uncaptured signal | run `inbox-capture` — the mid-cycle **capture addendum** posture (folds into unbuilt builds only; mechanics live in `inbox-capture`) |
| `factory/inbox/*.md` exist that no open roadmap's `derives_from` lists | Uncaptured field signal | run `inbox-capture` |
| Open roadmap has captured filings with no build assignment in its Ideation rulings section | Awaiting ideation | `ideation-scaffold` lays the skeleton, then the owner fills the rulings in session |
| Ideation rulings for the batch are filled but no Roundtable review record (nor owner waiver) covers them | Awaiting review | `convene the roundtable` (`roadmap-roundtable`) |
| A Roundtable review record carries OPEN disputes | Review unresolved | owner rules the open disputes (that closes the record) |
| A `factory/platform/spikes/S-N-*.md` whose `opened_by:` names the open cycle reads `status: running` | Spike running | finish the read inside its timebox, then fill `sources:`/`findings:`/`verdict:` and set `harvested` (a spent timebox reports `reshape`, not `kill`) |
| A `factory/platform/spikes/S-N-*.md` whose `opened_by:` names the open cycle reads `status: proposed` | Spike open | run the spike — read the **actual external source**, not its docs or memory of it — then harvest it |
| Rulings name build N, a Roundtable review record (or waiver) covers the batch, and no `factory/cycles/<CYCLE>/briefs/build-N-*.md` exists | Ready to brief | `brief build N` (`build-brief`) |
| A brief's `status:` is `BRIEFED …` (not BUILT) | Ready to build | fresh builder session implements that brief |
| Every cycle brief is BUILT and no `vX.Y.Z` tag exists for the cycle's version | Ready to release | `release vlt X.Y.Z` (`vlt-release`) |
| Tag exists; ledger has unchecked items; no acceptance evidence yet (no vault upgrade at/above the cycle's version) | Awaiting field upgrade | owner runs `vlt-upgrade` on a live vault |
| Acceptance evidence exists (upgrade-ledger entry, relayed evidence filing, or post-upgrade vault activity) and ledger items are unchecked | Acceptance pending | `run acceptance discharge` |
| Every ledger item is checked or carries an owner carry-forward ruling | Cycle closable | `close the cycle` (`cycle-closeout`) |
| Roadmap is CLOSED and `factory/CYCLE` reads none | Between cycles | next filings restart the loop at `inbox-capture` |

The rail rows are the table's **off-disk observables** — they need `gh`. When
`gh` is missing or unauthenticated, the position is **unknown**, reported as "rail state
unknown (`gh-missing`/`gh-unauthenticated`) — check online"; never rendered as absent.

Positions can coexist (an open cycle routinely has BUILT briefs *and* new uncaptured
filings). When they do, acceptance/closeout of shipped work and capture of new signal are
independent tracks — neither waits for the other.

## Blocked outcomes (every block has a route out)

A `blocked` verdict is a skill doing its job — but it must never be a dead end. Routes:

- **`inbox-capture` blocked** (a filing's claim conflicts with recent unshipped work) →
  owner rules on the conflict, then re-run capture for that filing.
- **`issue-triage` blocked** — `gh-missing`/`gh-unauthenticated` → fix the named cause,
  re-run (the queue re-derives; re-running is always safe). A stale-shape held issue →
  the owner hand-handles per the field contract's evolution rule. An owner who declines
  to rule the batch → issues simply stay `vault-filed` (candidacy costs the factory
  nothing) — not a dead end, just an unarmed intake.
- **`roadmap-roundtable` blocked** — unfilled ideation rulings → owner fills them
  (`ideation-scaffold` first if no skeleton exists); an existing review record for the
  batch → proceed to briefing, or the owner explicitly asks to re-convene.
- **`build-brief` blocked** — four causes, four routes: missing ideation rulings →
  `ideation-scaffold` lays the skeleton, owner fills it in session; missing roundtable
  record (and no waiver) or OPEN disputes on it → `convene the roundtable` /
  owner rules the disputes; a `spike:` field unfilled or naming a spike that is not yet
  `harvested`/`consumed` → run the spike (read the actual external source) and harvest it in
  the register, or have the owner rule the build `spike: none`; an unruled evidence debt →
  owner disposition in the rulings. Then re-invoke `brief build N`.
- **`vlt-release` gate failure** → fix the named gate's cause, re-run from stage 1
  (stages are idempotent up to the failure point).
- **`acceptance-discharge`** — per-item: a **FAILED** item routes its drafted inbox filing
  into the next `inbox-capture` run; a **STILL-OPEN** tail names the exact discharging
  event — wait for it, then re-run discharge (re-running is cheap and always safe). A tail
  whose discharging event *cannot occur* (no shipped surface can produce it) is not a
  waiting state — the rubric grades it **BLOCKED (unreachable)**: file it to
  `factory/inbox/` and let capture route it into a build.
- **`cycle-closeout` blocked** → an undischarged ledger routes to `acceptance-discharge`;
  a discharged-but-uncarried tail routes to an owner carry-forward ruling; a missing tag
  routes to `vlt-release`; an **orphan spike** (opened by this cycle, still
  `proposed`/`running`) routes to an owner batch ruling — harvest it, kill it with a
  recorded reason, or carry it forward to the next cycle.

## Standing rule: a report's terminal routing line is authoritative

*(Arc 9 roundtable, 2026-08-20.)* Cycle roadmaps and reports are **append-only** and long. A reader
— human or skill — trusts the **end** of the document for "what happens next", so a terminal
routing block left over from an earlier lifecycle position **silently routes the next reader to
the wrong step**. Arc 9's roadmap carried a closing block sending the reader back to step 3
(ideation) and re-posing three scope questions that had already been ruled, while its own
frontmatter said step 4.

**Every lifecycle skill restamps that line on exit**, in the same run that moves the position:
capture, ideation-scaffold, roadmap-roundtable, build-brief, release, acceptance-discharge,
cycle-closeout. One line, at the foot of the report, naming the current next move — and it must
agree with the frontmatter `status:`. Where they disagree, the frontmatter is the position and
the terminal line is the defect.

## The routing contract

Every lifecycle skill ends its report — interactive and headless alike — with an explicit
**Next lifecycle move** derived from its outcome (headless: a `"next"` field in the JSON).
The move names a skill invocation, an owner action, or the event being waited on — never
just a state description. This map is the authority on what routes where; a skill that
can't determine its next move points the owner here.
