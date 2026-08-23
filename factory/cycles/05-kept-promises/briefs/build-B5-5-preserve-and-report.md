---
title: 'Build #B5-5 — preserve & report (the vlt-upgrade honesty pair: the preserve set widens from a name test to the provenance test B1 already uses, and the ledger''s required lines get the close-out check that makes them hard to drop)'
status: 'BUILT 2026-07-29 — F1–F6 landed in `vlt-upgrade/SKILL.md` as briefed: Step-1 bullet retitled **Local mints** with the provenance test (per-kind shipped definition, both-kinds bracket-path fallback) + the Overview both-kinds phrase; Step-2 prohibition widened to "unshipped local-mint `vlt-*` dir (partner **or** vault-grown operation skill — the Step-1 provenance test)"; Step 3.1 confirm + Step 3.2 restore widened to local mints; report placeholders/comments (`mints_preserved:`/`bodies_restored:`) and the ledger Mints-preserved comment broadened (key names kept, per disposition 1); Verify widened to local-mint dirs and extended with the nine-line ledger field-completeness check; the one-sentence required-lines annotation added after the Step-5 template. `vlt-mint:168` and `merge-help-csv.py` deliberately unedited, per the out-of-scope dispositions. Verification: widening grep clean (survivors: Overview partner-mention beside the op mention, the :34 agents[] sub-clause, the loop-profile partner scan); Verify list ↔ Step-5 template one-to-one (nine lines); dry-read coherent Step 1→Verify; B1 fixture run PASS (`local_mints_preserved: [vlt-agent-x, vlt-fizzbin]`, zombie dropped); vlt-mint:168 promise confirmed true under the widened Step 1, no edit; package-lint A/B/C/E PASS; scrub clean (no filing instance names added; the one `vlt-core` grep hit pre-exists at HEAD in Step 3.7); no `.decision-log.md`. Deviations/notes: (1) the Overview own-the-apply bullet (:17, "never touching unshipped `vlt-agent-*` dirs") is a seventh name-scoped surface not in the brief''s F-list — widened to "unshipped local-mint `vlt-*` dirs" so no prohibition surface survives name-scoped (verification checks 1 and 3 require it). (2) The frontmatter `description:` ("without destroying minted partners / local convention overlays / mint history") left unchanged — an examples list, not a preserve-set claim, and outside the brief''s scope. (3) No commit made — owner directed the tree stay uncommitted (release choreography rides the arc level, as with B5-4), overriding this line''s prior one-commit exit obligation.'
module_code: 'vlt'
created: '2026-07-29'
derives_from:
  - 'inbox/2026-07-25-183003-upgrade-preserve-set-misses-vault-grown-op-skills.md (A5-2 — B1 preserves provenance-based while B2''s Step-1 snapshot is name-scoped to `vlt-agent-*`, so a vault-grown `vlt-{op}/` op skill is never snapshotted; vlt-mint Step 4 promises it is; the §5 exact-change wording + the mints_preserved broaden-vs-add question)'
  - 'inbox/2026-07-29-120003-sayari-upgrade-omitted-convention-adoption-line.md (A5-17 — the never-omit adoption line survived one of two field executions; capture''s PROVENANCE CORRECTION: the template already names the line, the genuine gap is that Verify checks a dated block exists, never that it carries its required fields)'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): grouping (B5-5 = A5-2 + A5-17, "Preserve & report" — the vlt-upgrade honesty pair, ships fifth; "A5-17 pairs here by shared skill, not with A5-15"); questions-designated (A5-2''s broaden-vs-add on `mints_preserved:` and A5-17''s Verify-side check vs template-side required markers are this brief''s to rule — dispositions 1–2)'
risk: 'low — prose-only edits to one skill (`vlt-upgrade/SKILL.md`) plus a verify-only read of `vlt-mint`; no convention touched, no version bump, no consumer walk, no workflow JS; the build touches the B1/B2 local-mint preserve path, so the durability-posture standing re-check (CLAUDE.md) runs at verification'
---

# Build #B5-5 — preserve & report

