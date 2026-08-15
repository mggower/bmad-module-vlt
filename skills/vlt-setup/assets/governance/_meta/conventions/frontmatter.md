---
type: note
created: 2026-06-01
last_updated: 2026-08-15
title: Frontmatter Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 7
consumers: [vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch, vlt-lint-full.js]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
deferral_metric: "prose/behavior drift lint findings + new conventions minted"
deferral_threshold: "2 prose/behavior drift findings since 2026-08-15, or the 3rd convention minted beyond the 9 shipped at that baseline"
review_after: 2026-11-15
---

# Frontmatter Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/frontmatter.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

This file is the **single source of truth** for the frontmatter schemas across every note type the vault uses. The operating contract (`vault-operating-contract.md`) points here and never restates the schema, so there is exactly one place these fields are defined.

Paths below use the structure-map logical names (see the operating contract); defaults shown resolve through `vault_structure` and are overridable per vault.

## YAML syntax rules

These rules are mandatory across every note type. They are codified from real misparse pain in Obsidian-style vaults — a handful of unquoted wikilinks silently misparse, and nested maps vanish from the properties UI. (See the operating contract's vault-syntax assumption.)

1. **Wikilink-valued fields must be double-quoted.** Any field whose value is a `[[wikilink]]` (or a list of them) takes double quotes — `superseded_by: "[[page-slug]]"`, never bare `superseded_by: [[page-slug]]`. YAML treats a leading `[` as a flow sequence and rejects or misparses the value otherwise.
2. **Long or multi-line string fields must be double-quoted.** Any string spanning multiple lines or containing YAML-significant characters (colons, leading dashes, leading brackets) takes double quotes. Block scalars (`>` / `|`) are not used — quote uniformly.
3. **No nested properties.** Obsidian's properties UI does not render nested YAML maps. Every schema in this file is intentionally **flat**; do not introduce nested structures even where YAML would accept them. List fields hold bare scalars (strings, paths, quoted wikilinks), never maps.
4. **List fields split by use: verify vs traverse.** A list you *verify against* — an audit trail, where the record is the point (a session log's `artifacts:`, a research note's `sources:`) — holds bare vault-relative paths, never wikilinks. A list you *traverse* — a link graph, where claims are answerable to origins and following the link is the point — is wikilink-form territory; **a wiki page's `sources:` is a link graph** and is the first field so classed. (Unless a specific schema says otherwise — that carve-out is the delegation slot per-schema rules build on.) **The form:** a wiki page's `sources:` entry that references a **vault note** is a **double-quoted wikilink** (rule 1) carrying the **full vault-relative path, no `.md`** — full path because basenames collide across zones; no `.md` per rule 1's own example (`superseded_by: "[[page-slug]]"`). Entries that are **external URLs are not page references and stay plain strings.** Reserved characters, stated positively: `[`, `]`, `#`, `^`, `|` are reserved inside a wikilink target; **`?` is not** — a target containing it keeps it. **Normalization clause:** any consumer comparing `sources:` entries — across pages, across zones, or against a prose `## Sources` section — normalizes both sides first: strip surrounding quotes and `[[ ]]`, strip a trailing `.md`, and compare on the vault-relative path (tolerating a bare-basename legacy entry by basename match) — so the wikilink and bare-path forms compare equal forever. **Coexistence posture:** existing bare-path entries stay legal and there is **no backfill sweep**; a page adopts the form on its next substantive edit — the normalization clause is what makes the mixed state permanently safe.
5. **Backtick-wrapped wikilinks do not resolve.** `` `[[X]]` `` renders as literal text. Never wrap a wikilink in backticks anywhere a link is intended, in frontmatter or body.
6. **Don't duplicate a frontmatter field as inline body metadata.** If a field lives in the frontmatter, it does not also appear as `**Field:** value` in the document body — that just invites drift.

## Base frontmatter

Every note in the vault carries at minimum:

```yaml
---
type: <note classification>
created: YYYY-MM-DD              # date first written — immutable, never bump on edit
title: <human-readable title>
author: <agent | human | hybrid>
trust: <raw | reviewed | verified | canonical>
---
```

**`created` vs `last_updated`:** `created` is the birth date and is **immutable** — never bump it on a later edit. Note types that are *continuously updated* (wiki pages, the index, re-extracted PARA artifacts) additionally carry `last_updated: YYYY-MM-DD`, bumped on every substantive edit; that is the field `vlt-lint` reads to judge staleness. Written-once note types (research notes, session logs) carry only `created`. The per-zone sections below say which applies. Note that `last_updated` measures *edit recency*, not *content validity* — a page carrying `review_after:` (wiki-page schema below) announces its own content expiry, so lint needs no `last_updated`/mtime inference for it.

**`author` values:**

- `agent` — generated by a partner without human editing
- `human` — written by the human
- `hybrid` — agent-drafted, then edited by a human (e.g. an extracted PARA artifact)

**`trust` ladder:**

| Trust | Meaning |
|-------|---------|
| `raw` | Unreviewed agent output (default for `_agent/` and `_meta/` notes) |
| `reviewed` | Human has read and validated the content |
| `verified` | Key claims checked against primary sources |
| `canonical` | Integrated into personal knowledge; safe to link from MOCs |

The `type:` list is **non-exhaustive.** Canonical values include `wiki`, `research`, `session`, `note`, `project`, `area`, `resource`, `idea`. New artifact classes may introduce new `type:` values without a contract edit; this convention names new values as they appear.

## Write attestation (agent-written artifacts)

Two keys record that the writing operation ran the tier-1 write-verification checklist on the file. This section defines only the **fields**; the checklist, fail-open rule, scope rule, and audit contract live in `write-verification.md`:

```yaml
verified_by: vlt-ingest | vlt-extract | vlt-research | vlt-lint
verified_at: YYYY-MM-DD
```

- **`verified_by`** — the operation that ran tier-1 on this file. The legal value set is the three write ops plus `vlt-lint` (lint attests **narrowly** — only files its own auto-fix touched; see `write-verification.md`).
- **`verified_at`** — the date of that verification. **Freshness rule:** an attestation is valid iff `verified_at` ≥ `last_updated`. A stale attestation is not a violation — lint quietly re-runs tier-1 on the file. Updates re-attest: an op that updates an existing page bumps both keys. Freshness keys off `last_updated`, never `review_after` (content expiry is a different axis).
- **Not the `trust:` rung.** `verified_by`/`verified_at` record *structural* verification (the write ran its checklist); the `trust: verified` rung records *claim* verification (key claims checked against primary sources). Same word, orthogonal axes — an attested page can be `trust: raw`, and a `trust: verified` page can carry a stale attestation.

## Wiki pages (`{wiki}`)

Add to base:

```yaml
last_updated: YYYY-MM-DD             # bumped on every substantive edit
summary: "<one-line scope of the page>"
category: <one controlled subject area — MUST match a wiki index H2 heading>
topic:                               # YAML list, ordered general → specific, lowercase
  - <broad domain>
  - <narrower facet>
status: draft | in-progress | complete
sources: []                          # vault notes as "[[path]]" wikilinks, URLs plain — YAML rule 4
review_after: YYYY-MM-DD             # OPTIONAL — content-expiry date; absence = evergreen
source_type: <url | book | paper>    # OPTIONAL — accession format facet (Register grouping); no rule, no check
review_note: "<what to recheck>"     # OPTIONAL — a hint paired with review_after; no rule, no check
```

`type: wiki`. Wiki pages have stable identity (no datetime prefix in the filename) and are updated continuously — so they carry `last_updated` alongside the immutable `created`. `sources:` accretes as new sources contribute claims. The wiki `index` carries the same `last_updated` for the same reason.

**`category:` and `topic:` — grouping vs. filtering.** These are deliberately two fields doing two jobs, both surfaced in Obsidian Bases:

- **`category:`** is a **single** value naming the page's home subject area, in **Title Case**. It is the **single source of truth for grouping** — it drives the Bases group-by and is the frontmatter projection of the wiki `index` H2 headings. The binding is strict: **every `category:` value MUST be an existing H2 in the `index`** (see `wiki-index.md`), so the agent's structural map and the human's Bases view share one controlled vocabulary and cannot drift. One page → one category. `vlt-lint` flags a `category:` that matches no index H2, or a wiki page missing `category:`.
- **`topic:`** is a **YAML list** of finer subject tags, ordered **general → specific**, **lowercase** (acronyms too: `api`, `ai`). It is for **filtering and cross-cutting discovery** — a page about cold-brew coffee is `category: Coffee Brewing` with `topic: [coffee, brewing, extraction]`, so it groups with all Coffee Brewing pages but filters alongside every `extraction` page across categories. The list is a flat sequence of bare scalars (YAML rule 3 — no nesting). The general→specific ordering is a human-readability convention; grouping is `category`'s job, not `topic[0]`'s.

**Why two fields rather than ordering a single list.** A single `topic` list could in principle drive grouping via a Bases formula on `topic[0]`, but a dedicated `category` keeps grouping legible in the properties UI, lint-enforceable against the index, and decoupled from topic-list reordering. Grouping and tagging never entangle.

**`summary:`** is the page's one-line scope — *what this page covers* — and it is the **single source of truth for that description.** It is the human-facing field surfaced in Obsidian Bases views (the human's primary way of scanning the wiki), and the agent's per-page blurb when it needs detail beyond the slug. It is therefore **not duplicated into the `index`** — the index is a structural map, not a description catalog (see `wiki-index.md`). It is distinct from `topic:` (a short subject-area tag for grouping) and from the page's prose opening (which can be longer).

