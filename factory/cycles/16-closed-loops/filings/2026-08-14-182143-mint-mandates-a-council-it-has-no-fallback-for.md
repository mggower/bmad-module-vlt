# `vlt-mint` mandates a council verdict but names no path when the panel cannot be fielded — so a gated mint either stalls or improvises, and nothing marks which happened

_Filed 2026-08-14 from **vlt-core**. Classification: **defect** (a missing path, not a wrong rule).
Surfaced during — and by — the `convention edit` mint that produced today's two companion filings
(`2026-08-14-180949-…`, `2026-08-14-181000-…`). This one is about the ceremony those two ran
**inside**, so it is worth capturing alongside them._

## The claim

`vlt-mint`'s blast-radius gate is unconditional for the gated kinds, and its language is emphatic:

- **Step 2a** — *"Capture is mandatory, not optional. Before the mint goes live, record the verdict
  **and its reasoning** … A gated change must carry its own rationale."*
- **Phase 2 exit gate** — *"the council verdict is **resolved** (a `pass`, or a `revise` applied and
  re-staged to pass) **and** every open user-decision is **ruled**."*

Neither names what to do when **the panel cannot be fielded at all**. Step 2a's step 2 says to invoke
the workflow; steps 3–4 describe capturing and acting on what it returns. There is no branch for "the
Workflow tool is unavailable in this environment." So a gated mint meeting that condition has exactly
two options, and the skill sanctions neither:

1. **Stall** — refuse to leave Phase 2, leaving the change unshipped.
2. **Improvise** — substitute some other form of review and proceed.

This vault took option 2.

## What actually happened

The mint ran in a **background job** whose harness defaults workflow fan-out to off unless the user
explicitly asks for it. (**Explicitly not filed as module feedback:** that restriction is
Claude-Code-side, not `vlt` module source — it fails this operation's module-source test. It is
described here only because it is the condition that exposed the gap. Any environment that cannot
spawn subagents — a constrained runner, a headless CI-style invocation, a tool-restricted session —
reaches the same place.)

With the panel unavailable, the mint staged the three edits to their live paths as Step 2a step 1
requires, then substituted **a user review of the staged diff** for the panel, and recorded:

> `verdict: user-ruled pass (council **not** fielded — the session's harness config forbids workflow
> fan-out without an explicit request, so the gate was run as a staged-diff review by the user, who
> is the boundary-setter here). Verdict captured per the mandatory-capture rule; the substitution is
> recorded rather than glossed, because a gated kind that skipped its panel should say so.`

— `_agent/mint/decision-log.md`, entry `## [2026-08-14] convention-edit — the address rule…`
(mirrored in `_agent/mint/2026-08-14-knowledge-gap-routing.md`, Phase 2 checklist line).

That worked, and for **this** mint it was arguably the right substitute — the user is the vault's
boundary-setter, the change was three files, and the review caught real things. But the honesty of
that record is entirely discretionary. Nothing in the module asked for it, nothing checks for it, and
a mint that had simply written `verdict: pass` would be indistinguishable in the log from one that
fielded four lenses.

## Why this is worth a build rather than a shrug

- **It is the module's strictest gate, and the improvisation happened inside it.** Every other
  ceremony in `vlt-mint` has a cheap path (`council-none` kinds "pass *through* the phase" trivially).
  The gated kinds are the ones where the module has decided review is non-negotiable — which is
  exactly where an unnamed escape hatch is most expensive.
- **The failure is silent by construction.** The decision log is the permanent, upgrade-durable
  record, and its `verdict:` field has no vocabulary for *how* the verdict was reached. A future
  reader — or `vlt-upgrade`'s reconcile pass, or a factory capture — sees a verdict string and cannot
  tell a panel from a substitute from a rubber stamp.
- **The stall path is already almost built.** This is the part that makes it cheap to fix: Phase 1
  already specifies a **resumable planning doc** at `_agent/mint/{date}-{slug}.md` with "the current
  phase + a done/pending checklist", and activation already scans for an incomplete one and offers to
  resume. **The machinery to park a mint mid-Phase-2 and pick it up in an environment that can field
  a panel exists and is exercised.** It simply is not named as the response to an unavailable council.

## The design question this filing does not presume to answer

Two defensible resolutions, and the choice is the factory's:

1. **A user-ruled verdict is a legal verdict type for a gated kind** — with a *required* companion
   field recording that the panel was not fielded and why, so the substitution is structural rather
   than a well-behaved author's discretion. Cheap; keeps constrained environments productive; risks
   normalizing the escape.
2. **The mint refuses to proceed** — Phase 2 becomes hard-blocking, the planning doc parks, and the
   mint resumes wherever a panel can run. Preserves the gate's meaning exactly; costs a round trip,
   and in a vault whose sessions are frequently headless it may mean gated mints rarely finish where
   they start.

A third, if the factory wants the gate's *function* without its *fan-out*: name a **degraded panel**
— the moderator's four-part synthesis produced inline by the minting context against the same
`{personas}` lenses, explicitly labelled as single-context. Weaker than N independent lenses and
should be recorded as such, but it is a named path rather than an improvisation.

## Adjacent prior filing (not a duplicate)

`2026-07-16-153000-new-partner-fields-one-lens.md` reports that the highest-stakes mint gets the
thinnest **panel composition**. This filing is about panel **availability**. They point the same
direction — the council is the module's least-defended machinery — but a fix for either leaves the
other standing. Worth capturing into the same arc if one exists.

## Provenance guess — marked as a guess

Guessing: the council gate was specified assuming an **interactive foreground session**, where
Workflow is simply always there, and the environment question was never asked. `vlt-mint`'s overview
does contemplate non-interactive use ("Runs in-flow … or interactively"), and several sibling ops
name headless behaviour explicitly — so the likelier shape is not that headless was forgotten
entirely, but that it was reasoned about for the **cheap, council-none** paths and never re-checked
against the **gated** ones, where it is load-bearing. I have not read module history to confirm any
of this, and the capture pass should re-ground it.

## One vault-side consequence, for calibration

Because the gate was substituted rather than skipped, the mint did ship — and it shipped **base**
convention edits (`frontmatter` 5→6 with a full consumer walk). So the quality of that substituted
review is now load-bearing on two upstream filings and a standing base divergence in this vault. That
is not a complaint; it is the honest statement of what the missing path cost, so acceptance can weigh
it.