Goal: make `vlt-upgrade`'s two honesty seams tell the truth the skill already claims. A5-2:
`vlt-mint` Step 4 reassures every minter that "a local mint's durability is the merge's job —
B1 preserves its live-registry row and B2 restores its body" — and B2's half is false for a
vault-grown **operation skill**, because B1's preserve test is provenance-based
(`merge-help-csv.py` — absent from the bundled source, dir exists live, no name test) while
B2's restore source, the Step-1 snapshot, is name-scoped to `vlt-agent-*`: a `vlt-{op}/` dir
matches no Step-1 bullet, is never snapshotted, and B1 ends up preserving a registry row that
points at a directory a destructive apply can have deleted. The class is populated at both
known installs; the false reassurance already deflected a live durability objection once
(filing §6). A5-17: the post-flight `convention_adoption:` line is specified **never omitted
when empty** — and one of its two field executions omitted it anyway; the capture's
provenance correction relocates the fix from the template (which already names the line) to
the skill's close-out: **Verify checks that a dated ledger block exists, never that it
carries its required fields**, so a skipped line survives the skill's own exit gate. The
build widens the Step-1/B2/prohibition/report/ledger surfaces from the name test to the
provenance test B1 already uses, and gives the ledger's required lines a Verify-side
field-completeness check.

All rejected alternatives in the parent filings are settled — do not re-litigate. A5-2's §5
suggested wording is owner-steered input, consumed in F1 (the B5-3/B5-4 precedent for
filing-suggested shapes); its two designated questions and A5-17's live fork are ruled in
dispositions 1–2 below.

**Re-grounding (2026-07-29, HEAD `2f19251` + B5-4's uncommitted working-tree edits — the
grounding baseline is the working tree, since B5-4 edited `vlt-upgrade/SKILL.md` extensively
and is not yet committed): clean, zero grounding corrections.** Every A5-2 capture site HOLDS
at its cited line in the current tree: the name-scoped *Minted partners* bullet
(`vlt-upgrade/SKILL.md:34`), no bullet among `:35-40` catching a vault-grown `vlt-{op}/` dir,
the Step-2 own-the-apply prohibition "never delete an unshipped `vlt-agent-*` dir" (`:48`),
B2's "each minted-partner dir in the Step-1 snapshot" (`:66`), the partner-only report fields
(`:97-98`), the partner-only ledger lines (`:124-125`), the `vlt-mint` durability promise
(`vlt-mint/SKILL.md:168`), `vlt-mint` minting op skills as a first-class kind
(`:131`, `:170`), and B1's provenance test with no name clause
(`merge-help-csv.py:192-230`, JSON key `local_mints_preserved` at `:374`). Every A5-17 site
HOLDS: the `convention_adoption:` report key (`:105`), the never-omit rule (`:112` — now
carrying B5-4's declared-since age, which changes nothing about this build's scope), the
ledger template's adoption line (`:131`), and Verify checking only "the ledger has a new
dated block" (`:146`). Two **grounding additions** (EXPANDED), both inside the filings'
letter: (1) Verify's own sentence "every minted-partner dir from the Step-1 snapshot still
exists (Step 3.2)" (`:146`) is a **sixth name-scoped site** the widening must touch, beyond
the capture's residual-scope list (`:34`, `:48`, `:66`, `:97-98`/`:124`, `vlt-mint:168`).
(2) Step 3.1's confirm clause "Confirm the JSON `local_mints_preserved` lists every
**partner** from the Step-1 snapshot" (`:64`) under-claims what the script already does — the
JSON key names the wider class and the script already preserves op-skill rows
provenance-based; the clause widens with the rest (F3).

## Brief-time dispositions

