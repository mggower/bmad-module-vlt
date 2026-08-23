---
title: 'Spike S1 — the PARA container harvest (A9-1, K13)'
status: 'SPIKE CLOSED 2026-08-21 — model harvested from app-vault (2 indexes read whole) + vlt-sayari (210-file survey); read-only, nothing written to either vault'
arc: 'Arc 10'
sources:
  - '~/Vaults/app-vault/projects/infinity-data-model/index.md (34.8K) + open-questions-worksheet.md (36.7K, structure) + infinity-generalization/index.md (10.6K)'
  - '~/Vaults/vlt-sayari — full projects/ (304 files, 210 md), areas/, resources/, _agent/projects/ survey'
---

# Spike S1 — the PARA container harvest

K13's instruction: read the model out of the field **before writing any contract text**.
Done. Below is the model the field actually built — twice, differently — and what each
divergence teaches.

## The headline: two vaults, two architectures, one thesis proven twice

- **app-vault** put the container **inside PARA**: `projects/<slug>/index.md`,
  `type: project`, `author: hybrid`, **container-level `status:`**, `trust: reviewed`,
  `sources:` pointing at wiki pages. The write-path rule was simply ignored in favor of
  honest `author: hybrid` stamping.
- **vlt-sayari** obeyed the write-path rule — and the container **fled to the agent
  zone**: a shadow tree `_agent/projects/<name>/{charter.md, status.md}` (10 charters,
  15 status files, 59 files, nested sub-containers), while `projects/` itself holds NO
  per-dir index at all. PARA files then cite the shadow container via
  `personalization_sources:` — the source of truth points *out* of PARA into `_agent/`.

A9-1's thesis (Layer 3's boundary drawn by location where it should be drawn by
authorship) is field-proven in **both directions**: one vault broke the location rule to
get an honest container; the other kept the rule and got a container the human-browsable
layer can't see. Same missing object, two incompatible private schemas — exactly the
accretion K13 predicted.

## The convergent container model (what both vaults built independently)

1. **A container object with its own identity and status**, distinct from artifact
   status. app-vault: frontmatter on `index.md`. vlt-sayari: charter frontmatter
   (`status: ongoing` — a vocabulary used nowhere else in the vault).
2. **Charter — the stable frame.** vlt-sayari states the doctrine in-file: Outcome,
   Scope, Owners, Definition of done, filing rule, re-sync protocol. app-vault's
   equivalent: thesis with attribution + date, MVP as a blockquote, proof stories.
3. **Running record — dated, append-shaped.** vlt-sayari: `status.md` of `## [date]`
   entries. app-vault: dated goal files superseded in place + the state-of-play section.
4. **A decision / open-questions register.** app-vault: the 36.7K worksheet —
   `question · evidence · options · decider · pick`, three tiers, a verification queue
   (V1–V5, "go-look items"), an assignments queue (A1–A5, unowned-since dates); Q-numbers
   cited from everywhere (`worksheet Q24`). vlt-sayari: a decision-register *document*
   (`purpose: Classify all 37 units … record where two sources of truth disagree`) plus
   an invented `canonical_rule:` precedence field (4 files).
5. **An evidence ledger — numbered rows with source links.** app-vault: the
   wild-instances ledger (W1–W6: instance · where · gap-it-hits), with a **standing feed
   convention** (repo stories relay findings back as `Data-model:` lines). vlt-sayari:
   `### N98..N103` numbered findings in `status.md`.
6. **Cross-project relations.** app-vault: a **bidirectional dependency table**
   ("From there → here | From here → there") plus a "sprinkles" table (cheap items that
   ride the sibling project's PRs). vlt-sayari: prose **portfolio hierarchy** ("umbrella"
   / "sub-umbrella", 23 files), `project: <slug>` membership strings, and a nascent
   low-frequency vocabulary: `related:` (11), `owner` (10), `grounds` (7), `supersedes`
   (4), `depends_on` (3), `blocks` (2), `requires` (2). K11's missing
   project-to-project edge: confirmed, hand-rolled in both vaults.
