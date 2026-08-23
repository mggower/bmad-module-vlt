---
title: 'Build #B7-5 — relay & address (the ask/answer shapes and the address rule''s mechanism: the rails the frontmatter@6 rules already await)'
status: >
  BUILT 2026-08-15. All 9 F-sites landed. Deviations: (1) EXPANDED — the operating-contract
  edit tripped package-lint C6 (rule-card sha binding, a consequence the brief did not list):
  vault-rule-card.md re-derived (new derived_from sha256 c32b5cb8b704…, derived 2026-08-15,
  last_updated bumped; no act-blocking rule added — the one content touch is the backlog map
  row gaining "by address (backlog or relay)"). (2) EXPANDED — a third key-definition
  restatement the brief missed, the dispatch.md file-header template at
  vlt-dispatch/references/daily.md:58 ("handoff-doc path for relay"), aligned to the
  pointer's-key vocabulary in the same pass (cross-file agreement; spec.md:63's "doc-path
  idempotency" verified still correct — specs ride the handoff shape). (3) Minor — the
  {backlog} bound reads "## Open item count and its last 5 entries" at the contract vs
  "## Open count and its last 5 entries" at the four partner/template sites, each verbatim
  per the brief's own F4/F8 texts; the grep criterion ("last 5 entries in {backlog}") matches
  identically at all five sites. Verification: (1) shape/key greps — relay.md single home,
  SKILL.md :4/:14/:22/:54 pointer-only, ledger.md same vocabulary, PASS; (2) single-home
  reflex grep — canonical address-aware sentence only in the contract's backlog section, four
  F5 sites + two F7 op-skill sites are pointers, no guard/limit text outside
  frontmatter.md:222, PASS; (3) bound grep — five sites agree, PASS; (4) frontmatter.md diff
  = the one trailer line, version: 6 unchanged, Group E PASS (bipartite-consistent); (5)
  uv run tools/package-lint.py --expect-version 0.9.1 → "package-lint: A/B/C/E PASS, D PASS —
  vlt 0.9.1", exit 0, C7 router budget held (11,610 < 14,000 bytes); (6) R2 non-trigger shown:
  tools/ diff empty, test-package-lint 20/20 green, CASE_FLOOR 20; (7) temp-fixture
  walkthrough (scratchpad _agent/dispatch.md, five pointers a–e): (a) un-annotated with real
  temp path resolves as handoff, (b) ask: source-provenance resolves by ref, (c) answer
  reusing (b)'s ref with different to-slug resolves and does not collide, (d) un-annotated
  pathless counted as "1 legacy unkeyed pointers (pre-shape)" — no finding, (e) annotated
  (ask) with no ref = the one finding; fixture deleted; (8) scrub grep clean — placeholder
  vocabulary only ({question-slug}, source-provenance); (9) no .decision-log.md on disk.
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-14-180949-relay-requires-a-path-for-traffic-that-has-no-doc.md (A7-11: pathless relay traffic has no legal shape; a pathless pointer is unkeyed, so the #1 spam guard is silently inert)'
  - 'inbox/2026-08-14-181000-knowledge-gap-addressed-to-a-rail-with-no-recipient.md (A7-12 mechanism half: the address rule''s rail — shape `ask`; the single-home reflex sentence; the severable unbounded-`{backlog}` Beat-2 read)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: >
  roadmap §Ideation rulings (2026-08-15): grouping row B7-5 (relay & address — narrow-fix
  MECHANISM build, A7-11+A7-12 bound); framing ruling 1 (A7-11/A7-12 are narrow fixes the module
  owns, NOT the B7-4 seam); the single-home reflex ruling (the contract owns the file-it-to-
  `{backlog}` sentence, four pointers, template pointer load-bearing); the frontmatter bump plan
  (B7-3 shipped the rules; mechanism builds cite, never re-bump — A1/A6 reopen is a 6→7 walk);
  brief-time designations for A7-11 and A7-12; post-ideation amendments A5 (the
  no-backfill-vs-receiver-check conflict is this brief''s to reconcile) and A8 (guard 2 scoped to
  the ship-time addressee model); standing rules R1 (interim postures) and R2 (fixture rides any
  gate-check change).
risk: >
  low-moderate — no convention version bump (frontmatter stays @6; the one frontmatter.md edit is
  the self-obsoleting interim-posture trailer, a prose update, no rule change, no consumer walk),
  but the build touches the operating contract (not handshaked; single-home + pointers is its
  mechanism), two op skills, three partner skills, the mint template, and the dispatch router +
  two mode references.
---

# Build #B7-5 — relay & address

## Intent

B7-3 (`313ae37`) shipped `frontmatter@6` carrying **the address rule** — *a noticed gap goes to
`{backlog}` only when the filing partner does not know whose turn it is; when it does, the gap is
relayed to that partner (`vlt-dispatch relay`, shape `ask`)* — with its three guards and its limit
paragraph, closed by an R1 interim posture: *"the `ask` shape and the relay-side machinery ship
with the relay build; until then this rule is declared."* **This is the relay build.** It ships the
mechanism those rules await, in two halves:

- **A7-11** — relay declares a **`shape`** (`handoff` / `ask` / `answer`) and a **`ref`** key; the
  idempotency key becomes `(handoff-path | ref, to-slug)`, so the traffic the field proved real
  (a question with no doc to point at; the answer closing it) is legal **and keyed** — today a
  pathless pointer has nothing to grep on, so the spec's own #1 failure mode (spam) is silently
  unguarded for that traffic. Plus the receiver-side check the filing offers: *every relay pointer
  resolves a key.*
- **A7-12 (mechanism half)** — the operating contract takes single-home ownership of the
  file-it-to-`{backlog}` reflex (four pointer sites: 3 partner skills + `vlt-mint`'s template, the
  template pointer the load-bearing one), and the severable Beat-2 fix lands: `{backlog}` is the
  one unbounded read in the contract's orient list, and the address rule is exactly what makes
  bounding it legal.

Scope discipline, per framing ruling 1: **these are narrow fixes to mechanisms the module owns** —
a missing idempotency key on an existing rail, an address rule's rail, a missing read bound.
Nothing here designs a receiving surface, a routing profile, or an addressee model; that is
B7-4's territory and this build does not enter it. All rejected alternatives in the parent filings
are settled — in particular the consult-adjacent **async mode** (capture grounded the relay facet
as the shape consistent with shipped design: `consult.md:7` already models consult as *a relay
whose drain happens immediately*, and `SKILL.md:18` makes all modes one machine) — **do not
re-litigate.**

**Provenance note (the A7-13 input, honored):** both filings' fixes were reviewed in the field by
a *substituted* council — exactly the provenance gap B7-7 exists to close. This brief therefore
**re-derives** the design from the shipped spec (the mode-appropriate-key principle at
`vlt-dispatch/SKILL.md:22`, the named failure modes in `relay.md`, the one-machine model) rather
than inheriting the vlt-core edits on authority; each carried property below is kept because it
survives that re-derivation, and vlt-core's applied text is treated as evidence, not as the spec.

## Brief-time dispositions

1. **The A5 conflict — resolved by a legacy grandfather (the receiver check grandfathers
   un-annotated pathless pointers).** Amendment A5 binds this brief to reconcile: *no backfill*
   ("an un-annotated header reads as `handoff`") vs the receiver check ("every relay pointer
   resolves a key") firing on the 13 existing pathless pointers the day it ships. Ruling:
   **backward-compat is refined, not given up.** An un-annotated header **with a path** reads as
   `handoff` (the 27). An un-annotated header **without a path** reads as **legacy pre-shape
   traffic** — tolerated as written, drained normally, exempt from the key check and from the
   idempotency guarantee (which it never had; the exemption states an existing fact rather than
   creating one). The receiver check reports legacy traffic as a **denominated count line**
   (ledger's existing honest-reporting idiom — "N legacy unkeyed pointers (pre-shape)"), never as
   findings; a **finding** is a *shape-annotated* pointer that fails its shape's key requirement
   (an `ask`/`answer` with no `ref`; an annotated `handoff` with no path). Nothing must be edited
   in any existing record (**no backfill kept**), the check still catches the failure that cannot
   be seen by reading (**the check kept**), and `handoff`'s path requirement holds for all
   annotated and all new traffic (**the contract kept**). Rejected: editing the 13 (backfill —
   violates the filing's kept property and the two-writer discipline); tolerating pathless
   `handoff` generally (would re-open the unkeyed hole for new traffic, the more serious half).
2. **A8 — guard 2's scope is stated against the single-addressee model, and it ships.** Guard 2
   (*self-addressed work is not a relay*) is written against today's model: one human principal,
   partners identified by slug — **"self" means the same partner slug.** This build embodies it
   mechanically with a `from-slug ≠ to-slug` validation in relay mode, mirroring
   `consult.md:22`'s existing "a partner does not consult itself" check (F1). **What changes if
   B7-4 later widens the addressee model:** under any roster/multi-principal model,
   *self-addressed* must be read as *same partner **and** same principal* — the same partner
   acting for a different principal is a legal relay, and the slug-equality check must widen to
   pair-equality in the same build that widens the model. Stated here per A8 (an R1 application)
   so the widening is a named consequence, not a silent behavior change. B7-4 precedes B7-5 in
   ship order but may slip; this build is correct in either order because it binds to the model
   *in force*, by name.
3. **The receiver-side check's home is `ledger` mode, and R2 does not fire.** The check reads the
   record — that is `ledger`'s definition ("grep the *whole* record", `ledger.md:7`) — and ledger
   already carries the integrity/vitals surface (`ledger.md:23-28`) and the honest-reporting
   idiom the legacy line needs. It is a **vault-side runtime check, not a release-gate check**:
   `tools/package-lint.py` gains and changes nothing, so R2's fixture obligation does not trigger
   (verified in §Verification — E4 inventory unchanged, `CASE_FLOOR` stays 20). Rejected:
   `vlt-lint` (the record is agent-zone traffic, not wiki content; lint's surface is pages and
   conventions) and `package-lint` (the record does not exist at the factory).
4. **The check's finding names its legal response (R3 honored ahead of its Arc-8 build).** An
   unresolved-key finding's stated response: **the publishing partner re-fires the relay
   correctly keyed; the recipient checks the malformed line off as superseded** (its own tagged
   line — two-writer discipline holds). The legacy count line needs no response — it is
   denominated context, not a finding. R3 is only *declared* this arc, but shipping a new finding
   class without a stated legal response would be Strand 1 re-enacted inside the build fixing it.
5. **The `frontmatter.md:222` interim-posture trailer is updated in place — prose, no bump, no
   walk; A1's reopen is NOT invoked.** The trailer is self-obsoleting by its own words ("ship with
   the relay build"), and B7-3 and B7-5 ship in the same release (v0.10.0), so no vault ever
   inhabits the interim window — but leaving the sentence would be shipped prose asserting a
   mechanism doesn't exist after it does: Strand 3. The replacement (F6) changes **no rule text**
   — the rule, guards, and limit paragraph stand verbatim — so per CLAUDE.md this is a prose
   clarification: **`version: 6` holds, no consumer re-ack.** A1's reopen path exists for base
   *rule/field* changes; this build needs none.
6. **The Beat-2 `{backlog}` bound: the `## Open` item count plus its last 5 entries.** Mirrors the
   contract's own `{log}` bound (last 5, `vault-operating-contract.md:169`) and the denominated
   honest-reporting idiom (a count is cheap; a silent truncation is not). The justification the
   contract states: under the address rule the backlog holds **the unassignable**, and addressed
   work reaches a partner through its **dispatch slice** (already a Beat-2 read) — so the backlog
   scan no longer needs to scale with vault age to be safe. Field data agrees: the rail with a
   drain was already winning off-spec. The partners' "especially `<kind>` items" emphasis
   survives inside the bound.
7. **Grounding addition — the three shipped partner Beat-2 bullets join the bound.** The ruling
   names `vault-operating-contract.md:169` and `partner-agent-template.md:40`; re-grounding shows
   the identical unbounded phrase ("the open items in `{backlog}`") restated at
   `vlt-agent-creative/SKILL.md:25`, `vlt-agent-librarian/SKILL.md:25`,
   `vlt-agent-researcher/SKILL.md:25`. Leaving them unbounded while the contract bounds the read
   would be a contradiction across the single-home seam; all three align in the same pass (F8).
   In scope beyond the filings' letter as an EXPANDED site (grounding-at-brief-time).
8. **The batched-`ask` widening ships, and carries the consolidation observation.** Relay.md:48's
   "one relay = one pointer" is amended to admit a batched `ask` (one publisher, several
   questions, **one recipient, one moment**; each pointer its own `ref`) — carried as proposed,
   re-derived: the constraint being preserved is *one pre-addressed act per block*, and a batched
   ask is one act. One sentence records the pattern the field surfaced (*a backlog accumulates
   items one at a time and never sees that nine of them are one act; the triage onto an addressed
   rail is where that becomes visible*) — an observation, not a rule.
9. **`answer`'s optional path cites wiki pages as `[[wikilinks]]` — no traversal claim.** The
   `answer` shape's optional artifact reference is a wikilink (the durable artifact is typically
   a wiki page), consistent with `frontmatter@6` rule 4's traverse-vs-verify split shipped by
   B7-3. The key for an `answer` is always its `ref` (required, = the originating ask's); the
   wikilink is payload, never the key — so the check never needs to resolve a wikilink.

## F-sites

### F1 — `skills/vlt-dispatch/references/relay.md` (the shape facet, the key, the guards' rail)

**Current state (all HOLD at HEAD):** `:7` mode intro takes `(slug, gist, handoff-path)` as the
one payload; `:11-13` the relay-when-done reflex fires `relay (to-slug, gist, handoff-path)`;
`:15` the human debugging form; `:19` *Inputs and validation* — **`handoff-path` required,
unconditional**; `:25-33` the idempotency rule **keyed on `(handoff-doc-path, recipient-slug)`**,
with `:30` naming #1 spam as what it guards; `:35-37` the stable-path lifecycle note; `:41-48` the
block format (`relay: <from> → <to>` header as the mode signal) and `:48` "One relay = one
pointer"; `:52-56` the report; `:66-74` Verify (`:71` the idempotency confirmation).

**The change** — relay.md remains the **single home of the relay contract**; it gains the shape
facet as a section of its own, and every existing site becomes shape-aware:

- **A "three shapes" section** (after *Who fires it*): relay declares a **`shape`** —
  - **`handoff`** — `handoff-path` **required**. The original contract, unchanged; the
    relay-when-done reflex and the spec `consumers:` fan-out both fire this shape.
  - **`ask`** — **no path** (the doc does not exist yet — that is the ask); **`ref` required**.
    The gist carries the question, why it matters, and what would close it. This is the shape the
    address rule (`{conventions}/frontmatter.md`, *The address rule*) routes onto this rail.
  - **`answer`** — path **optional** (cite the durable artifact, typically a wiki page, as a
    `[[wikilink]]`); **`ref` required and it must be the originating `ask`'s `ref`**.
  - **`ref`** is a short kebab slug naming the question, chosen by the ask's publisher and reused
    verbatim by the answer. It is not a path and points at nothing — **it exists to key the
    pointer.**
  - **Backward compatibility (no backfill):** an un-annotated header **with a path** reads as
    `handoff`; an un-annotated header **without a path** is **legacy pre-shape traffic** —
    drained normally, exempt from the key check and the idempotency guarantee it never had
    (disposition 1). No existing record is ever edited to conform.
- **`:19` Inputs and validation** becomes per-shape: `to-slug` + `gist` always required;
  `handoff-path` required for `handoff`, forbidden-to-be-assumed for `ask`, optional for
  `answer`; `ref` required for `ask`/`answer`. Add the guard-2 embodiment: **`from-slug ≠
  to-slug`** — a partner does not relay to itself (mirrors `consult.md:22`; scope per
  disposition 2, stated against the single-addressee model in force).
- **`:25-33` idempotency** — the key becomes **`(handoff-path | ref, to-slug)`**: a `handoff`
  keys on its path exactly as today; an `ask`/`answer` keys on its `ref`. State the two kept
  properties: an `answer` reusing its `ask`'s `ref` **does not collide** (opposite directions —
  different `to-slug`), and the open/checked/no-op ladder at `:29-31` applies per key unchanged.
  Add the *why `ref` is required* note: an unkeyed pointer disables the `:30` spam guard
  invisibly — the guard's absence is indistinguishable from the guard passing.
- **`:35-37` lifecycle note** — scope it to the `handoff` shape (stable doc path); one sentence
  scoping `ask`/`answer` to their `ref` lifetime (a `ref` is stable by construction — it is never
  revised, only answered).
- **`:41-48` block format** — the header carries the shape when not `handoff`:
  `## [YYYY-MM-DD HH:MM] relay: <from> → <to> (ask: <ref>) — N items` (the field-proven form);
  `answer` analogous (`(answer: <ref>)`). `:48` "One relay = one pointer" amended per
  disposition 8 (batched `ask`: one publisher, several questions, one recipient, one moment,
  each pointer its own `ref`) plus the one-sentence consolidation observation.
- **`:52-56` report** — add one `ask` example alongside the existing spec example (placeholder
  vocabulary only — e.g. a researcher-bound question slug; **no vault-local content**).
- **`:66-74` Verify** — extend `:71`: the idempotency confirmation checks the *shape's* key; add
  "every pointer written this run resolves a key (path on disk, or `ref` in the header)".

**Why:** A7-11 both halves — the spec is narrower than legitimate traffic, and the pathless third
of it is unkeyed, so the guard the spec itself names is silently inert.

**Out of scope here:** no new mode (settled at capture, confirmed by ruling — the facet, not a
fifth mode); no `daily`/`consult` changes (consult blocks carry their own `consult:` header and
are pre-checked traffic — the key rule never applied to them).

### F2 — `skills/vlt-dispatch/SKILL.md` (the router: second key-definition site, per single-home)

**Current state (all HOLD):** `:4` description — "`relay` appends a pre-addressed
partner→partner handoff pointer"; `:14` relay bullet — "appends the pointer with **doc-path
idempotency**"; `:22` — "a mode-appropriate idempotency key makes re-runs safe (a per-source
**watermark** for `daily`, the **handoff-doc path** for `relay`)" — the second key-definition
site the ruling names; `:54` mode dispatch — "a partner-supplied `(to-slug, gist, handoff-path)`
→ `relay`". Byte size 11,318 vs `ROUTER_BUDGETS` 14,000 (`tools/package-lint.py:246`).

**The change (minimal — the router points, relay.md owns):** `:22`'s parenthetical becomes "the
**pointer's key** for `relay` — the handoff-doc path, or the `ask`/`answer` `ref`; the key rule's
single home is `references/relay.md`". `:14` "doc-path idempotency" → "keyed idempotency (see the
mode reference)" and the bullet's "a durable handoff doc is waiting" gains "— or a doc-less
`ask`/`answer` (the shape facet; `references/relay.md`)". `:54`'s triple gains "(plus `shape`/
`ref` where the payload is an ask or answer)". `:4` description: "…handoff pointer" → "…pointer
(a handoff doc, or a doc-less ask/answer)". Keep the router lean — mechanics stay in relay.md;
budget headroom ~2.7KB is ample but the builder verifies C7 after editing.

**Why:** the ruling's explicit second site — "change the key in `references/relay.md` alone and
the router's own overview carries the old one"; single-home says one points at the other.

### F3 — `skills/vlt-dispatch/references/ledger.md` (the receiver-side check)

**Current state (HOLD):** `:7` ledger greps the whole record; `:11-17` the board build; `:23-28`
*Tripped wires & vitals* (the denominated-zero idiom at `:27`); `:31-37` Verify.

**The change:** after the board build, a **pointer-integrity line**: for every pointer in a
`relay:` block, resolve its key — a `handoff-path` that exists on disk, or a `ref` present in the
header. Render: **findings** (shape-annotated pointers failing their shape's key — with the legal
response per disposition 4: publisher re-fires keyed, recipient checks the malformed line off as
superseded) and the **denominated legacy line** ("N legacy unkeyed pointers (pre-shape)" — count,
never findings; zero renders as the denominated zero, matching `:27`'s idiom). Scope: `relay:`
blocks only (a `consult:` block is pre-checked traffic; a `daily` pointer keys on its watermark).
Verify gains: the integrity line agrees with a fresh grep of `relay:` blocks.

**Why:** A7-11's offered check — "the failure that cannot be seen by reading" needs a bell on the
read side; ledger is the read of the record (disposition 3).

### F4 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` (Beat 2 bound + hand-offs pointer + reflex ownership)

**Current state (all HOLD):** `:169` Beat 2 — every read bounded (**`{index}` section headings**,
**last 5** `{log}`, `## Thread` **only**) with the stated reason ("The bounds are what keep a
mature vault's orient from scaling with its age") — **except** "the **open items** in `{backlog}`",
the one unbounded, monotonically-growing read; `:171` the dispatch-slice drain; `:238` the
relay-when-done reflex bullet (fires `relay (to-slug, gist, handoff-path)`); `:239` stable-path
bullet; `:242-244` *The backlog — evolution intake* — already carries the file-freely reflex in
substance ("any partner files to it autonomously … and says so in-flow").

**The change (three edits):**

1. **`:169`** — the `{backlog}` read becomes bounded: "the `## Open` **item count and its last 5
   entries** in `{backlog}` (what the vault wants to become — the backlog holds the
   *unassignable*; work addressed to this partner arrives through its dispatch slice, below)".
   Same-sentence justification style as the existing bounds (disposition 6).
2. **`:238`** — one pointing clause appended to the reflex bullet: relay also carries **doc-less
   `ask`/`answer` traffic** (an addressed question and its closing answer — the address rule's
   rail, `{conventions}/frontmatter.md`); shapes, keys, and validation are owned by
   `vlt-dispatch`'s relay mode, not restated here. (Without this the contract's model — every
   relay pairs with a doc — contradicts the shipped shapes.)
3. **`:242-244`** — the backlog section becomes the **single home of the reflex sentence**, now
   address-aware: the canonical form is "file it to `{backlog}` **when no partner is its address**
   and say so in-flow; an addressed gap is **relayed** instead (`vlt-dispatch relay`, shape
   `ask`) — the address rule and its guards live in `{conventions}/frontmatter.md`" (points at
   the rule; never restates the guards or the limit paragraph — frontmatter.md:222 owns them).
   The capture-is-cheapest sentence and file-freely/act-deliberately posture stand.

**Why:** A7-12's severable Beat-2 finding (the one unbounded orient read); the single-home reflex
ruling ("THE CONTRACT OWNS IT, FOUR POINTERS"); coherence of the contract's hand-off model with
the shipped shapes.

**Out of scope here:** the contract is deliberately not handshaked — no version machinery; no
restatement of the address rule's text (frontmatter.md owns it).

### F5 — the four pointer sites (3 partner skills + the mint template)

**Current state (all HOLD):** the reflex boilerplate at `vlt-agent-creative/SKILL.md:48`
("file it to `{backlog}` and say so in-flow", `capability-gap`),
`vlt-agent-librarian/SKILL.md:47` (same reflex, `maintenance`, plus the upkeep-noticing framing),
`vlt-agent-researcher/SKILL.md:50` (same, `knowledge-gap`/`capability-gap`), and
`skills/vlt-mint/assets/partner-agent-template.md:63` (the leak into every future minted
partner — the load-bearing pointer per the ruling).

**The change:** each site keeps its persona voice and its kind-vocabulary but becomes a **short
pointer, no restated mechanics**: notice freely, then follow the contract's filing reflex (*The
backlog — evolution intake*) — file to `{backlog}` when the gap has no address, relay (shape
`ask`) when it does; say so in-flow either way. The Researcher's pointer notes that gaps
addressed **to it** arrive via its dispatch slice (the filing's Beat-2 observation — the read
side of the same rule). No site restates the guards, the limit, or the kinds' definitions.

**Why:** the single-home ruling, verbatim — four pointers, template load-bearing ("the only one
that fixes instances that do not exist yet").

### F6 — `skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md:222` (the interim trailer)

**Current state (HOLD — shipped by B7-3 exactly as the roadmap records):** the address rule +
three guards + limit paragraph, closed by "*Interim posture:* the `ask` shape and the relay-side
machinery ship with the relay build; until then this rule is declared — the existing relay form
carries what it can, filing to `{backlog}` remains legal for anything it cannot, and no check
fires on either choice."

**The change:** replace the trailer only (rule, guards, limit stand **verbatim**): the `ask`
shape and its keyed rail exist (`vlt-dispatch`, relay mode); filing to `{backlog}` remains the
correct move exactly where the rule says — when no partner is the address. No `version:` change,
no re-ack (disposition 5).

**Why:** R1's posture did its job and expired with the mechanism; leaving it is Strand 3.

### F7 — `vlt-lint` and `vlt-ingest` (the two op-skill routing sites, moved together)

**Current state (all HOLD):** `vlt-lint/references/fix-and-file.md:29-33` routes **every**
`adjudicable` contradiction to backlog, splitting only `maintenance` vs `knowledge-gap` (`:43`
repeats the split for entity collisions; `:21-27` plain maintenance items; `:45-49` spec
candidates); `vlt-lint/SKILL.md:59` standing rule — "file the `adjudicable` ones to backlog";
`vlt-ingest/SKILL.md:159` — `adjudicable` → "file it to `{backlog}` — the write-side counterpart
of `vlt-lint`'s Step 4"; `vlt-ingest/SKILL.md:129` — the declined-name drain files
`knowledge-gap`/`maintenance` to backlog.

**The change:** both skills gain the **address axis ahead of the kind split**, by pointer to the
address rule: an adjudicable contradiction (or declined-name / entity-collision item) whose
bounded closing act **names another partner's act** (needs an external source → the Researcher)
is **relayed** (shape `ask`, the `ref` naming the question; the `**Filed:**` back-write at
fix-and-file `:35` records the relay instead of a backlog item); the vault's own pages settle it →
`maintenance` to backlog; nobody can say what closes it → `knowledge-gap` to backlog. The
duplicate-filing guards (`:51-53`) extend naturally: an open relay pointer for the same question
counts as "already filed" (the idempotency key makes this checkable). `vlt-lint/SKILL.md:59`
updates to "file **or relay, by address**, per `references/fix-and-file.md`". `vlt-ingest:159`
keeps its counterpart sentence — the two sites move together, as the skill itself demands;
`:129`'s drain gains the same one-clause address gate.

**Why:** A7-12's consumer walk — two shipped skills encode the retired route; the field's own
full lint had already deviated correctly (four adjudicable contradictions relayed, not filed).

**Out of scope here:** no change to what counts as `adjudicable`, to tier rules, or to
single-writer safety; the fan-out workflow `vlt-lint-full.js` is untouched (B7-6's surface).

### F8 — the three partner Beat-2 bullets + template Beat-2 (grounding addition)

**Current state (HOLD; EXPANDED per disposition 7):** `vlt-agent-creative/SKILL.md:25`,
`vlt-agent-librarian/SKILL.md:25`, `vlt-agent-researcher/SKILL.md:25`, and
`partner-agent-template.md:40` each restate "the open items in `{backlog}`" unbounded.

**The change:** all four align to the contract's new bound — "the `## Open` count and its last 5
entries in `{backlog}`" — keeping each persona's "especially `<kind>`" emphasis inside the bound.
The template is the load-bearing instance (`:40`, named by the ruling); the three shipped skills
join per disposition 7.

**Why:** the severable Beat-2 fix is a single-home change; a bound the contract states and the
partners' own bullets contradict is no bound.

### F9 — `skills/vlt-setup/assets/module-help.csv:11` (the dispatch row)

**Current state (HOLD):** the row's description reads "`relay` appends a pre-addressed
partner→partner handoff pointer (doc-path idempotent; …)".

**The change:** "…partner→partner pointer — a handoff doc, or a doc-less ask/answer (keyed
idempotency: doc path or `ref`; …)". Quoted free-text fields, canonical 13-col header untouched
(CLAUDE.md).

**Why:** the help surface would otherwise assert the pre-shape contract; honest surface.

## Registration

**No new skill, no new workflow, no version bump.** `frontmatter` stays `@6` (disposition 5 —
prose trailer only; no rule change ⇒ no consumer walk; the six acks stand). The one registration
surface touched is the existing `module-help.csv` dispatch row (F9). The operating contract is
not handshaked (single-home + pointers, per standing rule). No workflow asset (`.claude/workflows/
*.js`) is touched, so no asset ack is owed and nothing here preempts B7-6's asset-handshake
mechanism.

## Out of scope (dispositioned)

- **The B7-4 seam** (routing profile, designed parameter read, multi-addressee roster, vault-
  writable declarations) — framing ruling 1: A7-11/A7-12 are narrow fixes; the seam is B7-4's.
  Guard 2's multi-principal reading is *stated* (disposition 2), not built.
- **A consult-adjacent async mode** — settled at capture and cited by the ruling: the relay facet
  is the shape consistent with shipped design; a fifth mode buys no new machinery.
- **Backfilling the 13 legacy pointers** (or any vault's record) — the kept no-backfill property;
  the legacy grandfather (disposition 1) makes backfill unnecessary forever.
- **Enforcement of the address rule itself** — the rule stays partner-behavior (`declared`);
  no lint check polices backlog-vs-relay choice. The only new check is the pointer-integrity read
  (F3), which polices the *rail*, not the choice.
- **Relay scheduling/aging alarms** — the limit paragraph is the ruling: relay buys an address
  and a drain, not execution; a stale-slice alarm would invite exactly the misreading the
  paragraph forbids. `ledger` already surfaces oldest-open per partner.
- **The workflow assets** (`vlt-lint-full.js`, `vlt-consult.js`, `vlt-review-council.js`) —
  untouched; first-class-node machinery is B7-6's. (Noted: `vlt-consult.js` parses `args` as a
  JSON string on intake; nothing here changes any workflow invocation.)
- **`daily` / `consult` mode mechanics** — the key rule never applied to them (watermark;
  pre-checked traffic); their references are untouched except nothing.
- **R3's per-check response field in `checks.md`** — Arc 8 builds the retrofit; F3's finding
  states its response inline (disposition 4) without opening the `checks.md` schema early.
- **vlt-core's standing local edits** to `vlt-dispatch`/`vlt-lint`/`vlt-ingest`/the template —
  field state, reconciled by the 0.10.0 upgrade's own-the-apply copy (acceptance check 4), never
  edited from the factory.

## Verification (unit, at rest)

1. **Shape-contract agreement, both key sites:** grep `handoff-path` / `ref` / `shape` across
   `skills/vlt-dispatch/` — relay.md states the per-shape requirements and the
   `(handoff-path | ref, to-slug)` key once; SKILL.md `:14`/`:22`/`:54` point at relay.md and
   restate no per-shape mechanics; ledger.md's check names the same key vocabulary.
2. **Single-home reflex:** grep `file it to` / `{backlog}` across `skills/` — the canonical
   address-aware reflex sentence appears **only** in the operating contract; the four F5 sites +
   F7's two op-skill sites carry pointers (no guard text, no limit text outside
   frontmatter.md:222).
3. **Bound agreement:** grep `open items in` / `last 5` across the contract, three partner
   skills, and the template — the `{backlog}` bound reads identically (count + last 5) at all
   five sites.
4. **Frontmatter discipline:** `frontmatter.md` diff touches only the `:222` trailer; `version: 6`
   unchanged; **`package-lint` Group E** (E1 bipartite, E2 structure map, E3 stray-pin) is the
   check of record that the handshake still closes — six consumers, six `@6` acks. (A hand-written
   `grep "frontmatter@" skills/` is not a substitute and is not the recorded verification.)
5. **Packaging lint:** mid-arc `uv run tools/package-lint.py` **A/B/C/E** passes — in particular
   **C7** router integrity (`vlt-dispatch/SKILL.md` stays under its 14,000-byte budget;
   no orphan/dangling reference tokens after the edits).
6. **R2 non-trigger, shown not assumed:** `tools/package-lint.py` diff is empty;
   `uv run tools/test-package-lint.py` still 20/20 with `CASE_FLOOR` 20 (no gate check added or
   changed ⇒ no fixture case owed; E4 inventory unchanged).
7. **Temp-fixture walkthrough of the check:** against a scratch `_agent/dispatch.md` containing
   (a) a keyed `handoff` pointer with a real temp path, (b) an `ask: <ref>` pointer, (c) an
   `answer: <ref>` pointer reusing (b)'s ref with a different `to-slug`, (d) an un-annotated
   pathless pointer, (e) an annotated `ask` with no ref — walk F3's check by hand: (a)-(c)
   resolve, (c) does not collide with (b), (d) counts as legacy (no finding), (e) is the one
   finding. Record the walkthrough in the build notes.
8. **Scrub:** no vault-local names, paths, or example vocabulary from the filings' vault in any
   changed shipped file; worked examples use placeholder paths/slugs (CLAUDE.md publishing
   rules). The `title:` above passes the same scrub.
9. **Decision-log hygiene:** delete any `.decision-log.md` before the build's single commit.

*(Not the release build — no version-string bumps here; v0.10.0's dual bump and
`--expect-version` gate ride the arc's release build.)*

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** The shape facet is coherent at rest: relay.md carries the three shapes
   with per-shape key requirements and the `(handoff-path | ref, to-slug)` key; both
   key-definition sites agree with relay.md as the single home; the ledger check, the router,
   and the help row use the same vocabulary; `package-lint` A/B/C/E green (C7 budget held) with
   Group E confirming `frontmatter@6` untouched and bipartite-consistent. Dischargeable at rest;
   re-confirmed at the arc's release gate.
2. **[ship-verifiable]** The A5 reconciliation is shipped, not just briefed: relay.md's
   backward-compat text distinguishes un-annotated-with-path (`handoff`) from un-annotated-
   pathless (legacy, exempt, denominated); ledger.md renders legacy as a count line and reserves
   findings for shape-annotated key failures, with the finding's legal response stated at the
   check. Verifiable by reading the two shipped references; the temp-fixture walkthrough
   (verification 7) is the could-have-failed probe of record.
3. **[ship-verifiable]** Single-home landed: the address-aware reflex lives only in the operating
   contract; the four partner-side sites and the two op-skill routing sites are pointers; the
   `{backlog}` Beat-2 bound (count + last 5) reads identically at the contract, three partner
   skills, and the template; frontmatter.md:222's interim trailer is replaced with no rule-text
   change. Dischargeable at rest by the §Verification greps.
4. **[ship-verifiable — next ordinary vlt-core upgrade (0.10.0, owner-run)]** The module's ruled
   relay/address text supersedes vlt-core's previewed local edits cleanly: post-upgrade, the
   vault's existing record parses legally under the shipped rules — a `ledger` run reports the
   pre-shape pathless pointers as the denominated legacy line (no false findings on legacy
   traffic), and keyed `ask`/`answer` pointers written under the local preview resolve their
   keys. Bounded — the upgrade happens anyway; evidence arrives as the owner's pasted ledger
   output + upgrade ledger entry (the factory cannot read vlt-core).
5. **[field-contingent — producing vault: vlt-core only (owner-run; evidence by owner paste)]**
   The drain the mechanism promises: over the window to arc closeout, newly noticed addressed
   gaps travel as keyed `ask` relays rather than accumulating as addressed backlog items, and
   the before/after measures move the right way against the filing's baselines (relay split
   40/27/13; backlog 85→62 open, `knowledge-gap` 33→10 at triage). Graded per the limit
   paragraph: an undrained-but-keyed slice on a rarely-summoned partner is the rail working, not
   failing. If unread by closeout it goes to the watch register, not the gate.
