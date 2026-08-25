# Reconcile wiki-index.md's row-format rule with its own worked example — the rule forbids what the example demonstrates

origin: mggower/bmad-module-vlt#4

- **filed:** 2026-08-21 (GitHub issue opened 15:02:12Z via the vlt-feedback rail)
- **origin vault:** app-vault · **module_version:** 0.12.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-08-22 by the factory intake (github-intake)

---

### what_happened

`wiki-index.md`'s *Row format* rule forbids descriptions, and the worked example four lines below it
carries one.

The rule:

> "Each page is one list item: its wikilink, optionally a terse **structural tag**. **No description,
> no source count, no date.**"

The example immediately below:

```markdown
## Coffee Brewing
- [[extraction-methods]] · hub — how grind, time, and pressure shape a cup, split by speed
  - [[cold-brew]] · slow
  - [[espresso]] · fast
```

"how grind, time, and pressure shape a cup, split by speed" is a description. The `structural tag`
bullet does not license it either — a tag is defined there as "a one- or two-word axis label", and
`hub` is already occupying that slot in the same row.

So the convention demonstrates the thing it prohibits, in the same section, and a writer cannot
satisfy both.

This is not academic: the file has two shipped consumers that land on opposite sides. `vlt-ingest`
writes index rows and `vlt-lint` validates them, so the ambiguity resolves per-run rather than
per-convention. In practice the example wins — a vault following the example ends up with every
category in violation of the prose, or vice versa, with no way to tell which is the defect.

### evidence

`_meta/conventions/wiki-index.md`, section *Row format — structure, not description*. The prohibition
and the example are four lines apart in the same section; the structural-tag bullet defining the only
permitted suffix is directly below the fence.

Observed downstream in a 16-category index: every category followed the **example** form, making the
whole file non-conformant to the prose rule. The divergence was recorded rather than silently
resolved, precisely because there is no principled way to pick from the shipped text.

Either reading is implementable — the ask is that the module state which one is the rule:

- **Example is right** — rows may carry a short description; the prose should say so and bound it.
- **Prose is right** — the example is wrong and should be rewritten to tags only, and existing
  indexes need a stated migration (`vlt-lint` would then flag description-bearing rows).

### provenance_guess

**A guess — please ground it.** The fix is in `assets/governance/_meta/conventions/wiki-index.md`
alone; no code change is implied by either resolution. Whichever way it goes, `version:` bumps and the
`consumers:` walk covers `vlt-ingest` and `vlt-lint`.

Worth checking while in there: whether `vlt-lint` currently has any check on row format at all. If it
does not, then "the prose is right" is unenforced today and would need a check to ship with it, per
the enforcement-ships-with-widening rule.

### kind

defect

### origin_vault

app-vault

### acceptance_vault

Any vault with a populated wiki index. Expected after fix: the rule and the worked example agree, and
a reader can determine conformance from the file alone.

### module_version

0.12.0

### rail_contract

1
