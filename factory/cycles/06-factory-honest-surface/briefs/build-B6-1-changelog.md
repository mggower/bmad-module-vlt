---
title: 'Build #B6-1 — the changelog (eight tags say a version happened and nothing says what it contains; the authoring was done thirty-six times and thrown away)'
status: 'BUILT 2026-08-01 — CHANGELOG.md created at the repo root with six entries (v0.4.0…v0.9.0),
  all 26 build lines collected verbatim from archived brief titles; package-lint Group D learned
  its third artifact (D3, signature now carries root); test-package-lint gained three D cases;
  vlt-release choreography Stages 3/4/5/6 and SKILL.md rows 3/6 + Overview updated; build-brief
  gained the title-scrub constraint in brief-anatomy §1 and at its Exit gate. Verification:
  package-lint --expect-version 0.9.0 exit 0 "A/B/C/E PASS, D PASS"; flagless run exit 0 "D SKIPPED";
  both D negatives (missing heading, duplicated entry) exit 1 naming CHANGELOG.md; collection
  fidelity 26/26 mechanically re-derived; all six changed-paths lists reproduce exactly from
  git diff; six heading dates equal their tag dates; single-home and scrub greps clean; no
  .decision-log.md in the tree. Deviations/notes: (1) F3 acceptance is 9/11, not the brief''s
  11/11 — the harness was already red at HEAD (6/8) because build_fixture is stale against C6
  (B5-7), C8 (B5-9) and E2; cases 1 and 7 fail on that inherited debt and are unchanged by this
  build. Owner-ruled 2026-08-01: case 9 asserts "PASS group D" (the group-scoped idiom cases 2-8
  use) rather than exit 0, and the fixture debt is filed as
  inbox/2026-08-01-143000-lint-fixture-stale-against-three-builds.md rather than repaired here.
  All three new D cases (9, 10, 11) are green. (2) F7 not performed in this build. Owner-ruled
  2026-08-01: the four local re-annotations defer to the release run, where they land after the
  ff-merge to main — satisfying disposition 3''s ordering literally — and batch into the same
  Stage 7 push the brief already routes them to. Exact commands are in §F7 of this brief.
  (3) F4''s Stage 7 backfill bullet could NOT be written: the edit was refused twice by the
  environment''s command classifier for containing force-push instructions. Stage 7 is otherwise
  unchanged, as the brief specified. The exact text the owner should paste is in the build report.
  (4) Brief error, corrected: F1 states builds 12 and 13 carry no trailing parenthetical — both do,
  and in fact all 26 titles do, so the "theme stands alone" fallback branch is never exercised.
  (5) Grounding note, not actioned: vlt-release SKILL.md''s own frontmatter description: still
  reads "dual version bump" — the same lying-map defect F5 fixes at three sites, at a fourth the
  brief did not name. Left for the owner rather than silently widening scope.'
module_code: 'vlt'
created: '2026-08-01'
derives_from:
  - 'inbox/2026-07-31-075115-release-changelog-practice.md (A6-1 — the whole filing: CHANGELOG.md retro-fill, package-lint Group D third artifact, choreography Stages 5+6, the build-brief title scrub, the lapsed-annotation drift)'
roadmap: 'skills/reports/inbox-evolution-arc6-roadmap.md'
rulings: 'roadmap §Ideation rulings — A6-1 (2026-08-01): one-build arc (B6-1); floor at v0.4.0 with NO v0.3.0/v0.3.1 entry and no caveat block (superseding the earlier in-session reconstruct ruling); re-annotate all four lightweight tags in place; breaking-change taxonomy deferred and `requires:` does NOT ship; entries never mention acceptance; the A/B/C/E staleness rides along; the entry is the single home for what-ships and Stage 5 drops its body paragraph; release-index.md is factory process record, NOT in this build.'
risk: 'low-moderate — no shipped vlt-* skill changes and no convention version moves (no consumer walk), but the build adds a new assertion to the release gate every future tag must satisfy, and force-updates four tag refs on a public remote.'
---

# Build #B6-1 — the changelog

## Intent

The module ships an enforcement machine that makes vaults keep their promises, and its own
public surface records that eight versions happened while saying nothing about what any of
them contains. A6-1's grounding established that this is **not a request to start a practice**:
the practice already runs. Every one of the 36 archived build briefs carries an authored
`title:` written by someone who understood the change — and every one of them lives in a
gitignored directory. The work exists; it has never had an output file.

