---
title: 'Build #2 — the findings cache: write-ready records, an in-workflow composed key, and an executable sidecar writer (the cache shipped two releases ago and has never once worked)'
status: >
  BUILT 2026-08-27 — every F-site landed; **7 of 8 acceptance checks are gradeable at rest and all
  7 PASS**; (8) is field-contingent, does not gate, and is UNFILLED by construction (it needs two
  consecutive `{field-vault}` sweeps under an unchanged ruleset, per A26). Version bump NOT taken —
  it belongs to the release step (`vlt-release`). Branch `cycle14-release2`.

  **Sites changed.**
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (767 → 870 lines): `:50-55` the `cachedScans`
  arg doc re-pointed at `_agent/lint-cache.json` read through `lint-cache.py`, records named as the
  previous run's returned `cache_records`; `:56-70` `rulesetFingerprint:` retired as an arg and
  replaced by the `rulesetComponents:` named-slot contract (F1 edit 1); `:114` reads
  `rulesetComponents` off the PARSED `a` with the object-and-not-array shape `:112` uses
  (F1 edit 2, the `:72-77` runtime contract intact); `:250-282` the composition — `RULESET_SLOTS`,
  `rulesetSlotsMissing`, `composeRulesetFingerprint()` and `const rulesetFingerprint`, sited
  immediately after `scanFingerprint` so both halves read together, commented with **why the
  composition is here and the component digests are not** (F1 edit 3); `:291-295` the `runKey`
  comment extended — three terms unchanged in shape, third term's provenance moved, `scanFingerprint`
  stays a term and why (F1 edit 4); `:297-305` `cacheRecordsRead` / `cacheRejected` with step 2's
  *stated in the report* mandate named as what they enforce (F1 edit 5); `:319-325` the
  incomplete-components coverage cap (deviation 2); `:426-450` `cacheRecords` built after the
  `outbound_links` normalization pass, keyed on `p.slug`, fresh and reused through one code path,
  emitted only when `pageHashes[p.slug]` and the composed fingerprint are both non-empty
  (disposition 3, F1 edit 6); `:855-870` the return — `fresh_scans:` **retired**, `cache_records:`,
  `cache_records_read:`, `cache_rejected:` added, `cache_fingerprint` unchanged, the READ-ONLY
  sentence kept and extended with the write-ready clause.
  **NEW shipped file:** `skills/vlt-lint/scripts/lint-cache.py` (F2) — the module's first `vlt-lint`
  script and `skills/vlt-lint/scripts/` its first script dir. PEP 723, `requires-python = ">=3.9"`,
  **no dependencies**; `read` exits 0 for ok/missing/unparseable alike; `write` is temp-file +
  `os.replace`, deletes a legacy `_agent/lint-cache.yaml` and reports `legacy_removed`; both modes
  print one JSON object; the docstring names its two callers and declines to duplicate the `:245`
  record predicate.
  `skills/vlt-lint/references/full-scale.md` (F3, build-2 owns the file): `:8` step 2 — the
  *"a digest over, in this order"* clause **retired outright** (A40) and replaced by the component
  contract with the digests as executable steps (`shasum -a 256`, base-then-overlay, UTF-8, first
  16 hex lowercase), the read command line, the *order does not matter, the workflow sorts* clause,
  the composition pointed at `vlt-lint-full.js` rather than restated, the standing cold-run mandate
  kept **verbatim** with one clause naming its two instruments; `:9` step 3 — `rulesetFingerprint`
  → `rulesetComponents` in the arg list **and** in the resume clause; `:12` step 5 — the write
  command line, `cache_records` as what is written, A6's reason stated, the legacy-deletion clause,
  every kept clause (rewritten-whole, facts-never-verdicts, not-a-report, safely-deletable) intact,
  and the report-composition rule extended with `cache_records_read` / `cache_rejected`.
  Untouched, as briefed: step 1's `crossLayerSlugs` predicate, step 4 in full, `:13`.
  `skills/vlt-lint/references/report.md` (F4): `:77` the rejected pair added to **both** the warm
  and the cold branch; `:88` the Findings-cache paragraph extended — never omitted, `rejected 0` on
  a cold run means no records were read. `:3` and `:13` untouched (build-4's).
  `skills/vlt-lint/SKILL.md:74` (F5): the **cache sentence only** — `.yaml` → `.json` plus
  *written by `scripts/lint-cache.py`*. The persist sentence on the same line is byte-identical
  (build-4's).
  `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:325` (F6): the Decay row's
  key becomes `` `_agent/lint-cache.json` ``; the exemption's reasoning is byte-identical.
  `skills/vlt-setup/assets/governance/_meta/vault-rule-card.md:11` (F6): `derived_from:` re-stamped
  to `sha256:990faf0a95eea68c1159ad658cc67ce9d4fa89b5fbc77171b7e999d8d8dc77ae (derived 2026-08-27)`;
  body unchanged, `RULE_CARD_BUDGET` not approached.
  `skills/vlt-setup/assets/module.yaml:88-89` (F7): the `uv` row's `needed_by:` widened to name
  vlt-lint's findings-cache script; `absent:` widened with the never-fails-because-its-cache-did
  clause. No new `machine_tools` row.
  **New factory records (never copied into a vault):**
  `factory/cycles/14-no-enforcement-point/lint-cache-roundtrip.mjs` (V1/V2) and
  `factory/cycles/14-no-enforcement-point/lint-cache-documented-invocation.mjs` (V3).

  **Verification, actually run.**
  **V1/V2 — `node factory/cycles/14-no-enforcement-point/lint-cache-roundtrip.mjs`: ALL CHECKS
  PASS.** The shipped workflow source (stubbed `agent`/`parallel`/`phase`/`log`/`budget`, `args`
  delivered as a JSON **string**) and the shipped `lint-cache.py` as a **subprocess** for every read
  and every write against a real temp vault dir. **Nothing on the write path is stubbed** — that is
  the whole repair. Six-page corpus. Run 1: `status=missing read=0 | files_checked=6 files_cached=0
  files_listed=6 cache_records=6 cache_records_read=0 cache_rejected=0 | written=6`. Run 2:
  `status=ok read=6 | files_checked=0 files_cached=6 files_listed=6 cache_records=6
  cache_records_read=6 cache_rejected=0 | written=6`. Run 3: identical to run 2, and the sidecar
  file compares **byte-for-byte equal** to run 2's — which is also the proof of `normalizeTarget`
  idempotence (the stored `outbound_links` are the normal form, deviation 6). One reused record
  verbatim: `{"slug":"alpha","key":"sha256-alpha-0|225f762e874613e61b05|af7e8840f80e6a94b9","scan":{…"outbound_links":["zeta"]…}}`.
  Negatives: a `PAGE_SCAN` differing by one character → `files_cached=0 files_checked=6
  cache_rejected=0` and a different middle key term (`de4e2b3e77b9da241b06`); one changed ruleset
  component → `files_cached=0` and a different third term (`681eef8090a59f8cb9`); neither changed →
  `files_cached=6`. Ordering: the same components with shuffled keys compose the identical
  `cache_fingerprint` `225f762e874613e61b05|af7e8840f80e6a94b9`. Completeness: a components object
  missing two slots → `cache_fingerprint: null`, `files_cached: 0`, `cache_records: 0`, and the cap
  *"findings cache cold: rulesetComponents incomplete — absent or empty slots [pin_vector,
  checks_digest]; no page was reusable this run"*. Flat pre-repair sidecar (the field's own shape),
  **cold branch**: `cache_records_read=6 cache_rejected=6 files_cached=0`; **warm branch including
  zero**: `cache_records_read=6 cache_rejected=0`; mixed 3+3 sidecar: `read=6 rejected=3 cached=3`.
  A page with no `pageHashes` entry produces **no** record. The writer deleted a seeded legacy
  `_agent/lint-cache.yaml` and reported `legacy_removed: true`.
  **V3 — `node factory/cycles/14-no-enforcement-point/lint-cache-documented-invocation.mjs`: ALL
  CHECKS PASS.** Both command lines extracted verbatim from `full-scale.md` and executed (deviation
  3): missing → `exit 0 {"status": "missing", …}`; corrupt → `exit 0 {"status": "unparseable", …}`;
  the documented write → `exit 0 {"written": 1, "path": …, "legacy_removed": false}`; read-back →
  `exit 0 {"status": "ok", … "count": 1}`.
  **V4 — retirements.** `grep -rn "fresh_scans" skills/` → **0**.
  `grep -rn "a digest over, in this order" skills/` → **0**. `lint-cache\.yaml` → 2 hits, both the
  legacy-deletion mechanism itself (deviation 1); excluding those, **0**. Survivors present: the
  reader filter `c && c.slug && c.key && c.scan` (1), the READ-ONLY sentence (1), step 4's
  version-skew defence (1). `node --check` and `python3 -m py_compile` both clean.
  **V5 — E6, measured with package-lint's own `_E6_NODE_EXTRACTOR`, never a source char count:**
  `PAGE_SCAN` **3688** (budget 3700) — unmoved from build-1. `INDEX_SCAN` 823, `CLUSTER_FINDINGS`
  1630, `PAIR_FINDINGS` 376.
  **V6 — manifest coverage, verified not assumed:** `verify-skill-manifest.py --write` against a
  temp root wrote 34 entries including `.claude/skills/vlt-lint/scripts/lint-cache.py`. No widening
  owed (structural scope holds for a new `scripts/` dir).
  **Packaging lint** — `uv run tools/package-lint.py` → `A/B/C/E PASS, D SKIPPED — vlt 0.16.2`,
  exit 0. **C6 isolated: PASS** (rule card re-stamped). **E6 isolated: PASS.** Handshake Group E
  passes and nothing was owed in substance (no `version:` moved, the `:11` ack untouched).
  **Scrub** — no personal or vault-local content in any changed file; `find . -name
  ".decision-log.md"` → nothing; no `__pycache__`/`.pyc` left.

  **Deviations (numbered).**
  1. **V4's retirement grep is not literally zero and cannot be.** The brief's command
  `grep -rn "fresh_scans\|lint-cache\.yaml\|a digest over, in this order" skills/` returns two
  `lint-cache.yaml` hits: `scripts/lint-cache.py:49` `LEGACY = "lint-cache.yaml"` and
  `full-scale.md:12`'s clause saying the script removes it. Both are **required by disposition 1** —
  the writer deletes the legacy file **by name**, so the name must exist in the shipped surface.
  Retirement 3 retires the `.yaml` as a **legal sidecar path**, and naming it as the file to delete
  is that retirement's own mechanism, not its survival. The grep is reported narrowed
  (`| grep -v "legacy\|LEGACY"` → 0); the other two terms return 0 unqualified.
  2. **The incomplete-components coverage cap is pushed a few lines below the composition, not at
  it.** The composition sits immediately after `scanFingerprint` as F1 edit 3 requires, but
  `coverageCaps` is not declared until the fan-out block. So the composition computes
  `rulesetSlotsMissing` and the cap is pushed at the first point `coverageCaps` exists, immediately
  above the overlay cap it mirrors. Behaviourally identical; the alternative was hoisting
  `coverageCaps` above a block that has been stable for four cycles.
  3. **V3 substitutes the doc's own placeholders before executing.** `$SKILL`, `{project-root}`,
  `<cache_fingerprint>` and `<path|->` are placeholders the Scrub rule *requires* the shipped prose
  to carry, so a literally-unsubstituted execution is impossible by construction. The harness
  substitutes exactly those four and alters nothing else — every flag name, order and quoting runs
  as written, which is what check (4) is about. It also fails if extraction finds anything but
  exactly two command lines.
  4. **V3 is a second durable harness file, not a section of V1's.** The brief names V3's instrument
  as "the extract-and-execute harness" with no path. It is
  `factory/cycles/14-no-enforcement-point/lint-cache-documented-invocation.mjs` — separate because
  its subject is the prose-to-executable seam, not the round trip, and it must be able to fail
  independently.
  5. **Two controls beyond the brief.** A **mixed** sidecar (3 well-formed + 3 flat → `read=6
  rejected=3 cached=3`) proves `cache_rejected` counts records rather than reporting a boolean; and
  a seeded legacy `.yaml` proves the writer's deletion clause. Additive, no scope moved.
  6. **The brief's grounding correction on the stored payload is CONFIRMED, and now proven.** The
  stored `outbound_links` are the normalized form (`["zeta"]` from `["[[zeta.md|alias]]"]`), not the
  scanner's verbatim extraction — build-1's brief disposition 6 is wrong on the letter, as this
  brief says. Run 3 ≡ run 2 byte-for-byte is the idempotence proof, so it is harmless.
  7. **The `status: 'failed'` near-total-shortfall return does NOT carry `cache_records_read` /
  `cache_rejected` / `cache_records`.** Stated rather than discovered: F1 edit 6 scopes the success
  return only, and step 4 refuses such a run before any report is written, so there is no report
  line for the pair to render into. Left as briefed.
  8. **The rule card's `last_updated:` was NOT moved**, only `derived_from:`. This matches every
  prior C6 re-stamp in this repo (`93797b9`, `853024b` both moved `derived_from:` alone) and the
  owner ruling that the card's body is unchanged.

  **Next:** `brief build 3` (ordered after this build so `PAGE_SCAN` settles once before the re-ack
  pass reads it — A3). Build-4 rebases its `full-scale.md` / `report.md` / `SKILL.md:74` edits onto
  this state and re-grounds; the edit surfaces are disjoint by sentence as F3/F4/F5 state.
module_code: 'vlt'
created: '2026-08-27'
derives_from:
  - 'factory/inbox/2026-08-26-141838-findings-cache-cannot-round-trip-writer-and-reader-disagree.md (A14-8 — Defect 1 the sidecar schema mismatch, Defect 2 the non-deterministic rulesetFingerprint, and the GAP: no instrument can see either)'
roadmap: 'factory/cycles/14-no-enforcement-point/roadmap.md'
rulings: >
  roadmap §Ideation rulings (2026-08-26): Q6 (remove both seams — write-ready `{slug, key, scan}`
  records; the fingerprint's COMPOSITION moves into the workflow, components stay SKILL-side; the
  round-trip check ships and GATES; the step-4 refusal predicate is NOT widened) as amended by
  roundtable A7 (component digests single-homed as executable steps or half of Defect 2 survives)
  and A40 (step 2's ordering clause is RETIRED with the move, not left beside it); Q1 (build-2
  caches build-1's structured `PAGE_SCAN` return — roundtable A4); Q5 (`.json` is a legal persist,
  on the corrected reason — A9) as extended to the sidecar by roundtable A7b; D3 as amended by
  A17/A17b (bounded ⇒ ship-verifiable ⇒ GATES; where an at-rest instrument is buildable in scope
  the brief MUST build it) + rule R1 (every ship-verifiable check names the seam its instrument
  crosses); §Grouping & order build-2 block incl. A4 (depends on build-1; `scanFingerprint` stays a
  term of the composed key), A5 (three runs, executable writer), A6 (fresh AND reused records),
  A8 (`full-scale.md` shared with build-4 — one brief owns it), A26 (two cold sweeps), A39
  (`cache_rejected:`).
risk: >
  moderate — no convention `version:` moves and no consumer walk is owed, but the build changes the
  workflow's return shape, adds the module's first shipped `vlt-lint` script, renames a
  vault-side file that the governance contract's Decay table enumerates by literal path (so
  package-lint C6 must be re-satisfied), and is the repair of a mechanism that shipped in Cycle 12
  on a green ledger and has never once worked.
