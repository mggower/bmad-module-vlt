---
title: 'Build #4 — spec-candidate relay-leg retune (the trigger counts revision, not traffic)'
status: 'BUILT 2026-08-24 — relay leg retuned at checks.md:48 to ≥2 same-key `handoff`-shaped
  relay entries (revision, never traffic; consult exclusion sharpened to "handoff-shaped relay
  entries only"), three consumer sites swept (report.md:59 + fix-and-file.md:50 carry `re-relay
  (2 same-key handoff entries)`; vlt-upgrade/SKILL.md:80 retrofit re-pointed as
  pointer-with-gist). Verification-1 derived-vs-expected (fixture tree built in the session
  scratchpad, fresh agent given only the retuned leg text + fixture): case A (round trip:
  1 handoff entry + answer keyed on ref `roundtrip-q` + consult block) derived NO fire —
  expected NO fire, MATCH; case B (same-key re-relay, first entry drained `[x]` to
  archive/dispatch.md, fresh open entry in live dispatch.md, key = path+librarian+default
  principal) derived FIRE, sole candidate doc Y, signal re-relay via ≥2 same-key handoff
  entries, reported loud as `new`, 0 declines honored — expected exactly that, MATCH; case C
  (fan-out, same path to librarian + creative = two keys) derived NO fire — expected NO fire,
  MATCH; 3/3, E3(a) evidence recorded. Verification-2: `grep -rn "2 relay entries" skills/` =
  zero hits; `grep -rln "re-relay" skills/` = the four edited surfaces plus one pre-existing
  rail-side hit (see note 1). Verification-3: all seven retained postures confirmed at
  checks.md:48 (records-never-reports, no stored counter, decline exclusion, handoff-shaped
  +consult exclusion, drained-history counts, repeat partition, never-auto-promote).
  Verification-4: no handshake movement. Verification-5: package-lint A/B/C/E PASS, D SKIPPED.
  Deviations/notes: (1) not a deviation — Verification-2 expected the `re-relay` grep to
  return exactly the four edited surfaces; it also hits `vlt-dispatch/references/relay.md:119`,
  a pre-existing rail-side prose use ("a re-relay after check-off …") that predates this build
  and restates nothing of the candidacy signal; relay.md untouched per Out-of-scope. No other
  deviations.'
module_code: 'vlt'
created: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-22-150000-spec-candidate-relay-leg-fires-on-ordinary-round-trips.md
    (A11-1 — the relay leg counts traffic, not revision; 6 of 8 field fires were single round
    trips)'
roadmap: 'factory/cycles/11-reachability/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-24): build-4 = A11-1 alone, binds E3 (split — (a)
  ship-verifiable fixture check GATES closeout, (b) field window opened by build-4''s release,
  re-anchored off the discharged B10-3(3) per roundtable A6); roundtable A6 scope obligation —
  the fixture dispatch record and the at-rest run of the retuned leg are same-build scope, the
  instrument named and runnable; spike: none (the S-3 sequencing was A9''s window constraint,
  satisfied — S-3 is harvested at cba331a — not a binding on this build); the retune direction
  itself was deliberately left to brief time and is ruled in §Brief-time dispositions.'
risk: 'low — prose retune of one lint-check leg plus three consumer-site sweeps; no convention
  version bump (all edited surfaces are skill references / skill prose, none handshaked), no
  workflow code, no schema, no new finding class.'
---

# Build #4 — the spec-candidate relay-leg retune

`vlt-lint`'s `spec_candidate` check has two OR-composed signals; this build retunes the second.
As shipped, "≥2 `relay:` entries … pointing at the same path" counts **traffic**: a single
ask→answer round trip produces two relay entries citing the same handoff doc, so ordinary use
fires the candidacy flag — field-measured 6 of 8 fires on the 2026-08-22 scoped lint were
single round trips (A11-1). The retune re-keys the count on the relay rail's own semantics so
it counts **revision**: only same-key `handoff`-shaped re-relays — the event `vlt-dispatch`'s
idempotency ladder itself names "new information (a revised spec)" — increment. The two
consumer sites restating the example vocabulary are swept in the same build, plus a third
restating site grounding surfaced (`vlt-upgrade`'s proto-spec retrofit). Every retained posture
at the check stays: records-never-reports derivation, no stored counter, decline exclusion,
relay-entries-only (consult blocks never increment), drained-history counts, the repeat
partition, never-auto-promote.

All rejected alternatives in the parent filing and the ideation rulings are settled — do not
re-litigate. The dated-revision-record leg (the other OR signal) is untouched.

## Brief-time dispositions

1. **Retune direction: candidate direction 1, sharpened by the relay rail's shape/key
   semantics — the leg counts same-key `handoff`-shaped re-relays.** *(The question the
   roadmap deliberately left to brief time — §Questions deliberately left to brief time,
   build-4 / A11-1.)* Grounding, from `skills/vlt-dispatch/references/relay.md` (current
   source, read 2026-08-24):
   - A `handoff` keys on its **doc path** as `(handoff-path, to-slug, principal)`; an
     `ask`/`answer`/`deliver` keys on its **`ref`**, and a `[[wikilink]]` in any pointer is
     "payload, never the key" (*The idempotency rule*).
   - The idempotency ladder makes a second same-key `handoff` entry constructible **only**
     via the checked-off → re-notify branch, which relay.md itself names: "the publisher is
     relaying **again** = new information (a revised spec — #2 stale-spec)". A second
     same-key handoff entry is therefore *definitionally* a revision event — the count
     cannot be inflated by traffic.
   - Back-compat is already solved rail-side: "An un-annotated header **with a path** reads
     as `handoff`" (*Backward compatibility*), so legacy records key correctly with no
     backfill.

   **Why not direction 2** (require the second entry to be a `deliver`-kind revisiting the
   same artifact): a `deliver` keys on its own `ref`, its path is optional payload — and a
   deliver/answer back citing the handoff doc is precisely what an ordinary round trip's
   return leg produces. Direction 2 would preserve the false-fire class the retune exists to
   remove, and "revisiting the same artifact" has no derivable key (the path is
   payload-never-key by the rail's own rule). Rejected on grounding.

   **Why not direction 3** (keep the count, require co-occurrence with the
   dated-revision-record signal): it collapses the two legs into one — the relay leg would
   never fire independently. A publisher who re-relays a revised handoff without writing a
   dated callout is fully legal (the stable-path lifecycle requires no callout; the
   re-notify **is** the revision record on the rail), and direction 3 would make that
   revision invisible. The field wearer's both-signals trust survives under direction 1
   anyway: both legs still exist, OR-composed. Rejected.

   **A deliberate narrowing this keying implies, on the record:** a fan-out of one doc to
   several recipients (the spec `consumers:` fan-out fires the `handoff` shape once per
   recipient) is several *keys* — it no longer fires the leg. Correct: fan-out is
   distribution, not revision. The old text would have fired on it; the fixture's case C
   pins the new behavior.

2. **Signal vocabulary and the one-time repeat-partition migration.** The derived signal's
   name becomes **`re-relay (2 same-key handoff entries)`** (consumer sites F2–F4 carry it).
   Two migration behaviors follow from the check's own shipped mechanics, neither needing new
   text: (a) a standing candidate whose open `{backlog}` item records the old clause
   (`spec_candidate: 2 relay entries`) and still qualifies under the retune reports **loud
   once as `signal changed`**, and Step 4 refreshes the item's clause in place — the designed
   convergence, not a defect; (b) a candidate that qualified only via round-trip traffic
   simply stops deriving as a candidate — its open backlog item stays (lint never closes
   items; the human disposes it), which **is** the false-fire collapse E3(b) measures.

3. **Grounding addition — a third consumer site (EXPANDED, per grounding-at-brief-time.md).**
   The roadmap named two consumer sites (`report.md:59`, `fix-and-file.md:50`). Re-grounding
   swept the shipped tree and found a third restating the signal verbatim:
   `skills/vlt-upgrade/SKILL.md:80`, the proto-spec retrofit ("≥2 relay entries in
   `_agent/dispatch.md` and its `{archive}`-mirrored sibling pointing at the same path") —
   and `checks.md:48` itself points at it ("the same signals the proto-spec retrofit …
   surfaces at upgrade time"). Leaving it would strand the retrofit on the traffic-counting
   signal — exactly the sweep-or-strand obligation the ruling states for the other two sites,
   so it joins scope as F4 (swept as pointer-with-gist per single-home discipline). Not a
   contradiction of any ruling; recorded in the roadmap restamp as a superseding note.
   *(The other `relay entries` mentions in `spec.md:14`/`:90` are a different sense —
   spec-version-bump notification discipline, not the candidacy signal — out of scope, §6.)*

4. **R1 (interim posture): not applicable** — the retuned check ships *with* its mechanism
   (the check's own text is the mechanism; lint is agent-executed prose), and the at-rest
   instrument ships in the same build (Verification-1).

## F1 — `skills/vlt-lint/references/checks.md:48` — the leg itself

**Current state (HOLDS at `:48`, re-grounded 2026-08-24 against the post-build-1/2/3/5
tree):** the *Spec candidates* check's second trigger reads:

> **or** has **≥2 `relay:` entries in `_agent/dispatch.md` and its `{archive}`-mirrored
> sibling pointing at the same path** (drained relay history counts — a drain must not
> silently reset a candidacy signal; **relay entries only** — a `consult:` block grounding in
> the same path is not a relay notification and must never increment this count, or a doc
> consulted twice before filing would self-promote),

**The exact change** — replace that clause (and only it; the dated-revision-record leg, the
derivation sentence, the decline exclusion, the repeat partition, and the never-auto-promote
posture all stand as written) with:

> **or** has been **re-relayed** — **≥2 `handoff`-shaped `relay:` entries sharing the same
> idempotency key (`handoff-path`, `to-slug`, principal) across `_agent/dispatch.md` and its
> `{archive}`-mirrored sibling** (shape and key per `vlt-dispatch`'s relay reference — an
> un-annotated header with a path reads as `handoff`; read the mechanics there, never restate
> them here). A second same-key `handoff` entry can exist only via the relay idempotency
> ladder's checked-off → re-notify branch — the rail's own revised-spec event — so this
> counts **revision, never traffic**: a single ask→answer round trip increments nothing (an
> `ask`/`answer`/`deliver` keys on its `ref`, and a `[[wikilink]]` citing the doc is payload,
> never the key), and a fan-out of one doc to several recipients is several keys, not a
> candidacy (drained relay history counts — a drain must not silently reset a candidacy
> signal; **handoff-shaped relay entries only** — a `consult:` block grounding in the same
> path is not a relay notification and must never increment this count, or a doc consulted
> twice before filing would self-promote),

The builder splices this so the sentence flows into the existing ", flag it
(`spec_candidate`) …" continuation unchanged. Note the retained-posture parenthetical is
preserved verbatim with one sharpening: "relay entries only" → "handoff-shaped relay entries
only" (the consult exclusion is now a special case of the shape rule, but it stays named —
its rationale sentence is load-bearing field teaching).

**Why:** A11-1 — the old predicate counts any two relay entries citing one path; the rail's
key semantics let the same count be read as a revision count with zero new machinery.

**Per-site out of scope:** the derivation posture sentence ("Derive the count from handoff
file state + dispatch relay entries; **no stored counter**") is untouched — the retuned count
derives the same way, from a grep of the same two files.

## F2 — `skills/vlt-lint/references/report.md:59` — the report schema's example vocabulary

**Current state (HOLDS at `:59`):**

> `spec_candidate: [<handoff-doc — signal 2 relay entries | dated revision record; new | signal changed (item updated); owner <partner>; M prior declines honored>, ...]`

**The exact change** — `signal 2 relay entries` → `signal re-relay (2 same-key handoff
entries)`; the rest of the line (including the trailing `# loud entries only …` comment) is
unchanged. The sibling `spec_candidate_standing:` line at `:60` carries no signal vocabulary
— no edit.

**Why:** the sweep-or-strand obligation in the build-4 ruling — a report template teaching
the old signal name would misreport the retuned derivation.

## F3 — `skills/vlt-lint/references/fix-and-file.md:50` — the backlog-item template

**Current state (HOLDS at `:50`, inside the Step-4 spec-candidate filing block at `:47`):**

> `- [ ] Promote <handoff-doc> to {specs} (maintenance, by: <owning partner>) — spec_candidate: <signal, e.g. 2 relay entries>; closes when: promoted per {conventions}/spec.md *Promotion from candidate*, or declined with reason recorded`

**The exact change** — `<signal, e.g. 2 relay entries>` → `<signal, e.g. re-relay (2
same-key handoff entries)>`; nothing else on the line or in the surrounding Guard (`:53`)
changes — the Guard's refresh-the-clause mechanics are exactly what performs disposition 2's
one-time migration.

**Why:** the filed item's `spec_candidate:` clause is the repeat partition's memory; a
template teaching the old vocabulary would seed clauses that read as `signal changed` forever.

## F4 — `skills/vlt-upgrade/SKILL.md:80` — the proto-spec retrofit (grounding addition)

**Current state (grounding addition — EXPANDED; see disposition 3):** Step 3's proto-spec
retrofit clause reads, mid-sentence:

> … or with ≥2 relay entries in `_agent/dispatch.md` and its `{archive}`-mirrored sibling
> pointing at the same path (drained relay history counts — a drain must not silently reset a
> candidacy signal) …

**The exact change** — replace that fragment with a pointer-with-gist (single-home
discipline: the mechanics now live in the retuned check, and this site already points there
for the other leg — "per the `spec_candidate` signal in `vlt-lint`"):

> … or carrying the **re-relay signal** — ≥2 same-key `handoff`-shaped relay entries in
> `_agent/dispatch.md` and its `{archive}`-mirrored sibling (mechanics single-homed at the
> `spec_candidate` check in `vlt-lint`; drained relay history counts — a drain must not
> silently reset a candidacy signal) …

The rest of `:80` (the offer mechanics, relocation-migration discipline,
`adoption_first_instance:` stamping) is untouched.

**Why:** `checks.md:48` promises the retrofit surfaces "the same signals"; an unswept
restatement would strand upgrade-time candidacy on the traffic count the lint-time check just
retired — the exact drift class the sweep obligation exists for.

## Registration

**None.** No new skill or workflow, no `module-help.csv` row. No convention `version:` bump
and no consumer walk: `checks.md`, `report.md`, `fix-and-file.md` are `vlt-lint` skill
references and `SKILL.md:80` is `vlt-upgrade` skill prose — none is a handshaked surface.
"No bump owed" cost check: no operating-contract edit (no C6 rule-card re-derive), no new
`package-lint` check (no E4 declaring case), no asset-node `depends_on` header touched (no
E5). The `spec_candidate` finding class itself is unchanged in name, legal response, and
report placement — only its second signal's derivation retunes.

## Out of scope (dispositioned)

- **The dated-revision-record leg** at `checks.md:48` — untouched; it is the other
  OR-composed signal and A11-1 filed no defect against it.
- **`vlt-dispatch` relay mechanics** (`relay.md`, `ledger.md`) — read-only grounding for this
  build; the retune consumes the shape/key/idempotency semantics as shipped, edits nothing
  there.
- **`spec.md:14`/`:90` "relay entries" mentions** — a different sense (spec version-bump
  notification discipline / the deferred `spec_notification_missing` check), not the
  candidacy signal. Already carries its own design note; untouched.
- **A11-2 and the amendment-trigger work** — deferred to Cycle 12 by Round 1; S-3's harvest
  (verdict `reshape`, `cba331a` + addendum `08f564f`) is Cycle 12's brief-time input, not
  this build's.
- **The backlog items already filed under the old signal in live vaults** — vault-owned; the
  check's own Guard refresh (disposition 2) converges them; no migration ships.
- **Promotion machinery** (`spec.md` *Promotion from candidate*) — the leg still routes to it
  by pointer; never-auto-promote unchanged.

## Verification (unit, at rest — lifecycle step 5)

1. **The E3(a) instrument — fixture dispatch record + agent-run derivation of the retuned
   leg** *(the roundtable A6 scope obligation: the fixture and this at-rest run are
   same-build scope; the instrument is named here per R1)*. Build a temp fixture tree in the
   session scratchpad (never committed, never in the working tree):

   ```
   fixture/_agent/handoffs/2026-08-20-roundtrip-doc.md   # doc X — plain body, no revision record
   fixture/_agent/handoffs/2026-08-18-amended-doc.md     # doc Y — plain body, no revision record
   fixture/_agent/handoffs/2026-08-21-fanout-doc.md      # doc Z — plain body, no revision record
   fixture/_agent/dispatch.md
   fixture/_agent/archive/dispatch.md                     # the {archive}-mirrored sibling
   fixture/_agent/backlog.md                              # empty ## Open — partition/decline inert
   ```

   `dispatch.md` carries (relay block shapes per `relay.md`):
   - **Case A (round trip — must NOT fire):** one open `handoff` entry
     `relay: researcher → librarian` → `[[…/2026-08-20-roundtrip-doc.md]]`, **plus** one
     `relay: librarian → researcher (answer: roundtrip-q)` entry whose pointer cites the same
     doc as a `[[wikilink]]`, **plus** one `consult:` block grounding in the same path (the
     retained consult exclusion, exercised). Two relay entries point at the path — the OLD
     predicate fires here; the retuned one must not.
   - **Case C (fan-out — must NOT fire):** two open `handoff` entries for doc Z, one
     `→ librarian`, one `→ creative` (same path, different `to-slug` = different keys). The
     OLD predicate fires here too; the retuned one must not.

   `archive/dispatch.md` carries:
   - **Case B (re-relay — MUST fire):** a checked `- [x]` `handoff` entry
     `relay: researcher → librarian` → `[[…/2026-08-18-amended-doc.md]]` — with the fresh
     open same-key `handoff` entry for doc Y in live `dispatch.md` (same path, same
     `to-slug`, default principal). Exercises drained-history-counts and the re-relay
     semantics in one case.

   **Protocol:** a fresh agent is given only the retuned *Spec candidates* leg text from
   `checks.md` and the fixture tree, and derives the `spec_candidate` findings. **Expected:**
   exactly one candidate — doc Y, signal `re-relay (2 same-key handoff entries)`, reported
   `new`; docs X and Z derive nothing. Every case could have failed: A and C fire under the
   old predicate, B fails if drained history or the re-notify branch is mis-keyed. **Record
   the derived-vs-expected result in this brief's BUILT `status:`** — it is E3(a)'s evidence.

2. **Cross-file agreement greps** (editing aid + completeness sweep, not the verification of
   record): `grep -rn "2 relay entries" skills/` must return **zero** hits after the build
   (the three swept sites carry the new vocabulary; nothing else restates it);
   `grep -rn "re-relay" skills/` returns exactly the four edited surfaces (F1–F4).
3. **Retained-postures read of `checks.md:48`** — confirm all seven survive verbatim or
   sharpened as specced: records-never-reports, no stored counter, decline exclusion,
   handoff-shaped-relay-entries-only + consult exclusion, drained-history counts, repeat
   partition, never-auto-promote.
4. **Handshake bipartite re-check:** no `version:` moved and no `consumers:`/structure-map
   change — Group E rides the packaging run below; nothing new to walk.
5. **Packaging lint** — mid-cycle `uv run tools/package-lint.py` groups A/B/C/E clean
   (D/`--expect-version` is the release gate, not this build's).
6. **R3:** no finding class added; `spec_candidate`'s legal response stands unchanged at its
   single home (`checks.md:48`, the file-to-backlog beat) — satisfied in place.
7. **R4: not applicable** — the fixture is scratchpad-only, never enters any enumerated
   class; no shipped file is added.
8. **Scrub** — the four edited shipped surfaces carry no personal or vault-local content;
   fixture examples use placeholder slugs (`researcher`, `librarian`, `creative`) and
   placeholder paths only.

*(No Release section — this is not the cycle's release build; the version bump rides the
release build per the roadmap.)*

## Acceptance (live — appended to the roadmap ledger)

Two checks (= E3's ruled halves, roadmap §Evidence-debt dispositions, re-anchored per
roundtable A6).

1. **`[ship-verifiable]` — GATES closeout.** The retuned `spec_candidate` relay leg computes
   correctly against a fixture dispatch record at rest: a single ask→answer round trip does
   **not** fire (case A), a fan-out to two recipients does **not** fire (case C), and the
   same-key re-relay — first entry drained to the `{archive}` sibling — **does** fire with
   signal `re-relay (2 same-key handoff entries)` (case B); the three consumer sites
   (`report.md:59`, `fix-and-file.md:50`, `vlt-upgrade/SKILL.md:80`) carry the retuned
   vocabulary with `grep -rn "2 relay entries" skills/` returning zero. **Instrument (R1):**
   this brief's Verification-1 fixture tree + agent-run derivation protocol — factory-side,
   runnable at rest (the B9-1 standard). **Evidence:** the derived-vs-expected record in this
   brief's BUILT `status:`.
2. **`[field-contingent]` — does not gate.** The false-fire rate actually collapses over a
   fresh two-run observation window **opened by build-4's release** (roundtable A6 — the
   B10-3(3) vehicle was discharged whole 2026-08-23; this is a new window, no B10-3
   dependency). **Baseline:** 6 of 8 `spec_candidate` fires on the 2026-08-22 scoped lint
   were single round trips. **Vault:** `{field-vault}` (readable; runs scoped/full lints
   routinely). **Event, calendar-shaped:** the first two owner-run `vlt-lint` runs after the
   v0.15.0 upgrade; **expected:** zero `spec_candidate` fires attributable to single
   round-trip traffic (a one-time `signal changed` refresh on a surviving standing candidate
   is the designed migration, not a false fire). Goes to the standing watch register at
   closeout.
