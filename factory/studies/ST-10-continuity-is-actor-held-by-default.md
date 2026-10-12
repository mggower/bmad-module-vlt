---
id: 'ST-10'
slug: 'continuity-is-actor-held-by-default'
title: 'Continuity is actor-held by default: a partner is the only place the module gives a role to remember anything, so roles whose subject is the vault itself keep corpus state in a persona — one remove from the thing it describes, with no address, paid at wake time in proportion to history rather than at query time in proportion to relevance'
status: 'standing'
opened: '2026-10-06'
opened_by: 'owner problem-solving session (bmad-cis-problem-solving, 2026-10-06, autonomous) contrasting the module against an external partnerless vault kit — reached one cause and a fix shape; opened on the owner''s go'
session: '_output/problem-solution-2026-10-06.md (gitignored — provenance only, never load-bearing; this study is self-contained)'
causes:
  - 'Primary A: the module has ONE home for a role''s continuity — partner memory. Statefulness arrives with the actor, uniformly, so nobody asks what a given role''s continuity is ABOUT. Where it is about the owner and a practice (a coaching loop), a partner is the right home: there is no corpus for it to live in. Where it is about the vault (what has been read, what is half-processed, what disagrees with what, what is still unknown), it is corpus state, and filing it in a persona stores it one remove from its subject, where it goes stale and must be groomed.'
  - 'Primary B: actor-held continuity has no address. A line in `thread.md` or `## Self` cannot be cited, contradicted by a source, superseded, or traced to where it entered — the properties the module built for the wiki (sources, supersession callouts, trust rungs) and withheld from the one layer that loads as instruction. Its cost model is also inverted: it is paid on every activation in proportion to the role''s history, where corpus state is paid at the moment of a question in proportion to relevance.'
  - 'Enabling C: the corpus''s slots for work state are partial, and where one exists the partner is told to keep a copy anyway. A research note carries no reading-depth state; the unit of citation is the page, so a claim has no address and a relation between two sources has no edge beyond the contradiction and supersession callouts. Unknowns DO have corpus homes — the backlog''s `knowledge-gap` kind (topic-level, one line), a research note''s Open Questions section, a contradiction callout''s disposition — but none carries an id an answer can close, and the Researcher''s sitting-end instruction still writes "the open questions still live" into its thread. So the default is two things at once: an absence of slots for some state, and a duplicate of the slots that exist.'
  - 'Contributing: the return path is the thinnest shipped surface. The skill that answers from the vault is ~1.0K words against ~18.8K for the skill that checks it, and its answer has no fixed shape. A corpus that is rarely consulted cannot show that it could have carried the continuity, so the partner keeps looking like the only thing that remembers.'
cited_by:
  - 'factory/inbox/2026-10-06-120000-the-answer-from-the-vault-has-no-shape.md (contributing cause — the shaped answer; independent, no convention bump)'
  - 'factory/inbox/2026-10-06-120100-work-state-has-no-complete-slot-on-the-corpus-and-a-claim-has-no-address.md (causes B + C — reading depth, ids on the homes unknowns already have, claim addresses, typed relations; spike owed)'
  - 'factory/inbox/2026-10-06-120200-structure-is-not-earned-and-the-unlock-rule-is-practised-but-unstated.md (cause A — the recurrence question at mint and the birth posture; the unlock rule''s population is a 3-of-76 sample, unclassified)'
  - 'factory/inbox/2026-10-06-120300-the-archetype-cut-exists-and-no-memory-posture-hangs-on-it.md (cause A — the lens cut; filed held, blocked on 120100 and the Researcher pilot)'
  - 'factory/inbox/2026-10-12-100000-the-memory-posture-has-no-always-read-carrier.md (defect — the posture the Researcher pilot depends on has no always-read carrier; filed so the pilot''s result is gradable)'
superseded_by: ''
---

# ST-10 — continuity is actor-held by default

## The claim

`ST-8` found that a partner's always-read memory has no budget and no owner-side author, and
Cycle 16 shipped the repair: a Beat 1 budget, a charter, a `demote` verb, a casebook, a cold
summon, a named partnerless sitting. The owner's doubt about the partner model outlived that
repair. This study names why: the repair **bounded** partner memory without asking, role by
role, whether the thing being remembered should be actor memory at all.

