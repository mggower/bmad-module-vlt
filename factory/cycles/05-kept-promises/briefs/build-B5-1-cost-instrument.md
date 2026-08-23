---
title: 'Build #B5-1 — the cost instrument (nothing measures what a partner session loads; every boot-diet disposition downstream is chosen against these numbers)'
status: 'BUILT 2026-07-29 — F1 (tools/cost-manifest.py) + F2 (tools/test-cost-manifest.py, 7/7 green) + F3 (skills/reports/cost-baseline-2026-07-29.md) all landed; module-mode aggregates match brief grounding exactly (contract 38,271 / lint 41,202 / conventions 73,387); vault-mode run against vlt-core proven read-only by full mtime snapshot (zero files changed); 4 vault figures hand-verified against independent getsize (index 39,808 / log 151,536 / dispatch 78,255 / backlog 103,086); package-lint A/B/C/E PASS; scrub grep zero hits. Deviations/notes: (1) the verification expectation "vlt-core''s map lacks capabilities: — expect it named as fallback" no longer holds — at build time vlt-core''s structure map carries every canonical key (the 0.8.0 upgrade evidently refreshed it), so the live run reports "No fallbacks" and the fallback-with-naming path is exercised by the test fixture instead (7 missing keys, each asserted named). (2) The tolerant parser gained a second fallback shape beyond the brief''s letter: vlt-core''s log holds 4 real headers with type+partner swallowed inside the date bracket (`## [2026-07-18 track (chess-coach)] | …`); with the fallback pattern all 299 entries parse — exact parity with the raw `^## \[` grep count. (3) Figures are labeled `bytes` (wc -c equivalent), not the brief''s "chars" — bytes is what the estimators'' inputs and the grounding figures actually were (pre-ideation ruling 3: say what is measured); the band formula is unchanged. (4) The last-5-entries slice is sized as the byte region from the 5th-from-last entry header to EOF (the region a recency read spans in an append-only log), reported with its own words/band. Acceptance check 1 (ship-verifiable) evidence is on disk awaiting discharge; check 2 (field-contingent, work-vault run) is the owner''s.'
module_code: 'vlt'
created: '2026-07-29'
derives_from:
  - 'inbox/2026-07-29-082933-no-instrument-measures-session-token-cost.md (A5-13 — the whole filing: the absence claim, the by-hand baseline, dispositions (a)–(d))'
roadmap: 'skills/reports/inbox-evolution-arc5-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-07-29): pre-ideation ruling 1 (ONE shared measurement substrate — B5-1 lands first, so B5-1 lays it, B5-9 extends it); pre-ideation ruling 2 (MEASURE FIRST — the instrument runs against the work vault before A5-10..A5-14 are briefed; a one-shot in disposition (d)''s form suffices); pre-ideation ruling 4 (ships-decides — a tools/ artifact is tracked and public, so this is an arc build); grouping (B5-1 ships first, disposition-(d)-shaped at minimum); cross-filing ruling 1 (pre-hoc/post-hoc governance DEFERRED until these numbers land — it is B5-7''s first act, not this brief''s)'
risk: 'low — a new factory-side tools/ script plus its test; ZERO shipped-surface changes (no skills/ edit, no convention version bump, no consumer walk, no module-help row)'
---

# Build #B5-1 — the cost instrument

Goal: the module gains its first sizing instrument — `tools/cost-manifest.py`, a read-only
script that resolves and sizes what a partner session reads, in two modes: the **module
mode** sizes the declared read surface from module source at rest (disposition (a)); the
**vault mode** sizes the field-variable surfaces of a real installed vault — the half (a)
admits it cannot see, and the half pre-ideation ruling 2's work-vault run exists to price.
Its vault-reading core is the **shared measurement substrate** of pre-ideation ruling 1:
B5-9's enforcement-kit vitals extend this reader, never lay a second one.

Why now: this is the batch's measurement keystone (A5-13, capture verdict *GAP CONFIRMED by
exhaustive absence check*). B5-7 (the boot diet) and B5-8 (the whale re-cut) are gated
behind its numbers, and the arc-level pre-hoc/post-hoc governance ruling is deferred until
they land. Every day this doesn't exist, cost regressions accumulate with no bell — but the
bell itself (thresholds, tripping, escalation) is B5-9's, not this build's. This build
measures and reports; it never nags.

**Rejected alternatives in the parent filing are settled — do not re-litigate:**
disposition (c) (a lint cost tier) is rejected by the filing's own admission (it conflicts
with A5-14's lint-weight concern); disposition (b) (shipped session self-report) is not
rejected but deferred by disposition (d)'s letter — built only if the field-variable
numbers prove the schema/handshake cost worth paying, a call made after this instrument
runs, not in it.

