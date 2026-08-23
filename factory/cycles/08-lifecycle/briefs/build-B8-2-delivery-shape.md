---
title: 'Build #B8-2 — the delivery shape (unsolicited inline-payload delivery gets a legal
  form, and the pointer-integrity check''s pending legal response ships with it)'
status: 'BUILT 2026-08-17 — all F-sites landed (F1 relay.md fourth shape + wikilink/proto-deliver
  rules; F2 ledger.md marker discharged, response rewritten, counting rules + second lane; F3
  SKILL.md ×4; F4 daily.md seeded header; F5 contract :242; F6 module-help.csv row 11). Unit
  verification all PASS: doc-less grep clean across shipped surface, three-shapes grep 0,
  marker grep 0, deliver present in every F1 subsection, fixture two-application agreement
  (findings=0 legacy=2 proto-deliver=2, hand vs script), package-lint A/B/C/E PASS. Deviations:
  (1) three additional enumeration sites inside relay.md, not itemized in F1''s change list,
  widened to name deliver — the intro act list (:7), the manual-invocation shape clause (:15),
  and the doc-less-pointer parenthetical (:57) — required for the doc-less-without-deliver grep
  to be zero and to avoid shipping stale prose in the shape''s own home; (2)
  vault-rule-card.md re-derived (derived_from sha256 + dates only, no content change — the card
  carries no shape enumeration) after the F5 contract edit staled it, required by package-lint
  Group C; (3) ledger.md''s finding-class definition widened to "an ask/answer/deliver with no
  ref" — the brief''s F2 list named only the marker removal and response rewrite, but grid
  closure requires a keyless deliver to be a finding.'
module_code: 'vlt'
created: '2026-08-17'
derives_from:
  - 'inbox/2026-08-17-140000-handoff-shape-has-no-form-for-an-inline-payload.md (A8-2 —
    the missing shape, the unperformable legal response, and the attached
    legacy-denominator lead folded in as evidence debt 3)'
roadmap: 'skills/reports/inbox-evolution-arc8-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-17): B8-2 grouping row + roundtable A5 (act-grid
  closure, terminal state of the seven, shape-enumeration sweep, commit-pinned evidence
  read); pre-ideation ruling 3 (R3 home generalized — the response lives where the check
  lives); evidence debt 3 (fold the denominator lead into this build); no-history-rewrite
  binding as scoped by A5. Depends on B8-1 (shipped, commit 8b3070a).'
risk: 'low-moderate — widens the relay shape set (a shipped vocabulary the field already
  strains against) and rewrites a finding class''s legal response; no convention version
  bump (relay.md is not a handshaked convention; frontmatter.md''s address rule is
  untouched), so no consumer walk. The riskiest joint is the read-side reclassification of
  the seven drained findings — mitigated by making it zero-write and denominated.'
---

# Build #B8-2 — the delivery shape

