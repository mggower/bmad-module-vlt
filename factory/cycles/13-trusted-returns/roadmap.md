---
title: 'Cycle 13 — trusted returns'
status: 'OPEN — **v0.16.1 SHIPPED 2026-08-26** (build 1 @ `5bc53f6`, release commit `c18c591`, annotated tag `v0.16.1` pushed to origin). Release gate: `package-lint: A/B/C/E PASS, D PASS — vlt 0.16.1`, exit 0; handshake bipartite-clean (9 conventions, 39 pins); no convention `version:` moved and no consumer re-ack was owed. **Acceptance discharged 2026-08-26 and the cycle DID NOT PASS ITS GATE** — build-1''s ledger item is 2 of 4 discharged: **(1) and (3) DISCHARGED** (harness arrays; and the class-homing greps + `package-lint` re-run at rest by the discharge run), **(2) FAILED and it GATES**, **(4) FAILED** (field-contingent, does not gate). (2) was graded DISCHARGED earlier the same day under an owner-ruled subject substitution and **that discharge was REVERSED by owner ruling** hours later when the first live post-upgrade full sweep refuted the check on a named subject — `execution-to-judgment-shift` reached `malformed_frontmatter` anyway. **Root cause, reproduced at rest:** the reduce-side guard''s residue rule (`claim.residue === ''`) assumes the scanner states a bare claim; a scanner that **cites the rule it is applying** defeats the conjunction on two legs at once, because the citation leaves prose residue *and* names `type:`/`author:` inside the rule''s own text. Nothing about the pages changed — only the scanner''s phrasing did. **Cycle 13 CANNOT CLOSE**: closeout is gated on (2), and repairing it needs a build-2. ⚠ Standing correction unchanged (`ST-5`): this check''s instrument should be the recorded returns, not the pages — and the 2026-08-26 evidence sharpens it, because the *recorded* returns were themselves an unrepresentative subset (all bare-form). ⚠ **Cycle 13 is CLOSED TO CAPTURE** (ship day is the capture boundary), so the three §Carried forward items — Finding 4, the general reduce-side posture, and the deferred `malformed_frontmatter` retirement — plus the **three filings this discharge run filed** must open **Cycle 14**. Next: **`inbox-capture` to open Cycle 14**, which captures the guard defect and briefs the repair.'
module_code: 'vlt'
created: '2026-08-26'
updated: '2026-08-26 (acceptance-discharge run — 2 discharged, 2 FAILED, (2) gate SHUT, 3 filings filed, cycle cannot close; earlier: opened; A13-1 captured and grounded; ideation filled — Q1..Q5 ruled, roundtable waived, spike none; build-1 briefed + ledger created; **build-1 BUILT** on branch `cycle13-v0.16.1`, disposition-6 retirement recorded as carry 3, release held for the owner)'
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

  ---

  **Acceptance-discharge run 2026-08-26** (evidence: `{field-vault}` upgrade-ledger entry
  `[2026-08-26 10:46] vlt 0.16.0 → 0.16.1 (own)`, module source @ `d1e3a9c`; and the first
  post-upgrade full-mode sweep `_agent/lint-reports/2026-08-26-1046-lint.yaml`, 146/146 pages,
  0 cached). **Item left UNCHECKED — the split is 2 discharged / 2 FAILED, and one of the
  failures GATES.**

  - **(1) DISCHARGED 2026-08-26** — V1 harness arrays in the brief's BUILT `status:`: the five
    attestation-only `malformed_frontmatter` entries and the one attestation
    `unmarked_supersession` refused; **four** negative controls survive (the brief required
    three; a prose-half compound was added at build time and is the one that caught the
    residue-rule gap).
  - **(3) DISCHARGED 2026-08-26** — re-verified at rest by the discharge run, not banked from
    the build: `grep -rn "malformed_frontmatter" skills/` → exactly **3** hits
    (`skills/vlt-lint/references/report.md:66`, `skills/vlt-lint/references/checks.md:15`,
    workflow emitter); `collect()` at `vlt-lint-full.js:542` string-compared byte-identical to
    `5bc53f6~1`; workflow `:11` pin line unchanged and `skills/vlt-lint/SKILL.md` untouched by
    the build commit; `uv run tools/package-lint.py --expect-version 0.16.1` → exit 0,
    `package-lint: A/B/C/E PASS, D PASS — vlt 0.16.1`; both version strings at `0.16.1`.
    *Correction on record:* the BUILT `status:` cites the emitter at `:688`; it is at `:700`.
    No commit after `5bc53f6` touched the file — a stale mid-build line number, not a defect.
  - **(2) FAILED 2026-08-26 — GATES closeout, and this REVERSES a same-day discharge.**
    Graded DISCHARGED earlier on 2026-08-26 under an owner-ruled subject substitution (the
    recorded 2026-08-25 field returns replayed through the shipped guard, in place of the
    briefed live re-probe, which had returned clean on all six and was non-probative). The
    first live post-upgrade sweep then **refuted the check on a named subject**:
    `execution-to-judgment-shift` — one of the six — reached `malformed_frontmatter` as an
    attestation-only complaint (report `:113`). The substitution is now visibly *why* it
    passed: the replayed 2026-08-25 returns were all **bare-form**, and bare-form is exactly
    the subset the guard handles, so the instrument could not observe the failure mode the
    check was written to catch — the defect (2)'s own binding warned about for Cycle 12
    build-1's fixture, reproduced with a different instrument. **Owner ruling 2026-08-26: grade
    FAILED, gate stays shut** — (2) carries the gate so build-1's central promise would not
    ride an ungated field check, and a green (2) against a field-refuted promise would close
    Cycle 13 on a trusted return, in the cycle named for refusing them. Filing:
    `factory/inbox/2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md`.
  - **(4) FAILED 2026-08-26 — field-contingent, does not gate.** Clause 1 false
    (`execution-to-judgment-shift` is an attestation complaint in `malformed_frontmatter`;
    `costa-rican-village-dog` is one in `unmarked_supersessions`, and appears in
    `unattested_write` too — the exact duplicate the guard shipped to remove). Clause 2 false
    (`empyrean-series-overview`: claimed-missing `review_after`, a documented-optional slot —
    disposition 2's own target). Clause 3 false — all 3 `unmarked_supersessions` entries and 2
    of 3 `malformed_frontmatter` entries were refuted **by hand** (5 folds, against the 20 of
    2026-08-24 and 6 of 2026-08-25 the check named as its baseline). Same filing as (2).

  **Root cause, reproduced at rest against the shipped source by the discharge run.** Both
  predicates end in `claim.residue === ''`. `parseClaim()` strips recognized frontmatter keys
  plus a fixed `CLAIM_FILLER` list and treats the remaining prose as residue; non-empty residue
  ⇒ no guard fires. A scanner that **cites the rule it is applying** defeats the conjunction on
  two independent legs at once — the citation leaves prose residue *and* names `type:`/`author:`,
  real `PAGE_REQUIRED_FRONTMATTER` members, inside the rule's own quoted text. Verified by
  running the shipped predicates over the real claims: the 2026-08-25 bare form → `residue=""`,
  REFUSED; the 2026-08-26 rule-citing form → `named=[verified_by, verified_at, author, type]`,
  `residue="lacks per write verification md scope rule files wiki research agent hybrid require
  attestation"`, NOT refused. **Nothing about the pages changed — only the scanner's phrasing
  did.** The guard's population is not the defect's population; it is the subset whose wording
  happened to be terse. Build-1's own premise (a rule stated in the prompt and enforced nowhere
  does not bind) recurs one level up: the enforcement point now *parses scanner-returned free
  text* in order to decide whether to trust a scanner-returned claim.


