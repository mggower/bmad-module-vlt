# vlt-dispatch — reference: Mode `daily`

Read on entering `daily` mode (router: `SKILL.md`, Mode dispatch).

## Mode: `daily` — scan the human capture stream

The original behavior, now named and behind an explicit subcommand. **Only this mode reads `daily/`.**

### Step 0: Determine scope

Like `vlt-lint`, pick one scope at the top of the run and announce it (with the file count, e.g. "Scoped dispatch — 3 daily notes with new content since last run"). The per-source **watermark** in `_agent/dispatch.md` is the baseline — read that file first, building `watermark[file]` = the `routed through line N` recorded in each file's most recent `daily/` run header (a never-dispatched note has watermark 0; **relay and consult blocks carry no watermark and are ignored here** — only a `daily/…` header is parsed for `routed through line N`).

**Scoped (default)** — every daily note with content **beyond its watermark**. Glob `daily/*.md`, and for each compare current line count to `watermark[file]`; include every note with new lines (on the first scoped run, the entire backlog of never-dispatched notes; thereafter only what's been appended). Process only the lines beyond each note's watermark; a run with nothing new anywhere routes nothing (report "nothing new since the last dispatch").

**Where a routing profile declares principals** (`SKILL.md`, *the routing profile*), the scan covers **each declared capture stream** — glob each principal's stream the same way (`daily/*.md` stays the default principal's); the watermark machinery is already per-source, so per-stream watermarks need no new mechanics. With no profile, this paragraph is inert.

**Full** — only when the user says "full dispatch" / "dispatch everything" / `--full`: re-route **every** `daily/*.md` from line 0, ignoring watermarks. Use after a format change or to rebuild the record. (Re-routing writes fresh open items; it does not resurrect items a partner already checked off in a prior block — those stay as their own historical blocks.)

**A named date or range** — "dispatch the 10th" / "this week's notes" / "today" → resolve to the matching `daily/YYYY-MM-DD.md` file(s) and process each beyond its watermark (or from line 0 if the user says "re-dispatch").

If a resolved note doesn't exist, say so plainly and skip it — don't invent content. If a daily note was edited *above* a watermark (rare — the human's prerogative), the line offset may be stale; if the content clearly doesn't line up, note it and offer a full re-dispatch of that file rather than guessing.

### Step 1: Classify against the live roster

Build the domain map from the **live roster**, not a hardcoded list — read the installed `vlt-agent-*` skills under `{project-root}/.claude/skills/` and use each partner's `description` to know which domain it serves (Researcher → open questions worth investigating; Creative → ideas worth making; Librarian → vault/knowledge-meta; plus any domain partners the roster has grown). Deriving the map live means dispatch stays correct as the roster grows — a newly minted partner's domain is routable the next run with no edit here.

**The routing slug is the skill basename minus `vlt-agent-`** — `vlt-agent-researcher` → `researcher`, `vlt-agent-creative` → `creative`, `vlt-agent-librarian` → `librarian`. This is the greppable key on every pointer line. Deriving it mechanically (not from a hand-chosen domain word) means a partner's grep is stable and exact, and a newly minted partner is routable with zero edits here — the slug *is* its identity. Pair it with the partner's human name (from its `description`) for legibility.

**Segment, then route.** Transcribed voice memos run together, so segment by **intent, not punctuation**: a fragment is one coherent thought/memo/ask, and a single `daily/` paragraph often holds two. Split on topic shifts; don't let a paragraph break decide a fragment for you. For each fragment:

- **One owner (common)** — assign the single partner whose domain it most serves → one pointer line with that slug.
- **A captured source or link → the Librarian.** A saved article, URL, or "read this" is *material*, not a question — it belongs to the Librarian's ingest queue (`librarian`), never the Researcher. Hold the line: the **Researcher** gets open *questions worth investigating*; the **Librarian** gets *sources and material to file*. A daily fragment that is just a saved link, or a "to-do: ingest X," routes to `librarian`.
- **Genuinely two domains** — a fragment that materially serves two partners is **cross-routed**: emit one pointer line per partner, each independently checkable, each gist framed for that partner. Don't over-split — only when each partner would actually act on it.
- **No owner → flag and skip (write no pointer).** A stray idea, reminder, shopping list, order, social observation, or to-do that fits no partner has **no home in the vault** — do **not** write it a pointer. A persistent no-owner pointer would sit open in the ledger forever, never drained — that accumulation is the very clutter dispatch exists to prevent. Instead, **surface it once in the run report** (Report → *Flagged and skipped*) and move on; nothing is written to `_agent/dispatch.md` for it.

### Step 2: Write the routing record

Append one **`daily` run block** per in-scope source to `_agent/dispatch.md` (create the file with the header below if absent). **Dispatch's only write is appending blocks with every item open** — it never flips a status. Format — a greppable run header (the **header shape is the mode signal**) plus one checkable pointer line per routed fragment:

```
## [YYYY-MM-DD HH:MM] daily/YYYY-MM-DD (routed through line N) — K item(s)
- [ ] `slug` Partner Name — one-line gist of the fragment, in the user's own framing → [[daily/YYYY-MM-DD]]
```

Only **owned** fragments get a pointer line. A no-owner fragment is flagged in the run report and written nowhere; the header's `K item(s)` counts only the pointers actually written. A pointer line **may** optionally carry the `blocked:` triage facet in a paren after the gist (`(blocked: user-decision | partner-bandwidth | external-event YYYY-MM-DD)` — the backlog facet in `{conventions}/frontmatter.md`, referenced not redefined); absence = untagged, and `ledger` groups by it. A pointer routed from a non-default principal's stream carries that principal's facet — `(for: <principal-slug>)` — so the draining partner knows whose capture it serves and whose thread the answer belongs to; default-stream pointers stay un-faceted (byte-identical single-user output).

Rules for the block:

- The **run header** carries the watermark: `routed through line N` = the source file's line count at this run (what the next run's watermark check reads). The `daily/…` shape *is* the mode signal — it tells the next `daily` run (and a human scanning) that this block uses watermark idempotency. It omits the `dispatch (librarian)` type/partner prefix — every line here would carry it, so it's pure boilerplate. (The `{log}` entry keeps `dispatch (librarian)` — that's a mixed stream where the tag is load-bearing.)
- Every pointer is a **checkbox written open (`- [ ]`)**. After the box comes the **routing slug in backticks** — the partner's skill basename minus `vlt-agent-` — the greppable key, followed by the human Partner Name. The backtick-wrapped slug makes a partner's grep exact and collision-free: `grep -nF '[ ] \`researcher\`' _agent/dispatch.md` returns only its open items. Every pointer carries a live partner slug — there is no domain-less pointer.
- The **gist** is a faithful one-line compression of the fragment in the user's framing — enough for the partner to know what's waiting and decide. It is a *pointer*, not an extraction: the `[[daily/…]]` wikilink sends the partner to the full memo. Do not interpret, grade, or fold the memo into anything here — that is the receiving partner's job (and preserves the personalization firewall).
- A **cross-routed** fragment gets one pointer line per partner (each its own checkbox).
- If multiple daily notes are in scope, write one run block per source file.

