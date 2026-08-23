---
title: 'Build #6 — Lifecycle Durability: the vlt-upgrade skill + append-only convention overlays + merge-not-replace registration (filing #8)'
status: 'BUILT 2026-06-24 — unit-verified at rest; live acceptance (a real durable vlt-core upgrade) is itself the unlock for ALL deferred acceptance and runs on the first safe upgrade.'
build_log:
  - 'BUILT 2026-06-24. Part 3 (B1, first — the must-ship): merge-help-csv.py gained a --live-skills-dir input + filter_rows_preserving_local() — a target vlt row absent from the bundle but whose skill dir exists live is preserved (local mint); a row whose dir is gone is still dropped (zombie); shipped rows refresh. Without the flag, original blind anti-zombie behavior (correct for fresh install). UNIT-TESTED: shipped row refreshed, dog-trainer mint preserved, ghost zombie dropped, other-module untouched; fallback path strips as before. Part 2 (overlays — the heart): operating contract gained a "## Durability across upgrades" section (the durability principle [two classes/two fates] + the append-only overlay mechanism + base-vs-baseline safety net); structure map + module.yaml gained overlays (_agent/conventions/) + upgrade_ledger (_agent/upgrade-ledger.md); all 5 base conventions got an "Overlay note" pointer (prose — NO version bump, handshake undisturbed); vlt-lint gained two coherence checks (convention_base_divergence vs .baseline + overlay_not_append_only/overlay_orphan) + report keys + {overlays} resolution; vlt-mint Edit-a-convention kind BRANCHED (vault-local addition → write {overlays}/{name}.overlay.md append-only, no base touch / no version bump / no consumer walk; generic rule change → base + existing version-handshake, bound upstream); vlt-setup stashes stock .baseline/ (module-owned, overwrite-on-update) + ensures {overlays}/. Part 5 (§A1 + ledger): vlt-mint .decision-log.md → _agent/mint/decision-log.md (all 5 refs relocated + idempotent migration + pointer-stub spec); vlt-setup ensures _agent/mint/; ledger schema authored in vlt-upgrade (append-only standing record). Parts 1+4 (vlt-upgrade skill + B2): new skills/vlt-upgrade/SKILL.md — pre-flight snapshot (from living vault) → apply (own-the-apply merge-copy / degrade-to-bracket) → reconcile (B1 merge-not-replace, B2 body-restore, overlay+baseline refresh, decision-log+overlay-lift migrations, calls vlt-setup) → post-flight divergence report + append ledger; registered in assets/module-help.csv (row UP, quoting-guard-validated). Part 6 (durability principle): folded into the contract section above. VERIFIED: handshake re-checked bipartite-consistent (no version drift — all acks match: frontmatter@2, wiki-index@2, wiki-consolidation@1, wiki-supersession@1, extraction@2); 0 leftover "this skill''s .decision-log" refs; {overlays}/{upgrade_ledger} defined in both SSoTs; assets CSV parses (13 rows); vlt-upgrade ships as a sibling dir (op skills are not enumerated in module.yaml). NOT built (per scope): Capability strand (build-7), vlt-lint method-traces firewall (build-8), section-override overlays (deferred until needed), interactive 3-way merge UI (superseded by overlays).'
phase: 'Phase D (Lifecycle durability)'
module_code: 'vlt'
created: '2026-06-24'
updated: '2026-06-24'
derives_from:
  - 'skills/reports/inbox-evolution-roadmap.md (Phase D row + Phase D ideation record + B2 spike record)'
  - 'inbox filing #8 — upgrade ownership + divergence durability (…100300…)'
