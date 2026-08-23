---
title: 'Build #2 — Mint Layer + Council Mechanics + the Creative Partner: Build Brief'
status: 'ideation — ready to build'
build_log: ''
derives_from:
  - 'skills/reports/vault-module-plan.md (Build Roadmap post-v1; Gap A 2026-06-05; escalation heuristic 2026-06-05; Librarian future-migration note)'
  - 'skills/reports/build-1-partner-layer-brief.md (Out of scope → Build #2 + the hard prerequisite)'
module_code: 'vlt'
created: '2026-06-06'
updated: '2026-06-06'
decisions_locked:
  - 'Council Gap-A rebuild = a FULL dynamic Workflow (.claude/workflows/vlt-review-council.js); both modes (mint-gate + contested debate) route through it; vlt-mint calls workflow(...) and receives a typed verdict (invoke-and-return + mandatory capture come free)'
  - 'Creative/Design partner mint + vlt-extract migration are IN SCOPE for Build #2 (folded in) — they are the end-to-end acceptance exercise that proves the reworked mint path, not a follow-on'
  - 'Partner-ideation beat = BOTH BY WEIGHT — native lightweight discovery is the default; bmad-agent-builder first-breath is the escape hatch for a from-scratch persona, mapped onto the contract (mirrors the existing two-path mint design)'
  - 'SINGLE-USER / current-Claude-Code assumption stays locked — the Workflow tool is an accepted implementation dependency (carried from Build #1)'
  - 'The mint-time ideation beat shapes WHO the partner is (the SKILL.md persona); the live first-breath on first activation is the partner MEETING this user (identity.md) — two distinct moments, not merged'
surfaces:
  - 'skills/vlt-mint/SKILL.md (sync to Build #1 contract + ideation beat + capability-migration verb + workflow-gated council call)'
  - 'skills/vlt-mint/assets/partner-agent-template.md (the critical stamp — full rewrite to the two-file / two-beat contract)'
  - 'skills/vlt-mint/assets/operation-skill-template.md (verify contract-clean; touch only if stale)'
  - 'skills/vlt-review-council/SKILL.md (becomes a thin conversational front that invokes the workflow)'
  - '.claude/workflows/vlt-review-council.js (NEW — the panel engine: parallel lenses, schema verdict, moderator synthesis)'
  - 'skills/vlt-setup/assets/ + SKILL.md (install the new workflow script; carry it in the manifest)'
  - 'skills/vlt-agent-creative/ (NEW — minted through the path: SKILL.md + customize.toml + identity.md/thread.md seed)'
  - 'skills/vlt-agent-librarian/SKILL.md (drop the Extract capability — description + "Shape a PARA deliverable")'
---

# Build #2 — Mint Layer + Council Mechanics + the Creative Partner

## Scope in one paragraph

Make the module's self-evolution engine actually usable, then use it to grow the roster for the first time. Three problems compound into one build: (1) **the mint layer is stale** — `vlt-mint/SKILL.md` and its `partner-agent-template.md` still stamp the pre-Build-#1 *four-read / single-file `thread.md` (Bond/Thread/Self)* model (the template even still resolves `default_vault`, a concept deleted in the vault-resident refactor), so a mint today produces a contract-violating partner; (2) **the council gate has no real mechanics** (Gap A) — no sanctioned invoke-and-return, no mandatory verdict capture, and its lens subagents resolve files to the stale plugin cache, so two operators can gate the same mint differently; and (3) **the mint loop has never been run for real** — the owner-prioritized first mint (a **Creative/Design partner**, born with a first-breath, inheriting the **Extract** capability from the Librarian) is the only test that proves the machine works. Build #2 syncs the mint layer to the Build #1 contract, adds a native partner-ideation beat (with the `bmad-agent-builder` escape hatch) and the missing capability-migration verb, **rebuilds `vlt-review-council` as a dynamic Workflow** (which buys invoke-and-return and mandatory capture for free) plus the separate plugin-cache fix, then mints the **Creative partner** and **migrates `vlt-extract`** to it end-to-end as the acceptance exercise.