This build gives it one. `CHANGELOG.md` lands at the repo root with six entries collected
(not authored) from the brief record, floor `v0.4.0`. `tools/package-lint.py` Group D — already
a pure equality check over version-bearing artifacts — learns a third artifact, so the rule
lives in the only file a fresh clone can see rather than in gitignored prose. The release
choreography stops restating what ships in the commit body (the entry is now its single home)
and restores the tag annotation it silently dropped when `git tag` was written bare into
Stage 6. `build-brief` gains the one constraint that promoting `title:` to public prose
requires.

Closes A6-1 in full, less the four items ideation ruled deferred. **All rejected alternatives
in the parent filing are settled — do not re-litigate**, in particular: no `v0.3.0`
reconstruction is owed (see disposition 1), `requires:` does not ship, entries never mention
acceptance, and `release-index.md` is out of this build entirely.

## Grounding record (2026-08-01, HEAD `f3b343d` = the `v0.9.0` tag commit)

Every capture-time site was re-derived against current source. **Zero grounding corrections** —
nothing has moved since capture (Arc 6 has shipped no builds, and HEAD is the same commit
capture ground against). Sites confirmed at their cited lines: `check_group_d`
`tools/package-lint.py:402-409`; the summary line `:619`; the Group-D docstring `:36-37`;
choreography Stage 4 exemplar `:72`, Stage 5 `:84`/`:86`/`:99`, Stage 6 `:110`;
`build-brief/references/brief-anatomy.md:17`; `build-brief/SKILL.md:112` (the Exit gate
heading). `find . -iname 'CHANGELOG*'` still returns nothing; `git tag` still returns eight,
four annotated (`v0.3.0`, `v0.3.1`, `v0.4.0`, `v0.6.0`) and four lightweight (`v0.5.0`,
`v0.7.0`, `v0.8.0`, `v0.9.0`).

**Four grounding additions** (in scope beyond the capture's letter, each named at its F-site):

1. `tools/test-package-lint.py` — capture never named it. A Group-D rule change that ships
   without a negative case is the class of defect Group D exists to catch. **F3.**
2. `check_group_d`'s signature `(expect, versions)` carries no `root` — the changelog check
   needs the filesystem, so the signature and its call site `:597` both move. **F2.**
3. `.claude/skills/vlt-release/SKILL.md:56` and `:59` restate Stages 3 and 6 in the stage
   table; editing the choreography without them leaves the router lying. **F5.**
4. The module docstring `:12-51` documents each group's assertions; Group D's two lines
   `:36-37` are part of the edit, not commentary on it. **F2.**

## Brief-time dispositions

The roadmap left six questions to brief time. Each is ruled here, citing the ruling it
derives from. Nothing ideation already ruled is re-opened.

**1. The entry schema — RULED: bespoke and collection-shaped, not Keep a Changelog.**
Keep a Changelog's file-level conventions are adopted (one dated section per released version,
reverse-chronological, ISO dates, "notable changes" framing). Its **category taxonomy**
(`Added` / `Changed` / `Fixed` / `Deprecated`) is rejected: sorting 26 builds into categories
is *authoring*, and the whole reason this build is cheap is that it is **collection** — the
roadmap's own opening property, and the thing a taxonomy would quietly destroy. Every entry
therefore carries exactly four things, all of them derivable: the version + date heading, one
arc line, one bullet per build, and a changed-paths line. `requires:` is absent by ideation
ruling 3.

**2. One scope sentence in the preamble, and nowhere else — a bounded extension of ruling 1.**
Ruling 1 forbids a `v0.3.0`/`v0.3.1` entry and forbids a caveat block. It is read here as
forbidding *per-entry apology*, not as forbidding the file from saying where its record
begins: a changelog that starts at `v0.4.0` with no statement of its floor is exactly the
mute surface this arc exists to close. The build writes **one factual sentence** in the file
preamble — the record begins at `v0.4.0`; earlier tags predate the per-build commit history
entries are derived from — with no apology, no reconstruction, and no second occurrence
anywhere in the file. Flagged as a bounded extension so the owner can overrule it by deleting
one sentence. *(Note in passing: the floor makes capture's "builds 1–2 are labels, not prose"
residual moot — builds 1–10 sit below it and never enter the file.)*

