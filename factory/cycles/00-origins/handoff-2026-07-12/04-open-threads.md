# Open Threads — raw findings (handoff 2026-07-12)

Scope: every in-flight, promised-but-unbuilt, awaiting-acceptance, or watched item in the
`vlt` factory repo. Sources: git state (verified live 2026-07-12), Claude project memory
topic files, `skills/reports/inbox-evolution-arc3-roadmap.md`, live `inbox/` filings,
build briefs' `status:` fields, archived roadmaps.

---

## 1. Release state (verified against live git, 2026-07-12)

**v0.6.0 is fully SHIPPED — committed, tagged, pushed. It is NOT yet field-accepted.**

- Tags on repo: `v0.3.0 v0.3.1 v0.4.0 v0.5.0 v0.6.0`. Current branch: `main`, clean tree.
- `main` HEAD = `a117f4f` "vlt 0.6.0 — Arc 3: the enforcement arc (builds 14+15+16+18)".
  Build commits on `arc3-v0.6.0` (branch still exists locally, ff-merged):
  `8c21736` build-14, `3795d86` build-15, `1142fb4` build-16, `2b79e89` build-18.
- Roadmap `status:` frontmatter (`skills/reports/inbox-evolution-arc3-roadmap.md:3`),
  verbatim: *"open (acceptance pending) — v0.6.0 SHIPPED 2026-07-08: builds 14+15+16+18
  committed on arc3-v0.6.0, ff-merged to main (@ a117f4f), tagged v0.6.0, pushed to
  origin. Pre-tag package-lint --expect-version 0.6.0 → A/B/C/D PASS. Acceptance rides
  the next vlt-core upgrade (owner runs it — see ledger). build-17 (enforcement kit)
  brief when its vault-side evidence matures (trails into 0.6.x/0.7.0)"*
- So: **version bump done** (both strings, per release commit), **pre-tag lint gate RUN and
  PASSED** (A/B/C/D, PASS line recorded in the release commit per roadmap :654-657),
  **tag pushed to origin** (github.com/mggower/bmad-module-vlt).
- **vlt-core has NOT been upgraded to 0.6.0 yet.** Everything in the Arc 3 acceptance
  ledger (§2 below) is waiting on that owner-run `vlt-upgrade`. Arc 3 stays OPEN until it
  runs and the checks pass. The six 2026-07-06 filings correspondingly remain in `inbox/`
  (not archived) — per lifecycle rule, a filing archives only after its build ships AND
  passes acceptance.
- Memory file `vlt-arc3-roadmap.md` agrees exactly with the roadmap doc (shipped
  2026-07-08, acceptance pending, build-17 trails). No contradiction.

**Immediate hard gate riding on that upgrade (vault-side, pre-existing):** build-15's
`status:` — *"Hard gate still stands vault-side: no new partner mint on vlt-core before
the convention is in place there"* — and vlt-core must mint its `spec.md` **FROM the
shipped text** so the divergence check self-clears (build-15 status, note 1: the vault-side
mint had NOT happened as of 2026-07-06; no `_meta/conventions/spec.md` or `_agent/specs/`
existed in vlt-core).

---

## 2. Pending acceptance checks — Arc 3 "Deferred acceptance ledger", verbatim

From `skills/reports/inbox-evolution-arc3-roadmap.md:576-622`. All unchecked. Acceptance
rides the next ordinary vlt-core upgrade (owner runs it).

- [ ] **(carried from Arc 1/2, STILL OPEN)** vlt-track loop-profile watch item: first
  post-0.4.0-upgrade track loop on vlt-core's vertical partners may not find the inline
  loop profile → if it breaks, build-11 field defect → inbox.
- [ ] **(owner action, carried from Arc 2)** file the bmad-module-builder template drift
  (`after,before` in template merge script + tests) upstream to BMAD-METHOD.
