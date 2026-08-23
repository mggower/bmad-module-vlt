---
title: 'Build #19 — the build-15 follow-up unit (spec advocacy gets a faster clock; two maps get their missing row)'
status: 'BUILT 2026-07-17 — F1–F4 landed + unit-verified at rest (handshake bipartite=4 acks all spec@1, no spec.md bump; contract specs row + SSoT note; tool-zone "not a content layer" reframe; package-lint A/B/C PASS D SKIPPED @0.6.0). Deviations: (a) built directly (no workflow to build — brief noted bmad-workflow-builder but the build ships no workflow); (b) spec_candidate check placed after the Personalized-extraction firewall bullet, at the tail of the governance cluster before High-value gaps (brief said "alongside 74-80" — kept in-cluster). Not a release build; release-tail acceptance rides the next arc-version release.'
module_code: 'vlt'
created: '2026-07-17'
derives_from:
  - 'inbox/2026-07-13-092341-spec-convention-has-no-advocate.md (A3-12: the unregistered `spec@1` consumer at `vlt-upgrade` + the spec-advocacy **cadence** residual — origination gated to upgrade cadence only)'
  - 'inbox/2026-07-12-114910-dev-zone-contract-graduation.md (A3-10: the operating contract''s structure-map table missing its `specs` row — a build-15 scope omission + the tool-zone closed-enumeration drift)'
roadmap: 'skills/reports/inbox-evolution-arc3-roadmap.md'
rulings: 'roadmap §Ideation rulings — A3-7..A3-17 (2026-07-17): build-19 = build-15 follow-up unit — A3-12 residuals (cadence + `vlt-upgrade`→`spec.md consumers:` join + `spec@1` ack, per the pointer-vs-ack ruling Q15 "vlt-upgrade:75 ENCODES → ack") plus A3-10 (contract `specs` row + dev-zone Q7/Q8); "smallest; ships first." Gate 1 (arc NOT blocked): origination path exists at `vlt-upgrade:75`; residual is CADENCE, not existence.'
risk: 'low-moderate — a convention-registry + governance-check cluster on `spec.md`. No `spec.md` version bump (registry corrections + a new enforcement mechanism for an existing rule are not rule changes); two new consumers (`vlt-upgrade`, `vlt-lint`) newly ack the current `spec@1`. The operating contract is deliberately un-handshaked, so its two edits register nothing. Not a release build — version bump rides the release build.'
---

# Build #19 — the build-15 follow-up unit

Build-15 shipped the spec convention and, in the same commit, its origination path (the
proto-spec retrofit at `vlt-upgrade:75`). Two residues survived it, both surfaced by field
evidence after the fact, and grouped here as the "build-15 follow-up unit" (roadmap §Ideation
rulings — A3-7..A3-17): **(1)** the origination path fires only at **upgrade cadence** — a
rare, owner-run event — so the spec class has an advocate but on too slow a clock; **(2)** the
site that encodes the convention's heuristic (`vlt-upgrade:75`) never joined the convention's
`consumers:`, so a future `spec.md` bump would drift silently past it. Alongside these,
build-15's scope omission left the operating contract's structure-map table missing its
`specs` row while the contract itself uses `{specs}` — and the same filing exposed a closed
"two top-level folders" enumeration in the contract's tool-zone prose (the completeness-list
drift the standing rules name).

This build closes all four. It adds a **lint-cadence spec-candidate surfacing check** (reusing
the `vlt-upgrade:75` heuristic — no new heuristic invented) to give the class a steady-state
advocate; **registers `vlt-upgrade` and `vlt-lint` as `spec@1` consumers**; **adds the `specs`
row** to the operating contract's map (with an SSoT-mirror note, matching the `vlt-setup:61`
precedent); and **reframes tool zones as an extensible class**. It is the smallest build in the
run and ships first.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** A3-12's
central "no shipped surface can originate a spec" claim is REFUTED (Gate 1, 2026-07-17):
`vlt-upgrade:75` originates specs and fired correctly on vlt-sayari (one candidate surfaced,
offered, human-declined). Empty `_agent/specs/` is a **correct negative**, not unreachability.
The build does **not** add an author-a-spec `vlt-mint` kind, does **not** touch the
adoption/first-instance facet (re-homed to build-20), and does **not** land the two deferred
lint checks (`spec_schema_violation`, `spec_notification_missing` — they stay deferred per
`spec.md:80`).

