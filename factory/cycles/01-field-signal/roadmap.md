---
title: 'Inbox Evolution Roadmap — folding the vlt-core field signal back into the module'
status: 'CLOSED — SHIPPED (arc 1: builds #3–#11 + strands merged to main, published v0.4.0 2026-06-25). Archived 2026-06-30. Arc 2 (2026-06-27 capability-field-hardening filings) tracked in a separate roadmap.'
build_log: ''
derives_from:
  - 'inbox/2026-06-06-125403-vlt-setup.md'
  - 'inbox/2026-06-06-130940-librarian.md'
  - 'inbox/2026-06-06-193105-vlt-lint-full-infra-and-cost-fixes.md'
  - 'inbox/2026-06-07-095509-wiki-category-topic-frontmatter-model.md'
  - 'inbox/2026-06-09-092306-vlt-mint-phases-and-planning-doc.md'
  - 'inbox/2026-06-09-092514-personalized-extraction-model.md'
  - 'inbox/2026-06-13-092848-council-args-not-threaded.md'
  - 'inbox/2026-06-13-100300-upgrade-ownership-and-divergence-durability.md'
  - 'inbox/2026-06-15-163847-vlt-dispatch-partner-communication-bus.md'
  - 'skills/reports/vault-module-plan.md (shipped baseline)'
module_code: 'vlt'
created: '2026-06-13'
updated: '2026-06-23'
related_design_strands:
  - 'skills/reports/vlt-partner-capabilities-ideation.md (Capability object / lightweight tier — ideation complete 2026-06-15; threads Phases B/C/D)'
build_log:
  - 'Phase 0 (systemic args fix) COMPLETE 2026-06-13 — empirically diagnosed (the Workflow runtime delivers args as a JSON STRING, not a dropped object; true for name/scriptPath/inline alike), then patched both shipped workflows (vlt-review-council.js + vlt-lint-full.js) with a parse-on-intake guard. Verified the council guard now passes. Dissolves filing #7''s "harness defect" + "scriptPath-by-default" open questions and filing #3''s blocker. No caller changes needed.'
intent: >
  Capture EVERYTHING the live vlt-core agents have filed since Build #2 shipped, in one
  durable, resumable document; then ideate + build it in phases. This roadmap is the cache —
  it spawns per-build briefs (build-3-*.md, build-4-*.md, …) the same way vault-module-plan.md
  spawned the Build #1/#2 briefs. Decision: evolve ALL of it (nothing cut), sequenced into phases.
proposed_phases:
  - 'Phase A — Stop the bleeding (tactical robustness): args-threading + lint-full cost/accuracy + setup SSoT'
  - 'Phase B — Coherence: convention→consumer propagation discipline + the category/topic schema (its worked example) + source-count drift cleanup'
  - 'Phase C — Mint maturation: explicit phases + resumable planning doc + vertical-partner archetype + personalized extraction'
  - 'Phase D — Lifecycle durability: the durability principle + vlt-upgrade skill + merge-not-replace registration + agent-zone relocation'
  - 'Phase E — Identity polish: naming home in the two-tier model + frontmatter-read-before-write + the two outstanding Build #1 owner gates'
  (phasing is a PROPOSAL — to be refined during per-phase ideation)
---

# Inbox Evolution Roadmap

## The through-line (why these nine filings are one story)

