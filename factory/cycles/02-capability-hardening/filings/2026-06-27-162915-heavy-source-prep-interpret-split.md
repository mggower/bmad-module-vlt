# Heavy-source ingest — the prep/interpret sub-agent split (generalize beyond YouTube)

_Filed from the `vlt-core` vault after the **first real production run** of the Librarian's `ingest-youtube` capability (the Mina Kimes "Top 10 Defenses for 2026" ingest, 2026-06-27) surfaced a context-economy + fidelity pattern that is **not YouTube-specific**. Follow-on to `2026-06-27-160109-light-capability-source-type-frontend.md` (the mint filing). The vault-grown capability edit stays local; what's filed here is the **generalizable pattern** the module should absorb and the convention seam it touches._

## Problem statement + evidence

Running `ingest-youtube` end-to-end in anger exposed where the cost and the risk in a **heavy-source ingest** actually live — and they're not where the intuition points:

- **Fetch + clean are cheap and safe.** `yt-dlp` + the `clean-captions.py` script are deterministic; run through Bash, the operator sees only the tail and the stats. No context cost, no hallucination surface (a script can't invent words).
- **The context cost is *reading the full transcript* to interpret it.** A 1.5h video ≈ ~16k words. Slurping that into the interpreting context to write the wiki is what actually fills the window — and it's the *interpretive* step, the one you most want done on a clean context.
- **The error surface is the *extraction handoff*** — turning unpunctuated raw text into structured claims (the capability already warns LLMs hallucinate when "restoring" such text). If interpretation happens on a context already saturated with raw transcript, judgment degrades exactly when it matters.

The user's instinct ("use sub-agents for the pre-ingest stages so my context is fresh for interpreting the source and writing the wiki") is correct, but the lever is **keep the raw source out of the interpreting context**, not "isolate the parsing."

## The pattern (worth naming in the module)

> **Prep/interpret split (heavy-source ingest).** For any source too large to interpret without flooding context (long video transcript, long PDF, multi-page crawl), split the ingest in two:
> - **Prep sub-agent (mechanical):** fetch → normalize/clean → deposit the source-of-record to `sources/` → run the credential scan. Returns a **neutral navigational brief** — section map, transcript/page **locations**, verbatim **located quotes**, and flags. **Never** the raw body; **never** an interpretation.
> - **Owning partner (fresh context):** runs the unchanged ingest verb, reading *selectively* into the deposited source-of-record at the brief's locations for only the passages it will canonicalize.

Three invariants make it safe:

1. **Single-writer holds.** Prep agents fetch/clean/deposit and *report*; they never write the wiki. The canonical write stays the verb skill's. (Same shape as `vlt-lint-full`: read-only finders return structured data, one serial writer applies.)
2. **The brief is a map, not the territory.** The full deposited source stays the source-of-record; the partner verifies each located quote against it before ingesting, so a prep-agent slip can't become a confident wiki claim.
3. **Neutral map, not a digest (the load-bearing design call).** The prep agent extracts *no interpretation* — structure and located raw material only. A pre-interpreted digest is cheaper for the context budget but **primes and quietly corrupts** the fresh reading that is the entire reason to keep interpretation with the partner. Judgment stays with the fresh context; the agent supplies structure, not conclusions.

Plus a sequencing note: the **re-ingest check runs up front** (a cheap `{log}` grep that gates whether to fetch at all — don't pay for fetch+clean on a re-ingest); the **credential scan runs in the prep agent** (it needs the cleaned text).

## Why this is general, not YouTube-local

`ingest-youtube` is one *source-type front-end*; the prep/interpret split is orthogonal to the source type. The same shape applies to:

- **Long PDFs** (a 200-page paper/book) — prep agent extracts → deposits text → returns a section/page map + located quotes.
- **Multi-page web crawls** (`tavily_crawl`/`tavily_map` over a doc site) — prep agent crawls + normalizes → deposits → returns a per-page map.
- Any future heavy input that `vlt-ingest` should eat.

It also composes cleanly with the existing **`batch-ingest-fanout-pattern`** (plan-first, approval-gated parser→topology→writer fan-out): batch fan-out is the *many-sources* axis; prep/interpret is the *one-large-source* axis. Same single-writer spine; they stack (a fan-out whose per-source leaf is itself a prep/interpret split).

## Exact module-side changes to ship

1. **Name the pattern** — add **"Prep/interpret split (heavy-source ingest)"** to the module's pattern catalog (wherever `batch-ingest-fanout-pattern` and the `source-type front-end` pattern live), with the three invariants verbatim. Goal: reached-for, not re-invented per capability.
2. **`vlt-ingest` guidance** — a note in `vlt-ingest` (and/or the contract's ingest discussion) that for a **heavy source**, Steps 1–3 (read/fetch/normalize) may be delegated to a read-only-style prep sub-agent returning a *neutral brief*, with Step 4+ (interpret + canonical write) staying with the invoking partner on fresh context. Reuse the `vlt-lint-full` single-writer framing explicitly — it's the same architecture.
3. **Threshold, not always-on** — like `vlt-lint`→`vlt-lint-full`, the split earns itself above a size threshold (a ~1.5h video fits one context; the win grows with length). State the threshold so small ingests stay inline (no sub-agent overhead) and large ones escalate.
4. **Capability-template note (optional)** — for source-type front-ends that wrap a heavy input, point at the prep/interpret split as the default orchestration, so the next front-end (PDF, crawl) inherits the neutral-map discipline rather than re-deriving "digest vs map."

## Provenance

- Vault: `vlt-core`. Capability edited locally: `_agent/partners/librarian/capabilities/ingest-youtube.md` (own-zone, council-none procedure refinement; decision-log line 2026-06-27).
- Triggering run: ingest of "Top 10 Defenses for 2026 | The Mina Kimes Show" (YouTube, 1:24:28, ~16k-word transcript) → `nfl-2026-defense-rankings` (new) + 2 updated pages.
- Design call (user + Librarian): chose **neutral map over faithful digest** deliberately; user affirmed the pattern should apply to **any heavy source**, not just YouTube.
</content>
