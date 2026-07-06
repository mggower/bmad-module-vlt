---
name: vlt-{op}
description: {5-8 word summary of what the operation does}. {Use-when trigger phrases the user would actually say.}
---

# vlt-{op}

## Overview

{What this operation does, how it works, the outcome it produces, and which partner(s) reach for it. One tight paragraph. If it diverges from a blanket rule — e.g. no web access — say so here.}

## On Activation

Load config from `{project-root}/_bmad/config.yaml` and `{project-root}/_bmad/config.user.yaml` (root level and the `vlt` section). If the `vlt` config is missing, tell the user `vlt-setup` can configure the module, then ask for a vault root to proceed.

The vault is this project — resolve every path relative to `{project-root}` through the `vault_structure` map materialized in `config.yaml` (override wins, else the shipped default). List only the logical names this operation uses, with their defaults — e.g. `index` → `_agent/wiki/index.md`, `wiki` → `_agent/wiki/`, `log` → `_agent/log.md`, `conventions` → `_meta/conventions/`. Below, `{index}` etc. mean the resolved path. Note the **active partner** for the log tag.

{If the operation writes notes derived from external content, add: scan that content for secrets before writing — never write a credential into a derived note.}

Before writing anything, JIT-read the governance conventions this operation obeys from `{conventions}` (at minimum `frontmatter.md`; add `wiki-supersession.md` / `wiki-consolidation.md` / `extraction.md` as relevant).

## {Named steps — the operation flow}

{The operation's stages as named sections, outcome-driven where the LLM is fluent, exact where fragile (paths, frontmatter schema, log format). Honor the conventions; respect the single-writer rule — only the Librarian writes canonical wiki pages, so route any canonical-page write through a hand-off rather than writing it here unless this operation IS the writer.}

Frontmatter for any note written follows `{conventions}/frontmatter.md`: **no `key:` field**; `created` (immutable) + `last_updated` only on continuously-updated types (wiki pages, index, re-extracted PARA); written-once notes (research, sessions) carry only `created`.

## Enforcement

{The boundary classifier — answer at mint time: **does this operation create a rule someone else must obey?**
 If NO: replace this section's body with one recorded line — `non-boundary: <why>` — and move on (keep honest small mints fast).
 If YES: declare the bell — who checks / at what moment / against which counter (an enforcement-kit metric id, once that vocabulary exists) — or carry a complete tripwired deferral (`deferral_metric` + `deferral_threshold` + `review_after`, all three), per `{conventions}/frontmatter.md` *Enforcement declaration*.}

## Log

Append one partner-tagged entry to `{log}` in the operating-contract format:

```
## [YYYY-MM-DD HH:MM] {op} (<partner>) | <summary> [→ <artifacts>]
```

Write **no** session note — the summoning partner owns the single session note for the sitting (operating contract § session-ownership).

## Verify

{If the operation writes, re-read what it produced and confirm against a short checklist — frontmatter complete and correct (no `key:`), citations/links resolve, the `{log}` entry was appended and is partner-tagged. Report the result; fix gaps before closing.}
