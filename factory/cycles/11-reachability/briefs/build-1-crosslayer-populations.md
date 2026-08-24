---
title: 'Build #1 — crossLayerSlugs reaches sources/, the index, and non-.md linkables (the missing-target check''s three blind populations, and the predicate fix the cycle-gating inherited debt discharges on)'
status: 'BUILT 2026-08-24 — F1 landed as the three ruled edits inside full-scale.md:7 (zone-roots insert after the subtree-exclusion sentence; the any-extension glob replacing the *.md-only sentence; the {index}-slug union clause after the pass-the-union sentence) + F2 two-word truthing at checks.md:13 (cross-layer note→target, note→file); nothing else changed. Verification: E1(a) DISCHARGED — agent-run of the amended step-1 prose against the scratchpad fixture tree (default map; resources/wiki/{index,page-a,page-b}.md, sources/fantasy/deposit-x.md, sources/articles/clip.pdf, _agent/bases/wiki.base, _agent/research/note-r.md, _agent/conventions/frontmatter.overlay.md, _agent/lint-reports/old-report.yaml, _archive/dead.md), cross-checked by a mechanical simulation of the same prose: derived crossLayerSlugs = {clip.pdf, deposit-x, index, note-r, wiki.base} — exact match to expected (all three populations present: sources/ nested .md + non-.md, {index} slug, non-.md in unmapped _agent/; note-r the mapped-key control entering via its own research key while _agent/research/ stays carved out of the zone walk); all expected exclusions absent (page-a/page-b, frontmatter.overlay via {overlays} carve-out, old-report.yaml via {lint_reports} carve-out, dead via archive) — pre-amendment prose fails all three populations, so the pass is non-vacuous. Single-home grep clean (mechanics in full-scale.md only; checks.md stays a pointer); git diff clean outside the two .md files (vlt-lint-full.js untouched, normalization clause agrees with normalizeTarget :71-76); package-lint A/B/C/E PASS (D skipped mid-cycle, by design). Deviations/notes: no deviations.'
module_code: 'vlt'
created: '2026-08-24'
derives_from:
  - 'factory/inbox/2026-08-23-160500-crosslayerslugs-blind-to-sources-index-and-non-md-linkables.md (A10-18 — cause 1 {index} in neither population, cause 2 sources/ has no structure-map key, cause 3 the linkable set is *.md-only)'
roadmap: 'factory/cycles/11-reachability/roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-24): build-1, first and non-negotiable — lands sources/, {index}, and non-.md linkables into the full-mode coverage predicate, single-homed at skills/vlt-lint/references/full-scale.md (step 1''s crossLayerSlugs derivation); binds E1 (SPLIT per roundtable A10+A1: (a) ship-verifiable fixture derivation gates closeout, (b) the field sweep still gates as bound, with the refusal posture stated) and Q2 (DISSOLVED — A11-11 direction 2 deferred to Cycle 12, no predicate collision); roundtable A10 (owner-sanctioned): the tools/test-package-lint.py declaring-case pricing is CONDITIONAL on this build adding a package-lint.py gate-check callable — as ruled the deliverable is prose in full-scale.md, so the obligation does not trigger; spike: none.'
risk: 'low — a prose edit to one single-homed skill reference (plus a two-word pointer truthing in checks.md); no convention version bump, no consumer walk, no workflow .js change, no `// depends_on:` re-ack, no package-lint check added. The risk that exists is semantic: widening a suppression set can only suppress flags on links that resolve to real files, which is the missing-target check''s own stated contract — but the fixture check (E1(a)) must prove the exclusions (governance, cold storage, report dirs, wiki pages) survive the widening.'
---

# Build #1 — crossLayerSlugs reaches `sources/`, the index, and non-`.md` linkables

The first post-0.14.0 full-mode sweep on the field vault executed end-to-end (145/146,
loud caps — the B10-12 repair field-proven) and returned **12 missing targets, all 12
verified false positives**: 3 × `[[index]]`, 8 × links into `sources/`, 1 ×
`[[_agent/bases/wiki.base]]`. All three causes live in one sentence-group — the
`crossLayerSlugs` derivation single-homed at `skills/vlt-lint/references/full-scale.md:7`
(the Cycle 10 capture's grounding correction stands: **not** a `vlt-lint-full.js` edit; the
workflow only consumes the array). This build lands the three missing populations into that
predicate so the **B10-2(5)/B10-12(6) bound inherited debt** — which GATES Cycle 11's
closeout — has a predicate its discharging sweep can run against. Ruled first and
non-negotiable for exactly that reason: shipping it late leaves the gating sweep no window
and carries the debt a fourth cycle.

