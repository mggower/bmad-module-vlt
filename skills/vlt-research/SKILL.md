---
name: vlt-research
depends_on: ["frontmatter@4", "write-verification@1"]
description: Investigate a question against the web and file a standalone research note. Use when the user wants to actively build new knowledge — 'research X', 'deep dive into Y', 'what's the current state of Z', 'get me up to speed on…', or any request to go learn something the vault doesn't yet hold. For a source already captured in the vault, use vlt-ingest; to synthesize what's already filed, use vlt-query.
---

# vlt-research

## Overview

vlt-research goes *out into the world* to build new knowledge on a question and files the result as a standalone research note — the permanent artifact this skill produces. It is the Researcher's main tool. (Contrast: `vlt-query` synthesizes what's already filed; `vlt-ingest` files a source the user brought in.) The wiki pass is a separate, offered step — and it flows through the Librarian, never written here. Runs interactively (the interview sharpens the brief) or headless ("research X").

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the module isn't set up (no `vlt` config or `_meta` governance in this project), tell the user `vlt-setup` can configure it.

The vault is this project — resolve paths relative to `{project-root}` through the `vault_structure` map (override wins, else the shipped default). Logical names used (default, relative to the project root): `index` → `_agent/wiki/index.md`, `wiki` → `_agent/wiki/`, `research` → `_agent/research/`, `log` → `_agent/log.md`, `conventions` → `_meta/conventions/`, `overlays` → `_agent/conventions/` (vault-local convention overlays). Below, `{research}` etc. mean the resolved path. Note the **active partner** for the log tag.

**Web access is host-provided.** Reach the web with whatever web tooling the host project supplies (an MCP connector it mandates, or native fetch/search). Don't hardcode a specific tool; if the host forbids one, honor that.

## Phase 1: Brief and feasibility gate

Sharpen the research brief through a short conversation (read the user's message first; ask only what isn't already clear, in 2–3 natural exchanges — not a numbered list):

- **The precise question** — vague topics produce vague research. Push for a formulation that could title a research note ("how do transformer attention mechanisms work, conceptually?", not "AI").
- **The angle** — practical vs theoretical, historical vs current, or a specific decision it informs.
- **The depth** — offer a concrete choice: *quick orientation* (lay of the land), *moderate investigation* (key debates, multiple perspectives), or *deep dive* (thorough, contradictions surfaced, open questions documented).
- **Seeds** — starting links, papers, or people.

**Feasibility gate (before committing effort):** confirm the question is actually researchable against the open web at the chosen depth — not too broad to converge, not dependent on sources you can't reach, not a moving target with no stable answer. If it's mis-scoped, propose a tighter question or a different depth and reconfirm before proceeding. Don't burn a deep dive on an unanswerable prompt.

**Partner-fronted mode.** If you were invoked downstream of a partner (the Researcher) that already sharpened the brief in conversation — you arrive with a precise question and depth, or a hand-off payload — treat Phase 1 as **satisfied**: state the question and depth you've inferred, run the feasibility sanity-check silently, and proceed. Reserve the full interview for a cold, vague direct invocation ("research X" with no partner context).

## Phase 2: Vault check

Before going to the web, check what the vault already knows — don't rediscover what's filed, and let the gaps shape what the research adds. Read `{index}`, then the directly relevant `{wiki}` pages and any germane `{research}` notes. Surface it briefly: "The vault already has [X]; this will focus on [Y]."

If the vault is **thin or empty** on the topic, say so — and ask whether these findings should **feed the wiki** (handed to the Librarian afterward) rather than just rest as a standalone note. A topic worth researching from scratch is often one the wiki should grow a page for.

## Phase 3: Research

Go research, calibrating effort to the agreed depth:

- **Quick orientation** — 3–5 searches, 3–5 sources; overviews and authoritative summaries.
- **Moderate investigation** — 5–10 searches, 5–8 sources; primary sources alongside overviews; cover the main positions.
- **Deep dive** — 10+ searches, 8–15+ sources; follow citations, seek primary and dissenting sources, look for what's contested.

