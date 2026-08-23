---
title: 'Build #B7-7 — the council fallback (a gated mint meeting an unavailable council now parks or records a user-ruled verdict — never an unmarked substitute)'
status: 'BUILT 2026-08-15 — all F-sites landed as briefed; no deliberate deviations. F1: decision-log.md verdict line reformed, new *Verdict provenance (v2)* subsection (three forms, no-backfill, pre-facet tier) landed verbatim, write-side-only enforcement honesty paragraph appended to Enforcement, version 1→2 + last_updated 2026-08-15 (consumers unchanged). F2: vlt-mint Step 2a gained the named-fallback paragraph after step 4 (park default / user-ruled attended-only escape / self-review illegal) + the step-3 provenance pointer sentence; ack → decision-log@2. F3: Phase-2→3 exit gate amended (fielded-or-user-ruled satisfies resolved; parked named a legal resting state, unrecorded substitute named illegal). F4: planning-doc contents widened with "not fielded — <why>; parked". F5: vlt-upgrade + vlt-lint walked — both key on kind:/ref:, neither encodes the verdict line''s form, no text edit needed; acks → decision-log@2. F6 verified: git diff empty for vlt-review-council.js and vlt-review-council/SKILL.md. VERIFICATION: (1) single-home greps — exact vocabulary strings ((council-degraded — …), (user-ruled — panel not fielded: …)) only in decision-log.md; vlt-mint carries the brief-drafted pointer, no restated form list. (2) cross-file greps — park/user-ruled path names agree across F2/F3; parked state string identical at F2 fallback and F4 (:64); :26 resume scan (incomplete-checklist key) unchanged and still matches. (3) desk-check, four cases, each one named path: (a) workflow available → steps 1-4, council provenance w/ lensesFielded; (b) unavailable+unattended → park (planning-doc state, checklist incomplete, stop; no step demands a verdict before the park; :26 resume offer picks it up); (c) unavailable+attended+user rules → user-ruled w/ required why, exit gate names it resolved; (d) context-substituted review → illegal from :102 alone ("an unrecorded substitute review is not"). (4) handshake — package-lint Group E PASS: decision-log@2 three consumers ↔ three acks, zero stray @1 in shipped tree (grep exit 1 outside gitignored reports/), frontmatter@7 untouched, vlt-review-council.js header ack intact. (5) uv run tools/package-lint.py --expect-version 0.9.1 → A/B/C/E PASS, D PASS, exit 0. (6) R2 non-trigger — git diff tools/ empty; test-package-lint 21/21 green; CASE_FLOOR 21. (7) F6 diff empty (shown, not assumed). (8) scrub — placeholder paths only, no vlt-core content quoted, no .decision-log.md anywhere in the working tree.'
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-14-182143-mint-mandates-a-council-it-has-no-fallback-for.md (A7-13: the unconditional Phase-2 gate with no branch for an unfieldable panel — stall or improvise, nothing marks which; and the verdict vocabulary''s missing provenance facet — a user-ruled substitute and a four-lens panel produce the same string in the permanent log)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: >
  roadmap §Ideation rulings (2026-08-15): grouping row B7-7 (the council fallback — a named path
  for an unavailable council built over the park-and-resume machinery that already exists, plus
  the verdict-provenance facet "scoped in regardless"; brief re-reads the Arc-3 adjacency filing);
  framing ruling 1 (A7-13 is one of the narrow three — a missing mechanism the module owns, NOT
  the B7-4 seam); brief-time designation for A7-13 ("B7-7's brief rules which of the three
  options"); evidence-debt disposition (A7-13's calibration disclosure ATTACHES to B7-7, not
  blocking); the frontmatter bump plan + A1/A6 (no frontmatter bump outside B7-3; reopen = a
  full-walk version bump — this build does not touch frontmatter.md); standing rules R1 (interim
  posture rides any rule shipped ahead of its mechanism), R2 (fixture rides any gate-check
  change), R3 (declared: no finding class without a stated legal response). Post-ideation
  amendment A3's optional move of the A4-4 (5) debt to B7-7 was DECLINED by B7-6's brief
  (its disposition 6), and B7-6 discharged that check with passing at-rest evidence — it is not
  re-scoped here.
