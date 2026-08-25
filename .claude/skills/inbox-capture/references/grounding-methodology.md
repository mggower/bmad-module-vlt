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
