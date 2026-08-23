# vlt-lint — Verification Notes

_Friction observed running `/vlt-lint` on `vlt-core`, 2026-06-03, immediately after the cortisol ingest. For module iteration._

Lint completed cleanly on the first pass — no script errors, no clobbering. It ran in **full mode** (correctly, since there was no prior `lint` entry in `{log}` to scope against), checked 2 wiki pages + the index, made one auto-fix (an index source-count correction), and emitted the structured report + log line. The friction below is ambiguity that forced a judgment call, ordered by impact. The headline one (#1) is that the single auto-fix I applied rested on an **inferred rule the module doesn't define anywhere** — so the "safe structural fix" was really a guess.

## 1. "Source counts accurate" is an auto-fix mandate with no definition of what a source *count* is

Step 2 (Index drift) and Step 3 (auto-fix) both make source counts a first-class, auto-applicable concern: *"every page appears in `{index}` … source counts accurate"* and *"update source counts."* But **nothing defines what the count counts.** The index rows read `(2 sources)` / `(1 source)`, while pages carry a frontmatter `sources:` list of varying length.

Concretely: `cortisol` showed `(1 source)` in the index but its frontmatter `sources:` has **11 entries** (1 research note + 10 URLs). `ashwagandha` showed `(2 sources)` and its frontmatter has exactly 2. So I reverse-engineered the rule from the one page that happened to agree with itself — "index count = length of frontmatter `sources:`" — and auto-corrected cortisol `1 → 11`.

That's shaky for two reasons:
- **It might be wrong.** `(1 source)` could have meant "built from **1 research note**" (which itself synthesizes 21 underlying sources, as the page's own Sources section says). Under *that* reading, `1` was correct and I just introduced drift. I mutated a file on a coin-flip between two defensible semantics.
- **The skill itself knows the spec is missing.** The open backlog item *"Author an index-structure convention"* explicitly says `vlt-lint`'s index-drift check *"can't validate … against a non-existent spec."* That warning is about category placement and the stubs section — but it applies just as hard to the source count. I was auto-applying a fix the skill has already flagged as unspecifiable.

This is the sharpest edge in the run: the skill grants index-drift **auto-fix** authority (no human gate) over a value whose definition doesn't exist yet.

**Suggested fix:** either (a) demote source-count correction from "auto-fix" to "flag_for_human" until the index-structure convention exists, or (b) pin the definition now in the skill text — e.g. *"index source count = number of entries in the page's frontmatter `sources:`"* — and point both `vlt-ingest`'s writer and this check at it. (b) is cheap and would have made my fix correct-by-construction instead of a guess. This is a real `maintenance` candidate, tightly coupled to the already-open index-structure-convention item — flagging for your call before I file it.

## 2. "Bump `last_updated` on any page you substantively edit" has a fuzzy threshold and silently no-ops same-day

Step 3 says bump `last_updated` on substantive edits, *"skip the bump for trivial formatting."* My index edit (a source-count correction) sits exactly on that line — it changes a fact, not just whitespace, so arguably substantive; but it's also a one-token parenthetical, so arguably trivial. **And it doesn't matter either way here:** the index's `last_updated` was already `2026-06-03` (today), so any "bump" is invisible. A reader diffing the file sees content change with no date movement, which *looks* like the exact silent-overwrite the supersession convention exists to prevent.

So I couldn't actually *exercise* the bump rule — same-day edits make it untestable, and the substantive/trivial line is mine to draw.

**Suggested fix:** add a one-line rule of thumb for the boundary (e.g. "callout add / claim change / section restructure = substantive; count tweak / link repoint / formatting = trivial") so the call isn't re-litigated each run. Same-day no-op is inherent and fine — but worth one sentence acknowledging it so an agent doesn't go hunting for a way to force a visible bump.

## 3. `files_checked` in the report has no counting rule, and full mode makes the scoped checks moot

The report schema example shows `files_checked: 10`. In full mode I read 2 wiki pages, the index, **and cross-read 2 research notes + `{log}` + `{backlog}`** for the staleness/contradiction checks. What's the denominator? I reported `files_checked: 3` (pages + index) with an inline comment that 2 research notes were cross-checked — but "checked" is genuinely ambiguous between "files I assessed for fixes" and "files I opened." A dashboard consuming this key will silently compare apples to oranges across runs depending on the agent's reading.

Relatedly, several Step-2 checks are framed for **scoped** mode ("orphan-relative-to-scope … flag, don't exhaustively re-check") with no full-mode counterpart stated — in full mode I just did the exhaustive version, which is presumably intended but never said.

**Suggested fix:** define `files_checked` as "files read in full for assessment" (or split into `files_assessed` vs `files_cross_read`), and add a one-liner that full mode supersedes the scoped-only hedges.

## 4. No-baseline → full fallback worked, and confirms a *known recurring theme*

Step 0's `grep "^## \[.*\] lint" {log} | tail -1` returned nothing (this was the vault's first lint). The skill handles this explicitly — *"If there's no prior `lint` entry … fall back to full mode and say so"* — and I did. **Smooth, no friction.** Logging it only because the handoff notes name *"lint-cadence-with-no-baseline"* as a recurring fresh-vault-edge theme: this pass **confirms** it, and confirms the skill's handling of it is correct. Per the handoff guidance ("if a new pass hits the same two, that's a strong signal"), the fresh-vault-edge family now has a third independent hit (setup `{log}`-scaffolding, ingest re-ingest grep, lint no-baseline) — but unlike the first two, lint's version is *already gracefully handled*, so it needs no fix. Worth noting that the root cause is shared: it'd vanish entirely if `vlt-setup` scaffolded `{log}` (the already-backlogged §6 item).

## 5. An *already-documented* contradiction has nowhere clean to go in the report

The chronic-stress hyper- vs. hypo-cortisol split is a real cross-page tension — but it's already documented in **both** pages' Open Questions *and* filed as a `knowledge-gap` in `{backlog}`. The skill's `flag_for_human.contradictions` slot and the "document in both pages, flag it" instruction assume a *newly-found* contradiction. There's no schema affordance for "contradiction exists, is properly handled, no action needed." I reported `contradictions: []` with a parenthetical — technically correct (nothing to fix) but it makes a healthy, well-managed disagreement invisible in the parseable output, which slightly undercuts the skill's own "contradictions are features, say so loudly" ethos.

**Suggested fix:** add an optional `contradictions_documented: [...]` key (or a `status: handled` marker) so a managed contradiction shows up as a *positive* signal in the report rather than vanishing into an empty list.

## What worked well

- **The 7-step spine is clean and linear** — scope → read → structural checks → auto-fix → backlog → structured report → log. I never wondered what came next.
- **"Contradictions are features, not bugs"** (Tips) is load-bearing and it worked: it actively stopped me from forcing a resolution on the cortisol hyper/hypo split, which would have been the wrong move. Best single line in the skill.
- **The structured YAML report format** is genuinely parseable and the keys are stable — emitting it was mechanical, not interpretive (the *values* needed judgment; the *shape* never did).
- **The log line format** is fully specified and greppable — and it now seeds the scoped-mode baseline for the next run, closing the loop that #4 was about.
- **"Don't over-clean"** correctly scoped me: I auto-fixed the one structural thing, flagged the `adaptogens` gap and the ashwagandha single-secondary-source gap, and left every content judgment to the human. The auto-fix / flag / backlog tri-state is the right granularity.

---

_Net: lint is solid and the spine flowed without a single procedural snag. The one real risk is #1 — the skill hands index source-count correction **auto-fix authority over a value the module never defines**, so my single mutation was a reverse-engineered guess that may have introduced drift rather than removed it. Pinning the source-count definition (or demoting it to flag-only until the index-structure convention lands) is the highest-value fix and pairs naturally with the already-open index-convention backlog item. Everything else is small: a same-day-invisible `last_updated` bump (#2), an undefined `files_checked` denominator (#3), and no report slot for an already-handled contradiction (#5). #4 is a no-fix confirmation of the known fresh-vault-edge theme._
