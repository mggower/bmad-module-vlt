---
title: 'Cycle 15 — nothing reads it back'
status: 'open — captured 2026-09-01 (16 filings graded: 15 captured here, 1 routed to the platform ledger as P-22). Ideation COMPLETE 2026-09-02 — seven owner-steered rounds, every slot ruled; 7 builds, 1 release (v0.18.0), all promises ratified. Next: roadmap-roundtable.'
module_code: 'vlt'
created: '2026-09-01'
updated: '2026-09-01'
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

**Half 1 — the substitution.** `skills/vlt-setup/assets/workflows/vlt-lint-full.js:228` carries the
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
per-page validity verdict"*, returned by the **scanner** as a structured verdict. There is no
length arithmetic in `vlt-lint-full.js`; the number `171` was produced by an agent measuring a
string. So this is the same shape as A15-3 and A15-4 — an executor's rendering of a prose
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
`wiki-supersession`, and `write-verification` (`vlt-lint-full.js:228`); a build bumping only
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
belonging to `build-brief`'s check anatomy. **It is recorded here and not routed** — the filing
deliberately kept both halves of the cost problem in one place (*how often* a cold sweep is forced,
factory-side and free; *what one costs* when it is, module-side), and splitting it would lose that.
Ideation may route the factory half to the platform ledger; capture does not pre-empt it.

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
*"verbatim"*; `convention_digests` — *"one entry per file in `{conventions}`"*, not *"per convention
this run judges against."*

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
`vlt-lint-full.js:130` — the message already **is** that pointer:

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

*(Empty — populated by `build-brief` as each build is briefed. Cycle 14's two bound debts above are
inherited obligations, not entries here; they are graded against Cycle 14's ledger text.)*

## Ideation rulings — A15-1..A15-15 (owner-steered, 2026-09-01)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**COMPLETE — filled over seven owner-steered rounds, 2026-09-01 to 2026-09-02.** Skeleton laid by
`ideation-scaffold`; **every slot is ruled and no slot is empty.** `build-brief` gates on this
section being filled — it is.

**What each round settled.**

- **Round 1 — the cause.** `ST-7` **does not bind** (D1(a)); the mechanism question folds into
  Grouping (D1(b)). ⚠ And the round's grounding found that **the reduce cannot perform its own
  read-back** — a premise `ST-7` and two captured entries all asserted. Corrected in all four
  places.
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

### Grouping & order`** (builds, numbering, `binds:` / `spike:` / `promise:` per build, order and
release count), **`### Spikes

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

## Roundtable review record

*(Not yet convened. `build-brief` gates on this record; skipping is an explicit owner waiver written
here, never a silence.)*

⚠ **The obsolescence beat has never been exercised**, and A15-12 + A15-13 are the material it was
built to receive. A15-12 explicitly asks that both retirements be routed to **the same ideation and
separate builds**.

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

⚠ **Two clerk actions still owed, both from Round 4's Q4 ruling:** open the routed item on
`factory/platform/roadmap.md` (build-brief check anatomy — bind a check to the population it judges),
and write the **back-pointer** to A15-9 plus A15-9's forward pointer. A one-way route is the failure
P-11/P-21 were written about.

⚠ **This block is the routing of record** (platform P-13): it sits at the file's **foot**, below
every earlier routing, and the roadmap's newest-at-top convention does **not** apply to it. The chat
report is a copy; this line is the obligation.
