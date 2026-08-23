---
title: 'Build #3 — vlt-lint-full Hardening: cost-tiering, noise, cap, cross-layer links + CSV quoting audit (Phase A)'
status: 'BUILT 2026-06-23 — unit-verified; acceptance (live --full sweep) pending a real wiki'
build_log:
  - 'BUILT 2026-06-23. All five components landed + unit-verified. C1 model tiering: scanModel/indexModel/clusterModel args (haiku/sonnet/sonnet defaults) passed on the three agent() calls; meta.phases annotated; node --check passes. C2 near-dup: rewrote the predicate to exclude cluster-hub links (derived from the inbound map, threshold max(5, 25% of pages)) then flag IFF shared-non-hub ≥3 AND (slug-stem OR title-Jaccard ≥0.5) — synthetic harness confirms hub co-citation no longer flags while genuine stem/title dups still do. C3 cluster cap: default now Math.max(12, ceil(pages/4)) (12@≤48p, 17@65p, 50@200p) — no false cap at the 13-cluster case. C4 cross-layer: missing_targets now excludes a passed-in crossLayerSlugs set; the vlt-lint SKILL globs {research}+agent-zone basenames and passes them; a genuine dangling link still surfaces. C5: column-count assertion added to merge-help-csv.py read_csv_rows (fires with located error on an unquoted-comma row; shipped module-help.csv audited clean — 13 cols, 11 rows). Surfaces: vlt-lint-full.js, vlt-lint/SKILL.md, merge-help-csv.py. NOT touched: source-count policing (Phase B), the Phase-0 args guard, the fan-out/JS-reduce/single-writer split, coverage_caps honesty, Gap-B slots. Remaining: a live --full sweep to confirm the ~10x cost drop empirically (needs a real/representative wiki).'
derives_from:
  - 'skills/reports/inbox-evolution-roadmap.md (Phase A — Stop the bleeding; scope corrected 2026-06-23)'
  - 'inbox/2026-06-06-193105-vlt-lint-full-infra-and-cost-fixes.md (filing #3 — items #2 cost, #4 accuracy/cross-layer, #5 near-dup noise, #6 cluster cap)'
  - 'inbox/2026-06-15-163847-vlt-dispatch-partner-communication-bus.md (filing #9 — the CSV-quoting latent bug)'
module_code: 'vlt'
created: '2026-06-23'
updated: '2026-06-23'
decisions_locked:
  - 'SCOPE: build-3 = lint-full hardening (vlt-lint-full.js) + a module-help.csv quoting audit. Filing #1 (vlt-setup SSoT/dep-check/wart) is ALREADY SHIPPED (commit c918274) — out of scope. Filing #3 §3 (source-count drift) is DEFERRED TO PHASE B — the module convention (wiki-index.md) still defines source counts, so the consumers are correctly in sync; stripping now would create drift. Phase 0 already fixed filing #3 §1 (args-as-string).'
  - 'COST (filing #3 §2): per-pass model tiering via args with defaults — scanModel||"haiku" (the ~65 pure-extraction page scanners), indexModel||"sonnet", clusterModel||"sonnet". Pass on the respective agent() calls; annotate meta.phases[].model. The single biggest win (~10x on a 65-page wiki — scanners were running on Opus).'
  - 'NEAR-DUP NOISE (filing #3 §5): flag a pair IFF it has a shared-link signal AND a secondary signal (shared slug-stem OR title similarity) — never shared-links alone. Exclude cluster-hub links (high-inbound links) from the shared count before comparing, so hub/entity co-citation stops manufacturing false pairs.'
  - 'CLUSTER CAP (filing #3 §6): clusterCap default scales with page count instead of a hard 12 (which sat just below the 13 natural clusters on the live wiki). Keep the explicit-arg override and the coverage_caps honesty.'
  - 'CROSS-LAYER WIKILINKS (filing #3 §4): a [[link]] target that resolves to a research / agent-zone note (not a wiki slug) is NOT a missing target. The SKILL passes the set of valid cross-layer basenames into the workflow; the reduce excludes them before populating missing_targets.'
  - 'CSV AUDIT (filing #9): the shipped module-help.csv has no vlt-dispatch row (dispatch is the separate strand, not upstreamed) — so this is the GENERAL quoting hygiene fix, not the dispatch row. Add a column-count assertion to merge-help-csv.py read_csv_rows (a mis-split row from an unquoted embedded comma has the wrong column count → error loudly, never merge silently) + audit the shipped source CSV.'
  - 'The script has NO filesystem access (it reduces returned findings) — so any check needing to read files (cross-layer link resolution, the optional deterministic checks) is fed by the SKILL, which already globs the page set. This constraint is load-bearing for C4.'
