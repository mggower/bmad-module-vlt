# GitHub intake — the factory's read of the remote feedback rail

Discovery's carved half for remote filings: how an owner-admitted GitHub issue becomes an
ordinary inbox filing. Self-contained — do not assume SKILL.md is in context. Every shape
here (payload fields, labels, `origin:` header, contract version) is single-homed at
`skills/vlt-feedback/references/field-contract.md` — this file carries **mechanics only**
and cites the contract for every shape; it restates none of them.

The transport repo `<repo>` is `feedback_repo.default` from
`skills/vlt-setup/assets/module.yaml` (an `OWNER/REPO` slug for `gh --repo`; the factory
has no vault `config.yaml`, so the module source default is the value).

Run the steps in order, per issue. If `gh` is unavailable or unauthenticated, report that
by name and skip the whole intake — never render it as "no issues found".

## 1. Query

```
gh issue list --repo <repo> --label vault-accepted --state open \
  --json number,title,labels,body,createdAt
```

Admitted, open, not yet captured — this query is the trigger because:

- **`vault-accepted` is owner-applied admission** (A15(a)) — `vault-filed` is candidacy
  only, so a stranger's filing costs the factory nothing mandatory until the owner admits
  it.
- **Declined issues are closed** (A15(b)) — `--state open` makes them structurally
  invisible; no decline logic is needed here.
- **The contract's state flow** (`field-contract.md:85-90`): an issue without
  `vault-filed` is off the rail entirely; one already labeled `captured` that still
  appears in the results is **reported, not re-materialized** (step 3's exclusion is the
  authority on whether it exists on disk).

## 2. Stale-shape gate (before any parse)

Read the issue body's `rail_contract` stamp and compare it to the current contract version
(`field-contract.md:12`). On **mismatch or a missing stamp on a rail-labeled issue**:
report the issue as **stale-shape, held for hand-handling** and stop for that issue — no
materialization, no label change, no hopeful parse. The evolution rule and its legal
response (the owner hand-handles) are homed at `field-contract.md:15-22`; cite it, don't
re-decide it.

## 3. Idempotence exclusion

Build the key `<repo>#<n>`. Search `factory/inbox/*.md` **and**
`factory/cycles/*/filings/*.md` (consumed filings live under the cycle that captured them)
for an
`origin:`-labeled header line carrying that token, **decoration-tolerant**: match the
`<repo>#<n>` token whether the line is the bare machine-written `origin: <repo>#<n>` or a
markdown-decorated variant (e.g. a bulleted, bolded, or backticked `origin:` line — one
pre-rail hand-materialized filing on disk carries exactly that decorated form).

A hit → the issue is already materialized: **skip it**. If the hit issue lacks the
`captured` label, report the label drift and offer the one-line fix
(`gh issue edit <n> --repo <repo> --add-label captured`) rather than re-materializing.
(A15(d): the `origin:` header is the idempotency key — `field-contract.md:56-60`.)

## 4. Materialize

Parse the `### <field_id>` sections (the contract's field table is the list — eight for
every kind, ten for `supersession`) per the contract's field table
(`field-contract.md:38-49` — the table lives there; read it, never copy it here). Write
`factory/inbox/YYYY-MM-DD-HHmmss-<slug>.md` — timestamp from the issue's `createdAt`, slug
from the title, matching `factory/inbox/README.md`'s filename convention — carrying:

- the machine-written header line `origin: <repo>#<n>` — the **bare contract shape**; the
  intake is the sole writer of this header (`field-contract.md:56-60`), so it never writes
  a decorated variant;
