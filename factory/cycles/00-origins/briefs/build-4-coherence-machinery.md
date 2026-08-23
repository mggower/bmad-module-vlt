---
title: 'Build #4 — The Coherence Machinery (convention→consumer version-handshake) + its three worked examples'
status: 'BUILT 2026-06-23 — unit-verified; acceptance (live --full sweep + a real convention-edit mint) pending a real vault'
build_log:
  - 'BUILT 2026-06-23. Part 1 (machinery): all 5 conventions seeded with version:/consumers: (frontmatter@2, wiki-index@2, the other three @1); vlt-ingest/vlt-lint/vlt-extract carry flat depends_on: ["name@version"] acks; vlt-lint gained the Convention-coherence governance check (Step 2 bullet + Step 3 never-auto-fix note + Step 5 convention_drift key); vlt-mint convention-edit kind completed (Step 1 enumeration + Step 3 authoring path + handshake exit gate). Part 2+3 (category/topic + source-count removal): lifted verbatim from vlt-core (a4af503 did BOTH in one commit) into frontmatter.md (category/topic/summary wiki schema) + wiki-index.md (structural-map redesign, counts removed) + vlt-ingest/vlt-lint/vlt-lint-full.js consumers. Part 4 (dispatch bus): vlt-dispatch created fresh in the module (was absent — not a mirror) from vlt-core''s three-mode bus, contract handoff #9 delta ported, module-help.csv row added (quoted scope, DP code, 13 cols); partner pointers DROPPED (health-coach/chef are vault-minted, not in module source). Verified: node --check passes; handshake bipartite-consistent at rest (every consumers: satisfied by a matching depends_on, both directions); zero residual source-count policing; flat frontmatter (rule 3) dogfooded; no handshake leak into dispatch/contract; no dangling consumers; no menu-code collision. Scope note: operating contract held OUT of the handshake (Phase D) as planned. vlt-core path: {field-vault}.'
phase: 'Phase B (Coherence)'
module_code: 'vlt'
created: '2026-06-23'
updated: '2026-06-23'
derives_from:
  - 'skills/reports/inbox-evolution-roadmap.md (Phase B row)'
  - 'inbox filing #4 — wiki category/topic frontmatter model (…095509…)'
  - 'inbox filing #3 §3 — source-count drift (…193105…)'
  - 'inbox filing #9 — vlt-dispatch partner communication bus (…163847…)'
ideation_decisions:
  - 'Machinery form: version-handshake (NOT content-diff, NOT a separate map, NOT a bare checklist). Convention declares version:+consumers:; consumer declares depends_on: [name@version]. Two-layer enforcement (vlt-lint net + vlt-mint gate).'
  - 'Field name: depends_on (package.json-faithful; honest about what is checked — a version relationship, not a conformance claim).'
  - 'Obsidian-flat: depends_on is a FLAT list of "name@version" scalars (frontmatter.md rule 3 forbids nested maps — the machinery dogfoods its own convention).'
  - 'Ack location: skill owns its workflow assets (vlt-lint''s ack covers vlt-lint-full.js); checker globs *.md frontmatter only.'
  - 'Scope: machinery + 3 worked examples — category/topic (ADDITION), source-count removal (REMOVAL), #9 dispatch (CLEAN/target case).'
  - 'Source-count: UPSTREAM the counted-row→structural-map index redesign so it becomes the genuine REMOVAL example.'
  - 'Operating contract: OUT of build-4 — its open consumer set (incl. vault-minted partners) is Phase D. #9 demonstrates the complementary single-home+pointer coherence pattern instead.'
  - 'Migration: documented recipe + lint-assisted incremental cleanup (default); a vlt-migrate dry-run helper noted as a follow-up if large-vault migration proves too slow.'
---

# Build #4 — The Coherence Machinery + its three worked examples

## Thesis

Vault is excellent at *making* things and weak at *preserving integrity across change*. Phase B closes
the **propagation** half of that gap: when a convention changes, its consuming skills must follow — and
today nothing detects when they don't (filing #4 §5: drift "sat latent through a whole migration";
filing #3 §3: the index pass still policed source counts the redesigned convention removed).

