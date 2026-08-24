# Review — the going-public block (P-7..P-10), fresh eyes

**Date:** 2026-08-24
**Scope:** verify that platform items P-7 (track the factory), P-8 (the `cycle` + `factory/`
build), P-9 (the publication act) and P-10 (the loop, visible) left the repo ready for
Cycle 11's `inbox-capture`.
**Method:** read the claims in `factory/platform/roadmap.md`, then verify every one against
disk and the two remotes. Nothing was taken from memory or from the ledger's own prose.
**Posture:** read-only. Nothing was fixed, and `inbox-capture` was **not** run.

**Verdict: READY WITH NITS.** Four findings, all documentation-level; none blocks the
Cycle 11 capture.

---

## 1. Structure

### 1a. The `factory/` tree stands as ruled

```
find factory -maxdepth 2 -type d
ls factory/cycles ; cat factory/CYCLE
```

`factory/cycles/` holds exactly the eleven ruled directories — `00-origins`,
`01-field-signal`, `02-capability-hardening`, `03-enforcement`, `04-honest-surface`,
`05-kept-promises`, `06-factory-honest-surface`, `07-nowhere-to-put-it`, `08-lifecycle`,
`09-boundary`, `10-signal-integrity` — alongside `inbox/` (54 files: 53 filings +
`README.md`), `platform/` (`roadmap.md` + the 2026-07-17 lifecycle-skills audit),
`method/` (`README.md`, `cycles-were-arcs.md`, `vault-resident-architecture-spec.md`)
and the `CYCLE` pointer.