ideation_decisions:
  - 'Installer posture (owner: "decide during ideation" → resolved): vlt-upgrade PREFERS TO OWN THE APPLY (merge-copy from a reachable module source, no destruction) and DEGRADES TO BRACKET MODE (snapshot-before → installer runs → reconcile-after) only when the bits arrive welded to a destructive apply. Honors the owner ideal (own the upgrade entirely) without depending on the B2 installer unknown.'
  - 'Acquire/apply split: the upgrade is two welded jobs — acquire new bits + apply to the vault. Owning the APPLY is all the owner ideal requires; acquire-without-destructive-apply is the happy path, destructive-installer-then-reconcile is the guard rail.'
  - 'Convention durability = APPEND-ONLY OVERLAYS (owner idea, supersedes 3-way merge). Base convention stays pristine/overwrite-safe; local edits live in _agent/conventions/{name}.overlay.md (agent-zone durable); consumers merge base+overlay on read. The collision never forms (vs 3-way, which only detects+resolves it).'
  - 'Overlay semantics: APPEND-ONLY (overlay can only ADD field/rule/section — no addressing, unambiguous precedence) + DETECT-AND-REPORT safety net for direct base hand-edits. Section-override DEFERRED until a real edit demands it.'
  - 'The owner''s deepest grief is losing LOCAL CONVENTION EDITS (over bodies/registration) — so the overlay mechanism is the heart of build-6, weighted above B1/B2 in design care.'
  - 'Divergence ledger = a STANDING, append-only record of vault evolution over time (owner: "something I would want to keep to view evolution") — top-level _agent/upgrade-ledger.md (spans more than mints), NOT a throwaway per-upgrade diff.'
  - 'Overlays rewire vlt-mint''s convention-edit kind (built in build-5): it must write the OVERLAY, never the base — making mint output upgrade-durable by construction. Concrete edit to a just-built thing.'
  - 'Overlays extend Phase B''s handshake resolver: consumers already declare depends_on: ["name@version"]; "also read the local overlay" is the same resolver, one step further. Coherence (B) and durability (D) are the same seam.'
  - 'B1 (merge-not-replace registration) is the CONFIRMED in-repo must-ship (B2 spike): merge-help-csv.py:117-119 strips ALL vlt rows then re-appends only bundled rows → local mints deregistered every upgrade regardless of installer copy strategy.'
  - 'B2 (body-restore) is INSURANCE under the safe-pessimistic assumption — cheap whether installer clean-replaces (A, mandatory) or copies-over (B, belt-and-suspenders). Does not block specification.'
  - '§A1 decision-log relocation is GENUINELY still Phase D: build-5 moved the resumable planning doc to _agent/mint/ but left the PERMANENT .decision-log.md in the clobber-prone vlt-mint/ skill dir.'
  - 'Scope: filing #8 durability core ONLY (owner ruling). Capability-object strand → build-7; vlt-lint method-traces firewall → build-8. Both ride Phase B''s handshake machinery as their own small builds AFTER D.'
---

# Build #6 — Lifecycle Durability

## Thesis

Vault was designed to **grow** — and in `vlt-core` it actually did: three partners minted in anger, a
65-page wiki, local convention edits. But every upgrade runs through the generic, module-agnostic BMad
installer, which has no concept of vault-specific evolution and can silently destroy it. The machinery
is excellent at *making* things and weak at *preserving integrity across change*. Build #6 closes that
gap from the durability end (the coherence end was build-4).

The decisive reframe from ideation: **the upgrade is two welded jobs — *acquire* the new module bits
and *apply* them to the vault.** The installer does both, destructively. But owning the *apply* is all
the owner ideal ("vlt-upgrade owns the upgrade entirely") actually requires. So `vlt-upgrade` is built
to **prefer owning the apply** (merge-copy from a reachable module source — no destruction ever) and
**degrade to bracket mode** (snapshot → installer → reconcile) only when the bits arrive welded to a
destructive apply. The skill ships under known facts; the B2 installer unknown only toggles whether
body-restore is mandatory or belt-and-suspenders.

The second reframe — the owner's: **the thing most worth grieving is local convention edits, and the
cure is structural, not after-the-fact.** Don't 3-way-merge collisions at upgrade time; make the
collision *never form*. Base conventions stay pristine (always overwrite-safe); local edits live in a
separate, agent-zone **overlay** file; consumers merge base+overlay on read. This is the same move vlt
makes everywhere — separate durable location + merge, not edit-in-place — and it threads straight into
Phase B's handshake resolver. Coherence and durability turn out to be one seam.

---

## Part 1 — `vlt-upgrade` skill (filing #8 §C)

A new skill `skills/vlt-upgrade/SKILL.md` that **owns the lifecycle** and *calls* `vlt-setup` for
provisioning (never duplicates it).