All rejected alternatives in the parent filing and the roadmap are settled — do not
re-litigate. In particular: Q2 is DISSOLVED (A11-11 direction 2 deferred to Cycle 12 — no
competing edit to this predicate this cycle), and the roundtable-A10 conditional
(declaring-case pricing in `tools/test-package-lint.py`) does **not** trigger because this
build adds no `package-lint.py` gate-check callable.

## Brief-time dispositions

The Cycle 10 capture carried three open design questions verbatim ("ideation's, not
capture's"). Ideation answered them at the deliverable level — all three populations land
**in the predicate, as prose, at `full-scale.md`** (build-1 bullet + roundtable A10's
as-ruled statement). The mechanism residue is dispositioned here, inside that frame:

1. **`{index}` joins the cross-layer set, not the page population.** The index is the
   wiki's navigation catalog, not a concept page: admitting it to the page population would
   put a catalog under per-page convention judgment (one-concept-per-page, frontmatter
   schema) and double-run it against the workflow's dedicated index pass. The cheap true
   fix is one clause: `{index}`'s own slug (`index` under the default map, by the standing
   basename normalization) is added to the `crossLayerSlugs` union. The page-list glob's
   "(excluding `{index}`)" stays untouched. *(Derives from the capture's cause 1 — excluded
   "from two directions"; both exclusions stay, the union gains the slug.)*

2. **`sources/` is admitted as a named zone root in the predicate — no `vault_structure`
   key is minted.** The capture flagged "should `sources/` become a structure-map key" as
   the one question that could be the vault's business rather than the module's; the ruled
   deliverable (prose in `full-scale.md`, per roundtable A10's as-ruled statement) settles
   the route: the predicate names the zone directly. This is also the honest shape:
   `sources/` is the operating contract's **Layer 1**
   (`vault-operating-contract.md:62` — immutable raw inputs, read-only to partners), human
   territory the map deliberately does not manage; a canonical key would put a
   partner-facing logical name on a zone partners may not write. The derivation therefore
   gains a stated exception to derive-from-keys, recorded as such in the single home
   (see F1) — a deliberate named exception, not silent drift from the derivation rule.

3. **The linkable glob widens from `*.md` to every walker-visible file, and the `_agent/`
   zone root joins the qualifying set (grounding addition — EXPANDED).** The missing-target
   check's own contract (`vlt-lint-full.js:277-279` comment; `checks.md:13`) is that **only
   a target resolving to nothing anywhere is missing** — so a real file of any extension is
   a valid target by definition, and widening the population can only suppress flags on
   links that resolve to real files. Non-`.md` basenames keep their extension, lowercased
   (`wiki.base`), matching the reducer's `normalizeTarget` (`vlt-lint-full.js:71-76`:
   basename, strip `.md` only, lowercase). **The EXPANDED part, and why it is in scope
   beyond the filing's letter:** the ruled population "non-`.md` linkables"' only field
   instance lives at `_agent/bases/wiki.base` — and `_agent/bases/` is under **no** mapped
   key (the contract's ad-hoc owned-artifact grant, `vault-operating-contract.md:64`,
   makes such dirs legal *by design unmapped*), so no extension widening over qualifying
   keys can ever reach it. Landing the ruled population requires the `_agent/` zone root.
   The standing subtree-exclusion rule already in the predicate ("a qualifying key's glob
   excludes any subtree that is another mapped key's home") makes this composition safe
   with **zero new exclusion machinery**: `{overlays}` (= `_agent/conventions/`),
   `{lint_reports}`, `{upgrade_reports}` are mapped keys' homes, so the `_agent/` walk
   carves them out automatically; `{research}`/`{sessions}`/`{specs}`/etc. are likewise
   carved out and keep entering via their own qualifying keys. The exclusion posture is
   preserved by the existing mechanism, not restated.

4. **Basename-collision semantics: unchanged, and named as accepted.** A `[[foo]]`
   intended as a missing wiki page is suppressed if any real file normalizing to `foo`
   exists in the widened population. This risk is not new — it is inherent to the
   basename normal form every qualifying key already uses — and the widening enlarges it
   only marginally. Changing the normal form (path-carrying slugs) is a workflow-seam
   redesign, out of this build's ruled scope.

**R1 (interim posture): not applicable** — the predicate prose is itself the mechanism
(the SKILL reader executes it); nothing ships ahead of its mechanism.

## F-sites

### F1 — `skills/vlt-lint/references/full-scale.md:7` (step 1, the `crossLayerSlugs` derivation — the single home)

**Current state (re-grounded 2026-08-24, HOLDS at `:7`; the whole step is one long
line).** The three load-bearing fragments, verbatim:

- Page list: "glob `{wiki}` for `*.md` (excluding `{index}`)" — and the qualifying-key
  predicate excludes the wiki's own key, so `[[index]]` resolves nowhere (cause 1, two
  independent exclusions: file-valued key fails the "names a *directory*" test; page glob
  excludes it).
