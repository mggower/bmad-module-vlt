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

## The specimen manifest — a filing carries its evidence, not a count of it

*(Platform P-18 Tier A, 2026-09-01. The cause is `ST-5`, *specimens have no owner* — read
`factory/studies/ST-5-specimens-have-no-owner.md` for the derivation. **This section is the
single home for the manifest's shape**; `acceptance-discharge` and `inbox-capture` point here.)*

A filing that observed a **set** must carry the set. Today one routinely reports *"18 entries"*
where 18 slugs were on screen, and the slugs are gone by the time anyone builds the check that
should catch them — the Cycle 12 build-1 trace is **20 specimens observed → 2 filed → 2 captured
→ 0 reaching the brief**, after which the briefer built a fixture from the shape of the fix and it
passed at rest while the field failed twice.

A filing whose evidence is a set carries a **specimen manifest**, with both parts:

1. **The complete set** — every member, named. Not a sample, not the interesting ones. Where the
   set is genuinely large, give the full set in a fenced block and say how it was obtained
   (the report path and key it was read from), so a later reader can re-derive it.
2. **The minimal triggering fragment** — the smallest quoted evidence that shows the defect
   happening: the report lines, the frontmatter block, the exact returned value. Enough that
   someone who cannot re-run the observation can still build an instrument from it.

**A bare count where a set was observable is a defect in the filing**, and capture will try to
recover the set (`inbox-capture`'s second grounding axis). Say so plainly when a set genuinely
cannot be recovered — *"count only; the report did not persist the slugs"* is honest and useful;
a silent count is neither.

**Worked pair, both real, both on disk.** Cited by **filing id**, not by path, for the reason
this directory's own lifecycle makes obvious: a filing lives here only until its build ships and
its clauses pass, then it moves to its cycle's `filings/`. A worked example pinned to an inbox
path documents itself into a dead link on the day the example is proven. (Precedent:
`factory/studies/ST-5-specimens-have-no-owner.md` cites the same filing as `2026-08-24-173002`.)

- **Conforms** — filing **`2026-08-26-075130`** (attestation misroute survives the jurisdiction
  narrowing) names all **6 of 6** specimens (`execution-to-judgment-shift`, `bistec-encebollado`,
  `k-curve-career-divergence`, `kettl`, `llm-wiki-pattern`, `obsidian-bases`) and quotes the
  triggering fragment from the report it read. It did this **unprompted**, before the rule existed.
  It has already migrated, to `factory/cycles/13-trusted-returns/filings/` — a closed cycle's
  directory stops changing, so *that* path is permanently addressable and safe to name in full.
- **Does not** — filing **`2026-08-24-173002`** (page scanners double-report missing attestation)
  observed **20** and named **2** (`acotar-world-building`, `katsuo-dashi`); the other 18 survive
  only as the number 18. It is the negative control, and it is not a bad filing — it is a good
  filing written before anyone owned its specimens. It is still in the active inbox as of
  2026-09-01, so it is named by id alone; find it here, or in the `filings/` of whichever cycle
  ships its build.

**A manifest is not a fixture, but it becomes one.** When a build's instrument needs the set,
the manifest materializes as a tracked, frozen file under that cycle's `fixtures/` — the cycle
directory's shape is single-homed in `.claude/skills/vlt-lifecycle.md`. Freezing is the point:
a fixture built from the fix's shape passes because it was built to.

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

## When the fix site is off-cadence — `channel: platform`

*(Platform P-3, 2026-09-01.)* One intake, two destinations. Most filings describe shipped
behavior and land in the open cycle's roadmap. A filing whose fix site is **factory-side** —
a factory skill under `.claude/skills/`, `tools/`, `.github/`, a process doc, this README —
belongs on the **platform ledger** (`factory/platform/roadmap.md`) instead, because
`vlt-upgrade` never delivers it to a vault. Before P-3 such candidates reached that ledger
only by hand, which meant they reached it only when someone happened to remember.

Mark those filings `channel: platform` in the opening line (the same place `class:` goes) and
`inbox-capture` routes them to the ledger's **Queued** section rather than the cycle roadmap.

Two things the marker does **not** do. It is not self-service: capture grounds a marked
filing like any other and **the boundary is re-derived, not trusted** — a filing that marks
itself platform but names a fix under the shipped surface (`skills/vlt-*`,
`.claude-plugin/`) is routed to the cycle roadmap with the mis-mark reported, and an unmarked
filing whose only fix site is factory-side is surfaced to the owner rather than silently
re-routed. And it is optional: the boundary rule is the ledger's, and an unmarked filing is
routed the ordinary way, so nothing regresses if the marker is never used.

The boundary itself — *"an item is platform iff `vlt-upgrade` does not deliver it to
vaults"* — is single-homed in the platform ledger's channel contract. Read it there.

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
