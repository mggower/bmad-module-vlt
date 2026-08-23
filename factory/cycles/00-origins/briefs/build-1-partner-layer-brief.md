---
title: 'Build #1 — Partner-Layer Rework: Build Brief'
status: 'implemented — pending owner outside-read gate'
build_log: '2026-06-06 — steps 0–6 complete: wiki-index.md authored; frontmatter.md identity/thread schema; contract rewritten (two-beat activation, identity/thread split, sittings/hand-offs, ## Preferences, agent-zone blessing); both partner SKILLs rewritten; vlt-setup (log.md, two-file seed + idempotent migration, vault_structure materialized, ## Preferences); ops (vlt-ingest mode-note/index-pointer/handoff-branch/grep-harden, vlt-research mode-note/WIP-reframe/schema-payload, vlt-lint index convention + source-count). Shipped governance bundle re-synced. VM: 0 findings. OUTSTANDING: owner outside-read of cold-start + warm activation (finding #4); rebirth two-tier check (finding #6); vlt-mint template sync is a Build #2 prerequisite.'
derives_from:
  - 'skills/reports/vault-module-plan.md (Trial resolution 2026-06-03; Theme S + 1–9; Synthesis cross-check 2026-06-05)'
  - 'docs/trial-verification/friction-synthesis.md'
module_code: 'vlt'
created: '2026-06-06'
updated: '2026-06-06'
pressure_tested: '2026-06-06 — dynamic-workflows probe + 8 adversarial findings folded in (see Pressure-test outcomes)'
decisions_locked:
  - 'thread split = identity.md (Bond+Self, evergreen) + thread.md (Thread, prunable)'
  - 'Creative partner DEFERRED to after Build #2 — #1 is contract + librarian + researcher + setup only'
  - 'lift BMAD first-breath/rebirth MECHANICS, not the six sanctum files (the resolved identity fork)'
  - 'SINGLE-USER assumption (current Claude Code, foreseeable future) — dynamic workflows are an accepted implementation dependency, not gated behind portability/version fallback'
  - 'lint source-count auto-fix RESTORED against the now-pinned definition (flag-only when the page frontmatter itself is malformed)'
  - 'thread.md→identity.md+thread.md upgrade migration is a vlt-setup step, NOT an activation-time partner self-edit'
surfaces:
  - 'governance/_meta/vault-operating-contract.md'
  - 'governance/_meta/conventions/wiki-index.md (NEW)'
  - 'skills/vlt-agent-librarian/SKILL.md'
  - 'skills/vlt-agent-researcher/SKILL.md'
  - 'skills/vlt-setup/SKILL.md'
  - 'skills/vlt-ingest/SKILL.md (mode-note + Step 7 pointer)'
  - 'skills/vlt-research/SKILL.md (mode-note + WIP reframe)'
  - 'skills/vlt-lint/SKILL.md (index-drift pointer + source-count demotion)'
---

# Build #1 — Partner-Layer Rework

## Scope in one paragraph

