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
version: 1
consumers: [vlt-ingest, vlt-lint, vlt-extract, vlt-track]
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

## Reading list

- `vault-operating-contract.md` — the operating constitution (three layers, log format, vault-syntax assumption)
- `wiki-consolidation.md` — the merge discipline, which runs under these supersession rules
- `extraction.md` — re-extractions reuse the inline supersession callout
