# B5-1 acceptance check 2 — the work vault's numbers (vlt-sayari instrument run)

- **Date:** 2026-07-30 11:11
- **Filed by:** owner (run executed by the factory session at the owner's direction)
- **What this is:** the field-contingent half of B5-1's acceptance — the work-vault
  instrument run named by pre-ideation ruling 2 (measure first). These are the numbers
  the pre-hoc/post-hoc governance ruling is made against, and the measure-first gate
  B5-7/B5-8's briefs cite. Check 1's vlt-core baseline
  (`skills/reports/cost-baseline-2026-07-29.md`) is the floor; this is the
  signal-bearing measurement.
- **Vault measured:** `vlt-sayari` at `~/Vaults/vlt-sayari` — readable
  directly from the factory machine at run time. (The B5-1 brief's premise that the
  factory cannot read this vault no longer holds; noted so the anatomy's
  named-vault requirement is discharged honestly, not by proxy.)
- **Command:** `uv run tools/cost-manifest.py --vault ~/Vaults/vlt-sayari`
  at factory working tree `2f19251` + B5-4..B5-6 uncommitted edits (the instrument
  itself is B5-1's shipped `c1a4f9b` version, untouched since). Exit 0.
- **Read-only proof:** full vault mtime snapshot (1,317 files) before and after the
  run — byte-identical, no file changed.
- **Spot verification:** `_agent/log.md` 340,749 bytes and `_agent/dispatch.md`
  129,450 bytes match independent `wc -c` exactly; 8 convention files on disk match
  the conventions table. Log entries: parser reports 419 against 420 raw `## [`
  lines — the one uncounted line is `## [2026-07-02 12:00] relay: engineer →
  creative — 1 item`, a relay note without the canonical `|` separator; the
  tolerant parser correctly excludes it.

The verbatim report follows, unedited.

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

Read from `_bmad/config.yaml` key `vlt.vault_structure` (15 keys).
No fallbacks — the vault's map carries every canonical key.

## Beat-2 variable surfaces (the orient reads)

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| _agent/log.md (full) | 340,749 | 43,528 | ~56,586–85,187 |
| _agent/dispatch.md (full — a partner reads only its open slice, but the slice is semantic; file size is the honest measurable) | 129,450 | 16,860 | ~21,918–32,362 |
| _agent/backlog.md | 17,869 | 2,355 | ~3,062–4,467 |
| _agent/log.md (last-5-entries slice — the contract's recency read) | 7,291 | 1,089 | ~1,416–1,823 |
| _agent/wiki/index.md | 5,268 | 652 | ~848–1,317 |

### Per-partner memory (identity.md + thread.md + capabilities/)

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| navigator (identity+thread, capabilities/ ×7) | 323,191 | 47,136 | ~61,277–80,798 |
| engineer (identity+thread, capabilities/ ×7) | 260,961 | 35,587 | ~46,263–65,240 |
| creative (identity+thread, capabilities/ ×1) | 56,390 | 8,309 | ~10,802–14,098 |
| librarian (identity+thread) | 16,836 | 2,385 | ~3,100–4,209 |
| researcher (identity+thread) | 9,734 | 1,411 | ~1,834–2,434 |
| **partner memory total** | **667,112** | **94,828** | **~123,276–166,778** |

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

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| _agent/conventions/extraction.overlay.md | 20,179 | 2,734 | ~3,554–5,045 |
| **overlays total** | **20,179** | **2,734** | **~3,554–5,045** |

Workflows (`.claude/workflows/*.js`):

| surface | bytes | words | est. tokens |
| --- | ---: | ---: | ---: |
| .claude/workflows/vlt-lint-full.js | 22,809 | 2,992 | ~3,890–5,702 |
| .claude/workflows/vlt-review-council.js | 12,755 | 1,745 | ~2,268–3,189 |
| .claude/workflows/vlt-consult.js | 10,180 | 1,412 | ~1,836–2,545 |
| **workflows total** | **45,744** | **6,149** | **~7,994–11,436** |

## `{log}` derivations (derive-only — no thresholds, no judgments)

- Total entries: **419**
- By type: ingest: **14**, backlog-reconcile: 1, consult: 1, dev-loop: 32, dispatch: 54, dispatch-drain: 1, extract: 11, hub: 4, lint: 2, mint: 1, problem-solving: 1, project-spec: 24, research: 5, session: 197, spec-external: 1, track: 70
- By partner: (none — partner-less generic op): 3, creative: 33, engineer: 122, ideation: 1, librarian: 65, navigator: 186, researcher: 8, tech-writer: 1
- First entry: 2026-06-24 — last entry: 2026-07-28
