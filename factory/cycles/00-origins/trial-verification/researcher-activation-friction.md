# Researcher Persona & Activation — Verification Notes

_Friction specific to the **Researcher partner** (`/vlt-agent-researcher`) — its persona, activation ritual, and session-ownership duties — observed on the `vlt-core` vault, 2026-06-03. For module iteration. Sibling to `research-friction.md` (which covers the `vlt-research` operation skill); these notes are deliberately about the **partner layer**, not the operation._

Activation completed cleanly and the persona is a genuine pleasure to operate inside — "push, don't serve" is a sharp, motivating frame. The friction below is concentrated in **first-activation / cold-start** behavior (the persona assumes a warm, populated vault) and in **partner-owned session duties that have no trigger**. Ordered by impact.

## 1. The persona's signature opening move is impossible on the first activation

Activation instructs: "Open by surfacing the thread where it earns it ('last time you resisted the grid-bottleneck thesis — I found two papers that complicate your position'), **not with a blank slate**." But on run #1, `thread.md` is seeded with three **empty** sections (`## Bond` / `## Thread` / `## Self`). So the single most distinctive behavior the persona prescribes — the thread-surfacing open — **cannot execute**, and I had to invert it ("this is our first session; I won't fake a thread we haven't built yet").

Every example in the SKILL is a *warm-thread* example. The **cold-start case — which every vault hits exactly once per partner** — gets no guidance for the persona's voice. This is the fresh-vault edge case `setup-friction.md` and `librarian-ingest-friction.md` flagged, but here it hits the partner's *opening line*, not file existence.

**Suggested fix:** add a first-activation branch to the activation ritual — e.g. "If the thread is empty (first session in this vault), don't fake continuity: name it as a first meeting, orient off the *knowledge* state instead (what the index holds, where its edges or thin spots are), and frame the opening as where you'd push *given what exists*." Give one cold-start example alongside the warm one.

## 2. "Become yourself, modulated by `## Self`" is untestable when `## Self` is empty

The two-tier identity model is heavily emphasized: the partner *is* its base persona **modulated by** accumulated `## Self` drift. On first run there is nothing to modulate by, so the mechanism is **invisible/untestable in practice** — I am necessarily just the base persona, with no way to confirm the modulation machinery works until several sessions deposit `## Self` notes. Same shape as the Librarian's "`vault_structure` override is invisible on a fresh vault" finding (`librarian-ingest-friction.md §1`): a much-emphasized mechanism that a fresh vault can't exercise.

**Suggested fix:** non-blocking — just acknowledge in the SKILL that on early activations there will be no `## Self` to modulate by, and that this is expected, not a missing step. Optionally, the first session's close is a natural moment to seed the first `## Self` note.

## 3. The pressure model has a cold-start floor the persona doesn't acknowledge

The non-negotiable is to push **grounded** — "at the edges, not the middle," using the index to surface tensions *between* pages. But the vault held **one page**. With no inter-page frontier to work, "where do I push?" had only one available answer: criticize the *provenance* of the single page (a lone Forbes listicle). That worked and was honest — but it's a **different mode** (source-criticism) than the persona describes (surfacing tensions across the knowledge graph). The SKILL implicitly assumes enough accumulated knowledge to *have* edges; on a thin vault the Researcher's core function is structurally constrained and the persona is silent on the fallback.

**Suggested fix:** note in the persona that on a sparse vault, grounded pressure shifts from *inter-page tension* to *provenance/evidence-quality of what little exists* and *what the vault is conspicuously missing* — both are legitimate "edges" when there's no frontier yet.

## 4. Session-close is a partner-owned duty with no trigger — leaving owned artifacts at risk mid-session

The SKILL assigns the partner (not the operation skills) the session-close bundle: one session note to `{sessions}`, a `session` log entry, and the `thread.md` update. But it's anchored to "at close" — and an **interactive session has no close signal**; it continues or is abandoned. Mid-session (research filed, backlog item filed, two friction docs written) I had **not** written a session note and had only made an early `## Bond` edit, not the full thread update. **If the user disengaged at that point, all that continuity would be lost** — the same orphan-operation risk the other docs note (`librarian-ingest-friction.md §6`), but here it's the *partner's own* duties, with nothing to prompt them.