1. **A5-2's `mints_preserved:` question — RULED: BROADEN, never add a sibling field** (the
   designated question; the filing's own stated default — "I'd default to broadening rather
   than adding a field" — adopted). Adding a partner field and an op-skill field would
   re-create in the report surface exactly the partner/op split whose divergence *is* this
   defect: B1 and B2 diverged because one got the general rule and one got a special case
   (filing §2). The preserve class is **one class** — local mints, defined by provenance —
   so it reports through one field. The key **name** `mints_preserved:` (and the ledger line
   "Mints preserved") is kept, not renamed: renaming would churn every existing ledger
   entry's readability for nothing, "mints" is already the accurate class word (`vlt-mint`
   mints both kinds), and the merge script's own JSON key `local_mints_preserved` already
   reads this way. What broadens is the **description and placeholders** — the comments and
   examples stop implying partners-only (F4).
2. **A5-17's live fork — RULED: the Verify-side field-completeness check is the mechanism;
   the template gets a one-line required-lines annotation as a cheap belt, not the
   load-bearing fix** (the designated question, as sharpened by the capture's grounding
   note: the filing's template-side option "already exists" — `:131` lists the adoption line
   exactly as Mints/Overlays/Migrations are listed — so the live fork is Verify-side check
   vs required-vs-optional markers). The failed execution skipped a line the template
   already named, which means template-side markers rely on precisely the write-time
   attention that already failed once out of two runs; only a close-out check catches the
   skip mechanically, and Verify is the skill's existing exit gate — the natural home
   (`:146`). The annotation (F6) costs one sentence and makes the template's contract
   explicit ("every line is required; a line with nothing to report says none"), but the
   check is what makes the rule hard to drop. **The capture's open sub-question — whether
   the post-flight *report* (`:92-108`) needs the same completeness net — is ruled NO:** the
   ledger is the durable record (the artifact the filing's cross-vault diff read, and the
   only one acceptance can read after the fact); report and ledger are completed in the same
   post-flight beat from the same data, so a Verify check anchored on the persisted artifact
   disciplines the beat itself, and a second net over a transient surface would be a
   restatement, not a protection.

## F1 — `vlt-upgrade/SKILL.md` Step 1: the snapshot bullet widens from name to provenance

**Current state.** `vlt-upgrade/SKILL.md:34` — the first pre-flight bullet is **"Minted
partners** — every `vlt-agent-*` dir under the live skills dir whose code is **not** a
shipped agent in the **incoming module source's** `module.yaml agents[]`…", followed by the
(correct, kept) pristine-incoming-source caveat and the bracket-path fallback. No bullet in
`:35-40` catches a vault-grown `vlt-{op}/` dir — overlays (`:35`), base divergence (`:36`),
skill-asset divergence (`:37`), mint history (`:38`), capabilities (`:39` — scans
`{partners}/*/capabilities/*.md`, the agent zone, so a heavy capability's *pointer file* is
caught but the op-skill dir itself is not), governance (`:40`). Meanwhile `vlt-mint` mints op
skills as a first-class kind into `{module-skills}/vlt-{op}/` (`vlt-mint:131`, `:170`) — the
two skills disagree about what a vault can grow. The Overview (`:11`) carries the same
partner-only framing: "it mints its own `vlt-agent-*` partners".

**The change.**
- **`:34`** — retitle the bullet **"Local mints"** and widen its head to the provenance test,
  per the filing's §5 wording (adjusted to the current bullet's text): *every **`vlt-*` dir**
  under the live skills dir that is **not** shipped by the incoming module source — for a
  `vlt-agent-*` dir, "shipped" means present in the incoming `module.yaml agents[]` (the
  existing pristine-source caveat applies unchanged); for any other `vlt-*` dir, present in
  the incoming bundle's skills at all. This covers both minted **partners** and vault-grown
  **operation skills** — `vlt-mint` mints both, and B1's own preservation test
  (`merge-help-csv.py`) is provenance-based, not name-based, so this snapshot must be too.
  Record dir path + its help-registry row(s).* The existing `agents[]` caveat and its
  B1-mirroring rationale stay as-is; the **bracket-path fallback** sentence extends to cover
  both kinds (on the bracket path, fall back to the known-shipped set / live manifest for
  partners **and the live registry's shipped rows for other `vlt-*` dirs**, best-effort, and
  re-verify shipped-vs-local at reconcile once the incoming source is present — the existing
  deferral pattern, unchanged in shape).
