---
title: 'Cycle 15 — nothing reads it back'
status: 'open — captured 2026-09-01 (16 filings graded: 15 captured here, 1 routed to the platform ledger as P-22). Ideation COMPLETE 2026-09-02 — seven owner-steered rounds, every slot ruled; 7 builds, 1 release (v0.18.0), all promises ratified. Roundtable review CONVENED 2026-09-02 — full 13-voice roster, 21 amendments applied, 2 standing rules declared (R1, R2 → [P-24]), 6 owner rulings live, 0 open disputes; the key was re-ruled (facts-not-verdicts + scanModel), build-4 replaces the scanner\'s link return, both retirements gained their handshake lines. Build-1 BRIEFED 2026-09-02 (`briefs/build-1-supersession-kind.md`, 5 checks in the ledger, 3 grounding corrections). Next: a fresh builder session implements the build-1 brief.'
module_code: 'vlt'
created: '2026-09-01'
updated: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-08-26-123151-lint-full-inline-args-payload-costs-the-caller-84kb.md'
  - 'factory/inbox/2026-08-27-153000-persisted-lint-report-is-not-machine-readable.md'
  - 'factory/inbox/2026-08-27-160000-summary-length-check-counts-the-raw-yaml-line.md'
  - 'factory/inbox/2026-08-27-160100-orphan-false-positive-two-consecutive-sweeps.md'
  - 'factory/inbox/2026-08-27-160200-governance-memory-denominator-missed-twelve-entries.md'
  - 'factory/inbox/2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md'
  - 'factory/inbox/2026-08-31-104501-stub-discovery-regex-drops-the-stub-list-and-manufactures-missing-targets.md'
  - 'factory/inbox/2026-08-31-152000-para-type-carve-out-is-an-enumeration-of-one-and-penalizes-accurate-vocabulary.md'
  - 'factory/inbox/2026-09-01-093000-the-findings-cache-cannot-survive-the-release-that-makes-it-needed.md'
  - 'factory/inbox/2026-09-01-140600-ruleset-fingerprint-inputs-are-under-specified-and-a-wrong-reading-is-silent.md'
  - 'factory/inbox/2026-09-01-140601-same-page-heading-anchors-are-reported-as-missing-targets.md'
  - 'factory/inbox/2026-09-01-140602-a-scanner-substituted-a-proper-noun-and-the-cache-made-it-permanent.md'
  - 'factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md'
  - 'factory/inbox/2026-09-01-170000-supersession-the-verified-by-roster-is-superseded-by-the-authorization-net.md'
  - 'factory/inbox/2026-09-01-183000-rail-kind-set-has-no-value-for-a-supersession.md'
predecessor: 'factory/cycles/14-no-enforcement-point/roadmap.md (Cycle 14 — CLOSED 2026-09-01, builds 1–5 shipped v0.16.2 / v0.17.0 / v0.17.1)'
intent: >
  Cycle 14 asked what happens when a rule has no enforcement point. Cycle 15 asks the harder
  version: what happens when a *value* has no enforcement point. Fourteen of these fifteen
  filings are one shape — the module specifies a derivation in prose, an executor renders it,
  and the rendered value is consumed without ever being compared back to the specification that
  asked for it. That holds whether the executor is an agent (a scanner substituting a proper
  noun, dropping a `#`, under-returning links, measuring the wrong string) or the SKILL's own
  operator (a stub list rendered by a regex that ships nowhere, a fingerprint slot rendered as
  the wrong type, a denominator that missed a fifth of its population). It holds at the output
  end too: the persisted report's shape is stated in one file and enforced in none, so two
  renders with no code change between them produced different shapes. Every one of these
  failures is silent by construction, because a wrongly-rendered value and a legitimately-absent
  one produce the same observable — which is why the module's honest-degradation posture, which
  is real and works, cannot fire. That cause is opened as `ST-7`. Against it sit two
  retirements — the loop's first `class: supersession` filings — which are the same disease read
  from the other end: a closed enumeration standing in for an honest field that now has a net
  behind it. Cycle 14 said rules need enforcement points. Cycle 15 says nobody reads anything
  back.
---

## The through-line

**Nothing in the loop compares a value against the thing that specified it.**

The module is unusually good at *stating* how a value is derived. `full-scale.md` step 2 specifies
its two digest slots down to the instrument, the merge order, the encoding and the truncation, and
says out loud why that precision is there: *"an executor that follows them lands on the same value
every run, **which is the property that failed**."* Two slots later, in the same paragraph, the
component slots get one word each — *"verbatim"* — and both were read wrongly on first contact with
the field, at a cost of 96% of the scan phase.

That is the cycle in one paragraph: **the module already knows this lesson, wrote it down, applied
it to half the slots on one line, and has no mechanism that would ever make the other half's
absence visible.**

Read the fifteen captures by *who renders the value* and the story is flat:

| Executor | Value | What arrived | Entry |
|---|---|---|---|
| page scanner (haiku) | outbound links | `cornerboxes` for `cornerbacks` — a substituted proper noun, now **permanent in the cache** | A15-4 |
| page scanner | outbound links | a same-page anchor with its `#` dropped, becoming a page target that cannot exist | A15-3 |
| page scanner | outbound links | under-returned, shortening the inbound map and manufacturing orphans — **3 consecutive sweeps, 100% of all orphans ever reported** | A15-1 |
| page scanner | summary length | the raw YAML line measured instead of the parsed scalar — biased toward flagging compliant values | A15-5 |
| SKILL operator | `stubSlugs` | **empty**, from a regex that exists in no file the module ships | A15-2 |
| SKILL operator | `pin_vector`, `convention_digests` | wrong type / wrong population — 146 of 146 pages uncacheable, silently | A15-10 |
| SKILL operator | `governance_memory` denominator | 47 where the truth was 59 — and *nothing about the output looked wrong* | A15-6 |
| SKILL renderer | the persisted report | keys dropped, a mandated per-file list collapsed to one string — **intermittently**, across two renders with no code change | A15-8 |
| SKILL renderer | the persisted report | one archive in six does not parse at all | A15-7 |

Nine instances. Four executors. **Zero read-backs anywhere in the tree.**

Two consequences make this cycle's version worse than a list of false positives.

**First, the failures are silent by construction, and that defeats the module's own best habit.**
The module degrades honestly on *absence* — `full-scale.md` states the cold-branch posture
explicitly and it works. But a wrongly-typed `pin_vector` **is** an absent `pin_vector` from the
consumer's side; an empty stub list from a failed regex is the same value as an empty stub list
from a vault with no stubs. The instrument built to make degradation loud reports the honest cold
branch and says nothing, because from where it stands nothing was wrong. `coverage_caps` names
*which slot was absent* and can never name *your rendering was wrong*.

**Second, the cache — which finally started working — has begun freezing the errors.** This is
the genuinely new fact of the cycle and it inverts a success. Cycle 14 build-2 repaired the
findings cache, which had shipped broken for three cycles; it now reuses 145 of 146 records. A
scanner's substituted proper noun is therefore served from the sidecar on every subsequent sweep,
and **re-running the lint — the ordinary response to a suspect finding — cannot re-derive it**,
because reuse is the cache working correctly. The window in which a wrong derivation was cheap to
catch has closed. A15-4 is the specimen; A15-9 and A15-10 are why the window's economics matter.

**And the cost of looking is itself the third act.** The one instrument that could catch these —
a full sweep — costs 146 agents and ~591k prompt chars cold, and the cache is invalidated by
`module_version`, so *every release forces a cold sweep whatever the release contained* (A15-9).
The cheap instrument exists and cannot be trusted; the trustworthy instrument is priced out of
the loop it verifies.

**The two retirements are the same disease read from the other end.** A15-12 and A15-13 are the
loop's first two `class: supersession` filings — the rail platform P-15 shipped on 2026-08-25 for
exactly this and which sat unused for a week while the thing it was built for happened again.
Both ask that a **closed enumeration** be retired because a **net now checks the honest field** it
was standing in for. Where the rest of the cycle is *a value nobody reads back*, these two are *a
value the module reads back against the wrong thing* — a folder deciding whether to believe a
`type:` the file already declared, a roster deciding whether to believe a `verified_by:` the
container's `writers:` list can now adjudicate directly. A15-13's proof is the sharpest artifact
in the batch: `para_writer_unauthorized` resolves `verified_by:` → *partner slug*, and
`write-verification.md:47` makes that value **illegal**, so the authorization net ships a leg no
conformant vault can ever exercise. Two shipped clauses that cannot both be satisfied.

**One entry is not about the module at all**, and it belongs here anyway: A15-15, the rail's `kind`
set has no value for a supersession, so the loop's first two retirements had to be filed as
`candidate` with an apologetic note in the body — where no label filter, no form router and no
triage check can read it. The module has four filing classes and its transport carries three.

### The cause is opened as a study

Grounding kept finding one shape under seven filings from four separate sweeps, which is this
register's own named trigger for opening one. **`ST-7` — prose-specified derivations have no
read-back** (`factory/studies/ST-7-prose-specified-derivations-have-no-read-back.md`) carries the
full diagnosis, its four causes, its rejected alternatives (including why it is *not* ST-3 and
*not* Cycle 14 re-filed), and the instance where **this capture nearly fell to the cause itself**
— see A15-3.

No study gates anything (`factory/studies/README.md`, *Citable, never blocking*). Whether it binds
a build is ideation's ruling, not capture's.

## Capture — 15 filings (grounded against module source 2026-09-01, at v0.17.1 @ `c846520`)

Every `file:line` below was re-derived this run against working-tree source. Where a filing's own
`provenance_guess` was checked and **failed**, that is stated first and loudly — three did, and
two of the three would have shipped a repair to a site that does not exist.

Where a filing reported a count and the set was recoverable, it was recovered by dereferencing the
filing's named evidence in the live field vault, read-only (P-18 Tier A's second grounding axis).
That axis paid for itself immediately: it is what refuted A15-3.

---

### A15-1. The orphan slot carries no trustworthy signal at all (2026-08-27) — `factory/inbox/2026-08-27-160100-orphan-false-positive-two-consecutive-sweeps.md`

**GAP CONFIRMED — and the filing's own title is stale by one.**

**The mechanism, grounded.** `skills/vlt-setup/assets/workflows/vlt-lint-full.js:457` builds the
inbound map purely from what scanners returned — `for (const s of scans) for (const l of
s.outbound_links) inbound.set(l, …)` — and `:472` derives orphans as
`scans.filter((s) => !(inbound.get(nslug(s)) > 0))`. **A link the scanner does not return is a
link that does not exist**, so an under-returning scanner manufactures orphans directly. There is
no second source for inbound edges.

The workflow's authors saw a *neighbouring* version of this and guarded it. `:460-464` documents
the shortfall case at length — under `partialShortfall` (fewer scans than pages) orphans and
near-duplicates are emitted **empty** with a coverage cap, precisely because *"a page whose only
inbound link came from an unscanned page falsely reads as an orphan."* **The guard covers a page
that failed to scan and not a page that scanned badly**, which is this defect. The distinction is
invisible from inside the reduce: a scan that returned three of five links is `scans.length ===
pages.length` and trips nothing.

**Specimen manifest — recovered to three, from the filing's two.** The filing names two sweeps;
its own ⚠ addendum adds a third, and the third was re-verified this run against the live report.

| Sweep | False orphan | Inbound link that exists |
|---|---|---|
| 2026-08-26 | `fantasy-football-evaluation` | recorded in that sweep's `instrument_findings` |
| 2026-08-27 | `katsuo-dashi` | `chicken-soup`, plus the index |
| 2026-09-01 (1519) | `fantasy-platform-read-access` | `fantasy-football-evaluation.md`, plus the index |

Triggering fragment, `_agent/lint-reports/2026-09-01-1519-lint.yaml:225` — verified verbatim this
run:

> `"orphans: 1 of 1 refused - fantasy-platform-read-access carries a real inbound [[fantasy-platform-read-access]] from fantasy-football-evaluation.md. Third consecutive sweep refusing it"`

**Three consecutive sweeps, 1 of 1 each, across two module versions (0.16.2 and 0.17.1) and both
a cold and two warm sweeps.** Read the filing's title as stale, per its own instruction. **100% of
every orphan this instrument has ever reported has been wrong** — the slot carries no signal, and
`orphans: []` at `:7` of the same report is the *post-refusal* value, so the honest reading is that
the slot has never once been correct **and** has never once been non-empty before a human emptied
it.

**Relationship.** The filing correctly identifies itself as a **recurrence datum**, not a new
class: `2026-08-26-164501` filed the diagnosis and was captured as **A14-2 in Cycle 14 and
deliberately not built**. That filing remains live in the inbox with its clause undischarged.
**This entry does not re-open A14-2's diagnosis** — it supplies the rate, which is what Cycle 14's
capture could not have: a steady-rate defect at 100% relative frequency, not a one-off.