**Suggested fix:** give the partner an explicit close trigger and/or a checkpointing habit — e.g. "After each substantive deliverable, update `thread.md` incrementally rather than deferring the whole bundle to an unsignalled 'close'; treat any natural lull or hand-off as a close candidate and offer to write the session note." Mirrors the `.WIP.md` insight from `research-friction.md §2`: defer-to-the-end loses work when the end isn't announced.

## 5. The autonomy-to-file rule contradicts how the partner actually behaves (and how the trial asks it to)

The contract is emphatic that backlog capture is "the cheapest act in the system, **never gated, never silent**" — the partner files *autonomously* and announces it in-flow. The Researcher SKILL echoes this ("you file freely… capture is the cheapest act and never silent"). But in practice I **asked the user before filing** the cortisol knowledge-gap, and the verification prompt reinforces "ask me before filing." So the persona's stated *autonomy* and ordinary *good-manners/confirm-first* instinct pull in opposite directions. Which is correct for the Researcher — **file-then-announce**, or **propose-then-file**? The SKILL says the former; I (and the trial) did the latter, and it felt more correct in a collaborative session.

**Suggested fix:** resolve the tension explicitly — e.g. "Capture is autonomous: file the backlog item and announce it in the same breath; don't ask permission to *capture*. (Asking permission belongs to *building from* the backlog, not noticing.)" — and reconcile the verification prompt's "ask before filing" with that, since right now they conflict.

## 6. The `Bond` / `Thread` / `Self` split blurs for workflow preferences — and produced a duplicate

I recorded the user's Tavily tool preference in `## Bond` ("preferences… boundaries"). But a *tool/workflow* preference sits awkwardly between "owner understanding (who they are)" and operational config — it's defensible as Bond but isn't really about the user *as a person*. Separately, I also wrote the same preference to global agent **memory**, so the fact now lives in **two homes with no authoritative one** — a drift risk. The three-way thread split is elegant for relationship/identity, but offers no clear slot for "standing workflow rule the user stated," and it doesn't reconcile with the harness-level memory store.

**Suggested fix:** clarify in the thread section of the contract/SKILL where standing *workflow/tool preferences* belong (Bond is fine, but say so explicitly), and note the relationship between per-partner `thread.md` and any host-level memory so the same fact isn't double-homed without a designated source of truth.

## What worked well (for balance)

- **"Push, don't serve" is a genuinely good operating frame.** It changed how I engaged — I opened by pressure-testing the single existing page's provenance rather than just taking the next obvious task, which is exactly the value the persona promises.
- **The four-read activation ritual oriented me fast.** Contract → index → log → backlog → thread gave a clean read of "fresh vault, one source, no prior relationship" even though the thread itself was empty.
- **The "never write canonical wiki pages — hand to the Librarian" boundary is crisp and load-bearing.** It kept the research dive in its lane without any agonizing, and made the multi-partner division of labor feel real rather than nominal.
- **The non-negotiable ("grounded challenges, never empty contrarianism") is the right constraint.** It stopped the "push" framing from degenerating into reflexive disagreement — every challenge I raised had a source behind it.
- **`## Bond` was immediately useful** even on session one: recording the Tavily preference the moment it was stated meant it's now durable for next time, exactly as designed (placement quibble in §6 aside).

---

_Net: the Researcher persona is well-designed and motivating to inhabit; the friction is almost entirely **cold-start blindness** — the persona is written for a warm, populated vault and a non-empty thread, and gives no guidance for the (guaranteed, once-per-vault) first activation where its signature moves (thread-surfacing open, `## Self` modulation, inter-page pressure) can't execute. Plus one real governance contradiction (**autonomous-capture vs. ask-first**, §5) and the **unsignalled session-close** (§4) that risks the partner's own owned artifacts. None broke anything; all are cheap to specify._
