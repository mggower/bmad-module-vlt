---
type: note
created: 2026-06-01
last_updated: 2026-08-22
title: Extraction Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 4
consumers: [vlt-extract, vlt-lint, vlt-track]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
---

# Extraction Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/extraction.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

This file is the **PARA-layer reference** — containers *and* extracted artifacts: what extraction is (for `vlt-extract` and any other operation that performs an extraction — see *Personalized extraction* below), how extracted PARA artifacts are named and typed, how trust is assigned, how re-extractions preserve history, and the container schema (*PARA containers* below). Paths use the structure-map logical names (see the operating contract); defaults resolve through `vault_structure`.

## What extraction is

PARA artifacts (`projects/`, `areas/`, `resources/`) are **extracted from the wiki** (`{wiki}`), not promoted from research notes. The wiki is the living synthesis layer and remains the source of truth; an extracted artifact is a synthesized, human-oriented deliverable pulled from one or more wiki pages at a specific moment in time. (One bounded widening of the *personalization* provenance — for a deliverable that must reflect the user's lived state — is defined in *Personalized extraction* below; it does not add an artifact write-path, and it does not relax the rule that every method claim traces to a wiki page.)

Research notes in `{research}` are dated snapshots. They rest once complete and are not promoted.

The key distinction: a query returns an answer (optionally filed); a research note records one investigation (dated, rests); a wiki page accretes knowledge across sources (living); an extracted artifact is a deliverable — a curated document shaped for a specific human purpose, pulled from the wiki.

## Personalized extraction — drawing on agent-zone state

A standard extraction's provenance is the wiki and only the wiki. Some deliverables, though, must be **personalized to the user's lived state** — a state the wiki deliberately does not hold, because the wiki is general and reusable (it knows *how spaced repetition works*, not *how this learner is progressing*). Extraction is widened for these by exactly one allowance, with one invariant held hard.

**The hard invariant (unchanged, load-bearing).** Every general or method claim in the body still traces to a wiki page listed in `sources:`. This is the firewall that makes an extracted artifact trustworthy; the amendment does not touch it. Provenance *width* is the soft parameter that moves below; method-grounding is the hard line that does not.

**The soft parameter (the one widening).** *Which files an extraction may additionally draw on for personalization.* A personalized extraction may read a partner's own **agent-zone operational data** (e.g. a progress log under `_agent/`) to tailor the deliverable to the user's situation — the learner's current level, their constraints, what worked last week. To keep the hard invariant legible to a reader **and to a future lint check**, the two provenance roles are **segregated in frontmatter**:

- **`sources:`** continues to list **only wiki pages** — exactly as before, the wiki-provenance audit trail. Every method/general claim in the body maps to an entry here.
- **`personalization_sources:`** is a **separate** list of the agent-zone operational path(s) the extraction drew on for personalization (bare vault-relative paths, per `frontmatter.md` YAML rule 4). Nothing in this list may be the provenance for a method/knowledge claim — it supplies *situation, not fact*.

Because the two roles are distinct fields, "is every method claim wiki-grounded?" stays mechanically checkable: a method claim whose only support is a `personalization_sources` entry is a violation, visible without parsing prose.

**This does not add an artifact write-path.** Artifacts reach PARA only through extraction — same verb, same supersession/re-extraction model, same filename and trust discipline. The **container maintenance surface** (dated, attributed appends to a container's `record.md`/`register.md` — *PARA containers* below, and the operating contract's Layer 3) is the one other named surface, and it carries operational records, never artifacts. The widening here is in what a single extraction may *cite for personalization*, not in how artifacts reach PARA.

**Scope of the allowance — bounded, opt-in, named per operation.** This is **not** a standing license: an operation may use personalized extraction *only* when it is **named as sanctioned**. Per-**partner** authorization was retired at 0.3.0; per-**op** *naming* remains live — a **module-shipped op is named here in the base**, a **vault-local op in `{overlays}/extraction.overlay.md`**. The one **module-shipped** op sanctioned to use personalized extraction is **`vlt-track`** — the shared longitudinal-loop hand (see `vlt-track`); it is module-shipped and so cannot rely on a vault-local overlay for its own authorization, which is why it is named in the base. A domain (vertical) partner's *own* operation may use the widening *only* when that operation's own gated mint **explicitly extends this allowance to name it** (in the vault's overlay): for example, a progress-tracking op for a domain partner that writes a tailored plan to `areas/<domain>/…`, grounded in the wiki and personalized from a progress log under `_agent/`. Absent such a named, gated sanction (base for a shipped op, overlay for a vault-local one), an agent-zone path in a `sources:`/`personalization_sources:` field is a violation, not a precedent. The Creative's `vlt-extract` is unchanged — it remains the general wiki→PARA hand and does not use `personalization_sources`.

**Operational-log discipline (protects single-home).** An agent-zone operational source feeding a personalized extraction holds **state, never general/method knowledge** — a progress log records *what this user did*, not *how a method works*. General knowledge that belongs in the wiki goes to the wiki (via the Researcher/Librarian); it is never parked in an operational log, which would create a second home for the same fact. Such an operation's verify step must check for this leak; the `vlt-lint` personalized-extraction check flags a method/general claim found in a progress log or a body method-claim covered only by `personalization_sources`.

## Trust ladder (extracted artifacts)

| Trust | Meaning | Who sets it |
|-------|---------|-------------|
| `raw` | Unreviewed agent output | Agent (default for `_agent/` notes) |
| `reviewed` | Human has read and validated | Human (starts here for extracted artifacts) |
| `verified` | Claims checked against primary sources | Human |
| `canonical` | Linked from MOCs; fully integrated | Human |

Extracted PARA artifacts start at `author: hybrid`, `trust: reviewed` — the synthesis is agent-drafted; the act of extraction is a human-initiated curation step, so the artifact enters the layer already past `raw`. The ladder climbs from there as the human revises and integrates. MOCs only link artifacts at `canonical`.

## Filename conventions

Kebab-case, **no datetime prefix** — extracted artifacts have stable identity like wiki pages, not dated-snapshot identity like research notes. A later re-extraction overwrites in place (applying supersession callouts for changed claims; see below).

Examples:
- `projects/teal-framework-launch.md`
- `areas/home-energy-plan.md`
- `resources/spaced-repetition-primer.md`

Pick slugs that will still make sense in a year. Avoid datestamps, version suffixes (`-v2`), and status words (`-draft`, `-wip`).

## `type:` mapping by target folder

`type:` matches the target PARA folder:

| Target folder | `type:` value |
|---------------|---------------|
| `projects/` | `project` |
| `areas/` | `area` |
| `resources/` | `resource` |

## Required frontmatter for extracted artifacts

```yaml
---
type: <project | area | resource>
created: YYYY-MM-DD                  # immutable
last_updated: YYYY-MM-DD             # bumped on each re-extraction (overwrite-in-place)
title: <human-readable title>
author: hybrid
trust: reviewed
topic: <subject area>
status: <per-type enum — see below>
sources:
  - <wiki page 1>
  - <wiki page 2>
  - <wiki page N>
# grounding:                         # OPTIONAL — non-wiki evidence/relations (PARA sibling, container, external repo/URL); never method provenance
#   - <reference>
# personalization_sources:           # ONLY on a personalized extraction (see that section); omit otherwise
#   - _agent/<operational path>       # agent-zone state for personalization — never a method-claim provenance
---
```

**Per-type artifact `status:` enums.** `status:` takes a value from the artifact's type enum:

| `type:` | `status:` enum | Note |
|---------|----------------|------|
| `project` | `draft \| in-progress \| complete` | matches the wiki/research enum (`frontmatter.md`) |
| `area` | `ongoing \| retired` | unbounded work — no "done", only retirement |
| `resource` | `complete` | resources arrive finished |

Two rules ride the enums. **A `status:` value is a state, never a changelog** — history belongs in the container's `record.md` and in `last_updated`, never stuffed into the field. **Coexistence posture:** legacy values on files predating this convention stay legal, and there is **no backfill sweep** — a file adopts the enum on its next substantive edit (`vlt-lint` reports an out-of-enum value on a pre-adoption file as informational only: `para_status_unknown`). A **vault-grown** type or template declares its `status:` vocabulary **as schema in `{overlays}/extraction.overlay.md` at the type's birth** — never as an enum-in-comment inside a template.

A re-extraction overwrites the artifact in place, so it bumps `last_updated` (never `created`).

`sources:` lists the wiki pages that fed the extraction — the audit trail back into the vault. Every wiki page referenced in the body must appear in `sources:`. The wiki, not any source beneath it, is the provenance layer for extracted content. A *personalized* extraction additionally carries `personalization_sources:` for the agent-zone state it drew on — a **separate** field so the wiki-provenance audit trail stays clean and the method-grounding invariant stays checkable (see *Personalized extraction*).

**`grounding:`** is an **optional** flat list of evidence and context references that are **not wiki provenance** — a PARA sibling, a container, an external repo or URL — the relation/evidence edge `sources:` was never meant to carry. It may appear on PARA artifacts and on container charters. The segregation rule, stated beside its siblings: `sources:` remains **wiki-only method provenance**; `personalization_sources:` remains **agent-zone state**; **`grounding:` carries evidence and relations, never method** — a method/general claim whose only support is a `grounding:` entry is a violation, and `vlt-lint`'s personalized-extraction firewall polices it (`method_in_grounding`).

## Skill flow (summary)

`vlt-extract` implements:

1. Interview — confirm topic, target folder, purpose, reader
2. Read `{index}` + the identified wiki pages
3. Synthesize into prose (a shaped deliverable, not a dump of wiki content)
4. Prompt for target PARA folder (no default)
5. Propose filename; check for slug collision in the target folder
6. Write with correct frontmatter
7. Append an `extract` entry to `{log}` (partner-tagged, per the operating contract)
8. Verify (re-read, checkbox pass)

(A personalized extraction follows the same flow, additionally reading the relevant agent-zone state in step 2 and listing it under `personalization_sources:` — not `sources:` — in step 6. The one **module-shipped** op that uses this is `vlt-track`, named in *Personalized extraction* above; a vault-local domain op opts in per its own gated mint, named in the overlay.)

## Re-extraction and supersession

When a wiki topic evolves and an earlier extraction becomes stale, the user may ask for a re-extraction. The skill overwrites the existing PARA artifact in place — the filename is stable.

Re-extraction is a wiki-like edit, not a research-like snapshot: the old artifact is not preserved under a new filename. Substantive claim changes use the same supersession conventions the wiki uses — see `wiki-supersession.md`, specifically the inline `[!superseded]` callout for updated claims.

If the re-extraction is so sweeping that the old artifact is effectively a different document, treat it as a page-level supersession: archive the old artifact to `{archive}/<target>/<filename>.md` and write a new one. This is a judgment call the skill surfaces to the user, not an automatic step.

## PARA containers

A **container** is the unit of bounded or ongoing work in Layer 3 — a directory `{projects}/<slug>/` (bounded) or `{areas}/<slug>/` (unbounded) carrying 2–3 declared files. The *behavior* — the two-surface write rule, human-gated charters, whole-container archiving — lives in the operating contract (Layer 3, *PARA containers*); this section owns the **fields**. Sub-containers nest as directories (2–3 levels is typical); membership and containment are answered **by location**, no field. An extracted artifact belonging to a container files into the container's directory; a loose artifact at the layer root stays legal.

**`charter.md`** — the stable frame: outcome, scope, definition-of-done. Human-gated: partner-drafted at most, human-ratified.

```yaml
---
type: charter
created: YYYY-MM-DD                  # immutable
last_updated: YYYY-MM-DD
title: <container title>
author: hybrid                        # partner-drafted, human-ratified
trust: reviewed
status: <container enum below>
# grounding:                          # OPTIONAL — non-wiki evidence/relations (see the grounding paragraph above)
#   - <reference>
---
```

**Container `status:` enums** (on the charter; the bounded/unbounded axis — distinct from artifact status by construction):

| Container | `status:` enum |
|-----------|----------------|
| project container (bounded) | `open \| paused \| closed` |
| area container (unbounded) | `active \| dormant \| retired` |

A lifecycle transition the field records only as prose (e.g. project → area reclassification) is a `status:` change plus a location move, recorded as a dated `record.md` entry — no event machinery.

**Dependency and supersession between containers** live in the charter as a **`## Relations` table** — `kind · target container · note`, kinds `depends-on | feeds | supersedes` — prose and human-curated, never frontmatter machinery (membership and containment already resolve by location). Deliberately **not** a `depends_on:` frontmatter field — that name is the module's handshake-ack vocabulary and would invite confusion in lint reads. Artifact-level evidence edges go to `grounding:`.

**`record.md`** — the dated, append-shaped running record: `type: record`, entries under `## YYYY-MM-DD` headings, **each entry attributed `(<partner>)`** (the `{log}`-entry idiom). The recommended evidence shape is numbered evidence rows (`W1…`/`N1…`) with source links — an idiom, not machinery.

**`register.md`** *(optional)* — decisions and open questions: `type: register`; the recommended shape is numbered questions as `question · evidence · options · decider · pick` rows, with verification/assignment queues as prose idioms — documented here, not enforced by lint.

**Attestation posture:** container files are **operational records, not knowledge artifacts** — attribution rides each dated entry; they carry **no** `verified_by:`/`verified_at:` pair (`vlt-lint`'s `para_missing_attestation` carve-out judges them by this schema, not the artifact attestation rule). The `trust:` ladder above is the container-relevant trust answer — no separate container trust field exists. The three `type:` values (`charter`, `record`, `register`) ride `frontmatter.md`'s declared non-exhaustive `type:` list — named here, no contract edit owed.

## Reading list

- `vault-operating-contract.md` — three layers, the `{log}` format, frontmatter pointer
- `wiki-supersession.md` — supersession callouts used by the wiki and by re-extractions
- `frontmatter.md` — the base frontmatter standard and trust ladder