## Next lifecycle move

*(Rewritten by the acceptance-discharge run 2026-08-26. The prior text — "owner-steered
ideation, then brief build 1" — was discharged by build-1 shipping and is preserved in git.)*

**`inbox-capture`, opening Cycle 14.** Cycle 13 **cannot close**: acceptance check (2) is
ship-verifiable, GATES closeout, and is FAILED by owner ruling on live field evidence. There is
no discharge path left inside this cycle — (2) is refuted, not waiting, so no re-run of
`acceptance-discharge` can move it. Only a shipped repair can, and Cycle 13 is closed to
capture (ship day is the capture boundary).

Cycle 14's capture batch inherits, at minimum:

1. **The three filings this discharge run filed** (`factory/inbox/`, all dated 2026-08-26) —
   `…-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md` (the
   gating one), `…-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md`,
   `…-164502-html-escaped-scanner-return-fails-an-exact-comparison.md`.
2. **The three §Carried forward items** — Finding 4, the general reduce-side posture (Q3's
   backlog), and the deferred `malformed_frontmatter` retirement.
3. **Cycle 12's six bounded tails** — b2(5), b3(6), b3(7), b3(9), b4(5), b4(6). Per §Owner
   ruling — narrow-capture carve-out, they attach to **Cycle 13's first FULL capture batch**,
   which the narrow patch capture explicitly did not trigger. Cycle 13 never ran one and is now
   closed to capture, so **Cycle 14's capture is that batch** and the bounds land there.
4. **The `{field-vault}` overlay staleness surfaced by the 0.16.1 upgrade** —
   `vault-operating-contract.overlay.md` §D's parenthetical names Layer-3 territory as
   "`{projects}` and `{areas}`"; `{resources}` has been Layer-3 since 0.15.0. Report-only and
   correctly not fixed by the upgrade (an overlay is vault-owned and append-only).

**The shape worth carrying into ideation:** three of this sweep's four false findings came from
the reduce trusting scanner-returned **text** — prose, an enumeration, an encoding — rather than
positively identified structure. Q3 backlogged the general reduce-side posture as "named, not
omitted"; the field has now paid for that deferral once. Whether Cycle 14 fixes the three
instances or the posture is the ideation question, and the evidence for taking the posture is
materially stronger than it was on 2026-08-26 morning.

**Owner action outstanding:** the vault has not run `vlt-feedback` — the `{field-vault}` session
flagged that as the vault owner's call, so nothing from this sweep is filed upstream on the
public tracker yet. The two live `kind: parked-interim` entries (issues #15, #16) both reproduced
exactly in the lint — 5 `type: research` briefs and 27 unattested PARA files, counts matching the
parked entries to the file — and both remain valid on their own terms; v0.16.1 moved nothing
they rest on.
