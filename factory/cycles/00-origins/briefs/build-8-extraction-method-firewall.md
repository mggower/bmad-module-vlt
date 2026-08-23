---
title: 'Build #8 — The personalized-extraction method-traces firewall (filing #6 deferred enforcement)'
status: 'BUILT 2026-06-24 — unit-verified at rest (handshake bipartite-consistent); live acceptance deferred to the batched first-safe vlt-core upgrade.'
build_log:
  - 'BUILT 2026-06-24. Added a "Personalized-extraction firewall" check to vlt-lint Step 2 (both modes): for each extracted artifact carrying personalization_sources:, flag method_not_in_sources (a general/method body claim not covered by any wiki page in sources: — leaked in via personalization) and method_in_personalization (a personalization_sources entry / operational-log file carrying method rather than the user''s operational state). Never auto-fix — flag for the partner to re-ground or move. Added report key personalized_extraction_issues. COHERENCE: because vlt-lint now encodes a rule from extraction.md, the build-4 handshake required registering it — extraction.md consumers: [vlt-extract] → [vlt-extract, vlt-lint]; vlt-lint depends_on gained "extraction@2". Handshake re-verified bipartite-consistent (extraction@2 ↔ both vlt-extract and vlt-lint).'
phase: 'Follow-on — deferred firewall from filing #6 (rides Phase B handshake)'
module_code: 'vlt'
created: '2026-06-24'
updated: '2026-06-24'
derives_from:
  - 'inbox filing #6 — personalized extraction model (the deferred "ship a vlt-lint firewall check" enforcement gap)'
  - 'skills/reports/build-5-mint-maturation.md (built the widening; deferred the firewall)'
ideation_decisions:
  - 'Sibling, not merged with build-7''s capability lane-firewall (same philosophy — lint enforces a declared boundary — different target: extraction provenance vs capability write-lane).'
  - 'The check makes vlt-lint a consumer of extraction.md → must carry the handshake ack (extraction@2) and be listed in extraction''s consumers:. Coherence machinery applied to the build''s own change.'
---

# Build #8 — Personalized-extraction method-traces firewall

## Thesis

Build #5 shipped the personalized-extraction widening (filing #6): a domain deliverable may additionally read the partner's agent-zone state via a separate `personalization_sources:` field — but the hard invariant holds, **every method/general claim must still trace to a wiki page in `sources:`**, and `personalization_sources:` carries **state, never method**. Build #5 enforced that with prose + a verify-checkbox and **deferred the lint net** (exposure bounded: n=1, gated). Build #8 ships the net.

## What shipped

- **vlt-lint "Personalized-extraction firewall"** (Step 2, both modes): for each extracted artifact with `personalization_sources:`, flag `method_not_in_sources` (a general-method body claim not covered by its wiki `sources:`) and `method_in_personalization` (a `personalization_sources:` entry carrying method, not operational state). Report key `personalized_extraction_issues`. Never auto-fix.
- **Handshake registration** (build-4 discipline applied to this change): `extraction.md` `consumers:` → `[vlt-extract, vlt-lint]`; `vlt-lint` `depends_on` += `"extraction@2"`. Bipartite-consistent.

## Acceptance (deferred — batched to the first safe vlt-core upgrade)
- [ ] A real `vlt-track`-style personalized extraction with a method claim **not** grounded in its wiki `sources:` is flagged `method_not_in_sources`.
- [ ] An operational log under `personalization_sources:` carrying general knowledge is flagged `method_in_personalization`.
- [ ] The handshake coherence check sees `vlt-lint`'s `extraction@2` ack as current.