- the origin vault and kind (from the payload's fields), and the body content;
- **when the payload's `kind` is `supersession`, the filing's opening line is
  `# \`class: supersession\` — <title>`** — the marker `factory/inbox/README.md:80` defines
  and `inbox-capture/references/grounding-methodology.md:57-59` keys on; without it a
  rail-filed retirement is graded as a candidate. The two halves are carried as their own
  sections (`## superseded_rule`, `## superseding_mechanism`) so the grounding's
  *verify-both-halves-separately* step (`grounding-methodology.md:64-67`) has them by name.

A `kind: supersession` payload missing either half — no `### superseded_rule` or
`### superseding_mechanism` section, or an empty one — is **held for hand-handling**
exactly as a stale-shape issue is (step 2): reported by name, no label change, never
materialized under another class.

The filing is **raw field signal**: materialization does not ground it. Grounding is
Capture's next stage, unchanged — the filing joins this same run's un-captured set.

## 5. Transition

Apply the capture label:

```
gh issue edit <n> --repo <repo> --add-label captured
```

(A15(c).) The issue stays **open** — it closes at archival (its build shipped and passed
acceptance), a transition owned by `cycle-closeout` Stage 5, not here. Report each
materialization (issue → filing path) in the run's output; in headless mode each key joins
the `issues_materialized` list.

## 6. Amendment leg

Consume owner-admitted post-capture comments. The `amended` label's meaning — owner-applied
admission of comment(s) on a `captured` open issue — is the contract's (its label table,
`field-contract.md:65-83`); this leg only consumes it. Query:

```
gh issue list --repo <repo> --label captured --label amended --state open \
  --json number,title,labels,createdAt
```

Per hit, in order:

1. **Locate the filing** by the `origin:` token `<repo>#<n>` — step 3's search, reused
   unchanged (decoration-tolerant, `factory/inbox/*.md` **and**
   `factory/cycles/*/filings/*.md`).
2. **Archived filing → hold.** If the token lives only in a cycle's `filings/`, report
   **"amendment on an archived filing — held for owner hand-handling"** and stop for that
   issue: post-archive signal is new signal, and whether it becomes a fresh filing is the
   owner's call. Nothing is appended to closed history; the label is left standing for the
   owner.
3. **No filing anywhere → hold.** A `captured`+`amended` issue with no `origin:` hit is
   label drift (captured but never materialized): report it, held for hand-handling — no
   append target exists.
4. **Append, comment-granular.** Fetch the issue's comments
   (`gh issue view <n> --repo <repo> --json comments`). For each comment **not already
   recorded in the filing** — matched by comment timestamp+author against existing
   amendment headers — append a dated section to the filing:

   ```
   ## Amendment — <repo>#<n> comment <ISO-timestamp> (<author>)
   ```

   carrying the comment body **verbatim**. The stale-shape gate (step 2) does **not**
   apply: comments are not payloads; the appended text is raw field signal that Capture
   grounds like any filing body. The filing is never re-materialized — the `origin:`
   header stays the idempotency key.
5. **Consume on read.** `gh issue edit <n> --repo <repo> --remove-label amended`. The
   label is the watermark — no stored state; the owner re-applies it to admit a later
   comment batch. The issue stays `captured` (and open); no other label changes.
6. **The filing re-enters capture.** The appended amendment **joins this run's un-captured
   set**: the filing re-enters capture for its amendment section only, under whatever
   capture posture prevails (mid-cycle addendum posture included).

Report each consumption (issue → filing path, comments appended) and each hold in the
run's output.

## What this file does not own

- **Admission and decline are owner triage verbs, performed on GitHub**: the owner applies
  `vault-accepted` to admit, or applies `declined` and closes the issue with a stated
  reason (nothing materialized). The intake only respects the results — declined issues
  never reach the query.
- **Applying `amended` is an owner triage verb, performed on GitHub**: the owner admits
  post-capture comment(s) by applying the label; the intake only consumes it (the
  amendment leg above). An unadmitted comment reaches nothing.
- **The label vocabulary and state flow** live in the contract's label table
  (`field-contract.md:65-83`).
- **Community/noise traffic** on the public tracker is a released standing watch (E4, Arc
  9) — the admission trigger above *is* the mitigation; nothing more is built until real
  traffic teaches otherwise.
