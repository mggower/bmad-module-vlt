# Candidate: graduate the `dev/` developer code zone into the shipped operating contract

_Filed 2026-07-12 **on behalf of `vlt-sayari`** (no inbox access; signal carried from
its own backlog by the factory-side handoff inspection — see
`skills/reports/handoff-2026-07-12/05-field-inspection-vlt-sayari.md`). This is a
**candidate** (vault-proven pattern proposed for upstreaming), not a defect._

## The pattern, as grown in the field

vlt-sayari is a development-support vault: its Engineer partner works against real
codebases (11 codebase maps, 5 dev-loop runs against live sprint stories). To give
partners a sanctioned read surface into code, the vault grew a **`dev/` zone**:
symlinks to external checkouts (`dev/sayari-ai`, `dev/arc`), wired 2026-07-08,
machine-local by design, declared in a vault-local `CLAUDE.md ## Local zones` section,
and slated for Obsidian excluded-files so it never syncs.

The vault's own backlog explicitly requests the upstream move: "Graduate the `dev/`
developer code zone into the shipped operating contract… Verified working here
2026-07-08."

## Why it plausibly belongs in the contract

- The operating contract's zone vocabulary (three layers, human zones, tool zones)
  has no slot for "external code the partners may read": `sources/` is read-only
  *knowledge* material, `.claude/`/`_bmad/` are "ignored as knowledge." A code checkout
  is neither — it's a live, out-of-vault, read-only reference surface.
- The pattern generalizes to any development-flavored vault (the module's second field
  profile — see the 05 dossier's two-animals contrast), and leaving it vault-local
  means every such vault re-invents the zone, its name, and its boundary rules.
- It has real boundary questions the contract should answer once: read-only-for-
  partners? (sayari's usage: yes — the Engineer maps and digests, never edits through
  the vault); excluded from ingest/lint sweeps? (must be — symlinked repos would
  swamp any scan); excluded from sync/backup? (machine-local by nature).

## Grounding notes for capture (factory-side, checked 2026-07-12)

- The shipped contract's structure map and zone sections
  (`skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md`) carry no
  `dev/`-like entry; `module.yaml`'s canonical `vault_structure.default` map likewise.
- Adjacent open issue the capture should weigh together: the contract's structure-map
  table has already drifted behind `module.yaml` (missing `specs` — see handoff
  `02-module-map.md` §5.2). Adding a zone is a **rule change** → contract edit
  discipline applies (the contract is un-handshaked by design; single-home + pointers),
  and the same edit could fix the drift.
- Sayari-side residue if this ships: its vault-local `## Local zones` CLAUDE.md section
  becomes redundant-with-the-base — the overlay-subsumption analogue for contract prose
  has no mechanism (contract isn't overlaid); the upgrade note should just tell the
  owner to trim it.

## Provenance

- Vault: `vlt-sayari`, backlog item (open, filed by the vault 2026-07-08-era) +
  `CLAUDE.md ## Local zones`; verified working in the field since 2026-07-08.
- Related to nothing currently roadmapped; natural home is the next capture run
  (frontmatter@4 cycle or Arc 4).
