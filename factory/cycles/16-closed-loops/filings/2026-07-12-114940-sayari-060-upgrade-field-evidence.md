# Field evidence: vlt-sayari's 0.4.0→0.6.0 upgrade exercised the untested half of the machinery

_Filed 2026-07-12 **on behalf of `vlt-sayari`** (no inbox access; carried by the
factory-side handoff inspection — full dossier:
`skills/reports/handoff-2026-07-12/05-field-inspection-vlt-sayari.md`). This is an
**evidence filing** (acceptance/validation data, in the Arc-2 build-13 tradition of
acceptance arriving via a filing), plus two small watch notes. No defects to report._

## 1. The 2026-07-09 upgrade ledger entry is the richest field validation the module has

One own-the-apply run performed, with zero destruction: a **two-version jump**
(0.4.0→0.6.0, skipping 0.5.0), **3 local mints preserved** (`vlt-agent-navigator`,
`vlt-agent-engineer`, `vlt-project-spec`; `local_mints_preserved` confirmed all 3, 17
registry rows), the **build-13 help-CSV header migration** run on the jump path
(`after,before` → `preceded-by,followed-by` — this install predated 0.5.0, so the
migration got its second, harder field exercise), a real **overlay-subsumption pass**
(build-18) against a live ~270-line `extraction.overlay.md` (verdict: nothing retired
— correctly, with reasoning recorded), and the **proto-spec retrofit scan** (build-15)
surfacing exactly one candidate, offering it, and accepting the owner's decline
("a resolved two-round handoff, not an ongoing versioned contract. Nothing moved.").
Governance landed byte-identical to shipped 0.6.0 (verified factory-side by diff).

## 2. Machinery that was "shipped-but-unexercised" now has field evidence — here, not vlt-core

- **Capability families:** first real instance — `_agent/capabilities/families/
  project-hub.md`, `instances: [navigator, creative]`, binding a producer/consumer pair
  (created 2026-07-10). The families-are-dead-weight question is answered: exercise, don't prune.
- **Convention overlays:** full lifecycle run — creation, a council-gated overlay edit
  (REVISE→PASS, 07-01), append-only discipline with RETIRED-in-place banners, and the
  upgrade-time subsumption check.
- **Loop profiles (vlt-track):** live — the Navigator's `capabilities/track.md` carries
  a complete `## Loop profile` block driving 6 real project loops.
- **Skill retirement:** first field retirement of a minted skill (`vlt-spec-external`,
  minted 06-29, retired 06-30, replaced by `vlt-project-spec`) — managed residue,
  archived not deleted.
- **Personalized extraction:** both named opt-ins (`vlt-track`, `vlt-project-spec`) in
  real use — the extraction@2 firewall is no longer dormant-at-rest.

## 3. Watch note: the loop-profile watch item is only HALF discharged

The Arc-1→3 ledger item reads as one check but is two claims. vlt-sayari discharges the
**machinery half**: a profile in the shipped location works in anger. It does NOT
discharge the **vlt-core wearer half**: vlt-core's vertical partners (Dog Trainer,
Health Coach) still show **zero** loop profiles in any capability file (per the
2026-07-12 vlt-core inspection), so their first post-0.4.0 track loop remains the
untested event — if their loop config lives inline in SKILL.md (or nowhere), that's
the anticipated build-11 field defect. Acceptance-discharge should tick this item as
"machinery: discharged (sayari evidence); vlt-core wearers: still open."

## 4. Watch note: upgrade preserve-sets must derive from disk, not the prior ledger

Within **two days** of the 07-09 upgrade, the vault grew 4 new light capabilities
(`project-synthesis`, `dev-loop`, `codebase-backlog`, `hub`), 1 minted skill
(`vlt-hub`), and the `project-hub` family — none in any ledger inventory. This is not a
defect (vlt-upgrade's pre-flight already snapshots from the intact vault), but it is a
standing hazard for any future tooling or session habit that treats the previous ledger
entry as the preserve checklist. If the prose in `vlt-upgrade/SKILL.md` Step 1 doesn't
already say "derive the snapshot from disk, never from the prior ledger entry"
explicitly, one sentence would make the derive-first rule load-bearing there too.
New durability shapes to be aware of on this vault's next upgrade: vault-root
`DESIGN.md`/`PRODUCT.md` and a grown `CLAUDE.md ## Local zones` section (see the
companion `dev/`-zone candidate filing).

## Provenance

- Vault: `vlt-sayari` (synced snapshot; `.claude/`, `_bmad/` file contents, and
  `.baseline/` unverifiable — every claim above rests on md surfaces: the upgrade
  ledger, mint decision-log, dispatch, conventions dir, and a factory-side governance
  diff). Re-check list for the work machine is in the 05 dossier §9.
- Capture note: §1–2 are acceptance/validation evidence (route to the ledger, not a
  build); §3 amends an existing ledger item's discharge criteria; §4 is a
  one-sentence-candidate for vlt-upgrade prose, below build threshold on its own.
