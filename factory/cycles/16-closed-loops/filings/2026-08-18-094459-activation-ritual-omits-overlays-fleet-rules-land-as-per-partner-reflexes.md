# Activation ritual omits `{overlays}` — fleet-wide rules end up living as per-partner reflexes

_Filed 2026-08-18 from **vlt-core**, classification: **pattern**. Filed by the Researcher (Dorian) out of its own 2026-08-18 groom pass, at the owner's request. Grounding measured against vlt-core at `2400dd9`._

## What happened

The vault minted a local convention overlay on 2026-08-14 (`_agent/conventions/frontmatter.overlay.md`, rule A: prose is not hard-wrapped — Obsidian is the reading surface). Within three days, **two different partners violated it in the same day**, the second one *after* reading a log entry recording the first one's correction:

1. **2026-08-17, Career Strategist (Rook):** corrected by the user mid-sitting for hard-wrapped prose. His own session note names the miss: the correction was "already written in my own files" — the overlay existed, he had not read it before writing. Evidence: `_agent/log.md`, the `[2026-08-17 13:51] session (career-strategist)` entry.
2. **2026-08-17, Researcher (Dorian), ~1 hour later:** wrote a research note hard-wrapped despite having read Rook's correction in the log at orient. Self-caught only at a late verification step whose JIT-read happened to include the overlay — the catch was luck of sequence, and a sitting that writes early and verifies late ships the violation. Evidence: the Researcher's own `## Self` record of it, now promoted to a reflex at `_agent/partners/researcher/reflexes.md` ("Read the vault's convention overlays before the first write of a sitting, not at verification time").

The mechanism, not the symptom: **the activation ritual never surfaces `{overlays}`.** Beat 1 reads persona + identity + reflexes; Beat 2 reads index headings, log tail, backlog tail, thread, dispatch slice, capabilities (operating contract, *Activation ritual — two beats*). Overlays reach a partner only through per-op JIT-read instructions ("read `{conventions}/frontmatter.md` together with `{overlays}/frontmatter.overlay.md` if present") — so any write made *outside* an op that happens to name that JIT pair is unprotected. A lesson recorded in one partner's log entry protects nothing: it arrives labeled as *that partner's* lesson, not as a rule binding the reader's next write.

## The pattern (why this is more than one missing read)

The vault's grooming machinery now gives each partner a reflex layer, and the observed failure mode is that **fleet-relevant rules condense there as N per-partner copies** because no fleet-wide always-loaded rung exists between "one partner's reflexes" and "shipped governance." Three rules from the Researcher's 2026-08-18 first groom illustrate the gradient:

- "Read the convention overlays before the first write of a sitting" — **purely mechanical, binds every writing partner**; it is machinery patching, not research craft.
- "A routed/consolidated ask is a snapshot, not a live read — re-ground it against the current page before acting" — binds **any partner draining a dispatch slice** (field case: a 2026-08-14 consolidated ask asserted a page held nothing on a schema the same vault had filed 2026-07-03).
- "A relay's named pages are a starting point, not the scope" — the general half binds any relay recipient; only the "audit the cluster" half is one partner's craft.

Each will now be independently rediscovered and re-minted per partner (9 partners in this install), which is the module's own verb-not-subject smell applied to rules instead of skills. The reflex cap (30/partner) also spends per-partner budget on rules that aren't that partner's.

## Provenance guess (explicitly a guess)

The likely home of the fix is the **contract's Activation ritual** — a `{overlays}` read (they are small: one file, 4KB, append-only by declaration) added to Beat 1 or the rule-card load, since overlays are act-blocking for writes the way reflexes are. An alternative shape is a fleet-wide rule layer (a `reflexes`-like always-loaded file at vault scope) that overlays and dispatch-discipline rules could promote into — but that is a design call the factory owns, and it interacts with the 2026-08-14 filing `no-legal-home-for-a-vault-originated-new-convention` (this filing is the *read-side* of that one's *residence-side* gap) and with the 2026-07-29 boot-cost filings (any new always-loaded read spends the budget those filings measure). All of the above is a guess; the grounded claim is only: two same-day field violations, a self-catch that was luck of sequence, and no shipped read that would have prevented either.
