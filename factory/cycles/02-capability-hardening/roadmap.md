---
title: 'Inbox Evolution Roadmap — Arc 2: capability field-hardening + installer interop'
status: 'CLOSED 2026-07-06 — SHIPPED v0.5.0 2026-07-03 (commit c542e4b, tag v0.5.0 on origin/main); live acceptance rode the vlt-core 0.4.0→0.5.0 upgrade + 2026-07-06 vault-evolution run (evidence: the 2026-07-06 inbox filing batch was produced post-upgrade; build-13 header migration confirmed run in anger by 2026-07-06-091002 filing). Owner ruled archive 2026-07-06. Still open elsewhere: vlt-track loop-profile watch item (carried forward), bmad-module-builder template drift to file upstream to BMAD-METHOD (owner action). This arc is archived — do not append.'
module_code: 'vlt'
created: '2026-07-03'
updated: '2026-07-06'
derives_from:
  - 'inbox/2026-06-27-160109-light-capability-source-type-frontend.md'
  - 'inbox/2026-06-27-162915-heavy-source-prep-interpret-split.md'
  - 'inbox/2026-07-03-120000-bmad-installer-interop-warnings.md'
predecessor: 'skills/reports/archive/inbox-evolution-roadmap.md (Arc 1 — CLOSED, builds #3–#11 shipped v0.4.0)'
intent: >
  Same loop as Arc 1: capture everything vlt-core filed since v0.4.0 shipped, grounded
  against current module source; then ideate + build in owner-steered groups. This doc is
  the durable cache — it spawns per-build briefs (build-12-*.md, …) the way Arc 1's roadmap
  spawned build-3 through build-11.
---

# Inbox Evolution Roadmap — Arc 2

## The through-line (why these three filings are one story)

Arc 1 built the machinery (capability object, handshake, durable upgrade). Arc 2 is that
machinery **meeting the field**: the first real light capability was minted and *run in
production* (filings 1–2), and the first *foreign* tool — the generic BMad installer —
scanned a vault with vlt installed (filing 3). Both encounters validated the architecture
and returned the residue only real use surfaces: two doc-level ambiguities, one reusable
orchestration pattern worth naming, and two install-surface deviations from the canonical
BMad module shape. Nothing structural broke. All three filings are hardening, not redesign.

---

## Capture — all three filings (grounded against module source 2026-07-03)

### A2-1. Light capability, first instantiation — the "source-type front-end" (2026-06-27) — `…160109-light-capability-source-type-frontend.md`

**Context.** vlt-core minted the Librarian's `ingest-youtube` — the vault's **first light
capability** and first use of any partner's `capabilities/` folder. The build-7 model held
up in anger. Three findings filed; grounding adjusts one of them.

