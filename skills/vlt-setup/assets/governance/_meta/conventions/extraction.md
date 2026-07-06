---
type: note
created: 2026-06-01
last_updated: 2026-07-06
title: Extraction Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 2
consumers: [vlt-extract, vlt-lint, vlt-track]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
---

# Extraction Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/extraction.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

This file is the reference for the `vlt-extract` operation (and any other operation that performs an extraction — see *Personalized extraction* below): what extraction is, how extracted PARA artifacts are named and typed, how trust is assigned, and how re-extractions preserve history. Paths use the structure-map logical names (see the operating contract); defaults resolve through `vault_structure`.

## What extraction is

PARA artifacts (`projects/`, `areas/`, `resources/`) are **extracted from the wiki** (`{wiki}`), not promoted from research notes. The wiki is the living synthesis layer and remains the source of truth; an extracted artifact is a synthesized, human-oriented deliverable pulled from one or more wiki pages at a specific moment in time. (One bounded widening of the *personalization* provenance — for a deliverable that must reflect the user's lived state — is defined in *Personalized extraction* below; it does not open a second PARA write-path, and it does not relax the rule that every method claim traces to a wiki page.)

Research notes in `{research}` are dated snapshots. They rest once complete and are not promoted.

The key distinction: a query returns an answer (optionally filed); a research note records one investigation (dated, rests); a wiki page accretes knowledge across sources (living); an extracted artifact is a deliverable — a curated document shaped for a specific human purpose, pulled from the wiki.

## Personalized extraction — drawing on agent-zone state

A standard extraction's provenance is the wiki and only the wiki. Some deliverables, though, must be **personalized to the user's lived state** — a state the wiki deliberately does not hold, because the wiki is general and reusable (it knows *how spaced repetition works*, not *how this learner is progressing*). Extraction is widened for these by exactly one allowance, with one invariant held hard.

**The hard invariant (unchanged, load-bearing).** Every general or method claim in the body still traces to a wiki page listed in `sources:`. This is the firewall that makes an extracted artifact trustworthy; the amendment does not touch it. Provenance *width* is the soft parameter that moves below; method-grounding is the hard line that does not.

**The soft parameter (the one widening).** *Which files an extraction may additionally draw on for personalization.* A personalized extraction may read a partner's own **agent-zone operational data** (e.g. a progress log under `_agent/`) to tailor the deliverable to the user's situation — the learner's current level, their constraints, what worked last week. To keep the hard invariant legible to a reader **and to a future lint check**, the two provenance roles are **segregated in frontmatter**:

- **`sources:`** continues to list **only wiki pages** — exactly as before, the wiki-provenance audit trail. Every method/general claim in the body maps to an entry here.
- **`personalization_sources:`** is a **separate** list of the agent-zone operational path(s) the extraction drew on for personalization (bare vault-relative paths, per `frontmatter.md` YAML rule 4). Nothing in this list may be the provenance for a method/knowledge claim — it supplies *situation, not fact*.

Because the two roles are distinct fields, "is every method claim wiki-grounded?" stays mechanically checkable: a method claim whose only support is a `personalization_sources` entry is a violation, visible without parsing prose.

**This does not open a second PARA write-path.** The hard boundary stands: PARA is written *only* through extraction — same verb, same supersession/re-extraction model, same filename and trust discipline. The widening is in what a single extraction may *cite for personalization*, not in how artifacts reach PARA.

**Scope of the allowance — bounded, opt-in per operation.** This is **not** a standing license, and **no skill shipped with the module uses it** — the general `vlt-extract` draws on the wiki only. A domain (vertical) partner's operation may use personalized extraction *only* when that operation's own mint **explicitly extends this section to name it** (and is gated accordingly): for example, a progress-tracking op for a domain partner that writes a tailored plan to `areas/<domain>/…`, grounded in the wiki and personalized from a progress log under `_agent/`. Absent such a named, gated extension, an agent-zone path in a `sources:`/`personalization_sources:` field is a violation, not a precedent. The Creative's `vlt-extract` is unchanged — it remains the general wiki→PARA hand and does not use `personalization_sources`.

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
status: <varies by type — project: in-progress, area: ongoing, resource: complete>
sources:
  - <wiki page 1>
  - <wiki page 2>
  - <wiki page N>
# personalization_sources:           # ONLY on a personalized extraction (see that section); omit otherwise
#   - _agent/<operational path>       # agent-zone state for personalization — never a method-claim provenance
---
```

A re-extraction overwrites the artifact in place, so it bumps `last_updated` (never `created`).

`sources:` lists the wiki pages that fed the extraction — the audit trail back into the vault. Every wiki page referenced in the body must appear in `sources:`. The wiki, not any source beneath it, is the provenance layer for extracted content. A *personalized* extraction additionally carries `personalization_sources:` for the agent-zone state it drew on — a **separate** field so the wiki-provenance audit trail stays clean and the method-grounding invariant stays checkable (see *Personalized extraction*).

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

(A personalized extraction follows the same flow, additionally reading the relevant agent-zone state in step 2 and listing it under `personalization_sources:` — not `sources:` — in step 6. No shipped op uses this; a domain op opts in per its gated mint — see *Personalized extraction* above.)

## Re-extraction and supersession

When a wiki topic evolves and an earlier extraction becomes stale, the user may ask for a re-extraction. The skill overwrites the existing PARA artifact in place — the filename is stable.

Re-extraction is a wiki-like edit, not a research-like snapshot: the old artifact is not preserved under a new filename. Substantive claim changes use the same supersession conventions the wiki uses — see `wiki-supersession.md`, specifically the inline `[!superseded]` callout for updated claims.

If the re-extraction is so sweeping that the old artifact is effectively a different document, treat it as a page-level supersession: archive the old artifact to `{archive}/<target>/<filename>.md` and write a new one. This is a judgment call the skill surfaces to the user, not an automatic step.

## Reading list

- `vault-operating-contract.md` — three layers, the `{log}` format, frontmatter pointer
- `wiki-supersession.md` — supersession callouts used by the wiki and by re-extractions
- `frontmatter.md` — the base frontmatter standard and trust ladder