The file's header (written once, on creation):

```
# Dispatch

_The vault's partner communication bus — one routing record with a drain, read through four modes. `daily` routes human daily-note captures to the partner whose domain they serve; `relay` appends pre-addressed partner→partner pointers (a handoff doc, or a doc-less ask/answer/deliver); `consult` records a synchronous partner→partner question already answered; `ledger` is the read-only open-items board. Every routed pointer is written open (`- [ ]`); a partner greps its `` `slug` `` for open items and checks off (`- [x]`) what it picks up. A `consult` pointer is written already checked — it never waited. Never edits daily notes; never auto-ingests. Idempotency is per-source watermark for `daily`, the pointer's key (doc path or ref, per recipient pair) for `relay`; the open/picked-up status makes the backlog self-reporting._
```

`_agent/dispatch.md` is a log-style agent record (like `{log}`), not a "note" — it carries **no per-note frontmatter** (a `vlt-decay` drain leaves at most a one-line breadcrumb beneath the title — still no frontmatter).

### Step 3: Report (and print the standing ledger inline)

Lead with the **scope you ran** (scope + how many notes), then what was routed, grouped by partner, and **name who to summon** — `daily` mode ends at the routing record + this report; it does not summon partners or move fragments into anyone's working record. Example:

> Scoped dispatch — 3 daily notes with new content since the last run. Routed 4 open items:
> - **Researcher** (2) — a question on transformer attention; a thread to chase on context-window pricing.
> - **Librarian** (1) — a saved article to ingest.
> - **Creative** (1) — cross-routed: an idea worth making.
>
> Summon each partner to drain theirs (each greps its `` `slug` `` for open items and checks them off). Nothing was written into your daily notes or the wiki.

If there were no new fragments anywhere in scope, say "nothing new since the last dispatch."

**Flagged and skipped (no-owner fragments).** When a fragment had no partner home, list it here — a one-time surface so nothing is silently dropped — and say plainly it was **not** written to the record (it lives in the daily note; place it yourself if you want it somewhere). This is the *only* trace a no-owner fragment leaves. Example:

> **Flagged, not routed (2):** a personal reminder; a shopping list. No vault home — left in your daily note, nothing written to the record.

**Then print the standing open ledger inline** (not just this run's routes). A `daily` run is a natural moment to show the human the whole open backlog — so after routing, run the **`ledger` read** (`references/ledger.md`) and append it to the report. This inline ledger and the standalone `ledger` mode are the **same board**; `daily` prints it as the closing signal of a routing run, `ledger` serves it on demand without scanning `daily/`.

### Log line

The mode's `{log}` entry (router: Log):

```
## [YYYY-MM-DD HH:MM] dispatch (librarian) | daily <scope>: <N> fragment(s) from <M> daily note(s) routed to <partners> [→ [[_agent/dispatch.md]]]
```

### Verify

After writing, re-read what you produced and confirm:

- `_agent/dispatch.md` gained exactly one `daily/…` run block per in-scope source, each with a valid `routed through line N` watermark and one pointer line per routed fragment.
- **Every new pointer is written open** (`- [ ]`); dispatch flipped no status and touched no prior block.
- **No file under `daily/` was modified** and **nothing was written to the wiki**.
- Every pointer resolves: `- [ ]` + a backtick `` `slug` `` matching a live `vlt-agent-{slug}` + a `[[daily/…]]` link to a real file. No domain-less slug.
- The `{log}` entry was appended, tagged `(librarian)`. No secret in a pointer.

Report the result; fix any gap before closing.
