# Work state has no complete slot on the corpus, and a claim has no address — so the thread keeps what the artifact cannot

_Filed 2026-10-06 by the **factory**, from an owner problem-solving session contrasting the module
with an external partnerless vault kit (`bmad-cis-problem-solving`; session artifact gitignored).
Evidence is module source at `d3111e0` (v0.19.0), read-only, plus the external kit read in source.
Kind: `candidate`. Cause: **`ST-10`** (`factory/studies/ST-10-continuity-is-actor-held-by-default.md`,
causes B and C) — cited, not restated. Owner elected to file, and ruled the three mechanisms
below stay **one filing** (one convention bump, one spike). **A spike is owed before any brief.**_

## The claim

Three kinds of working knowledge a knowledge role needs between sessions have no finished home on
the artifact, so the module's only fallback — the partner's thread — holds them:

1. **How far a source has been read.** Not recorded anywhere.
2. **What is still unknown.** Recorded in three places, none with an id an answer can close.
3. **What exactly was claimed, and how two claims relate.** A claim is a bullet with a source and
   no address; the only typed relations are *contradicts* and *supersedes*, as callouts.

## Grounding (module source, `d3111e0`)

- **No reading-depth field.** A research note's frontmatter (`skills/vlt-research/SKILL.md:59–72`)
  is `type`, `created`, `title`, `author`, `trust`, `topic`, `status`, `sources`, optional
  `revisit_after`. `status` is `draft | in-progress | complete` (`frontmatter.md:107`) — the
  state of the *note*, not of the *reading*. `revisit_after` records graduation candidacy, a
  different question.
- **Unknowns: three homes, no ids.** (a) backlog `knowledge-gap` — *"a topic the vault is thin
  on"* (`frontmatter.md:290`), one line, topic-level; (b) a research note's **Open Questions**
  section (`skills/vlt-ingest/SKILL.md:102`); (c) a contradiction callout's `open | adjudicable`
  disposition (`wiki-supersession.md:88`). None carries a permanent id; none is closed by a link
  to what answered it; nothing connects a per-note question to the backlog line about the same gap.
- **The thread duplicates (a).** The Researcher reads `knowledge-gap` items at Beat 2
  (`skills/vlt-agent-researcher/SKILL.md:25`) and is also told to write *"the open questions
  still live"* into `thread.md` at sitting end (`:58`).
- **Claims have a source and no address.** Wiki page sections (`skills/vlt-ingest/SKILL.md:160`):
  *"**Key Facts / Claims** (each with its source)"*. `vlt-query` cites the page (`:33`). A search
  of `skills/` for block ids, a typed-relation syntax, or an evidence-quality field returns
  nothing.
- **Two of five relations exist, as callouts.** `wiki-supersession.md:27–42` (claim-level
  supersession, reasons `updated | contradicted | refined | retracted`) and `:77–97`
  (contradiction with disposition). *Supports*, *extends*, and *special case of* have only an
  untyped wikilink "with a note on each relationship" (`vlt-ingest:102`).

**No set was observed.** This filing rests on convention and skill text. No `{field-vault}`
thread, research note, or wiki page was sampled; whether real threads hold the state the skills
instruct them to hold is **unverified** and is the first thing capture should ground.

## The external contrast (read in source, `seanathon/vault-starter` @ `fef0118`)

- `processing: captured → processed → connected → synthesized` on each source record, advanced
  only by the skill that did the work.
- `00-meta/questions.md`: ids permanent and never reused; a question closes by moving to
  *Answered* with the answering link; capture and deepening stamp `answers: [Q<n>]`.
- One claim per bullet, own words, ending in an idea-named block id never renamed once linked.
- Five typed inline relations, closed vocabulary, written on the newer note, inverses derived; a
  sixth only after a documented need recurs three times.
- **The warning in its own source:** its deepening skill records an audit that found 30 of 33
  processed records with no claim anchors, and added a gate. The kit ships no checker.

## Why it matters

- **Until these slots exist, a role cannot leave actor memory without losing state** — this
  filing is the precondition for `2026-10-06-120300`.
- **An unaddressed claim cannot be cited, contradicted, or traced** (`ST-10` cause B). The wiki
  has those properties per page; the unit that carries meaning is smaller than the page.
- **A second register would breach single-home.** The unknowns already have homes; the work is
  ids and closing links on them, not a fourth place.

## Candidate shape (ideation rules)

1. **A reading-depth ladder on research notes** — a controlled field, advanced by the op that
   earned the rung, distinct from `status`. Legacy notes carry no value and are legal
   (coexistence, not migration).
2. **Ids and closing links on the homes unknowns already have.** Give `knowledge-gap` backlog
   items a permanent id and a closing form that names the answering note or page; let a research
   note's Open Questions cite that id. **No new register.** Retire the Researcher's `:58`
   "open questions still live" thread clause in the same build (precedence by elimination — the
   thread's population is narrowed, not ranked against the backlog).
3. **An address per claim** — a block id on each *Key Facts / Claims* bullet of a wiki page,
   idea-named, stable once linked. Additive: an unanchored legacy bullet is cited at page level
   and said to be.
4. **A small closed set of typed relations** that subsumes the two callouts rather than sitting
   beside them — the vocabulary and its growth rule in one convention.
5. **The checker ships in the same build or the convention does not ship** — a `vlt-lint` check
   for anchors on new claim bullets, keyed on something a scanner can see in the bytes (the
   Cycle 16 A16-2 lesson: never a rule whose legality depends on write date).

## The spike owed (before any brief)

Read the kit's `deepen` and `synthesize` skills against **one** `{field-vault}` topic with three
or more sources, and answer: (i) does claim-anchoring survive the single-writer wiki rule, or
does every anchor become a Librarian hand-off; (ii) what does that hand-off cost per source;
(iii) do block ids survive `vlt-lint`'s reconciliation writes and the consolidation convention's
page merges; (iv) which conventions bump — `frontmatter`, and whether `extraction`,
`wiki-supersession`, `wiki-consolidation` re-ack.

## Acceptance (draft)

- **Ship-verifiable:** the depth field in `frontmatter.md` with its enum and its legacy posture;
  the `knowledge-gap` id and closing form in the backlog schema; the claim-anchor rule in the
  wiki page shape; the relation vocabulary single-homed; the lint check passing a conforming
  fixture and failing a non-conforming one, with a fixture on **both** sides of each read;
  handshake bipartite-consistent after the bump.
- **Field-contingent:** one `{field-vault}` ingest producing anchored claims end to end; one
  `knowledge-gap` item closed by a link; a first full lint reporting anchor coverage with its
  denominator.

## Related filings

`2026-10-06-120000` (the shaped answer — consumes the claim addresses);
`2026-10-06-120300` (the lens cut — blocked on this filing);
`2026-09-09-160100` (the Beat 1 budget — its `demote` verb is the path by which thread state
reaches these slots).
