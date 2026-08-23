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

## Open design questions

A filing may carry open questions it deliberately didn't resolve. Carry them into the roadmap
as-is (a labeled "open design questions" note) rather than resolving them yourself — that
resolution is ideation's job, not capture's.

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
