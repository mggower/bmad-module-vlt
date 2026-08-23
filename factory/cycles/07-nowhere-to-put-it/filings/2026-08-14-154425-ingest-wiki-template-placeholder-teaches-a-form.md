# `vlt-ingest`'s wiki template shows `sources:` in a form-neutral placeholder — templates teach shape, and this one teaches the wrong one

_Filed 2026-08-14 from **vlt-core**, alongside the wiki-`sources:` wikilink candidate
(`2026-08-14-154424`). Evidence is module source, read-only. Classification: **candidate** — minor, and
deliberately filed as minor after an earlier reading of it was checked and found overstated._

## The claim

`vlt-ingest/SKILL.md:147` emits the wiki-page frontmatter template with:

```yaml
sources:
  - <every source that has contributed>
```

The placeholder specifies **no form**. That is defensible in isolation, and the skill is properly bound
to the merged convention at line 26:

> **Read the conventions you will obey** before writing anything: `{conventions}/frontmatter.md` and
> `{conventions}/wiki-supersession.md` … read each together with its `{overlays}/{name}.overlay.md` if
> present, honoring the overlay's appended rules. These govern every write; honor them exactly.

So a correct run resolves the placeholder against the convention and there is no defect in the binding.
The residual risk is narrower and worth naming precisely: **an agent copying the placeholder's *shape*
rather than resolving it.** A template sitting inline in the skill is the most concrete thing in the
agent's context at write time, and concrete beats a rule read forty lines earlier.

## Why this is filed as minor, and the correction that got it there

An earlier review in the same session called this a **treadmill** — the op producing wiki pages
emitting a violation on every run, so the rule could never converge. Checked directly, that is
overstated: the placeholder is form-neutral rather than a bare path, and line 26's binding is explicit
and strong ("honor them exactly"). Recording the correction because a filing that over-asserts is worse
than one that under-asserts, and the factory re-grounds every claim anyway.

## Suggested fix

If the wiki-`sources:` wikilink candidate (`2026-08-14-154424`) is accepted, show the resolved form in
the template directly rather than a neutral placeholder:

```yaml
sources:
  - "[[sources/articles/<source-basename-without-extension>]]"
```

Generally: where a template's field has a form the convention constrains, the template should **show**
the form. A placeholder that hides it converts a convention rule into a per-run judgment call, and
per-run judgment calls are where drift enters.

## Provenance guess — marked as a guess

The placeholder likely predates any form constraint on `sources:` — with rule 4's bare-path default in
force, `- <every source that has contributed>` was fully specified by the base and needed to say nothing
more. It only becomes under-specified once a schema-level override exists. **Inference from the file; no
history read.**

## What acceptance should check

Nothing on its own — this rides whatever build takes `2026-08-14-154424`. If that candidate is declined,
this one is moot and should be archived with it.