surfaces:
  - 'skills/vlt-setup/assets/workflows/vlt-lint-full.js (the workflow — C1 model tiering, C2 near-dup, C3 cluster cap, C4 missing_targets reduce; this is the module SOURCE, installed into vaults by vlt-setup → {project-root}/.claude/workflows/)'
  - 'skills/vlt-lint/SKILL.md (Step 0 invoke — pass scanModel/indexModel/clusterModel + crossLayerSlugs; Step 2/5 wording for near-dup signal + cross-layer links)'
  - 'skills/vlt-setup/scripts/merge-help-csv.py (C5 — column-count assertion in read_csv_rows)'
  - 'skills/vlt-setup/assets/module-help.csv (C5 — audit every row for embedded commas in unquoted fields; appears already-clean)'
---

# Build #3 — vlt-lint-full Hardening (Phase A: Stop the bleeding)

## Scope in one paragraph

`vlt-lint-full` is the fan-out wiki health-check (one agent per page, JS reduce). Its first real run on the 65-page `vlt-core` wiki (filing #3) worked — but cost ~10× what it needed to (every agent ran on Opus, though ~65 of 78 are pure structured extraction), and its JS reduce manufactured noise: the near-duplicate heuristic fired 70 false pairs from hub/entity co-citation, the contradiction-cluster cap sat one below the natural cluster count, and `missing_targets` flagged 14-of-17 valid cross-layer `[[wikilinks]]` (to research/agent-zone notes) as broken. Phase 0 already fixed the args blocker (§1); filing #1's setup fixes already shipped (`c918274`); and the source-count drift (§3) defers to Phase B (the module convention still defines counts). What remains is a tight, single-surface hardening of `vlt-lint-full.js` (+ its `vlt-lint` caller): **per-pass model tiering** (the ~10× win), **a precise near-duplicate rule** (shared-link AND a secondary signal, hubs excluded), **a page-count-scaled cluster cap**, and **cross-layer-aware missing-target resolution** — plus a small **CSV-quoting audit** (filing #9's latent bug) hardening `merge-help-csv.py` against an unquoted-comma row mis-splitting on read.

## Why this grouping (the "one finder, made cheap and quiet" argument)

Every component here makes the *same finder* cheaper or quieter, and four of the five touch one file (`vlt-lint-full.js`); the fifth (CSV audit) is the one extra Phase-A tactical-robustness bug that has no home of its own and is too small to brief alone. Unlike Build #2 (a machine plus its first run), this is pure remediation of a machine that already shipped and field-ran — so there is no acceptance "mint" to fold in; the acceptance exercise is **re-running the sweep on a real wiki and confirming the cost drop + the noise disappearance** against the filing's recorded numbers. Bundling is by single-surface coherence, not theme: the broad "Phase A — stop the bleeding" bundle collapsed to this once filing #1 was found already-done and §3 was routed to Phase B during ideation.

## Surfaces touched

| File | What changes |
| --- | --- |
| `skills/vlt-setup/assets/workflows/vlt-lint-full.js` | **The workflow (module source).** **C1** — add `scanModel`/`indexModel`/`clusterModel` args (defaults `haiku`/`sonnet`/`sonnet`), pass `model:` on the page-scan, index, and cluster `agent()` calls, annotate `meta.phases[].model`. **C2** — rewrite the near-duplicate block (lines ~124–140): compute a hub set from the existing `inbound` map, exclude hub links from the shared count, and flag IFF `shared ≥ N AND (sameStem OR titleSimilar)`. **C3** — `clusterCap` default scales with `pages.length` (line ~40). **C4** — `missing_targets` reduce (lines ~121–122) excludes targets present in a passed-in `crossLayerSlugs` set; add `crossLayerSlugs` to the args contract + guard. |
| `skills/vlt-lint/SKILL.md` | **The caller.** Step 0 invoke (line ~41): pass `scanModel`/`indexModel`/`clusterModel` (omit to take defaults) **and** `crossLayerSlugs` — the SKILL already globs `{wiki}`; add a cheap glob of `{research}` (and any agent-zone note dirs it links into) for basenames, passed so the reduce can resolve cross-layer links. Step 2 *Near-duplicates* wording (line ~58) updated to the AND-rule. Step 2 *Missing targets* (line ~53) + Step 5 report note: a target resolving to a research/agent-zone note is not missing. **No source-count wording touched (that's Phase B).** |
| `skills/vlt-setup/scripts/merge-help-csv.py` | **C5.** In `read_csv_rows` (line ~74): after parsing, assert every data row has exactly `len(header)` columns; on mismatch, raise with the offending row index + content (an unquoted embedded comma mis-splits a row into too many columns — fail loudly rather than merge a corrupt row). Mirror the same assertion for `--source`. |
| `skills/vlt-setup/assets/module-help.csv` | **C5 audit.** Verify every field containing a comma is quoted (Python's `csv.writer` quotes on write, but a hand-edited source can drift). Current read shows all comma-bearing fields already quoted — so this is expected to be a no-op confirmation; fix any that aren't. |

---

## Component 1 — Per-pass model tiering (the ~10× cost win) — filing #3 §2

**The waste:** on the 65-page run, ~65 of 78 agents were pure structured extraction (read one page, return the `PAGE_SCAN` schema — no deep reasoning) yet ran on the default Opus (~2.1M tokens). The page scanners are the overwhelming majority of the spend and the cheapest work.

**The change (in `vlt-lint-full.js`):**
- Read three optional model args near the top (beside `clusterCap`):
  ```js
  const scanModel    = a.scanModel    || 'haiku'   // ~65 pure-extraction page scanners
  const indexModel   = a.indexModel   || 'sonnet'  // one index-drift pass, light reasoning
  const clusterModel = a.clusterModel || 'sonnet'  // cross-page contradiction judgement
  ```
- Pass `model:` on each `agent()` call: the page-scan fan-out (line ~108) gets `{ …, model: scanModel }`; the index pass (line ~143) `{ …, model: indexModel }`; the cluster pass (line ~176) `{ …, model: clusterModel }`.
- Annotate `meta.phases` so the cost shape is legible: `{ title: 'Scan pages', …, model: 'haiku' }`, `{ title: 'Reduce + cross-page', …, model: 'sonnet' }`.
- Update the args-contract comment block (lines ~18–25) to document the three new optional args.

**Design note — why these tiers.** Page scanners are exhaustive extraction against a fixed schema → `haiku` is sufficient and is where the 10× lives. The index pass and the cross-page contradiction pass involve light cross-document judgement → `sonnet`. Nothing here needs Opus. The args keep it tunable per invocation (a caller can force `scanModel:'sonnet'` for a high-stakes audit) without editing the workflow. (Model aliases `haiku`/`sonnet`/`opus` are the `agent()` `model:` option's accepted values; the sibling `vlt-review-council.js` shows the same `agent(prompt, {label, phase, schema})` idiom this extends.)

## Component 2 — Precise near-duplicate detection (kill the 70 false pairs) — filing #3 §5

**The noise:** the current rule (line ~137) is `if (shared >= 3 || sameStem)` — a pure OR on shared outbound links, threshold 3. On a real wiki, hub pages and shared entity pages get co-cited everywhere, so "≥3 shared links" fires constantly (70 pairs, all false). The signal is real only when it *coincides* with another similarity.

**The change (rewrite the near-duplicate block, ~lines 124–140):**
1. **Exclude cluster-hub links before counting.** The reduce already builds an `inbound` count map (lines ~117–118). Derive a hub set — links whose inbound count is high relative to the corpus (e.g. `inbound.get(l) > max(5, scans.length * 0.25)`, tune against the live numbers). Build each page's `linkSet` from its outbound links **minus hubs**, so co-citing the same hub no longer counts as shared.
2. **Require two independent signals.** Flag a pair IFF it has a shared-link signal **AND** a secondary signal:
   - shared (non-hub) links `≥ N` (keep ~3, now meaningful post-hub-exclusion), **AND**
   - (`sameStem` **OR** `titleSimilar`) — `sameStem` is the existing first-two-slug-segments match; `titleSimilar` is a cheap token-overlap on the `title` field the `PAGE_SCAN` already returns (e.g. Jaccard of lowercased title tokens above a threshold).
3. Keep the existing `pairBudget` cap + `nearCapped`/`coverageCaps` honesty unchanged — only the *predicate* changes.

**Note the signal in the output** so a human can see *why* a pair flagged: keep the existing `(${shared} shared links)` / `(shared slug stem)` annotation and extend it (`(N shared non-hub links + title overlap)`).

**Design note.** This is the filing's strongest option (combine signals) deliberately chosen over a high-threshold-Jaccard-only approach — co-citation density is exactly what Jaccard-alone still rewards, so a structural secondary signal (stem/title) is what actually discriminates a true near-duplicate from two well-connected siblings.

## Component 3 — Page-count-scaled cluster cap — filing #3 §6

**The off-by-one:** `clusterCap = a.clusterCap || 12` (line ~40). The live wiki had 13 natural contradiction clusters — so the default silently capped one cluster every run and reported it in `coverage_caps`, even though nothing was actually too big.

**The change:** scale the default with the page count, keeping the explicit override:
```js
const clusterCap = a.clusterCap || Math.max(12, Math.ceil(pages.length / 4))
```
(Tune the divisor against observed cluster-to-page ratios; the point is the floor of 12 holds for small wikis while large wikis don't trip a false cap.) The `clusters.length > clusterCap` guard, the slice, and the `coverage_caps` message (lines ~166–171) are unchanged — only the default is no longer a fixed 12.

## Component 4 — Cross-layer-aware missing targets (14/17 were valid) — filing #3 §4

**The false positives:** `missing_targets` (lines ~121–122) declares any `[[link]]` whose slug isn't in `slugSet` (the wiki page set) as missing. But the vault links *across layers* — wiki pages legitimately `[[link]]` to `_agent/research/` and other agent-zone notes. On the live run, 14 of 17 "missing" targets were valid cross-layer links.

**The change (the script has no filesystem access, so the SKILL feeds it):**
- **Args contract:** add `crossLayerSlugs: [string]` (optional) — the normalized basenames of valid non-wiki link targets (research notes, agent-zone notes the wiki may reference). Update the guard/comment; default `[]`.
- **Reduce:** build `const crossLayer = new Set(a.crossLayerSlugs || [])` and change the missing test to `if (!slugSet.has(l) && !crossLayer.has(l)) missing_targets.push(…)`.
- **Caller (`vlt-lint` Step 0):** the SKILL already globs `{wiki}` to build `pages`; add a cheap glob of `{research}` (and any agent-zone note location the wiki conventionally links into) for basenames, normalized the same way page slugs are, and pass as `crossLayerSlugs`.

**Design note — keep it a denylist of known-valid, not a guess.** We only suppress links that resolve to a *real* cross-layer note the SKILL actually found on disk; a `[[link]]` to nothing anywhere still surfaces as missing. This preserves the check's value (genuinely dangling links) while removing the structural false-positive class. (This is the *finding*-side fix; the broader "resolve targets against the whole vault" stays bounded to what the SKILL can cheaply enumerate.)

## Component 5 — CSV-quoting audit + read-time guard — filing #9 (latent bug)

**The latent bug:** in the `vlt-core` install, the *live* `module-help.csv` had a scope field containing a comma left **unquoted**, while the `vlt-setup` mirror had it quoted — a strict CSV parser mis-splits the unquoted row into too many columns. `merge-help-csv.py` reads with `csv.reader` and writes with `csv.writer` (which quotes correctly on write), so the corruption manifests at **read** time, *before* the writer can normalize it — a mis-split row silently merges with shifted columns.

**The change:**
- **`merge-help-csv.py` `read_csv_rows` (line ~74):** after `rows = list(reader)`, assert every data row has exactly `len(header)` columns. On mismatch, raise a clear error naming the row index + offending content ("row N has K columns, expected H — likely an unquoted comma in a field"). Apply to both the `--target` and `--source` reads. This converts a silent corruption into a loud, located failure.
- **Audit `skills/vlt-setup/assets/module-help.csv`:** confirm every comma-bearing field is quoted. The current file's comma fields (descriptions, `outputs`, multi-value `args`) all read as already quoted — expected no-op; fix any drift found.

**Note:** the shipped module CSV has **no `vlt-dispatch` row** — dispatch isn't upstreamed yet (it's the separate "(strand) Dispatch bus mirror" build). So filing #9's dispatch-row retitle is *not* part of build-3; only the general quoting hygiene + the read-guard are. When the dispatch strand lands, it inherits a CSV reader that now refuses to merge a mis-quoted row.

---

## Build sequence

Dependency order; each step is independently verifiable.

1. **C1 model tiering** — smallest, highest-value, zero behavioral risk (pure cost). Land first so the re-test sweeps cheaply.
2. **C3 cluster cap** — one-line default change; trivial.
3. **C2 near-dup rewrite** — the largest logic change; the hub-exclusion reuses the `inbound` map C-nothing-else depends on. Verify the predicate against the recorded 70-false-pair case (should drop to near-zero true pairs).
4. **C4 cross-layer links** — touches both the workflow args and the SKILL caller; do the workflow side + SKILL side together so the new arg is produced and consumed in one step.
5. **C5 CSV guard + audit** — independent of the workflow; can land any time. Add the assertion, run it against the shipped CSV (expect pass), and over a deliberately-broken fixture (expect the located error).
6. **Acceptance:** re-run a `--full` sweep on a real (or representative) wiki via `vlt-lint` and confirm: (a) scanners run on haiku (cost drop toward the filing's ~10×), (b) `near_duplicates` no longer lists hub co-citation pairs, (c) no spurious cluster cap on a ~13-cluster wiki, (d) cross-layer `[[links]]` no longer appear in `missing_targets`. Honor `coverage_caps` honesty throughout — never present a capped sweep as exhaustive.

**Protect (don't regress) — carried from filing #3's "protect" list:** the fan-out + JS-reduce split (finding is parallel + read-only; the SKILL is the single writer); `files_checked`/`files_listed`/`coverage_caps` honesty; the budget-guard chunking; the Gap-B slots (`contradictions_handled`, `sources_vs_prose_mismatch`); and the Phase-0 args-parse guard at the top of the file (do not remove). **Do not touch source-count policing** in either the workflow or the `vlt-lint` SKILL — it is in sync with the module's `wiki-index.md` convention and its removal is Phase B work.

### Resume caveat carried from filing #3
Resuming the workflow with `resumeFromRunId` **without** re-passing `args` nulls them (the runtime delivers args fresh each run). Any caller that resumes a sweep must re-pass the full args object (now including the model + `crossLayerSlugs` keys). This is a documentation note for the `vlt-lint` Step 0 invoke, not a code change.
