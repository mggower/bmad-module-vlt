# The ruleset fingerprint's inputs are under-specified, and a defensible reading fails silently

_Filed 2026-09-01 from **`{field-vault}`**, on the sweep that produced the vault's **first warm cache
run** (`{lint_reports}/2026-09-01-1406-lint.yaml`, module 0.17.1). Reported by the operator of that
run; every fact below re-verified against the persisted report. Evidence is `{field-vault}`,
read-only._

⚠ **Sibling of `2026-09-01-093000`** (the fingerprint is *over-broad*: `module_version` guarantees a
cold sweep per release). **This filing is a different cause with a different fix:** the fingerprint's
inputs are *under-specified*, so a correct-looking run silently produces a cold sweep with **no
release involved at all**. Capture may brief them together; they are not the same defect.

## The claim

`skills/vlt-lint/references/full-scale.md` step 2 tells the SKILL to compute **`rulesetComponents`**
and pass four named slots to the workflow. For the two **digest** slots it is exact — instrument
(`shasum -a 256`), merge order (base then overlay), encoding (UTF-8, no normalization), truncation
(first 16 hex, lowercase) — and it says why that precision exists: *"an executor that follows them
lands on the same value every run, **which is the property that failed**."*

**The two component slots get no such treatment, and both were read wrongly in the field on the first
attempt.** The composition is an exact match, so a wrong reading does not degrade — it silently yields
a fingerprint that matches nothing.

**Slot 1 — `pin_vector`, described as *"this skill's own `depends_on:` pins, verbatim."*** The
operator passed the pins as a **JSON array**, which is a fair reading of *verbatim* for a list-valued
frontmatter key. `vlt-lint-full.js` requires `typeof v === 'string'`, so the slot **read as missing**,
the fingerprint composed as `''`, and **all 146 pages became uncacheable**.

**Slot 2 — `convention_digests`, described as *"one entry per convention this run judges against."***
The operator read that as the **8** conventions named in the pin vector. The value the workflow
expects is **all 9 files in `{conventions}`** — `wiki-consolidation` is judged (convention coherence,
enforcement doctrine) **without being pinned**, so "judges against" and "pins" are not the same set,
and the phrase does not say which one it means.

**Corrected, the recomposed fingerprint reproduced the sidecar's recorded key half
`bd6e1e211804a2011af` exactly and 141/146 pages reused.** The mechanism is sound; only its
specification is not.

## Why this is the expensive one

**The failure is silent by construction.** A cold run caused by a mis-rendered slot is **indis­tinguishable
from a correct first-run-after-release**: same `files_cached: 0`, same honest cold-branch reason. The
one surface that could disambiguate does not — `full-scale.md` says *"any slot missing or empty is a
cold sweep with the absent slots named in `coverage_caps`"*, which names **which slot was absent** but
never **that the operator's rendering was wrong**, because from the workflow's side those are the same
event.

⚠ **This plausibly explains why the cache had never once worked in this vault.** The findings cache
shipped in v0.17.0 (Cycle 14 build-2, repairing Cycle 12's `b2(5)` which shipped broken and undetected
for three cycles). Its acceptance check (8) went unfired through three discharge runs. The first
sweep to attempt reuse (2026-08-30) was cold — correctly, no sidecar existed. **The second attempt was
cold for this reason**, and only a hand-debugged re-render made it warm. A vault following the doc as
written gets a permanently cold cache and a report that says nothing is wrong.

**Measured cost of the difference, from the two reports' own `cost_accounting`:**

| | 2026-08-30 (cold) | 2026-09-01 (warm) |
|---|---|---|
| Scan-page agents | **146** | **5** |
| Scan-page prompt chars | **591,152** | **20,294** |
| total dispatches | 172 | 31 |

**A 96% reduction on the scan phase, gated behind a sentence's ambiguity.**

## The fix the field already identified

State the two component slots' **exact rendering** the way the digest steps are already stated:

1. **`pin_vector`** — name the rendering (the JSON-array serialization of the `depends_on:` list, or
   whatever the workflow in fact requires) rather than *"verbatim"*, which is ambiguous for a
   list-valued key.
2. **`convention_digests`** — *"one entry per file in `{conventions}`"*, not *"per convention this run
   judges against."* The two sets differ by `wiki-consolidation` today and will differ again whenever a
   convention is judged without being pinned.

⚠ **A second-order direction worth capture's attention:** make a wrong rendering **loud** rather than
merely making the right one documented. A slot that is present but of the wrong *type* is a different
event from a slot that is absent, and the workflow can tell them apart (`typeof v === 'string'`
already distinguishes them — it simply discards the distinction). Surfacing *"slot `pin_vector` was
present but not a string"* would have made this a five-minute fix rather than a silent cold sweep,
and it is the honest-degradation posture `full-scale.md` already takes everywhere else.

## Grounding

- `skills/vlt-lint/references/full-scale.md`, step 2 — the four slots, the exact digest steps, the
  two under-specified descriptions, and the `coverage_caps` degradation clause.
- `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the `typeof v === 'string'` requirement and
  the composition (single-homed there; `full-scale.md` supplies inputs).
- `{lint_reports}/2026-09-01-1406-lint.yaml:240` — the warm run's `lint_cache` line, which records the
  discarded first attempt and both mis-renderings verbatim.
- `{lint_reports}/2026-08-30-1123-lint.yaml:232` — the cold predecessor that wrote the sidecar.

_Ship-verifiable at rest: a repair is gradeable by rendering both slots per the corrected text and
asserting the composed fingerprint matches a recorded sidecar key — no field event needed._