**3. Re-annotation mechanics — RULED: local `-f` re-annotation in the build; the four
force-pushes are owner-confirmed and batched into the release's Stage 7.**
Message text is **collected, not written**: each lightweight tag's own release-commit subject
already has the exact shape of the four surviving annotations (`vlt X.Y.Z — Arc N: <name>
(builds …)`), so `git log -1 --format=%s <tag>` *is* the message. Ordering: `CHANGELOG.md`
lands and is committed on `main` before any tag is touched, so no annotation points at a
record that does not exist. The build performs the four local `git tag -a -f` operations and
**stops there**, leaving the exact push commands in its report — rewriting refs on a public
remote is outward-facing, and this repo has exactly one owner-confirmed outward-facing moment
(choreography Stage 7). Derives from ideation ruling 2, which ruled the re-annotation but sent
the mechanics here.

**4. Group D's assertion — RULED: existence + exactly one correctly-dated heading; no content
assertion; and the lint stays git-free.**
D3 asserts `CHANGELOG.md` exists at the root and contains **exactly one** line matching
`^## v{expect} — \d{4}-\d{2}-\d{2}$`. Exactly-one (not at-least-one) guards a re-cut release
appending a second block for a version that already has one. It asserts nothing about the
entry's body — a lint that graded prose would be the proxy-check failure B5-3 spent a build
closing. **What Group D deliberately does not check:** that all eight (nine, ten…) tags have
entries. That check needs `git tag`, and the lint's founding constraint is that it reads the
**working tree on disk, never the git index** (`tools/package-lint.py:8-10`) — because
`vlt-upgrade`'s own-the-apply is a filesystem copy. Group D stays disk-only. The summary line
at `:619` is unchanged: D is still one group, so `A/B/C/E PASS, {D PASS|D SKIPPED}` still
describes the run truthfully.

**5. The arc↔release mapping — RULED: one `**Arc:**` line per entry, collected verbatim from
the release-commit subject, naming only the builds in *that release*.**
Arc ≠ release is confirmed from the tree (Arc 3 spans `v0.6.0` + `v0.7.0`). Each release
commit's subject already carries `Arc N: <arc name> (builds …)` and is the authoritative
statement of which builds shipped in that tag; the entry collects it. Where an arc spans
releases the line says so in three words (`Arc 3 — first of two releases`). `v0.4.0` predates
the arc-in-subject habit: its line reads `Arc 1 — closing release.` — a fact, not a caveat,
and explicitly not an occasion to reintroduce the prose ruling 1 removed.

**6. `changed_paths` — RULED: it ships in every entry, retro ones included, at installable-surface
granularity.**
Derivation is `git diff --name-only <prev-tag>..<tag>`, filtered and collapsed to:
`skills/vlt-*` at **directory** granularity, `.claude-plugin/marketplace.json`, and `tools/*.py`
at **file** granularity. Repo housekeeping (`README.md`, `LICENSE`, `CLAUDE.md`, `.gitignore`)
is excluded — it is public but is not module content, and the deferred consumer this field
exists for (`vlt-upgrade`'s Step-1 divergence snapshot, which keys on installed skill dirs and
per-file skill-asset SHAs — `skills/vlt-upgrade/SKILL.md:30-42`) can do nothing with it.
Directory granularity for skills is chosen to match that snapshot's grain. Shipping it in the
retro entries costs one command per entry and the diffs are real at every tag regardless of
commit granularity (capture confirmed); withholding it would make the field's first consumer
start with a five-entry hole.

## F1 — `CHANGELOG.md` (NEW, repo root, public)

**Current state:** does not exist. `find . -iname 'CHANGELOG*'` → nothing.

**The exact change.** Create `CHANGELOG.md` at the repo root with a short preamble (per
disposition 2) and **six** entries, newest first: `v0.9.0`, `v0.8.0`, `v0.7.0`, `v0.6.0`,
`v0.5.0`, `v0.4.0`. Per-entry shape:

```markdown
## v0.9.0 — 2026-07-30

**Arc 5** — the kept-promises arc.

- **B5-1 — the cost instrument:** nothing measures what a partner session loads; every
  boot-diet disposition downstream is chosen against these numbers.
- …one bullet per build in this release…

**Changed paths:** `.claude-plugin/marketplace.json`, `skills/vlt-agent-creative`, …
```

