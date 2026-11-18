# Entity-collision coverage is silently pair-incomplete — cluster bounding lost a known, documented collision

_Filed 2026-07-29 from **acceptance discharge run 2** (Arc 4 ledger, A4-4 clause 5, graded FAILED
on its named subject 2026-07-27; owner confirmed filing at run 3). Evidence is vlt-core's
2026-07-26 18:05 full lint, read-only._

## The claim

A4-4's entity-collision check works — the 18:05 full lint surfaced **three real collisions**
(Tariq Woolen; Anthony Campanile; Miyabi's cultivar count, correctly read as a probable
supersession wearing a collision's clothes). But the acceptance clause's **named test case — the
Jonah/Alaric pair — is still on disk and did not surface**, because the sweep is cluster-bounded
and never compared that pair of pages. The check didn't mis-classify it (not in both slots, not
filed as a contradiction); it simply **could not see it**, for the reason the report itself states:
*"a cluster-bounded sweep did not compare every pair."*

## Grounding

- `vlt-core _agent/wiki/los-angeles-rams.md:77` — a `[!stale]` *"Which Jackson?"* callout against
  `[[nfl-2026-offense-rankings]]`, tracked in `{backlog}`.
- The sharp detail: that callout says the Rams instance is *"Tracked in `{backlog}` alongside the
  Seahawks-coordinator instance — one lookup settles both"* — and the check **found the Seahawks
  instance and missed its twin**. A known, already-documented, explicitly-paired collision is the
  cheapest regression test the check could have, and cluster bounding lost it.
- The report was honest about the limit (`entity_scan:` names the cluster-bounded blind spot) —
  the honesty machinery worked; the coverage gap is what's filed.

## Why it matters

Unlike the single-mention blind spot (by construction, unclosable), this is a **sweep-shape**
limit with a cheap close: a cluster-aware second pass over already-flagged name callouts
(`[!stale]` / name-verification callouts already on disk) would have compared exactly the pairs
the vault itself has marked as suspicious. Pages that document their own suspects should never be
the ones the check can't see.
