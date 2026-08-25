---
title: 'Build #2 — the change-keyed findings cache (full lint stops re-judging pages nothing changed, and says how many it reused and under which ruleset)'
status: 'BUILT 2026-08-25 — the change-keyed findings cache landed whole across all seven F-sites, and the cycle''s release build is staged but **NOT tagged**. `vlt-lint-full.js` gained three optional cache args, a page-independent `scanFingerprint` over the invariant prompt + `PAGE_SCAN`, the composite per-page key, a `toScan`/`reused` split of the fan-out, both guards re-anchored to the dispatched population, and three new return keys (`files_cached`, `cache_fingerprint`, `fresh_scans`); `full-scale.md` gained the digest pass, a new step 2 (the sidecar + fingerprint, its single home), the narrowed B10-12 predicate and the write-back sub-bullet; `report.md` gained `lint_cache:`, `files_cached:` and the reporting paragraph; `vlt-lint/SKILL.md` gained the Step-6 pointer; the contract gained the exempt Decay row and `vault-rule-card.md` was re-derived to `sha256:265922bb…` (7,106 B); `CHANGELOG.md` gained the v0.16.0 entry with all four rule-change facts; both version strings read `0.16.0`. **Verification (real runs, not adjectives):** two-run fixture — run 1 `files_checked 6 / files_cached 0 / listed 6`, 6 agents, sidecar written with 6 records; run 2 (one page''s bytes edited) `files_checked 1 / files_cached 5`, **exactly one** agent dispatched (`delta`), same `cache_fingerprint`, reduce still correct over all six (`missing_targets ["delta → nowhere-page"]`, `orphans ["delta","epsilon","zeta"]`). Findings parity cold vs fully-cached — `/usr/bin/diff` (unwrapped) over the two `fix_now`/`flag_for_human`/`opportunities` blocks exited **0**, both files `sha256:45cc87b1e3b4…`; the fully-cached run dispatched **0** agents against a fan-out stubbed to throw. All four fingerprint mutations forced a cold run (`files_checked 6 / files_cached 0` each): `module_version` 0.15.0↔0.16.0 (fp `5a09279477…`), `extraction` 7→6 (`92799020d9…`), `decision-log` 4→3 (`45908a6778…`), one character of `pageScanPrompt` (scanFp `ce33db26a72c8e3e16ed` → `79890b0f08bd686716ed`). B10-12: refuses a stale-copy sim (`status failed`, 0/0), does **not** refuse a fully-cached run, and **does** refuse a half-cached run whose fan-out all died (`0/3` dispatched — the case that passes wrongly if the guard stays denominated on `pages.length`). Skew both ways clean: old workflow + cache args → `files_cached undefined`, line renders `cached 0`; new workflow + no cache args → `files_cached 0`, `cache_fingerprint null`, behaviour identical to HEAD. `PAGE_SCAN` unchanged at **3598**. `uv run tools/package-lint.py --expect-version 0.16.0` → **exit 0**, `package-lint: A/B/C/E PASS, D PASS — vlt 0.16.0`. Deviations/notes: (1) the corpus is assembled in **page order** (fresh ∪ reused) rather than F1(d)''s literal fresh-then-appended-reused — reason: findings must not depend on which pages happened to be cached, and page ordering makes a mixed run''s arrays identical to a cold run''s; parity check (2) is unaffected, the mixed run gains. (2) F2(b)''s new step is inserted as **step 2**, renumbering the old steps 2→3, 3→4, 4→5; two pointers were corrected in the same edit — step 1''s internal *(step 4 below)* → *(step 5 below)*, and `vlt-lint/SKILL.md`''s *"full-scale.md step 3"* → *"step 4"*. Forced by the insertion, not named in the brief. (3) that same `vlt-lint/SKILL.md` sentence **restated** the un-narrowed B10-12 predicate (*"or a `files_checked: 0` report"*); disposition 10 narrowed the predicate in its single home, so the restatement was rewritten as a pointer that restates nothing — leaving it would have shipped a stale second statement of a rule this build narrowed. (4) F2(b)''s worked-instance sentence could **not** carry `extraction@6` / `decision-log@3` in `name@N` form: package-lint **Group E** refuses a stray pin recited outside `depends_on:` (observed as a real FAIL, then fixed). Written version-free — *"`extraction` convention moving 6 → 7"*. (5) `full-scale.md`''s `workflow(''vlt-lint-full'', {…})` example and its resume sentence gained `pageHashes, cachedScans, rulesetFingerprint` — implied by F2(a)/(b), not spelled out as an edit. (6) `scanFingerprint` is FNV-1a **widened** to 20 hex chars (forward hash + reverse-string hash + length) rather than a bare 32-bit value — the brief allows "32-bit-or-wider", and a bare 32-bit hash over a ~7 KB prompt has too much accidental-collision surface for a value whose only job is to notice that the text moved. (7) the CHANGELOG heading is dated **2026-08-25** (today). The owner holds the tag; **if the release lands on a later date the heading date must be re-stamped before tagging** — package-lint D checks the version, not the date. (8) V8 R4 enumeration audit run and recorded below; V9 (R3) not applicable, stated. **The release is NOT performed:** no ff-merge, no tag, no push — held for the owner (§8). Next: `release vlt 0.16.0`.'
module_code: 'vlt'
created: '2026-08-25'
derives_from:
  - 'factory/cycles/11-reachability/filings/2026-08-24-102813-full-lint-cost-scales-with-corpus-not-with-change.md (A11-11 **direction 2** — "separate coverage from recomputation": a per-page findings cache keyed on page bytes × the convention version vector; cache extracted facts, never verdicts; the coverage line states `scanned N / cached M of T`. Carried into Cycle 12 by the Cycle-11 closeout hand-off.)'
  - 'factory/inbox/2026-07-26-124223-lint-has-no-memory-of-adjudicated-divergence.md (the Q8b companion, `B5-6(2)` on the E8 register — read for the shared-mechanism obligation only; see brief-time disposition 2. **No part of it is built here.**)'
roadmap: 'factory/cycles/12-proxy-claims/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-25): Q8b(b) DIRECTION 2 LANDS THIS CYCLE, justified by the direction-0 live number `churn_since_last_full: 5 of 146` · Q8b brief-time obligation — design the sidecar with filing `124223` in view, shared mechanism or it gets built twice · D3 ONE RELEASE, WHOLE CYCLE — this build carries it · roundtable A11 build-2 queues behind builds 1 AND 3 · roundtable A10 the cache key (five independent hits) · A12 the acceptance shape · A13 the derive-first boundary must be answered · A14 `checks.md`''s narrowing question (Mary dissents; the brief rules) · A15 `lint-debt`''s premise · A16 `coverage_caps` is NOT retired · A3(John) if the one-tag load proves over the line, the cut point is build-2'
risk: 'moderate — no convention `version:` moves and no consumer walk is owed, but the build edits the **operating contract** (one Decay-contracts row), which costs a `vault-rule-card.md` `derived_from:` re-derivation under package-lint **C6**; it narrows the **B10-12 version-skew refusal predicate**, a defence whose three-cycle debt was only retired in Cycle 11; and it is the release build, so the `--expect-version` gate and both version strings ride it.'
---

# Build #2 — the change-keyed findings cache

## Intent

A full lint re-judges every page in the wiki every run. On the 2026-08-24 live full run,
`churn_since_last_full` measured **5 of 146** — **141 pages re-judged for nothing**, at one
`haiku` agent apiece plus the convention bytes each agent reads. Direction 2 separates
**coverage** from **recomputation**: a per-page sidecar of *extracted facts*, keyed on a hash
of the page bytes crossed with a fingerprint of the ruleset those facts were adjudicated
under. Full mode re-scans only pages whose key changed, reuses the rest, runs the whole-corpus
JS reduce exactly as today, and reports `scanned N / cached M of T` beside the fingerprint it
cached under — so a cached run can never read as a fresh sweep.