**Mode / flow:**
1. **Pre-flight (always, from the living vault — before any destruction):** snapshot the non-stock
   state and **append** to the divergence ledger (Part 5): minted `vlt-agent-*` partners (dirs +
   their help rows), convention overlays present, any base conventions hand-edited (vs the stock
   baseline — see Part 2), governance divergences. This must run while the vault is intact.
2. **Apply — happy path (own it):** if the updated module source is reachable, **merge-copy** shipped
   `vlt-*` skills into the install — refresh shipped skills, never touch unshipped `vlt-agent-*` dirs,
   never overwrite agent-zone. No destruction occurs; B2 is moot on this path.
3. **Apply — fallback (bracket):** if the bits arrive only via the destructive installer, the
   installer runs (pre-flight already snapshotted), then reconcile repairs.
4. **Reconcile:** B1 merge-not-replace registration (Part 3) · B2 body-restore if a destructive apply
   ran (Part 4) · overlay-aware convention handling (Part 2) · run any pending migrations.
5. **Post-flight:** divergence report in the confirm summary (governance files that differ; mints
   restored/re-registered; overlays applied) · hand off to `vlt-setup` for provisioning.

**Design notes:** `vlt-upgrade` calls `vlt-setup`, doesn't reimplement it (filing #8 §C). The
"prefer-own / degrade-to-bracket" branch is a single decision at step 2 — same reconcile logic both
ways. Idempotent: re-running on an already-current vault is a no-op that still refreshes the ledger's
"checked, no drift" line.

---

## Part 2 — Append-only convention overlays (the heart; filing #8 B3, reconceived)

The owner's structural answer to "never lose a local convention edit." Supersedes filing #8's
detect-and-report *floor* — detect-report survives only as the safety net (below).

**Mechanism:**
- **Base conventions are never edited in place** → pristine → always overwrite-safe → upgrades apply
  cleanly every time. (This is the invariant that makes the whole upgrade path safe.)
- **Local edits live in `_agent/conventions/{name}.overlay.md`** — agent-zone, upgrade-durable by
  location (never overwritten).
- **Consumers merge base + overlay on read.** This extends Phase B's handshake resolver: a consumer
  that declares `depends_on: ["frontmatter@2"]` now also reads `_agent/conventions/frontmatter.overlay.md`
  if present and applies it after the base. Same resolver, one step further.
- **Append-only semantics:** an overlay may only **ADD** (a new frontmatter field, a new rule, a new
  section). No addressing scheme, unambiguous precedence (base first, overlay appends). Covers the
  80% of real edits ("add `category:`", "add a `track` log type").
- **Safety net (detect-and-report):** to *change* an existing base rule you edit the base directly;
  the upgrade's pre-flight detects a base file that differs from its stock baseline and **reports**
  it (warns, never silently clobbers). Requires a **stock baseline** stashed at install time — see
  below.
- **Stock baseline:** `vlt-setup` stashes a pristine copy of each governance file it installs (e.g.
  `_agent/conventions/.baseline/{name}.md`, agent-zone, never overwritten). "What did I change" =
  current base vs baseline. Only needed for the safety net (overlays don't need it — they're additive).

