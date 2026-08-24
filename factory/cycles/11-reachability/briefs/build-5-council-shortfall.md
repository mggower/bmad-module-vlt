---
title: 'Build #5 — the council shortfall signal (a partial panel says so instead of reading
  as full)'
status: 'BUILT 2026-08-24 — the council shortfall signal landed in vlt-review-council.js
  (F1: raw parallel results captured before the double filter, lensesSelected + lensesMissing
  ({lens, cause}, unavailable vs failed partitioned by the two existing filter stages) derived
  once, partial-panel log() line; F2: conditional PANEL SHORTFALL segment in the moderator
  prompt, no SYNTHESIS schema change; F3: both keys on all three post-selection returns,
  lensesFielded name/shape unchanged) + the F4 one-clause SKILL.md:41 extension. Verification:
  fixture harness (scratchpad Node script, stubbed log/phase/parallel/agent, args as a JSON
  string) ran all three debate-mode cases — FULL: lensesMissing=[], lensesSelected=4,
  lensesFielded=4, prior keys unchanged, no shortfall segment in the moderator prompt;
  PARTIAL (skeptic available:false, historian null): lensesFielded=2,
  lensesMissing=[{skeptic,unavailable},{historian,failed}], moderator prompt carried
  "PANEL SHORTFALL: only 2 of 4", log() fired ("partial panel: 2 of 4 lenses fielded —
  missing: skeptic (unavailable), historian (failed)"); ZERO: degraded return fired with
  condition and note unchanged, now carrying lensesSelected (4) + lensesMissing (4, with
  causes). The index-alignment assumption HELD — the harness parallel preserves falsy entries
  in place, matching the existing .filter(Boolean) assumption; no fallback needed. Args-parse
  guard at :43 verbatim. Greps: lensesFielded appears only in the workflow, vlt-mint/SKILL.md,
  and decision-log.md; F4 clause present. package-lint A/B/C/E PASS, D SKIPPED — vlt 0.14.0.
  Deviations/notes: no deviations — F1 shape adopted as briefed (identifiers unchanged),
  no .decision-log.md existed, one commit.'
module_code: 'vlt'
created: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-23-111410-council-consult-partial-lens-shortfall-is-silent.md
    (A11-3 — the council double silent filter; the consult half was answered NO at grounding,
    no build there)'
roadmap: 'factory/cycles/11-reachability/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-24): build-5 = A11-3, council only, spike: none,
  binds: none — brief-time questions only (§Questions deliberately left to brief time,
  build-5 entry); the carried candidate (minimal shortfall signal, no error threshold) is the
  ruled direction.'
risk: 'low — one shipped workflow asset, no convention touched, no version bump, no consumer
  walk; the return change is key-additive and every downstream consumer reads by key.'
---

# Build #5 — the council shortfall signal

`vlt-review-council.js` fields its lens panel through a double silent filter: a lens whose
agent dies and a lens whose persona is unreadable are both dropped with no denominator, no
named missing lenses, and nothing in the synthesis output — a partial panel reads as a full
one. The zero case is already loudly guarded; the partial case is the gap (A11-3, the cycle's
honesty-under-partial-shortfall instance). This build lands the carried candidate: a minimal
shortfall signal on the council return — lenses selected vs fielded, the missing lenses named
with their cause where distinguishable, surfaced into the moderator's synthesis — with **no
error threshold**: a partial panel may be legitimate; the ask is that it says so.

Scope is the **council workflow only**. The consult sibling has no fan-out (one agent per
consult, both degrade paths loud and attributed) — the filing's requested parity audit was
answered NO at grounding, and that answer is settled. All rejected alternatives in the parent
filing and capture are settled — do not re-litigate.

## Brief-time dispositions

The roadmap deliberately left three questions to brief time (§Questions deliberately left to
brief time, build-5 / A11-3). Each is ruled here, grounded against current source. This brief
was authored headless; these dispositions are the run's recorded judgment calls.

1. **Does the moderator prompt need to know, or is a return-level field enough? — BOTH, and
   the division of labor is deliberate.** The return-level fields are the *record*; the
   moderator learns of the shortfall so the *synthesis language* can hedge. Grounds: in
   debate mode the four-part synthesis **is** the product handed to a human or filed by the
   Librarian (`skills/vlt-review-council/SKILL.md:45`) — a return key nobody prints never
   reaches that reader, which would reproduce the cycle's declared-but-unreachable defect
   inside its own fix. The moderator receives only the fielded positions inline
   (`vlt-review-council.js:178`) and structurally cannot know what is missing unless told.
   Conversely, the *facts* (selected, fielded, missing, cause) are computed deterministically
   by the workflow and must live as workflow-written return fields, **not** as
   moderator-schema output — an LLM is not the provenance instrument for a count the code
   already has. So: fields on the return (F3), a conditional shortfall paragraph in the
   moderator prompt (F2), and **no change to the SYNTHESIS schema** (it stays
   `additionalProperties: false`, serialized size unchanged against the standing ≤3,700
   schema budget carried from DA11/B10-12 disp. 7).

2. **Is `available: false` worth partitioning from a dead agent? — YES; it is free and the
   remedies differ.** The two causes are already distinguished by the two existing filter
   stages (`:151` `.filter(Boolean)` drops a died/empty agent result; `:152`
   `.filter((p) => p.available !== false)` drops an unreadable persona). Capturing the raw
   results before filtering yields the partition at zero marginal cost. The causes carry
   different remedies — `unavailable` points at the personasPath / governance install (the
   remedy the zero-case note at `:161` already names); `failed` is transient
   infrastructure — so collapsing them would discard signal the code already holds. Each
   missing lens is named with `cause: 'unavailable' | 'failed'`.

3. **Does anything downstream consume the council return positionally? — NO; every consumer
   reads by key, and additive keys are safe.** Grounded across the full consumer set:
   `skills/vlt-mint/SKILL.md:98-100` reads `verdict` / `changes` / `reason` /
   `lensesFielded` by name; the decision-log provenance vocabulary
   (`skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md:53-54`, v3) cites
   "the workflow's `lensesFielded`" and "the workflow's note" by name;
   `skills/vlt-review-council/SKILL.md:41` describes the return by its named sections;
   `consult.md:31` is definitional only. Nothing indexes or destructures positionally. Two
   hard constraints follow: **`lensesFielded` keeps its name and shape** (the v3 provenance
   vocabulary depends on it — renaming would be an unruled convention change), and the
   `additionalProperties: false` on VERDICT/SYNTHESIS constrains *agent outputs*, not the
   workflow's hand-built return object at `:186-192`, which may gain keys freely.

**Interim posture (R1): not applicable** — this build ships the mechanism itself; no rule,
check, or finding class lands ahead of it.

## F-sites

All sites re-grounded against `skills/vlt-setup/assets/workflows/vlt-review-council.js` as of
2026-08-24 (post-build-3 tree, commit `9ccc653`). Every capture-cited line HOLDS at its cited
location; one nuance and one grounding addition are recorded where they apply.

### F1 — the lens fan-out captures its shortfall (`vlt-review-council.js:148-164`)

**Current state.** `:148-152`:

```js
const positions = (
  await parallel(lenses.map((lens) => () => agent(lensPrompt(lens), { label: `lens:${lens}`, phase: 'Lenses', schema: VERDICT })))
)
  .filter(Boolean)
  .filter((p) => p.available !== false)
```

Both filters are silent. `:154-164` guards only `positions.length === 0` (loud: `log()` +
`degraded: true` return). The panel is selected at `:79-96` (kind map or debate default,
capped at 4 by `:96`) — the denominator exists in `lenses` and is currently discarded.
*(Grounding nuance: the filing's "4 of 7" is illustrative — the `:96` cap bounds a real panel
at 4 lenses + moderator; the shortfall shape is unchanged.)*

**The exact change.** Capture the raw parallel results, then derive the partition. Shape (the
builder may adjust identifiers, not semantics):

```js
const rawResults = await parallel(
  lenses.map((lens) => () => agent(lensPrompt(lens), { label: `lens:${lens}`, phase: 'Lenses', schema: VERDICT }))
)
const positions = rawResults.filter(Boolean).filter((p) => p.available !== false)
const lensesSelected = lenses.slice()
const lensesMissing = lenses
  .map((lens, i) => {
    const r = rawResults[i]
    if (!r) return { lens, cause: 'failed' }               // agent died / returned nothing
    if (r.available === false) return { lens, cause: 'unavailable' } // persona file unreadable
    return null
  })
  .filter(Boolean)
if (lensesMissing.length > 0 && positions.length > 0) {
  log(`partial panel: ${positions.length} of ${lensesSelected.length} lenses fielded — missing: ${lensesMissing.map((m) => `${m.lens} (${m.cause})`).join(', ')}`)
}
```

The index-alignment assumption (`rawResults[i]` ↔ `lenses[i]`) is exactly the one the
existing `.filter(Boolean)` code already makes about `parallel` (falsy entries in place); if
the builder finds `parallel` compacts its results, fall back to matching fielded results by
their required `lens` field and attribute the remainder — record whichever held as a
numbered deviation note. The zero-case guard at `:154` keeps its condition and loudness
unchanged.

**Why:** A11-3's core defect — the denominator and the missing-lens names exist in local
scope and are thrown away. The partial case gains the same loudness class the zero case
already has (a `log()` line), mirroring the guard at `:155`.

**Out of scope (this site):** no retry, no error threshold, no minimum-quorum rule — the
capture's carried candidate is explicit that a partial panel may be legitimate; the ask is
honesty, not enforcement.

### F2 — the moderator is told, conditionally (`vlt-review-council.js:171-178`)

**Current state.** `moderatorPrompt` (`:171-178`) hands the moderator the fielded positions
inline and says nothing about selection — the moderator cannot distinguish a full panel from
a partial one.

**The exact change.** Insert one conditional segment into the template (position: after the
map-them-faithfully sentence ending at `:174`, before the mode-specific segment at `:175`):

```js
(lensesMissing.length > 0
  ? `PANEL SHORTFALL: only ${positions.length} of ${lensesSelected.length} selected lenses fielded — missing: ${lensesMissing.map((m) => `${m.lens} (${m.cause})`).join(', ')}. Synthesize ONLY the fielded positions; your synthesis language must not present this as a full panel — say "the fielded lenses" where it matters, and do not attribute silence to the missing lenses. A partial panel is not itself an error; the shortfall must simply be visible in your output. `
  : '') +
```

**No SYNTHESIS schema change** (disposition 1): the moderator hedges *within* the four
existing sections; the deterministic facts ride the return object (F3), not the LLM's
output.

**Why:** in debate mode the synthesis is what a human reads or the Librarian files
(`vlt-review-council/SKILL.md:45`); in mint mode the recorded verdict's reasoning
(`vlt-mint/SKILL.md:99`) is drawn from it. A shortfall the synthesis never mentions is
unreachable by every reader that matters.

### F3 — the shortfall rides every post-selection return (`vlt-review-council.js:156-163, 182-184, 186-192`)

**Current state.** Three returns exist after panel selection: the zero-case degraded return
(`:156-163`), the moderator-failed degraded return (`:183`), and the main return
(`:186-192`). The main return already carries `lensesFielded` *(grounding nuance on the
capture: the fielded names are returned today — but with no selected-set denominator and no
missing-lens names, so the capture's "no denominator, no named missing lenses, nothing in
the synthesis output" holds in substance)*. Neither degraded return carries even that.

**The exact change.** Add `lensesSelected` (string array) and `lensesMissing` (array of
`{ lens, cause }`) to **all three** returns, computed once at F1:

- Main return (`:186-192`): add both keys beside `lensesFielded` (which keeps its exact name
  and shape — the decision-log v3 provenance vocabulary cites it).
- Zero-case return (`:156-163`): add both (`lensesMissing` will name every selected lens
  with its cause — strictly more diagnostic than today's prose note, which stays).
- Moderator-failed return (`:183`): add both beside the existing `positions` passthrough.

**Why:** one computation, uniform record on every exit — a consumer (or a human reading a
mint decision log's captured verdict) can always reconstruct selected vs fielded vs missing.
Key-additive only; disposition 3 grounds that no consumer breaks.

### F4 — the SKILL's degrade sentence names the signal (`skills/vlt-review-council/SKILL.md:41`) — grounding addition

**Current state.** `:41` ends: "It degrades gracefully if a lens persona is missing."
True, and after this build incomplete in the direction A11-3 was filed about — the sentence
is where a reader learns what degradation looks like.

**The exact change (one clause, prose only):** extend the sentence to say a partial panel
declares itself, e.g.: "It degrades gracefully if a lens persona is missing — and a partial
panel says so: the return names the lenses selected, fielded, and missing (with cause), and
the synthesis is told not to read as a full panel."

**Why (EXPANDED, beyond the filing's letter):** a return-level signal documented nowhere is
the cycle's own declared-but-unreachable class reproduced inside its fix. One clause at the
surface where council behavior is looked up closes it. No other doc site restates the return
shape mechanically, so this is the only prose site owed.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row (the council's row is
unchanged — behavior description still accurate). No convention `version:` moves and no
`consumers:`/structure-map change, so no consumer walk and no Group E delta. The workflow's
`// depends_on: []` header (`:11`) is **unchanged and must stay** — this build adds no
convention read (package-lint E5 posture preserved). The operating contract is untouched
(no C6 rule-card re-derivation); no new package-lint check (no E4 declaring case owed).

## Out of scope (dispositioned)

1. **The consult sibling (`vlt-consult.js`)** — answered NO at grounding (no fan-out exists;
   both degrade paths are loud and attributed); the roadmap's build-5 header rules council
   only. Settled, not deferred.
2. **A `lensesShortfall` note in the decision-log provenance vocabulary** — the v3
   vocabulary (`decision-log.md:53-54`) records `council — lenses: <lensesFielded>`; making
   shortfall part of the *provenance grammar* would be a convention rule change (v3 → 4,
   four-consumer re-ack) that no ruling ordered — and build-3 just shipped v3. Not taken.
   The recorded verdict's reasoning inherits the hedged synthesis (F2), which is how the
   shortfall reaches the log today. If the field shows partial-panel mint verdicts recorded
   with the shortfall invisible, that is a new filing.
3. **Retry / quorum / error-threshold machinery** — explicitly outside the carried
   candidate ("no error threshold — a partial panel may be legitimate"). Rejected by the
   capture; not re-litigated.
4. **A SYNTHESIS schema field for the shortfall** — rejected at disposition 1: the facts
   are the workflow's to state deterministically, not the moderator LLM's to echo; the
   schema stays closed and its serialized size unchanged.
5. **`vlt-mint/SKILL.md` prose** — its Step 2a already defers the return-shape vocabulary
   to the workflow and the convention; adding a restatement there would violate
   single-home. Untouched.

## Verification (unit, at rest — lifecycle step 5)

1. **Fixture-harness run (the named instrument — build it in the scratchpad or a temp dir,
   do not commit it).** A small Node script that reads the shipped
   `skills/vlt-setup/assets/workflows/vlt-review-council.js` source, wraps it with stubbed
   runtime globals (`args` **as a JSON string** — exercising the standing parse-on-intake
   rule; `phase`, `log`, `parallel` (executes the thunks), and a scripted `agent` stub), and
   executes three cases in debate mode (4-lens default panel):
   - **Full panel:** all 4 lens stubs return valid VERDICT objects → `lensesMissing` is
     `[]`, `lensesSelected` has 4, `lensesFielded` has 4, prior keys unchanged, moderator
     prompt carries **no** shortfall segment.
   - **Partial panel:** one stub returns `{ available: false, ... }`, one returns `null`,
     two return valid → return names both missing lenses with causes
     (`unavailable`, `failed`), `lensesFielded` has 2, the captured moderator prompt
     contains the `PANEL SHORTFALL: only 2 of 4` segment, and the partial-panel `log()`
     line fired.
   - **Zero panel:** all four unavailable/dead → the `:154` degraded return fires unchanged
     in condition and note, now also carrying `lensesSelected` (4) and `lensesMissing` (4,
     with causes).
   Record the three results in the BUILT status.
2. **Args-parse regression guard:** confirm `:42-43` (`typeof a === 'string' → JSON.parse`)
   survives the edit verbatim — the standing vlt-workflows rule; case 1's string-`args`
   harness input is the executable check.
3. **Greps for cross-file agreement:** `lensesFielded` still present by that exact name in
   the workflow return; `grep -n 'lensesFielded' skills/` shows only the workflow,
   `vlt-mint/SKILL.md`, and `decision-log.md` — no site newly restates the return shape;
   the F4 clause present at `vlt-review-council/SKILL.md:41`.
4. **Handshake bipartite re-check: not triggered** — no `version:` moved, no `consumers:`
   or structure-map change. (Group E rides the mid-cycle lint anyway, next item.)
5. **Packaging lint:** `uv run tools/package-lint.py` A/B/C/E mid-cycle run, exit 0
   (D/`--expect-version` is the release gate, not this build's).
6. **R3: not applicable** — no finding class added or changed (a workflow return field is
   not a lint/dispatch finding class).
7. **R4: not applicable** — no file added to any enumerated class (one shipped asset and
   one SKILL edited in place; the temp harness is never committed).
8. **Scrub:** the changed files carry no personal or vault-local content (the diff touches
   generic workflow code and generic SKILL prose only).

This is not the release build — no version bump here; the bump rides the cycle's release
build. §8 omitted accordingly.

## Acceptance (live — appended to the roadmap ledger)

Two checks; same content as the roadmap's Deferred acceptance ledger bullet for build-5.

1. **`[ship-verifiable]` — GATES closeout.** The shortfall signal behaves correctly at rest
   across full / partial / zero panels: partial runs return `lensesSelected` +
   `lensesMissing` (causes partitioned `unavailable` vs `failed`) alongside an unchanged
   `lensesFielded`, inject the shortfall segment into the moderator prompt, and log the
   partial-panel line; full runs add no shortfall segment and change no prior key; the zero
   case keeps its existing loud degraded return, now carrying the same two fields.
   **Instrument (R1, named at tag time):** the brief's Verification-1 fixture harness — a
   factory-side Node script with stubbed runtime globals and scripted lens results, run at
   rest against the shipped workflow source, `args` delivered as a JSON string.
   **Evidence:** the three recorded case results in the brief's BUILT status.
2. **`[field-contingent]` — does not gate.** A real partial-shortfall council run in a live
   vault surfaces the signal end-to-end: a gated mint or debate in which at least one lens
   dies or a persona is unreadable produces a synthesis that visibly hedges and (mint mode)
   a captured verdict whose reasoning shows the shortfall. **Vault:** `{field-vault}`
   (readable; runs gated mints and debates routinely). **Event:** the first post-v0.15.0
   council run that actually suffers a lens shortfall — a fault condition nothing in the
   plan schedules, so this is unbounded by construction and goes to the standing watch
   register at closeout; the ship-verifiable half is the graded one.
