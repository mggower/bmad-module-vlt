---
type: note
created: 2026-07-29
last_updated: 2026-08-24
title: Decision-Log Conventions
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
version: 3
consumers: [vlt-mint, vlt-upgrade, vlt-lint, vlt-ingest]
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
- kind: mint | capability-change | convention-edit | stage-promotion | upgrade-ruling | retirement | deviation
- ref: <governed object>    # e.g. conventions/frontmatter.md | overlays/extraction.overlay.md | capabilities/families/<name> | partners/<name>
- verdict: <verdict> (<provenance>) — <reasoning>   # or `non-boundary: <why>` / `council-none`
- convention: <name> <old→new>          # convention-edit ONLY — the version delta
<free-form detail: what was decided and why>
```

- **`kind:`** makes the log **scopable by class** — it is how `vlt-upgrade`'s reconcile pass finds gated `convention-edit`/`upgrade-ruling` entries with no accounted-for superseding entry. A **`deviation`** licenses a **scoped exception while the governed rule stands unchanged**: its `ref:` names the rule deviated from; it is a **gated** kind (`verdict:` with provenance required, per v2); it carries **no `convention:` line** (that line stays convention-edit ONLY — nothing moved); and it is **outside the reconcile pass's superseding-entry scan by design** — nothing changed, so no superseding entry can or need exist. It stays live until superseded like any entry.
- **`ref:`** names the **governed object**, making an entry findable **by subject**, not only by date — it is the machine key `vlt-lint`'s read-before-flag matches on. It is **required on every new entry**: every entry names a governed object (a mint names the minted thing, a convention edit names the convention, a retirement names the retiree), and a conditional key would re-create the classifiability gap one tier down.

### Verdict provenance (v2)

A **gated** entry's `verdict:` records *how the verdict was reached*, not only what it was — a parenthetical provenance, one of exactly three forms:

- **`(council — lenses: <the workflow's lensesFielded>)`** — the panel workflow was invoked and fielded; the lens list is the workflow's own return, not a recollection.
- **`(council-degraded — <the workflow's note>)`** — the workflow ran but produced a degraded verdict (e.g. no persona lens could be read); carry its `note`.
- **`(user-ruled — panel not fielded: <why>)`** — the council could not be fielded and the **user** explicitly ruled the verdict in the live session. The *why* is **required**, never optional: an entry that cannot say why the panel was not fielded is an improvisation, not a ruling. Only the user may substitute for the panel — a minting context never reviews its own staging (see `vlt-mint`, Step 2a).

Provenance is required on every **new** gated entry from v2 on. `non-boundary:` and `council-none` entries carry none (there was no panel to account for). **No backfill** — append-only means pre-v2 entries without the facet are *pre-facet*, a third honest tier of the classifiability tail, surfaced, never silently swept.

### Subject coherence (v3)

**One entry, one governed subject.** An entry's prose stays on its `ref:` subject; a rule or ruling about a *different* governed object gets its **own entry** under its own `ref:` (or its own home), never a trailing clause. The why lives in the rule itself: every reader that matters resolves by subject — `vlt-upgrade`'s reconcile pass scopes by `kind:`+`ref:`, `vlt-lint`'s read-before-flag matches by `ref:` — so an off-subject trailing clause is unreachable **by construction**; the better the ref discipline, the more invisible the clause.

Applies to every **new** entry from v3 on. **No backfill** — append-only means pre-v3 entries are read as written. The rule is **write-side** — enforced by the rostered write beats (the v2 verdict-provenance posture) — and is *not* covered by the read-before-flag check, which keys on `ref:` only. No new finding class ships with v3; a build that later adds a subject-coherence checker owes that check its own stated legal response.

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
- `vlt-ingest`'s write-through — in-session user rulings on a governance deviation surfaced mid-ingest.

An op outside this roster **never appends**: it surfaces the deviation and the user's ruling, and the record lands through a rostered route — the discovering op where rostered; otherwise `vlt-lint`'s write-through at the next sweep or `vlt-upgrade`'s at upgrade time.

**Readers** — every one derives from the recorded entries:

- `vlt-upgrade`'s reconcile pass — scopes by `kind:`.
- `vlt-lint`'s read-before-flag — matches a governance finding's governed object by `ref:` against **live** entries.

**No inference of rationale, ever:** a reader may *cite* a recorded ruling or *admit absence* — never reconstruct *why* a divergence happened from a diff.

## The honest limit, stated in the rule itself

The memory covers what was **recorded**. A ruling made and never written through is invisible to every reader **by construction** — the log is the only signal, and where the only signal would be the process's own leavings, the state must be recorded, not inferred (the boundary clause on derive-first, `vault-operating-contract.md`, *Honest reporting*). This convention reduces that class — the write-through beats are what feed it — but it does not close it.

## Enforcement

Stage and owner are declared in this file's own frontmatter, per `frontmatter.md` *Enforcement declaration* — `checked`, by `vlt-lint`, at every lint run. The check is the read-before-flag: for each long-lived governance finding, derive exactly one of three states — **`adjudicated`** (a matching live entry exists; cite it), **`undisposed`** (no matching entry), **`unclassifiable`** (the tail above, surfaced in the report's denominator). It **never auto-fixes** — `adjudicated` changes what lint *reports*, never what it writes to the governed files — and its counter (undisposed governance findings) is **derived from the log at each run, never stored**.

There is no deferral: the check exists, its owner is named, and its moment is named, all as of this convention's first version.

The **verdict-provenance rule (v2)** is **write-side** — enforced by the ceremonies that write gated entries (`vlt-mint` Step 2a is the first) — and is *not* covered by the read-before-flag check, which keys on `ref:` only. No new finding class ships with v2; a build that later adds a provenance checker owes that check its own stated legal response.

## Reading list

- `vault-operating-contract.md` — the honest-reporting rule and the derive-first boundary clause the enforcement follows
- `wiki-supersession.md` — the never-silent supersession principle this log's idiom applies
- `frontmatter.md` — the enforcement declaration this file's frontmatter follows
- `spec.md` — the sibling supersession application (structural rewrite as a new file)