## Brief-time dispositions

Ideation designated no leftover questions to B5-1, but the rulings it stands on jointly
force four design calls the roadmap left unstated. Each is recorded here with its
derivation; none reopens a ruled question.

1. **The tool is two-mode, not static-only.** Disposition (a)'s letter is a static
   manifest, and (a) "cannot see field-variable reads (index/log/orient)" by the filing's
   own admission. But pre-ideation ruling 2's work-vault run exists precisely to price
   A5-12's vault-age-scaling surfaces — a purely static tool cannot produce the numbers
   that gate B5-7/B5-8. And pre-ideation ruling 1's substrate ("one derive-only reader over
   existing records") *is* the vault-reading half. So the grouping's "disposition-(d)-shaped
   at minimum" resolves as: (a)'s static manifest **plus** a read-only vault mode; (b)'s
   shipped self-report stays unbuilt. This adds no field footprint — vault mode is a
   factory-side read of a vault tree, not a shipped surface.
2. **The substrate seam is a factored layer inside the script, factory-homed for now.**
   The vault-mode core — resolve the structure map from the vault's `_bmad/config.yaml`,
   enumerate records, size files, parse `{log}` headers per the contract's grammar
   (`vault-operating-contract.md:114`, grep patterns `:140-142`) — is factored as a
   distinct, documented layer (functions, not prose) with a header comment naming it the
   shared substrate per pre-ideation ruling 1. The header parser is **tolerant**
   (case-insensitive, paren-optional — the paren is omittable for partner-less generic
   operations per contract `:124` territory; A5-19's residual probe found strict parsing
   drops ~5% of real headers) so B5-9 inherits a correct parser instead of rewriting one.
   B5-9's open "module-owned code home" question (A5-19 Q1) is **not** answered here:
   homing the substrate in `tools/` today does not foreclose B5-9 shipping or porting it —
   that homing call re-opens at B5-9's brief as the roadmap already rules.
3. **Token figures are always a band, never one number.** Every sized surface reports
   `chars`, `words`, and an estimated-token band `[words×1.3 … chars/4]` — the two
   estimators the A5-13/A5-15 captures used, which disagreed by ~25% on the contract
   (7.3K vs 9.6K). Per pre-ideation ruling 3 (a check must state what it actually
   measures), the report header states the instrument's honest limit: it measures the
   **declared** read surface in bytes and estimates tokens; it does not observe what a
   live session actually read (that would be disposition (b), unbuilt).
4. **No thresholds, no baseline persistence, no gate wiring in v1.** The filing's "cost
   regression gate" lands as: a stable, deterministically-ordered, diffable report,
   re-runnable at release next to `package-lint.py`, compared by re-run + diff. Automated
   thresholds and tripping belong to the enforcement kit's vocabulary (B5-9); shipping a
   parallel threshold mechanism here would be exactly the second-substrate fork ruling 1
   prohibits.

## F1 — NEW `tools/cost-manifest.py`

Python, stdlib-only, run as `uv run tools/cost-manifest.py` from the repo root (the
`package-lint.py` idiom — `tools/package-lint.py` is the shape precedent: argparse,
deterministic output, exit 0 on success). Read-only in both modes — it never writes
anything but stdout. Output: a markdown report to stdout with stable section order and
stable within-section sort (by size desc, ties by path), so two runs diff cleanly.

**Module mode (default, no args; explicit `--module` also accepted).** Sizes the declared
read surface from module source at rest. Sections:

- **Per-partner fixed boot** — for each partner discovered by glob
  `skills/vlt-agent-*/SKILL.md`: the SKILL.md + the operating contract
  (`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`), each and
  summed. This is the eager surface every activation pays: all three partners open with a
  full contract read (identical opener at each partner `SKILL.md:22`; the ritual's other
  home is `contract:161` — grounded 2026-07-29 @ `9f05579`, both HOLD).
- **Governance stock** — each `_meta/conventions/*.md` (8 files, total 73,387 at HEAD)
  plus the other `_meta/` files, per-file and total, with the contract broken out. These
  are lazy point-of-use reads (partner SKILLs `:53-:56`, `vlt-lint:17`), labeled as such —
  the report distinguishes eager from contingent surface.