- **`:11`** (Overview, one phrase) — "it mints its own `vlt-agent-*` partners" widens to name
  both kinds ("its own `vlt-agent-*` partners and vault-grown `vlt-*` operation skills"), so
  the skill's framing stops teaching the narrow class its own Step 1 just stopped enforcing.

**Why.** A5-2's core defect: B2 restores only what Step 1 snapshots, and Step 1's glob is the
bug ("the bug is the glob, not the source of truth" — the derive-first invariant at `:44` is
right and does not help here; deriving from disk still only finds what the enumeration looks
for). The invariant text itself needs no edit.

**Out of scope at this site.** The Capabilities bullet (`:39`) is unchanged — the agent-zone
pointer files it scans stay its concern; the op-skill *dir* is the widened Local-mints
bullet's.

## F2 — Step 2: the own-the-apply prohibition widens

**Current state.** `:48` — "**Refresh shipped files only**; never delete an unshipped
`vlt-agent-*` dir, never write into the agent zone…" — the prohibition protects only the
named prefix (the capture's grounding addition: a third name-scoped site).

**The change.** "never delete an unshipped `vlt-agent-*` dir" → "never delete an unshipped
local-mint `vlt-*` dir (a minted partner **or** a vault-grown operation skill — the Step-1
provenance test)". The rest of the sentence and the dev-cruft exclusion sub-bullet are
untouched.

**Why.** The prohibition is the own-the-apply path's half of the same promise; leaving it
name-scoped would license the merge-copy to delete exactly what Step 1 now snapshots.

## F3 — Step 3: B1's confirm clause and B2's restore widen

**Current state.** `:64` — "Confirm the JSON `local_mints_preserved` lists every **partner**
from the Step-1 snapshot" (grounding addition 2 — the script already preserves op-skill rows;
the confirm under-claims). `:66` — B2: "For each **minted-partner dir** in the Step-1
snapshot, confirm it still exists under the live skills dir. If a destructive apply removed
one, **restore it** from the snapshot."

**The change.**
- **`:64`**: "lists every partner from the Step-1 snapshot" → "lists every **local mint**
  from the Step-1 snapshot (partners and vault-grown op skills — the script's test is
  provenance-based and already covers both)".
- **`:66`**: "each minted-partner dir in the Step-1 snapshot" → "each **local-mint dir** in
  the Step-1 snapshot" (filing §5's exact B2 change). The no-op-on-own-path sentence stays.

