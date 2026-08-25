# Migrations that amend a base document walk no vault-local overlay — a human caught the resulting stale rule

_Filed 2026-08-23. Evidence: relayed carry-back from vlt-core session vlt-core-d4
(Act 1, commit `10d935e`), factory-verified read-only; the finding is the Act-1
skeptic's unrebutted structural point, which no other council lens engaged.
Classification: **defect** (one proven instance) carrying a **pattern** (the general
gap). Provenance: the 0.14.0 wiki-relocation migration._

## What happened

The 0.14.0 upgrade's wiki-relocation migration moved the wiki
(`_agent/wiki/` → `resources/wiki/`) and updated the BASE contract's path
enumeration accordingly. It walked **no vault-local overlay**. vlt-core's
`frontmatter.overlay.md` §A scoped itself to "`_agent/` and the PARA folders" —
so the relocation silently carried `{wiki}` out of §A's scope. The rule went stale
**by relocation, never by a ruling**, and a human (not a check) caught it; the vault
patched the one instance with a new §D restating the scope as a predicate over
territory.

## The gap

The module's durability posture protects overlays' *bytes* (merge-not-replace,
byte-intact across upgrades) but nothing protects their *meaning*: a migration that
changes what a path resolves to has no obligation to visit overlays whose rules are
stated in terms of that path. The consumer-walk discipline exists for handshaked
conventions (the nine-leg walks) — the overlay layer has no walk of its own.

## Candidate directions (for capture, not answered here)

- Cheapest: a migration-authoring rule — any migration that changes path resolution
  or moves a zone must grep `{overlays}/` for the affected path/key and surface hits
  as a human-gated review bullet (report, never auto-edit — overlays are
  vault-owned).
- Alternatively a lint class: an overlay section naming a path/key whose resolution
  changed since the overlay's `last_updated` — harder to state honestly (needs a
  resolution history).
- The vault's own mitigation (predicate-over-territory phrasing instead of path
  enumerations) is a drafting convention the module could recommend at overlay-mint
  time — it shrinks the exposed surface but does not close the walk gap.
