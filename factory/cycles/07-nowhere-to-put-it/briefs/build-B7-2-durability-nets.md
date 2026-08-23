---
title: 'Build #B7-2 — the durability nets (the config merge preserves instead of rebuilding, and the skill-asset manifest walks the tree instead of trusting a list)'
status: 'BUILT 2026-08-15 — F1 merge_config() rewritten preserve-unless-answered
  (declaration-read variable predicate via prompt/default/result/user_setting markers;
  metadata always refreshed; answers > existing > module.yaml default; returns
  (config, merge_report); result JSON gains module_keys_preserved/removed/defaulted;
  docstring + argparse carry the {"core","module"} payload contract). F2
  skills/vlt-setup/scripts/verify-skill-manifest.py shipped (stdlib PEP 723; --write with
  previous_entries/added/removed shrink report, --verify with diverged/missing, exit 0 on
  findings / 2 on operational error; compute_manifest() is the importable structural walk —
  shipped vlt-* dirs by provenance from --source-skills-dir, plus installed
  .claude/{workflows,hooks} extras by shipped-assets basenames, cruft excluded). F3
  vlt-setup SKILL.md :150 rewritten structural + script invocation in $SKILL/$ROOT idiom,
  :75 belt-and-suspenders clause, :103 echo-removals clause, Confirm gains the manifest
  line. F4 vlt-upgrade :37 re-pointed at --verify (SHA mechanics single-homed in the
  script), Verify carries removed-paths→ledger-Notes. F5 check_durability_nets in
  package-lint group C (probe 1 in-process merge_config preservation; probe 2 script scope
  vs the check''s own independent walk, vacuity-guarded) + doc-header C9 line. F6 harness
  copies real merge-config.py + verify-skill-manifest.py into the fixture; cases 19
  (destructive-merge stub → C fails, preservation string) + 20 (references/-dropping stub →
  C fails naming references/how.md); CASE_FLOOR 18→20.
  VERIFICATION: test-package-lint 20/20 green; package-lint repo A/B/C/E PASS D SKIPPED and
  --expect-version 0.9.1 exit 0. R2 mutation probe: coverage stripped from cases 19/20 →
  real-repo lint FAIL group E naming check_durability_nets (E4); restored → green.
  Red-then-green: check_durability_nets neutered (return []) → cases 19+20 FAIL (18/20);
  restored → 20/20. A7-2 table inverted at rest (temp fixture): absent-from-answers →
  vault_structure preserved byte-identical incl vault-local sub-key, named in
  module_keys_preserved, zombie named in module_keys_removed; mis-nested top-level
  vault_structure → non-destructive; correct nesting → merges as today; fresh install →
  17-row default map materialized, module_keys_defaulted. Manifest e2e (temp installed-shape
  tree with decoy mint vlt-agent-test + decoy vault-local hook): 60 entries covering all 8
  references/*.md, scripts/*.py, 3 workflows, installed vitals hook; both decoys + all
  cruft excluded; deleting a shipped file → removed names it; editing/deleting live files →
  --verify names diverged + missing, exit 0. Repo spot-assert:
  skills/vlt-lint/references/checks.md + skills/vlt-setup/scripts/merge-config.py in the
  computed set (56 entries). Cross-file greps: .skill-manifest name + cruft set agree
  across both SKILL.mds and the script; no restated SHA mechanics at vlt-upgrade:37. B1
  preserve-path re-checked: merge-help-csv.py untouched; provenance-based scope excludes
  mints (tested); overlays unaffected. No .decision-log.md on disk; scrub clean.
  Deviations/notes: (1) verify-skill-manifest.py declares no pyyaml dependency — it needs
  none (stdlib-only); the brief''s "(pyyaml, matching its siblings)" is honored as the
  PEP 723 idiom, not a false dependency. (2) F1: an ANSWERED key that is not a defined
  variable is also not written and is reported in module_keys_removed — the brief defined
  removed over existing-section keys only; extended so no drop of any origin is ever
  silent (disposition 3''s letter applied to both origins). (3) verify-skill-manifest
  main() resolves --live-skills-dir/--manifest/--overlays-dir against cwd (found in
  end-to-end verification: relative args vs resolved --root raised ValueError in
  relative_to).'
module_code: 'vlt'
created: '2026-08-15'
derives_from:
  - 'inbox/2026-08-02-080528-merge-config-strips-vault-structure.md (A7-2 — merge_config()
    destroys any module variable absent from answers["module"] and reports success; second
    ask: the result JSON must report what was removed)'
  - 'inbox/2026-08-03-100710-skill-manifest-scope-lost-references-and-scripts.md (A7-3 — the
    skill-asset manifest scope is an enumeration; references/ fell out at v0.9.0 (regression),
    scripts/ was never in (original gap); second-order: the hand-widened 40→55 manifest does
    not survive the module-owned overwrite)'
roadmap: 'skills/reports/inbox-evolution-arc7-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-15): grouping row B7-2 (the durability nets — the
  doctrine''s second application at two altitudes; depends on B7-1, shipped); §Pre-ideation
  ruling 2 (A7-3 scripts/: SAME BUILD, BOTH INCLUDED, provenance kept distinguishable);
  §Cross-filing decide-once ruling 5 (enumeration-vs-structure DOCTRINE: a durability net
  defines its protected surface structurally, never by enumeration; a net that must carry a
  list carries a shrink check; a generated-and-verified list is a structure read with a
  cache); §Evidence-debt dispositions (A7-2''s prior-strip lead ATTACHES here, NOT BLOCKING);
  §Questions left to brief time — B7-2 slot (script-computed manifest + shrink-check home;
  "the structural doctrine already forecloses the prose-instruction form, so the open half is
  the shrink-check''s home"); §Post-ideation amendments R2 (wired by B7-1: a build that adds
  or changes a release-gate check extends tools/test-package-lint.py in the same build).'
risk: 'low-moderate — no convention version moves, no consumer walk, no help-registry change;
  but the build edits the install/upgrade durability path itself (merge-config.py + the
  skill-asset manifest net), where a regression is silent data loss. Mitigated by a new
  release-gate check (R2-covered) and at-rest reproductions of both defects.'
---

# Build #B7-2 — the durability nets

Arc 7's Strand-2 build: two mechanisms whose whole job is to protect vault state were found
defining their protected surface by enumeration, and both silently destroyed or ignored what
the enumeration missed. **A7-2:** `merge_config()` deletes the entire existing `vlt:` config
section and rebuilds it from `answers["module"]` alone — any module variable absent from the
answers payload is destroyed, `"status": "success"` reported either way (reproduced at rest;
the observed casualty was the 17-key `vault_structure` map plus a vault-local override key).
**A7-3:** the skill-asset manifest spec (`vlt-setup/SKILL.md:150`) enumerates
`SKILL.md + assets/ + .claude/workflows/*.js`, so the eight `references/*.md` (shipped at
v0.9.0) and three `scripts/*.py` (shipped at v0.3.0, pre-dating the build-18 manifest) sit
outside the divergence net — and re-grounding adds a third dropout of the same class, the
installed `.claude/hooks/vlt-vitals.py` (shipped by the Arc-5 enforcement kit, after the
manifest spec was written).

The fix in both cases is the doctrine ruling applied: derive the protected surface by walking
the tree / reading the declaration the protected thing carries about itself
(`module.yaml`'s variable definitions; the shipped skill dirs), and where a cached list
remains (the manifest file), carry a shrink check. Per R2, the build also extends the release
gate: a new `check_durability_nets` gate check proves both nets structurally, with covering
fixture cases and a `CASE_FLOOR` bump.

**All rejected alternatives in the parent filings are settled — do not re-litigate.** In
particular: A7-2's map-shape/missing-branch guesses are disproven (the capture's grounding is
authoritative and reproduced); A7-3's split-the-scripts-inclusion option is ruled SAME BUILD;
and the merged fix does not merge the provenance — restored protection (`references/`) and
new protection (`scripts/`, installed hook) stay distinguishable in this brief, the changelog
line, and the acceptance checks.

## Grounding at brief time

Every capture-cited site re-verified against current source at HEAD of `arc7-v0.10.0`
(post-B7-1):

- **HOLDS** — `merge-config.py:271-278` (anti-zombie `del config[module_code]`, no read of
  what it destroys), `:281-285` (rebuild = `extract_module_metadata()` + templated
  `answers.get("module", {})`, nothing else), `:182-191` (`extract_module_metadata` — exactly
  `name`/`description`/`version`/`default_selected`), `:194-221` (`apply_result_templates`
  passes map values through correctly — never the problem), `:393-403` (result JSON:
  `module_keys` lists what was written; nothing reports what was removed).
- **HOLDS** — `vlt-setup/SKILL.md:75` (the `"module"`-nesting contract, prose only),
  `:150` (the manifest enumeration + module-owned overwrite posture, both halves verbatim),
  `:23` (the anti-zombie rationale: "stale values never persist").
- **HOLDS** — `vlt-upgrade/SKILL.md:37` (`skill_asset_divergence` computed "for each file the
  manifest records" — scope loss silent by construction), `:30-40` (Step-1 pre-flight covers
  mints/overlays/bases/skill-assets/mint-history/capabilities/governance, not `config.yaml`),
  `:48` (the skills-have-no-overlay-mechanism veto — stands, per ideation), `:83` (Step-3.6
  provision hand-off that refreshes the manifest via `vlt-setup`), `:148` (Verify: manifest
  exists and was refreshed).
- **HOLDS** — the directory census: `find skills -type d` still yields exactly
  `vlt-dispatch/references` (4 files), `vlt-lint/references` (4 files),
  `vlt-setup/scripts` (3 `.py`), plus the two `assets/` trees. Eight references + three
  scripts remain the filing's uncovered set.
- **EXPANDED (grounding addition — now in scope):** the installed
  **`.claude/hooks/vlt-vitals.py`** copy. The source file `vlt-setup/assets/hooks/vlt-vitals.py`
  is inside the old enumeration (under `assets/`), but the *installed* copy the enforcement
  kit writes to `{root}/.claude/hooks/` (`vlt-setup/SKILL.md:170` — "module-owned …
  overwrite it on every install/update, exactly like the workflows") is not: the enumeration
  names only `.claude/workflows/*.js` among installed extras. A vault-local edit of the
  installed hook is therefore silently clobbered with no divergence line — the identical
  failure shape, created the identical way (a surface shipped *after* the enumeration was
  written, by B5-9). It joins the net in this build. This is an addition beyond the filing's
  letter, justified by the doctrine ruling itself: the walk finds it; only the list missed it.
- No site MOVED or was SUPERSEDED; no roadmap superseding note is required, and no ideation
  ruling is contradicted.

## Brief-time dispositions

Numbered; each derives from the question the roadmap designated to this brief (autonomous
run — recorded here per the headless contract).

1. **The manifest is computed and verified by a script — `verify-skill-manifest.py` ships in
   `skills/vlt-setup/scripts/`.** Derives from the B7-2 designation slot, whose own note
   states the structural doctrine forecloses the prose-instruction form; the 2026-07-12
   handoff had already flagged this exact machinery as "prose where a script should be". A
   prose instruction to an LLM to "walk the tree" is an enumeration one paraphrase away; a
   script's walk is the structure read the doctrine demands.
2. **The shrink check lives in the script's write path and is a path-level removal report,
   not a bare count, and not a new key in the upgrade report's YAML schema.** Derives from
   the designated question's open half ("whether a manifest-entry-count-didn't-shrink check
   belongs in the upgrade report") plus the doctrine's shrink clause. Ruling: yes in
   substance — the manifest is the doctrine's sanctioned "structure read with a cache", and
   its cache carries the shrink check — but a count-didn't-shrink check cannot distinguish a
   legitimate de-ship from scope loss, so the check reports *which paths left the net*
   (`removed: [...]` in the script's JSON output when overwriting an existing manifest).
   Surfacing: `vlt-setup`'s Confirm section and `vlt-upgrade`'s Verify/ledger Notes carry it
   (F3/F4); the Step-4 report schema (`vlt-upgrade/SKILL.md:92-108`) stays unchanged — its
   keys are a shipped parseable surface and this build has no ruling to extend it.
3. **`merge_config()` preservation semantics: answers > existing config > `module.yaml`
   variable default; metadata always refreshed; undefined keys removed and reported.**
   Derives from the ideation ruling's "preserve-unless-answered rather than
   rebuild-from-answers" plus the doctrine (the protected surface is *declared* — a key is
   legitimate iff it is module metadata or a variable defined in `module.yaml`). The
   `module.yaml`-default fallback (the capture's "no fallback to `module.yaml`'s own
   `default:` map") makes the script correct by construction against the exact caller error
   observed — the prose at `SKILL.md:75` stops being the only thing standing between a
   correct run and data loss. The anti-zombie *purpose* (`SKILL.md:23` — stale values never
   persist) is retained, made honest: a key that is neither metadata nor a defined variable
   is a true zombie, still removed — but now **reported**, never silent.
4. **The removal report is the result-JSON fix A7-2's second ask demands.** `merge_config()`
   returns its merge report alongside the config; the printed result JSON gains
   `module_keys_preserved` (defined variables carried from the existing section, unanswered),
   `module_keys_removed` (zombies dropped, by name), and `module_keys_defaulted` (filled from
   `module.yaml` defaults). `"status"` stays `"success"` — under the new semantics a removal
   is only ever a deliberate zombie drop, and it is now loud. Independent of disposition 3,
   per the ruling ("the second ask is independent and is the minimum honest fix either way").
5. **R2 is triggered: this build adds a release-gate check.** A new
   `check_durability_nets(root)` callable in `tools/package-lint.py` (group C aggregation,
   E4-inventoried automatically by its `check_` name) proves both nets against the real
   scripts. Per R2 (wired by B7-1, commit `25765a1`), the same build extends
   `tools/test-package-lint.py`: two covering cases with `covers=("check_durability_nets",)`
   and `CASE_FLOOR` 18 → 20. Judgment call: a gate check (rather than an unwired standalone
   test) is chosen precisely because an unwired test is the A7-1 failure — a net nobody
   proves; wiring it to the gate puts it under E4 and the shrink floor.
6. **The installed `.claude/hooks/vlt-vitals.py` joins the manifest net** (the grounding
   addition above). Structural derivation, not a new list entry: installed extras outside the
   skill dirs are exactly the files whose basenames the shipped `vlt-setup/assets/workflows/`
   and `vlt-setup/assets/hooks/` trees carry — the walk of the shipped tree defines the set,
   so a future `assets/hooks/` addition enters the net automatically.
7. **The payload contract moves into the script's own surface.** `merge-config.py`'s
   docstring/`--help` gains the `{"core": {...}, "module": {...}}` shape and the
   preserve-unless-answered semantics (the capture's finding 3: the nesting rule lived only
   in the consumer's prose). `SKILL.md:75` keeps its sentence (the caller should still send
   the full map) and gains one clause noting the script now preserves and falls back — a
   malformed payload is no longer destructive, only lazy.
8. **`vlt-upgrade`'s Step-1 gets no new `config.yaml` divergence snapshot.** The capture's
   impact note (pre-flight covers everything but `config.yaml`) is confirmed, but ideation
   ruled the fix script-side (preserve + report); with merge-config preserving by
   construction, the destruction path the snapshot would have guarded is closed. A
   config-baseline net is unruled scope — left for a future filing if the field shows a
   residual loss path. Recorded as out-of-scope disposition, not silently dropped.

## F1 — `skills/vlt-setup/scripts/merge-config.py`: preserve-unless-answered + removal report

**Current state.** `merge_config()` (`merge-config.py:224-295`): after core handling, the
anti-zombie delete removes the entire existing module section unread (`:271-278`), then the
section is rebuilt as `extract_module_metadata(module_yaml)` (`:281`, helper at `:182-191`)
plus `apply_result_templates(module_yaml, answers.get("module", {}))` (`:282-285`). Any module
variable absent from `answers["module"]` is destroyed. The result JSON (`:393-403`) reports
`module_keys` (what was written) and nothing about what was removed. The docstring (`:6-20`)
and `--help` never state the `"module"`-nesting payload contract.

**The exact change.**

- Replace the delete-and-rebuild (`:271-285`) with a structural merge inside
  `merge_config()`:
  1. `existing_section = config.get(module_code)` if it is a dict, else `{}` (a non-dict
     legacy value is treated as absent and reported as removed).
  2. Derive the **defined-variable set** from `module_yaml`: top-level keys whose value is a
     dict carrying any of `prompt` / `default` / `result` / `user_setting` (today exactly
     `vault_structure`; the predicate must be a declaration read, never a hard-coded name —
     the looser `isinstance(v, dict)` test `load_legacy_values` uses at `:130` is acceptable
     as a floor but the builder should prefer the marker-key predicate so `agents:`-style
     structured metadata can never be mistaken for a variable).
  3. Build the new section: metadata from `extract_module_metadata()` (always refreshed —
     module-owned); then, per defined variable, the value from `answers["module"]` (with
     result templates applied, exactly as today) if answered, else the existing section's
     value if present, else the variable's `module.yaml` `default:` if it has one
     (written as-is — defaults ship final; no result-template application to non-answers).
  4. Compute the merge report: `preserved` (defined variables carried from the existing
     section), `removed` (existing-section keys that are neither metadata nor defined
     variables — dropped), `defaulted` (filled from `module.yaml` defaults).
- Change `merge_config()`'s return to `(config, merge_report)` and update its one caller
  (`main()`, `:373`). The result JSON (`:393-403`) gains `module_keys_preserved`,
  `module_keys_removed`, `module_keys_defaulted` from the report; `module_keys` stays.
- Docstring + argparse description: add the answers payload shape
  (`{"core": {...}, "module": {...}}` — module variables **must** nest under `"module"`) and
  one line of the preserve-unless-answered semantics (disposition 7).
- Update the module docstring's "Uses an anti-zombie pattern" line (`:11`) to describe the
  new posture: metadata refreshed, defined variables preserved unless answered, undefined
  keys removed and reported.

**Why.** A7-2's confirmed mechanism — the rule "any module variable absent from
`answers["module"]` is destroyed silently" becomes "no defined variable can be destroyed by
an absent answer, and no key is ever removed unreported." Doctrine applied: enumeration by
omission (anything unnamed is destroyed) becomes a declaration read (`module.yaml` defines
the legitimate surface).

**Out of scope at this site:** `extract_user_settings` / `config.user.yaml` handling
(untouched — no filing clause); `apply_result_templates` (correct as-is, capture-confirmed);
the `--legacy-dir` machinery (untouched; `vlt-setup` never passes it, `SKILL.md:101`).

## F2 — `skills/vlt-setup/scripts/verify-skill-manifest.py` (new): the manifest computed, verified, and shrink-checked

**Current state.** No script exists; the manifest is produced by prose instruction at
`vlt-setup/SKILL.md:150` and consumed by prose instruction at `vlt-upgrade/SKILL.md:37`.

**The exact change.** A new PEP 723 script (pyyaml, matching its siblings) with two modes:

- **`--write`** — compute the manifest and write it to the given path (default derivable
  from `--overlays-dir`, matching `{overlays}/.baseline/.skill-manifest`). Scope, derived
  structurally, never listed:
  - **every file** under each **shipped** `vlt-*` skill dir in the live skills dir — whole
    trees: `SKILL.md`, `assets/`, `references/`, `scripts/`, and anything a future build
    adds. Shipped-ness is **provenance-based, from the module source** (the same B1
    discipline as `merge-help-csv.py` and the Step-1 snapshot): the script takes the module
    source's skills root (`--source-skills-dir`) and treats as shipped exactly the `vlt-*`
    dirs present there — a locally-minted `vlt-agent-*`/`vlt-*` dir is **never** manifested
    (it is the vault's; the manifest is the module-owned net only).
  - **installed module-owned extras**: files under `{root}/.claude/workflows/` and
    `{root}/.claude/hooks/` whose basenames exist under the shipped
    `vlt-setup/assets/workflows/` and `vlt-setup/assets/hooks/` trees respectively
    (disposition 6 — the walk of the shipped tree defines the set; a vault's own hooks are
    untouched and unlisted).
  - **exclusions**: the upgrade's cruft set, byte-for-byte the same names as
    `vlt-upgrade/SKILL.md:49` (`.decision-log.md`, `__pycache__/`, `*.pyc`, `.DS_Store`) —
    dev artifacts must not enter the net even if present on disk.
  - Line format unchanged: `<sha256>\t<path>` (the existing consumer prose stays true).
  - **Shrink check (disposition 2):** when a manifest already exists at the target path,
    diff entry sets before overwriting and report `previous_entries`, `added`, `removed` in
    the JSON output. `removed` is informational, never blocking (a de-shipped file
    legitimately leaves the net) — but it is always printed, so a silent narrowing is
    structurally impossible.
- **`--verify`** — recompute SHAs for every manifest entry against the live files and report
  `diverged: [paths]` (SHA mismatch) and `missing: [paths]` — the mechanical half of
  `vlt-upgrade` Step-1's `skill_asset_divergence`. Exit 0 with the JSON report either way
  (divergence is a finding for the caller to surface, not a script failure); non-zero only
  on operational error (manifest missing/unreadable).
- JSON result to stdout in both modes (the `merge-config.py` result idiom): mode, manifest
  path, `entries`, and the mode-specific fields above.

**Why.** Doctrine ruling: the net's known application "the skill-asset manifest → walk the
shipped tree", plus the designated brief-time question resolved in disposition 1. The
provenance rules keep both A7-3 blame lines legible: `references/` re-enters the net
(restored, regression at v0.9.0/`f3b343d`), `scripts/` and the installed hook enter it for
the first time (new protection — `scripts/` an original gap since v0.3.0/`8c0955f`; the hook
a post-spec surface from B5-9). The vault ruling that hand-widened a manifest to 55 entries
is honored by construction — the structural walk strictly contains it, so the module stops
silently reverting a documented vault decision.

**Out of scope at this site:** no gate on `--verify` results (detect-and-report is the
standing posture, `vlt-upgrade/SKILL.md:110`); no manifest of governance files
(`governance_divergence` already covers `_meta/` — see Out of scope 3).

## F3 — `skills/vlt-setup/SKILL.md`: the spec becomes structural and invokes the script

**Current state.** `:150` — *"…covering every **shipped** `vlt-*` skill dir (those in
`module.yaml` — i.e. **not** a locally-minted `vlt-agent-*`), across `SKILL.md` + everything
under each skill's `assets/`, plus the installed `.claude/workflows/*.js`"* — the
enumeration, plus the module-owned overwrite posture, plus "Compute it from the *installed*
shipped files". `:75` states the payload contract in prose. `:295` (Confirm) lists provision
outcomes with no manifest line.

**The exact change.**

- **`:150` rewrite** (same paragraph, same heading, same build-18 attribution): the manifest
  covers **every file the module ships into the vault** — derived by
  `verify-skill-manifest.py --write`, never by a hand-kept scope list: whole shipped `vlt-*`
  skill dirs (shipped-ness from the module source, never the live tree) plus the installed
  module-owned extras under `.claude/workflows/` and `.claude/hooks/` (basenames from the
  shipped assets trees). Name the three surfaces the old enumeration missed as a *worked
  consequence*, not as the definition (`references/`, `scripts/`, the installed vitals hook)
  — point-at-the-map, per the standing lists-drift rule. Keep: module-owned,
  overwrite-on-every-install/update; computed from the installed files. Add: the write
  reports `added`/`removed` vs any prior manifest, and removals are surfaced in the Confirm
  summary. Give the invocation in the existing `$SKILL`/`$ROOT` command idiom of `:83-97`
  (placeholder paths only — no install-specific paths, per the worked-example rule).
- **`:75` one-clause addition** (disposition 7): the module object still always carries
  `vault_structure`, *and* the script now preserves any defined variable absent from the
  answers (existing value, else `module.yaml` default) and reports every removal — the
  contract is belt, the script is suspenders.
- **`:103` touch-up:** "If either script exits non-zero, surface the error and stop" —
  extend the sentence so the caller also **echoes `module_keys_removed` (and any
  `module_keys_defaulted`) from the result JSON in the confirmation summary** — a removal
  the user never sees is the A7-2 silence back again one layer up.
- **`:295` (Confirm, "Per vault provisioned"):** add the manifest to the list — entries
  written, and `added`/`removed` vs the prior manifest when one existed.

**Why.** A7-3's spec site — the enumeration is the defect; the doctrine names this exact
fix. The Confirm additions are the shrink check's human surface (disposition 2).

## F4 — `skills/vlt-upgrade/SKILL.md`: the consumer reads the script, and Verify carries the shrink line

**Current state.** `:37` — Step-1 `skill_asset_divergence`: "For each file the manifest
records, recompute its SHA against the live copy…" (prose instruction; correct but
mechanics-bearing). `:148` (Verify) — "…the skill-asset manifest `{overlays}/.baseline/.skill-manifest`
exists and was refreshed to the shipped versions (via the Step-6 provision)…".

**The exact change.**

- **`:37`:** replace the recompute-mechanics clause with the script invocation —
  `verify-skill-manifest.py --verify` produces the diverged/missing sets this bullet
  records — keeping everything else (the copy-into-working-note rule, the
  `skill_manifest_missing` seed path, the net's stated purpose sentence). Single-home: the
  SHA mechanics now live in the script; this bullet points at it.
- **`:148` (Verify):** extend the manifest clause — "…and was refreshed to the shipped
  versions (via the Step-6 provision), **with the refresh's `removed` paths (if any) carried
  into the ledger entry's Notes line** — a path that left the net is a fact the standing
  ledger must record". No Step-4 YAML schema change (disposition 2).

**Why.** The consumer half of A7-3; the shrink report needs a home at the only cadence a
vault re-derives the manifest. Step-2 (`:48`) and Step-3.6 (`:83`) are correct as written
and untouched — the manifest refresh already rides the provision hand-off.

**Durability posture re-check (CLAUDE.md standing rule), performed at brief time:** this
build touches `vlt-setup`, `vlt-upgrade`, and a merge script, so the B1 local-mint preserve
path was re-walked: `merge-help-csv.py` is untouched; `merge-config.py` becomes strictly
more preserving; the new manifest scope is provenance-based from the module source (F2), so
a local mint can never enter the module-owned net and can never be flagged or clobbered
through it. Overlays (`*.overlay.md`) live under `{overlays}`, not under any manifested
surface — unaffected. The builder re-confirms this paragraph against the finished diff.

## F5 — `tools/package-lint.py`: `check_durability_nets` (R2-triggered gate check)

**Current state.** Group C aggregates `check_rule_card` / `check_router_integrity` /
`check_enforcement_kit` (`:230-232`); E4 (`:567-614`) introspects every `^check_|^_e\d+_`
callable and fails any without a covering harness case; the doc header (`:30-53`) narrates
each group's checks.

**The exact change.** One new module-level callable `check_durability_nets(root) -> list`,
aggregated into group C beside `check_enforcement_kit` (`:232`), with two probes:

- **Probe 1 — merge-config preservation:** import `root`'s
  `skills/vlt-setup/scripts/merge-config.py` (the `load_canonical_header` importlib idiom,
  `:106-112` — single source, never a copy) and call `merge_config()` in-process with a
  synthetic triple: an existing config whose module section carries a defined variable's map
  (with an extra vault-local sub-key) plus one undefined zombie key; a minimal module_yaml
  (`code`, metadata, one variable definition with a `default:`); answers whose `"module"`
  omits the variable. FAIL unless the variable survives byte-identical (vault-local sub-key
  included) **and** the returned merge report names the zombie in `removed` and the variable
  in `preserved`. This is A7-2's reproduction table promoted to a standing gate.
- **Probe 2 — manifest structural scope:** run/import `root`'s
  `skills/vlt-setup/scripts/verify-skill-manifest.py` against `root`'s own `skills/` tree
  (source == live for the repo case) and compare its computed entry set against the check's
  **own independent walk** of the shipped `vlt-*` dirs (marketplace `skills[]` ∩ disk, cruft
  excluded) — FAIL on any file the walk finds that the script's manifest lacks. The truth
  side is the check's own walk, not the script's (never confirm a surface's claim about
  itself — the build-23/E-group posture); a regression of the script back to an enumeration
  goes red on the first `references/` or `scripts/` file it drops.
- Doc header (`:30-53`): add one C-group line naming the check (build B7-2, doctrine ruling).

**Why.** R2 (wired by B7-1) plus the arc's Strand-2 finding: a durability net nobody can
prove is the defect class this arc opened with. The name matches `_E4_CHECK_NAME_RE`, so E4
inventories it the moment it is defined — the fixture cases in F6 are mandatory, not polish.

## F6 — `tools/test-package-lint.py`: fixture scripts + two covering cases + `CASE_FLOOR` 20

**Current state.** `build_fixture()` copies `merge-help-csv.py` into the fixture
(`:74`) and builds the R2-era tree; 18 cases; `CASE_FLOOR = 18` (`:212`); `covers=` required
per case (`:215-225`); baselines 1 and 9 assert whole-run exit 0, so **any** new gate check
must pass on the clean fixture or the baselines go red loudly.

**The exact change.**

- `build_fixture()` additionally copies the real `merge-config.py` and
  `verify-skill-manifest.py` into the fixture's `skills/vlt-setup/scripts/` (the
  merge-help-csv precedent — real scripts, never stubs, so the clean-tree baselines exercise
  the true code paths). Ensure the fixture satisfies probe 2 (its `vlt-mint/references/how.md`
  and `vlt-setup` trees are walked; seed whatever minimal file the probe needs if the
  fixture's shape leaves a probe vacuous — a probe that cannot fire on the clean fixture is
  the A7-1 vacuity again, so the builder must confirm probe 2 actually compares a non-empty
  set on the fixture).
- **Case 19** (`covers=("check_durability_nets",)`): swap the fixture's `merge-config.py`
  for a minimal destructive stub whose `merge_config()` rebuilds from answers only (the
  pre-B7-2 behavior, ~10 lines) → assert exit non-zero, `FAIL group C`, and the check's
  failure string.
- **Case 20** (`covers=("check_durability_nets",)`): swap the fixture's
  `verify-skill-manifest.py` for a stub whose walk filters out `references/` (the
  enumeration regression) → assert exit non-zero, `FAIL group C`, and the failure string
  naming the dropped path.
- `CASE_FLOOR` 18 → **20**, in the same edit that registers the cases (the ratchet comment
  at `:209-211` — bump in the same edit, never separately).

**Why.** R2's letter: a build that adds a gate check extends the fixture in the same build;
E4 fails the repo lint outright if F5 lands without this. The stub-swap shape is chosen over
editing the real scripts because it deterministically reproduces the *actual historical
defect* each probe exists to catch.

## Registration

**None.** No new skill or workflow — `verify-skill-manifest.py` is a script inside the
existing `vlt-setup` skill (rides its existing marketplace `skills[]` entry and help row,
like its three siblings). No convention `version:` moves and no `consumers:` list changes ⇒
no consumer walk, no re-ack; Group E's E1–E3 are unaffected (E4 gains the new check's
coverage via F6).

## Out of scope (dispositioned)

1. **A7-2's prior-strip lead** (the vlt-core 0.8.0→0.9.0 ledger entry as possible evidence of
   an earlier silent strip) — attached to this build's *acceptance*, not its scope, per the
   evidence-debt disposition (NOT BLOCKING: "the lead can only add a prior instance, never
   change the fix"). Carried as acceptance check 5.
2. **A `config.yaml` divergence snapshot in `vlt-upgrade` Step-1** — rejected-for-now; see
   brief-time disposition 8 (the ruled fix closes the destruction path script-side; a
   config-baseline net is unruled scope for a future filing if a residual loss path shows).
3. **A divergence net for `_meta/vault-rule-card.md` and the governance bundle** —
   already-covered-by: the card is *derived* and deliberately overwrite-always with edits
   surfaced by `governance_divergence` (`vlt-setup/SKILL.md:145`); governance files have
   their own Step-1 line (`vlt-upgrade/SKILL.md:40`).
4. **Manifesting `{tripwires}`, `settings.json`, `CLAUDE.md`, or any merge-not-replace /
   vault-grown surface** — rejected-because: the manifest is the *module-owned* net; those
   surfaces are vault-grown or merged by design (`vlt-setup/SKILL.md:171-178`, `:200-202`)
   and a SHA net over them would flag legitimate vault state as divergence.
5. **The Step-4 post-flight YAML schema** — untouched (disposition 2): the shrink report
   rides Confirm/Verify/ledger-Notes prose; extending a shipped parseable schema is a design
   act no ruling requested.
6. **`cleanup-legacy.py` behavior** — untouched; it enters the manifest net automatically
   (it ships in `scripts/`) but its never-invoked posture (`SKILL.md:284-288`) is not this
   build's business.
7. **The installer's `config.toml` `[object Object]` quirk** (`SKILL.md:40`) — upstream
   BMad's, filed upstream if ever; explicitly not Vault's to fix.
8. **A7-1's remaining fixture wishes beyond R2's letter** — B7-1 shipped the harness; this
   build extends it only where its own gate check requires (F6).

## Verification (unit, at rest — lifecycle step 5)

- **Harness:** `uv run tools/test-package-lint.py` → **20/20 green**, including the two new
  cases; record the R2 **red-then-green** mutation probe in the BUILT line (per B7-1's
  ledger check 4): (a) F5 landed without F6's cases → real-repo lint FAILs group E (E4 names
  `check_durability_nets`); (b) with F6 → exit 0. Also observe each new case red by
  neutering its probe (the B7-1 seed-one-defect discipline), then restore.
- **Gate:** `uv run tools/package-lint.py` on the repo → `A/B/C/E PASS, D SKIPPED` with the
  new check active (D/`--expect-version` is the release gate, not per-build; this is a
  non-release build — the version bump and Release section ride the arc's release build).
- **A7-2 reproduction, inverted:** re-run the capture's two-row fixture table against the
  built `merge-config.py` (temp config carrying `vault_structure` with a vault-local
  sub-key): the absent-from-answers row now **preserves** the block byte-identical and
  reports it in `module_keys_preserved`; a payload with a top-level (mis-nested)
  `vault_structure` no longer destroys; the correct-nesting row still merges exactly as
  today; a config carrying a genuine zombie key shows it in `module_keys_removed`. Also run
  a fresh-install shape (empty existing config, no `vault_structure` answer) and confirm the
  `module.yaml` default map materializes (`module_keys_defaulted`).
- **Manifest end-to-end:** against a temp installed-shape tree (skills + `.claude/workflows/`
  + `.claude/hooks/` + a decoy locally-minted `vlt-agent-test/` and a decoy vault-local
  hook), `--write` produces entries covering every shipped file including `references/*`,
  `scripts/*`, the workflows, and the vitals hook, and **excluding** both decoys and all
  cruft names; re-run after deleting one shipped file → `removed` names it; `--verify` after
  editing one live file → `diverged` names it. Against the repo tree, spot-assert
  `skills/vlt-lint/references/checks.md` and `skills/vlt-setup/scripts/merge-config.py`
  appear in the computed set (the two A7-3 classes, one file each).
- **Cross-file agreement greps (aids, not the record):** the manifest filename
  `.skill-manifest` and the cruft-exclusion names agree across
  `vlt-setup/SKILL.md`, `vlt-upgrade/SKILL.md`, and `verify-skill-manifest.py`; no restated
  SHA mechanics remain at `vlt-upgrade/SKILL.md:37` (single-home check).
- **Handshake:** no convention `version:` or `consumers:` moved ⇒ no bipartite walk owed;
  the check of record, `package-lint` **Group E**, runs green above regardless (never a
  hand-written handshake grep).
- **B1 preserve-path re-check:** confirm against the finished diff that `merge-help-csv.py`
  is untouched and the F4 durability paragraph holds (local mints outside the manifest net).
- **Scrub:** no personal or vault-local content in any changed shipped file — the new
  SKILL.md prose uses `$SKILL`/`$ROOT`/`{overlays}` placeholder idioms only; no vault name,
  no vault-local key name (the reproduction fixtures' vault-local key stays in the factory's
  temp dirs and this brief, never in shipped text). Delete any `.decision-log.md` before the
  build's single commit.

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable]** The durability-net gate check is live and proven fallible: real-repo
   `package-lint` passes A/B/C/E with `check_durability_nets` in the inventory;
   `test-package-lint` 20/20 with `CASE_FLOOR` 20; the recorded mutation probes show E4
   red without the covering cases and cases 19/20 each able to fail. Dischargeable at rest;
   re-confirmed at the arc's release gate (this is B7-1 ledger check 4's "first later build"
   instance — R2 observed binding in-arc).
2. **[ship-verifiable]** merge-config preservation at rest: the A7-2 reproduction table
   inverted (absent-from-answers ⇒ preserved + reported; mis-nested payload ⇒ non-destructive;
   zombie ⇒ removed **and named** in `module_keys_removed`; fresh install ⇒ defaults
   materialized). Dischargeable at rest and re-runnable by anyone from the scripts alone.
3. **[ship-verifiable — next ordinary vlt-core upgrade]** After the next upgrade of vlt-core,
   `_bmad/config.yaml` still carries the full `vault_structure` map **including its
   vault-local override key**, and the run's merge-config result JSON shows the preservation
   (`module_keys_preserved`/`module_keys_removed`) with no unreported removal. Bounded — the
   0.10.0 upgrade happens anyway; vault: vlt-core (owner-run, factory-readable evidence via
   the pasted result JSON + ledger entry).
4. **[ship-verifiable — next ordinary upgrade, either vault]** The manifest is re-written
   with structural scope on that upgrade: entry count rises from the enumeration-era 40 to
   the full walk (all 8 `references/*.md`, all `scripts/*.py` including the new script, the
   workflows, and the installed vitals hook present as entries), the shrink report lists
   removals only for files the new version legitimately stopped shipping, and the work
   vault's hand-widened 55-entry set is strictly contained (the silently-reverted vault
   ruling is honored by construction). Provenance stays legible in the ledger note: restored
   (`references/`, regressed v0.9.0) vs new (`scripts/` since v0.3.0; hook since v0.9.0's
   enforcement kit). Vault: vlt-core suffices; the work vault corroborates the 55-entry
   containment if reachable.
5. **[field-contingent]** A7-2's attached lead: whether the vlt-core 0.8.0→0.9.0 ledger entry
   ("map reconstructed, local key kept") evidences a **prior** silent strip — graded by
   reading vlt-core's upgrade ledger/git history at acceptance time. Vault that can produce
   the event: **vlt-core only** (owner-run; the factory cannot read it directly — evidence
   arrives as the owner's paste). Outcome changes the field-loss narrative, never this
   build's fix; if unread by arc closeout it goes to the watch register, not the gate.