**Length limit: 160 characters** (counting characters, not bytes — em-dashes count as one). The cap keeps it a single scannable line in a Bases column and forces it to name *what the page is*, not enumerate every section (the body holds the detail). Double-quote it (it almost always contains a colon, em-dash, or comma — see YAML rule 2). `vlt-lint` flags a wiki page whose `summary:` is **missing** or **exceeds 160 characters**.

**`review_after:`** is **optional** and names the date the page's *content validity* should be rechecked — a **resolved date, never a duration** (`2026-08-17`, not `6mo`; the duration judgment belongs at write time, in the writing partner's head). **Absence = evergreen**: only genuinely time-sensitive content carries it (pricing, versioned tools, event timelines, dosing/market state), set at write time. On review, exactly one of three legal outcomes: **bump the date**, **mark the specific claims `[!stale]`** per `wiki-supersession.md`, or **remove the key** (the page proved evergreen). This is the single definition of `review_after` — every other use (including the enforcement-deferral expiry below) references it, never redefines it. A page carrying `review_after` announces its own expiry: `vlt-lint` flags past-due pages (`review_due`) mechanically instead of inferring staleness from `last_updated`/mtime; it never auto-resolves them — the three-outcome review is judgment work.

**`source_type:` and `review_note:`** are **documented-optional** wiki-page slots (091006's v2 keys): `source_type:` (`url` | `book` | `paper`) is the accession *format* facet for cheap Register grouping; `review_note:` is a short "what to recheck" hint paired with `review_after:`. Both are **absence = default, no rule, and no `vlt-lint` check** — inert schema slots defined for forward-compatibility until usage evidence activates them; a page carrying neither is fully conformant.

**Reference Bases views (documented, not shipped).** A vault surfacing these fields in Obsidian Bases typically adds three views to its own vault-grown wiki base (the module ships no `.base` file): **Register** — created / sources / trust / category / last_updated, sorted `created` DESC; **Due for review** — filter `and: [review_after, review_after <= today()]` (`today()` is a global function; the presence guard is load-bearing — a page without `review_after` is evergreen and must not match; if the property registers as text rather than a date, wrap it: `date(review_after) <= today()`); **Horizon** — `review_after` set, sorted ASC (the fallback primary if date filtering misbehaves).

## Research notes (`{research}`)

Add to base:

```yaml
topic:                               # YAML list, ordered general → specific, lowercase
  - <broad domain>
  - <narrower facet>
status: draft | in-progress | complete
sources: []
revisit_after: YYYY-MM-DD            # OPTIONAL — graduation-candidacy recheck date; absence = not a candidate
```

`type: research`. Research notes use the same `topic:` list form as wiki pages (general → specific, lowercase) but carry **no `category:`** — `category` binds to the wiki index, and research notes are not wiki pages. Research notes are dated snapshots (datetime-prefixed kebab-case filenames per the operating contract's Naming Conventions) and rest once complete. **No `last_updated`** — they are written-once; a correction is a new note, not an edit.

**`revisit_after:`** is **optional** and names the date a research note's *graduation candidacy* — its readiness to graduate into the wiki — should be rechecked. It applies the wiki-page key `review_after:`'s date semantics (defined once above) to a research note's *candidacy* rather than a page's *content validity* — same date discipline, different axis; it is **not** redefined here. **Absence = not a candidate** (the note is not offered for graduation): only a note the writing partner judged graduation-relevant carries it, set at write time. Because research notes carry no `last_updated`, `revisit_after` is the self-announcing candidacy signal — `vlt-lint` reads it directly (`revisit_due`) rather than inferring from mtime, exactly as `review_after` announces a wiki page's expiry. `vlt-lint` **surfaces** a past-due `revisit_after` and the linkage finding (`linkage_ripe`); it never auto-promotes a note into the wiki — graduation is judgment work (see `vlt-lint`).

## Session logs (`{sessions}`)

The minimum set:

```yaml
---
type: session
created: YYYY-MM-DD
title: Session Log — YYYY-MM-DD HH:MM
author: agent
trust: raw
partner: <partner-name>              # the roster member who ran the session, e.g. librarian, researcher
---
```

Datetime-prefixed kebab-case filename; optional `-<type>` suffix per the operating contract's canonical suffix set (`ingest | query | lint | research | extract | setup | remediation | misc`). **No `last_updated`** — written once at session end.

**`partner:`** names the roster member who authored the session — the frontmatter analogue of the `(<partner>)` tag on `{log}` entries, so the session trail is greppable by partner (`grep -l "partner: researcher" {sessions}/*.md`). The summoning partner owns the session note for the whole sitting (operation skills append `{log}` entries but never write session notes — see the operating contract's session-ownership rule). Omit only for a partner-less generic-agent session.

## PARA artifacts (`projects/`, `areas/`, `resources/`)

Defined in `extraction.md` (the canonical reference; not duplicated here). Summary:

- `author: hybrid`, `trust: reviewed` at extraction.
- `type:` mapped to target folder: `projects/` → `project`; `areas/` → `area`; `resources/` → `resource`.
- `sources:` lists the wiki pages that fed the extraction.

See `extraction.md` for the full schema, the trust ladder progression, and re-extraction supersession rules.

## Partner memory (`{partners}`)

Each partner keeps its relationship with the user *in this vault* under `{partners}/<partner>/`, split by lifecycle into two files (the sections inside each are defined in the operating contract's "Partner memory — the thread", not here):

**`identity.md`** — the evergreen identity layer (`## Bond` + `## Self`). Continuously updated, so it carries `last_updated`:

```yaml
---
type: identity
partner: <role>             # the roster role — librarian, researcher — stable; used for attribution/grep
name: <given-name>          # OPTIONAL: the name THIS user gave the partner in THIS vault. Empty/absent = go by role/title.
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

**`name` is a first-class but ungated identity fact.** When the user gives a partner a name ("I'll call you Gwyn"), the partner writes it here freely — a user naming a partner is not a contract change, so it needs no council gate; but it is load-bearing enough to deserve its own field rather than being buried in `## Self` prose. It is **per-vault** (the same partner can be named differently in another vault — consistent with "different person per vault") and **overrides the `customize.toml` install default** (`[agent].name`) for this vault. On activation the partner reads it in Beat 1 and answers to it; absent, it goes by its role/title.

**`thread.md`** — the prunable attention layer (`## Thread`). Also continuously updated (and pruned/set-aside as inquiries fade):

```yaml
---
type: thread
partner: <partner-name>
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

Both are partner-private (a relationship layer, not shared knowledge), so they carry `partner:` for attribution but need no `author`/`trust`. Their bodies are `## ` sections per the operating contract. *(Prior to the two-file split these lived in a single `type: thread` file carrying all three sections; `vlt-setup` performs the one-time, idempotent migration to the two files.)*

## Backlog (`{backlog}`)

The vault's evolution intake is a single living file, `{backlog}` — not one file per item. It is glanceable, append-cheap, and read by every partner on activation. It is **not** a per-item note type with its own frontmatter; it is a structured Markdown checklist:

```markdown
# Backlog

## Open
- [ ] <short imperative title> (kind, by: <partner|user>, blocked: user-decision | partner-bandwidth | external-event YYYY-MM-DD) — <one-line why>

## Done
- [x] <short imperative title> (kind, by: <partner|user>) — <one-line why> [resolved: <how>]
```

- **`blocked`** (the optional third facet) is **triage metadata, never a status** — an item can be open and unblocked. **Optional; absence = untagged (zero backfill)** — never rewrite existing items to add it. **`external-event` requires its companion `YYYY-MM-DD` date** (a dateless external-event block could never age — nothing would ever re-surface it); the date dovetails with `review_after:`'s date semantics (referenced, not redefined). The facet may also ride a dispatch pointer line's paren (see `vlt-dispatch`); `vlt-dispatch ledger` groups open items by it, untagged rows rendering as their own bucket.
- **`kind`** ∈ `capability-gap` | `maintenance` | `knowledge-gap`:
  - `capability-gap` — a missing operation or partner; `vlt-mint` filters for these.
  - `maintenance` — wiki health work (drift, near-duplicates, stale claims); feeds `vlt-lint` and inline merges via `vlt-ingest`.
  - `knowledge-gap` — a topic the vault is thin on.
- **`by`** — who filed it (a partner name, or `user`).
- **`why`** — one line; enough to act on later without re-deriving context.

**The address rule.** A noticed gap goes to `{backlog}` only when the filing partner does not know whose turn it is; when it does, the gap is **relayed to that partner** (`vlt-dispatch relay`, shape `ask`). The backlog is evolution intake, not a shared to-do list — it holds the unassignable. Three guards: **(1)** the rule binds every `kind`, not just `knowledge-gap` — it is a rule about address, not subject; **(2)** self-addressed work is not a relay — a partner does not relay to itself; **(3)** migration is one-home — an item that acquires an owner is relayed **and struck** from `## Open`, never left on both rails. And the rule's limit: relay does not schedule work — it buys an **address and a drain**, which the backlog has neither of, not execution; a stale relayed slice is not evidence the rail failed. The `ask` shape and its keyed rail exist — `vlt-dispatch`, `relay` mode owns the shapes, keys, and validation. Filing to `{backlog}` remains the correct move exactly where the rule says: when no partner is the address.

An item promotes to its own note only if it grows into real design work. Filing an item is the cheapest, ungated act in the system; building from it is deliberate (see the operating contract's backlog rules).

## Enforcement declaration (convention files)

Every convention file in `{conventions}` declares, in its own frontmatter, how the boundary it creates is enforced — **no boundary without a bell.** All keys are flat (YAML rule 3; a nested `enforcement:` map is exactly what that rule forbids):

```yaml
enforcement_stage: declared | checked | enforced
enforcement_checked_by: <owner — a partner or a skill, e.g. vlt-lint>
enforcement_moment: <the moment the check runs, e.g. lint run | op final-steps | SessionStart hook>
enforcement_counter: <optional; when present, must name a metric id from the vitals reader's canonical table (.claude/hooks/vlt-vitals.py) — the enforcement kit's one vocabulary>
# deferral — ALL THREE required for any deferral; missing any field = invalid:
deferral_metric: <what is counted>
deferral_threshold: <the tripwire — a number, or a short prose threshold a vault can evaluate from its own state>
review_after: YYYY-MM-DD             # deferral expiry — the wiki-page key above, referenced not redefined
# adoption — OPTIONAL first-instance axis, orthogonal to the violation facets above:
adoption_first_instance: <null | dated reference to the boundary's first live instance>   # null = declared-but-not-yet-adopted; key absent = axis not declared (both absences, not violations)
```

Stage semantics: **`declared`** = the rule exists in prose only; **`checked`** = a mechanical check exists **and** a named owner + moment; **`enforced`** = the check fires at a moment needing no human memory (op final-steps, a hook, a blocking gate). A named human moment ("the Librarian checks at every lint run") is a legitimate `checked` stage before any counter exists. A `declared` stage must carry a complete tripwired deferral — `declared` with no deferral is `declared_untripwired`, a `vlt-lint` finding, as are an incomplete deferral (`deferral_invalid`) and an expired one (`deferral_expired`). Stage promotions (`declared → checked → enforced`) happen through the mint ceremony — dated entries in `_agent/mint/decision-log.md` — never through lint.

**Adoption axis (optional, orthogonal).** Every facet above measures **violation** — the boundary being crossed. `adoption_first_instance:` measures the orthogonal **adoption** question the violation facets structurally cannot: has the boundary this convention declares had its *first live instance* yet? It is one class-wide answer — the first real spec minted under `spec.md`, the first instance of a declared loop profile — recorded as a dated reference **by the ceremony that produces it**, and **explicit `null`** while the class is declared-but-unexercised (a wholly absent key means the axis is not declared — `vlt-upgrade`'s adoption report distinguishes the three values). Because adoption is an **absence** (there is no event to count until the first instance occurs), it is a stamp set once, **never a counter**, and its absence is **not** a `vlt-lint` finding. Whatever checks consume it — a convention's first-exercise acceptance, a loop profile's non-vacuity gate — live where those checks live; this declaration defines only the facet. *Live consumers today:* the facet is stamped by the ceremony that produces a convention's first live instance — `vlt-mint` (mint ceremonies, the same ceremony that promotes `enforcement_stage`), the spec promotion step (`spec.md`, *Promotion from candidate*), `vlt-upgrade`'s proto-spec retrofit, and `vlt-dispatch`'s consult record (the authority rule's single home is `vlt-mint`, Step 4) — and `vlt-upgrade`'s post-flight report + upgrade ledger surface each convention's adoption state. Its absence remains **not** a `vlt-lint` finding; `vlt-lint` never writes it.

**Vault-writable declared fields.** A base convention field may be **declared vault-writable** — an authorized vault-local carry on a shipped base, the class `adoption_first_instance:` already instantiates — and a declared field's local value is not base divergence. The deferral-expiry key `review_after:` on a shipped convention is the second member of that class: a vault records a performed review's outcome without forking the base. *Interim posture:* until the mechanism that honors the declaration ships (the seam build's divergence-diff generalization), a shipped deferral's expiry is **reviewed upstream, and a vault's only legal move is to file** — an expired `review_after:` on a stock convention produces a `deferral_expired` finding that is **correct**, a base edit to clear it still flags `convention_base_divergence` (also correctly), and neither finding should be suppressed locally.

## Narrow-convention escape hatch

This file is one broad convention by deliberate choice — most vault notes touch overlapping schemas (base + per-type additions), and one file keeps the cross-references coherent. If scale or per-type coupling ever justifies it, a narrower convention (e.g. a hypothetical `wiki-frontmatter.md` consumed only by `vlt-ingest`) can be split out later. At current vault scale, one convention is the right default.

**Local conventions (vault-originated).** A vault may originate a **local convention** — a convention file in `{conventions}` with no stock counterpart, carrying its own enforcement declaration. Two properties are mandatory: **(a)** it exists without a stock counterpart — it is not an overlay and shadows no shipped base — and **(b)** it is visible to the split tripwire as a convention in its own right: it counts toward this file's `deferral_metric` ("new conventions minted") exactly as a module-shipped mint would. A landing zone that is merely silent would reproduce today's outcome with better manners; both properties are the floor. *Interim posture:* until the seam build ships the mechanism (the `baseline_missing` exemption and the consumer read), a vault-originated convention file in `{conventions}` still flags `baseline_missing` — the finding is correct in the window; the legal move is to carry the file and file the finding upstream, not to suppress the check or disguise the rule inside an unrelated overlay (the silent third zone this rule exists to close).

## Reading list

- `vault-operating-contract.md` — the operating constitution that points here for frontmatter
- `extraction.md` — PARA artifact schema (cross-referenced above)
- `write-verification.md` — the tier-1 checklist and attestation contract behind `verified_by`/`verified_at`
- `wiki-supersession.md` — supersession callouts used by wiki pages and re-extractions
- `wiki-index.md` — the structural-map index that consumes `type: index` and the `summary:`/`category:`/`topic:` fields (it carries no source counts)
