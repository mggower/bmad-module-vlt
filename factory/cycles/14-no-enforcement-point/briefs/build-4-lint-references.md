---
title: 'Build #4 — lint references: a destructive fix direction gets routed by the scanner, and the report persist gets the parse check it has always asserted'
status: >
  BUILT 2026-08-27 — every F-site landed; **5 of the 6 ship-verifiable checks are gradeable at rest:
  4 PASS, 1 FAILS on real material and the failure is the filing's own prediction confirmed**;
  (6) is bound to the first full `{field-vault}` sweep after release 2 and is UNFILLED by
  construction. Version bump NOT taken — owner ruling 2026-08-27 moved it to the release step
  (`vlt-release`, v0.17.0). Branch `cycle14-release2`.

  **Sites changed — 7 shipped files.**
  `skills/vlt-lint/references/checks.md` (F1): `:16` the *Sources-vs-prose agreement* bullet rewritten
  whole — the single, universal legal response RETIRED (P-15, replaced not supplemented), the direction
  routing stated as the check's own semantics (five enum members named, `diverge_unclassified` named as
  the escape and as never-auto-fixed), two direction-bound legal responses (add-to-prose auto-fixable;
  add-to-frontmatter-or-rule-it-out flagged, citation never deleted), and a pointer to
  `fix-and-file.md` Step 3 that does not restate the procedure. `:14`/`:15` (build-1's) and `:17`/`:19`
  (build-3's) untouched.
  `skills/vlt-lint/references/fix-and-file.md` (F2): one bullet added to Step 3's auto-fix list at
  `:12`, immediately after *Broken wikilinks* — the procedure the class has never had; it names the
  class, states the mechanical add-only act, excludes the `flag_for_human` half, and CITES `checks.md`
  for the direction test rather than restating it.
  `skills/vlt-lint/references/report.md` (F3, F5): `:3` restated WHOLE (never appended to, per Q5's ⚠)
  — strict YAML in-session, two legal persisted homes, content-verbatim, the no-dependency requirement,
  the JSON-subset emission strategy with its reason, and the claim's enforcement point NAMED; `:21` the
  `fix_now` slot narrowed to the prose-gap direction; `:67` a new `flag_for_human` slot
  `sources_vs_prose_unresolved` added immediately after `malformed_frontmatter` (R4's enumeration
  widening). Build-2's `:77`/`:88` untouched.
  `skills/vlt-lint/SKILL.md` (F6, F8): `:74` build-4's persist sentence rewritten — `.yaml` default or
  `.json`, `verbatim` restated as **content-verbatim**, the JSON-subset strategy pointed at rather than
  restated, append-only/retention/never-wake-read/Decay clauses preserved, the pre-existing-reports
  clause widened to either format; `:76` the failed-run record names both extensions. **Build-2's cache
  sentence on `:74` is byte-identical and untouched.**
  `skills/vlt-lint/references/full-scale.md` (F8): `:10` (step 4) the failed-run record accepts both
  extensions — refusal predicate, stale-copy diagnosis and `next:` line untouched; `:13` the
  `churn_since_last_full` discovery matches both extensions (A8's silent wrong number). **Build-2's
  `:8`/`:9`/`:11`/`:12` untouched.**
  `skills/vlt-setup/SKILL.md` (F8): `:194` `{lint_reports}` provisioning names `.yaml` (default) or
  `.json`; the never-clobber clause untouched. `:195` (the **upgrade** report class) deliberately NOT
  touched.
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (F4, the grounding addition — the FOURTH build
  in this file this cycle; 870 → 882 lines): `:178` the `sources_vs_prose` enum widened to
  `match | diverge_prose_gap | diverge_frontmatter_gap | diverge_unclassified | no_prose_section` and
  its description trimmed, `write-verification@4` preserved; `:179` the detail slot's description
  trimmed; `:229` the page-scan prompt's Gap B clause replaced with the three directed members, naming
  `diverge_unclassified` as the safe answer that is flagged and never auto-fixed (`frontmatter@14` and
  `write-verification@4` preserved verbatim); `:795-800` the `fix_now` predicate narrowed to
  `=== 'diverge_prose_gap'` with a comment recording that the route tests the RETURNED verdict, never
  the free-text detail (D1); `:844-850` a new `flag_for_human.sources_vs_prose_unresolved` entry
  filtering `diverge_frontmatter_gap || diverge_unclassified`. `:161` `required:` unchanged; `:11`
  `depends_on:` untouched; build-1's `frontmatter_defect` machinery and build-2's `cache_records`
  machinery untouched.

  **Verification at rest.**
  **V1 (check 2) PASS** — node harness over the SHIPPED reduce (whole file executed with the runtime's
  hooks stubbed, `args` delivered as a **JSON string** so parse-on-intake at `:77` was exercised), five
  stub scans, one per enum member. `fix_now.sources_vs_prose_mismatches =
  ["p-prosegap: frontmatter cites A; prose lacks A"]`;
  `flag_for_human.sources_vs_prose_unresolved = ["p-fmgap: prose cites B; frontmatter lacks B",
  "p-unclass: divergence the scanner could not direction-classify"]`. All five assertions PASS:
  prose-gap in `fix_now` and nowhere else; frontmatter-gap and unclassified in `flag_for_human` and
  never in `fix_now`; `match`/`no_prose_section` produce neither.
  **V2 (check 1) — RAN ON REAL MATERIAL, and it FAILED. ⚠ The `.yaml` limb FAILS 1 of 6; the `.json`
  limb PASSES.** Read-only copies of all six `.yaml` reports in `{field-vault}`'s `{lint_reports}`
  archive (`2026-08-23-1504`, `2026-08-23-1739`, `2026-08-24-1700`, `2026-08-25-1600`,
  `2026-08-26-1046`, `2026-08-27-1104`); the four `.md` reports are out of the class. Instrument
  `uv run --with pyyaml`, at rest, archive never written. **Five parse; `2026-08-24-1700-lint.yaml`
  does not**, verbatim: `mapping values are not allowed here, in "<unicode string>", line 102,
  column 59: ...  scanned; 24 carry revisit_after:`. The offending line is
  `  research_zone: 145 notes scanned; 24 carry revisit_after:` — a **bare unquoted scalar containing
  `: `**, which is exactly the class A14-5 predicted and nothing had ever tested. **The archive was NOT
  repaired** (it is the vault's, append-only). **`.json` limb PASS:** the most recent archived report
  (`2026-08-27-1104`) re-rendered per F5's documented JSON-subset strategy re-parses under PyYAML
  identically, translates mechanically to `.json`, and `python3 -m json.tool` exits **0** with content
  round-trip-identical. **The strategy is proven to cure the observed failure**: the same scalar
  rendered as `"145 notes scanned; 24 carry revisit_after:"` parses. **No fallback path was taken and
  rule R2's observer duty did NOT fire** — the instrument ran on real material.
  **V3 (checks 3 + 4) PASS** — `grep -rn "reconcile the prose section to frontmatter" skills/` returns
  **zero** (the P-15 retirement, verified); `grep -rn "sources_vs_prose" skills/` returns **14 hits**
  across five files, every one accounted (`checks.md:16`; `fix-and-file.md:12`; `report.md:21`/`:67`;
  `vlt-lint-full.js` `:161`, `:178`, `:179`, `:229`, `:795`, `:799`, `:800`, `:848`, `:849`, `:850`);
  the `.yaml`-mandate grep leaves only `vlt-upgrade/SKILL.md:132` + `vlt-setup/SKILL.md:195` (the
  **upgrade** report class, out of scope by F8) and `vault-operating-contract.md:330` (deviation 2);
  `node --check` on the workflow parses.
  **V4 (part of check 5) PASS — E6 measured 3676**, with package-lint's own `_E6_NODE_EXTRACTOR`, never
  a source char count: `PAGE_SCAN` **3688 → 3676** (budget 3700; margin 12 → 24). Other three schemas
  unchanged: `INDEX_SCAN` 823, `CLUSTER_FINDINGS` 1630, `PAIR_FINDINGS` 376. **Build-4 returned 12
  characters to the budget**, as briefed.
  **V5 (check 5, release-gate half) PASS** — `uv run tools/package-lint.py`:
  `package-lint: A/B/C/E PASS, D SKIPPED — vlt 0.16.2`. **Group E (E1-E7) PASS whole, including E7**,
  build-3's new check, over the two edited in-prose pin sites; the token counts build-3's check (2)
  established hold: **5 `frontmatter@14`, 5 `write-verification@4`**. Group D SKIPPED because no
  `--expect-version` was passed — see deviation 1.
  **Handshake bipartite re-check: not applicable** (no convention `version:` moves, no `consumers:`
  change); package-lint Group E is the check of record and ran whole. **R2 fixture extension: not
  applicable** (no gate check added or changed; `CASE_FLOOR` stays 24). **R3 discharged** at
  `checks.md:16`. **R4 discharged** at `report.md:67` + `vlt-lint-full.js:848`.
  **Scrub PASS** — no personal or vault-local content in any changed shipped file; no `ST-N`
  study-register id anywhere in `skills/` or `.claude-plugin/` (verified **zero** before and after).
  No `.decision-log.md` in the tree.

  **Ship-verifiable check grades: (1) FAIL (`.yaml` limb 5/6; `.json` limb PASS) — see deviation 3;
  (2) PASS; (3) PASS; (4) PASS with one residual site — see deviation 2; (5) PASS on its at-rest half,
  the `--expect-version` half deferred to `vlt-release` per deviation 1; (6) UNFILLED by construction.**

  **Deviations.**
  1. **The dual version bump was NOT taken in this build, contradicting §Release.** Owner ruling
     2026-08-27: release 2 ships as **v0.17.0** and the bump belongs to the release step (`vlt-release`),
     not to the build — the same posture builds 1, 2 and 3 took. Check (5) is therefore graded in two
     halves: its at-rest half (A/B/C/E green, E6 = 3676, E7 clean) PASSES here, and its
     `--expect-version` half is the release step's, written against the released version rather than a
     literal. Nothing else in §Release changed.
  2. **F9 is INCOMPLETE — `vault-operating-contract.md:330` still mandates `.yaml`, and it was NOT
     edited. ⚠ OWNER DECISION OWED BEFORE THE TAG.** F9 verified `:51` and `:323` (both name
     `{lint_reports}` as a directory with no extension — correct, and re-verified here) but did not
     reach `:330`, which reads *"A **structured report-emitting** verb persists its report verbatim as
     a dated plain `.yaml` file under its report dir, declared in these tables in the act that creates
     it (retention-at-birth)"*. After this build the operating contract asserts one persisted format
     while `vlt-lint/SKILL.md:74` permits two — **the exact inverted-pointer shape check (4) exists to
     catch**, one file outside the six sites check (4) enumerates. It was left unedited because the
     owner's 2026-08-27 ruling is explicit (*no governance-bundle edit, no C6, no rule-card re-stamp*)
     and because the sentence is **generic across report classes** — widening it would also widen the
     `vlt-upgrade` report class, which F8 explicitly scopes out. **The build honours the ruling and
     records the contradiction rather than resolving it unilaterally.** The repair is cheap and known:
     one clause on `:330` plus a `vault-rule-card.md` `sha256:` re-stamp (C6 is a hash check, nothing
     more). **Recommended: an owner ruling before the release-2 tag, and a `factory/inbox/` filing if
     it is deferred.**
  3. **Acceptance check (1) FAILED on real material, and the failure is the build's central evidence,
     not a build error.** One of six archived reports does not parse. The brief anticipated exactly
     this (*"It can fail... the failure is recorded verbatim and the archive is not repaired"*), and the
     failing construct — an unquoted scalar carrying `: ` inside its value — is the precise class the
     shipped JSON-subset mandate removes, demonstrated in V2. **The check is graded FAIL, honestly**;
     it is ship-verifiable and it GATES, so it needs an owner grade at `acceptance-discharge`: the
     archive predates the mandate by construction, so the question is whether the check reads *"the
     existing archive parses"* (FAIL, permanently, on immutable append-only material) or *"a report
     persisted under this build's mandate parses"* (which V2's `.json` limb and the cure demonstration
     already evidence). **The builder does not re-grade it.**
  4. **The brief's F4 pre-measurement of the two properties (338 → 326) is off by 4 in both terms.**
     Measured by property-pair serialization: **334 → 322**. The **delta is exactly −12 as briefed**,
     and the number that gates — `PAGE_SCAN` measured whole by `_E6_NODE_EXTRACTOR` — is **3688 → 3676**,
     exactly as briefed. No consequence; recorded so a later reader does not re-derive the discrepancy.
  5. **The brief's V3 expectation of "six hits" for `grep -rn "sources_vs_prose" skills/` was already
     wrong at `6525715`: there were seven** (it omitted `vlt-lint-full.js:161`'s `required:` array,
     which is untouched by this build). The post-build count is 14 and every hit is accounted above.
  6. **`fix-and-file.md`'s new bullet landed at `:12`, not "after `:11`" as a line number.** The brief
     named the *Broken wikilinks* bullet as `:11`; it is in fact at `:11` and the new bullet is the line
     after it. Same site, same order, no ambiguity — recorded only because the brief's Step-3 line
     inventory (`:9`-`:13`) shifts by one below the insertion.
module_code: 'vlt'
created: '2026-08-27'
derives_from:
  - 'factory/inbox/2026-08-26-123144-reclassify-sources-vs-prose-mismatches-out-of-fix-now.md (A14-4 — the `fix_now:` misclassification, the one-directional fix instruction that deletes real citations, and the GAP capture found: the class has no Step-3 auto-fix procedure at all)'
  - 'factory/inbox/2026-08-26-123153-lint-mandates-strict-yaml-persist-with-no-yaml-library.md (A14-5 — the strict-YAML persist mandate with no validation site; PROVENANCE-CORRECTED at capture: the gap is the unchecked claim, not a missing emitter)'
roadmap: 'factory/cycles/14-no-enforcement-point/roadmap.md'
rulings: >
  roadmap §Ideation rulings (2026-08-26): Q5 (`.json` is a legal ALTERNATIVE persisted format, the
  fenced in-session block stays YAML, `report.md` gains an explicit no-dependency requirement and the
  JSON-subset emission strategy) as amended by roundtable A9 (the stdlib-asymmetry rationale is
  STRUCK as factually false — `machine_tools` declares four tools and `uv` is the declared PEP 723
  route; the `.json` direction stands on the corrected reason, and option 4 "ship an emitter" stays
  NOT TAKEN); D3 as amended by A17/A17b (BOUNDED ⇒ ship-verifiable ⇒ it GATES; where an at-rest
  instrument is buildable inside the build's own scope the brief MUST build it) + rule R1 (every
  ship-verifiable check names the seam its instrument crosses); E1 (the detectability-vs-remediability
  account is the filer's unverified reasoning — attached as context, NEVER asserted as a finding);
  E2 (the *"frontmatter is the source of truth"* qualifier is SCOPED OUT — `write-verification.md`'s
  tier-1 item is not touched; routed by A32 to `factory/inbox/` as an owner-filed `pattern`);
  §Grouping & order build-4 block incl. A8 (the persist mandate's single home is `vlt-lint/SKILL.md:74`,
  not `report.md:3`; `full-scale.md` is shared with build-2 and BUILD-2 OWNS IT; a `.json` persist is a
  translation the word *verbatim* forbids, and the brief says which act emits which home) and A10
  (build-4 SHIPS the validation beat, gating — "lets" is not "does"); A26 (release 2 is the cycle's
  second cold sweep, by construction); P-15 (the retirement clause).
risk: >
  moderate — no convention `version:` moves, no consumer walk, no governance-bundle edit and no
  `machine_tools` row is owed; but the build is the FOURTH to enter `vlt-lint-full.js` in one cycle
  (a grounding addition the roadmap's touch-list did not name), it edits `PAGE_SCAN` and the page-scan
  prompt inside a hard release gate with 12 characters of headroom, it changes a shipped finding
  class's tier, and it is the RELEASE build for release 2 — it carries the dual version bump and the
  `--expect-version` gate that build-3's check (1) deliberately left to it.
---

# Build #4 — lint references: the routed fix direction and the checked persist

## Intent

Two filings, one shape, and it is this cycle's own name. **A stated rule with no enforcement point.**

**A14-4.** `sources_vs_prose_mismatches` sits in the report's `fix_now:` block — the slot whose
meaning is *safe to apply serially without judgment* — and the only fix direction the module states
is `checks.md:16`'s *"reconcile the prose section to frontmatter `sources:` — frontmatter is the
source of truth."* Applied where the prose cites sources the frontmatter omits (the direction the
field measured as dominant), **that instruction deletes real citations.** The field's own answer was
to stop obeying it: 26 then 25 instances across two consecutive full sweeps, **zero** auto-applied,
both runs declining the whole class for the same recorded reason. Capture then found the gap is
sharper than the filing knew — `fix-and-file.md` Step 3, the auto-fix procedure list, **does not name
the class at all**; the whole `skills/vlt-lint/` tree carried exactly two hits, the report slot and
the check. A `fix_now` class with no procedure to execute and one destructive direction.

**A14-5.** `vlt-lint/SKILL.md:74` mandates persisting the report block **verbatim** as plain YAML,
and `report.md:3` mandates that it *"keep parsing whole in both homes."* Capture corrected the
filing's premise — nothing is serialized, the agent authors the block and Step 6 persists it, so no
YAML emitter was ever missing — and relocated the gap: **nothing validates the claim.** The report
is LLM-authored YAML carrying free-text findings with em-dashes, colons inside values, arrows and
quoted strings: exactly the content where naive emission breaks and *"it looked fine"* is not
verification.

Build-4 gives both an enforcement point. A14-4's routing stops being prose a fixer is asked to
infer and becomes **a scanner verdict the reduce dispatches on**; A14-5's claim stops being an
assertion and becomes **a parse run over real persisted reports, at rest, gating the tag.**

**All rejected alternatives in the parent filings are settled — do not re-litigate.** In particular:
the emitter (Q5 option 4) is not shipped; `write-verification.md`'s tier-1 item is not touched (E2);
the detectability-vs-remediability account is not asserted anywhere (E1).

## Cold by construction, stated up front

**The first full lint after release 2 is COLD, and build-4 is one of three reasons.** `checks.md` is
a component of `rulesetFingerprint` and build-4 moves its digest; build-4 also edits `PAGE_SCAN` and
`pageScanPrompt`, both terms of `scanFingerprint` (`vlt-lint-full.js:232-233` at v0.16.1; the
composition now lives at `:250-282` after build-2). Builds 2 and 3 moved the same fingerprints first.
**This is not a cache regression, and no acceptance check may be graded as if it were one.** Release 1
already forced one cold sweep; this cycle knowingly costs two (roundtable A26), and `{field-vault}`
pays its owed COMPLETE sweep on the **second** sweep after release 2.

## File ownership with build-2, honoured

`references/full-scale.md` is **shared, and build-2 owns it** (roundtable A8, ruled in
`briefs/build-2-findings-cache.md` §Brief-time dispositions). Build-4 **cites** that brief and
confines itself to **step 4 (`:10`) and `:13`** — the two lines build-2 does not touch (build-2 took
steps 2, 3 and 5, i.e. `:8`, `:9`, `:11`, `:12`). Two finer collisions build-2's brief dispositioned,
**both re-verified against current source in this pass**:

- **`vlt-lint/SKILL.md:74` carries a build-2 sentence and a build-4 sentence on one physical line.**
  Verified at `d641050`+: the line's cache sentence now reads *"A full-mode sweep also rewrites the
  findings cache at `_agent/lint-cache.json`, written by `scripts/lint-cache.py`"* — **build-2's,
  shipped, untouched by this build.** The persist sentence (*"Also **persist the report** (both
  modes): write the Step-5 report block **verbatim** to `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` —
  plain YAML…"*) is **build-4's**. Disjoint sentences; build-4 edits only the second.
- **`report.md` splits `:77`/`:88` (build-2's `lint_cache:` slot and its reporting paragraph) from
  `:3` (build-4's both-homes sentence).** Verified: `:77` and `:88` carry build-2's
  `rejected R of P records read` clause and are not touched here.

## Brief-time dispositions

### 1. THE DIRECTION ROUTING'S SINGLE HOME IS `checks.md:16`. `fix-and-file.md` Step 3 CITES it. *(settles the roadmap's deferred build-4 question 1)*

The roadmap left this open: *"whether the `sources_vs_prose` direction routing lives in `checks.md`
or in `fix-and-file.md` Step 3."*

**Ruled: `checks.md:16`, and nowhere else.** The routing is **check semantics** — it decides the
finding's *class* (which report slot it occupies) and *which legal response applies*. Both are the
check catalogue's business, and the module already rules it so: cycle rule **R3** requires that
*"any build that adds or changes a finding class states that class's one-line legal response at the
check's own single home — `checks.md` for lint."* `fix-and-file.md` Step 3 is the **procedure** — what
a fixer executes on the auto-fixable half — and it gets the entry that does not exist today, written
as a **pointer**: it names the class, states the mechanical edit, and **cites `checks.md` for the
direction test rather than restating it.**

This is the shipped precedent one line over: `checks.md:19` defines `para_type_unknown`'s recognized
set nowhere and instead states *"defined in `{conventions}/extraction.md` … which is its single home;
named here for the reader only."* Same discipline, same file.

**Why the alternative was rejected:** siting the routing in Step 3 would put the test that decides a
finding's **tier** inside the procedure that only ever sees findings already tiered — the routing
would have to be restated in `checks.md` anyway for the report to know which slot to fill, and a
rule restated in two places is the drift CLAUDE.md's single-home rule names. `report.md` states the
two slots and their one-line meanings, as it does for every other slot; it does not restate the test.

### 2. THE ROUTING NEEDS A SCANNER VERDICT, AND THE SCANNER DOES NOT RETURN ONE — grounding addition *(the change that makes disposition 1 executable)*

**Grounding finding, not in the roadmap and not in the capture.** `PAGE_SCAN` returns
`sources_vs_prose` as a **tri-state** — `'match' | 'diverge' | 'no_prose_section'`
(`vlt-lint-full.js:178`) — plus a free-text `sources_vs_prose_detail` (`:179`), and the page-scan
prompt's Gap B clause (`:229`) instructs *"'diverge' only when both exist and an entry in one is not
traceable in the other."* The reduce at `:795` therefore has **no direction to route on**:

```js
sources_vs_prose_mismatches: scans.filter((s) => s.sources_vs_prose === 'diverge').map(...)
```

**Routing by direction is not expressible against this return.** The only remaining route —
inferring direction from `sources_vs_prose_detail`'s free text — is precisely the reduce-side
prose-parsing that **build-1 retired eleven weeks of debt to remove**, and D1 rules in this same
cycle that a schema description is never an enforcement point. It is refused.

**Ruled: `PAGE_SCAN`'s `sources_vs_prose` enum carries the direction, and `vlt-lint-full.js` joins
build-4's file surface as a grounding addition** (`grounding-at-brief-time.md`, *EXPANDED*). This is
not a contradiction of an ideation ruling and is not the owner's to re-rule: §Grouping ruled that
build-4 *"adds the second legal response and **the direction routing**"*, and grounding shows only
where the routing must live for that ruling to be executable. The capture itself already named the
workflow as a home of the class (`vlt-lint-full.js:665` at v0.16.1, the `fix_now:` slot); §Grouping's
**Touches:** list — the list roundtable A8 amended precisely because it was wrong — simply omitted it.

**The enum, and its escape member.** Per roundtable **A35** (a closed enum meeting an actor the
surrounding rules authorize is this cycle's own named cause, and a closed roster must carry an
unclassified member whose disposition **reports**), and mirroring the `frontmatter_defect` enum
build-1 shipped into this same file (`none | missing_required | malformed_block | unclassified`):

| member | meaning | slot |
|---|---|---|
| `match` | both sides agree | neither |
| `no_prose_section` | no prose `## Sources` section — conformant | neither |
| `diverge_prose_gap` | frontmatter carries entries the **prose section** lacks | `fix_now` |
| `diverge_frontmatter_gap` | the **prose** cites entries frontmatter lacks | `flag_for_human` |
| `diverge_unclassified` | both directions present, **or** the scanner cannot say which | `flag_for_human` |

`diverge_unclassified` is the escape, and **its failure direction is to flag, never to auto-apply** —
the conservative direction here, because the auto-fix half is the only half that writes. A
divergence the scanner cannot classify is never silently swallowed and never mechanically
"reconciled."

**E6, measured with package-lint's own `_E6_NODE_EXTRACTOR`, never a source char count.**
Baseline at `6525715`: `PAGE_SCAN` = **3688** of **3700** — 12 characters. The ruled shape widens the
enum (+) and pays for it by trimming both descriptions (−), landing at **3676**. **Build-4 returns 12
characters to the budget rather than spending any**; margin goes from 12 to 24. The measured deltas
are in F4 and must be re-measured by the builder with the same extractor.

### 3. THE REPORT PERSIST GETS **NO** SERIALIZER, AND `lint-cache.py` IS NEITHER REUSED NOR SHARED *(the roadmap's deferred question, and the "two serializers" hazard, ruled)*

Build-2 shipped `skills/vlt-lint/scripts/lint-cache.py` — stdlib-only PEP 723, atomic temp+rename,
exit 0 on missing/unparseable. A14-5 is the *report* persist with a superficially identical shape:
strict serialization mandated, no library, PEP 668 machines. **Ruled: the report persist gets no
writer at all, `lint-cache.py` is not extended and nothing is shared. Exactly one serializer exists
in `vlt-lint` and it stays exactly one.** Four reasons, on record so no later cycle re-derives them:

1. **The two problems are not the same problem.** `lint-cache.py` exists because a
   **machine-constructed** value — the workflow's returned `cache_records` array — was persisted by
   **prose** telling a hand-writer what to emit, and the writer and the reader disagreed. The report
   has no machine-constructed source object to serialize: `report.md:5-7` has the **agent** author
   the fenced block, and Step 6 persists that block. There is nothing to serialize *from*, so a
   serializer would have to be handed a JSON document the agent hand-built first — which is the
   hand-emission the script would exist to remove. It would add a file and enforce nothing.
2. **Shipping an emitter is Q5's option (4), and it is still not taken.** Roundtable A9 struck the
   *cost rationale* that ranked option 4 last (`machine_tools` declares four tools, and `uv` is the
   declared PEP 723 route, so an emitter's dependency was never the barrier the ruling claimed) —
   **it did not reverse the ruling.** The owner ruled the `.json` direction stands on the corrected
   reason. Reusing `lint-cache.py` for the report is that emitter under another name.
3. **The report's failure mode calls for a reader, not a writer.** A cache record fails by being
   **mis-shaped** — a writer is the right enforcement point, because shape is decidable at write
   time. A report fails by being **unparseable** — and the only thing that decides parseability is a
   parser. The enforcement point A14-5 is missing is therefore the **gating parse check** (F7,
   acceptance check (1)), which is what A10 ordered and what this build ships.
4. **`lint-cache.py` already declines the symmetric temptation** — its docstring records that it
   deliberately does **not** re-validate the record schema, because the reader-side filter is that
   contract's single home and *"a write-side copy of that predicate would be a second statement of
   one contract — the exact defect this build exists to remove."* The same discipline, one file over.

### 4. ONE AUTHORING ACT, ONE PERSIST ACT — `verbatim` IS RESTATED AS **CONTENT-VERBATIM** *(settles A8's "which act emits which home, or the cycle ships a permission with no emission point")*

A8's objection is exact: a `.json` persist is **not a verbatim copy of the fenced block — it is a
translation**, and `SKILL.md:74`'s word *verbatim* forbids a second authoring act.

**Ruled: `.json` adds no authoring act.** Step 5 authors the report content **once** and emits it
fenced as strict YAML. Step 6 persists it. Where the vault persists `.json`, Step 6's output is the
**same content rendered in the persisted format** — and because `report.md` now mandates JSON-subset
emission (every scalar a JSON string, lists as `- <json>`, nested maps by indentation), **the
rendering is punctuation, not judgment**: no value is re-authored, re-worded, re-ordered, dropped or
summarized. `SKILL.md:74` says exactly that — *content-verbatim*: the persisted home carries the
block's content unabridged, unreordered and unreworded, in the persisted format.

This preserves what `verbatim` was built to guard — persist-time summarizing and pruning, the failure
that would make a persisted report a lossy paraphrase of what the session saw — without asserting a
byte-identity that a second format cannot have. **The emission point is named: Step 6, one act, one
file.**

### 5. `.json` IS AN **ALTERNATIVE**, NOT THE DEFAULT — and the mandate is not scoped away from `.yaml` *(settles the roadmap's deferred build-4 question 2, and A10's brief-time addition)*

Q5 already ruled the word: *"(b) **`.json` as a legal alternative persisted format**, the fenced
in-session block staying YAML for human reading."* Grounding **confirms** the ruling rather than
reopening it, and names two costs a default-flip would have incurred that ideation did not price:
`vlt-setup/SKILL.md:194` provisions `{lint_reports}` as *"plain `.yaml`"* and every existing vault's
archive is `.yaml`, and `full-scale.md:13` discovers the previous full report **by its dated
filename** — a default-flip would make every vault's own history invisible to its churn measure on
the first post-upgrade run. **Default stays `.yaml`. `.json` is permitted, never required, and
pre-existing reports in either format stay as they are** (the shipped `.md`-reports precedent already
in `SKILL.md:74`).

**A10's brief-time addition, answered:** *"if `.yaml` remains a legal persist the check must cover it
(which costs a `machine_tools` row) or the mandate is explicitly scoped to `.json`."*
**Ruled: the check covers both homes, and NO `machine_tools` row is owed, because the check is
factory-side.** `machine_tools` (`skills/vlt-setup/assets/module.yaml:83-95`) declares what a **vault**
must have; build-4 adds no vault-side step and no vault-side tool assumption. The gating parse check
runs **at rest in the factory** over read-only copies of real persisted reports, using
`uv run --with pyyaml` for the `.yaml` home and stdlib `python3 -m json.tool` for the `.json` home —
and `uv` is already a declared tool whose stated purpose is literally *"PEP 723 inline deps"* (A9).
**Neither the mandate nor the check is scoped away from `.yaml`.**

### 6. INTERIM POSTURE (R1) — the vault has no run-time enforcement point, and the window is named

**R1 applies: build-4 ships a rule with a factory-side mechanism and no vault-side one.** After this
build, a vault that persists a malformed report is caught by nothing at run time. The interim posture,
stated rather than discovered:

- **What is legal in the window:** the vault persists per `SKILL.md:74` and validates nothing. The
  module's enforcement point is at the **tag** — acceptance check (1), which parses real persisted
  reports and can fail the gate. That is one bound, not a vault-side one, and the brief says so.
- **What the exposure actually is:** a malformed persisted report costs nothing downstream in the
  same sweep — the persist is the sweep's last act, lint reports are **never wake-read** (the
  operating contract's Decay exemption at `vault-operating-contract.md:323`), and
  `full-scale.md:13`'s churn lookup reads **filenames**, not content. The loss is bounded to *a later
  reader cannot parse this one report*, discovered when someone tries.
- **The successor, and why it is not this build's:** a vault-side validation beat would owe **no new
  `machine_tools` row** (A9: `uv` + `python3` are already declared), so the cheap route exists and is
  named. It is out of scope here because it adds a **step** to a shipped skill's sweep on an
  unmeasured benefit, and A14-5's measured defect is the unchecked *claim*, which check (1) closes.
  **Recorded for closeout as a carry-forward** (§Out of scope, item 7).

### 7. RETIREMENT (P-15) — one prohibition retired, three negatives returned explicitly

**Retired in this build:** `skills/vlt-lint/references/checks.md:16`'s **single, universal legal
response** — *"reconcile the prose section to frontmatter `sources:` — frontmatter is the source of
truth."* It is **replaced, not supplemented**: applied to the `diverge_frontmatter_gap` direction it
is the instruction that deletes real citations, which is A14-4's entire filing, and leaving it beside
the new routed pair would leave the destructive reading available to any fixer who read the older
sentence first. A ship-verifiable check greps that the sentence does not survive anywhere in
`skills/` (acceptance check (3)).

**Negatives returned explicitly, so the beat is answered rather than silent:**

- **`report.md:3` — rewritten, NOT retired.** The roundtable already ruled this one: *"the strictness
  survives; only the format monopoly goes."* The sentence is restated whole (Q5's ⚠: *restated, not
  appended to, or the bundle asserts one format while permitting two*).
- **`sources_vs_prose_detail` — NOT retired.** It looks like build-1's retired free-text slots and is
  not one: after this build **nothing routes on it**. It carries the diverging entries for a human to
  read, and the routing lives entirely in the enum. A free-text slot nothing branches on is a
  payload, not an enforcement point.
- **`full-scale.md` step 4's version-skew refusal — NOT retired** (the roundtable's own negative,
  re-confirmed here). Build-4 edits only its persisted-record **format** clause; the refusal
  predicate is untouched and still detects a stale vault-local workflow copy.

## F1 — `skills/vlt-lint/references/checks.md:16` (the routing's single home)

**Current state**, verified at `6525715` (the file is 72 lines; build-1 edited `:14`/`:15` and build-3
edited `:17`/`:19` — `:16` sits between them, untouched by either, and the roadmap's capture cite of
`:16` **HOLDS**):

> `- **Sources-vs-prose agreement** — where a wiki page carries a prose `## Sources` section, compare
> it against frontmatter `sources:` (the tier-1 item in `{conventions}/write-verification.md`); an
> entry in one not traceable in the other → `sources_vs_prose_mismatches`. A page with no prose
> section is conformant — frontmatter is the source of truth. **Legal response:** reconcile the prose
> section to frontmatter `sources:` — frontmatter is the source of truth.`

**The exact change.** Rewrite the bullet whole. It must state, in this order:

1. **The finding, unchanged in jurisdiction** — where a page carries a prose `## Sources` section,
   compare it against frontmatter `sources:`; an entry in one not traceable in the other is a
   divergence. **The tier-1 citation stays** (`{conventions}/write-verification.md`) and **the
   convention is not restated** — it already states the symmetric requirement at
   `write-verification.md:38` (*"every entry in one is traceable in the other (frontmatter is the
   source of truth; a page with no prose section is conformant)"*) and the source-completeness
   requirement at `:33`. **Both directions are already violations under the convention; only the
   response differs.** This is why build-4 needs no convention edit (see F9 / E2).
2. **The direction routing** — the scanner returns which direction diverged, and the class splits:
   `diverge_prose_gap` → `sources_vs_prose_mismatches` (`fix_now`); `diverge_frontmatter_gap` and
   `diverge_unclassified` → `sources_vs_prose_unresolved` (`flag_for_human`). State the enum members
   by name; state that `diverge_unclassified` is the escape and is **never auto-fixed**.
3. **Two legal responses (R3), each bound to its direction:**
   - `sources_vs_prose_mismatches` — **add the frontmatter entries the prose section omits to the
     prose `## Sources` section.** Nothing is deleted. Frontmatter is the source of truth about what
     the page rests on, so the prose section is the side that moves.
   - `sources_vs_prose_unresolved` — **add the prose section's uncited entries to frontmatter
     `sources:`**, or rule the prose mention not a contributing source and remove it. **Never
     mechanical**: deciding a prose mention is a contributing source is a provenance judgment
     (`write-verification.md:33`, *"every contributing source"*), which is why it is flagged and not
     applied. **The citation is never deleted to make the two sides agree.**
4. **The pointer to the procedure** — the auto-fix mechanics live at `fix-and-file.md` Step 3; named
   here for the reader only, never restated.

**A14-4's residual-scope option 1 is what this implements**, verbatim from capture: *"Give the check a
second legal response — add the missing entries to frontmatter — and route by direction … Keeps the
cheap half automatic."*

**Why.** The measured 0% application rate across two consecutive full sweeps against a `fix_now` slot
whose meaning is *safe to apply serially without judgment*, plus the grounded fact that Step 3 names
no procedure for the class at all. **E1 binds the framing: the brief and the build assert nothing
about detectability-versus-remediability** — that is the filer's unverified reasoning, and no
acceptance check rests on it.

**Out of scope at this site:** the phrase *"frontmatter is the source of truth"* survives **in its
finding-definition role** (a page with no prose section is conformant). It is not re-scoped, not
qualified, and not moved. **That is E2**, and E2 is scoped out of this cycle.

## F2 — `skills/vlt-lint/references/fix-and-file.md` Step 3 (the procedure that does not exist)

**Current state**, verified at `6525715` (57 lines). Step 3's auto-fix list is `:9`–`:13`: index drift
(`:9`), frontmatter / Bases-field drift (`:10`), broken wikilinks (`:11`), formatting (`:12`),
unmarked supersession/stale callouts (`:13`). `:14` is blank; `:15` is the lint-as-attester paragraph.
**`sources_vs_prose` appears nowhere in the file** — confirmed by `grep -rn "sources_vs_prose"
skills/`, which returns six hits, none in `fix-and-file.md`.

**The exact change.** Add one bullet to the auto-fix list, after `:11` (broken wikilinks — the nearest
sibling in kind: a mechanical, non-deleting repair of a reference), reading in substance:

> - **Sources-vs-prose (`sources_vs_prose_mismatches` only)** — add the frontmatter `sources:` entries
>   the page's prose `## Sources` section omits, in the section's existing form. **Add only; never
>   remove a prose citation to make the two sides agree.** The `flag_for_human` half
>   (`sources_vs_prose_unresolved`) is **not** auto-fixed — the direction test and both legal
>   responses live at `checks.md`, *Sources-vs-prose agreement*.

**Single-home discipline is the whole shape of this edit:** the entry names the class, states the
mechanical act, and **cites** — it does not restate the direction test, the enum, or the second legal
response.

**Why.** Capture's sharpened finding: the class occupies a `fix_now:` slot *"whose Step-3 procedure
gives a fixer nothing to execute."* Adding the second legal response without adding the procedure
would leave that half of the defect exactly where it was.

## F3 — `skills/vlt-lint/references/report.md:21` + a new `flag_for_human:` slot (R4)

**Current state**, verified at `6525715`:

- `:21` — `  sources_vs_prose_mismatches: [<page: frontmatter sources vs prose Sources diverge>, ...]`,
  the last slot in the `fix_now:` block opened at `:15`. **HOLDS** — the roadmap's capture cite of
  `report.md:21` is exact.
- `flag_for_human:` opens at `:22` and runs to `:66`; the block's last slot is `malformed_frontmatter`
  at `:66`; `opportunities:` opens at `:67`.
- **Build-2's sites `:77` and `:88` are outside this F-site and are not touched.**

**The exact change**, two edits:

1. **`:21` narrowed** — the slot's inline meaning becomes the prose-gap direction only, e.g.
   `[<page: frontmatter sources: entries missing from the prose Sources section — auto-fixed>, ...]`.
2. **One new slot added to `flag_for_human:`**, sited immediately after `malformed_frontmatter` at
   `:66` (the block's tail, beside the other tier-1 structural findings):
   `sources_vs_prose_unresolved: [<page: prose Sources cites entries absent from frontmatter sources:, or a divergence the scanner could not direction-classify — never auto-fixed>, ...]`

**R4 — enumeration widening, performed in the same build.** `report.md`'s slot list is the enumeration
of the report's schema, and build-4 adds a member to it. The widening is **complete**: `grep -rn
"sources_vs_prose" skills/ tools/` establishes the class's full site set (six hits at
`6525715`), and no other file enumerates report slots — `vault-operating-contract.md:51`/`:323` name
`{lint_reports}` as a directory with no slot list and no extension, and no tool reads the slot names.
**The workflow's emitted `flag_for_human` object is the second half of this widening and is F4.**

## F4 — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` (grounding addition; the FOURTH build in this file)

⚠ **Grounding addition, per disposition 2.** The roadmap's build-4 **Touches:** list does not name this
file; grounding shows the ruled direction routing is not expressible without it. The capture named
`vlt-lint-full.js:665` as a home of the class at v0.16.1; the file is now **870 lines** after builds 1
and 2, and every cite below is re-derived against `6525715`.

**Build-3 also edits this file and is ordered before build-4** (roundtable A3). **Build-4 rebases onto
post-build-3 source** and re-runs **E5**, **E6** and **E7** against it.

### Edit 1 — `:178`, the enum (and `:179`, its detail slot)

**Current state**, verbatim:

```js
    sources_vs_prose: { type: 'string', enum: ['match', 'diverge', 'no_prose_section'], description: 'GAP B tri-state (match | diverge | no_prose_section) — apply the prompt Gap B rule, per write-verification@4' },
    sources_vs_prose_detail: { type: 'string', description: "what diverges when sources_vs_prose is 'diverge'; empty otherwise" },
```

**The exact change:**

```js
    sources_vs_prose: { type: 'string', enum: ['match', 'diverge_prose_gap', 'diverge_frontmatter_gap', 'diverge_unclassified', 'no_prose_section'], description: 'GAP B verdict — apply the prompt Gap B rule, per write-verification@4' },
    sources_vs_prose_detail: { type: 'string', description: 'the diverging entries; else empty' },
```

- **`write-verification@4` is preserved deliberately.** It is one of the **eight in-prose pin tokens**
  build-3's package-lint **E7** now validates against this file's own `// depends_on:` header
  (`:11`), and one of build-3's check-(2) grep counts (*5 `frontmatter@14` + 5 `write-verification@4`*).
  **Dropping or staling it fails E7 at the gate.** No convention version moves in build-4, so `@4`
  stays `@4`.
- **The `diverge_unclassified` escape is A35's requirement**, not decoration; it is the member a
  scanner meeting a divergence it cannot direction-classify returns, and it **reports** (through
  `flag_for_human`) rather than being refused.

**E6, measured with `_E6_NODE_EXTRACTOR` (never a source char count):** the two properties serialize
to **338** today and to **326** after; `PAGE_SCAN` **3688 → 3676**, budget **3700**. **Build-4 returns
12 characters.** The builder re-measures and records the four schema lengths.

### Edit 2 — `:229`, the page-scan prompt's Gap B clause

**Current state** (inside the `pageScanPrompt` template literal; the clause is the ninth sentence of
`:229`), verbatim:

> `For the sources-vs-prose comparison (Gap B), report sources_vs_prose: 'no_prose_section' when the
> page carries no prose ## Sources section — such a page is conformant (per write-verification@4, the
> wiki-page tier-1 item: frontmatter is the source of truth); 'diverge' only when both exist and an
> entry in one is not traceable in the other; otherwise 'match'`

**The exact change.** Replace the `'diverge'` half with the three directed members, stating the test
mechanically and **naming the escape as the safe answer**: report `diverge_prose_gap` when every
divergent entry is one **frontmatter carries and the prose section lacks**; `diverge_frontmatter_gap`
when every divergent entry is one **the prose section cites and frontmatter lacks**;
`diverge_unclassified` when **both** kinds are present **or you cannot tell which side is missing the
entry**. `'no_prose_section'`, `'match'` and the normalization sentence earlier in `:229`
(*"normalize both sides first per frontmatter@14 rule 4"*) are **unchanged**. **Preserve
`write-verification@4` and `frontmatter@14` verbatim** — both are E7-validated body tokens.

**Note the cost, priced and already paid:** editing `pageScanPrompt` moves `scanFingerprint`. Release
2 is **cold by construction** for three other reasons already; this adds nothing.

### Edit 3 — `:795` and `:797`, the reduce

**Current state**, verified: `:795` is the last entry of the `fix_now:` object; `flag_for_human:`
opens at `:797`.

```js
    sources_vs_prose_mismatches: scans.filter((s) => s.sources_vs_prose === 'diverge').map((s) => `${s.slug}: ${s.sources_vs_prose_detail || 'frontmatter sources: vs prose Sources diverge'}`),
```

**The exact change.** `:795` narrows its predicate to `=== 'diverge_prose_gap'`, and a sibling entry
is added inside the `flag_for_human:` object (after `malformed_frontmatter`, mirroring `report.md`'s
slot order) filtering `'diverge_frontmatter_gap'` **or** `'diverge_unclassified'` into
`sources_vs_prose_unresolved`, with the same `slug: detail` rendering and a default string per
direction. **Both predicates test the returned verdict**, never the detail text — the invariant
build-1 established in this file and D1 rules cycle-wide.

**Out of scope at this site:** the `cache_records`/`runKey` machinery (build-2's, untouched); every
other `PAGE_SCAN` property; the `frontmatter_defect` enum and its `unclassified` member (build-1's);
the `:11` `depends_on:` header (build-3's, and no version moves here).

## F5 — `skills/vlt-lint/references/report.md:3` (Q5's rewrite)

**Current state**, verbatim at `6525715` — **HOLDS**, the roadmap's cite is exact and build-2 did not
touch it:

> `Read on reaching Step 5. The fenced report block is strict YAML as a whole — emitted fenced
> in-session and **persisted as the plain `.yaml` file** (`vlt-lint` Step 6) — same content, no fence;
> keep it parsing whole in both homes.`

**The exact change.** **Restate the sentence whole** — Q5's ⚠ is explicit that appending to it makes
the bundle *"assert one format while permitting two."* The replacement states, in this order:

1. **The strictness survives.** The fenced in-session block is strict YAML as a whole and stays YAML
   for human reading.
2. **Two legal persisted homes, one content.** Step 6 persists it as `.yaml` (the default) **or**
   `.json`; the persisted file carries the block's content unabridged, unreordered and unreworded —
   *content-verbatim* (disposition 4). The persist step's mechanics are **not** restated here: they
   live at `vlt-lint/SKILL.md`, Step 6, and this sentence **points at it** (A8 — `report.md:3` is a
   restatement of that home, and the pointer must not invert).
3. **The no-dependency requirement, explicit** (Q5(a)) — emitting the report must require no library
   the vault does not already have.
4. **The JSON-subset emission strategy, stated** (Q5(a)) — every scalar a JSON string, lists as
   `- <json>`, nested maps by indentation. State **why**: it makes the block mechanically
   translatable to the `.json` home without a second authoring act, and it makes every vault's output
   identical instead of independently invented.
5. **The claim, and what checks it.** *"Parses whole in both homes"* is stated as a requirement with
   its enforcement point **named** — the module's release gate parses real persisted reports before
   the tag (acceptance check (1)). **No `ST-N` id and no factory-register reference appears in this or
   any shipped file** (owner ruling, 2026-08-27): the reason is stated, never cited.

## F6 — `skills/vlt-lint/SKILL.md:74` (the persist mandate's single home)

**Current state**, verified at `6525715`. The line carries **two disjoint sentences owned by two
builds**; build-4 edits only its own. Build-4's sentence, verbatim:

> `Also **persist the report** (both modes): write the Step-5 report block **verbatim** to
> `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` — plain YAML, the block's content without the fence
> (append-only — never edit, prune, or re-read-to-rewrite past reports; retention is the human's —
> lint reports are never wake-read; the operating contract's *Decay contracts* table records the
> exemption). Pre-existing `.md` reports in `{lint_reports}` stay as they are — legal, never converted
> or swept.`

**Build-2's sentence on the same line — NOT TOUCHED:** *"A full-mode sweep also rewrites the findings
cache at `_agent/lint-cache.json`, written by `scripts/lint-cache.py` — mechanics at
`references/full-scale.md` … It is **not** a report…"*

**The exact change**, confined to build-4's sentence:

- The filename becomes `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` **or** `…-lint.json`, `.yaml` named
  as the default.
- **`verbatim` is restated as content-verbatim** (disposition 4): the persisted file carries the
  block's content unabridged, unreordered and unreworded; the `.json` home is that same content
  rendered per the JSON-subset strategy at `references/report.md`, **not a second authoring act**.
  Point at `report.md` for the strategy; do not restate it.
- The append-only, retention, never-wake-read and Decay-exemption clauses are **preserved verbatim**.
- The pre-existing-`.md` clause is **preserved and widened by one word** — pre-existing reports in
  **either** format stay as they are, legal, never converted or swept. *(This is the shipped
  precedent that makes the alternative-format posture already true in this file.)*

**Why this site and not `report.md:3` alone:** A8, found independently by five voices. `SKILL.md:74`
is the persist step's **single home** and `report.md:3` is a restatement; permitting `.json` only in
the restatement would leave the executing skill mandating the other format.

## F7 — the validation beat's instrument (A10 — what "ships the check" means here)

**No new shipped file, no new script, no package-lint check.** The check A10 ordered is an
**acceptance check with a named at-rest instrument** (acceptance check (1)), and this F-site exists so
the builder does not have to invent it:

- **Subject:** real persisted lint reports — read-only copies of every `.yaml` file in
  `{field-vault}`'s `{lint_reports}` archive, the same archive build-1's checks (6) and (7) read as
  their baseline. **Never written, never moved.**
- **Instrument, `.yaml` home:** a strict YAML load per file — `uv run --with pyyaml python -c
  "import sys,yaml;yaml.safe_load(open(sys.argv[1],encoding='utf-8').read())"` — factory-side, at
  rest. `uv` is a declared tool whose stated purpose is PEP 723 inline deps (A9); **this adds no
  `machine_tools` row because it adds no vault-side step.**
- **Instrument, `.json` home:** the most recent archived report, re-rendered per the JSON-subset
  strategy F5 documents, parsed by stdlib `python3 -m json.tool`. This is the emission point's own
  first exercise: if the documented strategy cannot render a real report, the documentation is wrong
  and the check fails.
- **It can fail, and failing is informative.** An archived LLM-authored report that does not parse is
  precisely the defect A14-5 predicted and nobody had ever tested. Record the failure verbatim; do
  **not** repair the archive (it is the vault's, append-only).
- **Fallback, and its cost:** if the archive is not reachable from the build machine, the instrument
  degrades to a **synthetic specimen report** carrying the content classes that break naive emission
  (em-dashes, colons inside values, `→` arrows, quoted strings, nested maps, an empty list, a
  denominated literal). ⚠ **Rule R2's observer duty then fires** — the builder records the
  synthetic-fixture reach in the BUILT `status:` and it is named at closeout.

## F8 — the four restatement sites (`.json`'s permission, propagated)

Each is a **restatement** of F6's single home and each currently mandates `.yaml` alone. All four
`file:line` cites are re-derived at `6525715`.

- **`skills/vlt-lint/SKILL.md:76`** — the failed-run paragraph. Current: *"it persists a
  `…-lint-failed.yaml` failed-run record."* **Change:** name both extensions; the refusal predicate
  and the "mechanics live in `full-scale.md`" pointer are untouched.
- **`skills/vlt-lint/references/full-scale.md:10`** (step 4 — **build-4's half of the shared file**).
  Current: *"write a **failed-run record** to `{lint_reports}/YYYY-MM-DD-HHMM-lint-failed.yaml` (plain
  YAML: `status: failed`, the `reason`, …)"*. **Change:** the record may be `.yaml` or `.json`, same
  content, same fields, same dir-level Decay exemption. **Everything else in step 4 is untouched** —
  the `files_checked`/`files_cached` predicate, the stale-copy diagnosis, the directed refusal, the
  `next:` line. *Ruled here rather than left open: A10 asked whether the failed-run record accepts
  both extensions. It does — a vault that persists `.json` reports and `.yaml` failure records would
  carry two formats for one class for no reason, and the failed record is read by the same reader.*
- **`skills/vlt-lint/references/full-scale.md:13`** (**build-4's second half**). Current:
  `churn_since_last_full` counts pages whose mtime postdates *"the most recent prior full-mode report,
  by its dated filename."* ⚠ **A8's silent wrong number.** **Change:** the discovery matches **both**
  extensions, so a `.json`-persisting vault is not invisible to its own history and does not render
  `unmeasured (no prior full report)` forever. The instrument-naming rule and the
  `unmeasured`/`not measured` literals are untouched.
- **`skills/vlt-setup/SKILL.md:194`** — provisioning. Current: *"`vlt-lint` persists its dated Step-5
  reports there (plain `.yaml`)"*. **Change:** `.yaml` (default) or `.json`. The never-clobber clause
  is untouched.

**Out of scope at this F-site, dispositioned:** `vlt-setup/SKILL.md:195` and `vlt-upgrade/SKILL.md:132`
persist the **upgrade** report as plain `.yaml`. **Not touched** — A14-5 is about `vlt-lint`'s report
class, no upgrade-report defect is filed, and widening the permission to a second skill's report
class is unmeasured scope. Named so a later reader does not read the asymmetry as an oversight.

## F9 — the governance bundle (a NON-site, verified)

**Verified at `6525715`, and the reason build-4 owes no handshake:**

- `vault-operating-contract.md:51` (the address table) and `:323` (the Decay-contracts table) name
  `{lint_reports}` as a **directory**, with **no file extension** in either row. A `.json` persist is
  therefore already legal under the contract as written. **No contract edit ⇒ no package-lint C6
  ⇒ no `vault-rule-card.md` re-derivation and no `sha256:` re-stamp.**
- `write-verification.md` is at `version: 4` with `consumers: [vlt-ingest, vlt-extract, vlt-research,
  vlt-lint, vlt-lint-full.js]` (build-3's bump). **`:33` and `:38` already state the symmetric
  sources requirement and the source-completeness rule that F1's second legal response rests on** —
  the convention authorizes both directions today. **Nothing in `write-verification.md` moves, and
  E2's prohibition is honoured by construction, not by discipline.**
- **No convention `version:` moves in build-4 ⇒ no consumer walk, no re-ack, package-lint E1/E5
  unchanged.**

## Registration

**`None.`** No new skill, no new workflow, no new script, no `module-help.csv` row, no
`.claude-plugin/marketplace.json` `skills[]` entry. No convention `version:` moves, so no consumer
walk is owed. **No `machine_tools` row is owed** — build-4 adds no vault-side tool assumption
(disposition 5).

**"No bump owed" is not "no cost" — priced anyway:**
- **package-lint C6** — not triggered; no governance-bundle file is edited (F9).
- **package-lint E4** — not triggered; build-4 adds no `package-lint` check, so no declaring case in
  `tools/test-package-lint.py` and no `CASE_FLOOR` bump is owed. *(Build-3 took `CASE_FLOOR` 23 → 24
  for E7; build-4 leaves it there.)*
- **package-lint E5** — the asset ack at `vlt-lint-full.js:11` is **not** edited; no version moves.
- **package-lint E7** — **triggered and load-bearing.** Build-4 edits two of the eight E7-validated
  in-prose pin sites (`:178`, `:229`). Both pins are preserved at their current versions; the builder
  runs E7 and confirms the token counts build-3's check (2) established.
- **package-lint E6** — triggered; re-measure, expect **3676**.
- **package-lint D** — this is the release build; see §Release.

## Out of scope (dispositioned)

1. **E2 — the *"frontmatter is the source of truth"* qualifier.** SCOPED OUT of this cycle by ideation
   and re-confirmed here. `write-verification.md`'s tier-1 item (`:38`) is **not touched**, and the
   phrase survives verbatim in its finding-definition role at `checks.md:16`. Routed by roundtable
   A32: **the owner files it to `factory/inbox/` as a `pattern`**, so a later capture grounds it, and
   it is carried at closeout as a deferred question. **Not build-4's, and not silently dropped.**
2. **E1 — the detectability-vs-remediability root-cause account.** Attached as **context, never a
   premise**. Asserted nowhere in this brief, in no F-site's *Why*, and in no acceptance check. The
   fix stands on the measured 0% application rate and on the grounded absence of a Step-3 procedure.
3. **A vault-side validation beat for the persist.** Deferred with its reason and its price
   (disposition 6): it owes no `machine_tools` row, so the cheap route exists — but it adds a step to
   a shipped sweep on unmeasured benefit, and the measured defect is the unchecked claim, which
   acceptance check (1) closes. **Carried to closeout as a Cycle-14 carry-forward.**
4. **Making `.json` the default persist.** Rejected in disposition 5, with the two costs grounding
   named (`vlt-setup/SKILL.md:194`; `full-scale.md:13`'s filename-based discovery).
5. **Shipping a report emitter / extending `lint-cache.py`.** Rejected in disposition 3 — Q5 option 4,
   still not taken.
6. **The `vlt-upgrade` report class.** Untouched (F8's disposition).
7. **Per-entry (rather than per-page) direction routing.** Considered and rejected: `diverge_unclassified`
   already covers the mixed-direction page and routes it to the conservative slot, and per-entry
   routing would put a page in both slots at once for no gain in what a fixer can safely do.
8. **`full-scale.md` steps 2, 3 and 5 (`:8`, `:9`, `:11`, `:12`)** — **build-2's**, by roundtable A8 as
   ruled in `briefs/build-2-findings-cache.md`. Not touched.
9. **`checks.md:14`/`:15`** (build-1's) and **`:17`/`:19`** (build-3's) — not touched. Build-4's edit at
   `:16` sits between them and collides with neither.

## Verification (unit, at rest — lifecycle step 5)

Run all of these before the commit; record the outputs in the BUILT `status:`.

- **V1 — the routing fixture (the build's own end-to-end).** A node harness over the shipped
  `vlt-lint-full.js` reduce with five stub scans, one per enum member, `args` delivered as a **JSON
  string** (the runtime contract; parse-on-intake at `:77` is untouched), and the agent/parallel/phase/
  log/budget hooks stubbed — the V-harness pattern build-1 established. Assert: `diverge_prose_gap`
  appears in `fix_now.sources_vs_prose_mismatches` **and nowhere else**; `diverge_frontmatter_gap` and
  `diverge_unclassified` appear in `flag_for_human.sources_vs_prose_unresolved` **and never in
  `fix_now`**; `match` and `no_prose_section` produce neither.
- **V2 — the parse run** (F7's instrument, in full). Both homes, real archive material, the fallback
  and its R2 record if the archive is unreachable.
- **V3 — the greps for cross-file agreement.**
  - `grep -rn "reconcile the prose section to frontmatter" skills/` → **zero**.
  - `grep -rn "sources_vs_prose" skills/` → the class's full site set, each hit accounted for
    (`checks.md:16`, `fix-and-file.md` Step 3, `report.md` ×2, `vlt-lint-full.js` ×5).
  - `grep -rn "plain \`\.yaml\`\|plain YAML\|-lint\.yaml\|-lint-failed\.yaml" skills/` → every
    surviving hit is either the **upgrade** report class (out of scope, F8) or a site that now names
    both extensions.
  - `node --check skills/vlt-setup/assets/workflows/vlt-lint-full.js` parses.
- **V4 — E6, re-measured with package-lint's own `_E6_NODE_EXTRACTOR`**, never a source char count.
  Expect `PAGE_SCAN` **3676** (from 3688; budget 3700) and the other three schemas unchanged.
- **V5 — Packaging lint.** `uv run tools/package-lint.py` (A/B/C/E) green mid-build, **E7** clean over
  the eight in-prose pins with `:178`/`:229` preserved at `write-verification@4` / `frontmatter@14`.
  The `--expect-version` gate is §Release.
- **Handshake bipartite re-check — `not applicable` as a re-check, but Group E still runs.** No
  convention `version:` moves and no `consumers:` list changes, so no re-ack is owed; **package-lint
  Group E is nonetheless the check of record** and is run whole. **No hand-written `grep "<name>@"
  skills/` is written as a verification** — it is self-confirming and is never the recorded check.
- **R2 — fixture extension: not applicable.** Build-4 adds and changes no release-gate check, so
  `tools/test-package-lint.py` and `CASE_FLOOR` are untouched. *(R2's other sense — the roundtable's
  synthetic-fixture observer duty — fires only on F7's fallback path; see F7.)*
- **R3 — legal response: applicable, and discharged at the check's own single home.** The class's two
  legal responses are stated at `checks.md:16` in the same build that changes the class (F1).
- **R4 — enumeration widening: applicable, and performed in the same build.** `report.md`'s slot list
  and the workflow's emitted `flag_for_human` object both gain `sources_vs_prose_unresolved` (F3, F4).
- **Scrub.** No personal or vault-local content in any changed shipped file; worked examples use
  placeholder paths; **no `ST-N` study-register id appears anywhere in the shipped surface** (owner
  ruling 2026-08-27 — verified zero instances before this build; the builder re-verifies zero after).
- **No `.decision-log.md` left in the working tree.**

## Release (this IS the release build for release 2)

**Release 2 = builds 2, 3 and 4**, on branch `cycle14-release2`, one commit per build. Build-4 carries
the release choreography that build-2's check (7) and build-3's check (1) both deferred to it.

- **Both version strings bump, in this build:** `.claude-plugin/marketplace.json` `"version"` and
  `skills/vlt-setup/assets/module.yaml` `module_version`, currently **0.16.2** in both.
  **Recommended: `0.17.0`** — a minor, because release 2 ships a new shipped script, a renamed vault
  sidecar the governance contract enumerates, three convention `version:` bumps with 19 re-acks, a new
  release-gate check (E7), a changed workflow return shape and a changed report schema. **The owner
  confirms the number at `vlt-release`;** the acceptance check is written against the released version,
  not against a literal.
- **The gate:** `uv run tools/package-lint.py --expect-version X.Y.Z` — **tag only on exit 0**, and the
  PASS summary line goes in the release commit message (skipping the lint is then visible in history).
- **Then:** ff-merge `cycle14-release2` → `main`, tag `vX.Y.Z`, push main + tag.
- **`vlt-release` owns the choreography** as one gated sequence (pre-flight, handshake, dual bump, lint
  gate, commit, ff-merge, tag, push). Do not hand-roll it.
- ⚠ **The CHANGELOG entry for this release collects all three builds' `title:` lines verbatim.**

## Acceptance (live — appended to the roadmap ledger)

**Cycle ruling D3 as amended (roundtable A17) governs: a BOUNDED discharging event — at rest, at the
release gate, or on the next ordinary upgrade — is `[ship-verifiable]` and it GATES.** Per rule **R1**,
every ship-verifiable check below names **which seam its named instrument actually crosses**.
**Six checks — all `[ship-verifiable]`, all GATE; none field-contingent.**

**(1) `[ship-verifiable]` — at rest — GATES. ⚠ THIS IS A10's VALIDATION BEAT, AND IT IS THE FILING'S
CURE.** A persisted report parses whole, **on real material**: every `.yaml` report in read-only copies
of `{field-vault}`'s `{lint_reports}` archive loads under a strict YAML parser, and the most recent one,
re-rendered to `.json` per the emission strategy F5 documents, parses under `python3 -m json.tool`.
**It can fail** — an archived LLM-authored report that does not parse is exactly what A14-5 predicted
and what nothing has ever tested; the failure is recorded verbatim and the archive is not repaired.
Instrument: `uv run --with pyyaml` (a declared tool, factory-side, adding no vault-side assumption) plus
stdlib `json.tool`, over copied archive material, at rest. **Seam: agent-authored report block →
persisted file → machine reader** — the seam `report.md:3` asserts and nothing checked, which is the
whole filing. Evidence: file count, per-file verdict, any parse error verbatim, in the BUILT `status:`.
⚠ Fallback path (archive unreachable) is the synthetic specimen of F7, and **rule R2's observer duty
then fires**: recorded in `status:`, named at closeout.

**(2) `[ship-verifiable]` — at rest — GATES.** The direction routing has an enforcement point that is
not prose. Over the **shipped** reduce: `diverge_prose_gap` lands in
`fix_now.sources_vs_prose_mismatches` and nowhere else; `diverge_frontmatter_gap` and
`diverge_unclassified` land in `flag_for_human.sources_vs_prose_unresolved` and **never** in `fix_now`;
`match` and `no_prose_section` produce neither. **It can fail** — a predicate written against
`sources_vs_prose_detail` instead of the verdict passes a reading and fails this. Instrument: the V1
node fixture, five stub scans, `args` as a JSON string, factory-side at rest. **Seam: scanner verdict →
report slot** — the tier assignment A14-4 files as wrong. Evidence: both arrays verbatim.

**(3) `[ship-verifiable]` — at rest — GATES.** The destructive instruction is gone and the second
response exists. `grep -rn "reconcile the prose section to frontmatter" skills/` returns **zero**;
`checks.md:16` states **two** legal responses routed by direction, names `diverge_unclassified` as
never-auto-fixed, and **cites** `fix-and-file.md` for the procedure without restating it;
`fix-and-file.md` Step 3 carries the class's entry and **cites `checks.md` for the direction test**;
`report.md` carries both slots. Instrument: the V3 greps plus a read of the four edited sites, at rest.
**Seam: module source → vault-read documentation** — named as such, not dressed as behavioural.
Evidence: grep output plus the four rewritten lines.

**(4) `[ship-verifiable]` — at rest — GATES.** The persist permission has **one** format story and no
site still mandates the other — A8's finding, closed. `SKILL.md:74` permits both homes and defines
`verbatim` as content-verbatim; `report.md:3` is **restated, not appended to**; `SKILL.md:76`,
`full-scale.md:10` and `vlt-setup/SKILL.md:194` name both extensions; **`full-scale.md:13`'s churn
discovery matches both**, so a `.json`-persisting vault is not invisible to its own history. **It can
fail** — leaving any one of the five restatements at `.yaml`-only reproduces the inverted pointer this
check exists to catch. Instrument: the V3 format greps plus a read of the six sites, at rest.
**Seam: the persist step's single home → its five restatements** — the seam A8 found five voices deep.
Evidence: grep output plus the six lines.

**(5) `[ship-verifiable]` — at the release gate — GATES. ⚠ THIS IS THE GATE build-3's CHECK (1) LEFT TO
BUILD-4.** `uv run tools/package-lint.py --expect-version X.Y.Z` exits **0** with **both** version
strings bumped, **E6** measuring `PAGE_SCAN` at **3676** (down from 3688 — build-4 returns 12 characters
to a budget that had 12), **E7** clean over the eight in-prose pin tokens with `:178`/`:229` preserved at
`write-verification@4` / `frontmatter@14`, and **E1/E5/C6 unchanged** (no convention `version:` moves and
no governance-bundle edit in this build). Instrument: package-lint Groups A/B/C/D/E at the release commit.
**Seams: source tree → release gate**, and for E6 specifically **source literal → runtime serialization**.
Evidence: the PASS summary line in the release commit message plus the four measured schema lengths.

**(6) `[ship-verifiable]` — bounded to the first full `{field-vault}` sweep after release 2 — GATES.**
The 0% application rate is cured, **measured not assumed**. In that sweep every
`sources_vs_prose_mismatches` entry is either applied (it appears in `fixes_applied:`) or its
non-application is recorded with its reason, and **no** `sources_vs_prose_unresolved` entry is
auto-applied. Baseline, from the persisted `{lint_reports}` archive: **26 then 25 instances across two
consecutive full sweeps, zero applied, both runs declining the whole class for the same recorded
reason.** **It can fail:** a `fix_now` entry declined again for a judgment reason means the routing did
not cut the populations apart, and the class belongs in `flag_for_human` whole (A14-4's own fallback
option 2). Instruments, two and different: the archive for the baseline (no new sweep needed) and the
live post-upgrade sweep. **Seam: live wiki corpus → the routed check → the serial fixer** — the seam
where the misclassification was measured and the only one that can show the routing working. Event: the
owner runs `vlt-lint --full` on `{field-vault}` after upgrading to release 2; performer: the owner;
vault: `{field-vault}` only. ⚠ That sweep is **COLD by construction** (three fingerprint movers across
release 2) — coldness is not a finding and does not affect this check, which reads per-page scan
verdicts.

**No check binds a vault to choosing the `.json` persist**, and that is deliberate. `.json` is a
permission, nothing in the build, the release or the upgrade causes a vault to take it, and a check
requiring it would be the unbounded species wearing a ship-verifiable tag. The `.json` path's emission
is exercised at rest instead, in check (1).

## Next lifecycle move

A **fresh builder session** implements this brief via `bmad-workflow-builder`. Exit obligations:
rewrite this brief's `status:` to a **BUILT record with numbered deviations** (including R2's
observer record if F7's fallback path was taken), delete any `.decision-log.md`, **one commit for the
build**. Then **`vlt-release`** — build-4 is the last build of Cycle 14 and carries release 2's dual
version bump and `--expect-version` gate.

⚠ **Two cycles remain open and `factory/CYCLE` holds one line** (A24). Before running
`acceptance-discharge` or `cycle-closeout` against **Cycle 13**, hand-point `factory/CYCLE` at
`13-trusted-returns` and restore it immediately after. **Never run either headless while that is true.**
