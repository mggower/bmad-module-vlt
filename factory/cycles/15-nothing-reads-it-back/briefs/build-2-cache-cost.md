---
title: 'Build #2 — what the instrument costs to run: after this ships, a vault owner who re-runs `vlt-lint --full` — after an upgrade, or because a finding looks wrong — pays for what actually changed instead of for everything, and can force a re-derivation instead of being served the same suspect answer'
status: 'BRIEFED 2026-09-02 — build via bmad-workflow-builder in a fresh session. The builder rewrites this line to a BUILT record: `BUILT <date> — <what landed>; <verification result>. Deviations/notes: (1) … (2) …` with numbered deliberate deviations (precedent: Cycle 14 build-5), deletes any `.decision-log.md`, one commit for the build. Not the release build — no version bump here (rides build-7 / v0.18.0). File-edit order across the cycle is 2 → 3 → 4 → 6 → 7: this build lands BEFORE build-3 on the three shared sites named in §Boundary with build-3.'
module_code: 'vlt'
created: '2026-09-02'
derives_from:
  - 'factory/inbox/2026-09-01-093000-the-findings-cache-cannot-survive-the-release-that-makes-it-needed.md (A15-9 — directions 2 and 1 as re-ruled whole by roundtable A3 / owner ruling D-B: the per-page key is facts-not-verdicts + the extractor identity; the companion finding is P-23, out of scope here)'
  - 'factory/inbox/2026-08-26-123151-lint-full-inline-args-payload-costs-the-caller-84kb.md (A15-11 — direction 1 only: the `scriptPath` route documented in `full-scale.md` step 3; direction 2 `argsPath` DECLINED by Q2; the `:127` wording observation ruled already-satisfied)'
  - 'factory/inbox/2026-09-01-140602-a-scanner-substituted-a-proper-noun-and-the-cache-made-it-permanent.md (A15-4 — direction 2''s INVALIDATION half only (D3): the eviction route end to end per roundtable A13; record provenance DEFERRED; the fidelity half is build-4''s under D-C; direction 3 stays refused)'
roadmap: 'factory/cycles/15-nothing-reads-it-back/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-09-01/02): Q3 as extended by A3/D-B (facts-not-verdicts + `scanModel`; `module_version` deleted, `checks_digest` out, `pin_vector` narrowed-or-dropped; the brief-time whole-file-or-reduce question DISSOLVED); Q2 (direction 1 only); Q2b (this build precedes build-4 — hard); D3 (eviction in, provenance deferred, direction 3 refused); D4 (invalidation never weakened on judgment — shown per slot in §Brief-time dispositions 1); D2 as amended (the `RULESET_SLOTS`-loop property); roundtable A2 (v0.18.0 cold by construction — cache clauses graded at rest), A4 (build-2 owns slot population, build-3 rendering/type; d1 as a workflow-side required-name set), A13 (the eviction route end to end), A20 (retire the "first full run after any release is COLD" statements); instrument-beat property (a)/(b)/(c) for build-2.'
risk: 'low-moderate — one workflow asset (`vlt-lint-full.js`) changes its cache-key composition and gains a required-name set, one shipped script gains a subcommand, three reference docs and the SKILL/help row move; NO handshaked convention moves (pins unchanged, `// depends_on:` header unchanged, PAGE_SCAN untouched — E5/E6 stay green); no consumer walk; the v0.18.0 first sweep is cold by construction regardless of this build, so the key change has no live observable on its own release (A2) and is proven at rest.'
specimens: '2/3 — observed: (i) the 2026-08-30 cold sweep''s `cost_accounting` row (146 agents / 591,152 prompt chars / 172 dispatches — A15-9), (ii) the composed-args manifest (146 pages / 146 hashes / 1,849 crossLayerSlugs / 6 stubs / ~84KB — A15-11), (iii) the `seattle-seahawks` cached record carrying `…-espn-top-10-cornerboxes-2026` for `cornerbacks`, served from the sidecar by a 1-agent sweep (A15-4). Preserved into this brief: (ii) — quoted into the `scriptPath` recipe as the sizes it exists for; (iii) — the eviction fixture''s poisoned record is that slug and that link, so the evict check runs against the class''s live shape. NOT preserved: (i) — no instrument in this build reads a cost row; the at-rest key fixture is synthetic by necessity (A2: the live release re-rolls every record before any check runs).'
---

# Build #2 — what the instrument costs to run

## Intent

The findings cache works — Cycle 14 build-2 repaired it and the field measured a 96% cut on the
scan phase (146 agents → 5) when it hits. Three filings say what it still costs. **A15-9:** its key
carries `module_version`, so every release invalidates every record, and the only sweep an
acceptance check ever forces is a post-release sweep — the instrument is cold by construction at
the one moment it is mandatory; and the key carries every convention *this run judges against* and
`checks_digest`, so a change the page scanner never reads invalidates page-scan facts twice over.
**A15-11:** the fan-out's ~84KB args payload transits the caller's context on every run and again
on every resume, and the route that avoids it (`scriptPath`) works today and is documented nowhere.
**A15-4:** a scanner substituted a proper noun, the cache faithfully preserved it, and the only
remedies were a release or deleting all 146 records — no proportionate remedy existed, and `lint-cache.py`
exposes `read` and `write` only.

This build makes the promise's four outcomes true, each with its own mechanism (roadmap build-2
bullet, the ⚠ paragraph — a brief shipping the cache work alone has not met the promise):

1. **Survive an upgrade that did not move the scan surface** (A15-9 d2, re-ruled D-B) — the
   ruleset half of the key is re-composed from *facts-not-verdicts*: the three scanner-read
   convention digests plus the extractor identity (`scanModel`). `module_version` is **deleted**
   (not replaced by prose-file digests — the reduce re-runs over cached facts every sweep, so a
   reduce or prose change is fully exercised with no cold sweep); `checks_digest` leaves the key;
   `pin_vector` is **dropped** as redundant with the digests (§Brief-time dispositions 1).
