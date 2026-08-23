# PARA's single write-path has the wrong shape — the guard is producing falsified provenance, not protection

**Filed:** 2026-08-20
**Source vault:** `app-vault` (shared team dev vault, project-dominant) — evidence only; the defect is base-layer
**Filed by:** owner, via `bmad-cis-problem-solving` session (full analysis: `_output/problem-solution-2026-08-20.md`)
**Kind:** design gap / governance defect
**Severity:** high — a load-bearing invariant is currently breached at scale, silently, in a live vault

---

## The report as filed

> The vlt module's PARA guards are too strict. The only available way for an agent to write into a
> vault's PARA zones is via `vlt-extract`, and `vlt-extract` is limited to wiki → PARA promotion.
> In practice `vlt-extract` is hardly ever used, but blocking the creative from operating within PARA
> has become a significant blocker. This is extremely apparent in `app-vault` — a shared team vault
> where projects are the most significant focus — leading to messy instrumentation and organization.

## Grounding correction (do not capture the filing as written)

One premise is **false**, and the correction makes the defect more serious.

- **`vlt-extract` is not rarely used.** In `app-vault` it is the *most-used* op: **28 of 85** `_agent/log.md`
  entries are `extract` (33%).
- **PARA is not empty of agent work.** `projects/` holds **57 markdown files**, all carrying correct-looking
  extraction frontmatter (`author: hybrid`, `trust: reviewed`, `sources:`).

Agents are not blocked. **They are routing through the one door by falsifying the fields at it.**

| `extraction.md` invariant | Observed in `app-vault` |
|---|---|
| Kebab-case, **no datestamp**, stable identity | `projects/infinity-data-model/2026-08-14-harness-grounding-insights.md`, `pr8-review-2026-08-12.md` |
| `sources:` lists **only wiki pages** — the provenance firewall | `2026-08-14-harness-grounding-insights.md` lists a PARA **sibling** (`../infinity-generalization/2026-08-13-goal-harness-epics-and-stories.md`) and a bare external prose reference (`"sayari-ai docs/harness/epics (branch sy/docs/harness-epics, PR #1304)"`) |
| One synthesized single-file deliverable | Multi-file trees w/ binaries: `canvas/*.excalidraw`, `canvas/*.canvas`, `canvas/screens/*.png`, `presentation/index.html`, `slides/`, `reference/`, `research/` |
| `status:` per type (`project` → `in-progress`) | `status: done` |

Overflow also went **outside** PARA: `_agent/artifacts/{brainstorming,develop,party-mode,planning}/`,
`_agent/repos/`, plus top-level `publish/` and `users/` that sit outside the layer model entirely —
the contract's "ad-hoc owned artifacts under `_agent/`" allowance acting as an unmetered relief valve.

**The real cost is not blocked work.** It is that `sources:` no longer certifies wiki provenance on
57 files in a live vault. The guard converted a cheap, visible write-boundary breach into an expensive,
silent **provenance** breach — the one invariant `extraction.md` calls the trustworthiness firewall.

## Sites that carry the rule (four, all agreeing)

- `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` — *The three layers and the hard write boundaries*
- `skills/vlt-setup/assets/governance/_meta/conventions/extraction.md` — *What extraction is*; *Personalized extraction* ("This does not open a second PARA write-path")
- `skills/vlt-agent-creative/SKILL.md` — *Your non-negotiable*
- `skills/vlt-extract/SKILL.md` — Overview ("reaches the wiki **only**")

Because the rule is identity-bearing, partners recite it accurately while violating a deeper invariant
to get work done. Internalization bought compliance theater, not compliance.

## Root cause

**Primary:** the module encodes **one vault posture** — wiki-centric, single-owner, PARA-as-output-shelf —
as a **hard universal invariant** rather than a **declared, configurable posture**. The vault class has
widened; in a shared dev vault the work product *is* the project and the wiki is a support layer.

**Secondary (equally load-bearing):** the module has **exactly one PARA verb**, which fuses *write
permission* to *wiki-provenance discipline*. You cannot take the first without the second, so work
needing the first paid by faking the second.

## Owner rulings taken at filing time (2026-08-20)

1. `projects/` **wants to be a shared agent+human workspace** — this is a re-draw of Layer 3, not a wider door.
2. **Do not solve for `app-vault`** — it is evidence, not scope.
3. **General module change**, base layer, all vault instances.

## Proposed resolution — "Two verbs, one boundary, drawn by authorship"

- **C1** — Contract re-draws Layer 3 by **authorship, not location**: a partner never modifies an artifact
  it did not author (`author: human`, or `trust: verified|canonical`), never edits MOCs, never raises
  `trust:`, never restructures a human taxonomy. It **may** create and maintain its own PARA artifacts.
- **C2** — **Per-zone `para_posture`** as a *designed parameter read* (`curated` | `workspace`).
  Proposed shipped defaults: `projects: workspace`, `areas: curated`, `resources: curated`.
  ⚠️ A real default change for every vault — needs an explicit owner ruling at ideation.
