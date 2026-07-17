---
name: vlt-ingest
description: Integrate a source into the vault wiki. Use when the user adds a file to the sources layer, shares an article or URL, pastes text to file, or says 'ingest this', 'process this source', 'add this to the wiki', or 'what should I take from this?' For curated material already in the vault's sources layer; for open-ended topics that need the web, use vlt-research.
depends_on: ["frontmatter@4", "wiki-index@2", "wiki-consolidation@1", "wiki-supersession@1", "write-verification@1"]
---

# vlt-ingest

## Overview

Ingest is how new knowledge enters the vault. A source comes in raw; by the end its key ideas are integrated into the wiki, connected to what was already known, and any contradictions or updates to existing pages are resolved. The goal is not to summarize the source in isolation — it is to change the wiki *because of* the source. Always ask: **what changes in the wiki because of this?**

vlt-ingest is the **single writer of canonical wiki pages** — the spine of the roster. Other partners propose or hand off sources; ingest is where they land. Runs interactively (a working session) or headless (one-shot "ingest this", fronted by the Librarian).

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

**Resolve paths:**

- The vault is this project (`{project-root}`).
- Resolve every location through the `vault_structure` map: an explicit override wins, else the shipped default. The logical names this skill uses (default shown, relative to the project root): `wiki` → `_agent/wiki/`, `index` → `_agent/wiki/index.md`, `research` → `_agent/research/`, `log` → `_agent/log.md`, `sessions` → `_agent/sessions/`, `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/` (vault-local convention overlays), `archive` → `_archive/`. Below, `{wiki}` etc. mean the resolved path.

**Identify the active partner** (the roster member running this — e.g. `librarian`) for the log tag. If invoked standalone with no partner, omit the tag.

**Read the conventions you will obey** before writing anything: `{conventions}/frontmatter.md` and `{conventions}/wiki-supersession.md` (and `{conventions}/wiki-consolidation.md` if a merge arises in Step 6) — read each together with its `{overlays}/{name}.overlay.md` if present, honoring the overlay's appended rules. These govern every write; honor them exactly.

## Step 1: Re-ingest check

Before any writes, grep `{log}` for a distinguishing token from the source (its URL, its filename, or a short title phrase):

```bash
grep -iE "<url|filename|title-phrase>" {log} 2>/dev/null
```

(The `2>/dev/null` is defense-in-depth — `vlt-setup` creates `{log}` with its header, but a hand-built or pre-setup vault may lack it; a missing log just means "no prior ingest," not an error.)

If a prior `ingest` entry exists, read the linked `{research}/...` note, then show the user **what a re-ingest would change** — the prior note's scope and what this pass would add or revise — before touching it. Ask whether to **update** the existing note, **re-ingest as new** (rare — justify), or **skip**. Default to update-in-place when ambiguous; never silently clobber a refined note. If no prior entry, proceed.

## Step 2: Credential scan

Before writing anything derived from the source, scan its content for secrets — **never write credentials into a derived note**, even when the source itself stays untouched. Flag: API-key prefixes (`sk-`, `pk_`, `AKIA`, `ghp_`, `xoxb-`), long high-entropy tokens (≥32 mixed-case+digit runs), SSNs (`\d{3}-\d{2}-\d{4}`), credit-card-shaped digit runs (Luhn-conformant 16-digit), labelled account/routing numbers. On a match, show it and confirm before writing — do not silently redact. The source layer is read-only; the user may excise an incidental credential from the derived note only.

## Step 3: Read the source

The source is a file in the vault's sources layer (check its subfolders — articles, papers, books, transcripts, notes), a URL (reach the web with whatever web tooling the host provides — fetch the page, or crawl if it spans several pages on one site), or text already pasted in the conversation. Read it in full before doing anything else; read long documents in sections.

## Heavy sources — the prep/interpret split (Steps 2–3 at scale)

For a source too large to interpret without flooding the context — a long video transcript, a long PDF, a multi-page crawl — the cost is not the fetch (mechanical, safe) but *reading the full body to interpret it*, and the risk lives in the extraction handoff happening on a context already saturated with raw text. The lever: **keep the raw source out of the interpreting context.**

