---
title: 'Build #B7-4 — the seam: vault-writable fields honored, local conventions received, dispatch given a routing profile (the mechanisms behind the rules the frontmatter bump shipped)'
status: 'BUILT 2026-08-15 — F1–F10 landed as briefed across 16 shipped files: both interim trailers retired (frontmatter.md version: 7 holds, prose only, no re-ack — all seven frontmatter@7 pins unmoved); the divergence nets generalized to the declared vault-writable member set with frontmatter.md:*Vault-writable declared fields* as the single home (checks.md base-divergence + vlt-upgrade pre-flight point, no list carried); three-way carry-forward + vault_writable_collisions and local_conventions_intact report keys + local-convention Step-1 snapshot/preserve/never-seed-baseline clauses in vlt-upgrade; the local-convention receiving surface (baseline_missing carve + inventory line + report key, coherence pin-exemption, vlt-mint third Edit-a-convention route, contract consumer-read bullet wired into the five JIT-read sites); the dispatch routing profile at _agent/dispatch-profile.md (roster + default principal + capture streams, (for: …) facet, relay key widened to (path|ref, to-slug, principal), guard 2 pair-equality per A8, absent-profile byte-identical, dispatch_profile_invalid lint check + report key). Verification: C6 red-then-green probe recorded (contract edited -> FAIL C "rule-card stale ef0210cba05f… != 12f03853c529…" -> sha re-derived -> PASS); package-lint --expect-version 0.9.1 exit 0, A/B/C/D/E all green; test-package-lint 21/21, CASE_FLOOR 21, tools/ diff empty (R2 not triggered); fixture desk-checks of record 19/19 green (scratchpad seam_desk_checks.py — divergence exclusion a1/a2, carry-forward table b1–b5 incl. adoption-stamp reproduction and undeclared-field refresh, local-convention truth table c1–c3b, profile cases d1–d8 incl. two-defaults refusal, unknown-principal stop, distinct pair keys, guard-2 pair-equality and its no-profile slug-equality reduction); single-home greps clean (member set enumerated only in frontmatter.md, nets carry pointer language, facet defined in vlt-dispatch SKILL.md and used not redefined in the mode refs, guard-2 pair language in relay.md only); scrub clean (placeholder slugs/paths only). Deviations: (1) the contract carve-out bullet''s dangling "routes per the next bullet" reference re-pointed to "the base-rule-change bullet below" — the new local-convention bullet inserted after it would otherwise capture the reference; two-word clarification, no rule change. (2) the contract''s Edit-a-convention routing summary sentence gained "; local convention for a vault-originated new subject" so it agrees with F6''s third route — F4-adjacent, same section. (3) F1''s local-conventions replacement keeps one retained sentence — "Disguising a rule inside an unrelated overlay remains illegal (the silent third zone this rule exists to close)" — because F2''s out-of-scope disposition leans on F1 naming disguise illegal and the brief''s replacement text had dropped it. (4) contract last_updated bumped 2026-07-26 -> 2026-08-15 (substantive edit, the file''s own rule). ⚠ OWNER-REVIEW FLAG (undischarged): this brief re-derives A7-4''s decision space without the vault-side decision matrix (disposition 1) and rules two questions the roadmap reserved for the owner (dispositions 6/7 and 8) — review the dispositions at or before the v0.10.0 release.'
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-08-123610-dispatch-hardcodes-single-user-addressee-model.md (A7-4 — the design gap: dispatch welds vault-population policy into module-owned mechanism; the routing-profile mechanism half)'
  - 'inbox/2026-08-14-142624-stock-deferral-dates-expire-with-no-vault-side-review-form.md (A7-5 — the mechanism half: the divergence diff honors declared vault-writable base fields; B7-3 shipped the rule)'
  - 'inbox/2026-08-14-154423-no-legal-home-for-a-vault-originated-new-convention.md (A7-8 — the mechanism half: the baseline_missing exemption and the consumer read; B7-3 shipped the two-property rule)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: >
  roadmap §Ideation rulings (2026-08-15): the framing SPLIT (one designed seam over A7-5+A7-8+A7-4);
  the authorized-carry precedent GENERALIZES (a declared vault-writable field is not base divergence);
  THE VETO STANDS (no generic skill-overlay mechanism — A7-4''s answer is a designed parameter read on
  the vlt-track pattern); the dedicated frontmatter@6 build (B7-3) ships rules, mechanisms cite them;
  B7-4 owns A7-4''s five open questions (a)–(e). Post-ideation amendments A1/A6 (the frontmatter reopen
  condition — weighed here, NOT invoked, disposition 7) and A8 (guard 2 widens to pair-equality in the
  build that widens the addressee model — this build).
risk: >
  moderate — three mechanisms across eight files including the operating contract (C6 rule-card sha
  re-derive owed) and two durability nets (lint divergence check + upgrade carry-forward); NO convention
  version bump (frontmatter stays @7 — disposition 7 declines the A1 reopen), so no consumer walk and no
  re-ack; no release-gate check changes (R2 not triggered, CASE_FLOOR stays 21).
---

# Build #B7-4 — the seam

## Intent

Arc 7's framing ruling split the six no-landing-zone filings: A7-5, A7-8 and A7-4 are one class —
**a vault holding legitimate content (a performed review, a novel convention subject, a population
policy) with no sanctioned place to put it** — and they get one designed seam, not three ad-hoc
fixes. B7-3 shipped the *rules* into `frontmatter@6` (now @7 after B7-6): the vault-writable-field
declaration (`frontmatter.md:247`), the local-convention two-property rule (`frontmatter.md:253`).
Both ship today with R1 interim postures that name this build as the mechanism: *"until the
mechanism that honors the declaration ships (the seam build's divergence-diff generalization)"* and
*"until the seam build ships the mechanism (the `baseline_missing` exemption and the consumer
read)."* This build is the seam build. It ships three mechanisms:

