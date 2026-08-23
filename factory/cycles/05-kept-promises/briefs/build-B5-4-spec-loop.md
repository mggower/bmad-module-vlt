---
title: 'Build #B5-4 — the spec loop (candidates get an owner and a promotion step, the revision signal stops reading the template back as history, and the adoption stamp becomes reachable off the mint path)'
status: 'BUILT 2026-07-29 — F1–F7 landed as briefed: spec.md 1→2 with the *Promotion from candidate* section (named-owner derivation per disposition 6, promote/decline terminal states, honored-decline exclusion) + the deferral blind-spot statement + annotated deferral_metric comment, all four consumers re-acked spec@2; vlt-lint''s spec-candidate signal re-cut to the dated-revision-record (heading named non-evidence, extended proxy-check rule cited), named-owner routing pointer, Step-4 item shape + decline guard, spec_candidate: + consult_retroactive: report keys; consult precedence comparison beside pair-presence, consult.md Enforcement prose sharpened (frontmatter byte-unchanged, no bump); vlt-upgrade retrofit signal re-cut in step + first-instance stamp beat; authority rule single-homed at vlt-mint Step 4, frontmatter.md:242 descriptive (no bump), vlt-dispatch consult-block stamp beat, adoption_first_instance: exclusion in both divergence compares, apply carry-forward in Step 2; adoption null reports declared-since age from created:. Verification: package-lint A/B/C/E PASS (Group E bipartite at spec@2), whole-fence yaml.safe_load PASS with both new keys, two-site "What changed" grep clean (survives only inside not-revision-evidence clauses), single-home greps clean, temp-fixture divergence-exclusion walk PASS (stamp-only diff clean; genuine edit still flags), consult.md/frontmatter.md frontmatter byte-unchanged, no personal/vault-local content, no .decision-log.md. Deviations/notes: (1) the F2/F3 report-key placeholder text was de-colonized (`signal 2 relay entries`, `owner <partner>`, `after created YYYY-MM-DD`) — the brief''s suggested placeholders carried a second `: ` inside flow-sequence entries, which its own verification check 3 forbids (whole-fence strict-YAML); the keys and semantics are exactly as specified. (2) F6 additionally aged the Step-4 report template line (vlt-upgrade `:105`) and not only the `:112` definition + `:131` ledger comment, so the render surface and the definition agree — smaller drift risk, same single change. Exit obligations: no .decision-log.md present; one commit for the build (release-time, not committed here).'
module_code: 'vlt'
created: '2026-07-29'
derives_from:
  - 'inbox/2026-07-26-142000-spec-convention-surfaces-candidates-nobody-accepts.md (A5-6 — the acceptance dead end: candidates terminal in the backlog, no named next owner or promotion step; the zero-adoption-unreachable deferral_metric; the unread 18-day-old adoption null)'
  - 'inbox/2026-07-26-184705-spec-candidate-revision-signal-is-template-boilerplate.md (A5-9 — the "What changed" heading leg detects a partner template, not revision (7/7 false positives), in two sites; addendum: consult_missing cannot tell a precondition from a postcondition)'
  - 'inbox/2026-07-29-120001-adoption-stamp-unreachable-beyond-mint.md (A5-15 — adoption_first_instance has one writer (vlt-mint) while module source itself creates instances by two non-mint roads; the frontmatter.md:242 internal inconsistency; the structural lock-out on where a stamp write may land)'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): grouping (B5-4 = A5-6 + A5-9 + A5-15, "The spec loop", ships fourth; "one spec.md version: bump + one four-consumer re-ack covers all three"); cross-filing ruling 2 (named-slot principle, module instance — spec_candidate named next owner + promotion step land in this build, citing the principle); pre-ideation ruling 3 via B5-3''s F8 (the extended proxy-check rule is written once in the contract — this brief CITES it, never re-words it); questions-designated (A5-6''s three candidate directions and A5-15''s second-writer vs mint-borne-only scope incl. where the stamp write lands are this brief''s to rule)'
risk: 'low-moderate — one convention RULE change (spec 1→2: the promotion step + deferral honesty repair) with a four-consumer re-ack (vlt-mint, vlt-dispatch, vlt-upgrade, vlt-lint; Group E is the net); everything else is SKILL prose and check re-cuts across five skills plus two prose-clarified conventions (no other version moves); no workflow JS is touched'
---

