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
- **WIP limit 2 — on work in flight, not on finished work waiting.** New items queue below
  the line. The channel is a rail, not a second roadmap. An item that is **BUILT and awaiting
  self-acceptance consumes no slot**: it needs no design, no code, no decisions, only an
  exogenous lifecycle run. Counting it re-coupled the channel to the cycle cadence through the
  back door — the one thing "cadence separates" exists to prevent — and the limit was
  owner-overridden three times in flagged queue-jumps before anyone named the cause
  (*ruled 2026-08-25, off the P-2 discharge: both slots then read full while zero design or
  build work was in flight*). **Each built-awaiting item must name its discharging event and
  bound on its entry**; where that event cannot occur it is not a waiting state but
  **BLOCKED (unreachable)** and routes to an owner ruling — the grade and its rubric are
  `acceptance-discharge`'s, not restated here (P-10's re-binding, 2026-08-25, is the worked
  example). No separate section or second cap until built-awaiting inventory reaches three;
  below that the bookkeeping would cost more than the sprawl it guards against.
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

## Active (WIP 0/2 — P-10, P-15, P-14, P-20 and P-13 are all BUILT-awaiting and consume no slot, per the contract header)

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

### P-15 — the retirement rail: let the loop process obsolescence, not only defects — **open: BUILT 2026-08-25, awaiting self-acceptance (Cycle 12's roundtable + its briefs)**

*(Filed 2026-08-25 from the PARA problem-solving session, as its **Root Cause 2**. The
evidence is Cycle 11's own build-6: it extended the `para_*` honesty nets across the whole
PARA population — the exact moment the Layer 3 location prohibition became redundant — and
the nets landed **beside** the prohibition rather than **in place of** it. Nothing in the
loop could notice, because every input to the loop is a filing and a filing describes
something that **broke**. Obsolescence produces no field pain, only friction that reads as
normal governance. Eleven cycles have retired **zero** rules while adding many; the
roundtable hunts "rules ahead of mechanisms" and has no beat for the reverse. The
consequence, five times over: a root cause arrives as a symptom, a build repairs the
clause the symptom named, and the superseded rule survives to be re-filed next cycle.)*

**One item, not three.** The three sites below are one capability. A filing class with no
beat to act on it is ceremony; a beat with no way to file what it finds has no input; a
retirement question at brief time with neither is a box to tick. Splitting them would also
spend three queue slots on one idea, in a rail whose contract says it is not a second
roadmap.

**Brief-lite:**
- **Intent:** give obsolescence a channel. A protection superseded by a better mechanism
  should be retirable **through the normal loop**, rather than requiring an owner-driven
  structural ruling — which is the only route that exists today, and the reason this
  session had to be convened at all.
