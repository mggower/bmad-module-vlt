# Principal-engineer handoff — vlt module & lifecycle

**Date:** 2026-07-12 · **Repo state:** `main` @ `a117f4f`, v0.6.0 tagged & pushed
**Field state:** vlt-core at 0.6.0 (upgraded 2026-07-08), byte-identical to repo HEAD

This is the synthesis. The raw evidence lives beside it and every claim below is
grounded there — read those before overruling anything here:

- `01-lifecycle-archaeology.md` — the loop as practiced; fossil record of every standing rule
- `02-module-map.md` — the full shipped surface, handshake verification, weak points
- `03-field-inspection-vlt-core.md` — read-only inspection of the live vault
- `04-open-threads.md` — release state, ledgers, watch items, owner rulings (verbatim)
- `05-field-inspection-vlt-sayari.md` — second-vault inspection (added later on 2026-07-12;
  **materially revises §2.1/§2.2 — read the Addendum at the end of this doc**)
- `briefs/` — build briefs for the four factory lifecycle skills (§1.2) + the vlt-core
  inbox-rail capability

---

## 0. The one thing the dossiers disagreed on (read this first)

The roadmap, project memory, and open-threads sweep all say Arc 3 acceptance is
"pending the vlt-core upgrade." **The field inspection shows the upgrade already ran on
2026-07-08** (`_agent/upgrade-ledger.md` top entry: `vlt 0.5.0 → 0.6.0 (own)`; skills
byte-identical to HEAD; spec.md + write-verification.md seeded; `.skill-manifest`
written; `_agent/specs/` created).

So the truth is: **the upgrade ran, but the acceptance bookkeeping never did.** Nobody
walked the vlt-core ledger evidence back onto the Arc 3 roadmap's checkboxes, ticked
them, archived the six 091001–091006 filings, closed the arc, or synced memory. This is
not a trivia point — it is a *live demonstration* of the central lifecycle finding in
§2: the steps that are pure discipline are the steps that silently don't happen. The
factory's own doctrine ("a boundary without a bell doesn't exist") applies: acceptance
discharge is a boundary with no bell, and it just failed quietly.

**First task for a successor:** run acceptance discharge against vlt-core's 0.6.0
ledger entry + the on-disk evidence in `03-field-inspection-vlt-core.md`, tick the Arc 3
ledger, archive accepted filings, close or explicitly hold the arc, sync memory.
Most checks look dischargeable from what the field inspection saw (manifest seeded,
conventions seeded from shipped text, exclusion pass clean, csv canonical); the ones
that need *first-exercise* evidence (spec consumer lock at next mint, flood-free first
lint, subsumption offer, track loop) stay open honestly.

---

## Domain 1 — The lifecycle

### 1.1 What the loop is and why it's shaped this way

Seven steps: **field notes (`inbox/`) → capture (arc roadmap) → ideate (owner rulings +
spikes) → brief (`build-N-*.md`) → build (one commit each) → release (lint-gated tag) →
live acceptance (owner-run upgrade, ledger discharge)**. Three arcs have run it
(builds 3–18, v0.4.0 → v0.6.0). Full step-by-step anatomy in `01-…` §1.

What I've learned, distilled:

1. **Filings lie; grounding is the load-bearing step.** Filings mis-attributed
   provenance, guessed wrong fixes, and reported already-shipped work as missing, in
   *every* arc (filing #1, #7, R2-1, Arc 2's installer hypothesis, Arc 3's A3-3 —
   catalog in `01-…` §2). Grounding-before-capture is why `inbox-capture` became the
   first lifecycle skill. Never capture a claim you haven't re-verified against source.

2. **Reading the actual external source beats reasoning from docs/memory, every time
   it's been tried.** Three spikes, three refutations of the prior hypothesis (installer
   resolver, Bases `today()` — `01-…` §1 step 3). Keep the spike-before-brief rule hard.

3. **Every standing rule is a scar, not a preference.** The fossil record (`01-…` §2)
   traces each CLAUDE.md rule to a specific documented failure — governance SSoT to the
   build-5 dual-tree divergence, no-`.decision-log` to a live-vault clobber, the lint to
   three consecutive tags shipping packaging defects. Corollary for successors: don't
   relax a rule without reading its origin, and when something new bites, mint the rule
   *and record the bite* — the tracing is what keeps rules honest later.

