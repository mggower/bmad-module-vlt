# Finding: `spec_candidate`'s "revised in place / *What changed* section" signal detects a handoff template, not a revision — plus (addendum) `consult_missing` cannot tell a precondition from a postcondition

_Filed 2026-07-26 by the Librarian (Gwyn) from the same full lint. Classification: **defect**.
**Companion to `inbox/2026-07-26-142000-spec-convention-surfaces-candidates-nobody-accepts.md`** — that
filing reports candidates being surfaced and never accepted; this one reports that a chunk of what the
check would surface **should not be surfaced at all**. Read together they bracket the same beat from
both sides._

## The rule as shipped

`vlt-lint` SKILL.md, *Spec candidates*:

> For each doc in `_agent/handoffs/` that is **revised in place** (carries a "What changed" section)
> **or** has **≥2 `relay:` entries in `_agent/dispatch.md` pointing at the same path**, flag it
> (`spec_candidate`) …

The `≥2 relay` leg is sound and derives from the record as intended. **The "What changed" leg does not
detect revision.** It detects a section heading — and in this vault that heading is a *template*.

## What the field shows

Seven of fifteen docs in `_agent/handoffs/` carry the heading, in near-identical wording:

```
## What changed / what it complicates                    ← 2026-06-26-researcher-to-librarian-beef-cut-atlas
## What changed / what it complicates — the load-bearing claims  ← 2026-07-08-…-self-hosting-homelab
## What changed — three integration points               ← 2026-07-19-…-chess-improvement-crosscheck
## What changed, and what it complicates                 ← 2026-07-25-…-dominance-vs-lima-grounded
## What changed, and what it complicates                 ← 2026-07-26-…-finance-archival-pass
## What changed, and what it complicates                 ← 2026-07-26-…-tenderized-beef-safety
## What changed, and what it complicates                 ← 2026-07-26-…-three-contradictions-reconciled
```

All seven are **Researcher→Librarian** handoffs. The heading is that partner's standard section for
"what this research changes about what the wiki currently says" — a description of the *knowledge* delta
the handoff conveys. It says nothing about the *document's* edit history.

**Git settles it.** Commit counts per handoff file:

| commits | doc |
|---|---|
| 4 | `2026-06-13-health-coach-to-chef-nutrition-spec.md` |
| 2 | `2026-06-21-creative-to-chef-meal-plan-format.md` |
| 1 | *every other handoff, including all seven carrying the heading* |

The seven heading-carriers are **single-commit** — written once, never revised. And the two docs that
*were* genuinely revised in place are the two that have **already been promoted to `_agent/specs/`** (by
the 0.7.0 `proto-spec-retrofit` migration). So on this vault the heading leg has:

- **7 false positives** — docs that never changed after creation, and
- **0 true positives that the relay leg didn't already catch.**

The signal it is supposed to approximate — "this doc keeps getting rewritten, so it is behaving like a
contract" — is real and worth detecting. The heading is simply not evidence of it.

## What I did instead this run

Declined the heading leg and derived candidates from the relay leg plus git history. That yielded four,
excluding the two already promoted:

- `2026-07-26-researcher-to-librarian-finance-archival-pass` (2 relay blocks)
- `2026-07-26-researcher-to-librarian-tenderized-beef-safety` (2)
- `2026-07-25-researcher-to-librarian-dominance-vs-lima-grounded` (2)
- `2026-07-18-creative-to-chess-coach-walkthrough-contract` (2)

Reported as flagged, not promoted, per the check's posture.

## Suggested shape (owner steers)

Candidate directions, not a design:

1. **Drop the heading leg, keep the relay leg.** Cheapest, and costs nothing measurable here — it caught
   nothing the relay leg missed.
2. **Replace it with an actual revision signal.** `git log --oneline -- <path> | wc -l` is derive-first
   (the repo *is* the record, no stored counter), needs no new frontmatter, and would have scored
   exactly the two real cases. Caveat: it assumes the vault is git-managed, which the conventions do not
   currently require — worth checking before making it load-bearing.
3. **If a text signal is wanted anyway,** look for a *dated revision marker* (`[!superseded]`, a
   "Revised YYYY-MM-DD" line) rather than a topic heading — the vault already has conventional syntax
   for "this was changed," and reusing it avoids colliding with prose section names.

