---
title: 'Cycle 14 — no enforcement point'
status: '**CLOSED 2026-09-01** — the no-enforcement-point cycle. **THREE RELEASES SHIPPED 2026-08-27**: **v0.16.2** (build-1, release commit `bd985a6`, tag `v0.16.2`), **v0.17.0** (builds 2/3/4, release commit `c02fe3d`, tag `v0.17.0` @ `b3c8646`), **v0.17.1** (build-5 hot-fix, `56cde45`, tag `v0.17.1` @ `da8ff4d`) — all pushed to origin, every release gate clean (`package-lint: A/B/C/E PASS, D PASS`). Build-6 was briefed and then **WITHDRAWN 2026-09-01** before any code shipped; nothing was released for it and its six checks are struck. **Acceptance: discharged over FIVE passes (2026-08-27 ×2, 2026-08-31, 2026-09-01 ×2) plus three owner rulings.** Final tally — **36 checks in 6 items: 32 DISCHARGED · 3 FAILED · 1 BLOCKED · 0 STILL-OPEN · 0 SPLIT.** Every check in the cycle is graded; nothing awaits an event. ⚠ **The ledger''s three ticked items are NOT a measure of what the cycle proved** — items tick only when all of their checks discharge, and three of the six carry a single graded FAIL apiece. **The cycle closes on ONE gating FAIL, deliberately and honestly: build-3 (6), the two parked interims'' unwind.** All three of its clauses are unmet — park #15 (`extraction.md`) is still LIVE and un-superseded, park #16 (`write-verification.md`) was RE-PARKED not unwound (vault `307c901`, both halves verified in-vault at `decision-log.md:1259` and `:1446`), and `para_type_unknown`''s legal response was not executed (that clause was build-6''s). **A green was available only by falsifying a `type:` field**: the vault re-derived both parks, found one of the rules itself defective, and filed for its retirement rather than executing an exit it believes false — `decision-log.md` v4''s mechanism working exactly as intended. **Two headline outcomes.** (i) **THE FINDINGS CACHE HIT — first time in three cycles.** Shipped in Cycle 12, refuted as b2(5) (*"has never once worked"*), rebuilt as build-2, and observed warm on pass 4: `files_cached: 141` / `files_checked: 5` / `cache_rejected: 0` under the same fingerprint the prior sweep wrote — scan-page agents **146 → 5**, prompt chars **591,152 → 20,294**, **96% off the scan phase**. ⚠ Its first attempt was cold and discarded, because `full-scale.md` step 2 under-specifies two of its four fingerprint slots — filed, and it plausibly explains the three-cycle failure. (ii) **Build-1 check (2) re-graded Cycle 13''s refuted acceptance check on six real vault subjects: PASS — Cycle 13''s closeout gate was REOPENED and Cycle 13 closed 2026-08-27.** **Also first-of-kind:** the cycle''s two `class: supersession` filings (`2026-09-01-160000`, `2026-09-01-170000`) are **P-15''s retirement rail''s first use**, and build-6''s withdrawal was ruled on the finding that it was a perimeter patch on **`ST-2`** (*location as proxy for trust*). **Carried forward past Cycle 14 (authoritative list in §Carried forward past Cycle 14 + its CLOSEOUT ADDENDUM 2026-09-01):** **build-3 (6) FAILED → BOUND DEBT, ship-verifiable so it GATES Cycle 15** (owner-ruled at closeout); **build-1 (6) FAILED → BOUND DEBT, ship-verifiable so it GATES Cycle 15** (owner-ruled 2026-08-31; E4 transfers at `10 / 8 genuine / 2 refuted at 146 pages`, a sample not a measurement); the ten ideation-time deferrals (A14-2''s enumeration, the `summary` paraphrase, the general reduce-side posture, tracker #13, the `malformed_frontmatter` retirement, `para_author_unknown`, E2, Cycle 12''s A12-4/A12-5/A11-11 d4/A12-1 inheritance, the `:168` dissent, `{field-vault}` overlay staleness); and the two supersession retirements, which go to **Cycle 15 ideation''s obsolescence beat**. **Not carried:** the inherited Cycle 12 b3(7) — graded BLOCKED on its third unfired run, filed as `2026-08-31-104502-…`, and the carry ends there; build-5 (6) FAILED field-contingent, routed to platform **[P-20]** as its fourth instance, no module filing owed. ⚠ **Owed, not blocking:** neither supersession filing has been posted through `vlt-feedback` (invoked-only, needs the owner''s explicit go), so park #16 references no live tracker issue. **Closeout 2026-09-01:** 6 filings moved to `filings/`, 3 held live in `factory/inbox/` (`…-164501` A14-2 deferred by A23, `…-125529` A14-6 = park #15''s clause, `…-141418` A14-7 = park #16''s clause); tracker issues **#12** and **#14** closed; `factory/CYCLE` reset to none. **Platform work landed during this cycle: P-19, P-20, P-13** (channel visibility floor; six `plat:` commits, none touching the shipped surface, no platform item closed). ⚠ **This roadmap is [P-13]''s first COLD exercise of its widened done-when and it FAILED four times before correction** — three `acceptance-discharge` passes and this closeout each stamped inside the existing `## Next lifecycle move` heading with superseded routing below it, following this file''s newest-at-top convention in preference to the map''s *last block in the file* rule; the foot was restructured at closeout and **P-13 stays open on a negative cold exercise**, which is also a [P-20] instance. **This cycle is closed — do not append.** — **Superseded working history (the OPEN status as it stood at close):** OPEN — captured 2026-08-26, **8 filings** grounded against module source at v0.16.1. **IDEATION COMPLETE** (four owner-steered rounds, every slot ruled): **4 builds, 2 releases** — b1 reduce-side (A14-1 + A14-3), b2 findings cache (A14-8), b3 governance (A14-6 + A14-7 — **SETTLED at build-3''s brief 2026-08-27: 3 conventions / 19 re-acks / 11 files** (`extraction.md` 7→8 joins, A13+A15), plus **8 in-prose pin tokens at 6 sites that the handshake gate cannot see — given an enforcement point, package-lint `E7`**; E6 price ZERO, `PAGE_SCAN` stays 3688), b4 lint references (A14-4 + A14-5 — **BRIEFED 2026-08-27; the release build for release 2**, routing single-homed at `checks.md:16`, `vlt-lint-full.js` a grounding addition, E6 price **−12** (`PAGE_SCAN` 3688 → 3676), no serializer, no `machine_tools` row); **build-1 is released alone** because it **gates Cycle 13''s closeout**. Cycle-wide ruling D3, **as amended at the roundtable**: a **bounded** check (at rest, at the release gate, or on the next ordinary upgrade) is ship-verifiable and it GATES — an at-rest instrument is one sufficient bound, not the criterion. `ST-6` opened at D4. Scope was owner-ruled at capture — defects and blockers from Cycles 12–13 only, net-new deferred (tracker #13). **ROUNDTABLE COMPLETE 2026-08-26** — 32 amendments applied, 2 rules, 4 owner-ruled disputes (2 dissents on record), 0 open, 6 retirements; `build-brief`''s gate is satisfied. **RELEASE 1 SHIPPED 2026-08-27 — v0.16.2 @ `bd985a6`, tag `v0.16.2` (`594b958`), build-1 built at `ceb5cb2`; package-lint A/B/C/E PASS, D PASS.** Build-1''s 8 acceptance checks are ALL ship-verifiable and ALL GATE (D3-as-amended); **6 of 8 graded at rest, 6/6 PASS** — including **check (2), which re-grades Cycle 13''s refuted acceptance check on six real vault subjects: PASS. Cycle 13''s closeout gate is REOPENED.** Checks (6) and (7) bound to the first live full sweep after upgrade. **RELEASE 2 SHIPPED 2026-08-27 — v0.17.0 @ `c02fe3d`, tag `v0.17.0` (`b3c8646`); builds 2/3/4 plus an ST-N scrub, a contract widening and two inbox filings. Lint gate `A/B/C/E PASS, D PASS — vlt 0.17.0`; handshake 9 conventions / 39 pins bipartite-consistent; **19 acks re-pinned across 3 moved conventions** (write-verification 3→4, frontmatter 13→14, extraction 7→8) and 8 in-prose recitations re-stated, now guarded by the new **E7** gate check — which passed on its first real release. **ALL FOUR BUILDS SHIPPED; the cycle is code-complete.** At-rest acceptance: build-2 7/7 PASS, build-3 5/5 PASS, build-4 **4 of 6 PASS with check (1) FAILED** (owner-ruled: keep the honest FAIL, do not re-scope; the unparseable archive report is filed). **Next: two independent tracks — owner runs `vlt-upgrade` on `{field-vault}` for release-2 acceptance, then `run acceptance discharge`; and Cycle 13''s acceptance re-run (hand-point `factory/CYCLE` at `13-trusted-returns` first, restore after, never headless).** **ACCEPTANCE DISCHARGE RUN 2026-08-27 — acceptance PARTIALLY discharged; the cycle CANNOT CLOSE.** Graded against release 1''s upgrade + the first full sweep after it, release 2''s upgrade post-flight, both release commits, and shipped source at `c02fe3d`. **30 checks: 23 DISCHARGED, 2 FAILED, 4 STILL-OPEN, 1 SPLIT, 0 BLOCKED**; all five ledger items stay UNCHECKED and no filing archived. **Discharged incl. build-1 (7) — `unmarked_supersessions` reached ZERO against a 3-all-false baseline, so the `:168` dissent does NOT become the ruling** — and build-3 (6)''s trigger half: `governance_rule_changes:` rendered non-empty with three rule-worded entries and BOTH parked interims were re-derived (the unpark trigger A14 demanded fired). **TWO STANDING FAILS, both gating:** build-4 (1) (1 of 6 archived reports unparseable — owner-ruled KEPT, filed `2026-08-27-153000`) and **build-1 (6)** (the `malformed_frontmatter` bound MET on both escape classes at zero but FAILING leg 3 — 10 flagged / 8 genuine / 2 refuted by a different, scanner-side mechanism, filed `2026-08-27-160000`; E4 transfers with that number, not zero). **Build-3''s check (4) DISCHARGED AS WRITTEN with a caveat on record: every clause holds and the property it protects is violated** — `extraction.md:84` vs `:190` give the operational-record class two memberships; the check tested single-home-ness, never membership (filed `2026-08-27-171000`, ship-verifiable at rest). **Build-3 (6) is a partial:** the `extraction.md` park''s blocker is RESOLVED (5 files, matching the 5 at park time) but the `write-verification.md` park resolves only partially — jurisdiction narrowed by artifact class ONLY, the partner-sitting reading explicitly refused, 29 unattested Layer-3 files outside `{wiki}` of which only 1 is exempted, so 28 remain in jurisdiction. **NO full sweep has run after release 2 (owner-deferred), so build-3 (7), build-4 (6) and build-2 (8) are STILL-OPEN awaiting their named event, not failed.** **Distance from closeout: two owner acts** — (i) one `vlt-lint --full` on `{field-vault}` under 0.17.0 (discharges build-3 (7) + build-4 (6)), then a SECOND with no ruleset change between (discharges build-2 (8)); (ii) the two parks'' unwind. Then `cycle-closeout` must rule the two standing FAILs. **HOT-FIX RELEASE 3 SHIPPED 2026-08-27 — v0.17.1 @ `56cde45`, tag `v0.17.1` (annotated), build-5 built at `3910974`; package-lint A/B/C/E PASS, D PASS; NOT YET PUSHED (owner-gated).** Build-5 repairs the contradiction build-3 shipped in v0.17.0 hours earlier (filing `2026-08-27-171000`): the Layer-3 operational-record class is `charter | record | register` at all ten enumerating sites, and a `charter` is exempt from attestation jurisdiction. Handshake: `write-verification` 4->5 (5 re-acks) and `extraction` 8->9 (4 re-acks) — the extraction bump ruled a RULE CHANGE (its `:190` is the appointed definition site and the edit moves a shipped check''s population); `frontmatter` held at 14. **The membership-agreement check this build introduces is the enforcement point build-3''s check (4) lacked** — (4) tested single-home-ness and never compared members — and it earned its keep on first run by finding a SIXTH defective site the filing had missed (`vault-operating-contract.md:66`, the Layer-3 entry condition). Build-5''s 4 ship-verifiable checks ALL GATE and ALL PASS at rest; its 2 field-contingent checks ride the 0.17.1 upgrade. Predecessor Cycle 12 CLOSED 2026-08-26; Cycle 13 remains OPEN, now gate-open, awaiting its acceptance re-run (a SEPARATE act — hand-point `factory/CYCLE` first, restore after, never headless). **ACCEPTANCE DISCHARGE PASS 2 — 2026-08-27, after `{field-vault}` took BOTH remaining upgrades (0.16.2 → 0.17.0, then the 0.17.0 → 0.17.1 hot-fix; the 0.17.1 run clean on every durability axis — 7 mints preserved, 2 overlays intact, no base/skill-asset/manifest/governance divergence, no collisions).** Six checks graded — **build-5''s whole ledger, which pass 1 predates**: **4 DISCHARGED and TICKED** ((1) membership 10/10 sites agree at rest, (2) E1/E5 clean with ZERO stray `@8`/`@4` pins, (3) C6 digest `8f8a7116…` matches byte-for-byte, (4) E7 clean with `:684` at `write-verification@5`) — **the first ticked boxes in the cycle**, each re-verified independently at rest by the run rather than accepted on the build''s say-so (`package-lint --expect-version 0.17.1` re-run: A/B/C/E PASS, D PASS). **build-5 (5) STILL-OPEN — the predicted 28 → 27 was measured EXACTLY (2 exempt, 27 in jurisdiction) but by the upgrade post-flight, NOT the `vlt-lint --full` sweep the check names**; graded honestly rather than discharged on an adjacent instrument, consistent with the identical call already made for build-3 (7). **build-5 (6) FAILED `[field-contingent, does NOT gate]` — the `write-verification.md` park was RE-SURFACED, not unparked** (*"STILL LIVE AND STILL UNRULED … the hot-fix moved exactly one file out of the population; it did not move the park"*), blocker intact for 27 files. ⚠ **PREMISE CORRECTION ON RECORD: the park''s blocker is the REFUSED PARTNER-SITTING READING and the unchanged `verified_by` roster (A14-7 / filing `2026-08-26-141418`), NEVER the charter-membership contradiction** — and the 0.17.0 post-flight said so hours BEFORE build-5 was briefed. **A live, real-time instance of [P-20] (the check adversary) — its FOURTH, and the first observed as it happened; added to P-20''s evidence table in the same commit.** No inbox filing drafted or owed: the signal is factory-side (a mis-written check, not a module defect) and routes to the platform ledger. Corroboration logged but grading nothing: the skill manifest moved **67 → 68** at 0.17.0 (`lint-cache.py`) and held **steady at 68** through the hot-fix — build-2''s verification step V6 confirmed in the field, but **no ledger item names the manifest**. **Cumulative: 36 checks in 6 items — 27 DISCHARGED · 3 FAILED · 5 STILL-OPEN · 1 SPLIT · 0 BLOCKED.** The two GATING FAILs are unchanged (build-1 (6), build-4 (1)); build-5 (6) does not gate. **Distance from closeout is unchanged in acts but ONE act now buys more: a single `vlt-lint --full` under 0.17.1 discharges THREE checks** (build-3 (7), build-4 (6), build-5 (5)), a second consecutive sweep discharges build-2 (8), the two parks'' unwind remains the human''s call, and then `cycle-closeout` must rule the two standing gating FAILs. **ACCEPTANCE DISCHARGE PASS 3 — 2026-08-31, over `{lint_reports}/2026-08-30-1123-lint.yaml`: the FIRST full `vlt-lint --full` sweep taken under 0.17.1, the sweep passes 1 and 2 both recorded as deferred.** 146 checked / 0 cached / 146 listed, cold by construction. **5 checks graded: 2 DISCHARGED · 2 BLOCKED · 1 STILL-OPEN**, plus one evidence refresh. **build-4 (6) DISCHARGED** — the 0% application rate is CURED on the named instrument: 10 `sources_vs_prose_mismatches`, **5 applied** and in the build''s own direction (frontmatter → prose, where the 08-27 baseline ran the reverse), 5 refused as over-reports with a per-page reason each, and the misrouted `unmarked_supersessions` entry **reclassified by the routing** to flag-only; ⚠ caveat filed — the report omits `fixes_applied:` entirely though `report.md:72` mandates it, so the check''s named location did not exist to look in. **build-5 (5) DISCHARGED and TICKED** — `para_missing_attestation` reads **27** on the sweep the check names, the two operational-record files (`projects/fantasy-2026/charter.md` + `record.md`) verified exempt at rest, and the two instruments now AGREE where at 0.17.0 they read 28 vs 27; ⚠ **but the check could not have failed** — the 08-27 sweep already read 27 under 0.16.2 before either carve-out shipped, so a failed repair would have read the same. **[P-20] instance #5, and the FIRST caught at grading time rather than after.** ⚠⚠ **build-3 (7) BLOCKED (unreachable), owner-ruled — `[ship-verifiable]`, so the cycle gains a THIRD GATING item.** Its bound event fired; the sweep rendered `para_missing_attestation` as a **27-file rollup string** where `report.md:32` mandates a per-file list, and **no shipped surface produces the `type:` distribution the check names** (`vlt-lint-full.js:812-814` returns the slot empty as *"a structural slot the SKILL fills"*). Its own fail conditions were UNTRIPPED — this is unreachability, not contradiction. **INHERITED Cycle 12 b3(7) BLOCKED, owner-ruled** — pass 1''s own third-run instruction came due; `[field-contingent]`, does NOT gate; **filed rather than carried a fourth time** (8 `{resources}` writes and four partner-session lanes since 0.17.1, and the legality question was never posed: the tail has a trigger but **no cause**). **build-2 (8) STILL-OPEN — sweep 1 of 2, and the WRITE LEG IS FIELD-CONFIRMED FOR THE FIRST TIME** since the cache shipped: `_agent/lint-cache.json` verified at rest, 156 KB, fingerprint `31f40c2cc90313a41dd3|bd6e1e211804a2011af`, 146 records — the half b2(5) never once achieved across Cycles 12 and 13. **build-1 (6) refreshed, grade UNCHANGED (FAILED, GATES)**: the sweep reads `malformed_frontmatter: []`, but the 8 genuine specimens were repaired inside the 08-27 sweep and ⚠ **the 2 REFUTED specimens vanished with no cause** on a corpus the report itself certifies unchanged (*"0 of 146 pages changed … scanner variance on an identical corpus"*) — **the specimen set is NOT REPRODUCIBLE**, E4 still transfers with `10 / 8 / 2`, and this is **[P-19]''s first field instance**. **THREE FILINGS FILED, all owner-confirmed:** `2026-08-31-104500` (the report shape is stated in `report.md` and enforced nowhere — three instances, one root cause; **the filing build-3 (7)''s BLOCKED rests on**, and Cycle 14''s own through-line arriving inside Cycle 14''s own instrument), `2026-08-31-104501` (the `stubSlugs` discovery regex requires a bare `## Stubs` heading, so an EMPTY stub list reached the workflow and manufactured 3 false `missing_targets` — ⚠ capture must ground the `file:line`), `2026-08-31-104502` (the no-cause check species; factory-side, cousin of [P-20]). **Cumulative: 36 checks in 6 items — 29 DISCHARGED · 3 FAILED · 1 STILL-OPEN · 1 SPLIT · 2 BLOCKED.** **The sweep bought two discharges and cost one blocker.** **THREE OWNER RULINGS RECORDED 2026-08-31, after the pass**, clearing the gate to a single item: **build-4 (1) RE-GRADED DISCHARGED** on its forward subject — v0.17.0 shipped 11:57 on 2026-08-27 and `2026-08-27-1104` was written at 11:04, so **`2026-08-30-1123` is the FIRST report ever written under the mandate and it PARSES** (all 7 archived reports re-parsed at rest; the lone failure `2026-08-24-1700` is pre-mandate and read-only by the check''s own terms); ⚠ **this ruling rests on a CONTESTED READING and is the one to reopen if closeout disagrees** — under the check''s literal population 1 of 7 still fails, and this ledger says two different things about who may narrow it (pass 1: *the successor build''s at brief time, not this run''s*; §Next lifecycle move: *the re-grade belongs to `acceptance-discharge`*), both quoted at the annotation. **build-3 (7) RE-GRADED DISCHARGED WITH CAVEAT** — the `type:` distribution was measured at rest this run (**29: `area` 22 · `project` 3 · `resource` 2 · `record` 1 · `charter` 1**, minus the 2 carved out = **27**, reproducing both the sweep''s 27 and the post-flight''s 29) and is derivable from the shape `report.md:32` ALREADY mandates; ⚠ an owner-ruled instrument substitution, **narrow precedent only** — it does not disturb the two substitution refusals this ledger already made. **build-1 (6) FAIL STANDS, carried as BOUND DEBT to Cycle 15, ship-verifiable so it GATES there** — not fixed in-cycle because the reproducibility problem is upstream of the counting problem; the bound is leg 3 alone on the first full sweep after the Cycle 15 release. **Tally after rulings: 36 checks — 31 DISCHARGED · 2 FAILED · 1 STILL-OPEN · 1 SPLIT · 1 BLOCKED.** ⚠⚠ **CYCLE 14 NOW HAS EXACTLY ONE GATING BLOCKER: build-3 (6), the two parks'' unwind** — (a) `extraction.md`, blocker resolved, needs a superseding decision-log entry + the legal response executed on ≥1 of 5 files, both owner acts available today; (b) `write-verification.md`, 27 files, blocker is the **refused partner-sitting reading and the unchanged `verified_by` roster** (NOT the charter contradiction v0.17.1 fixed), where **keep-the-hold with a stated exit condition is a legal disposition**. **NO filing was withdrawn and no defect ruled away** — the gate moved, the module did not; all four filings route to `inbox-capture` live. **⚠ PARK 1 RE-DERIVED 2026-08-31 — IT DOES NOT UNWIND, and a FIFTH FILING was written.** Re-derived against `extraction.md` v9 per the park''s own standing instruction: the ruling it waited on landed and **the re-derivation found the RULING defective.** `extraction.md:84` removes the `{wiki}` subtree from the PARA population **BY NAME**, so `resources/wiki/`''s **146 files carrying `type: wiki`** (module-canonical, non-PARA) are legal while `resources/briefs/`''s identically-shaped **8** are a finding forever — *"one carve-out by name"* (`contract:70`) is a **completeness-claiming list of ONE** that fell behind an addition, the module''s own lists-drift discipline failing inside its own convention. **And the rule INVERTS:** `:84` admits vault-declared overlay schema but forbids declaring **module** vocabulary, so a vault typing its briefs `dispatch-brief` is conformant today while `{field-vault}`, which used the module''s own accurate word `research`, is permanently not — **strictest against the vaults that use the vocabulary correctly.** Both stated legal responses require writing something false, and ⚠ **the vault already refused this exact move once in park 2 and `write-verification.md:55` v5 RATIFIED the refusal** (*"fusing permission to provenance is the write-path failure this exemption exists to prevent"*) — falsifying `type:` for `para_type_unknown` is the same act as falsifying `verified_by:` for `para_missing_attestation`. **Filed `2026-08-31-152000-para-type-carve-out-is-an-enumeration-of-one-and-penalizes-accurate-vocabulary.md`**; direction: **generalize the carve-out into a vault-declarable typed subtree** (both halves already ship — `module.yaml:45` declares `{wiki}` as a configurable path, and declare-at-birth declares types — the module has simply never let a vault say *this declared subtree carries this type*), which also makes the owner''s consistent-and-intentional position **enforceable**: the declaration is the intention, conformance to it the consistency, and it is a STRICTER check than today''s, not a looser one. Population refreshed **5 → 8** — the growth rate the park priced has fired once, on schedule. **Disposition: a superseding `parked-interim` against the NEW filing**, an owner act not yet written. ⚠⚠ **CONSEQUENCE: build-3 (6) is now expected to be graded FAILED and it GATES** — it requires both parks *re-derived AND unwound* plus the legal response executed, and park 1 is re-derived but deliberately not unwound. **Cycle 14 therefore closes on ONE honest gating FAIL rather than a clean gate** — the check fails because the module is wrong, which is what an acceptance check is for; retyping 8 files to a value the vault believes false to turn a gate green is the failure mode this cycle is named for. **⚠⚠ BUILD-6 WITHDRAWN 2026-09-01 — owner-ruled, before any code was written; all 6 checks STRUCK; nothing shipped and `extraction.md` stays at `version: 9`.** Superseded by `factory/inbox/2026-09-01-160000-supersession-…` — **the FIRST USE of P-15''s `supersession` class**, the retirement rail built 2026-08-25 and unused for a week while the thing it was built for happened again. **The friction behind park #15 is not a clause defect; it is `ST-2` (*location as proxy for trust*, `status: standing`)**: Cycle 12 retired that proxy for `author:` and `trust:` and left it standing for **`type:`**, and Cycle 14 **build-3 restated and strengthened it** six days after `ST-2` opened. Build-6 answered with a **new mechanism** plus a **minimal-scope ruling cutting out the `{wiki}` unification** — the half that makes it a category rather than an allowlist entry — which is `ST-2` RC2 exactly (*"the minimal patch [is] the rational move every time — which is exactly how a root cause survives four cycles"*). Filing `2026-08-31-152000` is **superseded too** and withdraws at capture. ⚠ **build-3 (6) reverts to an EXPECTED GATING FAIL** — park #15 cannot unwind under v9 without writing something false — so **Cycle 14 closes on ONE honest gating FAIL** and the retirement goes to **Cycle 15 ideation**, where P-15''s **obsolescence beat** is the beat built to receive it. Superseded ruling, retained: **BUILD-6, a hot-fix, NOT a carry to Cycle 15.** `git log -S` established the defect was shipped by **this cycle''s own build-3** (`e42429d`, v0.17.0) — **the second defect in the same `extraction.md:84` statement** after build-5 repaired the first — so build-5''s precedent governs and it is repaired in-cycle. **Scope owner-ruled MINIMAL** (the prohibition gains a **subtree qualifier**; unifying `{wiki}` is **OUT**, to Cycle 15). **BRIEFED** `briefs/build-6-declared-typed-subtree.md`, 6 checks appended (5 gating, 1 field-contingent), release **v0.17.2** cut alone, `extraction` **9→10** ruled a RULE CHANGE with 4 re-acks. ⚠ **build-3 (6) therefore becomes PASSABLE, not an expected FAIL** — under v10 park #15 can unwind by declaring the subtree, writing nothing false. ⚠ **build-6 check (4) carries a MANDATORY CONTROL** (a different non-PARA `type:` in the same subtree must still report) — **[P-20]''s question asked at brief time rather than discovered afterward, the first check in this cycle written that way.** ⚠ A correction is on record in the filing and memory: the direction is **LOOSER by one declared value per declared subtree**, not stricter — an earlier framing claimed a stray `type: wiki` under `{briefs}` is invisible today, and `checks.md:19` shows it is already flagged; what makes it safe is **scope**, not strictness. **⚠ PASS 4, 2026-09-01 — THE CACHE HIT. build-2 (8) DISCHARGED and its item TICKS at 8/8; NO STILL-OPEN CHECK REMAINS.** The second consecutive sweep (`{lint_reports}/2026-09-01-1406-lint.yaml`, run by a peer session and **re-verified here against the persisted report, not taken on relay**) read `files_cached: 141` / `files_checked: 5` / `cache_rejected: 0` under the **same fingerprint the 2026-08-30 sweep wrote** — *"WARM - the first warm run this vault has recorded"* — with the 5 rescans being exactly the 5 pages the prior sweep auto-fixed, as pass 3 predicted. **The findings cache shipped in Cycle 12, was refuted as b2(5) (*"has never once worked"*), was rebuilt as build-2, and is now observed working for the FIRST TIME IN THREE CYCLES.** Cost effect — the direct answer to the owner''s objection: scan-page agents **146 → 5**, prompt chars **591,152 → 20,294**, dispatches **172 → 31** (**96% off the scan phase**). ⚠⚠ **Large caveat, now its own filing: the run''s FIRST ATTEMPT WAS COLD AND WAS DISCARDED** — `full-scale.md` step 2 pins its two *digest* slots exactly and its two *component* slots not at all, `pin_vector` was read as a JSON array (workflow needs a string → slot missing → fingerprint composed EMPTY) and `convention_digests` as the 8 pinned conventions rather than all 9 in `{conventions}`. Only hand-debugging made it warm; **a vault following the shipped doc gets a permanently cold cache and a report that says nothing is wrong — which plausibly explains the three-cycle failure the check was written to end.** **Tally now 36 checks — 32 DISCHARGED · 2 FAILED · 0 STILL-OPEN · 1 SPLIT · 1 BLOCKED.** **FOUR FILINGS ADDED 2026-09-01:** `093000` (fingerprint **over-broad** — `module_version` forces a cold sweep every release), `140600` (fingerprint inputs **under-specified** — fails **silently**; different cause, different fix, may be briefed with `093000`), `140601` (same-page heading anchors reported as missing targets — 2nd consecutive sweep, cause diagnosed: `normalizeTarget` returns an empty string and reports it), `140602` (a scanner **substituted a proper noun** — `cornerboxes` for `cornerbacks` — and on its 2nd occurrence was **served from the CACHE**, so a scanner error is now permanent for the sidecar''s life and re-running cannot re-derive it). ⚠ Filing `104500` **corrected**: its instance (a) rollup recurred a 3rd time but (b)/(c) did NOT — the render is **intermittently** wrong, a stronger claim than consistently wrong. ⚠ **#15''s population moved 5 → 8 → 9 in three days** — the park''s scope is the `type:` not the count, so the ruling is unmoved, but the blast radius is compounding. **PASS 5, 2026-09-01 — build-3 (6)''s SPLIT RESOLVES to FAILED; EVERY CHECK IN THE CYCLE IS NOW GRADED.** Park #16''s re-park landed in `{field-vault}` (vault `307c901`, sweep `2026-09-01-1519`, 27 dispatches — 145 of 146 reused), **both halves verified in-vault by this run** at `decision-log.md:1259` (the 2026-08-26 park annotated `superseded_by:`/`superseded_date:`/`superseded_reason:`) and `:1446` (the new `parked-interim` carrying `supersedes:`). ⚠ **All three of (6)''s clauses are unmet:** park #15 is **still LIVE and un-superseded** (no `superseded_by:` on it — verified at rest) because under `extraction.md` v9 it cannot unwind without writing something false; park #16 was **RE-PARKED, not unwound** (a re-park is a re-derivation, and the check''s word is *unwound*); and `para_type_unknown`''s legal response was **not executed** — that clause was build-6''s, and build-6 is withdrawn. **The FAIL is the honest outcome, not a process failure: a green was available only by falsifying a `type:` field.** The vault re-derived both parks, found one of the rules itself defective, and filed for its retirement rather than executing an exit it believes false — `decision-log.md` v4''s mechanism working exactly as intended. **Tally: 36 checks — 32 DISCHARGED · 3 FAILED · 0 STILL-OPEN · 0 SPLIT · 1 BLOCKED**; nothing awaits an event. ⚠ **Owed, not blocking:** neither supersession filing is posted through `vlt-feedback`, so park #16 references no live tracker issue the way #15/#16 do — `vlt-feedback` is invoked-only and needs the **owner''s** go, deliberately not taken by any agent. Three workflow filings strengthened to their **third** consecutive sweep (heading-anchor false positive, the cache-served `cornerboxes` substitution — its amplification claim now independently confirmed, and the `fantasy-platform-read-access` orphan, whose filing title says *two*). **Next: run `cycle-closeout`** — it rules the one gating FAIL and closes.; independently, a SECOND `vlt-lint --full` **taken BEFORE any release** discharges build-2 (8) (non-gating) and adds a second member to build-4 (1)''s thin post-mandate population.'
module_code: 'vlt'
created: '2026-08-26'
updated: '2026-08-26 (opened by inbox-capture; GitHub intake materialized 5 issues; 8 filings captured and graded; 1 deferred by owner ruling; Cycle 12''s six bounded tails ruled at the bound; **IDEATION COMPLETE — filled over four owner-steered rounds, every slot ruled: 4 builds, 2 releases, build-1 cut alone to reopen Cycle 13''s gate; ST-6 opened**; **ROUNDTABLE CONVENED + CONVERGED 2026-08-26 — full 13-voice roster, 32 amendments, 2 rules, 4 disputes ruled, 6 retirements, D5 confirmed**); **2026-08-27 — build-1 BRIEFED, BUILT @ `ceb5cb2` and RELEASED as v0.16.2 @ `bd985a6`, tag `v0.16.2` pushed to origin; 6/6 at-rest acceptance checks PASS incl. the Cycle 13 re-grade**; **2026-08-27 — build-2 BRIEFED + BUILT @ `d641050`; build-3 BRIEFED (`briefs/build-3-governance-handshake.md`) — re-ack figure SETTLED at 19, the in-prose pins given package-lint `E7`, `checks.md:17` ruled in scope, cite-not-restate ruled, E6 price measured at zero; 7 acceptance checks + Cycle 12''s inherited b3(7) appended to the ledger**; **2026-08-27 — build-4 BRIEFED (`briefs/build-4-lint-references.md`), the LAST build of the cycle: the `sources_vs_prose` direction routing single-homed at `checks.md:16`, `vlt-lint-full.js` added as a grounding addition (the scanner returns no direction) at an E6 price of MINUS 12 (`PAGE_SCAN` 3688 → 3676), no report serializer ruled and no `machine_tools` row owed, 6 acceptance checks appended; it is the RELEASE BUILD for release 2**; next: build 4, then `vlt-release`); **2026-08-27 — build 4 BUILT and RELEASE 2 SHIPPED as v0.17.0 @ `c02fe3d`, tag `b3c8646` pushed; all four builds shipped, cycle code-complete; next: `vlt-upgrade` for release-2 acceptance, then `acceptance-discharge`**; **2026-08-27 — ACCEPTANCE DISCHARGE RUN over both releases'' evidence: 30 checks graded 23 DISCHARGED / 2 FAILED / 4 STILL-OPEN / 1 SPLIT / 0 BLOCKED, all five ledger items still UNCHECKED, no filing archived, no new filing owed (the three from today already cover every contradiction); build-1''s specimen-set Half 2 FILLED at 146 pages; next: the owner''s post-0.17.0 `vlt-lint --full` sweeps + the two parks'' unwind, then `cycle-closeout` rules the two standing FAILs**); **2026-08-27 — ACCEPTANCE DISCHARGE PASS 2 over the 0.17.1 hot-fix upgrade: build-5''s six checks graded 4 DISCHARGED (ticked — the cycle''s first ticks) / 1 FAILED / 1 STILL-OPEN; build-3 (6) refreshed 28 → 27 with its grade unchanged; pass 1''s verdicts untouched; build-5 (6)''s FALSE PREMISE recorded and added to [P-20]''s evidence table as its fourth instance and first real-time one; no filing drafted; cumulative 27/3/5/1/0 across 36 checks; next: ONE `vlt-lint --full` on `{field-vault}` under 0.17.1 (discharges three checks at once), then a second consecutive sweep, the two parks'' unwind, then `cycle-closeout`**); **2026-08-31 — ACCEPTANCE DISCHARGE PASS 3 over the first full sweep under 0.17.1: 5 checks graded 2 DISCHARGED (build-4 (6); build-5 (5), ticked) / 2 BLOCKED (build-3 (7), **which GATES**, and the inherited Cycle 12 b3(7)) / 1 STILL-OPEN (build-2 (8), sweep 1 of 2, write leg field-confirmed); build-1 (6) refreshed with its grade unchanged and its specimen set shown NOT reproducible; 3 filings filed; cumulative 29/3/1/1/2 across 36 checks; **the gate grew from two gating items to three**; **then THREE OWNER RULINGS the same day cut it back to ONE** — build-4 (1) re-graded DISCHARGED on a contested reading, build-3 (7) re-graded DISCHARGED with a narrow substitution caveat, build-1 (6)''s FAIL carried as bound debt gating Cycle 15; tally 31/2/1/1/1; **the only gating blocker left is build-3 (6), the two parks**; next: the parks, then `cycle-closeout`, with a second sweep before any release**)'
derives_from:
  - 'factory/inbox/2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md'
  - 'factory/inbox/2026-08-26-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md'
  - 'factory/inbox/2026-08-26-164502-html-escaped-scanner-return-fails-an-exact-comparison.md'
  - 'factory/inbox/2026-08-26-123144-reclassify-sources-vs-prose-mismatches-out-of-fix-now.md'
  - 'factory/inbox/2026-08-26-123153-lint-mandates-strict-yaml-persist-with-no-yaml-library.md'
  - 'factory/inbox/2026-08-26-125529-recognized-type-names-no-owning-convention.md'
  - 'factory/inbox/2026-08-26-141418-layer-3-open-entry-vs-closed-verified-by-roster.md'
  - 'factory/inbox/2026-08-26-141838-findings-cache-cannot-round-trip-writer-and-reader-disagree.md'
predecessor: 'factory/cycles/13-trusted-returns/roadmap.md (Cycle 13 — SHIPPED v0.16.1 @ `c18c591` 2026-08-26; OPEN and GATE-SHUT for acceptance, closed to capture, cannot close without a Cycle 14 repair)'
intent: >
  Cycle 13 shipped a guard on the premise that a rule stated in a prompt and enforced nowhere
  does not bind. The guard then failed in the field within hours, for the same reason: its own
  enforcement point had to parse scanner-returned free text in order to decide whether to trust
  a scanner-returned claim. Cycle 14 opens on the generalized form. Every entry here names a
  rule the module genuinely states and a place that is supposed to enforce it, and in each case
  the enforcement point is missing, unreachable, or lacks the one input that would let it
  decide — the reduce that cannot read a page, a fix_now class whose auto-fix procedure never
  names it, a strict-YAML mandate with no parser, an entry condition whose vocabulary has no
  named owner, an open writer set meeting a closed attester roster. This is a deliberate
  debt-clearing cycle: it takes the blockers the last two releases left open and adds no new
  capability.
---

## The through-line

Cycle 12 asked what a claim rests on. Cycle 13 asked what the *reduce* rests on and answered it
for one case — then watched the answer break in the field on 2026-08-26, refuted on a named
subject by the first live post-upgrade sweep. Cycle 14 is what that failure generalizes to.

The shape, stated once: **the module states a rule, and names a place responsible for it, and
that place is missing, unreachable, or cannot carry out the judgment the rule requires.**
*(roundtable A28, 2026-08-26 — restored to the `intent:` block's own trichotomy. The tidied
headline had dropped the **missing** case, which is the case the cycle is titled for: A14-4's
auto-fix procedure and A14-5's validator were never written, not written-and-unreachable. A brief
quoting the old sentence would scope A14-4 as re-wording an existing procedure rather than
authoring one.)* Not because the rule is wrong, and
not because the enforcement was forgotten — in every one of the eight captures below, the half
that was written was written deliberately and is individually defensible.
*(roundtable A27/A28, 2026-08-26: was "seven" and "both halves" — the capture holds eight, and
A14-4/A14-5/A14-8 are cases where the second half was never written at all.)* The defect is the *seam*.

Eight filings, three seams: *(roundtable A27, 2026-08-26)*

**The scan → reduce seam (A14-1, A14-2, A14-3).** `vlt-lint-full.js` fans out to LLM scanners and
reduces their returns with exact, careful JavaScript. The reduce has the arithmetic; it does not
have the page. All three of this sweep's false findings come from the reduce performing precise
work over a value it has no way to verify — prose (A14-1), an enumeration (A14-2), an encoding
(A14-3). The workflow's filesystem-free design (`vlt-lint-full.js:36-38`) is the structural
reason: it is what keeps the fan-out clean and it is what makes verification impossible from
inside. Cycle 13's own §Carried forward already named the general answer (*every agent-returned
value that is mechanically checkable at the reduce is checked there*) and deferred it once.
The field has now paid for that deferral three times in one sweep.

**The stated-mandate seam (A14-4, A14-5, A14-8).** A promise written into a schema or a reference with
nothing shipped that could keep it. `sources_vs_prose_mismatches` sits in the `fix_now:` slot —
the slot meaning *safe to apply serially without judgment* — and the auto-fix procedure it would
be applied by never mentions it (A14-4). `report.md` requires the persisted report parse as
strict YAML "whole, in both homes" and the module ships nothing that emits it and nothing that
checks it (A14-5). Both are the Cycle 13 premise one layer out from the workflow: an instruction
at a site with no enforcement point. **A14-8 is the seam's purest form and arrived after this
section was first written**: the findings cache's record shape is a contract stated in code on the
read side and in prose on the write side, meeting at a file on disk that nothing validates — so the
mechanism has never once worked, and no shipped instrument could see it.

**The roster seam (A14-6, A14-7).** Two shipped governance surfaces that each answer correctly
and answer differently. Layer 3's entry condition requires "a recognized `type:`" and never names
the recognizing convention, while `frontmatter.md` ships a non-exhaustive list and
`extraction.md` ships a closed set that excludes one of the other's canonical values (A14-6). The
contract declares the Layer-3 writer set explicitly open, and `write-verification.md` closes the
attester set to write ops — so a write the contract calls legal cannot satisfy the condition of
its own legality (A14-7). Both are 0.16.0 residue: that release moved Layer 3's boundary from
location to attestation and walked three of the four legs to their homes. The two that did not
move are exactly these.

**Why the three seams are one cycle and not three.** Cycle 13's diagnosis — *a rule stated where
it cannot bind* — was written about a schema description read by an LLM. Every entry here is that
same sentence with a different pair of surfaces substituted in. A14-7 is the governance-side twin
of A14-1: in one, JavaScript trusts a claim it cannot check; in the other, a partner must produce
an attestation it cannot legally hold. Fixing them as eight unrelated patches *(roundtable A27)* is available and is
what "instances only" means; the roadmap records that the option exists and that ideation, not
capture, rules on it.

## Owner ruling — debt-clearing scope (2026-08-26)

Ruled at capture, before grounding, and recorded here because it shaped what this run covered.

**The ruling:** Cycle 14 carries forward the **defects and blockers** from Cycles 12 and 13 only.
Lingering issues from the last two releases are closed out **before** any net-new capability
opens. Capture applied it as an admission test, not as a grading input — every filing this run
touched was still fully grounded.

**Admitted from the inbox at capture (7):** *(roundtable A27, 2026-08-26)* A14-1..A14-3 (the three defects the Cycle 13 discharge run filed), A14-4
(`kind: defect`), A14-6 and A14-7 (both blocking a live `{field-vault}` `parked-interim`), and
A14-5 — filed as `kind: candidate` but **owner-reclassified as a blocker at capture**: the module
mandates a machine-readable artifact and ships no means to produce it, on an environment class
(PEP 668) that is now the default rather than the exception.

**Deferred from the inbox (1) — NOT one of the eight captures:** `factory/inbox/2026-08-26-123151-lint-full-inline-args-payload-costs-the-caller-84kb.md`
(tracker **#13**) — a request for a new `argsPath` invocation route for `vlt-lint-full`. Net-new
capability; it stays in `factory/inbox/` un-captured and is **not** in this cycle's
`derives_from:`. Its issue is labeled `captured` on the tracker because the intake materialized
it this run; that label records materialization, not admission to this roadmap.

*(roundtable A27, 2026-08-26 — the arithmetic above is accidentally consistent with the wrong set.
**7 + 1 = 8 does not account for the eight captures.** The deferred one (#13) is not among them;
**A14-8 is admitted and uncounted here** (it arrived via Cycle 12's b2(5) tail, not the inbox
admission test); and the three Cycle 13 carry-forwards are admitted separately at §Carried forward.
**Eight captures, eleven admitted items.**)*

⚠ **The deferral is not clean, and ideation must see why.** Cycle 13 §Carried forward item 1
records that fixing the paraphrased-verbatim field "costs a SKILL-side per-page arg on the
`pageHashes` precedent (`:47-49`) — and that arg moves the joint against tracker **#13**'s payload
cost." The same is true of A14-2's and A14-3's mechanical-verification directions and of the
general posture. **Any resolution that gives the reduce ground truth needs a payload route, and
#13 is that route.** If ideation takes the posture, #13 stops being net-new and becomes a
dependency; the owner would then re-admit it by ruling. Capture does not pre-empt that — it
records the joint so the ruling is made with it in view.

## Capture — 8 filings (grounded against module source 2026-08-26, at v0.16.1 @ `c18c591`)

Every `file:line` below was re-derived this run against working-tree source; none was taken from
a filing on faith. Where a filing's own `provenance_guess` was checked and held, that is stated —
three of the four rail filings guessed their sites exactly, which is unusual and is worth the
record.

### A14-1. The reduce-side guard is defeated by a scanner that cites the rule it applies (2026-08-26) — `factory/inbox/2026-08-26-164500-reduce-guard-residue-rule-defeated-by-a-scanner-that-cites-its-rule.md`

**⚠ This is the cycle's gating entry.** Cycle 13's acceptance check (2) is ship-verifiable, GATES
its closeout, and is FAILED by owner ruling on this filing's evidence. Cycle 13 has no discharge
path left — (2) is refuted, not waiting — so only a shipped repair moves it, and Cycle 13 is
closed to capture. **Cycle 13 cannot close until a Cycle 14 build lands this.**

**CONFIRMED — the guard, the predicates, and the defeat mechanism.** Both dispositions end in the
same conjunction. `attestationOnlyComplaint()` at `vlt-lint-full.js:612-617` and
`inventedRequirement()` at `:623-628` each require, as their final term, `claim.residue === ''`.
`parseClaim()` at `:593-603` normalizes the claim text (`:584` `normalizeClaim`, lowercase +
non-alphanumeric collapse), consumes every recognized frontmatter key longest-first from
`KNOWN_FRONTMATTER_BY_LENGTH` (`:580`), and returns whatever survives the `CLAIM_FILLER` strip
(`:589`) as `residue`.

*(roundtable A29, 2026-08-26 — four cites corrected against working-tree source. As written the
entry gave `:591` for **both** `normalizeClaim` and `CLAIM_FILLER`, asking one line to carry two
constants, and `:579` for `KNOWN_FRONTMATTER_BY_LENGTH` (that line is its comment). Small in
itself; **not small in a build whose scope is "retire these exact lines"**, under a header
asserting every cite was re-derived. Build-1's brief re-derives every `file:line` at brief time.)*

A scanner that **cites the rule it is applying** defeats the conjunction on two independent legs
at once, and the citation is the cause of both:

- the quoted rule text leaves prose the filler list does not cover, so `residue !== ''`; and
- the quoted rule names `type:` and `author:`, both real members of `PAGE_REQUIRED_FRONTMATTER`
  (`:569`), so `fieldsNamed(claim, PAGE_REQUIRED_FRONTMATTER).length === 0` is also false.

Either leg alone suppresses the guard. The discharge run reproduced this at rest against shipped
source: the 2026-08-25 bare form yields `residue=""` and is REFUSED; the 2026-08-26 rule-citing
form yields `named=[verified_by, verified_at, author, type]` and a non-empty residue, and is not
refused. **Nothing about the pages changed — only the scanner's phrasing did.**

**GAP CONFIRMED — the comment at `:559-561` is now false as written.** It states the guards "never
fire on a claim they cannot positively identify — the failure direction is over-reporting, never
swallowing a genuine schema break." The first half is the residue rule and it holds. The claim
the comment makes about *safety* is the one the field refuted: over-reporting is indeed the
failure direction, and that is precisely why the guard silently stops working the moment a
scanner gets more verbose. A guard whose population is "the subset whose wording happened to be
terse" has no stable population at all. Whatever build takes this must correct the comment or
retire the claim — a shipped comment asserting a safety property the field has refuted is the
same defect one level further out.

**Residual scope, stated honestly.** The filing's own diagnosis is the durable one and capture
does not improve on it: the enforcement point *parses scanner-returned free text in order to
decide whether to trust a scanner-returned claim*. Any fix that keeps that shape is a
better-tuned parser, and the next rephrasing finds the next hole. Cycle 13's §Carried forward
item 2 (the general posture) is the named alternative. **Which of the two Cycle 14 takes is
ideation's ruling, not capture's** — but note the asymmetry: the narrow fix reopens Cycle 13's
gate sooner, and the general fix is the only one that also answers A14-2 and A14-3.

**Cites `ST-5`** (`factory/studies/ST-5-specimens-have-no-owner.md`). Cycle 13's roadmap carries
the standing correction unchanged, and this filing sharpens it rather than restating it: the
instrument for check (2) was the *recorded returns*, and those returns were themselves an
unrepresentative subset — every one of them bare-form, which is exactly the subset the guard
handles. The instrument could not observe the failure mode the check was written to catch. That
is ST-5's second cause (*an instrument authored from the fix's shape cannot observe what the
fix's author did not anticipate*) with a new and unusually clean specimen: the substitution that
made the check pass is visibly *why* it passed.

*Not carried, deliberately (restated from Cycle 13 so a later reader does not read it as an
oversight):* the prompt-side prohibitions at `vlt-lint-full.js:159`/`:168` that the guard makes
redundant are **kept** as defence in depth. They remain correct and cheap, and a scanner that
honours them produces less work for the guard.

### A14-2. The page scanner under-returns outbound links, and one miss manufactured an orphan (2026-08-26) — `factory/inbox/2026-08-26-164501-page-scanner-under-returns-outbound-links-and-manufactures-an-orphan.md`

**CONFIRMED — the consumption path.** The reduce normalizes the agent's returned
`outbound_links` at `vlt-lint-full.js:354`, builds the inbound map from it at `:363`, and computes
`orphans` at `:377` as the scans with no inbound entry. `outbound_links` is agent-returned
(`:158`, `required` at `:148`); nothing between the scanner and `:363` verifies it. The filing's
field measurement — 11 of 146 pages under-returning, 23 dropped instances, exactly 1 wiki→wiki,
manufacturing the sweep's only orphan — is consistent with this path.

**CONFIRMED — the severity bound, in the direction the filing states.** A dropped link lowers an
inbound count and can therefore fabricate an orphan; it cannot raise one, so it cannot hide a
true orphan. `missing_targets` at `:385` iterates the returned links, so a dropped link is never
iterated and cannot fabricate a missing target. Both halves hold.

**Sharpened — the filing understates its own blast radius on two counts.**

1. *`missing_targets` is not "undamaged in direction" — it is silently under-inclusive.* A
   dropped link that pointed at nothing is a real missing target that goes unreported. The filing
   is right that the class gains no false positives; it is wrong that the class is undamaged. The
   false-negative direction is the one nobody notices.
2. *There is a third consumer the filing does not mention.* `near_duplicates` reads
   `outbound_links` at `:397` (the hub-excluded link sets) and again at `:452-455` (the shared-link
   count and the direct-citation test, gated on `NEAR_SHARED_MIN` at `:396`). Dropped links
   suppress shared-link signals, so under-returned pages are under-detected as near-duplicates.
   Three consumers inherit the incompleteness, not one.

**PROVENANCE CORRECTION — candidate direction 1 is not implementable where the filing puts it.**
The filing proposes that "the reduce (or a cheap non-agent pass) can count them itself." It
cannot: `vlt-lint-full.js:36-38` states the division explicitly — *"the SKILL has filesystem
access, this script has none."* The workflow never sees page bytes. A mechanical `[[...]]`
extraction must run SKILL-side and arrive as an argument, on the `pageHashes` precedent at
`:47-49`. **That is the #13 payload joint** (§Owner ruling above), and it applies to candidate 2
as well, since a cross-check needs the same mechanical count. Capture does not rule the direction
out — it corrects where the work lands and names the cost the filing did not know about.

Candidate 3 (ask the scanner to return links more carefully) is named **to be rejected** by the
filing itself, on the grounds that prompt-side fixes failing is the entire premise of Cycle 13.
Capture agrees and records it so ideation does not re-derive the rejection.

### A14-3. An HTML-escaped scanner return failed the reduce's exact comparison (2026-08-26) — `factory/inbox/2026-08-26-164502-html-escaped-scanner-return-fails-an-exact-comparison.md`

**CONFIRMED — the comparison and its deliberate strictness.** `category_no_match` at
`vlt-lint-full.js:670` tests `!h2set.has(s.category)`, and the comment at `:668-669` states the
binding is "case-sensitive by design: no trimming, no case folding." A scanner returning
`Energy &amp; Clean Tech` for a page carrying `Energy & Clean Tech` fails a `Set.has()` against
the un-escaped heading. The filing's field result — the sweep's only `category_no_match`, and
false — follows directly.

**CONFIRMED — the filing's framing of the fix.** The exactness is not the bug. Loosening the
comparison (candidate 3) retires a class of true drift finding in order to work around a
transport defect, and leaves the transport defect live for every other exactly-compared field.
The filing names this to be rejected; capture agrees.

**Sharpened — both sides of the comparison traverse an agent, and the filing only noticed one.**
`h2set` is built at `:643` from `indexScan.h2_headings` — the **index scanner's** returned value,
not a mechanically parsed heading list. So the exposure is symmetric, and the two sides are not
equally severe:

- a `&amp;` on the **page** side produces one false finding (what the field hit);
- a `&amp;` on the **index** side produces a false `category_no_match` for **every page in that
  category at once**, because the entire `h2set` member is wrong.

The fan-out-wide failure is the one that has not fired yet. Any repair that normalizes only the
page-side `category` leaves the worse half live.

**GAP CONFIRMED — this is the second face of A13-1 Finding 2, and the filing identifies it
correctly.** `PAGE_SCAN` marks fields *verbatim* in schema descriptions (`:158` for
`outbound_links` — *"verbatim; do not normalize"*; `:162` for `summary`), and Cycle 13 established
that a schema description is an instruction, not an enforcement point. Cycle 13's §Carried forward
item 1 is the **paraphrase** face of that finding; this is the **re-encoding** face. The comment
at `:543` states the design posture — *"Verdicts computed from verbatim extractions (B5-3) — the
scanner reads, JS does the arithmetic"* — and that posture is sound. Nothing enforces the word
*verbatim* in it.

### A14-4. `sources_vs_prose_mismatches` sits in `fix_now:` and its fix direction deletes real provenance (2026-08-26) — `factory/inbox/2026-08-26-123144-reclassify-sources-vs-prose-mismatches-out-of-fix-now.md` (`origin: mggower/bmad-module-vlt#12`)

**CONFIRMED — the classification.** The class is in the `fix_now:` block in both homes: the report
schema at `skills/vlt-lint/references/report.md:21`, and the emitted report at
`vlt-lint-full.js:665` (inside the `fix_now:` object opened at `:652`; `flag_for_human:` opens at
`:667`).

**CONFIRMED — the fix direction and its asymmetry.** `skills/vlt-lint/references/checks.md:16`
states the legal response as *"reconcile the prose section to frontmatter `sources:` — frontmatter
is the source of truth."* Applied where prose cites sources frontmatter omits — the direction the
filing measured as dominant — that instruction deletes real citations. The filing's field
evidence (26 then 25 instances across two consecutive full sweeps on ~146 pages, **zero**
auto-applied, both runs declining the whole class for the same recorded reason) is a 0%
application rate against a slot whose meaning is *safe to apply serially without judgment*.

**GAP CONFIRMED, and sharper than the filing knew — the class has no auto-fix procedure at all.**
`skills/vlt-lint/references/fix-and-file.md` Step 3 is the auto-fix list: index drift, frontmatter
/ Bases-field drift, broken wikilinks, formatting, unmarked supersession/stale callouts. It does
**not** name `sources_vs_prose` anywhere; a `grep` for the token across `skills/vlt-lint/` returns
exactly two hits, `report.md:21` and `checks.md:16` — the slot and the check, never the procedure.
So the class occupies a `fix_now:` slot whose Step-3 procedure gives a fixer nothing to execute,
and the only stated direction lives in the check catalogue. This strengthens the filing rather
than changing it: the misclassification is not merely mis-tiered, it is **unimplemented**, and
the two full-sweep declines are what an unimplemented `fix_now` class looks like from the field.

**Residual scope.** The filing's own preference order survives grounding intact and capture
enshrines it as the material, not as a ruling:

1. Give the check a **second legal response** — *add the missing entries to frontmatter* — and
   route by direction: prose ⊂ frontmatter is auto-fixable, frontmatter ⊂ prose is
   `flag_for_human`. Keeps the cheap half automatic. Costs an edit at `checks.md:16`, a Step-3
   entry in `fix-and-file.md` that does not exist today, and a report-slot decision.
2. Failing that, move the whole class to `flag_for_human` and drop the `fix_now:` slot.

**Open design question, carried verbatim, not resolved here:** the filing argues that
*"frontmatter is the source of truth"* needs a qualifier — *"it is authoritative about what the
page claims to rest on, not about what the page actually cites, and the check currently reads it
as the latter."* That is a claim about `write-verification.md`'s tier-1 item, not only about the
lint check, and its blast radius was not measured by the filing or by this grounding.

*The filing's `provenance_guess` — that the classification was set from the check's
**detectability** (one-file-checkable → tier 1 → amortizable into writes) rather than from its
**remediability** — is a diagnosis capture could not confirm or refute from source. It is
recorded as the filer's reasoning, unverified.*

### A14-5. `vlt-lint` mandates a strict-YAML report persist and ships no way to satisfy it (2026-08-26) — `factory/inbox/2026-08-26-123153-lint-mandates-strict-yaml-persist-with-no-yaml-library.md` (`origin: mggower/bmad-module-vlt#14`)

**CONFIRMED — both mandates, quoted exactly as the filing quotes them.**
`skills/vlt-lint/SKILL.md:74` requires the persist: *"write the Step-5 report block **verbatim** to
`{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` — plain YAML, the block's content without the fence."*
`skills/vlt-lint/references/report.md:3` requires the strictness: *"The fenced report block is
strict YAML as a whole … keep it parsing whole in both homes."* Neither site names a mechanism.

**PROVENANCE CORRECTION — the shipped design needs no serializer, and that relocates the gap.**
The filer inferred a missing YAML *emitter*. The report is not serialized from a data structure:
Step 5 (`report.md:5-7`) has the **agent** author the fenced block directly, and Step 6 persists
that block **verbatim**. So the shipped path never calls a YAML library, and the PEP 668 failure
the filer hit was in their own hand-rolled workaround, not in a shipped code path.

What is genuinely missing is the other half, and it is worse: **nothing validates the claim.**
"Keep it parsing whole in both homes" is a property asserted at `report.md:3` with no site that
checks it, and — as the filing correctly observes — on a PEP 668 machine the vault cannot even
check it by hand. The report is LLM-authored YAML containing free-text findings with em-dashes,
colons inside values, quoted strings and arrows: exactly the content where naive emission breaks
and "it looked fine" is not verification. **This is the cycle's through-line at the report seam** —
a stated rule with no enforcement point — and it is why the owner reclassified a `candidate` as a
blocker.

**GAP CONFIRMED — and a shipped constraint the filing could not have known.** `machine_tools` in
`skills/vlt-setup/assets/module.yaml` currently declares exactly one vault-side tool assumption:
`gh`, needed by `vlt-feedback`. The same block carries a writer clause: *"a module build that adds
a shipped tool assumption adds its row here in the same build."* So the filing's option 2 (ship an
emitter) and any validation step that assumes a YAML parser are **not free** — each adds a
machine-tool assumption and owes a `machine_tools` row in the same build, and `vlt-setup`'s
dependency probe reports but never gates, so a vault without it degrades rather than fails.

**Residual scope, re-ordered by grounding.** The filing's option 1 was written as "specify the
JSON-subset emission strategy." Grounding narrows and redirects it:

1. **A validation beat**, not an emitter — the gap is the unchecked claim. Whether it can be
   satisfied without a parser is genuinely open (JSON-subset emission is self-validating by
   construction only if something checks the construction).
2. **State the no-dependency requirement explicitly** in `report.md` and specify JSON-subset
   emission — every scalar a JSON string, lists as `- <json>`, nested maps by indentation. Pure
   documentation, zero `machine_tools` cost, and it makes every vault's output identical instead
   of independently invented. Available immediately.
3. **Allow `.json` as an alternative persist.** The report's consumers are machines; JSON is
   trivially emittable and trivially checkable everywhere, and the fenced in-session block can
   stay YAML for human reading. Note this touches the "both homes" rule at `report.md:3` directly.
4. Ship an emitter as a skill asset — **costs a `machine_tools` row**; ranked last for that reason,
   which is a reversal of the filing's own ordering.

### A14-6. Layer 3's entry condition requires "a recognized `type:`" and names no owning convention (2026-08-26) — `factory/inbox/2026-08-26-125529-recognized-type-names-no-owning-convention.md` (`origin: mggower/bmad-module-vlt#15`)

**CONFIRMED — the entry condition and the missing pointer.**
`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md:66` states Layer 3's boundary
as an entry condition requiring "an honest `author:`", "a `trust:` rung the writer is entitled to
set (**the trust ladder in `extraction.md`**)", "a recognized `type:`", and "the write-verification
attestation pair (**`write-verification.md`**)". Three legs carry an inline home. The `type:` leg
carries none. The filing's central claim is exact.

**CONFIRMED — the two conventions genuinely disagree, on a named value.**
`conventions/frontmatter.md:71`: *"The `type:` list is **non-exhaustive.** Canonical values include
`wiki`, `research`, `session`, `note`, `project`, `area`, `resource`, `idea`, and the PARA
container files `charter`, `record`, `register` … New artifact classes may introduce new `type:`
values without a contract edit."*
`skills/vlt-lint/references/checks.md:19`, `para_type_unknown`: the recognized set is *"the artifact
types `project|area|resource|moc`, the container types `charter|record|register`, and any
vault-declared schema in `{overlays}/extraction.overlay.md`."*
`research` is **canonical** under the first and **outside the recognized set** under the second. A
file carrying it is simultaneously well-formed and a loud finding. Confirmed as filed.

**CONFIRMED — the precedent, and it is stronger than the filing argues.** The by-name `{wiki}`
exclusion appears twice, and the canonical statement is in the **contract** itself
(`vault-operating-contract.md:65`, Layer 2): the `{wiki}` subtree *"is **removed from any PARA
population at selection time**, by name, never as an exception applied inside a check or a
resolver"* — with `checks.md:19` implementing it. The filing calls this "hard-coded to that one
case"; grounding confirms it and adds that the hard-coding is written into the contract as a
named singleton, not as a list with one member. A vault landing a second agent-lane subtree at a
browsable `{resources}` address has no general form of the move.

**Sharpened — the filing's option 4 is not a new ruling; it is already the shipped text.**
`checks.md:19` states `para_type_unknown`'s legal response as *"declare the vault-grown type as
overlay schema (declare-at-birth, `extraction.md`), retype to the shipped vocabulary, or relocate
the file out of PARA."* So "overlay-declare it, every time" is what the module already says. What
is missing is only that `contract:66`'s entry condition never points a reader at the convention
that says it. **The residual scope may therefore be a pointer, not a vocabulary decision** — a
materially cheaper cycle than the filing's four-option framing implies. Ideation should test that
reading first, because if it holds, options 1 and 3 are re-scoped from "widen the set" to "were we
right the first time."

**Sharpened — the sibling net has the same shape and no escape hatch at all.**
`para_author_unknown` (same line, `checks.md:19`) closes `author:` to `human|agent|hybrid` with no
overlay route. If ideation rules that closed sets need a general declaration mechanism, that net
is in the population and the filing does not mention it.

**Cites `ST-2`** (`factory/studies/ST-2-location-as-proxy-for-trust.md`). Its RC1 is the cause this
filing sits downstream of, and the filing's own account of *why this bites now* is RC1's
repair-residue: 0.16.0 replaced the location test with an attestation-based entry condition, and
under the retired location rule an agent-lane `type:` could never reach the PARA population
because agent-lane *files* never did. Capture states only what is new — the `type:` leg is the one
of four that did not move with the boundary — and does not re-derive ST-2's diagnosis. Append this
capture to ST-2's `cited_by:`.

**Live blocking instance.** `{field-vault}` holds a live `kind: parked-interim` against this
filing rather than resolving it locally by overlay, on the stated grounds that a local overlay
would be a vault answering a module-level question. Cycle 13's discharge run confirms it
reproduced exactly in the 0.16.1 sweep — 5 `type: research` briefs, matching the parked entry to
the file — and that v0.16.1 moved nothing here.

**Open design questions, carried verbatim, not resolved here.** The filing states four usable
rulings (frontmatter's list governs and the closed set narrows to a status-enum concern; the
closed set is authoritative and frontmatter's non-exhaustiveness is scoped to the agent lane; a
general carve-out mechanism generalizing the by-name exclusion to a declared list; or ruled
working-as-designed). It explicitly declines to choose: *"This is an ask for a ruling, not a
proposed answer. Any of these is usable; the current silence is not."*

### A14-7. Layer 3's open entry condition meets `write-verification.md`'s closed `verified_by` roster (2026-08-26) — `factory/inbox/2026-08-26-141418-layer-3-open-entry-vs-closed-verified-by-roster.md` (`origin: mggower/bmad-module-vlt#16`)

**CONFIRMED — every cited site, at the exact line the filing guessed.** This filing's
`provenance_guess` was checked against working-tree source and holds on all four:

- `vault-operating-contract.md:66` — Layer 3's entry condition, and the openness clause: the two
  shipped dispositions *"are the shipped set, **not** a closed one: another verb filing an honest,
  attested document under the condition above is legal."*
- `conventions/write-verification.md:47` — the closure: *"the `verified_by` value set is this
  file's `consumers:` **that are write ops**, plus write-op `local_consumers:` registrants … The
  roster is **membership and ceiling**, never an automatic grant."* `consumers:` at `:12` is
  `[vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js]`.
- `conventions/write-verification.md:53-54` — §Scope rule (self-marker), which puts the resulting
  files in jurisdiction: lint flags *"files carrying vault frontmatter (`type:
  wiki|research|project|area|resource` with `author: agent|hybrid`) and no attestation"*, exempting
  only `daily/`, raw `sources/` deposits, and human-authored PARA files.
- `conventions/extraction.md:188` — the container-file carve-out, *"operational records, not
  knowledge artifacts … they carry **no** pair"* — restated canonically at
  `vault-operating-contract.md:70`. The precedent the filing names is real: the module has already
  ruled one class of Layer 3 file **out of attestation jurisdiction** rather than inventing a value
  for it.

**CONFIRMED — the contradiction is live and the failure direction is the dishonest one.** The
contract declares the writer set open; `:47` closes the attester set to write ops. A partner
authoring a Layer 3 document during an ordinary sitting satisfies honest `author:`, an entitled
`trust:` rung and a recognized `type:` (subject to A14-6), then reaches §Attestation and finds no
value it may honestly hold — every roster member names an op that did not write the file. The
§Scope rule then places the file in jurisdiction and flags it, with no route to clear the flag.
The filing's observation that the cheaper of the two available responses is the dishonest one
(fake a provenance claim, or leave the finding permanently open) is a correct reading of the
shipped text.

**Sharpened — a third route exists in the source that the filing's two options miss, and it
narrows the gap without closing it.** `:47` admits *"write-op `local_consumers:` registrants"*, and
`local_consumers:` is a **vault-written** declared field (`frontmatter.md:294`, `:296`). So a
vault-minted partner **can** already hold a legal `verified_by` value — by registering as a
write-op local consumer. That route does not rescue the filing's population, for two reasons worth
stating precisely because they change what a fix must do:

1. the write-op qualifier binds the whole set (`:47` says so explicitly), and a partner writing in
   a facilitated sitting is not an op — registering one would be a false declaration, not a fix; and
2. nothing in the bundle tells a partner the route exists or when it applies.

So the honest statement is not "no route exists" but **"the only route requires the writer to be
something it is not, and is undiscoverable besides."**

**GAP CONFIRMED — the field measurement, and what it does and does not establish.** The filing
measured, before filing: 27 Layer 3 files outside the wiki subtree carrying `author: agent|hybrid`
with no pair, across six partners' domains; 5 carrying the pair, **all five written by an operation
skill**; zero partner-sitting-written Layer 3 documents attested, and none able to be. The
population spans the module's own shipped partner roster and vault-minted partners alike, over
~10 weeks of sanctioned work — so it is not one careless partner. Cycle 13's discharge run
independently confirms the 27 reproduced in the 0.16.1 sweep. Capture notes the limit: the counts
are `{field-vault}`-local and establish that the class is large and ordinary there; they do not
establish a rate for vaults generally, and the filing does not claim they do.

**Residual scope.** Both filing directions survive grounding; the precedent asymmetry is the
material fact for ideation:

1. **Widen the value set** — admit a partner identifier, or a sentinel meaning "verified in-sitting
   by the authoring partner." Keeps every Layer 3 artifact attested; weakens the field's current
   meaning (an op name, checkable against a roster) and owes a story for what the new value is
   checked against. Note this interacts with `local_consumers:` above rather than replacing it.
2. **Narrow the jurisdiction** — exempt partner-sitting writes in §Scope rule the way container
   files already are. **Has shipped precedent** (`extraction.md:188`), is honest about what the pair
   records today (that a *write op* ran its checklist), and is the cheaper edit. Cost: a real class
   of Layer 3 artifact stops being covered by any structural check.

Either direction changes a **rule** in `write-verification.md` and therefore bumps `version:` from
`3` and re-acks all five consumers in the same build (the version-handshake rule; the file is
currently unbumped at `3` with 5 consumers). A jurisdiction narrowing that only edits §Scope rule
is still a rule change, not a prose clarification. Ideation should price this in — Cycle 13 shipped
with no convention bump and no re-ack owed, and this cycle will not.

**Open design question, carried verbatim, not resolved here.** The filing flags its own
classification: *"Filed as a `defect` rather than a `pattern` because this instance blocks a
concrete write today; the maintainer may prefer to reclassify."*

**⚠ Cross-filing — a second instance of one shape, and a study candidate.** The filing names the
link itself: *"this may be the same shape as the open filing about the decision log's Writers
roster having no route for a shipped write op that legitimately discovers a deviation mid-run.
Both are **a closed roster meeting an actor the surrounding rules authorize.**"* That filing is
`factory/inbox/2026-08-21-150214-decision-log-writer-roster-admits-no-discovery-site.md`
(`origin: mggower/bmad-module-vlt#6`), captured into Cycle 10. Grounding confirms both are live
and the shape is the same. A14-6 is arguably a third instance in the vocabulary register rather
than the writer register.

**⚠ SUPERSEDED 2026-08-26 by D4 — `ST-6` IS OPEN and holds this cause.** *(roundtable A36,
2026-08-26; Dr. Quinn)*. Read
`factory/studies/ST-6-closed-rosters-meet-authorized-actors.md` — registered in
`factory/studies/README.md`, opened this session, written from the pre-repair state — **not this
paragraph's candidate framing.** The paragraph below is kept for provenance only, and it matters
because **E5 orders build-3's brief to write A14-6/A14-7 from this very section.**

**No study in `factory/studies/` holds this cause.** `ST-1`'s primary cause is adjacent —
*permission fused to provenance in one verb* — but it is about one verb's shape, not about closed
rosters meeting authorized actors, and reading A14-7 as ST-1 would flatten the distinction. Per
`factory/studies/README.md` *(Opening a study / Citable, never blocking)* this is recorded as a
**study candidate**: the cause is bigger than any of the three filings, and whether `ST-6` is
opened is the author's call and gates nothing. Naming it here so the third instance does not
re-derive it from scratch.

### A14-8. The findings cache cannot round-trip — the writer and the reader disagree, and no instrument can see it (2026-08-26) — `factory/inbox/2026-08-26-141838-findings-cache-cannot-round-trip-writer-and-reader-disagree.md`

*Captured the same day the cycle opened, from a `{field-vault}` session run deliberately as Cycle
12 b2(5)'s acceptance test. It joins the opening Capture rather than a mid-cycle addendum: this
cycle's batch has not been ideation-ruled or roundtable-stamped, so the addendum posture does not
apply. **It refutes b2(5), which was graded FAILED in Cycle 12's ledger the same day** — the
authoritative record is `factory/cycles/12-proxy-claims/roadmap.md` §Owner ruling — the six bounded
tails at their bound.*

**CONFIRMED — Defect 1, the sidecar schema mismatch, and the root cause is the spec.**
The reader requires `{slug, key, scan}`: `vlt-lint-full.js:243` filters
`cachedScans.filter((c) => c && c.slug && c.key && c.scan)` and `:344` dereferences
`cacheBySlug.get(p.slug).scan`. The spec tells the SKILL to write something else —
`skills/vlt-lint/references/full-scale.md` step 5, findings-cache sub-bullet: *"one record per page
adjudicated this run — the workflow's returned `fresh_scans`."* But `fresh_scans` is the array of
**raw PAGE_SCAN returns** (`:293` pushes the agent's `r` unmodified; `:723` returns it as-is), which
carry no `key` and are not wrapped. **Following the spec literally produces a sidecar the reader
discards whole.** On disk: `_agent/lint-cache.yaml` holds 146 flat records and
`grep -c "^    key:"` returns **0**.

The key is derivable — `:722` returns `cache_fingerprint` as exactly
`${scanFingerprint}|${rulesetFingerprint}`, and `:242`'s `runKey` is
`${pageHashes[slug]}|${scanFingerprint}|${rulesetFingerprint}`, so the correct record is
`{slug, key: "${pageHashes[slug]}|${cache_fingerprint}", scan: <entry>}`. **That derivation is
nowhere in the spec** and must be reverse-engineered from workflow source by every implementer.

**Sharpened — the written sidecar is lossy, not merely mis-nested.** It stores `fingerprint:` once
at the top level (`_agent/lint-cache.yaml:1`) and **no per-page digest anywhere**, so it cannot
express the reader's key even in principle. A reader-side fix alone cannot rescue an existing
sidecar; the file has to be rewritten. Worth knowing before anyone proposes tolerating the flat
shape.

**CONFIRMED — Defect 2, `rulesetFingerprint` has no deterministic algorithm.** `full-scale.md`
step 2 enumerates the inputs in order — `module_version`; the skill's `depends_on:` pin vector
verbatim; each judged convention's digest **as merged with its overlay**; the digest of
`references/checks.md` — and specifies **no digest construction**: no separator, no hash algorithm,
no encoding, no truncation, no canonical member list. Two runs over an identical ruleset therefore
compute different values; the field observed `980d749d9acf418e` against an independent
`66d27a0e6cd8fabe` over a provably unchanged ruleset. Since `reusable()` (`:244-245`) requires
`rulesetFingerprint` non-empty **and** an exact key match, **the cache is structurally incapable of
hitting across sessions — the only case it exists for.**

**GAP CONFIRMED — the failure is invisible to every shipped instrument, and that is the durable
finding.** The version-skew defence (`full-scale.md` step 4) refuses only when `files_checked`
**and** `files_cached` are **both** `0`. A run that cold-scans everything *because the cache is
broken* reports `files_checked: 146` — full coverage, honest report, no refusal — and is
indistinguishable from a healthy cold run. **Nothing checks that a cache written by run N is
readable by run N+1.** Every instrument reports the cache's *counts*, never its *round-trip*.

**This is the cycle's through-line, and A14-8 is its cleanest instance.** A contract stated in one
place (the reader's filter, in code) and restated as prose in another (the spec's write
instruction), with **no enforcement point where the two meet**. The seam is a file on disk that
nothing validates. Defect 2 is the same shape at one remove: an algorithm *described* for each
caller to re-derive rather than single-homed as executable steps — the `ST-3` cause (governance has
no machine-addressable projection) reappearing as a fingerprint with no machine-addressable
definition.

**Cites `ST-5`, and sharpens it with the cleanest specimen the register has.** Build-2's
ship-verifiable checks (1)–(3) proved the cache on a two-run temp fixture **inside one harness
invocation, where the SKILL-side write step never ran because the harness stubbed it**. The one
seam that breaks in the field is precisely the one the at-rest instrument could not exercise —
ST-5's second cause, exactly. And the compounding half: **the field check that would have caught it
was b2(5), tagged field-contingent and therefore non-gating** — ST-5's third cause (*one tag
resolves a check's blocking power from its grading modality*). Cycle 12 shipped a mechanism that
has never once worked, on a green ship-verifiable ledger. Append this capture to ST-5's `cited_by:`.

**Residual scope.** Five directions, the field's own, re-ordered by grounding:

1. **Move the wrapping into the workflow** — return write-ready `{slug, key, scan}` records instead
   of raw `fresh_scans`, so read and write shapes cannot drift apart again. Preferred over
   documenting the derivation: it removes the seam rather than describing it.
2. **Move `rulesetFingerprint`'s computation into the workflow**, or single-home it as executable
   steps (canonical member order, separator, digest, truncation). Same argument.
3. **A round-trip acceptance check** — write the sidecar, read it back, assert every record is
   reusable against an unchanged corpus. This is what the cancelled sweep manually stood in for,
   and its absence is what made both defects invisible. **Ship-verifiable at rest**, so it can gate.
4. Amend `full-scale.md` step 5 to state the record shape and key derivation explicitly — the
   fallback if 1 is not taken.
5. **Widen the step-4 refusal predicate** (or add a distinct signal) so "cold because the cache was
   unreadable" is distinguishable from "cold because the ruleset legitimately moved."

**Note for ideation — this one is cheap and it is not on the #13 joint.** Unlike A14-1..A14-3 and
Cycle 13 carry 1, nothing here needs the reduce to read page bytes. `pageHashes` already crosses the
seam (`:47-49`), the workflow already returns `cache_fingerprint`, and every fix is a shape or a
single-homing. It is the one entry in this cycle that can be taken without ruling question 2 first.

⚠ **SUPERSEDED IN PART — grounding correction at brief time (2026-08-27, `build-brief`)**, recorded
per `grounding-at-brief-time.md`'s two-place rule. Every `file:line` in this capture was derived
against **v0.16.1**; build-1 shipped as **v0.16.2** and took `vlt-lint-full.js` from 724 to **767
lines**. Re-derived against the working tree at `bd985a6`: reader filter **`:245`** (was `:243`);
`runKey` **`:244`** (was `:242`); `reusable` **`:246-247`** (was `:244-245`); `.scan` deref
**`:346`** (was `:344`); `reused` **`:249`** (was `:248`); `freshScans.push(r)` **`:295`** (was
`:293`); `cache_fingerprint` **`:765`** (was `:722`); `fresh_scans` **`:766`** (was `:723`); the
READ-ONLY comment **`:762-766`** (was `:719-723`); `scanFingerprint` **`:234-235`** (was `:232-233`);
"no filesystem access" **`:26-28`** (was `:36-38`). `pageHashes`' arg doc at `:47-49` **HOLDS**.
**Scope is unchanged by every one of these; only the numbers moved.**
**One substantive correction, beyond line drift:** the capture and build-1's brief both describe the
sidecar's payload as the scanner's **verbatim** `PAGE_SCAN` return. It is not — **`:356` mutates the
scan objects in place** (`s.outbound_links = (…).map(normalizeTarget)`) and `freshScans` holds those
same references, so what is returned for the sidecar carries **normalized** link targets, today as
well as after build-2. It is harmless because `normalizeTarget` (`:81-87`) is idempotent — and
build-2's brief makes that an **asserted** property (its run-2 ≡ run-3 identity check) rather than an
assumed one. Brief:
`factory/cycles/14-no-enforcement-point/briefs/build-2-findings-cache.md`.

## Carried forward from Cycle 13 — live, grounded, un-built

Recorded in `factory/cycles/13-trusted-returns/roadmap.md` §Carried forward (ruled OUT of the
patch, not dropped) and orphaned by the v0.16.1 release under the ship-day capture boundary,
exactly as that section's ⚠ routing question predicted. They open here. **All three are defect or
posture work; none is net-new capability, so all three are admitted under §Owner ruling.**

1. **Finding 4 — the paraphrased verbatim field.** `vlt-lint-full.js:162` asks for the frontmatter
   `summary:` value *verbatim*; the agent returns a paraphrase and `:545` measures it faithfully,
   so the reported character count is wrong (`kettl` 168 vs an actual 156; `l-theanine` 162 vs
   159). **The blast radius is wider than `summary`** — every schema field marked verbatim is
   unguarded by the same argument, which A14-3 has now demonstrated on a second field with a
   different mechanism. Fixing it needs the real frontmatter value, which the workflow cannot read
   (`:36-38`), so it costs a SKILL-side per-page arg on the `pageHashes` precedent (`:47-49`) —
   **the #13 joint** (§Owner ruling).
2. **The general posture (Cycle 13 Q3's "true fix").** *Every agent-returned value that is
   mechanically checkable at the reduce is checked there.* The durable answer to A14-1, A14-2,
   A14-3 and carry 1 at once; larger than a patch. Cycle 13's discharge run recorded that **the
   evidence for taking it is materially stronger than it was on 2026-08-26 morning** — three of
   that sweep's four false findings came from the reduce trusting scanner-returned text.
3. **Retiring `malformed_frontmatter` itself** — named and deferred by Cycle 13 build-1's
   brief-time disposition 6, per P-15 (a retirement is named, never silently survived). Once the
   guard works, the class's genuine population is "schema breaks that are not attestation and not
   invented," which may be fully covered by the documented `frontmatter_drift`
   (`vlt-lint-full.js:573-575`). Not taken in build-1 because retiring a shipped finding class is a
   behavioral removal needing a **measured** population first — and Cycle 13's check (2) was to be
   that measurement. **It FAILED, so the measurement does not exist**: whatever build takes this
   must produce it, and the successor named by Cycle 13 is the build that takes carry 2.

## Cycle 12's six bounded tails — the bound landed on this run, and was ruled

Cycle 12 shipped v0.16.0 and its acceptance left six field-contingent checks open, each bounded to
**"Cycle 13's `inbox-capture`"**. Cycle 13's capture was a narrow patch capture that explicitly did
not trigger the attachment (Cycle 13 §Owner ruling — narrow-capture carve-out), and Cycle 13 is now
closed to capture without ever having run a full batch. **This run is that batch, so the bound
landed here.**

**The tails were ruled in the same session, against evidence re-gathered from `{field-vault}` at
the bound rather than from the ledger's last-known state.** The authoritative record — grades,
reasoning, and the superseded ledger notes — is single-homed at
`factory/cycles/12-proxy-claims/roadmap.md` §Owner ruling — the six bounded tails at their bound
(2026-08-26). It is **not** restated here. Outcome only:

| tail | the check, in one line | outcome at the bound |
|---|---|---|
| b2(5) | the `churn`-ratio saving is real at live churn | **FAILED** — the corrected bound was tested the same day and refuted; filed and captured as **A14-8** |
| b3(6) | `trust: raw` representable-and-present in PARA (`ST-2`'s own test) | **DISCHARGED on substance** (owner ruling) — the ledger's evidence note was stale |
| b3(7) | a partner resolves a `{resources}`-write legality question without escalating | **STILL OPEN** — needs owner observation; no disk evidence either way |
| b3(9) | a vault declares `writers:` on a container it had framed in prose | **CLOSED by owner ruling** — A33's notification sufficient, no re-carry |
| b4(5) | a real park recorded through the new `vlt-feedback` step | **DISCHARGED** — two parks, both against rail-filed blockers |
| b4(6) | the next `vlt-upgrade` renders a non-empty `parked_interims_review:` | **DISCHARGED** — first live non-empty render |

**Five of the six do not enter Cycle 14 as build scope** — none of those five is a defect, and
§Owner ruling admits only defects and blockers. **b2(5) is the exception: it FAILED**, and the
defects behind it enter as **A14-8**. Cycle 12's field-contingent ledger stands at **7 of 11
discharged, 1 FAILED**, and holds no no-re-carry item.

**Three things this cycle inherits from the ruling, none of them build scope:**

1. **A14-6's filing is stale against its own vault, and its capture should be read knowing that.**
   Tracker #15 describes moving the `vlt-brief` shelf to a `{resources}` address as prospective;
   the shelf has been at `resources/briefs/` since before the 2026-08-26 10:46 lint, which
   enumerates all five issues by path in `para_type_unknown`. The defect A14-6 reports is
   unaffected — the two conventions still disagree — but the framing *"moving the shelf today
   would put files into the PARA population"* is past tense, and the files are already there under
   a recorded park.
2. **b3(7) interacts with A14-6 and A14-7.** Both are live parks against the same bundle, so a
   partner attempting a `{resources}` write today may legitimately escalate — which would not be a
   failure of the rewritten bundle but of the two vocabularies it is waiting on. b3(7) is
   effectively ungradeable until those two rule.
3. **The b3(9) population problem is `ST-5` material.** A field-contingent check whose discharging
   population was a *single vault artifact* was not gradeable in the field on the day it was
   written. Named in the Cycle 12 ruling; carried here so the instrument work has the third
   instance.

## Also carried, not a filing

**`{field-vault}` overlay staleness, surfaced by the 0.16.1 upgrade** (Cycle 13 §Next lifecycle
move, item 4). `vault-operating-contract.overlay.md` §D's parenthetical names Layer-3 territory as
*"`{projects}` and `{areas}`"*; `{resources}` has been Layer 3 since 0.15.0. Report-only and
correctly not fixed by the upgrade — an overlay is vault-owned and append-only. **This is a
vault-side owner action, not module work**, and it is recorded here only so it is not lost.

**Owner action outstanding from Cycle 13** (unchanged, restated so it does not fall through): the
`{field-vault}` session had not run `vlt-feedback` for the 2026-08-26 sweep at the time Cycle 13's
roadmap was written. This run's intake shows #12–#16 did arrive on the rail and are now
materialized, so that action is at least partly discharged; A14-1..A14-3 remain factory-filed and
deliberately carry no `origin:` header — **do not re-file them upstream** (a rail copy would
materialize a second time; the `origin:` header is the only idempotency key).

## Open design questions — the batch's, not resolved by capture

Carried here so ideation sees them together rather than one filing at a time.

1. **Instances or posture?** A14-1, A14-2, A14-3 and Cycle 13 carry 1 are four faces of one seam.
   Repairing them individually reopens Cycle 13's gate soonest; taking Cycle 13 carry 2's general
   posture answers all four and the next one. The owner ruled at capture that this is
   **ideation-steered with the full cost in view**, not pre-ruled here.
2. **Does the posture re-admit #13?** Every mechanical-verification direction in this cycle needs
   ground truth the workflow structurally cannot fetch (`vlt-lint-full.js:36-38`), which means a
   SKILL-side per-page arg, which moves the joint against #13's ~84KB payload cost. If the posture
   is taken, #13 is a dependency, not net-new — and re-admitting it is an owner ruling.
3. **A14-6: pointer or vocabulary?** If `contract:66`'s missing pointer is the whole defect, the
   cycle is a one-line edit plus a handshake. If the two conventions must be reconciled, it is a
   vocabulary decision with `para_author_unknown` in the population too.
4. **A14-7: widen or narrow?** Narrowing has shipped precedent (`extraction.md:188`) and is
   cheaper; widening keeps structural coverage. Either bumps `write-verification.md` from
   `version: 3` and re-acks five consumers in the same build.
5. **Is "a closed roster meeting an authorized actor" a pattern worth naming once?** Three live
   instances (A14-7, the Cycle-10 decision-log Writers roster filing, and arguably A14-6). No study
   holds the cause; opening `ST-6` gates nothing and is the author's call.
6. **A14-4's qualifier.** Whether *"frontmatter is the source of truth"* needs re-scoping is a
   claim about `write-verification.md`'s tier-1 item, not only about a lint slot. Blast radius
   unmeasured.

## Ideation rulings — A14-1..A14-8 (owner-steered, 2026-08-26)

**Rulings below are the owner's; briefs cite this section, never re-litigate.** Session
**COMPLETE — filled 2026-08-26 over four owner-steered rounds. Every slot is ruled.**
`build-brief` gates on this section being filled — it is.

**What each round settled.**

- **Round 1 — the cycle's size.** The reduce-side posture is taken **where it needs no new
  inputs**: A14-1's claim return is **restructured** and A14-3's seam **entity-decoded**, while
  A14-2 and the `summary` paraphrase — the only two faces needing real page bytes — are deferred.
  Tracker **#13 stays deferred** as a consequence. And **an at-rest instrument now means the check
  GATES** (D3) — the cycle-level answer to what let b2(5) ship a mechanism that never worked.
- **Round 2 — the governance pair.** A14-6 is a **pointer**, not a vocabulary fight: the closed set
  governs the PARA population and `contract:66` names it, at zero handshake cost. A14-7 narrows
  jurisdiction **by artifact class**, extending `extraction.md:188`'s shipped principle rather than
  adding a writer-shaped axis.
- **Round 3 — the costs.** **Two conventions move in one build**, by *elimination* not precedence
  (15 re-acks). A14-8 **removes both seams** rather than documenting them, with an in-session
  correction to what "move the fingerprint into the workflow" can actually mean. The
  `malformed_frontmatter` retirement **defers a third time — but ships its measurement**.
- **Round 4 — the shape.** `.json` becomes a legal persist because **`json` is stdlib and `yaml` is
  not**, which is what makes A14-5's claim checkable at all. **Four builds, two releases**, build-1
  cut alone so Cycle 13's gate reopens without waiting on a 15-re-ack handshake. **`ST-6` opens
  now**, written from the pre-repair state.

Seeded from the Cycle 14 capture run (2026-08-26, 8 filings). Question numbering is the clerk's,
for in-session reference only; it implies no ordering or priority.

**Two constraints the capture established that ideation inherits rather than decides:**

- **A14-1 gates Cycle 13's closeout.** Cycle 13 shipped v0.16.1 and FAILED acceptance check (2)
  by owner ruling on live field evidence; it is closed to capture and has no discharge path left.
  Only a shipped repair moves it. Whatever build takes A14-1 is the one that reopens Cycle 13.
- **A14-7 — and A14-6 under a widening reading — forces a convention `version:` bump and a
  same-build re-ack of every consumer.** `write-verification.md` is at `version: 3` with 5
  consumers. Cycle 13 shipped with no bump owed; this cycle will not. See D2.

### Grouping & order

**Ruled Round 4 (2026-08-26): four builds, two releases. Order 1 → (2, 3, 4).**

**Release plan.** **Release 1 = build-1 alone.** It is the only thing that reopens Cycle 13's
closeout gate, and cutting it alone keeps that repair off the critical path of build-3's
15-re-ack handshake. **Release 2 = builds 2, 3, 4** together.

*Cycle-wide, ruled: **every check every brief writes obeys D3** — **as amended at the roundtable
(A17): a BOUNDED check (at rest, at the release gate, or on the next ordinary upgrade) is
ship-verifiable and it GATES; an at-rest instrument is one sufficient bound, not the criterion.**
Every brief additionally states, per ship-verifiable check, **which seam its named instrument
actually crosses** (R1). And **the first full lint after either release is COLD by construction**
(build-1 moves `scanFingerprint`, build-2 rewrites the record shape, build-3 moves two convention
digests, build-4 moves `checks.md`'s) — briefs state it up front so it is never discovered as a
regression. ⚠ **The two-release plan therefore costs TWO cold full sweeps, not one** (roundtable
A26) — accepted knowingly as the price of reopening Cycle 13's gate early; see §Next lifecycle move
for where `{field-vault}` should pay its owed sweep.*

- **build-1 — reduce-side: A14-1 (the guard) + A14-3 (the encoding).** ⚠ **Gates Cycle 13's
  closeout.** Replaces the free-text claim with a structured `PAGE_SCAN` return (retiring the
  residue rule at `:593-603` and both predicates' `residue === ''` conjunction), and entity-decodes
  the category seam on **both** sides (`s.category` and `h2set` at `:643`). Carries the
  `malformed_frontmatter` **population measurement** per Q8.
  - `binds:` Q1, Q7, Q8, **E4**, D1, D3, D5 *(roundtable A20 — E4 is the cycle's only
    build-discharged debt and was the only E absent from a `binds:` list)*
  - `spike:` none

  **⚠ `attestationOnlyComplaint()` has TWO call sites, not one** *(roundtable A2, 2026-08-26 —
  verified in session; `:664` appears nowhere in the capture or the rulings)*. `:701`
  (`malformed_frontmatter`, via `refusedFrontmatterClaim` at `:630`) is the one Q1 structures.
  **`:664` filters `unmarked_supersession` — an array of free-text strings Q1 does NOT structure**,
  and the comment at `:659-663` records why the guard is there: *"A13-1 Finding 1's sixth entry (an
  attestation complaint) arrived here after the same prompt-side prohibition was ignored."*
  As ruled, build-1 either leaves the whole `parseClaim`/`CLAIM_FILLER` machinery standing for
  `:664` — so Q7's "the comment goes with the guard" is **false** and the residue rule is not
  retired — **or deletes it and silently regresses A13-1 Finding 1. Neither is a decision anyone has
  made. The brief must rule `:664` explicitly**: structure `unmarked_supersession` too, keep the
  parser scoped to `:664` alone, or retire the guard with its reason on record. **Q7's retirement of
  `:559-561` is conditional on that ruling.**

  **Retirement list, completed and named (P-15)** *(roundtable A37, 2026-08-26)*. Retires with the
  residue rule: `parseClaim` (`:593-603`), `fieldsNamed` (`:605`), `KNOWN_FRONTMATTER_BY_LENGTH`
  and its `:579` comment (`:580`), `normalizeClaim` (`:584`), `claimWords` (`:585`), `CLAIM_FILLER`
  (`:589`), and **the `frontmatter_issue` free-text schema slot itself (`:163`)** — each exists only
  to parse prose the structured return no longer sends. **`PAGE_REQUIRED_FRONTMATTER` and
  `PAGE_OPTIONAL_FRONTMATTER` SURVIVE** — they carry a live second role at `:563-568`, and the
  opposite error (deleting them by association) was equally available from the old text. A
  ship-verifiable check greps that none of the retired symbols survives.

  ⚠ **SUPERSEDED IN PART — grounding correction at brief time (2026-08-26, `build-brief`)**, recorded
  per `grounding-at-brief-time.md`'s two-place rule. Re-derived against working-tree source at
  v0.16.1 (`c18c591`), the file being `skills/vlt-setup/assets/workflows/vlt-lint-full.js`, 724 lines:
  - **`CLAIM_FILLER` is at `:591`, not `:589`** — `:586-590` is the residue-rule comment. (A29
    corrected four cites in this region and this one survived the pass.)
  - **`parseClaim` is at `:594-604`, not `:593-603`** — `:592-593` is its comment. (Q1 ruling 1
    already carried `:594-604`; §Grouping's list carried `:593-603`. The former is right.)
  - **`KNOWN_FRONTMATTER_BY_LENGTH`'s comment spans `:578-579`**, not `:579` alone.
  - **`PAGE_REQUIRED_FRONTMATTER` / `PAGE_OPTIONAL_FRONTMATTER` have NO live *code* role today** —
    `:563-568` is a **comment block**, and every code reference to the two sets is inside the
    machinery A37 retires (`:577`, `:614-615`, `:625-626`). Their survival is therefore something
    build-1 must **make true**, not merely preserve: the brief rules that the rewritten dispositions
    classify `frontmatter_defect_fields` against these sets directly (set containment replacing
    `fieldsNamed`). **Grounding addition:** `KNOWN_FRONTMATTER` (`:577`) is dead once `:580` goes and
    joins the retirement list as an eighth symbol; `ATTESTATION_FRONTMATTER` (`:576`) survives.
  - **`:664` RULED** (A2's third option): the guard is **retired**, because once the predicate takes
    a structured record it cannot be applied to a free-text string at all. Structuring
    `unmarked_supersession` is refused on **measured** grounds — `PAGE_SCAN` closes at **3688 of
    3700** after the ruled repair — and would flip the deferred `:168` dissent into a ruling, which
    is ideation's act. `:559-561`'s retirement (Q7) is therefore unconditional. Compensations on
    record: `:168` KEPT (A-R1), an R1 interim posture, and a gating acceptance check that **measures**
    the A13-1 Finding 1 exposure and decides §Carried forward item 9.
  - **Schema budget re-measured with package-lint's own `_E6_NODE_EXTRACTOR`**: baseline **3598**
    (A1 confirmed); the brief's ruled shape lands at **3688 ≤ 3700**, paid for by retiring
    `frontmatter_valid` (`:159`) **whole** as well as `frontmatter_issue` (`:163`).
  - **Scope is otherwise unchanged.** Brief:
    `factory/cycles/14-no-enforcement-point/briefs/build-1-structured-claim-return.md`.

  **⚠ RETIRES `:159`; KEEPS `:168` — owner ruling, roundtable 2026-08-26** *(roundtable A-R1)*.
  `:159`'s prohibition (208 chars) becomes **unexpressible by construction** once the disposition is
  an enum — the enum's range excludes the route rather than forbidding it in prose — and **its 208
  characters are load-bearing against the E6 ceiling (A1)**. **`:168` is KEPT and becomes
  load-bearing again**: Q1 leaves `unmarked_supersession` free-text and build-1 removes its
  reduce-side guard at `:664`, so `:168` is **not defence in depth — it is the only depth.**
  **DISSENT ON RECORD (Victor, Amelia):** `vlt-lint-full.js:551-557` states that Cycle 12 build-1
  shipped exactly that prohibition and *"the very next two full sweeps reported the defect
  unchanged"*, and D1 rules in this same cycle that a schema description is never an enforcement
  point — so keeping one as an enforcement layer is a contradiction the cycle ships against itself.
  **The dissent is deferred, not resolved: `:168` survives only as long as `:664` does, and the
  moment `unmarked_supersession` is structured the dissent becomes the ruling.**

  **⚠ Also carries the check that re-grades CYCLE 13's acceptance check (2)** *(roundtable A21,
  2026-08-26)*. The sole justification for cutting build-1 alone is that it reopens Cycle 13's gate
  — **and no ruling asked for a check that actually re-grades it.** Cycle 13's (2) was refuted **at
  rest** on shipped source, so its re-grade is at-rest, bounded, ship-verifiable and **GATES**.
  Without it, **release 1 could ship and Cycle 13 still not close.**

  **Touches** `vlt-lint-full.js` **and `skills/vlt-lint/references/checks.md`** *(roundtable A38,
  2026-08-26)* — `checks.md:15` carries **the same refuted over-reporting safety claim** in the
  vault-facing catalogue and additionally documents the conjunction/residue mechanism build-1
  removes. Q7 retires the claim at `:559-561` and would leave the shipped, vault-read copy asserting
  it. No new cost: `checks.md`'s digest already moves the ruleset fingerprint and build-1 is cold by
  construction.

- **build-2 — the findings cache: A14-8.** Workflow returns write-ready `{slug, key, scan}` records
  **for every page adjudicated this run — fresh AND reused** *(roundtable A6)*; fingerprint
  **composition** moves into the workflow (components still computed SKILL-side — see Q6's
  in-session correction); the round-trip check ships and **gates**. Touches `vlt-lint-full.js` and
  `full-scale.md` (**`full-scale.md` is shared with build-4 — one brief owns the file, the other
  cites it**, roundtable A8).
  - `binds:` **Q1**, Q6, D3 *(roundtable A4 — Q1 was missing and it defines the object build-2 caches)*
  - `spike:` none

  **⚠ NOT "independent of build-1 in substance" — it DEPENDS on it** *(roundtable A4, 2026-08-26)*.
  The `scan` payload build-2 wraps **is** build-1's structured `PAGE_SCAN` return, and
  `scanFingerprint` (`:232-233`, derived from `pageScanPrompt(...) + JSON.stringify(PAGE_SCAN)`) is
  a **key component** build-1 moves. A brief working build-2 from `Q6, D3` alone would build its
  fixture against the **pre-build-1 schema** and ship a gating check proving the wrong shape
  round-trips. **Interface, stated rather than assumed:** build-1's `PAGE_SCAN` change invalidates
  every release-1-era sidecar record, and **build-2's composition move MUST keep `scanFingerprint`
  a term of the composed key** — the SKILL supplies only the ruleset-side components. Nothing in the
  record said so, and the brief-time question ("list or pre-joined string") makes dropping it
  available. A ship-verifiable check asserts a record keyed under a different `PAGE_SCAN` is **not**
  reusable.

  **⚠ Q6.1 as ruled fixes only HALF the sidecar** *(roundtable A6, 2026-08-26)*. `:723` returns
  fresh records only; `:248`'s `reused` surfaces solely as the count `files_cached`; and
  `full-scale.md` step 5 tells the SKILL to write back *"the reused records that are still valid"* —
  where validity is `key === runKey(slug)` and `runKey` embeds `scanFingerprint`, **a
  workflow-internal value the SKILL structurally cannot compute** (`:36-38`). So *"the read shape
  and the written shape cannot drift apart again"* is true of **a warm run's fresh records only**.
  The workflow must return records for every adjudicated page so the SKILL never re-derives
  reusability it cannot compute.

  **⚠ The round-trip fixture must be THREE runs and its writer must be executable** *(roundtable
  A5, 2026-08-26)*. Two independent faults. (a) A two-run fixture (cold → warm) **cannot observe
  reused-half loss**: if run 2 drops the reused records the sidecar empties and the check still
  passes — a **third** run is what fails. The fixture is **cold → warm → warm**, asserting record
  count and per-record reusability are stable across runs 2 and 3. (b) A14-8's own capture records
  why b2(5) shipped broken: *"a two-run temp fixture inside one harness invocation, where the
  SKILL-side write step never ran because the harness stubbed it."* **After Q6 the write side is
  still SKILL-side prose** — `:719-723` says *"This workflow stays READ-ONLY — it returns the
  records, the SKILL persists them"* — so a JS round trip grades workflow-return → workflow-consume
  and **stubs exactly the seam that broke.** The brief must either move the sidecar **write** into a
  shipped script so the round trip runs end-to-end, **or** record that the SKILL-side serialize/merge
  step is **not covered** and tag a second check for it. **A round trip that stubs the writer does
  not discharge A14-8 and must not be tagged ship-verifiable under D3.**

  **⚠ Q5's format reasoning applies to the sidecar too** *(roundtable A7b, 2026-08-26)*.
  `_agent/lint-cache.yaml` is hand-emitted by an LLM and hand-read by the SKILL on the same PEP 668
  machines — **the identical property Q5 rules on for the report — and build-2's check GATES on it
  round-tripping.** Two rulings in one cycle reach opposite conclusions about the same problem on
  two files, and **the one that gates got the harder format.** The brief rules whether
  `_agent/lint-cache.{yaml,json}` follows Q5's `.json` permission.

  **⚠ Returns a `cache_rejected:` count** *(roundtable A39, 2026-08-26)* — the number of records
  discarded by the `:243` filter, rendered in the report. `full-scale.md` step 2 **already mandates**
  that *"a missing, unparseable or schema-mismatched sidecar is a cold run, **stated in the
  report**"* — this cycle's through-line verbatim, with no enforcement point, and it is what failed
  in the field. The round-trip check gates the **module at rest**; it cannot observe a **vault**
  whose sidecar is schema-mismatched. This costs no new argument and is **not** the step-4 widening
  Q6 declined — that refusal predicate stays as ruled.

  ⚠ **BRIEFED 2026-08-27 — the five open questions this block left are RULED**
  (`briefs/build-2-findings-cache.md`; line cites re-derived against v0.16.2 — see the superseding
  note on §Capture → A14-8). In summary, so no later reader re-derives them from prose:
  - **A4 (depends on build-1)** — honoured: every fixture is built against post-build-1 source, and
    `runKey`'s shape is **unchanged** (`:244`); only its third term's provenance moves. Acceptance
    check (2) asserts a record keyed under a different `PAGE_SCAN` is not reusable.
  - **A6 (fresh AND reused)** — the workflow returns `cache_records: [{slug, key, scan}]` for every
    adjudicated page, keyed on the SKILL-supplied `p.slug`, one code path for both halves; the SKILL
    is never asked to re-derive reusability. `fresh_scans:` **retires** (P-15).
  - **A5 (three runs, executable writer)** — **option (a) taken: the writer is built.**
    `skills/vlt-lint/scripts/lint-cache.py` (stdlib-only, read + write modes, atomic, exit 0 on
    missing/unparseable) does every read and write in the cold → warm → warm fixture, so nothing
    but the page-scanner agents is stubbed. The residual — the SKILL *transcribing* 146 records into
    inline workflow args — is named out of scope (tracker #13's territory, Q2) and watched by the
    one field-contingent check, which **does not gate**.
  - **A7b (the sidecar's format)** — **RULED `.json`, and it is the only legal format** (not a
    permission like Q5's). The writer is now a script, so the hand-emission property A7b turned on
    is gone; a YAML writer would need `pyyaml` or a hand-rolled second serializer. The legacy
    `_agent/lint-cache.yaml` is **deleted** by the writer, not converted (Q6: unmigratable).
    ⚠ **Cost, priced:** `vault-operating-contract.md:325` enumerates the sidecar **by literal path**
    in the Decay contracts table, so the rename is an **R4 enumeration widening into the governance
    bundle** and package-lint **C6** requires `_meta/vault-rule-card.md`'s `derived_from: sha256:` to
    be re-stamped in the same build.
  - **A39 (`cache_rejected:`)** — returned **with its denominator** (`cache_records_read`), rendered
    on **both** the warm and the cold branch of `report.md:77`, including zero.
  - **A8 (`full-scale.md` shared with build-4)** — **RULED: build-2 OWNS `full-scale.md`** (steps 2,
    3 and 5); **build-4 cites this brief** and confines itself to step 4 and `:13`, which build-2
    does not touch. A second, finer collision the roadmap did not name: **`vlt-lint/SKILL.md:74`
    carries both the cache sentence (build-2) and the report-persist sentence (build-4) on one
    line** — disjoint sentences, build-2 first; likewise `report.md` (`:77`/`:88` build-2 vs `:3`
    build-4).
  - **The brief-time question as posed** ("components as a list or a pre-joined string") — **neither:
    a named-slot object**, because a positional list re-creates in prose the ordering contract A40
    retires, and a pre-joined string leaves composition SKILL-side. The workflow sorts convention
    names; order is code, not prose.

- **build-3 — governance: A14-6 (the `type:` vocabulary) + A14-7 (the `verified_by` roster).** The
  handshake build. `write-verification.md` 3 → 4 (5 re-acks) + `frontmatter.md` 13 → 14 (10
  re-acks) + the `contract:66` pointer (no bump). **15 re-acks, one bipartite-consistency check.**
  `extraction.md` does **not** move — **but see A15: D2's own grounding may force it to.**
  - `binds:` Q3, Q4, D2, D3, D4, E3, E5
  - `spike:` none

  **⚠ ALSO TOUCHES `vlt-lint-full.js` — this is the THIRD build in that file, and the first to
  re-enter it after release 1 has shipped** *(roundtable A3, 2026-08-26 — found independently by
  nine voices; the block named no files at all)*. The workflow is a listed `consumers:` entry of
  **both** bumped conventions, so build-3 must edit **the `:11` `depends_on:` ack line — which
  package-lint **E5** parses, and the release fails if it is missed** — plus **seven in-prose
  version citations** at `:158`, `:159`, `:164`, `:168`, `:215`, `:571`, `:573`.
  **Nothing catches those seven.** Verified in session: package-lint's **E3** stray-pin check scans
  `skills/vlt-*/SKILL.md` and `skills/vlt-*/references/*.md` and **deliberately excludes
  `vlt-setup/assets/**`** (`tools/package-lint.py:736-739`, comment verbatim). So build-3 can bump
  both conventions, re-ack all 15, **pass the gate green, and ship seven stale citations to every
  vault. The handshake's enforcement point cannot see the sites that restate the rule — this cycle
  is named for that.**
  Worse than staleness: **`:159`, `:164` and `:168` are the workflow's restatements of §Scope rule —
  the rule Q4 amends** — so they are **content re-checks, not version-string bumps**, and by this
  cycle's own D1 they are unenforced copies of a moving rule. And **`:158`/`:159`/`:164`/`:168` sit
  inside `PAGE_SCAN`**, so any edit to them re-enters A1's 102-char budget and moves
  `scanFingerprint`. **Build-3 rebases onto build-1's rewrite of that file (several of these lines
  build-1 rewrites or retires first), writes its re-ack against post-build-1 source rather than
  v0.16.1, and re-runs E5 AND E6.** Ordered after build-2 so `PAGE_SCAN` settles once before the
  re-ack pass reads it.

  **⚠ Also touches `skills/vlt-lint/references/checks.md:17`** *(roundtable A11b, 2026-08-26)*.
  `checks.md:17` carries `para_missing_attestation`'s **"Population carve-out"**, restating the
  container exemption in the check's own words — **it is where §Scope rule actually binds.** Q4 adds
  a second exempt class and neither build-3 nor build-4 adds it there. Ship that and **the
  convention exempts a class the shipped net still flags with no route to clear it — A14-7's exact
  shape relocated one file over.** The convention states the jurisdiction; the check is where it binds.

  ⚠ **SUPERSEDED IN PART — grounding correction at brief time (2026-08-27, `build-brief`)**, recorded
  per `grounding-at-brief-time.md`'s two-place rule. Re-derived against working-tree source at
  `d641050` (post-build-1 **and** post-build-2), `vlt-lint-full.js` now **870 lines**. Brief:
  `factory/cycles/14-no-enforcement-point/briefs/build-3-governance-handshake.md`.
  - **THE RE-ACK FIGURE IS SETTLED: 19, not 15 — `extraction.md` MOVES (7 → 8, 4 consumers).**
    A13's pointer target is ruled **`extraction.md`**, because `checks.md` has **no frontmatter, no
    `version:`, no `consumers:`** (verified `checks.md:1`) and pointing the Layer-3 entry condition
    there would put it beyond every handshake while letting a lint check *define* a governance term.
    The closed recognized-set statement therefore lands in `extraction.md` — which repairs A15's
    falsified `:188` grounding sentence **inside a bump already owed**, and gives A11's `type:`
    discriminator its declaration site at no marginal cost. **D2's "`extraction.md` does NOT move" is
    VOID.** The cycle is **3 conventions / 19 acks / 11 files**. D2's re-put trade (the precedence
    statement) is **not** taken: J2 verified the populations cut apart, so `CLAUDE.md`'s
    precedence-by-elimination still indicates elimination at the true price.
  - **THE SEVEN IN-PROSE PINS ARE NOW SIX SITES / EIGHT TOKENS, and NONE is a content re-check.**
    Re-derived: `:158`→**`:171`**, `:159`→**RETIRED WHOLE by build-1**, `:164`→**`:178`**,
    `:168`→**`:182`**, `:215`→**`:229`** (three tokens on one line), `:571`→**`:682`**,
    `:573`→**`:684`**. `grep -c` over the file: 5 `frontmatter@13` + 5 `write-verification@3`, one of
    each being the `:11` header ack ⇒ **8 in-prose tokens.**
    ⚠ **A3's "three of them restate the very §Scope rule Q4 amends" is SUPERSEDED**: `:159` is
    retired; `:178` (was `:164`) cites the **tier-1 wiki-page item** (`write-verification.md:38`), not
    §Scope rule; `:182` (was `:168`) and `:684` (absent from A3's list) cite §Scope rule's
    **Jurisdiction-boundary** clause, which Q4 does **not** amend. **Every one of the eight is a pure
    version-string bump.** Consequence: **the `:168` dissent (§Carried forward 9) is NOT tripped** —
    it fires when `unmarked_supersession` is *structured*, and build-3 structures nothing.
  - **THE SEVEN GET AN ENFORCEMENT POINT: package-lint `E7`.** D3-as-amended clause 1 (A17b) makes
    the instrument **mandatory** — pin currency inside a workflow asset is gradeable at rest by a
    check next to E5, which already parses that exact header — and `brief-anatomy.md` §7 forbids A3's
    prescribed manual grep as a *recorded verification* (it is self-confirming). **E7 checks every
    `name@version` token in a workflow body against that file's own `// depends_on:` header.** It
    owes a fixture case and `CASE_FLOOR` 23 → 24 (package-lint **E4** / R2). ⚠ **This RETIRES D2's
    "the bipartite verification is manual for those seven" prescription (P-15).**
  - **E6 PRICE: ZERO.** Measured with package-lint's own `_E6_NODE_EXTRACTOR` at `d641050`:
    `PAGE_SCAN` **3688** (INDEX_SCAN 823, CLUSTER_FINDINGS 1630, PAIR_FINDINGS 376). The same
    extractor over a simulated all-pins-rewritten copy returns **3688 — unchanged**, because `13`→`14`
    and `3`→`4` are digit-count-neutral. **12 chars spare, as build-1 left it** — conditional on
    build-3 making **no content edit inside `PAGE_SCAN` (`:158-189`)`**. `scanFingerprint` still moves.
  - **`checks.md:17` IS RULED IN SCOPE (A11b confirmed at the cited line).** Its Population carve-out
    is a **filename-plus-location** test (`charter.md`/`record.md`/`register.md` under a container
    directory), *not* the `type:` test §Scope rule uses — so without the widening a `type: record`
    file outside a container is exempt in the convention and still flagged by the net. Also confirmed:
    `para_missing_attestation` carries **no** pre-adoption clause while `unattested_write` on the same
    line does (A12), and `:19`'s legal response says *"vault-grown"* (A14).
  - **CITE, NOT RESTATE (the deferred wording question, ruled).** §Scope rule **cites**
    `extraction.md`, *PARA containers* — but as a **section** pointer, never `extraction.md:188`: a
    shipped convention must not carry a `file:line` (this brief corrected four of this roadmap's own).
  - **A11's DISCRIMINATOR IS `type:`** — the existing operational-record types `record`/`register`,
    widened from container-file position to a Layer-3 artifact class. §Scope rule's jurisdiction is
    **already** a `type:` test (`write-verification.md:55`) and `record`/`register` are already
    outside it; `checks.md:19`'s recognized set already admits them. ⚠ **Grounding finding that
    settles why it must be `type:` and not a class judgment: `para_missing_attestation` has NO code
    enforcement point** — `vlt-lint-full.js:809` emits it as *"a structural slot the SKILL fills"* and
    `full-scale.md:11` confirms the PARA scan is SKILL-side. **The check is an agent reading prose**,
    so the discriminator must be readable from frontmatter.
  - **A14's TWO OPTIONS ARE BOTH REFUTED; a third is written.** ⚠ *Owner-visible.* Admitting
    `research` to the PARA set re-imports the ambiguity D2 paid to eliminate (J2 holds only because
    `{research}` defaults outside PARA); telling the vault to overlay-declare **module-canonical**
    vocabulary is precisely what the park exists to refuse. Ruled instead: `para_type_unknown`'s legal
    response routes three ways — vault-grown → overlay-declare (unchanged); **module-canonical but
    non-PARA → retype to the target-folder type (`extraction.md:74-78`) or relocate to that type's
    home zone**; otherwise → relocate out of PARA. **That is the written unpark trigger**, graded by
    acceptance check (6).
  - **A12's TRANSITION: the pre-adoption informational posture** (retroactive satisfaction is
    impossible — retyping vault files is a vault act, not a module act). It is also this build's
    **R1 interim posture**.
  - **A16 CORRECTED:** `moc` has zero hits in `frontmatter.md` (confirmed), but it is **not** "named in
    no convention" — `extraction.md:78` already names it as recognizable `para_type_unknown` schema.
    The `:71` addition still lands; the stronger claim is corrected.
  - **Drifted cites corrected:** `vault-operating-contract.md`'s `{wiki}`-removal statement is at
    **`:64`**, not `:65` (A14-6 capture); `write-verification.md` §Scope rule's **body is `:55`**, not
    `:53-54` (A14-7 capture, Q4) — `:53` is the heading and `:54` is blank; E3's exclusion docstring
    is at **`tools/package-lint.py:737-740`**, not `:736-739` (A3). `contract:66`, `:70`,
    `write-verification.md:47`, `:12`, `frontmatter.md:71`, `extraction.md:188`, `checks.md:17`/`:19`
    all **HOLD** at their cited lines.
  - **NEW COST the roadmap did not price: package-lint C6 fires twice over.** Build-3 edits
    `vault-operating-contract.md`, so `_meta/vault-rule-card.md`'s `derived_from: sha256:` must be
    re-stamped — **and `vault-rule-card.md:26` itself restates the entry condition** (*"recognized
    `type:`, attestation pair"*), an **act-blocking** clause that goes over-broad the moment Q4's
    exemption lands. The card is edited, not merely re-hashed. 7,106 of `RULE_CARD_BUDGET` 8,000.
  - **R2 (P-18 Tier B observer) FIRES:** build-3 reaches for a synthetic fixture (acceptance check
    (3)), unavoidably — there is no executable implementation of `para_missing_attestation` to run
    against. Recorded in the BUILT `status:` and named at closeout. Observation duty, never a gate.
  - **Scope is otherwise unchanged.**

- **build-4 — lint references: A14-4 (`sources_vs_prose` misclassification) + A14-5 (the persist
  mandate).** A14-4 adds the second legal response and the direction routing, **and the Step-3
  procedure entry that does not exist today**; A14-5 rewrites `report.md:3`'s both-homes sentence
  and permits `.json`.
  - `binds:` Q5, D3, E1, E2
  - `spike:` none

  **⚠ "Paired because both land in `report.md`" is FALSE — the persist mandate does not live there**
  *(roundtable A8, 2026-08-26 — found independently by five voices)*. **Touches:**
  `skills/vlt-lint/references/report.md`; **`skills/vlt-lint/SKILL.md:74`** — the persist step's
  **single home** (*"write the Step-5 report block **verbatim** to
  `{lint_reports}/YYYY-MM-DD-HHMM-lint.yaml` — plain YAML"*), of which `report.md:3` is only a
  restatement, so permitting `.json` in the restatement **inverts the pointer** and leaves the
  executing skill mandating the other format; **`skills/vlt-lint/SKILL.md:76`** and
  **`references/full-scale.md` step 4** (`-lint-failed.yaml`, a second report class that stays
  YAML-only and un-checkable — **Q5's argument buys it nothing**); **`skills/vlt-setup/SKILL.md:194`**
  (provisions the directory as *"plain `.yaml`"*); **`references/full-scale.md:13`**, where
  `churn_since_last_full` locates the previous full report **"by its dated filename"** — **a
  `.json`-persisting vault is invisible to that discovery and renders `unmeasured (no prior full
  report)` forever, a silent wrong number rather than an error**; and **`references/fix-and-file.md`
  Step 3** for A14-4's missing procedure entry. **`full-scale.md` is shared with build-2** — one
  brief owns the file, the other cites it.
  ⚠ Note a `.json` persist is **not a verbatim copy of the fenced block — it is a translation**, a
  second authoring act `SKILL.md:74`'s word *verbatim* forbids. The brief says which act emits which
  home, or **the cycle ships a permission with no emission point.**

  **⚠ SHIPS THE VALIDATION BEAT — gating** *(roundtable A10, 2026-08-26)*. The capture's own
  top-ranked direction for A14-5 was *"(1) a **validation beat**, not an emitter — the gap is the
  unchecked claim."* Q5 adopts (2) and (3) and says `.json` *"is what **lets** it carry a gating
  at-rest check under D3."* **"Lets" is not "does": D3 binds every check a brief writes; it does not
  require one to exist.** As ruled, build-4 could ship a rewritten `report.md:3` and no parse check
  — **a restated rule with no enforcement point, in the cycle named "no enforcement point", curing a
  filing whose defect is a stated rule nothing checks.** Build-4 ships a check that **parses a
  persisted report whole**; at rest ⇒ ship-verifiable ⇒ it **GATES**.
  Brief-time, added: **if `.yaml` remains a legal persist the check must cover it** (which costs a
  `machine_tools` row) **or the mandate is explicitly scoped to `.json`**; and whether the
  failed-run record and the `churn_since_last_full` lookup accept both extensions.

  ⚠ **SUPERSEDED IN PART — grounding correction at brief time (2026-08-27, `build-brief`)**, recorded
  per `grounding-at-brief-time.md`'s two-place rule. Re-derived against worktree source at `6525715`
  (post-build-1, -2, -3, post-scrub). Brief:
  `factory/cycles/14-no-enforcement-point/briefs/build-4-lint-references.md`.
  - **The `Touches:` list is INCOMPLETE — `skills/vlt-setup/assets/workflows/vlt-lint-full.js` is a
    build-4 site, and it is the FOURTH build in that file this cycle.** A8 amended this list once
    already; it still omitted the workflow. **The ruled direction routing is not expressible without
    it:** `PAGE_SCAN` returns `sources_vs_prose` as a **tri-state**
    (`'match' | 'diverge' | 'no_prose_section'`, `:178`) with a free-text `:179` detail, the prompt's
    Gap B clause (`:229`) says *"'diverge' only when both exist"*, and the reduce (`:795`) filters on
    `=== 'diverge'`. **There is no direction at the reduce**, and inferring one from the free-text
    detail is the reduce-side prose-parsing build-1 just retired and D1 forbids cycle-wide. Recorded
    as a **grounding addition** (`grounding-at-brief-time.md`, *EXPANDED*), not a re-ruling: §Grouping
    ruled build-4 *"adds … the direction routing"*, and the capture itself named the workflow as a
    home of the class (`:665` at v0.16.1).
  - **The enum carries the direction, with A35's escape member.** `match | diverge_prose_gap |
    diverge_frontmatter_gap | diverge_unclassified | no_prose_section`; `diverge_unclassified` is the
    escape and routes to `flag_for_human` (never auto-fixed) — mirroring the `frontmatter_defect`
    enum build-1 shipped into the same file.
  - **E6 price: NEGATIVE 12.** Measured with package-lint's own `_E6_NODE_EXTRACTOR`, never a source
    char count: the two properties serialize to 338 today and 326 after, so **`PAGE_SCAN` goes
    3688 → 3676** against the 3700 gate. **Build-4 RETURNS 12 characters to a budget that had 12.**
  - **The remaining capture/roadmap cites all HOLD, re-verified:** `checks.md:16` (A14-4's check),
    `report.md:21` (the `fix_now` slot), `report.md:3`, `vlt-lint/SKILL.md:74` and `:76`,
    `full-scale.md:10` (step 4) and `:13`, `vlt-setup/SKILL.md:194`. `fix-and-file.md` Step 3 still
    names the class nowhere (`:9`-`:13` is the list). Build-2's collisions verified disjoint:
    `SKILL.md:74`'s cache sentence is build-2's and untouched; `report.md:77`/`:88` are build-2's.
  - **NO governance-bundle edit, and it is a finding not an omission.**
    `vault-operating-contract.md:51` and `:323` name `{lint_reports}` as a **directory with no file
    extension**, so a `.json` persist is already legal under the contract as written. **No C6, no
    `vault-rule-card.md` re-stamp, no convention `version:` move, no re-ack.** `write-verification.md`
    (`version: 4`) already states the symmetric sources requirement (`:38`) and source-completeness
    (`:33`) that the second legal response rests on — **E2 is honoured by construction.**
  - **A10's brief-time additions RULED:** the check covers **both** homes and **no `machine_tools`
    row is owed**, because the instrument is **factory-side** at rest (`uv run --with pyyaml` +
    stdlib `json.tool`) and build-4 adds no vault-side step; the failed-run record **and** the
    `churn_since_last_full` lookup **both** accept both extensions.
  - **The report persist gets NO serializer**, and `lint-cache.py` is neither reused nor shared —
    the report has no machine-constructed object to serialize, an emitter is Q5 option 4 (still not
    taken; A9 struck only its cost rationale), and a report fails by being **unparseable**, so its
    enforcement point is a **reader**, not a writer. Reasoning in full at the brief's disposition 3.
  - **The deferred routing question RULED: `checks.md:16` is the single home**; `fix-and-file.md`
    Step 3 gets the missing procedure entry as a **pointer** that cites it. **`.json` is an
    ALTERNATIVE, not the default** — Q5 already said so, and grounding names the two costs a
    default-flip would incur (`vlt-setup/SKILL.md:194`; `full-scale.md:13`'s filename-based discovery).
  - **Scope is otherwise unchanged**, and build-4 is the **release build** for release 2.

**Deliberately NOT in this cycle, and where each went:** A14-2 (outbound-link enumeration) and
Cycle 13 carry-forward 1 (`summary` paraphrase) — the two faces needing real page bytes, deferred
by Q1 to the build that takes the args route; tracker **#13** — stays deferred per Q2, and becomes
that build's dependency; the `malformed_frontmatter` **retirement** — deferred per Q8, with its
measurement attached to build-1; the step-4 refusal predicate widening — declined in Q6;
**A14-4's *"frontmatter is the source of truth"* qualifier (E2)** — scoped out unmeasured, **filed
to `factory/inbox/` by the owner as a `pattern`** so a later capture grounds it, and carried at
closeout as a deferred question *(roundtable A32)*.

⚠ **A14-2 is captured but UNBUILT, and its filing STAYS in `factory/inbox/` at closeout**
*(roundtable A23, 2026-08-26; John)*. A14-2 is in this cycle's `derives_from:` **with no build and
no ledger clause**, and `cycle-closeout`'s Stage-5 move criterion passes it **vacuously**:
condition 1 (*"every clause traceable to that filing is discharged"*) is trivially true over **zero**
clauses, and condition 2 — the checklist's own warning bound — **cannot bind where there is no
build**. **A literal closeout would `mv` an unrepaired defect out of the active inbox into
`14-no-enforcement-point/filings/`.** Stage 5's criterion does not apply to a filing with no build,
and **clause 1 must not be read vacuously over zero clauses.**

### Pre-ideation rulings the capture demanded

- **Q1 — instances, or the posture?** A14-1, A14-2, A14-3 and Cycle 13 carry-forward 1 are four
  faces of one seam: the reduce performing exact work over agent-returned values it cannot verify.
  Repairing them individually reopens Cycle 13's gate soonest; taking Cycle 13 carry-forward 2's
  general posture (*every agent-returned value that is mechanically checkable at the reduce is
  checked there*) answers all four and the next one. **The capture flagged this as the ruling that
  determines the cycle's size, and noted Q2 and Q6 depend on it.**
  → **RULED Round 1 (2026-08-26): structure the return; defer the ground-truth args.**
  Take the posture **where it needs no new inputs**, on a distinction neither the filings nor the
  capture drew: for two of the four faces the reduce does not need to *verify* the return, because
  the return can be shaped so there is nothing to parse.
  1. **A14-1 — replace the free-text claim with a structured `PAGE_SCAN` return** (an enum plus a
     field list; exact shape settled at brief time). The residue rule at `:594-604` and the
     `claim.residue === ''` conjunction in both predicates (`:612-617`, `:623-628`) exist **only**
     because the scanner returns prose; given structure they have no reason to exist. **This is the
     A14-1 repair, and it is what reopens Cycle 13's gate.**
  2. **A14-3 — decode HTML entities at the seam, on BOTH sides.** `h2set` (`:643`) is agent-returned
     too, so the index side is exposed and its failure is category-wide; both values are already in
     hand, so this costs no new argument. The exact comparison's strictness is **not** softened (D5).
  3. **A14-2 and Cycle 13 carry-forward 1 (`summary`) are OUT of this cycle's reduce work** — they
     are the only two faces needing real page bytes, and therefore the only two that force the args
     question. Not dropped; deferred to the build that takes the args route.
  *Consequence, stated so no brief re-derives it: the general posture is **partially** taken, and
  Cycle 13 carry-forward 2 stays live for the deferred half.*

  ⚠⚠ **AMENDED — the enum MUST carry an unclassified member, or build-1 ships a fresh instance of
  `ST-6`'s own cause inside the build that reopens Cycle 13's gate** *(roundtable A35, 2026-08-26;
  Maya)*. The mechanism Q1 retires is **fail-OPEN by construction**: `:603` returns anything
  unrecognized as `residue`, and the entry **reports**. A closed enum is **fail-CLOSED by
  construction** — a scanner meeting a genuine schema break outside the enum's roster must **mis-file
  it under a member that fits badly, or drop it.** That **inverts the invariant Q7 explicitly rules
  must survive the move** (*"the failure direction is over-reporting, never swallowing a genuine
  schema break"*). And it is **a closed roster meeting an actor the surrounding rules authorize —
  the exact cause D4 opened `ST-6` to name, shipped by the same cycle that names it.**
  **The enum carries an explicit unclassified member with a free-text detail slot, and an
  unclassified disposition REPORTS rather than being refused.** Shipped precedent, already in the
  file: `sources_vs_prose`'s third member `no_prose_section` (`:164`). *The over-reporting failure
  direction is a property of the escape member, not of the fields list — and it is what build-1's
  own acceptance must test rather than inherit as an assurance (Q7).*
  ⚠ Note the budget interaction: this member is **inside** A1's 102-char ceiling and must be costed
  with the rest of the return.

- **Q2 — does the posture re-admit tracker #13?** Every mechanical-verification direction needs
  ground truth the workflow structurally cannot fetch (`vlt-lint-full.js:36-38`), i.e. a SKILL-side
  per-page arg on the `pageHashes` precedent (`:47-49`) — which moves the joint against #13's ~84KB
  inline-args payload cost. #13 was **deferred as net-new at capture by owner ruling**; if the
  posture is taken it becomes a **dependency**, and re-admitting it is an owner ruling. Depends on Q1.
  → **RESOLVED by Q1 (Round 1, 2026-08-26): #13 stays deferred, not re-admitted.** Q1 took the
  half of the posture that needs no new arguments, so the joint does not move this cycle and #13
  remains net-new. It stays un-captured in `factory/inbox/` and out of this cycle's `derives_from:`.
  **It becomes a dependency the moment the deferred half (A14-2, `summary`) is taken** — that build
  cannot be briefed without ruling #13 first.

- **Q3 — A14-6: pointer, or vocabulary?** If the whole defect is that `vault-operating-contract.md:66`
  never names the convention that owns "a recognized `type:`", the fix is a pointer plus a handshake.
  If the two conventions must be reconciled (`frontmatter.md:71` non-exhaustive incl. `research`, vs
  `checks.md:19`'s closed set), it is a vocabulary decision — and `para_author_unknown` is in the
  population too, with no overlay escape at all. **The capture recommends testing the pointer reading
  first**, because `checks.md:19` already ships "declare the vault-grown type as overlay schema" as a
  stated legal response, which is the filing's own option 4.
  → **RULED Round 2 (2026-08-26): pointer only — the closed set governs the PARA population.**
  `extraction.md` / `checks.md:19` owns what "recognized" means **for the PARA population**, and
  `vault-operating-contract.md:66`'s entry condition is edited to **name it**, exactly as the other
  three legs already name theirs inline. `frontmatter.md:71`'s non-exhaustiveness is scoped so it
  no longer answers for that population.
  **Why this is cheap, on record:** the operating contract is **deliberately not handshaked**
  (single-home + pointers — `CLAUDE.md`), so the `contract:66` edit bumps nothing and re-acks
  nobody. And "declare the vault-grown type as overlay schema (declare-at-birth)" is **already**
  `checks.md:19`'s stated legal response — this ruling signposts an answer the module already
  gives rather than inventing one. The filing's own option 4 was never a new rule.
  **Not taken:** widening the recognized set, and generalizing the `{wiki}` by-name exclusion into
  a declared list. Both remain available if a second agent-lane subtree ever forces the question;
  neither is needed to close this filing.
  ⚠ **`para_author_unknown` is untouched and still closed to `human|agent|hybrid` with no overlay
  escape.** Named so a later reader does not read its survival as an oversight. **How
  `frontmatter.md` is scoped is D2's question**, not settled here. *(roundtable, 2026-08-26: **and
  its owning convention is likewise unnamed — the same defect A14-6 repairs for `type:`.** Recorded
  so the third cycle does not rediscover it.)*

  ⚠ **AMENDED — the pointer's TARGET is not settled, and it is not free** *(roundtable A13,
  2026-08-26; Paige, Maya, Sally)*. The ruling names the owner as *"`extraction.md` / `checks.md:19`"*
  — **two files** — and D2 then rules `extraction.md` does not move. Grounding splits them:
  `extraction.md` states a target-folder→`type:` mapping (`:72-82`, incl. `moc` at `:82`) and the
  container types (`:184-186`), but **never states a closed recognized set, never uses the word
  "recognized"**, and its declare-at-birth sentence (`:118`) declares a vault-grown type's `status:`
  vocabulary, **not the type**. Pointing `contract:66` there **requires adding the closed-set
  statement — a rule change, `extraction.md` 7 → 8, 4 consumers — which D2 forbids.** Pointing at
  `checks.md:19` instead points the module's most load-bearing boundary at a file with **no
  frontmatter, no `version:`, no `consumers:`** (verified `checks.md:1`) — **making a lint check
  *define* a governance term instead of implementing one, and putting the entry condition beyond
  every handshake.** The contract's other three legs each point at a handshaked convention; this one
  would not. **Build-3's brief rules the target explicitly. If it is `extraction.md`, D2's
  "`extraction.md` does NOT move" is void and the cycle is 3 conventions / 19 re-acks.**

  ⚠ **AMENDED — the shipped legal response does not cover the blocked population** *(roundtable
  A14, 2026-08-26; Sally, Maya)*. The ruling rests on `checks.md:19` already shipping the answer.
  Grounded: its legal response is *"declare the **vault-grown** type as overlay schema…"* — and the
  field's blocked files carry **`type: research`, which `frontmatter.md:71` lists as
  MODULE-CANONICAL, not vault-grown.** So option A does not apply by its own words, option B
  (retype) discards a canonical classification, option C (relocate) evicts the shelf. **The module
  does not already give an answer for this population**, and the same holds for `note` and `idea`.
  Worse: A14-6's park was filed on the stated grounds that a local overlay would be **a vault
  answering a module-level question** — and this ruling's practical effect is *yes, overlay it*,
  which would have the vault **assert local authorship of module vocabulary. That is the precise
  thing it parked to avoid.** Build-3 therefore also amends `checks.md:19`'s `para_type_unknown`
  legal response to cover **a module-canonical type outside the PARA set** (admit it to the set, or
  state that overlay-declaration covers module-canonical values — and say which), **and the park
  gets a written unpark trigger: an acceptance check that the vault can execute the stated response
  without declaring module vocabulary as its own.**

- **Q4 — A14-7: widen the value set, or narrow the jurisdiction?** Widening admits a partner
  identifier or an in-sitting sentinel — keeps every Layer 3 artifact attested, weakens the field's
  meaning, and owes a story for what the value is checked against. Narrowing exempts partner-sitting
  writes in §Scope rule the way container files already are (`extraction.md:188`) — **has shipped
  precedent**, is honest about what the pair records today, is the cheaper edit, and costs structural
  coverage of a real class. Either bumps `write-verification.md` from `version: 3`.
  → **RULED Round 2 (2026-08-26): narrow the jurisdiction — by ARTIFACT CLASS, not by writer.**
  `write-verification.md` §Scope rule is amended so that the class of Layer 3 file that is an
  **operational record rather than a knowledge artifact** carries no attestation pair — extending
  `extraction.md:188`'s **existing principle** (restated canonically at `contract:70`) to cover
  partner-sitting writes, rather than adding a writer-shaped axis to a list of exemptions that are
  otherwise about *what the file is*.
  **Why by class and not by writer, on record:** §Scope rule's existing exemptions — `daily/`, raw
  `sources/` deposits, human-authored Layer 3 files — are all statements about the artifact.
  "Written during a partner sitting" is a statement about provenance, and fusing permission to
  provenance is `ST-1`'s named primary cause. The class principle is already shipped, already
  reasoned, and already carries a worked instance.
  **Not taken:** widening the `verified_by` value set. Recorded with its reason — it preserves
  structural coverage but weakens what the field means (an op name, checkable against a roster) and
  owes a story for what a partner identifier or in-sitting sentinel would be checked against.
  **Cost accepted knowingly:** a real class of Layer 3 artifact stops being covered by any
  structural check. The filing said so and the ruling accepts it.
  ⚠ **The `local_consumers:` route stays as-is** (`write-verification.md:47`, `frontmatter.md:296`)
  — a vault-minted partner that genuinely *is* a write op can still register and hold a legal
  value. This ruling does not remove that; it removes the need to pretend to be one.
  **Bumps `write-verification.md` 3 → 4 and re-acks all 5 consumers — see D2.**

  ⚠⚠ **AMENDED — the class test needs a MECHANICAL DISCRIMINATOR, named in the ruling, or the
  ruling reverts** *(roundtable A11, 2026-08-26 — found independently by five voices; the room's
  single strongest finding after the schema budget)*. The precedent this ruling extends is not a
  class judgment. **`extraction.md:188` is RATIONALE, not a predicate** — it is a label attached to
  three filenames; the shipped carve-out is enforced mechanically and by name at `checks.md:17`
  (*"container files (`charter.md`/`record.md`/`register.md`) under a `{projects}`/`{areas}`/
  `{resources}` container directory"*). §Scope rule's jurisdiction today is likewise a **mechanical
  frontmatter test** (`type: wiki|research|project|area|resource` with `author: agent|hybrid`, minus
  three location exemptions) — **which is exactly why `extraction.md:188` was cheap.**
  *"An operational record rather than a knowledge artifact"* is **neither a frontmatter fact nor a
  path fact.** `write-verification.md:13-15` declares `enforcement_checked_by: vlt-lint` — **so the
  rule's own declared enforcement point has no input that decides it, and neither does the partner
  deciding whether to attest.** A14-7's population carries `type: project|area|resource|research`
  with `author: agent|hybrid`, **indistinguishable from the artifacts that must stay covered**; the
  only thing separating the two populations is **the writer**, which Q4 correctly refused on `ST-1`.
  **In the cycle named "no enforcement point", build-3 would ship a rule with no enforcement point**
  — and the partner's journey dead-ends one step **later** than before: it used to have no honest
  `verified_by`; now it would have no way to know whether it needs one, and lint no way to agree.
  **The exemption MUST be expressible in the frontmatter §Scope rule already reads — a `type:`
  value, a declared field, or a location — and build-3's brief NAMES it. If no such discriminator
  exists, Q4 reopens and the fallback is the not-taken widening.** If the discriminator is a new
  `type:` value it is declared in `extraction.md` and re-opens A13's scope; if a new declared field,
  it rides the `frontmatter.md` 13 → 14 bump already owed. **Build-3's brief-time question is
  promoted from "the exact wording" to the discriminator, and is BLOCKING.**

  ⚠ **AMENDED — the TRANSITION is ruled here, not left to the field** *(roundtable A12,
  2026-08-26; Sally)*. Whatever discriminator A11 forces, **no existing file carries it** — so on
  the day build-3 ships, the 27 measured files are still in jurisdiction, still flagged, and still
  hold only the two responses the filing called illegitimate. Verified: `checks.md:17`'s
  `unattested_write` is *"informational, not a violation, for files whose `created` predates
  convention adoption"* — **`para_missing_attestation` carries no such pre-adoption clause.**
  **A narrowing that legalizes only files not yet written is not a repair for the vault that filed
  it.** Build-3 either satisfies the discriminator retroactively for files already on disk (stating
  how) **or ships a pre-adoption informational posture for `para_missing_attestation` matching
  `checks.md:17`'s clause**, and its acceptance names what happens to the measured population. The
  **type distribution of those 27 across §Scope rule's jurisdiction list is unmeasured** — measure
  it, or the exemption's reach is unknown.

  ⚠ **AMENDED — the CONTRACT's entry condition still demands the pair, and D2 forbids bumping it**
  *(roundtable A12b, 2026-08-26; Amelia)*. The pair is not merely a lint net — it is **a term of
  `contract:66`'s Layer-3 entry condition**: *"Content that carries it is in; content that does not
  is out, wherever it sits."* `:70`'s existing carve-out names container files **by class and
  nothing else**. After build-3, a partner-written operational record in `{resources}` would be
  exempt from the finding **while the contract still says it is "out" of Layer 3** — **the batch
  would resolve A14-7's two-surface disagreement by creating a new one, the same shape, one file
  over.** So `vault-operating-contract.md` gains the A14-6 pointer at `:66` **and** the Q4 class
  carve-out (widening `:70`'s operational-record sentence, or qualifying `:66`'s attestation-pair
  leg) — **still no bump, the contract is deliberately not handshaked** — and **build-3's acceptance
  checks that the contract and `write-verification.md` state the same exemption.**

- **Q5 — A14-5: which direction, given the `machine_tools` cost?** The capture re-ordered the
  filing's own list: (1) a **validation beat** — the gap is the unchecked "parses whole in both
  homes" claim, not a missing emitter; (2) state the no-dependency requirement + JSON-subset emission
  in `report.md` (pure documentation, zero cost); (3) allow `.json` as an alternative persist (touches
  the both-homes rule directly); (4) ship an emitter — **costs a `machine_tools` row in the same
  build** per that block's writer clause, which is why it ranks last here and first in the filing.
  → **RULED Round 4 (2026-08-26): allow a `.json` persist, and document the emission strategy.**
  `report.md` gains (a) an explicit **no-dependency** requirement with the JSON-subset emission
  strategy stated — every scalar a JSON string, lists as `- <json>`, nested maps by indentation —
  and (b) **`.json` as a legal alternative persisted format**, the fenced in-session block staying
  YAML for human reading.
  **The reason for this direction over the filing's own first choice, on record:** a `.json` persist
  makes the *"parses whole in both homes"* claim **checkable with `python3 -m json.tool` against an
  already-declared tool**, which is what lets it carry a **gating at-rest check under D3**.
  ⚠ **AMENDED — the ORIGINAL rationale rested on a false premise and is struck** *(roundtable A9 /
  owner Ruling 4, 2026-08-26; Maya, verified in session by the moderator)*. The ruling as filled read
  *"`json` is Python **stdlib** and `yaml` is not — that asymmetry is the whole ruling … at zero
  `machine_tools` cost"*, resting on the capture's statement that `machine_tools` *"currently
  declares exactly one vault-side tool assumption: `gh`."* **That is false against working-tree
  source.** `skills/vlt-setup/assets/module.yaml` declares **four** — `gh`, **`uv`**, **`python3`**,
  `git` — and **`uv`'s declared purpose is literally *"vlt-setup / vlt-upgrade merge + manifest
  scripts (PEP 723 inline deps)"***, which is the mechanism for obtaining a `yaml` dependency on a
  PEP 668 machine **without a new row**. **The stdlib asymmetry the ruling turned on does not
  exist.** The `.json` direction **STANDS on the corrected reason above** (owner ruling); recorded
  because the not-taken option 4 (ship an emitter) **was ranked last for a `machine_tools` cost it
  does not incur**, and a later cycle re-opening this must know that. Documentation alone leaves the
  claim unenforced, which is the exact defect this cycle is named for; an emitter asset would
  enforce it but owes a `machine_tools` row.
  ⚠ **This rewrites `report.md:3`'s "both homes" sentence** — it must be restated, not appended to,
  or the bundle asserts one format while permitting two.

- **Q6 — A14-8: fix the shapes, or remove the seam?** The field named five directions. The capture's
  reading is that (1) moving the record wrapping **into the workflow** and (2) moving
  `rulesetFingerprint`'s computation into the workflow are strictly better than documenting either,
  because they remove the derivation rather than describing it. Also open: (5) whether the step-4
  refusal predicate widens so "cold because unreadable" is distinguishable from "cold because the
  ruleset moved."
  → **RULED Round 3 (2026-08-26): remove both seams; leave the step-4 predicate alone.**
  1. **The workflow returns write-ready `{slug, key, scan}` records** instead of raw `fresh_scans`
     (`:723`), so the read shape (`:243`, `:344`) and the written shape cannot drift apart again.
  2. **The fingerprint is composed in the workflow.** ⚠ **Correction to the capture's reading,
     issued in session:** the capture said moving `rulesetFingerprint`'s *computation* into the
     workflow was strictly better. That is only half available — the fingerprint's inputs include
     each convention's digest **as merged with its overlay** and `checks.md`'s digest, and the
     workflow cannot read files (`:36-38`), so the SKILL must compute the component digests
     regardless. **What moves is the composition** — canonical member order, separator, digest and
     truncation — with the SKILL passing components and the workflow assembling them. That still
     kills the defect (one implementation composes), and it is a narrower move than the capture
     described. A brief must not scope it as "compute the fingerprint in the workflow."
  3. **The round-trip check ships and GATES** (D3: at-rest instrument ⇒ ship-verifiable): write the
     sidecar, read it back, assert every record is reusable against an unchanged corpus.
  **Not taken: (5), widening the step-4 refusal predicate.** Recorded with its reason — the
  round-trip check is a *direct* instrument for the failure the predicate would only *infer*, and
  under D3 it gates, so the invisibility is closed at its source. Available if the round-trip check
  proves insufficient.
  ⚠ **The existing sidecar cannot be migrated.** It stores `fingerprint:` once at top level and no
  per-page digest, so it cannot express the reader's key even in principle — the first run after
  this build is COLD by construction, and the brief should say so rather than let it read as a
  regression.

  ⚠ **AMENDED — the composition move kills only HALF the defect** *(roundtable A7, 2026-08-26;
  Builder)*. Defect 2 was grounded as *"no separator, no hash algorithm, no encoding, no truncation,
  no canonical member list."* Moving **composition** single-homes separator, member order and
  truncation. It does **not** touch **hash algorithm or encoding** — those belong to the component
  digests Q6 explicitly leaves SKILL-side, and `full-scale.md` step 2 states them with **no
  instrument, no merge order, and no digest algorithm.** (Contrast step 1, which for `pageHashes` at
  least names `shasum -a 256` and a property.) **Two conformant executors still produce different
  fingerprints from identical rulesets — exactly the field's `980d749d9acf418e` vs
  `66d27a0e6cd8fabe`, which the grounding never attributed to the composition half.** So: **the
  component digests must be single-homed as executable steps in `full-scale.md` step 2 in the same
  build** — named instrument, merge order (base then overlay), encoding, truncation — **or the
  fingerprint stays non-deterministic and only its composition is fixed.**

  ⚠ **AMENDED — step 2's ordering clause is RETIRED with the move, not left beside it** *(roundtable
  A40, 2026-08-26; Victor)*. `full-scale.md` step 2 specifies the fingerprint as *"a digest over,
  **in this order**: …"*. Once composition moves into the workflow, **that clause describes an
  algorithm the SKILL no longer performs.** Left standing beside the workflow's implementation it
  **re-creates A14-8's exact shape — one contract in code, one in prose, nothing where they meet.**
  It is replaced by a **component-list contract** (what the SKILL passes), never amended to sit
  alongside.

- **Q7 — A14-1's false safety comment.** `vlt-lint-full.js:559-561` asserts the guards *"never fire
  on a claim they cannot positively identify — the failure direction is over-reporting, never
  swallowing a genuine schema break."* The field refuted the safety property. Whatever build takes
  A14-1 must **correct the comment or retire the claim** — a shipped comment asserting a refuted
  property is the same defect one level out. Ruling needed on which.
  → **RESOLVED by Q1 (Round 3, 2026-08-26): the comment goes with the guard.** Q1 replaces the
  free-text claim with a structured return, which removes the residue rule the comment describes —
  so `:559-561` is not corrected, it is **retired along with the mechanism it documents**. The
  build states the new invariant in its place. *Recorded because the honest half of the old comment
  must survive the move: the failure direction is over-reporting, never swallowing a genuine schema
  break, and that property must hold of the structured return too — it is a claim the round-trip of
  Q1's own acceptance should test, not an inherited assurance.*

- **Q8 — Cycle 13 carry-forward 3, the `malformed_frontmatter` retirement.** Its named successor is
  the build that takes Q1's general posture. It was deferred because retiring a shipped finding class
  needs a **measured** population first — and Cycle 13's check (2), which was to be that measurement,
  **FAILED**. So the measurement does not exist and the taking build must produce it. Ruling needed
  on whether the retirement rides this cycle at all.
  → **RULED Round 3 (2026-08-26): defer again — but attach the measurement to A14-1's build.**
  The retirement does **not** ride this cycle. Q1 changes the class's genuine population a second
  time (a structured return alters what can reach `malformed_frontmatter` at all), so retiring it
  now would be a behavioral removal on grounds that are not merely unmeasured but **about to
  change**. **The correction to the pattern:** A14-1's build carries an acceptance check that
  *produces the measurement* — what genuinely reaches the class once the structured return ships —
  so the successor build inherits real numbers instead of a third deferral with nothing behind it.
  *This is the third cycle this retirement has been carried; the deferral is only defensible
  because it now ships with the instrument that ends it.*

  ⚠ **AMENDED — J1 answered, and the real fault is elsewhere** *(roundtable A19, 2026-08-26)*.
  **The room went looking for the circularity the roadmap itself flagged and did not find it**
  (Winston, conceding on the evidence; Amelia concurring): Q8 measures the **post-repair**
  population, which is the population a retirement decision actually needs — measuring the
  pre-repair one would be the error. **Three real faults replace it:**
  1. **It must be able to FAIL.** `brief-anatomy.md:245-247` binds both tags to *"a discharging
     instance must be one that could have failed"*, and `tools/package-lint.py:56-59` already ships
     the principle (*"a gate check with no fixture case is itself a lint failure"*). **A population
     count has no failing state and would discharge on the act of counting.** The check therefore
     **asserts a stated bound** on the class's post-repair population, not merely reports a number.
  2. **It is a SPECIMEN SET, never a bare count.** `ST-5`'s direct evidence is the 20 → 2 → 2 → 0
     trace in which the filing's phrase *"18 entries"* is precisely what left the briefer nothing to
     build from. **Inheriting a cardinality would reproduce ST-5 one section below the citation.**
     The measurement is **slug plus the minimal triggering fragment for every page reaching the
     class**, materialized in `factory/cycles/14-no-enforcement-point/`.
  3. **Its two halves are DIFFERENT instruments and the brief must say so.** Pre-change: the
     persisted `{lint_reports}` archive already holds `malformed_frontmatter:` entries across
     multiple full sweeps — **a real corpus needing no new sweep** (Carson). Post-change: only a
     live sweep produces it, because **build-1 changes the return's shape, so pre-change recorded
     returns are free-text the post-change schema cannot emit** (Maya, Amelia) — and no wiki corpus
     ships in this repo. **Under D3-as-corrected (bounded, not at-rest) the check is BOUNDED and
     therefore GATES**, bounded to the first full `{field-vault}` sweep after release 1.

### Cross-filing decide-once rulings

- **D1 — the `verbatim` enforcement question, decided once.** `PAGE_SCAN` marks fields *verbatim* in
  schema descriptions (`:158`, `:162`) and Cycle 13 established a schema description is an
  instruction, not an enforcement point. Two faces are live: **paraphrase** (Cycle 13 carry-forward 1,
  `summary`) and **re-encoding** (A14-3, `category`, HTML entities). A third surface is exposed and
  has not fired: `h2set` is built from the *index scanner's* returned `h2_headings` (`:643`), so a
  `&amp;` on the index side falsifies **every page in that category at once**. Decide the enforcement
  posture once across all three rather than per-field.
  → **RESOLVED by Q1 (Round 3, 2026-08-26): structure or normalize at the seam; never rely on the
  word `verbatim`.** The posture, stated once for all three surfaces: a field the reduce works on
  exactly is either **returned in a machine-checkable shape** (A14-1's claim → structured) or
  **normalized on intake at the seam** (A14-3's encoding → entity-decoded, on **both** sides, since
  `h2set` at `:643` is agent-returned and its failure is category-wide). **The word `verbatim` in a
  schema description is documentation, never an enforcement point, and no build may treat it as
  one.** The third surface — the **paraphrase** face (`summary`, `:162` → `:545`) — cannot be
  closed by either move without real frontmatter, so it is deferred with A14-2 per Q1. *The posture
  is ruled whole here even though it is applied in two cycles: the deferred build inherits it
  rather than re-deciding it.*

- **D2 — the handshake scope for this cycle, decided once.** Q4 bumps `write-verification.md`
  (`version: 3`, 5 consumers) under either direction. Q3 under a widening reading touches
  `frontmatter.md` (`version: 13`) and/or `extraction.md` (`version: 7`, 4 consumers). Rule the total
  bump-and-re-ack set once, in one build, so the bipartite-consistency check is satisfied in a single
  edit rather than re-derived per build. `build-brief` gates on it.
  → **RULED Round 3 (2026-08-26): two conventions move, in ONE build. Elimination, not precedence.**
  - **`write-verification.md` 3 → 4**, re-acking all **5** consumers
    (`vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-lint-full.js`) — forced by Q4's §Scope
    rule amendment.
  - **`frontmatter.md` 13 → 14**, re-acking all **10** consumers
    (`vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint, vlt-dispatch, vlt-setup, vlt-groom,
    vlt-query, vlt-lint-full.js`) — `:71`'s non-exhaustiveness is **scoped** so its `type:` list
    governs the base/agent lane and explicitly does **not** answer for the PARA population.
  - **`vault-operating-contract.md:66`** gains the pointer. **No bump** — the contract is
    deliberately not handshaked.
  - **`extraction.md` does NOT move** (stays `version: 7`): Q3 takes no widening, and Q4 extends
    `extraction.md:188`'s principle by **citing** it from `write-verification.md` §Scope rule, not
    by editing it.
  **Total: 2 conventions, 15 re-acks, one bipartite-consistency check, one build.**
  **Why elimination and not the cheaper precedence statement, on record:** `CLAUDE.md`'s
  *precedence by elimination* rule makes a precedence statement **the fallback**, legal only where
  the populations cannot be cut apart. Here they cut cleanly — the PARA population versus
  everything else — so narrowing `frontmatter.md`'s population is the indicated move. The 10
  re-acks are the price of not leaving a canonical value that is simultaneously well-formed and a
  loud finding, resolvable only by reading a third file.

  ⚠⚠ **AMENDED — the narrowing FALSIFIES a sentence in the one convention D2 forbids moving**
  *(roundtable A15, 2026-08-26; Builder, Amelia, Sally)*. The container types are grounded by a
  **circular pointer pair**: `frontmatter.md:71` names `charter|record|register` pointing at
  `extraction.md`, and **`extraction.md:188` closes with *"The three `type:` values … ride
  `frontmatter.md`'s declared non-exhaustive `type:` list — named here, no contract edit owed."***
  Container files sit under `{projects}`/`{areas}`/`{resources}` and are in the `para_*` population.
  **Scoping `:71` out of the PARA population makes `:188`'s grounding sentence false the moment
  build-3 lands, in the very population where those three values are used.** Repairing it edits
  `extraction.md` — a rule change: **`version: 7 → 8`, 4 consumers. 15 re-acks become 19, and D2's
  own cost line is wrong.** *(Compounding, same site: `:188` is also the precedent Q4 extends, and
  A11 finds it is rationale rather than predicate.)*
  **Build-3's brief settles the number before it is written.** If the owner will not pay 19, **the
  alternative is the precedence statement D2 rejected — and that trade is re-put with the true
  number in view**, since D2 chose elimination over precedence partly on cost. *(Owner Ruling 2,
  2026-08-26: the four-build shape holds and this is absorbed as a brief-time scoping fact; the
  re-pricing is not waived.)*

  ⚠ **AMENDED — the cut is asymmetric: it opens `moc` in the other direction** *(roundtable A16,
  2026-08-26; Amelia)*. `checks.md:19`'s recognized set includes **`moc`**, and **`frontmatter.md`
  never mentions `moc` — zero hits in the file.** Narrowing `:71` so it does not answer for the PARA
  population leaves `moc` **recognized by a shipped lint check and named in no convention** — the
  ambiguity is not eliminated, it **changes direction**. The same edit therefore **adds `moc` to
  `:71`'s canonical list**, inside the 13 → 14 bump already owed.

  ⚠ **AMENDED — the re-ack surface is larger than the bipartite check can see** *(roundtable A3,
  2026-08-26; Caravaggio, Builder, Paige, Carson, Maya, Amelia, John, Victor)*. **15 re-acks is the
  `depends_on:` surface. `vlt-lint-full.js` additionally recites the two conventions by version at
  SEVEN in-prose sites** (`:158`, `:159`, `:164`, `:168`, `:215`, `:571`, `:573`). Verified:
  `handshake-check.py` reads only `version:`/`consumers:` and the flat `depends_on`; package-lint
  **E5** parses only `:11`; and **E3's stray-pin net deliberately excludes `vlt-setup/assets/**`**
  (`tools/package-lint.py:736-739`). **So the bipartite check passes green while seven stale
  citations ship to every vault — three of which (`:159`, `:164`, `:168`) restate the very §Scope
  rule Q4 amends, making them wrong rather than merely old.** **Build-3 greps `write-verification@3`
  and `frontmatter@13` across `skills/`, updates every hit, and its verification NAMES the grep** —
  the bipartite verification is manual for those seven. **Total: 15 re-acks + 7 prose pins, one
  bipartite check, one manual grep.**

  ⚠ **Recorded as a RETIREMENT under P-15** *(roundtable, 2026-08-26; Amelia)*: `frontmatter.md:71`'s
  open-vocabulary clause **ceases to govern the PARA population**; `checks.md:19`'s closed set
  supersedes it there. **Named, not silently survived** — D2 performed the narrowing and did not
  record it as a retirement.

- **D3 — the ship-verifiable / field-contingent tagging posture for this cycle.** ⚠ **The capture
  and the Cycle 12 ruling both flag this as the cycle's most consequential procedural decision.**
  b2(5) was tagged field-contingent, therefore did not gate, and v0.16.0 shipped a findings cache
  **that has never once worked** on a green ship-verifiable ledger (A14-8; `ST-5` causes 2 and 3
  compounding). A14-8's round-trip check is gradeable **at rest**, so nothing forces it to be
  field-contingent. Precedent for the correction exists: B7-6 retired the four-cycle A4-4(5) debt
  precisely by tagging it ship-verifiable so it gated. Rule the posture once, for every check this
  cycle writes.
  → **RULED Round 1 (2026-08-26): an at-rest instrument ⇒ the check is ship-verifiable and it
  GATES.** `field-contingent` is reserved for checks that **genuinely cannot be graded before
  shipping** — never for checks that are merely more convincing in the field. This binds **every
  check every brief in this cycle writes**; `build-brief` reads it as a cycle-level constraint, not
  a per-check judgment. Rationale on record: B7-6's correction (which retired the four-cycle
  A4-4(5) debt by tagging it ship-verifiable so it gated) promoted from a one-off to a standing
  rule, aimed at the mechanism that let b2(5) through.
  **Immediate application:** A14-8's round-trip check is gradeable at rest and therefore **GATES**.

  ⚠⚠ **AMENDED — D3 was written on the WRONG AXIS, and as drafted it makes FEWER checks gate, not
  more** *(roundtable A17, 2026-08-26 — reached independently by Winston and Mary; corroborated by
  Quinn, John, Amelia, Maya)*. The shipped criterion is **boundedness**, not at-rest gradability.
  `build-brief/references/brief-anatomy.md:203-210` defines `[ship-verifiable]` as **three** species
  — *"dischargeable **at rest, at the release gate, or on the next ordinary upgrade**. **Bounded**:
  an event that is going to happen anyway will settle it"* — and `[field-contingent]` as the
  **unbounded**: *"nothing in the build, the release, or the upgrade causes it."* **D3's phrasing
  ("field-contingent is reserved for checks that genuinely cannot be graded before shipping") pushes
  the upgrade-bounded species — which GATES today — into field-contingent, where it stops gating.**
  And the check it costs is **E4's** (see Q8). **The operative sentence is therefore restated:**
  → *"A check whose discharging event is **bounded** — at rest, at the release gate, or on the next
  ordinary upgrade — is **ship-verifiable and it GATES**. `field-contingent` is reserved for the
  genuinely **unbounded**, per `brief-anatomy.md:203-210`. **An at-rest instrument is one sufficient
  bound, not the criterion.**"*

  ⚠ **AMENDED — D3 binds the TAG; it does not bind INSTRUMENT ADEQUACY, which is what actually
  failed** *(roundtable A17b, 2026-08-26; John, Builder, Amelia)*. Verified: b2(5)'s shipped text
  (`12-proxy-claims/roadmap.md:2807-2816`) bound its event to *"the owner runs `vlt-lint --full` …
  **twice** after upgrading"* — a field event with no at-rest instrument available, **correctly
  tagged** under the shipped definition. **Under D3, b2(5) is STILL field-contingent and STILL
  non-gating: the rule does not reach the failure it cites as its whole motivation.** What failed
  was its sibling — **an at-rest instrument that stubbed the seam and was believed.** D3's
  antecedent is also the briefer's discretionary output, so *not writing an instrument* is a route
  out of the gate. **Two clauses close both:**
  1. *"Where a check's subject is gradeable at rest by an instrument buildable inside the build's
     own scope, the brief **must build it**. Declining is a written justification in the brief,
     never a tag choice."*
  2. *"Every brief states, **per ship-verifiable check, which seam its named instrument actually
     crosses**"* — see **R1** in the Roundtable review record.

  ⚠ **AMENDED — the routing sentence was not true as written; the P-N already exists** *(roundtable
  A18, 2026-08-26; Amelia's grounding, correcting Quinn's reading)*. The closing note read as if
  `ST-5`'s fix were unrouted. It is **already on the platform ledger as P-18 Tier C — "gating
  honesty (`ST-5` C8/C9)"** (`factory/platform/roadmap.md:697-701`), **precondition-blocked behind
  P-18 Tier A** (*"Tier A must first produce one cycle of real manifests"*), and **P-18's in-cycle
  repair lane (`:703-705`) names ruling D3 directly.** So: **no new P-N opens.** D3 is the
  cycle-scoped stand-in for P-18 Tier C and **expires when Tier C lands**; a Tier C build must read
  this ruling. D3 is **re-ruled per cycle, never inherited as precedent** — the honest statement is
  that the lifecycle fix is *deferred by a stated precondition*, not merely unwritten.

  ⚠ **NOT taken, recorded with its reason** *(roundtable, 2026-08-26; John's obsolescence finding)*.
  John argued D3 should be **cut to a pointer** at `brief-anatomy.md:242-243` (*"Do not use the tag
  to dodge rigor … Tagging a ship-verifiable check field-contingent to get it out of the gate is the
  vacuous-discharge failure wearing a new hat"*) — i.e. that D3 is that shipped prohibition re-said
  one cycle down, **a rule restated where it already lives, which adds no enforcement point.** The
  room agrees the observation is correct and that **D3 must never restate the definition** (it now
  cites it, per A17). It is kept as a **cycle-scoped tagging instruction applying the shipped
  definition** because the two new clauses above are genuinely new. **Dissent recorded: a pointer
  plus the instrument-adequacy clause would have been the smaller, single-homed move.**

- **D4 — is "a closed roster meeting an actor the surrounding rules authorize" a named pattern?**
  Three live instances: A14-7 (`verified_by` roster vs the contract's open writer set), the Cycle-10
  decision-log Writers-roster filing (`origin: mggower/bmad-module-vlt#6`, still in the inbox), and
  arguably A14-6 in the vocabulary register rather than the writer register. **No study holds this
  cause** — `ST-1` is adjacent but bottoms out in one verb's shape. Opening `ST-6` gates nothing and
  is the author's call (`factory/studies/README.md`, *Citable, never blocking*); the ruling here is
  whether this cycle patches the instances or names the cause first.
  → **RULED Round 4 (2026-08-26): open `ST-6` now, while all three instances are grounded and in
  hand.** It gates nothing and blocks nobody (`factory/studies/README.md`, *Citable, never
  blocking*), and the register's own documented failure mode is **a cause re-derived because nobody
  thought to look** — which has already happened twice (ST-1 → ST-2 at five days; the 2026-08-24
  session → ST-2's RC2 at one day).
  **Not a reason to defer:** that Q3 and Q4 repair two of the three instances this cycle. A study's
  test is the **cause**, not the fix (`README.md`, *What does not earn an entry*) — a cause whose
  repair already shipped still passes if naming it would change how a later cycle reads a problem
  it has not met yet. **The study is written from the pre-repair state; the repairs are recorded in
  its `cited_by:`.**

- **D5 — the named-to-be-rejected directions, recorded so no brief re-derives them.** A14-2's
  candidate 3 (ask the scanner to return links more carefully) and A14-3's candidate 3 (loosen the
  category comparison) were each named to be rejected **by their own filings**, and the capture
  agreed: the first is the prompt-side fix whose failure is Cycle 13's entire premise; the second
  retires real drift findings to work around a transport defect. Confirm as standing, or reopen.
  → ⚠ **Sharpened by Q1 — the two can be misread as contradictory, and the distinction is
  load-bearing.** Q1 rules that A14-1's claim return is **restructured**, which a careless brief
  could read as A14-2's rejected candidate 3 ("ask the scanner to return links more carefully").
  They are different acts: **changing what the schema asks for, so the answer arrives in a
  machine-checkable shape, is not the same as asking the scanner to try harder at the same
  free-text task.** The first removes the parse; the second is the prompt-side plea whose failure
  is Cycle 13's entire premise. **Both rejections stand.**
  → **CONFIRMED as sharpened (owner, at the roundtable, 2026-08-26): both rejections stand.**
  *(roundtable A-D5, 2026-08-26 — the slot read "(owner to confirm as sharpened)" while the
  frontmatter, this section's header, and §Next lifecycle move all asserted "every slot is ruled",
  and **build-1 `binds:` D5**. `build-brief` gates on the section being filled and would have read
  an unconfirmed slot as filled. Victor tested the beat here and returned a negative on record:
  both re-confirmed rejections are of directions **never built**, so **a rejection of an unshipped
  direction has no site to retire** — D5 adds no retirement and the Q1 sharpening is a genuine
  distinction, not a preserved prohibition.)*

### Spikes

**Register read 2026-08-26** (`factory/platform/spikes/`; mechanics single-homed at its `README.md`).
**No `proposed` or `running` entries — this batch inherits no open spike.** The capture opened none:
every claim in all eight filings was groundable against module source in the working tree, and no
grounding hit an external unknown.

- `S-1` (para-container-harvest) — **consumed** (verdict `proceed`; Cycle 9 → consumed Cycle 10).
- `S-2` (projection-baseline) — **consumed** (verdict `proceed`; Cycle 3).
- `S-3` (github-notification-semantics) — **harvested, unconsumed** (verdict `reshape`, run
  2026-08-24, owner-delegated; opened for Cycle 11 A11-2, which deferred to Cycle 12). `harvested`
  is the state the gates accept, so it is available to any build that wants it. Listed here so it is
  not rediscovered at brief time — **not** a claim that this batch needs it.

**Spikes this batch newly demands: NONE (ruled Round 4, 2026-08-26).** Every build above carries
`spike: none`. No grounding in this cycle hit an external unknown — all eight filings grounded
against module source in the working tree — and none of the four builds reads an external source.
*No register file changes as a result of this session; `S-3` stays `harvested`, unconsumed.*
*(Register hygiene, per `factory/platform/spikes/README.md`: **every spike disposition made**
here (open a spike, kill one, rule a build `spike: none`) is written back to the register file in
the same session; status and `verdict:` live there, never only in roadmap prose.)*
*(roundtable A30, 2026-08-26 — the section ended in an orphaned fragment with a dangling
close-paren and no subject; the lost opener is the clause that makes the register authoritative
over roadmap prose, and `build-brief` gates on this section.)*

### Evidence-debt dispositions

*Ruled Round 4 (2026-08-26) — each debt attached to a build or ruled not-blocking. Two constrain a
brief's text (E2, E5); one is discharged by a build (E4).*

- **E1 — A14-4's root-cause guess is unverified.** The filing argues the `fix_now` classification was
  set from the check's *detectability* rather than its *remediability*. Capture could neither confirm
  nor refute this from source; it is recorded as the filer's reasoning. A fix does not depend on it.
  → **NOT BLOCKING (Round 4). Attached to build-4 as context, not as a premise.** The fix — a second
  legal response routed by divergence direction — stands or falls on the measured 0% application
  rate across two full sweeps, which is grounded. **No brief may assert the
  detectability-vs-remediability account as a finding**; it is the filer's reasoning, unverified.

- **E2 — A14-4's qualifier has an unmeasured blast radius.** The filing argues *"frontmatter is the
  source of truth"* needs re-scoping — authoritative about what a page *claims to rest on*, not what
  it *actually cites*. That is a claim about `write-verification.md`'s tier-1 item, not only about a
  lint slot. Neither the filing nor the grounding measured how far it reaches.
  → **SCOPED OUT of this cycle (Round 4), and named so it is not lost.** Build-4 rewrites the
  **lint check's** fix direction only; it does **not** touch `write-verification.md`'s tier-1 item.
  Rationale: build-3 already moves `write-verification.md` 3 → 4, and folding an unmeasured
  re-scoping of *"frontmatter is the source of truth"* into that bump would put an unbounded claim
  inside a 15-re-ack handshake. **If the qualifier is real it is a filing, not a footnote** —
  measure the blast radius first.
  ⚠ **AMENDED — it is routed, or it evaporates** *(roundtable A32, 2026-08-26; Mary)*. E2 prescribes
  the remedy and **names nobody to measure it and nothing to file it**, and its item is **missing
  from §Grouping & order's "Deliberately NOT in this cycle, and where each went"** — the roadmap's
  purpose-built destination. `closeout-checklist.md:74` is unambiguous: *"anything left off here is
  silently dropped."* **The one entry in the batch whose disposition is "this deserves its own
  filing" was the one entry with no route to becoming one** — and the cycle it would land in is the
  cycle that has just bumped `write-verification.md`, and will be least inclined to reopen it.
  **Routed: the owner files it to `factory/inbox/` as a `pattern` against `write-verification.md`'s
  tier-1 item**, so a later capture grounds it. Listed in "where each went" and carried at closeout
  as a deferred question. **Not a build in this cycle.**

- **E3 — A14-7's counts are single-vault.** 27 unattested / 5 attested / 0 partner-sitting-attested
  are `{field-vault}`-local. They establish the class is large and ordinary there; they establish no
  rate for vaults generally, and the filing does not claim they do.
  → **NOT BLOCKING (Round 4). Attached to build-3.** The counts establish the class is large and
  ordinary in one vault, which suffices for a jurisdiction narrowing — the ruling turns on what the
  attestation pair *means*, not on how many files lack it. **The brief must not cite 27 as a general
  rate**, and the acceptance check must not be written as if it were.
  ⚠ **AMENDED — E3 forbade the only framing build-3 had and left a hole where the check was**
  *(roundtable A33, 2026-08-26; Mary)*. With both halves ruled out, what survives at rest for
  build-3 is: version strings bumped, 15 acks current, package-lint E1 bipartite-consistent,
  `contract:66` contains a pointer. **Every one is satisfied by build-3's own diff — they grade
  whether the edit was TYPED, never whether the narrowing WORKS**, and only E1 can fail at all.
  **So the cycle's largest and most irreversible build — 15 re-acks and a permanent coverage loss
  accepted knowingly at Q4 — would gate on bookkeeping.** The substance claim **is** gradeable at
  rest against a fixture. **What replaces the count:** build-3's brief names an **at-rest fixture
  PAIR** — a Layer-3 file bearing `author: agent`, no attestation pair, **of the operational-record
  class the amended §Scope rule exempts** (per A11's discriminator), **plus a control of the
  knowledge-artifact class that must still flag**. The gating check is that the first yields no
  finding **and the control does**. The 27 appear in the brief only as the observation that
  motivated the ruling — never as a rate, never as a check.

- **E4 — Cycle 13 carry-forward 3 has no population measurement.** See Q8: the measurement was to be
  Cycle 13 check (2), which FAILED. Retiring `malformed_frontmatter` without one is a behavioral
  removal on unmeasured grounds.
  → **RESOLVED by Q8 (Round 3).** *(roundtable A31, 2026-08-26 — Q8 is stamped Round 3.)* Build-1 carries an acceptance check that **produces** the
  measurement.
  ⚠ **AMENDED — PARTIALLY resolved; the debt is BOUND, not discharged** *(roundtable A19,
  2026-08-26; Mary, Amelia, Maya, John)*. E4's debt is *"retiring `malformed_frontmatter` without a
  measurement is a behavioral removal on unmeasured grounds"* — **and build-1 does not retire it.**
  Q8 defers the retirement a **third** time to a successor build §Grouping & order does not
  schedule. **A build that produces a datum does not discharge a debt owed by the build that acts on
  it.** So: build-1 carries a check that **could fail** (Q8 amendment 1), the measurement is a
  **specimen set** recorded with its corpus size and date in build-1's `status:`, and **the debt
  itself transfers, with the number attached, to the build that takes the retirement** — recorded at
  closeout as a Stage-2 carry-forward with a **named successor cycle** (`closeout-checklist.md:67`
  is the slot for a standing metric). **A bare count does not discharge E4.**

- **E5 — A14-6's own filing is stale against its vault.** Tracker #15 describes moving the
  `vlt-brief` shelf to a `{resources}` address as prospective; the shelf has been at
  `resources/briefs/` since before the 2026-08-26 10:46 lint, which enumerates all five issues in
  `para_type_unknown`. **The reported defect is unaffected** — the two conventions still disagree —
  but a brief quoting the filing's framing would assert a false premise about vault state.
  → **BLOCKING for build-3's brief (Round 4).** The brief writes A14-6 from **the capture's grounded
  text and the vault's current state**, never from tracker #15's prose. The shelf is at
  `resources/briefs/`, five issues, enumerated in `para_type_unknown` by the 2026-08-26 10:46 lint.
  **The reported defect is unaffected** — the two conventions still disagree — but a brief repeating
  the filing's prospective framing asserts a false premise in the one build whose subject is which
  convention tells the truth.
  ⚠ **AMENDED — vault-current state grounds the BRIEF; no vault path reaches the SHIPPED edit**
  *(roundtable A34, 2026-08-26; Paige)*. Build-3's deliverables are shipped governance
  (`write-verification.md`, `contract:66`), and **a class-based exemption is exactly the kind of
  rule that reaches for a worked instance — the only worked instance in front of the brief is a live
  vault's.** Per `CLAUDE.md`'s worked-examples rule (build-15/build-18 precedent), the shipped edit
  uses placeholders (`{resources}`, `{field-vault}`), never a specific install's artifact paths.

### Questions deliberately left to brief time

*Per-build, not cross-cutting. Ruled Round 4 (2026-08-26) — these are deliberately unresolved and
`build-brief` decides them with the source in front of it.*

- **build-1** — the exact shape of the structured claim return (an enum over disposition kinds plus
  a named-fields list, versus a discriminated union), and its cost against `PAGE_SCAN`'s size
  budget: `JSON.stringify(PAGE_SCAN).length ≤ 3700` is a **hard release gate** measured by
  package-lint Group E6 (`tools/package-lint.py:900`). ⚠ **`PAGE_SCAN` measures 3598 in the working
  tree at v0.16.1 — 102 characters of headroom, not the ~477 the old "3223 at Cycle 12's baseline"
  figure implied (3223 is the PRE-Cycle-12 value; Cycle 12 build-1 took it to 3598).** The ruled
  structured return costs ~218 with empty description strings (+54 if the two fields join
  `required:` at `:148`); deleting the `frontmatter_issue` property it replaces returns ~98. **Net:
  over budget before one word of description is written.** The brief must name the description bytes
  it retires to pay for it — Ruling 1 retires `:159` (208 chars) for exactly this — and must
  **re-measure with package-lint's own `_E6_NODE_EXTRACTOR`, never from a source char count.**
  Build-1 is released alone, so it has no sibling to absorb the trim.
  *(roundtable A1, 2026-08-26 — measured in session by four voices independently and re-run by the
  moderator.)*
  Also: how build-1's acceptance check measures the `malformed_frontmatter` population (Q8).
- **build-2** — whether the SKILL passes fingerprint components as a list or a pre-joined string,
  and what the round-trip check's fixture is. Also: the migration sentence — the existing sidecar
  cannot be migrated (no per-page digest), so the first run is cold by construction.
- **build-3** — the exact wording of `write-verification.md` §Scope rule's class-based exemption,
  and whether it cites `extraction.md:188` or restates the principle (single-home discipline says
  cite).
- **build-4** — whether the `sources_vs_prose` direction routing lives in `checks.md` or in
  `fix-and-file.md` Step 3, and whether `.json` becomes the default persist or an alternative.

## Carried forward past Cycle 14

*(roundtable A22, 2026-08-26; John, Winston. **Cycle 14 had no such section**, and its survivals
lived in five scattered places — a sub-bullet of §Grouping & order, Q2, Q8, a ⚠ inside Q3, and the
evidence-debt list. `cycle-closeout` Stage 2's collector would have had to reconstruct all of them
from prose: the exact condition `closeout-checklist.md:74` calls "silently dropped."*
**And the rail is worse than it looks:** `closeout-checklist.md:74-75` asserts *"the next cycle's
`inbox-capture` re-lists them … anything left off is silently dropped"* — while
`inbox-capture/SKILL.md:97-100` says reading a prior cycle's closed roadmap is *"useful … but
**never required**"*, and its New-cycle path ingests nothing from the predecessor. **The carry rail
is prose on the sending end and OPTIONAL on the receiving end.** Cycle 13's carries survived only
because a human read them across. **So Cycle 14 writes its deferrals down at ideation time rather
than leaving closeout to reconstruct them — and every one carries a BOUND**, on the Cycle-12-tails
precedent, because a deferral with no bound is what carried `malformed_frontmatter` to three cycles
and A4-4(5) to four.)*

1. **A14-2 — the outbound-link ENUMERATION.** Deferred by Q1. **Bound: Cycle 15's `inbox-capture`.**
   Its filing **stays in `factory/inbox/`** (A23). *Corrected premise it inherits (A-Ruling 3): the
   deferred faces need the page's **text**, not merely "page bytes" — a per-page **scalar** is not
   the #13 route.*
2. **Cycle 13 carry-forward 1 — the `summary` paraphrase.** Deferred by Q1. **Bound: Cycle 15's
   `inbox-capture`.** ⚠ **Carson's route, recorded so the successor does not re-derive the
   deferral:** `:545` consumes `s.summary` **only** as `.trim()` and `.length` — it never reads the
   string — so a SKILL-side `{slug: summary_len}` map on the `pageHashes` precedent (`:47`, `:99`)
   closes it for ~146 integers. Likewise a mechanical `[[…]]` **count** feeds the **already-shipped**
   `partialShortfall` response at `:371-377`, killing A14-2's false orphan at a few KB. *(Owner
   Ruling 3, 2026-08-26: not taken this cycle — build-1 is the release-1 critical path and already
   over its schema budget — but the premise is corrected and the routes are named.)*
3. **Cycle 13 carry-forward 2 — the general reduce-side posture.** Partially taken by Q1; **stays
   live for the deferred half.** Bound with items 1–2.
4. **Tracker #13 (the `argsPath` route).** Not re-admitted (Q2). ⚠ **Bound: Cycle 15's
   `inbox-capture`** — at that capture #13 is re-admitted by owner ruling **or the deferral is
   re-ruled with its reason on record.** *(Without a bound, §Owner ruling's admission test re-defers
   it as net-new at every future capture on identical grounds — the loop itself.)*
5. **The `malformed_frontmatter` RETIREMENT (Cycle 13 carry-forward 3).** Third deferral, Q8.
   **Successor: the build that takes carry-forward 2.** Carries build-1's **specimen set** (not a
   count) as a Stage-2 standing metric; **E4 transfers with it, BOUND not discharged** (A19).
6. **`para_author_unknown`** — still closed to `human|agent|hybrid`, no overlay escape, **and its
   owning convention likewise unnamed** — the same defect A14-6 repairs for `type:`. Untouched (Q3).
7. **E2 — A14-4's *"frontmatter is the source of truth"* qualifier.** Scoped out unmeasured;
   **owner files it to `factory/inbox/` as a `pattern`** (A32).
8. **Inherited from Cycle 12's never-delivered hand-off** (A25): **b3(7)** (re-read on release 2's
   acceptance run), **A12-4**, **A12-5's module side**, **A11-11 d4 + A12-1's cause-fix instrument**.
9. **The `:168` dissent** (Victor, Amelia) — `:168` survives only as long as `:664` does; **when
   `unmarked_supersession` is structured, the dissent becomes the ruling.**
10. **`{field-vault}` overlay staleness** — vault-side owner action, unchanged (§Also carried).


### CLOSEOUT ADDENDUM — the acceptance-time carries (2026-09-01, `cycle-closeout` Stage 2)

*(Items 1–10 above were written at ideation time, on the roundtable A22 lesson. These are what
**acceptance** produced across five discharge passes and four owner rulings — they did not exist when
that section was written. Cycle 15's `inbox-capture` re-lists **both** halves; the checklist's
`closeout-checklist.md:74` warning applies to this addendum equally: anything left off here is
silently dropped.)*

11. ⚠ **BOUND DEBT — build-3 (6), the two parked interims' unwind. FAILED, carried as inherited debt,
    tagged `[ship-verifiable]` so it GATES Cycle 15's closeout.** *(Owner-ruled at closeout
    2026-09-01.)*
    **The FAIL is not discharged, softened, or re-scoped.** All three clauses stand unmet as graded on
    pass 5 (park #15 live and un-superseded at rest; park #16 re-parked, not unwound, at vault
    `307c901`; `para_type_unknown`'s legal response unexecuted). **A green was reachable only by
    falsifying a `type:` field**, so the FAIL is the honest outcome of the `decision-log.md` v4
    mechanism working, not a process failure.
    **Why it is not fixed inside Cycle 14.** Build-6 would have given park #15 a legal response and was
    **withdrawn 2026-09-01** on the finding that it was a perimeter patch on **`ST-2`** (*location as
    proxy for trust*): its own minimal-scope ruling cut the `{wiki}` unification — the half that makes
    it a category — which is `ST-2` RC2 exactly. The two rules are now the subjects of the cycle's two
    `class: supersession` filings rather than of a patch.
    **The bound, stated so Cycle 15's closeout can grade it without re-deriving it:** Cycle 15 rules
    the two retirements at ideation (see item 13), and the re-check is graded on the **first
    `parked_interims_review` of the first `vlt-upgrade` after that release**, against
    `{field-vault}`'s `_agent/mint/decision-log.md` read at rest. **Clause (b) is already satisfied in
    substance and is not re-litigated** — park #16 was re-derived and superseded in the log; what it
    lacks is a *legal* exit, which is the retirement's to supply. **Clauses (a) and (c) are the bound.**
    ⚠ **A re-park is not an unwind, and a re-park at Cycle 15's bound does not discharge this** — that
    distinction is what produced this FAIL and it transfers with the debt.
    **Mechanism chosen deliberately**, on the same reasoning that carried build-1 (6) four days
    earlier: bound debt tagged ship-verifiable **so it gates** is the only mechanism in this loop's
    history that has ever retired an inherited debt rather than re-carrying it — **A4-4(5)** died after
    four arcs when B7-6 tagged it that way, **B8-2(4)** went green preemptively on that lesson,
    **B10-2(5)/B10-12(6)** retired on its bound at Cycle 11. A released watch would put this with the
    tails that have sat for five cycles.

12. ⚠ **BOUND DEBT — build-1 (6), the `malformed_frontmatter` specimen set (Q8/E4). FAILED on leg 3,
    carried as inherited debt, `[ship-verifiable]` so it GATES Cycle 15.** *(Owner-ruled 2026-08-31;
    re-listed here so closeout's collector carries both debts under one rule.)* **E4 transfers with
    `10 / 8 genuine / 2 refuted at 146 pages` — a 20% false-positive rate, NOT zero** — and the pass-3
    refresh strengthens that refusal: the specimen set is now known **not reproducible** (the two
    refuted specimens vanished on a corpus the report itself certifies unchanged), so the number is a
    **sample, not a measurement**. Proximate cause filed and small
    (`factory/inbox/2026-08-27-160000-summary-length-check-counts-the-raw-yaml-line.md`); the
    reproducibility problem is **upstream of the counting problem** and belongs to platform **[P-19]**.
    **Bound:** the repair ships in Cycle 15 and is graded on the **first full `vlt-lint --full` sweep
    after that release**, against a corpus whose identity is recorded at grading time; **leg 3 alone is
    the bound**, legs 1 and 2 are already met and are not re-litigated. ⚠ **If [P-19] has opened by
    then, this is one of the first checks that should declare which corpus it rests on — it is the
    check that proved the need.**

13. **The two retirements — `class: supersession` filings, P-15's rail's FIRST USE — to Cycle 15
    ideation's obsolescence beat.** `factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md`
    (the `extraction.md:84` PARA carve-out: an enumeration of one, and it *inverts* — punishing
    `{field-vault}` for using the module's own accurate word `research` where an invented synonym
    would be legal) and
    `factory/inbox/2026-09-01-170000-supersession-the-verified-by-roster-is-superseded-by-the-authorization-net.md`
    (`para_writer_unauthorized` at `checks.md:20` — *"the authorization question a location rule could
    never answer"*, whose identity list reads `verified_by:` → partner slug, a value
    `write-verification.md:47` makes **illegal**, so the net ships a leg no vault can exercise). Both
    supersede the earlier `2026-08-31-152000` filing, which is superseded and stays in the inbox for
    Cycle 15's capture to route. ⚠ **The roundtable's obsolescence beat has never been exercised** —
    this is the material it was built to receive. ⚠ **Read `_output/problem-solution-2026-08-25.md`
    before touching PARA zoning again.**
    ⚠ **OWED, NOT BLOCKING — an owner act:** neither supersession filing has been posted through
    `vlt-feedback`, so **park #16 references no live tracker issue** the way #15 and #16 do (the
    vault's entry says so explicitly). `vlt-feedback` is invoked-only and needs the owner's explicit
    go — deliberately not taken by any agent.

14. **Park #15's population is compounding, and the park's scope is the `type:` not the count.** It
    moved **5 → 8 → 9 in three days**. The ruling is unmoved by the number; the blast radius is not.
    Recorded as a **standing metric** (Stage 2 sense), re-read at Cycle 15's capture.

15. **Four workflow filings from pass 4, plus three strengthened to a THIRD consecutive sweep — all
    un-captured, all awaiting Cycle 15's `inbox-capture`.** New 2026-09-01: `…-093000` (the ruleset
    fingerprint is **over-broad** — `module_version` forces a cold sweep every release), `…-140600`
    (the fingerprint's inputs are **under-specified and a wrong reading is silent** — different cause,
    different fix from `093000`, **may be briefed with it**), `…-140601` (same-page heading anchors
    reported as missing targets), `…-140602` (a scanner **substituted a proper noun** —
    `cornerboxes` for `cornerbacks` — and on its second occurrence was **served from the cache**, so a
    scanner error is now **permanent for the sidecar's life** and re-running cannot re-derive it).
    `…-104500` stands **corrected**: the rendered report is *intermittently* wrong, a stronger claim
    than consistently wrong.

16. **Platform-side signals recorded, none owed a module filing.** **[P-20]** (the check adversary)
    gained instances **#4 and #5** from this cycle — build-5 (6)'s false premise, caught **in real
    time rather than reconstructed after the escape**, and build-5 (5) discharged while structurally
    unable to fail. **[P-19]** (the acceptance corpus) gained its **first field instance** — build-1
    (6)'s specimen set returning two different answers on the same bytes three days apart. Both items
    are open on `factory/platform/roadmap.md` and neither is Cycle 15 build scope.

17. **`full-scale.md` step 2's under-specified component slots — the caveat behind the cache's first
    warm run.** Filed as `…-140600` (item 15) and re-stated here because of what it costs: a vault
    following the shipped doc gets a **permanently cold cache and a report that says nothing is
    wrong**. It is the most likely explanation for the three-cycle failure build-2's check was written
    to end, and it survived the very run that proved the cache works.

## Deferred acceptance ledger

*Per-build `- [ ] **build-N (<slug>, briefed <date>):** …` bullets, appended by `build-brief`; form
per `factory/cycles/13-trusted-returns/roadmap.md` §Deferred acceptance ledger. Created 2026-08-26
with build-1's append — the section did not exist, and every brief in this cycle gates against it.
**Cycle ruling D3 as amended (roundtable A17) governs every bullet: BOUNDED ⇒ ship-verifiable ⇒ it
GATES**; per rule **R1** each ship-verifiable check names which seam its instrument crosses.
Also to be recorded here by build-3's brief: **Cycle 12's b3(7)**, inherited unread and landing on
release 2's acceptance run (roundtable A25).*

### Acceptance-discharge run — 2026-08-27

**Evidence sources** (all read-only; `{field-vault}` was never written):
`{upgrade_reports}/2026-08-27-0947-upgrade.yaml` (0.16.1 → **0.16.2**, release 1 — clean: every
divergence axis `[]`, 7 mints preserved, `governance_rule_changes: []`, correct because no
convention moved at 0.16.2); `{lint_reports}/2026-08-27-1104-lint.yaml` (**the first full sweep
after release 1** — 146 checked, 146 cold, the bound event for build-1's (6) and (7));
`{upgrade_reports}/2026-08-27-1157-upgrade.yaml` (0.16.2 → **0.17.0**, release 2 — the bound event
for build-3's (6)); the two release commits `bd985a6` and `c02fe3d` for the release-gate checks; and
shipped source at `c02fe3d` for the at-rest re-reads.

⚠ **NO full sweep has been run after release 2 — deliberately deferred by the owner.** Every check
bound to it is graded **STILL-OPEN awaiting its named event**, never failed, and no evidence for it
was invented.

**Tally across 30 checks in 5 items: 23 DISCHARGED · 2 FAILED · 4 STILL-OPEN · 1 SPLIT · 0 BLOCKED.**
**Gating (ship-verifiable) checks: 28 of the 30 — 23 discharged, 2 failed, 2 still-open, 1 split.**
The 2 non-gating checks are the two `[field-contingent]` ones (build-2 (8) and the inherited
Cycle 12 b3(7)), both STILL-OPEN.
**All five ledger items remain UNCHECKED. NO filing is archived this run** — a filing archives only
when *all* its ledger items are DISCHARGED, and none is.

| item | verdict | outstanding |
|---|---|---|
| build-1 | 7/8 DISCHARGED, **(6) FAILED** | (6) — the `malformed_frontmatter` bound fails leg 3: 2 of 10 specimens refuted |
| build-2 | 7/8 DISCHARGED, **all gating checks discharged** | (8) `[field-contingent]` — awaits two consecutive post-0.17.0 sweeps |
| build-3 | 4 DISCHARGED + **(4) discharged-with-caveat**, **(6) SPLIT**, (7) STILL-OPEN | (6) both parks' unwind; (7) the first post-release-2 sweep |
| build-4 | 4/6 DISCHARGED, **(1) FAILED (kept)**, (6) STILL-OPEN | (1) the unparseable archived report; (6) the first post-release-2 sweep |
| INHERITED Cycle 12 b3(7) | STILL-OPEN `[field-contingent]` | an observed `{resources}`-write partner session |

**Three filings already on disk carry every FAILED/contradicted finding — no new filing was drafted
and none is owed:** `2026-08-27-153000` (build-4 (1)), `2026-08-27-160000` (build-1 (6)),
`2026-08-27-171000` (the membership defect that build-3's (4) structurally could not see). Two
further sweep filings (`160100` orphan false positive, `160200` `governance_memory` denominator) are
**Cycle 15 material, not Cycle 14 ledger items** — neither is named by any check here.

**Distance from closeout: two owner acts.** (i) Run `vlt-lint --full` on `{field-vault}` under
0.17.0 — one sweep discharges build-3 (7) and build-4 (6), and a **second** sweep with no ruleset
change between discharges build-2 (8). (ii) Work the two parks' unwind (build-3 (6)). Then
`cycle-closeout` must rule on the **two standing FAILs** — build-1 (6) and build-4 (1) — both of
which GATE. **Cycle 14 cannot close today.**

### Acceptance-discharge run — 2026-08-27, PASS 2 (post-hot-fix)

*Second discharge pass, run after `{field-vault}` took **both** remaining upgrades on the
own-the-apply path — 0.16.2 → **0.17.0** and then the 0.17.0 → **0.17.1** hot-fix. Scope: the items
that became **gradeable** since pass 1 (`c08a5ab`). **Pass 1's verdicts are not re-graded** — no new
evidence overturns any of them, and where a number moved the annotation is marked an evidence
refresh, not a re-grade.*

**New evidence source** (read-only; `{field-vault}` was never written):
`{upgrade_reports}/2026-08-27-1328-upgrade.yaml` (0.17.0 → **0.17.1**), plus the release commit
`56cde45` and shipped source at HEAD for the at-rest re-verifications. **The 0.17.1 run is clean on
every durability axis**, verified against the report itself rather than taken on relay: 7 local mints
preserved, `bodies_restored: []`, **2 overlays intact** (`frontmatter.overlay.md`,
`vault-operating-contract.overlay.md`), `base_divergence: []`, `skill_asset_divergence: []`,
`manifest_write_divergence: []`, `governance_divergence: []`, `vault_writable_collisions: []`,
`machine_tools_missing: []`, `family_invariant_drift: []`.

⚠ **STILL NO FULL SWEEP SINCE ANY OF THE THREE RELEASES — deliberately deferred by the owner.**
`{lint_reports}` ends at `2026-08-27-1104-lint.yaml`, taken under **0.16.2**. Every check bound to a
post-release-2 sweep therefore stays **STILL-OPEN awaiting its named event**, never failed, and no
sweep evidence was invented. **Three forced cold sweeps are outstanding.**

**Graded this pass: 6 checks (all of build-5's, whose ledger pass 1 predates).
4 DISCHARGED · 1 FAILED · 1 STILL-OPEN.** Build-5's checks (1)–(4) are individually checkboxed, so
**four boxes are ticked this run — the first ticks in the cycle.** Builds 1–4 and the inherited
Cycle 12 b3(7) each remain **one unchecked bundled item**, unchanged.

| item | pass-2 action | outstanding |
|---|---|---|
| build-5 (1)(2)(3)(4) | **DISCHARGED + TICKED**, each re-verified at rest by this run | — |
| build-5 (5) | **STILL-OPEN** — predicted number met, by an instrument the check does not name | one `vlt-lint --full` under 0.17.1 |
| build-5 (6) | **FAILED** `[field-contingent, does NOT gate]` — the park was **re-surfaced, not unparked**; ⚠ **false premise**, routed to [P-20] | nothing new — the park tail is already build-3 (6) (b) |
| build-3 (6) | evidence refresh only, **grade unchanged** | 28 → **27** in jurisdiction; both parks still live and unruled |
| build-3 (7) · build-4 (6) · build-2 (8) · Cycle 12 b3(7) | **untouched — STILL-OPEN on their named events** | the deferred sweeps; the observed `{resources}`-write session |

**Cumulative across both passes: 36 checks in 6 items — 27 DISCHARGED · 3 FAILED · 5 STILL-OPEN ·
1 SPLIT · 0 BLOCKED.** The two **gating** FAILs are unchanged and unmoved: **build-1 (6)** and
**build-4 (1)**. Build-5 (6) is the third FAIL and is `[field-contingent]`, so it **does not gate**
and does not extend the closeout distance.

**Corroboration recorded but grading nothing — the skill-asset manifest.** The 0.17.0 run moved the
net **67 → 68** (`added: ["…lint-cache.py"]`, `removed: []`) and 0.17.1 held it **steady at 68**
(`previous_entries: 68`, all four partitions empty) — *"no path left the net"* both runs. This is the
field confirmation that build-2's new shipped script reached a vault's manifest by the structural
`rglob`, which is build-2's **verification step V6**, not an acceptance check: **no ledger item in
this cycle names the manifest**, so this datum discharges nothing and is logged so a future reader
does not mistake it for an ungraded item.

**No inbox filing drafted this pass.** The one FAILED check's signal is **factory-side** (a
mis-written check, not a module defect) and routes to the platform ledger's **[P-20]**, where it is
recorded as that item's fourth instance — reasoning in full at build-5 (6)'s annotation.

**Distance from closeout — narrowed by ZERO owner acts, but ONE act now buys more.**
(i) **One** `vlt-lint --full` on `{field-vault}` under **0.17.1** now discharges **three** checks —
build-3 (7), build-4 (6) **and** build-5 (5) — where before it bought two; a **second** sweep with no
ruleset change between still discharges build-2 (8). (ii) The two parks' unwind (build-3 (6)),
unchanged and still the human's call. Then `cycle-closeout` must rule the **two standing gating
FAILs**. **Cycle 14 still cannot close.**

### Acceptance-discharge run — 2026-08-31, PASS 3 (the first full sweep under 0.17.1)

*Third discharge pass, run after `{field-vault}` took its **first full `vlt-lint --full` sweep since
any of the cycle's three releases** — the sweep passes 1 and 2 both recorded as deliberately deferred
and priced as an outstanding cold run. Scope: the four checks bound to that sweep, plus the one
inherited tail whose third-run tripwire came due. **Passes 1 and 2's verdicts are not re-graded**;
where new evidence bears on a standing verdict it is recorded as an evidence refresh and the grade is
stated unchanged.*

**New evidence source** (read-only; `{field-vault}` was never written):
`{lint_reports}/2026-08-30-1123-lint.yaml` — `mode: full`, `scope_since: full`, **146 checked / 0
cached / 146 listed**, taken against `{field-vault}` at `module_version: 0.17.1`
(`.claude/skills/vlt-setup/assets/module.yaml:4`). Cold by construction and correctly so: 0.17.1
moved two convention digests. Corroborating vault reads at rest: `_agent/lint-cache.json`,
`projects/fantasy-2026/{charter,record}.md`, `_agent/sessions/` 2026-08-28..2026-08-30,
`resources/` mtimes since the upgrade. Baseline for every delta:
`{lint_reports}/2026-08-27-1104-lint.yaml`, taken under **0.16.2**.

⚠ **The corpus did not move between the two sweeps.** The report certifies it:
`churn_since_last_full: '0 of 146 pages changed since 2026-08-27 … The wiki did not move between the
two sweeps — every wiki-side delta below is scanner variance on an identical corpus, not vault
change'`. That certification is load-bearing twice below.

**Graded this pass: 5 checks. 2 DISCHARGED · 2 BLOCKED · 1 STILL-OPEN**, plus one evidence refresh
that leaves its grade unchanged. **One box is ticked** (build-5 (5)); builds 1–4 and the inherited
Cycle 12 b3(7) each remain one unchecked bundled item.

| item | pass-3 action | outstanding |
|---|---|---|
| build-4 (6) | **DISCHARGED** — 0% application rate cured, 5 of 10 applied, in the routed direction | ⚠ caveat: the report omits `fixes_applied:` entirely (filed) |
| build-5 (5) | **DISCHARGED + TICKED** — 27 measured on the named instrument, charter out | ⚠ caveat: the *transition* is unobservable on this instrument (P-20 #5) |
| build-3 (7) | **BLOCKED (unreachable)** — owner-ruled; the named observable is produced by no shipped surface | routes to `inbox-capture`; **GATES** |
| INHERITED Cycle 12 b3(7) | **BLOCKED (unreachable)** — owner-ruled; pass 1's own third-run instruction came due | routes to `inbox-capture`; does NOT gate |
| build-2 (8) | **STILL-OPEN** — this is sweep **1 of 2**; the write leg is now field-confirmed | one second consecutive sweep, no release between |
| build-1 (6) | evidence refresh, **grade unchanged (FAILED, GATES)** | the specimen set proved **not reproducible** — P-19 evidence |

**Cumulative across three passes: 36 checks in 6 items — 29 DISCHARGED · 3 FAILED · 1 STILL-OPEN ·
1 SPLIT · 2 BLOCKED.**

**The gating picture changed, and not for the better.** Two gating FAILs stand unmoved (build-1 (6),
build-4 (1)) and **build-3 (7) joins them as a gating BLOCKED** — so `cycle-closeout` must now rule
**three** gating items, not two, plus build-3 (6)'s SPLIT (the two parks' unwind). The sweep bought
two discharges and cost one blocker; that is the honest net.

**Three filings drafted and filed this run**, all owner-confirmed:
- `factory/inbox/2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md`
  — three instances, one root cause: `para_missing_attestation` rendered as a rollup where
  `report.md:32` mandates a per-file list; `fixes_applied:` omitted though `:72` mandates it and five
  fixes were applied; `backlog_filed:` omitted though a real instrument defect was found. **This is
  the filing that build-3 (7)'s BLOCKED rests on**, and it is Cycle 14's own through-line arriving
  inside Cycle 14's own instrument: a shape stated in one file and enforced in none.
- `factory/inbox/2026-08-31-104501-stub-discovery-regex-drops-the-stub-list-and-manufactures-missing-targets.md`
  — the SKILL builds `stubSlugs` with a regex requiring a bare `## Stubs` heading; `{field-vault}`'s
  index reads `## Stubs (linked, not yet written)`, so an **empty** stub list reached the workflow and
  three registered stubs were reported as missing targets. Caught and refused by the run, but only by
  reading every entry against the index. ⚠ **Capture must ground the exact `file:line`** — this rests
  on the sweep's own diagnosis plus the observable outcome, not on a located site.
- `factory/inbox/2026-08-31-104502-resources-write-legality-check-has-no-cause-and-survived-three-runs.md`
  — the inherited tail's BLOCKED, filed as **factory-side** signal about how acceptance checks are
  written. A check dischargeable only by staging its own evidence has a trigger but **no cause**;
  the brief vocabulary has no word for that species today. Cousin of platform **[P-20]**.

**Two platform-side signals recorded, neither owed a module filing:**
- **[P-20] instance #5** — build-5 (5) passed while structurally unable to fail. Detail at its
  annotation.
- **[P-19] (the acceptance corpus)** — build-1 (6)'s specimen set is **not reproducible**. Detail at
  its refresh below.

**Distance from closeout — one act shorter on the tails, one item longer on the gate.**
(i) A **second** `vlt-lint --full` on `{field-vault}` with **no release, overlay edit or convention
change between** discharges build-2 (8) `[non-gating]`. ⚠ Take it **before** any release: the
stubSlugs repair the sweep asks for is factory-side and reaches the vault only through a release,
and a release moves the ruleset fingerprint and forfeits the warm sweep. (ii) The two parks' unwind
(build-3 (6)), unchanged and still the human's call. (iii) **New:** build-3 (7)'s BLOCKED needs
either a module repair routed through `inbox-capture` (which would give the check a real trigger and
let a future run grade it honestly) or an owner ruling at closeout. Then `cycle-closeout` rules the
three gating items. **Cycle 14 still cannot close.**


### Owner rulings — 2026-08-31, recorded after discharge pass 3

*Three rulings taken on the pass-3 evidence, recorded here and annotated per item below. They clear
the gate; they retire no filing. Every filing named in pass 3 routes to `inbox-capture` unchanged.*

| item | was | now | rests on |
|---|---|---|---|
| **build-4 (1)** | FAILED, gates | **DISCHARGED** on the forward subject | new measurement **+ a contested reading** — see the ⚠ tension at its annotation |
| **build-3 (7)** | BLOCKED, gates | **DISCHARGED with caveat** | an owner-ruled instrument substitution, narrow and reasoned |
| **build-1 (6)** | FAILED, gates | **FAILED — carried as BOUND DEBT to Cycle 15, ship-verifiable so it GATES there** | the A4-4(5) / B8-2(4) / B10-2(5) mechanism |

**Tally after the rulings: 36 checks in 6 items — 31 DISCHARGED · 2 FAILED · 1 STILL-OPEN · 1 SPLIT ·
1 BLOCKED.**
*(Pass 3 as first written mis-added its STILL-OPEN column as 2; it was 1 — build-2 (8) alone, pass 2's
five tails minus the four pass 3 moved. Verdicts unaffected; corrected throughout.)*

**build-4 is TICKED — 6/6, the first bundled item in this cycle to complete.** Its two filings
(`2026-08-26-123144`, `2026-08-26-123153`) are archive-eligible and were **deliberately not moved**;
see the note at the item. Builds 1, 2, 3 and the inherited Cycle 12 b3(7) stay unchecked.

**⚠ Cycle 14 now has exactly ONE gating blocker: build-3 (6), the two parks' unwind.** Everything
else that gated is ruled. The remaining FAIL (build-1 (6)) gates **Cycle 15**, not this one;
build-5 (6) and the inherited Cycle 12 b3(7) are `[field-contingent]` and never gated; build-2 (8)
is `[field-contingent]` and open on a live trigger.

**The parks, restated once so closeout needs no re-derivation:**
- **(a) `extraction.md`** — blocker RESOLVED; 5 files under `resources/briefs/**` across 3
  subscriptions. Needs a superseding decision-log entry through the rostered write route **plus**
  the vault executing `para_type_unknown`'s stated legal response (retype or relocate) on at least
  one named file. Both are owner acts in `{field-vault}`, available today.
- **(b) `write-verification.md`** — 27 files in jurisdiction. ⚠ The blocker is the **refused
  partner-sitting reading and the unchanged `verified_by` roster**, **NOT** the charter-membership
  contradiction, which v0.17.1 already fixed — a premise correction already on record at build-5 (6)
  and [P-20]'s fourth instance. Widening the roster is a Cycle 15 build. **"Keep the hold, with a
  stated exit condition" is a legal disposition**, not an evasion: the check asks for the park's
  disposition, and a deliberate ruling to hold discharges it as honestly as an unwind.

**What the rulings deliberately did NOT do.** No filing was withdrawn, no check was rewritten, and
no defect was ruled away. Three of the four filings on the board
(`2026-08-27-153000`, `2026-08-27-160000`, `2026-08-31-104500`) are the diagnoses *underneath* the
items just discharged or carried, and all three go to capture live. **The gate moved; the module
did not.**

- [ ] **build-1 (structured-claim-return, briefed 2026-08-26):** brief
  `factory/cycles/14-no-enforcement-point/briefs/build-1-structured-claim-return.md`. **Eight checks
  — all `[ship-verifiable]`, all GATE; none field-contingent.** Release 1, cut alone; ⚠ **the first
  full lint after it is COLD by construction** (`scanFingerprint` moves — `:232-233`), never a cache
  regression.
  **(1) `[ship-verifiable]` — at rest — GATES:** the defeat mechanism is gone and the escape reports
  — over the V1 harness against shipped source, the attestation-only case is refused **whether or not
  `_detail` carries the 2026-08-26 rule-citing text**, the invented-requirement case is dropped, and
  all five controls survive (genuine break, compound break, `unclassified`, `malformed_block`,
  genuine unmarked supersession) — instrument: the V1 harness, stubbed
  `agent`/`parallel`/`phase`/`log`/`budget`, `args` as a JSON string, factory-side at rest;
  seam: **scan → reduce**; evidence: the four arrays verbatim in the BUILT `status:`.
  **(2) `[ship-verifiable]` — at rest — GATES: ⚠ THIS RE-GRADES CYCLE 13's ACCEPTANCE CHECK (2)**
  (roundtable A21) — the six subjects of `13-trusted-returns/roadmap.md:468-477`, re-scanned with the
  **post-build** `PAGE_SCAN` and prompt and run through the shipped rewritten reduce, reach **neither**
  `malformed_frontmatter` nor `unmarked_supersessions`, while `unattested_write` /
  `attestation_census` still carry them — instrument: a single-agent reader probe over **read-only
  copies of those six pages** from `{field-vault}` (never written) plus the shipped reduce, at rest;
  seam: **page bytes → scanner → reduce**, end-to-end, the only check here that crosses the agent;
  **binding, carried verbatim from Cycle 13's (2): a fixture built to exercise only the surfaces this
  build changes does NOT satisfy this check**; evidence: returned JSON + post-reduce arrays verbatim.
  **Without this check release 1 could ship and Cycle 13 still not close.**
  **(3) `[ship-verifiable]` — at rest — GATES:** the retirement landed whole and the survivors live —
  `grep -n "parseClaim\|fieldsNamed\|KNOWN_FRONTMATTER\|normalizeClaim\|claimWords\|CLAIM_FILLER\|frontmatter_issue\|frontmatter_valid" skills/`
  returns **zero**; the three surviving constant sets are **referenced from the rewritten predicates**,
  not merely defined; `node --check` parses; `:168` and `:550-557` byte-identical to v0.16.1 —
  instrument: the V3 greps + `node --check`; seam: **source agreement across the shipped tree** (named
  as such, not dressed as behavioural); evidence: grep outputs verbatim.
  **(4) `[ship-verifiable]` — at the release gate — GATES:** `JSON.stringify(PAGE_SCAN).length ≤ 3700`
  re-measured by **package-lint's own `_E6_NODE_EXTRACTOR`** (never a source char count; baseline
  3598, ruled shape 3688), and `uv run tools/package-lint.py --expect-version X.Y.Z` exits **0** with
  both version strings bumped — instrument: package-lint Groups E and D; seam: **source literal →
  runtime serialization**; evidence: the measured length + the PASS summary line in the release commit.
  **(5) `[ship-verifiable]` — at rest — GATES:** the category seam is closed on **both** sides and no
  looser — page-side and index-side `&amp;` forms each produce no `category_no_match`, numeric refs
  decode, and all three controls still flag (different category, case difference, leading space; D5
  — strictness not softened) — instrument: the V2 fixture against the shipped reduce; seam: **index
  scanner → reduce** and **page scanner → reduce**; evidence: the six `category_no_match` arrays.
  **(6) `[ship-verifiable]` — bounded to the first full `{field-vault}` sweep after release 1 —
  GATES:** the Q8/E4 `malformed_frontmatter` measurement, **as a specimen set with a bound it can
  fail** — **zero** post-repair specimens are attestation-only complaints, **zero** are
  claimed-missing documented-optional fields, and **every** remaining specimen is adjudicated one by
  one against its page as a genuine schema break (the cardinality is recorded, and is **not** the
  check); deliverable: slug + **minimal triggering fragment** per page, with corpus size and date,
  materialized under `factory/cycles/14-no-enforcement-point/` and summarized in the BUILT `status:`
  — instruments, **two and different** (A19): the persisted `{lint_reports}` archive for the
  pre-change baseline (no new sweep needed), and a **live** full sweep post-change (this build changes
  the return's shape, so pre-change recorded returns are free text the new schema cannot emit, and no
  wiki corpus ships in this repo); seam: **live page corpus → scanner → reduce** at 146-page scale;
  event: the owner runs `vlt-lint --full` on `{field-vault}` after upgrading to release 1;
  performer: the owner; vault: `{field-vault}` only. ⚠ **E4 is BOUND by this check, not discharged**
  — the debt transfers with the number to the build that takes the retirement (§Carried forward 5).
  **(7) `[ship-verifiable]` — bounded to the same sweep as (6) — GATES:** the `:664` retirement's
  exposure, measured not assumed — **no** `unmarked_supersessions` entry in that sweep is an
  attestation-only complaint and `fixes_applied:` records **no** hand-fold of a misrouted attestation
  entry, against a baseline where all three entries of the 2026-08-26 sweep were false and one was
  exactly this — instrument: the same live sweep read against the `{lint_reports}` archive baseline;
  seam: **prompt instruction (`:168`) → scanner return → reduce**, the one seam this build knowingly
  leaves with no reduce-side enforcement point; event/performer/vault: as (6). **If it fails, the
  `:168` dissent (Victor, Amelia) becomes the ruling and `unmarked_supersession` is structured by the
  successor build — this number exists to make that decision** (§Carried forward 9).
  **(8) `[ship-verifiable]` — at rest — GATES:** the vault-facing catalogue no longer asserts the
  refuted claim — `checks.md:15` carries **no** conjunction/residue prose and **no** over-reporting
  *guarantee*, describes the structured verdict and its two exclusions, states that an `unclassified`
  defect always reports, and keeps the class's legal response (R3); `checks.md:14` states the
  entity-decoded, still-exact category binding; `grep -rn "residue\|Both exclusions are conjunctions"
  skills/` returns **zero** — instrument: the V3 greps + a read of the two lines, at rest; seam:
  **module source → vault-read documentation**; evidence: grep output + the two rewritten lines.
  **— ACCEPTANCE DISCHARGE 2026-08-27 — 7 of 8 DISCHARGED, (6) FAILED; the item stays UNCHECKED.**
  **(1)(2)(3)(5)(8) DISCHARGED at rest** — recorded 6/6 PASS in the brief's BUILT `status:`,
  including **(2), which re-graded Cycle 13's refuted acceptance check on its six named subjects and
  PASSED — Cycle 13's closeout gate is reopened on this evidence**. **(4) DISCHARGED at the release
  gate** — `package-lint: A/B/C/E PASS, D PASS — vlt 0.16.2 (… --expect-version 0.16.2, exit 0)`,
  release commit `bd985a6`.
  **(7) DISCHARGED** — bound event occurred: the first full `{field-vault}` sweep after release 1,
  `{lint_reports}/2026-08-27-1104-lint.yaml` (146 checked, `lint_cache: cold`, cold by construction
  per the ⚠ above). `unmarked_supersessions` reached **zero entries** — no entry, therefore no
  attestation-only complaint — against a baseline where the 2026-08-26 sweep returned **3, all
  three refuted, one of them exactly this misroute** (`2026-08-26-1046-lint.yaml:150`:
  *"costa-rican-village-dog is an attestation-only complaint that the v0.16.1 build-1 guard exists
  to refuse — it leaked because the scanner quoted the rule text"*). `fixes_applied:` records three
  entries, **none** a hand-fold of a misrouted attestation entry, and `instrument_findings` carries
  **no** `unmarked_supersessions` refutation this run. **The `:168` dissent (Victor, Amelia) does
  NOT become the ruling** — this number existed to make that decision and it decided against
  structuring `unmarked_supersession` in the successor build (§Carried forward 9).
  **(6) FAILED — the bound fails on its third leg.** Same sweep. Population: **10 flagged, 8
  genuine, 2 refuted** (`2026-08-27-1104-lint.yaml:259` + `flag_for_human.malformed_frontmatter`).
  Legs 1 and 2 are **MET and emphatically so** — **zero** attestation-only complaints and **zero**
  claimed-missing documented-optional fields, against a baseline of 18/18, 5+1 of 7 and 1+1 of 3
  across the three archived pre-change sweeps. Leg 3 — *every remaining specimen is a genuine schema
  break* — is **NOT met**: `barbacoa` (*"summary exceeds 160 characters (171)"*) and `l-theanine`
  (*"(161)"*) are refuted, the parsed scalars being under the limit while the scanner counted the
  raw YAML line including its quoting. **The escape is a different mechanism than the one build-1
  closed** — a scanner-side measurement bug, not a rule-citing scanner defeating a reduce-side
  conjunction — so it is not a refutation of the repair, but the check was written to be failable on
  exactly this and it fails. Filed 2026-08-27 as
  `factory/inbox/2026-08-27-160000-summary-length-check-counts-the-raw-yaml-line.md` (drafted at the
  sweep, confirmed by this run — no second filing owed). Specimen set materialized: **Half 2 of
  `malformed-frontmatter-specimens.md` is FILLED** with all 10 slugs, fragments, corpus size 146 and
  the sweep date, plus the honest resolution limit (the 8 genuine were repaired in the same run, so
  per-slug minimal fragments are not re-derivable — the same cap the 2026-08-24 baseline hit).
  ⚠ **E4 transfers to the retirement build with the number `10 / 8 genuine / 2 refuted at 146
  pages` — a 20% false-positive rate, NOT zero** (§Carried forward 5).
  **⚠ EVIDENCE REFRESH 2026-08-31 (discharge pass 3) — the grade is UNCHANGED (still FAILED, still
  GATES). The new sweep does not retire the FAIL, and what it does show is worse than the FAIL.**
  `{lint_reports}/2026-08-30-1123-lint.yaml` reports **`malformed_frontmatter: []`** — an empty
  population where the bound sweep three days earlier reported 10.
  **Why zero does not discharge it.** The 8 genuine specimens were **repaired inside the 2026-08-27
  sweep itself** (`fix_now.frontmatter_drift`: *"…the stray lines removed … all 146 pages parse
  now"*). An empty list on a repaired corpus is the expected reading, not a re-run of the failed
  check: the check's bound sweep has already happened and already failed, and a specimen-set check is
  not retired by later finding no specimens.
  ⚠ **What the sweep actually establishes: the specimen set is NOT REPRODUCIBLE.** The two **refuted**
  specimens — `barbacoa` and `l-theanine`, the raw-YAML-line summary-length artefact that is the whole
  of leg 3's failure — **did not reappear**. Nothing repaired them: filing `2026-08-27-160000` is
  still un-captured, no build has touched the scanner, and the report certifies the corpus did not
  move (`churn_since_last_full: '0 of 146 pages changed since 2026-08-27 … every wiki-side delta below
  is scanner variance on an identical corpus, not vault change'`). **Identical corpus, identical
  instrument, two specimens present and then absent.** The same run supplies a second instance in a
  different slot: the scanner returned the slug `cornerboxes` for a link that reads
  `…espn-top-10-cornerBACKS-2026`.
  **Consequences, stated so neither is lost.** (i) The FAIL stands and still **GATES**; `cycle-closeout`
  must rule it. (ii) **E4 still transfers with `10 / 8 genuine / 2 refuted at 146 pages`, not zero** —
  and that number is now known to be a *sample*, not a measurement, which strengthens rather than
  weakens the refusal to transfer zero. (iii) An owner **may** argue at closeout that the corpus is
  now clean; this run does not make that argument, because a number that changes without a cause is
  not evidence in either direction.
  **Routed to platform [P-19] (the acceptance corpus)** as its first field instance: a check graded
  against a live corpus produced two different answers on the same bytes three days apart, which is
  exactly the reproducibility P-19 was opened for — and its cause is reproducibility, not cost, as
  P-19's scope already insists. **No new inbox filing owed** — `2026-08-27-160000` covers the
  measurement bug and the reproducibility signal is factory-side.
  **⚠ RULED 2026-08-31 — the FAIL STANDS and is carried as BOUND DEBT to Cycle 15, ship-verifiable
  so it GATES there. OWNER-RULED. It is no longer a Cycle 14 closeout blocker; it is Cycle 15's
  gate.**
  **The FAIL is not discharged, softened, or re-scoped.** Leg 3 failed on its bound sweep and stays
  failed: 10 flagged / 8 genuine / **2 refuted**. **E4 transfers with `10 / 8 genuine / 2 refuted at
  146 pages` — a 20% false-positive rate, NOT zero** (§Carried forward 5), and the pass-3 refresh
  makes that refusal stronger rather than weaker: the specimen set is now known **not reproducible**,
  so the number is a *sample*, not a measurement.
  **Why it is not fixed inside Cycle 14.** The proximate cause is filed and small — the scanner
  counts the raw YAML line instead of the parsed scalar
  (`factory/inbox/2026-08-27-160000-summary-length-check-counts-the-raw-yaml-line.md`). Fixing the
  counter would remove the two refutations **and still not yield a gradeable check**, because the
  2026-08-30 sweep showed those same two specimens vanishing on a corpus the report itself certifies
  unchanged, with no build having touched the scanner. A hot-fix here would buy a
  differently-unreliable instrument, not a re-grade. **The reproducibility problem is upstream of the
  counting problem**, and it is [P-19]'s, not a build's.
  **The mechanism, chosen deliberately.** Bound debt tagged **ship-verifiable so it GATES** is the
  only mechanism in this loop's history that has ever actually retired an inherited debt rather than
  re-carrying it: **A4-4(5)** died after four arcs when B7-6 tagged it ship-verifiable (amendment A3
  was the mechanism); **B8-2(4)** was tagged that way *preemptively* on the A4-4(5) lesson and went
  GREEN on its bound at Cycle 9; **B10-2(5)/B10-12(6)** retired on its bound at Cycle 11 after three
  cycles. Every debt this loop has killed died on a bound that gated. A released watch would put this
  on the register with the tails that have sat for five cycles.
  **The bound, stated so Cycle 15's closeout can grade it without re-deriving it:** the repair ships
  in Cycle 15 and its re-check is graded on the **first full `vlt-lint --full` sweep after that
  release**, against a corpus whose identity is recorded at grading time. Legs 1 and 2 are already
  MET and emphatically so and are not re-litigated; **leg 3 alone is the bound** — every remaining
  specimen adjudicated a genuine schema break, with the cardinality recorded and explicitly not the
  check. ⚠ **If [P-19] (the acceptance corpus) has opened by then, this check is one of the first
  that should declare which corpus it rests on** — it is the check that proved the need.

- [x] **build-2 (findings-cache, briefed 2026-08-27):** brief
  `factory/cycles/14-no-enforcement-point/briefs/build-2-findings-cache.md`. **Eight checks — seven
  `[ship-verifiable]`, all GATE; one `[field-contingent]`, which does NOT.** Release 2 (with builds
  3 and 4); ⚠ **the first full lint after release 2 is COLD by construction** (build-2 rewrites the
  record shape *and* the sidecar's filename; builds 3/4 move convention and `checks.md` digests) —
  **release 1 already forced one cold sweep, so this cycle knowingly costs two (A26)**, and
  `{field-vault}` pays its owed COMPLETE sweep on the **second** sweep after release 2.
  **(1) `[ship-verifiable]` — at rest — GATES:** the sidecar round-trips over **three** runs with a
  **real writer** — cold → warm → warm; run 2 is `files_checked: 0` / `files_cached: N` /
  `cache_rejected: 0`, and run 3 is **identical to run 2** (same N, same per-record `key`, same
  `scan` payloads). The third run is the check (A5(a)): a two-run fixture cannot observe reused-half
  loss — if run 2 dropped the reused records the sidecar would empty and a two-run check would still
  pass — instrument: `factory/cycles/14-no-enforcement-point/lint-cache-roundtrip.mjs` over the
  **shipped** workflow source **and the shipped `skills/vlt-lint/scripts/lint-cache.py`**, temp vault
  dir, `args` as a JSON string, only the page-scanner agents stubbed; seam: **workflow return →
  serialize (shipped script) → file on disk → parse (shipped script) → workflow consume** — the exact
  seam b2(5)'s harness stubbed and the only seam that has ever broken; evidence: the three returns
  and both sidecar files verbatim.
  **(2) `[ship-verifiable]` — at rest — GATES:** a record keyed under a **different `PAGE_SCAN` is
  NOT reusable** (A4's stated interface) — a workflow copy whose `PAGE_SCAN` differs by one character
  yields `files_cached: 0` with `cache_rejected: 0`; changing only a ruleset component likewise
  yields 0; changing neither yields full reuse — instrument: the patched-workflow control on the same
  harness; seam: **`PAGE_SCAN` + prompt text → `scanFingerprint` → the composed per-page key**, the
  term the composition move could silently drop; evidence: the three `files_cached` values.
  **(3) `[ship-verifiable]` — at rest — GATES:** the **reused half is returned, not lost** (A6) —
  `cache_records.length === files_checked + files_cached === files_listed` on the warm run, every
  record carries a non-empty `slug`/`key`/`scan`, a page with no `pageHashes` entry produces **no**
  record, and `fresh_scans` is **absent** from the return (retirement) — instrument: assertions over
  the run-2 return; seam: **workflow adjudication → the SKILL's write instruction**, where the spec
  previously asked the SKILL to re-derive a reusability judgment it structurally cannot compute;
  evidence: the counts + one reused record verbatim.
  **(4) `[ship-verifiable]` — at rest — GATES:** the **documented invocation is the executable one**
  — the two command lines extracted **verbatim from `full-scale.md`** (steps 2 and 5) run as written
  against a temp vault fixture and exit 0; a **missing** sidecar returns `status: "missing"` at
  exit 0 and a **corrupt** one `status: "unparseable"` at exit 0, never an error (step 2's standing
  mandate) — instrument: the extract-and-execute harness; seam: **prose instruction → shipped
  executable**, the seam A14-8 names as having no enforcement point; evidence: the extracted command
  lines + the three exit codes and status strings.
  **(5) `[ship-verifiable]` — at rest — GATES:** the fingerprint is **deterministic, complete and
  single-homed** — the same components in a **different key order** compose the identical value; a
  missing slot composes `''`, goes cold, and pushes a `coverage_caps` entry naming the absent slots;
  `full-scale.md` step 2 carries the **executable** component recipe (`shasum -a 256`,
  base-then-overlay merge order, UTF-8, first-16-hex lowercase) and
  `grep -n "a digest over, in this order" …/full-scale.md` returns **zero** (A40's retirement must
  not survive beside its replacement) — instrument: the ordering/completeness controls + the grep +
  a read of the rewritten step 2; seam: **SKILL-computed component digests → workflow-composed
  fingerprint** (Defect 2's composition half) **and prose recipe → SKILL execution** (Defect 2's
  digest half, which A7 shows the composition move alone does not reach); evidence: the two composed
  values + the cold-run cap text.
  **(6) `[ship-verifiable]` — at rest — GATES:** a **schema-mismatched sidecar is COUNTED and
  STATED** (A39) — seeded with K records in the field's own **flat pre-repair shape**, the run
  returns `cache_records_read: K`, `cache_rejected: K`, `files_cached: 0`, and `report.md:77`
  renders the rejected pair on its **cold** branch. The field failure (146 read, 146 discarded, a
  report that said only `cold`) cannot recur silently — instrument: the flat-shape control + a read
  of `report.md:77`/`:88`; seam: **vault sidecar file → workflow reader filter (`:245`) → report
  line**, the mandate that has been prose with no enforcement point since it shipped; evidence: the
  two counts + the rendered line.
  **(7) `[ship-verifiable]` — at the release gate — GATES:** `uv run tools/package-lint.py
  --expect-version X.Y.Z` exits **0** with both version strings bumped; **C6 passes with
  `_meta/vault-rule-card.md` re-stamped** against the edited operating contract (the R4 rename's
  priced cost); **E6 measures `PAGE_SCAN` unchanged at 3688** — build-2 must not move build-1's
  schema — instrument: package-lint Groups A/B/C/D/E at the release commit; seam: **source tree →
  release gate**, specifically the derived-artifact seam a contract edit opens and the schema-budget
  seam a sibling build could disturb; evidence: the PASS summary line in the release commit message.
  **(8) `[field-contingent]` — does NOT gate:** the cache actually **hits in a vault** — two
  consecutive `vlt-lint --full` sweeps on `{field-vault}` under an **unchanged** ruleset, the second
  reporting `files_cached > 0`, `cache_rejected: 0`, and the fingerprint it reused under (the first
  time the mechanism has worked since it shipped); event: the owner runs `vlt-lint --full` after
  upgrading to release 2 (that sweep is cold by construction) and then a **second** time with no
  release, overlay edit or convention change in between — **A26 already schedules that second sweep
  as the slot where `{field-vault}` pays its owed COMPLETE sweep**; performer: the owner; vault:
  `{field-vault}` only (no wiki corpus ships in this repo). **Tagged field-contingent because the
  roundtable verified in session (A17b) that b2(5)'s identical two-sweep event was CORRECTLY tagged
  so and that D3 does not reach it** — and **A14-8's discharge rests on checks (1)–(6)**, which cover
  the seam that broke with an executable writer, which is what A5 demanded and b2(5) did not have.
  This check is the residual named at the brief's §Out of scope 4: the SKILL invoking the script and
  transcribing 146 records into inline workflow args at scale. **A watch, not the proof.**
  **— ACCEPTANCE DISCHARGE 2026-08-27 — 7 of 8 DISCHARGED, (8) STILL-OPEN; the item stays
  UNCHECKED. Every GATING check is discharged.** **(1)–(6) DISCHARGED at rest** — recorded 7/7 PASS
  in the brief's BUILT `status:` (the three-run round-trip over the shipped writer, the
  `PAGE_SCAN`-keyed rejection control, the reused-half return, the extract-and-execute of
  `full-scale.md`'s own two command lines, the fingerprint ordering/completeness controls, and the
  flat-shape `cache_rejected: K` control). **(7) DISCHARGED at the release gate** —
  `package-lint: A/B/C/E PASS, D PASS — vlt 0.17.0 (… --expect-version 0.17.0, exit 0)`, release
  commit `c02fe3d`; `E6` held `PAGE_SCAN` and `C6` re-stamped `vault-rule-card.md`.
  **(8) STILL-OPEN — `[field-contingent]`, does NOT gate.** Its event has **not** occurred and is
  not a failure: the owner has deliberately deferred the first full sweep after release 2, so
  neither the cold sweep nor the second warm one has run. **Discharging event:** two consecutive
  `vlt-lint --full` sweeps on `{field-vault}` after the 0.17.0 upgrade
  (`{upgrade_reports}/2026-08-27-1157-upgrade.yaml` — already taken), with **no** release, overlay
  edit or convention change between them, the second reporting `files_cached > 0` /
  `cache_rejected: 0` and naming the fingerprint it reused under. **Trigger:** the owner, twice, on
  `{field-vault}` — sweep 1 is cold by construction (A26) and sweep 2 is the slot A26 already
  schedules for `{field-vault}`'s owed COMPLETE sweep. **First-exercise, not pass-through:** no
  sweep of the discharging kind has run since release 2, so the tripwire does not fire.
  **— ACCEPTANCE DISCHARGE 2026-08-31 (pass 3) — STILL-OPEN, and this is sweep 1 of the 2 it needs.
  The write leg is field-confirmed for the FIRST TIME since the cache shipped.**
  `{lint_reports}/2026-08-30-1123-lint.yaml` is the cold half of the pair, and it is cold for the
  right reason and says so: `lint_cache: 'cold (no sidecar - lint-cache.py read returned
  status: missing). scanned 146 / cached 0 of 146; this run''s fingerprint
  31f40c2cc90313a41dd3|bd6e1e211804a2011af; cache_records_read 0, cache_rejected 0. Sidecar
  rewritten from this run''s 146 cache_records'`. ⚠ **`cache_rejected: 0` on 0 records read is NOT
  the check's `cache_rejected: 0`** — that clause is about a *reuse* attempt, and none was made.
  **Verified at rest, not taken from the report:** `{field-vault}`'s `_agent/lint-cache.json` now
  exists at 156 KB carrying `"fingerprint": "31f40c2cc90313a41dd3|bd6e1e211804a2011af"` and its
  `records` array — the exact fingerprint the sweep names. The writer reached a live vault and left a
  readable sidecar behind. That is the half **b2(5) never once achieved across Cycles 12 and 13**,
  and it is now field-fact rather than at-rest fixture. **The reader has still never been exercised
  in a vault**, which is the whole of what this check measures.
  **Discharging event, unchanged:** a **second** `vlt-lint --full` on `{field-vault}` with no
  release, overlay edit or convention change between it and the 2026-08-30 sweep, reporting
  `files_cached > 0`, `cache_rejected: 0`, and the fingerprint it reused under. **Trigger:** the
  owner, once more. **Two notes for whoever runs it, so the result is not misread:**
  ⚠ (i) the 2026-08-30 sweep **wrote to five wiki pages** (prose `## Sources` sections — see
  build-4 (6)), so their digests moved and they will re-scan: expect roughly `files_cached: 141` /
  `files_checked: 5`, **not** 146. The check's bar is `> 0`, so partial reuse discharges it; a
  reading of 146 would be the surprising one. ⚠ (ii) the sweep's own `false_positives_refused` asks
  to *"fix the discovery regex before the next full sweep"* (filed `2026-08-31-104501`). **That
  repair is factory-side and reaches `{field-vault}` only through a release, and a release moves the
  ruleset fingerprint and forfeits the warm sweep.** Take sweep 2 first; the regex repair costs one
  more cold run whenever it ships.
  **First-exercise, not pass-through:** exactly one sweep of the discharging kind has run and it is
  the pair's cold half by construction — the tripwire does not fire on a pair half-completed.
  **— ACCEPTANCE DISCHARGE 2026-09-01 (pass 4) — DISCHARGED. The cache HIT in a vault. Every clause
  met on the named instrument, and build-2's item TICKS at 8/8 — the second bundled item in this
  cycle to complete.**
  **Evidence:** `{lint_reports}/2026-09-01-1406-lint.yaml`, the **second** consecutive full sweep, run
  by a peer session on the owner's behalf and **re-verified against the persisted report by this run
  rather than taken on relay**. `files_checked: 5` · **`files_cached: 141`** · `files_listed: 146` ·
  `coverage_caps: []`.
  **The three clauses, each verified:** `files_cached > 0` — **141**. `cache_rejected: 0` — the
  `lint_cache` line reads *"rejected 0 of 146 records read"*. **The fingerprint it reused under** —
  `31f40c2cc90313a41dd3|bd6e1e211804a2011af`, **byte-identical to the one the 2026-08-30 sweep
  recorded when it wrote the sidecar**. Ruleset unchanged between the two: both at 0.17.1, no release,
  no overlay edit, no convention change. The line says it plainly: **"WARM - the first warm run this
  vault has recorded."**
  ⚠ **The pass-3 prediction was exact.** That annotation said *"expect roughly `files_cached: 141` /
  `files_checked: 5`, not 146"*, because the 2026-08-30 sweep wrote five wiki pages after scanning
  them. The five re-scans are precisely those five — `drake-maye`,
  `fading-food-and-cue-reliability`, `nfl-2026-offense-rankings`, `shanahan-offensive-system`,
  `throne-of-glass-series-overview`. **A partial reuse discharges the check; 146 would have been the
  surprising reading.**
  **This closes the longest-standing defect in the register.** The findings cache shipped in Cycle 12,
  was refuted as **b2(5) FAILED — *"shipped and has never once worked"*** — and was rebuilt as Cycle 14
  build-2 (A14-8). **This is the first time in three cycles the mechanism has been observed working on
  a live vault.**
  **Measured effect, from the two runs' own `cost_accounting` — the answer to the owner's cost
  objection:** scan-page agents **146 → 5**, scan-page prompt chars **591,152 → 20,294**, total
  dispatches **172 → 31**. A **96% reduction on the scan phase.**
  ⚠⚠ **DISCHARGED WITH A CAVEAT THAT IS NOW ITS OWN FILING, AND THE CAVEAT IS LARGE.** The run's first
  attempt **was COLD and was discarded.** `rulesetComponents` was built with `pin_vector` as a JSON
  **array** (the workflow requires `typeof v === 'string'`, so the slot read as missing and the
  fingerprint composed **empty**), and with only the **8** conventions named in the pin vector rather
  than all **9** in `{conventions}` (`wiki-consolidation` is judged without being pinned). Both are
  defensible readings of `full-scale.md` step 2, which specifies the two **digest** slots exactly
  (instrument / merge order / encoding / truncation) and the two **component** slots not at all. Only
  a hand-debugged re-render made the sweep warm.
  **The check is discharged as written — it asks whether the cache hits in a vault, and it did, on the
  named instrument, with every clause met.** But **the mechanism reached warm by operator debugging,
  not by following the shipped documentation**, and a vault following that documentation gets a
  permanently cold cache and a report that says nothing is wrong. ⚠ **This plausibly explains the
  three-cycle failure the check was written to end** — it may never have been the writer that was
  broken. **Filed
  `factory/inbox/2026-09-01-140600-ruleset-fingerprint-inputs-are-under-specified-and-a-wrong-reading-is-silent.md`.**
  The discharge stands; the filing goes to capture; **do not read the tick as evidence the cache works
  for a vault that has not hand-debugged it.**

- [ ] **build-3 (governance-handshake, briefed 2026-08-27):** brief
  `factory/cycles/14-no-enforcement-point/briefs/build-3-governance-handshake.md`. **Seven checks —
  all `[ship-verifiable]`, all GATE; none field-contingent.** Release 2 (with builds 2 and 4).
  ⚠ **THE RE-ACK FIGURE IS SETTLED AT 19, NOT 15** (A15 + A13, ruled at brief time): `extraction.md`
  **7 → 8** (4 consumers) joins `write-verification.md` **3 → 4** (5) and `frontmatter.md` **13 → 14**
  (10) — because A13's pointer target must be a **handshaked** convention (`checks.md:19` has no
  frontmatter, no `version:`, no `consumers:`), and the closed recognized-set statement therefore
  lands in `extraction.md`, which repairs A15's falsified `:188` grounding sentence inside a bump
  already owed. **3 conventions, 19 acks, 11 files, one bipartite check.** ⚠ **The first full lint
  after release 2 is COLD by construction** (three convention digests + `checks.md`'s +
  `scanFingerprint`) — never a cache regression.
  **(1) `[ship-verifiable]` — at the release gate — GATES:** `uv run tools/package-lint.py
  --expect-version X.Y.Z` exits **0** with **E1** clean over `write-verification@4` /
  `frontmatter@14` / `extraction@8`, **E5** confirming `vlt-lint-full.js:11` acks both at the new
  versions, **C6** passing with `vault-rule-card.md`'s `derived_from: sha256:` re-stamped against the
  edited contract and the card under `RULE_CARD_BUDGET`, and **E6** measuring `PAGE_SCAN` unchanged
  at **3688** — instrument: package-lint Groups A/B/C/D/E at the release commit; seam: **convention
  `version:` ⟷ every consumer's declared ack**, across both edit surfaces (skill frontmatter and the
  asset `// depends_on:` header), plus the **derived-artifact** seam a contract edit opens; evidence:
  the PASS summary line in the release commit message + the four E6 lengths.
  **(2) `[ship-verifiable]` — at rest — GATES: ⚠ THIS IS THE CYCLE'S OWN THESIS MADE ENFORCEABLE.**
  The in-prose pins can no longer go stale silently: **package-lint `E7` ships**, is inventoried by
  E4, and **can fail** — mutating any one of the **eight** body tokens in `vlt-lint-full.js` (`:171`,
  `:178`, `:182`, `:229`×3, `:682`, `:684`) to a wrong version makes the lint exit non-zero naming
  that `file:line`; `grep -c` returns **5 `frontmatter@14` + 5 `write-verification@4`** with **zero**
  `@13`/`@3` survivors — instrument: the new E7 case in `tools/test-package-lint.py` (`CASE_FLOOR`
  23 → 24) plus a mutate-and-restore run against the shipped workflow; seam: **a convention's
  `version:` → the asset's header ack → the asset's PROSE recitations of the same pin** — the seam
  **E3 deliberately excludes** (`tools/package-lint.py:737-740`) and **E5 stops short of**, i.e. the
  seam that could have shipped stale citations to every vault through a green gate; evidence: the
  failing and passing lint outputs verbatim + the grep counts.
  **(3) `[ship-verifiable]` — at rest — GATES:** the narrowing **works** and the control still flags
  (A33's replacement for the forbidden count) — a Layer-3 file with `author: agent`, no pair,
  `type: record`, outside a container directory yields **no** `para_missing_attestation`, while the
  knowledge-artifact control (identical but `type: resource`) **does**, each with the shipped clause
  that decided it — instrument: a **reader protocol**, an agent given only the four edited shipped
  texts and the two fixture files; seam: **shipped convention prose → the agent that actually
  executes `para_missing_attestation`**, the check's only enforcement point (`vlt-lint-full.js:809`
  emits it as a structural slot; the PARA scan is SKILL-side per `full-scale.md:11`); evidence: both
  verdicts and both cited clauses verbatim. ⚠ **E3 binds the framing — the 27 appear nowhere in this
  check**, never as a rate and never as a measure.
  **(4) `[ship-verifiable]` — at rest — GATES:** the contract and the convention state the **same**
  exemption (A12b), so the batch does not resolve A14-7's two-surface disagreement by creating a new
  one — `contract:66`'s attestation-pair leg, `contract:70`'s carve-out, `write-verification.md`
  §Scope rule and `checks.md:17`'s Population carve-out all name the Layer-3 **operational-record
  class** in the same terms, and the class is **defined in exactly one file** (`extraction.md`) and
  cited at the other three — instrument: a four-site read + `grep -n "operational record"` over the
  governance bundle and `vlt-lint/references/`; seam: **contract ⟷ convention ⟷ shipped lint
  catalogue**, the three-surface agreement whose breakage is A14-7 itself.
  **(5) `[ship-verifiable]` — at rest — GATES:** `contract:66` no longer has an unowned leg and the
  pointer resolves to something that exists — the `type:` leg names `extraction.md`; `extraction.md`
  carries an explicit **closed recognized-set statement for the PARA population** (it did not before:
  zero occurrences of "recognized" in the file at `d641050`); `frontmatter.md:71` carries the PARA
  scoping clause and names `moc`; `checks.md:19` **cites** the set rather than defining it; and
  `grep -n "ride \`frontmatter.md\`'s declared non-exhaustive" skills/` returns **zero** (retirement
  2) — instrument: the retirement greps + a read of the four sites; seam: **governance boundary
  statement → the handshaked convention that owns its vocabulary**, A14-6's whole defect.
  **(6) `[ship-verifiable]` — bounded to the release-2 `vlt-upgrade` post-flight — GATES:** ⚠ **the
  unpark trigger A14 demanded.** The two live `kind: parked-interim` entries — against
  `conventions/extraction.md` (upstream filing #15) and `conventions/write-verification.md` (#16) —
  are each **re-derived against the rules in force and unwound**, and the vault executes
  `para_type_unknown`'s stated legal response for its blocked files **without declaring module
  vocabulary as its own** (the brief's route (b): retype to the target-folder type per
  `extraction.md`'s mapping, or relocate to the type's home zone); event: the owner runs
  `vlt-upgrade` on `{field-vault}` and works the post-flight — the same post-flight that ran for
  v0.16.2, already scheduled; performer: the owner; vault: `{field-vault}` only (it holds the parks);
  seam: **shipped ruling → the parked vault-local interim it was blocking**; evidence: the two parked
  entries resolved and the response executed on at least one named file — recorded with placeholders
  per A34/E5, never a real install path.
  **(7) `[ship-verifiable]` — bounded to the first full `{field-vault}` sweep after release 2 —
  GATES:** the transition posture reaches the measured population (A12), **measured not assumed** —
  the sweep reports the **`type:` distribution** of every `para_missing_attestation` entry across
  §Scope rule's jurisdiction list (the distribution A12 found **unmeasured**), and **every** entry
  has a legal response available under the amended `checks.md:17`, with pre-adoption entries rendered
  **informational**. **It can fail:** an entry with no available response, or one rendered as a
  violation where the pre-adoption clause should apply, fails it — instrument: the first full
  `vlt-lint --full` sweep after upgrading to release 2, read against the persisted `{lint_reports}`
  archive baseline that recorded the 27; event/performer/vault: as (6); seam: **the amended
  jurisdiction rule → the live PARA corpus that predates it**, the only seam where a narrowing that
  legalizes just-written files gets caught legalizing nothing.
  **— ACCEPTANCE DISCHARGE 2026-08-27 — 5 DISCHARGED (one with a stated caveat), (6) SPLIT, (7)
  STILL-OPEN; the item stays UNCHECKED.**
  **(1) DISCHARGED at the release gate** — `package-lint: A/B/C/E PASS, D PASS — vlt 0.17.0
  (… --expect-version 0.17.0, exit 0)`, release commit `c02fe3d`; the handshake reported
  **9 conventions / 39 pins bipartite-consistent** with 19 acks re-pinned across
  `write-verification@4` / `frontmatter@14` / `extraction@8`. **(2)(3)(5) DISCHARGED at rest** —
  recorded 5/5 PASS in the brief's BUILT `status:`; **`E7` shipped and passed on its first real
  release**, which is the cycle's own thesis made enforceable.
  **(4) DISCHARGED AS WRITTEN — ⚠ WITH A CAVEAT THAT MUST NOT BE LOST, AND THE OWNER MAY RE-RULE IT
  FAILED AT CLOSEOUT.** Every clause the check enumerates is verified true at rest against shipped
  source at `c02fe3d`: `vault-operating-contract.md:66` (attestation-pair leg), `:70` (carve-out),
  `write-verification.md:55` §Scope rule and `vlt-lint/references/checks.md:17` Population carve-out
  **all** name the Layer-3 operational-record class in the same terms (`record` / `register`), and
  the class is **defined in exactly one file** — `extraction.md:190`, one grep hit — and cited at
  the other three. **And the property the check was written to protect is nevertheless violated.**
  `extraction.md:84` — the closed recognized-`type:`-set statement, a *fifth* naming site the check
  never enumerated because it sits inside the defining file — names the class as
  **`charter | record | register`**, while `:190` defines it as `record` and `register`. A `charter`
  file is therefore a recognized PARA `type:` **and** outside the class that recognition places it
  in. The check tested **single-home-ness** (exactly one definition) and never compared
  **membership** between a naming site and the defining site; a class can have exactly one
  definition and still be named elsewhere with a different member list. **This is Cycle 14's own
  through-line reproduced by Cycle 14's own repair** — a rule stated, one site made responsible, a
  second site stating it differently, and no enforcement point comparing them. Concrete harm
  measured the same day: `{field-vault}`'s `write-verification.md` park resolves only partially and
  the post-flight names this as a reason (the 1 `charter` file among the 29 is not exempted).
  Filed as
  `factory/inbox/2026-08-27-171000-operational-record-class-has-two-memberships.md` (ship-verifiable
  at rest, no field event needed to grade a fix; candidate direction 2 is *give check (4) a
  membership comparison*). **Recorded as DISCHARGED because the rubric grades the check as written
  and every stated clause holds — not because the batch is clean.** Nothing is ticked on this
  reading: the build-3 item stays unchecked on (6) and (7) regardless, so no checkbox asserts the
  contradiction away.
  **(6) SPLIT — the TRIGGER DISCHARGED, the OUTCOME STILL-OPEN.** Bound event occurred: the
  release-2 `vlt-upgrade` post-flight, `{upgrade_reports}/2026-08-27-1157-upgrade.yaml`.
  **Upgrade-side DISCHARGED —** `governance_rule_changes:` rendered **non-empty with three
  rule-worded entries** (`write-verification` v3→v4, `extraction` v7→v8, `frontmatter` v13→v14) and
  `parked_interims_review` reported on **both** live parks, each **re-derived against the rules in
  force** rather than executed as recorded. **The unpark trigger A14 demanded exists and fired.**
  **Outcome, honestly a partial:** the **`extraction.md` park's blocker is RESOLVED** — its ruling
  landed in this release and the affected population was measured this run at **5 files**
  (`resources/briefs/**`, 3 subscriptions), matching the **5 recorded at park time**, so the growth
  rate did not bite; the post-flight also records that the ruling did **not** go the way the park's
  held position assumed. The **`write-verification.md` park resolves only PARTIALLY**: the ruling
  took the narrow-the-jurisdiction direction and narrowed **by artifact class only**, **explicitly
  refusing the partner-sitting reading the park was built on**. Measured this run: **29 unattested
  `author: agent|hybrid` Layer-3 files outside `{wiki}`** (`area` 22, `project` 3, `resource` 2,
  `record` 1, `charter` 1) — **only the 1 `record` file is exempted; `charter` is not named in the
  exemption text; 28 of 29 remain in jurisdiction** and the park's substantive blocker **STANDS**.
  **STILL-OPEN tails, both owner-triggered on `{field-vault}`:** (a) the `extraction.md` park's
  actual **unwind** — a superseding decision-log entry through the rostered write route, the
  human's act, not the upgrade's; (b) the `write-verification.md` park — keep the hold, re-file, or
  resolve narrowly, the human's call, and **`2026-08-27-171000` is a named blocker on resolving it
  fully**. The check's second leg — the vault executing `para_type_unknown`'s stated legal response
  (retype or relocate) on at least one named file — has **not** been executed and is part of (a).
  **⚠ EVIDENCE REFRESH 2026-08-27 (discharge pass 2) — the grade is UNCHANGED (still SPLIT, both
  tails still open); only the measured number moves.** The 0.17.1 upgrade
  (`{upgrade_reports}/2026-08-27-1328-upgrade.yaml`) re-measured both parks. **Tail (a),
  `extraction.md`:** *"STILL LIVE AND STILL UNRULED"*, population re-measured **unchanged at 5 files**
  under `resources/briefs/**` across 3 subscriptions; `extraction` v8 → v9 corrects a **different
  clause** and does not touch that ruling. **Tail (b), `write-verification.md`:** *"STILL LIVE AND
  STILL UNRULED"* — the `charter` exemption moved **one** file out, so **27 of 29 remain in
  jurisdiction (was 28)**, and *"the hot-fix moved exactly one file out of the population; it did not
  move the park"*. The blocker named in the pass-1 annotation — the refused partner-sitting reading,
  roster unchanged — **stands verbatim**. Both tails remain owner-triggered on `{field-vault}`.
  ⚠ The blocker `2026-08-27-171000` named in tail (b) is now **fixed and shipped** (v0.17.1,
  build-5 (1) discharged) and is **no longer a blocker on resolving the park** — but resolving it was
  never gated on that filing alone, as build-5 (6)'s FAILED grade records at length.
  **⚠ PARK 1 RE-DERIVED 2026-08-31 — IT DOES NOT UNWIND. The ruling it waited on landed and the
  re-derivation surfaced a defect in the ruling. Filed
  `factory/inbox/2026-08-31-152000-para-type-carve-out-is-an-enumeration-of-one-and-penalizes-accurate-vocabulary.md`.**
  The re-derivation was performed against `extraction.md` **v9** as shipped in v0.17.1, per the park's
  own standing instruction (*re-derive against the rules in force; do not execute the exit as
  recorded*) — and the exit recorded at park time is **invalid**: it assumed the ruling would make
  `type: research` legal at a `{resources}` address, and the ruling instead made it explicitly illegal
  **while leaving an identically-shaped shelf legal by name**.
  **The finding, in one line:** `extraction.md:84` removes the `{wiki}` subtree from the PARA
  population **by name** — `{wiki}` resolves to `resources/wiki/`, holds **146 files carrying
  `type: wiki`** (module-canonical, non-PARA), and is legal only because the rule contains its shelf's
  name. `resources/briefs/` is the same shape and is a finding forever. **The carve-out is a
  completeness-claiming list of one** — `vault-operating-contract.md:70` says *"one carve-out by
  name"* — and it fell behind an addition, which is the exact failure the module's own
  lists-that-claim-completeness-drift discipline names.
  **And the rule inverts:** `:84` admits vault-declared overlay schema but forbids *"declaring module
  vocabulary as vault-grown overlay schema"*, so a vault that types its briefs `dispatch-brief` is
  conformant today and `{field-vault}`, which used the module's own accurate word `research`, is
  permanently not. **The rule is strictest against vaults that use the vocabulary correctly.**
  **Both stated legal responses require writing something false.** Retyping to `type: resource`
  contradicts `extraction.md:28-30`'s own research-snapshot-vs-extracted-artifact distinction;
  relocating to `{research}` reverses a logged `capability-change` and destroys per-subscription
  containment. ⚠ **The vault already refused this exact move once and the module ratified the
  refusal** — park 2 (#16) declined to stamp a rostered `verified_by` on a file that op did not write,
  and `write-verification.md:55` v5 now reads *"fusing permission to provenance is the write-path
  failure this exemption exists to prevent."* **Falsifying `type:` to satisfy `para_type_unknown` is
  the same act as falsifying `verified_by:` to satisfy `para_missing_attestation`.**
  **Disposition:** a **superseding `parked-interim` entry against the new filing**, replacing the hold
  against #15 — a new park with a correct premise, not a continuation. ⚠ **That entry is an owner act
  in `{field-vault}` and has NOT yet been written**; until it is, park 1 is live and unchanged in the
  log, and the next `vlt-upgrade` will surface it again.
  **Evidence refresh:** the population is **8 files across 3 subscriptions**, not 5 — the park
  recorded 5 and the 2026-08-30 sweep re-measured 5; **three more were written 2026-08-31**. The
  growth rate the park priced (*"one file per subscription per cadence"*) **has fired exactly once and
  on schedule.** The producer is the vault-local `vlt-brief`, and under the filed direction its
  current line becomes correct rather than something to change.
  ⚠⚠ **CONSEQUENCE FOR THIS CHECK: (6) is now expected to FAIL, and it GATES.** The check requires
  **both** parks *"re-derived against the rules in force **and unwound**"* plus `para_type_unknown`'s
  legal response executed on at least one named file. Under this disposition the `extraction.md` half
  is re-derived but **not** unwound and the response is **not** executed. **The honest outcome: the
  check fails because the module is wrong, which is what an acceptance check is for.** The
  alternative — retyping 8 files to a value the vault believes false in order to turn a gate green —
  is the failure mode this cycle exists to name. **Not graded FAILED yet**: park 2's disposition and
  the superseding entries are still outstanding, and (6) is graded once, whole, on the owner's acts.
  **(7) STILL-OPEN.** Its event has **not** occurred and is not a failure: the owner has
  deliberately deferred the first full sweep after release 2. **Discharging event:** the first
  `vlt-lint --full` sweep on `{field-vault}` after the 0.17.0 upgrade, reporting the `type:`
  distribution of every `para_missing_attestation` entry across §Scope rule's jurisdiction list,
  every entry carrying a legal response under the amended `checks.md:17`, pre-adoption entries
  rendered informational; read against the `{lint_reports}` archive baseline that recorded the 27.
  **Trigger:** the owner, once, on `{field-vault}`. That sweep is COLD by construction (A26).
  ⚠ The 29-file `type:` distribution already measured at the post-flight is **not** this check — it
  is an upgrade-side count over a different population, not the sweep's `para_missing_attestation`
  entries with their responses adjudicated.
  **— ACCEPTANCE DISCHARGE 2026-08-31 (pass 3) — ⚠ BLOCKED (unreachable). OWNER-RULED. The bound
  event OCCURRED and the observable the check names is produced by NO SHIPPED SURFACE.**
  `[ship-verifiable]`, so it **GATES** — this is the cycle's **third** gating blocker.
  **The event fired.** `{lint_reports}/2026-08-30-1123-lint.yaml` is the first full `vlt-lint --full`
  sweep on `{field-vault}` after release 2, taken at `module_version: 0.17.1`. There is no longer any
  waiting to do.
  **What the sweep rendered.** `flag_for_human.para_missing_attestation` carries **one string
  standing in for 27 files**: *"27 PARA files carry a vault type: + author: agent|hybrid with no
  attestation pair - ADJUDICATED [2026-08-26] parked-interim (ref: conventions/write-verification.md;
  upstream filing #16, open). Count unchanged from the 2026-08-27 sweep. Disposed, not undisposed"*.
  No `type:` distribution. No per-file entries. The 2026-08-27 sweep renders the identical rollup
  form, so this is the standing behaviour and not a one-run slip.
  **Why BLOCKED and not FAILED.** The check's own stated fail conditions are **untripped**: no entry
  lacks a legal response (the whole population is disposed *adjudicated parked-interim*, which
  `checks.md:17` allows), and no entry is rendered as a violation where the pre-adoption clause should
  apply. Nothing here contradicts the check. What is absent is the **observable**: grounded against
  shipped source at 0.17.1, `skills/vlt-lint/references/report.md:32` mandates
  `para_missing_attestation: [<para-file: …>, ...]` — a per-file list — and **never a `type:`
  distribution anywhere in `skills/`** (`grep -rn "distribution" skills/vlt-lint/` returns zero).
  `skills/vlt-setup/assets/workflows/vlt-lint-full.js:812-814` returns the slot empty and comments
  that it is *"a structural slot the SKILL fills"* — the workflow cannot produce it and the SKILL is
  not asked to. **No amount of further sweeping produces this check's evidence**, which is the
  rubric's definition of BLOCKED and the reason re-annotating STILL-OPEN is forbidden: waiting cannot
  discharge it.
  **The pass-through tripwire also fires**, independently and for the same conclusion: a sweep of the
  discharging kind has now run and did not touch the surface under test.
  **Filed** as
  `factory/inbox/2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md`
  (instance (a) of three), ship-verifiable at rest — a repair is gradeable against a rendered report
  with no field event. Once that repair ships, the check has a real trigger and a future discharge run
  can grade it honestly, which is the whole point of routing an unreachable tail into capture rather
  than carrying it.
  ⚠ **This is Cycle 14's own through-line arriving inside Cycle 14's own instrument** — a rule stated
  (`report.md`'s slot-by-slot shape), a place named responsible for it (the SKILL's Step 6 render),
  and no enforcement point comparing the render to the rule. The cycle is titled for exactly this.
  ⚠ **A second reading the owner may take at closeout, stated so it is not lost:** the check's
  *substantive* question — does the amended jurisdiction rule reach the measured population with a
  legal response available for every entry — is answered **yes** by this sweep, on the rollup's own
  terms. What cannot be verified is the per-`type:` claim the check chose as its evidence. Closeout
  may rule that sufficient. This run does not, because the check names its instrument and this is not
  it — the identical call already made twice in this ledger (build-5 (5) pass 2, and the pass-1
  refusal of the post-flight's 29-file count directly above).
  **⚠ RE-GRADED 2026-08-31 — DISCHARGED WITH A CAVEAT ON RECORD. OWNER-RULED, on the second reading
  this run's BLOCKED annotation set out immediately above. The gating blocker is cleared; the defect
  is not.**
  **What the ruling accepts.** The check's **substantive** question — *does the amended jurisdiction
  rule reach the measured population, with a legal response available for every entry and
  pre-adoption entries informational* — is answered **yes** by the 2026-08-30 sweep on the rollup's
  own terms: all **27** entries are disposed *ADJUDICATED [2026-08-26] parked-interim*, which
  `checks.md:17` permits, and no entry is rendered as a violation where the pre-adoption clause
  should apply. Both of the check's stated fail conditions are untripped.
  **And the `type:` distribution the check names is now measured — at rest, this run.** Computed
  directly over `{field-vault}`'s PARA tree (files carrying a vault `type:` + `author: agent|hybrid`
  with no `verified_by`/`verified_at` pair, outside `{wiki}`): **29 total —
  `area` 22 · `project` 3 · `resource` 2 · `record` 1 · `charter` 1** — minus the two
  operational-record files carved out (`projects/fantasy-2026/record.md`,
  `projects/fantasy-2026/charter.md`) = **27 in jurisdiction.** This reproduces the 0.17.1
  post-flight's distribution exactly, and it is the distribution A12 found unmeasured. **The number
  the check was written to obtain now exists and is on the record.**
  ⚠ **CAVEAT, and it is the whole reason this is not a clean discharge: the distribution was NOT
  produced by the instrument the check names.** It was computed at rest by this discharge run, not
  rendered by the sweep. That is the identical instrument substitution this ledger refused twice —
  for build-5 (5) at pass 2, and in the pass-1 refusal of the post-flight's 29-file count. **The
  refusals were right and are not disturbed.** This discharge rests on an explicit owner ruling that
  the substitution is acceptable **here specifically**, for a reason the earlier two lacked: the
  substituted computation is over **the same population the check names**, reproduces the sweep's own
  27 and the post-flight's own 29, and is derivable from the shape `report.md:32` **already
  mandates** — the per-file entry form is `<para-file: vault **type** + author agent|hybrid …>`, so a
  correctly-rendered slot carries the type per entry and the distribution falls out of it. The
  observable is not unobtainable; it is **unrendered**.
  **The defect is NOT ruled away.** `factory/inbox/2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md`
  routes to `inbox-capture` unchanged, carrying all three instances. This ruling clears the gate; it
  does not retire the filing, and a Cycle 15 repair that makes the slot render per `:32` is what
  makes this check honestly gradeable next time. **A future ledger must not cite this ruling as
  precedent for substituting instruments** — it is precedent only for the narrow case where the
  substitute computes the check's own population and the shipped shape already mandates the missing
  render.
  **— ACCEPTANCE DISCHARGE 2026-09-01 (pass 5) — the SPLIT RESOLVES to FAILED. `[ship-verifiable]`,
  it GATES, and it is the ONE gating item Cycle 14 closes on. Graded, no longer predicted.**
  **Verified in `{field-vault}` by this run against the decision log itself, not taken on relay**
  (`core-lint` landed the entry at vault commit `307c901`; the sweep is
  `{lint_reports}/2026-09-01-1519-lint.yaml`, `rulings_recorded:` carrying the write-through).
  **The check has three clauses. None is met.**
  **(a) Park #15 (`extraction.md`) — NOT re-derived in the log, NOT unwound. Still LIVE.** Confirmed
  at rest: `_agent/mint/decision-log.md` carries **no** `superseded_by:` on the 2026-08-26
  `parked-interim` against `conventions/extraction.md`. It was re-derived *analytically* on 2026-08-31
  and the re-derivation found the **ruling** defective, which is why it produced a supersession filing
  rather than an unwind. **Under `extraction.md` v9 it cannot unwind without writing something false**
  — both stated legal responses require it — so the park stands and build-6, which would have given it
  a legal response, was withdrawn.
  **(b) Park #16 (`write-verification.md`) — re-derived and superseded in the log, but RE-PARKED, NOT
  UNWOUND.** Both halves verified: `decision-log.md:1259` carries `superseded_by:` /
  `superseded_date: 2026-09-01` / `superseded_reason:`, and `:1446` is the new
  `[2026-09-01] parked-interim — partner-sitting Layer 3 writes, held for the retirement of the
  `verified_by` roster`, carrying `supersedes:`. **A re-park is a re-derivation, not an unwind** — the
  check's word is *unwound*, and the vault deliberately holds rather than concedes.
  **(c) The legal response — NOT executed.** `para_type_unknown`'s stated response (retype or
  relocate) was not carried out on any of the 9 brief issues, because both available forms require
  writing something the vault holds to be false. That clause was build-6's to satisfy; build-6 is
  withdrawn.
  ⚠ **The FAIL is the honest outcome and should not be read as a process failure.** The check asked
  the vault to unwind two parks against the rules in force. The vault re-derived both, found that one
  of the rules was itself defective, and **filed for its retirement instead of executing an exit it
  believes false.** That is the parked-interim mechanism working exactly as `decision-log.md` v4
  intends — *"re-derive the unwind against the rules in force at unwind time"* — and it is what the
  rule exists to make possible. **A green here was available only by falsifying a `type:` field.**
  **Routes to `cycle-closeout` for its ruling.** Both retirements are filed
  (`factory/inbox/2026-09-01-160000-…` and `…-170000-…`, the cycle's first two `class: supersession`
  filings) and both go to **Cycle 15 ideation**, where the roundtable's **obsolescence beat** — P-15's
  half that has never been exercised — is the beat built to receive a retirement.
  ⚠ **One thing owed and not done:** neither supersession filing has been posted through
  `vlt-feedback`, so park #16 references no live tracker issue the way #15 and #16 do. The entry says
  so explicitly. `vlt-feedback` is invoked-only and needs the owner's explicit go — **an owner
  decision, deliberately not taken by any agent.**

- [x] **build-4 (lint-references, briefed 2026-08-27):** brief
  **— ITEM TICKED 2026-08-31.** With (1) re-graded and (6) discharged this run, **all 6 of build-4's
  checks are DISCHARGED** — the first bundled item in this cycle to complete. ⚠ **It rests on the
  contested build-4 (1) ruling**: reopening that un-ticks this item and restores one gating FAIL.
  ⚠ **Its two filings are consequently archive-eligible and were deliberately NOT moved** —
  `factory/inbox/2026-08-26-123144-reclassify-sources-vs-prose-mismatches-out-of-fix-now.md` (A14-4)
  and `factory/inbox/2026-08-26-123153-lint-mandates-strict-yaml-persist-with-no-yaml-library.md`
  (A14-5). The rubric archives a filing once all its ledger items are discharged, and both map to
  build-4 alone. **Left in `factory/inbox/` as an owner call**, because archiving them now would have
  to be reversed if closeout reopens (1), and because A14-5's filing is the parent of
  `2026-08-27-153000`, which is **not** discharged and stays live regardless. `cycle-closeout`
  Stage 5 is the natural place to take this.
  `factory/cycles/14-no-enforcement-point/briefs/build-4-lint-references.md`. **Six checks — all
  `[ship-verifiable]`, all GATE; none field-contingent.** ⚠ **THE RELEASE BUILD for release 2**
  (with builds 2 and 3) — it carries the dual version bump and the `--expect-version` gate that
  build-3's check (1) and build-2's check (7) both deferred to it. ⚠ **The first full lint after
  release 2 is COLD by construction** — build-4 moves `checks.md`'s digest **and** edits `PAGE_SCAN`
  and `pageScanPrompt`, on top of builds 2 and 3; never a cache regression (A26: this cycle's second
  cold sweep, knowingly). ⚠ **GROUNDING ADDITION: `vlt-lint-full.js` is a build-4 site** — the
  roadmap's `Touches:` list omitted it, and the ruled direction routing is not expressible without it
  (the scanner returns a tri-state with no direction). **E6 price is NEGATIVE 12: `PAGE_SCAN`
  3688 → 3676.**
  **(1) `[ship-verifiable]` — at rest — GATES: ⚠ THIS IS A10's VALIDATION BEAT.** A persisted report
  parses whole, **on real material** — every `.yaml` report in read-only copies of `{field-vault}`'s
  `{lint_reports}` archive loads under a strict YAML parser, and the most recent one, re-rendered to
  `.json` per the newly documented JSON-subset strategy, parses under `python3 -m json.tool`. **It can
  fail** — an archived LLM-authored report that does not parse is exactly what A14-5 predicted and
  nothing has ever tested; the failure is recorded verbatim and the archive is never repaired —
  instrument: `uv run --with pyyaml` (a declared tool, **factory-side**, adding no vault-side
  assumption) + stdlib `json.tool`, over copied archive material, at rest; seam: **agent-authored
  report block → persisted file → machine reader**, the seam `report.md:3` asserts and nothing checked;
  evidence: file count, per-file verdict, any parse error verbatim. ⚠ Fallback if the archive is
  unreachable: a synthetic specimen report — **rule R2's observer duty then fires**, recorded in the
  BUILT `status:` and named at closeout.
  **(2) `[ship-verifiable]` — at rest — GATES:** the direction routing has an enforcement point that
  is not prose — over the **shipped** reduce, `diverge_prose_gap` lands in
  `fix_now.sources_vs_prose_mismatches` and nowhere else, `diverge_frontmatter_gap` and
  `diverge_unclassified` land in `flag_for_human.sources_vs_prose_unresolved` and **never** in
  `fix_now`, `match`/`no_prose_section` produce neither. **It can fail:** a predicate written against
  `sources_vs_prose_detail` instead of the verdict passes a reading and fails this — instrument: a
  node fixture, five stub scans, `args` as a JSON string, factory-side at rest; seam: **scanner verdict
  → report slot**, the tier assignment A14-4 files as wrong; evidence: both arrays verbatim.
  **(3) `[ship-verifiable]` — at rest — GATES:** the destructive instruction is gone and the second
  response exists — `grep -rn "reconcile the prose section to frontmatter" skills/` returns **zero**;
  `checks.md:16` states **two** legal responses routed by direction, names `diverge_unclassified` as
  never-auto-fixed, and cites `fix-and-file.md` for the procedure; `fix-and-file.md` Step 3 carries the
  class's missing entry and **cites `checks.md` for the direction test** rather than restating it;
  `report.md` carries both slots — instrument: the greps + a read of the four edited sites; seam:
  **module source → vault-read documentation** (named as such, not dressed as behavioural); evidence:
  grep output + the four rewritten lines.
  **(4) `[ship-verifiable]` — at rest — GATES:** the persist permission has **one** format story and
  no site still mandates the other (A8, closed) — `SKILL.md:74` permits both homes and defines
  `verbatim` as **content-verbatim**; `report.md:3` is **restated, not appended to**; `SKILL.md:76`,
  `full-scale.md:10` and `vlt-setup/SKILL.md:194` name both extensions; and **`full-scale.md:13`'s
  churn discovery matches both**, so a `.json`-persisting vault is not invisible to its own history
  and cannot render `unmeasured (no prior full report)` forever. **It can fail:** leaving any one of
  the five restatements `.yaml`-only reproduces the inverted pointer — instrument: the format greps +
  a read of the six sites; seam: **the persist step's single home → its five restatements**; evidence:
  grep output + the six lines.
  **(5) `[ship-verifiable]` — at the release gate — GATES: ⚠ THE GATE build-3's CHECK (1) LEFT TO THIS
  BUILD.** `uv run tools/package-lint.py --expect-version X.Y.Z` exits **0** with **both** version
  strings bumped (recommended **0.17.0**, the owner confirming at `vlt-release`), **E6** measuring
  `PAGE_SCAN` at **3676**, **E7** clean over the eight in-prose pin tokens with `:178`/`:229` preserved
  at `write-verification@4` / `frontmatter@14`, and **E1/E5/C6 unchanged** (no convention `version:`
  moves, no governance-bundle edit — `vault-operating-contract.md:51`/`:323` name `{lint_reports}` as a
  directory with no extension, so a `.json` persist is already legal under the contract) — instrument:
  package-lint Groups A/B/C/D/E at the release commit; seams: **source tree → release gate**, and for
  E6 **source literal → runtime serialization**; evidence: the PASS summary line in the release commit
  message + the four measured schema lengths.
  **(6) `[ship-verifiable]` — bounded to the first full `{field-vault}` sweep after release 2 —
  GATES:** the **0% application rate is cured, measured not assumed** — every
  `sources_vs_prose_mismatches` entry in that sweep is applied (it appears in `fixes_applied:`) or its
  non-application is recorded with its reason, and **no** `sources_vs_prose_unresolved` entry is
  auto-applied. Baseline from the persisted `{lint_reports}` archive: **26 then 25 instances across two
  consecutive full sweeps, zero applied**, both runs declining the whole class for the same recorded
  reason. **It can fail:** a `fix_now` entry declined again for a judgment reason means the routing did
  not cut the populations apart and the class belongs in `flag_for_human` whole (A14-4's own fallback
  option 2) — instruments, **two and different**: the archive for the baseline (no new sweep needed) and
  the live post-upgrade sweep; seam: **live wiki corpus → the routed check → the serial fixer**, the
  seam where the misclassification was measured; event: the owner runs `vlt-lint --full` on
  `{field-vault}` after upgrading to release 2; performer: the owner; vault: `{field-vault}` only.
  ⚠ That sweep is COLD by construction; coldness is not a finding here.
  *No check binds a vault to CHOOSING the `.json` persist, deliberately:* nothing in the build, the
  release or the upgrade causes a vault to take a permission, so such a check would be the unbounded
  species wearing a ship-verifiable tag. The `.json` emission is exercised at rest in check (1)
  instead.
  **— ACCEPTANCE DISCHARGE 2026-08-27 — 4 DISCHARGED, (1) FAILED (owner-ruled kept), (6)
  STILL-OPEN; the item stays UNCHECKED.**
  **(2)(3)(4) DISCHARGED at rest** and **(5) DISCHARGED at the release gate** — recorded in the
  brief's BUILT `status:` (4 PASS); release commit `c02fe3d` carries
  `package-lint: A/B/C/E PASS, D PASS — vlt 0.17.0 (… --expect-version 0.17.0, exit 0)`, with **E6
  measuring `PAGE_SCAN` at 3676** (the ruled −12) and **E7 clean over the eight in-prose pin
  tokens**.
  **(1) FAILED — and the FAIL is KEPT, owner-ruled 2026-08-27: do NOT re-scope it to pass.**
  A10's validation beat found exactly what A14-5 predicted and nothing had ever tested: of the 6
  archived `.yaml` reports in read-only copies of `{field-vault}`'s `{lint_reports}` archive,
  **1 does not load under a strict YAML parser** — `2026-08-24-1700-lint.yaml`, a bare unquoted
  scalar containing `: ` at **line 102**. **The archive was NOT repaired** (the check forbids it;
  the vault is read-only). Filed as
  `factory/inbox/2026-08-27-153000-persisted-lint-report-is-not-machine-readable.md` at `7056ae6`,
  before release 2 shipped. ⚠ **The check's honest subject going forward is reports written *under*
  the mandate** — `report.md:3`'s restated persist clause post-dates every file in that archive, so
  a successor check must measure reports emitted after v0.17.0, not retrofit a verdict onto ones
  emitted before it. That re-scoping is the successor build's to make at brief time, **not** this
  run's to apply retroactively.
  **⚠ RE-GRADED 2026-08-31 — DISCHARGED on the check's forward subject. OWNER-RULED, over a recorded
  tension in this ledger's own instructions. Read the tension before citing this discharge.**
  **The new evidence, verified at rest this run.** `yaml.safe_load` over all **seven** archived
  reports in read-only copies of `{field-vault}`'s `{lint_reports}`: `2026-08-23-1504` PASS ·
  `2026-08-23-1739` PASS · **`2026-08-24-1700` FAIL** (*"mapping values are not allowed here"*, the
  same bare unquoted scalar at `:102`) · `2026-08-25-1600` PASS · `2026-08-26-1046` PASS ·
  `2026-08-27-1104` PASS · **`2026-08-30-1123` PASS**.
  **The dating that matters.** v0.17.0 — the release carrying `report.md:3`'s restated persist
  clause — shipped at **11:57 on 2026-08-27** (`{upgrade_reports}/2026-08-27-1157-upgrade.yaml`).
  `2026-08-27-1104-lint.yaml` was written at **11:04, fifty-three minutes earlier**, so it is
  pre-mandate like every report before it. **`2026-08-30-1123-lint.yaml` is the first report ever
  written under the mandate, and it parses. Post-mandate population: 1 of 1.**
  ⚠ **THE TENSION, STATED PLAINLY — under the check's LITERAL population this still reads FAIL.**
  The check as written measures *"of the archived `.yaml` reports … 1 does not load"*. That archive
  now holds **7** reports and **1 still does not load**. The discharge depends entirely on accepting
  the forward-subject narrowing, and **this ledger has said two different things about who may make
  it**: the pass-1 annotation immediately above reserves it — *"That re-scoping is the successor
  build's to make at brief time, **not** this run's to apply retroactively"* — while §Next lifecycle
  move routes it here — *"the re-grade belongs to `acceptance-discharge`."* **Both lines are in the
  record and neither was written in ignorance of the other.**
  **What the owner ruled, and the reasoning offered for it.** That grading a shipped emission
  discipline against an artifact **rendered by the path the build replaced** measures history, not
  the discipline; that `2026-08-24-1700-lint.yaml` is read-only by the check's own terms and can
  never leave the archive, so under the literal population **this check can never pass at any point
  in the future** — which is a check with no passing state, the exact species [P-20] exists to catch;
  and that the narrowing is not invented here but was already written into the check's own
  annotation on the day it failed.
  ⚠ **What this discharge does NOT claim, and what a reader must not take from it.** **(i)** One
  report is a population of one — the emission discipline is **not** proven at scale. The honest
  reading is *"the first report written under the mandate parses"*. The second sweep (build-2 (8))
  adds a second member and **should be read against this check too**. **(ii)** The 2026-08-27 ruling
  *keep the honest FAIL, do not re-scope it to pass* is **not overturned** and still governs any
  narrowing made to dodge a failure; this one is accepted because the check's forward subject went
  from **empty** to non-empty, not because the bar moved. **(iii)** Filing
  `factory/inbox/2026-08-27-153000-persisted-lint-report-is-not-machine-readable.md` is **NOT
  withdrawn.** It diagnoses the **absence of an emission discipline**, which is still absent — the
  render simply happened to be well-formed. It routes to `inbox-capture` unchanged, alongside its
  cousin `2026-08-31-104500` (the shape is mandated at `report.md` and enforced nowhere), which is
  the same gap seen from the other side. **The check is discharged; the defect it was written to
  catch is open.**
  ⚠ **If closeout disagrees, this is the item to reopen.** Of the three rulings recorded 2026-08-31,
  this is the one resting on a contested reading rather than on new measurement alone — build-3 (7)'s
  substitution and build-1 (6)'s bound debt do not depend on it. Reversing it restores one gating
  FAIL and nothing else.
  **(6) STILL-OPEN.** Its event has **not** occurred and is not a failure: the owner has
  deliberately deferred the first full sweep after release 2. **Discharging event:** the first
  `vlt-lint --full` sweep on `{field-vault}` after the 0.17.0 upgrade, in which every
  `sources_vs_prose_mismatches` entry is applied (appearing in `fixes_applied:`) or its
  non-application is recorded with its reason, and **no** `sources_vs_prose_unresolved` entry is
  auto-applied — read against the archive baseline of **26 then 25 instances across two consecutive
  full sweeps, zero applied**. **Trigger:** the owner, once, on `{field-vault}` — the **same** sweep
  build-3's (7) awaits, so one owner act discharges both. That sweep is COLD by construction;
  coldness is not a finding here. ⚠ Note for that run: the **2026-08-27 sweep (release 1, not
  release 2) already applied 6 of its `sources_vs_prose_mismatches` entries** — a 0-of-26 baseline
  moving off zero — but it ran under the **pre-build-4** routing and therefore cannot grade this
  check.
  **— ACCEPTANCE DISCHARGE 2026-08-31 (pass 3) — DISCHARGED. The 0% application rate is CURED,
  measured on the named instrument, and the routing cut the populations apart. ⚠ One caveat is on
  record and is filed.**
  **Bound event occurred:** `{lint_reports}/2026-08-30-1123-lint.yaml`, the first full sweep after
  release 2, at `module_version: 0.17.1`, 146 pages, cold as expected.
  **Leg 1 — every `fix_now` entry applied or its non-application recorded with its reason: MET.**
  Ten `sources_vs_prose_mismatches` entries. **Five applied**, each naming the page and what was
  written: `drake-maye` (the ESPN top-10-QB-2026 URL + a research-note wikilink),
  `fading-food-and-cue-reliability` (the YouTube lure-fading demonstration),
  `nfl-2026-offense-rankings` (the Schottenheimer research note), `shanahan-offensive-system` (a
  `sources/articles/…` schematic-trend piece), `throne-of-glass-series-overview` (the
  series-complete report). **Five refused, with a per-page reason for each** — `barbacoa` (the prose
  delegates explicitly: *"see that note's Sources section for individual URLs"*),
  `carbon-steel-seasoning` (all three Made In articles named descriptively, all three research notes
  wikilinked), `obsidian-dataview` (`functions.md` cited as repo + path rather than URL),
  `positionless-defense-nfl` (the War Room transcript IS in the prose section),
  `nfl-2026-draft-first-round` (transcript present; the article cited indirectly via its research
  note) — with the refusal restated in `false_positives_refused` as *"sources_vs_prose_mismatches:
  5 of 10 refused"*.
  ⚠ **The direction is the build's direction.** The 08-27 baseline moved entries **prose → frontmatter**
  (*"6 pages: prose-only entries added to frontmatter sources:"*). This sweep moves them
  **frontmatter → prose** (*"added … to the prose ## Sources section"*), which is the legal response
  `checks.md:16` single-homes for this class. The routing build-4 shipped is doing the thing it was
  built to do, on a live corpus, at 146-page scale.
  **Leg 2 — no `sources_vs_prose_unresolved` entry auto-applied: MET.** Fourteen entries sit in
  `flag_for_human.sources_vs_prose_unresolved`, none applied. The strongest evidence is the
  fourteenth: the workflow returned `roast-chicken` under `unmarked_supersessions`, and the reduce
  **reclassified it** — *"it is a prose-cites-what-frontmatter-lacks divergence
  (diverge_frontmatter_gap), which is flag-only: deciding whether a prose mention is a contributing
  source is a provenance judgment"* — and `false_positives_refused` records the reclassification
  separately. A misrouted entry was caught **by the routing** and sent to the flag-only half. That is
  the enforcement point A14-4 asked for, working on a real return.
  **The stated fail condition is NOT tripped.** It reads: *a `fix_now` entry declined again for a
  judgment reason means the routing did not cut the populations apart and the class belongs in
  `flag_for_human` whole.* The five refusals are **refutations of over-reports**, not declines — each
  was *"verified against each prose section before writing, not from the scanner's prose"*, and each
  found the citation already traceable. The class was **not** declined whole for one recorded reason,
  which is exactly what both baseline sweeps did. Five of ten applied is the cure; the remaining five
  are a **scanner precision** problem (the scanner claims a divergence that is not one), not a
  routing problem.
  ⚠ **CAVEAT ON RECORD, AND FILED: the check's named location does not exist in this report.** The
  check says *"is applied (**it appears in `fixes_applied:`**)"*. `{lint_reports}/2026-08-30-1123-lint.yaml`
  has **no `fixes_applied:` key at all** — its top-level keys are `mode`, `scope_since`,
  `files_checked`, `files_cached`, `files_listed`, `fix_now`, `flag_for_human`, `rulings_recorded`,
  `coverage_caps`, `false_positives_refused`, `lint_cache`, `churn_since_last_full`,
  `cost_accounting`. `report.md:72` mandates the key, and the **2026-08-27 report renders it
  correctly**, so it was dropped between two renders of the same skill with no code change between.
  The five applications are recorded inline in `fix_now.sources_vs_prose_mismatches` instead.
  **Discharged on the substance, not the slot:** unlike build-5 (5) pass 2 and build-3 (7) — where the
  evidence came from a *different instrument over a different population* — the fact here is **in the
  named instrument**, in an adjacent slot of the same report. That distinction is why this discharges
  and those do not; it is stated so the ledger's consistency is checkable rather than asserted.
  **Filed** as instance (b) of
  `factory/inbox/2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md`.

- [ ] **INHERITED — Cycle 12 b3(7) (re-read on release 2's acceptance run; recorded here by build-3's
  brief per roundtable A25):** `[field-contingent]` — **does NOT gate.** A partner resolving a
  `{resources}`-write legality question from the rewritten bundle **without escalating**
  (`factory/cycles/12-proxy-claims/roadmap.md:2896-2902`, `:3082-3088`). Released as a standing watch
  at Cycle 12's closeout with the instruction *"re-read it after Cycle 14 build-3, against a bundle
  that is no longer waiting on itself"* — **build-3 is that build**: it ships both rulings the two
  live parks were waiting on, so the escalation that would previously have been legitimate is no
  longer the bundle's fault. Event: the owner **observes** a partner session attempting a
  `{resources}` write after the release-2 upgrade; performer: the owner; vault: `{field-vault}`.
  **Tagged field-contingent because nothing in the build, the release or the upgrade causes such a
  session** — it is the unbounded species per `brief-anatomy.md:203-210`, and Cycle 12 recorded that
  no evidence exists either way on disk. Not build-3's to discharge; carried so `cycle-closeout`
  cannot silently drop the one item Cycle 12's never-delivered hand-off left it.
  **— ACCEPTANCE DISCHARGE 2026-08-27 — STILL-OPEN; `[field-contingent]`, does NOT gate.**
  The precondition it was waiting on is now **met**: build-3 shipped in v0.17.0 and both rulings the
  live parks were waiting on are in force, so the bundle is no longer waiting on itself and an
  escalation would no longer be its fault. The **observation** has not occurred: no
  `{resources}`-write partner session is recorded on `{field-vault}` since the 0.17.0 upgrade, and
  no evidence exists either way on disk — the same state Cycle 12's closeout recorded.
  **Discharging event:** the owner **observes** a partner attempt a `{resources}` write in an
  ordinary session after the release-2 upgrade and resolve the legality question from the rewritten
  bundle **without escalating**. **Trigger:** the owner, deliberately — open a partner session and
  pose a `{resources}`-write legality question.
  ⚠ **PASS-THROUGH TRIPWIRE RE-EXAMINED, as the rubric requires of a tail surviving a second
  discharge run unfired.** This tail was carried at Cycle 12's closeout and is now unfired at a
  second run, so re-annotating STILL-OPEN without re-examining reachability is forbidden.
  Re-examined: **the event IS reachable** — the shipped surface produces it whenever a partner
  session touches a `{resources}` write, and the owner can cause one directly at any time. It is
  therefore **STILL-OPEN, not BLOCKED**; what it lacks is not a trigger but an *automatic* one,
  which is exactly why it is tagged field-contingent and does not gate. **If it survives a THIRD
  discharge run unfired, that is no longer a waiting state and the honest reading is that nothing
  will ever cause it — re-grade it BLOCKED and file it then.**
  **— ACCEPTANCE DISCHARGE 2026-08-31 (pass 3) — ⚠ BLOCKED (unreachable). OWNER-RULED. The third
  discharge run has come due and the tail is unfired.** `[field-contingent]`, so it does **NOT**
  gate — Cycle 14's closeout distance is unchanged by this grade.
  **The condition the pass-1 annotation set, verbatim:** *"If it survives a THIRD discharge run
  unfired, that is no longer a waiting state and the honest reading is that nothing will ever cause
  it — re-grade it BLOCKED and file it then."* Pass 1 (2026-08-27) graded it STILL-OPEN; pass 2
  (2026-08-27) left it untouched; this is the third run and it is still unfired. **The owner ruled
  the instruction honored.**
  **The event has still not occurred**, checked directly rather than assumed: no session record under
  `{field-vault}`'s `_agent/sessions/` from 2026-08-28 through 2026-08-30 contains a `{resources}`-write
  **legality question** (`grep -il "legality|write posture|escalat"` over that window returns
  nothing).
  **And ordinary activity of the surrounding kind HAS run, repeatedly, without reaching it.** Since
  the 0.17.1 upgrade `{field-vault}` has taken at least **eight `{resources}` writes** — five wiki
  pages rewritten by the 2026-08-30 sweep's own fixer, three brief issues written into
  `resources/briefs/` on 2026-08-31 — across partner sessions spanning the misc, extract, lint and
  groom lanes. The flow ran; the surface under test was never reached. That is the rubric's
  pass-through proof, on the second axis.
  **The finding, stated precisely.** Pass 1 was right that the event is *reachable*: the owner can
  open a partner session and pose the question at any time. It needs no **trigger** — it needs a
  **cause**, and nothing in a build, a release, an upgrade, or four days of ordinary vault use
  supplies one. The item concedes this itself, tagging the unbounded species at
  `brief-anatomy.md:203-210`. A check dischargeable only by staging its own evidence is not observing
  the field; it is asking the field to pose for it. **Cycle 14's own ruling D3-as-amended turns on the
  word *ordinary*** — a bound is *at rest, at the release gate, or on the next **ordinary** upgrade*.
  This check has no bound of any of those kinds **and** no ordinary occasion, and the brief vocabulary
  has no name for that species today.
  **Filed** as
  `factory/inbox/2026-08-31-104502-resources-write-legality-check-has-no-cause-and-survived-three-runs.md`
  — **factory-side signal** about how acceptance checks are written, not a module defect, cousin of
  platform **[P-20]**. Its candidate directions: name the third species in the brief vocabulary and
  forbid it; re-express the underlying question **at rest** against the bundle (which is gradeable and
  needs no partner to volunteer); or retire it, since its substantive premise — both blocking rulings
  shipped, the bundle no longer waiting on itself — is satisfied.
  **This ends the carry.** The tail does not go to `cycle-closeout` as a fifth carry-forward; it goes
  to `inbox-capture` as material.

### Build-5 (charter-membership-repair, briefed + built 2026-08-27) — the hot-fix's ledger

*Appended by build-5's record (`briefs/build-5-charter-membership-repair.md`). The repair of the
contradiction this cycle's own build-3 shipped in v0.17.0, filed
`factory/inbox/2026-08-27-171000-operational-record-class-has-two-memberships.md`, owner-ruled
hot-fix-now. Checks (1)-(4) are **ship-verifiable and GATE** per D3-as-amended; each names its seam
per R1. **All four were graded at rest during the build and all four PASS.***

**— ACCEPTANCE DISCHARGE PASS 2, 2026-08-27 (see §Acceptance-discharge run — pass 2 above):
(1)(2)(3)(4) DISCHARGED and TICKED; (5) STILL-OPEN; (6) FAILED.** Checks (1)–(4) were re-verified
independently at rest by this run against shipped source at `56cde45`/HEAD — not accepted on the
build's own say-so — and each is annotated with the re-verification below.

- [x] **build-5 (1):** `[ship-verifiable — GATES]` Every site in the shipped surface that
  enumerates the Layer-3 **operational-record class** names exactly `charter | record | register`.
  **Instrument:** the membership-agreement check — the comparison build-3's check (4) lacked, which
  tested single-home-ness (the class is *defined* once) and never compared *members*.
  **Seam crossed:** factory script → shipped governance bundle + `vlt-lint` references, at rest.
  **— GRADED AT BUILD 2026-08-27: PASS**, 10/10 enumerating sites agree. The check found a **sixth**
  site the filing had not (`vault-operating-contract.md:66`, the Layer-3 entry condition), which a
  site-list copied from the filing would have shipped still broken.
  **— DISCHARGED 2026-08-27 (discharge pass 2), re-verified at rest.** `grep -rn "operational.record"
  skills/` returns the enumerating sites, and each names all three members: `extraction.md:190`
  (*"`charter`, `record` and `register` — **all three**"*, the defining site), `extraction.md:84`
  (the closed recognized-`type:` set — the site whose disagreement was the defect),
  `write-verification.md:55` (*"`charter`, `record` or `register`"*), `vault-operating-contract.md:66`
  (*"`charter`/`record`/`register`"* — the sixth site the filing missed), `:70`,
  `checks.md:17` (*"`type: charter`, `type: record` or `type: register`"*), `checks.md:19`
  (*"`charter|record|register`"*), and `frontmatter.md:173` (*"`type: charter | record | register`"*).
  **Zero disagreeing sites.** The v0.17.0 contradiction (`:84` naming three, `:190` defining two) no
  longer exists.
- [x] **build-5 (2):** `[ship-verifiable — GATES]` Both moved conventions are bipartite-consistent
  in **both** directions, and no consumer still pins `extraction@8` or `write-verification@4`.
  **Instrument:** package-lint `E1` + `E5` + a stray-pin grep. **Seam crossed:** convention
  `consumers:` ↔ consumer `depends_on:`, including the asset-node half.
  **— GRADED AT BUILD 2026-08-27: PASS.** `write-verification` 4→5 (5 consumers re-acked),
  `extraction` 8→9 (4 re-acked); `frontmatter` deliberately held at 14 (not edited).
  **— DISCHARGED 2026-08-27 (discharge pass 2), re-verified at rest.**
  `uv run tools/package-lint.py --expect-version 0.17.1` re-run by this discharge run at HEAD:
  **`package-lint: A/B/C/E PASS, D PASS — vlt 0.17.1`, exit 0** — E1 and E5 clean over
  `write-verification@5` / `extraction@9`. Stray-pin grep for `extraction@8|write-verification@4`
  across `skills/`, `.claude/`, `tools/` returns **zero**; the two current pins appear **11** times.
  The same PASS line is recorded in release commit `56cde45`.
- [x] **build-5 (3):** `[ship-verifiable — GATES]` `vault-rule-card.md`'s `derived_from:` sha256
  equals the shipped contract's digest, the contract having been edited at `:66`.
  **Instrument:** package-lint `C6`. **Seam crossed:** derived artifact → its source contract.
  **— GRADED AT BUILD 2026-08-27: PASS** (re-stamped to `8f8a7116…`).
  **— DISCHARGED 2026-08-27 (discharge pass 2), re-verified at rest.** `shasum -a 256` over the
  shipped `vault-operating-contract.md` returns
  `8f8a71160253367d536a7995a7da5d5bb1426732875a6a8524864f3c747b9f20`, byte-for-byte the digest
  `vault-rule-card.md:11` carries in `derived_from:`. C6 PASS in this run's own package-lint.
- [x] **build-5 (4):** `[ship-verifiable — GATES]` No workflow body recites a stale convention pin
  after the `write-verification` bump. **Instrument:** package-lint `E7`. **Seam crossed:** workflow
  prose ↔ that file's own `// depends_on:` header.
  **— GRADED AT BUILD 2026-08-27: PASS.** `vlt-lint-full.js:684` recited `write-verification@4` and
  would have failed the release un-repaired — **E7 working as designed on its second release.**
  **— DISCHARGED 2026-08-27 (discharge pass 2), re-verified at rest.** E7 clean in this run's own
  package-lint (exit 0), and a direct read confirms `vlt-lint-full.js:684` now recites
  **`write-verification@5`** while `:11`'s `// depends_on:` header pins the same version; `:682`
  recites `frontmatter@14`, which did not move. No `@4`/`@8` token survives anywhere in the body.
- [x] **build-5 (5):** `[field-contingent]` — **does NOT gate.** On `{field-vault}`, after the
  v0.17.1 upgrade, the next full `vlt-lint` sweep reports the `charter` file **out** of
  `para_missing_attestation` jurisdiction: the unattested Layer-3 count outside `{wiki}` in
  jurisdiction falls **28 → 27**, both the `record` and the `charter` file exempted. **Event:** the
  owner runs `vlt-upgrade` to 0.17.1 then one `vlt-lint --full`. **Performer:** the owner.
  **Tagged field-contingent** because it needs a live corpus and an owner-initiated sweep — nothing
  in the build, release or upgrade causes it. This is the check that measures the defect's actual
  measured harm being undone, on the very file that surfaced it.
  **— ACCEPTANCE DISCHARGE 2026-08-27 (pass 2) — STILL-OPEN. ⚠ THE PREDICTED NUMBER IS MET, BY A
  DIFFERENT INSTRUMENT THAN THE CHECK NAMES, AND THAT IS NOT A DISCHARGE.**
  **The corroboration, recorded because it matters:** the 0.17.1 upgrade post-flight
  (`{upgrade_reports}/2026-08-27-1328-upgrade.yaml`, `parked_interims_review` park 2) re-measured the
  population and found **exactly what the check predicted** — 29 unattested `author: agent|hybrid`
  Layer-3 files outside `{wiki}` (`area` 22, `project` 3, `resource` 2, `record` 1, `charter` 1),
  *"the v5 exemption now covers `charter`, so **2 of 29 are exempt** where 1 was yesterday, and
  **27 remain in jurisdiction** (was 28)"*. Both the `record` and the `charter` file are exempted.
  The prediction **28 → 27** is met on the nose.
  **Why it is nevertheless not discharged: the check names its instrument and this is not it.** The
  check's event is *"the next full `vlt-lint` sweep reports the `charter` file **out** of
  `para_missing_attestation` jurisdiction"* — a **sweep**, reporting a **`para_missing_attestation`
  population**. The 27 came from an **upgrade post-flight** re-measuring *unattested Layer-3 files
  outside `{wiki}`* — a different instrument over a different population, computed by the upgrade's
  own park review rather than by the shipped check whose jurisdiction the repair narrowed. Nothing
  here observes `para_missing_attestation` actually declining to emit the `charter` file, which is
  the property the check exists to protect. **This is the identical distinction this ledger already
  drew for build-3 (7)** (*"the 29-file `type:` distribution already measured at the post-flight is
  **not** this check — it is an upgrade-side count over a different population"*), and grading (5)
  differently would make the ledger inconsistent with itself on the same evidence in the same week.
  The rubric's *never tick on "should be fine"* covers this exactly: a corroborating count from an
  adjacent instrument is not the named exercise. **The rubric offers no equivalent-instrument
  discharge and none is claimed here.**
  **Discharging event, unchanged:** one `vlt-lint --full` sweep on `{field-vault}` under **0.17.1**,
  in which no `type: charter` file appears under `para_missing_attestation` and the in-jurisdiction
  unattested Layer-3 count outside `{wiki}` reads **27**. **Trigger:** the owner, once, on
  `{field-vault}` — the **same sweep** build-3 (7) and build-4 (6) await, so **one owner act now
  discharges three checks** (and its successor discharges build-2 (8)). ⚠ That sweep is COLD by
  construction (0.17.1 moved two convention digests); coldness is not a finding.
  **First-exercise, not pass-through:** no sweep of the discharging kind has run since **any** of the
  three releases — `{lint_reports}` ends at `2026-08-27-1104-lint.yaml`, taken under 0.16.2 — so the
  tripwire does not fire.
  **— ACCEPTANCE DISCHARGE 2026-08-31 (pass 3) — DISCHARGED and TICKED. The named instrument ran and
  reads 27. ⚠ A caveat that must not be lost: this check could not have failed.**
  **Bound event occurred:** `{lint_reports}/2026-08-30-1123-lint.yaml` — a full `vlt-lint` sweep on
  `{field-vault}` under **0.17.1**, the exact instrument the check names and the one pass 2 refused to
  substitute for.
  **Both clauses hold on that instrument.** `flag_for_human.para_missing_attestation` reads **27** —
  the check's target number. No `type: charter` file appears in the population. Verified at rest
  rather than inferred: `{field-vault}` holds exactly **two** Layer-3 operational-record files,
  `projects/fantasy-2026/charter.md` (`type: charter`, `author: hybrid`, `created: 2026-08-23`) and
  `projects/fantasy-2026/record.md` (`type: record`, `author: hybrid`, same date), both unattested;
  27 in jurisdiction + those 2 exempt = the **29** the 0.17.1 post-flight counted. The two instruments
  now **agree**, where at 0.17.0 they disagreed (post-flight 28 vs sweep 27).
  ⚠ **CAVEAT — the TRANSITION the check names is not observable on the instrument it names, and the
  check would have read the same on a failed repair.** The check says the count *"falls **28 → 27**"*.
  On this instrument it did not fall: **the 2026-08-27 sweep — taken under 0.16.2, before either
  carve-out shipped — already read 27**, and says so itself (*"Count unchanged from the 2026-08-27
  sweep"*). The sweep's container-sited carve-out had **always** excluded both
  `projects/fantasy-2026/` files; the 28 was the post-flight's different population, computed a
  different way. So the sweep would have reported 27 whether or not build-5's repair worked. The
  endpoint is right, the two instruments now agree, and the property genuinely holds — but the check
  had **no state in which it could have reported failure**.
  **Recorded as [P-20] instance #5** — the check adversary: *name the property the check protects,
  then construct a state where the check PASSES and the property is VIOLATED.* Here the construction
  is trivial and real: the pre-repair vault. Added to P-20's evidence table. **No inbox filing is
  owed** — the module behaved correctly and the repair worked; the defect is in the check's choice of
  observable, which is factory-side and routes to the platform ledger.
  **Ticked on the check as written**, per the rubric's grade-the-check-as-written rule and the
  precedent build-3 (4) set in this same cycle — with the caveat above on record so a reader cannot
  mistake this tick for proof the repair was measured working.
- [ ] **build-5 (6):** `[field-contingent]` — **does NOT gate.** `{field-vault}`'s
  `write-verification.md` park resolves **fully** on the 0.17.1 upgrade — the *partial* resolution
  recorded on the 2026-08-27 discharge run (build-3 (6)) was blocked by exactly this contradiction.
  **Event:** the post-upgrade `parked_interims_review` shows the park unparked, not re-parked.
  **Performer:** the owner.
  **— ACCEPTANCE DISCHARGE 2026-08-27 (pass 2) — FAILED. The named event occurred and the evidence
  refutes the check.** `[field-contingent]`, so it does **not** gate; the cycle's closeout distance
  is unchanged by it.
  **What the evidence showed.** The bound event ran: `{field-vault}` took the 0.17.1 upgrade
  (`{upgrade_reports}/2026-08-27-1328-upgrade.yaml`). The check predicted the park would show
  **unparked**. `parked_interims_review` park 2 instead reads *"**STILL LIVE AND STILL UNRULED**, and
  THIS HOT-FIX MOVES ITS DENOMINATION … The park's substantive blocker is **UNCHANGED** for those 27:
  the ruling narrowed jurisdiction by artifact class only and **explicitly refused the partner-sitting
  reading the park rests on**, and the `verified_by` roster is **still unchanged at v5**. **The
  hot-fix moved exactly one file out of the population; it did not move the park.**"* The park was
  **RE-SURFACED, not unparked** — re-derived against the rules in force, as `vlt-upgrade` requires,
  and re-parked with its blocker intact for the remaining **27** files.
  ⚠ **PREMISE CORRECTION — RECORDED EXPLICITLY, BECAUSE IT MATTERS BEYOND THIS CHECK.** The check did
  not merely mis-predict; it rested on a **false premise about what blocked the park**, and the
  evidence refuting that premise was **already on disk when the check was written**. The check states
  build-3 (6)'s partial resolution *"was blocked by **exactly this contradiction**"* — the
  charter-membership defect. It was not. The **0.17.0** post-flight, written hours *before* build-5
  was briefed, already named the actual blocker: *"The ruling took the narrow-the-jurisdiction
  direction and narrowed it by **ARTIFACT CLASS ONLY** (`record`/`register`), **explicitly refusing
  the partner-sitting reading the park was built on** … So 28 of 29 remain in jurisdiction **with the
  roster unchanged**, and the park's substantive blocker **STANDS** for them."* The charter omission
  was **one file of 29**, named there as such. Curing it moved 1 file and could never have unparked
  the park, because the park rests on the `verified_by` **roster** question (upstream filing #16 /
  A14-7, `factory/inbox/2026-08-26-141418-layer-3-open-entry-vs-closed-verified-by-roster.md`), which
  v0.17.1 did not touch and v5 still leaves unchanged. **The refused partner-sitting reading is the
  blocker; the membership contradiction never was.**
  **The check tested what the fix does, not the property it claims to protect** — the fix exempts
  `charter`, so the check asked whether the park (which the fix does not reach) would clear. Stated
  as P-20's adversary question: *property* = the park's blocker is cleared; *passing-but-violated
  state* is unreachable here, but the inverse holds — **the property was already known unreachable by
  this fix when the check was written**, and the brief wrote the prediction from the fix's framing
  anyway. **This is a live, real-time instance of the failure mode opened the same day as
  [P-20] — the check adversary** (`factory/platform/roadmap.md` §P-20); it is that item's **fourth**
  recorded instance and **the first observed as it happened rather than reconstructed after the
  escape**. Added to P-20's evidence table in the same commit as this grade.
  **Filing disposition — NO inbox filing is drafted or owed, and this is a routing call, not an
  omission.** The rubric routes a FAILED item to `factory/inbox/`, which is the rail for **module**
  signal from a vault. There is no module defect here: v0.17.1 shipped exactly what it claimed, the
  membership is repaired at 10/10 sites (build-5 (1), discharged above), and `vlt-upgrade` behaved
  correctly by re-deriving the park against the rules in force instead of executing a stale exit.
  The defect is **factory-side, in how the check was written**, and off-cadence factory work routes
  to the **platform ledger**, not the inbox (`CLAUDE.md`, *the evolution lifecycle*). Its home is
  **P-20**, already open, and the instance is recorded there. The park's *own* substantive blocker
  already has an inbox home in the A14-7 filing above. ⚠ **If the owner disagrees with this routing,
  the filing to draft is a factory-method one and P-20 should absorb it rather than duplicate it.**
  **What the successor owes.** The park's resolution is the human's call — keep the hold, re-file, or
  resolve narrowly — and it is the **same tail already carried as build-3 (6)'s STILL-OPEN (b)**, now
  measured at **27** rather than 28. This FAIL adds no new field work; it retires a prediction that
  should never have been made.

## Roundtable review — A14-1..A14-8, the four-build batch (2026-08-26)

**Convened** over the filled Ideation rulings, before any brief, per `.claude/skills/vlt-lifecycle.md`
step 4. **`build-brief` gates on this section.** Session file:
`_output/party-mode/2026-08-26-cycle14-roadmap-roundtable-session.md`. Keepsake:
`_output/party-mode/2026-08-26-cycle14-roadmap-roundtable.html`.

**Roster — all 13 installed voices convened, none excused (owner call).** Discovered fresh by glob,
never recalled: Mary (analyst), Winston (architect), Builder, Amelia (dev), John (PM), Paige (tech
writer), Sally (UX), Carson (brainstorming), Dr. Quinn (problem-solving), Maya (design thinking),
Victor (innovation/disruption), Caravaggio (presentation), Sophia (storytelling). The owner named no
prior worries, so the roadmap's own five joints (§Next lifecycle move) were carried verbatim into
every persona prompt and are answered inline there.

**Six findings landed independently in four or more lanes** — the stale schema budget, the second
call site at `:664`, three-builds-in-`vlt-lint-full.js`, build-4's misplaced persist mandate, Q4's
missing discriminator, and D3's wrong axis. The moderator re-verified the three most consequential
in session (`PAGE_SCAN` = 3598 via package-lint's own `_E6_NODE_EXTRACTOR`; `attestationOnlyComplaint`
at `:630`/`:664`; `machine_tools` = four tools).

### Amendments applied (32)

| # | What it cures | Where it landed |
|---|---|---|
| **A1** | schema budget stale by 375 chars — build-1's ruled repair does not fit the hard E6 gate | §Questions left to brief time → build-1 |
| **A2** | `attestationOnlyComplaint`'s **second** call site at `:664` — unnamed anywhere in the batch | §Grouping → build-1 |
| **A3** | **build-3 also edits `vlt-lint-full.js`**; 7 in-prose pins E3 deliberately cannot see; 3 of them restate the rule Q4 amends | §Grouping → build-3; D2 |
| **A4** | build-2 `binds:` += Q1; "independent in substance" → **depends**; the interface stated | §Grouping → build-2 |
| **A5** | round-trip fixture: **three** runs, and the writer must be executable or the seam is uncovered | Q6 ruling 3 → build-2 |
| **A6** | Q6.1 covers **fresh AND reused** records | Q6 ruling 1 → build-2 |
| **A7** | component digests single-homed as executable steps, or half of Defect 2 survives | Q6 ruling 2 |
| **A8** | build-4's real file surface (`SKILL.md:74` is the persist home, not `report.md`) + `full-scale.md:13`'s silent wrong number | §Grouping → build-4 |
| **A9** | Q5's rationale rested on a **false premise** (`machine_tools` = 4, not 1; `uv` *is* the PEP 723 route) | Q5 |
| **A10** | build-4 **ships** the validation beat — "lets" is not "does" | §Grouping → build-4 |
| **A11** | Q4's class exemption needs a **mechanical discriminator** `vlt-lint` can evaluate, or reverts | Q4 |
| **A12** | the **transition** for the existing 27; and `contract:66` still demands the pair | Q4 |
| **A13** | Q3's pointer **target** is unsettled — and neither candidate is free | Q3 |
| **A14** | the shipped legal response excludes the blocked population (`research` is module-canonical, not vault-grown); park gets an unpark trigger | Q3 |
| **A15** | D2's narrowing **falsifies `extraction.md:188`** → 19 re-acks, not 15 | D2 |
| **A16** | `moc` recognized by a check and named in no convention | D2 |
| **A17** | **D3 rebuilt on BOUNDEDNESS** — as drafted it made fewer checks gate, not more | D3 |
| **A18** | D3's routing was untrue — **P-18 Tier C already exists**, precondition-blocked | D3 |
| **A19** | Q8/E4: the check must be able to **fail**, be a **specimen set** not a count, two instruments | Q8; E4 |
| **A20** | build-1 `binds:` += E4 (the only build-discharged debt, absent from every `binds:`) | §Grouping → build-1 |
| **A21** | **build-1 carries the check that re-grades Cycle 13 (2)** — release 1's whole purpose, unasked-for | §Grouping → build-1 |
| **A22** | a **`## Carried forward past Cycle 14`** section — 10 items, each with a bound | new section |
| **A23** | A14-2's filing pinned in the inbox against a **vacuous** Stage-5 move | §Grouping → where each went |
| **A24** | **two cycles open, `factory/CYCLE` holds one line** — the headless hazard | §Next lifecycle move |
| **A25** | "Cycle 12 can close" → **CLOSED**; its never-delivered hand-off inherited | §Next lifecycle move |
| **A26** | **two** cold sweeps, not one; the owed sweep moves to after release 2 | §Next lifecycle move |
| **A27/A28** | "seven filings" → eight (3 sites) + the admission arithmetic + the through-line's dropped **missing** case | §The through-line; §Owner ruling |
| **A35** | Q1's enum is **fail-CLOSED** where the mechanism it replaces was fail-OPEN — a fresh `ST-6` instance inside the gate-reopening build | Q1 ruling 1 |
| **A36** | §A14-7's "no study holds this cause" paragraph, superseded the same session by D4 | §Capture → A14-7 |
| **A37/A38** | build-1's retirement list completed (7 symbols + the 2 that must survive); `checks.md:15`'s second copy of the refuted claim | §Grouping → build-1 |
| **A39/A40** | `cache_rejected:` gives step 2's mandate its enforcement point; step 2's ordering clause retired with the composition move | Q6 |
| **A29–A34** | four drifted cites; §Spikes' truncated sentence; E4's round; E2 routed; E3's replacement fixture pair; E5's placeholder rule | various |

### Rules (2)

- **R1 — every brief states, per ship-verifiable check, WHICH SEAM its named instrument actually
  crosses.** *Home: `build-brief` (`references/brief-anatomy.md`, the tag section).* **Interim
  posture:** the home edit is a platform-channel change and cannot ship in this cycle, so R1 is
  **declared here and binds every Cycle 14 brief** via D3's amended text. It is the clause that
  reaches b2(5), which D3 alone does not (A17b).
- **R2 — P-18 Tier B's opening trigger gets an observer.** Its stated condition — *"a build with no
  prior failure behind it reaches brief-time and reaches for a synthetic fixture unchallenged"* —
  **is met by builds 3 and 4 and names no site obliged to evaluate it.** *Home:
  `factory/platform/roadmap.md` P-18.* **Interim posture:** if build-3's or build-4's brief reaches
  for a synthetic fixture, the brief records it in `status:` and it is named at closeout.
  **Observation duty, never a gate.**

### Disputes — owner-ruled live, dissents on record

- **`:159`/`:168`** — three-way split. **RULED: retire `:159`, keep `:168`.** `:159`'s route becomes
  unexpressible under an enum and its 208 chars are load-bearing against E6; `:168` guards
  `unmarked_supersession`, which Q1 does not structure and whose reduce-side guard build-1 removes —
  **not defence in depth, the only depth.**
  **DISSENT (Victor, Amelia):** `vlt-lint-full.js:551-557` records that prohibition as
  **field-refuted** (Cycle 12 shipped it; the next two sweeps reported the defect unchanged), and D1
  rules this same cycle that a schema description is never an enforcement point. **Deferred, not
  resolved — carried at item 9 of §Carried forward.**
- **Cycle scope** — **RULED: the four-build / two-release shape HOLDS**; the added surface is
  brief-time scoping, not a re-cut. **Builder's 19-re-ack re-pricing is NOT waived** (A15).
- **Carson's per-page scalars** — **RULED: Q1's deferral STANDS**, build-1 is the critical path and
  over budget. **The premise is corrected on the record** and both cheap routes are named for the
  successor (§Carried forward items 1–2).
- **Q5's premise** — **RULED: the `.json` direction STANDS on a corrected reason.** The
  stdlib-asymmetry argument is struck as factually false (A9).
- **D3 as a pointer** (John) — **NOT taken**; kept as a cycle-scoped tagging instruction that now
  *cites* rather than restates. **Dissent recorded** at D3.

### Obsolescence beat (P-15) — MANDATORY, and it ran

**Every persona ran it; every one returned an answer. Four retirements found, three negatives
returned explicitly.** This is the first cycle in eleven to retire anything — and the file already
knew: `vlt-lint-full.js:551-557` records the `:159`/`:168` prohibition as field-refuted eleven lines
above the guard built to supersede it.

**Retirements landed:**
1. **`vlt-lint-full.js:159`** — superseded by build-1's structured `PAGE_SCAN` return (the enum's
   range excludes the route rather than forbidding it in prose). **Landed:** build-1's block.
2. **The residue-rule apparatus** — `parseClaim` (`:593-603`), `fieldsNamed` (`:605`),
   `KNOWN_FRONTMATTER_BY_LENGTH` + its comment (`:580`/`:579`), `normalizeClaim` (`:584`),
   `claimWords` (`:585`), `CLAIM_FILLER` (`:589`), and **the `frontmatter_issue` free-text slot
   (`:163`)**. The roadmap named two of these; the room named all seven, plus the two symbols that
   must **survive**. **Landed:** build-1's block (A37).
3. **`checks.md:15`** — the same refuted safety claim in the **vault-facing** catalogue, which Q7
   would have left standing. **Landed:** build-1's block (A38).
4. **`full-scale.md` step 2's *"a digest over, in this order"* ordering clause** — superseded by
   build-2's in-workflow composition; left standing it re-creates A14-8's exact shape.
   **Landed:** Q6 (A40).
5. **`frontmatter.md:71`'s open-vocabulary clause, for the PARA population** — D2 performed this
   narrowing and did not record it as a retirement. **Landed:** D2, named.
6. **§A14-7's "no study holds this cause" paragraph** — superseded the same session by D4's opening
   of `ST-6`, and it sits in the section E5 orders build-3's brief to write from. **Landed:** A14-7
   (A36).

**Negatives returned explicitly, so the beat is answered rather than silent:**
- **`vlt-lint-full.js:168` — NOT superseded** (Winston, Carson, Paige, Sophia; owner-ruled). Kept,
  with dissent.
- **Every shipped `verbatim:` marker — NOT retirable** (Victor, having checked `:152`–`:171`). Each
  is an instruction about what the scanner must *return*; no build displaces one. *"Retiring markers
  wholesale would be the tidiness, not the retirement."*
- **D5's two re-confirmed rejections — nothing to retire** (Victor). Both are of directions **never
  built**; a rejection of an unshipped direction has no site.
- **`full-scale.md` step 4's version-skew refusal — NOT superseded** (Amelia, Caravaggio, Paige). It
  detects a stale vault-local workflow copy, a failure the round-trip check cannot observe. **Q6's
  decline stands on a real distinction.** *(Victor's related finding — that step **2** is the other
  silencer and IS made redundant — landed instead as the `cache_rejected:` amendment, A39.)*
- **`report.md:3` — rewritten by Q5, not retired.** The strictness survives; only the format
  monopoly goes.

### Out of scope, filed rather than debated (capture-don't-interrupt)

- **E2's *"frontmatter is the source of truth"* qualifier** → `factory/inbox/` as a `pattern`
  against `write-verification.md`'s tier-1 item (owner action; A32).
- **Three `cited_by:` appends** — `ST-1` (Q4 rests on *permission fused to provenance* by name),
  `ST-3` (A14-8 attributes Defect 2 to it by name), and `ST-6` (its own **instance 2**, the
  2026-08-21 decision-log filing still in the inbox — whose later capture would otherwise re-derive
  the cause D4 opened `ST-6` to prevent). *(`ST-2` and `ST-5` already carry their Cycle 14 entries.)*

**OPEN DISPUTES: none.** All four were owner-ruled live; two dissents are on record and one is
carried as a live item.


### Build-6 (declared-typed-subtree, briefed 2026-09-01) — ⚠ WITHDRAWN 2026-09-01, ALL 6 CHECKS STRUCK

⚠ **The build was withdrawn before any code was written, owner-ruled, and its six checks are STRUCK —
they gate nothing and are not counted in any tally.** Superseded by
`factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md`,
the first use of P-15's `supersession` class.

**Why, in one line:** the build asked for a **new mechanism** where the honest ask was a
**retirement** — and its own minimal-scope ruling cut out the `{wiki}` unification, the half that
would have made it a category rather than an allowlist entry. That is `ST-2`'s RC2 reproduced inside
Cycle 14: *"the minimal patch [is] the rational move every time — which is exactly how a root cause
survives four cycles."* `ST-2` is `status: standing`; Cycle 12 retired the location proxy for
`author:` and `trust:` and left it standing for `type:`; **Cycle 14 build-3 (`e42429d`) then restated
and strengthened it.**

**Nothing shipped.** No commit, no version bump, no handshake — `extraction.md` stays at `version: 9`
and `vault-operating-contract.md` is untouched. **The checks below are retained struck, not deleted**,
so the record shows what was asked and withdrawn rather than showing nothing at all.

⚠ **One check is worth carrying forward to whatever build the supersession produces:** the struck
check (4) required a **mandatory control** — a different non-PARA `type:` in the same subtree must
still report — because a check that only watches findings disappear cannot tell a working declaration
from a disabled net. That is [P-20]'s question answered at brief time, and it survives the
withdrawal as a design requirement even though the build does not.


*Appended by build-6's brief (`briefs/build-6-declared-typed-subtree.md`). Owner-ruled hot-fix over
`factory/inbox/2026-08-31-152000-…`, a defect shipped by this cycle's own **build-3** (`e42429d`,
v0.17.0) — **the second defect in the same `extraction.md:84` statement**, after build-5 repaired the
first. Checks (1)–(5) are `[ship-verifiable]` and **GATE** per D3-as-amended; (6) is
`[field-contingent]` and does not. Scope owner-ruled **MINIMAL**: the module-vocabulary prohibition
gains a subtree qualifier; unifying `{wiki}` into the mechanism is **OUT** and goes to Cycle 15.*

- [~] ~~**build-6 (1):**~~ ⚠ **STRUCK — build WITHDRAWN 2026-09-01.** Original text: `[ship-verifiable — GATES]` Both prohibition sites carry the subtree qualifier
  and state the scoping **in words** — `extraction.md:84` and `vlt-lint/references/checks.md:19`.
  **Instrument:** `grep -rn "never to declare module vocabulary\|never overlay-declare module vocabulary" skills/`
  returning both sites, plus a read of each. **It can fail:** one site qualified and the other not —
  which would reproduce the two-memberships defect build-5 just fixed, in the same file. **Seam:**
  module source agreement across two files.
- [~] ~~**build-6 (2):**~~ ⚠ **STRUCK — build WITHDRAWN 2026-09-01.** Original text: `[ship-verifiable — GATES]` The declaration's mechanics are stated in
  `extraction.md` and **nowhere else**; `checks.md:19` cites without restating (it already says the
  set is *"defined in `extraction.md` … which is its single home; named here for the reader only"*).
  **It can fail:** a second statement of the declaration's shape anywhere in `skills/`. **Seam:**
  single-home discipline.
- [~] ~~**build-6 (3):**~~ ⚠ **STRUCK — build WITHDRAWN 2026-09-01.** Original text: `[ship-verifiable — GATES]` `extraction@10` **bipartite-consistent both
  directions** across exactly **4** consumers (`vlt-extract`, `vlt-lint`, `vlt-track`, `vlt-query`),
  and `uv run tools/package-lint.py --expect-version 0.17.2` exits **0** with both version strings
  bumped and **E7 clean**. **Seam:** convention → consumer ack. **Evidence:** the handshake count +
  the PASS summary line in the release commit.
- [~] ~~**build-6 (4):**~~ ⚠ **STRUCK — build WITHDRAWN 2026-09-01.** Original text: `[ship-verifiable — GATES]` **bounded to a SCOPED `vlt-lint` run over the
  declared subtree — NO full sweep.** With `{briefs}` declared, the 8 brief issues **leave
  `para_type_unknown`** — **and a control file carrying a different non-PARA `type:` in the same
  subtree still reports.** ⚠ **The control is MANDATORY and the check fails without it:** a check
  that only watches findings disappear cannot tell a working declaration from a disabled net.
  **This is [P-20]'s question asked at brief time rather than discovered afterward — the first check
  in this cycle written that way.** **Event:** the owner declares `{briefs}` in
  `{overlays}/extraction.overlay.md`, then runs a **scoped** `vlt-lint` covering `resources/briefs/`.
  **Performer:** the owner.
  ⚠⚠ **CORRECTED 2026-09-01 — this check was first bound to a full sweep and that was a COST ERROR.**
  `checks.md:19` puts the `para_*` closing nets in **both modes**, and `vlt-lint/SKILL.md:41` defines
  *"every PARA file"* as *"the PARA members of the scoped set in scoped mode."* The 146-agent fan-out
  scans **`{wiki}`**; `resources/briefs/` is PARA, **outside** `{wiki}`. A scoped run exercises this
  check exactly. ⚠ **The same error is on record twice already this cycle** — build-3 (7) and
  build-5 (5) are both `para_*` checks that were bound to full sweeps they never needed. **Three
  forced full sweeps, none of which the population required.**
- [~] ~~**build-6 (5):**~~ ⚠ **STRUCK — build WITHDRAWN 2026-09-01.** Original text: `[ship-verifiable — GATES]` **bounded to the same scoped run.** The loosening
  is **scoped**: a file carrying `type: research` at a PARA address **outside** any declared subtree
  still reports `para_type_unknown`. **It can fail:** the declaration leaked to the whole population.
  **Seam:** declaration scope → check population. Extend the scoped set to that control's address;
  still no full sweep.
- [~] ~~**build-6 (6):**~~ ⚠ **STRUCK — build WITHDRAWN 2026-09-01.** Original text: `[field-contingent]` — **does NOT gate.** Park **#15** unwinds: re-derived
  against **v10** and resolved by a superseding decision-log entry, the vault executing a legal
  response (**declare the subtree**) **without writing anything false**. ⚠ **This is the clause
  build-3's check (6) has been structurally unable to reach.** Tagged field-contingent because
  nothing in the build, release or upgrade causes an owner to write a log entry. ⚠ **Do NOT
  pre-draft the unwind** — the v4 parked-interim rule requires re-derivation against the rules in
  force **at unwind time**; a pre-authorized sequence is the failure that broke park #11.

## Next lifecycle move — historical record

*(Demoted 2026-09-01 per `vlt-lifecycle.md`'s foot rule. Everything in this section is
**superseded routing**, preserved for history. **The authoritative Next lifecycle move is the
LAST block of this file, below.**)*

**Historical — the routing that stood at code-complete, before closeout (2026-09-01).**


*(Restamped 2026-09-01 — `acceptance-discharge` pass 3 and its three rulings (2026-08-31), then
park 1's re-derivation and the build-6 ruling (2026-09-01). Prior routing preserved below.)*

**Tally: 36 checks in 6 items — 32 DISCHARGED · 3 FAILED · 0 STILL-OPEN · 0 SPLIT · 1 BLOCKED.**
*(Updated 2026-09-01 pass 5 — build-3 (6)'s SPLIT resolves to **FAILED**. Every check in the cycle is
now graded: nothing STILL-OPEN, nothing SPLIT, nothing predicted.)*

**⚠ Cycle 14 closes on ONE gating FAIL: build-3 (6) — graded, not expected.** Park #16 re-parked in
the log (vault `307c901`; both halves verified in-vault by this run at `decision-log.md:1259` and
`:1446`), park #15 remains **live and un-superseded**, and `para_type_unknown`'s legal response was
not executed. All three clauses unmet — and the FAIL is the honest outcome, because **a green was
available only by falsifying a `type:` field.** The vault re-derived both parks, found one of the
rules itself defective, and filed for its retirement rather than executing an exit it believes false.
That is `decision-log.md` v4's mechanism working as intended.
*(Updated 2026-09-01 pass 4 — build-2 (8) DISCHARGED. **No STILL-OPEN check remains in the cycle.**)*

**⚠ THE CACHE HIT — the longest-standing defect in the register is closed.** The second consecutive
sweep (`{lint_reports}/2026-09-01-1406-lint.yaml`, run by a peer session, **re-verified here against
the persisted report**) read `files_cached: 141` / `files_checked: 5` / `cache_rejected: 0` under the
**same fingerprint the 2026-08-30 sweep wrote** — *"WARM - the first warm run this vault has
recorded."* The findings cache shipped in Cycle 12, was refuted as **b2(5) — "has never once
worked"** — and rebuilt as Cycle 14 build-2. **First observed working in three cycles.**
**Build-2's item TICKS at 8/8.** Cost effect, the direct answer to the owner's objection: scan-page
agents **146 → 5**, prompt chars **591,152 → 20,294**, dispatches **172 → 31** — **96% off the scan
phase.**
⚠ **And the caveat is large enough to be its own filing:** the run's **first attempt was cold and was
discarded** — `full-scale.md` step 2 specifies its two *digest* slots exactly and its two *component*
slots not at all, and both were read defensibly and wrongly. Only hand-debugging made it warm.
**This plausibly explains the three-cycle failure the check was written to end.**

**Four filings added 2026-09-01** (one written before the sweep, three from it):
`2026-09-01-093000` (the fingerprint is **over-broad** — `module_version` forces a cold sweep every
release), `2026-09-01-140600` (the fingerprint's inputs are **under-specified** — a defensible reading
fails **silently**; a different cause and a different fix from `093000`, and capture may brief them
together), `2026-09-01-140601` (same-page heading anchors reported as missing targets — second
consecutive sweep, cause now diagnosed), `2026-09-01-140602` (a scanner **substituted a proper noun**
and, on the second occurrence, **served it from the cache** — a scanner error is now permanent for the
life of the sidecar). ⚠ Filing `2026-08-31-104500` was **corrected**: instance (a) recurred, (b) and
(c) did not — the render is **intermittently** wrong, which is a stronger claim than consistently
wrong, not a weaker one.

**⚠⚠ BUILD-6 WITHDRAWN 2026-09-01 — owner-ruled, before any code was written. All 6 checks STRUCK.**
Superseded by
`factory/inbox/2026-09-01-160000-supersession-the-para-type-enum-is-locations-last-proxy-for-trust.md`
— **the first use of P-15's `supersession` class**, a rail built 2026-08-25 for exactly this and
unused for a week while the thing it was built for happened again.

**What the withdrawal is about.** The friction behind park #15 is not a defect in a clause; it is
`ST-2` (*location as proxy for trust*, `status: standing`). Cycle 12 retired that proxy for `author:`
and `trust:` and left it standing for **`type:`** — and Cycle 14 **build-3 (`e472429d`… `e42429d`)
restated and strengthened it**, six days after `ST-2` opened. Build-6 answered that with a **new
mechanism** and an explicit **minimal-scope ruling that cut out the `{wiki}` unification** — the half
that makes it a category rather than an allowlist entry. `ST-2` RC2 names the trap precisely: *"the
repo's own governance quality biases toward perimeter patches … the minimal patch [is] the rational
move every time — which is exactly how a root cause survives four cycles."*

⚠ **Nothing shipped.** No commit, no version bump, no handshake; `extraction.md` stays at `version:
9`. The brief is **retained unbuilt as a worked negative** at
`briefs/build-6-declared-typed-subtree.md` — its grounding is sound and reproduced in the filing;
what was wrong is the **shape of the ask**.

⚠ **Filing `2026-08-31-152000` is superseded too** and should be withdrawn at capture — it reported
the same friction as a defect and proposed a carve-out. *"A filing that ends in a new carve-out has
diagnosed the symptom"* (`inbox/README.md`).

**Consequence for the cycle, stated plainly:** build-3 (6) reverts to an **expected gating FAIL** —
park #15 does not unwind, because under v9 both of its legal responses require writing something
false. **Cycle 14 closes on one honest gating FAIL**, and the structural retirement goes to **Cycle 15
ideation**, where the roundtable's **obsolescence beat** (P-15's other half) is the beat built to
receive it. That is the trade `ST-2` already priced: *"B fixes today's problem; C fixes the class."*

*(Superseded, retained for the record — the ruling this replaces:)*
**OWNER-RULED 2026-09-01: BUILD-6, a hot-fix, rather than carrying the defect to Cycle 15.**
Park 1's re-derivation found the ruling it waited on defective — and `git log -S` established that
**this cycle's own build-3 shipped it** (`e42429d`, v0.17.0), making this the **second** defect in the
same `extraction.md:84` statement after build-5 repaired the first. The build-5 precedent therefore
governs: repair it in-cycle. **Scope owner-ruled MINIMAL** to stay inside the cycle's debt-clearing
ruling — the module-vocabulary prohibition gains a **subtree qualifier**; unifying `{wiki}` into the
mechanism is **OUT** and goes to Cycle 15 ideation on the filing (which stays live).

**Briefed:** `briefs/build-6-declared-typed-subtree.md`; 6 acceptance checks appended to the ledger
above (5 gating, 1 field-contingent). **Release v0.17.2, cut alone.**

~~**This changes build-3 (6)'s expected outcome from FAILED to PASSABLE.**~~ ⚠ **REVERSED by the
withdrawal — build-3 (6) is again an expected gating FAIL.** The superseded reasoning: Under v10 park #15 has a
legal response that requires writing nothing false — declare the subtree — so it can genuinely unwind
and the cycle can close on a discharge rather than a deliberate gating FAIL. ⚠ **Expected, not
assured:** (6) is graded once, whole, on the owner's acts, and both parks' entries are still
unwritten.

**Next lifecycle move: run `cycle-closeout`.** Park #16's disposition **landed 2026-09-01** (vault
`307c901`), build-3 (6) is **graded FAILED**, and **every check in the cycle is now graded** — nothing
STILL-OPEN, nothing SPLIT, nothing awaiting an event. Closeout rules one gating FAIL and closes.

⚠ **Two things owed that closeout should see, neither blocking it:**
- **Neither supersession filing is posted through `vlt-feedback`**, so park #16 references no live
  tracker issue the way #15 and #16 do — its entry says so. `vlt-feedback` is invoked-only and needs
  the **owner's** explicit go; deliberately not taken by any agent.
- **Park #15 is still live in the log** and will surface on every `vlt-upgrade` until Cycle 15's
  retirement lands. That is correct — it is genuinely still held.

⚠ **Park #15 is NOT worked in this cycle.** Its retirement is
`factory/inbox/2026-09-01-160000-supersession-…` and it goes to **Cycle 15 ideation**, where the
roundtable's **obsolescence beat** — the half of P-15 that has never been exercised — is the beat
built to receive a retirement. Working it here would be a fifth perimeter pass.

1. **The parks (the move — both are owner acts, no build and no release).**
   - ⚠ **(a) `extraction.md` — RE-DERIVED 2026-08-31; it does not unwind under v9, and BUILD-6 is
     the answer.** It unwinds **after v0.17.2 ships**, by declaring `{briefs}` as a typed subtree —
     a legal response that writes nothing false. ⚠ **Do NOT pre-draft that entry**: the v4
     parked-interim rule requires re-derivation against the rules in force **at unwind time**, and a
     pre-authorized sequence is the failure that broke park #11. The re-derivation record: The ruling it waited
     on landed and the re-derivation found the ruling defective: `extraction.md:84` removes the
     `{wiki}` subtree from the PARA population **by name**, so `resources/wiki/`'s **146 files
     carrying `type: wiki`** are legal while `resources/briefs/`'s identically-shaped 8 are a finding
     forever — *"one carve-out by name"* (`contract:70`) is a completeness-claiming list of one, and
     it fell behind an addition. Both stated legal responses require writing something false, and the
     vault **already refused this exact move once** in park 2, a refusal `write-verification.md:55`
     v5 then ratified. **Filed
     `factory/inbox/2026-08-31-152000-para-type-carve-out-is-an-enumeration-of-one-and-penalizes-accurate-vocabulary.md`.**
     **The owner act is now a superseding `parked-interim` entry against the NEW filing** — a park
     with a correct premise, replacing the hold against #15. Population refreshed **5 → 8**; the
     growth rate the park priced has fired once, on schedule.
   - **(b) `write-verification.md`** — 27 files in jurisdiction. ⚠ The blocker is the **refused
     partner-sitting reading and the unchanged `verified_by` roster** — **NOT** the charter-membership
     contradiction, which v0.17.1 already fixed. Widening the roster is a Cycle 15 build, so the
     realistic disposition is **keep the hold with a stated exit condition**, which the check accepts:
     it asks for the park's disposition, and a deliberate hold discharges it as honestly as an unwind.
2. **Then `cycle-closeout` — build-3 (6) is now PASSABLE, not an expected FAIL** (build-6 gives park
   #15 a legal response). The earlier reading, superseded, was: The check
   requires both parks *"re-derived … **and unwound**"* plus the legal response executed on a named
   file; under (a)'s disposition it is re-derived but not unwound and the response is not executed.
   **That is the honest outcome — the check fails because the module is wrong, which is what an
   acceptance check is for.** The alternative is retyping 8 files to a value the vault believes false
   in order to turn a gate green, which is the failure mode this cycle is named for. So Cycle 14
   closes on **one gating FAIL, deliberately** — the same posture already taken for build-4 (1) and
   build-1 (6). Its carry-forward list, already determined:
   - **build-1 (6)** — FAILED, **bound debt to Cycle 15, ship-verifiable so it GATES there.** Bound is
     leg 3 alone, graded on the first full sweep after the Cycle 15 release, corpus identity recorded.
   - **build-2 (8)**, **build-5 (6)**, **Cycle 12 b3(7)** — `[field-contingent]`, never gated.
   - **Four filings to `inbox-capture`**: `2026-08-27-153000`, `2026-08-27-160000`,
     `2026-08-31-104500`, `2026-08-31-104501`. ⚠ **None was withdrawn by the rulings** — three of them
     are the diagnoses *underneath* items just discharged or carried. **The gate moved; the module did
     not.** (`2026-08-31-104502` is factory-side, routing to the brief vocabulary.)
3. **Independently, and worth doing before anything ships: a SECOND `vlt-lint --full`.** It discharges
   build-2 (8) (non-gating) — the first exercise the cache reader has ever had — **and** it adds a
   second member to build-4 (1)'s post-mandate population, which is currently **one report**. ⚠ **Take
   it BEFORE any release**: a release moves the ruleset fingerprint and forfeits the warm sweep, and
   the `stubSlugs` repair the sweep itself asks for **is** a release. Expect `files_cached ≈ 141` /
   `files_checked ≈ 5`; the bar is `> 0`, not 146.
4. **Cycle 13's acceptance re-run,** then its closeout — independent of all of the above; its gate is
   open on build-1 check (2).

⚠ **The ruling most likely to be revisited: build-4 (1).** It is the only one of the three resting on
a contested reading rather than on new measurement alone — under the check's literal population 1 of
7 archived reports still fails, and this roadmap says two different things about who may narrow the
subject (both quoted at the annotation). **If closeout disagrees, reopening it restores one gating
FAIL and touches nothing else** — build-3 (7)'s substitution and build-1 (6)'s bound debt do not
depend on it.

⚠ **`factory/CYCLE` reads `14-no-enforcement-point` and TWO cycles are open.** Hand-point it at
`13-trusted-returns` before running either cycle-scoped skill against Cycle 13 and restore it
immediately after. **Never headless while that is true** (A24).

**Two platform-side signals from pass 3, neither owed a module filing:** **[P-20]** gains instance
**#5** (build-5 (5) discharged while structurally unable to fail), and **[P-19]** gains its **first
field instance** (build-1 (6)'s specimen set returned two different answers on the same bytes three
days apart — the reason that check is carried as debt rather than hot-fixed).

---

**Historical — the routing that stood between pass 3 and the rulings (2026-08-31).**

**ACCEPTANCE PASS 3 COMPLETE — 2 DISCHARGED, 2 BLOCKED, 1 STILL-OPEN, 1 refresh. Cumulative across
three passes: 36 checks — 29 DISCHARGED · 3 FAILED · 1 STILL-OPEN · 1 SPLIT · 2 BLOCKED. Cycle 14
CANNOT CLOSE, and the gate got one item longer, not shorter.**

**Next lifecycle move: run `inbox-capture`** — three filings were filed this run and two of them are
the only route by which a gating item can clear.

1. **`inbox-capture` (the move).** Three new filings await capture, all owner-confirmed:
   - `2026-08-31-104500-rendered-lint-report-is-never-checked-against-its-own-mandated-shape.md`
     — ⚠ **the one that gates.** Build-3 (7) is graded **BLOCKED (unreachable)** because the sweep
     renders `para_missing_attestation` as a rollup where `report.md:32` mandates a per-file list,
     and no shipped surface produces the `type:` distribution the check names. `[ship-verifiable]`,
     so it **GATES**. Only a repair (or an owner ruling at closeout) clears it; waiting cannot.
   - `2026-08-31-104501-stub-discovery-regex-drops-the-stub-list-and-manufactures-missing-targets.md`
     — ⚠ **capture must ground the exact `file:line`**; this rests on the sweep's own diagnosis.
   - `2026-08-31-104502-resources-write-legality-check-has-no-cause-and-survived-three-runs.md`
     — factory-side; the inherited Cycle 12 b3(7) tail, **BLOCKED and filed rather than carried a
     fourth time**. Non-gating.
2. ~~**A second `vlt-lint --full` on `{field-vault}`**~~ — **DONE 2026-09-01, and it DISCHARGED
   build-2 (8).** ⚠ Retained note for the next release: a release moves `module_version`, which is a
   fingerprint slot, so **the next full sweep after v0.17.2 is cold by construction.** The 2026-08-30 sweep
   wrote the sidecar for the first time (`_agent/lint-cache.json`, fingerprint
   `31f40c2cc90313a41dd3|bd6e1e211804a2011af`, 146 records — the write leg is field-confirmed at
   last), so the reader can finally be exercised; but a release moves the ruleset fingerprint and
   forfeits the warm sweep, and the stubSlugs repair above is a release. Expect
   `files_cached ≈ 141` / `files_checked ≈ 5` — the 2026-08-30 run wrote five wiki pages — and note
   the bar is `> 0`, not 146.
3. **The two parks' unwind** (build-3 (6) SPLIT) — unchanged and still the human's call:
   (a) `extraction.md`'s park needs a superseding decision-log entry through the rostered write
   route; (b) `write-verification.md`'s park is intact for 27 files, its blocker the **refused
   partner-sitting reading and the unchanged `verified_by` roster** — *not* the charter-membership
   contradiction, which v0.17.1 already fixed.
4. **Then `cycle-closeout`, which must rule THREE gating items** (was two): **build-1 (6)** FAILED
   — and note the refresh, the specimen set is now known **not reproducible** on an unchanged
   corpus; **build-4 (1)** FAILED, owner-ruled kept; **build-3 (7)** BLOCKED, new this run.
5. **Cycle 13's acceptance re-run,** then its closeout — independent of all of the above; its gate
   is open on build-1 check (2).

⚠ **`factory/CYCLE` reads `14-no-enforcement-point` and TWO cycles are open.** Hand-point it at
`13-trusted-returns` before running either cycle-scoped skill against Cycle 13 and restore it
immediately after. **Never headless while that is true** (A24).

**Two platform-side signals recorded this run, neither owed a module filing:** **[P-20]** gains
instance **#5** (build-5 (5) discharged while structurally unable to fail — the pre-repair vault
reads the same 27), and **[P-19]** gains its **first field instance** (build-1 (6)'s specimen set
returned two different answers on the same bytes three days apart).

---

**Historical — the routing that stood before pass 3 (2026-08-27).**

**ALL FOUR BUILDS SHIPPED — the cycle is code-complete. Two independent tracks remain, neither
waiting on the other.**

1. **Acceptance (both releases at once):** the owner runs `vlt-upgrade` on `{field-vault}` for
   v0.17.0, then `run acceptance discharge`. Outstanding field-bound checks: build-1 (6)/(7)
   — *evidence already exists* in the 2026-08-27 post-v0.16.2 sweep and is dischargeable now —
   plus build-3 (6)/(7), build-4 (6), and build-2's field-contingent (8), which needs **two
   consecutive sweeps under an unchanged ruleset** (A26: pay `{field-vault}`'s owed complete sweep
   on the SECOND sweep after this release, not the first).
2. **Cycle 13's acceptance re-run,** then its closeout. Build-1's check (2) re-graded its refuted
   check PASS at rest on six real subjects, so its gate is open.

⚠ **`factory/CYCLE` reads `14-no-enforcement-point` and TWO cycles are open.** Hand-point it at
`13-trusted-returns` before running either cycle-scoped skill against Cycle 13 and restore it
immediately after. **Never headless while that is true** (A24).

⚠ **Build-4's check (1) is graded FAILED and it GATES** — owner-ruled 2026-08-27: keep the honest
FAIL, do not re-scope a check after it fails. Its subject going forward is reports written *under*
the mandate; the re-grade belongs to `acceptance-discharge`. The unparseable archive report is
filed (`factory/inbox/2026-08-27-153000-…`) and was not repaired.

*(Superseded 2026-08-27: this line previously routed to `brief build 2`. **Release 2 SHIPPED —
v0.17.0 @ `c02fe3d`, tag `v0.17.0` (`b3c8646`), pushed.** Builds 2, 3 and 4 all BUILT; at-rest
acceptance 7/7, 5/5 and 4-of-6 respectively.)*

---

**Historical — the routing that stood between release 1 and release 2.**

1. **Release-1 acceptance:** the owner runs `vlt-upgrade` on `{field-vault}`, then
   `run acceptance discharge`. Build-1's checks **(6)** and **(7)** are bound to that first live
   full sweep; the other six are graded at rest and PASS.
2. **Toward release 2:** ~~`brief build 2`, then builds 3 and 4~~ → **`brief build 4`**.
   *(Superseded 2026-08-27: **build-2 is BRIEFED and BUILT @ `d641050`**; **build-3 is BRIEFED** —
   `briefs/build-3-governance-handshake.md` — and awaits a fresh builder session. A3's ordering
   constraint was honoured: build-3's re-ack pass was written against post-build-1, post-build-2
   source, `PAGE_SCAN` measured settled at 3688. Build-4 is the release build and carries the dual
   version bump + the `--expect-version` gate.)*

⚠ **Before running `acceptance-discharge` or `cycle-closeout` against CYCLE 13, hand-point
`factory/CYCLE` at `13-trusted-returns` and restore it immediately after** — two cycles are open
and the pointer holds one line (A24, restated at the foot of this roadmap). Never run either headless
while that is true.

*(Superseded 2026-08-27: this line previously routed to `brief build 1`. **Build-1 is BRIEFED, BUILT
@ `ceb5cb2`, and RELEASED as v0.16.2 @ `bd985a6`, tag `v0.16.2` pushed to origin.** Its check (2)
re-graded Cycle 13's refuted acceptance check on six real vault subjects: **PASS — Cycle 13's
closeout gate is REOPENED.**)*

---

**Historical — the routing that stood until release 1.** ✅ **The roundtable CONVENED 2026-08-26 and its record is
above** (§Roundtable review — A14-1..A14-8, the four-build batch): 32 amendments applied, 2 rules
declared, 4 disputes owner-ruled live with 2 dissents on record, **no OPEN disputes**, and the
obsolescence beat run to 6 retirements and 5 explicit negatives. `build-brief`'s gate is satisfied.
Build-1 first (it alone reopens Cycle 13's gate), then builds 2, 3, 4 — **build-3 ordered after
build-2 so `PAGE_SCAN` settles once before the re-ack pass reads it** (A3).
*(Superseded: this line previously routed to `convene the roundtable`.)*

**The joints worth putting in front of the room**, named here so the session starts from them.
*(All five were put to the room 2026-08-26 and are answered below and in the Roundtable review
record. J1 was CONCEDED — it is not circular; J2 was partially conceded and re-aimed; J3, J4 and J5
were confirmed and are amended above.)*

1. **Build-1 carries the Cycle 13 gate and a measurement it has never taken.** Q8 attaches the
   `malformed_frontmatter` population measurement to the same build that changes the population.
   The room should test whether that is circular.
   → **ANSWERED: NOT circular** *(Winston, conceding after hunting for it; Amelia concurring)*.
   Q8 measures the **post-repair** population, which is the population a retirement decision needs;
   measuring pre-repair would be the error. **The faults are elsewhere** — it must be able to fail,
   it must be a specimen set not a count, and its two halves are different instruments (A19).
2. **Build-3 is 15 re-acks across two conventions in one build**, ruled by elimination over the
   cheaper precedence statement (D2). The room should test whether the `frontmatter.md` narrowing
   really cuts the populations apart, or whether it relocates the ambiguity.
   → **ANSWERED: the cut HOLDS, and it relocates the ambiguity twice over.** `{research}` defaults
   to `_agent/research/`, **outside PARA** (`module.yaml:47`), so the populations do cut apart
   (Amelia, checking the worst case; Winston concurring). **But** the narrowing falsifies
   `extraction.md:188`'s grounding sentence (**19 re-acks, not 15**) and leaves **`moc`** recognized
   by a shipped check and named in no convention — both amended into D2 (A15, A16). **And 15 was
   never the true surface: seven in-prose pins are invisible to the handshake gate** (A3).
3. **Builds 1, 2 AND 3 all edit `vlt-lint-full.js`, across two releases** — the joint as written
   named two. *(roundtable A3/A4: the interface is now stated in build-2's block, build-3's true
   surface is named in its own, and build-3 is the first to re-enter the file after release 1 has
   shipped.)*
4. **The deferred half is a promise, not a plan.** A14-2 and the `summary` paraphrase are out on
   the argument that they need real page bytes; nothing schedules the build that takes them, and
   tracker #13 is its unruled dependency (Q2).
5. **D3 is a cycle-scoped rule standing in for a lifecycle change.** `ST-5`'s own fix — splitting
   grading modality from blocking power — was noted and routed to the platform ledger. The room
   should say whether a cycle-level rule is enough or whether P-N should open now.
   → **ANSWERED: no new P-N — it already exists as P-18 Tier C, precondition-blocked** (A18). And
   the room found D3 itself was written on the wrong axis and, as drafted, **made fewer checks gate,
   not more** — restated on **boundedness** per `brief-anatomy.md:203-210`, plus an
   instrument-adequacy clause, because **D3 did not even reach b2(5)** (A17, A17b).

After the review, each ruled build goes to `build-brief` (`brief build 1`, and so on). Build-1 is
released alone; builds 2–4 ride the second release.

**Also open, outside this cycle's scope** *(roundtable A25/A24/A26, 2026-08-26 — this paragraph was
stale by one commit and acting on the stale half fires a real hazard)*:

**Cycle 12 is CLOSED — it closed 2026-08-26 at `bb3a2d8`, after this cycle's capture ran**, and
this roadmap's own frontmatter already said so while this paragraph still read *"Cycle 12 can
close."* **The cost is concrete: Cycle 12's closeout wrote a hand-off Cycle 14 never took delivery
of**, because the hand-off's stated mechanism (*"the next cycle's `inbox-capture` re-lists them"*)
**cannot fire — Cycle 14's capture ran BEFORE Cycle 12 closed. Cycle 14 is the last reader these
items get.** Inherited now, none of it build scope:
- **b3(7)** — released as a standing watch with the instruction *"re-read it after Cycle 14
  build-3, against a bundle that is no longer waiting on itself."* **That lands on release 2's
  acceptance run** and is recorded in this cycle's ledger.
- **A12-4, A12-5's module side, and A11-11 direction 4 + A12-1's cause-fix instrument** — re-listed
  unchanged in this cycle's carry-forwards at closeout. *(Cycle 12's own section labelled the last
  two "the two items most at risk of being silently dropped."*)

⚠⚠ **TWO cycles are open and `factory/CYCLE` holds ONE line.** Cycle 13 is OPEN, gate-shut, and
un-pointed; `factory/CYCLE` reads `14-no-enforcement-point`. **Both cycle-scoped skills resolve
their target from that file** (`cycle-closeout/SKILL.md:60-61`, `acceptance-discharge/SKILL.md:66-68`).
So after release 1 lands build-1, run naively: **`acceptance-discharge` would write Cycle 13's
check-(2) evidence onto CYCLE 14's ledger, and `cycle-closeout` would close Cycle 14 and — at
Stage 4 — reset `factory/CYCLE` to `none`, un-opening Cycle 14 while builds 2/3/4 are unbuilt.**
Both skills' `-H` modes skip the confirming question entirely. **Before running either against
Cycle 13, hand-point `factory/CYCLE` at `13-trusted-returns` and restore it immediately after.
Never run either headless while two cycles are open.** *(There is no three-open state — Cycle 12 is
closed. Two is already one more than the pointer can express.)*

⚠ **The two-release plan costs TWO cold full sweeps, not one, and the roadmap priced neither.**
`scanFingerprint` is derived from `pageScanPrompt(...) + JSON.stringify(PAGE_SCAN)` (`:232-233`) and
reuse is an exact key match — so **build-1 forces a cold sweep at release 1, and builds 2/3/4 force
a second at release 2.** Accepted knowingly as the price of reopening Cycle 13's gate early.
**`{field-vault}` still owes a completed full sweep — pay it on the SECOND sweep after release 2,
not "the first sweep after release 1"** (the old advice named the most expensive possible slot, days
before a second forced cold run). **Build-2's cache repair cannot be field-confirmed until two
consecutive sweeps under an unchanged ruleset**, which release 2's own contents defer past.

---

## Next lifecycle move — AUTHORITATIVE

> ⚠ **This cycle is CLOSED (2026-09-01) — do not append.** From this line the document is
> read-only history. New signal goes to `factory/inbox/`; new work opens Cycle 15.

*(Restamped 2026-09-01 by `cycle-closeout` — the cycle is retired. **This is the last block in the
file and it is authoritative**; all prior routing is demoted above under `— historical record`,
per `vlt-lifecycle.md`'s foot rule.)*

**CLOSED on ONE gating FAIL, deliberately.** Gate passed: three releases tagged and pushed
(v0.16.2 / v0.17.0 / v0.17.1), no spike opened by this cycle left un-harvested, and every one of the
36 checks graded — **32 DISCHARGED · 3 FAILED · 1 BLOCKED**. The single gating FAIL, **build-3 (6)**,
was owner-ruled at closeout into **bound debt tagged `[ship-verifiable]` so it GATES Cycle 15**,
alongside **build-1 (6)**, ruled the same way on 2026-08-31. Both bounds are written out in
§Carried forward past Cycle 14 → *CLOSEOUT ADDENDUM* items 11 and 12, so Cycle 15's closeout can
grade them without re-deriving them.

**The loop restarts at field signal.** `factory/CYCLE` is reset to none; Cycle 15 opens at
`factory/cycles/15-<slug>/` on its `inbox-capture` run, which re-lists the carry-forwards from this
now-closed roadmap — **both halves of §Carried forward past Cycle 14**: the ten ideation-time
deferrals (items 1–10) *and* the seven acceptance-time carries (items 11–17). Six filings moved to
`filings/`; **three are held live in `factory/inbox/`** because their own clauses are undischarged —
`…-164501` (A14-2, deferred by A23), `…-125529` (A14-6, park #15's clause) and `…-141418` (A14-7,
park #16's clause). Tracker issues **#12** and **#14** are closed; the held three stay open.

⚠ **`factory/inbox/` is NOT empty — the immediate move is `inbox-capture`, not a wait for new
signal.** It holds the three held filings above plus a substantial un-captured backlog, and two of
those are the cycle's first-ever **`class: supersession`** filings (`2026-09-01-160000`,
`2026-09-01-170000`), which route to **Cycle 15 ideation's obsolescence beat** — P-15's half that has
never been exercised. Read `_output/problem-solution-2026-08-25.md` before touching PARA zoning
again.

⚠ **Owed and outside any build:** neither supersession filing has been posted through `vlt-feedback`,
so park #16 references no live tracker issue. `vlt-feedback` is invoked-only and needs the **owner's**
explicit go.

✅ **The two-open-cycles `factory/CYCLE` hazard is CLEARED** — Cycle 13 closed 2026-08-27 and Cycle 14
is closed here, so the pointer holds `none` and expresses the truth for the first time since
release 1.

**Next lifecycle move: `inbox-capture` — it will find a clean open-cycle slate and re-list this
roadmap's carry-forwards.**

**Platform work landed during this cycle: P-19, P-20, P-13** *(channel visibility floor,
`factory/platform/roadmap.md` §The channel contract — recorded here because the floor is a
closeout obligation and this run initially skipped it).* Six `plat:` commits fell inside Cycle 14's
window (2026-08-26 → 2026-09-01): **[P-19]** the acceptance corpus **opened** (`ba057eb`) and
**amended** (`db4b69f` — sampling policy added, its sweep-cost premise refuted); **[P-20]** the
check adversary **opened** (`f22dce2`) and **built** (`93107c6`); **[P-13]** the terminal-restamp
disambiguation **built** (`95e405a`) and its **done-when widened** (`e6230d4`) by P-20's own
question. None touched the shipped surface, so the channel's delivery boundary held. **No platform
item closed during this cycle**; five remain BUILT-awaiting self-acceptance.

⚠ **And this roadmap is [P-13]'s first COLD exercise — it FAILED, four times, before this
correction.** P-13's done-when was widened 2026-08-27 to require a restamp *"in a session that did
not author the clause."* Cycle 14's `acceptance-discharge` passes 3, 4 and 5 and this
`cycle-closeout` run were all cold, and all four placed their stamp **inside** the existing
`## Next lifecycle move` heading with superseded routing still below it — the exact defect P-13
exists to prevent, and the exact wording the map sharpened the same day (*"**Foot** means the
**last block in the file** … if anything at all follows the stamp, it is not the foot"*). The cause
is on record: this file's own newest-at-top convention was followed **in preference to the map's
rule**, by readers who had the wording and not the author's working memory. **The structure of this section is the correction** — prior routing demoted under a `— historical record` heading, the
authoritative stamp written last. **P-13 is NOT closed on this run**; it records a *negative* cold
exercise and stays open for an owner ruling, and the same evidence is a [P-20] instance (property:
*a cold reader restamps the last block*; passing-but-violated state: *a cold reader restamps
something, in the right heading, with stale routing below it* — reached four times running).
