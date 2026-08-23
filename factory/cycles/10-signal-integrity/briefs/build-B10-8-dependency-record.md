---
title: 'Build #B10-8 — the dependency record (a vault ports but its toolchain doesn''t:
  the module declares the machine tools its shipped skills assume, capabilities record
  theirs at birth, and setup/upgrade probe the declared set at arrival — report, never
  gate)'
status: 'BUILT 2026-08-22 — all five F-sites landed on arc10-v0.14.0 per the brief.
  Verification at rest: module.yaml YAML-parses with the four-row machine_tools: list
  (tool/needed_by/absent each row); fixture merge-config.py run proves inertness (no
  machine_tools in config.yaml vlt: section, module_keys = metadata + vault_structure +
  feedback_repo only, nothing removed); four-way agreement greps pass (requires: =
  template both blocks + rule paragraph, mint both Step-3 bullets, setup probe walk,
  upgrade census/schema; bare machine_tools: = module.yaml + setup probe only;
  machine_tools_missing = upgrade schema + Notes only; dependency-census = bullet +
  enum; tool-missing = setup only); package-lint A/B/C/E PASS (D skipped, no
  --expect-version — mid-arc, no version bump). Acceptance check 1 discharged at rest.
  Deviations: (1) F2''s rule paragraph landed as a bold-led plain paragraph rather than
  the brief''s blockquote rendering — content verbatim in substance, formatting matches
  the template''s surrounding prose style. (2) F1''s needed_by:/absent: values are all
  double-quoted (the brief''s sketch quoted only some) — always-quote is the safer YAML
  posture and the parse verifies the shape unchanged. No other deviations; no
  .decision-log.md cruft.'
module_code: 'vlt'
created: '2026-08-22'
derives_from:
  - 'inbox/2026-08-21-150800-vault-capabilities-install-tools-with-no-dependency-record.md
    (A10-9 whole — the two-layer gap: module-level deps undeclared, vault-grown deps
    unrecorded, arrival unchecked; the gh-missing pattern its one ad-hoc instance)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-8 grouping bullet (binds: D6);
  D6 — BOTH halves: declare-at-birth (module.yaml declares module-level deps; the
  mint/capability ceremony records vault-grown deps at birth; one retroactive census) plus
  check-at-arrival (vlt-setup/vlt-upgrade probe and report, never gate, generalizing
  vlt-feedback''s gh-missing named-error + degrade pattern). Stands alone as a build.'
risk: 'low — no convention version: moves anywhere (capability-template.md is a skill
  asset, module.yaml is unhandshaked, SKILL.md edits are unhandshaked), no contract edit
  (no C6 rule-card re-derive), no new package-lint check (no E4 fixture debt), no new
  persisted surface (the arrival result rides the existing Step-4 report). The one
  cross-file agreement to hold is a four-way name/shape match: template field = mint
  ceremony text = setup probe = upgrade schema key.'
---

# Build #B10-8 — the dependency record

A vault is designed to be durable and portable — git-carried, upgrade-safe, agent-zone
preserved — but nothing records what the *machine* must provide. Shipped skills assume
`gh`, `uv`, `python3` with zero declarations in `module.yaml` (re-verified: zero
dependency keys of any kind on the current branch), vault-grown capabilities install or
assume tools with no record anywhere durable, and the one shipped instance of a
dependency being checked-and-reported is `vlt-feedback`'s ad-hoc `gh-missing`
(`skills/vlt-feedback/SKILL.md:90`, degrade choreography `:107`). The failure mode is
deferred and silent: everything works where the capability was born; on a fresh machine
it fails at exercise time with no declared expectation to check against (A9-4's
multi-machine theme — vaults provably move across machines faster than their toolchains).

This build ships D6's ruling whole, both halves complementary by construction — **the
declaration is the record the check reads**:

- **Declare** — `module.yaml` gains a `machine_tools:` declaration (module level);
  capability frontmatter gains an optional `requires:` field recorded at birth by the
  mint/capability ceremony (vault-grown level, the durable-host doctrine's population —
  a declared home, not prose); one retroactive census covers what's already born.
