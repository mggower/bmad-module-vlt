# The spec-candidate ">=2 relay entries" leg fires on ordinary ask-and-answer round trips

_Filed 2026-08-22 by the owner (relayed from the vlt-core scoped lint of 2026-08-22,
vault commit `f39946a`; owner's words in-session: "a check-tuning question for the
module, not vault debt"). Classification: **pattern / check-tuning candidate**.
Provenance: the run's own `coverage_caps` line plus the wearer's triage of the
firing set._

## The signal, precisely

In the 2026-08-22 scoped lint over vlt-core (33 files; the first fully conformant
B10-3-era run — annotated loud slot + denominated `spec_candidate_standing:` both
behaving), the spec-candidate check's ">=2 relay entries" leg fired on **8 of 31
handoffs. Six of the eight are a single ask→answer round trip** — the ordinary handoff
lifecycle, not a document under repeated amendment. The wearer filed only the one
candidate carrying **both** signals (dated revision record AND a relay whose second
entry is a `deliver, ref:` amendment — `penny-treat-rotation`), and named the other six
in the report rather than dumping six backlog items on a threshold judged mis-tuned.

## Why this is module signal, not vault debt

The leg's intent (B10-3, `checks.md:47` partition) is "this handoff keeps getting
amended — maybe it wants to be a spec." A single ask→answer pair satisfies ">=2
entries" while carrying zero amendment signal: the threshold counts *traffic*, not
*revision*. On any conversational vault the ordinary lifecycle produces exactly two
entries, so the leg's false-fire rate scales with normal usage. The field wearer
absorbed the noise this run by judgment; the check shouldn't rely on wearer judgment
to suppress a structurally mis-tuned trigger.

## Candidate directions (for capture to grind, not a ruling)

- Count **relay entries past the first delivery** (amendments), or require the second
  entry to be a `deliver`-kind revisiting the same artifact (`ref:` to an amended
  variant) — the shape the genuine candidate actually had.
- Or keep the count but require co-occurrence with the dated-revision-record signal
  (the both-signals case is what the wearer trusted in practice).
- Whatever lands must honor B10-3's retained postures (records-never-reports
  derivation, no stored counter, decline exclusion, relay-entries-only).

## Acceptance linkage

Rides B10-3(3)'s open tail: run 1 (2026-08-22) is recorded conformant; whichever build
takes this tuning re-states the leg, and the check's next two-run observation window
sizes the false-fire collapse.