Under `ST-7` this is surface 2 — an agent's return consumed without read-back. ~~The comparison that
would catch it is mechanically available and cheap: the reduce holds every page's path, so a
returned link set can be checked against the page's own bytes.~~ **STRICKEN — the premise is wrong**
*(ideation Round 1, 2026-09-01; the same correction is applied to `ST-7`, which states it too).*
**The reduce holds the paths and cannot open them.** `vlt-lint-full.js` has **no filesystem access**,
stated three times in its own arg contract — `:37` (*"the SKILL has filesystem access, this script
has none — the `crossLayerSlugs`/`stubSlugs` division"*), `:64` (*"The SKILL computes the digests
(it has filesystem access, this script has none)"*) and `:476` (`crossLayer` targets *"supplied by
the SKILL which has filesystem access"*); `grep` over all 882 lines finds no `require`, no `import`
and no `fs.`. Holding a **path** is not holding the **bytes**. The comparison is available to the
**SKILL**, not to the reduce: it either moves SKILL-side, or the SKILL passes new inputs across that
boundary the way it already does for `crossLayerSlugs`, `stubSlugs` and `pageHashes`. **That is real
plumbing, and it is the largest cost difference among this cycle's nine `ST-7` instances** — a brief
scoping this from the struck sentence would have priced a cheap comparison and found a boundary
crossing. That said, it is still the same repair A15-4 needs, which remains the strongest argument in
the batch for treating them as one build rather than four.

**Residual scope.** Grounding does not shrink this one; it sharpens the site (`:457` and `:472`,
plus the shortfall guard at `:460-464` whose population must be widened, not duplicated) and
supplies a third specimen. The filing's own candidate direction — *"build it, or state that the
orphan slot is advisory until it is built"* — stands, and the 100% rate makes the second half a
real option rather than a hedge.

---

### A15-2. The stub list is derived by a regex the module does not ship (2026-08-31) — `factory/inbox/2026-08-31-104501-stub-discovery-regex-drops-the-stub-list-and-manufactures-missing-targets.md`

**PROVENANCE CORRECTION — and the correction makes the defect worse, not better.**

The filing says: *"The SKILL builds that argument by matching the index's stub heading with a regex
that requires a bare `## Stubs` heading."* It also says, with unusual and commendable honesty,
*"the regex site … has not been located in module source by this run … **Capture must ground the
exact `file:line` before this is briefed**."*

**Grounded: there is no regex.** `grep` for any stub-discovery pattern across `skills/` returns
nothing. The entire specification is one clause of prose at
`skills/vlt-lint/references/full-scale.md` step 1:

> *"Also parse `{index}`'s `## Stubs` section for its backtick-wrapped slugs and pass them as
> `stubSlugs` — a `[[link]]` to a registered stub is a recorded gap (the Stubs section is its
> record), not a missing target."*

The regex was the **field operator's own rendering** of that sentence. There is no shipped artifact
to widen.

**And the module contradicts itself about the heading, in its own two files.** `full-scale.md`
step 1 writes the bare `## Stubs`. `skills/vlt-lint/references/checks.md:39` — the index-drift
check — writes the long form verbatim: *"the `## Stubs (linked, not yet written)` section is
well-formed."* The live vault's index uses `checks.md`'s form. **An operator who rendered the
sentence at `full-scale.md` literally produced a matcher the module's own sibling file says will
miss**, and nothing anywhere reconciles the two.

**Specimen manifest.** Three registered stubs reported as missing targets in one sweep: `birria`,
`jesse-minter`, `nfl-draft-safety-archetypes` — full set, from the filing, and the filing quotes
its triggering fragment (the `false_positives_refused` entry) in full. **This filing conforms to
the manifest shape** and is worth naming as such: it observed a set of three and named three.

**Why the self-catch is not a mitigation** — the filing's own argument, which grounding confirms:
the refusal held because the run's operator read every entry against the index by hand. That is the
expensive path the false-positive discipline exists to make unnecessary, and an empty `stubSlugs`
is **silent** — the workflow (`vlt-lint-full.js:108`, `:478`) cannot distinguish *"this vault has
no stubs"* from *"discovery failed"*, so it does the correct thing with wrong input. The failure
mode is a `fix_now` class whose legal response is **to create pages that were deliberately not
created**. A mechanical fixer acting on this input writes the vault backwards.

**This is `ST-7`'s cleanest specimen** and it is cited there as such: the filer believed they were
reporting a too-narrow regex in module source; the truth is that there was nothing to be too
narrow, only a sentence and a reader.

**Residual scope — the filing's directions survive grounding, with one re-pointed.** Direction 1
(*widen the discovery match*) is **not** a code change: it is a prose repair at `full-scale.md`
step 1, and it should be reconciled against `checks.md:39` in the same act or the contradiction
simply moves. Direction 2 (*make an empty `stubSlugs` loud* — a denominated line rather than
silence) is untouched by the correction and is the half that generalizes; it is the module's own
denominated-zero posture, which Cycle 14 build-2 already ruled for `cache_rejected`. Direction 3
(both) is the filing's own preference and grounding supports it.

**Open design question, carried verbatim from the filing** — *"it does not make a future discovery
failure loud"* is stated as direction 1's known limitation; whether the denominated half ships with
it or separately is ideation's, not capture's.

---

### A15-3. Same-page anchors reach `fix_now` — but not for the reason filed (2026-09-01) — `factory/inbox/2026-09-01-140601-same-page-heading-anchors-are-reported-as-missing-targets.md`

**PROVENANCE CORRECTION, and the most consequential one in this capture. The fix the filing asks
for is already in the tree; shipping it would have been a graded no-op.**

**The filing's claim:** *"`vlt-lint-full.js`'s `normalizeTarget` strips the `#anchor` portion, is
left with an **empty string**, and reports that empty result rather than dropping it."* Its single
candidate direction: *"Drop an empty normalization result rather than reporting it."*

**Grounded — that is already what happens, and it is deliberate.**
`skills/vlt-setup/assets/workflows/vlt-lint-full.js:420-423`, verbatim:

```js
// Normalize once at intake (B5-3): scanners returned raw wikilink text; every graph
// comparison below runs on the normal form. Empty-after-normalization targets (e.g. a
// bare [[#anchor]]) are dropped, not compared.
for (const s of scans) s.outbound_links = (s.outbound_links || []).map(normalizeTarget).filter(Boolean)
```

The comment names **this exact case** — *"e.g. a bare `[[#anchor]]`"* — and `.filter(Boolean)`
drops it. `normalizeTarget` (`:94-99`) on `#Early Loading Phase (≈ Days 3–7)` splits on `#`,
takes index 0, and yields `''`, which is falsy. It never reaches `missing_targets` at `:480`. This
shipped as **B5-3**.

**So why did the finding fire, three sweeps running?** The second grounding axis answers it. The
filing cites its evidence; dereferencing it in the live vault
(`_agent/lint-reports/2026-09-01-1519-lint.yaml:226`) gives the **reported value**, which the
filing never quotes:

> `"calf-strain -> 'early loading phase (~ days 3-7)' is a SAME-PAGE HEADING ANCHOR"`

**`'early loading phase (~ days 3-7)'` is not the empty string.** Had the scanner returned the link
verbatim as `[[#Early Loading Phase (≈ Days 3–7)]]`, `normalizeTarget` would have produced `''` and
`:423` would have dropped it. The value that arrived has **no leading `#`** — so the scanner
mutated the link before returning it, exactly as it substituted `cornerboxes` in A15-4, and
`normalizeTarget` then correctly processed a string that was never an anchor.

**This is not a normalizer defect. It is A15-4, on a different page, with a different mutation.**

**Consequence for the plan, stated because it is the whole reason this correction matters.** Had
the filing's direction been briefed as written, the build would have added a drop that
`:423` already performs; the acceptance check would have been a fixture carrying a bare
`[[#anchor]]`; **that fixture would have passed, because the code already handles it**; and the
field would have kept firing on every sweep forever. That is `ST-5`'s failure mode — *an instrument
built from the fix's shape passes because it was built to* — reached by `ST-7`'s road, and it is
recorded in `ST-7` §What this session got wrong as an instance of the cause **arriving inside its
own capture**: this capture initially graded the filing CONFIRMED and was corrected only by
reading the evidence back.

**Residual scope.** The anchor half of this filing collapses into A15-4 (the scanner returns
non-verbatim; nothing checks the return against the page's bytes). What does **not** collapse is
the filing's own deferred question, and grounding raises its priority:

> **Open design question, carried verbatim:** *"Whether the anchor's *existence* should be
> validated (the heading is present here, but a stale anchor is a real defect class) is a
> **separate question capture should rule rather than fold in** — this filing asks only that an
> empty target stop being reported as a missing page."*

Capture declines to rule it, per the standing rule that a filing's open questions are ideation's.
But note what grounding changes: the filing offered this as a *possible extension*; since the
"empty target" half is already shipped, **the anchor-validation question is now the only unbuilt
thing in this filing that is about anchors at all.** If ideation declines it, this filing
contributes exactly one thing to the cycle — a second specimen for A15-4 — and should be said to
do so rather than briefed as its own scope.

**Cost that is real regardless:** three consecutive sweeps, and the filing is right that *"it will
re-fire on every sweep until the normalizer changes"* — with the correction, until the **scanner
return check** exists. And per the same filing's ⚠, the cache now serves it, so the entry is stable
and no longer re-derived.

---

### A15-4. A scanner substituted a proper noun, and the cache made it permanent (2026-09-01) — `factory/inbox/2026-09-01-140602-a-scanner-substituted-a-proper-noun-and-the-cache-made-it-permanent.md`

**CONFIRMED, both halves — and the filing's own ⚠ confidence caveat is discharged by this
grounding, as it asked.**

**Half 1 — the substitution.** `skills/vlt-setup/assets/workflows/vlt-lint-full.js:229-230` carries the
verbatim-extraction instruction the filing quotes. Verified this run against the live reports: the
page `seattle-seahawks` links
`[[_agent/research/2026-07-26-112444-espn-top-10-cornerbacks-2026]]`, which resolves; the scanner
returned `…-espn-top-10-cornerboxes-2026`. **`cornerboxes` for `cornerbacks`.** The instruction is
explicit and was not followed.

The filing's own framing deserves to survive into the brief: **this is the failure class the
entity-collision check exists to catch in sources, occurring in the instrument that feeds it.** A
check that hunts substituted proper nouns across pages is fed by a reader that substitutes proper
nouns.

**Half 2 — the amplification, which the filing marked ⚠ inferred. Now confirmed, twice.** The
filing inferred cache-service from `seattle-seahawks` being absent from the five re-scanned pages
on 2026-09-01 14:06. Its own addendum adds the 15:19 sweep, and this run verified that sweep's
`cost_accounting` directly (`_agent/lint-reports/2026-09-01-1519-lint.yaml:232`):

> `{"phase": "Scan pages", "agents_dispatched": 1, "model": "haiku", "prompt_chars": 4072}`

**One agent dispatched, against `pages_total: 146`.** `churn_since_last_full` at `:240` names the
single changed page — `fading-food-and-cue-reliability` — and `seattle-seahawks` is not it. The
`cornerboxes` entry nonetheless re-fired unchanged at `:226`. **The record was served from the
sidecar. The ⚠ caveat is discharged: the substitution is now permanent for the life of the cache.**

**This is the cycle's new fact and it inverts a Cycle 14 success.** The findings cache shipped
broken for three cycles (Cycle 12 `b2(5)`), was repaired in Cycle 14 build-2, and now works —
145/146 reuse. **Because it works, a scanner error is durable**: it survives every subsequent
sweep, and re-running the lint — the ordinary response to a suspect finding — *cannot re-derive
it*, because reuse is the cache behaving correctly. The provenance is gone too: no model call
anyone can inspect. The filing states this precisely and grounding adds nothing but confirmation —
**the cache is not defective here; it faithfully preserves what it was given, which is exactly why
the input's fidelity now matters more than it did.** `ST-7` cause 4 (*amplifying*) is this
paragraph generalized.

**The unification.** A15-1 (under-returned links), A15-3 (a dropped `#`) and this entry (a
substituted noun) are **three mutations of the same unaudited return**, reaching two different
`fix_now` slots. The filing's direction 1 addresses all three:

> *"A slug the scanner returned that is absent from the page's own bytes is mechanically
> detectable"* — ~~and the reduce already holds each page's live absolute path (`vlt-lint-full.js`
> arg `pages: [{slug, path}]`)~~ **and the SKILL can perform that comparison; the reduce cannot.**
*(Corrected ideation Round 5, 2026-09-01 — third and final instance of the premise struck in A15-1
and `ST-7` at Round 1. The reduce receives `pages: [{slug, path}]` and has **no filesystem access**:
`vlt-lint-full.js:37`, `:64`, `:476`, and no `require`/`import`/`fs.` in 882 lines. Holding a path
is not holding the bytes — the read-back moves SKILL-side or the SKILL passes new inputs across
that boundary. See* Ideation rulings *§Round 1 grounding correction.)*

**Direction 3 is named by the filing to be refused, and grounding agrees on the filing's own
reasoning:** moving the scan phase off haiku is not the fix. One substitution across sweeps does
not carry the cost case (146 agents cold), and *"direction 1 makes the substitution harmless
regardless of which model made it, which is the more robust fix and the one that survives a future
model change."* Recorded as a **rejected alternative already resolved by the filing** — ideation
should not re-litigate it without new evidence.

**Direction 2** (*give a cached record a provenance and an invalidation path*) is untouched by
grounding and is the only direction that addresses the **durability** half rather than the
**fidelity** half. Both halves are real; they are separable, and direction 1 does not cure records
already poisoned.

---

### A15-5. The summary-length check measures the wrong string (2026-08-27) — `factory/inbox/2026-08-27-160000-summary-length-check-counts-the-raw-yaml-line.md`

**GAP CONFIRMED — and the convention is on the filing's side, explicitly.**

**Grounded.** `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:125`:

> **"Length limit: 160 characters** (counting characters, not bytes — em-dashes count as one). …
> **Double-quote it** (it almost always contains a colon, em-dash, or comma — see YAML rule 2).
> `vlt-lint` flags a wiki page whose `summary:` is **missing** or **exceeds 160 characters**."

The convention states the measure as a property of the **summary** and, four clauses later,
**mandates the quoting** that the field measurement is counting. The rule and the instrument
disagree, and the rule is unambiguous.

**Where the check lives — and it is `ST-7` surface 2, not a code bug.**
`skills/vlt-lint/references/checks.md:15` defines `malformed_frontmatter` as *"the fan-out's
per-page validity verdict"*, returned by the **scanner** as a structured verdict. ~~There is no length arithmetic in `vlt-lint-full.js`; the number `171` was produced by an agent measuring a string.~~ **STRICKEN at the roundtable (A11, six lanes): `vlt-lint-full.js:640` `summaryIssue` measures `s.summary.length` from the scanner's verbatim return into `frontmatter_drift` — and got both specimens right (the 2026-08-27 report carries 0 `over-length` entries). The `171`/`161` arrived through the scanner's separate `malformed_frontmatter` verdict. Two measurers, one wrong, no comparison — the cycle's thesis inside one report. Mechanism ruled at build-4 (D-A).** So this is the same shape as A15-3 and A15-4 — an executor's rendering of a prose
specification, consumed unchecked — with the twist that here the executor was measuring rather
than extracting.

**Specimen manifest — full set, both directions.** Population: 10 `malformed_frontmatter` findings,
one sweep. **8 genuine, 2 refuted (20% false positive).**

| Page | Reported | Verdict |
|---|---|---|
| `barbacoa` | `summary exceeds 160 characters (171)` | **REFUTED** — parsed value under the limit |
| `l-theanine` | `summary exceeds 160 characters (161)` | **REFUTED** — same artefact |

**The filing preserved the other direction too, and it is load-bearing:** 3 of the 8 genuine
findings (`career-history-as-evidence`, `nfl-2026-position-rankings`, `technical-hiring-pipeline`)
**parse cleanly under PyYAML and were still correctly flagged** — the scanner caught a semantic
mis-key a parser cannot see. **The instrument is not weak, and a repair must not replace the
scanner with a parser.** That is the single most important constraint this filing carries into a
brief, and it is the filing's own observation, not grounding's.

**Why it matters.** `malformed_frontmatter` routes to `fix_now`, so a refuted finding invites an
auto-fix that rewrites a `summary:` which was never too long. And the bias is **systematic, not
random**: `161` against a `160` limit means quoting overhead alone can carry a compliant value
over, so the error is directional — it flags values sitting just under the cap, which is where
well-written summaries cluster.

**Residual scope.** Direction 1 (*measure the parsed scalar*) is the fix and grounding confirms the
convention already requires it — this is not a rule change, it is an instrument correction.
Direction 2 (*if the raw line is deliberate, say so and rename the check*) is **eliminated by
grounding**: `frontmatter.md:125` states the measure and mandates the quoting, so a byte-budget
reading is not available. Say so rather than carrying it to ideation as a live option.

---

### A15-6. The `governance_memory` denominator missed a fifth of its population, silently (2026-08-27) — `factory/inbox/2026-08-27-160200-governance-memory-denominator-missed-twelve-entries.md`

**GAP CONFIRMED — and again the convention already mandates counting what was missed.**

**Grounded, and the provenance is `ST-7` surface 1.**
`skills/vlt-lint/references/report.md:91`:

> *"**You compose both lines yourself** in both modes — the decision log is a vault-zone read the
> fan-out workflow never performs (it sweeps `{wiki}` only), so these are this SKILL's own facts."*

**No counter ships.** The pattern that matched only bracketed headings was the operator's, exactly
as in A15-2. There is no code to repair.

**And the missed population is a class the convention names.**
`skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md:38` gives the entry schema as
`## [YYYY-MM-DD] <kind> — <one-line subject>`; `:78` is a section titled **The classifiability
tail**, for pre-schema entries. `skills/vlt-lint/references/checks.md:43` then mandates their
treatment:

> **"`unclassifiable`** — the log carries entries that cannot be keyed (`kind:` but no `ref:`, or
> pre-schema — the convention's two-tier tail); counted in the report's `governance_memory:`
> denominator line (Step 5), **never silently swept.**"

So the 12 oldest entries are precisely the pre-schema tail the module **already requires be
counted**. The operator's matcher implemented the schema and dropped the tail the schema's own
convention says to carry. **This sharpens the filing's direction 1 considerably**: it is not "match
both heading forms" as a new rule — it is *the denominator must include the classifiability tail,
as `checks.md:43` already says*, and the shipped prose is on the filing's side.

**Specimen manifest — a count, and the set is recoverable but was not preserved.**

| Quantity | Reported by prior sweeps | True |
|---|---|---|
| Decision-log entries | 47 | **59** |
| Undercount | — | **12 (20.3%)** |
| Unclassifiable | — | 24 |

**Attrition note (`ST-5`).** The filing names the 12 as *the oldest* but does not enumerate them,
and the report persisted the corrected count rather than the slugs. The set is **recoverable in
principle** — it is every unbracketed `## YYYY-MM-DD —` heading in the live vault's
`_agent/mint/decision-log.md` — but it is a *vault* artifact, not a module one, so it must be
materialized into this cycle's `fixtures/` by the build that needs it rather than assumed. **12
observed, 0 preserved.** A brief constructing a fixture from the shape of a bracketed-vs-unbracketed
heading will produce exactly the fixture that passes; the real tail is a live file and should be
frozen from it.

**Why this one is worse than a false positive, in the filing's words and confirmed by grounding:**
*"nothing about the output looked wrong — 47 is a plausible number and no finding was raised. It
was caught only because a sweep re-derived the population rather than trusting the counter."* A
denominator silently rescales every ratio built on it, and every prior sweep's governance-memory
metric was computed over a window **biased toward recent decisions**.

**Residual scope.** Direction 2 is the one that generalizes and the filing already argues it
correctly: *"have the counter report **what it matched against what exists** … the same shape Cycle
14 build-2 ruled against for `cache_rejected` (rendered with its denominator, precisely so a
discard is never silent)."* That is `ST-7`'s cheapest general move (denominate every derived slot)
arriving from the field independently — worth noting at ideation, because a direction two filings
reach separately is a stronger signal than one a capture proposes.

---

### A15-7. One archived report in six does not parse (2026-08-27) — `factory/inbox/2026-08-27-153000-persisted-lint-report-is-not-machine-readable.md`

**CONFIRMED. This filing is the graded FAIL of Cycle 14 build-4's check (1) — it is inherited
material, not fresh signal, and it arrives with its bound already set.**

**Grounded.** `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:330` — *"A
**structured report-emitting** verb persists its report content-verbatim as a dated plain file
under its report dir, in the format that verb declares"*. `skills/vlt-lint/SKILL.md:74` performs
it: *"write the Step-5 report block to `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` … **content-verbatim**
… unabridged, unreordered and unreworded."* `skills/vlt-lint/references/report.md` states the
block's shape and it is **agent-authored** — Cycle 14 build-4 ruled **deliberately no serializer**,
on the reasoning that *the enforcement point for a report is a reader, not a writer*.

**Between the mandate and the render there is nothing.** Confirmed: no grep hit anywhere in
`skills/` validates a persisted report.

**Specimen manifest — complete, 6 of 6 named, with the triggering fragment.** Re-verified this run
against the live archive:

| Report | Result |
|---|---|
| `2026-08-23-1504-lint.yaml` | OK |
| `2026-08-23-1739-lint.yaml` | OK |
| **`2026-08-24-1700-lint.yaml`** | **FAIL** |
| `2026-08-25-1600-lint.yaml` | OK |
| `2026-08-26-1046-lint.yaml` | OK |
| `2026-08-27-1104-lint.yaml` | OK |

**1 of 6 (16.7%).** The fragment, at line 102 of the failing report:

```yaml
  research_zone: 145 notes scanned; 24 carry revisit_after:
```

A bare unquoted scalar containing `: `. YAML reads the second colon as a nested mapping key:
`mapping values are not allowed here, line 102, column 59`. Quoting parses clean.

**The filing conforms to the manifest shape exactly** — full population, per-member verdict,
minimal triggering fragment — and is worth citing as a second positive specimen alongside
`2026-08-26-075130`.

**Bound and disposition, carried forward verbatim from the filing.** Owner-ruled 2026-08-27: *do
not re-scope a check to make it pass.* The check's honest subject going forward is reports written
**under** the mandate; a report predating the rule cannot be evidence about it. **That re-grade
belongs to `acceptance-discharge` against post-release-2 reports, not to a narrowing written after
the fact.** The archived report was **not repaired** — the vault's archive is the owner's record,
append-only, and editing field evidence to satisfy a test is the failure mode Cycle 14 exists to
close.

**Relationship — this and A15-8 are cousins and `104500` says so.** `153000` says *a persisted
report must load*; A15-8 says *a report that loads must also carry its mandated slots in their
mandated form*. **A parse is already required, and a parse is the natural place a key-presence and
slot-type check could live** — which is the strongest argument in the batch for briefing them
together rather than as two repairs at the same site.

**Residual scope.** Direction 1 (*a pre-persist parse gate in Step 6 — the reader exists, run it
before the write*) is unchanged. Direction 2 (*constrain the emitting slots*) is a narrower cure and
grounding notes the filing's own caveat: the `.json` render already sidesteps it, *"which is why
the `.json` limb passed"* — but **nothing makes an author choose it**, so it is a cure available to
the author, not an enforcement point. Direction 3 (*declare the archive best-effort and stop
claiming it is machine-read*) is the honest fallback and should stay on the table; the filing lists
it and grounding does not eliminate it.

---

### A15-8. The report's shape is stated in one file and enforced in none (2026-08-31) — `factory/inbox/2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md`

**CONFIRMED, and the filing's ⚠ follow-up makes the claim *stronger*. Read the follow-up as the
claim; the title understates it.**

**Grounded, slot by slot.**

- `skills/vlt-lint/references/report.md:32` — `para_missing_attestation: [<para-file: vault type +
  author agent|hybrid, no attestation — …>, ...]`, **one entry per file**.
- `skills/vlt-lint/references/report.md:72` — `fixes_applied: [<summary>, ...]`.
- `skills/vlt-lint/references/report.md:73` — `backlog_filed: [<merge item>, ...]`.
- `skills/vlt-setup/assets/workflows/vlt-lint-full.js:812-814` — the workflow returns
  `para_missing_attestation: []` and comments that it is *"a structural slot the SKILL fills"*.
  **The workflow does not and cannot render it; the SKILL does, unchecked.**
- **No grep hit anywhere in `skills/` validates a rendered report against `report.md`'s slots.**
  Confirmed independently this run.

**Specimen manifest — three instances, one sweep, and the follow-up splits them.**

**(a) `para_missing_attestation` rendered as a rollup where `:32` mandates a per-file list.** The
2026-08-30 render carries a **single string** standing in for 27 files. The disposition is
legitimate and the count is correct; what is lost is the **population** — no reader, human or
check, can learn which 27 files, what `type:` each carries, or which are pre-adoption and therefore
informational. **RECURRED on the 2026-09-01 sweep in identical form — third consecutive sweep.**
This is standing behaviour.

**(b) `fixes_applied:` omitted entirely from a report that applied fixes.** Five fixes *were*
applied; they were recorded inline inside `fix_now.sources_vs_prose_mismatches` instead. The
2026-08-27 render carries the key correctly at `:221-224`. **DID NOT RECUR** — 2026-09-01 carries
it, well-formed.

**(c) `backlog_filed:` omitted, and the finding it should have carried filed nowhere.** **DID NOT
RECUR** — 2026-09-01 carries a denominated *"NONE - every filable finding this run already carries
an open item"*, which is the honest rendering rather than an omission. Verified this run at
`_agent/lint-reports/2026-09-01-1519-lint.yaml:220`.

**Why the non-recurrence strengthens rather than weakens the filing — grounding endorses the
filing's own re-framing.** Two renders of the same skill over comparable runs produced **different
report shapes with no code change between them**. An unchecked hand-render is not *consistently*
wrong; it is **intermittently** wrong, which is the harder failure for a consumer to defend
against — a slot cannot be relied on to be present, and a reader has no way to tell an absent key
from a legitimately empty one without a denominated line. **Intermittence is the signature of no
enforcement point**; a consistent deviation would at least be a de-facto contract. `ST-7` names
this as its instance (f).

**What it cost, concretely — this is inherited gating damage, not a hypothetical.** Cycle 14
build-3's check (7) reads *"the sweep reports the `type:` distribution of every
`para_missing_attestation` entry."* Its bound event occurred; the sweep rendered instance (a); no
shipped surface produces a `type:` distribution and the render did not even produce the per-file
list `:32` mandates. It was graded **BLOCKED (unreachable)**, and it is `[ship-verifiable]` and
**GATES** — so Cycle 14 gained a gating blocker from a report-shape defect. Cycle 14 build-4's
check (6) was graded DISCHARGED on substance but with instance (b) as a caveat, *because the
check's named location was not there to look in*.

**Why this is not three filings — the filing's argument, which grounding sustains.** All three are
one absence: **the report shape is stated in one file and enforced in none.** A per-slot repair
would be another rule stated at the same altitude as the rules that just failed.

**Residual scope.** Direction 1 (*validate at persist — parse it back and assert the mandated
top-level keys are present and of their mandated type; fail loudly*) is unchanged and **composes
with A15-7's parse requirement rather than duplicating it**. Direction 2 (*move the population
slots off the hand-render*) is real and narrower. Direction 3 (*rule the rollup legal and fix the
checks instead*) now **demonstrably cannot explain (b) and (c)** — they were not a policy, they
were a miss — and the filing says so; grounding confirms it with the non-recurrence evidence.

---

### A15-9. The findings cache cannot survive the release that makes it needed (2026-09-01) — `factory/inbox/2026-09-01-093000-the-findings-cache-cannot-survive-the-release-that-makes-it-needed.md`

**CONFIRMED — the load-bearing quotes are verbatim in current source. One status correction: the
platform-side amendment this filing demands has already landed.**

**Grounded.** `skills/vlt-lint/references/full-scale.md` step 2, verbatim:

> *"compute this run's **ruleset components** … four named slots: `module_version` (the installed
> one); `pin_vector` …; `convention_digests`, a `{name: digest}` map with one entry per convention
> this run judges against; and `checks_digest` … **Any of those moving invalidates every record.**"*

and, as the filing quotes, the document states the consequence itself as settled fact:

> *"State it plainly: **the first full run after any release is a COLD one** — stated up front,
> never discovered."*

**The first slot is `module_version`. Every release moves it.** So every release invalidates every
record, whatever the release contained — and **the only sweep an acceptance check ever forces is a
post-release sweep.** The instrument built to make sweeps affordable is invalidated, by
construction, at precisely the moment a sweep becomes mandatory. The filing's central claim is
exact.

**Measured cost, re-verified against the live report's own `cost_accounting`:** 146 scan agents,
591,152 prompt chars, `files_checked: 146`, `files_cached: 0`, 172 total dispatches. And
`prompt_chars` is the **floor**: the report's own note says it is *"workflow-composed prompt text
only — agent-side file reads (page + convention bytes) are not visible from JS"*, and each of the
146 scanners also reads its page and three conventions.

**The over-broadness argument, which grounding sustains as gradeable.** `module_version` is a
**proxy** for *"something that changes what a finding means may have moved."* The other three slots
answer that directly and with precision, and the workflow-side `scanFingerprint`
(`vlt-lint-full.js:232-233`) independently catches the page-scan prompt and `PAGE_SCAN` schema
moving. What `module_version` **uniquely** catches is a change to the lint surface's own logic that
moves no pin and no digest — `vlt-lint/SKILL.md`, `references/full-scale.md`, the reduce in
`vlt-lint-full.js`. **That is a real gap and the filing says so; the slot is not pointless.** It is
answerable by digesting those files, which is what every other slot already does.

**The second, deeper over-broadening.** The cache stores **page-scan facts**, but its key is
`convention_digests` — *"one entry per convention **this run** judges against"* — so a change to a
convention the page scanner never reads invalidates every page-scan record. The filing's worked
instance is exact and verified: `pageScanPrompt` reads exactly `frontmatter`,
`wiki-supersession`, and `write-verification` (`vlt-lint-full.js:229-230`); a build bumping only
`extraction` cannot change a cached page-scan record, yet would invalidate all 146 — twice over.

**⚠ Status correction — the platform half is done.** The filing opens by refuting a premise on
record in **[P-19]**'s Out of scope (*"Cycle 14 build-2's cache repair is the answer to that"*) and
says *"P-19 is being amended in the same act."* **That amendment has landed**:
`factory/platform/roadmap.md:1381` now reads *"(amended 2026-09-01: sampling policy added; the
sweep-cost out-of-scope premise refuted)"* and the clause is struck through in the entry. Ideation
should treat the refutation as **settled and applied**, not pending. The module half is what
remains, and is this entry.

**Residual scope.** Direction 1 (*key the cache to the cached artifact's own dependencies*) is the
largest-effect direction and the filing correctly names its precondition: it *"needs the 'what does
a cached record actually depend on' question answered explicitly, which no site answers today."*
That is a design ruling, not a code change, and it is ideation's. Direction 2 (*replace
`module_version` with digests of the lint surface it proxies for*) is smaller, independently
shippable, and **correct even if (1) is declined** — the filing says so and grounding agrees.
Direction 3 (*make the release-time sweep unnecessary by binding checks to the population they
judge*) is **free, already being applied**, and belongs to `build-brief`'s check anatomy — see the
companion finding below.

**⚠ Not a direction, carried forward verbatim because it is a constraint on every repair:**

> *"**Not a direction: weakening invalidation on judgment.** A record reused under a moved rule is
> a false clean, which is worse than an expensive sweep. Any repair must show the reused facts are
> **independent** of what moved, not merely unlikely to be affected."*

**Companion finding — factory-side, recorded not routed.** The filing records that three of Cycle
14's acceptance checks were bound to a full sweep whose population they do not judge (`checks.md:19`
places the `para_*` nets in **both** modes; the fan-out sweeps `{wiki}` only and the `para_*` slots
are SKILL-filled at `vlt-lint-full.js:812-814`), so a **scoped** run was what each needed. Build-6's
two were corrected at brief time 2026-09-01; the other two are historical and annotated, not
re-graded. The filing itself calls this *"a brief-time discipline gap, not a module defect"*
belonging to `build-brief`'s check anatomy. ~~**It is recorded here and not routed**~~ — the filing
deliberately kept both halves of the cost problem in one place (*how often* a cold sweep is forced,
factory-side and free; *what one costs* when it is, module-side), and splitting it would lose that.
~~Ideation may route the factory half to the platform ledger; capture does not pre-empt it.~~

**➜ ROUTED — ideation Round 4 ruling Q4 (2026-09-01); opened as [P-23] on 2026-09-02:**
`factory/platform/roadmap.md` §*P-23 — a check names the population it judges, not the run that will
produce it*. **The capture's reason for not routing was overruled deliberately, and its cost is
mitigated rather than dismissed — this pointer and P-23's back-pointer ARE the mitigation**, so both
halves of the cost problem stay findable together after the split. **The module-side half is this
entry and ships as Cycle 15 build-2**; the factory-side half is P-23 and is explicitly out of
build-2's scope.

---

### A15-10. The fingerprint's inputs are under-specified, and a wrong reading is silent (2026-09-01) — `factory/inbox/2026-09-01-140600-ruleset-fingerprint-inputs-are-under-specified-and-a-wrong-reading-is-silent.md`

