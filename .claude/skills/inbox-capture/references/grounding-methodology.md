# Grounding Methodology

For each filing this run covers, verify every claim it makes against the module source as it
exists right now — not as the filing describes it, not from memory of what the module used to
do. A filing is a snapshot from whoever wrote it; the module may have moved since, or the
filing may have simply gotten the site wrong.

## What grounding means in practice

For each distinct claim a filing makes (a bug, a gap, a proposed fix, a "the module already
does X" assertion):

- **Locate the real site(s).** Grep/read the actual files the claim is about — don't take the
  filing's cited `file:line` on faith; re-derive it.
- **Classify the outcome:**
  - **CONFIRMED** — the claim holds, at the site(s) verified. Cite exact `file:line`.
  - **PROVENANCE CORRECTION** — the filing mis-attributes something to module source that's
    actually vault-local (a partner's own memory, a decision log, a local convention). Say so
    explicitly and point at what the module *actually* says instead.
  - **SUPERSEDED** — a prior build already shipped this; the filing was written against a
    now-stale module state. Cite what shipped and where.
  - **GAP CONFIRMED** — the claim describes something genuinely missing or inconsistent, and
    grounding didn't change its shape, only sharpened the exact site(s).
- **Note residual scope.** Grounding often shrinks what's left to actually do (a "fix" claim
  might turn out to already be half-shipped) — say what's left, not what the filing originally
  asked for.

## The second grounding axis — recover the set behind a count

*(Platform P-18 Tier A, 2026-09-01; cause `ST-5`, *specimens have no owner*.)* Everything above
grounds a filing against **module source** — code, conventions, shipped prose. That axis cannot
see a filing's *evidence*, and the standing rule that grounding reads current module source is
sometimes read as forbidding anything else. It does not: source is what a **claim** is checked
against; a filing also carries **observations**, and those are checked against the artifact they
were observed in.

So when a filing reports a **count where a set was observable** — *"18 entries"*, *"two of two
miscounted"*, *"145 pages, 42 unattested"* — do not simply carry the number forward:

- **Dereference the named evidence.** The filing cites where it looked (a persisted lint report,
  a session report, a report key and line). Open it and recover the members.
- **Record the recovered set in the capture entry**, as the manifest shape at
  `factory/inbox/README.md` defines it — full set plus the minimal triggering fragment. The
  capture entry is where it becomes durable; the filing stays as filed.
- **When recovery fails, say which and why.** *"18 reported; report persisted the count only, no
  slug list at `<path>` — set unrecoverable"* is a grounded finding and belongs in the entry. The
  failure is itself signal about the instrument that produced the report.
- **Attrition is worth a line.** If a filing observed N and preserved M < N, note it. That ratio
  is the number `ST-5` is about, and a build's brief is entitled to know its evidence is partial
  before it constructs a fixture to stand in for the missing part.

**This does not license spelunking.** Dereference what the filing **names**; if it names no
evidence artifact, there is nothing to recover and that absence is the finding. Nor does it
change the grades above — a recovered set sharpens a CONFIRMED or GAP CONFIRMED, it does not
become a fifth outcome.

## Grounding a `supersession` filing

*(Platform P-15, 2026-08-25.)* A filing marked `class: supersession` claims a shipped
protection is now **redundant**, not broken (`factory/inbox/README.md` defines the class).
Grounding it is a different question from grounding a defect, and reading it as one turns a
retirement into a fifth exception:

- **Verify both halves separately.** The rule still exists and still binds (cite its
  `file:line`); the named mechanism shipped and its **population covers the rule's**. A
  mechanism covering a narrower population does not supersede — say so, and say what is left
  uncovered. That gap, not the rule, is the residual scope.
- **The outcome grade is about the claim, not the fix.** CONFIRMED here means *the redundancy
  is real*; GAP CONFIRMED means the mechanism does not yet cover what the rule stands in for.
  Do not grade it **SUPERSEDED** — that grade means the module already fixed what a filing
  reported, and the collision reads a live retirement as stale news.
- **Capture the retirement, not a carve-out.** The captured entry names the rule to retire and
  the mechanism that earns it. Whether it retires, narrows, or survives is ideation's ruling;
  a capture that quietly converts it into a new exception has re-filed the symptom.

## Does this cause already have a study?

*(Platform P-14, folded 2026-08-25.)* Ask it once per filing, at the moment you have the cause
in hand and are already reading source: **does `factory/studies/` hold this cause already?** The
register is small; `ls` plus the README's index table is the whole check.

- **It does** — the capture **cites the `ST-N`** and states only what is new: the fresh
  instance, the residual scope, and any way the filing sharpens or contradicts the study. Do not
  re-derive the diagnosis in the roadmap; that duplication is what the register exists to end.
  Append the capture to the study's `cited_by:`.
- **It does not, and the cause is bigger than this filing** — say so in the capture. Whether a
  study gets opened is the author's call and needs no ruling (`factory/studies/README.md`,
  *Opening a study* and *Citable, never blocking*); an unopened one is a missed chance, never a
  blocked capture.

**This is a prompt, not a gate.** No filing is held, and a run that asks and finds nothing has
answered it. The whole cost is one question against a directory listing.

*Why it is here:* the register's failure mode is not "no studies written" — it is **a cause
re-derived that a study already holds**, which has now happened twice (ST-1 → ST-2 at five days;
the 2026-08-24 session → ST-2's RC2 at one day). Both times the register was empty or tiny, so
size was never the problem: **nobody thought to look.** Grounding is the one beat that is
already reading source for a cause, which makes it the only cheap place to ask.

## Open design questions

A filing may carry open questions it deliberately didn't resolve. Carry them into the roadmap
as-is (a labeled "open design questions" note) rather than resolving them yourself — that
resolution is ideation's job, not capture's.

## When grounding hits an external unknown

Sometimes grounding cannot finish, because the answer isn't in module source at all: it lives
in an external tool's real behavior, an upstream package's actual code, a live vault's real
content. That is a **spike** (CLAUDE.md step 3: read the actual external source, never its
docs or your memory of them), and the question is at its sharpest right now — at the moment
grounding failed to answer it.

Open a `proposed` stub in the spike register: one file at
`factory/platform/spikes/S-N-<slug>.md`, id one past the highest existing, with the question
written in the one form that matters — *what would a real source have to say?* Mechanics
(ids, statuses, frontmatter, the gates) are single-homed at
`factory/platform/spikes/README.md`; point at it, never restate it. Note the stub's id in the
filing's capture so ideation sees it.

**A stub is a question with an id, not a ruling.** Capture never runs the spike, never rules
that a build depends on it, and never lets the unknown silently become an assumption in the
capture text — say plainly that the claim is ungrounded pending `S-N`. Whether it binds a
build is ideation's call; whether it blocks a brief is `build-brief`'s gate.

## Cross-filing relationships

When two or more filings in the same run share a pattern, a dependency, or one adopts a
convention the other proposes, say so in the roadmap narrative — this is what makes a batch of
filings read as one cycle's story instead of a flat list.

## Style precedent

`factory/cycles/02-capability-hardening/roadmap.md` is the reference example of this
method applied — read it for the level of specificity expected (exact `file:line` citations,
explicit rejected-alternative reasoning where a filing already resolved its own design, "ruling
to enshrine" framing for decisions the filing already made). Match its rigor, not its length —
a thin filing gets a thin, honest capture; don't pad.

Once every filing this run covers has been graded, proceed to `references/roadmap-synthesis.md`.