This is the cycle's **last** build, and the ordering is a correctness constraint, not a
preference (roundtable A11, five voices converged): a sidecar populated before builds 1 and 3
would serve findings adjudicated under a **retired ruleset**. Both predecessors are BUILT on
this branch — build-1 `f134190` (rewrote `pageScanPrompt` and `PAGE_SCAN`), build-3 `5585877`
(bumped `extraction.md` 6 → 7 and added the `para_writer_unauthorized` check) — and build-4
`0e76901` (bumped `decision-log.md` 3 → 4) is BUILT too. §F1's fingerprint is what makes each
of those a cache invalidation rather than a silent staleness.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** In
particular: **sampling is forbidden unconditionally** (`ST-3`'s standing anti-direction, and
the filing's own "explicitly not proposed"); **no `coverage_caps` entry is ever removed to make
a run look cleaner** (the filing's standing rule, restated as roundtable A16); and the cache
stores **facts, never verdicts** — the JS reduce, the index pass and the cluster/pair passes
all still run whole-corpus every run.

---

## Brief-time dispositions

**1. The sidecar's home is `_agent/lint-cache.yaml` — a fixed agent-zone path, NOT a new
`vault_structure` key.** *(Deferred by the roadmap: direction 2 names no home.)*
The established pattern for an agent-zone operational file that no consumer needs to
re-locate is a fixed `_agent/` path — `_agent/dispatch.md`, `_agent/reflexes.md`,
`_agent/dispatch-profile.md`, `_agent/mint/decision-log.md` are all hardcoded and all live in
the Decay-contracts table without a map key. Three reasons to prefer that here over a key:
(a) a new key rides `vlt-upgrade`'s merge-config path, where **C6-b is a known open defect —
merge-config strips `vault_structure`** (Arc 6 carry-forward, still uncaptured); (b) the
`crossLayerSlugs` predicate at `full-scale.md:7` qualifies **directory-valued** keys, so a
file-valued key is dead weight in the map; (c) a key costs `module.yaml`, the contract's
structure table, a `vlt-setup` creation step and a `vlt-vitals.py` map row for zero
addressability gained. **The file is created lazily by the first full run** (the
`_agent/dispatch.md` precedent) — `vlt-setup` gains nothing.

**2. Q8b's shared-mechanism obligation: the mechanism filing `124223` asked for ALREADY
SHIPPED, and build-2 must NOT duplicate it.** *(Q8b: "design the sidecar with the
adjudicated-divergence memory filing `124223` (`B5-6(2)`) in view — shared mechanism, or it
gets built twice.")*
Grounded at HEAD, not from the filing's text: `124223` §4 asked for (A) a `ref:` machine key
on decision-log entries, (B) a read-before-flag on governance findings, (C) a lint-time
write-through. **All three are shipped.** `decision-log.md:48` states the `ref:` key *"is the
machine key `vlt-lint`'s read-before-flag matches on"*; `:108` rosters the read-before-flag as
a reader; `:118` states the check with its three states (`adjudicated`/`undisposed`/
`unclassifiable`) and its legal response; `checks.md:42` carries the read-before-flag preface;
`report.md:43` carries the `governance_memory:` denominator and `:71` `rulings_recorded:`.
**So the answer to "shared mechanism or built twice" is neither: they are two different
mechanisms with two different homes, and the boundary is already drawn.**

| | `124223` — adjudication memory | build-2 — the findings cache |
|---|---|---|
| what is stored | a **human ruling** on a governance finding | a scanner's **extracted facts** about a page |
| where | `_agent/mint/decision-log.md` (`ref:`-keyed, append-only, permanent) | `_agent/lint-cache.yaml` (rewritten in place, disposable) |
| written by | the event itself (a human rules; lint writes through) | the process's own run |
| invalidated by | a superseding entry, by hand | a page-byte or ruleset-fingerprint change, mechanically |
| if deleted | a ruling is lost — a real regression | the next run goes cold; nothing is lost |

**Binding consequence: the sidecar carries no adjudication, no dismissal, and no governance
finding.** Cross-run *finding suppression* — the filing's item 4 — is **not built here**. If a
later cycle wants it, its home is the decision log, not this cache. The builder must not add a
"dismissed" or "acknowledged" field to the sidecar; the record shape in F1 is closed
(`additionalProperties` posture) and that is deliberate.

**3. A13 — the derive-first boundary, answered rather than asserted.**
`vault-operating-contract.md:349` (re-derived, correct at HEAD): *"Derive-first does not
license deriving a state from the residue of the very process that produces it — where the
only available signal is the process's own leavings, the state must be **recorded, not
inferred**."* The worked instance is `vlt-upgrade/SKILL.md:45` (*"never read from the prior
ledger entry"*), correct at HEAD. **Build-2 opens a third home and it sits on the LEGAL side,
for two independently sufficient reasons:**

  1. **Nothing is inferred.** The clause's own remedy is *"the state must be recorded"* — the
     sidecar records the scanner's returned facts verbatim, under an explicit key. It is the
     recorded-state branch of the rule, not the inferred-from-residue branch.
  2. **The reuse decision is not derived from the residue at all.** Whether a record may be
     reused is decided by comparing two values computed **this run from primary sources** — the
     page's current `sha256` (read from the page file) and the current ruleset fingerprint
     (read from the module version, the pin vector, the merged conventions and the check
     catalog). The sidecar is only ever the *object* of that comparison, never a *source* of
     it. A corrupt, forged or stale sidecar cannot cause a stale finding to be served; it can
     only cause a cache miss.

  The contrast with `vlt-upgrade:45` is exact and is what makes the third home legal: the
  preserve set has **no primary source other than the prior ledger**, so reading the ledger
  *is* inference from residue. A page's bytes are a primary source that is always available.
  **Write this reasoning into the sidecar's own header comment (F1) — it is the file's
  standing defence against being read as a derive-first violation.**

**4. A14 — `checks.md`'s narrowing: MARY'S DISSENT IS UPHELD. The clause survives intact; no
narrowing, no precedence statement, no edit to the rule.**
*(A14 proposed narrowing the spec-candidate clause to "no stored **verdict**; derived facts may
be carried in the sidecar keyed on change." Mary dissented: the clause survives intact,
"facts-not-verdicts is that rule honoured, not repealed." The roadmap says the brief rules.)*
**Grounding correction first: the cite has drifted.** A14 cites `checks.md:49`; at HEAD that
line is the *personalized-extraction firewall*. The clause A14 quotes — *"never prior lint
reports (`{lint_reports}` is not read; reports stay walker-exempt)"* — is in the
**Spec candidates** bullet at **`checks.md:50`** (build-3's `para_writer_unauthorized` work
shifted the catalog by one).
Read at its real site, the clause is scoped to **how the spec-candidate check derives its
repeat-count**, and its population is `{lint_reports}`. The sidecar is not a lint report, is
not in `{lint_reports}`, and is not read by the spec-candidate check. **The two rules do not
address the same population, so there is no overlap to eliminate** — D5's precondition is
absent, and both the narrowing and the fallback precedence statement would be inventions.
`checks.md:50` is **not edited by this build.** What the build owes instead is one clause in
the sidecar's own single home stating that it is not a report and is never read by any check's
counter (F1's header, F2's step 5) — a pointer outward, not a rule inward.

**5. A15 — `lint-debt`'s premise: it STANDS this cycle, with its reason recorded. Not
re-tuned, and not re-tuned blind.**
*(Victor: the tripwire rations full runs because a full run is expensive; direction 2 makes
that premise false. Re-tune on the first post-release numbers **or** record why it stands.)*
Re-grounded: `tripwires.yaml:83-89` — `id: lint-debt`, `metric: ingests_since_lint`,
`threshold: ">= 10"`, `review_after: 2027-01-31`. **It stands, for three reasons.**
(a) The metric is `ingests_since_lint`, which counts *work piled up*, not *cost*; the threshold
is a nudge cadence, and cheapness makes the nudge more affordable, not wrong.
(b) `{tripwires}` is a **vault-owned, human-gated** file (contract Decay table, the
`{upgrade_ledger}`/`{overlays}`/`{tripwires}` row); the module ships a default, and a live
vault may already have tuned it — a module-side threshold change is not delivered to a vault
that edited it, so a blind bump buys nothing and desynchronizes the shipped default from the
field.
(c) There are **no post-release numbers yet**. The evidence a re-tune needs is exactly
acceptance check (5) below. **Recorded for Cycle 13:** re-tune `lint-debt` against the first
post-release full-run `lint_cache:` and `cost_accounting` lines, or record again why it stands.

**6. A16 — `coverage_caps` is NOT retired and the coverage line is ADDITIVE.** Recorded so no
reader takes the honest cache line as an opening. `ST-3` anti-direction 2 stands. The new
`lint_cache:` line sits **beside** `coverage_caps:`, `cost_accounting:` and
`churn_since_last_full:`, and no existing cap message, denominator or blind-spot statement is
removed, shortened or merged. A cached run is **not** a capped run — but it is also not a
fresh one, which is precisely why the line names the fingerprint and the two counts.

**7. Version: `0.16.0`, which is already asserted in shipped source — the owner confirms it,
the builder does not choose it.** The branch is `cycle12-v0.16.0`; build-4's brief already
wrote `--expect-version 0.16.0`; and **build-3 shipped the literal string into a shipped
surface**: `vlt-upgrade/SKILL.md:124` reads *"**Crossing v0.16.0** it renders, at minimum: …"*.
A different number would require editing that line. The builder writes `0.16.0` into both
version strings and the CHANGELOG heading; **the owner approves the tag** (§8).

**8. Interim posture (R1): not applicable.** No rule, check or finding class ships ahead of
its mechanism. The `lint_cache:` reporting rule (F3), the cache mechanism (F1) and the SKILL's
read/write of the sidecar (F2) all ship in this one build, in one release.

**9. Retirement clause (P-15): this build retires NOTHING, and that is an answered question,
not a blank.** *(A48: mark each retirement PRE-NAMED or BEAT-PRODUCED. A50: the cycle records
its retirement count at closeout.)* Three retirement candidates were put to this build by the
roundtable's obsolescence beat; **all three were examined and all three are refused**:

| candidate | site | disposition |
|---|---|---|
| `checks.md`'s "never prior lint reports" clause | `checks.md:50` | **survives intact** — populations disjoint, no overlap to eliminate (disposition 4) |
| `coverage_caps` (as made redundant by the coverage line) | `full-scale.md:10`, `report.md:72` | **refused** — the honest line is additive; retiring a coverage disclosure to make a cache look complete is the exact move `ST-3` forbids (A16) |
| `lint-debt`'s full-run ration | `tripwires.yaml:83-89` | **survives, reason recorded** (disposition 5); a Cycle-13 re-tune is named with its evidence |

**Build-2's contribution to the cycle's retirement count is zero, all three refusals
beat-produced.** The cycle's retirements are build-3's (pre-named, D2) plus build-3's
build-time additions; this build's honest input to A50's closeout line is *three candidates
examined, zero retired, all three refusals reasoned*. Entering this as a zero rather than
leaving the clause blank is the point of the clause.

**10. Cached records do not count as `files_checked`, and that collides with the B10-12
refusal — the refusal predicate is narrowed, not the counting rule.** *(Judgment call, made
without the owner; the collision is not named anywhere in the roadmap.)*
`report.md:77` and the workflow's own comment at `:498` fix the Gap-B counting rule:
*"count a page as checked only if it was actually read/scanned this run."* A cached page was
not. So `files_checked` stays **fresh scans only** — which means a fully-cached run returns
`files_checked: 0`, and `full-scale.md:9` **refuses a `files_checked: 0` report as a stale
vault-local workflow copy** (the B10-12 version-skew defence, whose bound debt was only retired
in Cycle 11 — it is not to be weakened casually).
**Ruling:** the counting rule is untouched; the refusal's **population is narrowed** from
"pages scanned" to "pages **adjudicated** this run" (`files_checked + files_cached`). This is
D5 elimination on a shipped rule: after the narrowing the two rules cannot both fire on one
run, and no precedence statement is needed. The defence loses nothing it was built for — a
stale workflow copy ignores the cache args entirely and returns `files_cached: 0`, so a
stale-copy shortfall still refuses exactly as today. F1 and F2 carry both halves; verification
V4 proves the defence still fires.

**11. The majority-coverage floor measures the FAN-OUT, not the corpus.** Same shape as 10,
inside the workflow. `vlt-lint-full.js:265` refuses below `ceil(pages.length / 2)` scanned.
With cached records spliced into `scans`, that guard would pass on a run where every dispatched
agent died, because the cache made up the numbers. **Ruling:** the guard is re-anchored to the
dispatched population (`freshScans.length` against `toScan.length`) and is **skipped when
`toScan.length === 0`** (a fully-cached run has no fan-out and therefore no fan-out shortfall).
The whole-corpus `scans` array still feeds the reduce. F1 carries it; V5 proves it.

**12. Whose facts the coverage line reports: the WORKFLOW's, never the SKILL's intent.** The
SKILL may pass cached records to a workflow copy too old to use them. `lint_cache:` is composed
**only** from the counts the workflow returns (`files_checked` / `files_cached` /
`cache_fingerprint`), never from what the SKILL passed in. A vault whose workflow copy predates
this build renders `cached 0 of T` — true, and quietly diagnostic of a stale copy. F2 states
it; V6 tests the skew both ways.

---

## F-sites

Every `file:line` below was re-derived against **HEAD (`0e76901`)** on 2026-08-25. Corrections
found in this pass are marked **⚠ GROUNDING CORRECTION** and are the fourteenth and fifteenth
this cycle has logged.

### F1 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` — the cache seam

**Current state (HEAD, all cites re-derived):**

| what | line | note |
|---|---|---|
| `args` doc block | `:31-56` | `pages: [{ slug, path }]`, the `crossLayerSlugs`/`stubSlugs` division comment at `:38-40` is the precedent this build follows |
| the **args-are-a-JSON-string** parse-on-intake | `:66-67` | `let a = args \|\| {}` / `if (typeof a === 'string') …` — **live standing rule; do not disturb** |
| `const pages = …` | `:78` | |
| `PAGE_SCAN` | `:130-176` | build-1 edited `:143`/`:144`/`:153` and deleted `key_claims`; measured **3598** of the 3700 E6 cap, **102 chars of margin** |
| `pageScanPrompt` | `:199-201` | build-1's edit; `:199` head, `:200` rules half, `:201` reduced return-only half |
| `const scans = []` | `:203` | |
| the chunked fan-out loop | `:220-244` | `CHUNK = 16` at `:220`; `costRow('Scan pages', …)` at `:245` |
| the partial-sweep coverage cap | `:250-257` | |
| the **near-total shortfall guard** | `:265-280` | `scans.length === 0 \|\| scans.length < Math.ceil(pages.length / 2)`; `status:'failed'` return at `:268-280`, its `files_checked:`/`files_listed:` at `:272-273` |
| the findings return | `:496-558` | `files_checked: scans.length` `:499`, `files_listed:` `:500`, `coverage_caps:` `:555`, `cost_accounting:` `:557` |

⚠ **GROUNDING CORRECTION (14th this cycle).** Roundtable A10 and the ideation record describe
the cache key as *"the convention `version:` pins … the scan was judged under"*, implicitly the
workflow's own pin line. **That is insufficient, and build-3 is the proof.** The workflow's
`// depends_on:` at `:12` reads
`["frontmatter@13", "wiki-supersession@2", "wiki-index@2", "write-verification@3"]` —
**`extraction` is not in it and never was**, because the page scanners do not judge against
`extraction.md`. Build-3 bumped `extraction.md` **6 → 7** and added the
`para_writer_unauthorized` check; **neither moves a single character of `:12`.** A key built on
the workflow's own pins would have failed to invalidate on the exact build the roundtable
ordered build-2 to queue behind. The pin vector of record is therefore **`vlt-lint/SKILL.md:4`**
(the whole run's ack line), which at HEAD reads
`["frontmatter@13", "wiki-index@2", "wiki-supersession@2", "extraction@7", "write-verification@3", "spec@2", "consult@1", "decision-log@4"]`
— carrying **both** build-3's `extraction@7` **and** build-4's `decision-log@4`.

**The exact change.**

**(a) Three new optional args**, documented in the `:31-56` block in the same voice as
`crossLayerSlugs`/`stubSlugs` (the SKILL has filesystem access, this script has none — that
division is the reason these are args and not reads):

```
//     pageHashes:      {slug: sha256} (optional) // content digest per page, computed by the SKILL with an
//                                          //   unwrapped instrument it names in the record. Absent → no page
//                                          //   is cacheable this run (a cold sweep, stated, never silent).
//     cachedScans:     [{slug, key, scan}] (optional) // prior PAGE_SCAN records the SKILL read from the
//                                          //   sidecar. A record is reusable iff its `key` equals the key
//                                          //   recomputed here from THIS run's inputs. default [].
//     rulesetFingerprint: string (optional)// the SKILL-side half of the fingerprint (module version, the
//                                          //   vlt-lint pin vector, the merged convention digests, the check
//                                          //   catalog digest). Absent → cold sweep.
```

Parse them beside `:78-96` with the same defensive shape already used there (`Array.isArray`
guards, `typeof === 'string'` guards, no `||` fallback on a value where `0`/`''` is meaningful).

**(b) The prompt/schema half of the fingerprint, computed in the workflow** — the only place
`pageScanPrompt` and `PAGE_SCAN` exist. Immediately after `pageScanPrompt` is defined (`:201`),
add a small deterministic digest over the **invariant** prompt text and the schema:

```js
// The scan-surface fingerprint (A10). Any edit to the prompt's invariant half or to
// PAGE_SCAN changes it, so a sidecar written under the old surface cannot be reused —
// build-1 rewrote both in this very release, which is why this exists.
const canonicalScan = pageScanPrompt({ path: '', slug: '' }) + ' ' + JSON.stringify(PAGE_SCAN)
const scanFingerprint = <a stable 32-bit-or-wider hash of canonicalScan, hex>
```

Use a small inline hash (FNV-1a or equivalent, ~6 lines) — the script has **no `crypto` import
and no fs**; the strong digest lives on the SKILL side, and this half only needs to change
whenever the text changes, which a non-cryptographic hash does. Building the canonical string
from `{ path: '', slug: '' }` strips the per-page variable head (`${p.path}`/`${p.slug}`) so the
value is page-independent — the same 100-byte variable head build-1's disposition 1 measured.

**(c) The composite key and the split of the page list.** Before the fan-out loop:

```js
const runKey = (slug) => `${pageHashes[slug] || ''}|${scanFingerprint}|${rulesetFingerprint}`
// A record is reusable iff its recorded key equals the key recomputed from this run's
// inputs. Nothing in the sidecar is ever a SOURCE of that comparison — only its object.
const cacheBySlug = new Map(cachedScans.filter(c => c && c.slug && c.key).map(c => [c.slug, c]))
const reusable = (p) => pageHashes[p.slug] && rulesetFingerprint &&
  cacheBySlug.get(p.slug) && cacheBySlug.get(p.slug).key === runKey(p.slug)
const toScan = pages.filter((p) => !reusable(p))
const reused = pages.filter(reusable)
```

**(d) The loop fans out `toScan`, not `pages`.** `:224`'s `for (let i = 0; i < pages.length; …)`
becomes `toScan.length`, and `pages.slice(...)` becomes `toScan.slice(...)`. Collect fresh
results into a `freshScans` array; **then** splice the reused records into the corpus:

```js
for (const c of reused) scans.push(c.scan)   // cached FACTS join the corpus; the reduce runs whole
```

The budget-guard message at `:225-230` keeps its shape but denominates on `toScan.length`, and
its cap text names the cached count so a capped cached run is still honest.

**(e) The two guards, per dispositions 10 and 11.**
- The partial-sweep cap at `:250-257`: compare `freshScans.length` against `toScan.length`.
- The near-total shortfall guard at `:265`: becomes
  `if (toScan.length > 0 && (freshScans.length === 0 || freshScans.length < Math.ceil(toScan.length / 2)))`.
  Its comment block (`:258-264`) is updated to say **why** it now measures the dispatched
  population: the cache would otherwise make up the numbers for agents that all died. Its
  `status:'failed'` return gains `files_cached: reused.length` beside `:272-273`, so the
  failed-run record `full-scale.md:9` writes is complete.

**(f) The return gains three keys** (findings return, `:496-558`, beside `files_checked:` at
`:499`):

```js
  files_checked: freshScans.length,          // Gap B rule unchanged: SCANNED this run
  files_cached: reused.length,               // reused under an unchanged key — adjudicated, not scanned
  files_listed: pages.length,
  ...
  cache_fingerprint: rulesetFingerprint ? `${scanFingerprint}|${rulesetFingerprint}` : null,
  fresh_scans: freshScans,                   // the records the SKILL writes back to the sidecar
```

`fresh_scans` is the write-back channel: the workflow is **read-only** (`full-scale.md:8`) and
must stay so — it returns the records, the SKILL persists them. Do **not** add an fs write.

**(g) `cost_accounting` is unchanged in shape** and stays truthful for free: `agents_dispatched`
and `prompt_chars` already count only what was dispatched, so a cached run's numbers fall on
their own. Add nothing.

**Why:** A11-11 direction 2; A10 (the cache key); dispositions 10, 11.

**Out of scope at this site:** the `key_claims` drop, the `wiki-index` read drop and the `:201`
reduction are build-1's and are **BUILT** — do not revisit them. The cluster/pair/index passes
are not cached (they re-read live by design; build-1's F4 deliberately kept `:403`'s live
re-read) and are not touched.

### F2 — `skills/vlt-lint/references/full-scale.md` — the SKILL's half

**Current state (HEAD):** 13 lines. Step 1 (page/`crossLayerSlugs` discovery) at `:7`;
step 2 (invoke) at `:8`; **step 3 the version-skew refusal** at `:9`; step 4 (apply fixes) at
`:10`; the cost + churn sub-bullet at `:11`.

**The exact change — four edits, no new file.**

**(a) Step 1 gains the page digests.** Append to `:7`: while globbing the page list, compute a
content digest per page and pass it as `pageHashes`. The digest **uses an unwrapped instrument
and names it in the run's record** — the operating contract's *Honest reporting* instrument
rule (`vault-operating-contract.md:351`); point at it, do not restate it. This mirrors
`:11`'s existing `churn_since_last_full` instrument sentence exactly — write it in that voice.
`shasum -a 256` over the page files is the expected instrument; the rule names a property, not
a tool.

**(b) A new step between the current steps 1 and 2 — read the sidecar and compute the
fingerprint.** It states, in one paragraph and as the **single home** of the fingerprint's
definition:

> Read `_agent/lint-cache.yaml` if it exists. Compute this run's **ruleset fingerprint** — a
> digest over, in this order: the installed `module_version`; this skill's own `depends_on:`
> pin vector verbatim; the digest of each convention this run judges against **as merged with
> its overlay** (base + `{overlays}/{name}.overlay.md` where one exists — the same merged-on-read
> set the fan-out's scanners receive); and the digest of `references/checks.md` (plus its
> overlay, where a vault carries one). Any of those moving invalidates every record, because
> each of them changes what a finding *means*. Pass it as `rulesetFingerprint`, and pass the
> file's records as `cachedScans`. **A missing, unparseable or schema-mismatched sidecar is a
> cold run, stated in the report — never an error and never a silent full sweep presented as a
> cached one.**

Name the three worked instances so a reader can see the mechanism bite, since they are this
release's own: **`module_version` 0.15.0 → 0.16.0** (build-1's `pageScanPrompt` and `PAGE_SCAN`
rewrite is carried by the version and by the workflow-side `scanFingerprint` independently);
**`extraction@6 → @7`** and the new `para_writer_unauthorized` check (build-3); and
**`decision-log@3 → @4`** (build-4). **State plainly: the first full run after any release is a
COLD one** (A10 — *stated rather than discovered*).

**(c) Step 3, the version-skew refusal (`:9`) — the narrowed predicate** (disposition 10).
*"a findings report with `files_checked: 0`"* becomes *"a findings report that adjudicated no
page at all — `files_checked` **and** `files_cached` both `0`"*, with one clause of reasoning:
a stale vault-local workflow copy ignores the cache args and returns `files_cached: 0`, so the
stale-copy signal the defence was built for is unchanged; a fully-cached run adjudicated every
page and is not a shortfall. **The failed-run record's key list gains `files_cached`.**
Everything else in step 3 — the failed-run YAML, the directed refusal, the no-log-line rule, the
`lint-debt` non-reset — is untouched.

**(d) Step 4's cost sub-bullet (`:11`) gains a sibling** — the write-back and the coverage line:

> **The findings cache (A11-11 direction 2).** After a sweep that was **not** refused, rewrite
> `_agent/lint-cache.yaml` in place from the run's own records: this run's fingerprint, and one
> record per page adjudicated this run — the workflow's returned `fresh_scans`, plus the reused
> records that are still valid. **It is rewritten whole, never appended to**, so it never
> accumulates and never needs draining; deleting it is always safe and costs only a cold run.
> It stores **extracted facts, never verdicts**: no finding, no ruling, no dismissal, and no
> governance state (a human's ruling on a governance finding belongs in the decision log's
> `ref:`-keyed record, which the read-before-flag reads — a different mechanism with a
> different home). It is **not a lint report**, is not written to `{lint_reports}`, and no
> check's counter derives from it. Compose the report's `lint_cache:` line from the
> **workflow's returned counts only** — never from what was passed in — so a vault whose
> workflow copy predates this feature renders an honest `cached 0`.

**Why:** the sidecar has no home, no lifecycle and no honesty rule until this reference states
them; `full-scale.md` is already the single home of the fan-out protocol and of the
`crossLayerSlugs` predicate, so this is the one place both halves can be read together.

**Out of scope:** the `crossLayerSlugs` derivation at `:7` is not touched. The PARA population
(build-3's step 0) is scanned by the SKILL inline and is **not cached** by this build — see
Out of scope 3.

### F3 — `skills/vlt-lint/references/report.md` — the coverage line

**Current state (HEAD):** the report fence's tail at `:69-74` — `rulings_recorded:` `:71`,
`coverage_caps:` `:72`, `cost_accounting:` `:73`, `churn_since_last_full:` `:74`. The
`files_checked` counting rule is prose at `:77`. The `files_checked`/`files_listed` schema
lines are `:12-13`.

**The exact change.**

**(a) A new key in the fence, immediately after `churn_since_last_full:` (`:74`):**

```yaml
lint_cache: <scanned N / cached M of T pages (fingerprint <fp>, written YYYY-MM-DD) | cold (<reason>) | not used (scoped run)>   # facts reused under an unchanged page digest + ruleset fingerprint — never verdicts; additive to coverage_caps, never a replacement
```

**(b) One schema line added beside `:12-13`:** `files_cached: 0   # pages whose extracted facts
were reused under an unchanged key — adjudicated this run, NOT scanned (see files_checked)`.

**(c) The `files_checked` counting rule at `:77` gains one sentence**, not a rewrite: a cached
page is **not** counted as checked — it is counted in `files_cached`, and
`files_checked + files_cached < files_listed` is still a coverage cap, exactly as today.

**(d) A short reporting paragraph** in the run of `**…reporting.**` paragraphs at `:79-85`,
matching their voice:

> **Findings-cache reporting.** `lint_cache:` states what the run reused and what it was reused
> *under*: the two counts against the listed total, and the fingerprint the records were
> adjudicated under. It is **additive** — `coverage_caps:` keeps every cap it would have carried
> and nothing is removed to make a cached run look cleaner. **A cold run says so and says why**
> (no prior cache; fingerprint changed; sidecar unreadable), so the first full run after an
> upgrade is a stated cold run rather than a discovered one. Scoped runs render the literal
> `not used (scoped run)`. Per the operating contract's honest-reporting rule — read it there.

**Why:** direction 2's second non-negotiable — *"the coverage line must state
`scanned N / cached M of T`, so a cached run can never read as a fresh sweep"* — plus A10's
requirement that the line name its fingerprint, and A16's that it not displace anything.

### F4 — `skills/vlt-lint/SKILL.md` — the router's one pointer

**Current state (HEAD):** `depends_on:` at `:4`; the step sequence at `:50-56`
(*Step 5 — report* at `:55`, *Step 6 — log* at `:56`); the full-mode-at-scale router sentence
at `:43`; Step 6's heading at `:68`, its report-persist paragraph at `:74`, and the B10-12
failed-run pointer at `:76`.

**The exact change: one sentence appended to Step 6's report-persist paragraph (`:74`)**,
after the report-persist rule and before the B10-12 pointer at `:76`:

> A full-mode sweep also rewrites the findings cache at `_agent/lint-cache.yaml` — mechanics at
> `references/full-scale.md` (the fan-out protocol's single home). It is **not** a report: it is
> never persisted to `{lint_reports}`, never wake-read, and deleting it costs only a cold run.

`depends_on:` at `:4` is **not** edited — no convention `version:` moves in this build. But note
for the builder: **that line is now read as data by the fingerprint**, so a future build that
edits it changes the fingerprint by construction. That is the intended coupling, and F2's step
states it.

**Out of scope at this site:** Step 0's scoped/full selection and build-3's PARA population
selection are untouched.

### F5 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md` — one Decay row

**Current state (HEAD):** *Decay contracts — retention declared at birth* at `:307`; the table
header at `:311-312`; rows `:313-325`; the `{lint_reports}` row at `:323`; the
`{upgrade_ledger}`/`{overlays}`/`{tripwires}` human-gated-accumulators row at `:326`; the
`{archive}` row at `:327`; the closing rule at `:329` — *"A new accumulating agent-zone file
class enters this table in the act that creates it — no accumulator ships without a declared
decay contract."*

**The exact change: one exempt row**, placed immediately after the `{upgrade_reports}` row
(`:324`), in the table's existing voice:

```
| `_agent/lint-cache.yaml` (the findings cache) | exempt — **not an accumulator**: rewritten whole by each full-mode `vlt-lint` run, bounded by the page population, never wake-read, and safely deletable (the next run goes cold). Stores extracted facts keyed on change, never verdicts and never rulings — a governance ruling's home is the decision log | — | — | — |
```

**Why:** `:329` demands the row only of *accumulating* classes, and this file does not
accumulate — so the row is a **declared exclusion rather than a silent omission**, which is
what the table exists for and what R4 requires (§Verification V8). It also forecloses the
`ST-2` RC2 shape: a future filing rediscovering that the lint cache has no declared retention.

**⚠ Cost, per the anatomy's "No bump owed is not no cost":** editing the contract fires
**package-lint C6** (`tools/package-lint.py:325-348`). The build **must re-derive**
`vault-rule-card.md:11`'s `derived_from: … sha256:` against the edited contract and re-stamp
its `(derived <date>)`. The card's **text does not change** — this row is not act-blocking — so
`RULE_CARD_BUDGET` is not at risk (measured **7,106 B** at HEAD against 8,000; build-3 left
894 B of headroom). Only the digest moves.

### F6 — `CHANGELOG.md` — the v0.16.0 entry (build-3 deviation 4's debt)

**Current state (HEAD):** `## v0.15.0 — 2026-08-24` at `:7`, with `**Cycle 11** — the
reachability cycle.` at `:9` and one `- **Build N — <title clause>:** …` bullet per build at
`:11-19`. Newest first, immediately under the preamble ending `:5`.

**This is not release prose — it is a shipped functional input.** Build-3's F11 shipped
`vlt-upgrade/SKILL.md:122`, which fixes `governance_rule_changes:`'s source as *"the module
source's `CHANGELOG.md` entries for the versions being crossed, read from the same source tree
this upgrade applies from"*, and `:124` states what **crossing v0.16.0 must render, at
minimum**. **A missing or thin v0.16.0 entry makes that key render less than the shipped text
promises** — the rule-change notification would fail on the very release that introduced it.

**The exact change: a new `## v0.16.0 — <release date>` section above `:7`**, in the file's
existing shape:

- `**Cycle 12** — the proxy-claims cycle.`
- One bullet per shipped build, its clause taken from the brief `title:` (the anatomy's rule —
  titles are collected verbatim into this file), in build order:
  - **Build 1** — page-scanner corrections + waste removal: the full-lint page scanner stops
    reading raw text as link structure and frontmatter validity as attestation, and sheds the
    reads it never used.
  - **Build 2** — the change-keyed findings cache: full lint stops re-judging pages nothing
    changed, and says how many it reused and under which ruleset.
  - **Build 3** — the PARA posture: PARA stops using location as a proxy for trust — honest,
    attested frontmatter becomes the entry condition, containers declare their own `writers:`,
    and lint enforces it.
  - **Build 4** — parked-interim guidance: a park records the blocker's shape, and something
    re-reads it at the upgrade that can invalidate it.

**Mandatory content, over and above the four bullets — the rule-change facts `:124` renders
from.** The v0.16.0 section must state, in rule-change vocabulary and unambiguously enough that
a reader crossing 0.15.0 → 0.16.0 can act on it:
1. `vault-operating-contract.md` **Layer 3** + `extraction.md` **v7** — PARA's entry condition
   is now honest, attested frontmatter rather than a closed set of named write surfaces; a
   container may declare `writers:` on its `charter.md`; **an undeclared container is `open`**,
   so a partner may now file an honest `author: agent` / `trust: raw` document into
   `{projects}`/`{areas}`/`{resources}` outside `{wiki}` where no ancestor charter refuses it.
2. `vlt-lint` gains **`para_writer_unauthorized`**.
3. `decision-log.md` **v4** — the `kind: parked-interim` entry, re-read by `vlt-upgrade`'s
   reconcile pass and surfaced as `parked_interims_review:`.
4. The **retirement**, named as one: the Layer-3 location prohibition and the surface-count
   prohibition are gone (P-15's rail, and the first thing a vault reading the entry should know).

**Ordering constraint for the builder:** the ordinal build numbers here are the roadmap's
authoritative post-renumbering ones (four builds — the amendment trigger moved to the platform
channel at ruling R-5). Do **not** renumber to shipping order.

**Scrub:** this file is public and vault-facing. No machine paths, no username, no
vault-local artifact paths — placeholders only.

### F7 — the release: both version strings

**Current state (HEAD):** `.claude-plugin/marketplace.json:16` — `"version": "0.15.0"`;
`skills/vlt-setup/assets/module.yaml:4` — `module_version: 0.15.0`.

**The exact change:** both to `0.16.0`, in this build (disposition 7). §8 carries the gate.

---

## Registration

**None** — no new skill, no new workflow, no `module-help.csv` row, and **no convention
`version:` moves**, so no consumer walk and no re-ack is owed. `write-verification.md` stays
`version: 3` / 5 consumers, `extraction.md` stays at `7` / 4 consumers, `frontmatter.md` at
`13` / 10, `decision-log.md` at `4` / 5 — all as builds 1, 3 and 4 left them.

**"No bump owed" is not "no cost" — the two gates this build does owe:**

- **package-lint C6** — F5 edits `vault-operating-contract.md`, so `vault-rule-card.md`'s
  `derived_from: … sha256:` is re-derived and re-stamped **in the same build** (F5). The card's
  text is unchanged; `RULE_CARD_BUDGET` has 894 B of headroom and is not at risk.
- **package-lint D** — this is the release build, so `--expect-version 0.16.0` runs and both
  version strings move together (F7, §8).

**Not owed:** **E4** (no `package-lint` check is added or changed, so no
`tools/test-package-lint.py` case and no `CASE_FLOOR` bump — R2 is not applicable);
**E5** (the workflow's `// depends_on:` line at `vlt-lint-full.js:12` is **not** edited — the
build adds args and a hash, not a convention ask); **E1/E2/E3** have nothing to re-derive, but
Group E still runs as the recorded check (§Verification V2).

---

## Out of scope (dispositioned)

1. **Cross-run finding suppression** (`124223`'s item 4 — "don't re-report a flag a human
   already dismissed"). *Not built.* Disposition 2: the mechanism it needs already shipped as
   the decision log's `ref:`-keyed read-before-flag; the sidecar deliberately carries no
   dismissal state. A future cycle that wants suppression extends the decision log, not this
   cache.
2. **Direction 4 (scanner-card projection) and A12-1's cause-fix instrument.** *Declared for
   Cycle 13* (Q8b), not deferred. **Carry to Cycle 13's ideation, on roundtable A51:** direction
   2 **retires direction 4's own cost case** — a cached page is not scanned, so its agent never
   runs and never reads a convention; after this build at `churn 5 of 146` the convention-read
   pool falls from `ST-3`'s 8.6 MB/run to ~0.29 MB/run and direction 4's marginal saving to
   ~0.19 MB/run. **Cycle 13 must rule direction 4 on `ST-3` cause (a) — projection binds every
   future fan-out consumer, which survives direction 2 untouched — and re-measure the residual
   pool against acceptance check (5)'s numbers, not against the stale 8.6 MB figure.**
3. **Caching the PARA scan** (build-3's step 0 population) and the `{research}` candidacy pass.
   *Deferred, unruled.* Both run inline in the SKILL, not through the fan-out; direction 2 is
   scoped to the fan-out page scan and its measured 141-of-146 waste. Naming a second cached
   population in the release build would be scope the roadmap never ruled.
4. **Caching the index, cluster and seeded-pair passes.** *Rejected.* Their inputs are
   cross-page and change whenever any member page changes; a per-page key cannot express that,
   and the filing's non-negotiable is that the reduce stay whole-corpus.
5. **`checks.md:50`'s clause.** *Already covered* — disposition 4 rules it survives intact.
6. **`lint-debt`'s threshold.** *Deferred to Cycle 13 with its evidence named* — disposition 5.
7. **`vault_structure` / `module.yaml` / `vlt-setup` / `vlt-vitals.py`.** *Not touched* —
   disposition 1 rules the sidecar a fixed agent-zone path, not a map key, and F5's row is a
   declared exclusion from every wake-read enumeration.
8. **C6-b (merge-config strips `vault_structure`).** *Not fixed here* — a real open defect,
   still uncaptured since Arc 6; disposition 1 routes **around** it rather than into it. It
   remains a Cycle-13 capture candidate.
9. **A46's stale BLOCKED grading.** *Not acted on — owner act.* See §Routing.

---

## Verification (unit, at rest — lifecycle step 5)

**V1 — parse-on-intake, re-proved.** The workflow's `args`-as-a-JSON-**string** parse at
`vlt-lint-full.js:66-67` must still be the first thing that runs, and the **three new args must
be read from the parsed `a`, never from `args`.** Grep: `grep -n "JSON.parse(args" -A2` shows
the guard above every new destructure; and V7's harness run delivers `args` as a **string**.

**V2 — the handshake bipartite re-check. The check of record is `package-lint` Group E.**
`uv run tools/package-lint.py` — E1/E2/E3/E5. No pin moves in this build, so Group E is proving
that none moved. **Do not write a hand-rolled `grep "extraction@" skills/` as the recorded
verification** — it is self-confirming (it greps for the token you just wrote, in the files you
just edited) and cannot fail on the drift Group E exists to catch. A grep is an editing aid;
Group E is the record.

**V3 — packaging lint, A/B/C/E** mid-build (`uv run tools/package-lint.py`), then the
release run in §8. **C6 must pass** after F5 + the rule-card re-stamp; record the new sha and
the card's byte count. Confirm `PAGE_SCAN` is **unchanged at 3598** under E6 (this build must
not grow the schema; only 102 chars of margin remain).

**V4 — the version-skew defence still fires (disposition 10).** Three harness cases against the
shipped source with stubbed `agent`/`parallel`/`phase`/`log`/`budget`:
(a) a stale-copy simulation — every fan-out returns `null`, no cache args →
`files_checked: 0`, `files_cached: 0` → `status: 'failed'` **and** `full-scale.md`'s narrowed
predicate refuses it;
(b) a fully-cached run — every page reusable, `toScan` empty → a **findings report** with
`files_checked: 0`, `files_cached: T`, **not** refused, and the reduce populated;
(c) a half-cached run whose fan-out all dies — `toScan` non-empty, every fresh agent `null` →
`status: 'failed'` (disposition 11's re-anchoring; **this is the case that fails if the guard
is left denominated on `pages.length`**). Record all three returns verbatim.

**V5 — findings parity, cached vs cold (the correctness proof).** Run the shipped workflow
twice against one temp fixture of ≥ 6 pages with scripted scan results: run 1 cold (no cache
args), run 2 with every record cached under a matching key and the fan-out stubbed to **throw**
if dispatched. **The two returns must be byte-identical in `fix_now`, `flag_for_human` and
`opportunities`** — orphans, `missing_targets`, `category_no_match`, `attestation_census`,
`near_duplicates`, all of it. Then a third run with **one** page's hash changed: exactly one
agent dispatched, `files_checked: 1`, `files_cached: 5`, and the reduce still correct across
all six. Record the diff result and the three count triples.

**V6 — the two skew directions (disposition 12).** (a) New SKILL, old workflow: invoke with the
cache args against a copy of the **pre-build workflow** — it ignores them, fans out everything,
returns no `files_cached`, and the `lint_cache:` line composed from the return reads
`cached 0`. (b) Old SKILL, new workflow: invoke the new workflow with **no** cache args — every
page fans out, `files_cached: 0`, `cache_fingerprint: null`, behaviour identical to HEAD.

**V7 — harness sanity run** of the shipped source with `args` delivered as a JSON **string**,
a 3-page fixture and scripted scan results: the reduce is unchanged from build-1's recorded V8
baseline (`missing_targets`, `malformed_frontmatter`, `unmarked_supersessions`,
`attestation_census`, `category_no_match`, `index_drift`, `frontmatter_drift`,
`sources_vs_prose_mismatches`, `cost_accounting` all populate).

**V8 — R4 enumeration widening.** The build adds one new vault-local file class. Enumerations
audited and their dispositions: the contract's **Decay contracts table — WIDENED in this build**
(F5, a declared exempt row); `vlt-vitals.py`'s structure map and wake-read metrics — **declared
outside**, the file is disk-side and never wake-read, exactly as `{lint_reports}` is;
`full-scale.md:7`'s `crossLayerSlugs` predicate — **no edit needed by construction**, the
`_agent/` zone root is walked recursively and the file joins as an ordinary link target;
`vault_structure` / `module.yaml` — **declared outside** (disposition 1). Record the audit.

**V9 — R3 legal response.** The build **adds no finding class** (`lint_cache:` is a coverage
line, not a finding; `files_cached` is a count). **R3: not applicable** — stated, so the absence
is an answer rather than an omission.

**V10 — greps for cross-file agreement.**
- `grep -rn "lint-cache" skills/` → the mechanics in **exactly one** place (`full-scale.md`),
  plus short pointers at `SKILL.md` Step 6, `report.md`'s reporting paragraph, and the contract
  row. Single-home discipline: any second statement of the fingerprint's definition is a defect.
- `grep -rn "files_cached" skills/` → the workflow's two returns, `report.md`'s schema line and
  counting rule, `full-scale.md`'s narrowed step 3.
- `grep -n "files_checked: 0" skills/vlt-lint/references/full-scale.md` → **0** (the predicate
  was narrowed, not left beside its replacement).
- `grep -c "coverage_caps" skills/vlt-setup/assets/workflows/vlt-lint-full.js` → unchanged from
  HEAD (A16: nothing removed).
- `shasum -a 256` of the edited contract equals `vault-rule-card.md:11`'s stamped value.

**V11 — CHANGELOG cross-check.** Read `vlt-upgrade/SKILL.md:124` and confirm the new v0.16.0
section actually supports the minimum rendering that line promises — all four mandatory facts
in F6 present, in rule-change vocabulary.

**V12 — durability posture.** This build touches no `vlt-setup`/`vlt-upgrade` merge path and no
own-the-apply copy path. Re-confirm by grep that the B1 local-mint preserve path
(`vlt-upgrade/SKILL.md:55`, `:100`) is byte-identical. The new sidecar is vault-written and
**never** overwritten by upgrade — state it, then verify nothing in the copy surface names it.

**V13 — scrub.** No personal or vault-local content in any changed shipped file; worked
examples use placeholder paths. `CHANGELOG.md` gets the same scrub as a shipped surface.

**V14 — no `.decision-log.md` anywhere in the working tree** before the commit. *(Note the
collision build-4's brief spells out: the gitignored per-skill build artifact is a different
file from `_agent/mint/decision-log.md`, the vault's durable log. Delete the former; never
touch the latter.)*

---

## Release

**This IS the release build** (D3 — one release, whole cycle; roundtable A11 — build-2 is
last). All four builds are on `cycle12-v0.16.0`: build-1 `f134190`, build-3 `5585877`,
build-4 `0e76901`, and this build's own commit.

1. **Both version strings, in this build's commit** (F7): `.claude-plugin/marketplace.json:16`
   `"version": "0.16.0"` **and** `skills/vlt-setup/assets/module.yaml:4`
   `module_version: 0.16.0`. Both, or neither — a split bump is the failure the standing rule
   names.
2. **The gate:** `uv run tools/package-lint.py --expect-version 0.16.0`. **Tag only on exit 0**,
   and record the PASS summary line in the release commit message, so a skipped lint is visible
   in history.
3. Then ff-merge to `main`, tag `v0.16.0`, push main + tag.

**🛑 The release is HELD for the owner's explicit approval.** The builder's session ends at a
committed, lint-clean `cycle12-v0.16.0` with both strings bumped — **it does not ff-merge, does
not tag and does not push.** Two things are the owner's: the go/no-go itself, and the version
number's confirmation (disposition 7 — `0.16.0` is the branch-implied and shipped-text-implied
target, not an owner ruling on record). The release choreography then runs as one gated
sequence under `vlt-release` (`release vlt 0.16.0`), which re-runs the pre-flight, the
handshake and the gate itself.

**Carried into the release, from roundtable A3 (John):** the release-size argument bounded
direction 4 *out* and bounded nothing *in*, and nothing tests the one-tag load. *If the load
proves over the line, the cut point is **build-2** — independent of build-3's text, no shared
file, no acceptance dependency — never build-3's steps.* Recorded, not exercised: build-2 is
built, so the cut would now cost a revert rather than a deferral.

---

## Acceptance (live — appended to the roadmap ledger)

**Six checks — four `[ship-verifiable]`, all gating closeout; two `[field-contingent]`, neither
gating.** The A12 shape is honoured exactly: the ship-verifiable half is the sidecar **at rest
on a two-run temp fixture**; the live `churn`-ratio saving is field-contingent and **gates
nothing**.

**(1) `[ship-verifiable]` — GATES closeout. The two-run fixture: it populates, then it reuses,
and it says so.** On a temp fixture vault of ≥ 6 pages, run 1 (no sidecar) writes
`_agent/lint-cache.yaml` with a fingerprint and one record per page and reports
`lint_cache: scanned T / cached 0 of T … cold (no prior cache)`; run 2, with one page's bytes
edited and nothing else changed, dispatches **exactly one** scan agent, reports
`files_checked: 1`, `files_cached: T-1`, and a `lint_cache:` line naming the same fingerprint.
**Instrument:** the brief's Verification-5 harness run against the shipped workflow source with
stubbed `agent`/`parallel`/`phase`/`log`/`budget` and a real temp fixture — factory-side, at
rest, run at tag time. **Evidence:** the three count triples and both `lint_cache:` lines
recorded verbatim in the brief's BUILT `status:`.

**(2) `[ship-verifiable]` — GATES closeout. Findings parity: the cache changes cost, never
findings.** The cold run and the fully-cached run over the same fixture return **byte-identical**
`fix_now`, `flag_for_human` and `opportunities` blocks, and the one-page-changed run's reduce is
still correct across the whole corpus (orphans and `missing_targets` computed over all T pages,
not over the 1 rescanned). **Instrument:** Verification-5's runs 1–3, compared with an
**unwrapped** `diff` whose invocation is named in the record (the contract's instrument rule).
**Evidence:** the diff result and the third run's `missing_targets`/`orphans` recorded.

**(3) `[ship-verifiable]` — GATES closeout. Each of the three predecessor builds invalidates the
cache, and the release's first full run is COLD.** Against a sidecar written under the current
fingerprint, four mutations each force a full cold sweep, one at a time: `module_version`
0.15.0 → 0.16.0; `vlt-lint/SKILL.md:4`'s pin vector with `extraction@7` reverted to `@6`
(build-3); the same line with `decision-log@4` reverted to `@3` (build-4); and one character of
`pageScanPrompt`'s invariant half or of `PAGE_SCAN` (build-1). Each yields
`files_cached: 0` and a `lint_cache:` line reading `cold (fingerprint changed)`. **Instrument:**
the brief's Verification-5 harness plus a fingerprint-recomputation probe over the four mutated
inputs, at rest. **Evidence:** the four fingerprints and the four cold lines recorded.

**(4) `[ship-verifiable]` — GATES closeout. The release gate and the honesty surfaces survive
the build.** `uv run tools/package-lint.py --expect-version 0.16.0` exits **0** with **C6**
green against the re-derived `vault-rule-card.md` sha and **E6** showing `PAGE_SCAN` unchanged
at **3598**; both version strings read `0.16.0`; the B10-12 refusal still fires on a stale-copy
simulation (Verification V4a) and does **not** fire on a fully-cached run (V4b); and
`coverage_caps` is unchanged in count (A16). **Instrument:** `package-lint`'s own D/C6/E6 run
plus Verification V4 and V10's greps, all at rest. **Evidence:** the PASS summary line, the new
contract sha and card byte count, and the V4 returns.

**(5) `[field-contingent]` — does not gate. The saving is real at live churn.** On the first
full lint after the vault is upgraded to this release, the run **after** the release's cold run
reports `files_cached` materially greater than `files_checked` at comparable `pages_total`, and
`cost_accounting.phases[Scan pages].agents_dispatched` falls proportionally against the
2026-08-24 baseline of 146. **Event:** the owner runs `vlt-lint --full` on `{field-vault}`
**twice** after upgrading it to v0.16.0 — the first is the stated cold run, the second is the
measurement. **Performer:** the owner (standing rule — the owner runs upgrades and field runs).
**Vault:** `{field-vault}` only; it is the sole install with a 146-page wiki and a measured
churn history. **Bound:** the second full lint after the release, no later than Cycle 13's
`inbox-capture`. *Stated honestly: this is the number direction 2 exists for, and it
deliberately gates nothing — a fixture proves the mechanism, only the field proves the ratio.*

**(6) `[field-contingent]` — does not gate. The v0.16.0 rule-change notification actually
renders.** On the `{field-vault}` upgrade to v0.16.0, `vlt-upgrade`'s report's
`governance_rule_changes:` renders non-empty and carries all four facts F6 requires — the
Layer-3/`extraction@7` entry-condition change with the `writers:`/undeclared-is-`open`
consequence, `para_writer_unauthorized`, `decision-log@4`'s `kind: parked-interim`, and the
named retirement — sourced from this build's CHANGELOG entry rather than from a diff.
**Event:** the owner's `vlt-upgrade` run on `{field-vault}` crossing 0.15.0 → 0.16.0.
**Performer:** the owner. **Vault:** `{field-vault}` (the only install crossing this boundary
from 0.15.0). **Bound:** that upgrade run, no later than Cycle 13's `inbox-capture`. *This is
the first live exercise of build-3's F11 key and the only check that proves F6 was written as a
functional input rather than as release prose.*

---

## Grounding corrections issued at brief time — build-2

Two, taking the cycle's running total to **fifteen**. Both are written back into the roadmap as
superseding notes.

1. **The cache key's pin vector (roundtable A10).** A10 says *"the convention `version:` pins …
   the scan was judged under"*, which reads as the workflow's own `// depends_on:` line
   (`vlt-lint-full.js:12`). At HEAD that line does not contain `extraction` at all, so it does
   **not** move on build-3 — the very build the roundtable ordered build-2 to queue behind. The
   pin vector of record is **`vlt-lint/SKILL.md:4`**, which carries both `extraction@7` and
   `decision-log@4`. Superseded in F1; the finding A10 made is unchanged and the ordering ruling
   stands — only the mechanism's input is corrected.
2. **`checks.md:49` → `checks.md:50` (roundtable A14).** The quoted clause (*"never prior lint
   reports…"*) is in the **Spec candidates** bullet, which build-3's catalog work moved to
   `:50`; `:49` at HEAD is the personalized-extraction firewall. Superseded in disposition 4.
   *(Third cite-drift class this cycle to be caught by re-grounding at brief time, and the
   second one caused by a sibling build in the same release.)*

Every other cite this brief rests on was re-derived at HEAD and **held**, including all three
of build-4's restated moved lines (`vlt-upgrade` `:113`, `:126`, `:134`) and the contract's
`:349` derive-first clause.

---

## Next lifecycle move

A **fresh builder session** implements this brief via `bmad-workflow-builder`. Its exit
obligations: rewrite this brief's `status:` to a **BUILT** record with **numbered deviations**,
delete any `.decision-log.md` from the working tree, one commit on `cycle12-v0.16.0` — and
**stop before the tag**. The cycle is then **release-ready** and the release is **held for the
owner's explicit approval**: `release vlt 0.16.0` (`vlt-release`).

**Owner acts carried to the release, not performed here:** re-grade **A46** — it grades A12-5's
module side *"BLOCKED (unreachable) until A33's `governance_rule_changes:` key exists"*, and
**build-3 shipped that key** (`vlt-upgrade/SKILL.md:111`), so the grading is stale and the
platform item **`P-17`** needs re-grading. **Two briefs have now flagged this and nobody has
acted on it.** Also outstanding at release: hand-deliver build-3's re-derive notice to
`{field-vault}`'s known PARA park (A57), and the parked-interim survey (E6, bounded to before
Cycle 13's `inbox-capture`).

---

## Build-time verification record (V8 / V9, run at rest 2026-08-25)

**V8 — R4 enumeration widening, audited.** The build adds one new vault-local file class
(`_agent/lint-cache.yaml`). Dispositions, each checked on disk:
- the contract's **Decay contracts table** — **WIDENED** (F5, a declared *exempt* row placed
  after the `{upgrade_reports}` row); the closing rule at the table's foot demands the row only
  of accumulators, so this is a declared exclusion rather than a silent omission.
- `vlt-vitals.py`'s structure map and wake-read metrics — **declared outside**: disk-side,
  never wake-read, exactly as `{lint_reports}` is. No edit; grep confirms no reference.
- `full-scale.md` step 1's `crossLayerSlugs` predicate — **no edit needed by construction**: the
  `_agent/` zone root is walked recursively and the file joins as an ordinary link target.
- `vault_structure` / `module.yaml` / `vlt-setup` — **declared outside** (disposition 1: a fixed
  agent-zone path, not a map key). Verified: neither file names the sidecar.

**V9 — R3 legal response: NOT APPLICABLE, stated.** The build adds **no finding class**.
`lint_cache:` is a coverage line and `files_cached` is a count; neither is a finding, so no
legal response is owed. The absence is an answer, not an omission.

**V10 — cross-file greps (run):** `lint-cache` mechanics appear in exactly **one** place
(`full-scale.md`), with short pointers at `vlt-lint/SKILL.md` Step 6, the contract's Decay row
and two workflow comments — no second statement of the fingerprint's definition.
`files_cached` appears in the workflow (2), `report.md` (3) and `full-scale.md` (2).
`grep -c "files_checked: 0" skills/vlt-lint/references/full-scale.md` → **0** (narrowed, not
left beside its replacement). `coverage_caps` count in the workflow → **4**, unchanged from
HEAD (A16: nothing removed). `shasum -a 256` of the edited contract =
`265922bb1caa2dd984df9f06fcea42f98a4622e2ef84543c68a168e3a2fcbe88` = the card's stamped value.

**V12 — durability posture:** `git diff HEAD -- skills/vlt-upgrade/` is **empty** — the B1
local-mint preserve path is byte-identical and no own-the-apply copy path was touched. The
sidecar is vault-written and never named in the copy surface, so an upgrade cannot overwrite it.

**V13 — scrub:** no machine paths, username or vault-local artifact paths in any changed
shipped file or in `CHANGELOG.md` (grep clean).

**V14 — no `.decision-log.md`** anywhere in the working tree (`find . -name .decision-log.md
-not -path './.git/*'` → empty). `_agent/mint/decision-log.md`-shaped vault artifacts were not
touched.
