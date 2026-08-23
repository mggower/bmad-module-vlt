# Supply write-verification.md to the lint fan-out scanner — Gap B is asked unconditionally and misfires on 88% of pages

origin: mggower/bmad-module-vlt#3

- **filed:** 2026-08-21 (GitHub issue opened 14:45:54Z via the vlt-feedback rail)
- **origin vault:** app-vault · **module_version:** 0.12.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-08-21 by the factory intake (github-intake, first live run)

---

### what_happened

The full-mode lint fan-out asks every page scanner to judge Gap B (frontmatter `sources:` vs the
prose `## Sources` section) **unconditionally**, but the convention that governs Gap B scopes it
**conditionally** — and that convention is not among the files the scanner is told to read.

`write-verification.md`, tier-1 per-artifact-kind, wiki page:

> "**where the page carries** a prose `## Sources` section, it agrees with frontmatter `sources:` —
> every entry in one is traceable in the other (frontmatter is the source of truth; **a page with no
> prose section is conformant**)."

`workflows/vlt-lint-full.js`, `pageScanPrompt`, asks for:

> "whether the frontmatter `sources:` and the prose Sources section diverge (Gap B)"

with no carve-out for a page that has no prose section. The scanner's convention-read list is
`frontmatter`, `wiki-supersession`, `wiki-index` — `write-verification.md` is **never supplied**, so
the scanner has no way to know the rule it is applying has a precondition. It reports every
frontmatter-only page as a divergence.

The result is not a cosmetic mislabel: it is a bulk false-positive class that makes the check
untrustworthy at exactly the scale full mode exists for.

### evidence

From a real `--full` sweep over a 56-page wiki:

```
25 findings in the sources-vs-prose class
  3 genuine mismatches
 22 dismissed as false positives  (88%)
```

The 22 were pages whose frontmatter `sources:` has no prose `## Sources` counterpart — which
`write-verification.md` declares conformant. Only 25 of the 56 pages carry a prose section at all, so
the unconditional ask misfires on most of the corpus by construction. Recorded vault-side in
`_agent/lint-reports/{date}-lint.md`.

Note the second-order cost: a reviewer who learns that this class is ~88% noise stops reading it, and
the 3 real mismatches are what get lost.

### provenance_guess

**A guess — please ground it.** Two candidate fix sites in `workflows/vlt-lint-full.js`:

1. Add `write-verification` to the scanner's `convRead(...)` list, so the merged rule (base plus any
   overlay) reaches the agent judging against it. This looks like the root cause — a scanner is being
   asked to enforce a convention it was never handed.
2. Scope the ask in `pageScanPrompt` itself: request the Gap B verdict only where a prose `## Sources`
   section exists, and have the scanner return "no prose section" as a distinct third value rather
   than folding it into "diverge".

(1) alone may be sufficient and is the more general fix — but (2) makes the tri-state explicit at the
schema level instead of relying on the scanner to infer it, which matters when the reduce step counts
findings.

Worth a general check beyond this instance: whether any other shipped check asks a fan-out scanner to
judge a rule whose governing convention is absent from that scanner's read list. The pattern — the
enforcing agent not being given the rule — would produce exactly this failure shape anywhere it
recurs.

### kind

defect

### origin_vault

app-vault

### acceptance_vault

Any vault with a wiki where some pages carry a prose `## Sources` section and some do not — the
mixed corpus is what exposes it. Expected after fix: frontmatter-only pages produce no Gap B finding.

### module_version

0.12.0

### rail_contract

1