1. **The divergence diff honors declared vault-writable base fields** (A7-5's mechanism) — the
   lint-time half (`vlt-lint/references/checks.md:41`) and the upgrade-time half (`vlt-upgrade/SKILL.md:36`
   pre-flight, `:48` carry-forward) stop hard-coding `adoption_first_instance:` and instead honor the
   member set the governing convention itself declares, per the enumeration-vs-structure doctrine.
2. **Vault-originated local conventions are received** (A7-8's mechanism) — a sanctioned (minted)
   local convention stops flagging `baseline_missing`, survives upgrades explicitly, is visible to
   the split tripwire, and is read by consumers the way overlays are.
3. **`vlt-dispatch` gets a designed routing-profile read** (A7-4) — on the shipped `vlt-track`
   pattern (`vlt-track/SKILL.md:16, 31-40`, headless fallback `:40`): a vault-local profile declares
   the human-principal roster and per-principal capture streams; `daily`/`relay`/`ledger` consult it
   on entry; **absent profile ⇒ byte-identical current behavior**. The veto stands: this is a
   parameter read, not a skill-overlay mechanism.

All rejected alternatives in the parent filings are settled — **do not re-litigate**. In
particular: no generic skill-overlay/extension mechanism, no `customize.toml` on op skills, no
dispatch-v2 rewrite, no permanent-workaround posture (A7-4's own pre-rejections, upheld by the
ideation veto ruling); no per-partner inbox queues (rejected in dispatch's own design,
`vlt-dispatch/SKILL.md:22`); no suppression of the interim-window findings (B7-3's postures said
they were correct, and they were).

## Brief-time dispositions

> **⚠ The whole of disposition 1's reconstruction, and the reserved-question rulings in
> dispositions 6 and 7, are flagged for owner review at the v0.10.0 release.** They are grounded
> and conservative, but two of them decide things the roadmap earmarked for the owner.

1. **A7-4's vault-side decision matrix is unrecoverable on disk; the decision space is re-derived
   here from the filing and the shipped precedent (owner-directed).** The roadmap pinned an owner
   action to this brief: supply `_output/problem-solution-2026-08-08.md` from vlt-core. **The file
   does not exist anywhere in `{field-vault}`**: there is no `_output/`
   directory; no problem-solution artifact dated 2026-08-08 exists under `_agent/artifacts/` or
   elsewhere; the closest-dated artifacts are unrelated. (The filing itself says the artifact was a
   *factory* problem-solving session's output filed from a **team-vault install, not vlt-core** —
   the roadmap's pin pointed at a vault that never held it.) The owner has directed this build
   cycle to complete without further input. Ruling: the matrix is treated as lost; the decision
   space is re-derived from (a) the filing's own summary — which is unusually complete: it records
   the losing shapes *and why they lost* ("the matrix's losing shapes lost on invariants —
   text/behavior overrides of module skills are the silent-fork pattern the SHA manifest and
   single-home discipline exist to refuse", filing `:48-50`) — and (b) the shipped precedent the
   capture names as exact (`vlt-track`'s designed-parameter read). Dispositions 2–6 below are that
   re-derivation. If the owner later recovers the matrix and it contradicts a ruling here, that is
   a filing, not a silent re-cut.

2. **(a) Profile home: a single vault-wide file at `_agent/dispatch-profile.md` — the routing
   record's sibling.** Alternatives weighed: **(i)** `{overlays}`-adjacent
   (`_agent/conventions/…`) — rejected: that directory is convention overlays + `.baseline/`; a
   profile is not a convention and is not append-only, and a stray `*.overlay.md`-shaped file
   there would sit one naming slip away from `overlay_orphan` (`checks.md:42`); **(ii)** a
   per-partner capability file (`{partners}/<p>/capabilities/dispatch.md`, the literal vlt-track
   form) — rejected with (b) below; **(iii)** extending `vault_structure` — rejected: the map
   carries paths, not policy, and a roster is policy. The record's sibling wins on ownership and
   durability: dispatch already creates and owns `_agent/dispatch.md` in the agent zone
   (`vlt-dispatch/SKILL.md:40`); the agent zone is never written by upgrades (contract, *Durability
   across upgrades*), so the profile is upgrade-durable **by construction** — merge-not-replace is
   satisfied by the module never shipping or touching the file at all. The module ships no profile
   and no template file; the profile's shape is documented in `vlt-dispatch` (F7) with
   placeholder-path examples.

3. **(b) One vault-wide profile, not per-partner files — a justified deviation from the vlt-track
   precedent's *location*, not its *pattern*.** vlt-track's profile is per-partner because the
   parameterization (roots, streams, gates) genuinely varies per calling partner. Dispatch's
   addressee model cannot vary per partner: all four modes are "the same machine" writing "the
   identical record" (`SKILL.md:18`), the drain is source-agnostic, and the idempotency key is
   shared state — if the Researcher's profile and the Librarian's profile disagreed about who
   `alex` is or whether `alex` exists, the bus would fork (dedup breaks, addresses become
   reader-relative). A roster is a fact about the **vault's population**, not about a partner's
   practice. One profile, read identically by every mode regardless of the invoking partner.

4. **(c) v1 parameter scope — roster, default principal, per-principal capture streams, and the
   principal facet on addressing; nothing more.** The v1 profile declares exactly: **(i)** the
   **principal roster** — one line per human: routing slug + display name; **(ii)** the **default
   principal** — the one un-annotated traffic belongs to (a single-entry roster is its own
   default); **(iii)** optionally per principal, a **capture stream** — the daily-notes location
   `daily` mode scans for that principal (default principal's default: `daily/`, i.e. today's
   behavior). Addressing widens with one facet: a pointer line may carry `(for: <principal-slug>)`
   and relay accepts an optional `to-principal`; the relay idempotency key becomes
   `(handoff-path | ref, to-slug, principal)`; guard 2 widens to pair-equality (A8). **Ruled out
   of v1**, each with its reason in §Out of scope: per-principal record files (contradicts the
   record-not-inbox design), per-principal permissions/visibility, notification machinery,
   consult-mode principal awareness, principal fields on backlog items or session logs. The
   filing's "more?" is answered **no**: v1 is the smallest set that makes the team vault's actual
   ask ("the same thing to more destinations") expressible, and every candidate addition either
   contradicts a shipped design ruling or has no second consumer yet.

5. **(d) No convention vocabulary in v1.** The filing leaned toward homing rule-like vocabulary
   (addressee facets on the record) in a convention "so the existing overlay seam covers it."
   Ruled: not yet. The dispatch record's line format has exactly one owner today — the dispatch
   skill and its mode references (single home; the record carries no per-note frontmatter,
   `daily.md:61`) — and the one facet it borrows (`blocked:`) is owned by `frontmatter.md` only
   because it is the *backlog's* schema, which that convention owns. The `(for: …)` facet has one
   writer and one reader, both dispatch. Moving its definition into `frontmatter.md` today would
   be a rule change on a seven-consumer convention (a bump + walk under A1/A6) to give one skill's
   private format a second home — the exact churn single-home exists to prevent. **The revisit
   trigger, stated so this is a decision and not a drift:** the day a second surface consumes the
   principal vocabulary (a `principal:` key on session logs, a backlog facet, a lint check that
   parses it), it has become schema and belongs in `frontmatter.md` via the then-current bump
   path. Until then the profile and facet are skill-parameter territory, exactly like vlt-track's
   loop-profile keys (which also live outside the conventions).

6. **(e) State the generalized designed-read pattern in the contract now — and record the veto's
   reasoning with it.** The wait-for-a-second-instance option is moot: this build *is* the second
   instance (vlt-track's loop profile is the first), and the arc's own logic — "a second instance
   of a one-off is a category" (the ruled-by-consequence generalization) — applies. The clerk's
   recommendation (roadmap, veto ruling — explicitly *not* a ruling; the owner was to rule it at
   this brief) is **adopted as this disposition**: the contract records not just the veto but its
   reasoning, so the next dispatch-shaped filing does not re-propose the shape a fourth time.
   ⚠ Owner-review flag: this decides a question reserved for the owner; the text lands in F4 and
   is cheap to soften or cut at review.

7. **The A1 frontmatter reopen is NOT invoked — the vault-writable member set is a governed class
   declaration in `frontmatter.md`'s prose, not a new per-file frontmatter field.** ⚠ Owner-review
   flag: A1 anticipated this build might prove the field ("a declaration the base file carries
   about itself… is a new convention-frontmatter field B7-4 may need"), and B7-3 left a clean seam
   for a 7→8 reopen. Weighed:
   - **Per-file `vault_writable:` key (the reopen path).** For: literal reading of "a declaration
     the base file carries about itself"; per-file extensibility. Against: **all three shipped
     conventions would declare the identical two-member list** — a constant wearing a variable's
     clothes (the class is defined class-wide: `adoption_first_instance:` and `review_after:` are
     vault-writable on *every* convention, `frontmatter.md:247`); it opens a **self-authorization
     surface** (a vault edits the key to launder a base edit — closable only by a further rule
     that the key itself is never vault-writable); and it costs a 7→8 bump with a full
     seven-consumer walk to ship an unconsumed-variance schema.
   - **The governed-class declaration (taken).** The member set already has exactly one home:
     `frontmatter.md:247` (*Vault-writable declared fields*), shipped and re-acked at @7. The two
     nets (F2, F3) stop naming any field and **point at that section for the member set** — the
     enumeration moves out of the nets and into the governed declaration, which is what the
     doctrine's own words ask for ("reading a declaration the protected thing carries about
     itself" — the protected corpus's governing convention carries it). **The doctrine's required
     growth-check exists mechanically:** changing the member set is a `frontmatter` rule change,
     which bumps `version:` and walks all seven consumers — the handshake *is* the shrink/growth
     check, in exactly the A6 sense (a mechanical, checkable state, not a prose promise). The need
     for a base *field* is therefore **not proven**, the base carries no new schema, and
     `frontmatter` stays @7 with no consumer walk. The reopen stays available to any later build
     that proves a genuinely per-file variance.

8. **The local-convention sanctioning test is the mint record, not a new frontmatter key.** How
   does lint tell a sanctioned local convention from a shipped base whose baseline was lost, or
   from a drive-by unminted file? Weighed: **(i)** an `origin:`/provenance frontmatter key —
   rejected: it is another 7→8-bump schema addition (disposition 7's economics), and it is
   self-asserted (any file can claim it); **(ii)** "carries full convention meta ⇒ local" —
   rejected: every shipped base also carries full meta, so a lost baseline would silently
   reclassify a stock file as local and hand-editable; **(iii — taken)** **a live, `ref:`-keyed
   convention-mint entry in `_agent/mint/decision-log.md`**. The rule's own vocabulary is "new
   conventions **minted**" (`frontmatter.md:16, :253`), the mint ceremony is council-gated and
   already writes the ref-keyed entry, and lint's read-before-flag machinery already reads the log
   for exactly these findings (`checks.md:39`). This derives a state from **the record of the
   sanctioning event** — the posture `checks.md:47` explicitly blesses ("written *by* the
   consult, an event… derives from a record and not from the residue of the process being
   checked") — not from the residue of the thing checked. Consequence, stated as a feature: an
   **unminted** file in `{conventions}` keeps flagging `baseline_missing` — the landing zone is
   legal *when sanctioned*, which is the enforcement half of A7-8's bar ("a landing zone that is
   merely silent would reproduce today's outcome with better manners"). A pre-schema mint entry
   that cannot be keyed keeps flagging until the decision-log reconcile pass
   (`vlt-upgrade/SKILL.md:77`) surfaces it for a one-time ruling — noted, not special-cased.

9. **Carry-forward semantics for vault-writable fields: three-way against the old baseline; the
   vault's value wins; a both-moved collision is surfaced, never silently picked.** The shipped
   one-field rule ("a dated stamp is the vault's, `null` ships", `vlt-upgrade/SKILL.md:48`) does
   not generalize as written — `review_after:` ships a *real* value, so "non-null wins" is
   meaningless. General rule: on base refresh, for each declared vault-writable field, compare the
   live base's value to the **old baseline's** value. Equal ⇒ the vault never wrote it ⇒ the
   incoming shipped value lands (the module can re-derive dates). Different ⇒ the vault legally
   wrote it ⇒ **carry the vault's value into the refreshed base**; and if the incoming shipped
   value *also* differs from the old baseline (both sides moved), keep the vault's value **and
   surface the collision** in the post-flight report (F3) — the honest-reporting posture, not a
   silent merge. `adoption_first_instance:` under this rule behaves exactly as it does today
   (baseline ships `null`; a stamp differs; carried).

10. **Profile absence defaults silently; profile malformation refuses loudly.** A deviation from
    vlt-track's headless fallback ("ask for the missing pieces — never guess", `:40`), justified:
    track has **no** legal default (a guessed `{root}` writes to a wrong place); dispatch has a
    complete one — the single-principal model, which is every existing vault. So: absent file ⇒
    byte-identical current behavior, no question asked (the filing's own requirement). Present but
    malformed, or an addressed act naming a slug not in the roster ⇒ **say so and stop the
    addressed act** — never guess a roster (that would misdeliver another human's traffic), never
    silently fall back to single-principal while a roster exists. The never-guess half of the
    track precedent survives; only the absent case diverges, because only there does a legal
    default exist.

## F-sites

### F1 — `frontmatter.md`: the two interim trailers retire (no bump)

`skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md` — **prose clarification
only; `version: 7` holds, no re-ack** (the B7-5 precedent: interim trailer replaced with no
rule-text change, roadmap ledger B7-5 check 3). The rules themselves are untouched.

- **Current (`:247`, *Vault-writable declared fields*):** the rule + this R1 interim posture:
  *"until the mechanism that honors the declaration ships (the seam build's divergence-diff
  generalization), a shipped deferral's expiry is reviewed upstream, and a vault's only legal move
  is to file…"*
- **Change:** replace the interim-posture sentence (everything from *"Interim posture:"* to the
  end of the paragraph) with the live-mechanism statement, keeping the rule sentences before it
  verbatim: *"The mechanism is live: the divergence surfaces (`vlt-lint`'s base-divergence check
  and `vlt-upgrade`'s pre-flight) exclude the declared fields, and the upgrade's base refresh
  carries a locally-written value forward (both-moved collisions are surfaced, never silently
  merged — see `vlt-upgrade`). **This section is the member set's single home** — today
  `adoption_first_instance:` and `review_after:` — and the consuming nets point here rather than
  carrying their own list. Declaring a further field vault-writable is a base rule change: it
  bumps this file's `version:` and walks every consumer."* (That last sentence is a *statement of
  the existing base-edit ceremony applied to this section*, not a new rule — the ceremony at
  `vlt-mint/SKILL.md:147-150` already binds any rule change here.)
- **Current (`:253`, *Local conventions (vault-originated)*):** the two-property rule + the R1
  interim posture: *"until the seam build ships the mechanism (the `baseline_missing` exemption
  and the consumer read), a vault-originated convention file in `{conventions}` still flags
  `baseline_missing`…"*
- **Change:** replace the interim-posture sentence with: *"The mechanism is live: a local
  convention is **sanctioned by its mint** — a live, `ref:`-keyed convention-mint entry in
  `_agent/mint/decision-log.md` (`vlt-mint`, *Edit a convention*) — and a sanctioned local
  convention is not a `baseline_missing` finding (`vlt-lint` reports it on the local-conventions
  inventory line instead); it survives upgrades untouched (`vlt-upgrade` preserves it explicitly),
  counts toward this file's `deferral_metric` by construction (it is a `{conventions}` file beyond
  the shipped baseline count), and is read by every consumer it names in its own `consumers:` (the
  operating contract, *Durability across upgrades*). An **unminted** file in `{conventions}` still
  flags `baseline_missing` — the landing zone is legal when sanctioned, not merely occupied."*
- **Why:** Strand 3's own rule — shipped prose must not keep asserting an interim that ended; both
  postures name the seam build and the seam build is shipping.
- **Out of scope at this site:** any rule change (both rules ship as B7-3 wrote them); the schema
  block; `deferral_threshold:` (self-baselined by B7-3 — the local-convention count rides it
  unchanged).

### F2 — `vlt-lint/references/checks.md`: the divergence net reads the declaration; the receiving surface reports honestly

- **Current (`:41`, convention base divergence):** *"compare the two, **excluding the
  `adoption_first_instance:` line** — an authorized vault-local stamp on a shipped base (the
  authority rule, `vlt-mint`, Step 4), never a hand-edit; every other difference still flags"* —
  and, same bullet: *"If no baseline exists for a base file, **flag** it once as
  `baseline_missing`."*
- **Change (exclusion generalized — pointer, no second enumeration):** *"…comparing the two,
  **excluding the lines of fields declared vault-writable** (`{conventions}/frontmatter.md`,
  *Vault-writable declared fields* — the member set's single home; read it there, never carry a
  list here); a declared field's local value is an authorized vault-local carry
  (`adoption_first_instance:` via the authority rule, `vlt-mint` Step 4; `review_after:` via a
  performed deferral review), never a hand-edit; every other difference still flags."*
- **Change (`baseline_missing` carve — the receiving surface):** the no-baseline sentence becomes:
  *"If no baseline exists for a base file, first apply the local-convention test: a file whose
  `{name}` has a live, `ref:`-keyed convention-mint entry in `_agent/mint/decision-log.md` (the
  read-before-flag read above — same log, same liveness rule) is a **sanctioned local convention**
  (`{conventions}/frontmatter.md`, *Local conventions*), **not a finding**: report it on the
  report's local-conventions inventory line (a denominated line — 'N local convention(s):
  <names>'; zero renders as the denominated zero), where it is visible as a convention in its own
  right (the split-tripwire property). A no-baseline file with **no** live mint entry flags
  `baseline_missing` exactly as today — that covers both a lost baseline and an unminted drive-by
  file, and the legal response for the latter is to mint it or remove it (`frontmatter.md`, *Local
  conventions*)."*
- **Change (`:36`, convention coherence — the local-convention clause):** the coherence check
  walks `consumers:` → `depends_on:` pins. A local convention's `consumers:` names module skills
  that **cannot** pin it (module-owned `depends_on:` lists are shipped text; a vault-local pin
  would be clobbered on refresh — and is exactly the local-skill-edit the veto refuses). Append to
  the check: *"A **sanctioned local convention** (no baseline + live mint entry — the
  base-divergence bullet's test) is exempt from the pin half: its `consumers:` is a **discovery
  roster** (who must read it — the operating contract's local-convention read), not a handshake;
  flag nothing for a missing `depends_on` ack against it. The version handshake binds shipped
  conventions only. Its `version:`/`consumers:` presence is still required
  (`convention_meta_missing` applies to every `{conventions}` file, local ones included)."*
  Without this clause the first sanctioned local convention ships a guaranteed false positive
  (`unacknowledged`) on day one — the A5 lesson (two shipped properties in conflict, caught at
  brief time, not acceptance).
- **Change (new governance check — the dispatch routing profile):** add one compact governance
  check (both modes), after the capability checks: *"**Dispatch routing profile** — if
  `_agent/dispatch-profile.md` exists, validate it: every roster line carries a backtick slug +
  display name; slugs unique; exactly one `(default)` (or a single-entry roster); every declared
  capture stream resolves to an existing directory. Flag `dispatch_profile_invalid`
  (`flag_for_human`) with the failing line. **Legal response, stated at the check (R3 posture):
  fix the profile — it is vault-owned and freely editable; `vlt-dispatch` refuses addressed acts
  against a malformed profile rather than guessing, so this finding mirrors a runtime refusal.**
  Absent file ⇒ no findings (the single-principal default, not a gap)."* This is the filing's
  explicit ask ("malformed profile loud not silent, dangling destinations reported") and ships no
  finding class without a stated response.
- **Why:** the enumeration-vs-structure doctrine applied to the divergence net (the flagged
  candidate instance in the roadmap's authorized-carry ruling); A7-8's grounded table
  (`baseline_missing` / `overlay_orphan` / silence) closed at its non-silent corner; A7-4's lint
  coverage.
- **Out of scope at this site:** `overlay_not_append_only`'s verbatim-heading weakness (the silent
  third zone) — **deliberately not strengthened here**: F1's retired posture already names
  disguise-in-an-unrelated-overlay illegal, the legal landing zone this build opens removes the
  motive, and a prose-drift check is not this arc's scope (B7-3 F1g's same disposition). Report
  Step-5 key plumbing for the inventory line is the builder's (mirror the existing denominated
  lines).

### F3 — `vlt-upgrade/SKILL.md`: the upgrade-time half — exclusion, carry-forward, and local-convention preservation

- **Current (`:36`, pre-flight base-divergence):** *"compare to its stock baseline …, **excluding
  the `adoption_first_instance:` line** (an authorized vault-local stamp on a shipped base — the
  authority rule, `vlt-mint`, Step 4 — never a hand-edit; every other difference still counts)"* —
  and *"If a baseline is missing, record `baseline_missing` (can't classify — seed it from the
  incoming source this run, best-effort)."*
- **Change:** generalize the exclusion identically to F2 (pointer at `frontmatter.md`, *Vault-writable
  declared fields*; no list carried here). And the missing-baseline sentence gains the same test:
  *"If a baseline is missing, apply the local-convention test (a live convention-mint entry in
  `_agent/mint/decision-log.md` — same test as `vlt-lint`'s): a sanctioned **local convention** is
  recorded as such (it has no baseline by design and is never refreshed); otherwise record
  `baseline_missing` (can't classify — seed it from the incoming source this run, best-effort;
  note a stock-named seed will make an unminted same-named local file show as divergence next run,
  which is the honest outcome)."* Add one Step-1 snapshot bullet after *Convention overlays*:
  *"**Local conventions** — every `{conventions}/*.md` with no stock counterpart in the incoming
  bundle and a live convention-mint entry (vault-originated conventions, durable — must never be
  lost; `{conventions}/frontmatter.md`, *Local conventions*). Record path + mint ref."*
- **Current (`:48`, own-the-apply):** *"when refreshing a base convention, **carry the vault's
  stamped `adoption_first_instance:` value forward** into the refreshed base (merge-not-replace
  for this one key — a dated stamp is the vault's, `null` ships; the authority rule, `vlt-mint`,
  Step 4)"*.
- **Change (carry generalized — disposition 9):** *"when refreshing a base convention, **carry
  forward the vault's locally-written value of every declared vault-writable field**
  (`{conventions}/frontmatter.md`, *Vault-writable declared fields* — the member set lives there):
  a declared field whose live-base value differs from the **old** baseline's was legally written
  by the vault — keep the vault's value in the refreshed base; a field equal to the old baseline
  takes the incoming shipped value. Where the vault wrote it **and** the incoming shipped value
  also changed, keep the vault's value and surface the collision in the post-flight report
  (`vault_writable_collisions`) — never silently pick. (`adoption_first_instance:` behaves exactly
  as before under this rule: `null` ships, a stamp differs, the stamp is carried.)"* Same
  sentence-cluster: add *"**Never overwrite or delete a sanctioned local convention** recorded in
  Step 1 — it has no shipped counterpart, so the merge-copy has nothing to refresh it with; its
  durability is location + this preserve clause (merge-not-replace)."*
- **Change (Step 3.3):** append: *"Baselines exist for shipped bases only — never seed a baseline
  for a sanctioned local convention (it is baseline-exempt by design)."*
- **Change (Step 4 report + Step 5 ledger + Verify):** the report YAML gains two always-present
  keys (never omitted when empty, per the honest-reporting rule): `local_conventions_intact:
  [<name> (mint <ref>), ...]` and `vault_writable_collisions: [<convention>: <field> — vault value
  kept, shipped value also changed, ...]`. The Step-5 ledger template's `Notes:` line guidance
  names both when non-empty (no new mandatory ledger line — template churn kept to the report,
  where the never-omit machinery already lives). Verify's checklist adds: every Step-1 local
  convention still exists post-apply.
- **Why:** the durability posture (anything a vault grows locally survives upgrades —
  merge-not-replace); without the carry, the first upgrade after a vault legally records a review
  would clobber the recorded outcome — the mechanism un-shipping its own rule; without the
  preserve clause, a local convention's survival is an accident of the copy implementation rather
  than a stated invariant.
- **Out of scope at this site:** the bracket path's local-convention handling beyond Step 1's
  snapshot + Step 3's existing restore posture (the snapshot is the restore source; nothing
  bespoke needed); `vlt-upgrade`'s `depends_on:` — it **points** at `frontmatter.md` for the
  member set and recites no rule mechanics, so it is not a consumer and owes no ack
  (`checks.md:36`'s own recites-vs-points test).

### F4 — the operating contract: the local-convention read rule + the designed-parameter-read pattern (C6 owed)

`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`, §*Durability across
upgrades* (`:88-105`).

- **Current:** the overlay bullet list `:97-105`; the merged-on-read invariant at `:100`; no
  statement anywhere of how a module skill takes vault-local *parameters*, and no home for the
  veto's reasoning (the veto lives as one clause at `vlt-upgrade/SKILL.md:48`).
- **Change 1 (the consumer read — A7-8's second mechanism half):** append one bullet to the
  overlay list after `:101`: *"**A sanctioned local convention is read the same way.** A
  vault-originated convention (`{conventions}/frontmatter.md`, *Local conventions*) is a
  convention in its own right: a consumer JIT-reading its governing conventions **also honors any
  local convention that names it in its `consumers:`** — discovery is by the local file's own
  consumer roster (scan `{conventions}` for it), never by an enumeration inside the skill. Local
  conventions are vault-local: they carry `version:`/`consumers:` for meta-completeness and
  discovery, but they are **outside the version handshake** (no `depends_on:` pin exists or is
  owed — the handshake binds shipped conventions only)."*
- **Change 2 (the pattern + the veto's reasoning — disposition 6):** append a short subsection at
  the end of §Durability: *"**Designed parameter reads — how a module skill takes vault-local
  policy.** A module-owned skill that needs per-vault variation consumes it as a **designed
  parameter read**: a vault-declared object in a declared home — `vlt-track`'s loop profile
  (`capabilities/track.md`), `vlt-dispatch`'s routing profile (`_agent/dispatch-profile.md`) —
  with a named fallback when absent. The declaration lives where upgrades never write, so it is
  durable by construction; the skill hardcodes none of it. **The boundary, and why it is a veto:**
  skill *text and behavior* are never locally patchable — skills have no overlay mechanism, a
  local skill edit is a `skill_asset_divergence` the user re-applies every upgrade (a treadmill,
  not a home), and a text override is the silent-fork pattern the SHA manifest and single-home
  discipline exist to refuse. The standing answer to 'can I overlay skill X?': **parameters yes**
  (a designed read, filed upstream if the skill lacks one), **content yes** (conventions,
  overlays, local conventions), **new behavior by mint** (a vault-grown op skill or capability),
  **skill text no**."*
- **C6 (mandatory):** the contract changed, so re-derive `vault-rule-card.md`'s `derived_from:`
  sha256 per the release contract (`tools/package-lint.py` group C6 is the gate that catches a
  stale one). The rule-card's *content* is unchanged — neither addition is an identity-bearing or
  act-blocking rule (the veto's act-blocking half, "partners write only to `_agent/` and `_meta/`",
  already stands); sha only. Builder verifies C6 green after the edit.
- **Why:** the read rule is the mechanism half F1's retired posture promises; the pattern
  statement is disposition 6 (second instance ⇒ category), homed once so five skills and the next
  filing can point at it.
- **Out of scope at this site:** Beat 2 (`:170`) — the profile is not an orient read (dispatch
  reads it on invocation, partners never do); the hand-off payload; any rule-card content change.

### F5 — the five JIT-read pointer clauses (the consumer read, wired)

Each of the five convention-JIT-read sentences gains one short pointer clause — pointers, not
restated mechanics (the contract owns the rule, F4):

- `skills/vlt-ingest/SKILL.md:26`, `skills/vlt-extract/SKILL.md:21`,
  `skills/vlt-research/SKILL.md:88`, `skills/vlt-lint/SKILL.md:17`,
  `skills/vlt-track/SKILL.md:42` — after each *"read each together with its
  `{overlays}/{name}.overlay.md` if present, honoring the overlay's appended rules"*, append:
  *"— and any **local convention** naming this skill in its `consumers:` (the operating contract,
  *Durability across upgrades*)"* (adapted to each sentence's grammar; `vlt-research:88`'s clause
  attaches to its write-verification read the same way).
- **Why:** without the clause, each skill's own text enumerates its reads and a local convention
  is never discovered — the read rule would be contract prose with no operating consumer.
- **Out of scope:** `vlt-dispatch` (writes a frontmatter-less record — no convention-governed
  write to widen); partner SKILL.mds and the mint partner template (partners write session
  notes/memory via the contract's point-of-use reads — the contract sentence covers them; adding
  five more pointer sites is enumeration creep with no write-path gain); the three workflow assets
  (a workflow with no convention read satisfies the contract at the point it would read one —
  B7-6's ruled latitude, verbatim; when one acquires a convention read, the merged read it owes
  includes local conventions by the contract's definition).

### F6 — `vlt-mint/SKILL.md`: the third convention route — minting a local convention

- **Current (`:138-141`, *Edit a convention*):** two routes — vault-local **addition** → overlay
  (`:140`); generic **rule change** → base + handshake (`:141`). A vault-originated **new
  convention** is neither: `:143` already says *"a **new** convention … must carry valid
  enforcement frontmatter"*, but no route names where a new local one lands or what sanctions it.
- **Change:** add a third bullet between `:140` and `:141`: *"**Vault-originated new subject →
  mint a local convention.** If the change is a **new rule subject with no stock counterpart**
  (not an addition to an existing convention's subject, not a change to a shipped rule), mint a
  **local convention**: a new file in `{conventions}` carrying full convention meta
  (`version: 1`, `consumers:` naming its readers, a valid enforcement declaration) per
  `{conventions}/frontmatter.md`, *Local conventions*. Council-gated like every convention change
  (Step 2). **The decision-log entry is the sanctioning record**: record the mint with `ref:`
  keyed to the convention file — `vlt-lint` and `vlt-upgrade` recognize a local convention by that
  live entry (no baseline exists or is ever seeded for it; `baseline_missing` does not apply to a
  sanctioned one). Its `consumers:` is a discovery roster, not a handshake — module skills honor
  it via the contract's local-convention read and never pin it in `depends_on:`. No help-registry
  row (a convention edit registers nothing, Step 4). It counts toward `frontmatter.md`'s split
  tripwire as a minted convention — that visibility is the point, not a side effect."*
- **Why:** disposition 8 — the sanctioning test keys on the mint record, so the ceremony must say
  it writes one for this kind (it already writes decision-log entries for every convention edit,
  `:150`; this names the kind and the `ref:` so the entry is mechanically keyable); without this
  route the only path to a sanctioned local convention is knowing the lint test by heart.
- **Out of scope at this site:** the mint classifier/kind taxonomy elsewhere in the skill (the
  Edit-a-convention umbrella covers it); template assets; the council-fallback machinery (B7-7,
  already shipped — this kind inherits it as any gated kind does).

### F7 — `vlt-dispatch/SKILL.md`: the routing-profile read (the designed parameter read itself)

- **Current:** `:30-44` — the resolved logical names + the four prose-fixed locations; no roster,
  the addressee model implicit (one human, partners by slug). `:22` — the why-a-record paragraph
  with the idempotency-key gist. `:54` — mode-dispatch argument forms.
- **Change (On Activation — the read, after the four-locations list `:39-43`):** add: *"**The
  routing profile (the designed parameter read).** Read `_agent/dispatch-profile.md` if it exists
  — the vault-wide declaration of the **human-principal roster** (this operation's own agent-zone
  artifact, vault-authored; the operating contract, *Designed parameter reads*). It declares: one
  line per principal (backtick **slug** + display name), exactly one `(default)` (a single-entry
  roster is its own default), and optionally per principal a **capture stream** (the daily-notes
  location `daily` scans for them; the default principal's default stream is `daily/`). **Absent
  ⇒ the single-principal model — byte-identical behavior, ask nothing.** Present but malformed,
  or an addressed act naming an unknown principal ⇒ say so and stop the addressed act — never
  guess a roster (`vlt-lint`'s `dispatch_profile_invalid` is the lint-time bell). The skill
  hardcodes no roster; the profile is upgrade-durable by location (agent zone, never shipped,
  never refreshed). Profile shape example (placeholder paths):"* — with a fenced example:

  ```
  ## Roster
  - `{principal-slug}` {Display Name} — capture: daily/ (default)
  - `{principal-slug-2}` {Display Name 2} — capture: daily/{principal-slug-2}/
  ```

- **Change (the addressee facet, one sentence in `:22`'s paragraph):** after the key gist, update
  the parenthetical to *"(a per-source **watermark** for `daily`; the **pointer's key** for
  `relay` — the handoff-doc path, or the `ask`/`answer` `ref`, paired with the recipient — the key
  rule's single home is `references/relay.md`)"* and add: *"Where a routing profile declares more
  than one principal, a pointer may carry a **principal facet** — `(for: <principal-slug>)` after
  the gist — addressing it to a human on the roster; absence = the default principal. The facet
  is dispatch's own vocabulary (this file and the mode references are its single home), and the
  drain is unchanged — partners still grep their slug; the facet says whose traffic it is, not
  who drains it."*
- **Change (Mode dispatch `:54`):** relay's argument gist gains the optional principal: *"a
  partner-supplied `(to-slug, gist, handoff-path)` → `relay` (plus `shape`/`ref` where the payload
  is an ask or answer, plus `to-principal` where a routing profile declares a roster)"*.
- **Why:** A7-4's mechanism — the pattern the filing asked for, on the precedent the capture
  grounded as exact; dispositions 2–4 and 10.
- **Out of scope at this site:** the pickup loop (unchanged — slug-keyed drain); the Log section;
  the human-zone boundary rules (per-principal capture streams under `daily/` remain human-owned,
  read-only, `daily`-mode-only — the boundary follows the zone, not the principal count).

### F8 — `references/relay.md`: addressing, guard 2 pair-equality (A8), the widened key

- **Current:** `:31` inputs (required/per-shape/optional); `:34` guard 2 — *"**`from-slug ≠
  to-slug`** — a partner does not relay to itself … Stated against the addressee model in force:
  one human principal, partners identified by slug — 'self' means the same partner slug."*;
  `:38-48` the idempotency rule keyed `(handoff-path | ref, to-slug)`; `:56-70` the block shapes;
  `:27` backward compatibility; `:94-99` Verify.
- **Change (inputs `:31`):** add to Optional: *"**`to-principal`** (a roster principal-slug, only
  meaningful where a routing profile declares one — `SKILL.md`, *the routing profile*; absent =
  the default principal; an unknown principal-slug stops the act — never guess a roster)."*
- **Change (guard 2 `:34` — the named consequence, shipped by the build that widens the model):**
  replace the model-in-force sentence: *"Stated against the addressee model in force: **'self'
  means the same `(partner-slug, principal)` pair** — under a routing profile, the same partner
  acting for a **different** principal is a legal relay (the cross-principal handoff is the
  traffic a roster exists for); with no profile there is one principal, and the pair test reduces
  to the same slug-equality this rule has always been."*
- **Change (the idempotency key `:38-40`):** the key becomes **`(handoff-path | ref, to-slug,
  principal)`** — the recipient pair, not the recipient slug: *"the same ask relayed to the same
  partner for two different principals is two distinct waits, not a duplicate; an un-annotated
  pointer keys as the default principal, so every existing key is unchanged (backward-compatible,
  no backfill — the pre-shape idiom, `Backward compatibility` above, extends to the facet: an
  un-faceted pointer *is* default-principal traffic, exempt from nothing because it needs no
  exemption)."* The open/checked/no-op ladder is per key, unchanged.
- **Change (block shapes `:56-70`):** the header/pointer examples show the facet where addressed
  — the pointer's paren idiom, beside `blocked:`: `- [ ] `to-slug` Partner Name — gist (for:
  {principal-slug}) → [[…]]`; the report examples gain one addressed variant. Verify (`:94-99`)
  adds: the key check ran against the **pair-inclusive** key; any `(for: …)` facet names a roster
  principal.
- **Why:** A8 verbatim — *"the slug-equality check must widen to pair-equality in the same build
  that widens the model"*; B7-5's brief (disposition 2) names this build for exactly this edit.
- **Out of scope at this site:** the shapes themselves, `ref` mechanics, the legacy pre-shape
  exemption (all B7-5's, shipped, untouched); the relay-when-done reflex text (principal-neutral
  as written — the publisher passes `to-principal` when it has one, which is argument plumbing,
  not reflex change).

### F9 — `references/daily.md`: per-principal capture streams

- **Current:** `:11-19` Step 0 scope — globs `daily/*.md`, per-source watermarks; `:36-51`
  Step 2 — the run block, pointer format, `blocked:` facet sentence at `:43`; `:53-58` the
  record's file header.
- **Change (Step 0):** after the scoped-default paragraph: *"**Where a routing profile declares
  principals** (`SKILL.md`, *the routing profile*), the scan covers **each declared capture
  stream** — glob each principal's stream the same way (`daily/*.md` stays the default
  principal's); the watermark machinery is already per-source, so per-stream watermarks need no
  new mechanics. With no profile, this paragraph is inert."*
- **Change (Step 2, beside the `blocked:` facet sentence `:43`):** *"A pointer routed from a
  non-default principal's stream carries that principal's facet — `(for: <principal-slug>)` — so
  the draining partner knows whose capture it serves and whose thread the answer belongs to;
  default-stream pointers stay un-faceted (byte-identical single-user output)."*
- **Change (file header `:56-58`):** the created-once header's idempotency sentence gains the
  pair: *"…the pointer's key (doc path or ref, per recipient pair) for `relay`…"* — existing
  installs keep their old header (created once; never edited — no backfill).
- **Why:** disposition 4's capture-stream half; the human-zone rules hold per stream (the streams
  are declared inside `daily/`'s zone or a sibling human zone — read-only, `daily`-mode-only,
  unchanged).
- **Out of scope:** classification (Step 1 is principal-neutral — domains route by partner, not
  by human); no-owner handling; the report shape beyond one faceted example.

### F10 — `references/ledger.md`: the board shows principals

- **Current:** `:9-17` the board build + grouped presentation; `:21-28` pointer integrity; `:30`
  the `blocked:` grouping sentence.
- **Change:** beside `:30`'s facet-grouping sentence: *"Where `(for: <principal>)` facets are
  present, additionally annotate the per-partner counts by principal (e.g. 'Researcher 3 — 2 for
  `{principal-slug}`') and render un-faceted items as the default principal's — absence = default,
  never infer. The pointer-integrity check is unchanged (a key is a path or a `ref`; the
  principal widens the key's *pair*, not its *presence*)."*
- **Why:** the board is the standing signal; an addressed item invisible on it would be a silent
  second class of waiting work.
- **Out of scope:** the vitals/wires surface; per-principal boards (one board, one record — the
  design ruling).

## Registration

**None.** No new skill, no new workflow, no new command surface: `module-help.csv` is untouched
(the dispatch row's description already names the modes; the profile changes no invocation form —
it is read, not called). No convention `version:` moves (F1 is prose clarification; disposition 7
declines the reopen), so **no consumer walk and no re-ack**; `consumers:` lists are untouched, so
Group E's bipartite state is unchanged by construction and verified below. The routing profile is
vault-grown, never shipped — the module ships no file for it.

## Out of scope (dispositioned)

- **A generic skill-overlay/extension mechanism** — vetoed by ideation (owner's gut, clerk
  concurring), pre-rejected by the filing itself; this build ships the veto's *reasoning* into the
  contract (F4) instead. Not re-litigated.
- **Per-principal record files / inbox queues** — rejected-because: contradicts the shipped
  "record with a drain, not an inbox" design (`vlt-dispatch/SKILL.md:22`); the principal facet on
  the one record is the same-thing-to-more-destinations the filing asked for.
- **Per-principal permissions, visibility, or notification machinery** — deferred-until-evidence:
  no filing asks for it; v1 is address, not access control (disposition 4).
- **Consult-mode principal awareness** — rejected-for-v1: consult is synchronous and returns to
  the caller at the wheel; no destination exists to widen. `consult.md`'s "a partner does not
  consult itself" stays slug-keyed (no A8 analogue — consult transfers nothing).
- **Principal fields on backlog items, session logs, or any note frontmatter** — deferred by
  disposition 5's revisit trigger (a second consuming surface makes it schema; today it would be
  a seven-consumer `frontmatter` bump for a one-writer facet).
- **Strengthening `overlay_not_append_only` beyond verbatim headings** (A7-8's silent third
  zone) — already-covered-by: the legal landing zone this build opens plus F1's "disguise is
  illegal" sentence remove the motive; a prose-drift check is not Arc-7 scope (matches B7-3 F1g's
  disposition).
- **Who reviews a module-owned deferral, and on what cadence** — explicitly outside the A7-5
  ruling ("it does not perform the review"); the field data rides the capture for whoever does.
- **A `review_after` live-review event as an acceptance check** — deliberately not written: B7-3
  reset the dates to 2026-10/11/12, so no review ripens inside this arc's horizon; a check on it
  would be the unbounded stuck-tail shape §9 exists to prevent. The desk-check (verification) and
  the upgrade check cover the mechanism.
- **Workflow assets reading local conventions** — satisfied at the point a workflow acquires a
  convention read (B7-6's ruled latitude, extended by definition through F4's contract sentence);
  no workflow edit here (`vlt-lint-full.js` sweeps `{wiki}` pages, not `{conventions}` files).
- **The A7-4 workaround mint in the team vault** — vault-side; on this build's arrival the vault
  can retire it onto the profile + relay path at its own pace (migration is the vault's, noted
  for acceptance evidence, never a module act).

## Verification (unit, at rest)

1. **Single-home greps (the member set has one home):** `grep -rn "adoption_first_instance"
   skills/ | grep -v frontmatter.md` shows the two nets (checks.md, vlt-upgrade) no longer naming
   it as *the* exclusion (pointer language only — the authority-rule mentions for who *writes*
   the stamp remain, correctly); no file but `frontmatter.md` enumerates the vault-writable
   members; `grep -rn "for: " skills/vlt-dispatch/` shows the facet defined in SKILL.md and used
   (not redefined) in the three mode refs; guard-2 pair language appears in `relay.md` only.
2. **Fixture desk-checks of record (each a could-have-failed probe), against a temp fixture
   vault:** (a) *divergence exclusion* — base+baseline pair differing only in `review_after:` →
   no divergence; differing in `deferral_threshold:` → flags; (b) *carry-forward table* — vault
   bumped `review_after`, shipped unchanged → vault value survives simulated refresh; vault
   untouched, shipped new date → shipped lands; both moved → vault value kept **and**
   `vault_writable_collisions` line rendered; `adoption_first_instance` stamp → carried (today's
   behavior reproduced); (c) *local-convention truth table* — no-baseline file + live ref-keyed
   mint entry → inventory line, zero findings; no-baseline + no entry → `baseline_missing`;
   local convention's `consumers:` naming `vlt-ingest` → coherence check flags nothing; (d)
   *profile cases* — absent → single-principal, no question; malformed roster (two defaults;
   unknown slug on an addressed relay) → loud refusal + `dispatch_profile_invalid` desk-fired;
   two-principal roster → relay writes `(for: …)` faceted pointer; same ask, same partner, two
   principals → two pointers (distinct keys); same partner + same principal from=to → refused
   (guard 2); same partner, different principal → legal.
3. **Handshake bipartite re-check:** no convention `version:` moved and no `consumers:` list
   changed — **the check of record is `package-lint` Group E** (E1/E2/E3), run and green at rest;
   `frontmatter@7`, `spec@2`, `decision-log@2`, `consult@1` pins all unmoved (a hand grep is an
   editing aid only, never the recorded verification).
4. **Packaging lint:** `uv run tools/package-lint.py` groups **A/B/C/E** green mid-arc — including
   **C6** after F4's contract edit + rule-card `derived_from:` sha re-derive (the probe: run C6
   *before* re-deriving and record the red, then green — the check could have failed).
5. **Fixture extension (R2): not triggered** — no release-gate check added or changed
   (`checks.md` is vault-side lint; `package-lint.py` is untouched). `uv run
   tools/test-package-lint.py` still 21/21, `CASE_FLOOR` stays 21 — run it and record.
6. **Scrub:** no personal or vault-local content in any changed shipped file; every worked example
   uses placeholder paths/slugs (`{principal-slug}`, `_agent/handoffs/…` generic forms); the
   profile example ships no real name.
7. **Cross-file agreement reads:** F1's retired trailers agree with F2/F3's pointered behavior
   (no contradiction between the declaration's prose and either net); F5's five clauses all point
   at the contract and restate nothing; `vlt-mint`'s third route names the same test `checks.md`
   and `vlt-upgrade` apply (the words "live, `ref:`-keyed convention-mint entry" appear
   consistently, pointered to `decision-log.md` for liveness).

Non-release build: no version bump here (the bump rides the arc's release build), no §8.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** Seam coherence at rest — the member set single-homed (only
   `frontmatter.md` enumerates vault-writable fields; both nets point), both interim trailers
   replaced with **no rule-text change** (`frontmatter.md` `version: 7` holds, no re-ack, zero
   stray pins), `package-lint` A/B/C/E green at rest and in the arc's pre-tag run — **C6 green
   after the rule-card sha re-derive, with the red-then-green probe recorded**; harness 21/21,
   `CASE_FLOOR` 21 (R2 not triggered — no gate check touched).
2. **[ship-verifiable]** The mechanism desk-checks of record, each able to fail: the
   divergence-exclusion pair (declared field excluded / undeclared field flags), the
   carry-forward table (vault-kept / shipped-lands / both-moved collision surfaced /
   adoption-stamp behavior reproduced), the local-convention truth table (minted → inventory
   line + no coherence false positive; unminted → `baseline_missing`), and the dispatch-profile
   cases (absent → byte-identical default; malformed → loud refusal; roster → `(for: …)` facet,
   pair-inclusive key, guard-2 pair-equality passing same-partner/different-principal and
   refusing same-pair).
3. **[ship-verifiable — next ordinary upgrade, either vault]** Delivery + the generalized carry
   live on real state — installed `checks.md`/`vlt-upgrade`/contract/`frontmatter.md`/dispatch
   surfaces carry the seam edits (grep-checkable); vlt-core's stamped `adoption_first_instance:`
   survives the 0.10.0 refresh **via the generalized rule** (not the retired special case), and
   the post-flight report renders `local_conventions_intact` and `vault_writable_collisions`
   (both may honestly read empty); bounded — the upgrade happens anyway (owner-run; evidence via
   pasted report + ledger entry).
4. **[field-contingent]** The first sanctioned local convention — a vault mints a convention
   with no stock counterpart; post-mint lint shows the inventory line (no `baseline_missing`, no
   coherence false positive), the split-tripwire count includes it, and a consumer honors it via
   the contract read. Producing vault: **vlt-core only** (owner-run; the factory cannot read it —
   evidence arrives as the owner's pasted lint report/decision-log entry; the named candidate
   event is the owner re-homing vlt-core's A7-8 prose-line rule from the unrelated overlay into a
   minted local convention). If unread by closeout it goes to the watch register, not the gate.
5. **[field-contingent]** The first roster — a multi-principal vault declares
   `_agent/dispatch-profile.md` and routes a cross-principal relay: principal-faceted pointer,
   pair-inclusive key, guard 2 passing same-partner/different-principal; the workaround mint
   retires onto the profile path at the vault's pace. Producing vault: **the work-machine team
   vault only** (the filing's origin; the factory cannot read it; vlt-core is single-principal
   and structurally cannot produce this event) — evidence arrives as the owner's pasted record
   lines/ledger output. If unread by closeout it goes to the watch register, not the gate.

**Builder's exit obligations** (the target `status:` shape): rewrite this brief's `status:` to a
BUILT record — `BUILT <date> — <what landed>; <verification result>. Deviations/notes: (1) … (2) …`
with numbered deliberate deviations (the build-15 precedent); delete any `.decision-log.md` from
the working tree; one commit for the build. The ⚠ owner-review flag in `status:` survives into the
BUILT record until the owner discharges it.
