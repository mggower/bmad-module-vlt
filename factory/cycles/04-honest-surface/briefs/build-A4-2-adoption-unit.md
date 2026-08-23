---
title: 'Build #A4-2 — the adoption unit (a key nobody is asked to fill, and a count whose only value is "fine")'
status: 'BUILT 2026-07-25 — F1–F8 landed as briefed across nine shipped files: the two-outcome `revisit_after:` ask in both writers (`vlt-research:75`, `vlt-ingest:90` key + `:94` ask, key line byte-identical), the new `## Honest reporting — what a check may claim` section in `vault-operating-contract.md` (`:250-256`) carrying the general rule plus the relocated derive-first boundary clause, `vlt-lint` reduced to a pointer at `:84` with the honest limit at `:43`/`:94` and the `research_zone:` denominator above both candidacy slots, `frontmatter.md:242`''s live-consumers sentence, explicit `adoption_first_instance: null` in `spec.md` + `wiki-consolidation.md`, and the facet''s consumer (`vlt-upgrade` Step-4 report line + definition + Step-5 ledger line) and writer (`vlt-mint` Step 4). Verification: 1–6 and 8–11 PASS (both homes single, no `version:`/`consumers:` line moved, package-lint A/B/C/E PASS on vlt 0.7.0 with D skipped as briefed, no cruft, scrub clean); check 7 PASS for `vlt-upgrade`, PARTIAL for `vlt-lint` — see deviation 1. Not a release build; no version bump, no registration, no re-ack. Deviations/notes: (1) **Verification 7, `vlt-lint` half — the Step-5 fence does not parse as strict YAML, and did not at `4ca619e` either.** The failure is a pre-existing plain-scalar `: ` inside the flow sequence at `sources_vs_prose_mismatches:` — the exact slot disposition 5 leaves to capture — and it is byte-unchanged here. The new `research_zone:` line parses in isolation and is a stable snake_case identifier; `vlt-upgrade`''s fence parses whole. No regression introduced, so the check is recorded PARTIAL rather than failed. (2) **The five `checked`-stage conventions are deliberately not stamped** (F6''s named asymmetry) — no witnessed first instance exists to cite, and F7''s third report value covers them honestly. Recorded here because the brief asked for it explicitly if the builder was tempted to normalize it. (3) **File count reads nine, not the risk line''s "six"** — the brief''s own F1–F8 enumerate nine files (two writers, three consumer skills, the contract, `frontmatter.md`, and the two stamped conventions); the risk line undercounted the governance side. No scope change, purely the brief''s arithmetic.'
module_code: 'vlt'
created: '2026-07-25'
derives_from:
  - 'inbox/2026-07-25-144500-revisit-after-has-no-adoption-path.md (A3-19 — shape 1 `revisit_after:` in the write beat, shape 2 wire `adoption_first_instance:`, shape 3 the `revisit_due` report line; shape 3 conforms to the general rule rather than being briefed separately)'
  - 'inbox/2026-07-25-193000-report-slot-with-no-check.md (the `sources_vs_prose_mismatches` slot — its honesty half only; the missing-check half is capture''s to rule)'
roadmap: 'skills/reports/inbox-evolution-arc4-roadmap.md (§Builds → A4-2; §Deferred acceptance ledger)'
rulings: 'Arc-3 roadmap §Ideation rulings — A3-18..A3-23 (2026-07-25), the binding home: A4-2 = A3-19, ships second; fix the key in BOTH writers AND wire the adoption facet (ODQ #3+#4, owner-delegated to clerk''s recommendation, reversible); the silent-zero class gets ONE general honest-reporting rule, STATED ONCE, written by this build and cited by the rest — no site briefs a bespoke report-line fix; where the `adoption_first_instance:` consuming check lives is LEFT TO BRIEF TIME, hard-bounded by `frontmatter.md:242` (outside lint, or revisit `:242` explicitly); A3-19''s one-vault / four-post-fix-notes evidence debt is NOT BLOCKING, carried as context.'
risk: 'low-moderate — six shipped files across three surfaces (two write templates, the operating contract, three consumer skills), but **no convention `version:` moves**: F5 is a prose clarification and F6 stamps an optional self-describing facet, neither of which changes a rule a consumer must follow. No consumer walk, no re-ack, no `module-help.csv` row. The moderate half is breadth, not depth — the contract gains a new governing section that three later builds will cite, so its wording is load-bearing beyond this build.'
---

# Build #A4-2 — the adoption unit

Arc 4's opening position is that the module can report on itself but cannot tell a true report
from a comfortable one. A4-1 fixed the mirror case (a projection whose hits were all noise).
This build fixes the other half of the same shape — **a key nobody is ever asked to fill, and a
count whose only attainable value is "fine"** — and it writes the one general rule the rest of
the arc cites rather than re-inventing.

Three things land, and they are one story:

1. **`revisit_after:` gets a write beat in *both* research-note writers.** The filing found
   0-of-96 adoption. Grounding found the mechanical reason the filing missed: `vlt-ingest` —
   the *majority* research-note write path — omits the key from its template entirely, so a
   partner on that path never sees the slot and therefore cannot decline it. A
   `vlt-research`-only fix leaves the 0-of-96 mechanism intact.
