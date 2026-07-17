# Mint Decision Log

_The vault's permanent record of every gated decision — mints, capability changes, convention
edits, stage promotions, upgrade-time rulings, retirements. Institutional memory: it lives in
the agent zone and survives every module upgrade. **Append-only.**_

**Read order.** Faithful append-only writing yields **strict oldest-first** — the first entry
below is the oldest, the last is the newest. A file whose dated headings are **not** in
ascending order has been hand-edited; trust the dates, not the position. Never rewrite an
existing entry to reorder or revise it — supersede it in place (see *Supersession* below).

**Entry shape** (single-homed in `vlt-mint`, *The mint decision log*):

```markdown
## [YYYY-MM-DD] <kind> — <one-line subject>
- kind: mint | capability-change | convention-edit | stage-promotion | upgrade-ruling | retirement
- verdict: <council verdict + reasoning, or `non-boundary: <why>` / `council-none`>
- convention: <name> <old→new>          # convention-edit ONLY — the version delta
<free-form detail: what was decided and why>
```

The `kind:` field is what makes the log mechanically scopable (it is how `vlt-upgrade`'s
reconcile pass finds gated `convention-edit`/`upgrade-ruling` entries with no accounted-for
superseding entry). Entries predating this schema carry no `kind:` and cannot be classified.

**Supersession.** A later ruling never silently overwrites an earlier one. The superseding
entry carries a `supersedes:` pointer at the superseded heading; the superseded entry is marked
**in place** with `superseded_by:` / `superseded_date:` / `superseded_reason:` (mirroring
`wiki-supersession.md` and `spec.md`). The prior decision stays legible.

---

<!-- Worked example below — documentation of the schema + supersession idiom. NOT seeded as
     real history: `vlt-setup` seeds the header only. Uses placeholder tokens, never a live
     vault's artifact paths. -->

## [{earlier-date}] convention-edit — declare {convention} widening unused by shipped ops
- kind: convention-edit
- verdict: council pass — bounded, opt-in; no shipped consumer at the time
- convention: {convention} 1→2
- superseded_by: [{date}] convention-edit — name the shipped op that uses the {convention} widening
- superseded_date: {date}
- superseded_reason: a shipped op does use the widening; the "unused" assertion was false
Original bounded-allowance entry; recorded that no module-shipped op exercised the widening.

## [{date}] convention-edit — name the shipped op that uses the {convention} widening
- kind: convention-edit
- verdict: council pass — naming a module-shipped op in the base is a rule change; consumers re-acked in the same build
- convention: {convention} 2→3
- supersedes: [{earlier-date}] convention-edit — declare {convention} widening unused by shipped ops
Named `{op}` in the base as the one shipped op sanctioned to use the widening; deleted the false
"no shipped op uses it" clause; bumped the rule and re-pinned every consumer's `depends_on` to
`{convention}@3`. Supersedes the earlier entry that asserted the widening had no shipped consumer.
