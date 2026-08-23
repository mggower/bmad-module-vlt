---
title: "vlt-core capability: file-module-feedback (the inbox rail)"
status: BRIEFED 2026-07-12 — build IN vlt-core via vlt-mint (owner-run); NOT module source, never ships
kind: vault-local capability for {field-vault}
created: 2026-07-12
derives_from: handoff-2026-07-12 (00-handoff §1.2 final para; 04-open-threads §4.6); inbox/2026-07-11-153000 field-calibration filing
risk: low — writes new files into the factory inbox only; touches nothing in module source or vault canon
---

# file-module-feedback — vlt-core's rail into the factory inbox

## Placement ruling (why this is vault-local, not module source)

vlt-core is the **only** vlt install with access to the module inbox, because both live
on this machine. Every other install (the work-machine vault today, any future
consumer) has no path to `inbox/` — so an inbox rail cannot ship as module source
without being dead weight (or worse, a broken absolute path) everywhere but here.
Ruling: build it directly into vlt-core via `vlt-mint`, as vault-local evolution. The
machine-local absolute path this capability hardcodes is therefore a *feature*, not a
leak — the placeholder-paths rule (CLAUDE.md) governs shipped module content, and this
is deliberately unshipped. The capability lives in the agent zone, so the module's
durability posture preserves it across upgrades automatically.

## What it formalizes (currently ad-hoc, three observed shapes)

Filing module feedback already happens, informally, three ways — all visible in
vlt-core today:

1. **Backlog-flagged candidates** — `_agent/backlog.md` items marked
   "Module-feedback candidate" (e.g. the ingested-sources ledger gap, which later
   became the 07-06 ingestion-ledger filing) that wait for someone to remember them.
2. **Evolution artifacts** — the `_agent/artifacts/problem-solution-*.md` docs that
   became the six Arc 3 filings; the transformation into inbox filings was manual.
3. **Second-vault relay** — the 2026-07-11-153000 field-calibration filing explicitly
   carried signal on behalf of the work-machine vault ("that vault has no inbox
   access… this filing carries its signal").

The capability gives all three one procedure and one owner.

## Mint-session inputs (what the vlt-mint run needs to know)

- **Kind:** `add a capability`.
- **Proposed owner: the Librarian** — custodial partner, owns the backlog where
  module-feedback candidates already accumulate, fronts lint (a defect-finding op), and
  runs dispatch. Owner may rule otherwise at mint time.
- **write_scope (state it exactly in the becoming/planning doc):** creates **new files
  only**, in exactly one location **outside the vault**:
  `{factory-root}/inbox/` (the factory inbox).
  Never edits or deletes there (`inbox/archive/` is factory-side machinery, untouched).
  Inside the vault it writes only the ordinary traces: a `{log}` line and a
  backlog-item annotation ("filed → <filing filename>").
- **Weight/council analysis for the classifier:** an extra-vault write scope is
  unprecedented — the contract's lane vocabulary covers vault zones, and "new-file
  deposits" carve-outs (the `sources/` precedent) are in-vault. On the additive/no-lane
  -collision reading this is a **light capability** (own-zone file under the
  Librarian's `capabilities/`, council-none); on the novel-write-surface reading it
  deserves a **gated mint**. Recommendation: let the mint's boundary classifier and (if
  routed) the council rule — that's what the machinery is for — but do not let the
  extra-vault scope pass silently un-ruled. The capability file must record the ruling
  either way.
- **Boundary classifier answer:** this mint creates no rule anyone else must obey (the
  filing *shape* is factory-owned, defined in the factory's `inbox/README.md`; this
  capability conforms to it, it doesn't define it) → `non-boundary: conforms to a
  factory-owned convention; no vault-side bell needed`.

## Capability mechanics (the body of `capabilities/file-module-feedback.md`)

1. **Triggers** — any of: a backlog item flagged module-feedback that the owner says to
   file; a completed evolution artifact (problem-solution doc) the owner wants filed;
   defect/pattern/candidate signal arising live in a session ("file that to the module
   inbox"); signal arriving from the work-machine vault (owner relays it in).
2. **Pre-flight** — read the factory's `inbox/README.md` fresh each run (the shape is
   factory-owned and may evolve; never file from memory). Confirm the factory repo
   exists at the hardcoded path; if not (new machine, moved repo), stop and say so —
   the capability's one standing assumption is machine-local co-residence.
3. **Draft** — one filing per distinct signal, named `YYYY-MM-DD-HHmmss-<slug>.md`
   (real timestamp), body per the README shape: what happened / evidence with concrete
   vault paths / a provenance guess **explicitly marked as a guess** (factory capture
   re-grounds every claim — filings that over-assert provenance have repeatedly been
   wrong, so humility in the filing is a kindness to the loop). Classify honestly:
   defect / pattern / candidate / design-stage-proposal (the last only at owner
   request, with its evidence debts declared, per the Arc 3 precedent).
4. **Second-vault relays** — when the signal originates from the work-machine vault,
   the filing states its origin vault up front, carries whatever calibration caveats
   the origin context imposes, and says where acceptance should run (precedent to
   imitate: `inbox/2026-07-11-153000-graduation-queue-field-calibration.md`).
5. **Write + trace** — write the filing into the factory inbox; append a `{log}` line
   (reuse an existing type or coin one per the contract's non-exhaustive-type rule —
   suggest `filed`); annotate the source backlog item / artifact with the filing
   filename so nothing double-files.
6. **Never** — edit factory module source, edit existing inbox files, touch
   `inbox/archive/`, or file vault-content problems (a wiki contradiction is vault
   work, not module feedback — the test: "would fixing this change module source?").

## Out of scope (dispositions)

- A return channel (factory → vault) — acceptance results already flow back via
  `vlt-upgrade` + the upgrade ledger; no second rail needed.
- Shipping any of this in the module — placement ruling above; if a future
  multi-machine story emerges, that's a factory design problem (a remote inbox), not a
  vault capability.
- An inbox rail *on* the work-machine vault — it has no filesystem path to the inbox;
  its rail IS this capability's relay branch, owner-mediated. Revisit only if that
  vault's signal volume makes owner-relay painful.
- Auto-filing (e.g. lint auto-files findings that implicate module machinery) — tempting,
  rejected for now: filing is a judgment act and the loop's quality depends on it
  (capture-cheap applies to the vault's backlog, not the factory's front door). A
  backlog flag + this capability on demand is the right friction.

## Verification (at mint time, in-vault)

- Mint ceremony completes per its own gates (planning doc if gated; decision-log entry
  either way; capability file lands under the Librarian's `capabilities/`).
- Dry-run: draft a filing for a synthetic candidate to a scratch path, verify shape
  against the factory README, do not deliver it.
- Lint pass: next `vlt-lint` run reports no `capability_lane_violation` /
  `scope_mismatch` on the new capability (its declared scope must be written precisely
  enough that the lane checks can read it).

## Acceptance (live)

- First real filing goes through the capability end-to-end: correctly named and shaped
  file appears in the factory inbox, `{log}` line + backlog annotation written, and the
  factory's next `inbox-capture` run grounds it without shape complaints.
- First work-machine relay filing (the graduation-queue acceptance evidence is the
  expected first case) carries origin-vault framing per the 153000 precedent.
