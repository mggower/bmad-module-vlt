# Roadmap Synthesis

Fold this run's grounded findings into the cycle roadmap Discovery identified — amend the
open one, or create a new one if none is open.

## The roadmap doc IS the decision log

This skill doesn't keep a separate `.decision-log.md`. The roadmap doc's frontmatter +
capture narrative already carry that role across the cycle's whole lifetime (every closed
roadmap under `factory/cycles/` does this) — don't introduce a second, redundant
artifact. Every judgment call this run made (which filings were covered, how a claim graded,
what got deferred) belongs in the doc itself, in prose, at the point it's relevant.

## Frontmatter

```yaml
title: 'Cycle NN — <short signal-cluster theme>'
status: '<open — one line on where the cycle stands>'
module_code: 'vlt'
created: '<date this cycle opened>'
updated: '<today>'
derives_from:
  - 'factory/inbox/<filing>.md'
  # one entry per filing folded in across this cycle's whole life, not just this run
predecessor: 'factory/cycles/<prior NN-<slug>>/roadmap.md (Cycle N-1 — CLOSED, builds #.. shipped vX.Y.Z)'
intent: >
  One paragraph: what this cycle is capturing and why these filings read as one story.
```

`derives_from` and the capture body are **append-only** across the cycle's life — a later
run that opens the same still-open roadmap adds new filings' sections and extends
`derives_from`; it never removes or rewrites a prior run's grounded capture.

## Body shape

Follow the precedent in `factory/cycles/02-capability-hardening/roadmap.md`:

- `## The through-line` — why these filings (the ones covered so far in this cycle) read as
  one story, not a flat list. Rewrite this section each time new filings join the cycle,
  since the through-line can shift.
- `## Capture — <N> filings (grounded against module source <date>)` — one subsection per
  filing, titled `### A<cycle>-<i>. <short title> (<filing date>) — <filing filename>`, holding
  the graded findings from `references/grounding-methodology.md` (confirmed / provenance
  correction / superseded / gap-confirmed, with exact `file:line` citations) and, where the
  filing already resolved its own design, the exact module-side changes it implies.
- Carry forward each filing's open design questions verbatim in their own subsection or
  callout — don't resolve them here.

## New cycle vs. amend

- **New cycle** (no open roadmap): pick the cycle number (one past the highest existing
  cycle directory under `factory/cycles/`) and a slug from the cycle's theme, create
  `factory/cycles/NN-<slug>/roadmap.md` with the full shape above from scratch, **and write
  the `NN-<slug>` line into `factory/CYCLE`** — this is what opens the cycle
  (`cycle-closeout` resets the pointer to none).
- **Amend** (an open roadmap exists): read it in full first, then extend — new filing
  subsections appended to Capture, `derives_from` and `updated` extended, the through-line
  section rewritten if the new filings change the story. Never touch a closed
  roadmap.

## Mid-cycle capture addendum

When the open roadmap's current batch is already roundtable-stamped (the mid-cycle posture —
SKILL.md's Discovery owns the rule of *when* this applies and the unbuilt-only/joint-test
constraints), grounded findings don't join the original Capture section as if ideation
never ran. Append instead, after the existing Roundtable review record (append-only order
preserved):

`## Capture addendum — <date> (mid-cycle)` — per-filing subsections in the standard
`### A<cycle>-<i>. …` shape (numbering continues the cycle's sequence; `derives_from` and
`updated` extend as usual), each closing with a dated **addendum ruling** the owner made
in-session:

- **Ruled into:** build N (unbuilt) — the scope delta in one sentence.
- **Joint test:** `joint moved: none` — or the named joint, which makes a roundtable
  delta the next move before that build's brief.

`build-brief`'s record gate reads these rulings as part of the batch's review record —
write each one so a later reader can verify build N's widened scope without this
session's context.

## Handoff

This skill's job ends at a grounded, current roadmap doc. **Restamp that roadmap's foot** — its **last block**,
below any earlier routing — with the **Next lifecycle move**, then close the run with the same line (routing contract,
`.claude/skills/vlt-lifecycle.md`) — **the roadmap's foot is the obligation; the chat report is
a copy** *(platform P-13)*. Normally
*owner-steered ideation* — the owner rules on grouping, order, and scope, recorded in the
roadmap's Ideation rulings section — after which each ruled build goes to the
`build-brief` skill (`brief build N`). If this run's captures joined a cycle whose ideation
already ruled on them, route straight to `build-brief`. Headless: the same move goes in
the JSON `next` field.
