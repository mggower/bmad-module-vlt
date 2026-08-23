---
title: 'Build #11 — Upstream vlt-track: the shared longitudinal-loop hand (Round 2 candidate #4)'
status: 'BUILT 2026-06-25 — unit-verified at rest (handshake bipartite-consistent; CSV parses at 13 cols; manifest complete). Live acceptance deferred to the batched first-safe vlt-core upgrade.'
build_log:
  - 'BUILT 2026-06-25. Five parts shipped: (1) NEW skills/vlt-track/SKILL.md — lifted from vlt-core in substance with two changes: depends_on ["extraction@2","wiki-supersession@1"] (mirrors vlt-extract; defers PARA frontmatter to extraction.md so does NOT ack frontmatter@2), and the loop-profile read REHOMED from the calling partner SKILL.md → its capabilities/track.md heavy pointer (Overview + On-Activation read beat + headless fallback). (2) capability-template.md heavy-pointer extended with an optional "## Loop profile" block (root/target/subject-model/data-streams/log-tag/non-negotiable-gate) + a "wear vlt-track = add capabilities/track.md, do not mint a duplicate" note. (3) Handshake: added vlt-track to extraction.md (now [vlt-extract, vlt-lint, vlt-track]) and wiki-supersession.md (now [vlt-ingest, vlt-lint, vlt-extract, vlt-track]) consumer lists. (4) Registration: module-help.csv row TK (always-quoted free-text per build-10 #3, caller-driven scope note) + marketplace.json skills[] += ./skills/vlt-track. (5) vlt-mint vertical-partner archetype docs (SKILL.md:52 + :120) reframed — a domain partner running a longitudinal loop WEARS vlt-track via capabilities/track.md, only a non-loop verb mints its own op skill; (c) widening clause notes the vlt-track loop requires the personalized-extraction allowance. Verification: a python check confirmed BIPARTITE-CONSISTENT across all 5 conventions ↔ their consumers, module-help.csv parses (header 13 cols, vlt-track row 13 cols, zero mis-split rows), marketplace.json valid + every on-disk vlt-* skill registered + no manifest path missing. Zero migration. build-7 acceptance check #1 superseded + build-11 acceptance appended in the roadmap Deferred ledger.'
phase: 'Follow-on — Round 2 candidate #4 (upstream the local longitudinal-loop op; threads build-7 capability-object + build-8 firewall)'
module_code: 'vlt'
created: '2026-06-25'
updated: '2026-06-25'
derives_from:
  - 'inbox-evolution-roadmap §R2-4 — the deferred upstream candidate'
  - 'vlt-core local mint: {field-vault}/.claude/skills/vlt-track/SKILL.md (the field-evolved source of truth)'
  - 'skills/reports/vlt-partner-capabilities-ideation.md (build-7 — the capability object model this lands inside)'
  - 'skills/reports/build-7-capability-object.md (heavy = a registered op skill via a capabilities/{slug}.md skill: pointer)'
  - 'skills/reports/build-8-extraction-method-firewall.md (the vlt-lint firewall that polices this op''s personalized-extraction writes)'
ideation_decisions:
  - 'FORM (owner: instinct #1, asked for recommendation → recommended + confirmed #1): ship vlt-track exactly as field-evolved — a single SHARED, profile-driven HEAVY op ("one verb, many subjects"). The build-7 "light track family" acceptance prediction is SUPERSEDED. Framing: the field validated build-7''s OBJECT model (op skill = heavy capability with a skill: procedure) while refuting its WEIGHT prediction (light family) — because vlt-track writes a curated PARA deliverable, a shared lane, which is heavy by the capability model''s own lane-safety rule.'
  - 'PROFILE HOME (owner: capability-file pointer / build-7-integrated): the calling partner''s loop profile moves from inline-in-SKILL.md (vlt-core''s field location) into the partner''s capabilities/track.md heavy pointer. One home for "this partner wears track + here is its profile." This is the single substantive design delta from a verbatim lift, enabled by build-7 shipping AFTER vlt-core minted vlt-track.'
  - 'WEARER (owner: ship the hand only): no example vertical partner ships — consistent with the module shipping zero vertical partners today. vlt-mint archetype docs + a worked example inside the skill teach vaults to wear it; vaults mint the wearer (as vlt-core did).'
  - 'NO FAMILY: vlt-track does NOT instantiate a Model-B family (one shared body, not N free bodies → nothing to bind). The family construct stays valid infrastructure awaiting a genuinely-light recurring verb. build-7''s family machinery is shipped-but-unexercised after this; noted honestly, not forced.'
  - 'HANDSHAKE: vlt-track mirrors vlt-extract''s ack set exactly — depends_on ["extraction@2", "wiki-supersession@1"]; add vlt-track to those two conventions' consumers:. It defers PARA frontmatter to extraction.md (like vlt-extract), so frontmatter.md consumers stay wiki-writers only.'
