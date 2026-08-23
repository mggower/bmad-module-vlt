---
title: 'Build #B9-3 — the remote feedback rail (GitHub issues become the module''s reachable
  front door — the ingress two of this arc''s own filings had to route around)'
status: 'BUILT 2026-08-21 — all nine F-sites landed in one commit on arc9-v0.12.0.
  Verified at rest: package-lint A/B/C/E PASS, D SKIPPED (mid-arc; C5 sees vlt-feedback
  in skills[], C7 names field-contract.md, E3 clean); test-package-lint 21/21 green;
  contract-agreement fixture run (check (i)) PASS — field-contract payload ids == both
  forms'' id: sets == composed artifact section headers, 8 ids mechanically compared;
  gh degradation probe (check (ii)) PASS — stripped-PATH lookup exit 1 fires the named
  gh-missing branch, paste-ready artifact written with labels + origin-vault pre-written;
  scrub grep clean; no .decision-log.md. Owner action still owed pre-tag: run the
  gh label create sequence recorded in .github/ISSUE_TEMPLATE/config.yml (seven labels).
  Deviations: (1) F5''s pointer bullet names the contract home in prose ("the
  vlt-feedback skill''s field-contract reference"), not as the literal
  references/field-contract.md token — package-lint C7 resolves any such token relative
  to the naming skill and flagged it as a dangling route in vlt-setup. (2) The brief left
  the gh-label-create sequence''s recording site unnamed within F1; it is sited as the
  comment block atop .github/ISSUE_TEMPLATE/config.yml. (3) The defect form carries kind
  as a single-option dropdown (options: [defect]) so both forms'' id: sets are identical
  — the brief required the id-set identity but did not spell out how the defect form
  carries kind. (4) The gh-unauthenticated branch was verified by protocol-text review
  only, per the brief''s explicit allowance (no cheap simulation of a failing gh auth
  status).'
module_code: 'vlt'
created: '2026-08-21'
derives_from:
  - 'inbox/2026-08-19-130120-feedback-loop-is-single-machine-github-issues-as-remote-rail.md
    (A9-4 — the whole filing: repo-side contract, vlt-feedback skill, transport URL; build A
    of D4''s two-build split. Evidence debts E1–E3 attach here field-contingent; E4 released
    as a watch.)'
roadmap: 'skills/reports/inbox-evolution-arc9-roadmap.md'
rulings: 'roadmap §Ideation rulings (2026-08-20), B9-3 bullet — binds: D4 (build A: rail then
  intake, the four parts designed as ONE field contract), D6 via roundtable A3 (the build runs
  D6''s test on itself and records the result), E1–E3 (attached field-contingent, discharging
  events named per A20/R5), roundtable A13 (transport URL as a merge-config defined variable),
  A14 (registration surfaces + two ship-verifiable checks), A15 (paste-ready failure artifact;
  contract version stamp; the field contract''s single home moves into the shipped half —
  this brief owns the whole siting, B9-5 cites it), R1, R2. Plus A16 (.github/ extends the
  release-commit surface) and A20/R5 (E1/E3 name their discharging event, ledger partitions
  by release).'
risk: 'low-moderate — no convention version bump, no consumer walk, no governance-bundle edit
  (no C6), no new package-lint check (no E4), no workflow asset (no E5); but it is the arc''s
  most consequential build in the field: a NEW shipped skill (two registration surfaces, R2),
  a greenfield .github/ tree extending the release-commit surface (A16), and an irreversible
  widening of where vault-adjacent text can land (a public tracker) — gated in-build per D6.'
---

# Build #B9-3 — the feedback rail

The module's only feedback ingress is a filesystem write into `inbox/` — reachable solely from
vlt-core, the one vault co-resident with this repo. Two of Arc 9's six filings originated on
machines with no route into it; one reached the factory only because an agent bypassed the
module and opened `mggower/bmad-module-vlt#1` with no shape governance, no labels, no origin
vault. This build stands up the rail: **one field contract in four parts, designed together**
(D4 build A) — `.github/ISSUE_TEMPLATE/` forms + the label set, a new shipped skill
`skills/vlt-feedback/`, and the transport URL declared as a `module.yaml` defined variable.
The factory-side intake is **B9-5** (build B, ordered after this one — no labels exist to
query until this lands). Issues are transport; **`inbox/` stays SSoT**; capture is the
airlock.