---

# Build #2 — the findings cache: write-ready records, an in-workflow composed key, an executable writer

## Intent

Cycle 12 shipped a findings cache. It has **never once worked**. A14-8 grounded three faults:

1. **The writer and the reader disagree.** The reader requires `{slug, key, scan}`
   (`vlt-lint-full.js:245`, `:346`); `full-scale.md` step 5 tells the SKILL to write the workflow's
   returned `fresh_scans`, which is the array of raw `PAGE_SCAN` returns (`:295`, `:766`) — no
   `key`, no wrapper. **Following the spec literally produces a sidecar the reader discards whole.**
2. **`rulesetFingerprint` has no deterministic algorithm.** `full-scale.md` step 2 enumerates the
   inputs and specifies no separator, no hash algorithm, no encoding, no truncation. The field
   observed `980d749d9acf418e` against `66d27a0e6cd8fabe` over a provably unchanged ruleset.
3. **Nothing checks that a cache written by run N is readable by run N+1.** A run that cold-scans
   because the cache is broken reports `files_checked: 146` — full coverage, honest report, no
   refusal, indistinguishable from a healthy cold run.

This is the cycle's through-line at its cleanest: a contract stated once in code and restated as
prose somewhere else, **with no enforcement point where the two meet**. This build removes both
seams rather than documenting them, and — the part b2(5) got wrong — it builds the instrument that
can see the seam, with the write step **executable** rather than stubbed.

**Build-2 DEPENDS on build-1; it is not independent of it** *(roundtable A4)*. The `scan` payload
this build caches **is** build-1's structured `PAGE_SCAN` return, and `scanFingerprint` (`:235`,
derived from `pageScanPrompt(…) + JSON.stringify(PAGE_SCAN)` at `:234`) is a key component build-1
moved. Every fixture in this build is built against **post-build-1 source at v0.16.2**, never
against the pre-build-1 schema; a fixture built against the old schema would ship a gating check
proving the wrong shape round-trips. **The composition move MUST keep `scanFingerprint` a term of
the composed key** — the SKILL supplies only the ruleset-side components — and acceptance check (2)
asserts that a record keyed under a different `PAGE_SCAN` is not reusable.

**⚠ The first full lint after release 2 is COLD BY CONSTRUCTION, and that is not a cache
regression.** Build-2 rewrites the sidecar's record shape *and* its filename; build-3 moves two
convention digests; build-4 moves `checks.md`'s. Every one of those invalidates every record. Say so
in the release note. **Release 1 already forced one cold sweep** — this cycle knowingly costs two
(roundtable A26). Per A26, `{field-vault}`'s owed COMPLETE sweep is paid on the **second** sweep
after release 2, not the first, and **build-2's cache repair cannot be field-confirmed until two
consecutive sweeps under an unchanged ruleset** — which is why acceptance check (8) is the only
field-contingent check in this brief and why it deliberately does **not** gate.