---

# Build #11 — Upstream vlt-track: the shared longitudinal-loop hand

## Thesis

`vlt-track` is the one genuinely-new verb the live `vlt-core` roster grew that the module never had:
**running a program across weeks** (design a protocol → log progress → review and adjust), as opposed
to answering a one-off question. It was minted locally in `vlt-core`, preserved across the 0.3.0
upgrade as a local mint, and flagged in Round 2 as an upstream candidate — **not a defect fix, a real
op-skill design.** Now that 0.3.0's invariant-based personalized-extraction firewall (build-8) and the
capability object model (build-7) have shipped, vlt-track fits the module cleanly. This build upstreams
it.

## The crux this ideation resolved

The vlt-track that actually evolved in the field is a **shared, profile-driven _heavy_ op** —
*"one verb, many subjects."* The skill encodes the loop; the **calling partner brings the voice, the
non-negotiable, and a loop profile** (where the working record lives, where the polished protocol
lands, single- vs multi-subject, which data streams). It writes the working log to the agent zone and
the **polished protocol to PARA via personalized-extraction discipline**.

That PARA write is decisive: it is a **shared lane**, which makes vlt-track **heavy** by the capability
model's own lane-safety discriminator. This **refutes build-7's prediction** that vlt-track would
become a *light* `track` family across the three horizontal partners — that prediction assumed
tracking writes only the partner's own zone. **The field chose a better answer:** one shared heavy
body, parameterized per-caller, instead of N per-partner bodies bound by a family contract. The "one
idea, per-partner application, no switch-skill, no duplicate skills" problem the family was invented to
solve is solved here by **profile parameterization + the partner's coloring** — at one registration,
not N.

**Resolution: ship the field design (#1).** The field **validated build-7's object model** (op skill =
heavy capability with a `skill:` procedure) while **refuting its weight prediction** (light family).
build-7 is not wasted — vlt-track lands *inside* its model, at heavy weight.

## Scope (frozen)

Upstream vlt-track as a shared heavy op + wire it into the build-7 capability model + register the
build-4 handshake + the build-8 firewall coverage + the vlt-mint archetype coherence edit. **No example
vertical partner. No Model-B family. No new convention.** Zero data migration.

## What ships — the parts

### Part 1 — `skills/vlt-track/SKILL.md` (lift + one rehoming)

Lift the field skill from `vlt-core` verbatim **in substance** (Overview / On-Activation / Design /
Log / Review-and-adjust / the personalized-extraction write spec / Verify), with **one substantive
change** and the mechanical frontmatter add:

- **Frontmatter handshake ack:** add `depends_on: ["extraction@2", "wiki-supersession@1"]` (mirrors
  `vlt-extract`). It JIT-reads `frontmatter.md` for the PARA schema but **defers** that schema to
  `extraction.md` exactly as `vlt-extract` does → does **not** ack `frontmatter@2` (keeps
  frontmatter.md's consumer set = wiki-writers only; bipartite-clean).
- **THE REHOMING (owner Q2 — the design delta):** the "Read the loop profile" beat changes its source.
  In vlt-core the profile is read from the **calling partner's SKILL.md** (a *Loop profile* block). Here
  it is read from the **calling partner's `capabilities/track.md`** — the heavy capability pointer
  (build-7). Update every reference:
  - On-Activation: "read that partner's **loop profile from its `capabilities/track.md`** (the heavy
    `skill: vlt-track` pointer) and bind `{root}` / `{target}` / subject-model / data-streams / log-tag
    / non-negotiable-gate for the run."
  - Headless fallback: "take the profile from the **named owning partner's `capabilities/track.md`**,
    or ask for the missing pieces — never guess `{root}` / `{target}`."
