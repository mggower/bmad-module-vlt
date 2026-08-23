# Friction Synthesis — the `vlt` Module Trial

_A cross-cutting roll-up of the ten verification docs in `_agent/vlt-verification/`, synthesized 2026-06-05 on the `vlt-core` vault. For module iteration. This is the "future `vlt-lint`-style sweep over `vlt-verification/`" the handoff prompt anticipated — a trial artifact, **not** a wiki page: not ingested, not logged, not council-gated._

## What this covers

Ten field-test passes across the module's surface, all run 2026-06-03 on a single fresh vault as it went from empty to two wiki pages:

| Doc | Surface tested | Hard failures |
| --- | --- | --- |
| `setup-friction.md` | `vlt-setup` on an installer-built vault | none |
| `librarian-activation-friction.md` | Librarian persona / activation / disciplines | none |
| `librarian-ingest-friction.md` | `vlt-ingest` (2 passes + lint addendum) | none |
| `researcher-activation-friction.md` | Researcher persona / activation | none |
| `research-friction.md` | `vlt-research` dive | none |
| `partner-handoff-friction.md` | the Researcher→Librarian seam | none |
| `lint-friction.md` | `vlt-lint` (first run, full mode) | none |
| `mint-friction.md` | `vlt-mint` (minted the Creative) | none |
| `review-council-friction.md` | `vlt-review-council` as the mint gate | none |
| `verification-prompt.md` | the reusable handoff harness itself | — |

**The headline finding of the whole trial: nothing broke.** Every flow completed cleanly, no clobbering, no broken links, no script errors. The module *works*. All friction below is ambiguity that forced a judgment call, an unstated rule that had to be inferred, or a mechanism that a fresh/thin vault couldn't actually exercise. That is the good kind of friction to have — it is all cheap to specify away, and none of it is a redesign.

The deeper signal is that the ~45 individual friction points are not 45 independent problems. They collapse into **six structural themes**, and two of those themes account for most of the leverage.

---

## Theme 1 — Structure-by-inference: rules that survive only because one writer keeps them self-consistent

**The highest-leverage cluster.** Several load-bearing structures in the vault have **no canonical definition** — they exist only as per-operation inference, and they stay coherent *only* because the single-writer contract means one skill maintains each of them in roughly one style. The contract masks the gap; it does not close it. The moment the wiki scales, or the single-writer/single-conversation assumption loosens, these drift.

- **The index body-structure is defined nowhere.** Category sections, the canonical row format (`- [[page]] — desc (N source[s])`), and the genuinely-useful `## Stubs (linked, not yet written)` section are all invented and sustained by mimicry. `vlt-ingest` Step 7 is the only (loose) spec; no `{conventions}` file owns it. `vlt-lint`'s index-drift check is correspondingly under-powered — it can't validate category placement or the stubs section against a non-existent spec. _(`librarian-ingest-friction.md §9`)_
- **"Source count" is auto-fixed against an undefined definition.** `vlt-lint` is granted **auto-fix authority** (no human gate) over index source counts — but nothing says what a count counts. On the first lint, `cortisol` read `(1 source)` against an 11-entry frontmatter list; I reverse-engineered "count = length of frontmatter `sources:`" from the one page that agreed with itself and mutated `1 → 11` — but `(1 source)` plausibly meant "built from 1 research note" (itself synthesizing 21 URLs), under which my "fix" *introduced* drift. A file was mutated on a coin-flip between two defensible semantics. _(`lint-friction.md §1`, `librarian-ingest-friction.md §9` addendum)_
- **The `kind → council` gate table is duplicated verbatim in two skills — and already drifts** ("architect (+moderator)" vs "architect + moderator"). A single-home violation *inside the gate that enforces single-home.* _(`mint-friction.md §4`, `review-council-friction.md §1–2`)_
- **`vault_structure` overrides are invisible/untestable** because the installed config carries no map at all — every path resolves to the shipped default by necessity. The much-emphasized override mechanism can't be exercised on a real installed vault. _(`librarian-ingest-friction.md §1`)_

> **Why this is the top theme:** every item here is a place where the module *relies on* an unwritten rule and gets away with it *today* only because of an assumption (one writer, one conversation) that the roster premise is explicitly built to outgrow. Fixing these is fixing the module's ability to scale past its own happy path.