The module has exactly one place where a role can keep continuity between sessions — the
partner's memory files. So every role that needs continuity becomes a stateful actor, and every
kind of continuity lands in the same files regardless of what it is about. For the knowledge
roles, most of it is about **the vault**: which inquiries are open, where the last lint landed,
which pages to watch. That is state of the corpus. Held in a persona it has no address, costs
on every wake, and drifts from the thing it describes. Held on the corpus it would be
greppable, citable, and free until relevant.

`ST-8` is the budget question. This is the prior one: **the home question.**

## The evidence — module source at `d3111e0` (v0.19.0), read-only

**1. The shipped partners' own thread instructions describe corpus state.**

- Librarian, sitting-end write (`skills/vlt-agent-librarian/SKILL.md:55`): *"Update `thread.md`
  — `## Thread` movement: what's drifting and worth watching, where the last lint landed, pages
  to watch."* Every item is a fact about the wiki. None is a fact about the relationship.
- Researcher, sitting-end write (`skills/vlt-agent-researcher/SKILL.md:58`): *"the open
  questions still live, the stances you took, what the user is circling or resisting."* The
  first clause is corpus state; the rest is relationship state. The file mixes two kinds with
  one home and one read cost.
- The Researcher's persona states the opposite principle (`:10`): it becomes itself by reading
  *"the rules you obey, the state of the knowledge, and your running inquiry with this user —
  all of which live in the vault itself."* The intent was vault-held continuity. The mechanism
  that shipped holds it under `{partners}/`, where only that partner reads it.

**2. The corpus's slots are partial — and duplicated where they exist.**

- A research note's frontmatter (`skills/vlt-research/SKILL.md:59–72`) carries `type`,
  `created`, `title`, `author`, `trust`, `topic`, `status`, `sources`, and an optional
  `revisit_after` (graduation candidacy) — nothing that says how deeply a source was read or
  whether the note has been connected to anything.
- Unknowns have three corpus homes already: the backlog's `knowledge-gap` kind — *"a topic the
  vault is thin on"* (`frontmatter.md:290`), a research note's **Open Questions** section
  (`skills/vlt-ingest/SKILL.md:102`), and a contradiction callout's `open | adjudicable`
  disposition (`wiki-supersession.md:88`). None carries a permanent id, and none is closed by a
  link to the thing that answered it. And the Researcher already reads the backlog's
  `knowledge-gap` items at Beat 2 (`skills/vlt-agent-researcher/SKILL.md:25`) **and** is told to
  keep "the open questions still live" in its own thread (`:58`) — the same fact, two homes,
  one of them private.
- The unit of citation is the page. `vlt-query` cites `[[page]]` (`skills/vlt-query/SKILL.md:33`)
  and a canonical page's claims sit in a *Key Facts / Claims* section with a source each
  (`skills/vlt-ingest/SKILL.md:160`) but no per-claim address. A search of `skills/` for block
  ids, typed relations, or an evidence-quality field returns nothing.

**3. The ladder already half-knows.** The promotion ladder's last rung
(`vault-operating-contract.md:242`) is *"wiki — shared knowledge leaves partner memory"*, and
`demote` (`:246`) moves material *"from partner memory to the wiki by Librarian hand-off."* The
contract concedes that some partner memory belongs on the corpus. But the wiki is the only
corpus destination it names, and wiki pages are for durable shared *knowledge* — not for
*work state* (open, half-read, to-watch). Work state has no destination, so it stays.

**4. The weight map and the role map coincide.** `ST-8`'s 2026-09-09 measurement put the three
shipped knowledge partners among the four heaviest of nine at Beat 1 (Librarian ~19.3K words,
Creative ~16.4K, Researcher ~9.2K), and five of six minted practice partners between ~4.4K and
~7.8K. `ST-8` read that as *the model fails at weight, not at concept*. Read by role it says
something narrower: the model is heaviest exactly where the role's subject is the vault.

The module already draws this line and attaches nothing to it. `skills/vlt-mint/SKILL.md:55`
distinguishes *horizontal* partners — *"**function** partners (librarian / researcher /
creative) defined by a mode of work that spans domains"* — from *vertical (domain)* partners
that most often run *"the **longitudinal loop**"*. The archetype decides which hand a partner
wears. It does not decide whether the partner is stateful: both archetypes get the same memory
files and the same `memory: full` default (`:132`).

