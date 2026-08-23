# 02 — Module map: the shipped `vlt` surface (raw findings)

Handoff domain: the shipped module itself — every skill, the governance bundle, the
enforcement layer, cross-cutting patterns, and weak points visible from source.
Grounded against the working tree at commit `a117f4f` (v0.6.0, Arc 3 shipped). All
paths relative to `{factory-root}/` unless absolute.

Shipped surface inventory (all verified on disk):

- 14 skills under `skills/` — matches `.claude-plugin/marketplace.json:21-36` exactly
  (package-lint group C5 enforces the bijection, `tools/package-lint.py:189-196`).
- Governance bundle: 7 conventions + 5 personas + the operating contract at
  `skills/vlt-setup/assets/governance/_meta/`.
- 2 dynamic workflows at `skills/vlt-setup/assets/workflows/` (council + lint-full).
- 3 setup scripts (`merge-config.py`, `merge-help-csv.py`, `cleanup-legacy.py`),
  `module.yaml`, `module-help.csv` (15 lines = header + 14 rows, one per skill).
- 3 mint templates at `skills/vlt-mint/assets/`.
- `tools/`: `package-lint.py` + `test-package-lint.py` (release-contract documentation,
  not part of the own-the-apply copy surface).
- Versions agree: `module.yaml:4` `module_version: 0.6.0` == `marketplace.json:16`
  `"version": "0.6.0"`.

---

## 1. Skill-by-skill map

### 1.1 `vlt-setup` (skills/vlt-setup/SKILL.md, 287 lines) — install/provision

Purpose: installs the module into a vault (the vault IS the project). Two jobs: config
write + vault provisioning (SKILL.md:12-15).

Key mechanics:
- **Config** → three files: `_bmad/config.yaml` (core at root + `vlt:` section with the
  materialized `vault_structure` map), `_bmad/config.user.yaml` (user-only keys), and
  `_bmad/module-help.csv` (SKILL.md:17-21). Both scripts are anti-zombie (existing `vlt`
  entries stripped before fresh write, SKILL.md:23). `{project-root}` is a **literal
  token inside config values**, resolved only at use time (SKILL.md:25, 80).
- **Tooling traps documented in-skill** (SKILL.md:77-81): must use `uv run` (PEP 723
  pyyaml dep); `{project-root}` must NOT be passed literally to `--config-path`
  (creates a junk dir — a real past defect); scripts anchor to the skill's install dir,
  not cwd. `--legacy-dir` is explicitly forbidden (SKILL.md:101) because it deletes
  `_bmad/core/config.yaml` belonging to the base BMad install.
- **Installer-interop stance** (SKILL.md:35-41): the BMad installer writes its own
  `config.toml` + staging dirs; vlt's runtime reads only `config.yaml`. Setup never
  reconciles/deletes the TOML (known installer wart: `vault_structure` serialized as
  `"[object Object]"` — acknowledged in the confirm step, SKILL.md:280).