**Backlog status:** the index-structure convention (which must also pin + gate the source-count definition) and the single-source gate table are **already filed**. The `vault_structure`-materialization question is **not** filed.

---

## Theme 2 — The hand-off seam is the least-specified domain in the module

The roster's entire reason to exist is that multiple partners share one vault and hand work between them. Yet **every mechanical decision in a hand-off is a judgment call with no guidance**, and the partner layer is written as if *one partner = one conversation* — which the first real hand-off immediately violated.

- **Session boundaries are undefined and contradict the contract.** The contract's invariant is "one conversation yields one session note." A mid-conversation Researcher→Librarian hand-off produced **two** notes (one per partner sitting) — defensibly, but in direct contradiction of the stated rule. The fix ("one *partner sitting* yields one note; a hand-off is the boundary") reconciles both sides at once. _(`librarian-activation-friction.md §1`, `partner-handoff-friction.md §1`)_
- **There is no hand-off payload schema.** The brief is freeform prose in the receiving skill's args. It worked only because the handing-off partner was deliberately thorough; a hurried hand-off could silently drop the supersession targets or a user preference and the receiver would never know what it didn't get. _(`partner-handoff-friction.md §2`)_
- **`vlt-ingest` Step 5 doesn't fit a research-note hand-off** — the single most-blessed way knowledge reaches the wiki. Following it literally produces a research-note-of-a-research-note; I skipped Step 5 by judgment. _(`librarian-ingest-friction.md §7`)_
- **"No partner calls another" (activation) vs. "hand off to the Librarian" (operation)** is an unreconciled tension; **activation assumes a user summon** but the Librarian was invoked by a partner; and the **shared state reads are redundant** on a same-conversation switch. _(`partner-handoff-friction.md §3`, `librarian-activation-friction.md §2–3`)_
- **A role-boundary smell:** the Researcher told the Librarian *how to file* (callout type, reason code) — reaching across the single-writer line. The hand-off invites this because nothing says how much filing-intent a hand-off should carry. The subtlest item in the whole trial and most worth watching. _(`partner-handoff-friction.md §4`)_

> The good case is genuinely good — knowledge flowed end-to-end with zero loss and the single-writer contract held. The fixes are about the **floor**, not the ceiling: making the seam robust to a careless or decoupled (headless/async) hand-off rather than relying on a thorough operator.

**Backlog status:** **none of this is filed.** The two highest-value fixes — define the hand-off as an explicit session boundary, and specify a minimal hand-off payload — are unfiled candidates.

---

## Theme 3 — Interactive-vs-headless ambiguity, sharpened to "partner-fronted skills"

Seen in **three independent flows**, which makes it the most-corroborated single pattern in the trial. When a partner fronts an operation skill, the user-facing conversation has *already happened* in the partner layer — so the skill's own elicitation phase is structurally redundant, and the agent must guess which mode it's in.

- `vlt-setup`: re-prompt for values, or silently reuse the installer's answers? _(`setup-friction.md §1`)_
- `vlt-ingest` Step 4: a one-word "yes, ingest" — pause for the multi-exchange deliberation, or surface-the-plan-and-proceed? _(`librarian-ingest-friction.md §3`)_
- `vlt-research` Phase 1: the brief-sharpening interview is already spent before the skill activates. _(`research-friction.md §1`)_

Each was resolved the same way (proceed in one pass, present for review) but each was a guess. **The fix is one reusable mode-note**, applied to every elicitation phase: "if invoked downstream of a partner with an already-sharp brief, treat the phase as satisfied; reserve the full interview for a cold, vague prompt."

**Backlog status:** not filed. A single cross-skill candidate.

---

## Theme 4 — Cold-start / fresh-vault blindness: personas written for a warm, populated vault

The rituals and personas assume accumulated state. A vault hits the empty case exactly once per partner — and that once is unguided.