2. **Survive a convention change the scanner never reads** (A15-9 d1, A4) — the required
   convention set is one workflow-side constant shared by the scan prompt's `convRead` calls and
   `rulesetSlotsMissing`; a missing name is reported *by name*; names outside the set do not enter
   the key.
3. **Place no payload in the caller's context** (A15-11 d1, Q2) — `full-scale.md` step 3 documents
   the `scriptPath` wrapper route as the invocation at scale, with the resume implication.
4. **Force a re-derivation of one page** (A15-4 eviction half, D3 + A13) — `lint-cache.py evict`,
   reachable from two operator-facing routes (a `vlt-lint` intent before the sidecar read; the
   refused-finding response after the step-5 write), reported as `evicted E by request`.

And the retirement that comes with them (A20): the module stops saying *"the first full run after
any release is a COLD one"*, because after this build it is not — a run is cold when the scan surface,
the extractor, or a scanner-read convention moved, **and the cold reason names which**.

All rejected alternatives in the parent filings are settled — do not re-litigate: no `argsPath`
(Q2 — a Claude Code harness parameter the module cannot build and the lifecycle has no rail to
request); no model change for the scan phase (D3 — direction 3 refused); no whole-file digest of
`vlt-lint-full.js` / `SKILL.md` / `full-scale.md` (D-B — the brief-time question dissolved); no
per-record provenance (D3 — deferred, a data-model question no filing specifies); no weakening of
invalidation on judgment (D4 — a bound, shown per slot below); no factory-side check-anatomy work
(Q4 → P-23).

**The properties this build's acceptance protects** (roadmap §Instrument beat, stated without the
fix): *(a) a cached page-scan record is reused iff the page's bytes, the extractor, the scan prompt +
schema, and the three scanner-read conventions are byte-identical since it was written — whatever
else in the module moved; (b) one named page's record can be removed and the next sweep re-derives
exactly that page and says so; (c) invoking the sweep at scale places no page/hash/slug payload in
the caller's context on first run or resume.* The antecedent of (a) is false at v0.18.0 (build-7
moves `write-verification.md` and the `@5` literal inside `pageScanPrompt`), so (a) and (b) are
proven by at-rest fixtures, never by the upgrade sweep.

## Brief-time dispositions

Ideation left one question to brief time for this build and the roundtable **dissolved** it (D-B:
neither the whole file nor the reduce is digested). The dispositions below are the judgment calls
this headless run made inside the rulings' letter, each recorded so the builder does not re-decide
them.

### 1. D4 shown per slot — what leaves the key, what enters, and why each is safe

D4 is a bound: *"any repair must show the reused facts are **independent** of what moved."* A cached
record is a `PAGE_SCAN` return (`vlt-lint-full.js:158-189`): facts a scanner extracted from **one
page's bytes**, reading **exactly three conventions** (`:228-229`: `convRead('frontmatter')`,
`convRead('wiki-supersession')`, `convRead('write-verification')`), under **one prompt + schema**
(`scanFingerprint`, `:247-248`), by **one model** (`scanModel`, `:122`, `:357`). Nothing else the
module carries is an input to that return.

| Slot (today, `:262`) | Disposition | D4 argument |
|---|---|---|
| `module_version` | **DELETED** (D-B) | A version string is not an input to any scanner. What it proxied — a lint-surface change — either moves the prompt/schema (caught by `scanFingerprint`), a scanner-read convention (caught by its digest), or the reduce/prose (re-executed over cached facts every run, `:408-415`; no reuse of a verdict is possible because verdicts are never stored, `full-scale.md` step 5). |
| `checks_digest` | **OUT** (D-B) | `checks.md` is read by the SKILL and the reduce, never by a page scanner (`grep -n 'checks' vlt-lint-full.js` — no scanner prompt names it). It moves what the reduce concludes, and the reduce re-runs. |
| `pin_vector` | **DROPPED** — the "or drops as redundant" branch of D-B, ruled here | The three scanner-read pins ack conventions whose bytes are already digested (base + overlay). A convention's `version:` lives in its own file's frontmatter, so a rule change that bumps the version changes the digested bytes — the pin cannot move for a scanner-relevant reason without the digest moving. Conversely a **re-ack without a convention change** (a consumer bump alone) changes nothing a scanner reads — invalidating on it is the over-breadth A15-9 filed. Narrowing to three pins would keep a slot whose every true positive the digests already catch and whose only unique positives are false. *Consequence recorded for build-3's briefer:* A15-10's `pin_vector`-rendering half **dissolves** with the slot; the `convention_digests` "judges against" ambiguity is closed by disposition 2. |
| `convention_digests` | **NARROWED** to the required-name set (A4) | Only the three conventions the scanner reads are inputs; a fourth name in the map would re-widen invalidation (the A15-9 over-breadth) — names outside the set are **ignored for the key** and logged (disposition 2). |
| `scanModel` | **ENTERS** (D-B) — as a workflow-resolved term, see disposition 3 | The extractor is an input to every fact; today it is in no key term (`:296`), so a model change or a caller override would reuse haiku facts under a different extractor forever. |

An upgrade that moves the scan surface, the extractor, or a scanner-read convention still invalidates
every record — correctly. One that moves nothing a scanner reads leaves every record reusable — the
outcome the promise names.

### 2. The required-name set — one constant, three names, missing reported by name, extras ignored