# Build #B5-4 — the spec loop

Goal: close the loop the three filings bracket from three sides. A5-6: the spec convention's
candidates are **offered at every lint cadence and declined by the absence of a decision** — a
`spec_candidate`'s terminal state is the backlog, no surface names a next owner or a promotion
step, and the convention cannot report its own non-adoption (a `deferral_metric` unreachable at
zero adoption; an 18-day-old `adoption_first_instance: null` whose age nothing reads). A5-9:
half of what the candidate check surfaces **should not be surfaced at all** — the "revised in
place" leg matches a section heading the module's own spec template teaches (`spec.md:63` makes
"What changed" the *required* revision mechanism), so the check scores template vocabulary as
edit history (7/7 false positives on the live vault), in two sites; and its addendum shows
`consult_missing` reading a postcondition as a precondition. A5-15: the adoption stamp the loop
should terminate in is **unreachable off the mint path** — `vlt-mint:176` is the exclusive
writer while module source itself creates first instances by two non-mint roads (the proto-spec
retrofit, the consult record), and a vault cannot self-stamp without tripping the divergence
nets. The build gives the candidate a named owner and a promotion step (the named-slot
principle's module home, per cross-filing ruling 2), re-cuts both proxy signals per the
contract's extended proxy-check rule (written by B5-3 for this brief to cite —
`vault-operating-contract.md:260`), and makes the stamp reachable and durable from every road
that produces a first instance.

All rejected alternatives in the parent filings are settled — do not re-litigate. A5-9's
"Suggested shape" blocks are owner-steered input, consumed in the dispositions below (the B5-3
precedent for A5-8); A5-6's three directions and A5-15's scope question are the questions the
roadmap designates to this brief, ruled in dispositions 1–2.