**5. The proportion of the return path.** `skills/vlt-query/` is one file, ~1.0K words.
`skills/vlt-lint/` is nine files, ~18.8K. Word count is a proxy and is offered as one. But the
cycle themes from 10 through 16 are all about whether the machinery reports honestly; none is
about what the owner gets back from a question. (`vlt-query:34` does ask for contradictions to
be named — ranked by recency and source count — and for edges to be flagged; it fixes no output
shape for either.)

**6. The pilot that would test this is on the books and unrun.** Cycle 16 shipped
`memory: reflexes` as a per-partner posture (`vault-operating-contract.md:196`) with the
Researcher as its pilot. The cycle roadmap's pass-4 record
(`factory/cycles/16-closed-loops/roadmap.md:1878–1885`) finds the flip has not been made in
`{field-vault}` and none of its five post-flip dives has run.

### The external contrast — a partnerless kit, read in source

`github.com/seanathon/vault-starter` at `fef0118` (MIT; one commit, 2026-09-27), plus its
author's launch article. It is evidence for one thing only: **that the knowledge roles can be
run with no actor memory at all**, because every piece of continuity they need has a slot on
the corpus.

| Continuity the role needs | Where the kit puts it | Where the module puts it |
|---|---|---|
| How deeply has this source been read? | `processing: captured → processed → connected → synthesized` on the source record | the partner's thread |
| What is still unknown? | `00-meta/questions.md`, permanent ids, closed by a citing claim | the backlog's `knowledge-gap` line, per-note Open Questions, **and** the partner's thread — no ids, no closing link |
| What disagrees with what? | a typed inline field on the newer note (`contradicts::`), five relations, closed vocabulary | prose in a page section; supersession callouts for two of the five |
| What exactly was claimed? | one bullet, own words, a block id (`^claim-<idea-slug>`), citable as `[[Source#^claim-slug]]` | a bullet with a source, no address |
| What does the agent remember about itself? | nothing; a ~660-word root contract and skills read on demand | `identity.md`, `thread.md`, `reflexes.md`, `casebook.md` |

Three mechanisms in the kit bear on the cause rather than on taste:

- **Structure is earned, and the refusal names its unlock.** A topic hub needs three sources;
  below that the skill declines and says what would clear it. The same number gates promoting a
  claim to a concept and adding a relation type.
- **The answer has a fixed shape.** Answer first; grounds cited to claims; tensions stated as
  open choices; gaps that become the next capture. All reading completes before any conclusion,
  and freshly read material gets no extra weight.
- **The contract says which half is the product.** Its pipeline page: *"A corpus nobody queries
  is a cost."*

What the kit is **not** evidence for:

- That partners are unnecessary. It has no longitudinal loop of any kind — nothing like
  `vlt-track`. It is silent on the practice partners.
- That its rules hold unenforced. Its own deepening skill records an audit that found 30 of 33
  processed records carrying no claim anchors, and added a gate in response. Prose rules
  without a checker fail there as they do here.
- Durability. One commit, days old. Its usage counts are the author's own, from a launch
  article; no step of this diagnosis depends on them.

Its reading here is a contrast case, not a harvest. A brief that borrows a mechanism from it
owes a spike over the actual skill files first (`factory/platform/spikes/README.md`).

## The causal chain

The owner doubts the partner model after its budget repair → because the knowledge partners are
still the expensive, drift-prone way to do knowledge work, and a partnerless sitting is still
the productive one (`ST-8` observation 9) → because those partners carry state that is about
the vault, and vault state changes whether or not that partner was the one who changed it, so
the thread is stale by construction and has to be re-read, re-reconciled, and groomed → because
the thread is the only place that state can go (cause C) → because continuity was designed as a
property of the actor (cause A), at a time when partners were the only actors (`ST-8` cause C,
the same origin).

And the loop that hides it: R1 — the partner remembers the corpus → the owner asks the partner
rather than the corpus → the corpus's own return path stays thin → the partner's memory looks
indispensable. Each turn makes the default look like a requirement.

## Rejected alternatives

- **"This is `ST-8` with more evidence."** `ST-8`'s causes are *no budget* and *no owner-side
  author*; both are properties of partner memory and both were repaired inside it. This cause
  is upstream of the file: a budgeted, chartered, groomed thread that says "where the last lint
  landed" is still the wrong home for that fact. `ST-8`'s own prediction — any fix that leaves
  the ladder one-way is re-eaten by growth — is refined, not replaced: a two-way ladder whose
  only corpus rung is the wiki still has nowhere to put work state.

