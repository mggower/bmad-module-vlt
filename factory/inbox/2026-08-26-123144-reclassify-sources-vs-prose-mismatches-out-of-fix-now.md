# Reclassify sources_vs_prose_mismatches out of fix_now, or give it a second legal response

origin: mggower/bmad-module-vlt#12

- **filed:** 2026-08-26 (GitHub issue opened 12:31:44Z via the vlt-feedback rail)
- **origin vault:** vlt-core · **module_version:** 0.16.0 · **rail_contract:** 1 · **kind:** defect
- **materialized:** 2026-08-26 by the factory intake (github-intake)

---

### what_happened

`vlt-lint`'s `sources_vs_prose_mismatches` check is classified under `fix_now` in the report schema, and its stated legal response is "reconcile the prose section to frontmatter `sources:` — frontmatter is the source of truth." That direction assumes the prose `## Sources` section is a *subset* of frontmatter `sources:`.

In practice the divergence usually runs the other way: the prose section cites real sources that frontmatter omits. Applying the stated fix direction in that case does not reconcile anything — it **deletes real provenance**.

Across two consecutive full-mode sweeps on the same mature wiki, the class was surfaced 26 times and then 25 times, and **not one instance was auto-fixable**. Both runs declined the entire class for the same reason and recorded the decline in `fixes_applied`. A `fix_now` class with a 0% application rate across two full sweeps is misclassified: `fix_now` signals "safe to apply serially without judgment," and this one requires a judgment call every time about which side of the divergence is authoritative.

### evidence

Two full-mode runs, ~146 wiki pages each, same corpus.

Run 1: 26 entries, all declined. Run 2: 25 entries, all declined.

The declining rationale recorded in run 2's `fixes_applied`:

> 25 sources_vs_prose_mismatches NOT auto-reconciled — the convention's fix direction (reconcile prose TO frontmatter, frontmatter is source of truth) assumes prose is a subset of frontmatter, and in most of these the divergence runs the other way. Applying the stated direction would delete real provenance.

Representative shapes, generalized:

- A page whose prose `## Sources` section cites **ten** external sources (blog posts, industry reporting, practitioner threads) that do not appear in frontmatter `sources:` at all. The stated fix deletes ten real citations.
- A page whose prose section cites **five** `_agent/{research}/{note}.md` notes absent from frontmatter. Same outcome.
- A page whose prose section cites **three** sources absent from frontmatter, including a direct source URL.
- The inverse and genuinely fixable shape does occur — frontmatter lists a URL that prose names by title only — but it is the minority, and it is cosmetic rather than substantive.

The check text itself is at `references/checks.md`, tier 1, *Sources-vs-prose agreement*; the fix direction is at `references/fix-and-file.md`, Step 3; the report slot is under `fix_now:` in `references/report.md`.

### provenance_guess

**A guess.** The classification looks like it was set from the check's *detectability* (one-file-checkable, so tier 1, so amortizable into writes) rather than from its *remediability*. Tier-1 membership and `fix_now` eligibility are being treated as the same axis, and this class shows they are not: it is cheaply detectable and expensively resolvable.

Candidate fixes, in preference order:

1. Give the check a **second legal response** — "add the missing entries to frontmatter" — and route by direction: prose ⊂ frontmatter is auto-fixable, frontmatter ⊂ prose is `flag_for_human`. This keeps the cheap half automatic.
2. Failing that, move the whole class to `flag_for_human` and drop the `fix_now:` slot.

Either way, the phrase "frontmatter is the source of truth" needs a qualifier: it is authoritative about *what the page claims to rest on*, not about *what the page actually cites*, and the check currently reads it as the latter.

### kind

defect

### origin_vault

vlt-core

### acceptance_vault

A vault with a mature wiki (100+ pages) whose pages carry both frontmatter `sources:` and a prose `## Sources` section — the divergence needs real accumulated citation history to reproduce.

### module_version

0.16.0

### rail_contract

1

