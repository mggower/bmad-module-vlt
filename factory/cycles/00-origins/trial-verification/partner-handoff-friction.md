# Partner Hand-off (Researcher → Librarian) — Verification Notes

_Friction specific to the **deliberate hand-off between partners** — the seam where the Researcher passes a finished research note to the Librarian for canonical ingest — observed on the `vlt-core` vault, 2026-06-03. For module iteration. This is its own domain: not researcher-specific, not librarian-specific, not ingest-specific, but the **interface between them**. Sibling to `researcher-activation-friction.md`, `librarian-activation-friction.md`, and `librarian-ingest-friction.md` (which each touch the hand-off from one side; this doc is the seam itself._

The hand-off **completed cleanly and the knowledge flowed end-to-end** — Researcher dive → research note → Librarian ingest → new `cortisol` page + supersededed `ashwagandha` claims. The single-writer contract held: the Researcher built knowledge, the Librarian filed it. But the *mechanics* of the hand-off are almost entirely **unspecified by the module** — every step below was a judgment call I made because nothing told me how the seam should work. Ordered by impact.

## 1. Where does one partner's session end and the next begin? — undefined, and it conflicts with the contract

This was the first and sharpest decision. The Researcher had done substantive work (research, backlog, friction docs); the user then asked for the ingest hand-off. **Does the Researcher close its session before summoning the Librarian, or does the whole conversation stay one session?** I chose: **close the Researcher session, then open a Librarian session** — two sittings, two session notes. That felt right (two partners did genuinely separate work) but it **contradicts the operating contract's "one conversation yields one session note"** invariant (see `librarian-activation-friction.md §1`).

Nothing in either SKILL, the contract, or the hand-off language ("hand the note to the Librarian") says how to slice sessions across a hand-off. A different agent could equally defensibly have kept one Researcher-owned session spanning the ingest — producing a session note whose `partner:` tag misrepresents who did the wiki write.

**Suggested fix:** define the hand-off as an explicit **session boundary**: the handing-off partner closes its sitting (session note + log + thread) *before* invoking the receiving partner, who opens a fresh sitting. State this once, in the contract's session-ownership section, and reference it from both partner SKILLs. Resolves §1 here and `librarian-activation-friction.md §1` together.

## 2. There is no hand-off payload schema — the brief is freeform prose, and context can silently drop

I (as Researcher) packed the hand-off into the `vlt-agent-librarian` **Skill args as prose**: source path, tasks, supersession intent, tool preference. It worked *because I was deliberately thorough*. But there is **no defined hand-off payload** — no schema for what a research→ingest hand-off must carry (the note path, the target concept(s), known supersession targets, the wiki-shaping intent, user preferences to forward). A hurried or headless hand-off could easily omit the supersession targets or the tool preference, and the receiving partner would never know what it didn't receive.

The module documents *that* the hand-off exists (`vlt-research` Phase 6: "hand the note to the Librarian / `vlt-ingest`") but not *what the hand-off contains*.

**Suggested fix:** specify a minimal hand-off payload in `vlt-research` Phase 6 — at least: (a) the research-note path, (b) the concept(s) to create/update, (c) any existing claims the note refines/contradicts (supersession targets), (d) user/tool preferences to forward. A checklist, not a form. Makes the seam robust to a careless hand-off.

## 3. "No partner calls another" (activation) vs. "hand off to the Librarian" (operation) — an unacknowledged tension

The contract's activation ritual emphasizes that each partner orients "**without calling any other partner**" — the four state reads are how the roster stays coherent without inter-partner calls. Yet a hand-off **is** one partner invoking another: as the Researcher I literally called the `vlt-agent-librarian` Skill to switch personas mid-conversation. So the system has two models that aren't reconciled: *orientation* is self-contained (no partner calls another), but *operation* includes a partner summoning another partner.

It worked, but it's conceptually muddy — is the Librarian a fresh persona I *became*, or a separate agent I *called*? In a single-context conversation these collapse to the same thing; in a more decoupled (async/multi-agent) future they wouldn't.

**Suggested fix:** acknowledge the distinction explicitly — "partners orient independently (no cross-partner calls during *activation*), but a deliberate *hand-off* is a sanctioned partner-to-partner invocation that switches the active persona." One sentence resolves the apparent contradiction.

## 4. The handing-off partner over-specified into the receiver's domain (a role-boundary smell)

In my Researcher hand-off brief I wrote: "use inline `[!superseded]` callouts (reason: `refined`)." But **supersession discipline is the Librarian's expertise, not the Researcher's** — I told the single-writer *how to write*. It happened to be correct, but it crosses the role boundary the roster is built on: the Researcher's job is "here is the knowledge and what it complicates," the Librarian's is "here is how it's filed canonically." The hand-off invited me to reach across that line because there's no guidance on *how much filing-intent* a hand-off should carry.

**Suggested fix:** clarify the division in the hand-off spec — the Researcher conveys **what changed and what it complicates** (the supersession *targets* and *why*); the Librarian decides the **mechanism** (callout type, reason code, page structure). The Researcher flags "this refines the ashwagandha cortisol claim"; the Librarian chooses `[!superseded] refined`. Keeps each partner in its lane.

## 5. User-level preferences must be manually relayed through the hand-off, or they're lost

I had to **explicitly forward the Tavily tool preference** in the hand-off args, because I knew (as the Researcher) that the Librarian's thread wouldn't carry it — per-partner Bonds don't share (see `librarian-activation-friction.md §6` and `researcher-activation-friction.md §6`). This worked only because I remembered to relay it. A hand-off that forgets to forward standing user preferences silently strips them at the partner boundary.

**Suggested fix:** the real fix is shared user-level preferences (per the two activation docs) — once preferences live in a shared home every partner reads, the hand-off no longer needs to relay them at all. Until then, make "forward standing user/tool preferences" an explicit item in the hand-off payload (§2).

## 6. The hand-off is fire-and-forward — no receipt, no scope-back

The hand-off ran one-directional: Researcher → args → Librarian executes → reports to user. The Librarian never **confirmed receipt or scoped the task back** to the Researcher ("I read the note; I'll create `cortisol` and refine two `ashwagandha` claims — confirm?"). In a single conversation this is moot (same context, user is right there). But it means the seam has **no acknowledgment step**, so in any more decoupled hand-off (headless, async, cross-session) there's nothing catching a misunderstood brief before the Librarian writes.

**Suggested fix:** non-blocking for the synchronous case — but note that a robust hand-off should include a lightweight receipt ("here's my read of the task before I write") when the partners aren't sharing live context. Cheap insurance against a misread brief becoming a wiki write.

## What worked well (for balance)

- **The knowledge flowed end-to-end with zero loss.** Despite the unspecified mechanics, the research note reached the wiki intact, and the wiki got *better* for it (the new page refined an existing one). The core value proposition — Researcher builds, Librarian files, wiki compounds — demonstrably works.
- **The single-writer contract held under hand-off.** The exact thing the roster is designed to protect (one canonical writer) survived a cross-partner flow cleanly: the Researcher never wrote a wiki page, the Librarian never did original research. The division of labor is real.
- **A thorough freeform brief was sufficient.** Even without a schema, a carefully-written args brief carried everything — which suggests the schema fix (§2) is about *robustness/floor*, not about a broken ceiling. The good case is already good.
- **Persona switching mid-conversation was seamless to execute.** Invoking the Librarian Skill and re-orienting via its activation ritual worked without friction — the mechanical act of handing off is smooth; it's the *conventions around* it that are underspecified.

---

_Net: the hand-off **works in the good case** and proves the roster's core premise — but it is the **least-specified domain in the module**. Every mechanical decision (session boundary §1, payload contents §2, partner-calls-partner §3, role-boundary §4, preference relay §5, receipt §6) was a judgment call with no guidance. The two highest-value fixes: **define the hand-off as an explicit session boundary** (§1, reconciles the contract) and **specify a minimal hand-off payload** (§2, makes the seam robust to a careless hand-off). The role-boundary smell (§4) is the subtlest and most worth watching — the hand-off quietly invites the Researcher to do the Librarian's job._
