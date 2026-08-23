# Field inspection — vlt-sayari (raw findings)

Handoff dossier section 05. Read-only inspection of the second consumer vault (the
owner's WORK-machine vault) at `~/Vaults/vlt-sayari`, 2026-07-12,
compared against module source at `{factory-root}`
(repo HEAD = a117f4f == tag `v0.6.0`, verified same commit). Nothing in the vault was
written, moved, or deleted.

**Snapshot caveat (read first):** this copy arrived on this machine via **Obsidian
Sync**, which does not carry hidden (`.`-prefixed) folders and, in this vault's
configuration, does not carry most non-markdown file types either. Everything reported
"absent" in §2 is a **sync artifact, not vault state** — treat those surfaces as
*unverifiable*, not missing.

---

## 1. Layout and installed version

Vault top level: `.obsidian/`, `_agent/`, `_archive/`, `_bmad/` (dirs only — see §2),
`_meta/`, `_output/`, `_vault/`, PARA dirs (`areas/`, `projects/`, `resources/`,
`sources/`, `daily/`, `new/`, `docs/`), plus three root docs: `CLAUDE.md` (3.7K),
`DESIGN.md` (19.5K), `PRODUCT.md` (4.6K) — the latter two are **vault-grown** (the
Creative's "Living Monograph" print-editorial design system for fabricated HTML docs;
PRODUCT.md explicitly scopes it apart from the sayari-ai product design system).

**Version: 0.6.0.** Install and upgrade history from `_agent/upgrade-ledger.md`
(append-only, 2 entries):

- Fresh install at **0.3.1** from public GitHub (`github.com/mggower/bmad-module-vlt`),
  circa 2026-06-24 (first log entry 2026-06-24 16:20; first session file
  `2026-06-24-182204-ingest.md`). The vault was seeded by migrating a prior
  "workspace-v2" vault's wiki (28 pages re-stamped on 06-24).
- `## [2026-06-25 12:53] vlt 0.3.1 → 0.4.0 (own)` — "First upgrade; ledger created this
  run… Pristine vault: no mints, overlays, or capabilities."
- `## [2026-07-09 12:13] vlt 0.4.0 → 0.6.0 (own)` — a **two-version jump skipping
  0.5.0**, and the richest ledger entry either vault has produced: 3 mints preserved
  (`vlt-agent-navigator`, `vlt-agent-engineer`, `vlt-project-spec`; help-registry
  `local_mints_preserved` confirmed all 3, 17 total rows), `extraction.overlay.md`
  intact with the **overlay-subsumption pass run** (verdict: nothing retired — 0.6.0's
  `spec.md` judged "a distinct agent-zone contract class, not the overlay's retired
  `code_sources:`… sections"), help-CSV **header migration run**
  (`after,before` → `preceded-by,followed-by` — this was a pre-0.5.0 install so build-13's
  migration path got real exercise), and the **proto-spec-retrofit scan** ran, surfaced
  exactly one candidate (`_agent/handoffs/graph-approval-gate-vs-move4-hitl.md`),
  offered it, and the user **declined** ("a resolved two-round handoff, not an ongoing
  versioned contract. Nothing moved.") — the offer-don't-force shape worked as designed.

So this vault has field-exercised, in one run: multi-version jump, mint preservation,
overlay subsumption, CSV header migration, retrofit-offer-decline, and lazy
`_agent/specs/` creation (dir deliberately NOT scaffolded; it still does not exist —
consistent, since no spec has been minted).

## 2. Visible vs unverifiable (the sync gap inventory)

Confirmed sync behavior: `.obsidian/core-plugins.json` has `"sync": true`; PDFs synced
(5 present under `sources/`) but `find . -type f ! -name '*.md'` outside `.obsidian/`
returns ONLY those 5 PDFs. Therefore **unverifiable in this snapshot** (all known to
exist from ledger/log/dispatch evidence):

- **`.claude/` entirely** — the 14 shipped skills, the 3 minted skill dirs
  (`vlt-agent-navigator`, `vlt-agent-engineer`, `vlt-project-spec` — plus `vlt-hub`,
  minted 07-10, which the ledger predates), the 2 workflows. Byte-level skill drift vs
  source **cannot be checked** for this vault (contrast: vlt-core diffed clean).
- **`_bmad/` contents** — all 8 subdirs present but empty of files: `config.yaml`,
  `_config/manifest.yaml`, and **`module-help.csv` are NOT checkable** (the task brief
  assumed the CSV would be; it is not, because Sync drops non-md). Row count 17 and
  header migration are attested only by the 07-09 ledger entry.
- **`_agent/conventions/.baseline/`** and the build-18 `.skill-manifest` — hidden dir,
  not synced. `_agent/conventions/` shows only `extraction.overlay.md` (19.7K); do NOT
  read the missing baseline as a defect.
- **HTML artifacts** — the `vlt-hub` deliverable
  `projects/generative-ui/infinite-canvas/index.html` + back-strips injected into five
  children (attested by backlog + the 07-11 creative relay) are invisible; only the
  `.md` children synced.
- **`dev/` code zone** — symlinks to external checkouts (`dev/sayari-ai`, `dev/arc`),
  wired 2026-07-08, machine-local by design and additionally slated for Obsidian
  excluded-files ("Left to Mikey: Obsidian excluded-files → `dev/`"). Absent here as
  intended.
- `_vault/templates/` and `_vault/media/` are empty — plausibly genuinely empty (the
  librarian thread notes the daily-note Templater target "doesn't exist yet — harmless
  no-op"), but templates could also be non-md casualties.

Everything else — the whole `_agent/` zone (247 md files), `_meta/`, PARA, `_output/` —
is markdown and appears fully synced and internally consistent (no dangling
same-day references found between log/dispatch/sessions).

## 3. Drift vs module source: governance byte-identical; skills unverifiable

`diff -rq skills/vlt-setup/assets/governance/_meta/ ↔ vault _meta/` → **exit 0, zero
differences.** Operating contract, 5 personas, and all 7 conventions are byte-identical
to shipped 0.6.0: extraction@2, frontmatter@3, spec@1, wiki-consolidation@1,
wiki-index@2, wiki-supersession@1, write-verification@1. Ledger corroborates:
"Governance divergence: none" at both closes. (Skill-file drift unverifiable per §2.)

## 4. Vault-local growth (the durability surface for the next upgrade)

This vault has grown far more module-visible structure than vlt-core, and some of it
is **newer than the 07-09 ledger's inventory** — the next upgrade's preserve pass must
not treat that ledger snapshot as complete:

- **2 minted partners + 2 minted skills:** Navigator (minted 2026-06-25, council PASS,
  bundled with its `vlt-track` capability + the extraction overlay), Engineer (minted
  2026-06-26), `vlt-project-spec` (2026-06-30, heavy, Navigator-owned), **`vlt-hub`
  (2026-07-10, Creative-owned — minted AFTER the 0.6.0 upgrade, so it has never been
  through an upgrade preserve pass and is not in any ledger inventory).**
- **A full mint-retire-remint cycle:** `vlt-spec-external` minted 2026-06-29 (gated,
  heavy), **retired 2026-06-30** and replaced by `vlt-project-spec` — the only known
  field retirement of a minted skill. Its residue is managed but still open: the one
  orphaned external spec `resources/specs/langchain-ai-deepagentsjs/
  human-in-the-loop-interrupts.spec.md` awaits the librarian's ingest-then-archive
  relay (open since 06-30), and the 07-01 council-gated overlay edit marked the
  `code_sources:` machinery RETIRED in three overlay sections + 2 DORMANT notes in
  `vlt-lint/SKILL.md` (per the dispatch sub-task, those five sites must be swept
  together when the relay drains).
- **Partner memory (5 partners):** `_agent/partners/{navigator,engineer,librarian,
  researcher,creative}/` on the identity/thread layout. Engineer is the giant (52.9K
  thread, 13.9K identity, and a **persona self-edit** recorded in the 07-10 dev-loop
  mint); navigator 31.9K/22.3K; librarian only 8.7K; researcher 3.7K; creative 4.1K.
- **13 light-capability profiles:** navigator/{track, project-spec, project-synthesis,
  jira-story-hydrate, jira-devstate, jira-file-issue}, engineer/{codebase-map,
  pr-review, code-change-digest, design-investigations, dev-loop, codebase-backlog},
  creative/{hub}. **Four of these (project-synthesis, dev-loop, codebase-backlog, hub)
  post-date the 0.6.0 upgrade.**
- **A live capability FAMILY:** `_agent/capabilities/families/project-hub.md` —
  `family: project-hub`, `instances: [navigator, creative]`, binding the
  producer/consumer pair (Navigator's `synthesis-brief.md` → Creative's `vlt-hub`
  HTML render). **The family machinery, shipped-but-unexercised since 0.3.0 and empty
  in vlt-core, has its first real instance here** (created 2026-07-10; the 07-09 ledger
  still said "families/ empty").
- **A live convention overlay:** `_agent/conventions/extraction.overlay.md` (19.7K,
  ~270 lines) — proper `overlay_for: extraction` frontmatter, append-only discipline
  with RETIRED-in-place banners, two named `personalization_sources:` opt-ins
  (`vlt-track`, `vlt-project-spec`), and a namespace rule for `projects/<name>/`
  (`.html` = Creative / `.md` = Navigator). The overlay lifecycle — creation, gated
  edit (council REVISE→PASS 07-01), subsumption check at upgrade — has all run here.
- **Mint history:** `_agent/mint/decision-log.md` (581 lines, **13 entries**,
  2026-06-25 → 2026-07-11: 2 partners, 5 self-grown light capabilities, 2 heavy
  capability mints, 1 batched convention edit, 1 coordinated bundle + family, 2
  revisions) + 6 dated planning docs.
- **Engineer working state:** 11 codebase maps under `partners/engineer/codebases/`
  (sayari-ai split into 7 package maps + arc + arc-backlog mirror + falcor-api +
  sayari-mcp), 5 dev-loop runs (`APP-5833`, `-geo`, `-imgexp`, `-showcase`,
  `APP-5847`) with 16 story files, 1 investigation.
- **Navigator project state:** `_agent/projects/` — 6 project trees (graph-ai incl.
  dev-state + arc-integration, generative-ui with gen-packages + infinite-canvas
  children, agentic-platform, doc-gen, native-tools-mcp, project-california) +
  `strategic-realignment-2026-07.md`.
- **Root docs:** `CLAUDE.md` (with a vault-local `## Local zones` section declaring the
  `dev/` zone — the backlog files this for upstream graduation into the contract's
  Tool zones), `DESIGN.md`, `PRODUCT.md`. **These live at vault root, outside
  `_agent/` — a durability shape vlt-core doesn't have.**
- **PARA outputs:** `projects/` 11 build-specs/briefs across graph-ai + generative-ui;
  `_output/` 38 files (5 SPEC kernels under `_output/specs/spec-*`, epics/sequencing,
  3 brainstorm keepsakes, implementation artifacts); `areas/` 34 files (incl. a
  31-file `project-cali` due-diligence tree); `sources/` 10 files.

## 5. Governance state

Fully stock (§3). The interesting governance activity is all in the **overlay and the
mint gate**, not in base divergence: the 07-01 batched convention-edit mint is the only
gated governance change, and it landed in the overlay, exactly as the
generic-vs-local routing rule intends. One governance near-miss worth quoting: the
07-01 log entry flags "GOVERNANCE GAP … allowance is claimed-by-skill but
not-yet-named-in-convention" — caught by the vault itself and closed by that same
mint. The version-handshake seam (`depends_on` in skills) is unverifiable (§2).

## 6. Evidence of real use (very heavy, current, engineering-centric)

- **Operation log:** 185 entries, 2026-06-24 16:20 → 2026-07-11 (18 days, **~10/day** —
  denser than vlt-core's ~5.6/day). Partner distribution: **navigator 78, engineer 46,
  librarian 40, creative 11, researcher 6.**
- **Sessions:** 94 files (~5.2/day), through `2026-07-11-211500-geo-dev-loop.md`.
  Type mix: misc ~65, ingest 7, extract 6, research 4, lint 1, dev-loop 2.
- **Dispatch:** `_agent/dispatch.md` — **36 relay pointers (27 picked up, 9 open)**,
  2026-06-25 → 2026-07-11, ALL `relay:` mode; the `daily` routing mode has never fired
  (`daily/` is empty — no human daily notes in this vault). The relay traffic is the
  vault's backbone: grounding relays fire and return same-day (e.g. the 07-11
  image-export spike: fired 08:52, verdict returned 11:35), verdicts carry
  "✓ picked up" annotations with fold-in notes.
- **Wiki:** 34 pages + `index.md`. **But see §8 — 29 of 34 were created in the 06-24/25
  migration burst; only 5 pages have been created since.**
- **Research:** 13 notes (2026-06-22 → 2026-07-10).
- **Handoffs:** 27 files, 06-26 → 07-11 — the spike/grounding return pattern
  (`*-grounding.md` + `*-grounding-return.md` pairs) is this vault's invention.
- **Backlog:** 12 open + 4 done items; living (the 07-11 codebase-backlog item went
  filed→ruled-on-by-Mikey→minted same day).
- **Jira integration in anger:** navigator capabilities jira-file-issue /
  jira-devstate / jira-story-hydrate drove real tickets (APP-5575/76/77 filing saga in
  the 07-01 log, incl. Mikey correcting the agent's misread of board automation);
  engineer dev-loops track real sprint stories (APP-5833 epic: "all six stories merged
  to arc main (PR #126)").
- **Skills demonstrably exercised:** vlt-mint (13 decisions), vlt-track (6 project
  loops), vlt-dispatch (36 relays), vlt-ingest (14 log entries), vlt-lint (2 full
  runs), vlt-research (4+ sittings), vlt-extract (6 extract sessions; personalized
  extraction via both named opt-ins), vlt-project-spec (5 SPEC kernels in `_output/specs/`),
  vlt-hub (hub shipped + masthead revision), vlt-review-council (REVISE→PASS verdicts
  recorded), vlt-upgrade (2 runs), vlt-setup (install), plus bmad-brainstorming (3
  keepsakes) and a bmad UX-design run (`_output/planning-artifacts/ux-designs/`).
- **Confidential-material discipline:** the 07-09 product-narrative ingest split
  confidential running state away from the wiki explicitly ("CONFIDENTIAL running-state
  must NOT enter the wiki/PARA — durable naming/architecture facts only") — the
  durable/project-state split holding under real stakes.

## 7. Machinery exercised HERE that vlt-core never touched (and vice versa)

This vault is the missing half of the field-coverage matrix:

| Machinery | vlt-core | vlt-sayari |
|---|---|---|
| Loop profiles (build vlt-track 0.4.0) | never (0 profiles) | **LIVE** — `navigator/capabilities/track.md` carries a full `## Loop profile` block (root/target/subject-model:multi/data-streams/gate). **The Arc-1 loop-profile watch item is discharged in the field by this vault.** |
| Capability families | never (`.gitkeep` only) | **LIVE** — `project-hub` family, 2 instances |
| Convention overlays | never | **LIVE** — extraction overlay incl. gated edit + subsumption pass |
| Overlay-subsumption at upgrade (build-18) | ran against nothing | ran against a real overlay |
| Help-CSV header migration (build-13) | ran (0.5.0) | ran (0.4.0→0.6.0 jump) |
| Proto-spec retrofit offer | n/a | offered + declined (correct outcome) |
| Skill retirement | never | `vlt-spec-external` retired 06-30 |
| Multi-version upgrade jump | never (stepwise) | 0.4.0→0.6.0 |
| Personalized extraction opt-ins | 0 | 2 named ops |
| Minted partner count | 3 (domain/lifestyle) | 2 (work verticals) + 2 skills |
| Dispatch `daily` mode | used | **never** (no daily notes) |
| Spec convention artifacts (`_agent/specs/`) | dir exists, empty | **dir doesn't exist** — zero specs |
| Attestation (`verified_by`) | 37/124 pages (30%) | **7/34 pages (21%)** |
| `review_after` freshness | 1/124 | **3/34** (incl. `superconductor-platform: 2027-01-15`) |
| Enforcement-kit prototype | live (tripwires/vitals) | none |

The Arc-3 hard gate — first spec minted from the shipped text — is unmet in BOTH
vaults; here not even the directory exists yet.

## 8. THE ORPHANING PATHOLOGY (the graduation-queue headline)

Context: the 2026-07-11 inbox filing pair
(`inbox/2026-07-11-114226-research-note-graduation-queue.md` + the same-day
`…-153000-graduation-queue-field-calibration.md`) named this vault as the real
pathology site: "The owner's second vault (the work vault, where research supports
development projects and routinely goes un-ingested) is where the 114226 filing's
actual pathology lives … the mechanism's acceptance run should happen there." Here are
the numbers that acceptance run will face.

**Raw counts:** 13 research notes; 34 wiki pages (+index); 10 raw sources; 27 handoffs;
94 sessions.

**Naive (frontmatter-only) orphan projection:** 9 of 13 notes appear in no wiki
`sources:` (69% "orphaned").

**Union projection (frontmatter ∪ body-wikilink ∪ shared-source overlap — the
calibration filing's recommended shape), computed note by note:**

- Referenced from wiki (frontmatter or body): **5 notes** — `…changesets-turborepo-
  publishing` (1 page), `…tools-skills-tradecraft-equivalency` (1), `…2h-2026-product-
  narrative` (1), `…stitch-infinite-canvas-arc` (2), `…sigma-canvas-image-export` (2).
- Shared-source overlap: **5 more** — the four graph-ai standup/testing notes + live-
  testing note each cite exactly one `sources/transcripts/` file, and every one of
  those five transcripts is cited by 2–3 wiki pages (e.g. `source-provenance-in-agent-
  responses.md` frontmatter lists four of them). These are the durable/project-state
  *split* working as designed: durable content went to the wiki citing the transcript;
  the research note is the project-state half, deliberately not cited.
- **True zero-wiki-linkage residue: 3 of 13 (23%)** —
  `2026-07-02-spike-arc-profile-derivation` (spike output; consumed by 3 project-layer
  artifacts, never wiki'd), `2026-07-09-135219-html-in-canvas-arc-webgl` (promotion
  condition evaluated and **explicitly declined** — backlog item resolved 2026-07-09,
  "the note stays standalone unless cross-engine standardization revives it"),
  `2026-07-09-204051-react-components-in-svelte-5` (consumed by 3 project-layer
  artifacts — the gen-packages islands decision — never wiki'd).

So the union projection works here too: 69% → 23%, and of the residual 3, one is a
documented deliberate island. **The per-note orphan rate is NOT this vault's
pathology.** The pathology is one level up, and it is bigger:

**(a) The wiki froze after the migration burst.** `created:` dates: 28 pages on
2026-06-24, 1 on 06-25 (all migration of the prior workspace-v2 wiki), then **5 new
pages in the following 17 days** (1 on 07-08, 3 on 07-09, 1 on 07-10) against ~156
post-migration log operations and 94 sessions. Knowledge production is furious;
wiki graduation is a trickle. `last_updated` tells the same story (16×06-24, 6×06-25,
3×06-30, then only 07-08/09/10 touches on 9 pages).

**(b) The durable-knowledge pipeline stalls at the librarian.** Of the 9 open dispatch
pointers, **4 are librarian-bound ingest relays**: the 06-30 alpha-testing-session
durable-knowledge relay (**12 days open**, itself carrying "Still owed alongside this:
the 06-26 live-testing raw transcript ingest (parked since 06-26)" — 15 days), the
06-30 deepagents ingest-then-archive (12 days, with its five-site governance sweep
attached), the 07-09 California-naming reconciliation, and the 07-10 arc-architecture
knowledge relay. The oldest open pointer of all is the **06-26 engineer→researcher**
openuidev render-internals gap (16 days). The librarian's log share (40) is heavily
migration-era; its thread is the smallest working file among active partners (8.7K vs
engineer's 52.9K).

**(c) Deferred backfill compounds it.** The librarian thread carries the paused
workspace-v2 migration: "Phase 3 — Research + sources. Carry the top ~8 research notes
from `workspace-v2/_agent/research/` … archive the 22 transcripts read-only …" — an
acknowledged, un-scheduled pile of pre-vault research that a graduation queue would
inherit on arrival.

**(d) The vault has already asked for the mechanism, twice.** Backlog (researcher,
2026-07-09): "Brainstorm mechanisms for detecting research notes that should be
promoted to the wiki … the vault has **no** mechanism to surface an old `{research}`
note that has earned a wiki page … research notes carry no expiry axis and
deliberately 'rest.'" And the engineer's open knowledge-gap item — the
"failure-as-invisibility / over-claim" pattern distilled across 4 PR reviews, wanting
"a Librarian-filed wiki page … so it's canon rather than re-derived each review" — is
precisely a graduation candidate whose content lives in a partner thread, not even a
research note. **Signal for the design: in this vault the graduation-ripe knowledge
lives in handoffs (27), partner threads, and project status files at least as much as
in `_agent/research/`.** A detector scoped to the research zone alone would miss most
of what's stranded here.

**(e) Substrate raggedness confirmed on the work vault too:** `topic:` styles mix
YAML lists (11 notes) with a comma-joined string (`topic: frontend, framework-interop`
in the 07-09 svelte note) — the calibration filing's normalization prerequisite for
`cluster_ripe` holds here as well.

**Date-pattern summary for the queue's first run here:** one migration burst (06-24/25),
research notes in two clusters (4 on 06-22/25 transcript-era, 6 on 07-08/09/10
development-era), wiki additions only where an ingest happened to run same-day
(changesets 07-08, tradecraft + narrative + superconductor 07-09, graph-canvas-image-
export 07-10). Nothing has been linted since 07-02 (two full lints: 06-25 on 27 pages,
07-02 on 28 pages — the 5 newest pages have never seen a lint pass).

## 9. Friction / defects on disk

- **Duplicate source file:** `sources/tools-skills-tradecraft-equivalency.pdf` exists
  BOTH at `sources/` root and at `sources/docs/…` (the wiki cites the `docs/` copy) —
  filing-location cruft from an ingest.
- **9 open dispatch pointers**, oldest 16 days (06-26 researcher relay) — see §8(b).
  Not malformed, but the board's own "self-reporting backlog" is reporting a drain
  problem. One open pointer (07-02 engineer→creative Move-3 update) may be mooted by
  the 07-10 realignment (graph-ai paused) but was never retired the way the 07-10
  retirement of the graph-investigator-boundary relay was ("killed as moot, not
  answered" — that retirement note is the model).
- **No lint since 07-02** while 5 pages + several updates landed; the librarian thread
  itself flags a page carrying "live external risk" (`changesets-monorepo-publishing`
  naming two open upstream bugs) as "worth flagging at the next lint pass."
- **The upgrade ledger's capability inventory is already stale** (4 capabilities + 1
  family + 1 minted skill grown in the 2 days after the 07-09 entry) — not a defect
  (the ledger is a snapshot by design) but the next upgrade must derive the preserve
  set from disk, not from the previous ledger entry. (Derive-first, as Arc 3 says.)
- **Unverifiables to re-check on the work machine itself:** skill-dir drift,
  `module-help.csv` 17 rows + header, `_bmad/config.yaml` version + structure map
  (did it gain `specs:` despite the dir not existing? — ledger says the config gained
  the logical path), `_config/manifest.yaml` (expect the same stale-0.x issue found in
  vlt-core), `.baseline/` + `.skill-manifest` presence, hub `index.html` + back-strips,
  and whether `vlt-hub`/`dev-loop`/`codebase-backlog` skill/capability surfaces carry
  `spec.md`-convention acks where required.
- **No conflicted-copy files, no stray `.decision-log.md`, no root cruft** found in the
  synced surface (cleaner than vlt-core on this axis).
- Root `CLAUDE.md` orientation is 3.7K vs vlt-core's 2.3K — grown with `## Local zones`
  (the `dev/` zone) — vault-local contract prose the backlog wants graduated upstream
  (open item: "Graduate the `dev/` developer code zone into the shipped operating
  contract… Verified working here 2026-07-08").

## 10. vlt-core vs vlt-sayari contrast

- **Two different animals on the same module.** vlt-core is librarian-centric personal
  knowledge (124 wiki pages, 90 research notes, heavy ingest/lint); vlt-sayari is
  navigator/engineer-centric development support (34 wiki pages, 13 research notes,
  but 36 dispatch relays, 27 handoffs, 11 codebase maps, 5 dev-loop runs, 5 SPEC
  kernels, real Jira traffic). Same contract, opposite center of gravity — strong
  evidence the partner/capability model generalizes.
- **Complementary machinery coverage:** loop profiles, families, overlays, retirement,
  multi-version jump, retrofit-decline — all exercised ONLY here; enforcement-kit
  prototype, daily dispatch, bases, heavy attestation rollout — ONLY in vlt-core.
  Between the two vaults, almost every shipped mechanism now has field evidence; the
  shared zero remains the **spec convention** (Arc-3 gate unmet everywhere).
- **Orphaning inverts:** vlt-core is the benign case (90 notes, ingest almost always
  runs, losses are partial-ingest residue; union-projection residue ~13/90 ≈ 14%).
  vlt-sayari's per-note residue is 3/13 (23%) — but its real starvation is
  wiki-graduation throughput (5 new pages / 17 days / 94 sessions) and a
  librarian-side relay queue (4 open ingest relays, 12–15 days). The graduation
  queue's acceptance here must therefore measure **drain latency and non-research
  strandings (handoffs/threads/status)**, not just note citation coverage.
- **Governance:** both vaults byte-identical to shipped on bases; divergence expresses
  itself here through the overlay (correctly) and in vlt-core through vault-local
  top-level prototypes. Both patterns are durable surfaces the merge scripts must keep
  treating as untouchable.
- **Upgrade discipline held under harder conditions here** (jump + mints + overlay +
  migration + retrofit in one run) than in vlt-core's stepwise history — the 07-09
  ledger entry is arguably the module's best single piece of field validation.