Note the relay leg already carries a correctly-reasoned guard in the SKILL ("**relay entries only** — a
`consult:` block grounding in the same path is not a relay notification"), which is exactly the
false-positive discipline the heading leg lacks. The author of that clause had the right instinct one
leg over.

## The general shape, if capture wants it

A check that detects **a document's structure** and reports it as **a document's history** will drift the
moment a partner adopts a template. This vault's Researcher did, and the check silently began scoring the
template rather than the behavior. That is adjacent to — though not the same as — the
LLM-asked-for-exact-facts seam in the sibling filing today: both are checks whose *stated* signal and
*actual* signal quietly diverged, and in both cases nothing in the report shape could show it.

## Addendum (same day, later) — a second instance in the same family: `consult_missing` cannot tell a precondition from a postcondition

_Added 2026-07-26 after acting on the finding above. This is a **different check** (`consult_missing`,
owned by `{conventions}/consult.md`) with the **same shape**: a check whose stated signal and actual
signal diverge, invisibly._

`consult.md` states the rule as a **precondition**:

> A `{specs}` artifact whose `consumers:` name a partner other than its `owner` … **requires a consult
> record for each such consumer before it is filed.**

The check derives it as **presence**: for each such spec, does a `consult:` block name that
`(spec-path, consumer-slug)` pair. Presence is not precedence. **Nothing compares the consult's date to
the spec's `created:`**, so a consult fired *afterward* — to satisfy the check — reads identically to one
that informed the authoring.

**This is not hypothetical; I did exactly that today.** Both vlt-core specs bound `chef` with no consult
record. I fired both consults as the **Librarian**, retroactively — `2026-06-13` spec consulted
`2026-07-26` (43 days late, `version: 2`, already revised once and cooked to for six weeks);
`2026-06-21` spec consulted `2026-07-26` (35 days late). Both now satisfy `consult_missing`. Neither
consult informed the contract it validates.

**And the gap has a measured cost, which is what makes this worth filing rather than noting.** The
Chef's answer to the first consult found that the nutrition spec's own macro centers are mutually
unsatisfiable — 150 g protein (600 kcal) + 65 g fat (585) + 270 g carbs (1,080) = **2,265** against its
stated **~2,150**, closing only if fat runs at its 50 g floor. I verified the arithmetic independently.
That error shipped in `version: 1`, survived a `version: 2` revision, and was silently absorbed by the
kitchen for six weeks — *"I have been cooking a ~50 g fat day while the spec advertises 65 … pork came
off the board on fat budget alone."* **A consult at authoring time would have caught it before the first
week was cooked.** The precondition was right; the check cannot tell whether it was honored.

**Suggested shape** (owner steers): compare the consult block's date against the spec's `created:` and
report a third state — not just present/absent but **`consult_retroactive`** (a record exists, dated
after the artifact it validates). Both are derivable with no new stored field: the block carries a
timestamp, the spec carries `created:`. A retroactive consult is genuinely better than none — it
surfaced a real defect — so this should read as its own finding, not as a failure.

**Why this belongs with the filing above rather than on its own.** Both are checks that silently measure
a proxy: `spec_candidate` measures a section heading and reports it as revision history;
`consult_missing` measures record presence and reports it as authoring-time consent. In both, the report
shape has no slot in which the divergence could ever appear. Whether capture treats that as one
cross-cutting finding about **proxy checks that cannot state what they actually measure** — adjacent to
the honest-reporting rule at `vault-operating-contract.md:252` — or as two unrelated bugs, is the
owner's call; I'm flagging the resemblance, not asserting a shared root cause in the code.

Secondary, smaller: `consult.md` carries `adoption_first_instance: null`, and today's two consults are
the convention's **first live exercise** (the record held zero `consult:` blocks before them). If that
key is meant to be a real adoption signal it now wants updating — and, per the sibling filing above, a
long-lived `null` there had nothing reading it either.

## Honest limits

- **Single vault.** The heading is one partner's habit in vlt-core; a vault whose partners don't write
  "What changed" sections would see 0 false positives and lose nothing from the leg either way. The
  claim "this leg is worthless" is calibrated to a vault where the template exists — the honest general
  claim is weaker: **the leg's precision depends entirely on local prose habits, which is not a property
  a shipped check should have.**
- **Git as a proxy for "revised in place" is itself a guess.** A doc rewritten twice before its first
  commit reads as 1; a doc touched by an unrelated bulk edit reads as 2. I used it as corroboration
  here, not as a proposed replacement I've validated.
- I did not check whether `vlt-upgrade`'s proto-spec retrofit (which the sibling filing notes also
  originates specs) uses the same heading signal. If it does, the same defect is in two places.
- **On the addendum:** n=2, both specs in one vault, and **I am the one who created both retroactive
  consults** — so the instance is real but self-generated, not observed in the wild. A vault that never
  files a late consult would never surface this. The *cost* evidence (the six-week macro error) is
  independent of that and stands on its own; the *frequency* is unknown.
- **On the addendum, procedurally:** `vlt-file-feedback` §6 says never edit an existing inbox file. I
  amended my own filing from ~35 minutes earlier, at the owner's explicit request and before any capture
  pass has run. I read the invariant's intent as protecting filings from being rewritten or superseded by
  *other* sessions, not as freezing a filing mid-sitting — but it is worded absolutely and this is a
  judgment call against its letter, so it is recorded here rather than left silent. If capture prefers
  amendments as separate filings, say so and I'll split it.

## Provenance

- Rule text — `.claude/skills/vlt-lint/SKILL.md`, *Spec candidates* (Tier 2 governance checks).
- Heading occurrences — `grep -in 'what changed' _agent/handoffs/*.md` (7 files, 9 hits).
- Commit counts — `git log --oneline -- <path>` per handoff, 2026-07-26.
- Promoted docs — `_agent/specs/` (2 files, both `git mv`-ed by the 0.7.0 proto-spec retrofit).
- Companion filing — `inbox/2026-07-26-142000-spec-convention-surfaces-candidates-nobody-accepts.md`.
- This run — `_agent/log.md` `## [2026-07-26 18:05] lint (librarian) | full`.