2. **`adoption_first_instance:` gets its first real consumer.** The facet shipped in Arc 3 as
   the answer to "declared but never exercised" and is itself declared and never exercised —
   zero of seven shipped conventions carry it, including `spec.md`, the example
   `frontmatter.md:242` itself names. The arc's remedy became the arc's fourth instance. This
   build wires it end to end: a writer, a stamp, and a consumer that reports it.
3. **The general honest-reporting rule is written, once, in one home.** *A count whose only
   attainable value is "fine" must state what it cannot see.* Every later site in the class
   (A4-3's `contradictions_handled`, A4-4's ingest counts, the `sources_vs_prose_mismatches`
   slot, the original `deferral_metric` scar) conforms to it rather than wording its own.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** In
particular: the filing's shape 3 is *not* a separate `vlt-lint:94` report-line item (it is an
instance of the general rule, ruled at the silent-zero decide-once); and the facet's consumer is
*not* free to be a lint absence-check without explicitly revisiting `frontmatter.md:242` — a
constraint this brief honors rather than reopens (disposition 2).

---

## Grounding at brief time — results

Every site A3-19's capture cited was re-verified against current source (post-A4-1, commit
`4ca619e`). **One grounding correction, four grounding additions.**

| Capture site | Outcome | Fresh site |
|---|---|---|
| `vlt-research/SKILL.md:71` | **HOLDS** — byte-exact | `:71` (template `:58-73`) |
| `vlt-ingest/SKILL.md:77-91` | **HOLDS** — template still emits `type/created/title/author/trust/topic/status/sources` and stops; no `revisit_after:` | `:77-91` |
| `frontmatter.md:138` (`revisit_after:` semantics) | **HOLDS** — byte-exact | `:138` (schema line `:133`) |
| `frontmatter.md:237` / `:242` (adoption axis) | **HOLDS** — byte-exact, both | `:237`, `:242` |
| `vlt-lint/SKILL.md:84` (`revisit_due` report line) | ⚠️ **MOVED → `:94`** | see correction below |
| `vlt-lint/SKILL.md:74` (build-23 honest-limit precedent) | **HOLDS** — the convention-coherence check's "verifies the **pin**… not that a consumer's body actually conforms; content-conformance is out of its jurisdiction" | `:74` |
| zero-of-seven conventions carry `adoption_first_instance:` | **HOLDS** — `grep -rn adoption_first_instance skills/…/conventions/` still returns `frontmatter.md` only (`:237`, `:242`) | — |

**Grounding correction — `vlt-lint`'s `revisit_due` bullet moved `:84 → :94`.** A4-1 inserted the
derive-first boundary clause and rewrote the `linkage_ripe` bullet above it, shifting everything
below by ten lines. The bullet's **text is byte-unchanged** (A4-1's own verification 8 confirmed
it as "A4-2's site, not this build's") — this is a pure line shift, not a scope change. The
roadmap's superseding note is appended (see *Roadmap notes written by this brief*). Note that
`:84` is now the **boundary clause A4-2 inherits**, so the old number now points at a different
obligation — cite `:94` for `revisit_due` and `:84` for the clause, never the capture's `:84`.