- [ ] **091002 success metric (standing, not one-shot):** zero packaging filings into
  `inbox/` for releases ≥ 0.6.0; the 0.6.0 upgrade-ledger entry on vlt-core is the
  regression probe (exclusion pass finds nothing; CSV canonical; module.yaml resolves).
- [ ] **build-14 (packaging lint, briefed 2026-07-06):** factory-side — the 0.6.0 tag is
  cut only after `uv run tools/package-lint.py --expect-version 0.6.0` exits 0, PASS line
  recorded in the release commit; field-side — vlt-core's 0.6.0 own-the-apply runs the
  **widened** exclusion list from `vlt-upgrade/SKILL.md` text (not session practice).
  *(Factory half DISCHARGED at the 2026-07-08 tag; field half pending.)*
- [ ] **build-15 (spec convention, briefed 2026-07-06):** hard gate honored — next vlt-core
  partner mint happens only with the convention in place and exercises the consumer lock
  (days-to-first-check = 0 for that boundary); 0.6.0 upgrade — skip-if-present preserves
  vlt-core's minted `spec.md` base, baseline stash gains the shipped stock, `config.yaml`
  gains `specs:` via provision, divergence report clean or example-only; migration offer
  human-gated + idempotent (stub at old path, open pointers re-pointed, `migrations_run:`
  records it); a live spec version bump produces one relay per listed consumer with the
  `_agent/specs/` path accepted.
- [ ] **build-16 (frontmatter@3, briefed 2026-07-06):** 0.6.0 upgrade — consumer walk
  converges on vlt-core (post-upgrade lint: zero coherence findings; five skills at
  `frontmatter@3`, four at `write-verification@1`); first post-upgrade lint run is
  flood-free on the legacy corpus (`unattested_write` informational-only pre-convention,
  `review_due` only where set, `para_missing_attestation` true-positive only); next
  boundary-creating mint has days-to-first-check = 0 and zero conventions sit `declared`
  untripwired; local base stamps/overlays converge (with build-18's subsumption retire).
  Pending attachments: 091005 M4 two measured lint cycles; 091006 first review-cycle
  evidence.
- [ ] **build-18 (durability cluster, briefed 2026-07-08):** 0.6.0 upgrade on vlt-core —
  F2 subsumption pass offers vlt-core's `review_after` overlay section for retirement
  (`overlay-subsumption` in `migrations_run`), shadow gone, lint clean; F1 skill-asset net
  seeds `.skill-manifest` (0.6.0 run reports `skill_manifest_missing` once, then clean) and a
  subsequent local `vlt-mint/assets/*` edit surfaces as `skill_asset_divergence` on the next
  upgrade, not a silent clobber; F3 first post-upgrade write op honors an overlaid convention
  rule without a manual reminder; F4 next relocation migration leaves a stub, touches no
  worktree copy, re-points open pointers; F5 standing — no future shipped worked example
  couples to a live artifact path (0.6.0 shipped surface is the clean baseline).
- [ ] **Design-stage evidence debts (vault-side, before their builds close acceptance):**
  091003 M0 counter-accuracy audit + tripwire-hit data; 091005 two measured lint cycles
  under the attestation contract (M4); 091006 first review-cycle evidence (does the
  due-queue get worked). Filed as pending attachments by the filings themselves.

---

## 3. Deferred / unbuilt

### 3a. build-17 — enforcement kit, slices 0–3 (filing 091003). BRIEF NOT WRITTEN.

- Roadmap grouping table (:500): *"build-17 — enforcement kit (slices 0–3) | The
  substrate | 091003 (vitals + tripwires + hooks provisioning + dispatch Tripped-wires +
  mint/council wire rule + `blocked_on` rider + contract grammar tighten) | Depends on
  build-16's vocabulary decisions (metric ids, `review_after`) and the hooks-home ruling;
  vault-side slices 0–3 evidence may still be maturing. Last, and can trail the 0.6.0
  release if its evidence isn't in."*
- Ruled (Ideation rulings): trails into **0.6.x/0.7.0**; brief written only *"when its
  vault-side evidence matures"*.
- **What evidence is awaited:** 091003 is a design-stage filing — vault-side measurement
  numbers from vlt-core are pending: the **M0 counter-accuracy audit + tripwire-hit
  data** (ledger item, last bullet), plus roadmap A3-3 grounding note (:244-246): the
  filing's vault-side probe numbers *"(175/184 grammar conformance, the 4-pointer board,
  the six-week-old pointer) are vault-local probes — re-verify in vlt-core before the M0
  audit closes."* Filing 091003 itself was *"filed ahead of its plan's slice-5 evidence
  at owner request."*