**All rejected alternatives in the parent filing are settled — do not re-litigate.** Specifically:
A14-8 direction 4 (document the key derivation in `full-scale.md` instead of moving the wrapping)
is rejected by Q6.1 — the wrapping moves. A14-8 direction 5 (widen the step-4 refusal predicate) is
**declined** by Q6 with its reason on record: the round-trip check is a direct instrument for the
failure the predicate would only infer, and step 4's version-skew refusal detects a stale
vault-local workflow copy, which the round-trip cannot observe (roundtable obsolescence beat,
negative 4). **The step-4 predicate is not touched by this build.** And "move
`rulesetFingerprint`'s *computation* into the workflow" is **not** the scope: the workflow cannot
read files (`:26-28`), so the SKILL computes the component digests regardless — **what moves is the
composition** (Q6.2's in-session correction; a brief must not scope it as computing the fingerprint
in the workflow).

## Brief-time dispositions

### 1. The sidecar's format — RULED: `.json`, and it is the sidecar's only legal format

*Derives from: roundtable A7b (Q5's format reasoning applies to the sidecar too — "the brief rules
whether `_agent/lint-cache.{yaml,json}` follows Q5's `.json` permission"); Q5 as amended by A9.*

**Ruled: the sidecar becomes `_agent/lint-cache.json`, and `.yaml` ceases to be legal for it.**

A7b is right that two rulings in one cycle were reaching opposite conclusions on the same problem,
and that **the one that GATES got the harder format.** The asymmetry is now larger than A7b priced,
because disposition 2 makes the sidecar's writer an **executable script** rather than an LLM's hand
emission:

- `json` is Python stdlib; `yaml` is not. (This is the argument A9 **struck** for the *report*,
  because `uv`'s declared purpose is *"PEP 723 inline deps"* — a dependency route that exists. It
  is struck as a claim about `machine_tools` cost, not as a claim about stdlib membership.) For the
  sidecar the argument returns in a form A9 does not reach: a **YAML writer** would either take a
  `pyyaml` dependency (a resolution step in the middle of every full sweep) or hand-roll a second
  serializer — **a second emitter to get wrong, in the build whose whole subject is two
  serializations of one contract disagreeing.**
- **`.json` is what makes check (1) exact.** A round trip over JSON asserts byte-level record
  identity across runs 2 and 3. A round trip over hand-emitted YAML asserts identity of whatever the
  emitter chose to do that run, which is the property that failed.
- The sidecar is **machine-only** by contract: never wake-read, never a report, deleting it costs a
  cold run (`vault-operating-contract.md:325`; `vlt-lint/SKILL.md:74`). The human-readability that
  Q5 preserves for the *report* (the fenced in-session block stays YAML) has **no** counterpart
  claim here — nobody reads this file.

**Unlike Q5's ruling for the report, this is not a permission — it is a replacement.** Permitting
two formats would double the reader's parse surface for a file that has exactly one reader and one
writer, both shipped in this build. One format, one writer, one reader.

**Migration: there is none, by construction** (Q6's closing ⚠). The existing
`_agent/lint-cache.yaml` stores `fingerprint:` once at top level and **no per-page digest anywhere**,
so it cannot express the reader's key even in principle. It is not converted, not read, and not
left behind: the writer script **deletes a legacy `_agent/lint-cache.yaml` when it writes the JSON
sidecar**, and reports that it did. Leaving it would strand an unowned file at a path the Decay
table no longer covers (disposition 6) — this cycle's shape, one file over.

### 2. The writer is EXECUTABLE — a shipped script, not SKILL-side prose. RULED, and this is A5(b)'s question answered

*Derives from: roundtable A5 (b) — "the brief must either move the sidecar **write** into a shipped
script so the round trip runs end-to-end, **or** record that the SKILL-side serialize/merge step is
**not** covered and tag a second check for it. A round trip that stubs the writer does not discharge
A14-8 and must not be tagged ship-verifiable under D3." Also D3 as amended by A17b clause 1.*

**Ruled: build the writer.** A14-8's own capture records why b2(5) shipped broken — *"a two-run temp
fixture inside one harness invocation, where the SKILL-side write step never ran because the harness
stubbed it."* After Q6 the write side would **still** be SKILL-side prose (`:762-766`: *"This
workflow stays READ-ONLY — it returns the records, the SKILL persists them"*), so a JS round trip
would grade workflow-return → workflow-consume and **stub exactly the seam that broke**. Taking
option (b) — declaring the seam uncovered and watching it — would leave the only gating instrument
blind to the only thing that has ever failed.

D3's amended clause 1 settles it independently: *"Where a check's subject is gradeable at rest by an
instrument buildable inside the build's own scope, the brief **must build it**. Declining is a
written justification in the brief, never a tag choice."* A stdlib-only serializer/parser is
squarely inside this build's scope. So it is built.

**`skills/vlt-lint/scripts/lint-cache.py`** — the module's first `vlt-lint` script; two modes,
stdlib only:

| mode | contract |
|---|---|
| `read --vault-root <abs>` | prints one JSON object to stdout: `{"status": "ok"\|"missing"\|"unparseable", "reason": "<words>", "records": [...], "count": N}`. **Exit 0 in all three cases** — a missing or unparseable sidecar is a cold run, never an error (`full-scale.md` step 2's standing mandate, which this build finally gives an executable home). |
| `write --vault-root <abs> --fingerprint <cache_fingerprint> --records <path\|->` | writes `_agent/lint-cache.json` **whole** (temp file + atomic rename), removes a legacy `_agent/lint-cache.yaml` if present, prints `{"written": N, "path": "…", "legacy_removed": true\|false}`. |

**The workflow stays READ-ONLY.** The script is the SKILL's hands, not the workflow's — the
read-only property at `:762-766` is preserved verbatim and is *why* the sidecar needs an executable
writer somewhere other than the workflow.

**The script does NOT re-validate the record schema.** The reader-side filter at `:245` is the
single home of what makes a record usable, and `cache_rejected` (disposition 5) is its instrument.
A write-side copy of the same three-key predicate would be a second statement of one contract — the
defect this build exists to remove. The workflow constructs every record it returns, so records
reaching the writer are well-formed by construction.

**Invocation form** — `uv run --quiet "$SKILL/scripts/lint-cache.py" …`, matching every shipped
script (`vlt-setup/SKILL.md:90`, `:96`, `:156`; `vlt-upgrade/SKILL.md:58`), with a PEP 723 header
declaring `requires-python` and **no dependencies**. `uv` is already declared in `machine_tools`
(`module.yaml:87-89`); its `needed_by:` text is widened in this build to name vlt-lint's cache
script (disposition 6). **Degradation is loud and non-fatal:** if either mode fails, the sweep
continues, the sidecar is not written, and the report's `lint_cache:` line renders
`cold (<reason>)` — a lint sweep never fails because its cache did.

**What this check still does NOT cover, stated rather than discovered** (A5's honesty requirement,
answered even though option (a) was taken): the SKILL **invoking** the script, and **transcribing**
the returned records into `workflow(...)` args at 146-page scale. Acceptance check (4) closes the
first half at rest by executing the command line **extracted verbatim from `full-scale.md`**. The
second half — inline transcription — is structural to the shipped design (the workflow has no
filesystem access, `:26-28`; the `argsPath` route is tracker #13, deferred by Q2) and is
**out of scope**, named at §Out of scope item 4, watched by field check (8), and made *visible* by
`cache_rejected` (disposition 5), which is exactly what a transcription failure would move.

### 3. The record shape and the key — `{slug, key, scan}`, for every adjudicated page, fresh AND reused

*Derives from: Q6 ruling 1; roundtable A6 ("Q6.1 as ruled fixes only HALF the sidecar"); A4.*

**Ruled: the workflow returns `cache_records: [{slug, key, scan}]` — one record per page adjudicated
this run, fresh **and** reused — and `fresh_scans:` retires with it** (disposition 7).

A6 is the load-bearing half. `:766` returns fresh records only; `:249`'s `reused` surfaces solely as
the count `files_cached` (`:673`); and `full-scale.md` step 5 tells the SKILL to write back *"the
reused records that are still valid"* — where validity is `key === runKey(slug)` and `runKey`
(`:244`) embeds `scanFingerprint`, **a workflow-internal value the SKILL structurally cannot
compute**. So the shipped spec asks the SKILL to re-derive a reusability judgment it cannot make.
**The SKILL is never asked to re-derive reusability. It writes what it is handed.**

- `slug` is **`p.slug` from the page list** — the SKILL-supplied slug, never the agent-returned
  `s.slug`. The key's first term is `pageHashes[p.slug]`; keying a record by an agent-returned
  string would let a scanner's typo poison a page's cache line.
- `key` is `runKey(p.slug)` for **every** record. For a reused page the recomputed key is by
  definition equal to the reused record's key (that is what made it reusable), so one code path
  serves both halves — there is no fresh/reused branch to keep in agreement.
- `scan` is the record the reduce actually adjudicated (`:346`'s `rec`).
- **A record is emitted only when `pageHashes[p.slug]` and the composed `rulesetFingerprint` are
  both non-empty.** Otherwise the key is degenerate (`|scanFp|`) and writing it stores junk that can
  never hit. On a cold run with no components the sidecar is rewritten with `records: []` — still
  *"rewritten whole, never appended to"*.

**Grounding correction — the stored payload is NOT byte-verbatim, and the roadmap and build-1's
brief both imply it is.** `:356` mutates the scan objects in place
(`for (const s of scans) s.outbound_links = (s.outbound_links || []).map(normalizeTarget)…`), and
`freshScans` holds those same object references. So whatever this build returns for the sidecar
carries **normalized** `outbound_links`, not the scanner's verbatim extraction — including today,
for `fresh_scans`. Build-1's brief disposition 6 states the opposite (*"`scans` records are what
build-2 will persist to the sidecar as verbatim `PAGE_SCAN` returns"*), and it is wrong on the
letter. **It is harmless and it is now asserted rather than assumed:** `normalizeTarget` (`:81-87`)
is idempotent — a second pass over an already-normalized target strips nothing further — so a stored
record adjudicates identically on the next run. Acceptance check (1)'s run-2 ≡ run-3 identity
assertion is precisely the proof of that idempotence, and it is why the fixture is three runs and
not two for a second, independent reason.
**Build the record array where the return is composed** (after `:356`), from the page list, so the
stored payload is exactly the payload the reduce adjudicated — one site, no snapshot to keep in
sync.

### 4. The fingerprint composition — a NAMED-SLOT object, not a list and not a pre-joined string

*Derives from: §Questions deliberately left to brief time → build-2 ("whether the SKILL passes
fingerprint components as a list or a pre-joined string"); Q6 ruling 2 and its in-session
correction; roundtable A7 and A40.*

**Ruled: neither. The SKILL passes `rulesetComponents`, an object with named slots.**

```
rulesetComponents: {
  module_version:      string,             // the installed module_version
  pin_vector:          string,             // vlt-lint's own depends_on: pin vector, verbatim
  convention_digests:  { <name>: digest },  // merged (base + overlay) digest per convention judged
  checks_digest:       string,             // references/checks.md merged digest
}
```

**Why not a list.** A positional list re-creates the ordering contract in prose — the SKILL would
have to know which slot goes where, stated in `full-scale.md`, executed in the workflow, with
nothing where the two meet. That is A14-8's exact shape, and A40 retires the sentence that states it.

**Why not a pre-joined string.** That leaves composition SKILL-side, which is the defect Q6.2 moves.

**The workflow composes, and the canonical order is code, not prose.** In the workflow:
`module_version`, then `pin_vector`, then every `convention_digests` entry as `name=digest` with
**names sorted lexicographically**, then `checks_digest` — joined with `|`, then digested with the
same `fnv1a`-pair-plus-length construction `scanFingerprint` uses (`:226-235`). No crypto import
exists in the workflow and none is needed: this half only has to change whenever its inputs change;
**the strong digest is the SKILL's**, and disposition 5's `full-scale.md` rewrite is what makes the
SKILL's half deterministic. A caller passing the same components in a different key order composes
the identical value — asserted by acceptance check (5).

**Completeness is enforced, not assumed.** Any slot missing or empty ⇒ `rulesetFingerprint = ''` ⇒
`reusable()` (`:246-247`) is false for every page ⇒ a cold sweep, **with a named `coverage_caps`
entry** saying which slots were absent. This is the same loud-degrade posture the file already
carries for absent overlay args (`:259-264`).

**`scanFingerprint` stays a term of the composed key** (A4's interface, stated rather than assumed):
`runKey` (`:244`) is unchanged in shape — `${pageHashes[slug]}|${scanFingerprint}|${rulesetFingerprint}`
— and only its third term's *provenance* moves. `cache_fingerprint` (`:765`) likewise stays
`${scanFingerprint}|${rulesetFingerprint}`. **Do not fold `scanFingerprint` into the components
object**: it is workflow-internal by construction (the SKILL cannot compute it — that is A6's whole
point), and dropping it would make a sidecar written under one `PAGE_SCAN` reusable under another.
Acceptance check (2) exists to fail if it is dropped.

### 5. `cache_rejected:` — the enforcement point for a mandate that already exists

*Derives from: roundtable A39.*

**Ruled: the workflow returns `cache_records_read` and `cache_rejected`, and `report.md`'s
`lint_cache:` line renders both.**

`full-scale.md` step 2 **already mandates** that *"a missing, unparseable or schema-mismatched
sidecar is a cold run, **stated in the report** — never an error and never a silent full sweep
presented as a cached one."* That is this cycle's through-line verbatim, with no enforcement point,
and it is what failed in the field: 146 flat records were passed in, the `:245` filter discarded
every one of them, and the report said `cold` with no indication that a sidecar had been read and
thrown away.

- `cache_records_read` = `cachedScans.length`; `cache_rejected` = `cachedScans.length -
  cacheBySlug.size`. **The denominator ships with the count** — a bare `rejected: 146` is the kind
  of cardinality-without-a-referent `ST-5` names, and the report-composition rule
  (`full-scale.md:12`, `report.md:88`) forbids the SKILL from supplying the denominator itself
  (*"from the workflow's returned counts only"*).
- **Rendered always, including zero** — never omitted on a clean run. An absent field reads as
  "not measured"; `report.md:13`'s `unmeasured (no prior full report)` idiom is the file's own
  precedent for that distinction.
- The missing/unparseable half of the mandate is carried by the **reader script's** `status:` and
  `reason:` (disposition 2), which the SKILL renders into the `cold (<reason>)` branch.

**This is not the step-4 widening Q6 declined** — it adds no refusal, changes no predicate, and
costs no new argument. The round-trip check gates the **module at rest**; `cache_rejected` is what
makes a **vault's** own schema-mismatched sidecar visible on the run it happens.

### 6. R4 — enumeration widening. SUBSTANTIVE: renaming the sidecar moves it out of an enumeration

*Required by R4.*

Three enumerations meet this build; one is a hand-kept list and must be widened in the same build.

1. **The Decay contracts table — `vault-operating-contract.md:325`** enumerates
   `` `_agent/lint-cache.yaml` (the findings cache) `` **by literal path** and grants it its
   decay exemption. Rename the file and the new path has **no exemption** and the old row points at
   nothing. **Widened in this build** (F6). ⚠ **This is a governance-bundle edit and it is not
   free** (`brief-anatomy.md` §5): package-lint **C6** requires `_meta/vault-rule-card.md`'s
   frontmatter `derived_from: … sha256:` to be **re-stamped** against the edited contract. The
   card's distilled clauses do not change (the Decay table is not distilled into it — verified: the
   card's only decay row, `:52`, is the hygiene/safety-model line), so the re-derivation is a
   re-stamp, not a rewrite, and `RULE_CARD_BUDGET` is not approached. Do the re-stamp in this build;
   C6 fails the release otherwise.
2. **The skill-asset manifest** — `skills/vlt-lint/scripts/lint-cache.py` is a new shipped file. Its
   scope is **structurally derived**, not hand-kept: `verify-skill-manifest.py:129`/`:149` `rglob`s
   every shipped `vlt-*` skill tree whole (`SKILL.md`, `assets/`, `references/`, `scripts/`, *"and
   anything a future build adds"* — `:14`). **No widening is owed; the coverage is verified at build
   time** (Verification V6), not assumed — C6-d is on record as an instance of this exact scope
   question going wrong.
3. **`machine_tools`** (`module.yaml:83-95`) enumerates tool assumptions, not their consumers. `uv`
   is already a row; **its `needed_by:` text is widened** to name vlt-lint's cache script, so the
   absence story stays true. **No new row** — the `machine_tools` cost Q5 priced does not arise
   here.

### 7. Retirement clause (P-15) — three retirements, all in this build

*Derives from: roundtable A40 (named in the obsolescence beat as retirement 4) and Q6.1.*

| # | Retired | Site (re-grounded) | Because |
|---|---|---|---|
| 1 | `fresh_scans:` in the workflow's return | `vlt-lint-full.js:766` | superseded by `cache_records:` — it is the exact value `full-scale.md` step 5 mis-instructs the SKILL to write, and leaving it beside its replacement leaves the wrong write available |
| 2 | `full-scale.md` step 2's *"a digest over, **in this order**: …"* ordering clause | `full-scale.md:8` | **A40** — once composition moves into the workflow the clause describes an algorithm the SKILL no longer performs; left standing beside the implementation it **re-creates A14-8's exact shape**. Replaced by a component-list contract, **never amended to sit alongside** |
| 3 | `_agent/lint-cache.yaml` as a legal sidecar path | `full-scale.md:8`, `:12`; `vlt-lint/SKILL.md:74`; `vlt-lint-full.js:51`, `:763`; `vault-operating-contract.md:325` | disposition 1 — one format, and the legacy file is deleted by the writer rather than left unowned |

**SURVIVES — do not retire:** `full-scale.md` step 4's version-skew refusal predicate. It detects a
**stale vault-local workflow copy**, a failure the round-trip check cannot observe; the roundtable's
obsolescence beat returned this negative explicitly and Q6's decline of direction 5 stands on it.
Also surviving verbatim: the workflow's READ-ONLY property (`:762-766`) and the reader-side filter
at `:245` (disposition 2 declines to duplicate it).

### 8. R1 — interim posture. SUBSTANTIVE

*Required by R1 (a rule shipped ahead of its mechanism).*

The rule *"a missing, unparseable or schema-mismatched sidecar is a cold run, stated in the report"*
gets its enforcement point in this build (disposition 5). But between release 2 and the **second**
consecutive `{field-vault}` sweep under an unchanged ruleset, **no field evidence exists that the
cache hits at all** — release 2's own contents guarantee the first sweep is cold, and A26 defers the
owed complete sweep to the second. What a vault legally does in that window:

- **A `cold (<reason>)` `lint_cache:` line after release 2 is expected, not a defect.** It is not
  filed, not fixed, and not read as a regression. The reason string names which of the three causes
  fired.
- **`cache_rejected: 0` on a cold run is not evidence the cache works** — it means no records were
  read. The pair to look for is a warm run's `files_cached > 0` **with** `cache_rejected: 0`.
- **`files_cached: 0` never suppresses or softens any coverage cap.** The cache buys recomputation,
  never coverage (`:341-344`) — a cold sweep is a full sweep, and the report says so.
- The posture expires when acceptance check (8) is graded, on the second sweep after release 2.

## F-sites

All `file:line` below re-derived against the working tree at **v0.16.2 (`bd985a6`)** on 2026-08-27.
The roadmap's A14-8 capture and the build-2 block were written against **v0.16.1** and their cites
have drifted by build-1's +43 lines; the corrections are recorded at F1 and a superseding note is
appended to the roadmap's A14-8 capture. Bare `:N` below is
`skills/vlt-setup/assets/workflows/vlt-lint-full.js` (**767 lines**).

### F1 — `vlt-lint-full.js`: the composed fingerprint, the write-ready records, the rejected count

**Grounding correction — every cite in the roadmap's A14-8 capture and build-2 block has moved.**
Re-derived this run:

| the roadmap says | current source | what it is |
|---|---|---|
| `:243` reader filter | **`:245`** | `cachedScans.filter((c) => c && c.slug && c.key && c.scan)` |
| `:242` `runKey` | **`:244`** | `` `${pageHashes[slug] \|\| ''}\|${scanFingerprint}\|${rulesetFingerprint}` `` |
| `:244-245` `reusable` | **`:246-247`** | requires `pageHashes[p.slug]` **and** `rulesetFingerprint` **and** an exact key match |
| `:344` `.scan` deref | **`:346`** | inside the corpus-assembly loop `:345-348` |
| `:248` `reused` | **`:249`** | `pages.filter(reusable)` |
| `:293` pushes `r` | **`:295`** | `freshScans.push(r); freshBySlug.set(chunk[k].slug, r)` |
| `:722` `cache_fingerprint` | **`:765`** | |
| `:723` `fresh_scans` | **`:766`** | |
| `:719-723` the READ-ONLY comment | **`:762-766`** | |
| `:232-233` `scanFingerprint` | **`:234-235`** | `canonicalScan` `:234`, `scanFingerprint` `:235`; `fnv1a` `:226-233` |
| `:36-38` "no filesystem access" | **`:26-28`** | |
| `:47-49` `pageHashes` arg doc | **`:47-49`** | HOLDS |

Scope is unchanged by every one of these; only the numbers moved.

**Current state.** `:50-53` documents `cachedScans`, `:54-56` `rulesetFingerprint`; `:101` reads
`rulesetFingerprint` off the parsed args; `:240-249` is the key/split block; `:345-348` assembles
the corpus; `:356` normalizes `outbound_links` in place; `:668-767` is the return.

**The exact change — six edits, in this order.**

1. **`:54-56` → the new arg contract.** Replace the `rulesetFingerprint:` arg doc with
   `rulesetComponents:` per disposition 4's shape, stating: the SKILL computes the component
   digests (it has filesystem access, this script does not — `:26-28`); the workflow composes them;
   any slot missing ⇒ cold sweep with a named cap. **`rulesetFingerprint` is no longer an accepted
   arg** — it is composed, never passed. Also update `:50-53`'s `cachedScans` doc: the sidecar is
   `_agent/lint-cache.json`, and its records come from the previous run's returned `cache_records`.
2. **`:101` → read `rulesetComponents`** off the parsed `a` (the same defensive shape as `:99-100`:
   object-and-not-array, else `{}`). **Read from the PARSED `a`, never the raw `args` string** — the
   standing runtime contract at `:72-77`.
3. **Compose the fingerprint, immediately after `:235`** (`scanFingerprint`, so both halves sit
   together and the comment at `:218-224` reads across them). One helper: canonicalize per
   disposition 4 (module_version, pin_vector, lexicographically-sorted `name=digest` pairs,
   checks_digest, joined `|`), then the same `fnv1a`-pair-plus-length construction. Empty/missing
   slot ⇒ `rulesetFingerprint = ''` **and** a `coverageCaps` push naming the absent slots (mirroring
   `:259-264`). Comment it with **why composition is here and the component digests are not**
   (Q6.2's correction, so no later reader re-derives the wrong scope).
4. **`:244-249` → unchanged in substance, re-commented.** `runKey`'s three terms stay exactly as
   they are (A4). Extend the `:240-243` comment by one clause: the third term is now **composed
   here** from SKILL-supplied components, so two conformant executors cannot disagree.
5. **After `:245`'s filter → the rejected count.** `const cacheRecordsRead = cachedScans.length` and
   `const cacheRejected = cacheRecordsRead - cacheBySlug.size`, with a comment naming step 2's
   *"stated in the report"* mandate as what these exist to enforce (A39).
6. **`:762-766` → the return.** Keep `cache_fingerprint` as is. **Replace `fresh_scans: freshScans`
   with `cache_records:`** — built here (after `:356`, per disposition 3) by walking `pages`,
   taking `rec` the same way `:346` does, emitting `{ slug: p.slug, key: runKey(p.slug), scan: rec }`
   for every page with a record **and** a non-empty `pageHashes[p.slug]` **and** a non-empty
   composed `rulesetFingerprint`. Add `cache_records_read` and `cache_rejected`. Keep the READ-ONLY
   sentence verbatim and add one clause: *the records are write-ready — the SKILL persists them
   through `scripts/lint-cache.py`, and never derives a key or a reusability judgment itself*
   (A6).

**Why.** Defect 1 (the writer and the reader disagree) dies when the workflow emits the reader's own
shape; Defect 2's composition half dies when one implementation composes; the GAP's vault-side half
becomes visible through `cache_rejected`. Q6.1, Q6.2, A4, A6, A39.

*Out of scope at this site:* `PAGE_SCAN` and `pageScanPrompt` (**do not touch** — build-1 closed the
E6 budget at 3688/3700 with 12 chars spare, and any edit here moves `scanFingerprint` for no
reason); `files_checked` / `files_cached` denomination (`:671-673`) and the fan-out guards at
`:304-337`, which are deliberately dispatched-population-denominated; the step-4 refusal predicate
(Q6 declined); `:11`'s `depends_on:` ack (build-3 owns it, and this build enforces no convention
rule and drops no convention read, so nothing is owed there).

### F2 — NEW: `skills/vlt-lint/scripts/lint-cache.py`

**Current state.** `skills/vlt-lint/` has `SKILL.md` and `references/` only — **no `scripts/` dir**.
This build creates it.

**The exact change.** Create the script per disposition 2's two-mode contract. Constraints the
builder must not simplify:

- **Stdlib only.** PEP 723 header (`requires-python = ">=3.9"`, **no `dependencies`**), matching
  `verify-skill-manifest.py:1-4`'s form.
- **Exit 0 on missing and on unparseable.** A cold run is not an error. Non-zero exit is reserved
  for a genuine failure to write (permissions, no `_agent/` dir).
- **Atomic write** — temp file in the same directory plus `os.replace`, so an interrupted sweep
  never leaves a half-written sidecar that the next run reads as unparseable.
- **File shape:** `{"fingerprint": "<cache_fingerprint>", "written": "YYYY-MM-DD", "records": [ … ]}`.
  The top-level `fingerprint` is **informational only and is never a source of a reuse decision** —
  state that in the module docstring. The per-record `key` is the sole authority; the old sidecar's
  fatal shape was a top-level fingerprint with no per-page digest, and this file must not read as a
  return to it.
- **Deletes a legacy `_agent/lint-cache.yaml`** on a successful write and reports `legacy_removed`.
- **JSON to stdout in both modes**, one object, nothing else — it is parsed by the SKILL.
- Module docstring names its two callers (`full-scale.md` steps 2 and 5) and the workflow's `:245`
  filter as the single home of the record predicate it deliberately does not duplicate.

**Why.** A5(b) and D3's amended clause 1: the seam that broke was the SKILL-side write, and a round
trip that stubs it does not discharge A14-8.

*Out of scope at this site:* computing the component digests (the SKILL's, and `full-scale.md`
step 2 states them as executable steps — F3); reading or writing anything under `{lint_reports}`
(this is not a report, `vlt-lint/SKILL.md:74`); any validation of `scan` payload contents.

### F3 — `skills/vlt-lint/references/full-scale.md` — **BUILD-2 OWNS THIS FILE** (A8)

**Ownership, ruled explicitly.** *(Roundtable A8: "`full-scale.md` is shared with build-4 — one
brief owns the file, the other cites it.")* **Build-2 owns `full-scale.md`.** It makes the
structural edits (steps 2, 3 and 5), it lands first in release 2, and it defines the file's state
build-4 rebases onto. **Build-4 cites this brief** for steps 2/3/5 and confines its own edits to two
sites build-2 does not touch: **step 4**'s `-lint-failed.yaml` failed-run record and **step 5's
`churn_since_last_full` sub-bullet at `:13`**, whose *"by its dated filename"* discovery clause A8
flags as rendering a silent wrong number for a `.json`-persisting vault. The edit surfaces are
**disjoint by line**, and build-4's brief must say so and re-ground against post-build-2 source.

**Current state** (the file is 15 lines; each numbered step is one long line):
- **`:8`** — step 2. Reads `_agent/lint-cache.yaml`; specifies the ruleset fingerprint as *"a digest
  over, **in this order**: the installed `module_version`; this skill's own `depends_on:` pin vector
  verbatim; the digest of each convention this run judges against **as merged with its overlay** …;
  and the digest of `references/checks.md` (plus its overlay …)"*; *"Pass it as `rulesetFingerprint`,
  and pass the file's records as `cachedScans`."*; carries the standing mandate *"**A missing,
  unparseable or schema-mismatched sidecar is a cold run, stated in the report** — never an error and
  never a silent full sweep presented as a cached one."*
- **`:9`** — step 3, the `workflow('vlt-lint-full', {…})` invocation, naming `rulesetFingerprint` in
  both the arg list and the **resume** clause.
- **`:12`** — step 5's findings-cache sub-bullet: *"rewrite `_agent/lint-cache.yaml` in place … one
  record per page adjudicated this run — the workflow's returned `fresh_scans`, plus the reused
  records that are still valid"*, then the rewritten-whole / facts-not-verdicts / not-a-report
  clauses and the report-composition rule.

**The exact change.**

1. **`:8` — replace the fingerprint paragraph.** **Retire** the *"a digest over, in this order"*
   clause outright (A40 — it is not amended to sit beside the workflow's implementation). In its
   place, a **component contract** with the digests stated as **executable steps** (A7 — without
   this, half of Defect 2 survives and two conformant executors still disagree):
   - **instrument:** `shasum -a 256` over the file bytes (the same instrument step 1 already names
     for `pageHashes`, and the operating contract's honest-reporting instrument rule applies —
     pointed at, never restated);
   - **merge order:** base file bytes, then a newline, then the overlay file's bytes where one
     exists — **base then overlay, never the reverse**, matching the merged-on-read contract;
   - **encoding:** UTF-8, bytes as they sit on disk, no normalization;
   - **truncation:** the first **16 hex characters**, lowercase;
   - **what is passed:** `rulesetComponents` per disposition 4's named slots, `convention_digests`
     keyed by convention name — **order does not matter; the workflow sorts** (say so, so no reader
     re-invents an ordering contract);
   - **composition is the workflow's** and is not restated here (single-home discipline: the
     mechanism lives at `vlt-lint-full.js`, this file carries the pointer).
   Also: read **`_agent/lint-cache.json`** through
   `uv run --quiet "$SKILL/scripts/lint-cache.py" read --vault-root {project-root}` and pass its
   `records` as `cachedScans`; the script's `status`/`reason` is what the report's cold branch
   renders. **Keep the standing "cold run, stated in the report" mandate verbatim** and add one
   clause naming its instruments: the script's `status` for missing/unparseable, and the workflow's
   returned `cache_rejected` for schema-mismatched.
   **Keep** *"the first full run after any release is a COLD one — stated up front, never
   discovered."*
2. **`:9` — step 3**: `rulesetFingerprint` → `rulesetComponents` in the arg list **and** in the
   resume clause (the resume clause enumerates the args that null out — a stale name there is a
   silent cold run on every resume).
3. **`:12` — step 5's cache sub-bullet, rewritten.** The SKILL writes **the workflow's returned
   `cache_records`** — *one record per page adjudicated this run, fresh and reused; the workflow
   composes every key, and the SKILL never derives a key or a reusability judgment itself* (A6,
   stated as the reason, not just the instruction). The write is
   `uv run --quiet "$SKILL/scripts/lint-cache.py" write --vault-root {project-root} --fingerprint <cache_fingerprint> --records <path|->`.
   **Keep** rewritten-whole / never-appended, facts-never-verdicts, not-a-report, safely-deletable,
   and the report-composition rule — extending the last to name `cache_rejected` and
   `cache_records_read` alongside `files_checked` / `files_cached` / `cache_fingerprint`.

**Why.** A14-8's root cause is *the spec*: the reader's contract lives in code and the writer's in
prose, and the derivation between them *"is nowhere in the spec and must be reverse-engineered from
workflow source by every implementer."* After this edit the prose does not state a shape at all — it
names an executable.

*Out of scope at this site:* step 4's refusal predicate (Q6 declined) and its failed-run record
(build-4); `:13`'s `churn_since_last_full` clause (build-4); step 1's `crossLayerSlugs` derivation
predicate (single-homed here, untouched); step 2's dated "worked instance three times over"
illustration — left as the historical example it is, not re-versioned per release.

### F4 — `skills/vlt-lint/references/report.md` — the `lint_cache:` render

**Current state.** `:77`, inside the report's fenced shape block:
`lint_cache: <scanned N / cached M of T pages (fingerprint <fp>, written YYYY-MM-DD) | cold (<reason>) | not used (scoped run)>`.
`:88` is the **Findings-cache reporting** paragraph (what the line states, the additive rule, *"A
cold run says so and says why"*, the scoped-run literal, and the compose-from-returned-counts-only
rule).

**The exact change.**
1. `:77` — add the rejected pair to the warm branch:
   `… (fingerprint <fp>, written YYYY-MM-DD, rejected R of P records read) | cold (<reason>, rejected R of P records read) | not used (scoped run)`.
   **Rendered on both branches and including zero** (disposition 5) — a cold run that read and
   discarded 146 records is the field failure, and it must be legible on the cold branch above all.
2. `:88` — one clause: `rejected` counts records the workflow's reader filter discarded as
   schema-mismatched, against the number read; **it is never omitted, and `rejected 0` on a cold run
   means no records were read, not that the cache is healthy.**

**Why.** A39 — step 2's *"stated in the report"* mandate has no enforcement point today, and the
report is where it was supposed to land.

*Out of scope at this site:* **`report.md:3`'s "both homes" sentence and the `.json` persist
permission — build-4 owns them** (Q5, A8). The two edit surfaces are disjoint by line (`:3` vs
`:77`/`:88`); build-4 re-grounds against post-build-2 source. Also untouched: `churn_since_last_full`
at `:13`'s render (build-4), and every other slot in the fenced block.

### F5 — `skills/vlt-lint/SKILL.md:74` — the sidecar's path, in the persist step

**Current state.** `:74` is a single long line carrying **two independent sentences** this cycle
touches: the **report persist** sentence (*"write the Step-5 report block **verbatim** to
`{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` — plain YAML …"*), and the **cache** sentence (*"A
full-mode sweep also rewrites the findings cache at `_agent/lint-cache.yaml` — mechanics at
`references/full-scale.md` (the fan-out protocol's single home). It is **not** a report: it is never
persisted to `{lint_reports}`, never wake-read, and deleting it costs only a cold run."*).

**⚠ Line-level collision with build-4, dispositioned.** A8 names `vlt-lint/SKILL.md:74` as **build-4's**
site — for the *persist* sentence, which is the persist step's single home and which Q5's `.json`
permission would otherwise invert. **Build-2 edits the CACHE sentence only; build-4 edits the PERSIST
sentence only.** Same line, disjoint sentences, build-2 first. Build-4's brief re-grounds here and
must not restate build-2's clause.

**The exact change.** In the cache sentence only: `_agent/lint-cache.yaml` → `_agent/lint-cache.json`,
and one added clause — *written by `scripts/lint-cache.py`* — so the persist step names the
executable rather than implying a hand emission. Everything else on `:74` byte-identical.

**Why.** Disposition 1's rename, at the site a vault-side reader meets first.

### F6 — `skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:325` + the rule card

**Current state.** `:325` is the Decay contracts table row keyed on the literal path
`` `_agent/lint-cache.yaml` (the findings cache) ``, granting the exemption *"not an accumulator:
rewritten whole by each full-mode `vlt-lint` run, bounded by the page population, never wake-read,
and safely deletable (the next run goes cold). Stores extracted facts keyed on change, never
verdicts and never rulings…"*.

**The exact change.**
1. `:325` — the key becomes `` `_agent/lint-cache.json` (the findings cache) ``. **The exemption's
   reasoning is unchanged in substance** — every clause is still true of the JSON sidecar. Do not
   take the opportunity to rewrite it.
2. **Re-stamp `skills/vlt-setup/assets/governance/_meta/vault-rule-card.md`'s frontmatter
   `derived_from: … sha256:`** to the edited contract's SHA-256. package-lint **C6**
   (`tools/package-lint.py:315-349`) fails the release otherwise. The card's body does not change:
   the Decay table is not distilled into it (its only decay row is `:52`, the hygiene/safety-model
   line), and `RULE_CARD_BUDGET` (8000 bytes, `:261`) is not approached.

**Why.** R4 (disposition 6): renaming a file enumerated by literal path in a hand-kept enumeration
moves it out of that enumeration. The governance bundle is a **single-home SSoT** — this row is the
only home of the sidecar's decay exemption, and there is no second copy to keep in sync (CLAUDE.md,
Governance SSoT).

*Out of scope at this site:* every other Decay row; the contract's derive-first clauses (`:350` is
cited in build-1's deviation 3 as untouchable and stays untouched); any rewrite of the exemption's
wording.

### F7 — `skills/vlt-setup/assets/module.yaml` — the `uv` tool row's `needed_by:`

**Current state.** `:83-95` is `machine_tools:` with four rows. `:87-89` is `uv`:
`needed_by: "vlt-setup / vlt-upgrade merge + manifest scripts (PEP 723 inline deps)"`.

**The exact change.** Widen `needed_by:` to name vlt-lint's cache script — e.g.
`"vlt-setup / vlt-upgrade merge + manifest scripts and vlt-lint's findings-cache script (PEP 723 inline deps)"`.
`absent:` is widened by one clause: a full-mode sweep still runs, and renders `lint_cache: cold` —
**the sweep never fails because its cache did** (disposition 2's degradation posture).

**Why.** Disposition 6 item 3 — the row exists; only its truth about who needs it moves. **No new
`machine_tools` row is added**, so the writer-clause cost Q5 priced does not arise.

*Out of scope at this site:* `module_version:` — the dual version bump is the **release step's**
(`vlt-release`), never a build's; every other row.

## Registration

**None.** This build creates no skill directory, so no `.claude-plugin/marketplace.json`
`plugins[0].skills[]` entry and no `module-help.csv` row is owed — `skills/vlt-lint/` is already
registered in both, and a script inside an existing skill dir is not a registrable surface
(package-lint **C5** fails on an unregistered `skills/vlt-*` **dir**, not on a file within one).

**No bump owed is not no cost** (`brief-anatomy.md` §5) — this build pays two of the named ones:

- **package-lint C6** — F6 edits `governance/_meta/vault-operating-contract.md`, so
  `_meta/vault-rule-card.md`'s `derived_from: … sha256:` is re-stamped **in this build**.
  `RULE_CARD_BUDGET` is not approached.
- **package-lint E4** — **not triggered**: this build adds no `package-lint` check, so no declaring
  case in `tools/test-package-lint.py` is owed and `CASE_FLOOR` does not move. The round-trip harness
  is a factory-side fixture under `factory/cycles/14-no-enforcement-point/`, not a release-gate check.
- **package-lint E5** — the workflow's `// depends_on:` ack line (`:11`) is **not touched**. This
  build enforces no convention rule and drops no convention read, so no consumer walk is owed.
  **Build-3 owns that line** and must re-ground against post-build-2 source.

## Out of scope (dispositioned)

1. **Widening `full-scale.md` step 4's version-skew refusal predicate** — declined at Q6 with its
   reason, and re-confirmed by the roundtable's obsolescence beat: it detects a stale vault-local
   workflow copy, a failure the round-trip check cannot observe. Not touched.
2. **`PAGE_SCAN`, `pageScanPrompt`, `scanFingerprint`'s own construction** — build-1's, shipped, and
   closed at 3688 of a 3700 hard gate. This build reads `scanFingerprint`; it does not move it.
   Verification V5 measures `PAGE_SCAN` to prove it did not move.
3. **The `:11` `depends_on:` ack and the seven in-prose version pins at `:158`/`:159`/`:164`/`:168`/
   `:215`/`:571`/`:573`** — build-3's, per roundtable A3. Build-2 must not pre-empt them; build-3 is
   deliberately ordered **after** build-2 so `PAGE_SCAN` settles once before the re-ack pass reads it.
4. **The SKILL's inline transcription of cached records into `workflow(...)` args.** The workflow has
   no filesystem access (`:26-28`), so every record crosses the boundary as inline JSON — at
   146-page scale, an act no at-rest instrument in this build can grade. It is a property of the
   shipped design, not of this build; the `argsPath` route is **tracker #13, deferred by Q2** and
   bound to Cycle 15's `inbox-capture` (§Carried forward item 4). **Named, not silently inherited:**
   `cache_rejected` (disposition 5) is what makes a transcription failure legible on the run it
   happens, and field check (8) is what would see it.
5. **`report.md:3`'s both-homes sentence, `vlt-lint/SKILL.md:74`'s persist sentence,
   `full-scale.md` step 4 and `:13`, `vlt-setup/SKILL.md:194`** — build-4's, per A8 and Q5. F3, F4
   and F5 state the disjointness line by line.
6. **Migrating existing sidecars** — impossible in principle (Q6: no per-page digest), so the legacy
   file is deleted rather than converted. The first sweep after release 2 is cold regardless.
7. **`files_checked` / `files_cached` denomination and the fan-out shortfall guards** — deliberately
   dispatched-population-denominated (build B10 dispositions 10/11); untouched.

## Verification (unit, at rest — lifecycle step 5)

- **V1 — the three-run round trip.** `factory/cycles/14-no-enforcement-point/lint-cache-roundtrip.mjs`:
  loads the **shipped** workflow source with stubbed `agent`/`parallel`/`phase`/`log`/`budget`,
  `args` delivered as a **JSON string** (the runtime contract; the workflow's parse-on-intake at
  `:72-77` consumes it), a small synthetic page corpus with stable `pageHashes`, and the **shipped**
  `lint-cache.py` doing every read and write against a temp vault dir. **Three runs: cold → warm →
  warm.** Record every return and both sidecar files verbatim. It is a factory record, never copied
  into a vault by own-the-apply, and it is durable — re-runnable by a later cycle, not a scratch
  script.
- **V2 — the negative controls, on the same harness.** A patched workflow copy whose `PAGE_SCAN`
  differs by one character; a components object with one slot removed; a components object with its
  keys in a different order; a sidecar seeded with the field's own flat pre-repair record shape.
- **V3 — the documented-invocation check.** Extract the two command lines **verbatim** from
  `full-scale.md` steps 2 and 5 and execute them against the temp vault fixture. They must run as
  written; a divergence between the prose and the script's argument parser is a **failure**, not a
  transcription note.
- **V4 — retirement greps.** `grep -rn "fresh_scans\|lint-cache\.yaml\|a digest over, in this order" skills/`
  returns **zero**. Survivor greps: the workflow's READ-ONLY sentence, the `:245` filter, and step
  4's refusal predicate each still present and referenced. `node --check` parses the workflow;
  `python3 -m py_compile` parses the script.
- **V5 — E6 non-movement, measured.** `JSON.stringify(PAGE_SCAN).length` re-measured with
  **package-lint's own `_E6_NODE_EXTRACTOR`** (never a source char count) and asserted **equal to
  3688** — build-2 must not move the schema.
- **V6 — manifest coverage of the new script.** Run `verify-skill-manifest.py --write` against a
  temp root and confirm `skills/vlt-lint/scripts/lint-cache.py` appears as a manifest entry. The
  scope is structurally derived (`:129`, `:149`), but C6-d is on record as this exact scope question
  going wrong — **verify it, do not assume it**.
- **Packaging lint** — `uv run tools/package-lint.py` (A/B/C/E; D / `--expect-version` is the release
  gate, not this build's). **C6 must PASS**, which requires F6's rule-card re-stamp.
- **Handshake bipartite re-check (Group E)** — **not applicable in substance**: no convention
  `version:` moves, no `consumers:` list changes, and the workflow's `// depends_on:` ack is
  untouched. Stated rather than left silent; Group E runs anyway as part of the A/B/C/E pass and
  must PASS.
- **Fixture extension (R2)** — **not applicable**: no release-gate check is added or changed, so
  `tools/test-package-lint.py` and `CASE_FLOOR` do not move.
- **Legal response (R3)** — **not applicable**: this build adds and changes no **finding class**.
  `cache_rejected` is a report *fact*, not a finding — it fills no `fix_now` / `flag_for_human` slot
  and no check's counter derives from it. The reporting rule it obeys is stated at its single home
  (`report.md:88`) in this build.
- **Enumeration widening (R4)** — **substantive; see disposition 6**: the Decay contracts table
  (`vault-operating-contract.md:325`) is widened in this build; the skill-asset manifest needs no
  widening (structural scope, verified at V6); `machine_tools`' `uv` row's `needed_by:` is widened.
- **Roundtable rule R2 (synthetic-fixture observation duty)** — R2 names builds 3 and 4, not this
  one, but the duty is answered here anyway rather than left silent: **V1/V2 are synthetic fixtures
  by necessity** — no wiki corpus ships in this repo — and they are declared as such. They are *not*
  the shape R2 warns about (a synthetic fixture reached for with no prior failure behind it): this
  build has a documented, reproduced field failure behind it, and V2 seeds the harness with the
  field's own pre-repair record shape.
- **Scrub** — no personal or vault-local content in any changed shipped file. `{field-vault}`,
  `{project-root}` and `$SKILL` placeholders only; no real vault path anywhere, including in the
  script's docstring and the `full-scale.md` command lines. **Delete any `.decision-log.md`** before
  the build ends (`find . -name ".decision-log.md"` → nothing).

*(Non-release build: the dual version bump and the `--expect-version X.Y.Z` gate ride the **last**
build of release 2, not this one.)*

## Acceptance (live — appended to the roadmap ledger)

**Eight checks. Seven `[ship-verifiable]`, all GATE; one `[field-contingent]`, which does not.**
Per cycle ruling **D3 as amended (A17)**: bounded ⇒ ship-verifiable ⇒ GATES. Per rule **R1**, each
ship-verifiable check names the seam its instrument crosses.

**(1) `[ship-verifiable]` — at rest — GATES: the sidecar round-trips over three runs, with a real
writer.** Over V1: run 1 (no sidecar) is cold — `files_cached: 0`, every page dispatched, the script
writes N records; run 2 is warm — `files_checked: 0`, `files_cached: N`, `cache_rejected: 0`, and
the script rewrites N records; run 3 is **identical to run 2** — the same N, the same per-record
`key`, the same `scan` payloads byte-for-byte. **The third run is the check** (A5(a)): a two-run
fixture cannot observe reused-half loss, because if run 2 dropped the reused records the sidecar
would empty and a two-run check would still pass.
*Instrument:* `factory/cycles/14-no-enforcement-point/lint-cache-roundtrip.mjs` over the **shipped**
workflow source and the **shipped** `scripts/lint-cache.py`, temp vault dir, agents stubbed with
recorded `PAGE_SCAN` returns.
*Seam:* **workflow return → serialize (shipped script) → file on disk → parse (shipped script) →
workflow consume** — the exact seam b2(5)'s harness stubbed and the only seam that has ever broken.
*Evidence:* the three returns and both sidecar files, verbatim, in the BUILT `status:`.

**(2) `[ship-verifiable]` — at rest — GATES: a record keyed under a different `PAGE_SCAN` is NOT
reusable** (A4's stated interface). Re-run V1's run 2 against a workflow copy whose `PAGE_SCAN`
differs by one character: `files_cached: 0`, every page re-dispatched, and `cache_rejected: 0` (the
records are well-formed — they are keyed differently, which is the point). Symmetrically: changing
only a **ruleset component** also yields `files_cached: 0`; changing neither yields full reuse.
*Instrument:* V2's patched-workflow control on the same harness.
*Seam:* **`PAGE_SCAN` + prompt text → `scanFingerprint` → the composed per-page key** — the seam the
composition move could silently drop.
*Evidence:* the three `files_cached` values and the composed keys.

**(3) `[ship-verifiable]` — at rest — GATES: the reused half is returned, not lost** (A6). On V1's
run 2, `cache_records.length === files_checked + files_cached === files_listed`, and the majority of
its records are reused-derived; every record carries a non-empty `slug`, `key` and `scan`; and
`fresh_scans` is **absent** from the return (retirement 1). A page with no `pageHashes` entry
produces **no** record rather than one keyed on an empty digest.
*Instrument:* assertions over V1's run-2 return.
*Seam:* **workflow adjudication → the SKILL's write instruction** — where the spec previously asked
the SKILL to re-derive a reusability judgment it structurally cannot compute.
*Evidence:* the counts and one reused record verbatim.

**(4) `[ship-verifiable]` — at rest — GATES: the documented invocation is the executable one.** The
two command lines are extracted **verbatim from `full-scale.md`** (steps 2 and 5) and executed
against a temp vault fixture: both run as written and exit 0; a **missing** sidecar returns
`status: "missing"` at exit 0 and a **corrupt** one returns `status: "unparseable"` at exit 0 —
never an error, per step 2's standing mandate.
*Instrument:* V3, the extract-and-execute harness.
*Seam:* **prose instruction → shipped executable** — the seam A14-8 names as having no enforcement
point, and the half of the SKILL-side step disposition 2 can close at rest.
*Evidence:* the extracted command lines and the three exit codes + status strings.

**(5) `[ship-verifiable]` — at rest — GATES: the fingerprint is deterministic, complete, and
single-homed.** Two invocations with the same components in **different key order** compose the
identical `rulesetFingerprint`; a components object missing any slot composes `''`, yields a cold
run, and pushes a `coverage_caps` entry naming the absent slots. **And** `full-scale.md` step 2
carries the executable component recipe — instrument `shasum -a 256`, base-then-overlay merge order,
UTF-8, first-16-hex lowercase truncation — while
`grep -n "a digest over, in this order" skills/vlt-lint/references/full-scale.md` returns **zero**
(A40's retirement, which must not survive beside its replacement).
*Instrument:* V2's ordering/completeness controls plus the V4 grep and a read of the rewritten step 2.
*Seam:* **SKILL-computed component digests → workflow-composed fingerprint** (Defect 2's composition
half) **and prose recipe → SKILL execution** (Defect 2's digest half, which A7 shows the composition
move alone does not reach).
*Evidence:* the two composed values, the cold-run cap text, and the rewritten step 2.

**(6) `[ship-verifiable]` — at rest — GATES: a schema-mismatched sidecar is COUNTED and STATED**
(A39). Seed the harness with a sidecar carrying K records in the **field's own flat pre-repair
shape**: the run returns `cache_records_read: K`, `cache_rejected: K`, `files_cached: 0`, and the
`lint_cache:` line renders the rejected pair on its **cold** branch. `report.md:77`/`:88` describe
that render. The field failure — 146 records read, 146 discarded, a report that said only `cold` —
**cannot recur silently**.
*Instrument:* V2's flat-shape control plus a read of the two `report.md` lines.
*Seam:* **vault sidecar file → workflow reader filter (`:245`) → report line** — the mandate at
`full-scale.md` step 2 that has been prose with no enforcement point since it shipped.
*Evidence:* the two counts and the rendered line.

**(7) `[ship-verifiable]` — at the release gate — GATES: the packaging gates pass, including the
governance-edit cost.** `uv run tools/package-lint.py --expect-version X.Y.Z` exits **0** with both
version strings bumped; **C6 passes with the rule card re-stamped** against the edited contract; E6
measures `PAGE_SCAN` **unchanged at 3688** (build-2 must not move build-1's schema); Groups A/B/C/E
pass.
*Instrument:* package-lint Groups A/B/C/D/E, run at the release commit.
*Seam:* **source tree → release gate** — specifically the derived-artifact seam a contract edit
opens (C6) and the schema-budget seam a sibling build could disturb (E6).
*Evidence:* the PASS summary line recorded in the release commit message.

**(8) `[field-contingent]` — does NOT gate: the cache actually hits in a vault.** Two consecutive
`vlt-lint --full` sweeps on `{field-vault}` under an **unchanged** ruleset: the second reports
`files_cached > 0`, `cache_rejected: 0`, and a `lint_cache:` line naming the fingerprint it reused
under — the first time the mechanism has worked since it shipped.
*Event:* the owner runs `vlt-lint --full` on `{field-vault}` after upgrading to release 2 (that
sweep is **cold by construction** — build-2 rewrites the record shape, builds 3 and 4 move
convention and checks digests), then runs it a **second** time with no release, no overlay edit and
no convention change in between. Per roundtable **A26**, that second sweep is the slot where
`{field-vault}` pays its owed COMPLETE sweep — so the event is already scheduled, not invented here.
*Performer:* the owner. *Vault:* `{field-vault}` only — no wiki corpus ships in this repo, and the
factory cannot produce this event.
*Why field-contingent and why it does not gate:* the roundtable verified in session (**A17b**) that
b2(5)'s identical two-sweep event was **correctly** tagged field-contingent under the shipped
definition, and that **D3 does not reach it**. This check is tagged the same way for the same
reason. **The discharge of A14-8 rests on checks (1)–(6)** — the seam that broke is covered at rest
by an executable writer, which is what A5 demanded and what b2(5) did not have. This check is the
residual named at §Out of scope item 4: the SKILL invoking the script and transcribing 146 records
into workflow args at scale. **It is a watch, not the proof.**

---

**Next lifecycle move:** a **fresh builder session** implements this brief via
`bmad-workflow-builder`. Exit obligations: rewrite this brief's `status:` to a **BUILT** record with
**numbered deviations**, delete any `.decision-log.md`, one commit for the build. Then **`brief build
3`** — ordered after this build so `PAGE_SCAN` settles once before the 15-re-ack pass reads it (A3).
⚠ Two cycles are open and `factory/CYCLE` holds one line (A24): before running `acceptance-discharge`
or `cycle-closeout` against **Cycle 13**, hand-point `factory/CYCLE` at `13-trusted-returns` and
restore it immediately after. Never run either headless while that is true.