7. **A doc catalog with per-doc status and supersession tracking.** app-vault tracks
   "superseded-but-still-authoritative-looking" docs as named **propagation debt**.

## The defects, quantified (vlt-sayari, 210 md under projects/)

- **142/210 no frontmatter at all; 143/210 no `status:`**. Of the 67 with status: **25
  distinct values**, ≥8 vocabularies in this one vault (module-ish, BMad `drafted`,
  `open/active/proposed`, `ongoing`, `digested|draft`, `verified-against-develop`,
  free-prose phase strings, BMad workflow-state) — plus changelogs literally stuffed
  into `status:` ("Phase 3, first batch. Six units dissected…"). K4 confirmed with a
  sharper number than the filing's.
- **Bounded things that never close (K8):** ~12/210 terminal; 17 of the 25 `in-progress`
  files ≥4 weeks stale; `_archive/` used 3 times ever. The honest reading of "210
  candidate instances": 210 files of which 55 explicitly open + 143 status-less.
- **K9's enum-in-comment** found at its origin: a *template*
  (`areas/graph-ai/alpha/_session-digest-template.md:11`, `status: digested # digested |
  draft`) defining a bespoke per-type status vocabulary with nowhere schema-shaped to
  declare it — the same defect as the module's own `capability-template.md:23`.
- **`resources/` holds 1 file in both vaults** (K3/K6 confirmed: the wiki *is* the
  unbounded reference layer). Note: **app-vault has zero areas** (56/0/1) while
  vlt-sayari has 8 area files — "areas unused" is not universal; it tracks whether the
  vault has unbounded ongoing concerns or only bounded exercises.
- **Verification lifecycle forked:** vlt-sayari hand-rolled `trust: raw/reviewed` (37
  files) + `status: living — re-stamp whenever…` while the module's `verified_by:`
  appears on exactly **1 of 210** files.
- **A visibility boundary the module has no field for:** charters declare "agent-zone
  only, no PARA extraction, no shared brief" — confidentiality as a container attribute,
  enforced today by keeping whole containers out of PARA.
- **Lifecycle transitions exist only as prose:** project→area reclassification and
  umbrella succession are recorded in charter narrative ("On 2026-07-10 Mikey reframed…
  Project California is now an **area**") — no field, no event.

## What this shapes for the contract (harvest → ideation inputs, not rulings)

1. **The container is 2–3 files, not one index.** app-vault's single 33K index is
   splitting under its own weight (the worksheet spun out at 36.7K); vlt-sayari split
   charter/status from birth. Stable frame + running record (+ register) is the shape
   the field converged on.
2. **Container `status:` needs its own small enum** (the field invented `ongoing`;
   bounded/unbounded suggests something like `open/paused/closed` for projects), and
   per-type artifact status must become a real enumeration — K4's unstated second half,
   now with 25-value evidence.
3. **Nesting is real.** Sub-projects (generative-ui's 5 slices, 2–3 levels deep) and
   portfolio umbrellas exist in both vaults; the bounded/unbounded model needs a
   containment answer, not just a leaf-project answer.
4. **The relations to model:** membership (file→container), dependency (bidirectional,
   project↔project), supersession, containment (umbrella). All four are hand-rolled in
   the field today.
5. **K7 confirmed at scale:** close-events fire ~never (12/210). A harvest trigger on
   container close only works if closing is cheap and the container is real.
6. **New objects the filing didn't name, now candidates:** the decider·pick question
   register (with verification + assignment queues), the numbered evidence ledger with a
   standing feed convention, propagation-debt tracking, and the
   confidentiality-as-container-attribute boundary.
7. **The Q6 posture question has field data now:** both vaults built project containers;
   neither has a `workspace` concept. And the Q7 wiki-into-resources move matches the
   field exactly (resources/ is already vestigial in both).

**Bound honored:** read-only on both vaults; this report is factory-side
(`skills/reports/`, gitignored) and no contract text was drafted.
