# Candidate: a synchronous partner→partner **consult** channel (the missing half of `vlt-dispatch`)

_Filed 2026-07-25 by the owner, from friction observed in **`vlt-sayari`** (work vault, navigator +
engineer partners in a PM / staff-eng dynamic). Produced by a factory-side ideation session —
`_output/brainstorming/brainstorming-session-2026-07-25-1313.md` (4 techniques: first-principles,
cross-pollination, assumption-reversal, pre-mortem). This is a **candidate** (design gap proposed
for upstreaming), not a defect._

## The friction, as hit in the field

In `vlt-sayari` the Navigator regularly needs the Engineer's judgment *to finish its current move* —
feasibility, blast radius, "will this break the ingest path." Today the vault has two ways to get
it, and neither fits:

- **`vlt-dispatch relay`** routes the question, but **asynchronously** — it appends a pointer to
  `_agent/dispatch.md` and the Engineer drains it on some later turn. The Navigator cannot use it
  mid-thought.
- **`vlt-review-council`** spawns multiple agents, but as **fixed lenses in parallel with no
  cross-talk**, returning a typed verdict. It is a panel, not a partner answering as itself.

So the gap is precise: **a synchronous, conversational, cross-partner consult in which the summoned
partner answers as itself and remembers that it did.** In practice the Navigator either guesses
(claiming authority it doesn't have) or the human hand-carries the question between two sessions.

## Grounding notes (factory-side, checked 2026-07-25)

- `skills/vlt-dispatch/SKILL.md:12–21` — dispatch is declared "the vault's partner communication
  bus… one record with a drain, three modes" (`daily` / `relay` / `ledger`). All three are
  write-and-wait; there is no synchronous channel. **A `consult` mode is a fourth channel of the
  same bus**, which is why this should not become a new skill (single-home discipline).
- `skills/vlt-review-council/SKILL.md:11–13` — the parallel-lens engine, explicitly *not* a
  conversation; lenses are "independent reads — they don't see each other's positions." Its Step-1
  discipline of passing **live absolute paths to ground in** is the pattern a consult payload should
  copy.
- `skills/vlt-dispatch/SKILL.md:21` — "`identity.md`/`thread.md` are per-partner and off-limits."
  A stateful consult *appears* to violate this. **It does not:** the summoned partner is the one
  running, so it writes its own memory — the same self-write the drain loop already prescribes at
  `vlt-dispatch/SKILL.md:225`. Single-writer holds. Any capture should record this, because the
  naive reading blocks the feature.
- One-line framing that survived the session: **a consult is a `relay` whose drain happens
  immediately, in-process, with the answer returned to the caller instead of left on the board.**

## Proposed shape (session output, for the capture to weigh — not a ruling)

- **Surface:** a fourth `vlt-dispatch` mode, `consult`. Not a new op skill.
- **Depth-1, hard.** A summoned partner answers or refuses-and-names; it never summons.
- **Typed return union**, inheriting the review-council idiom rather than returning prose:
  `answer` / `insufficient-context` / `wrong-partner(→slug)` / `needs-human` / `needs-work`.
- **Fat payload** — the question *plus* the live absolute paths the summoned partner must ground in.
- **Read-only except its own memory.** *Consult answers; relay assigns.* If the answer implies work,
  the return is `needs-work` and it exits through the existing async `relay` path.
- **Trail, split across three sites:** the summoned partner's `thread.md` (self-written, and only
  when the consult *changed its stance* — otherwise the prunable file rots), a `{log}` line tagged
  with **both** partners (novel: every existing log line has a single author), and a **pre-checked**
  pointer in `_agent/dispatch.md` (a consult never waited, so it is traffic, not a queue item).
- **Raw answer surfaced, attributed, in its own block** — then the caller's use of it. A digested
  partner voice is an unattributed claim, which is what `vlt-lint` exists to catch.

## Two items that ship independently of the mechanism

1. **A contract prohibition:** *a partner never speaks in another partner's voice; it consults, or it
   cites.* This is the failure mode the mechanism exists to prevent (a partner ventriloquizing
   another's authority) and it is shippable prose with zero machinery. Worth landing even if the
   channel is deferred.
2. **The read-and-cite fallback as documented default:** a partner may read another partner's
   `identity.md`/`thread.md` and cite what it holds. Works today, costs nothing — and it supplies
   the trigger rule for the real mechanism: **spawn only when the interaction should be
   remembered.** Memory is what justifies the consult's cost.

## The governance pairing (the session's strongest finding)

The session's dark horse was **rule-triggered consults**: a handshaked `{conventions}/consult.md`
(carrying `version:`/`consumers:`) declaring artifact **preconditions** — e.g. *a spec authored by a
partner that touches a domain outside its authority requires a consult record before it is filed* —
paired with a `vlt-lint` check for artifacts that claim out-of-authority domain with no consult
record.

This matters for two reasons: it is squarely in the enforcement-arc idiom, and it is the answer to
the module's own **shipped-but-unexercised** scar (capability families). A *required* consult is
exercised by construction. Recommendation for capture: **do not ship the mechanism without at least
planning the convention + lint pairing.**

## Explicitly deferred

- **`dialogue`** (A and B exchange N turns while the human watches) and **`convene`** (true
  party-mode: human + both partners, human addresses either by name). Both are later *compositions*
  of the consult primitive; the field traffic is overwhelmingly single-question. Copying
  `bmad-party-mode`'s roundtable premise would build for the 20% case — and the roundtable already
  exists as `vlt-review-council`.
- **`summon`** (the answer goes to the human, caller overhears) — reduces to running the other
  partner's skill directly. Not a mechanism.

## Known risks the brief must answer

- **Confabulated authority** — a thin payload produces an invented opinion relayed as authoritative.
  Strictly worse than no mechanism, since the read-and-cite fallback cannot impersonate. Mitigated by
  the fat payload and by making `insufficient-context` a first-class, praised return.
- **`thread.md` rot** from unbounded consult appends.
- **Boundary erosion** — the summoned partner starting to *do* work, putting two writers in one turn.
- **Human out of the loop** — two agents converging visibly on consensus while a hedge is lost in
  digestion.
- **Upgrade durability** — any `dispatch.md` shape change is a **B1 preserve-path** question for
  `vlt-setup`/`vlt-upgrade`/merge scripts.

## Provenance

- Vault: `vlt-sayari` (work machine, currently 0.6.0), Navigator + Engineer partner pair.
- Session record: `_output/brainstorming/brainstorming-session-2026-07-25-1313.md` (gitignored).
- Natural home: **Arc 4** — Arc 3 (enforcement) is shipped at v0.7.0 and gated only on closeout.
