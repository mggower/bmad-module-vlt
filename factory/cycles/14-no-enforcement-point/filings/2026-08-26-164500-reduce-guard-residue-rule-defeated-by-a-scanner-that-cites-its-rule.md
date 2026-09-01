# The reduce-side guard is defeated whenever the scanner cites the rule it is applying

**Filed:** 2026-08-26 · **Vault:** `{field-vault}` · **Module:** v0.16.1
**Instrument:** full-mode `vlt-lint` sweep, `_agent/lint-reports/2026-08-26-1046-lint.yaml`
(146/146 pages, 0 cached — cold run, ruleset fingerprint moved with the upgrade)
**Filed by:** the factory session, transcribed from a `{field-vault}` session's relayed report,
**not** through the `vlt-feedback` rail — so this filing carries no `origin:` header and is not
rail-materialized. Do not re-file it upstream: a rail copy would materialize a second time
(the `origin:` header is the only idempotency key, and this filing has none). Claims were
re-verified factory-side against the lint report on disk and against shipped module source
before filing; the reproduction below was run at rest, not relayed.
**Against:** Cycle 13 build-1 (`5bc53f6`), acceptance checks (2) and (4)

## What happened

v0.16.1's build-1 shipped two reduce-side guards so the full-lint reduce would stop believing
the page scanner's `frontmatter_valid` / `frontmatter_issue` claims unread. On the **first live
full sweep after the upgrade**, the defect the guards exist to remove recurred, in the same
shape, at the same two slots:

- `costa-rican-village-dog` appears in **both** `unattested_write` **and**
  `unmarked_supersessions` — precisely the duplicate the guard shipped to remove.
- `execution-to-judgment-shift` reached `malformed_frontmatter` as an attestation-only
  complaint. This page is **one of the six named subjects of acceptance check (2)**.
- `empyrean-series-overview` reached `malformed_frontmatter` as a claimed-missing
  **documented-optional** field (`review_after`) — disposition 2's exact target.

Net for the sweep: **all 3** `unmarked_supersessions` entries and **2 of 3**
`malformed_frontmatter` entries were false, and were refuted by hand — the hand-fold the build
set out to end (20 folds 2026-08-24, 6 on 2026-08-25, 5 today).

## Why — the residue rule assumes a bare claim

Both predicates are conjunctions ending in `claim.residue === ''`
(`skills/vlt-setup/assets/workflows/vlt-lint-full.js`, `parseClaim` / `attestationOnlyComplaint`
/ `inventedRequirement`, the guard block at `:549-630`). `parseClaim` strips every recognized
frontmatter key and a fixed `CLAIM_FILLER` list; **whatever prose is left is residue**, and
non-empty residue means no guard fires.

A scanner that states the claim bare is refused. A scanner that **cites the rule it is
applying** is not — the citation both leaves prose residue *and* names real
`PAGE_REQUIRED_FRONTMATTER` members inside the rule's own text.

Reproduced at rest against the shipped source, factory-side:

| claim text (real, from the field) | `named` | `residue` | refused? |
|---|---|---|---|
| ``missing `verified_by`/`verified_at` `` (2026-08-25 form) | `verified_by, verified_at` | `""` | **yes** |
| `lacks verified_by and verified_at per write-verification.md scope rule (files with type: wiki\|research\|... and author: agent\|hybrid require attestation)` (2026-08-26 form) | `verified_by, verified_at, author, type` | `"lacks per write verification md scope rule files wiki research agent hybrid require attestation"` | **no** |
| `review_after missing on time-bound content` | `review_after` | `"on time bound content"` | **no** |
| `missing review_after` | `review_after` | `""` | **yes** |

Nothing about the pages changed. **Only the scanner's phrasing did** — and the phrasing is
free text from a non-deterministic agent, so the guard's population is not the defect's
population. It is the subset of the defect whose wording happened to be terse.

## The shape, stated generally

Build-1's own premise was that *a rule stated in the prompt and enforced nowhere does not
bind*. The repair moved enforcement to the reduce — correctly — but the enforcement **still
rests on scanner-returned free text**, parsed. The guard trusts the *wording* of a claim in
order to decide whether to trust the *claim*. That is the same class one level up, and it is
the class Cycle 13 is named for.

Three of this sweep's four false findings share it. The other two are independent instances,
filed separately:
- page-scanner link under-return (11 pages, 23 instances, 1 wiki→wiki) manufacturing the
  sweep's only orphan;
- an HTML-escaped scanner return (`Energy &amp; Clean Tech`) failing the reduce's deliberately
  exact category comparison, producing the sweep's only `category_no_match`.

## What this contradicts

- **Acceptance check (4)** `[field-contingent]` — **FAILED outright.** Its clause 1 (no entry in
  either class is an attestation complaint) and clause 2 (none is a claimed-missing optional
  field) are both false on this sweep; the hand-fold it promised to end did not end.
- **Acceptance check (2)** `[ship-verifiable, GATES closeout]` — refuted **on a named subject**.
  (2) passed at rest by replaying the returns the field produced on **2026-08-25**, which were
  all bare-form. Bare-form is exactly the subset the guard handles. The instrument therefore
  could not observe the failure mode it was written to catch — the same defect (2)'s own
  binding warned about for Cycle 12 build-1's fixture, reproduced with a different instrument.

## Candidate direction (not a ruling)

The residue rule is the wrong primitive. Candidates, in rough order of appeal:

1. **Stop parsing prose for this decision at all.** The attestation facts are already returned
   structurally (`attested()` computes `unattested_write` and `attestation_census` from the same
   scan without reading `frontmatter_issue`). A duplicate can be refused by *structure* — "this
   page is already reported unattested, and the validity claim names no required field that is
   actually absent" — rather than by proving the sentence mentions nothing else.
2. **Ask the scanner for a structured claim** — a `frontmatter_missing: []` array of field names
   beside the prose `frontmatter_issue`. Moves the decidable part out of free text entirely.
   Costs a `PAGE_SCAN` schema change and a re-ack.
3. Widen `CLAIM_FILLER` / ignore parenthesized spans. **Named to be rejected** — it is another
   carve-out against an open-ended adversary (agent prose), and the next phrasing defeats it.

Direction 1 or 2 is the real fix; 3 is the trap.