## Brief-time dispositions

The roadmap left five questions to this brief (§"Questions deliberately left to brief time —
build-19": Q7, Q8, Q13, Q14, Q16). Each is ruled here, grounded, and none is re-litigating an
ideation ruling. The most consequential is disposition 1 (it decides whether the build ships
machinery at all) — flagged for owner amendment at review.

1. **Q14 (cadence — the load-bearing decision): upgrade-cadence origination is NOT sufficient;
   the class gets a steady-state advocate at lint cadence.** The real defect is "advocate on
   too slow a clock," not "no advocate" — grounding already pointed at the fix (A3-12 capture:
   "what isn't shipped is running it at lint cadence rather than upgrade cadence — the residual
   gap is CADENCE, not existence"). The advocate is a new `vlt-lint` governance check
   (`spec_candidate`, F2) that **reuses the exact `vlt-upgrade:75` heuristic** — a doc in
   `_agent/handoffs/` revised in place (carrying a "What changed" section) or with ≥2 relay
   entries in `_agent/dispatch.md` pointing at the same path. Lint runs far more often than
   upgrade, so the candidate is surfaced while it is fresh, not at the next rare upgrade.
   Derive-first is honored: the count derives from handoff file state + dispatch relay entries
   (the inputs `:75` already greps), **no stored counter** (A3-12 grounding, roadmap
   `:798-800`).

2. **Q13 (reflex routing vs the dispatch firewall): the advocate lives in lint, not at the
   handoff write path — so the firewall (`vlt-dispatch:41`, "relay points at specs, never
   authors them") is untouched by design.** The advocate does **not** sit as a reflex at the
   handoff/dispatch write path (that would breach the firewall) and does **not** route back to
   the owning partner automatically. It is a **human-gated surfacing flag** at lint cadence —
   exactly the posture of the proto-spec retrofit (`vlt-upgrade:75`, "offer … never auto-move;
   spec-vs-handoff is a judgment call") and of `vlt-lint`'s existing `review_due` and
   near-duplicate/merge-candidate checks (surface, never auto-fix, never escalate — `vlt-lint:62`
   states escalation of an aging queue is a tripwire concern, not lint's). Routing "back to the
   owning partner" is not lint's job; lint surfaces the candidate to the human/partner who then
   decides. The firewall question dissolves because nothing automated crosses it.

3. **Q16 (is zero-specs-at-9-days a signal?): NO — absence is not a signal; the check surfaces
   candidates that EXIST, never alarms on an empty spec zone.** Both observed candidates across
   two vaults were human-judged not-specs, correctly (Gate 1: "a convention working, not a
   convention unreachable"). So `spec_candidate` flags only handoff docs that *match the
   spec-shaped signals* — it manufactures no signal from the absence of specs (which would be
   the same "measure an absence with no event to count" trap that made the adoption facet a poor
   fit for build-17). An empty `_agent/handoffs/` or `_agent/specs/` produces **zero findings**,
   never a "this vault has no specs" nag. This also keeps the check honest against the
   scarcity reading: zero durable cross-partner contracts at current vault scale may simply be
   true, and the check must not pathologize it.

4. **Q7 (dev-zone: extensible tool-zone class vs. a named `dev/` row): make tool zones an
   extensible class; do NOT add a `dev/` row.** A named `dev/` row would encode a vault-local
   pattern (vlt-sayari's symlink tree) into module source — a durability-posture violation
   (CLAUDE.md: never treat vault-local evolution as module source). The grounded fix is to
   replace the closed "two top-level folders" enumeration (`contract:81`) with an extensible
   class that admits a vault's own tool infrastructure, using the **actual** boundary rule from
   `vlt-sayari/CLAUDE.md:38` — **"not a content layer"** (partners never ingest/lint/extract
   from it) — **not** the filing's "read-only for partners" misreading (A3-10 grounding
   confirmed the invariant is "not a content layer": a dev context reads the vault's
   spec/knowledge *and edits code in one tree*).

5. **Q8 (should a hand-transcribed third copy of the map exist at all?): YES — keep the contract
   table; it is the map's SEMANTIC home, not a redundant SSoT.** `module.yaml:44-59` (the SSoT)
   and `vlt-setup:61` carry only `name → path` pairs; the contract table (`:29-44`) is the only
   copy carrying the **"What lives there"** semantic column — the definitional documentation a
   partner or a generic agent reads to understand the vault. It should exist. The SSoT tension
   (`module.yaml:41-43` declares "never a hand-transcribed markdown table" while `:29-44` is
   one) is resolved exactly as `vlt-setup:61` already resolved it for its own copy: **add the
   missing `specs` row AND a one-line note that the path defaults mirror `module.yaml` (the SSoT
   for path values), while this table is the semantic home.** That neutralizes the
   competing-SSoT concern without deleting the constitution's explanatory map.

6. **Version-handshake disposition (not a deferred question, but load-bearing — recorded so the
   builder does not bump in error): NO `spec.md` version bump.** Per Q15 (RULED) and the
   general pointer-vs-ack line: adding `vlt-upgrade` and `vlt-lint` to `consumers:` corrects the
   registry to reflect real consumption, and adding a lint check is a *new enforcement
   mechanism for an existing rule* — neither changes "the rules consumers must follow" (schema,
   supersession, notification are unchanged). `spec.md` stays `version: 1`; the two pre-existing
   consumers (`vlt-mint`, `vlt-dispatch`) keep their current `spec@1` acks (no re-ack); the two
   new consumers newly ack `spec@1`. This is a registry+ack change, not a consumer walk.

## F1 — `vlt-upgrade` registered as a `spec@1` consumer

**Current state.** `skills/vlt-upgrade/SKILL.md:1-4` carries `name` + `description` **only — no
`depends_on:` line at all** — yet `:75` reads `{conventions}/spec.md`, encodes its spec-shaped
detection heuristic, and conforms retrofitted docs to the spec schema. `spec.md:12` lists
`consumers: [vlt-mint, vlt-dispatch]`. `vlt-upgrade` is the one place in the module where a
skill recites a convention's mechanics without appearing in its `consumers:` (A3-12,
roadmap `:786-795`). If `spec.md` ever bumps, the consumer walk (`vlt-mint:140`, exit-gated
`:141`) and lint's coherence net (`vlt-lint:74`) both walk only *listed* consumers, so `:75`
would drift silently.

**The exact change.**
- Add a `depends_on:` line to `vlt-upgrade`'s frontmatter (after `name:`, before
  `description:` — matching the shape of `vlt-mint`'s `depends_on: ["spec@1", "frontmatter@3"]`
  at `vlt-mint:2`): **`depends_on: ["spec@1"]`**. Ack the CURRENT version (no bump — disposition
  6). `vlt-upgrade` acks *only* `spec@1`: for every other convention it merely refreshes files
  (survives any rule change unedited → pointer, not consumer, per Q15's general line); only
  `:75` encodes a rule.
- Add `vlt-upgrade` to `spec.md:12`: `consumers: [vlt-mint, vlt-dispatch, vlt-upgrade]`
  (F2 adds `vlt-lint` — final state in F2).

**Why.** Discharges A3-12's "unregistered consumer of `spec@1`" gap (roadmap `:786-795`).
Build-15's own verification missed it because its grep searched for the *ack*, not the
*consumption* (roadmap `:790-792`).

**Out of scope (per-site).** `vlt-upgrade`'s many other convention touches (it refreshes the
whole governance bundle) do **not** become acks — they are pointers by the Q15 line.

## F2 — spec advocacy at lint cadence (the cadence residual)

**Current state.** Spec origination fires only at upgrade cadence: `vlt-upgrade:75` (proto-spec
retrofit, human-gated offer) is the sole origination surface, run on a rare owner-initiated
upgrade. `vlt-lint`'s governance checks (`vlt-lint:74-80`, "both modes") operate on
`{conventions}/`, `{overlays}/`, `{partners}/*/capabilities/` — there is **no** spec-candidate
check. `vlt-lint:4` `depends_on` does not include `spec@1`. `spec.md:80` (Enforcement) names two
*deferred* lint checks (`spec_schema_violation`, `spec_notification_missing`) and states "When
they land, `vlt-lint` joins this file's `consumers:`." The governance checks are **SKILL-side
prose**, not part of the `vlt-lint-full.js` page-fan-out workflow (the workflow reduces the wiki
link graph only) — so this check is a SKILL-level addition, no workflow edit.

**The exact change.**
- **Add a governance check** to `vlt-lint`'s "both modes" governance list (alongside the bullets
  at `vlt-lint:74-80`), worded as a surfacing-only, human-gated check. Model its prose on the
  existing governance bullets and on `vlt-upgrade:75`'s heuristic so the heuristic stays
  **single-home** (define the signals once — point at `{conventions}/spec.md`'s spec-vs-handoff
  boundary and at the shared `vlt-upgrade:75` detection wording; do not invent a third phrasing).
  Substance:

  > **Spec candidates (governance check; both modes)** — surface handoff docs that have outgrown
  > the handoff class. For each doc in `_agent/handoffs/` that is **revised in place** (carries a
  > "What changed" section) **or** has **≥2 relay entries in `_agent/dispatch.md` pointing at the
  > same path**, flag it (`spec_candidate`) as a possible `{specs}` contract per
  > `{conventions}/spec.md` — the same signals the proto-spec retrofit (`vlt-upgrade:75`) offers
  > at upgrade time, surfaced here at lint cadence. **Never auto-promote** (spec-vs-handoff is a
  > judgment call — file to the backlog / flag for the human, exactly as merge candidates and
  > `review_due` are surfaced). An empty `_agent/handoffs/` yields no findings; **the check never
  > alarms on the absence of specs** — it surfaces candidates that exist, never zero-specs.

- **Add `spec@1` to `vlt-lint:4`** `depends_on`:
  `["frontmatter@3", "wiki-index@2", "wiki-supersession@1", "extraction@2", "write-verification@1", "spec@1"]`.
  Rationale (Q15 line): the check encodes `spec.md`'s spec-vs-handoff threshold, so it must
  change if that threshold changes → consumer → acks. The ack covers its workflow asset
  (`vlt-lint-full.js`) per the standing rule, though that asset is unchanged here.
- **`spec.md:12` final state:** `consumers: [vlt-mint, vlt-dispatch, vlt-upgrade, vlt-lint]`.
- **Update `spec.md:80` (Enforcement) prose** — a clarification, not a rule change (no bump):
  replace the "When they land, `vlt-lint` joins this file's `consumers:`" clause with a
  statement that `vlt-lint` joins `consumers:` **now** for the live `spec_candidate` advocacy
  check, while the two schema/notification checks (`spec_schema_violation`,
  `spec_notification_missing`) **remain deferred** per this file's tripwire. Keep the
  `enforcement_stage: declared` frontmatter and the notification deferral UNCHANGED — that stage
  tracks the notification machinery, which is still deferred; the `spec_candidate` check is a
  surfacing aid (like `review_due`), not an enforcement of a spec *rule*, so it does not promote
  the stage. Bump `spec.md`'s `last_updated` to `2026-07-17`.

**Why.** Discharges the spec-advocacy **cadence** residual (roadmap ruling: rides build-19).
Gives the class a steady-state advocate without new stored state, without touching the firewall,
and without pathologizing an empty spec zone (dispositions 1–3).

**Out of scope (per-site).** The two deferred checks stay deferred (`spec.md:80` tripwire
governs their promotion — a `version` bump shipping without relay entries). No
`enforcement_stage` promotion. No author-a-spec `vlt-mint` kind (origination stays the
human-gated retrofit + this surfacing; A3-12's "creation has no home" is answered by "creation
is human-gated at two cadences," not by an automated author).

## F3 — the operating contract's structure map gains its `specs` row

**Current state.** `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:29-44`
is the structure-map table; it has rows for `wiki, index, research, sessions, log, backlog,
partners, capabilities, conventions, overlays, personas, contract, upgrade_ledger, archive` —
**no `specs` row** — while the contract itself uses `{specs}` at `:227` ("it is a **spec**, it
lives in `{specs}`"). `module.yaml:49` and `vlt-setup/SKILL.md` (the illustrative table) both
carry `specs`. This is the third-of-three copies missing it — a build-15 scope omission
(`build-15-spec-convention.md:98-108` scoped the two siblings and never listed the contract
table), not organic drift (A3-10, roadmap `:662-670`). Compounding: `module.yaml:41-43` declares
itself SSoT ("never a hand-transcribed markdown table") while `:29-44` is one.

**The exact change.**
- Insert a `specs` row into the table (`:29-44`), placed after the `sessions` row to mirror the
  ordering in `module.yaml:44-59`, carrying its semantic description:

  > `| `specs`       | `_agent/specs/`                           | Durable, owned, versioned cross-partner contracts (see `{conventions}/spec.md`) |`

  Match the existing rows' column widths / pipe alignment.
- Add a one-line SSoT-mirror note beneath the table (mirroring the `vlt-setup:61` disclaimer:
  "do not hand-transcribe … `module.yaml` is the single source of truth"): state that the path
  **defaults** in this column mirror `module.yaml`'s `vault_structure.default` (the SSoT for
  path values), and this table is the **semantic** home (the "What lives there" documentation).
  This resolves Q8's competing-SSoT tension without deleting the table.
- Bump the contract's `last_updated` to `2026-07-17` (`:4`).

**Why.** Discharges A3-10's "GAP CONFIRMED — worse than filed: the contract is internally
inconsistent" (roadmap `:662-670`). The operating contract is deliberately **un-handshaked**
(`:1-10` carries no `version:`/`consumers:`; it uses single-home + pointers — CLAUDE.md standing
rule), so this edit registers nothing and triggers no walk.

## F4 — tool zones become an extensible class

**Current state.** `vault-operating-contract.md:79-81` ("### Tool zones") reads: "Because Vault
is installed *into* the vault, **two top-level folders** are **tool infrastructure**, not vault
content: `.claude/` … and `_bmad/` …". The hardcoded "two top-level folders" is a closed
enumeration — the completeness-list drift the standing rules name (A3-10, roadmap `:657-661`;
the parallel human-zone enumeration at `:64` is a *deliberately* closed, module-defined set —
out of scope, see below).

**The exact change.** Reframe `:81` from the closed "two folders" enumeration to an extensible
class that admits a vault's own tool infrastructure, keyed on the **"not a content layer"**
boundary rule (not "read-only"). Preserve the shipped members (`.claude/`, `_bmad/`) as the
module's own tool zones; name that a vault may add its own (e.g. a `dev/` working tree) as an
example, not as a shipped row. Substance:

  > **Tool-infrastructure folders are not vault content.** The module ships two — `.claude/`
  > (the installed `vlt-*` skills + project settings) and `_bmad/` (the module config) — and a
  > vault may add its own (e.g. a `dev/` tree that reads the vault's spec/knowledge and edits
  > code in one place). The boundary is **"not a content layer"**: partners never ingest, lint,
  > or extract from these folders (they are not knowledge — `vlt-lint` and the partners ignore
  > them exactly as they would `.obsidian/`), regardless of whether a partner may *read* them.
  > A partner touches a skill under `.claude/skills/` only deliberately, through `vlt-mint`.

Keep the wording placeholder-safe: `dev/` is a generic *example* of a vault-added tool tree,
**not** a specific install's path (CLAUDE.md placeholder-path rule). Do not name vlt-sayari.

**Why.** Discharges Q7 (disposition 4) — the tool-zone class becomes vault-extensible without
encoding a vault-local pattern as a shipped row, and the boundary rule matches the field reality
("not a content layer," `vlt-sayari/CLAUDE.md:38`), not the filing's "read-only" misreading.

**Out of scope (per-site).** The human-zone enumeration (`:64`, "Three top-level folders are
human-only") is a **deliberately closed, module-defined** boundary (`_vault/`, `new/`, `daily/`)
— not vault-extensible, not filed, not touched.

## Registration

**None.** Every edit is a convention-registry / governance-check / operating-contract change:
- No new skill, no new workflow, no `module-help.csv` row.
- **No `spec.md` version bump** ⇒ **no consumer walk / re-ack** of the pre-existing consumers
  (disposition 6). The two new `depends_on: ["spec@1"]` acks (`vlt-upgrade`, `vlt-lint`) are
  *registrations of existing consumption*, not re-acks of a moved version.
- The operating contract is un-handshaked (no `version:`/`consumers:`) — F3/F4 register nothing.

## Out of scope (dispositioned)

- **The adoption / first-instance frontmatter facet** (A3-12's strongest point,
  `frontmatter.md:216-231`) — **deferred to build-20** (per the build-17 rescope ruling,
  roadmap `:1631`: "adoption facet → build-20's schema bump"). Build-19 touches no
  `frontmatter.md` enforcement facet.
- **The two deferred `spec.md` lint checks** (`spec_schema_violation`,
  `spec_notification_missing`) — **remain deferred** (`spec.md:80` tripwire; promotion trigger =
  a `version` bump shipping without relay entries). Only the `spec_candidate` advocacy check
  lands.
- **An author-a-spec `vlt-mint` kind** — **rejected.** Origination stays human-gated at two
  cadences (upgrade retrofit + lint surfacing); `vlt-mint:11`'s kind list gains nothing, and the
  consumer lock (`vlt-mint:108`) remains the only mint-side spec contact.
- **build-15's consumer-lock / spec-bump acceptance tail** — **attached to no build** (roadmap
  evidence-debt disposition `:1713`): its discharging event is "the first real spec minted in a
  live vault, non-vacuously per gate 2." Build-19 improves the odds (a faster-clock advocate)
  but **cannot cause** that event — do not treat F2 as discharging it.
- **`vlt-dispatch`** — already acks `spec@1` (`vlt-dispatch:2`) and its firewall
  (`vlt-dispatch:41`, relay "never authors" specs) is preserved unchanged; no edit.
- **The human-zone enumeration** (`contract:64`) — deliberately closed; not touched (F4 note).

## Verification (unit, at rest — lifecycle step 5)

- **Handshake bipartite re-check.** After F1+F2, `spec.md:12` = `[vlt-mint, vlt-dispatch,
  vlt-upgrade, vlt-lint]`; confirm each of the four carries `spec@1` in `depends_on`
  (`vlt-mint:2`, `vlt-dispatch:2` unchanged; `vlt-upgrade` and `vlt-lint` newly added). Grep
  `grep -rn "spec@" skills/*/SKILL.md` → exactly four acks, all `spec@1`. `spec.md` still
  `version: 1` (no bump). This should leave `vlt-lint`'s own convention-coherence check
  (`vlt-lint:74`) reporting **zero** findings for `spec` — walk it by hand against the four
  consumers to confirm no unacknowledged/stale/dangling entry.
- **Single-home for the heuristic.** Grep that the spec-candidate signal wording ("revised in
  place / ≥2 relay entries … same path") is defined once and pointed at, not triplicated — the
  new `vlt-lint` bullet should reference `{conventions}/spec.md` and the `vlt-upgrade:75`
  detection, not restate a fourth divergent phrasing.
- **Contract map.** `specs` row present at `contract:29-44` with its semantic description; the
  SSoT-mirror note present; `{specs}` at `:227` still resolves against the new row. `last_updated`
  = 2026-07-17.
- **Tool-zone reframe.** No "two top-level folders" closed enumeration remains at `:79-81`; the
  boundary rule reads "not a content layer"; `dev/` appears only as a generic example (no
  vault-local path; grep the changed contract for `sayari` → zero).
- **spec.md enforcement prose.** The "When they land …" clause updated to reflect `vlt-lint`
  joining now for `spec_candidate`; the notification deferral + `enforcement_stage: declared`
  frontmatter UNCHANGED; run `vlt-lint`'s enforcement-doctrine meta-check (`vlt-lint:75`) by
  inspection → `spec.md` still valid (complete tripwired deferral present).
- **node --check** is not required (no workflow edited).
- **Packaging lint.** `uv run tools/package-lint.py` → A/B/C PASS (D / `--expect-version` is the
  release gate, not per-build).
- **Scrub.** No personal / vault-local content in any changed shipped file; worked examples use
  placeholder paths (the `dev/` example and `{specs}/{date}-{owner}-to-{consumer}-{slug}.md`
  style stay generic).
- **Not a release build.** Versions remain `0.6.0` in both strings; the bump to the next version
  rides the release build of this arc's next version, not build-19.

## Release

Not a release build — omitted. Build-19 opens the next version's work; the dual version bump
(`.claude-plugin/marketplace.json` `"version"` + `vlt-setup/assets/module.yaml` `module_version`)
and the pre-tag `uv run tools/package-lint.py --expect-version X.Y.Z` gate ride the release
build at the end of the arc's next version, per the release choreography.

## Acceptance (live — appended to the roadmap ledger)

Rides the next ordinary vlt-core (and/or vlt-sayari) upgrade:

- **Spec-candidate surfacing works in anger.** The next lint run on a vault with a spec-shaped
  handoff (revised in place, or ≥2 relay pointers at one path) surfaces it as a `spec_candidate`
  — human-gated, filed to the backlog / flagged, **never auto-promoted**; a lint run on a vault
  with an empty `_agent/handoffs/` (or empty `_agent/specs/`) produces **no `spec_candidate`
  finding and no zero-specs alarm**. Steady-state advocacy now fires at lint cadence, not only at
  upgrade cadence.
- **Coherence converges on the new consumers.** Post-upgrade `vlt-lint` convention-coherence
  reports **zero** findings for `spec` — all four consumers (`vlt-mint`, `vlt-dispatch`,
  `vlt-upgrade`, `vlt-lint`) ack the current `spec@1`; no unacknowledged/stale/dangling entry
  (`vlt-upgrade` no longer drifts silently).
- **The contract map shows `specs`.** After the governance refresh, the operating contract's
  structure-map table carries the `specs` row with its semantic description; a partner (or a
  generic agent entering via the vault's `CLAUDE.md`) reading the contract can resolve `{specs}`
  from the table; the SSoT-mirror note is present.
- **Tool-zone reframe visible + non-regressing.** The contract's tool-zone prose reads as an
  extensible "not a content layer" class; a vault carrying its own tool tree (e.g. a `dev/`
  working tree) is **not** treated as vault content by `vlt-lint` or the partners (no
  ingest/lint/extract into it), and the field pattern the filing described is now covered by the
  contract rather than contradicted by it.
- **No discharge of the build-15 first-exercise tail.** This build must not be read as
  discharging the consumer-lock / spec-bump-relay tail (that needs a real spec minted
  non-vacuously per gate 2) — record only the advocacy/registration/map outcomes here.