- **Sites:** (1) `roadmap-roundtable` — one beat, the reverse of the existing
  rules-ahead-of-mechanisms hunt: **mechanisms that have obsoleted their rules**;
  (2) `factory/inbox/README.md` — a **`supersession`** filing class ("this protection is
  now redundant, because *X* now enforces what it was standing in for"), additive to the
  existing defect/pattern/candidate shapes; (3) `build-brief` — a required clause: when a
  build ships **enforcement**, name the prohibition that enforcement makes redundant, or
  state that none exists. Every net becomes a retirement prompt at the moment it ships.
- **Verification:** grep each of the three sites; a fixture `supersession` filing routes at
  capture without being mistaken for a defect; Cycle 12's roundtable record shows the beat
  exercised (a finding **or** an explicit nothing-found); a Cycle 12 brief that ships a
  check carries the retirement clause answered rather than blank.
- **Out of scope:** any **automated** redundancy detection — a rule cannot know it has been
  superseded, and this is a prompt for the roster and the owner, not a checker (a
  P-6-class deterministic check here would be the wrong instrument); retro-auditing the
  shipped rule set for existing redundancy (that is a **study**, P-14's register, not this
  rail); changing what a filing *is* for field vaults — the class is additive, and no
  existing filing shape moves.
- **Done-when:** Cycle 12's roundtable runs with the obsolescence beat exercised **and**
  that cycle's briefs carry the retirement clause answered.

**Discharging event + bound (per the contract header).** Event: **Cycle 12's
`roadmap-roundtable` run**, with its briefs following. Bound: **Cycle 12's roundtable**. If
Cycle 12 reaches its roundtable without the beat present, or closes with the clause never
asked, this is not a waiting state but **BLOCKED (unreachable)** under
`acceptance-discharge`'s rubric, and routes to an owner ruling rather than holding a slot.

**Sequencing (load-bearing, not cosmetic).** This must land **before** Cycle 12's roundtable
and briefs, because those are the beats that consume it — and because the PARA work it
enables is *itself a retirement*. The cycle-side change removes a protection on the grounds
that a better one superseded it; the loop needs the vocabulary to record what it is about
to do **before** it does it. Shipping the rail afterwards would make this analysis a
one-off owner ruling instead of a repeatable capability, which is precisely the failure
being fixed.

**Tripwire (recorded at filing, from the session's risk register).** The live risk is that
the rail ships and never fires — added, then ignored, indistinguishable from working. **Two
consecutive cycles with zero retirement questions asked means the beat is ceremony and needs
redesign, not defence.** Measure: rules retired per cycle, baseline **zero across eleven
cycles**; any non-zero is a change of kind.

**Queue note.** Takes a free slot (WIP 0/2 → 1/2 under the 2026-08-25 ruling), ahead of
P-3/P-5/P-6/P-11/P-12/P-13/P-14. Not an override — no cap is exceeded — but a **precedence
call** on the stated dependency above, flagged here per house practice rather than left to
be inferred from position.

**Build record (2026-08-25).** All three sites landed, plus one flagged addition:

1. `roadmap-roundtable` — the joints frame gained the reverse fault ("a mechanism that
   quietly obsoletes the rule it was written to stand in for and leaves it standing"); Hunt
   gained **§The obsolescence beat (required, every run)** with the mandatory-return clause;
   Converge's record item (3) now carries the beat's outcome — each retirement finding, or an
   explicit `Obsolescence: none found` line. Silence is no longer a legal record.
2. `factory/inbox/README.md` — **§When the filing is not a defect — `supersession`**: the
   class, its two required halves (the redundant rule with its site; the mechanism whose
   population covers it), the retirement-not-carve-out bar, and an explicit disambiguation
   from the `SUPERSEDED` **grounding grade**, which means the opposite (already fixed).
   Additive; no existing filing shape moved.
3. `build-brief` — `references/brief-anatomy.md` §3 gained the **Retirement clause** beside
   R1 (it is R1 read backwards: R1 catches a rule ahead of its mechanism, this catches a
   mechanism landing *beside* the rule it obsoletes); SKILL.md's Exit gate now fails a brief
   that leaves it blank, alongside the R1/R4 line.

**Deviation (1), flagged.** A fourth site was edited:
`inbox-capture/references/grounding-methodology.md` gained **§Grounding a `supersession`
filing**. The brief-lite's own verification requires that a fixture supersession filing
"routes at capture without being mistaken for a defect", and capture's grade vocabulary
already contained a `SUPERSEDED` outcome meaning *the module already fixed this* — a live
retirement would have graded as stale news. Four lines of routing, no existing grade changed.

**Verification (at rest).** Grep of all four sites confirms each clause present at the named
home; `uv run tools/factory-paths-check.py` PASS (123 refs, 20 files). No personal or
vault-local content added. The remaining verification clauses are field-side by
construction — the fixture-filing route, the beat's exercise, and a brief carrying the clause
answered all discharge on the Cycle 12 run named below.


### P-14 — the study register: give root-cause analyses a tracked home — **open: BUILT 2026-08-25, awaiting self-acceptance (Cycle 12's `inbox-capture` folding a study-citing filing)**

*(Filed 2026-08-25, from the PARA problem-solving session. The session's own finding:
the 2026-08-20 analysis diagnosed the PARA root cause correctly, lived in `_output/`
— **gitignored** — and was distilled into a filing that carried the symptom but not the
cause. The cause never entered the factory record, and re-surfaced five days and two
releases later as an independent re-derivation by the owner. The loss was not a filing
discipline failure; the document had nowhere tracked to live. Note this ledger already
cites `_output/brainstorming/…` as provenance in its own stood-up note and in P-5 — the
factory record's own links point into untracked space.)*

**Brief-lite:**
- **Intent:** a durable, citable home for **studies** — cross-cycle, problem-shaped
  root-cause analyses that outlive any one cycle and that filings rest on. A filing
  should cite a study by tracked path instead of restating it or losing it.
- **Sites:** new `factory/studies/` with `README.md` as **single home** (what a study is,
  the naming shape, and the boundary against neighbours — a **spike** reads an *external*
  source before a brief (P-2's register); a **study** diagnoses *internal* structure
  across cycles; a **method** note records how the factory works). Entries are
  `ST-N-<slug>.md`. Back-fill **ST-1** (2026-08-20, PARA write-path — the stranded one)
  and **ST-2** (2026-08-25, location-as-proxy-for-trust) from `_output/`, scrubbed to
  placeholders per the publication rules. One clause in CLAUDE.md's lifecycle section
  pointing at the register (point-at-the-map, no restated mechanics).
- **Verification:** `factory-paths-check` PASS; the 2026-08-25 PARA filing's provenance
  paragraph resolves to a tracked `ST-2` path rather than declaring itself
  self-contained-because-`_output/`-is-gitignored; no personal or machine-specific
  content in either back-fill (grep for machine paths, owner username, field-vault name).
- **Out of scope:** gates in the lifecycle skills (P-2's spike register earns those; a
  study is *citable*, not *blocking* — adding a second set of adoption gates across five
  skills is exactly the accretion this session was convened about); migrating
  `_output/brainstorming/` wholesale (brainstorm memlogs are a different artifact class
  — a later item if they prove worth tracking); any change to shipped surface.
- **Done-when:** Cycle 12's `inbox-capture` folds a filing that cites a study, and the
  citation resolves to a tracked path.

**Build record (2026-08-25).** `factory/studies/` stood up with `README.md` as single home:
what a study is; the boundary against **spike** (reads an *external* source pre-brief),
**method** note (how the factory works), and **filing** (one field instance); `ST-N-<slug>`
register-global ids; the frontmatter shape; and the register index. Two back-fills landed —
**`ST-1`** (2026-08-20, the PARA write-path analysis that stranded) and **`ST-2`** (2026-08-25,
location-as-proxy-for-trust), each self-contained, each scrubbed. The 2026-08-25 PARA filing's
provenance paragraph now **cites `ST-2`** instead of declaring itself
self-contained-because-`_output/`-is-gitignored. CLAUDE.md gained a three-line pointer below
the platform-ledger clause (point-at-the-map; no restated mechanics).

**Design note (1), stated because it diverges from P-2's register.** A spike entry is a
**pointer** — its harvest lives in the cycle directory that produced it. A study has no durable
source to point at: the session artifact is in gitignored `_output/`, which is the failure being
fixed. So a study **carries its diagnosis in full**, and the `_output/` path is recorded as
provenance only, never load-bearing. The README states this so the two registers are not read
as the same shape.

**Design note (2).** `status: superseded` means a later study **replaced the diagnosis**, not
that the problem was fixed — and a superseded study stays in the register. Knowing what the
factory believed, and why it was wrong, is half of what a register is for. `ST-1` and `ST-2`
are both `standing`: `ST-2` sharpens `ST-1`'s primary cause and adds the process cause, and
does not refute its second-verb design (out-priced, not wrong). Each says so at the other's
name.

**Deviation (1), flagged — and half of it was an error, corrected 2026-08-25.** The brief-lite's
back-fill scope said "from `_output/`, scrubbed." Three neighbouring `problem-solution-*`
sessions (2026-08-08 — extending module-owned skills without editing source; 2026-08-19 — the
single-machine feedback loop; 2026-08-24 — full lint's cost curve) were **deliberately not**
back-filled. **08-08 and 08-19 reached their fix and stand excluded. 08-24 did not, and its
exclusion was an error** — its cause is live, captured as Cycle 11's **A11-11**, graded
CONFIRMED, with **directions 1–4 deferred to Cycle 12** and only the instrumentation shipped.
It is now back-filled as **`ST-3`**. Named **here**, so the silence is a recorded choice; the
README states the criterion, not the roster (a dated list of untracked paths is build-time
bookkeeping, not study mechanics).

**What the error was, since it is the item's own subject matter.** The excluded session's
Key Insight 4 — *"every honesty repair correctly added coverage guards; none of them ever
removed work… a guard's cost should be reviewed on the same cadence as its correctness"* — is
`ST-2`'s **RC2** and **P-15**'s baseline claim, derived a day earlier from the cost side. So
this register's back-fill dropped a live third derivation of the very cause the register and
the retirement rail were both built to stop losing. The criterion that produced it ("reached
its fix") also contradicted the README's own `status:` rule, which keeps a repaired cause
`standing` once inside. **The criterion has been replaced with a cause-reusability test carrying
an explicit guard that a live diagnosis is never excluded**, and the miss is recorded at
`ST-3`'s head and in the README rather than quietly repaired. *(Found by the tech-writer review
pass, 2026-08-25.)*

**Verification (at rest).** `uv run tools/factory-paths-check.py` PASS (re-run after the
2026-08-25 review corrections; the new register paths, including `ST-3`, resolve); a scrub grep over every new and edited file for machine paths,
the owner's name, and partner-local names returns clean; the filing's citation resolves to a
tracked path on disk, which is the done-when's own test performed early. The remaining clause
is the Cycle 12 capture run named above.

**Scope addition, owner-ruled 2026-08-25 — the re-derivation detector.** Folded into P-14
*before* self-acceptance rather than opened as its own item: one non-blocking clause in
`inbox-capture`'s `references/grounding-methodology.md` — **"does this filing's cause already
have a study?"** — asked at the one beat already reading source for a cause. Cited → the capture
names the `ST-N`, states only the residual, appends to `cited_by:`; not cited → say so, and
opening a study stays the author's call. **Not a gate**, so *Citable, never blocking* is
untouched, and P-14's out-of-scope line (no second set of adoption gates across five skills)
does not bite: one clause, one skill, no hold.

*Grounds for folding rather than opening:* the clause lives in the same skill, fires at the same
moment, and is exercised by the same event as P-14's own done-when — P-15's "one item, not
three" argument pointing the other way. *Grounds for building it now rather than waiting:* the
detector has **two observed instances** (ST-1 → ST-2 at five days; the 2026-08-24 session →
ST-2's RC2 at one day), and both occurred while the register was empty or tiny — so "small
enough to remember" is the condition under which it already failed twice. The failure was never
volume; **nobody thought to look.** Flagged as scope touching a built item so it reads as a
ruling, not creep.

**Watch (attached to this item's discharging event) — partial supersession.** `superseded_by:`
is a whole-file scalar and cannot express what `ST-2` did to `ST-1`: RC-A sharpened into RC1,
RC-B left standing ("out-priced, not wrong"). The relationship survives only in prose, in two
sections that must be read to be found — **a register whose schema cannot express partial
obsolescence, describing a loop that could not express partial obsolescence.** Deliberately
**not** designed now: the population is **one**, and a schema change grounded in a single
instance is a rule ahead of its mechanism — the fault the roundtable hunts, and poor form to
ship out of the item just reviewed for that class of problem. Re-examined at this item's
self-acceptance (Cycle 12's `inbox-capture`), by which point a second instance may exist and
would show whether the fix is scalar→list, a `supersedes:` field with per-cause granularity, or
nothing. *(Owner-ruled 2026-08-25 off the tech-writer review.)*

### P-20 — the check adversary: attack the checks, not the fix — **open: BUILT 2026-08-27, awaiting self-acceptance (the next cycle's briefing run)**

*(Filed 2026-08-27, from an owner observation at the end of Cycle 14's two-release day: *"we need a
better release review/test process — the last few releases have had a lot of defects and this has
become expensive."* Routed here, not inbox: every site is a factory skill — `vlt-upgrade` delivers
none of them. Cross-referenced to [P-18] Tier B and [P-19].)*

**The cause it repairs — a check inherits the blind spot of the fix it was written beside.** The
same reasoning that designs a repair designs its acceptance check, in the same sitting, from the
same framing. A briefer who has just ruled *"define the class in one place"* writes a check that
verifies one definition exists. The property they meant to protect — *every site that names it
agrees* — is never tested, because it was never stated separately from the fix.

**This is not a hypothesis. It is the same failure three cycles running — now four recorded
instances — and it is the ONLY failure mode that has escaped to the field in that span** (the
fourth, added 2026-08-27, did **not** escape: it was field-contingent and was caught by the next
discharge run, which is why it is the cheapest and clearest of the four):

| Cycle | Check | The blind spot | Cost |
|---|---|---|---|
| 12 | b2(5), findings cache | Tagged **field-contingent**, so it never gated; the fixture stubbed the SKILL-side writer — the exact seam that broke | Shipped broken, undetected **three cycles** |
| 13 | check (2), reduce-side guard | The instrument could be **defeated by the thing it measured** (a scanner citing the rule it applies) | Refuted in the field **within hours**; cycle could not close |
| 14 | build-3 check (4), class membership | Tested single-home-**ness** (defined in exactly one file) and never compared **membership** between the naming sites and the defining site | Contradiction shipped in v0.17.0; hot-fixed as v0.17.1 the same day |
| 14 | build-5 check (6), the park's resolution | Predicted the `write-verification.md` park would unpark **because the hot-fix cured the charter membership** — testing *what the fix does*, never the property (*the park's blocker is cleared*). The park's actual blocker is the **refused partner-sitting reading** and the unchanged `verified_by` roster, which the hot-fix does not touch | **FAILED** on the 0.17.1 upgrade — the park was **re-surfaced, not unparked**, blocker intact for 27 files. Field-contingent, so no gate was breached and nothing shipped broken |

**Fifth instance, and the first the item CAUGHT rather than reconstructed — 2026-08-27, on
[P-13]'s own done-when.** A day after both items shipped, the adversary question was run against
P-13's check (*"the next lifecycle run leaves the roadmap's foot restamped without being
prompted"*) and found a reachable passing-violating state immediately: **the check passes when
the agent that authored the clause runs the skill in the same session**, while the property — *a
reader who did not write the clause restamps* — goes untested. Two real runs had already passed
it that way. P-13's done-when was **widened rather than closed**, which is this item's prescribed
cure applied for the first time. Two things this instance establishes that the reconstructed four
could not: the question **works prospectively** (minutes, at rest, no field escape), and it is
**not self-exempting** — the item's own neighbour was written beside its own fix, in one sitting,
by one author, and inherited that framing exactly like the rest.

**The fourth instance is the one that scopes the intervention, because it was observed in REAL
TIME.** Instances 1–3 were reconstructed after an escape. Instance 4 was graded by the very next
`acceptance-discharge` run, hours after the check was written — and its refuting evidence was
**already on disk when the check was written**: the **0.17.0** post-flight, hours before build-5 was
briefed, had already named the actual blocker (*"narrowed it by ARTIFACT CLASS ONLY … explicitly
refusing the partner-sitting reading the park was built on … the park's substantive blocker
STANDS"*) and had already counted the charter omission as **one file of 29**. It was flagged in
session before the hot-fix was ruled. **The brief wrote the check from the fix's framing anyway.**

That is the sharpest available statement of this item's cause: **the blind spot is not missing
evidence, and it is therefore not curable by more grounding or another reviewer.** The briefer had
the refutation in hand and did not apply it, because the question they were answering was *"what
does this fix achieve?"* rather than *"what property am I protecting, and could this check pass
while it is violated?"*. It also confirms the item's own **out-of-scope** ruling: a second reviewer
reading that brief would have inherited the same framing and the same in-hand-but-unapplied
evidence. Graded at `factory/cycles/14-no-enforcement-point/roadmap.md` §build-5 (6) (discharge
pass 2, 2026-08-27); no inbox filing was drafted for it — the signal is factory-side and its home is
this item.

**Confirmed the same day the item was filed.** v0.17.1's repair built the membership comparison build-3 check (4) lacked, and it immediately found a **sixth** enumerating site the defect's own filing had missed — `vault-operating-contract.md:66`, the Layer-3 **entry condition itself**. It also caught that a naive member insert would ship a *new* contradiction: `:190`'s predicate said the class is *append-shaped*, and a charter is not. **A hand-written enumeration of the defect found 5 sites and one wrong predicate; the mechanical comparison found 6 and the predicate.** That gap — between what careful reading finds and what asking the adversary question finds — is this item's whole argument, measured.

**The counter-evidence matters too, and it is what scopes this item.** On the 2026-08-27 two-release
day, every *other* defect was caught before it shipped — three by briefer grounding (a roundtable
amendment that was factually wrong about live code; a second wrong about which rules three lines
restated; a roadmap `Touches` list missing a file), three by builder verification (a brief that
contradicted itself; an incomplete grounding pass; a pre-measurement off by 4), one at the release
gate (a re-ack count conflating acks with prose recitations). **Grounding and at-rest verification
are working. The gap is specifically in the checks.**

**Brief-lite:**
- **Intent:** make each ship-verifiable check state the property it protects, then try to break the
  check rather than the fix.
- **The mechanic, one question per ship-verifiable check:** *"Name the property this check exists to
  protect. Now construct a state where the check **passes** and the property is **violated**."*
  If such a state exists and is reachable, the check is incomplete — widen it, or add a second.
  Worked example (build-3 check (4)): property = *the class has one consistent definition*;
  passing-but-violated state = *a second site names the class with different members*. That is
  exactly the defect that shipped, findable at brief time in minutes.
- **Sites:** `build-brief`'s check anatomy (the adversary question sits beside the existing seam
  declaration under R1 — same slot, same discipline) · `roadmap-roundtable` (the roster already
  hunts the plan's joints; this points one voice at the *instruments* rather than the plan) ·
  the brief's acceptance section records the answer, so a check that survived the question is
  visibly distinct from one never asked.
- **Verification:** at rest — run the question against Cycle 14's shipped checks. It **must** find
  build-3 check (4) (a known positive) and **must not** flag build-1 check (2) or build-2 check (1)
  (known negatives — both were adversarially constructed already: check (2) was graded on six real
  subjects and its instrument proven failable against the prior release's code; check (1)'s fixture
  is three runs precisely because two cannot observe reused-half loss). A pass that flags everything
  is noise, not an instrument.
- **Out of scope, named not omitted:**
  - **A new review stage or an extra reviewer.** Refused on the cause: a reviewer reading the brief
    inherits the brief's framing, which is the defect. The intervention has to be a *question that
    reframes*, not a *person who re-reads*.
  - **Anything about grounding or at-rest verification discipline.** Both are working — see the
    counter-evidence above. Widening this item to "release quality" would dilute it into the generic
    review stage the previous bullet refuses.
  - **Release cost / cadence.** The owner's expense complaint on 2026-08-27 was **three forced cold
    sweeps in one day**, and that is release *granularity*, not defect rate: release 1 was split
    deliberately to reopen Cycle 13's gate and the hot-fix was an owner-chosen third cut. Two of the
    three were scheduling decisions. The structural answer is [P-19]'s frozen corpus plus Cycle 14
    build-2's cache repair (routine sweeps become warm again). **Do not justify P-20 on cost** — it
    buys correctness, and the sweeps are a separate lever.
  - **Automating the question.** It is a reasoning prompt, not a lint rule. If a mechanical subset
    emerges (e.g. "every enumeration of a set named in >1 site is compared"), that is a package-lint
    check earned later, on evidence.
- **Relationship to the neighbours:** [P-18] Tier B declares *what kind* of evidence a check rests
  on; [P-19] declares *which corpus* supplies it; **P-20 asks whether the check tests the right
  property at all.** Provenance, population, and validity — three different questions about one
  instrument. P-20 is independent of both and blocked by neither.
- **Done-when (self-acceptance):** the next cycle's briefing runs the adversary question on its
  ship-verifiable checks and **either** widens at least one check **or** records that each survived
  — the answer on record either way, since a silent pass is indistinguishable from a skipped one.

---

**BUILT 2026-08-27** (`plat:` commit — both sites are tracked factory skills). Three edits, no
new skill, no new stage — the item's out-of-scope forbade both.

1. **`build-brief/references/brief-anatomy.md` §9** gains *The adversary question (required, per
   ship-verifiable check)* — the question verbatim, the widen-or-add-a-second cure, the explicit
   *"no passing-violating state found"* return, the cause paragraph (why a reviewer cannot fix
   what only restating the property fixes), the worked positive (build-3 check (4)) and the two
   worked negatives (build-1 check (2), build-2 check (1)), the reconcile clause against a
   property the roadmap already recorded, and the field-contingent scope exclusion.
2. **`build-brief/SKILL.md` Exit gate** gains a bullet beside the existing R1/R4 and retirement
   clauses: an unanswered adversary question makes the brief **not complete**. This is what stops
   the question being optional; a silent pass is not an answer.
3. **`roadmap-roundtable/SKILL.md`** gains *The instrument beat (required, every run)*, modelled
   exactly on [P-15]'s obsolescence beat, plus its two consequential edits — the Hunt return
   contract now mandates **both** beats, and Converge records the instrument beat's outcome or an
   explicit `Instruments: none named` line.

**⚠ Grounding correction — the brief-lite's Sites line was wrong twice, and the second error
changed the build.**

- *"beside the existing **seam** declaration under R1"* — §9 has no "seam" declaration. The
  paragraph meant is **"A ship-verifiable check names its at-rest *instrument* at tag time"**
  *(Cycle 11 roundtable R1, 2026-08-24)*, and that "R1" is the **Cycle 11 roundtable amendment
  id**, not `build-brief` §3's own R1 (interim posture). The adversary question was placed beside
  that paragraph as intended; only the name was wrong. (Per-check *seams* are named in the
  ledger bullets, not mandated by §9 — a separate observation, not repaired here.)
- *"`roadmap-roundtable` … points one voice at the **instruments** rather than the plan"* —
  **not implementable as written.** The roundtable is lifecycle step 4; checks are authored at
  step 5. **At review time no check exists to attack.** Shipping the sentence literally would
  have produced a beat whose only legal return is "no checks yet", every run — ceremony, which
  the item's own P-15-derived standard forbids. The beat was re-shaped to what the roundtable
  *can* do and no other stage can: **name the property, before anyone has a fix to state it in
  terms of.** `build-brief` then reconciles the authored check against that recorded property.
  This strengthens the item's cause rather than diluting it — the roundtable voice does not
  inherit the brief's framing **because the brief does not exist yet**, which is the one thing
  the refused "extra reviewer" could never claim.

**Verification — the brief-lite's at-rest test, run against Cycle 14's shipped checks. 1 of 3
flagged, and it is the known positive.**

| Check | Property, stated without the fix | Passing-but-violated state | Verdict |
|---|---|---|---|
| build-3 (4) *(known positive)* | Every site that names the Layer-3 operational-record class agrees on its **members** | Reachable, and it happened: exactly one file *defines* the class while a fifth naming site inside that same file (`extraction.md:84`) lists **different members** than `:190`. The check enumerated four sites and tested single-home-**ness**, never membership | **FLAGGED** — cure: compare membership across every naming site (this is precisely what build-5 shipped, and it found a **sixth** site the filing had missed) |
| build-1 (2) *(known negative)* | The rewritten reduce stops producing the two false classes on real pages, **without** silencing the classes that should still fire | None found. It runs end-to-end over real bytes from the six subjects that refuted the prior release, requires two *other* detectors to still carry them (a both-directions control blocking "everything went quiet"), and carries a binding refusing any fixture limited to the changed surfaces | **not flagged** ✓ |
| build-2 (1) *(known negative)* | The cache sidecar round-trips through the **shipped** writer and reader without losing reused records | None found. The third run exists specifically because two runs cannot observe reused-half loss, run 3 must be identical to run 2, and only the page-scanner agents are stubbed — the serialize→disk→parse seam is real, which is the exact stub that defeated Cycle 12 b2(5) | **not flagged** ✓ |

A pass that flagged all three would have been noise; the instrument discriminates on the
corpus the item named.

**Cross-file agreement at rest:** `build-brief`'s §9 points at
`roadmap-roundtable/SKILL.md` for the property record, and the roundtable's instrument beat
points back at `brief-anatomy.md` §9 — mutual, one pointer each, neither restating the other's
mechanics (single-home). No shipped surface touched: `git status` shows edits confined to
`.claude/skills/build-brief/` and `.claude/skills/roadmap-roundtable/`, so the channel's
delivery boundary holds.

**Done-when (unchanged):** the next cycle's briefing runs the adversary question on its
ship-verifiable checks and **either** widens at least one check **or** records that each
survived. The instrument beat self-accepts on the next `roadmap-roundtable` run.

---

### P-13 — say "the roadmap's foot", not "the report": disambiguate the terminal-restamp obligation — **open: BUILT 2026-08-27, awaiting self-acceptance (the next lifecycle run that moves the position)**

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

---

**BUILT 2026-08-27** (`plat:` commit — all sites are tracked factory skills). **Eleven clauses
across nine files, plus the root fix in the map.**

**⚠ The brief-lite's "optional" was wrong, and the optional edit turned out to be the root.**
The Sites line called the `vlt-lifecycle.md` clause *"optionally one clarifying clause"*. It is
not optional: **the map's own standing-rule paragraph said "One line, at the foot of the
report"** — the map, which is the single home of the rule, was itself the source of the
ambiguity every consumer skill inherited. Repairing the eleven consumer clauses while leaving
that sentence standing would have left every reader one hop from the wrong reading. The map is
therefore the **first** edit, not an afterthought:

- `.claude/skills/vlt-lifecycle.md` — *"One line, written **into the foot of the open cycle
  roadmap** — the file the next reader opens"*, plus a short dated paragraph recording that the
  wording said "report" until today and what that cost (Cycle 11's roadmap: **zero** stamps
  across its whole lifecycle, against 2–3 in Cycles 9/10).

**The eleven consumer clauses**, one pair per position-moving skill — the overview sentence that
states the obligation, and the operative site where the line is actually written:

| Skill | Overview clause | Operative clause |
|---|---|---|
| `inbox-capture` | `SKILL.md` | `references/roadmap-synthesis.md` Handoff |
| `ideation-scaffold` | `SKILL.md` | `SKILL.md` Handoff |
| `roadmap-roundtable` | `SKILL.md` | `SKILL.md` Handoff |
| `build-brief` | `SKILL.md` | `SKILL.md` Handoff |
| `vlt-release` | `SKILL.md` | `references/choreography.md` **Stage 8 — the site that bit** |
| `acceptance-discharge` | `SKILL.md` | `references/evidence-rubric.md` |
| `cycle-closeout` | `SKILL.md` | `references/closeout-checklist.md` |

Every clause is a **pointer**: it names the roadmap's foot as the obligation and the chat report
as a copy, then defers to the map. **None restates the map's rule body** (the frontmatter-agreement
clause and the append-only rationale appear nowhere outside `vlt-lifecycle.md`) — single-home
discipline held. Two sites per skill matches the doubling these skills already had for the
"report ends with a Next lifecycle move" sentence; it is the same sentence, corrected in both
its existing homes, not a new home.

**Two skill-specific wordings, deliberately not uniform:**
- `cycle-closeout` says *"the foot of the roadmap **it is closing**"* — it resets `factory/CYCLE`
  to `none`, so "the open cycle roadmap" would name nothing by the time the stamp lands. This is
  also where the clause matters most: that roadmap becomes a permanent archive nobody restamps later.
- `vlt-release`'s Stage 8 carries the dated instance record, because that is the exact line whose
  "report" resolved to the chat report in the v0.15.0 run.

**Verification — the brief-lite's grep test, all four legs green:**

| Leg | Expected | Result |
|---|---|---|
| Coverage | all 7 position-moving skills carry the clause | **7/7**, two sites each |
| Exclusion | `lifecycle-status` (read-only, restamps nothing) not touched | **0 hits** — and `issue-triage` also **0**, excluded on the same ground: it moves *rail* state, never the cycle's lifecycle position *(named here rather than silently omitted; the brief-lite's site list did not mention it)* |
| Single-home | no consumer restates the map's rule body | **0 hits** outside `vlt-lifecycle.md` |
| Gates | tree still clean | `factory-paths-check` **PASS** (128 refs, 20 files); `package-lint` **A/B/C/E PASS, D SKIPPED** |

**No shipped surface touched** — every edit is under `.claude/skills/`, so the channel's
delivery boundary holds.

**Done-when — WIDENED 2026-08-27, by [P-20]'s question run against this item's own check.**

Original: *"the next lifecycle run that moves the position leaves the roadmap's foot restamped
without being prompted."* **That check was incomplete, and the adversary question found it the
day both items shipped:**

> **Property it protects:** a lifecycle skill's text reliably causes the roadmap's foot to be
> restamped — *by a reader who did not write the clause*.
> **Passing-but-violated state:** the check passes when the agent that **authored** the clause
> runs the skill **in the same session**, with the change still in working memory, while the
> property — a cold reader restamps — goes untested.

That state is not hypothetical. It is what happened: the 2026-08-27 Cycle 13
`acceptance-discharge` and `cycle-closeout` runs both restamped unprompted, and both were the
authoring session. **The evidence is real but contaminated**, and P-13 is therefore **NOT closed
on it**. This is the item's own instance of the failure P-20 exists for — a check written beside
its fix, in one sitting, by one author, inheriting that fix's framing.

**Corroborating: the clause was demonstrably not self-sufficient.** The first restamp landed
inside the roadmap's existing `## Next lifecycle move` heading with superseded routing still
below it — the exact defect this item exists to prevent, committed while obeying it. It was
self-caught from the **map's** rule (*"the reader trusts the END"*), not from the clause's own
wording, which said only *"the roadmap's foot."* A cold reader has the wording and not the
author's working memory.

**Wording repair shipped the same day.** The precise definition landed in `vlt-lifecycle.md`,
where the mechanics are single-homed — *"**Foot** means the **last block in the file**, not the
last `## Next lifecycle move` heading"*, plus the demote-prior-stamp-under-a-`— historical
record`-heading procedure and the closing test (*if anything at all follows the stamp, it is not
the foot*). The seven **operative** clauses gained a six-word pointer-grade precision (*"its
**last block**, below any earlier routing"*); the seven overview clauses are unchanged, and no
consumer restates the map's rule body.

**Done-when (widened):** the next lifecycle run that moves the position leaves the roadmap's
foot restamped without being prompted **in a session that did not author the clause** — a cold
exercise. Cycle 14's next `acceptance-discharge` is the first available one. Record that run's
date here; the two 2026-08-27 runs stand as evidence the mechanism works, not as the close.

**Out of scope, unchanged and now more clearly earned:** no mechanical lint for a missing or
stale foot stamp. That is a [P-6]-class deterministic check — *"the open roadmap's last
`Next lifecycle move` agrees with its frontmatter `status:`"* is exactly the shape P-6's
tranche takes, and it should be earned there on evidence rather than invented here.


---

**Built-awaiting inventory is now FIVE (P-10, P-15, P-14, P-20, P-13) — well past the contract
header's threshold.** The header defers a separate section or second cap "until built-awaiting
inventory reaches three." It reached three on 2026-08-25 and **five on 2026-08-27**. Flagged as an
**owner call**, not acted on: four items with named discharging events and bounds may still be
cheaper to read in place than to re-file into a section. The ruling belongs on the ledger either
way, and it is now **two** items overdue — the inventory grew by two in a single day, which is
itself the argument that the threshold was set at the right number. *(Count updated 2026-08-27 at P-20's build; the original
note is preserved above in substance, not re-derived.)*

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
  *(Amended 2026-08-25: the platform observable rows should render **built-awaiting** as a
  position in its own right — evidence "entry reads BUILT, awaiting self-acceptance", next move
  = the discharging event the entry names, per the contract header's WIP clause. It is the
  mechanism half of that clause; the contract half shipped as a ledger edit the same day and
  needs no build.)*
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

### P-16 — the `promise:` line: name the vault-visible delivery at ruling time — **queued**

*(Filed 2026-08-25, from an owner brainstorming session on the loop's comprehension problem
— memlog + keepsake at `_output/brainstorming/brainstorm-lifecycle-comprehension-2026-08-25/`,
untracked, provenance only. **Not actioned mid-flight by owner ruling**: three of the session's
directions touch `ideation-scaffold` and `build-brief`, which Cycle 12 is mid-way through
using, and changing the scaffold's contract against a half-filled skeleton risks a section that
parses under neither shape. This item waits for Cycle 12 to ship.)*

**The cause it repairs — `ST-4`** (*provenance is staffed, cognition is not*; root cause (b):
no promise artifact stands between the diagnosis chain and the implementation chain, so the first
vault-facing sentence anywhere is the CHANGELOG, written after the surprise). Read the study for
the derivation and for the four other repairs it implies; this item is only the first of them.
`ST-4` gates nothing — the scope ruling below is this item's, not the study's.

- **Intent:** every build bullet carries a one-sentence, vault-facing **`promise:`** line
  written at ruling time — *after this ships, a vault owner running `vlt-<x>` sees Y instead of
  Z* — so scope is ruled against promises rather than against filing ids, and the sentence is
  reused (not re-invented) at acceptance and in the CHANGELOG. **Amended 2026-08-25 — see the
  correction below; the CHANGELOG half of this intent rests on a premise that was wrong.**
- **Sites:** `.claude/skills/ideation-scaffold/SKILL.md:76-80` (the grouping bullet — a third
  one-line field beside `binds:` and `spike:`, same `*(owner to fill)*` discipline) and its
  standing-rule section at `:114` if the roster rule is the right home for the parallel rule;
  `.claude/skills/build-brief/SKILL.md:83-88` (Discovery reads the bullet — carry the
  `promise:` into the brief's scope statement, never re-author it);
  `.claude/skills/vlt-release/references/choreography.md:61-62` (the sentence that names the
  CHANGELOG bullet source — **corrected from `:59`**, which opens the paragraph but is not the
  clause in question).

  **Correction, 2026-08-25, from the first `ST-4` instrument dry run.** This entry was written
  on the premise that the CHANGELOG is the *first* vault-facing sentence in the loop. It is not.
  A brief's **`title:`** is already *"public prose … collected verbatim into the module's
  `CHANGELOG.md` entry"* (`.claude/skills/build-brief/references/brief-anatomy.md:30-31`), and
  `choreography.md:61-62` collects *"one bullet per build … from each open-cycle brief's
  `title:`"*. So a vault-facing per-build sentence exists today; it is authored at **brief
  time** by the **briefer**. `ST-4` root cause (b) is corrected to match: the gap is *who and
  when*, not that nothing exists. **This entry never mentioned `title:` — it was not considered
  when the item was queued.**

  **Prior open question this raises, ahead of the gate question below:** given that `title:`
  already reaches the CHANGELOG, what relation does `promise:` bear to it — does `promise:`
  become the CHANGELOG bullet source in place of `title:`, does it feed `title:` at brief time,
  or do the two coexist with different jobs? Unsettled; not settled here.

  **Owner-ruled open question, not settled here:** which treatment `build-brief`'s Readiness
  gate gives an unfilled `promise:` — **(A)** blocking, the treatment `spike:` has
  (`build-brief` SKILL.md:129-135); **(B)** non-blocking carry-when-present, which has no
  precedent in the tree; or **(C)** non-blocking reconstruct-and-disclose, the treatment
  `binds:` has (`build-brief` SKILL.md:88). *(The original phrasing here — "gating makes it real
  … not gating makes it advisory and probably decorative" — is **struck**. It was a
  recommendation written into a tracked file, which is the failure `ST-4` root cause (c) names:
  it would have pre-framed the question for every later reader of this entry. The three-option
  form above is the dry-run packet's, and the packet is where the grounding lives.)*
- **Verification:** grep — bipartite agreement between the scaffold's emitted field and
  `build-brief`'s reader; a scaffolded skeleton on a real cycle shows the field present and
  empty; no site restates another's mechanics (single-home).
- **Out of scope:** the wider comprehension-debt repair this session produced — the
  six-field ruling shape, ruling-by-exception (a reversal of the 2026-07-12 "an empty slot is
  honest, a guessed answer is a lifecycle violation" ruling, which belongs to the roundtable,
  not to this channel), the generated ideation view, and the `NEVER-VERIFIABLE` acceptance
  grade. Also out: retro-writing promises for shipped builds.
- **Done-when:** the first cycle ideated after Cycle 12 ships carries a filled `promise:` line
  on every build bullet, and that cycle's CHANGELOG entry is recognisably the same sentence.

**PARKED 2026-08-25, and this block is the whole parked set** — owner ruling, taken while
Cycle 12 was still open. Everything below reopens together.

*Recorded per A12-5's shape (Cycle 12 build-5): an exit condition records the **blocker's
shape** and the reference, never a pre-authorized sequence of moves. So no command list and no
"then do X" below — only what is unsettled, where its grounding lives, and what state ends the
park.*

- **Exit condition (shape, not a trigger):** Cycle 12 ships. Nothing here is actioned before
  that — three of the repairs touch `ideation-scaffold` and `build-brief`, which Cycle 12 used
  mid-flight. The park does not expire on a date and nothing schedules it; `cycle-closeout`'s
  carry-forward record is where it should surface.
- **If Cycle 12's shape changes before it ships** (a build dropped, a ruling reversed, the
  grouping re-cut) this block does not silently survive it — re-read the two P-16 questions
  above against whatever actually shipped. That is the A12-5 failure mode this block exists to
  avoid: a parked record that reads as still-authorized after the thing it rested on moved.

**The two P-16 questions** are stated in full above (the `promise:`/`title:` relation, then the
Readiness-gate treatment A/B/C). They are not restated here.

**Homeless items — unsettled, and this is their only tracked home:**

1. **The reversibility rubric has no definition in the tree.** The three grades used by the
   six-field shape are: **CHEAP** — change it next cycle, nothing shipped; **STICKY** — it is in
   vaults, unwinding needs a migration; **ONE-WAY** — a convention bump plus re-ack, or a
   governance rule other runs cite. Recorded here because they existed nowhere on disk. *Known
   defect:* the dry run could not grade its own option (A) — "nothing shipped" and "a governance
   rule others cite" point at different grades for a factory-side gate, so the clerk wrote the
   disagreement rather than picking. Unsettled: whether the rubric gets a tracked home, and how
   that clause conflict resolves.
2. **Field 4 (*what happens if you say nothing*) leans structurally toward the status quo**,
   because the status quo is what it describes. Unsettled: keep, reshape, or drop. Known to be
   the shape's sharpest flaw; ordering it after options mitigates and does not remove it.
3. **Fields 5 and 6 collapse into each other on platform-channel questions** — roughly 40%
   restatement when nothing ships and no version bumps, because "which files get re-edited" and
   "how hard to unwind" are the same question there. They separate cleanly on shipped work.
   Unsettled: whether they merge for platform items only.
4. **Whether the six-field shape gets a tracked home at all before Cycle 13.** The field list
   survives in `ST-4` §Disposition; the withholding protocol survives in `ST-4` §The sharpest
   acceptance test. What survives nowhere else: the per-question marks — **ruled / stalled /
   routed** — and the two numbers a run reports (how many of a batch ruled with no read, and
   where the stalls clustered). Recorded here for that reason. Unsettled: file it as a method
   note, leave it in `ST-4`, or leave it unwritten until a second run.
5. **Who clerks the first clean legibility reading, and on what.** It cannot be the session that
   produced `ST-4` or this entry — both have given the owner recommendations on `promise:`,
   which is what made the 2026-08-25 dry run a *format* test rather than a measurement. Earliest
   honest venue: the first ideation batch after Cycle 12 ships. Unsettled: venue and clerk.
6. **`P-17` and `P-18` are not queued.** Their diagnoses are carried in `ST-4` §Disposition —
   *inbox holds unclaimed only, filings migrate at capture* (repairs root cause (d)) and *a
   `NEVER-VERIFIABLE` acceptance grade* (lets a tail die rather than carry). Unsettled: whether
   they enter the queue at all. Nothing is lost by leaving them out — the causes are tracked.
7. **`ST-4`'s scope precedent awaits nobody, and that is deliberate — but it is unratified.**
   The study is the register's first factory-side entry; the descriptive-vs-causal cut it rests
   on was the clerk's call, stated at the head of the file for a later reader to overrule in
   place. No ruling is owed. Recorded so the reopening does not mistake silence for ratification.

**The dry-run packet itself is not tracked.** It lives only in the transcript of the session
that assembled it (2026-08-25) and will not survive. Deliberate: it re-derives in ~15 minutes
and 9 reads from four files — `factory/platform/roadmap.md` (this entry),
`.claude/skills/build-brief/SKILL.md`, `.claude/skills/ideation-scaffold/SKILL.md`,
`.claude/skills/vlt-release/references/choreography.md` — plus two confirmatory reads
(`build-brief/references/brief-anatomy.md`, `tools/package-lint.py`). Its durable findings are
the corrections already applied above and in `ST-4`; nothing else in it is load-bearing.

### P-18 — specimen custody: give field observations a carrier — **queued**

*(Filed 2026-08-26, from an owner problem-solving session on the acceptance gate's oscillation
— session artifact at `_output/problem-solution-2026-08-26.md`, gitignored, provenance only.
Routed here, not inbox: every site is a factory skill, `factory/inbox/README.md`, or closeout
mechanics — `vlt-upgrade` delivers none of them. **Scoped deliberately to Tier A of the study's
nine components**; the other two tiers are named in Out of scope with their preconditions, per
P-6's form.)*

**The cause it repairs — `ST-5`** (*specimens have no owner*; primary cause: no lifecycle stage
owns field-specimen preservation, so verification instruments are built at the point of least
evidence — from the shape of the fix rather than the shape of the failure). The direct evidence
is the Cycle 12 build-1 trace: **20 specimens observed, 2 filed, 2 captured, 0 reaching the
brief**, after which the briefer synthesized a fixture that passed at rest while the field failed
twice. Read the study for the derivation, the six causes, the rejected alternatives and the
falsifier. `ST-5` gates nothing — the scope ruling below is this item's, not the study's.

**Brief-lite:**
- **Intent:** make a field observation survive to the instrument that grades it. Today a filing
  may report *"18 entries"* where 18 slugs were observed, capture grounds only against module
  source (*"ground every filing claim against current module source"* — code, never corpora), and
  `acceptance-discharge` holds complete specimens at the moment of maximum evidence while being
  told *"Read only what the item names. Don't go spelunking."* The stage with the specimens has
  no authority to use them; the stage that must build the instrument has none left to build from.
- **Sites:** `factory/inbox/README.md` (filing shape gains a **specimen manifest** section — full
  slug set plus the minimal triggering fragment; a bare count where a set was observable is a
  defect in the filing) · `.claude/skills/acceptance-discharge/references/evidence-rubric.md`
  (the FAILED and BLOCKED grades must emit a complete manifest with the filing they already
  mandate) · `.claude/skills/inbox-capture/` (second grounding axis: where a filing carries a
  count, dereference the named report and recover the set) · `factory/cycles/NN-<slug>/fixtures/`
  established by convention so the manifest materializes as a tracked, frozen fixture · the
  ledger gains a per-build **specimen retention** number.
- **Verification:** at rest — the 2026-08-26 filing
  (`…-attestation-misroute-survives-the-jurisdiction-narrowing.md`) already carries a complete
  6/6 manifest unprompted and is the conformance fixture for the new filing shape; the
  2026-08-24 filing (2/20) is the negative control that must fail it.
- **Out of scope, named not omitted:**
  - **Tier B — instrument provenance (`ST-5` C6/C7):** every check declares
    `population-shaped`/`specimen-derived`/`synthetic` with synthetic requiring justification,
    and carries negative controls in both directions. **Deferred because its substance was
    already obtained by owner ruling** — Cycle 13's ideation ruled Q4 *"THE INSTRUMENT IS THE
    REAL CORPUS AND IT GATES."* That is the ninth hand-applied brake in the series `ST-5`
    documents, not a mechanism; open Tier B when a build with **no prior failure behind it**
    reaches brief-time and reaches for a synthetic fixture unchallenged.
  - **Tier C — gating honesty (`ST-5` C8/C9):** narrow closeout's non-gating clause to
    *field-contingent **and not yet fired***, routing a fired-and-failed check to an owner
    ruling; decay unfired checks on a date or run-count bound. **Precondition: Tier A must
    first produce one cycle of real manifests** — landing C8 first would tighten gating on
    checks that still could not be made good, which is the strict era rediscovered.
  - **The in-cycle repair lane:** a shipped cycle staying open to capture for repairs of its own
    acceptance failures. Touches release policy and ruling D3; `ST-5` records it as a live option
    it does not recommend either way. **Owner call, not queued here.**
  - **A specimen register (`factory/specimens/`, `SP-N`):** generated and **rejected** on the
    study register's own accretion warning. The manifest lives inside the filing and is cited by
    path — the root is *no owner*, not *no register*.
- **Done-when (self-acceptance):** the next `acceptance-discharge` run grading a FAILED or
  BLOCKED item emits a complete specimen manifest with its filing, **or** an `inbox-capture` run
  recovers a specimen set from a count-only filing. Either exercises the changed surface on a
  real lifecycle run.

**Tier C — second real instance, 2026-08-27.** Cycle 13's acceptance check (4) **fired on
2026-08-26, FAILED, and gated nothing**, passing straight through closeout's non-gating clause;
it was re-graded DISCHARGED a day later on a repair that shipped in a *different cycle*. That is
exactly the state Tier C's narrowing (*field-contingent **and not yet fired***) exists to catch:
a fired-and-failed check is not a waiting check, and today nothing distinguishes them. Recorded
as evidence for the tier, not acted on — **Tier C's precondition (Tier A producing one cycle of
real manifests) is still unmet**, and landing C8 ahead of it is the strict-era mistake this item
already refuses. *(Same run also recorded a MISSED bound on (4) — owner-ruled recorded-only at
closeout, since the bound governed when the check was graded, not what it asserts.)*

**Trigger near-miss recorded 2026-08-27 (Tier B).** Tier B's opening condition is *"a build with
no prior failure behind it reaches brief-time and reaches for a synthetic fixture unchallenged."*
Cycle 14 **build-3's brief reached for a synthetic fixture at its check (3)** — unavoidably:
nothing executable implements `para_missing_attestation` (`vlt-lint-full.js` carries a structural
slot only; the PARA scan is SKILL-side prose, so the check is an agent reading prose). **Tier B is
NOT opened on it** — the reach was *challenged and recorded in the brief*, which is the opposite of
the unchallenged case Tier B waits for, and A14-7 is a prior failure behind it. Recorded because the
near-miss is evidence about **where the trigger actually sits**: the condition as written turns on
*unchallenged*, and a briefer who names the reach honestly will keep clearing the bar while the
underlying gap — a rule with no executable enforcement point — stays open. If a second challenged
reach lands before an unchallenged one, the trigger's wording is the thing to revisit, not the tier.

### P-19 — the acceptance corpus: freeze it, and say which checks bind to it — **queued**

*(Filed 2026-08-27, from an owner observation during Cycle 14's release-2 run: the live field
vault's wiki has grown to the point where a full lint per release is expensive — measured that day
at **146 files checked, 146 cold, 0 cached**, against 377 markdown files in the vault. Routed here,
not inbox: every site is a factory skill or process doc — `vlt-upgrade` delivers none of them.
**Cross-referenced to [P-18] Tier B**; see the shared-brief note under Out of scope.)*

**The cause it repairs — the corpus moves underneath the measurement.** This is *not* `ST-5`'s
cause (*specimens have no owner*) and is not repaired by fixing it: with perfect specimen custody
and perfectly honest provenance labels, two releases' sweeps over a **growing** vault still are not
comparable — a real regression and three months of new pages present identically. Cost is the
symptom the owner felt; **reproducibility is the defect.** Scoping this item on cost would be a
mistake and is explicitly refused below.

**Brief-lite:**
- **Intent:** make acceptance evidence reproducible across releases by binding corpus-shaped checks
  to a **frozen, dated, real** corpus, and by making every check say which corpus it rests on.
- **Sites:** a **snapshot manifest** (tracked) recording what the snapshot *is* — snapshot date,
  file count, source vault as a placeholder — while the snapshot itself stays **local-only and
  gitignored** (the factory is public; a real vault snapshot is the owner's personal content and
  can never be tracked — this is the constraint that shapes the whole item) · `build-brief`'s check
  anatomy gains a **corpus declaration** alongside the seam each ship-verifiable check already names
  under R1 · `acceptance-discharge` records, per item, which corpus graded it · a **re-snapshot
  policy**: refreshing is a dated event with a recorded reason, so *"the corpus changed"* is never a
  silent explanation for a changed result.
- **The split the declaration enforces:** *mechanism* checks need no corpus (most already grade at
  rest under D3-as-amended — Cycle 14 graded 6/8, 7/7 and 7/7 at rest across builds 1–3);
  *population* questions (*"how many pages predate this rule"*) may bind to the snapshot;
  *currency* questions (*"did this upgrade preserve the mints that exist right now"*) **may not** —
  they are about the live vault by definition.
- **Verification:** at rest — a corpus-shaped check from a shipped brief is re-run against the
  snapshot and against the live vault, and the difference between the two results is *explained by
  the manifest's delta*, not unaccounted. Cycle 14 build-1's checks (6)/(7) are the available
  worked pair.
- **Out of scope, named not omitted:**
  - **A synthetic or authored test vault — generated and REJECTED, reason on record.** A corpus
    built to exercise checks passes because it was built to. That is how Cycle 12's findings cache
    shipped broken (b2(5): a fixture that stubbed the seam that failed), and it is what Cycle 13's
    check (2) binding forbids in as many words: *a fixture exercising only the surfaces this build
    changes does not satisfy it.* Build-1's check (2) re-graded PASS on 2026-08-27 **because** it
    ran against six real subjects. The snapshot is *real content, frozen* — not content authored
    for the test.
  - **Retiring live-vault acceptance.** The snapshot is an addition. Upgrade-preservation,
    post-flight evidence, and every currency question stay live.
  - **Sweep cost.** Cycle 14 build-2's cache repair is the answer to that, shipping in release 2;
    146/146 cold is the broken cache, not the vault's size. **P-19 must not be justified on speed**
    — that framing would make it the licence to dodge a live check the first time one is
    inconvenient.
  - **Shared brief with [P-18] Tier B.** The two are one declaration in halves — Tier B says *what
    kind* of evidence a check rests on (`population-shaped`/`specimen-derived`/`synthetic`), P-19
    says *which corpus* supplies it. **If both are open at brief time they get ONE brief.** They
    are kept as two items because their causes differ, because Tier B is gated on a trigger that
    may not fire for cycles while this problem is live now, and because either is useful without
    the other.
- **The guardrail it must survive:** Cycle 13's ideation ruled **"THE INSTRUMENT IS THE REAL CORPUS
  AND IT GATES."** A frozen snapshot is still a real corpus, so P-19 does not overturn that ruling —
  but the ruling is the boundary, and any drift from *frozen real* toward *authored* is the ruling
  being broken, not interpreted.
- **Done-when (self-acceptance):** the next release's acceptance runs at least one corpus-shaped
  check against the snapshot **and** the discharge record names which corpus graded each item.




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
