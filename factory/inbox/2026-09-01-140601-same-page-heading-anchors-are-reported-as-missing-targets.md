# Same-page heading anchors are reported as missing targets

_Filed 2026-09-01 from **`{field-vault}`**'s `{lint_reports}/2026-09-01-1406-lint.yaml`. **Second
consecutive sweep** — the same finding was refused on 2026-08-30 without a diagnosed cause; this run
supplies one. Evidence is `{field-vault}`, read-only._

## The claim

A wikilink to a **same-page heading anchor** — `[[#Heading Text]]`, no page component — is reported as
a **missing target**. `vlt-lint-full.js`'s `normalizeTarget` strips the `#anchor` portion, is left
with an **empty string**, and reports that empty result rather than dropping it.

**The specimen, twice:** the wiki page `calf-strain` carries `[[#Early Loading Phase (≈ Days 3–7)]]`
and the heading exists **on that page at line 111**. It was reported as a missing target on
2026-08-30 (refused: *"an intra-page anchor, never a page target"*) and again on 2026-09-01
(refused, with the cause identified).

## Why it matters more than one false positive

`missing_targets` sits in **`fix_now`**, whose legal response is to create or repoint the target. An
entry whose normalized target is the **empty string** cannot be acted on correctly by any responder:
there is no page to create and no link to repoint. It is guaranteed operator friction on every sweep,
forever, and it consumes exactly the manual verification budget that the `false_positives_refused`
discipline exists to spend on real ambiguity.

**It will re-fire on every sweep until the normalizer changes** — the page is conformant, so nothing
in the vault can stop it. ⚠ And because the cache now works, a page carrying an anchor link keeps
producing this finding **from its cached record**, so re-running the sweep does not even re-derive it.

## Candidate direction (not a fix — capture's call)

**Drop an empty normalization result rather than reporting it.** A link whose entire target is an
anchor is a **same-page reference**, which is conformant and not a link-integrity question at all.
Whether the anchor's *existence* should be validated (the heading is present here, but a stale
anchor is a real defect class) is a **separate question capture should rule rather than fold in** —
this filing asks only that an empty target stop being reported as a missing page.

## Grounding

- `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — `normalizeTarget` and the `missing_targets`
  derivation. ⚠ **Exact `file:line` not pinned by this filing**; capture must ground it.
- `{lint_reports}/2026-09-01-1406-lint.yaml:225` and `{lint_reports}/2026-08-30-1123-lint.yaml:229` —
  the two refusals.

_Ship-verifiable at rest: gradeable against a fixture page carrying an anchor-only wikilink._