- **Provisioning** (SKILL.md:107-252), step by step:
  1. Seed `wiki/`, `log.md` (with header — vlt-ingest's grep assumes it exists,
     SKILL.md:114), empty `index.md`; never touch existing pages.
  2. Governance bundle copy `./assets/governance/_meta/` → `{root}/_meta/`,
     **skip-if-present per file** (vault's version wins, SKILL.md:141-144).
     Then two module-owned overwrite-always durability artifacts:
     - **Stock baseline** (build-6): each shipped convention copied to
       `{overlays}/.baseline/{name}.md` (SKILL.md:147) — the divergence reference for
       lint + upgrade.
     - **Skill-asset SHA-256 manifest** (build-18): `{overlays}/.baseline/.skill-manifest`,
       one `<sha256>\t<path>` line per shipped file across shipped `vlt-*` SKILL.md +
       assets/ + installed workflows, excluding locally-minted `vlt-agent-*`
       (SKILL.md:149). Computed from the *installed* files at install time.
  3. (2a) Workflows `./assets/workflows/*.js` → `{root}/.claude/workflows/` —
     **module-owned, overwrite on every run** (SKILL.md:160-162).
  4. `CLAUDE.md`: write minimal pointer + `## Preferences` home if absent; if present,
     only additive heading-scoped edits — never clobber (SKILL.md:164-185).
  5. Partner layer: idempotent legacy single-`thread.md` → two-file
     (`identity.md`/`thread.md`) migration (SKILL.md:190); seed both files per shipped
     partner if absent; seed frontmatter-less `backlog.md`; ensure `_agent/mint/` and
     `{capabilities}/families/` exist (SKILL.md:237-238). Per-partner `capabilities/`
     folders are lazy.
  6. (§5) Seed the generic-BMad installer cache `~/.bmad/cache/custom-modules/bmad-module-vlt`
     with `.claude-plugin/` marker + `module.yaml` at the standard probe path, refreshed
     every run, skipped silently if `~/.bmad` absent (SKILL.md:240-252).
- Dependency checks are warn-never-block; host-provided skills count as present
  (SKILL.md:254-261). `cleanup-legacy.py` ships but is **explicitly never invoked**
  (SKILL.md:267-271 "Do Not Run Installer Cleanup").

Design decisions visible: setup is strictly additive/non-invasive; module-owned vs
vault-owned files are explicitly two overwrite regimes (workflows/baseline/manifest =
overwrite-always; governance/partner memory/CLAUDE.md = skip-if-present/never-clobber).
`module.yaml` `vault_structure.default` is the declared single source of the structure
map (module.yaml:41-43 "CANONICAL default map — the SINGLE SOURCE OF TRUTH"); the
SKILL's own table is marked "illustrative only" (SKILL.md:53).

### 1.2 `vlt-upgrade` (skills/vlt-upgrade/SKILL.md, 134 lines) — durable upgrade

Purpose: refresh shipped bits without destroying vault-local evolution. Governing rule:
"two classes of evolution, two fates" (SKILL.md:12, contract §Durability).

Mechanics — five steps:
- **Step 1 pre-flight** (SKILL.md:29-41), always from the intact vault; snapshot:
  minted `vlt-agent-*` not in `module.yaml agents[]`; overlays; **base convention
  divergence** vs `.baseline/`; **skill-asset divergence** vs `.skill-manifest`
  (build-18 — diverged file contents are copied into the working note before refresh,
  SKILL.md:36); mint history; capabilities + families (shipped vs vault-grown noted);
  governance edits. Missing baseline/manifest → `baseline_missing` /
  `skill_manifest_missing`, seeded best-effort this run.
- **Step 2 apply** (SKILL.md:44-47): prefer **own-the-apply** (merge-copy shipped
  `vlt-*` skills + `_meta/` + workflows from module source; never delete unshipped
  dirs, never write agent zone, never overwrite overlays); fallback **bracket the
  installer**. Own-the-apply is a *filesystem* copy, so dev cruft must be excluded:
  `.decision-log.md`, `__pycache__/`, `*.pyc`, `.DS_Store`, `reports/` (SKILL.md:46 —
  the rsync exclude list; a stray `.decision-log.md` would overwrite the vlt-mint
  relocation stub).
- **Step 3 reconcile** (SKILL.md:49-78):
  1. **B1 (the must-ship)**: re-run `merge-help-csv.py --live-skills-dir` so locally
     minted registry rows are preserved (SKILL.md:51-61); confirm JSON
     `local_mints_preserved`; `header_migrated: true` = one-time after/before →
     preceded-by/followed-by rename noted in ledger.
  2. **B2 insurance**: restore any minted-partner dir a destructive apply removed
     (no-op on own path, but always verified — SKILL.md:63).
  3. Conventions: confirm overlays intact, refresh baselines to new shipped versions;
     **overlay-subsumption pass** (build-18, SKILL.md:66) — diff each overlay against
     the newly refreshed base; where the base now covers an overlay addition (it was
     upstreamed), *prompt* to retire the overlay section — human-gated, never
     auto-delete. Rationale stated: `overlay_not_append_only` only catches verbatim
     heading duplication; a reworded shadow escapes.
  4. Capabilities: agent zone untouched; if a *shipped family's* invariants changed,
     fire the propagation check → `family_invariant_drift`, human reconciles
     (SKILL.md:68).
  5. Migrations (idempotent), all under the **relocation-migration discipline**
     (SKILL.md:71: stub the old path, never touch parallel-worktree copies, re-point
     open dispatch pointers — dedup key resets on a move): decision-log relocation
     (§A1), overlay lift (first upgrade of an already-diverged vault), proto-spec
     retrofit (human-gated `_agent/handoffs/` → `{specs}` per spec.md).
  6. Provision hand-off: invoke `vlt-setup` reconfigure — never reimplements it
     (SKILL.md:78, 127); this also refreshes the manifest and the installer-cache seed.
- **Step 4** post-flight YAML divergence report (SKILL.md:84-99) — parseable keys
  incl. `base_divergence`, `skill_asset_divergence`, `family_invariant_drift`.
  Detect-and-report, never auto-merge (SKILL.md:101).
- **Step 5** the append-only `{upgrade_ledger}` (`_agent/upgrade-ledger.md`) — opened
  at pre-flight, completed at post-flight (SKILL.md:103-123).

### 1.3 `vlt-ingest` (skills/vlt-ingest/SKILL.md, 165 lines) — the single wiki writer

`depends_on: ["frontmatter@3", "wiki-index@2", "wiki-consolidation@1",
"wiki-supersession@1", "write-verification@1"]` (SKILL.md:4).

Purpose: integrate a source; "what changes in the wiki because of this?" (SKILL.md:11).
The **single writer of canonical wiki pages** (SKILL.md:13).

Flow: re-ingest check (grep `{log}` for the source token, with `2>/dev/null`
defense for pre-setup vaults, SKILL.md:30-38) → credential scan with explicit pattern
list (SKILL.md:42) → read source → **heavy-source prep/interpret split** above ~15k
words (SKILL.md:50-63): a mechanical prep sub-agent fetches/normalizes/deposits to
sources/ and returns a *neutral navigational brief* — "never the raw body; never an
interpretation" (SKILL.md:54); three stated invariants: single-writer holds, brief is a
map not territory (quotes re-verified), map-not-digest (a pre-interpreted digest
"primes and quietly corrupts" the fresh read, SKILL.md:61). Then takeaway interview
(skipped in partner-fronted mode, SKILL.md:69) → research note (or hand-off branch:
reuse a handed `{research}` note, SKILL.md:73) → wiki update with required
near-duplicate check + inline consolidation merges per wiki-consolidation.md
(SKILL.md:97-135) → index update per wiki-index.md, `category:` ↔ H2 kept in lockstep
(SKILL.md:139) → `{log}` entry → **verify and attest** (tier-1 checklist from
write-verification.md, fail-open, then `verified_by: vlt-ingest` / `verified_at`,
SKILL.md:151-159).

### 1.4 `vlt-research` (105 lines) — web investigation

`depends_on: ["frontmatter@3", "write-verification@1"]` (SKILL.md:3). Files a dated
`{research}` note; web tooling is host-provided, never hardcoded (SKILL.md:19). Brief +
feasibility gate (SKILL.md:21-32; partner-fronted mode skips the interview), vault
check before web (SKILL.md:34-38), depth-calibrated research with a `.WIP` checkpoint
keyed to interruption-risk not call-count (SKILL.md:50), note schema (SKILL.md:56-79),
verify/attest (SKILL.md:81-85), then the **offered wiki pass**: structured hand-off
payload (`note`/`concepts`/`supersession`/`prefs`) to the Librarian — never writes the
wiki itself (SKILL.md:95-99).

### 1.5 `vlt-query` (60 lines) — wiki-only synthesis

No `depends_on` (its only writes are optional research notes; frontmatter is referenced
prose-level at SKILL.md:46). Reads index → pages; provenance tag on every claim
("— general knowledge, not in the vault" marking, SKILL.md:32); contradiction ranking
by recency+sources (SKILL.md:33); file-back rubric: ≥3 pages / likely-to-recur / novel
conclusions (SKILL.md:41); canonical-page syntheses hand to the Librarian (SKILL.md:47).

Note: vlt-query writes research notes per `frontmatter.md` but carries **no
`depends_on` ack and is not in any convention's `consumers:`** — it also runs no
attestation step (write-verification's consumers list omits it too). See §5.7.

### 1.6 `vlt-extract` (116 lines) — wiki → PARA deliverable

`depends_on: ["extraction@2", "wiki-supersession@1", "frontmatter@3",
"write-verification@1"]` (SKILL.md:4). "The one sanctioned way a partner writes into
PARA" (SKILL.md:13). Interview → read wiki with the **hard thin-wiki gate** (≥2
contributing pages or stop, SKILL.md:38) → synthesize (cite via wikilinks; carry
forward caveats; `.draft.md` for large artifacts, SKILL.md:50) → prompt for PARA folder
(no default, SKILL.md:54) → near-duplicate check with update-in-place default
(SKILL.md:64) → write (`author: hybrid` fixed; `trust:` confirmed by depth; no `key:`,
SKILL.md:87) → log → verify/attest (SKILL.md:106-110).

### 1.7 `vlt-lint` (170 lines) — the enforcement net

`depends_on: ["frontmatter@3", "wiki-index@2", "wiki-supersession@1", "extraction@2",
"write-verification@1"]` (SKILL.md:4).

- **Scoping** (SKILL.md:19-37): scoped-by-default off the last `lint` `{log}` timestamp
  (validated as a real datetime; fallback to full); full mode >~30 pages delegates to
  the `vlt-lint-full` workflow (SKILL.md:39-45) — the SKILL keeps the writes
  (single-writer safety "lives here in the SKILL, not in the parallel finders",
  SKILL.md:43) and fills the report slots the workflow doesn't sweep (PARA attestation,
  governance checks).