`const SCANNER_CONVENTIONS = ['frontmatter', 'wiki-supersession', 'write-verification']` is declared
once, above `convRead` (`:223`). **Two consumers, no third statement:** `pageScanPrompt` builds its
read clause from it (`SCANNER_CONVENTIONS.map(convRead).join('; ')` — producing text byte-identical
to today's three literal calls, so this build alone does not move `scanFingerprint`); and
`rulesetSlotsMissing` requires `convention_digests` to carry each name with a non-empty string
digest, reporting **each missing name** (`convention_digests[write-verification]`), never the bare
slot. **Extra names** (a SKILL passing all nine, the Cycle 14 reading) are excluded from the canonical
string and named in one `log()` line — the run is not degraded, so this is not a `coverage_caps`
entry; a wrong-**type** digest (a number, an object) is build-3's rendering language (§Boundary) and
this build leaves the `typeof`/`length` test as it stands, applied per required name.

`full-scale.md` step 2's slot sentence is rewritten to match: *"`convention_digests`, a `{name:
digest}` map carrying **exactly the three conventions the page scanner reads — `frontmatter`,
`wiki-supersession`, `write-verification` — the set single-homed as `SCANNER_CONVENTIONS` in
`vlt-lint-full.js`**"*. The digest steps (instrument, merge order, encoding, truncation) are unchanged.

### 3. `scanModel` enters the key as the workflow-resolved value, not as a `rulesetComponents` slot

D2 (ii) assumed the new term would be a `RULESET_SLOTS` member. **Ruling:** it is not. The workflow
already resolves the effective extractor at `:122` (`a.scanModel || 'haiku'`); keying on a
SKILL-supplied slot would either force the SKILL to restate a default that lives in the workflow (a
second home — the A14-8 defect shape) or leave the default case with an empty slot and a permanently
cold cache. The canonical string becomes `[scanModel, ...pairs].join('|')` with `scanModel` the
resolved value, so the key names the extractor that actually ran. **Consequence for D2:** the loop
gains no new slot; `RULESET_SLOTS` after this build is `['convention_digests']`, and D2's loop
property applies to that one slot (build-3's). **One type guard rides here** because the value now
enters a key: `scanModel` must be a non-empty string — anything else is refused with the args-guard
error shape at `:126-128` (a model override that is not a string is a caller defect, and
`String([...])` would otherwise compose a junk term and dispatch anyway). This is not D2 (iii)'s
pre-dispatch-refusal posture for ruleset slots (build-3's); it is the existing args guard widened by
one predicate. Recorded in the roadmap at the build-2 bullet as a dated note against D2 (ii).

### 4. The cold reason names what moved — two attribution levels, each from the instrument that holds it

A20's replacement text is *"cold when the scan surface, the extractor, or a scanner-read convention
moved — and the cold reason names which."* The workflow holds the cached keys and this run's; the
SKILL holds this run's digests by name and the sidecar's recorded ones. **Ruling:** (i) the workflow
returns `cache_miss_terms: {page_bytes: N, scan_surface: N, ruleset: N}` — for each sidecar record
that failed `reusable()`, the **first** of the three `|`-separated key terms that differs (`:296`),
counted; (ii) the sidecar gains an **informational** `components` object beside its informational
`fingerprint` — `{scan_model, convention_digests}` as composed this run (returned by the workflow as
`cache_components`, stored by `write --components`, returned by `read`) — and the SKILL renders the
cold reason by **diffing names**: `cold (ruleset moved: write-verification; scan surface moved; …)`.
Neither addition is a source of any reuse decision — `lint-cache.py`'s docstring rule (`:31-34`)
stands verbatim and is extended to `components` in the same sentence. Page-bytes misses are churn,
not cold: the cold branch renders only when `files_cached` is 0 with `cache_records_read` > 0, and
names the non-page terms.

### 5. Eviction — one subcommand, two routes, and the order that makes the refusal route work

`lint-cache.py evict --vault-root R --slug S [--slug S…]` removes every record whose `slug` equals a
given slug **exactly** (records are keyed on the SKILL-supplied slug, `:433-435` — no normalization
here, so a slug that does not match is a loud miss, never a silent near-match), rewrites the sidecar
through the same atomic temp-and-replace path `write` uses, and emits
`{"evicted": K, "of": N, "missing": [slugs not found], "path": …}` plus a stderr line
`evicted K of N`. **K = 0 exits non-zero** (a missing sidecar is `evicted 0 of 0`, also non-zero) —
A13's "loud non-zero"; `read`'s exit-0-on-missing rule is untouched (a cold run is not an error; an
eviction that evicted nothing is).

**Route A — on request, before the sidecar read** (A13's step): the `vlt-lint` intent *"full lint,
re-scan <slug>"* runs `evict` for the named slug(s) as the **first act of `full-scale.md` step 2**, so
this run's `cachedScans` no longer carries them and the workflow's own `toScan` (`:306-308`) re-scans
exactly those pages.

**Route B — a refused finding, after the step-5 cache write** (A13's legal response, sequenced
correctly): step 5 rewrites the sidecar **whole** from the workflow's `cache_records`, which include
the reused (poisoned) record — so an evict before that write is written straight back, which is the
very observation A13 made about D3's callerless subcommand. *Grounding refinement, recorded in the
roadmap:* the refusal evict runs **after** the step-5 `write` and **before** Step 6 persists the
report, so the **next** sweep re-derives the page. The response is stated once, in `full-scale.md`
step 5's cache paragraph: *"a `fix_now` / `flag_for_human` entry the operator refuses as false evicts
its page's record (`evict --slug`) after this write and before the report persists — a refused
finding served from the cache would otherwise be re-served on every sweep (refuse → re-serve →
refuse)."* `fix-and-file.md` step 3 carries a one-line pointer to it, never the mechanic. The
report's `lint_cache:` line renders `evicted E by request` on both branches, E the count across both
routes this run (0 rendered, never omitted — the `rejected R` idiom, `report.md:89`).

**Hand-deleting the sidecar** stays legal and stays true (*"deleting it is always safe and costs only
a cold run"*, step 5) and becomes the **second** remedy, named after eviction.

### 6. The `scriptPath` route — recipe, location, and what "no payload in context" requires

`full-scale.md` step 3 gains the route as **the invocation at scale**: the SKILL derives the args
object (step 1's spec is unchanged) **by an executable it runs** — a script with filesystem access
whose output is the wrapper file, not the payload — writes a thin wrapper workflow embedding it,
and invokes `Workflow({scriptPath: <wrapper>})`; on resume it passes `resumeFromRunId` **with the same
`scriptPath`**, and the re-pass-the-full-args sentence becomes the fallback for inline invocation
only. The recipe carries the filing's wrapper shape verbatim (`export const meta = …; const LINT_ARGS
= {…}; return await workflow('vlt-lint-full', LINT_ARGS)`) and the measured sizes it exists for
(146 / 146 / 1,849 / 6 entries, ~84KB). **Location:** a scratch path **outside the vault** (`mktemp
-d`), removed after the run completes — outside every enumeration by construction (R4, §Verification
8). The `:89-90` parse-on-intake already covers `scriptPath` invocation (`:85-86` says so) — no
workflow edit for this outcome. **Why "by an executable"**: an agent that composes 1,849 slugs
in-context and then writes them to disk has already paid the cost; the filing's own workaround
("build the args object with a script that has filesystem access") is the route, and the recipe
says so. A *shipped* discovery executable is not this build's — build-4 (A12) ships the executable
sibling of `lint-cache.py` that derives `pageLinks`, and it is the natural home for the whole
derivation; this brief records that as the follow-on, not as scope (Q2: a documentation edit).
The `ST-7` caveat the capture attached (a prose recipe is one more derivation nobody reads back)
is accepted knowingly, per D2's *not extended there* — and is exactly why the recipe is
executable-shaped rather than a description.

`vlt-lint-full.js:127`'s no-args refusal is **not edited** — Q2 ruled the pointer already present.

### 7. Interim posture (R1) — not applicable

Every response this build states ships with its mechanism in the same build: the refusal response
with `evict`; the required-name set with its enforcement in `rulesetSlotsMissing`; the cold-reason
text with `cache_miss_terms` + `components`. The one report slot named beside this work that does
**not** ship here — `false_positives_refused:` promoted into `report.md` — is build-5's (A16) and
lands in the same release, so no vault sees a window.

### 8. Retirement clause (P-15 / A20) — substantive

The obsolescence beat ruled for this build, re-checked at brief time by grep (`grep -rn -i 'cold'
skills/vlt-lint skills/vlt-setup/assets/workflows`). Every restatement, with its disposition:

| Site | Text | Disposition |
|---|---|---|
| `full-scale.md` step 2 (`:8`), last two sentences | *"This release is its own worked instance three times over: `module_version` 0.15.0 → 0.16.0 … `extraction` 6 → 7 … `decision-log` 3 → 4. State it plainly: the first full run after any release is a COLD one — stated up front, never discovered."* | **RETIRED** — replaced by: *"A run is cold when the scan surface (`scanFingerprint`), the extractor (`scanModel`), or a scanner-read convention's merged bytes moved since the sidecar was written — and the `lint_cache:` cold reason names which. A release that moves none of these leaves every record reusable."* The worked instance is history and goes with it. |
| `full-scale.md` step 2, the four-slot sentence + *"Any of those moving invalidates every record, because each of them changes what a finding means"* | | **RETIRED** — the slot list becomes the one slot + its required names (disposition 2); the sentence becomes *"a scanner-read convention moving invalidates every record, because it changes what a scanner returned; nothing else the SKILL passes does"*. |
| `full-scale.md` step 5, *"deleting it is always safe and costs only a cold run"* | | **SURVIVES** — true; demoted to the second remedy after `evict` (disposition 5). |
| `report.md:89`, *"so the first full run after an upgrade is a stated cold run rather than a discovered one"* + the three-item reason list *"(no prior cache; fingerprint changed; sidecar unreadable)"* | | **RETIRED** (the echo) — the sentence becomes *"a cold run says so and names which key term moved (scan surface / extractor / a named scanner-read convention), or that no prior cache existed or the sidecar was unreadable"*. ⚠ Build-3 (A14 v) adds a **fourth** reason to the same list (*slot rendered with the wrong type*) — this build rewrites the list's frame, build-3 appends its member (§Boundary). |
| `vlt-lint-full.js:58` `module_version: string` row; `:59` `pin_vector`; `:63` `checks_digest`; the `:256-257` canonical-order comment; `:262` `RULESET_SLOTS`; `:279` canonical | | **RETIRED** — the arg contract lists one slot; the comment and the canonical name the new order (`scanModel`, then `name=digest` pairs sorted). |
| `vlt-lint/SKILL.md:74`, *"deleting it costs only a cold run"* | | **SURVIVES unchanged** — a pointer to `full-scale.md`; still true. |
| `vault-operating-contract.md:325` Decay row, *"safely deletable (the next run goes cold)"* | | **SURVIVES unchanged** — true, and touching the contract would owe a rule-card re-derivation (C6) for no rule change. |
| `CHANGELOG.md` v0.17.x / v0.16.x entries, *"COLD BY CONSTRUCTION"* | | **HISTORY** — never edited; the v0.18.0 entry states its own cold run (§Release). |

**The population statements that must NOT move** (R2's third element): D4's bound, verbatim in
`full-scale.md` step 2's replacement text (*a record reused under a moved rule is a false clean*);
the standing mandate *"a missing, unparseable or schema-mismatched sidecar is a cold run, stated in
the report — never an error and never a silent full sweep presented as a cached one"* (`:298-303`,
step 2); and the facts-never-verdicts rule (step 5) — the reason `module_version` can go.

### 9. The A15-9 companion finding is not here

Q4 routed it to the platform ledger as **P-23**; the roadmap's A15-9 entry carries the forward
pointer. This brief adds nothing to `build-brief`'s check anatomy.

## Boundary with build-3 — stated so build-3's briefer inherits it (A4)

Three sites are shared; **build-2 lands first and owns slot POPULATION; build-3 owns RENDERING and
TYPE language only.**

| Shared site | Build-2 (this brief) owns | Build-3 owns |
|---|---|---|
| `vlt-lint-full.js:56-69` arg contract (roadmap `:55-66`) | **which** `rulesetComponents` slots exist (one: `convention_digests`), the required-name set, `scanModel`'s key role | the per-slot wording of what a *wrong type* is |
| `vlt-lint-full.js:262-282` `RULESET_SLOTS` / `rulesetSlotsMissing` / `composeRulesetFingerprint` (roadmap `:262-271`) | `RULESET_SLOTS` membership; `SCANNER_CONVENTIONS`; missing-by-name; extras ignored; the canonical string | the present-but-wrong-type branch reported as *wrong*, never *missing* (D2 ii), and its **pre-dispatch refusal** posture (D2 iii) replacing the `:322` cold cap |
| `full-scale.md` step 2 (`:8`) | the slot list, the required names, the digest steps (unchanged), the retirement text, the evict step | *"any slot missing or empty"* → three-way absent / empty / wrong-type (A20, build-3) |
| `report.md:78` + `:89` (`lint_cache:`) | the `evicted E by request` term; the cold-reason **frame** naming the moved term | the fourth cold reason *slot rendered with the wrong type: <slot>* (A14 v); merge order on `report.md` is **2 → 3 → 5** |

Build-3's briefer should read disposition 1's `pin_vector` row (its A15-10 half dissolves) and
disposition 3 (the loop has one slot; `scanModel` is not in it).

## F-sites

Every `file:line` below was re-derived against the working tree at brief time (branch
`cycle15-v0.18.0`, tip `0e01381`). Grounding outcome per site is marked. A concurrent build-1
builder is editing `.github/`, `skills/vlt-feedback/`, `.claude/skills/issue-triage/`,
`.claude/skills/inbox-capture/`, `factory/inbox/README.md` — none of these sites.

### F1 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the key, the required-name set, the miss attribution (HOLDS, two ranges widened)

1. **`:56-69` — the `rulesetComponents` arg contract** *(grounding: the roadmap's `:55-66` is the
   block at `:56-69`; HOLDS)*. Replace the four slot rows with one: `convention_digests: {name: digest}
   — merged (base + overlay) digest for EACH name in SCANNER_CONVENTIONS (the three conventions the
   page scanner reads); names outside the set are ignored for the key and logged; ORDER DOES NOT
   MATTER`. Keep the "SKILL computes, this script composes" sentences; replace *"naming the absent
   slots"* with *"naming each absent required name"*. Add to the `scanModel` row (`:77`): *"— enters
   the per-page cache key as the extractor identity; must be a non-empty string"*.
2. **`:16-21` — the R4 fan-out-currency header comment.** *"adds that convention to convRead AND to
   the pins above"* → *"adds that convention to `SCANNER_CONVENTIONS` (which feeds convRead and the
   cache key) AND to the pins above"* — the constant is now the read list's single home.
3. **`:122` — `scanModel` resolution.** Add the type guard (disposition 3): a present non-string or
   empty `scanModel` returns the `:126-128` error shape with a message naming it. Keep the default.
4. **New constant above `:223`:** `const SCANNER_CONVENTIONS = ['frontmatter', 'wiki-supersession',
   'write-verification']` with a comment naming both consumers and A4. **`:229`** — replace the three
   literal `convRead(...)` calls with `${SCANNER_CONVENTIONS.map(convRead).join('; ')}` producing
   **byte-identical** prompt text (verify: `canonicalScan` unchanged → `scanFingerprint` unchanged
   by this build; build-7 moves it later). ⚠ **`PAGE_SCAN` is not touched** — E6 stays at 3676/3700
   (A11's hard constraint, `tools/package-lint.py:966`).
5. **`:250-261` comment + `:262-282`** *(grounding: the roadmap's `:262-271` omits the compose
   function `:275-281`, whose `:279` canonical joins the deleted slots — widened)*. `RULESET_SLOTS =
   ['convention_digests']`. `rulesetSlotsMissing` becomes a list of **missing required names** (each
   `convention_digests[<name>]` absent or not a non-empty string), computed over `SCANNER_CONVENTIONS`;
   the object-shape test (`!v || typeof v !== 'object' || Array.isArray(v)`) stays and reports the
   slot itself when the map is absent. `composeRulesetFingerprint` builds pairs **only** from
   `SCANNER_CONVENTIONS` (sorted), logs any extra names once, and joins `[scanModel, ...pairs]`. Rewrite
   the comment's canonical-order sentence accordingly; keep the fnv1a construction and the
   "algorithm here, inputs there" paragraph.
6. **`:322` cap text** — *only* the interpolation changes to the by-name list (the wording *"absent or
   empty slots"* is build-3's to re-frame — do not pre-empt A20/build-3 here).
7. **`:296-309` — miss attribution** (disposition 4). Beside `reusable`, compute `cacheMissTerms`
   from each `cacheBySlug` record whose key ≠ `runKey(slug)`: split both on `|` and count the first
   differing index as `page_bytes` / `scan_surface` / `ruleset`. Return it at `:873-881` as
   `cache_miss_terms`, and return `cache_components: { scan_model: scanModel, convention_digests:
   <the three pairs as an object> }` (a fact, never a reuse source). Update the `:291-295` comment
   ("three terms unchanged in shape") — still true; the ruleset term's inputs changed.
8. **`:433-441` comment** — unchanged in substance; keep *"a cold run with no components rewrites the
   sidecar with records: []"* (still true).

**Why:** outcomes 1, 2 and the cold-reason half of the retirement live here; this file is the single
home of the composition (A14-8), which is why the required-name set is a constant and not a
sentence.

### F2 — `skills/vlt-lint/scripts/lint-cache.py` — the `evict` subcommand + `components` (HOLDS: `read`/`write` only at `:140-154`)

- **`cmd_evict(args)`** (disposition 5): load the sidecar as `cmd_read` does; on missing/unparseable
  emit `{"evicted": 0, "of": 0, "missing": [...], "reason": …}` and **return 1**; else filter
  `records` by exact `slug` match against the `--slug` set, rewrite via the same atomic path (factor
  the temp-and-replace block out of `cmd_write` into `_atomic_write(agent, sidecar, payload)` and
  reuse it — one writer, not two), preserving `fingerprint`, `written`, and `components`; emit
  `{"evicted": K, "of": N, "missing": [...], "path": …}` and print `evicted K of N` to stderr; **return
  1 when K == 0**, else 0.
- **`write`** gains `--components <path|->` (optional; a JSON object, stored as `components`);
  **`read`** returns `components` beside `fingerprint`/`written`.
- **Docstring** (`:15-17`, `:31-34`): three callers now (step 2 `read`, step 2/5 `evict`, step 5
  `write`); extend the informational-only sentence to `components`: *"The top-level `fingerprint` and
  `components` are INFORMATIONAL ONLY … `components` exists so the SKILL can name which term moved on
  a cold run."* The exit-code paragraph (`:36-38`) gains: *"`evict` exits non-zero when it evicted
  nothing — an eviction that removed no record is the one outcome the operator must not mistake for
  success."*
- **`main`**: register `evict` (`--vault-root`, `--slug` `action='append'`, `required=True`).

**Why:** outcome 4's mechanism. **Out of scope here:** an `--all` flag (hand-delete is the second
remedy and needs no subcommand); any record-schema validation (the docstring's single-home rule).

### F3 — `skills/vlt-lint/references/full-scale.md` — steps 2, 3, 5 (HOLDS: step 2 `:8`, step 3 `:9`, step 5 cache paragraph `:12`)

- **Step 2, opening** — insert the **evict step first** (Route A): *"If this run was asked to
  re-scan named pages (`full lint, re-scan <slug>`), first run `uv run --quiet "$SKILL/scripts/lint-cache.py"
  evict --vault-root {project-root} --slug <slug> [--slug …]` — it prints `evicted K of N` and exits
  non-zero when K is 0 (a slug that matched no record; say so, do not proceed as if it had). Then read
  the sidecar…"*. The `read` sentence gains `components` to its returned-fields list.
- **Step 2, the slot sentence** → disposition 2's text; **the digest-steps sentence is unchanged**;
  the closing sentence → disposition 8's replacement text (the retirement), including the by-name
  cold reason and a pointer that the workflow returns `cache_miss_terms` for the term level.
- **Step 3** → disposition 6: the `scriptPath` route as the invocation at scale (recipe, sizes,
  location, resume with the same `scriptPath`); the existing `workflow('vlt-lint-full', {…})` call
  stays as the inline form for small sweeps, and the *"On resume … re-pass the full args object"*
  sentence is scoped to it.
- **Step 5, the cache paragraph** → Route B's response text (disposition 5) after the `write`
  sentence, the `--components <cache_components>` argument added to the `write` invocation, and
  *"deleting it is always safe…"* re-worded as the second remedy: *"— and, for one page, `evict
  --slug` is the proportionate remedy; deleting the file whole stays safe and costs only a cold run."*
  The `lint_cache:` composition sentence adds `evicted E by request` (E = this run's evictions across
  both routes) and the cold-reason diff (`components` from `read` vs `cache_components` from the
  return).

**Why:** outcomes 3 and 4, the retirement's home, and the single home of every cache mechanic —
every other site points here.

### F4 — `skills/vlt-lint/references/report.md:78` + `:89` — the `lint_cache:` line (HOLDS)

- **`:78`** — both branches gain `, evicted E by request` after the `rejected R of P records read`
  term; the cold branch's `<reason>` placeholder becomes `<reason — names the moved term(s)>`.
- **`:89`** — disposition 8's replacement of the echo sentence and the parenthetical reason list's
  frame; the `rejected` semantics paragraph unchanged; add one sentence: *"`evicted E by request` is
  rendered on both branches and never omitted, including zero."*

**Why:** the report is where the promise's *"can force a re-derivation"* becomes visible. Build-3
appends its fourth reason and build-5's validator reads the line after both — merge order 2 → 3 → 5.

### F5 — `skills/vlt-lint/references/fix-and-file.md` step 3 (HOLDS; grounding addition — the refusal has no home today)

After the auto-fix list (`:7-14`), one pointer sentence: *"**A finding you refuse as false** (a
`fix_now` entry whose target exists, a `missing_targets` slug the page's own bytes do not carry) is
not applied and is **evicted from the findings cache** so the next sweep re-derives it — the
mechanic and its sequencing live at `references/full-scale.md` step 5."* A pointer, not a mechanic.

### F6 — `skills/vlt-lint/SKILL.md:3` + `:39` — the intent (HOLDS)

- **`:3` description**: after `'full lint' / '--full' sweeps everything` add `; 'full lint, re-scan
  <slug>' first evicts that page's cached facts so the sweep re-derives it`.
- **`:39` Full paragraph**: one sentence: *"`full lint, re-scan <slug>` (one or more slugs) is full
  mode with those pages evicted from the findings cache before the sidecar read — the mechanic is
  `references/full-scale.md` step 2."*
- `:74` unchanged (disposition 8).

### F7 — `skills/vlt-setup/assets/module-help.csv:10` — the help row (HOLDS)

`args` field `"{--full: sweep everything (default is since last lint)}"` → `"{--full: sweep everything
(default is since last lint)}|{re-scan <slug>: with --full, evict the page's cached facts first}"`.
Keep every free-text field quoted (package-lint Group B).

### F8 — `factory/cycles/15-nothing-reads-it-back/fixtures/` — two fixtures + one harness (NEW; factory-side, un-enumerated)

- `build-2-sidecar.json` — a sidecar of **three** records in the shipped shape (`{slug, key, scan}`),
  one of them `seattle-seahawks` whose `scan.outbound_links` carries
  `_agent/research/2026-07-26-112444-espn-top-10-cornerboxes-2026` (specimen (iii), the class's live
  shape); keys composed by the harness below so they match its "unchanged" case.
- `build-2-key-harness.mjs` — loads `vlt-lint-full.js`, rewrites `export const meta` to `const meta`,
  wraps the body in an `AsyncFunction` with the runtime globals stubbed (`args`, `agent` → `null`,
  `parallel` → `Promise.all`, `phase`/`log` → no-ops, `budget` → `{total: 0}`, `workflow` unused) —
  the same node-over-the-file approach `package-lint` E6 uses — and runs the case table in
  §Acceptance (1) and (2). The stub is **never on the path the checks observe**: a fully-reused case
  dispatches no agent (`toScan` empty, `:390` guard skipped); a not-reused case dispatches the null
  stub, which the workflow reports as `agent_failed` — the honest observable that exactly those slugs
  were re-scanned.
- `build-2-wrapper-example.js` — the step-3 recipe's wrapper with a two-page payload; `node --check`
  exits 0.

## Registration

**None.** No new skill, no new workflow, no new package-lint check (E4 untouched). **No handshake
owed:** no `governance/_meta` convention moves; `vlt-lint/SKILL.md:4` pins unchanged; the workflow's
`// depends_on:` header (`:11`) unchanged — E5 and E7 stay green; **E6 unchanged** (`PAGE_SCAN` not
edited). The `module-help.csv:10` row edit is a Group B concern, not a registration. The contract is
not touched (no C6 cost).

## Out of scope (dispositioned)

- **Per-record provenance** (which run / model call produced a record) — D3 deferred it; the
  informational `components` object is sidecar-level, not per-record, and does not pre-empt the
  design.
- **`argsPath` / any runtime parameter** — Q2 declined; no spike owed.
- **A shipped discovery executable for the args payload** — build-4's sibling script (A12) is its
  natural home; recorded as the follow-on in disposition 6.
- **Moving the scan phase off haiku** — D3, direction 3 refused; `scanModel` entering the key is the
  opposite move: the model can change and the cache stays honest.
- **Build-3's rendering/type language** on the shared sites — §Boundary.
- **`false_positives_refused:` as a mandated report slot** — build-5 (A16); the eviction response
  here is the mechanic that slot will count.
- **`vlt-lint-full.js:127` wording** — Q2 ruled the pointer present.
- **P-23** (a check names the population it judges) — platform ledger.
- **The contract's Decay row `:325`** — true as written; a C6 re-derivation for no rule change is not
  paid.

## Verification (unit, at rest — lifecycle step 5)

1. **Key fixture (P-18 — built from the failure's shape):** run `build-2-key-harness.mjs` over the
   cases in §Acceptance (1); record the per-case `files_cached` / `agent_failed` / `cache_miss_terms`
   table in the BUILT `status:`.
2. **Prompt-text invariance:** before and after F1 edit 4, print `scanFingerprint` from the harness —
   **equal** (this build moves no scan surface; build-7 will).
3. **Required-name set is single-homed:** `grep -n "convRead('" vlt-lint-full.js` → 0 hits; `grep -c
   SCANNER_CONVENTIONS` ≥ 3 (declaration, prompt, slot loop); `grep -n 'module_version\|checks_digest\|pin_vector'
   skills/vlt-lint skills/vlt-setup/assets/workflows/vlt-lint-full.js` → 0 hits (the CHANGELOG is
   history and excluded).
4. **Eviction fixture:** copy `build-2-sidecar.json` to a temp vault's `_agent/lint-cache.json`;
   `evict --slug seattle-seahawks` → stdout `evicted: 1, of: 3`, exit 0; `read` → `count: 2`,
   `components` present; `evict --slug not-a-page` → `evicted: 0`, exit 1; `evict` on a vault with no
   sidecar → `0 of 0`, exit 1; then the harness "unchanged inputs" case over the evicted sidecar →
   `agent_failed: ['seattle-seahawks']` exactly, `files_cached: 2`.
5. **Retirement grep:** `grep -rn -i 'first full run after any release\|COLD one\|worked instance three times' skills/` → 0
   hits; `grep -n 'evicted E by request' skills/vlt-lint/references/report.md` → both branches.
6. **Wrapper recipe:** `node --check fixtures/build-2-wrapper-example.js` exits 0; the recipe text in
   `full-scale.md` step 3 and the fixture agree on the three elements (embed, `scriptPath`, resume
   with the same `scriptPath`).
7. **Package lint** — `uv run tools/package-lint.py` Groups **A/B/C/E** PASS (B: the csv row; E5/E6/E7:
   the workflow header and schema budget unchanged — E6 must still read 3676). D / `--expect-version`
   is build-7's. **Handshake:** nothing moved; Group E is the check of record.
8. **R4 (enumeration widening):** no shipped file is added (`evict` is a subcommand of an existing
   script; the sidecar gains a key, not a file); the runtime wrapper lives outside the vault by the
   recipe; fixtures live in the un-enumerated cycle `fixtures/` dir. `R4: not applicable — declared
   exclusion, reasoning above.`
9. **R3 (legal response):** no finding class is added or changed. The refusal response homes at
   `full-scale.md` step 5 (the cache mechanics' single home) with a pointer from `fix-and-file.md`.
   `R3: not applicable (no finding class); the response is single-homed.`
10. **Scrub** — no vault-local paths or personal content in any shipped edit; the recipe uses
    placeholder paths; the fixture's `seattle-seahawks` record carries a slug and a research-note
    slug already on the public roadmap, nothing else.
11. **Cleanup** — no `.decision-log.md` left in the tree; the temp vault from step 4 removed.

## Release

Not the release build — v0.18.0's bump, `--expect-version 0.18.0` gate and tag ride build-7. **Two
release-time obligations this brief hands to build-7's briefer and `vlt-release`:**

1. **The v0.18.0 CHANGELOG states the cold run** (A2): *the first full lint after this release is
   COLD BY CONSTRUCTION — build-7 moved `write-verification.md` (a scanner-read convention) and the
   `@5` literal inside the scan prompt; the `lint_cache:` line will name both* — so
   `acceptance-discharge` never reads it as a build-2 FAIL. And, in the same entry, **why it is the
   last such statement**: from v0.18.0 the key is facts-not-verdicts, and a release that moves no
   scanner-read convention, no scan surface and no extractor leaves the cache warm (the build-2
   `title:` is collected there verbatim).
2. **The CHANGELOG's recurring "COLD BY CONSTRUCTION" paragraph is not a template** — after this
   release it appears only when a release actually moves one of the three named inputs, and it names
   which.

## Acceptance (live — appended to the roadmap ledger)

**Six checks — five `[ship-verifiable]` (GATE), one `[field-contingent]`.** `specimens: 2/3`.

**(1) `[ship-verifiable]` — at rest — GATES.** *The per-page key is facts-not-verdicts.* **Instrument:**
`fixtures/build-2-key-harness.mjs` over a two-page fixture whose sidecar was written under baseline
inputs; cases (each observed as `files_cached` and `agent_failed`): (a) identical inputs → 2 cached;
(b) an extra `module_version` slot passed with a different value → 2 cached (the term no longer
exists; extras ignored); (c) a fourth convention (`extraction`) added to `convention_digests` with a
new digest → 2 cached, one log line naming the ignored name; (d) `wiki-supersession`'s digest changed
→ 0 cached, `cache_miss_terms.ruleset: 2`; (e) `scanModel: 'sonnet'` → 0 cached, `ruleset: 2`;
(f) one byte of `PAGE_SCAN` changed in a copy of the workflow → 0 cached, `scan_surface: 2`;
(g) `convention_digests` missing `write-verification` → cold, the cap names
`convention_digests[write-verification]`. **Adversary:** property — *a record is reused iff its page
bytes, extractor, scan surface and the three scanner-read conventions are unchanged, whatever else
moved*; passing-violating state — the harness passes because the fixture's keys were composed by the
same code under test (a key that ignored `scanModel` entirely would still satisfy (a)–(d)). **Widened:**
the instrument is proven failable against the pre-build workflow (the Cycle 14 build-1 (2) standard):
the builder runs the harness against `git show 0e01381:…/vlt-lint-full.js` with the four legacy slots
supplied and records that there case (b) goes **cold** (the over-breadth A15-9 filed) and case (e) stays
**warm** (the extractor not in the key — the defect D-B named), while after the build (b) is warm and
(e) is cold — two cases that flip between the builds, so a harness that could not tell them apart
would be visible.

**(2) `[ship-verifiable]` — at rest — GATES.** *One named page's record can be removed and the next
sweep re-derives exactly that page and says so.* **Instrument:** Verification 4 — `evict` over
`fixtures/build-2-sidecar.json` (three records, the `seattle-seahawks` / `cornerboxes` specimen among
them): `evicted 1 of 3`, `read` → 2, the identical-input harness run dispatches exactly
`['seattle-seahawks']`; unknown slug → `evicted 0 of 3` exit 1; no sidecar → `0 of 0` exit 1.
**Adversary:** property — *the removal survives to the next sweep and is reported*; passing-violating
state — the subcommand works but the documented refusal route runs it **before** step 5's whole-file
`write`, which writes the record straight back (A13's own observation). **Widened:** a reader check on
`full-scale.md` step 5 asserts the refusal evict is sequenced **after** the `write` sentence and before
Step 6, and `report.md:78` carries `evicted E by request` on both branches — a stale "before the read"
placement of the refusal route is a FAIL.

**(3) `[ship-verifiable]` — at rest — GATES.** *The required convention set has one home and the
retired statements are gone.* **Instrument:** Verification 3 + 5 grep manifests, recorded in the BUILT
`status:`; plus `scanFingerprint` equality before/after (Verification 2). **Adversary:** property —
*every site that names what the scanner reads agrees, and no shipped text still promises a cold run
per release*; passing-violating state — the constant exists and both consumers use it, but
`full-scale.md` step 2 still tells the SKILL *"one entry per convention this run judges against"*, so a
conformant SKILL passes nine names and the workflow silently keys on three (correct) while the doc
describes a different population (the A14-8 shape). **Widened:** the manifest greps `full-scale.md` for
the retired phrase *"judges against"* in the slot sentence and requires the three names to appear
there verbatim.

**(4) `[ship-verifiable]` — on the v0.18.0 upgrade sweep (bounded: it happens anyway) — GATES.** *The
cold run says why, by name.* **Instrument:** the first full-mode report persisted after the
`{field-vault}` 0.18.0 upgrade: `lint_cache:` renders `cold (…)` naming `write-verification` and
`scan surface` (build-7's movers) and `evicted 0 by request`; the v0.18.0 CHANGELOG entry states the
cold run and its cause (§Release). **Adversary:** property — *a cold run is attributed, never merely
announced*; passing-violating state — the line reads `cold (fingerprint changed)` (the retired
three-reason idiom rendered by a SKILL following stale prose) — caught: the check requires the named
term. No further passing-violating state found.

**(5) `[ship-verifiable]` — on the v0.18.0 upgrade sweep — GATES.** *Invoking at scale places no
payload in the caller's context.* **Instrument:** the same sweep is invoked per `full-scale.md` step 3:
the evidence is the session's `Workflow` call carrying `scriptPath` (not `args`), the wrapper produced
by a tool call whose output is a path, and — if the run resumed — the resume call carrying
`resumeFromRunId` + the same `scriptPath` with no args. **Adversary:** property — *the ~84KB never
transits the context on first run or resume*; passing-violating state — the SKILL follows the recipe
but composes the 1,849-slug array in-context first and then writes it (the payload paid before the
wrapper exists). **Widened:** the check asserts the wrapper was **written by a script run** (the
recipe's own requirement), not by an agent authoring the file from values it holds — the tool-call
record is the instrument.

**(6) `[field-contingent]`** — *the cache stays warm across a release that moves nothing a scanner
reads.* **Event:** the first release after v0.18.0 whose diff touches none of `frontmatter.md`,
`wiki-supersession.md`, `write-verification.md` (base or overlay bytes), `pageScanPrompt`/`PAGE_SCAN`,
or the scan model default. **Performer:** the owner, on `{field-vault}` (readable from the factory
machine), running the ordinary post-upgrade full sweep. **Grades:** `lint_cache: scanned N / cached M`
with `M ≥ files_listed − churn_since_last_full`, `cost_accounting` scan-phase agents = the churned
pages only, `files_cached > 0`. Unbounded by construction (nothing in this cycle schedules such a
release — `factory/cycles/` shows every release to date moved a scanner-read convention); routes to
the standing watch register at closeout if unfired.
