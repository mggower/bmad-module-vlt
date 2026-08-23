# A PARA file with an undeclared `type:` is invisible by construction — two checks each correctly decline, summing to no coverage

_Filed 2026-08-23. Evidence: vlt-core lint `{lint_reports}/2026-08-23-1739-lint.yaml`
(`para_status_unknown` informational note), factory-verified read-only.
Classification: **pattern** — a coverage gap proven by one live instance, produced by
two checks each behaving correctly. Provenance: the B10-10(4) acceptance lint._

## The instance

`projects/fantasy-2026/draft-night-dashboard-intent.md` sits in PARA jurisdiction
carrying `type: note` and `author: creative`, with `status: in-progress`. Neither net
reaches it:

- `para_status_unknown` cannot fire — `note` is not a PARA artifact type, so no
  per-type enum exists for its `status:` to be outside of.
- `para_missing_attestation` cannot fire — the net keys on `author:` in
  `human|agent|hybrid`, and `creative` (a partner name) is off that vocabulary.

The 1739 report surfaced it only as prose ("reported rather than slotted, because no
check as written covers it") — executor judgment, not a check. A less careful run
reports nothing.

## Why this is module signal

Each check's decline is individually correct; the gap is the **sum**. The PARA
jurisdiction rule (write-verification scope; the bare-human-file exemption) assumes a
file either carries the model's vocabulary or is exempt — a file carrying *almost* the
vocabulary (a declared but unknown `type:`, an author value naming a partner rather
than the provenance class) lands in neither world. Both failure shapes are natural:
`type: note` is a plausible author habit, and `author: <partner-name>` is arguably
more informative than `agent` — the vocabulary invites the mistake.

## Candidate directions (for capture, not answered here)

- A closing net: a PARA-jurisdiction file whose `type:` is outside the known set (or
  whose `author:` is outside `human|agent|hybrid`) gets its own finding class
  (`para_type_unknown` / `para_author_unknown`) — the R3 pattern: a legal response
  stated, loud rather than silent.
- Or widen the vocabulary deliberately: rule whether partner names are legal
  `author:` values (they carry more information; the nets could map them to `agent`),
  and whether non-artifact types are legal residents of container folders.
