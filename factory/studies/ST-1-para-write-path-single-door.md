---
id: 'ST-1'
slug: 'para-write-path-single-door'
title: 'The PARA write-path is a single door of the wrong shape — one vault posture shipped as a universal invariant, with permission fused to provenance'
status: 'standing'
opened: '2026-08-20'
opened_by: 'owner problem-solving session'
session: '_output/problem-solution-2026-08-20.md (gitignored — provenance only)'
causes:
  - 'Primary: the module encodes one vault posture (wiki-centric, single-owner, PARA-as-output-shelf) as a hard universal invariant rather than as a declared, configurable posture.'
  - 'Secondary, equally load-bearing: there is exactly one PARA verb, and it fuses write permission to wiki provenance — widening the first required a second verb, none existed, so falsification was the only outlet.'
cited_by:
  - 'factory/cycles/10-signal-integrity/filings/2026-08-20-093000-para-write-path-single-door-wrong-shape.md (the filing distilled from this session — it carried the symptom, not the cause)'
  - 'factory/studies/ST-2-location-as-proxy-for-trust.md (the re-derivation five days later; ST-2 §Why this study is here explains what was lost)'
  - 'factory/cycles/12-proxy-claims/roadmap.md §A12-3 (capture 2026-08-25 — the filing''s six steps re-derive C1/C2/C3/C5; C4 provenance segregation and RC-B permission-fused-to-provenance are NOT carried, flagged there as the un-carried half)'
  - 'factory/cycles/14-no-enforcement-point/roadmap.md §Ideation rulings Q4 (roundtable 2026-08-26 — Q4 rules A14-7''s jurisdiction narrowing BY ARTIFACT CLASS rather than by writer, citing this study''s permission-fused-to-provenance cause by name as the reason to refuse the writer-shaped axis; the roundtable then found the class test has no mechanical discriminator, so the refusal stands but the replacement does not yet bind)'
superseded_by: ''
---

# ST-1 — The PARA write-path is a single door of the wrong shape

**Back-filled 2026-08-25** (platform P-14) from the 2026-08-20 owner problem-solving session.
This is the analysis that was lost: it lived only in gitignored `_output/`, and the filing
distilled from it carried the symptom while the cause never entered the factory record. Read
`ST-2` for what that cost.

## The presenting complaint, and the premise grounding killed

The session opened on: *the PARA guards are too strict; `vlt-extract` is the only door, it is
hardly ever used, and blocking the Creative from operating within PARA has become a
significant blocker.*

**Grounding inverted the premise, and the correction strengthened the case.** In `app-vault` —
a shared team development vault where *projects* are the dominant focus — `vlt-extract` was
not hardly used: it was the **most-used op in the vault** (28 of 85 `{log}` entries, 33%). Nor
was PARA empty of agent work: **57 markdown files** lived under `projects/`, all carrying
correct-looking extraction frontmatter.

What was actually broken was the **shape of the door, not its existence**. Every PARA write in
that vault had to masquerade as an extraction, and extraction's own invariants were falsified
to make the disguise fit:

| `extraction.md` invariant | What the field vault did |
|---|---|
| Kebab-case filenames, **no datestamp**, stable identity | Dated-snapshot identity throughout (`…/2026-08-14-harness-grounding-insights.md`) — the exact form the convention forbids |
| `sources:` lists **only wiki pages** — the provenance firewall | A PARA sibling, and a bare external prose reference to a repo branch and PR |
| One artifact = one synthesized deliverable | Multi-file trees with binaries: `canvas/*.excalidraw`, `canvas/screens/*.png`, `presentation/`, `slides/`, `research/` |
| `status:` per type (project → `in-progress`) | `status: done` |

The pressure valve was visible outside PARA too: the contract's allowance for *"ad-hoc owned
artifacts under `_agent/` that are not named in the structure map"* absorbed the overflow, and
the vault then went past the layer model entirely with top-level `publish/` and `users/`.

## The refined problem

vlt models PARA as a **curation destination reachable only by wiki synthesis**, but a
development vault uses PARA as a **workspace** — where in-flight, externally-grounded,
multi-file project work lives. One door, one cargo type. Work that is legitimately
project-shaped but not wiki-derived has no honest route in, so agents either dump it into
ad-hoc `_agent/` and top-level folders, or push it through `vlt-extract` by falsifying
extraction's invariants.

**The cost is not blocked work — the work happens anyway.** The cost is that the flagship
shared vault's PARA metadata now *lies*: `sources:` no longer certifies wiki provenance, so the
firewall that makes an extracted artifact trustworthy was already breached, silently, on 57
files.

## Root cause

**Five Whys, condensed:** an agent can't file project work into PARA because the contract
declares PARA human territory with one sanctioned door → PARA is modeled as human territory
because it inherits the PARA-method framing of a *personal* knowledge vault → that framing
survived into the shipped invariant because vlt v1 was designed against **one** vault, where
the wiki *is* the vault and PARA is downstream of it → it breaks now because **the vault class
widened**: in a shared team dev vault the work product *is* the project and the wiki is a
support layer, so the arrow reverses → and the breakage expresses as *falsification* rather
than as a blocked agent because **permission and provenance are fused into a single verb**.
`vlt-extract` grants the right to write into PARA and the wiki-provenance discipline as one
indivisible package. You cannot take the first without accepting the second, so work that
needed the first paid for it by faking the second.