- **Skill surface** — every `skills/*/SKILL.md`, sorted desc, + total, labeled
  "SKILL.md files only" (the capture's correction: the 267,254 figure is not "all skills").
- **Workflow assets** — `skills/vlt-setup/assets/workflows/*.js`, each + total.
- **Named aggregates** — the whales the captures track, printed as one block so
  regressions are one diff line: contract; lint SKILL; dispatch SKILL; conventions total;
  frontmatter.md; all-SKILL.md total. (At HEAD these are 38,271 / 41,202 / 38,285 /
  73,387 / 22,977 / 267,254 — the tool computes them fresh; these figures are this
  brief's grounding, not constants to hardcode.)

The eager/contingent grouping mirrors the ritual's two documented homes (partner SKILLs
`:22-:25`, `contract:161-167`). The tool encodes that grouping as data with a comment
naming both homes; it does **not** parse activation prose. This creates a soft third home —
accepted, noted in Out of scope (6).

**Vault mode (`--vault <path>`).** Sizes an installed vault's field-variable surfaces:

- **Structure map resolution** — read `<path>/_bmad/config.yaml`, key
  `vlt.vault_structure` (grounded live on vlt-core: nested under the `vlt:` section). Any
  key missing there (vlt-core's map, e.g., predates `capabilities:`) falls back to the
  canonical default map in `skills/vlt-setup/assets/module.yaml:39` `vault_structure.default`
  — the SSoT — and the report **names each fallback** rather than silently defaulting.
  A vault with no `_bmad/config.yaml` at all → clear error, exit nonzero.
- **Beat-2 variable surfaces** (the A5-12 pricing targets, read list per `contract:167`):
  `{index}`; `{log}` — full size **and** the last-5-entries slice (the contract's own
  recency idiom, `:140`); `{backlog}`; per-partner `identity.md` + `thread.md` +
  `capabilities/` total (glob `{partners}/*/`); `_agent/dispatch.md` full size (the open
  slice is semantic — the file size is the honest measurable, and the report says so).
- **Installed governance** — the vault's `{conventions}` dir, overlays dir
  (`_agent/conventions/`), and `.claude/workflows/*.js`, per-file + totals.
- **`{log}` derivations (the substrate seed)** — via the tolerant header parser
  (disposition 2): total entry count, count by operation type (`ingest` explicitly — the
  count `vlt-lint:3`'s "after several ingestions" has no counter behind it), count by
  partner, first/last entry dates. Derive-only display; no thresholds, no judgments.
- **Context section** — `{sessions}` dir: file count + total size (not a boot read;
  labeled context).

**Why:** discharges A5-13's core gap (no instrument anywhere — `tools/` was package-lint
only, no cost surface in lint/track/session schema; absence re-verified at HEAD this
brief); lays ruling 1's substrate; produces the numbers ruling 2 holds B5-7/B5-8 behind.

**Scrub:** `tools/` is tracked and public. No personal or vault-local content in the
script: no hardcoded vault paths (vlt-core's path appears nowhere), examples in `--help`
and comments use placeholder paths (`/path/to/vault`).

## F2 — NEW `tools/test-cost-manifest.py`

Mirrors the `tools/test-package-lint.py` idiom (stdlib, temp-dir fixtures, exit nonzero on
failure; run as `uv run tools/test-cost-manifest.py`). Covers:

- **Fixture vault** built in a temp dir: minimal `_bmad/config.yaml` with a partial
  `vlt.vault_structure` (to exercise fallback-with-report), a `{log}` with known headers
  including the tolerant-parser edge cases (mixed case, paren-less generic-op header, a
  non-header `##` line that must not match), an index, a backlog, two partner dirs (one
  with `capabilities/`, one without), an overlays dir. Assert: sizes exact, entry counts
  exact (total / by type / by partner), fallbacks named in output, missing-config error
  path exits nonzero.
- **Module-mode self-check** against the real repo: assert the named aggregates equal
  ground truth the test computes itself with its own `os.path.getsize` walk — never
  hardcoded figures (source moves; the test must not fossilize HEAD's numbers).
- **Determinism**: two consecutive runs of each mode produce byte-identical output.
- Fixture content is placeholder-only (public repo).

## F3 — the baseline report (build-time artifact, not shipped)

After F1/F2 verify, the builder runs both modes — module mode at HEAD, vault mode against
`{field-vault}` — and files the output as
`skills/reports/cost-baseline-2026-07-<dd>.md` with a short header stating: (1) this is
the measure-first gate artifact pre-ideation ruling 2 names — B5-7's and B5-8's briefs
cite it; (2) what it is **not** — the work-machine consumer vault's numbers (the
originating signal's vault, which this machine cannot read; that run is the owner's, see
Acceptance). `skills/reports/` is gitignored — this artifact is factory-local by design,
like `spike2-projection-baseline-2026-07-25.md`.

## Registration

**None.** A `tools/` script registers nothing: no `module-help.csv` row (the
`package-lint.py` precedent — tools are release-contract documentation, not installed
surface), no workflow, no convention edit, no `version:` bump ⇒ no consumer walk, no
re-ack. The shipped `skills/` tree is untouched by this build.

## Out of scope (dispositioned)

1. **Disposition (b), the shipped session self-report** — deferred by disposition (d)'s
   letter; built only if the vault-mode numbers prove the field-variable half matters.
   Its schema touch (frontmatter consumers, handshake) is deliberately unpaid here.
2. **Disposition (c), a lint cost tier** — rejected in the filing (conflicts with A5-14);
   settled, do not re-litigate.
3. **Thresholds, tripwires, escalation, persisted baselines with automated comparison** —
   B5-9's (the enforcement kit extends this build's substrate; brief-time disposition 4).
4. **Any boot-diet change** (contract digest, consult-lite boot, orient bounds, whale
   re-cut) — B5-7/B5-8's, gated behind this build's numbers; the pre-hoc/post-hoc
   governance ruling is B5-7's first act (cross-filing ruling 1), not this brief's.
5. **B5-9's substrate-homing question** (module-owned code home, A5-19 Q1) — deliberately
   left open by brief-time disposition 2; re-opens at B5-9's brief per the roadmap.
6. **A read-list drift check** (the tool's eager/contingent grouping vs its two prose
   homes, partner SKILLs `:22-:25` / `contract:161-167`) — a real seam, accepted for v1
   with a naming comment; if it bites, it is tripwire/package-lint territory, filed then.
7. **Sizing `{research}`/`{wiki}` content** — partner sessions read wiki pages
   point-of-use and unboundedly; sizing knowledge content is not sizing the *machinery*,
   which is what A5-13 filed. Vault mode's totals deliberately stop at the operating
   surfaces + governance.

## Verification (unit, at rest)

- `uv run tools/test-cost-manifest.py` → exit 0 (fixture assertions + module-mode
  self-check + determinism).
- Module-mode run at HEAD: spot-check ≥3 named aggregates against independent `wc -c`
  (at brief-time HEAD `9f05579`: contract 38,271; lint SKILL 41,202; conventions total
  73,387 — recompute if source has moved).
- Vault-mode run against vlt-core completes read-only (no write anywhere under the vault —
  verify by mtime snapshot before/after or `git status` if the vault is clean), reports
  the structure map's missing-key fallbacks (vlt-core's map lacks `capabilities:` at
  brief time — expect it named).
- **Handshake re-check: not applicable** — no convention `version:`, `consumers:`, or
  structure-map change in this build (package-lint Group E is the check of record when one
  occurs; none does).
- Mid-arc packaging lint: `uv run tools/package-lint.py` groups A/B/C/E → PASS (the
  shipped tree is untouched; this confirms it).
- Scrub: grep the two new tools/ files for `vlt-core`, `{owner}`, `/Users/` → zero hits.
- Delete any `.decision-log.md` before commit; one commit for the build.

(No Release section — B5-1 is not the arc's release build; the version bump rides the
arc's release build per standing practice.)

## Acceptance (live — appended to the roadmap ledger)

1. **[ship-verifiable] The baseline lands and is trustworthy.** The tool has run in both
   modes — module mode at the build's HEAD, vault mode against vlt-core — and the dated
   baseline report is on disk in `skills/reports/` (F3's shape: gate-artifact header +
   honest not-the-work-vault statement). At least three vault-mode figures hand-verified
   against independent `wc -c`/`grep -c` on vlt-core (a discharge that could fail: a
   parser that miscounts log entries or a size that disagrees with `wc -c` fails this
   check). Bounded: the factory runs this the day the build lands; B5-7/B5-8's briefs
   cite the artifact as their measure-first gate.
2. **[field-contingent] The work vault's numbers.** The owner runs
   `uv run tools/cost-manifest.py --vault <work-vault-path>` on the **work-machine
   consumer vault** — the originating signal's vault, which the factory machine cannot
   read — and files the output back (ordinary inbox filing or a report drop). This is
   the vault named at brief time per the anatomy's rule; only the owner can produce the
   event. Non-gating at closeout, but pre-ideation ruling 2 names the work vault, so
   B5-7's brief should not choose its dispositions without these numbers if they exist
   by then — check 1's vlt-core baseline is the floor, this is the signal-bearing
   measurement.
