# The backlog's `knowledge-gap` addresses work to a partner through a rail that has no recipient and no drain — so it is never picked up

_Filed 2026-08-14 from **vlt-core** (single-user vault, ~14 months). Classification: **defect**.
Companion to `2026-08-14-180949-relay-requires-a-path-for-traffic-that-has-no-doc.md` — same mint,
applied together, and the two fixes only make sense side by side (this one routes work onto the rail
that one repairs)._

## The claim

`{conventions}/frontmatter.md` defines the kind as:

> `knowledge-gap` — a topic the vault is thin on; **a cue for the Researcher**.

That sentence addresses work to a specific partner. **The backlog it addresses it into has no
recipient field, no drain, and no pickup loop.** `by:` records who *filed*, never who *acts*. So the
address exists in the prose and nowhere in the mechanism, and the work is never picked up.

## Evidence

Measured in vlt-core at mint time:

- `_agent/backlog.md` is **162 KB — 85 open items / 34 done**. Of the open, **33 were
  `knowledge-gap`** (20 `capability-gap`, 31 `maintenance`).
- The surface is not missing on paper — that was the first hypothesis and it was wrong. The operating
  contract's Beat 2 (orient) *and* every partner SKILL.md mandate reading "the **open items** in
  `{backlog}`" on activation, and the Researcher's Beat 2 calls out `knowledge-gap` **by name**. The
  read is specified. It just isn't bounded, and there is nothing to pick up *with*.
- The bounds Beat 2 applies elsewhere are careful and explicit (`{index}` **section headings** only;
  the **last 5** `{log}` entries; `## Thread` only, not `## Set aside`) — with a measured
  justification for each. **`{backlog}` is the one item in that list with no bound at all**, and it
  is the one that grows monotonically with vault age. On a one-year vault "the open items" is 85
  entries in a 162 KB file.
- Meanwhile the same vault's partners had **already routed identical work through `vlt-dispatch
  relay`** — where it drained reliably (see the companion filing: ~8 pathless `ask` relays, nearly
  all to the Researcher, all checked off). Two rails for one job; the one with a drain won, off-spec.
- **The shipped `vlt-mint/assets/partner-agent-template.md` propagates the defective reflex** — every
  future minted partner is born filing addressed work into the unaddressed rail.

## The local fix (applied; proposed upstream) — "the address rule"

> A noticed gap goes to `{backlog}` only when the filing partner does **not** know whose turn it is;
> when it does, the gap is **relayed to that partner** (`vlt-dispatch relay`, shape `ask`).
> The backlog is **evolution intake, not a shared to-do list** — it holds the unassignable.

Three guards were written in alongside it, each closing a way the rule can be misread:

1. **It binds every `kind`, not just `knowledge-gap`** — an addressed `maintenance` item is a relay
   too. It is a rule about *address*, not about subject.
2. **Self-addressed work is not a relay.** A partner noting its own future act in its own lane (the
   Librarian filing upkeep it will run itself) still files to backlog — a partner does not relay to
   itself, and the rail exists to cross a partner boundary. "Addressed" means *addressed to someone
   else*. Without this, a literal reading produces librarian→librarian relays.
3. **Migration is one-home.** An item that later acquires an owner is relayed **and struck** from
   `## Open` (to `## Done` with `[resolved: relayed to <partner>]`), never left in both rails.

## The limit, written into the convention rather than left implicit

Relay **does not schedule work**. Measured at mint time: 7 open pointers, oldest **27 days**
(`chess-coach → creative`, 2026-07-18). That age tracks *time since that partner was last summoned*,
not neglect by the rail — a partner that is not summoned does not drain.

The rule therefore carries a *What this rule does not claim* paragraph stating that it buys an
**address and a drain** — which the backlog has neither of — and **not execution**. This is
deliberate: without it, the obvious misreading is that moving items onto the bus makes them happen,
and the next person to measure a stale slice will conclude the rule failed when it did exactly what
it claimed. **If the module takes this rule, please take that paragraph with it.**

## Consumer walk — where the retired rule was actually encoded

Worth reporting because two of these are shipped skills already improvising around the defect:

- **`vlt-lint`** — `references/fix-and-file.md` routed **every** `adjudicable` contradiction to
  backlog, splitting only on `maintenance` vs `knowledge-gap`. But an adjudicable contradiction names
  *the bounded act that would close it*, which usually names **whose act it is**. And this vault's own
  2026-07-25 full lint had **already** deviated — it relayed four adjudicable contradictions to the
  Researcher instead of filing them. The skill's spec and the skill's practice had diverged before
  anyone noticed. Now routed by address (needs an external source → relay to Researcher; the vault's
  own pages settle it → `maintenance` to backlog; nobody can say what closes it → `knowledge-gap` to
  backlog). Also the SKILL.md standing rule at line 59.
- **`vlt-ingest`** — both filing sites: the declined-proper-noun drain (Step 5) and the
  `adjudicable` contradiction disposition (which explicitly calls itself "the write-side counterpart
  of `vlt-lint`'s Step 4", so the two must move together).
- **All 8 partner SKILL.md files** shared one boilerplate sentence (`**file it to {backlog} and say
  so in-flow**`) — a single-point edit reached all of them, which suggests the module should own that
  sentence in one place rather than copying it per partner.
- **`vlt-mint/assets/partner-agent-template.md`** — the leak into every future partner.
- The Researcher's Beat 2 bullet now points at its **dispatch slice** for addressed gaps.

Locally this was `frontmatter` **5 → 6** with the full consumer walk (`vlt-ingest`, `vlt-extract`,
`vlt-research`, `vlt-lint`, `vlt-mint`, `vlt-dispatch` all re-pinned to `frontmatter@6`).

## Result of the one-time triage

Of the 33 open `knowledge-gap` items (one was mis-tagged), **23 were addressed** to the Researcher
and **10 stayed** — 2 are the Researcher's own notes-to-self (self-addressed, guard 2 above), 1 is
blocked by *access* rather than evidence, and the rest are the Librarian's own lane or genuinely
structural ("the fantasy cluster has no dynasty lens"). The 23 were **consolidated into 9 asks**
rather than dumped as 23 pointers — nine of them were the same roster lookup against
machine-transcribed sources, four were one critical-AI research push — and relayed as a single
stakes-ordered batched `ask` block. Backlog went **85 → 62 open**, `knowledge-gap` **33 → 10**.

The consolidation is worth noting as a pattern: **a backlog accumulates items one filing at a time,
so it never sees that nine of them are one act.** The triage that moves items onto an addressed rail
is the moment that becomes visible.

## Provenance guess — marked as a guess

Guessing: "a cue for the Researcher" reads like it predates `vlt-dispatch` existing at all — i.e.
when it was written, the backlog *was* the only cross-partner surface, and the sentence was accurate.
Dispatch then arrived with a recipient and a drain, and nothing went back to re-home the addressed
half of the backlog. If that is right, the general lesson for the module is that **the backlog's
scope was never narrowed when the bus was added**, and this filing is one instance of a wider
un-narrowing. I have not checked module history to confirm any of this.

## A standing divergence this vault now carries

Both this and the companion fix were applied as **base edits**, not overlays — an overlay can only
*add*, and both of these *change an existing rule*, so neither has an overlay form. vlt-core
therefore carries a base divergence against `_meta/conventions/frontmatter.md` (and local edits to
`vlt-dispatch`, `vlt-lint`, `vlt-ingest`, `vlt-mint`'s template) until the module accepts or rejects
them. `vlt-lint`'s base-divergence net will flag it, correctly, in the meantime.
