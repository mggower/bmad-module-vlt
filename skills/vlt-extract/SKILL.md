---
name: vlt-extract
description: Shape wiki knowledge into a human-facing PARA artifact. Use when the user wants a curated deliverable from what the vault already knows — 'extract from wiki', 'build a resource doc on X', 'pull a project brief on Y', 'turn the wiki into a deliverable', filed into projects/, areas/, or resources/. Reaches the wiki only — for new knowledge use vlt-research; to file a source use vlt-ingest.
depends_on: ["extraction@2", "wiki-supersession@1", "frontmatter@4", "write-verification@1"]
---

# vlt-extract

## Overview

Extraction turns wiki knowledge into a PARA artifact — a curated, human-oriented deliverable filed into `projects/`, `areas/`, or `resources/`. The wiki stays the source of truth; the artifact is a synthesis shaped for a specific reader at a specific moment. It reaches the wiki **only** (no web, no research notes, no source files — extracting from anything but the curated wiki bypasses the curation that makes it trustworthy). The output is a deliverable, not a transcript of wiki content. Runs interactively (the interview shapes the artifact) or headless ("extract a resource doc on X").

PARA folders are human territory; **extraction is the one sanctioned way a partner writes into them** — this skill does not touch canonical wiki pages.

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

The vault is this project — resolve paths relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). Logical names used (default, relative to the project root): `index` → `_agent/wiki/index.md`, `wiki` → `_agent/wiki/`, `log` → `_agent/log.md`, `archive` → `_archive/`, `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/` (vault-local convention overlays); the PARA targets are `projects/`, `areas/`, `resources/` at the project root. Note the **active partner** for the log tag.

**Read the conventions you will obey** before writing: `{conventions}/extraction.md` (trust ladder, filename rules, `type:` mapping, re-extraction supersession) and `{conventions}/wiki-supersession.md` (the inline `[!superseded]` callout shape) — read each together with its `{overlays}/{name}.overlay.md` if present, honoring the overlay's appended rules.

## Step 1: Interview

Through a short conversation (2–3 exchanges, woven naturally — not a numbered list; read the user's message first and ask only what's unclear), establish:

- **The topic** — concrete enough that a slug is obvious.
- **The purpose** — a project brief, a reference doc to share, a weekly dashboard, a meeting one-pager? Purpose shapes structure.
- **The reader** — the user's own use, a collaborator, future-self? Audience shapes tone and density.
- **The target PARA folder, if already obvious** ("a project brief on X" → `projects/`); otherwise defer to Step 4.

Confirm the brief before moving on.

## Step 2: Read the wiki — hard thin-wiki gate

Read `{index}` first, then read fully every relevant page (err toward more — a missed page is a gap in the artifact). Brief the user: "The wiki has N pages on this — `<page1>`, `<page2>`, `<page3>`. I'll synthesize these." Ask whether any are missing or should be excluded.

**Hard gate:** extraction requires **at least 2 contributing wiki pages.** If only one (or none) covers the topic, **stop** — a one-page extraction just duplicates the page. Offer the real alternatives instead: a richer wiki pass first (`vlt-ingest` a source, or `vlt-research` the topic), or simply link the single page. Proceed only if the user explicitly overrides with a reason.

## Step 3: Synthesize

Draft the artifact as prose shaped for the reader — not a dump of wiki content:

- **Shape for the purpose.** A project brief leads with decisions and open questions; an area dashboard with current state and commitments; a resource doc with clear explanation. Pick the shape from Step 1.
- **Cite wiki pages inline** via `[[wikilinks]]`; every non-trivial claim is traceable to a page.
- **Surface contradictions, don't resolve silently.** If two pages disagree on something the artifact must state, raise it with the user before writing a resolution.
- **Carry forward caveats.** When a source page carries marked contradictions (`[!superseded]`/`[!stale]`, or a Contradictions section), note that caveat in the artifact — don't present a contested claim as settled.
- **Leave wiki machinery behind otherwise.** Source counts and routine `[!superseded]` callouts don't belong in the deliverable unless material to the reader; the wiki is the audit trail, the artifact points back via `sources:`.