The cure is a **version handshake**, not a content diff. A consumer skill never *contains* a convention —
it contains an *application* of it (vlt-ingest's template is a *use* of `frontmatter.md`, not a copy), so
you can't cheaply diff faithfulness. But you *can* compare two declared integers. Each convention
publishes a `version:`; each consumer pins which version it was last reconciled against (`depends_on:`).
The check is an integer compare — deterministic, zero false positives. The ack only advances when a
human/agent **deliberately reconciles and records it**, so it is an honest receipt, not an inferred mtime.

The elegant part: **the dependency map already exists as prose.** Every convention ends with a
`## Reading list`, and `wiki-index.md` carries a `## Writer / validator contract` table naming
`vlt-ingest` (writer) and `vlt-lint` (validator). We are not inventing the convention→consumer graph —
we are **formalizing the contract table into machine-checkable frontmatter** and adding the handshake.

Build it, then exercise it with three different *shapes* of change in one phase — the same way Build #2
shipped "a machine and its first run":

| Worked example | Shape | Proves |
|---|---|---|
| **category/topic schema** (#4) | **Addition** to `frontmatter.md` + `wiki-index.md` → 5 consumers | the handshake catches a wide fan-out (does `consumers:` have all 5?) |
| **source-count removal** (#3 §3) | **Removal** from `wiki-index.md` → must reach 3 consumers | the canonical historical drift, now *fixed by* the machinery |
| **#9 dispatch bus** | **Already-coherent** (single home + pointers) | the complementary coherence pattern; the *target state* the handshake encodes |

---

## Part 1 — The coherence machinery (the version-handshake)

### 1.1 Convention side

Add two flat fields to the frontmatter of **each file in `{conventions}` (`_meta/conventions/`)**:
`extraction.md`, `frontmatter.md`, `wiki-consolidation.md`, `wiki-index.md`, `wiki-supersession.md`.

```yaml
version: 1                                  # integer; bump on a change to the RULES consumers must follow
consumers: [vlt-ingest, vlt-lint, vlt-lint-full]   # flat list of consuming skill names
```

- `consumers:` is **seeded from the existing `## Writer / validator contract` table and `## Reading list`** —
  not invented. Where a convention has no formal contract table (e.g. `extraction.md`), derive consumers from
  the skills that JIT-read it (grep the SKILLs for `{conventions}/<file>`).
- `consumers:` lists **skill names**, not workflow assets. A workflow (`vlt-lint-full.js`) is covered by its
  owning skill (`vlt-lint`) — see §1.5.
- Both fields are flat (a scalar + a list of scalars), honoring `frontmatter.md` **rule 3** (no nested maps).

### 1.2 Consumer side

Add one flat field to the frontmatter of **each consuming `SKILL.md`**:

```yaml
depends_on: ["frontmatter@1", "wiki-index@1"]      # flat list of "name@version" scalars
```

- One entry per convention the skill consumes, each pinning the `version` it was last reconciled against.
- **Flat list of strings** — split on `@` to parse. Honors rule 3 (no nested map like `{frontmatter: 1}`).
- Quote each entry (rule 2 — contains a YAML-significant `@` and is safest quoted).

### 1.3 The check — `vlt-lint` (lint-time safety net)

Add a **Convention coherence** check to `vlt-lint`. It is a *governance* check (reads `{conventions}` +
skill frontmatter), distinct from the per-page wiki checks. Slot it as a new bullet in **Step 2** ("Convention
coherence") and a matching report key; it runs in **both** scoped and full modes (cheap — a handful of files).

Logic:
1. For each file in `{conventions}` with a `version:`, read its `version` and `consumers:`.
2. For each named consumer, read that skill's `SKILL.md` `depends_on:` and find its `<convention>@N` entry.
3. **Flag drift** when: the consumer's pinned `N` ≠ the convention's `version` (behind = stale ack), OR the
   consumer is listed in `consumers:` but has **no** `depends_on` entry for that convention (unacknowledged),
   OR a consumer named in `consumers:` doesn't exist as an installed skill (dangling consumer).
4. This is **flag-for-human, never auto-fix** — closing a handshake means a human/agent verified the consumer
   actually conforms; lint must not rubber-stamp that by bumping the integer itself.

Report: add under `flag_for_human` a key `convention_drift: [<convention@version → consumer acks @N>, ...]`.

`SKILL.md` anchor: this is a new bullet in **Step 2: Structural checks** ("Convention coherence — validate the
convention→consumer handshake: every `consumers:` skill's `depends_on` pins the current `version`"), a new
**Step 3** note that it is *not* auto-fixed, and the new `convention_drift` report key in **Step 5**. The
`{conventions}` files are already JIT-read on activation, so no new read cost.

### 1.4 The gate — `vlt-mint` `convention edit` kind (edit-time enforcement)

**`convention edit` is currently a half-wired kind** in `vlt-mint`: Step 2 (the blast-radius gate) lists it as
council-gated, but Step 1's kind enumeration and Step 3's authoring paths **omit it entirely**. Build-4
completes it, and the coherence gate is its authoring discipline:

- **Step 1 (Resolve what's being minted):** add `convention edit` to the named kind set (subject = the
  convention file + the change). It stays **council-gated** (already true in Step 2 — full panel, the
  conventions are load-bearing governance).
- **Step 3 (new authoring path "Edit a convention"):** the procedure is the handshake ceremony —
  1. Apply the convention change.
  2. **Bump the convention's `version:`** (only if the change touches the *rules consumers follow* — see §1.6).
  3. **Read the convention's `consumers:` and walk every one** — present them as a checklist the gate can't
     skip. For each consumer that needs updating, make the change and **bump that consumer's `depends_on`
     entry** to the new version.
  4. **Exit gate:** the mint cannot close while any `consumers:` skill's `depends_on` still pins the old
     version. (This is the edit-time mirror of §1.3's lint check — the gate makes drift impossible to ship,
     the lint check catches drift introduced *outside* the ceremony.)
- This dovetails with filing #5's request for explicit phased gates in `vlt-mint`; the convention-edit exit
  gate is one concrete instance.

### 1.5 Ack location — skill owns its workflow

`vlt-lint-full.js` is a JS workflow with no frontmatter and is listed (filing #4 §5) as a distinct consumer.
Decision: **the owning skill's ack speaks for its workflow assets.** `vlt-lint`'s `depends_on` covers
`vlt-lint-full.js`; the coherence checker globs `*.md` frontmatter only (one format). Revisit only if a
workflow ever consumes a convention its owning skill does not — none does today.

Therefore `consumers:` lists `vlt-lint` (not `vlt-lint-full`) wherever the workflow is the real consumer; the
"5 consumers" of the category/topic example collapse to the **skills** `vlt-ingest`, `vlt-lint` (covering its
workflow). Confirm the exact consumer set per convention during the build from the contract tables + greps.

### 1.6 Seeding & the bump rule

- **Seed:** all five conventions start at `version: 1`; every consumer's `depends_on` is seeded to `@1` as part
  of the build (the build itself is the first full reconciliation — everyone is in sync at v1).
- **Bump rule (document it in `vlt-mint`'s convention-edit path and as a one-liner in each convention or the
  Reading list):** `version` bumps on a change to *the rules consumers must follow* — a schema field, a row
  format, a validation rule. It does **not** bump on a typo, a `## Reading list` tweak, prose clarification, or
  an example. This keeps the handshake from churning on cosmetic edits.

After seeding, the two worked-example edits below land as the **first real version bumps** — the machinery's
maiden voyage.

---

## Part 2 — Worked example A: the category/topic schema (ADDITION)

Splits the overloaded `topic:` string into `category:` (single Title-Case value = a wiki-index H2, the
grouping key for Obsidian Bases) + `topic:` (lowercase YAML list, general→specific, the filtering axis).
Reference implementation: vlt-core branch `frontmatter-category-topic`, commit `a4af503` (74 files) — **lift
the schema verbatim where possible.** Exact module-side edits (from filing #4):

- **`conventions/frontmatter.md`** → **bump `version`**. Wiki schema: add `category:` (single Title-Case),
  convert `topic:`→list; add a "grouping vs filtering" subsection (Bases group-by wants one value/page; a
  dedicated `category` is legible + lint-enforceable + decoupled from list ordering). Research-note schema:
  `topic:`→list, explicitly **no `category:`**.
- **`conventions/wiki-index.md`** → **bump `version`** (this file is *also* edited by Part 3 — do both edits,
  one version bump). Add "The `category:` binding": every `category:` value = an existing H2; rename/merge
  rewrites all affected pages in the same edit; lint validates; the index keeps finer within-category
  structure. Update the writer/validator contract table.
- **`vlt-ingest/SKILL.md`** (consumer) → wiki template: add **`summary:`** (currently missing from the wiki
  frontmatter template entirely), `category:`, `topic:` as a list, plus "never invent a category outside the
  index H2 set." Research template: `topic:`→list. Step 9 verify adds category/summary/topic checks. **Bump
  `depends_on` for `frontmatter` and `wiki-index`.**
- **`vlt-lint/SKILL.md`** (consumer) → Step 2/3 add a "Frontmatter / Bases-field drift" check+fix; Step 5
  report adds `fix_now.frontmatter_drift` + `flag_for_human.category_no_match`. **Bump `depends_on`.**
- **`vlt-lint-full.js`** (covered by `vlt-lint`'s ack): `PAGE_SCAN` returns `category` / `topic_is_list` /
  `summary_issue`; `INDEX_SCAN` returns `category_violations`; the reduce emits the two new report keys.

**Open sub-decisions to confirm during build (from filing #4):** topic casing (chose lowercase incl.
acronyms); keep/drop general→specific ordering (readability-only); should `vlt-setup` ship a starter
`wiki-index.base` with `groupBy: category`.

---

## Part 3 — Worked example B: source-count removal (REMOVAL)

The decision (ideation 2026-06-23): **upstream the counted-row → structural-map index redesign** so source-count
removal is a genuine convention removal the machinery propagates. In the *module* source today the count is a
legitimate, in-sync convention (writer sets it, lint auto-fixes it); the removal lives only in the vlt-core
install. Adopting it bumps `wiki-index.md` and forces the handshake to find all three consumers.

The redesign (reconcile against the vlt-core reference `wiki-index.md` if available; else apply this delta):

- **`conventions/wiki-index.md`** → (same **`version` bump** as Part 2):
  - Canonical row format drops the count: `- [[page-slug]] — <one-line description>` (remove `(N source[s])`).
  - **Remove the entire "## Source count — the pinned definition" section.**
  - Update the "## Writer / validator contract" table: drop the writer's "set counts" obligation and the
    validator's "auto-fix counts" obligation. Reframe the index as a **structural navigation map** (categories
    + rows + stubs), not a metrics ledger.
- **`vlt-ingest/SKILL.md`** (consumer) → stop writing the source count into the index row (line ~110: the
  `(N source[s])` clause and the "pinned definition" instruction). `depends_on` already bumped in Part 2.
- **`vlt-lint/SKILL.md`** (consumer) → remove "source counts match the pinned definition" from Step 2 Index-drift
  (line ~60) and "correct source counts against the pinned definition" from Step 3 (line ~67), plus the
  malformed-`sources:` count exception. `depends_on` already bumped in Part 2.
- **`vlt-lint-full.js`** (covered by `vlt-lint`) → remove `sourcecount_fixes` from `INDEX_SCAN` (line ~90), the
  `index_sourcecount_fixes` reduce emission (line ~237), and any index-agent prompt text computing count
  corrections.

Because Parts 2 and 3 both edit `wiki-index.md` and both touch `vlt-ingest` + `vlt-lint`, do them as **one
reconciliation pass per consumer** — a single `depends_on` bump per consumer covers both the addition and the
removal. This is the machinery's value made visceral: one handshake walk catches *both* shapes of change at once.

---

## Part 4 — Worked example C: the #9 dispatch bus mirror (CLEAN / target case)

`vlt-dispatch` becomes the vault's **partner communication bus** — one record (`_agent/dispatch.md`), one drain,
three modes (`daily` / `relay` / `ledger`). Already designed + applied in the vlt-core install; this is a
low-risk **mirror-upstream** job with **zero migration** (idempotent text edits; existing records are
forward-compatible). It earns its place in Phase B as the coherence pattern done *right*: the **relay-when-done
reflex has a single home** (the `relay` mode mechanics + the operating contract's cross-cutting rule), with
partner skills carrying only a **pointer** — the same single-source-of-truth discipline the handshake enforces,
applied to prose instead of versions. It is the *target state*, not a drift to fix.

Mirror the full filing-#9 spec (it is exact and complete):
- **`vlt-dispatch/SKILL.md`** — replace wholesale with the bus version (three modes; `daily` is the only mode
  that reads `daily/`; `relay` is a thin scribe; `ledger` is a read-only board; bare call → mode menu).
- **`_meta/vault-operating-contract.md` § Sessions, sittings, and hand-offs** — add the two handoff timings
  (synchronous payload vs durable doc in `_agent/handoffs/`), the relay-when-done reflex (named here, mechanics
  owned by `relay` mode — single-home), and the "durable handoffs updated in place at a stable path" lifecycle
  rule. *(Note: this contract edit is the single-home/pointer coherence pattern — it is **not** wired into the
  version-handshake, per the scope decision that the contract's open consumer set belongs to Phase D.)*
- **Partner pointers (only where a live durable-handoff relationship exists):** `vlt-agent-health-coach`
  (fire the relay reflex after writing the nutrition-spec doc; revise in place) and `vlt-agent-chef` (the spec
  arrives as an open pointer; ordinary pickup). Resist baking into all partners.
- **`module-help.csv` (×2 — live + `vlt-setup` install mirror, kept identical):** retitle the dispatch row
  "The Partner Communication Bus"; three-mode description; scope column `{mode: daily | relay | ledger; bare
  call → menu}`. **Quote the scope cell** (it contains commas) — see the CSV-quoting guard from Build #3.

---

## Migration (category/topic data — existing vaults)

**Default (this build): documented recipe + lint-assisted incremental cleanup.** Ship a short upgrade recipe;
the new `vlt-lint` frontmatter-drift check (Part 2) flags pages missing `category:` / `topic`-as-list so cleanup
is guided and incremental. The module ships the *convention*; the *data* lives per-vault. The handshake itself
needs **no** migration (additive frontmatter). Source-count removal needs no data migration either — existing
`(N sources)` index suffixes are cosmetic and get cleaned on the next `vlt-ingest`/`vlt-lint` index pass.

**Follow-up (note, don't build now):** a `vlt-migrate` dry-run helper (mirroring the reference
`migrate_category_topic.py`: add `category:` = index H2, convert `topic:`→list, per-page review) — adopt only if
lint-assisted migration proves too slow on large vaults (vlt-core's ~65 pages is the stress case).

---

## Build order

1. **Machinery first (Part 1)** — add `version:`/`consumers:` to all 5 conventions (seed v1), add `depends_on:`
   (seed @1) to every consumer SKILL, add the `vlt-lint` Convention-coherence check, complete the `vlt-mint`
   `convention edit` kind + its handshake gate. *Verify: a deliberately stale `depends_on` is flagged; the
   vlt-mint gate refuses to close on a stale ack.*
2. **Worked example A+B together (Parts 2+3)** — the single `wiki-index.md` + `frontmatter.md` version bumps and
   the one-pass-per-consumer reconciliation (category/topic addition AND source-count removal). *Verify: after
   the bumps, every consumer's `depends_on` is current and the coherence check is green; a forgotten consumer
   bump is caught.*
3. **Worked example C (Part 4)** — mirror the #9 dispatch bus (independent of the handshake; can land in
   parallel). *Verify: idempotent re-apply is a no-op; CSV scope cell is quoted; both csv copies identical.*

Order rationale: the machinery must exist before its first bumps can be reconciled through it; A+B share the
same files so they reconcile in one pass; C is independent prose-coherence and can slot anywhere.

---

## Acceptance / verification

- **Handshake green at rest:** with everything seeded + reconciled, `vlt-lint`'s `convention_drift` is empty.
- **Drift is caught:** hand-edit one consumer's `depends_on` back a version → lint flags exactly that consumer.
- **Gate holds:** a `convention edit` mint that updates the convention but forgets a consumer cannot close.
- **Both shapes propagate:** category/topic addition reaches all consumers; source-count removal leaves no
  consumer still policing counts (grep `vlt-ingest`/`vlt-lint`/`vlt-lint-full.js` for `source count` / `sourcecount`
  → zero hits).
- **#9 mirror:** dispatch three-mode SKILL installed; contract handoff section present; partner pointers in
  health-coach + chef only; both `module-help.csv` copies identical with the scope cell quoted.
- **Dogfooding:** every new frontmatter field added by this build is flat (no nested maps) — the machinery
  obeys `frontmatter.md` rule 3.

---

## Explicitly NOT in build-4 (and why)

- **Operating-contract versioning** → Phase D. Its consumer set is *open* (every partner, incl. vault-minted
  partners absent from module source) and needs a *discovery* variant of the check, which is entangled with
  Phase D's minted-partner durability problem. #9's contract edit uses the complementary single-home+pointer
  pattern instead.
- **A bespoke `vlt-migrate` skill** → follow-up (see Migration). Recipe + lint covers the default case.
- **The Capability-object family-invariant check** → Phase C strand. It is *the same handshake applied to
  capability families*; build it on this machinery once the lightweight capability tier exists.

---

## Open questions for the build

- **Consumer-set exactness:** confirm each convention's `consumers:` from its contract table + a grep of which
  SKILLs JIT-read it (especially `extraction.md`, `wiki-consolidation.md`, `wiki-supersession.md`, which have no
  formal contract table).
- **vlt-core reference availability:** can the build read the vlt-core install's redesigned `wiki-index.md` +
  the `a4af503` category/topic schema to lift verbatim, or must it reconstruct from the deltas above?
- **Index `base` starter:** ship `wiki-index.base` (`groupBy: category`) in `vlt-setup` now, or defer? (filing #4)
- **Does the coherence check belong in `vlt-lint` or a tiny dedicated `vlt-doctor`-style governance check?**
  (Recommendation: `vlt-lint` — it already reads `{conventions}` and runs in both modes; a new skill is
  premature at n=1 governance check.)