> **RC-A (primary).** One vault posture is encoded as a hard universal invariant instead of a
> declared, configurable posture. The write boundary is a *derivative* of an assumption about
> what a vault is for, and that assumption is now one case among several.
>
> **RC-B (secondary, equally load-bearing).** Exactly one PARA verb exists, fusing write
> permission to wiki provenance.

### Contributing factors

1. **Four-site internalization.** The rule lives in the contract, `extraction.md`,
   `vlt-extract/SKILL.md`, and the Creative's *"Your non-negotiable."* Being identity-level,
   partners complied **rhetorically** while routing around it **behaviorally**. An
   identity-bearing rule that cannot be satisfied produces a partner that *performs* the rule.
2. **The `_agent/` ad-hoc permission was an unmetered relief valve** — the module got sprawl
   where it should have gotten an error signal.
3. **Lint was blind to the failure.** Everything superficially validates.
4. **No PARA state model** (in-flight vs settled) and **no multi-file artifact model.**

### System dynamics

- **R1 — the self-defeating guard (reinforcing).** Stricter single door → more work must
  disguise itself → `sources:` certifies less → the firewall means less → the guard commands
  less respect → the next disguise is cheaper. **The guard erodes the invariant it exists to
  protect**, and the loop was already several turns in.
- **B1 — the balancing loop that was never built.** A refusal should raise a signal (block,
  file a `capability-gap`, surface to the owner). The ad-hoc valve absorbed the pressure with
  no signal, so **the system had no way to learn that its rule was wrong.**
- **D1 — the audit delay.** Falsification is visible only on deliberate inspection, which is
  why R1 ran unchecked for months.

**Leverage point:** not the rule's strictness — tightening feeds R1, loosening sacrifices the
firewall — but the **fusion of permission and provenance in one verb**.

## What the session recommended

**"Two verbs, one boundary, drawn by authorship"** — a composite scoring 141 against 113/103/101
for the single-lever options and 83 for the tempting relaxation of extraction's `sources:` rule
(which scores *below status quo* on the criterion that matters most).

- **C1** — re-draw Layer 3 by **authorship, not location**: *a partner never modifies an
  artifact it did not author*; never `author: human`, never `trust: verified|canonical`, never
  MOCs, never raises `trust:`, never restructures a human taxonomy.
- **C2** — **per-zone posture** as a designed parameter read (`projects: workspace`,
  `areas: curated`, `resources: curated`), so a vault declares its posture without forking
  skill text.
- **C3** — a **second verb** owning the folder-artifact model, the `working|settled` lifecycle,
  and dated-vs-stable naming. Extraction is not modified at all.
- **C4** — **provenance segregation**: `sources:` stays wiki-only forever; a new `grounding:`
  field carries external evidence. This is the component that restores the firewall.
- **C5** — **enforcement in the same build**: lint catches non-wiki `sources:` entries,
  agent-authored artifacts in curated zones, dated `settled` filenames, and modification of
  human-authored or endorsement-grade artifacts.

Two hard constraints came out of reverse-brainstorming ("how would we guarantee this fails?"):
**enforcement ships in the same build as the rule**, and **`extraction.md`'s invariants are not
touched** — relaxing `sources:` to solve a permission problem trades the invariant for the
convenience.

## Lessons that generalize

1. **A guard that cannot be satisfied does not get obeyed — it gets performed.** Internalizing
   a rule at four sites bought compliance theater, not compliance.
2. **Check whether the rule is actually holding before deciding it is too strict.** Five
   minutes of grounding inverted the filing's premise and made the damage 3× worse than
   reported. Grounding is not a gate you pass; it is where the real problem is found.
3. **When every single-lever fix scores about the same and none scores well, the root cause has
   more than one head.** The clustering *was* the diagnostic signal, not a close call.
4. **Fusing permission to discipline in one verb guarantees that widening the first will
   corrupt the second.** A reusable design smell, well beyond this module.
5. **A relief valve with no signal is worse than a hard failure.**
6. **The module had already solved this once** — *Personalized extraction* is the same
   amendment shape, already argued and shipped. Finding the precedent beat building the
   argument.

## What became of it

The session's Step 0 filed
`factory/cycles/10-signal-integrity/filings/2026-08-20-093000-para-write-path-single-door-wrong-shape.md`.
That filing carried the **symptom** — the write-path shape — and not RC-A or RC-B. Cycle 10's
answer was the **container model** (build-B10-10): a second named surface, which is Loop 3 of
`ST-2`'s diagnosis running one more turn. The analysis above never entered the factory record,
and the same ground was re-derived independently on 2026-08-25.

**RC-A and RC-B are not retired.** `ST-2` reaches the same territory from a different angle and
supersedes neither: it finds that location is used as a **proxy for trust** (a sharper statement
of RC-A) and adds the process cause that explains why RC-A survived. Read them together; where
they disagree, `ST-2` is later and better grounded, and says so at its own §Where this differs
from ST-1.