risk: >
  low — bumps `decision-log` 1→2 (a real rule change: the verdict line gains a required
  provenance facet for gated kinds), which triggers the three-consumer walk
  (vlt-mint, vlt-upgrade, vlt-lint) and a Group E bipartite re-check; `frontmatter` stays @7
  untouched; no workflow `.js` change, no release-gate-check change (R2 not triggered,
  CASE_FLOOR stays 21), no new finding class (R3 satisfied by declaration below).
---

# Build #B7-7 — the council fallback

## Intent

`vlt-mint`'s blast-radius gate is the module's strictest ceremony, and it is unconditional: Step 2a
(`skills/vlt-mint/SKILL.md:93-100`) stages, invokes `workflow('vlt-review-council', …)`, captures,
and acts — with **no branch for the workflow being unavailable**, and the Phase-2 exit gate (`:102`)
requires a resolved verdict before anything goes live. A gated mint in a tool-restricted environment
(a background job with fan-out off, a constrained runner, a headless CI-style invocation) can only
**stall** or **improvise**, and the module sanctions neither. The field event that filed A7-13 took
the second path: vlt-core substituted a user review of the staged diff and — purely by the author's
discretion — recorded the substitution honestly. Nothing asked for that honesty and nothing checks
it: the permanent decision log's `verdict:` field
(`skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md:41`) has **no vocabulary for
how a verdict was reached**, so a rubber stamp, a user ruling, and a four-lens panel are
indistinguishable forever.

This build ships the two halves the capture graded CONFIRMED: (1) a **named response to an
unavailable council** — built over the park-and-resume machinery that already exists and is
exercised (`vlt-mint/SKILL.md:57-66` the resumable planning doc, `:26` the activation-time resume
scan) and *"simply is not named as the response"*; (2) a **verdict-provenance facet** in the
decision-log entry schema, required for gated kinds, so the substitution the field already performed
becomes structural rather than discretionary. Per framing ruling 1 this is a **narrow fix** — a
missing branch and a missing facet in mechanisms the module owns — not a seam, and nothing here
touches the B7-4 receiving-surface design.

All rejected alternatives in the parent filing and the rulings are settled — do not re-litigate.
The three-option design question the roadmap left to this brief is ruled in disposition 1 below.

## Brief-time dispositions

Autonomous run — every judgment call this brief made without the owner is recorded here.