**Re-grounding (2026-07-29, HEAD `2f19251`): clean, zero grounding corrections.** B5-2/B5-3
shifted `vlt-lint/SKILL.md` lines (capture's `:86` spec-candidates → `:89`; `:81` base
divergence → `:84`); every other capture site HOLDS at its cited line (`vlt-mint:176`,
`vlt-upgrade:79/:105/:112/:131`, `frontmatter.md:242`, `consult.md:41/:57`,
`vlt-dispatch:271`, `spec.md:11-17/:50/:63/:81`). Fresh lines are used throughout. Two
**grounding additions** (EXPANDED), both inside the designated questions' scope:
(1) `vlt-lint`'s Step-5 template carries **no `spec_candidate:` report key at all**
(`vlt-lint/SKILL.md:168-198`) — the check at `:89` files and flags with no slot, the inverse of
A5-3's slot-with-no-check; the key is added (F2). (2) The stamp's landing problem has an
**upgrade half** the capture's lint-side lock-out implies but did not enumerate:
`vlt-upgrade` Step 2 refreshes base conventions wholesale (`vlt-upgrade/SKILL.md:48` — "Base
conventions **are** refreshed (they are pristine by design)") and Step 1 records any stamped
base as hand-edit divergence (`:36`), so a stamped `adoption_first_instance:` would be
clobbered back to `null` on the next upgrade even on the mint road. The "where the write lands"
ruling (disposition 2) covers both halves.

## Brief-time dispositions

1. **A5-6's three candidate directions — ALL THREE adopted, each scoped tight** (the question
   the roadmap designates to this brief).
   - **Direction 1 (the acceptance beat) is not optional here** — cross-filing ruling 2 already
     rules the principle ("a standing obligation gets a named slot and a named owner, never an
     unnamed one") and assigns its module instance — `spec_candidate` named next owner +
     promotion step — to whatever build takes A5-6. This build takes A5-6. The beat: a
     surfaced candidate is filed to `{backlog}` **with a named owner** (the doc's authoring
     partner) and a closes-when bound (promoted per `spec.md`'s new section, or declined with
     the reason recorded); `spec.md` gains the **promotion step** as a convention rule (F1) —
     which is the rule change that makes this build's `version: 1→2` bump real, exactly as the
     grouping ruling sized it.
   - **Direction 2 (the unread null's age) lands minimally**: `vlt-upgrade`'s adoption line —
     the axis's only reporter (`:112`) — states *since when* for a `declared, no first instance
     yet` value, derived from the convention's own `created:` (F6). Derive-first, no new key,
     no new reader — longevity becomes visible at the cadence that already reports the value.
   - **Direction 3 (repair the `deferral_metric`) is an honesty repair, not a new metric**: at
     zero adoption, "spec version bumps shipping without their relay entries" can never fire —
     a count whose only attainable value is "fine" (`vault-operating-contract.md:256`, the rule
     A5-6 itself cites). The repair states the blind spot in the deferral's own text and names
     the bound that actually fires regardless of adoption — the deferral's `review_after:`
     expiry (`spec.md:16`, the live 2026-08-17 clock) — rather than inventing a second metric
     (F1). It rides the same version bump.
2. **A5-15 — RULED: a second writer (not mint-borne-only), stated as a general authority rule,
   and the stamp lands in the base convention's frontmatter with the divergence machinery made
   adoption-aware** (the designated question, incl. "where a second stamp write is allowed to
   land"; the grouping row's own label — "stamp's second writer" — points the same way, and
   mint-borne-only would leave the axis permanently dishonest for the two non-mint roads module
   source itself ships).
   - **The authority rule** replaces `vlt-mint:176`'s exclusivity: *the ceremony that produces
     a convention's first live instance stamps it*. Named writers: `vlt-mint` (mint
     ceremonies — unchanged), the **spec promotion step** (F1), `vlt-upgrade`'s **proto-spec
     retrofit** (F4), and `vlt-dispatch`'s **consult record** (F5). `vlt-lint` still never
     writes it. The rule's single home stays `vlt-mint:176` (where the exclusivity sentence
     lives today); `frontmatter.md:242`'s *Live consumers today* sentence is updated to match —
     a **descriptive-sentence update, not a schema change**, so `frontmatter@4` does not bump
     (the grouping ruling's "one bump covers all three" is binding sizing).
   - **Where the write lands**: in the base convention's frontmatter — the axis's declared home
     (`frontmatter.md:237`) — and the divergence machinery learns that this one line is an
     **authorized vault-local write, not a hand-edit**: `vlt-lint`'s
     `convention_base_divergence` compare and `vlt-upgrade`'s pre-flight compare both exclude
     the `adoption_first_instance:` line, and `vlt-upgrade`'s apply **carries the vault's
     stamped value forward** when refreshing a base (F5). Without the carry-forward, every
     upgrade silently un-adopts every convention — merge-not-replace (the durability standing
     rule) applied to the one key the module instructs a vault to write into a shipped base.
   - Retro-stamping vlt-core's `consult.md`/`spec.md` for the instances that already exist is a
     **vault-side act**, not module source — the new writers stamp going forward; the field's
     existing instances get stamped the next time their road runs (acceptance check 2 does not
     depend on retro-stamps).
3. **A5-9's revision signal — RULED: the topic-heading match dies at both sites; "revised in
   place" is evidenced only by a *dated revision record*** (directions 1+3 combined; direction
   2 — `git log` — **rejected** on the filing's own caveat: the conventions do not require the
   vault to be git-managed, so a git signal cannot be load-bearing in a shipped check). Per the
   extended proxy-check rule (`vault-operating-contract.md:260` — cited, not re-worded): the
   heading is "a template's own vocabulary read back as evidence", the rule's literal named
   case; the check either narrows its claim or changes the signal. It changes the signal: a
   dated revision marker — a `[!superseded]`/`[!stale]`-style dated callout or a dated
   changelog entry ("Revised YYYY-MM-DD", a dated "What changed" *entry*) — is a deliberate
   record of the revision event, in syntax the vault already owns, and cannot be manufactured
   by a partner's prose habit. A bare topic heading ("What changed, and what it complicates")
   never matches. The relay leg is untouched — the filing grades it sound, its consult guard
   included. Both sites move in step (`vlt-lint:89` and `vlt-upgrade:79` — "two sites, one
   defect", and `:89` cross-cites "the same signals").
4. **A5-9's addendum — `consult_retroactive` is reported as a third state, its own finding and
   not a failure; the derivation is a date comparison on records that already exist.** The
   consult block header carries a timestamp (`vlt-dispatch:271`); the spec carries `created:`
   (`spec.md:50`). A consult record dated **after** the spec's `created:` reports
   `consult_retroactive` — a record exists, but it validated the contract after the fact (the
   filing's measured cost: a six-week macro error a filing-time consult would have caught).
   Present-and-prior stays `consult_missing`-clean; absent stays `consult_missing`. The
   `consult.md` Enforcement text is sharpened to name the third state — a **prose
   clarification of the check description, not a rule change** (the precondition itself —
   consult before filing — is unchanged; nothing new is demanded of any writer), so
   `consult@1` does not bump, consistent with the grouping's one-bump sizing.
5. **The promotion/decline record and the re-file guard — derive from the backlog record,
   which the decision itself writes.** A candidate's backlog item is the loop's state: open →
   the obligation stands (lint mentions the existing item, never files a duplicate — the B5-2
   Step-4 guard's posture); closed as promoted → the doc is in `{specs}` and no longer in
   `_agent/handoffs/`, so the signal itself is gone; closed as **declined** (with the reason
   recorded in the item) → the doc is excluded from future `spec_candidate` findings, with the
   count of honored declines stated beside the finding (never a silent suppression). This
   conforms to the contract's boundary clause on derive-first (`:262`): the decline is a
   **recorded decision**, not process residue — the check derives from the record the decision
   wrote, which is exactly what the clause licenses.
6. **Named-owner derivation:** the candidate's owner is the doc's **authoring partner** —
   from the handoff filename's `{owner}-to-{consumer}` shape where it parses, else the doc's
   own attribution, else the `relay:` entries' from-slug; where all three are ambiguous, the
   item is filed `by: <human>` with the ambiguity stated (a named slot is never left unnamed —
   the principle's whole point).

## F1 — `spec.md`: the promotion step, the deferral honesty repair, `version: 1→2`

**Current state.** `version: 1`, `consumers: [vlt-mint, vlt-dispatch, vlt-upgrade, vlt-lint]`
(`spec.md:11-12`); `deferral_metric: "spec version bumps shipping without their relay
entries"` at threshold 1 (`:14-15`), unreachable at zero adoption; `review_after: 2026-08-17`
(`:16`); `adoption_first_instance: null` (`:17`). The body defines the class, home, schema,
supersession, notification, and the mint-time consumer lock (`:77`) — and **no section says
what happens to a surfaced candidate**: `vlt-lint:89` mandates "Never auto-promote… routing
back to the owning partner is not lint's job", and nothing picks the routing up. The Enforcement
section (`:81`) records the two deferred lint checks and the pre-agreed escalation.

**The change.**
- **New section, after *Mint-time consumer lock*: `## Promotion from candidate`** — the
  acceptance beat, as a convention rule: *A `spec_candidate` surfaced by lint or the retrofit
  is never left unowned: it is filed to the backlog with a **named next owner** — the doc's
  authoring partner (disposition 6's derivation) — and a closes-when bound. The owner, in
  ordinary work, either **promotes** — conform the doc's frontmatter to the spec schema above
  and move it to `{specs}` per the relocation-migration discipline (single-homed in
  `vlt-upgrade`, Step 3 *Migrations* preamble — stub the old path, re-point open dispatch
  pointers; read it there), satisfying the consult precondition (`consult.md`) where the new
  spec's `consumers:` name a partner other than its `owner`, and **stamping
  `adoption_first_instance:`** if this is the convention's first live instance (the authority
  rule, `vlt-mint`, Step 4) — or **declines**, closing the backlog item with the reason
  recorded; a recorded decline is the loop's terminal state and is honored by future
  surfacing.* One home for the beat; lint and the retrofit point at it (F2, F4).
- **Deferral honesty repair** (disposition 1, direction 3): extend the Enforcement section
  (`:81`) with the blind-spot statement, and annotate the `deferral_metric:` comment to match:
  *at zero adoption this metric cannot fire — its only attainable value is "fine" — so it
  measures notification discipline once specs exist, never adoption itself; the deferral's
  `review_after:` expiry is the bound that fires regardless (`vlt-lint`'s `deferral_expired`),
  per the operating contract's honest-reporting rule (cited, not restated).*
- **`version: 1` → `version: 2`** (`:11`) — the promotion step is a rule change; the
  four-consumer re-ack is F7.

**Why.** A5-6's finding in one sentence: "the loop has a producer and no consumer." This gives
it the consumer, in the convention that owns the class, and makes the convention's own
non-adoption reporting honest.

**Out of scope at this site.** The two deferred lint checks (`spec_schema_violation`,
`spec_notification_missing`) stay deferred exactly as `:81` records — their tripwire and
escalation are untouched. The zero-specs posture stands: nothing alarms on the absence of
specs (`vlt-lint:89`'s closing sentence is preserved).

## F2 — `vlt-lint/SKILL.md`: the candidate check re-cut, the named-owner filing, the report key

**Current state.** The *Spec candidates* check (`vlt-lint/SKILL.md:89`) flags a handoff doc
"**revised in place** (carries a "What changed" section) **or** has **≥2 `relay:` entries**…";
the heading match is the template-vocabulary proxy (A5-9: 7 single-commit false positives, 0
true positives the relay leg missed). It files "to the backlog / flag for the human" with **no
named owner**, Step 4 (`:124-148`) has **no item shape for spec candidates**, and Step 5's
template (`:168-198`) has **no `spec_candidate:` key at all** (grounding addition 1) — the
check's findings have nowhere parseable to land.

**The change.**
- **`:89`, the signal**: replace the heading clause — *"revised in place (carries a **dated
  revision record** — a dated `[!superseded]`/`[!stale]`-style callout or a dated changelog
  entry; a bare topic heading such as "What changed…" is a partner template, never revision
  evidence — per the operating contract's extended proxy-check rule, *Honest reporting*)"* —
  relay leg and its consult guard byte-untouched. Keep the cross-cite to the retrofit ("the
  same signals", now true again after F4).
- **`:89`, the routing**: after "file to the backlog / flag for the human", point at the beat:
  *the item carries the candidate's **named next owner** and closes-when per
  `{conventions}/spec.md`, *Promotion from candidate* (read the beat there); a candidate with
  a recorded decline in `{backlog}` is excluded, with the count of honored declines stated
  beside the finding.*
- **Step 4** (after the entity-collision shape, `:143`): add the item shape:

  ```
  - [ ] Promote <handoff-doc> to {specs} (maintenance, by: <owning partner>) — spec_candidate: <signal, e.g. 2 relay entries>; closes when: promoted per {conventions}/spec.md *Promotion from candidate*, or declined with reason recorded
  ```

  plus the guard sentence: an existing item for the same doc — open → mention it in-flow, never
  file a second (the B5-2 duplicate-filing posture); closed as declined → do not re-file
  (disposition 5).
- **Step 5**: add to `flag_for_human:` (near `authority_scan:`/`consult_missing:`, `:196-197`):

  ```yaml
  spec_candidate: [<handoff-doc — signal: 2 relay entries | dated revision record; owner: <partner>; M prior declines honored>, ...]
  ```

**Why.** A5-9's heading leg dies where it lives; A5-6's named slot lands where the candidate is
filed; the check's findings get the report slot the honest-reporting rule assumes they have.

## F3 — the `consult_retroactive` third state (`vlt-lint/SKILL.md` + `consult.md`)

**Current state.** The *Consult preconditions* check (`vlt-lint/SKILL.md:90-92`) confirms
pair-presence only; `consult.md:41` states the rule as a **pre**condition ("before it is
filed") and its Enforcement section (`:57`) describes the presence check; no date comparison
exists anywhere — a consult fired afterward to satisfy the check reads identically (A5-9
addendum, self-demonstrated at 43 and 35 days late). Step 5 carries `consult_missing:`
(`:197`) and no third state.

**The change.**
- **`:90`**: after the pair-presence sentence, add the comparison: *compare the consult
  block's header timestamp (`vlt-dispatch`'s block shape) against the spec's `created:` — a
  record dated **after** the spec it validates reports **`consult_retroactive`** (its own
  state, not a `consult_missing`): the precondition was honored late, which is genuinely
  better than never (a retroactive consult still surfaces real defects) and is reported as
  what it is, per the operating contract's extended proxy-check rule — presence is not
  precedence.*
- **Step 5**: add beside `consult_missing:` (`:197`):

  ```yaml
  consult_retroactive: [<spec — consult for <consumer-slug> dated YYYY-MM-DD, after created: YYYY-MM-DD>, ...]
  ```

- **`consult.md:57`** (Enforcement): sharpen the check description to name both derived
  states — presence (`consult_missing`) and precedence (`consult_retroactive`, dated after the
  spec's `created:`) — a prose clarification per disposition 4; frontmatter untouched,
  `version: 1` stays.

**Why.** The addendum's exact gap, closed with the two fields both records already carry — no
new stored state, per the check's own "derived, never stored" posture (`consult.md:49`).

## F4 — `vlt-upgrade/SKILL.md`: the retrofit's signal re-cut + stamp beat

**Current state.** The proto-spec retrofit (`vlt-upgrade/SKILL.md:79`) scans for "spec-shaped
docs — revised in place, carrying "What changed" sections, or with ≥2 relay entries…" — the
same heading proxy, the defect's second site — and its accepted retrofit conforms frontmatter
"with **zero body changes**" and **no stamp beat**, which is how vlt-core got two live specs
under a `spec.md` still reading `adoption_first_instance: null` (A5-15 road 1).

**The change.**
- Re-cut the signal in step with F2: *"spec-shaped docs — revised in place (a **dated revision
  record**, per the `spec_candidate` signal in `vlt-lint` — a bare "What changed" topic heading
  is not one) or with ≥2 relay entries…"*.
- Add the stamp beat to the accepted-retrofit sentence: *on an accepted retrofit that produces
  the convention's **first live instance**, stamp `spec.md`'s `adoption_first_instance:` with a
  dated reference to the retrofitted spec (the authority rule, `vlt-mint`, Step 4 — set once;
  if the key already carries a date, leave it)* — the same run's post-flight report (`:105`)
  then reads the stamp it just wrote, closing the reporter loop in one upgrade.

**Why.** A5-9's "two sites, one defect" (the fix lands in both), and A5-15's road 1 gets its
writer at the moment the road runs.

## F5 — the stamp's authority rule and its landing (`vlt-mint`, `frontmatter.md`, `vlt-dispatch`, `vlt-lint`, `vlt-upgrade`)

**Current state.** `vlt-mint/SKILL.md:176`: "Nothing else may write this key; `vlt-lint` never
does." `frontmatter.md:242`: recorded "the moment that instance appears" (impossible off the
mint path under that topology), with *Live consumers today* naming only mint as writer.
`vlt-dispatch`'s consult block write (`:266-275`) has no stamp beat, so `consult.md` stayed
`null` through its first live exercise (A5-15 road 2). And the landing is locked out twice:
`vlt-lint:84` flags any base≠baseline as `convention_base_divergence`, and `vlt-upgrade` Step 1
(`:36`) records a stamped base as hand-edit divergence while Step 2 (`:48`) refreshes bases
wholesale — clobbering any stamp back to `null` (grounding addition 2).

**The change** (disposition 2).
- **`vlt-mint:176`** — the exclusivity sentence becomes the authority rule's single home:
  *"the stamp is written by **the ceremony that produces the first instance** — this mint
  beat, the spec promotion step (`{conventions}/spec.md`, *Promotion from candidate*),
  `vlt-upgrade`'s proto-spec retrofit, and `vlt-dispatch`'s consult record; `vlt-lint` never
  writes it."* Set-once semantics unchanged (dated key present → leave it).
- **`frontmatter.md:242`** — update the *Live consumers today* sentence to the same writer
  set, and soften "the moment that instance appears" to match reality ("by the ceremony that
  produces it"). Descriptive prose only; `frontmatter@4` does not bump (disposition 2).
- **`vlt-dispatch`, *Write the consult block*** (after `:273`'s block shape): *if this is the
  record's **first** `consult:` block (grep the record) and `{conventions}/consult.md` reads
  `adoption_first_instance: null`, stamp it with a dated reference to this consult (the
  authority rule, `vlt-mint`, Step 4 — set once).*
- **`vlt-lint:84`** (`convention_base_divergence`): the compare **excludes the
  `adoption_first_instance:` line** — an authorized vault-local stamp on a shipped base (the
  authority rule), never a hand-edit; every other difference still flags.
- **`vlt-upgrade:36`** (pre-flight compare): the same one-line exclusion. **`:48`** (apply):
  when refreshing a base convention, **carry the vault's stamped `adoption_first_instance:`
  value forward** into the refreshed base (merge-not-replace for this one key — a dated stamp
  is the vault's, `null` ships); state it beside the existing "base conventions are refreshed"
  sentence so the two rules read together.

**Why.** A5-15 in full: the axis's third value stops being permanently dishonest for non-mint
roads, the `frontmatter.md:242` inconsistency dissolves, and a stamp — from any authorized
writer — survives both the lint net and the upgrade it must outlive (the durability standing
rule).

**Out of scope at this site.** No overlay-based or agent-zone relocation of the axis — the key
stays where `frontmatter.md:237` declares it; the machinery learns the one authorized line
instead (smaller, and keeps the facet's single declared home).

## F6 — `vlt-upgrade/SKILL.md`: the adoption line carries the null's age

**Current state.** `convention_adoption` (`:105`, defined `:112`, ledger `:131`) reports three
values; a `declared, no first instance yet` renders identically at day 1 and day 180 — the
18-day-old null nobody read (A5-6 direction 2).

**The change.** In the `:112` definition (and the `:131` ledger comment to match): *an explicit
`null` reports **declared, no first instance yet (declared since `created:` — N days)**,
deriving the date from the convention file's own `created:` frontmatter* — so longevity is
visible at the only cadence that reports the axis. No gate, no threshold, no new key — a
long-lived null becomes readable, which is all the direction asked.

**Why.** Disposition 1, direction 2 — minimal, derive-first, at the existing reporter.

## F7 — the four-consumer re-ack (`spec@2`)

**Current state.** `spec.md` `consumers: [vlt-mint, vlt-dispatch, vlt-upgrade, vlt-lint]`
(`:12`); pins today: `vlt-mint/SKILL.md:3` (`spec@1`), `vlt-dispatch/SKILL.md:3` (`spec@1`),
`vlt-upgrade/SKILL.md:3` (`spec@1`), `vlt-lint/SKILL.md:4` (`spec@1`).

**The change.** With F1's `version: 2`, move all four pins `spec@1` → `spec@2` **in this
build**, each with a confirming read that the consumer's body points at the convention rather
than restating its mechanics (the promotion beat's mechanics live in `spec.md` only; F2 and F4
point). Bipartite consistency is verified by `package-lint` Group E — the check of record, not
a hand-written grep.

## Registration

No new skill, no new workflow — no `module-help.csv` row. **The consumer walk is real:** `spec`
bumps `1→2` (F1) and all four listed consumers re-ack in this build (F7); Group E is the net.
`consult@1` and `frontmatter@4` deliberately do **not** bump (dispositions 2 and 4 — prose
clarifications only, per the grouping ruling's one-bump sizing). No structure-map change. Not
the release build — no version-string bumps (they ride the arc's release build).

## Out of scope (dispositioned)

- **A5-9 direction 2 (git-log revision signal)** — rejected (disposition 3): the conventions do
  not require a git-managed vault, per the filing's own caveat; not load-bearing in a shipped
  check.
- **Retro-stamping vlt-core's existing instances** (`spec.md`'s two retrofitted specs,
  `consult.md`'s two consults) — vault-side act, not module source (disposition 2); the roads
  stamp going forward, and the field's standing instances stamp the next time a road runs.
- **The spec convention's two deferred lint checks** (`spec_schema_violation`,
  `spec_notification_missing`) — stay deferred with their tripwire, exactly as `spec.md:81`
  records; landing them is not any filing's ask.
- **Escalation of an aging candidate queue** — a tripwire concern (the enforcement kit), per
  `vlt-lint:63/:107`'s standing deferral; B5-9's territory, not this build's. The named owner
  bounds the obligation; the kit escalates it.
- **A5-9's `adoption_first_instance` secondary** — deduped to A5-15 at capture; discharged here
  by F5 (the consult-road writer), not separately.
- **A5-6's "zero-specs alarm" temptation** — the check still never alarms on the absence of
  specs (`vlt-lint:89`'s closing sentence preserved verbatim); the loop fix is acceptance, not
  advocacy pressure.
- **`vlt-lint` auto-promotion or partner routing** — "Never auto-promote… routing back to the
  owning partner is not lint's job" stands; lint *names* the owner in the backlog item, the
  owner acts in ordinary work (the beat lives in `spec.md`, F1).
- **A factory report-contract lint** (declared-key↔producer tracing, `package-lint.py`
  territory) — routed by ships-decides as ordinary arc work if taken up; not this build (the
  B5-3 disposition, unchanged; F2's report-key addition is the manual instance).

## Verification (unit, at rest)

1. **Group E** (`tools/package-lint.py` — E1 handshake-bipartite, E2 structure-map, E3
   stray-pin) passes with `spec` at `version: 2` and all four consumers at `@2`. Group E is the
   check of record for the re-ack; any `grep "spec@"` is an editing aid only, never the
   recorded verification.
2. **Packaging lint** — `uv run tools/package-lint.py` A/B/C/E PASS (D / `--expect-version` is
   the release gate, not this build's).
3. **Strict-YAML fence** — the `vlt-lint/SKILL.md` Step-5 fenced block still parses whole under
   `yaml.safe_load` with the two new keys (`spec_candidate:`, `consult_retroactive:`) — B5-3
   made whole-fence PASS the standing expectation; do not regress it (no second `: ` inside a
   flow-sequence placeholder).
4. **Two-site agreement grep** — `grep -n '"What changed"' skills/vlt-lint/SKILL.md
   skills/vlt-upgrade/SKILL.md` shows the heading surviving only inside the
   "not-revision-evidence" clauses (no site still *matches on* the heading); both sites name
   the dated-revision-record signal.
5. **Single-home greps** — the promotion beat's mechanics exist only in `spec.md` (*Promotion
   from candidate*), with `vlt-lint` and `vlt-upgrade` pointing; the stamp authority rule's
   writer list exists only at `vlt-mint` Step 4, with `frontmatter.md:242` descriptive and the
   three other writers pointing at "the authority rule, `vlt-mint`, Step 4"; the carry-forward
   rule exists only in `vlt-upgrade` Step 2.
6. **Dry-read coherence** — `vlt-lint` Steps 2→4→5: `spec_candidate` and `consult_retroactive`
   each trace check → backlog/flag → report key (the A5-3 class, checked by reading); the
   Step-4 spec-candidate item shape carries `by:` + closes-when; the decline guard reads the
   backlog record, never a stored counter.
7. **No-bump confirmation** — `consult.md` and `frontmatter.md` frontmatter byte-unchanged
   (`version:`/`consumers:` lines untouched); only their prose moved.
8. **Temp-fixture walk of the divergence exclusion** — copy a base convention + its `.baseline`
   to a temp dir, stamp `adoption_first_instance:` with a date in the copy, and confirm the
   compare rule as written (diff excluding that line) reports clean, while a second, genuine
   edit still reports divergence.
9. **Scrub** — no personal/vault-local content in any changed shipped file (vlt-core paths,
   partner names, and the filing's macro numbers stay out; worked examples use placeholder
   paths per the standing rule).
10. **No `.decision-log.md`** in the working tree at commit time.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** the spec loop reaches the field — on the next ordinary vlt-core
   upgrade, the installed `spec.md` is `version: 2` carrying the *Promotion from candidate*
   section and the deferral blind-spot statement, with all four installed consumers acking
   `spec@2`; the installed `vlt-lint/SKILL.md` carries the dated-revision-record signal (no
   heading match), the named-owner backlog shape, and the `spec_candidate:` +
   `consult_retroactive:` report keys; the installed `vlt-upgrade/SKILL.md` carries the
   re-cut retrofit signal, the retrofit stamp beat, the adoption-aware pre-flight compare +
   apply carry-forward, and the aged adoption line; the installed `vlt-mint` carries the
   authorized-writers rule and the installed `vlt-dispatch` the consult stamp beat.
   Grep-checkable on the installed vault; bounded — the upgrade happens anyway. (The same
   upgrade's own post-flight adoption line exercises F6 live: every `null` renders with its
   declared-since age.)
2. **[field-contingent]** the loop closes on real candidates — producing vault: **vlt-core**
   (factory-readable; the owner runs lint, and the filing's four relay-leg candidates plus its
   two retroactive consults are already standing, so the events are expected in ordinary use).
   On the first full `vlt-lint` after the upgrade: (a) no candidate is surfaced on a bare
   "What changed" heading (the seven Researcher→Librarian template docs stay unflagged; the
   relay-leg candidates still surface), each surfaced candidate carrying a **named owner** in
   its backlog item; (b) the two known retroactive consults report `consult_retroactive`, not
   silence; and (c) when the owner subsequently promotes or declines any one candidate, the
   loop terminates — a promotion lands the doc in `{specs}` and stamps `spec.md`'s
   `adoption_first_instance:` (surviving the *next* upgrade's refresh un-clobbered — the
   carry-forward's live proof), or a decline is recorded and the next lint honors it (no
   re-file, honored-decline count stated). Clause (c)'s promotion/decline is the owner's
   decision to make, not caused by the upgrade — if no candidate is ruled on before arc
   closeout, (c) stays open as this check's unbounded tail while (a)/(b) grade on the first
   lint.
