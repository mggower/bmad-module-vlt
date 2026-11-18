---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: Frontmatter
---
# Frontmatter

The keys a note carries, by type. This file is the vault's own: add a type or a key here when the vault needs one.

## Syntax

1. **Flat.** No nested maps. A list holds plain strings.
2. **Quote wikilinks.** `superseded_by: "[[page]]"`, never bare.
3. **Quote any string with a colon, a leading dash or a leading bracket.** No block scalars.
4. **A key lives in one place.** A value in frontmatter is not repeated in the body.

## Base keys

Every note a session writes:

```yaml
type: <the note's kind>
created: YYYY-MM-DD        # never changed after the first write
last_updated: YYYY-MM-DD   # only on notes that keep changing; bumped on each real edit
title: <readable title>
```

`type:` is an open set. The values with a schema below are `wiki`, `research`, `session`, `record` (a task) and the zone kinds `project`, `area`, `resource`. `moc` marks a Map of Content.

## Attestation

Required on **wiki pages and research notes**. Optional anywhere else.

```yaml
author: agent | human | hybrid
trust: draft | reviewed | verified | canonical
verified_by: <the playbook that wrote the note: ingest, supersede, consolidate, research, query>
verified_at: YYYY-MM-DD
```

- **`author`**: `agent` for a session's own writing, `human` for the owner's, `hybrid` once the owner has edited an agent's draft.
- **`trust`**: a session writes `draft`. Only the owner raises it: `reviewed` (read and accepted), `verified` (key claims checked against primary sources), `canonical` (safe to link from a MOC). Notes written before this file may carry `raw`; it means `draft`.
- **`verified_by` / `verified_at`**: which procedure wrote or last rewrote the note, and when. An edit through a playbook bumps both. It records how the note was made, not that its claims are true.

## Review in PARA

A document in a zone that the owner must read before it is used or published carries one key:

```yaml
review: requested     # set by the session that wrote it
review: approved      # set by the owner, and only by the owner
```

A zone can ask for this on everything written in it, with `review_default: requested` in its `README.md`. `_agent/bases/review.base` lists every note waiting.

A document with no `review:` key and no zone default needs no review.

## By type

### Wiki page (`resources/wiki/`)

Base keys with `last_updated`, attestation, and:

```yaml
type: wiki
summary: "<one line, at most 160 characters: what the page covers>"
category: <one subject area; must be a heading in the wiki index>
topic: [<broad>, <narrower>]      # lowercase, general to specific
status: draft | in-progress | complete
sources: ["[[sources/...]]"]      # every source the page's claims rest on
review_after: YYYY-MM-DD          # optional; absent means the content does not expire
```

The rules for the index, supersession and consolidation are in `_meta/wiki.md`.

### Research note (`_agent/research/`)

Base keys without `last_updated` (written once), attestation, and:

```yaml
type: research
topic: [<broad>, <narrower>]
status: draft | in-progress | complete
sources: [<paths and URLs>]
```

### Session note (`_agent/sessions/`)

```yaml
type: session
created: YYYY-MM-DD
title: Session — YYYY-MM-DD HH:MM — <subject>
zone: <the zone worked in, or vault>     # optional
```

Written once, at the end of the session. No attestation.

### Playbook (`resources/playbooks/`)

`type: resource`, the base keys, and the index keys (`need`, `state`, `domain`, `tools`, `companion`, `companion_of`). They are defined in `resources/playbooks/README.md` and not repeated here.

### Task (`<zone>/tasks/`, `_agent/tasks/`)

`type: record`, and the board keys (`key`, `status`, `summary`, and the rest). They are defined in `resources/playbooks/task-board.md` and not repeated here.

### Zone README (`<zone>/README.md`)

```yaml
type: project | area | resource
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
title: <the zone's name>
writers: any | owner              # optional; absent means any session may write here
review_default: requested         # optional; see Review in PARA
subs: [<the zone's sub-areas>]    # optional; the values a task's sub: may take
```
