# Convention change: wiki `category` / `topic` frontmatter model

**Filed:** 2026-06-07
**Origin vault:** `vlt-core` (`{field-vault}`)
**Filed by:** Librarian (Gwyn)
**Type:** convention + skill change — fold into the module's next version
**Branch with the reference implementation:** `frontmatter-category-topic` (commit `a4af503`)

---

## TL;DR for the maintainer

We split the Bases-surfaced wiki frontmatter into **two fields doing two jobs**:

- **`category:`** — a *single* Title-Case value that **must equal a wiki `index` H2 heading**. It is the **grouping key** (drives Obsidian Bases group-by). One controlled vocabulary, two representations: the `index` (Markdown, for the agent) and `category:` (frontmatter, for the human's Bases). Lint-enforced so they can't drift.
- **`topic:`** — a **YAML list**, ordered general → specific, lowercase. It is the **filtering / cross-cutting** axis, not a grouping key.

This replaces the prior single `topic:` string field, which was carrying both jobs and could be neither consistent nor groupable. The change touches **two convention files and three skills/workflows**, and it **surfaced a separate latent bug** (the index-redesign was never propagated into the skills — see §5). All of these likely exist in the **module's shipped artifacts** and should be fixed at the source, not just in this vault.

---

## 1. Problem statement

Two coupled problems in the shipped wiki schema:

### 1a. `topic:` was overloaded and inconsistent

Across 65 real pages, the single `topic:` string field had **four simultaneous inconsistencies**:

| Axis | Evidence in the wild |
|---|---|
| **Delimiter** | both slash (`books / fantasy romance / characters`) and comma (`personal finance, portfolio construction`) — two conventions in one field |
| **Type** | a **string**, not a list — Bases can only string-match the whole value, not filter on a member |
| **Granularity** | 1 level (`cooking`, `dogs`) vs 3 levels (`books / fantasy romance / characters`) |
| **Casing** | `NFL defensive schemes` vs `dog training` vs `japanese-tea` (kebab) |

Root cause: `topic:` was being asked to be **both** the broad bucket **and** the fine tag. A field doing two jobs can't be consistent at either.

### 1b. No frontmatter grouping key; index categories over-fragmented

The user wanted to **group the Bases view by category**, but the only category vocabulary lived in `index.md` (Markdown headings) — not readable by Bases, which groups on frontmatter. And the index categories were over-split for scanning: three separate NFL categories (`NFL Defensive Schemes`, `NFL Offensive Schemes`, `NFL Draft`) decoupled a natural cross-over.

---

## 2. The decision and its rationale

**Two fields, not one.** `category:` (single, controlled) for grouping; `topic:` (list) for filtering.

Rationale worth preserving in the module docs:

- **Bases group-by wants one value per page.** A list field produces a row in *every* group for each member — not clean mutually-exclusive groups. So grouping needs a single-valued field.
- **A single `topic` list *could* group via a Bases formula on `topic[0]`** (the user correctly noted this). We chose a dedicated `category` anyway, for robustness: (1) it's legible in the properties UI; (2) it's lint-enforceable against the index; (3) it **decouples grouping from topic-list ordering** — reordering `topic` (a frequent, low-stakes edit) can't silently re-bucket a page. Same destination, sturdier road.
- **`category` = `index` H2, as a strict binding.** This is the elegant part: the index *already is* the category vocabulary, just in a representation Bases can't read. Rather than duplicate or let them drift, we bound them: every `category:` MUST be an existing H2; renaming/merging an H2 means rewriting the `category:` of every page under it in the same edit; lint validates the binding. This honors the vault's "one artifact, one master" principle — the index stays the agent's map, `category` is its projection for the human's Bases, sharing one vocabulary.
- **`topic` ordered general → specific** is a human-readability convention only (grouping is `category`'s job). Lowercase incl. acronyms (`nfl`, `ai`) for tag consistency.

The index keeps **finer structure within a category** (italic sub-groups, hub→entity nesting) that `category` doesn't capture — so a category can be broad (one Bases group) while the index still clusters its pages richly for filing precision. Example: the merged `NFL` category holds italic `*Defensive schemes*` / `*Offensive schemes*` / `*Draft*` sub-groups, and the per-page `topic` carries `[football, nfl, defense|offense|coaching|draft]`.

---

## 3. Exact changes to ship in the module

### 3a. `conventions/frontmatter.md`

- **Wiki pages schema** — add `category:` and convert `topic:` to a list:
  ```yaml
  summary: "<one-line scope, ≤160 chars>"
  category: <one controlled subject area — MUST match a wiki index H2 heading>
  topic:                               # YAML list, ordered general → specific, lowercase
    - <broad domain>
    - <narrower facet>
  ```
- Add a **`category:` and `topic:` — grouping vs. filtering** subsection (the spec: category single/Title-Case/= index H2/single source of truth for grouping; topic YAML list/general→specific/lowercase/filtering; the "why two fields not one ordered list" rationale).
- **Research notes schema** — convert `topic:` to the same list form; explicitly state research notes carry **no `category:`** (category binds to the wiki index; research notes aren't wiki pages).

### 3b. `conventions/wiki-index.md`

- Add **"The `category:` binding"** subsection under the Category model: the strict bidirectional rule (every `category:` must be an existing H2; rename/merge rewrites all affected pages in the same edit; lint validates; the index keeps finer within-category structure that `category` doesn't capture).
- Update the **Writer/Validator contract table**: writer (`vlt-ingest`) sets `category:` (= the H2 it files under) and the `topic:` list, and rewrites `category:` on rename/merge; validator (`vlt-lint`) checks `category` exists + matches an H2 and that `topic` is a list.

### 3c. `vlt-ingest` SKILL

- **Wiki page frontmatter template** — add `summary:`, `category:`, and the `topic:` list (NB: the shipped template was *also missing `summary:`* entirely — predates that field). Add the explanatory note: never invent a `category` outside the index H2 set; if none fits, that's a structural index decision.
- **Research note template** — `topic:` as a list.
- **Step 9 verify checklist** — add `category` (matches an H2), `summary` (≤160), and `topic` (a list).

### 3d. `vlt-lint` SKILL

- **Step 2 / Step 3** — add a **"Frontmatter / Bases-field drift"** check + fix (summary present/≤160; category present + matches an H2; topic is a list; auto-fix typos & string→list, flag a category that fits no H2).
- **Step 5 report schema** — add `fix_now.frontmatter_drift` and `flag_for_human.category_no_match`.

### 3e. `vlt-lint-full.js` workflow

- `PAGE_SCAN` schema + per-page prompt — return `category` (verbatim), `topic_is_list`, `summary_issue`.
- `INDEX_SCAN` schema + index-agent prompt — return `category_violations` (pages whose `category` matches no H2); the index agent knows the H2 set, the per-page agents don't.
- Reduce — emit `fix_now.frontmatter_drift` and `flag_for_human.category_no_match`.

---

## 4. Migration for existing installs (upgrade path)

Any vault upgrading to this schema needs a **one-time data migration** of its wiki pages: add `category:` (= the page's index H2) and convert `topic:` string → list. The reference implementation is a dry-run-first Python script (kept at `_agent/vlt-verification/migrate_category_topic.py` in `vlt-core`):

- Build a `{slug: (category, [topics])}` mapping by hand (judgment per page — the topic facets aren't mechanically derivable).
- Validate **before** writing: every wiki page is mapped; every `category` ∈ the index H2 set; no empty categories.
- Dry-run prints a full manifest + sample diffs; `--apply` writes in place.
- Post-apply invariant check: `set(category values) ⊆ set(index H2s)` and no empty H2.

**Module action:** consider shipping this as a `vlt-migrate` helper or a documented upgrade recipe, since every existing install hits the same one-time conversion. At minimum, the upgrade notes should warn that the schema change is **not backward-auto-filled** — old pages keep working in Obsidian but won't group until migrated.

---

## 5. SEPARATE BUG surfaced — index-redesign drift (likely in the shipped module too)

While updating the skills, I found that an **earlier** index redesign (counted-row index `- [[page]] — desc (N sources)` → a structural map with no descriptions/counts/dates) had updated `conventions/wiki-index.md` **but not the skills that consume it**:

- `vlt-ingest` Step 7 still instructed writing the **old counted-row format** and maintaining source counts in the index.
- `vlt-lint` Steps 2/3 still told lint to **"correct source counts against the pinned definition"** in the index — against an index that no longer has them.
- `vlt-lint-full.js` still carried `sourcecount_fixes` in `INDEX_SCAN` and a "pinned source-count" index-agent prompt.

I fixed all three in lockstep with the category work. **But the module almost certainly ships the same inconsistency** — verify whether the module's `wiki-index.md` was redesigned to structural while its `vlt-ingest`/`vlt-lint`/`vlt-lint-full` still describe counted rows, and fix at source.

**Process recommendation for the module:** a convention change must be propagated to *every skill that references it* in the same change. The module would benefit from a tracked **convention→consumer dependency map** (which skills cite which convention), so a convention edit has a checklist of skills to update. This drift sat latent through a whole migration because nothing connected the convention to its consumers.

---

## 6. Open design questions (decide module-wide)

1. **Casing of `topic` values** — we chose lowercase incl. acronyms (`nfl`, `ai`). Confirm as the module default.
2. **The general→specific ordering convention** — readability-only (Bases won't enforce it). Keep as a soft convention or drop?
3. **Should `research` notes ever carry `category`?** We said no (binds to the wiki index). Revisit if research notes ever get their own Bases view.
4. **`vlt-setup`** — should new vaults get a starter Bases view (`wiki-index.base`) with `groupBy: {property: category}` pre-wired? The user hand-added the groupBy this session; shipping a default view would close the loop.

---

## 7. Reference artifacts in `vlt-core`

- Commit `a4af503` on branch `frontmatter-category-topic` — the full diff (74 files: 2 conventions, 3 skills/workflows, 65 pages, index, .base, migration script).
- `_agent/vlt-verification/migrate_category_topic.py` — the migration script + embedded mapping (a worked example of the per-page category/topic assignment).
- `_agent/wiki/index.md` — the 13-category structure post-merge.
- `_agent/wiki/wiki-index.base` — the Bases view with `groupBy: {property: category, direction: ASC}`.