**Why.** B2 is the restore half of the promise; with F1 the snapshot carries both kinds, and
this makes the restore read them. `merge-help-csv.py` itself needs **no change** — B1 was
always right (filing §2's table); that asymmetry is the whole finding.

## F4 — Step 4 + Step 5: the report and ledger surfaces broaden (disposition 1)

**Current state.** `:97-98` — `mints_preserved: [<vlt-agent-x>, ...]  # registration kept`
and `bodies_restored: [<vlt-agent-x>, ...]  # B2 — empty on the own path`: the placeholders
teach partners-only. `:124-125` — ledger lines "- Mints preserved: `<list>` # local partners
kept registered" and "- Bodies restored: `<list or none>` # B2".

**The change** (broaden, never add — disposition 1; key names and line labels unchanged):
- **`:97`**: placeholder + comment become `[<vlt-agent-x>, <vlt-op>, ...]  # registration
  kept — every local mint (partners + vault-grown op skills)`.
- **`:98`**: placeholder likewise `[<vlt-agent-x>, <vlt-op>, ...]`; comment stays "B2 — empty
  on the own path".
- **`:124`**: comment becomes "# local mints kept registered (partners + op skills)".

**Why.** A5-2's smaller second change, as ruled: the widened set is visible in the ledger
through the field that already reports the class, described honestly.

## F5 — Verify: the widened dir check + the field-completeness check (disposition 2)

**Current state.** `:146` — Verify checks "every **minted-partner dir** from the Step-1
snapshot still exists (Step 3.2)" (grounding addition 1 — the sixth name-scoped site), and
"the ledger has a new dated block" — existence only, never field-completeness (A5-17's
genuine gap, per the capture's provenance correction): a skipped required line survives the
skill's own close-out, which is exactly how the second field execution shipped without its
adoption line.

**The change.**
- Widen: "every minted-partner dir from the Step-1 snapshot still exists (Step 3.2)" →
  "every **local-mint dir** from the Step-1 snapshot still exists (Step 3.2)".
- Extend the ledger clause: "the ledger has a new dated block" → "the ledger has a new dated
  block **and that block carries every line the Step-5 template names** (Mints preserved,
  Bodies restored, Overlays, Base divergence, Skill-asset divergence, Migrations, Governance
  divergence, Convention adoption, Notes) — re-read the appended block and check each line is
  present; a missing line is a defect to repair before closing, per the never-omit rule
  (Step 4): an absent line reads as 'nothing to report' without ever saying so."

**Why.** A5-17 in one sentence: the spec was right, the template was right, and one execution
out of two dropped the line anyway — reliability wants a mechanical net at the moment the
skill already stops to check itself. The line list is enumerated deliberately: it is the
completeness check's own checklist, and it must agree with the Step-5 template (verification
check 2 pins that agreement).

## F6 — Step 5: the template's required-lines annotation (disposition 2's belt)

**Current state.** The ledger-entry template (`:118-133`) lists nine lines; several say
`<list or none>`, the adoption line says `<list>`; nothing states that every line must
appear in every entry.

**The change.** One sentence directly after the template block: *Every line above is
required in every entry — a line with nothing to report says "none" (the adoption line uses
its three-valued read, Step 4); omitting a line entirely is the failure the Verify
completeness check exists to catch.* Point, don't restate: the never-omit rationale's single
home stays the Step-4 `convention_adoption` paragraph (`:112`).

**Why.** Cheap explicitness at the write site; the check (F5) remains the mechanism.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row. No convention is touched —
no `version:` moves, no consumer walk, no re-ack (`vlt-upgrade`'s own `depends_on: ["spec@2"]`
is untouched). No structure-map change. Not the release build — no version-string bumps (they
ride the arc's release build).

## Out of scope (dispositioned)

- **`vlt-mint/SKILL.md:168` ("…and B2 restores its body")** — **no edit**: the filing's §5
  third point rules it — the sentence becomes true the moment the Step-1 widening ships in
  the same release, and this build is that ship. A confirming read is verification check 5;
  editing it would add a qualification the same release makes false.
- **`merge-help-csv.py`** — no change: B1 is the half that was always right
  (provenance-based, `:192-230`); the standing durability-posture re-check exercises it
  against a fixture (verification check 4) rather than editing it.
- **Renaming `mints_preserved:` / "Mints preserved"** — rejected (disposition 1): churns
  ledger readability for nothing; "mints" is the accurate class word.
- **A completeness net over the transient post-flight report (`:92-108`)** — rejected
  (disposition 2): the ledger is the durable artifact; one net, anchored where the record
  persists.
- **A5-4's `vlt-upgrade` seams (decision-log reconcile extension, lint memory)** — B5-6's,
  per the grouping ruling; the capture's "upgrade-machinery pair" (A5-2, A5-4) was
  observation, not grouping, and the owner grouped them apart.
- **A5-15's stamp machinery in this skill** — shipped by B5-4 (carry-forward, adoption-aware
  pre-flight, retrofit stamp beat); nothing here touches those lines beyond coexisting with
  them.
- **A live destructive-apply drill for B2's op-skill restore** — not staged: the exposure is
  latent by design on the own-the-apply path (filing §4 — merge-copy, no `--delete`; B2 is
  insurance), and no vault has a reason to take a destructive path on demand. The at-rest
  read (verification 3) and the ship check cover what is boundable; writing a
  field-contingent check that needs a vault to break itself would measure the wrong thing.
- **A factory report-contract lint (required-lines tracing in `package-lint.py`)** — routed
  by ships-decides as ordinary arc work if taken up; not this build (the standing B5-3/B5-4
  disposition, unchanged).

## Verification (unit, at rest)

1. **Widening grep** — `grep -n 'minted-partner\|vlt-agent-\*' skills/vlt-upgrade/SKILL.md`:
   no snapshot/prohibition/restore/confirm/verify path is still name-scoped; every surviving
   `vlt-agent-*` occurrence is genuinely partner-specific (the `agents[]` pristine-source
   caveat, partner placeholders beside op placeholders, the Overview's partner mention beside
   the op-skill mention).
2. **List-vs-template agreement read** — the Verify completeness check's enumerated line list
   (F5) matches the Step-5 template's lines (`:124-132`) exactly, one-to-one; a line added to
   either later must move both (they are two renderings of one contract, and this check is
   the at-rest pin).
3. **Dry-read coherence** — Step 1 → Step 2 → Step 3.1/3.2 → Step 4 → Step 5 → Verify all
   speak the widened class consistently ("local mints", both kinds); B2's restore reads a
   snapshot that now contains what it restores; nothing still promises partner-only.
4. **B1 durability re-check (CLAUDE.md standing rule — the build touches the preserve
   path)** — real script run against a temp fixture: a target CSV carrying a `vlt-agent-x`
   partner row, a `vlt-{op}`-style op-skill row (both absent from a minimal source CSV), and
   a zombie row with no live dir; a temp live-skills-dir containing the two live dirs. Run
   `merge-help-csv.py --live-skills-dir`; the JSON `local_mints_preserved` lists **both**
   local mints and the zombie is dropped. (Expected to pass unchanged — the check documents
   that the build did not regress the half that was right.)
5. **`vlt-mint` promise read** — `vlt-mint/SKILL.md:168`'s "B1 preserves its live-registry
   row … and B2 restores its body" is confirmed true under the widened Step 1 (no edit made;
   the out-of-scope disposition recorded as verified).
