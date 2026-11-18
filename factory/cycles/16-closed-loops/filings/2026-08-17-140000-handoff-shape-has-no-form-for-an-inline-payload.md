# The `handoff` shape has no form for a delivery whose payload is written inline

- **filed:** 2026-08-17
- **vault:** vlt-core
- **kind:** defect / missing-shape
- **surface:** `vlt-dispatch/references/relay.md` (the three shapes + key requirements),
  `vlt-dispatch/references/ledger.md` (pointer integrity)
- **found by:** `acceptance-discharge` run 1 — the post-0.10.0 `vlt-dispatch ledger` run that
  discharged B7-5 check (4) surfaced this as a by-product. The check itself passed.

## What happened

The first post-0.10.0 `ledger` run on vlt-core reported **7 pointer-integrity findings**, all
the same shape: the 2026-08-15 21:30–22:10 batch of `researcher → librarian` relays are
header-annotated `handoff` but carry no `_agent/handoffs/` path. Six of the seven carry a
`ref:` instead. All seven are already drained.

The payload in each case was **written inline in the relay block** — there is no handoff
document, because none was ever produced. The Researcher had a real delivery to make and
picked the only shape that reads as "I am delivering something to you."

## Why the shipped vocabulary has no right answer here

B7-5 shipped three shapes and their key requirements:

- `handoff` — keyed by a **path** on disk. Wrong: no doc exists.
- `ask` — keyed by `ref`. Wrong: this is not a question.
- `answer` — keyed by `ref`. Wrong: nothing was asked. These were unsolicited deliveries.

So an **unsolicited delivery with an inline payload** has no legal shape. A7-11 filed exactly
this class ("relay requires a path for traffic that has no doc") and B7-5's answer was the
`ask`/`answer` pair keyed by `ref` — which covers *solicited* pathless traffic and leaves
unsolicited pathless delivery uncovered. The field then did the locally-correct thing:
`handoff` + `ref`, a form the shipped rules do not define, and the receiver check duly flags
it seven times.

Note the shape of the miss: this is the arc's own through-line ("the vault does the
legitimate thing and the module has nowhere to put it") reproducing itself **inside the build
written to fix it**.

## Grounding against module source

- `relay.md` states the three shapes and the `(handoff-path | ref, to-slug)` key as its single
  home — a `handoff` with a `ref` and no path is undefined, not merely discouraged.
- `ledger.md`, *Pointer integrity*: the finding's stated legal response is "the publishing
  partner re-fires the relay correctly keyed; the recipient checks the malformed line off as
  superseded." **That response is unavailable here** — there is no correct key to re-fire
  with, because no path exists and no shape accepts a bare `ref` for unsolicited delivery.
  A finding class whose legal response cannot be performed is an R3 violation.

## Candidate dispositions (for ideation, not pre-ruled)

1. Widen `answer` to cover unsolicited delivery (drop the "responds to an ask" precondition),
   keyed by `ref`. Cheapest; slightly weakens the ask/answer pairing.
2. Add a fourth shape (`deliver`/`note`) keyed by `ref`, leaving the existing three untouched.
3. Rule inline payloads illegal and require a doc — i.e. the publishing partner must write a
   handoff file. Honest but heavier; pushes back on the field's actual working habit.
4. Leave the vocabulary and fix the legal response instead: state that a drained malformed
   pointer is annotated in place, never re-fired.

## Field disposition already taken

None retro-fixed. The owner's read on the run: the signal is the Researcher's publish-side
reflex (handoff shape with a `ref` instead of a path), worth correcting going forward rather
than rewriting history. All seven were drained, so nothing was lost.

## Attached lead

The `ledger` legacy-line denominator could not be reproduced from the factory: a
block-header-scope grep of `_agent/dispatch.md` yields 37 un-annotated pathless relay blocks,
a per-pointer-line grep yields 2, and the run reported 18. `ledger.md`'s phrase "un-annotated
**pathless** pointers" does not say whether the unit is the relay block or the pointer line,
nor whether a payload `[[wikilink]]` counts as a path. Not a defect on its own — the check it
serves passed — but the count is unverifiable by a second reader, which is the property the
denominated-line idiom exists to provide.