- **The Researcher's signature opening move can't execute on first activation** (thread-surfacing open against three empty sections), and **"become yourself modulated by `## Self`" is untestable** when `## Self` is empty, and **the pressure model has no inter-page tension** to work on a one-page vault. The persona's three most distinctive behaviors all need a warm vault. _(`researcher-activation-friction.md §1–3`)_
- **The lint-cadence reflex has no baseline** — "several ingestions since the last lint" is undefined when no lint has ever run. _(`librarian-activation-friction.md §4`)_
- **Missing `log.md`** makes the activation "read the log" step silently no-op and the re-ingest grep error. _(`setup-friction.md §6`, `librarian-ingest-friction.md §2`)_ — the one *hard* gap in this family (file absent → errors), as opposed to the soft "valid file, undefined behavior" gaps.
- The contrast is instructive: the **Librarian's warm-thread activation visibly outperformed the Researcher's cold start** in the same trial — strong evidence the thread mechanism delivers *once seeded*; it just has nothing to say about the seeding moment. _(`librarian-activation-friction.md` "what worked")_
- Lint's no-baseline case is the exception that's **already gracefully handled** (falls back to full mode and says so). _(`lint-friction.md §4`)_

**Backlog status:** `log.md` scaffolding at setup is **filed**. The persona cold-start guidance is **not**.

---

## Theme 5 — Mint persistence & registration fragility

The self-evolution engine works (a partner was minted live and loaded), but its durability rests on undocumented assumptions and its registration is a hand-edited fan-out.

- **A divergent plugin-cache copy of the module shadows every mint.** Mints land in the project `.claude/skills/` tree; a full pristine copy also lives in the plugin cache, and the two diverge the instant a mint lands (verified by size + inode). Risks: a plugin refresh could **silently revert** any mint, and **subagents (incl. review-council lenses) resolve files to the cache** — so the gate can review pre-mint state. _(`mint-friction.md §1`, `review-council-friction.md §3`)_
- **The "new partner" path omits capability migration** — exactly the case this mint hit (the Creative took `vlt-extract` from the Librarian). Inferred from the council verdict, not the skill; a careless pass leaves two partners claiming one op. _(`mint-friction.md §2`)_
- **Registration is a manual fan-out across 5+ files**, and the two `module-help.csv` files use **different quoting styles** so a copied row is malformed unless reformatted. _(`mint-friction.md §3`)_
- **The council has no real invocation mechanism** — "run it via `vlt-review-council`" has no sanctioned way for one skill to call another and get a value back, so the caller *reimplements* the council from its prose; two operators could gate the same mint via materially different procedures. And a mint verdict's reasoning survives only if the caller chooses to record it. _(`review-council-friction.md §1, §4`)_

**Backlog status:** the **mint persistence model** and the **registration helper + single-source gate table** are both **filed**. The council-invocation mechanism and verdict-capture requirement are **not**.

---

## Theme 6 — Observability gaps for a parser / future dashboard

Small individually, but they compound for anything that consumes the `{log}` or note structure programmatically.

- **Orphan operation-entries are an expected intermediate state** (a mid-session `ingest`/`research` log line with no closing session note yet) — seen in three docs, correct by design, but undocumented, so a completeness sweep would flag healthy state as corruption. _(`librarian-ingest-friction.md §6`, `research-friction.md §6`, `researcher-activation-friction.md §4`)_
- **Double-homed facts with no source of truth:** the Tavily tool preference lives in the Researcher's `## Bond` *and* global memory *and* would have to be relayed by hand to reach the Librarian — because per-partner Bonds don't share. The real fix is a **shared user-level preferences home** distinct from the relationship `## Bond`. _(`researcher-activation-friction.md §6`, `librarian-activation-friction.md §6`, `partner-handoff-friction.md §5`)_
- **`files_checked` has no counting rule** (assessed vs. opened), and **a handled contradiction has no report slot** — a well-managed disagreement vanishes into an empty list, undercutting the skill's own "contradictions are features" ethos. _(`lint-friction.md §3, §5`)_
- **`sources:` frontmatter vs. the prose Sources section** duplicate every URL with nothing checking them against each other — a future lint rule could diff them. _(`research-friction.md §4`)_

**Backlog status:** none filed; shared-preferences home is the notable candidate.

---

## Recurring papercuts (low-severity, cross-flow)

