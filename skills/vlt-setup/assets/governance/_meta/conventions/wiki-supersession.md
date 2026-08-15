---
type: note
created: 2026-06-01
last_updated: 2026-07-06
title: Wiki Supersession Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 2
consumers: [vlt-ingest, vlt-lint, vlt-extract, vlt-track, vlt-lint-full.js]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
---

# Wiki Supersession Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/wiki-supersession.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

When new information updates, refines, or contradicts an existing claim in the wiki, the change must be **visible** — never silently overwritten. This is how the wiki maintains intellectual honesty and lets readers see how knowledge has evolved.

Any operation that overwrites existing wiki content reads this file before editing. (These conventions assume Obsidian-style Markdown callouts — see the operating contract's vault-syntax assumption.)

## Claim-Level Supersession (Inline)

When updating a specific claim on a wiki page, place the supersession callout immediately after the updated text:

```markdown
> [!superseded] Claim updated (YYYY-MM-DD)
> **Was:** <old claim>
> **Now:** <new claim>
> **Source:** <what source drove the change>
> **Reason:** updated | contradicted | refined | retracted
```

**Reason values:**
- `updated` — newer data replaces older data (e.g. a 2025 figure replaced by 2026 data)
- `contradicted` — a new source directly conflicts with the old claim; both may still have merit
- `refined` — the old claim wasn't wrong, but the new source adds nuance or narrows it
- `retracted` — the old claim was demonstrably incorrect

**When to use:** any time you would otherwise just delete or overwrite a claim during a wiki page update. The new claim goes in the body text; the supersession callout records what changed and why.

**When NOT to use:** additive updates (new claims that don't replace anything), formatting fixes, or link updates. Only for substantive claim changes.

## Page-Level Supersession (Frontmatter)

When an entire wiki page has been superseded by a different page (a topic was split, merged, or reconceptualized), add to the old page's frontmatter:

```yaml
superseded_by: <new-page-filename>
superseded_date: YYYY-MM-DD
superseded_reason: "brief explanation"
```

And add a visible callout at the top of the old page body:

```markdown
> [!warning] This page has been superseded
> See [[new-page-name]] — <brief reason>.
```

## Stale Claim Markers

When a claim is suspected to be stale (time-sensitive data past its shelf life) but no replacement is available yet, mark it inline:

```markdown
> [!stale] Possibly outdated (YYYY-MM-DD)
> <the claim in question>
> **Why stale:** <reason — e.g. "references 2025 deadline; we're now in 2026">
```

This flags the claim for investigation without removing it. `vlt-lint` surfaces these for resolution.

## Contradiction Callouts (with a disposition)

A contradiction is **two credible claims that cannot both hold** — across two pages, within one page, or between a `{research}` note and the wiki. It is documented in **both** pages' `## Contradictions / Open Questions` section, and never silently resolved by picking a winner.

Documentation alone is not a resolution. Every contradiction callout carries a **disposition** — which kind it is, and, when it is adjudicable, what would close it:

```markdown
> [!contradiction] <short claim> (YYYY-MM-DD)
> **This page:** <what this page claims>
> **[[other-page]]:** <what the other page claims>
> **Recency/authority:** <which source is more recent or more authoritative — stated, not acted on>
> **Disposition:** open | adjudicable
> **Closes when:** <adjudicable only — the bounded act that would settle it>
> **Filed:** <adjudicable only — the `{backlog}` item this was filed as>
```

**Disposition values:**
- `open` — two credible sources genuinely disagree and the vault should hold both. **Documentation is the resolution**; there is nothing further to do and nothing to file. A well-documented disagreement beats false certainty.
- `adjudicable` — one side is simply wrong, or one page is stale, and a **bounded act** closes it. Documentation is a deferral, not a resolution: `**Closes when:**` names the act, and the contradiction is filed to `{backlog}` (`maintenance` when the vault's own pages settle it, `knowledge-gap` when it needs external evidence).

Choosing between them is judgment work and belongs to whoever holds the context — the writer at ingest time, or the human at sweep time. **A callout with no `Disposition:` is not an error**; callouts predating this convention have none, and checks report them as their own third value rather than defaulting them into either bucket (`vault-operating-contract.md`, *Honest reporting*). No sweep backfills them.

## Reading list

- `vault-operating-contract.md` — the operating constitution (three layers, log format, vault-syntax assumption)
- `wiki-consolidation.md` — the merge discipline, which runs under these supersession rules
- `vault-operating-contract.md` — *Honest reporting*: what a check may claim about a disposition it cannot read
- `extraction.md` — re-extractions reuse the inline supersession callout
