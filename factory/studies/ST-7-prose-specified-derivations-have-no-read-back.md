---
id: 'ST-7'
slug: 'prose-specified-derivations-have-no-read-back'
title: 'Every value the module has an executor derive is specified in prose and never read back, so a wrong rendering is indistinguishable from a correct one and the instrument degrades silently in the direction of confident wrongness'
status: 'standing'
opened: '2026-09-01'
opened_by: 'capture (Cycle 15 inbox-capture, grounding A15-2 / A15-6 / A15-8 / A15-10) — opened without a ruling, per this register''s *Opening a study*'
session: 'none — written from the capture''s own grounding across seven filings, not distilled from a working session'
causes:
  - 'Primary: the module specifies a derivation as PROSE for an executor (an agent, or the SKILL''s own operator) to render, and then consumes the rendered VALUE without ever comparing it back to the prose that specified it. The specification is enforceable against a reader''s understanding and against nothing else.'
  - 'Secondary: every consumer of such a value is built to handle the value being ABSENT and none to handle it being WRONG. An empty stubSlugs list, an empty pin_vector, a short denominator and a dropped report key are each locally well-formed, so the consumer does the correct thing with wrong input and reports success.'
  - 'Enabling (why it is invisible): a wrongly-rendered slot and a legitimately-empty one produce the SAME observable. `files_cached: 0` is the honest cold branch and the silent failure; an absent report key and an empty one are the same absence; a stub list that is empty because the vault has no stubs and one that is empty because discovery missed are indistinguishable at the consumer. The module''s own honest-degradation posture — naming which slot was absent — cannot fire, because from the consumer''s side nothing WAS absent.'
  - 'Amplifying (new, and specific to a cached instrument): once a wrongly-derived value is persisted — into a findings cache, a sidecar, an archived report — it stops being re-derivable. Re-running the instrument, which is the ordinary response to a suspect result, returns the same wrong value from storage. The error graduates from intermittent to permanent, and its provenance (which model call, which run) is gone.'
cited_by:
  - 'factory/cycles/15-nothing-reads-it-back/roadmap.md §A15-2 (stub discovery — the spec is one clause of prose; NO regex ships anywhere in skills/)'
  - 'factory/cycles/15-nothing-reads-it-back/roadmap.md §A15-6 (governance_memory — report.md:91 says "you compose both lines yourself"; no counter ships)'
  - 'factory/cycles/15-nothing-reads-it-back/roadmap.md §A15-8 (the report shape — stated at report.md, enforced nowhere; intermittently wrong across two renders with no code change between)'
  - 'factory/cycles/15-nothing-reads-it-back/roadmap.md §A15-10 (pin_vector / convention_digests — both slots read wrongly on first attempt; 96% of the scan phase gated behind a sentence''s ambiguity)'
  - 'factory/cycles/15-nothing-reads-it-back/roadmap.md §A15-3, §A15-4, §A15-5 (the scanner-return half — the executor is an agent rather than an operator, and the same absence of read-back applies)'
superseded_by: ''
---

# ST-7 — prose-specified derivations have no read-back

## The claim

The module is unusually careful about *stating* how a value is derived, and has no mechanism
anywhere for checking that the value it received is the value it asked for. Every instance below
is a place where the module wrote a good sentence, an executor read it, rendered something else,
and the module consumed the something-else and reported success.

This is not the same cause as Cycle 14's *no enforcement point*, though they are close relatives
and the confusion is worth heading off. Cycle 14's thesis was about **rules governing artifacts**:
a rule exists, files violate it, nothing checks. This study is about **values flowing through the
instrument**: a derivation is specified, a value arrives, nothing compares the two. Cycle 14's
defect is a file that breaks a rule; this one is a *number* or a *list* that is confidently wrong
and structurally indistinguishable from right.

## The evidence — seven instances, four surfaces, one shape

All seven were grounded against module source at v0.17.1 during Cycle 15's capture. They arrived
as seven unrelated filings, from four separate field sweeps, over five days.

### Surface 1 — an input slot the SKILL's operator derives from prose

**(a) `stubSlugs`.** `skills/vlt-lint/references/full-scale.md` step 1 says, in one clause:
*"Also parse `{index}`'s `## Stubs` section for its backtick-wrapped slugs and pass them as
`stubSlugs`."* The field operator rendered this as a regex requiring a bare `## Stubs` heading.
The live index writes `## Stubs (linked, not yet written)` — a form the module's **own**
`references/checks.md:39` uses verbatim. The regex missed, an **empty** list reached the
workflow, and three registered stubs were reported as missing targets, in `fix_now`, whose legal
response is *create the page*. The vault would have been written backwards.

