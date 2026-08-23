---
type: inbox
created: 2026-06-06
title: "vlt-lint-full — infra bugs, cost optimization, and convention drift found during first full lint"
source: live run in vlt-core (65-page wiki, first `vlt-lint --full`)
component: vlt-lint skill + vlt-lint-full workflow
priority: high (one blocker bug + one ~10x cost win)
---

# vlt-lint-full — issues & optimizations to fold into the next module version

Filed from the first real `vlt-lint --full` run against a 65-page wiki (`vlt-core`).
The run eventually succeeded (78 agents, all 65 pages scanned), but only after working
around a blocker, and it ran far more expensively than it needed to. Below are the
fixes worth making at the **module source** so the next install gets them for free.

---

## 1. BLOCKER — `args` arrives as a JSON *string*, not an object

**Symptom.** Invoking the workflow by name with a structured `args` object
(`Workflow({ name: 'vlt-lint-full', args: { pages, indexPath, conventionsPath } })`)
caused an immediate bail (0 agents, ~9ms):

```
{"error":"vlt-lint-full requires { pages:[{slug,path}], indexPath, conventionsPath }. ..."}
```

**Cause.** Inside the script, `args` was delivered as a **JSON-encoded string**, not the
object. So `const a = args || {}` left `a` a string, `Array.isArray(a.pages)` was `false`,
and the guard tripped. Confirmed from the run journal: `args type: str` (len 7393).

**Fix (ship in `vlt-lint-full.js`).** Parse defensively at the top:

```js
let a = args || {}
if (typeof a === 'string') { try { a = JSON.parse(a) } catch (e) { a = {} } }
```

This is harness-version-robust — works whether `args` arrives as an object or a string.
Without it, the workflow is unusable via the documented named-invocation path that the
`vlt-lint` SKILL itself uses.

**Related gotcha (doc, not code).** Resuming with `resumeFromRunId` but *without*
re-passing `args` nulls the args in the journal (the journal gets overwritten with
`args: null`), so the resumed run bails the same way. Worth a one-line caveat in the
skill/workflow docs: on resume, re-pass `args`.

---

## 2. COST — per-page scanners should default to a cheap model (~10x win)

**Observation.** The dominant cost is the per-page fan-out: ~65 of ~78 agents. That phase
is pure **structured extraction** against a strict JSON schema (links, sources count,
frontmatter validity, thin?, key-claims) — no deep reasoning. The whole run defaulted to
the main-loop model (Opus here: `defaultModel: claude-opus-4-8[1m]`, ~2.1M subagent tokens).

**Fix (ship in `vlt-lint-full.js`).** Add per-tier model overrides, configurable via args:

```js
const scanModel    = a.scanModel    || 'haiku'    // per-page extraction
const indexModel   = a.indexModel   || 'sonnet'   // index-drift pass
const clusterModel = a.clusterModel || 'sonnet'   // contradiction judgment
```

…and pass `model: scanModel` / `indexModel` / `clusterModel` on the respective `agent()`
calls. Also annotate `meta.phases[].model` so the cost intent is visible. The judgment-heavy
passes (index, contradiction clusters) keep a mid model; only the mechanical scan drops to
Haiku. Estimated order-of-magnitude saving on the dominant phase.

**Caveat to keep regardless of tier:** see §5 — keep the SKILL's deterministic re-verify
step, because per-page scanners (even on Opus) produced false positives.

---

## 3. CONVENTION DRIFT — the index pass still polices source counts the redesigned convention removed

