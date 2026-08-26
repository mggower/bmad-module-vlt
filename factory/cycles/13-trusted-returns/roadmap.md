---
title: 'Cycle 13 — trusted returns'
status: 'OPEN — opened 2026-08-26 by a **narrow patch capture** (one filing, one build, targeting a v0.16.1 patch release). Cycle 12 shipped v0.16.0 on 2026-08-25 and is therefore closed to capture (ship day, not closeout day, is the capture boundary) while remaining open for `acceptance-discharge` and `cycle-closeout`. **This capture is deliberately narrow and the title is provisional** — the cycle has one filing so far; the through-line and title are to be revisited when the first full capture batch lands. **Ideation COMPLETE 2026-08-26** — one build, `spike: none`, roundtable owner-waived on `joint moved: none`: **build-1 fixes the two JS-side instances** (the attestation misroute + the invented requirement, both at `vlt-lint-full.js:609`), cut for a **v0.16.1** patch. Finding 4 (the paraphrased verbatim field) and the general posture are **BACKLOGGED** — see §Carried forward, incl. the open routing question that the patch tag would close Cycle 13 to capture. Acceptance instrument ruled to the **six real pages that failed**, ship-verifiable so it gates. **build-1 BRIEFED 2026-08-26** — `briefs/build-1-reduce-side-guards.md`; four acceptance checks in the ledger (three ship-verifiable, all gating; one field-contingent). Brief-time grounding found `malformed_frontmatter` to be the module''s only **unhomed** finding class — one occurrence, no definition, no legal response, no report slot — owner-ruled **HOME IT, GUARD IT**, with the retirement named and deferred. Next: **a fresh builder session** implements the brief via `bmad-workflow-builder`.'
module_code: 'vlt'
created: '2026-08-26'
updated: '2026-08-26 (opened; A13-1 captured and grounded; ideation filled — Q1..Q5 ruled, roundtable waived, spike none; build-1 briefed + ledger created; **build-1 BUILT** on branch `cycle13-v0.16.1`, disposition-6 retirement recorded as carry 3, release held for the owner)'
derives_from:
  - 'factory/inbox/2026-08-26-075130-attestation-misroute-survives-the-jurisdiction-narrowing.md'
predecessor: 'factory/cycles/12-proxy-claims/roadmap.md (Cycle 12 — SHIPPED v0.16.0 @ `216bea2` 2026-08-25; OPEN for acceptance/closeout, closed to capture)'
intent: >
  Cycle 12 asked what a claim rests on and retired the proxies — location standing in for
  trust, a cached verdict standing in for a re-judgment. Cycle 13 opens on the same question
  aimed one layer down, at the module's own instruments: what does the *reduce* rest on? The
  opening filing shows a rule stated in a place where it cannot bind — a prohibition written
  into an agent's schema description while the JavaScript that consumes the agent's answer
  trusts it unconditionally. The cycle's opening claim is that this is one defect with three
  live faces, not three defects.
---

## The through-line

*(One filing so far — this section is a seed, and is rewritten as the cycle grows.)*

Cycle 12's build-1 tried to stop the full-lint page scanner from reporting a missing
attestation pair as two other kinds of finding. It did the natural thing: it wrote the
prohibition into the schema descriptions the scanning agent reads. The field then reported
the defect again, unchanged in shape, on the very next sweep.

The grounding in A13-1 says why, and the answer generalizes past this one check: **the
prohibition was stated in the prompt and enforced nowhere.** The reduce takes the agent's
returned booleans, strings and counts at face value — so a rule the agent declines to follow
has no second line of defence. Three separately-reported symptoms turn out to be that same
structure:

- a complaint routed into a slot the schema told the agent not to use,
- a field marked *verbatim* in the schema returned paraphrased, and measured faithfully,
- a requirement the schema does not contain, invented from a page's content and printed.

The first and third are literally the same line of JavaScript. The second is the same shape
one step over. Cycle 13 opens by asking where a rule has to live to actually bind, and the
patch build is the narrow, urgent instance of it.

## Owner ruling — narrow-capture carve-out (2026-08-26)

This capture opens Cycle 13 roughly one day after Cycle 12's release, driven by a single
acceptance failure that the owner ruled should be repaired by a mid-cycle patch rather than
carried as inherited debt.