**No regex ships.** `grep` over `skills/` finds no stub-discovery pattern anywhere. The filing
that reported this believed it was reporting a too-narrow regex in module source; the truth is
worse, and it is this study's cleanest specimen: there was nothing to be too narrow, only a
sentence and a reader.

**(b) `pin_vector` and `convention_digests`.** The same file's step 2 specifies four fingerprint
slots. For the two **digest** slots it is exact — instrument, merge order, encoding, truncation —
and says why: *"an executor that follows them lands on the same value every run, **which is the
property that failed**."* The two **component** slots get one phrase each: *"verbatim"* and
*"one entry per convention this run judges against."* Both were read wrongly on the first
attempt. `pin_vector` was passed as a JSON array (a fair reading of *verbatim* for a list-valued
key); the workflow requires `typeof v === 'string'`, so the slot read as **missing**, the
fingerprint composed as `''`, and 146 of 146 pages became uncacheable.

The module had already learned this lesson, written it down, and applied it to two slots out of
four in the same paragraph.

**(c) The `governance_memory` denominator.** `skills/vlt-lint/references/report.md:91`:
*"**You compose both lines yourself** in both modes."* No counter ships. The operator's pattern
matched only `decision-log.md:38`'s schema heading `## [YYYY-MM-DD] <kind> — …` and missed the
12 oldest entries, which predate that schema. The convention **itself** anticipates them —
`decision-log.md:78`, *The classifiability tail* — and `checks.md:43` mandates they be counted
`unclassifiable` and *"never silently swept."* The rule was already on the operator's side. The
denominator was wrong by 20.3% for an unknown number of sweeps and **nothing about the output
looked wrong**: 47 is a plausible number, and no finding was raised.

### Surface 2 — a return an agent produces from prose

**(d) Outbound links.** `vlt-lint-full.js:228` instructs the page scanner: *"Extract verbatim: do
not normalize, and keep any |alias, #anchor, or path prefix intact."* Three distinct
non-verbatim returns are on record in the field, each landing in `fix_now`:

- a **substituted proper noun** (`cornerboxes` for `cornerbacks`);
- a **dropped `#`** on a same-page anchor, which converted a conformant intra-page reference into
  a page target that does not exist;
- **under-returned links**, which shorten the derived inbound map and manufacture orphans.

Nothing compares a returned slug against the bytes of the page it was read from — a comparison
that is mechanically available, since the page is on disk and the reduce already has its path.

**(e) The summary-length verdict.** `frontmatter.md:125` states the measure precisely —
*"counting characters, not bytes"*, on the summary, and separately mandates double-quoting. The
scanner measured the raw frontmatter line *including its quoting*. 2 of 10 findings were false,
both near-miss (`161` against a `160` limit), and the error is **systematically biased** toward
flagging compliant values, because quoting overhead alone can carry one over.

### Surface 3 — an output the SKILL renders from prose

**(f) The persisted report's shape.** `references/report.md` states the report slot by slot, and
`vlt-lint/SKILL.md:74` mandates it be persisted *"content-verbatim … unabridged, unreordered and
unreworded."* Nothing reads a rendered report back against that shape. Two renders of the same
skill over comparable runs, **with no code change between them**, produced different shapes: one
dropped `fixes_applied:` and `backlog_filed:` entirely, the next carried both correctly.

**Intermittence is the signature of this cause, and it is worse than consistency.** A
consistently-deviating render is at least a de-facto contract a consumer can be written against.
An intermittent one means no slot can be relied on to be present, and a reader cannot distinguish
an absent key from a legitimately empty one.

**(g) The persisted report's parseability.** One archived report in six does not load: an
unquoted scalar containing `: ` at line 102. A report that cannot be read is **indistinguishable
on disk** from one that can — same name, same date, same directory — so every downstream claim
resting on "the archive" silently rests on 5 of 6.

## Why it recurs — the causal chain

1. **Single-home discipline pushes derivations into prose.** The module's strongest and most
   correct convention is that mechanics live in exactly one place and every other site points at
   it. A derivation stated once, in prose, at its single home, is *exactly what the discipline
   asks for* — and prose is the one form no consumer can check. The discipline is not wrong; it
   simply has no clause about who verifies the rendering, because verification was never the
   question it was built to answer.

2. **The executor boundary is invisible in the source.** Reading `full-scale.md` step 1, nothing
   marks the moment where a specification stops being executed by code and starts being executed
   by a reader. The clause about `stubSlugs` sits in the same sentence shape as the clauses about
   globbing and exclusion, which *are* mechanical. There is no notation for *this one is on you*,
   so no author has ever had a reason to ask what happens when the reader gets it wrong.