6. **Packaging lint** — `uv run tools/package-lint.py` A/B/C/E PASS (D / `--expect-version`
   is the release gate, not this build's). No handshake surface moved, so Group E is
   expected unchanged — run it anyway (it is the check of record, not a grep).
7. **Scrub** — no personal/vault-local content in the changed shipped file: the filings'
   concrete instances (`vlt-file-feedback`, `vlt-hub`, vault names) stay out of
   `skills/`; placeholders use the `vlt-{op}` / `<vlt-op>` style.
8. **No `.decision-log.md`** in the working tree at commit time.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** the widened preserve set and the completeness net reach the field
   and self-exercise — on the next ordinary vlt-core upgrade: (a) the installed
   `vlt-upgrade/SKILL.md` carries the *Local mints* provenance bullet, the widened Step-2
   prohibition, the widened B2/confirm wording, the broadened `mints_preserved:` report and
   ledger descriptions, the template's required-lines annotation, and the Verify
   field-completeness check — grep-checkable on the installed vault; (b) that upgrade's
   Step-1 snapshot and its `mints_preserved:`/ledger line name vlt-core's standing
   vault-grown op skill (`vlt-file-feedback`) as a local mint — the widened path is forced,
   not hypothetical, because the dir is already standing, and under the 0.8.0 wording it
   would be omitted from the snapshot, so this clause can fail; (c) the upgrade's own ledger
   entry carries every required template line, Convention adoption included — the
   completeness check's first live exercise. Bounded — the upgrade happens anyway.
2. **[field-contingent]** the reliability fix holds where it failed — the next
   **vlt-sayari** upgrade's ledger entry carries the Convention adoption line (and every
   required template line): the exact execution shape that dropped the line at 0.8.0
   (Arc 4's A4-2 clause-7 adoption-half FAIL), re-run under the completeness check.
   Producing vault: **vlt-sayari on the work machine — the factory cannot read it**; the
   owner runs that upgrade on their own cadence and files the ledger evidence back (the
   B5-1 check-2 pattern). Non-gating at closeout; until it lands, the fix is proven shipped
   and self-exercised (check 1) but not proven on the vault that failed.