B7-5 shipped three relay shapes (`handoff`/`ask`/`answer`) and within two days of field use
the vault produced a legitimate act — **unsolicited delivery with an inline payload** —
that none of them fits. The field's workaround (`handoff` header + invented `ref`, no doc)
generated seven pointer-integrity findings whose stated legal response ("re-fire correctly
keyed") cannot be performed: no correct key exists. B8-1 stamped that truth on the check as
a known-incomplete marker (its R1 interim posture); this build discharges the marker by
shipping the shape, rewriting the check's legal response under R3's regime, ruling the
terminal legal state of the seven drained findings, and defining the legacy line's unit and
wikilink-as-path rule (evidence debt 3). Acceptance claims **grid closure**, not
fit-to-the-seven — the B7-5 lesson (A5).

All rejected alternatives in the parent filing are settled — do not re-litigate. In
particular the field disposition (nothing retro-fixed, all seven drained) and the
no-history-rewrite posture stand as scoped by A5: retroactive re-keying/re-firing is
forbidden; performing a legal response on a drained line is not.

**Evidence read (A5's commit-pinned read-before-brief pin, honored 2026-08-17):** the
malformed relay blocks were read in the live vault's dispatch record, read-only, at
**vlt-core commit `4f0656805c5946f30b4f9eed8e0b4df8939270a4`**. Composition, precisely:
**six** `(handoff, ref: …)` blocks in the 2026-08-15 21:30–22:10 batch (record lines 315,
318, 321, 324, 327, 330 at that commit) plus **one** `(handoff)`-annotated block at
2026-08-15 20:35 (line 309) carrying neither `ref` nor path — seven findings total, six
with a `ref`, matching the filing's own "six of the seven carry a `ref:`". The roadmap
pin's phrase "the seven malformed `handoff`+`ref` relay blocks" was imprecise; a
superseding note is in the roadmap. All seven are `[x]` drained; every payload is written
inline and cites durable `_agent/research/…` notes and wiki concepts as `[[wikilinks]]` —
none cites a handoff-zone doc, because none exists.

## Brief-time dispositions

1. **The shape choice (deferred to brief time by the rulings; capture's note weighed):
   option 2 — a fourth shape, named `deliver`, keyed by `ref`.** *(Headless judgment
   call.)* Reasoning against each alternative:
   - **Option 1 (widen `answer`)** breaks the pairing invariant the check leans on —
     `answer`'s `ref` "must be the originating `ask`'s `ref`" (`relay.md:23`), which is
     what makes an unpaired `answer` detectable. Making the precondition optional turns
     that cross-check conditional and makes "answer" a lie for traffic that answers
     nothing.
   - **Option 3 (require a doc)** pushes against the field's observed habit (capture's
     note, confirmed at the pin: seven real deliveries in one evening, every payload
     already citing durable `_agent/research/` notes) — forcing an `_agent/handoffs/` doc
     would duplicate content that already has a durable home, purely to satisfy the key
     rule. The vocabulary would be legislating against the vault's legitimate act, the
     exact through-line failure this arc prosecutes.
   - **Option 4 (fix the response only)** leaves the act itself illegal; the field would
     keep producing it and the check would keep flagging correct behavior. It repairs R3
     compliance while preserving the gap. (Its annotate-in-place idea is not needed even
     for the seven — see disposition 3, which resolves them with zero writes.)
   - **Option 2** matches what the field already invented (delivery + publisher-chosen
     key), keeps `ask`/`answer` pairing intact, and closes the grid symmetrically.
     **Name:** `deliver`, not `note` — verb symmetry with `ask`/`answer`, and `note`
     collides with the observed payload idiom (every one of the seven writes
     "**note:** [[…]]" for its research artifact).

2. **The act grid (A5 — every cell legal or reasoned-excluded).** Axes: solicitation ×
   payload home, plus the two axes the seven relays and their neighbors surface
   (keyedness; broadcast). With `deliver` shipped:

   | | **doc'd** (durable doc at a stable handoff-zone path) | **pathless** (payload inline; durable artifacts cited as wikilinks) |
   |---|---|---|
   | **solicited** | `handoff` fired at the asker (path-keyed) — legal, unchanged; an `answer` may also cite the doc (path optional, `relay.md:23`) | `ask` → `answer` (`ref`-keyed pair) — legal, B7-5, unchanged |
   | **unsolicited** | `handoff` (the original contract; incl. the spec `consumers:` fan-out) — legal, unchanged | **`deliver`** (`ref`-keyed) — the hole, closed by this build |

   - **Keyedness axis (surfaced by the seven):** post-B8-2, every shape carries a key
     (path or `ref`) — the seven show the field *wants* keys (six invented one); `deliver`
     restores the spam guard their form silently lost. Unkeyed traffic remains exactly the
     two tolerated legacy lanes (pre-shape un-annotated, and the proto-`deliver` lane of
     disposition 3) — tolerated, denominated, never a legal form to write anew.
   - **Broadcast axis (surfaced by the adjacent `(bell declaration)` block, vlt-core
     record line 299 at the pinned commit): reasoned exclusion.** A multi-recipient
     declaration is N pre-addressed acts — one relay per recipient, each independently
     legal (as `deliver` where pathless); the combined multi-recipient header is not
     legislated as a shape. One act, one recipient stands (`relay.md:78`'s "one relay =
     one pre-addressed act").
   - **Durable-citation axis (all seven payloads):** a `[[wikilink]]` is legal payload in
     **every** shape and is never the key — this generalizes `relay.md:23`'s
     answer-scoped sentence to a shape-general rule (F1), which is also what makes the
     legacy line's wikilink rule (disposition 4) coherent with the shapes.
   - **Batched `answer`/`deliver` headers** (observed in post-filing traffic, 2026-08-17,
     outside the seven): **out of scope, dispositioned** — see Out of scope.

3. **Terminal legal state of the seven drained findings (A5 required ruling):
   denominated-legacy, by read-side reclassification — zero writes to the record.**
   Shape-annotated pathless pointers written **before `deliver` existed** are
   **proto-`deliver` traffic**: tolerated as written, drained normally, exempt from the
   key check, reported by `ledger` as a **denominated count** ("N proto-`deliver`
   pointers (pre-shape)"), never as findings. This is the same posture the pre-shape
   legacy lane already holds (`relay.md:27`), extended to the shape's own pre-history.
   Scope of the no-history-rewrite binding honored exactly as A5 drew it: no line is
   re-keyed, re-fired, or edited; the legal response performed on the drained lines is
   the reclassification itself, which lives in the check's definition, not in the record.
   The seven therefore terminate as **7 counted in the proto-`deliver` denominator, 0
   findings** — satisfying A5's acceptance form ("zero or denominated-legacy").

4. **The legacy line's unit and wikilink-as-path rule (evidence debt 3, folded here).**
   - **Unit: the pointer line**, matching the integrity check's own scope ("for every
     pointer in a `relay:` block, resolve its key", `ledger.md:23`) — one scope, one
     unit; a block's item count never inflates or deflates the denominator.
   - **Pathless, defined:** a pointer line is pathless iff it carries no **key-path** — a
     trailing `→ [[…]]` link (or plain path) resolving under the handoff zone
     (`_agent/handoffs/` or `_agent/specs/`, the two homes `relay.md:31` names for
     `handoff-path`). **Any other wikilink — research notes, wiki concepts — is payload
     and never counts as a path.** This is what makes the count reproducible: the filing's
     37-vs-2-vs-18 irreproducibility is exactly block-unit vs any-wikilink-counts vs
     ad-hoc, and each ambiguity is now closed.

5. **Interim posture (R1): no rule ships ahead of its mechanism in this build.** The
   shape, the rewritten legal response, the proto-`deliver` denomination, and the legacy
   definitions all land in the same build; B8-1's inherited interim posture (the
   known-incomplete marker) is **discharged by this build**, same release (0.11.0) as A3
   preferred — the marker's field-visible terminal state is not exercised. No residual
   window exists.

6. **`ref` semantics for `deliver`** (small, but the builder needs it): publisher-chosen
   kebab slug, unique per delivery act, reused only to re-notify — the open/checked/no-op
   ladder (`relay.md:44-46`) applies per `(ref, to-slug, principal)` unchanged: open →
   no-op; checked-off → fresh open pointer (revised delivery = new information). A
   `deliver` `ref` is stable by construction, like an `ask`'s — never revised, only
   re-fired.

## F-sites

All sites re-grounded 2026-08-17 against the working tree at `8b3070a` (B8-1 built,
uncommitted-nothing relevant). Capture-time cites: relay.md `:21/:22/:23/:40` **HOLD**;
ledger.md `:25/:26` **HOLD** (with `:25` now carrying B8-1's known-incomplete marker, as
the roadmap's A3 record predicts — expected state, not drift).

### F1 — `skills/vlt-dispatch/references/relay.md`: the fourth shape

**Current state:** `:7` "Every relay declares a **`shape`** — `handoff`, `ask`, or
`answer` (The three shapes, below)"; `:17-27` "### The three shapes" enumerates the three
and defines `ref` and backward compat; `:31` inputs/validation requires `ref` "for `ask`
and `answer`"; `:38-48` the idempotency key `(handoff-path | ref, to-slug, principal)` and
ladder; `:52` "An `ask`/`answer` needs no lifecycle rule beyond its `ref` lifetime";
`:56-78` write formats (header carries the shape when not `handoff`; `:78` "a `handoff` or
`answer` carries a single pointer; a **batched `ask`** may carry several"); `:82-94`
report examples; `:104-113` Verify.

**The change:**
- `:7` and the `:17` heading: four shapes — `handoff`, `ask`, `answer`, `deliver`.
- Add the `deliver` bullet after `answer` (`:23`): *`deliver`* — **no path required**
  (path optional, same clause as `answer`: cite durable artifacts as `[[wikilinks]]` —
  payload, never the key); **`ref` required**. An **unsolicited delivery whose payload is
  written inline**: the gist carries the delivery; nothing was asked. Publisher-chosen
  `ref`, per disposition 6.
- Generalize `:23`'s wikilink sentence to a shape-general line under the `ref` paragraph
  (`:25`): a `[[wikilink]]` in any shape's pointer is payload, never the key — the key
  check never resolves a wikilink **except** a key-path link under the handoff zone
  (disposition 4's rule, stated here once; `ledger.md` renders it).
- `:27` Backward compatibility gains the proto-`deliver` sentence (disposition 3): a
  shape-annotated **pathless** pointer written before `deliver` existed is proto-`deliver`
  traffic — tolerated as written, drained normally, exempt from the key check, reported
  as a denominated count. (Single home for the lane's definition; `ledger.md:26` renders
  the count.)
- `:31` inputs: `ref` required "for `ask`, `answer`, and `deliver`"; path optional for
  `answer` and `deliver`.
- `:38-48` idempotency: the per-shape key sentence adds `deliver` keys on its **`ref`**;
  ladder unchanged.
- `:52`: "An `ask`/`answer`/`deliver` needs no lifecycle rule beyond its `ref` lifetime…"
- `:56-68` write formats: header form `(deliver: <ref>)`, one example block mirroring the
  ask example; `:78`: "a `handoff`, `answer`, or `deliver` carries a single pointer; a
  batched `ask` may carry several".
- `:82-94` Report: one `deliver` example ("Relayed a delivery to **X** (`deliver:
  {slug}`): …" — placeholder vocabulary, no vault-local content); `:104-113` Verify: the
  key-resolution line reads "a path on disk (`handoff`), or a `ref` in the header
  (`ask`/`answer`/`deliver`)".

**Why:** closes the unsolicited×pathless cell; A8-2's core gap.

**Per-site out-of-scope:** the publish-side reflex paragraph (`:11-15`) is untouched —
the reflex fires on handoff-doc writes and spec bumps; a `deliver` is fired by the
publishing partner directly, no new reflex is legislated (the field already does this).

### F2 — `skills/vlt-dispatch/references/ledger.md`: the check catches up (marker discharge)

**Current state:** `:23` key resolution names "`(ask: <ref>)` / `(answer: <ref>)`"; `:25`
the findings bullet carries the legal response *"the publishing partner re-fires the relay
correctly keyed; the recipient checks the malformed line off as superseded"* **plus
B8-1's known-incomplete-pending-B8-2 marker** (the italic parenthetical, F2 of B8-1's
brief); `:26` the legacy line: "un-annotated **pathless** pointers … denominated count …
'N legacy unkeyed pointers (pre-shape)'".

**The change:**
- `:23`: add `(deliver: <ref>)` to the key-resolution forms.
- `:25`: **remove the known-incomplete marker entirely** (B8-1's brief names this exact
  discharge) and rewrite the legal-response sentence to cover the class: for an
  unsolicited delivery mis-keyed as an annotated `handoff`, the correct re-fire **now
  exists** — re-fire as `deliver` with a publisher-chosen `ref` — so the single response
  sentence ("the publishing partner re-fires the relay correctly keyed; the recipient
  checks the malformed line off as superseded") becomes true for every finding the check
  renders. Keep it one line (B8-1's one-line-per-check cap; this stays the check's single
  R3 seat — the walk denominator of B8-1's acceptance check (1) is unchanged at 1 marker
  in this file).
- `:26`: the legacy line gains, in its own paragraph, disposition 4's definitions (unit =
  pointer line; pathless = no key-path under `_agent/handoffs/`/`_agent/specs/`; other
  wikilinks are payload, never paths) and the second denominated lane rendered beside the
  first: "N proto-`deliver` pointers (pre-shape)" per `relay.md`'s Backward-compatibility
  home — zero renders as the denominated zero.
- Verify section (`:44`): the legacy-count agreement line now names both denominated
  lanes.

**Why:** discharges B8-1's marker (A3's preferred same-release path); performs R3 for the
class; closes evidence debt 3 where it lives.

### F3 — `skills/vlt-dispatch/SKILL.md`: enumeration sites (sweep hits)

**Current state:** `:4` (description: "a handoff doc, or a doc-less ask/answer"), `:14`
("a doc-less `ask`/`answer`; the shape facet"), `:22` ("the **pointer's key** for `relay`
— the handoff-doc path, or the `ask`/`answer` `ref`"), `:62` ("plus `shape`/`ref` where
the payload is an ask or answer").

**The change:** each widens to include `deliver` — e.g. "a doc-less ask/answer/deliver",
"the `ask`/`answer`/`deliver` `ref`", "where the payload is an ask, answer, or delivery".
No mechanics restated — pointers stay pointers.

### F4 — `skills/vlt-dispatch/references/daily.md:60`: the seeded record header

**Current state:** the dispatch.md file-header template reads "…`relay` appends
pre-addressed partner→partner pointers (a handoff doc, or a doc-less ask/answer)…".

**The change:** "(a handoff doc, or a doc-less ask/answer/deliver)". Existing vaults keep
their already-seeded header — prose only, nothing migrates.

### F5 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:242` (grounding addition — sweep widened)

**Current state:** the relay-when-done bullet ends: "Relay also carries **doc-less
`ask`/`answer` traffic** — an addressed question and its closing answer, the address
rule's rail (`{conventions}/frontmatter.md`); shapes, keys, and validation are owned by
`vlt-dispatch`'s `relay` mode, not restated here."

**The change:** widen the clause: "doc-less `ask`/`answer`/`deliver` traffic — an
addressed question, its closing answer, or an unsolicited delivery…". **Grounding
addition:** A5's sweep scope was `vlt-dispatch/` outside `relay.md`; this site (and F6)
sit outside `vlt-dispatch/` and would ship stale the day `deliver` lands — the B7-8
stale-prose class. In scope beyond the letter; superseding note in the roadmap. The
operating contract is deliberately not handshaked (CLAUDE.md) — prose reconciliation, no
bump. `frontmatter.md:222`'s address rule is **checked and untouched**: it names shape
`ask` for its own routing and defers the shape set to relay's home ("relay mode owns the
shapes") — it does not enumerate, so it does not drift.

### F6 — `skills/vlt-setup/assets/module-help.csv`, row 11 (`vlt-dispatch`) (grounding addition)

**Current state:** the description reads "…`relay` appends a pre-addressed
partner→partner pointer — a handoff doc, or a doc-less ask/answer (keyed idempotency: doc
path or `ref`; …)".

**The change:** "…a handoff doc, or a doc-less ask/answer/deliver (keyed idempotency: doc
path or `ref`; …)". Keep the field fully quoted (CLAUDE.md CSV rule); header untouched.

### The shape-enumeration sweep — per-hit disposition table (A5)

Corpus: `grep -rn` over `skills/` for `doc-less`, `three shapes`, `(ask:`, `(answer:`,
shape-set enumerations. Hits and dispositions:

| Site | Hit | Disposition |
|---|---|---|
| `vlt-dispatch/SKILL.md:4,14,22,62` | ask/answer enumerations | **F3 — edit** |
| `vlt-dispatch/references/daily.md:60` | seeded-header enumeration | **F4 — edit** |
| `vlt-dispatch/references/ledger.md:23,25,26` | key forms, response, legacy | **F2 — edit** |
| `vlt-dispatch/references/consult.md` | `answer` as consult's return-union member (`:48`) | **no edit** — different vocabulary (typed return, not a relay shape) |
| `vault-operating-contract.md:242` | doc-less ask/answer clause | **F5 — edit** (grounding addition) |
| `module-help.csv` row 11 | description enumeration | **F6 — edit** (grounding addition) |
| `frontmatter.md:222` (address rule) | names shape `ask`, defers the set | **no edit** — does not enumerate |
| `skills/reports/**`, `inbox/**` | historical/dev artifacts | **no edit** — gitignored, not shipped surface |

## Registration

`module-help.csv` row 11's description is refreshed (F6) — no new row, canonical 13-col
header untouched, free-text fields stay quoted. **No convention `version:` moves** (relay
mechanics are not a handshaked convention; `frontmatter.md` is untouched at @7) — no
consumer walk, no re-ack.

## Out of scope (dispositioned)

- **Batched `answer`/`deliver` header forms** (`(answer, batched — refs: …)`, observed in
  vlt-core traffic 2026-08-17, post-filing): not part of A8-2's seven, not legislated
  here — `relay.md:78`'s single-pointer rule for `handoff`/`answer`/`deliver` stands. If
  the field keeps producing batched answers, that is a fresh filing (the through-line's
  test, applied honestly to this build's own boundary).
- **A multi-recipient/broadcast shape** (the `(bell declaration)` block): reasoned out at
  the grid — N single-recipient acts; no combined-header shape. Re-raise only via filing.
- **A publish-side `deliver` reflex** (auto-fire rule mirroring relay-when-done):
  rejected-because the field already fires deliveries deliberately; a reflex needs a
  triggering write event and inline deliveries have none.
- **Retro-annotation of the seven drained lines** (option 4's mechanism): not needed —
  disposition 3 resolves them read-side with zero writes; the no-history-rewrite posture
  stays maximally intact.
- **The legacy lanes' eventual draining/decay**: B8-5's territory (the decay arc build);
  this build only makes their counts reproducible.
- **`vlt-lint` involvement**: pointer integrity remains `ledger`'s check (cross-filing
  ruling 4's lint-scope split is not touched).

## Verification (unit, at rest)

- **Enumeration agreement greps:** `grep -rn "doc-less" skills/` — every hit names
  `deliver`; `grep -rn "three shapes" skills/vlt-dispatch/` → 0; `grep -n
  "Known-incomplete\|pending the delivery-shape" skills/vlt-dispatch/references/ledger.md`
  → 0 (marker discharged); `grep -c "deliver" skills/vlt-dispatch/references/relay.md` >
  0 at every F1 subsection (shapes, inputs, key, format, verify).
- **Fixture run (evidence debt 3's reproducibility claim):** build a temp fixture
  `dispatch.md` reproducing the field's mixed forms (an un-annotated doc'd handoff; an
  un-annotated pathless pre-shape line; a `(handoff, ref:)` proto-`deliver` line; a
  `(handoff)` no-ref no-path line; an `(ask: ref)` line; a `(deliver: ref)` line; a
  payload-wikilink-only line) and hand-execute `ledger`'s defined counts: findings,
  legacy denominator, proto-`deliver` denominator. Two independent applications of the
  written rules must produce identical counts — the property the filing's 37-vs-2-vs-18
  proved missing.
- **Handshake bipartite re-check:** no `version:` moved, no `consumers:`/structure-map
  change — the check of record is `package-lint` **Group E**, run in the packaging lint
  below; expected no-op.
- **Packaging lint:** mid-arc `uv run tools/package-lint.py` A/B/C/E — clean.
- **Fixture extension (R2): not applicable** — no release-gate check added or changed.
- **Legal response (R3): substantive** — this build changes a finding class (the
  inline-delivery class dissolves into the re-fire-as-`deliver` response) and adds a
  denominated lane (a count, not a finding class — a denominated report line needs no
  legal response beyond its own reproducibility). Both stated at the check's single home
  (`ledger.md`, F2), same build.
- **Enumeration widening (R4): not applicable** — this build adds no file to any class a
  vital or manifest enumerates (it adds a *shape*, and the shape enumerations it widens
  are exactly the F1–F6 sweep). Per A13, B8-2 creates no new accumulating file — the
  `deliver` traffic lands in the existing `_agent/dispatch.md`, whose decay contract is
  B8-5's.
- **Scrub:** worked examples in F1's report/format additions use placeholder vocabulary
  and `{slug}`-style paths — no vault names, partner names, or vault-local artifact
  paths.
- **No `.decision-log.md` left in the working tree; one commit for the build.**

*(Not the release build — the 0.11.0 version bumps ride the arc's release build; this
brief's `status:` is rewritten to a BUILT record with numbered deviations by the builder.)*

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** `relay.md` defines exactly four shapes with `deliver` `ref`-keyed;
   every enumeration site in the sweep table (SKILL.md ×4, daily.md seeded header,
   ledger.md key forms, contract `:242`, module-help.csv row 11) names `deliver`; the
   `doc-less`-without-`deliver` grep is zero across `skills/`.
2. **[ship-verifiable]** `ledger.md`'s known-incomplete-pending-B8-2 marker is gone (grep
   zero) and the pointer-integrity legal-response sentence covers every finding the check
   renders, one line, the file's single R3 seat — B8-1's acceptance (2) terminal state
   "discharged by B8-2" is thereby the one exercised, and B8-1's walk denominator (1
   marker-bearing seat in `ledger.md`) still holds.
3. **[ship-verifiable]** the legacy paragraph defines unit (pointer line) + the
   key-path/wikilink rule + the proto-`deliver` denominated lane, and the fixture run's
   two independent count applications agree — the denominator is reproducible by a second
   reader at rest.
4. **[field-contingent — vlt-core]** the first post-upgrade `vlt-dispatch ledger` run
   reports **zero** pointer-integrity findings for the inline-delivery class, with the
   seven rendering under the denominated proto-`deliver` count (7 at the pinned commit;
   the number may grow if the field produced more before upgrading) — A5's named
   acceptance ("zero or denominated-legacy"), and the count matches a by-hand application
   of the shipped rules.
5. **[field-contingent — vlt-core]** the first unsolicited pathless delivery after the
   upgrade is fired as `deliver` with a publisher-chosen `ref` (the publish side adopts
   the legal form unprompted — vlt-core produces this event routinely; seven in one
   evening at the pin).