**Threshold, not always-on.** Small ingests stay inline — the split only earns its overhead at scale (same discipline as `vlt-lint`'s fan-out escalation). Inline up to roughly what one context can read *and still interpret freshly* — about **~15k words of normalized text (a ~1.5h transcript)**; above that, split:

- **Prep sub-agent (mechanical).** Delegate Steps 2–3's heavy half: fetch → normalize/clean → **deposit the source-of-record to the sources layer** → run the Step 2 credential scan (it needs the cleaned text). It returns a **neutral navigational brief** — section map, transcript/page *locations*, verbatim *located quotes*, and flags. **Never the raw body; never an interpretation.**
- **You, on fresh context (interpretive).** Run the unchanged remaining steps, reading *selectively* into the deposited source-of-record at the brief's locations, for only the passages you will canonicalize.

Three invariants make it safe:

1. **Single-writer holds.** Prep agents fetch/clean/deposit and *report*; they never write the wiki — the canonical write stays this skill's. (Same architecture as `vlt-lint-full`: read-only finders return structured data, one serial writer applies.)
2. **The brief is a map, not the territory.** The full deposited source stays the source-of-record; verify each located quote against it before ingesting, so a prep-agent slip can't become a confident wiki claim.
3. **Neutral map, not a digest** (the load-bearing rule). The prep agent extracts *no interpretation* — structure and located raw material only. A pre-interpreted digest is cheaper on context but **primes and quietly corrupts** the fresh reading that is the split's entire point. Judgment stays here; the agent supplies structure, not conclusions.

Sequencing: the **Step 1 re-ingest check runs up front** as always — a cheap `{log}` grep that gates whether to fetch at all (don't pay for fetch+clean on a re-ingest); the **credential scan rides in the prep agent**. The split applies to *any* heavy input form — a source-type front-end capability that wraps one (see `vlt-mint/assets/capability-template.md`) should default to this orchestration.

## Step 4: Discuss key takeaways

Before writing, surface the 3–5 most significant claims, anything surprising, and which domain(s) this belongs to. Ask the user what to emphasize, de-emphasize, or connect — they know their own knowledge base better than you. Keep it to a couple of exchanges unless the user wants to go deep.

**Partner-fronted mode.** If you were invoked downstream of a partner (the Librarian) that already did this interview — i.e. you arrive with an already-sharp brief or a hand-off payload — treat this elicitation as **satisfied**: state the emphasis you've inferred and proceed (present-the-plan-and-go), rather than re-running the conversation the partner already had. Reserve the full interview for a cold, vague direct invocation.

## Step 5: Write the research note

**Hand-off branch — source is already a research note.** If the "source" is itself an existing `{research}/...` note handed over by another partner (the Researcher's hand-off payload names a `note` path), do **not** create a research-note-of-a-research-note. Use the handed note as the research artifact and go straight to Step 6 (the wiki update), citing that note as the source. The log entry records the hand-off rather than a fresh research note. Only create a new research note when ingesting a genuine external source.

Otherwise, create `{research}/YYYY-MM-DD-HHmmss-<slug>.md` (`<slug>` is a 3–5 word kebab-case title). This is the dated snapshot of *what this source said* — the scratchpad, not the product.

```yaml
---
type: research
created: YYYY-MM-DD
title: <human-readable title>
author: agent
trust: raw
topic:                             # YAML list, general → specific, lowercase
  - <broad domain>
  - <narrower facet>
status: complete
sources:
  - <source filename or URL>
---
```

Sections: **Summary** (2–4 paragraphs of your own analysis — what it *means* and how it connects, flagging uncertain or contradicting claims), **Key Points** (discrete facts/arguments), **Connections** (`[[wikilinks]]` to related pages with a note on each relationship), **Open Questions**, **Source** (full citation/path).

## Step 6: Update the wiki

Read `{index}` first — it tells you what pages exist. The wiki is the living product: long-lived, multi-source reference pages, one canonical page per concept. For each concept the source touches, decide: update an existing page (new info, nuance, contradiction, refinement), create a new page (significant, recurring, ≥3–4 substantive points), or skip (mentioned only in passing).

**Near-duplicate check before creating a page (required).** List existing slugs (`ls {wiki}`) and compare the *concept*, not just the slug string, against existing pages — leading noun, synonyms (`coaching-tree` vs `coaching-lineage`), and topic overlap all count. Creating near-duplicate pages is the most common way the wiki drifts.

- If an existing page already covers the concept → **update it**, don't splinter.
- If the source reveals that two existing pages have **drifted into near-duplicates** and should be one → fold the merge in here, under `{conventions}/wiki-consolidation.md` (choose primary vs subsumed, merge under supersession discipline, archive the subsumed page to `{archive}/_agent/wiki/`, name the merge in the log entry). This is where the retired consolidate operation re-homes.
- If genuinely distinct → create the new page.

Wiki page frontmatter (kebab-case filename, no datetime prefix):

```yaml
---
type: wiki
created: <date first created>      # immutable; keep the original on update
last_updated: YYYY-MM-DD           # set to today on every substantive edit
title: <human-readable title>
author: agent
trust: raw
summary: "<one-line scope, ≤160 chars>"
category: <one index H2 — see {index}; MUST match an existing heading>
topic:                             # YAML list, general → specific, lowercase
  - <broad domain>
  - <narrower facet>
status: in-progress
sources:
  - <every source that has contributed>
review_after: YYYY-MM-DD           # OPTIONAL — only if the content is time-sensitive; a resolved date, never a duration
---
```

If the content is **time-sensitive** (pricing, versioned tools, event timelines, dosing/market state), set `review_after:` to a resolved date — absence = evergreen, so omit it everywhere else (semantics: `{conventions}/frontmatter.md`).

`summary:`, `category:`, and `topic:` are the Bases-surfaced fields (see `{conventions}/frontmatter.md`): `summary` is the ≤160-char scope, `category` is a **single** value that **must equal an existing `{index}` H2** (the grouping key — if no category fits, the page needs a new index category, a structural index edit), and `topic` is a lowercase general→specific list for cross-cutting filtering. Never invent a `category` outside the index H2 set.

Sections: **Overview** (synthesis across all contributing sources — reads like an encyclopedia entry, flags uncertainty), **Key Facts / Claims** (each with its source), **Connections** (`[[wikilinks]]`), **Contradictions / Open Questions**, **Sources**. When updating, weave new information in — don't append — and bump `last_updated`.

**Supersession (required).** Whenever the source updates, contradicts, refines, or retracts an existing claim, apply the `[!superseded]` / `[!stale]` / page-level patterns from `{conventions}/wiki-supersession.md`. Never silently overwrite; document both sides of a genuine, unresolved contradiction rather than picking a winner.

**Cross-source contradiction summary.** If this one source contradicts claims across **several** pages, surface that as a single systemic observation ("this source challenges the prevailing view on X across N pages") rather than patching each page in isolation — the pattern is the signal.

## Step 7: Update the index

After writing pages, update `{index}` **per `{conventions}/wiki-index.md`** (the index-structure convention): add each new page as a **structural row** `- [[page]] · <optional structural tag>` under the right `##` category — **no description, no source count, no date** (those live in frontmatter / the `{log}`, surfaced via Bases). Nest entity pages under their hub; create/adjust categories as the wiki grows. The page's `category:` frontmatter **must equal the H2 you file it under** — they are one controlled vocabulary; if you add or rename a category here, rewrite the `category:` of every affected page in the same pass. Move any stub that now has a real page out of `## Stubs` into its category, and bump the index `last_updated`. Read that convention if unsure of the row format or category model — it is the single source for index structure.

## Step 8: Append to the log

Append one partner-tagged entry to `{log}`:

```
## [YYYY-MM-DD HH:MM] ingest (<partner>) | "<Source Title>" → research: [[<research-note>]], wiki: [[<page>]] (new), [[<page>]] (updated)
```

Prefix new pages with `(new)`, updated ones with `(updated)`. If a merge happened, name it: `merged: [[{archive}/_agent/wiki/<subsumed>]] → [[<retained>]]`. Omit the wiki clause if no pages changed. **Write no session note** — the summoning partner owns the session log for the whole sitting (operating contract § session-ownership).

## Step 9: Verify and attest

Run the **tier-1 checklist** from `{conventions}/write-verification.md` on every file you created or updated — that file is the checklist's single home; read it, don't re-derive it from memory. **Fail-open:** fix what you can, flag what you can't, always complete the write. Then write the attestation on every page created or updated: `verified_by: vlt-ingest`, `verified_at: <today>` (fields + freshness rule: `{conventions}/frontmatter.md`).

One ingest-specific check rides along:

- [ ] `review_after` present **iff** the content is time-sensitive — and a resolved date, not a duration

Report the result (what was created/updated, and "verification passed" or the specific gaps flagged).

## Tips

- **Contradictions are gold.** They're where the interesting intellectual work happens — surface them, don't smooth them over.
- **Think cross-reference first.** The value of a wiki is the connections. After writing anything, ask what else should link here.
- **Quality over breadth.** Three pages touched well beats ten touched superficially.
