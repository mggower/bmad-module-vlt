# vlt-dispatch — reference: Mode `ledger`

Read on entering `ledger` mode (router: `SKILL.md`, Mode dispatch). Read-only; writes no `{log}` entry (router: Log).

## Mode: `ledger` — the read-only open board

A **read-only** view: grep the *whole* record for still-open items and group them by partner, across **both** daily and relay traffic. No write, no `daily/` read — pure report. This is the human's **standing signal**: a partner only drains its slice when next summoned, so an item routed to a rarely-summoned partner could sit open, unseen, indefinitely; `ledger` shows the full open backlog without summoning anyone.

Build it:

1. Count all open items: `grep -c '^- \[ \]' _agent/dispatch.md`.
2. Per live slug, count open: `grep -cF '[ ] \`<slug>\`' _agent/dispatch.md`, and find the oldest (the earliest run header above an open line).
3. Present grouped by partner, oldest-first signal:

> **Still open across the record:** Researcher 3 (oldest 2026-05-21) · Librarian 1 · Creative 2 *(1 relayed: a spec)*. Summon a partner to drain its column.

If everything is picked up, say "all routed items have been picked up — nothing open." The ledger holds **only partner-owned work** — every open item belongs to someone who can drain it (no-owner captures were flagged in their run report, never recorded), so the board stays an honest signal of real waiting work, not a graveyard.

`ledger` is also printed **inline at the end of a `daily` run** (Step 3) — same board, two surfaces: `daily` closes with it, `ledger` serves it on demand.

### Pointer integrity — every relay pointer resolves a key

After the board, check the rail: for every pointer in a `relay:` block, **resolve its key** — a `handoff-path` that exists on disk, or a `ref` present in the block header (`(ask: <ref>)` / `(answer: <ref>)`). Scope: `relay:` blocks **only** — a `consult:` block is pre-checked traffic, and a `daily` pointer keys on its watermark. Render:

- **Findings** — a *shape-annotated* pointer that fails its shape's key requirement: an `ask`/`answer` with no `ref`, or an annotated `handoff` with no path on disk. The finding's legal response: **the publishing partner re-fires the relay correctly keyed; the recipient checks the malformed line off as superseded** (its own tagged line — two-writer discipline holds). *(Known-incomplete: for an unsolicited delivery whose payload is written inline, no correct key exists to re-fire with — this class's response is pending the delivery-shape build. Interim posture: drain the finding normally; no re-fire is expected of anyone.)*
- **The legacy line** — un-annotated **pathless** pointers are legacy pre-shape traffic (exempt from the key check by design; see `references/relay.md`, *Backward compatibility*). Report them as a **denominated count**, never as findings: "N legacy unkeyed pointers (pre-shape)" — zero renders as the denominated zero, matching the wires idiom below.

This is the read-side bell for the failure that cannot be seen by reading a single block: an unkeyed pointer disables the spam guard invisibly.

**Group open items by `blocked:` facet where tagged** (the optional inline facet on backlog items and pointer lines — `blocked: user-decision | partner-bandwidth | external-event YYYY-MM-DD`, per `{conventions}/frontmatter.md`'s backlog schema): render `user-decision` first as the owner's question list, then the other facets; untagged rows are their own bucket (absence = untagged; never infer a facet). Where `(for: <principal>)` facets are present, additionally annotate the per-partner counts by principal (e.g. "Researcher 3 — 2 for `{principal-slug}`") and render un-faceted items as the default principal's — absence = default, never infer. The pointer-integrity check is unchanged (a key is a path or a `ref`; the principal widens the key's *pair*, not its *presence*).

### Tripped wires & vitals

After the open board, run the vitals reader — `{root}/.claude/hooks/vlt-vitals.py` (default mode) — and render:

- **Tripped wires** — one row per **tripped** wire: wire id, current value vs threshold, owner slug, its `surface_text`. A reader failure renders as a **warning row** (`⚠ vitals unavailable: <reason>`) — never omitted, never faked green. No tripped wires → one line **with the wire count checked**: "0 of 2 wires tripped" (a denominated zero, per the operating contract's *Honest reporting* — cited, not re-worded).
- **Display-only vitals block** (pull, not push — everything beyond the strip's tripped-wires line is pull-budgeted): `days_since_lint`, the denominated `classifier_streak` line exactly as the reader renders it (count, denominator, and unreadable-count in the same breath), `expired_pages`, and the size vitals (`{log}` / `{backlog}` / `{index}` / per-partner memory bytes). Display only — nothing here trips or nags.

### Verify

After writing, re-read what you produced and confirm:

- **Nothing was written** — read-only. The counts match a fresh grep of open items; the board groups only live, partner-owned slugs.
- **The pointer-integrity line agrees with a fresh grep of `relay:` blocks** — every finding is a shape-annotated key failure; the legacy count matches the un-annotated pathless pointers actually present.
- **The rendered wires match a fresh vitals run** — re-run the reader; every tripped row (or the denominated zero, or the warning row) agrees with it.

Report the result; fix any gap before closing.
