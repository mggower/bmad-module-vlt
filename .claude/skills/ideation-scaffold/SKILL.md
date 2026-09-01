---
name: ideation-scaffold
description: Lays the empty ideation-rulings skeleton into the open cycle roadmap for the owner to fill. Use when the user says 'scaffold ideation' or 'start ideation'.
---

# ideation-scaffold

## Overview

Ideation (lifecycle step 3) is owner-steered and deliberately unformalized — and that is a
feature, ruled in the 2026-07-12 handoff. But `build-brief` hard-gates on rulings existing,
so the one unformalized step gatekeeps the formalized one, and when build-brief returns
`blocked: ideation missing` nothing tells anyone what a sufficient rulings record looks
like. This skill closes exactly that gap: it scaffolds the **recording**, never the
**deciding**. Act as the ideation session's clerk — you lay out the ledger pages and put
the open questions on the table; every answer written into them is the owner's.

Concretely: given the open cycle roadmap, write an empty, dated **Ideation rulings** section
shaped so that `build-brief`'s Discovery and Readiness gate parse it — then seed it with
the *questions* the capture already flagged as needing rulings, unanswered. Do not propose
groupings, assign filings to builds, resolve open questions, or close spikes. A slot the
owner hasn't filled stays visibly empty; an empty slot is honest, a guessed answer is a
lifecycle violation.

