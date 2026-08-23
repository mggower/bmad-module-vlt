---
title: 'Build #15 — the spec convention (a named home for inter-partner contracts, before the third consumer forks the format)'
status: 'BUILT 2026-07-06 — all six F-sites landed; unit verification + package-lint PASS. Deviations/notes: (1) the faithfulness diff could not run against vlt-core''s minted spec.md — the vault-side mint has NOT happened yet (no _meta/conventions/spec.md or _agent/specs/ in vlt-core); grounding used the design source directly (the 29/30 pressure-test artifact + filing 091001) — when vlt-core mints, it should mint FROM the shipped text so the divergence check self-clears. (2) Additive beyond the brief''s letter: `specs` added to vlt-mint''s and vlt-upgrade''s activation logical-name lists (so their `{specs}` references resolve via the map), dispatch''s locations intro reworded three→four, `proto-spec-retrofit` added to vlt-upgrade''s migrations_run enum, contract last_updated bumped. (3) Pre-existing `health-coach` example slug in vlt-track/SKILL.md:37 noted for build-18''s placeholder rule — not touched here. Hard gate still stands vault-side: no new partner mint on vlt-core before the convention is in place there.'
module_code: 'vlt'
created: '2026-07-06'
derives_from:
  - 'inbox/2026-07-06-091001-spec-convention.md (A3-1)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-06): build order 14→15→16 (spec v1 ships declared-stage bell prose, adopts 091004 formal keys at build-16); drift enforcement = lint/dispatch find + tripwires nag; _agent/dispatch.md stays a hardcoded read; 091001 LB1/LB3 generalize in build-18'
risk: 'low-moderate — additive governance + prose; one human-gated vlt-upgrade migration offer; no schema bump of any existing convention (spec.md is NEW at version 1, so no re-ack of frontmatter/wiki-* consumers)'
---

# Build #15 — the spec convention

Goal: "spec" becomes a defined artifact class — home, schema, supersession rules,
notification mechanism, mint-time consumer lock — shipped as governance stock, so the
Health-Coach→Chef contract (3 versions in 6 weeks, hand-run notification) and the
Creative→Chef proto-spec stop being one goodwill practice and one fork risk. Design source:
the vault's 29/30 pressure-test — **rejected alternatives (auto-notify, registry file,
overlay-only, spec-as-wiki-note, defer-until-n=3, lint-in-v1) are settled; do not
re-litigate.** Two load-bearing facts: the convention codifies practice (the reference
spec conforms with zero body changes), and `wiki-supersession.md:11-12` already models the
version/consumers handshake this strengthens.

## Brief-time dispositions (filing's open questions, resolved per ideation rulings)

1. **Carried-flag scheduling (filing Q1):** the cheap variant wins — carried decision-log
   flags with stated triggers get **seeded as tripwires in 091003's registry (build-17)**;
   no vlt-mint Phase-2 flag-scan in v1. Build-17's brief owns the seed format; this brief
   contributes the worked instance (the flag that survived two mints on luck).
2. **Generalize to "contracts" (filing Q2):** NO — pressure-test ruling stands; test
   against a real second instance (the meal-plan format is candidate #2, migrated not
   generalized) before any superclass.
3. **Notification-drift enforcement home (filing Q3):** ruled — **lint finds, tripwires
   nag**. The deferred `spec_notification_missing` check lands ONCE in vlt-lint (follow-on,
   not v1); the escalation/nagging wire is build-17 registry material. Per the ideation
   ruling it reads `_agent/dispatch.md` **hardcoded** (dispatch's own agent-zone treatment,
   `vlt-dispatch/SKILL.md:35-38`; comment cites the precedent) — recorded here for the
   follow-on, no action in this build.
4. **Escalation trigger (filing Q4):** pre-agreed and RECORDED IN THE SHIPPED TEXT — spec.md's
   v1 deferral prose states it: a spec version bump ever shipping without its relay entries
   promotes the lint check from "scheduled follow-on" to "next mint" priority.
