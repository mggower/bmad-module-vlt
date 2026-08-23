# Tracker sync — the roadmap, projected onto GitHub (one-way)

*(Born in platform item P-10. This file is the single home of the sync's mechanics and
of the `stage:`/`check:` label set. The field contract at
`skills/vlt-feedback/references/field-contract.md` is a different, untouched surface —
see "Two populations" below.)*

The cycle roadmap does by hand what a milestone and a label set do for free: progress,
position, and the inherited-debt story. This mode projects the open cycle's roadmap onto
the tracker so the loop is readable by someone who never opens a file. **One direction
writes:** disk is the source of truth, the tracker is a rendering. The sync never edits
the roadmap from tracker state — that is what makes hand-mirroring (the sync tax)
structurally impossible. Flipping source-of-truth to issues is explicitly a later item,
only if this proves out.

## Two populations, no overlap

- **Rail issues** are filer-authored, enter as `vault-filed`, and belong to the field
  contract. The sync never touches them, their labels, or their lifecycle.
- **Sync issues** are factory-authored, titled `B<NN>-<i> — <slug>` (the build id), and
  exist only as projections of roadmap state. The rail never creates issues shaped like
  that, so the populations are disjoint by construction — no precedence rule needed.

The one sanctioned link between them: when a rail issue's filing is captured into a
build, `github-intake`'s captured-comment may name the build issue (`captured into #n`)
— that comment is the intake's, not the sync's.

## What the sync owns on the tracker

| Roadmap object | Tracker object | Derivation |
|---|---|---|
| The open cycle | Milestone `Cycle NN — <Title>` (title from the roadmap's `title:`) | created open; closed when the roadmap stamps CLOSED |
| A build in the Ideation rulings | Issue `B<NN>-<i> — <slug>`, milestoned | created at first sync after the build is ruled |
| The build's lifecycle position | One `stage:` label (see the ladder below) | re-derived each sync from the same observables the lifecycle map names |
| The build's acceptance checks | A task list in the issue body, each line tagged `(ship-verifiable)` or `(field-contingent)` | from the cycle ledger; checked lines mirror discharged items |
| Undischarged check kinds | `check:ship-verifiable` / `check:field-contingent` labels | applied while any unchecked line of that kind remains; both may coexist |
| Inherited debt | The existing issue **re-milestoned** to the new cycle, never recreated | GitHub's own timeline then tells the carry story |
| A closed cycle | Milestone closed; still-open build issues carry to their new milestone or close with the roadmap's disposition | |

**The `stage:` ladder** (one label at a time, matching the map's positions):
`stage:captured` → `stage:ideated` (rulings filled) → `stage:reviewed` (roundtable
record or waiver) → `stage:briefed` (brief `BRIEFED`) → `stage:built` (brief `BUILT`) →
`stage:released` (the cycle's tag exists) → `stage:accepted` (its ledger items checked
or owner-carried; the issue closes). Stages derive from disk observables — the
lifecycle map (`.claude/skills/vlt-lifecycle.md`) is the authority on what state means
what; this table adds only the label names.

## Mechanics

1. **Resolve** the open cycle: `factory/CYCLE` → `factory/cycles/<that>/roadmap.md`.
   A `none` pointer syncs nothing forward-looking but may still close out the previous
   cycle's milestone/issues if the roadmap just closed.
2. **Derive** the desired tracker state per the table — cheap reads (rulings headings,
   brief `status:` lines, ledger checkboxes, `git tag`), the same observables
   `lifecycle-status` walks.
3. **Diff** against the live tracker: find the milestone by exact title, issues by exact
   `B<NN>-<i> — ` title prefix. The sync edits only objects it owns and only the
   `stage:`/`check:` label namespaces — it never adds or removes any other label.
4. **Batch gate — same constitution as triage:** render every planned operation (exact
   `gh` commands, exact issue bodies) and **HALT for the owner's batch ruling**. These
   are public writes; nothing posts unapproved, and there is no headless path across
   the gate. Idempotent by construction: a re-run after a partial apply re-derives and
   re-diffs.
5. **Apply** approved operations; report per-op outcomes with paste-ready residue for
   any failure, exactly as the triage apply does.

Transport and auth are the triage pre-flight's (`gh-missing`/`gh-unauthenticated`,
reported by name). Run the sync after any lifecycle transition, or whenever — it is a
projection, so running it late loses nothing.

## Label + fixture bootstrap (owner, once; idempotent via --force)

The `stage:`/`check:` labels — defined here, never in the field contract:

```
gh label create "stage:captured"  --repo mggower/bmad-module-vlt --force --color BFD4F2 --description "Tracker sync: build captured into the open cycle"
gh label create "stage:ideated"   --repo mggower/bmad-module-vlt --force --color BFD4F2 --description "Tracker sync: ideation rulings filled"
gh label create "stage:reviewed"  --repo mggower/bmad-module-vlt --force --color BFD4F2 --description "Tracker sync: roundtable record (or waiver) covers it"
gh label create "stage:briefed"   --repo mggower/bmad-module-vlt --force --color 8EB4E3 --description "Tracker sync: brief written (BRIEFED)"
gh label create "stage:built"     --repo mggower/bmad-module-vlt --force --color 5B92C9 --description "Tracker sync: brief status BUILT"
gh label create "stage:released"  --repo mggower/bmad-module-vlt --force --color 2D6BAF --description "Tracker sync: shipped in the cycle's release"
gh label create "stage:accepted"  --repo mggower/bmad-module-vlt --force --color 0E4C90 --description "Tracker sync: acceptance discharged; issue closes"
gh label create "check:ship-verifiable"  --repo mggower/bmad-module-vlt --force --color 0E8A16 --description "Tracker sync: undischarged ship-verifiable checks remain (gates closeout)"
gh label create "check:field-contingent" --repo mggower/bmad-module-vlt --force --color C2E0C6 --description "Tracker sync: undischarged field-contingent checks remain (never gates)"
```

The pinned **"How this project evolves"** issue is created once by the owner (or an
approved sync run) and pinned with `gh issue pin` — it points at the README section and
`factory/`; the sync never edits it.
