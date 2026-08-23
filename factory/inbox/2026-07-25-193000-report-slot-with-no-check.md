# `sources_vs_prose_mismatches` is a report slot no check ever fills

_Filed 2026-07-25 from the **factory**, not from a vault. Found while building A4-1
(`skills/reports/build-A4-1-linkage-polarity.md`, Out of scope) — the brief observed it, ruled it
off-brief, and recommended filing so it enters the loop as an ordinary filing rather than being
fixed unbriefed. Owner elected to file (build-time ruling, 2026-07-25)._

## The claim

`vlt-lint`'s Step-5 report block declares a `fix_now` key that **no Step-2 check defines**. The slot
is emitted-shaped but unreachable: nothing in the SKILL ever computes a value for it, so it can only
ever render empty — and an always-empty slot reads to a consumer (human or dashboard) as *"checked,
nothing found"*.

## Grounding

- `skills/vlt-lint/SKILL.md:128` (pre-A4-1 numbering; `:137` after) — the slot:
  ```yaml
    sources_vs_prose_mismatches: [<page: frontmatter sources: vs prose Sources diverge>, ...]
  ```
- Step 2 read in full (`:55-88` pre-A4-1) during A4-1 brief grounding: **no check** produces this
  finding. Tier 1 covers missing targets, frontmatter/Bases drift, attestation, `review_due`; tier 2
  covers orphans, staleness, contradictions, supersessions, near-duplicates, thin pages, index drift,
  and the governance checks. None compares a wiki page's frontmatter `sources:` against its prose
  `## Sources` section.
- Verified still true after A4-1 landed (A4-1 changed the `linkage_ripe` slot's description only,
  disposition 6 — no report-line work).

## Why it matters

Two axes, and they are different sizes:

1. **The honest-reporting axis (the general one).** This is an instance of the silent-zero class
   A4-2 already owns — a report line that cannot distinguish *"ran and found nothing"* from *"never
   ran"*. Worse than the usual instance, because here the check does not exist at all. **Do not brief
   a bespoke fix for this line**; the Arc-4 decide-once ruling is that ONE general rule (A4-2) governs
   the class and every site cites it. If A4-2's rule covers this slot, the honesty half closes for
   free.
2. **The missing-check axis (the specific one).** Separately from honesty: *should* the check exist?
   The A4-1 spike established the underlying signal is real and load-bearing on the **research** side
   — a wiki page cites research notes in its frontmatter `sources:` **and** in its prose `## Sources`
   section, and frontmatter `sources:` entries are sometimes human prose rather than paths
   (`vlt-core` audit `:69`; A4-1 disposition 4, now shipped as the `linkage_ripe` cited leg). If the
   two surfaces diverge **on a wiki page**, one of them is wrong — that is a genuine wiki-side
   finding, adjacent to A4-1's leg but a different check on a different layer.

## Candidate dispositions (for capture to rule — not pre-empted here)

- **(a) Delete the slot.** Cheapest and honest: a declared finding with no producer is a promise the
  SKILL does not keep. Cost: loses the intent record.
- **(b) Define the check.** A tier-1 (one-file-checkable) wiki-page check: frontmatter `sources:` vs
  prose `## Sources`, flag divergence. Note A4-1 already made the wiki-side prose-`## Sources` read
  mandatory for the candidacy pass, so the read is no longer additional cost in full mode.
  Membership test lives in `{conventions}/write-verification.md` — tier-1 vs tier-2 is that file's
  call, not this filing's.
- **(c) Keep + mark.** Leave the slot, let A4-2's general rule mark it unimplemented. Weakest — the
  slot keeps claiming a check that does not exist.

Preference, weakly held: **(b)** if the check survives the membership test, else **(a)**. What must
not happen is (c) plus silence.

## Loop hygiene note

This is the second Arc-4 filing of the form *"a shipped surface claims a check it does not run"*
(cf. the polarity inversion in `2026-07-25-171500-brief-restatement-drift.md`, and the silent-zero
class itself). Whether that is a pattern worth a check of its own — a lint on the module's own report
contract, i.e. every declared report key traces to a check that fills it — is a **factory-tooling**
question (`tools/package-lint.py` territory, plausibly a Group E extension), not module source.
Raised, not argued.
