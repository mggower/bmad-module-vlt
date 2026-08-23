---
title: 'Inbox Evolution Roadmap — Arc 8: the lifecycle arc — what the vault accumulates has no contract for aging'
status: 'CLOSED 2026-08-18 — the lifecycle arc. SHIPPED v0.11.0 2026-08-17 @ 86efd48, annotated tag v0.11.0 on the remote (builds B8-1..B8-5; new skills vlt-groom + vlt-decay, the deliver relay shape, frontmatter@8). ACCEPTANCE DISCHARGED over four acceptance-discharge runs 2026-08-18 against the vlt-core 0.10.0->0.11.0 own-the-apply (2026-08-17 18:10) plus post-upgrade field activity (rotate+drain f0538d2, grooms 0d80d25 + 2400dd9, the first vlt-dispatch ledger run, career sitting 9e6b949, pointer-integrity repair 84aea7c + e6d556b): ALL ship-verifiable checks across all five builds DISCHARGED (package-lint A/B/C/D/E exit 0); B8-1 TICKED complete (R3s first full field cycle — a check named its legal response, a maintainer performed it, the finding cleared); B8-2 (5) the vaults first deliver, B8-3 (5), B8-4 (4) and B8-5 (7)s integrity+ledger legs also discharged. Closed on an owner batch ruling 2026-08-18 over its field-contingent tails — 4 released as standing watches, 1 staged, 1 carried as inherited debt. **Only 1 of 5 ledger items is ticked; that count is NOT a measure of what the arc proved** — see the per-item annotations. Still open elsewhere: B8-2 (4) FAILED -> INHERITED DEBT to Arc 9, bound to seed a build at capture and to carry a [ship-verifiable] re-check so it GATES Arc 9 closeout (filing 2026-08-18-101612); B8-3 (6)+(7), B8-4 (5), B8-5 (6, flagged PASS-THROUGH with a re-examine-or-BLOCK instruction) released as standing watches; B8-5 (7) staged with a named action; ruling 4cs three lint-surfaced candidates BOUND MISSED (owner-filed, defaulting to Arc 9 capture); plus the inherited C6-c, the B5-3..B5-9 + pre-Arc-5 registers, Arc 7s five released watches, and Victors lifecycle-table frame candidate — authoritative list in this roadmaps Closeout record. All 4 filings HELD live (none archived — every derives_from filing has its own clause released, staged or carried, and released is not passed); 2 uncaptured filings await Arc 9 capture. **This arc is archived — do not append.**'
module_code: 'vlt'
created: '2026-08-17'
updated: '2026-08-18'
derives_from:
  - 'inbox/2026-08-16-093429-append-only-agent-files-have-no-decay-contract.md'
  - 'inbox/2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload.md'
  - 'inbox/2026-08-17-143641-partner-memory-has-no-promotion-ladder-or-staleness-contract.md'
predecessor: 'skills/reports/archive/inbox-evolution-arc7-roadmap.md (Arc 7 — CLOSED 2026-08-17, builds B7-1..B7-8 shipped v0.10.0)'
intent: >
  Arc 7 prosecuted "the vault does the legitimate thing and the module has nowhere to put
  it" at the level of single acts: a relay, a local convention, a council verdict. These
  three filings raise the same charge one level up, against time: the module solved write
  correctness (append-only, single-writer, commit-paired) and never gave anything it
  scaffolds a contract for aging. Records accumulate with no decay verb (A8-1), a partner's
  memory accumulates with no promotion or staleness rules so recorded knowledge stops
  binding (A8-3), and the one build that shipped mid-Arc-7 to give pathless traffic a home
  reproduced the miss inside itself within two days of field use (A8-2). Arc 8 also
  inherits a declared-not-built rule (R3) whose first live field instance is A8-2.
---

# Inbox Evolution Roadmap — Arc 8: the lifecycle arc

> **Status: open.** Capture run 1 (2026-08-17) grounded three filings against module source
> at `b117d81` (v0.10.0, working tree clean). Ideation not yet run.

## The through-line

All three filings were filed from vlt-core within 48 hours of the v0.10.0 upgrade, and they
read as one story: **the module's write discipline has no time axis.** Every durable surface
the module scaffolds was designed for correct *writes* — append-only, single-writer,
commit-paired — and each filing catches a different consequence of nothing ever being
designed to *age*:

- **A8-1** is the volume face: every operational file in the agent zone is a producer with
  no decomposer. Growth is linear with use and the read-side cost lands on every wake.
- **A8-3** is the routing face: partner memory has a write path but no promotion path, so a
  thread can be *small* and still fail — stale reads stacked atop live ones, rules recorded
  in a form that demonstrably does not bind. The two filings name each other and are
  deliberately not merged: rotation would shrink A8-3's files without fixing one mis-filed
  rule; a promotion ladder would route A8-1's mass without draining a byte.
- **A8-2** is the cautionary instance: B7-5 shipped *during Arc 7* precisely to give
  pathless traffic a legal shape, and within two days the field produced a legitimate act
  (unsolicited delivery, payload inline) that the new vocabulary still has no form for —
  the arc-7 through-line reproducing itself inside the build written to fix it. Its legal
  response cannot be performed, which makes it the first live field instance of **R3**
  ("no finding class ships without a stated legal response"), the rule Arc 7 declared and
  assigned to Arc 8 to build (archived Arc 7 roadmap, *Three standing rules*, R3 entry).

Cross-filing mechanics worth holding onto at ideation:

- **A8-1 ↔ A8-3 share machinery even though they refuse to merge**: both ride
  git-as-archive (every append already pairs with a commit, so compaction/retirement is
  never destruction) and the watermark idiom (`compacted-through:` generalizing dispatch's
  `routed through line N`; `archive:` frontmatter pointing at a pre-groom commit).
