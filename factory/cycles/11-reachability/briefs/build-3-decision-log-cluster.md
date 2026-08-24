---
title: 'Build #3 — decision-log v3: subject coherence, a rostered discovery route, and a
  deviation kind (three reachability gaps on one convention, one handshake)'
status: 'BUILT 2026-08-24 — decision-log v3 landed at the single home (F1: version 2→3,
  consumers grow to four, `deviation` in the kind enum with its full contract on the
  `kind:` bullet, new *Subject coherence (v3)* section sibling to *Verdict provenance
  (v2)*, Writers roster at four + the non-writer hand-off sentence); vlt-ingest acks
  decision-log@3 + gains the pointer-only write-through beat after the conventions-read
  paragraph (F2); vlt-mint/vlt-upgrade/vlt-lint re-ack @3, no body edits (F3–F5).
  Verification: `uv run tools/package-lint.py` → "PASS group E — self-description
  integrity" / "package-lint: A/B/C/E PASS, D SKIPPED — vlt 0.14.0", exit 0 (acceptance
  check 1 GREEN); roster↔consumers read: the four write-through ops and the four
  `consumers:` entries are the same set, and the non-writer sentence names only rostered
  routes (vlt-lint sweep / vlt-upgrade upgrade-time); single-home greps: `grep -rn
  decision-log skills/vlt-ingest/` returns only the ack + the pointer beat (no restated
  mechanics), `grep -rn "convention-edit" skills/` returns only the convention itself +
  `vlt-upgrade/SKILL.md:78` (the reconcile''s own matched classes, correct unedited),
  and no site outside the convention enumerates the kind list (acceptance check 2
  GREEN); no `.decision-log.md` in the working tree. Deviations/notes: no deviations.'
module_code: 'vlt'
created: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-23-180100-rule-shelved-as-trailing-clause-is-unreachable-by-subject.md
    (A11-4 — off-subject trailing clause unreachable by every ref-keyed reader)'
  - 'factory/inbox/2026-08-21-150214-decision-log-writer-roster-admits-no-discovery-site.md
    (A10-12, issue #6 — writer roster admits no discovery site; no non-writer hand-off stated)'
  - 'factory/inbox/2026-08-21-150215-decision-log-kind-has-no-value-for-scoped-deviation.md
    (A10-13, issue #7 — no `kind:` for a scoped deviation; forcing `convention-edit`
    mis-scopes the reconcile pass)'
roadmap: 'factory/cycles/11-reachability/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-24): build-3 grouping (the batch''s only
  decision-log bump — one handshake, not three); D1 (A11-4 write-time, no new finding
  class, reopen clause on ceremony-mediation); D2 (decision-log 2→3, bipartite
  verification not abstinence; build-3 bumps regardless of D1); roundtable A14 (the
  ceremony-mediation question answered below, disposition 2)'
risk: 'low-moderate — one convention rule change bumping decision-log.md `version:` 2→3
  with a consumer walk that grows the roster to four (vlt-ingest joins); prose-only edits
  across five files, no code, no new finding class, no release-gate check touched'
---

# Build #3 — the decision-log cluster

## Intent

Three reachability gaps live on one convention,
`skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md`, and this build
closes all three in one `version:` bump (the grouping's whole point — three separate
builds would mean three handshakes on one convention):

- **A11-4** — nothing constrains an entry's prose to its `ref:` subject, so a rule
  shelved as a trailing clause under an unrelated `ref:` is unreachable by every
  ref-keyed reader *by construction* (the read side — lint's read-before-flag, upgrade's
  reconcile — resolves only by subject). Fix: a **write-time subject-coherence rule**
  (v3), per D1 — no new finding class.
- **A10-12** — the Writers roster is a closed list of three, admits no discovery site,
  and the convention is silent on what a non-writer op does with a deviation it
  surfaces. Fix: **roster `vlt-ingest`'s write-through** (the proven discovery site) and
  **state the non-writer hand-off** — see disposition 1.