`factory/CYCLE`'s value line reads `none — Cycle 11 opens at factory/cycles/11-<slug>/ on
its inbox-capture run`. **Verified as claimed.**

### 1b. The old homes are gone

```
for p in skills/reports inbox docs; do [ -e "$p" ] && echo PRESENT || echo absent; done
```

All three absent. **Verified.**

### 1c. No file lost — compared against the private mirror

```
git fetch origin && git fetch private
git ls-tree -r --name-only <ref> | wc -l
git diff --find-renames=40% --diff-filter=D --name-only bd605aa HEAD
git diff --name-only b785abd e8c92ae
```

| Ref | Tracked files |
|---|---|
| `283fe5d` (v0.14.0, pre-publication) | 78 |
| `bd605aa` (P-7 on `private/p7-p9-history`) | 319 |
| `b785abd` (public squash) | 323 |
| `e8c92ae` (private `p7-p9-history` tip) | 323 |
| `HEAD` / `origin/main` / `private/main` | 325 |

- **`b785abd` vs `e8c92ae`: 0 differing files.** The public squash is byte-identical in
  content to the private per-item history's tip — the squash lost nothing.
- **Pure deletions `bd605aa..HEAD` (rename-aware): none.** Every file P-7 tracked is still
  tracked.
- The eleven basenames that vanish under a naive basename diff are all confirmed renames
  at R076–R100 similarity — the ten `skills/reports/archive/inbox-evolution-arc*-roadmap.md`
  → `factory/cycles/NN-<slug>/roadmap.md`, plus `skills/reports/platform-roadmap.md` →
  `factory/platform/roadmap.md`.
- All 78 pre-publication tracked files survive at `HEAD` (`comm` of the two path lists is
  empty).
- 319 → 325 is fully accounted for by six born files: `factory/CYCLE`,
  `factory/method/README.md`, `factory/method/cycles-were-arcs.md`,
  `tools/factory-paths-check.py` (P-8/P-9), `.github/PULL_REQUEST_TEMPLATE.md` and
  `.claude/skills/issue-triage/references/tracker-sync.md` (P-10).

**Finding: none. Structure is complete and no file was lost.**

---

## 2. Consistency

### 2a. Both gates pass

```
uv run tools/factory-paths-check.py   → exit 0
uv run tools/package-lint.py --expect-version 0.14.0   → exit 0
```

```
factory-paths-check PASS — 110 concrete path references resolve (20 files scanned)
package-lint: A/B/C/E PASS, D PASS — vlt 0.14.0
```

Both match the ledger's claimed numbers (P-10 recorded 110 refs / 20 files).
Version strings agree: `.claude-plugin/marketplace.json:16` = `0.14.0`,
`skills/vlt-setup/assets/module.yaml:4` = `0.14.0`.

### 2b. Zero diff on the shipped surface vs tag `v0.14.0`

```
git diff --name-only v0.14.0 HEAD -- 'skills/vlt-*' .claude-plugin/   → 0 files
git status --porcelain -- 'skills/*' .claude-plugin/                  → clean
```

The tag object `55b739d` dereferences to `283fe5d`. **The boundary held: the whole
going-public block touched no shipped surface.** Verified as claimed.

### 2c. Stale "arc" / old-path references in the 9 factory skills

Every `\barcs?\b` and `arc[0-9<N-]` hit across the nine skills plus `vlt-lifecycle.md`
and `CLAUDE.md` was read in context. **All are deliberate:**

- Historical precedent citations (Arc 2/3/7/8/9 exemplars in `acceptance-discharge`,
  `build-brief`, `cycle-closeout`, `roadmap-roundtable`) — falsifying these would falsify
  when decisions were made, per `factory/method/cycles-were-arcs.md`.
- Identifiers (`A4-4`, `B10-…`, "four-arc debt") — the letters mean amendment and build.
- Two rename-aware clauses that name the old form *as* old:
  `vlt-release/references/choreography.md:8` (`cycleN-vX.Y.Z` … "branches before the
  rename were `arcN-vX.Y.Z`") and `:104` ("entries before the rename carry `Arc N`").
- `roadmap-roundtable/SKILL.md:123` cites the Arc 7 keepsake as a *mold*; the live output
  template on the next line is `<date>-cycle<N>-roadmap-roundtable.html`. Correct.
- `roadmap-roundtable/.memlog.md` — a dated build log; historical by nature (and excluded
  from `factory-paths-check` by design).

Stale-path grep (`skills/reports`, root `inbox/`, `docs/`, `arc-closeout`) over the nine
skills returns only `build-brief/SKILL.md:128` ("reason from docs/memory") — an English
phrase, not a path — and the memlog above.

**Finding: none inside the nine skills.** But see **F3** for what the gate does not scan.

---

## 3. Public surface

### 3a. Remotes

```
git rev-parse HEAD origin/main private/main
```

All three = `2970850036e5343ab6db31914a5bd8457a47fae3`. Working tree clean; no untracked
non-ignored files. `private/p7-p9-history` exists and carries the four per-item commits
(`bd605aa`, `a9d8403`, `8ef152b`, `e8c92ae`) whose hashes the P-7/P-8 records cite — the
provenance note in P-9 is accurate.

### 3b. Personal tokens — tracked files

```
git ls-files -z | xargs -0 grep -lI 'mikeypioli'   → 0 files
git ls-files -z | xargs -0 grep -nI '/Users/'      → 4 files, all meta-references
git ls-files -z | xargs -0 grep -nI 'gowermikey'   → .claude-plugin/marketplace.json only
```

- **Username: zero hits.**
- **`/Users/` : four hits, all tolerated by P-9's own stated exception** — three are
  scrub-verification lines inside historical briefs (`build-B5-1:217`, `build-B5-2:262`,
  `build-B7-6:444`) that *name* the token as something to grep for, and the fourth is
  P-9's own verification sentence at `factory/platform/roadmap.md:487`.
- **Author email: two hits, both in `marketplace.json`** — the one deliberate exception
  CLAUDE.md names.
- **The field vault's real *name* is not scrubbed** — see **F2**.

### 3c. Personal tokens — public history

```
git rev-list --count origin/main                        → 75 commits
git rev-list --objects origin/main | … cat-file blob    → 778 unique blobs scanned
```

Zero `mikeypioli` hits across all 778 blobs reachable from `origin/main`. Zero
`mikeypioli` or `/Users/` hits across all 75 commit messages. **The squash did its job:
no pre-scrub file state is reachable from public history.**

### 3d. The story: README / CLAUDE.md / pinned issue #9

- `README.md:220-234` "How this project evolves" describes the field-driven loop, points
  at `factory/CYCLE`, `factory/cycles/`, `factory/method/` and `.claude/skills/`. All
  resolve.
- `README.md:236-242` "Notable files" describes `factory/`'s four sub-trees accurately.
- `CLAUDE.md` Git-&-publishing section states the factory-public posture and the
  gitignore reality; `.gitignore` matches it exactly (`.claude/skills/bmad-*`,
  `.claude/settings.local.json`, `_bmad/`, `_output/`, `.vscode/`, `CLAUDE.local.md`,
  `**/.decision-log.md`).
- Pinned issue **#9 "How this project evolves"** is OPEN, links to the README section,
  the field contract, `factory/cycles/` and `factory/CYCLE`, and explains the milestone
  projection and the `B<NN>-<i>` title convention. Every link target exists.
- The three tell one consistent story. **One inconsistency inside the README itself:
  see F1.**

### 3e. Hygiene

No `.decision-log.md` anywhere on disk. No `.analysis/` directories. `tools/__pycache__/`
exists but is gitignored and package-lint group A (on-disk cruft) passes.

---

## 4. Readiness

### 4a. A Cycle 11 `inbox-capture` run — walked read-only, not executed

Every instruction in `.claude/skills/inbox-capture/SKILL.md` was checked against the real
tree:

| Instruction | Resolves? |
|---|---|
| GitHub intake: read `feedback_repo.default` from `skills/vlt-setup/assets/module.yaml` | ✔ `:69` |
| Point (never restate) `skills/vlt-feedback/references/field-contract.md` | ✔ exists |
| Intake mechanics at `references/github-intake.md` | ✔ exists |
| List `factory/inbox/*.md` | ✔ 53 filings present |
| Read `factory/CYCLE` | ✔ reads `none` |
| `none` → start a fresh cycle, number = one past the highest existing cycle directory | ✔ highest = `10-signal-integrity` → **11** |
| Create `factory/cycles/NN-<slug>/roadmap.md` and write `NN-<slug>` into `factory/CYCLE` | ✔ parent exists, writable |
| Frontmatter shape `title: 'Cycle NN — <theme>'` (`references/roadmap-synthesis.md:17`) | ✔ matches P-8's D3 ruling and feeds tracker-sync's milestone derivation |
| Mid-cycle addendum posture (P-4) | ✔ present, N/A on a fresh cycle |
| Grounding + Synthesis stage files | ✔ both exist |

**The run is followable end to end against the real tree.** One shape watch (**F4**) and
one cosmetic observation (O1) below.

### 4b. A tracker-sync dry read

`.claude/skills/issue-triage/references/tracker-sync.md` is coherent and every referenced
surface resolves. Live tracker state checked with `gh`:

- **All nine sync labels exist** with the descriptions the reference documents:
  `stage:captured`, `stage:ideated`, `stage:reviewed`, `stage:briefed`, `stage:built`,
  `stage:released`, `stage:accepted`, `check:ship-verifiable`, `check:field-contingent`.
- The 14 field-contract labels are present and untouched — the two populations are
  disjoint on the live tracker as the reference claims.
- **No milestones exist yet** — correct: `factory/CYCLE` reads `none`, and step 1 says a
  `none` pointer syncs nothing forward-looking.
- Open issues: #1, #4, #6, #7, #8 (all `vault-filed`+`vault-accepted`+`captured`) and #9
  (unlabeled). Closed: #2, #3, #5. Matches the ledger.
- **Issue #9 does not pollute the triage queue.** `issue-triage/SKILL.md:44-51` derives
  untriaged as open-`vault-filed`-minus-accepted/captured, and routes unlabeled open
  issues to a report-only "off-rail traffic — owner discretion" list. #9 lands there, is
  never triaged, and never matches the `B<NN>-<i> — ` sync prefix. Clean.

---

## Findings

### F1 — nit — README's skill roster is stale and omits `vlt-feedback`

`README.md` says **"16 skills"** in four places (`:10`, `:155`, `:238`, `:239`), and the
grouped roster table at `:157-165` enumerates exactly 16. Disk carries **17**
(`ls -d skills/vlt-*`), and `.claude-plugin/marketplace.json` registers all 17. The
missing one is **`vlt-feedback`**, shipped in `2f1d757` (build B9-3, v0.12.0) — the skill
that *implements* the feedback rail the README's own "How this project evolves" section
tells readers to use, and that pinned issue #9 links into.

Two of the four stale lines (`:238`, `:239`) were **written by P-9 itself** in `b785abd`,
whose ledger record claims "a truthful Notable-files list". This is precisely the
completeness-drift class CLAUDE.md names as a standing rule, and precisely what queued
P-6's check (a) exists to catch — the rule is written, and its own README broke it.

*Not fixed — owner's call. The mechanical fix is a count bump plus a `vlt-feedback` row
(group: the rail / self-evolution).*

### F2 — nit — the field vault's real name is published; P-9's verification line says otherwise

P-9's verification reads: *"grepping every tracked file for the owner's username,
`/Users/` paths, or the field vault's real name returns nothing."* The first two are
true (§3b/§3c). The third is not:

```
git ls-files -z | xargs -0 grep -lI 'vlt-core' | wc -l   → 180 files
git ls-files -z | xargs -0 grep -ohI 'vlt-core' | wc -l  → 1183 hits
```

Concentrated in `factory/inbox/` (41 files) and the cycle briefs/filings, plus **one on
the shipped surface**: `skills/vlt-upgrade/SKILL.md:89` (pre-dates publication and rode
in with v0.14.0).

**No path leaks** — `/Users/mikeypioli/Vaults/vlt-core` never appears; only the bare
vault name does. CLAUDE.md's rule targets the field vault's real *path*, and the owner
already ruled the exactly-analogous `vlt-sayari` case at publish ("it names no path,
publish as-is"). So the *posture* is probably consistent and intended — but the ledger's
verification sentence overstates what was checked, and a 1183-hit scrub is not something
to discover later.

*Two clean resolutions, owner's call: (a) rule `vlt-core` publishable on the sayari
precedent and correct P-9's verification line to say "real path", or (b) scrub.
Nothing fixed here.*

### F3 — nit — `factory-paths-check` does not scan `factory/`, and three queued platform items point at dead paths

`tools/factory-paths-check.py:20-32` scans the nine factory skills + `vlt-lifecycle.md` +
`CLAUDE.md`. It does **not** scan anything under `factory/`. Closed records legitimately
keep pre-move paths (history), but three **queued, forward-facing** brief-lites carry
paths that will be executed and are wrong:

- **P-2** (`:52`, `:55`) — spike register site `skills/reports/spikes/S-N-<slug>.md`
  (dead root; no `spikes/` directory exists anywhere) and `arc-closeout` gains an
  orphan-spike check (skill renamed to `cycle-closeout` by D1).
- **P-3** (`:135`, `:137`, `:140`) — `inbox/` filings (now `factory/inbox/`) and
  `arc-closeout` twice.
- **P-5** (`:151`, `:165`) — cites its own source as
  `skills/reports/eval-roi-count-2026-08-23.md`, which now lives at
  `factory/cycles/10-signal-integrity/eval-roi-count-2026-08-23.md`; and scopes the
  citation checker at `skills/reports/*.md` (briefs + roadmaps), a glob that now matches
  nothing. **P-5 is the citation-resolution item — its own citation is broken**, which is
  both the sharpest instance of the problem it exists to solve and an argument for
  widening the checker's scope to `factory/**` when it is built.
- Also, the channel contract's own visibility-floor clause (`:31`) still says "each
  arc-closeout notes …" — a live contract line naming a renamed skill.
- Lower severity: `factory/method/vault-resident-architecture-spec.md:109` names
  `skills/reports/vault-module-plan.md` (a design-era doc; arguably historical).

*Not fixed. The one-line structural option is extending `SCAN_FILES` to cover
`factory/platform/roadmap.md` — but that would go red on the historical records too, so
it needs a history-vs-live distinction rather than a blind widening.*

### F4 — nit (already self-recorded by P-8, still open) — `ideation-scaffold`'s shape exemplar dies with Cycle 11

`.claude/skills/ideation-scaffold/SKILL.md:63` instructs: *"Match the shape of the
roadmap's existing 2026-07-06 rulings section (read it first; it is the parse target
`build-brief` already understands)."* A **fresh Cycle 11 roadmap contains no such
section**, so on the first ideation run of the new cycle the instruction has no local
referent. It still resolves via a closed roadmap — P-8 flagged exactly this as its Watch
— but it is now one cycle from biting for real, and the P-8 record is the only place it
is written down.

*Not fixed. Cheapest repair: re-point at the closed roadmap by path (e.g.
`factory/cycles/09-boundary/roadmap.md`'s rulings section), which would also then be
covered by `factory-paths-check`.*

### Observations (no action proposed)

- **O1** — `factory/CYCLE`'s value line is `none — Cycle 11 opens at
  factory/cycles/11-<slug>/ on its inbox-capture run`, while its own comment header and
  `vlt-lifecycle.md:9` describe a one-line `NN-<slug>` / `none` value. Every consumer
  (`inbox-capture`, `build-brief`, `ideation-scaffold`, `roadmap-roundtable`,
  `acceptance-discharge`, `cycle-closeout`, `vlt-release`, `lifecycle-status`,
  `tracker-sync`) reads it as prose, not by exact match, so nothing breaks — the trailing
  clause is arguably a feature.
- **O2** — `inbox-capture`'s Discovery says "List `factory/inbox/*.md` — these are the
  un-captured filings", a glob that also matches `factory/inbox/README.md`. Pre-existing,
  and obvious in context to any reader.

---

## Verdict

**READY WITH NITS.** The going-public block delivered what it claimed on every load-bearing
axis:

- the `factory/` tree is complete and correctly shaped; **no file was lost** (verified
  rename-aware against the private mirror, and the public squash is content-identical to
  `p7-p9-history`'s tip);
- both gates pass (`factory-paths-check` 110/20, `package-lint` A/B/C/D/E at 0.14.0);
- the **shipped surface is byte-identical to tag `v0.14.0`** — the delivery-not-topic
  boundary held across all four items;
- `origin/main == private/main == HEAD`; **zero username or `/Users/` leaks in any tracked
  file or in any of the 778 blobs of public history**;
- the tracker is bootstrapped and coherent — nine sync labels, 14 field labels, pinned
  issue #9, no milestones yet (correct), and #9 cannot pollute the triage queue;
- **a Cycle 11 `inbox-capture` run is followable end to end against the real tree**, and
  will correctly open `factory/cycles/11-<slug>/`.

Findings, all documentation-level, none blocking:

1. **F1** — README claims 16 skills in four places; there are 17. `vlt-feedback` is
   missing from the roster table. Two of the stale lines were written by P-9 itself.
2. **F2** — the field vault's name `vlt-core` appears in 180 tracked files (one on shipped
   surface); no path leaks. P-9's verification line claims the name returns nothing.
   Needs an owner ruling (publish-as-is on the sayari precedent, or scrub) either way.
3. **F3** — `factory-paths-check` does not scan `factory/`, and queued items P-2/P-3/P-5
   carry dead forward-facing paths — including P-5's own broken source citation.
4. **F4** — `ideation-scaffold`'s "2026-07-06 rulings section" exemplar has no referent in
   a fresh Cycle 11 roadmap (P-8's own recorded watch, still open).

Nothing was fixed. Cycle 11's capture may open on this tree as it stands.

## Findings disposition (2026-08-24, follow-up session)

- **F1 FIXED** — README's four skill-count lines bumped 16 → 17 (matching disk and
  marketplace.json) and `vlt-feedback` added to the roster's Lifecycle row.
- **F2 HELD — owner ruling pending.** Not touched, per the finding's own instruction:
  the vault *name* `vlt-core` (180 files, incl. one shipped-surface site) vs. the P-9
  record's overstated verification line. Options (a) correct the record line / (b) scrub
  are with the owner.
- **F3 FIXED** — live/queued ledger entries repointed: the channel contract's
  visibility-floor line (cycle-closeout), P-2's spike-register path
  (`factory/platform/spikes/`) + orphan-check owner, P-3's intake/closeout sites,
  P-5's ROI-count citation and citation-walk target. Closed records (P-7/P-8/P-9)
  deliberately untouched — their old paths are history.
  `factory/method/vault-resident-architecture-spec.md:109` judged **historical** — left
  as-is. The factory-paths-check SCAN_FILES widening is raised to the owner as a
  candidate P-item (needs a history-vs-live distinction), not done as a drive-by.
- **F4 FIXED** — ideation-scaffold's shape exemplar repointed to
  `factory/cycles/09-boundary/roadmap.md`'s `## Ideation rulings — A9-1..A9-6` section
  (now under factory-paths-check coverage, as suggested).

Verification after fixes: factory-paths-check PASS (111 refs, 20 files); package-lint
A/B/C/E PASS at 0.14.0; `git diff --name-only v0.14.0 HEAD -- 'skills/vlt-*'
.claude-plugin/` empty (no shipped-surface touch).

### F2 disposition (2026-08-24, owner-ruled)

Split ruling: **(1)** the one shipped-surface occurrence (`skills/vlt-upgrade/SKILL.md`,
Step 3 item 7's provenance note) is a **defect** — a shipped skill must be
recipient-agnostic — and is FILED to
`factory/inbox/2026-08-24-085505-vlt-upgrade-names-a-real-install-on-shipped-surface.md`
for Cycle 11 capture (shipped surface → cycle roadmap, never a platform fix).
**(2)** the ~179 factory-record files keep the name under the publish-as-is posture
(names no path — the vlt-sayari precedent). The P-9 record's overstated verification
line carries a dated correction defining "personal-token" as the three scrubbed tokens.
F2 is closed as a review finding; the shipped-surface repair is now the filing's.