**Six of Cycle 12's open acceptance tails are bounded "no later than Cycle 13's
`inbox-capture`"** — b2(5), b3(6), b3(7), b3(9), b4(5) and b4(6). Those bounds were written
on 2026-08-25 expecting Cycle 13's capture to be roughly a cycle away, and they use *an
event* as a proxy for *elapsed opportunity to fire*.

**Ruled:** this narrow patch capture does **NOT** trigger those six bounds. They attach to
**Cycle 13's first FULL capture batch** instead. Cycle 12's ledger is unchanged and its tails
keep their runway; no tail disposition is forced today.

*Recorded because a later reader would otherwise find a Cycle 13 capture dated before the
bounds and conclude they lapsed unruled. The bound's shape is acknowledged as imperfect — an
event-proxy that an unscheduled capture can trigger early — and repairing it to a calendar
form was offered and declined in favour of this carve-out, which costs one line and preserves
the evidence.*

## Capture — 1 filing (grounded against module source 2026-08-26, at v0.16.0 / `c2d66af`)

### A13-1. The reduce trusts what the prompt only asked for (2026-08-26) — `factory/inbox/2026-08-26-075130-attestation-misroute-survives-the-jurisdiction-narrowing.md`

**Origin note.** This filing is unusual in provenance: it was written by `acceptance-discharge`
on 2026-08-26 as the FAILED verdict of Cycle 12 build-1 acceptance check (5), not filed from a
vault by a partner. Its field evidence is the `{field-vault}` post-0.16.0 full lint
(`{lint_reports}/2026-08-25-1600-lint.yaml`, cold, 146/146 pages) plus the executor session's
own report. Grounding below **corrects the filing's own diagnosis** — the filing reasoned from
symptom to a plausible cause and got it half wrong, which is precisely why capture grounds
filings rather than trusting them.

---

**Finding 1 — CONFIRMED. The defect recurred, second consecutive run.**

Report `:241` records one entry under `unmarked_supersessions` (`execution-to-judgment-shift`)
and **5 of 7** `malformed_frontmatter` entries (`bistec-encebollado`,
`k-curve-career-divergence`, `kettl`, `llm-wiki-pattern`, `obsidian-bases`), all of them
"missing `verified_by`/`verified_at`" — hand-folded into the attestation census **"same as the
2026-08-24 run"**. Magnitude fell 20 → 6; shape unchanged. The predecessor filing
(`2026-08-24-173002-…`, captured into Cycle 12, built as build-1 F2/F3/F7) is confirmed as the
same defect, not a near neighbour.

**Finding 2 — CONFIRMED, and the prohibitions are present and correctly worded.**
Build-1 did ship what it claimed. At HEAD:

- `skills/vlt-setup/assets/workflows/vlt-lint-full.js:159` — `frontmatter_valid`'s description
  reads *"Absent `verified_by:`/`verified_at:` is NOT a validity defect (per
  write-verification@3 Scope rule) — attestation is reported through the
  `verified_by`/`verified_at` values above."*
- `:168` — `unmarked_supersession`'s description reads *"A missing or stale attestation is
  NEVER an unmarked supersession (per write-verification@3 Scope rule)."*

Both are unambiguous, correctly scoped, and cite their convention. **The build is not
under-delivered; the text is exactly right.** This matters for the fix direction: no amount of
re-wording these two descriptions is the answer, because the wording is already correct.

