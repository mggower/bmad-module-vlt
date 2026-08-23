# `new partner` fields one lens — the roster's highest-stakes mint gets the module's thinnest panel

**Filed from:** `vlt-core` (installed vault, module 0.6.0)
**Found by:** the Chess Coach mint (2026-07-16), after two council rounds returned a single lens and the
second round's moderator flagged that three claims had gone untested for the second time.
**Confidence:** high — this is a config read, verified against three mints' records. (Stated plainly
because an earlier filing from this vault today asserted a mechanism it had not checked; that filing has
been withdrawn. This one is a `grep` of a literal.)

---

## 1. The defect

`workflows/vlt-review-council.js`, `KIND_PANEL` (line 54ff):

```js
'add a capability':          ['architect', 'skeptic', 'pragmatist'],   // gated case only
'change family invariants':  ['architect', 'skeptic', 'pragmatist', 'historian'],
'new partner':               ['architect'],                             // <-- one lens
'persona self-edit':         ['architect', 'skeptic', 'pragmatist', 'historian'],
'convention edit':           ['architect', 'skeptic', 'pragmatist', 'historian'],
'retire a partner':          ['architect'],                             // <-- one lens
```

**The two kinds that permanently change who is on the roster field the thinnest panels in the map.**
Editing an existing partner's voice (`persona self-edit`) convenes four lenses. *Creating a whole new
partner* — a persona that ships, joins the roster, carries a non-negotiable, and outlives everyone's
memory of the mint — convenes one. Retiring one likewise.

The asymmetry is hard to read as intentional: a `persona self-edit` is a subset of what a `new partner`
decides (the self-edit changes a persona; the mint *invents* one, plus its distinctness, its capabilities,
its lane, and its non-negotiable). If the four-lens panel is right for the subset it cannot be excessive
for the superset.

## 2. Evidence it bites — three consecutive partner mints, all noticed, none fixed

The condition is **already recorded twice in this vault's own decision log**, by the mints it degraded:

- **Health Coach mint** (`_agent/mint/decision-log.md:42ff`) — noted the single-lens fielding.
- **Chef mint** (`decision-log.md:70ff`) — *"the `new partner` `KIND_PANEL` is **`['architect']` by
  design** — a single-lens fielding (`lensesFielded: ["architect"]`), same condition the Health mint
  noted; here it is the designed panel, not a degradation."*
- **Chess Coach mint** (2026-07-16, this one) — two rounds, one lens each.

Three partners in, every mint has written the same caveat and moved on. **A defect that every victim
documents and nobody can fix from inside is a module problem, not a vault problem.**

## 3. Why it actually mattered here (the concrete cost)

The Chess Coach mint put eight claims to the council. Round 1's architect **explicitly ceded claim 2 to
the skeptic** ("is this non-negotiable one testable gate or two rules in a trenchcoat?"). Round 2 was
convened *specifically* to field the skeptic — the prompt said so in capitals. The skeptic could not
field, because `mint` mode takes its lenses from `KIND_PANEL` and the caller cannot widen it:

```js
if (mode === 'mint') {
  lenses = KIND_PANEL[kind].slice()      // caller's `lenses` is ignored in mint mode
} else {
  lenses = Array.isArray(a.lenses) && a.lenses.length ? a.lenses.slice() : [ ...full panel ]
}
```

So three claims — the partner's **non-negotiable framing**, its **evidence honesty** (its entire
character rests on a `trust: raw` single-source vendor-run survey), and its **v0 sufficiency** — went
untested across two rounds and ~206k subagent tokens. The vault's workaround was to re-ask them in
**`debate` mode**, which *does* default to the full panel and *does* honor a caller-supplied `lenses`.
That works, but it means **the way to get a real panel on a new partner is to not tell the council it's
reviewing a mint** — which is a strange shape for a governance tool.

## 4. Exact change to ship

**A. `workflows/vlt-review-council.js` — `KIND_PANEL`:**

```js
'new partner':      ['architect', 'skeptic', 'pragmatist', 'historian'],
'retire a partner': ['architect', 'skeptic', 'pragmatist', 'historian'],
```

Rationale per lens, for `new partner` specifically — each has a question no other lens asks:
- **skeptic** — is the non-negotiable one testable gate or two rules wearing a trenchcoat? Is the
  grounding strong enough to carry a *non-negotiable* rather than a strong prior?
- **pragmatist** — does the partner survive contact with a real user, or does it defer/stall at exactly
  the moment it's wanted?
- **historian** — does this vault have precedent for this shape, and what did the last three mints learn?
  (This is the lens that would have caught the Chess Coach mint's fabricated root cause *immediately* —
  it is the only lens whose job is to read the record.)
- **architect** — structure, lanes, distinctness. The one lens that does field.

If the single-lens config was a deliberate cost-control choice, it is optimizing the wrong axis: a partner
mint is rare (four in this vault's lifetime) and permanent. The `add a capability` gated path — far more
frequent, far more reversible — already spends three lenses.

**B. Consider letting `mint` mode honor a caller-supplied `lenses` as a *widening* only** (never a
narrowing — a caller must not be able to dodge the gate by requesting one friendly lens). Then a mint that
knows it has a contested axis can convene the lens that owns it, instead of laundering the question
through `debate` mode.

**C. If (A) is rejected, at minimum make the thin panel loud.** The workflow should return a warning in
its verdict when a gated kind fields fewer than the full panel — something the moderator must surface —
rather than leaving each mint to notice and write its own caveat. Three mints wrote the caveat; nothing
aggregated it.

## 5. Open question for the maintainer

Was `['architect']` for the roster-changing kinds a deliberate cost decision, or a stub that was never
filled in? The decision log's phrasing (*"by design"*) is a vault author's inference from reading the
config — **not** a citation of any module-side rationale. Nobody here knows, and the file carries no
comment explaining it while the neighbouring entries carry detailed ones. If it was deliberate, the
reasoning deserves a comment on the line; if it was a stub, it has been silently thinning the review of
every partner this module has ever minted.