- **A8-3's proposed `reflexes.md` sits outside an existing enumeration**: the
  `partner_memory_bytes` vital sums exactly `identity.md` + `thread.md` + `capabilities/`
  (`skills/vlt-setup/assets/hooks/vlt-vitals.py:453`). A new always-loaded partner file
  added without widening that enumeration is the A7-3 manifest-scope failure again —
  whatever build ships a reflex layer must extend the vital in the same build (this is
  R2's shape, applied to a vital instead of a gate check).
- **A8-1's trigger half is already built**: the size metrics exist in the vitals table
  (`vlt-vitals.py:213-218`); what's missing is a wire and the decay verbs. Candidate (d)
  is far cheaper than filed.
- **A8-2 gates on (or ships with) the R3 build** — its fix *is* a stated-legal-response
  question, and R3's declared home (`vlt-lint/references/checks.md` per-check field) does
  not obviously cover a `vlt-dispatch`-side check; the R3 build must rule on that scope.

Not captured here but inherited into this arc's ideation pool from Arc 7's closeout
(authoritative list in the archived Arc 7 roadmap's Closeout record): the **R3 build**
(declared Arc 7, built Arc 8 — subject to R1: its build must carry an interim posture or
the declaration is withdrawn), **B7-4's ⚠ owner-review flag** (inherited debt, 1st arc),
three lint-surfaced module-feedback candidates, and two drift residues. None of these are
inbox filings, so capture does not grade them; ideation should seat them.

## Capture — 3 filings (grounded against module source at `b117d81`, 2026-08-17)

### A8-1. The agent zone's append-only files have no decay contract (2026-08-16) — `2026-08-16-093429-append-only-agent-files-have-no-decay-contract.md`

**Claim:** every operational file the module scaffolds into the agent zone is append-only or
grow-only with no retention/rotation/compaction contract; the module ships producers and no
decomposer, so growth is linear with use and the cost is read-side.

**GAP CONFIRMED, with one provenance correction and three sharpenings.**

- **The no-decay-contract claim holds across every cited surface.** The operating contract
  declares `{log}` "Append-only chronological operation record"
  (`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:36`, restated
  `:122`), and likewise `overlays` (`:41`), `upgrade_ledger` (`:44`), and `lint_reports`
  (`:47`). `vlt-lint` states retention out loud and declines it: lint reports are
  "append-only — never edit, prune, or re-read-to-rewrite past reports; **retention is the
  human's**" (`skills/vlt-lint/SKILL.md:72`). A repo-wide grep of the governance bundle for
  retention/rotation/compaction language finds decay machinery **only in the wiki lane**
  (consolidation/supersession/archive — `wiki-consolidation.md`, `wiki-supersession.md`)
  and the thread's prose-level set-aside. No agent-zone operational file carries any.
- **PROVENANCE CORRECTION — this is a deliberate deferral, not a design blind spot.** The
  filing's provenance guess ("lifecycle simply out of frame at design time") is wrong for
  the trigger half: the vitals reader ships four size metrics — `log_bytes`,
  `backlog_bytes`, `index_bytes`, `partner_memory_bytes` — each annotated "display-only
  size vital" (`skills/vlt-setup/assets/hooks/vlt-vitals.py:213-218`), and the code
  comment records the ruling: "Size vitals (disposition 8 — display-only; no rollover
  machinery)" (`vlt-vitals.py:441`). Lifecycle was in frame at the B5-9 enforcement-kit
  build and **deliberately deferred**. Likewise `tripwires.yaml` self-caps at two wires:
  "the alert-fatigue budget is a hard constraint; add a third only when a real failure
  earns it" (`skills/vlt-setup/assets/tripwires.yaml`, header). The filing *is* the
  claimed real failure — the seed text anticipated exactly this moment — but the build
  that acts on it is **revisiting a recorded prior disposition**, which is an owner ruling,
  not a routine fix. (The guess stands for the decay *verbs* themselves — no design record
  considers rotation/draining — just not for the measurement/trigger half.)
- **Sharpening 1 — candidate (d)'s cost collapsed at grounding.** The metric vocabulary the
  filing asks for already exists in the canonical METRICS table; a mass wire is a
  `tripwires.yaml` entry referencing an existing id, zero new metric code. What (d) still
  needs built is the age facet (nothing derives "fully-closed dispatch section older than
  N") and the scheduled-run execution half.
- **Sharpening 2 — the backlog has a `## Done` home, in-file.** The backlog schema defines
  `## Done` with `[resolved: <how>]`
  (`skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:210-211`). The
  filing's "resolved items have no archive destination defined" is imprecise: resolved
  items have a destination; nothing ever leaves the **file**. The gap is the exit, not the
  slot — which is the filing's real point, restated correctly.
- **Sharpening 3 — the "tend" verb partially exists as unenforced prose.** The contract
  already gives the thread a set-aside mechanism — "a faded entry moves to a `## Set
  aside` subsection **(or an archived thread note)**, never silently deleted"
  (`vault-operating-contract.md:195`) — and Beat 2's orient reads are explicitly bounded
  (last-5 slices, `:173`, with the ~25–85K vs ~1–2K measurement stated in-line). So the
  wake-read cost claim is narrower than filed: the *bounded orient* does not scale with
  vault age by design; what scales is everything that greps or reads whole files —
  dispatch drains and the ledger's whole-record greps, `thread.md` full reads (the bound
  is "## Thread only", not a size), and any human/whole-file read.
- **Vault-side measurements taken as reported** (259K log / 155K dispatch / 181K backlog /
  240K librarian memory at ~10 weeks): not verifiable from module source; internally
  consistent and nothing rests on their exact values.
- **Adjacency claim confirmed:** the 2026-07-29 boot-whale filings costed *shipped module
  text*; this is the runtime twin (vault-side data). Both tax the same wake budget.

**Candidate dispositions (a)–(d) and the filing's non-goals carried to ideation verbatim**
(retention-at-birth; the rotate/drain/tend three-verb taxonomy; git-as-archive +
idempotent-watermark safety model; tripwire-and-vitals triggering — with (d) re-costed per
Sharpening 1). The filing's weakly-held preference — (b)+(c) core, (a) durable convention,
(d) bell — is recorded, not adopted. **Open for the owner at ideation:** revisiting
disposition 8's display-only posture, and whether the alert-fatigue budget admits a third
wire.

### A8-2. The `handoff` shape has no form for a delivery whose payload is written inline (2026-08-17) — `2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload.md`

**Claim:** an unsolicited delivery with an inline payload has no legal relay shape; the
pointer-integrity finding it generates has a stated legal response that cannot be
performed; the ledger legacy-line denominator is unverifiable by a second reader.

**GAP CONFIRMED on all three counts — the cleanest-grounding filing of the batch.**

- **The vocabulary gap is real and exactly as filed.** `relay.md` defines exactly three
  shapes: `handoff` — "`handoff-path` **required**"
  (`skills/vlt-dispatch/references/relay.md:21`); `ask` — "no path … **`ref` required**"
  and it carries a question (`:22`); `answer` — "**`ref` required, and it must be the
  originating `ask`'s `ref`**" (`:23`). An unsolicited pathless delivery satisfies none.
  A `handoff` keyed by a `ref` is not merely discouraged — the key is defined per shape
  ("a `handoff` keys on its **doc path**", `:40`) and an "annotated `handoff` with no
  path on disk" is a named pointer-integrity finding
  (`skills/vlt-dispatch/references/ledger.md:25`). The field's seven `handoff`+`ref`
  relays are duly-flagged undefined forms, as filed.
- **The unperformable-legal-response claim holds.** `ledger.md:25` states the finding's
  only legal response: "the publishing partner re-fires the relay correctly keyed; the
  recipient checks the malformed line off as superseded." For this class there is no
  correct key to re-fire with — no path exists and no shape accepts a bare `ref` for
  unsolicited delivery. **This is the first live field instance of R3** ("no finding
  class ships without a stated legal response — every check names what a vault may
  legally do about it", declared in the archived Arc 7 roadmap's standing-rules section,
  build assigned to Arc 8). Capture flags for the R3 build: R3's declared home is a
  per-check field in `vlt-lint/references/checks.md`, but this finding class lives in
  `vlt-dispatch`'s ledger check — the R3 build must rule whether its home covers
  dispatch-side checks or R3 needs a second seat.
- **The A7-11/B7-5 history is accurate as filed:** B7-5's `ask`/`answer` pair covered
  *solicited* pathless traffic; unsolicited pathless delivery was left uncovered. The
  filing's own observation stands: the arc-7 through-line reproduced itself inside the
  build written to fix it, within two days of field use.
- **The attached lead (denominator ambiguity) is a confirmed textual gap.** `ledger.md:23`
  scopes the integrity check per **pointer line** ("for every pointer in a `relay:`
  block, resolve its key") while the legacy line counts "un-annotated **pathless**
  pointers" (`:26`) — but annotation is a **header**-level property (`relay.md:56`, the
  header "carries the shape when it is not `handoff`") and a path is a **line**-level
  property, so "un-annotated pathless pointer" genuinely does not resolve to one unit.
  Whether a payload `[[wikilink]]` counts as a path is likewise undefined for the legacy
  test (`relay.md:23` settles wikilinks only for `answer`'s *key*: "payload, never the
  key"). The filing's 37-vs-2-vs-18 irreproducibility is exactly what that ambiguity
  predicts. Small, self-contained fix: define the unit and the wikilink rule in
  `ledger.md`'s legacy-line paragraph.
- **Field disposition respected:** nothing retro-fixed, all seven drained; the owner read
  the signal as publish-side reflex, correct going forward. Consistent with `relay.md:27`'s
  no-backfill posture — capture concurs no history rewrite belongs in any build here.

**Candidate dispositions 1–4 carried to ideation verbatim** (widen `answer`; fourth shape
`deliver`/`note` keyed by `ref`; rule inline payloads illegal and require a doc; leave the
vocabulary and fix the legal response to annotate-in-place). Capture adds no preference —
but notes that option 3 pushes against the field's observed working habit, and that
whichever option ships must also update `ledger.md:25`'s legal-response sentence (single
home for the response is the check that renders the finding).

### A8-3. Partner memory has no promotion ladder or staleness contract (2026-08-17) — `2026-08-17-143641-partner-memory-has-no-promotion-ladder-or-staleness-contract.md`

**Claim:** partner memory (`identity.md` + `thread.md`) has a write path but no promotion
path and no staleness contract; corrections land on knowledge already recorded; reads
revise by stacking; there is no template slot for an always-loaded rule layer; partner
files sit outside lint scope.

**GAP CONFIRMED, with the existing partial machinery mapped precisely.**

- **No promotion ladder, no staleness contract — confirmed.** The partner-memory model's
  two homes are the operating contract's *Partner memory — identity and thread*
  (`vault-operating-contract.md:185-197`) and the frontmatter schemas
  (`frontmatter.md:170-200`). Between them the full lifecycle vocabulary is: identity is
  "evergreen … continuously updated", thread is "prunable … supposed to fade", and
  set-aside exists for *faded* inquiries (`:195`). Nothing distinguishes a durable rule
  from a revisable read from an episodic narrative; nothing states latest-form-only or
  retire-on-falsifier; no frontmatter field carries a staleness or promotion contract.
  The filing's core claim stands unreduced.
- **The wiring gap is confirmed at the template.** Beat 1 reads `identity.md` only
  (`skills/vlt-mint/assets/partner-agent-template.md:39`); Beat 2 reads `thread.md`'s
  `## Thread` (`:40`); "reflex" appears nowhere in the template. An always-loaded rule
  layer has no slot — the prototype's smuggle-into-identity workaround is accurately
  described.
- **Partner files outside lint scope — confirmed with an edge.** `vlt-lint`'s scope is the
  wiki lane (wiki + research + index; `skills/vlt-lint/SKILL.md:17,23,39`); `{partners}`
  is resolved there only to locate `capabilities/`, and the contract assigns lint exactly
  one partner-adjacent duty — capability `write_scope` and family invariants
  (`vault-operating-contract.md:207`). Thread/identity staleness, duplication-with-wiki,
  and rule-phrased-as-narrative are checked by nothing. (If disposition (f) ships, note
  A8-2's R3 flag: every new finding class needs its legal response stated at birth.)
- **The module already owns a two-tier ladder this filing generalizes** — worth naming as
  the design's native hook: "drift breathes, ratification reborns"
  (`vault-operating-contract.md:197`) is already a two-rung promotion ladder (`## Self`
  drift, ungated ↔ SKILL.md rebirth, council-gated) with entry criteria phrased as the
  partner's own test. Disposition (a)'s remark→…→wiki ladder extends an existing idiom,
  not a foreign one.
- **The enumeration trap (capture addition).** `partner_memory_bytes` sums exactly
  `identity.md` + `thread.md` + `capabilities/` (`vlt-vitals.py:453`); a shipped
  `reflexes.md` outside that enumeration silently under-reports the vital — the A7-3
  scope-as-enumeration failure recurring at a vital. Any build shipping disposition (b)
  widens the vital in the same build.
- **Vault-side evidence taken as reported** (the Rook triple-recurrence with its
  three-class self-analysis; the 4-versions-loaded revision stack; the 63% groom cut;
  `reflexes.md` prototype at vlt-core `b00db0a`): none verifiable from module source, and
  the filing correctly marks the prototype as vault-local evolution, not module source.
  The partner's three-class warning — "(a) is the easiest to fix and (c) is where the
  damage is" — is carried verbatim as the arc's honesty check on whatever ships.
- **Provenance guess graded:** plausible and consistent with grounding — the two-file
  split solved continuity and write safety; neither home carries any internal-economy
  rule; the template predates the enforcement-declaration discipline (its schemas carry
  no `enforcement_*` keys, which conventions now require of boundary-creating rules,
  `frontmatter.md:228+`). Unlike A8-1, no recorded prior disposition deferred this —
  here the out-of-frame guess stands.

**Candidate dispositions (a)–(f) carried to ideation verbatim** (typed promotion ladder;
reflex layer in the template; thread lifecycle rules at birth; correction as a typed
signal with corrections-per-sitting as the metric; a groom op, upstream not minted —
filing itself says it can wait for a second data point; partner files enter lint scope).
The filing's weakly-held preference — (b)+(c) at the template, (d) as behavior+metric,
(a) durable, (e)/(f) follow — is recorded, not adopted.

## Capture narrative — judgment calls this run made

- **Scope confirmed with the owner before grounding**: all three un-captured filings, per
  the default. The other 31 inbox files are prior arcs' captures awaiting field
  acceptance; the Arc 7 carry-forwards that are not inbox filings (R3 build, B7-4 ⚠ flag,
  3 lint-surfaced candidates, 2 drift residues) were seated in the through-line as
  ideation-pool context, not graded — capture grades filings only.
- **Arc numbering**: Arc 7 closed today; per the ship-day boundary rule these filings are
  Arc 8's, and 2026-08-16-093429 — filed post-ship, oddly absent from Arc 7's
  carry-forward list — is captured here on the same rule.
- **One provenance correction issued** (A8-1: the display-only size vitals are a recorded
  deliberate deferral, "disposition 8", not a blind spot — which reclassifies part of that
  build as revisiting a prior ruling, an owner call).
- **Two claims narrowed** (A8-1: backlog has a `## Done` home, the gap is the file exit;
  A8-1: bounded orient reads don't scale by design — the unbounded cost is in whole-file
  greps/reads), **one cost collapsed** (A8-1 disposition (d): metrics already exist), and
  **one hazard added** (A8-3/A8-1: `reflexes.md` outside the `partner_memory_bytes`
  enumeration — the A7-3 lesson applied forward).
- **A8-2 was tied to the R3 build at capture** — not a resolution, a dependency: its legal
  response question *is* an R3 question, and R3's declared home may not cover
  dispatch-side checks. Left for the R3 build to rule.
- **No design questions resolved.** All candidate dispositions carried verbatim; both
  weakly-held preferences recorded as the filers', not adopted.
- **Vault-side measurements in all three filings taken as reported** — none are verifiable
  from module source and none are load-bearing for the grounding verdicts.

**Superseding note (roundtable A15, 2026-08-17):** three contract cites in the capture are
off by one or four at `b117d81` — the set-aside sentence is `vault-operating-contract.md:196`
(cited `:195`); "drift breathes, ratification reborns" is `:198` (cited `:197`; the section
spans `:185-198`); lint's capability `write_scope`/family duty is `:211` (cited `:207`, which
is the shared-lane paragraph). The grounding verdicts stand; briefs re-ground per standing
practice and should not re-derive these corrections.

**Superseding note (B8-2 brief re-ground, 2026-08-17):** two precisions from the
commit-pinned evidence read (vlt-core `4f0656805c5946f30b4f9eed8e0b4df8939270a4`) and the
A5 sweep. (i) The read-before-brief pin's phrase "the seven malformed `handoff`+`ref`
relay blocks (the 2026-08-15 21:30–22:10 batch)" is imprecise: the seven findings are
**six** `(handoff, ref:)` blocks in that batch **plus one** `(handoff)`-annotated block at
20:35 carrying neither `ref` nor path — matching the filing's own "six of the seven carry
a `ref:`". Grounding verdicts unchanged. (ii) The A5 shape-enumeration sweep ("across
`vlt-dispatch/` outside `relay.md`") found two enumeration sites **outside**
`vlt-dispatch/` that would ship stale — `vault-operating-contract.md:242`'s "doc-less
`ask`/`answer` traffic" clause and `module-help.csv` row 11 — added to B8-2's scope as
grounding additions (brief F5/F6).

**Superseding note (B8-5 brief re-ground, 2026-08-17):** three precisions from the
post-B8-4 source read (branch `arc8-v0.11.0`, four builds after capture). (i) A10's
reader-list phrasing "the METRICS derivations in `vlt-vitals.py` (…, `spec_candidate`,
the consult-precondition check)" mis-homes the last two: `spec_candidate` and the
consult-precondition check are **`vlt-lint` governance checks**
(`vlt-lint/references/checks.md:47-48`) deriving from `_agent/dispatch.md` whole-record
reads, not vitals METRICS derivations — the enumeration mandate is unchanged and both are
in the brief's reader table; the brief's sweep also found two readers the A10 list
predates (`vlt-upgrade/SKILL.md:80`'s proto-spec retrofit relay-count, and the partner
Beat-2 open-slice greps in the template + three shipped partners), added as R-11/R-12.
(ii) The capture's vitals cites drifted under B8-3/B8-4: the size vitals are now
`vlt-vitals.py:213-219` (`partner_memory_bytes` includes `reflexes.md`), the partner
derivation loop `:449-461`, and the `:441` deferral comment is now the **discharge
comment at `:441-443`** — B8-4's carrier landed it self-contained per A12, and B8-5's
verify-present duty (ruling 1) is **discharged at re-ground and re-checked in its
acceptance check 4**. (iii) Candidate disposition (c) (the safety model) is **SHIPPED**,
not open — B8-3 seated the contract home (`vault-operating-contract.md:270-277`) per A6;
the brief cites it and builds nothing for it. Grounding verdicts otherwise stand.

**Next lifecycle move:** owner-steered **ideation** over A8-1..A8-3 plus the inherited
pool (the R3 build foremost — it is both a carried obligation and A8-2's dependency) —
grouping, order, and scope rulings recorded in this roadmap's Ideation rulings section;
then `build-brief` per ruled build. *(Skeleton laid below, 2026-08-17.)*

## Ideation rulings — A8-1..A8-3 + inherited pool (owner-steered, 2026-08-17)

Rulings below are the owner's; briefs cite this section, never re-litigate. **Session OPEN —
every slot below is unfilled.** *(superseded 2026-08-17, roundtable A15: the session closed
the same day — see the SESSION CLOSED record at this section's foot; every slot below is
filled. A fresh briefer reads one state, not two.)* The unresolved question pool for this batch is the
candidate-disposition and flagged-ruling material in this roadmap's own *Capture* section
(A8-1's dispositions (a)–(d) + non-goals, A8-2's dispositions 1–4, A8-3's dispositions
(a)–(f) — all carried verbatim, both filers' weakly-held preferences recorded but not
adopted) plus the cross-filing mechanics named in *The through-line* and the inherited
non-filing pool from Arc 7's closeout. Each question ends this session either ruled here,
or explicitly left to brief time, per build. A slot left empty is honest — do not fill it
with a guess, and do not let a brief infer one.

### Grouping & order

**RULED 2026-08-17 (owner accepted the clerk's drafted grouping as-is; clerk-drafts-
owner-amends mode, per the Arc-3/5/7 precedents). FIVE builds; numbering follows intended
ship order at assignment (a build that later slips does not renumber, per the Arc-3
convention); `B8-*` per the Arc-5 slug convention.** The draft was derived from this
session's eleven rulings, not proposed ahead of them.

| Build | Filings / pool items | Subject & notes |
|---|---|---|
| **B8-1** | R3 (pool, per rulings 4a + 3) | **The R3 retrofit.** Per-check legal-response field, homed where each check lives (ruling 3's generalized home): `vlt-lint/references/checks.md` for lint's checks, `vlt-dispatch/references/ledger.md` for pointer integrity, and any other check-bearing surface found at brief time. Opens the arc: every later build adds or changes a finding class and inherits R3's bar on landing. **R1 binds: the brief carries an interim posture for the window, or the R3 declaration is withdrawn.** *(roundtable 2026-08-17 — A3: the `ledger.md` pointer-integrity seat is stamped with the current response PLUS an explicit known-incomplete-pending-B8-2 marker (that marker is this check's R1 interim posture); B8-1 never rewords the response itself; window posture for the inline-delivery class: drain normally, no re-fire expected — B8-2 discharges the marker (same release preferred; otherwise the marker is field-visible and honest). A4: the walk is recorded as evidence — corpus (the shipped `skills/` tree), predicate, per-hit disposition table — so the acceptance check gains a denominator; the walk rules wires in or out of R3 explicitly: a vault-grown registry (`tripwires.yaml`, merge-by-id, `WIRE_REQUIRED_FIELDS`-enforced) takes no new required field — a wire's legal response homes in `surface_text` semantics, B8-1's ruled exception to the generalized home; the legal-response field is capped at one line per check (response, not rationale — rationale lives in the brief; `checks.md` is JIT-read whole every lint Step 2). A15: carries drift residue (i)'s rider — B8-1 deterministically touches shipped prose first.)* |
| **B8-2** | A8-2 (+ evidence debt 3) | **The delivery shape.** Legalizes unsolicited inline-payload delivery (options 1–4 open at brief time), updates `ledger.md:25`'s legal-response sentence under R3's regime, and defines the legacy line's unit + wikilink-as-path rule (debt 3). **Depends on B8-1** — it is R3's first field instance. Read-before-brief pin: the seven malformed relay blocks. No history rewrite (capture concurrence with the field disposition stands). *(roundtable 2026-08-17 — A5: the brief additionally rules the terminal legal state of the seven existing drained findings, with the no-history-rewrite binding scoped: it forbids retroactive re-keying/re-firing, never the performance of a legal response on a drained line (option 4 is thereby legal to consider); acceptance names a post-ship ledger run whose count for this class is zero or denominated-legacy. The brief exhibits the full act grid (solicited/unsolicited × doc'd/pathless, plus any axis the seven relays surface) and shows every cell has a legal shape or a reasoned exclusion — closure, not fit-to-the-seven, is the acceptance claim (the B7-5 lesson). A shape-enumeration sweep runs across `vlt-dispatch/` outside `relay.md` (SKILL.md's doc-less-ask/answer and shape/ref mentions, `ledger.md`'s header-annotation list), every hit dispositioned. The read-before-brief pin is commit-pinned to a vlt-core commit — the arc is about to teach the vault to compact that file.)* |
| **B8-3** | A8-3 contracts | **The memory contracts.** The promotion ladder / reflex layer / thread-lifecycle / correction-as-signal mix — dispositions (a)–(d) and (f) decided at brief time. **Widens `partner_memory_bytes` in the same build (R4).** Cites the safety model (cross-filing ruling 1). Read-before-brief pin: the vlt-core groom prototype + Rook's thread. *(roundtable 2026-08-17 — A8: FLOOR — B8-3 ships at minimum the contract surface B8-4's verbs target, as named vocabulary (promote / compress-to-latest-form / retire); the brief may not disposition the floor out without re-opening B8-4's seating. The vital clause is the conditional it means: **if** a reflex file (or any new always-loaded partner file) ships, `partner_memory_bytes` widens in the same build (R4). The reflex-load rule homes CONTRACT-SIDE (Activation ritual — the shipped, upgrade-refreshed surface every partner re-reads), the template mirroring it; template-only homing is ruled out (minted SKILL.md text is unpatchable — a template-only slot never reaches Rook or any existing partner); the brief states the adoption path for existing minted partners and the fleet's window posture (R1's shape at vault level). The brief also states: the pre-contract-material posture (contracts bind at-write going forward; existing material legal-until-groomed; (f) findings on pre-contract threads informational until the groom op exists in the vault's installed version — B8-3's R1 section); the two-file-model prose reconciliation sites (operating contract *Partner memory* + Beat 1, `frontmatter.md` *Partner memory*, the template's activation text, `vlt-setup`'s seeding/migration) alongside the R4 widening; n=1-evidenced rungs/caps ship with a named falsifier + `review_after:`, and B8-4's first field runs are named as the calibration evidence that may amend those rungs without re-opening ideation; acceptance checks are class-tagged per the partner's (a)/(b)/(c) taxonomy — class (c) recorded watched-not-covered unless a mechanism names how it reaches it; an (f) finding class whose legal response is the groom carries an R1 interim posture or sequences after B8-4; if (b) ships without (f), the reflex cap's enforcement declaration or R1 posture is stated — the cap may not ship silent. A7: B8-3 owns the single `frontmatter.md` bump defining BOTH safety-model watermark fields (`archive:` + `compacted-through:`), with its consumer re-ack; any further B8-5 schema rule change carries its own explicitly-named bump — neither brief may assume the other.)* |
| **B8-4** | A8-3 disposition (e) (per evidence debt 2) | **The groom op — the arc's motivating deliverable.** Its own build: it grooms *toward* B8-3's rules (depends on B8-3) and must not sink with B8-3's convention weight. Approval-gated diff (bond material is intimate; never silently deleted), under the safety model. Upstream op, not minted. *(roundtable 2026-08-17 — A9: ≥1 SHIP-VERIFIABLE acceptance check is mandated — the groom run end-to-end against a factory fixture partner producing its approval-gated diff — so the motivating deliverable gates closeout (the A4-4(5) lesson; Arc 7's A3 was the cure). The diff renders grouped by B8-3's shipped disposition types, one-line rationale per item, approvable per class — a monolithic ~30K deletion wall is not review. Brief-time questions gain: the LEGAL WRITER (the contract's own-zone single-writer rule cited as the constraint the answer must satisfy; the upstream-op ruling stands, the brief reconciles), and the DECLINE disposition (what a declined hunk records; whether declined material is excluded from or re-argued at the next groom — the lint-has-no-memory precedent predicts re-proposal turning the gate into ceremony). Owner-ruled at the roundtable (D2): B8-4's brief is the decide-once home for the hygiene-execution idiom, AND its interim default is invoked-only unless the brief argues otherwise; B8-5 adopts or records an owner-ruled divergence. The `vlt-vitals.py:441` comment update rides B8-4's brief (first ship-order build that retires recorded content); B8-5 verifies it present. B8-4's own read-before-brief pin: the full pre/post-groom state at vlt-core `b00db0a`.)* |
| **B8-5** | A8-1 | **The decay contracts.** Rotate/drain verbs, retention-at-birth, and the mass/age wire — legal under pre-ideation rulings 1–2 (disposition 8 reopened; third wire admitted). Cites the safety model; disposition mix (a)–(d) + the filing's non-goals decided at brief time. Last: widest surface, and it gains from watching B8-3/B8-4 exercise the safety model first. *(roundtable 2026-08-17 — A10: the tend verb for partner memory resolves by pointer to B8-4's groom op (single home); B8-5 ships rotate/drain machinery only, no second thread mechanism. The brief enumerates every derive-first reader of each file a verb touches — the METRICS derivations in `vlt-vitals.py` (`ingests_since_lint`, `days_since_lint`, `spec_candidate`, the consult-precondition check), `vlt-lint` Step 0's `{log}` baseline grep (missing header → silent full-mode fallback, the whale the arc exists to shrink), dispatch whole-record greps (`open_pointers`, relay idempotency) — and states each one's rotation-safety invariant (e.g. rotation never crosses the newest lint header; drains move only fully-closed sections), with a ship-verifiable fixture check: rotate a fixture log, re-run the reader, counts hold. Prose reconciliation: every shipped sentence the verbs falsify (`vlt-lint/SKILL.md:72`'s "retention is the human's", the contract's structure-table Append-only declarations) is updated or deliberately reaffirmed, per surface. Newborn sweep: every file class B8-1..B8-4 introduced is covered by retention-at-birth or exempted with a one-line reason. Per size vital, the build rules whether archived siblings count toward the metric, in the same build the verb ships.)* |

**Residue (i)'s rider** (`vlt-upgrade/SKILL.md:134` third adoption wording, ruling 4d)
attaches at brief time to whichever build first touches `vlt-upgrade` or shipped prose.
*(roundtable A15, 2026-08-17: resolved — B8-1 is the carrier; it deterministically touches
shipped prose first, and a floating condition invites five narrow readings and an untouched
residue.)*

**Cross-build (roundtable A13, 2026-08-17):** any Arc 8 build that creates a new
accumulating file states that file's decay contract in its own brief (formalized to
disposition (a)'s frontmatter form once B8-5 ships) — the arc may not mint fresh no-decay
accumulators inside the arc that exists to end them.

### Pre-ideation rulings the capture demanded

1. **Disposition 8 revisit (A8-1)** — the display-only size vitals are a *recorded
   deliberate deferral* ("no rollover machinery", `vlt-vitals.py:441`). Does the owner
   reopen it? **RULED 2026-08-17 (owner): REOPEN FULLY.** A8-1's build may ship
   rollover/decay machinery (rotation, drains, compaction) — the deferral is discharged
   by field evidence. The `vlt-vitals.py:441` comment updates to record the discharge
   (pointing here) in whatever build first ships machinery, so the code stops asserting
   a deferral that no longer stands. *(roundtable A12, 2026-08-17: the comment records the
   discharge SELF-CONTAINED — date + evidence, e.g. "display-only deferral discharged by
   field evidence (filing 2026-08-16, Arc 8)" — never a factory-internal path;
   `skills/reports/` is gitignored and unresolvable from the public repo or any install.
   Carrier named per A9: the update rides B8-4's brief, B8-5 verifies it present.)*
2. **The third wire (A8-1)** — `tripwires.yaml` self-caps at two wires on an alert-fatigue
   budget, "add a third only when a real failure earns it." Is this filing that failure —
   does the budget admit a mass/age wire? **RULED 2026-08-17 (owner): YES — A8-1 is the
   earned failure.** A mass/age wire joins the seed; the seed header's bar ("a real
   failure earns it") is met by the filing's field evidence, and the header text stays —
   the bar governs any *fourth* wire the same way. *(roundtable A11, 2026-08-17: two
   refinements. The admission is the decay-contract wire CLASS — the wires B8-5's brief
   derives from its shipped verbs (each `tripwires.yaml` wire keys exactly one canonical
   metric id, and mass and age cannot key one wire), count and thresholds at brief time
   with the alert-fatigue budget re-judged there; the header's bar governs wires outside
   the class. And "the header text stays" means the BAR sentence stays — the count/ordinal
   wording ("two stock wires" / "a third") updates in the same build that adds a wire,
   else the ruling ships stale prose of the exact class B7-8 swept.)*
3. **R3's home vs dispatch-side checks (A8-2)** — R3's declared home is a per-check field
   in `vlt-lint/references/checks.md`; A8-2's finding class lives in `vlt-dispatch`'s
   ledger check. Does R3's home cover dispatch-side checks, or does R3 need a second seat?
   **RULED 2026-08-17 — owner-delegated to the clerk, recorded as owner-adopted per the
   Arc-5/Arc-7 delegation precedent; overturnable (clerk supplied the reasoning):
   GENERALIZE — the field lives where the check lives.** R3's home becomes a rule, not a
   file: every check's own single home carries the legal-response field (`checks.md` for
   lint's checks, `ledger.md` for dispatch's pointer-integrity check, and so on for any
   future check-bearing skill). Reasoning: R3's declared text already binds *every* check;
   single-home discipline puts a legal response beside the check that renders the finding
   (capture already treats `ledger.md:25` as that single home); a named-seat list would be
   an enumeration claiming completeness — the drift class the standing rules refuse. The
   R3 build's brief restates its home accordingly.
4. **Seating the inherited pool** — which of Arc 7's non-filing carries join Arc 8 builds:
   the **R3 build** (subject to R1: its build must carry an interim posture or the
   declaration is withdrawn), **B7-4's ⚠ owner-review flag** (inherited debt, 1st arc),
   the **3 lint-surfaced module-feedback candidates**, the **2 drift residues**? Each:
   joins a build / stays carried / files as an inbox filing first.
   **RULED 2026-08-17 (owner), per item:**
   - **(4a) The R3 build JOINS ARC 8 as a build.** Scope per ruling 3's generalized home
     (the legal-response field lives where each check lives); merge-vs-sequence with
     A8-2's build is a grouping call. R1 binds: its brief carries an interim posture for
     the window, or the declaration is withdrawn.
   - **(4b) B7-4's ⚠ owner-review flag: REVIEWED IN-SESSION, this date** — the owner
     elected to discharge it live rather than carry or schedule. The review's outcome is
     recorded in its own subsection below (*B7-4 ⚠ flag — in-session review*), which is
     the flag's discharge record.
   - **(4c) The three lint-surfaced candidates FILE TO INBOX FIRST** — each becomes a
     proper dated filing (owner's vault-side report is the source), grounded in a capture
     run 2 before any build folds them in. They are not Arc 8 scope until captured.
     *(roundtable A15, 2026-08-17: filer = owner; bound = before Arc 8's release; capture
     run 2's output defaults to Arc 9 capture unless the owner reopens Arc 8 ideation by
     explicit ruling — the candidates no longer sit on a rail with no destination.)*
   - **(4d) Drift residue (i) (`vlt-upgrade/SKILL.md:134` third adoption wording) rides
     as a RIDER on whichever Arc 8 build first touches `vlt-upgrade` or shipped prose** —
     named in that build's brief, not a build of its own. Drift residue (ii) needs no
     seat: it is A8-2's attached lead, already captured there.

### B7-4 ⚠ flag — in-session review (2026-08-17, per ruling 4b)

The owner reviewed the three flagged B7-4 brief dispositions live (the flag's terms: review
disposition 1's reconstruction and the reserved-question rulings in dispositions 6/7 and 8;
originally due at the v0.10.0 release, carried 1 arc). Each was presented with its shipped
reasoning and alternatives from `skills/reports/archive/build-B7-4-the-seam.md:62-194`:

- **Disposition 1 (matrix ruled lost; decision space re-derived): UPHELD.** The
  reconstruction posture stands, including its own rule: a resurfaced matrix that
  contradicts a ruling is a filing, never a silent re-cut.
- **Disposition 6 (contract records the designed-read pattern + the skill-overlay veto's
  reasoning): UPHELD.** The adopted clerk recommendation is now owner-confirmed; the
  soften-or-cut option lapses.
- **Disposition 7 (A1 reopen not invoked; governed-class prose declaration;
  `frontmatter` stays @7): UPHELD.** The reopen remains available only to a build proving
  genuinely per-file variance.
- **Disposition 8 (sanctioning test = ref-keyed mint entry; unminted files keep flagging
  `baseline_missing`): UPHELD.** The keep-flagging consequence is confirmed as a feature.

**The B7-4 ⚠ owner-review flag is DISCHARGED 2026-08-17 — nothing files forward from it.**
This subsection is the discharge record; Arc 8 carries no B7-4 debt.

### Cross-filing decide-once rulings

1. **The shared safety model (A8-1 ↔ A8-3)** — both filings ride git-as-archive
   (compaction/retirement is never destruction; every append already pairs with a commit)
   and the watermark idiom (`compacted-through:` / `archive:` pointers generalizing
   dispatch's `routed through line N`). Ruled once as one safety model both builds cite,
   or per-build? **RULED 2026-08-17 (owner): RULE ONCE — this paragraph is the single
   home.** The Arc 8 safety model: *hygiene and grooming acts are never destruction —
   every append already pairs with a commit, so raw content retires by reference
   (git-as-archive / `archive:` pointers / moves to `{archive}`), interpretive digests
   only add, and progress state lives in the files' own watermarks
   (`compacted-through:` generalizing dispatch's `routed through line N`), never in a new
   ever-growing ledger.* The A8-1 and A8-3 builds cite this ruling; briefs never restate
   it. *(roundtable A6, 2026-08-17 — three clauses added, this paragraph amended as the
   model's current home: (i) HOME SPLIT — this paragraph is the factory single home only
   until first ship; B8-3, the first citing build in ship order, seats the model's shipped
   text in the operating contract (a hygiene-safety section) and defines both watermark
   fields (`archive:`, `compacted-through:`) in one `frontmatter.md` bump; B8-4/B8-5 cite
   the shipped home; this paragraph then becomes the factory-side pointer — a field vault
   performing a groom must be able to cite the rule it acts under. (ii) mechanical /
   lossless-by-reference acts are council-free; INTERPRETIVE rewrites are legal only as an
   approval-gated diff with the pre-state reachable via the `archive:` pointer — A8-1's
   "no in-place LLM rewriting" non-goal accordingly reads "no *ungated* in-place
   rewriting", dissolving the B8-4/B8-5 contradiction. (iii) DERIVABILITY — a decay act
   must keep every derive-first consumer correct: the retained tail provably contains the
   consumer's full derivation window, or the consumer is widened to read the archive, in
   the same build (R2's shape applied to derivations; without this, a drain manufactures
   false `consult_missing` findings whose legal response an already-consulted vault cannot
   perform — the arc reintroducing its own R3 fault class).)*
   *(Shipped-home marker — build-B8-3, 2026-08-17: the model's shipped text is seated in the
   operating contract's **"Hygiene and grooming — the safety model"** section (all three A6
   clauses), with both watermark fields defined once in `frontmatter.md`'s *Hygiene
   watermarks* under the single 7→8 bump; per A6 clause (i) this paragraph is henceforth the
   **factory-side pointer** — B8-4/B8-5 cite the shipped home, not this paragraph.)*
2. **The enumeration-widening rule (A8-3 ↔ A8-1, the A7-3 lesson forward)** — any build
   that adds an always-loaded partner file or a new accumulating file widens the
   corresponding vital's enumeration (`partner_memory_bytes`, `vlt-vitals.py:453`) in the
   same build. Enshrine as a standing rule (R2's shape applied to vitals), or handle
   per-build? **RULED 2026-08-17 — owner-delegated to the clerk, recorded as
   owner-adopted per the delegation precedent; overturnable (clerk supplied the
   reasoning): ENSHRINE, as standing rule R4** (numbering continues Arc 7's R1–R3):
   *a build that adds a file to a class an existing vital or manifest enumerates —
   always-loaded partner files, accumulating agent-zone records, skill assets — widens
   that enumeration in the same build.* **Home: `build-brief`** (a required brief
   section, R1's home and shape — factory-binding, not a shipped check, so R3's
   legal-response bar does not yet apply). Reasoning: the class has bitten twice at ship
   (A7-3's manifest, C6-d's `references/`/`scripts/`) and recurred at capture within one
   arc (`reflexes.md` vs `partner_memory_bytes`); per-build handling depends on each
   brief-writer independently remembering the trap, which is the failure mode R2 was
   written against. The mechanical half (a lint case keying vitals enumerations to the
   structure contract) is left to a build that wants it — R4 binds briefs today.
   *(roundtable 2026-08-17 — A1: the home now EXISTS ON DISK. The roundtable found —
   unanimously, twelve voices — that R4's named home held neither R4 nor the R1 precedent
   it cites: R1's Arc-7-declared `build-brief` section was never written, and R1 had bound
   by memory for a full arc. Owner-ruled in-session (D3): the R1 interim-posture and R4
   enumeration-widening required sections were written into `build-brief`
   (`references/brief-anatomy.md` §3 and §7, plus an Exit-gate presence check) at this
   roundtable; arc closeout re-checks by the same grep that failed today. A2 — R4's
   recorded text is amended in two places: the em-dash list is ILLUSTRATIVE ("e.g." — the
   enumeration itself, or one a build's own walk establishes, is the class test; a list
   read as membership is the drift class the rule legislates against), and a brief may
   DECLARE a new file outside the enumerated class with reasoning recorded — a declared
   exclusion, never a silent omission; files retired to cold storage under ruling 1's
   safety model are outside live-read enumerations by design (vitals measure wake-read
   mass, not vault mass).)*
3. **Volume vs routing stay separate (A8-1 / A8-3)** — both filings deliberately refused
   to merge (rotation fixes no mis-filed rule; promotion drains no bytes). Accept the
   filers' separation as binding on grouping, or overrule? **RULED 2026-08-17 (owner):
   BINDING — separate builds.** Grouping may not fold A8-1 and A8-3 into one build;
   shared machinery is handled by ruling 1's safety model, not by merging.
4. **The lint-scope split (B8-3(f) ↔ B8-5) — added at the roundtable (A14, 2026-08-17):**
   staleness / duplication-with-wiki / rule-phrased-as-narrative finding classes on
   partner files are disposition (f)'s lint territory; mass/age machinery is B8-5's
   sibling hygiene per A8-1's traveling non-goal ("a sibling of `vlt-lint`, not folded
   into its wiki niche"). Neither brief may re-rule the split — without this line, two
   independently-written briefs could cut the lint boundary in opposite directions
   within one arc.

### Spike obligations

**RULED 2026-08-17 (owner): NO SPIKES** — all three filings ground against internal module
source; no external unknown exists in this batch. **Two read-before-brief pins bind
instead** (the Arc 7 idiom; obligations to read primary evidence, not summaries):

- **A8-3's brief**: read the actual vlt-core groom prototype (`reflexes.md` and the
  pre/post-groom state at vlt-core `b00db0a`) and Rook's thread carrying the three-class
  self-analysis — never work from the filing's summary alone.
- **A8-2's brief**: read the seven malformed `handoff`+`ref` relay blocks in vlt-core's
  `_agent/dispatch.md` (the 2026-08-15 21:30–22:10 batch) — the actual traffic the new
  shape must legalize.

### Evidence-debt dispositions

1. **Vault-side measurements taken as reported** (A8-1's file sizes at ~10 weeks; A8-3's
   Rook triple-recurrence, 4-version stack, 63% groom cut) — none verifiable from module
   source, none load-bearing on grounding verdicts. **RULED 2026-08-17 (owner):
   NOT-BLOCKING.** Recorded as sizing urgency only; no re-measurement obligation created
   (the builds' own acceptance checks define their measured outcomes).
2. **A8-3's groom op second data point** — the filing itself says disposition (e) "can
   wait for a second data point"; the manual pass exists once (vlt-core `b00db0a`).
   **RULED 2026-08-17 (owner): THE GROOM OP SHIPS THIS ARC — the filing's wait-lean is
   overruled, with reasoning on record: the groom capability is what prompted kicking off
   Arc 8 now; it is the arc's motivating deliverable.** Grouping seats disposition (e)
   accordingly (in the A8-3 build or a dedicated build — a grouping call). The filing's
   own guardrail travels with it: the groom produces an approval-gated diff (bond
   material is intimate; never silently deleted), under the cross-filing safety model.
3. **A8-2's denominator lead** (37-vs-2-vs-18 irreproducibility) — confirmed textual
   ambiguity in `ledger.md:26`; the check it serves passed. **RULED 2026-08-17 (owner):
   FOLD INTO THE A8-2 BUILD** — same file and section; the brief defines the legacy
   line's unit (block vs pointer line) and whether a payload `[[wikilink]]` counts as a
   path.

### Questions deliberately left to brief time

**DESIGNATED 2026-08-17 (owner), per build:**

- **B8-1**: which surfaces beyond `checks.md` and `ledger.md` carry checks (found by
  walking, not listing); the interim posture's exact text (R1).
- **B8-2**: the shape choice, options 1–4 (capture's note stands: option 3 pushes against
  the field's observed habit; whichever ships updates `ledger.md:25` in the same build).
- **B8-3**: the disposition mix (a)–(d) + (f); the reflex-file cap; how far the ladder's
  rungs formalize. The partner's three-class honesty check binds the brief's claims —
  "(a) is the easiest to fix and (c) is where the damage is"; the brief must state which
  classes its mechanisms reach and not let the easy fixes claim class (c).
- **B8-4**: trigger model (scheduled vs invoked); diff-approval surface; what of the
  manual prototype's method is codified vs left to judgment.
- **B8-5**: the disposition mix (a)–(d); the wire's metric/threshold; the filing's
  non-goals list travels into the brief verbatim (no in-place LLM rewriting of records;
  no binary compression; no new ever-growing hygiene ledger; hygiene is a sibling of
  `vlt-lint`, not folded into its wiki niche).

**SESSION CLOSED 2026-08-17 — every slot above is filled:** four pre-ideation rulings
(disposition 8 reopened; the third wire admitted; R3's home generalized; the pool seated
4a–4d), the B7-4 ⚠ flag reviewed in-session and DISCHARGED (all four dispositions upheld),
three cross-filing rulings (safety model ruled once; **R4 enshrined**; separation binding),
spikes closed empty with two read-before-brief pins, three evidence debts dispositioned
(including the owner's overrule seating the groom op as the arc's motivating deliverable),
grouping & order ruled (**five builds, B8-1..B8-5**), and the remaining pool designated to
named briefs. **Two rulings were owner-delegated to the clerk** and are recorded as
owner-adopted per the delegation precedent, both overturnable: R3's generalized home
(ruling 3) and R4 (cross-filing 2). Grouping was accepted from the clerk's draft as-is
(clerk-drafts-owner-amends). Mid-session the owner gave standing process feedback —
decision context must be surfaced in-chat, not compressed into option cards — recorded to
project memory (`ideation-full-context-in-chat`) and applied from the spikes/debts rulings
onward.

## Roundtable review — Arc 8 ideation batch (2026-08-17)

**Convened** per lifecycle step 4 over the closed ideation rulings above. Roster: the full
installed room — Mary (analysis), Winston (architecture), Amelia (engineering), John
(product), Paige (documentation), Sally (UX), Carson (ideation), Dr. Quinn (systems),
Maya (design thinking), Victor (strategy), Caravaggio (visual communication), Sophia
(narrative); the owner excused nobody and declared no pre-hunt joints. Twelve parallel
hunts returned ~80 raw findings merging to the resolutions below; session file at
`_output/party-mode/2026-08-17-arc8-roadmap-roundtable-session.md`, keepsake at
`_output/party-mode/2026-08-17-arc8-roadmap-roundtable.html`. **No OPEN disputes.**

**Amendments (all applied in-session, markers in the sections they amend):**

- **A1** — `build-brief` factory edit applied at the roundtable: R1 interim-posture and R4
  enumeration-widening required sections written into `references/brief-anatomy.md` (§3,
  §7) + an Exit-gate presence check; the roundtable found R1's Arc-7 home was never
  written (R1 bound by memory for one arc). Landed in cross-filing ruling 2's marker.
- **A2** — R4 text: em-dash list marked illustrative; declared-exclusion clause added
  (cold storage outside live-read enumerations by design). Ruling 2 marker.
- **A3** — B8-1/B8-2 seam: pointer-integrity seat stamped known-incomplete-pending-B8-2
  (that marker = the check's R1 posture); window posture for the inline-delivery class.
  B8-1 row.
- **A4** — B8-1 depth: walk recorded as evidence with a denominator; wires ruled in/out of
  R3 (vault-grown registry takes no new required field); field capped one line/check.
  B8-1 row.
- **A5** — B8-2 depth: terminal state for the seven drained findings + binding scope
  defined; act-grid closure as the acceptance claim; shape-enumeration sweep; evidence
  pin commit-pinned. B8-2 row.
- **A6** — safety model gains three clauses: shipped home via B8-3 (contract text + both
  watermark fields in one bump); gated-interpretive-rewrite sentence (dissolves the
  B8-4/B8-5 contradiction); derivability clause (decay keeps every derive-first consumer
  correct, same build). Cross-filing ruling 1 marker.
- **A7** — frontmatter coordination: B8-3 owns the safety-model-fields bump; any B8-5
  schema change carries its own named bump. B8-3 row.
- **A8** — B8-3 package: floor for B8-4 (named promote/compress/retire vocabulary);
  conditional vital widening; reflex-load rule homes contract-side (template-only ruled
  out — unreachable by the minted fleet); existing-fleet adoption path + window posture;
  pre-contract-material posture; two-file prose reconciliation; n=1 rungs carry falsifier
  + `review_after:` with B8-4's runs as calibration; class-tagged acceptance (class (c)
  watched-not-covered unless reached); (f)-groom R1 posture; cap may not ship silent.
  B8-3 row.
- **A9** — B8-4 package: ≥1 ship-verifiable check (fixture groom → gated diff); diff
  grouped by B8-3's types, approvable per class; legal-writer + decline-disposition brief
  questions; `vlt-vitals.py:441` comment carrier named (B8-4, B8-5 verifies); pin split
  (B8-4 reads `b00db0a` pre/post state). B8-4 row.
- **A10** — B8-5 package: tend resolves by pointer to B8-4's groom; derive-first reader
  enumeration + rotation-safety invariants + fixture check; prose-reconciliation list;
  newborn sweep of B8-1..B8-4's file classes; per-vital exit-side ruling. B8-5 row.
- **A11** — tripwire ruling refined: decay-contract wire CLASS admitted (count at brief
  time); bar sentence stays, count wording updates same build. Pre-ideation ruling 2
  marker.
- **A12** — vitals comment self-contained (date + evidence), never a factory path.
  Pre-ideation ruling 1 marker.
- **A13** — cross-build newborn rule: any Arc 8 build creating an accumulating file states
  its decay contract in its own brief. After the grouping table.
- **A14** — lint-scope split decided once: partner-file finding classes = (f); mass/age =
  B8-5's sibling machinery. New cross-filing ruling 4.
- **A15** — housekeeping: stale "Session OPEN" sentence superseded; capture cite
  corrections (three off-by-N contract cites); ruling 4c gains filer/bound/destination;
  residue (i)'s rider resolved to B8-1; `## Deferred acceptance ledger` seeded below
  (build-brief's exit gate previously had no append target).

**Rules:** no new standing rule numbers minted; the session's rule work was landing R1 and
R4 in their declared home (A1) and amending R4's recorded text (A2).

**Disputes — all owner-ruled live, none OPEN:**

- **D1 (sequencing):** John moved to sever (f) from B8-3 so the B8-3→B8-4 groom track
  could run parallel to B8-1→B8-2 and the motivating deliverable ship earlier. **Owner
  ruled: the five-build order stands** (the floor amendment protects B8-4; B8-5 watches
  the safety model exercised first). *Dissent on record (John): queuing the arc's
  motivating deliverable fourth behind an overloadable B8-3 risks the arc's value if it
  stalls.*
- **D2 (B8-4 trigger):** Maya moved to pre-rule invoked-only; Carson moved to leave the
  idiom to the brief as its decide-once home. **Owner ruled: the composed option** —
  B8-4's brief is the decide-once home for the hygiene-execution idiom AND its interim
  default is invoked-only unless the brief argues otherwise; B8-5 adopts or records an
  owner-ruled divergence.
- **D3 (factory-edit timing):** in-session vs rider on B8-1. **Owner ruled: in-session,
  now** — the edit landed at this roundtable (A1); closeout re-checks by the grep that
  failed today.

**Out-of-scope material for `inbox/` (captured, not debated):** Victor's frame candidate —
a single shipped lifecycle convention (every agent-zone file class declares its
decay/promotion posture in one table) as the eventual replacement for per-build contract
accretion; file if a ninth-arc filing repeats the pattern.

**Next lifecycle move:** `brief build B8-1` (`build-brief`).

## Deferred acceptance ledger

*(Seeded empty at the roundtable (A15, 2026-08-17) so `build-brief`'s exit gate has its
append target — per-build `- [ ]` bullets land here as briefs complete, tagged
ship-verifiable or field-contingent per `build-brief` §9.)*

- [x] **build-B8-1 (r3-retrofit, briefed 2026-08-17):** (1) [ship-verifiable] every
  check entry in the shipped `checks.md` carries exactly one one-line legal-response
  marker — 25 there + 1 in `ledger.md`, matching the brief's walk denominator (26
  entries, 2 no-marker rows); (2) [ship-verifiable] `ledger.md`'s pointer-integrity seat
  carries the unchanged response plus the known-incomplete-pending-B8-2 marker, and the
  marker's only legal terminal states are field-visible-in-release or discharged by
  B8-2 — no silent third state; (3) [ship-verifiable] `tripwires.yaml`'s `surface_text`
  semantics sentence present, `WIRE_REQUIRED_FIELDS` unchanged — an existing vault's
  registry merges clean on the next upgrade; (4) [ship-verifiable] residue (i) closed —
  the third adoption wording in `vlt-upgrade/SKILL.md`'s ledger template matches the
  canonical Step-4 wording, drifted phrase greps to zero across `skills/`;
  (5) [field-contingent — vlt-core] on the first post-upgrade lint/`ledger` run
  rendering ≥1 finding, the maintainer performs (or explicitly declines) the response
  named at the check without leaving the file — the inline-delivery class exempted by
  its marker until B8-2's discharge.

  **Discharge run 2026-08-18 (evidence: vlt-core 0.10.0→0.11.0 own-the-apply
  2026-08-17 18:10, upgrade-ledger entry).** Upgrade-side DISCHARGED 2026-08-18:
  (1) `grep -ci "legal response" vlt-lint/references/checks.md` = 26 (25 markers +
  the pre-existing :45 worked example, per the brief's reconciled denominator) and
  `vlt-dispatch/references/ledger.md` = 1 — the walk denominator holds; (2) B8-2
  discharged the marker in the same arc (see B8-2 (2) below), so the seat's only
  terminal state was exercised, not left silent; (3) `tripwires.yaml:21` carries the
  `surface_text` semantics sentence and the vault's 0.11.0 registry merged clean by id
  (upgrade-ledger: "2 wires added: log-mass, drain-due; local wires + thresholds kept");
  (4) drifted phrase greps to 0 across shipped `skills/` (reports/ excluded).
  **STILL-OPEN: (5)** — no post-upgrade `vlt-lint` or `vlt-dispatch ledger` run has
  occurred on vlt-core (last full lint 2026-08-16 11:18, pre-upgrade), so no rendered
  finding has yet met a maintainer at the check. *Trigger: the next vlt-core lint or
  ledger run (owner/partner-initiated).*

  **Update — discharge run 2 (2026-08-18, `vlt-dispatch ledger` run).** The triggering
  event fired. **(5) render leg DISCHARGED:** the run rendered 2 pointer-integrity
  findings and each carried its legal response inline at the check — finding 1 states
  "Legal response: the Researcher re-fires it correctly keyed (a `deliver` with a
  publisher-chosen ref fits the payload better than `ask`); Gwyn checks the malformed
  line off as superseded", finding 2 states its re-fire option. R3 held in the field:
  the response was readable where the check lives, with no departure from the file.
  **Maintainer-action leg DISCHARGED 2026-08-18 (discharge run 4) — ITEM COMPLETE, ticked.**
  The named response was performed in full, both halves, at the check: the Researcher
  re-fired the malformed pointer (vlt-core `84aea7c`, `_agent/dispatch.md:322` —
  `relay: researcher → librarian (deliver: career-cluster-wiki-pass)`) and the Librarian
  checked the 2026-08-17 15:12 line off as superseded (`e6d556b`), each in its own
  partner's sitting, neither leaving the file to learn what to do. Log lines at
  `[2026-08-18 10:26]` (researcher) and `[2026-08-18 10:35]` (librarian). **R3's first
  full field cycle: a check named its legal response, a maintainer performed it, and the
  finding cleared.** All five sub-clauses discharged — B8-1 is the arc's first ticked
  ledger item.
- [ ] **build-B8-2 (delivery-shape, briefed 2026-08-17):** (1) [ship-verifiable]
  `relay.md` defines exactly four shapes with `deliver` `ref`-keyed; every
  shape-enumeration site in the brief's sweep table (`vlt-dispatch/SKILL.md` ×4,
  `daily.md` seeded header, `ledger.md` key forms, operating contract :242,
  `module-help.csv` row 11) names `deliver`; the `doc-less`-without-`deliver` grep is
  zero across `skills/`; (2) [ship-verifiable] `ledger.md`'s
  known-incomplete-pending-B8-2 marker is gone (grep zero) and the pointer-integrity
  legal-response sentence covers every finding the check renders, one line, the file's
  single R3 seat — discharging B8-1's marker via its "discharged by B8-2" terminal
  state, B8-1's walk denominator (1 marker-bearing seat in `ledger.md`) still holding;
  (3) [ship-verifiable] the legacy paragraph defines the unit (pointer line), the
  key-path/wikilink-as-path rule, and the proto-`deliver` denominated lane, and two
  independent applications of the written counting rules against the brief's fixture
  agree — the denominator is reproducible by a second reader at rest;
  (4) [field-contingent — vlt-core] the first post-upgrade `vlt-dispatch ledger` run
  reports zero pointer-integrity findings for the inline-delivery class, the seven
  drained findings rendering under the denominated proto-`deliver` count (7 at vlt-core
  `4f06568`; may grow pre-upgrade), matching a by-hand application of the shipped rules;
  (5) [field-contingent — vlt-core] the first unsolicited pathless delivery after the
  upgrade fires as `deliver` with a publisher-chosen `ref` — vlt-core produces this
  event routinely (seven in one evening at the pin).

  **Discharge run 2026-08-18.** Upgrade-side DISCHARGED 2026-08-18: (1) `relay.md:17`
  "The four shapes" with the `deliver:` block at :72 `ref`-keyed; the
  doc-less-without-`deliver` grep and the "three shapes" grep are both 0 across
  shipped `skills/`; `module-help.csv` and the contract carry `deliver`; (2) the
  known-incomplete-pending-B8-2 marker greps to 0 across shipped `skills/` — B8-1's
  marker discharged via its named terminal state; (3) the counting rules shipped and
  the brief's two-application fixture agreement is recorded in its status (findings=0,
  legacy=2, proto-deliver=2, hand vs script).
  **STILL-OPEN: (4)** — no post-upgrade `vlt-dispatch ledger` run yet. *Trigger: the
  next vlt-core ledger run.* **STILL-OPEN: (5)** — no `deliver`-keyed relay block
  exists in vlt-core `_agent/dispatch.md` since the upgrade (the three `deliver*`
  greps are prose "deliverable"). *Trigger: the next unsolicited pathless delivery in
  a vlt-core sitting — the vault produced seven in one evening pre-upgrade, so the
  event is routine.*

  **(5) DISCHARGED 2026-08-18 (discharge run 4).** The vault's **first `deliver`** landed
  at `_agent/dispatch.md:322` (vlt-core `84aea7c`): `relay: researcher → librarian
  (deliver: \`career-cluster-wiki-pass\`)` — **pathless**, **publisher-chosen `ref`**,
  payload carried inline with durable notes cited as `[[wikilinks]]` (payload, never the
  key). It arose exactly as designed: the pointer-integrity check flagged the unkeyed
  predecessor, named `deliver` as the legal response, and the publisher re-fired in the
  correct shape — the same act that discharged B8-1 (5). **The item nonetheless stays
  unchecked on (4)'s FAILED grade.**

  **Update — discharge run 2 (2026-08-18, `vlt-dispatch ledger` run). (4) FAILED.**
  The run rendered **`0 proto-deliver pointers (pre-shape)` and 2 pointer-integrity
  findings**; the check required the seven to render under the denominated
  proto-`deliver` count with zero findings for the class. **A by-hand application of
  the shipped rules reproduces the check's number exactly, not the run's.** In the live
  record there are 18 shape-annotated relay headers, of which **7 are pathless**: the
  2026-08-15 21:30–22:10 batch of six `(handoff, ref: <slug>)` blocks
  (`_agent/dispatch.md:272,275,278,281,284,287`) plus `(handoff)` at :266 — the very
  seven this build's filing was written about. None carries a handoff-zone path; every
  payload link is an `[[_agent/research/...]]` wikilink, which `relay.md:28` calls
  "payload, never the key". Under `relay.md:41` a `handoff` **keys on its doc path**,
  not on a `ref`; under `relay.md:28` a shape-annotated **pathless** pointer written
  before `deliver` existed is proto-`deliver` traffic, "reported by `ledger` as a
  denominated count … **never as a finding**". By hand: proto-`deliver` = 7, findings
  for the class = 0. The run instead credited the six `ref:` values as keys (counting
  them among its 45 keyed) and rendered :266 as a finding. Its two verdicts are also
  mutually inconsistent on the era datum — it called the **2026-08-17 15:12** pointer
  "post-`deliver`-era" while calling the **older 2026-08-15** pointer a finding too, and
  no single boundary produces both (the vault gained `deliver` at the 2026-08-17 18:10
  upgrade, after both). **Root cause candidate for capture: `relay.md:28`'s era test —
  "written before `deliver` existed" — names no datum (module ship? vault upgrade?),
  and the interaction of `handoff`'s path-key with a supplied `ref` is unstated.**
  This is precisely the property check (3) claimed; see its qualification below.
  **Inbox filing FILED 2026-08-18** —
  `inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md`;
  routes to the next `inbox-capture`.
  **Independent field corroboration (2026-08-18, discharge run 4):** during the
  pointer-integrity repair the two partners reached the same reading unprompted — the
  Librarian's log line at `[2026-08-18 10:35]` records "verified Dorian's *one live
  finding* boundary — **the 08-15 `(handoff, ref:)` batch is proto-`deliver` traffic**,
  `deliver` having landed with the 0.11.0 upgrade on 2026-08-17, so it counts and never
  flags." Two independent readers now derive **7**, against the run's **0** — and they
  anchored the era to the **vault's upgrade date**. That is a defensible datum but a
  *chosen* one, not a shipped rule: evidence for the filing's disposition (a).

  **Qualification on (3):** (3) stays DISCHARGED on its own named evidence (the fixture
  two-application agreement, hand vs script, recorded in the brief's status) — the
  *counting unit* is reproducible. What the field shows is that the **era datum and the
  handoff-key interaction** are not, and (3) never named them. The drafted filing carries
  this, not a revocation.
- [ ] **build-B8-3 (memory-contracts, briefed 2026-08-17):** (1) [ship-verifiable]
  `frontmatter.md` at `version: 8` in one bump — both watermark fields (`archive:` +
  `compacted-through:`) defined exactly once in the Hygiene watermarks subsection, the
  `reflexes.md` schema present with in-frontmatter cap + falsifier + `review_after:`,
  all eight consumers acked `frontmatter@8` (incl. the new `vlt-setup` ack) —
  `package-lint` Group E green, `frontmatter@7` grep zero in `skills/`;
  (2) [ship-verifiable] the operating contract carries the hygiene-safety section (the
  safety model's single shipped home, citable by B8-4/B8-5) and the three ladder verbs
  by name — promote / compress-to-latest-form / retire (B8-4's floor) — with Beat 1
  naming the reflex read and the rule-card digest fresh (Group C green);
  (3) [ship-verifiable] R4 discharged — the vitals fixture run sums `identity.md` +
  `thread.md` + `reflexes.md` + `capabilities/` into `partner_memory_bytes`, the `:441`
  display-only comment untouched (B8-4's carrier); (4) [ship-verifiable] a fresh
  fixture vault's setup pass seeds all three memory files per partner, and a re-run
  against a populated `reflexes.md` leaves it byte-identical (never-clobber);
  (5) [field-contingent — vlt-core; honesty class (b)] first post-upgrade activation of
  a partner already carrying a vault-grown `reflexes.md` loads it in Beat 1 under the
  contract rule with zero SKILL.md edits, and partners lacking one acquire the seed —
  the fleet adoption path observed live; (6) [field-contingent — vlt-core; honesty
  classes (a)/(b)] first at-write exercise — a rule-shaped lesson lands as a one-line
  reflex (promote) rather than thread narrative, and a revised standing read is
  compressed-to-latest-form rather than stacked (no four-version recurrence on
  at-write material); (7) [field-contingent — vlt-core; honesty class (c) — watched,
  not covered] corrections-per-sitting on already-recorded knowledge observed across
  post-upgrade sittings, handled in-the-moment per the rule, class-(c) recurrences
  recorded as watch data feeding B8-4's calibration — the build claims no class-(c)
  coverage.

  **Discharge run 2026-08-18.** Upgrade-side DISCHARGED 2026-08-18: (1)
  `governance/_meta/conventions/frontmatter.md:11` = `version: 8`, `frontmatter@7`
  greps to 0 across shipped `skills/`, 8 consumer↔ack pairs, `package-lint` Group E
  PASS re-run today; (2) the contract carries `## Hygiene and grooming — the safety
  model` at :270 and the three verbs at :212 (`compress-to-latest-form` by name),
  Group C PASS; (3)+(4) the R4 vitals fixture sum and the seed-idempotence dry-run are
  recorded PASS in the brief's status (`partner_memory_bytes` 650 = 100+200+300+50;
  populated `reflexes.md` sha256-equal after re-run) — and the field confirms the seed
  path: the 0.11.0 upgrade seeded `reflexes.md` for 8 of 9 partners, never touching
  career-strategist's existing one (upgrade-ledger, Migrations line).
  **STILL-OPEN: (5), vault-grown leg** — the one partner carrying a *vault-grown*
  `reflexes.md` (career-strategist, minted `b00db0a` 2026-08-15) has not activated
  since the upgrade; the only post-upgrade activation (librarian, 2026-08-18 09:18)
  carried the *seeded* file. *Trigger: the next career-strategist summon.*

  **Update — discharge run 3 (2026-08-18). (5) DISCHARGED.** The trigger fired: the
  career-strategist sitting at 09:28 (`_agent/sessions/2026-08-18-092852-misc.md`,
  commit `9e6b949`) is the first post-upgrade activation of the one partner carrying a
  **vault-grown** `reflexes.md` (minted pre-upgrade at `b00db0a`, 2026-08-15). The file
  was loaded and consulted in-sitting — the session note names the rule by its text
  ("The existing reflex — read the overlay before the base — should have fired at the
  first write, not the last read"), which is verbatim `reflexes.md:35`. **Zero SKILL.md
  edits** were required: the contract-side reach worked as A8 designed it. The seed leg
  was already discharged (8 partners seeded at upgrade, career-strategist's existing
  file never touched).
  **STILL-OPEN: (6)** — no at-write exercise yet: the promote/compress observed on
  2026-08-18 was the B8-4 groom op, not the at-write path. *Trigger: the next partner
  sitting that produces a rule-shaped lesson or revises a standing read.*

  **Update — discharge run 3 (2026-08-18): first at-write opportunity observed, verdict
  deliberately withheld.** The 09:28 career sitting produced a rule-shaped correction
  (hard-wrapped prose in breach of overlay rule A) and handled it **at write, in one
  line**, under the contract's correction-as-signal rule — but it landed in the session
  note plus `identity.md`/`thread.md`, **not** in `reflexes.md` (that file is absent from
  `9e6b949`'s changed-file list). Two honest readings, and this run does not pick one:
  (a) the promote path failed to fire on at-write material — the exact behavior this
  check exists to detect; (b) correctly **no promotion was owed**, because the lesson was
  "an *existing* reflex should have fired earlier" (`reflexes.md:35` already carried the
  rule), and correction-as-signal is a behavioral rule with no metric (disposition 9), so
  narrative was the right home. Reading (b) is the stronger one on the evidence. What is
  still genuinely unobserved is the check's **other half** — a *revised standing read*
  compressed-to-latest-form rather than stacked. *Trigger: a sitting that produces a
  genuinely new rule-shaped lesson, or revises an existing standing read.*
  **STILL-OPEN: (7)** — watch data needs multiple post-upgrade sittings; one has
  occurred. *Trigger: accumulating vlt-core sittings (dated clock).*

  **Update — discharge run 3 (2026-08-18): first watch data recorded.** Three
  post-upgrade sittings so far (librarian groom 09:18, career 09:28, researcher groom
  09:34). One class-(a) correction observed and handled in-the-moment per the rule
  (career, hard-wrap breach, self-caught at the overlay read and unwrapped in place —
  recorded as a one-line *Correction-as-signal* section). **Feeding B8-4's calibration
  as intended, and it has already produced module signal:** the researcher filed
  `inbox/2026-08-18-094459-activation-ritual-omits-overlays-fleet-rules-land-as-per-partner-reflexes.md`
  out of its own groom pass, reporting two same-day overlay violations by two partners
  and arguing the reflex layer is becoming the condensation point for **fleet-wide**
  rules because no always-loaded rung exists between one partner's reflexes and shipped
  governance. That is a design consequence of B8-3's reflex layer, not a failure of any
  B8-3 check — it is new, uncaptured field signal for `inbox-capture` and Arc 9.
- [ ] **build-B8-4 (groom-op, briefed 2026-08-17):** (1) [ship-verifiable] the fixture
  groom runs end-to-end against a factory fixture partner planting every disposition
  class: gate halt with the class-grouped, one-line-rationale-per-item rendering
  (promote / compress-to-latest-form / retire — never a monolithic wall); partial
  approval honored; the declined item intact plus its inline decline marker; unapproved
  material byte-identical; a pre-marked item excluded from the proposal;
  `groomed:`/`archive:` written with `archive:` resolving to the pre-groom bytes;
  staging directory removed; `groom` log line present — the arc's motivating
  deliverable gates closeout on this check (A9); (2) [ship-verifiable] registration
  coherent — `package-lint` A/B/C/E green with `vlt-groom` in marketplace `skills[]`
  (C5 both directions), a quoted 13-col help-csv row, README at 15 in both count
  sites, and the ninth `frontmatter@8` consumer ↔ ack pair (Group E), no `frontmatter`
  version bump anywhere in the diff; "Until the groom op ships" greps to zero in
  `skills/`; (3) [ship-verifiable] `vlt-vitals.py:441` carries the self-contained
  disposition-8 discharge comment (date + evidence in the text, no factory-internal
  path, code behavior unchanged; B8-5 independently verifies it present);
  (4) [field-contingent — vlt-core] first live groom of an active partner
  post-upgrade: invoked-only observed, per-class approval actually exercised,
  watermarks land, per-file byte deltas reported, pre-groom state reachable via the
  applied `archive:` reference; (5) [field-contingent — vlt-core] decline memory
  across two live grooms — an item declined with a reason is not re-proposed by the
  next groom absent a content change (the lint-has-no-memory failure not reproduced).

  **Discharge run 2026-08-18.** Upgrade-side DISCHARGED 2026-08-18: (1) the A9 fixture
  groom end-to-end is recorded PASS in the brief's status (gate halt with 3-class
  rendering, partial approval honored, declined item intact + marker, unapproved
  material byte-identical, pre-marked item excluded, `groomed:`/`archive:` written,
  staging removed, log line present); (2) `package-lint` A/B/C/E PASS re-run
  2026-08-18 with `vlt-groom` in marketplace `skills[]` and a quoted 13-col csv row
  (`module-help.csv:11`), "Until the groom op ships" greps to 0; (3)
  `hooks/vlt-vitals.py:508-510` carries the self-contained disposition-8 discharge
  comment (date + evidence, no factory path).
  **(4) DISCHARGED 2026-08-18 on four of five legs — first live groom fired**
  (vlt-core `0d80d25`, librarian/Gwyn, 2026-08-18 09:19): invoked-only observed
  ("Mikey invoked `vlt-groom Librarian`"); watermarks landed (`thread.md`
  `groomed: 2026-08-18` / `archive: f0538d2`); per-file byte deltas reported
  (thread.md 134,067 → 13,758; reflexes.md 416 → 1,783; identity.md untouched);
  pre-groom state reachable via the applied `archive:` reference; applied == proposal
  diff-verified byte-identical. **⚠ Owner flag — the per-class-approval leg was
  offered but not exercised:** the proposal rendered in three classes and the owner
  approved the whole pass in one word (promote 10 / compress 7 / retire 58 /
  **declined 0**). Partial approval and decline are fixture-covered (check 1) but
  remain unexercised live. Owner ruling needed on whether check (4) is satisfied by
  the offered-but-unused surface, or waits for a live partial approval.
  **STILL-OPEN: (5)** — decline memory needs two live grooms and a declined item;
  one groom has run with 0 declines. *Trigger: a second vlt-core groom carrying a
  declined item (owner-initiated).*

  **Update — discharge run 3 (2026-08-18, second live groom). (4) DISCHARGED; the
  earlier owner flag resolves.** A second groom ran (vlt-core `2400dd9`,
  researcher/Dorian, 09:34): promote 36 / compress 17 / retire 19 / declined 0;
  watermarks `groomed: 2026-08-18` / `archive: 0d80d25`; identity.md, thread.md and
  reflexes.md all revised. The owner reports engaging the gate **with per-item feedback
  rather than a blanket approval** this time ("provided feedback but mostly approved"),
  so the per-class approval surface was exercised interactively — the leg the librarian
  pass left open. All four other legs held a second time (invoked-only, watermarks,
  byte deltas, archive reachability).
  **(5) STILL-OPEN — and two grooms do not discharge it.** Both grooms recorded
  **`declined: 0`**, so no declined item exists to test re-proposal against; and they
  were two *first* grooms of two **different** partners (librarian, then researcher),
  where the check needs a groom **and its successor on the same partner** — decline
  markers are per-item in that partner's own files, so subject-match is load-bearing
  here. *Trigger: a groom that actually declines an item with a reason, followed by a
  second groom of that same partner.*
- [ ] **build-B8-5 (decay-contracts, briefed 2026-08-17):** (1) [ship-verifiable]
  fixture rotate holds every `{log}` reader — `ingests_since_lint`, `days_since_lint`,
  and lint Step-0's scoped baseline identical pre/post; archive + live tail reproduce
  the pre-rotation record; a never-linted fixture draws a loud refusal; a second rotate
  no-ops; (2) [ship-verifiable] fixture drain holds every dispatch/backlog reader —
  open-pointer counts, per-slug greps, and `oldest_open_pointer_days` identical; each
  source's newest `daily/` watermark block and every `consult:` block retained;
  `## Open` byte-identical; the widened `spec_candidate`/retrofit reads (live +
  archive) derive the pre-drain counts; `oldest_drainable_section_days` clears its
  wire; a second drain no-ops; (3) [ship-verifiable] the registry ships 4 wires, one
  canonical metric id each, mass (`log_bytes`) and age
  (`oldest_drainable_section_days`) on separate wires; the bar sentence intact verbatim
  with the count wording updated ("two stock wires" greps to zero across `skills/`);
  `WIRE_REQUIRED_FIELDS` unchanged; an existing 2-wire vault registry merges to exactly
  4 with local thresholds winning; (4) [ship-verifiable] the contract carries the Decay
  contracts table covering every structure-table file class and every B8-1..B8-4
  newborn (verb-covered or exempt-with-reason; `reflexes.md` cited to its at-birth
  contract; partner memory pointed at `vlt-groom`) plus the A13 sentence; every
  prose-reconciliation surface shows its ruled state (contract `:36`/`:122` updated;
  `vlt-lint/SKILL.md:72` + `daily.md:63` reaffirmed-with-clause; `ledger.md`
  live-record clause present); the `vlt-vitals.py:441-443` discharge comment verified
  present and unedited; `frontmatter.md` and `consult.md` diffs empty — no version bump
  anywhere (A7), Group E green with zero handshake motion; (5) [ship-verifiable]
  release gate — `package-lint` A/B/C/E green with `vlt-decay` registered (C5, quoted
  csv row, README 16 both sites) and `--expect-version 0.11.0` exit 0, PASS line in
  the release commit; (6) [field-contingent — vlt-core] the adoption bell rings as
  designed — first post-upgrade wake trips `log-mass`, the maintainer invokes the
  rotation (or deliberately raises the local threshold — either is the legal response);
  after a performed rotation the strip goes green, the next scoped lint still runs
  scoped (no full-mode fallback), and `lint-debt`'s count matches its pre-rotation
  derivation; (7) [field-contingent — vlt-core] first live drain of the real dispatch
  record — board counts identical pre/post, every capture source's next scoped `daily`
  run routes only genuinely-new lines (no watermark reset, no duplicates), and the
  ledger's legacy denominators re-render as live-record counts per the shipped clause
  with the drained blocks reachable at the archive mirror.

  **Discharge run 2026-08-18.** DISCHARGED 2026-08-18: (1)+(2) the fixture rotate and
  drain runs are recorded PASS in the brief's status with their named reader-invariant
  numbers; (3) the shipped seed carries exactly 4 wires with one canonical metric id
  each and mass/age on separate wires (`tripwires.yaml:46/54/62/70`), "two stock
  wires" greps to 0, and the vault's existing 2-wire registry merged to exactly 4 with
  local wires and thresholds kept (upgrade-ledger, Notes); (4) the contract carries the
  Decay contracts table with :36/:122 updated, and the `vlt-vitals.py` discharge
  comment is present and unedited; (5) release gate — `package-lint --expect-version
  0.11.0` exit 0 re-run 2026-08-18 (A/B/C/D/E PASS), PASS line present in release
  commit `86efd48`.
  **(6) STILL-OPEN — ⚠ pass-through: the rotation fired without the bell.** The
  rotate verb was exercised live (vlt-core `f0538d2`, 2026-08-18 09:08: 238 entries /
  223,208 bytes → `_archive/_agent/log.md`), but `log-mass` never rang — `log_bytes`
  at rotation was 244,238, under the stock 262,144 threshold (the wire that rang at
  the upgrade was `drain-due`, 65 > 45). Post-rotation `log_bytes` = 19,323, so the
  bell is now months of growth away. *Reachability re-examined per the rubric: the
  wire is live in the vault registry at stock threshold and `vitals` evaluates
  `log_bytes` every wake — reachable, hence STILL-OPEN rather than BLOCKED.* The
  post-rotation legs (next scoped lint still scoped, `lint-debt` count matching its
  pre-rotation derivation) are equally untested — no lint has run since the rotation.
  *Trigger: vlt-core `log_bytes` regrowing past 262,144, plus the next scoped lint.*
  **Discharge run 2 (2026-08-18) confirms both legs still unfired:** the ledger run's
  wire block reads "`log-mass` ok" at `log` 19,323 B, and `days_since_lint` 2 — no lint
  has run since the rotation.
  **(7) DISCHARGED 2026-08-18 on the drain-integrity legs; STILL-OPEN on the
  downstream legs.** First live drain fired (`f0538d2`): 15 closed dispatch blocks
  (13,825 bytes) + 34 backlog Done items (43,639 bytes) → `_archive/_agent/`. Board
  counts verified identical pre/post by direct diff — dispatch `## Open` section
  **byte-identical**, open pointer rows 12 → 12, backlog open rows 65 → 65;
  breadcrumbs written in place (`dispatch.md:3`, `backlog.md:3`); drained blocks
  reachable at the archive mirror. **STILL-OPEN:** no capture source has run a scoped
  `daily` since the drain (the 2026-08-17/18 capture notes committed at `624eb94`
  predate it), and no `ledger` run has re-rendered the legacy denominators as
  live-record counts. *Trigger: the next vlt-core scoped `daily` run and the next
  `ledger` run.*

  **Update — discharge run 2 (2026-08-18, `vlt-dispatch ledger` run). Ledger leg
  DISCHARGED:** the shipped live-record clause (`ledger.md:26`) rendered as designed —
  the run reported "15 legacy unkeyed pointers (pre-shape)" as a **live-record** count
  and the drained blocks are reachable at the archive mirror (`_archive/_agent/dispatch.md`
  holds 10 relay headers, all un-annotated = the legacy lane). Note the re-baselining was
  exercised **for the legacy lane only**: the archive holds **zero** shape-annotated
  headers, so no proto-`deliver` pointer was drained — the proto-`deliver` lane's 0 is
  the B8-2 (4) failure above, not a drain effect. **Corroboration for the drain's
  boundary:** `drain-due` now reads **44** against threshold 45 — the drain took
  everything over the line and left the next-oldest just under it, exactly the intended
  behavior. **STILL-OPEN:** no scoped `daily` run since the drain. *Trigger: the next
  vlt-core scoped `daily` run.*

## Owner batch ruling over the open acceptance tails (2026-08-18)

*Taken at the close of `acceptance-discharge` run 4, against
`arc-closeout/references/closeout-checklist.md` Stage 1. Every ship-verifiable check in
this arc is DISCHARGED; the tails below are all `[field-contingent]`, which by the gate's
own rule **cannot fail closeout** — they move to the Stage 2 standing watch register. The
dispositions are the owner's, recorded here so no item enters closeout as a bare `- [ ]`.*

**B8-1 — no ruling needed.** Ticked `- [x]`, all five sub-clauses discharged 2026-08-18.

- **B8-3 (6) — at-write promote half → RELEASED as a standing watch.** The first
  opportunity was observed (career sitting `9e6b949`) and the verdict deliberately
  withheld: the lesson was that an *existing* reflex (`reflexes.md:35`) fired late, not
  that a new rule needed promoting, so narrative was plausibly the correct home
  (correction-as-signal, disposition 9, no metric). **Never ticked — released, not
  proved.** The check's other half (a revised standing read compressed-to-latest-form
  rather than stacked) remains entirely unobserved. Watch subject: the next sitting
  producing a genuinely new rule-shaped lesson, or revising a standing read.
- **B8-3 (7) — corrections-per-sitting watch → RELEASED as a standing watch.** By
  construction this check claims no coverage (honesty class (c), "watched, not covered").
  First data recorded: 3 post-upgrade sittings, 1 class-(a) correction handled
  in-the-moment. It feeds B8-4's calibration and has already produced module signal
  (`inbox/2026-08-18-094459`).
- **B8-4 (5) — decline memory → RELEASED as a standing watch.** Two grooms have run and
  neither discharges it: both logged `declined: 0`, and they were two *first* grooms of
  **different** partners (librarian `0d80d25`, researcher `2400dd9`), where the check needs
  a groom **and its successor on the same partner** — decline markers are per-item in that
  partner's own files. Watch subject: a groom that declines an item with a reason, followed
  by a second groom of that same partner. **Not ticked; the decline path is unexercised.**
- **B8-5 (6) — the adoption bell → RELEASED as a standing watch, flagged PASS-THROUGH.**
  The rotate verb was exercised live (`f0538d2`) but `log-mass` never rang: `log_bytes` at
  rotation was 244,238 against the stock 262,144 threshold, and post-rotation reads 19,323,
  so the bell is months of growth away. Reachability was re-examined per the rubric and
  confirmed (wire live at stock threshold; `vitals` evaluates `log_bytes` every wake), which
  is why this is a watch rather than BLOCKED. **Standing instruction for the next discharge
  run:** if this tail survives a further run still unfired, the rubric forbids
  re-annotating it STILL-OPEN — it must be re-examined for reachability and, failing that,
  graded BLOCKED and filed.
- **B8-5 (7) — post-drain daily leg → STAGED.** The drain-integrity and ledger legs are
  DISCHARGED; only the "next scoped `daily` run routes only genuinely-new lines (no
  watermark reset, no duplicates)" leg is unobserved, and the event is cheap and honest to
  manufacture. **Named action:** run `vlt-dispatch daily` on vlt-core against a capture
  source whose block was drained, and confirm no watermark reset and no duplicate routing.
- **B8-2 (4) — FAILED, exercised.** Disposition recorded separately below (the checklist's
  build-20 form: a clause exercised and FAILED is carried as inherited debt). See
  *B8-2 (4) — disposition*.

### B8-2 (4) — disposition: INHERITED DEBT to Arc 9, bound to settle and to gate

**Owner ruling, 2026-08-18.** B8-2 (4) was exercised and FAILED, so it takes the checklist's
build-20 form — carried as inherited debt to the next arc rather than released as a watch.
**Arc 8 is not reopened:** the defect mis-writes nothing into the vault (the two lanes are
counts, never findings), so a v0.11.1 release cycle is not earned.

**The debt, stated for the inheritor.** Two shipped sentences are underspecified and
interact: `relay.md:28`'s era test ("written before `deliver` existed") names **no datum**,
and `relay.md:41` gives `handoff` a **path**-key while leaving undefined what a
supplied-but-unrequired `ref` does on a pathless `handoff` — six pointers change lane on
that answer. Applied by hand the shipped rules give **proto-`deliver` = 7, findings = 0**;
the first live run rendered **0 and 2**.

**The second-order finding, which is the more valuable half.** The backward-compat exemption
is arguably **over-broad**: read strictly it would have *suppressed* the 2026-08-17 15:12
finding (it predates the vault's upgrade, so it "counts and never flags") — yet surfacing
that pointer was correct, and acting on it discharged B8-1 (5) and B8-2 (5). A rule that
silences a **live, guard-disabled** pointer because it is old is a design question the count
mismatch merely exposed. Arc 9 should rule on the exemption's *scope*, not only its datum.

**Two binding conditions on the carry** (the whole point of this disposition — a bare carry
is the failure mode this repo already has evidence for):

1. **It seeds Arc 9 as a build candidate at capture**, not as a watch-register line. Its
   filing is already in the inbox with a corroborated root cause and four candidate
   dispositions:
   `inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md`.
2. **Its re-check is tagged `[ship-verifiable]` from birth, so it gates Arc 9's closeout.**
   This is possible here and was *not* possible for the Jackson pair: the fix is prose in
   `relay.md` plus a reproducibility line in `ledger.md`'s verify checklist, and the
   corrected counting rules are provable **at rest against a fixture** — no field event
   required. **Precedent being applied deliberately:** the A4-4(5) debt rode **four arcs**
   because it was field-contingent and therefore could never block a closeout; B7-6 retired
   it only once amendment A3 tagged it ship-verifiable so it would gate. That lesson is
   applied here preemptively rather than after three more arcs of drift.

**Evidence quality on inheritance.** Two vlt-core partners independently derived 7 against
the run's 0 on 2026-08-18, anchoring the era to the **vault's upgrade date** — a defensible
but *chosen* datum, not a shipped rule. Arc 9's capture inherits a diagnosis it does not need
to re-litigate.

**On the `[x]` count.** Exactly one of five ledger items is ticked. That count is **not** a
measure of what this arc proved: every ship-verifiable check across all five builds passed,
and four items stay unticked because they bundle field-contingent tails that were released
or staged rather than exercised. Read the per-item annotations, not the checkboxes.

## Closeout record — Arc 8 CLOSED 2026-08-18

**This arc is archived — do not append.** Read it for history; the next arc's
`inbox-capture` re-lists the carry-forwards below from this file.

**Gate (per `arc-closeout` Stage 1):** PASSED. Release shipped — `v0.11.0` tagged locally and
on the remote (`86efd48`). Ledger — B8-1 ticked `- [x]` with dated evidence; B8-2..B8-5 each
carry an explicit owner carry-forward ruling (§ *Owner batch ruling*, 2026-08-18). Acceptance
was graded by four `acceptance-discharge` runs on 2026-08-18, not by this skill.

**Acceptance evidence in one line:** the vlt-core `0.10.0 → 0.11.0` own-the-apply
(2026-08-17 18:10) plus post-upgrade field activity — rotate+drain `f0538d2`, grooms
`0d80d25` (librarian) + `2400dd9` (researcher), the first `vlt-dispatch ledger` run, career
sitting `9e6b949`, and the pointer-integrity repair `84aea7c` + `e6d556b`. **Every
ship-verifiable check across all five builds DISCHARGED** (`package-lint` A/B/C/D/E exit 0).

### Carried forward past Arc 8

*Authoritative hand-off list. Anything not named here is dropped.*

**From Arc 8's own ledger (owner-ruled 2026-08-18):**

1. **B8-2 (4) — INHERITED DEBT to Arc 9, bound.** Exercised and FAILED: the first live
   `ledger` run rendered `0` proto-`deliver` + 2 findings where the shipped rules applied by
   hand give `7` + 0. Root causes: `relay.md:28`'s era test names no datum, and `relay.md:41`
   leaves undefined what a supplied `ref` does on a pathless `handoff`. **Bound: it seeds
   Arc 9 as a build candidate at capture, and its re-check is tagged `[ship-verifiable]` from
   birth so it GATES Arc 9's closeout** — the A4-4(5)/B7-6 lesson applied preemptively. Also
   carries the second-order question: the backward-compat exemption may be **over-broad**
   (read strictly it would have suppressed the very finding whose repair discharged B8-1 (5)
   and B8-2 (5)), so Arc 9 rules on the exemption's *scope*, not only its datum. Filing:
   `inbox/2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md`.
2. **B8-3 (6) — released standing watch.** At-write promote half; first opportunity observed,
   verdict withheld (no promotion likely owed). The compress-to-latest-form half is entirely
   unobserved. **Never exercised — released, not proved.**
3. **B8-3 (7) — released standing watch.** Corrections-per-sitting; the build claims no
   class-(c) coverage by construction. First data: 3 post-upgrade sittings, 1 correction.
4. **B8-4 (5) — released standing watch.** Decline memory. Needs a groom that **declines an
   item with a reason**, followed by a **second groom of that same partner**; the two grooms
   run so far were first grooms of different partners, both `declined: 0`.
5. **B8-5 (6) — released standing watch, flagged PASS-THROUGH.** The rotate fired without the
   `log-mass` bell (`log_bytes` 244,238 < 262,144 at rotation; 19,323 after). Reachability
   re-examined and confirmed. **Standing instruction:** if this tail survives a further
   discharge run still unfired, the rubric forbids re-annotating it STILL-OPEN — re-examine
   reachability and, failing that, grade it BLOCKED and file it.
6. **B8-5 (7) — STAGED, named action.** Run `vlt-dispatch daily` on vlt-core against a capture
   source whose block was drained; confirm no watermark reset and no duplicate routing.

**Inherited, still open at Arc 8's close:**

7. **Ruling 4c — the three lint-surfaced module-feedback candidates: BOUND MISSED.** The
   roundtable (A15) set filer = owner and bound = **before Arc 8's release**; v0.11.0 shipped
   2026-08-17 with no such filings in `inbox/`. Recorded here rather than quietly re-dated —
   the candidates default to **Arc 9 capture** (capture run 2), still owner-filed.
8. **C6-c** — the Stage-7 bullet the owner must paste (from Arc 6, inherited through Arc 7).
9. **The B5-3..B5-9 field-contingent watch register + the pre-Arc-5 carries** — authoritative
   list in `skills/reports/archive/inbox-evolution-arc5-roadmap.md`'s Closeout record.
10. **Arc 7's five released standing watches** — authoritative list in
    `skills/reports/archive/inbox-evolution-arc7-roadmap.md`'s Closeout record.
11. **Victor's frame candidate** (a single shipped lifecycle convention: every agent-zone file
    class declares its decay/promotion posture in one table) — file if a ninth-arc filing
    repeats the pattern. **Arc 8 shipped the per-build accretion this would replace**, so the
    candidate is now testable against real surface.
12. **D1 dissent on record (John)** — queuing the arc's motivating deliverable fourth behind an
    overloadable B8-3 risked the arc's value. Recorded, not actioned; the order held and B8-4
    shipped.

### Filings — all four held live, none archived

Per `arc-closeout` Stage 5's per-filing criterion, a filing archives only when **every clause
traceable to that filing** is discharged **and** the build's residue belongs to a different
filing. All three `derives_from` filings fail condition 1 — each has its own clause released,
staged, or carried as debt, and *released is not passed*:

- `2026-08-16-093429-append-only-agent-files-have-no-decay-contract.md` — **held** (B8-5 (6)
  released watch, (7) staged).
- `2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload.md` — **held** (B8-2 (4)
  inherited debt).
- `2026-08-17-143641-partner-memory-has-no-promotion-ladder-or-staleness-contract.md` —
  **held** (B8-3 (6)/(7), B8-4 (5) released watches).

**Uncaptured field signal already in `inbox/` at close** (for Arc 9's `inbox-capture`, which
opens on a clean slate):

- `2026-08-18-094459-activation-ritual-omits-overlays-fleet-rules-land-as-per-partner-reflexes.md`
  — filed by the Researcher out of its own groom pass. The activation ritual never surfaces
  `{overlays}`, and **the reflex layer is becoming the condensation point for fleet-wide
  rules** because no always-loaded rung exists between one partner's reflexes and shipped
  governance. A **design consequence of B8-3**, not a failure of any B8-3 check; it is the
  read-side of the 2026-08-14 `no-legal-home-for-a-vault-originated-new-convention` filing.
- `2026-08-18-101612-proto-deliver-era-test-names-no-datum-and-handoff-ref-slips-its-key-rule.md`
  — the B8-2 (4) debt filing (carry-forward 1).

**Next lifecycle move:** `inbox-capture` for Arc 9 — two uncaptured filings already sit in
`inbox/`, and capture re-lists the twelve carry-forwards above from this archived roadmap.