4. **The loop improves by dogfooding its own diagnosis.** Arc 3's thesis about the
   vault ("state lives in prose, so nothing can count, trigger, or trip") was applied to
   the factory itself: CLAUDE.md, the capture skill, and package-lint all landed in the
   same arc. The lifecycle and the module co-evolve; treat factory-process defects as
   filable signal just like vault defects (091002 was exactly that).

5. **Enforcement beats discipline, and the gradient shows.** The two mechanized points
   — capture (skill) and the release lint (script + PASS-line-in-commit) — have not
   failed since they landed. The purely disciplined steps are where the misses live:
   acceptance discharge just silently didn't happen (§0), inbox/README's own archive
   list has drifted (says 10, holds 15), and an Arc 1 roadmap once "simply never
   recorded" a shipped fix. Formalize where it has already bitten; the repo's
   defer-until-it-bites philosophy is right, and these steps *have bitten*.

### 1.2 Skills to build (formalizing the loop) — in priority order

Evidence for each ranking in `01-…` §4. Pattern to copy: `inbox-capture` (SKILL.md +
`references/` methodology + a named style precedent + headless mode with a JSON
completion contract).

1. **`acceptance-discharge`** — input: a vault's `_agent/upgrade-ledger.md` entry +
   on-disk evidence; output: ticked arc-ledger checkboxes with evidence citations,
   filings moved to `inbox/archive/`, arc closed (or held with named residuals), memory
   synced. *Justification: it just failed in production — see §0.* This is the highest-
   value, most mechanizable gap.

2. **`vlt-release`** — wraps the whole choreography: branch check → dual version bump →
   `uv run tools/package-lint.py --expect-version X.Y.Z` → PASS line into the release
   commit → ff-merge → tag → push. Nothing today forces the lint to run (no hook, no
   CI); only the PASS-line convention makes skipping visible *after the fact*. Every
   pre-lint tag (0.3.0–0.5.0) shipped a packaging defect. Bonus inside the same skill:
   the factory-side handshake bipartite check (today a hand grep ritual repeated in
   nearly every build record) and the 091002-Q4 registration of the lint as the release
   boundary's `checked_by` (ruled, never done).

3. **`build-brief`** — codify the converged brief shape: frontmatter
   (`derives_from`/`rulings`/`risk`), F-site grounding with `file:line`, brief-time
   dispositions citing the ideation rulings, deviation-recording in `status:`, and the
   append-acceptance-checks-to-ledger step (the step most likely to be forgotten,
   since it edits a *different* file).

4. **`arc-closeout`** — the multi-step archival ritual: discharge check, CLOSED banner,
   `git mv` roadmap+briefs to `archive/`, filing archival, memory sync, inbox/README
   update (or better: delete its completeness-claiming archive list — it's the exact
   drift class CLAUDE.md warns about).

5. **Leave ideation human-led** — but a light scaffold for *recording* rulings (the
   decide-once section shape, spike-obligation tracking) would help. Do not automate the
   decisions themselves; owner steering is a feature.

Also fix the structural gap the newest filings exposed: **the second consumer vault has
no inbox channel** (vlt-core files on its behalf). Before the graduation-queue work
lands — whose acceptance is explicitly assigned to that vault — define a filing rail
for non-primary vaults, even if it's just a documented relay convention.

### 1.3 The immediate queue (what's actually next)

Full inventory with verbatim ledger text in `04-…`. Priority order, corrected for §0:

1. **Discharge Arc 3 acceptance** against the already-run 0.6.0 upgrade (§0).
2. **Capture the two 2026-07-11 graduation-queue filings** (`04-…` §3b) — uncaptured,
   and the field-calibration filing materially rewrites the first filing's design
   (orphan projection ~79% false-positive as specced → union projection; `cluster_ripe`
   not viable on current topic data). Targets `frontmatter@4` with the parked 091006 v2
   keys — a natural bundle. Acceptance belongs on the work-machine vault.
3. **build-17 (enforcement kit)** — the brief was waiting on vault evidence, and the
   field inspection found it already exists: a live prototype at `_agent/`
   (`tripwires.yaml`, `vitals.sh`, `session-health-strip.sh` — one wire has fired and
   been cleared) plus `enforcement-kit-evidence.md`. Design rulings are locked
   (hooks home, lint/dispatch-find + tripwires-nag, derive-first). Verify the M0
   counter-accuracy numbers, then brief.
4. **Watch items:** vlt-track loop-profile (first post-upgrade track loop — 0.6.0 is
   installed, so the next track invocation is the test); owner files BMB `after,before`
   drift upstream to BMAD-METHOD; 091002 standing metric (zero packaging filings ≥ 0.6.0).