**Build-line derivation rule (mechanical, no authoring).** Read the build's archived brief
frontmatter `title:` and transform: drop the `Build #` prefix, keep `<id> — <theme>` as the
bold lead, and render the trailing parenthetical as the clause after the colon. Where a title
has no parenthetical (builds 12, 13), the theme stands alone. **Do not rewrite, shorten, or
re-editorialize a title** — the collection property is the point, and a rewrite is
unverifiable against its source.

**Tag → date → builds → source briefs** (all re-derived at brief time; the builder collects,
does not decide):

| Entry | Date | Arc line | Builds (source brief in `skills/reports/archive/`) |
|---|---|---|---|
| `v0.9.0` | 2026-07-30 | Arc 5 — the kept-promises arc | B5-1 … B5-9 (`build-B5-1-cost-instrument.md` … `build-B5-9-enforcement-kit.md`) |
| `v0.8.0` | 2026-07-26 | Arc 4 — the honest-surface arc | A4-1 … A4-5 (`build-A4-1-linkage-polarity.md` … `build-A4-5-consult-channel.md`) |
| `v0.7.0` | 2026-07-18 | Arc 3 — the enforcement arc, second of two releases | 19, 20, 21, 22, 23 |
| `v0.6.0` | 2026-07-08 | Arc 3 — the enforcement arc, first of two releases | 14, 15, 16, 18 |
| `v0.5.0` | 2026-07-03 | Arc 2 — capability field-hardening + BMad installer interop | 12, 13 |
| `v0.4.0` | 2026-06-25 | Arc 1 — closing release | 11 |

Build 17 is deliberately absent from `v0.7.0`: it was never built (folded into Arc 5). Every
other Arc-1 build (1–10) sits below the floor.

**`Changed paths:` values, re-derived at brief time** (the builder re-runs the derivation and
must reproduce these exactly; a mismatch means the filter was applied wrong, not that the
table is stale):

- `v0.4.0` — `.claude-plugin/marketplace.json`, `skills/vlt-mint`, `skills/vlt-setup`, `skills/vlt-track`
- `v0.5.0` — `.claude-plugin/marketplace.json`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-setup`, `skills/vlt-upgrade`
- `v0.6.0` — `.claude-plugin/marketplace.json`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`, `tools/package-lint.py`, `tools/test-package-lint.py`
- `v0.7.0` — `.claude-plugin/marketplace.json`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`, `tools/package-lint.py`
- `v0.8.0` — `.claude-plugin/marketplace.json`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-setup`, `skills/vlt-track`, `skills/vlt-upgrade`
- `v0.9.0` — `.claude-plugin/marketplace.json`, `skills/vlt-agent-creative`, `skills/vlt-agent-librarian`, `skills/vlt-agent-researcher`, `skills/vlt-dispatch`, `skills/vlt-extract`, `skills/vlt-ingest`, `skills/vlt-lint`, `skills/vlt-mint`, `skills/vlt-research`, `skills/vlt-review-council`, `skills/vlt-setup`, `skills/vlt-upgrade`, `tools/cost-manifest.py`, `tools/package-lint.py`, `tools/test-cost-manifest.py`

**Why.** A6-1's core gap. **This file is public** — every one of the 26 collected build lines
passes the scrub (CLAUDE.md publishing rules) before it lands; see Verification.

**Out of scope at this site:** no entry for the release this build itself ships in. That entry
is written by `vlt-release` Stage 3 during its own run (F4) — which is the first live exercise
of the loop, and is acceptance check 2.

## F2 — `tools/package-lint.py` (Group D learns the third artifact)

**Current state.** `check_group_d(expect, versions)` at `:402-409` asserts exactly two
equalities — `module.yaml module_version == expect` (`:405-406`) and `marketplace.json version
== expect` (`:407-408`). It takes no `root`. Its call site is `:597`
(`check_group_d(args.expect_version, versions)`), inside the `if args.expect_version:` branch
at `:596`. The group's documented contract is the module docstring `:36-37`. The summary line
is `:619`.

**The exact change.**

- **Signature** → `check_group_d(expect, versions, root)`; call site `:597` passes `root`
  (already in scope at `:589`).