- **Tier 1** structural checks (SKILL.md:53-62), with the attestation **re-scoping
  rule**: fresh-attested files skip tier-1 except a ≈1-in-5 sample audit (SKILL.md:57).
  Findings: missing targets (cross-layer-aware), frontmatter/Bases drift
  (`summary ≤160`, `category` = index H2, `topic` a list), attestation findings
  (`para_missing_attestation` — the out-of-path-write net; `unattested_write`
  informational for pre-convention files; `attestation_stale` → quiet re-run),
  `review_due` (never auto-resolved).
- **Tier 2** (SKILL.md:64-81) — the sweep, including the whole **governance suite**:
  - convention coherence — the version-handshake validator (stale ack / unacknowledged
    / dangling consumer), SKILL.md:74; explicitly never auto-bumps an ack (SKILL.md:95).
  - enforcement doctrine meta-check — `enforcement_missing` / `deferral_invalid` /
    `deferral_expired` / `declared_untripwired` / `convention_meta_missing`, SKILL.md:75.
  - convention base divergence vs `.baseline/` (+ `baseline_missing`), SKILL.md:76.
  - overlay append-only (`overlay_not_append_only`, `overlay_orphan`) — overlays
    deliberately unversioned, invisible to the handshake by design, SKILL.md:77.
  - capability lane-safety (`capability_lane_violation` / `scope_mismatch` /
    `weight_mismatch` / `skill_missing`) with the sources/-new-file-deposit carve-out,
    SKILL.md:78.
  - family-invariant conformance (`family_invariant_violation`, `family_instance_missing`),
    SKILL.md:79.
  - personalized-extraction firewall (`method_not_in_sources`,
    `method_in_personalization`), SKILL.md:80.
- Auto-fix only the safe set (SKILL.md:83-95); **lint-as-attester narrowly** — attests
  only files its auto-fix touched (SKILL.md:93). Merge candidates go to `{backlog}`;
  ingest resolves them (SKILL.md:97-105). Structured YAML report with
  `files_checked` vs `files_listed` and `coverage_caps` — "never present a capped sweep
  as exhaustive" (SKILL.md:107-153).

### 1.8 `vlt-dispatch` (260 lines) — the partner communication bus

`depends_on: ["spec@1"]` (SKILL.md:3). One record (`_agent/dispatch.md`) with a drain,
three modes; every mode emits the identical pointer line drained by the identical
pickup loop (SKILL.md:17).

- **`daily`**: per-source line-count **watermark** idempotency (SKILL.md:73-81);
  classify against the **live roster** — slug derived mechanically as skill basename
  minus `vlt-agent-` (SKILL.md:85-87); routing rules incl. "a captured source/link →
  the Librarian, never the Researcher" and **no-owner → flag-and-skip, write no
  pointer** (a persistent no-owner pointer would rot the ledger, SKILL.md:94); run
  block format with `routed through line N` header (SKILL.md:100-113); closes by
  printing the standing ledger inline (SKILL.md:142).