Standing constraints a successor must not trip: never push `full-history`; dev
artifacts stay gitignored; scrub personal content from anything shipped; derive-first
binds all Arc 3 enforcement work; closed roadmaps are read-only; don't re-litigate
rejected alternatives documented in filings.

---

## Domain 2 — The module

### 2.1 What is working well (field-proven)

Evidence in `03-…`; architecture in `02-…`.

- **The durability posture is the crown jewel, and it works.** Five clean upgrades,
  exactly one governance divergence ever (upstreamed and closed), and after the 0.6.0
  own-the-apply the installed skills are **byte-identical to repo HEAD** with all three
  minted partners, their capabilities, and their registry rows intact. Merge-not-replace,
  `.baseline/` divergence detection, the B1 CSV preserve path, and the append-only
  upgrade ledger are field-proven. Protect this above everything.

- **Real, heavy, current use.** 201 log entries over ~5 weeks, 82 sessions, 124 wiki
  pages + 90 research notes, 63 drained dispatch items, 7 cross-partner handoffs, 3
  minted partners, 3 light capabilities (incl. `ingest-youtube` with a scripts/ sibling
  — the 0.5.0 shape exercised in anger). The core loop — ingest → wiki → lint →
  extract, fronted by partners, routed by dispatch — is not a demo; it runs daily.

- **Single-writer lanes + single-home-with-pointers hold up.** The who-writes-what
  table (`02-…` §6) is respected on disk; no lane violations found in the field. The
  handshake is **fully bipartite-consistent** at 0.6.0 (verified both directions,
  `02-…` §2.4).

- **The self-evolution rail is real.** The vault prototyped the enforcement kit
  locally, the artifacts became inbox filings, filings became builds. The
  local-prototype → filing → module-source → upgrade round trip (build-18 closed the
  overlay return leg) is the module's most distinctive property.

- **Scoped-by-default + honest coverage reporting** (lint's `coverage_caps`,
  `files_checked` vs `files_listed`, D-check "SKIPPED not PASS") — a consistent honesty
  idiom worth preserving in everything new.

### 2.2 Weaknesses (each with its evidence)

1. **Prose where a script should be.** The build-18 SHA-256 `.skill-manifest` is
   written and verified by LLM-followed instructions — no script computes or checks the
   hashes (`02-…` §5.6). vlt-upgrade's only scripted step is the CSV merge; snapshot,
   merge-copy exclusions, baseline refresh, and subsumption diff all ride on per-run
   execution fidelity. The hash-exact durability net is only as strong as a transcription.

2. **Convention-to-convention drift is invisible to the handshake.**
   `wiki-consolidation.md:116-118` still instructs index counts/dates/descriptions that
   wiki-index@2 abolished — a real doc bug the coherence check structurally cannot
   catch (it walks consumer *skills*, not cross-convention text). Same class: the
   operating contract's structure-map table omits `specs`, and its Reading list omits
   the two build-15/16 conventions — the repo's own "complete lists drift" failure mode,
   in the constitution itself (`02-…` §5.1–5.3). Fix the three instances; consider a
   lint heuristic for the class.

3. **Shipped-but-never-exercised machinery is accumulating.** Capability families
   (since 0.3.0: zero uses), vlt-track loop profiles (zero), convention overlays (never
   created — good news, but overlay-lift/subsumption have never run against real
   divergence), personalized-extraction firewall (dormant until a vertical partner
   wears track), `cleanup-legacy.py` (dead by policy). Each unexercised path is
   untested risk wearing a feature's clothes. Ruling needed per item: exercise it
   deliberately, or prune it.

4. **Two version registries in the vault disagree.** `_bmad/_config/manifest.yaml`
   still says vlt 0.4.0 while the vault runs 0.6.0 — own-the-apply never touches the
   installer-side manifest (`03-…` §1). Anything reading that file (installer,
   bmad-help) sees a stale version. Decide: own-the-apply bumps it, or document the
   discrepancy as intended.

5. **vlt-query sits outside the attestation perimeter.** It can file research notes but
   isn't a legal `verified_by` value, has no verify step, no `depends_on` — its notes
   are born unattested by construction (`02-…` §5.7). Probably a one-build fix; decide
   whether the narrow perimeter is intentional and write the answer down either way.

