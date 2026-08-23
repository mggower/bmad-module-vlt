---
title: 'Build #B10-1 — the manifest source-hash: the skill-asset divergence net stops blessing the edits it exists to catch (source-hashed on write, sanctioned edits self-recording, the live-as-source and version-skew escape paths closed)'
status: 'BUILT 2026-08-21 — all six F-sites landed; unit-verified at rest (fixtures 1–5 green + duplicate-basename error probe, cross-file greps clean, package-lint A/B/C/E PASS with C6 green against the F6 re-stamp, rule card 6,022 bytes < 8,000 budget). RED-THEN-GREEN (Verification 1, A10-6 synthetic case): RED — pre-fix v0.12.0 script over a fixture with a hand-edited live manifested file: --write succeeded, then --verify reported "diverged": [] (clean — the edit silently absorbed as the new baseline). GREEN — post-fix: --write reports the path in "diverged", the manifest line carries the SOURCE sha (08db6ea7…, verified equal to shasum of the source file, unequal to the live edit), and --verify still reports the path in "diverged". Deliberate deviations, numbered: (1) the "N sanctioned divergences: <paths>" report line is carried as a "sanctioned_summary" string field in the JSON result (present when sanctioned is non-empty, both modes) rather than a second output channel — the JSON is the script''s one report surface; the Confirm/Step-4 prose renders it. (2) F2.2 taken on the brief''s allowed alternative: the invocation block gains a one-line note that --overlays-dir derives the sanction-record default (--sanctioned only to override), rather than a redundant explicit flag. No other deviations; ship-verifiable acceptance checks 1–4 discharged at rest this session (check 5 field-contingent, rides the vlt-core v0.13.0 upgrade). No .decision-log.md in the working tree; one commit.'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-21-144352-skill-asset-manifest-hashed-from-live-files-divergence-net-blind.md (A10-6 — the whole defect: compute_manifest hashes the live tree, both prose claims false, the no-upgrade reproduction; origin mggower/bmad-module-vlt#2, captured)'
  - 'inbox/2026-08-20-093000-para-write-path-single-door-wrong-shape.md (A9-1 K9 — the enum-in-comment template defect at capability-template.md:23; drive-by per ruling D7, confirmed at its origin by the S1 harvest)'
  - 'inbox/2026-08-21-150500-captured-issues-accept-comments-the-intake-never-reads.md (A10-8, interim half only — the one-sentence honesty note in both issue forms; drive-by per roundtable A14, superseded by B10-7)'
roadmap: 'skills/reports/inbox-evolution-arc10-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-21): build-B10-1 grouping bullet (binds: Q4, D4, D7, S3, Q3a per roundtable A6); Q4 (A10-6 builds early, B9-6/B10-4 briefed only after it lands); D4 as widened by roundtable A4 (--write reports, never refuses; sanctioned edits record themselves at sanction time, zero-ritual; the report covers only unsanctioned divergence, sanctioned excluded-and-denominated); D7 (K9 is a drive-by, rides this build); S3 (SPIKE CLOSED 2026-08-21 — the Step-3/Step-3.6 ordering trap is a special case of A10-6; the sanctioned-lift tension is this brief''s to resolve); roundtable A5 (close the live-as-source and version-skew escape paths; two new acceptance fixtures); A6 (the write-time divergence list routes into the upgrade post-flight report/Confirm; the manifest write is named an E2 census entry born under Q3a''s shape or the brief records why not); A14 (the interim honesty note rides here).'
risk: 'low-moderate — one script''s hashing semantics change inside the divergence net (the one instrument vaults rely on to see local edits), plus a one-row operating-contract edit that triggers the package-lint C6 rule-card re-stamp; no convention version: moves, no consumer walk, no new lint check (E4 untouched), no release in this build (v0.13.0 cuts after B10-5). The hazard is semantic: a manifest whose entries silently change meaning (live-hash → source-hash) mid-fleet — bounded because the manifest is module-owned and rewritten on every install/upgrade anyway, so the next provision converts every vault wholesale.'
---

# Build #B10-1 — the manifest source-hash

The skill-asset manifest is the module-owned divergence net over everything the module
ships into a vault — and its `--write` hashes the **live** tree
(`verify-skill-manifest.py:85/:90/:102`), so the one state it exists to catch, a local
edit, is the state that silently becomes its new baseline. Both prose claims that describe
it are false in the field (`vlt-setup/SKILL.md:153` "Compute it from the *installed*
shipped files (which equal stock at install time)" — true once, false thereafter;
`vlt-upgrade/SKILL.md:49` "refreshed to the new shipped versions" — it is refreshed to
live versions). Field-hit in the 2026-08-21 vlt-core upgrade: the vitals divergence had to
be re-established by hand. S3 proved the `vlt-upgrade` Step-3/Step-3.6 ordering trap is a
special case of the same defect — any edit landing between the Step-2 refresh and the
item-6 manifest write is recorded as stock, and two sanctioned in-skill writers (the
loop-profile lift, write-through) can make exactly such edits.

This build makes both prose claims true rather than rewording them: `--write` hashes
**source-tree content for source-provenanced paths, live only where no counterpart
exists**; reports divergence loudly, never refuses (D4); gives sanctioned migration edits
a zero-ritual self-recording home so the report covers only unsanctioned divergence (A4,
resolving S3's tension); and closes the two escape paths (A5): the live-as-source fallback
reports loudly that the net is live-hashed, and a version-skewed source refuses with a
named error. It unblocks B10-4 (B9-6 is briefed only after this lands, per Q4/S3). Two
drive-bys ride along: the K9 enum-in-comment fix at `capability-template.md:23` (D7) and
the A14 interim honesty note in both `.github/` issue forms.

All rejected alternatives in the parent filings and the rulings are settled — do not
re-litigate. In particular: a refusing `--write` (D4 ruled report-never-refuse, because
sanctioned migration edits are legal states), rewording the prose claims instead of fixing
the script (capture ruled the script the right single site), a per-item sanction ritual
(A4 ruled zero-ritual — A10-1's field evidence is the bound: per-item rituals go unused),
and a comment-scan for the rail (D5's territory, not this build's).

**`binds:` roster (from the roadmap bullet, per the standing rule): Q4, D4 (as widened by
A4), D7, S3, Q3a (via A6) — plus roundtable A5, A6, A14 as in-bullet annotations.** The
bullet carries the roster explicitly; nothing was reconstructed.

## Brief-time dispositions

**✅ OWNER-REVIEWED 2026-08-23 (first-half review, dated batch): all seven dispositions
CONFIRMED.** Field evidence at review time: B10-1 discharged whole on the 0.14.0
acceptance run (manifest_write_divergence present-when-empty; source_mode: source;
67/67 clean; the sanction and version-skew paths shipped but unexercised, no contrary
signal). Review record: the arc roadmap's first-half review section.

Autonomous run 2026-08-21 — the owner is not present; each call below is **clerk-resolved
(autonomous run 2026-08-21, owner review pending)** with its reasoning, bounded to what
the rulings deliberately left to this brief.

1. **Live-as-source posture (A5's first escape path): REPORT LOUDLY, not refuse.**
   *Clerk-resolved.* A5 offered "refuse the silent path **or** report loudly that the
   manifest is live-hashed." Refusal would break the one fully legal case — the fresh
   install, where the just-installed live dir *is* verbatim the shipped set
   (`vlt-setup/SKILL.md:163`). Ruling: when the resolved `--source-skills-dir` equals the
   resolved live skills dir, the write proceeds and the JSON gains `"source_mode": "live"`
   plus a top-level `"warning"` stating the net is live-hashed for this write (blind to
   any pre-existing edit); `source_mode` is `"source"` on the normal path so the loud case
   is distinguishable, never the default silence. The SKILL.md fallback text (F2) and the
   Confirm summary (F2) surface it. The version-skew check (disposition 2) is trivially
   satisfied in this case (same file both sides).

2. **Version-skew mechanics (A5's second escape path): compare the two `module.yaml`
   `module_version:` strings; refuse with the named error `version-skew`, exit 2.**
   *Clerk-resolved.* The "installed version record" is the installed copy of the module
   metadata — `{live-skills-dir}/vlt-setup/assets/module.yaml` `module_version:` (the
   same record `vlt-upgrade` Step 4 reads for `from_version`; no other installed version
   record exists — grep confirmed `module.yaml:4` is the only `module_version:` home).
   The source side is `{source-skills-dir}/vlt-setup/assets/module.yaml`. On `--write`
   with `source_mode == "source"`: parse both (stdlib line-parse — the script stays
   stdlib-only), refuse on mismatch with the named error **`version-skew`** printed to
   stderr naming both versions (the `gh-missing` discipline: a named error plus a stated
   recovery — "apply the source to the install first, or pass the source that matches the
   installed version"), exit 2. Either record unreadable/missing → named error
   **`version-record-missing`**, exit 2 (the script's existing operational-error idiom).
   Rationale: a skewed source would source-hash a manifest against files the vault does
   not have — every entry instantly `diverged`/`missing`, a net that cries wolf; the skew
   state has no legal use, so refusal is honest, unlike the divergence case D4 governs.

3. **S3's sanctioned-lift tension, resolved within D4's posture (per A4): a sanction
   record beside the overlays, written by the sanctioning act itself.** *Clerk-resolved
   (the mechanism's design; the posture itself is ruled by D4+A4).*
   - **Elimination first, per A4's allowed alternative — checked and REJECTED as
     unreachable.** Stock cannot converge to the pointer shape: the shipped partners
     (`vlt-agent-librarian`/`-researcher`/`-creative`) carry **no** loop profile and no
     `capabilities/` tree in stock (grep over all three: zero hits for
     loop-profile/track.md), so a lifted profile's pointer line has nothing in stock to
     converge to — the pointer names a vault-specific `capabilities/track.md`. And
     write-through (`vlt-upgrade/SKILL.md:86`, "an upgrade-time ruling that changes … a
     skill's stated rule") is by nature a vault-ruled deviation from stock. A standing
     record it is.
   - **The record:** `{overlays}/.skill-manifest.sanctioned` — one `<sha256>\t<path>`
     line per sanctioned edit, the sha of the file **as sanctioned** (post-edit content).
     It lives in the overlay zone root (vault's, append-only, durable — the zone
     `vlt-setup` explicitly never writes or clobbers, `vlt-setup/SKILL.md:151`), NOT in
     `.baseline/` (module-owned overwrite territory). `vlt-setup` never creates or
     touches it.
   - **The writers, zero-ritual (A4):** the two sanctioned in-skill editors of manifested
     files append their line **in the same act that makes the edit** — `vlt-upgrade`
     Step 3 item 5's loop-profile relocation (`SKILL.md:81`: on an accepted lift, the
     pointer-line edit to an installed partner's SKILL.md appends the edited file's sha
     + path) and Step 3 item 7's write-through (`SKILL.md:86`: a ruling written into a
     shipped skill's prose appends likewise). No separate ceremony, no per-item prompt —
     the record write is one more sentence in each act's existing instruction.
   - **The readers:** the script gains `--sanctioned <path>` (default
     `{overlays-dir}/.skill-manifest.sanctioned` when `--overlays-dir` is given; absent
     file ⇒ empty set, never an error). `--verify` partitions: live sha == manifest sha →
     clean; live sha == sanctioned sha → **sanctioned** (excluded from `diverged`,
     denominated: `"sanctioned": [paths]` + the report line "N sanctioned divergences:
     <paths>"); else → `diverged`. `--write` partitions its write-time divergence the
     same way. A sanction entry whose live sha now equals the source sha (the edit was
     refreshed away or upstreamed) is reported `sanction_stale` — informational, never
     auto-pruned (the record is the vault's).
   - **Semantics guard:** the sanctioned sha pins the *sanctioned content* — a further
     unsanctioned edit on top of a sanctioned file shows `diverged` again, which is
     correct.

4. **Report key naming: `--write` reports `diverged` (+ `sanctioned`), not `absorbed`.**
   *Clerk-resolved.* D4's text is "`absorbed: [...]`-style" — the "-style" hedge leaves
   naming to the brief. Under the fix nothing is absorbed anymore: the edit is preserved
   *and* reported, so an `absorbed:` key would assert the exact behavior the build
   removes. Ruling: `--write` output gains `"diverged": [...]` (unsanctioned live≠source
   at write time — the paths the old behavior would have silently absorbed),
   `"sanctioned": [...]` (excluded-and-denominated per A4), and `"sanction_stale": [...]`
   — mirroring `--verify`'s existing vocabulary, one word one meaning. Everywhere the
   roadmap routes "the `absorbed:` list" (A6), this write-time `diverged`/`sanctioned`
   pair is that list.

5. **A6's E2 census naming — the manifest-write report is named an E2 census entry and
   is NOT born under Q3a's persist shape in this build; the why-not:** *Clerk-resolved.*
   Q3a's general rule (report-emitting verbs persist verbatim to dated `.yaml` under a
   config path, retention row same build) is **B10-6's build** — the census (E2), the
   config-path plumbing, and the walker-exclusion declaration all land there. Building a
   one-off dated-`.yaml` path for this one report now would pre-empt the census and
   plant a second home for the persist rule before its single home exists (the exact
   drift CLAUDE.md's single-home discipline forbids). Instead: (a) this brief **names the
   manifest write as an E2 census-population entry** — B10-6's census must disposition
   the `verify-skill-manifest.py --write`/`--verify` reports explicitly (this paragraph
   is the register entry; B10-6's brief starts its census from E2's list plus this named
   addition); (b) interim durability is already real: the write-time
   `diverged`/`sanctioned` lines reach the **append-only upgrade ledger** via Step 5's
   Notes-line mechanism (F3) and the Confirm summary (F2), and the v0.13.0 discharge
   runs under roundtable A1's hand-save posture anyway.

6. **The sanction record's decay contract: extend the existing exempt row — a contract
   edit, priced.** *Clerk-resolved.* The operating contract is explicit
   (`vault-operating-contract.md:314`): "A new accumulating agent-zone file class enters
   this table in the act that creates it." The sanction record is an accumulating
   agent-zone file (rare, human-gated appends — one line per accepted migration ruling).
   Per A12's never-a-new-list spirit: **extend the existing exempt row at
   `vault-operating-contract.md:311`** (`{upgrade_ledger}`, `{overlays}`, `{tripwires}` —
   "slow, human-gated accumulators") to name `{overlays}/.skill-manifest.sanctioned`
   in-row, rather than adding a row or a second list. This is a contract edit ⇒
   **package-lint C6 fires**: re-stamp `_meta/vault-rule-card.md`'s `derived_from: …
   sha256:` against the edited contract (`vault-rule-card.md:11`); the row is not an
   act-blocking clause, so the card's clause content is expected unchanged and the
   `RULE_CARD_BUDGET` (8,000 bytes, `package-lint.py:251`) untouched — verify anyway.
   The contract is deliberately not handshaked; no `version:` moves.

7. **K9 fix shape (D7's drive-by): move the vocabulary out of the copied line.**
   *Clerk-resolved.* The defect class is an enumeration living only in a trailing
   comment on a line that a template copies verbatim into live files (S1 found the class
   at its origin: `vlt-sayari`'s `digested   # digested | draft`). Restyling the comment
   would leave the class intact. Ruling: the fenced template line at
   `capability-template.md:23` drops the enum from its comment; the legal vocabulary
   (`shipped | vault-grown`) is stated once in the template's surrounding prose (the
   body above the fence), which is read but never copied. Exact text in F4.

**Interim posture (R1) — substantive.** The A14 honesty note **is** a declared interim
posture shipped ahead of its mechanism: the one sentence in both issue forms states that
comments on captured issues reach the factory only via owner admission — that sentence is
the legal state of the world until B10-7 ships the `amended` re-triage channel and
replaces it with the affirmative-move text (comment + @mention). Nothing else in this
build ships a rule ahead of its mechanism: the sanction record ships **with** its writers
and readers in the same build, and the manifest semantics change ships with both prose
homes updated.

## F-sites

All sites re-grounded 2026-08-21 against v0.12.0 @ `336d90b` (capture ran the same day
against the same commit; no build has landed since). **Every site HOLDS — zero grounding
corrections, no superseding notes owed.**

### F1 — `skills/vlt-setup/scripts/verify-skill-manifest.py` (the core fix)

**Current state.** `compute_manifest` (`:72-104`): the shipped-name set comes from source
(`:81-83` — names only), but both hashing loops read the **live** tree — `:85`
`skill_dir = live_skills_dir / name` with `:90` `sha256_file(f)` over live files, and the
EXTRA_DIRS loop (`:92-102`) hashes installed files at `:102`. `--write` (`:172-208`)
reports only `added`/`removed` vs a prior manifest; `--verify` (`:210-236`) reports
`diverged`/`missing`. No sanction concept, no version check, no source==live detection.

**The exact change.**

1. **Source-hash for source-provenanced paths.** Rework `compute_manifest`:
   - *Shipped skill dirs:* for each shipped `vlt-*` name, walk the **source** skill tree
     (`source_skills_dir / name`), and for each non-cruft source file record entry path
     `str((live_skills_dir / name / relpath).relative_to(root))` with
     `sha256_file(source_file)`. Keep the existing `if not (live_skills_dir /
     name).is_dir(): continue` guard (a shipped skill absent live stays unmanifested,
     as today). A source file whose live counterpart is missing is still recorded —
     `--verify` then reports it `missing`, which is the honest finding (a failed copy).
   - *Live-only files ("live only where no counterpart exists", the ruled clause):* a
     live file under a shipped skill dir with **no** source counterpart at the same
     relpath keeps today's behavior — hashed from live and recorded (preserves the
     current net over de-facto extras; the shrink check still reports departures).
   - *EXTRA_DIRS:* build a basename → source-path map from the shipped
     `vlt-setup/assets/{workflows,hooks}` trees (error operationally, exit 2, on a
     duplicate basename — cannot happen in current source, but a silent arbitrary pick
     would be a new blind spot); for each installed file whose basename is mapped,
     record the live-relative path with the **source** file's sha. An installed file
     with no mapped basename stays unlisted (unchanged).
   - Return per-entry provenance alongside the sha (e.g. `{path: (sha, "source"|"live")}`
     internally) so the write-time divergence pass knows which entries can diverge.
2. **Write-time divergence report (D4 + A4, dispositions 3–4).** In `--write`, after
   computing entries and before writing: for every source-hashed entry whose live file
   exists and whose live sha ≠ entry sha, classify against the sanction record — 
   `"diverged"` (unsanctioned), `"sanctioned"` (live sha equals the record's sha for that
   path). Add `"sanction_stale"` for record entries whose live sha now equals the source
   sha. Add `"source_mode": "source" | "live"` and, in live mode, the top-level
   `"warning"` (disposition 1). **The write always proceeds** — report, never refuse
   (D4) — except the version-skew refusal below.
3. **Version-skew refusal (A5, disposition 2).** In `--write` with
   `source_mode == "source"`: parse `module_version:` from
   `{source_skills_dir}/vlt-setup/assets/module.yaml` and
   `{live_skills_dir}/vlt-setup/assets/module.yaml` (stdlib line-parse); mismatch →
   stderr named error **`version-skew`** with both versions and the recovery line, exit
   2; unreadable/missing → **`version-record-missing`**, exit 2.
4. **Sanction partition in `--verify` (disposition 3).** Split today's `diverged` into
   `diverged` (unsanctioned) and `sanctioned` (denominated), plus `sanction_stale`.
   `missing` unchanged. Exit codes unchanged (0 with findings; divergence is the
   caller's to surface).
5. **CLI:** add `--sanctioned <path>` (default derived from `--overlays-dir` as
   `{overlays-dir}/.skill-manifest.sanctioned`; absent file ⇒ empty set). Update the
   module docstring (`:5-38`) — it currently documents the live-hash scope and must
   state the source-hash rule, the sanction record, and the two named errors (the
   docstring is the script's single-home mechanics statement that
   `vlt-upgrade/SKILL.md:38` defers to).

**Why:** A10-6's core defect — the net's baseline must be *stock*, not *whatever is on
disk*; this is the single site the capture grounded as making both prose claims true.

**Out-of-scope note (per-site):** no change to manifest file format (`<sha256>\t<path>`
— readers exist; provenance is computed, not stored) and no change to `--verify`'s
comparison target (live vs manifest — the manifest now *is* stock, which is the fix).

### F2 — `skills/vlt-setup/SKILL.md` (the false claim, the fallback, the Confirm line)

**Current state.** `:153` — the manifest paragraph ends "Compute it from the *installed*
shipped files (which equal stock at install time), so the next upgrade's pre-flight
compares against what this install shipped" (the claim capture graded "true once, false
thereafter"). `:156-161` — the invocation block (no `--sanctioned`). `:163` — the
fallback paragraph: fresh-install live-as-source, and the later-re-run allowance
("only if no locally-minted `vlt-*` dir exists"). `:324` — the Confirm bullet's manifest
sentence ("the **skill-asset manifest** written (entry count, plus `added`/`removed` vs
the prior manifest when one existed — removals always shown)").

**The exact change.**

1. `:153` — replace the "Compute it from the *installed* shipped files…" clause with the
   true rule: the manifest records **stock content — hashed from the module source tree
   for every source-provenanced path, live only where no source counterpart exists** —
   so a local edit present at write time is *reported as divergence, never absorbed as
   the new baseline*; keep the surrounding sentence's purpose ("so the next upgrade's
   pre-flight compares against what the module shipped"). Add one sentence stating the
   write-time report surfaces `diverged`/`sanctioned` (mechanics by pointer to the
   script — single-home; do not restate the partition rules here) and that **the write
   refuses with the named error `version-skew`** when the source tree's `module_version`
   ≠ the installed record's.
2. `:156-161` — extend the invocation block with `--sanctioned
   "$ROOT/<resolved {overlays}>/.skill-manifest.sanctioned"` (or note the
   `--overlays-dir` default covers it — match the block's existing style).
3. `:163` — keep both fallback allowances but close the silence (A5): append that when
   the live dir serves as the source, **the write reports `source_mode: live` and a loud
   warning that the net is live-hashed for that write** (blind to pre-existing edits) —
   surface that warning in the Confirm summary, never swallow it.
4. `:324` — extend the Confirm manifest sentence: "…removals always shown), **plus its
   write-time `diverged` (unsanctioned local edits preserved-and-reported, never
   absorbed) and `sanctioned` (N sanctioned divergences: paths) lines, and the
   live-hashed warning when `source_mode: live`** — always shown when non-empty."
5. **The sanction record's never-touch line:** in the manifest paragraph (`:153`), one
   sentence: `{overlays}/.skill-manifest.sanctioned` is the vault's sanction record
   (written by the sanctioning acts in `vlt-upgrade` Step 3, read by the script) —
   **`vlt-setup` never creates, writes, or clobbers it** (the overlay-zone posture at
   `:151` applied).

**Why:** the shipped claim must match the shipped behavior (A10-6); the fallback and
Confirm edits are A5/A6's routing halves.

### F3 — `skills/vlt-upgrade/SKILL.md` (the second claim, the sanction writers, the report routing)

**Current state.** `:38` — Step-1 skill-asset divergence bullet (runs `--verify`; JSON
`diverged`/`missing` are the finding). `:49` — Step-2 own-the-apply bullet ends "The
skill manifest itself is refreshed to the new shipped versions by the Step-6 provision
hand-off (it is module-owned in `vlt-setup`)" — capture graded it false (refreshed to
*live* versions). `:81` — Step 3 item 5, loop-profile relocation (the sanctioned lift;
leaves a pointer line in an installed partner's SKILL.md). `:84` — item 6, the provision
hand-off that triggers the write. `:86` — item 7, write-through (can edit "a skill's
stated rule"). `:93-110` — the Step-4 report YAML (`skill_asset_divergence` at `:105`).
`:121-139` — the Step-5 ledger entry shape, whose Notes line carries the
"name the report's … entries here when non-empty" mechanism (`:138`).

**The exact change.**

1. `:38` — the Step-1 bullet notes the `--verify` JSON now partitions
   `diverged`/`sanctioned`/`sanction_stale`/`missing` (mechanics stay single-homed in
   the script); a **sanctioned** divergence is a recorded legal state — denominated in
   the report, not a finding to route.
2. `:49` — the sentence becomes true as written once F1 lands; extend it with the
   honesty clause: "…by the Step-6 provision hand-off — **hashed from the source tree,
   so an edit landing between this refresh and that write is reported as divergence,
   never absorbed** (the ordering trap S3 confirmed is closed by construction)."
3. `:81` (loop-profile relocation) — one sentence: on an accepted lift, **the same act
   appends `<sha256>\t<path>` of the edited partner SKILL.md to
   `{overlays}/.skill-manifest.sanctioned`** (create the file if absent) — the sanction
   record the manifest verbs read; zero-ritual, no separate prompt (roundtable A4).
4. `:86` (write-through) — the parallel sentence: a ruling written through into a
   **shipped skill file** appends its sanction line in the same act. (A ruling into a
   convention base is out of the manifest's net — no line.)
5. Step-4 YAML (`:93-110`) — add one line after `skill_asset_divergence`:
   `manifest_write_divergence: [<path: live differed from source at manifest-write time (unsanctioned — preserved, reported; route per skill_asset_divergence) | N sanctioned divergences: <paths> | source_mode: live — net live-hashed this write>, ...]`
   — the A6 routing home: the Step-3.6 write's `diverged`/`sanctioned` output lands
   here, never-omitted-when-empty per the report's standing rule. Its **legal response
   (R3)** is stated in the same clause: unsanctioned entries route exactly as
   `skill_asset_divergence` routes (`:107`'s durable-host doctrine line — by pointer,
   not restated); sanctioned entries require nothing (that is what sanctioned means).
6. Step-5 ledger (`:138`) — extend the Notes-line instruction to also name the report's
   `manifest_write_divergence` entries when non-empty (the existing mechanism; the
   required-lines set is unchanged — no new ledger line, so no entry-shape migration).

**Why:** the second false claim (A10-6), the sanction writers (disposition 3 / A4), and
A6's routing of the write-time list into the post-flight report.

**Out-of-scope note (per-site):** Step-2's refresh treatment of sanctioned files (a
refresh clobbers the sanctioned edit back to stock and the lift's pointer line silently
evaporates — the sanction record then reports `sanction_stale`, making the state
*visible* for the first time) is deliberately not changed — see Out of scope item 2.

### F4 — `skills/vlt-mint/assets/capability-template.md:23` (the K9 drive-by)

**Current state.** Line 23, inside the fenced light-capability template that vaults copy
verbatim:
`provenance: vault-grown            # shipped | vault-grown (usually implied by location)`
— the legal vocabulary lives only in a trailing comment on a copied line (K9's
enum-in-comment class, found live at its template origin by S1).

**The exact change.** Line 23 becomes:
`provenance: vault-grown            # usually implied by location`
and the prose above the fence (the paragraph block at `:9-11`, after the "Ownership =
location" paragraph) gains one sentence stating the vocabulary once, uncopied:
"**`provenance:` takes exactly one of `shipped | vault-grown`** — stated here, not in a
copied comment, so live files never carry (or drop) their own vocabulary."

**Why:** D7 (drive-by ruling); the fix must retire the *class* (vocabulary riding a
copied comment), not restyle the instance.

**Out-of-scope note (per-site):** lines 20–22 (`write_scope`/`weight`/`council_class`)
also carry comment-borne vocabulary, but their enumerations are already stated in the
template's body prose (`:5-6`, the two-weights bullets) — the comments are restatements
with a prose home, not the vocabulary's only home. K9's ruled site is `:23` alone; do not
widen the drive-by.

### F5 — `.github/ISSUE_TEMPLATE/{field-defect,field-pattern-candidate}.yml` (the A14 drive-by)

**Current state.** Both forms open with a markdown intro block
(`field-defect.yml:11-16`, `field-pattern-candidate.yml:11-18`) pointing at the field
contract and recommending `vlt-feedback`. Neither says what happens to comments — today's
silence is the honesty gap A10-8 names.

**The exact change.** Append **one sentence** to each intro block (after
`field-defect.yml:16` / `field-pattern-candidate.yml:18`), the same sentence in both:
"Note: comments added after an issue is labeled `captured` reach the factory only if the
owner admits them by hand — an amendment channel is planned; until it ships, assume a
comment on a captured issue is not read."
This is interim text by design — **B10-7 replaces it** with the affirmative-move wording
(comment + @mention; roundtable A14). Keep it to the one sentence: the forms are
ADDITIVE-ONLY surfaces (their own header rule) and this touches no field, label, or
meaning — no `rail_contract` bump.

**Why:** roundtable A14; R1's declared interim posture (disposition block above).

### F6 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:311` + `_meta/vault-rule-card.md` (the sanction record's decay contract)

**Current state.** The Decay-contracts table's exempt row at `:311`:
`| {upgrade_ledger}, {overlays}, {tripwires} | exempt — slow, human-gated accumulators (one entry per upgrade / append-only local rules / rare wire edits); their append-only declarations stand | — | — | — |`
and the birth rule at `:314` ("A new accumulating agent-zone file class enters this table
in the act that creates it"). The rule card carries `derived_from: …
sha256:cdf187b5…` (`vault-rule-card.md:11`).

**The exact change.** Extend the `:311` row in place — the file-class cell becomes
`{upgrade_ledger}`, `{overlays}` (incl. `.skill-manifest.sanctioned`, the manifest's
sanction record), `{tripwires}`; the reason cell's parenthetical gains "/ one line per
sanctioned migration edit". Extending the existing row, never a new list (A12's
discipline). Then **re-stamp the rule card**: recompute the shipped contract's sha256 and
update `vault-rule-card.md:11`'s `derived_from:` — the row is not an act-blocking clause,
so the card's clause content is expected unchanged and the byte size stays under
`RULE_CARD_BUDGET` (8000, `package-lint.py:251`); package-lint **C6** is the check of
record.

**Why:** the contract's own birth rule (`:314`) makes the row mandatory in the act that
creates the file class; disposition 6 prices it.

## Registration

**None.** No new skill (no `marketplace.json` `skills[]` entry, no `module-help.csv`
row), no workflow change, no convention `version:` moves (skill prose and a contract row
— the contract is deliberately not handshaked), so no consumer walk / re-ack.

**"No bump owed" is not "no cost" — priced:**
- **package-lint C6** — fires (F6's contract edit): rule-card re-stamp +
  `RULE_CARD_BUDGET` re-check, in this build. This is the one gate this build touches.
- **package-lint E4** — not owed: no new `package-lint` check is added
  (`verify-skill-manifest.py` is a shipped skill script, not a lint check;
  `tools/test-package-lint.py` and `CASE_FLOOR` are untouched).
- **package-lint E5** — not owed: no asset `// depends_on:` header changes
  (`vlt-lint-full.js` untouched — that is B10-2).

## Out of scope (dispositioned)

1. **B9-6's durable metric home / overlay bell / Finding 4** — deferred-to-build-B10-4;
   this build merely unblocks its brief (Q4/S3 sequencing).
2. **Step-2 refresh semantics for sanctioned files** (carry-forward vs
   clobber-and-surface; the detect-preserve-**reapply** third verb) — rejected-because:
   not ruled anywhere in the batch, and the roundtable already routed the instrument gap
   to `inbox/` (Carson's out-of-scope item 1). The sanction record makes the state
   visible (`sanction_stale`); if the field shows sanctioned edits evaporating on
   refresh, that is a filing, not a silent widening of this build.
3. **The lint fan-out / `convRead` / `write-verification` handshake** —
   deferred-to-build-B10-2 (D1).
4. **Persisting the manifest-write report as a dated `.yaml`** —
   deferred-to-build-B10-6 per disposition 5 (the E2 census entry is named there; the
   why-not is on record per A6's "or the brief records why not").
5. **`module.yaml` dependency declarations (`uv` for this script, `gh`)** —
   deferred-to-build-B10-8 (D6); this build adds no new tool dependency (`uv` was
   already the invocation).
6. **The template's other comment-borne vocabulary (`capability-template.md:20-22`)** —
   rejected-because: prose homes exist for those enums (F4's per-site note); D7 ruled
   `:23` alone.
7. **B10-7's full template text (the `amended` label, the @mention move)** — the F5
   sentence is explicitly interim; B10-7 supersedes it (roundtable A14).
8. **Manifest file-format change (storing provenance or sanctions in the manifest
   itself)** — rejected-because: the manifest is module-owned and overwritten on every
   provision; vault-grown sanction state inside a module-overwritten file violates the
   durability posture (two classes of evolution, two fates). The sanction record is a
   separate vault-owned file by design.

## Verification (unit, at rest — lifecycle step 5)

Real script runs against temp fixture trees (build them under the scratchpad; a fixture
= a fake `--root` with a live skills dir, a source skills dir, both `module.yaml`s, and
an overlays dir):

1. **Red-then-green core reproduction (A10-6's synthetic case).** Fixture: source tree
   with one shipped `vlt-*` skill; install (copy) to live; hand-edit one live manifested
   file. *Red (pre-fix, current script):* `--write` → `--verify` reports clean (the edit
   absorbed). *Green (post-fix):* `--write` reports the path in `diverged`, the manifest
   carries the **source** sha, and `--verify` still reports `diverged`. Record the
   red-then-green in the BUILT status.
2. **Live-as-source fixture (A5).** `--source-skills-dir` == live dir → write proceeds,
   JSON carries `source_mode: "live"` + the warning; normal path carries
   `source_mode: "source"` and no warning.
3. **Version-skew fixture (A5).** Source `module.yaml` `module_version:` ≠ installed →
   exit 2, stderr names `version-skew` and both versions; missing installed record →
   exit 2, `version-record-missing`.
4. **Sanction fixtures (disposition 3).** (a) Sanction record entry matching the live
   edit → `--verify` and `--write` report it under `sanctioned` (excluded from
   `diverged`), denominated; (b) a further edit on top of a sanctioned file →
   `diverged`; (c) live restored to source → `sanction_stale`; (d) absent record file →
   empty set, no error.
5. **Live-only counterpart fixture.** A live file under a shipped skill dir with no
   source counterpart → still manifested, live-hashed, `--verify` clean (current
   behavior preserved).
6. **Cross-file greps.** "Compute it from the *installed* shipped files" gone from
   `vlt-setup/SKILL.md`; `.skill-manifest.sanctioned` named at exactly the designed
   sites (script, `vlt-setup/SKILL.md` §2 manifest paragraph, `vlt-upgrade/SKILL.md`
   items 5+7 and Step-1/Step-4, contract `:311`) and nowhere else; the enum
   `shipped | vault-grown` present in `capability-template.md` prose and absent from the
   fenced line's comment; the identical honesty sentence in both issue forms;
   `manifest_write_divergence` present in Step-4 YAML and the Notes-line instruction.
- **Handshake bipartite re-check** — not owed (no convention `version:` moved, no
  `consumers:` list or structure map changed). The mid-arc lint run below still executes
  Group E as part of A/B/C/E.
- **Packaging lint** — mid-arc `uv run tools/package-lint.py` **A/B/C/E** run, expected
  PASS — with **C6 green against the F6 re-stamp** (this is the check of record for the
  contract edit; do not hand-verify the sha). D / `--expect-version` rides the B10-5
  release build, not here.
- **Fixture extension (R2): not applicable** — no release-gate check added or changed
  (`tools/test-package-lint.py` untouched).
- **Legal response (R3): substantive** — the new write-time divergence class states its
  legal response at its home in the same build: unsanctioned → the durable-host routing
  by pointer (F3.5, riding `skill_asset_divergence`'s existing doctrine line); sanctioned
  → none required, denominated. Stated once, in the Step-4 report clause where the class
  lives.
- **Enumeration widening (R4): substantive** — the build creates one new file class
  (`{overlays}/.skill-manifest.sanctioned`): it enters the contract's Decay-contracts
  table in the same act (F6, the birth rule at `:314`), and is **declared outside the
  skill-manifest net by construction** (it lives under `{overlays}`, not a shipped skill
  dir or EXTRA_DIRS — the net cannot manifest its own sanction record, which is correct:
  it is the vault's). No always-loaded/vitals enumeration reads it.
- **Scrub** — no personal or vault-local content in any changed shipped file (the F5
  sentence, F2/F3 prose, F4 template, F6 contract row are all generic; worked examples
  stay placeholder-pathed).

## Release

Not the release build — v0.13.0 cuts after B10-5 (roadmap release line). No version
strings move here; the dual bump, the `--expect-version` gate, and the ff-merge/tag/push
ride B10-5's release choreography.

## Acceptance (live — appended to the roadmap ledger)

Five checks; the same prose goes to the roadmap's Deferred acceptance ledger this run.

1. **`[ship-verifiable]` — the divergence net catches the edit it exists to catch.**
   The synthetic reproduction (Verification 1) discharged at rest, red-then-green
   recorded in the BUILT status: hand-edit a manifested file → `--write` → `--verify`
   **still reports `diverged`** (the pre-fix behavior — clean — is the red). Bounded:
   dischargeable in the build session and re-runnable at the v0.13.0 gate.
2. **`[ship-verifiable]` — the live-as-source escape path is loud (A5 fixture 1).**
   A write with source == live carries `source_mode: "live"` + the warning in its JSON,
   and the Confirm/Step-4 routing text ships. Discharged at rest by Verification 2 + the
   F2/F3 greps.
3. **`[ship-verifiable]` — the version-skew escape path refuses (A5 fixture 2).**
   A write against a source whose `module_version` ≠ the installed record exits 2 with
   the named error `version-skew` (the `gh-missing` discipline). Discharged at rest by
   Verification 3.
4. **`[ship-verifiable]` — both prose claims true, both drive-bys landed, the contract
   row priced.** Greps at rest: `vlt-setup/SKILL.md` no longer claims installed-files
   compute; `vlt-upgrade/SKILL.md:49`'s refreshed-to-shipped sentence is now literally
   true and carries the trap-closed clause; `capability-template.md:23`'s enum lives in
   prose, not the copied comment; both issue forms carry the identical interim honesty
   sentence; the contract `:311` row names the sanction record and package-lint **C6
   passes** against the re-stamped rule card.
5. **`[field-contingent]` — the first live upgrade under the fixed net reports
   honestly.** Discharging event, named per the R5-style rule: **the owner's vlt-core
   upgrade to v0.13.0** (already scheduled as the release's acceptance run; performer:
   the owner; vault: vlt-core, whose evidence reaches the factory via roundtable A1's
   hand-saved Step-4 report). Pass = the Step-3.6 manifest write's
   `manifest_write_divergence` line appears in the Step-4 report (empty or not, never
   omitted); any Step-3 sanctioned migration edit made in that run shows as
   **sanctioned-and-denominated, not silently blessed**; and the known vlt-core local
   edits that the 2026-08-21 run had to re-establish by hand remain `diverged` on the
   post-upgrade `--verify` instead of being absorbed. Fail = a clean report over a vault
   whose live tree differs from v0.13.0 stock at any unsanctioned manifested path.

---
*Brief authored by `build-brief` (autonomous run 2026-08-21, owner review pending on the
seven clerk-resolved dispositions). Grounding: all sites HOLD against v0.12.0 @ 336d90b;
zero grounding corrections.*
