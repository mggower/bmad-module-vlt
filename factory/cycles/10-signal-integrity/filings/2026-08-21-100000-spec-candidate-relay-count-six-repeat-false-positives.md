# The naive `spec_candidate` relay count fires the same 6 false positives run after run

_Filed 2026-08-21 from the factory on the owner's go-ahead, classification: **defect**
(module-feedback candidate). **Provenance:** lint-surfaced on vlt-core (the 2026-08-16 full
`vlt-lint` run, Arc 8 era — the owner's vault-side report, where this was the
strongest-ordered of three candidates); content recovered from Arc 7's Closeout record item 8
(`skills/reports/archive/inbox-evolution-arc7-roadmap.md:1852-1856` — the substance was never
lost, only the pointer to it); filed 2026-08-21 on the owner's go-ahead discharging ruling
4c's pre-tag bound (Arc 9 roadmap, roundtable A8, discharge route 1)._

## The claim, as recorded in Arc 7's closeout (item 8, verbatim substance)

> the naive `spec_candidate` relay count firing the same 6 false positives for a **third
> consecutive run**

Six handoff docs were flagged as `spec_candidate` by the relay-count signal on the
2026-08-16 full lint, and the same six had been flagged on the two prior full-lint runs. The
count is naive: once a doc has ever accumulated ≥2 `relay:` entries pointing at its path, it
re-fires on every subsequent run, forever, whether or not anything about its candidacy has
changed.

## Grounding against current module source (HEAD 86efd48, v0.11.0)

The check lives at `skills/vlt-lint/references/checks.md:47` (Spec candidates). Current
source has hardened the *count* considerably since the signal was born: relay entries only
(a `consult:` block never increments), drained `{archive}`-mirrored relay history counts
(a drain must not reset candidacy), no stored counter, and — the designed suppression path —
**a candidate with a recorded decline in `{backlog}` or its drained sibling is excluded**,
with the count of honored declines stated beside the finding.

**The defect still stands, in narrowed form.** The signal remains cumulative file state with
no per-run memory: the *only* suppression is an explicit per-candidate decline record. The
decline mechanism (B5-4, shipped v0.9.0, live on vlt-core from 2026-07-30) predates the
2026-08-16 run — so the six repeats persisted *with the designed suppression path already
shipped*. Either the six were never declined vault-side (a UX/ritual gap: three consecutive
runs surfaced them and no run led to six recorded declines), or the decline path is too heavy
for a batch of known-noise candidates. Either way the field evidence is that the shipped
mechanism does not, in practice, stop a stable false-positive set from repeating.

## What a fix might look at (for capture, not a ruling)

- A batch-decline affordance at report time (the report already knows the repeat set).
- Or a repeat-aware report line: "N candidates unchanged since the last run" rather than
  re-listing them at full strength — surfacing *new* candidates loudly and repeats quietly.