- **Check** — `vlt-setup`'s existing `## Check Dependencies` section (already
  warn-never-hard-fail for skill-level deps) gains the machine-tool probe over both
  layers; `vlt-upgrade` reaches it through its Step-3.6 provisioning hand-off and its
  Step-4 report carries the result as a new never-omit key. **Report, never gate** — the
  vault must stay usable degraded.

All rejected alternatives in the parent filing are settled — do not re-litigate. In
particular D6 already ruled *both* halves (not check-only, not declare-only) and ruled
the build stands alone (not folded into A10-6/B10-1).

## Brief-time dispositions

*(Autonomous run 2026-08-22, clerk-resolved, owner review pending — D6 ruled the shape;
these resolve only what it deliberately left open: the exact declared set, the record's
home and YAML shape, the census posture, and the report surfaces.)*

1. **The module-level declared set is `gh`, `uv`, `python3`, `git` — D6's named pair plus
   two grounding additions.** D6 names "(`gh`, `uv`)"; a fresh sweep of shipped skills
   for tool invocations (grounding addition, in scope beyond the ruling's letter because
   the ruling's *rule* is "module.yaml declares module-level dependencies", not "declares
   exactly two") finds two more shipped assumptions: **`python3`** — the enforcement
   kit's SessionStart hook runs `python3 ".claude/hooks/vlt-vitals.py" --strip`
   (`vlt-setup/SKILL.md:190`) with a stated degrade at `:193` ("a machine without
   `python3` degrades to the hook printing only its own error line — loud, never
   silent-green"); and **`git`** — the vault's own durability premise (the groom safety
   model's `git show <ref>:<path>` resolution test, `vlt-groom/references/groom-pass.md:9`;
   the upgrade's worktree discipline, `vlt-upgrade/SKILL.md:75`; the mint planning doc's
   "git has it"). `uv` grounds at `vlt-setup/SKILL.md:82` (PEP 723 scripts; "bare
   `python3` … exits with `Error: pyyaml is required`") with invocations at `:90`, `:96`,
   `:156` and `vlt-upgrade/SKILL.md:58`; `gh` at `vlt-feedback/SKILL.md:90-99`. Four
   rows, each carrying who needs it and what absence degrades to.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

2. **The declaration's YAML shape is a plain top-level list — deliberately inert to
   merge-config.** `merge-config.py` treats a top-level `module.yaml` key as a *defined
   variable* iff its value is a dict carrying a declaration marker
   (`prompt`/`default`/`result`/`user_setting` — `merge-config.py:203-216`, the B7-2
   declaration read), and as metadata only if named in its fixed metadata set (`:199-201`,
   `:219-228`). A key whose value is a **list** is neither — ignored entirely, never
   exported to `config.yaml`, never prompted. So `machine_tools:` is a list of flat
   mappings (`tool:` / `needed_by:` / `absent:`) and the probe reads it **directly from
   `./assets/module.yaml`** (which `vlt-setup` already reads on activation, `SKILL.md:30`)
   — no config round-trip, no per-vault override (module-level facts are module-owned).
   The block's comment states this inertness and carries the **same-act writer clause**
   (the B10-5 discipline, mitigating the lists-claim-completeness drift risk): a module
   build that adds a shipped tool assumption adds its row in the same build. Report-not-
   gate makes staleness safe-degrading: an undeclared tool fails exactly as it does
   today, never worse.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

3. **The vault-grown record's single home is the capability file's own frontmatter — no
   central manifest.** The filing offered "capability frontmatter, or a vault-level
   dependency file in the agent zone". Ruled: **frontmatter**. A central vault-level
   manifest is a completeness-claiming list that drifts (CLAUDE.md standing rule) and a
   second home for a fact the capability already owns; frontmatter travels with the
   capability, retires with it (the groom re-marker precedent), is upgrade-durable by
   location (partner zone — the durable-host doctrine satisfied by construction,
   contract `:96-98`), and the probe *derives* the population by walking
   `{partners}/*/capabilities/*.md` — point-at-the-map, not a second enumeration. The
   capability schema's single home is `vlt-mint/assets/capability-template.md` (the
   contract delegates exactly this at `vault-operating-contract.md:242` — "the full
   schema + templates live in `vlt-mint/assets/capability-template.md`"), and
   capability files are **not** `frontmatter.md`'s population (verified: no capability
   schema there; its note-type schemas don't cover partner-zone capability objects) — so
   the field lands in the template with **no convention `version:` bump and no consumer
   walk**.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

4. **`requires:` is a flat list of strings; explicit `requires: []` is the censused-none
   marker.** Form: `requires: [gh, "pandoc (brew install pandoc)"]` — tool name,
   optionally followed by a parenthesized install hint; flat scalars only (the vault's
   YAML flatness posture; no per-tool maps). Present whenever the capability installs
   *or assumes* a machine-level tool, including the interpreter/deps of a
   `capabilities/scripts/` sibling (`capability-template.md:33`). **Absent key** = born
   before this record or never considered (the census's population test); **`[]`** =
   considered, needs nothing (the idempotency marker that keeps the census from
   re-asking). Both weights carry it — a heavy capability's pointer file records what
   its vault-grown op skill assumes (shipped op skills are the module layer's problem,
   disposition 1).

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

5. **The census is a human-gated offer in the upgrade's migration slot, never an
   auto-write.** Inferring tool assumptions from capability prose is unreliable, and
   every sibling migration in `vlt-upgrade` Step 3.5 (`SKILL.md:77-81`) is
   surface-and-offer. The census walks vault-grown capabilities **lacking any
   `requires:` key**, surfaces each with its body and `scripts/` sibling plus the
   clerk's inferred entries, and writes `requires:` (or explicit `[]`) only on the
   owner's confirmation. `dependency-census` joins the `migrations_run` enum. Idempotent
   by the key's presence — a censused capability is skipped forever.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

6. **The probe is single-homed in `vlt-setup`'s Check Dependencies; the upgrade consumes
   it via the Step-3.6 hand-off; the result surfaces per B10-6's census postures.**
   Setup's end-of-run Confirm is census-recorded **report-and-discard by design**
   (B10-6 §E2) — the probe's lines join the existing Dependencies bullet there. The
   upgrade path *persists* the result: Step 3.6 (`vlt-upgrade/SKILL.md:84`) already
   invokes `vlt-setup` on every upgrade, so Step 4 renders a new schema key
   **`machine_tools_missing:`** — never omitted when empty (`[]` = every declared tool
   present, an honest arrival record), rendered from the hand-off's probe result — and
   the existing persist + key-set verify (`SKILL.md:120-122`) covers it with no further
   mechanism. **No new persisted surface is born** (the key rides the already-censused
   Step-4 report, B10-6's E2), so no Decay-contracts row, no zone-map row, no Q3a
   ceremony — recorded here as the reason B10-8 stays out of E2's census population.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

7. **Named-line discipline, generalized from `gh-missing`.** Each missing tool reports
   one named line — `tool-missing: <tool>` — carrying the declaration's `needed_by:` and
   `absent:` text (module layer) or the owning `partner/slug` (vault-grown layer) plus
   any install hint. Probe mechanics: `command -v <tool>` on PATH — presence only, never
   versions (out of scope, §6). `vlt-feedback`'s own pre-flight is **untouched**: it
   probes at *exercise* time (the moment that matters for transport), the arrival probe
   at *install* time; complementary moments, no overlap to eliminate.

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

**R1 — interim posture (substantive).** Declare-at-birth reaches a live vault's
*existing* capabilities only at its first post-upgrade census, and the census is
human-gated — so in the window between this release and an accepted census (and forever
for a declined one), the probe covers the module layer fully and the vault-grown layer
only where `requires:` exists. Legal interim state: an unrecorded vault-grown dependency
degrades exactly as it does today — fails at exercise time, undeclared. The probe never
guesses at undeclared tools; the census offer re-fires on every upgrade until the keys
exist (idempotency skips only censused capabilities, not the offer itself).

> ✅ **OWNER-RULED 2026-08-23 — CONFIRMED under the batch disposition** (owner-filtered review: four calls taken live, the remainder confirmed as one dated batch; see the roadmap's *Owner review of clerk dispositions — 2026-08-23* record. Reversible at arc close.)

## F-sites

### F1 — `skills/vlt-setup/assets/module.yaml` — the module-level declaration

**Current state:** no dependency key of any kind (re-verified on `arc10-v0.14.0`: the
file is metadata + `agents:` + two defined variables, `vault_structure:` at `:39` and
`feedback_repo:` at `:64`). **Change:** append a commented `machine_tools:` block after
`feedback_repo:`:

```yaml
# --- Machine-tool dependencies (module level) ---
# The machine-level tools shipped skills assume. Read directly from this file by
# vlt-setup's Check Dependencies probe (report, never gate). NOT a defined variable
# (no prompt:/default: markers) and not metadata — merge-config.py ignores a list-valued
# key by its declaration read (B7-2), so this never reaches config.yaml and is never
# prompted. Writer clause (same-act): a module build that adds a shipped tool assumption
# adds its row here in the same build.
machine_tools:
  - tool: gh
    needed_by: vlt-feedback (issue transport pre-flight)
    absent: "degrades to the paste-ready outbox failure path (named error gh-missing)"
  - tool: uv
    needed_by: vlt-setup / vlt-upgrade merge + manifest scripts (PEP 723 inline deps)
    absent: "config/help/manifest merges cannot run — install uv before setup or upgrade"
  - tool: python3
    needed_by: the vlt-vitals SessionStart hook (enforcement kit)
    absent: "hook prints only its own error line — loud, never silent-green"
  - tool: git
    needed_by: "the vault itself (groom safety model, upgrade ledger refs, worktrees)"
    absent: "the durability premise fails — effectively required for a vault"
```

Exact `needed_by:`/`absent:` wording is the builder's within these facts (grounded at
`vlt-feedback/SKILL.md:90/:107`, `vlt-setup/SKILL.md:82/:190/:193`,
`vlt-groom/references/groom-pass.md:9`, `vlt-upgrade/SKILL.md:75`). **Why:** D6's
declare half, module layer; dispositions 1–2. **Out of scope here:** no `version:`-range
or minimum-version fields — presence-only (disposition 7).

### F2 — `skills/vlt-mint/assets/capability-template.md` — the birth-record field

**Current state:** the light schema block (`:14-31`) has no dependency field; the heavy
pointer block (`:37-51`) likewise; `:33` names the `capabilities/scripts/<tool>` sibling
with no record of what runs it. **Change:** (a) add one optional line to the **light**
schema block after `family:` —
`requires: []                       # OPTIONAL — machine-level tools this capability installs/assumes; flat strings, hint in parens; [] = censused, needs none`
— and the same line to the **heavy** pointer block; (b) add a short rule paragraph after
the `:33` scripts-sibling paragraph, the field's single home:

> **`requires:` — the machine-tool birth record.** A capability that installs or assumes
> a machine-level tool (a CLI, a parser, a converter — including whatever runs its
> `scripts/` sibling) records it in `requires:` **at birth**: a flat list of tool-name
> strings, an install hint in parentheses where useful. `requires: []` states the
> considered answer "needs nothing" (and is what the upgrade's dependency census writes
> on a no-deps ruling — an absent key means *unconsidered*, not *none*). **Same-act
> writer clause:** an exercise that installs a new tool appends it to the owning
> capability's `requires:` in the same act. `vlt-setup`'s Check Dependencies probe reads
> the field at arrival and reports (never gates) missing tools — this record is what
> makes a vault's toolchain portable alongside the vault.

**Why:** D6's declare half, vault-grown layer; dispositions 3–4. No handshake: the
template is a skill asset, not a versioned convention, and capability frontmatter is not
`frontmatter.md`'s population (disposition 3 grounding).

### F3 — `skills/vlt-mint/SKILL.md` — the ceremony records at birth

**Current state:** Step 3 "Add a capability" (`:119-122`) instantiates the template with
no dependency mention; the self-grow shortcut (`:121`) logs one decision-log line; Step
3's light path and `:161` (light registers nothing) stand. **Change:** one sentence in
the light bullet (`:121`) and one in the heavy bullet (`:122`), pointing at the
template's rule, never restating it — e.g. (light): "Fill `requires:` at birth when the
capability installs/assumes a machine-level tool — the birth record; schema + rule in
`assets/capability-template.md`. Self-grown capabilities carry it the same way (the
decision-log one-liner is unchanged)." and (heavy): "The pointer file records the op's
machine-tool assumptions in `requires:` per the template." **Why:** D6's "the
mint/capability ceremony records vault-grown tool dependencies at their birth moment" —
the ceremony text is what makes the field a *ritual*, not documentation. **Out of scope:**
the boundary classifier (`:42`) is untouched — a `requires:` entry is a fact record, not
a rule someone else must obey; `_agent/mint/decision-log.md` mechanics untouched
(`{conventions}/decision-log.md` is Arc 11's, per the addendum ruling on A10-12/13 —
the B10-8 adjacency was explicitly declined).

### F4 — `skills/vlt-setup/SKILL.md` — the arrival probe + Confirm line

**Current state:** `## Check Dependencies` (`:319-326`) probes *skill*-level companions
(`bmad-agent-builder` etc.), warn-never-hard-fail, with the Confirm surface at `:344`
("**Dependencies** — any genuinely missing skills…"). **Change:** (a) extend the section
with a **machine-tool probe** subsection: read `machine_tools:` from `./assets/module.yaml`
(already read on activation, `:30`); walk `{partners}/*/capabilities/*.md` (resolve
`{partners}` through the structure map; skip the archive zone) collecting `requires:`
entries; probe each distinct tool with `command -v`; for each absent one report the named
line `tool-missing: <tool>` with its declaration's `needed_by:`/`absent:` text (module
rows) or owning `partner/slug` + hint (vault-grown entries). **Report, never gate — the
legal response to a missing tool is stated here (R3): install it per the hint, or accept
the named degraded behavior; setup completes either way.** A fresh install with no
partner zones yet probes the module layer only. (b) Widen the Confirm bullet at `:344`
to "**Dependencies** — any genuinely missing skills (not host-provided ones) **and any
`tool-missing:` lines from the machine-tool probe (declared module tools + capability
`requires:` entries)**, each with its degrade note." **Why:** D6's check half; the
existing section already embodies report-not-gate, so the probe lands in its native home
(single home — `vlt-upgrade` never restates it, F5). **Out of scope:** the `:326` no-web-
tool-check posture stands; the skill-level bullets are untouched.

### F5 — `skills/vlt-upgrade/SKILL.md` — the persisted arrival record + the census

**Current state:** Step-4 schema (`:93-112`) has no dependency key; `migrations_run:`
enum at `:107`; migration bullets `:77-81`; Step-5 ledger Notes line (`:142`) names
`local_conventions_intact`/`vault_writable_collisions`/`manifest_write_divergence`
when non-empty. **Changes:**

1. **Schema key.** Add to the Step-4 block (natural position: after
   `governance_divergence:`):
   `machine_tools_missing: [<tool>: needed by <needed_by> — <absent/degrade note>, ...]   # the Check Dependencies machine-tool probe (vlt-setup, via the Step-3.6 hand-off) — declared module tools + capability requires: entries; report-never-gate; never omitted when empty ([] = every declared tool present)`
   The walk-the-schema-top-to-bottom rule (`:91`) and the persist + key-set verify
   (`:120-122`) then carry it with no further mechanism. A10-14's
   unskippable-mandatory-lines direction is **B10-6's** (already shipped) — this key
   simply joins the schema it hardened.
2. **Census migration.** New bullet in Step 3.5 (after loop-profile relocation, `:81`,
   before "`Run any other migrations`" `:82`): **Dependency census (human-gated offer,
   one-time per capability):** walk vault-grown capabilities
   (`{partners}/*/capabilities/*.md`) **lacking any `requires:` key**; for each, surface
   the capability (body + any `scripts/` sibling) with the clerk's inferred tool entries
   and **offer** to write `requires:` — or explicit `requires: []` on a "needs nothing"
   ruling (the censused-none marker; template rule, F2). Never auto-write. Record
   `dependency-census` in `migrations_run` when any capability is censused. Idempotent —
   a capability carrying the key is skipped; the offer itself re-fires each upgrade
   while uncensused capabilities remain (R1). Not a relocation — the `:75` discipline's
   stub/re-point rules don't apply (frontmatter edit in place).
3. **Enum + Notes.** Add `dependency-census` to the `migrations_run:` enum (`:107`);
   add `machine_tools_missing` to the Step-5 Notes name-when-non-empty list (`:142`).

**Why:** D6's check half on the upgrade path + the retroactive census; dispositions 5–6.
**Out of scope:** Step 1 pre-flight snapshots nothing new (the probe is arrival-time,
not drift-detection); the Step-4 prose paragraphs (`:114-118`) gain nothing — the schema
line's own annotation is the key's contract.

## Registration

**None.** No new skill, no workflow, no `module-help.csv` row, no marketplace entry. No
convention `version:` moves anywhere: `capability-template.md` is a skill asset (not
handshaked), `module.yaml` and SKILL.md files are unhandshaked, and the operating
contract is untouched (no C6 rule-card re-derive — the contract already delegates the
capability schema to the template at `:242` and its durable-host doctrine at `:96-98` is
satisfied, not amended). No new `package-lint` check (no E4 fixture debt). Priced and
clear.

## Out of scope (dispositioned)

- **A version-aware probe (minimum versions, `--version` parsing)** — rejected: presence
  is the portability gap the filing names; version constraints are speculative machinery
  with no field instance. A field case files the widening.
- **Auto-install of missing tools** — rejected: report-not-gate is D6's letter; an
  installer is a consent + platform-matrix problem this module refuses.
- **A `vlt-lint` check over `requires:` well-formedness or drift** — deferred: no
  finding class exists yet for it; the probe is the net. If requires-drift shows up in
  the field, it files and gets captured (enforcement-ships-with-evidence).
- **`{conventions}/decision-log.md` and the writer roster** — untouched by explicit
  addendum ruling (A10-12/13 held for Arc 11; "the B10-8 mint-ceremony adjacency was
  declined as a weak fit").
- **`vlt-feedback`'s own pre-flight** — untouched (disposition 7): exercise-time and
  arrival-time probes are complementary moments, not an overlap to eliminate
  (precedence-by-elimination not triggered — distinct populations by construction).
- **Shipped op skills' per-skill tool assumptions beyond the four declared** — covered
  by the module.yaml writer clause going forward; today's sweep found no fifth (web
  tooling is explicitly a host concern, `vlt-setup/SKILL.md:326`).
- **Per-vault override of `machine_tools:`** — rejected: module-level facts are
  module-owned; a vault's own additions are the vault-grown layer.
- **A config.yaml export of the declaration** — rejected (disposition 2): the probe
  reads module.yaml directly; exporting would mint a second home.

## Verification (unit, at rest)

- **YAML integrity:** `uv run` a one-line pyyaml parse of `module.yaml`; confirm
  `machine_tools` is a list of four mappings each carrying `tool`/`needed_by`/`absent`.
- **Merge-config inertness (fixture run):** against a temp fixture vault, run
  `merge-config.py` with the edited `module.yaml` and empty answers; assert the emitted
  `config.yaml` `vlt:` section carries **no** `machine_tools` key and the JSON output
  lists only `vault_structure`/`feedback_repo` as variables (the disposition-2 claim,
  proven not asserted).
- **Four-way agreement greps:** `requires:` appears in `capability-template.md` (both
  schema blocks + the rule paragraph), `vlt-mint/SKILL.md` (both Step-3 bullets, pointer
  form), `vlt-setup/SKILL.md` (probe walk); `machine_tools:` in `module.yaml` +
  `vlt-setup/SKILL.md` (probe) only; `machine_tools_missing` in `vlt-upgrade/SKILL.md`
  (schema + Notes list) only; `dependency-census` in both the migration bullet and the
  `migrations_run:` enum; `tool-missing` in `vlt-setup/SKILL.md` (and nowhere restated).
- **Handshake bipartite re-check:** no `version:` moved, but run **`package-lint` Group
  E** anyway as the check of record (E1/E2/E3 must stay green — E2 in particular proves
  the `module.yaml` edit didn't disturb the `vault_structure` default map the contract
  table mirrors).
- **Packaging lint:** mid-arc `uv run tools/package-lint.py` groups **A/B/C/E** pass
  (C parses the edited `module.yaml`; version gate D rides the release build, not this
  one — this build ships no version bump).
- **R2:** not applicable — no release-gate check added or changed.
- **R3:** substantive — the `tool-missing:` report class's one-line legal response
  (install per hint, or accept the named degrade; never a gate) ships at the check's
  single home, `vlt-setup/SKILL.md` Check Dependencies (F4), in the same build.
- **R4:** substantive — every enumeration this build's additions touch is widened in the
  same act: the Step-4 schema key set (+ its verify), the `migrations_run:` enum, the
  Step-5 Notes name-when-non-empty list, and the capability schema blocks at their
  single template home. No new *file* joins any enumerated class (no manifest entry, no
  always-loaded file, no persisted-surface census entry — disposition 6 records why).
- **Scrub:** no personal or vault-local content in any changed shipped file; the
  `machine_tools` rows and all worked examples name tools and placeholder paths only.

*(Non-release build: no version-string bumps; the Release section is omitted per the
anatomy — v0.14.0's release build carries them.)*

## Acceptance (live — appended to the roadmap ledger)

1. **`[ship-verifiable]`** — the declaration layer is on disk and inert where it must
   be: `module.yaml` carries the four-row `machine_tools:` block with the writer clause,
   the fixture `merge-config.py` run shows the key never reaches `config.yaml` and the
   variable set is unchanged, and the four-way agreement greps + package-lint A/B/C/E +
   Group E pass. Discharged at rest, recorded in the BUILT status.
2. **`[ship-verifiable]`** — the arrival record reaches the persisted report: on the
   owner's next ordinary vlt-core upgrade (bounded — it happens per release), the Step-4
   report renders `machine_tools_missing:` (empty form `[]` legal, absence a failure —
   the never-omit contract), the persisted `_agent/upgrade-reports/*.yaml` verifies with
   the widened key set, and the Confirm summary's Dependencies bullet carries the probe
   result. Performer: the owner; vault: vlt-core (factory-readable).
3. **`[ship-verifiable]`** — the census offer fires where its population exists: the
   same vlt-core upgrade surfaces the dependency-census offer over vlt-core's
   vault-grown capabilities (they exist — the filing's own provenance), writes
   `requires:`/`requires: []` only on the owner's per-capability confirmations, records
   `dependency-census` in `migrations_run` when any is censused, and a re-run offers
   only still-keyless capabilities. Performer: the owner; vault: vlt-core.
4. **`[field-contingent]`** — declare-at-birth is exercised by a real birth; discharging
   event: **the next capability mint or self-grow in vlt-core after this release**
   (performer: the owner with a partner at the wheel; vault: vlt-core,
   factory-readable). Pass = the newborn capability file carries `requires:` (or
   explicit `[]`) from its first commit, with no separate ceremony beyond the template's
   line. Fail = a post-release birth with the key absent.
5. **`[field-contingent]`** — check-at-arrival catches a genuinely stranded toolchain;
   discharging event: **the next `vlt-setup`/`vlt-upgrade` run on the work machine's
   vault** (performer: the owner; vault: the work-machine install — **a vault the
   factory cannot read**; evidence is the owner's report of the probe lines, or a
   hand-saved Confirm/Step-4 excerpt). Pass = every genuinely missing declared tool
   surfaces as a named `tool-missing:` line with its degrade note, and the run completes
   (report, never gate); an all-present result discharges vacuously only for the probe's
   *gating* claim, not its detection claim — a deliberate probe with one tool absent
   (e.g. `gh` off PATH) is the could-have-failed form if the machine has no natural gap.
