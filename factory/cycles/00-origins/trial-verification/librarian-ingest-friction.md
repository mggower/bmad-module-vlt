# Librarian Activation & Ingest — Verification Notes

_Friction observed running the **Librarian** persona (`/vlt-agent-librarian`) and a first **`vlt-ingest`** on the fresh `vlt-core` vault, 2026-06-03. For module iteration. Sibling to `setup-friction.md` (which covers `vlt-setup`)._

Both the activation ritual and the ingest completed cleanly — first source filed (research note + new `ashwagandha` wiki page + index + log), verification checklist passed, no broken mechanisms. The notes below are friction/ambiguity that required a judgment call or a workaround, ordered roughly by impact. A "what worked" section follows for balance.

## 1. `config.yaml` carries no `vault_structure` map at all

The operating contract and every SKILL.md lean hard on "resolve every path through the `vault_structure` map — an explicit override wins, else the shipped default." But the installed `_bmad/config.yaml` `vlt:` section holds only `name` / `description` / `version` — **there is no `vault_structure` key**. So there are zero overrides; every path resolved to the shipped default by necessity.

This *worked* (the fallback is well-defined), but it means the much-emphasized override mechanism is currently invisible/untestable on a real installed vault, and an agent has to know the defaults from the contract rather than read them from config. Worth confirming this is intended (defaults-only until a user customizes) vs. setup being expected to write the full map.