- **New D3**, appended after the two existing equality checks: read
  `root / "CHANGELOG.md"`; a missing file appends
  `f"CHANGELOG.md missing — no entry for --expect-version {expect}"`. Otherwise count lines
  matching `^## v{re.escape(expect)} — \d{4}-\d{2}-\d{2}$` (`re.M`; `re` is already imported
  at `:59`). Zero matches → `f"CHANGELOG.md has no '## v{expect} — YYYY-MM-DD' entry"`.
  More than one → `f"CHANGELOG.md has {n} entries for v{expect} — expected exactly one"`.
  Note the heading uses an **em dash**; match the literal character the file writes.
- **Docstring `:36-37`** gains the third artifact in the existing telegraphic style — Group D
  now reads: with `--expect-version X.Y.Z`, both version strings equal it **and `CHANGELOG.md`
  carries exactly one dated `## vX.Y.Z` entry**; without the flag, SKIPPED.
- **Unchanged:** the summary line `:619` (disposition 4), the SKIPPED behaviour at `:599`, and
  every other group.

**Why.** Ideation's cross-surface ruling: the enforcing rule must live in `tools/` because
`tools/` is the only thing a fresh clone can see — the gitignored choreography can only point
at it. Group D was already a pure equality check over version-bearing artifacts; this is the
same move a third time.

**Out of scope at this site:** no check that every existing tag has an entry (disposition 4 —
that needs git, and the lint is disk-only by construction). No content grading of an entry.

## F3 — `tools/test-package-lint.py` (grounding addition — the negative case)

**Current state.** 194 lines, 8 registered cases. `build_fixture` (`:37-80`) seeds a synthetic
tree at `module_version: 9.9.9` / marketplace `version: "9.9.9"` and writes **no**
`CHANGELOG.md`. Case 1 (`:107-113`) asserts a clean tree exits 0 with `SKIPPED group D`; case 7
(`:158-163`) asserts `--expect-version 1.2.3` fails D. **There is no positive D case at all** —
nothing today proves D can pass.

**The exact change.**

- `build_fixture` writes `CHANGELOG.md` at the fixture root containing a valid entry for the
  fixture's version: `## v9.9.9 — 2026-01-01` plus one body line.
- **New case 9 — `--expect-version 9.9.9` on the clean fixture → exit 0, `PASS group D`.** The
  first positive D case; without it the new assertion could be unsatisfiable and no test would
  notice.
- **New case 10 — the entry's heading edited to a different version → FAIL group D**, with the
  failure text naming `CHANGELOG.md`.
- **New case 11 — the entry block duplicated → FAIL group D** (exercises exactly-one).
- Case 7 is left as-is: it now fails D for two reasons, and its assertion is on the group, not
  the message.

**Why.** The build changes the rule that gates every future tag. Grounding addition 1.

## F4 — `.claude/skills/vlt-release/references/choreography.md` (Stages 3–6)

**Current state and exact changes**, in file order:

- **Stage 3 `:47-58` — "Dual version bump".** Gate is currently "both version strings equal
  `X.Y.Z`". Retitle to **"Version bump + changelog entry"** and add a third artifact bullet
  beside the two at `:53-54`: prepend a `## vX.Y.Z — YYYY-MM-DD` entry to `CHANGELOG.md`,
  authored per the shape `CHANGELOG.md` itself carries — the arc line collected from the
  release-commit subject about to be written, one bullet per build collected from each
  `skills/reports/build-*.md` `title:` in this release, and `Changed paths:` from
  `git diff --name-only <prev-tag>..HEAD` under F1's filter. **State why HEAD is the right
  basis:** the release commit that follows touches only the version strings and the changelog
  itself, so the pre-commit diff equals the tag's shipped-surface diff. Keep the existing
  already-bumped tolerance and the disagreement stop, extending both to the third artifact
  (an entry already present for `X.Y.Z` is fine; do not write a second — Group D would fail it).
- **Stage 4 `:72` — the staleness (ideation ruling 5).** `package-lint: A/B/C PASS, D PASS —
  vlt X.Y.Z` → `package-lint: A/B/C/E PASS, D PASS — vlt X.Y.Z`, matching
  `tools/package-lint.py:619`. The verbatim-capture instruction at `:68-69` stays as-is — it is
  what has kept the wrong exemplar from propagating.
