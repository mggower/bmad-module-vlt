---
name: issue-triage
description: Grounds open rail issues against module source and rules them accepted or declined in one owner-approved batch; also projects the open cycle's roadmap onto the tracker as milestone + build issues + stage labels (one-way sync). Use when the user says 'run issue triage', 'triage the tracker', or 'sync the tracker'.
---

# issue-triage

## Overview

The factory-side triage step for the remote feedback rail. `github-intake` (the capture
half) only respects triage *results* — an issue sits `vault-filed` and invisible until the
owner admits or declines it. This skill moves that work in-session: it discovers the
untriaged queue, **grounds every issue claim against current module source before any
verdict is drafted** (inbox-capture's grounding discipline, applied at stage-0), and
renders one batch table for the owner to rule.

**Admission and decline remain owner verbs** — `github-intake`'s "What this file does not
own" stays true. This skill grounds, drafts, and (only after the owner's batch ruling)
applies the ruled results via `gh` under the field contract's **voice rule**
(single-homed there; no headless path across the gate).

Every rail shape — labels, state flow, payload fields, `rail_contract` and its evolution
rule — is single-homed at `skills/vlt-feedback/references/field-contract.md`. This file
cites the contract everywhere and restates none of it. The issue thread is the durable
triage record: verdicts land as labels plus a comment carrying the grounding evidence;
nothing new is stored factory-side, and there is no watermark — the queue re-derives from
the rail every run.

## On Activation

Resolve the transport repo `<repo>` exactly as `github-intake` does: `feedback_repo.default`
from `skills/vlt-setup/assets/module.yaml` (the factory has no vault `config.yaml`).

**Pre-flight:** `gh` not on PATH → named error **`gh-missing`**; `gh auth status` non-zero
→ **`gh-unauthenticated`**. Either way report the error by name and stop — never render a
failed pre-flight as "queue empty".

`--report` / report-only: run Discovery and Grounding, render the table, and stop before
the gate (no `gh` write of any kind). Headless runs are report-only by construction: emit
the table as JSON with `status: "awaiting-owner-batch-ruling"`.

## Discovery — the queue is derived, never remembered

1. **Untriaged queue:**
   `gh issue list --repo <repo> --label vault-filed --state open --json number,title,labels,body,createdAt`
   — keep those carrying **neither** `vault-accepted` **nor** `captured`. That set is the
   queue; no state file, no watermark (untriaged is a property of the rail, re-derived
   each run).
2. **Off-rail sweep (report-only):** open issues without `vault-filed` are off the rail by
   construction (the contract's state flow). List them under "off-rail traffic — owner
   discretion"; this skill never triages them.
3. **Amendment sweep (report-only):** open `captured` issues carrying `amended` are
   surfaced and routed: consumption is the intake's — `github-intake.md`'s amendment leg
   appends the admitted comment(s) and clears the label, cited not restated. Route: run
   `inbox-capture`; this skill never appends.

## Stale-shape gate

Before grounding an issue, compare its body's `rail_contract` stamp to the current
contract version. Mismatch or missing stamp → **held for hand-handling** per the
contract's evolution rule (`field-contract.md:15-22`): no verdict drafted, no label
change. Report it in its own table section.

## Grounding — before any verdict

Per issue, against module source as it sits on disk:

- Verify each concrete claim (`what_happened`, `evidence`) at `file:line`; treat
  `provenance_guess` as exactly that — a guess to check, not a finding.
- Check classification: the body's `kind` field against the `field:*` label. The contract
  makes triage an authorized applier of classification labels — a mismatch gets a drafted
  label fix, with the body's `kind` authoritative. For `kind: supersession`, also confirm
  both halves are present (`superseded_rule`, `superseding_mechanism`) — a missing half is
  a drafted `needs-info`, never a drafted re-kind to `candidate`.
- Check for duplicates: prior issues (open and closed) and existing `factory/inbox/`
  filings covering the same ground.

Filings regularly mis-attribute provenance or guess wrong fixes — grounding corrections
go into the draft verdict comment, so the issue thread carries the corrected read.

## Verdicts — the contract's verbs, nothing wider

Only the contract's label set exists (`field-contract.md:65-83`); this skill widens
nothing. Three draftable verdicts:

- **accept** → add `vault-accepted` (+ any ruled classification-label fix). The next
  `inbox-capture` run materializes it — that boundary is `github-intake`'s, untouched.
- **decline** → comment with a **stated reason**, then
  `--add-label declined --add-label "declined:<reason>"` (exactly one reason label, from
  the contract's label table — labels scope, prose explains), close. The closing comment
  still states the reason in prose, including any `#n` / filing pointer (upstream declines
  point the filer at BMAD-METHOD; a duplicate names the issue or filing it duplicates).
- **hold** → a plain hold is label-free (candidacy costs the factory nothing). When a
  question comment is drafted (the filing needs information only the filer has), the
  drafted ops include `--add-label needs-info` — the issue keeps `vault-filed` until the
  owner rules.

## The batch gate — mandatory, no exceptions

Render one table: per issue — number, title, gist, grounding evidence (`file:line`
facts), classification check, recommended verdict, and the **exact public bytes** of any
comment plus the exact label operations. Then **HALT for the owner's batch ruling.** The
owner rules per-row (amendments welcome); one approval covers the batch. Nothing posts,
labels, or closes without it — these are public, largely irreversible writes.

## Apply — one approved transaction

Per approved row, in order: comments first (`gh issue comment`), then labels
(`gh issue edit --add-label`), then closes (`gh issue close`) — so a decline never lands
label-first with its reason missing. A per-issue `gh` failure is reported by name; the
run continues, and every un-applied operation is printed as an exact paste-ready `gh`
command — never a silent drop.

## Report

Applied verdicts (issue → outcome), holds, stale-shape held set, off-rail and amendment
sweeps, and any paste-ready residue. **Next lifecycle move** (the map's routing
contract): accepted issues route to `run inbox-capture` (the intake's trigger is now
armed); an all-declined or empty run routes to the map's prevailing position.

## Tracker sync mode ('sync the tracker')

The skill's second mode, mechanics single-homed at `references/tracker-sync.md`: project
the open cycle's roadmap onto the tracker — milestone `Cycle NN — <Title>`, one issue
per ruled build (`B<NN>-<i> — <slug>`), a `stage:` label per lifecycle position, the
acceptance ledger as a task list with `check:` labels. **One direction writes** (disk →
tracker; the roadmap is never edited from tracker state), the sync touches only objects
it owns (rail issues are a disjoint population — see the reference), and every apply
passes the same owner batch gate as triage. Pre-flight, transport, and report discipline
are this skill's own, unchanged.

## References

- `skills/vlt-feedback/references/field-contract.md` — the single home of labels, state
  flow, payload fields, and the evolution rule. This skill derives from it.
- `references/tracker-sync.md` — the sync mode's mechanics and the `stage:`/`check:`
  label set (single home; not field-contract labels).
- `.claude/skills/inbox-capture/references/github-intake.md` — the downstream consumer of
  an `accept`; materialization and the `captured` transition are its, never this skill's.
- `.claude/skills/vlt-lifecycle.md` — position and routing.