1. **The named path (the roadmap's three options, ruled): park-and-resume is the default response
   (option 2); a user-ruled verdict is legal only as an explicit, user-present escape (option 1's
   shape, bounded), and it always carries the provenance facet; the inline degraded panel
   (option 3) is REJECTED.** Derives from the brief-time designation ("B7-7's brief rules which of
   the three; the provenance facet is scoped in regardless"). Reasoning: **(a)** the grouping row
   itself frames the build as *"built over the park-and-resume machinery that already exists"* —
   the planning doc is specified live/resumable with a current-phase checklist (`:57-66`) and the
   activation scan already offers to resume an incomplete mint (`:26`); parking preserves the
   gate's meaning exactly, at the cost of a round trip. **(b)** A park-only design has the real
   cost the filing names — in a vault whose sessions are frequently constrained, gated mints
   rarely finish where they start — and the field event shows the user-ruled substitute working
   and being *"arguably the right substitute"* (the user is the vault's boundary-setter, per the
   filing). The arc's honest-surface posture is to name what will happen anyway and mark it, not
   to forbid it into improvisation; so the escape is legalized but bounded: **only the user, only
   explicitly, only in the live session, and never silently** — the provenance facet is the mark.
   **(c)** Option 3 is rejected on two structural grounds: an inline "degraded panel" synthesized
   by the minting context reviews its own staging — the independence that is the panel's entire
   value (`vlt-review-council.js:129-131`: lenses "do NOT see each other's positions") is
   unavailable to a single context by construction; and a prose degraded-panel in `vlt-mint` would
   restate panel composition, the exact single-home violation Step 2 deliberately retired
   (`vlt-mint/SKILL.md:80` — `KIND_PANEL` is owned in one place, the workflow). An unattended
   session therefore parks; an attended session may proceed on the user's explicit ruling; a
   minting context may never substitute its own review.
2. **The provenance facet lands in the decision-log convention, as verdict-line vocabulary — and
   that is a rule change: `decision-log` bumps 1→2 with the full three-consumer walk in this
   build.** The permanent record is the log; its entry schema is single-homed at
   `decision-log.md:33-47` ("every writer appends in this shape … both point here rather than
   restating"), so the facet has exactly one legal home. Making it *required* for gated kinds
   changes what writers must produce — a rule consumers must follow — so per the version-handshake
   rule the `version:` bumps and every consumer (`vlt-mint`, `vlt-upgrade`, `vlt-lint`,
   per `decision-log.md:12`) is walked and re-acked in the same build. The vocabulary
   (F1): `council` (workflow fielded — record the lenses), `council-degraded` (the workflow's own
   degraded return — it already exists at `vlt-review-council.js:154-164` and is unrecordable
   today), `user-ruled` (panel not fielded — the *why* is required). **No backfill**: append-only
   forbids rewriting old entries (`decision-log.md:56`), so pre-@2 entries without the facet are
   simply pre-facet, the same honest-tail posture the schema already takes for `kind:`/`ref:`.
3. **Rule and mechanism ship together, so R1 is satisfied with no interim window — and no new
   finding class ships, so R3 is satisfied by declaration.** The @2 rule (writers record
   provenance) and its mechanism (`vlt-mint` Step 2a's amended capture step, F3) land in the same
   build; there is no window in which a vault holds the rule without the ceremony that honors it.
   Deliberately **no lint check** is added for the facet: the convention's existing enforcement
   (`decision-log.md:83-87` — the read-before-flag, keyed on `ref:`) does not validate verdict
   lines, and adding a checker would create a finding class this narrow fix does not need. Per R3
   (declared this arc, built Arc 8): **this build ships no new finding class**; the facet's
   enforcement is write-side — the ceremony itself — and F1 states that honestly in the
   convention's Enforcement section so the surface does not imply a check that does not exist. If
   a later build promotes the facet to a checked rule, R3 binds it then (its legal response must
   ship with the check).
4. **No change to `vlt-review-council.js`, and its `depends_on: []` stays truthful.** The workflow
   already returns everything the facet needs — `lensesFielded` (`:190`), `degraded: true` on the
   no-lens path (`:154-164`), the verdict enum (`:120`) — and it never writes the decision log, so
   the @2 rule does not bind it and it is not (and does not become) a `decision-log` consumer.
   Its B7-6 header ack (`:11-15`) is untouched. No release-gate check changes → **R2 is not
   triggered**: `tools/package-lint.py` and `tools/test-package-lint.py` are untouched,
   `CASE_FLOOR` stays 21.
5. **Re-derived from the shipped module spec, not inherited from vlt-core's preview** (the
   disclosure honored by every Arc-7 brief, and the evidence debt the rulings attach to this
   build). vlt-core's 2026-08-14 substituted review — its decision-log entry recording
   *"user-ruled pass (council not fielded — …)"* — is treated as **one field instance of what
   `user-ruled` provenance looks like**, evidence that the shape occurs, never as the design or
   the wording. Every F-site below derives from `vlt-mint/SKILL.md`, `decision-log.md`, and
   `vlt-review-council.js` at HEAD. The calibration half of the disclosure (the substituted
   review's quality being load-bearing on A7-11/A7-12/the base divergence) was consumed by
   B7-3's and B7-5's briefs per the disposition ("their briefs should re-derive rather than
   inherit"); nothing remains of it for this build beyond the acceptance note in §9.
6. **Adjacency re-read performed (per the grouping row):
   `inbox/2026-07-16-153000-new-partner-fields-one-lens.md` — its composition half is already
   fixed at HEAD; the availability half is this build; the filing is not folded in.** The Arc-3
   filing's §4-A (`new partner` / `retire a partner` field one lens) is superseded by build-22:
   both kinds are full-panel at `vlt-review-council.js:72,75`, with the rationale comments the
   filing asked for. Its §4-B (mint-mode lens *widening*) and §4-C (thin-panel warning) remain
   un-shipped and are **out of scope here** (that filing's own tail, tracked by its own arc's
   disposition — see §6). The capture's "a fix for either leaves the other standing" now reads:
   composition fixed, availability is this build. This is an adjacency note, not a grounding
   correction — nothing in the Arc-7 roadmap asserts the composition half open.
7. **The A4-4 (5) inherited debt is not re-scoped here.** Amendment A3's optional move to B7-7 was
   ruled "owner's call at brief time" and B7-6's brief declined it (its disposition 6); B7-6 then
   discharged the check ship-verifiably with passing at-rest evidence (its ledger check 3, gating
   the arc). Re-opening it here would double-home a discharged check.

## Grounding record (re-ground at HEAD, 2026-08-15, branch arc7-v0.10.0 after B7-6 `525f077`)

Every capture-cited site re-verified against current source. **All HOLD** (some trivially shifted —
B7-3/B7-6 edited `vlt-mint/SKILL.md` above and around Phase 2); no grounding corrections, no
roadmap superseding note owed. Fresh lines:

- `skills/vlt-mint/SKILL.md:26` — the *Resume an in-flight mint* activation scan. HOLDS.
- `:57-66` — *The planning doc (gated kinds — resumable)*: `:59` gated kinds named + "ceremony-free"
  carve-out; `:63` created at Phase-1 start at `_agent/mint/{YYYY-MM-DD}-{slug}.md`; `:64` contents
  incl. "the council verdict (or \"not yet run\")" and "the **current phase + a done/pending
  checklist**"; `:65` phase-boundary write points. HOLDS.
- `:70` — the mint-operational decision-log paragraph ("**when this skill writes** — a gated mint's
  verdict capture (Step 2a) …"); mechanics single-homed at `{conventions}/decision-log.md`. HOLDS.
- `:80` — Step 2's single-home statement: `KIND_PANEL` owned by the workflow; vlt-mint "does
  **not** restate the panel composition (that was a single-home violation)". HOLDS (load-bearing
  on disposition 1's rejection of option 3).
- `:93-100` — Step 2a's four numbered steps (capture cited `:92-95`; heading now at `:93`). The
  verdict vocabulary `pass`/`revise`/`reject` is in step 2 at `:98` (capture cited `:100` — the
  vocabulary sentence sits one step earlier at HEAD; act-on-verdict is `:100`). `:99` — "**Capture
  is mandatory, not optional.**" verbatim as captured. HOLDS, trivially shifted.
- `:102` — the Phase-2 → 3 exit gate, incl. the council-none trivial clearance. HOLDS.
- `skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md` — `:11` `version: 1`;
  `:12` `consumers: [vlt-mint, vlt-upgrade, vlt-lint]`; `:33-47` entry schema; `:41` the verdict
  line (`<council verdict + reasoning, or 'non-boundary: <why>' / 'council-none'>` — no provenance
  vocabulary); `:56` no-backfill; `:60-62` supersession idiom; `:83-87` Enforcement. HOLDS.
- `skills/vlt-setup/assets/workflows/vlt-review-council.js` — `:11-15` the B7-6 `depends_on: []`
  header ack; `:120` the SYNTHESIS `verdict` enum; `:129-131` lens-independence comment;
  `:154-164` the no-lens degraded return (`degraded: true`, mint mode → `verdict: 'revise'`);
  `:190` `lensesFielded`. HOLDS.
- `skills/vlt-review-council/SKILL.md:46` — hand-run mint review: "`vlt-mint` owns recording it
  and gating the mint". HOLDS (keeps F-sites out of this file — recording mechanics are not
  restated there).
- Acks at HEAD: `vlt-mint/SKILL.md:3`, `vlt-upgrade/SKILL.md:3`, `vlt-lint/SKILL.md:4` — all pin
  `decision-log@1`. HOLDS (these are F4/F5's walk targets).
- Adjacency: `vlt-review-council.js:72,75` — `new partner` / `retire a partner` full panel with
  build-22 comments (disposition 6's evidence).

## F1 — `skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md` (the provenance facet: schema + version 1→2)

**Current state:** `:41` inside the entry-schema fence:

```
- verdict: <council verdict + reasoning, or `non-boundary: <why>` / `council-none`>
```

`:11` `version: 1`; `:4` `last_updated: 2026-07-29`. The Enforcement section (`:83-87`) describes
only the `ref:`-keyed read-before-flag.

**The change (four edits, one file):**

1. **The verdict line** (`:41`) is replaced with a form that carries provenance:

   ```
   - verdict: <verdict> (<provenance>) — <reasoning>   # or `non-boundary: <why>` / `council-none`
   ```

2. **A new short subsection** immediately after the schema's two key bullets (`:46-47`), titled
   `### Verdict provenance (v2)`, stating the rule — draft text the builder lands verbatim or
   tightens without weakening:

   > A **gated** entry's `verdict:` records *how the verdict was reached*, not only what it was —
   > a parenthetical provenance, one of exactly three forms:
   >
   > - **`(council — lenses: <the workflow's lensesFielded>)`** — the panel workflow was invoked
   >   and fielded; the lens list is the workflow's own return, not a recollection.
   > - **`(council-degraded — <the workflow's note>)`** — the workflow ran but produced a degraded
   >   verdict (e.g. no persona lens could be read); carry its `note`.
   > - **`(user-ruled — panel not fielded: <why>)`** — the council could not be fielded and the
   >   **user** explicitly ruled the verdict in the live session. The *why* is **required**, never
   >   optional: an entry that cannot say why the panel was not fielded is an improvisation, not a
   >   ruling. Only the user may substitute for the panel — a minting context never reviews its
   >   own staging (see `vlt-mint`, Step 2a).
   >
   > Provenance is required on every **new** gated entry from v2 on. `non-boundary:` and
   > `council-none` entries carry none (there was no panel to account for). **No backfill** —
   > append-only means pre-v2 entries without the facet are *pre-facet*, a third honest tier of
   > the classifiability tail, surfaced, never silently swept.

3. **Enforcement honesty line** appended to the Enforcement section (`:83-87`): the provenance
   rule is **write-side** — enforced by the ceremonies that write gated entries (`vlt-mint`
   Step 2a is the first) — and is *not* covered by the read-before-flag check, which keys on
   `ref:` only. No new finding class ships with v2 (stated so the surface does not imply a
   checker that does not exist; a build that later adds one owes R3 its legal response).

4. **Frontmatter:** `version: 1` → `version: 2`; `last_updated:` → the build date. `consumers:`
   is unchanged (`[vlt-mint, vlt-upgrade, vlt-lint]` — no consumer added or removed).

**Why:** the silent-by-construction half of A7-13 — `verdict:` has no vocabulary for how the
verdict was reached, so the permanent, upgrade-durable record cannot distinguish a panel from a
substitute from a rubber stamp. Single-home discipline puts the vocabulary here and only here
(`:23` — "every writer appends in this shape … both point here rather than restating").

**Out-of-scope note (this site):** the governance bundle is the SSoT (CLAUDE.md standing rule) —
no second copy exists to edit. `vlt-mint/assets/decision-log-template.md` needs **no change**: it
already points at this convention for the entry shape and restates no mechanics.

## F2 — `skills/vlt-mint/SKILL.md` Step 2a (the unavailable-council branch + provenance-aware capture)

**Current state:** `:93-100` — Step 2a's four numbered steps assume the invocation returns; no
branch exists for the Workflow tool being unavailable. `:99` (step 3) requires recording "the
verdict **and its reasoning**" with no provenance form named.

**The change (two edits):**

1. **A new paragraph after step 4** (`:100`), bolded lead-in, the named branch — draft text:

   > **When the council cannot be fielded (the named fallback — never improvise):** if the
   > Workflow tool is unavailable in this environment (fan-out disabled, a constrained or
   > headless runner), the gate does not dissolve and the mint does not self-review. Exactly two
   > legal paths:
   >
   > - **Park (the default — the only path in an unattended session).** Write the condition into
   >   the planning doc (`council verdict: not fielded — <why>; parked`), leave the checklist
   >   incomplete at Phase 2, and stop. The activation-time resume scan picks the mint up in a
   >   session that can field the panel — parking is the *designed* response, not a failure.
   > - **User-ruled verdict (attended sessions only, the user's explicit act).** The user — the
   >   vault's boundary-setter — may review the staged diff and rule `pass`/`revise`/`reject`
   >   themselves. Record it with `user-ruled` provenance per `{conventions}/decision-log.md`
   >   (*Verdict provenance*): the panel-not-fielded *why* is required. The minting context may
   >   never substitute its own synthesis for the panel — a self-review is not a fallback, and
   >   the panel's composition lives in the workflow, not here.

2. **Step 3 (`:99`)** gains one sentence after "A gated change must carry its own rationale.":

   > The verdict line carries its **provenance** per `{conventions}/decision-log.md` (*Verdict
   > provenance*) — `council` with the workflow's `lensesFielded`, `council-degraded` with its
   > note, or `user-ruled` with the required why; the vocabulary is single-homed there, not
   > restated here.

3. **Ack bump:** `:3` `depends_on: ["spec@2", "frontmatter@7", "decision-log@1"]` →
   `"decision-log@2"` (the walk's real-edit consumer).

**Why:** the missing branch is the filing's core defect; the two named paths are disposition 1's
ruling. The pointer-not-restatement form keeps the vocabulary single-homed at F1.

## F3 — `skills/vlt-mint/SKILL.md:102` (the Phase-2 exit gate names the fallback states)

**Current state:** `:102` — "the council verdict is **resolved** (a `pass`, or a `revise` applied
and re-staged to pass) **and** every open user-decision is **ruled** …". No legal non-exit state
for an unfieldable panel; a user-ruled verdict is not named as satisfying the gate.

**The change:** amend the gate's first clause (keeping the boundary-mint and council-none text
untouched) to:

> the council verdict is **resolved** (a `pass`, or a `revise` applied and re-staged to pass —
> fielded by the workflow, or user-ruled under the named fallback in Step 2a, recorded with its
> provenance) **and** every open user-decision is **ruled** … A gated mint whose council cannot
> be fielded and whose user has not ruled it **parks** (planning doc, Step 2a's fallback) — parked
> is a legal resting state; an unrecorded substitute review is not.

**Why:** the exit gate is the sentence the filing quotes as sanctioning neither stall nor
improvisation; after this edit both legal states are named at the gate itself, and the illegal one
is named illegal.

## F4 — `skills/vlt-mint/SKILL.md:64` (planning-doc contents: the parked vocabulary)

**Current state:** `:64` — "**Contents:** … the council verdict (or "not yet run"); …".

**The change:** widen the parenthetical: `the council verdict (or "not yet run", or "not fielded —
<why>; parked" per Step 2a's fallback)`.

**Why:** the park writes a state the resume scan must be able to read; today's contents vocabulary
has no word for it. One clause — the planning-doc mechanics otherwise stand.

## F5 — `skills/vlt-upgrade/SKILL.md:3` and `skills/vlt-lint/SKILL.md:4` (the walk's no-edit consumers: ack `decision-log@2`)

**Current state:** both pin `decision-log@1`.

**The change:** walk each against the @2 rule change and bump the ack to `decision-log@2`.
Expected conclusion for both: **no text edit needed** — `vlt-upgrade`'s writers/readers
(write-through at `:85`, reconcile at `:77`) and `vlt-lint`'s read-before-flag key on
`kind:`/`ref:`, not on the verdict line's internal form; a `verdict:` line with a provenance
parenthetical still matches the schema they consume. The ack bump records that a human verified
exactly that (the ceremony's own rule: "Reconciliation may legitimately conclude 'no edit needed
here' — bumping the ack still records that a human verified it"). If the walk finds either skill
*does* encode the verdict line's form, the matching edit ships in the same build — record it as a
deviation.

**Why:** the version-handshake standing rule — a rule change bumps `version:` and re-acks every
consumer in the same build, bipartite-consistent.

## F6 — deliberately untouched, verified so (the truthful-header check)

**`skills/vlt-setup/assets/workflows/vlt-review-council.js` — no edit.** Per disposition 4: the
workflow already returns `lensesFielded`, `degraded`, and the verdict enum; it never writes the
decision log; its `depends_on: []` header (`:11-15`) remains truthful (it still reads no
conventions) and it does not join `decision-log`'s `consumers:`. The builder verifies at rest that
the file is byte-identical to HEAD after the build (a diff, not a promise). Likewise **no edit** to
`skills/vlt-review-council/SKILL.md` — its `:46` already routes recording to `vlt-mint`, which is
where the mechanics now live; adding fallback prose there would be a second home.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row (a convention edit registers
nothing — `vlt-mint/SKILL.md:145`'s own rule). The registration-adjacent act this build *does*
perform is the handshake: `decision-log` 1→2 with the three-consumer walk (F1/F2/F5), verified by
`package-lint` Group E.

## Out of scope (dispositioned)

- **The Claude-Code-side harness condition** (workflow fan-out defaulting off in background jobs) —
  the filing itself declines to file it as module feedback ("fails this operation's module-source
  test"); the capture's scope note agrees. Not module source; nothing to build.
- **An inline degraded panel (option 3)** — rejected, disposition 1(c): self-review breaks lens
  independence and would re-home panel composition into prose (`vlt-mint/SKILL.md:80` retired
  exactly that).
- **A lint/package-lint check for the provenance facet** — rejected, disposition 3: no new finding
  class this arc; write-side enforcement, stated honestly in F1's Enforcement line. A later build
  that adds the check owes R3 its legal response and R2 its fixture case.
- **Backfilling historical decision-log entries** (including vlt-core's 2026-08-14 substituted
  entry) — forbidden by the schema's own append-only/no-backfill rule (`decision-log.md:56`);
  pre-@2 entries are honestly pre-facet.
- **The Arc-3 filing's remaining asks** (`2026-07-16-153000` §4-B mint-mode lens widening, §4-C
  thin-panel warning) — availability-adjacent but not A7-13's; that filing is tracked under its own
  arc's batch disposition, and folding its tail in here would widen a ruled narrow fix. Its §4-A is
  already shipped (build-22; disposition 6).
- **`frontmatter.md`** — untouched (A1 lockout; the facet needed no convention-frontmatter field,
  which is why this build never approaches the 7→8 reopen).
- **The A4-4 (5) inherited debt** — not re-scoped (disposition 7; discharged in B7-6).
- **Who reviews a *parked* mint's queue** (cadence/ownership of resuming parked mints) — the resume
  scan surfaces them on every activation (`:26`), which is the shipped mechanism; a
  cadence rule would be new governance beyond the narrow fix. Left to the field to file if the
  scan proves insufficient.

## Verification (unit, at rest)

1. **Single-home greps:** the provenance vocabulary strings (`council-degraded`, `user-ruled —
   panel not fielded`) appear in exactly one shipped file — `decision-log.md` (F1);
   `vlt-mint/SKILL.md` carries pointers to `{conventions}/decision-log.md` (*Verdict provenance*)
   and no restated value list; `vlt-review-council/SKILL.md` unchanged.
2. **Cross-file agreement greps:** F2's fallback paragraph, F3's exit-gate clause, and F4's
   planning-doc vocabulary agree on the two path names (park / user-ruled) and on the parked state
   string (`not fielded — <why>; parked`); the resume-scan sentence at `:26` still matches the
   planning-doc shape it scans for.
3. **Desk-check walkthrough (recorded in the build's verification):** the three environment cases
   each resolve to exactly one named path against the shipped text — (a) workflow available →
   Step 2a steps 1-4, `council` provenance with `lensesFielded`; (b) workflow unavailable +
   unattended → park, planning doc carries the state, `:26` resume offer picks it up (walk the
   text, confirm no step demands a verdict before the park); (c) workflow unavailable + user
   present and ruling → proceed, `user-ruled` provenance with a required why; and (d) the negative
   case — a context-substituted review — is nameable as illegal from `:102`'s amended text alone.
4. **Handshake bipartite re-check — the check of record is `package-lint` Group E**
   (`tools/package-lint.py`): `decision-log@2` — three consumers listed ↔ three acks current
   (`vlt-mint`, `vlt-upgrade`, `vlt-lint`), zero stray `decision-log@1` pins in `skills/`;
   `frontmatter@7` bipartite state unchanged, `vlt-review-council.js` header ack unchanged. A
   hand grep is an editing aid, never the recorded verification.
5. **Packaging lint:** mid-arc `uv run tools/package-lint.py` **A/B/C/E** green
   (D/`--expect-version` is B7-8's release gate, not this build's).
6. **R2 non-trigger shown, not assumed:** `git diff --stat tools/` empty;
   `uv run tools/test-package-lint.py` all cases green at 21/21; `CASE_FLOOR` 21 unchanged.
7. **F6 untouched-files check:** `git diff` shows no change to
   `skills/vlt-setup/assets/workflows/vlt-review-council.js` or
   `skills/vlt-review-council/SKILL.md`.
8. **Scrub:** no personal or vault-local content in any changed shipped file; worked examples use
   placeholder paths only (`_agent/mint/{YYYY-MM-DD}-{slug}.md` style); vlt-core's entry text is
   not quoted into any shipped surface. No `.decision-log.md` anywhere in the working tree at
   commit time.

No Release section — B7-7 is not the release build (B7-8 closes the arc and carries the dual
version bump and the `--expect-version` gate).

## Acceptance (live — appended to the roadmap ledger)

Four ship-verifiable checks, one field-contingent.

1. **[ship-verifiable]** `decision-log@2` handshake closed and bipartite-consistent — `package-lint`
   Group E passes at rest and inside the arc's pre-tag `--expect-version` run: three consumers
   listed, three acks at @2, zero stray @1 pins in `skills/`; `frontmatter@7` untouched and still
   bipartite-consistent; `vlt-review-council.js` byte-identical with its `depends_on: []` header
   ack intact.
2. **[ship-verifiable]** the named fallback coherent at rest — the recorded desk-check of the four
   environment cases (council fielded / unavailable-unattended → park / unavailable-attended →
   user-ruled / self-substitution → nameable as illegal from the shipped text), each resolving to
   exactly one named path across Step 2a, the `:102` exit gate, the planning-doc vocabulary, and
   the `:26` resume scan; cross-file greps agree on path names and the parked state string.
3. **[ship-verifiable]** provenance single-homed and honestly enforced — the three-form vocabulary
   lives only in `decision-log.md`'s *Verdict provenance* section; `vlt-mint` points and never
   restates; the convention's Enforcement section states the write-side-only posture (no new
   finding class shipped — the R3 declaration line); grep-checkable.
4. **[ship-verifiable — next ordinary upgrade, either vault]** delivery — the installed
   `_meta/conventions/decision-log.md` is @2 with the *Verdict provenance* section, installed
   `vlt-mint` carries the fallback branch, exit-gate clause, planning-doc vocabulary, and the
   `decision-log@2` ack; grep-checkable, bounded (the 0.10.0 upgrade happens anyway).
5. **[field-contingent]** the facet and the fallback observed on real gated mints — the first
   post-0.10.0 gated mint in a council-capable session records `verdict: … (council — lenses: …)`
   from the workflow's own return; and the first gated mint in a constrained session either parks
   (planning doc state + later resume) or records `(user-ruled — panel not fielded: <why>)` —
   nothing before 0.10.0 can produce either event, and no upgrade forces a gated mint. Producing
   vault: **vlt-core only** (owner-run; the factory cannot read it — evidence arrives as the
   owner's pasted decision-log entry / planning-doc lines). Calibration context rides here, never
   gates: vlt-core's 2026-08-14 substituted entry is the pre-facet exemplar the first `user-ruled`
   entry should be legible against. If unread by closeout it goes to the watch register, not the
   gate.