- **Stage 5 `:79-100` — the body paragraph is dropped (cross-surface ruling).** At `:83-84`,
  delete "a body paragraph naming what ships" from the message shape; the message is now title
  + the captured PASS line. In the exemplar block `:95-100`, drop the
  `-m "<what ships this release>"` line and add `CHANGELOG.md` to the `git add` at `:96`. Fix
  the stale exemplar text at `:86` and `:99` to `A/B/C/E PASS, D PASS`. Add one sentence naming
  the reason: what ships is single-homed in the changelog entry, and the commit points at it.
- **Stage 6 `:102-115` — the annotation is restored, not added.** `git tag vX.Y.Z` at `:110`
  → `git tag -a vX.Y.Z -m "<the release commit's subject line, verbatim>"`. Add one sentence
  recording *why*: annotation was practised through `v0.6.0` and lapsed for four tags precisely
  because it lived in habit rather than in this file. Keep the ff-only gate untouched.
- **Stage 7 `:117-138` — no change to the gate**, but the push list gains a line for the
  one-time backfill if it has not yet gone out (F7): explicit tag refspecs only, never `--all`.

**Why.** Ideation ruling 5 (the staleness rides), the cross-surface ruling (single home for
what-ships), ruling 2 (annotation is a lapsed practice being restored). Note that
`choreography.md` and everything else under `.claude/` is **gitignored** — none of this is
public surface, which is exactly why the enforcing half had to go into F2.

## F5 — `.claude/skills/vlt-release/SKILL.md` (grounding addition — the stage table)

**Current state.** The stage table restates each gate in one line: `:56` `| 3 | Dual version
bump | Both version strings set to X.Y.Z; disagreement stops |`, `:59` `| 6 | Ship | True
ff-merge to \`main\`, tag \`vX.Y.Z\` |`. The Overview at `:12-13` calls release a "seven-move
ritual … (branch → dual version bump → pre-tag lint → PASS line in the commit → ff-merge → tag
→ push)".

**The exact change.** Row 3 → `| 3 | Version bump + changelog | Both version strings set to
X.Y.Z and CHANGELOG.md carries the vX.Y.Z entry |`. Row 6 → `…ff-merge to \`main\`, **annotated**
tag \`vX.Y.Z\``. In the Overview parenthetical, `dual version bump` → `version bump + changelog
entry` and `tag` → `annotated tag`. These are pointers-not-mechanics (single-home discipline) —
the table summarizes gates, the choreography states procedure; do not restate the entry shape
here.

**Why.** Grounding addition 3: a router that describes a two-artifact Stage 3 after the
choreography moved to three is a lying map.

## F6 — `.claude/skills/build-brief` (the `title:` scrub constraint)

**Current state.** `references/brief-anatomy.md:17` specifies
`title: 'Build #N — <theme> (<one clause on the why-now>)'`, and the bullets at `:30-40`
explain `status`, `derives_from`, `rulings` — **nothing constrains `title:`**. Grepping the
whole `build-brief` skill for `scrub` returns zero hits. `SKILL.md:112` is the `## Exit gate:
ledger append` heading; its verification bullet ends the gate.

**The exact change.**

- **`references/brief-anatomy.md`** — add a `title:` bullet to the `:30-40` group, before the
  `status` bullet: the title is now **public prose** — it is collected verbatim into the
  module's `CHANGELOG.md` entry for the release this build ships in, so it carries no personal
  names, no vault names, and no vault-local artifact paths (CLAUDE.md publishing rules; worked
  examples use placeholder paths). One sentence plus the pointer; do not restate CLAUDE.md's
  rule, cite it.
- **`SKILL.md`, Exit gate section** — add a second gate clause after the ledger-append
  verification: before reporting complete, re-read the authored `title:` and confirm it carries
  no personal / vault-local content. A title that does not pass is rewritten, not shipped.
- **Deliberately unchanged:** the headless JSON contract. No new key — the scrub is a
  completion condition, and adding a field would break every consumer of the existing shape for
  no gain.

**Why.** A6-1's `build-brief` gap. The constraint is only *required* because this build makes
`title:` public — before F1 it would have been ceremony. Renaming the rule's home: the rule
lives in CLAUDE.md, `build-brief` carries the pointer and the enforcement moment.

## F7 — the four lightweight tags (a one-time backfill, not a file edit)

