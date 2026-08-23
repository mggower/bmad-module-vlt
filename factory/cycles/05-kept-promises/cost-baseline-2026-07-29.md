---
title: 'Cost baseline 2026-07-29 — B5-1 measure-first gate artifact'
build: 'B5-1 (the cost instrument)'
tool: 'uv run tools/cost-manifest.py — module mode at build HEAD; vault mode against the vlt-core field vault'
---

# Cost baseline — 2026-07-29

**What this is:** the measure-first gate artifact named by Arc 5 pre-ideation
ruling 2. B5-7's (boot diet) and B5-8's (whale re-cut) briefs cite these numbers;
their dispositions are chosen against them, not against guesses.

**What this is NOT:** the work-machine consumer vault's numbers — the
originating signal's vault, which this machine cannot read. That run is the
owner's (acceptance check 2, field-contingent): `uv run tools/cost-manifest.py
--vault <work-vault-path>`, output filed back to the inbox. The vlt-core
figures below are the floor, not the signal-bearing measurement.

Module mode ran at the build's HEAD (post-9f05579 working tree); vault mode ran
against `~/{field-vault}` (v0.8.0 install). Verified read-only by full mtime
snapshot: zero files changed under the vault.

---

# vlt cost manifest — module mode

> **What this measures:** the *declared* read surface — file sizes in bytes on
> disk (`wc -c` equivalent) and whitespace-split word counts. **Est. tokens**
> is a band, never one number: `[words × 1.3 … bytes / 4]` — the two
> estimators the arc's captures used, which disagree by ~25% on prose. This
> instrument does **not** observe what a live session actually read (that
> would be a session self-report, deliberately unbuilt — A5-13 disposition
> (b)). It measures and reports; it never nags — thresholds and tripping are
> the enforcement kit's (B5-9).

Module source at rest, measured from the repo root. Vault-side field-variable surfaces (index/log/orient reads) are the other half — run `--vault /path/to/vault` for those.

## Per-partner fixed boot (eager — paid at every activation)

Every partner activation opens with its SKILL.md plus a full operating-contract read (the two-beat ritual's opener).

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| vlt-agent-creative (SKILL.md 11,497 + contract 38,271) | 49,768 | 7,498 | ~9,747–12,442 |
| vlt-agent-researcher (SKILL.md 10,426 + contract 38,271) | 48,697 | 7,298 | ~9,487–12,174 |
| vlt-agent-librarian (SKILL.md 10,069 + contract 38,271) | 48,340 | 7,236 | ~9,407–12,085 |

## Governance stock (lazy — point-of-use reads)

Conventions (`_meta/conventions/`):

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| skills/vlt-setup/assets/governance/_meta/conventions/frontmatter.md | 22,977 | 3,302 | ~4,293–5,744 |
| skills/vlt-setup/assets/governance/_meta/conventions/extraction.md | 11,310 | 1,634 | ~2,124–2,828 |
| skills/vlt-setup/assets/governance/_meta/conventions/wiki-index.md | 8,174 | 1,266 | ~1,646–2,044 |
| skills/vlt-setup/assets/governance/_meta/conventions/wiki-consolidation.md | 7,881 | 1,148 | ~1,492–1,970 |
| skills/vlt-setup/assets/governance/_meta/conventions/spec.md | 7,155 | 1,016 | ~1,321–1,789 |
| skills/vlt-setup/assets/governance/_meta/conventions/wiki-supersession.md | 5,532 | 803 | ~1,044–1,383 |
| skills/vlt-setup/assets/governance/_meta/conventions/write-verification.md | 5,520 | 796 | ~1,035–1,380 |
| skills/vlt-setup/assets/governance/_meta/conventions/consult.md | 4,838 | 729 | ~948–1,210 |
| **conventions total** | **73,387** | **10,694** | **~13,902–18,347** |

Contract (broken out — it is the eager read above):

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| skills/vlt-setup/assets/governance/_meta/vault-operating-contract.md | 38,271 | 5,636 | ~7,327–9,568 |

Other `_meta/` files:

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| skills/vlt-setup/assets/governance/_meta/personas/historian.md | 2,779 | 441 | ~573–695 |
| skills/vlt-setup/assets/governance/_meta/personas/pragmatist.md | 2,594 | 405 | ~526–648 |
| skills/vlt-setup/assets/governance/_meta/personas/moderator.md | 2,590 | 394 | ~512–648 |
| skills/vlt-setup/assets/governance/_meta/personas/architect.md | 2,505 | 392 | ~510–626 |
| skills/vlt-setup/assets/governance/_meta/personas/skeptic.md | 2,480 | 396 | ~515–620 |
| **other _meta total** | **12,948** | **2,028** | **~2,636–3,237** |

Governance bundle total: **124,606** bytes, 18,358 words, ~23,865–31,152 est. tokens.

## Skill surface (SKILL.md files only — not whole skill dirs)

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| skills/vlt-lint/SKILL.md | 41,202 | 5,827 | ~7,575–10,300 |
| skills/vlt-dispatch/SKILL.md | 38,285 | 5,962 | ~7,751–9,571 |
| skills/vlt-mint/SKILL.md | 34,519 | 5,023 | ~6,530–8,630 |
| skills/vlt-setup/SKILL.md | 27,053 | 3,692 | ~4,800–6,763 |
| skills/vlt-upgrade/SKILL.md | 26,821 | 3,734 | ~4,854–6,705 |
| skills/vlt-ingest/SKILL.md | 20,967 | 3,106 | ~4,038–5,242 |
| skills/vlt-track/SKILL.md | 16,053 | 2,351 | ~3,056–4,013 |
| skills/vlt-agent-creative/SKILL.md | 11,497 | 1,862 | ~2,421–2,874 |
| skills/vlt-agent-researcher/SKILL.md | 10,426 | 1,662 | ~2,161–2,606 |
| skills/vlt-research/SKILL.md | 10,225 | 1,517 | ~1,972–2,556 |
| skills/vlt-agent-librarian/SKILL.md | 10,069 | 1,600 | ~2,080–2,517 |
| skills/vlt-extract/SKILL.md | 9,596 | 1,407 | ~1,829–2,399 |
| skills/vlt-review-council/SKILL.md | 5,452 | 832 | ~1,082–1,363 |
| skills/vlt-query/SKILL.md | 5,089 | 797 | ~1,036–1,272 |
| **all SKILL.md total** | **267,254** | **39,372** | **~51,184–66,814** |

## Workflow assets

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| skills/vlt-setup/assets/workflows/vlt-lint-full.js | 22,809 | 2,992 | ~3,890–5,702 |
| skills/vlt-setup/assets/workflows/vlt-review-council.js | 12,755 | 1,745 | ~2,268–3,189 |
| skills/vlt-setup/assets/workflows/vlt-consult.js | 10,180 | 1,412 | ~1,836–2,545 |
| **workflows total** | **45,744** | **6,149** | **~7,994–11,436** |

## Named aggregates (the tracked whales — one diff line each)

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| contract | 38,271 | 5,636 | ~7,327–9,568 |
| lint SKILL | 41,202 | 5,827 | ~7,575–10,300 |
| dispatch SKILL | 38,285 | 5,962 | ~7,751–9,571 |
| conventions total | 73,387 | 10,694 | ~13,902–18,347 |
| frontmatter.md | 22,977 | 3,302 | ~4,293–5,744 |
| all-SKILL.md total | 267,254 | 39,372 | ~51,184–66,814 |


---

# vlt cost manifest — vault mode

> **What this measures:** the *declared* read surface — file sizes in bytes on
> disk (`wc -c` equivalent) and whitespace-split word counts. **Est. tokens**
> is a band, never one number: `[words × 1.3 … bytes / 4]` — the two
> estimators the arc's captures used, which disagree by ~25% on prose. This
> instrument does **not** observe what a live session actually read (that
> would be a session self-report, deliberately unbuilt — A5-13 disposition
> (b)). It measures and reports; it never nags — thresholds and tripping are
> the enforcement kit's (B5-9).

An installed vault's field-variable surfaces — the half module mode cannot see. Paths resolve through the vault's own structure map.

## Structure map resolution

Read from `_bmad/config.yaml` key `vlt.vault_structure` (16 keys).
No fallbacks — the vault's map carries every canonical key.

## Beat-2 variable surfaces (the orient reads)

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| _agent/log.md (full) | 151,536 | 18,684 | ~24,289–37,884 |
| _agent/backlog.md | 103,086 | 14,555 | ~18,922–25,772 |
| _agent/dispatch.md (full — a partner reads only its open slice, but the slice is semantic; file size is the honest measurable) | 78,255 | 10,993 | ~14,291–19,564 |
| _agent/wiki/index.md | 39,808 | 5,329 | ~6,928–9,952 |
| _agent/log.md (last-5-entries slice — the contract's recency read) | 4,698 | 651 | ~846–1,174 |

### Per-partner memory (identity.md + thread.md + capabilities/)

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| librarian (identity+thread, capabilities/ ×2) | 177,083 | 26,575 | ~34,548–44,271 |
| creative (identity+thread, capabilities/ ×8) | 82,226 | 11,257 | ~14,634–20,556 |
| researcher (identity+thread) | 72,875 | 10,755 | ~13,982–18,219 |
| chess-coach (identity+thread, capabilities/ ×4) | 38,020 | 6,122 | ~7,959–9,505 |
| chef (identity+thread) | 26,661 | 4,323 | ~5,620–6,665 |
| health-coach (identity+thread, capabilities/ ×1) | 23,873 | 3,571 | ~4,642–5,968 |
| dog-trainer (identity+thread, capabilities/ ×1) | 10,445 | 1,598 | ~2,077–2,611 |
| **partner memory total** | **431,183** | **64,201** | **~83,461–107,796** |

## Installed governance

Conventions (`{conventions}`):

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| _meta/conventions/frontmatter.md | 22,977 | 3,302 | ~4,293–5,744 |
| _meta/conventions/extraction.md | 11,310 | 1,634 | ~2,124–2,828 |
| _meta/conventions/wiki-index.md | 8,174 | 1,266 | ~1,646–2,044 |
| _meta/conventions/wiki-consolidation.md | 7,881 | 1,148 | ~1,492–1,970 |
| _meta/conventions/spec.md | 7,155 | 1,016 | ~1,321–1,789 |
| _meta/conventions/wiki-supersession.md | 5,532 | 803 | ~1,044–1,383 |
| _meta/conventions/write-verification.md | 5,520 | 796 | ~1,035–1,380 |
| _meta/conventions/consult.md | 4,838 | 729 | ~948–1,210 |
| **conventions total** | **73,387** | **10,694** | **~13,902–18,347** |

Overlays (`{overlays}` — top-level files only; `.baseline/` stock copies are upgrade machinery, not a read surface):

*(no overlay files)*

Workflows (`.claude/workflows/*.js`):

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| .claude/workflows/vlt-lint-full.js | 22,809 | 2,992 | ~3,890–5,702 |
| .claude/workflows/vlt-review-council.js | 12,755 | 1,745 | ~2,268–3,189 |
| .claude/workflows/vlt-consult.js | 10,180 | 1,412 | ~1,836–2,545 |
| **workflows total** | **45,744** | **6,149** | **~7,994–11,436** |

## `{log}` derivations (derive-only — no thresholds, no judgments)

- Total entries: **299**
- By type: ingest: **68**, archive: 1, dispatch: 32, extract: 16, filed: 6, fix: 1, handoff: 1, lint: 10, maintenance: 1, mint: 7, remediation: 1, research: 33, session: 104, track: 18
- By partner: (none — partner-less generic op): 7, chef: 15, chess-coach: 20, creative: 13, dog-trainer: 17, health-coach: 12, librarian: 158, meta: 2, researcher: 52, user: 3
- First entry: 2026-06-06 — last entry: 2026-07-29

## Context — `{sessions}` (not a boot read)

- 113 files, 440,763 bytes total