As you go: **synthesize across sources** rather than reporting each one; note where they agree, disagree, or hedge (disagreement is the interesting part); **flag anything that updates or contradicts the vault** (high-value); treat a source's contribution as input to the synthesis, recording substantial ones in the sources list without full ingest ceremony.

**Checkpoint by interruption-risk, not call-count.** The `.WIP` file exists to survive an interruption mid-dive — so write/refresh it whenever there's real state that losing would hurt: before a long or batched run of calls, and whenever you pause with work still open. Maintain `{research}/YYYY-MM-DD-HHmmss-<slug>.WIP.md` with **Progress** (sub-questions done / remaining), **Sources collected** (URL + one-line contribution), **Open threads** (what you're chasing). A dive that completes in a single uninterrupted pass needs no separate checkpoint — the note itself is the artifact; don't perform the ceremony for its own sake. On completion, drop the `.WIP` suffix — it becomes the note in Phase 4.

## Phase 4: Write the research note

Before writing, **don't carry any secret into the note** — if a fetched source exposes a credential or private token, leave it out (record only what the investigation needs).

Write `{research}/YYYY-MM-DD-HHmmss-<slug>.md` (slug = 3–5 words from the *question*, not just the topic).

```yaml
---
type: research
created: YYYY-MM-DD
title: <the research question, not just the topic>
author: agent
trust: raw
topic:                             # YAML list, general → specific, lowercase
  - <broad domain>
  - <narrower facet>
status: complete
sources:
  - <url or citation for each source consulted>
revisit_after: YYYY-MM-DD          # OPTIONAL — graduation-candidacy recheck date; absence = not a candidate (see frontmatter.md)
---
```

Structure (no `key:` field):

- **Research Question** — the precise question, one or two sentences; this is what "done" means.
- **Scope & Approach** — depth, angle, what was out of scope.
- **Executive Summary** — 3–5 dense, specific sentences (the key answer, the most important finding, the biggest caveat). Written last, placed first — it's what the user reads when they return in six months.
- **Findings** — organized by theme / sub-question, **not by source**; each section synthesizes across sources.
- **Open Questions** — what's uncertain or contested; name the tension, not "more research needed".
- **Sources** — annotated; each with one line on what it contributed. Every URL you actually used appears here.

## Phase 5: Verify and attest

Run the **tier-1 checklist** from `{conventions}/write-verification.md` on the note — that file is the checklist's single home; read it, don't re-derive it from memory (read it together with its `{overlays}/write-verification.overlay.md` if present, honoring the overlay's appended rules). **Fail-open:** fix what you can, flag what you can't, always complete the write. Then attest the note you created: `verified_by: vlt-research`, `verified_at: <today>` (fields + freshness rule: `{conventions}/frontmatter.md`, together with its `{overlays}/frontmatter.overlay.md` if present).

Report the result with the headline finding, and "verification passed" or the specific gaps flagged — before logging.

## Phase 6: Log and close

Append a partner-tagged entry to `{log}`:

```
## [YYYY-MM-DD HH:MM] research (<partner>) | "<question summary>" → [[<research-note>]]
```

Write **no** session note — the summoning partner owns the session log (operating contract § session-ownership). Then report: the headline finding, what was filed and where, the verification result, and **offer the wiki pass** —

> "Want these findings folded into the wiki? I'll hand the note to the Librarian (`vlt-ingest`) to integrate it canonically — or you can review the note first."

If taken, hand off with the **structured payload** (operating contract § Sessions, sittings, and hand-offs), not freeform prose: `note` (this research-note path), `concepts` (the target concept[s] it should affect), `supersession` (any existing claims it updates/contradicts, each with a one-line why), `prefs` (any user/tool preferences to forward). Convey *what changed and what it complicates*; leave the filing mechanism to the Librarian. The wiki update is never done here (the Librarian is the single writer of canonical pages); vlt-research only hands off. For a large deep-dive note, you may also offer an HTML rendering if the host has a renderer — otherwise skip it.

## Tips

- **A sharp question is half the work.** Time spent in Phase 1 is repaid in Phase 3.
- **Disagreement beats consensus.** Where sources conflict, that's the finding — surface it, don't average it away.
- **The note is the deliverable, not the draft.** Verify before logging; an unverified note isn't done.