3. **Absent is handled; wrong is not.** Every consumer here degrades honestly on absence — this
   is a real and repeatedly-exercised strength, and `full-scale.md` states it explicitly for the
   cache. Absence is a *state the code can see*. Wrongness is a *relation between the value and
   its specification*, and no site holds both.

4. **The two failures share an observable, so the honest-degradation report cannot fire.** The
   module's remedy for absence — name the missing slot in `coverage_caps` — is defeated by
   construction: a wrongly-typed `pin_vector` **is** a missing `pin_vector` from the workflow's
   side. The instrument built to make degradation loud reports the cold branch honestly and says
   nothing, because from where it stands nothing is wrong.

5. **Then the cache freezes it.** Once the findings cache began working (v0.17.0), a
   wrongly-derived value acquired durability. A scanner's substituted proper noun is now served
   from the sidecar on every subsequent sweep; re-running the lint — the ordinary response to a
   suspect finding — **cannot re-derive it**, because reuse is the cache working correctly. This
   is not a defect in the cache. It is the cause's amplifier, and it means the window in which a
   wrong derivation is cheap to catch has closed.

## Rejected alternatives

- **"This is a model-quality problem; use a better scanner."** Refuted by the specimens, and
  named as refused by the filings themselves. Three of the seven instances (a, b, c) involve **no
  model at all** — they are the SKILL's own operator rendering prose. A better scanner fixes at
  most surface 2, and leaves the shape intact. It is also the fix that does not survive a future
  model change.

- **"Tighten the prose."** This is the *local* fix each filing correctly proposes for its own
  slot, and each is worth doing. But the module already knew: the two digest slots in the very
  same paragraph are specified to the byte, *and say why*, and the two beside them are not. The
  precision was available, was applied, and did not spread. Prose precision has no ratchet — one
  careless sentence added later reopens the gap, and nothing will report it.

- **"This is ST-3."** ST-3 names the module's lack of a machine-addressable governance projection
  and full mode's lack of memory across runs — a **cost** diagnosis about paying for whole files
  and recomputing from zero. It is adjacent (both bear on `full-scale.md`, and the cache repair
  ST-3 provoked is what froze instance (d)), but it is about what an instrument *pays*, not about
  whether what it *received* is right. A cheap instrument with no read-back is this study's
  problem at lower cost.

- **"This is Cycle 14's no-enforcement-point, re-filed."** The closest call, and the reason this
  study opens rather than a filing citing Cycle 14. See §The claim: Cycle 14's population is
  *artifacts governed by rules*; this study's is *values flowing between stages*. The tell is
  that Cycle 14's remedy — build the enforcement point — was **shipped**, in build-4, for exactly
  one of the seven instances (report parseability), and it graded FAIL on its first real corpus
  while the other six were never in its scope. A remedy that generalizes has to be about the
  derivation, not about each artifact in turn.

## What this session got wrong, on record

The capture that opened this study initially graded filing `2026-09-01-140601` **CONFIRMED** on
its own diagnosis — that `normalizeTarget` reports an empty string. It does not:
`vlt-lint-full.js:423` carries `.filter(Boolean)` and a comment naming this exact case
(*"Empty-after-normalization targets (e.g. a bare `[[#anchor]]`) are dropped, not compared"*),
shipped as B5-3. The fix the filing asked for **was already in the tree**.

The correction came only from dereferencing the filing's own cited evidence — the field report
records the reported target as `'early loading phase (~ days 3-7)'`, a **non-empty** string,
which proves the empty case never occurred and relocates the defect to the scanner's return.

**This is the study's own cause, arriving inside the study's own capture.** A filing derived a
diagnosis from prose (its reading of the normalizer), and the capture nearly consumed the
diagnosis without reading it back against the value. Had it not been caught, the module would
have shipped a no-op repair, built a fixture proving the no-op, and the field would have kept
failing — which is `ST-5`'s failure mode reached by this study's road.

## What would close it

Not stated as a fix — this is a diagnosis, and ideation rules. But the shape the evidence points
at is narrow enough to name: **every value crossing an executor boundary needs a read-back at the
consumer, and the consumer is the only place that can perform one.** The four consumers here are
all in a position to do it — the reduce holds the page paths, the workflow holds the fingerprint
inputs' types, the persist step holds the report and its shape spec, the SKILL holds the decision
log. None of them looks.

The cheapest general move the evidence supports is **denominate every derived slot**: a value
arriving with the population it was derived from (*"stub discovery: 0 slugs found under
`## Stubs…` across 1 index"*) makes a wrong rendering visible without anyone having to anticipate
which rendering will be wrong. That is the module's own posture elsewhere — Cycle 14 build-2
ruled `cache_rejected` must render with its denominator, precisely so a discard is never silent —
applied to the inputs rather than only the outputs.