6. **Adoption of the new enforcement surfaces is thin, which is expected but must be
   watched.** Attestation on 37/124 wiki pages, `review_after` on 1/124, `_agent/specs/`
   empty (the spec convention is seeded but has never been exercised — the consumer-lock
   and relay-per-bump paths are untested in the field). The rollout is
   organic-on-touch by design; the risk is declaring victory on machinery whose main
   paths haven't fired. The `declared`-stage tripwires (spec@1, wiki-consolidation@1,
   review_after 2026-08-17) are the scheduled check-ins — honor them.

7. **Small cruft, cheap to fix:** stale vlt-mint row in `module-help.csv` (pre-build-7
   kind vocabulary); README's Updating section recommends the destructive installer
   path without mentioning vlt-upgrade; README:216 registry contradiction; 📖/📚 icon
   mismatch; in the vault, one iCloud conflicted-copy session file and a 3-byte
   `Untitled.md` (`02-…` §5.9, `03-…` §7).

### 2.3 What I want built after I'm gone

In order:

1. **build-17, the enforcement kit** — the field has already voted with a working
   prototype. This completes Arc 3's thesis (derive-first vitals, tripwires that nag,
   hooks provisioning) and gives every future `declared` deferral a real bell. It also
   unlocks `enforcement_counter` and makes the doctrine self-hosting.

2. **Script the durability net.** A `verify-skill-manifest.py` (compute + diff SHA-256s)
   and ideally a scripted own-the-apply copy step with the exclusion list baked in.
   This is the single cheapest reliability win: it converts the module's most important
   guarantee from prose to code. Ship it inside vlt-setup/scripts so both setup and
   upgrade call it.

3. **The graduation queue (`frontmatter@4`)** — but built to the *calibrated* design
   from the 07-11 field audit (union projection, `revisit_after` + `linkage_ripe`
   first, `cluster_ripe` gated behind topic normalization), bundled with the parked
   091006 v2 keys, accepted on the work-machine vault. Prerequisite: the second-vault
   inbox rail (§1.2).

4. **Exercise-or-prune the dormant machinery.** The write-verification family invariant
   (deferred "after M4") is the designated first real family — build it and the family
   machinery earns its keep; otherwise prune. Same ruling for loop profiles at the next
   track loop, and for `cleanup-legacy.py`.

5. **First real spec.** The next cross-partner durable doc on vlt-core should be minted
   as a spec (the convention is seeded; `_agent/specs/` is empty). Until one exists with
   a version bump and consumer relays, build-15 is unproven. The proto-spec retrofit of
   the 7 existing handoffs is the natural candidate.