- **C3** — Second verb **`vlt-file`** for agent-authored work product. Single home for the folder-artifact
  model, the `working | settled` lifecycle, and dated-vs-stable naming. Restates no extraction mechanics.
  (`vlt-deliver` is unavailable — `deliver` is a `vlt-dispatch` relay kind, contract:262.)
- **C4** — **Provenance segregation**, applying the *Personalized extraction* template verbatim:
  `sources:` stays **wiki-only forever, on every artifact**; new `grounding:` field carries external
  evidence (repos, PRs, live systems, sibling artifacts). A method claim supported only by `grounding:`
  is a violation. **This is the component that repairs the firewall.**
- **C5** — **Enforcement ships in the same build:** `vlt-lint` gains (i) non-wiki entry in `sources:`,
  (ii) agent-authored artifact in a `curated` zone, (iii) `settled` artifact with a dated filename,
  (iv) partner modification of a human-authored/endorsement-grade artifact; plus a MOC-edit tripwire
  and a `capability-gap` backlog signal on legitimate refusal.

**Framing for the roundtable: this is a repair, not a relaxation.** The firewall is already breached;
C4 is how it comes back, and how it becomes mechanically checkable for the first time.

## Two hard constraints (from reverse-brainstorm — both are tempting failure modes)

- **Do not** ship the widening without the lint family. A sanctioned-and-invisible breach is worse than the current one.
- **Do not** take the lazy path of relaxing `vlt-extract`'s `sources:` rule. It scores *below status quo*
  on the criterion that matters most — it destroys the firewall to solve an unrelated permission problem.
  **`extraction.md`'s invariants must not be touched; `vlt-extract`'s behavior must not change.**

## Expected blast radius (joint-heavy — roundtable should not be waived)

`extraction@3 → @4` (one sentence) + re-ack `vlt-extract` / `vlt-lint` / `vlt-track`;
`frontmatter@8 → @9` (`grounding:`, `lifecycle:`, `owner:`); new `filing.md` convention;
contract + rule-card; three partner SKILL non-negotiable recasts; new `vlt-file` skill;
`vlt-lint` check family; `vlt-setup` posture seeding; `vlt-upgrade` one-time PARA provenance **report**
(never an auto-rewrite).

## Open questions for ideation

1. Is the `projects: workspace` **default** (vs. opt-in) the owner's call? — flagged, not assumed.
2. Does `areas/` behave like `resources/` (curation) or like `projects/` (workspace)? Field evidence is
   thin — `app-vault`'s `areas/` is empty. One-line default, revisable.
3. Verb name: `vlt-file` vs. alternatives (`vlt-produce`, `vlt-make`). `vlt-deliver` is taken.
4. Does `lifecycle:` become a new frontmatter field, or reuse/extend `status:`?
5. Disposition of `app-vault`'s existing 57 files — report-only, per ruling 2, but the disposition still needs ruling.

## Watch item

`grounding:` is a candidate laundering channel for method claims — the same failure `extraction.md`
already anticipates for `personalization_sources:`. If lint shows method claims landing there, the
self-defeating loop has restarted in a new field.

---

# Roundtable amendments — 2026-08-20 (party-mode, installed roster)

The room reviewed this filing's open questions and edge cases to consensus. **Four owner rulings
landed mid-session and the diagnosis above is superseded in part.** Read this section as authoritative
where it conflicts with the body.

## Owner rulings (2026-08-20, in session)

- **R-a — No friction at write time.** The proposed write-time triage gate is rejected.
- **R-b — Project knowledge does not belong in the wiki.** It changes often and is often duplicative.
  The module should **highlight these characteristics, not move agents away from them.**
- **R-c — Projects have a start and an end; areas are ongoing.**
- **R-d — `resources/` is retired: wiki === resources. The wiki moves out of `_agent/`.**

## Consensus items

**K1 — The module already has a second PARA door, in lint, and governance won't name it.**
`skills/vlt-lint/references/checks.md:16` ships `para_missing_attestation` — *"a PARA file carrying
vault `type:` + `author: agent|hybrid` with no attestation (the out-of-path-write net — a real finding
from day one)."* The contract insists this cannot happen; lint has caught it since day one.
**0 of 56** `app-vault` PARA files are attested. Full lint has run. The finding read as a census.

**K1b — That finding has no lawful remedy.** Its legal response is *"the owning writer re-runs its
verify pass and attests."* `write-verification.md:47` admits only **three** ops in the `verified_by`
set; an out-of-path writer can be none of them. A rule with no lawful obedience degrades to wallpaper.