**Suggested fix:** either have `vlt-setup` materialize the default `vault_structure` map into `config.yaml` (so it's inspectable and overridable in one place), or add a line to the activation rituals: "config will usually omit `vault_structure`; treat the contract's default table as the live map."

## 2. The activation ritual reads `{log}`, but on a fresh vault the log doesn't exist

Activation step 2 is "read recent `{log}`." On a just-set-up vault, `_agent/log.md` **did not exist** — `vlt-setup` scaffolds the wiki index, backlog, and partner threads, but not the log. The Librarian's Init step explicitly ensures `thread.md` and `{backlog}` exist, but **says nothing about the log**. I created `log.md` lazily on the first ingest write.

Two consequences: (a) the activation "read the log" step silently no-ops on a fresh vault, and (b) the ingest **Step 1 re-ingest check** (`grep ... {log}`) would error on a missing file if run literally — I skipped it knowing the vault was empty, but a naive pass would hit a grep error.

**Suggested fix:** have `vlt-setup` (or the partner Init step) create an empty `log.md` with a header, alongside the backlog. And/or make the re-ingest grep tolerant of a missing log (`grep ... {log} 2>/dev/null`).

## 3. Interactive-vs-headless is ambiguous when the Librarian fronts an ingest after a one-word "yes"

`vlt-ingest` **Step 4** wants the agent to "surface the 3–5 most significant claims… ask the user what to emphasize… keep it to a couple of exchanges" *before* writing. But the user's instruction was simply "yes ingest the new source" — a one-shot directive with no appetite signalled for a back-and-forth. I judged it a clear single-source / single-concept case, surfaced takeaways **and** my wiki-shaping plan, and proceeded to write in the same turn without waiting for a reply.

That was a guess about which mode I was in — the same interactive-vs-non-interactive ambiguity flagged in `setup-friction.md §1`, but for ingest. The skill doesn't say how a Librarian-fronted "yes, ingest" should resolve: pause for confirmation, or proceed and present?

**Suggested fix:** add a mode rule to `vlt-ingest` Step 4 — e.g. "If invoked headless or via a direct 'ingest this' with no request to deliberate, surface takeaways + the shaping plan and proceed in one pass, presenting the result for review rather than blocking on it. Reserve the multi-exchange discussion for explicitly interactive sessions."

## 4. Precise timestamp for filenames requires shelling out mid-flow

Research-note and session-log filenames mandate a `YYYY-MM-DD-HHmmss` prefix "collision-safe." The harness exposes today's date in context, but not seconds — so I had to run `date +"%Y-%m-%d %H:%M:%S"` to mint the filename. Minor, but it's an extra step every ingest/research/session pays, and a forgetful agent could reuse the context date with a guessed time and risk collision.

**Suggested fix:** non-blocking — just note in the skills that the precise timestamp must come from a real clock read, not the context date. (Already implicit, never stated.)

## 5. `vlt-verification/` is unmapped — writing here is a judgment call

This very folder, `_agent/vlt-verification/`, is **not** in the `vault_structure` map. Recognizing that writing here is legitimate (it's under `_agent/`, the agent-owned zone, and not a governed wiki page) was a small inference. An agent over-indexed on "only write to mapped locations" might balk. Fine as-is given the trial context, but worth a one-liner that the agent zone permits ad-hoc owned artifacts outside the named map.

## 6. Mid-session, a log entry exists with no session note (by design — but an observability gap)

Per the session-ownership rule, `vlt-ingest` appends its own `ingest` log entry but **must not** write a session note — the Librarian owns one session note for the whole sitting, written at close. Correct and well-reasoned. But it means that *right now*, mid-session, there is an `ingest` log line and **no** session note. If a session is abandoned before the Librarian closes it, the log shows an operation with no session record. Acceptable, but a real edge for anyone parsing the log for completeness.

**Suggested fix:** none needed functionally — possibly note that an orphan operation-entry without a closing session note is an expected intermediate state, so a future dashboard/lint doesn't flag it as corruption.

## What worked well (for balance)

- **The activation ritual is genuinely orienting.** Index → log → backlog → thread gave a clean, fast read of "fresh vault, one unintegrated source, no prior relationship" — I knew exactly where I stood and what the obvious next move was.
- **The conventions are clear and truly single-source.** `frontmatter.md` as the one schema home worked — I never had to reconcile competing field lists. The "no `key:` field" and wikilink-quoting rules are specific and checkable.
- **The research-vs-wiki distinction made the shaping decision easy.** "What did this source say" → dated research note; "what do we know about this concept" → canonical `ashwagandha` page. No agonizing over where things go.
- **Stub wikilinks handled the fresh-vault case gracefully.** The checklist's "resolve to an existing page **or** be explicitly flagged as a new stub" let me link `[[adaptogens]]` / `[[cortisol]]` honestly without splintering thin pages or leaving dead links — and the index has a clean place to list them.
- **Supersession discipline had nothing to do yet (first source) but the framing is sound** — additive-vs-superseding is a clear test for the next ingest that touches these pages.
- **The verification step caught its own gaps.** Re-reading each artifact against the explicit checklist before reporting is the right discipline and felt load-bearing, not ceremonial.

---

_Net: the Librarian + ingest path is solid and the persona/convention design is genuinely good to operate inside. The friction is concentrated in **fresh-vault edge cases** (missing log file, empty `vault_structure`, re-ingest grep on a nonexistent log) and the same **interactive-vs-headless ambiguity** that setup surfaced — none of it broke anything, all of it is cheap to specify away._

---

## Pass 2 — 2026-06-03 (ingest of a Researcher hand-off, `cortisol` research note)

Second ingest pass, this time integrating an **agent-authored research note** handed off by the Researcher (not a `sources/` file). Completed cleanly — new `cortisol` page, two `[!superseded]` (refined) callouts on `ashwagandha`, index updated, verification passed after one fix. New friction below; numbering continues from Pass 1.

### 7. `vlt-ingest` Step 5 has no branch for "the source is already an `_agent/` artifact" (research-note hand-off)

Step 5 mandates writing a `{research}/...` note — "the dated snapshot of *what this source said*." But the input here **was** a research note (the Researcher's cortisol dive). Following Step 5 literally would have produced a **research-note-of-a-research-note** — a duplicate dated snapshot of an existing dated snapshot. I **skipped Step 5** and treated the existing note as the snapshot it already is, going straight to the wiki update (Step 6).

The skill is written for *external raw material* (a `sources/` file, URL, or pasted text) and Step 3 ("Read the source… in the sources layer") reinforces that assumption. But the **research → ingest hand-off is a first-class, documented flow** (`vlt-research` Phase 6 explicitly hands the note to the Librarian/`vlt-ingest`). So the most-blessed way knowledge moves from the Researcher to the wiki hits a step that doesn't fit it.

**Suggested fix:** add a branch to Step 5 — "If the source is already an `_agent/{research}` note (a partner hand-off), skip creating a new research note; that note *is* the dated snapshot. Proceed to Step 6, and cite the existing note as the contributing source on any wiki page you touch." Possibly also soften Step 3's "in the sources layer" to include agent research notes as a valid input class.

### 8. Frontmatter omission slipped through initial write — caught only on Step 9 re-read

Writing the new `cortisol` page, I **omitted `author: agent` and `trust: raw`** from the frontmatter on the first pass — they're easy to drop because they're the two *constant* fields (always the same values for an agent wiki write), so attention goes to the variable fields (`topic`, `status`, `sources`). The Step 9 verification re-read caught it and I fixed it before closing.

Working-as-intended (the checklist did its job), but it's a recurring human-style slip the checklist *catches* rather than *prevents*. **Suggested fix:** non-blocking — consider a copy-paste frontmatter block in the skill with `author: agent` / `trust: raw` pre-filled (rather than the field-list-with-placeholders), so the constant fields are present by default and only the variable ones need editing.

### 9. The index's body structure is defined nowhere — categories, row format, and the `## Stubs` section are all per-ingest inference

`vlt-ingest` Step 7 is the *only* specification for how the index is organized, and it's loose: "add new pages (one-line description + source count)… adjust categories as the wiki grows." There is **no index-structure convention** in `{conventions}/` (which defines frontmatter, extraction, consolidation, supersession — but not the index body; `frontmatter.md` covers only the index's *frontmatter*). So everything about the index's *organization* is inferred per ingest:

- **Category sections** (`## Health & Supplements`, `## Endocrinology & Physiology`) — I had to decide whether `cortisol` warranted a new category or belonged under the existing `Health` one. Pure judgment; a different pass could split/merge categories differently each time. No naming guidance, no granularity rule.
- **Row format** (`- [[page]] — description (N sources)`) — shown by example in the live index, specified nowhere. Easily mimicked, but mimicry is what lets it drift.
- **The `## Stubs (linked, not yet written)` section is entirely emergent.** "stub" appears in the skills only as the *concept* of an unwritten wikilink target (ingest checklist; lint "missing targets"/"needed stub") — never as an index section. The dedicated stubs-tracking heading is a genuinely useful convention the Librarian invented, surviving **only by mimicry**. A future ingest could silently drop it, rename it, or stop maintaining it.

This is **not** a setup gap (setup correctly scaffolds a *minimal valid* index — frontmatter + placeholder — and is right not to impose a taxonomy on an empty vault) and **not** an activation gap (activation only reads the index, which works). It is a **convention gap** owned by `vlt-ingest` Step 7 (the writer) and `vlt-lint` (the validator). The single-writer contract *masks* it — one skill maintaining the index keeps it roughly self-consistent — but with no canonical definition there are two real consequences:

1. **`vlt-lint`'s index-drift check is under-powered** — it validates pages-present and source-count-accuracy (§ "Index drift"), but it *cannot* validate category placement or the stubs section, because there's no defined structure to check against. It catches a missing row, not a miscategorized or malformed one.
2. The useful stubs convention is undocumented and fragile.

Contrast with the `log.md` finding (`setup-friction.md §6`): that was a *hard* gap (file absent → errors); this is a *soft* gap (a valid file whose internal organization is unspecified and drifts by inference). Easily inferred enough to never break — but not specified enough to stay consistent as the wiki scales or if the single-writer assumption ever loosens.

**Suggested fix (module-direct):** author an **index-structure convention** in `{conventions}/` (e.g. `wiki-index.md`) defining: the category-section model (and how categories are named/created/collapsed), the canonical row format (`- [[page]] — one-line description (N source[s])`), and the `## Stubs (linked, not yet written)` section as a blessed convention. Point `vlt-ingest` Step 7 and `vlt-lint`'s index-drift check at it, so the writer has a spec and the validator has something to check against. Filed to `{backlog}` as `maintenance`.

> **Addendum — confirmed from the lint seat (2026-06-03, `vlt-lint` pass; see `lint-friction.md §1`).** Running lint over this same index turned the soft gap above into an **active wrong-direction mutation**, and sharpens one claim in this section. §9 lists *"source-count-accuracy"* as something `vlt-lint` **can** validate (consequence 1, contrasted with category/stubs which it can't). The lint run shows it **can't validate that either** — and worse, the skill grants it **auto-fix authority** over source counts (Step 3: *"update source counts"*, no human gate). `cortisol` showed `(1 source)` in the index against an 11-entry frontmatter `sources:` list. With no convention defining what the count *counts*, I reverse-engineered "count = length of frontmatter `sources:`" from `ashwagandha` (the one page that agreed with itself) and auto-changed cortisol `1 → 11`. But `(1 source)` plausibly meant "built from **1 research note**" (which itself synthesizes 21 underlying sources) — under that reading my "fix" *introduced* drift rather than removing it. So the source count isn't a safe auto-fix; it's the **same undefined-spec gap as the row format and stubs section**, just with the validator empowered to mutate on a guess. The convention proposed above should therefore pin the count's definition explicitly (e.g. *"index source count = number of entries in the page's frontmatter `sources:`"*); until it lands, the cheap interim is to **demote source-count correction from auto-fix to flag-for-human** so the guess surfaces to a human instead of being silently applied. No separate backlog item needed — this folds into the index-structure-convention item already filed, as a "must also define the source count, and gate it until then" sub-point.

### What worked well (Pass 2)

- **Supersession discipline is excellent in practice.** The `[!superseded]` (refined) callouts let me tighten the `ashwagandha` cortisol claims *without erasing* the original figures — the page now shows its own evolution, which is exactly the intellectual-honesty goal. This is the convention's best moment so far: a second page arriving made a first page *more honest*, visibly.
- **Near-duplicate check was fast and unambiguous** — `cortisol` vs. `ashwagandha` are plainly distinct concepts; no agonizing, no false merge.
- **The hand-off args carried everything I needed** — source path, specific tasks, supersession instruction, even the tool preference. The Researcher → Librarian boundary felt like real division of labor, not ceremony.

_Net (Pass 2): two new structural findings — **#7, ingest's Step 5 doesn't fit the research-note hand-off** (a primary documented flow), and **#9, the index's body structure is defined nowhere** (categories, row format, and the emergent `## Stubs` section all survive by inference; the single-writer contract masks the drift, and `vlt-lint` can't validate what isn't specified). Both backlogged as `maintenance`. The frontmatter slip (#8) is the checklist working. Supersession + near-duplicate discipline remain the standouts._
