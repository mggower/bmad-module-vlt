# Closeout Checklist

Discovery has handed you: the open cycle roadmap (at `factory/cycles/NN-<slug>/roadmap.md`,
named by `factory/CYCLE`), its Deferred acceptance ledger, its `build-N-*.md` briefs, and the
field filings it derives from. Now close it. Work the stages in order — the gate comes first,
and nothing moves until it passes.

**This skill never deletes** — archival is a property of location (a closed cycle's directory
simply stops changing), and the one move it makes (filings into the cycle's `filings/`) is a
`mv`. It does not commit: its edits and moves land as ordinary working-tree changes for the
owner.

## Stage 1 — Precondition gate

The cycle may close only when **all three** hold:

- **Ledger discharged.** Every item in the Deferred acceptance ledger is either checked
  (`- [x]`) with a dated evidence line, or carries an explicit owner carry-forward ruling
  recorded in the roadmap (a STILL-OPEN first-exercise tail the owner has ruled a standing
  watch rather than a blocking debt). An item that is still a bare `- [ ]` with no ruling
  fails the gate.
  <br>**Only ship-verifiable checks gate closeout.** Briefs written from build-brief tag each
  acceptance check `[ship-verifiable]` (bounded — settles at rest, at the release gate, or on the
  next ordinary upgrade) or `[field-contingent]` (unbounded — needs a field event of a specific
  kind, and names which vault can produce it). **A field-contingent check that has not fired does
  not fail this gate**; it moves to the standing watch register in Stage 2 and the cycle closes over
  it. Gating on both kinds is what left Arc 3 unclosable for eighteen days: nine of its thirteen
  tails were field-contingent and four needed a vault the factory machine cannot read.
  <br>**On an older ledger with no tags** (anything briefed before this rule), classify each open
  item yourself and **show the owner the classification before acting on it** — the tag changes
  whether an item can block, so it is not yours to assign silently. Then take a batch ruling rather
  than thirteen separate ones. Three dispositions cover almost everything, and all three have Arc-3
  precedent: **released as a standing watch** (no reachable subject — the build-19 form: *"recorded
  here rather than ticked — the check was never exercised, it was released"*); **filed as a finding**
  (the event has come and gone repeatedly without the check firing — that pattern is evidence, and
  evidence goes to `factory/inbox/`, the build-15/build-16 form); **carried as inherited debt to the
  next cycle** (a clause exercised and FAILED — the build-20 form). A fourth exists for a check whose event
  can be manufactured cheaply and honestly: **staged**, with the named action written down.
  <br>**Never tick what was not exercised.** A released check keeps its `- [ ]` and says why. If the
  ledger's `[x]` count could be read as a measure of what the cycle proved, add a sentence saying it
  cannot.
- **Release shipped.** The cycle's release version is tagged and pushed. Verify with
  `git tag` — the tag for the cycle's shipped version (e.g. Arc 3 → `v0.6.0`) must exist.
- **No orphan spikes** *(platform P-2, 2026-08-24)*. Read `factory/platform/spikes/` and
  check every register file whose `opened_by:` names the closing cycle. None may still read
  `status: proposed` or `status: running`. Each must be one of: **harvested** (the source was
  read; `verdict:` filled), **killed** by an owner ruling (`status: harvested`,
  `verdict: kill`, with the reason in the file — a question that turned out not to need
  answering), or **explicitly carried forward** to the next cycle, which re-stamps its
  `opened_by:` and lists it in Stage 2's carry-forwards. A cycle does not close over a
  question nobody answered and nobody killed — that is how an external unknown becomes
  invisible and gets re-derived from memory two cycles later. Register mechanics are
  single-homed at `factory/platform/spikes/README.md`; the kill-or-carry ruling is the
  **owner's**, so surface the orphans and take one batch ruling rather than deciding.

If any fails, **stop before moving anything**: report `blocked` with the specific open
items (the missing tag, or the orphan spike ids), and point at `acceptance-discharge` when
an undischarged ledger is the cause. Closing over unresolved acceptance is the exact failure this gate exists to
prevent — do not offer to "close anyway."

## Stage 2 — Record carry-forwards

Collect everything that outlives the cycle and does not resolve at close:

- STILL-OPEN watch items the owner ruled forward (e.g. the vlt-track loop-profile watch).
- Standing metrics a cycle established that keep accruing.
- Deferred questions and design-stage evidence debts (an unmeasured audit, an unrun cycle).
- Owner action items filed elsewhere (e.g. a drift to file upstream to BMAD-METHOD).

Record each in the roadmap's status section in the **Arc 2 carried-item form** — see
`factory/cycles/02-capability-hardening/roadmap.md` (the ledger's carried loop-profile
item and the "Still open elsewhere:" clause in its frontmatter `status`). Phrasing that
travels: *"carried from <origin> — STILL OPEN at cycle close, carries forward past Cycle NN."*
These are the authoritative hand-off point: the next cycle's `inbox-capture` re-lists them from
the closed roadmap. Anything left off is silently dropped.

## Stage 3 — Stamp CLOSED

Rewrite the roadmap frontmatter `status` to the closed form, **in place** — the roadmap
already lives in its cycle directory and never moves. Match the Arc 2 precedent
(`factory/cycles/02-capability-hardening/roadmap.md` frontmatter `status:`), which carries:

- the word CLOSED with the close date;
- the shipped version, ship date, and its commit + tag;
- a one-line acceptance-evidence summary (what upgrade/run discharged it);
- a "Still open elsewhere:" clause naming the carry-forwards;
- the **do-not-append banner**: *"This cycle is closed — do not append."*

From this edit forward the doc is read-only history. Also stamp the do-not-append line into
the roadmap's own "Status & next step" body section if it has one, per the Arc 2 form.

## Stage 4 — Confirm the cycle directory + reset `factory/CYCLE`

Nothing archives by moving: a closed cycle's directory simply stops changing. The roadmap is
already stamped in place (Stage 3) and the briefs already live in
`factory/cycles/NN-<slug>/briefs/` — confirm each brief there belongs to **this** cycle (a
brief numbered for a later, still-open cycle must not sit in this cycle's directory), and
that no stray brief for this cycle sits outside it.

Then **reset `factory/CYCLE` to the "none" state**: keep its comment header lines and replace
the pointer line with the between-cycles form, naming the next cycle number —

```
none — Cycle <NN+1> opens at factory/cycles/<NN+1>-<slug>/ on its inbox-capture run
```

`inbox-capture` writes the real `NN-<slug>` line back when the next cycle opens.

## Stage 5 — Move the accepted filings into the cycle

`mv` each accepted field filing `factory/inbox/<filing>.md` →
`factory/cycles/NN-<slug>/filings/` (the closing cycle's directory). Filings that
`acceptance-discharge` already moved are done — skip them; this stage only catches
stragglers. A filing whose acceptance was **carried forward** (its ledger item is a live
carry-forward, not discharged) stays in the active inbox — leave it and name it in the report.

### The criterion is per-filing, not per-build (widened 2026-07-26, owner-ruled at Arc 3's close)

CLAUDE.md's lifecycle states the standing rule: a filing moves out of the active inbox once **its
build** has shipped *and* passed acceptance. **After a batch disposition that rule moves nothing** —
builds close on rulings, and *released is not passed* — so every filing would sit in the active inbox
indefinitely and **the inbox would lie about what is outstanding**. That is the honest-surface
failure the module files against; it must not live in the lifecycle's own front room.

**A filing moves when both hold:**

1. Every clause traceable to **that filing** is discharged with a dated evidence line; **and**
2. the build's remaining tails are attributable to a **different** filing.

**A filing stays active when its own clause is** a released watch, a dated watch, a filed finding, or
an inherited debt — regardless of how much of its build discharged. At Arc 3's close this moved three
filings whose builds were still open (build-21 A3-15, build-22 F4, build-16 M4 — each fully
discharged, each build's residue belonging to a different filing) and correctly held `091001`,
`091004`, `091006`, the four graduation-queue filings, and three others.

**Do not widen this further.** The bound is condition 2: the moment you find yourself moving a
filing because its build *mostly* worked, you are back to inferring acceptance instead of evidencing
it. Record in the roadmap which filings moved under which criterion, so the next closeout inherits a
rule rather than re-deciding.

### Materialized filings close their issue

The move criterion above is unchanged — this extends the *act* of moving a filing, mirroring
the `mv`. A filing being moved whose header carries `origin: <repo>#<n>` (see the field
contract at `skills/vlt-feedback/references/field-contract.md` — the single home; point,
never restate) gets its issue closed in the same stage:

```
gh issue close <n> --repo <repo> --comment "<shipped version/build + one-line disposition>"
```

The `captured` label stays (history, and the `origin:` header remains the idempotency key
either way). A filing that **stays active** (live carry-forward, still in `factory/inbox/`)
leaves its issue **open**
— the tracker mirrors the inbox, in both directions. If `gh` is unavailable, record the
owed close in the closeout report rather than skipping silently.

## Stage 6 — Fix the front door (idempotent)

`factory/inbox/README.md` once carried a completeness-claiming description of processed
filings that drifted (it named a count that fell behind the real contents) — the
"lists that claim completeness drift" failure, in the lifecycle's own front door. If an
enumerating description is still there, replace it with a non-enumerating pointer:

> A filing whose build has shipped and passed acceptance lives in the `filings/` of the
> cycle that shipped it (`factory/cycles/NN-<slug>/filings/`); the closed cycle roadmaps
> (`factory/cycles/*/roadmap.md`) are the authoritative per-filing record.

This is idempotent: if the README already carries a pointer (no counts, no enumeration),
leave it — the skill maintains **no** list here, ever (standing single-home / point-at-the-map
rule). Do not add this cycle's filings to any list; there is no list to add to.

## Stage 7 — Sync memory

Update the cycle's project-memory topic file (`{project-root}/CLAUDE.local.md` records the
obligation; precedent: the `vlt-arc2-roadmap` memory) to the CLOSED/archived state:
mark it CLOSED with the shipped version and close date, add the do-not-append note, and list
the residual open carry-forwards. Update its one-line entry in the memory `MEMORY.md` index
to match. Keep the memory and the closed roadmap's status saying the same thing.

## Report

Summarize the close:

- **Gate:** passed (or `blocked` with the open items — in which case nothing below ran).
- **Carry-forwards:** each item recorded, by name.
- **Closed:** the roadmap stamped in place, N briefs confirmed in the cycle's `briefs/`,
  N filings moved into the cycle's `filings/` — with the paths — and `factory/CYCLE` reset
  to none.
- **Held live:** any filing left in the active inbox because its acceptance carried forward.
- **Front door:** README fixed, or already a pointer (unchanged).
- **Memory:** topic file + index line synced.

End with the **Next lifecycle move** (routing contract — `.claude/skills/vlt-lifecycle.md`):
the cycle is closed, so the loop restarts at field signal — "next filings (or the recorded
carry-forwards) go through `inbox-capture`, which will find a clean open-cycle slate and
re-list the carry-forwards from this now-closed roadmap." If uncaptured filings already
sit in `factory/inbox/`, say so and name `inbox-capture` as the immediate move. When blocked, the
next move is the route out of the gate cause: `acceptance-discharge` for an undischarged
ledger, an owner carry-forward ruling for an unruled tail, `vlt-release` for a missing tag.

Then emit the headless JSON if `--headless`, with the same move in `next`.