The `wiki-index.md` convention was redesigned to make the index a **structural map** that
does **not** carry source counts or dates ("the validator does NOT police source counts in
the index — they are not there to police"). But `vlt-lint-full.js` still:

- declares `INDEX_SCAN.sourcecount_fixes` and asks for "a source-count that disagrees with
  the pinned definition",
- builds `index_sourcecount_fixes` into the returned report,
- and the index-drift agent prompt instructs it to compute `slug: N→M` count corrections.

This contradicts the current convention. It returned empty on this run (correct, because the
redesigned index has no counts), but the schema + prompt are now dead weight that could
produce spurious "fixes" against an older index. **Recommend:** strip source-count checking
from `INDEX_SCAN`, the prompt, and the report shape.

**Same drift in the SKILL.** `vlt-lint` SKILL.md still lists, under index-drift fixes,
"**correct source counts against the pinned definition**" and a `sources_vs_prose` /
`index_sourcecount_fixes` emphasis. Reconcile the SKILL text with the redesigned
`wiki-index.md` (validator obligations are now: rows resolve, no missing/dangling pages,
stubs well-formed, every page has a `summary:` ≤160 — *not* counts/dates).

---

## 4. NOISE — the near-duplicate heuristic over-fires badly on hub/entity clusters

The `shared outbound links >= 3` signal flagged **70 "near-duplicate" pairs** on this wiki,
**all false**. They were hub/entity co-citations within a cluster (every dog-training page
links the same training hubs; every finance page links the same portfolio hubs; every tea
page links the same production hub). The skill had to discard all 70 by hand.

The raw shared-link count is dominated by shared hub links, so cluster siblings always cross
the threshold. Suggested improvements (any one helps):

- Exclude links to the cluster's own hub before counting overlap.
- Use Jaccard similarity over link sets with a high threshold, not a raw count.
- Require shared-links **AND** a secondary signal (slug-stem match or title/topic similarity)
  before flagging.

As shipped, the `near_duplicates` output is noise at any non-trivial wiki size.

---

## 5. ACCURACY — move deterministic checks into the JS reduce; don't rely on per-page LLM judgment

Two findings classes were unreliable when left to per-page LLM scanners:

- **Inline-metadata rule-6 violation under-detected.** A `> *Last updated… | Sources: N*`
  body line (forbidden by frontmatter rule 6) was present on **all 65 pages**, but per-page
  scanners only flagged it on ~11. The systemic pattern was invisible one page at a time.
- **Summary length false positives.** Scanners reported summaries as over the 160-char limit
  that were well under it (e.g. one flagged at "~195" was actually 143) — likely
  em-dash/arrow glyph miscounting. (These came from **Opus**, so it's not a cheap-model
  artifact — it's an LLM-counting artifact.)

Both are **deterministic** checks. Recommend doing them in the JS reduce (free, exhaustive):

- rule-6 inline-metadata: grep each page body for `^>\s*\*?Last updated:` → report all hits.
- summary length: read frontmatter `summary:`, count chars, compare to 160.

This makes them exhaustive and removes a class of false positives the SKILL currently has to
re-verify by hand. (The SKILL *should* still re-verify, but it shouldn't have to.)

Related: **cross-layer wikilinks falsely reported as missing targets.** 14 of 17
`missing_targets` were valid `[[…]]` links to **research notes** that exist in
`_agent/research/` — the reduce only checks targets against the wiki `slugSet`. Consider
resolving link targets against the whole vault (or at least `{research}` basenames) before
declaring a target missing, or label cross-layer links distinctly rather than as "missing."

---

## 6. MINOR — contradiction-cluster cap sits just below the natural cluster count

Default `clusterCap = 12`; this 65-page wiki produced **13** link-adjacency clusters, so 1
cluster went unchecked for cross-page contradictions (correctly surfaced in `coverage_caps`).
The cap mechanic + reporting worked well; consider scaling the default with page count (or a
modestly higher default) so a mid-size wiki isn't capped on the very first run.

---

## What worked well (keep)

- The fan-out + JS-reduce split is the right shape; `files_checked` vs `files_listed` and
  `coverage_caps` reporting is honest and useful.
- Read-only finder + single-writer SKILL applying fixes serially — clean separation; no write
  contention.
- `contradictions_handled` (Gap B) is genuinely valuable: it surfaced 41 well-managed,
  already-documented disagreements instead of vanishing them. Keep this.
- The structured report shape consumed cleanly.

---

## Suggested priority for next version

1. **§1 args parse** — blocker; ship immediately.
2. **§2 model tiering** — big, easy cost win.
3. **§3 convention drift** — correctness vs the redesigned index convention (skill + workflow).
4. **§5 deterministic checks in JS** — accuracy + free exhaustiveness.
5. **§4 near-dup heuristic** — noise reduction.
6. **§6 cluster cap default** — minor.
