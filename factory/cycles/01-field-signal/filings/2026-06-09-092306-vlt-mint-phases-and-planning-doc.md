# vlt-mint: explicit Ideate→Validate→Build phases + a resumable planning doc

**Filed:** 2026-06-09 · **Origin:** dog-trainer mint session in `vlt-core` · **Target skill:** `vlt-mint` (with a touch to the operating contract's agent-zone guidance)

## Problem statement + evidence

`vlt-mint` runs a real multi-stage process — ideation (resolve kind + subject, the becoming conversation), the blast-radius/council gate, then authoring + install + record. But the SKILL describes these as a flat sequence of numbered steps, not as **phases with visible boundaries the user can stop between**. Two concrete failures observed in a live gated mint (the Dog Trainer — a new partner + a convention amendment):

1. **No phase boundaries.** The session slid from the ideation beat straight into staging and building with no clean "Phase 1 complete — entering validation" marker. A user who wants to approve the *brief* before any building happens has no natural gate to do so; the skill's own structure doesn't surface one.
2. **No resumable artifact.** The entire live session state — the kind, the partner brief, the four ideation decisions, a mid-session architecture pivot (agent-zone vs PARA, driven by re-reading the write-boundary), the council `revise` verdict, and six applied hardenings — lived **only in conversation context**. Closing the session mid-flow would have lost all of it. `vlt-mint`'s `.decision-log.md` is written *post-hoc* (after the mint completes), so it cannot serve as a resume point.

The user's framing: *"we need clear boundaries between ideation / validation / build phases ... a planning doc would enable me to end a session and resume in a fresh one."*

## Decision + rationale

Introduce **three named phases** in the `vlt-mint` SKILL, each with an explicit exit gate, and a **persistent planning doc** for gated kinds that makes a mint resumable across sessions.

**Phases (rename/regroup the existing steps under these headers; the work is mostly the same, the boundaries are new):**

| Phase | Maps to current steps | Exit gate |
|---|---|---|
| **1 · Ideate** | Step 1 (resolve kind/subject) + the becoming conversation for a partner | User confirms the brief |
| **2 · Validate** | Step 2 / 2a (blast-radius gate + council) + resolve `revise` and any product/timing calls | Verdict resolved (pass or revised-to-pass) + open user-decisions ruled |
| **3 · Build** | Step 3 (author) + Step 4 (install/register/record) | Verified + (offer to) commit |

Why phases over the flat step list: the gates are where a user wants control (approve the brief before building; rule on a council `revise` before going live). Naming the phases makes those decision points first-class instead of emergent.

**Planning doc — scope: gated kinds only.** Write it for `new partner`, `persona self-edit`, and `convention edit` (the council-gated, multi-phase kinds). Keep `operation skill` and `capability migration` ceremony-free (no doc) — they are the cheap in-flow path and rarely span sessions; adding a doc there would tax exactly the case the skill is designed to keep fast. (User chose this scope explicitly over "every mint.")

- **Location:** `_agent/mint/{YYYY-MM-DD}-{slug}.md` — agent zone, resumable and durable. Same contract-sanctioned ad-hoc-owned-folder pattern the contract already blesses (it names `_agent/verification/` as precedent), so **no contract change is required** to legitimize it.
- **Contents:** kind; the brief; architecture decisions + rationale; staged-artifact absolute paths; **current phase + done/pending checklist**; the council verdict (or "not yet run"); open user-decisions with their resolutions.
- **Lifecycle:** created at the start of Phase 1; updated at each phase boundary; on a fresh-session resume, `vlt-mint` reads it (a new activation branch: *"resume an in-flight mint"*) and continues at the live phase. On completion, the post-hoc `.decision-log.md` entry is still written; the planning doc can then be archived or deleted (suggest: leave it, it's cheap, and `git` already has it).

This keeps the existing `.decision-log.md` unchanged in role (post-hoc, permanent record) and adds the planning doc as the orthogonal *live/resumable* artifact.

## Exact changes to ship (module-side)

1. **`vlt-mint` SKILL.md** —
   - Restructure the body under `## Phase 1 — Ideate`, `## Phase 2 — Validate`, `## Phase 3 — Build`, each ending with an explicit **Exit gate** line. Preserve all current step content; this is regrouping + gate-naming, not a rewrite.
   - Add a **planning-doc subsection** under Phase 1 (create the doc) with updates called out at each phase boundary, scoped to the three gated kinds. Specify the `_agent/mint/{date}-{slug}.md` location and the contents list above.
   - Add an **activation branch**: on activation, check `_agent/mint/` for an in-flight planning doc (a gated mint not marked complete) and offer to **resume** it, reading the doc to restore phase state — analogous to how partners read identity/thread to resume.
   - Cross-reference: the planning doc is the *live/resumable* artifact; `.decision-log.md` remains the *post-hoc* record. State the distinction so they aren't conflated.
2. **Operating contract (optional, 1 line)** — the contract already sanctions ad-hoc `_agent/` folders (vlt-verification precedent), so no change is strictly needed. Optionally name `_agent/mint/` as a known working location for symmetry. Low priority.
3. **No convention (`extraction.md` etc.) changes** — this is purely a `vlt-mint` process change.

## Upgrade / migration path for existing installs

- Pure additive skill edit. No data migration: existing installs simply gain phases + the planning-doc behavior on the next `vlt-setup` refresh / skill update.
- No back-compat concern — there are no in-flight mints persisted today (the gap being fixed). The first mint after upgrade just starts producing planning docs.
- `_agent/mint/` is created lazily on first gated mint; `vlt-setup` need not scaffold it (but may, harmlessly).

## Latent bugs / observations surfaced

- **`workflow('vlt-review-council', {...})` arg-passing:** invoking the council via the **named-workflow** form of the Workflow tool (`{name:'vlt-review-council', args:{…}}`) delivered an **empty `args` global** to the script (it errored `received: {mode:null,…}`). The **inline `workflow(name, args)`** form (a thin driver script) passed args correctly. If `vlt-mint`'s Step 2a guidance ever leans on the named-tool form, it should instead use the documented inline call. Worth a note in the council SKILL / mint Step 2a so the next implementer doesn't hit it. (Not necessarily a module bug — could be harness arg-wiring — but the workaround belongs in the docs.)

## Open design questions (module-wide)

1. **Resume UX:** should the resume-offer be automatic on every `vlt-mint` activation (scan `_agent/mint/` for incomplete docs), or only when the user says "resume the mint"? Auto-scan is friendlier but adds an activation read. (Recommendation: auto-scan — it's one `ls`, and the whole point is frictionless resume.)
2. **Completed-doc disposition:** leave the planning doc in place (git-tracked history), or archive to `{archive}` on completion? (Recommendation: leave; it's cheap and the decision-log already summarizes.)
3. **Does this pattern generalize** to other multi-phase ops (e.g. a large `vlt-research` deep-dive, a `vlt-extract` of a big deliverable)? If so, a shared "resumable working doc in `_agent/{op}/`" convention might be worth extracting rather than baking it only into `vlt-mint`. Defer until a second op wants it (n=1 caution).
