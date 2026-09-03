# The stub-discovery regex drops the stub list, and the sweep manufactures missing targets

_Filed 2026-08-31 from **Cycle 14's third acceptance-discharge run**, surfaced by
`{field-vault}`'s `{lint_reports}/2026-08-30-1123-lint.yaml` — the first full `vlt-lint --full`
sweep under 0.17.1. The sweep diagnosed this defect itself, in its own
`false_positives_refused` slot, and had nowhere to file it. Evidence is `{field-vault}`,
read-only; nothing in the vault was edited._

## The claim

The full-sweep workflow is handed a `stubSlugs` argument so it can tell a **recorded gap** (a slug
registered in the index's stub section, deliberately unwritten) from a **missing target** (a link
pointing at nothing, a finding). The SKILL builds that argument by matching the index's stub
heading with a regex that requires a **bare `## Stubs` heading**. `{field-vault}`'s index writes the
heading as `## Stubs (linked, not yet written)`. The regex misses, an **empty** `stubSlugs` list
reaches the workflow, and every registered stub is reported as a missing target.

Three false `missing_targets` were produced this run — `birria`, `jesse-minter`,
`nfl-draft-safety-archetypes` — all three registered stubs. The sweep caught and refused them:

> `'missing_targets: 5 of 5 refused. THREE (birria, jesse-minter, nfl-draft-safety-archetypes) are already registered in the index''s ''## Stubs (linked, not yet written)'' section and are recorded gaps, not missing targets - they were reported only because this run''s stubSlugs arg was built with a regex requiring a bare ''## Stubs'' heading, so an EMPTY stub list reached the workflow. Instrument defect on the SKILL side, not a workflow defect; fix the discovery regex before the next full sweep.'`

## Why the self-catch is not the answer

The refusal held **this** time because the run's operator read every entry against the index. That
is the expensive path, and it is the path the false-positive discipline exists to make unnecessary.
An empty `stubSlugs` list is silent: the workflow has no way to distinguish *"this vault has no
stubs"* from *"discovery failed"*, so it does the correct thing with wrong input. The failure mode
is a `fix_now` class populated with entries whose legal response is to **create pages that were
deliberately not created** — a mechanical fixer acting on this input writes the vault backwards.

This is the same shape as the report defect filed alongside it (`2026-08-31-104500`): a value the
SKILL derives by pattern-matching prose, handed to a workflow that cannot audit it, with no
enforcement point between.

## Grounding needed at capture

The regex site was reported by the sweep as SKILL-side and has not been located in module source by
this run — the grading here rests on the sweep's own diagnosis plus the observable outcome (three
registered stubs reported as missing). **Capture must ground the exact `file:line` before this is
briefed**, per the standing rule that filings mis-attribute provenance. The two facts a build can
rely on are: the index heading in the field is `## Stubs (linked, not yet written)`, and the
resulting `stubSlugs` argument was empty.

## Companion observation, recorded not filed

The same `false_positives_refused` slot names a fourth refusal that is **not** this defect: the
scanner returned the slug `cornerboxes` where the live link reads
`…espn-top-10-cornerBACKS-2026` — a transcription error in a scanner return, producing a fifth
false missing target. That is scanner variance, not stub discovery, and it belongs with the
reproducibility signal rather than here.

## Candidate directions (not a fix — capture's call)

1. **Widen the discovery match** to any `## Stubs…` heading rather than a bare one. Cheapest, and
   it fixes the observed case; it does not make a future discovery failure loud.
2. **Make an empty `stubSlugs` loud.** If discovery returns nothing, the sweep should say so — a
   denominated line (`stub discovery: 0 slugs found under <heading pattern>`) rather than silence,
   so an empty list is visibly a measurement and not an absence. This is the direction that
   matches the module's own denominated-zero posture elsewhere.
3. **Both** — widen the match and denominate the result, so the next vault whose index words the
   heading differently degrades loudly instead of manufacturing findings.

_Ship-verifiable: a repair to the regex is gradeable at rest; the denominated-zero half is gradeable
on the next full sweep._