**Lifecycle position:** step 3 (Ideate) of the loop mapped in
`.claude/skills/vlt-lifecycle.md` — this skill is the recording scaffold for the
owner-steered session, not the session itself. Every report ends with a
**Next lifecycle move** line. The same line is **restamped into the open cycle roadmap's
foot** in the run that moves the position — the chat report alone does not discharge it
*(the map's standing rule; platform P-13)*.

## On Activation

Load available config from `{project-root}/_bmad/config.toml` and `config.user.toml` if
present. This skill needs none beyond `user_name` / `communication_language` if set.

`--headless` / `-H`: run Discovery → Scaffold with no questions. On completion, emit only:

```json
{"status": "complete", "roadmap": "{path}", "section": "{the new section's heading}", "seeded_questions": N, "next": "{next lifecycle move}"}
```

`status` is `blocked` with a one-line `reason` when there is nothing to ideate (no open
roadmap, or every captured filing already has a build assignment in a rulings section) or
when an unfilled skeleton for this capture batch already exists — point at it instead of
laying a second (never two skeletons for one batch).

## Discovery

Find the **open cycle roadmap**: read `factory/CYCLE` (a `none` line → blocked, nothing to
ideate), then open `factory/cycles/<that NN-<slug>>/roadmap.md`.
In it, identify the **unideated batch**: captured filings (`### A<cycle>-<i>` subsections)
that no existing Ideation rulings section assigns to a build. Then collect what the
skeleton must surface, from where the capture recorded it — the pending owner rulings the
capture flagged as gating ideation, the open-design-questions section entries tied to this
batch, any proposed-grouping material the capture left (carry it as *capture's proposal,
unaccepted* — never promote it to a ruling), and any spike obligations or evidence debts
the captures name.

Then read the **spike register** at `factory/platform/spikes/` — its mechanics (ids,
statuses, frontmatter, the gates) are single-homed at `factory/platform/spikes/README.md`;
point at it, never restate it. Collect every register file whose `status:` is `proposed`
or `running`, including any stub `inbox-capture` opened while grounding this batch. Those
are the open questions the batch inherits, and the skeleton must show them: **a spike
that is invisible at adoption gets rediscovered at brief time, which is the most
expensive moment to find it.**

## Scaffold

Append a new section to the roadmap:
`## Ideation rulings — <batch label> (owner-steered, <date>)` — after any existing
rulings sections, before the Deferred acceptance ledger. Match the shape of a closed
cycle's rulings section — exemplar: `factory/cycles/09-boundary/roadmap.md`, its
`## Ideation rulings — A9-1..A9-6` section (read it first; that shape is the parse
target `build-brief` already understands). Skeleton slots, each either seeded with the flagged-but-unanswered
questions from Discovery or left as an explicit `*(owner to fill)*` placeholder:

- **Grouping & order** — which builds, numbered, and which filings each folds in. Build
  numbering is itself an owner call; placeholders, not proposed numbers. Lay each build
  bullet with three one-line fields for the owner to fill: **`binds:`** (the ruling-id
  roster — see the standing rule below), **`spike:`** (`none`, or the `S-N` this
  build's brief depends on), and **`promise:`** (the one vault-facing sentence — see the
  standing rule below). `spike:` and `promise:` are what `build-brief` gates on; an unfilled
  field is not `none` and blocks, which is correct — the owner says whether a build waits on a
  spike and what it promises a vault, never the briefer.
- **Pre-ideation rulings the capture demanded** — seed each flagged ruling as a question.
- **Cross-filing decide-once rulings** — decisions that resolve the same question across
  filings identically.
- **Spikes** — external unknowns needing a read-the-actual-source spike before a brief.
  List every open register entry Discovery collected as one line —
  `S-N (<slug>) — <status> — <question>` — plus a `*(owner to fill)*` slot for spikes
  this batch newly demands. **The register is the record; this section is its view.** An
  owner ruling here (open a spike, kill one, rule a build `spike: none`) is written back
  to the register file in the same session — status and `verdict:` live there, never only
  in roadmap prose. Mechanics: `factory/platform/spikes/README.md`.
- **Evidence-debt dispositions** — each debt attached, or ruled not-blocking, per build.
- **Questions deliberately left to brief time** — per-build, not cross-cutting.

Head the section with the standing sentence that makes it binding once filled: rulings
below are the owner's; briefs cite this section, never re-litigate. Verify the append
landed (re-read), then report.

## Handoff

**Interactive:** state where the skeleton landed and enumerate the seeded questions —
they are the session's agenda. If the owner wants to fill it now, stay and record their
rulings verbatim into the slots (clerk, not advisor: capture, read back, never steer).

**Restamp the cycle roadmap's foot** with this move before reporting — its **last block**, below
any earlier routing. The roadmap's foot is the obligation, the chat report a copy
*(platform P-13)*.

**Next lifecycle move** (routing contract): owner fills the rulings in session; once the
rulings are filled, the move is `convene the roundtable` (`roadmap-roundtable`) — briefs
follow the review. Blocked runs route
per the reason: nothing to ideate → `lifecycle-status` or the map's table for where the
loop actually stands; existing unfilled skeleton → fill that one.

**Headless:** emit only the JSON contract above; the same move goes in `next`.

## Standing rule: every build bullet carries a `promise:` line

*(Platform P-16, 2026-09-01; cause `ST-4`, *provenance is staffed, cognition is not*.)* One
sentence, vault-facing, written **here at ruling time by the owner** — not at brief time, and
not by the briefer:

> *after this ships, a vault owner running `vlt-<x>` sees Y instead of Z*

**Why it sits at ruling time.** A per-build vault-facing sentence already exists: a brief's
`title:` is public prose collected verbatim into the CHANGELOG. But it is authored at **brief
time by the briefer**, *after* scope has been ruled — so scope gets ruled against filing ids and
the first sentence describing the delivery is written by someone reporting a decision they did
not make. `promise:` moves that sentence to the person and the moment that own the scope call.

**What consumes it.** `build-brief` carries it into the brief's scope statement and into the
brief's `title:`, **never re-authoring it** — the release path is unchanged, and the CHANGELOG
still collects from `title:` (owner-ruled 2026-09-01: `promise:` *feeds* `title:` rather than
replacing it as the CHANGELOG source, so a briefer may sharpen the sentence for what actually
shipped without a second vault-facing sentence existing to drift).

**Unfilled blocks**, the treatment `spike:` has — not the reconstruct-and-disclose treatment
`binds:` has. The reason is structural: `binds:` is reconstructible (the ruling ids are in the
roadmap and can be re-derived), and **a promise is not — it can only be re-invented**, by the
wrong author at the wrong time, which is the exact failure the field exists to repair. Leave it
`*(owner to fill)*` and the brief will not be written; that is the field working.

**Scope is ruled against promises, not filing ids.** That is the point of the field, and it is
why it is laid in the grouping bullet rather than anywhere later.

## Standing rule: every build bullet carries a `binds:` roster

*(Arc 9 roundtable, 2026-08-20 — home for the rule; `build-brief` Discovery is its reader.)*

The skeleton's grouping section addresses rulings by **question id** (`Q*`/`D*`/`S*`/`E*`) and
every downstream consumer — the build-order table, the release plan, `build-brief`'s Discovery —
resolves by **build number**. The mapping is written in one direction only, so a ruling routinely
governs a build without naming it: **a briefer obeying "read every ruling that names build N"
misses it.**

So lay each build bullet with a **`binds:`** line — a one-line roster of the ruling ids that
govern that build — and keep it current as rounds add rulings. It costs a line per build and it
is the difference between a brief that inherits its constraints and one that rediscovers them
after shipping.

Related: when a lead-in **counts** its contents ("four items, one unruled"), later rounds append
and the count silently lies. Prefer "as ruled" over a count, or re-stamp the lead-in on append —
`CLAUDE.md`'s *lists that claim completeness drift* rule, applied to append-only reports.
