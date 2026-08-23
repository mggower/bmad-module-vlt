# Inbox — field filings from live vaults

This is where a live `vlt-*` install (e.g. a field vault) files **field notes** back to the module:
friction hit in anger, defects, design gaps, "this should ship upstream" observations. Each filing
is one dated markdown note (`YYYY-MM-DD-HHmmss-slug.md`) written by a partner or the owner.

## Lifecycle

1. **File** — a filing lands here, raw, the moment a real install hits something worth upstreaming.
2. **Capture** — filings are folded into a durable, resumable **roadmap** at
   `factory/cycles/NN-<slug>/roadmap.md` (one roadmap per signal-cluster "cycle"; the open cycle is
   named by `factory/CYCLE`), which phases and builds them. The roadmap is the cache; it spawns the
   briefs in that cycle's `briefs/`. A closed cycle's directory simply stops changing — archival is a
   property of location, not a move. (Cycles 1–10 were called arcs; Cycle 1 is
   `factory/cycles/01-field-signal/`, builds #3–#11.)
3. **Build** — each phase ships as a build; the roadmap tracks status + a deferred-acceptance ledger.
4. **Retire** — once a filing's findings are fully captured (and built, and its clauses accepted), the
   filing moves to the consuming cycle's `filings/` directory. The active inbox holds only
   **un-captured** filings.

## Remote filings

- Filings can also arrive as GitHub issues on the module's public tracker and are
  materialized here by the factory intake — the field contract (payload shape, labels,
  `origin:` header) is single-homed at `skills/vlt-feedback/references/field-contract.md`.
- A materialized filing carries an `origin: <repo>#<n>` header per that contract.
- When a materialized filing retires (its build shipped and passed acceptance), the
  factory closes its issue — and a declined issue is closed at triage with a reason,
  nothing materialized. Mechanics: `inbox-capture`'s github-intake reference and
  `cycle-closeout` Stage 5; vocabulary: the field contract (same home as above).

So: an **empty** active inbox means everything filed so far has been pulled into a roadmap. New field
signal goes here; processed signal lives in its cycle's `filings/` for provenance.

## Where processed filings live

Each cycle's `filings/` under `factory/cycles/` holds the filings whose builds shipped and passed
acceptance during that cycle; the closed roadmap beside them is the authoritative per-filing record.

**This README maintains no list.** It once enumerated the archive by count, and the count fell behind
the archive's real contents — the "lists that claim completeness drift" failure, in the lifecycle's
own front door. Read the directories, and read the closed roadmap for why any given filing is there.