- **A10-13** — the `kind:` enum has six values, all presupposing the governed object
  changed; a scoped deviation forced into `convention-edit` enters the reconcile pass's
  scan and reads perpetually unreconciled. Fix: a **`deviation` kind** with its reconcile
  relationship stated — see disposition 3.

This is the cycle's through-line applied to the governance memory itself: routes and
legal values that ought to exist and don't, so correct behavior has nowhere legal to
land. All rejected alternatives in the parent filings are settled — **do not
re-litigate**. D1 and D2 are cited, never re-derived.

## Brief-time dispositions

1. **A10-12's discovery route: widen the roster to `vlt-ingest` (narrowly), and state
   the non-writer hand-off — both halves, each where it is strongest.** The filing's
   resolution 1 taken for the proven discovery site only, plus resolution 2's missing
   sentence for everyone else:
   - `vlt-ingest` joins the Writers roster as a fourth named write-through — *in-session
     user rulings on a governance deviation surfaced mid-ingest* — with the matching
     `consumers:` entry and `depends_on` ack (F2). Grounds: ingest is the op that
     actually hits a rule that cannot be satisfied as written; the field already
     produced two well-formed, correctly-keyed ingest-run entries ("the writes look
     right; it is the roster that does not admit them" — the filing's own evidence); and
     the convention's honest limit (`decision-log.md:91`) says a ruling made and never
     written through is invisible **by construction** — so a defer-to-next-lint-run
     hand-off would recreate exactly the invisible class this convention exists to
     reduce. **Rejected:** hand-off-only with a deferred route (recreates the
     never-written-through class); the filing's third shape, B9-4-style checked
     registration of write authority (`local_consumers:` registration is the
     vault-grown-consumer mechanism; moving a *shipped* op's write authority into
     vault-local registration machinery is over-machinery for a one-op gap, and the
     roster is described as load-bearing for the handshake — keep it closed and
     enumerated).
   - The Writers section gains one **non-writer sentence**: an op outside the roster
     **never appends** — it surfaces the deviation and the user's ruling, and the record
     lands through a rostered route (the discovering op where rostered; otherwise
     `vlt-lint`'s write-through at the next sweep — the standing lint-as-recorder beat,
     `skills/vlt-lint/references/fix-and-file.md:19` — or `vlt-upgrade`'s at upgrade
     time). The hand-off names real routes, so it does not recreate the gap in prose
     form (the filing's own warning about resolution 2).

2. **A14 (roundtable) — is A10-12's discovery route ceremony-mediated? YES; D1's reopen
   clause does not apply, and no subject-coherence finding class enters build-3.** D1's
   test is "the writer passes a chokepoint the module controls." Under disposition 1,
   every legal write path into the log passes shipped-op text the module controls:
   `vlt-mint`'s ceremonies, `vlt-upgrade`'s Step 3.7 write-through
   (`skills/vlt-upgrade/SKILL.md:88`), `vlt-lint`'s fix-and-file write-through
   (`fix-and-file.md:19`), and — new this build — `vlt-ingest`'s write-through beat
   (F2), which points at the convention for the entry shape exactly as the other three
   do. The pre-build field practice (user-direct in-session writes during ingest with
   **no** shipped beat) was precisely the un-mediated route; this build *rosters and
   mediates it* rather than leaving it outside the chokepoint. The subject-coherence
   rule therefore reaches every writer through the single-home pointer all writers
   follow ("points here for the shape"), and D1's condition — "if the decision-log's
   authors turn out not to be reliably ceremony-mediated in practice, A11-4 flips to
   detection and build-3 grows a finding class" — stays a *field* reopen condition, not
   a brief-time fact. Recorded per roundtable A14.

3. **A10-13: add `deviation` to the `kind:` enum (resolution 1); resolution 2
   rejected.** The new kind's contract, stated at the single home (F1): a `deviation`
   licenses a **scoped exception while the governed rule stands unchanged**; `ref:`
   names the rule deviated from; it is a **gated** kind (`verdict:` with v2 provenance
   required); it carries **no `convention:` line** (that line stays "convention-edit
   ONLY — the version delta"; nothing moved); and the reconcile pass does **not** scan
   it for a superseding entry — nothing changed, so no superseding entry can or need
   exist (the exact mis-scope A10-13 verified end-to-end). It stays live until
   superseded like any entry. **Rejected:** declaring `convention-edit` covers it —
   that blesses using a required field against its own definition (`convention: …
   unchanged`) and leaves the mis-scoped reconcile scan as contract; the filing's
   verified mechanism is the disqualifier.

4. **A11-4's mechanism is D1's, cited not re-decided:** write-time subject-coherence
   discipline, same posture as verdict provenance (v2) — write-side, enforced by the
   ceremonies that write entries, **no new finding class ships with v3**. The v3 section
   carries the same forward clause as v2 (`decision-log.md:99`): a build that later adds
   a subject-coherence checker owes that check its own stated legal response.

5. **R1 (interim posture): substantive, one paragraph.** Nothing ships ahead of its
   mechanism. The subject-coherence rule's mechanism *is* write-side ceremony
   enforcement, which exists at ship (the v2 verdict-provenance precedent — all four
   rostered write beats point at the convention for shape); the deliberately-unshipped
   detection net is not a missing mechanism but a D1-rejected one, with the reopen
   clause on the roadmap as the recorded route if the write-time premise fails in the
   field. The `deviation` kind and the rostered route are self-mechanizing (schema +
   beat, both shipped this build).

## F-sites

### F1 — `skills/vlt-setup/assets/governance/_meta/conventions/decision-log.md` (the single home; all three gaps)

**Current state (all re-grounded 2026-08-24; the file is untouched by builds 1–2):**
`version: 2` at `:11`; `consumers: [vlt-mint, vlt-upgrade, vlt-lint]` at `:12`;
`last_updated: 2026-08-15` at `:4`; the `kind:` enum (six values) at `:39`; the `ref:`
schema line at `:40`; the `convention:` delta line ("convention-edit ONLY") at `:42`
*(capture cited `:43` — shifted one line; HOLDS)*; the `kind:` machine-key bullet at
`:46`; the `ref:` findable-by-subject bullet at `:47`; *Verdict provenance (v2)* at
`:49-57` with the write-side enforcement statement at `:99`; the Writers roster at
`:76-80`; the Readers list at `:82-85`; the honest limit at `:91`.

**The changes:**

1. **Frontmatter:** `version: 2` → `version: 3` (`:11`); `consumers:` → `[vlt-mint,
   vlt-upgrade, vlt-lint, vlt-ingest]` (`:12`); bump `last_updated:` (`:4`).
2. **`kind:` enum (`:39`):** append `deviation` — the line becomes
   `- kind: mint | capability-change | convention-edit | stage-promotion |
   upgrade-ruling | retirement | deviation`.
3. **`kind:` bullet (`:46`):** after the existing reconcile sentence, add the
   deviation relationship (disposition 3): a **`deviation`** licenses a scoped
   exception while the governed rule stands unchanged; its `ref:` names the rule
   deviated from; it is gated (verdict + provenance per v2); it carries **no
   `convention:` line**; and it is **outside the reconcile pass's superseding-entry
   scan by design** — nothing changed, so no superseding entry exists to look for. It
   stays live until superseded like any entry.
4. **New section — *Subject coherence (v3)*,** placed as a sibling of *Verdict
   provenance (v2)* (after `:57`), mirroring its shape: **one entry, one governed
   subject** — an entry's prose stays on its `ref:` subject; a rule or ruling about a
   different governed object gets its **own entry** under its own `ref:` (or its own
   home), never a trailing clause. State the why in the rule itself (the A11-4
   mechanism): every reader that matters resolves by subject, so an off-subject
   trailing clause is unreachable **by construction** — the better the ref discipline,
   the more invisible the clause. Applies to every **new** entry from v3 on; **no
   backfill** (append-only — pre-v3 entries are read as written). Write-side, enforced
   by the rostered write beats (the v2 posture, `:99`); **not** covered by the
   read-before-flag, which keys on `ref:` only; **no new finding class ships with v3**
   — a build that later adds a subject-coherence checker owes that check its own stated
   legal response (D1).
5. **Writers roster (`:76-80`):** add the fourth writer line — `vlt-ingest`'s
   write-through: in-session user rulings on a governance deviation surfaced
   mid-ingest — and, closing the roster, the **non-writer sentence** (disposition 1):
   an op outside this roster never appends; it surfaces the deviation and the user's
   ruling, and the record lands through a rostered route (the discovering op where
   rostered; otherwise `vlt-lint`'s write-through at the next sweep or `vlt-upgrade`'s
   at upgrade time).

**Why:** A11-4 (item 4), A10-13 (items 2–3), A10-12 (items 1, 5). One file, one bump —
the grouping ruling honored. *Out of scope at this site:* no edit to the classifiability
tail, the supersession idiom, or the enforcement section — none of the three gaps
touches them; the v3 additions are new text plus the enum line, never a rewrite of v2
content (the base stays refresh-safe prose).

### F2 — `skills/vlt-ingest/SKILL.md` (the new writer: ack + beat)

**Current state:** `depends_on: ["frontmatter@13", "wiki-index@2",
"wiki-consolidation@1", "wiki-supersession@2", "write-verification@3"]` at `:4` — **no
decision-log entry**; a full grep of `skills/vlt-ingest/` for any decision-log
reference returns nothing (A10-12's gap, re-verified against the current tree). The
conventions-read bullet at `:26` ("Read the conventions you will obey") is the natural
neighbor for the new beat.

**The changes:**

1. **Ack:** append `"decision-log@3"` to `depends_on` (`:4`).
2. **The write-through beat** — one short paragraph in *On Activation*, after the `:26`
   conventions-read bullet (a standing rule, not a step, since a deviation can surface
   at any step): when an ingest surfaces a governance deviation — a convention that
   cannot be satisfied as written — and the **user rules on it in-session**, append the
   ruling to `_agent/mint/decision-log.md` in the shape single-homed at
   `{conventions}/decision-log.md` — **follow it; do not restate the entry mechanics
   here** (the fix-and-file.md:19 pattern: point, don't restate). This records the
   user's decision, never the op deciding; the write-through **never stamps
   `adoption_first_instance:`** (the stamp is the authorized ceremonies' — the
   authority rule, `vlt-mint` Step 4). No ruling → nothing to append; surfacing alone
   is not an entry.

**Why:** A10-12 — the discovery route, made ceremony-mediated (dispositions 1–2). The
beat is deliberately a pointer: `vlt-ingest` becomes a consumer that *recites no
mechanics*, so the single-home discipline holds and future convention changes reach it
through the handshake alone.

### F3 — `skills/vlt-mint/SKILL.md:3` (ack)

`depends_on: ["spec@2", "frontmatter@13", "decision-log@2"]` → `"decision-log@3"`. No
body edit: the mint ceremonies already point at the convention for the entry shape and
provenance (`:105` cites `{conventions}/decision-log.md` *Verdict provenance*); the v3
subject-coherence rule reaches them through that same pointer.

### F4 — `skills/vlt-upgrade/SKILL.md:3` (ack)

`depends_on: ["spec@2", "decision-log@2"]` → `"decision-log@3"`. No body edit — two
deliberate non-edits, dispositioned: **(a)** the reconcile pass at `:78` already names
its matched classes ("gated `convention-edit` (or `upgrade-ruling`)"), which is exactly
what A10-13 asked for; a `deviation` entry is outside that scan by enumeration, and the
relationship is stated at the single home (F1 item 3), not restated here. **(b)** the
Step 3.7 write-through at `:88` already defers entry mechanics to the convention
("follow it; do not restate") — v3 rides in unedited.

### F5 — `skills/vlt-lint/SKILL.md:4` (ack)

`depends_on: [… "decision-log@2"]` → `"decision-log@3"` (the list currently ends
`"consult@1", "decision-log@2"`; build-2's `extraction@6` re-ack sits earlier in the
same line — leave it untouched). No body or `references/` edit — dispositioned: the
read-before-flag (`references/checks.md:40`) keys on `ref:` only and is explicitly not
the v3 rule's enforcement surface (D1: no new finding class); the lint write-through
(`references/fix-and-file.md:19`) already points at the convention for shape. Nothing
in `vlt-lint` restates the `kind:` enum or the writer roster, so nothing strands.

## Registration

**No new skill, no new workflow — nothing enters `marketplace.json` or
`module-help.csv`.** The registration this build owes is the **consumer walk**: the
decision-log convention's rule change (2→3) re-acks all four listed consumers in this
same build — `vlt-mint` (F3), `vlt-upgrade` (F4), `vlt-lint` (F5), `vlt-ingest` (F2,
the new fourth). Bipartite target: `consumers: [vlt-mint, vlt-upgrade, vlt-lint,
vlt-ingest]` ↔ each of the four `depends_on` lists pinning `decision-log@3`. Priced
non-costs, per anatomy §5: no `vault-operating-contract.md` edit (no C6 rule-card
re-derive); no new or changed `package-lint` check (no E4 declaring case); the
convention has no workflow-asset consumers (no E5 `// depends_on:` header walk — the
roster is skills-only, now four of them).

**Roster-expansion note (two-place record):** D2's handshake-inventory row for build-3
lists three consumers — the roster *as read at capture* (`decision-log.md:12`, then
three). Disposition 1 grows it to four. This is a brief-time-disposition consequence,
not a stale-grounding correction (source never moved); D2's actual ruling — bipartite
verification, however many consumers — is unchanged and is exactly what Group E
verifies. The roadmap's status line carries the matching superseding note (appended
this run); D2's "no build carries two handshakes" holds — build-3 still carries exactly
one.

## Out of scope (dispositioned)

- **A subject-coherence lint heuristic / finding class** — rejected by D1 (write-time;
  writers pass module-controlled chokepoints; the cheapest lint class is the one not
  added, per A11-11's own finding). The reopen clause is on the roadmap (D1) and
  re-affirmed at brief time (disposition 2); not silently dropped.
- **"Any shipped write op" as an open roster grant** — rejected; the roster stays
  closed and enumerated (it is "the roster the handshake protects"). A future
  discovery-site op earns its line the way `vlt-ingest` did: a filing, a ruling, a
  bump.
- **B9-4-style checked registration of write authority** — rejected (disposition 1):
  vault-local registration machinery for a shipped op's authority is over-machinery for
  a one-op gap.
- **`vlt-upgrade` reconcile-pass text edit (`SKILL.md:78`)** — already names its
  matched classes; the deviation relationship single-homes at F1 (see F4).
- **Backfill or migration of existing field entries** — the two observed ingest-run
  entries and the `convention-edit`+`convention: … unchanged` workaround entry are
  vault-owned, append-only records; superseding the workaround with a `kind: deviation`
  entry is the vault's own act under the existing supersession idiom (acceptance check
  3 watches for it; the module never rewrites a vault's log).
- **A10-10 (`wiki-index` rule-vs-example)** — build-8 scope with its own conditional
  handshake (D2 inventory, roundtable A15); a different convention entirely (the
  Round-1 grounding correction).
- **The council/provenance machinery (v2 content)** — untouched; v3 is additive.

## Verification (unit, at rest)

1. **Handshake bipartite re-check — the check of record is `package-lint` Group E**
   (`tools/package-lint.py`: E1 handshake-bipartite, E2 structure-map SSoT, E3
   stray-pin). Run the mid-cycle `uv run tools/package-lint.py` **A/B/C/E** pass; Group
   E must come back clean with `decision-log` at `version: 3`, four listed consumers,
   four current acks. A hand `grep "decision-log@" skills/` is an editing aid only,
   never the recorded verification (the build-23 lesson — Group E derives both sides).
2. **Roster ↔ consumers agreement (prose half Group E cannot see):** read the Writers
   roster (F1 item 5) against `consumers:` (`:12`) and confirm the four write-through
   ops and the four consumers are the same set, and that the non-writer sentence names
   only rostered routes. Agent-run read, recorded in the BUILT status.
3. **Single-home check:** grep the four consumer skills for restated entry mechanics —
   `vlt-ingest`'s new beat must point at the convention and restate nothing (the
   fix-and-file.md:19 shape); no consumer carries the `kind:` enum or the roster.
4. **Enum-site sweep:** `grep -rn "convention-edit" skills/` — confirm the only
   non-convention site remains `vlt-upgrade/SKILL.md:78` (the reconcile's own matched
   classes, correct unedited); no site enumerates the six-value kind list that would
   now strand at seven.
5. **R2 (fixture extension): not applicable** — no release-gate check added or
   changed.
6. **R3:** no new finding class ships (D1); the v3 section itself carries the
   forward clause (a later checker owes its stated legal response) — the same shape
   `:99` carries for v2. Stated here so the builder doesn't invent a finding class out
   of caution.
7. **R4 (enumeration widening): not applicable** — no file is added to any enumerated
   class (all edits are in-place prose; the one enumeration touched, `consumers:`, is
   itself the change and is verified by item 1).
8. **Scrub:** no personal or vault-local content in any changed shipped file; the F1/F2
   prose uses placeholder paths (`{conventions}/…`, `_agent/mint/decision-log.md`)
   only. The field vault's name appears nowhere in this build's edits.

This is not the release build — no version-string bumps, no `--expect-version` gate
here (Release section omitted; the bump rides the cycle's release build).

## Acceptance (live — same checks appended to the roadmap ledger this run)

1. **`[ship-verifiable]` — GATES closeout.** The decision-log handshake is
   bipartite-consistent at `version: 3` with the **four**-consumer roster (`vlt-mint`,
   `vlt-upgrade`, `vlt-lint`, `vlt-ingest`) — every consumer listed ↔ every ack
   current. **Instrument (R1):** `tools/package-lint.py` Group E (E1), factory-side,
   runnable at rest; **evidence:** the clean Group E line recorded in this brief's
   BUILT status.
2. **`[ship-verifiable]` — GATES closeout.** The three additions read coherently at
   the single home and nowhere else: the *Subject coherence (v3)* section present with
   the no-new-finding-class + later-checker-owes-response clause (D1); the `deviation`
   kind in the enum with its stated contract (gated, `ref:` = the rule deviated from,
   no `convention:` line, outside the reconcile scan by design); the Writers roster at
   four with the non-writer hand-off naming only rostered routes; and **no consumer
   restates mechanics** — `vlt-ingest`'s new beat is a pointer (single-home check).
   **Instrument (R1):** the brief's Verification items 2–4 protocol (agent-run read +
   greps against the shipped tree), factory-side, at rest; **evidence:** the recorded
   read/grep results in the BUILT status.
3. **`[field-contingent]` — does not gate.** The new routes are actually used: a
   mid-ingest governance deviation ruled in-session lands as a rostered `vlt-ingest`
   write-through entry in the vault's log, and/or the vault supersedes its observed
   `convention-edit`+`convention: … unchanged` workaround entry with a `kind:
   deviation` entry that the next `vlt-upgrade` reconcile pass then reads clean (not
   surfaced as unreconciled). **Vault:** `{field-vault}` (readable; it holds both the
   two ingest-run entries and the workaround entry — a standing reason). **Event:** the
   first post-v0.15.0 ingest run that surfaces a deviation, or the vault's own
   supersession act followed by the next upgrade's reconcile pass. Unbounded — goes to
   the standing watch register at closeout.
