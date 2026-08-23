# Lifecycle Archaeology — the vlt development lifecycle as actually practiced

Raw findings for the 2026-07-12 principal-engineer handoff. Domain: the evolution
lifecycle of the `vlt` module factory repo (`{factory-root}`),
not the module's features. Everything below is grounded with file references; quotes are
verbatim from source.

Ground truth as of 2026-07-12: repo clean on `main` @ `a117f4f` (= v0.6.0 release commit,
tagged, pushed). Three arcs run so far: Arc 1 (builds 3–11, v0.4.0), Arc 2 (builds 12–13,
v0.5.0), Arc 3 (builds 14/15/16/18, v0.6.0 — **open, acceptance pending**; build-17 trails).

---

## 1. The lifecycle as practiced, step by step

The canonical statement is `CLAUDE.md` § "The evolution lifecycle (the loop this repo runs
on)" (7 steps). Below: each step's artifact, governing convention, and enforcement status
(tooling vs. discipline). Note CLAUDE.md itself is **young** — it was only written at commit
`6f21952` (2026-07-06, after v0.5.0 shipped, "docs: add CLAUDE.md — vlt module lifecycle +
standing rules"). The first two arcs ran the loop with no written charter; CLAUDE.md is
largely a *fossilization* of what those arcs learned (see §2).

### Step 1 — Field notes arrive (`inbox/`)

- **Artifact:** one dated markdown note per filing, `YYYY-MM-DD-HHmmss-slug.md`, written by
  a partner or the owner from a live vault. Shape documented in `inbox/README.md:1-20`.
- **Convention:** "an **empty** active inbox means everything filed so far has been pulled
  into a roadmap" (`inbox/README.md:19`). Filings move to `inbox/archive/` only once their
  build has shipped **and** passed acceptance (`CLAUDE.md` step 7; arc3 roadmap
  `inbox-evolution-arc3-roadmap.md:663` "Filings stay in `inbox/` until their build ships
  **and** passes acceptance, then archive"). Note the archival criterion *tightened* over
  time: Arc 1/2's rule was "until their build ships" (`arc2-roadmap:303`); Arc 3 added the
  "and passes acceptance" clause.
- **Filing quality varies and is expected to:** filings can be defects, patterns,
  candidates, or **design-stage proposals filed at the owner's request ahead of evidence**
  (Arc 3's 091003/091005/091006, flagged honestly at `arc3-roadmap:59-63`; the 2026-07-11
  graduation-queue filing states "Design-stage proposal, filed at the owner's request …
  Nothing is built in vlt-core yet").
- **Enforcement:** pure convention. No tooling checks filing shape, naming, or that a live
  vault actually filed it. Also a live structural gap surfaced by the newest filing: the
  second consumer vault (work machine) "has no access to this inbox"
  (`inbox/2026-07-11-153000-graduation-queue-field-calibration.md:9`) — vlt-core files on
  its behalf. There is no defined channel for non-primary vaults.

### Step 2 — Capture (roadmap in `skills/reports/`)

- **Artifact:** one arc roadmap per signal-cluster, `inbox-evolution-arc<N>-roadmap.md`,
  frontmatter `status`/`derives_from`/`predecessor`/`intent`; body = through-line, per-filing
  grounded capture (`### A<arc>-<i>. …`), cross-cutting threads, proposed grouping table,
  deferred acceptance ledger. Closed roadmaps + their briefs move to
  `skills/reports/archive/` and are never appended (`CLAUDE.md` step 2; every archived
  roadmap's status carries "do not append").
- **Convention — grounding-before-capture:** every filing claim is re-verified against
  current module source, with a verdict grade: **CONFIRMED / PROVENANCE CORRECTION /
  SUPERSEDED / GAP CONFIRMED** (`.claude/skills/inbox-capture/references/grounding-methodology.md:16-24`).
  "never trust a filing's self-description — filings mis-attribute provenance and guess
  wrong fixes often enough that this is the whole point of the step"
  (`.claude/skills/inbox-capture/SKILL.md:13-15`).
- **Convention — the roadmap IS the decision log:** "This skill doesn't keep a separate
  `.decision-log.md`. The roadmap doc's frontmatter + capture narrative already carry that
  role across the arc's whole lifetime" (`references/roadmap-synthesis.md:6-11`).
  `derives_from` and capture body are **append-only** across the arc's life
  (`roadmap-synthesis.md:30-32`).
- **Enforcement:** **this is the ONLY lifecycle step formalized as a skill** —
  `.claude/skills/inbox-capture/` (SKILL.md, 70 lines + `references/grounding-methodology.md`
  + `references/roadmap-synthesis.md`). It has a `--headless` mode with a JSON completion
  contract and a `blocked` status for owner-ruling conflicts (`SKILL.md:33-44`). Its style
  precedent is explicitly the Arc 2 roadmap: "read it for the level of specificity expected
  … Match its rigor, not its length" (`grounding-methodology.md:42-47`). Everything else in
  the skill is still LLM discipline, but the method is written down and versioned.

### Step 3 — Ideate (owner-steered; spikes for external unknowns)

- **Artifact:** an "Ideation rulings" section appended to the open roadmap, "binding for
  all Arc N briefs … Briefs cite this section, never re-litigate"
  (`arc3-roadmap:505-509`). Covers grouping/order acceptance, per-filing owner rulings,
  cross-filing decide-once rulings, spike obligations, and "questions deliberately left to
  brief time" (`arc3-roadmap:510-573`).
- **Convention — spike before brief:** "An external unknown gets a **spike before the brief
  is written** — read the actual external source rather than reasoning from its docs or
  from memory" (CLAUDE.md step 3). Practiced three times, each recorded as a closed spike
  record in the roadmap:
  - Arc 1 **B2 installer-copy spike** (`archive/inbox-evolution-roadmap.md:445-449`) —
    could NOT be settled from available source; resolved by specifying under a
    "safe-pessimistic assumption" and identifying the *actually* ship-blocking sub-finding
    (B1 anti-zombie at `merge-help-csv.py:186-198`).
  - Arc 2 **F1 installer spike** (`archive/inbox-evolution-arc2-roadmap.md:231-247`) — read
    the real installer source (`tools/installer/project-root.js:102`), which **refuted** the
    capture-time hypothesis and the filing's guessed fix, yielding the correct fix (cache
    seed).
  - Arc 3 **Obsidian Bases date-filter spike** (`arc3-roadmap:550-565`) — verified against a
    live `.base` file + official syntax docs; found the filing's assumed `today` is actually
    `today()` and added a key-presence guard.
- **Tooling used:** `bmad-module-builder` drives the ideation session ("Session ran via
  `bmad-module-builder` ideation against this doc", `arc3-roadmap:507`), but the
  vlt-specific conventions (rulings section shape, spike obligations, binding-ness) are
  discipline only.
- **Enforcement:** discipline + CLAUDE.md prose. Nothing checks that a brief actually cites
  the rulings or that spikes closed before briefing.

### Step 4 — Brief (`skills/reports/build-N-<slug>.md`)

- **Artifact:** per-build brief with frontmatter `title`/`status`/`module_code`/`created`/
  `derives_from` (filings, with the specific latent-bug IDs they contribute)/`roadmap`/
  `rulings`/`risk` (see `build-18-durability-cluster.md:1-11`). Body organized as **F-sites**
  (`## F1 …` per file/feature touched, e.g. `build-15-spec-convention.md:50-150`), plus a
  "Brief-time dispositions" section resolving the filing's open questions per the ideation
  rulings (`build-15:25`), verification + acceptance checks.
- **Convention:** "exact sites with `file:line` grounding, out-of-scope dispositions,
  verification + acceptance checks. Append its live-acceptance checks to the arc roadmap's
  ledger" (CLAUDE.md step 4). The append actually happens — arc3 ledger has per-build
  bullets dated at brief time (`arc3-roadmap:589-618`). Build-18's brief was additionally
  **re-grounded against post-16 source** and recorded a grounding correction superseding a
  roadmap note (`arc3-roadmap:649-653` — "build-16 made vlt-research a frontmatter@3
  consumer … the roadmap's A3-6-LB1 'non-consumer' note is superseded").
- **Enforcement:** pure discipline. No skill, no lint. The brief shape has converged hard by
  imitation (all 16 briefs share it), but nothing checks e.g. that acceptance checks were
  appended to the ledger, or that a brief cites the rulings section.

### Step 5 — Build

- **Artifact:** the implementation itself, plus the brief's `status:` field rewritten to a
  long BUILT record including **deliberate deviations**. Exemplar: `build-15:3` records
  three numbered deviations (faithfulness diff couldn't run because the vault-side mint
  hadn't happened; additive-beyond-letter items; a pre-existing example-slug leak "noted for
  build-18's placeholder rule — not touched here"). `build-18:3` records four
  deviations/notes plus its own unit-verification evidence inline.
- **Convention — unit-verify at rest:** "greps for cross-file agreement, real script runs
  against temp fixtures, end-to-end against real external code where possible" (CLAUDE.md
  step 5). Practiced: build-13 "verified end-to-end against the real installer resolver"
  (`arc2-roadmap:258`), build-18 "Python fixture dry-runs PASS" (`build-18:3`), build-6 B1
  "unit-tested: shipped-refresh / mint-preserve / zombie-drop" (`arc1-roadmap:427`).
- **Convention — one commit per build** (CLAUDE.md step 6; visible in git log: `8c21736`,
  `3795d86`, `1142fb4`, `2b79e89` are exactly builds 14/15/16/18).
- **Enforcement:** discipline, except the packaging surface (see step 6). Builds routinely
  run `package-lint.py` mid-arc too (`build-18:3` — "A/B/C PASS (D skipped — `--expect-version`
  is the release gate)").

### Step 6 — Release

- **Artifact:** branch `arcN-vX.Y.Z`, one commit per build, a release commit bumping
  **both** version strings (`.claude-plugin/marketplace.json` `plugins[0].version` and
  `skills/vlt-setup/assets/module.yaml` `module_version`), ff-merge to main, tag `vX.Y.Z`,
  push main + tag (CLAUDE.md step 6).
- **Enforcement — the one mechanically-gated step:** `tools/package-lint.py` (build-14,
  shipped in this very release). "The release boundary's bell: every tag is cut only after
  this exits 0. Checks the WORKING TREE ON DISK, never the git index — vlt-upgrade's
  own-the-apply is a filesystem copy, so a git-scoped check silently misses on-disk cruft"
  (`tools/package-lint.py:8-11`). Four groups:
  - **A** — on-disk cruft (`.decision-log.md`, `__pycache__/`, `*.pyc`, `.DS_Store`) within
    the shipped surface + repo root depth 1 (`:58-71`; the root scope exists because
    "./.DS_Store has shipped before", `:68`).
  - **B** — `module-help.csv` canon: header **imported from `merge-help-csv.py`'s `HEADER`
    symbol, never duplicated** (`:74-80`), 13-field rows, always-quote free-text rule
    checked against the *raw* line (`:83-148`).
  - **C** — module.yaml parses; module_version == marketplace version; governance bundle
    home exists non-empty; `skills[]` ↔ `skills/vlt-*` dirs bidirectional (`:151-198` —
    "silently doesn't ship" / "breaks install" messages encode the two drift directions).
  - **D** — `--expect-version X.Y.Z` asserts both strings equal the tag about to be cut;
    without the flag it reports **SKIPPED, not PASS** (`:201-208`, `:227`) — an honesty
    detail: a lint run without tag intent can't be mistaken for a release gate.
  - The PASS summary line must be recorded in the release commit — and is, verbatim, in
    `a117f4f`: "package-lint: A/B/C PASS, D PASS — vlt 0.6.0 (uv run tools/package-lint.py
    --expect-version 0.6.0, exit 0)". CLAUDE.md's rationale: "skipping the lint is then
    visible in history."
- **Still discipline:** the branch/ff-merge/tag/push choreography, recording the PASS line,
  and running the lint at all (the lint can't force itself to be run — there is no git hook
  or CI; `arc3-roadmap:153-155` confirms "no `.github/`, no active git hooks" was the state
  at capture, and only the script itself was added).

### Step 7 — Live acceptance (batched, owner-run, closes the loop)

- **Artifact:** the **Deferred acceptance ledger** section of the arc roadmap — checkbox
  items per build, appended at brief time, discharged after the owner runs `vlt-upgrade` on
  the live vault (`arc3-roadmap:576-622`; Arc 1's original at
  `archive/inbox-evolution-roadmap.md:344-409`).
- **Convention evolution:** Arc 1 **batched all acceptance behind Phase D** ("Do **not**
  upgrade vlt-core … until Phase D — lifecycle durability — ships" — the whole board gated
  on the durable upgrade path existing, `arc1-roadmap:346-358`). From Arc 2 on, "Arc 1's
  batching decision no longer applies — vlt-upgrade exists and has run clean … Acceptance
  … can ride the **next ordinary vlt-core upgrade**" (`arc2-roadmap:268-270`).
- **Discharge is evidence-based, recorded in the ledger:** e.g. Arc 2 build-13 "Discharged
  2026-07-06 — the in-place header migration confirmed run in anger by the
  `2026-07-06-091002` filing" (`arc2-roadmap:282-286`) — acceptance evidence can arrive
  *via a later inbox filing*, closing the loop in both directions.
- **Enforcement:** pure discipline + owner action. Nothing tracks that ledger items are
  discharged before an arc closes, or that filings archive on time.

### Step 0 (implicit) — the pre-arc origin

`skills/reports/vault-module-plan.md` (118K, `status: shipped`) is the pre-lifecycle
artifact: the original BMad module plan whose `build_progress` field served as the
Build #1/#2 log. The roadmap pattern was invented when field signal started arriving:
"it spawns per-build briefs (build-3-*.md, …) the same way vault-module-plan.md spawned
the Build #1/#2 briefs" (`arc1-roadmap:26-27`).

---

## 2. The fossil record — every "this bit us before" rule traced to its origin

Each CLAUDE.md standing rule exists because of a specific, documented failure. Origins:

### "Governance SSoT … a top-level staging tree once diverged silently and was retired"
Origin: **the governance SSoT collapse, 2026-06-24, mid-build-5** (`arc1-roadmap:425`).
Builds 3 AND 4 edited only `skills/vlt-setup/assets/governance/` while a top-level
`governance/` "staging source" (pointed at by README:71 at the time) silently diverged —
"all 5 conventions + the operating contract. Ironically the Phase-B *coherence* machinery
was applied incoherently." Resolution: git rm 11 files, repoint README + arch-spec.
The failure mode (dual copies drift) is the same one the module's own version-handshake
exists to catch — the factory tripped over the exact class it was shipping a cure for.

### "Version-handshake (build-4)"
Origin: **two independent convention→consumer drift incidents in the Arc 1 filings**:
filing #4 §5 (an index redesign updated `wiki-index.md` but not vlt-ingest/vlt-lint/
vlt-lint-full — "drift sat latent through a whole migration", `arc1-roadmap:116`) and
filing #3 §3 (source-count checks the redesigned convention had removed — which grounding
then showed was itself a *vault-local* edit never upstreamed, `arc1-roadmap:98`).
Cross-cutting thread: "a convention changed and its consuming skills didn't"
(`arc1-roadmap:310`). Even after shipping, the handshake had its own miss: **build-4
shipped the relay-when-done reflex without wiring its Beat-2 pickup read** — found only by
the 0.3.0 acceptance run (R2-1, `arc1-roadmap:232-252`), initially mis-blamed on build-7
until grounding diffed the actual commits ("build-7 is innocent … #1 is a build-4
coherence gap"). Arc 2 then found the same shape one level up: the BMB builder template's
own header drift ("exactly the convention→consumer failure the build-4 handshake was
built to catch, but living in tooling the handshake doesn't cover", `arc2-roadmap:207-211`).

### "The operating contract is deliberately NOT handshaked — single-home + pointers"
Origin: a **deliberate Phase B ruling** ("Operating contract held OUT → Phase D … #9 uses
the complementary single-home+pointer pattern", `arc1-roadmap:326`), grounded in filing #9
being "the same shape handled *correctly*: the relay-when-done reflex is given a single
home … with partner skills carrying only a pointer" (`arc1-roadmap:310`).

### "Single-home discipline … lists that claim completeness drift"
Origin: **build-9 / Phase E** (`arc1-roadmap:329, :431`): partner SKILLs + template carried
an inline *full-set* logical-name enumeration that "had fallen 2 names behind
(`overlays`/`upgrade_ledger`) while telling the reader to 'read the map'". Fix: delete the
enumeration (4 files). The nuance in CLAUDE.md ("subset-with-defaults listings don't
[drift]") is verbatim from build-9's finding: "op skills left untouched (their
subset-with-defaults listings don't claim completeness, so they don't drift on additions)".

### "`module-help.csv`: canonical header … always quote free-text fields … don't regress either"
Two origins, two arcs:
- **Always-quote:** R2-3 (0.3.0 acceptance run) — two live rows with unquoted commas made
  `merge-help-csv.py` **abort the whole merge before the local-mint preserve ran**,
  blocking registration until hand-fixed. "The guard was a *detector*; field use shows it
  must become a *survivor*" (`arc1-roadmap:265-275`). Fixed both sides in build-10
  (write-side always-quote + read-side skip/report).
- **Canonical header:** Arc 2 A2-3 F2 — the generic BMad installer warned on vlt's
  `after,before` header; grounding discovered the drift **originates upstream in the
  builder's own scaffold** (template CSV canonical, template script + tests stale,
  `arc2-roadmap:161-179`), plus the migration wrinkle: `merge-help-csv.py:291`
  target-header-wins means renaming the source never fixes an installed vault → build-13's
  rename-in-place migration. Both rules are now mechanically enforced by lint group B.

### "Workflows: the runtime delivers `args` as a JSON string — parse-on-intake"
Origin: **Phase 0, the highest-pain Arc 1 defect** — "Every council-gated mint fails on the
first try" (filing #7, `arc1-roadmap:145-155`), same bug as filing #3 §1's lint-full
blocker. The filing's diagnosis ("harness didn't thread args") was **wrong**; the empirical
Phase-0 test found the runtime delivers args as a JSON-encoded **string** for *every*
invocation form; `args || {}` on a truthy string then `.mode` → undefined "looked like a
drop. It was never dropped — just unparsed" (`arc1-roadmap:147`, Phase 0 record `:458-462`).
"Standing rule for all future module workflows: parse args defensively at the top"
(`arc1-roadmap:308`).

### "No per-skill `.decision-log.md` in the working tree"
Origin: **R2-2** (0.3.0 acceptance run) — 10 gitignored-but-on-disk `.decision-log.md`
files rode `vlt-upgrade`'s **filesystem** own-the-apply into the live vault; "one
**clobbered the vlt-mint relocation stub** — the precise failure the stub warns about.
gitignore governs the repo, not a filesystem copy" (`arc1-roadmap:254-263`). Fixed both
layers in build-10 (delete + copy-exclude); now *also* mechanically enforced by lint
group A. This incident is the root of the whole "two ship surfaces" insight that made
build-14 check the working tree, not the index.

### "Durability posture … merge-not-replace … re-check the B1 local-mint preserve path"
Origin: **filing #8** (2026-06-13), "the deepest filing" — the generic BMad installer "can
silently destroy/deregister vault-specific evolution on every version bump"
(`arc1-roadmap:157-173`). The B2 spike then proved the *registration* hazard was the real,
verified ship-blocker: `merge-help-csv.py` "is anti-zombie — on every run it strips **all**
`vlt` help rows and rewrites only from the **bundled** CSV … locally-minted partners are
deregistered on upgrade even if their dirs survive" (`arc1-roadmap:448`). Build-6 shipped
merge-not-replace + append-only convention overlays + `vlt-upgrade`
prefer-own/degrade-to-bracket. The first real upgrade (2026-06-24) validated it: "all 4
local mints preserved … zero destruction" (`arc1-roadmap:434`). Arc 3's build-18 extended
the same posture to shipped skill *assets* (which had no divergence net) and the overlay
*return leg* (subsumption/retirement) — "the missing half of the local-prototype→upstream
rail" (`arc3-roadmap:415-422`).

### "Worked examples in shipped skills use placeholder paths"
Origin: **091001 latent bug 2** — `vlt-dispatch/SKILL.md:193` hardcoded a live vault
artifact path (`_agent/handoffs/2026-06-13-…`) in a shipped worked example; "a vault-side
file move otherwise strands the module's own documentation" (CLAUDE.md Git & publishing).
Build-15 fixed the instance; build-18 shipped the standing rule (F5), and its brief's
verification confirms "build-15's `2026-06-13` leak absent; the sole dated-path hit
`spec.md:38` is a compliant stock-cast placeholder" (`build-18:3`). CLAUDE.md carves out
generic *domain* illustrations (dog-training/health-coaching) explicitly because build-18's
disposition 5 ruled those slugs KEPT.

### "Run package-lint before tagging"
Origin: **091002** — "Every tag 0.3.0→0.5.0 shipped a known packaging defect class, each
caught downstream by vlt-core's vlt-upgrade and hand-fixed at the cost of a full lifecycle
round-trip. The release boundary has no bell" (`arc3-roadmap:146-149`). At grounding time
both defect classes were live on disk (`skills/vlt-setup/scripts/__pycache__/…​.pyc`,
`./.DS_Store`, `./docs/.DS_Store` — `arc3-roadmap:169-183`). A related historical instance:
the 0.3.0 version bump itself had to patch a registration gap — "vlt-dispatch (build-4)
and vlt-upgrade (build-6) were missing from marketplace.json's skills[] install manifest"
(`arc1-roadmap:432`) — the exact drift class lint group C5 now catches.

### "Ground every filing claim against current module source before capturing"
Origin: an accumulating pattern of filings being wrong in load-bearing ways, plus one
capture failure:
- Filing #1's fixes were **already shipped** in `c918274` and "the roadmap simply never
  recorded it" — discovered only during Phase A ideation (`arc1-roadmap:68`).
- Filing #7's root-cause diagnosis was wrong (see args above).
- R2-1's provenance was wrong (blamed build-7; was build-4).
- Arc 2 A2-1(a): the "stale guidance" was **vault-local memory, not module source**
  (`arc2-roadmap:41-52`); A2-3 F1: the filing's guessed fix (`_bmad/vlt/module.yaml`) "is a
  non-location" (`arc2-roadmap:244`).
- Arc 3: A3-3's "new" contract-grammar section already existed verbatim
  (`arc3-roadmap:218-226`); A3-6's overlay-blind sweep list was corrected
  (`arc3-roadmap:407-414`).
The rule is now the entire reason `inbox-capture` exists as a skill ("this is the whole
point of the step", `SKILL.md:14`).

### "Spike before the brief is written"
Origin: the three spike records in §1 step 3 above. The pattern each time: reasoning from
docs/memory produced a wrong answer (Arc 2's naming-convention hypothesis refuted by
installer source; Arc 3's `today` vs `today()`), and reading the actual external source
was cheap and decisive.

---

## 3. How the process evolved, Arc 1 → Arc 2 → Arc 3

**Pre-arc (Builds 0–2, May–June 2026):** `vault-module-plan.md` frontmatter
`build_progress` as the only log; briefs (`build-1-partner-layer-brief.md`,
`build-2-mint-and-council-brief.md`) spawned directly from the plan. No inbox, no roadmap,
no ledger.

**Arc 1 (2026-06-06 → 06-25, builds 3–11, v0.4.0)** — the loop invents itself:
- The **inbox → roadmap-as-durable-cache → per-build briefs** pattern
  (`arc1-roadmap:23-27`).
- **Phases → builds:** Arc 1 thought in "Phases 0/A–E + strands" that each *became* a
  numbered build; later arcs dropped phase language and go straight to builds.
- The **Deferred acceptance ledger** (batched behind Phase D, because upgrading before the
  durable upgrade path existed risked destroying the live vault, `arc1-roadmap:346-358`).
- **Owner-steered ideation with recorded rulings** (Phase C scoping record, Phase D
  ideation record, `arc1-roadmap:451-489`).
- **Spike records** (B2 installer spike).
- **Round-2 capture inside the same roadmap** — acceptance-run defects captured, ideated,
  built (build-10/11) without opening a new arc.
- **Grounding corrections as first-class citizens** (filing #1 already-shipped, #7 wrong
  diagnosis, R2-1 provenance correction).
- Mid-arc process fossils minted: governance SSoT collapse; parse-args standing rule;
  always-quote; no-.decision-log.

**Arc 2 (2026-07-03 → 07-06, builds 12–13, v0.5.0)** — the loop tightens:
- Acceptance **unbatched**: rides the next ordinary upgrade (`arc2-roadmap:268-270`).
- The **verdict-graded capture style** matures into the reference exemplar the
  inbox-capture skill now points at.
- **Spike-at-ideation formalized** with a closed spike record in the roadmap (F1,
  `arc2-roadmap:231-247`).
- **Upstream-vs-local boundary ruled:** builder-template drift "must be **filed upstream to
  BMAD-METHOD** (owner action)", not patched here (`arc2-roadmap:225-229`) — the seed of
  CLAUDE.md's "What not to touch".
- Acceptance discharge **by field evidence** (build-13 confirmed run-in-anger by a later
  filing).

**Arc 3 (2026-07-06 → open, builds 14–16, 18, v0.6.0)** — the loop gets teeth (it is
literally "the enforcement arc" and the factory dogfoods it):
- **CLAUDE.md written** (`6f21952`, 2026-07-06) — lifecycle + standing rules finally
  codified out of two arcs of scar tissue.
- **inbox-capture becomes a skill** — capture formalized with headless mode and a written
  grounding methodology.
- **package-lint.py** — the first mechanical lifecycle gate (build-14), with the PASS line
  in the release commit making a skipped lint visible in history.
- **Ideation rulings section made explicitly binding** ("Briefs cite this section, never
  re-litigate", `arc3-roadmap:507-509`), including "cross-filing decide-once rulings" and
  "questions deliberately left to brief time".
- **Spike obligations declared at ideation and closed inline** (Bases syntax,
  `arc3-roadmap:550-565`).
- **Design-stage filings with declared evidence debts** admitted into capture, tracked as
  "pending attachments" in the ledger (`arc3-roadmap:619-622`).
- **Coordinated-bump discipline** (one `frontmatter@3` walk across three filings rather
  than three churning bumps, `arc3-roadmap:51-57`) and an **arc-wide design invariant**
  ("derive-first … Any build in this arc proposing a stored counter is wrong by ruling,
  not by taste", `arc3-roadmap:451-456`).
- **Filing archival criterion tightened** to ship+acceptance.
- The through-line is self-referential: the arc's diagnosis of the vault ("vault state
  lives in prose, so nothing can count, trigger, or trip") applies verbatim to this repo's
  own lifecycle — 091002 is "the factory-side worked instance" (`arc3-roadmap:48-49`), and
  its open question 4 proposes registering the packaging lint as the release boundary's
  `checked_by`, "making the module repo the doctrine's first fully `checked` boundary"
  (`arc3-roadmap:486-489`).

---

## 4. Lifecycle steps still pure discipline — candidates for formalization

Ranked by evidence that discipline has actually failed or nearly failed there:

1. **Release choreography beyond the lint** (branch → dual bump → lint → PASS line in
   commit → ff-merge → tag → push). Group D covers the dual bump *if the lint runs*, but
   nothing forces the run (no hook/CI — confirmed absent at `arc3-roadmap:153-155`; only
   the PASS-line-in-commit convention makes skipping *visible after the fact*). Historical
   evidence of this step's fragility: the 0.3.0 bump had to retro-fix marketplace `skills[]`
   omissions (`arc1-roadmap:432`); every 0.3.0–0.5.0 tag shipped a packaging defect
   (`arc3-roadmap:146-148`). A release skill (or pre-tag hook) wrapping the whole sequence
   is the obvious next bell. Note 091002's own open question already points here
   (retroactive `checked_by` registration once the doctrine exists factory-side).

2. **Brief-writing.** The most conventionalized unformalized artifact: frontmatter shape,
   F-site grounding, dispositions, deviation-recording in `status:`, and the
   append-acceptance-checks-to-ledger step are all imitation of prior briefs. The
   inbox-capture skill proves the codification pattern works (references/ files carrying
   methodology + a named style precedent). Failure evidence is thin but real: build-15's
   faithfulness check couldn't run because a vault-side sequencing dependency wasn't
   surfaced until build time (`build-15:3` deviation 1); Arc 1's early phases had scope
   discovered-already-shipped at ideation because capture hadn't grounded (now fixed
   upstream of briefing).

3. **Arc close-out / archival.** Multi-step and entirely manual: discharge ledger items
   with evidence, mark roadmap CLOSED with the do-not-append banner, `git mv` roadmap +
   briefs to `skills/reports/archive/`, move accepted filings to `inbox/archive/`, sync
   Claude project memory ("keep it in sync with the arc roadmap docs when builds/releases
   land", CLAUDE.local.md). Failure evidence: Arc 1's roadmap "simply never recorded" a
   shipped fix (`arc1-roadmap:68`); inbox/README's archived-so-far paragraph
   (`inbox/README.md:22-28`) is itself a completeness-claiming list of the kind CLAUDE.md
   warns drifts (it describes 10 filings; the archive now holds 15).

4. **Ideation rulings capture.** Owner-steered by design (should stay human-led), but the
   *recording* discipline (rulings section shape, decide-once dedup across filings, spike
   obligations) could be scaffolded the way inbox-capture scaffolds grounding.

5. **Live-acceptance discharge.** Owner runs the upgrade; mapping upgrade-ledger evidence
   back onto the roadmap's checkboxes (and then archiving filings) is manual bookkeeping
   with a clear input (vlt-core's `_agent/upgrade-ledger.md`) and output (ticked ledger,
   moved filings) — mechanizable.

6. **Handshake bipartite-consistency verification** at build time is a recurring manual
   grep ritual ("Handshake re-verified bipartite-consistent" appears in nearly every build
   record) — a natural candidate for a factory-side check the way lint group B imports
   `HEADER`. (Vault-side, vlt-lint does this; factory-side it's re-derived by hand each
   build.)

Counter-observation: the repo's own philosophy cuts against over-formalizing — "defer
until it bites" is applied everywhere (unrouted retirement, pattern-catalog YAGNI at n=1,
`arc2-roadmap:254-256`). The steps above are the ones that have *already bitten*.

---

## 5. Currently in flight (as of 2026-07-12)

- **Arc 3 is OPEN, acceptance pending.** `arc3-roadmap:3`: v0.6.0 SHIPPED 2026-07-08
  (builds 14+15+16+18, commit `a117f4f`, tagged, pushed; pre-tag lint A/B/C/D PASS
  recorded in the commit). "Next: live acceptance — rides the next vlt-core vlt-upgrade
  run (owner runs it)" (`arc3-roadmap:658-662`).
- **The six 091001–091006 filings are still in the live `inbox/`** — correct per the
  tightened rule (shipped but not yet accepted).
- **build-17 (enforcement kit, 091003) is briefless by design** — "brief when its
  vault-side evidence matures (trails into 0.6.x/0.7.0)" (`arc3-roadmap:3`).
- **Two UNCAPTURED filings landed 2026-07-11** (after the arc's capture run):
  `2026-07-11-114226-research-note-graduation-queue.md` (a `frontmatter@4` proposal — the
  research-zone complement to build-16's `review_after`) and
  `2026-07-11-153000-graduation-queue-field-calibration.md` (field evidence from a 90-note
  audit that **materially changes the first filing's design**: the specced orphan
  projection is ~79% false-positive; `cluster_ripe` not viable on current topic data;
  K-threshold accretion wasn't the observed pattern). They must be captured together
  (`…153000:53`), and per the inbox-capture skill they'd append to the open Arc 3 roadmap
  (an open-arc amend, the skill's first exercise of that branch) — or await Arc 4; that's
  a capture-time owner call. The calibration filing also flags that the *work vault* is
  the real pathology site but has no inbox access, and acceptance for that mechanism
  "should happen there, not here" (`…153000:9`) — a first-ever second-vault acceptance
  requirement.
- **Hard gates standing:**
  - No new partner mint on vlt-core before the spec convention is minted there, **from the
    shipped text** so the divergence check self-clears (`build-15:3`; memory + roadmap).
  - Pre-tag lint `--expect-version` on every future tag; standing success metric "zero
    packaging filings into inbox/ for releases ≥ 0.6.0" (`arc3-roadmap:586-588`).
  - Derive-first invariant binds any future Arc 3 enforcement build (`arc3-roadmap:451-456`).
- **Open ledger items** (`arc3-roadmap:576-622`): the four per-build 0.6.0 acceptance
  bullets (esp. build-16's consumer-walk convergence + flood-free first lint, build-18's
  subsumption-retire + manifest seed on that very upgrade); the vlt-track loop-profile
  watch item **carried since Arc 1**; the owner action to file BMB template drift upstream
  to BMAD-METHOD (carried since Arc 2); three design-stage evidence debts (091003 M0
  audit, 091005 M4 lint cycles, 091006 first review-cycle).
- **This handoff's own directory** `skills/reports/handoff-2026-07-12/` sits inside the
  gitignored dev-artifact zone (`skills/reports/` is gitignored per CLAUDE.md Git &
  publishing), so it will not ship.