- **Everything else lifts unchanged:** the persona-neutral/profile-driven framing; the two-layer split
  (agent-zone working record + PARA polished protocol); the hard invariant (every method claim traces
  to a wiki page in `sources:`; `personalization_sources:` carries state, never method); the gated-mint
  sanction requirement; the in-place re-extraction + supersession callouts; the `track` `{log}` type
  (contract's type set is non-exhaustive); the no-session-note rule.
- **Logical names used** are all existing (`index`, `wiki`, `log`, `conventions`). `{root}` and
  `{target}` are **profile-supplied, ad-hoc under `_agent/` / PARA** — **no new `vault_structure`
  entries needed.**

### Part 2 — `skills/vlt-mint/assets/capability-template.md` (extend the heavy-pointer template)

The heavy-pointer template (`procedure: { skill: vlt-{op} }`, `write_scope: {lane}`, `weight: heavy`,
`council_class: gated`) gains an **optional "Loop profile" section** for longitudinal-loop ops. This is
what makes "wear vlt-track" a concrete, copyable shape:

```markdown
## Loop profile  (only for a longitudinal-loop op, e.g. vlt-track)
- root: _agent/<area>/<subject?>/      # agent-zone working root (the running log[s] live here)
- target: <PARA area>/<subject?>/      # where the polished protocol lands (extraction target)
- subject-model: single | multi (scoped under a slug, e.g. {dog})
- data-streams: <file(s) the log beat appends to, and what each holds>
- log-tag: <this partner's slug for the {log} line>
- non-negotiable-gate: <this partner's named method gate, re-asserted at the write>
```

A wearing partner's `capabilities/track.md` is then: the heavy `skill: vlt-track` pointer **+** this
filled Loop-profile block. Single home for "this partner wears track + its profile."

### Part 3 — Handshake registration (build-4 discipline)

- `extraction.md` `consumers: [vlt-extract, vlt-lint]` → **`[vlt-extract, vlt-lint, vlt-track]`**.
- `wiki-supersession.md` `consumers: [vlt-ingest, vlt-lint, vlt-extract]` → **`+ vlt-track`**.
- `vlt-track` `depends_on: ["extraction@2", "wiki-supersession@1"]`.
- **Re-verify bipartite-consistent** at rest across all 5 conventions after the edit.

### Part 4 — Registration

- **`skills/vlt-setup/assets/module-help.csv`** — add a `vlt-track` row. **Always-quote** the
  free-text fields (build-10 #3 write-side rule — no unquoted commas). Menu-code + a description naming
  it the shared longitudinal-loop hand; `args`/scope note that it is partner-driven (reads the caller's
  loop profile).
- **`.claude-plugin/marketplace.json`** — add `"./skills/vlt-track"` to `skills[]` (the install
  manifest — the exact gap the 0.3.0 bump caught for vlt-dispatch/vlt-upgrade; don't repeat it).

### Part 5 — vlt-mint vertical-partner archetype coherence

vlt-mint's archetype guidance (`SKILL.md:52`, and the Phase-1 / Mint-a-partner refs at `:116`/`:120`)
currently says a vertical/domain partner "**typically needs its own operation skill**." Reframe to point
at vlt-track as **the canonical shared longitudinal hand**: a domain partner that runs a *program over
time* **wears vlt-track** by adding a `capabilities/track.md` heavy pointer + loop profile (and opting
its mint into the `extraction.md` personalized-extraction widening) — it does **not** mint a bespoke
duplicate loop op. Keep "may need its own op skill" for genuinely-novel domain verbs that aren't a
longitudinal loop. This closes the coherence gap the upstream creates (a shipped shared hand the
archetype docs don't yet mention).

## What this build deliberately does NOT do

- **No example vertical partner** (owner: ship the hand only). The module keeps shipping zero vertical
  partners; vaults mint the wearer.
- **No Model-B `track` family.** One shared body ≠ N bound instances. build-7's family machinery stays
  valid but **unexercised** after this — it awaits a genuinely-light own-zone recurring verb
  (`watch`/`digest`) as its real example. Honest note, not a gap to fill here.
- **No new convention, no convention version bump.** vlt-track is a *consumer*; the personalized-
  extraction rule it obeys already shipped at `extraction@2` (build-5/8).
- **No data migration.** Pure additive: one new skill + handshake/registration adds + doc coherence.

## Cross-build reconciliation (housekeeping this build triggers)

- **build-7 acceptance check #1** ("re-create vlt-track as a **light, vault-grown** capability with a
  `track` **family**") is **SUPERSEDED** — update it in the roadmap's Deferred ledger to the real shape:
  *vlt-track ships as a **heavy** capability; a vertical partner wears it via a `capabilities/track.md`
  heavy pointer + loop profile; lane-safety + the build-8 extraction firewall hold.* Add a one-line note
  that build-7's family machinery now lacks a canonical example (awaiting a light verb).
- **build-8 acceptance** already references "a real `vlt-track`-style personalized extraction" — now
  there's a real `vlt-track` to exercise it against. No change needed; just connect them in the ledger.

## Acceptance (deferred — batched to the next safe vlt-core upgrade)

- [ ] A vertical partner (e.g. vlt-core's Dog Trainer / Health Coach) wears vlt-track via its
      `capabilities/track.md` heavy pointer + loop profile; the skill reads `{root}`/`{target}`/streams
      /gate from **that file** (not the partner SKILL.md) and runs all three beats.
- [ ] **Design** writes a PARA protocol whose `sources:` are **wiki pages only** and whose
      `personalization_sources:` cite the agent-zone stream(s); **every method claim traces to a wiki
      page**; the partner's named non-negotiable is re-asserted at the write.
- [ ] **Log** appends to the right agent-zone stream with **no method/general knowledge leaking** into
      the log (state only); **Review** interprets the trend (not the noisy point) and re-extracts the
      protocol **in place** with supersession callouts.
- [ ] **vlt-lint** flags a vlt-track protocol with a method claim ungrounded in its wiki `sources:`
      (`method_not_in_sources`) — build-8 firewall fires against the real op.
- [ ] Handshake reads **bipartite-consistent**: `vlt-track`'s `extraction@2`/`wiki-supersession@1` acks
      are current; both conventions list `vlt-track`.
- [ ] vlt-track is **registered** (module-help.csv row parses with quoted fields; marketplace.json
      installs it) and **survives** a vlt-upgrade as shipped (no longer a vlt-core local mint — it's now
      upstream, so B1 preserve no longer has to carry it).

## Open questions (non-blocking — flag at build, defer if quiet)

- Should the heavy-pointer template's Loop-profile block be a **separate small asset** (referenced by
  both the template and vlt-track) rather than inlined, to keep one source if its shape evolves? (Lean
  no for n=1; revisit at a second longitudinal op.)
- Does `module-help.csv` want a discovery hint that vlt-track is **caller-driven** (not directly summon-
  able) so a user isn't pointed at it cold? (Probably a scope-column note; cheap.)
- Once a genuinely-light recurring verb appears, does it become build-7's family acceptance example —
  closing the loop this build opened? (Tracked as a future note, not scope.)

## Build order

1. Part 1 (the skill) — it's the thing being shipped; everything else references it.
2. Part 2 (template Loop-profile block) — gives wearers a copyable shape.
3. Parts 3–4 (handshake + registration) — make it coherent + installable.
4. Part 5 (archetype coherence) — points future mints at it.
5. Re-verify handshake bipartite-consistent; unit-check the help.csv parse + marketplace manifest.