**Current state.** `git cat-file -t` per tag: `v0.3.0`, `v0.3.1`, `v0.4.0`, `v0.6.0` are
annotated tag objects carrying one-line messages; `v0.5.0`, `v0.7.0`, `v0.8.0`, `v0.9.0` are
lightweight refs.

**The exact change.** After `CHANGELOG.md` is committed on `main`, for each of the four:

```
git tag -a -f v0.5.0 <its sha> -m "<git log -1 --format=%s v0.5.0, verbatim>"
```

The four messages (collected, not written — each is that tag's release-commit subject, and
each already matches the shape of the four surviving annotations):

| Tag | Message |
|---|---|
| `v0.5.0` | `vlt 0.5.0 — Arc 2: capability field-hardening + BMad installer interop` |
| `v0.7.0` | `vlt 0.7.0 — Arc 3: the enforcement arc (builds 19+20+21+22+23)` |
| `v0.8.0` | `vlt 0.8.0 — Arc 4: the honest-surface arc (builds A4-1+…+A4-5)` |
| `v0.9.0` | `vlt 0.9.0 — Arc 5: the kept-promises arc (builds B5-1+…+B5-9)` |

(For `v0.8.0`/`v0.9.0` use the subject **verbatim and in full**, not the abbreviation shown
here.)

**The build stops after the local re-annotation.** It must **not** push. It records the four
`git push --force origin refs/tags/vX.Y.Z` commands in its report for the owner to run at the
release's Stage 7. Per disposition 3 and the standing rule that this repo has exactly one
owner-confirmed outward-facing moment.

**Out of scope at this site:** the four already-annotated tags are not touched. Their existing
one-line messages are the shape the four new ones match.

## Registration

**None.** No new skill, no new workflow, no `module-help.csv` row — nothing this build touches
is a shipped `vlt-*` skill. No governance convention's `version:` moves, so **no consumer walk
and no re-ack**. `CHANGELOG.md` is repo-root public documentation, not part of the own-the-apply
copy surface (the same posture `tools/` has).

## Out of scope (dispositioned)

- **`v0.3.0` / `v0.3.1` entries, and any reconstruction of the `v0.3.0` build list** —
  rejected by ideation ruling 1, which explicitly supersedes the earlier in-session
  "reconstruct from brief archive" ruling. No caveat block. The one preamble sentence
  (disposition 2) is the whole of what the file says about the floor.
- **`requires:` / breaking-change taxonomy** — deferred by ideation ruling 3; the key does not
  ship even empty. It arrives in the build that writes the taxonomy.
- **Any mention of acceptance in an entry** — ruled out (ruling 4): a tag is immutable, an
  acceptance verdict is revisable, and A4-4(5) is two-arc standing proof they contradict.
- **`release-index.md`** — ruled a gitignored factory process record under ships-decides;
  consumes no build number and must not appear in this build's output.
- **`vlt-upgrade` consumption of `changed_paths`** — deferred; taking it here would make this
  build's acceptance field-contingent and forfeit the property the whole arc shape rests on.
  `skills/vlt-upgrade/SKILL.md` is not edited.
- **`README.md`** — no changelog pointer added. `CHANGELOG.md` at the repo root is surfaced by
  GitHub without help, and the README is a product narrative, not a release record.
- **Collapsing `arc-closeout` / `acceptance-discharge` onto a single reader** — the
  `release-index.md` follow-on; not this build.
- **`inbox` filings gaining `first-bad-version:`** — deferred in capture; becomes fillable
  because of this build, but is a separate change to a separate surface.

## Verification (unit, at rest)

1. **The gate passes and can fail.** `uv run tools/package-lint.py --expect-version 0.9.0` from
   the repo root → exit 0, `PASS group D`, summary `package-lint: A/B/C/E PASS, D PASS — vlt
   0.9.0`. This is a **live positive**: the tree is at `0.9.0` and F1 writes a real `v0.9.0`
   entry. Then, in a temp copy, delete the `v0.9.0` heading → exit non-zero, `FAIL group D`
   naming `CHANGELOG.md`; and duplicate it → exit non-zero on exactly-one.
2. **`uv run tools/package-lint.py`** (no flag) → exit 0, `SKIPPED group D` — the changelog
   check must not leak into a flagless run.