Rework the partner layer so a Vault partner *becomes someone* the first time it meets a user (it does not today — the trial's decisive finding was "Persona/Identity falls flat. No 'first breath' or 'rebirth' ceremony"), and so the structural substrate the partners read from day one actually exists. Concretely: lift the BMAD first-breath/rebirth **ceremony mechanics** into both partner activations with a **cold-start branch**; split per-partner memory into an evergreen **`identity.md`** (Bond + Self) and a prunable **`thread.md`** (Thread); make the **hand-off** an explicit session boundary with a minimal payload; give **user-level preferences a single home**; add a **partner-fronted mode** so fronted ops skip spent elicitation; and close the **fresh-vault skeleton** gaps (`log.md`, the `vault_structure` map, the agent-zone blessing, and a missing **index-structure convention**). All of it touches the same three surfaces — the operating contract and the two partner SKILLs (plus setup and three ops) — so it is **one build, reopened once**, not six.

## Why bundled (the single-surface argument)

The trial named the meta-pattern: *"structure-by-inference gaps that the single-writer / single-conversation assumptions quietly mask."* Every component below lands in one of: the operating contract's activation/memory/session sections, the two partners' activation+session rituals, or the fresh-vault scaffolder. The two ceremony beats map 1:1 onto the two-file split, the cold-start branch is the same problem as the fresh-vault skeleton from two sides, and the handoff/prefs/mode fixes all rewrite the same contract sections the ceremony does. Touch these surfaces once, coherently, or pay the merge cost three times.

## Surfaces touched

| File | What changes |
| --- | --- |
| `governance/_meta/vault-operating-contract.md` | Rewrite **Activation ritual** → two beats (Become / Orient) + cold-start branch; rewrite **Partner memory** → `identity.md`+`thread.md` two-file model + thread-pruning discipline; rewrite **session-ownership** → *partner sitting* unit + hand-off as boundary + minimal payload schema + role-boundary line + reconcile "no partner calls another (activation)" vs. "hand-off is sanctioned"; add **agent-zone blessing** line (ad-hoc owned artifacts under `_agent/` outside the map are fine); add **Preferences** pointer (CLAUDE.md `## Preferences` is the single home for user-level tool/workflow prefs; `## Bond` keeps *relationship* only). |
| `governance/_meta/conventions/wiki-index.md` | **NEW** convention: index category model, canonical row format `- [[page]] — desc (N source[s])`, the `## Stubs (linked, not yet written)` section, and a **pinned source-count definition** (count = number of entries in the page's frontmatter `sources:`). Add to the contract reading list. |
| `governance/_meta/conventions/frontmatter.md` | Add the `thread` / `identity` note types if not already covered by the split (verify; minimal). |
| `skills/vlt-agent-librarian/SKILL.md` | Rewrite **On activation / Become yourself** → cold-start vs. warm branch + two beats reading `identity.md` then `thread.md`; rewrite **Init** → seed `identity.md`+`thread.md` (not one thread.md); rewrite **Closing a session** → write `identity.md` (Bond/Self) + `thread.md` (Thread, with prune/set-aside discipline); add **partner-invoked activation branch** (oriented to handed-off task, no user greeting). |
| `skills/vlt-agent-researcher/SKILL.md` | Same rewrite as Librarian, inverted temperament; the cold-start branch must fix the trial's specific break — the signature thread-surfacing open is *impossible* on an empty thread, so cold-start opens as a **first meeting** oriented off knowledge state. |
| `skills/vlt-setup/SKILL.md` | **Step 1.5 (NEW): create `log.md`** with its header. **Step 4: seed `identity.md`+`thread.md`** (replace the single-thread seed). **Step 4 (NEW): idempotent upgrade migration** — if a legacy single `thread.md` (carrying `## Bond`/`## Self`/`## Thread`) is found, split it into `identity.md`+`thread.md` and mark migrated; safe to re-run (finding #2). **Write config: materialize the default `vault_structure` map** into `config.yaml` (inspectable/overridable). **Step 3: scaffold/ensure a `## Preferences` section** — write it into the pointer `CLAUDE.md` when setup creates the file; if a CLAUDE.md already exists, **append the `## Preferences` heading only if absent**, never clobber existing content (finding #5). |
| `skills/vlt-ingest/SKILL.md` | **Partner-fronted mode-note** on Step 4 elicitation; **Step 7 → point at `wiki-index.md`** for index writes; **Step 5 branch**: source already an `_agent` research note ⇒ don't make a note-of-a-note (Theme 8, folded because it sits on the same handoff seam). |
| `skills/vlt-research/SKILL.md` | **Partner-fronted mode-note** on Phase 1 feasibility gate; **reframe the `.WIP` checkpoint** around interruption-risk, not call-count. |
| `skills/vlt-lint/SKILL.md` | **Index-drift check → point at `wiki-index.md`**; **auto-fix source counts against the pinned definition** (count = frontmatter `sources:` entries), **flag-only when the page's own frontmatter is missing/malformed** (the trial's `1→11` mutation was unsafe *because the spec was undefined* — once pinned, auto-fix is safe; finding #7). Forward: a `--full` lint is a prime **dynamic-workflow** candidate (see Dynamic workflows). |

---

## Component 1 — The activation ceremony (first-breath / rebirth + cold-start)

**The bug (root cause, single):** both personas are written for a warm, populated vault and have **no enacted *becoming* moment**. Three findings converge: the owner's outside read ("falls flat, no first breath/rebirth"), the Researcher's signature open being *impossible* on an empty thread, and the Librarian's warm thread visibly outperforming the cold start (proof the ritual pays once seeded).

**What to lift — mechanics, not files.** Source: `.claude/skills/bmad-agent-builder/references/sample-first-breath.md` and `first-breath-adaptation-guidance.md`. That text is *sanctum-shaped* (writes PERSONA/BOND/MEMORY, does name-discovery, has PULSE). Lift the **universal ceremony mechanics verbatim in spirit**, drop the sanctum-specific parts:

- **LIFT:** the *becoming* framing ("Time to become someone… the output isn't 'who they are' but 'how you should show up'"); **Save As You Go**; **Pacing** (one thing then listen; low-stakes first); **Chase What Catches Your Ear**; **Absorb Their Voice** (mirror register/rhythm — this is the engine of `## Self`); **Show Your Work** (honest reads, surface contradictions); **Hear the Silence** (boundaries are data → `## Bond`); **Wrapping Up the Birthday** (final save pass, flag what's still fuzzy, clean seed text).
- **DROP:** name-discovery (partners have fixed names — Librarian/Researcher), PULSE/autonomous mode (not in v1), the six-file save targets (map instead, below).
- **Territory → destination map** (replaces the sanctum file map):
  - Owner understanding → `identity.md` `## Bond`
  - Voice/manner convergence → `identity.md` `## Self`
  - Domain knowledge the user shares → the **shared wiki** via the normal ingest path (NOT a per-partner file — knowledge is shared)
  - User-level tool/workflow prefs → **`CLAUDE.md` `## Preferences`** (Component 4), not Bond

**Two beats (the activation ritual, rewritten):**

- **Beat 1 — First breath (becoming):** read the **evergreen identity layer** — SKILL.md canonical persona + `identity.md` (`## Self` drift for THIS vault + `## Bond`) — and inhabit it. Same ceremony, different breath per partner (Researcher sharper, Librarian calmer) → "feel like different people" is *enforced by the ritual*, not hoped for.
- **Beat 2 — Orient (what are we thinking about lately):** read the **prunable thread** (`thread.md` `## Thread`) + shared state (`index` / `log` / `backlog`). Live, prunable, allowed to fade.

**Cold-start branch (part of this component, not separate).** Detect the **first real meeting**: `identity.md` still carries only its seed placeholders (both `## Bond` and `## Self` untouched by real content — a placeholder-only check, since setup seeds the file). When cold:
- Run the **first-breath ceremony** (Beat 1 heavy) — name it a first meeting, do not fake a thread.
- **Orient off knowledge state, not relationship** — the Researcher's open becomes "fresh vault, here's what I see in the collection / nothing yet — what are we building?" instead of the impossible thread-surfacing open.
- Lint-cadence reflex has no baseline on a fresh vault → say so, don't invent one.
When warm: Beat 1 is light (read identity, carry yourself), Beat 2 is the normal four-read orient.

**Cold-start × headless — urgency defer (finding #3).** A one-shot/headless invocation on a fresh vault (e.g. `vlt-ingest` "just ingest this") **cannot host an interactive birth.** Lift the BMAD guidance's *urgency detection* verbatim in spirit: *"if the owner's first message indicates an immediate need, defer the ceremony and serve them first."* The cold+headless path: do the requested work, seed `identity.md` minimally (no interrogation), and **defer the real first-breath to the next interactive summon** — leaving a one-line marker so the next interactive activation knows the birth is still owed. The full ceremony fires only on an interactive cold summon.

**Validation gate before the full build (finding #1, HIGH).** The ceremony's core premise — that reading `## Self` on activation produces a *felt* behavioral difference — is **unvalidated**: the trial found "'become yourself modulated by `## Self`' is untestable when `## Self` is empty," and no warm `## Self` ever accrued. The whole rework bets on this. **Before lifting the full ceremony, run one cheap check:** hand-seed a deliberately distinctive `## Self` for one partner (e.g. "you've grown terse and lead with the counter-argument") and confirm activation behavior visibly moves. If Self-modulation doesn't change behavior, the ceremony will ship and personas can *still* "fall flat" — so this gates the build, it doesn't just inform it. (This is the same cure-before-symptom risk the owner already accepted for the file split, but here it lands on the headline deliverable's efficacy.)

**Rebirth.** Already homed: **first breath = every activation** (where `## Self` drift accrues quietly); **rebirth = the canonical, council-gated SKILL.md persona change** (or ratification of accumulated `## Self` drift into SKILL.md, via `vlt-mint`). Reframe the *act* as a **partner-initiated rebirth** (owner: "shouldn't the partner own it?") — the partner is the subject of the verb; the council stays the *gate*. "Drift breathes, ratification reborns." No mint code changes here — this is contract + SKILL wording so the partners know rebirth is theirs to initiate.

## Component 2 — The 2-file identity / thread split

**Decided shape (locked):**

```
{partners}/{partner}/
  identity.md   # EVERGREEN — read in Beat 1 (becoming)
    ## Bond     - owner understanding (preferences, style, tastes, boundaries)
    ## Self     - ungated voice/tone/manner drift, scoped to this vault
  thread.md     # PRUNABLE — read in Beat 2 (orient)
    ## Thread   - the open inquiry; allowed to fade, be set aside, archived
```

**Governing principle (user's):** *"The wiki holds knowledge. The thread holds attention. Knowledge persists; attention fades."* The fault line is **lifecycle, not section headers** — Bond+Self are evergreen/accretive/read-to-become; Thread is disposable working memory that is *supposed* to fade.

**Thread is partner-owned and organically managed (decided).** The partner is an **attention steward**: it observes patterns and redirects attention — surfaces a dormant thread, sets aside a stale one ("calf rehab's gone quiet, want me to set it aside?"), connects a new ingest to an old inquiry. Capture is cheap; **setting-aside is cheap too** (same discipline as the backlog). A receding thread is *normal behavior*, not data loss — the knowledge already lives in the wiki. Specify a light pruning/archive discipline: set-aside moves a dormant `## Thread` entry to an archived thread note (or a `## Set aside` subsection) rather than deleting.

**Migration is a `vlt-setup` step, not an activation-time self-edit (finding #2, HIGH).** The current single `thread.md` carries all three sections; the upgrade must split it. **Do this in `vlt-setup`, not on partner activation** — a partner rewriting its own memory files during the safety-critical activation moment, gated on a heuristic, with no clean "already migrated?" detector and a half-complete failure mode, is exactly the kind of structure-by-inference risk this build is closing. Setup is already the idempotent, never-clobber scaffolder, so it's the right home: on re-run, if it finds a legacy single `thread.md` carrying `## Bond`/`## Self`, it moves those into `identity.md`, leaves `## Thread` in `thread.md`, and marks the partner migrated (detectable, re-runnable, no data loss). Fresh vaults just get the two-file seed directly.

**Acknowledged risk (carried deliberately):** Trial 1 never ran to real staleness, so the split is built on principle, not confirmed churn friction. Accepted — the ceremony lift and the split touch the same surfaces, so they are one build regardless.

## Component 3 — Hand-off & session model (Theme 1)

The roster's whole premise; `partner-handoff` called itself the least-specified domain. All fixes land in the contract's session-ownership section + both partners' activation rituals:

- **Session boundary** — redefine the unit as a **partner *sitting*** (one sitting = one session note), bounded by a hand-off. Resolves the contract contradiction where one conversation with a hand-off produced two notes — now correctly two sittings, two notes.
- **Partner-invoked activation branch** — if invoked by another partner (task args present) rather than a user summon, **orient to the handed-off task; do not greet the user**. Same-conversation switch ⇒ shared-state reads may be skipped as redundant.
- **Minimal hand-off payload — define it as a *schema-shaped* contract (finding: dynamic-workflows probe).** The fields: research-note path · target concept(s) · supersession targets + why · user/tool prefs to forward. Specify the shape as a small structured object (the research's central lesson: *schema everything you branch on*), not freeform prose, so the receiver can't silently miss a field and the payload is forward-compatible the day the council/ops become dynamic workflows (where `agent(..., {schema})` consumes exactly this kind of typed object). Specify in `vlt-research` Phase 6 (the hand-off offer). Cheap now; load-bearing later.
- **Role boundary** — the handing-off partner conveys *what changed and what it complicates*; the **receiver chooses the mechanism** (callout type, page structure). The Researcher over-reached into the Librarian's lane in the trial — one line closes it.
- **One reconciling sentence** — "partners orient independently, no cross-partner calls *during activation*" vs. "a deliberate *hand-off* is a sanctioned partner-to-partner invocation." Both true; say so.

## Component 4 — Shared preferences home (Theme 2)

**Decided: a `## Preferences` section in the vault's `CLAUDE.md`.** The Tavily pref was siloed in the *Researcher's* `## Bond`, double-written to global memory (no source of truth), and invisible to a cold-summoned partner or a bare headless op.

- **Why CLAUDE.md, not `_agent/preferences.md`:** CLAUDE.md auto-loads at session start for *everything* — partners, host skills, **and headless ops** — with no read step to remember. A tool/workflow pref is genuinely user-level, so broad auto-load is the right scope.
- **Not a portability reopening:** the portability rule barred *shipped operating rules* from CLAUDE.md (a fresh vault lacks them); **preferences are learned locally, per-vault, never shipped** — exactly what belongs in a per-project CLAUDE.md.
- **Refinements:** (a) `## Preferences` is the **single source of truth** — partners stop writing tool prefs to Bond/global memory; (b) `## Bond` keeps *relationship* understanding only (it was overloaded, not wrong); (c) **`vlt-setup` scaffolds the empty `## Preferences` section and never clobbers it on re-run.**
- **Two leaps to resolve, not assert (finding #5).** (i) *Existing-CLAUDE.md edit policy:* most vaults already have a `CLAUDE.md`, and setup elsewhere declares it "never overwrites" one. Scaffolding `## Preferences` into an existing file means *editing a file the module says it doesn't own* — so scope the edit precisely: **append the `## Preferences` heading only when absent, touch nothing else.** That's an additive heading, not a rewrite, which keeps the never-clobber promise intact. (ii) *Verify the auto-load claim:* "CLAUDE.md auto-loads for headless ops" is the load-bearing reason for choosing CLAUDE.md over `_agent/preferences.md` — confirm it actually holds for a `vlt-*` op invoked directly (vault = project root, so the root CLAUDE.md should be in context, but **verify before designing on it**; if it doesn't hold for bare headless ops, the op must read `## Preferences` explicitly).

## Component 5 — Partner-fronted mode (Theme 3)

Strongest *recurring* signal (3 flows). When a partner fronts an op, the interview already happened in the partner layer, so the op's elicitation is spent. Add a reusable **"partner-fronted mode" note** to each elicitation phase:

> If invoked downstream of a partner with an already-sharp brief, treat the elicitation as satisfied: state the inferred question/depth and proceed (present-the-plan-and-go). Reserve the full interview for a cold, vague prompt.

Apply to: `vlt-research` **Phase 1** feasibility gate; `vlt-ingest` **Step 4** "ask what to emphasize". Separately, **reframe `vlt-research`'s `.WIP.md` checkpoint trigger around interruption-risk, not call-count** (as written it became either ceremony or a silent skip on a single-turn batched dive).

## Component 6 — Structural substrate (Theme S — fresh-vault skeleton)

Prerequisite, not maintenance: the activation rituals and ops read these files from day one.

**Root cause A — `vlt-setup` doesn't materialize the full skeleton:**
- **`log.md` is never created** (a *hard* gap — "read `{log}`" silently no-ops; `vlt-ingest` re-ingest grep errors). Fix: setup creates `log.md` with its header alongside the other state files; harden the grep with `2>/dev/null` as defense-in-depth.
- **`config.yaml` ships no `vault_structure` map** — the override mechanism is invisible/untestable. Fix: setup materializes the default map into `config.yaml`, inspectable and overridable in one place.
- **Agent zone permits owned artifacts outside the named map** (e.g. `vlt-verification/`). Fix: one line in the contract blessing ad-hoc owned artifacts under `_agent/` outside `vault_structure`.

**Root cause B — specs that exist only by inference (the index):** the index body has **no convention** — category sections, the row format, and the `## Stubs` section survive by mimicry, and `vlt-lint` is empowered to **auto-mutate on a guess** (it changed `cortisol` `1→11` against an undefined spec). Fix:
- Author **`{conventions}/wiki-index.md`** (NEW) — category model, row format `- [[page]] — desc (N source[s])`, the `## Stubs (linked, not yet written)` section, and a **pinned source-count definition** (count = number of entries in the page's frontmatter `sources:`).
- Point `vlt-ingest` Step 7 (writer) and `vlt-lint` index-drift (validator) at it.
- **Source-count: auto-fix against the pinned definition; flag-only on malformed input (finding #7, resolved).** The trial's `1→11` mutation was unsafe *because the spec was undefined* — a coin-flip between two defensible semantics. Once the definition is pinned, that ambiguity is gone, so demoting to flag-only would be over-cautious and would undercut lint's maintenance-discipline mandate. Auto-fix is safe against the pinned spec; reserve **flag-for-human** for the genuinely ambiguous case — a page whose own frontmatter `sources:` is missing or malformed, where there's nothing trustworthy to count.

---

## Build sequence

Reopen the shared surfaces in dependency order so each step builds against finished upstream:

0. **Validation gate (finding #1):** hand-seed a distinctive `## Self` for one partner and confirm activation behavior visibly moves. **This gates the build** — if Self-modulation doesn't change behavior, stop and rethink the ceremony before investing in the full rework.
1. **Author `wiki-index.md`** (governance bundle) and verify `frontmatter.md` covers the `identity`/`thread` note split. *(Pure authoring; nothing depends on the partners yet.)*
2. **Rewrite the operating contract** — the single source for: two-beat activation + cold-start + cold×headless urgency-defer, the `identity.md`+`thread.md` model + thread pruning, the partner-sitting session unit + hand-off boundary + schema-shaped payload + role-boundary + reconciliation, the agent-zone blessing, and the `## Preferences` pointer. Add `wiki-index.md` to the reading list. *(Everything downstream references this.)*
3. **Rewrite both partner SKILLs** against the new contract — activation (cold/warm branch, cold×headless defer, two beats, partner-invoked branch), init (seed two files), closing-a-session (write both files, prune thread), rebirth-is-yours wording. Do them as a pair so the inverted-temperament cold-start opens stay symmetric. *(Use the Agent Builder, plan + this brief as context — but build **directly to the partner contract, not the sanctum**, exactly as v1 did.)* **Checkpoint (finding #8):** the ceremony is the riskiest piece and the contract is internalized into both SKILLs (no isolated test point), so do an **outside read of the reworked ceremony** (see Acceptance) before proceeding to setup/ops.
4. **Update `vlt-setup`** — create `log.md`; seed `identity.md`+`thread.md`; the idempotent legacy-`thread.md`→two-file **migration**; materialize the `vault_structure` map; scaffold/append `## Preferences`; harden the grep.
5. **Update the three ops** — `vlt-ingest` (Step 4 mode-note, Step 7 → `wiki-index.md`, Step 5 research-note branch), `vlt-research` (Phase 1 mode-note, `.WIP` reframe, Phase 6 schema-shaped payload), `vlt-lint` (index-drift → `wiki-index.md`, source-count auto-fix-vs-pinned). *(Workflow Builder; smallest blast radius, last.)*
6. **VM (Validate Module)** — re-run `validate-module.py`; expect 0 findings.

## Acceptance checklist

**The real gate is an OUTSIDE read, not self-assessment (finding #4, HIGH).** The entire rework exists because the partners rated *themselves* glowingly while the owner's outside read said "falls flat" — the inside/outside delta *was* the signal that resolved the fork. So the headline acceptance test is the owner running a **cold-start birth** and a **warm activation** and reporting felt aliveness — not a partner-written verification doc. Do not let the partners grade their own ceremony; that reproduces the exact false positive this build is correcting.

**Regression guard — do not regress the trial's load-bearing wins** (`friction-synthesis.md` "What consistently worked"): supersession discipline still compounds; the activation orient still reads index→log→backlog→thread fast; conventions stay single-source; the single-writer contract still holds under hand-off; the personas stay good to inhabit.

**Per-component pass conditions:**
- [ ] **Gate (finding #1):** a hand-seeded distinctive `## Self` visibly changes activation behavior (proves the ceremony's premise before/with the build).
- [ ] A **fresh-vault first activation** of each partner runs the first-breath ceremony and writes real `identity.md` content — no faked thread, no impossible thread-surfacing open.
- [ ] A **cold + headless** one-shot (e.g. fresh-vault `vlt-ingest`) serves the request, seeds `identity.md` minimally, and **defers** the birth (with a marker) — it does not attempt an interactive ceremony.
- [ ] A **warm activation** runs the light two-beat orient and carries `## Self` drift.
- [ ] **Rebirth two-tier line holds (finding #6):** a partner routes a "how I sound" change to `## Self` (ungated) and a "what I refuse to do / core role" change to a council-gated SKILL.md edit via `vlt-mint` — the line is enacted, not just described.
- [ ] `identity.md` + `thread.md` exist as two files; a dormant `## Thread` entry can be set aside cheaply without touching `identity.md`.
- [ ] A **Researcher→Librarian hand-off** produces **two session notes** (two sittings), a complete **schema-shaped payload** (no field silently dropped), and the Librarian — invoked by a partner — orients to the task without greeting the user; the Researcher does not dictate filing mechanism.
- [ ] A **headless op** sees the `## Preferences` tool pref with no relay; `## Bond` no longer carries tool prefs. *(Confirms the auto-load assumption of finding #5 — if it fails, the op reads `## Preferences` explicitly.)*
- [ ] A **partner-fronted op** skips spent elicitation and states its inferred brief; a **cold/vague** direct invocation still runs the full interview.
- [ ] `vlt-setup` on a fresh vault produces `log.md`, the `vault_structure` map in `config.yaml`, both partner files, and a `## Preferences` heading — and clobbers none of them on re-run; **on an upgrade vault it migrates a legacy single `thread.md` into the two files idempotently**.
- [ ] `vlt-lint` validates the index against `wiki-index.md` and **auto-fixes** a source-count mismatch against the pinned definition (and **flags** rather than mutates when a page's own `sources:` is malformed).
- [ ] **Outside-read gate (finding #4):** the owner confirms felt aliveness on cold-start + warm activation.
- [ ] VM: 0 findings.

## Dynamic workflows (folded from the pressure-test probe)

The Workflow tool (JS orchestration: `agent()`/`parallel()`/`pipeline()`/`phase()`, JSON-Schema structured output, nested `workflow()`) is a strong fit for Vault's **bounded, headless, fan-out** operations — and, given the **single-user / current-Claude-Code assumption** (locked), it can be treated as a real implementation dependency, not a hedged "opportunistic where available" fallback. Two reference docs: this repo's `_output/planning-artifacts/research/technical-claude-code-dynamic-workflows-*.md`.

**The hard line: the interactive partner layer stays conversational.** This is *not* a version concern — workflows trade away mid-run steering ("approve up front, then watch") and carry token-runaway risk, both fatal to the Researcher's "pushed, not served" exploration. Workflows fit the *operations*, never the partner conversation. **So none of this is Build #1** (the partner-identity layer); it's captured here so the brief's scoping is on record and the direction isn't lost.

- **`vlt-lint --full` → a dynamic workflow (owner-prioritized).** Lint balloons as the vault grows — a 60→600-page wiki is exactly the fan-out-over-N case the tool is built for: one agent per page (or per check dimension) via `pipeline()`, schema-validated findings reduced into the already-planned structured report, with `log()` on any coverage cap (no silent truncation) and a `budget` guard so a big sweep can't run away. This is the highest-value op-layer workflow and the natural next op-layer build after Build #1. *(Build #1 keeps only the small `vlt-lint` touches — index-drift pointer + source-count auto-fix; the workflow rebuild is its own pass.)*
- **`vlt-review-council` → a dynamic workflow (Build #2).** The council *is* the research's named **judge-panel / perspective-diverse-verify** pattern: `parallel()` the lenses, each `agent(lens, {schema: VERDICT})`, moderator synthesizes. This directly solves **two-thirds of Gap A**: nested `workflow('vlt-review-council', {proposal, kind})` is the invoke-and-return contract, and schema-forced verdicts *are* the mandatory capture. **Not solved by workflows:** the plugin-cache file-resolution hazard (Gap A's third sub-issue) — workflow agents share it; still needs the explicit "read the live project tree / stage the pending mint" fix.
- **`vlt-research` heavy dives** — already gestured at (the Researcher reaches for `deep-research`, itself a bundled workflow); a deep multi-source dive with adversarial claim-verification is the canonical use case. Op-layer, future.

## Out of scope for Build #1

- **Creative (Design) partner + Extract migration** → after **Build #2** (`vlt-mint`'s partner-ideation beat), so Creative is *born through the mint+ceremony path*, not hand-built. Migrating `vlt-extract` off the Librarian rides with that mint.
- **Build #2** — `vlt-mint` native partner-ideation beat + **Gap A** council mechanics, now with a concrete direction: **rebuild `vlt-review-council` as a dynamic workflow** (invoke-and-return + mandatory verdict capture for free) + the separate plugin-cache-resolution fix.
  - **⚠ Hard prerequisite (known inconsistency left by Build #1):** `vlt-mint/SKILL.md` and `vlt-mint/assets/partner-agent-template.md` still encode the **old four-read / single-file `thread.md` (Bond/Thread/Self)** model. Until they are synced to the reworked contract (two-beat activation, `identity.md`+`thread.md`, sitting/hand-off, rebirth-is-yours), **no partner should be minted** — a mint would produce a contract-violating partner. Sync the template *first* in Build #2, before the Creative mint. (Left out of #1 deliberately: Build #2 rewrites `vlt-mint` wholesale, and nothing mints in between.)
- **Op-layer dynamic-workflow pass** — `vlt-lint --full` as a fan-out workflow (owner-prioritized; see Dynamic workflows), then `vlt-research` heavy dives. Next op-layer build after Build #1.
- **Backlog tail (Themes 6–8, Gap B)** — registration helper / single-source `kind→council` table; setup disambiguation on installer-built vaults; lint observability micro-items (`files_checked` rule, handled-contradiction report slot, `sources:`-vs-prose diff); timestamp-from-clock convention; frontmatter constant-field block. Much already filed in vlt-core's `_agent/backlog.md`.
- **Pulling the vlt-core Creative + Extract-migration diff back into this repo** — the escalation-heuristic instance-level fix; rides with the Creative mint, not #1.

## Handoff

Build #1 is ready. Recommended order: **(0) author `wiki-index.md` → (1) rewrite the contract → (2) rebuild both partners via the Agent Builder (BA) → (3) update `vlt-setup` → (4) update the three ops via the Workflow Builder (BW) → (5) VM.** Pass `vault-module-plan.md` + this brief as context to each builder. Build directly to the partner contract, never the six-file sanctum.