- **"Retire the partner model."** Refuted by the same control group `ST-8` used, and by the
  contrast case's silence: nothing examined here runs a longitudinal practice without a
  stateful actor. It would also break the durability rule.

- **"Adopt the kit."** Its layout, its single-librarian actor, and its lack of enforcement are
  not what the evidence supports. What transfers is narrower: slots on the artifact for work
  state, an address per claim, and a shaped answer.

- **"The partners are fine; the owner should groom more."** `ST-8` observation 7 already
  refuted groom-as-fix for weight. For this cause it is refuted differently: grooming a thread
  that mirrors the corpus is reconciling a copy against its original by hand.

- **"The heavy partners are heavy because they are used most."** Partly true and not
  separable from the data in hand: the shipped three are also the oldest and most used. The
  role reading is supported by module source (evidence 1 — the thread instructions themselves)
  rather than by the weight table alone; the weight table is corroboration, not proof.

- **"`ST-3` — governance has no addressable projection."** The same word, a different object.
  `ST-3` is about paying for a whole convention when a slice is needed. Here the thing without
  an address is not a rule but a role's working knowledge.

## What this session got wrong, on record

- The first draft said the module's query answers surface no tensions or gaps "by
  construction". Grounding refuted it: `vlt-query:34` asks for both. The true gap is narrower —
  no fixed output shape, and ranking by recency where evidence quality is available.

- The study's first committed text (`0aaea50`) said no convention holds what the vault does not
  yet know. Grounding for the filings refuted it: the backlog's `knowledge-gap` kind, the
  research note's Open Questions section, and the contradiction disposition all do. The
  correction sharpens cause C rather than weakening it — the gap is ids and closing links, and
  the thread duplicates a slot that exists — but a filing written from the first text would
  have proposed a second register beside the backlog, against single-home discipline.

- The same pass found the module's own horizontal/vertical archetype split (`vlt-mint:55`),
  which the session had re-derived from an outside kit as if it were new. The cut exists; what
  is missing is anything that hangs statefulness on it.

- The session treated the Creative as a knowledge role alongside the Librarian and Researcher
  because it is shipped and heavy. Brainstorming is not corpus work and the contrast case has
  nothing to say about it. The Creative's place on either side of this cut is **not established
  here**; it rests on the owner's report about partnerless sittings alone.

- The session ran without owner checkpoints. Nothing in it was tested against the owner's
  experience of *which* remembered things the knowledge partners actually use. Evidence 1 shows
  what the skills instruct the thread to hold, not what a year of threads actually hold; no
  `{field-vault}` thread was read for this study.

- The heaviest practice partner (`ST-8`'s first row) is not explained by this cause. Its weight
  is a casebook and an owner-model filed under `## Bond` — `ST-8`'s diagnosis, unchanged.

## What would close it

Not a fix — ideation rules. The evidence bounds the shape:

- **A second home, completed rather than added.** A slot for how far a source has been read;
  ids and closing links on the homes unknowns already have, not a new register beside them;
  an edge for what relates to what. Until those exist, moving a role off actor memory just
  loses the state — and where a slot already exists, the thread's copy of it is retired.
- **An address per claim**, so that what a role "knows" can be cited, contradicted, and traced
  — the wiki's properties extended one level down. Shipped with its checker or not at all; the
  contrast case's own audit is the warning.
- **A cut by what the continuity is about.** Practice roles keep a stateful partner. Roles
  whose subject is the vault become lenses: persona, charter and reflexes, with continuity read
  from the corpus. `memory: reflexes` is already the posture; `demote` is already the migration
  path; neither destroys anything.
- **A return path with a shape**, so the corpus can be seen carrying the continuity.
- **The cheap test first.** The Researcher pilot costs one frontmatter field and is already
  ruled. This study's own prediction, stated so it can fail: after the flip the Researcher
  loses nothing it needed *that was about the vault*, and what it does miss will be
  relationship-shaped — stances and resistances — which is the part that belongs in a partner.
  If it instead misses corpus facts it had no other way to find, cause C is the binding one and
  the slots come before any role moves.
