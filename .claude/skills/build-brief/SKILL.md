---
name: build-brief
description: Scaffolds a build brief from the open cycle roadmap's captured entry and ideation rulings. Use when the user says 'write the build brief for build N' or 'brief build N'.
---

# build-brief

## Overview

This skill runs the Brief step of the module's evolution lifecycle (CLAUDE.md step 5): it
turns a captured, ideated roadmap entry into the open cycle's
`factory/cycles/<cycle>/briefs/build-N-<slug>.md` — the scoped,
`file:line`-grounded, verification-and-acceptance-bearing document a fresh builder session
implements without re-asking what shape a brief takes. Act as the module's build-briefer.

The brief is the most conventionalized *unformalized* artifact in the lifecycle: every brief
to date shares a shape sustained purely by imitation of the last one. This skill codifies that
shape and closes the two failure modes it has bred — (1) capture-time `file:line` sites drift
before brief time, so **every site is re-grounded against current source**; (2) the step most
often forgotten is the one that edits a *different* file — appending the brief's acceptance
checks to the roadmap's ledger — so that append is an **exit gate**, not a footnote.

This skill **consumes** ideation rulings; it never invents them. Briefing ahead of ideation is
the lifecycle violation it must refuse: when the rulings a brief needs are missing, a spike
obligation is open, or a fresh grounding pass contradicts the roadmap in a way only the owner
can rule on, the correct outcome is `blocked`, not a brief. Capture (`inbox-capture`) and
building (a separate session, per brief) are out of scope.

**Lifecycle position:** step 5 (Brief) of the loop mapped in
`.claude/skills/vlt-lifecycle.md` — see it for the full flow, the routes out of each
`blocked` cause, and the routing contract. Every report this skill emits ends with a
**Next lifecycle move** line.

## Conventions

- Bare paths (e.g. `references/brief-anatomy.md`) resolve from the skill root.
- `{skill-root}` resolves to this skill's installed directory.
- `{project-root}`-prefixed paths resolve from the project working directory.
- `{skill-name}` resolves to the skill directory's basename.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` (also the
legacy `{project-root}/_bmad/bmb/config.yaml`) if present. This skill needs none beyond `user_name` /
`communication_language` if set; use sensible defaults otherwise.

Take the build number from the invocation (`brief build 17` → N=17). If none was given, ask.

`--headless` / `-H`: run Discovery → Readiness gate → Re-ground → Author → Exit gate with no
clarifying questions; every judgment call this run made without the user (a scope ruling, a
disposition) gets recorded inline in the brief at the point it applies. On completion, emit
only:

```json
{"status": "complete", "brief": "{path}", "ledger_appended": true, "grounding_corrections": N, "next": "{next lifecycle move}"}
```

`status` is `blocked` with a one-line `reason` when the Readiness gate fails (ideation rulings
for this build are missing, the batch has no Roundtable review record nor owner waiver — or
the record carries OPEN disputes, its `spike:` field is unfilled or names a spike that is not
yet `harvested`/`consumed`, or a declared
evidence debt is neither attached nor ruled not-blocking) or when Re-ground turns up a
roadmap-contradicting site the owner must rule on. **Blocked is the correct outcome in those
cases** — do not author a brief to avoid it.

## Discovery

Find the **open cycle roadmap**: read `factory/CYCLE` — it names the open cycle as
`NN-<slug>` (or "none" between cycles); the roadmap is `factory/cycles/<that>/roadmap.md`.
Confirm via its frontmatter `status` that it isn't closed/shipped. (A closed cycle's roadmap
and briefs stay in that cycle's own `factory/cycles/NN-<slug>/` directory — read there, but a
brief for a closed cycle is almost certainly a mistake; confirm with the owner first.)