3. **`uv run tools/test-package-lint.py`** → 11/11 cases green (8 existing + 3 new).
4. **Collection fidelity.** For each of the 26 build lines, grep its source brief's `title:` in
   `skills/reports/archive/` and confirm the line is that title transformed by F1's rule and
   nothing else. Any line that cannot be traced to a title is authored, not collected, and is a
   defect.
5. **`changed_paths` reproduction.** Re-run the F1 derivation per entry and diff against the
   six lists in F1. Exact match required.
6. **Dates and arc lines.** Each heading date equals `git log -1 --format=%ad --date=short
   <tag>`; each arc line's builds match that tag's release-commit subject.
7. **Tag objects.** `git cat-file -t` returns `tag` for all eight tags locally; the four new
   messages equal their release-commit subjects verbatim. Nothing pushed.
8. **Single-home.** Grep the choreography for any surviving instruction to write what-ships
   into the commit body, and for any surviving `A/B/C PASS` exemplar — both must return zero.
   Grep `SKILL.md` and the choreography for restated entry-shape mechanics — the shape lives in
   `CHANGELOG.md` and Stage 3 only.
9. **Handshake.** No convention `version:` moved and no `consumers:` list changed, so no walk is
   owed; **Group E is the check of record** and is covered by check 1's A/B/C/E run. Do not
   write a hand-rolled `grep "<name>@" skills/`.
10. **Scrub.** No personal or vault-local content anywhere in `CHANGELOG.md` — all 26 build
    lines, all six arc lines, all six changed-paths lists — nor in this build's own brief
    `title:`, which is the first title authored under F6's new constraint and must satisfy it.
11. **Cruft.** No `.decision-log.md` anywhere in the working tree at build end.

## Release

B6-1 is the **only** build in Arc 6, so it is the release build. The release itself runs
through `vlt-release`, which asks the owner for the version — do not fix it here. For the
owner's decision: `0.10.0` is the natural read (a new public artifact plus a new release-gate
rule), and `0.9.1` is defensible (no shipped `vlt-*` skill changes, so nothing a vault installs
moves). The choice is the owner's at Stage 1.

At release, the standing obligations apply: both version strings bumped
(`.claude-plugin/marketplace.json` `plugins[0].version` and
`skills/vlt-setup/assets/module.yaml` `module_version`), the pre-tag
`uv run tools/package-lint.py --expect-version X.Y.Z` gate passed with exit 0 and its PASS line
verbatim in the release commit, then ff-merge → annotated tag → owner-confirmed push.

**One thing is new and load-bearing:** Stage 3 now also writes the `## vX.Y.Z` entry for *this*
release, and Group D will refuse the tag without it. That is the loop closing on itself, and it
is acceptance check 2. The four backfill force-pushes (F7) batch into the same Stage 7.

## Acceptance (live — appended to the roadmap ledger)

Both checks are **`[ship-verifiable]`**. Arc 6 has no field-contingent tail: no shipped `vlt-*`
skill moves, so nothing here waits on a live vault event, and closeout gates on the full set.

1. **[ship-verifiable] The record exists and the gate enforces it.** `CHANGELOG.md` is on
   `main` with six correctly-dated entries (`v0.4.0`…`v0.9.0`), every build line traceable to an
   archived brief `title:`, every `changed_paths` list reproducing from `git diff`; and Group D
   really gates — `--expect-version` for a version with no entry exits non-zero naming
   `CHANGELOG.md`, `--expect-version 0.9.0` exits 0, `test-package-lint.py` is 11/11. Bounded:
   dischargeable at rest the day the build lands, and again at the release gate.
2. **[ship-verifiable] The loop closes on its own release.** Arc 6's release run authors the new
   version's entry at Stage 3 before the lint gate (Group D would otherwise refuse the tag); its
   captured PASS line reads `A/B/C/E PASS, D PASS`; the release commit carries **no** what-ships
   body paragraph; the new tag is an annotated object (`git cat-file -t` → `tag`); and after the
   owner-confirmed Stage-7 push all eight prior tags plus the new one are annotated on the
   remote (`git ls-remote --tags` shows the dereferenced `^{}` form for each). Bounded: the
   release is going to happen anyway, and it is the event that grades this. Also settles F6 in
   passing — the next brief authored after this build is checked for the `title:` scrub at its
   Exit gate; at rest, this brief's own `title:` is the first instance and passes.
