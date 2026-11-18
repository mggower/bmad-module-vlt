# Inbox — field filings from live vaults

This is where a vault files **field notes** back to the plugin: a defect hit in real use, a pattern worth naming, something that should ship. Each filing is one dated markdown note (`YYYY-MM-DD-HHmmss-slug.md`).

## The flow (since 1.0)

1. **A filing lands here.** Written directly, or materialised from a tracker issue by the `issue-triage` skill.
2. **A change is made on a branch.** The filing is grounded against current source first: filings regularly guess the wrong cause, and the change follows what the source shows.
3. **The package check runs:** `python3 tools/package-lint.py --expect-version X.Y.Z`, exit 0.
4. **The release is tagged and noted in `CHANGELOG.md`** (`vlt-release`). The filing moves to `factory/shipped/vX.Y.Z/`, and the issue it came from is answered and closed.

There are no cycles, roadmaps, briefs or acceptance ledgers after 1.0. Cycles 1 to 16 are history under `factory/cycles/`; each closed cycle's `filings/` holds what it resolved.

A filing that no longer applies is closed with a dated line at its top saying why, and moved the same way.

> **The two sections below are the pre-1.0 filing guidance, kept as written.** What they ask of a filing (carry the evidence, not a count of it; a `supersession` names both halves) still holds. The skills and files they name (`inbox-capture`, `acceptance-discharge`, `vlt-lifecycle.md`, cycle `fixtures/`) were removed with 1.0.

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
in its opening line (a retirement filed through the remote rail arrives as `kind: supersession`
and the factory intake writes this marker — `.claude/skills/inbox-capture/references/github-intake.md`
§4), and it carries **both halves** or it is not one:

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

- A filing can arrive as a GitHub issue on the plugin's public tracker. The field contract (payload shape, labels, the `origin:` header, the voice rule) is single-homed at `kits/core/files/resources/playbooks/feedback-field-contract.md`.
- `issue-triage` grounds each issue, the owner rules, and an accepted issue is written here with an `origin: <repo>#<n>` first line.
- When the release that answers it ships, the issue is commented on and closed (`vlt-release`, stage 8). A declined issue is closed at triage with a reason, and nothing is written here.

## Where processed filings live

- **Before 1.0:** each cycle's `filings/` under `factory/cycles/`, beside the closed roadmap that says why each is there. Filings closed when 1.0 superseded Cycle 16 are in `factory/cycles/16-closed-loops/filings/`, with the reasons in `2026-11-18-1.0-disposition.md`.
- **From 1.0:** `factory/shipped/vX.Y.Z/`.

This README maintains no list. Read the directories.
