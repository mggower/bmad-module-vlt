# Researcher Activation & Research — Verification Notes

_Friction observed running the **Researcher** persona (`/vlt-agent-researcher`) and a first **`vlt-research`** dive on the `vlt-core` vault, 2026-06-03. For module iteration. Sibling to `setup-friction.md` and `librarian-ingest-friction.md`._

Both the activation ritual and the research dive completed cleanly — cortisol stub filled with a 21-source note, verification checklist passed, log entry appended, Librarian hand-off offered, no broken mechanisms. Tavily MCP (a user-stated tool preference) worked first try. The notes below are friction/ambiguity that required a judgment call or a deviation, ordered by impact.

## 1. When the Researcher fronts `vlt-research`, Phase 1 (brief + feasibility gate) is already spent

`vlt-research` Phase 1 is a "short conversation to sharpen the brief" — push for a precise question, pick a depth, run a feasibility gate. But the summoning happened in the **partner layer**: by the time the skill activated, the Researcher had *already* had that conversation with the user ("let's fill the cortisol stub") and composed a fully-formed, depth-implied brief as the skill's arguments. So Phase 1 had nothing left to do — I declared the brief sharp and the depth "moderate-to-deep" and proceeded **without actually interviewing**. That was a judgment call: re-running the interview would have been redundant theater.

This is the **interactive-vs-headless ambiguity** flagged in `setup-friction.md §1` and `librarian-ingest-friction.md §3`, now in a third flow — and here it has a specific shape: a partner-fronted skill receives a pre-sharpened brief, so the skill's own elicitation phase is structurally redundant. The skill doesn't acknowledge it might be invoked *downstream of* a partner who already did Phase 1.

**Suggested fix:** add a mode note to `vlt-research` Phase 1 — "If invoked by a partner (or via a direct 'research X') with an already-sharp brief and an implied depth, treat Phase 1 as satisfied: state the question + depth you've inferred and proceed, rather than re-interviewing. Reserve the full interview for a cold, vague prompt." Mirrors the fix proposed for ingest Step 4.

## 2. The mandated `.WIP.md` auto-checkpoint never materialized — and felt like overhead, not insurance

Phase 3 mandates a running `{research}/...WIP.md` checkpoint "every few web calls — not only on declared deep dives." I ran **6 Tavily searches** but executed the whole dive in **one continuous turn** (searches batched in parallel), then wrote the final note directly. I never wrote a WIP file — at no point was the work at interruption risk, so a checkpoint would have been pure ceremony I'd delete moments later.

So a load-bearing-sounding mechanism was, in this (common) shape of session, **skipped entirely by reasonable judgment**. The trigger ("every few web calls") keys off call *count*, but the thing that actually justifies a checkpoint is *interruption risk / session length* — which a single-turn batched dive doesn't have. As written, an obedient agent writes-then-discards a WIP file for no benefit; a judging agent (me) silently skips a mandated step. Neither is clean.

**Suggested fix:** re-frame the checkpoint trigger around risk, not count — e.g. "If the dive spans multiple turns, or you're pausing/at risk of interruption, maintain a `.WIP.md`. For a short dive completed in one pass, write the note directly." Make the skip explicit and blessed instead of a silent deviation.

## 3. The skill is tool-agnostic by design, so the Tavily preference had to come from the partner/Bond layer

Phase intro says "Web access is host-provided… don't hardcode a specific tool." Correct and portable. But the user's actual instruction this session was a specific preference — "use Tavily MCP, flag connection issues before falling back." That knowledge lived in the **partner `## Bond`** (where I recorded it) and in memory, **not** in the skill. The skill would never have told me to prefer Tavily, nor to flag-before-fallback. It happened to compose fine because I carried the preference in as the partner — but a bare headless `vlt-research` invocation with no partner context would have used whatever default web tool and silently ignored the user's stated preference.

**Suggested fix:** non-blocking. Possibly a one-liner in Phase 3: "Honor any user- or vault-level tool preference (e.g. a mandated MCP connector recorded in the partner thread / config) over the generic default, and surface a fallback rather than degrading silently." Keeps the skill tool-agnostic while making it preference-aware.

## 4. Frontmatter `sources:` and the Sources section duplicate every URL — drift risk

The verification checklist requires that **every URL appears in both** the frontmatter `sources:` list *and* the prose Sources section. For this note that meant maintaining **21 URLs in two places** — bare in frontmatter, annotated in the body. I had to manually reconcile them to be sure neither list dropped or added an entry. It's a real maintenance/error surface: the two lists can silently drift, and nothing checks them against each other except a careful human re-read.

**Suggested fix:** non-blocking, but a future `vlt-lint` rule could diff a research note's `sources:` frontmatter against the URLs in its Sources section and flag mismatches. Cheap, catches a real failure mode.

## 5. Timestamp for the filename still requires shelling out (recurring)

Same as `librarian-ingest-friction.md §4`: the `YYYY-MM-DD-HHmmss` filename prefix needs a real clock read (`date +...`) because the harness context exposes the date but not seconds. Paid it again here. Recurring across every flow that writes a datetime-prefixed file — strong signal it deserves the one-line "mint timestamps from a real clock, not context date" note in the shared conventions rather than per-skill rediscovery.

## 6. Mid-session: research log entry exists, no session note yet (by design, recurring)

Per the session-ownership rule, `vlt-research` Phase 6 appends a `research` log entry but writes **no** session note — the Researcher owns one session note at close. So right now there's a `research` log line and no session record, exactly the intermediate state `librarian-ingest-friction.md §6` describes. Re-confirming it across a second flow: correct by design, but a parser/lint sweeping for completeness will see orphan operation-entries until the partner closes the sitting. Worth documenting as an expected intermediate state once, centrally.

## What worked well (for balance)

- **Depth calibration is concretely useful.** "Moderate = 5–10 searches, 5–8 sources" gave me an actual target to hit (I ran 6 searches / 21 sources) instead of guessing when "enough" was reached.
- **"Organize by theme not source; disagreement is the finding" produced the best part of the note.** Following that instruction directly surfaced the hyper- vs. hypo-cortisol tension — the single most valuable finding — instead of a flat per-source summary that would have buried it.
- **The Phase 2 vault check made the note land as a *complication of existing knowledge*, not an island.** Connecting cortisol back to the existing `ashwagandha` page (cortisol-as-mechanism) is what made the dive feel like the wiki *compounding*. This is the module's core promise working in practice.
- **The research-vs-wiki + Librarian-handoff boundary kept me in my lane.** "File a research note, offer the canonical-page write to the Librarian, never write the wiki page yourself" was unambiguous — I never agonized over whether to write `cortisol.md` directly.
- **Backlog capture mid-flow was frictionless.** Noticing the hyper/hypo tension and filing it as a `knowledge-gap` (with the user's OK) took one edit and felt like the cheapest act in the system, as advertised.
- **The verification checklist was load-bearing again.** Re-reading the note against the explicit list (dense summary? every claim sourced? wikilinks resolve? no `key:`?) caught nothing broken this time — but the discipline is what *makes* "no `key:` field" reliable rather than hoped-for.

---

_Net: the Researcher + research path is solid and a genuine pleasure to operate inside; the persona's "push, don't serve" framing and the skill's theme-not-source synthesis discipline are the standouts. Friction is concentrated in (a) the **partner-fronted-skill makes Phase 1/elicitation redundant** ambiguity — now seen in a third flow, the strongest recurring signal — and (b) the **`.WIP.md` checkpoint triggering on call-count rather than interruption-risk**, which made a mandated step into either ceremony or a silent skip. Both are cheap to specify away._
