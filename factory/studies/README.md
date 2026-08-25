# The study register

**Single home for study mechanics** (platform P-14, 2026-08-25). Every other site that cites
a study carries a pointer here and never restates the ids, the frontmatter, or the boundary.

A **study** is a cross-cycle, problem-shaped **root-cause analysis**: the durable record of a
diagnosis that outlives any one cycle and that filings, captures, and briefs can rest on by
citation instead of by restatement.

## Why the register exists

The 2026-08-20 PARA analysis diagnosed its root cause correctly, lived in `_output/` —
**gitignored** — and was distilled into a filing that carried the *symptom* but not the
*cause*. The cause never entered the factory record. It re-surfaced five days and two releases
later as an independent re-derivation by the owner, who arrived at the same answer without
reference to having proposed it before. That convergence is good evidence the answer is right
and equally good evidence that the loop dropped it the first time.

The loss was not a filing-discipline failure. **The document had nowhere tracked to live.**
This ledger's own stood-up note and P-5 both cite `_output/brainstorming/…` as provenance —
the factory record's links point into untracked space. The register is the fix: a tracked,
citable path, so a filing can say *see `ST-N`* rather than restating an analysis badly or
losing it entirely.

## The boundary against its neighbours

| Artifact | Reads | Lives | Answers |
|---|---|---|---|
| **Spike** (`factory/platform/spikes/`) | an **external** source, before a brief | register entry + a cycle-local harvest | *what does the real source actually say?* |
| **Study** (here) | the module's **internal** structure, across cycles | here, self-contained | *why does this keep happening?* |
| **Method note** (`factory/method/`) | the factory's own practice | there | *how does the factory work?* |
| **Filing** (`factory/inbox/`) | one field instance | inbox → its cycle's `filings/` | *what broke, where?* |

A filing is bounded to what a vault experienced; a study is bounded to a *cause*. Where a
filing's claim rests on a study, it cites the `ST-N` path and states the claim — never both
the claim and its full derivation.

**A study is self-contained, and that is the one place it diverges from the spike register.**
A spike's harvest lives in the cycle directory that produced it and the register entry points
at it. A study has no such durable source: the session artifact it distils lives in
gitignored `_output/`, which is exactly the failure being fixed. So a study **carries its
diagnosis in full** — the evidence, the causal chain, the rejected alternatives, and what the
session got wrong. The `_output/` path is recorded as the session's provenance, and is never
load-bearing; assume it is gone.

## Files and ids

One file per study: `factory/studies/ST-N-<slug>.md`.

- **`ST-N` is a register-global id**, not per-cycle. Allocated once, never reused, never
  renumbered — a cited study's id stays live because filings cite it.
- The next id is one past the highest `ST-N-*.md` in this directory. Nothing else assigns ids.

```yaml
---
id: 'ST-N'
slug: '<kebab-slug>'
title: '<the cause, as a claim — not the symptom>'
status: 'standing'          # standing | superseded
opened: 'YYYY-MM-DD'
opened_by: '<owner problem-solving session | capture | roundtable>'
session: '<path to the source session artifact, if any — provenance only, never load-bearing>'
causes: []                  # the root causes this study names, one line each
cited_by: []                # filings, captures, briefs that rest on it — appended, never replaced
superseded_by: ''           # optional: the ST-N that replaced this diagnosis
---
```

`status: superseded` means a later study **replaced the diagnosis** — not that the problem was
fixed. A study whose cause has been repaired stays `standing`; the repair is recorded in
`cited_by:` and in the cycle record. A diagnosis that was simply wrong is superseded, and the
wrong one stays in the register: knowing what the factory believed, and why it was wrong, is
half of what a register is for.

## Citable, never blocking

**A study gates nothing.** The spike register earns lifecycle gates because an unread external
source makes a brief reason from memory; a study is a diagnosis anyone may cite, argue with, or
ignore with reasons. Adding a second set of adoption gates across five skills would be the
accretion the register's own first two entries were written about. If a study should bind a
build, ideation says so as a ruling — the register does not say it for them.

## What is *not* in the register

Back-fill was bounded to the two entries below (P-14 out-of-scope). Deliberately unmigrated,
named here so the register's silence is a recorded choice rather than an oversight:

- `_output/problem-solution-2026-08-08.md` — extending module-owned skills without editing
  source (resolved into the dispatch generalization).
- `_output/problem-solution-2026-08-19.md` — the single-machine feedback loop (resolved: the
  GitHub filing rail shipped).
- `_output/problem-solution-2026-08-24.md` — full lint's cost curve outrunning the wiki it
  audits.
- `_output/brainstorming/` memlogs — a different artifact class (generative, not diagnostic).
  A later item if they prove worth tracking.

The first three are problem-solving sessions that **reached their fix**; the register exists
for diagnoses that outlive their cycle, and a spent one earns no entry merely by sharing a
filename shape. Any of them can be back-filled later if a live question starts resting on it.

## Register

| id | slug | status | opened | the cause it names |
|---|---|---|---|---|
| `ST-1` | para-write-path-single-door | standing | 2026-08-20 | One vault posture shipped as a universal invariant; permission fused to provenance in one verb |
| `ST-2` | location-as-proxy-for-trust | standing | 2026-08-25 | PARA location carries a trust claim `trust:` already carries; the loop can process defects but not obsolescence |

*(This table is a convenience index over the files, which are authoritative. It lists every
register file — a completeness claim it can keep only because the directory is its population;
re-derive it from `ls` when in doubt.)*
