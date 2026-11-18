# Add a kind: value for a scoped deviation — forcing it to convention-edit mis-scopes the reconcile pass

origin: mggower/bmad-module-vlt#7

- **filed:** 2026-08-21 (GitHub issue opened 15:02:15Z via the vlt-feedback rail)
- **origin vault:** app-vault · **module_version:** 0.12.0 · **rail_contract:** 1 · **kind:** candidate
- **materialized:** 2026-08-22 by the factory intake (github-intake)

---

### what_happened

`decision-log.md`'s `kind:` enumeration has no value for a **scoped deviation** — a one-off ruling
that permits an exception while leaving the governing rule fully intact.

The vocabulary:

```
- kind: mint | capability-change | convention-edit | stage-promotion | upgrade-ruling | retirement
```

All six presuppose the governed object *changed*. `mint` creates, `capability-change` and
`convention-edit` alter, `stage-promotion` advances, `retirement` removes, and `upgrade-ruling` is
scoped to upgrade time. None covers "the rule stands unchanged; this one instance is licensed."

This is not cosmetic, because `kind:` is a machine key. The convention says so:

> "**`kind:`** makes the log **scopable by class** — it is how `vlt-upgrade`'s reconcile pass finds
> gated `convention-edit`/`upgrade-ruling` entries with no accounted-for superseding entry."

So a deviation forced into `convention-edit` is not merely untidy — it enters the reconcile pass's
scope as a convention edit, and the pass will look for a superseding entry for a convention that was
never edited. The mis-class propagates into a shipped consumer's behavior.

### evidence

Observed workaround in a real vault: a scoped deviation was logged as `convention-edit` — the
least-wrong available key — with the `convention:` delta line written as **unchanged** to signal that
no version moved. That line is defined by the schema as "convention-edit ONLY — the version delta", so
the workaround required using a required field to say the opposite of what it is for.

The entry's own text had to carry the disambiguation in prose ("a scoped deviation, not an edit; the
rule stands at full force for every other case") because the schema had no way to express it
structurally.

### provenance_guess

**A guess — please ground it.** Two resolutions:

1. **Add a value** — e.g. `deviation` (or `ruling`) to the `kind:` enumeration, with a stated
   relationship to the reconcile pass: a scoped deviation presumably does *not* need a superseding
   entry, since nothing was changed to supersede.
2. **State that `convention-edit` covers it** — if that is the intent, say so in the convention and
   define what `convention:` carries when nothing moved, so the `unchanged` idiom becomes contract
   rather than improvisation.

(1) looks cleaner given the machine-key role, but (2) is cheaper and may be right if scoped deviations
are meant to be rare. Either way the reconcile pass's scoping rule needs to say which classes it
matches, since that is where the mis-class currently lands.

Adding an enumeration value is additive; per the frontmatter rules this is still a base rule change
and would carry the `version:` bump and consumer walk.

Related, same file: the writer-roster gap filed separately. Same shape — a closed enumeration with no
value for a legitimate real case — different field and different consumer.

### kind

candidate

### origin_vault

app-vault

### acceptance_vault

Any vault that rules a one-off exception without amending the rule. Expected after fix: the entry has
a `kind:` that does not misrepresent it to the reconcile pass.

### module_version

0.12.0

### rail_contract

1
