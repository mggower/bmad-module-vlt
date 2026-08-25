# Page scanners double-report missing attestation under two other finding classes

_Filed 2026-08-24. Evidence: the first post-0.15.0 full-mode `vlt-lint` sweep on
`{field-vault}` (`{lint_reports}/2026-08-24-1700-lint.yaml`, persisted; vault read-only
throughout). Classification: **defect** — one fact surfaced as up to three findings.
Provenance: executor adjudication recorded in the report's `fixes_applied:` block._

## The defect

A page missing `verified_by:`/`verified_at:` is one fact with one home — the attestation
surface (`unattested_write` / the attestation census). This run the page scanners also
returned the same fact under two other classes:

- **18 entries under `malformed_frontmatter`** — all of them "missing
  `verified_by`/`verified_at`", nothing else malformed.
- **2 entries under `unmarked_supersessions`** (`acotar-world-building`, `katsuo-dashi`) —
  attestation complaints misrouted into a supersession class.

The executor folded all 20 into the attestation census rather than triple-counting; a
less careful run would have reported the same gap three times (inflating counts the
factory reads as signal — the census read 145 pages: 97 fresh / 6 stale / 42 unattested
pre-adoption only because of this fold).

## The fix direction

In the page-scan classification (full-mode fan-out assets), make missing-attestation
its own terminal class: a frontmatter block whose only defect is absent
`verified_by`/`verified_at` must not enter `malformed_frontmatter`, and attestation
complaints must never route to `unmarked_supersessions`. One fact, one class.