6. **Close the doc-drift class** (§2.2.2's three instances) and the perimeter question
   (vlt-query), in one small hygiene build.

### 2.4 Beware-list for successors (the rules, with their reasons)

Restated from the fossil record so they read as engineering, not superstition:

- **One governance home** — a second copy diverged silently once, mid-build, in the
  very machinery meant to prevent divergence. Grep before you create.
- **Rule change → version bump → walk every consumer, same build** — drift sat latent
  through a whole migration once; the handshake exists because of it. Prose
  clarifications don't bump.
- **The working tree ships, not the git index** — own-the-apply is a filesystem copy.
  This is why `.decision-log.md` files are deleted (one clobbered a live vault), why
  the lint checks the disk, and why root `.DS_Store` matters.
- **Always quote free-text CSV fields** — two unquoted commas once aborted an entire
  upgrade's registration step before the local-mint preserve ran.
- **Parse `args` on intake in every workflow** — the runtime delivers it as a JSON
  string; the un-parsed string once made every gated mint fail on first try and the
  filing's own diagnosis of it was wrong.
- **Placeholder paths in shipped examples** — a vault-side file move strands the
  module's own docs; live-path examples are couplings.
- **Never "fix" module bugs in a vault; never treat vault growth as module source** —
  the factory/field boundary is the whole design. And `.claude/skills/bmad-*` is
  upstream's; file, don't patch.
- **When touching setup/upgrade/merge scripts, re-verify the B1 preserve path** — it's
  the line between "upgrade" and "destroying a user's minted partners."

---

*Everything above is grounded in the four dossiers in this folder; where they disagreed
(§0) the on-disk evidence won. This folder lives in gitignored `skills/reports/` and
will not ship.*

---

## Addendum (2026-07-12, later the same day) — the vlt-sayari inspection

The owner synced the work vault ("vlt-sayari") onto this machine and a fifth dossier
(`05-field-inspection-vlt-sayari.md`) inspected it. Caveat baked into that dossier:
Obsidian Sync drops hidden folders and most non-markdown files, so `.claude/`,
`_bmad/` file contents (including `module-help.csv`), and `.baseline/` are
*unverifiable in the snapshot*, not missing — re-check them on the work machine itself.
What the inspection changes:

**§2.2.3 ("dormant machinery") is largely retired.** vlt-sayari, at 0.6.0 via a
0.4.0→0.6.0 jump on 2026-07-09, has field-exercised nearly everything vlt-core never
touched: a **live capability family** (`project-hub`, 2 instances), a **live convention
overlay** (extraction, ~270 lines, including a council-gated edit and a real
subsumption pass at upgrade), **loop profiles** (Navigator's `track.md` carries a full
profile — this discharges the *machinery half* of the Arc-1 loop-profile watch item;
the *vlt-core wearer half* stays open, since Dog Trainer/Health Coach still carry zero
profiles and their first post-upgrade track loop remains the untested event), a **skill
retirement** (`vlt-spec-external`, 06-30), **personalized extraction** (2 named
opt-ins), the CSV header migration on the jump path, and a proto-spec retrofit
offer correctly declined. Between the two vaults almost every shipped mechanism now has
field evidence. The 07-09 upgrade-ledger entry — jump + 3 mints preserved + overlay
subsumption + migration + retrofit-offer in one run, zero destruction — is arguably the
module's best single piece of field validation. The **one shared zero remains the spec
convention**: zero specs in both vaults (`_agent/specs/` doesn't even exist in
vlt-sayari), so §2.3 item 5 (first real spec) rises in priority.

**The graduation-queue design gets its second calibration, and it reframes the
problem.** Per-note orphaning is NOT the work vault's pathology either: naive
frontmatter-only projection says 9/13 notes (69%) orphaned; the calibration filing's
union projection collapses that to **3/13 (23%)**, one of which is a documented
deliberate island — the union shape is now validated on both vaults. The real
starvation is one level up: **wiki-graduation throughput** (29 of 34 pages are the
06-24/25 migration burst; only 5 new pages in 17 days against ~156 ops and 94
sessions) and **librarian-side drain latency** (4 open ingest relays 12–15 days old;
oldest open pointer 16 days; no lint since 07-02). And the graduation-ripe knowledge
lives in **handoffs (27), partner threads, and project status files at least as much as
in `_agent/research/`** — a detector scoped to the research zone alone misses most of
what's stranded there. The `topic:` normalization prerequisite for `cluster_ripe`
reproduces on this vault too. The frontmatter@4 capture run must fold this in alongside
the two 07-11 filings; acceptance measures should be drain latency and non-research
strandings, not just note citation coverage.

**Durability notes for the next vlt-sayari upgrade.** The 07-09 ledger's inventory is
already stale — `vlt-hub`, `dev-loop`, `codebase-backlog`, `project-synthesis`, and the
`project-hub` family all post-date it — so the preserve pass must derive its set from
disk, never from the previous ledger entry (derive-first, applied to upgrades). New
durability shapes vlt-core doesn't have: vault-root `DESIGN.md`/`PRODUCT.md` and a
grown `CLAUDE.md ## Local zones` section (the `dev/` zone — which the vault's backlog
wants graduated upstream into the shipped operating contract, a real inbox candidate
for the rail once it exists).

**Two vaults, two animals, one module.** vlt-core is librarian-centric personal
knowledge; vlt-sayari is navigator/engineer-centric development support (36 dispatch
relays, 27 handoffs, 11 codebase maps, 5 dev-loop runs, real Jira traffic, denser use
at ~10 ops/day). Same contract, opposite center of gravity — the strongest evidence yet
that the partner/capability model generalizes.

**The sayari signal has been filed into the inbox** (2026-07-12, on the vault's behalf
— it will never have inbox access, so its module signal is relayed the moment it's
found rather than parked here):

- `inbox/2026-07-12-114837-graduation-queue-sayari-calibration.md` — second
  calibration; capture together with the two 07-11 filings.
- `inbox/2026-07-12-114910-dev-zone-contract-graduation.md` — candidate: `dev/` zone
  into the shipped operating contract.
- `inbox/2026-07-12-114940-sayari-060-upgrade-field-evidence.md` — acceptance/
  validation evidence (jump upgrade, families/overlays/profiles/retirement first
  exercises) + the loop-profile half-discharge nuance + the derive-preserve-set-from-
  disk watch note.

Everything else sayari-flavored in the 05 dossier is vault-local work (open relay
drain, duplicate PDF, lint cadence, moot-pointer retirement) — deliberately NOT filed;
it belongs to the vault's own backlog, not the module inbox.