5. **Bell form for v1 (091004 not yet landed):** honest **declared-stage prose**, not the
   formal keys — an "Enforcement" paragraph in spec.md's body: stage = declared (checked by
   inspection at mint/dispatch time); deferral = lint checks named above, `review_after:
   2026-08-17` (aligned with 091004's own first self-application date), escalation trigger
   per (4). Build-16's backfill walk retrofits the formal frontmatter keys — spec.md is
   listed there as a rider.

## F1 — NEW `skills/vlt-setup/assets/governance/_meta/conventions/spec.md`

Ships stock. Convention-file frontmatter mirrors the siblings (`wiki-supersession.md:1-13`
is the pattern): `type: note`, `created`/`last_updated: 2026-07-06`, `title`, `author:
hybrid`, `trust: reviewed`, `topic: vault-meta, conventions`, `status: complete`,
`sources: []`, **`version: 1`, `consumers: [vlt-mint, vlt-dispatch]`** (vlt-lint joins when
the follow-on checks land). Body sections:

- **Class definition + boundary.** A spec is a *durable, owned, versioned cross-partner
  contract* — authored by one partner, consumed by ≥1 other, cited into durable artifacts,
  revised over time. Explicitly distinguished from a **handoff pointer** (transient, closes
  on pickup), a **handoff doc** (one-shot payload in `_agent/handoffs/`), a **wiki note**
  (knowledge, `wiki-supersession.md`'s domain), and **BMad's SPEC kernel** (`bmad-spec`).
  This boundary is what disambiguates dispatch's existing informal "spec" usage
  (`vlt-dispatch/SKILL.md:162/:176/:193`) — untyped overloading, now typed.
- **Home:** `{specs}` → `_agent/specs/` (agent zone → upgrade-durable by construction),
  created **lazily on first spec** (like `capabilities/` — no eager scaffold).
- **Spec-artifact frontmatter schema:** `type: spec`, `title`, `owner` (authoring partner
  slug), `consumers` (list of **partner slugs**), `version` (integer; bump only on changes
  to targets/constraints/rules — never typos/prose), `supersedes` (prior spec path,
  structural rewrites only), `status` (active | superseded), `created`, `last_updated`.
- **The two `consumers:` semantics, stated explicitly:** on a *convention file* the key
  lists **skills**, acked via `depends_on` (the existing handshake); on a *spec artifact*
  it lists **partners**, notified via dispatch relay. Same key, different registries — this
  convention owns the disambiguation.
- **Supersession rules:** parameter changes → in-place revision at the stable path +
  `version` bump + a "What changed" changelog section (codifies the reference spec's
  six-week practice; preserves relay's doc-path idempotency). Structural rewrites → new
  file + `supersedes:` back-pointer (wiki-supersession's never-silent principle).
- **Notification rule — push-MUST + pull-SHOULD** (auto-notify is architecturally
  impossible; "auto" appears nowhere in the text): on version bump the author MUST fire
  `vlt-dispatch relay (to-slug, gist, spec-path)` once per listed consumer, same session
  as the bump; a consumer citing a spec SHOULD re-check its `version` against the last
  version it consumed. Redundant pair by design.
- **Mint-time consumer lock:** any mint or capability change that makes a partner consume
  an existing spec MUST add that partner to the spec's `consumers:` in the same change
  (the anti-fork mechanism, placed at the only moment a third consumer can appear).
- **Enforcement (v1 bell):** the declared-stage paragraph per disposition 5.

**Scrub rule (public repo):** examples in the shipped text use the stock cast
(librarian/researcher/creative) or placeholder paths
(`_agent/specs/{date}-{owner}-to-{consumer}-{slug}.md`) — never vlt-core's
health-coach/chef artifacts. Schema and rules text should match the vault's local mint
**exactly** (coordinate: read vlt-core's minted `spec.md` before finalizing, grounding
read-only) so the upgrade divergence check self-clears on everything except examples —
any residual example-only delta is expected to surface as `convention_base_divergence`
for a one-time reconcile (see Migration).

## F2 — `vlt-setup` + `module.yaml`: the `{specs}` logical path

- `skills/vlt-setup/assets/module.yaml` `vault_structure.default` map (`:44-58`, the
  declared SSoT at `:41-43`): add `specs: _agent/specs/` (alphabetical-ish placement beside
  `sessions:` fine — match existing ordering style). Existing installs pick it up via
  vlt-upgrade Step 3.6's provision hand-off (setup materializes config.yaml from this map).
- `skills/vlt-setup/SKILL.md:143` §2 enumeration: `_meta/conventions/{frontmatter,
  wiki-index,wiki-supersession,wiki-consolidation,extraction,spec}.md`. The baseline stash
  (`:146`) loops over shipped conventions — covers spec.md automatically, no edit.
- `skills/vlt-setup/SKILL.md:55-70` illustrative path table: add the `specs` row
  (secondary documentation touch; the table is marked illustrative, module.yaml rules).
- **No eager scaffold** — setup does not create `_agent/specs/`.

## F3 — `vlt-dispatch`: the notification rail (five touch points + depends_on)

1. Locations list (`:39` block): add **the spec zone** → `_agent/specs/` beside the
   handoff-zone bullet (durable cross-partner contracts; `relay` points at these too).
2. Relay-when-done reflex (`:152`): fires equally on a **spec version bump** — one relay
   per listed consumer, same session (the reflex text gains the spec case).
3. Input validation (`:158`): "the stable path under `_agent/handoffs/`" widens to
   `_agent/handoffs/` **or `_agent/specs/`**.
4. Stable-path lifecycle note (`:176`): gains the spec nuance — in-place version bumps
   *are* the stable-path discipline; a `supersedes` rewrite is a new path and gets fresh
   pointers.
5. Worked example (`:193`): currently hardcodes the live vault artifact
   `_agent/handoffs/2026-06-13-…` — **repoint to a placeholder**
   (`_agent/specs/{date}-{owner}-to-{consumer}-{slug}.md` style). This is 091001 LB2's
   fix, and it ships here (it IS this touch point); the general "no live vault paths in
   shipped worked examples" rule statement is build-18 material.
6. Frontmatter: **ADD** `depends_on: ["spec@1"]` — vlt-dispatch has no `depends_on` today
   (`:1-4` is name+description), so this is a new block, not an append.

## F4 — `vlt-mint`: the consumer lock (+ depends_on)

- One sentence in **Step 3, before the per-kind blocks** (`:101`, binding all kinds), and
  echoed in *Mint a new partner* (`:116`, where a vertical partner typically acquires a
  spec relationship): a mint that makes the partner consume an existing spec edits that
  spec's `consumers:` in the same change, and `_agent/mint/decision-log.md` records it.
- *Edit a convention* (`:124-134`) needs **no change** — spec.md enters the ceremony as an
  ordinary base convention.
- Frontmatter: **ADD** `depends_on: ["spec@1"]` (vlt-mint likewise has none today; its
  four "depends_on" grep hits are handshake prose, not frontmatter).

## F5 — operating contract: the third boundary

`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` — the *Two handoff
timings* paragraph (`:223`, section from `:208`): add the third boundary — a durable doc
that *outlives sittings, crosses a partner boundary, and revises over time* is a **spec**,
lives in `{specs}` under `_meta/conventions/spec.md`, and is not a handoff doc. Pointer
only, no mechanics restated (the contract is deliberately un-handshaked — single-home +
pointers; this stays consistent).

## F6 — `vlt-upgrade` Step 3 item 5 (Migrations): the human-gated proto-spec retrofit offer

Add one idempotent migration item (host: `vlt-upgrade/SKILL.md:67-70`, reported via
`migrations_run:` at `:88`): scan `_agent/handoffs/` for spec-shaped docs (revised in
place, "What changed" sections, or ≥2 relay entries pointing at the same path) and
**offer** — never auto-move — the retrofit:

- `git mv` to `_agent/specs/`; leave a **one-line pointer stub at the old path**
  (append-only records stay untouched); conform frontmatter to the spec schema; zero body
  changes.
- **Re-point any open dispatch pointers** at the old path to the new one (relay dedups on
  doc path; a move resets the key — without this, a stale open pointer and a fresh relay
  can coexist. This is 091001 LB3's fix *for this migration*; the generalized
  move-safety rule — worktree copies untouched, stub-the-old-path as standing procedure
  for all relocation migrations — is build-18's).
- Idempotent: a second run finds nothing spec-shaped left in `_agent/handoffs/`.

vlt-core's own retrofit (nutrition spec → `version: 3`, `owner: health-coach`,
`consumers: [chef]`) is the vault-side dry run of this exact procedure — it happens
field-side at mint time, not here; this migration serves *other* installs and the general
case.

## Registration

**None.** A convention ships in the governance bundle; no `module-help.csv` row (per
vlt-mint: "a convention edit registers nothing in the help registry"). No workflow changes.

## Out of scope (dispositioned)

- **The two lint checks** (`spec_schema_violation`, `spec_notification_missing`) — named
  follow-on, explicitly not v1 (filing change 6). Home and path ruling recorded in
  disposition 3; lands once, in vlt-lint, after the doctrine machinery exists.
- **Formal 091004 bell keys on spec.md** — build-16 rider (backfill walk retrofits;
  disposition 5's prose bell holds until then).
- **Carried-flag tripwire seeding** — build-17 (disposition 1).
- **"Contracts" superclass** — not pre-generalized (disposition 2).
- **Generalized move-safety + worked-example placeholder rules** — build-18 (this build
  ships both *instances*, build-18 ships the *rules*).

## Verification (unit, at rest — lifecycle step 5)

- **Bipartite handshake:** spec.md `consumers: [vlt-mint, vlt-dispatch]` ↔ both skills
  carry `depends_on: ["spec@1"]`; no other skill needs an ack (grep `spec@` across
  `skills/` finds exactly two). vlt-lint deliberately NOT a consumer yet — its
  `depends_on` (`vlt-lint/SKILL.md:4`) untouched.
- **Path resolution:** grep `{specs}` across `skills/` — every hit is in a skill whose
  text explains resolution via the structure map; `module.yaml` has the `specs:` row;
  setup §2 enumeration includes `spec`; illustrative table row present.
- **No live-vault paths in shipped skills:** grep `2026-06-13` (and `_agent/handoffs/2026`)
  across `skills/` → zero hits after F3.5.
- **Scrub check:** grep `health-coach|chef|nutrition` (case-insensitive) across the new/
  changed shipped files → zero hits.
- **Packaging:** `uv run tools/package-lint.py` (build-14 precedes this build) → exit 0 —
  covers module.yaml still parsing with the new row and no cruft introduced.
- **Contract/dispatch/mint single-home spot-check:** the relay mechanics appear only in
  vlt-dispatch; the consumer-lock mechanics only in vlt-mint's one sentence + spec.md's
  rule; the contract carries pointers only.
- **Faithfulness diff:** shipped spec.md rules/schema sections match vlt-core's minted
  version (read-only grounding diff recorded in the build notes; example sections may
  differ by scrub).

## Acceptance (live — appended to the Arc 3 roadmap ledger)

- **Hard gate honored:** the next partner mint on vlt-core happens only with the spec
  convention in place, and exercises the consumer lock (the new partner lands in the
  consumed spec's `consumers:` in the same mint — days-to-first-check = 0 for this
  boundary, vs the firewall's 4).
- **0.6.0 upgrade on vlt-core:** skip-if-present honored (the vault's minted `spec.md`
  base NOT clobbered); baseline stash gains `spec.md` (shipped stock); `config.yaml` gains
  `specs:` via the provision hand-off; divergence report either clean or surfaces the
  expected example-only delta for a one-time reconcile — nothing else.
- **Migration offer:** fires and is human-gated; on decline, nothing moves; on accept for
  a proto-spec, old path carries the stub, open pointers re-pointed, `migrations_run:`
  records it. (On vlt-core the retrofit likely pre-empts this at mint time — the offer
  then finds nothing spec-shaped and reports idempotent-clean, which is itself the check.)
- **Relay accepts a spec path:** a spec version bump on vlt-core produces one relay per
  listed consumer with the `_agent/specs/` path validated.