**K2 (REVISED — supersedes the body's C3 gate) — File freely; harvest later.** Separation in **time**,
not permission. The wiki-feeding question moves downstream to an approval-gated pass on Arc 8's
`vlt-groom`/`vlt-decay`, triggered by **project close** — never by a human remembering.

**K3/K6 — Bounded vs unbounded is the real PARA axis, and it resolves three symptoms at once.**
Projects are bounded; areas are unbounded; `resources/` is unbounded reference with no lifecycle —
which **is the wiki**. Evidence: `resources/` holds exactly **1 file in three structurally dissimilar
vaults** (vlt-core 30/20/1 · vlt-sayari 210/6/1 · app-vault 56/0/1). Single-home discipline had already
executed one of the two homes; the module never noticed.
· **Ideation is an area** — unbounded until it earns a start date. "No home for ideation" and "areas
  unused" were **one fact**, not two symptoms.
· A project is **born from** an area, closes back into it.
· **Retention derives from the axis for free:** bounded ⇒ decayable at close (Arc 8 machinery, already
  shipped); unbounded ⇒ never decays.

**K4 — vlt ships PARA folders but no PARA model, and the field proves it mechanically.**
A project is a `type:` string, not an object. Across three vaults: **195 of 296 project files carry no
`status:` at all** (vlt-core: 30/30 absent), and those that do have forked into **8 vocabularies**
(`in-progress`, `draft`, `complete`, `drafted`, `open`, `final`, `proposed`, `stable`, `done`) with zero
convergence. Cause: `status:` is on the **artifact**, not the project — `app-vault` has 56 files and
**2 projects**. One `status:` field in `app-vault` contains an entire changelog with commit SHAs
(the Arc-7 "nowhere to put it" signature, one layer down).

**K7 — The harvest trigger must fire on the container's close.** The originally-agreed
"artifact `status:` flips to done" fires on an event the field has emitted ~never.

**K8 — The module's move is observation, not enforcement.** A bounded thing that never ends **is** an
area — mechanically detectable, surfaced later as an offer, never as a block. This is the literal
reading of R-b. (`vlt-sayari` has 210 candidate instances.)

**K9 — Never illustrate a vocabulary with an inline `# a | b` comment.** It ships into live data as a
value: `vlt-sayari` has an areas file whose `status:` reads `digested   # digested | draft`.

**K10 — The project container already exists in the field, hand-rolled.**
`projects/<slug>/index.md` in both `app-vault` projects: `type: project`, **container-level `status:`**,
33K and 10K. It carries four objects vlt models none of: a **charter** (thesis, attribution, MVP),
a **bidirectional cross-project dependency table**, a **decision / open-questions register** (Q-numbered,
in a separate 36K worksheet), and a **workplan**.

**K11 — The body's headline "falsified `sources:`" was a missing edge type, not a lie.** Projects
genuinely depend on projects (documented bidirectionally in the index above). Wiki-only provenance was
the only field available. **The fix is a project-to-project relation**, and it exonerates the field.
*The body's framing of that violation is hereby corrected.*

**K12 — OUT OF SCOPE (owner ruling, 2026-08-20).** The room raised the multi-user trust model:
`raw→reviewed→verified→canonical` and `author: human` both assume a single curator, and `app-vault` has
grown `_agent/OWNERS`, `users.yaml`, `users/` locally to cope. **Owner ruled this a vault-side question
for the `app-vault` users, not a base-layer module concern** — it does not enter Arc 9 capture, and no
build owes it. Recorded here so the observation is on file and does not get re-discovered as a defect.
Durability still applies by construction: those files live in the agent zone, so they survive upgrades
whatever `app-vault` decides.

**K13 — Build one is a HARVEST, not a design.** Three vaults each hand-built vlt's missing half,
**differently**. The cost is not mess (recoverable) but **N incompatible private schemas accreting in
production**. Read the model out of `app-vault`'s two index files and `vlt-sayari`'s 210 before writing
any contract text.

**K14 — Retiring `resources/` and moving the wiki out of `_agent/` are ONE operation** (per R-d):
the wiki **moves into `resources/`**. Mechanically this is a single `vault_structure` entry
(`wiki: _agent/wiki/` → `resources/`) — the designed-parameter machinery was built for exactly this.
`[[wikilinks]]` are path-independent, so the link layer survives the move.

**K15 — K14 is the final proof that the write boundary cannot be location-based.** After the move, the
module's **most-written layer sits outside `_agent/`**. The layer model stops being *human vs agent* and
becomes **content vs machinery**: everything a human cares about is visible (PARA + wiki), and `_agent/`
holds only operational machinery (log, sessions, partners, dispatch, specs). That boundary needs no
policing because it is self-evident.

**K16 (watch) — Every time content crosses the agent/human boundary, an attestation check becomes a
census.** Seen twice already (`para_missing_attestation` at 56/56). Moving the wiki into human-browsable
space makes human edits to wiki pages routine, which will mass-produce `attestation_stale`. Third
instance is predictable; design for it now.

## Resolved / moot open questions

| Body question | Disposition |
|---|---|
| `projects: workspace` default vs opt-in | **Moot** — posture was the wrong axis; bounded/unbounded is the axis |
| `areas/` posture | **Resolved** — areas are real, unbounded, and are the **ideation home** |
| Verb name (`vlt-file` etc.) | **Moot** — the write-time gate was withdrawn (R-a); name follows the harvested model |
| `lifecycle:` new field vs reuse `status:` | **Resolved** — lifecycle lives on the **container**, not per artifact |
| Disposition of the 56 files | **Moot** — they were never violations in the sense the body claimed (K11) |
| `resources/` | **Ruled** — retired by inhabitation; the wiki moves into it (R-d, K14) |
