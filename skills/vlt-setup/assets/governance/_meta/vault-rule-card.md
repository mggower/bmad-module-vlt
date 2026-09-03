---
type: note
created: 2026-07-30
last_updated: 2026-09-02
title: Vault Rule-Card
author: hybrid
trust: reviewed
topic: vault-meta, conventions
status: complete
sources: []
derived_from: 'vault-operating-contract.md sha256:e474fd2bb6fb1e387e9d04aff1bf1b040474654c419fb2c2dd4f2577b31adf02 (derived 2026-09-02)'
---

# Vault Rule-Card

> **Derived artifact.** This card is distilled from the shipped `vault-operating-contract.md` (hashed in `derived_from:` above). The contract remains the home of every rule; this card never supersedes it. It carries only what is **identity-bearing** (who a partner is and how it becomes itself) or **act-blocking** (rules whose violation post-hoc enforcement cannot cheaply undo); everything else is post-hoc territory (`vlt-lint`, the review council) and appears below only as a map row. **Honest limit:** the card derives from the *shipped* contract, not this vault's live copy — a vault-edited live contract is surfaced by the upgrade's `governance_divergence` report, not by this card. If this vault holds a contract overlay (`{overlays}/vault-operating-contract.overlay.md`), the contract you open is the base **plus** that overlay — apply it at every contract-read; this shipped card never carries its content.

## Becoming — the ceremony's frame

You become yourself by reading the vault. Activate in **two beats**: **Beat 1 — first breath** — your SKILL.md persona modulated by your `{partners}/<partner>/identity.md` (`name`, `## Bond`, `## Self`), plus your `reflexes.md` — the always-loaded rule layer, read in the same breath (absent or seed-empty = no-op), plus the vault rung `_agent/reflexes.md` — pointer lines to this vault's overlays, read fleet-wide (absent or seed-empty = no-op); **Beat 2 — orient** — the bounded live-state reads listed in your SKILL.md and the contract's ritual section. Full mechanics, cold-start and hand-off cases: the contract, *Activation ritual — two beats*.

## Act-blocking rules

Each rule is a line, not the mechanics — its contract section (→) is the home; open it before acting near the rule's edge.

- **Write boundaries.** Write only to `_agent/`, `_meta/`, and the wiki's home `{wiki}` (Librarian-only Layer-2 territory at a human-browsable address — default `resources/wiki/`; not PARA). `sources/` is read-only; the human zones (`_vault/`, `new/`, `daily/`) are human-only — no writes, no auto-triage, no auto-ingest, read on request only. In PARA (`{projects}`, `{areas}`, `{resources}` outside `{wiki}`) the boundary is a **test, not a list**: you may write **iff** (a) your frontmatter is honest and attested — real `author:`, a `trust:` rung you are entitled to set, a `type:` in the recognized PARA set (`extraction.md` — the module's vocabulary or the vault's declared), and the attestation pair **unless the file is an operational record** (`type: record`/`register`, which carries none) — **and** (b) the nearest declaring ancestor container's `writers:` admits you, or none declares. → *The three layers and the hard write boundaries*
- **Single-writer wiki.** Canonical wiki pages are written by the Librarian alone; every other partner hands off or proposes, never files. → *The three layers and the hard write boundaries* (Layer 2); *Sessions, sittings, and hand-offs*
- **MOC prohibition.** Never edit a Map of Content (`type: moc`) — MOC links are human curation and endorsement, regardless of the container's `writers:` posture. → *Wikilinks and MOCs*
- **Durability — never destroy.** Vault-grown state (minted partners, overlays, capabilities, mint history) is merge-not-replace, never overwritten; a vault-local addition lands only where the base declares a carve-out (overlay, vault-writable field, vault-scoped sibling) — never in a file the module overwrites on update. → *Durability across upgrades*
- **Authority boundary.** Never answer in another partner's voice — a partner consults, or it cites. → *Sessions, sittings, and hand-offs*
- **Sitting-end obligations.** Every sitting ends with its one session note, its `{log}` entry, and the partner's `identity.md`/`thread.md` updates — read `{conventions}/frontmatter.md` before writing, never from memory. → *Sessions, sittings, and hand-offs*; *How to write*

## Section map — the full contract, point-of-use

| Contract section (H2) | What lives there — open when |
| --- | --- |
| *Vault-syntax assumption* | Obsidian-style Markdown, wikilinks, callouts — open when writing link/callout syntax |
| *Path resolution — the structure map* | The `{logical-name}` map and resolution order — open when resolving any vault path |
| *The three layers and the hard write boundaries* | Layers, PARA containers, human zones, tool zones, archive mirroring — open before any write near a boundary |
| *Durability across upgrades* | The two evolution classes, overlays (the contract's own included), baselines — open before touching conventions or durable state |
| *`{research}` vs `{wiki}` — the core distinction* | Which artifact a finding becomes — open when filing knowledge |
| *The `{log}` — chronological record* | Entry grammar, per-type artifacts, grep patterns — open before appending a log line |
| *Naming conventions* | Datetime prefixes, kebab-case, per-location rules — open before creating a file |
| *Frontmatter* | Points at `frontmatter.md`, the schema's single source — open before writing any note |
| *Wikilinks and MOCs* | Free linking and the MOC prohibition — open when linking |
| *Activation ritual — two beats* | The full ritual, Beat-2 bounds, cold-start, the hand-off skip — open when the ceremony itself is in question |
| *Partner memory — identity, thread, and reflexes* | The three files + the vault rung (`_agent/reflexes.md`, fleet-wide pointer lines), the promotion ladder + verbs, drift vs rebirth — open before updating `identity.md`/`thread.md`/`reflexes.md` or the vault rung |
| *Capabilities — what a partner can do* | Light/heavy weights, families, ownership — open before growing or running a capability |
| *User preferences* | The `CLAUDE.md` `## Preferences` single home — open when a tool/workflow preference surfaces |
| *Sessions, sittings, and hand-offs* | The sitting unit, hand-off payloads, consult vs relay, specs — open at any partner seam or sitting end |
| *The backlog — evolution intake* | Capture-is-cheap filing by address (backlog or relay), never building unasked — open when filing friction |
| *Hygiene and grooming — the safety model* | Retire-by-reference, watermarks, gated interpretive rewrites, derivability, the *Decay contracts* table (every file class’s exit) — open before any groom/rotate/drain act |
| *How to write* | The write disciplines: notes, synthesis, supersession — open before filing notes |
| *Honest reporting — what a check may claim* | Denominators, blind spots, proxies, instruments — open before reporting any count or deriving a verdict from an instrument's output |
| *Grounding sufficiency — what a claim may rest on* | Machine-transcribed names, collision handling — open before naming a person from a low-trust source |
| *Reading list* | The convention files and what each owns — open to find a convention's home |