**Finding 3 — PROVENANCE CORRECTION (against the filing's own stated diagnosis).**
The filing proposes the cause is a missing *terminal class* — that the complaint routes to
"whichever slot is still open" because attestation was never given a home the scanner is
obliged to use. Grounding says the mechanism is different and more specific.

`:609` is the whole story:

```js
malformed_frontmatter: scans.filter((s) => s.frontmatter_valid === false)
  .map((s) => `${s.slug}: ${s.frontmatter_issue || 'invalid'}`),
```

The reduce admits **any** scan whose `frontmatter_valid` is `false`, and prints the free-text
`frontmatter_issue` (`:163`, *"what is wrong if frontmatter_valid is false"*) verbatim, with no
inspection of what that text says. `unmarked_supersessions` is the same posture —
`collect('unmarked_supersession')` at `:576`, unfiltered.

So the prohibition at `:159`/`:168` is **prompt-only, enforced nowhere.** An agent that sets
the boolean anyway is believed. The defect is not an absent destination; it is an absent
**guard** — the rule was stated in the one place in the pipeline that cannot enforce it.

*The filing's fix direction ("give the fact a terminal class", "make the prohibition general")
is therefore necessary but not sufficient, and its framing should not be carried into a brief
unamended. This correction supersedes the filing's §"Why the fix did not take".*

**Finding 4 — PROVENANCE CORRECTION (a claim in the filing's corroborating evidence is
wrong).** The filing cites the executor's report that the scanner "miscounted a pure `len()`
measurement twice out of two" (`kettl` reported 168, actually 156; `l-theanine` 162, actually
159) and reads it as evidence the scanners are *"eyeballing rather than counting."*

**They are not.** The count is computed in JavaScript, at `:545`:

```js
const summaryIssue = (s) => !(s.summary || '').trim() ? 'summary missing'
  : s.summary.length > 160 ? `over-length (${s.summary.length} chars)` : ''
```

JS measured correctly. What was wrong is `s.summary` itself — the schema at `:162` asks for
*"the frontmatter `summary:` value **verbatim** (empty if absent)"*, and the agent returned a
paraphrase. A 12-character transcription drift on `kettl`.

This is a **worse** finding than the filing's, and a broader one: it puts every schema field
marked *verbatim* under suspicion, not just `summary`, and it is the same structure as Finding
3 — a constraint stated in the schema and trusted absolutely downstream.

**Finding 5 — CONFIRMED, and it unifies the batch.** The third reported symptom
(`ashwagandha: missing review_after`, a requirement that does not exist — `review_after:` is
optional in the wiki schema) travels **the same line of code** as Finding 1: the agent set
`frontmatter_valid: false` with an invented reason, and `:609` printed it. Symptoms 1 and 3
are one defect at one site. Symptom 2 is the same shape at a second site.