**Rewires vlt-mint (built in build-5):** the `convention edit` kind currently edits the base in place.
Under overlays it must **write the overlay, never the base** — making the mint's output upgrade-durable
by construction. Its build-4 handshake exit gate still applies (consumers re-pinned to the new
`version` when the *base* version legitimately bumps upstream; an overlay-only local edit does not bump
the base version — it's a local addition, not an upstream convention change).

**Artifacts:** new `_agent/conventions/` overlay zone + `.baseline/` stash; consumer activation/resolver
(the skills carrying `depends_on:`); `vlt-setup` (baseline stash + ensure overlay dir); `vlt-mint`
`convention edit` kind; operating contract (name `_agent/conventions/` as a known location).

---

## Part 3 — B1: merge-not-replace registration (the confirmed must-ship; filing #8 §B1)

`skills/vlt-setup/scripts/merge-help-csv.py:117-119` (`filter_rows`) strips **all** rows where
`row[0] == module_code` then re-appends only the **bundled** rows — so every locally-minted
`vlt-agent-*` help row is destroyed on every merge, regardless of installer copy strategy (the B2
spike's decisive finding).

**Fix (preferred, per filing):** preserve a local `vlt` row when its corresponding skill **dir exists
live** in `.claude/skills/` but is **absent from the bundled CSV** — i.e. distinguish *shipped* rows
(in the bundle → refresh) from *local-mint* rows (not in bundle, dir present → preserve). Rewrite only
shipped rows; carry local-mint rows through untouched.

**Design notes:** needs the live skills dir as an input to the merge (today it only sees two CSVs). The
"dir exists" check is what makes it anti-zombie-safe (a truly orphaned row whose dir is gone is *not*
preserved — that's the original anti-zombie intent, kept). Alt from filing #8 (a durable
`_agent/mint/roster.md` to re-derive rows from) noted but not chosen — the dir-existence check is
simpler and needs no new artifact.

**Artifacts:** `merge-help-csv.py` (+ a live-skills-dir argument), `vlt-upgrade` reconcile step (invokes
it), `vlt-setup` (already invokes it — unaffected on fresh install).

---

## Part 4 — B2: minted-partner body-restore (insurance; filing #8 §B2)

Under the safe-pessimistic assumption (a destructive apply may delete unshipped `vlt-agent-*` dirs),
`vlt-upgrade` reconcile **restores** any partner dir that pre-flight snapshotted but the apply removed.
On the happy path (own-the-apply, step 2.2) no destruction occurs and this is a no-op.

**Design notes:** the pre-flight snapshot is the restore source (or, cheaper, the snapshot just records
*which* dirs are unshipped-but-present and the reconcile skips/guards them). Mandatory only if the
installer clean-replaces (B2-A); belt-and-suspenders if it copies-over (B2-B). Either way it does not
block shipping — the A/B answer only toggles its necessity.

---

## Part 5 — §A1 decision-log relocation + the standing divergence ledger (filing #8 §A1)

**§A1 — decision-log relocation (genuinely still open):** build-5 moved the *resumable planning doc* to
`_agent/mint/` but left the **permanent** `.decision-log.md` in the clobber-prone `vlt-mint/` skill dir.
Relocate `vlt-mint/.decision-log.md` → `_agent/mint/decision-log.md` + pointer stub; update vlt-mint's
two refs (SKILL.md:76, :104, :117 region); idempotent `.decision-log.md` → `_agent/mint/` migration
(mirrors the legacy `thread.md` split); `vlt-setup` ensures `_agent/mint/` exists (build-5 may already).

**Divergence ledger — a standing record (owner call):** `_agent/upgrade-ledger.md`, top-level
agent-zone (spans more than mints), **append-only**. Each upgrade appends a dated block: module version
before/after, mints present + their registration status, conventions overlaid + any base hand-edits
flagged, governance divergences, bodies restored. Between upgrades it's a readable autobiography of how
far this vault has drifted from stock — the owner's "view evolution over time."

---

## Part 6 — The durability principle → operating contract (filing #8)

Add to `_meta/vault-operating-contract.md`: **two classes of evolution, two fates.** Generic evolution
→ upstream (file to the module, ship, receive on upgrade). Vault-specific evolution (minted partners,
local convention edits via overlays, mint/decision history) is **upgrade-durable** — it lives in the
agent zone (`_agent/`, never overwritten) or is reconciled by **merge, never replace**. Durability is a
property of *location + merge strategy*, not of getting an upgrade procedure right each time. Name the
new agent-zone homes: `_agent/conventions/` (overlays + baseline), `_agent/upgrade-ledger.md`,
`_agent/mint/decision-log.md`.

*(This is the operating-contract versioning that Phase B deliberately held out to Phase D. The contract
itself is a governance file under the same overlay regime once this ships.)*

---

## Explicitly NOT in build-6 (and why)

- **Capability-object lightweight tier** → **build-7** (owner ruling: keep separate). Its agent-zone
  home (`{partners}/*/capabilities/`, `_agent/capabilities/`) is reconciled-not-replaced — it *rides*
  build-6's durability machinery but is its own build on Phase B's handshake.
- **vlt-lint method-traces-to-wiki firewall** → **build-8** (deferred from build-5). The personalized-
  extraction firewall check; its own small build on Phase B's handshake machinery.
- **Section-override overlays** — deferred until a real edit needs to *change* (not add to) a base rule.
  Append-only + detect-report covers the present need.
- **Full 3-way governance merge** — superseded by overlays (collision never forms) + detect-report
  safety net. No interactive merge UI.
- **Controlling/wrapping the installer copy** — the B2 spike found this unknowable from module source;
  prefer-own/degrade-to-bracket sidesteps it.

---

## Migration / upgrade path

- **Overlays:** one-time **lift of vlt-core's existing in-place convention edits into overlays** —
  per-file judgment (what did the vault add vs. the stock baseline → move the additions to
  `{name}.overlay.md`, restore the base to pristine). Lint-assisted; document as a recipe. This is the
  *first real exercise* of the overlay machinery.
- **Decision-log:** idempotent move + pointer stub (re-runnable; mirrors the `thread.md` precedent).
- **Baseline stash:** populated going forward by `vlt-setup`; for an existing vault, seed from the
  shipped module source at first `vlt-upgrade` run (best-effort — a hand-edited base with no baseline
  falls back to "report as divergent, can't auto-classify").
- **Ledger:** created lazily on first `vlt-upgrade`. No back-fill.
- **B1/B2:** pure reconcile logic; no data migration.

---

## Build order

1. **Part 3 (B1 merge-not-replace)** — the confirmed must-ship, smallest, self-contained, testable in
   isolation. Unblocks registration durability immediately.
2. **Part 2 (overlays + baseline)** — the heart; the resolver extension + `_agent/conventions/` zone +
   the vlt-mint convention-edit rewire. Largest design surface.
3. **Part 5 (§A1 decision-log + ledger)** — relocation migration + the standing ledger schema.
4. **Part 4 (B2 body-restore)** — reconcile insurance, leans on Part 1's pre-flight snapshot.
5. **Part 1 (vlt-upgrade skill)** — ties it together; orchestrates Parts 2–5; calls vlt-setup.
6. **Part 6 (durability principle → contract)** — last, names the homes the other parts created.

---

## Acceptance / verification

*(Live acceptance is the one this whole roadmap was waiting for: build-6 IS the durable upgrade path
that lets vlt-core finally upgrade and exercise build-3/4/5 in anger. Unit-verify at rest first; the
first real `vlt-upgrade` run on vlt-core then discharges the entire Deferred acceptance ledger.)*

- [ ] A local convention edit expressed as an overlay **survives** an upgrade that bumps the base
  convention upstream — base improved AND local addition both present after, no conflict.
- [ ] A direct hand-edit to a base convention is **reported** (not silently clobbered) at pre-flight.
- [ ] `merge-help-csv.py` **preserves** a local `vlt-agent-*` row whose dir exists live but is absent
  from the bundled CSV; still strips a truly orphaned row (dir gone).
- [ ] On a (simulated) destructive apply, B2 **restores** the snapshotted unshipped partner dirs.
- [ ] Decision-log relocation migration is **idempotent**; vlt-mint refs resolve to the new path.
- [ ] `_agent/upgrade-ledger.md` **appends** a dated block per upgrade; readable as an evolution record.
- [ ] `vlt-upgrade` **calls** `vlt-setup` for provisioning (doesn't duplicate it); happy path performs
  **no destruction**; bracket path reconciles after.
- [ ] vlt-mint `convention edit` now writes the **overlay**, never the base.

---

## Open questions for the build

- **Resolver home:** does base+overlay merge-on-read live in each consumer's activation, or in a single
  shared resolver the consumers call? (Single resolver = DRY, but adds an indirection; per-consumer =
  matches how `depends_on` acks already live inline. Lean: extend the existing per-consumer handshake
  read.)
- **Baseline stash for an already-diverged vault:** seed from current module source at first upgrade
  (best-effort) vs. require a clean re-install to establish it. (Lean: best-effort seed + report
  unclassifiable hand-edits.)
- **Acquire reachability:** on the happy path, *where* does vlt-upgrade find the updated module source
  (a path config, the BMad module cache, a git remote)? Determines how often "own the apply" actually
  fires vs. falling back to bracket. (Empirical — settle at build time against the real install.)
- **Operating contract under overlays:** the contract is itself a governance file — confirm it lands in
  the same overlay regime (it should; Part 6 says so) and that bootstrapping (the contract describing
  the overlay system that governs the contract) isn't circular in practice.
