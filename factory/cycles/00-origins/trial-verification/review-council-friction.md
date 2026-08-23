# vlt-review-council — Verification Notes

_Friction observed running the review-council as the blast-radius gate inside a `vlt-mint` new-partner mint (**The Creative**), `vlt-core`, 2026-06-03. For module iteration._

The council produced a clean, actionable verdict (pass + two conditions, no `Disputed-open`) that mapped directly onto the mint gate, and the single-axis lens discipline produced genuinely high-signal output. The friction is about *how a caller actually runs the council* — the invocation boundary is underspecified, and a 2-member panel exposes seams the skill doesn't address. Ordered by impact.

## 1. "Run it via `vlt-review-council`" has no concrete invocation mechanism — I reimplemented the council inline

`vlt-mint` Step 2 says "run it via `vlt-review-council`" and "pass `vlt-review-council` the proposal and its kind." But there's no sanctioned way for one skill to *call* another and get a structured value back. So I did what the council's own Step 3–4 describe — spawned the architect as an independent agent with its Activation Prompt pasted verbatim, then performed the moderator synthesis myself — rather than "invoking the council." Functionally faithful, but the line between **"vlt-mint runs the council"** and **"vlt-mint reimplements the council from its prose"** is entirely on the operator. Two operators could gate the same mint via materially different procedures and both be "correct."

**Suggested fix:** state the intended mechanism explicitly — e.g. "spawn the lenses per `vlt-review-council` Step 3 and synthesize per Step 4" (blessing inline execution), or define a real hand-off. Right now the verb "run it via" implies a call that the harness doesn't actually provide.

## 2. With a 2-member panel, the moderator-as-its-own-agent step is wasteful, but the skill doesn't say so

For `new partner` the map yields `architect + moderator`. The moderator "holds no stance" and only synthesizes, so spawning it as a *separate* agent to read a single other lens is pure overhead. I did the moderator synthesis in the main context. The skill's graceful-degradation note permits sequential/in-context lenses "where subagents aren't available" — but that's framed as a fallback, not as the sensible default when the only non-synthesizing lens is one agent. So I took a defensible shortcut the skill doesn't actually bless.

**Suggested fix:** add a line — "when the panel reduces to one substantive lens plus the moderator, the moderator may synthesize in the caller's context; spawning it separately buys nothing." Make the efficient path explicit instead of leaving it as an inferred exception.

## 3. The architect lens grounded itself in the **plugin-cache** copy, not the working tree

Given the proposal + system context, the architect independently read the real files to ground its judgment — and resolved `vlt-agent-librarian/SKILL.md` etc. to `~/.claude/plugins/cache/vlt/vlt/1.0.0/`, the **pristine installed copy**, not the project `.claude/skills/` tree the mint writes to (see `mint-friction.md §1`). Here it was harmless (pre-mint state matched), but a mint that edits the project copy before gating would have the council review stale state and possibly pass/reject against the wrong baseline.

**Suggested fix:** when the council reviews a mint, the caller should point each lens at the **specific working-tree paths** under review, not let the lens resolve files by name (which can hit the cache). Tie this to the mint-persistence fix.

## 4. For a mint review, the verdict's reasoning survives only if the caller chooses to record it

Step 5 is explicit and correct: for a mint review the council "writes no file" and returns the verdict to `vlt-mint`. But that means the architect's detailed, multi-point reasoning — the actual fit/overlap analysis — exists nowhere durable unless the *caller* captures it. I folded it into `vlt-mint/.decision-log.md`, but only because I chose to; nothing in either skill requires it. A future mint that skips that step loses the rationale for a roster change.

**Suggested fix:** have `vlt-mint` Step 4 ("Record the mint") require capturing the council verdict (at least Consensus + Recommended-actions + any Disputed-open) in the decision log, so the gate's reasoning is preserved with the change it gated.

## 5. A single substantive lens carries a whole "new partner" fit-check (observation, not a defect)

`architect + moderator` means the architect alone judges roster fit, overlap, and precedent. It did this well here — it caught the Researcher-overlap risk, reframed the differentiation structurally, and flagged a deferred boundary. But "is this partner worth its cost / will the user know who to summon" is arguably also a pragmatist or roster-coherence question, and the map doesn't field one for a new partner. Not friction — the gate worked — but worth a deliberate check that one lens is the intended coverage for adding a roster member.

## What worked well

- **Activation-Prompt-verbatim + single-axis discipline produces real signal.** The architect stayed rigorously on structural-coherence, didn't drift into shipping-speed or scope, and returned a position dense with checkable claims (file/line citations, a concrete "two gating conditions"). The lens design does what it claims.
- **The four-section verdict maps perfectly onto a mint gate.** Consensus / Disputed-resolved / Disputed-open / Recommended-actions translated to pass/revise/reject with the specific revisions attached — exactly what the caller needs to proceed.
- **The `kind → council` selection is frictionless.** Looking up `new partner → architect + moderator` was instant; the skill's instruction to skip a lens whose exclusion-case matches (e.g. skeptic on a cheap reversible call) is a good discipline even though it didn't bind here.
- **Independence held by construction.** With one lens it's moot, but the structure (lenses don't see each other) is clearly the right call and was trivial to honor.

---

_Net: the council's **output** is excellent — disciplined lenses, an actionable structured verdict. The friction is the **seam between caller and council**: "run it via vlt-review-council" has no real invocation (§1), the 2-member moderator step is awkward (§2), lenses can ground in the wrong file tree (§3), and a mint verdict's reasoning is preserved only by caller goodwill (§4). The §1/§2 items are doc clarifications; §3 ties to the mint-persistence backlog candidate; §4 is a worthwhile `vlt-mint` requirement. None are blocking._