**Finding 6 — GAP CONFIRMED, with a constraint that shapes the fix.** The workflow has **no
filesystem access** — stated outright at `:36-37` (*"the SKILL has filesystem access, this
script has none"*), and `pages:` carries `[{ slug, path }]`, paths only (`:32`). So JS cannot
independently read a page's frontmatter to check an agent's claim against the source text.

Two consequences, and they cut in opposite directions:

- **Findings 1 and 5 are fixable JS-side with no new data.** Whether a `frontmatter_issue`
  string is an attestation complaint is decidable from the string itself; whether a claimed
  missing field is actually required is decidable against the known required-field set
  (`:148`). Neither needs the page. **No new arg, no payload cost.**
- **Finding 4 is not.** Verifying a verbatim `summary` needs the real frontmatter value, which
  only the SKILL can read. The precedent for that shape already exists in this file —
  `pageHashes` is *"computed by the SKILL with an unwrapped instrument it names in the record"*
  (`:47-49`) — but it means a new per-page arg.

**Finding 7 — JOINT (partial). The Finding-4 fix aggravates a separately-filed defect.**
Tracker issue **#13** (`vault-filed`, 2026-08-26) reports that invoking `vlt-lint-full` already
requires an ~84KB inline args payload with no file-based route, costing the caller a large
slice of context before the first agent dispatches. A SKILL-side per-page `summary` arg makes
that payload larger.

The joint is **partial, not total**: it binds only if Finding 4 is scoped into the patch.
Findings 1 and 5 carry no payload cost and are joint-free.

---

**Open design questions — carried verbatim, NOT resolved here (owner rules at ideation).**

1. **Scope: two findings or three?** Findings 1 + 5 are one site, JS-side, cheap, joint-free.
   Finding 4 is a second site, needs a SKILL-side arg, and moves the joint with issue #13.
   Does the patch take all three, or ship 1 + 5 and route 4 to the full batch?
2. **If Finding 4 is in — does issue #13's file-based args route ride along?** If the payload
   is gaining an arg anyway, that is the cheapest moment to add the route. But #13 is
   `vault-filed`, **not** `vault-accepted`, so it is not admitted signal yet; pulling it in
   means the owner accepts it first.
3. **How far does the guard generalize?** Findings 1/4/5 are three instances of "the reduce
   trusts an agent-returned value." Does the patch fix the three known instances, or does it
   establish a general posture (every agent-returned value that is mechanically checkable is
   checked at the reduce)? The general form is more durable and materially larger.
4. **What is the acceptance instrument?** The Cycle 12 failure's root cause in verification was
   an at-rest fixture built to test the two closed slots, which structurally could not observe
   leakage into a third — it passed while the field failed. The candidate replacement is the six
   real pages that failed (`bistec-encebollado`, `k-curve-career-divergence`, `kettl`,
   `llm-wiki-pattern`, `obsidian-bases`, `execution-to-judgment-shift`), tagged
   **ship-verifiable so it gates**. Owner confirms.
5. **Release shape.** v0.16.1 as a patch, per the owner's standing intent. Cycle 12's ruling D3
   (*one release, whole cycle*) governed Cycle 12's four planned builds and does not reach a
   Cycle 13 release — recorded here so the question is not re-litigated at brief time.

## Grounding corrections issued at brief time — build-1 (2026-08-26)

*The superseding notes `build-brief`'s Re-ground stage owes the roadmap. **The capture body above
is append-only and is not rewritten** — this note supersedes a specific gap within it. No cite
had drifted (all seven of A13-1's `file:line` cites re-verified and HELD at HEAD, `c2d66af`);
one **material fact the capture did not establish** was found, and it did not contradict any
ideation ruling, so it did not block.*

**`malformed_frontmatter` is an undocumented, unhomed finding class.** The capture grounded
`vlt-lint-full.js:609` as the site where the reduce admits the agent's boolean unchecked, which
holds. What it did not establish is that **`:609` is the class's ONLY occurrence in the module**:

- `grep -rn "malformed_frontmatter" skills/` returns **one hit**, the emitting line itself.
- `skills/vlt-lint/references/checks.md` carries **no check definition and no legal response**
  for it.
- `skills/vlt-lint/references/report.md` carries **no slot** for it (`grep -n "malformed"` → 0),
  while the sibling mechanical class `frontmatter_drift` (`:573-575`) has both a documented slot
  and a stated population.

**Why this matters to the fix.** The misroute is not only "the reduce trusts the agent" — it is
also that **the destination has no specification**. An agent setting `frontmatter_valid: false`
has no documented contract for what that class means, so anything plausible lands there, and the
persisted report has nowhere to render it. That is the mechanical reason the 2026-08-24 and
2026-08-25 runs both required a hand-fold: the executor received entries for a class with no
report slot.

**Owner ruling, 2026-08-26 — HOME IT, GUARD IT.** Build-1 gives the class a `checks.md`
definition with a stated legal response (satisfying R3, which the build owes the moment it
narrows the class) and a `report.md` slot, then guards `:609` so only genuine schema breaks
reach it. **Nothing shipped is deleted.** The alternative — retiring the class outright and
folding genuine schema breaks into the documented `frontmatter_drift` — was considered and
**deferred, not dismissed**: it is recorded as this build's Retirement disposition naming a
later build, never a silent survival (platform P-15).

## Ideation rulings — A13-1 (owner-steered, 2026-08-26)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**COMPLETE — filled 2026-08-26.** Every slot is ruled: Q1 and Q3 scope the
build, Q2 is moot by Q1, Q4 sets a gating instrument, Q5 sets the release, the roundtable is
owner-waived on a `joint moved: none` test, and `spike:` reads `none`. `build-brief` gates on
this section being filled — it is.

Seeded from the Cycle 13 capture's *Open design questions* (A13-1), which staged five. Question
ids **Q1–Q5 map one-to-one onto that list's items 1–5**, in order, so the two records can be
read together. Numbering is the clerk's, for in-session reference only; it implies no ordering
or priority.

### Grouping & order

*Ruled 2026-08-26 — **one build**, per Q1 and Q3.*

**Capture's proposal, UNACCEPTED — recorded as material, not as a ruling:** the capture staged
A13-1 as a single patch build cut for a **v0.16.1** release. Whether that is one build, two
(splitting the SKILL-side Finding 4 from the JS-side Findings 1+5), or a wider general-posture
build is exactly what Q1 and Q3 decide. Nothing below is assigned.

**Cycle 13's patch scope, ruled 2026-08-26 (Q1 + Q3): ONE build, the two JS-side instances.
Finding 4 and the general posture are BACKLOGGED to a future cycle.**

- **build-1 — the reduce stops believing the scanner on two checkable claims (Findings 1 + 5).**
  Folds A13-1's Findings 1 and 5 only. Both live at the same site,
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js:609`, and are decidable without page
  content: whether a `frontmatter_issue` string is an attestation complaint is decidable from the
  string; whether a claimed-missing field is actually required is decidable against the
  required-field set at `:148`. **No new args, no payload cost, no joint.** Cut for a **v0.16.1**
  patch release.
  - `binds:` Q1, Q3, Q4, Q5
  - `spike:` **none** *(ruled 2026-08-26 — nothing in A13-1 is an external unknown; every finding was grounded against module source at capture)*

*(Add further build bullets as ruled. Each carries its own `binds:` and `spike:` line; an
unfilled `spike:` field is **not** `none` and blocks `build-brief`, which is correct — the owner
says whether a build waits on a spike, never the briefer.)*

**Numbering note for the record:** this is Cycle 13's build 1. The id `build-5` was used in
session on 2026-08-26 while the patch was still believed to belong to Cycle 12; it does not
apply here, and Cycle 12's own `build-5` was separately renumbered to `build-4` under its ruling
R-5. Do not carry either reference forward.

### Pre-ideation rulings the capture demanded

**Q1 — Scope: two findings or three?** Findings 1 + 5 (the misroute and the invented
requirement) are one site, JS-side, cheap, and joint-free — they travel the same line,
`vlt-lint-full.js:609`, and need no new data. Finding 4 (a `summary` marked *verbatim* in the
schema at `:162` and returned paraphrased) is a second site, needs a SKILL-side per-page arg
because the workflow has no filesystem access (`:36-37`), and moves the joint against tracker
issue #13. Does the patch take all three, or ship 1 + 5 and route 4 to the full batch?

**RULED 2026-08-26 — the first two only.** Findings 1 + 5 ship in the patch. Finding 4 (the
paraphrased verbatim field) is **not built here** and carries forward. Consequences that follow
mechanically and are recorded so no later reader re-derives them: no SKILL-side arg is added,
**Finding 7's partial joint does not bind**, Q2 goes moot, and the roundtable waiver is clean.

**Q2 — If Finding 4 is in, does issue #13's file-based args route ride along?** If the payload
is gaining an arg anyway, that is the cheapest moment to add the route. But #13 is `vault-filed`
and **not** `vault-accepted` — it is candidacy, not admitted signal — so pulling it in requires
the owner to accept it first (the label is the owner's act; materialization is gated on it).

**MOOT 2026-08-26, by Q1.** Finding 4 is out of scope, so no per-page arg is added and the
payload does not grow. Tracker **#13 is not pulled into this build** and stays `vault-filed`
candidacy — un-accepted, un-materialized, awaiting the owner's label like #12 and #14. The
question revives if and when Finding 4 is built.

**Q3 — How far does the guard generalize?** Findings 1, 4 and 5 are three instances of one
structure: *the reduce trusts an agent-returned value that the prompt merely asked to be
constrained.* Does this build fix the three known instances, or establish a general posture —
every agent-returned value that is mechanically checkable at the reduce is checked there? The
general form is more durable and materially larger than a patch, and would likely stop being a
patch.

**RULED 2026-08-26 — fix the known instances; BACKLOG the true fix.** This build guards the two
instances it can reach and does **not** attempt the general posture. The general rule — *every
agent-returned value that is mechanically checkable at the reduce is checked there* — is
**explicitly deferred to a future cycle**, named here so it is a carried decision rather than an
omission.

*Clerk's note on the record: the owner's words were "fix the three known instances and backlog
the true fix." Read together with Q1's "first two only", this is recorded as — **two instances
built now, the third instance (Finding 4) and the general posture both carried**. See
§Carried forward. If the intent was that all three instances ship in the patch, Q1 governs and
this note is the correction site.*

**Q5 — Release shape.** v0.16.1 as a patch is the owner's standing intent. Recorded so it is not
re-litigated at brief time: Cycle 12's ruling **D3** (*one release, whole cycle*) governed Cycle
12's four planned builds and does not reach a Cycle 13 release. Confirm, and state whether the
release rides this build alone.

**RULED 2026-08-26 — v0.16.1, riding build-1 alone.** A patch release carrying one build. Both
version strings bump per the standing release contract (`.claude-plugin/marketplace.json`
`"version"` and `skills/vlt-setup/assets/module.yaml` `module_version`), and
`uv run tools/package-lint.py --expect-version 0.16.1` must exit 0 before the tag, its PASS
summary line recorded in the release commit. Cycle 12's D3 is confirmed as not reaching this
release.

### Cross-filing decide-once rulings

**None.** The batch holds one filing; no cross-filing question arose. Slot kept rather than
deleted, per the skeleton's shape.

### Spikes

**Register state at scaffold time (2026-08-26):** `S-1` **consumed**, `S-2` **consumed**, `S-3`
**harvested**. **No register entry is `proposed` or `running`** — this batch inherits no open
spike. Mechanics: `factory/platform/spikes/README.md` (the register is the record; this section
is its view).

A13-1's findings were all grounded against module source in the capture; nothing here is an
external unknown. **RULED 2026-08-26 — `spike: none` on build-1, and this batch demands no
new spike.** Nothing in A13-1 is an external unknown; every finding was grounded against module
source at capture time. No register file changes state as a result of this ruling.

### Evidence-debt dispositions

**Q4 — What is the acceptance instrument?** *(This is the batch's one evidence-debt question,
and it carries the weight.)* Cycle 12 build-1's at-rest fixture **passed while the field
failed** — it was built to test the two slots the build closed and structurally could not
observe leakage into a third. The candidate replacement is the six real pages that failed
(`bistec-encebollado`, `k-curve-career-divergence`, `kettl`, `llm-wiki-pattern`,
`obsidian-bases`, `execution-to-judgment-shift`), tagged **ship-verifiable so it gates** — the
Arc 7 amendment A3 mechanism that retired the four-arc A4-4(5) debt, applied at brief time
rather than after a re-carry. Owner confirms the instrument and the tag.

**RULED 2026-08-26 — the instrument is the real corpus, and it GATES.** Build-1's acceptance
check for the misroute is graded against the **six real pages that failed on 2026-08-25**
(`bistec-encebollado`, `k-curve-career-divergence`, `kettl`, `llm-wiki-pattern`,
`obsidian-bases`, `execution-to-judgment-shift`), **tagged `ship-verifiable` so it gates
closeout** — not against a constructed fixture. **Binding on the briefer:** a fixture built to
test only the surfaces this build changes is the exact instrument that passed while the field
failed in Cycle 12; it does not satisfy this ruling, alone or in addition.

**Scope of this ruling: build-1 only.** It deliberately does **not** set a general rule about
when a check may be tagged field-contingent — that question is with the owner's dedicated
problem-solving session and its factory study on the acceptance-gate oscillation. This ruling
governs one build and does not pre-empt the study's conclusion.

*Standing context the owner may want in view when ruling Q4: the owner has opened a dedicated
problem-solving session and a factory study on the acceptance-gate oscillation itself
(ship-verifiable vs field-contingent, and in-cycle repair). Q4's ruling governs this build only
and does not pre-empt that study.*

### Carried forward — ruled OUT of the patch, not dropped (2026-08-26)

*Recorded under Q1 and Q3. Both are live, grounded, and un-built; neither has a home yet.*

1. **Finding 4 — the paraphrased verbatim field.** The schema at
   `vlt-lint-full.js:162` asks for the frontmatter `summary:` value *verbatim*; the agent
   returns a paraphrase and `:545` measures it faithfully, so the reported character count is
   wrong (`kettl` 168 vs an actual 156; `l-theanine` 162 vs 159). **The blast radius is wider
   than `summary`** — every schema field marked verbatim is unguarded by the same argument.
   Fixing it needs the real frontmatter value, which the workflow cannot read (`:36-37`), so it
   costs a SKILL-side per-page arg on the `pageHashes` precedent (`:47-49`) — and that arg moves
   the joint against tracker **#13**'s payload cost (Finding 7).
2. **The general posture (Q3's "true fix").** *Every agent-returned value that is mechanically
   checkable at the reduce is checked there.* The durable answer to A13-1's diagnosis; larger
   than a patch.
3. **Retiring `malformed_frontmatter` itself** — *named and deferred by build-1's brief-time
   disposition 6, recorded here in the same run, per P-15 (a retirement is named, never silently
   survived).* Once build-1's guard lands, the class's genuine population is "schema breaks that
   are not attestation and not invented" — which may be fully covered by the documented
   `frontmatter_drift` (`vlt-lint-full.js:573-575`). **Not taken in build-1:** retiring a shipped
   finding class is a behavioral removal that needs a *measured* population before it is safe, and
   build-1's own acceptance produces exactly that measurement (check (2) records what genuinely
   reaches the class). **Successor named:** the Cycle 13+ build that takes Q3's general posture
   (carry 2 above) also takes this retirement, informed by build-1's field numbers. Note the same
   ⚠ routing question below applies to this carry.
   *Not carried, deliberately:* the prompt-side prohibitions at `vlt-lint-full.js:159`/`:168` that
   build-1's guard makes redundant are **kept**, as defence in depth — they remain correct, they
   are cheap, and a scanner that honours them produces less work for the guard. Stated so a later
   reader does not read their survival as an oversight.

**⚠ Open routing question — where these land.** If **v0.16.1 ships out of Cycle 13**, then by
`inbox-capture`'s own rule (*ship day, not closeout day, is the capture boundary*) Cycle 13
becomes **closed to capture** the moment the patch is tagged — and both carries would have to
open **Cycle 14**, exactly as A13-1 could not be captured back into Cycle 12.

*This is not a defect in the ruling; it is the structural gap the owner has already routed to a
dedicated problem-solving session and a factory study (the acceptance-gate oscillation and the
absent in-cycle repair path). Flagged here so the carries are not silently orphaned by the
release, and so the study has a second live instance of the same mechanism, dated one day after
the first.*


### Roundtable disposition

`build-brief`'s readiness gate requires either a `## Roundtable review` record covering this
batch, or an explicit `Roundtable waived (owner)` line **in this section**. The material fact:
the capture's **Finding 7** records a **partial joint** — the Finding-4 fix aggravates tracker
issue #13's payload cost — which binds only if Q1 scopes Finding 4 in.

- If Q1 rules **Findings 1 + 5 only**: no joint moves, and a waiver is clean.
- If Q1 rules **Finding 4 in**: a joint moves, and the indicated route is a roundtable **delta**
  on that joint before the brief.

**`Roundtable waived (owner)` — 2026-08-26.** Q1 ruled Finding 4 out of scope, so no
SKILL-side arg is added, **no joint moves**, and the joint test returns `joint moved: none`. The
waiver rests on that fact, not on convenience: were Finding 4 scoped back in, this waiver would
not carry and a roundtable delta on the #13 payload joint would be the indicated route before
the brief.

### Questions deliberately left to brief time

**Left to build-1's brief:** the exact predicate that recognizes an attestation complaint in a
`frontmatter_issue` string, and the exact form of the required-field validation against `:148`
— both are implementation shape over a ruled boundary, not scope. The brief rules them and
records its reasoning; neither reopens Q1 or Q3.


## Deferred acceptance ledger

*Per-build `- [ ] **build-N (<slug>, briefed <date>):** …` bullets, appended by `build-brief`;
form per `factory/cycles/12-proxy-claims/roadmap.md` §Deferred acceptance ledger. Created
2026-08-26 with build-1's append — the section did not exist, and every brief in this cycle
gates against it.*

- [ ] **build-1 (reduce-side-guards, briefed 2026-08-26):** brief
  `factory/cycles/13-trusted-returns/briefs/build-1-reduce-side-guards.md`. Four checks — three
  ship-verifiable (all gate), one field-contingent (does not gate). **Q4 governs check (2) and is
  binding: the instrument is the real corpus, never a purpose-built fixture.**
  **(1) `[ship-verifiable]` — GATES closeout:** the guards behave on the reproduced real returns
  — over the Verification-1 fixture the five attestation-only `malformed_frontmatter` entries and
  the one attestation `unmarked_supersession` are **refused**, while **all three negative controls
  survive**: a genuine schema break, a **compound** break (malformed *and* unattested — the
  conjunction in brief disposition 1), and a genuine unmarked supersession — instrument: the
  brief's Verification-1 harness against the shipped workflow source with stubbed
  `agent`/`parallel`/`phase`/`log`/`budget` and `args` delivered as a JSON string, factory-side at
  rest; evidence: the four arrays recorded verbatim in the BUILT `status:`.
  **(2) `[ship-verifiable]` — GATES closeout:** the six pages that actually failed stop reaching
  the wrong classes — re-scanned, **zero** of `bistec-encebollado`, `k-curve-career-divergence`,
  `kettl`, `llm-wiki-pattern`, `obsidian-bases` and `execution-to-judgment-shift` reach
  `malformed_frontmatter` or `unmarked_supersessions`, and the attestation surface still carries
  them — instrument: a single-agent reader probe over **read-only copies of those six pages from
  `{field-vault}`** plus the shipped guard applied to the returns (the vault is never written);
  evidence: the returned JSON and the post-guard arrays, verbatim. **Binding: a fixture built to
  exercise only the surfaces this build changes does NOT satisfy this check** — Cycle 12 build-1's
  probe passed on exactly such a fixture while the field failed, because it could not observe
  leakage into a slot it did not model.
  **(3) `[ship-verifiable]` — GATES closeout:** the class is homed and the gate survives —
  `grep -rn "malformed_frontmatter" skills/` returns **three** hits (emitter + `checks.md`
  definition with its legal response + `report.md` slot) where it returned **one**; `collect()` at
  `:542` byte-identical; the workflow's `depends_on:` at `:11` and `vlt-lint/SKILL.md:4`'s pin
  vector unchanged; `uv run tools/package-lint.py --expect-version 0.16.1` exits **0** with both
  version strings at `0.16.1` — instrument: the brief's Verification-4 greps + package-lint's own
  A/B/C/D/E run at rest; evidence: the grep outputs verbatim and the PASS summary line.
  **(4) `[field-contingent]` — does not gate:** the defect is gone in anger and the hand-fold with
  it — on the next full-mode `vlt-lint` on `{field-vault}` after the v0.16.1 upgrade, **no** entry
  in either class is an attestation complaint, **none** is a claimed-missing optional field, and
  `fixes_applied:` records **no hand-fold of misrouted attestation entries**, against a corpus that
  produced 20 such folds on 2026-08-24 and 6 on 2026-08-25 — event: the owner runs `vlt-lint
  --full` on `{field-vault}` after upgrading to v0.16.1; performer: the owner (standing rule);
  vault: `{field-vault}` only (sole install with the 146-page wiki and this defect's two-run
  baseline); bound: the first full lint after the v0.16.1 upgrade, **no later than Cycle 13's first
  FULL capture batch** — *not* the narrow patch capture that opened this cycle, per §Owner ruling —
  narrow-capture carve-out. *This is deliberately the only field-contingent check: it measures what
  (2) measures, in anger. **(2) carries the gate precisely so this one does not have to** — the
  Cycle 12 lesson (a build's central promise riding entirely on an ungated field check) applied at
  brief time rather than after a failure.*


## Next lifecycle move

**Owner-steered ideation** on A13-1 — the five open design questions above are the ideation
agenda, and questions 1 and 3 set the build's scope. Record the rulings in an
`## Ideation rulings` section (with each build bullet's `binds:` and `spike:` fields — `spike:`
is expected to read `none`, since nothing here is an external unknown, but that is the owner's
ruling to state, not the briefer's).

Then `brief build 1`. Note that `build-brief`'s readiness gate also wants either a
`## Roundtable review` record or an explicit `Roundtable waived (owner)` line in the rulings —
Finding 7's partial joint is the material fact for that decision: if the owner scopes Finding 4
in, a joint moves and a roundtable delta is the indicated route; if the patch is Findings 1 + 5
only, no joint moves and a waiver is clean.