- Design already locked for build-17 (decide-once rulings, roadmap :533-548): hooks home
  = `{root}/.claude/hooks/` (module owns, overwrites); "lint/dispatch find, tripwires
  nag"; lint attests narrowly; `_agent/dispatch.md` hardcoded read accepted. Brief-time
  questions reserved: `days_since_lint` display-only?, `blocked_on` shape.
- Arc-wide standing law binding it: **derive-first — no mutable stored counters, ever**
  (derived or append-only only); `review_after` defined once (091006); metric vocabulary
  defined once (091003's ids). *"Any build in this arc proposing a stored counter is
  wrong by ruling, not by taste."* (roadmap :455-456)

### 3b. TWO LIVE, UNCAPTURED inbox filings (2026-07-11) — the graduation queue

Neither appears anywhere in the Arc 3 roadmap (grep for graduation/revisit_after/114226
returns only the unrelated `frontmatter@4` parking note). **Capture has not run on them.**
They arrived after the 0.6.0 ship and are the seed of the next build cycle (likely a
`frontmatter@4` build or Arc 4).

1. `inbox/2026-07-11-114226-research-note-graduation-queue.md` — design-stage proposal,
   filed at owner request; owner's stated intent is *"to build this at the module source
   directly."* Proposes `frontmatter@4`: two optional research-note keys
   (`revisit_after: YYYY-MM-DD` deferral/snooze; `ingest: exempt` terminal opt-out),
   a computed orphan projection (reverse index over wiki `sources:`), three lint findings
   (`revisit_due`, `cluster_ripe` K=3, `linkage_ripe`) as a Graduation Queue under
   `flag_for_human`, consumer walk bumps on vlt-lint/vlt-research/vlt-ingest (+ optional
   vlt-dispatch ledger line), workflow reducer-stage computation for cross-page signals,
   no shipped `.base` (mirrors the 091006 owner ruling). Rejected alternatives documented
   (auto-ingest, revisit-only, status-overload, sidecar file, embeddings — don't
   re-litigate). v2 parked: `revisit_when:` free-text, fuzzy topic matching.
2. `inbox/2026-07-11-153000-graduation-queue-field-calibration.md` — supplements (not
   supersedes) 114226 with a full 90-note × 123-page vlt-core audit ("Slice 0 executed
   plus the first manual drain"). **Materially changes the design:**
   - The specced orphan projection is **~79% false-positive** (62/90 flagged, 49 absorbed)
     → must ship as a **union**: frontmatter citation ∪ body wikilinks ∪ shared-source
     overlap (residual ~13 notes, contains every genuine gap).
   - `cluster_ripe` **not viable** on current `topic:` data (four serialization styles,
     vocabulary drift/collision) → ship `revisit_after` + `linkage_ripe` first; gate
     `cluster_ripe` behind a documented normalization rule. Resolves 114226's open Q2.
   - K-threshold accretion was NOT the observed gap pattern; actual signal yield order:
     date-ordering tell, bundled-note residue (partial ingestion outnumbered orphaning
     8:5 — ingest-probe should be per-source/per-section), fan-out droppage, explicit
     deferral markers in page prose, declared-connection diff.
   - Exempt backfill tiny (1/90 terminal).
   - **Calibration caveat carried:** vlt-core is the benign low-orphaning case; the
     owner's second vault (work machine) is where the real pathology lives and *"the
     mechanism's acceptance run should happen there, not here"* — that vault has no
     inbox access, so this filing carries its signal.

### 3c. Other roadmapped-but-unbuilt / parked

- **Parked to `frontmatter@4` "against usage evidence"** (roadmap :439-440, build-16
  brief item 13): 091006 v2 keys `source_type:`, `review_note:`. The graduation-queue
  filings now target the same bump — natural bundling candidate.
- **Family-invariant encoding of "write ops verify and attest own output"** — deferred
  "after M4" (091005 Q5; ideation rulings :573). Would be the first exercise of build-7's
  shipped-but-unexercised family machinery. Also listed in build-18 brief :258
  out-of-scope block ("family-invariant / operating-contract bells, family write-op
  invariant, frontmatter@4").
- **091002 open Q4 (retroactive doctrine registration):** declare the packaging lint as
  the factory release boundary's `checked_by` once 091004 landed — making the module repo
  the doctrine's first fully `checked` boundary. 091004 has landed (build-16); this
  registration hasn't been done anywhere findable.
- **Carried open design questions** (deliberately unresolved, roadmap A3-1 :135-142 etc.):
  carried-flag scheduling (build-15/17 seam); does the spec class generalize to
  "contracts" (ruling: don't pre-generalize, test on a real second instance);
  spec-version-bump-without-relays escalation promotes lint/ledger enforcement to "next
  mint".
- **vlt-help capability — DEFERRED indefinitely** (owner, 2026-06-25; arc1-history memory):
  tension with anti-menu philosophy; module-help.csv is a registration manifest, not
  runtime-read; no shape yet.
- **Arc 1 backlog tail never picked up** (identity-fork memory, "Other maintenance tail"):
  single-home the two module-help.csv + kind→council table, setup config-precedence +
  host-provided dep check, ingest research-note-handoff branch, partner-frontmatter
  coverage on research/session notes. (Some of these may have been absorbed by later
  builds — verify before acting; listed here because no record marks them done.)

---

## 4. Watch items

1. **vlt-track loop-profile watch (carried Arc 1 → 2 → 3, STILL OPEN).** Origin:
   arc1-history memory + archived arc2 roadmap :273 (*"carried from 0.4.0 watch item —
   STILL OPEN at arc close, carries forward past Arc 2"*). vlt-core's vertical partners
   (Dog Trainer / Health Coach) likely declare the vlt-track loop profile INLINE in
   SKILL.md while shipped vlt-track reads `capabilities/track.md` → first post-upgrade
   track loop may not find the profile = likely build-11 field defect; fix = per-wearer
   migration of the inline Loop-profile block; verify by running a real track loop +
   check whether B1 preserved vs shipped body won. Now item 1 of the Arc 3 ledger.
2. **BMB template drift upstream filing (OWNER ACTION, open since Arc 2).** The
   bmad-module-builder's own merge script + tests still carry the old `after,before` CSV
   header; verified present in latest upstream BMB cache, so upgrading installed BMB
   won't fix it. Must be filed upstream to BMAD-METHOD by the owner. Ledger item 2.
3. **Capability-family machinery: shipped-but-unexercised** (build-7, v0.3.0). Build-11
   explicitly ruled NO Model-B family for vlt-track; the first real exercise candidate is
   the write-verification family invariant (after M4). Memory `vlt-capability-object-design`
   + arc1-history.
4. **091002 standing success metric** (not one-shot): zero packaging filings into
   `inbox/` for releases ≥ 0.6.0 — every future release's vlt-core upgrade-ledger entry
   is a regression probe.
5. **Design-stage evidence debts** (ledger, last item): 091003 M0 audit, 091005 M4 two
   measured lint cycles, 091006 first review-cycle evidence — pending attachments the
   filings owe before their builds close acceptance.
6. **Second consumer vault (work machine)** — fresh install from public GitHub, has no
   inbox access; the graduation-queue mechanism's acceptance is explicitly assigned to it
   (153000 filing). Someone must carry signals to/from it manually.
7. **build-16 residual:** `vlt-lint-full.js` requires a `today:` arg (scripts have no
   clock — `Date.now()` throws in the runtime); absence reported as a coverage cap. Any
   future caller must pass it.
8. **Session-memory sync obligation** (CLAUDE.local.md): keep Claude project memory
   (`vlt-arc3-roadmap` et al.) in sync with the arc roadmap docs when builds/releases
   land. Currently in sync (see §6).

---

## 5. Owner rulings & decisions a successor must know

**Repo/publishing posture** (memory `vlt-published-to-github`, CLAUDE.md):
- Public at github.com/mggower/bmad-module-vlt; `main` = fresh clean public history.
  **`full-history` branch (30-commit dev history w/ personal vlt-core content) is
  local-only — NEVER push it.** Backup bundle:
  `~/develop/projects/vlt-full-dev-history-20260624.bundle`.
- Dev artifacts gitignored and untracked (`inbox/`, `skills/reports/`, `docs/`,
  `.claude/`, `_bmad/`, `CLAUDE.local.md`) — not version-controlled anywhere current.
- Shipped content must be scrubbed of personal/vault-local info; established neutral
  example vocabulary: coffee brewing, photosynthesis, spaced repetition, Language Tutor,
  home-energy-plan. Keep future governance edits neutral.
- Version lives in TWO files, bump together: `.claude-plugin/marketplace.json`
  `plugins[0].version` + `skills/vlt-setup/assets/module.yaml` `module_version`.

**Architecture rulings:**
- **No bespoke BMad** (memory `prefer-standard-bmad-no-bespoke`): install the standard
  BMad way, per-vault; vaults registry + `default_vault` indirection dropped; owner said
  "we don't need any bespoke approach." When unsure, pick the plain BMad convention.
- **Identity fork RESOLVED 2026-06-03** (memory `vlt-identity-fork-trial`): lean into
  the *ceremony* (real BMAD first-breath/rebirth lifted into activations), NOT six-file
  sanctum weight; 2-file identity/thread cut built bundled with it; mint loop verdict
  "cheap-good for hands, cheap-bad for people" → vlt-mint has a native partner-ideation
  beat decoupled from BMB; rebirth is partner-initiated (council gate stays).
- **Capability object** (build-7): owner declares only `write_scope`; weight/home/
  council-class derive. Light = own-zone partner file, council-none; heavy = registered
  op skill. Families = Model B thin invariants, opt-in.
- **Convention durability = append-only overlays** (owner idea, Phase D — supersedes
  3-way merge): base pristine, local edits in `_agent/conventions/{name}.overlay.md`,
  consumers merge on read; build-18 added the subsumption/retirement return leg.
- **vlt-upgrade prefers-to-own the apply** (merge-copy), degrades-to-bracket.
- **Arc 3 decide-once rulings** (binding, roadmap Ideation rulings section — briefs cite,
  never re-litigate): hooks at `{root}/.claude/hooks/`; lint/dispatch find + tripwires
  nag (one finder per fact, one nagger overall); lint attests narrowly (only files its
  auto-fix touched; `moment: lint run` real only once 091003's lint-debt wire lands);
  `_agent/dispatch.md` hardcoded read accepted; `tools/` tracked + public; attestation
  key is `verified_at:` (not `verified:` — trust-rung collision); ship NO `.base`
  (documented reference views use `and: [review_after, review_after <= today()]`,
  `date()` wrap as robust form — Bases spike CLOSED, `today()` is a function).
- **Standing arc law: derive-first** — no mutable stored counters, ever.
- **Lifecycle discipline** (CLAUDE.md): spike-before-brief for external unknowns; ground
  every filing claim against source at capture (filings mis-attribute); closed roadmaps
  are read-only; pre-tag `package-lint --expect-version` gate with PASS line in the
  release commit; one commit per build on an `arcN-vX.Y.Z` branch.

**Process facts:**
- vlt-core (`{field-vault}`) is a consumer install; the OWNER runs
  upgrades and acceptance. Module fixes ship only via `vlt-upgrade`, never edited in-vault.
- `.claude/skills/bmad-*` is upstream's — file defects to BMAD-METHOD, don't patch.
- Every workflow parses `args` as a possibly-JSON-string on intake (standing rule).
- Rejected alternatives documented in filings/pressure-tests are settled — don't
  re-litigate (091001's registry-file/overlay-only/defer-until-n=3; 114226's
  auto-ingest/status-overload/sidecar/embeddings; 091004's Warden partner; etc.).

---

## 6. Contradiction check: memory vs roadmap docs

Checked memory topic files against the live roadmap, briefs, and git. **No live
contradictions found.** Notes:

- `vlt-arc3-roadmap` memory ↔ roadmap doc ↔ git: all three agree (v0.6.0 shipped
  2026-07-08 @ a117f4f, tagged, pushed; acceptance pending; build-17 trails). In sync.
- MEMORY.md's arc3 line says "next = build-18 brief (owner returns)" then also records
  build-18 as built — internally slightly stale phrasing, but the topic file it points to
  is current; harmless.
- **One superseded note, already flagged in-source:** roadmap A3-6-LB1 says vlt-research
  is a frontmatter.md "non-consumer" (grounded at capture, v0.5.0) — build-16 made it a
  frontmatter@3 consumer, so it became overlay-blind and joined build-18's F3 fix. The
  supersession is recorded in the roadmap's own Status section (:650-652), the build-18
  brief status, and the arc3 memory. Consistent everywhere; just don't trust the :409
  capture-time sentence in isolation.
- Memory files carry v0.5.0-era `file:line` cites (e.g. `vlt-dispatch/SKILL.md:193`,
  `vlt-lint/SKILL.md:63`) — point-in-time; re-derive before use, per the memory system's
  own warning.
- Memory `vlt-capability-object-design` ends "Not yet built" — stale in isolation
  (build-7 shipped it), but the file's own description says "SHIPPED as build-7" and
  MEMORY.md's index line is correct. Cosmetic only.
- The two 2026-07-11 inbox filings appear in NO memory file and NO roadmap — this is a
  *gap*, not a contradiction: capture simply hasn't run since they were filed. It is the
  single largest un-tracked open thread.

---

## 7. One-screen open-threads inventory (priority order)

1. **Run the vlt-core 0.5.0→0.6.0 upgrade (owner)** — discharges the whole Arc 3
   acceptance ledger (§2); until then Arc 3 is open and the six 091001–091006 filings
   stay un-archived in `inbox/`.
2. **vlt-core must mint `spec.md` FROM the shipped text before its next partner mint**
   (build-15 hard gate, vault-side, still standing).
3. **Capture the two live 2026-07-11 graduation-queue filings** into a roadmap (new arc
   or 0.6.x cycle) — uncaptured, design materially recalibrated by the field audit,
   targets `frontmatter@4` alongside the parked 091006 v2 keys.
4. **build-17 (enforcement kit)** — brief when 091003's M0 counter-accuracy audit +
   tripwire-hit evidence arrives from vlt-core; design rulings already locked.
5. **vlt-track loop-profile watch** — verify on the first post-upgrade track loop.
6. **Owner action: file BMB `after,before` header drift upstream to BMAD-METHOD.**
7. Standing: 091002 zero-packaging-filings metric per release; design-stage evidence
   debts (091003 M0 / 091005 M4 / 091006 review-cycle); family machinery unexercised;
   work-machine vault has no inbox rail; keep project memory in sync with roadmap docs.
