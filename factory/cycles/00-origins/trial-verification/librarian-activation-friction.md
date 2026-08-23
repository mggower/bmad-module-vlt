# Librarian Persona & Partner Disciplines — Verification Notes

_Friction specific to the **Librarian partner** (`/vlt-agent-librarian`) — its persona, activation ritual, proactive-upkeep reflex, and session-ownership duties — observed on the `vlt-core` vault, 2026-06-03. For module iteration. Sibling to `librarian-ingest-friction.md` (which covers the `vlt-ingest` *operation*); these notes are deliberately about the **partner layer**, not the op. Parallel to `researcher-activation-friction.md`._

Activation and the partner disciplines worked well, and notably **better than the Researcher's cold start** — because by this activation the Librarian already had a populated `thread.md` from an earlier sitting, so the warm-thread opening the persona prescribes actually executed. The friction below is concentrated in **partner-switch-within-one-conversation** mechanics (the persona assumes a fresh user summon) and **fresh-vault baselines** for the upkeep reflex. Ordered by impact.

## 1. Session-ownership breaks when partners hand off *within a single conversation*

The operating contract's session-ownership rule states "one conversation yields **one session note** plus N operation log entries." But this conversation involved a deliberate **Researcher → Librarian hand-off mid-conversation**, so it produced **two** session notes (`...-research.md` and `...-ingest.md`) — one per partner sitting. I judged that correct (two partners did genuinely separate work, each owns its record), but it **directly contradicts the contract's stated invariant**. The rule is written for single-partner conversations and has no provision for an intra-conversation partner switch.

This is the single most load-bearing ambiguity in the partner layer: the whole roster premise is that multiple partners share one vault and can hand off, yet the session-accounting rule assumes one partner per conversation.

**Suggested fix:** amend the session-ownership rule to "one **partner sitting** yields one session note" and define a sitting as bounded by a partner switch — so a conversation with a hand-off correctly yields one note per partner. Name the hand-off explicitly as the boundary event. (See `partner-handoff-friction.md §1` for the session-boundary decision from the other side.)

## 2. Activation assumes a *user* summon, but I was invoked by another *partner*

The activation ritual ends "**Greet the user** as the Librarian, oriented to the collection's state." But I wasn't summoned by the user — I was invoked by the **Researcher's** hand-off (a `Skill` call carrying task args). So "greet the user" was slightly wrong: the user didn't call me, a partner did, and what I owed was *orientation to the handed-off task*, not a fresh greeting. I oriented to the task and reported, which felt right, but it deviated from the literal ritual.

**Suggested fix:** add a partner-invoked branch to activation — "If invoked via a hand-off from another partner (task args present) rather than a direct user summon, acknowledge the hand-off and orient to the task; reserve the fresh greeting for a direct user activation."

## 3. The four state reads are largely redundant on a same-conversation re-activation

Activation mandates four state reads (index, log, backlog, own thread). But I had **already read index/log/backlog minutes earlier as the Researcher in this same conversation** — they were still fresh in context. Re-reading them as the Librarian was ritual-compliant but duplicative; only my own `thread.md` (partner-specific) genuinely needed reading. On a partner switch within one conversation, three of the four reads re-fetch unchanged state.

**Suggested fix:** non-blocking — note that on a same-conversation partner switch, the *shared* reads (index/log/backlog) can be trusted from context if still fresh; only the **partner-specific thread** must always be re-read. Keeps the ritual honest without paying for redundant reads.

## 4. The proactive-upkeep / lint-cadence heuristic has no fresh-vault baseline

My SKILL says to notice when upkeep is due — "e.g. several ingestions since the last lint" — and file a `maintenance` item. But **no lint has ever run** on this vault, so "since the last lint" has no baseline, and "several ingestions" is undefined (is 2 several?). I judged upkeep **not** due and filed nothing — a defensible call, but a pure guess against an undefined threshold. Same fresh-vault-edge family as the missing-`log.md` finding in `librarian-ingest-friction.md §2`.

**Suggested fix:** give the cadence reflex a concrete baseline — e.g. "treat the vault's creation as the implicit last-lint date; suggest a first lint once the wiki reaches N pages or M ingestions, whichever first." Replace "several" with a number the partner can actually evaluate.

## 5. A carried thread item can sit "undecided" indefinitely with nothing forcing closure

My `## Thread` carried an open item from the *prior* Librarian session — "undecided: whether to file the missing-`log.md`-scaffolding finding to `{backlog}` as `maintenance`." This sitting I **re-noted it again without resolving it**. The thread faithfully preserves open items, but nothing in the discipline pushes a perennially-"undecided" item toward a decision; it can accrue as permanent thread debt across sessions.

**Suggested fix:** non-blocking — consider a light convention that a thread item carried unresolved across ≥2 sessions should either be decided or promoted to `{backlog}` (where it's at least tracked in the shared evolution intake rather than siloed in one partner's thread). Surfaces stale decisions instead of letting them drift.

## 6. User-level tool preferences are siloed in the *summoning* partner's Bond, invisible to me

The user's Tavily preference was recorded by the Researcher in the **Researcher's** `## Bond` (and global memory). My Librarian `thread.md` has no record of it — I only knew it because the Researcher **manually relayed it in the hand-off args**. If the user summoned me *fresh* next session, I would not know the Tavily preference. A *tool/workflow* preference is **user-level, not partner-level**, but the per-partner thread design silos it in whichever partner first heard it.

This is the mirror image of `researcher-activation-friction.md §6` (where to put workflow prefs), now seen from the receiving partner: the answer "put it in Bond" *fails across partners* because Bonds don't share.

**Suggested fix:** give standing user-level **tool/workflow preferences** a *shared* home (vault config, or a shared preferences note in `_agent/`) that every partner reads on activation — distinct from the per-partner relationship `## Bond`. Reserve `## Bond` for genuinely relationship/partner-specific understanding.

## What worked well (for balance)

- **The warm-thread opening executed — and the contrast with the Researcher's cold start is instructive.** Because a prior Librarian sitting had populated the thread, activation surfaced a real carried item ("undecided: missing-log.md maintenance") exactly as the persona intends. Same ritual, opposite outcome from the Researcher's empty-thread first run — strong evidence the thread mechanism delivers once there's anything in it.
- **"Single writer of canonical wiki pages" is a clean, load-bearing identity.** Receiving a hand-off and being *the one* who files it made the roster division of labor feel real — the Researcher built knowledge, I owned the canonical write. No overlap, no ambiguity about who writes the wiki.
- **The custodial reflexes fired correctly** — near-duplicate check, supersession discipline, index hygiene all came naturally from the persona framing without needing the op to prompt them.
- **Separating the trial-verification layer from the knowledge layer held up** — I kept these friction docs out of the `{log}` taxonomy and ingest pipeline, consistent with the prior session's stance. The boundary is intuitive to maintain.

---

_Net: the Librarian persona is solid and its warm-thread activation visibly outperforms a cold start — the design works once the thread is seeded. The real friction is that the partner layer is written as if **one partner = one conversation**: session-ownership (§1), user-vs-partner invocation (§2), redundant state reads (§3), and siloed tool preferences (§6) all break or blur the moment partners hand off within a single conversation — which is the roster's whole reason to exist. Plus two fresh-vault-baseline gaps (§4 lint cadence, and the carried-item drift in §5). None broke anything; all are cheap to specify._