- **`relay`**: thin scribe for pre-addressed handoffs; the **relay-when-done reflex**
  is owned here as its single home (SKILL.md:152-154), incl. its spec extension: fire
  one relay per spec `consumers:` partner on a version bump. Liveness check on
  `to-slug` (phantom-recipient failure mode #4, SKILL.md:162). **Idempotency keyed on
  `(handoff-path, to-slug)`** (SKILL.md:166-174): open pointer → no-op (spam, #1);
  checked-off → fresh pointer (stale-spec re-notify, #2). Depends on the
  stable-path/update-in-place handoff lifecycle whose single home is the operating
  contract (SKILL.md:178).
- **`ledger`**: read-only grep-built board, no log entry (SKILL.md:201-215, 239).
- **The pickup loop** (SKILL.md:219-228): partner greps `'[ ] \`slug\`'`, acts, flips
  its own lines only, stamps `✓ picked up`. Two writers cleanly separated: dispatch
  appends blocks; recipients flip statuses (SKILL.md:21).
- Hard human-zone boundary: only `daily` mode reads `daily/`, only when invoked; never
  edits, never auto-ingests, never runs unprompted (SKILL.md:45). Per-mode Verify
  sections (SKILL.md:241-260).

### 1.9 `vlt-mint` (167 lines) — the self-evolution engine

`depends_on: ["spec@1", "frontmatter@3"]` (SKILL.md:3). Three phases with exit gates.

- **Phase 1 Ideate** (SKILL.md:28-68): resolve the kind (`add a capability` routes by
  `write_scope`; migrate/retire; family ops; new partner / persona self-edit /
  convention edit / retire partner). The **boundary classifier** on every kind: "does
  this mint create a rule someone else must obey?" → declare a bell or a complete
  tripwired deferral, else record `non-boundary: <why>` (SKILL.md:42). New-partner
  "becoming conversation" with native-lightweight default and a `bmad-agent-builder`
  escape hatch mapped onto the Vault contract (MEMORY dropped — knowledge lives in the
  wiki, SKILL.md:48-51). Horizontal-vs-vertical archetype guidance: a domain partner
  running a longitudinal loop **wears `vlt-track`** via a `capabilities/track.md`
  pointer + Loop profile rather than minting a duplicate (SKILL.md:55). Gated kinds get
  a **resumable planning doc** at `_agent/mint/{date}-{slug}.md`; ceremony-free kinds
  don't (SKILL.md:57-66). The permanent decision log is `_agent/mint/decision-log.md`
  — agent-zone, clobber-proof (build-6; legacy in-skill `.decision-log.md` migrates with
  a pointer stub, SKILL.md:61).
- **Phase 2 Validate** (SKILL.md:70-98): the `kind → council` map is owned **only** in
  the workflow's `KIND_PANEL` (single-home fix; vlt-mint keeps just the none-predicate,
  SKILL.md:76). Council-none: light or lane-rightful-additive capability, migrate,
  retire, create/extend family. Gated: second-writer/lane-ownership capability, family
  invariant change, new partner, self-edit, convention edit, retire partner. Council
  invocation stages the mint in the **live tree** (plugin-cache fix) and passes the
  live absolute `personasPath` (SKILL.md:93-94); verdict capture is mandatory
  (SKILL.md:95). Exit gate includes: a boundary-creating mint cannot pass with neither
  a bell nor a valid deferral (SKILL.md:98).
- **Phase 3 Build** (SKILL.md:100-159): author from locally-owned scaffolds (the
  contract guarantee, SKILL.md:106); **spec consumer lock** — a mint that makes a
  partner consume a spec edits that spec's `consumers:` in the same change
  (SKILL.md:108, spec.md:76). Light capability = own-zone file, nothing registered,
  self-grow shortcut = one decision-log line (SKILL.md:112). Heavy = op skill from
  template + registry row. Convention edit routes **overlay (vault-local addition,
  no version bump, no consumer walk) vs base + handshake** (SKILL.md:131-132); the
  base-edit ceremony (SKILL.md:138-141): apply → bump `version:` only for rule changes
  → walk every `consumers:` skill and re-pin its `depends_on` → **exit gate: mint
  cannot close with any stale ack**. Step 4 registration carries the **always-quote CSV
  rule** (SKILL.md:149) and the live-registry + install-manifest mirroring
  (SKILL.md:151-152). Retire a partner archives `identity.md`/`thread.md` to
  `{archive}` — never deletes (SKILL.md:145).

### 1.10 `vlt-review-council` (54 lines) — conversational front for the panel engine

No `depends_on`. The engine is the workflow (`.claude/workflows/vlt-review-council.js`);
this SKILL resolves subject + live paths, invokes, routes the verdict (SKILL.md:12).
`vlt-mint` calls the workflow directly, not through this SKILL (SKILL.md:12, 23).
Debate → full panel; verdicts worth keeping are handed to the Librarian to file
(SKILL.md:45). Explicit "does not re-implement the panel in prose" (SKILL.md:51). No
retro mode (SKILL.md:54).

### 1.11 `vlt-track` (113 lines) — the shared longitudinal-loop hand

`depends_on: ["extraction@2", "wiki-supersession@1"]` (SKILL.md:4). Persona-neutral,
profile-driven: "one verb, many subjects" (SKILL.md:13); the wearing partner's
`capabilities/track.md` Loop profile supplies `{root}`, `{target}`, subject model, data
streams, log tag, and the **non-negotiable gate** (SKILL.md:31-40). Three beats:
design (wiki-grounded; thin wiki → stop and hand off, SKILL.md:50), log (agent-zone
only; operational-log discipline — state never method, SKILL.md:61), review/adjust
(trend-not-noisy-point; re-extract in place, SKILL.md:67-69). The protocol write is a
**personalized extraction**: `sources:` = wiki pages only; `personalization_sources:` =
agent-zone streams, separate field so the invariant is mechanically checkable
(SKILL.md:71-96). The wearing partner's widening **must be sanctioned by its own gated
mint** or vlt-track stops (SKILL.md:98). Verify re-asserts the firewall and the named
non-negotiable gate (SKILL.md:111-113). Coins its own `track` log type (contract's type
set is non-exhaustive, SKILL.md:109).

### 1.12 The three partner agents (`vlt-agent-librarian` / `-researcher` / `-creative`)

63-66 lines each + a metadata-only `customize.toml` (override surface deliberately off
— "memory agents default the customization surface to off",
vlt-agent-librarian/customize.toml:18-23; memory lives in in-vault
`identity.md`/`thread.md`, `agent_type = "memory"`).

Shared skeleton (mirrors `partner-agent-template.md`): persona + explicit "not built
from a six-file sanctum… become yourself by reading the vault" (librarian:10); a
non-negotiable; the **two-beat activation ritual** (Beat 1 first-breath =
SKILL persona modulated by `identity.md` `## Self`/`## Bond`/`name`; Beat 2 orient =
index, log, backlog, thread, dispatch slice drain, capabilities folder —
librarian:22-25); four activation branches (first meeting cold-open, cold×headless
deferred ceremony, partner-invoked no-greeting, normal); "What you do" delegating to
ops; reflection = file-to-backlog freely, never build unasked; ending-a-sitting = one
session note + identity/thread updates, with the JIT frontmatter.md read reminder
(librarian:53); the drift-vs-rebirth line ("drift breathes, ratification reborns",
librarian:57).

Differentiation: Librarian = sole canonical-wiki writer, owns ingest/lint/query,
carries maintenance cadence (librarian:45-47); **extraction belongs to the Creative,
not the Librarian** (librarian:41 — a making act, not custodial). Researcher =
grounded challenge, research/query + BMad thinking tools, hands findings to the
Librarian (researcher:35-46). Creative = wiki→PARA maker, owns `vlt-extract`, treats
the ≥2-page gate as a feature (creative:37).

---

## 2. The governance bundle (`skills/vlt-setup/assets/governance/_meta/`)

### 2.1 The operating contract (`vault-operating-contract.md`, 249 lines)

Deliberately **not** version-handshaked (single-home + pointers instead; confirmed — it
carries no `version:`/`consumers:` keys, only note frontmatter, lines 1-11). Owns:

- The structure map table (lines 29-46) — resolution order override → default; the
  vault root is the project root.
- **The three layers + hard write boundaries** (lines 48-60): sources/ read-only;
  `_agent/`+`_meta/` partner-owned (ad-hoc owned folders sanctioned, line 54); PARA
  human-curated, reached only via extraction. Human zones `_vault/`, `new/`, `daily/`
  (lines 62-77: read-on-request only, no auto-ingest, "That instinct is the bug").
  Tool zones `.claude/`, `_bmad/` (line 81).
- **Durability across upgrades** (lines 83-99): two classes/two fates; overlay
  mechanics (append-only, merged on read, handshake pins the *base*); hand-edited base
  = divergence, detect-and-report.
- research-vs-wiki distinction (lines 101-109); the `{log}` format + non-exhaustive
  type set + grep patterns (lines 111-139); naming conventions (141-147); frontmatter
  pointer — schema lives only in frontmatter.md (149-151); MOCs never partner-edited
  (154-156).
- **Activation ritual** (158-174) incl. the dispatch-slice drain as "the one orient
  read that may mutate shared state" (line 166), cold-start, cold×headless,
  partner-invoked.
- Partner memory two-file split + the two-tier identity line (176-189); **Capabilities**
  (191-202): light/heavy derive from `write_scope`; shared lane = synthesized
  single-writer lane; new-file `sources/` deposits are lane-safe; families Model B.
- User preferences → `CLAUDE.md ## Preferences` single home (204-206).
- **Sessions, sittings, hand-offs** (208-227): sitting = unit; typed hand-off payload;
  the two handoff timings; relay-when-done reflex named with mechanics pointed at
  vlt-dispatch; stable-path update-in-place; the third boundary — a durable doc that
  revises over time is a **spec** in `{specs}` (line 227).
- Backlog (229-231), How to write (233-241), Reading list (243-249).

### 2.2 Conventions — versions, consumers, enforcement frontmatter

| Convention | version | consumers (skills) | enforcement |
|---|---|---|---|
| `frontmatter.md` | 3 | vlt-ingest, vlt-extract, vlt-research, vlt-lint, vlt-mint (frontmatter.md:11-12) | `checked` by vlt-lint at lint run; + deferral fields (drift findings / 3rd new convention; review_after 2026-08-17) (frontmatter.md:13-18) |
| `wiki-index.md` | 2 | vlt-ingest, vlt-lint (wiki-index.md:11-12) | `checked` / vlt-lint / lint run |
| `wiki-supersession.md` | 1 | vlt-ingest, vlt-lint, vlt-extract, vlt-track (wiki-supersession.md:11-12) | `checked` / vlt-lint / lint run |
| `wiki-consolidation.md` | 1 | vlt-ingest (wiki-consolidation.md:12) | `declared` + full deferral (3 unresolved near-dups across 2 sweeps; review_after 2026-08-17) (wiki-consolidation.md:13-16) |
| `extraction.md` | 2 | vlt-extract, vlt-lint, vlt-track (extraction.md:12) | `checked` / vlt-lint / lint run |
| `write-verification.md` | 1 | vlt-ingest, vlt-extract, vlt-research, vlt-lint (write-verification.md:12) | `checked` / vlt-lint / lint run |
| `spec.md` | 1 | vlt-mint, vlt-dispatch (spec.md:12) | `declared` + full deferral (any spec bump shipping without relays → promote lint checks; review_after 2026-08-17) (spec.md:13-16) |

Every base convention opens with the identical **Overlay note** (pristine base;
additions go to `{overlays}/{name}.overlay.md`; e.g. frontmatter.md:23).

Content highlights per convention:

- **frontmatter@3**: YAML syntax rules 1-6 (quote wikilinks; no nesting; bare paths for
  audit-trail lists; backticked wikilinks don't resolve; no field/body duplication,
  lines 29-38). Base schema; immutable `created` vs `last_updated` (line 54).
  **Write attestation** fields `verified_by`/`verified_at` (build-16, lines 73-84):
  freshness rule `verified_at ≥ last_updated`; explicitly orthogonal to the `trust:`
  ladder (line 84). Wiki-page schema: `summary ≤160`, `category` = strict index-H2
  binding, `topic` list; `review_after` single definition — resolved date, absence =
  evergreen, three legal review outcomes (line 115); reference Bases views documented
  not shipped (line 117). Research/session/PARA/partner-memory/backlog schemas
  (119-214). **Enforcement declaration** (216-231, build-16 "the bell"): flat keys,
  stage semantics declared/checked/enforced, deferral = all-three-or-invalid, stage
  promotions only through the mint ceremony. Narrow-convention escape hatch (233-235).
- **wiki-index@2**: map-not-catalog (no descriptions/counts/dates, lines 24-32);
  emergent categories; strict bidirectional `category:`↔H2 binding (56-60); row format
  + structural tags + Stubs section; the writer/validator contract table binding
  vlt-ingest and vlt-lint to this one definition (92-99).
- **wiki-supersession@1**: `[!superseded]` inline callout (Was/Now/Source/Reason with
  the 4 reason values), page-level `superseded_by` frontmatter + warning callout,
  `[!stale]` markers (28-75).
- **wiki-consolidation@1**: no standalone consolidate op — lint detects, ingest
  executes (line 25); 3 detection heuristics; merge-direction rules (source count →
  slug stability → link incidence → recency, 59-66); archive-and-stamp never delete
  (110). ⚠ Its "Index update" section (114-119) still instructs updating the retained
  page's *Sources count / Updated date / description in the index* — contradicts
  wiki-index@2 (see §5.1).
- **extraction@2**: wiki-only provenance; the **personalized-extraction widening**
  (34-49): hard invariant (every method claim traces to a `sources:` wiki page) vs the
  one soft parameter (`personalization_sources:` — state never method); bounded opt-in
  per gated mint, "no skill shipped with the module uses it" (line 47); operational-log
  discipline (line 49). Trust ladder (extracted artifacts start `hybrid`/`reviewed`),
  stable-slug filenames, type↔folder map, re-extraction supersession (51-129).
- **write-verification@1** (build-16): the tier-1 checklist's single home (24-40);
  attestation contract incl. lint-attests-narrowly (44-47); **fail-open rule** (51);
  **scope rule** — self-marker not quality grade, human files out of jurisdiction (55);
  tier membership/promotion test (59-60); sample audit ≈1-in-5 with the honest threat
  model: attestation defends bypass, not deception; the sample audit mitigates the
  latter (64).
- **spec@1** (build-15): defines the spec class (durable, owned, versioned,
  cross-partner) against its four non-examples incl. BMad's SPEC kernel (27-34); home
  `{specs}` lazy-created, filename shape uses placeholder tokens (38); schema (40-49);
  **the two `consumers:` semantics** disambiguation — convention consumers = skills
  acking via depends_on; spec consumers = partners notified via relay (51-58);
  supersession: parameter change = in-place version bump + "What changed" changelog;
  structural rewrite = new file + `supersedes:` (60-63); **push-MUST + pull-SHOULD**
  notification, redundant by design (65-72); mint-time consumer lock (74-76);
  enforcement: `declared` with named deferred lint checks `spec_schema_violation` +
  `spec_notification_missing` and a pre-agreed escalation trigger (78-80).

### 2.3 Personas (5 files)

`architect` (structural coherence/long-term fit), `skeptic` (what breaks this),
`pragmatist` (smallest thing that works now), `historian` (precedent — we've been here
before), `moderator` (stance-less synthesis into the four-part verdict). Each carries
Core Lens / Instincts / **Blind Spots** (self-declared over-weighting, e.g.
architect.md:31-35) / Best Used When / an Activation Prompt section the workflow
applies verbatim (vlt-review-council.js:128).

### 2.4 Version-handshake bipartite verification (done by hand, both directions)

Forward (every listed consumer acks the current version):

- frontmatter@3 → vlt-ingest:4 ✓, vlt-extract:4 ✓, vlt-research:3 ✓, vlt-lint:4 ✓,
  vlt-mint:3 ✓ (all pin `frontmatter@3`)
- wiki-index@2 → vlt-ingest ✓, vlt-lint ✓ (both pin `wiki-index@2`)
- wiki-supersession@1 → vlt-ingest ✓, vlt-lint ✓, vlt-extract ✓, vlt-track:4 ✓
- wiki-consolidation@1 → vlt-ingest ✓
- extraction@2 → vlt-extract ✓, vlt-lint ✓, vlt-track ✓
- write-verification@1 → vlt-ingest ✓, vlt-extract ✓, vlt-research ✓, vlt-lint ✓
- spec@1 → vlt-mint ✓, vlt-dispatch:3 ✓

Reverse (every `depends_on` entry appears in that convention's `consumers:`): checked
for all 7 skills carrying `depends_on` (ingest, extract, research, lint, mint,
dispatch, track) — every ack maps to a listing. **The handshake is fully
bipartite-consistent. No stale, unacknowledged, or dangling entries.**

(Also consistent by design: vlt-lint is *not* yet in spec@1's `consumers:` — the spec
lint checks are deferred per spec.md:80; and vlt-query carries no acks — but see §5.7
for why that's a soft spot.)

---

## 3. The enforcement layer

### 3.1 `tools/package-lint.py` (build-14) — the release-boundary bell

250 lines; checks the **working tree on disk, never the git index** (own-the-apply is a
filesystem copy — docstring lines 8-10). Four groups:

- **A — on-disk cruft** (lines 58-71): `.decision-log.md`, `__pycache__/`, `*.pyc`,
  `.DS_Store` within `skills/vlt-*/**`, `.claude-plugin/**`, and repo root depth 1
  ("./.DS_Store has shipped before", line 68).
- **B — module-help.csv canon** (lines 109-148): header must equal
  merge-help-csv.py's `HEADER` — **imported by exec'ing the script, never duplicated**
  (lines 74-80, with `sys.dont_write_bytecode = True` at line 41 so the import doesn't
  create the cruft group A polices); every row exactly 13 fields; the **always-quote**
  rule verified against the *raw line* via a hand-rolled quote scanner
  (`field_quote_flags`, lines 83-106) for display-name/description/args/outputs.
- **C — resolvability + version agreement** (lines 151-198): module.yaml parses,
  `module_version` == marketplace `plugins[0].version`, governance bundle home
  non-empty, and marketplace `skills[]` ↔ `skills/vlt-*` dirs **both directions**
  (missing dir "breaks install"; unlisted dir "silently doesn't ship").
- **D — tag intent**: with `--expect-version X.Y.Z` both strings must equal it;
  without the flag it prints **SKIPPED (not PASS)** (lines 201-208, 227, 232) — the
  release process requires the flag (CLAUDE.md release rule).

`tools/test-package-lint.py` (194 lines) is a negative-test harness: synthetic fixture
tree, one seeded defect per case, asserts failure lands in the right group, and runs
the lint via `uv run` exactly as release time does (docstring lines 6-13).

### 3.2 Merge scripts (`skills/vlt-setup/scripts/`)

- **`merge-help-csv.py`** (384 lines). Canonical 13-col `HEADER` (lines 38-52) and the
  exact `LEGACY_HEADER` (after/before) it will migrate (line 58);
  `canonicalize_header` renames only the exact known-old form — "an unknown header is
  never blindly rewritten" (lines 61-69). **Merge-not-replace (B1)**: with
  `--live-skills-dir`, `filter_rows_preserving_local` (lines 188-230) keeps a row whose
  skill is absent from the bundle but whose dir exists live (local mint), drops shipped
  rows (re-appended fresh) and true zombies (no live dir). **Malformed-row tolerance
  (build-10/R2-3)**: a mis-split row is skipped and reported loudly instead of raising
  (lines 111-171, warning text at 294-301 — the pre-fix ValueError once let one bad
  row block an entire upgrade's registration step). JSON result includes
  `local_mints_preserved`, `malformed_rows_skipped`, `header_migrated` (367-379).
- **`merge-config.py`** (408 lines). Anti-zombie on the `vlt` section only
  (271-278); core keys written at root; **user-only keys (`user_name`,
  `communication_language`) stripped from config.yaml and routed exclusively to
  config.user.yaml** (254-269, 298-321); legacy `core:` section migrated to root
  (249-252); result templates `{value}` substitution with double-prefix guard
  (194-221); `--legacy-dir` migration+delete path exists but vlt-setup forbids it
  (vlt-setup SKILL.md:101).
- **`cleanup-legacy.py`** (259 lines). Ships "only for parity with the BMad template"
  and is never invoked (vlt-setup SKILL.md:271). Dead-by-policy code.

### 3.3 frontmatter@3 — the bell / attestation / freshness machinery (build-16)

Three interlocking pieces, each single-homed:

1. **The bell (enforcement declaration)** — frontmatter.md:216-231. Every convention
   declares in its own frontmatter how its boundary is enforced ("no boundary without a
   bell"): `enforcement_stage` (declared/checked/enforced), owner + moment, and — for
   `declared` — a complete tripwired deferral (`deferral_metric` + `deferral_threshold`
   + `review_after`, all three or invalid). Wired into: the mint boundary classifier
   (vlt-mint:42), the council's standing "WHERE'S THE BELL?" rubric line + moderator
   hard rule (vlt-review-council.js:134-135, 167), lint's enforcement doctrine
   meta-check (vlt-lint:75), and all three mint templates (capability-template.md:71-77,
   partner-agent-template.md:7-9, operation-skill-template.md:28-32). Stage promotions
   only via mint ceremony, never lint (frontmatter.md:231).
2. **Attestation** — fields in frontmatter.md:73-84; contract in
   write-verification.md. Write ops attest what they wrote; lint attests only what its
   auto-fix touched; absence on a file claiming vault provenance is the finding
   (`para_missing_attestation`).
3. **Freshness** — `verified_at ≥ last_updated` (frontmatter.md:83); stale = quiet
   re-run, not a violation; attested-and-fresh files skip lint tier-1 re-checks except
   the 1-in-5 sample audit (vlt-lint:57). One mechanism, two payoffs: re-scoping
   telemetry + bypass detector (write-verification.md:22). Five-consumer walk was the
   build-16 verification (all five ack `frontmatter@3` — confirmed in §2.4).

### 3.4 The spec convention (build-15)

See §2.2 spec@1. The load-bearing pieces: the third-boundary rule in the contract
(line 227) routes durable-and-revising docs out of `_agent/handoffs/`; relay's
doc-path idempotency assumes the stable path (vlt-dispatch:178); the push-MUST relay
per consumer on a version bump (spec.md:69, vlt-dispatch:154); the mint-time consumer
lock (spec.md:74-76, vlt-mint:108); vlt-upgrade's human-gated proto-spec retrofit
migration (vlt-upgrade:75). Enforcement is currently prose + inspection —
`enforcement_stage: declared` with the two lint checks explicitly deferred and
tripwired (spec.md:78-80).

### 3.5 Durability / merge-not-replace (build-18 + B1)

The full net, in layers:

- **Location**: everything vault-grown lives in the agent zone, never overwritten
  (contract:90): minted partner memory, overlays, capabilities, families, mint history,
  specs, the upgrade ledger.
- **Registration (B1)**: `merge-help-csv.py --live-skills-dir` preserves local-mint
  rows (§3.2); vlt-upgrade Step 3.1 requires it and verifies the JSON.
- **Bodies (B2)**: minted skill dirs restored from the pre-flight snapshot if a
  destructive apply removed them (vlt-upgrade:63).
- **Conventions**: pristine base + append-only overlay = "the collision never forms"
  (contract:96); `.baseline/` gives the divergence detector (lint's
  `convention_base_divergence` + upgrade pre-flight); overlay-lift migration puts an
  already-diverged vault on the durable path (vlt-upgrade:74); **overlay-subsumption**
  (build-18) closes the round trip by retiring upstreamed overlays, human-gated
  (vlt-upgrade:66).
- **Skill assets** (build-18): the `.skill-manifest` SHA net (vlt-setup:149) turns a
  local hand-edit of a shipped skill file into a surfaced divergence with contents
  preserved in the ledger, instead of a silent clobber (vlt-upgrade:36, 45). Skills
  have no overlay mechanism, so a local skill edit is "the user's to re-apply"
  (vlt-upgrade:45).
- **Overlay-aware reads** (build-18): every convention-reading skill reads base +
  overlay together (vlt-ingest:26, vlt-lint:17, vlt-extract:21, vlt-research:83,
  vlt-track:42).

---

## 4. Cross-cutting patterns

- **Single-home + pointers.** Pervasive and explicit: frontmatter schema only in
  frontmatter.md (contract:151 "deliberately does not restate"); the tier-1 checklist
  only in write-verification.md (vlt-ingest:153 "read it, don't re-derive it from
  memory"); the panel composition only in `KIND_PANEL`
  (vlt-review-council.js:50-53 "the SINGLE SOURCE OF TRUTH"); the relay reflex owned by
  vlt-dispatch, the pickup loop owned by vlt-dispatch (vlt-dispatch:152, 221); the
  handoff stable-path lifecycle owned by the contract (vlt-dispatch:178); the
  structure-map defaults owned by module.yaml (module.yaml:41-43); package-lint
  *imports* HEADER rather than copying it (package-lint.py:74-80); `review_after` has
  one definition, "referenced not redefined" (frontmatter.md:115, 228).
- **Derive-first.** Weight/home/council-class derive from the one declared
  `write_scope` (contract:193, capability-template.md:3); routing slugs derive
  mechanically from skill basenames (vlt-dispatch:87); the dispatch domain map derives
  from the live roster, not a hardcoded list (vlt-dispatch:85); anything derivable from
  frontmatter is banned from the index (wiki-index.md:30); Bases derives counts/dates
  live.
- **Capability objects/families.** One first-class object, two weights
  (contract:191-202); light = own-zone file, self-growable, council-none, one
  decision-log line; heavy = registered op skill owned by the lane's rightful partner.
  Families (Model B) = thin invariant contracts at `{capabilities}/families/`, opt-in;
  invariant change is gated and fires the same propagation discipline as a convention
  edit — "durability and coherence, the same seam" (contract:202, vlt-mint:119,
  vlt-upgrade:68). vlt-track + the Loop profile is the flagship worn-not-minted example
  (capability-template.md:55-67).
- **Own-the-apply.** vlt-upgrade's preferred path merge-copies from module source
  directly (never the installer): refresh shipped `vlt-*` + `_meta/` + workflows only;
  never delete unshipped dirs, never write `_agent/`, never touch overlays; excludes
  dev cruft at the copy seam (vlt-upgrade:16, 45-46). Because it's a *filesystem* copy
  of the working tree, package-lint deliberately lints the disk, not the index
  (package-lint.py:8-10), and the repo rule bans `.decision-log.md` in the working tree
  (project CLAUDE.md).
- **Other recurring disciplines**: scoped-by-default with explicit full escalation
  (lint, dispatch, ingest's heavy-source split — each names the same
  "only earns its overhead at scale" rationale, vlt-ingest:52, vlt-lint:45);
  fail-open verification (write-verification.md:51); capture-cheap/act-deliberate
  (contract:231); read-only finders + one serial writer (vlt-lint-full meta:4,
  vlt-ingest:59); args parse-on-intake in both workflows (vlt-review-council.js:32-37,
  vlt-lint-full.js:39-44); live-path passing everywhere subagents read files (the
  plugin-cache fix — vlt-mint:93-94, vlt-lint:41, vlt-review-council.js:22-27);
  placeholder paths in shipped worked examples (vlt-dispatch:195, spec.md:38).

### 4.1 The two dynamic workflows

- **`vlt-review-council.js`** (183 lines): parse args (string-delivered);
  guard on `{mode, subject, personasPath}`; `KIND_PANEL` map with none-kinds returning
  an immediate `pass` (lines 79-83) and back-compat aliases for pre-build-7 callers
  (lines 62-64); lens cap of 4 (line 90); parallel independent lenses each forced into
  the `VERDICT` schema, reading their persona's Activation Prompt verbatim from the
  live path, with the mint-mode "WHERE'S THE BELL?" rubric (134-135); graceful
  degradation when personas are unreadable (`available: false`; all-unavailable →
  degraded `revise` verdict, 145-155); stance-less moderator synthesizes into the
  `SYNTHESIS` schema with the hard no-bell-no-pass rule (167).
- **`vlt-lint-full.js`** (281 lines): read-only fan-out finder. Model tiering —
  scanners default `haiku` (the ~10x cost win), index/cluster passes `sonnet`
  (56-58); chunked fan-out (16/chunk) with a budget floor guard recording a coverage
  cap (126-137); pure-JS graph reduce for orphans/missing-targets with the
  cross-layer-slug allowance (146-152); near-duplicate detection requires shared-link
  signal AND a structural secondary (slug stem or title Jaccard ≥ 0.5), hub links
  excluded — annotated with the live-wiki false-positive history (70 false pairs,
  154-192); cluster cap scales with page count (fixed 12 falsely tripped on the live
  wiki, 51-53); index pass validates the strict category↔H2 binding (195-199); bounded
  contradiction-cluster pass separating handled vs unhandled disagreements (Gap B,
  226-237); returns the vlt-lint Step-5 report shape with `files_checked` vs
  `files_listed` and `coverage_caps` (243-281). `para_missing_attestation` is emitted
  empty as a structural slot the SKILL fills (262-263).

---

## 5. Weak points visible from source

1. **wiki-consolidation.md contradicts wiki-index@2 (real doc bug).** Its "Index
   update" section instructs: "Update the retained page's `Sources` count (new union
   size) and `Updated` date / Adjust the retained page's description"
   (wiki-consolidation.md:116-118). wiki-index@2's whole point is that the index
   carries **no** descriptions, counts, or dates (wiki-index.md:28-31, 64), and
   vlt-ingest Step 7 + vlt-lint enforce that. The section predates the wiki-index v2
   change and was never reconciled — notably the handshake could not catch it: the
   coherence check walks *consumer skills'* `depends_on`, not cross-convention text,
   and wiki-consolidation's own version never bumped. A convention-to-convention drift
   class the machinery doesn't cover.
2. **Contract structure-map table has drifted behind module.yaml (missing `specs`).**
   module.yaml's canonical map includes `specs: _agent/specs/` (module.yaml:49) and
   vlt-upgrade/vlt-dispatch/vlt-mint resolve `{specs}` through the map
   (vlt-upgrade:25, vlt-mint:24), but the operating contract's table
   (contract:29-44) lists 14 entries and omits `specs` — despite the contract itself
   defining the spec boundary at line 227. This is exactly the repo's own
   "lists that claim completeness drift" failure mode, in the constitution itself.
3. **Contract Reading list is stale.** contract:243-249 lists five conventions and
   omits `write-verification.md` and `spec.md` (both created 2026-07-06, builds 15/16).
   Same drift class as (2).
4. **module-help.csv vlt-mint row is stale vs build-7.** Its `args` column reads
   `{kind: operation | partner | self-edit | retire}` and the description says "mint a
   new operation skill…" (module-help.csv:12) — the pre-build-7 kind vocabulary;
   the live kinds are `add a capability` / migrate / retire / family ops / etc.
   (vlt-mint:34-40). Functional (help text only) but the registry row is the module's
   advertised interface. The dispatch and track rows, by contrast, were updated to
   their current framing.
5. **Dead / unexercised machinery.**
   - `cleanup-legacy.py` (259 lines) ships and is never invoked by policy
     (vlt-setup:271) — carried "for parity with the BMad template". Also
     `merge-config.py`'s `--legacy-dir` path is likewise forbidden in vlt-setup usage.
   - Family machinery (family contracts, `change family invariants` gate, lint's
     family checks, upgrade's `family_invariant_drift`) is fully built with no shipped
     family contract to exercise it — `{capabilities}/families/` ships empty
     (vlt-setup:238 creates the empty dir).
   - `enforcement_counter` awaits an "enforcement kit" metric vocabulary that doesn't
     exist yet (frontmatter.md:224).
   - The KIND_PANEL back-compat aliases (`operation skill`, `capability migration`,
     vlt-review-council.js:63-64) exist for "mid-upgrade vlt-mint" callers — both map
     to `[]` (no panel) so they're harmless, but they're a small permanent shadow
     vocabulary.
   - Personalized extraction: "no skill shipped with the module uses it"
     (extraction.md:47) — vlt-track is shipped and implements the discipline but only
     fires when a vault-minted vertical partner wears it; until then the whole
     firewall (lint's `personalized_extraction_issues`, track's verify gate) is
     unexercised at rest.
6. **Discipline substituting for enforcement (prose-only mechanics).**
   - The **skill-asset manifest** is written and verified by LLM-followed prose in
     vlt-setup/vlt-upgrade — there is no script computing/checking SHA-256s
     (vlt-setup:149 says "write a SHA-256 manifest"; vlt-upgrade:36 "recompute its
     SHA"). The one durability net that is hash-exact in spec is hand-executed in
     practice; a transcription slip silently weakens it.
   - **vlt-upgrade generally has no scripted step except the CSV merge** — snapshot,
     merge-copy with exclusions, baseline refresh, subsumption diff, ledger append are
     all prose procedure. The design compensates (detect-and-report, ledger,
     idempotent migrations) but correctness rides on each run's execution fidelity.
   - **spec@1 is `declared`** — its two lint checks are deferred (tripwired, but until
     the tripwire fires, notification/schema discipline is inspection-only,
     spec.md:78-80). Same for wiki-consolidation@1 (`declared`).
   - The **version handshake itself is prose + lint-flag**: nothing blocks a release
     with a stale ack; package-lint does not check the handshake (it checks packaging
     only). The edit-time exit gate lives in vlt-mint's prose (vlt-mint:141) and the
     lint-time net requires someone to run lint in a vault — the *factory* repo has no
     handshake check in `tools/`.
7. **vlt-query is outside the attestation/handshake perimeter.** It can write
   `{research}` notes (vlt-query:44-46) but: it is not in `write-verification.md`
   `consumers:` (write-verification.md:12), is not a legal `verified_by` value
   (frontmatter.md:78-82), runs no verify/attest step, and carries no `depends_on`
   despite writing frontmatter per `frontmatter.md` (vlt-query:46). A query-filed note
   is therefore born unattested — lint will surface it as `unattested_write`
   (informational-or-flag depending on `created`), which is arguably working as
   designed but means one shipped write path is permanently un-attestable. Either an
   intentional narrow perimeter (query filing is rare) or a gap; the source doesn't
   say which.
8. **Complexity hot-spots.**
   - `vlt-setup` (287 lines) is the densest prose surface: three config files, two
     overwrite regimes, five provisioning steps, installer-interop caveats, cache
     seeding, and two shell-trap warnings. It is also on the critical path of every
     upgrade (Step-6 hand-off). Highest execution-fidelity risk per run.
   - `vlt-dispatch` (260 lines) carries three modes, two idempotency schemes, two
     writer roles, and the pickup-loop protocol in one skill — well-factored but the
     watermark scheme (line-count offsets against human-editable files,
     vlt-dispatch:73, 81) is inherently fragile; the skill acknowledges the
     stale-offset case and punts to "offer a full re-dispatch".
   - `vlt-mint` (167 lines) + capability-template (97) + KIND_PANEL: the kind
     vocabulary now spans three surfaces (mint prose, workflow map, help-CSV row) and
     the help row already drifted (see 4).
9. **Minor inconsistencies.**
   - README:194-195 tells users "**Updating:** re-run the installer … re-running
     `vlt-setup` refreshes registration" without mentioning `vlt-upgrade` — the
     destructive-installer path the durability arc exists to bracket. The README
     *does* describe vlt-upgrade at 141-145; the Install section wasn't reconciled.
   - README:215-217 ("A vault ≠ this repo … you register its path during
     `/vlt-setup`") contradicts the module's own no-registry stance (README:171-172
     "There is no external registry"; module.yaml:36 "there is no vault registry").
     Stale pre-rework text.
   - README:38 uses 📖 for the Librarian; customize.toml/module.yaml use 📚
     (module.yaml:22). Cosmetic.
   - The heavy-capability template hand-sets `council_class: gated`
     (capability-template.md:47) with a comment "(unless owned by the lane's rightful
     owner & additive)" while the light template insists the field is "DERIVED …
     never hand-set" (line 22) — the heavy case genuinely needs judgment, so the
     "derive, never hand-set" claim is only true for the light weight; the template
     doesn't say so crisply.
   - contract:121 lists the log type set as `session | ingest | query | lint |
     research | extract` (non-exhaustive, fine), but `dispatch` (vlt-dispatch:232)
     and `track` (vlt-track:109) are shipped types named only at their owning ops —
     consistent with the stated rule ("name the op that owns one where it's defined")
     but a reader of the contract alone under-counts the shipped vocabulary.
10. **The `13 cols` positional dependency.** package-lint group B and
    merge-help-csv's malformed-row detection both key off exact column counts and the
    `skill` column sitting at index 1 (merge-help-csv.py:164-167 relies on `skill`
    preceding every comma-prone field). Any future BMad header change re-runs the
    build-13 migration problem; `canonicalize_header` only knows the one legacy form.

---

## 6. Quick reference — who writes what in a vault

| Lane / artifact | Sole writer | Others |
|---|---|---|
| Canonical wiki pages + index | `vlt-ingest` (fronted by Librarian) | propose/hand off only |
| PARA (`projects/`, `areas/`, `resources/`) | `vlt-extract` (Creative) / `vlt-track` protocol write (personalized extraction, opt-in) | read only |
| `{research}` notes | `vlt-research`, `vlt-ingest` (source snapshots), `vlt-query` (file-back) | — |
| `_agent/dispatch.md` blocks | `vlt-dispatch` (Librarian's op; relay = scribe for publishers) | each partner flips only its own line statuses |
| `_agent/handoffs/`, `{specs}` | the publishing/authoring partner | dispatch points, never authors |
| `{log}` | every op appends its own tagged line | append-only |
| Session notes | the summoning partner, one per sitting | ops never |
| `{partners}/<p>/identity.md`+`thread.md` | that partner only | never pushed into by others |
| `{partners}/<p>/capabilities/`, `{capabilities}/families/` | vlt-mint / partner self-grow | lint guards |
| `_meta/` (conventions/personas/contract) | module (refresh on upgrade); base edits only via gated mint + handshake | overlays in `{overlays}` are the vault's |
| `daily/`, `new/`, `_vault/`, `sources/` (existing files), MOCs | human only | read-on-request; new-file `sources/` deposits permitted |
| `.claude/`, `_bmad/` | installer / vlt-setup / vlt-mint (deliberate) | ignored as knowledge |
