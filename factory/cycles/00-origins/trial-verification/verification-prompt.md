# Trial Verification — Handoff Prompt

_A reusable prompt for handing the `vlt` module trial off to a future partner or session. Copy the block below into a new session (optionally after summoning a partner, e.g. `/vlt-agent-librarian`). Each run produces (or appends to) a friction doc in `_agent/vlt-verification/`._

---

## The prompt

> I'm running a trial of the `vlt` module and collecting structured feedback on it. As you work this session, act as an honest field tester: do the real task you've been asked to do, **and** capture the friction.
>
> **Write your findings to `_agent/vlt-verification/<skill-or-flow>-friction.md`** — one file per skill or flow (e.g. `ingest-friction.md`, `lint-friction.md`, `research-friction.md`, `query-friction.md`, `extract-friction.md`, `mint-friction.md`). If a file for this flow already exists, **append a dated pass** to it rather than overwriting. You own these files directly — they are trial artifacts, **not** wiki pages, so don't run them through ingest, don't write a `{log}` entry for them, and don't council-gate them.
>
> **Match the house style** (see `setup-friction.md`, `librarian-ingest-friction.md`):
> - A one-line header note: which skill/flow, on what vault, what date, "for module iteration."
> - A one-sentence verdict up front (did it complete cleanly? any hard failures?).
> - **Numbered friction points, ordered by impact.** Each: what happened (concrete — quote the skill text or the actual command), the judgment call or workaround you made, and a **Suggested fix**.
> - A **"What worked well"** section — the feedback loop needs positives, not just complaints.
> - A one-line **Net:** summary at the bottom.
>
> **What counts as friction worth logging:** anything that made you guess, shell out, infer an unstated rule, hit a missing/empty file, re-read to disambiguate, or choose between two defensible behaviors. Anything that *broke* (errors, clobbering, broken links). And the inverse — anything that was notably smooth and should be preserved.
>
> **Bias toward honesty over politeness.** "This worked but was a guess" is more useful than "this worked." If a mechanism the module emphasizes turned out to be invisible or untestable in practice, say so. If you noticed a real backlog candidate (a `capability-gap`, `maintenance`, or `knowledge-gap`), mention it — and ask me before filing it to `{backlog}`.
>
> At the end, give me a 3–5 bullet summary of the top friction points and whether any rise to backlog items.

---

## Notes for whoever hands this off

- **Scope it.** The prompt is generic; pair it with an actual task ("ingest this source", "lint the vault", "research X"). The friction doc is a byproduct of doing real work, not a standalone audit.
- **Recurring themes so far** (2026-06-03, from `setup` + `librarian-ingest` passes): *fresh-vault edge cases* (missing `log.md`, empty `vault_structure`, grep on a nonexistent log) and *interactive-vs-headless ambiguity*. If a new pass hits the same two, that's a strong signal they're worth fixing first.
- **One file per flow, append don't overwrite** — so the docs accumulate passes across sessions instead of resetting. A future `vlt-lint`-style sweep over `vlt-verification/` could then summarize the whole trial.
