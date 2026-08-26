# The study register

**Single home for study mechanics** (platform P-14). Every other site that cites a study
carries a pointer here and never restates the ids, the frontmatter, or the boundary.

A **study** is a cross-cycle, problem-shaped **root-cause analysis**: the durable record of a
diagnosis that outlives any one cycle and that filings, captures, and briefs can rest on by
citation instead of by restatement.

The register exists because a diagnosis with nowhere tracked to live does not survive. It is
distilled into whatever artifact was due that day — which carries the *symptom*, because a
symptom is what that artifact is shaped to carry — and the cause is lost. Cycles later the
same cause is re-derived from scratch, and the loop pays twice for one answer. A study is the
tracked, citable path that makes the first derivation reusable: a filing says *see `ST-N`*
rather than restating an analysis badly or dropping it entirely.

## Opening a study

Open one when the diagnosis is bigger than the thing that provoked it — when *why does this
keep happening?* has an answer that will still be true next cycle and that is about more than
the one artifact in front of you. Typical openers: an owner problem-solving session that
reached a cause but no fix; a capture whose grounding kept finding one shape under three
unrelated filings; a roundtable that named a structural cause with no build to attach it to.

Do **not** open one for a defect with a known fix (that is a filing), for an external unknown
(that is a spike), or for how the factory itself works (that is a method note). The boundary
table below is the full cut.

Anyone may open one. There is no adoption gate and no owner ruling required — see *Citable,
never blocking*.

## Using a study

- **Cite it, don't copy it.** A citing site states its own claim in its own scope and names
  the `ST-N`. It never carries both the claim and the derivation — that is the duplication
  the register exists to end.
- **Append yourself to `cited_by:`.** The citing site's path goes in the study's `cited_by:`
  list, appended, never replaced. That list is how a study's reach stays visible: it is the
  evidence that a cause is still live, and the trail a later repair follows to find everything
  that rested on it.
- **Argue with it.** A study is a diagnosis, not a ruling. Disagreeing is ordinary work; the
  register records the disagreement rather than resolving it. Where a later study replaces the
  diagnosis, it stamps `superseded_by:` on the old one and says at its own name what changed.
- **Read it whole before resting on it.** A study carries its rejected alternatives and what
  its own session got wrong. Those are load-bearing: they are how you tell a cause that was
  tested from a cause that was merely first.

## The boundary against its neighbours

| Artifact | Reads | Lives | Answers |
|---|---|---|---|
| **Spike** (`factory/platform/spikes/`) | an **external** source, before a brief | register entry + a cycle-local harvest | *what does the real source actually say?* |
| **Study** (here) | the module's **internal** structure, across cycles | here, self-contained | *why does this keep happening?* |
| **Method note** (`factory/method/`) | the factory's own practice | there | *how does the factory work?* |
| **Filing** (`factory/inbox/`) | one field instance | inbox → its cycle's `filings/` | *what broke, where?* |

A filing is bounded to what a vault experienced; a study is bounded to a *cause*.

**A study is self-contained, and that is the one place it diverges from the spike register**,
which points at a harvest it does not carry (mechanics: `factory/platform/spikes/README.md`).

A study has no such durable source. The working session it distils is a **transcript, not a
record**: it carries the factory's unscrubbed specifics — machine paths, real vault paths, the
owner's name — and hundreds of lines of method ceremony around the diagnosis, so it can be
neither published as-is nor read cheaply by a citing site. A spike's harvest has neither
problem: it is written into the cycle directory as a tracked, already-public artifact.

So a study **carries its diagnosis in full**: the evidence, the causal chain, the rejected
alternatives, and what the session got wrong. Where a source artifact exists it is named in
`session:` as provenance only, never load-bearing. Write every study as if that path is
already gone.

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
ignore with reasons. A second set of adoption gates across five skills would be the accretion
the register's own first two entries were written about. If a study should bind a build,
ideation says so as a ruling — the register does not say it for them.

## What does not earn an entry

The test is the **cause**, not the fix. Ask: *would naming this cause change how a later cycle
reads a problem it has not met yet?* A cause whose repair already shipped still passes if the
answer is yes — the repair is recorded in `cited_by:`, and the study stays `standing`.

Two near-misses, stated so the line holds under pressure:

- **A cause local to the thing it explained.** Not *it reached its fix* — a shipped fix retires
  nothing. The test is whether the cause generalizes past the artifact that carried it. A
  diagnosis that bottoms out in one file's design is that file's commit message.
- **Generative artifacts** — brainstorms, memlogs, option sketches. A different class: they
  produce candidates, not diagnoses.

**A live diagnosis is never excluded.** Where the fix is deferred, unbuilt, or only partly
shipped, the cause is by construction still doing work — read the cycle record before judging a
session spent. The register's silence about a specific document is a choice, and the item that
made it records which document and why.

*(The bolded guard is here because this register's own build failed it: `ST-3` was excluded at
back-fill as "reached its fix" when its cause was live and deferred to the next cycle. The
earlier criterion also contradicted the `status:` rule above — a repaired cause stays
`standing` once inside, while "reached its fix" barred it at the door.)*

## Register

| id | slug | status | opened | the cause it names |
|---|---|---|---|---|
| `ST-1` | para-write-path-single-door | standing | 2026-08-20 | One vault posture shipped as a universal invariant; permission fused to provenance in one verb |
| `ST-2` | location-as-proxy-for-trust | standing | 2026-08-25 | PARA location carries a trust claim `trust:` already carries; the loop can process defects but not obsolescence |
| `ST-3` | governance-has-no-addressable-projection | standing | 2026-08-24 | A convention's only unit is the whole file, so every consumer needing a slice pays for all of it; and full-mode lint has no memory across runs |
| `ST-4` | provenance-staffed-cognition-unstaffed | standing | 2026-08-25 | Every lifecycle artifact is written to be re-read later and none to be read now; the vault-facing sentence is authored in the wrong chain by the wrong party; the loop has no measure of its own legibility, so a recommendation silently substitutes for one; the inbox uses location as a proxy for status |
| `ST-5` | specimens-have-no-owner | standing | 2026-08-26 | Field specimens have no owner, so instruments are built at the point of least evidence — from the fix's shape, not the failure's; and one tag welds blocking power to grading modality |

*(This table is a convenience index over the files, which are authoritative. It lists every
register file — a completeness claim it can keep only because the directory is its population;
re-derive it from `ls` when in doubt.)*
