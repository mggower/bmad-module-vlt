# Mint Decision Log

_The vault's permanent record of every gated decision — mints, convention edits, upgrade-time
rulings and the rest; the kinds are enumerated once, in the entry schema at
`_meta/conventions/decision-log.md`. Institutional memory: it lives in the agent zone and
survives every module upgrade. **Append-only.**_

**Read order.** Faithful append-only writing yields **strict oldest-first** — the first entry
below is the oldest, the last is the newest. A file whose dated headings are **not** in
ascending order has been hand-edited; trust the dates, not the position. Never rewrite an
existing entry to reorder or revise it — supersede it in place.

**Entry shape.** The entry schema (including the required `ref:` key), the classifiability
tail, and the supersession idiom are single-homed at `_meta/conventions/decision-log.md` —
the convention ships into this vault, so the pointer always resolves. Writers read them
there; do not restate the mechanics here.