All rejected alternatives in the parent filing are settled — do not re-litigate. In
particular: the skill's name is `vlt-feedback` (owner-ruled, distinct from vlt-core's local
`vlt-file-feedback` mint — no upgrade collision); vlt-core's posture is one rail (the local
mint is retired by explicit owner act post-ship, **not** by this build); and issues sit
*beside* the repo because `inbox/` is gitignored — there is no git-native remote route into
it, structurally, not merely conveniently.

## Brief-time dispositions

1. **D6's test on the rail — the REAL MECHANISM ships, in this build.** *(Binds: roundtable
   A3/Victor; D6 as amended by A1/A2.)* `vlt-feedback` widens what may be written — from a
   gitignored local directory that reaches nobody to a public tracker that reaches everybody,
   irreversibly — and the roadmap offered two exits: a mandatory rendered-payload preview the
   filer approves before `gh issue create` (the approval-gate shape `vlt-groom` already
   ships), or a stated owner-machines-only interim posture. **Ruled: the approval gate
   ships.** Grounding found no reason it can't: the gate is protocol text inside the skill
   itself, the exact shape already shipped and field-tested at `skills/vlt-groom/SKILL.md:29`
   (render the gated proposal, halt, apply on approval) and `:36` ("**Nothing applies without
   the gate.** The proposal halts for the user's ruling") — no external mechanism, no new
   walker, no cost beyond the skill's own text. The scrub gate is thereby a **mechanism**
   (a mandatory halt showing the exact bytes that would go public), not a prose checklist;
   what remains untested is its **efficacy** against real personal-domain signal, which is E2,
   field-contingent by nature, and stays so. D6's result, recorded per A3: **a named bell
   ships in the same build as the widening — the mandatory preview-approval gate in F2. No
   interim posture is needed** (see §Verification R1 line for the one residual sliver: labels
   are a repo-side owner action, bound below).

2. **The config key is `vlt.feedback_repo`; the default is the `OWNER/REPO` slug.** *(Binds:
   A13.)* `module.yaml` declares `feedback_repo:` as a **defined variable** — a top-level dict
   carrying `default:` — because that is the only shape `merge-config.py` exports:
   `_VARIABLE_MARKER_KEYS = ("prompt", "default", "result", "user_setting")` at
   `skills/vlt-setup/scripts/merge-config.py:207`, declaration-read by `defined_variables()`
   (`:210-216`); a flat scalar is neither metadata (`_METADATA_KEYS`, `:201`) nor a variable
   and is removed as a zombie. A defined variable absent from answers and from the existing
   section is written from its `default:` (`:333-336`, "Defaults ship final"). **The key
   `vlt-feedback` reads is `feedback_repo` in the `vlt:` section of
   `{project-root}/_bmad/config.yaml`** — the same section every runtime skill already loads
   (e.g. `skills/vlt-groom/SKILL.md:17`). Default value: **`mggower/bmad-module-vlt`** — the
   `OWNER/REPO` slug `gh` takes via `--repo` (public module metadata, fine to ship; the full
   URL already ships in `marketplace.json:8-9`). **No `prompt:`** — setup materializes the
   default silently, exactly like `vault_structure`'s no-per-path-prompt posture; a vault
   overrides by editing `config.yaml` or at reconfigure. **Existing vaults gain the key on
   upgrade** (grounding addition): `vlt-upgrade` Step 3.6 hands off to `vlt-setup`
   (reconfigure) (`skills/vlt-upgrade/SKILL.md:84`), whose merge runs `merge-config.py`
   (`skills/vlt-setup/SKILL.md:88-98`) — the defaulted path writes the new variable and
   reports it under `module_keys_defaulted`. Fallback when the key is absent (unupgraded
   config): `vlt-feedback` reads the SSoT default from the installed
   `.claude/skills/vlt-setup/assets/module.yaml` (`feedback_repo.default`) and says the
   config is stale — never a second hard-coded URL in the skill (single-home).

3. **The label set — defined once, here, for the whole contract.** *(Binds: D4; A15 items
   (a)–(c) are B9-5's mechanisms but consume labels this contract must define.)* Seven
   labels:
   - `field:defect`, `field:pattern`, `field:candidate` — classification, template-selected
     (the filing's set, carried verbatim);
   - `vault-filed` — applied automatically by the issue forms' `labels:` frontmatter. Per
     A15(a) it marks **candidacy, not admission**;
   - `vault-accepted` — the **owner-applied triage label** A15(a) makes B9-5's
     materialization trigger;
   - `captured` — the capture-state label A15(c), applied at materialization;
   - `declined` — the terminal disposition A15(b) (issue closed with a reason, nothing
     written to `inbox/`).
   B9-3 defines and creates them; **B9-5 owns the state-transition mechanics** and cites this
   contract. GitHub labels are repo state, not files — creation is an owner-run, scripted
   `gh label create` sequence recorded in F1 (build-time owner action, bound before the
   v0.12.0 tag).

4. **The field contract's version stamp is `rail_contract: 1`.** *(Binds: A15/Victor.)*
   `vlt-feedback` writes `rail_contract` and `module_version` (read from `config.yaml`'s
   `vlt.version` metadata, refreshed on every merge) into every issue body. The templates are
   **additive-only** (stated in the contract home and in each template's own comment); B9-5's
   intake reads the stamp and flags a stale-shape filing instead of parsing it hopefully. The
   constant's single home is the field-contract reference (F3); templates and README carry
   pointers, never a copy.

5. **The failure artifact lands at `_agent/feedback-outbox/YYYY-MM-DD-HHmmss-<slug>.md`.**
   *(Binds: A15/Sally+Sophia; amended E3.)* On **any** transport failure (missing `gh`,
   unauthed `gh`, network, non-zero exit), `vlt-feedback` writes the fully-composed filing —
   title, body with all payload fields, **label names and origin-vault field pre-written,
   paste-ready** — and prints the file path plus the manual route (open an issue at the
   transport repo, paste body, apply the named labels). The path is a fixed agent-zone
   location, **not** a `vault_structure` entry: adding a logical name would edit the
   module.yaml default map *and* the contract's hand-transcribed table (package-lint E2 checks
   their agreement) for a directory that exists only on failure; precedent for fixed `_agent/`
   paths outside the map is `_agent/dispatch.md` (`skills/vlt-dispatch/SKILL.md:11`, not in
   the map). R4 disposition in §Verification.

6. **The single home is `skills/vlt-feedback/references/field-contract.md`.** *(Binds:
   A15/Paige, sited here per the B9-5 section's explicit instruction — "the siting decision
   moves to B9-3's brief… one build owns the whole field contract.")* The contract — payload
   field set, the `origin:` header shape for materialized filings (`origin: <repo>#<n>`),
   the label set + who applies each, `rail_contract` + the additive-only evolution rule —
   lives in one shipped reference that **rides the skill-asset manifest automatically**
   (`verify-skill-manifest.py:72-87` walks every source `vlt-*` dir; no manual manifest
   entry exists to add). `inbox/README.md` and the issue templates become **pointers**.
   Package-lint C7 (router integrity) requires the SKILL.md to name the reference — F2 does.

7. **Blank (non-template) issues stay enabled.** The tracker is public and E4 (community
   traffic) is a released watch, not a build item. Label partitioning already does the work:
   an issue without `vault-filed` is invisible to B9-5's Discovery by construction. Disabling
   blank issues would buy nothing and cost ordinary open-source hygiene.

**Interim posture (R1):** substantially **not needed — the widening and its gate ship in the
same build** (disposition 1). One residual sliver is bound rather than left as prose: the
label set exists on the repo only after the owner runs F1's `gh label create` step, so filing
before that lands as an unlabeled issue (exactly issue #1's shape). Bound: **the label-create
step runs before the v0.12.0 tag** (it is a Verification item and a ship-verifiable
acceptance element, checkable at rest via `gh label list`). No owner-machines-only posture is
declared.

## F-sites

### F1 — `.github/ISSUE_TEMPLATE/` (NEW, greenfield): the repo-side half of the contract

**Current state:** `.github/` does not exist in the repo (verified 2026-08-21; `.gitignore`
carries no `.github` exclusion, so it will be tracked). Issue #1 was filed with no template
and carries no labels — the confirmed-by-exercise gap.

**The change — three files plus one owner action:**

- `.github/ISSUE_TEMPLATE/field-defect.yml` — GitHub issue form, `labels: ["vault-filed",
  "field:defect"]`.
- `.github/ISSUE_TEMPLATE/field-pattern-candidate.yml` — one form for the two non-defect
  kinds, `labels: ["vault-filed"]` plus a required dropdown that instructs selecting
  `field:pattern` vs `field:candidate` (forms cannot branch labels; the kind field in the
  body is authoritative, the label is applied by the filer or at owner triage — state this
  in the form's own description).
- `.github/ISSUE_TEMPLATE/config.yml` — `blank_issues_enabled: true` (disposition 7) and a
  contact link pointing at the field-contract home in the repo
  (`skills/vlt-feedback/references/field-contract.md` on GitHub) — the template **points at
  the shape's SSoT, never restates it** (the filing's own rule).
- **Field set (must agree with the `vlt-feedback` payload — ship-verifiable check (i)):**
  what happened; generalized evidence (placeholder paths, no vault-local literals);
  provenance guess (marked as a guess); classification/kind; **origin vault**; where
  acceptance should run; `module_version`; `rail_contract`. Each form field's `id:` matches
  the payload field name in F3 — that identity is what the fixture check greps.
- Every form carries a comment: **additive-only** — fields may be added, never renamed or
  removed, without bumping `rail_contract` (disposition 4).
- **Owner action (build-time, pre-tag):** create the seven labels of disposition 3 via a
  recorded `gh label create` sequence (idempotent: `--force` or pre-checked). Not a commit;
  bound per R1 above.

**Why:** D4 build A's repo-side half; A15's label semantics; the intake half (B9-5) has
nothing to query until these exist. **Sizing note carried from D4:** this half is **not
shipped surface** — outside `skills/`, the own-the-apply copy surface, and every handshake;
it reaches vaults only as the remote endpoint. It is briefed anyway because it is half of one
field contract.

### F2 — `skills/vlt-feedback/SKILL.md` (NEW): the shipped half — judgment core, gates, transport

**Current state:** no `vlt-feedback` (or `vlt-file-feedback`) exists under `skills/`
(verified — 16 `vlt-*` dirs, none feedback-shaped). The judgment core exists only as
vlt-core's local mint, which is **vault-local source and must not be copied** — the skill is
written fresh from the filing's description (scrub rule: no vault-local content lands in
shipped surface).

**The change — one SKILL.md carrying:**

- **Frontmatter:** `name: vlt-feedback`, `depends_on: []` (it consumes no handshaked
  convention — package-lint E1 vacuously clean; write no `name@version` token anywhere in the
  body, E3 stray-pin scans this file), description covering triggers ("file this upstream",
  "send feedback to the module", a partner proposing a filing).
- **On Activation:** load config from `{project-root}/_bmad/config.yaml` (root + `vlt`
  section) per the standard block (`skills/vlt-groom/SKILL.md:17` shape); resolve
  `feedback_repo` per disposition 2 (config key → module.yaml default fallback, loudly).
- **The judgment core** (ported by description from the filing, `inbox/…130120…md:46-53`):
  module-source routing test with hand-off-when-unsure; **never auto-file** (a partner may
  propose; only the user's explicit go executes — the `vlt-groom` invoked-only posture);
  honest classification (defect / pattern / candidate); duplicate guard via
  `gh issue list --repo <feedback_repo> --label vault-filed --search` before composing.
- **The scrub gate + approval gate (D6's bell, disposition 1):** compose the full payload;
  run the scrub checklist (no vault paths, no personal-domain content, no third-party names;
  two-tier escape hatch — a vault-side companion detail note, referenced not pasted); then
  **render the exact issue title + body + labels and HALT for the filer's approval. Nothing
  posts without the gate.** Declined material is not posted and not retained outside the
  session.
- **Transport:** `gh issue create --repo <feedback_repo> --title … --body … --label …` with
  the labels from F3. Before any transport: detect missing `gh` (not on PATH) and unauthed
  `gh` (`gh auth status` non-zero) and **report each by name** — `gh-missing` /
  `gh-unauthenticated` — never an obscure failure (ship-verifiable check (ii)).
- **Failure artifact:** on any transport failure, write the paste-ready filing per
  disposition 5 and print its path + the manual route.
- **Stamps:** every body carries `origin vault`, `module_version` (from `vlt.version`),
  `rail_contract` (from F3).
- **Routing:** names `references/field-contract.md` (satisfies package-lint C7 — an orphan
  reference fails the gate).

**Why:** D4 build A's shipped half; A14's two ship-verifiable checks live here; amended E3's
recovery path lives here; D6's mechanism lives here.

### F3 — `skills/vlt-feedback/references/field-contract.md` (NEW): the contract's single home

**Current state:** the shape has no home anywhere — `inbox/README.md` specifies only the
filename convention (`YYYY-MM-DD-HHmmss-slug.md`) and **no header/frontmatter shape at all**
(verified against current `inbox/README.md`); capture's candidate siting there was overruled
by roundtable A15/Paige (gitignored — invisible to every shipped producer and every public
contributor).

**The change — one reference file stating, once:**

- the **payload field set** (the F1 list, field ids normative — the issue forms and the
  composed body both derive from this list);
- the **`origin:` header shape** for factory-materialized filings: `origin: <repo>#<n>`
  (e.g. `origin: mggower/bmad-module-vlt#1`) — machine-written by B9-5's intake, the
  idempotency key for A15(d)'s Discovery exclusion;
- the **label set** and who applies each (disposition 3), with the state flow
  `vault-filed → vault-accepted → captured` / `→ declined` noted as **B9-5's mechanics,
  defined here so both builds read one contract**;
- **`rail_contract: 1`** and the additive-only evolution rule: renaming/removing a field or
  changing a field's meaning bumps `rail_contract`; adding a field does not; B9-5's intake
  compares the stamp and flags stale-shape filings.

**Why:** A15/Paige — a three-site field contract whose single home is invisible to two of the
three is joint 2's fault reappearing in the ingress build; this file ships into vaults and
rides the skill-asset manifest (`verify-skill-manifest.py:72-87`, automatic — no registration
surface exists for it and none is owed).

### F4 — `skills/vlt-setup/assets/module.yaml:35-39` + end: the transport URL as a defined variable

**Current state:** the configuration-variables block opens at `:35` with the comment "The
only variable is an optional layout override" (`:37`), and `vault_structure:` (`:39`) is the
sole defined variable. Nothing feedback-shaped exists (roadmap cited `:36-62`; trivially
shifted, HOLDS).

**The change:** append after the `vault_structure` block:

```yaml
feedback_repo:
  # Transport endpoint for vlt-feedback (OWNER/REPO slug for `gh --repo`). A defined
  # variable (dict with default:) — merge-config.py exports ONLY defined variables into
  # config.yaml's vlt: section; a flat scalar here would be silently dropped (roundtable
  # A13). Public module metadata; override per-vault in config.yaml if filing elsewhere.
  default: mggower/bmad-module-vlt
```

and amend the `:37` comment ("The only variable is…" → the layout override **and the
feedback transport**). No `prompt:` (disposition 2).

**Why:** A13 — the ideated flat `feedback_repo: <url>` scalar would be dropped by
`merge-config.py` (`:207` marker keys; zombie removal `:339-346`) and `vlt-feedback` would
fire in a vault with no transport.

### F5 — `skills/vlt-setup/SKILL.md:52-54`: document the second module variable

**Current state:** `:52` — "The only module variable is optional:" followed by the
`vault_structure` bullet (`:54`).

**The change:** reword `:52` to admit two variables and add a short `feedback_repo` bullet:
not prompted; materialized into `config.yaml`'s `vlt:` section from the `module.yaml`
default; what it is (vlt-feedback's transport endpoint); override by editing `config.yaml`
or at reconfigure. One bullet, pointer-grade — the contract itself lives in F3.

**Why:** without this, setup's own collect-configuration text contradicts the module.yaml it
reads (`:30`), and the one document an installer session follows never mentions the key it
just wrote.

### F6 — `skills/vlt-setup/assets/module-help.csv`: the FB row

**Current state:** 16 rows after the canonical 13-col header (`module,skill,display-name,
menu-code,description,action,args,phase,preceded-by,followed-by,required,output-location,
outputs` — matches `merge-help-csv.py:38` HEADER). No feedback row. Menu-code `FB` is
unclaimed (in use: SU LB RS CR IN RE QY EX LN GM DC DP MN RC UP TK).

**The change:** append one row, **all four free-text fields double-quoted**
(`package-lint.py:94` FREE_TEXT_FIELDS; always-quote rule, `check_group_b` `:154-195`):

```
Vault,vlt-feedback,"File Module Feedback",FB,"File a field note upstream to the module's public tracker: classify honestly (defect / pattern / candidate), scrub (no vault paths, no personal-domain content), preview the exact public payload for your approval, then post via gh with origin-vault and contract-version stamps. Degrades loudly: no gh or no auth → a named error plus a paste-ready local filing, never a silent drop.",feedback,"{note: what happened / the observation}|{kind: defect | pattern | candidate}",anytime,,,false,{project-root},"a labelled issue on the module's feedback repo (approval-gated), or a paste-ready filing in _agent/feedback-outbox/ on transport failure"
```

(Exact prose is the builder's to polish; the shape — quoted free-text, 13 fields, `FB`,
`feedback` action — is scope.) The row reaches live vaults via `vlt-upgrade`'s
`merge-help-csv.py` step (`skills/vlt-upgrade/SKILL.md:58-60`) and fresh installs via setup
(`skills/vlt-setup/SKILL.md:95-96`).

**Why:** A14/R2 — **this surface is caught by nothing**: `check_group_b` validates header,
field count and quoting but never that each shipped skill has a row. A rail nobody's help
surface lists is an ingress mechanism vaults cannot find, and lint exits 0.

### F7 — `.claude-plugin/marketplace.json:21-38` `plugins[0].skills[]`: the install surface

**Current state:** 16 entries, no `./skills/vlt-feedback` (verified). Package-lint **C5**
(`tools/package-lint.py:234-241`) fails both directions: an unlisted on-disk `skills/vlt-*`
dir is "silently doesn't ship".

**The change:** add `"./skills/vlt-feedback"` to `skills[]`. (The `"version"` string is
untouched — the dual bump rides the release build, B9-4.)

**Why:** A14/R2's lint-caught half; without it C5 blocks the v0.12.0 tag — by design.

### F8 — `CLAUDE.md:87-92` (*Git & publishing*): `.github/` joins the release-commit surface

**Current state:** the release-commit enumeration reads "`skills/`, `.claude-plugin/`,
`tools/`, README, LICENSE" (`CLAUDE.md:88-90`) — `.github/` is tracked-but-unenumerated the
moment F1 lands (roundtable A16's exact note).

**The change:** add `.github/` to the enumerated surface with its qualifier (repo-side field
contract; tracked and public; **not** part of the own-the-apply copy surface — like `tools/`,
documentation of a contract rather than shipped-into-vault content). Ruled **in scope as an
F-site** rather than a release-time obligation: it is one line, this build creates the
surface, and deferring it re-creates the exact "tracked yet outside the enumerated surface"
state A16 flagged.

**Why:** A16 — the v0.12.0 release commit will contain `.github/`; the factory's own
publishing rule must say so before the release, not after.

### F9 — `inbox/README.md`: pointers to the contract's shipped home (factory-side)

**Current state:** describes filename convention and lifecycle; no header shape; no mention
of the remote rail (verified).

**The change:** two pointer lines, no mechanics restated: (1) remote filings arrive as
GitHub issues and are materialized by the factory intake — the field contract (payload,
labels, `origin:` header) is single-homed at `skills/vlt-feedback/references/field-contract.md`;
(2) a materialized filing carries `origin: <repo>#<n>` per that contract. Gitignored,
factory-only, costs nothing in the release.

**Why:** A15/Paige — README becomes a pointer; B9-5 will extend the lifecycle prose when the
intake lands, citing the same home.

## Registration

- **`.claude-plugin/marketplace.json` `plugins[0].skills[]`** — F7 (package-lint C5 enforced).
- **`module-help.csv` row** — F6 (enforced by nothing; R2 makes it scope; it is acceptance
  check (1)'s explicit grep).
- **Skill-asset manifest** — no action: `verify-skill-manifest.py` computes scope by walking
  source `vlt-*` dirs (`:72-87`); `vlt-feedback` and its reference ride automatically.
- **No version bump, no consumer walk:** `vlt-feedback` pins no convention
  (`depends_on: []`) and no convention rule changes. R1 pricing of the non-handshake gates:
  **C6** not touched (no governance-bundle edit — F4/F5 are vlt-setup surfaces, not the
  contract); **E4** not owed (no new package-lint check is added); **E5** not owed (no
  workflow `.js` asset). C5/C7/E1/E3 all *apply* to the new skill and are named in
  Verification.

## Out of scope (dispositioned)

1. **The factory intake** (materialization on `vault-accepted`, capture-state transitions,
   Discovery's `origin:` exclusion, `arc-closeout` Stage 5 issue-close) — **B9-5's**, ordered
   after this build; it cites F3's contract. This brief defines the labels and the `origin:`
   shape B9-5 consumes; it builds none of B9-5's mechanics.
2. **Retiring vlt-core's `vlt-file-feedback` mint** — explicit **owner act post-ship**
   (owner-ruled at filing, carried at capture; durability posture untouched).
3. **E4 community/noise traffic** — released as a standing watch (roadmap Evidence-debt
   dispositions); no build can discharge it; disposition 7 keeps the partition honest.
4. **The A21 field-facing PARA posture** — flagged by B9-2's brief to **B9-4's** brief;
   not this build's.
5. **`check_group_b`'s missing per-skill-row check** — surfaced by the roundtable and
   **captured for `inbox/`** (roadmap §Captured for inbox, item 1); building the check here
   would smuggle an unfiled, uncaptured item into scope. The CSV row is protected by R2 +
   the acceptance grep instead.
6. **`merge-config.py`'s silent key-drop** — same status (§Captured for inbox, item 3); this
   build routes *around* it per A13 rather than fixing it.
7. **A `vault_structure` entry for the outbox** — rejected (disposition 5): E2 table-sync
   cost for a failure-only directory; fixed-path precedent exists.
8. **Prompting for `feedback_repo` at setup** — rejected (disposition 2): silent default,
   like `vault_structure`'s no-per-path prompt; override remains available.

## Verification (unit, at rest — lifecycle step 5)

- **The contract-agreement fixture run (ship-verifiable check (i)).** In a temp fixture vault
  (scratch `_bmad/config.yaml` with a `vlt:` section, no network): run `vlt-feedback`'s
  compose path to the **failure artifact** (transport deliberately absent), then verify
  **three-way field agreement** mechanically — the field ids in
  `references/field-contract.md`, the `id:` keys in both F1 forms, and the section headers of
  the composed artifact are the same set (grep/diff, recorded). This is the one failure the
  "designed together as one field contract" ruling exists to prevent.
- **The `gh` degradation probe (ship-verifiable check (ii)).** Same fixture, `PATH` without
  `gh`: the run must emit the **named** `gh-missing` error and write the paste-ready artifact
  (labels + origin-vault pre-written) and print its path + manual route. Repeat with `gh`
  present but a failing `gh auth status` if cheaply simulable; otherwise verify the
  `gh-unauthenticated` branch by protocol-text review and say so.
- **Registration greps:** `vlt-feedback` present in `marketplace.json` `skills[]`; the FB row
  present, 13 fields, free-text quoted (run `uv run tools/package-lint.py` groups **A/B/C/E**
  mid-arc — C5 proves the marketplace half, B proves the row's *form*; the row's *presence*
  is the explicit grep, per R2).
- **C7/E3 hygiene:** `references/field-contract.md` is named by `vlt-feedback`'s SKILL.md (C7
  router integrity); no `name@version` token appears in the new skill's files outside
  `depends_on:` (E3 stray-pin).
- **Handshake bipartite re-check:** no convention `version:` moved and no `consumers:` list
  changed — the check of record is package-lint **Group E** in the mid-arc run above; no
  hand-written handshake grep.
- **Fixture extension (R2, package-lint sense):** not applicable — no release-gate check is
  added or changed (no `tools/test-package-lint.py` case, no `CASE_FLOOR` move).
- **Legal response (R3):** not applicable — no vault-side finding class is added.
  (`gh-missing`/`gh-unauthenticated` are the skill's own named errors with their response —
  the paste-ready artifact — stated at their single home, F2/F3.)
- **Enumeration widening (R4):** `_agent/feedback-outbox/` is **declared outside** the
  enumerated live-read classes, with reasoning: it is written only on transport failure, is
  not always-loaded (no boot-cost), is not a decay-drained accumulating record (its files are
  transient — deleted or archived by the filer once pasted; the skill says so), and no vital
  or manifest enumerates a class it belongs to. A declared exclusion, not a silent omission.
- **Labels at rest:** after the owner runs F1's `gh label create` sequence, `gh label list
  --repo mggower/bmad-module-vlt` shows all seven (bound: before the v0.12.0 tag).
- **Scrub:** no personal or vault-local content in any shipped file; worked examples in F2/F3
  use placeholder paths (`_agent/feedback-outbox/{date}-{slug}.md` style); the vlt-core mint
  is not copied from (F2); the transport slug is public module metadata (disposition 2).
- **Release note (not this build):** B9-3 is not the release build — the dual version bump,
  `--expect-version 0.12.0` gate and CHANGELOG entry ride **B9-4**. This build's title ships
  verbatim into `CHANGELOG.md` at that release.

## Acceptance (live — appended to the roadmap ledger)

Four checks. Per A20 the ledger partitions by release; (1) and (2) fall under **"Discharges
on the v0.12.0 run"**; E1–E3 are field-contingent with **named discharging events** (R5).

1. **`[ship-verifiable]` — the rail is registered, agreed, and gated, at rest / at the
   v0.12.0 gate.** (a) package-lint C5 passes with `vlt-feedback` listed and the FB
   `module-help.csv` row is present, quoted, 13-field (explicit grep — lint cannot catch its
   absence, R2); (b) the contract-agreement fixture run is recorded: field-contract ids ==
   both issue forms' `id:` set == the composed payload's sections (check (i)); (c) the `gh`
   degradation probe is recorded: named `gh-missing` error + paste-ready artifact with labels
   and origin-vault pre-written (check (ii)); (d) all seven labels exist on the transport repo
   (`gh label list`, bound before the tag); (e) the D6 record stands in the brief and the
   shipped skill: the mandatory preview-approval gate is in `vlt-feedback`'s protocol text.
2. **`[ship-verifiable, v0.12.0 run]` — the transport arrives in a live vault.** On the
   owner's vlt-core upgrade to v0.12.0 (the A20 obligation run): `config.yaml`'s `vlt:`
   section carries `feedback_repo` (reported `module_keys_defaulted` or preserved), the
   live `module-help.csv` carries the FB row post-merge, and `vlt-feedback` is on disk with
   its reference.
3. **`[field-contingent]` — E1 shared-vault attribution + E3 `gh` variance, one named
   event** (A20/R5): **a `vlt-feedback` run from the work machine's app-vault, performed by
   the owner, bound before Arc 9 closeout** — E1 discharges when the posted issue's
   origin-vault field correctly names app-vault while the GitHub author is the owner's
   account; E3 discharges on **either** that successful run **or** a recovered failure
   artifact (the amended-E3 either-way design). Vault: app-vault (work machine — the one
   place the factory cannot exercise; vlt-core cannot produce this event). A missed bound is
   recorded at closeout as a miss, never a silence — these do not gate closeout
   (`build-brief` §9), but they are bound, not wishes.
4. **`[field-contingent]` — E2 scrub-gate efficacy.** Discharges **only** on a filing
   carrying **real personal-domain signal** whose posted payload shows the gate scrubbed or
   blocked it — a machinery-only filing proves nothing and must not tick this (capture's
   explicit instruction). Event: the first personal-domain-adjacent filing from any live
   vault; unschedulable by nature and named as such; vault: any work vault.