**(a) `mint-verb-not-subject` stale guidance — ⚠️ PROVENANCE CORRECTION during grounding.**
The stale phrasing ("same verb, new subject → per-partner profile + **gated registry
row**") is **not in module source** (grep-verified across `skills/` and the contract). It is a
**vlt-core-local memory** — `[[mint-verb-not-subject]]`, cited in vlt-core's
`_agent/mint/decision-log.md:253`, which itself already notes the registry-row half is
superseded. The module already states the modern realization: `vlt-mint/SKILL.md:35`
(`add a capability` routes by `write_scope`) and `:107` (light = own-zone file, "Register
**nothing** in the help CSV"). **Residual module-side action shrinks to:** at most one
explicit line in the mint narrative — *"existing verb + new source type → light capability
profile in the owning partner's zone (no registry row); only heavy registers a CSV row"* —
so the next minter reaching for verb-not-subject lands on the light path directly.
Phase-E-shaped (mostly already shipped).

**(b) `sources/` deposit vs "never a shared lane" — ✅ CONFIRMED real ambiguity, 3 sites.**
The light-capability wording says "never a shared lane" without defining *shared lane*:
- contract `vault-operating-contract.md:195` — "writes only the partner's own zone … never a shared lane"
- `capability-template.md:30` and `:80` — same phrasing (template body + `own-zone-only` family invariant)
- `vlt-lint/SKILL.md:66` — the lane-safety guard flags "a write **outside the owner's own
  zone** — into the wiki, another partner's zone, or any shared lane" → a correct raw-input
  deposit to `sources/` **would read as `capability_lane_violation`** under current wording.

Ruling to enshrine (made + documented vault-side): **"shared lane" means a
*synthesized/single-writer* lane (the wiki).** Appending a **new raw-input file** to
`sources/` — the immutable input tray the user already writes freely, with no single-writer
owner — is lane-safe, stays own-zone-compatible, and does **not** promote a light cap to
heavy. Modifying an existing source is still out. Fix = one clarifying line at each of the
three sites (contract + template agree = single-home; lint guard wording made consistent so
the check stays honest).

**(c) Name the "source-type front-end (light)" pattern + the `scripts/` sibling — ✅ CONFIRMED gap.**
To teach an existing ingest/verb a new *input form*: mint a light capability owned by the
verb's partner — an own-zone profile (`capabilities/<slug>.md`) that fetches + normalizes
the new form into the text the verb already eats, plus a **`capabilities/scripts/<tool>`
sibling** for reusable tooling. Writes only scratch + a raw-input deposit; the canonical
write stays with the unchanged verb skill. Council-none, upgrade-safe, no skill
proliferation. `capability-template.md` currently shows only the bare `.md` — no mention
that a light cap may carry a `scripts/`/`assets/` sibling (grep-verified). Fix = one note in
the template (+ optionally reference the pattern from vlt-ingest / the mint narrative).

**Filing's open design questions (carry, don't resolve now):** a declared
`deposits:` field for mechanical lint verification (filing leans no — YAGNI at n=1); promote
"source-type front-end" to a Model-B **family** once a second instance lands (premature —
but note this would finally exercise build-7's shipped-but-unexercised family machinery).

**Risk/migration:** doc-only, zero migration, **no version-handshake** (the contract is not
handshaked — Arc 1 held it out — and the capability template is a template, not a
convention). Vault-grown light caps live in the agent zone and survive upgrades by
construction.

### A2-2. Prep/interpret split for heavy-source ingest (2026-06-27) — `…162915-heavy-source-prep-interpret-split.md`

**Context.** First production run of `ingest-youtube` (1:24:28 video, ~16k-word transcript)
located the real cost + risk of a heavy-source ingest: fetch/clean are cheap and safe
(deterministic scripts); the context cost is *reading the full transcript to interpret it*,
and the error surface is the *extraction handoff* on a saturated context. The lever: **keep
the raw source out of the interpreting context**.

**The pattern (to absorb verbatim, with its three invariants):**
> **Prep/interpret split (heavy-source ingest).** For any source too large to interpret
> without flooding context (long transcript, long PDF, multi-page crawl): a **prep
> sub-agent** (mechanical: fetch → normalize → deposit source-of-record to `sources/` → run
> the credential scan) returns a **neutral navigational brief** — section map, locations,
> verbatim located quotes, flags; never the raw body, never an interpretation. The **owning
> partner** then runs the unchanged ingest verb on fresh context, reading *selectively* into
> the deposited source at the brief's locations.
1. **Single-writer holds** — prep agents deposit + report; the canonical write stays the
   verb skill's (same shape as `vlt-lint-full`: read-only finders, one serial writer).
2. **The brief is a map, not the territory** — the partner verifies each located quote
   against the deposited source before ingesting.
3. **Neutral map, not a digest** (the load-bearing call) — a pre-interpreted digest primes
   and quietly corrupts the fresh reading that is the whole point.
Sequencing: re-ingest check runs **up front** (cheap `{log}` grep gates the fetch);
credential scan runs **in the prep agent** (needs cleaned text).

**Grounding:**
- The module has **no pattern-catalog home**: `batch-ingest-fanout-pattern` (which the
  filing cites as the sibling many-sources axis) is **vlt-core-local, not in module source**;
  `vlt-ingest/SKILL.md` has **zero** sub-agent/fan-out guidance today (grep-verified).
- The nearest module precedent is **vlt-lint's own escalation**: `vlt-lint/SKILL.md:39`/`:45`
  — delegate full mode to the fan-out workflow above ~30 pages; "the fan-out only earns its
  overhead at scale." That is exactly the **threshold-not-always-on** discipline the filing
  asks vlt-ingest to adopt (filing item 3), and the single-writer framing it asks to reuse.

**Ship shape (filing's, grounded as sensible):** (1) name the pattern where orchestration
patterns live — **open ideation question: where is that?** (candidates: a section in
`vlt-ingest`, the contract's ingest discussion, or a first small pattern-catalog home;
related: should `batch-ingest-fanout` be absorbed upstream at the same time, since the two
patterns stack?); (2) `vlt-ingest` heavy-source note — Steps 1–3 delegable to a prep
sub-agent returning a neutral brief, Step 4+ stays with the invoking partner; (3) state the
size threshold so small ingests stay inline; (4) capability-template note pointing
source-type front-ends that wrap heavy inputs at this split as default orchestration
(inherits the digest-vs-map discipline). **Risk/migration:** doc/guidance-only, zero
migration, no handshake.

### A2-3. BMad installer interop — `module.yaml` not locatable + CSV header off-canon (2026-07-03) — `…120000-bmad-installer-interop-warnings.md`

**Context.** A manual generic-BMad upgrade (installing the CIS module, vlt excluded) scanned
vlt-core's installed modules and warned three times against vlt. Nothing broke; all three
warnings say vlt's install surface deviates from the canonical BMad module shape — the exact
friction the standing "prefer standard BMad, no bespoke" ruling exists to eliminate.

**F1 — installer cannot locate vlt's `module.yaml` (agents + config-scope fallout). Grounded, cause OPEN.**
- Live-vault evidence: **no module** — vlt *or* canonical bmb/bmm/cis/core — places a
  `module.yaml` under `_bmad/<code>/` (verified by ls). So the fix is NOT "copy it to
  `_bmad/vlt/`" as the filing guessed — the installer looks elsewhere.
- `module.yaml` lives at `.claude/skills/<setup-skill>/assets/module.yaml`; bmb's setup skill
  is **`bmad-bmb-setup`**, vlt's is **`vlt-setup`**. **Leading hypothesis:** the installer
  probes by the `bmad-<code>-setup` naming convention (or an equivalent manifest pointer),
  and vlt's off-pattern setup-skill name is why only vlt warns. **Confirm against installer
  source at ideation** — the installer isn't present in the vault; note also bmm/cis/core
  have no `module.yaml` anywhere in the vault yet reportedly didn't warn (bundled with the
  installer package, or warned unquoted — check).
- Consequences (per the warnings): the **agent roster** (3 shipped partners — including the
  naming ceremony's `[agents.<code>]` config-side half from Build #1) never reaches
  `config.toml`; **config answers default to team scope** (blast radius today = only
  `vault_structure`, but it's a standing scope bug). Worth checking whether this explains any
  past roster-UI blankness in vlt-core.
- Whatever the fix (rename/alias the setup skill, manifest pointer, or a placed copy), it
  must be **durable through `vlt-upgrade`'s own-the-apply** and reconciled every upgrade.

**F2 — `module-help.csv` header drifted from canonical (`after,before` vs `preceded-by,followed-by`). ✅ FULLY GROUNDED + upstream-drift discovery.**
- vlt ships the old header: `skills/vlt-setup/assets/module-help.csv:1` **and** the canonical-header
  constant in `merge-help-csv.py:36–37` (`"after"`, `"before"`). Canonical schema (installer
  warning + current builder template): `preceded-by,followed-by`. Same 13 columns/positions;
  installer recovers positionally but warns on every run.
- **⚠️ Drift originates upstream, in `bmad-module-builder`'s own scaffolding** (discovered
  during grounding): the builder's `setup-skill-template/assets/module-help.csv` already
  carries the **canonical** header, but the template's `merge-help-csv.py` (:36–37) **and all
  three scaffold tests** still hardcode `after,before`. vlt inherited the old header at
  scaffold time; the builder skill is internally split *today* and will re-mint the same
  drift into the next module. (Side-fix for the builder skill — distinct from, but sibling
  to, the vlt fix; decide at ideation whether it rides along.)
- **Migration wrinkle CONFIRMED at `merge-help-csv.py:291`** — `header = target_header if
  target_header else source_header` means **target-header-wins**: renaming the shipped source
  alone never fixes an already-installed vault; vlt-core's live `_bmad/vlt/module-help.csv`
  keeps the old header forever. Needs an explicit **rename-in-place migration** when the
  target header is the known-old variant (most naturally in the merge script itself, or
  vlt-upgrade's reconcile). Local-mint rows (chef, dog-trainer, health-coach, retired local
  vlt-track) are positionally unaffected but **must survive the rewrite** (B1 rule).
- Sites that move together: shipped CSV header, merge-script constant, any vlt-mint/vlt-setup
  prose naming the columns (the build-10 always-quote teaching).

**Suggested shape (filing's, non-binding):** one hardening build — (1) determine the
installer's actual `module.yaml` resolution + make it durable; (2) the two-column rename
across all module-owned sites + target-header migration; (3) acceptance = re-run a generic
BMad install/upgrade against a vault with vlt installed → **zero** vlt warnings, roster in
`config.toml`, all local mints intact. **Risk:** low-moderate — F2 is mechanical with a real
migration; F1 has an external-unknown (installer behavior) to pin first.

---

## Cross-cutting threads

- **The capability model survived first contact; what it lacked was *definitions at the
  edges*.** A2-1(b) (what exactly is a "shared lane") and A2-1(c) (what may a light cap
  carry) are boundary clarifications, not model changes — the cheap kind of hardening that
  only field use reveals.
- **Same escalation discipline everywhere.** A2-2's threshold-gated prep/interpret split is
  vlt-lint's `--full`→fan-out move applied to ingest. The module now has two instances of
  "inline until scale, then delegate finding/prep to sub-agents, keep the single serial
  writer" — arguably *the* vlt orchestration principle; where it gets named is A2-2's open
  question.
- **"Prefer standard BMad, no bespoke" now has a mechanical enforcer** — the generic
  installer itself (A2-3). Its warnings are effectively a free conformance lint for vlt's
  install surface; the acceptance criterion "zero vlt warnings on a generic BMad run" is a
  durable regression check, not a one-off.
- **The builder-template drift (A2-3 F2) is Arc 1's coherence lesson replayed one level up:**
  a schema changed (`after,before` → `preceded-by,followed-by`) and its consumers (template
  merge script, tests, and every already-scaffolded module) didn't move — exactly the
  convention→consumer failure the build-4 handshake was built to catch, but living in
  tooling the handshake doesn't cover.
- **vlt-lint keeps accreting field-honesty checks** — A2-1(b) touches the lane-safety guard's
  wording so a correct capability doesn't false-positive; same spirit as build-8's firewall
  and build-3's noise fixes.

---

## Proposed grouping (a PROPOSAL — owner steers at ideation, as in Arc 1)

| Build | Theme | Folds in | Why this grouping |
|---|---|---|---|
| **build-12 — capability field-hardening** | Doc/guidance reconciliation from the first light-cap lifecycle | A2-1 (shared-lane definition ×3 sites incl. the lint guard, scripts/ sibling note, verb-not-subject line) + A2-2 (prep/interpret pattern + vlt-ingest heavy-source note + threshold + template pointer) | Both filings are the same event (first light cap, mint then production run), doc-only, zero migration, no handshake — one small Phase-A/E-shaped build. Open Q inside: where named patterns live. |
| **build-13 — installer interop** | Canonical-shape conformance | A2-3 F1 (module.yaml resolution — pin the installer's probe first) + F2 (column rename + target-header migration + B1-safe rewrite) | Different risk class: an external unknown (F1) and a real live-vault migration (F2). Keep separate from the doc build so its spike/migration doesn't gate the cheap wins. Builder-template side-fix: decide whether it rides along or files separately. |

**Sequencing RESOLVED 2026-07-03 (owner deferred to recommendation):** grouping as proposed;
order build-12 → build-13; F1 spike done at ideation time (closed, below); builder-template
fix ruled **out of build-13 scope** — the drift exists in the *latest upstream BMB* (verified
in `~/.bmad/cache/external-modules/bmb`), so it must be **filed upstream to BMAD-METHOD**
(owner action); upgrading the installed BMB would not resolve it.

### F1 installer spike record (CLOSED 2026-07-03)

Read the installer source directly (`bmad-method` in the npx cache,
`tools/installer/project-root.js:102` `resolveInstalledModuleYaml`). **Root cause:** the
installer resolves an installed module's `module.yaml` **only from its own source caches**
(built-in `src/modules/`, `~/.bmad/cache/{external,community,custom}-modules/`) — never
from the vault. Its candidate probes *include* the "BMB standard"
`{root}/skills/*-setup/assets/module.yaml` (matched by any `*-setup` dir name) and it
matches by the yaml's `code`/`name` — so **vlt's layout (`skills/vlt-setup/assets/module.yaml`)
and identity (`code: vlt`) are already conformant.** The warning fires because vlt was
installed as a **Claude plugin from GitHub** and therefore exists in **no BMad cache**
(`external-modules/` = bmb/cis/tea only; the other caches empty). The earlier naming
hypothesis (`bmad-<code>-setup`) is **refuted**; the filing's guessed fix
(`_bmad/vlt/module.yaml`) is a non-location. **Fix (briefed):** vlt-setup/vlt-upgrade seed +
reconcile a copy of the module source into `~/.bmad/cache/custom-modules/` (the installer's
own designed home for url-source modules; walker accepts `.claude-plugin/` as the repo
marker), with graceful degrade when `~/.bmad` is absent. Details in the build-13 brief.

### Briefs spawned
- **`build-12-capability-field-hardening.md`** (✅ **BUILT 2026-07-03, unit-verified**: 5 files — contract *Capabilities* shared-lane definition; template mirror + `scripts/` sibling + named front-end pattern; vlt-lint guard reworded (deposit-permissive, still flags genuine violations); vlt-mint verb-not-subject line; vlt-ingest *Heavy sources* section with 3 invariants + ~15k-word threshold. Zero handshake/version lines touched.) — A2-1 + A2-2.
  Design calls: shared-lane definition single-homed in the contract's *Capabilities* section
  with template + vlt-lint-guard mirrors; source-type front-end pattern named in
  `capability-template.md` + one-line verb-not-subject reconciliation in vlt-mint;
  **prep/interpret split's mechanics live in `vlt-ingest/SKILL.md`** (no pattern-catalog
  artifact — precedent: vlt-lint's fan-out lives in vlt-lint; catalog is YAGNI at n=1),
  threshold-gated (~15k words / ~1.5h transcript), template pointer for heavy-input
  front-ends. Zero migration, zero handshake.
- **`build-13-installer-interop.md`** (✅ **BUILT 2026-07-03, commit `a27b6cc`**: F1 = minimal cache stub seeded by vlt-setup Provision §5, vlt-upgrade inherits via provisioning hand-off; **verified end-to-end against the real installer resolver**. F2 = canonical header in shipped CSV + script constant, rename-in-place target migration reported as `header_migrated`, 17 unit checks incl. B1-preserve + build-10 malformed-skip regressions + unknown-header pass-through.) — A2-3. F1 = cache
  seed/reconcile per the spike; F2 = header rename at the two grounded sites (CSV `:1`,
  merge-script `:36–37`; vlt-mint prose confirmed clean) **+ rename-in-place target-header
  migration inside `merge-help-csv.py`** (runs before row parsing so B1 preserve + build-10
  skip/report see canonical schema), unit-tested 4 ways. One small live migration, B1-safe.

---

## Deferred acceptance ledger (Arc 2)

Arc 1's batching decision no longer applies — `vlt-upgrade` exists and has run clean across
multiple version steps on two vaults. Acceptance for Arc 2 builds can ride the **next
ordinary vlt-core upgrade** (no special gate). Checks to be appended per build at brief
time, per Arc 1 convention. Standing items carried from the field:

- [ ] **(carried from 0.4.0 watch item — STILL OPEN at arc close, carries forward past Arc 2)** vlt-core's vertical partners (Dog Trainer /
  Health Coach) wore the *local* vlt-track with the loop profile **inline in SKILL.md**;
  shipped 0.4.0 reads it from `capabilities/track.md`. First post-upgrade track loop on
  vlt-core may not find the profile → likely needs a per-wearer migration of the inline
  Loop-profile block. Verify by running a real track loop post-0.4.0-upgrade; if it breaks,
  it's a build-11 field defect → inbox.
- [x] **build-12:** a `sources/` raw-input deposit by a light cap passes
  `vlt-lint` clean; the lane guard still flags a genuine synthesized-lane write.
  (Discharged at arc close 2026-07-06 — 0.4.0→0.5.0 upgrade + vault-evolution run clean.)
- [x] **build-13:** a generic BMad install/upgrade against a vault with vlt
  installed emits **zero** vlt warnings; agent roster present in `config.toml`; live
  `module-help.csv` header migrated in place with all local-mint rows intact.
  (Discharged 2026-07-06 — the in-place header migration confirmed run in anger by the
  `2026-07-06-091002` filing, `merge-help-csv.py:61`.)

---

## Status & next step

- **CLOSED 2026-07-06.** Shipped v0.5.0, acceptance rode the vlt-core 0.4.0→0.5.0
  upgrade + 2026-07-06 vault-evolution run; owner ruled archive. Briefs + the three
  filings archived alongside this doc. Do not append.
- **This doc** = Arc 2's durable capture + grouping cache. `status: ideation`.
- **Capture complete 2026-07-03**, all three filings grounded against module source. Two
  grounding corrections recorded above: A2-1(a) shrinks (stale guidance is vault-local, not
  module source), A2-3 F2 gains an upstream cause (builder-template drift) and F1 loses its
  guessed fix (`_bmad/<code>/` placement is not where canonical modules put it either).
- **Next:** per-build ideation with owner steering — grouping, order, the F1 installer
  spike, and where the named-patterns home lives. Each ideation spawns its brief
  (`build-12-*.md`, `build-13-*.md`) per Arc 1 convention.
- Filings stay in `inbox/` until their build ships, then archive (Arc 1 convention).