**Drafting:** for a large artifact, write a working draft to `<target>/<slug>.draft.md` so multi-turn synthesis survives an interruption; finalize by dropping the `.draft` suffix once the user confirms shape and folder. A short artifact can stay in conversation until confirmed.

## Step 4: Choose the target PARA folder

Prompt the user — no default:

> "Which PARA folder — `projects/`, `areas/`, or `resources/`?"

If unsure: **`projects/`** = discrete work with a defined outcome/"done" state; **`areas/`** = ongoing commitments without an end (dashboards, standing references); **`resources/`** = reference material not tied to a commitment (primers, how-tos). The choice sets both the path and the `type:`.

## Step 5: Filename and near-duplicate check

Propose a kebab-case slug from the topic (no datetime prefix — extracted artifacts have stable identity). Before writing, check the target folder for an overlapping artifact (`ls <target>/`), comparing the *concept* not just the slug string — leading noun, synonym, lexical or topic overlap.

If something overlaps, ask: create new, or **update the existing in place**? Default to update-in-place when ambiguous — re-extraction is the expected path as a wiki topic evolves, and a near-duplicate artifact is the dominant PARA failure mode. On an in-place update, apply the re-extraction supersession rules from `{conventions}/extraction.md` (which defer to `{conventions}/wiki-supersession.md`).

## Step 6: Write the artifact

Write `<target>/<slug>.md`.

```yaml
---
type: <project | area | resource>     # matches the target folder
created: YYYY-MM-DD                    # immutable
last_updated: YYYY-MM-DD               # set today; bump on every re-extraction
title: <human-readable title>
author: hybrid
trust: reviewed                        # confirm by depth — see below
topic: <subject area>
status: <in-progress for projects | ongoing for areas | complete for resources>
sources:
  - <wiki page 1>
  - <wiki page 2>
  - <wiki page N>
---
```

`author: hybrid` is fixed (agent-drafted synthesis, human-curated extraction). **Confirm `trust:` by depth** rather than assuming: default `reviewed` per the extraction convention when the human has actually validated the synthesis; use `raw` when it's a quick agent draft they haven't reviewed yet. `sources:` must list every wiki page that contributed — the audit trail back into the vault; **no `key:` field.**

Sections (a baseline, not a straitjacket — add what the purpose needs, e.g. Goals/Milestones for a brief, Current State/Commitments for a dashboard):

- **Overview** — 2–4 paragraphs of synthesis shaped for the reader; the frame for the whole artifact (write last, place first).
- **Thematic sections** — organized by what the reader needs (decisions, facts, steps, context), not by wiki page; cite pages inline.
- **Open Questions** — what's uncertain; name the tension.
- **Sources** — the wiki pages consulted as `[[wikilinks]]`, one line each on what they contributed.

## Step 7: Append to the log

Append a partner-tagged entry to `{log}`:

```
## [YYYY-MM-DD HH:MM] extract (<partner>) | "<Topic/Title>" — N wiki sources → [[<target>/<slug>]]
```

`N` is the number of pages in `sources:`. Write **no** session note — the summoning partner owns the session log (operating contract § session-ownership).

## Step 8: Verify and attest

Run the **tier-1 checklist** from `{conventions}/write-verification.md` on the artifact — that file is the checklist's single home; read it, don't re-derive it from memory. **Fail-open:** fix what you can, flag what you can't, always complete the write. Then write the attestation on the artifact: `verified_by: vlt-extract`, `verified_at: <today>` (fields + freshness rule: `{conventions}/frontmatter.md`).

Report the result (what was extracted, to which folder, and "verification passed" or the specific gaps flagged).

## Tips

- **Extraction is curation, not retrieval.** If it reads like concatenated wiki pages, it was copied, not extracted. Shape it for the reader.
- **Re-extraction is the common case.** Wiki topics evolve and artifacts go stale — overwrite in place (bumping `last_updated`), with supersession callouts for substantively changed claims, rather than spawning a near-duplicate.
- **A thin wiki is a stop, not a caveat.** Fewer than two pages → offer a wiki pass or a direct link; don't synthesize thin air.