**CONFIRMED — verbatim, and this is `ST-7`'s sharpest economic specimen: 96% of the scan phase
gated behind a sentence's ambiguity.**

**Grounded.** `skills/vlt-lint/references/full-scale.md` step 2, re-read in full this run. For the
two **digest** slots the document is exact and *says why the precision is there*:

> *"**Each digest is computed by these exact steps** (an executor that follows them lands on the
> same value every run, **which is the property that failed**): **instrument** `shasum -a 256` …
> **merge order** the base file's bytes, then a newline, then the overlay … **encoding** UTF-8 …
> **truncation** the first 16 hex characters, lowercase."*

For the two **component** slots, in the same paragraph, it says only:

> *"`pin_vector` (this skill's own `depends_on:` pins, **verbatim**)"* and
> *"`convention_digests`, a `{name: digest}` map with **one entry per convention this run judges
> against**"*.

**Both were read wrongly in the field on the first attempt, and neither wrong reading degraded —
it composed a fingerprint that matched nothing.**

- **`pin_vector`** — the operator passed the pins as a JSON array, a fair reading of *verbatim* for
  a list-valued frontmatter key. `vlt-lint-full.js` requires `typeof v === 'string'`, so the slot
  **read as missing**, the fingerprint composed as `''`, and **all 146 pages became uncacheable**.
- **`convention_digests`** — the operator read *"judges against"* as the 8 conventions named in the
  pin vector. The workflow expects all 9 files in `{conventions}`: `wiki-consolidation` is judged
  (convention coherence, enforcement doctrine) **without being pinned**, so *"judges against"* and
  *"pins"* are not the same set and the phrase does not say which it means.

**Corrected, the recomposed fingerprint reproduced the sidecar's recorded key half
`bd6e1e211804a2011af` exactly and 141/146 pages reused.** The mechanism is sound; only its
specification is not.

**Why this is the expensive one — the filing's argument, and grounding confirms the mechanism.**
The failure is **silent by construction**: a cold run caused by a mis-rendered slot is
*indistinguishable* from a correct first-run-after-release — same `files_cached: 0`, same honest
cold-branch reason. The one surface that could disambiguate does not: `full-scale.md` says *"any
slot missing or empty is a cold sweep with the absent slots named in `coverage_caps`"*, which names
**which slot was absent** but never **that the operator's rendering was wrong** — because from the
workflow's side those are the same event. This is `ST-7` cause 3 stated by the field before the
study existed.

