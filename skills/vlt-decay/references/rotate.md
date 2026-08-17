# vlt-decay — reference: `rotate` (the `{log}`)

Read on entering the rotate verb (router: `SKILL.md`, The verbs). Every act obeys the operating contract's *Hygiene and grooming — the safety model* — cited, not restated.

## The cut point — content-derived, idempotent

The cut is **every entry strictly before the newest `lint` header** in `{log}` — found by the same grep `vlt-lint` Step 0 uses:

```bash
grep -n "^## \[.*\] lint" {log} | tail -1
```

Everything from the file's first entry header up to (not including) that `lint` header line is the **cut prefix**; the newest `lint` header and every entry after it are the **live tail** and never move. Re-running rotate immediately after finds nothing before the newest `lint` header — a said-out-loud no-op, files byte-identical. No stored counter, no ledger: the cut point derives from content, so progress state needs none.

**Refuse loudly when no `lint` header exists** — say: *"never linted — run `vlt-lint` first; rotation has no safe cut."* The whole file is then `ingests_since_lint`'s derivation window and any cut would silently corrupt the count into its every-ingest-counts fallback. Nothing moves.

## The move

1. **Append** the cut prefix to `{archive}/_agent/log.md` (create it, with a `# Log (archive)` title line, if absent) — the `{archive}`-mirrored path, per the contract's archive-structure rule. Chronological order preserved: the archive is older-first, and **archive + live tail concatenate to the pre-rotation record byte-for-byte** (breadcrumb aside). Content moves whole and unedited.
2. **Cut** the prefix from the live `{log}`, leaving the file title, the breadcrumb, and the live tail.
3. **Write/update the one breadcrumb line** beneath the live file's title, updated in place (never an appended series):

   ```
   > rotated through [YYYY-MM-DD HH:MM] → {archive}/_agent/log.md
   ```

   where the timestamp is the newest archived entry's header timestamp. No frontmatter is added — `{log}` carries none by design.
4. **Commit** — cut + archive append in one commit.
5. Report what moved (entries, lines, bytes) and append the `decay` log line (router: Ending the run).

## Reader invariants (the verb's own contract — hold every one)

- **`ingests_since_lint` / `days_since_lint`** (the vitals reader) derive from the newest `lint` header and the entries after it — the live tail retains both, so the derivations are byte-for-byte unchanged. The never-linted refusal covers the no-baseline case.
- **`vlt-lint` Step 0's scoped baseline** (the grep above) reads the newest `lint` header — it survives every rotation, so scoped mode's baseline is identical pre/post and rotation never manufactures a full-mode fallback.
- **`log_bytes` drops by design** — vitals measure wake-read mass; the archived sibling is excluded (the metric's own definition says so).
- **The whole record stays derivable** — any reader that genuinely needs pre-rotation history reads the archive sibling; concatenation reproduces the full record.
