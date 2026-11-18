---
type: resource
created: 2026-11-18
last_updated: 2026-11-18
title: The wiki's rules
---
# The wiki's rules

The wiki (`resources/wiki/`) is the vault's long-lived reference: one page per concept, each built from several sources and kept current. It is strict so that it can be trusted. This file is the vault's own; change a rule here and it is changed.

## Who writes it

**The wiki is written only by a session running a wiki playbook:** `ingest`, `supersede` or `consolidate` (`resources/playbooks/`). Any session may run them. No session edits a wiki page outside them.

**Every claim traces to a stored source.** A page's `sources:` lists what its claims rest on: files in `sources/`, or research notes. Nothing reaches the wiki from a conversation, from memory or from the web directly; it is stored first, then ingested.

A session that sees something wrong or missing while doing other work files a task on the vault board (`_agent/tasks/`) or writes a research note. The owner may edit a page by hand; the next playbook run on it sets `author: hybrid`.

## A page

- **File name:** kebab-case, no date. The name is the page's identity; other pages link to it.
- **Frontmatter:** the wiki schema in `_meta/frontmatter.md`, with all four attestation keys. A playbook that writes or rewrites a page sets `verified_by:` to its own name and `verified_at:` to today, and bumps `last_updated`.
- **Sections:** Overview (a synthesis across the sources, saying what is uncertain), Key facts and claims (each with its source), Connections (`[[wikilinks]]`), Contradictions and open questions, Sources.
- **One concept, one page.** Before making a page, compare the concept (not only the name) with the pages that exist. A second page for the same idea is the commonest way a wiki rots.
- **New material is woven in,** not appended at the bottom.

## The index

`resources/wiki/index.md` is a map of the wiki's structure, read first before any ingest or query. It is not a catalogue: a page's description is its own `summary:`, and dates and source counts are in its frontmatter.

- **Frontmatter:** `type: index`, `created`, `last_updated`, `title`. No attestation.
- **Categories** are `##` headings: short subject areas in Title Case. A category earns a heading once it holds two pages. These headings are the only legal values of a page's `category:`; renaming one means rewriting `category:` on every page under it in the same edit.
- **A row** is a list item: the page's wikilink and, if it helps, a one- or two-word tag for the page's role in its cluster. No description, no date, no count.

  ```markdown
  ## Coffee Brewing
  - [[extraction-methods]] · hub
    - [[cold-brew]] · slow
    - [[espresso]] · fast
  ```

- **Nesting** puts the pages that hang off a hub under it.
- **Every page has exactly one row,** and every row has a page.
- **A concept linked but not yet written** goes under a last heading, `## Stubs (linked, not yet written)`, as a backtick-wrapped name with a line on why it is linked. It moves to its category when the page is written.

## When a claim changes

A change is always visible. Nothing is silently overwritten.

**A claim is replaced.** The new claim goes in the body, and directly after it:

```markdown
> [!superseded] Claim updated (YYYY-MM-DD)
> **Was:** <old claim>
> **Now:** <new claim>
> **Source:** <what drove the change>
> **Reason:** updated | contradicted | refined | retracted
```

Not for additions, formatting or link fixes: only where a claim would otherwise be deleted or rewritten.

**A claim looks out of date and nothing replaces it yet:**

```markdown
> [!stale] Possibly outdated (YYYY-MM-DD)
> <the claim>
> **Why stale:** <reason>
```

**Two credible sources disagree.** Both pages record it under Contradictions and open questions, and neither picks a winner:

```markdown
> [!contradiction] <short claim> (YYYY-MM-DD)
> **This page:** <what this page claims>
> **[[other-page]]:** <what the other claims>
> **Recency/authority:** <which source is newer or stronger; stated, not acted on>
> **Disposition:** open | adjudicable
> **Closes when:** <adjudicable only: the act that would settle it>
> **Filed:** <adjudicable only: the task that carries it>
```

`open` means the vault holds both views and there is nothing to do. `adjudicable` means one side is wrong or stale and a bounded act settles it; that act is a task on the vault board.

**A name from a machine transcript that collides with what a page already records is not a contradiction.** It is a doubt about the source (`_meta/vault.md`, *Honest reporting and grounding*): keep the claim, leave the name out, record the doubt in the research note.

**A whole page is replaced by another** (split, merged or rethought). The old page gets, in frontmatter:

```yaml
superseded_by: "[[new-page]]"
superseded_date: YYYY-MM-DD
superseded_reason: "<brief>"
```

and at the top of its body:

```markdown
> [!warning] This page has been superseded
> See [[new-page]] — <brief reason>.
```

Then it moves with `git mv` to `_agent/archive/resources/wiki/`, and its index row is removed. Nothing is deleted.

## Checks

`python3 _agent/tools/wiki/check.py` checks three things: attestation keys present, superseded pages point at a page that exists, the index and the folder agree. It does not check whether a claim is true.