In that roadmap, resolve build N to its material by **heading**, never by line number — line
refs drift (the roadmap is append-only and edited across the cycle's life):

- Its row in the **proposed-grouping table** (the build's theme + which filings it folds in).
- Every **per-filing capture** those filings produced (the `### A<cycle>-<i>` subsections), with
  their graded `file:line` findings and carried open design questions.
- The **Ideation rulings** section — every ruling that names build N (grouping/order, the
  decide-once cross-filing rulings, spike records, and the "questions deliberately left to
  brief time"). This section is binding: the brief **cites** it, never re-litigates it.
  **Read the build bullet's `binds:` roster, not only the rulings that name the build.**
  *(Arc 9 roundtable, 2026-08-20.)* Rulings are addressed by **question id** (`Q*`/`D*`/`S*`/`E*`)
  while every consumer resolves by **build number**, and the mapping is written in one direction
  only — so a ruling can govern build N without ever naming it. Arc 9's B9-6 was bound by three
  such rulings, including the ordering constraint that would have shipped a checker against a
  metric home that did not exist. If the bullet carries no `binds:` line, reconstruct it before
  authoring and say so in the brief. **Read the bullet's `spike:` field too** — the
  Readiness gate turns on it, and where it names an `S-N` the register file's findings are
  part of the brief's grounding, not just a gate token.
- Any **Capture addendum** section naming build N — mid-cycle scope deltas owner-ruled after
  the roundtable stamped the batch (`inbox-capture` owns the posture). Its dated addendum
  rulings are part of build N's binding record: the brief folds the addendum filing's
  grounded findings into scope and cites the ruling, exactly as it cites ideation.
- The **Deferred acceptance ledger** — where this build's acceptance checks will be appended
  at the Exit gate.

## Stages

| # | Stage | Purpose | Location |
|---|-------|---------|----------|
| 1 | Discovery | Resolve build N to its roadmap row, captures, and rulings | SKILL.md (above) |
| 2 | Readiness gate | Confirm ideation ran, spikes closed, evidence debts ruled — else `blocked` | SKILL.md (below) |
| 3 | Re-ground | Re-verify every capture-time `file:line` against current source | `references/grounding-at-brief-time.md` |
| 4 | Author | Write the open cycle's `briefs/build-N-<slug>.md` per the anatomy | `references/brief-anatomy.md` |
| 5 | Exit gate | Append acceptance checks to the roadmap ledger; verify present | SKILL.md (below) |

Route to each in order. The carved references are self-contained — don't assume this SKILL.md
is still in context when Author runs.

## Readiness gate

Before grounding or authoring, confirm the build is ready to brief. Any failure → stop and
emit `blocked` with a one-line `reason` (interactive: surface it and ask the owner):

- **Ideation ran for this build.** The Ideation rulings section names build N with a grouping
  and order. No ruling → ideation hasn't happened; briefing now would invent the scope
  decisions that are the owner's to make. Block.
- **The roundtable reviewed this batch.** A `## Roundtable review` section covers the rulings
  batch that names build N and carries no OPEN dispute — or the rulings carry an explicit
  `Roundtable waived (owner)` line. Neither → block (lifecycle step 4: briefing an unreviewed
  plan is how joint defects reach builds); the route is `convene the roundtable`
  (`roadmap-roundtable`). A **capture addendum** naming build N does not fail this gate:
  the batch's roundtable record **plus the addendum's dated rulings** is a complete record
  — *unless* an addendum ruling records a moved joint, in which case a
  `## Roundtable review — addendum` record must cover it (none → block; the route is the
  roundtable delta).
- **Spike obligations are closed.** Read build N's **`spike:`** field in the Ideation rulings
  grouping (lifecycle step 3: external unknowns get spikes). It must read `none`, or name an
  `S-N` whose register file at `factory/platform/spikes/S-N-*.md` carries
  `status: harvested` or `status: consumed`. Anything else → block: a `proposed`/`running`
  spike (the brief would reason from docs and memory instead of the real external source), an
  `S-N` with no register file (the id resolves to nothing), or an **unfilled `spike:` field**
  (an absent ruling is not `none` — the owner says whether a build waits on a spike, not the
  briefer). Register mechanics are single-homed at `factory/platform/spikes/README.md`.
  A pre-register roadmap that carries a dated **SPIKE CLOSED** record instead of a `spike:`
  field satisfies this gate as written — cycles before Cycle 11 predate the register.
  <br>On a **consuming** run (the gate passed on a named `S-N`), append this build to that
  register file's `consumed_by:` and set `status: consumed` — appended, never replaced; a
  spike may be consumed by more than one build.
- **Evidence debts are dispositioned.** Any design-stage evidence debt the roadmap ties to
  this build is either attached, or explicitly ruled not-blocking-the-brief in the rulings. An
  undischarged, unruled debt the brief depends on → block; one that only gates *acceptance*
  (not the brief) is fine — note it and proceed.

## Exit gate: ledger append

The brief is not complete until its Acceptance (live) checks are appended to the roadmap's
**Deferred acceptance ledger** as a dated per-build bullet, and that append is verified present
on disk. This is the load-bearing step this skill exists to make unforgettable.

- Append a bullet matching the ledger's existing shape:
  `- [ ] **build-N (<slug>, briefed <date>):** <the acceptance checks, prose>` — read the
  sibling bullets already in the ledger and match their form (they carry per-check specifics
  and, later, discharge notes appended by acceptance-discharge; author only the `[ ]` briefed
  line). **If a build-N bullet already exists** (this build is being re-briefed), update that
  bullet in place rather than appending a second — never leave two bullets for one build, and
  never overwrite a discharge note a prior acceptance run appended.
- The bullet's checks are the **same** ones written into the brief's Acceptance (live) section
  — single source, two homes: the brief states them, the ledger tracks them.
- **Verify the append landed** (re-read the ledger and confirm the build-N bullet is present)
  before reporting complete. `ledger_appended: true` is earned by that re-read, never assumed.
- **R1/R4 present** — the brief carries the Interim-posture (R1) disposition and the
  Enumeration-widening (R4) statement (`references/brief-anatomy.md` §3 and §7), each either
  substantive or an explicit one-line `not applicable`. Absent → the brief is not complete.
- **Scrub the `title:`** before reporting complete: re-read the authored title and confirm it
  carries no personal or vault-local content. It ships verbatim into the public `CHANGELOG.md`
  (see `references/brief-anatomy.md` §1). A title that does not pass is rewritten, not shipped.

## Handoff

**Interactive:** state where the brief landed, that its acceptance checks are in the ledger,
and any grounding corrections issued (with the superseding notes they wrote into the roadmap).
Ideation is not re-opened.

**Next lifecycle move** (routing contract): a **fresh builder session** implements this
brief via `bmad-workflow-builder` (the brief's `status:` line says exactly this). Name the
builder's exit obligations so the session doesn't have to rediscover them: rewrite the
brief `status:` to a BUILT record with numbered deviations, delete any `.decision-log.md`,
one commit for the build. When blocked, the next move is the route out of the specific
gate cause (see the lifecycle map), not a brief.

**Headless:** emit only the JSON contract above; the same move goes in `next`.
