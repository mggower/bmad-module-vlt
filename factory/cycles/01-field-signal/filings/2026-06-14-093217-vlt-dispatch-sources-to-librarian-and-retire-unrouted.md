# vlt-dispatch: route captured sources to the Librarian, and retire the `unrouted` pointer

**Date:** 2026-06-14
**Origin:** `vlt-core` vault, first real dispatch run surfaced two routing defects.
**Affected module artifact:** `skills/vlt-dispatch/SKILL.md` (operation skill). No convention or contract change.
**Blast radius / gate:** `operation skill` self-edit — council-none. Additive/reversible.

---

## Problem statement + evidence

After the first production `vlt-dispatch` run over a backlog of `daily/` notes, two classes of bad output appeared in `_agent/dispatch.md`:

1. **Captured sources mis-routed to the Researcher.** A daily fragment that was just a *saved article* ("saved NYT Athletic article: 2026 NFL Draft winners & losers", `daily/2026-04-26`) was tagged `researcher`. But a saved article needs no investigation — it needs *ingesting*. The Researcher's domain is **open questions worth investigating**; a captured source/URL/"read this" is **material**, which is the Librarian's ingest domain. The skill's domain-map gloss ("Researcher → open questions worth investigating; Librarian → vault/knowledge-meta") did not state where a *saved source* goes, so the router defaulted material into the question lane.

2. **`unrouted` pointers are a permanent ledger leak.** The skill routed every no-owner fragment (social observations, shopping lists, orders, product links) to a persistent `` `unrouted` `` checkbox in `_agent/dispatch.md`. Per the skill's own design, `unrouted` "is the user's to drain" and no partner ever greps it — so these items sit **open in the standing ledger forever**. That is precisely the *unprocessed-accumulation* clutter the operation exists to prevent: the "Still open across the record" ledger fills with un-homeable notes that no one will ever check off, drowning the real partner-owned signal. Evidence: after one run the ledger already carried multiple permanently-open `unrouted` lines (PR packing list, cleaning-supplies list, social-gathering notes).

This is the natural extension of an already-shipped principle. The module already says *unintelligible* fragments should be **flagged with the user, not forced into `unrouted`**. The same logic applies to **every** no-owner fragment: the honest outcome for something with no vault home is a one-time flag, not a parked checkbox that can never be drained.

## Decision + rationale

**Change 1 — captured sources/links route to the Librarian.** Add an explicit classification rule: a saved article, URL, or "read this / ingest this" is material for the **Librarian's** ingest queue (`librarian`), never the Researcher. State the dividing line plainly — *Researcher gets questions; Librarian gets material/sources.* This generalizes the existing reading/book-notes→Librarian convention (a saved source is the same family as a reading reflection).

**Change 2 — retire the `unrouted` pointer entirely; flag-and-skip instead.** No-owner fragments get **no pointer written** to `_agent/dispatch.md`. They are surfaced **once** in the run report (a new *Flagged and skipped* section) and otherwise left untouched in the daily note. Result: the routing record and standing ledger hold **only partner-owned, drainable work** — the ledger becomes an honest signal again.

Alternative considered and rejected: *keep `unrouted` for actionable to-dos (shopping/orders/links) and flag-and-skip only "home-less" personal captures.* Rejected by the vault owner — the distinction is fuzzy at classification time, and even to-do `unrouted` items are never drained by a partner, so they leak the ledger just the same. Chosen rule is the simpler invariant: **if no partner owns it, it gets no pointer.**

## Exact changes to ship in the module

All in `skills/vlt-dispatch/SKILL.md`:

1. **"Classify against the live roster" → the per-fragment bullets:**
   - Add a bullet: **A captured source or link → the Librarian.** Saved article/URL/"read this"/"ingest X" routes to `librarian`; Researcher = open questions, Librarian = sources/material. Note it generalizes the reading-notes→Librarian rule.
   - Rewrite the **No owner** bullet from "routes to `[unrouted]` … a valid, honest outcome" to **flag-and-skip**: no pointer is written; surface once in the run report; extends "flag, don't force a fit" from unintelligible to *all* no-owner fragments.
2. **"Write the routing record":** remove the `` - [ ] `unrouted` … `` example line from the format block; remove the "`` `unrouted` `` has no partner name" sentence (replace with "every pointer carries a live partner slug; no domain-less pointer exists"); add a line that only owned fragments get a pointer and `K item(s)` counts only written pointers.
3. **"The pickup loop":** delete step 4 ("`unrouted` is the user's to drain"); add a parenthetical that there are no domain-less items to drain (flagged in report, never recorded).
4. **"Report the handoff":** replace "If anything routed to `unrouted`, list it" with a **Flagged and skipped** report section (list no-owner fragments once, state they were *not* written to the record and remain in the daily note); remove `unrouted N` from the standing-ledger example; add that the ledger holds partner-owned work only.
5. **"Verify":** remove the "(or `` `unrouted` ``)" allowance; add an assertion that **no pointer carries a domain-less slug** and every no-owner fragment was flagged-not-written.

The skill **frontmatter `description`** and the **`module-help.csv` row** need **no change** — neither names `unrouted` or Researcher-routing.

## Upgrade / migration path for existing installs

- **Skill body:** ship the edited `SKILL.md`. Pure prose/behavior change; no schema or path change.
- **Existing `_agent/dispatch.md` data (per install):** older records may contain (a) `researcher`-tagged source items and (b) open `unrouted` lines. These are **not** auto-migrated by the upgrade. Recommended one-time reconciliation, left to the vault owner / Librarian:
  - Re-tag any `` `researcher` `` line that is actually a saved source → `` `librarian` `` (or check off if already ingested).
  - Resolve open `` `unrouted` `` lines: check off (`- [x]`) any the user has handled, and treat the rest as flagged — they can be struck or left as historical, but no new `unrouted` lines will ever be written.
  - This is a data cleanup, not a skill action; the skill change alone is forward-correct (no new `unrouted`/mis-routed-source lines going forward).

## Latent bugs surfaced

- The `unrouted` design had **no drain owner** — "the user's to drain" with no mechanism and no partner grep meant guaranteed unbounded growth of the one surface (the standing ledger) the skill advertises as the human's honest signal. The flag-and-skip fix removes the leak at the source.

## Open design questions (module-wide)

- Should "captured source → Librarian" be tightened to *auto-suggest* `vlt-ingest` for that fragment in the report (a nudge), or stay a pure pointer? Current change keeps it a pointer (consistent with surface-and-point; no auto-ingest).
- Should the *Flagged and skipped* report list be capped/summarized when a full dispatch flags many no-owner fragments at once (avoid a wall of text on first-run backlogs)? Possibly summarize by category beyond N.
