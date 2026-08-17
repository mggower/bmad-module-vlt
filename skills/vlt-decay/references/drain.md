# vlt-decay — reference: `drain` (the dispatch board + the backlog)

Read on entering the drain verb (router: `SKILL.md`, The verbs). Every act obeys the operating contract's *Hygiene and grooming — the safety model* — cited, not restated. One invocation may run both drains below; report what moved per file.

## Dispatch drain — `_agent/dispatch.md`

**Eligibility — a run block is drain-eligible iff ALL of:**

1. it is a `daily/…` or **`relay`** block — **`consult:` blocks are permanently drain-exempt** (tiny by construction; their evidentiary window is unbounded — the consult-precondition check compares them against specs of any age, so retaining them is the derivability clause's retained-tail leg, at a cost that rounds to nothing);
2. **every** pointer line in it is checked (`- [x]`) — an open row anywhere keeps the whole block live;
3. it is **not** the newest `daily/<source>` block for its capture source (per principal stream) — that block carries the source's `routed through line N` watermark, and removing it would reset the watermark to 0 and re-route the entire note as duplicate open items;
4. its run-header date is older than **45 days** (mirroring the `drain-due` wire, so a performed drain always clears the wire it answers).

**The move:** eligible blocks move **whole** — header + every row travel together, never a row out from under its header — **appended** in file order to `{archive}/_agent/dispatch.md` (create it, with a `# Dispatch (archive)` title line, if absent). Content moves unedited. Then write/update the one breadcrumb line beneath the live file's title, in place:

```
> drained through [YYYY-MM-DD HH:MM] → {archive}/_agent/dispatch.md
```

Still no frontmatter — the record stays a log-style agent file. Nothing eligible → a said-out-loud no-op; a second drain immediately after is one by construction.

## Backlog drain — `{backlog}`

Move **all** `- [x]` items out of `## Done` (resolved is terminal, per the backlog schema), with their `[resolved: <how>]` tails intact, appended under a `## Done` heading in `{archive}/_agent/backlog.md` (create it, with a `# Backlog (archive)` title line, if absent). **The `## Done` section heading stays** in the live file (the schema's shape holds); **`## Open` is never touched — byte-identical.** Write/update the live file's breadcrumb line beneath the title, same form as above with the backlog's archive path.

## Commit and log

One commit per invocation — the live-file cuts and the archive appends together. Then the `decay` log line (router: Ending the run), naming what moved per file in lines/bytes.

## Reader invariants (the verb's own contract — hold every one)

- **`open_pointers` / `oldest_open_pointer_days`** (the vitals reader) and **the ledger's whole-record greps** (total + per-slug `[ ] \`slug\``) count open rows — a drain moves only fully-closed blocks, whole, so zero `[ ]` rows move and both counts are identical pre/post.
- **The ledger's pointer-integrity findings** live only in open or terminal checked-off lines; a drained block is fully closed, so no actionable finding leaves the board. The two **legacy lanes are live-record counts** — a drain re-baselines them downward by design (`vlt-dispatch`'s ledger reference states it).
- **The `daily` watermark baseline** reads each source's most recent `daily/…` header — protected by eligibility rule 3, even when that block is fully closed and old. This is the single most load-bearing invariant of the verb.
- **Relay idempotency** greps `(key, to-slug, principal)`: blocks with an open pointer never drain (rule 2), so the no-op guard's evidence stays; draining a *checked* latest pointer changes the ladder's input from "checked → append fresh open pointer" to "absent → append fresh open pointer" — the same behavior.
- **`spec_candidate`'s relay count and decline read** (`vlt-lint`) and **the proto-spec retrofit's relay count** (`vlt-upgrade`) read the live record **and its `{archive}`-mirrored sibling** — widened in the same build as this verb, so a drain never resets a candidacy signal.
- **The consult-precondition check** needs no widening: consult blocks never drain (rule 1).
- **`## Open` consumers** (partner activation reads, mint's capability-gap filter, `backlog_bytes`'s live-only definition) are untouched by construction.
