---
title: 'Build #B10-3 — repeat-aware spec-candidate reporting (new candidates report loud; unchanged already-filed candidates collapse to one denominated standing line instead of re-firing every run)'
status: 'BUILT 2026-08-21 — all three F-sites landed as prose edits inside skills/vlt-lint/ (checks.md:47 repeat partition + extended records-never-reports derivation sentence; report.md:56-57 annotated loud slot + spec_candidate_standing: denominated sibling; fix-and-file.md:47 filing-quiets pointer clause + :53 Guard signal-refresh). Verification: grep 1 — spec_candidate_standing in exactly checks.md + report.md within skills/ shipped surface; grep 1b — spec_candidate site set unchanged from brief time plus the new mentions, no new home restates mechanics; grep 2 (A3) — no shipped text directs reading {lint_reports}/prior reports for repeat detection (hits: SKILL.md:72 persist instruction, the two new negative statements, and full-scale.md:7 pre-existing walker-exemption of lint_reports — the exemption A3 preserves, not a read); grep 3 — no stored counter / Never auto-promote / decline exclusion / relay entries only / empty-handoffs closer all survive verbatim, checks.md:48 posture-above citation still true; package-lint A/B/C/E PASS (D skipped, no tag — vlt 0.12.0). Six-case desk-check, each resolving unambiguously from shipped text alone: (a) new candidate no item → loud `new` + Step-4 files; (b) open item same signal → standing line only; (c) open item signal grew → loud `signal changed` + clause refreshed in place; (d) recorded decline live or drained → excluded before the partition, honored-declines count stated; (e) empty _agent/handoffs/ → no findings, no standing line; (f) doc promoted to {specs} → absent from handoffs, no finding. No .decision-log.md in the tree. Deliberate deviations: (1) F2 comment wording tuned per the brief''s own builder-tunes clause — the loud-slot comment names the partition''s home ("Step 2''s repeat partition") and the standing-line comment drops the brief''s "(D3)" ruling tag (shipped files never cite roadmap rulings); load-bearing content shipped verbatim. (2) Grep 2''s expected hit set gains one pre-existing site the brief did not enumerate: full-scale.md:7 excludes lint_reports from the walker predicate — recorded as an observation, A3-compliant by construction, no text changed. One commit for the build.'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-21-100000-spec-candidate-relay-count-six-repeat-false-positives.md (A10-1 — the naive relay-count check re-fires the same six false candidates every run; decline mechanism live since v0.9.0, three field runs, six repeats, zero declines — the field indicts the per-candidate ritual, not the mechanism''s absence)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-3 grouping bullet (binds: D3); D3 (the repeat-aware report line — new candidates loud, unchanged repeats collapse to ONE quiet line with their repeat count; no human act required; the per-candidate decline path stays as-is; no batch-decline affordance); roundtable A3 (binding: repeat detection derives from vault record state — relay/backlog/archive — NEVER from prior persisted reports, keeping reports walker-exempt per Q3b''s premise and B10-3 out of E1''s census by construction; the exact derivation is this brief''s to design, returning to the owner only if vault records prove insufficient); D1 (A10-1 is a separate build from the fan-out repair — different instrument: checks.md:47, not vlt-lint-full.js).'
risk: 'low — prose edits to three reference files inside one skill (vlt-lint); no convention file touched, no version: moves, no consumer walk, no contract edit (C6 untouched), no code/workflow change (the check is inline SKILL jurisdiction, not the fan-out — R4-fanout not triggered), no new package-lint check (E4 untouched), no release in this build (v0.13.0 cuts after B10-5). The report shape gains one additive denominated line; the existing spec_candidate: slot keeps its name and position (the B10-2 slot-stability precedent).'
---

# Build #B10-3 — repeat-aware spec-candidate reporting