- **Timestamp shelling-out** (`date +…`) for every datetime-prefixed filename — the harness exposes the date but not seconds. Hit in every write flow; deserves a one-line shared-convention note ("mint timestamps from a real clock, not the context date") rather than per-skill rediscovery. _(`librarian-ingest-friction.md §4`, `research-friction.md §5`)_
- **Frontmatter constant-field slip** — `author: agent` / `trust: raw` dropped on first write, caught by the checklist; a pre-filled copy-paste block would prevent rather than catch it. _(`librarian-ingest-friction.md §8`)_
- **`last_updated` bump threshold is fuzzy** and same-day edits make it invisible. _(`lint-friction.md §2`)_
- **`vlt-verification/` is unmapped** — writing here is a (correct) inference that the agent zone permits ad-hoc owned artifacts outside the named map. _(`librarian-ingest-friction.md §5`)_
- **A governance contradiction:** the contract says backlog capture is autonomous ("never gated, never silent") but the Researcher (and the trial prompt) ask-first. File-then-announce vs. propose-then-file is unresolved. _(`researcher-activation-friction.md §5`)_

---

## What consistently worked — the load-bearing wins to preserve

The feedback loop needs the positives, and several recur across every doc:

- **Supersession discipline is the standout.** The `[!superseded]` (refined) callouts let the `cortisol` page *tighten* the `ashwagandha` page without erasing it — a second source made a first page visibly more honest. This is the wiki **compounding**, not just accumulating: the module's core promise, demonstrably working.
- **The four-read activation ritual orients fast** — index → log → backlog → thread gave a clean "fresh vault, one source, no relationship" read every time.
- **The conventions are truly single-source** — `frontmatter.md` as the one schema home meant no reconciling competing field lists.
- **The research-vs-wiki distinction makes the shaping decision trivial** — "what did this source say" → dated note; "what do we know" → canonical page. No agonizing.
- **Verification checklists are load-bearing, not ceremonial** — they caught their own gaps (the frontmatter slip) every pass.
- **The single-writer contract held under hand-off** — the Researcher built knowledge, the Librarian filed it, neither crossed the line. The division of labor is real, not nominal.
- **The personas are genuinely good to inhabit** — "push, don't serve" (Researcher) and "contradictions are features" (lint) actively changed behavior for the better and stopped failure modes (empty contrarianism, forced resolution).
- **The mint scaffold is turnkey** and the council's *output* (single-axis lenses, four-section verdict) is high-signal.

---

## Backlog reconciliation

**Already filed (module-friction items):**

1. Mint persistence model vs. plugin cache — Theme 5 _(maintenance)_
2. Mint registration ergonomics + single-source gate table — Themes 5 & 1 _(maintenance)_
3. `vlt-setup` scaffolds `{log}` — Themes 4 & 1 _(maintenance)_
4. Index-structure convention (must also pin + gate the source-count definition) — Theme 1 _(maintenance)_

_(Also open but not module-friction: the Creative's HTML/PARA-boundary capability-gap, and the cortisol hyper/hypo knowledge-gap.)_

**Surfaced by this synthesis but NOT yet filed — candidates, in rough leverage order:**

- **Define the hand-off as an explicit session boundary + a minimal payload schema** (Theme 2) — reconciles a contract contradiction and makes the roster's defining mechanism robust. *Highest-value unfiled item.*
- **One reusable "partner-fronted skill" mode-note** for every elicitation phase (Theme 3) — the most-corroborated pattern (3 flows), one cheap cross-skill fix.
- **A shared user-level preferences home** distinct from per-partner `## Bond` (Themes 6 & 2) — closes a double-homing / silent-stripping risk.
- **Persona cold-start guidance** for the guaranteed once-per-vault empty activation (Theme 4).
- Smaller: timestamp-from-clock convention note; council-invocation mechanism + verdict capture; resolve autonomous-capture vs. ask-first; `files_checked` definition + handled-contradiction report slot.

I have **not** filed any of these — per the trial discipline, that's your call. The hand-off pair and the partner-fronted mode-note are the two I'd file first if you say go.

---

_Net: ten passes, zero hard failures — the module works, and the friction is uniformly the cheap, specify-it-away kind. The ~45 points collapse to six themes, and two carry the leverage: **structure-by-inference gaps** (Theme 1 — rules that survive only because one writer keeps them consistent) and **the under-specified hand-off seam** (Theme 2 — the roster's defining mechanism, least defined). The unifying diagnosis: the module is written for its happy path — one writer, one conversation, a warm and populated vault — and the friction is concentrated exactly where that happy path's assumptions get stressed (scale, partner hand-off, cold start). Four fixes are already backlogged; the highest-value unfiled candidate is to specify the hand-off (session boundary + payload). The supersession discipline and the compounding wiki are the wins most worth protecting as the fixes land._