**⚠ And it plausibly explains a three-cycle mystery.** The findings cache shipped in v0.17.0 (Cycle
14 build-2, repairing Cycle 12's `b2(5)`, which shipped broken and undetected for three cycles). Its
acceptance check (8) went unfired through three discharge runs. The first sweep to attempt reuse
(2026-08-30) was cold — correctly, no sidecar existed. **The second attempt was cold for this
reason**, and only a hand-debugged re-render made it warm. **A vault following the doc as written
gets a permanently cold cache and a report that says nothing is wrong.** Capture does not upgrade
this to a certainty — the filing says *plausibly* and the earlier cycles' failures have their own
recorded causes — but it is the first mechanism offered that would produce exactly the observed
history.

**Measured, from the two reports' own `cost_accounting`:**

| | 2026-08-30 (cold) | 2026-09-01 (warm) |
|---|---|---|
| Scan-page agents | **146** | **5** |
| Scan-page prompt chars | **591,152** | **20,294** |
| total dispatches | 172 | 31 |

**A 96% reduction on the scan phase.**

**Relationship to A15-9 — sibling, not duplicate, and the filing insists on this.** A15-9 says the
fingerprint is **over-broad** (a release guarantees a cold sweep); this says it is
**under-specified** (a correct-looking run goes cold with no release involved). *"Capture may brief
them together; they are not the same defect."* Grounding sustains the distinction: A15-9's repair
changes **which slots** compose the key; this one changes **how two slots are rendered** and would
be needed even if A15-9 shipped whole.

**Residual scope — the field already identified the fix and grounding adds nothing to it.** State
the two component slots' exact rendering the way the digest steps already are: `pin_vector` — name
the rendering (the JSON-array serialization, or whatever the workflow in fact requires) rather than
*"verbatim"*; ~~`convention_digests` — *"one entry per file in `{conventions}`"*, not *"per convention this run judges against."*~~ **SUPERSEDED at the roundtable (A4): the population is Q3 d1's three scanner-read conventions, landed by build-2 as a workflow-side required-name set; build-3 owns only the rendering/type language. A build-3 brief scoped from this sentence would have re-widened what build-2 narrowed.**

**⚠ Second-order direction, carried forward and worth ideation's attention** — because it is the
only one in this cluster that generalizes past these two slots:

> *"make a wrong rendering **loud** rather than merely making the right one documented. A slot that
> is present but of the wrong *type* is a different event from a slot that is absent, and the
> workflow can tell them apart (`typeof v === 'string'` already distinguishes them — it simply
> discards the distinction)."*

That is a read-back at the consumer, which is `ST-7`'s named shape, available here for the cost of
not throwing information away.

---

### A15-11. The inline args payload costs the caller ~84KB before the first agent dispatches (2026-08-26) — `factory/inbox/2026-08-26-123151-lint-full-inline-args-payload-costs-the-caller-84kb.md`

**CONFIRMED. ⚠ This filing carries a standing deferral from Cycle 14 that this capture does NOT
overturn — it re-admits it to the roadmap so ideation can rule with the joint in view.**

**Its Cycle 14 history, on the record.** Roundtable A27 (2026-08-26) deferred it explicitly:
*"Net-new capability; it stays in `factory/inbox/` un-captured and is **not** in this cycle's
`derives_from:`."* Cycle 14's own capture then recorded, at length, why the deferral is **not
clean** (`factory/cycles/14-no-enforcement-point/roadmap.md:117-127`):

> *"**Any resolution that gives the reduce ground truth needs a payload route, and #13 is that
> route.** If ideation takes the posture, #13 stops being net-new and becomes a dependency; the
> owner would then re-admit it by ruling."*

**Capture's judgment call, stated plainly:** the owner ruled this run's scope as all 16 un-captured
filings, so it is captured. **Capture does not re-admit it as a build** — that was and remains the
owner's ruling — but it does record that **the condition Cycle 14 named has now arrived.** A15-1,
A15-3 and A15-4 all converge on *check the scanner's return against the page's bytes*, which is the
reduce needing ground truth. Cycle 14 predicted exactly this and said what it would mean.

**Grounded, verbatim.** `skills/vlt-lint/references/full-scale.md` step 3 requires re-passing the
full args object on resume:

> *"**On resume** (`resumeFromRunId`), re-pass the full args object — the runtime delivers args
> fresh per run, so omitting them nulls `pages`/`crossLayerSlugs`/…"*

so the caller pays the payload again on every resume. Step 1 is the derivation spec for all three
scaling axes (`pages`, `pageHashes`, `crossLayerSlugs`).

**Specimen manifest — the filing preserved its measurement in full.**

```
pages            146 entries  ({slug, path}, absolute paths)
pageHashes       146 entries  (sha256 each)
crossLayerSlugs  1849 entries
stubSlugs        6 entries
total            ~84KB serialized JSON
```

**The cost scales on three axes at once**, so it worsens exactly where the fan-out is most needed.

**⚠ Correction to the filing's second observation.** The filing reports that invoking the workflow
by name with no args fails with a *"correct and well-worded refusal"* that *"reads as a broken
asset"*, and asks for *"a pointer to the SKILL route in that message."* Grounded at
`vlt-lint-full.js:127` — the message already **is** that pointer:

> `'vlt-lint-full requires { pages:[{slug,path}], indexPath, conventionsPath }. The vlt-lint SKILL discovers pages and passes live paths.'`

The second sentence names the SKILL and what it does. Residual scope on this half is at most a
wording nudge, not a missing pointer — say so rather than briefing it as a gap.

**Residual scope on the main claim.** Direction 1 (*document the wrapper-script route in
`full-scale.md` step 3 as the recommended invocation at scale*) is **available immediately, costs a
documentation edit, and the filing supplies the working recipe** — it invokes by `scriptPath` with
the payload embedded, so the payload never enters the caller's context and resume does not re-send
it. The filing is careful and correct that this *"works today with no module change — it is
undocumented, not unavailable."* Direction 2 (*an `argsPath` parameter*) *"needs runtime support and
may be out of the module's control"* — that is an **external unknown** by the filing's own framing.
No spike stub is opened for it here, because direction 1 does not depend on the answer and the
filing does not rest its ask on it; if ideation takes direction 2, the spike is due **before** the
brief.

⚠ **A `ST-7` note that ideation should see:** direction 1 documents a route for an *executor* to
render, which is this cycle's own failure shape. A wrapper-script recipe stated in prose is one
more derivation nobody reads back. Not an objection — it is the cheap fix and it works — but the
denominated-slot posture (A15-2, A15-6, A15-10) applies here too.

---

### A15-12. `class: supersession` — retire the PARA `type:` prohibition (2026-09-01) — `factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md`

**CONFIRMED — both halves, separately verified. Graded as a *supersession*, not SUPERSEDED: the
redundancy is real.** *(Tracker **#17**; `class: supersession`, the loop's first, alongside A15-13.)*

**Half 1 — the rule now redundant. Site verified.**
`skills/vlt-setup/assets/governance/_meta/conventions/extraction.md:84` (`version: 9` at `:11`),
restated at `skills/vlt-lint/references/checks.md:19` as legal-response case (b). The line is long;
its operative clauses, verbatim from source:

> *"A file in the `para_*` population … carries a `type:` from the **closed** set: the artifact
> types `project | area | resource | moc` …, the **operational-record class** `charter | record |
> register` …, and any vault-declared schema in `{overlays}/extraction.overlay.md` (the
> declare-at-birth rule). **Closed for this population** … A module-canonical but **non-PARA**
> `type:` …"*

**The rule still exists and still binds.** Confirmed.

**Half 2 — the mechanism, and its population.** `skills/vlt-lint/references/checks.md:19` ships
`para_type_unknown` (and its siblings) over *"files under `{projects}`, `{areas}`, and
`{resources}`"* in **both modes**, with `{wiki}` excluded by name at selection time. **The
population is exact: the nets judge the identical file set the enum governs.** No population is
left uncovered by the retirement. Confirmed as the filing states.

**And the filing's second mechanism holds too, which is the subtler half.** `extraction.md:84`
**already admits** *"any vault-declared schema in `{overlays}/extraction.overlay.md`"* into the
closed set. The declare-at-birth route exists, ships, and is relied upon. **The prohibition does not
doubt the mechanism — it carves one class of value out of a route it otherwise accepts.**

**The inversion, verified.** The overlay route stays open for *vault-grown* vocabulary and is closed
**only** to the module's own words. A vault typing agent-written periodicals `dispatch-brief` is
conformant; the field vault, which typed them `research` — the module's own accurate word for a
dated, single-pass, `trust: raw` snapshot (`extraction.md:28-30`) — is permanently not. **A
recognized-vocabulary rule that punishes correct vocabulary has stopped serving its stated
purpose.**

**Field evidence, re-verified this run.** 146 files under the wiki carry `type: wiki`, legal solely
by the by-name removal. **9** files under `resources/briefs/` carry `type: research` — a standing
`para_type_unknown` finding, ⚠ **up from 5 → 8 → 9 in three days**. The park's scope is the `type:`,
not the count, so the number moves no ruling — **but Cycle 14's closeout recorded this as a standing
metric to re-read at this capture, and it is still climbing.** Both stated legal responses require
writing something false.

**Study.** The filing cites **`ST-2`** (location as proxy for trust, `status: standing`) and is its
RC1 remainder. Grounding confirms the fit: `ST-2` RC1 names the redundancy since the `para_*` nets
were extended across the whole PARA population, and this is that argument applied to the **third
field of the quartet** — `author:`, `trust:` and `verified_by:` are believed when honest; `type:` is
believed only if the folder approves the noun. This capture is appended to `ST-2`'s `cited_by:`.

**⚠ The reinforcement fact, and it is the reason the retirement is urgent rather than tidy.** Cycle
14 build-3 (`e42429d`, v0.17.0) **did not inherit this rule — it restated and strengthened it**.
`extraction.md:84`'s closed-set statement and its by-name `{wiki}` removal are build-3's own text,
shipped six days after `ST-2` was opened and P-15 shipped the vocabulary for retiring exactly this.
**The invariant was reinforced by a build in the very cycle whose thesis is that rules without
enforcement points do not bind.** Verified: `version: 9` is current and the text is build-3's.

**What the retirement is, precisely — carried forward as the filing states it, because the scope is
the ruling.** Retire the **prohibition** at `extraction.md:84` and `checks.md:19` case (b).

⚠ **Two constraints the filing states as non-negotiable, both preserved verbatim:**

> *"**`para_type_unknown` is NOT retired and this filing does not ask for that.** A genuinely
> undeclared value (`type: banana` at an `{areas}` address) must still land loud. … **Retiring a
> prohibition is not retiring its enforcement.**"*

> *"**And the `{wiki}` carve-out is retired with it, in the same act.** … ⚠ **This half is not
> optional.** Retiring the prohibition while leaving `{wiki}` a named exception converts a category
> back into an allowlist — *'four exceptions, zero categories'* is `ST-2`'s measured failure mode …
> **A build that ships half of this has shipped pass five.**"*

**Routing note the filing makes and capture endorses:** the sibling retirement (A15-13) *"is named
here and filed separately … because its retirement is a different act with a different population
(an attestation roster, not a vocabulary), and folding two retirements into one build is how a
structural change becomes unreviewable. **Capture should route both to the same ideation.**"* Done —
both are in this batch, and both are the material for the roundtable's **obsolescence beat, which
has never been exercised**.

⚠ **Read `_output/problem-solution-2026-08-25.md` before touching PARA zoning again** — carried
forward from Cycle 14's closeout, gitignored, provenance only.

---

### A15-13. `class: supersession` — retire the `verified_by` roster closure (2026-09-01) — `factory/inbox/2026-09-01-170000-supersession-the-verified-by-roster-is-superseded-by-the-authorization-net.md`

**CONFIRMED — both halves. And the proof is the strongest artifact in this capture: two shipped
clauses that cannot both be satisfied.** *(Tracker **#18**; sibling of A15-12.)*

**Half 1 — the rule now redundant. Verified verbatim at
`skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md:47` (`version: 5` at
`:11`):**

> *"**`verified_by` value set:** the `verified_by` value set is this file's `consumers:` **that are
> write ops**, plus write-op `local_consumers:` registrants … The roster is **membership and
> ceiling**, never an automatic grant."*

**Half 2 — the mechanism. Verified verbatim at `skills/vlt-lint/references/checks.md:20`**, and the
check states its own purpose in the exact terms the filing needs:

> *"**`para_writer_unauthorized`** (governance check; both modes) — the **write-posture** net, **the
> authorization question a location rule could never answer.** For each file in the `para_*`
> population above, resolve the posture: walk **up** to the **nearest declaring ancestor
> container** … and join the file's writer identities against that list, admitting on **any**
> match: `author: human` → `human`, `author: agent` → `agent`, **`author: hybrid` → `human`** …
> and the attestation **`verified_by:` → that partner slug.**"*

**⚠ The contradiction, verified in both directions.** `checks.md:20`'s identity-resolution list
resolves **`verified_by:` → that partner slug**. `write-verification.md:47` limits the field's legal
values to write-op consumers and write-op `local_consumers:` registrants. **A partner slug is not a
write op.** So the authorization net ships with a resolution leg **that no conformant vault can ever
exercise.** This is not an inference about intent — it is two shipped clauses in current source that
cannot both be satisfied, and the filing is right that one of them has to move.

**Population — exact, verified.** `checks.md:20` runs over *"each file in the `para_*` population
above"*, which `:19` defines as `{projects}` / `{areas}` / `{resources}` with `{wiki}` excluded by
name, in **both modes**. That is the identical file set the roster's attestation requirement
governs. **No population is left uncovered by the retirement.**

**⚠ Study correction — grounding relocates the primary citation.** The filing cites **`ST-2`**
(location as proxy for trust). That fits the sibling A15-12 exactly, and it is not wrong here. But
this instance's shape is more precisely **`ST-6` — closed rosters meet authorized actors**
(`status: standing`), whose secondary cause reads:

> *"a roster is written from the actors that exist when it is written, and its membership rule is
> stated as a property of those actors (**'consumers that are write ops'**) rather than as a
> property of the capability. So the roster cannot admit an actor of a kind its author did not
> anticipate, even when the granting rule plainly covers it."*

**That is `write-verification.md:47` quoted almost verbatim, written before this filing existed.**
And `ST-6`'s enabling cause — *"the module has no check that a grant and its roster cover the same
population … the contradiction is only visible to a reader holding both files at once"* — is exactly
how this survived: `checks.md:20` and `write-verification.md:47` are each locally correct.
**Recorded as `ST-6` instance 3**, and this capture is appended to both studies' `cited_by:`.
Ideation should read `ST-6` before ruling, because it predicts the shape of a bad fix (re-widening
the roster by naming more actors, rather than stating the membership rule as a property of the
capability).

**⚠ The self-naming fact, verified.** `write-verification.md:55` (v5, Cycle 14 build-5) reads
*"fusing permission to provenance is the write-path failure this exemption exists to prevent"* — a
correct principle, shipped in the same file, **eight lines from the roster that fuses permission to
provenance** by restricting *who may mark* to a list of *what may write*. As with A15-12, a Cycle 14
build named the disease while writing another instance of it.

**Field evidence, re-verified.** **27** Layer-3 files outside `{wiki}` carry `author: agent|hybrid`
with no attestation pair, across six partners' domains — count confirmed unchanged on the
2026-09-01 sweep. **Zero** partner-sitting-written Layer-3 documents are attested, **and under the
current value set none can be.** The tier-1 pass *is* being run — the park records *"the substance
the pair stands for is done and reported; only the marker is withheld."* The work happens; the field
cannot record it. The alternatives were considered and refused at park time, and the module later
**ratified the refusal**.

**What the retirement is, precisely.** Retire the roster's **closure** at `write-verification.md:47`
— the clause limiting `verified_by` to write ops and write-op registrants.

⚠ **Three constraints the filing states, all preserved:**

> *"**The attestation pair is NOT retired** … `verified_by:`/`verified_at:` stay required on Layer-3
> knowledge artifacts; `para_missing_attestation` keeps its job. What changes is **which values are
> legal in the field**. **Retiring a restriction is not retiring the field.**"*

> *"**Nor does this ask for authorization to be dropped.** It asks for it to be answered **once**,
> by the net built to answer it, instead of twice."*

> *"Where no ancestor declares `writers:`, `checks.md:20` already rules the posture **`open` and the
> file PASSES**; that default is the honest one and this filing does not disturb it."* — **verified
> verbatim in source.**

**Open design question, carried verbatim — the filing explicitly hands this to capture and capture
hands it to ideation rather than resolving it:**

> *"**The residual question capture must rule rather than assume:** whether an unrostered attester
> needs *any* floor (e.g. must name an identity the vault has minted) or whether the container
> `writers:` join is the whole of it. The vault's read is the latter — `writers:` is human-gated, so
> the human already holds the gate — **but that is a ruling, not a fact.**"*

Capture declines it deliberately: it is a scope ruling with a live population behind it (park #16),
and the standing rule is that a filing's open questions go to ideation unresolved.

**Park status.** This filing is what live parked-interim **#16** re-parks against — *"#16's original
question was answered, narrowly and by artifact class, and the substantive half was **refused**
rather than resolved … **The vault is holding for retirement.**"* Cycle 14's closeout recorded the
re-park; this entry is its capture.

---

### A15-14. The superseded predecessor — WITHDRAWN at capture, by the filing that replaced it (2026-08-31) — `factory/inbox/2026-08-31-152000-para-type-carve-out-is-an-enumeration-of-one-and-penalizes-accurate-vocabulary.md`

**WITHDRAWN. Not graded on its merits; superseded by A15-12 at that filing's own explicit
instruction, and captured here so the withdrawal is a record rather than a silence.**

A15-12 states it directly:

> *"**It supersedes `factory/inbox/2026-08-31-152000-…`**, which reported the same friction as a
> defect and proposed a new mechanism — *'a filing that ends in a new carve-out has diagnosed the
> symptom,'* and that one did. That filing should be **withdrawn at capture** in favour of this
> one; its grounding (the `{wiki}` asymmetry, the accuracy inversion, the measured population) is
> reproduced here and is not lost."*

**Capture verified the second clause before honoring the first.** The three substantive findings
`152000` carried are all present in A15-12: the `{wiki}` asymmetry (grounded there against
`extraction.md:84` and `vault-operating-contract.md:70`), the accuracy inversion (`dispatch-brief`
legal / `research` not), and the measured population (9 files, up from 5 → 8). **Nothing is lost by
the withdrawal**, which is the only condition under which capture would honor a filing's request to
retire another.

**Why the withdrawal is itself signal, and belongs in the record.** `152000` is a *good filing that
diagnosed a symptom* — it reported real friction, correctly, and proposed a **new mechanism** to
accommodate it. `ST-2` RC2 names precisely that reflex: *"the repo's own governance quality biases
toward perimeter patches … they make the minimal patch the rational move every time — which is
exactly how a root cause survives four cycles."* The loop then produced three perimeter moves in
three days off this friction — this filing, an owner-ruled hot-fix brief (Cycle 14 **build-6**,
scoped minimal with the `{wiki}` unification cut out), and a drafted `deviation` recording the
sibling exception rather than retiring its rule. **Build-6 was withdrawn on A15-12** and Cycle 14
closed with it briefed-then-withdrawn as an `ST-2` perimeter patch.

**This is the first time the loop has retired a filing in favour of a retirement**, which is P-15's
rail doing the job it was built for — a week after it shipped, on the first material that needed it.

**No residual scope.** This entry exists so a later reader finds the withdrawal reasoned rather than
inferring it from an absence. The filing's inbox file is retired to this cycle's `filings/` on the
normal criterion (`cycle-closeout` Stage 5) alongside A15-12's, since its disposition is settled
here and carries no clause of its own.

---

### A15-15. The rail's `kind` set has no value for a supersession (2026-09-01) — `factory/inbox/2026-09-01-183000-rail-kind-set-has-no-value-for-a-supersession.md`

**CONFIRMED, all five sites. Routing re-derived and the filer's pre-ruling upheld — this is cycle
work with a named factory-side half.**

**The claim, verified: the module has four filing classes and its transport carries three.**
`factory/inbox/README.md` defines `supersession` (platform **P-15**, 2026-08-25) with two mandatory
halves no other class requires. `skills/vlt-feedback/references/field-contract.md` §The payload
field set defines `kind` as *"`defect` … `pattern` … `candidate`"*, and its label table carries
`field:defect` / `field:pattern` / `field:candidate` and no fourth.

**Observed in anger, and this run is a witness rather than a reader.** A15-12 and A15-13 — the
class's first two real instances — are filed on the tracker as **#17** and **#18**, both
`field:candidate`, both carrying an apologetic classification note in the body. **This capture
confirmed both labels directly against the live tracker** while performing the intake. The filing's
argument stands: *"A classification that has to be explained in prose is not doing its job — and the
explanation lives in the body, where neither the label filter, the issue-form router, nor
`issue-triage`'s classification check can read it."*

**The five sites, each re-derived this run.**

| Site | Change | Channel | Verified |
|---|---|---|---|
| `skills/vlt-feedback/references/field-contract.md` | the `kind` row's value set; a `field:supersession` row in the label table | **shipped → cycle** | ✅ both tables read; neither carries a fourth value |
| `skills/vlt-feedback/` (the composer) | emit the new value | **shipped → cycle** | ✅ |
| `.github/ISSUE_TEMPLATE/` | **a fourth form** | repo-side → **platform** | ✅ three forms present (`field-defect.yml`, `field-pattern.yml`, `field-candidate.yml`); `field-candidate.yml:7` hard-codes `labels: ["vault-filed", "field:candidate"]` and its `kind` dropdown is a **single-option** list with `options: [candidate]`. **There is no shared dropdown to widen** — confirmed |
| the tracker's label set | a `field:supersession` label | shipped (defined in the contract table) | ✅ |
| `.claude/skills/issue-triage/` | the classification check's value set | **platform** | ✅ |

**Routing — re-derived, not trusted.** The filing pre-ruled itself cycle-not-platform and cited the
boundary and [P-10]'s out-of-scope. **Grounding confirms it: three of five sites are under the
shipped surface** (`skills/vlt-*`), which the channel boundary sends to the cycle roadmap without
exception. Per the fork's rule for a filing with sites on both sides, **it captures here, with the
factory-side half named as a platform candidate** — the fourth issue form and `issue-triage`'s value
set — rather than being split into two entries in two ledgers without an owner ruling. That split,
if wanted, is ideation's.

**The additive-only claim, verified.** `field-contract.md` §Contract version: *"**Evolution rule —
additive-only.** Adding a payload field does **not** bump `rail_contract`. … The same rule covers
labels: **adding a label is additive** (no bump)."* **So the whole change lands without a
`rail_contract` bump and without invalidating a single filed issue.** The filing's ⚠ notes that the
platform ledger's P-10 entry over-stated the bump and was corrected there 2026-09-01; capture did
not re-verify that correction and does not rest on it.

**Not asked for, carried forward:** *"a fifth class, any change to what the three existing kinds
mean, or any change to the two mandatory halves the README already defines."*

**⚠ The timing argument, and capture endorses it as a real ordering constraint rather than
advocacy.** The filing's close: *"Cycle 15's ideation is already scheduled to rule two supersession
retirements (#17, #18) at the roundtable's obsolescence beat. That is the first cycle where the
class carries real weight — and the run where the missing vocabulary will be most visible."* That is
now literally true of this roadmap: A15-12 and A15-13 are in this batch, the obsolescence beat has
never been exercised, and the two filings that will exercise it are mis-classified on the tracker
right now. **This is a joint** — it bears on the order of builds within the cycle — which makes it
roundtable material under `roadmap-roundtable`'s frame rather than a scope-internal detail.

---

## Routed away from this cycle — the platform fork

**One filing routed to the platform ledger this run.**

- `factory/inbox/2026-08-31-104502-resources-write-legality-check-has-no-cause-and-survived-three-runs.md`
  → **[P-22]**, queued at `factory/platform/roadmap.md`.

**It was NOT marked `channel: platform`.** Under the fork's rule for an unmarked filing whose fix
site is plainly factory-side, capture surfaced it to the owner as a routing question rather than
re-routing it silently; the owner ruled it to the ledger on 2026-09-01. The grounding behind the
question: its only fix site is
`.claude/skills/build-brief/references/brief-anatomy.md` — a factory skill reference that
`vlt-upgrade` never copies into a vault. The filing itself says so (*"Factory-side signal: this
concerns how acceptance checks are written, not shipped module behaviour"*), but a filer's opinion
is not the boundary, so it was re-derived.

**The filing does not move.** It stays in the active inbox: `cycle-closeout` Stage 5 retires filings
against *cycle* builds, and a platform item joins no acceptance ledger, so nothing would ever move
it. It is **not** in this roadmap's `derives_from:` — the cycle derives nothing from it — and it is
named here so the run's filing count reconciles: **16 graded = 15 captured + 1 routed.**

**Fork outcome, reported in full:** **no filing in the un-captured set carried the `channel:
platform` marker.** The marker's first real exercise found nothing marked and one unmarked
candidate, which is the fork's weak branch behaving exactly as [P-3] designed it — the marker is
optional, the boundary is re-derived, and an unmarked factory-side filing reaches the owner rather
than being routed by an agent's judgment.

## Capture narrative — the judgment calls this run made

Recorded here because this skill keeps no separate decision log; the roadmap is it.

1. **What counted as un-captured.** The inbox holds 70 filings, but `factory/inbox/README.md`'s
   lifecycle means a filing stays there until its build ships **and** its clauses pass acceptance —
   so most are captured-but-not-retired. Membership in a prior cycle's **`derives_from:`** was used
   as the test, not filename mentions: Cycle 14's roadmap *names* several un-captured filings in
   prose (its closeout item 15 lists four by name), and a mention test would have wrongly excluded
   them. **54 already-captured, 16 genuinely un-captured.**

2. **Scope: all 16, owner-ruled.** Three narrower options were offered (defer #13; capture only the
   gating clusters; capture in two passes). The owner ruled all 16.

3. **A15-11 (#13) is captured without overturning its deferral.** Cycle 14 roundtable A27 deferred
   it as net-new capability. Capture records the deferral, records that Cycle 14 itself named the
   condition under which it stops being net-new, and records that the condition has arrived — but
   **re-admission is an owner ruling and capture does not make it.**

4. **A15-14 was withdrawn on another filing's instruction, after verifying nothing was lost.** A
   filing asking that another be withdrawn is honored only when its findings are demonstrably
   carried; all three of `152000`'s were checked against A15-12 first.

5. **A15-3 was corrected against the evidence, and it changed the answer.** It was initially graded
   CONFIRMED on its own diagnosis. Dereferencing its cited report (P-18's second grounding axis)
   showed the reported target is a **non-empty** string, which proves the empty-string path never
   ran and relocates the defect to the scanner. **The filing's proposed fix is already in the tree
   at `vlt-lint-full.js:423`.** Had this not been caught, the cycle would have shipped a no-op with
   a fixture that passes.

6. **`ST-7` was opened without a ruling.** Grounding kept finding one shape under seven filings from
   four sweeps — this register's own named trigger. Opening a study needs no owner ruling and gates
   nothing (`factory/studies/README.md`).

7. **`ST-6` was added to A15-13 as the primary citation.** The filing cites `ST-2`; grounding found
   `ST-6`'s secondary cause quotes `write-verification.md:47`'s membership rule almost verbatim,
   written before this filing existed. `ST-2` is not removed — both are cited.

8. **A15-9's companion finding was left in place, not routed.** It is factory-side (brief-time check
   anatomy) and would ordinarily be a routing question. It was left because the filing deliberately
   keeps both halves of the cost problem legible together, and splitting it would destroy that.
   Ideation may route it; capture did not.

9. **Tracker label drift was repaired, owner-ruled.** Issues **#17** and **#18** carried
   hand-written `origin:` headers (a filing→issue direction the contract has no route for, recorded
   in both filings and owner-ruled on 2026-09-01) and lacked the `captured` label. **Nothing was
   re-materialized** — the headers are the idempotency key and both matched. The label was applied
   on the owner's ruling this run.

10. **No spike stub was opened.** A15-11's direction 2 (`argsPath`) is an external unknown by the
    filing's own framing, but direction 1 does not depend on it and the filing does not rest its ask
    on it. If ideation takes direction 2, the spike is due **before** the brief.

## GitHub intake — this run's record

Ran against `mggower/bmad-module-vlt` (`feedback_repo.default`,
`skills/vlt-setup/assets/module.yaml`); `gh` authenticated, no degradation.

- **Query** (`--label vault-accepted --state open`): **9 issues** — #18, #17, #16, #15, #13, #11,
  #7, #6, #1.
- **Idempotence exclusion:** **all 9** already carry an `origin:` header on disk. **Nothing
  materialized this run** (`issues_materialized: []`).
- **Label drift:** #17 and #18 lacked `captured`; applied on the owner's ruling (see narrative 9).
- **Amendment leg** (`--label captured --label amended --state open`): **no hits.** No holds, no
  appends.
- **Stale-shape gate:** not reached — no issue proceeded past exclusion.

## Carried forward INTO this cycle from Cycle 14

Named, not restated — the authoritative text is
`factory/cycles/14-no-enforcement-point/roadmap.md` §Carried forward past Cycle 14, both halves
(items 1–10 ideation-time, 11–17 acceptance-time). Ideation must consume that section; this list
exists so nothing is lost between the two documents.

⚠ **TWO BOUND DEBTS THAT GATE THIS CYCLE**, both tagged `[ship-verifiable]` deliberately so they
cannot be carried again (the A4-4(5) lesson, applied preemptively):

1. **Cycle 14 build-3 (6)** — the two parks, unwind. Owner-ruled at closeout into bound debt; Cycle
   14 closed on this as its **one honest gating FAIL**, a green being available only by falsifying a
   `type:` field. ⚠ **A15-12 and A15-13 are the retirements those parks are now holding for** — the
   debt and the two supersessions are the same subject matter and must be ruled together.
2. **Cycle 14 build-1 (6)** — `malformed_frontmatter`, ruled 2026-08-31. **E4 at 10/8/2, not zero.**
   ⚠ **A15-5 is a fresh measurement on this exact check** (10 findings, 8 genuine, 2 refuted) and
   should be read against the bound rather than separately.

Plus: three filings held live in the inbox with undischarged clauses (`…-164501` = A14-2 — **A15-1
is its recurrence datum**; `…-125529` = A14-6, park #15's clause; `…-141418` = A14-7, park #16's
clause — **A15-13 is what park #16 re-parks against**), the released standing watches, and ruling
4c's bound.

⚠ **Owed and outside any build, carried from Cycle 14's closeout and now DISCHARGED in part:**
Cycle 14 recorded that neither supersession had been posted through `vlt-feedback`, so park #16
referenced no live tracker issue. **Both are now posted — #17 and #18** — and this run labeled them
`captured`. The owner performed the posting; the ⚠ is retired.

## Open design questions carried into ideation

Verbatim from their filings, unresolved by capture, gathered so ideation has them in one place. Each
is also stated at its own entry.

1. **A15-3** — *"Whether the anchor's **existence** should be validated (the heading is present
   here, but a stale anchor is a real defect class) is a separate question capture should rule
   rather than fold in."* ⚠ Grounding raises its stakes: since the "empty target" half is already
   shipped, this is now the only unbuilt anchor-related thing in that filing.
2. **A15-13** — *"whether an unrostered attester needs **any** floor (e.g. must name an identity the
   vault has minted) or whether the container `writers:` join is the whole of it. The vault's read
   is the latter … but that is a ruling, not a fact."*
3. **A15-9** — direction 1 *"needs the 'what does a cached record actually depend on' question
   answered explicitly, which no site answers today."*
4. **A15-2** — whether the denominated-empty half ships with the prose repair or separately.
5. **A15-15** — whether the factory-side half (the fourth issue form, `issue-triage`'s value set)
   splits to the platform ledger or rides the cycle build. Capture kept them together; the split is
   an owner call.

## Deferred acceptance ledger

*(Empty — populated by `build-brief` as each build is briefed.)* **Cycle 14's two bound debts are appended HERE by the briefs of the builds that carry them** *(roundtable A18, 2026-09-02 — the earlier sentence "not entries here; graded against Cycle 14's ledger text" pointed every parser at a CLOSED roadmap)*: build-4 appends Cycle 14 build-1 (6) leg 3; build-6 appends Cycle 14 build-3 (6) clauses (a)+(c) — each as a `[ship-verifiable]` sub-clause quoting Cycle 14's bound text verbatim (the b3(7) precedent), the vault-act half of the parks debt tagged `[field-contingent]` per D-D.

- [ ] **build-1 (supersession-kind, briefed 2026-09-02):** brief
  `factory/cycles/15-nothing-reads-it-back/briefs/build-1-supersession-kind.md`. **Five checks — four
  `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 2/2` (observed: #17, #18;
  preserved: both are check (3)'s subjects, #17's body seeds check (4)'s fixture). R1 n/a (nothing
  ships ahead of its mechanism); Retirement n/a (obsolescence beat: none found, re-checked at brief);
  R4 n/a (the new form is `.github/`, never copied; fixtures un-enumerated — declared exclusion).
  **(1) `[ship-verifiable]` — at rest — GATES:** every surface that names the rail's kind set names
  `supersession` — instrument: a per-old-value grep manifest (each `defect`/`pattern`/`candidate`
  kind-naming hit must co-occur with `supersession` in the same file; the four single-kind forms the
  enumerated exception); adversary: a `|`- or `/`-separated list a grep for the new value misses —
  widened to grep the old values. **(2) `[ship-verifiable]` — at the v0.18.0 release sitting — GATES:**
  after the owner runs `config.yml`'s label bootstrap, `gh label list` carries `field:supersession` and
  the issue chooser lists four field-contract forms; adversary: label exists but the form's `labels:`
  still says `field:candidate` — widened by the form-parse assertion on `labels:` byte-for-byte.
  **(3) `[ship-verifiable]` — after the owner act, before the v0.18.0 tag — GATES** *(A9)*: #17 and #18
  re-kinded (body `### kind` → `supersession` AND label → `field:supersession`) and the
  `issue-triage/SKILL.md:70-72` comparison, applied directly via `gh issue view <n> --json labels,body`
  (both are `captured`, outside triage's queue), reports no mismatch on either; adversary: label-only
  relabel (caught — both sides read), or the apologetic classification note still in the body —
  widened: the note's absence is asserted, a stale note FAILS. **(4) `[ship-verifiable]` — at rest —
  GATES:** the fixture pair `fixtures/build-1-supersession-payload-17.md` (#17's real body re-shaped
  with `kind: supersession` + both halves) and `…-missing-half.md` run through `github-intake.md` §4 as
  a reader protocol (no `gh`, scratch output): the first yields a filing whose line 1 opens
  `# \`class: supersession\`` byte-equal to the two on-disk specimens' opening shape, the second is
  HELD with a named reason and writes nothing; adversary: marker present but in a spelling/position
  `grounding-methodology.md:57-59` does not key on — widened: the two hand-written specimens are the
  oracle. **(5) `[field-contingent]`:** a vault files a real retirement through `vlt-feedback` —
  event: the next `supersession` filing from a live vault (named candidate: Cycle 14 carry 6,
  `para_author_unknown`); performer: the owner from `{field-vault}` (readable); grades: issue labelled
  `field:supersession`, both halves non-empty, no classification note, and the next `inbox-capture`
  materializes it with the `class: supersession` opening line. Unbounded; watch register if unfired.

## Ideation rulings — A15-1..A15-15 (owner-steered, 2026-09-01)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**COMPLETE — filled over seven owner-steered rounds, 2026-09-01 to 2026-09-02.** Skeleton laid by
`ideation-scaffold`; **every slot is ruled and no slot is empty.** `build-brief` gates on this
section being filled — it is.

**What each round settled.**

- **Round 1 — the cause.** `ST-7` **does not bind** (D1(a)); the mechanism question folds into
  Grouping (D1(b)). ⚠ And the round's grounding found that **the reduce cannot perform its own
  read-back** — a premise `ST-7` and two captured entries all asserted. Corrected in three places at Round 1, the fourth (A15-4) at Round 5 *(roundtable A19 — the line said "all four")*.
- **Round 2 — scope.** **All fifteen.** A15-11 re-admitted (Q1); **direction 1 only**, `argsPath`
  declined as a **Claude Code harness** parameter with no rail to request it (Q2); and A15-11 is
  **upstream** of the read-back, a **hard ordering constraint** (Q2b).
- **Round 3 — the retirements.** **No floor** on `verified_by:`, the container `writers:` join is
  the whole of it (Q5); **all five non-negotiable constraints adopted** (D5); **each bound Cycle 14
  debt rides its subject-matter build** (Q9).
- **Round 4 — routing and preconditions.** A15-9 takes **both directions, d2 → d1**, and its
  precondition is **ruled answered from source** (Q3); the companion finding **routes to the
  platform ledger** (Q4); A15-15 ships as **one act** (Q6).
- **Round 5 — the remaining scope.** Anchor-existence **declined**, A15-3 folds (Q7); A15-2's halves
  **together** (Q8); **D2 adopted** — ⚠ *the only read-back entering this cycle*; A15-4 direction 2
  **half-taken**, eviction in, provenance deferred (D3).
- **Round 6 — the debts.** E1 **validation + cardinality**, the `type:` distribution out; E2
  **attached**; E3 **discharged**. ⚠ Round 6 also found that a **type-only validator does not catch
  the rollup**, which is what shaped E1.
- **Round 7 — grouping and promises (2026-09-02).** **Seven builds, one release, v0.18.0**; every
  `binds:` / `spike:` / `promise:` filled; spikes ruled none-opened-none-consumed; three questions
  deferred to brief time by ruling.

**⚠ Four grounding corrections were applied to upstream records in-session, on owner rulings** — the
`ST-7`/A15-1/A15-4 *reduce-has-the-path* premise, and the A15-8 *live gating blocker* reading. Two
promises were also caught over-claiming before ratification (build-1's routing clause, build-7's
"27 files clear on release"). See the entries.

**Next: `roadmap-roundtable`.** Briefs follow the review; `build-brief` gates on that record too.

### Grouping & order

**Cycle scope — RULED Round 2 (2026-09-01): ALL FIFTEEN. A15-1..A15-15 are in this cycle; nothing
defers.** A15-11's Cycle 14 deferral is overturned (Q1). See *Pre-ideation rulings* Q1/Q2/Q2b.
*(A15-14 was WITHDRAWN at capture by the filing that replaced it and takes no build — 14 filings
need build homes.)*

**Grouping, order and release count — RULED 2026-09-02: SEVEN BUILDS, ONE RELEASE, v0.18.0.**
One release is sufficient because no build in this batch depends on a prior release's field evidence
(the condition that forced Cycle 14 to three). The bump is **minor** because the two retirements
change shipped rule semantics.

⚠ **Ordering note:** with one release all seven ship together, so build order governs commit order
and review sequence, not field exposure. **The one exception is Q2b, which is a hard rule
regardless:** build-2 precedes build-4.

**Ordering, extended at the roundtable (2026-09-02, A2/A4):** file-edit order is **2 → 3 → 4 → 6 → 7** —
builds 2/3 share `vlt-lint-full.js:55-66`, `:262-271` and one `full-scale.md` step 2 paragraph; 3/5 share
`report.md`; 4/7 share `vlt-lint-full.js`; 6/7 share `vlt-lint/SKILL.md:4`. And ⚠ **v0.18.0's first
full sweep is COLD BY CONSTRUCTION** — build-7 moves a scanner-read convention and the prompt literal at
`vlt-lint-full.js:229`; build-6 moves `pin_vector` as shipped; builds 6/7 move `checks.md`. Build-2's
cache clauses are therefore graded **at rest** (see its entry) and the CHANGELOG states the cold run.

⚠ **`promise:` authorship — a deliberate, recorded deviation from P-16's letter (2026-09-02).** The
standing rule says the promise is *written here at ruling time by the owner*. In this session the
promises are **clerk-drafted and owner-ratified**: the clerk offers candidates that promise
**materially different things** (scope, not tone) and the owner's pick is therefore a scope choice,
not a proofread; where all candidates are wrong the owner says so and the clerk drafts again.
**Recorded rather than done silently**, because P-16's target is a *briefer* authoring the sentence
after the fact — reporting a decision they did not make — and that failure is not reproduced here:
the owner is present, owns the scope call, and ratifies the words at ruling time. **The safeguard
that makes it honest is grounding each candidate before ratification, and it fired twice** —
build-1's first pick and build-7's draft were both caught over-claiming (see their entries).

- **build-1 — A15-15, the rail's missing `supersession` kind.** All five sites in one act (Q6): the
  `field-contract.md` `kind` row **and** its label table, the `vlt-feedback` composer, the tracker
  label, the fourth `.github/ISSUE_TEMPLATE/` form, and `issue-triage`'s classification value set.
  Additive-only — **no `rail_contract` bump, no filed issue invalidated**. First because the class
  must exist before the beat that rules the retirements, and because it is independent of every
  other build.
  - `binds:` Q6, D5
  - `spike:` `none`
  - `promise:` **After this ships, a vault owner filing a retirement gets an issue that says it is
    one — findable by label, routed by its own form, and checked by triage against the body —
    instead of a candidate whose real class survives only in a note nothing machine-readable can
    read.** *(Owner-ratified 2026-09-02.)*

    ⚠ **A stronger draft was rejected on grounding, and the correction is recorded so no brief
    re-inflates it.** The rejected clause claimed a retirement would now *"reach the roadmap through
    the same route as a defect, instead of surviving only because a human read the body."* **The
    route was never broken:** `inbox-capture`'s intake queries the owner-applied **`vault-accepted`**
    label, not `field:*` kind (`.claude/skills/inbox-capture/SKILL.md:62` — *"`vault-filed` marks
    candidacy, not acceptance"*), so materialization is kind-agnostic. **Proof in this cycle:** #17
    and #18 were filed as `candidate` and reached this roadmap anyway — they are A15-12 and A15-13.
    An acceptance check written against the rejected clause would have failed honestly.

  - **Roundtable amendments (2026-09-02):**
    - *(A9, 13 lanes)* **The ordering sentence "first because the class must exist before the beat" is
      STRUCK** — the beat is the roundtable that ruled this, which precedes every build; under one release
      build order constrains no field exposure. What is real is the tracker: **#17 and #18 are re-kinded
      by an owner act after build-1 lands — body `kind:` → `supersession` AND label →
      `field:supersession`** (the body's `kind` is authoritative to `issue-triage`,
      `.claude/skills/issue-triage/SKILL.md:70-72`, so a label-only relabel manufactures the mismatch
      triage flags); no re-materialization, the `origin:` header is the key. `[ship-verifiable]`: triage
      reports no mismatch on either.
    - *(A10)* **Sites corrected and completed.** Site 5 as named was a phantom — `issue-triage` has **no**
      classification value set; what drifts there are line-range cites (`issue-triage/SKILL.md:52, :78`;
      `inbox-capture/references/github-intake.md:57, :61`), re-pointed. **Site 6 = the intake
      materializer**: `github-intake.md` §4 maps `kind: supersession` → `class: supersession` **in the
      opening line** (the marker `factory/inbox/README.md:80` and `grounding-methodology.md:59` key on —
      without it a rail-filed retirement is graded as a candidate) and **holds** materialization when both
      halves are unidentifiable. **Site 7** = `.github/ISSUE_TEMPLATE/config.yml:13-15`'s `gh label create`
      block. Composer restatements enumerated: `vlt-feedback/SKILL.md:4`, `:51-53`, `:56`, `:87`, `:101`,
      `module-help.csv:18`. The `kind` row's `supersession` value states the class's **two mandatory
      halves** in one clause; the halves ship as two **optional, additive** payload fields
      (`superseded_rule`, `superseding_mechanism` — required when `kind: supersession`), so triage and the
      intake have something structured to read. **E3 amended** (see E3). The fourth form carries
      `field-candidate.yml:16`'s `@mention` line with a pointer to `S-3` (met, not consumed).
  - `binds:` **corrected → Q6, E3, S-3 *(named, not consumed)***. D5 removed — nothing in build-1 invokes
    it; `build-brief` resolves rosters by id. *(roundtable A10, G-F4)*
  - **Grounding corrections at brief time (2026-09-02, `build-brief` — brief
    `briefs/build-1-supersession-kind.md`):** three of A10's cites are superseded; scope unchanged.
    (i) ~~`vlt-feedback/SKILL.md:56`~~ is the duplicate-guard `gh issue list` line and names no kind —
    the compose site is **`:61-62`**. (ii) ~~`field-candidate.yml:16`~~ → the `@mention` line is
    **`:17`**. (iii) the drifting line-range cites are not at ~~`issue-triage/SKILL.md:52, :78`~~ /
    ~~`github-intake.md:57, :61`~~ but at **`issue-triage/SKILL.md:61, :81`** and
    **`github-intake.md:30, :38, :41, :57, :62, :67, :91, :144`** — and **eight of those ten are already
    stale today** (the contract's tables moved before this cycle); the brief re-points all ten (F6/F7).
    Grounding addition: `github-intake.md:61`'s hard count *"the eight `### <field_id>` sections"* is a
    restatement and goes with the same edit. BRIEFED 2026-09-02.

- **build-2 — A15-9 + A15-11 + A15-4's eviction half: what the instrument costs to run.**
  A15-9 both directions **ordered d2 → d1** (Q3); A15-11 **direction 1 only** (Q2 — document the
  `scriptPath` route in `full-scale.md` step 3; direction 2 declined); A15-4's **direction 2
  invalidation half** (D3 — `lint-cache.py` gains an eviction path; **record provenance is
  deferred**). ⚠ **Placed before build-4 to satisfy Q2b's hard ordering.**
  - `binds:` Q3, Q2, Q2b, D3, D4
  - `spike:` `none`
  - `promise:` **After this ships, a vault owner who re-runs `vlt-lint --full` — after an upgrade, or
    because a finding looks wrong — pays for what actually changed instead of for everything, and can
    force a re-derivation instead of being served the same suspect answer.** *(Owner-ratified
    2026-09-02.)*

    ⚠ **The promise covers FOUR outcomes and the brief must satisfy all of them** — this was raised at
    ruling time and the owner kept the build whole rather than splitting it, so the risk is named
    here rather than discovered at acceptance. *"Pays for what actually changed"* is **two** repairs
    (A15-9 d2, the upgrade case; A15-9 d1, the unrelated-convention case) **plus** A15-11 d1 (the
    ~84KB payload, re-sent on every resume, closed by documenting the `scriptPath` route). *"Can
    force a re-derivation"* is A15-4's eviction half. **A brief that ships the cache work alone has
    satisfied the first clause and not the promise** — the cache work is much the largest part, which
    is exactly why the split option was offered and declined.

  - **Roundtable amendments (2026-09-02):**
    - *(A2, 11 lanes)* ⚠ **v0.18.0's own first full sweep is COLD BY CONSTRUCTION**, correctly under D4:
      build-7 edits `write-verification.md` (a scanner-read convention) and its `@5` literal inside
      `pageScanPrompt` (`vlt-lint-full.js:229` — moves `scanFingerprint`); build-6 bumps `extraction`
      (moves `pin_vector` as shipped); builds 6/7 edit `checks.md:19-20`. So **"pays for what actually
      changed" has no live observable on the only release the cycle schedules** — the `b2(5)` shape one
      cycle after Cycle 14 named it. Both cache clauses are graded **`[ship-verifiable]` at rest**: a
      fixture of two `rulesetComponents` sets — only `module_version` moved ⇒ equal per-page key; only a
      non-scanner convention moved ⇒ equal; a scanner-read convention, the extractor, or the scan surface
      moved ⇒ unequal. The warm-after-upgrade observation is `[field-contingent]`, bound to *the first
      release after v0.18.0 that moves none of the scanner-read set*. The v0.18.0 CHANGELOG states the
      cold run so `acceptance-discharge` never reads it as a build-2 FAIL.
    - *(A3, owner ruling D-B)* **The key is re-ruled whole — see Q3's amendment.** `module_version` is
      **deleted, not replaced by prose-file digests**; **`scanModel`** enters the key; `checks_digest`
      leaves it; `pin_vector` narrows to the three scanner-read pins or drops as redundant with their
      digests. **The brief-time question "whole file or only the reduce" DISSOLVES** — neither.
    - *(A4)* **build-2 precedes build-3** on three shared sites (`vlt-lint-full.js:55-66` arg contract,
      `:262-271` `RULESET_SLOTS`/`rulesetSlotsMissing`, the `full-scale.md` step 2 paragraph); build-2
      owns the slot **population**, build-3 only the rendering/type language. d1 lands as a
      **workflow-side required-name set** — one constant shared by `convRead` and `rulesetSlotsMissing`,
      a missing name reported **by name** (today `:265-268` accepts any non-empty object, so a map missing
      `wiki-supersession` would compose a key that never invalidates when it moves — D4 breached
      silently).
    - *(A13)* **The eviction route, end to end** — D3's subcommand had no caller and step 5 rewrites the
      sidecar whole, so a hand-removed record is written straight back: an operator-facing evict step in
      `full-scale.md` step 2 run **before** the sidecar read, keyed by slug (`lint-cache.py`'s
      `{slug, key, scan}`), exposed as a `vlt-lint` intent (*"full lint, re-scan <slug>"*); `evict` emits
      `evicted K of N`, K=0 a loud non-zero; `report.md:78`'s `lint_cache:` line renders
      `evicted E by request`; the **legal response** written into `full-scale.md`/`fix-and-file.md`: *a
      finding the operator refuses as false evicts its page's record before the report persists* (the
      field's `false_positives_refused` ships nowhere — without this the loop is refuse → re-serve →
      refuse). At-rest acceptance: fixture of N records; evict one; `read` returns N-1; the next
      identical-input run puts exactly that slug in `toScan` (`:306-308`). The live `cornerboxes` specimen
      **cannot** grade it — the cold sweep re-derives it first. D3's *"only remedies"* sentence is
      corrected: `runKey` leads with `pageHashes[slug]`, so a byte change already evicts; eviction's value
      is that it is **designed and reported**.
    - *(A20, obsolescence)* **Retire in the same act:** `full-scale.md` step 2's *"State it plainly: the
      first full run after any release is a COLD one"* + its `0.15.0 → 0.16.0` worked instance,
      `report.md:89`'s echo, and the `module_version: string` arg-contract row (`:58`) → *"cold when the
      scan surface, the extractor, or a scanner-read convention moved — and the cold reason names
      which."* Step 5's *"deleting it is always safe and costs only a cold run"* stays true and becomes
      the **second** remedy behind eviction. The `cold (<reason>)` rendering names the moved slot(s).
  - `binds:` **+= Q3 (as amended), D2 (the `RULESET_SLOTS`-loop property — build-2's new slot inherits
    it)**. *(roundtable A3, A14)*

- **build-3 — A15-2 + A15-6 + A15-10, the denominated slots.** D2's **whole population** in one
  build, so the cycle's only read-back posture lands coherently rather than split across three
  briefs. A15-2's two halves ship together (Q8).
  - `binds:` D2, Q8
  - `spike:` `none`
  - `promise:` **After this ships, a vault owner reading a lint report sees each derived slot with
    the population it came from — "0 slugs found under `## Stubs…` across 1 index" — and a slot that
    arrived wrong is reported as wrong rather than as absent.** *(Owner-ratified 2026-09-02.)*

    ⚠ **The second clause exists because the first does not reach A15-10, and was added at ruling
    time for exactly that reason.** `stubSlugs` and the `governance_memory` denominator are
    populations and denominate naturally; **`pin_vector` is a scalar with a type**, and its defect is
    that a **wrong type is reported as absent** — `vlt-lint-full.js:263`'s `typeof v !== 'string'`
    already separates the two cases and discards the distinction. Without the clause a brief could
    denominate the two list-shaped slots, satisfy the promise, and leave the conflation intact —
    `binds: D2` would still oblige it, but **scope is ruled against the promise**, which is the
    field's purpose.

  - **Roundtable amendments (2026-09-02):**
    - *(A4)* **Lands AFTER build-2** and rebases `rulesetSlotsMissing` on build-2's final slot set;
      A15-10's residual *"one entry per file in `{conventions}`"* is **superseded** — the population is
      Q3 d1's three. `binds:` **+= Q3**.
    - *(A14)* **D2 as amended binds here:** a present-but-wrong-type ruleset slot is a **pre-dispatch
      refusal** with a directed `next:` (the failed-run posture, `SKILL.md` §Step 6), never a cold-branch
      cap — the promise's second clause gains *"before the scan phase dispatches"*; **the denominator is
      produced by an instrument independent of the one that produced the value** — `governance_memory`:
      a form-agnostic `## ` heading count against schema-matched entries (a 47-of-47 rendered by the same
      matcher reads back nothing); `stubSlugs`: `section located: yes|no` beside the count (D2's exemplar
      *"0 slugs across 1 index"* cannot distinguish *not located* from *empty* — the observable A15-2
      reports).
    - *(A14 v)* **The report has no home for "wrong" today** — `report.md:89` closes cold reasons to
      three; `stubSlugs` has no report key; `governance_memory:` at `:44` carries no total (the field's
      *"13 of 54"* was the operator's invention). **build-3's scope includes the `report.md` edits**: a
      fourth `lint_cache:` cold reason `slot rendered with the wrong type: <slot>` at `:78`/`:89` (retiring
      the closed three-reason list), a `stub_discovery:` line, a population term in `governance_memory:`.
      **Merge order on `report.md`: build-3 → build-5** (build-5's validator is authored against
      `report.md` at build-3's commit).
    - *(A17)* **Q8 as amended:** stub discovery matches the heading **as `{conventions}/wiki-index.md:83`
      states it** (overlay-merged); `full-scale.md:7`, `checks.md:39`, `vlt-lint-full.js:44`/`:476` become
      pointers — reconciling two copies would have made a third. The bare `## Stubs` form retires.
    - *(A20, obsolescence)* the cap wording at `vlt-lint-full.js:322` (*"absent or empty slots"*) and
      `full-scale.md` step 2's *"absent slots named in `coverage_caps`"* → three-way absent / empty /
      wrong-type, in the same act.

- **build-4 — A15-1 + A15-3 + A15-4 (fidelity half) + A15-5, the scanner's returns.** One unaudited
  return, four mutations. A15-3 **folds in and carries no build of its own** (Q7).
  ⚠ **Carries Cycle 14 build-1 (6)** — `malformed_frontmatter`, E4 at 10/8/2 — `[ship-verifiable]`,
  **GATES closeout** (Q9). ⚠ **Scoped under the Round 1 correction: the reduce has no filesystem
  access**, so this read-back moves SKILL-side or the SKILL passes new inputs across the boundary.
  - `binds:` Q7, Q9, Q2b, D4, *Round 1 grounding correction*
  - `spike:` `none`
  - `promise:` **After this ships, a vault owner stops being sent to fix pages that are not broken —
    no orphan that has an inbound link, no missing target that exists, no over-length summary that is
    inside the limit.** *(Owner-ratified 2026-09-02.)*

    **The three clauses map to the build's four filings**: *orphan with an inbound link* → A15-1;
    *missing target that exists* → A15-3 (the dropped `#`) **and** A15-4 (the substituted proper
    noun), which reach the same `fix_now` slot by different mutations; *over-length summary inside
    the limit* → A15-5. **It is gradeable against live specimens already on record** — the
    `fantasy-platform-read-access` orphan (third consecutive sweep), the `cornerboxes`-for-
    `cornerbacks` substitution, and the two `161`-against-`160` summaries.

    ⚠ **The promise is the OUTCOME, not the mechanism** — a build that lands the comparison but
    leaves the specimens still firing has not met it. Chosen over a mechanism-facing draft for that
    reason.

  - **Roundtable amendments (2026-09-02):**
    - *(A11, owner ruling D-A)* **A15-5 re-grounded and re-mechanised.** The capture's *"no length
      arithmetic in `vlt-lint-full.js`"* was **false**: `:640` `summaryIssue` measures `s.summary.length`
      from the scanner's verbatim return into `frontmatter_drift`; the refuted `171`/`161` arrived through
      the scanner's **`malformed_frontmatter` verdict** — two measurers, one wrong, no comparison.
      **Ruled:** the SKILL reads each page from disk and passes `{slug: summary_len}` on the `pageHashes`
      precedent (Cycle 14's own named route, carry item 2 — **consumed here**); the reduce measures from
      that, never from the returned `summary` (Cycle 13 CF1: `l-theanine` 162 vs 159 — the return is
      itself paraphrased); the scanner is told length is **not its verdict** (`checks.md:15`'s own
      exclusion — an Arc 9 D5 elimination, prompt string only). The Cycle 14 build-1 (6) re-check names
      `frontmatter_drift` as its instrument and gains an **at-rest leg** (fixture: a quoted 158-char
      summary whose raw line is 161) with the post-release sweep as corroboration — leg 3 rests on bytes,
      not on one haiku measurement per page. *Dissent on record (Builder, Victor, Amelia): elimination
      alone sufficed for the two specimens; conceded that only the disk read closes the paraphrase case.*
    - *(A12, owner ruling D-C)* **The read-back branch is RULED, not left to brief time: REPLACE.** The
      SKILL derives each page's `[[…]]` set by an **executable** script (a sibling of `lint-cache.py` —
      never a prose recipe, or A15-2's regex-nobody-ships returns) and passes `pageLinks` (the
      `crossLayerSlugs` pattern); the reduce builds the inbound map (`:457`) and `missing_targets` (`:480`)
      from it; **`outbound_links` leaves `PAGE_SCAN.required`**; the DA7 `partialShortfall` orphan
      suppression (`:460-472`) retires with its cause. Not D3's refused direction 3 — no model changes; an
      executor is removed from a slot that never needed one. The audit alternative is recorded as
      **refused**: comparing a return against a value the consumer already holds is ceremony. *Dissent on
      record (Quinn, Carson): audit preserved the literal read-back and a rejected-return cap; conceded.*
      Any scanner-returned value the reduce still consumes after this build is subject to `full-scale.md`
      step 5's single-writer clause: **a return that fails a read-back is never persisted to the cache** —
      rejection is reduce-side, named in a denominated `scanner_return_rejected` cap (N of T).
    - *(A11)* ⚠ **Hard constraint: `PAGE_SCAN` serializes to 3676 of the 3700-char E6 budget**
      (`tools/package-lint.py:966`, measured with E6's own extractor) — no build-4 change may land in a
      schema description; prompt string or new args only. Removing `outbound_links` from `required` is
      the only edit that *frees* budget.
    - *(A12)* **The instrument is the fixture, not the specimens.** Under one release the v0.18.0 cold
      sweep re-rolls every named specimen before any check runs; the promise's acceptance could pass with
      no mechanism in the tree. The `[ship-verifiable]` check is a fixture whose SKILL-passed link set and
      page bytes are deliberately at odds with a planted scanner return (a substituted slug, a stripped
      `#`, one dropped link) and the report must follow the bytes; specimens clearing in the field is
      `[field-contingent]`.
    - *(A12)* **Discharges `factory/inbox/2026-08-26-164501` (A14-2)** — Cycle 14 pinned it in the inbox
      because Stage 5 passed it vacuously; build-4's ledger clause names the filing so Stage 5 can move
      it.
    - *(A21)* **Consumes Cycle 14 carries 2 and 3**; carry 5 (the `malformed_frontmatter` retirement) is
      ruled at this build's leg-3 grading event — see *Cycle 14 carries — dispositions*.
  - `binds:` **+= D3** (halves A15-4; *direction 3 stays refused*; *direction 1 does not cure records
    already poisoned*); **D4 kept with its reason** — new SKILL-passed inputs (`pageLinks`, `summary_len`)
    may not enter the cache key by judgment. *(roundtable A12, G-F4)*

- **build-5 — A15-7 + A15-8, the persisted report.** A15-7's parse requirement plus E1's ruling:
  validate the mandated keys **and** the **cardinality** check that un-collapses a per-file slot.
  The `type:` distribution is **out** (E1).
  - `binds:` E1, D2
  - `spike:` `none`
  - `promise:` **After this ships, a vault owner can read every persisted lint report, and each slot
    `report.md` mandates per-file carries one entry per file — or the run fails loudly instead of
    writing a report that quietly isn't one.** *(Owner-ratified 2026-09-02.)*

    **Three clauses, three obligations:** *read every report* → A15-7 (one archive in six does not
    parse; an unreadable report is **indistinguishable on disk** from a readable one, so every claim
    resting on "the archive" silently rests on 5 of 6). *One entry per file* → A15-8 instance (a),
    the 27-file rollup. *Fails loudly* → A15-8 instances (b) and (c), the dropped keys, and the
    intermittence that is *"the signature of no enforcement point."*

    ⚠ **The per-file clause is deliberate and is E1's ruling made gradeable.** A presence-checking
    draft was rejected at ruling time: the rollup **has** the key, so *"find every slot `report.md`
    promises"* passes it — the exact trap E1's correction (ii) identified. **The promise reaches
    cardinality or it reaches nothing.**

  - **Roundtable amendments (2026-09-02):**
    - *(A16)* **E1 made buildable — see E1's amendment.** In brief: one artifact is the
      key/type/cardinality source (parsed from `report.md`'s fence, or a schema file `report.md` points
      at) — never a second hand-typed list; presence + type + cardinality, **never closure** (extra keys
      pass; `false_positives_refused:` — which carried every specimen this cycle and ships nowhere — is
      promoted into `report.md` as a mandated per-slot list); each per-file slot's population is derived
      **mechanically** from the `para_*` file walk, never `len()` of the rendered list (the renderer's own
      count reads back nothing); the gate runs via a `uv run` script with inline deps (the `lint-cache.py`
      precedent) or `json.loads` over the JSON render, `report.md:3`'s no-dependency clause pointing at
      that route.
    - *(A16)* **"Fails loudly" names what the owner is left holding — never no file.** A failed gate
      re-renders **once** from the same Step-5 facts; a second failure persists the existing
      `…-lint-failed.yaml` shape with `status: failed`, `reason: shape — <slot / cardinality>`, the full
      unvalidated block embedded, and `next: re-render from the returned workflow object, not re-sweep`;
      the Step-6 `{log}` line does **not** write (lint-debt is not reset — the B10-12 mirror); the
      in-session YAML remains the owner's copy. (`vault-operating-contract.md:330` mandates persistence;
      fixes were already applied at Step 3 — an unrecorded run is *"silently rests on 5 of 6"* produced by
      the fix.)
    - *(A14 v)* **Ordering: build-3 → build-5 on `report.md`**; the validator's key set is read from
      `report.md` at build-3's commit.
    - *(A20, obsolescence)* `report.md:3`'s *"the module's release gate parses real persisted reports
      before the tag"* — `package-lint.py` has no such group — is re-pointed at the persist gate; A15-7
      direction 3 (declare the archive best-effort) dies as an option.
    - Brief-time question **reworded**: not *what is the population* but *which independent instrument
      produces each per-file population*.

- **build-6 — A15-12, retire the PARA `type:` prohibition.** `extraction.md:84` and `checks.md:19`
  case (b), **with the `{wiki}` carve-out retired in the same act** — not optional (D5).
  ⚠ **Carries Cycle 14 build-3 (6)'s live clauses (a) and (c)** — both `type:`/park #15 —
  `[ship-verifiable]`, **GATES closeout** (Q9). *(Clause (b) is park #16, A15-13's subject, and
  Cycle 14 recorded it "already satisfied in substance and not re-litigated" — so build-7 carries no
  gating debt.)* ⚠ **E2 attaches: read `_output/problem-solution-2026-08-25.md` BEFORE the brief is
  written**; gitignored, provenance only, contents never quoted.
  - `binds:` D5, Q9, E2
  - `spike:` `none`
  - `promise:` **After this ships, a vault owner who types a file accurately is no longer told to
    retype or move it — the declared `type:` is judged on whether it is honest rather than on which
    folder the file sits in, and `{wiki}` stops being a named exception to that.** *(Owner-ratified
    2026-09-02; framing from one candidate, coverage from another, grafted at ruling time.)*

    **The inversion the first clause names, grounded.** `extraction.md:84` gives a vault that
    **invents** a word a legal route (declare it in `{overlays}/extraction.overlay.md`) and gives a
    vault using **the module's own accurate word** none — *"never to declare module vocabulary as
    vault-grown overlay schema"*, so the only responses are retype it to something less true or move
    it. **Accuracy is penalized; invention is accommodated.**

    ⚠ **The final clause is load-bearing and was added for that reason.** Drafts naming only the
    prohibition would let a brief retire it, leave the `{wiki}` carve-out standing, and satisfy its
    own promise — the failure D5.2 and the filing both forbid: *"'four exceptions, zero categories'
    is `ST-2`'s measured failure mode … **A build that ships half of this has shipped pass five.**"*

    *(Deliberately NOT in the sentence: D5.1, `para_type_unknown` is not retired. "Judged on whether
    it is honest" implies a dishonest value still lands, and D5.1 binds through `binds:` — naming it
    would pad the promise without adding an obligation. Owner-ruled 2026-09-02.)*

  - **Roundtable amendments (2026-09-02):**
    - *(A1 — R1's first instance, 12 of 13 lanes)* **`handshake:` `extraction` 9 → 10; re-ack
      `vlt-extract`, `vlt-lint`, `vlt-track`, `vlt-query` in the same commit** (`extraction.md:11-12`;
      acks at each `SKILL.md:4`). Instrument: `package-lint` Group E, bipartite. The pin move is what
      invalidates the cache — correctly under D4 (see build-2 A2). Authors the v0.18.0
      `governance_rule_changes` CHANGELOG block (`vlt-upgrade/SKILL.md:122` renders from the CHANGELOG,
      never a diff; it is the line beside `parked_interims_review`). **Seven ideation rounds did not
      find this; twelve roundtable lanes did in an hour — R1 exists because nothing in the skeleton
      asked.**
    - *(A5)* **D5.2 names its object — see D5's amendment.** The **type-legality** carve-out retires:
      `extraction.md:84`'s closure, `checks.md:19` case (b), and `:84`'s *"`frontmatter.md`'s list does
      not answer here"* sentence. The Layer-2 **population / container** exclusion
      (`vault-operating-contract.md:64/:68/:70`, `checks.md:19`'s population clause, `:20`,
      `full-scale.md` step 1, `vlt-lint/SKILL.md` Step 0) is **NOT touched** — wiki pages remain outside
      every `para_*` net; build-6 records **why** it is a zone rule and not a type exception.
      `vault-operating-contract.md:66`: *closed* → *recognized* (a contract edit ⇒ rule-card
      re-derivation, `package-lint` C6). The filing's *"a subtree carries a `type:`"* mechanism is **not
      shipped and not in scope** — recorded so the filing's four-site count reads as three sites over.
    - *(A6)* **The recognized set after retirement is STATED:** PARA `project | area | resource | moc` ∪
      operational-record `charter | record | register` ∪ overlay-declared ∪ **the values named at
      `frontmatter.md:71`** (closed by enumeration at that line, open by edit); `para_type_unknown` (D5.1)
      fires only on a value in none; `frontmatter.md:71`'s PARA clause amended in the same act.
      **Consequence stated so the owner's experience is ruled, not discovered:** the 9 `type: research`
      files **stop firing on upgrade with no vault act**; park #15's unwind is a superseding decision-log
      entry citing v0.18.0. Without this, "retire the prohibition" leaves the legal response *declare
      `research` in the overlay* — the route park #15 refused on principle (`decision-log.md:1204`).
    - *(A6)* **Promise re-ratified** — nothing in the module judges *honesty*; after retirement the only
      judge is vocabulary membership: *"After this ships, a vault owner who types a file accurately is no
      longer told to retype or move it — the declared `type:` is judged on whether it is **recognized
      vocabulary, the module's or the vault's declared,** rather than on which folder the file sits in,
      and `{wiki}` stops being a named exception to that."*
    - *(A18, owner ruling D-D)* **Cycle 14 build-3 (6) is SPLIT IN PLACE.** The at-rest half — each
      park's recorded blocker claim is demonstrably **false** against shipped
      `extraction.md`/`write-verification.md` — is the `[ship-verifiable]` clause that **GATES**,
      appended to this roadmap's ledger by build-6's brief quoting Cycle 14's bound text verbatim (the
      b3(7) precedent — prose GATES markers sit on a wall no parser faces). The vault-act half (the
      superseding decision-log entries; the 9 files' response, now a no-op under A6) is
      `[field-contingent]`, triggered by the post-upgrade `parked_interims_review:` line. Clauses (a)+(c)
      ride here; **build-7 carries no gating clause** (Q9 resolved).
  - `binds:` **+= handshake (R1)**; Cycle 14 carry 6 released here by reason (see dispositions).

- **build-7 — A15-13, retire the `verified_by` roster closure.** `write-verification.md:47`'s
  closure only. **Separate from build-6 on the filing's own argument** — *"folding two retirements
  into one build is how a structural change becomes unreviewable"* — ratified by the owner
  2026-09-02. **No floor on unrostered attesters** (Q5).
  - `binds:` D5, Q5, Q9
  - `spike:` `none`
  - `promise:` **After this ships, a vault owner's attestation is authorized once — by the
    container's `writers:` list where one is declared — instead of twice, by a roster that cannot
    admit a partner.** *(Owner-ratified 2026-09-02.)*

    **It states D5.4 nearly verbatim** — authorization is *"answered **once**, by the net built to
    answer it, instead of twice"* — and Q5's ruling that the `writers:` join is the whole of it.

    ⚠ **"where one is declared" is a precision fix made at ruling time, not filler.** Q5 ruled **no
    floor**, and `checks.md:20` holds that *"If no ancestor declares, the posture is `open` and the
    file PASSES"* (D5.5, undisturbed). Without the qualifier the promise reads as though a `writers:`
    list adjudicates **every** case — it does not, and an acceptance check written against that would
    fail on the undeclared population the owner accepted knowingly at Q5.

    ⚠ **An over-claim rejected at ruling time, recorded so no brief re-inflates it:** a draft
    promising the vault *"stops seeing 27 files reported as unattested"* is **false at ship time**.
    The retirement makes attestation **possible**, not automatic; the 27 clear only when partners
    actually re-attest. **A check graded on the count dropping to zero on release would fail
    honestly.** The promise is capability, never a cleared backlog.

    *(Not in the sentence, and binding anyway through `binds: D5`: D5.3, the attestation pair is not
    retired — "whether an attester may attest" presupposes attestation continues.)*

  - **Roundtable amendments (2026-09-02):**
    - *(A1 — R1's second instance)* **`handshake:` `write-verification` 5 → 6; re-ack `vlt-ingest`,
      `vlt-extract`, `vlt-research`, `vlt-lint`, and `vlt-lint-full.js` — the header `:11` AND the body
      pins `:178`, `:182`, `:229`, `:684`** (`package-lint` E7 fails the tag on a stale body pin). ⚠ **A
      workflow-asset edit in a build that otherwise never touches the workflow**, and the `:229` edit
      moves `scanFingerprint` — correct, the scanner reads that convention (build-2 A2). File-edit order
      across the cycle: **2 → 3 → 4 → 6 → 7**. **Field notice (CHANGELOG):** vaults with
      `local_consumers:` registrants on write-verification (the field vault's `vlt-brief` acks `@5`) see
      one expected `convention_drift` finding until the registrant is reconciled by ceremony — the module
      cannot re-ack a vault-minted op.
    - *(A7)* **`:47`'s value set is RESTATED, never deleted** — `frontmatter.md:78`/`:82` point at it
      (*"not restated here"*) and would dangle: *"whatever the nearest declaring container's `writers:`
      join admits; unconstrained where none declares."* The two `:47` clauses that **survive verbatim**:
      *lint attests narrowly*; *a skill added to `consumers:` for handshake reasons alone acquires no
      attestation authority*. Prose re-nouns, **no `frontmatter` bump** (stated so a briefer does not
      pick `frontmatter@15` + ten re-acks): `frontmatter.md:78` (*the attesting **op***), `:82` (*the
      operation that ran tier-1* → *the attester — an op, or a partner*), `:296(c)` (restates the
      write-op ceiling — becomes a version-free pointer; `local_consumers:` keeps its handshake role,
      `checks.md:40`, and loses its attestation-widening one — said so). One sentence at
      `write-verification.md` §Attestation for the **non-op attester**: a partner attesting a knowledge
      artifact it wrote runs the tier-1 checklist and writes its own slug — today every attestation
      instruction is addressed to an op (`grep` over `vlt-dispatch`, `vlt-mint`, `vlt-agent-*` for
      tier-1/attest: nothing).
    - *(A7)* **Promise subject corrected:** the 27 files are partner-written and only the partner can
      re-attest them — *"After this ships, a **partner's** attestation is authorized once — by the
      container's `writers:` list where one is declared — instead of twice, by a roster that cannot admit
      a partner."*
    - *(owner ruling D-E)* **Scope += the one-line `checks.md:20` change: the `verified_by:` identity must
      itself be admitted by the nearest declaring `writers:` list — never carried by the `author:` leg.**
      As shipped the join admits on **any** match (`hybrid → human`), so `verified_by: banana` would pass
      wherever `writers:` names `human`; the roster was that value's ceiling and Q5 removed it accepting
      only the *undeclared* population knowingly. This is D5.4 (*answered once, by the net*) made true.
      Undeclared containers still pass `open`.
    - *(A8)* **D2 extends here with one denominated line:** `para_writer_unauthorized: N judged; D under a
      declaring ancestor; O passed on open posture` — the value stays legal, the population Q5 accepted
      becomes visible (`report.md:39` renders violations only; the `open` PASS population is counted
      nowhere today).
    - *(A20, obsolescence — reverse)* `checks.md:20`'s `verified_by:` → partner-slug leg becomes
      exercisable for the first time — the contradiction is **eliminated**, no precedence statement
      needed (Arc 9 D5). `write-verification.md:55`'s *"fusing permission to provenance"* sentence
      survives and now reads true. Contract `:68` already reads a partner slug — nothing to do.
  - `binds:` **Q9 → `Q9 (no gating clause — see build-6)`; += handshake (R1)**.

⚠ **A15-4 spans build-2 and build-4** (eviction half / fidelity half — D3 half-took the filing).
**Both `binds:` rosters name it deliberately**: a brief scoping one half from the filing alone would
cover half the ask and still read as compliant. This is the `CLAUDE.md` *lists that claim
completeness drift* hazard in its per-filing form.

*(roundtable A12, G-F4 — the note above is corrected: rosters carry ruling **ids**, and no id in
build-4's roster resolved to A15-4; **both builds now bind D3**, the ruling that halves the filing.
And under D-C the "fidelity half" is no longer an audit of the scanner's return but its replacement —
the split survives, the mechanism changed.)*

⚠ **Roundtable material, carried from the capture and not resolved here:** A15-15's timing argument —
the two filings that exercise the never-exercised obsolescence beat are **mis-classified on the
tracker right now**. Capture endorsed it as *a real ordering constraint rather than advocacy*, which
makes it a joint under `roadmap-roundtable`'s frame.

**→ RESOLVED at the roundtable (2026-09-02, A9):** the timing argument does **not** hold as a build-order
constraint — the beat is the roundtable itself, which precedes every build, and one release erases
order. It holds as an **owner act**: re-kind #17/#18 (body `kind:` + label) after build-1 lands;
build-1's acceptance checks it.

### Pre-ideation rulings the capture demanded

Seeded unanswered. Each is a question the capture flagged and declined.

- **Q1 — A15-11 re-admission. RULED, Round 2 (2026-09-01): RE-ADMITTED. Cycle scope is all 15 —
  A15-1..A15-15.** Cycle 14's roundtable A27 deferred A15-11 as net-new capability; Cycle 14 named
  the condition under which it stops being net-new; the capture recorded that the condition has
  arrived and declined to act. The owner overturns the deferral.

  ⚠ **Recorded with the re-admission — A15-11 is not a peer of the read-back filings, it is
  UPSTREAM of them.** Cycle 14's capture
  (`factory/cycles/14-no-enforcement-point/roadmap.md:117-127`): *"**Any resolution that gives the
  reduce ground truth needs a payload route, and #13 is that route.** If ideation takes the posture,
  #13 stops being net-new and becomes a dependency."* Round 1's grounding correction proved the
  premise Cycle 14 was predicting against: the reduce **cannot** reach ground truth on its own. See
  the ordering ruling below.

- **Q2 — A15-11 direction 2. RULED, Round 2 (2026-09-01): DIRECTION 1 ONLY. Direction 2
  (`argsPath`) is DECLINED — it is not the module's to build and not the factory's to request.**

  **Direction 1 is the whole repair, not the lesser half.** Documenting the wrapper-script route in
  `full-scale.md` step 3 invokes by `scriptPath` with the payload embedded, so the ~84KB never
  enters the caller's context **and resume does not re-send it** — the entire measured cost, on both
  legs. It *"works today with no module change — it is undocumented, not unavailable."*

  **Why direction 2 is declined, grounded.** `argsPath` would be a parameter of the **Claude Code
  harness's `Workflow` tool** — a different upstream from this repo's known one (`CLAUDE.md`
  §*What not to touch* routes `bmad-*` defects to BMAD-METHOD; this is not that). Read against the
  runtime's own parameter contract this session, `Workflow` accepts `args`, `name`, `script`,
  `scriptPath`, `resumeFromRunId`, `title`, `description` — **no `argsPath` and no file-valued
  alternative to `args`**, which is specified as *"exposed to the script as the global `args`,
  verbatim"*, inline by construction. The factory cannot build it, and **the lifecycle has no
  factory→harness rail** to request it (the feedback rail runs vault→factory).
  ⚠ **Confidence limit, stated rather than buried:** that is one session's read of one invocation
  surface, not an exhaustive read of the harness. It is sufficient to decline a build; it is not a
  closed spike, and **no spike is owed** because nothing in this cycle's scope depends on the
  answer.

  **Also settled here (capture's ⚠, so it is not re-briefed as a gap):** A15-11's second observation
  — that the no-args refusal *"reads as a broken asset"* and needs a pointer to the SKILL route — is
  **already satisfied** at `vlt-lint-full.js:127`, whose second sentence names the SKILL and what it
  does. Residual scope there is **at most a wording nudge**, and briefs must say so rather than
  scope a missing pointer.

- **Q2b — ORDERING. RULED, Round 2 (2026-09-01): HARD CONSTRAINT.** Any build taking the
  A15-1 / A15-3 / A15-4 read-back is ordered **after** A15-11's build. **Grouping may not invert
  it**, and both builds carry it in their `binds:` rosters so `build-brief` reads it. *(This is the
  joint Cycle 14 predicted and Round 1's boundary correction confirmed: a script-side read-back
  needs the payload route first.)*
- **Q3 — A15-9. RULED, Round 4 (2026-09-01): BOTH DIRECTIONS, ordered d2 → d1. The precondition is
  RULED ANSWERED from source, not deferred.**

  **The frame the ruling was made under:** today the cache cannot survive **any** upgrade.
  `full-scale.md` step 2 names four ruleset slots and states *"Any of those moving invalidates every
  record"*; the first is `module_version`, and every release moves it. Since **the only sweep an
  acceptance check ever forces is a post-release sweep**, the instrument is invalidated by
  construction at the exact moment it is mandatory. Measured floor, from the live report's own
  `cost_accounting`: `files_cached: 0`, 146 scan agents, 591,152 prompt chars — against a 96%
  saving on the scan phase when the cache does hit.

  - **Direction 2 (first) — survive an upgrade that did not touch the lint surface.** Replace the
    `module_version` proxy with digests of what it actually stands for: `vlt-lint/SKILL.md`,
    `references/full-scale.md`, and the reduce. Grounding sustains that the slot is **not
    pointless** — it uniquely catches a lint-surface change that moves no pin and no digest — so it
    is **replaced by a precise instrument, never deleted**.
  - **Direction 1 (after) — survive a convention change the page scanner never reads.** Narrow
    `convention_digests` from *"one entry per convention this run judges against"* to the three
    `pageScanPrompt` actually reads (`vlt-lint-full.js:229-230`): `frontmatter`, `wiki-supersession`,
    `write-verification`.

  **The precondition, answered — this is the ruling, and briefs cite it rather than re-deriving
  it.** A cached **page-scan record** depends on: **the page's own bytes**, **the three conventions
  the scanner reads** (`:228`), and **the scan prompt + `PAGE_SCAN` schema** (already caught
  independently by `scanFingerprint`, `vlt-lint-full.js:232-233`). It does **not** depend on
  `extraction`, on `checks_digest`, or on `module_version` as such. The filing's worked instance
  stands verified: *a build bumping only `extraction` cannot change a cached page-scan record, yet
  would invalidate all 146 — twice over.*

  ⚠ **D4 is satisfied by construction and briefs must show it, not assert it.** Neither direction
  weakens invalidation on judgment; both **narrow the key to real dependencies**. An upgrade that
  *does* move the lint surface still invalidates, correctly.

  **Direction 3** (bind checks to the population they judge) is free and already being applied —
  it is Q4's subject and routes to the platform ledger.

  **→ EXTENDED at the roundtable (2026-09-02, A3; owner ruling D-B over a three-way split).** Six lanes
  found the ruling repaired two of the key's four terms and left `pin_vector` and `checks_digest` in
  place though its own dependency sentence says neither is a dependency — so *"a build bumping only
  `extraction` would invalidate all 146"* stayed **true** via the pin slot, and build-6 is exactly such a
  bump. **Ruled: the per-page key is facts-not-verdicts** — page bytes | scan prompt + `PAGE_SCAN`
  (`scanFingerprint`, already shipped) | **`scanModel`** (the extractor identity — `vlt-lint-full.js:122`,
  today in **no** key term, so a model change or caller override would reuse haiku facts under a
  different extractor forever; the exact "future model change" D3 direction 1 was chosen to survive) |
  the three scanner-read convention digests (base+overlay). **`module_version` is deleted, not replaced
  by digests of `SKILL.md`/`full-scale.md`/the reduce** — the cache stores *extracted facts, never
  verdicts* (`full-scale.md` step 5) and the reduce re-runs over cached facts every sweep, so a reduce or
  prose change is fully exercised without a cold sweep; digesting `full-scale.md` would make every
  operator-prose clarification a 146-agent sweep, the over-breadth A15-9 filed. Q3's *"replaced by a
  precise instrument, never deleted"* is honoured: the precise instrument for the scan surface is
  `scanFingerprint`. **`checks_digest` leaves the page-scan key; `pin_vector` narrows to the three
  scanner-read pins or drops as redundant with their digests** (a version bump changes the bytes the
  digest already covers) — the brief shows D4 per slot. *Dissent on record: Amelia/Quinn held the
  whole-file digest as the conservative D4 reading; conceded on facts-not-verdicts.* The brief-time
  question "whole file or only the reduce" **dissolves**.

- **Q4 — A15-9's companion finding. RULED, Round 4 (2026-09-01): ROUTED TO THE PLATFORM LEDGER.**
  It is brief-time check anatomy — factory-side by the channel boundary — and the filing itself
  calls it *"a brief-time discipline gap, not a module defect."* The channel has room:
  `factory/platform/roadmap.md:55` reads **WIP 0/2** (seven items BUILT-awaiting, consuming no
  slot).

  **The item, as ruled:** Cycle 14 bound three acceptance checks to a full sweep whose population
  they do not judge (`checks.md:19` places the `para_*` nets in **both** modes; the fan-out sweeps
  `{wiki}` only and the `para_*` slots are SKILL-filled at `vlt-lint-full.js:812-814`), so a
  **scoped** run was what each needed. Build-6's two were corrected at brief time 2026-09-01; the
  other two are historical and annotated, not re-graded.

  ⚠ **The capture's reason for NOT routing is overruled deliberately, and its cost is mitigated
  rather than dismissed:** the filing kept both halves of the cost problem in one place on purpose
  (*how often* a cold sweep is forced, factory-side; *what one costs*, module-side). **A15-9's
  roadmap entry keeps a pointer to the platform item** so the two halves stay findable together.
  ✅ **DISCHARGED 2026-09-02 — opened as [P-23]** (*a check names the population it judges, not the
  run that will produce it*) on `factory/platform/roadmap.md`, **queued**, with the pointer pair
  written in both directions: A15-9's entry forward to P-23, P-23's provenance note back to A15-9.
  The cross-link discipline is satisfied — a one-way route is the failure P-11/P-21 were written
  about.
- **Q5 — A15-13's residual (ODQ 2). RULED, Round 3 (2026-09-01): NO FLOOR. The container `writers:`
  join is the whole of it — the vault's read, adopted.** Legal `verified_by:` values are whatever
  that join admits; nothing further is required of an unrostered attester.

  **The reasoning on record.** Where a charter declares, the human already holds the gate —
  `checks.md:20`: *"Never auto-fixed — `writers:` is human-gated, so a partner may propose the
  charter edit and may not make it."* Where none declares, `checks.md:20` already rules *"If no
  ancestor declares, the posture is `open` and the file PASSES — never a finding"* (verified verbatim
  in source this session, and preserved by D5).

  ⚠ **Accepted knowingly:** in an **undeclared** container, `verified_by:` is then checked by no net
  at all — `para_missing_attestation` requires only that the pair exist, and
  `para_writer_unauthorized` passes on the `open` posture. A floor is the only thing that would
  close that, and it is ruled unnecessary. *(`ST-6` was read before ruling, per the capture's ask;
  its bad-fix prediction — re-widening by naming more actors — is avoided here by adding no
  enumeration at all.)*
- **Q6 — A15-15's split (ODQ 5). RULED, Round 4 (2026-09-01): NO SPLIT — ONE ACT, on the cycle
  build.** All five sites land together:
  1. `skills/vlt-feedback/references/field-contract.md` — the `kind` row's value set **and** a
     `field:supersession` row in the label table *(shipped)*
  2. `skills/vlt-feedback/` — the composer emits the new value *(shipped)*
  3. the tracker's label set — a `field:supersession` label *(shipped, defined in the contract)*
  4. `.github/ISSUE_TEMPLATE/` — **a fourth form** *(factory-side, rides along)*
  5. `.claude/skills/issue-triage/` — the classification check's value set *(factory-side, rides
     along)*

  **Grounded:** there is **no shared dropdown to widen** — `field-candidate.yml:7` hard-codes
  `labels: ["vault-filed", "field:candidate"]` and its `kind` dropdown is a single-option list. The
  change is **additive-only**, so it lands **without a `rail_contract` bump and without invalidating
  a single filed issue** (`field-contract.md` §Contract version).

  ⚠ **The reason a split was refused:** a vocabulary that ships three-fifths is a vocabulary the
  transport cannot carry — the exact defect A15-15 reports. And the timing argument the capture
  endorsed as *a real ordering constraint rather than advocacy* applies now: the two filings that
  will exercise the obsolescence beat (A15-12, A15-13) are **mis-classified on the tracker right
  now**. This remains **roundtable material** as a joint bearing on build order.
- **Q7 — A15-3's remaining half (ODQ 1). RULED, Round 5 (2026-09-01): DECLINED. No anchor-existence
  check this cycle, and A15-3 carries no build of its own — it FOLDS into the scanner-return
  build** with A15-1 and A15-4 (the verbatim-extraction instruction at `vlt-lint-full.js:229-230`).

  ⚠ **Recorded so no later cycle re-files a shipped fix:** A15-3's own proposed direction (*drop an
  empty normalization result*) **is already in the tree** — `vlt-lint-full.js:420-423`, shipped as
  **B5-3**, whose comment names this exact case (*"e.g. a bare `[[#anchor]]`"*) and whose
  `.filter(Boolean)` drops it. The reported value was `'early loading phase (~ days 3-7)'`, a
  **non-empty** string, which is what relocated the defect to the scanner. Briefing the filing's ask
  would have been a **graded no-op**.

- **Q8 — A15-2's split (ODQ 4). RULED, Round 5 (2026-09-01): TOGETHER, one build.** The prose repair
  (specify stub discovery precisely in `full-scale.md` step 1 — recall **no regex ships anywhere in
  `skills/`**, only a sentence and a reader) ships **with** the denominated-empty half (*"0 slugs
  found under `## Stubs…` across 1 index"*). Shipping the prose alone would leave a failed parse
  indistinguishable from a vault with no stubs — the exact observable the filing reports.
  **→ AMENDED at the roundtable (2026-09-02, A17):** *"reconcile against `checks.md:39`"* would have
  produced a **third** copy of a heading that has one home. Discovery matches the heading **as
  `{conventions}/wiki-index.md:83` states it** (overlay-merged); `full-scale.md:7`, `checks.md:39`,
  `vlt-lint-full.js:44`/`:476` become pointers. The bare `## Stubs` form retires (obsolescence, build-3).

- **Q9 — the two bound Cycle 14 debts. RULED, Round 3 (2026-09-01): each debt rides its
  subject-matter build.** Both are `[ship-verifiable]` and both **GATE closeout**.
  - **Cycle 14 build-3 (6)** — the two parks' unwind — **rides the A15-12 / A15-13 build(s)**. The
    parks are what those retirements release; Cycle 14 closed on this as its one honest gating FAIL,
    *a green being available only by falsifying a `type:` field*.
  - **Cycle 14 build-1 (6)** — `malformed_frontmatter`, **E4 at 10/8/2, not zero** — **rides
    A15-5's build**, which is a fresh measurement on the same check.

  ⚠ **Consequence for Grouping:** whichever builds carry A15-12/A15-13 and A15-5 inherit a
  closeout-gating obligation, and their `binds:` rosters must name it. A cycle cannot close on these
  being re-carried — that is the point of the bound.

  **→ RESOLVED and SPLIT at the roundtable (2026-09-02, A18; owner ruling D-D):** build-6 carries Cycle
  14 build-3 (6) clauses (a)+(c); **build-7 carries no gating clause** (clause (b) was ruled satisfied in
  substance by Cycle 14). The debt is **split in place**: the at-rest half — each park's recorded blocker
  claim is false against shipped rules — is the `[ship-verifiable]` clause that GATES; the vault-act
  half (the superseding decision-log entries) is `[field-contingent]`, triggered by the post-upgrade
  `parked_interims_review:` line. Cycle 14 build-1 (6) leg 3 rides build-4 with an **at-rest leg** (D-A).
  ⚠ **Both debts are appended to THIS roadmap's ledger by the carrying briefs** as `[ship-verifiable]`
  sub-clauses quoting Cycle 14's bound text verbatim — `acceptance-discharge` and `cycle-closeout` read
  only this roadmap's `- [ ]` items, and Cycle 14's is CLOSED; "GATES" in prose is a wall no parser
  faces. Every bare `E4` in this section reads *Cycle 14's E4* — this roadmap's E-namespace ends at E3.

### Cross-filing decide-once rulings

Decisions that resolve the same question across filings identically. Seeded from the capture's
through-line; **the capture proposes none of these as answered.**

- **D1 — does `ST-7` bind a build? RULED, Round 1 (2026-09-01) — split into two axes, because the
  question as seeded conflated them.**

  **D1(a) — scope authority: `ST-7` DOES NOT BIND. Citable only.** Each brief is discharged by its
  own filing's ask; the study gates nothing, which is the study register's own default
  (`factory/studies/README.md:102-108`). A brief may cite it, argue with it, or ignore it with
  reasons. Concretely: A15-6's brief is done when the `governance_memory` denominator counts 59
  instead of 47 — it is **not** additionally obliged to make the slot arrive denominated, and
  `ST-7`'s rejected alternatives (notably *"tighten the prose"*) are **not** binding on briefers.

  ⚠ **The cost is on record and was accepted knowingly** — `ST-7`'s own words on this route:
  *"Prose precision has no ratchet — one careless sentence added later reopens the gap, and nothing
  will report it."*

  **D1(b) — mechanism: FOLDED INTO GROUPING, no separate ruling.** With D1(a) unbound there is no
  scope authority left for D1(b) to carry, so **no shared read-back instrument and no per-consumer
  grouping is imposed**. How the nine instances group is settled at *Grouping & order* on the
  ordinary grounds of order, size, and the boundary cost recorded immediately below.
  **→ AMENDED at the roundtable (2026-09-02, A15):** the A15-6 illustration above is **struck** — it
  contradicts D2, ruled four rounds later for the same slot, and `build-brief` reads rulings by id.
  D1(a)'s illustration is now **A15-7** (parseability), whose ask has no D2 overlap: *a brief is done
  when the persisted report loads; it is not obliged by `ST-7` to do more.* D1(a)'s principle is
  unchanged.

- **D2 — the denominated-slot posture. RULED, Round 5 (2026-09-01): ADOPTED for A15-2, A15-6 and
  A15-10. All three derived slots arrive denominated.**
  - **`stubSlugs`** — report the population, not just the list: *"N slugs found under `## Stubs…`
    across 1 index."* (Rides Q8's single build.)
  - **`pin_vector` / `convention_digests`** — stop discarding the distinction the workflow already
    computes. `rulesetSlotsMissing` (`vlt-lint-full.js:263`) **already exists** and already degrades
    loudly with a named cap; it reports **"missing"** where the truth is **"present but of the wrong
    type"**. A15-10's entry prices this exactly: *"the workflow can tell them apart (`typeof v ===
    'string'` already distinguishes them — it simply discards the distinction)"* — available *"for
    the cost of not throwing information away."*
  - **`governance_memory`** — the denominator renders with its population.

  ⚠ **This is the ONLY read-back posture entering Cycle 15**, and it was ruled knowingly on that
  basis: D1(a) already ruled `ST-7` non-binding, so nothing else in the cycle obliges a consumer to
  compare a value against what specified it. The posture reaches these three slots and no further.

  *(The capture noted the posture also applies to A15-11 direction 1 — a wrapper-script recipe
  stated in prose is one more derivation nobody reads back. **Not extended there**: Q2 ruled
  direction 1 as a documentation edit, and D1(a) imposes no obligation on it.)*
  **→ REWRITTEN at the roundtable in five moves (2026-09-02, A14).** (i) The ⚠ above is **false as
  worded** — three lanes counted: builds 4 and 5 carry read-backs through their own filings' asks, E1
  reaches an output-side site, and counted against `ST-7` §What would close it **the cycle reaches all
  four consumers**. It reads: *"D2 is the only read-back imposed by **cross-filing ruling**; builds 4 and
  5 carry read-backs through their own filings' asks; extended once by E1 to an output-side site."*
  Round 5's summary line reads *"the only input-side read-back by cross-filing ruling."* (ii) The
  `pin_vector`/`convention_digests` bullet is a property of the **`RULESET_SLOTS` loop** — *a slot
  present but of the wrong type or shape is reported as wrong, never as missing, for every slot the loop
  iterates* — so build-2's new slot (`scanModel`) inherits it. (iii) A present-but-wrong-type ruleset
  slot is a **pre-dispatch refusal** with a directed `next:` (the failed-run posture), **never a
  cold-branch cap** — a wrong type is the SKILL's own rendering error, detectable before the first agent
  dispatches; as ruled the owner would still have paid 146 agents and read "wrong type" afterwards.
  (iv) **The denominator is produced by an instrument independent of the one that produced the value**
  — `governance_memory`: form-agnostic `## ` heading count vs schema-matched entries (a 47-of-47 from
  the same matcher reads back nothing — A15-6 reproduced inside its fix); `stubSlugs`: `section located:
  yes|no` beside the count. (v) The homes: `report.md` gains a fourth `lint_cache:` cold reason, a
  `stub_discovery:` line, and a `governance_memory:` population term (build-3's scope; merge order
  3 → 5). Extends to build-7 with one line (A8).

- **D3 — the cache-freezes-errors consequence. RULED, Round 5 (2026-09-01): A15-4 direction 2 is
  HALF-TAKEN — the invalidation path is IN, record provenance is DEFERRED.**

  **In scope:** `skills/vlt-lint/scripts/lint-cache.py` gains an **eviction path**. Grounded: the
  script exposes exactly two subcommands, **`read` and `write`** — no purge, no per-page
  invalidation, no force-refresh. So today the only remedies for a poisoned record are **ship a
  release** (move the fingerprint) or **hand-delete the sidecar**, which discards all 146 records and
  forfeits the 96% the cache exists to deliver. There is no proportionate remedy at all, and there
  is a **live poisoned record in the field right now** (`cornerboxes` for `cornerbacks`, re-firing on
  a sweep that dispatched **1 agent against 146 pages**).

  **Deferred, and recorded as half-taken so the remainder is not silently dropped:** per-record
  **provenance** (which run / which model call produced a record). It is a data-model change to the
  sidecar and **no filing in this batch establishes what it should carry**; a brief taking it would
  price an unspecified design question as scope.

  ⚠ **What this does NOT do, stated so no brief over-claims:** Q3's d2/d1 change *when* the cache
  invalidates; the eviction path changes *whether a wrong record can be removed on purpose*; the
  scanner-return read-back (if scoped) would stop *new* poisoning at derivation time. Three distinct
  things. **Direction 1 does not cure records already poisoned** — the capture says so, and it is why
  this half was taken.

  ⚠ **Direction 3 stays refused, and briefs may not re-litigate it without new evidence:** moving the
  scan phase off haiku is not the fix — *"direction 1 makes the substitution harmless regardless of
  which model made it, which is the more robust fix and the one that survives a future model
  change."* The filing named it to be refused and grounding agreed.
- **D4 — the invalidation constraint, carried verbatim as a constraint on every repair (not a
  question, an inherited bound the owner may only widen deliberately):** *"**Not a direction:
  weakening invalidation on judgment.** A record reused under a moved rule is a false clean, which
  is worse than an expensive sweep. Any repair must show the reused facts are **independent** of
  what moved, not merely unlikely to be affected."* **RULED, Round 4 (2026-09-01): STANDS — inherited bound, unchanged.** *(Stamped at the roundtable, A19 — the scaffold's placeholder had survived under the "every slot is ruled" header.)*
- **D5 — the two retirements' non-negotiable halves. RULED, Round 3 (2026-09-01): ALL FIVE ADOPTED,
  binding on both briefs. No brief may narrow any of them.**
  1. **`para_type_unknown` is NOT retired** (A15-12) — a genuinely undeclared value at a PARA
     address must still land loud. *"Retiring a prohibition is not retiring its enforcement."*
  2. **The `{wiki}` carve-out retires in the SAME ACT** (A15-12) — *"This half is not optional …
     **A build that ships half of this has shipped pass five.**"*
  3. **The attestation pair is NOT retired** (A15-13) — `verified_by:`/`verified_at:` stay required
     on Layer-3 knowledge artifacts and `para_missing_attestation` keeps its job. *"Retiring a
     restriction is not retiring the field."*
  4. **Authorization is NOT dropped** (A15-13) — it is *"answered **once**, by the net built to
     answer it, instead of twice."*
  5. **The no-ancestor `open` + PASS default is NOT disturbed** (A15-13) — verified verbatim at
     `checks.md:20` this session. *(This is also the premise Q5's ruling rests on.)*

  **→ D5.2 NAMES ITS OBJECT (roundtable 2026-09-02, A5 — eight lanes found "the `{wiki}` carve-out"
  names two or three different rules).** The **type-legality** carve-out retires (`extraction.md:84`,
  `checks.md:19` case (b), `:84`'s *"does not answer here"* sentence). The Layer-2 **population /
  container** exclusion — `vault-operating-contract.md:64` (*"this is the sentence other sites point
  at"*), `:68`, `:70`, `checks.md:19`'s population clause, `:20`, `full-scale.md` step 1,
  `vlt-lint/SKILL.md` Step 0 — is **not touched**: wiki pages stay outside every `para_*` net (the
  Librarian-only zone is a write-boundary fact, not a vocabulary fact; retiring it drops 146 pages into
  four nets and double-covers `unattested_write`, the duplicate `checks.md:15(a)` was written to remove).
  D5.2's *"four exceptions, zero categories"* is satisfied by reading (a): the exception retires **from
  the type judgment**; the population statement is a category (Layer 2 zone), not a name. Reading (b) —
  a shipped subtree-`type:` declaration — exists in no artifact and is a mechanism-first item for a later
  filing. Contract `:66` *closed* → *recognized*. D5.1's kept net needs a set to judge against — **A6
  states it** (build-6).

### Round 1 grounding correction — the reduce cannot perform its own read-back

*(Recorded here so no brief re-inherits the wrong premise; both upstream sites were amended in the
same session on the owner's ruling.)*

A15-1's captured entry and `ST-7` **both** asserted that comparing a scanner's returned links
against the page's bytes is *mechanically available* because *the reduce already has the path*.
**It holds the path and cannot open it.** `skills/vlt-setup/assets/workflows/vlt-lint-full.js` has
**no filesystem access** — stated three times in its own arg contract (`:37`, `:64`, `:476`), and
`grep` over all 882 lines finds no `require`, no `import`, no `fs.`.

**Consequence for grouping and for every brief that touches surface 2:** the read-back for A15-1 /
A15-3 / A15-4 either **moves SKILL-side** or requires the SKILL to **pass new inputs** across that
boundary, as it already does for `crossLayerSlugs`, `stubSlugs` and `pageHashes`. It is the **most
expensive** of the four consumers' read-backs, not the cheapest — the largest cost difference among
this cycle's nine `ST-7` instances.

**The sites, as grounded Round 1** *(a map for Grouping, not a grouping ruling)*:

| Site | Instances | What the repair actually is |
|---|---|---|
| workflow **intake** — `vlt-lint-full.js:108`, `:262-271` | A15-2, A15-10 | Same file, adjacent region. `rulesetSlotsMissing` (`:263`) **already exists** and already degrades loudly with a named cap — A15-10's defect is that a `pin_vector` passed as a JSON array trips `typeof v !== 'string'` and reports **"missing"** where the truth is **"wrong type"**. `stubSlugs` (`:108`) silently coerces a failed parse to `[]`. |
| the **SKILL/script boundary** | A15-1, A15-3, A15-4 | New plumbing — see the correction above. |
| **SKILL** composition — `report.md:91` | A15-6 | *"You compose both lines yourself."* No counter ships. |
| **persist** step | A15-7, A15-8 | Rendered report against `report.md`'s slot spec. |
| **scanner prompt** | A15-5 | Measure the parsed scalar, not the raw YAML line — a prompt edit. |

⚠ **Clerk's note on the scope of the amendment.** The owner ruled *correct both* (the roadmap entry
and `ST-7`). The same false premise appears **twice** in `ST-7` — §Surface 2 (d) as well as §What
would close it — and the clerk corrected **both occurrences**, plus added a §Corrections section to
the study, on the reading that leaving one standing would defeat the ruling. Flagged rather than
assumed.

### Spikes

**The register is the record; this section is its view.** Mechanics — ids, statuses, frontmatter,
the gates — are single-homed at `factory/platform/spikes/README.md`. An owner ruling here is written
back to the register file in the same session; status and `verdict:` live there, never only in
roadmap prose.

**RULED 2026-09-02: Cycle 15 opens NO spike and consumes NONE. All seven builds carry
`spike: none`.**

- **Open register entries (`proposed` or `running`): none.** The register holds three files, all past
  `running` — `S-1` (`consumed`), `S-2` (`consumed`), `S-3` (`harvested`). No stub was opened during
  capture (capture narrative 10). **No register file is edited by this session.**
- **`S-3` (`github-notification-semantics`) — harvested, verdict `reshape`, `consumed_by: []`,
  in hand since 2026-08-24 and carried by Cycle 11. RULED: no Cycle 15 build consumes it.** Its
  question is **notification and permission semantics** (does a repository watch notify a maintainer
  on issues they have not participated in; is there a filer-grantable *"please look"* mechanism) —
  an adjacent surface to build-1's rail work but **a different question**. Named here so **build-1's
  brief meets it rather than rediscovering it at brief time**, which is what this section is for.
  ⚠ **It is now unconsumed into a third cycle** — recorded as a deliberate decision, not drift.
- **A15-11 direction 2 (`argsPath`) was NOT registered as a spike** and none is owed: Q2 declined it
  as a Claude Code **harness** parameter the module cannot build and the lifecycle has no rail to
  request. The confidence limit on that read is stated at Q2.

### Evidence-debt dispositions

Per build: attached, or ruled not-blocking.

- **E1 — A15-8's scope. RULED, Round 6 resumed (2026-09-02).**

  **Two grounding corrections were established before the pause; both stand and briefs inherit
  them.**

  **(i) The "gating blocker" A15-8's entry describes was CLEARED the same day.** A15-8 says Cycle 14
  build-3 (7) *"was graded **BLOCKED (unreachable)**, and it is `[ship-verifiable]` and **GATES** —
  so Cycle 14 gained a gating blocker from a report-shape defect."* True as history, **not as a live
  obligation**: `factory/cycles/14-no-enforcement-point/roadmap.md:2820` records **⚠ RE-GRADED
  2026-08-31 — DISCHARGED WITH A CAVEAT ON RECORD. OWNER-RULED** — *"The gating blocker is cleared;
  the defect is not."* That is why it appears in **none** of Cycle 14's seventeen carry-forwards and
  why Cycle 15 inherits **two** bound debts, not three. *(It cuts FOR A15-8: the owner accepted the
  substantive answer and recorded that the defect stands unrepaired.)*

  **(ii) A type-only validator does NOT catch the failure that cost the blocker.** `report.md:32`
  mandates `para_missing_attestation: [<para-file: …>, ...]` — a list of **per-file** entries. What
  the sweep rendered was **one string standing in for 27 files**, which is *still a list of
  strings*: **type-valid**. So A15-8's direction 1 as written (*parse it back and assert the mandated
  top-level keys are present and of their mandated type*) **passes the rollup cleanly** and catches
  only instances (b) and (c), the dropped keys. Catching instance (a) needs a **cardinality** check —
  the slot's entry count against the population it reports on — which is a **denominated read-back**,
  the same posture D2 adopted, and meaningfully more than "check the keys."

  **The `type:` distribution is mandated NOWHERE** — `grep -rn "distribution" skills/vlt-lint/`
  returns **zero**, and `vlt-lint-full.js:812-814` returns the slot empty, commenting it is *"a
  structural slot the SKILL fills."* Adding it would mean inventing a spec to retro-satisfy a check
  already re-graded DISCHARGED.

  **RULED, Round 6 resumed (2026-09-02): VALIDATION + CARDINALITY. The `type:` distribution is
  OUT.**
  - **Direction 1, as filed** — at persist, parse the report back and assert `report.md`'s mandated
    top-level keys are present and of their mandated type, failing loudly. **Composes with A15-7's
    parse requirement rather than duplicating it.**
  - **Plus the cardinality check** — a slot `report.md` mandates **per-file** must render per-file,
    verified by the slot's **entry count against the population it reports on**. This is what
    catches instance (a); correction (ii) proves direction 1 alone does not.
  - **Out:** a `type:` distribution. Mandated nowhere, and the check that wanted it is already
    DISCHARGED — writing a spec to retro-satisfy it is backwards.

  ⚠ **The cost, named rather than discovered at brief time:** cardinality is a **denominated
  read-back**, not a key check. It is the same posture D2 adopted for the three input slots, now
  reaching an **output** slot — so Cycle 15 ships the denomination posture at four sites, not three.
  This is the one place the cycle's read-back reaches beyond D2's list, and it arrives through
  A15-8's own filing rather than through `ST-7`, which D1(a) ruled non-binding.

  **→ MADE BUILDABLE at the roundtable (2026-09-02, A16 — six lanes).** As ruled the validator had **no
  machine-readable slot list** (`report.md:9-79` is a template with placeholders — a hand-typed key list
  in the validator is a second statement of the shape, the A14-8 defect) and **no denominator**
  (`report.md` carries no `para_*` population count; `attestation_census.pages_total` is the *wiki*
  population). Ruled: (1) one artifact is the key/type/cardinality source — parsed from `report.md`'s
  fence, or a schema file `report.md` points at; (2) presence + type + cardinality, **never closure** —
  extra keys pass through; `false_positives_refused:` (vault-invented, ships nowhere, carried **every**
  specimen this cycle) is promoted into `report.md` as a mandated per-slot list; (3) each per-file slot
  gets a report-internal population line derived **mechanically** from the `para_*` file walk — never
  `len()` of the rendered list, or the check compares the renderer against itself; (4) the gate runs via
  a `uv run` script with inline deps (the `lint-cache.py` precedent) or `json.loads` over the JSON
  render — `report.md:3`'s *"no library the vault does not already have"* clause points at that route;
  (5) **the failure artifact**: re-render once from the same Step-5 facts; a second failure persists the
  `…-lint-failed.yaml` shape (`status: failed`, `reason: shape — <slot>`, the full unvalidated block,
  `next: re-render from the returned workflow object, not re-sweep`); the Step-6 log line does **not**
  write; never no file. **Merge order on `report.md`: build-3 → build-5.** The brief-time question is
  reworded: *which independent instrument produces each per-file population*.

- **E2 — the `_output/` provenance read. RULED, Round 6 (2026-09-01): ATTACHED to A15-12's build —
  read BEFORE the brief is written.** ⚠ *"Read `_output/problem-solution-2026-08-25.md` before
  touching PARA zoning again"* (carried from Cycle 14's closeout). It is **gitignored and provenance
  only**, so nothing from it is quoted into tracked files; **the brief records that the read
  happened, never its contents.**

- **E3 — A15-15's unre-verified dependency. RULED, Round 6 (2026-09-01): DISCHARGED. Nothing owed.**
  The build rests on `field-contract.md` §Contract version's **additive-only** evolution rule — read
  verbatim this session (*"Adding a payload field does not bump `rail_contract` … adding a label is
  additive"*) — **not** on the platform ledger's P-10 prose, which the capture declined to
  re-verify. **Briefs cite the convention, never the platform entry**, so the two records cannot
  silently disagree.
  **→ AMENDED at the roundtable (2026-09-02, A10, W-F6):** the Evolution rule E3 rests on is **silent**
  on build-1's actual change — `field-contract.md:15-17` covers *adding a field* and *adding a label* (no
  bump) and *changing a field's meaning* (bump); build-1 **widens an existing field's closed value set**,
  and the nearest clause cuts the other way for a strict reader. E3 stands, and build-1 writes the ruling
  into the rule itself: *widening a closed value set is additive when no existing value's meaning
  changes.*

- **No further debts. RULED 2026-09-02:** E1, E2 and E3 are the whole of this cycle's evidence-debt
  register. Every other build's evidence is grounded in tracked source and was read in session.

### Questions deliberately left to brief time

Per-build, not cross-cutting. **RULED 2026-09-02 — three, recorded so a briefer knows they are open
by ruling rather than by oversight.**

- **build-2** — does A15-9's direction 2 digest `vlt-lint-full.js` **whole**, or only its **reduce**?
  The file also carries the page-scan prompt, whose movement `scanFingerprint`
  (`vlt-lint-full.js:232-233`) already catches independently, so digesting the whole file would
  double-count that half.
- **build-4** — does the read-back **move SKILL-side**, or does the **SKILL pass new inputs** across
  the boundary (as it already does for `crossLayerSlugs`, `stubSlugs` and `pageHashes`)? Round 1's
  grounding correction established it must be one or the other — the reduce has no filesystem access
  — but **which** is a brief-time design call, not an ideation ruling.
- **build-5** — what does *"the population it reports on"* resolve to, per slot, for E1's cardinality
  check? `report.md` mandates several per-file slots and their denominators are not uniform.

**→ Status after the roundtable (2026-09-02):** build-2's question **DISSOLVED** (D-B — neither whole
file nor the reduce; `module_version` is deleted, `scanModel` enters). build-4's question **RULED** (D-C —
replace, not audit; the SKILL passes `pageLinks` and `summary_len`; the extraction ships as an
executable). build-5's question **REWORDED** (A16 — *which independent instrument produces each per-file
population*), and its precondition is now a `report.md` shape change build-5 owns.

### Cycle 14 carries — dispositions *(roundtable A21, owner ruling D-F, 2026-09-02)*

Ideation consumed items 1, 4, 11–15 and 17 of `factory/cycles/14-no-enforcement-point/roadmap.md`
§Carried forward past Cycle 14 and left six undispositioned; three of them carried the bound *"Cycle
15's `inbox-capture`"*, which had already passed — the numbered-cycle done-when expiring unread, the
pattern P-16 named. Every re-bind below names an **event**.

| Item | Disposition |
|---|---|
| **2** — the `summary` paraphrase (Cycle 13 CF1; Carson's route) | **CONSUMED by build-4** (D-A: the SKILL passes `{slug: summary_len}` from disk) |
| **3** — the general reduce-side posture, deferred half | **CONSUMED by build-4's boundary ruling** (D-C) + D1(b) |
| **5** — the `malformed_frontmatter` RETIREMENT (third deferral) | **RE-BOUND to an event:** ruled at build-4's Cycle 14 build-1 (6) leg-3 grading — if the specimen set is 0 refuted there, the retirement question is answered there; Cycle 14's E4 transfers BOUND with it |
| **6** — `para_author_unknown` closed to `human\|agent\|hybrid` | **RELEASED with reason:** no filing asks it; it is the sibling closed enumeration to build-6's and the next `supersession` candidate — the owner may file it through the rail build-1 completes |
| **8** — Cycle 12's hand-off (b3(7), A12-4, A12-5, A11-11 d4 + A12-1) | **CARRIED unchanged** to this cycle's closeout collector — not this cycle's scope |
| **9** — the `:168` dissent (Victor, Amelia) | **CARRIED unchanged** — becomes the ruling when `unmarked_supersession` is structured |

### Standing rules declared at the roundtable *(2026-09-02 — R1, R2; homes named; mechanisms queued as [P-24])*

- **R1 — a rule change to a handshaked convention carries its `handshake:` line at ideation.** The
  Grouping bullet of any build that changes a convention **rule** names the bump and the re-ack roster
  (read from the convention's `consumers:`, bipartite), and `build-brief` refuses a brief whose
  convention rule change has none. *Home:* `ideation-scaffold` (the build-bullet skeleton gains a
  `handshake:` slot beside `binds:` / `spike:` / `promise:`) + `build-brief`'s gate. *Mechanism:* a
  factory-skill edit, off-cadence → **[P-24]** on the platform ledger. *Interim posture:* this
  declaration; builds 6 and 7 carry the line by A1. *Why a rule and not an amendment:* twelve of thirteen
  lanes found the gap in an hour; seven owner-steered ideation rounds did not, because nothing in the
  skeleton asks.
- **R2 — a retirement's brief enumerates every restatement and pointer of the retired rule across the
  bundle, each with a disposition.** P-15 defined the *filing* class; nothing defines the *brief* shape
  for one, and this session found each retired closure restated at four to seven sites (the operating
  contract `:66`, `frontmatter.md:71/:78/:82/:296`, `checks.md:19/:20`, the prompt literal at
  `vlt-lint-full.js:229`). *Home:* `build-brief/references/brief-anatomy.md` — a retirement section:
  grep-derived site list, a disposition per site, and the population statement that must **not** move.
  *Mechanism:* factory-skill edit → **[P-24]**. *Interim posture:* A5 and A7 carry the enumerations for
  builds 6 and 7.

## Roundtable review — A15-1..A15-15, the seven-build batch (2026-09-02)

**Convened** over the filled Ideation rulings, before any brief, per `.claude/skills/vlt-lifecycle.md`
step 4. **`build-brief` gates on this section.** Session file:
`_output/party-mode/2026-09-02-cycle15-roadmap-roundtable-session.md`. Keepsake:
`_output/party-mode/2026-09-02-cycle15-roadmap-roundtable.html`. *(The placeholder heading
`## Roundtable review record` was renamed to this canonical form at Converge — a prefix reader would
otherwise have passed an empty section, G-F2.)*

**Roster — all 13 installed voices convened, none excused (owner call).** Discovered fresh by glob,
never recalled: Mary (analyst), Winston (architect), Builder, Amelia (dev), John (PM), Paige (tech
writer), Sally (UX), Carson (brainstorming), Dr. Quinn (problem-solving), Maya (design thinking),
Victor (innovation/disruption), Caravaggio (presentation), Sophia (storytelling). The owner named no
prior worries (*"nothing in particular"*), so the roadmap foot's four joints (J1–J4) were carried
verbatim into every persona prompt and are answered inline below.

**Convergence.** The version-handshake gap (both retirements are convention **rule** changes; neither
build named a bump or a re-ack) landed in **12 of 13 lanes** independently — seven owner-steered
ideation rounds had not found it, which is why it became a rule (R1) and not only an amendment. The
v0.18.0-cold-by-construction joint landed in 11; the two-carve-outs ambiguity in 8; `pin_vector` left
in the key in 6; A15-5's false grounding sentence in 6; the J1 relabel owner-act in 13. The moderator
re-verified the six load-bearing sites in session (`summaryIssue` at `vlt-lint-full.js:640`;
`scanModel` in no key term; `SCHEMA_SIZE_BUDGET = 3700`; `checks.md:20`'s any-match join;
`lint-cache.py`'s `read`/`write` only; the five `write-verification@5` pins).

### Amendments applied (21)

| # | What it cures | Where it landed |
|---|---|---|
| **A1** | both retirements are **rule changes** and no build named the handshake — `extraction` 9→10 (4 re-acks), `write-verification` 5→6 (4 SKILLs + workflow header + 4 body pins); prose re-nouns in `frontmatter.md` with **no bump**; the v0.18.0 `governance_rule_changes` block; the `local_consumers:` field notice | §Grouping → build-6, build-7 |
| **A2** | **v0.18.0's first sweep is COLD BY CONSTRUCTION** — build-2's headline clause has no live observable on its own release; graded `[ship-verifiable]` at rest, the warm-after-upgrade half `[field-contingent]` to the next clean release; CHANGELOG states the cold run | §Grouping → Ordering note, build-2 |
| **A3** | Q3 repaired two of four key terms — **the key is re-ruled whole** (owner ruling D-B): facts-not-verdicts + `scanModel`; `module_version` deleted, `checks_digest` out, `pin_vector` narrowed | Q3; build-2 |
| **A4** | builds 2 and 3 rewrite the same `full-scale.md` paragraph and the same `RULESET_SLOTS` region with **contradictory** populations — order 2→3, build-3 `binds:` += Q3, A15-10's residual struck, d1 as a workflow-side required-name set; file-edit order 2→3→4→6→7 | §Grouping → Ordering note, build-2, build-3; §A15-10 |
| **A5** | **"the `{wiki}` carve-out" named two rules** — the type-legality one retires, the Layer-2 population/container exclusion is not touched (146 pages would otherwise enter four nets); contract `:66` *closed* → *recognized* | D5.2; build-6 |
| **A6** | nothing ruled the **recognized set** after retirement — stated (PARA ∪ operational-record ∪ overlay ∪ `frontmatter.md:71`); the 9 `type: research` files clear on upgrade with no vault act; promise re-ratified on *recognized vocabulary*, not *honesty* | build-6 |
| **A7** | build-7's retirement strands `frontmatter.md:78/:82/:296(c)` and no artifact tells a **partner** how to attest — `:47` restated never deleted, surviving clauses named, the non-op attester sentence, promise subject → *a partner's* | build-7 |
| **A8** | after build-7 the `open`-posture PASS population is counted nowhere — one denominated line | build-7; D2 |
| **A9** | J1 does **not** hold as build order (the beat is this session) — #17/#18 re-kinded by an owner act (body `kind:` + label), build-1's `[ship-verifiable]` check | build-1; §Grouping J1 note |
| **A10** | build-1's site 5 was a **phantom** (`issue-triage` has no enum); site 6 = the intake materializer (`kind` → `class:` opening line), site 7 = `config.yml`; the two mandatory halves as optional additive payload fields; `binds:` → Q6, E3, S-3 | build-1; Q6 by reference |
| **A11** | A15-5's *"no length arithmetic"* was **false** (`:640`); two measurers, one wrong — SKILL passes parsed length from disk, scanner's length verdict retired (owner ruling D-A); **`PAGE_SCAN` at 3676/3700** hard constraint; Cycle 14 build-1 (6) gains an at-rest leg | §A15-5; build-4 |
| **A12** | build-4's branch **ruled: replace, not audit** (owner ruling D-C) — `pageLinks` from an executable, `outbound_links` leaves `required`, DA7 suppression retires; a failing return is never cached; the instrument is a mutated fixture, not the live specimens; `binds:` += D3; discharges `164501` | build-4; the spanning note |
| **A13** | D3's eviction subcommand had **no caller** and step 5 writes a hand-removed record straight back — the route end to end, the legal response (a refused finding evicts), `evicted E by request` in the report, at-rest acceptance | build-2; D3 by reference |
| **A14** | D2's *"ONLY read-back"* was false as worded; the wrong-type case was still a cold cap; the denominator came from the same reader; the report had **no home for "wrong"** — rewritten in five moves | D2; build-3 |
| **A15** | D1(a)'s worked example contradicted D2 for the same slot — illustration moved to A15-7 | D1 |
| **A16** | E1's validator had no machine-readable slot list and **no denominator**; "fails loudly" left the owner nothing — one schema artifact, never closure, mechanical populations, `uv run` gate, the `…-lint-failed.yaml` failure artifact, never no file | E1; build-5 |
| **A17** | Q8's "reconcile" would have made a **third** copy of the stub heading — single home `wiki-index.md:83`, the rest pointers | Q8; build-3 |
| **A18** | the two Cycle 14 GATES markers sat in prose on a CLOSED roadmap's ledger — appended to **this** ledger by the carrying briefs; Q9 resolved (build-7 carries none); the parks debt **split in place** (owner ruling D-D) | §Deferred acceptance ledger; Q9; build-6 |
| **A19** | D4 still wore the scaffold's placeholder under an "every slot ruled" header; `updated:` stale; Round 1's "all four" wrong; cite drift `:130`→`:127`, `:228`→`:229-230` | frontmatter; D4; §What each round settled; four cites |
| **A20** | the obsolescence beat's retirements, each written into the build that ships the superseding mechanism (see below) | builds 2–7 |
| **A21** | six Cycle 14 carries ideation never dispositioned, three on an expired numbered-cycle bound — a dispositions block (owner ruling D-F) | §Cycle 14 carries — dispositions |

### Rules (2) — declared here, mechanisms queued as [P-24]

- **R1 — a rule change to a handshaked convention carries its `handshake:` line at ideation** (bump +
  re-ack roster, bipartite), and `build-brief` refuses a brief without it. *Home:* `ideation-scaffold`
  + `build-brief`. *Interim:* A1.
- **R2 — a retirement's brief enumerates every restatement and pointer of the retired rule, each with
  a disposition, and names the population statement that must not move.** *Home:*
  `build-brief/references/brief-anatomy.md`. *Interim:* A5, A7.

### Disputes — six, all owner-ruled live; no OPEN disputes

| | The split | Ruling | Dissent on record |
|---|---|---|---|
| **D-A** | A15-5: elimination only (reduce's `:640` is the single measurer) vs the SKILL passes parsed length from disk | **SKILL passes `{slug: summary_len}` + scanner verdict retired** — only this rests the gating leg 3 on bytes and consumes Cycle 14 carry 2 | Builder, Victor, Amelia — elimination sufficed for the two specimens; conceded on the paraphrase case |
| **D-B** | d2 as ruled (prose-file digests) vs delete (facts-not-verdicts) vs `scanModel` | **facts-not-verdicts + `scanModel`**; `module_version` and `checks_digest` out; `pin_vector` narrowed | Amelia, Quinn — whole-file digest was the conservative D4 reading; conceded that the reduce re-runs over cached facts every sweep |
| **D-C** | audit the scanner's `outbound_links` vs replace it with the SKILL's set | **replace** | Quinn, Carson — audit preserved the literal read-back; conceded that comparing against a value already held is ceremony |
| **D-D** | Cycle 14 build-3 (6) whole and ship-verifiable vs split at-rest / vault-act | **split in place**; the at-rest half gates | none |
| **D-E** | `verified_by:` unbounded in declared containers: change `checks.md:20` vs widen Q5's caveat | **the one-line `checks.md:20` change is in build-7** | none (Carson's alternative withdrawn) |
| **D-F** | six Cycle 14 carries | **block ratified as proposed** | none |

### Obsolescence beat — exercised for the first time, and it found retirements in five of seven builds

- **build-1:** `Obsolescence: none found` (additive vocabulary). The seam `class:` (filing) vs `kind:` (rail) is named so the brief does not invent a third word.
- **build-2:** **RETIRES** `full-scale.md` step 2's *"the first full run after any release is a COLD one"* + its worked instance, `report.md:89`'s echo, the `module_version: string` arg row — superseded by the facts-not-verdicts key; step 5's hand-delete demoted to the second remedy. → build-2 (A20).
- **build-3:** **RETIRES** the bare `## Stubs` form (single home `wiki-index.md:83`), the two-way cap wording at `:322` and step 2's *"absent slots named"*, and `report.md:89`'s closed three-reason list — superseded by the three-way absent/empty/wrong-type rendering. → build-3, Q8.
- **build-4:** **RETIRES** the scanner's summary-length verdict (superseded by the reduce's `summaryIssue` — `checks.md:15`'s own exclusion, finally enforced), `outbound_links` from `PAGE_SCAN.required` with the `:230` verbatim-links instruction, and the DA7 `partialShortfall` orphan suppression (superseded by SKILL-derived link sets). → build-4 (D-A, D-C).
- **build-5:** **RETIRES** `report.md:3`'s *"the module's release gate parses real persisted reports"* claim (no such group exists; superseded by the persist gate) and A15-7 direction 3 as an option. Cycle 14 build-4's *"the enforcement point is a reader"* ruling is honoured, not superseded. → build-5.
- **build-6:** **RETIRES** `extraction.md:84`'s closure, `checks.md:19` case (b), the `{wiki}` type-legality exception, `:84`'s *"does not answer here"* sentence, and the word *closed* at contract `:66`. **Deliberately NOT retired:** the Layer-2 population/container exclusion (A5) and `para_type_unknown` (D5.1). Reverse dependents left standing were enumerated and dispositioned (A5, A6). → D5, build-6.
- **build-7:** **RETIRES** `write-verification.md:47`'s closure (restated, not deleted) and `frontmatter.md:296(c)`'s write-op ceiling; `checks.md:20`'s partner-slug leg becomes exercisable — the two-clause contradiction is **eliminated by narrowing**, no precedence statement (Arc 9 D5). Reverse dependents enumerated (A7). → build-7.

### Instrument beat — the property each build's acceptance must protect, stated without the fix

- **build-1:** *A filing whose body says `kind: supersession` reaches the tracker under a label, a form route, and a materialized `class:` opening line that a filter, a router, triage, and capture each read as a retirement without opening prose — and a body/label disagreement is flagged, never defended.*
- **build-2:** *(a) A cached page-scan record is reused iff the page's bytes, the extractor, the scan prompt + schema, and the three scanner-read conventions are byte-identical since it was written — whatever else in the module moved; (b) one named page's record can be removed and the next sweep re-derives exactly that page and says so; (c) invoking the sweep at scale places no page/hash/slug payload in the caller's context on first run or resume.* ⚠ The antecedent of (a) is false at v0.18.0 — the instrument is the at-rest fixture, never the upgrade sweep.
- **build-3:** *For every SKILL-rendered input slot, a reader can tell from the report alone whether the value came from a non-empty population, was legitimately empty, or arrived in a form the workflow could not use — three distinct renderings — and the population line comes from an instrument other than the one that produced the value, before any agent dispatches.*
- **build-4:** *No orphan, missing-target, or over-length-summary finding names a page whose own bytes on disk contradict it — under either key that reports it — and no scanner-returned value the reduce still consumes is persisted to the cache after failing that test.* Bound: Cycle 14 build-1 (6) leg 3, now with an at-rest leg.
- **build-5:** *Every file written under `{lint_reports}` loads under a strict parser and carries every mandated key in its mandated type, and every per-file slot's entry count equals an independently derived population — or no report is written and a failed-run record says why.*
- **build-6:** *A PARA-addressed file carrying any module-canonical or vault-declared `type:` raises no `para_type_unknown` whatever folder it sits in; a value declared nowhere still does; the `para_*` population count is unchanged before and after; no rule text names `{wiki}` as an exception to the type judgment.* Bound: each park's blocker claim is false at rest.
- **build-7:** *A Layer-3 file whose `verified_by:` names an identity the nearest declaring `writers:` admits raises no authorization finding whatever kind of actor it is; one naming an identity that list refuses fails regardless of what `author:` resolves to; with no declaring ancestor it passes and is counted; the pair remains required; the handshake is bipartite-consistent.*

### Joints inherited from the foot — answered

- **J1** (A15-15's timing) — does **not** hold as build order; holds as an owner act (A9).
- **J2** (A15-4 spans builds 2/4) — holds; the rosters did not carry it (no id in build-4's resolved to A15-4) — both now bind D3 (A12); under D-C the fidelity half is a replacement, not an audit.
- **J3** (build-2's four outcomes) — the whole-build ruling stands; two of the four had no observable at this release and one had no caller — graded at rest per outcome (A2, A13).
- **J4** (`S-3` unconsumed a third cycle) — holds and is deliberate; named in build-1's roster as met-not-consumed; the fourth form inherits the `@mention` line that is S-3's exact question.

### Out of scope — for `factory/inbox/` at handoff

- **`para_author_unknown`'s closed `human|agent|hybrid`** (Cycle 14 carry 6) — released; the next `supersession` candidate, filed through the rail build-1 completes.
- **A subtree-carries-a-`type:` declaration** (A15-12's stated mechanism, reading (b) of D5.2) — exists in no shipped artifact; a mechanism-first `candidate` filing if the owner wants it.
- **[P-24]** opened on the platform ledger — R1 and R2's skill edits (`ideation-scaffold`, `build-brief`), one item.

---

**Next lifecycle move: owner-steered ideation** — rule grouping, order and scope over the 15
captures above, recorded in this roadmap's *Ideation rulings* section, then convene
`roadmap-roundtable` before any brief. Start `ideation-scaffold` to lay the skeleton.

---

**Next lifecycle move (2026-09-01, `ideation-scaffold`): the owner fills the rulings skeleton.**
The skeleton is laid at *Ideation rulings — A15-1..A15-15* above: **9 seeded pre-ideation
questions (Q1–Q9), 5 cross-filing decide-once slots (D1–D5), 3 evidence debts (E1–E3), the spikes
view, and empty build bullets** — every one unanswered, which is the honest state. No spike is
`proposed` or `running`; `S-3` is harvested-and-unconsumed, and A15-11 direction 2 is an
unregistered external unknown that demands a spike **before** its brief if Q2 takes it. Once the
rulings are filled, the move is **convene the roundtable** (`roadmap-roundtable`) — briefs follow
the review, and `build-brief` gates on both records.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below
every earlier routing, and the roadmap's newest-at-top convention does **not** apply to it. The
chat report is a copy; this line is the obligation.

---

**Next lifecycle move (2026-09-02): convene the roundtable — `roadmap-roundtable`.**

**Ideation is COMPLETE.** Seven owner-steered rounds filled every slot of *Ideation rulings —
A15-1..A15-15* above: **seven builds, one release, v0.18.0**, each build carrying its `binds:`
roster, `spike: none`, and an **owner-ratified `promise:`**. Spikes: none opened, none consumed.
Three questions deferred to brief time by ruling. `build-brief`'s ideation gate is **satisfied**;
its roundtable gate is **not** — that record is still empty, and skipping the review is an explicit
owner waiver written there, never a silence.

**Joints the roundtable inherits, named rather than left for it to find:**
1. **A15-15's timing** — the two filings that exercise the **never-exercised obsolescence beat** are
   mis-classified on the tracker right now. Capture endorsed this as a real ordering constraint.
2. **A15-4 spans build-2 and build-4** (eviction half / fidelity half); both `binds:` rosters name it.
3. **build-2's promise covers four outcomes**; the split option was offered and declined.
4. **`S-3` is unconsumed into a third cycle** — ruled deliberately, not drifted.

✅ **Round 4's Q4 clerk actions are DISCHARGED (2026-09-02):** the routed item is open as **[P-23]**
on `factory/platform/roadmap.md` (queued), and the pointer pair is written in both directions —
A15-9's entry forward to P-23, P-23's provenance note back to A15-9. **Nothing is owed at the
platform ledger from this cycle's ideation.**

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below
every earlier routing, and the roadmap's newest-at-top convention does **not** apply to it. The chat
report is a copy; this line is the obligation.

---

**Next lifecycle move (2026-09-02, `roadmap-roundtable`): brief build 1 — `build-brief`.** *(— historical record; superseded by the block at the foot, 2026-09-02 `build-brief`.)*

**The roundtable is CONVENED and its record is in place** (*§Roundtable review — A15-1..A15-15, the
seven-build batch (2026-09-02)* above): full 13-voice roster, **21 amendments applied** into the sections
they amend, **2 standing rules** declared with named homes (R1 the `handshake:` line at ideation, R2 the
retirement brief's site enumeration — mechanisms queued as **[P-24]**), **6 disputes owner-ruled live,
0 OPEN**. `build-brief`'s roundtable gate is **satisfied**. The obsolescence beat ran for the first time
and found retirements in five of seven builds; the instrument beat recorded a fix-blind property for all
seven.

**What the review changed that a briefer must not miss:** the cache key is **facts-not-verdicts +
`scanModel`** (Q3 as extended — `module_version` deleted, `checks_digest` out, `pin_vector` narrowed);
build-4 **replaces** the scanner's link return and passes `summary_len` from disk; both retirements carry
**handshake lines** (`extraction@10`, `write-verification@6`) and their site enumerations; D5.2 retires
the **type-legality** `{wiki}` carve-out only; the recognized `type:` set is **stated**; v0.18.0's first
sweep is **cold by construction** and build-2 is graded at rest; the two Cycle 14 debts are appended to
**this** ledger by builds 4 and 6; file-edit order is **2 → 3 → 4 → 6 → 7**.

**Owed outside any build:** (i) re-kind #17/#18 (body `kind:` + label) after build-1 lands — owner act,
checked by build-1's acceptance; (ii) two inbox candidates named in the record's *Out of scope*.

⚠ ~~This block is the routing of record~~ — demoted 2026-09-02 (`build-brief`); the routing of record is
the block below.

---

**Next lifecycle move (2026-09-02, `build-brief`): a fresh builder session implements the build-1
brief — `factory/cycles/15-nothing-reads-it-back/briefs/build-1-supersession-kind.md`, via
`bmad-workflow-builder`.**

**Build-1 is BRIEFED** (headless run; readiness gate passed on Q6 / E3-as-amended / `spike: none` /
roundtable 0 OPEN / owner-ratified promise). Eight F-sites (the contract, the composer, the help row,
the fourth form, the label bootstrap, the intake materializer, triage's classification clause, one
README pointer); nine brief-time dispositions recorded inline, none owner-ruled; three grounding
corrections written at the build-1 bullet above. Five acceptance checks are in the ledger
(`specimens: 2/2`). `S-3` is met, not consumed — its register file is untouched.

**The builder's exit obligations:** implement F1–F8 in that order (F1 first — every other site derives
from it), run Verification 1–10 (the fixture pair in `fixtures/` is part of the build), rewrite the
brief's `status:` to a **BUILT record with numbered deviations**, delete any `.decision-log.md`, one
commit for the build on `cycle15-v0.18.0`. Not the release build — no version bump. Then the move is
**`brief build 2`** (file-edit order 2 → 3 → 4 → 6 → 7 governs the rest of the cycle).

**Owed outside any build, unchanged:** the owner re-kinds #17/#18 (body `### kind` + label) after
build-1 lands and before the v0.18.0 tag, at the same sitting as `config.yml`'s label bootstrap —
check (3) grades it.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below every
earlier routing, and the roadmap's newest-at-top convention does **not** apply to it. The chat report is
a copy; this line is the obligation.