- "Build `crossLayerSlugs` by **derivation from the resolved `vault_structure` map** …
  a key **qualifies** when its resolved value names a *directory* of walker-visible
  linkable notes — every directory-valued key **except** the wiki's own (`wiki`),
  governance (`conventions`, `overlays`, `personas`), cold storage (`archive`), and
  report dirs (`lint_reports`, `upgrade_reports`)." — `sources` is not among the resolved
  map's keys (`skills/vlt-setup/assets/module.yaml:44-66`, `vault_structure.default` —
  22 keys at current source; the Cycle 10 capture said 23, a count-only slip, the material
  fact `sources` absent HOLDS), so the derivation structurally cannot admit it (cause 2).
- "Glob each qualifying key's directory for `*.md` basenames, normalized the same way
  page slugs are." — the `*.md`-only filter (cause 3).

The single-home parenthetical ("*This predicate is single-homed here — other sites point
at it, never restate it*") and the subtree-exclusion sentence ("A qualifying key's glob
**excludes any subtree that is another mapped key's home**…") both HOLD and both survive
this edit unchanged in force (the subtree-exclusion rule is load-bearing for the new
`_agent/` zone root — see disposition 3).

**The exact change — three edits inside the step-1 line, in place:**

1. **After** the subtree-exclusion sentence ("…must not be double-covered by the parent
   key's glob)."), **insert**:

   > The qualifying set also contains two **zone roots** the map deliberately never
   > names — `sources/` (Layer 1: real, legally linked, and by design keyless — raw-input
   > territory is the human's to organize, and partners may not write it) and `_agent/`
   > (the contract's ad-hoc owned-artifact grant means partners legally link files in
   > unmapped `_agent/` dirs — e.g. `[[_agent/bases/wiki.base]]`); each zone root is
   > walked recursively under the same subtree-exclusion rule above, so a mapped key's
   > home inside it (`{overlays}`, `{lint_reports}`, `{upgrade_reports}` under `_agent/`)
   > stays carved out with no new exclusion list. *(These two are the predicate's only
   > deliberate exceptions to derivation-from-keys — named here, in the single home,
   > because no honest key can exist for either zone.)*

2. **Replace** "Glob each qualifying key's directory for `*.md` basenames, normalized the
   same way page slugs are." **with**:

   > Glob each qualifying key's directory (and each zone root) for **every walker-visible
   > file, any extension** — the missing-target contract is that only a target resolving
   > to *nothing* is missing, so any real file is a valid target: `*.md` basenames
   > normalize the same way page slugs are (extension stripped), non-`.md` basenames
   > **keep** their extension (`wiki.base`), all lowercased — the reducer's normal form.

3. **After** "Pass the union as `crossLayerSlugs` so a valid cross-layer link isn't
   reported as a missing target.", **insert**:

   > Add `{index}`'s **own slug** (its basename, extension-stripped — `index` under the
   > default map) to that union: the index is excluded from the *page* population by
   > design, but `[[index]]` is a legal link to a file that exists.

The builder may smooth conjunctions where the inserts meet the existing prose, but every
bolded mechanic above lands, and nothing else in the line changes (the `stubSlugs` parse,
the overlay collection, the invoke contract at `:8` are untouched).

**Why:** all three A10-18 causes are edits to this one sentence-group; the fix is the
predicate the E1 debt discharges against.

### F2 — `skills/vlt-lint/references/checks.md:13` (the missing-target pointer — two-word truthing)

**Current state (re-grounded, HOLDS):** "A link that resolves to a **cross-layer note**
(a note in a cross-layer location — the derived glob set of `full-scale.md` step 1) is
**not** missing…". It is a compliant pointer (no mechanics restated), but after this build
the derived set contains non-note files, so "note" is no longer true twice.

**The exact change:** "cross-layer note" → "cross-layer **target**"; "(a note in a
cross-layer location — the derived glob set…)" → "(a **file** in a cross-layer location —
the derived glob set…)". Nothing else — the legal-response clause and the stub clause are
untouched, and the site stays a pointer (the widening's mechanics live only in F1).

**Why:** single-home discipline — pointers must not silently narrow the set the single
home defines.

## Registration

**None.** A prose edit to a skill reference and a two-word pointer edit register nothing:
no new skill, no workflow, no `module-help.csv` row, no version surface. Priced
non-triggers, named per the anatomy so their absence is a decision, not an oversight:

- **No handshake:** `full-scale.md` and `checks.md` are `vlt-lint` skill references, not
  handshaked conventions — no `version:` bump, no consumer re-ack.
- **package-lint C6:** the operating contract is not edited — no rule-card re-derivation.
- **package-lint E4 / roundtable A10:** no `package-lint.py` check callable is added, so
  the conditional declaring-case obligation in `tools/test-package-lint.py` does **not**
  trigger (recorded as ruled, owner-sanctioned A10).
- **package-lint E5:** `vlt-lint-full.js` is untouched — no `// depends_on:` movement.

## Out of scope (dispositioned)

- **A `vault_structure` key for `sources/`** — rejected (disposition 2): the ruled
  deliverable is predicate prose; a canonical key would name a partner-read-only zone in
  the partner-facing map and change the shipped map for every vault.
- **`vlt-lint-full.js`** — already correct: it consumes whatever population it is passed
  (`:84` normalize-on-intake, `:281` Set build, `:284` missing-target test). The Cycle 10
  capture's site-attribution correction stands; touching it would spend a `.js` change and
  a `// depends_on:` re-ack for nothing.
- **The slug normal form (basename-only)** — kept as-is; collision semantics accepted and
  recorded (disposition 4). A path-carrying normal form is a workflow-seam redesign no
  filing asks for.
- **`stubSlugs` / the overlay-args machinery** — untouched; orthogonal halves of the same
  step-1 line.
- **`report.md` / `fix-and-file.md`** — no restatement of this predicate exists in either
  (grep-verified); their `missing_targets` report key is population-agnostic.
- **A11-11 directions 1–4 (the cost/caching redesign of this same predicate's
  neighborhood)** — deferred to Cycle 12 by ruling; Q2 DISSOLVED. Direction 0
  (instrumentation) is build-8's, not this build's.
- **Build-2's `resources/` PARA-parity contract change** — no interaction: `resources` is
  already a qualifying key today (the Q1 clerk grounding leaned on exactly that), and
  build-2 edits the contract, not this predicate.
- **The `{research}`-zone fan-out second cut** (`full-scale.md:10`) — pre-existing named
  second-cut work, unchanged.

## Verification (unit, at rest)

1. **E1(a) — the fixture derivation (the check of record; GATES closeout).**
   **Instrument, named (R1-of-the-roundtable applied at tag birth):** an **agent-run of
   the amended step-1 prose** against a **temp fixture vault tree** built for the run
   (scratchpad; never a live vault), with the recorded evidence being the derived
   `crossLayerSlugs` union vs the expected set, written into the BUILT status. Fixture
   shape (minimum): default-map `vault_structure`; `resources/wiki/{index.md, page-a.md,
   page-b.md}`; `sources/fantasy/deposit-x.md` and `sources/articles/clip.pdf` (nested +
   non-`.md`); `_agent/bases/wiki.base`; `_agent/research/note-r.md`;
   `_agent/conventions/frontmatter.overlay.md`; `_agent/lint-reports/old-report.yaml`;
   `_archive/dead.md`. **Expected union contains:** `deposit-x`, `clip.pdf`, `wiki.base`,
   `index`, `note-r` — the three ruled populations plus a mapped-key control.
   **Expected union excludes:** `page-a`/`page-b` (page population, not cross-layer),
   `frontmatter.overlay` (governance, via subtree-exclusion carving `{overlays}` out of
   the `_agent/` walk), `old-report.yaml` (report dir, same mechanism), `dead` (cold
   storage). The pre-amendment prose fails this fixture on all three populations — the
   check could have failed, so a pass means something (no vacuous discharge).
2. **Single-home grep** — `grep -rn "crossLayerSlugs\|qualifying" skills/` shows the
   derivation mechanics in `full-scale.md` only; `checks.md:13` remains a pointer
   (F2 wording, no restatement).
3. **Cross-file agreement** — F1's normalization clause agrees with
   `vlt-lint-full.js:71-76` (`normalizeTarget`: basename, `.md`-only strip, lowercase);
   nothing in the `.js` changed (git diff clean outside the two `.md` files).
4. **Packaging lint** — mid-cycle `uv run tools/package-lint.py` A/B/C/E (D /
   `--expect-version` is the release gate, not this build's; the version bump rides the
   cycle's release build).
5. **R2 (fixture extension): not applicable** — no release-gate check added or changed
   (the A10 conditional did not trigger).
6. **R3 (legal response): not applicable** — no finding class added or changed; the
   missing-target class and its legal response at `checks.md:13` are unchanged (its
   population moved, not its response).
7. **R4 (enumeration widening): not applicable** — the build adds no file to any
   enumerated class; it edits an enumeration's *predicate*, which is the single home
   doing its job.
8. **Scrub** — both changed files are shipped surface: no personal names, no vault names,
   no real install paths (fixture content uses placeholder names; the worked example in
   F1's insert is the generic `_agent/bases/wiki.base` shape, an in-vault relative path,
   which is placeholder-compliant).

*(No Release section — this is not the release build; the dual version bump and the
`--expect-version` gate ride the cycle's release build.)*

## Acceptance (live — appended to the roadmap ledger)

Both checks below are E1's ruled halves (roadmap §Evidence-debt dispositions, E1 —
roundtable A10 + A1), restated here as the brief's acceptance and appended to the Deferred
acceptance ledger in this same run.

1. **`[ship-verifiable]` — GATES closeout.** The amended `crossLayerSlugs` derivation, run
   against a fixture `vault_structure`, yields the three missing populations —
   `sources/` (nested, `.md` and non-`.md`), `{index}`'s slug, and a non-`.md` linkable in
   an unmapped `_agent/` dir — correctly at rest, **and** the standing exclusions
   (wiki page population, governance, cold storage, report dirs) survive the widening.
   **Instrument:** the Verification-1 fixture + agent-run derivation protocol
   (factory-side, runnable at rest); **evidence:** the derived-vs-expected record in the
   brief's BUILT status. Dischargeable the day the build lands.
2. **`[field — still gates, as bound]` (the B10-2(5)/B10-12(6) inherited-debt
   re-discharge; criteria as amended by DA9).** **Event:** an executing full-mode
   `vlt-lint` sweep on the field vault (`{field-vault}`; the owner runs it, on the first
   post-release full lint) whose missing-target flags **survive verification** — or a
   measured zero — after this build's predicate lands. The gating run carries build-8's
   direction-0 instrumentation live, and its budget is sized from that evidence where
   available. **Refusal posture (A1):** an availability-failed sweep
   (`status: 'failed'`, no persist — the A11-11 dynamic) neither discharges nor forfeits
   the debt; it escalates to an owner ruling (an owner-authorized re-run at explicit
   budget, or a knowing re-carry), and the failed run's instrumentation counts as A11-11
   measurement evidence either way. The anti-direction binds in every branch: **no
   sampling; no `coverage_caps` entry is ever removed to make a run look cleaner.**
