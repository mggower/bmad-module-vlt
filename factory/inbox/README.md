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

## When the filing is not a defect — `supersession`

*(Platform P-15, 2026-08-25.)* Almost every filing here describes something that **broke**:
friction hit in anger, a defect, a gap. A **`supersession`** filing describes the opposite —
*this protection is now redundant, because X now enforces what it was standing in for.* A
prohibition written when the honest fields had no teeth stops earning its place the moment a
net enforces them, and nothing else in the loop can say so: obsolescence produces no field
pain, only friction that reads as normal governance.

A supersession filing is an ordinary dated note in this directory, marked `class: supersession`
in its opening line, and it carries **both halves** or it is not one:

1. **The rule now redundant** — its exact site (`file:line`), and what it was standing in for.
2. **The mechanism that supersedes it** — what shipped, where, and why its population covers
   the rule's. "Something better exists now" is a wish; "check *Y* at `<site>` enforces the
   same claim across the same population" is a filing.

It asks for a **retirement**, not another exception — a filing that ends in a new carve-out
has diagnosed the symptom. Capture grounds it like any other filing (`inbox-capture`); the
roundtable's obsolescence beat is where a retirement found *inside* a plan lands instead.

**Not to be confused with the `SUPERSEDED` grounding grade**, which means the module already
fixed what a filing reported. Here supersession is the filing's *claim*, not its verdict.

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