Vault was designed to **grow** — mint partners, amend conventions, accrue history. Since Build #2
shipped it actually **has**, in `vlt-core` (a 65-page wiki, three partners minted in anger: Dog
Trainer, Health Coach, Chef). The nine inbox filings are the sound of a self-evolving system
hitting the parts of its **own lifecycle that were never designed** — including the moment one
minted partner needed to hand durable work to another and found **no pickup path** (filing #9):

> The machinery is excellent at *making* things and weak at *preserving integrity across change* —
> in two directions. **(1) Vault-specific evolution** (a vault's own minted partners, its local
> convention edits, its mint history) can be silently destroyed by the generic, module-agnostic
> BMad upgrade installer. **(2) Generic evolution** (a redesigned convention) can fail to propagate
> to every skill that consumes it, sitting latent as drift. Durability and coherence are the same
> gap from opposite ends.

Everything else clusters around that core: the **mint engine maturing** from three real gated mints,
**tactical robustness** bugs (one of which — args-threading — blocks every council-gated mint
*today*), **identity-model polish**, and a concrete **convention content** upgrade that doubles as
the worked example for the coherence machinery.

---

## Capture — all nine filings

Each entry: the source, a one-line essence, the **concrete module-side changes the filer specified**,
the **artifacts touched**, **open questions** the filer left for the maintainer, and a **priority/risk**
read. Nothing is cut; phasing comes after.

### 1. vlt-setup friction (2026-06-06) — `…125403-vlt-setup.md`  — ✅ RESOLVED (commit `c918274`)
**Status (verified 2026-06-23 during Phase A ideation):** **ALL of filing #1 is already shipped** in commit `c918274` ("vlt-setup field-test fixes: single-source vault_structure, dependency check, installer-wart note") — the roadmap simply never recorded it. Confirmed against the current `vlt-setup/SKILL.md` + `assets/module.yaml`: (a) **`vault_structure` SSoT done** — `module.yaml` `vault_structure.default` is the canonical map with a "SINGLE SOURCE OF TRUTH" comment; the SKILL reads it and explicitly says "do not hand-transcribe the table below" (the markdown table is marked illustrative-only); the temp-JSON write sources from `module.yaml`. (b) **dep-check false-negative fixed** — counts host/global-provided skills as present ("not found in project skills (may be host-provided)"). (c) **`[object Object]` wart acknowledged** in the confirm summary. (d) **traps hoisted** — `uv run`-not-`python3` and the `{project-root}`-literal-vs-resolved-`$ROOT` trap are at the top of *Write Files*. **Nothing left to build.** *(Filing #2's "partner SKILLs re-list a path subset" is a separate, still-open Phase-E concern — not part of #1's setup fixes.)*

**Essence (original):** A clean fresh install went smoothly; three drift/robustness warts surfaced.
**Changes specified:**
- **Dependency check false-negatives** — SKILL checks `{project-root}/.claude/skills/` and so reports host/global skills (e.g. `deep-research`) as MISSING. Fix: check the real skill registry, or soften to "absent from project skills *and* not host-provided."
- **`vault_structure` default map has no single source of truth** (the biggest one) — the map lives in three hand-synced places (SKILL.md markdown table → temp answers JSON; runtime skill fallbacks; materialized `config.yaml`). Fix: put the canonical map in `module.yaml` (or a shipped asset) and have setup *read* it rather than transcribe a table.
- **Installer `[object Object]` wart** — `config.toml` literally contains `vault_structure = "[object Object]"`; Vault correctly ignores it (reads YAML) but it's a debugging landmine. Optional fix: acknowledge it in the setup confirm summary.
- **Minor:** SKILL.md density (repeated never-clobber/cleanup warnings); hoist the two load-bearing traps (`uv run` not bare `python3`; `{project-root}` literal-in-config vs resolved-`$ROOT`-in-shell-args) to the top. Date-stamping depends on the agent knowing today's date.
**Artifacts:** `vlt-setup/SKILL.md`, `vlt-setup/assets/module.yaml`, runtime skill fallbacks.
**Open questions:** none material.
**Priority/risk:** Medium pain, low design risk. The `vault_structure` SSoT is the durable win (it's a *coherence* problem too — see filing #8's durability principle).
**Protect (don't regress):** idempotent `vlt`-scoped merge scripts; skip-if-present governance install; explicit fresh-vs-reconfigure branch.

### 2. Librarian first-breath field notes (2026-06-06) — `…130940-librarian.md`
**Essence:** Gwyn's first activation in an empty vault — the birth ritual held up; four identity/ordering frictions surfaced.
**Changes specified:**
- **Naming has no home in the two-tier identity model** (the conceptual one). When named "Gwyn," the partner had to choose `## Self` / `## Bond` / gated-rebirth — and the two-tier test (refuses-to-do / core-expertise / capabilities → gated; how-it-sounds → `## Self`) doesn't cleanly cover *a name*. Filed to `## Self` as least-wrong. Suggestion: name identity explicitly — bless the partner's name as a first-class `## Self` fact, or give it its own line.
- **Wrote before reading the frontmatter standard** (latent) — activation reads the contract but *not* the convention files; the contract deliberately doesn't restate the frontmatter schema (it lives only in `frontmatter.md`). The "read on activation" set and the "what I need before my first write" set don't line up. Suggestion: fold base frontmatter fields into the internalized SKILL rules, **or** make "read `frontmatter.md` before your first write" an explicit beat.
- **Path map split across two sources** (minor) — SKILL "On activation" enumerates a subset of logical paths; the full `vault_structure` map (incl. `sessions`, `research`, `personas`, `archive`) lives in `config.yaml`. Suggestion: SKILL points at the map as the single source rather than re-listing a subset. *(Same SSoT theme as filing #1.)*
- **Cold start reads ~7 files to find emptiness** (acceptable) — correct behavior; flagged as observed shape only.
**Artifacts:** operating contract, partner SKILLs (librarian/researcher/creative), `vlt-mint/assets/partner-agent-template.md`.
**Open questions:** **Is renaming a partner a free `## Self` act, or ceremonial / council-gated?** The module is silent and the filer wants an opinion baked in.
**Priority/risk:** Low-to-medium pain, but *conceptual* — touches the contract and every partner stamp. Relates to the two outstanding Build #1 owner gates (cold-start/warm outside-read; rebirth two-tier check).
**Protect:** don't-invent-baselines cold-start instruction; two-beats-as-birth metaphor; write-as-you-learn for `## Self`/`## Bond`.

### 3. vlt-lint-full infra + cost (2026-06-06) — `…193105-vlt-lint-full-infra-and-cost-fixes.md`
**Essence:** First real `--full` lint of a 65-page wiki succeeded (78 agents) but only after a blocker workaround and at ~10× the necessary cost.
**Changes specified (filer's own priority order):**
1. **BLOCKER — `args` arrives as a JSON *string*, not an object.** Named-invocation `Workflow({name:'vlt-lint-full', args:{…}})` delivered `args type: str` (len 7393) → guard tripped, 0 agents. Fix in `vlt-lint-full.js`: `let a = args||{}; if (typeof a==='string'){try{a=JSON.parse(a)}catch{a={}}}`. **Doc gotcha:** resuming with `resumeFromRunId` *without* re-passing `args` nulls them — re-pass on resume. *(Sibling of filing #7 — same systemic args defect.)*
2. **COST — per-page scanners should default to a cheap model (~10× win).** ~65 of 78 agents are pure structured extraction (no deep reasoning) but ran on Opus (~2.1M tokens). Add `scanModel||'haiku'`, `indexModel||'sonnet'`, `clusterModel||'sonnet'`, pass on respective `agent()` calls, annotate `meta.phases[].model`.
3. **CONVENTION DRIFT — index pass still polices source counts the redesigned `wiki-index.md` removed.** `INDEX_SCAN.sourcecount_fixes`, `index_sourcecount_fixes`, and the index-agent prompt all compute count corrections the convention says don't exist. Strip from schema/prompt/report. **Same drift in the `vlt-lint` SKILL** ("correct source counts against the pinned definition"). *(This is the coherence theme #8 — a convention redesign that didn't reach its consumers.)* — **⚠️ DEFERRED TO PHASE B (decided 2026-06-23 during Phase A ideation):** the redesign that removed source counts was a **local vlt-core edit never upstreamed**. In the *module source*, `wiki-index.md` still carries a full "Source count — the pinned definition" section (the writer sets counts, `vlt-lint` auto-fixes them) — so the consumers are **correctly in sync** and stripping them now would *create* drift. This cleanup is entangled with the counted-row→structural-map index redesign that belongs to Phase B (the category/topic schema work — filing #4 §5). Pull it forward only by also redesigning the convention. **Not in build-3.**
4. **ACCURACY — move deterministic checks into the JS reduce.** Per-page LLM scanners under-detected a rule-6 inline-metadata violation present on all 65 pages (flagged ~11), and false-positived summary length (em-dash/arrow miscount, even on Opus). Do rule-6 (`^>\s*\*?Last updated:` grep) and summary-length (read `summary:`, count chars vs 160) in JS — free, exhaustive. Related: **cross-layer wikilinks** (14 of 17 `missing_targets`) were valid `[[…]]` to `_agent/research/` notes; resolve targets against the whole vault (or `{research}` basenames) before declaring missing.
5. **NOISE — near-dup heuristic over-fires.** `shared outbound links ≥ 3` flagged 70 pairs, all false (hub/entity co-citation). Fix: exclude cluster-hub links before counting / Jaccard with high threshold / require shared-links AND a secondary signal (slug-stem or title similarity).
6. **MINOR — contradiction-cluster cap** (`clusterCap=12`) sat just below the 13 natural clusters; scale default with page count.
**Artifacts:** `.claude/workflows/vlt-lint-full.js`, `vlt-lint/SKILL.md`.
**Open questions:** none material.
**Priority/risk:** #1 blocker + #2 cost are high-value, low-risk. #3 is coherence. #4/#5 improve accuracy.
**Protect:** fan-out + JS-reduce split; `files_checked`/`files_listed`/`coverage_caps` honesty; read-only finder + single-writer; `contradictions_handled` (Gap B).

### 4. wiki category/topic frontmatter model (2026-06-07) — `…095509-wiki-category-topic-frontmatter-model.md`
**Essence:** Split the overloaded `topic:` string into `category:` (single Title-Case, = a wiki index H2, grouping key for Obsidian Bases) + `topic:` (lowercase YAML list, general→specific, filtering axis). Reference impl: branch `frontmatter-category-topic`, commit `a4af503` (74 files).
**Changes specified (exact, module-side):**
- **`conventions/frontmatter.md`** — wiki schema: add `category:`, convert `topic:`→list; add a "grouping vs filtering" subsection (the why-two-fields rationale: Bases group-by wants one value/page; dedicated `category` is legible, lint-enforceable, decoupled from list ordering); research-note schema: `topic:`→list, explicitly **no `category:`**.
- **`conventions/wiki-index.md`** — add "The `category:` binding" (every `category:` = an existing H2; rename/merge rewrites all affected pages in the same edit; lint validates; index keeps finer within-category structure); update writer/validator contract table.
- **`vlt-ingest` SKILL** — wiki template: add `summary:` (was missing entirely!), `category:`, `topic:` list + "never invent a category outside the index H2 set"; research template `topic:`→list; Step 9 verify adds category/summary/topic checks.
- **`vlt-lint` SKILL** — Step 2/3 add "Frontmatter / Bases-field drift" check+fix; Step 5 report schema add `fix_now.frontmatter_drift` + `flag_for_human.category_no_match`.
- **`vlt-lint-full.js`** — `PAGE_SCAN` returns `category`/`topic_is_list`/`summary_issue`; `INDEX_SCAN` returns `category_violations`; reduce emits the two new report keys.
**Migration:** one-time data migration (add `category:` = index H2; `topic:` string→list) — judgment per page, not mechanical. Reference: dry-run-first `migrate_category_topic.py`. **Module action:** ship a `vlt-migrate` helper or documented upgrade recipe; warn the change is not backward-auto-filled.
**SEPARATE BUG surfaced (§5):** the earlier index-redesign (counted-row → structural map) updated `wiki-index.md` but NOT `vlt-ingest`/`vlt-lint`/`vlt-lint-full` — drift sat latent through a whole migration. **Process rec:** a tracked **convention→consumer dependency map** so a convention edit has a checklist of skills to update. *(This is the seed of the coherence phase.)*
**Artifacts:** `frontmatter.md`, `wiki-index.md`, `vlt-ingest/SKILL.md`, `vlt-lint/SKILL.md`, `vlt-lint-full.js`; possible new `vlt-migrate`.
**Open questions:** topic casing (chose lowercase incl. acronyms — confirm); keep/drop general→specific ordering (readability-only); should research notes ever carry `category`; should `vlt-setup` ship a starter `wiki-index.base` with `groupBy: category`.
**Priority/risk:** Medium-high. The schema is well-reasoned and reference-implemented; the *coherence rec* it surfaced is architectural.

### 5. vlt-mint phases + resumable planning doc (2026-06-09) — `…092306-vlt-mint-phases-and-planning-doc.md`
**Essence:** A live gated mint (Dog Trainer) slid from ideation→build with no phase boundary to approve the brief, and all session state lived only in context (closing mid-flow = total loss; `.decision-log.md` is post-hoc).
**Changes specified:**
- **Three named phases** in `vlt-mint` SKILL, each with an explicit **Exit gate**: **1·Ideate** (resolve kind/subject + becoming convo → gate: user confirms brief); **2·Validate** (blast-radius + council + resolve `revise`/open decisions → gate: verdict resolved + decisions ruled); **3·Build** (author + install/register/record → gate: verified + offer to commit). Regroup existing steps under these headers — content mostly unchanged, boundaries are new.
- **Resumable planning doc — gated kinds only** (`new partner`, `persona self-edit`, `convention edit`; keep `operation skill` + `capability migration` ceremony-free). Location: `_agent/mint/{YYYY-MM-DD}-{slug}.md` (agent-zone, contract-sanctioned). Contents: kind; brief; architecture decisions+rationale; staged-artifact absolute paths; current phase + done/pending checklist; council verdict; open decisions+resolutions. Created at Phase 1, updated at each boundary; new **resume activation branch** reads it.
- Operating contract (optional, 1 line): name `_agent/mint/` as a known working location.
**Artifacts:** `vlt-mint/SKILL.md`, operating contract (optional).
**Latent bug surfaced:** `workflow('vlt-review-council', {name-form})` delivered empty `args`; the inline `workflow(name, args)` form worked. *(→ filing #7.)*
**Open questions:** auto-scan `_agent/mint/` for resume on every activation (rec: yes); leave vs archive completed doc (rec: leave); does the resumable-working-doc pattern generalize to other multi-phase ops (defer, n=1 caution).
**Priority/risk:** Medium. Pure additive skill edit, no migration. High UX value for gated mints.

### 6. Personalized extraction — bounded provenance widening (2026-06-09) — `…092514-personalized-extraction-model.md`
**Essence:** The first **vertical (domain) partner** (Dog Trainer) needs a deliverable that's part general method (wiki) + part the user's lived state (agent-zone) — colliding with the contract's most load-bearing rule (PARA is written only through extraction, which draws from the wiki only). Council `revise`→pass (full panel).
**Changes specified (exact; the amended `extraction.md` is in the vault at commit `4154b12`, lift verbatim):**
- **`extraction.md`** — add "## Personalized extraction — drawing on agent-zone state": hard invariant (every method/general claim traces to a wiki page in `sources:`) unchanged; soft parameter (a personalized extraction may *additionally* read the partner's agent-zone operational data, cited in a **separate `personalization_sources:`** field, never in `sources:`); n=1 scope bound to `vlt-track` by name; operational-log discipline (state, never method). Plus pointer clauses in *What extraction is* / *Required frontmatter* / *Skill flow*.
- **Operating contract** — `{log}` `<type>` set stated **non-exhaustive** (ops may coin a type, e.g. `track`), mirroring the non-exhaustive `type:` set. One-line (commit `4154b12`).
- **`vlt-agent-creative` SKILL** — one-line carve-out in the non-negotiable (a domain partner's personalized extraction may list an agent-zone path under `personalization_sources:` — same single write-path, bounded widening, not a second one).
- **`frontmatter.md`** — no change (already defers PARA frontmatter to `extraction.md`; `personalization_sources:` is a bare-path list under YAML rule 4). Single-home held.
- **`vlt-mint` templates/docs** — document the **vertical (domain) partner** as a recognized archetype alongside horizontal (function) partners: names its domain self-awarely, typically needs its own op skill, may need a bounded convention widening.
**Migration:** additive/reversible; `personalization_sources:` optional+absent on every standard extraction. Rollback ~ the few `vlt-track` protocol files.
**Latent bug surfaced:** the council args-threading defect (→ #7). **Enforcement gap (filed to vault backlog):** the method-traces-to-wiki firewall is prose + a verify checkbox; **ship a `vlt-lint` check** that flags (a) a personalized artifact whose body method-claims aren't covered by its wiki `sources:`, and (b) an operational log carrying method/general knowledge.
**Open questions:** make `personalization_sources:` general (any extraction) vs stay gated per-op (current: gated); promote "vertical vs horizontal partner" to a first-class contract concept now (n=1) or wait for n=2; ship the `vlt-lint` firewall check as a *precondition* (skeptic) vs follow-up (vault deferred — module may want them together).
**Priority/risk:** Medium. Council-validated design; the open n=1-vs-generalize and the lint-firewall-precondition calls are the real decisions.

### 7. Council `args` not threaded (2026-06-13) — `…092848-council-args-not-threaded.md`  — ✅ RESOLVED in Phase 0
**Essence:** **Every council-gated mint fails on the first try.** Name-invoking `vlt-review-council.js` with a populated `args` object → the guard refuses (~3ms, 0 agents). Reproduced on all three gated mints (Dog Trainer, Health Coach, Chef).
**Root cause — CORRECTED by Phase 0 empirical test (2026-06-13):** the filing's "harness didn't thread args / args empty" diagnosis was **wrong**. The Workflow runtime delivers `args` as a **JSON-encoded string** (confirmed for name-, scriptPath-, *and* inline-script invocation alike). The council code did `const a = args || {}` (the string is truthy), then read `a.mode` → `undefined` → the guard reported `mode: null`, which *looked* like a drop. It was never dropped — just unparsed. **Cure: parse on intake** (`if (typeof a==='string') a=JSON.parse(a)`) — this is filing #7's "harden #1", and it turns out to be the *complete* cure, not a partial mitigation. The baked-in recoveries (#1 inline-and-rerun, #5 driver-script) only worked because they sidestep the unparsed-string path. **Dissolved:** the "escalate harness defect upstream" and "prefer scriptPath by default" open questions (nothing to escalate; scriptPath delivers the same string). **No caller changes** — both callers already invoke by name correctly.
**Changes specified:**
1. **Harden `vlt-review-council.js` args intake** — `let a=args||{}; if (typeof a==='string'){try{a=JSON.parse(a)}catch{a={}}}` (defends the stringified variant; does *not* rescue total-drop).
2. **Document the recovery in both callers** (`vlt-mint` Step 2a + `vlt-review-council` SKILL Step 2): if the guard error returns, take the persisted script path, inline the inputs (replace `const a = args||{}` with a literal `{mode,kind,subject,personasPath}`), re-invoke `Workflow({scriptPath})`. Capture stays mandatory.
3. **(Optional, stronger)** extend the guard's error `note` to name the likely cause + fix inline.
**Artifacts:** `vlt-review-council.js`, `vlt-mint/SKILL.md` (Step 2a), `vlt-review-council/SKILL.md` (Step 2).
**Latent:** the **debate path** shares the defect (call the same workflow the same way). Note: `new partner` KIND_PANEL = `['architect']` only (single lens) — Health Coach + Chef logs both flag "thinner than ideal"; a separate KIND_PANEL decision.
**Open questions:** escalate the harness defect upstream (is there a channel?); **prefer scriptPath invocation by default** if it threads args reliably where name does not (would remove the failure entirely vs recovering from it) — worth a maintainer test.
**Priority/risk:** **HIGHEST PAIN — blocks every gated mint today.** Low-risk hardening + docs. The "scriptPath by default" test could be the real cure.

### 8. Upgrade ownership + divergence durability (2026-06-13) — `…100300-upgrade-ownership-and-divergence-durability.md`
**Essence:** The deepest filing. Vault self-evolves *into* a vault, but upgrades run through the generic, module-agnostic BMad installer — which can silently destroy/deregister vault-specific evolution on every version bump.
**Concrete losses identified:**
1. The mint **decision log** lived in a clobber-prone skill dir (`.claude/skills/vlt-mint/.decision-log.md`) — a version upgrade replacing `vlt-mint/` destroys it. **(Fixed locally — §A1.)**
2. **Locally-minted partners aren't in the module source** → two independent upgrade hazards: **body** (clean-replace of `.claude/skills/vlt-*` deletes unshipped `vlt-agent-*`, orphaning their `_agent/partners/` memory) and **registration** (`merge-help-csv.py` is anti-zombie — strips all `vlt` rows and rewrites from the *bundled* CSV, which won't contain this vault's mint rows → deregistered even if dirs survive).
3. **Convention divergence is invisible** — skip-if-present protects local edits (good) but a new version's *improved* conventions silently don't apply, with no drift notification either way.
**The durability principle (propose adding to the operating contract):** *Two classes of evolution, two fates.* Generic evolution → upstream (file to module, ship, receive on upgrade). Vault-specific evolution (minted partners, local convention edits, mint/decision history) must be **upgrade-durable** — it lives in the agent zone (`_agent/`, never overwritten) or is reconciled by **merge, never replace**. Durability becomes a property of *location + merge strategy*, not of getting an upgrade procedure right.
**Changes specified:**
- **§A1 (shipped locally — mirror in module):** relocate decision log → `_agent/mint/decision-log.md` + pointer stub; `vlt-mint/SKILL.md` both refs → new path; `vlt-setup` ensures `_agent/mint/` exists; idempotent `.decision-log.md`→`_agent/mint/` migration (mirrors the legacy `thread.md`→two-file split).
- **§B1 — minted-partner registration: merge, don't replace.** (preferred) preserve local mint rows whose `vlt-agent-*` skill exists in live `.claude/skills/` but is absent from the bundled CSV; rewrite only shipped rows. (alt) durable mint registry `_agent/mint/roster.md`, re-derive help rows from there.
- **§B2 — minted-partner bodies must survive the installer copy.** A Vault upgrade must not delete unshipped `vlt-agent-*` dirs. *Could not be confirmed from inside the vault — determines whether B2 is already safe or actively broken.*
- **§B3 — governance divergence: detect + report** (floor; full 3-way merge is nice-to-have). On update, for each governance file that exists locally AND differs from shipped, report in the confirm summary.
- **§C — new `vlt-upgrade` skill** that owns the lifecycle: pre-flight (snapshot divergence ledger of non-stock state) → refresh (installer copies first) → reconcile (merge never replace; restore/re-register dropped mints; run migrations; report+offer merge on divergent governance) → post-flight divergence report → hand off to `vlt-setup` for provisioning. `vlt-upgrade` *calls* `vlt-setup`; doesn't duplicate it.
- **Operating contract** — add the durability principle.
**Artifacts:** `vlt-mint/SKILL.md`, `vlt-setup` (provision step + B3), `merge-help-csv.py` (B1), installer contract / new `vlt-upgrade` (B2), operating contract.
**Open questions:** **installer copy strategy (blocks B2)** — purge unshipped dirs, or copy-over-and-leave?; can `vlt-upgrade` control the installer or is it always "installer runs, then reconcile after" (design assumes latter); ledger location/name (`_agent/mint/divergence.md` vs top-level `_agent/upgrade-ledger.md` — spans more than mints); **should some current local mints be upstreamed** (Dog Trainer reads as a generic vertical worth shipping; Health Coach/Chef may be vault-specific).
**Priority/risk:** **Highest architectural value.** The "evolve the architecture" core. B2 has an unresolved external dependency (installer behavior) that must be confirmed before it can be specified.

### 9. vlt-dispatch → the partner communication bus (2026-06-15) — `…163847-vlt-dispatch-partner-communication-bus.md`  — already applied in vlt-core; mirror into module
**Essence:** `vlt-dispatch` shipped as a **daily-note router** (human-capture → partner) and solved nothing for **partner → partner**. Live evidence: a Health-Coach→Chef nutrition-spec handoff sat at `_agent/handoffs/2026-06-13-…` with **no pointer telling the Chef it was waiting** — a durable handoff with no pickup path. **Validated insight:** dispatch's drain (open pointer + slug-grep + check-off) is **source-agnostic**, so the cure is to *generalize the existing record into a multi-intake bus*, not build a second mechanism. **Status:** designed + applied in the vlt-core install; this filing is the **mirror-into-module-source** spec.
**The decision:** `vlt-dispatch` becomes the **vault's partner communication bus — one record (`_agent/dispatch.md`), one drain, three modes:**
- **`daily`** — the original scan/classify/route, now an explicit subcommand; **only this mode reads `daily/`** (human-zone boundary tightens — relay/ledger never touch it).
- **`relay`** (NEW) — a publishing partner supplies a pre-addressed `(to-slug, gist, handoff-path)`; dispatch appends a `relay: A → B` pointer. Destination is **known**, so classification is skipped. **Thin scribe, not gatekeeper** (YAGNI — mirrors the `unrouted` retirement). **Single-writer preserved:** the publisher never writes `_agent/dispatch.md`; it invokes the Librarian's `relay` op, which writes on its behalf.
- **`ledger`** (NEW) — read-only open board (grep whole record for open items, grouped by partner, across daily + relay); promoted from the inline standing-ledger report into its own callable mode.
- **Bare invocation → mode menu** (the menu is the home, not a silent default).
**Why generalize, not fork:** every mode emits the *identical pointer line* into the *identical record*, drained by the *identical pickup loop*; the header shape (`relay: A → B` vs `daily/… (routed through line N)`) **is the mode signal** and selects the idempotency rule.
**Relay idempotency** — keyed on `(handoff-doc-path, recipient-slug)`: no pointer → append; **open** pointer exists → no-op (kills re-relay spam); latest pointer **checked off** → re-relay = new info → append fresh. Forces a **handoff lifecycle rule:** durable handoffs are **updated in place at a stable path**, not versioned into new files.
**Changes specified (exact, module-side):**
- **`skills/vlt-dispatch/SKILL.md`** — replace wholesale with the bus version: frontmatter `description` (three modes; "reads daily/ only in `daily` mode"); Overview (bus framing + source-agnostic drain + single-writer-holds-for-relay); On-Activation adds `_agent/handoffs/` to not-in-structure-map locations; new **Mode dispatch** section; `daily` mode = prior Step 0/Classify/Write/Report verbatim-in-substance, now nested, ending with inline `ledger` print; `relay` mode (who-fires + the **relay-when-done reflex full text — this is its single home**, inputs/validation incl. light liveness, the `(doc-path, recipient-slug)` rule, stable-path lifecycle note pointing at the contract, `relay: A → B` block format, brief report); `ledger` mode (read-only board steps); pickup loop reframed source-agnostic; per-mode `{log}` lines (`ledger` writes none); per-mode Verify; file-header blurb rewritten.
- **`_meta/vault-operating-contract.md` § Sessions, sittings, and hand-offs** — add after "Role boundary at the seam": **two handoff timings** (synchronous typed payload vs **durable doc** in `_agent/handoffs/`); **the relay-when-done reflex** (named here, mechanics owned by `relay` mode — single-home, not restated); **durable handoffs updated in place at a stable path** (the lifecycle rule relay's idempotency depends on).
- **Partner skills (pointer only, where a real durable-handoff relationship exists today):** `vlt-agent-health-coach/SKILL.md` (fire the relay reflex after writing the nutrition-spec doc; revise in place); `vlt-agent-chef/SKILL.md` (the spec arrives as an open pointer in its dispatch slice — ordinary pickup). *Maintainer note:* resist baking into all partners; the contract carries the cross-cutting rule, per-partner is just a pointer where a live handoff exists.
- **`module-help.csv` (module copy + install mirror, kept identical):** retitle dispatch row "The Partner Communication Bus"; rewrite description for three modes; scope column → `{mode: daily | relay | ledger; bare call → menu}`.
**Migration:** **none required.** Skill/contract/partner edits are idempotent text replacements; existing `_agent/dispatch.md` records are forward-compatible (all prior blocks are `daily/…`, watermark logic reads them unchanged; relay/ledger only add/read block shapes). One-time *optional* (data, not skill): any handoff doc already sitting in `_agent/handoffs/` without a pointer can be relayed live next time the producing partner sits.
**Latent bug surfaced — CSV quoting drift (Phase A):** in the vlt-core install the *live* `module-help.csv` had the dispatch scope column **unquoted despite containing a comma**, while the `vlt-setup` mirror had it quoted — a strict CSV parser mis-splits the live row. **Module action: audit every `module-help.csv` row for embedded commas in unquoted fields** (both copies).
**Artifacts:** `vlt-dispatch/SKILL.md`, `_meta/vault-operating-contract.md`, `vlt-agent-health-coach/SKILL.md`, `vlt-agent-chef/SKILL.md`, `module-help.csv` (×2).
**Open questions:** relay liveness depth (ship cheap slug-must-be-live check; defer a `ledger`-mode sweep flagging pointers whose slug retired *after* writing — failure #4); relay across more partner pairs (per-handoff reflex now; a shared fan-out *workflow* later as the roster grows — parallels the daily-fan-out backlog); ledger as canonical board (kept both inline-`daily` print AND `ledger` mode per user; revisit if the inline copy drifts).
**Priority/risk:** Medium, **low risk — already field-validated and applied downstream.** Mostly a *mirror-upstream* job. Touches three themes at once (see cross-cutting): coherence (relay reflex single-home + pointers), durability (`_agent/handoffs/` + forward-compatible records), and one tactical Phase-A bug (CSV quoting).
**Protect:** source-agnostic drain; single-writer (Librarian sole author of `_agent/dispatch.md`); the defer-until-it-bites discipline that retired `unrouted`; daily-mode watermark format (old-install idempotency).

---

## Emergent design strand — the Capability object (ideation 2026-06-15)

**Not a field filing** — surfaced from a design question (how BMad agents add slug-callable capabilities vs. vlt's "every capability is a minted op skill"), grounded by the live `vlt-track` friction in vlt-core. **Full plan:** `skills/reports/vlt-partner-capabilities-ideation.md` (`status: complete`). Captured here because it threads three existing phases rather than standing alone.

**Essence:** Make **Capability** a first-class object with two *weights*. The owner declares only `write_scope`; **weight, home, council-class, and durability all derive** from it. Own-zone write → *light* (a partner-owned file beside `identity.md`, or self-grown live, council-none). Shared-lane write → *heavy* (a registered op skill owned by the lane's partner — i.e. today's op skill, now understood as "the heavy weight"). Recurring ideas across partners become **opt-in families** (Model B: thin shared invariants + per-partner body) — the structural answer to `vlt-track` (one idea, per-partner application, no switch-skill, no duplicate skills).

**Changes specified (build order in the plan):**
- Capability schema + a light-capability template in `vlt-mint/assets`.
- Partner activation (operating-contract Beat-2 Orient + partner SKILLs) reads `{partners}/{name}/capabilities/` and surfaces **contextually** (data, not a fixed menu); "What you do" becomes derived.
- `vlt-mint`: `add a capability` routing by `write_scope`, council-class derivation, self-grow path, `retire a capability`, family ops (`change invariants` = gated).
- `vlt-lint`: coherence guard — declared `write_scope` matches actual writes (lane firewall) + family-invariant conformance.
- `_agent/capabilities/families/` zone; per-partner `capabilities/` folders created lazily.

**How it threads the phases (no new phase needed):**
- **Phase B (coherence):** the family-invariant propagation check *is* the convention→consumer dependency machinery, applied to capability families. The lint lane-firewall is its enforcement.
- **Phase C (mint maturation):** the lightweight tier is a new mint output; routing fits the planned **Ideate→Validate→Build** phases; pairs with #6's vertical-partner work (the `vlt-track` lint-firewall in #6 is the same firewall this strand specifies).
- **Phase D (durability):** the capability agent-zone (`{partners}/*/capabilities/`, `_agent/capabilities/`) is reconciled-not-replaced — rides the existing durability principle; family-invariant change on upgrade fires the same propagation check.

**Open questions:** is the light-capability/self-grow tier its own small build, or absorbed into Phase C's mint work? Does `module-help.csv` (shipped-only today) need a vault-grown-capability discovery counterpart? Does the lint firewall here merge with #6's deferred firewall check (same mechanism)?

**Priority/risk:** Medium. Mostly *unifies and lightens* existing machinery rather than adding new subsystems; lane-safety preserved by construction. Low migration risk (additive). Best sequenced alongside C, leaning on B's coherence work and D's durability work.

---

## Round 2 capture — the 0.3.0 upgrade field notes (2026-06-24)

**Source:** `inbox/2026-06-24-123000-upgrade-0.3.0-field-notes.md`, filed by `vlt-upgrade` during the
first real `vlt-core` upgrade (0.2.0 → 0.3.0, own-the-apply) — the batched acceptance run that
discharged the entire Deferred ledger in anger. The run *worked* (4 mints preserved, zero
destruction); it also did what a real run always does — surfaced defects unit-tests can't. **Three
confirmed defects + one upstream candidate.** All three defects grounded against current module
source 2026-06-24; ideated + briefed → **`build-10-round2-upgrade-hardening.md`** (one build for
#1–3, owner-steered). `vlt-track` (#4) deferred to its own build.

### R2-1. Contract Beat 2 dropped the dispatch-slice drain — the bus stalls
**Defect (coherence).** `vault-operating-contract.md:164` (Beat 2 Orient) reads
`index/log/backlog/thread/capabilities` but has **no dispatch-slice read**, while `:221` (relay-when-done
reflex) explicitly depends on the recipient "drain[ing] it via the ordinary pickup loop on its next
orient." Relayed hand-offs are appended and never picked up — silent bus stall (the exact failure
filing #9 was built to cure).
**Provenance — CORRECTED during grounding (build-7 is innocent):** the field note blamed build-7's
`capabilities/` read for "taking the slot." The module truth: **build-4** (`92b53d6`) added the relay
reflex (`:189`) but its Beat 2 read was only `index/log/backlog/thread` — it **never wired** the
pickup read. **build-7** (`d2f52fc`) added `capabilities/` to Beat 2 **purely additively** (verified
in the diff) — it displaced nothing. So #1 is a **build-4 coherence gap** — a relay *reflex* shipped
without its *pickup* read, which is itself a convention→consumer coherence miss *inside the contract*.
vlt-core read it as "capabilities took the slot" because its installed 0.2.0 had filing #9 applied
locally first.
**Fix:** restore the dispatch-slice drain to Beat 2 **alongside** capabilities (both coexist) + its
mutation-license note ("the one orient read that may mutate shared state — draining checks an item
off; deliberate, never a silent activation side-effect"). Single-home discipline held (Beat 2 names
the drain, points at `vlt-dispatch`'s pickup loop, restates no mechanics).
**vlt-core fold-back:** vlt-core re-grafted exactly this as its one intentional governance divergence;
once the module ships, that divergence folds back to zero.
**Artifacts:** `vault-operating-contract.md` (Beat 2, `:164`). **Risk:** low; one prose edit, zero migration.

### R2-2. Per-skill `.decision-log.md` build cruft ships into the installed surface
**Defect (hygiene).** 10 `.decision-log.md` (build-time authoring metadata) live in the **working
tree** under `skills/`; `.gitignore` carries `**/.decision-log.md` so they're absent from the *repo*
but present on *disk*. `vlt-upgrade`'s own-the-apply does a **filesystem** merge-copy → dragged all 10
into the live vault; one **clobbered the vlt-mint relocation stub** (build-6 §A1) — the precise
failure the stub warns about. gitignore governs the repo, not a filesystem copy.
**Fix (both layers):** (1) delete the 10 working-tree files (stops the bleeding today); (2) add a
**copy-exclude** for `.decision-log.md` at `vlt-upgrade`'s apply seam (structural — survives a future
build authoring a fresh one). Confirms the relocation stub's value.
**Artifacts:** delete `skills/**/.decision-log.md` (×10); `vlt-upgrade/SKILL.md` apply step. **Risk:** low; zero migration.

### R2-3. `merge-help-csv.py` aborts on unquoted-comma rows minted in the field
**Defect (brittleness).** vlt-core's live `module-help.csv` had 2 rows (`vlt-agent-health-coach`,
`vlt-lint`) with **unquoted comma** free-text → mis-split. Build-3's read-guard (`merge-help-csv.py:113–119`)
**detects but `raise`s** → aborts the whole merge *before* build-6 B1's local-mint preserve runs →
registration blocked until hand-fixed. The guard was a *detector*; field use shows it must become a
*survivor*. Write-side root cause: vlt-mint emits free-text fields unquoted.
**Fix (both sides — owner-confirmed):** write-side — vlt-mint / help-row authoring **always quote**
free-text fields (drift-proof vs quote-if-comma); read-side — guard **skips/repairs + reports**
instead of aborting, so one bad field never blocks an upgrade. Sibling of build-3 (which hardened the
read side as a detector); build-10 completes both ends.
**Artifacts:** `vlt-mint/SKILL.md` (+ any other help-row author), `merge-help-csv.py:113–119`. **Risk:** low; backward-compatible, zero migration.

### R2-4. (candidate, not a defect) `vlt-track` — upstream the longitudinal-loop op
The local `vlt-track` op (design protocol → log progress → review/adjust; caller supplies profile +
voice) is **absent from 0.3.0**, preserved as a vlt-core local mint. With 0.3.0's invariant-based
**personalized-extraction firewall** (build-8) shipped, it now fits cleanly as a domain op that opts
into the widening per its mint. **Threads the build-7 capability-object + build-8 firewall strands** —
a real op-skill design, **not** a defect fix. **Decision (Round 2 steering):** capture as a candidate,
**defer to its own build** (its own brief, if the owner elects to upstream). Out of scope for build-10.

**✅ IDEATED + BRIEFED + BUILT 2026-06-25 → `build-11-vlt-track-upstream.md` (unit-verified at rest).** Owner
elected to upstream. **BUILT:** new `skills/vlt-track/SKILL.md` (lift + handshake ack + loop-profile read
rehomed to `capabilities/track.md`); `capability-template.md` heavy-pointer gained a *Loop profile* block;
handshake registered (`extraction@2` + `wiki-supersession@1` ↔ vlt-track, bipartite-consistent); help.csv
row TK (always-quoted) + marketplace manifest; vlt-mint archetype docs reframed to wear-the-hand. CSV parses
13-col, manifest complete, zero migration. **Crux resolved:** the field-evolved vlt-track is a **shared, profile-driven
_heavy_ op** ("one verb, many subjects" — caller brings voice + non-negotiable + loop profile; writes a
PARA protocol via personalized-extraction). Because it writes a **shared lane (PARA)** it is heavy by
the capability model's own lane-safety rule → this **refutes build-7's "light `track` family"
prediction** while **validating build-7's object model** (op skill = heavy capability with a `skill:`
procedure). **Owner rulings:** (#1) ship the shared heavy op as-is, supersede the family acceptance;
(profile home) move the loop profile from inline-in-SKILL.md (vlt-core) into the wearer's
`capabilities/track.md` heavy pointer (build-7-integrated — the one substantive delta from a verbatim
lift); (wearer) **ship the hand only**, no example vertical partner. **No Model-B family** (one shared
body, not N — family machinery stays valid but unexercised, awaiting a genuinely-light verb). Handshake:
mirror vlt-extract — `depends_on ["extraction@2", "wiki-supersession@1"]` + add vlt-track to those
consumers. Coherence edit: vlt-mint vertical-partner archetype docs point at vlt-track as the canonical
shared loop hand (wear-the-hand, don't mint a duplicate). Zero migration.

---

## Cross-cutting threads (things that appear in more than one filing)

- **Args delivery is string-encoded for ALL workflow invocation forms.** ✅ **RESOLVED in Phase 0.** Filing #3 (lint-full) and #7 (council) were the same bug — the runtime delivers `args` as a JSON string; code that did `args || {}` then read a property got `undefined`. Fixed both shipped workflows with a parse-on-intake guard; verified. The "scriptPath-by-default" idea was unnecessary (scriptPath delivers the same string). **Standing rule for all future module workflows: parse args defensively at the top.**
- **Single-source-of-truth for `vault_structure`.** Filing #1 (setup transcribes a table) and #2 (partner SKILLs re-list a subset) are the same SSoT gap. One canonical map, everything else points at it. **✅ Half resolved (commit `c918274`):** `module.yaml` is now the canonical map and `vlt-setup` reads it (filing #1 done). The remaining half — filing #2's runtime skills (`vlt-lint` On-Activation, partner SKILLs) still *re-listing* a path subset inline instead of pointing at the map — stays open for **Phase E**.
- **Convention→consumer coherence.** Filing #4 §5 (index-redesign drift) and #3 §3 (source-count drift) are the *same latent failure* — a convention changed and its consuming skills didn't. **Filing #9 is the same shape handled *correctly*:** the relay-when-done reflex is given a **single home** (the `relay` mode mechanics + the operating contract's cross-cutting rule) with partner skills carrying only a *pointer* — exactly the single-source-of-truth discipline the dependency map is meant to enforce. The proposed **convention→consumer dependency map** would have caught the #4/#3 drift; #9 shows the target state. This is the coherence half of the architectural core.
- **Agent-zone as the durable home.** Filing #5 (mint planning docs in `_agent/mint/`), #6 (operational state in agent zone), #8 (decision log + durability principle), and **#9 (`_agent/handoffs/` for durable partner-to-partner handoffs; `_agent/dispatch.md` records forward-compatible across upgrades)** all converge on `_agent/` as the upgrade-safe location. `_agent/mint/` is becoming the single home for mint institutional memory; `_agent/handoffs/` + `_agent/dispatch.md` are the partner-communication-durable equivalents.
- **The two outstanding Build #1 owner gates** (cold-start/warm activation outside-read; rebirth two-tier check) live in the same identity-model territory as filing #2's naming question — fold together.
- **The Capability object strand is a coherence + durability + mint story at once** (see the emergent-design-strand section above). Its family-invariant propagation = the convention→consumer machinery; its agent-zone home = the durable-home thread; its lightweight tier = the mint engine maturing. It's the same architectural core ("make + preserve across change") viewed through *what a partner can do* rather than *what a vault knows*.

---

## Proposed phasing (a PROPOSAL — to refine during per-phase ideation)

Sequenced by pain, dependency, and architectural coherence. Each phase becomes its own build brief
(`build-3-*.md`, etc.) when we ideate it.

| Phase | Theme | Folds in | Why this grouping / order |
|---|---|---|---|
| **0 — Systemic args fix** | Workflow robustness | #7 (council) + #3 §1 (lint-full blocker) | ✅ **COMPLETE 2026-06-13.** Parse-on-intake guard in both shipped workflows; empirically diagnosed + verified. Unblocked every gated mint. |
| **A — Stop the bleeding** → **build-3 ✅ BUILT 2026-06-23** | Tactical robustness | #3 (lint-full cost + near-dup noise + cluster cap + cross-layer wikilinks), #9 (CSV-quoting audit) | **Ideated + BUILT 2026-06-23 (`build-3-lint-full-hardening.md`, unit-verified).** Scope corrected during ideation: filing #1 (setup SSoT/dep-check/wart) found **already shipped** (`c918274`) — dropped; filing #3 §3 (source-count drift) **deferred to Phase B** (module convention still defines counts). Shipped: ~10× model-tiering (haiku/sonnet), near-dup AND-rule with hub-exclusion, page-count-scaled cluster cap, cross-layer wikilink resolution, and a `merge-help-csv.py` quoting read-guard (#9). Remaining: a live `--full` sweep to confirm the cost drop empirically. |
| **B — Coherence** → **build-4 ✅ BUILT 2026-06-23** | Propagation discipline + its worked examples | The convention→consumer **version-handshake** (from #4 §5 + #3 §3), the category/topic schema #4 (addition), source-count removal #3 §3 (removal), **#9 dispatch bus folded in** (clean case) | **Ideated 2026-06-23 → `build-4-coherence-machinery.md` (ready to build).** Decisions: machinery is a **version-handshake** (convention `version:`+`consumers:`; consumer `depends_on: ["name@version"]` — flat per rule 3; two-layer = vlt-lint net + vlt-mint `convention edit` gate), NOT content-diff/separate-map/bare-checklist. Source-count = **upstream the counted-row→structural-map redesign** so it's a real REMOVAL example. **Operating contract held OUT → Phase D** (open consumer set = minted-partner durability; #9 uses the complementary single-home+pointer pattern). Migration = recipe + lint-assisted (vlt-migrate noted as follow-up). Three worked examples in one phase (addition / removal / clean), mirroring Build #2's "machine + its first run." |
| **C — Mint maturation** → **build-5 ✅ BUILT 2026-06-24 (unit-verified)** | The engine learning from 3 real mints | #5 (phases + resumable planning doc), #6 (vertical-partner archetype + personalized extraction) — **lint firewall DEFERRED, capability tier SEPARATE** (owner rulings) | Built: vlt-mint regrouped under Ideate→Validate→Build phases + exit gates (new-partner becoming convo moved to Phase 1; build-4 convention-edit handshake gate cross-ref'd as the Phase-3 instance); resumable `_agent/mint/{date}-{slug}.md` planning doc + On-Activation resume scan; personalized-extraction widening lifted from vlt-core `4154b12` (extraction `version:` 1→2, vlt-extract ack reconciled, contract {log} non-exhaustive, Creative carve-out, frontmatter.md untouched); vertical-partner archetype docs. **PRECURSOR (owner-ruled): governance SSoT collapse** — see note below. `status: BUILT — acceptance pending a real vault`. See `build-5-mint-maturation.md`. |
| **D — Lifecycle durability** → **build-6 ✅ BUILT 2026-06-24 (unit-verified)** | The architectural core | #8 (durability principle + `vlt-upgrade` + merge-not-replace registration + agent-zone relocation + governance divergence report) | **Built 2026-06-24 → `build-6-lifecycle-durability.md`.** B1 merge-not-replace (merge-help-csv.py `--live-skills-dir`, unit-tested), append-only convention overlays (contract *Durability across upgrades* section + 5 convention pointers + vlt-lint base-divergence/overlay checks + vlt-mint convention-edit branch + vlt-setup baseline stash), decision-log relocation to `_agent/mint/`, standing `_agent/upgrade-ledger.md`, and the new `skills/vlt-upgrade/` skill (prefer-own/degrade-to-bracket; B2 body-restore; calls vlt-setup) registered in module-help.csv. Handshake re-verified bipartite-consistent (no version drift). **Ideated 2026-06-24 → `build-6-lifecycle-durability.md`.** Key reframes: (a) the upgrade is *acquire* + *apply* welded — `vlt-upgrade` **prefers to own the apply** (merge-copy, no destruction) and **degrades to bracket mode** only when bits arrive welded to a destructive apply (resolves the "decide during ideation" posture without the B2 unknown); (b) convention durability = **append-only overlays** (owner idea, supersedes 3-way merge — base stays pristine/overwrite-safe, local edits in `_agent/conventions/{name}.overlay.md`, consumers merge on read, extends Phase B's handshake resolver) + detect-report safety net; (c) ledger = **standing append-only evolution record** `_agent/upgrade-ledger.md`. Scope = filing #8 core ONLY; capability strand → build-7, lint firewall → build-8. The deepest change; benefits from Phases A–C having stabilized the pieces it must preserve. **B2 spike done 2026-06-23 → now specifiable** (see B2 spike record below): A-vs-B is owned by the external installer and only an upgrade-test would settle it (the very upgrade we're avoiding), so D is specified under the **safe-pessimistic assumption** (installer copies destructively first, `vlt-upgrade` reconciles after — already the §C design posture). The **confirmed, in-repo ship-blocker is B1** (registration anti-zombie), not B2. |
| **E — Identity polish** → **build-9 ✅ BUILT 2026-06-24** | Partner-layer follow-ons | #2 (naming home in two-tier model + frontmatter-read-before-write) + the two outstanding Build #1 owner gates | **Scoped + BUILT 2026-06-24 (`build-9-identity-polish.md`).** Phase-A-shaped result: **build content already shipped by Build #1.1** (the close-out of the field test that *spawned* filing #2) — naming's home (ungated `name` field), read-frontmatter-before-write, and the point-at-the-map behavioral instruction are all present in the contract + frontmatter.md + all 3 partner SKILLs + the partner template. **The one genuine residual** (filing #2 ③): the partner SKILLs/template inline *full-set* logical-name enumeration had drifted 2 names behind (missing `overlays`/`upgrade_ledger`) while telling the reader to "read the map" — owner-chosen SSoT-clean fix = **delete the enumeration** (4 files), killing the drift vector. Op skills left as-is (subset-with-defaults pattern doesn't have the claims-completeness-and-drifts failure mode; all 7 verified current). The **two owner gates** (finding #4 warm-activation aliveness; finding #6 rebirth two-tier enacted) are **live acceptance, not code** → reclassified into the Deferred ledger to fire in the batched `vlt-upgrade` run. **Phase E is the last build phase — the full roadmap has now shipped.** |
| **(strand) Capability object** → **build-7 ✅ BUILT 2026-06-24** | Lightweight first-class capabilities | Emergent design strand (plan: `vlt-partner-capabilities-ideation.md`) — `vlt-track` problem | **BUILT as its own small build (`build-7-capability-object.md`).** Capability object (write_scope→weight derivation), light/heavy templates, contract `## Capabilities` + Beat-2 read, vlt-mint add/migrate/retire + family ops (change-invariants gated→propagation), vlt-lint lane-safety + family-invariant guard, vlt-setup + vlt-upgrade durability. Threaded B (propagation = handshake machinery), C (light tier = mint output, paired with #6), D (agent-zone reconcile). |
| **(follow-on) Extraction firewall** → **build-8 ✅ BUILT 2026-06-24** | filing #6 deferred enforcement | The method-traces-to-wiki firewall deferred from build-5 | **BUILT (`build-8-extraction-method-firewall.md`).** vlt-lint personalized-extraction firewall; registered as an `extraction@2` consumer (handshake bipartite-consistent). Sibling of build-7's lane-firewall, not merged. |
| **Round 2 — upgrade hardening** → **build-10 ✅ BUILT 2026-06-24** | Post-acceptance robustness | 0.3.0 upgrade field notes: #1 contract dispatch-slice drop, #2 `.decision-log.md` install cruft, #3 CSV unquoted-comma brittleness | **Ideated + BUILT 2026-06-24 (`build-10-round2-upgrade-hardening.md`, unit-verified).** Owner steering: one build for #1–3; CSV fix **both sides**; **`vlt-track` deferred** (candidate #4). **#2:** deleted 10 working-tree `.decision-log.md` + `vlt-upgrade` copy-exclude. **#3:** `merge-help-csv.py` skips+reports mis-split rows (no longer aborts; fresh-install path unregressed) + vlt-mint Step 4 always-quote rule. **#1:** grounding found the **partner SKILLs + template also enumerate Beat 2 and all omitted the dispatch slice** (build-4 gap in the consumers, not a build-7 regression — build-7's capabilities read was verified additive) → **owner-approved full fix (5 files):** contract Beat 2 + standalone mutation-license note + dispatch-drain added to all 3 partners + the template, each in voice (name+point-at-contract). Contract not version-handshaked → no bump. vlt-core's one governance divergence folds to zero on next upgrade. Phase-A-shaped, low-risk, zero migration. |
| **(strand) Dispatch bus mirror** | Partner communication bus | #9 (vlt-dispatch daily/relay/ledger; contract handoff section; partner pointers; CSV) | **✅ FOLDED INTO build-4 (Phase B), decided 2026-06-23.** It is coherence-done-right (relay-reflex single-home + pointers) — the *clean case* worked example alongside category/topic (addition) and source-count (removal). Its contract edit uses the single-home+pointer pattern, NOT the version-handshake (consistent with holding the operating contract out to Phase D). Low-risk mirror-upstream, zero migration. See `build-4-coherence-machinery.md` Part 4. |

**Open sequencing questions for ideation:**
- ~~Should the systemic args fix be its own tiny Phase-0?~~ ✅ Resolved — it was, and it's done.
- Does **Phase E** deserve to stand alone, or fold into Phase C (both touch the mint template + partner stamp)?
- Phase D's **B2 installer question** is an external unknown — resolve before D is specifiable. Worth a spike now.
- Which **local mints upstream** (Dog Trainer → ship as a generic vertical?) — affects how much weight B1/B2 must carry.
- **Dispatch-bus mirror (#9): own small build first, or fold into B?** It's already applied downstream and *fully specified* (zero design risk, zero migration), so it's the cheapest, most-ready unit on the board — a case for mirroring it upstream *immediately* to stop the cache drifting from the install. Counter-case: it's small enough to ride into Phase B alongside the coherence machinery it exemplifies.

---

## Deferred acceptance ledger (verified post-ship, via vlt-core inbox filings)

**Decision (2026-06-23):** Do **not** upgrade `vlt-core` to pick up build-3/build-4 (or any later
build) **until Phase D — lifecycle durability — ships.** Upgrading now would run the live vault
through the generic, module-agnostic BMad installer that filing #8 documents as able to silently
destroy vault-specific evolution (the three minted partners, local convention edits, mint history).
Verifying a cost optimization is not worth that risk. **Therefore all live acceptance is deferred**
and **batched to the first safe upgrade** (the one Phase D's `vlt-upgrade` makes durable). At that
point `vlt-core` upgrades once, exercises the accumulated changes in anger, and **files any defects
back into the inbox** as ordinary field filings — the same loop that produced this roadmap.

**Consequence — the whole board is now gated on Phase D.** build-3, build-4, and any Phase C output
are all unverifiable in the live vault until the durable upgrade path exists. This raises Phase D's
priority: it is the unlock for *all* outstanding acceptance, not just its own feature. (Phase D
remains blocked on the **B2 installer-copy spike** — resolve that first.)

**Outstanding acceptance checks** (to run as `vlt-core` upgrades post-Phase-D; defects → inbox):

- **Build #3 (Phase A — lint-full hardening):**
  - [ ] Live `--full` sweep confirms the **~10× cost drop** (haiku scanners / sonnet index+cluster vs. all-Opus baseline ~2.1M tokens).
  - [ ] **Near-dup AND-rule + hub-exclusion** suppresses the 70 false co-citation pairs without dropping real near-dups.
  - [ ] **Page-count-scaled cluster cap** clears the 13 natural clusters (no longer truncates at 12).
  - [ ] **Cross-layer wikilink resolution** stops false-flagging valid `[[…]]` into `_agent/research/` (the 14-of-17 `missing_targets`).
  - [ ] **`merge-help-csv.py` quoting read-guard** correctly parses comma-bearing scope columns.
- **Build #4 (Phase B — coherence machinery):**
  - [ ] Live `--full` sweep: the **Convention-coherence check fires** and reports any `name@version` handshake mismatch.
  - [ ] A real **`convention edit` mint** exercises the **version-handshake exit gate** (gate holds; consumers re-acked or flagged).
  - [ ] Handshake verified **bipartite-consistent at runtime** (not just at rest) across the 5 seeded conventions + their consumers.
  - [ ] **#9 dispatch bus** three modes (`daily` / `relay` / `ledger`) work live; relay idempotency keyed on `(doc-path, recipient-slug)` behaves; bare call → menu.
- **Build #5 (Phase C — mint maturation):**
  - [ ] A real **gated mint** (new partner / persona self-edit / convention edit) visibly traverses **Phase 1 → 2 → 3** and **stops at each exit gate** for approval (brief / verdict+decisions / verified+commit).
  - [ ] The **resumable planning doc** is created at `_agent/mint/{date}-{slug}.md`, updated at each boundary; **closing mid-flow + re-activating** offers resume and restores phase state; a **non-gated** mint (`operation skill`) creates **no** doc.
  - [ ] A **personalized extraction** (e.g. a `vlt-track`-style domain deliverable) writes `personalization_sources:` separate from `sources:`; the method-grounding invariant holds; the contract's new `track`-style `{log}` type is accepted.
  - [ ] The **vertical-partner archetype** guidance is usable on a real domain mint (names domain self-awarely / own op skill / bounded widening).
  - [ ] **Governance single-source** holds in a fresh `vlt-setup` install (the collapsed bundle installs correctly; no top-level `governance/` staging tree to drift).
- **Build #6 (Phase D — lifecycle durability):**
  - [ ] A local convention **overlay** survives an upgrade that refreshes the base convention (both present after; no conflict); a direct base hand-edit is **reported** (not clobbered).
  - [ ] `merge-help-csv.py --live-skills-dir` **preserves** a minted partner's help row live; still drops a true zombie.
  - [ ] Decision-log relocation runs **idempotently** to `_agent/mint/decision-log.md`; `_agent/upgrade-ledger.md` appends a dated block.
  - [ ] `vlt-upgrade` happy path performs **no destruction**; bracket path reconciles; calls `vlt-setup`.
- **Build #7 (Capability object):**
  - [ ] ~~Re-create `vlt-track` as a **light, vault-grown** capability with a `track` **family** across Researcher/Librarian/Creative~~ **SUPERSEDED by build-11 (2026-06-25).** vlt-track is a **heavy** capability (it writes PARA, a shared lane) → it ships as a shared op worn via a `capabilities/track.md` heavy pointer + loop profile, **not** a light family. Real check now lives under Build #11 below. build-7's family (Model-B) machinery is shipped but **lacks a canonical example** until a genuinely-light recurring verb appears.
  - [ ] A partner **self-grows** a light capability mid-conversation (one decision-log line; no full mint); it survives a simulated upgrade.
  - [ ] `vlt-lint` flags a lane-violating light capability + a family-invariant breach; a changed shipped family invariant fires `family_invariant_drift` on upgrade.
- **Build #8 (Extraction firewall):**
  - [ ] A personalized extraction with a method claim not grounded in its wiki `sources:` is flagged `method_not_in_sources`; the `extraction@2` ack reads current in the coherence check.
- **Build #9 (Phase E — identity polish) + the two reclassified Build #1 owner gates:**
  - [ ] A **warm activation** (a partner with accrued `## Self`/thread) runs the light two-beat orient and carries its drift — and the owner's **outside read** confirms felt aliveness (Build #1 finding #4; cold-start already PASSED live 2026-06-06).
  - [ ] The **rebirth two-tier line is enacted** (Build #1 finding #6): a "how I sound" change routes to `## Self` (ungated); a "what I refuse to do / core role / capabilities" change routes to a council-gated SKILL.md rebirth via `vlt-mint` — the line is *enacted*, not just described.
  - [ ] After the partner-SKILL enumeration deletion, a fresh partner activation still resolves every path through the `vault_structure` map with no missing-name surprise (the deletion is behaviorally inert).

- **Build #10 (Round 2 — upgrade hardening):**
  - [ ] **#1** — A relayed hand-off is **picked up on the recipient's next orient** without prompting; Beat 2 visibly reads + drains the `_agent/dispatch.md` slice (the one sanctioned Beat-2 mutation); build-7's `capabilities/` read and the restored dispatch read **coexist**.
  - [ ] **#2** — A fresh `vlt-upgrade` own-the-apply (or install) drags **zero** `.decision-log.md` into the vault; the vlt-mint relocation stub survives.
  - [ ] **#3** — vlt-mint writes a comma-bearing help row **quoted**; `merge-help-csv.py` fed a pre-existing **unquoted-comma** row **does not abort** (reports + skips/repairs), and build-6 B1 local-mint preserve still runs on the rest.

- **Build #11 (vlt-track upstream):**
  - [ ] A vertical partner wears vlt-track via its `capabilities/track.md` **heavy pointer + loop profile**; the skill reads `{root}`/`{target}`/streams/gate from **that file** (not the partner SKILL.md) and runs design / log / review.
  - [ ] **Design** writes a PARA protocol: `sources:` = wiki pages only, `personalization_sources:` = agent-zone streams, every method claim traces to a wiki page, the partner's non-negotiable re-asserted at the write.
  - [ ] **Log** writes agent-zone only (no method leak); **Review** interprets the trend and re-extracts **in place** with supersession callouts.
  - [ ] **vlt-lint** fires `method_not_in_sources` against a real vlt-track protocol (connects build-8's deferred check to a real op).
  - [ ] Handshake bipartite-consistent: vlt-track acks `extraction@2`/`wiki-supersession@1`; both conventions list vlt-track.
  - [ ] vlt-track is registered (help.csv parses; marketplace installs) and **survives upgrade as shipped** (no longer a vlt-core local mint that B1 must preserve).

*(This ledger is the durable home for "what to confirm once it's safe to upgrade." vlt-core's
filings back are the verification record.)*

---

## Status & next step

- **This doc** = the durable capture + phasing cache. `status: ideation`.
- **Emergent strand filed 2026-06-15:** the **Capability object** design (`vlt-partner-capabilities-ideation.md`, complete) — threads Phases B/C/D, captured above; not a standalone phase.
- **Filing #9 folded in 2026-06-23:** the **vlt-dispatch partner communication bus** (daily/relay/ledger) — already designed + applied in the vlt-core install; captured above as filing #9 + a "(strand) Dispatch bus mirror" phasing row. It is a low-risk *mirror-upstream* job (zero migration), threading B (coherence) / D (durability) / A (CSV-quoting bug). Open: mirror it upstream first vs. fold into B.
- **Phase 0 (systemic args fix): ✅ COMPLETE 2026-06-13.** Both shipped workflows patched + verified; existing installs pick it up on the next `vlt-setup` refresh / upgrade. (No data migration; pure additive.)
- **Phase A ideated + BUILT → `build-3-lint-full-hardening.md` (2026-06-23).** During ideation, two scope corrections landed (see filing #1 ✅ and filing #3 §3 ⚠️ above): filing #1 was already shipped (`c918274`), and §3 source-count drift defers to Phase B. Build-3 is the clean residue — lint-full cost-tiering + near-dup noise + cluster cap + cross-layer wikilinks + CSV-quoting guard — **all five components implemented and unit-verified.** `status: BUILT — acceptance (live --full sweep) pending a real wiki`.
- **Phase B ideated + BUILT → `build-4-coherence-machinery.md` (2026-06-23).** The convention→consumer **version-handshake** + its three worked examples (category/topic addition, source-count removal, #9 dispatch clean case). **Built + unit-verified 2026-06-23:** all 5 conventions seeded with `version:`/`consumers:`; vlt-ingest/vlt-lint/vlt-extract carry flat `depends_on: ["name@version"]` acks; vlt-lint gained the Convention-coherence check; vlt-mint's `convention edit` kind completed with the handshake exit gate. Category/topic + source-count removal lifted verbatim from vlt-core (`a4af503` did both in one commit). The **#9 dispatch bus** turned out to be **absent from the module** (not a mirror — a first creation); created fresh from vlt-core's three-mode version, contract handoff delta ported, CSV row added; partner pointers dropped (health-coach/chef are vault-minted, not in module source). Handshake verified bipartite-consistent at rest. Operating-contract versioning held out to Phase D as planned. `status: BUILT — acceptance (live --full sweep + a real convention-edit mint) pending a real vault`.
- **Live acceptance DEFERRED (decided 2026-06-23).** Do not upgrade `vlt-core` until Phase D's durable upgrade path lands; all outstanding acceptance is now tracked in the **Deferred acceptance ledger** above and batched to the first safe upgrade, with `vlt-core` filing any defects back into the inbox. This gates build-3/build-4/Phase-C verification on Phase D and raises Phase D's priority (it is the unlock for *all* acceptance).
- **B2 spike DONE (2026-06-24) → Phase D unblocked to specify** (see B2 spike record): A-vs-B is external/installer-owned and only an upgrade-test settles it; D is specified under the safe-pessimistic assumption; the confirmed in-repo ship-blocker is **B1 (registration anti-zombie)**, not B2.
- **Phase C ideated + brief written → `build-5-mint-maturation.md` (2026-06-24, ready to build).** Owner rulings: Phase C built first (D follows); scope = filings #5 + #6 only; lint firewall DEFERRED; capability tier SEPARATE. The brief covers: (1) explicit Ideate→Validate→Build phases + exit gates in `vlt-mint` (harmonizing with build-4's convention-edit handshake gate), (2) the resumable `_agent/mint/{date}-{slug}.md` planning doc + activation resume branch, (3) personalized extraction widening (`personalization_sources:`, n=1 to `vlt-track`, lifted from vlt-core `4154b12`, honoring the build-4 handshake on `extraction.md`'s version bump), (4) the vertical-partner archetype docs.
- **Phase C BUILT → `build-5-mint-maturation.md` (2026-06-24, unit-verified).** vlt-mint Ideate→Validate→Build phases + exit gates + resumable `_agent/mint/` planning doc + resume scan (#5); personalized-extraction widening lifted from vlt-core `4154b12` honoring the build-4 handshake (extraction `version:` 1→2, vlt-extract ack reconciled) + vertical-partner archetype docs (#6). Full convention→consumer handshake re-verified bipartite-consistent. Acceptance checks appended to the Deferred ledger.
- **⚠️ Governance SSoT collapse (during build-5, owner-ruled 2026-06-24).** Discovered build-3 AND build-4 edited **only** `skills/vlt-setup/assets/governance/` and never the top-level `governance/` "staging source" (README:71) — the two trees had silently diverged since Build #1.1 (all 5 conventions + the operating contract). Ironically the Phase-B *coherence* machinery was applied incoherently. Resolution: **collapse to a single source** — retired the stale top-level `governance/` tree (git rm, 11 files, verified strictly-older/no content lost), repointed README:71 + arch-spec:114 at the assets bundle. Net effect: build-3/build-4's "BUILT" state is now actually single-sourced (the divergence they created is closed), and the dual-copy drift hazard is gone. **Standing rule:** the governance bundle lives only at `skills/vlt-setup/assets/governance/_meta/` now — edit there.
- **Phase D ideated + brief written → `build-6-lifecycle-durability.md` (2026-06-24, PLANNED — ready to build).** See the Phase D ideation record for the owner-steered decisions. Heart = **append-only convention overlays** (owner's structural answer to the one thing they'd grieve — local convention edits — superseding 3-way merge); spine = **`vlt-upgrade` prefer-own/degrade-to-bracket**; must-ship = **B1 merge-not-replace registration**; plus B2 body-restore, §A1 decision-log relocation, the standing `_agent/upgrade-ledger.md`, and the durability principle → operating contract. Scope held to filing #8 core; capability strand → build-7, lint firewall → build-8.
- **Phase D BUILT → `build-6-lifecycle-durability.md` (2026-06-24, unit-verified).** Six parts shipped: B1 merge-not-replace registration (`merge-help-csv.py --live-skills-dir`, unit-tested: shipped-refresh / mint-preserve / zombie-drop); append-only convention overlays (contract *Durability across upgrades* = durability principle + overlay mechanism + base-vs-baseline safety net; 5 convention pointers; vlt-lint `convention_base_divergence` + `overlay_issues` checks; vlt-mint convention-edit branch overlay-vs-base; vlt-setup `.baseline/` stash + `{overlays}` ensure); §A1 decision-log relocation to `_agent/mint/decision-log.md` (+ idempotent migration spec); standing append-only `_agent/upgrade-ledger.md`; the new `vlt-upgrade` skill (pre-flight snapshot → own-the-apply/degrade-to-bracket → reconcile [B1/B2/overlays/migrations, calls vlt-setup] → post-flight report + ledger), registered in module-help.csv. Handshake re-verified bipartite-consistent (no version drift); new logical names `overlays`/`upgrade_ledger` in both SSoTs.
- **DECISION 2026-06-24 (owner): defer ALL live acceptance until the full roadmap ships; proceed with the follow-on builds now.** Live acceptance (the whole Deferred acceptance ledger — build-3/4/5/6 + the strands) stays batched to a single first-safe `vlt-core` upgrade run **after** the remaining builds land. Remaining build work, in order: **build-7** (Capability-object strand), **build-8** (vlt-lint method-traces firewall), **Phase E** (identity polish). The durable upgrade path (build-6 `vlt-upgrade`) already exists, so that batched acceptance is unblocked whenever the owner chooses to run it.
- **build-7 — Capability-object strand: ✅ BUILT 2026-06-24 → `build-7-capability-object.md` (unit-verified).** The plan's 6-step roadmap implemented 1:1 (step 6 folded in since `vlt-upgrade` exists): Capability object + light/heavy templates; operating-contract `## Capabilities` single-home + Beat-2 reads `capabilities/`; new `capabilities` logical name across all SSoTs; vlt-mint `add/migrate/retire a capability` (write_scope→weight derivation, self-grow shortcut) + family ops (`change invariants` gated → propagation); KIND_PANEL updated; vlt-lint lane-safety + family-invariant guard; vlt-setup scaffolds the families zone; vlt-upgrade reconciles-not-replaces the capability zone + fires the family-invariant propagation check.
- **build-8 — extraction method-traces firewall: ✅ BUILT 2026-06-24 → `build-8-extraction-method-firewall.md` (unit-verified).** vlt-lint Personalized-extraction firewall (`method_not_in_sources` / `method_in_personalization`); the check made vlt-lint a consumer of `extraction.md` → handshake registered (`extraction@2` consumers `[vlt-extract, vlt-lint]`, vlt-lint acks `extraction@2`). Sibling of build-7's capability lane-firewall, not merged.
- **Phase E ideated + scoped + BUILT → `build-9-identity-polish.md` (2026-06-24).** Phase-A-shaped outcome: the build content was **already shipped by Build #1.1** (naming's ungated `name` home, read-frontmatter-before-write, point-at-the-map behavior — all present in the contract, `frontmatter.md`, all 3 partner SKILLs, and the partner template). The lone genuine residual was filing #2 ③'s drift: the partner SKILLs/template inline *full-set* logical-name enumeration had fallen 2 names behind (`overlays`/`upgrade_ledger`) while telling the reader to "read the map." Owner-chosen SSoT-clean fix → **deleted the enumeration in 4 files** (3 partner SKILLs + partner template); op skills left untouched (their subset-with-defaults listings don't claim completeness, so they don't drift on additions — all 7 verified current; `vlt-lint` was briefly trimmed then reverted to keep op-skill consistency). The **two Build #1 owner gates** (finding #4 warm-activation aliveness; finding #6 rebirth two-tier enacted) are **live acceptance, not code** → reclassified into the Deferred acceptance ledger above. `status: BUILT — acceptance batched into the deferred ledger`.
- **Inbox archived (2026-06-24).** All field filings are now captured, so the active `inbox/` was drained to `inbox/archive/` (10 files, `git mv`). Nine are this roadmap's `derives_from:`; the tenth — `2026-06-14-…-dispatch-sources-to-librarian-and-retire-unrouted.md` — was **not** a separate `derives_from` entry because it was **subsumed into Build #4's fresh `vlt-dispatch` creation**: its two changes (captured-source→Librarian routing; retire `unrouted` → flag-and-skip) were verified present in the shipped `skills/vlt-dispatch/SKILL.md` before archiving. Lifecycle documented in `inbox/README.md`. **Module version bumped 0.2.0 → 0.3.0** (`module.yaml` + `.claude-plugin/marketplace.json`); the bump also fixed a registration gap — `vlt-dispatch` (build-4) and `vlt-upgrade` (build-6) were missing from marketplace.json's `skills[]` install manifest and are now registered.
- **▶ THE FULL ROADMAP HAS NOW SHIPPED (build-3 through build-9 + the strands).** No build work remains. **Next + only step: fire the batched live-acceptance `vlt-upgrade` run on `vlt-core`** (the first safe upgrade, made durable by Build #6) to discharge the entire **Deferred acceptance ledger** (build-3 through build-9 exercised in anger; `vlt-core` files any defects back into the inbox as ordinary field filings — the same loop that produced this roadmap). This is an owner-initiated live operation on the `vlt-core` install (`{field-vault}`), not module-repo build work.
- **✅ ACCEPTANCE RUN DONE 2026-06-24 → the deferred ledger is discharged in anger.** The first real `vlt-upgrade` ran on vlt-core (0.2.0 → 0.3.0, **own-the-apply**, source = the module repo on `main`). Result (see vlt-core `_agent/upgrade-ledger.md`): **all 4 local mints preserved** (chef / dog-trainer / health-coach + the `vlt-track` op — B1 `--live-skills-dir` confirmed), **zero destruction** (own path, B2 no-op), **5 baselines seeded**, decision-log + CSV migrations ran, governance reconciled with **one intentional divergence** (a dispatch-slice re-graft — see Round 2 #1). Build-3…9 are now exercised-in-anger and passing. Pre-upgrade restore point: vlt-core git tag `pre-vlt-upgrade-2026-06-24` + tar `develop/projects/vlt-core-pre-upgrade-backup-20260624.tar.gz`.
- **✅ ROUND 2 CAPTURED + IDEATED + BRIEFED 2026-06-24 → `build-10-round2-upgrade-hardening.md` (PLANNED, ready to build).** The 0.3.0 upgrade field notes (`inbox/2026-06-24-123000-…`) captured as a proper "Round 2 capture" section above; all 3 defects grounded against current source. **Owner steering:** one build for #1–3; CSV fix **both sides**; **`vlt-track` deferred to its own build** (candidate #4). **Provenance correction during grounding:** #1 is a **build-4 coherence gap** (relay reflex shipped without its Beat 2 pickup read), **not** a build-7 regression — build-7's `capabilities/` read was verified purely additive (diff `92b53d6`→`d2f52fc`). Build-10 acceptance checks appended to the Deferred ledger.
- **✅ ROUND 2 BUILT 2026-06-24 → `build-10-round2-upgrade-hardening.md` (unit-verified).** All 3 defects fixed: **#2** 10 working-tree `.decision-log.md` deleted + `vlt-upgrade` copy-exclude; **#3** `merge-help-csv.py` skips+reports mis-split rows (no abort; fresh-install path unregressed) + vlt-mint Step 4 always-quote rule; **#1** contract Beat 2 + mutation-license note + dispatch-drain added to all 3 partner SKILLs + the partner-template (owner-approved 5-file full fix, since grounding found the consumers drifted too — a build-4 gap, not a build-7 regression). Contract not version-handshaked → no bump. Build-10's live acceptance batches into the next vlt-core upgrade alongside the rest of the Deferred ledger.
- **✅ vlt-track UPSTREAM IDEATED + BRIEFED + BUILT 2026-06-25 → `build-11-vlt-track-upstream.md` (unit-verified at rest).** Round 2 candidate #4 closed out (see the R2-4 section above for the full crux + owner rulings). Shipped the field-evolved **shared heavy op** as-is (supersedes build-7's light-family acceptance — validated build-7's object model, refuted its weight prediction); homed the loop profile in the wearer's `capabilities/track.md` heavy pointer (build-7-integrated); shipped the hand only (no example partner); handshake mirrors vlt-extract (`extraction@2` + `wiki-supersession@1`, bipartite-consistent); vlt-mint archetype docs now point at vlt-track as the canonical loop hand. Verified: handshake bipartite-consistent across all 5 conventions, help.csv parses 13-col, manifest complete. Zero migration. **This was the last open roadmap item — the entire inbox-evolution arc (build-3 → build-11 + strands) has now shipped.** Only remaining work: the batched live-acceptance vlt-core upgrade run (which will now also exercise vlt-track as shipped, no longer a local mint B1 must preserve).
- **(original Round 2 brief, retained for reference)** — `inbox/2026-06-24-123000-upgrade-0.3.0-field-notes.md` (3 defects + 1 upstream candidate):
  1. **Dispatch-slice dropped from contract Beat 2 (real bug in shipped 0.3.0).** Build-7's `capabilities/` orient read displaced the partner's open dispatch-slice read in `vault-operating-contract.md` Beat 2, but the relay-when-done reflex still depends on partners draining their slice on orient → relayed hand-offs are never picked up; the bus silently stalls. Fix: restore the dispatch-slice read to Beat 2 **alongside** capabilities (+ its mutation-license paragraph). vlt-core re-grafted it locally (its one governance divergence) — folds back to zero when the module fixes it.
  2. **Per-skill `.decision-log.md` build cruft lands in the installed surface.** The own-the-apply merge-copy dragged 10 dev `.decision-log.md` files into the vault; one clobbered the vlt-mint relocation stub. They're gitignored from the *repo* but still on disk in the working tree, so a **filesystem** merge-copy still grabs them. Fix: remove them from the working tree and/or add a copy-exclude so they never reach a vault. (Confirms the relocation stub's value.)
  3. **`merge-help-csv.py` brittle vs unquoted-comma rows (write-side sibling of build-3's read-guard).** vlt-core's live `module-help.csv` had 2 rows (`vlt-agent-health-coach`, `vlt-lint`) with unquoted commas → parse hard-fails before the local-mint preserve step → registration blocked until hand-fixed. Fix: make `vlt-mint` / help-row authoring **always quote** free-text fields, AND/OR make `merge-help-csv.py` skip/repair a bad row instead of aborting.
  4. **Upstream candidate — `vlt-track`.** The local longitudinal-loop op (design protocol → log progress → review/adjust; caller supplies profile + voice) now fits 0.3.0's invariant-based personalized-extraction firewall cleanly. Candidate to upstream as the canonical loop hand (threads the capability-object/build-7 + personalized-extraction strands).
- *(Historical: prior resume was "ideate Phase D" then "build Phase D" — both done.)* Phase D was specified + built under the **safe-pessimistic assumption** (installer may copy destructively; `vlt-upgrade` reconciles after) with own-the-apply as the happy path. The **confirmed in-repo ship-blocker was B1** (merge-not-replace registration — shipped). The **confirmed in-repo ship-blocker is B1** — `merge-help-csv.py` anti-zombie strips/rewrites all `vlt` help rows from the bundled CSV, deregistering local mints on every upgrade regardless of installer copy strategy; **merge-not-replace registration is the must-ship.** B2 body-restore is insurance. Phase D is also **the unlock for ALL deferred acceptance** (vlt-core can't safely upgrade until `vlt-upgrade` exists). Scope to fold (filing #8): durability principle → operating contract; `vlt-upgrade` skill (pre-flight ledger → reconcile → post-flight report, *calls* vlt-setup); B1 merge-not-replace; §A1 decision-log relocation to `_agent/mint/`; B3 governance-divergence detect+report. **Capability-object strand** (`vlt-partner-capabilities-ideation.md`) and the **deferred vlt-lint method-traces firewall** ride alongside as their own small builds on Phase B's handshake machinery — decide sequencing during Phase D ideation. Note for Phase D: the governance SSoT is now a **single** copy (collapse done 2026-06-24) — one fewer thing for the upgrade path to reconcile. Then **Phase D** (lifecycle durability) — now specifiable: ideate it next (B1 merge-not-replace is the confirmed must-ship; B2 body-restore is insurance under the safe-pessimistic assumption). The deferred lint firewall and the Capability-object strand remain as their own follow-on builds on Phase B's handshake machinery. All live acceptance stays in the **Deferred acceptance ledger**, batched to the first safe (post-Phase-D) `vlt-core` upgrade.

### B2 installer-copy spike record (2026-06-23)
- **Question:** on a module-version upgrade, does the installer **(A)** clean-replace `.claude/skills/vlt-*` (deleting unshipped minted `vlt-agent-*` partners) or **(B)** copy-over-and-leave (bodies survive)?
- **Finding:** **Cannot be determined from module source — the installer is external and not vendored in this repo.** `vlt-setup` is explicitly *additive/non-invasive* and disclaims managing `.claude/skills/` content (`vlt-setup/SKILL.md` ~L31, L242-247). Only an empirical upgrade test (or reading external BMad installer source) would settle A vs B — and that test is the very upgrade this roadmap defers.
- **The decisive sub-finding — B1 is verified and ship-blocking regardless of A/B:** `merge-help-csv.py:186-198` is anti-zombie — on every run it strips **all** `vlt` help rows and rewrites only from the **bundled** CSV (which can't contain a vault's local mints). So locally-minted partners are **deregistered on upgrade even if their dirs survive (B).** Registration durability does not depend on resolving A/B.
- **Resolution for Phase D:** specify D under the **safe-pessimistic assumption** (installer copies destructively first; `vlt-upgrade` reconciles after — already the §C posture). Under it, B2's body-restore is cheap insurance whether A or B holds, and **B1's merge-not-replace fix is the confirmed must-ship.** The A/B answer only toggles whether B2 restore is *mandatory* (A) or *belt-and-suspenders* (B) — it does not block specification. **Phase D is unblocked to ideate.**

### Phase C scoping record (2026-06-23)
- **Scoped** filing #5 (mint phases + resumable planning doc) + filing #6 (personalized extraction + vertical-partner archetype) against current module source. **No conflicts with build-3/build-4** — both filings' target files are clean to edit (Build #4 touched `vlt-mint/SKILL.md` and `extraction.md` only for coherence-handshake additions, orthogonal to phasing/personalization).
- **Filing #5 gap:** `vlt-mint/SKILL.md` is a flat Step 1–4 sequence today — **no** phase headers, **no** exit gates, **no** resume branch; `_agent/mint/` is not yet a named concept in module source; decision log still lives at `vlt-mint/.decision-log.md` (its relocation is **Phase D / §A1**, not C).
- **Filing #6 gap:** `extraction.md` has **no** personalized-extraction section / `personalization_sources:`; operating contract lists `{log} <type>` as an **exhaustive** set (filing wants it marked non-exhaustive); `vlt-agent-creative/SKILL.md` has **no** carve-out; `frontmatter.md` correctly needs no change; `partner-agent-template.md` has **no** vertical-partner archetype docs.
- **Capability-object strand:** its lightweight-capability tier is the *same vertical-partner problem from the other side* (own-zone write → light, no ceremony) and its lane-firewall lint == filing #6's deferred method-traces-to-wiki firewall. Roadmap leaves open whether the light tier ships **with** C or as its own small build.
- **Owner rulings (2026-06-23):** (1) **Phase C built first**, D follows (both now specifiable; neither needs a live vault). (2) `vlt-lint` method-traces firewall **DEFERRED as a follow-up** — ship the convention widening with prose + verify-checkbox; exposure is bounded (n=1, gated). (3) **Capability lightweight tier KEPT SEPARATE** — Phase C = filings #5 + #6 only; the strand ships as its own small build on B's handshake machinery. → **`build-5-mint-maturation.md` written 2026-06-24.**

### Phase 0 record (for the eventual build_log / commit)
- **Diagnosis (empirical, this session):** the Workflow runtime delivers `args` as a **JSON-encoded string** for every invocation form (name / scriptPath / inline script) — confirmed with an echo-workflow test. Filing #7's "args dropped / harness defect" was a misread of `args || {}`-then-`.prop` over a string.
- **Change:** added `let a = args||{}; if (typeof a==='string'){try{a=JSON.parse(a)}catch{a={}}}` to the top of both `skills/vlt-setup/assets/workflows/vlt-review-council.js` (was line 32) and `…/vlt-lint-full.js` (was line 30), with a why-comment.
- **Verified:** a replica of the council intake+guard with the fix returns `GUARD PASSED` (mode/kind/subject/personasPath all resolve from string-delivered args).
- **Not changed (correctly):** callers — both already invoke by name; no recovery notes were ever added, so none to remove. Filing #3's resume caveat (re-pass `args` on `resumeFromRunId`) remains valid and rides into Phase A's lint-full work.

### Phase D ideation record (2026-06-24, IN PROGRESS — durability) — filing #8
Owner-steered ideation of Phase D (lifecycle durability). Captured live as the cache; spawns `build-6-*.md`.

**Owner signals (this session):**
1. **Ideal = vlt-upgrade owns the upgrade entirely** (no dependence on the destructive BMad installer); accepts a before-and-after bracket session *only if* the installer is an unavoidable requirement.
2. **The real grief = losing local convention edits.** (Bodies/registration matter, but convention loss is what would actually hurt → weight engineering there.)
3. **The divergence ledger is a standing record** to view vault evolution over time — NOT a throwaway per-upgrade diff. → durable, append-only, agent-zone (`_agent/upgrade-ledger.md`).

**Design synthesis so far:**
- **Acquire vs apply split.** The upgrade is two welded jobs: *acquire* new module bits + *apply* them to the vault. The installer does both destructively. Owning the *apply* is all the owner's ideal requires. → **vlt-upgrade design: prefer-to-own the apply** (merge-copy from a reachable module source — no destruction ever); **degrade to bracket mode** (snapshot-before → installer runs → reconcile-after) only when bits arrive welded to a destructive apply. Same skill, same reconcile logic, two entry paths. Ships without resolving the B2 installer unknown — owning-it is the happy path, bracketing the guard rail.
- **Overlay conventions (owner's idea — supersedes 3-way merge).** Don't edit base conventions in place. Base convention stays **pristine → always overwrite-safe → upgrades cleanly every time**; local edits live in a **distinct overlay file in the agent zone** (e.g. `_agent/conventions/{name}.overlay.md`) → upgrade-durable by location; **consumers merge base+overlay on read**. The collision *never forms* (vs 3-way, which only detects+resolves it). Same move vlt already makes everywhere: separate durable location + merge, not edit-in-place. Mirrors BMad's own customize/override philosophy.
  - **Threads Phase B:** the version-handshake already makes consumers declare `depends_on: ["name@version"]`; "also read the local overlay" extends the *same* resolver. Coherence machinery (B) and durability machinery (D) are the **same seam**.
  - **Rewires Phase C (build-5):** vlt-mint's `convention edit` kind currently edits the base in place → under overlays it must **write to the overlay, never the base**, making mint output upgrade-durable by construction. Concrete edit to a just-built thing.
  - **Merge semantics — DECIDED (owner, this session): append-only + report safety net.** Overlay can only ADD (new field / rule / section) — no addressing scheme, unambiguous precedence, covers the 80%. To CHANGE an existing base rule you edit the base directly, and the upgrade's **detect-and-report safety net** catches it (warns, never silently clobbers). One-time **migration lifts vlt-core's existing in-place convention edits into overlays.** Section-override deferred until a real edit demands it.
- **Posture (from prior Q):** owner chose "decide during ideation" → resolved above as prefer-own / degrade-to-bracket.

**RESOLVED + brief written → `build-6-lifecycle-durability.md` (PLANNED 2026-06-24):**
- Merge semantics: **append-only + report safety net** (owner-decided).
- Posture: **prefer-own / degrade-to-bracket** (owner "decide during ideation" → resolved).
- §A1 decision-log relocation: **confirmed still genuinely Phase D** — build-5 moved only the *resumable planning doc* to `_agent/mint/`; the **permanent `.decision-log.md` is still in the clobber-prone `vlt-mint/` skill dir** (verified). Relocate in build-6.
- B1 grounded: `merge-help-csv.py:117-119` `filter_rows` strips all `vlt` rows → fix = preserve local-mint rows whose dir exists live but is absent from the bundle.
- Ledger: `_agent/upgrade-ledger.md`, top-level, append-only standing record.
- Durability principle wording → operating contract (Part 6 of the brief).
- Strand sequencing: **Capability-object strand → build-7, vlt-lint method-traces firewall → build-8** (owner ruling: keep build-6 to filing #8 durability core only).

The six parts (vlt-upgrade skill · overlays+baseline · B1 · B2 · A1+ledger · durability-principle), build order, migration, acceptance, and open questions are all in `build-6-lifecycle-durability.md`. **Next: build it.**