**Grounding additions (in scope beyond the filing's letter):**

- **`vlt-lint/SKILL.md:43`** — the Step-0 description of the inline candidacy pass names its
  reads (`revisit_after:` + `sources:`). It is where the pass's coverage is described, so it is
  where the pass's honest limit belongs alongside the report block.
- **`vlt-lint/SKILL.md:151-152`** — the `linkage_ripe` / `revisit_due` report slots. One pass,
  two slots; the denominator that makes a zero honest is a property of the pass, so it is
  written **once** covering both rather than twice (see disposition 4 for why touching
  `linkage_ripe`'s slot is not re-opening A4-1).
- **`vault-operating-contract.md`** — the contract has **no** reporting section today
  (`grep '^## ' ` returns 20 headings, none of them about what a check may claim). The new
  section is a genuine addition, not an edit; A4-1 established the precedent for shipping
  governing prose into the contract (its two A3-22 items landed at `:226`/`:228` inside
  *Sessions, sittings, and hand-offs*).
- **`spec.md:13` and `wiki-consolidation.md:13`** — the two conventions at
  `enforcement_stage: declared`, i.e. precisely the ones the adoption facet exists for, and
  neither carries it. These are the instances F6 stamps.

Nothing found here contradicts an ideation ruling; no block.

---

## Brief-time dispositions

The roadmap left three questions to this brief, and A4-1 handed down two obligations. All five
are ruled here.

### 1. Where the general honest-reporting rule lives → **`vault-operating-contract.md`, a new `## Honest reporting — what a check may claim` section.**

*(Deferred question: "where the honest-reporting rule lives", left open at the silent-zero
decide-once ruling — "the cost the owner accepted is a governance decision about where the rule
lives, which is left to the brief that writes it".)*

Three homes were live. The ruling:

- **A new `{conventions}/reporting.md` — rejected.** It would need `version:`/`consumers:`, an
  enforcement declaration, a consumer walk on every future wording change, and — the decisive
  objection — it would ship at `enforcement_stage: declared` with zero instances, i.e. it would
  be a **fifth instance of the very scar this build exists to close**. A build whose subject is
  "declared and never exercised" may not create another declared-and-unexercised surface.
- **`frontmatter.md` — rejected.** It is the *schema* single-source; a rule about how a check
  reports is not a frontmatter rule. Worse, it is handshaked at `version: 4` with five
  consumers, so every future clarification of the reporting rule would drag a five-consumer
  re-ack behind it. The rule will be cited by A4-3, A4-4 and beyond; it must be cheap to sharpen.
- **The operating contract — chosen.** It is the home of the **shared operating rules**
  (`:19`), it is **deliberately not handshaked** (CLAUDE.md: the contract uses single-home +
  pointers instead), and it is internalized into every partner's SKILL.md, so the rule reaches
  partners writing their own reports as well as op skills emitting structured ones. The rule is
  constitutional in exactly the contract's sense: it constrains what any partner may *claim*.

**Cost accepted and recorded:** the contract grows by one section, and a contract edit is a
shipped-surface change that rides `vlt-upgrade`'s reconcile path (already exercised by A4-1; the
detect-and-report net at `vlt-upgrade:104` `governance_divergence` covers a locally hand-edited
contract).

### 2. The derive-first boundary clause → **RELOCATED into that same section, with `vlt-lint:84` reduced to a pointer.**

*(A4-1 handoff obligation 1: "A4-2 either relocates that clause into that home or points at it —
it must not create a second home.")*

Relocate, don't point-from-the-contract. Reasons: (a) both rules are about *how a check may
establish and report truth* — they are one family and reading them together is what makes either
land; (b) governance pointing **into** a skill for its own doctrine inverts the module's
direction of reference (skills point at governance, not the reverse); (c) A4-1 itself recorded
that the clause sat in `vlt-lint` only because "no derive-first doctrine file exists and both
candidate homes cost more than the clause" — this build creates the home, so the reason expires.

**This does not legislate derive-first itself into governance.** The clause is relocated *as
worded* — a boundary on an existing discipline whose two concrete homes stay where they are
(`vlt-upgrade:44`, and the enforcement counters). The ideation ruling was explicit: state it as a
boundary clause, **not** as a new standalone invariant. The builder must not expand it into a
statement of derive-first.

### 3. Where the `adoption_first_instance:` consuming check lives → **outside lint: `vlt-upgrade`'s post-flight report (the consumer) and `vlt-mint`'s ceremony (the writer). `frontmatter.md:242` is NOT revisited.**

*(ODQ #3, the hard-bounded question: "the first consumer either lives outside lint, or the brief
revisits `:242` explicitly and says so. It may not quietly contradict it.")*

The facet needs three things to stop being declared-and-unexercised, and a "consumer" alone is
not enough — a consumer of a key nothing ever writes is the same scar one layer up. So:

- **Instances (F6):** the two `declared`-stage conventions carry the key explicitly at `null`,
  rather than by absence. This matters because `:242` says *null/absent* — and the report in F7
  can only be three-valued (adopted / declared-not-yet / axis-not-declared) if some conventions
  actually declare the axis. An explicit `null` is the difference between "we asked and the
  answer is no" and "we never asked".
- **Writer (F8): `vlt-mint`.** `frontmatter.md:240` already fixes the ceremony as the only place
  a convention's enforcement frontmatter legitimately changes ("stage promotions… happen through
  the mint ceremony — dated entries in `_agent/mint/decision-log.md` — never through lint").
  A first-instance stamp is the same shape of event, so it belongs on the same beat and gets the
  same decision-log record. No new machinery.
- **Consumer (F7): `vlt-upgrade`'s Step-4 post-flight report + Step-5 ledger block.** An upgrade
  is the moment conventions arrive, and the ledger is the module's existing home for
  "how far has this vault drifted / moved". Reporting per-convention adoption there gives the
  facet a real consumer at a real cadence, with a **durable, append-only record** so
  declared-but-never-adopted becomes visible *over time* rather than only in one run's output.

**`frontmatter.md:242` stands unrevisited and uncontradicted** — the check lives outside lint,
exactly as `:242` anticipated ("whatever checks consume it… live where those checks live").

**Why not `vlt-track`'s loop-profile non-vacuity gate** (the other consumer `:242` names): that
gate does not exist yet, so choosing it would defer the wiring instead of doing it — the failure
mode this build is fixing. It remains a legitimate *second* consumer whenever it is built.

### 4. The two-outcome question's shape → **a required ask in both write beats, with the answer recorded in frontmatter only when it is a date; the decline is made visible in the *report*, not the schema.**

*(Deferred question: "the two-outcome question's shape in both templates".)*

The tempting design — write `revisit_after: none` on a decline so the decline is countable — is
**rejected**: it changes `frontmatter.md:138`'s settled semantics (*absence = not a candidate*),
which is a rule change, which bumps `frontmatter@4 → @5` and drags a five-consumer re-ack, to
make a decline countable. The ruling instead:

- **Both write beats ask, and the ask is not skippable.** One line, two named outcomes: *set a
  recheck date, or say in-flow why this note isn't a graduation candidate.* The point of the
  0-of-96 diagnosis is that the ingest path never **saw** the slot — being shown the slot and
  declining it is a legitimate outcome and is what "two-outcome" means. The templates carry the
  key identically so the two paths cannot diverge again.
- **Absence keeps its meaning** (`frontmatter.md:138` untouched), so no legacy backfill and no
  version bump.
- **The decline's invisibility is handled by the honest-reporting rule instead** — `vlt-lint`'s
  candidacy pass reports the denominator, so a `revisit_due: []` states *how many notes carried
  the key at all*. That is exactly the filing's shape 3, discharged by conformance to the general
  rule rather than by a bespoke fix, per the decide-once ruling.

### 5. The new filing's honesty half → **closed for free by the rule; the missing-check half stays with capture.**

*(A4-1 handoff obligation 2: `inbox/2026-07-25-193000-report-slot-with-no-check.md`.)*

`sources_vs_prose_mismatches` (`vlt-lint:137`) is a declared `fix_now` key no Step-2 check fills.
Its **honesty** half is governed by the rule F3 writes — a report key that no check produces is
the limiting case of a count whose only attainable value is "fine". The rule as worded covers it.
**This build does not delete the slot and does not define the check** — the filing's own
disposition (a)/(b)/(c) is capture's to rule, and its option (b) turns on a `write-verification.md`
tier-1/tier-2 membership test that is that file's call, not this brief's. Recorded so a later
reader does not read this build's silence as a ruling. See *Out of scope*.

---

## F1 — `vlt-research/SKILL.md`: the write beat asks

**Current state.** `skills/vlt-research/SKILL.md:52-83`, Phase 4. The template at `:58-73`
already carries the key at `:71`:

```yaml
revisit_after: YYYY-MM-DD          # OPTIONAL — graduation-candidacy recheck date; absence = not a candidate (see frontmatter.md)
```

Nothing in the phase asks the partner to fill it. `grep -rn "revisit_after" skills/vlt-research`
returns exactly one hit — the template comment. The key is offered and never requested.

**The exact change.** Leave `:71` byte-unchanged. Add the two-outcome ask as a short bolded
paragraph between the template fence (`:73`) and the `Structure (no key: field):` line at `:75`:

> **Decide `revisit_after:` before you write — two outcomes, both legitimate.** Either set a
> recheck date (when should this note's *graduation candidacy* — its readiness to become a wiki
> page — be looked at again?), or say in-flow why this note isn't a graduation candidate and
> omit the key. Absence means *not a candidate* (`{conventions}/frontmatter.md`), so an
> unconsidered omission and a deliberate decline look identical on disk — which is why the
> decline is spoken, not silent. Don't default to omitting it because the slot is optional.

**Why.** A3-19's core finding: the mechanism works perfectly and nothing ever invokes it
(`revisit_due` behaves exactly as specified — this is adoption, not logic). The ruling: the key
plus a two-outcome question lands in both writers.

**Out of scope at this site.** Phase 5's tier-1 checklist run is untouched — `revisit_after:` is
optional and must not become a verification failure.

## F2 — `vlt-ingest/SKILL.md`: the majority path finally sees the slot

**Current state.** `skills/vlt-ingest/SKILL.md:71-93`, Step 5. The research-note template at
`:77-91` emits `type / created / title / author / trust / topic / status / sources` and stops —
**`revisit_after:` is absent entirely.** This is the mechanical explanation for 0-of-96 that the
filing missed, and it is strictly better than "partners never elect it": on this path there is
nothing to elect.

**The exact change.** Two edits, mirroring F1:

1. Add the key to the template as the last field, **byte-identical to `vlt-research:71`**
   (including the comment) so the two schemas cannot drift again:

```yaml
sources:
  - <source filename or URL>
revisit_after: YYYY-MM-DD          # OPTIONAL — graduation-candidacy recheck date; absence = not a candidate (see frontmatter.md)
---
```

2. Add the **same two-outcome ask** as F1 — same wording, adapted only where the phrasing names
   the note ("this note" reads the same on both paths, so prefer verbatim reuse). Place it after
   the template fence (`:91`) and before the `Sections:` line at `:93`.

**Why.** The ruling is explicit that a `vlt-research`-only fix leaves the 0-of-96 mechanism
intact, because ingest is the majority write path on a vault that consumes external sources.

**Out of scope at this site.** Step 5's **hand-off branch** (`:73`) is untouched: when the
"source" is already a research note, no new note is created, so there is no slot to ask about.
Step 6's wiki-page template (`:107-125`) is untouched — `review_after:` is a different key on a
different axis (`frontmatter.md:138` states the relationship) and is not in this build's scope.

## F3 — `vault-operating-contract.md`: the honest-reporting rule, stated once

**Current state.** `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` — 20
`##` sections, none about reporting. The contract's self-description at `:19` establishes it as
"the home of the **shared operating rules**". A4-1's two prose items landed inside
*Sessions, sittings, and hand-offs* at `:226` and `:228`, so the pattern of shipping governing
prose here is established.

**The exact change.** Add a new section. Place it **immediately after `## How to write`
(`:240-248`) and before `## Reading list` (`:250`)** — "how to write" governs what a partner
commits to disk, this governs what a partner *claims about what it found*, and the adjacency is
the point.

```markdown
## Honest reporting — what a check may claim

**A count whose only attainable value is "fine" must state what it cannot see.** Any check,
sweep, or report that surfaces a count — findings, violations, candidates, gaps — reports
alongside it the **population it ran against** and the **class it structurally cannot detect**.
A bare zero is indistinguishable from "never ran", "ran against nothing", and "cannot see this
class at all"; a consumer (human or dashboard) reads all four as health. State the denominator,
and name the blind spot in the same breath as the count. A report key that no check fills is the
limiting case — it can only ever render empty, and an always-empty slot is a claim of health
nothing earned.

This is the single-home posture applied to reporting: **the rule is stated here and cited
elsewhere.** A check does not word its own version of it.

**Boundary clause on derive-first.** Derive-first does not license deriving a state from the
residue of the very process that produces it — where the only available signal is the process's
own leavings, the state must be recorded, not inferred, or the check must be read in the polarity
the evidence actually supports. The two rules are one family: this one governs how a check
establishes a truth, the one above governs what it may claim about it.
```

**Why.** The silent-zero decide-once ruling (ONE general rule, stated once; every site conforms
rather than inventing its own wording) plus A4-1 handoff obligation 1 (relocate the boundary
clause into this home or point at it, never a second home). Disposition 1 and 2 above set the
home and the relocate-vs-point call.

**Single-home implications the builder must honor.** After this lands, the wording of both rules
exists in **exactly one** file. `vlt-lint` points (F4). A4-3, A4-4 and any later conformer cite
`{conventions}`-adjacent contract prose by name and **never restate it**. Note the contract is
*not* in `{conventions}/` — it is the constitution beside them — so it carries no
`version:`/`consumers:` and this section triggers **no handshake and no re-ack** (CLAUDE.md: the
operating contract is deliberately NOT handshaked; it uses single-home + pointers).

**Out of scope at this site.** No other contract section is edited. In particular *How to write*
(`:240-248`) does not gain a reporting bullet — that would be a second home in the same file.

## F4 — `vlt-lint/SKILL.md`: point at the home, and make the candidacy pass honest

**Current state.** Three sites, all freshly re-grounded:

- `:84` — the derive-first boundary clause, stated in full inside the candidacy-pass header
  (A4-1's disposition 2: "its governance home is deferred to A4-2").
- `:94` — the `revisit_due` bullet (the capture's `:84`; moved by A4-1, text byte-unchanged):
  "**Absence of `revisit_after:` = not a candidate = zero findings** — legacy research notes
  generate no noise (backfill is a non-event by construction)."
- `:43` (pass description, names the per-note reads) and `:151-152` (the two report slots).

**The exact changes — four edits:**

1. **`:84` becomes a pointer.** Replace the stated clause with one line, keeping its
   *instance-local* second sentence (which is about this pass specifically and is not general
   doctrine, so it stays here):

   > **Boundary clause on derive-first** — stated once in the operating contract
   > (*Honest reporting — what a check may claim*); read it there, not from memory. Applied here:
   > this pass derives *absorption* (evidence the wiki has taken a note up), never *graduation*
   > (the event) — which is why **absence** of linkage is the signal and presence of it is not.

2. **`:94` gains its honest limit**, appended to the existing bullet (do not rewrite the
   existing sentences):

   > Reported per the operating contract's honest-reporting rule: a zero here means *no note
   > carrying the key is past due*, **not** that the zone has no graduation candidates — state
   > how many notes carry `revisit_after:` at all, of how many research notes, so the zero is
   > readable.

3. **`:43` names the pass's blind spot** — one clause appended to the sentence describing the
   inline candidacy reads: the pass sees only notes on disk in `{research}` at run time and can
   say nothing about notes that never carried the key, which is what the denominator reports.

4. **`:151-152` carry the denominator, once, for both slots.** The candidacy pass is one pass
   with two findings, so the coverage line is written once above them rather than duplicated
   into each:

```yaml
  research_zone: <M notes scanned; N carry revisit_after:>   # candidacy-pass denominator — a bare zero below is not health
  linkage_ripe: [<research-note — no absorption linkage: cited ∪ inbound wikilink ∪ shared sources>, ...]
  revisit_due: [<research-note — revisit_after YYYY-MM-DD past>, ...]
```

**Why.** Edit 1 discharges A4-1 handoff obligation 1 without creating a second home. Edits 2–4
are this build's own site conforming to the rule it writes — the filing's shape 3, discharged as
conformance per the decide-once ruling.

**Why touching `linkage_ripe`'s slot is not re-opening A4-1.** A4-1 shipped that finding's
*definition, polarity and legs*; none of that is touched. What changes is the **pass-level
coverage line** that sits above both slots — and writing it twice (once per slot) would be
exactly the per-site bespoke wording the decide-once ruling forbids. A4-1 explicitly deferred
"the general honest-reporting rule and any report-line silent-zero fix" to this build.

**Out of scope at this site.** `:137` `sources_vs_prose_mismatches` is **not** deleted and **not**
given a check (disposition 5). No other report slot gains a denominator in this build —
`contradictions_handled` is A4-3's site and its disposition is A4-3's to make.

## F5 — `frontmatter.md:242`: name the facet's now-real consumers

**Current state.** `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:242`
closes the adoption-axis paragraph with: "Whatever checks consume it — a convention's
first-exercise acceptance, a loop profile's non-vacuity gate — live where those checks live;
this declaration defines only the facet." As of today those consumers are hypothetical.

**The exact change.** Append one sentence to `:242`, naming the real ones:

> *Live consumers today:* `vlt-mint` stamps the facet when a mint ceremony produces a
> convention's first live instance (the same ceremony that promotes `enforcement_stage`), and
> `vlt-upgrade`'s post-flight report + upgrade ledger surface each convention's adoption state.
> Its absence remains **not** a `vlt-lint` finding.

**Why.** The facet's own definition invites naming its consumers, and leaving it un-named after
this build wires two of them is precisely the declared-with-no-consumer reading A3-19 caught.

**⚠️ This does NOT bump `frontmatter@4`, and the builder must not bump it.** Per CLAUDE.md's
version-handshake rule, a `version:` bump is for a **rule change**; prose clarifications don't
bump. This sentence changes no rule any of the five consumers (`vlt-ingest`, `vlt-extract`,
`vlt-research`, `vlt-lint`, `vlt-mint`) must follow — it records who already consumes an
existing optional facet, and it re-states the existing lint carve-out unchanged. A bump here
would drag a five-consumer re-ack for a factual note. Verification 5 checks that no `version:`
line moved.

**Out of scope at this site.** `:133` and `:138` (`revisit_after:`'s schema line and semantics)
are **untouched** — disposition 4 rules that absence keeps its meaning, which is what keeps this
whole build off the handshake path. `:237`'s schema line is untouched.

## F6 — `spec.md` + `wiki-consolidation.md`: the facet gets explicit instances

**Current state.** The two conventions at `enforcement_stage: declared` —
`conventions/spec.md:13` and `conventions/wiki-consolidation.md:13` — are exactly the ones the
adoption facet exists for, and neither carries it. Zero of seven shipped conventions do.
`spec.md` is the example `frontmatter.md:242` itself names ("the first real spec minted under
`spec.md`").

**The exact change.** Add one line to each file's frontmatter, in the enforcement block, in the
key order `frontmatter.md:227-238` establishes (after the deferral trio):

```yaml
adoption_first_instance: null        # no first live instance yet — declared, not yet adopted
```

`spec.md` frontmatter currently ends its enforcement block at `review_after: 2026-08-17`
(`:16`); `wiki-consolidation.md` follows the same shape. Insert after that line in both.

**Why.** Disposition 3: an explicit `null` is what makes F7's report three-valued. Without it,
"has not been adopted" and "does not declare the axis" are the same absence — the exact
ambiguity the honest-reporting rule forbids.

**⚠️ Neither convention's `version:` bumps either.** `spec.md` stays `version: 1` /
`consumers: [vlt-mint, vlt-dispatch, vlt-upgrade, vlt-lint]`; `wiki-consolidation.md` stays
`version: 1` / `consumers: [vlt-ingest]`. Adding an optional, self-describing enforcement facet
to a convention's own frontmatter changes nothing a consumer must do — it is the same class of
edit as declaring a deferral, which the enforcement-declaration section already treats as the
file describing itself. No re-ack.

**Out of scope at this site.** The five `checked`-stage conventions (`frontmatter`, `extraction`,
`wiki-index`, `wiki-supersession`, `write-verification`) are **not** stamped. Stamping a
broadly-exercised convention with a synthetic first-instance date would be fabricating a
provenance record nobody witnessed; F7's third value ("axis not declared") reports their state
honestly instead. This is a deliberate asymmetry — record it in the build's `status:` if the
builder is tempted to normalize it.

## F7 — `vlt-upgrade/SKILL.md`: the consuming check

**Current state.** Step 4 — Post-flight divergence report, `:88-109`; the parseable summary block
at `:92-107` carries `mints_preserved`, `overlays_intact`, `baselines_refreshed`,
`base_divergence`, `skill_asset_divergence`, `migrations_run`, `governance_divergence`,
`capabilities_intact`, `family_invariant_drift`. Step 5 — the append-only standing ledger,
`:111-131`, whose per-upgrade block (`:120-128`) mirrors those lines. Neither reads convention
enforcement frontmatter.

**The exact change.** Two edits:

1. **Report line**, added to the Step-4 YAML block after `governance_divergence:` (`:104`):

```yaml
  convention_adoption: [<convention: adopted <ref> | declared, no first instance yet | axis not declared>, ...]
```

   with a sentence below the block (beside the `:109` note that explains the divergence keys)
   defining it: for every `{conventions}/*.md`, read `adoption_first_instance:` — a dated
   reference reports **adopted**; an explicit `null` reports **declared, no first instance yet**;
   the key's total absence reports **axis not declared** (this report cannot tell that case from
   an unexercised one, which is why the three values are distinct). Per the operating contract's
   honest-reporting rule, the line is **never omitted when empty** — an absent line would read as
   "all adopted".

2. **Ledger line**, added to the Step-5 block template at `:127` (after `Governance divergence:`):

```markdown
- Convention adoption: <list>        # per-convention: adopted <ref> | declared, not yet | axis not declared
```

**Why.** Disposition 3 — the facet's first real consumer, outside lint, honoring
`frontmatter.md:242`. The ledger half is what makes "declared and never adopted" visible **across
upgrades** rather than in one run's scrollback; that longitudinal record is the property A3-19
found missing (nothing anywhere could have told the owner the key was at 0-of-96).

**Out of scope at this site.** `vlt-upgrade`'s Step 1 pre-flight, the reconcile pass, and the
`Verify` block (`:140`) are untouched — the adoption line is a *report*, never a gate, and must
not be able to block or fail an upgrade. `vlt-upgrade` gains no `depends_on` entry: it is already
a `spec.md` consumer, and reading a convention's own frontmatter facet is not consuming
`frontmatter.md`'s schema rules in the handshake sense (it does not recite the schema; it reads
one declared key). If the builder judges otherwise, that is a deviation to record in `status:`,
not a silent bump.

## F8 — `vlt-mint/SKILL.md`: the writing beat

**Current state.** Phase 3 — Build; `### Step 4: Install and register` at `:165-179`. The mint
decision-log entry schema is at `:68-87`. `frontmatter.md:240` already fixes this ceremony as the
only legitimate place a convention's enforcement frontmatter changes: "Stage promotions
(`declared → checked → enforced`) happen through the mint ceremony — dated entries in
`_agent/mint/decision-log.md` — never through lint."

**The exact change.** Add a short beat to Step 4 (place it beside the existing register steps,
not as a new phase):

> **Stamp first adoption when a mint produces one.** When this ceremony produces the **first
> live instance** of a boundary a `{conventions}` file declares — the first spec minted under
> `spec.md`, the first consolidation performed under `wiki-consolidation.md` — set that
> convention's `adoption_first_instance:` to a dated reference to the instance and record the
> stamp in `_agent/mint/decision-log.md` alongside the ceremony's other rulings. It is a stamp
> set **once, never a counter** (`{conventions}/frontmatter.md`, *Adoption axis*) — if the key
> already carries a date, leave it. Nothing else may write this key; `vlt-lint` never does.

**Why.** Disposition 3 — without a writer, the consumer in F7 reports `null` forever and the
facet stays declared-and-unexercised, which is the scar this build closes. Mint is the ceremony
that already owns edits to convention enforcement frontmatter, so this adds a beat, not a
mechanism.

**Out of scope at this site.** The blast-radius gate (`:92-117`), the becoming conversation, and
the planning doc are untouched. The beat is **conditional and cheap** — most ceremonies produce
no first instance and skip it; it must not become a mandatory prompt on every mint.

---

## Registration

**None.** No new skill, no new workflow, no new dispatch mode — so no `module-help.csv` row and
no header work. **No convention `version:` moves** (F5 is a prose clarification, F6 stamps an
optional self-describing facet — both dispositioned above with the reason), so there is **no
consumer walk and no re-ack** in this build. The operating contract is deliberately not
handshaked and registers nothing by design.

Not a release build: the owner is holding the module version to arc end, so neither
`.claude-plugin/marketplace.json` nor `skills/vlt-setup/assets/module.yaml` is touched. The
version bump rides the last Arc-4 build.

## Out of scope (dispositioned)

- **Defining or deleting `sources_vs_prose_mismatches`** (`vlt-lint:137`) — *deferred to
  capture*. Its honesty half closes via F3's rule; its missing-check half is
  `inbox/2026-07-25-193000-report-slot-with-no-check.md`'s (a)/(b)/(c), which turns on a
  `write-verification.md` tier-membership test that is that file's call. Disposition 5.
- **`contradictions_handled`'s silent zero** (`vlt-lint:160`) — *deferred to A4-3*, which owns
  that filing and cites F3's rule rather than wording its own.
- **Ingest-side entity/count reporting** — *deferred to A4-4*, same reason.
- **Bumping `frontmatter@4 → @5`** — *rejected*; F5 and F6 are not rule changes, and disposition
  4 deliberately chose a two-outcome shape that keeps `:138`'s semantics intact precisely to stay
  off the handshake path.
- **Writing `revisit_after: none` on a decline** — *rejected*; it buys countability at the cost
  of a schema rule change plus a five-consumer re-ack, and the denominator in F4 gets the same
  visibility for free. Disposition 4.
- **Stamping the five `checked`-stage conventions with a first-instance date** — *rejected*; no
  witnessed instance exists to cite, and fabricating one is a provenance lie. F7's third report
  value covers them honestly. F6.
- **A new `{conventions}/reporting.md`** — *rejected*; it would ship declared-and-unexercised,
  a fifth instance of this build's own subject. Disposition 1.
- **Making the adoption line a gate in `vlt-upgrade`'s `Verify` block** — *rejected*; adoption is
  an **absence**, not a violation (`frontmatter.md:242`), and a gate on an absence would
  re-create the `declared_untripwired` confusion the enforcement-declaration section already
  resolves. F7.
- **`vlt-track`'s loop-profile non-vacuity gate as the facet's consumer** — *deferred*; it does
  not exist yet and choosing it would defer the wiring rather than do it. A legitimate second
  consumer when built. Disposition 3.
- **The brief-restatement drift class** (`inbox/2026-07-25-171500-brief-restatement-drift.md`,
  and the roadmap's *Open items not owned by any build*) — *not this build's*; it is factory
  tooling, not module source.
- **`vlt-research` Phase 5 tier-1 checklist** — *untouched*; `revisit_after:` is optional and
  must never become a verification failure. F1.

## Verification (unit, at rest — lifecycle step 5)

Run every check; record any that does not pass in the build's `status:` as a numbered deviation.

1. **Both writers carry the key, byte-identically.**
   `grep -rn "revisit_after" skills/vlt-research skills/vlt-ingest` → exactly one hit per file,
   and the two lines are **character-for-character identical** (diff them, don't eyeball).
2. **Both writers carry the ask.** Each template fence is followed by the two-outcome paragraph;
   the wording is the same on both paths (F1/F2).
3. **The boundary clause has exactly one home.**
   `grep -rn "residue of the very process" skills/` → **one** hit, in
   `vault-operating-contract.md`. `vlt-lint:84` matches only a pointer (`grep -n "Boundary clause
   on derive-first" skills/vlt-lint/SKILL.md` → one hit, and the surrounding text names the
   contract).
4. **The honest-reporting rule has exactly one home.**
   `grep -rn "only attainable value" skills/` → **one** hit (the contract). No later site
   restates it; conformers point.
5. **No handshake moved.** `git diff -U0 -- skills/vlt-setup/assets/governance/` shows **no**
   changed `version:` or `consumers:` line in any `{conventions}/*.md`. Then run the bipartite
   re-check anyway (every consumer listed ↔ every ack current) — it must be unchanged from
   `4ca619e`.
6. **The facet is wired end to end.** `grep -rn "adoption_first_instance" skills/` returns
   `frontmatter.md` (`:237`, `:242` + the F5 sentence), `spec.md`, `wiki-consolidation.md`,
   `vlt-upgrade/SKILL.md`, `vlt-mint/SKILL.md` — a writer, two instances, a consumer, and the
   definition. Nothing in `vlt-lint`.
7. **The report block is well-formed.** The `vlt-lint` Step-5 fence and the `vlt-upgrade` Step-4
   fence still parse as YAML with the new keys present, and every new key is a stable
   snake_case identifier (a dashboard consumes these).
8. **Packaging lint.** `uv run tools/package-lint.py` — Groups A/B/C/E PASS. (Group D /
   `--expect-version` is the release gate, not this build's; this is not a release build.)
9. **Scrub.** No personal or vault-local content in any changed shipped file; no worked example
   gained a specific install's artifact path (CLAUDE.md publishing rules). The contract's new
   section uses no vault-specific example.
10. **No cruft.** No per-skill `.decision-log.md` anywhere in the working tree
    (`find skills -name '.decision-log.md'` → empty) — they are gitignored but ship into vaults
    through `vlt-upgrade`'s filesystem copy.
11. **`status:` rewritten** to a BUILT record with numbered deviations, and **one commit** for
    the build.

## Acceptance (live — appended to the roadmap ledger)

Rides the next ordinary vlt-core upgrade + the sittings that follow it.

1. **Both write paths ask, and the field can answer either way.** After upgrade, the installed
   `vlt-research` and `vlt-ingest` both carry `revisit_after:` in their research-note templates
   and the two-outcome ask; the next research note written by **each** path shows the partner
   either setting a date or naming the decline in-flow. The ingest path is the one that matters —
   it is the majority path and the one that could not see the slot.
2. **Adoption moves off zero.** Within the first sittings after upgrade, at least one newly
   written research note carries `revisit_after:`, breaking the 0-of-96. *Days-to-first-check:*
   the first research or ingest write after upgrade. A run of new notes with **no** date and
   **no** spoken decline is the failure signature — it means the ask is being skipped, not
   answered.
3. **The candidacy pass reports honestly.** The next full `vlt-lint` run's report carries the
   `research_zone:` denominator above `linkage_ripe`/`revisit_due` (M notes scanned, N carrying
   the key); no bare zero appears on either slot. This is A3-19 shape 3 discharged by conformance,
   not by a bespoke fix.
4. **The adoption facet has a live consumer.** The upgrade's post-flight report emits
   `convention_adoption:` with a three-valued line per shipped convention — `spec.md` and
   `wiki-consolidation.md` reporting **declared, no first instance yet**, the five `checked`
   conventions reporting **axis not declared** — and the same line is appended to the upgrade
   ledger block, so the state is durable and comparable at the *next* upgrade.
5. **The stamp is reachable, not just declared.** If a first live instance occurs in the window
   (the first spec minted under `spec.md`, the first consolidation under
   `wiki-consolidation.md`), `vlt-mint` stamps `adoption_first_instance:` with a dated reference
   and the mint decision log records it; the following upgrade then reports that convention as
   **adopted**. **Non-blocking if no such instance occurs** — but the absence must show up as
   *declared, no first instance yet* in check 4, never as silence.
6. **Single home holds in the field.** The installed operating contract carries the
   honest-reporting rule and the derive-first boundary clause; the installed `vlt-lint` carries a
   pointer and no restated wording; any vault-local convention overlay is untouched by the
   upgrade (`overlays_intact` in the post-flight report).
7. **Second-vault check, non-blocking.** A3-19's honest limit is one vault and four post-fix
   notes. If vlt-sayari becomes readable, confirm both writers carry the key there too and that
   its adoption line reports the same three-valued shape. The fix does not wait on this.

---

## Roadmap notes written by this brief

Appended to `skills/reports/inbox-evolution-arc4-roadmap.md` in the same run:

- The **A4-2 acceptance bullet** in the *Deferred acceptance ledger (Arc 4)*, carrying checks 1–7
  above.
- A **superseding note** in the roadmap's status section recording the one grounding correction:
  the A3-19 capture's `vlt-lint:84` (`revisit_due` report line) now lives at **`:94`** after A4-1
  shifted it; `:84` is now the derive-first boundary clause. Text byte-unchanged; a line shift,
  not a scope change.