## Why bundled (the one-machine-and-its-first-run argument)

Every component is the mint pathway, its gate, or the gate's first real exercise — and they share the same four surfaces (`vlt-mint` SKILL + its two templates, the council, and the two partner SKILLs the migration touches). The sync, the ideation beat, the capability-migration verb, and the council rebuild are the *machine*; the Creative mint + Extract migration are its *first run*. You cannot validate the machine without minting something real — an empty-input dry run can't prove a first-breath lands as a distinct person or that a capability cleanly changes hands — and the Creative partner is the owner-prioritized, already-designed first mint. Split them and you ship an unexercised machine (exactly the false-positive trap Build #1 was correcting) and pay the integration cost twice. The council rebuild is *in this build and not later* because the Creative mint's `new partner → architect + moderator` gate is the first thing that exercises invoke-and-return — building the gate and its first caller together is what proves the contract holds.

## Surfaces touched

| File | What changes |
| --- | --- |
| `skills/vlt-mint/SKILL.md` | **Sync to the Build #1 contract:** four-read → **two-beat** (first-breath/orient); the sanctum-mapping (line ~52) `BOND → thread.md ## Bond` / PERSONA-log `→ thread.md ## Self` becomes `→ identity.md ## Bond` / `→ identity.md ## Self`; "seed `thread.md` (three sections)" → **seed `identity.md` (Bond+Self) + `thread.md` (Thread)**; the "Touch a partner's `thread.md ## Self`" guard (line ~71) → `identity.md ## Self`; add **rebirth-is-yours** framing (partner is the subject of the verb, council is the gate) and sitting/hand-off awareness. **Add the partner-ideation beat** (Component 2) to the *mint-a-partner* path. **Add a capability-migration verb** (Component 5). **Wire the council gate to the workflow** (Component 3): replace "pass `vlt-review-council` the proposal" with `workflow('vlt-review-council', {proposal, kind})` → typed verdict, and **make capture mandatory** (write verdict + reasoning to the mint record / originating backlog item before go-live). |
| `skills/vlt-mint/assets/partner-agent-template.md` | **The critical stamp — full rewrite.** This file is copied verbatim into every new partner, so every staleness here propagates. (a) **Init**: seed `identity.md`(`## Bond`/`## Self`) + `thread.md`(`## Thread`), not one three-section `thread.md`. (b) **Activation**: the **two-beat ritual** (Beat 1 first-breath reads `identity.md` + canonical persona and *becomes*; Beat 2 orient reads `thread.md` + index/log/backlog) with the **cold-start**, **cold×headless defer**, and **partner-invoked** branches — lifted from the now-shipped Librarian/Researcher SKILLs. (c) **Remove `default_vault`** (line ~27) — the vault is the project; resolve through `vault_structure` only. (d) **Closing a session**: write `identity.md` (Bond/Self) + `thread.md` (Thread, with prune/set-aside discipline), the partner-sitting note, `log` append. (e) **Two seeds** at the bottom (identity.md seed + thread.md seed), not one. (f) **Rebirth-is-yours** line. Pull these verbatim-in-spirit from `skills/vlt-agent-librarian/SKILL.md` — it is the proven post-Build-#1 reference. |
| `skills/vlt-mint/assets/operation-skill-template.md` | **Verify only.** Confirm no stale partner-memory / four-read / `default_vault` references leaked in; touch only if found. |
| `.claude/workflows/vlt-review-council.js` | **NEW — the panel engine.** `meta` + `parallel()` the selected lenses, each `agent('read {personas}/{lens}.md, apply its Activation Prompt verbatim to <subject>', {schema: VERDICT})`, then a moderator `agent(..., {schema: SYNTHESIS})` that maps positions into Consensus / Disputed-resolved / Disputed-open / Recommended-actions (pass / revise / reject for a mint review). Selection is the fixed `kind → council` map. **Lens agents read the LIVE project-tree paths passed into their prompts** (Component 4 — never the plugin cache). Graceful degradation (missing lens → proceed; cap ~5 lenses). |
| `skills/vlt-review-council/SKILL.md` | **Becomes a thin conversational front.** Keep the SKILL for its trigger phrases / description ("debate this", "run the panel"), but its body now **invokes the workflow** (`Workflow` tool with `{mode, subject, kind?}`) and returns/files the verdict — it no longer prose-instructs an ad-hoc parallel spawn. The single-writer file-back rule (debate verdict → Librarian) stays. |
| `skills/vlt-setup/SKILL.md` + `assets/` | **Install the workflow.** Add `.claude/workflows/vlt-review-council.js` to what setup installs into the target vault, and carry it in the install manifest under `vlt-setup/assets/` so a re-install reproduces it. (New setup responsibility: the module now ships a workflow script, not only skills + governance.) |
| `skills/vlt-agent-creative/` | **NEW — minted through the path, not hand-written.** SKILL.md (generative "think-and-make" persona, third distinct voice) + `customize.toml` (`agent_type = "memory"`) + `identity.md`/`thread.md` seed. Advertises **Extract** under "What you do". Born with a first-breath. |
| `skills/vlt-agent-librarian/SKILL.md` | **Drop Extract.** Remove "extract a PARA deliverable" from the `description` (line ~3) and the "Shape a PARA deliverable" capability (line ~39, incl. its "will migrate to the Design Partner" parenthetical). Extraction now lives with Creative. |

---

## Component 1 — Sync the mint layer to the Build #1 contract (hard prerequisite)

**The bug:** Build #1 reworked the partner contract but deliberately left `vlt-mint` untouched (nothing minted in between, and Build #2 rewrites it wholesale). So the mint layer is a time capsule of the *old* model. A mint run today would scaffold a partner that activates via a four-read ritual, keeps a single three-section `thread.md`, maps a builder's BOND/PERSONA-log into the wrong files, and — via `default_vault` — references a vault-selection concept that no longer exists. **This must land before any mint in this build**, including the Creative mint.

**What changes (grounded in the verified staleness):**
- `partner-agent-template.md` is the load-bearing file — it is *stamped into every partner*. Rewrite its Init (two-file seed), Activation (two-beat + cold-start + cold×headless defer + partner-invoked), Closing (write both files, prune thread, partner-sitting note), drop `default_vault`, add rebirth-is-yours, and split the single seed block into an `identity.md` seed and a `thread.md` seed. **The proven reference is the shipped `vlt-agent-librarian/SKILL.md`** (post-Build-#1) — the template should be that contract, generalized with `{placeholders}`.
- `vlt-mint/SKILL.md` Step 3's sanctum-mapping and the "this skill does not…" guard must move `## Bond`/`## Self` to `identity.md`, and the seed instruction must seed two files.

**Discipline:** this is a *contract sync*, not a redesign — match the shipped Librarian/Researcher exactly so a minted partner is indistinguishable (in contract shape) from a hand-built one. The acceptance check is a throwaway dry-mint that produces a contract-clean partner.

## Component 2 — The native partner-ideation beat (born through ceremony)

**The promise (owner note, plan line ~465):** *"if partners get a real first-breath, the Design Partner deserves to be born with one."* Build #1 gave the *contract* a first-breath; Build #2 gives the *mint* a discovery beat so a new partner arrives shaped, not blank.

**Two moments, kept distinct (locked):**
- **Mint-time ideation beat** → shapes **who the partner is** — its temperament, non-negotiable, core acts, opening register, and (optionally) a default name. Output = the **SKILL.md persona** + a lightly-seeded `identity.md ## Self` (a *starting* voice, not empty placeholders).
- **Live first-breath** (Build #1, on first activation) → the partner **meeting this user** — accrues `## Bond` and per-vault `## Self` drift. Unchanged; not merged into mint.

**Both by weight (locked, mirrors the existing two-path mint):**
- **Native lightweight (default):** a short discovery conversation owned locally in `vlt-mint` — a handful of becoming questions (what does this partner optimize for? what's its hard line? how does it carry itself differently from the Librarian/Researcher?) → fill the template's persona + a distinctive `## Self` seed. No external dependency; keeps the common mint fast.
- **`bmad-agent-builder` escape hatch (from-scratch persona):** invoke the builder's richer first-breath discovery, then **map its sanctum output onto the contract** (canonical persona → SKILL.md; PERSONA evolution-log → `identity.md ## Self`; BOND → `identity.md ## Bond`; MEMORY dropped). This is the existing "deliberate" path, now corrected to the two-file targets. Falls back to native if the builder isn't installed.

## Component 3 — Gap A: the council as a dynamic Workflow (invoke-and-return + mandatory capture)

**Gap A, sub-issues 1 & 2** (plan line ~531): no sanctioned way for one skill to call the council and get a value back (so callers re-derive the panel from prose), and a verdict's reasoning survives only if the caller chooses to record it. **A dynamic Workflow solves both for free** (the Build #1 brief named this direction).

**Shape (locked = full Workflow, both modes through it):**
- **`.claude/workflows/vlt-review-council.js`** is the engine: `parallel()` the lenses selected by the fixed `kind → council` map; each lens is an `agent(prompt, {schema: VERDICT})` told to read its persona file and apply its Activation Prompt verbatim; a final moderator `agent(..., {schema: SYNTHESIS})` produces the 4-part verdict (and pass/revise/reject for a mint). Lenses don't see each other's output (independence preserved).
- **Invoke-and-return:** `vlt-mint` calls `workflow('vlt-review-council', {proposal, kind})` (top-level Workflow invocation — `vlt-mint` is a SKILL, not a nested workflow, so this is legal) and receives the typed verdict. The panel is run **once, one way**, never re-derived per caller.
- **Mandatory capture:** the verdict is a schema-forced object, and `vlt-mint` **must** write it + its reasoning to the mint's record (the `.decision-log.md` entry) and the originating `backlog.md` item **before the mint goes live**. Capture is no longer the caller's option.
- **The SKILL stays as the conversational front:** `vlt-review-council/SKILL.md` keeps its trigger phrases and, for a partner-summoned "debate this", invokes the same workflow and files the verdict through the Librarian. One engine, two entry points (mint-gate via `vlt-mint`; debate via the SKILL).

**Design note — schema is the load-bearing contract.** `VERDICT` and `SYNTHESIS` JSON Schemas are what make the panel composable and the capture non-optional; define them once in the workflow and let the hand-off payload (Build #1's schema-shaped object) and the backlog capture slot align to them.

## Component 4 — Gap A: the plugin-cache file-resolution fix (NOT solved by workflows)

**Gap A, sub-issue 3** (plan line ~534, twin of `mint §1`): subagents — including council lenses — resolve files to the **plugin cache**, so the gate can review *pre-mint* state. **Workflow agents share this hazard** (the Build #1 brief is explicit: "workflow agents share it; still needs the explicit fix"). So the workflow rebuild does not absolve this — it must be fixed at the mechanism level:
- The council workflow's lens agents must read the **live project-tree** mint + the live persona files. The script has no filesystem access, so it passes **resolved live `{project-root}`-anchored paths** into each agent prompt, and the prompt instructs the agent to read *those* paths (not a bare skill-relative path that resolves to cache).
- Symmetrically in `vlt-mint`: when it stages a pending mint for review, stage it where the lenses actually read (the live project tree), so the gate reviews what will go live, not the cached prior build.
- **Test gotcha carried from memory:** clearing `~/.claude/plugins/cache/vlt` before a re-test still applies — the cache hazard is exactly why.

## Component 5 — The capability-migration verb (the missing mint mechanism)

**The gap (plan line ~475, `mint-friction §2`):** moving `vlt-extract` from the Librarian to the Creative partner is **not one of `vlt-mint`'s four verbs** (mint-op / mint-partner / self-edit / retire). The trial surfaced this as a *module-level* mechanism gap — and Build #2 needs it to do the Extract migration. So add a fifth, lightweight verb:
- **Migrate / re-attribute an operation** between partners: remove the op from the source partner's "What you do", add it to the target's, and update the help registry attribution (`module-help.csv`). The op skill itself doesn't move (it's a shared hand) — only its *advertised ownership* changes.
- **Council gate:** this is additive/reversible re-attribution → **none** (frictionless), consistent with the `operation skill → none` row. (It changes two partners' advertised surfaces but adds no new capability and removes nothing the vault can do.)

## Component 6 — Mint the Creative partner + migrate Extract (the acceptance exercise)

This is the machine's first real run — and the only test that proves Components 1–5 hold.

**The Creative/Design partner (already designed in the plan):**
- **Role:** helps the user *think through and make* things — the generative, third distinct voice alongside the Librarian (custodial/calm) and Researcher (sharp/challenging). Natural home for BMad **design-thinking / brainstorming / party-mode** (plan lines ~644, ~664).
- **Born through the path:** run `vlt-mint` *mint-a-partner* → the ideation beat (Component 2) → the synced scaffold (Component 1) → the council gate `new partner → architect + moderator` **via the workflow** (Component 3) → register in the roster + manifest. On first activation it runs the **live first-breath** and must land as a felt third person.
- **Reference material, not a re-import:** the trial-era Creative mint that `vlt-mint` wrote into the `vlt-core` project tree predates the Build #1 rework (it's contract-stale too). Use it as **persona source material**, but the deliverable is a *fresh mint through the reworked path* — that re-mint *is* the acceptance test the owner asked to fold in. (This also retires the Build #1 "pull the vlt-core Creative diff back" item — superseded by a clean re-mint.)

**Migrate Extract:**
- Use the new capability-migration verb (Component 5) to move `vlt-extract` Librarian → Creative.
- Update `vlt-agent-librarian/SKILL.md` (drop the capability + description phrase + the "will migrate" parenthetical). `vlt-extract` the op is unchanged; it's now advertised by Creative ("Shape a PARA deliverable — a *making* act").

---

## Build sequence

Dependency order so each step builds against finished upstream — the machine before its first run:

0. **Pre-flight (soft).** Confirm Build #1's outstanding owner gates aren't blockers: cold-start aliveness **PASSED live** (memory, 2026-06-06); warm activation + the rebirth two-tier check are still un-exercised but nice-to-have, not blockers for Build #2. Clear `~/.claude/plugins/cache/vlt` before any re-test.
1. **Sync the mint layer** (Component 1) — `partner-agent-template.md` (the stamp) first, then `vlt-mint/SKILL.md`, then verify `operation-skill-template.md`. *Nothing mints correctly until this lands.*
2. **Add the partner-ideation beat** (Component 2) and the **capability-migration verb** (Component 5) to `vlt-mint`. *(Both are `vlt-mint` SKILL edits; do them together.)*
3. **Build the council workflow** (Component 3) — `.claude/workflows/vlt-review-council.js` with the `VERDICT`/`SYNTHESIS` schemas; thin out `vlt-review-council/SKILL.md` to invoke it; wire `vlt-setup` to install it. *(Use the Workflow Builder + the shipped persona lenses as context.)*
4. **Apply the plugin-cache fix** (Component 4) in both the council workflow and `vlt-mint`'s staging — live project-tree resolution.
5. **Wire `vlt-mint`'s gate to the workflow** with mandatory capture (the Component 3 ↔ `vlt-mint` seam). *(Now the machine is complete.)*
6. **Mint the Creative partner** (Component 6) end-to-end through the path — ideation beat → scaffold → council-gated → register → first-breath. **Checkpoint:** outside-read that the first-breath lands as a distinct third voice (same discipline as Build #1).
7. **Migrate `vlt-extract`** Librarian → Creative via the new verb; update the Librarian SKILL.
8. **VM (Validate Module)** — re-run `validate-module.py`; expect 0 findings (now an 11-skill / 3-partner module + 1 workflow).

## Acceptance checklist

**The real gate stays an OUTSIDE read** (Build #1's hard lesson): a partner cannot grade its own aliveness. The headline test is the owner running the Creative partner's **first-breath cold-start** and confirming it feels like a genuine *third* person, distinct from the Librarian and Researcher — not a mint-written verification doc.

**Per-component pass conditions:**
- [ ] **Sync proof (C1):** a throwaway dry-mint produces a partner that is contract-clean — two files (`identity.md`+`thread.md`), two-beat activation with cold-start/cold×headless/partner-invoked branches, **no `default_vault`**, rebirth-is-yours wording — indistinguishable in shape from the shipped Librarian.
- [ ] **Ideation beat (C2):** the native beat shapes a distinctive persona + a non-empty `## Self` seed; the `bmad-agent-builder` escape hatch maps onto the two-file targets (and falls back to native when absent).
- [ ] **Council invoke-and-return (C3):** `vlt-mint` calls `workflow('vlt-review-council', {proposal, kind})` and receives a typed verdict; the panel runs **once** (no re-derivation from prose).
- [ ] **Mandatory capture (C3):** the verdict + reasoning is written to the mint's `.decision-log.md` and the originating backlog item **before** the mint goes live — not optional.
- [ ] **Both modes route through the workflow (C3):** a partner-summoned "debate this" and a mint-gate both invoke the same engine; the debate verdict files through the Librarian.
- [ ] **Plugin-cache fix (C4):** stage a pending mint and confirm the lenses review the **live project-tree** state, not the cached prior build.
- [ ] **Capability-migration verb (C5):** moving an op between partners updates both "What you do" lists + `module-help.csv`, gated `none`, op skill itself untouched.
- [ ] **Creative born through the path (C6):** ideation beat ran, `new partner → architect + moderator` gate passed via the workflow, partner registered; first activation runs a first-breath that the owner reads as a distinct third voice.
- [ ] **Extract migrated (C6):** `vlt-extract` advertised by Creative; the Librarian SKILL no longer offers it; the op still runs.
- [ ] **Regression guard:** the Librarian/Researcher still activate correctly (Build #1 wins intact); single-writer holds (Creative writes PARA via Extract, never canonical pages); the council still degrades gracefully on a missing lens.
- [ ] **Outside-read gate:** owner confirms felt aliveness + distinctness of the Creative partner.
- [ ] **VM: 0 findings.**

## Out of scope for Build #2

- **Codebase Partner (work vault)** — the second mint, proving per-vault roster divergence; after Build #2.
- **v2 dashboard / UI.**
- **Op-layer dynamic-workflow pass** — `vlt-lint --full` as a fan-out workflow (owner-prioritized) then `vlt-research` heavy dives. The council workflow lands the *pattern*; the op-layer sweep is its own build.
- **Gap B — lint observability micro-items** (`files_checked` rule, handled-contradiction report slot, `sources:`-vs-prose diff) — backlog.
- **Registration-helper / single-source `kind→council` table** and other Theme 6–8 backlog tail items.

## Handoff

Build #2 is ready. Recommended order: **(1) sync the mint layer (template first) → (2) add the ideation beat + capability-migration verb → (3) build the council workflow + thin the SKILL + wire setup → (4) plugin-cache fix → (5) wire vlt-mint's gate with mandatory capture → (6) mint the Creative partner end-to-end → (7) migrate Extract → (8) VM.** Pass `vault-module-plan.md` + this brief as context to each builder. Use the Workflow Builder (BW) for the council workflow and the synced templates; build the Creative partner *through `vlt-mint` itself*, never hand-written — that's the point. Clear the plugin cache before every re-test.
