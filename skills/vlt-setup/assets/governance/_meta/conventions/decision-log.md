---
type: note
created: 2026-07-29
last_updated: 2026-07-29
title: Decision-Log Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 1
consumers: [vlt-mint, vlt-upgrade, vlt-lint]
enforcement_stage: checked
enforcement_checked_by: vlt-lint
enforcement_moment: lint run
adoption_first_instance: null        # stamped by the first authorized-ceremony ref-keyed entry — vlt-lint never writes it
---

# Decision-Log Conventions

> **Overlay note:** This is the pristine base (overwrite-safe on upgrade). A vault's local additions live in `{overlays}/decision-log.overlay.md`, read together with this file — **append-only**. See the operating contract, *Durability across upgrades*. Edit the overlay for a vault-local addition; edit this base only for a generic rule change bound upstream.

The **mint decision log** is the vault's permanent, upgrade-durable record of every gated decision — mints, capability changes, convention edits, stage promotions, upgrade-time rulings, retirements. This file single-homes its mechanics: the entry schema (including the `ref:` machine key), the classifiability tail, and the supersession idiom. Every writer appends in this shape and every reader derives from it; both point here rather than restating.

## What the log is and where it lives

The log lives at `_agent/mint/decision-log.md` — the agent zone, which no upgrade ever overwrites, so the institutional record survives every module refresh (a log kept inside a skill directory would be clobber-prone; the *legacy relocation migration* that moves such a log home is an operational beat owned by `vlt-mint`/`vlt-upgrade`, not part of this schema). `vlt-setup` seeds the log header-only from `vlt-mint`'s template when it is absent, never overwriting an existing log.

## Append-only + read order

The log is **append-only**. Faithful appending yields **strict oldest-first** — the first entry is the oldest, the last the newest. A file whose dated headings are out of ascending order has been hand-edited; trust the dates, not the position. Never rewrite an existing entry to reorder or revise it — supersede it (see *Supersession idiom* below).

## Entry schema

Each entry is a dated block:

```markdown
## [YYYY-MM-DD] <kind> — <one-line subject>
- kind: mint | capability-change | convention-edit | stage-promotion | upgrade-ruling | retirement
- ref: <governed object>    # e.g. conventions/frontmatter.md | overlays/extraction.overlay.md | capabilities/families/<name> | partners/<name>
- verdict: <council verdict + reasoning, or `non-boundary: <why>` / `council-none`>
- convention: <name> <old→new>          # convention-edit ONLY — the version delta
<free-form detail: what was decided and why>
```

- **`kind:`** makes the log **scopable by class** — it is how `vlt-upgrade`'s reconcile pass finds gated `convention-edit`/`upgrade-ruling` entries with no accounted-for superseding entry.
- **`ref:`** names the **governed object**, making an entry findable **by subject**, not only by date — it is the machine key `vlt-lint`'s read-before-flag matches on. It is **required on every new entry**: every entry names a governed object (a mint names the minted thing, a convention edit names the convention, a retirement names the retiree), and a conditional key would re-create the classifiability gap one tier down.

## The classifiability tail

The historical tail is stated honestly, in **two tiers**:

- An entry with **no `kind:`** is **pre-schema** — unclassifiable at all.
- An entry with **`kind:` but no `ref:`** is **post-schema-pre-key** — scopable by class, **unaddressable by subject**.

Both tiers are permanent (append-only means **no backfill** — never rewrite an old entry to add the keys), and both are **surfaced, never silently swept**: they are what the read-before-flag reports as `unclassifiable`, and what the upgrade-time reconcile surfaces one-time as cannot-classify.

## Supersession idiom

The log is append-only, so a changed disposition is a **new entry**: the superseding entry carries `supersedes:` (a pointer at the superseded entry's heading), and the superseded entry is marked **in place** with `superseded_by:` / `superseded_date:` / `superseded_reason:`. The prior decision stays legible; the change is visible. A **live** entry is one no later entry supersedes — the read side's match target.

This is the **third application of the never-silent supersession principle**, whose single home is `wiki-supersession.md`: a superseding record points at what it supersedes, the superseded record is marked in place, and the prior stays legible. Wiki pages apply it as per-claim callouts; specs apply it as structural-rewrite-as-new-file (`spec.md`, *Supersession rules*); this log applies it as append-only entry markers. One principle, three artifact-grain-appropriate mechanics — the convergence is **complete, not deferred**.

## Writers and readers (the roster the handshake protects)

**Writers** — every one appends in the schema above and points here for the shape (single-home):

- `vlt-mint`'s ceremonies — gated mints, stage promotions, the self-grow one-liner.
- `vlt-upgrade`'s write-through — upgrade-time rulings.
- `vlt-lint`'s write-through — lint-time rulings on governance findings.

**Readers** — every one derives from the recorded entries:

- `vlt-upgrade`'s reconcile pass — scopes by `kind:`.
- `vlt-lint`'s read-before-flag — matches a governance finding's governed object by `ref:` against **live** entries.

**No inference of rationale, ever:** a reader may *cite* a recorded ruling or *admit absence* — never reconstruct *why* a divergence happened from a diff.

## The honest limit, stated in the rule itself

The memory covers what was **recorded**. A ruling made and never written through is invisible to every reader **by construction** — the log is the only signal, and where the only signal would be the process's own leavings, the state must be recorded, not inferred (the boundary clause on derive-first, `vault-operating-contract.md`, *Honest reporting*). This convention reduces that class — the write-through beats are what feed it — but it does not close it.

## Enforcement

Stage and owner are declared in this file's own frontmatter, per `frontmatter.md` *Enforcement declaration* — `checked`, by `vlt-lint`, at every lint run. The check is the read-before-flag: for each long-lived governance finding, derive exactly one of three states — **`adjudicated`** (a matching live entry exists; cite it), **`undisposed`** (no matching entry), **`unclassifiable`** (the tail above, surfaced in the report's denominator). It **never auto-fixes** — `adjudicated` changes what lint *reports*, never what it writes to the governed files — and its counter (undisposed governance findings) is **derived from the log at each run, never stored**.

There is no deferral: the check exists, its owner is named, and its moment is named, all as of this convention's first version.

## Reading list

- `vault-operating-contract.md` — the honest-reporting rule and the derive-first boundary clause the enforcement follows
- `wiki-supersession.md` — the never-silent supersession principle this log's idiom applies
- `frontmatter.md` — the enforcement declaration this file's frontmatter follows
- `spec.md` — the sibling supersession application (structural rewrite as a new file)