The `spec_candidate` check (`skills/vlt-lint/references/checks.md:47`) derives its signal
fresh every run — deliberately, no stored counter — and its only suppression is a
per-candidate recorded decline. The field evidence (A10-1): the decline mechanism has been
live since v0.9.0, and across three consecutive lint runs the same six false candidates
re-fired loud every time with zero declines recorded. The signal-vs-noise second-order
cost is the one A10-7 named: a reviewer who learns a class is noise stops reading it.

This build lands D3's ruled fix: candidates the vault has **already surfaced and filed**
(an open Step-4 backlog item exists) and whose signal is **unchanged** collapse to one
quiet denominated standing line with their count; genuinely **new** candidates — and
standing candidates whose signal has **grown** — still report loud, one entry each. No
human act is added anywhere: the collapse derives entirely from records the existing
machinery already writes (the `{backlog}` item the check's own legal response files, and
the decline records it already reads), never from prior persisted lint reports (A3).

All rejected alternatives in the parent filing and the rulings are settled — do not
re-litigate. In particular: the batch-decline affordance (D3 ruled it out — A10-1's own
evidence is that per-item rituals go unused, and D4/A4 reuses that same evidence as a
bound), any change to the per-candidate decline path (D3: stays as-is), any stored
counter or run-memory file (the check's founding posture, reaffirmed below), and any read
of `{lint_reports}` for repeat detection (A3, binding — see disposition 1).

**`binds:` roster (from the roadmap bullet, per the standing rule): D3 (as amended by
roundtable A3).** The bullet carries the roster explicitly; nothing was reconstructed.

**Naming note (two R4s):** the roundtable's **R4** is the *fan-out currency rule*; the
brief-anatomy's standing **R4** is the *enumeration-widening rule* (§Verification). This
build touches no `vlt-lint-full.js` ask or read list, so R4-fanout's audit re-run is not
triggered; where this brief says R4 unqualified it means the anatomy's rule.

## Brief-time dispositions

**✅ OWNER-REVIEWED 2026-08-23 (first-half review, dated batch): all seven dispositions
CONFIRMED.** Field evidence at review time: B10-3 discharged whole — the two-run
record-establishing collapse landed exactly as dispositions 1/4/5 predicted
(penny-treat-rotation loud once + filed, then standing-line-only on run 2, denominated).
Review record: the arc roadmap's first-half review section.

All numbered dispositions below are clerk-resolved (autonomous run 2026-08-21, owner
review pending) except where they merely apply a ruling verbatim.

1. **The repeat record is the open `{backlog}` item — A3's sufficiency question resolves
   YES, vault records suffice; no owner return needed.** *(clerk-resolved, autonomous run
   2026-08-21, owner review pending.)* A3 mandates deriving repeats from vault record
   state (relay/backlog/archive), never prior reports, and reserves an owner return for
   the case where records prove insufficient. They don't: the check's own legal response
   (`fix-and-file.md:47-51`) files a dated-in-effect backlog item per candidate, and the
   existing Guard (`fix-and-file.md:53`) already reads `{backlog}` for exactly this
   record (open item → mention in-flow, never re-file; declined → excluded). An **open
   item for the same doc** is therefore a durable, event-written trace that the candidate
   was surfaced and handed to its named owner — precisely the memory a "repeat" needs.
   This is the same record-not-residue class the consult-preconditions check
   (`checks.md:48`) cites the spec-candidate posture for: the item is written *by the
   filing act*, an event, so reading it is a record read, not a stored counter. The
   "no stored counter" clause survives intact and is restated in the edited text (F1).
2. **"Their repeat count" = the count of standing unchanged candidates on the one line.**
   *(clerk-resolved.)* D3's wording — "unchanged repeats collapse to one quiet line with
   their repeat count" — is read as the line carrying N, the number of collapsed
   candidates. A per-candidate seen-K-times counter is **not derivable from vault
   records** (how many lint runs re-fired a candidate lives only in past reports, which
   A3 forbids reading) — and under A3 that unrecoverability is by construction, not a
   gap: the state that matters is *standing-and-unactioned*, which the open item carries
   exactly. The line lists the paths beside the count, so nothing is hidden — quiet,
   never silent.
3. **A changed signal makes a standing candidate loud again, and Step 4 refreshes the
   item's recorded signal clause in place.** *(clerk-resolved.)* "Unchanged" is
   determined by comparing the currently derived signal against the signal clause the
   open item recorded at filing (`spec_candidate: <signal>` in the item template,
   `fix-and-file.md:50`) — any difference (relay count grew; a dated revision record
   appeared where the item recorded relay entries only) → the candidate reports loud
   with the escalation named, and Step 4 updates the existing item's `spec_candidate:`
   clause to the new signal (never the checkbox, owner, or closes-when — lint is the
   item's author and this is its own clause). The refresh is load-bearing: without it
   the recorded clause stays stale, every subsequent run reads "changed", and the
   collapse never converges — the fix would reproduce the defect it closes.
4. **A candidate with no filed item reports loud — record-establishing, once.**
   *(clerk-resolved.)* Where a candidate fires and no open item exists (a prior run
   surfaced it but never filed, or this is its first surfacing), it is **new** by the
   only memory the vault has, reports loud, and Step 4 files its item per the existing
   mandate — so the *next* run finds the record and goes quiet. This is honest under A3
   (an unfiled surfacing left no record) and it creates exactly the filing pressure the
   field evidence showed missing. Consequence for acceptance: on a vault whose standing
   candidates were never filed (plausibly vlt-core's six), the first post-fix run is
   legitimately loud-with-filing and the *second* run demonstrates the collapse — check
   3 below is written to accommodate both shapes.
5. **Report shape: `spec_candidate:` keeps its name and loud-entries role; the standing
   line is a new sibling denominated scalar, `spec_candidate_standing:`.**
   *(clerk-resolved.)* Slot stability is the B10-2 precedent (its BUILT record kept
   `sources_vs_prose_mismatches` stable for dashboard consumers). Loud entries gain a
   short state annotation (`new` | `signal changed — item updated`); the standing line
   follows the `local_conventions:` idiom (`report.md:39`) — a denominated inventory
   line, not a finding. Rendering rule: the line renders (denominated zero included)
   whenever the check ran over a non-empty `_agent/handoffs/`; an empty handoffs dir
   yields no findings and **no line**, preserving the check's never-alarm-on-absence
   clause verbatim.
6. **The standing-item read is live-`{backlog}`-open only; the archive read stays where
   it already is (declines).** *(clerk-resolved.)* Open items never drain — the backlog
   drain (`vlt-decay/references/drain.md:22-24`) moves resolved/Done items to the
   archive sibling only — so a standing (open) item is by construction in live
   `{backlog}` `## Open`. The decline exclusion already reads `{backlog}` **and** its
   archive-mirrored sibling (`checks.md:47`, "a drained `## Done` decline still
   counts") and is untouched. No `drain.md:36` widening is needed (see Out of scope).
7. **R1 (interim posture): not applicable** — the reporting behavior and its mechanism
   (the record-derived partition) ship in the same build; nothing lands ahead of its
   mechanism.

## F-sites

### F1 — `skills/vlt-lint/references/checks.md:47` — the Spec candidates check gains the repeat partition

**Current state (re-grounded 2026-08-21, HOLDS; B10-2's edits touched `:12-13` only —
`:47` unshifted):** the check derives the signal (dated revision record, or ≥2 `relay:`
entries in `_agent/dispatch.md` + its `{archive}`-mirrored sibling; relay entries only,
consult blocks never count), states "Derive the count from handoff file state + dispatch
relay entries; **no stored counter**", routes the legal response to a backlog filing per
`{conventions}/spec.md` *Promotion from candidate*, excludes candidates with a recorded
decline (count of honored declines stated beside the finding), and never alarms on
absence (empty `_agent/handoffs/` → no findings).

**The exact change.** After the decline exclusion and before the empty-handoffs closer,
insert the repeat partition (kept in the check's own voice, one home):

- Partition every surviving candidate by the vault's own filing record: a candidate
  with an **open** `{backlog}` item for the same doc (the Step-4 item this check's legal
  response files — the same record the Step-4 Guard reads) whose recorded
  `spec_candidate: <signal>` clause **matches the currently derived signal** is a
  **standing candidate** — collapsed onto one denominated standing line
  (`spec_candidate_standing:`, Step 5) with the count and the paths, never a per-item
  loud entry. A candidate with **no** open item reports **loud as new** (and Step 4
  files it, so the next run finds the record). A candidate whose open item's recorded
  signal **differs** from the currently derived signal reports **loud with the change
  named** (Step 4 refreshes the item's signal clause — the item, not the report, is the
  memory).
- Extend the no-stored-counter sentence rather than contradicting it: the partition
  derives from the filing record (`{backlog}` open items) and the decline record —
  records written by their own events (the Step-4 filing, the owner's decline) — never
  a stored counter and **never prior lint reports** (`{lint_reports}` is not read;
  reports stay walker-exempt). This sentence is A3's rule landing at the check's single
  home.
- The decline exclusion, the never-auto-promote posture, the relay-entries-only rule,
  drained-relay/drained-decline reads, and the empty-handoffs closer are **retained
  verbatim in force** — the edit adds the partition between exclusion and closer and
  widens the derivation sentence; it deletes nothing.

**Why:** D3 — the loud/quiet split is the ruled fix; A3 — the derivation-from-records
sentence is the binding amendment, stated at the check's own home (R3: the legal
response for the finding is unchanged and stays in this same text — a standing
candidate's "response" is that no new act is owed per run; its open item already names
the owner and closes-when).

**Out of scope at this site:** the sibling consult-preconditions check (`checks.md:48`)
cites "the `spec_candidate` posture above" for its no-stored-counter justification — the
extension above keeps that citation true; `:48` itself is not edited.

### F2 — `skills/vlt-lint/references/report.md:56` — the report schema: loud slot annotated, standing line added

**Current state (re-grounded 2026-08-21, HOLDS):** line 56, inside `flag_for_human:`:

```
  spec_candidate: [<handoff-doc — signal 2 relay entries | dated revision record; owner <partner>; M prior declines honored>, ...]
```

**The exact change.** Replace with the loud-entries template plus the standing sibling
line (shapes per dispositions 2 and 5; match the file's comment idiom, e.g. the
`local_conventions:` line at `report.md:39`):

```
  spec_candidate: [<handoff-doc — signal 2 relay entries | dated revision record; new | signal changed (item updated); owner <partner>; M prior declines honored>, ...]   # loud entries only: new candidates + standing candidates whose signal changed
  spec_candidate_standing: <N standing candidate(s) — previously filed, open backlog item, signal unchanged: <paths>>   # the quiet line (D3) — derived from {backlog} open items, never prior reports; renders (denominated zero included) whenever _agent/handoffs/ is non-empty; no line when it is empty
```

The builder tunes exact comment wording to fit the file's style; the load-bearing
content — loud-only semantics on the stable slot, the denominated standing scalar, the
records-not-reports derivation note, the empty-handoffs no-line rule — is fixed.

**Why:** the check's report surface must carry the partition or the collapse is
invisible; the derivation note keeps the walker-exempt premise readable at the report's
own home. Slot name and position stable (disposition 5).

### F3 — `skills/vlt-lint/references/fix-and-file.md:47-53` — Step 4: the filing paragraph and the Guard learn their double duty

**Current state (re-grounded 2026-08-21, HOLDS):** `:47` the spec-candidate filing
paragraph; `:49-51` the item template
(`- [ ] Promote <handoff-doc> to {specs} (maintenance, by: <owning partner>) —
spec_candidate: <signal, …>; closes when: …`); `:53` the Guard ("an existing item for
the same doc — open → mention it in-flow, never file a second; closed as declined → do
not re-file").

**The exact change.** Two additions, no deletions:

- **The Guard (`:53`) gains the signal refresh:** when the open item's recorded
  `spec_candidate: <signal>` clause differs from the signal the run just derived,
  update that clause in place to the current signal — lint edits only its own clause
  on its own filed item, never the checkbox, the `by:` owner, or the closes-when
  (never-auto-promote untouched). Note in the same breath that this open item **is**
  the repeat record the Step-2 check partitions on (`checks.md`, *Spec candidates*) —
  a stale clause would make the collapse never converge, which is why the refresh is
  mandatory, not cosmetic.
- **The filing paragraph (`:47`)** gains one clause: filing the item is also what makes
  the next run's report quiet for this candidate (the record-establishing half of the
  partition) — a pointer at the check, not a restatement of its mechanics
  (single-home: the partition lives in `checks.md:47`; Step 4 points).

**Why:** disposition 3 (the refresh is load-bearing for convergence) and disposition 4
(filing is what turns loud into quiet); the Guard is the natural home because it is
already the code path that finds the open item.

## Registration

**None.** No new skill or workflow; no `module-help.csv` row changes (vlt-lint's row
describes lint generally); no convention file is edited, so no `version:` bump and no
consumer walk / re-ack (`vlt-lint`'s `depends_on` pins — including `spec@2` — are
unchanged and stay current). Priced per the "no bump owed is not no cost" rule:
package-lint **C6** untouched (no contract edit), **E4** untouched (no new package-lint
check), **E5** untouched (no workflow-asset ack changes — `vlt-lint-full.js` is not
edited; the spec-candidate check is inline SKILL jurisdiction, per `checks.md:51`'s
governance-checks-run-inline statement and `full-scale.md`'s wiki-only sweep).

## Out of scope (dispositioned)

- **Batch-decline affordance** — rejected by D3; not built, do not re-raise.
- **The per-candidate decline path** (`checks.md:47`, `spec.md:84`) — untouched by D3's
  explicit terms; the decline exclusion continues to run before the partition.
- **`vlt-upgrade/SKILL.md:80` (proto-spec retrofit)** — shares the candidacy signal but
  is a different instrument (a human-gated, idempotent offer at upgrade cadence, not a
  per-run report), so it has no repeat-noise defect; deferred-with-no-build-owed. If a
  field filing ever shows the retrofit re-offering declined candidates, that is a new
  filing, not this build's residue.
- **`vlt-decay/references/drain.md:36`** — no widening needed: the new read targets
  `{backlog}` **open** items, which never drain (drain moves resolved items only,
  `drain.md:22-24`); the archive-spanning reads that line records (relay count,
  declines) are unchanged. Already-covered-by the existing text.
- **`spec.md` (the convention)** — the promotion-from-candidate beat, owner derivation,
  and decline semantics (`spec.md:81-84`) are untouched; the collapse is a lint
  *reporting* posture, not a spec-lifecycle rule change. No version bump (Registration).
- **E1's report-consumer census** — B10-3 stays outside it by construction (A3): this
  build adds an additive line to the report *shape* but reads no persisted report;
  B10-6's E1 walk re-derives consumers against live source at its own brief time and
  will see the new line then.
- **`vlt-lint-full.js` / R4-fanout** — no ask or read list is touched; the fan-out
  audit does not re-run (the ruled trigger is an edit to an ask or the read list).

## Verification (unit, at rest)

1. **Cross-file agreement greps:** `spec_candidate_standing` present in exactly
   `checks.md` and `report.md` (the partition's home + its report surface);
   `grep -rn "spec_candidate" skills/` shows the same site set as at brief time plus
   the new mentions — no new home restates the partition mechanics (single-home:
   `checks.md:47` states, `fix-and-file.md` and `report.md` point/carry-shape).
2. **A3 compliance grep:** no instruction in any edited file (nor anywhere in
   `skills/vlt-lint/`) directs reading `{lint_reports}` or a prior report for repeat
   detection — `grep -rn "lint_reports\|prior report" skills/vlt-lint/` returns only
   the Step-6 persist instruction (`SKILL.md:72`) and the new negative statements.
3. **Posture-survival greps:** "no stored counter", "never auto-promote"/never-promote,
   the decline-exclusion sentence, relay-entries-only, and the empty-handoffs closer
   all still present in `checks.md:47`'s edited text; `checks.md:48`'s citation of the
   posture still true against the edited sentence.
4. **Scenario desk-check (recorded in the BUILT status):** walk the edited text against
   six paper cases — (a) new candidate, no item → loud `new` + Step-4 files; (b) open
   item, same signal → standing line only; (c) open item, signal grew → loud
   `signal changed` + clause refreshed; (d) recorded decline (live or drained) →
   excluded, honored-declines count; (e) empty `_agent/handoffs/` → no findings, no
   standing line; (f) doc promoted (moved to `{specs}`) → not in handoffs, no finding.
   Each case must resolve unambiguously from the shipped text alone.
5. **Handshake:** no convention `version:` or `consumers:` moved ⇒ no Group-E delta
   expected; still run **package-lint A/B/C/E** (the mid-arc ritual) and record PASS.
6. **Fixture extension (R2): not applicable** — no release-gate check added or changed.
7. **Legal response (R3):** discharged in-place — F1 retains the finding's legal
   response at its single home and states the standing line's non-response (no new act
   owed per run; the open item already carries owner + closes-when).
8. **Enumeration widening (R4): not applicable** — no file is added to any enumerated
   class (the build adds report lines and prose, no files; nothing joins an
   always-loaded, manifest, or vitals enumeration).
9. **Scrub:** edited shipped files carry no personal/vault-local content; worked
   examples keep placeholder shapes (`<handoff-doc>`, `{backlog}` — already the file's
   idiom).

No Release section — v0.13.0 cuts after B10-5; the version bump rides that build.

## Acceptance (live — appended to the roadmap ledger)

1. **`[ship-verifiable]`** — the partition shipped whole and agrees across its three
   homes: `checks.md:47` carries the open-item partition with the extended
   records-never-reports derivation sentence (A3's rule verbatim in force) and every
   retained posture (greps 1–3 above); `report.md` carries the annotated loud slot
   (name/position stable) + the `spec_candidate_standing:` denominated line with the
   empty-handoffs no-line rule; `fix-and-file.md`'s Guard carries the mandatory signal
   refresh. Discharged at rest by the verification greps + the six-case desk-check +
   package-lint A/B/C/E PASS, recorded in the BUILT status.
2. **`[ship-verifiable]`** — A3 compliance by construction: no shipped text directs a
   read of `{lint_reports}` or any prior report for repeat detection; no
   Decay-contracts / zone-map row changes (no new persisted surface — B10-3 stays out
   of E1's census). Discharged at rest by grep 2.
3. **`[field-contingent]`** — the six-repeat field class collapses. Discharging event,
   named: **the owner's next two `vlt-lint` runs on vlt-core after the v0.13.0
   upgrade** (performer: the owner; vault: vlt-core; the governance check reads all of
   `_agent/handoffs/` in both modes, so scoped runs qualify; evidence reaches the
   factory via the persisted `{lint_reports}` files — lint already persists verbatim,
   and a factory read of those files is acceptance evidence, not repeat detection).
   Pass = any standing candidate with an open filed item and unchanged signal appears
   **only** on `spec_candidate_standing:` with the count and paths, never as a loud
   entry; a candidate lacking a filed item reports loud **once**, its Step-4 filing
   lands, and the **second** run shows it collapsed (the two-run shape is disposition
   4's record-establishing path — expected if vlt-core's six were never filed); any
   genuinely new candidate still reports loud. Fail = an unchanged filed candidate
   re-fires loud on the second run, or the standing line is absent/undenominated over
   a non-empty handoffs dir.
